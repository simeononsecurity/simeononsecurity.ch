---
title: "Write Better AI Prompts with Task Packets and Acceptance Checks"
date: 2026-10-10
lastmod: 2026-10-10
toc: true
draft: false
description: "Turn vague AI requests into task packets with a defined outcome, source, file scope, test, and stop condition."
genre: ["Artificial Intelligence", "Productivity", "Software Engineering"]
tags: ["AI prompt writing", "task packet", "coding agent prompt", "acceptance criteria", "AI workflow", "AI agent instructions"]
cover: "/img/cover/effective-ai-task-packets.webp"
coverAlt: "A vague request rewritten into a short task packet with source, scope, test, and stop condition"
coverCaption: ""
---

#### [Return to the Practical AI Workflows Course](/effective-ai-course-start/)

**A useful prompt describes the work and how you will judge it.** More words do not fix missing scope. This lesson turns a vague request into a task packet for the course lab.

## Key Takeaways

- **Outcome** names the artifact or behavior you want.
- **Scope** names allowed files and excluded actions.
- **Source** identifies the approved requirement.
- **Acceptance checks** make success observable.
- **Stop conditions** prevent guessing or unauthorized follow-on work.

## Before You Begin

**Prerequisites:** the extracted lab, its `docs/requirements.md`, and the [repository context lesson](/articles/effective-ai-agents-md-context/). Set aside 30 minutes. Difficulty is beginner. This exercise ends with a written packet. You do not need to edit code yet.

## Compare Two Requests

**Vague request:** “Improve the task script.” An agent might rewrite output, add dependencies, edit sample data, or skip tests. None of those choices is established by the request.

**Bounded request:** “Add an optional status filter to `task_report.py` using revision 1 of `docs/requirements.md`. Keep default output. Add tests. Change no sample data. Stop before commit.” The agent still decides implementation details, while the task defines what success means.

| Packet part | Lab example | Check |
|---|---|---|
| **Outcome** | Add `--status` to the report | Both accepted values work |
| **Source** | `docs/requirements.md`, revision 1 | Code matches approved values |
| **Scope** | Program and tests only | Diff contains no other file |
| **Constraints** | Keep default output and sample data | Baseline output stays `Total tasks: 4` |
| **Evidence** | Test command and manual runs | Outputs match expected counts |
| **Stop** | Do not commit or push | Git history and remote stay untouched |

## Use a Reusable Template

**Copy this template** for a small coding or research task. Delete fields with no relevance instead of filling them with vague text.

```text
Outcome:
Authoritative source and revision:
Relevant files or records:
Allowed changes:
Excluded changes and actions:
Examples of desired behavior:
Completion checks:
Stop or ask when:
Report back with:
```

**For the lab,** the completed packet looks like this:

```text
Outcome: Add an optional --status filter to task_report.py.
Source: docs/requirements.md, revision 1.
Relevant files: task_report.py, tasks.json, tests/.
Allowed changes: task_report.py and focused tests.
Excluded: tasks.json, new dependencies, commits, pushes.
Examples: no filter prints Total tasks: 4; open and done each print 2.
Checks: run unit tests and three manual commands.
Stop or ask: source conflict, missing file, unrelated failing baseline.
Report: changed files, commands, observed outputs, unresolved issues.
```

**The packet does not prescribe every line of code.** It gives the agent room to choose a small implementation while keeping the result testable.

## Add Examples Carefully

**One accurate example fixes ambiguity.** The `open` and `done` examples specify output for the supplied four-task file. They do not establish a general rule for every input file. For a different file, counts depend on its records.

**Separate expected from observed.** Before running the program, `Total tasks: 2` is an expected result for each status. After running it, the terminal output is an observation. If the values differ, inspect the data and implementation before claiming success.

## Practice a Stop Condition

**Imagine the requirements file is missing.** The packet names it as the approved source. The correct next step is to stop and ask for the requirement, not infer accepted values from a stale chat or a sample issue.

**Imagine the baseline tests fail before editing.** Record the failure and ask whether to fix the baseline first. A later green run does not isolate whether the filter task or the starting state caused the difference.

**Imagine the agent wants to commit.** The packet excludes commits. Ask it to stop after the diff and tests. You decide whether a later commit belongs in the project workflow.

## Check the Packet

**Score one point for each answer:** Is the outcome concrete? Is the controlling source named? Is file scope clear? Are at least two observable checks stated? Is a stop condition present? A score below five means you should revise the packet before delegation.

**Your artifact:** save your final task packet and a one-line explanation of a stop condition. Give it to a coding agent in the next hands-on lesson or answer the expected results manually on the study route.

## Troubleshooting

- **Agent changes too much:** name files and excluded actions in the packet.
- **Agent asks many questions:** supply the missing source or a concrete example.
- **Agent claims success early:** request observed command output and inspect the files.
- **Packet grows too long:** replace copied source material with a path and revision.

## Next Steps

**Continue with [Context Windows and Handoffs](/articles/effective-ai-context-window-management/)**. That lesson shows which details to keep when a task spans several conversations.
