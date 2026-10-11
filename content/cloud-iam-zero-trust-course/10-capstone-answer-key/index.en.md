---
title: "Cloud IAM and Zero Trust Capstone Answer Key"
date: 2026-10-10
lastmod: 2026-10-11
toc: true
draft: false
description: "Review the Cloud IAM and Zero Trust capstone reference design, evidence boundaries, simulator results, migration order, and scoring requirements."
genre: ["Cloud Security", "Identity and Access Management", "Zero Trust", "Security Lab"]
tags: ["cloud IAM capstone answer key", "zero trust capstone reference", "access review", "least privilege plan", "cloud security portfolio"]
cover: "/img/cover/cloud-iam-capstone-answer-key.webp"
coverAlt: "A reviewer checks cloud identities, allow and deny decisions, and access through a protected gate."
coverCaption: "Compare the submitted package with the reference evidence."
---

[Return to the Cloud IAM and Zero Trust Capstone](/cloud-iam-zero-trust-course/08-capstone/)

**Open this reference after freezing your submission and assigning an initial score.** Preserve your first design. Record corrections in a separate review log.

## Access Review

| Principal | Decision | Reason |
|---|---|---|
| **alice@example.test** | Keep, then validate scope | Recent use and a named finance task support access. Confirm read-only scope |
| **build-bot@example.test** | Reduce | Editor exceeds the stated read-only report task. Replace with a custom read role and federated session |
| **legacy-export@example.test** | Investigate, then remove under change control | Owner and business need are unknown, role is organization owner, and last use is old |
| **breakglass-01@example.test** | Keep with stronger governance | Emergency recovery needs separate credentials, monitoring, tests, and restricted use |

## Identity and Effective-Access Record

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

For full live-provider evidence, attach the provider's effective-policy evaluation or live authorization record before labeling any current action `allowed` or `denied`. The table above separates a nominal role from an observed provider decision.

## Human Target State

Alice uses central federation, strong MFA, a short session, and a payroll-scoped reader role. Privileged changes use an eligible role with time-bound activation. The emergency identity stays separate, monitored, and tested.

## Workload Target State

The build workflow exchanges exact OIDC claims for a short-lived workload session. Trust binds the approved repository and production environment. A custom role reads required inputs and writes one report prefix. Policy administration, identity administration, and unrelated data access stay absent.

## Zero Trust Decision

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

## Zero Trust Test Matrix

These are target-state tests. They stay expected outcomes until executed in an approved sandbox. Record the request context, policy decision, audit event, and cleanup result for each live run.

| Case | Subject, action, and context | Expected | Evidence to collect |
|---|---|---|---|
| Required allow | Build bot reads named report input with exact issuer, audience, repository, environment, and valid short session | Allow | Federation exchange and object-read audit event |
| Privilege deny | Build bot requests policy administration with the same valid session | Deny | Authorization denial with action and resource |
| Context failure | Build bot requests report input from an unapproved repository or expired session | Deny | Failed exchange or resource decision, no object read |
| Revocation | Repeat a previously allowed read after trust or grant removal | Deny | Revocation record and denied repeat request |

The offline simulator covers synthetic allow, privilege deny, revocation, and local cleanup. It does not test federation claims, provider policy layers, provider audit events, or live object deletion.

## Migration Order

1. Export current policies, bindings, owners, and audit evidence.
2. Confirm owners and required actions.
3. Create the new narrow roles and trust relationships.
4. Test expected allow and deny behavior.
5. Move one principal at a time.
6. Remove the old broad grant.
7. Monitor denied requests and business outcomes.
8. Close only after owner acceptance and rollback expiry.

## Rollback

Rollback uses a time-limited payroll-scoped role approved by the security lead. Trigger rollback only when a required report fails due to the new authorization design. Record the denied action, restore the minimum missing permission, set an expiry, and open a follow-up review.

## Lab Completion

### Live Provider Reference

Full credit requires provider context before creation, exact object identifiers, read-only grant evidence, teardown output, and an absence check. A delete command without an absence check earns partial credit.

The AWS plan shows the required detail. The identity operations owner confirms the sandbox account and approved operator role. The expected preflight `aws iam get-role --role-name sos-iam-lab-reader` result is `NoSuchEntity`. Any existing role or uncertain error stops the run. After a successful create, the learner records the returned role ARN and inline policy name. Teardown removes the policy and recorded role only. The final `get-role` must return `NoSuchEntity`.

Without a provider run, every command's observed result and live cloud closure stay `not run`. A detailed plan does not prove provider cleanup.

### Offline Simulator Reference

Use [the maintained simulator](/downloads/cloud-iam-zero-trust-course/policy_teardown_simulator.py) with [the maintained fixture](/downloads/cloud-iam-zero-trust-course/policy-fixtures.json). A passing reference run records:

| Check | Expected | Observed |
|---|---|---|
| **Read before revocation** | Allow | Allow |
| **Policy administration** | Deny | Deny |
| **Read after revocation** | Deny | Deny |
| **Local state cleanup** | Removed | Removed |

Full offline lab-closure credit requires the learner's own terminal output, exit code `0`, evidence JSON, and absent work folder. A paper preflight and teardown plan earns at most **5 of 10** lab-closure points. The simulator proves local fixture behavior only. AWS, Azure, Google Cloud, and live tenant closure stay `not run`.

The [provider and offline lab](/cloud-iam-zero-trust-course/06-disposable-cloud-lab/) supplies exact commands and troubleshooting steps.

## Review Gate

Use the rubric on the [capstone prompt](/cloud-iam-zero-trust-course/08-capstone/). Pass with **80 out of 100 or higher**. A live lab also requires no leftover lab identity or credential.

## Verify Your Review

- [ ] Each correction points to evidence or a stated limit
- [ ] Local and live-provider evidence stay separate
- [ ] Plan-only lab closure receives partial credit
- [ ] The final score reaches 80 out of 100

Return to the [course hub](/cloud-iam-zero-trust-course-start/) and retain the package as a synthetic portfolio sample.
