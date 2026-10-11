---
title: "CompTIA Security+ (SY0-701): Security Architecture"
date: 2025-01-01
lastmod: 2026-10-10
toc: true
draft: false
description: "Design a segmented SY0-701 lab for a library export. Compare cloud duties, data states, firewall rules, and tested recovery evidence."
genre: ["CompTIA Security+ Course", "Security Architecture", "Cloud Security", "Data Protection", "Resilience", "Network Security", "CompTIA Certification", "Information Security", "Zero Trust", "Cybersecurity"]
tags: ["CompTIA Security+", "SY0-701", "security architecture", "cloud", "IaC", "serverless", "microservices", "segmentation", "data protection", "encryption", "high availability", "backups", "resilience", "recovery"]
cover: "/img/cover/comptia-security-plus-security-architecture-overview.webp"
coverAlt: "A digital illustration of various IT infrastructure architecture models, including cloud and on-premises systems, stylized servers, and icons for IoT and microservices, on a dark background."
coverCaption: "Master Security Architecture for the SY0-701 Exam"
---

[Click Here to Return To the CompTIA Security+ Course Page](/security-plus-start/)

**Security Architecture** is **18%** of the **CompTIA Security+ (SY0-701)** exam. This module covers how you design secure infrastructure, protect data across its states, and build systems that survive failure. *Architecture choices decide how resilient your environment stays under attack.*

You apply the concepts from Domain 1 to real designs here. You weigh trade-offs between cloud and on-premises, segment networks, encrypt data, and plan recovery before an incident forces your hand.

## Architecture Models

Each model shifts cost, control, and responsibility differently.

| Model | Strength | Trade-off |
|-------|----------|-----------|
| **On-premises** | More direct control of owned hardware | You operate and patch what you own or contract to manage |
| **Cloud** | Capacity and managed services depend on the offering | Responsibility and visibility vary by service model |
| **Hybrid** | Combines selected local and hosted services | Needs explicit identity, routing, and ownership boundaries |
| **Edge** | Processing near a user or device can reduce latency | Distributed devices need lifecycle and access controls |

You also design with **microservices**, **serverless**, and **Infrastructure as Code (IaC)**. *IaC lets you version and review infrastructure the same way you review code.* Embedded systems like **IoT**, **ICS/SCADA**, and **RTOS** may have constrained maintenance windows, so inventory and segment them according to their actual risk.

## Cloud Security and Shared Responsibility

Cloud duties vary by service model and contract. In a typical infrastructure service, the provider operates underlying facilities and hardware, while the customer manages data, identities, operating systems, and configuration. Managed services shift some tasks to the provider, but the customer still owns access and data decisions.

- **CASB** (Cloud Access Security Broker) enforces policy between users and cloud apps.
- **SASE** converges networking and security capabilities delivered as a service.
- A public storage bucket exposes data when access rules are wrong. Review configuration and test access before release.

Compare the major platforms in [AWS vs Azure vs Google Cloud Platform](/articles/aws-vs-azure-vs-google-cloud-platform/).

## Infrastructure Security

You reduce the attack surface with placement and segmentation.

- **Security zones** group systems by trust level (DMZ, internal, restricted).
- **VLANs** and **subnets** separate traffic at Layer 2 and Layer 3.
- **Zero Trust** removes implicit trust and verifies every request.
- **Network access control (NAC)** checks device health before granting access.

Firewalls come in several types:

| Firewall | Inspects |
|----------|----------|
| **Layer 4 (stateful)** | Ports and connection state |
| **NGFW** | Applications, users, and deep packets |
| **WAF** | Web application traffic (XSS, SQLi) |
| **UTM** | Many functions in one appliance |

Place an **IDS** to detect and an **IPS** to block. Use **DNSSEC** to authenticate DNS data. It does not encrypt queries. Study vendor designs in [Fortinet vs Cisco network security comparison](/articles/fortinet-vs-cisco-network-security-comparison/) and [pfSense vs Firewalla](/articles/pfsense-vs-firewalla-network-security-comparison/).

