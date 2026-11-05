# Effective AI Course Lab

This small Python project supports the Practical AI Workflows course. It uses synthetic tasks and makes no network calls.

## Start

Open a terminal in this extracted folder. Run:

```bash
python3 task_report.py tasks.json
python3 -m unittest discover -s tests -v
```

The first command prints `Total tasks: 4`. The second runs two baseline tests.

## Reset

Save review notes outside this folder. Delete this extracted copy and extract the original ZIP again. This restores the starting files without relying on Git or a coding agent.

## Files

- `task_report.py` reads the JSON task list and counts tasks.
- `tasks.json` holds four fictional tasks.
- `tests/test_task_report.py` tests the baseline behavior.
- `docs/requirements.md` states the approved change for later lessons.
- `docs/capstone-requirements.md` states a separate JSON report task for the capstone.

Lesson 5 asks you to add an optional `--status` filter. The capstone uses a fresh extraction and asks for a separate `--format json` report. The starter contains neither solution. Do not place credentials, customer records, or private files in this lab.
