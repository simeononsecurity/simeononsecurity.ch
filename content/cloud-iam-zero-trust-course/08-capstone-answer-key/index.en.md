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
10. **Lab closure record:** for a live provider track, record context, objects created, delete results, and absence checks. For the offline track, write the exact preflight, ownership, teardown, and absence-check plan. Mark live commands `not run`.

## Constraints

- Do not create a long-lived workload key.
- Do not remove the emergency identity without a tested replacement.
- Do not treat last-used age as sole removal evidence.
- Do not grant policy administration to the report build.
- Do not finish a live lab with temporary objects present.

> **Expected Result:** required payroll reporting still works, policy administration stays denied, and every old grant has an owner-approved disposition.

## Reference Answer

### Access Review

| Principal | Decision | Reason |
|---|---|---|
| **alice@example.test** | Keep, then validate scope | Recent use and a named finance task support access. Confirm read-only scope |
| **build-bot@example.test** | Reduce | Editor exceeds the stated read-only report task. Replace with a custom read role and federated session |
| **legacy-export@example.test** | Investigate, then remove under change control | Owner and business need are unknown, role is organization owner, and last use is old |
| **breakglass-01@example.test** | Keep with stronger governance | Emergency recovery needs separate credentials, monitoring, tests, and restricted use |

### Identity and Effective-Access Record

The CSV provides principal type, owner, role, scope, and stated need. It does not provide credential type, active session, inherited policy, deny policy, or resource policy. Record those fields as unknown until a provider export or owner confirms them. This is a completed evidence-gap record, not proof of live authorization.

| Principal | Type and owner | Current role and scope | Credential and session | Revocation route |
|---|---|---|---|---|
| Alice | Human, finance | Viewer, `project-payroll` | Unknown in CSV, inspect federation and session | Remove narrow grant and revoke session after owner approval |
| Build bot | Workload, platform | Editor, `project-payroll` | Unknown in CSV, replace stored key if found | Remove broad grant and revoke workload federation trust |
| Legacy export | Workload, owner unknown | Owner, organization | Unknown in CSV, investigate before change | Identify owner and dependencies, then remove grant and credential |
| Break-glass 01 | Human, security | Global admin, tenant | Unknown in CSV, verify separate emergency credential | Governed disablement only after alternate recovery path passes |

| Principal and requested action | Known nominal grant | Other policy layers and conditions | Current evidence conclusion | Target test |
|---|---|---|---|---|
| Alice, read payroll report | Project Viewer | Inherited grants, resource policy, device condition unknown | Read is plausible, not yet verified | Allow payroll read with strong MFA, deny unrelated write |
| Build bot, read report input | Project Editor | Trust claims, deny policy, resource conditions unknown | Broad grant exceeds need | Allow named reads under exact federation claims, deny policy write |
| Legacy export, change organization IAM policy | Organization Owner | Deny and boundary layers unknown | High-risk nominal authority, owner missing | Deny after approved removal, confirm no dependency breaks |
| Break-glass 01, emergency administration | Tenant Global Admin | Activation, monitoring, and session controls unknown | Emergency path needs control evidence | Allow only tested emergency activation, alert and expire session |

For full credit, attach the provider's effective-policy evaluation or live authorization record before labeling any current action `allowed` or `denied`. The table above separates a nominal role from an observed decision.

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

### Zero Trust Test Matrix

These are target-state tests. They are expected outcomes until executed in an approved sandbox. Record the request context, policy decision, audit event, and cleanup result for each live run.

| Case | Subject, action, and context | Expected | Evidence to collect |
|---|---|---|---|
| Required allow | Build bot reads named report input with exact issuer, audience, repository, environment, and valid short session | Allow | Federation exchange and object-read audit event |
| Privilege deny | Build bot requests policy administration with the same valid session | Deny | Authorization denial with action and resource |
| Context failure | Build bot requests report input from an unapproved repository or expired session | Deny | Failed exchange or resource decision, no object read |
| Revocation | Repeat a previously allowed read after trust or grant removal | Deny | Revocation record and denied repeat request |


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

For a live track, full credit requires provider context before creation, exact object identifiers, read-only grant evidence, teardown output, and an absence check. A delete command without an absence check earns partial credit. For the offline track, full credit requires a provider-specific preflight and teardown plan with each command's expected result, collision stop condition, and owner. Mark every live result `not run`.

This offline AWS example shows the required level of detail. The identity operations owner confirms the sandbox account and approved operator role. The expected preflight `aws iam get-role --role-name sos-iam-lab-reader` result is `NoSuchEntity`. Any existing role or uncertain error stops the run. After a successful create, the learner records the returned role ARN and inline policy name. Teardown removes that policy and that recorded role only. The final `get-role` must return `NoSuchEntity`. In this offline example, every command's observed result is `not run`, so no object is claimed absent. The [provider lab](/cloud-iam-zero-trust-course/06-disposable-cloud-lab/) supplies the exact commands for a live sandbox.

## Scoring Rubric

| Area | Points | Full-credit evidence |
|---|---:|---|
| **Identity and access model** | 20 | Principals, sessions, trust, roles, scope, revocation |
| **Review decisions** | 20 | Evidence, owner, business need, escalation path |
| **Target design** | 20 | Federated human and workload access with narrow roles |
| **Zero trust tests** | 15 | Allow, deny, context failure, revocation, audit proof |
| **Migration and rollback** | 15 | Safe sequence, owner acceptance, expiry, monitoring |
| **Lab closure** | 10 | Live track: all created objects removed and absence verified. Offline track: complete, collision-safe teardown plan with live state marked not run |

**Passing score:** 80 points. A live lab also requires no leftover lab identity or credential.

## Troubleshooting

- **Your design keeps Editor:** list exact required actions and replace the broad role.
- **Your workload uses a stored key:** redesign around managed identity or federation.
- **Your emergency path disappears:** restore a governed recovery identity before enforcement.
- **Your lab leaves a grant:** remove the binding or assignment before deleting the identity.

## Verify Completion

- [ ] All ten deliverables exist
- [ ] Human and workload paths are separate
- [ ] The allow and deny test matrix includes expected decisions and evidence. Live results are labeled `not run` on the offline track
- [ ] Rollback expires
- [ ] Live track: created provider objects are absent. Offline track: teardown and absence checks are specified
- [ ] Answer key comparison records corrections

Return to the [course hub](/cloud-iam-zero-trust-course-start/) and retain the package as a synthetic portfolio sample.
