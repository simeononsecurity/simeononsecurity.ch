---
title: "CompTIA SecOT+ (SOT-001): OT Security Operations"
date: 2025-01-01
toc: true
draft: false
description: "Master OT security operations for the CompTIA SecOT+ SOT-001 exam. Learn asset inventory and discovery, data collection with SIEM and SOAR, baselining and threat hunting, vulnerability management, patching with compensating controls, and removable media security."
genre: ["CompTIA SecOT+ Course", "OT Security Operations", "Asset Inventory", "SIEM", "Vulnerability Management", "Threat Hunting", "Patch Management", "Operational Technology", "SOT-001", "Cybersecurity"]
tags: ["CompTIA SecOT+", "SOT-001", "asset inventory", "passive discovery", "active discovery", "configuration management database", "SIEM", "SOAR", "baselining", "threat hunting", "patch management", "compensating control", "software bill of materials", "vulnerability triage", "removable media scanning", "write blocker", "sanitization kiosk"]
cover: "/img/cover/comptia-secot-ot-security-operations-control-room.webp"
coverAlt: "A high-tech control room showing professionals analyzing network traffic and asset inventories on multiple screens, with a dark navy background and vibrant blue and green accents."
coverCaption: "Run Day-to-Day OT Security Operations for the SOT-001 Exam"
---

#### [Click Here to Return To the CompTIA SecOT+ Course Page](/secot-plus-start/)

**OT Security Operations** is **22%** of the **CompTIA SecOT+ (SOT-001)** exam, making it the most heavily weighted domain. This is the daily work of keeping an OT environment secure. You discover and track assets, collect and analyze data, hunt for threats, and manage vulnerabilities in systems you often cannot simply patch. *Spend the most study time here. Visibility is the foundation, because you cannot protect an asset you do not know exists.*

OT operations differ from IT operations because uptime and safety constrain everything. You cannot reboot a turbine to apply a patch, so you lean on compensating controls and carefully scheduled downtime.

## Asset Inventory and Discovery

You cannot secure what you cannot see, so inventory comes first.

| Method | How it works |
|--------|-------------|
| **Passive discovery** | Identifies assets by observing network traffic without probing |
| **Active discovery** | Identifies assets by querying or scanning them |
| **Manual discovery** | Identifies assets through physical inspection and records |

A **configuration management database** stores asset configuration details and relationships, a **software inventory** records installed software, and each **asset attribute** captures a property such as IP, model, location, or owner.

*Prefer passive discovery in OT. Active scanning can disrupt fragile devices, so you watch traffic rather than probe whenever possible.*

## Data Collection and Analysis

You gather the data that reveals what is happening.

- A **packet capture** records network traffic for analysis.
- **Syslog** forwards and stores log messages.
- A **process log** records control system events and values.
- A **historian** holds time-series process data.
- **Security information and event management (SIEM)** aggregates and correlates security logs.
- **Security orchestration, automation, and response (SOAR)** automates security workflows.
- A **collection management framework** documents what data is collected, from where, and how.

## Detection

You turn collected data into detections.

- **Baselining** establishes normal behavior so deviations stand out.
- **Threat hunting** proactively searches for undetected threats.
- **IDS rule tuning** adjusts detection rules to reduce false positives.

## Vulnerability Management

You find weaknesses and prioritize them by real exposure.

| Concept | Meaning |
|---------|---------|
| **Vulnerability triage** | Prioritizes by exposure, severity, and impact |
| **Exposure** | How reachable an asset is by a threat |
| **Exploitability** | How easily a vulnerability can be used |
| **Software bill of materials** | Lists the components inside a piece of software |
| **National Vulnerability Database** | A repository of known vulnerabilities |
| **Remediation verification** | Confirms a fix actually resolved the issue |

You detect vulnerabilities through **passive**, **active**, and **derived detection**, choosing the least disruptive method for the asset.

## Patching and Compensating Controls

Patching OT is hard, so you often reach for alternatives.

- **Patch management** acquires, tests, and applies updates.
- A **mitigating control** reduces the impact of a vulnerability when patching is not possible.
- A **compensating control** substitutes for an impractical primary control.
- **Version management** tracks software and firmware versions.
- **Scheduling planned downtime** arranges maintenance windows to apply changes safely.
- **Spare availability** keeps backup hardware on hand to support remediation.

*When you cannot patch a vulnerable PLC, you wrap it in compensating controls such as tighter segmentation and monitoring. The risk is reduced even though the flaw remains.*

## Media and Field Device Security

Removable media and portable tools are a major OT threat vector, so you control them tightly.

- **Removable media scanning** checks portable storage for malware before use.
- A **sanitization kiosk** scans and cleans removable media at a dedicated station.
- A **write blocker** prevents writing to storage to preserve evidence.
- **Media destruction** securely destroys storage so its data cannot be recovered.
- **Calibration equipment** and **mobile device security** protect the portable tools and devices used in the field.
- A **security posture check** validates that a device meets requirements before it connects.

## Next Steps

With operations running, continue to [OT Incident Management](/secot-plus/ot-incident-management/) to prepare for when prevention fails. Return anytime to the [CompTIA SecOT+ Course](/secot-plus-start/).
