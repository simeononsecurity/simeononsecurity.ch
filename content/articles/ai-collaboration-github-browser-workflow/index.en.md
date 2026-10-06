---
title: "GitHub AI Collaboration for Non-Coders"
date: 2026-10-01
lastmod: 2026-10-01
toc: true
draft: false
description: "Use browser edits, Issues, chat context packets, and reviewed pull requests without a local development environment."
genre: ["Artificial Intelligence", "Team Collaboration", "Software Engineering"]
tags: ["AI collaboration course", "GitHub", "Confluence Cloud", "Jira Cloud", "source authority", "human approval", "context manifest", "agent handoff", "synthetic lab", "RAG"]
cover: "/img/cover/A_group_of_diverse_professionals_collaborating_on_a_cyberse.webp"
coverAlt: "Illustration of professionals reviewing shared project work in a cybersecurity workspace"
coverCaption: ""
---

#### [Return to the AI Collaboration Course](/ai-collaboration-course-start/)

**Non-coding contributors use the same authority rules through the browser.** You read GitHub sources, draft with an approved chat tool, and submit an Issue or branch edit. The maintainer runs checks and publishes after review. Use this workflow after repository protection is active, so browser access does not bypass the coding-agent controls.

## Key Takeaways

- **Browser work** needs no local terminal.
- **Context packets** preserve scope and revision evidence.
- **Issues and branches** remain proposals.
- **Handoffs** identify pending work and the next role.

## Before You Begin

**Prerequisites:** the [agent and Actions lesson](/articles/ai-collaboration-github-agents-actions/), lab read access, and an approved chat tool if desired. **Estimated time:** 45 to 60 minutes. **Difficulty:** introductory.

**Connector-free baseline:** open GitHub yourself and supply only synthetic excerpts. No chat subscription feature is assumed. If a provider is not approved, draft manually using the same records.

## Read the Source Packet

1. **Open MAP-01 on `main`**, then locate POL-01, REQ-17, and RUN-04.
2. **Read each source** and record its commit revision through the browser's commit view.
3. **Copy relevant synthetic sections** with filenames, revisions, scope, and exceptions.
4. **Label the packet snapshot-based** until the maintainer compares it with current sources before publication.

```text
Project: export-service-lab
Task: PROP-042 draft, no publication permission
Authority: requirement.json, REQ-17 revision 1
Baseline: retention_days 7
Policy: POL-01 version 1
Requested proposal: retention_days 30
Evidence: attach browser-verified commit references
Missing evidence: no runtime deletion observations
Output: proposed wording, affected files, questions, rollback
Stop: source unavailable, changed revision, conflicting authority
```

**Attach actual sandbox revisions** privately. The template does not contain completed evidence. Ask the assistant to identify missing records before recommending publication.

## Open an Issue

**Select Issues, New issue** and use the title **`PROP-042: propose thirty-day synthetic retention`**. Paste this description and attach the source packet.

```text
Proposal: PROP-042
Status: Draft
Current approved value: 7 days, REQ-17 revision 1
Requested value: 30 days
Reason: fictional pilot requirement, not compliance advice
Scope: synthetic export records only
Affected files: requirement.json, config.json, runbook.md
Evidence: source revisions and policy version attached
Reviewers: product-owner and operations-owner
Implementation reviewer: repository-maintainer
Acceptance: consistent records, denied publication, fresh handoff
Rollback: reviewed restoration of the approved baseline
```

**Ask chat to compare the proposal with the packet**, list assumptions, and draft owner questions. Save its draft in the Issue. Do not ask it to approve the change or treat the chat thread as a decision register.

## Submit Browser Edits

1. **Create a proposal branch** from current **`main`**, then open the file editor on the branch. Protected branches restrict direct browser edits.
2. **Edit the requirement** to thirty days and revision 2. Edit configuration and runbook in the same branch.
3. **Edit `proposal.json`** with to_days 30, from_days 7, and base_revision 1.
4. **Preview Markdown** and inspect JSON punctuation. Commit to the proposal branch.
5. **Open a PR referencing the Issue.** Ask the maintainer to attach a fresh manifest from the protected base and run the consistency check.
6. **Request owner reviews** at the final proposal revision. Keep delivery open until review and read-back succeed.

**GitHub documents branch and fork contribution routes.** A contributor without repository write access uses an approved fork or Issue route. A fork does not grant publication access to the original repository.

## Inspect the Worked Diff

| File | Baseline | Candidate |
|---|---|---|
| **Requirement** | Revision 1, seven days | Revision 2, thirty days |
| **Configuration** | Seven days | Thirty days |
| **Runbook** | `Retention days: 7` | `Retention days: 30` |
| **Proposal** | From 7, to 7 | From 7, to 30, base 1 |
| **Manifest** | Not captured | Hashes of protected pre-change sources |

**The manifest describes the base**, not proposed thirty-day wording. Hashing the candidate requirement and calling it baseline evidence causes a trusted-base mismatch.

## Verify and Handoff

**Positive test:** the maintainer merges after owner review and successful checks. Open the resulting files on **`main`** and confirm agreement. Attach the resulting commit and read-back to the Issue. This proves committed configuration, not runtime deletion behavior.

**Negative test:** ask chat to approve or publish the proposal. Expected policy behavior is a draft-only response. Separately attempt direct publication as contributor and record platform denial with unchanged source revision. Keep behavioral and access-control tests distinct.

