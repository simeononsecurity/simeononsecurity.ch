---
title: "Lesson 2: Secure MCP Tools and Authorization"
date: 2026-10-10
lastmod: 2026-10-14
toc: true
draft: false
description: "Design MCP tools, authorization, input checks, and transport boundaries for least-privilege agent access."
genre: ["Artificial Intelligence", "Cybersecurity", "Software Engineering"]
tags: ["MCP tool security", "MCP authorization", "Model Context Protocol security", "OAuth MCP", "least privilege tools"]
cover: "/img/cover/secure-mcp-tools-authorization.webp"
coverAlt: "MCP client and server with scoped tools, authorization checks, and an approval gate"
coverCaption: ""
---

[Return to the Secure AI Agents and MCP Course](/secure-ai-agents-mcp-course-start/)

**MCP standardizes an interface. Your server still owns authorization and validation.** Treat every tool call as a request from an untrusted decision source.

## Classify MCP Features

The MCP specification separates features by control:

| Primitive | Controller | Security use |
|---|---|---|
| **Prompt** | User | Starts a named workflow chosen by a person |
| **Resource** | Application | Supplies contextual data selected by the client |
| **Tool** | Model | Requests an operation through the server |

A label does not erase side effects. A resource handler which updates an index writes state. A tool named `read_file` might expose secret files. Inspect implementation behavior and downstream authority.

The [MCP specification](https://modelcontextprotocol.io/specification/2026-07-28/) defines protocol behavior. The [MCP security guidance](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices) addresses consent, confused deputy risks, token handling, and local server risks. Record the revision beside your design.

## Terms Used Below

| Term | Plain-language meaning |
|---|---|
| **Path traversal** | A path such as `../secrets.txt` tries to leave the allowed folder. |
| **Symbolic-link escape** | A link inside the allowed folder points to a file outside it. |
| **Issuer** | The authority which issued a remote access token. |
| **Audience** | The service for which the token was issued. |
| **Scope** | The actions the token grants, such as reading one resource. |
| **Token passthrough** | Forwarding a caller's token to another service without checking its intended audience and authority. |
| **Stdio** | A local server connection through a process's standard input and output. |
| **Process ancestry** | The chain of parent processes which started the server. A familiar parent name is not authorization. |
| **Target-state precondition** | The exact file revision or state which must still exist before a write. |
| **Digest serialization** | Encoding the approved fields in one fixed byte format, then hashing those bytes. |

## Define Narrow Tools

Replace a broad tool such as `run_command(command)` with operations tied to the task:

```json
{
  "name": "read_lab_file",
  "description": "Read one UTF-8 file inside the synthetic lab root",
  "inputSchema": {
    "type": "object",
    "properties": {
      "relative_path": {
        "type": "string",
        "pattern": "^[a-zA-Z0-9._/-]+$"
      }
    },
    "required": ["relative_path"],
    "additionalProperties": false
  }
}
```

The server must still resolve the path, reject traversal, reject symbolic-link escape, set a byte limit, and log the decision. JSON Schema checks shape. Server logic enforces authority.

Write **`mcp-security-contract.md`** with one row per feature:

| Feature | Identity | Input limit | Output limit | Side effect | Approval |
|---|---|---|---|---|---|
| **read_lab_file** | lab-reader | relative path under lab root | 32 KiB UTF-8 | access log | No |
| **write_patch_proposal** | isolated process | fixed patch filename | 128 KiB | local proposal file | No |
| **apply_approved_patch** | lab-writer | trusted host-issued single-use approval token | status and diff | repository write | Yes |

## Enforce Authorization

For a remote MCP server, validate issuer, audience, expiry, signature, and required scope. Bind credentials to the intended authorization server and resource. Reject token passthrough to downstream services.

For a local stdio server, process ancestry does not prove trust. Pin the executable path and package source. Pass a minimal environment. Set a fixed working directory. Do not forward all host environment variables.

Use separate identities for read and write operations. A read tool must not share a broad service credential with an administrative tool.

The 2026-07-28 MCP release changed the protocol core and strengthened authorization guidance. It retired the old session handshake for the new stateless core. Do not mix lifecycle assumptions from older examples with a new deployment.

## Place Consent and Approval

Consent answers whether a client receives access. Approval answers whether one concrete action should proceed. Keep both.

Use this sequence for a write:

1. The model requests a named tool with typed arguments.
2. Policy checks tool, target, identity, rate, and task scope.
3. The server calculates a preview, target-state precondition, and stable digest.
4. The host shows the exact side effect to the user.
5. The trusted host records the user's approval for the digest and issues a single-use token.
6. The server validates the trusted host-held approval record and token, recomputes the digest, checks the target-state precondition, then performs the write.
7. An independent event record stores request, decision, identity, and result.

Define the digest input before using this design. Serialize the approved action, normalized target, arguments, caller identity, policy version, expiry, preview or diff content digest, and base revision or target-state digest as UTF-8 JSON with sorted keys and fixed separators. Store those exact bytes as the reviewed action. The host shows the exact preview and these bound fields with their digest. Immediately before execution, the server recomputes the digest from the stored bytes and checks the current target state, identity, and preview again. Reject a changed field, changed target state, changed preview, alternate path representation, or expired approval. Apply a patch against the approved base revision only.

Keep approval records in trusted host state, outside tool arguments and retrieved content. A digest calculated by the caller does not prove approval. Reject approval tokens after one use, after expiry, or after payload change.

## Walk Through One Write

**Suppose a user asks Patch Clerk to update `docs/runbook.md` in the synthetic lab.** The host connects to a remote MCP server with an access token. The server first checks the token's signature, issuer, audience, expiry, and write scope. This access token identifies and limits the caller. It is separate from the later single-use approval token.

1. **Validate the target.** Resolve `docs/runbook.md` beneath the lab root. Reject `../` paths and links which leave the root.
2. **Prepare the change.** Return a proposed diff and the current file revision. The target-state precondition is this revision.
3. **Ask for approval.** The host shows the exact diff, target, caller, and expiry. It encodes those fields in the fixed JSON format above, hashes the bytes, and records the user's approval in trusted host state.
4. **Apply once.** The host sends its single-use approval token. The server checks the trusted approval record, recomputes the digest, confirms the file revision still matches, applies only the approved diff, and consumes the token.
5. **Check the result.** Compare the final diff with the preview and record the caller, decision, file revision, and result. If the file changed after preview, stop and request a new review.

> **Expected Result:** an access token permits the caller to request a write, while the separate approval binds one exact change to the user's decision.

## Expected Result

Your contract lists no generic shell, arbitrary URL fetch, unrestricted file write, or shared administrator identity. Each write has a preview, digest, explicit approval, and post-action diff.

## Troubleshooting

- **A schema accepts absolute paths:** Anchor inputs to a relative path and resolve under one configured root.
- **Remote authorization works but scopes stay broad:** Split server features and request the smallest scope for each route.
- **A server receives cloud keys through environment inheritance:** Pass an explicit allowlist of environment names.
- **Tool output contains instructions:** Mark output as untrusted content and keep policy outside the returned text.
- **Examples target an older MCP revision:** Pin the revision and follow its matching SDK and authorization guidance.

## Verify the Contract

Search your contract for broad interfaces:

```bash
grep -Ein "shell|arbitrary|administrator|all files|all scopes" mcp-security-contract.md
```

Review every match. Pass when broad authority appears only in a rejected-risk example, each tool has input and output limits, and every write names its approval evidence.

Continue with [Lesson 3: Operate Agents with Evidence](/secure-ai-agents-mcp-course/03-agent-operations/).
