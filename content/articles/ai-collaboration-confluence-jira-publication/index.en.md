---
title: "AI Collaboration Across GitHub, Confluence, and Jira"
date: 2026-10-01
lastmod: 2026-10-01
toc: true
draft: false
description: "Publish a fixed retention proposal across Confluence, GitHub, and Jira with version checks and partial-publication recovery."
genre: ["Artificial Intelligence", "Team Collaboration", "Software Engineering"]
tags: ["AI collaboration course", "GitHub", "Confluence Cloud", "Jira Cloud", "source authority", "human approval", "context manifest", "agent handoff", "synthetic lab", "RAG"]
cover: "/img/cover/A_group_of_diverse_professionals_collaborating_on_a_cyberse.webp"
coverAlt: "Illustration of professionals reviewing shared project work in a cybersecurity workspace"
coverCaption: ""
---

#### [Return to the AI Collaboration Course](/ai-collaboration-course-start/)

**The contributor freezes PROP-042 before owners approve it.** A Confluence publisher updates requirements, a GitHub maintainer merges implementation, and operations publishes the runbook. Jira records each step. Perform this after permission verification, because the three systems do not form one atomic transaction. Your publication ledger makes incomplete delivery visible.

## Key Takeaways

- **Approved intent** differs from delivered behavior.
- **Fixed proposal revisions** bind review.
- **Publication ledgers** expose partial completion.
- **Fresh reads** protect against changed bases.

## Before You Begin

**Prerequisites:** the [workplace setup](/articles/ai-collaboration-confluence-jira-setup/), publisher access, owners, and repository maintainer. **Estimated time:** two hours. **Difficulty:** advanced coordination.

**Baseline interface:** browser reads, optional approved chat drafting, and human publication. No connector subscription is assumed. Review tenant availability, scopes, provider handling, and identity mapping before adding an integration. Never share an owner's credential with a contributor.

## Capture Live Sources

1. **Read MAP-01**, then open REQ-17 and RUN-04 by mapped page ID.
2. **Open the page menu, Page History**, and capture numeric versions, status, wording, owner, and exceptions.
3. **Read the Jira item** and attach a fixed proposal export or GitHub commit. Its key alone does not freeze review evidence.
4. **Read approved POL-01** and the protected configuration baseline.
5. **Supply only needed synthetic excerpts** to chat, marking them as snapshots and keeping write-capable actions disabled.

```text
Task: PROP-042, propose only
Authority: Confluence REQ-17 for intent, GitHub for behavior
Read: mapped current pages, versions, scope, exceptions
Proposal: synthetic export retention from 7 to 30 days
Output: requirement wording, config diff, runbook, ledger
Evidence: source ID and captured revision for each factual claim
Unknowns: missing access and absent runtime observations
Stop: conflict, changed base, or denied access
```

**Offline packets remain snapshot-based.** The publisher repeats live reads before writing. Access denial blocks publication. An old export is not a substitute for current authorization.

## Freeze the Proposal

```json
{
  "proposal_id": "PROP-042",
  "proposal_revision": 1,
  "requirement_base_version": 1,
  "runbook_base_version": 1,
  "policy_version": 1,
  "from_days": 7,
  "to_days": 30,
  "status": "awaiting-owner-review",
  "publication_order": ["requirement", "implementation", "runbook", "delivery"]
}
```

**Replace illustrative page versions with actual captured versions.** Attach the fixed JSON and proposed wording to Jira. Each owner records role, decision, proposal revision, source versions, and review time. Any substantive edit returns the package to Review.

**Product reviews intent and scope. Operations reviews cleanup and recovery.** The maintainer reviews the diff. Reactions on mutable chat messages are not revision-bound approvals.

## Publish and Read Back

1. **Move Jira to Publishing** after the publisher verifies both owner reviews and unchanged source bases.
2. **Publish REQ-17** with thirty days and a pending-delivery field. Record the resulting version, scope, and exceptions.
3. **Open the GitHub implementation PR**, referencing the approved page version. Change configuration to thirty days and attach a non-authoritative requirement snapshot.
4. **Merge after repository review** and read **`main`** back. Record committed behavior separately from runtime behavior.
5. **Publish RUN-04**, read it back by ID, and record its resulting version. Update requirement delivery references through the publisher.
6. **Complete Jira** only after all records agree and the final read-back evidence is attached.

