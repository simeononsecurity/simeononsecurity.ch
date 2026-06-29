---
title: "ISC2 CISSP: Security Operations"
date: 2025-01-01
toc: true
draft: false
description: "Master Security Operations for the ISC2 CISSP exam. Learn investigations, logging and monitoring, configuration management, incident management, recovery, disaster recovery, and physical security."
genre: ["ISC2 CISSP Course", "Security Operations", "Incident Management", "Disaster Recovery", "Digital Forensics", "ISC2 Certification", "Information Security", "Business Continuity", "Monitoring", "Cybersecurity"]
tags: ["ISC2 CISSP", "CISSP", "security operations", "investigations", "digital forensics", "SIEM", "UEBA", "incident management", "disaster recovery", "business continuity", "physical security", "configuration management"]
cover: "/img/cover/isc2-cissp-security-operations-monitoring-incident-management.webp"
coverAlt: "A futuristic control room with a cybersecurity professional analyzing multiple screens showing data, logs, and monitoring dashboards against a dark background with vibrant colors."
coverCaption: "Master Security Operations for the CISSP Exam"
---

#### [Click Here to Return To the ISC2 CISSP Course Page](/cissp-start/)

**Security Operations** is **13%** of the **ISC2 CISSP** exam. This module covers the daily work of running security: monitoring systems, handling incidents, recovering from disaster, and keeping the business running. *This is the operational heart of the security program, where policy meets practice.*

Operations is where security lives or dies. A perfect architecture means nothing if nobody watches the logs, responds to alerts, or tests the backups. This domain teaches you to run security as an ongoing discipline, not a one-time project.

## Investigations and Digital Forensics

You conduct investigations to understand what happened and to support legal action.

**Evidence handling** follows a strict **chain of custody** so evidence holds up in court. You document who collected each item, when, where, and every transfer. A break in the chain makes evidence inadmissible.

You collect evidence in **order of volatility**, capturing the most fragile data first:

1. CPU registers and cache
2. RAM and running processes
3. Network connections and ARP cache
4. Disk and swap files
5. Logs and archived media

Investigation types differ by their standard of proof:

| Type | Standard of proof | Goal |
|------|-------------------|------|
| **Administrative** | Lowest | Internal policy and HR matters |
| **Civil** | Preponderance of evidence | Disputes between parties |
| **Criminal** | Beyond a reasonable doubt | Prosecution by the state |
| **Regulatory** | Varies by regulator | Compliance enforcement |

## Logging and Monitoring

You watch systems continuously so you detect threats before they cause harm.

- **SIEM** (Security Information and Event Management) collects logs from across the environment, correlates them, and alerts on suspicious patterns.
- **Continuous monitoring** keeps watch on controls and configurations in real time.
- **Egress monitoring** inspects outbound traffic to catch data exfiltration and command-and-control.
- **Threat intelligence** feeds known indicators into your detection so you spot known-bad activity.
- **UEBA** (User and Entity Behavior Analytics) baselines normal behavior and flags anomalies, like a user downloading gigabytes at 3 a.m.

```bash
# Tail authentication logs for failed logins during an investigation
grep "Failed password" /var/log/auth.log | tail -n 20

# Watch active network connections for unexpected outbound traffic
ss -tunp | grep ESTAB
```

You connect monitoring back to the testing in [Security Assessment and Testing](/cissp/security-assessment-and-testing/), where log reviews confirm your monitoring captures what you need.

## Configuration Management

You control how systems are built and changed so they stay secure and consistent.

- **Provisioning** deploys systems from a known-good template.
- **Baselining** defines a secure standard configuration every system must meet.
- **Automation** enforces the baseline at scale so manual drift cannot creep in. Tools like Ansible keep systems in their desired state, as covered in [Ansible for beginners](/articles/ansible-for-beginners/).

## Foundational Operations Concepts

These principles limit what any one person can do and reduce insider risk.

| Concept | What it does |
|---------|--------------|
| **Need-to-know** | Access only the data required for a task |
| **Least privilege** | The minimum rights to do the job |
| **Separation of duties (SoD)** | Split critical tasks so no one person controls a whole process |
| **Privileged account management** | Tightly control and monitor admin accounts |
| **Job rotation** | Move people through roles to detect fraud |
| **Mandatory vacation** | Force time off so hidden fraud surfaces |

## Incident Management

You follow a repeatable lifecycle for every incident so response is fast and consistent.

1. **Detection** identifies a possible incident from alerts or reports.
2. **Response** activates the team and contains the initial damage.
3. **Mitigation** stops the incident from spreading further.
4. **Reporting** notifies stakeholders, regulators, and law enforcement as required.
5. **Recovery** restores affected systems to normal operation.
6. **Remediation** removes the root cause so it cannot happen again.
7. **Lessons learned** reviews the incident to improve the process.

## Detection and Preventative Measures

You operate layered defenses that detect and block threats.

- **Firewalls** filter traffic by rules at network boundaries.
- **IDS/IPS** detect (IDS) or detect and block (IPS) malicious traffic.
- **Sandboxing** runs untrusted code in isolation to study its behavior safely.
- **Honeypots** are decoy systems that lure and study attackers.
- **Anti-malware** blocks known and behavior-based threats on endpoints.
- **AI-based tools** detect novel threats by learning normal behavior, a fast-moving area covered in [the state of AI in cybersecurity](/articles/state-of-ai-cybersecurity-2026/).

## Recovery, Disaster Recovery, and Continuity

You plan for failure so the business survives it. Two metrics drive every recovery decision:

| Metric | Defines |
|--------|---------|
| **RTO** (Recovery Time Objective) | How fast you must restore a system |
| **RPO** (Recovery Point Objective) | How much data you can afford to lose |

You choose a **recovery site** based on cost and speed:

| Site type | Ready in | Cost |
|-----------|----------|------|
| **Hot site** | Minutes to hours | Highest |
| **Warm site** | Hours to days | Medium |
| **Cold site** | Days to weeks | Lowest |

**Backup strategies** balance speed and storage. A full backup is complete but slow. Incremental backups are fast but slower to restore. The **3-2-1 rule** keeps three copies on two media types with one offsite.

You test **Business Continuity (BC)** plans with increasing realism:

1. **Read-through** of the plan on paper
2. **Tabletop** discussion of a scenario
3. **Walkthrough** step by step
4. **Simulation** of a realistic event
5. **Parallel** test running the backup site alongside production
6. **Full interruption** that fails over completely, the most thorough and most disruptive

## Physical Security and Personnel Safety

You protect facilities and people because *human life always takes priority over assets*. You use access controls, cameras, lighting, and guards, and you plan for evacuation and safety. You also watch for **insider threats**, using behavior analytics and separation of duties to catch malicious or careless employees.

## Next Steps

Finish the course with [Software Development Security](/cissp/software-development-security/), then ground operations in [Security and Risk Management](/cissp/security-and-risk-management/) and verify controls with [Security Assessment and Testing](/cissp/security-assessment-and-testing/). Return to the [ISC2 CISSP Course](/cissp-start/).
