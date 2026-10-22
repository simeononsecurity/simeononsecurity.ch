#!/usr/bin/env python3
"""Run a deterministic local IAM policy and teardown simulation."""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import sys
from pathlib import Path
from typing import Any


class SimulatorError(Exception):
    """Report invalid input or an unsafe local path."""


def load_fixture(path: Path) -> tuple[dict[str, Any], str]:
    try:
        raw = path.read_bytes()
    except OSError as exc:
        raise SimulatorError(f"fixture read failed: {exc}") from exc

    try:
        fixture = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise SimulatorError(f"fixture JSON failed: {exc}") from exc

    required = {
        "schema_version",
        "scenario",
        "principal",
        "resource",
        "initial_policy",
        "checks",
        "local_artifacts",
    }
    missing = sorted(required.difference(fixture))
    if missing:
        raise SimulatorError(f"fixture fields missing: {', '.join(missing)}")

    policy = fixture["initial_policy"]
    if not isinstance(policy, dict):
        raise SimulatorError("initial_policy must be an object")
    if not isinstance(policy.get("allow"), list) or not isinstance(policy.get("deny"), list):
        raise SimulatorError("initial_policy allow and deny must be lists")

    checks = fixture["checks"]
    expected_checks = {"allow_action", "deny_action", "revoked_action"}
    if not isinstance(checks, dict) or not expected_checks.issubset(checks):
        raise SimulatorError("checks must name allow_action, deny_action, and revoked_action")
    if checks["allow_action"] != checks["revoked_action"]:
        raise SimulatorError("revoked_action must repeat the allowed action")

    artifacts = fixture["local_artifacts"]
    if not isinstance(artifacts, list) or not artifacts:
        raise SimulatorError("local_artifacts must be a nonempty list")
    for name in artifacts:
        artifact = Path(name)
        if not isinstance(name, str) or artifact.is_absolute() or len(artifact.parts) != 1:
            raise SimulatorError("local_artifacts must contain plain file names")

    return fixture, hashlib.sha256(raw).hexdigest()


def decision(policy: dict[str, Any], action: str) -> tuple[str, str]:
    if action in policy["deny"]:
        return "deny", "explicit deny"
    if action in policy["allow"]:
        return "allow", "explicit allow"
    return "deny", "implicit deny"


def safe_paths(
    fixture_path: Path,
    workdir: Path,
    evidence_path: Path,
    evidence_input: Path,
) -> None:
    protected = {Path("/").resolve(), Path.home().resolve(), Path.cwd().resolve()}
    if workdir in protected:
        raise SimulatorError("workdir points to a protected directory")
    if workdir.exists():
        raise SimulatorError("workdir already exists, choose a fresh path")
    if workdir == fixture_path.parent or fixture_path.is_relative_to(workdir):
        raise SimulatorError("workdir overlaps the fixture")
    if evidence_path == fixture_path:
        raise SimulatorError("evidence path must differ from the fixture path")
    if evidence_path == workdir or evidence_path.is_relative_to(workdir):
        raise SimulatorError("evidence file must sit outside the removable workdir")
    if evidence_input.is_symlink():
        raise SimulatorError("evidence path must not be a symbolic link")
    if evidence_input.exists() or evidence_path.exists():
        raise SimulatorError("evidence file already exists, choose a fresh path")


def write_json(path: Path, data: dict[str, Any], *, exclusive: bool = False) -> None:
    mode = "x" if exclusive else "w"
    with path.open(mode, encoding="utf-8") as handle:
        handle.write(json.dumps(data, indent=2, sort_keys=True) + "\n")


def run(args: argparse.Namespace) -> int:
    fixture_path = Path(args.fixture).resolve()
    workdir = Path(args.workdir).resolve()
    evidence_input = Path(args.evidence).expanduser()
    evidence_path = evidence_input.resolve()
    fixture, fixture_sha256 = load_fixture(fixture_path)
    safe_paths(fixture_path, workdir, evidence_path, evidence_input)

    created_workdir = False
    checks: list[dict[str, str]] = []
    cleanup_record: dict[str, str] = {}

    try:
        workdir.mkdir(parents=True)
        created_workdir = True

        state = {
            "principal": fixture["principal"],
            "resource": fixture["resource"],
            "policy": fixture["initial_policy"],
            "revoked": False,
        }
        write_json(workdir / "policy-state.json", state)

        for artifact_name in fixture["local_artifacts"]:
            write_json(
                workdir / artifact_name,
                {
                    "principal": fixture["principal"],
                    "resource": fixture["resource"],
                    "synthetic": True,
                },
            )

        allow_action = fixture["checks"]["allow_action"]
        observed, reason = decision(state["policy"], allow_action)
        checks.append(
            {
                "check": "allow",
                "action": allow_action,
                "expected": "allow",
                "observed": observed,
                "reason": reason,
            }
        )

        deny_action = fixture["checks"]["deny_action"]
        observed, reason = decision(state["policy"], deny_action)
        checks.append(
            {
                "check": "deny",
                "action": deny_action,
                "expected": "deny",
                "observed": observed,
                "reason": reason,
            }
        )

        state["policy"] = {"allow": [], "deny": state["policy"]["deny"]}
        state["revoked"] = True
        write_json(workdir / "policy-state.json", state)
        revoked_action = fixture["checks"]["revoked_action"]
        observed, reason = decision(state["policy"], revoked_action)
        checks.append(
            {
                "check": "revocation",
                "action": revoked_action,
                "expected": "deny",
                "observed": observed,
                "reason": reason,
            }
        )

        failed = [entry for entry in checks if entry["expected"] != entry["observed"]]
        if failed:
            raise SimulatorError("one or more policy decisions differed from the fixture")
    finally:
        if created_workdir and workdir.exists():
            shutil.rmtree(workdir)
        cleanup_record = {
            "check": "local cleanup",
            "expected": "removed",
            "observed": "removed" if not workdir.exists() else "present",
            "path": args.workdir,
        }

    if cleanup_record["observed"] != "removed":
        raise SimulatorError("local workdir remains after cleanup")

    evidence = {
        "boundary": "Local synthetic policy logic only. No cloud API or tenant was used.",
        "checks": checks,
        "cleanup": cleanup_record,
        "fixture_sha256": fixture_sha256,
        "principal": fixture["principal"],
        "resource": fixture["resource"],
        "scenario": fixture["scenario"],
        "status": "pass",
    }
    evidence_path.parent.mkdir(parents=True, exist_ok=True)
    write_json(evidence_path, evidence, exclusive=True)

    for entry in checks:
        print(
            f"{entry['check'].upper()} PASS expected={entry['expected']} "
            f"observed={entry['observed']} action={entry['action']}"
        )
    print(
        "LOCAL CLEANUP PASS expected=removed "
        f"observed={cleanup_record['observed']} path={cleanup_record['path']}"
    )
    print(f"RESULT PASS checks=4/4 evidence={args.evidence}")
    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run a local synthetic IAM policy and teardown scenario."
    )
    parser.add_argument("--fixture", required=True, help="Path to the JSON fixture")
    parser.add_argument("--workdir", required=True, help="Fresh local state directory")
    parser.add_argument("--evidence", required=True, help="Output evidence JSON path")
    return parser.parse_args()


def main() -> int:
    try:
        return run(parse_args())
    except (OSError, SimulatorError) as exc:
        print(f"ERROR {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
