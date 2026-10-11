---
title: "AI Collaboration Course for GitHub, Confluence, and Jira"
date: 2026-10-01
lastmod: 2026-10-10
toc: true
draft: false
description: "Build two reviewed AI collaboration workflows with source authority, permissions, publication, recovery, and handoff exercises."
educationalLevel: "Beginner to Advanced"
genre: ["Artificial Intelligence", "Team Collaboration", "Software Engineering"]
tags: ["AI collaboration course", "GitHub", "Confluence Cloud", "Jira Cloud", "source authority", "human approval", "context manifest", "agent handoff", "synthetic lab", "RAG"]
cover: "/img/cover/A_group_of_diverse_professionals_collaborating_on_a_cyberse.webp"
coverAlt: "Illustration of professionals reviewing shared project work in a cybersecurity workspace"
coverCaption: ""
---

**Build two complete AI collaboration workflows** for developers, operations staff, and non-coding contributors. Carry one synthetic retention change through GitHub-first and GitHub with Confluence Cloud/Jira Cloud. Each track produces source records, review evidence, publication history, recovery records, and a fresh-session handoff.

## What You Will Build

**The fictional project is `export-service-lab`.** Approved retention starts at seven days. Your proposal changes it to thirty days. No production data or deletion job is involved. The exercise tests authority and coordination, not compliance requirements.

| Track | Authoritative homes | Final artifact |
|---|---|---|
| **GitHub-first** | Repository policy, requirements, implementation, runbook | Reviewed PR, consistency log, Issue, handoff |
| **Mixed workplace** | GitHub implementation, Confluence requirement/runbook, Jira delivery | Fixed proposal and cross-system ledger |

**This course implements the [AI collaboration framework](/articles/one-source-many-tools-ai-collaboration-framework/).** The framework explains ownership. These lessons supply exact procedures, copyable policies, worked examples, verification, negative tests, troubleshooting, rollback, and exercises. Course policy choices are not vendor defaults.

## Before You Begin

**Who:** contributor, product owner, operations owner, maintainer, and publisher. Assign people privately and use separate contributor/reviewer users for denial tests.

**What and where:** disposable GitHub repository, an approved coding/chat tool if desired, and dedicated Confluence/Jira Cloud sandboxes for Mixed. Python 3.10 or later runs the local lab without packages. Browser-only contributors ask the maintainer to run checks.

**When and why:** begin before attaching write-capable integrations. Reserve roughly 10 to 14 hours plus review across a one-week pilot. Finish GitHub-first before repeating the change in Mixed. The goal is reconstructable reviewed delivery, not agreement between two assistants.

**Plan boundaries:** GitHub protection depends on plan/visibility. Confluence Free lacks content restrictions. Jira Free lacks configurable permission schemes. Setup lessons explain the limits and provide official references. No particular paid chat connector, hosted coding agent, Rovo feature, or marketplace app is required.

**Readiness check:** open a GitHub repository, identify its default branch, explain what a PR changes, and read a small JSON record such as `{"retention_days": 7}`. For local checks, confirm Python and Git run in your terminal. For browser-only work, complete the foundation, repository, and browser lessons with a maintainer. You do not need to run the agent and Actions lesson to submit an Issue.

## Terms You Need First

| Term | Meaning in this course |
|---|---|
| **Authority** | The named record whose owner decides a specific fact, such as approved retention |
| **Protected branch** | A GitHub branch with rules governing direct changes and merges |
| **Pull request (PR)** | A proposed branch change for review before merging |
| **Manifest** | A file recording source revisions and hashes used for a check |
| **Revision-bound review** | Approval of a specific proposal version and the source versions behind it |
| **Read-back** | Opening published records again to confirm their final values |
| **Retrieval-augmented generation (RAG)** | Supplying selected source text to an AI response at request time |
| **Embedding and vector database** | A numeric text representation and a store used to find similar text. Both are optional here |

**Use the GitHub-first route when workplace access is unavailable.** Finishing modules 1 to 4 and the GitHub-first capstone produces a partial course result. The full two-track completion standard requires the Mixed workplace exercises.

