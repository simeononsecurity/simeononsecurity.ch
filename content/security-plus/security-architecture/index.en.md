---
title: "CompTIA Security+ (SY0-701): Security Architecture"
date: 2025-01-01
toc: true
draft: false
description: "Master security architecture for the CompTIA Security+ SY0-701 exam. Learn architecture models, infrastructure security, data protection, and resilience and recovery."
genre: ["CompTIA Security+ Course", "Security Architecture", "Cloud Security", "Data Protection", "Resilience", "Network Security", "CompTIA Certification", "Information Security", "Zero Trust", "Cybersecurity"]
tags: ["CompTIA Security+", "SY0-701", "security architecture", "cloud", "IaC", "serverless", "microservices", "segmentation", "data protection", "encryption", "high availability", "backups", "resilience", "recovery"]
cover: "/img/cover/comptia-security-plus-security-architecture-overview.webp"
coverAlt: "A digital illustration of various IT infrastructure architecture models, including cloud and on-premises systems, stylized servers, and icons for IoT and microservices, on a dark background."
coverCaption: "Master Security Architecture for the SY0-701 Exam"
---

#### [Click Here to Return To the CompTIA Security+ Course Page](/security-plus-start/)

**Security Architecture** is **18%** of the **CompTIA Security+ (SY0-701)** exam. This module covers how you design secure infrastructure, protect data across its states, and build systems that survive failure. *Architecture choices decide how resilient your environment stays under attack.*

You apply the concepts from Domain 1 to real designs here. You weigh trade-offs between cloud and on-premises, segment networks, encrypt data, and plan recovery before an incident forces your hand.

## Architecture Models

Each model shifts cost, control, and responsibility differently.

| Model | Strength | Trade-off |
|-------|----------|-----------|
| **On-premises** | Full control of data and hardware | High cost, you patch everything |
| **Cloud** | Scales fast, provider handles hardware | Shared responsibility, less visibility |
| **Hybrid** | Mixes control and scale | Complex to secure and connect |
| **Edge** | Low latency near the user | Many devices, wide attack surface |

You also design with **microservices**, **serverless**, and **Infrastructure as Code (IaC)**. *IaC lets you version and review infrastructure the same way you review code.* Embedded systems like **IoT**, **ICS/SCADA**, and **RTOS** often lack patching and run for years, so isolate them.

## Cloud Security and Shared Responsibility

In the cloud the provider and customer split duties. The provider secures the **of the cloud** layer (hardware, hypervisor). You secure **in the cloud** (data, identities, configuration).

- **CASB** (Cloud Access Security Broker) enforces policy between users and cloud apps.
- **SASE** combines networking and security in one cloud service.
- Misconfiguration, like a public storage bucket, is the leading cloud breach cause.

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

Place an **IDS** to detect and an **IPS** to block. Secure name resolution with **DNSSEC**. Study vendor designs in [Fortinet vs Cisco network security comparison](/articles/fortinet-vs-cisco-network-security-comparison/) and [pfSense vs Firewalla](/articles/pfsense-vs-firewalla-network-security-comparison/).

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

Test backups with the **3-2-1 rule**: three copies, two media types, one offsite. *A backup you never restored is not a backup you can trust.*

## Next Steps

Operate this architecture securely in [Security Operations](/security-plus/security-operations/), and govern it through [Security Program Management and Oversight](/security-plus/security-program-management-oversight/). Review the basics in [General Security Concepts](/security-plus/general-security-concepts/), then return to the [CompTIA Security+ Course](/security-plus-start/).
