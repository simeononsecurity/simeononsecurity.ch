---
title: "Bounded AI Agent Loops: Checks, Retries, and Stop Rules"
date: 2026-10-10
lastmod: 2026-10-10
toc: true
draft: false
description: "Define an AI goal loop with observable state, checks, retry limits, stop conditions, and a clear human handoff."
genre: ["Artificial Intelligence", "Software Engineering", "Productivity"]
tags: ["AI goal loops", "agent retry loop", "AI automation stop rules", "agent monitoring", "AI human handoff", "bounded AI workflow"]
cover: "/img/cover/effective-ai-bounded-agent-loops.webp"
coverAlt: "A small agent loop moving from one edit to a test, retry decision, and human handoff"
coverCaption: ""
---

#### [Return to the Practical AI Workflows Course](/effective-ai-course-start/)

**A goal loop repeats work until a defined result passes or a stop rule fires.** The useful loop reads current state, takes one bounded action, checks the result, and records what happened. An open-ended “keep trying” instruction has no reliable completion rule.

## Key Takeaways

- **Goal:** a result stated in observable terms.
- **State:** the current files, outputs, errors, and source revision.
- **Check:** a test or review tied to the goal.
- **Retry budget:** the maximum attempts allowed for one failure.
- **Stop rule:** a condition requiring an end or human decision.

## Before You Begin

**Prerequisites:** the [task packet](/articles/effective-ai-task-packets/), [verification record](/articles/effective-ai-output-verification/), and [delegation lesson](/articles/effective-ai-agent-delegation/). Set aside 30 minutes. Difficulty is intermediate. Keep this exercise inside a fresh copy of the synthetic lab.

## Write the Loop Contract

**For the status-filter request,** set the contract before any retry:

```text
Goal: support --status open|done without changing default output.
Source: docs/requirements.md, revision 1.
Allowed files: task_report.py and focused tests.
Checks: unit tests, counts 4/2/2, invalid value exits nonzero.
Retry budget: at most two edits after the first attempt.
Stop immediately: source conflict, unexpected file change, secret exposure,
or a failing baseline unrelated to this request.
Handoff: report final diff, commands, outputs, attempts, and unresolved issue.
```

**The budget is a task policy,** not a product default. Two retries are enough to diagnose a small lab task without hiding repeated failure. A production task needs its own risk and review choice.

## Use a State Table

| Step | State to record | Decision |
|---|---|---|
| **Read** | Source revision and baseline result | Stop if the starting state differs |
| **Act** | Changed files and action taken | Reject out-of-scope edits |
| **Check** | Exact test and manual output | Accept or diagnose |
| **Retry** | Failure cause and new hypothesis | Continue only within budget |
| **Handoff** | Final state and next owner | Stop after pass or blocked result |

**Record attempts, not only the last message.** A test passing after three hidden edits leaves no useful account of what changed. Keep a short attempt log with the failure, revised hypothesis, and new evidence.

## Walk Through a Failure

**Illustrative first attempt:** the agent adds filtering and tests. `open` prints 2, but `--status invalid` prints 0 and exits successfully. The requirement says an invalid value needs a nonzero exit. Mark the check failed.

**Diagnosis:** inspect argument validation. The agent treated an unknown value as an empty match instead of an error. Ask for one scoped fix to validate accepted values before counting. Run the same invalid case and all earlier checks again.

```text
Attempt 1: invalid status returned success, so acceptance failed.
Cause found: no accepted-value validation.
Attempt 2 request: reject unsupported values and retain 4/2/2 counts.
Evidence required: full test run and invalid command exit status.
```

**Expected second result:** a clear error and nonzero status for `invalid`, with unchanged valid counts. If the second run still fails, use the remaining retry only after naming a new cause. Repeating the same prompt is not diagnosis.

## Handle Ambiguous Results

**A process stopping without a result is not success.** If a tool times out after a possible file write, inspect the files and Git status before rerunning it. If a connected service reports an unknown outcome, read its current state before retrying an external action. Duplicate sends, posts, or writes are a real risk outside the lab.

**Stop for human review** when the requirement conflicts with another approved source, a permission blocks the action, the retry budget ends, or the requested action crosses a publication boundary. The handoff should name the exact state and the choice needed.

## Separate Loops from Monitors

**An edit loop** runs within a bounded task and checks after each action. **A scheduled monitor** wakes later to inspect a condition. A monitor needs its own cadence, change threshold, notification rule, and stop condition. Do not turn the lab edit loop into a recurring job. The next lesson evaluates persistent systems before enabling them.

## Practice and Check

**Your artifact:** a loop contract and a two-attempt log for the illustrative invalid-status failure. If you run a coding agent, replace illustrative output with observed output from your lab. On the no-cost route, write the proposed correction and mark execution not run.

**Completion check:** the contract names a source, file scope, observable checks, retry limit, at least one immediate stop condition, and a final handoff. The attempt log explains why the second attempt differs from the first.

## Troubleshooting

- **Loop repeats the same failure:** stop and form a new cause hypothesis.
- **Checks become weaker:** restore the original acceptance checks.
- **Uncertain external result:** inspect current state before another action.
- **Budget exhausted:** hand off the failure record instead of hiding it.

## Next Steps

**Continue with [Specialized Agent Evaluation](/articles/effective-ai-specialized-agent-evaluation/)**, an optional lesson before the capstone. For broader runtime choices, read the site's [agent harness guide](/articles/best-ai-agent-harnesses/).
