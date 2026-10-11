---
title: "AI Agent Delegation: Split Tasks, Assign Roles, and Review Results"
date: 2026-10-10
lastmod: 2026-10-10
toc: true
draft: false
description: "Decide when a second AI agent helps, give each worker a bounded task, prevent edit conflicts, and integrate evidence in the main session."
genre: ["Artificial Intelligence", "Software Engineering"]
tags: ["AI agent delegation", "subagents", "worker agents", "orchestrator context", "AI worktrees", "parallel AI tasks"]
cover: "/img/cover/effective-ai-agent-delegation.webp"
coverAlt: "A main agent assigning separate research and test review tasks before combining short evidence reports"
coverCaption: ""
---

#### [Return to the Practical AI Workflows Course](/effective-ai-course-start/)

**Delegate when a task has independent parts with clear outputs.** A worker agent inspects sources, reviews tests, or drafts a bounded change in its own session. The main agent still checks and integrates the result. This lesson starts with read-only work so you learn the handoff before handling concurrent edits.

## Key Takeaways

- **Orchestrator:** the main agent coordinating the task and final review.
- **Worker:** a separate agent assigned one bounded result.
- **Independent work:** a subtask whose answer does not depend on another worker's unfinished output.
- **Ownership:** a named file or question assigned to one worker.
- **Integration:** the main agent's comparison of worker output with current sources.

## Before You Begin

**Prerequisites:** a fresh extraction of the starter lab for Worker A, with the original two baseline tests, [context handoff](/articles/effective-ai-context-window-management/), and [output verification](/articles/effective-ai-output-verification/). Set aside 40 minutes. Difficulty is intermediate. An agent product with subagent support is useful for the hands-on route. The no-cost route uses two separate chats and manual integration.

## Decide Whether to Delegate

**Use one agent** for a small sequential edit. Delegation has setup, token, and review cost. Use a worker when a read-only question is independent and its answer would otherwise fill the main chat with many files or source pages.

| Lab task | Delegate? | Reason |
|---|---|---|
| **Add a two-value filter** | Usually no | One small file and focused tests |
| **Find missing test cases** | Yes, read-only | Separate review question and short report |
| **Check current product docs** | Yes, read-only | External research stays outside the main context |
| **Edit the same function twice** | No | Concurrent edits create conflict |

**The worker should receive less context than the orchestrator,** not a copy of the full conversation. Give the goal, source path, task boundary, and return format. Keep a short evidence report in the main session. Inspect the cited files yourself before acting.

## Run Two Read-Only Workers

**Worker A checks tests.** Give it the lab and this task:

```text
Read docs/requirements.md, task_report.py, and tests/.
Find missing tests for the --status request.
Do not edit files.
Return at most five rows: behavior, existing coverage, missing check,
file path, and evidence line.
```

**Worker B checks the requirement.** Give it a different question:

```text
Read docs/requirements.md and tasks.json.
List the accepted values and expected counts for the supplied data.
Do not edit files.
Return source revision, values, counts, and any ambiguity in 100 words.
```

**Expected Worker A finding:** baseline tests cover the total and malformed top-level JSON, but not filtered counts or invalid status. **Expected Worker B finding:** revision 1 accepts `open` and `done`, with two tasks in each group. These are expected findings from the starter, not claims about your worker run.

## Integrate the Findings

**Open the named files yourself.** If Worker A claims an invalid-status test exists, search the test file and confirm it. If Worker B says `pending`, compare with `docs/requirements.md` and reject the stale value. Write a short integration note:

```text
Accepted: two filtered-count tests and one invalid-value test are missing.
Source: docs/requirements.md, revision 1, open and done.
Decision: one coding agent will edit task_report.py and tests.
Boundary: tasks.json remains unchanged.
```

**This note is the useful worker output.** The orchestrator does not need both full transcripts. It needs the verified facts, source paths, and next decision.

## Assign Edit Ownership

**If workers edit files,** split ownership by file or use separate worktrees for overlapping repository tasks. A worktree is another checkout of the same Git repository, with its own working files. It helps keep simultaneous edits apart. The main agent still reviews and merges the results.

| Worker | Owned work | Return |
|---|---|---|
| **Implementation** | `task_report.py` | Diff and test command |
| **Test author** | `tests/test_task_report.py` | Test cases and observed result |
| **Orchestrator** | Requirement and final integration | Combined diff and acceptance record |

**The tiny lab does not need parallel edits.** This table teaches an ownership pattern for larger work. If two workers both need the same function, run them in sequence or ask one to review without editing. Separate worktrees prevent file collisions, but they do not resolve contradictory requirements.

## Check Product Behavior

**Subagents differ by host.** Codex, Claude Code, and OpenCode have different context inheritance, tool permissions, and result delivery. Read the [Codex subagent guide](https://learn.chatgpt.com/docs/agent-configuration/subagents), [Claude Code subagent guide](https://code.claude.com/docs/en/sub-agents), and [OpenCode agent guide](https://opencode.ai/docs/agents/) for your installed product. Do not assume a worker shares the main agent's full conversation or an isolated worktree.

## Practice and Check

**Your artifact:** two short worker reports and one integration note. On the no-cost route, use two new chats with the supplied file contents and label them as separate simulated workers. Do not claim native subagent execution on this route.

**Completion check:** each report names its source, stays within its question, and fits its length limit. Your integration note verifies both against the lab and assigns one owner to the later edit.

## Troubleshooting

- **Worker returns a long transcript:** request a shorter evidence table with file references.
- **Workers disagree:** reread the authoritative file before choosing either answer.
- **Two edits overlap:** stop one edit and establish file ownership or separate worktrees.
- **Worker tool access differs:** inspect the worker's permissions instead of assuming parent settings.

## Next Steps

**Continue with [Bounded Goal Loops](/articles/effective-ai-bounded-agent-loops/)**. For team governance beyond this small lab, use the [AI Collaboration Implementation Course](/ai-collaboration-course-start/).
