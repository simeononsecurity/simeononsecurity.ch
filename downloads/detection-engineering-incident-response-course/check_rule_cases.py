"""Offline check for the three selections in the course Sigma draft.

This is a small predicate harness, not a Sigma parser or SIEM translator.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path


def matches(event: dict[str, object]) -> bool:
    parent = str(event.get("ParentImage", "")).lower()
    child = str(event.get("Image", "")).lower()
    command = str(event.get("CommandLine", "")).lower()
    office = parent.endswith(("\\winword.exe", "\\excel.exe", "\\powerpnt.exe"))
    shell = child.endswith(("\\powershell.exe", "\\pwsh.exe"))
    encoded = "-encodedcommand" in command or "-enc " in command
    return office and shell and encoded


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: python3 check_rule_cases.py rule-test-events.jsonl", file=sys.stderr)
        return 2
    path = Path(sys.argv[1])
    passed = 0
    total = 0
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        event = json.loads(line)
        expected = event["expected"]
        if not isinstance(expected, bool):
            raise ValueError(f"line {number}: expected must be true or false")
        observed = matches(event)
        good = observed == expected
        passed += good
        total += 1
        print(f"{event['case']}: expected={expected} observed={observed} {'PASS' if good else 'FAIL'}")
    print(f"{passed}/{total} passed")
    return 0 if total == 5 and passed == 5 else 1


if __name__ == "__main__":
    raise SystemExit(main())