| Route | Access to arrange before starting |
|---|---|
| **GitHub-first** | A disposable repository, a maintainer, separate contributor and reviewer accounts, and branch protection available for its plan and visibility |
| **Mixed workplace** | GitHub-first access plus Confluence and company-managed Jira Cloud sandboxes, setup administrator rights, separate contributor and owner accounts, and plans supporting the permission controls in modules 5 and 6 |

**Check the plan controls in the setup lessons before inviting learners.** If a control is unavailable, label its live test Blocked and complete the GitHub-first route. A simulated denial does not replace a platform denial.

## Course Modules

| # | Lesson | Reader artifact |
|---|---|---|
| **1** | [Pilot Foundation](/articles/ai-collaboration-pilot-foundation/) | Charter, authority register, policy, test matrix |
| **2** | [GitHub Repository Setup](/articles/ai-collaboration-github-repository/) | Source map, owners, protected boundary |
| **3** | [Agent Adapters and Actions](/articles/ai-collaboration-github-agents-actions/) | Adapters, manifest, trusted-base check |
| **4** | [Browser Contributions](/articles/ai-collaboration-github-browser-workflow/) | Issue, reviewed PR, non-coder handoff |
| **5** | [Confluence and Jira Setup](/articles/ai-collaboration-confluence-jira-setup/) | Authority pages and permission evidence |
| **6** | [Cross-System Publication](/articles/ai-collaboration-confluence-jira-publication/) | Fixed proposal and publication ledger |
| **7** | [Map-First Retrieval](/articles/ai-collaboration-map-first-retrieval/) | Lookup procedure and optional RAG evaluation |
| **8** | [Drift, Recovery, and Handoffs](/articles/ai-collaboration-drift-recovery-handoffs/) | Recovery decision and fresh verification |
| **9** | [Retention Capstone](/articles/ai-collaboration-retention-capstone/) | Two runs and independent acceptance |

## How to Use It

1. **Approve the foundation** before connecting tools.
2. **Complete modules 2 to 4** for coding-agent and browser/chat GitHub contribution.
3. **Complete modules 5 and 6** to preserve workplace authority across systems.
4. **Run modules 7 and 8** for discovery, drift, denial, recovery, and handoff.
5. **Deliver the capstone** in both tracks and obtain independent review.

**Keep each artifact for the next module.** Lessons explain who acts, what changes, when to proceed, where evidence lives, why the control matters, and how to verify it. Worked examples are illustrative. Expected outcomes become observations only after your sandbox produces evidence.

## Download the Lab

**The [synthetic lab archive](/downloads/ai-collaboration-lab.zip)** contains baseline records, a Python validator, a runbook, and ten unit tests. Extract into an empty directory and follow module 1. It makes no network calls and requires no credentials.

**The validator is not an approval service.** It detects source-byte drift and inconsistent requirement, configuration, proposal, and runbook records. Live permissions, identity, owner approval, and external publication require separate course tests.

## Completion Standard

| Case | Required demonstration |
|---|---|
| **Approved change** | Review and consistent publication read-back |
| **Stale context** | Changed base rejected |
| **Unauthorized write** | Contributor denied by platform controls |
| **Conflict** | Authority owner reconciles sources |
| **Partial publication** | Incomplete delivery remains visible |
| **Access denial** | Protected text absent from unauthorized task |
| **Recovery** | Reviewed completion or compensation |
| **Handoff** | Fresh session independently reads sources |

**Completion requires observed evidence.** Mark missing controls Blocked. Synthetic success supports another bounded pilot, not automatic production authorization.

**Example evidence row, illustrative only:** GitHub-first unauthorized-write test. Actor role: contributor. Initial `main` revision: record the sandbox commit. Attempt: direct push with a harmless synthetic edit. Expected: server rejection. Observed: enter the actual terminal response or mark Not run. Final revision: read `main` again and record its commit. Evidence: `github-first/03-unauthorized-write.md`. Reviewer: independent maintainer. Do not label this row Passed until the sandbox supplies the response and unchanged revision.

## Next Steps

**Start with [Pilot Foundation](/articles/ai-collaboration-pilot-foundation/)**. After the capstone, review provider handling, runtime tests, secrets, deployment, and production access before selecting another pilot. Return to [Courses and Playbooks](/courses-and-playbooks/) for related study.

{{< centerbutton href="/articles/ai-collaboration-pilot-foundation/" >}}
  Start the Pilot Foundation
{{< /centerbutton >}}
