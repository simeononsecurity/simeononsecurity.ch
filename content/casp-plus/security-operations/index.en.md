---
title: "CompTIA SecurityX (CAS-005): Security Operations"
date: 2025-01-01
toc: true
draft: false
description: "Master security operations for the CompTIA SecurityX CAS-005 exam. Learn SIEM analysis, vulnerability management, attack analysis and mitigations, threat hunting, threat intelligence, incident response, and digital forensics."
genre: ["CompTIA SecurityX Course", "Security Operations", "Threat Hunting", "Threat Intelligence", "Incident Response", "Malware Analysis", "SIEM", "CASP+", "Enterprise Security", "Cybersecurity"]
tags: ["CompTIA SecurityX", "CASP+", "CAS-005", "security operations", "SIEM", "SOC", "threat hunting", "threat intelligence", "STIX", "TAXII", "YARA", "Sigma", "Snort", "malware analysis", "reverse engineering", "incident response", "digital forensics", "root cause analysis", "vulnerability management", "CVSS", "order of volatility", "PICERL", "chain of custody", "OSINT", "ISAC", "honeypot"]
cover: "/img/cover/comptia-securityx-cas-005-security-operations-monitoring-response.webp"
coverAlt: "An illustration of a high-tech security operations center with multiple monitors displaying security analytics. Silhouettes of professionals are engaged in monitoring activities in a dark setting with vibrant blue and green accents."
coverCaption: "Master Security Operations for the CAS-005 Exam"
---

#### [Click Here to Return To the CompTIA SecurityX Course Page](/casp-plus-start/)

**Security Operations** is **22%** of the **CompTIA SecurityX (CAS-005)** exam. This domain covers how you detect, hunt, analyze, and respond to threats using data, tooling, and threat intelligence. *SecurityX expects you to analyze evidence and recommend action, not just name a tool.*

Operations turns telemetry into decisions. You normalize logs into signal, hunt for what alerts missed, share intelligence in standard formats, and reconstruct what happened after a breach. Strong operational practice directly shortens attacker dwell time — every hour matters.

## Monitoring and Response

### SIEM Architecture and Usage

A **SIEM** (Security Information and Event Management) platform aggregates, normalizes, and correlates logs from across the environment.

| SIEM Capability | What it does |
|----------------|-------------|
| **Event parsing** | Normalizes log fields from heterogeneous sources into a common schema |
| **Correlation** | Matches patterns across multiple events; triggers alerts when thresholds are met |
| **Audit log reduction** | Filters high-volume noise events so analysts focus on meaningful data |
| **Behavior baselines** | Establishes normal patterns so anomalies — unusual login hours, rare processes — stand out |
| **UEBA** | User and Entity Behavior Analytics; detects insider threats through statistical deviation |

A well-tuned SIEM reduces alert volume through aggregation, enrichment, and threshold tuning. Poorly tuned SIEMs generate thousands of false positives per day, causing alert fatigue.

### SOC Tiers and Models

| Model | Description |
|-------|-------------|
| **In-house SOC** | Full internal team; highest control, requires investment in staff and tooling |
| **MSSP** | Managed Security Service Provider monitors on your behalf; faster to stand up |
| **Hybrid** | Internal team handles Tier 2 and 3 escalations; MSSP handles Tier 1 triage |
| **MDR** | Managed Detection and Response — combines EDR tooling with SOC service |

```bash
# Surface the top source IPs hitting a web server log during initial triage
awk '{print $1}' /var/log/nginx/access.log | sort | uniq -c | sort -rn | head -20

# Find failed SSH login attempts in auth.log
grep "Failed password" /var/log/auth.log | awk '{print $11}' | sort | uniq -c | sort -rn | head -10
```

## Vulnerability Management

You run a continuous vulnerability management program to systematically find, prioritize, and remediate weaknesses.

| Phase | Activity |
|-------|---------|
| **Discover** | Scan with Nessus, Qualys, or OpenVAS to identify assets and vulnerabilities |
| **Prioritize** | Use CVSS base score, exploit availability (EPSS), and asset criticality |
| **Remediate** | Patch, reconfigure, isolate, or accept risk with documented justification |
| **Verify** | Re-scan to confirm the fix applied correctly |
| **Report** | Track SLA compliance and trend vulnerability counts over time |

### CVSS Scoring

**CVSS** (Common Vulnerability Scoring System) v3.1 scores vulnerabilities 0.0–10.0:

- **Base score** — intrinsic characteristics: attack vector, attack complexity, privileges required, user interaction, CIA impact.
- **Temporal score** — adds exploit maturity and remediation status.
- **Environmental score** — adjusts for your specific environment and asset value.

