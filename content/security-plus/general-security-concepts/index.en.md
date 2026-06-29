---
title: "CompTIA Security+ (SY0-701): General Security Concepts"
date: 2025-01-01
toc: true
draft: false
description: "Master general security concepts for the CompTIA Security+ SY0-701 exam. Learn security controls, the CIA triad, change management, cryptography, PKI, and Zero Trust."
genre: ["CompTIA Security+ Course", "Security Fundamentals", "Cryptography", "PKI", "Zero Trust", "Access Control", "CompTIA Certification", "Information Security", "Security Controls", "Cybersecurity"]
tags: ["CompTIA Security+", "SY0-701", "security controls", "CIA triad", "non-repudiation", "AAA", "Zero Trust", "cryptography", "PKI", "encryption", "hashing", "digital signatures", "certificates", "change management"]
cover: "/img/cover/comptia-security-plus-general-security-concepts.webp"
coverAlt: "A digital security operations center with a large interface showing security concepts like CIA triad, surrounded by abstract representations of security controls and cryptographic elements."
coverCaption: "Master General Security Concepts for the SY0-701 Exam"
---

#### [Click Here to Return To the CompTIA Security+ Course Page](/security-plus-start/)

**General Security Concepts** is **12%** of the **CompTIA Security+ SY0-701** exam. This module covers security controls, core principles, change management, cryptography, PKI, and Zero Trust. *These fundamentals appear throughout the exam, so build a solid base here.*

Every other domain builds on these ideas. You classify controls, protect the three pillars of security, verify identity, and encrypt data. This module gives you the vocabulary and the mental models the rest of the course assumes.

## Security Controls

You classify controls by category and by function.

| Category | Example |
|----------|---------|
| **Technical** | Firewall, encryption, MFA |
| **Managerial** | Policies, risk assessments |
| **Operational** | Security training, guards |
| **Physical** | Locks, fences, cameras |

Controls also have a **function**:

| Function | Purpose |
|----------|---------|
| **Preventive** | Stops an event (firewall) |
| **Detective** | Identifies an event (IDS) |
| **Corrective** | Fixes after an event (backup restore) |
| **Deterrent** | Discourages an attacker (warning sign) |
| **Compensating** | An alternative when the primary control fails |
| **Directive** | Guides behavior (policy) |

## Fundamental Security Concepts

You protect the **CIA triad**:

- **Confidentiality** keeps data secret from unauthorized access.
- **Integrity** ensures data is not altered.
- **Availability** keeps data and systems accessible.

**Non-repudiation** proves an action happened and who did it, using digital signatures. **AAA** is the access trio:

| Term | Meaning |
|------|---------|
| **Authentication** | Prove who you are |
| **Authorization** | What you are allowed to do |
| **Accounting** | Record what you did |

**Zero Trust** assumes no implicit trust. It splits into a **control plane** (policy decisions) and a **data plane** (policy enforcement), and verifies every request.

## Change Management

You control change so security and uptime stay intact.

- **Approval process** routes changes through a change board.
- **Impact analysis** assesses what a change could break.
- **Backout plans** restore the prior state if a change fails.
- **Maintenance windows** schedule change for low-impact times.
- **Version control** tracks configuration and code over time.

*Unmanaged change is a top cause of outages and security gaps.*

## Cryptographic Solutions

You protect data with the right cryptographic tool.

| Tool | Provides |
|------|----------|
| **Symmetric encryption (AES)** | Fast confidentiality, one shared key |
| **Asymmetric encryption (RSA, ECC)** | Key exchange, two keys |
| **Hashing (SHA-256)** | Integrity, one-way fingerprint |
| **Digital signature** | Integrity plus non-repudiation |
| **HMAC** | Integrity with a shared key |

**Salting** adds random data to a hash to defeat rainbow tables. **Key stretching** slows brute force. A **TPM** and **HSM** store keys in hardware. Learn the practical side in [how to get hashes of files on Linux](/guides/how-to-get-hashes-of-files-on-linux/).

## Public Key Infrastructure (PKI)

You manage trust with certificates.

- A **Certificate Authority (CA)** issues and signs certificates.
- A **Registration Authority (RA)** verifies identity before issuance.
- A **Certificate Revocation List (CRL)** and **OCSP** report revoked certificates.
- **Key escrow** stores keys for recovery.

| Certificate type | Use |
|------------------|-----|
| **Wildcard** | Covers all subdomains |
| **SAN** | Multiple specific domains |
| **Root** | Top of the trust chain |
| **Self-signed** | Internal, not publicly trusted |

## Authentication and Access

You verify identity with multiple factors.

**MFA** combines factors: something you **know**, **have**, **are**, **do**, or somewhere you **are**. **SSO** lets one login reach many apps, often with **federation** through SAML or OpenID Connect. Strong, unique passwords remain the baseline, covered in [how to create strong passwords](/articles/how-to-create-strong-passwords/).

## Next Steps

Continue with [Threats, Vulnerabilities, and Mitigations](/security-plus/threats-vulnerabilities-mitigations/) and [Security Architecture](/security-plus/security-architecture/). Operationalize these concepts in [Security Operations](/security-plus/security-operations/). Return to the [CompTIA Security+ Course](/security-plus-start/) and review [tips for passing CompTIA exams](/articles/tips-and-tricks-for-passing-comptia-exams/).
