---
title: "Cloud IAM Lesson 5: Zero Trust Policy"
date: 2026-10-10
lastmod: 2026-10-10
toc: true
draft: false
description: "Turn zero trust principles into explicit cloud access decisions using identity, resource, device, workload, context, policy enforcement, and telemetry."
genre: ["Cloud Security", "Zero Trust", "Identity and Access Management"]
tags: ["zero trust architecture", "NIST SP 800-207", "conditional access", "identity policy", "cloud authorization", "continuous verification"]
cover: "/img/cover/cloud-zero-trust-policy.webp"
coverAlt: "A cloud access request evaluated by identity, device, resource, context, and telemetry policy."
coverCaption: "Evaluate each request against resource-focused policy."
---

[Return to the Cloud IAM and Zero Trust Lab Course](/cloud-iam-zero-trust-course-start/)

**Zero trust removes implicit trust from location, ownership, and prior access.** Policy evaluates a subject, resource, action, and current context before granting a session or request.

## Build the Decision

```text
Subject: Who or which workload requests access?
Credential: How was identity established?
Device or runtime: What executes the request?
Resource: Which exact asset receives access?
Action: Which operation is requested?
Context: Time, location, risk, environment, ticket, or branch
Policy decision: Allow, block, step up, narrow, or require approval
Enforcement point: Where is the decision applied?
Telemetry: Which event records decision and use?
Revocation: Which signal ends access?
```

This record links architecture to an observable decision.

## Apply Seven Tenets

| NIST-aligned idea | Cloud IAM action |
|---|---|
| **Treat resources individually** | Scope grants to the target application, project, vault, or data store |
| **Secure communication** | Require approved encrypted endpoints and authenticated service paths |
| **Per-session access** | Issue short sessions rather than standing credentials |
| **Dynamic policy** | Evaluate identity, resource, device, workload, risk, and context |
| **Monitor asset state** | Feed device and workload health into policy where supported |
| **Authenticate and authorize before access** | Separate identity proof from resource permission |
| **Collect evidence** | Record policy decision, session issuance, action, denial, and revocation |

Zero trust does not mean a prompt before every API call. **Policy enforcement should match resource sensitivity and current risk.**

## Design a Payroll Policy

```text
Subject: payroll-report-build workload
Credential: OIDC token from protected production environment
Runtime: approved hosted runner image
Resource: payroll-report storage
Action: read one input prefix and write one report prefix
Context: protected branch, approved environment, sixty-minute session
Decision: allow exact object actions, deny policy administration
Enforcement: cloud token exchange and storage policy
Telemetry: token exchange, object access, denied action, policy change
Revocation: remove trust subject or disable environment
```

Add a separate policy for human reviewers. Do not reuse the workload identity for people.

## Test Policy Behavior

Build four tests:

1. **Expected allow:** approved workload reads the input prefix.
2. **Expected deny:** same workload tries to change IAM policy.
3. **Context failure:** unprotected branch requests a token.
4. **Revocation:** removed subject fails token exchange.

For each test, save request context, decision, audit event, and cleanup state.

> **Expected Result:** required work succeeds, policy administration fails, unapproved context fails, and revoked trust stops new sessions.

## Troubleshooting

| Problem | Fix |
|---|---|
| **Policy trusts a network range alone** | Add verified identity, device or workload, resource, and action conditions |
| **A deny blocks emergency work** | Use a separately governed recovery path with monitoring and expiry |
| **Health signals are unavailable** | Apply stronger session and resource limits, then record the visibility gap |
| **Revocation leaves active sessions** | Account for token lifetime and use provider session revocation where supported |

## Verify Your Work

- [ ] Decision record names subject, resource, action, and context
- [ ] Human and workload policies are separate
- [ ] Enforcement points are named
- [ ] Four behavior tests exist
- [ ] Audit evidence covers allow, deny, and revocation
- [ ] Network location is not the only trust signal

**Primary references, checked 2026-10-10:** [NIST SP 800-207](https://csrc.nist.gov/pubs/sp/800/207/final) and [NIST SP 800-207A](https://csrc.nist.gov/pubs/sp/800/207/A/final).

## Next Steps

Continue to [Lesson 6: Disposable Cloud Lab](/cloud-iam-zero-trust-course/06-disposable-cloud-lab/). Create, test, remove, and verify one narrow identity path.