*The exam tests CVSS as a prioritization tool. A CVSS 10.0 on an isolated internal server matters less than a CVSS 7.0 on internet-facing infrastructure. Always combine CVSS with asset criticality.*

## Analyzing Vulnerabilities and Attacks

You recognize attacks by mechanism so you can recommend the right mitigation.

| Attack | Mechanism | Root cause |
|--------|-----------|------------|
| **SQL injection** | Attacker input runs as SQL query | Lack of parameterized queries |
| **Command injection** | Input passed unsanitized to a shell | Lack of input validation |
| **XSS (stored)** | Malicious script saved and rendered to other users | Missing output encoding |
| **XSS (reflected)** | Script reflected from server in response | Missing output encoding |
| **CSRF** | Forged request sent using victim's authenticated session | Missing CSRF token |
| **SSRF** | Server-side request to attacker-specified URL | No URL allowlist on server-side fetch |
| **Deserialization** | Crafted serialized data triggers code execution on deserialize | No type checking, no class allowlist |
| **Race condition (TOCTOU)** | State changes between a check and its use | Non-atomic operations on shared resources |
| **Weak cipher** | Outdated algorithm broken by modern attacks | TLS config allows RC4, 3DES, or export ciphers |
| **Path traversal** | `../` sequences read files outside the web root | Missing path canonicalization |

## Applying Mitigations

You fix root causes. Controls that treat symptoms leave the underlying vulnerability exploitable through a different path.

- **Input validation** rejects malformed input at ingestion. Drives SQL injection and command injection prevention.
- **Output encoding** neutralizes data before rendering. Stops stored and reflected XSS.
- **Parameterized queries / prepared statements** prevent SQL injection by separating code from data.
- **CSRF tokens** verify that a state-changing request originated from the legitimate UI.
- **Least privilege** limits the blast radius of any compromised component.
- **Secrets management** keeps API keys and credentials in a vault (HashiCorp Vault, AWS Secrets Manager), not in code.
- **Defense in depth** layers controls so no single failure produces a breach.

## Threat Hunting and Threat Intelligence

### Threat Hunting

Threat hunting is proactive: you search for attackers who are already present but have not triggered alerts. Every hunt starts with a **hypothesis**.

| Hunting approach | How it works |
|-----------------|-------------|
| **Hypothesis-based** | Pose a theory ("attackers are using scheduled tasks for persistence"), then search for evidence |
| **Intel-based** | Start from a known TTP or IOC from threat intelligence, search for its artifacts in your data |
| **Anomaly-based** | Baseline normal behavior, then surface statistical outliers |
| **Adversary emulation** | Simulate a real threat actor's TTPs to test detection coverage |

**Honeypots** and **honeytokens** lure attackers by presenting convincing fake assets. Any access to a honeypot is an unambiguous signal — legitimate users have no reason to touch it. For a practical passive detection approach, see the [ESP32 Wi-Fi canary project](/articles/esp32-wifi-canary-passive-wifi-threat-detection-2026/).

### Threat Intelligence Sources

| Source | Type | Examples |
|--------|------|---------|
| **OSINT** | Open-source | Shodan, VirusTotal, WHOIS, social media |
| **Dark web monitoring** | Closed-source | Ransomware leak sites, criminal forums |
| **ISAC** | Sector-specific sharing | FS-ISAC (financial), H-ISAC (healthcare), E-ISAC (energy) |
| **Commercial TI feeds** | Vendor-curated | Recorded Future, Mandiant, CrowdStrike Intel |
| **Internal telemetry** | First-party | Your own SIEM, EDR, and network flows |

### Intelligence Lifecycle

Good threat intelligence follows a cycle: direction, collection, processing, analysis, dissemination, feedback. The exam tests whether you can identify which phase a described activity belongs to.

## Sharing Indicators of Compromise

You share IOCs in standard formats so automation and partner organizations can act on them immediately.

| Standard | Role | Format |
|----------|------|--------|
| **STIX 2.1** | Structured language to describe threat objects, relationships, and campaigns | JSON |
| **TAXII 2.1** | API-based transport protocol for distributing STIX bundles | REST/HTTPS |
| **Sigma** | Generic log-based detection rule format convertible to any SIEM | YAML |
| **YARA** | Pattern matching to identify malware files and processes by strings or byte patterns | Custom |
| **Snort / Suricata** | Network intrusion detection signatures | Rule-based |

*STIX describes the intelligence; TAXII moves it. Both appear on the exam together.*

## Incident Response

### The PICERL Phases

CompTIA uses the **PICERL** model for incident response:

