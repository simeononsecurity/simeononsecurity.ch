---
title: "AI Workflow Capstone: Build and Verify a Small Feature"
date: 2026-10-10
lastmod: 2026-10-10
toc: true
draft: false
description: "Complete a workshop task-report feature using project context, a scoped agent request, source review, tests, and a fresh-session handoff."
genre: ["Artificial Intelligence", "Software Engineering", "Education"]
tags: ["AI workflow capstone", "coding agent project", "AI task verification", "AGENTS.md", "MCP practice", "agent handoff"]
cover: "/img/cover/effective-ai-capstone.webp"
coverAlt: "A completed workshop software task with source files, test results, agent review, and a handoff record"
coverCaption: ""
---

#### [Return to the Practical AI Workflows Course](/effective-ai-course-start/)

**Finish one small feature and prove its behavior.** You will use the synthetic workshop project from earlier lessons. The feature adds an optional status filter to a task report. The capstone also checks a chat project, repository guidance, a read-only source, a delegated review, and a fresh-session handoff.

## Key Takeaways

- **One approved requirement** controls the feature.
- **A coding agent's edit** stays within named files.
- **Independent checks** determine acceptance.
- **A handoff** lets a new session reconstruct the result.

## Before You Begin

**Prerequisites:** complete [course setup](/articles/effective-ai-course-setup/), [ChatGPT or Claude project setup](/articles/effective-ai-chat-projects/), [task packets](/articles/effective-ai-task-packets/), and [output verification](/articles/effective-ai-output-verification/). The context, MCP, and delegation lessons supply the remaining checkpoints. Set aside 90 to 120 minutes. Difficulty is intermediate.

**Use a fresh extraction** of the [starter lab](/downloads/effective-ai-course-lab.zip). Run `python3 task_report.py tasks.json` and the two baseline tests before any edit. On Windows, substitute `py -3` for `python3` when needed. Create a local Git baseline as in course setup.

**Choose your track.** The connected track uses a coding agent, a live read-only MCP call, and a native subagent or separate worker session. The study track uses a chat assistant to propose code, the official documentation page as a source instead of MCP, and two separate chats as simulated workers. Label tool steps “not run” on the study track. Both tracks require local tests and file review for hands-on completion. If the proposed patch fails, use the complete reference files in the answer key below. Copy them into a fresh lab extraction, then run Checkpoint 6. Keep your original attempt in separate notes so the answer key does not replace your evidence.

## Checkpoint 1: Project Brief

**Open your synthetic ChatGPT or Claude workshop project.** Its approved schedule says the class starts at 7 p.m. Ask for a two-sentence reminder draft and verify the time against `approved-schedule.md`. The schedule does not define the software filter. `docs/requirements.md` defines the feature.

**Evidence:** record the project name, source revision, observed draft time, and whether you corrected a stale 6 p.m. claim. Do not send the message.

## Checkpoint 2: Repository Context

**Open the lab.** Create a short `AGENTS.md` pointing to `docs/requirements.md`, `task_report.py`, tests, and the test command. If you use Claude Code, add a short `CLAUDE.md` pointer. Read the requirement yourself before asking for an edit. Store the test command proven during setup in `AGENTS.md`. On Windows, use `py -3` if the `python3` command failed. Make a human setup commit for `AGENTS.md` and optional `CLAUDE.md`, then confirm `git status --short` is clean. The coding agent must not commit the later feature edit.

**Evidence:** save your map, the clean guidance snapshot, and name `open` and `done` as the approved values. If a chat says `pending`, mark it as stale and follow revision 1 of the requirement.

## Checkpoint 3: External Source

