---
title: "GitHub AI Collaboration: Repository and Review Boundaries"
date: 2026-10-01
lastmod: 2026-10-01
toc: true
draft: false
description: "Build a GitHub-first source map, file ownership, and protected publication boundary for reviewed AI contributions."
genre: ["Artificial Intelligence", "Team Collaboration", "Software Engineering"]
tags: ["AI collaboration course", "GitHub", "Confluence Cloud", "Jira Cloud", "source authority", "human approval", "context manifest", "agent handoff", "synthetic lab", "RAG"]
cover: "/img/cover/A_group_of_diverse_professionals_collaborating_on_a_cyberse.webp"
coverAlt: "Illustration of professionals reviewing shared project work in a cybersecurity workspace"
coverCaption: ""
---

#### [Return to the AI Collaboration Course](/ai-collaboration-course-start/)

**The maintainer builds the GitHub-first publication boundary** after charter approval. Requirements, configuration, policy, and runbooks live in one disposable repository. Contributors propose through Issues and pull requests. You establish where approved facts live and block unreviewed changes before attaching agents.

## Key Takeaways

- **Protected `main`** is the publication boundary.
- **Issues** collect proposed work without approving policy.
- **CODEOWNERS** assigns eligible file reviewers.
- **Separate users** demonstrate review and denial controls.

## Before You Begin

**Prerequisites:** the [pilot foundation](/articles/ai-collaboration-pilot-foundation/), extracted lab, repository administrator, and separate product and operations reviewers. **Estimated time:** 60 minutes. **Difficulty:** moderate.

**Plan boundary:** GitHub documents protected branches for public repositories on Free and private repositories on Pro, Team, or Enterprise. Use public repositories only for synthetic content. Verify visibility and plan against the protected-branch reference before relying on enforcement.

## Create the Repository

1. **Create `export-service-lab`** with a README and default branch **`main`**.
2. **Copy the extracted lab** into the repository root, preserving **`check.py`**, **`test_check.py`**, and **`baseline/`**. Copy the baseline record files to the root as initial records.
3. **Create `docs/project-map.md`** using the foundation register. Add **`docs/policy.md`** with approved POL-01.
4. **Create `docs/decisions/DEC-12.md`** with charter approval, roles, baseline decision, and status.
5. **Commit the bootstrap** as administrator. Record this initial exception. Enable protection before subsequent contributions.

| Record | Location | Owner |
|---|---|---|
| **POL-01** | `policy.json`, `docs/policy.md` | Policy owner |
| **REQ-17** | `requirement.json` | Product owner |
| **RUN-04** | `runbook.md` | Operations owner |
| **Behavior** | `config.json` | Maintainer |
| **Decisions** | `docs/decisions/` | Project lead |

**The map links locations rather than copying values.** Keep README focused on setup and the map. Repeated retention requirements create drift even inside one repository.

## Assign File Owners

**Generate `.github/CODEOWNERS`** locally with actual sandbox handles. Enter handles without the leading **`@`**. Keep account identities in your private lab, not public exercise evidence.

```bash
python3 - <<'PY'
from pathlib import Path
roles = ['product', 'operations', 'maintainer', 'policy']
handles = {r: input(r + ' GitHub handle: ').strip().lstrip('@') for r in roles}
if any(not h or not all(c.isalnum() or c == '-' for c in h) for h in handles.values()):
    raise SystemExit('Invalid handle')
paths = {'requirement.json': 'product', 'runbook.md': 'operations',
         'config.json': 'maintainer', 'policy.json': 'policy',
         'docs/policy.md': 'policy', 'AGENTS.md': 'policy',
         'CLAUDE.md': 'policy', '.clinerules/': 'policy',
         '.github/': 'maintainer', 'check.py': 'maintainer',
         'test_check.py': 'maintainer', 'baseline/': 'maintainer'}
Path('.github').mkdir(exist_ok=True)
Path('.github/CODEOWNERS').write_text(''.join(
    '/' + path + ' @' + handles[role] + '\n' for path, role in paths.items()))
PY
```

**Owners need write access** for GitHub to recognize them. Inspect the CODEOWNERS file for errors in the browser. Protect ownership files and workflow definitions along with ordinary content.

**Multiple names on one line do not require all listed owners.** GitHub accepts one eligible owner approval for the matching path. Use distinct designated owners for requirement and runbook paths. The pilot also requires product-owner and operations-owner attestations tied to the final proposal.

## Protect Publication

1. **Open Settings, Branches** and add a branch protection rule for **`main`**. Use the branch-protection route consistently rather than mixing it with rulesets during this exercise.
2. **Require a pull request**, two approving reviews, and review from code owners.
3. **Dismiss stale approvals** after new commits and require conversation resolution.
4. **Enable Do not allow bypassing the above settings.** Keep force pushes and deletion disabled.
5. **Add the consistency check** after its first run in the next module. Require branches to be up to date before merging.

**Two approvals enforce a count, not business-role membership.** CODEOWNERS adds path-based owner coverage. The maintainer also checks the two role attestations. Record this procedural control explicitly instead of describing it as automated two-role enforcement.

**Administrators still manage configuration.** Capture the rule before and after tests. Do not grant an agent administrator access or use a privileged token to demonstrate contributor denial.

## Verify the Boundary

| Attempt | Expected result |
|---|---|
| **Contributor submits a branch** | Proposal permitted |
| **Contributor publishes directly** | Protected publication denied |
| **One reviewer approves** | Merge blocked by review threshold |
| **New commit follows review** | Fresh approval required |
| **Sensitive file lacks owner coverage** | Repair before publication |

