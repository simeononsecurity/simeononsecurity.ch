---
title: "Cloud IAM and Zero Trust Lab Course"
date: 2026-10-10
lastmod: 2026-10-10
toc: true
draft: false
description: "Design, test, review, and remove cloud identity access across AWS, Azure, and Google Cloud with zero trust principles and disposable labs."
genre: ["Cloud Security", "Identity and Access Management", "Zero Trust", "Security Lab"]
tags: ["cloud IAM course", "zero trust course", "AWS IAM lab", "Azure RBAC lab", "Google Cloud IAM lab", "least privilege", "workload identity", "access review"]
cover: "/img/cover/cloud-iam-zero-trust-lab-course.webp"
coverAlt: "Cloud identities passing through policy checks before reaching protected resources."
coverCaption: "Grant narrow access, test the result, and remove the lab."
---

**This course treats identity policy as executable security design.** You will model principals, calculate effective access, design human and workload controls, test a disposable provider lab, and prove teardown.

The course compares AWS, Azure, and Google Cloud without hiding their different policy models. Provider terms stay explicit.

## Audience

This course serves cloud administrators, security engineers, DevOps practitioners, and auditors who need practical identity access skills.

**You should understand accounts, command-line tools, and JSON.** Prior provider certification is optional.

## Outcomes

By the end, you will produce:

- An **identity map** for human and workload principals
- An **effective-permissions worksheet** across policy layers
- A **human access design** with federation, MFA, session, and emergency controls
- A **workload identity design** without long-lived access keys
- A **zero trust access policy** using identity, device, resource, context, and telemetry
- A **disposable lab record** with preflight checks, grant inspection, AWS policy simulation where selected, teardown, and absence checks
- An **access review decision log** and remediation plan

## Course Order

| # | Lesson | Skill and output |
|---|---|---|
| **1** | [Identity Model](/cloud-iam-zero-trust-course/01-identity-model/) | Map principals, credentials, sessions, roles, and resources |
| **2** | [Effective Permissions](/cloud-iam-zero-trust-course/02-effective-permissions/) | Evaluate allows, boundaries, conditions, inheritance, and denies |
| **3** | [Human Access](/cloud-iam-zero-trust-course/03-human-access/) | Design federation, MFA, privileged access, and recovery |
| **4** | [Workload Identity](/cloud-iam-zero-trust-course/04-workload-identity/) | Replace stored keys with short-lived identity |
| **5** | [Zero Trust Policy](/cloud-iam-zero-trust-course/05-zero-trust-policy/) | Build resource-focused, context-aware access decisions |
| **6** | [Disposable Cloud Lab](/cloud-iam-zero-trust-course/06-disposable-cloud-lab/) | Create, test, and remove narrow access in one provider |
| **7** | [Quiz and Answer Key](/cloud-iam-zero-trust-course/07-quiz-answer-key/) | Check policy and teardown knowledge |
| **8** | [Capstone and Answer Key](/cloud-iam-zero-trust-course/08-capstone-answer-key/) | Review access and deliver a zero trust migration plan |

## Prerequisites

- **One disposable provider sandbox** for the optional live lab
- **AWS CLI, Azure CLI, or Google Cloud CLI** for the selected track
- **Permission to create and remove lab identities and role assignments**
- **A second administrator or recovery route** before changing privileged access
- **A clean folder** for downloaded policy files and evidence

The concept lessons and capstone work offline. The live lab changes cloud identity state. Use a dedicated sandbox without production resources.

## Safety Rules

1. Confirm the active account, tenant, subscription, or project before every change.
2. Check that every exact `sos-iam-lab` object name is absent before creation. Stop on a collision or an uncertain result.
3. Grant read-only access at the narrowest lab scope.
4. Do not create access keys or client secrets.
5. Save identifiers returned by successful create commands. Delete only objects recorded as created by this run.
6. Run teardown in the same session for those recorded objects.
7. Verify absence after deletion.

> **Expected Result:** the lab ends with no temporary identity, role assignment, policy, group, or project binding left behind.

## Zero Trust Baseline

NIST SP 800-207 removes implicit trust based on network location or asset ownership. NIST SP 800-207A applies identity-tier and network-tier policy to cloud-native and multi-cloud applications. In this course, access decisions use the principal, credential, device or workload, resource, action, context, and current telemetry.

**Primary references, checked 2026-10-10:** [NIST SP 800-207](https://csrc.nist.gov/pubs/sp/800/207/final), [NIST SP 800-207A](https://csrc.nist.gov/pubs/sp/800/207/A/final), [AWS IAM policy evaluation logic](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html), [Microsoft Entra Conditional Access](https://learn.microsoft.com/en-us/entra/identity/conditional-access/overview), and [Google Cloud service account security](https://docs.cloud.google.com/iam/docs/best-practices-service-accounts).

## Troubleshooting

- **No cloud sandbox exists:** complete Lessons 1 through 5 and the offline capstone with synthetic data.
- **CLI access is denied:** record the denied action and use an approved sandbox operator.
- **Provider terms conflict:** return to the identity comparison and preserve provider-specific names.

## Verify Readiness

- [ ] The active provider context is recorded
- [ ] The environment holds no production resources
- [ ] Create and delete permissions are approved
- [ ] A recovery administrator exists outside the lab identity

> **Expected Result:** the selected lab environment has a known owner, bounded scope, and verified teardown route.

## Start Here

Begin with [Lesson 1: Identity Model](/cloud-iam-zero-trust-course/01-identity-model/). Draw the access path before writing policy.
