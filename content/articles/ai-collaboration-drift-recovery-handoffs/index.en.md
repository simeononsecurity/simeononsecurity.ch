---
title: "AI Collaboration Operations: Drift, Recovery, and Handoffs"
date: 2026-10-01
lastmod: 2026-10-01
toc: true
draft: false
description: "Detect stale sources and policy adapters, recover interrupted publication, and verify independent agent handoffs."
genre: ["Artificial Intelligence", "Team Collaboration", "Software Engineering"]
tags: ["AI collaboration course", "GitHub", "Confluence Cloud", "Jira Cloud", "source authority", "human approval", "context manifest", "agent handoff", "synthetic lab", "RAG"]
cover: "/img/cover/A_group_of_diverse_professionals_collaborating_on_a_cyberse.webp"
coverAlt: "Illustration of professionals reviewing shared project work in a cybersecurity workspace"
coverCaption: ""
---

#### [Return to the AI Collaboration Course](/ai-collaboration-course-start/)

**Operations checks drift before tasks and after interrupted publication.** You compare source versions, adapter versions, and delivery state in the repository or workplace sandbox. Do this after completing one track. The purpose is to prevent old summaries from becoming current authority and preserve a reviewable recovery history.

## Key Takeaways

- **Source drift** differs from adapter drift.
- **Partial publication** needs a per-system ledger.
- **Recovery** preserves history with reviewed changes.
- **Handoffs** require independent current reads.

## Before You Begin

**Prerequisites:** the [GitHub browser workflow](/articles/ai-collaboration-github-browser-workflow/) or [mixed publication workflow](/articles/ai-collaboration-confluence-jira-publication/). **Estimated time:** 60 to 90 minutes. **Difficulty:** advanced review.

**Safety:** synthetic records only. Freeze automatic publication before recovery tests. No running deletion service is supplied.

## Classify Drift

| Drift | Signal | Repair owner |
|---|---|---|
| **Requirement** | Source differs from manifest | Product owner |
| **Policy** | Adapter differs from POL-01 | Policy owner |
| **Implementation** | Configuration contradicts intent | Maintainer |
| **Runbook** | Instructions contradict approved behavior | Operations owner |
| **Access** | Previously readable source denied | Administrator, task stopped |
| **Delivery** | Done without completed ledger | Delivery owner |

**Newest text is not necessarily approved authority.** A recent unauthorized edit requires investigation, not automatic adoption. Resolve status and ownership before copying values.

## Run Preflight

```text
Read MAP-01 and capture its revision.
Read POL-01 and compare active adapter versions.
Read REQ-17 and RUN-04 from mapped homes.
Read config.json at protected main.
Read frozen proposal and current role reviews.
Compare current sources with reviewed bases.
List mismatches, denied reads, and pending publications.
Stop consequential writes until owners resolve each mismatch.
```

**The contributor runs preflight before drafting. The publisher repeats it before writing.** Retain the version comparison with the proposal. Weekly checks supplement these reads rather than replacing them.

**Worked adapter drift:** POL-01 reaches version 2 while CLAUDE.md still says 1. Stop, read the reviewed policy change, update the adapter through a protected PR, and start a fresh session. Changing only the version number without loading the policy does not repair context.

## Recover Interrupted Publication

1. **Freeze PROP-042 publication** and assign the recovery owner.
2. **Read actual state** across participating systems. Distinguish completed, failed, and not attempted.
3. **Ask product to choose** forward completion, reviewed backout, or hold.
4. **Prepare a recovery proposal** with fresh bases and unchanged scope/exceptions unless explicitly reviewed.
5. **Apply one reviewed step at a time**, recording and reading back each result.
6. **Verify final state** and remaining limits before ordinary work resumes.

```yaml
recovery_id: RECOVERY-042
proposal_id: PROP-042
mode: awaiting-owner-choice
illustrative_state:
  requirement: thirty-days-published
  implementation: seven-days-on-main
  runbook: seven-days
  delivery: blocked
choices:
  forward: finish approved implementation and runbook
  backout: restore baseline through reviewed changes
  hold: wait for evidence or access
```

**Replace illustrative states with observed revisions and values.** A previous ledger entry or assistant claim is not read-back evidence.

| Choice | Use when | Limitation |
|---|---|---|
| **Forward** | Approval remains valid and sources reconcile | Requires fresh verification |
| **Backout** | Owner withdraws change or implementation fails | Does not recover deleted data |
| **Hold** | Evidence or access unavailable | Delivery stays incomplete |

**Choose hold when evidence is missing.** Synthetic exercises provide no operational urgency for blind overwrites. Name the next role and missing evidence.

**GitHub recovery** uses reviewed revert or compensation. **Confluence recovery** uses history comparison and reviewed restoration/compensation. **Jira recovery** preserves proposal history while reopening or blocking delivery. Read resulting revisions rather than assuming history numbering resets.

## Verify Independent Handoff

```text
Handoff: HANDOFF-042
Task: PROP-042
Map and policy: attach current approved revisions
Evidence: requirement, runbook, configuration references
Ledger: completed, failed, pending
Decision: owner choice and fixed proposal revision
Limits: no runtime deletion test or production data
Next role: accountable role
Next action: one bounded step
Stop: changed base, access denial, conflicting authority
```