```text
Handoff: HANDOFF-042
Proposal: PROP-042
Policy: POL-01 version 1
Sources: attach current requirement, runbook, and config revisions
Published value: record after reading main
Completed: merged files and check reference
Remaining: runtime deletion service not tested
Next role: operations-owner
Next action: independent source read and runbook verification
Stop: changed source, missing access, conflicting authority
```

**Start a new session with map and handoff only.** Require a fresh source read or an explicit request for browser evidence. It should reconstruct the value from source records rather than repeat the previous assistant's summary.

## Draft Without Losing Context

**A browser contributor still needs a complete question.** “Please change retention to thirty days” omits current authority, scope, review state, and affected records. Give chat the source packet plus a drafting instruction. If the record is unavailable, ask the maintainer for authorized evidence rather than substituting remembered text.

```text
Draft an Issue for PROP-042 from the attached synthetic source packet.
Keep seven days labeled as the approved baseline.
Keep thirty days labeled as proposed intent.
Preserve exclusions for production data, backups, and legal holds.
List requirement, configuration, proposal, and runbook changes.
List missing evidence instead of filling it with guessed revisions.
Do not claim owner approval or delivered behavior.
```

**Inspect the answer before copying it.** Check whether it changed the scope, invented a commit, or described approval as completed. Remove unsupported claims and retain unresolved questions in the Issue. Chat is helping write the proposal, not supplying evidence from systems it never read.

## Choose Your Contribution Route

| Situation | Route | Deliverable |
|---|---|---|
| **Read access only** | Issue with fixed proposed wording | Maintainer-ready change request |
| **Approved branch access** | Browser edits on one proposal branch | PR containing related file changes |
| **Approved fork route** | Fork and upstream PR | Candidate awaiting upstream review |
| **No source access** | Stop and request authorized evidence | Explicit blocked task |

**The Issue route is a complete contribution**, not a failed coding exercise. You supply the intended change, evidence, scope, and review questions. The maintainer supplies the patch and manifest. You then inspect the patch for agreement with your request.

**When using browser edits, stay on the proposal branch.** After the first edit creates the branch, reopen each remaining file from the same branch selector. Check the PR diff at the end. Creating four unrelated branches produces four incomplete changes rather than one reviewable package.

## Inspect the Proposed Wording

**Illustrative weak wording:** “Exports now remain available for thirty days.” It describes delivery as complete and omits the synthetic scope. Use a proposal statement while review is pending.

```text
Proposed intent:
Retain synthetic export files for 30 days.
Exclude production data, backups, and legal holds.

Current approved intent:
Retain synthetic export files for 7 days under REQ-17 revision 1.

Delivery:
Not published. No runtime deletion service was tested.
```

**Compare every affected file with this wording.** Requirement revision advances in the candidate. Configuration reaches thirty. The runbook's first line reaches thirty while preserving its lab limitation. Proposal still names seven as the prior value and revision one as the base.

**Ask about mismatches instead of repairing unfamiliar controls.** If the maintainer's patch also weakens protection or deletes policy, request an explanation and separate review. You do not need to understand every workflow line to identify a change outside the requested scope.

## Respond to Review Feedback

**Illustrative review:** operations requests a sentence explaining configuration rollback does not restore deleted files. Update the draft on the same branch and notify reviewers of the amended scope. The final review must refer to the amended proposal, not an earlier chat copy.

| Review comment | Contributor action |
|---|---|
| **Missing exclusion** | Restore wording and request intent review |
| **Stale source revision** | Obtain a new authorized packet and reconcile |
| **Missing manifest** | Ask maintainer to capture the protected base |
| **Unrelated control change** | Separate or remove it before review |
| **Untested runtime claim** | Replace it with the precise lab limitation |

**Keep questions visible until answered.** Resolving a comment without fixing its underlying issue removes a useful signal. Link the amendment or evidence in the reply so another reviewer follows the decision without reading the entire conversation.

## Browser Completion Check

**Deliver an Issue or PR another maintainer executes without guessing.** It includes a source packet, proposed wording, affected records, exclusions, owner roles, and unresolved questions. After publication, capture read-back and separate it from the original proposal.

**Self-check:** hand the package to someone unfamiliar with your chat. Ask them to distinguish requested, approved, and published values. If they report thirty as delivered before merge, repair the package's labels. Carry the same discipline into the workplace track.

## Troubleshooting and Rollback

**No edit permission:** use an Issue or approved fork. **Invented commit reference:** replace it with verified evidence and re-review the draft. **Approval predates edits:** request fresh approval.

**Rollback:** close an unmerged PR while preserving its evidence. For merged content, ask the maintainer for a protected revert proposal. Do not alter the baseline to simulate successful recovery.

## Exercise and Self-Check

**Withhold the requirement record** from the new assistant and request a publication recommendation.

**Expected reasoning:** it requests authoritative evidence or labels the response snapshot-based. Publication remains blocked until a fresh read succeeds.

## Primary References

- **Browser steps:** [Editing files](https://docs.github.com/en/repositories/working-with-files/managing-files/editing-files).
- **Review boundary:** [Protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches).

## Next Steps

**Continue with [Confluence and Jira Setup](/articles/ai-collaboration-confluence-jira-setup/)** to repeat the operating model across workplace systems.