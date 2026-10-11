---
title: "How to Verify AI Output, Sources, Tests, and Costs"
date: 2026-10-10
lastmod: 2026-10-10
toc: true
draft: false
description: "Build an acceptance record for an AI result with source checks, file scope, test evidence, privacy review, and usage cost."
genre: ["Artificial Intelligence", "Software Engineering"]
tags: ["verify AI output", "AI fact checking", "coding agent review", "AI test evidence", "AI cost tracking", "human review"]
cover: "/img/cover/effective-ai-output-verification.webp"
coverAlt: "A review sheet comparing an AI claim with a source file, code diff, test output, and usage total"
coverCaption: ""
---

#### [Return to the Practical AI Workflows Course](/effective-ai-course-start/)

**Accept an AI result only after checking the evidence appropriate to the task.** A polished explanation, a configured tool, and a green test banner answer different questions. This lesson builds one review record for the workshop lab.

## Key Takeaways

- **Source check:** compare a factual claim with a current authoritative record.
- **Scope check:** inspect what files or systems changed.
- **Behavior check:** run tests and relevant manual cases.
- **Privacy check:** inspect what material reached the tool or provider.
- **Usage check:** record tokens, tool calls, and the rate used for cost.

## Before You Begin

**Prerequisites:** the course lab, `docs/requirements.md`, a local Git snapshot, and the [MCP lesson](/articles/effective-ai-mcp-server-setup/) or its browser fallback. Set aside 40 minutes. Difficulty is intermediate. Use your edited lab from the first coding-agent task. If you skipped the edit, use a fresh extraction and label the feature checks as baseline failures.

## Check a Factual Claim

**Claim:** “The approved status values are `open` and `pending`.” Open `docs/requirements.md`, revision 1. It says `open` and `done`. The claim fails. A confident tone does not change the requirement.

**For product claims,** use current official documentation and record the page title and review date. A claim about a menu, plan, command, or context limit grows stale faster than a general workflow principle. The [Codex documentation](https://learn.chatgpt.com/docs/codex/cli), [Claude Code documentation](https://code.claude.com/docs/en/overview), and [OpenCode documentation](https://opencode.ai/docs/) identify their current interfaces.

| Claim | Source | Decision |
|---|---|---|
| **`open` and `pending`** | Lab requirement, revision 1 | Reject, replace `pending` with `done` |
| **No-filter count is 4** | Baseline program and four JSON entries | Check by running the program |
| **An MCP read occurred** | Session tool transcript | Accept only if a tool call is visible |

## Inspect the Change

**For a coding task,** use Git to list changed files and read the actual diff. A new untracked file appears in status even when it does not appear in an ordinary diff, so inspect both.

```bash
git status --short
git diff -- task_report.py tests
```

**Expected scope:** only `task_report.py` and focused tests change after the filter task. A change to `tasks.json`, `docs/requirements.md`, or a hidden configuration file needs an explanation and separate review. If you have not run an edit, expect no changes.

## Test Behavior

**Run the same baseline and feature checks** from the extracted lab folder. These are the checks the agent's completion message should report with observed results.

```bash
python3 -m unittest discover -s tests -v
python3 task_report.py tasks.json
python3 task_report.py tasks.json --status open
python3 task_report.py tasks.json --status done
python3 task_report.py tasks.json --status invalid
```

**In the edited copy,** tests cover the new cases, counts are 4, 2, and 2, and the invalid value exits nonzero with a clear error. In a fresh starter copy, only the two baseline tests and total count of 4 pass. Record the starter state separately.

**A failed feature test needs diagnosis.** If `open` prints 4, check whether the filter argument reaches the count function and whether the program compares the task's `status` field. Do not relabel a failed test as a passing result because the agent says the implementation is finished.

## Check Privacy and Access

**Record which files the agent received.** The lab contains synthetic data and no secrets. A real project might include credentials, customer records, or private documents. Before sharing output, inspect prompts, logs, screenshots, and diffs for those values.

**A local test proves local behavior only.** It does not prove a cloud account's permissions, an MCP server's scope, or a deployed service. Test each boundary in the environment where it matters.

## Record Usage and Cost

**Tokens measure model input and output volume.** Product dashboards differ, so use the usage figures shown by your provider. Record tool calls and image or hosted-environment charges separately where applicable. Check current rates before calculating a real bill.

**Illustrative calculation, not vendor pricing:** 30,000 input tokens at $1 per million cost $0.03. 5,000 output tokens at $5 per million cost $0.025. The combined model charge in this example is $0.055 before tool or hosting charges.

```text
input cost = input tokens / 1,000,000 × input rate
output cost = output tokens / 1,000,000 × output rate
total = input cost + output cost + separate tool charges
```

**A worker task also spends tokens.** Delegation moves detailed output out of the main conversation, but it does not make the work free. Compare the cost with the value of the independent check.

## Keep an Acceptance Record

| Field | Worked example after the edit |
|---|---|
| **Source** | `docs/requirements.md`, revision 1, read |
| **Changed files** | `task_report.py` and `tests/test_task_report.py` in `git status --short` |
| **Tests** | Baseline and new filter tests passed, record your observed count |
| **Manual output** | `Total tasks: 4`, `2`, and `2` observed, invalid rejected |
| **Feature state** | `--status open` and `--status done` implemented |
| **Privacy** | Synthetic files only |
| **Usage** | Record your provider's figures, if used |
| **Decision** | Accept only after the source, diff, tests, and privacy checks pass |

**Your artifact:** copy this record and fill it after your own run. Replace “observed” only with output you saw. Use Accept when every required check passes, Revise when a fix is bounded, and Stop when the source, scope, or access is unclear.

## Troubleshooting

- **No source for a claim:** mark it unverified and find an authoritative record.
- **Tests pass but output differs:** add a manual case and inspect the data.
- **Usage missing:** record “not available” instead of estimating a real charge.
- **Diff includes private data:** stop sharing the output and remove the data from the practice record.

## Next Steps

**Continue with [Agent Delegation](/articles/effective-ai-agent-delegation/)**. For related cost and privacy detail, read [provider routing](/articles/openrouter-provider-routing-quality-cost/) and [local AI privacy](/articles/local-ai-privacy-boundary/).
