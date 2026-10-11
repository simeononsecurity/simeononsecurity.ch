---
title: "AI Context Window Management: Keep Coding Agents Focused"
date: 2026-10-10
lastmod: 2026-10-10
toc: true
draft: false
description: "Control an AI task's active context with selected files, compact handoffs, and small worker outputs while preserving decisions and evidence."
genre: ["Artificial Intelligence", "Software Engineering"]
tags: ["AI context window management", "coding agent context", "AI handoff", "context compaction", "agent orchestration", "token budget"]
cover: "/img/cover/effective-ai-context-window-management.webp"
coverAlt: "A compact handoff note beside selected project files and a much larger discarded chat transcript"
coverCaption: ""
---

#### [Return to the Practical AI Workflows Course](/effective-ai-course-start/)

**A context window is the text and other material a model processes for the current turn.** Prompts, file excerpts, tool output, and conversation history consume space. This lesson shows how to keep the next task focused and leave a reliable handoff.

## Key Takeaways

- **Tokens** are the units a model uses to process input and output.
- **Active context** is the material available during one turn, subject to product limits.
- **Durable sources** live in files or project records outside the chat.
- **Compaction** summarizes or prunes older context and might omit a needed detail.
- **A handoff** points a fresh session to current sources and verified work.

## Before You Begin

**Prerequisites:** your edited lab from the [first coding-agent task](/articles/effective-ai-coding-agent-first-task/), its approved requirement, and the [task packet lesson](/articles/effective-ai-task-packets/). If you used the study route, use your manually edited lab. Set aside 35 minutes. Difficulty is intermediate. Keep course notes outside the extracted lab folder so `git status` still reflects code changes alone.

## Select Context by Task

**For the status-filter edit,** the agent needs `task_report.py`, `docs/requirements.md`, relevant tests, and a small sample from `tasks.json`. It does not need every old chat, all site documentation, or the complete Git history. Read a map first, then fetch the smallest files needed for the next decision.

| Task | Useful context | Excess context |
|---|---|---|
| **Define behavior** | Approved requirement and one data sample | Old exploratory conversations |
| **Edit program** | Program and focused tests | Unrelated project directories |
| **Review result** | Diff, test output, requirement | Full agent transcript |
| **Resume later** | Handoff note and source paths | A pasted multi-hour chat |

**This is a retrieval choice, not a rule to hide evidence.** If a test fails, include the exact failure output and the file involved. Remove irrelevant logs, not the details needed to diagnose the failure.

## Build a Compact Handoff

**A handoff is a short record for the next session.** It should distinguish work completed from work proposed. Save this example as `course-notes/handoff.md` outside the lab and replace the example observations with your own.

```text
Goal: Add --status open|done to the course task report.
Source: docs/requirements.md, revision 1.
Workspace: extracted effective-ai-course-lab folder.
Current state: status filter edit is present in task_report.py and tests.
Verified: record your observed test result and manual counts 4, 2, and 2.
Decision: tasks.json stayed unchanged.
Pending: independent diff and source review.
Next check: rerun tests and the invalid-status case.
Stop if: requirement or baseline differs from the record above.
```

**The example is not a claim about your run.** Enter your actual test output and changed-file list after working. If a source revision changes, update the handoff after rereading the source.

## Test a Fresh Session

**Start a new chat or coding-agent session** in the lab. Give it only `AGENTS.md`, the handoff, and permission to read named files. Ask:

```text
Using this handoff and the current repository files, name the approved
status values, the baseline count, and the next check. Do not edit.
If the handoff conflicts with a current source, report the conflict.
```

**Expected reasoning:** the fresh session finds `open` and `done` in `docs/requirements.md`, identifies the baseline count of 4, and names tests plus manual checks. If it repeats an old `pending` value, reread the requirement and correct the handoff.

## Keep the Orchestrator Small

**An orchestrator is the main agent coordinating workers.** Give each worker a narrow question and named input files. Ask for a compact output: finding, evidence path, confidence, and unresolved issue. Keep detailed logs in a file or the worker's own session. Bring back only the parts the main agent needs to decide the next step.

**Example:** ask one read-only worker to inspect tests and return “missing case, file and line, suggested check.” Do not ask it to paste every test file into the main chat. The main agent then verifies the finding in the repository before editing.

**Worker sessions have their own context in many products,** but inheritance and isolation differ. Check the product's current rules before assuming a worker sees the same instructions, files, or tools as its parent. The [Codex subagent guide](https://learn.chatgpt.com/docs/agent-configuration/subagents) and [Claude Code subagent guide](https://code.claude.com/docs/en/sub-agents) describe their own behavior.

## Use Compaction Carefully

**Compaction shortens active history.** Codex, Claude Code, and OpenCode differ in when and how they compact. Treat a compacted summary as an aid to continuation, not a complete project record. Keep requirements and decisions in files, then check them again after compaction. Review [Codex best practices](https://learn.chatgpt.com/docs/learn/best-practices), [Claude Code commands](https://code.claude.com/docs/en/commands), and [OpenCode 2 compaction](https://opencode.ai/v2/docs/compaction) for current controls. OpenCode 1 and OpenCode 2 use different compaction schemas. Check `opencode --version` before copying settings.

**If the assistant loses a constraint,** stop the edit, reopen the source, and restate the task packet. A new session with a short verified handoff often costs less attention than repeatedly correcting a confused long chat.

## Practice and Check

**Your artifact:** a handoff under 180 words, saved outside the lab. Mark each line as source, observed result, decision, or pending action. Give the handoff to a fresh session and record whether it names both accepted status values and the next check.

**Completion check:** the fresh session names `open`, `done`, the baseline count of 4, and a test step without relying on the old chat. Correct any missing item, then retest with another fresh session.

## Troubleshooting

- **Summary omits a decision:** add a short decision line and its source revision.
- **Huge worker response:** request a limited evidence table and file references.
- **Stale handoff:** reread current source files before another edit.
- **Context pressure continues:** split the task into smaller sessions with separate artifacts.

## Next Steps

**Continue with [MCP Server Setup](/articles/effective-ai-mcp-server-setup/)**. You will add a read-only external tool while keeping its output scoped.
