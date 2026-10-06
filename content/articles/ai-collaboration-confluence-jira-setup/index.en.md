---
title: "AI Collaboration with Confluence and Jira: Setup"
date: 2026-10-01
lastmod: 2026-10-01
toc: true
draft: false
description: "Configure Confluence authority pages and company-managed Jira permissions for reviewed mixed-team collaboration."
genre: ["Artificial Intelligence", "Team Collaboration", "Software Engineering"]
tags: ["AI collaboration course", "GitHub", "Confluence Cloud", "Jira Cloud", "source authority", "human approval", "context manifest", "agent handoff", "synthetic lab", "RAG"]
cover: "/img/cover/A_group_of_diverse_professionals_collaborating_on_a_cyberse.webp"
coverAlt: "Illustration of professionals reviewing shared project work in a cybersecurity workspace"
coverCaption: ""
---

#### [Return to the AI Collaboration Course](/ai-collaboration-course-start/)

**The administrator configures workplace authority before connecting chat tools.** Product and operations owners publish requirements and runbooks in Confluence Cloud. Jira Cloud coordinates delivery. GitHub owns implementation. You build dedicated sandboxes after the foundation, because an incorrect permission grant exposes information independently of model behavior.

## Key Takeaways

- **Confluence** owns approved requirement wording.
- **Jira** owns delivery state, not retention policy.
- **GitHub** owns configuration and shared policy.
- **Permission tests** require suitable plans and separate users.

## Before You Begin

**Prerequisites:** the [foundation](/articles/ai-collaboration-pilot-foundation/), lab repository, Confluence space administration, Jira administration, and separate contributor, owner, and publisher users. **Estimated time:** 90 to 120 minutes. **Difficulty:** advanced administration.

**Plan requirement:** Confluence Free does not support content restrictions. Jira Free lacks configurable permission schemes, space roles, and work-item security schemes. Use suitable Standard-or-higher sandboxes for this track. Verify the actual plan and privileges against the references before testing.

**Navigation note:** current Jira documentation uses “space” and “work item.” Some tenants retain “project” and “issue.” Select a company-managed configuration. Team-managed permission behavior is outside this procedure. No Rovo, marketplace app, Jira Service Management approvals, or paid chat connector is required.

## Create Authority Pages

1. **Create a Confluence space** named **`Export Service Lab`**. Keep anonymous access and public sharing disabled through available site/space controls.
2. **Create published pages**, not live docs, named **`REQ-17 Export Retention`**, **`RUN-04 Export Cleanup`**, and **`Decision Register`**.
3. **Publish the initial requirement** below as the product owner. Record its actual page ID and version in the repository map.
4. **Publish RUN-04** as operations owner with seven-day retention and the statement explaining no deletion job runs in this lab.
5. **Open Share** on each authoritative page. Set general access to view-only for eligible space members and grant specific edit access to designated owners/publishers. Save and verify with the contributor user.

```text
Source ID: REQ-17
Owner role: product-owner
Status: Approved baseline
Scope: synthetic export files only
Retention: 7 days
Delivery state: baseline lab configuration
Exceptions: production data, backups, and legal holds excluded
Approval evidence: DEC-12 baseline review
Implementation reference: attach protected GitHub baseline commit
```

**Apply restrictions to each authoritative page.** Do not assume a parent's edit restriction protects its children. View and edit inheritance differ, and space permissions still apply. A link alone does not grant access. Inspect all memberships when an allegedly read-only user still edits.

## Update the Map

```yaml
track: mixed-workplace
policy: {source_id: POL-01, home: GitHub, version: 1}
requirements: {source_id: REQ-17, home: Confluence, owner_role: product-owner}
runbook: {source_id: RUN-04, home: Confluence, owner_role: operations-owner}
decisions: {source_id: DEC-12, home: Confluence, owner_role: project-lead}
implementation: {home: GitHub, file: config.json}
delivery: {home: Jira, proposal_id: PROP-042}
snapshot_rule: repository requirement copies are not authoritative
```

