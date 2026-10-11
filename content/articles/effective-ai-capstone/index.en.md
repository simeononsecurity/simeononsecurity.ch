---
title: "AI Workflow Capstone: Build and Verify a JSON Report"
date: 2026-10-10
lastmod: 2026-10-10
toc: true
draft: false
description: "Build a new JSON task report with project context, a scoped agent request, independent tests, source review, and a fresh-session handoff."
genre: ["Artificial Intelligence", "Software Engineering", "Education"]
tags: ["AI workflow capstone", "coding agent project", "AI task verification", "AGENTS.md", "MCP practice", "agent handoff"]
cover: "/img/cover/effective-ai-capstone.webp"
coverAlt: "A completed workshop software task with source files, test results, agent review, and a handoff record"
coverCaption: ""
---

[Return to the Practical AI Workflow Course](/effective-ai-course-start/)

**Build a new output format and prove its behavior.** Earlier you added a status filter. This capstone starts from a fresh lab and adds a JSON report for another program to read. The new requirement tests whether you transfer your workflow to a different feature.

**Learning outcome:** you will deliver a checked JSON report, a source and tool evidence record, and a handoff a fresh session understands.

## Key Takeaways

- **A separate requirement** controls the capstone feature.
- **A coding agent's edit** stays within named files.
- **Independent checks** determine acceptance.
- **A fresh handoff** lets another session reconstruct the result.

## Before You Begin

**Prerequisites:** complete lessons 0 through 10, including repository context, the first coding task, MCP or its browser fallback, delegation, and bounded loops. Lesson 11 is optional. Set aside 90 to 120 minutes. Difficulty is intermediate.

**Use a fresh extraction** of the [starter lab](/downloads/effective-ai-course-lab.zip). Run `python3 task_report.py tasks.json` and the two baseline tests before any edit. On Windows, use `py -3` if your setup used the Python launcher. Create a local Git baseline as in course setup. The status filter from lesson 5 is absent by design.

**Read `docs/capstone-requirements.md`, revision 1.** It requires `--format text|json`. Default text remains `Total tasks: 4`. JSON output has a numeric total and counts for every status in the data. You will test an empty list, a missing status, and an unsupported format. Do not use `docs/requirements.md` as the authority for this new feature.

**Choose your track.** The connected track uses an observed coding-agent edit, a real read-only MCP call, and a native worker or separate worker session. The study track uses a chat assistant to propose code, a browser source in place of MCP, and separate chats as simulated workers. Mark unavailable tool steps “not run.” Both tracks require local tests and file review. The answer key below provides complete files if your attempt needs a recovery path. Save your first attempt in notes before copying the answer key into a fresh extraction.

## Checkpoint 1: Project Brief

**Open the synthetic ChatGPT or Claude workshop project.** Ask for a two-sentence reminder draft. Verify its 7 p.m. time against `approved-schedule.md`. The schedule controls the reminder. The capstone requirement controls the program.

**Evidence:** record the project name, source revision, observed draft time, and any correction. Do not send the message.

## Checkpoint 2: Repository Context

**Open the fresh lab.** Create a short `AGENTS.md` pointing to `docs/capstone-requirements.md`, `task_report.py`, tests, and the test command proven during setup. If you use Claude Code, import the shared file from `CLAUDE.md`. Make a human setup commit for those guidance files, then confirm `git status --short` is clean. The coding agent must not commit the feature edit.

**Evidence:** save the map and clean guidance snapshot. Name the JSON keys and invalid-input behavior from revision 1. If a prior chat describes the status filter, treat it as background for a different task.

## Checkpoint 3: External Source

