---
title: "CompTIA SecurityX (CAS-005): Security Architecture"
date: 2025-01-01
toc: true
draft: false
description: "Master security architecture for the CompTIA SecurityX CAS-005 exam. Learn resilient system design, secure SDLC, Zero Trust, cloud security, IAM and PKI design, and data security."
genre: ["CompTIA SecurityX Course", "Security Architecture", "Zero Trust", "Cloud Security", "Secure SDLC", "Identity Management", "PKI", "CASP+", "Enterprise Security", "Cybersecurity"]
tags: ["CompTIA SecurityX", "CASP+", "CAS-005", "security architecture", "resilient systems", "SAST", "DAST", "IAST", "SBoM", "Zero Trust", "microsegmentation", "SASE", "SD-WAN", "CASB", "container security", "PKI", "OCSP stapling", "DLP"]
cover: "/img/cover/comptia-securityx-security-architecture-design.webp"
coverAlt: "A digital illustration of a modern security architecture featuring interconnected components like firewalls, VPNs, and API gateways on a dark background with vibrant colors."
coverCaption: "Master Security Architecture for the CAS-005 Exam"
---

#### [Click Here to Return To the CompTIA SecurityX Course Page](/casp-plus-start/)

**Security Architecture** is **27%** of the **CompTIA SecurityX (CAS-005)** exam. This module covers how you design systems that stay available, resist attack, and recover fast. *At 27% and feeding directly into security engineering, spend solid time on Zero Trust and cloud design here.*

An architect makes trade-offs leadership can live with. You balance security against cost, performance, and usability, then place each control where it does the most good. This domain is about design decisions, not button-clicking.

## Designing Resilient Systems

You place security components where traffic flows so each control sees what it needs to inspect.

| Component | Placement and role |
|-----------|--------------------|
| **Firewall** | Network boundary, filters by rules |
| **IPS/IDS** | Inline (IPS) or tap (IDS) to detect and block attacks |
| **WAF** | In front of web apps, filters layer 7 attacks |
| **VPN** | Encrypts remote and site-to-site traffic |
| **NAC** | At access points, checks device health before joining |
| **API gateway** | In front of APIs, enforces auth and rate limits |
| **CDN** | At the edge, caches content and absorbs DDoS |

You design for **availability and integrity** so a single failure does not take the business down:

- **Load balancing** spreads traffic across servers and removes single points of failure.
- **Recoverability** plans for fast restore through backups and failover.
- **Interoperability** lets systems work together using open standards.
- **Scaling** adds capacity. *Vertical* scaling grows one server. *Horizontal* scaling adds more servers and scales further.

## Security Throughout the Systems Life Cycle

You build security into development rather than testing at the end.

| Tool | What it checks |
|------|----------------|
| **SAST** | Source code, before running |
| **DAST** | A running application, black-box |
| **IAST** | Inside a running app during testing |
| **RASP** | Runtime, blocks attacks live in production |
| **SCA** | Third-party dependencies for known CVEs |

You generate an **SBoM** (software bill of materials) so you know every component you ship, and you secure the **CI/CD** pipeline because it has access to build and deploy everything.

## Supply Chain and Hardware Assurance

You manage supply chain risk for both software and hardware. You verify hardware authenticity to block counterfeits and tampered components, and you plan for **end-of-life** so unsupported hardware does not linger as an unpatched risk.

## Zero Trust

**Zero Trust** removes implicit trust based on network location. You verify every request with identity, device posture, and context. The summary is *never trust, always verify*.

- **Segmentation** divides the network into zones.
- **Microsegmentation** isolates individual workloads with their own policies.
- **SASE** (Secure Access Service Edge) combines networking and security in the cloud.
- **SD-WAN** routes traffic intelligently across links with built-in security.
- **Subject-object relationships** define which identities (subjects) may act on which resources (objects).

## Cloud Security

You implement cloud capabilities securely and respect the shared responsibility model.

- **CASB** (Cloud Access Security Broker) enforces policy between users and cloud apps.
- **Shadow IT detection** finds unsanctioned cloud services employees adopt on their own.
- **Shared responsibility** splits duties: the provider secures the cloud, you secure what you put in it.
- **Container security** scans images, limits privileges, and isolates workloads.
- **Serverless** shrinks the attack surface but shifts focus to code and configuration.

Compare the major providers in [AWS vs Azure vs Google Cloud](/articles/aws-vs-azure-vs-google-cloud-platform/).

## Access, Authentication, and Authorization

You design identity systems that scale across the enterprise.

- **Federation** lets one identity work across organizations.
- **SSO** lets a user authenticate once and reach many systems.
- **PKI architecture** issues and manages certificates through a trusted CA hierarchy.
- **OCSP stapling** lets a server present a fresh certificate-status response, cutting revocation-check latency.

```bash
# Verify a certificate chain and check OCSP stapling on a server
openssl s_client -connect example.com:443 -status -servername example.com < /dev/null 2>/dev/null | grep -A 5 "OCSP"
```

## Data Security Design

You protect data by classifying it and controlling where it goes.

- **Classification models** rank data by sensitivity, such as public, internal, confidential, and restricted.
- **Data labeling** tags data so controls apply automatically.
- **DLP** (Data Loss Prevention) blocks sensitive data from leaving through email, USB, or cloud.
- **Third-party integrations** need data-handling controls so partners cannot leak your data.

## Next Steps

With the architecture designed, continue to [Security Engineering](/casp-plus/security-engineering/) to implement these controls, then [Security Operations](/casp-plus/security-operations/) to run them. Return to [Governance, Risk, and Compliance](/casp-plus/governance-risk-compliance/) for the business context and the [CompTIA SecurityX Course](/casp-plus-start/).
