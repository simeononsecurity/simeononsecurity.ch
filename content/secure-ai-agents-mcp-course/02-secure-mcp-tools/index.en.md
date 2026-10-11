---
title: "Lesson 2: Secure MCP Tools and Authorization"
date: 2026-10-10
lastmod: 2026-10-10
toc: true
draft: false
description: "Design MCP tools, authorization, input checks, and transport boundaries for least-privilege agent access."
genre: ["Artificial Intelligence", "Cybersecurity", "Software Engineering"]
tags: ["MCP tool security", "MCP authorization", "Model Context Protocol security", "OAuth MCP", "least privilege tools"]
cover: "/img/cover/secure-mcp-tools-authorization.webp"
coverAlt: "MCP client and server with scoped tools, authorization checks, and an approval gate"
coverCaption: "Lesson cover placeholder. Image generation follows editorial review."
---

[Return to the Secure AI Agents and MCP Course](/secure-ai-agents-mcp-course/)

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
| **apply_approved_patch** | lab-writer | approved digest only | status and diff | repository write | Yes |

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
3. The server calculates a preview and stable digest.
4. The host shows the exact side effect to the user.
5. The user approves the digest.
6. The server verifies the digest again and performs the write.
7. An independent event record stores request, decision, identity, and result.

Reject approval tokens after one use, after expiry, or after payload change.

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