**Connected track:** use the read-only [OpenAI Docs MCP server](https://learn.chatgpt.com/learn/docs-mcp) through a supported client. Ask one MCP tool for current `AGENTS.md` guidance. Record the tool name, source URL, and one point relevant to your lab. Remove the practice connection afterward.

**Study track:** open the [official `AGENTS.md` documentation](https://learn.chatgpt.com/docs/agent-configuration/agents-md) in a browser. Record its title, URL, and one relevant point. Mark MCP discovery and execution “not run.”

**Evidence:** a configured server entry does not prove execution. The connected track needs a visible tool call and returned source content.

## Checkpoint 4: Delegate One Review

**Ask one read-only worker** to inspect `docs/capstone-requirements.md`, `task_report.py`, and the baseline tests. Require a five-row maximum report naming missing checks and file paths. On the study track, use a separate chat and label it as a simulated worker.

**Expected finding:** the starter tests cover total count and a non-list JSON value. They do not cover JSON output, an empty list, a missing status, or an invalid format. Open the test file yourself to verify the report. A short independent review has value here because the acceptance set differs from lesson 5.

**Evidence:** save the short report and your one-sentence integration decision. Keep the worker transcript outside the main task record.

## Checkpoint 5: Request the Edit

**Give one coding agent** the packet below. The study track uses a chat assistant to propose a patch, then you apply it manually in the lab.

```text
Goal: add --format text|json after the JSON path.
Source: docs/capstone-requirements.md, revision 1.
Allowed edits: task_report.py and tests/test_task_report.py.
Keep: default Total tasks: 4 and tasks.json unchanged.
JSON: one object with total and by_status counts, no extra stdout text.
Required checks: default and explicit text, JSON 4/2/2, empty list,
missing status, invalid format, and baseline tests.
Stop if: source conflict, unrelated baseline failure, or edit outside scope.
Report: changed files, commands, observed outputs, unresolved issue.
Do not commit, push, publish, or send a message.
```

**Inspect the plan** before edits. A schema choice matters: `total` is a number, not the string `"4"`. `by_status` contains every status present in input, so the report still accounts for a future status value. Keep the edit inside the extracted lab.

## Checkpoint 6: Test and Review

**Run these checks yourself.** On Windows, replace `python3` with `py -3` if needed. The JSON command's exact key order and whitespace do not matter. Parse its output as JSON and compare typed values.

```bash
git status --short
git diff -- task_report.py tests/test_task_report.py
python3 -m unittest discover -s tests -v
python3 task_report.py tasks.json
python3 task_report.py tasks.json --format text
python3 task_report.py tasks.json --format json
python3 task_report.py tasks.json --format invalid
```

**Expected behavior:** tests pass. Both text commands print `Total tasks: 4`. The JSON command returns a single object with `total` 4, `by_status.open` 2, and `by_status.done` 2. The invalid format exits nonzero. The tests also cover empty input and a task without a string `status`. Read the observed error output and exit status for those cases.

| Checkpoint | Pass evidence | Recovery if it fails |
|---|---|---|
| **Project brief** | Reminder uses 7 p.m. | Refresh the schedule source |
| **Repository map** | Capstone requirement and test paths named | Fix the guidance files |
| **External source** | MCP tool read or labeled browser fallback | Inspect connection or source URL |
| **Worker review** | Missing tests verified in file | Correct the worker report |
| **File scope** | Program and tests only | Inspect each unwanted edit before restoring it |
| **Behavior** | Text, JSON, empty, and errors checked | Diagnose one cause, then retry |
| **Handoff** | Fresh session reconstructs state | Add missing source or result |

**Use a fresh extraction as the safe reset.** Save your notes outside the lab, discard only the disposable extracted copy, and extract the original ZIP again. Do not use a broad Git reset in a repository with work you need to keep.

## Checkpoint 7: Fresh Handoff

**Write a handoff under 180 words** outside the lab folder. Include the capstone requirement revision, changed files, exact test command and result, text and JSON results, invalid-input checks, usage record, and pending action. Open a new session and ask it to identify the JSON keys and whether the feature passed.

**Expected answer:** the new session names `total` and `by_status`, points to revision 1, reports only observed checks, and flags any missing check. A handoff saying “all good” without evidence fails.

## Answer Key and Rubric

**One valid implementation** appears below. Save the first block as `task_report.py` and the second as `tests/test_task_report.py` in a fresh lab extraction. Keep `tasks.json` and both requirement files unchanged. Run the checks in Checkpoint 6. Compare another solution against the requirement and observed behavior.

`task_report.py`:

```python
"""Print a text count or JSON summary of workshop tasks."""

import argparse
import json
import sys
from collections import Counter
from pathlib import Path


def load_tasks(path: Path) -> list:
    tasks = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(tasks, list):
        raise ValueError("task data must be a list")
    for index, task in enumerate(tasks, start=1):
        if not isinstance(task, dict) or not isinstance(task.get("status"), str):
            raise ValueError(f"task {index} needs a string status")
    return tasks


def count_tasks(path: Path) -> int:
    return len(load_tasks(path))


def summarize_tasks(path: Path) -> dict:
    tasks = load_tasks(path)
    counts = Counter()
    for task in tasks:
        counts[task["status"]] += 1
    return {"total": len(tasks), "by_status": dict(sorted(counts.items()))}


def main() -> int:
    parser = argparse.ArgumentParser(description="Report workshop tasks")
    parser.add_argument("path", type=Path, help="path to the JSON task list")
    parser.add_argument("--format", choices=("text", "json"), default="text")
    args = parser.parse_args()
    try:
        if args.format == "json":
            print(json.dumps(summarize_tasks(args.path)))
        else:
            print(f"Total tasks: {count_tasks(args.path)}")
    except (OSError, ValueError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

`tests/test_task_report.py`:

```python
"""Checks for text and JSON workshop reports."""

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


def run_report(path: Path, *options: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, str(ROOT / "task_report.py"), str(path), *options],
        capture_output=True, text=True, check=False,
    )


class TaskReportTests(unittest.TestCase):
    def test_counts_four_sample_tasks(self):
        self.assertEqual(count_tasks(ROOT / "tasks.json"), 4)

    def test_rejects_non_list_data(self):
        with tempfile.TemporaryDirectory() as directory:
            sample = Path(directory) / "invalid.json"
            sample.write_text(json.dumps({"tasks": []}), encoding="utf-8")
            with self.assertRaises(ValueError):
                count_tasks(sample)

    def test_default_and_explicit_text(self):
        for options in ((), ("--format", "text")):
            result = run_report(ROOT / "tasks.json", *options)
            self.assertEqual(result.returncode, 0)
            self.assertEqual(result.stdout.strip(), "Total tasks: 4")

    def test_json_counts_and_types(self):
        result = run_report(ROOT / "tasks.json", "--format", "json")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(json.loads(result.stdout), {
            "total": 4, "by_status": {"open": 2, "done": 2},
        })

    def test_empty_list(self):
        with tempfile.TemporaryDirectory() as directory:
            sample = Path(directory) / "empty.json"
            sample.write_text("[]", encoding="utf-8")
            result = run_report(sample, "--format", "json")
            self.assertEqual(result.returncode, 0)
            self.assertEqual(json.loads(result.stdout), {
                "total": 0, "by_status": {},
            })

    def test_missing_status(self):
        with tempfile.TemporaryDirectory() as directory:
            sample = Path(directory) / "missing.json"
            sample.write_text('[{"id": 1}]', encoding="utf-8")
            for options in ((), ("--format", "json")):
                result = run_report(sample, *options)
                self.assertNotEqual(result.returncode, 0)
                self.assertIn("status", result.stderr)

    def test_invalid_format(self):
        result = run_report(ROOT / "tasks.json", "--format", "invalid")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("invalid", result.stderr)


if __name__ == "__main__":
    unittest.main()
```

**Reset after using the answer key:** save notes outside the lab, discard this extracted copy, and extract the original starter ZIP again. The new copy contains the two baseline tests and no feature implementation.

**Score one point for each checkpoint** in the table above. Seven points complete the connected track when the external-source row includes a real MCP tool call and the worker row records a real worker session. Seven points complete the study track when the source row contains a verified browser page and tool steps explicitly say not run. A missing behavior, source, or file-scope check blocks completion on either track.

## Check Your Understanding

1. **Which requirement controls this feature?** `docs/capstone-requirements.md`, revision 1. The earlier status-filter requirement belongs to lesson 5.
2. **What proves the JSON contract?** Parse the command output, compare numeric values and every status count, and check empty and invalid inputs. A polished agent summary is insufficient.

## Troubleshooting

- **Baseline fails before editing:** reset from the ZIP and rerun setup.
- **Agent changes another file:** inspect the diff and restore only the unwanted lab change.
- **MCP connection fails:** use the browser source and label the checkpoint as the study route.
- **Worker repeats a wrong value:** reread the capstone requirement and correct the report.
- **Retry budget ends:** preserve the failure log and ask a human reviewer for the next step.

## Next Steps

**Save your completed evidence record.** For advanced team publication and cross-system authority, continue with the [AI Collaboration Implementation Course](/ai-collaboration-course-start/).

**Course navigation:** [Previous required: Bounded Loops](/articles/effective-ai-bounded-agent-loops/), [Optional: Specialized Agents](/articles/effective-ai-specialized-agent-evaluation/), [Course outline](/effective-ai-course-start/).