**Use the local validator for snapshot consistency only.** Copy the pre-change Confluence requirement into the lab's baseline JSON schema, capture it, and edit the candidate to thirty days. Use an incremented local snapshot revision while separately preserving actual Confluence versions in Jira. The GitHub-first root-source workflow is not a live Confluence validator. Do not present its green status as verification of external authority.

**Do not deploy deletion in this exercise.** A real service needs deployment evidence, controlled test data, a hold mechanism, and runtime boundary tests. A merge proves repository state, not retention behavior in production.

## Track Partial Publication

| Step | Initial state | Completion evidence |
|---|---|---|
| **REQ-17** | Pending | Resulting page version |
| **Configuration** | Pending | Merged commit and review |
| **RUN-04** | Pending | Resulting page version |
| **Jira closure** | Pending | Final read-back and transition |

**Write each result before attempting the next step.** PROP-042 correlates the individual system events. One completed row never means the entire change is complete.

**Worked failure:** Confluence publishes thirty days, but GitHub denies merge. Keep Jira Blocked and the requirement marked pending delivery. Product chooses forward completion or reviewed restoration to seven days. Do not promote an emergency README copy into requirement authority.

## Handle Concurrent Edits

**Browser baseline:** appoint one publisher during the pilot window. Reopen Page History immediately before editing and after publishing. If another writer changes the source, stop, compare, reconcile, and renew approval. Serialized publication is a procedure, not an atomic transaction guarantee.

**API extension:** Confluence v2 documents **`GET /wiki/api/v2/pages/{id}?body-format=storage`** and **`PUT /wiki/api/v2/pages/{id}`** with a version object. A reviewed publisher integration compares the current version with the approved base, submits the next version, and reads back. Never refresh a failed version automatically and retry an old body.

**API success alone is insufficient.** Check resulting content, source ID, scope, and version. This course supplies no write-capable API client. Human browser publication is the executable baseline for non-coders.

## Verify Negative Cases

| Injection | Expected reasoning |
|---|---|
| **Change source after approval** | Stop and reapprove against new version |
| **Remove publisher edit access** | Deny update, retain pending ledger |
| **Set Jira to sixty days** | Stop conflict and preserve Confluence authority |
| **Runbook publication fails** | Keep delivery incomplete and assign recovery |

**Record actual sandbox results** with actor role and revisions before/after. Do not include protected page bodies in denied-user evidence. Expected results are not measured outcomes.

## Assemble the Review Package

**Freeze content, not only the proposal label.** PROP-042 appears in every system, but a label does not identify the body an owner reviewed. Include the exact requirement wording, implementation diff, runbook wording, source versions, and publication sequence in one fixed package.

```text
Package: PROP-042 revision 1, illustrative
Intent: synthetic export retention changes from 7 to 30 days
Exclusions: production data, backups, legal holds
Requirement amendment: fixed proposed REQ-17 wording
Implementation: fixed candidate diff and protected base reference
Runbook amendment: fixed RUN-04 wording and recovery limits
Review: product and operations decisions for this package
Delivery: requirement -> implementation -> runbook -> closure
Stop: changed source, missing review, denied write, failed read-back
```

**Keep the packet readable for both owners.** Product needs intent and exclusions. Operations needs the operating change and recovery boundary. Both need to understand the period when approved intent and delivered configuration differ. A bare code diff is insufficient for an owner unfamiliar with repository files.

**Separate the offline snapshot from live publication.** A consistency pass demonstrates agreement among captured records. Immediately before the first write, the publisher rechecks the mapped pages and the maintainer rechecks the protected base. If either changed, the old package stops at Review.

## Walk Through the Ledger

**Illustrative state progression:** the table uses teaching revisions, not observations. Fill your actual resulting versions and commits after each sandbox write.

