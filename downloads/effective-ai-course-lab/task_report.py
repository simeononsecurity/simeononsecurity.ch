"""Print a count of tasks from a JSON file."""

import json
import sys
from pathlib import Path


def count_tasks(path: Path) -> int:
    """Return the number of tasks in a JSON list."""
    tasks = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(tasks, list):
        raise ValueError("task data must be a list")
    return len(tasks)


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python3 task_report.py tasks.json", file=sys.stderr)
        return 2
    try:
        total = count_tasks(Path(sys.argv[1]))
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    print(f"Total tasks: {total}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