**Use the contributor's browser session.** Attempt a harmless synthetic direct edit on **`main`**. A UI directing you to a branch demonstrates the supported route. If you also test an authorized local direct push, retain the server's rejection separately.

**Read `main` after denial** and confirm the revision did not change. Record actor role, attempted action, result, and source revision. An assistant promising not to publish is behavioral evidence, not a platform-permission test.

## Build a Useful Source Map

**A source map is a routing document**, not a second requirements document. Someone arriving from chat needs to find current intent, implemented behavior, and operational instructions without choosing among competing summaries.

```text
Project: export-service-lab
Track: GitHub-first
Approved boundary: protected main

REQ-17 -> requirement.json
  Authority: retention intent for synthetic export files
  Owner: product-owner
  Revision: record revision plus protected commit

RUN-04 -> runbook.md
  Authority: operating instructions for the synthetic lab
  Owner: operations-owner
  Revision: protected commit

Behavior -> config.json
  Authority: committed retention configuration
  Owner: repository-maintainer
  Revision: protected commit

Proposals -> Issues and proposal branches
  Authority: requested changes only
```

**Do not put the current retention value in every map entry.** A map holding “seven days” becomes another value to synchronize after PROP-042. Keep stable identifiers and locations in the map, and read the value from the authoritative record.

**Protect map changes as routing changes.** Redirecting REQ-17 to a draft file alters the source selection even if the approved requirement remains untouched. Review the destination, owner, and authority scope whenever the map changes.

## Separate Baseline and Candidate

**The repository root contains the active lab records.** The downloaded **`baseline/`** directory is a teaching fixture. It is not automatically the protected baseline for every later PR. Once reviewed work reaches **`main`**, the protected root records define the next proposal's base.

| Location | Purpose | Edit during PROP-042? |
|---|---|---|
| **Root requirement/config/runbook** | Proposed active records on the branch | Yes, through reviewed changes |
| **`baseline/`** | Original offline exercise fixture | No |
| **Detached trusted worktree** | Captured protected root records | No |
| **`context.json`** | Evidence of captured base bytes | Regenerate after reconciliation |

**Keep control changes separate from retention changes.** Bootstrap the checker and review rules first. Then propose the seven-to-thirty-day change. Combining a policy rewrite, workflow rewrite, and value change makes it harder for a reviewer to distinguish repaired controls from bypassed controls.

## Review the Complete Change

**Open Files changed before accepting a PR description.** The description explains the author's intention. The diff reveals the submitted change. For PROP-042, inspect requirement revision, scope exclusions, configuration, runbook, proposal base, and manifest evidence.

1. **Product review:** confirm thirty-day intent and unchanged exclusions.
2. **Operations review:** confirm the runbook matches the proposed configuration and keeps the runtime limitation.
3. **Maintainer review:** inspect JSON, source capture, check results, and unrelated edits.
4. **Control review:** inspect any map, policy, CODEOWNERS, or workflow change separately.

**A green check does not explain an unrelated deletion.** If the branch removes the policy document while changing retention, request a separate proposal or a specific owner review. Restricting scope keeps the review object understandable.

## Diagnose a Denial Test

**Use one attempted action per evidence row.** “Contributor failed” is ambiguous. The user might lack ordinary repository write access, encounter a browser limitation, or hit the intended branch rule. Those observations establish different boundaries.

| Observation | Interpretation | Follow-up |
|---|---|---|
| **Cannot create any branch** | Contribution access is absent | Use an approved Issue/fork route |
| **Creates branch, cannot publish to main** | Tested publication route is restricted | Capture unchanged main revision |
| **Merge blocked with one review** | Review count applies to tested PR | Add role-specific evidence |
| **Admin publishes despite rule** | Tested identity bypasses the boundary | Inspect bypass settings and grants |

**Record role and action without exposing account details** in shared course evidence. Keep native actor records privately available for the reviewer. Capture the rule configuration, attempted operation, denial, and resulting protected revision together.

## Repository Completion Check

**Deliver a repository another contributor navigates independently.** README points to the map, the map resolves authoritative records, owner coverage includes sensitive paths, and protection applies to **`main`**. Retain one permitted proposal and one denied publication attempt.

**Do not claim enforcement from settings alone.** Settings establish intended configuration. The sandbox attempt establishes observed behavior for a particular role and route. Carry both into the agent and Actions lesson.

## Troubleshooting and Rollback

**Owner request missing:** confirm write access and base-branch path coverage. **Protection absent:** verify plan and visibility. **Merge remains enabled:** inspect rule target, bypass configuration, and review count.

**Rollback:** close unmerged proposals and deactivate lab automation. Revert merged lab content through another reviewed PR. Preserve evidence before deleting the disposable repository. Do not weaken protection to finish a failing test.

## Exercise and Self-Check

**Propose an edit to `docs/policy.md`** as contributor. Decide whether maintainer approval alone establishes policy-owner approval.

**Expected reasoning:** review count alone does not establish authority. The path needs policy-owner coverage and current role review. List unenforced role-specific requirements as procedural controls.

## Primary References

- **Plan and review controls:** [Protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches).
- **Owner eligibility:** [Code owners](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners).
- **Browser contribution:** [Editing files](https://docs.github.com/en/repositories/working-with-files/managing-files/editing-files).

## Next Steps

**Continue with [Agent Adapters and Actions](/articles/ai-collaboration-github-agents-actions/)** to connect source evidence to executable checks.