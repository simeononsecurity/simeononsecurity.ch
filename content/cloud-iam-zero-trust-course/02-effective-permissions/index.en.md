---
title: "Cloud IAM Lesson 2: Effective Permissions"
date: 2026-10-10
lastmod: 2026-10-10
toc: true
draft: false
description: "Evaluate cloud access across identity policies, resource policies, boundaries, hierarchy controls, conditions, inheritance, and explicit denies."
genre: ["Cloud Security", "Identity and Access Management"]
tags: ["effective permissions", "AWS IAM evaluation", "Azure RBAC", "Google Cloud IAM", "explicit deny", "least privilege"]
cover: "/img/cover/cloud-effective-permissions.webp"
coverAlt: "Several cloud policy layers combining into one allow or deny decision."
coverCaption: "Read every applicable policy layer before deciding access."
---

[Return to the Cloud IAM and Zero Trust Lab Course](/cloud-iam-zero-trust-course-start/)

**Effective access is the final result across every applicable policy layer.** Reading one role or binding does not establish the decision.

## Use a Decision Record

```text
Principal:
Session:
Action:
Resource:
Identity grant:
Resource grant:
Boundary or session limit:
Hierarchy control:
Condition:
Explicit deny:
Final decision:
Evidence:
```

Fill every row. Use `not applicable` where a layer does not exist.

## Compare Evaluation Models

| Provider | Core model | Review focus |
|---|---|---|
| **AWS** | Identity and resource allows interact, while boundaries, session policies, SCPs, RCPs, and explicit denies limit results | Principal type, resource policy target, boundary, organization controls, conditions |
| **Azure** | Role assignments apply at scopes and inherit downward, while deny assignments take precedence | Principal, role definition, assignment scope, inheritance, deny assignment, condition |
| **Google Cloud** | Allow bindings inherit through the resource hierarchy, deny policies restrict matching permissions, and conditions narrow grants | Principal, role, resource ancestry, condition, deny policy |

AWS documents identity and resource policies as a union in common same-account cases. Permissions boundaries and organization controls act as intersections. **An applicable explicit deny overrides an allow.** Resource policy behavior changes with principal type, so read the provider logic before simplifying a decision.

## Work an Example

The payroll build identity has these layers:

- Project-level **Editor** role from an old group binding
- Resource-level **Reader** role on payroll reports
- Organization deny for policy administration actions
- Time condition ending Friday at 18:00 UTC

For `reports.read`, the broad project grant and narrow resource grant both support access during the condition window. For `setIamPolicy`, the organization deny blocks the action. The correct remediation removes the old Editor grant, then retests required reads.

## Review Sample Access

Download [the synthetic access review](/downloads/cloud-iam-zero-trust-course/access-review.csv).

1. Verify the principal owner.
2. Compare the role with the stated business need.
3. Check scope size.
4. Review last-used evidence and its collection limit.
5. Identify privilege-escalation paths.
6. Choose keep, reduce, remove, or investigate.
7. Record a test and rollback plan.

The `build-bot@example.test` row needs a narrower read role. The `legacy-export@example.test` row needs owner research and a controlled removal plan. Last-used age alone does not prove safe removal.

> **Expected Result:** each decision states the principal, action, resource, applicable layers, final result, and evidence gap.

## Troubleshooting

| Problem | Fix |
|---|---|
| **Console access differs from one policy** | Inspect group membership, inherited scope, resource policies, session limits, and deny layers |
| **A broad role looks unused** | Check audit retention and indirect workload use before removal |
| **A deny surprises an administrator** | Locate hierarchy controls and the exact denied permission |
| **A condition fails** | Check attribute names, time zone, resource tags, and session claims |

## Verify Your Work

- [ ] One decision record is complete
- [ ] Scope inheritance is included
- [ ] Explicit deny and implicit deny are distinct
- [ ] Principal type is recorded
- [ ] Remediation includes a test and rollback plan
- [ ] Last-used data has a retention caveat

**Primary references, checked 2026-10-10:** [AWS IAM policy evaluation logic](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html), [Azure role assignments](https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments), and [Google Cloud IAM policy overview](https://docs.cloud.google.com/iam/docs/allow-policies).

## Next Steps

Continue to [Lesson 3: Human Access](/cloud-iam-zero-trust-course/03-human-access/). Build short-lived, monitored administrative access.
