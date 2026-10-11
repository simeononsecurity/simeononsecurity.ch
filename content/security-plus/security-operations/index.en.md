---
title: "CompTIA Security+ (SY0-701): Security Operations"
date: 2025-01-01
lastmod: 2026-10-10
toc: true
draft: false
description: "Triage synthetic SY0-701 access logs, set an asset baseline, restrict identities, track a vulnerability, and preserve incident evidence."
genre: ["CompTIA Security+ Course", "Security Operations", "Incident Response", "Identity Management", "Vulnerability Management", "Automation", "CompTIA Certification", "Information Security", "SIEM", "Cybersecurity"]
tags: ["CompTIA Security+", "SY0-701", "security operations", "secure baselines", "hardening", "vulnerability management", "SIEM", "IAM", "MFA", "EDR", "DLP", "automation", "SOAR", "incident response", "digital forensics"]
cover: "/img/cover/comptia-security-plus-sy0-701-security-operations.webp"
coverAlt: "A modern security operations center with diverse cybersecurity professionals monitoring multiple screens filled with data, graphs, and alerts in a high-tech environment."
coverCaption: "Master Security Operations for the SY0-701 Exam"
---

[Click Here to Return To the CompTIA Security+ Course Page](/security-plus-start/)

**Security Operations** is the largest domain on the **CompTIA Security+ (SY0-701)** exam at **28%**. This module covers the hands-on work of securing, monitoring, and responding day to day. *This domain carries the most exam weight, so study it thoroughly.*

This is where architecture meets practice. You harden systems, manage identities, watch for alerts, hunt vulnerabilities, and run the incident response process when something breaks.

## Hardening and Asset Management

A **secure baseline** is an approved configuration for a defined asset class. Establish separate baselines when systems have different roles, risks, or requirements, then review them as conditions change.

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

- **EDR** focuses on endpoint telemetry and response. **XDR** correlates signals across endpoints and other integrated sources.
- **Antivirus** detects or blocks supported malicious patterns, with gaps. **Host-based firewalls** filter local traffic according to rules.
- **DLP** detects or restricts selected data transfers when policy, coverage, and classification work.

Key management keeps cryptography trustworthy:

- **Key rotation** replaces keys on a schedule to limit exposure.
- **Key escrow** stores a copy for recovery.
- An **HSM** stores and processes keys in tamper-resistant hardware.

## Secure Protocols

You replace plaintext protocols with encrypted ones.

| Insecure | Secure replacement |
|----------|--------------------|
| HTTP | **HTTPS (TLS)** |
| FTP | **SFTP** uses SSH and a different protocol. FTPS is FTP protected by TLS. |
| Telnet | **SSH** |
| LDAP | **LDAP over TLS**, using StartTLS or a dedicated TLS listener with certificate validation. |
| DNS | **DNSSEC** authenticates DNS data. Use a separate encrypted DNS transport when confidentiality is required. |

Use **S/MIME** to sign and encrypt email. Verify file integrity with hashes, shown in [how to get hashes of files on Linux](/guides/how-to-get-hashes-of-files-on-linux/) and [in Windows](/guides/how-to-get-hashes-of-files-in-windows/).

## Vulnerability Management

You find weaknesses before attackers do.

- Identify with **scans**, **static and dynamic analysis**, threat feeds, and **penetration testing**.
- Use **CVSS** severity with asset exposure, exploitation evidence, business impact, and existing controls when prioritizing. Track applicable flaws by **CVE** number.
- Remediate, then **validate** the fix with a rescan.

Learn the configuration side in [Ansible for beginners](/articles/ansible-for-beginners/) for automated patching.

## Monitoring and Alerting

You watch the environment and react to signals.

- A **SIEM** aggregates logs and correlates events across systems.
- **NetFlow** and **SNMP traps** report network behavior.
- Tune alerts to cut false positives so real threats stand out.

```bash
# On a Linux host with this log path, inspect recent failed attempts
grep "Failed password" /var/log/auth.log | tail -n 20
```

## Automation and Orchestration

You automate repetitive work to respond faster and reduce error.

- **SOAR** runs playbooks that triage and contain incidents automatically.
- Scripts handle user provisioning, ticketing, and guard rails.
- *Automate the boring and dangerous tasks, then keep a human in the loop for decisions.*

## Incident Response and Forensics

You follow a repeatable process under pressure.

1. **Prepare** roles, tools, and communication paths.
2. **Detect and analyze** events before declaring an incident.
3. **Respond** through authorized containment and eradication decisions.
4. **Recover** services and validate the result.
5. **Improve** plans using recorded lessons.

This is a teaching sequence aligned with current NIST CSF 2.0 functions and NIST SP 800-61 Rev. 3. Match the exact SY0-701 objective wording when studying for the exam.

Digital forensics preserves evidence for investigation and possible legal use. Maintain a **chain of custody**, follow any applicable **legal hold**, and plan acquisition around volatility and incident needs. Document each transfer and action. Missing records weaken authentication and evidentiary weight, but admissibility depends on the jurisdiction and case.

## Practice: Triage a Synthetic Access Alert

Use these invented records. No live host or production account is needed.

```text
2026-10-10T09:01Z laptop-17 sshd Failed password for user archive from 192.0.2.40
2026-10-10T09:02Z laptop-17 sshd Failed password for user archive from 192.0.2.40
2026-10-10T09:04Z laptop-17 sshd Accepted publickey for user archive from 192.0.2.40
2026-10-10T09:06Z records-app export members.csv by archive, destination /tmp/out
```

The `192.0.2.0/24` block is reserved for examples. The log suggests a successful sign-in after two failures and a later export. It does not prove credential theft. In a worksheet, record host, account, source, time span, event sequence, and missing context. Ask the account owner and inspect approved maintenance records before declaring an incident. Preserve a copy of the original records, source, acquisition time, and SHA-256 digest. Restrict access to the copy.

Choose an initial decision. If the owner denies the activity or no approved change exists, escalate through the incident process and consider disabling the account under local policy. If the owner confirms authorized maintenance, document the evidence and close or continue monitoring. Do not automate account disabling from one synthetic alert.

Build a five-row operations board for this case: asset inventory entry, approved baseline, IAM rule, one vulnerability ticket, and backup status. For the vulnerability ticket, include affected version, evidence, severity with context, owner, due date, fix, and verification result. For the IAM rule, the `archive` role should read only the data needed for its job, with separate write or export approval. Mark a denied access test as unrun unless you perform it in a disposable lab.

Pass when your triage record separates observations from conclusions, identifies who receives an escalation, includes an evidence digest and custody notes, and shows a tracked fix with verification. The [NIST incident response guide](https://csrc.nist.gov/pubs/sp/800/61/r3/final) gives a response framework. Review the [CompTIA SY0-701 objectives](https://partners.comptia.org/docs/default-source/resources/comptia-security-sy0-701-exam-objectives-(4-0).pdf) for exam scope.

## Next Steps

Wrap the program with [Security Program Management and Oversight](/security-plus/security-program-management-oversight/), grounded in [General Security Concepts](/security-plus/general-security-concepts/) and [Security Architecture](/security-plus/security-architecture/). Return to the [CompTIA Security+ Course](/security-plus-start/).