| Phase | Key activity |
|-------|-------------|
| **Preparation** | Build playbooks, train team, deploy tooling before an incident occurs |
| **Identification** | Detect and confirm that an incident is occurring |
| **Containment** | Isolate affected systems to stop spread while preserving evidence |
| **Eradication** | Remove malware, close the vulnerability, and remove persistence mechanisms |
| **Recovery** | Restore systems to production from clean backups; validate operations |
| **Lessons Learned** | Post-incident review; update playbooks and controls |

*Containment comes before eradication. You must stop the bleeding before you treat the wound.*

### Containment Strategies

| Strategy | When to use |
|----------|------------|
| **Network isolation** | Cut the host from the network to stop lateral movement |
| **Forensic image before wipe** | Preserve evidence when legal or compliance requirements exist |
| **Credential rotation** | Rotate all credentials that may have been exposed |
| **Emergency patching** | Patch the exploited vulnerability immediately if exploiting continues |

## Digital Forensics

### Order of Volatility

Evidence must be collected from most volatile to least volatile to maximize what you capture.

| Order | Data type | How to collect |
|-------|-----------|---------------|
| 1 | CPU registers, cache | Memory acquisition tool (Volatility/LiME) |
| 2 | RAM contents | Live memory dump |
| 3 | Network connections, ARP table | `netstat`, `ss`, `arp -a` |
| 4 | Running processes | `ps`, `tasklist`, process tree |
| 5 | Open files / handles | `lsof`, `handle` |
| 6 | File system (disk) | Forensic image (dd, FTK Imager) |
| 7 | Logs and config | Copy log files; preserve timestamps |
| 8 | Archived / remote logs | SIEM export, cloud log archive |

*An analyst who reboots before capturing memory loses everything above line 5. Order of volatility is a tested concept.*

### Forensic Analysis Techniques

- **Malware analysis (dynamic)** runs samples in a sandbox (Any.run, Cuckoo) to observe file writes, network connections, and process behavior.
- **Malware analysis (static)** disassembles or decompiles code to understand logic without executing it. Uses IDA Pro, Ghidra, or strings analysis.
- **Volatile storage analysis** examines RAM for injected code, decrypted strings, network sockets, and running processes.
- **Non-volatile storage analysis** examines disk images for persistence mechanisms, deleted files, browser history, and registry hives.
- **Metadata analysis** reads file creation times, last-modified timestamps, author fields, and GPS coordinates embedded in images.

Verify file integrity before and after handling using hash comparison:

```bash
# Capture a disk image and immediately record its hash
dd if=/dev/sdb bs=4M | tee sdb_evidence.img | sha256sum > sdb_evidence.sha256
```

For more on file hashing in Linux, see [how to get hashes of files on Linux](/guides/how-to-get-hashes-of-files-on-linux/).

### Chain of Custody

Every piece of evidence needs a documented chain of custody — who collected it, when, how it was stored, and who had access. A broken chain makes evidence inadmissible. You use write blockers when imaging disks so the act of copying cannot alter timestamps.

## Timeline Reconstruction and Root Cause Analysis

A **timeline** orders every event across all data sources — logs, memory artifacts, network flows, disk timestamps — so you see the attacker's path from entry to action. Tools like Plaso (log2timeline) automate timeline construction from multiple artifact types.

**Root cause analysis** finds the underlying failure that allowed the incident. Common root causes include:

- Unpatched vulnerability exploited via phishing.
- Misconfigured access control granting excessive privilege.
- Credential reuse from a third-party breach.
- Supply chain compromise in a software update.

A post-incident writeup that only documents symptoms rather than root cause leaves the same door open for the next attacker.

## Operations Exam Tips

- Order of volatility: collect RAM before disk, network state before file system. Any question about what to capture first should trigger this knowledge.
- PICERL: containment comes before eradication. Never eradicate without first containing.
- STIX describes intelligence; TAXII transports it.
- CVSS score alone is not enough for prioritization — always factor in asset criticality and exploit availability.
- Hypothesis-based hunting: you start with a theory, then search. This distinguishes hunting from alert-response.
- Chain of custody is required for legal admissibility. A broken chain is a failed investigation.

## Next Steps

You have now covered all four SecurityX domains. Test your readiness with the [CompTIA SecurityX Practice Test](/casp-plus-practice-test/), then return to review weak areas:

- [Governance, Risk, and Compliance](/casp-plus/governance-risk-compliance/) — for frameworks, risk math, and threat modeling
- [Security Architecture](/casp-plus/security-architecture/) — for Zero Trust, cloud design, and resilient systems
- [Security Engineering](/casp-plus/security-engineering/) — for cryptography, hardware roots of trust, and IAM

Review [tips for passing CompTIA exams](/articles/tips-and-tricks-for-passing-comptia-exams/) before exam day, and explore more courses at [Courses and Playbooks](/courses-and-playbooks/).
