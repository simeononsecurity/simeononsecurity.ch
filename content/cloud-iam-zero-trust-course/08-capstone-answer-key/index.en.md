---
title: "Cloud IAM and Zero Trust Capstone"
date: 2026-10-10
lastmod: 2026-10-10
toc: true
draft: false
description: "Review synthetic cloud access, design a least-privilege target state, plan zero trust tests, and compare the result with a full answer key and rubric."
genre: ["Cloud Security", "Identity and Access Management", "Zero Trust", "Security Lab"]
tags: ["cloud IAM capstone", "zero trust capstone", "access review", "least privilege plan", "cloud security portfolio", "answer key"]
cover: "/img/cover/cloud-iam-zero-trust-capstone.webp"
coverAlt: "A cloud access review transformed into least-privilege roles, tests, monitoring, and verified teardown."
coverCaption: "Turn an access inventory into a tested target state."
---

[Return to the Cloud IAM and Zero Trust Lab Course](/cloud-iam-zero-trust-course-start/)

**The capstone turns an access review into a tested migration plan.** Finish the submission before reading the reference answer.

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
10. **Lab teardown evidence:** selected provider context, objects, delete results, and absence checks

## Constraints

- Do not create a long-lived workload key.
- Do not remove the emergency identity without a tested replacement.
- Do not treat last-used age as sole removal evidence.
- Do not grant policy administration to the report build.
- Do not finish the lab with temporary objects present.

> **Expected Result:** required payroll reporting still works, policy administration stays denied, and every old grant has an owner-approved disposition.

## Reference Answer

### Access Review

| Principal | Decision | Reason |
|---|---|---|
| **alice@example.test** | Keep, then validate scope | Recent use and a named finance task support access. Confirm read-only scope |
| **build-bot@example.test** | Reduce | Editor exceeds the stated read-only report task. Replace with a custom read role and federated session |
| **legacy-export@example.test** | Investigate, then remove under change control | Owner and business need are unknown, role is organization owner, and last use is old |
| **breakglass-01@example.test** | Keep with stronger governance | Emergency recovery needs separate credentials, monitoring, tests, and restricted use |

### Human Target State

Alice uses central federation, strong MFA, a short session, and a payroll-scoped reader role. Privileged changes use an eligible role with time-bound activation. The emergency identity stays separate, monitored, and tested.

### Workload Target State

The build workflow exchanges exact OIDC claims for a short-lived workload session. Trust binds the approved repository and production environment. A custom role reads required inputs and writes one report prefix. Policy administration, identity administration, and unrelated data access stay absent.

### Zero Trust Decision

```text
Subject: payroll build workload
Runtime: protected production workflow
Resource: payroll report storage
Action: read input and write report output
Context: exact issuer, audience, repository, environment, and short session
Decision: allow named object actions, deny or omit policy administration
Enforcement: token exchange and storage authorization
Telemetry: exchange, object access, denied action, policy change, revocation
```

### Migration Order

1. Export current policies, bindings, owners, and audit evidence.
2. Confirm owners and required actions.
3. Create the new narrow roles and trust relationships.
4. Test expected allow and deny behavior.
5. Move one principal at a time.
6. Remove the old broad grant.
7. Monitor denied requests and business outcomes.
8. Close only after owner acceptance and rollback expiry.

### Rollback

Rollback uses a time-limited payroll-scoped role approved by the security lead. Trigger rollback only when a required report fails due to the new authorization design. Record the denied action, restore the minimum missing permission, set an expiry, and open a follow-up review.

### Lab Completion

Full credit requires provider context before creation, exact object identifiers, read-only grant evidence, teardown output, and an absence check. A delete command without an absence check earns partial credit.

## Scoring Rubric

| Area | Points | Full-credit evidence |
|---|---:|---|
| **Identity and access model** | 20 | Principals, sessions, trust, roles, scope, revocation |
| **Review decisions** | 20 | Evidence, owner, business need, escalation path |
| **Target design** | 20 | Federated human and workload access with narrow roles |
| **Zero trust tests** | 15 | Allow, deny, context failure, revocation, audit proof |
| **Migration and rollback** | 15 | Safe sequence, owner acceptance, expiry, monitoring |
| **Teardown** | 10 | All objects removed and absence verified |

**Passing score:** 80 points with no leftover lab identity or credential.

## Troubleshooting

- **Your design keeps Editor:** list exact required actions and replace the broad role.
- **Your workload uses a stored key:** redesign around managed identity or federation.
- **Your emergency path disappears:** restore a governed recovery identity before enforcement.
- **Your lab leaves a grant:** remove the binding or assignment before deleting the identity.

## Verify Completion

- [ ] All ten deliverables exist
- [ ] Human and workload paths are separate
- [ ] Required allow and deny tests pass
- [ ] Rollback expires
- [ ] Provider lab objects are absent
- [ ] Answer key comparison records corrections

Return to the [course hub](/cloud-iam-zero-trust-course-start/) and retain the package as a synthetic portfolio sample.
