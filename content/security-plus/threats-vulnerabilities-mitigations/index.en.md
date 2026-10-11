---
title: "Security+ SY0-701 Threats, Vulnerabilities, and Mitigations"
date: 2025-01-01
lastmod: 2026-10-10
toc: true
draft: false
description: "Trace a synthetic phishing-to-export chain for SY0-701. Separate evidence from assumptions, select layered controls, and test residual risk."
genre: ["CompTIA Security+ Course", "Threat Analysis", "Vulnerabilities", "Malware", "Social Engineering", "Attack Vectors", "CompTIA Certification", "Information Security", "Mitigation", "Cybersecurity"]
tags: ["CompTIA Security+", "SY0-701", "threat actors", "attack vectors", "vulnerabilities", "malware", "phishing", "social engineering", "ransomware", "SQL injection", "buffer overflow", "DDoS", "mitigation", "hardening", "IoC"]
cover: "/img/cover/comptia-security-plus-threats-vulnerabilities-mitigations.webp"
coverAlt: "A digital illustration showing various cybersecurity threat actors including a shadowy figure, an anonymous hacker, and an insider threat, alongside icons representing different attack vectors like phishing and malware."
coverCaption: "Master Threats, Vulnerabilities, and Mitigations for the SY0-701 Exam"
---

[Click Here to Return To the CompTIA Security+ Course Page](/security-plus-start/)

**Threats, Vulnerabilities, and Mitigations** is **22%** of the **CompTIA Security+ SY0-701** exam, the second-largest domain. This module covers threat actors, attack vectors, vulnerabilities, malicious indicators, and mitigations. *Know the attacker, the attack, and the fix for each scenario the exam presents.*

You cannot defend what you do not understand. This module teaches who attacks, how they get in, where systems are weak, and how you close the gaps. It is the offensive knowledge a defender needs.

## Threat Actors

You profile attackers by motivation and capability.

| Actor | Motivation | Resources |
|-------|-----------|-----------|
| **Nation-state** | May seek espionage or disruption | Varies by actor and operation |
| **Organized crime** | Often seeks financial gain | Varies by group |
| **Hacktivist** | May seek publicity or change | Varies by group |
| **Insider threat** | Revenge, money, mistakes | Trusted access |
| **Unskilled attacker** | Motivation unknown without evidence | May rely on published tools |
| **Shadow IT** | Convenience | Internal, unsanctioned |

**Attributes** differ: internal vs external, resources/funding, and level of sophistication. Do not infer actor identity from a single indicator. Investigate the operation and evidence.

## Attack Vectors and Surfaces

You identify how attackers reach a target.

- **Message-based**: phishing (email), vishing (voice), smishing (SMS).
- **Business email compromise (BEC)** uses a message which appears to come from a known source to induce a fraudulent request. The impersonated person need not be an executive.
- **Supply chain** attacks compromise a trusted vendor or update.
- **Removable media** spreads malware over USB.
- **Unsecured networks** expose wireless and wired traffic.

## Vulnerability Types

You categorize weaknesses by where they live.

| Vulnerability | Example |
|---------------|---------|
| **Application** | Injection, memory leaks, race conditions |
| **Operating system** | Unpatched kernel flaws |
| **Hardware** | Firmware, end-of-life devices |
| **Virtualization** | VM escape, resource reuse |
| **Cloud** | Misconfiguration, weak IAM |
| **Zero-day** | A previously unknown vulnerability at the time of attack. Track awareness, disclosure, exploitation, and fix status separately. |

A zero-day attack exploits a previously unknown vulnerability. Once discovered, the same flaw still needs a patch and exposure review. Track awareness, disclosure, exploitation, and fix status separately. Misconfigurations are one important, preventable source of exposure.

## Indicators of Malicious Activity

You recognize attacks by their signs.

| Attack | Indicator |
|--------|-----------|
| **Malware** | Unexpected processes, beaconing traffic |
| **Ransomware** | Encrypted files, ransom note |
| **Password attack** | Many failed logins, spraying |
| **DDoS** | Traffic spike, service outage |
| **DNS attack** | Redirected or poisoned lookups |
| **On-path (MITM)** | Certificate warnings |

You also know application attacks: **SQL injection** runs database commands, **XSS** runs script in a victim's browser, **buffer overflow** writes past memory bounds, and **CSRF** forces an action with a logged-in session.

## Social Engineering

You defend against attacks on people.

- **Pretexting** invents a believable scenario.
- **Impersonation** poses as IT, a vendor, or an executive.
- **Watering hole** infects a site the target trusts.
- **Tailgating and piggybacking** bypass physical access.
- **Pharming** redirects users to fake sites.

Training, reporting channels, and technical controls reduce the impact of social engineering.

## Mitigation Techniques

You reduce risk with layered controls.

| Technique | Effect |
|-----------|--------|
| **Patching** | Closes known vulnerabilities |
| **Encryption** | Protects data confidentiality |
| **Segmentation** | Limits lateral movement |
| **Least privilege** | Shrinks the blast radius |
| **Monitoring** | Detects activity early |
| **Hardening** | Removes unneeded services and defaults |
| **Access control (ACL)** | Restricts who reaches what |

**Hardening** disables unused ports and services, changes default credentials, and applies secure baselines. To see why legacy systems stay exposed, read [why OT/ICS PLC cybersecurity is fundamentally broken](/articles/ot-ics-plc-cybersecurity-fundamentally-broken/).

## Practice: Trace an Attack Chain

Continue the fictional Harbor Library case. An employee receives a message asking them to open a new invoice. An attachment runs a script on `laptop-17`. The security log later shows an unusual sign-in to the `archive` account and a member export to `/tmp/out`. The observed facts are message, script execution, sign-in, and export. The actor's identity and intent are unknown.

Build a six-column worksheet: observation and timestamp, attack vector, exploited weakness, possible impact, control, and validation. For example, the message is a possible phishing vector; the attachment execution needs verification through endpoint telemetry. The export suggests a confidentiality risk, but you still need destination, owner, and authorization evidence.

Choose at least three layered controls: block or isolate risky attachments, use phishing-resistant MFA for the archive role, and restrict exports by role and destination. Add monitoring for unusual exports and a tested backup for recovery. Explain which control is preventive, detective, or corrective. State a residual risk: an authorized user or compromised endpoint might still misuse permitted access. Validate with synthetic negative and positive access cases; mark them unrun if no disposable lab exists.

Pass when the worksheet distinguishes indicator from conclusion, avoids naming a threat actor without evidence, names an owner for each control, and gives a test which would show a control working. Review the [CompTIA SY0-701 objectives](https://partners.comptia.org/docs/default-source/resources/comptia-security-sy0-701-exam-objectives-(4-0).pdf) and [NIST CSF 2.0](https://www.nist.gov/cyberframework).

## Next Steps

Continue with [Security Architecture](/security-plus/security-architecture/) to design defenses, and [Security Operations](/security-plus/security-operations/) to detect and respond. Review the [General Security Concepts](/security-plus/general-security-concepts/) module for controls. Return to the [CompTIA Security+ Course](/security-plus-start/).
