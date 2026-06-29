---
title: "CompTIA CySA+ (CS0-003): Security Operations and Threat Intelligence"
date: 2025-01-01
toc: true
draft: false
description: "Master security operations and threat intelligence for the CompTIA CySA+ CS0-003 exam. Learn the SOC, threat intelligence, MITRE ATT&CK, log analysis, SIEM tuning, traffic analysis, and threat hunting."
genre: ["CompTIA CySA+ Course", "Security Operations", "Threat Intelligence", "SIEM", "Threat Hunting", "SOC Analyst", "Log Analysis", "MITRE ATT&CK", "Cybersecurity Analyst", "Network Security"]
tags: ["CompTIA CySA+", "CS0-003", "security operations", "threat intelligence", "MITRE ATT&CK", "Diamond Model", "cyber kill chain", "SIEM", "log analysis", "threat hunting", "EDR", "STIX", "TAXII", "SOC", "network traffic analysis"]
cover: "/img/cover/security-operations-center-soc-cybersecurity-illustration.webp"
coverAlt: "A Security Operations Center with multiple analysts working at desks, monitoring screens filled with colorful graphs and alerts against a dark background."
coverCaption: "Master Security Operations for the CS0-003 Exam"
---

#### [Click Here to Return To the CompTIA CySA+ Course Page](/cysa-plus-start/)

**Security Operations** is the largest domain on the **CompTIA CySA+ (CS0-003)** exam at **33%**. This module teaches how a **Security Operations Center (SOC)** detects threats through intelligence, log analysis, SIEM tuning, traffic analysis, and proactive hunting. *This is the daily work of a cybersecurity analyst, so learn the workflow, not only the terms.*

## The SOC and the Alert Lifecycle

A **SOC** monitors and responds around the clock. Analysts work in tiers:

- **Tier 1** triages alerts and escalates real incidents
- **Tier 2** investigates and contains
- **Tier 3** hunts, reverse-engineers, and tunes detections

An alert moves through a lifecycle: **generation, triage, investigation, escalation or closure**. *Most alerts are false positives, so your triage skill decides how much real work reaches Tier 2.*

## Threat Intelligence

**Threat intelligence** turns raw data into context you act on.

- **Indicators of compromise (IoCs)** are artifacts left behind: malicious IPs, file hashes, domains, registry keys
- **Indicators of attack (IoAs)** describe behavior in progress, such as a process spawning PowerShell that downloads a payload
- Intelligence comes in three levels: **tactical** (IoCs for detection), **operational** (campaigns and TTPs), and **strategic** (business risk for leadership)

You share intelligence in standard formats: **STIX** structures the data and **TAXII** transports it between organizations.

## Threat Actors and TTPs

Know who attacks and how:

- **Nation-states** pursue espionage with patience and resources
- **Organized crime** chases money through ransomware and fraud
- **Hacktivists** disrupt for a cause
- **Insiders** abuse legitimate access

Their **tactics, techniques, and procedures (TTPs)** are more durable than IoCs. An attacker changes IP addresses easily but rarely changes their core technique.

## Frameworks: ATT&CK, Diamond, Kill Chain

Three models map adversary behavior, and they complement each other.

- **MITRE ATT&CK** is a matrix of real-world tactics and techniques. Each technique has an ID, for example **T1059** (Command and Scripting Interpreter) and **T1566** (Phishing). You map alerts to technique IDs to measure coverage.
- The **Cyber Kill Chain** breaks an attack into seven sequential phases from reconnaissance to actions on objectives.
- The **Diamond Model** links four vertices: adversary, capability, infrastructure, and victim.

*Use the kill chain to describe stages, ATT&CK to describe specific techniques, and the Diamond Model to pivot between related intrusions.*

## Log Analysis

You correlate evidence across many sources. Learn what each log tells you:

| Source | What you look for |
|--------|-------------------|
| Endpoint/EDR | Process creation, parent-child chains, persistence |
| Firewall | Allowed and denied connections, port scans |
| DNS | Lookups to known-bad or newly registered domains |
| Proxy/web | Downloads, command-and-control beacons |
| Authentication | Failed logins, impossible travel, off-hours access |

A suspicious Windows event chain looks like this:

```
4688  New process: powershell.exe  parent: winword.exe
      CommandLine: powershell -enc SQBFAFgA...
```

*Word spawning an encoded PowerShell command is a classic macro-based attack, which maps to ATT&CK T1059.001.*

## SIEM: Correlation and Tuning

A **SIEM** aggregates logs, **normalizes** them into common fields, and **correlates** events into alerts.

A correlation rule in plain terms:

```
IF failed_logins > 10 from one source IN 1 minute
   FOLLOWED BY a successful login from that source
THEN raise "possible brute force success"
```

A Splunk-style query that finds the same pattern:

```
index=auth action=failure | stats count by src_ip | where count > 10
```

**Alert tuning** removes noise. You suppress known-good sources, adjust thresholds, and add context so analysts trust the queue. *An untuned SIEM buries real incidents under thousands of false positives.*

## Network Traffic Analysis

Inspect traffic to find what logs miss:

- **Wireshark** and **tcpdump** capture and decode packets
- **Zeek** turns traffic into rich connection logs
- **NetFlow** summarizes who talked to whom, how much, and when

Look for **beaconing** (regular small connections to one host), large outbound transfers, and connections to newly registered domains.

```bash
sudo tcpdump -n -i eth0 'tcp port 443 and host 203.0.113.10'
```

## EDR and Endpoint Analysis

**Endpoint detection and response (EDR)** records process trees, network connections, and file changes. You trace an alert backward to the initial access and forward to lateral movement. Watch for **living-off-the-land** tools such as `certutil`, `rundll32`, and `wmic` used in unusual ways.

## Email and Phishing Triage

Most intrusions start with email. Read the **headers** to trace the true sender and check authentication:

- **SPF** confirms the sending server is authorized
- **DKIM** signs the message so tampering shows
- **DMARC** tells receivers what to do when SPF or DKIM fails

*A failed DMARC result on a message claiming to be from your CEO is a strong phishing signal.*

## Threat Hunting

Hunting is proactive. You start with a **hypothesis**, not an alert:

> "If an attacker used a scheduled task for persistence, I will find unusual task creation events in the last 30 days."

You then query telemetry, compare against a **baseline**, and investigate deviations. Hunting finds the threats that slipped past automated detection.

## Cloud Monitoring and Automation

Cloud platforms log control-plane actions (CloudTrail-style logs) you review for risky API calls and new IAM grants. **Cloud security posture management (CSPM)** flags misconfigurations such as public storage buckets. Automate repetitive triage with scripts and SOAR playbooks so analysts spend time on judgment, not copy-paste.

## Next Steps

Detection feeds straight into [Vulnerability Management](/cysa-plus/vulnerability-management/) and [Incident Response](/cysa-plus/incident-response-management/). Communicate what you find using [Reporting and Communication](/cysa-plus/reporting-and-communication/). Return to the [CompTIA CySA+ Course](/cysa-plus-start/).
