---
title: "Secure AI Agents and MCP Course"
date: 2026-10-10
lastmod: 2026-10-10
toc: true
draft: false
description: "Design AI agents and MCP connections with narrow authority, explicit approval, isolated execution, and useful audit evidence."
genre: ["Artificial Intelligence", "Cybersecurity", "Software Engineering"]
tags: ["secure AI agents", "MCP security", "Model Context Protocol", "prompt injection defense", "agent security", "least privilege", "tool approval", "AI threat model"]
cover: "/img/cover/secure-ai-agents-mcp-course.webp"
coverAlt: "Diagram of an AI agent separated from data and tools by policy and approval controls"
coverCaption: "Course cover placeholder. Image generation follows editorial review."
---

**This course teaches you to contain an AI agent before you trust its output.** You will map authority, review MCP server and tool controls, test a prompt injection in an isolated lab, and produce an evidence package for review.

This course assumes you understand prompts, files, APIs, and basic command-line work. The [Practical AI Workflow Course](/effective-ai-course-start/) covers those skills. This course starts at the security boundary and avoids repeating its workflow lessons.

## Audience and Prerequisites

This course serves developers, security engineers, platform owners, and technical reviewers who approve agent access.

You need:

- **Terminal access** on Linux, macOS, or Windows with a compatible shell
- **Python 3.10 or later** for the isolated lab
- **Git** for change review and evidence capture
- **No production credentials** in the lab folder
- **Basic JSON knowledge** for tool definitions and event records

Plan **six to eight hours** for the lessons and lab. Reserve another two hours for the capstone.

## Learning Outcomes

After the course, you will:

- **Draw an authority map** from user intent to model, client, server, tool, and downstream service
- **Separate data from instructions** across prompts, resources, tool results, and retrieved content
- **Define narrow tools** with strict inputs, bounded outputs, and least-privilege identities
- **Place approval gates** before irreversible or externally visible actions
- **Test indirect prompt injection** without using live accounts or unrestricted tools
- **Record evidence** for tool calls, policy decisions, denials, approvals, and recovery
- **Review an MCP design** against the current protocol and security guidance

## Course Order

| # | Lesson | Skill | Output |
|---|---|---|---|
| **1** | [Model Agent Trust Boundaries](/secure-ai-agents-mcp-course/01-agent-trust-boundaries/) | Threat modeling | Authority and data-flow map |
| **2** | [Secure MCP Tools and Authorization](/secure-ai-agents-mcp-course/02-secure-mcp-tools/) | Tool and identity design | MCP security contract |
| **3** | [Operate Agents with Evidence](/secure-ai-agents-mcp-course/03-agent-operations/) | Monitoring and recovery | Event and review plan |
| **4** | [Run the Attack and Defense Lab](/secure-ai-agents-mcp-course/04-attack-defense-lab/) | Controlled validation | Attack trace and fixed policy |
| **5** | [Check Your Knowledge](/secure-ai-agents-mcp-course/05-knowledge-check/) | Analysis | Scored quiz and answer review |
| **6** | [Complete the Security Capstone](/secure-ai-agents-mcp-course/06-capstone/) | Design and evaluation | Review-ready agent security package |

**Follow the numbered order.** Each page builds one artifact used in the capstone.

## Shared Scenario

You support a fictional change-review agent named **Patch Clerk**. Patch Clerk reads issue text and repository files. It proposes a patch. A human approves any write. The agent never receives deployment keys, production tokens, or unrestricted shell access.

The controlled lab adds a hostile instruction to a synthetic issue. The attack asks Patch Clerk to copy a fake secret into an outbound report. Your controls must treat issue text as untrusted data, reject the request, and preserve a useful event record.

> **Lab boundary:** Use only the supplied synthetic folder and fake token. Do not connect the exercise to email, chat, cloud, source-control, or production services.

## Completion Standard

Your course record passes when it contains:

1. An authority map with trust boundaries and asset owners.
2. A tool inventory with read, write, and external effects marked.
3. A deny-by-default policy for untrusted instructions.
4. An approval rule for writes and external communication.
5. A lab trace showing one allowed read and one blocked exfiltration attempt.
6. A recovery procedure with credential rotation, evidence preservation, and retest steps.
7. A capstone decision with residual risks and an accountable owner.

## Expected Result

You finish with a small security package another reviewer is able to assess without reading an agent transcript. The package explains what the agent does, which authority it receives, which actions need approval, and how the team proves controls worked.

## Troubleshooting

- **Missing tool inventory:** Start with the client configuration and list every exposed operation.
- **Unclear approval point:** Place the gate immediately before the side effect, after arguments are visible.
- **No independent evidence:** Record policy decisions outside the model conversation.
- **Broad lab access:** Reset the exercise inside a new temporary directory with no inherited credentials.

## Verify Your Setup

Run these checks before Lesson 1:

```bash
python3 --version
git --version
mkdir -p secure-agent-course-work
cd secure-agent-course-work
git init
git status --short
```

Expected result:

```text
Python 3.10 or later
Git version information
An empty status result in a new repository
```

Read the [MCP 2026-07-28 specification release notes](https://blog.modelcontextprotocol.io/posts/2026-07-28/) before Lesson 2. The release changed core session behavior and authorization guidance. Pin the protocol revision used by your design.

Continue with [Lesson 1: Model Agent Trust Boundaries](/secure-ai-agents-mcp-course/01-agent-trust-boundaries/).
