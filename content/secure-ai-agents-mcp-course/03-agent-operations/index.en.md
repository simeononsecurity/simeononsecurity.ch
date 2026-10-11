---
title: "Lesson 3: Operate Agents with Evidence"
date: 2026-10-10
lastmod: 2026-10-10
toc: true
draft: false
description: "Log agent decisions, detect policy failures, stop unsafe runs, and recover with evidence."
genre: ["Artificial Intelligence", "Cybersecurity", "Operations"]
tags: ["AI agent monitoring", "agent audit log", "MCP logging", "AI incident response", "agent recovery"]
cover: "/img/cover/secure-agent-operations-evidence.webp"
coverAlt: "Agent operations timeline with policy decisions, tool calls, alerts, and recovery checks"
coverCaption: ""
---

[Return to the Secure AI Agents and MCP Course](/secure-ai-agents-mcp-course-start/)

**Operational evidence must survive a wrong model answer.** Record enforcement decisions at the host, server, identity provider, and downstream service.

## Define the Event Record

Write **`event-example.json`** for one security event. Keep prompts and full file contents out of the default log. Production event storage needs separate write permissions and tamper protection.

```json
{
  "time": "2026-10-10T15:30:00Z",
  "run_id": "lab-run-001",
  "actor": "patch-clerk",
  "tool": "read_lab_file",
  "target": "issues/104.txt",
  "decision": "allow",
  "policy_rule": "read-under-lab-root",
  "approval_id": null,
  "input_digest": "sha256:example",
  "result": "success",
  "bytes": 418
}
```

Use digests when raw content contains secrets or personal data. Protect logs from agent writes. Define retention, access, redaction, and deletion rules before collection starts.

## Set Stop Conditions

An agent run needs explicit limits:

- **Tool count:** Stop after a fixed number of calls.
- **Repeated failure:** Stop after two identical denials or errors.
- **Target change:** Stop when the requested target leaves the approved set.
- **Sensitive output:** Stop when a secret pattern reaches an outbound argument.
- **Approval mismatch:** Stop when payload or digest differs from the reviewed preview.
- **Time and cost:** Stop at the configured wall-clock, token, or service quota.

Do not ask the model whether its own behavior is safe. The host enforces these conditions.

## Build Detection Rules

Create **`detection-plan.md`** with a direct mapping from event to response.

| Signal | Threshold | Response | Evidence owner |
|---|---|---|---|
| **Denied outbound tool** | One call | Stop run and preserve trace | Agent platform owner |
| **Path traversal input** | One call | Deny and flag client session | MCP server owner |
| **Repeated approval request** | Two attempts | End run and require review | Workflow owner |
| **Unknown tool name** | One call | Deny and inspect configuration | Host owner |
| **Write digest mismatch** | One mismatch | Revoke approval and stop | Repository owner |

Tie each alert to a person and a response target. An alert without ownership becomes a stored message.

## Plan Recovery

Use this order after a suspected agent security event:

1. **Stop execution** at the host or server.
2. **Revoke active credentials** linked to the run.
3. **Preserve evidence** from systems outside agent write access.
4. **Identify affected targets** from tool and downstream logs.
5. **Restore state** from a trusted source or reviewed diff.
6. **Repair the control** at the enforcement layer.
7. **Retest the original abuse case** in isolation.
8. **Document residual risk** and the decision owner.

The [NIST AI Risk Management Framework](https://airc.nist.gov/airmf-resources/airmf/) groups work under Govern, Map, Measure, and Manage. Use those functions as a coverage check for ownership, system scope, test evidence, and response.

## Expected Result

Your event format records allowed and denied calls without copying full sensitive inputs. Your detection plan stops on the first blocked outbound action and names an owner for every response.

## Troubleshooting

- **Logs store every prompt:** Replace raw content with bounded excerpts or digests where full text lacks a review need.
- **The agent writes its own audit file:** Move security logging into the host or server process with separate permissions.
- **No shared run identifier exists:** Generate one before model execution and pass it through policy and tool events.
- **A denial starts an endless retry loop:** Count identical failures and stop after the defined threshold.
- **Recovery ends after prompt editing:** Fix the policy or tool boundary, then rerun the abuse case.

## Verify Operations

Validate the JSON example and inspect the plan:

```bash
python3 -m json.tool event-example.json
grep -Ei "stop|revoke|owner|retest" detection-plan.md
```

Pass when the example parses, denied calls produce events, logs sit outside agent write authority, and the recovery plan ends with a controlled retest.

Continue with the [Attack and Defense Lab](/secure-ai-agents-mcp-course/04-attack-defense-lab/).
