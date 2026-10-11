---
title: "Turn IT Administration Work Into Cybersecurity Evidence"
draft: false
toc: true
date: 2023-07-01
lastmod: 2026-10-10
description: "Map IT administration tasks to security roles, complete a safe hardening project, and save evidence employers may review."
tags: ["systems administration", "cybersecurity portfolio", "security hardening", "IT to cybersecurity", "practical experience"]
cover: "/img/cover/A_symbolic_illustration_representing_cybersecurity_concepts.webp"
coverAlt: "A systems administrator documenting security controls on a computer"
coverCaption: "Turn operational work into clear security evidence."
---

[Return to the Cybersecurity Career Playbook](/cyber-security-career-playbook-start/)

Systems administration develops useful security habits. The value comes from **specific tasks and evidence**, not the job title by itself. Support, networking, software, audit, military, and business operations also offer valid entry routes.

## Map Tasks to Roles

| Prior task | Security evidence | Related role family |
|---|---|---|
| **Manage accounts and groups** | Access review, least-privilege decision, exception record | Identity and access management |
| **Patch systems** | Asset list, change ticket, test, rollback, verification | Security engineering or vulnerability management |
| **Review logs** | Timeline, observation, hypothesis, escalation | Security operations or incident response |
| **Configure networks** | Data flow, trust boundary, rule review | Network or cloud security |
| **Back up and restore data** | Recovery test, result, gap, follow-up | Resilience or incident recovery |
| **Support users** | Clear instructions, identity checks, safe escalation | Security awareness or operations |

## Complete a Safe Project

Use an owned disposable Linux or Windows virtual machine. Keep the VM behind network address translation. Do not expose it to the public internet. Take a snapshot first.

Create a **hardening change record** with these fields:

1. Asset purpose and starting state
2. One selected control, such as removing an unused local account or disabling an unused service
3. Risk addressed
4. Exact change
5. Before and after evidence
6. Service or login test
7. Rollback command or snapshot name
8. Remaining limitation

Test a denied case. For example, confirm the removed account no longer authenticates or the disabled service no longer listens. Then confirm the intended user or service still works.

**Pass condition:** Another learner should identify the asset, repeat the change on a fresh VM, observe the expected allowed and denied results, and restore the starting state from your record.

## Publish Safe Evidence

Remove usernames, internal addresses, tokens, customer data, employer names, and unique infrastructure details. Use reserved example addresses or synthetic data. State where the result came from and which parts are illustrative.

Your portfolio entry should include:

- A short problem statement
- The starting state
- The change and reason
- Evidence of the expected result
- One failed attempt or rejected option
- Rollback and cleanup
- Limits and next step

## Next Step

Compare your artifact with three target job postings. Mark each repeated task as demonstrated, partly demonstrated, or missing. Choose the next project from a repeated missing task.

## References

- [NICE Framework current versions](https://www.nist.gov/itl/applied-cybersecurity/nice/nice-framework-resource-center/nice-framework-current-versions)
- [NIST Cybersecurity Framework 2.0](https://www.nist.gov/cyberframework)

Use the result in the [Cybersecurity Resume Guide](/cyber-security-career-playbook/getting-a-job-in-cyber-security/resume-writing-tips-for-cybersecurity-professionals/).
