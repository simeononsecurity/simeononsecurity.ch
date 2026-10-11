"""Offline policy test for a fictional comment tool. No network calls."""

from __future__ import annotations

import hashlib
import json
import secrets
import time

TARGET = "TEST-104"
IDENTITY = "lab-commenter"
STATE_DIGEST = hashlib.sha256(b"synthetic-issue-state-v1").hexdigest()
MAX_CHARS = 2000
MAX_ACTIONS = 5


def action_digest(request: dict[str, str], identity: str, state: str, expiry: float) -> str:
    """Bind the approved action to its preview, identity, target state, and expiry."""
    payload = {
        "action": "post_comment",
        "target": request["target"],
        "comment": request["comment"],
        "preview_digest": hashlib.sha256(request["comment"].encode()).hexdigest(),
        "identity": identity,
        "target_state_digest": state,
        "policy_version": "lab-v2",
        "expires_at": expiry,
    }
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(encoded).hexdigest()


class Policy:
    """The host owns identity, target state, and approvals, outside tool arguments."""

    def __init__(self, identity: str = IDENTITY) -> None:
        self.identity = identity
        self.current_state = STATE_DIGEST
        self.approvals: dict[str, tuple[str, float]] = {}
        self.used: set[str] = set()
        self.count = 0
        self.events: list[dict[str, str]] = []

    def host_approve(self, request: dict[str, str]) -> str:
        """Simulate a trusted host recording human approval, never a tool call."""
        expiry = time.monotonic() + 60
        token = secrets.token_urlsafe(24)
        self.approvals[token] = (
            action_digest(request, self.identity, self.current_state, expiry),
            expiry,
        )
        return token

    def check(self, request: dict[str, str], token: str, *, host_origin: str) -> str:
        """host_origin comes from the host, never from the tool request."""
        record = self.approvals.get(token)
        if host_origin != "approved_user_task":
            result = "deny_origin"
        elif self.identity != IDENTITY:
            result = "deny_identity"
        elif request["target"] != TARGET:
            result = "deny_target"
        elif len(request["comment"]) > MAX_CHARS:
            result = "deny_length"
        elif not record:
            result = "deny_approval"
        elif token in self.used:
            result = "deny_replay"
        elif time.monotonic() >= record[1]:
            result = "deny_expired"
        elif action_digest(request, self.identity, self.current_state, record[1]) != record[0]:
            result = "deny_changed_action"
        elif self.count >= MAX_ACTIONS:
            result = "deny_rate"
        else:
            self.used.add(token)
            self.count += 1
            result = "would_post"
        self.events.append({"target": request["target"], "decision": result})
        return result


def make_request(**changes: str) -> dict[str, str]:
    request = {"target": TARGET, "comment": "I reviewed the test issue."}
    request.update(changes)
    return request


def main() -> int:
    policy = Policy()
    results: list[tuple[str, str, str]] = []

    hostile = make_request()
    results.append(("hostile issue", "deny_origin", policy.check(hostile, "", host_origin="retrieved_issue_text")))

    valid = make_request()
    approval = policy.host_approve(valid)
    results.append(("approved comment", "would_post", policy.check(valid, approval, host_origin="approved_user_task")))
    results.append(("approval replay", "deny_replay", policy.check(valid, approval, host_origin="approved_user_task")))

    forged = make_request(comment="I approve myself.")
    fake_token = action_digest(forged, IDENTITY, STATE_DIGEST, time.monotonic() + 60)
    results.append(("forged self-approval", "deny_approval", policy.check(forged, fake_token, host_origin="approved_user_task")))

    wrong_target = make_request(target="OTHER-999")
    results.append(("wrong target", "deny_target", policy.check(wrong_target, policy.host_approve(wrong_target), host_origin="approved_user_task")))

    oversize = make_request(comment="X" * (MAX_CHARS + 1))
    results.append(("oversize comment", "deny_length", policy.check(oversize, policy.host_approve(oversize), host_origin="approved_user_task")))

    wrong_identity_policy = Policy(identity="shared-admin")
    results.append(("wrong identity", "deny_identity", wrong_identity_policy.check(valid, wrong_identity_policy.host_approve(valid), host_origin="approved_user_task")))

    changed = make_request(comment="Target state changed.")
    changed_token = policy.host_approve(changed)
    policy.current_state = hashlib.sha256(b"synthetic-issue-state-v2").hexdigest()
    results.append(("changed target", "deny_changed_action", policy.check(changed, changed_token, host_origin="approved_user_task")))
    policy.current_state = STATE_DIGEST

    for number in range(2, 6):
        request = make_request(comment=f"Approved test comment {number}.")
        policy.check(request, policy.host_approve(request), host_origin="approved_user_task")
    sixth = make_request(comment="Approved test comment 6.")
    results.append(("sixth action", "deny_rate", policy.check(sixth, policy.host_approve(sixth), host_origin="approved_user_task")))

    passed = 0
    for name, expected, observed in results:
        ok = expected == observed
        passed += ok
        print(f"{name}: expected={expected} observed={observed} {'PASS' if ok else 'FAIL'}")
    print(f"{passed}/{len(results)} passed")
    return 0 if passed == len(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