**Add actual private sandbox locations and page IDs** to the map. The template names authority without pretending to contain live addresses. Remove README wording assigning mixed-track requirement authority to the copied JSON file.

**Keep POL-01 in GitHub** for both tracks. Confluence links to its reviewed revision. Moving policy authority during a task requires another reviewed authority transition.

## Set Jira Permissions

1. **Create a company-managed lab space** and copy a permission scheme into a dedicated lab scheme. Do not edit a shared production scheme.
2. **Open Settings, Work items, Permission Schemes**, then select the lab scheme and update grants.
3. **Grant browse, create, and comment** to contributors. Restrict administrative privileges. Review editing and **Transition work items** permissions explicitly.
4. **Associate the scheme** with the lab space and verify no production space shares it.
5. **Create PROP-042** as a work item. Record its generated key in the map and keep PROP-042 as the logical proposal ID in its description.

| Role | Confluence | Jira | GitHub |
|---|---|---|---|
| **Contributor** | Read approved pages | Create/comment on drafts | Proposal branch or Issue |
| **Product owner** | Review requirement | Record requirement review | Review PR evidence |
| **Operations owner** | Review runbook | Record operational review | Review operational impact |
| **Publisher** | Edit approved pages | Record publication state | No automatic merge authority |
| **Maintainer** | Read requirement | Record implementation | Review/merge protected PR |

**Grants across groups are additive.** Remove unintended broad grants in the lab rather than assuming a narrow grant overrides them. Keep connector identities out of administrative groups.

## Set Delivery States

**Copy a company-managed workflow** into a lab-only workflow. Add Draft, Review, Approved, Publishing, Done, and Blocked states. Add submission, approval, publication, completion, blocking, and return-to-review transitions. Associate it with the lab work type only.

1. **Select the transition into Approved** in the workflow editor.
2. **Add a condition/restriction** limiting the actor to the designated owner/publisher role or group. Use the documented condition controls and publish the workflow draft as administrator.
3. **Check both owner reviews manually** before transition. Each review identifies the frozen proposal and source versions.
4. **Restrict Done** to the accountable delivery role. Remove alternate/global transitions bypassing the boundary.

**A restricted transition is not two-person approval.** It controls the actor performing the transition. The two-role evidence check remains procedural in this pilot. Record this limit explicitly.

## Verify Denial

**As contributor**, read REQ-17, attempt an edit, create the Jira draft, and attempt the Approved transition. Expected results are readable requirement, denied edit, successful proposal creation, and denied approval transition. Compare source versions before and after denial.

**As an excluded user**, open a separately restricted synthetic page. Expect no content access. Test child pages independently. Do not paste protected text into the excluded user's chat as a workaround.

## Translate the Repository Map

**Keep source IDs stable when their homes change.** REQ-17 still means approved retention intent, but its mixed-track home is a Confluence page. A repository snapshot supports checks and review. It does not replace the page's authority.

| Record | Authoritative home | Repository treatment |
|---|---|---|
| **REQ-17** | Mapped Confluence requirement page | Captured snapshot with page revision evidence |
| **RUN-04** | Mapped Confluence runbook page | Captured operating excerpt for consistency |
| **POL-01** | Protected GitHub policy | Shared agent instructions reference it |
| **Configuration** | Protected GitHub record | Proposed implementation diff |
| **Delivery** | Jira work item | Correlation link rather than policy copy |

**Add capture provenance alongside snapshots.** Record source ID, page reference, page version, capture time, and capturing role in the private proposal packet. Keep native page identifiers out of public course submissions. If the publisher finds a different live version, reconcile before using the snapshot.

**Do not rename authority to fit the tool.** Jira's editable description is convenient for discussion, but it remains a delivery record. A thirty-day sentence in Jira does not supersede a seven-day requirement in Confluence.

## Design the Access Tests

**Separate reading, drafting, and publishing.** A contributor needs enough access to understand the synthetic requirement and submit a proposal. They do not need authority-page edit access or permission to mark their own proposal approved.

