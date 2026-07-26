---
title: "CompTIA SecurityX Course: Complete Study Guide for the CAS-005 Exam"
date: 2025-01-01
toc: true
draft: false
description: "A comprehensive CompTIA SecurityX (CAS-005, formerly CASP+) study course covering governance risk and compliance, security architecture, security engineering, and security operations for advanced security practitioners."
genre: ["CompTIA SecurityX Course", "CASP+ Certification", "Security Architecture", "Security Engineering", "Governance Risk Compliance", "CompTIA Certification", "Enterprise Security", "Advanced Security", "Cryptography", "Threat Hunting"]
tags: ["CompTIA SecurityX", "CASP+", "CAS-005", "security architecture", "security engineering", "governance", "risk", "compliance", "cryptography", "zero trust", "threat hunting", "incident response", "cloud security", "post-quantum cryptography", "enterprise security", "CompTIA certification", "SIEM", "IAM", "PKI", "OT security", "MITRE ATT&CK"]
cover: "/img/cover/comptia-securityx-cas-005-exam-study-guide-illustration.webp"
coverAlt: "A futuristic cybersecurity command center with a large digital screen showing data analytics, surrounded by advanced security tools like firewalls and cloud security devices, all on a dark background."
coverCaption: "Master CompTIA SecurityX and Lead Enterprise Security"
---

**CompTIA SecurityX (CAS-005)** is the advanced-level certification for security architects and senior engineers, *formerly known as CASP+*. It validates your ability to architect, engineer, and operate secure solutions across complex enterprise environments. *CompTIA recommends a minimum of 10 years of general IT experience with at least 5 years of hands-on security experience.*

This course covers all four exam domains in depth. Each domain page includes detailed tables, worked examples, exam tips, and cross-links to related domains and articles.

| Domain | Title | Exam Weight |
|--------|-------|-------------|
| 1.0 | [Governance, Risk, and Compliance](/casp-plus/governance-risk-compliance/) | 20% |
| 2.0 | [Security Architecture](/casp-plus/security-architecture/) | 27% |
| 3.0 | [Security Engineering](/casp-plus/security-engineering/) | **31%** |
| 4.0 | [Security Operations](/casp-plus/security-operations/) | 22% |

