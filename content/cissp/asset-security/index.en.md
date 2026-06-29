---
title: "ISC2 CISSP: Asset Security"
date: 2025-01-01
toc: true
draft: false
description: "Master Asset Security for the ISC2 CISSP exam. Learn information classification, data roles, the data lifecycle, asset retention, data security controls, and data protection methods."
genre: ["ISC2 CISSP Course", "Asset Security", "Data Classification", "Data Protection", "Data Lifecycle", "ISC2 Certification", "Information Security", "Data Governance", "Privacy", "Cybersecurity"]
tags: ["ISC2 CISSP", "CISSP", "asset security", "data classification", "data roles", "data lifecycle", "data remanence", "data destruction", "DRM", "DLP", "CASB", "data states", "retention"]
cover: "/img/cover/isc2-cissp-asset-security-data-management.webp"
coverAlt: "An illustration showing various digital assets such as servers and cloud icons connected by secure pathways, all on a dark background. Vibrant colors of blue, green, and cyan enhance the image."
coverCaption: "Master Asset Security for the CISSP Exam"
---

#### [Click Here to Return To the ISC2 CISSP Course Page](/cissp-start/)

**Asset Security** is **10%** of the **ISC2 CISSP** exam. This module covers how you classify, handle, and protect information and assets across their full lifecycle. *You cannot protect what you have not classified. Classification drives every control that follows.*

## Information and Asset Classification

You **classify** information and assets by their value and sensitivity. Classification decides how much protection each asset needs, so you spend money where it matters.

| Sector | Example labels (high to low) |
|--------|------------------------------|
| Government | Top Secret, Secret, Confidential, Unclassified |
| Commercial | Confidential, Private, Sensitive, Public |

For more on who sets these labels, read [who designates whether information is classified](/articles/who-designates-whether-information-is-classified/). You then set **handling requirements** so each label has clear rules for marking, storage, transport, and sharing.

## Data Roles

You manage **data roles** so accountability is clear. The exam tests these distinctions hard:

| Role | Responsibility |
|------|----------------|
| **Data owner** | Senior person accountable for the data, sets classification |
| **Data controller** | Decides why and how data is processed |
| **Data custodian** | Implements and maintains controls day to day |
| **Data processor** | Processes data on behalf of the controller |
| **Data user** | Uses the data to do their job |

The **owner** is accountable and senior. The **custodian** does the hands-on protection.

## The Data Lifecycle and Retention

You provision assets securely and manage the **data lifecycle** from creation to destruction. You set **asset retention** based on legal and business need, including **End of Life (EOL)** and **End of Support** dates, after which a system no longer gets patches and becomes a risk.

You also address **data remanence**, the residual data left on media after deletion. Standard file deletion does not remove data, so you use proper **destruction** methods.

| Method | How it works | Reuse media? |
|--------|--------------|--------------|
| **Clearing** | Overwrite with new data | Yes, internally |
| **Purging** | Degaussing or strong overwrite | Sometimes |
| **Destruction** | Shred, incinerate, pulverize | No |

*Crypto-shredding, destroying the encryption key, is a fast way to render encrypted data unrecoverable.*

## Data Security Controls

You determine controls based on the **data state**. Each state needs different protection.

| State | Protection |
|-------|------------|
| **At rest** | Full-disk or file encryption |
| **In transit** | TLS, IPSec, VPN |
| **In use** | Access controls, memory protection |

You apply **scoping** (selecting which controls apply) and **tailoring** (adjusting them to fit your environment) so a control baseline fits your real systems.

## Data Protection Methods

You apply specific technologies to enforce protection:

| Method | Purpose |
|--------|---------|
| **DRM** | Digital Rights Management controls how content is used and copied |
| **DLP** | Data Loss Prevention blocks sensitive data from leaving the org |
| **CASB** | Cloud Access Security Broker enforces policy between users and cloud services |

## Next Steps

With assets classified and protected, move to [Security Architecture and Engineering](/cissp/security-architecture-and-engineering/) to design secure systems, then [Communication and Network Security](/cissp/communication-and-network-security/). Revisit [Security and Risk Management](/cissp/security-and-risk-management/) for the governance behind classification, and return to the [ISC2 CISSP Course](/cissp-start/) for the full path.
