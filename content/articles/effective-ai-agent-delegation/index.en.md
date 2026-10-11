---
title: "AI Agent Delegation: Assign Workers and Review Results"
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

[Return to the Practical AI Workflow Course](/effective-ai-course-start/)

**Delegate when an independent question has enough work to justify a separate session.** A worker agent inspects sources, reviews tests, or drafts a bounded change in its own context. The main agent checks and integrates the result. This lesson uses a documentation comparison while your main session keeps the small lab task.

**Learning outcome:** you will assign an independent worker review and verify its short evidence report.

## Key Takeaways

- **Orchestrator:** the main agent coordinating the task and final review.
- **Worker:** a separate agent assigned one bounded result.
- **Independent work:** a subtask whose answer does not depend on another worker's unfinished output.
- **Ownership:** a named file or question assigned to one worker.
- **Integration:** the main agent's comparison of worker output with current sources.

## Before You Begin

**Prerequisites:** your [context handoff](/articles/effective-ai-context-window-management/) and [output verification](/articles/effective-ai-output-verification/) records. Set aside 40 minutes. Difficulty is intermediate. A product with worker support fits the connected route. The study route uses one separate chat and manual integration.

**Switch to a clean starter for this lesson.** Save your edited filter diff and test record outside the lab. Extract the original ZIP into a new disposable folder. Run the starter command and its two baseline tests. Repeat the course-setup Git baseline and recreate the short `AGENTS.md` and optional `CLAUDE.md` guidance from the repository-context lesson. Commit those guidance files yourself, then confirm `git status --short` is clean. Keep the edited filter copy for reference, but run this worker exercise against the clean starter.

## Decide Whether to Delegate

**Use one agent** for a small sequential edit. Delegation has setup, token, and review cost. Use a worker when a read-only question is independent and its answer would otherwise fill the main chat with many files or source pages.

| Lab task | Delegate? | Reason |
|---|---|---|
| **Add a two-value filter** | Usually no | One small file and focused tests |
| **Find missing cases in two baseline tests** | Usually no | The main agent reads one short file faster |
| **Compare three current product docs** | Yes, read-only | Source reading stays in the worker context |
| **Edit the same function twice** | No | Concurrent edits create conflict |

**The worker should receive less context than the orchestrator,** not a copy of the full conversation. Give the goal, source path, task boundary, and return format. Keep a short evidence report in the main session. Inspect the cited files yourself before acting.

## Run One Read-Only Worker

**Keep a small main task.** In your main session, read the local `AGENTS.md` and note which file contains the test command. Assign the separate research question below to one worker. The worker does not need the entire lab or earlier chat.

**Connected route:** in Codex, Claude Code, or another client with worker support, open the lab as the project and ask the main agent to delegate the following read-only request to one worker. Check the tool transcript for a real worker start and returned report. If the product does not expose a worker, use a separate session and label it as a separate worker session. The [Codex subagent guide](https://learn.chatgpt.com/docs/agent-configuration/subagents), [Claude Code subagent guide](https://code.claude.com/docs/en/sub-agents), and [OpenCode agent guide](https://opencode.ai/docs/agents/) describe current controls.

**Study route:** open one new chat for the same request. Give it the three official links or source excerpts. Label this a simulated worker. A second chat is separate context, not proof of native subagent execution.

```text
Use current official Codex AGENTS.md, Claude Code memory, and OpenCode rules docs.
Compare how each product loads repository instruction files.
Do not edit files.
Return at most three rows: product, instruction file, source URL,
and one loading behavior. Flag uncertainty. Do not paste full pages.
```

**Source set:** [Codex project instructions](https://learn.chatgpt.com/docs/agent-configuration/agents-md), [Claude Code memory](https://code.claude.com/docs/en/memory), and [OpenCode rules](https://opencode.ai/docs/rules/). An expected report names `AGENTS.md` for Codex and OpenCode. Current Claude Code versions also load `AGENTS.md` directly when no `CLAUDE.md` or `CLAUDE.local.md` takes precedence. This lab uses a `CLAUDE.md` file with an `@AGENTS.md` import, which also supports older or differently configured sessions. Verify the current pages and active version before treating this example as observed worker output.

## Integrate the Findings

**Open the cited source pages yourself.** If the worker claims Claude Code always requires a `CLAUDE.md` import, check its memory guide and correct the report. Compare the report with your local guidance files. Write a short integration note:

```text
Accepted: Codex and OpenCode use AGENTS.md project guidance.
Claude Code can load AGENTS.md directly in current versions. This lab
uses CLAUDE.md with an @AGENTS.md import for a stable shared map.
Evidence: record the three current official page URLs and review date.
Decision: keep one shared short map and one Claude import.
```

**This note is the useful worker output.** The orchestrator needs verified findings and source paths, not the research transcript. Delegation uses extra total tokens, so keep the main conversation smaller only when the separate work saves attention.

## Assign Edit Ownership

**If workers edit files,** split ownership by file or use separate worktrees for overlapping repository tasks. A worktree is another checkout of the same Git repository, with its own working files. It helps keep simultaneous edits apart. The main agent still reviews and transfers changes through an explicit merge, cherry-pick, or patch, then reruns tests in the integrated tree.

| Worker | Owned work | Return |
|---|---|---|
| **Implementation** | `task_report.py` | Diff and test command |
| **Test author** | `tests/test_task_report.py` | Test cases and observed result |
| **Orchestrator** | Requirement and final integration | Combined diff and acceptance record |

**The tiny lab does not need parallel edits.** This table teaches an ownership pattern for larger work. Tests in one worktree do not validate an implementation still isolated in another. If two workers need the same function, run them in sequence or ask one to review without editing. Separate worktrees prevent file collisions, but they do not resolve contradictory requirements.

## Check Product Behavior

**Subagents differ by host.** Codex, Claude Code, and OpenCode have different context inheritance, tool permissions, and result delivery. Read the [Codex subagent guide](https://learn.chatgpt.com/docs/agent-configuration/subagents), [Claude Code subagent guide](https://code.claude.com/docs/en/sub-agents), and [OpenCode agent guide](https://opencode.ai/docs/agents/) for your installed product. Do not assume a worker shares the main agent's full conversation or an isolated worktree.

## Practice and Check

**Your artifact:** one short documentation worker report and one integration note. On the study route, use one new chat and label it as a simulated worker. Do not claim native subagent execution on this route.

**Completion check:** the report names three official sources, stays within its question, and fits its length limit. Your integration note checks the sources and names the guidance files your lab uses.

## Check Your Understanding

1. **Question:** When does a worker help more than a single agent? **Answer:** When it owns an independent question or artifact with a useful evidence report.

2. **Question:** What must happen after two workers touch overlapping files? **Answer:** Integrate the changes, inspect the combined diff, and rerun the checks.

## Troubleshooting

- **Worker returns a long transcript:** request a shorter evidence table with file references.
- **Workers disagree:** reread the authoritative file before choosing either answer.
- **Two edits overlap:** stop one edit and establish file ownership or separate worktrees.
- **Worker tool access differs:** inspect the worker's permissions instead of assuming parent settings.

## Next Steps

**Continue with [Bounded Goal Loops](/articles/effective-ai-bounded-agent-loops/)**. For team governance beyond this small lab, use the [AI Collaboration Implementation Course](/ai-collaboration-course-start/).

**Course navigation:** [Previous: Output Verification](/articles/effective-ai-output-verification/), [Course outline](/effective-ai-course-start/).