```text
Test record: PERM-REQ-EDIT
Role: contributor
Source: REQ-17
Precondition: source is readable, published revision captured
Attempt: edit the authoritative requirement
Expected: edit denied, published revision unchanged
Observed: fill from the sandbox
Evidence: native result and independent revision read-back
Reviewer: administrator or independent permission reviewer
```

**Use a separate record for denied reading.** The contributor's readable requirement tests publication separation. An excluded user's inaccessible page tests confidentiality. Combining them into one row hides which boundary was exercised.

**Check positive access too.** Owners and publishers need their assigned route to work. If every user is denied, the sandbox is restrictive but unusable. Retain a successful authorized edit on a disposable test page without altering the approved requirement during permission diagnosis.

## Rehearse the Jira Review

**Treat the state names as this pilot's design.** Draft contains a request. Review contains a frozen package. Approved records completed owner review. Publishing records incomplete delivery. Done requires read-back. Blocked names missing evidence, access, or unresolved conflict.

| Transition | Required packet | Accountable check |
|---|---|---|
| **Draft to Review** | Fixed proposal and source versions | Contributor confirms completeness |
| **Review to Approved** | Product and operations decisions | Authorized actor checks both roles |
| **Approved to Publishing** | Current-source comparison | Publisher confirms unchanged bases |
| **Publishing to Done** | Completed per-system ledger | Delivery owner checks read-back |
| **Any supported step to Blocked** | Failure and pending action | Recovery owner assigned |

**Rehearse with a synthetic incomplete package.** Submit only a product review and ask the authorized transition actor to assess it. Expected reasoning is to leave work in Review and request operations review. This tests the procedural review step separately from the contributor's platform denial.

**Test alternate routes deliberately.** Use your sandbox workflow view to inspect every route into Approved and Done. A restricted named transition is insufficient if another available route skips the same review boundary. Record the routes inspected and the actor used, rather than claiming complete coverage from one click.

## Diagnose Unexpected Access

**Start with the effective identity.** Confirm the browser session belongs to the intended test role. Then inspect group membership, space grants, page access, and workflow association using the product's administration tools. Do not change several controls at once, because the resulting denial loses its diagnostic value.

1. **Confirm identity:** separate contributor, publisher, and excluded-user sessions.
2. **Locate the grant:** identify the membership or setting permitting the attempted action.
3. **Adjust the lab control:** retain legitimate owner access.
4. **Repeat the same attempt:** capture unchanged source revision after denial.
5. **Repeat the positive case:** confirm authorized publication still works.

**Completion check:** deliver the mapped authority pages, lab-only workflow, intended role matrix, and observed permission records. If the plan lacks a required control, leave the relevant row Blocked. The publication lesson assumes these tests succeeded, not merely the existence of settings screenshots.

## Troubleshooting and Rollback

**Contributor still edits:** inspect page access, space grants, and memberships. **Transition still succeeds:** inspect workflow association and bypass routes. **Settings missing:** verify company-managed type, edition, and administrator permission.

**Rollback:** remove connector grants and archive drafts. Detach lab-only schemes/workflows after retaining evidence. Restore approved page wording through reviewed history or a compensating edit. Do not delete audit evidence.

## Exercise and Self-Check

**Jira says thirty days while REQ-17 says seven.** Identify the implementation input and reconciliation owner.

**Expected reasoning:** Confluence governs intent. Jira contains a proposal or delivery error. Stop publication and ask the product owner to reconcile, rather than choosing the newest timestamp.

## Primary References

- **Restrictions and plan:** [Confluence permissions](https://support.atlassian.com/confluence-cloud/docs/manage-permissions-on-the-page-level/).
- **Share controls:** [Specific content access](https://support.atlassian.com/confluence-cloud/docs/add-or-remove-page-restrictions/).
- **Scheme administration:** [Jira permission schemes](https://support.atlassian.com/jira-cloud-administration/docs/grant-or-revoke-permissions-in-a-scheme/).
- **Transition conditions:** [Advanced workflows](https://support.atlassian.com/jira-cloud-administration/docs/configure-advanced-issue-workflows/).

## Next Steps

**Continue with [Cross-System Publication](/articles/ai-collaboration-confluence-jira-publication/)** after the permission tests pass.