**Open another tool or clean session** with the map and handoff, not the previous conversation. Require fresh source reads, a new manifest, and identification of the pending action. Manual browser evidence remains valid when labeled snapshot-based and rechecked before writing.

**Negative handoff:** withhold REQ-17 access. Expect an explicit block rather than a guessed value or privileged excerpt. Restore only approved access through administration and repeat verification.

## Diagnose Before Repairing

**Start with a state inventory.** “The assistants disagree” describes an answer symptom, not the underlying source problem. Read the mapped requirement, configuration, runbook, policy, and delivery record independently before asking either assistant to repair them.

| Observation | Diagnosis | First action |
|---|---|---|
| **Both sources agree, old answer differs** | Stale answer context | Reconstruct from fresh reads |
| **Requirement thirty, configuration seven** | Delivery or implementation mismatch | Inspect approved package and ledger |
| **Adapter one, policy two** | Instruction-version mismatch | Read policy change and repair adapter |
| **Source previously readable, now denied** | Access change | Stop task and seek authorized review |
| **Ledger complete, runbook seven** | Closure without valid read-back | Reopen/block delivery and investigate |

**Avoid treating every mismatch as a model problem.** Refreshing a session fixes stale conversational context. It does not publish a runbook, restore a missing permission, or reconcile conflicting owner decisions. Name the repair owner before choosing a tool action.

## Walk Through Compensation

**Illustrative interruption:** REQ-17 contains approved thirty-day intent with delivery pending. Configuration and runbook still contain seven. The maintainer reports an unresolved implementation failure. Product chooses restoration rather than forward completion.

1. **Capture current versions:** requirement thirty, configuration seven, runbook seven, delivery blocked.
2. **Freeze the pending proposal:** retain its reviews and failed publication evidence.
3. **Prepare a compensating requirement amendment:** restore seven while preserving intervening exclusions and notes.
4. **Obtain owner review:** identify the current source version and exact restoration wording.
5. **Publish through the authorized route:** read the resulting requirement version back.
6. **Reconcile the ledger:** all applicable published values seven, original change not delivered.

**Compensation is not history deletion.** Keep the attempted thirty-day change, its failure, and the later restoration as separate records. The final source states seven, while the delivery history explains why the approved proposal did not finish.

```text
Recovery decision: illustrative compensation
Original proposal: PROP-042 revision 1
Observed mismatch: requirement 30, configuration/runbook 7
Owner decision: restore approved baseline intent
Review object: fixed compensation against current requirement version
Result: capture resulting revision and seven-day read-back
Original delivery: withdrawn or blocked with explanation
Limit: no runtime deletion or data restoration performed
```

**If another writer added an exception, preserve it explicitly.** Blindly pasting an old page body risks removing a valid intervening change. Compare current and intended text, then review a minimal compensating amendment against the current version.

## Test a Fresh Handoff

**Use a clean session and a different reviewer.** Supply the map, fixed package, ledger, and recovery decision. Withhold the previous chat. Ask the receiver to state current intent, configuration, operating guidance, and the next authorized action.

```text
Read the mapped current sources independently.
Distinguish approved intent, committed configuration, and delivery state.
Compare them with the reviewed package and ledger.
List missing reads and changed bases.
Recommend one bounded next action with its accountable role.
Do not treat this handoff as approval or publication permission.
```

**Expected reasoning:** the receiver verifies the compensation result before describing the baseline as restored. If they only repeat “seven days” from the handoff, the independent-read requirement remains untested. Request source evidence rather than another summary.

## Decide Whether to Resume

| Preflight result | Resume decision |
|---|---|
| **Sources match fixed approval** | Continue the authorized pending step |
| **Source changed outside reviewed scope** | Stop for comparison and renewed review |
| **Read access missing** | Hold with an assigned access reviewer |
| **Policy changed** | Repair adapters and re-evaluate task permission |
| **Write result unknown** | Read destination before retrying |

**Keep recovery acceptance concrete.** Require matching read-back, a current review object, a reconciled ledger, and a fresh handoff. Do not close the recovery because the assistant says the issue is resolved.

**Completion check:** deliver an observed state inventory, owner decision, reviewed repair, final read-back, and independent reconstruction. If access prevents a read, document the block. Carry this evidence standard into the capstone.

## Troubleshooting and Backout

**Revert conflicts:** prepare a compensating change against current state. **Restore loses exceptions:** compare the full relevant section before writing. **Old memory controls the answer:** restart with approved sources and remove stale draft context.

**Backout of recovery:** stop at the last verified state and append another ledger entry. Do not erase native audit events or force-reset protected history. Escalate unresolved authority to product.

## Exercise and Self-Check

**Inject stale evidence, outdated policy adapter, and partial publication.** Give another reviewer the records without narration and ask for the repair owner.

**Expected reasoning:** product owns requirement reconciliation, policy owner owns adapter alignment, and delivery recovery coordinates participating owners. “Refresh context” is not a complete repair for all cases.

## Primary References

- **Repository recovery controls:** [Protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches).
- **Page history:** [Confluence documentation](https://support.atlassian.com/confluence-cloud/docs/use-confluence-for-technical-documentation/).
- **Instruction inspection:** [Claude Code memory](https://code.claude.com/docs/en/memory).

## Next Steps

**Complete the [Retention Capstone](/articles/ai-collaboration-retention-capstone/)** using both tracks and independent review.