**Exam details:** Maximum of 90 questions, multiple-choice and performance-based, 165 minutes, pass/fail with no scaled score. Confirm current details at [comptia.org/certifications/securityx](https://www.comptia.org/certifications/securityx).

## Resources

- [CompTIA SecurityX (CASP+) Practice Test](/casp-plus-practice-test/) — Test your readiness across all four domains
- [Tips for Passing CompTIA Exams](/articles/tips-and-tricks-for-passing-comptia-exams/)
- [Official CAS-005 Exam Objectives](https://www.comptia.org/certifications/securityx)
- [Cybersecurity Career Playbook](/cyber-security-career-playbook-start/)
- [CompTIA Security+ Course](/security-plus-start/) — Foundational prerequisite
- [CompTIA CySA+ Course](/cysa-plus-start/) — Recommended prerequisite
- [CompTIA SecurityAI+ Course](/secai-plus-start/) — Companion course for AI security
- [Additional Learning Resources](/recommendations/learning_resources/)

-----

## Domain 1: Governance, Risk, and Compliance (20%)

### [Governance, Risk, and Compliance](/casp-plus/governance-risk-compliance/)

*Think like an advisor to leadership, not a technician. Every answer should be grounded in business risk.*

The GRC domain establishes how the entire security program is governed, measured, and validated. You set direction through a documented policy hierarchy — policies, standards, procedures, and guidelines — and align the program to frameworks like COBIT and ITIL. Maturity models including CMMC and the NIST CSF Tiers measure how optimized and repeatable your processes are.

Risk management runs a continuous cycle of identify, assess, respond, and monitor. You perform quantitative analysis using **SLE, ARO, and ALE** formulas, and conduct a **Business Impact Analysis** to define RTO, RPO, MTBF, and MTTR for critical systems. Risk responses — mitigate, transfer, accept, avoid — are selected based on the ALE compared to the cost of controls.

Key skills in this domain:

- Apply the governance document hierarchy (policy, standard, procedure, guideline) and know which is binding
- Calculate ALE and cost-justify security controls
- Distinguish SOC 2 Type I vs. Type II for vendor assessments
- Map STRIDE threat categories to their countermeasures
- Explain AI-specific attacks: prompt injection, training data poisoning, model theft, model inversion, and deep fakes
- Apply GDPR, CCPA, HIPAA, and COPPA requirements in scenarios
- Assess supply chain risk using SBOM, right-to-audit clauses, and subprocessor reviews

-----

## Domain 2: Security Architecture (27%)

### [Security Architecture](/casp-plus/security-architecture/)

*Design decisions matter more than individual controls here. Always ask: where does the control go, and what does it inspect?*

Security Architecture is the second-heaviest domain and the design foundation for everything else. You place security components — firewalls, IPS/IDS, WAF, NAC, API gateways, CDN — where traffic flows, using network topology patterns like DMZ (two-firewall), screened subnet, VLANs, and air gaps to define what attackers can reach.

Availability design uses active-active vs. active-passive clustering, load balancing, and tested recovery runbooks. You integrate security throughout the SDLC using SAST, DAST, IAST, RASP, and SCA tools, protect CI/CD pipelines from supply chain attack, and generate SBOMs to track transitive dependencies.

**Zero Trust** is the central architectural principle: never trust, always verify. You implement it through microsegmentation, ZTNA replacing VPN, and SASE combining networking and cloud security services. Policy Decision Points evaluate access; Policy Enforcement Points enforce it near the resource.

In the cloud, you apply the shared responsibility model, deploy CASB and CSPM for visibility, and secure containers and serverless workloads. You design PKI hierarchies with offline root CAs, intermediate CAs, and OCSP stapling for efficient revocation. Data security design combines classification, DLP, IRM, and Privacy by Design principles.

Key skills in this domain:

- Choose the right network topology (DMZ vs. screened subnet vs. air gap)
- Select active-active vs. active-passive based on availability and cost requirements
- Explain where SAST, DAST, IAST, RASP, and SCA fit in the pipeline
- Explain Zero Trust components: ZTNA, microsegmentation, SASE, PDP, PEP
- Distinguish RBAC, ABAC, MAC, and DAC and choose the right model for the scenario
- Explain OCSP stapling and why it outperforms CRL for revocation performance
- Apply data classification levels and DLP to control where sensitive data goes

-----

## Domain 3: Security Engineering (31%)

### [Security Engineering](/casp-plus/security-engineering/)

*This is the heaviest domain at 31%. Build deep hands-on familiarity — the exam includes performance-based questions asking you to read output and diagnose failures.*

Security Engineering implements what Architecture designed. You troubleshoot identity systems across SAML, OpenID Connect, Kerberos, PAM, and 802.1X — often tracing failures to clock skew, misconfigured certificates, or vault issues. PAM provides credential vaulting, just-in-time access, session recording, and dual control.

Endpoint hardening uses EDR, XDR, MDR, application control (allowlisting), SELinux/AppArmor/seccomp for MAC, and MDM for mobile. You identify attacker TTPs across the full MITRE ATT&CK lifecycle — initial access through exfiltration — and recognize indicators for credential dumping, lateral movement, and defense evasion.

Hardware roots of trust ground security in physical components: **TPM** stores keys and boot measurements; **HSM** performs high-volume crypto operations; **Secure Boot** validates bootloader signatures; **Measured Boot** records boot stages into TPM PCR registers for attestation. This chain of trust is unbreakable from software.

For specialized systems, you apply the **Purdue Model** to segment OT/ICS/SCADA environments and monitor passively. You automate at scale using PowerShell, Bash, Python, IaC, and SOAR playbooks. SCAP, OVAL, and XCCDF standardize configuration compliance checking.

Advanced cryptography covers the full landscape: symmetric vs. asymmetric, forward secrecy, key stretching, homomorphic encryption, and post-quantum standards. **ML-KEM** replaces Diffie-Hellman for key exchange; **ML-DSA** replaces ECDSA for signatures. Harvest-now-decrypt-later is the threat driving migration urgency.

Key skills in this domain:

- Diagnose SAML/Kerberos/MFA failures (clock skew is usually first)
- Distinguish TPM vs. HSM use cases
- Explain Secure Boot and Measured Boot chain of trust
- Recognize MITRE ATT&CK TTP categories and their indicators
- Match cryptographic primitives to use cases (Argon2 for passwords, AES-GCM for bulk, ML-KEM for PQC key exchange)
- Explain what SOAR automates and how it differs from a SIEM
- Apply SELinux as a MAC control that confines compromised processes

-----

## Domain 4: Security Operations (22%)

### [Security Operations](/casp-plus/security-operations/)

*Analyze evidence and recommend action. Don't just name tools — explain what the data tells you and what to do next.*

Security Operations turns telemetry into decisions. Your **SIEM** parses, normalizes, correlates, and baselines events from hundreds of sources. UEBA detects insider threats through statistical deviation. You run a vulnerability management program using CVSS scores combined with asset criticality — a CVSS 10.0 on an isolated system matters less than a CVSS 7.0 on internet-facing infrastructure.

Attack analysis covers injection, XSS, CSRF, SSRF, deserialization, race conditions, path traversal, and weak ciphers. You recommend mitigations that fix root causes: parameterized queries stop SQL injection, CSRF tokens stop CSRF, output encoding stops XSS. Secrets management keeps credentials out of code.

**Threat hunting** starts with a hypothesis and searches data proactively. Intel-based, anomaly-based, and adversary emulation approaches complement hypothesis-based hunts. Honeypots and honeytokens generate unambiguous attacker signals. Threat intelligence is shared in **STIX** (format) and **TAXII** (transport), with Sigma, YARA, and Snort for detection rules.

Incident response follows **PICERL**: Preparation, Identification, Containment, Eradication, Recovery, Lessons Learned. Containment always comes before eradication. Digital forensics follows the **order of volatility** — RAM before disk — and maintains chain of custody. Timeline reconstruction across memory, network, and disk artifacts reveals the attacker's path from entry to action.

Key skills in this domain:

- Explain SIEM tuning for alert fatigue reduction
- Apply CVSS with asset criticality for vulnerability prioritization
- Identify the root cause of each attack type (injection — lack of parameterized queries; XSS — missing output encoding)
- Distinguish hypothesis-based hunting from alert-driven response
- Explain STIX vs. TAXII roles
- Order forensic evidence collection correctly (RAM first)
- Follow PICERL and know that containment precedes eradication

-----

Work through all four domains, then validate your readiness with the [CompTIA SecurityX Practice Test](/casp-plus-practice-test/). *SecurityX is the new exam name; CASP+ is the legacy name. Some study resources still use CASP+ — both refer to the CAS-005 exam objectives.* For more certification courses and career playbooks, visit [Courses and Playbooks](/courses-and-playbooks/).
