"""Synthetic consistency checks, not an authorization or approval service."""
import argparse
import hashlib
import json
from pathlib import Path

SOURCES = ("policy.json", "requirement.json")


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def capture(root):
    return {name: digest(root / name) for name in SOURCES}


def validate(candidate, base):
    manifest = json.loads((candidate / "context.json").read_text())
    if manifest.get("sources") != capture(base):
        raise ValueError("STALE_CONTEXT: capture the trusted base again")
    if manifest.get("policy_version") != json.loads((base / "policy.json").read_text())["version"]:
        raise ValueError("POLICY_DRIFT: reload the approved policy")
    req = json.loads((candidate / "requirement.json").read_text())
    config = json.loads((candidate / "config.json").read_text())
    proposal = json.loads((candidate / "proposal.json").read_text())
    if req.get("source_id") != "REQ-17" or req.get("status") != "approved":
        raise ValueError("INVALID_REQUIREMENT")
    days = req.get("retention_days")
    if type(days) is not int or days <= 0:
        raise ValueError("INVALID_RETENTION")
    if config.get("retention_days") != days:
        raise ValueError("IMPLEMENTATION_CONFLICT")
    if (candidate / "runbook.md").read_text().splitlines()[0] != f"Retention days: {days}":
        raise ValueError("RUNBOOK_CONFLICT")
    original = json.loads((base / "requirement.json").read_text())
    if proposal.get("base_revision") != original["revision"]:
        raise ValueError("STALE_PROPOSAL")
    if proposal.get("proposal_id") != manifest.get("proposal_id"):
        raise ValueError("PROPOSAL_MISMATCH")
    if proposal.get("from_days") != original["retention_days"] or proposal.get("to_days") != days:
        raise ValueError("PROPOSAL_CONFLICT")
    if req != original and req.get("revision") != original["revision"] + 1:
        raise ValueError("INVALID_REVISION")
    return "PASS: consistency only, human approval remains required"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("capture", "validate"))
    parser.add_argument("--base", type=Path, required=True)
    parser.add_argument("--candidate", type=Path)
    args = parser.parse_args()
    if args.command == "capture":
        policy = json.loads((args.base / "policy.json").read_text())
        print(json.dumps({"proposal_id": "PROP-042", "policy_version": policy["version"],
                          "sources": capture(args.base)}, indent=2))
    else:
        if args.candidate is None:
            parser.error("validate requires --candidate")
        try:
            print(validate(args.candidate, args.base))
        except (ValueError, KeyError, OSError) as exc:
            parser.exit(1, f"FAIL: {exc}\n")


if __name__ == "__main__":
    main()