**Connected track:** connect the read-only [OpenAI Docs MCP server](https://learn.chatgpt.com/learn/docs-mcp) through your chosen supported client. Find a tool and use it to read current `AGENTS.md` guidance. Record the tool name, source URL, and one point relevant to your lab. Remove the practice connection afterward.

**Study track:** open the [official `AGENTS.md` documentation](https://learn.chatgpt.com/docs/agent-configuration/agents-md) in a browser. Record the page title, URL, and one relevant point. Mark MCP discovery and execution “not run.”

**Evidence:** a configured server name alone does not pass this checkpoint on the connected track. You need a visible tool call and returned source content.

## Checkpoint 4: Delegate One Review

**Ask a read-only worker** to inspect the baseline tests. Give it `docs/requirements.md`, `task_report.py`, and `tests/`. Require a five-row maximum report naming missing cases and file paths. On the study track, use a separate chat and label it as a simulated worker.

**Expected finding:** the starter tests cover the total count and a non-list JSON value. They do not cover the new filtered values or invalid status. Open the test file yourself to verify this finding before editing.

**Evidence:** save the short report and a one-sentence integration decision. Do not paste the entire worker transcript into the main task.

## Checkpoint 5: Request the Edit

**Give one coding agent** this task packet. The study track uses a chat assistant to propose a patch, then you apply it manually in the lab.

```text
Goal: add --status open|done after the tasks.json path.
Source: docs/requirements.md, revision 1.
Allowed edits: task_report.py and tests/test_task_report.py.
Keep: no-filter output and tasks.json unchanged.
Required checks: tests, counts 4/2/2, invalid value nonzero.
Stop if: requirement conflict, unrelated baseline failure, or edit outside scope.
Report: changed files, commands, observed outputs, unresolved issue.
Do not commit, push, publish, or send a message.
```

**Inspect the proposed plan** before allowing edits. If the agent wants to alter `tasks.json`, point it back to the requirement. Keep the edit in the extracted lab folder.

## Checkpoint 6: Test and Review

**Run the checks yourself** after the edit. On Windows, replace `python3` with `py -3` in the commands below if your setup used the Python launcher. Capture the exact output or a compact record of it.

```bash
git status --short
git diff -- task_report.py tests/test_task_report.py
python3 -m unittest discover -s tests -v
python3 task_report.py tasks.json
python3 task_report.py tasks.json --status open
python3 task_report.py tasks.json --status done
python3 task_report.py tasks.json --status invalid
```

**Expected behavior:** tests pass, valid counts are 4, 2, and 2, and the invalid value shows a clear error with a nonzero exit. Check the invalid exit immediately with `echo $?` on macOS or Linux or `$LASTEXITCODE` in PowerShell. The exact invalid error text is not graded.

| Checkpoint | Pass evidence | Recovery if it fails |
|---|---|---|
| **Project brief** | Reminder uses 7 p.m. | Refresh the schedule source |
| **Repository map** | Requirement and test paths named | Fix `AGENTS.md` or pointer |
| **External source** | Tool read or labeled browser fallback | Inspect connection state or source URL |
| **Worker review** | Missing tests verified in file | Correct worker report |
| **File scope** | Program and tests only | Revert unwanted lab edits |
| **Behavior** | 4/2/2 and invalid rejection | Diagnose one cause, then retry |
| **Handoff** | Fresh session reconstructs state | Add missing source or result |

**Do not accept a summary in place of a diff.** A passing test supports only the behaviors tested. Manual runs cover the supplied data and argument handling. They do not establish security or correctness for every JSON input.

## Checkpoint 7: Fresh Handoff

**Write a handoff under 180 words** outside the lab folder. Include the requirement revision, changed files, exact test command and result, manual counts, any failure, usage record, and pending action. Open a new session and ask it to identify the status values and whether the feature passed.

**Expected answer:** the new session names `open` and `done`, points to revision 1, reports only observed checks, and flags any missing check. A handoff saying “all good” without evidence fails this checkpoint.

## Answer Key and Rubric

**One valid implementation** uses Python 3.10 or later. The complete files below provide a manual study route and a check for your agent's result. Save the first block as `task_report.py` and the second as `tests/test_task_report.py` in a fresh lab extraction. Keep `tasks.json` and `docs/requirements.md` unchanged. Run every command in Checkpoint 6. Compare any different solution with the requirement and observed behavior.

`task_report.py`:

```python
"""Print a count of tasks from a JSON file."""

import argparse
import json
import sys
from pathlib import Path


def count_tasks(path: Path, status: str | None = None) -> int:
    """Count all tasks or tasks with one approved status."""
    tasks = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(tasks, list):
        raise ValueError("task data must be a list")
    if status not in (None, "open", "done"):
        raise ValueError("status must be open or done")
    if status is None:
        return len(tasks)
    return sum(1 for task in tasks if task["status"] == status)


def main() -> int:
    parser = argparse.ArgumentParser(description="Count workshop tasks")
    parser.add_argument("path", type=Path, help="path to the JSON task list")
    parser.add_argument("--status", choices=("open", "done"))
    args = parser.parse_args()
    try:
        total = count_tasks(args.path, args.status)
    except (OSError, ValueError, KeyError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    print(f"Total tasks: {total}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

`tests/test_task_report.py`:

```python
"""Checks for the workshop task report."""

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from sys import path as module_path

ROOT = Path(__file__).resolve().parents[1]
module_path.insert(0, str(ROOT))
from task_report import count_tasks  # noqa: E402


class TaskReportTests(unittest.TestCase):
    def test_counts_four_sample_tasks(self):
        self.assertEqual(count_tasks(ROOT / "tasks.json"), 4)

    def test_rejects_non_list_data(self):
        with tempfile.TemporaryDirectory() as directory:
            sample = Path(directory) / "invalid.json"
            sample.write_text(json.dumps({"tasks": []}), encoding="utf-8")
            with self.assertRaises(ValueError):
                count_tasks(sample)

    def test_counts_each_approved_status(self):
        sample = ROOT / "tasks.json"
        self.assertEqual(count_tasks(sample, "open"), 2)
        self.assertEqual(count_tasks(sample, "done"), 2)

    def test_rejects_invalid_status_in_function(self):
        with self.assertRaises(ValueError):
            count_tasks(ROOT / "tasks.json", "pending")

    def test_default_command_stays_unchanged(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "task_report.py"), str(ROOT / "tasks.json")],
            capture_output=True, text=True, check=False,
        )
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout.strip(), "Total tasks: 4")

    def test_invalid_command_exits_nonzero(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "task_report.py"), str(ROOT / "tasks.json"),
             "--status", "invalid"],
            capture_output=True, text=True, check=False,
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("invalid", result.stderr)


if __name__ == "__main__":
    unittest.main()
```

**Reset after using the answer key:** keep your notes outside the lab, discard this extracted copy, and extract the original starter ZIP again. The new copy contains the original two tests and unfiltered program.

**Score one point for each checkpoint** in the table above. Seven points complete the connected track when the external-source row includes a real MCP tool call. Seven points complete the study track when the row contains a verified browser source and explicitly says MCP not run. A missing behavior, source, or file-scope check blocks completion on either track.

## Troubleshooting

- **Baseline fails before editing:** reset from the ZIP and rerun setup.
- **Agent changes another file:** inspect the diff and restore only the unwanted lab change.
- **MCP connection fails:** use the browser source and label the checkpoint as the study route.
- **Worker repeats a wrong value:** reread the approved requirement and correct the report.
- **Retry budget ends:** preserve the failure log and ask a human reviewer for the next step.

## Next Steps

**Return to the [course outline](/effective-ai-course-start/)** and save your completed evidence record. For advanced team publication and cross-system authority, continue with the [AI Collaboration Implementation Course](/ai-collaboration-course-start/). Its retention lab and governance checks address a different task scale.
