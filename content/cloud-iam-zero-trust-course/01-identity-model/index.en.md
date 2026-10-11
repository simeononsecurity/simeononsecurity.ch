---
title: "Cloud IAM Lesson 1: Identity Model"
date: 2026-10-10
lastmod: 2026-10-10
toc: true
draft: false
description: "Model human and workload principals, credentials, sessions, policies, roles, resources, and trust relationships across major cloud providers."
genre: ["Cloud Security", "Identity and Access Management"]
tags: ["cloud identity", "cloud principals", "IAM roles", "service accounts", "managed identities", "trust policy"]
cover: "/img/cover/cloud-iam-identity-model.webp"
coverAlt: "Human and workload principals receiving short-lived sessions before accessing cloud resources."
coverCaption: "Map who requests access, through which session, to which resource."
---

[Return to the Cloud IAM and Zero Trust Lab Course](/cloud-iam-zero-trust-course-start/)

**Cloud access starts with a principal and ends with a resource action.** Credentials create a session. Policies and trust relationships decide which actions the session receives.

## Name the Parts

| Part | Question | Example |
|---|---|---|
| **Principal** | Who or what asks? | Person, group, role session, service account, managed identity |
| **Credential** | How is identity proven? | Federation token, certificate, workload token |
| **Session** | Which temporary context acts? | AWS role session, Azure sign-in session, Google access token |
| **Role or policy** | Which actions are described? | S3 list, resource-group reader, logging viewer |
| **Resource** | What receives the action? | Bucket, vault, project, secret, application |
| **Trust relationship** | Who is allowed to obtain the role or identity? | Federation provider, workload pool, role trust policy |

Do not merge authentication and authorization. **A valid identity still needs an allowed action on the target resource.**

## Compare Provider Terms

| Concept | AWS | Azure | Google Cloud |
|---|---|---|---|
| **Human federation** | IAM Identity Center or external identity provider | Microsoft Entra ID | Workforce identity federation or Cloud Identity |
| **Workload principal** | IAM role | Managed identity or service principal | Service account or federated principal |
| **Permission package** | Policy | Role definition | Role |
| **Grant** | Attached policy or resource policy | Role assignment | Allow policy binding |
| **Hierarchy and authorization limit** | SCP or RCP in Organizations | Management-group RBAC scope and applicable deny assignments | Organization and folder policy, deny policy, and inherited bindings |

Azure Policy governs resource configuration and compliance. Review its effects separately from RBAC authorization. Provider names differ. The review question stays stable: **Which principal receives which action on which resource under which conditions?**

## Draw an Access Path

Use the synthetic payroll reporting service.

```text
Build workflow
  -> workload federation
  -> short-lived reporting identity
  -> custom read-only role
  -> payroll report storage
  -> audit event and alert path
```

Add these fields:

```text
Principal owner:
Authentication source:
Session lifetime:
Role or policy:
Resource scope:
Conditions:
Audit source:
Revocation route:
Emergency owner:
```

**The owner field matters.** An identity without an accountable owner tends to keep access after its original purpose ends.

## Practice Steps

1. List three human principals and three workload principals from a sandbox or fictional environment.
2. Record each owner and business purpose.
3. Trace one session from authentication to a resource action.
4. Mark long-lived credentials.
5. Mark shared identities.
6. Record the revocation route for each principal.
7. Draw one trust relationship separately from its permission policy.

> **Expected Result:** the map separates principal, credential, session, trust, permission, and resource scope.

## Troubleshooting

| Problem | Fix |
|---|---|
| **A role appears to be the principal and policy** | Separate the role identity, attached permissions, and active role session |
| **Owner is unknown** | Mark the identity for review instead of assigning a guessed owner |
| **Scope uses a provider root** | Find the smallest resource or project boundary which fits the task |
| **A key has no expiry** | Record replacement with federation or managed identity as a priority |

## Verify Your Work

- [ ] Human and workload identities are separate
- [ ] Trust and permissions are separate
- [ ] Sessions have lifetimes
- [ ] Every identity has an owner or review flag
- [ ] Every grant names a resource scope
- [ ] Revocation routes are recorded

## Next Steps

Continue to [Lesson 2: Effective Permissions](/cloud-iam-zero-trust-course/02-effective-permissions/). Calculate the final decision across policy layers.
