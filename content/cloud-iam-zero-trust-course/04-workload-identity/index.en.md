---
title: "Cloud IAM Lesson 4: Workload Identity"
date: 2026-10-10
lastmod: 2026-10-10
toc: true
draft: false
description: "Design workload identity with federation, managed identities, service accounts, short-lived tokens, narrow roles, and verified rotation or revocation."
genre: ["Cloud Security", "Identity and Access Management", "DevSecOps"]
tags: ["workload identity", "service account security", "managed identity", "OIDC federation", "short-lived credentials", "cloud secrets"]
cover: "/img/cover/cloud-workload-identity.webp"
coverAlt: "A deployment workload exchanging an external identity token for narrow temporary cloud access."
coverCaption: "Let the platform issue temporary workload access."
---

[Return to the Cloud IAM and Zero Trust Lab Course](/cloud-iam-zero-trust-course-start/)

**A workload needs identity without a stored cloud key.** Prefer platform identity or federation which exchanges trusted workload claims for short-lived access.

## Choose the Pattern

| Pattern | Fit | Main risk |
|---|---|---|
| **Platform-managed identity** | Workload runs inside one cloud | Attached identity receives broad resource access |
| **OIDC workload federation** | CI/CD, Kubernetes, or external workload | Trust conditions accept unintended repositories, branches, or subjects |
| **Service account with short-lived impersonation** | Central workload identity model | Users or workloads impersonate a more privileged account |
| **Static key or client secret** | Legacy exception | Copy, leak, unclear owner, weak expiry, and difficult revocation |

Use static credentials only under a documented exception with owner, storage, rotation, monitoring, and retirement date.

## Bind Trust Narrowly

Trust policy answers **who gets a session**. Permission policy answers **what the session does**.

For a CI workflow, bind trust to:

- **Issuer:** the approved identity provider
- **Audience:** the cloud token exchange endpoint or named application
- **Subject:** exact organization, repository, environment, branch, or service account
- **Session duration:** enough for one job
- **Resource role:** only required actions at the required scope

Avoid a wildcard subject covering every repository or branch. Review pull-request contexts separately from protected deployment environments.

## Protect Service Accounts

Google Cloud guidance warns against automatic broad grants, service account keys, privileged impersonation paths, and project-wide service account access. The same review logic applies across providers.

Check these escalation paths:

1. Who edits the workload's trust policy?
2. Who changes attached roles or bindings?
3. Who impersonates the identity?
4. Who deploys code under the identity?
5. Which metadata or token endpoint exposes credentials?
6. Which logs record token exchange and resource use?

**Control-plane permission is often more sensitive than the workload's current data permission.** A principal able to rewrite policy might grant itself new access.

## Practice Steps

Use the fictional payroll report build.

1. Define the workflow issuer, audience, and subject.
2. Set a sixty-minute maximum session.
3. Grant read access to one report store.
4. Exclude policy administration, identity administration, and write actions.
5. Name the code owner and identity owner.
6. Define token exchange and resource-access logs.
7. Write a revocation test.
8. Record the static key retirement date.

> **Expected Result:** the workload receives a temporary session from exact claims and lacks policy administration rights.

## Troubleshooting

| Problem | Fix |
|---|---|
| **Federation accepts too many workflows** | Narrow subject, audience, environment, and repository claims |
| **The workload needs many services** | Split identities by task and resource boundary |
| **A key still exists after migration** | Disable, monitor, remove, and verify rejected use through the approved process |
| **Token exchange succeeds but access fails** | Separate trust success from permission, scope, condition, and deny evaluation |

## Verify Your Work

- [ ] No long-lived key is required in the target design
- [ ] Trust claims are exact
- [ ] Session duration is bounded
- [ ] Permission scope matches one task
- [ ] Policy editors and impersonators are reviewed
- [ ] Revocation has a test and evidence source

**Primary reference, checked 2026-10-10:** [Google Cloud best practices for service accounts](https://docs.cloud.google.com/iam/docs/best-practices-service-accounts).

## Next Steps

Continue to [Lesson 5: Zero Trust Policy](/cloud-iam-zero-trust-course/05-zero-trust-policy/). Add resource, device, context, and telemetry to access decisions.
