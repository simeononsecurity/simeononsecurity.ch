---
title: "Incident Response Lesson 6: Containment and Recovery"
date: 2026-10-10
lastmod: 2026-10-10
toc: true
draft: false
description: "Plan evidence-aware containment, credential and token response, endpoint recovery, service restoration, communication, and detection improvements."
genre: ["Cybersecurity", "Incident Response", "Security Operations"]
tags: ["incident containment", "incident recovery", "token revocation", "endpoint isolation", "lessons learned", "response plan"]
cover: "/img/cover/incident-containment-recovery.webp"
coverAlt: "An incident response plan moving from containment through recovery and verified improvement."
coverCaption: "Contain risk, preserve evidence, and verify recovery."
---

[Return to the Detection Engineering and Incident Response Course](/detection-engineering-incident-response-course-start/)

**Response actions change evidence and business operations.** State the purpose, owner, approval, risk, rollback path, and success check before execution.

## Choose Action Order

For the course incident, start with this proposed order. The incident commander should decide whether to collect volatile endpoint evidence before isolation when policy permits and ongoing harm is controlled. If exfiltration or active misuse continues, contain first and record what volatile evidence may be lost.

1. Preserve cloud audit, endpoint, mail, DNS, and network evidence.
2. Isolate `HR-LT-044` through the approved endpoint process.
3. Disable or restrict Morgan's identity under the incident authority model.
4. Revoke active sessions and OAuth grants.
5. Remove the malicious mailbox rule after preserving its configuration.
6. Collect the document, script, and task definition under policy. Collect remaining volatile evidence where feasible.
7. Reset credentials and re-register strong factors through a verified recovery path.
8. Rebuild or restore the endpoint from trusted media.
9. Validate service, identity, and endpoint health.
10. Monitor for recurrence before closure.

**Do not execute these steps in a real environment from course notes.** Use the organization's incident plan, legal requirements, and assigned authority.

## Write Action Cards

```text
Action: Revoke Morgan's active sessions and application grants
Purpose: Stop continued use of stolen tokens and delegated mail access
Owner: Identity operations
Approval: Incident commander
Evidence first: Export sign-in, consent, application, and session records
Risk: Business interruption and loss of volatile session detail
Rollback: Reauthorize approved applications after review
Success check: Old sessions fail, grant is absent, fresh sign-in uses approved MFA
```

Write a card for endpoint isolation, mailbox rule removal, credential recovery, endpoint rebuild, and monitoring.

## Define Recovery Gates

| Gate | Evidence |
|---|---|
| **Identity ready** | Password or credential reset, approved factor enrollment, session revocation, consent review |
| **Endpoint ready** | Trusted rebuild, current patches, security agent healthy, no old task or script |
| **Mail ready** | Rule review complete, delegated access reviewed, message trace preserved |
| **Monitoring ready** | Indicators and behavior detections active with owners and expiry dates |
| **Business ready** | Service owner accepts restored function and residual risk |

Recovery does not end when a device boots. **Restoration needs security checks and owner acceptance.**

## Improve the System

Create work items from observed gaps:

- **Block or limit legacy authentication** under the identity policy process
- **Review application consent** and alert on risky delegated scopes
- **Collect process parent and command-line fields** across managed endpoints
- **Monitor scheduled task creation** outside approved deployment tools
- **Link DNS and endpoint network events** by host and time
- **Test the Office-to-PowerShell analytic** with positive and negative cases

Give each item an owner, due date, evidence target, and validation method. An improvement without a validation step is a proposal.

## Practice Steps

1. Write five action cards.
2. Put the cards in execution order.
3. Mark which actions alter evidence.
4. Define four recovery gates.
5. Write a three-sentence stakeholder update with facts, impact, and next checkpoint.
6. Create six improvement work items.

> **Expected Result:** the plan limits access, preserves needed records, restores trusted service, and assigns validation work.

## Troubleshooting

| Problem | Fix |
|---|---|
| **Containment authority is unclear** | Stop at the approval boundary and escalate to the named incident role |
| **Identity disablement affects payroll or safety work** | Use approved compensating controls and document residual risk |
| **Recovery checks fail** | Keep the asset out of service and return to the failed gate |
| **The incident closes with open unknowns** | Record residual uncertainty, owner, review date, and closure rationale |

## Verify Your Work

- [ ] Every action has an owner and approval path
- [ ] The plan records which evidence was preserved before each destructive action and why containment took priority where needed
- [ ] Session and OAuth grant response appears beside credential reset
- [ ] Recovery gates include identity, endpoint, mail, monitoring, and business checks
- [ ] Improvement items carry validation methods
- [ ] Stakeholder text separates confirmed facts from open questions

**Primary references, checked 2026-10-10:** [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) and [NIST Cybersecurity Framework 2.0](https://www.nist.gov/cyberframework).

## Next Steps

Take the [Course Quiz](/detection-engineering-incident-response-course/07-quiz-answer-key/), then complete the [Capstone](/detection-engineering-incident-response-course/08-capstone-answer-key/).
