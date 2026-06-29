---
title: "CompTIA SecurityX (CAS-005): Security Engineering"
date: 2025-01-01
toc: true
draft: false
description: "Master security engineering for the CompTIA SecurityX CAS-005 exam. Learn IAM troubleshooting, endpoint and server security, hardware roots of trust, OT/ICS security, automation, and advanced cryptography."
genre: ["CompTIA SecurityX Course", "Security Engineering", "Cryptography", "Hardware Security", "Endpoint Security", "OT Security", "Automation", "CASP+", "Enterprise Security", "Cybersecurity"]
tags: ["CompTIA SecurityX", "CASP+", "CAS-005", "security engineering", "IAM", "SAML", "Kerberos", "EDR", "SELinux", "TPM", "HSM", "Secure Boot", "OT", "ICS", "SCADA", "post-quantum cryptography", "homomorphic encryption", "SOAR", "SCAP"]
cover: "/img/cover/comptia-securityx-cas-005-security-engineering.webp"
coverAlt: "A digital illustration showing interconnected servers and endpoints in a futuristic security environment, with glowing circuits and cryptographic elements against a dark background."
coverCaption: "Master Security Engineering for the CAS-005 Exam"
---

#### [Click Here to Return To the CompTIA SecurityX Course Page](/casp-plus-start/)

**Security Engineering** is **31%** of the **CompTIA SecurityX (CAS-005)** exam, the single heaviest domain. This module covers how you implement and troubleshoot the controls an architect designed. *Build deep hands-on familiarity with cryptography and hardware roots of trust, because this domain rewards depth.*

Engineering is where designs meet reality. You configure identity systems, harden endpoints, root trust in hardware, secure industrial systems, automate at scale, and apply the right cryptography to each job. Expect performance-based questions here.

## Troubleshooting IAM Components

You diagnose identity problems across protocols and services.

| Component | Role | Common failure |
|-----------|------|----------------|
| **SAML** | Web SSO via XML assertions | Clock skew, bad certificate, wrong endpoint |
| **OpenID Connect** | AuthN on top of OAuth | Misconfigured redirect URI |
| **MFA** | Adds a second factor | Time drift on TOTP tokens |
| **Kerberos** | Ticket-based authN | Time skew over 5 minutes breaks tickets |
| **PAM** | Privileged access management | Vault misconfiguration, broken check-out |
| **802.1X** | Port-based network access | RADIUS or supplicant misconfiguration |

*Kerberos and SAML both break when system clocks drift, so check time sync first.*

## Endpoint and Server Security

You harden the hosts where attackers land.

- **EDR** (Endpoint Detection and Response) records endpoint activity and responds to threats.
- **Application control** allowlists approved software and blocks everything else.
- **HIPS/HIDS** detect and block host-level intrusions.
- **MDM** (Mobile Device Management) enforces policy on phones and tablets.
- **SELinux** applies mandatory access control on Linux so a compromised process cannot exceed its label.

## Threat-Actor TTPs

You recognize the tactics, techniques, and procedures attackers use after a foothold:

- **Injections** force an app to run attacker input as code.
- **Privilege escalation** moves from a normal account to admin.
- **Credential dumping** steals hashes and tokens from memory.
- **Lateral movement** spreads from one host to others.
- **Defensive evasion** disables logging and tools to stay hidden.

You map these to MITRE ATT&CK, the framework introduced in [Governance, Risk, and Compliance](/casp-plus/governance-risk-compliance/).

## Network Infrastructure Security

You troubleshoot the protocols that keep traffic trustworthy.

| Technology | Protects | Notes |
|-----------|----------|-------|
| **DNSSEC** | DNS integrity | Signs records to stop spoofing |
| **SPF** | Email sender IPs | Lists who may send for a domain |
| **DKIM** | Email integrity | Signs messages cryptographically |
| **DMARC** | Email policy | Tells receivers how to handle SPF/DKIM failures |
| **TLS** | Traffic confidentiality | Watch for expired certs and weak ciphers |

```bash
# Check a domain's SPF and DMARC records during email troubleshooting
dig +short TXT example.com | grep spf
dig +short TXT _dmarc.example.com
```

## Hardware Security Technologies

You root trust in hardware so software cannot lie about its own integrity.

| Technology | Role |
|-----------|------|
| **TPM** | Chip storing keys and boot measurements |
| **HSM** | Appliance for high-volume key operations |
| **vTPM** | Virtual TPM for virtual machines |
| **Secure Boot** | Allows only signed bootloaders |
| **Measured Boot** | Records each boot stage for attestation |
| **Self-encrypting drive** | Encrypts data at the hardware level |

## Specialized and Legacy Systems

You secure systems that cannot run standard endpoint tools.

- **OT, SCADA, and ICS** run critical infrastructure and often use old, fragile protocols. You isolate them with the Purdue model and monitor passively.
- **IoT** devices ship with weak defaults, so you segment them and change credentials.
- **SoC and embedded systems** have limited resources, so you secure them at the network boundary.

These systems carry deep, structural weaknesses, as explored in [why OT/ICS/PLC cybersecurity is fundamentally broken](/articles/ot-ics-plc-cybersecurity-fundamentally-broken/).

## Automation to Secure the Enterprise

You automate so security scales beyond manual effort.

- **PowerShell, Bash, and Python** script repetitive tasks and response actions.
- **Infrastructure as Code (IaC)** defines systems in version-controlled files, covered in [Ansible for beginners](/articles/ansible-for-beginners/).
- **SOAR** orchestrates and automates incident response.
- **SCAP, OVAL, and XCCDF** standardize how you express and check secure configurations.

## Advanced Cryptography

You explain and apply modern cryptographic concepts.

| Concept | What it does |
|---------|--------------|
| **Post-quantum cryptography** | Resists attacks from quantum computers (ML-KEM, ML-DSA) |
| **Homomorphic encryption** | Computes on encrypted data without decrypting |
| **Forward secrecy** | A stolen key cannot decrypt past sessions |
| **Key stretching** | Strengthens weak passwords (PBKDF2, bcrypt, Argon2) |

You then match the **use case** to the right technique:

- **Tokenization** replaces sensitive data with a non-sensitive token.
- **Code signing** proves software came from a trusted source and was not altered.
- **Digital signatures** provide integrity and non-repudiation.
- **Symmetric** cryptography is fast for bulk data; **asymmetric** solves key distribution and signatures.

## Next Steps

With the controls engineered, continue to [Security Operations](/casp-plus/security-operations/) to monitor and respond, then revisit [Security Architecture](/casp-plus/security-architecture/) for the design context. Return to the [CompTIA SecurityX Course](/casp-plus-start/) and review [tips for passing CompTIA exams](/articles/tips-and-tricks-for-passing-comptia-exams/).
