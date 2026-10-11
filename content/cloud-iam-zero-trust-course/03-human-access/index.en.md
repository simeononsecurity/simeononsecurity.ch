---
title: "Cloud IAM Lesson 3: Human Access"
date: 2026-10-10
lastmod: 2026-10-10
toc: true
draft: false
description: "Design federated human access with strong authentication, short sessions, privileged activation, emergency recovery, and continuous review."
genre: ["Cloud Security", "Identity and Access Management", "Zero Trust"]
tags: ["cloud federation", "multifactor authentication", "privileged access", "conditional access", "break glass account", "access review"]
cover: "/img/cover/cloud-human-access.webp"
coverAlt: "A cloud administrator passing federation, strong authentication, device, and privilege checks."
coverCaption: "Give people temporary access tied to a verified identity."
---

[Return to the Cloud IAM and Zero Trust Lab Course](/cloud-iam-zero-trust-course-start/)

**Human cloud access should begin at a central identity provider and end in a short-lived session.** Separate daily work, privileged work, and emergency recovery.

## Design the Path

```text
Person
  -> central identity provider
  -> phishing-resistant authentication
  -> device and risk checks
  -> group or eligible role
  -> short-lived cloud session
  -> resource action
  -> audit event
```

Each step needs an owner and failure route. A central sign-in without session limits or audit review still leaves excessive access risk.

## Separate Access Types

| Access type | Use | Control |
|---|---|---|
| **Daily** | Routine read and deployment work | Federated session with narrow role |
| **Privileged** | Policy, identity, billing, or security change | Eligible role, approval where needed, short activation, strong MFA |
| **Emergency** | Recover from identity or policy failure | Separate monitored account and tested procedure |

Do not use the emergency identity for daily work. Test its recovery path on a schedule and alert on every use.

## Apply Context

Microsoft Entra Conditional Access illustrates a context-aware policy engine. Signals include user, application, device, location, and risk. Decisions include block, MFA, authentication strength, compliant device, approved application, and session controls.

Provider features differ, but the design questions stay stable:

- **Who** requests access?
- **Which resource** receives the request?
- **Which device or client** carries the session?
- **Which risk signals** exist?
- **How long** should privilege last?
- **Which event** proves grant, activation, use, and removal?

## Build a Privileged Role Card

```text
Role: Payroll security administrator
Eligible group: payroll-security-admins
Activation reason: approved incident or quarterly policy change
Approval: security lead
Authentication: phishing-resistant MFA
Session: 60 minutes
Resource scope: payroll project only
Excluded action: organization policy administration
Audit: activation, assignment, policy change, and sign-out events
Review: monthly membership and quarterly role design
Emergency route: monitored recovery identity
```

## Practice Steps

1. Choose one sensitive cloud role.
2. Remove daily standing assignment from the design.
3. Define eligibility, activation, approval, MFA, and duration.
4. Set the narrowest resource scope.
5. Name excluded actions.
6. Define emergency access separately.
7. Write one audit query or console check for role activation.
8. Define a quarterly access review.

> **Expected Result:** daily, privileged, and emergency paths have different controls and evidence.

## Troubleshooting

| Problem | Fix |
|---|---|
| **Administrators fear lockout** | Test emergency access before enforcing new policy and keep two controlled recovery identities |
| **Users keep standing roles** | Move them to eligible activation and measure actual privileged use |
| **MFA prompts are bypassed** | Check legacy protocols, remembered sessions, authentication strength, and excluded applications |
| **Role review lacks context** | Add owner, business task, last activation, scope, and ticket evidence |

## Verify Your Work

- [ ] Human access uses federation
- [ ] Privileged access has time limits
- [ ] Strong authentication is required
- [ ] Emergency access is separate and monitored
- [ ] Resource scope is narrow
- [ ] Grant, activation, use, and removal create audit evidence

**Primary references, checked 2026-10-10:** [Microsoft Entra Conditional Access overview](https://learn.microsoft.com/en-us/entra/identity/conditional-access/overview) and [Microsoft Entra PIM deployment plan](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-deployment-plan).

## Next Steps

Continue to [Lesson 4: Workload Identity](/cloud-iam-zero-trust-course/04-workload-identity/). Replace stored secrets with scoped, short-lived identity.
