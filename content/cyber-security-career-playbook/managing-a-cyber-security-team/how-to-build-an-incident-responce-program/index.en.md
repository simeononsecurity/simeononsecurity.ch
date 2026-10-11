---
title: "How to Build an Incident Response Program"
draft: false
toc: true
date: 2023-07-04
lastmod: 2026-10-10
description: "Build an incident response program aligned with NIST SP 800-61 Rev. 3 through authority, severity, evidence, communication, recovery, and exercises."
genre: ["Incident Response", "Cybersecurity Management"]
tags: ["incident response program", "NIST SP 800-61 Rev. 3", "incident response plan", "tabletop exercise", "recovery validation"]
cover: "/img/cover/An_animated_illustration_of_a_shield_protecting_a_network.webp"
coverAlt: "An incident response team reviewing evidence, decisions, and recovery status"
coverCaption: "Prepare authority and evidence before an incident."
---

[Return to the Cybersecurity Career Playbook](/cyber-security-career-playbook-start/)

NIST SP 800-61 Rev. 3, published in April 2025, integrates incident response across Cybersecurity Framework 2.0. Govern, Identify, and Protect support incident-response preparation. Detect, Respond, and Recover form the incident-response life cycle. Improvement feeds lessons back into risk management.

## Define Authority

Name who declares an incident, assigns severity, authorizes containment, accepts service impact, contacts counsel, handles privacy and notification review, speaks externally, approves recovery, and closes the incident.

Create contact and backup routes which work when normal identity, email, or ticket systems fail.

## Build the Plan

The plan should cover:

- Service, data, and third-party scope
- Severity and escalation criteria
- Evidence handling and time sources
- Communications and approved channels
- Containment options and business trade-offs
- Eradication and recovery validation
- Legal, privacy, regulator, insurer, and contract review
- Backup, disaster recovery, and provider dependencies
- Decision and action records
- Improvement ownership

Containment timing depends on evidence, impact, and authority. Preserve needed evidence and avoid destructive steps without the incident lead's decision.

## Create Playbooks

Build short playbooks for priority scenarios such as stolen credentials, ransomware, public-service outage, data exposure, vendor compromise, or lost device. Each playbook needs triggers, evidence, owners, decisions, recovery tests, and records.

## Tabletop Exercise

Use a fictional payroll portal. A privileged login occurs from an unexpected location, then payroll export volume rises.

Injects:

1. Identity logs are available but endpoint logs are delayed.
2. Disabling the account stops payroll processing.
3. The provider reports a support session at the same time.
4. A reporter asks for comment.
5. Recovery succeeds, but the original access path stays unknown.

Produce a severity decision, evidence list, containment decision, communication route, recovery test, and unresolved-risk owner.

**Pass condition:** Every inject has an owner and timestamped decision. Recovery includes functional and security validation. Unknown cause stays open rather than being presented as resolved.

## References

- [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final)
- [NIST Incident Response project](https://csrc.nist.gov/projects/incident-response)

Use [Cybersecurity Policies and Procedures](/cyber-security-career-playbook/managing-a-cyber-security-team/how-to-develop-cybersecurity-policies-and-procedures/) to document authority and evidence requirements.