| Step | State after successful read-back | Remaining work |
|---|---|---|
| **Owner review complete** | Approved package, all published values seven | All publication steps |
| **REQ-17 published** | Intent thirty, delivery pending | Configuration and runbook |
| **GitHub merge read back** | Intent/configuration thirty, runbook seven | Runbook and final reconciliation |
| **RUN-04 published** | All applicable records thirty | Independent final read-back |
| **Delivery closed** | Complete ledger with evidence | Declared runtime gaps remain |

**Pending delivery is a meaningful state.** It avoids describing the old implementation as compliant with new intent while publication is incomplete. Readers need both values during this period, not a single summary claiming “retention is thirty.”

**Append failed attempts as separate events.** If a runbook write fails, keep the successful requirement and configuration results. Record the attempted runbook action, failure, unchanged version, assigned role, and next action. Do not reset completed rows to Pending and erase the observed sequence.

## Handle an Uncertain Write

**A timeout leaves the outcome unknown.** It does not establish success or failure. In the browser baseline, reopen the mapped source and inspect its current content and history before deciding whether to retry.

1. **Pause the next step:** keep delivery incomplete.
2. **Read the destination:** compare current wording, version, and scope with the fixed package.
3. **Record the observation:** completed, unchanged, conflicting, or inaccessible.
4. **Choose the next action:** continue from verified completion, retry an authorized unchanged step, or escalate a conflict.
5. **Retain the uncertainty:** keep the failed/unknown attempt alongside the later read-back.

**Do not replay the whole sequence blindly.** Repeating an already completed step adds revisions and risks overwriting unrelated edits. Resume from verified state. If source access is unavailable, choose Hold rather than guessing from the old ledger.

## Compare Recovery Decisions

| Situation | Decision to review | Reason |
|---|---|---|
| **Requirement changed, merge denied** | Forward or compensate requirement | Intent and behavior differ |
| **Configuration changed, runbook denied** | Finish runbook or back out configuration | Operating guidance is stale |
| **Another owner edits scope** | Return to Review | Frozen approval describes another body |
| **Write outcome unknown** | Read destination first | Retry depends on observed state |
| **Publisher loses access** | Hold and request authorized administration | Old authorization does not permit new writes |

**Choose against the current state and owner decision.** Forward completion needs current approvals and workable controls. Compensation needs review of the restoration against intervening edits. A recovery change is another publication, not a privileged exception to the process.

## Publication Completion Check

**Deliver a package an independent reviewer reconciles.** They should find the exact reviewed proposal, its source bases, both role reviews, each write result, final values, and remaining runtime limitations. Ask them to identify the first incomplete step after an interruption.

**Expected reasoning:** the next action comes from fresh sources plus the ledger, not the previous assistant's confidence. Carry the final mapped references into retrieval tests, where discovery must preserve the same authority distinction.

## Troubleshooting and Recovery

**Version changed:** compare history and renew review. **Snapshot check passes but wiki differs:** fetch current Confluence sources again. **Done too early:** reopen through the allowed workflow and record missing steps.

**Recovery:** use Page History comparison and an owner-reviewed restoration or compensating edit. Record the resulting version rather than assuming restoration resets numbering. Revert configuration through a protected PR if product selects backout. Deleted files remain outside the rollback promise.

## Exercise and Self-Check

**Interrupt after REQ-17 publication** and give another publisher only the map and ledger.

**Expected reasoning:** they fetch current sources, confirm frozen approval, and resume only the authorized pending step. Missing evidence returns work to Review.

## Primary References

- **History and restoration:** [Confluence technical documentation](https://support.atlassian.com/confluence-cloud/docs/use-confluence-for-technical-documentation/).
- **Versioned API operations:** [Confluence REST API v2 pages](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-page/).
- **Workflow controls:** [Jira advanced workflows](https://support.atlassian.com/jira-cloud-administration/docs/configure-advanced-issue-workflows/).
- **Integration security:** [MCP security best practices](https://modelcontextprotocol.io/docs/latest/tutorials/security/security_best_practices).

## Next Steps

**Continue with [Map-First Retrieval](/articles/ai-collaboration-map-first-retrieval/)** after completing a reviewed publication run.