## Virtualization and Containerization

Virtual machines and containers share a host, so isolation matters.

- A **hypervisor** runs VMs, and **VM escape** is the worst-case breach.
- Containers share the host kernel, so a kernel flaw can spread.
- Scan images, sign them, and run with least privilege.

See [Docker vs VMs](/articles/docker-vs-vms/) for the practical differences.

## Protecting Data

You match the control to the **data state**.

| State | Risk | Control |
|-------|------|---------|
| **At rest** | Stolen disk or backup | Full-disk and database encryption |
| **In transit** | Network sniffing | TLS, IPSec, VPN |
| **In use** | Memory scraping | Access control, secure enclaves |

You also obscure data:

- **Encryption** makes data unreadable without a key.
- **Hashing** creates a one-way fingerprint for integrity.
- **Masking** hides part of a value (showing only the last four digits).
- **Tokenization** swaps data for a non-sensitive token.

## Resilience and Recovery

You design for failure before it happens.

- **Redundancy** removes single points of failure (RAID, dual power, NIC teaming).
- **Load balancing** spreads traffic across servers for uptime.
- **Replication** keeps live copies of data across sites.
- **High availability (HA)** keeps service running through clustering and failover.

Recovery sites trade speed for cost:

| Site | Recovery speed | Cost |
|------|----------------|------|
| **Hot** | Minutes | Highest |
| **Warm** | Hours | Medium |
| **Cold** | Days | Lowest |

Test backups with the **3-2-1 rule**: three copies, two media types, one offsite. A restore test shows whether the backup meets the recovery need.

## Practice: Draw and Test a Trust Boundary

Continue the Harbor Library case. The public catalog serves anonymous readers. Staff use a private records app and export member data. A cloud object store holds encrypted backups. Draw three zones: internet, staff, and restricted records. Mark the trust boundary and each permitted flow.

| Flow | Decision | Reason |
|------|----------|--------|
| Internet to public catalog on HTTPS | Allow | Readers need the catalog. |
| Internet to records database | Deny | No direct public access. |
| Staff app to records database on its required port | Allow for the app identity only | The app needs a narrow path. |
| Backup worker to object store | Allow for backup identity only | The worker needs write access. |
| Anonymous user to backup object | Deny | Backups contain restricted data. |

Now write one misconfiguration to look for in an infrastructure change, such as a bucket policy which grants public read. Explain the review gate and a negative access test. Do not deploy a public bucket to practice. A rule diagram and a written test are enough.

Assign cloud responsibilities to the provider or library: physical data-center security belongs to the provider; library identities, data classification, bucket policy, and restore checks belong to the library. The exact split depends on the service model. Encrypt the export at rest and in transit. Document who controls keys and who is allowed to decrypt.

Choose a recovery target: restore member records within 8 hours with no more than 24 hours of lost changes. These are fictional RTO and RPO requirements. Create a daily backup schedule, an offsite copy, and a monthly test restore to an isolated location. Record start time, finish time, recovered timestamp, file count, access check, and failed steps. RAID and replication improve availability but can copy corruption or deletion. They do not replace a recoverable backup.

Pass when your diagram shows no public path to the records database, your matrix assigns six controls or duties to an owner, and your restore evidence would show whether both targets were met.

References: [CompTIA SY0-701 exam objectives](https://partners.comptia.org/docs/default-source/resources/comptia-security-sy0-701-exam-objectives-(4-0).pdf) and [NIST Cybersecurity Framework 2.0](https://www.nist.gov/cyberframework).

## Next Steps

Operate this architecture securely in [Security Operations](/security-plus/security-operations/), and govern it through [Security Program Management and Oversight](/security-plus/security-program-management-oversight/). Review the basics in [General Security Concepts](/security-plus/general-security-concepts/), then return to the [CompTIA Security+ Course](/security-plus-start/).
