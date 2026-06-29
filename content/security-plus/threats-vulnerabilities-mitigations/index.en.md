---
title: "CompTIA Security+ (SY0-701): Threats, Vulnerabilities, and Mitigations"
date: 2025-01-01
toc: true
draft: false
description: "Master threats, vulnerabilities, and mitigations for the CompTIA Security+ SY0-701 exam. Learn threat actors, attack vectors, vulnerability types, malicious indicators, and mitigation techniques."
genre: ["CompTIA Security+ Course", "Threat Analysis", "Vulnerabilities", "Malware", "Social Engineering", "Attack Vectors", "CompTIA Certification", "Information Security", "Mitigation", "Cybersecurity"]
tags: ["CompTIA Security+", "SY0-701", "threat actors", "attack vectors", "vulnerabilities", "malware", "phishing", "social engineering", "ransomware", "SQL injection", "buffer overflow", "DDoS", "mitigation", "hardening", "IoC"]
cover: "/img/cover/comptia-security-plus-threats-vulnerabilities-mitigations.webp"
coverAlt: "A digital illustration showing various cybersecurity threat actors including a shadowy figure, an anonymous hacker, and an insider threat, alongside icons representing different attack vectors like phishing and malware."
coverCaption: "Master Threats, Vulnerabilities, and Mitigations for the SY0-701 Exam"
---

#### [Click Here to Return To the CompTIA Security+ Course Page](/security-plus-start/)

**Threats, Vulnerabilities, and Mitigations** is **22%** of the **CompTIA Security+ SY0-701** exam, the second-largest domain. This module covers threat actors, attack vectors, vulnerabilities, malicious indicators, and mitigations. *Know the attacker, the attack, and the fix for each scenario the exam presents.*

You cannot defend what you do not understand. This module teaches who attacks, how they get in, where systems are weak, and how you close the gaps. It is the offensive knowledge a defender needs.

## Threat Actors

You profile attackers by motivation and capability.

| Actor | Motivation | Resources |
|-------|-----------|-----------|
| **Nation-state** | Espionage, disruption | Very high (APT) |
| **Organized crime** | Financial gain | High |
| **Hacktivist** | Ideology, publicity | Medium |
| **Insider threat** | Revenge, money, mistakes | Trusted access |
| **Unskilled attacker** | Curiosity, thrill | Low, uses scripts |
| **Shadow IT** | Convenience | Internal, unsanctioned |

**Attributes** differ: internal vs external, resources/funding, and level of sophistication. *Nation-state APTs combine patience with deep funding.*

## Attack Vectors and Surfaces

You identify how attackers reach a target.

- **Message-based**: phishing (email), vishing (voice), smishing (SMS).
- **Business email compromise (BEC)** impersonates an executive to authorize fraud.
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
| **Zero-day** | Unknown, unpatched flaw |

A **zero-day** has no patch because the vendor does not yet know about it. A **misconfiguration** is the most common and most preventable weakness.

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

*The human is the most targeted and most exploitable attack surface.*

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

## Next Steps

Continue with [Security Architecture](/security-plus/security-architecture/) to design defenses, and [Security Operations](/security-plus/security-operations/) to detect and respond. Review the [General Security Concepts](/security-plus/general-security-concepts/) module for controls. Return to the [CompTIA Security+ Course](/security-plus-start/).
