---
title: "Cloud IAM and Zero Trust Capstone"
date: 2026-10-10
lastmod: 2026-10-14
toc: true
draft: false
description: "Review synthetic cloud access, design a least-privilege target state, test the offline simulator or a provider sandbox, and submit closure evidence."
genre: ["Cloud Security", "Identity and Access Management", "Zero Trust", "Security Lab"]
tags: ["cloud IAM capstone", "zero trust capstone", "access review", "least privilege plan", "cloud security portfolio"]
cover: "/img/cover/cloud-iam-zero-trust-capstone.webp"
coverAlt: "A cloud access review transformed into least-privilege roles, tests, monitoring, and verified teardown."
coverCaption: "Turn an access inventory into a tested target state."
---

[Return to the Cloud IAM and Zero Trust Lab Course](/cloud-iam-zero-trust-course-start/)

**The capstone turns an access review into a tested migration plan.** Finish and score the submission before opening the reference answer.

## Scenario

The payroll reporting environment contains four principals in [the synthetic access review](/downloads/cloud-iam-zero-trust-course/access-review.csv). Leadership wants narrower access, short-lived sessions, visible policy decisions, and a rollback path.

## Required Deliverables

1. **Identity map:** principal, type, owner, credential, session, role, scope, and revocation
2. **Effective-access record:** one requested action per principal across applicable policy layers
3. **Review decision:** keep, reduce, remove, or investigate with evidence
4. **Human access target:** daily, privileged, and emergency paths
5. **Workload access target:** federation or managed identity, exact trust, short session, narrow role
6. **Zero trust decision record:** subject, runtime, resource, action, context, enforcement, telemetry
7. **Test matrix:** expected allow, expected deny, context failure, and revocation
8. **Migration order:** evidence, owner confirmation, new grant, tests, old grant removal, monitoring
9. **Rollback plan:** trigger, owner, temporary access, expiry, and follow-up
10. **Lab closure record:** choose one route below.

### Live Provider Route

Record provider context, objects created, object identifiers, test type, delete results, and absence checks. Keep any unobserved authorization result labeled `not run`.

### Offline Simulator Route

Download [the Python simulator](/downloads/cloud-iam-zero-trust-course/policy_teardown_simulator.py) and [the synthetic fixture](/downloads/cloud-iam-zero-trust-course/policy-fixtures.json). Follow the [Lesson 6 offline steps](/cloud-iam-zero-trust-course/06-disposable-cloud-lab/). Attach:

- The full terminal output with `RESULT PASS checks=4/4`
- **`simulator-evidence.json`** with allow, deny, revocation, and cleanup records
- The exit code from the simulator
- The successful cleanup result. In Bash or WSL, use `test ! -e sim-state`. In PowerShell, use `if (Test-Path sim-state) { throw "sim-state still exists" }`.
- A boundary statement which labels AWS, Azure, Google Cloud, and live tenant closure `not run`

**A paper preflight and teardown plan earns partial lab-closure credit.** Full offline lab-closure credit requires executed simulator evidence.

## Constraints

- Do not create a long-lived workload key.
- Do not remove the emergency identity without a tested replacement.
- Do not treat last-used age as sole removal evidence.
- Do not grant policy administration to the report build.
- Do not finish a live lab with temporary objects present.
- Do not label local simulator evidence as live cloud evidence.

> **Expected Result:** your target design preserves required payroll reporting and denies policy administration. The offline route records synthetic allow, deny, revocation, and local cleanup results. A provider route records its grant and teardown checks, plus AWS policy simulation if selected. Label live authorization or revocation checks `not run` unless you observed them in an approved sandbox. Every old grant has an owner-approved disposition.

## Scoring Rubric

| Area | Points | Full-credit evidence |
|---|---:|---|
| **Identity and access model** | 20 | Principals, sessions, trust, roles, scope, revocation |
| **Review decisions** | 20 | Evidence, owner, business need, escalation path |
| **Target design** | 20 | Federated human and workload access with narrow roles |
| **Zero trust tests** | 15 | Allow, deny, context failure, revocation, and evidence labels |
| **Migration and rollback** | 15 | Safe sequence, owner acceptance, expiry, monitoring |
| **Lab closure** | 10 | Live route: all created objects removed and absence verified. Offline route: observed simulator allow, deny, revocation, and local cleanup evidence |

**Passing score:** 80 points. A live lab also requires no leftover lab identity or credential. A plan-only offline closure earns at most **5 of 10** lab-closure points.

## Troubleshooting

- **Your design keeps Editor:** list exact required actions and replace the broad role.
- **Your workload uses a stored key:** redesign around managed identity or federation.
- **Your emergency path disappears:** restore a governed recovery identity before enforcement.
- **Your live lab leaves a grant:** remove the binding or assignment before deleting the identity.
- **Your offline evidence lacks one check:** rerun the maintained fixture in a fresh folder and attach the complete evidence file.

## Verify Completion

- [ ] All ten deliverables exist
- [ ] Human and workload paths are separate
- [ ] The allow and deny test matrix includes expected decisions and evidence labels
- [ ] Rollback expires
- [ ] Live route: created provider objects are absent
- [ ] Offline route: all four simulator checks passed and live closure stays `not run`
- [ ] The submission score reaches 80 out of 100

## Review Your Submission

Freeze the submitted package and score it with the rubric. Then open the [Cloud IAM and Zero Trust Capstone Answer Key](/cloud-iam-zero-trust-course/10-capstone-answer-key/). Record corrections in a separate review log.
