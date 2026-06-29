---
title: "CompTIA Security+ (SY0-701): Security Operations"
date: 2025-01-01
toc: true
draft: false
description: "Master security operations for the CompTIA Security+ SY0-701 exam. Learn secure baselines, asset management, vulnerability management, monitoring, IAM, automation, and incident response."
genre: ["CompTIA Security+ Course", "Security Operations", "Incident Response", "Identity Management", "Vulnerability Management", "Automation", "CompTIA Certification", "Information Security", "SIEM", "Cybersecurity"]
tags: ["CompTIA Security+", "SY0-701", "security operations", "secure baselines", "hardening", "vulnerability management", "SIEM", "IAM", "MFA", "EDR", "DLP", "automation", "SOAR", "incident response", "digital forensics"]
cover: "/img/cover/comptia-security-plus-sy0-701-security-operations.webp"
coverAlt: "A modern security operations center with diverse cybersecurity professionals monitoring multiple screens filled with data, graphs, and alerts in a high-tech environment."
coverCaption: "Master Security Operations for the SY0-701 Exam"
---

#### [Click Here to Return To the CompTIA Security+ Course Page](/security-plus-start/)

**Security Operations** is the largest domain on the **CompTIA Security+ (SY0-701)** exam at **28%**. This module covers the hands-on work of securing, monitoring, and responding day to day. *This domain carries the most exam weight, so study it thoroughly.*

This is where architecture meets practice. You harden systems, manage identities, watch for alerts, hunt vulnerabilities, and run the incident response process when something breaks.

## Hardening and Asset Management

A **secure baseline** is a known-good configuration you apply to every system. You establish it, deploy it, and maintain it as threats change.

- Harden by removing default accounts, closing unused ports, and disabling unneeded services.
- Apply hardening to **mobile devices**, **workstations**, **servers**, **cloud infrastructure**, and **IoT**.
- Use **secure configuration guides** like CIS Benchmarks and DISA STIGs.

Asset management tracks gear through its life:

| Phase | Action |
|-------|--------|
| **Acquisition** | Approve and inventory new assets |
| **Assignment** | Assign an owner and classification |
| **Monitoring** | Track location and patch status |
| **Disposal** | Sanitize media and destroy data |

*You cannot protect an asset you do not know you own.*

## Identity and Access Management

You control who gets access and how much.

| Model | How access is granted |
|-------|-----------------------|
| **RBAC** | By job role |
| **ABAC** | By attributes (location, device, time) |
| **MAC** | By labels set by the system |
| **DAC** | By the data owner |

Apply **least privilege** so users get only what they need. Use **provisioning** and **deprovisioning** to add and remove access quickly. Strengthen logins with **MFA**, **SSO**, and **federation**. Strong passwords stay the baseline, covered in [how to create strong passwords](/articles/how-to-create-strong-passwords/).

## Endpoint Security and Key Management

You defend the endpoint and protect the keys.

- **EDR** and **XDR** detect and respond to threats on hosts.
- **Antivirus** blocks known malware, and **host-based firewalls** filter local traffic.
- **DLP** stops sensitive data from leaving the environment.

Key management keeps cryptography trustworthy:

- **Key rotation** replaces keys on a schedule to limit exposure.
- **Key escrow** stores a copy for recovery.
- An **HSM** stores and processes keys in tamper-resistant hardware.

## Secure Protocols

You replace plaintext protocols with encrypted ones.

| Insecure | Secure replacement |
|----------|--------------------|
| HTTP | **HTTPS (TLS)** |
| FTP | **SFTP** |
| Telnet | **SSH** |
| LDAP | **LDAPS** |
| DNS | **DNSSEC** |

Use **S/MIME** to sign and encrypt email. Verify file integrity with hashes, shown in [how to get hashes of files on Linux](/guides/how-to-get-hashes-of-files-on-linux/) and [in Windows](/guides/how-to-get-hashes-of-files-in-windows/).

## Vulnerability Management

You find weaknesses before attackers do.

- Identify with **scans**, **static and dynamic analysis**, threat feeds, and **penetration testing**.
- Prioritize with **CVSS** scores and track flaws by **CVE** number.
- Remediate, then **validate** the fix with a rescan.

Learn the configuration side in [Ansible for beginners](/articles/ansible-for-beginners/) for automated patching.

## Monitoring and Alerting

You watch the environment and react to signals.

- A **SIEM** aggregates logs and correlates events across systems.
- **NetFlow** and **SNMP traps** report network behavior.
- Tune alerts to cut false positives so real threats stand out.

```bash
# Watch authentication failures on a Linux host
grep "Failed password" /var/log/auth.log | tail -n 20
```

## Automation and Orchestration

You automate repetitive work to respond faster and reduce error.

- **SOAR** runs playbooks that triage and contain incidents automatically.
- Scripts handle user provisioning, ticketing, and guard rails.
- *Automate the boring and dangerous tasks, then keep a human in the loop for decisions.*

## Incident Response and Forensics

You follow a repeatable process under pressure.

1. **Preparation** builds plans, tools, and training.
2. **Identification** confirms an incident occurred.
3. **Containment** limits the spread.
4. **Eradication** removes the cause.
5. **Recovery** restores normal operations.
6. **Lessons learned** improves the next response.

Digital forensics preserves evidence for legal use. Maintain a **chain of custody**, apply a **legal hold**, and acquire data in order of volatility (memory first, disk later). *Document every step, because untracked evidence is inadmissible.*

## Next Steps

Wrap the program with [Security Program Management and Oversight](/security-plus/security-program-management-oversight/), grounded in [General Security Concepts](/security-plus/general-security-concepts/) and [Security Architecture](/security-plus/security-architecture/). Return to the [CompTIA Security+ Course](/security-plus-start/).
