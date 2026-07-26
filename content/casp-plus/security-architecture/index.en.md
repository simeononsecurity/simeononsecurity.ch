---
title: "CompTIA SecurityX (CAS-005): Security Architecture"
date: 2025-01-01
toc: true
draft: false
description: "Master security architecture for the CompTIA SecurityX CAS-005 exam. Learn resilient system design, secure SDLC, Zero Trust, cloud security, IAM and PKI design, data security, and supply chain assurance."
genre: ["CompTIA SecurityX Course", "Security Architecture", "Zero Trust", "Cloud Security", "Secure SDLC", "Identity Management", "PKI", "CASP+", "Enterprise Security", "Cybersecurity"]
tags: ["CompTIA SecurityX", "CASP+", "CAS-005", "security architecture", "resilient systems", "SAST", "DAST", "IAST", "RASP", "SBoM", "Zero Trust", "microsegmentation", "SASE", "SD-WAN", "CASB", "container security", "PKI", "OCSP stapling", "DLP", "DMZ", "federation", "SCIM", "ABAC", "DevSecOps", "supply chain", "privacy by design"]
cover: "/img/cover/comptia-securityx-security-architecture-design.webp"
coverAlt: "A digital illustration of a modern security architecture featuring interconnected components like firewalls, VPNs, and API gateways on a dark background with vibrant colors."
coverCaption: "Master Security Architecture for the CAS-005 Exam"
---

#### [Click Here to Return To the CompTIA SecurityX Course Page](/casp-plus-start/)

**Security Architecture** is **27%** of the **CompTIA SecurityX (CAS-005)** exam, the second-heaviest domain and the one that shapes all others. This domain covers how you design systems that stay available, resist attack, and recover quickly. *At 27% and feeding directly into Security Engineering, spend solid time on Zero Trust, cloud architecture, and secure SDLC here.*

An architect makes trade-offs leadership can accept. You balance security against cost, performance, and usability, then place each control where it provides the most value. If Governance sets the risk appetite, Architecture decides how to satisfy it.

## Designing Resilient Systems

### Network Security Component Placement

You place controls where traffic flows so each inspects the traffic it is designed to handle.

| Component | Best placement | Role |
|-----------|---------------|------|
| **Firewall** | Network boundary and segment boundaries | Filters traffic by rule; stateful or stateless |
| **IPS** | Inline on critical paths | Detects and blocks attacks in real time |
| **IDS** | Tap or SPAN port | Detects and alerts without disrupting flow |
| **WAF** | In front of web and API servers | Filters Layer 7 attacks; stops OWASP Top 10 |
| **VPN** | At the edge for remote and site-to-site | Encrypts traffic over untrusted networks |
| **NAC** | At access layer switches and wireless APs | Checks device health before granting network access |
| **API gateway** | In front of microservices | Enforces auth, rate limits, and input validation |
| **CDN** | At the global edge | Caches content; absorbs volumetric DDoS |
| **Proxy / web proxy** | Between users and internet | Inspects and filters outbound web traffic |

### Network Topology Patterns

The layout of your network defines what attackers can reach after compromising one component.

- A **DMZ** (demilitarized zone) sits between two firewalls. Internet-facing servers — web, email, DNS — live here, isolated so a DMZ breach does not reach internal assets.
- A **screened subnet** uses a single firewall with three interfaces. Simpler but provides less depth.
- **Air-gapped networks** have no electronic connection to untrusted networks. Required for classified environments and critical infrastructure control systems.
- **VLANs** segment a flat network into logical zones, limiting lateral movement without new hardware.

### Availability and Integrity Design

A single point of failure ends availability. You engineer it out through redundancy.

- **Load balancing** distributes traffic across servers, removes single points of failure, and enables rolling deploys.
- **Active-active clustering** runs all nodes simultaneously and shares load. Highest availability, highest cost.
- **Active-passive clustering** keeps standby nodes for automatic failover. Lower cost, brief failover delay.
- **Recoverability** requires tested backups and runbooks. Untested backups are assumptions, not assets.
- **Interoperability** uses open standards so heterogeneous components integrate without re-architecture.
- **Vertical scaling** adds RAM or CPU to one server. Fast but limited.
- **Horizontal scaling** adds servers behind a load balancer. Scales further but requires stateless application design.

*Active-active provides better performance under load. Active-passive provides simpler failover logic. The exam will present scenarios where you choose one — match availability requirement to cost.*

## Security Throughout the Systems Life Cycle

### Application Security Testing in the Pipeline

You shift security left so defects are corrected when they cost the least to fix.

| Tool/Practice | Stage | What it examines |
|--------------|-------|-----------------|
| **SAST** (Static Analysis) | Pre-commit, CI | Source code before execution; finds injection, hardcoded creds |
| **DAST** (Dynamic Analysis) | Staging | Running app from outside; simulates external attacker |
| **IAST** (Interactive) | QA testing | Agent inside a running app during test execution |
| **RASP** (Runtime Protection) | Production | Intercepts and blocks attacks inside the running process |
| **SCA** (Software Composition Analysis) | CI/CD | Third-party libraries for known CVEs |

The **CI/CD pipeline** itself is a high-value attack target because it has build and deploy authority. You protect it by requiring signed commits, limiting access to secrets, enforcing branch protection, and scanning pipeline configurations.

You generate an **SBOM** (Software Bill of Materials) for every release so you can quickly identify and patch when a transitive dependency has a new CVE.

### Supply Chain and Hardware Assurance

You verify software and hardware integrity across the supply chain.

- **Signed software** uses code signing to prove provenance and detect tampering.
- **Hardware attestation** uses TPM measurements to verify hardware has not been replaced with counterfeits.
- **End-of-life planning** schedules hardware replacement before vendor support ends, removing unpatched risk.
- **Secure boot process** validates firmware and bootloader signatures before executing them.

## Zero Trust Architecture

**Zero Trust** removes implicit trust based on network location. You verify every request using identity, device posture, and context. The principle is: *never trust, always verify*.

| Zero Trust Component | What it does |
|--------------------|-------------|
| **Segmentation** | Divides the network into zones with separate policies |
| **Microsegmentation** | Isolates individual workloads with per-workload policies, limiting lateral movement |
| **SASE** | Combines SD-WAN and security services (CASB, SWG, ZTNA) in the cloud |
| **SD-WAN** | Routes traffic intelligently across links with built-in security policy |
| **ZTNA** | Replaces VPN with identity-based, per-session access to specific applications |

In Zero Trust, **subject-object relationships** define which identities (subjects) may perform which actions on which resources (objects). Access is granted at the smallest possible scope for the shortest necessary time.

### Policy Decision and Enforcement Points

Zero Trust frameworks separate two roles:

- **Policy Decision Point (PDP)** evaluates access requests against policy.
- **Policy Enforcement Point (PEP)** enforces the decision close to the resource.

An attacker who compromises a workload in a Zero Trust environment can only reach what that workload's identity is permitted to reach — not the entire flat network.

## Cloud Security Architecture

You design cloud capabilities consistent with the **shared responsibility model**: the cloud provider secures the physical infrastructure and managed services; you secure the configuration, data, and access.

| Cloud Security Control | Purpose |
|-----------------------|---------|
| **CASB** | Cloud Access Security Broker — applies policy between users and cloud apps |
| **Shadow IT detection** | Discovers unsanctioned cloud services employees adopt without approval |
| **CSPM** | Cloud Security Posture Management — finds misconfigurations like open S3 buckets |
| **Container security** | Scans images, limits privileges, applies network policies between pods |
| **Serverless security** | Focuses on code, input validation, and IAM because the OS is abstracted away |
| **CWPP** | Cloud Workload Protection Platform — protects VMs, containers, and functions at runtime |

For a direct cloud provider comparison, see [AWS vs Azure vs Google Cloud](/articles/aws-vs-azure-vs-google-cloud-platform/).

### Multi-Cloud and Hybrid Design

Multi-cloud introduces sprawl and inconsistent identity. You address it by:

- Federating identity so users authenticate once and reach all clouds.
- Maintaining a consistent network security policy across providers using infrastructure as code.
- Centralizing logging and monitoring so you have one view of events across environments.

## Access, Authentication, and Authorization

### Identity Federation and SSO

You design identity so employees authenticate once and access all systems.

- **Federation** extends trust across organizational boundaries using SAML assertions or OIDC tokens. A healthcare provider can federate with a partner lab without sharing passwords.
- **SSO** lets a user authenticate once to an IdP and receive a token accepted by all connected apps.
- **SCIM** (System for Cross-domain Identity Management) automates user provisioning and deprovisioning across systems so a terminated employee loses access everywhere within minutes.

### Authorization Models

| Model | How it assigns access | Best for |
|-------|----------------------|---------|
| **RBAC** | Roles assigned to users; permissions assigned to roles | Stable, well-defined job functions |
| **ABAC** | Policy rules evaluate attributes of user, resource, and environment | Fine-grained, context-sensitive access |
| **MAC** | System enforces labels; users cannot override | Classified environments |
| **DAC** | Resource owner grants access | Sharing within a team |

*ABAC is the most flexible model. It can incorporate time of day, device posture, and data classification into a single access decision. The exam may present a scenario where coarse RBAC is insufficient and ABAC is the correct answer.*

### PKI Architecture

You design a certificate hierarchy that balances security with operational manageability.

- A **root CA** sits offline and signs only intermediate CA certificates. Keeping it offline protects the root key.
- **Intermediate CAs** issue end-entity certificates and can be revoked without replacing the root.
- **Certificate revocation** uses CRL (Certificate Revocation List) or OCSP (Online Certificate Status Protocol).
- **OCSP stapling** lets a web server attach a signed, pre-fetched OCSP response to the TLS handshake, eliminating the delay of a client making its own revocation check.

```bash
# Check OCSP stapling on a live server
openssl s_client -connect example.com:443 -status -servername example.com </dev/null 2>/dev/null \
  | grep -A 5 "OCSP"
```

## Data Security Design

You protect data by classifying it and controlling where it goes.

| Classification Level | Typical Label | Controls Required |
|---------------------|--------------|-------------------|
| **Public** | Unrestricted | Basic integrity |
| **Internal** | Company use only | Access control, encryption in transit |
| **Confidential** | Need-to-know only | Strong access control, encryption at rest and in transit |
| **Restricted** | Regulated or top-secret | MFA, detailed audit logging, DLP |

- **Data labeling** tags data at creation or classification so controls apply automatically as data moves.
- **DLP** (Data Loss Prevention) monitors data in use, in motion, and at rest, blocking transfers that violate policy.
- **IRM / DRM** (Information Rights Management) enforces access policy inside documents regardless of where they travel.
- **Third-party data sharing** requires contractual controls and technical enforcement such as API-level inspection.

### Privacy by Design

You integrate privacy into system design from the start.

- **Data minimization** — collect only what you need.
- **Purpose limitation** — use data only for stated purposes.
- **Storage limitation** — delete data when the purpose is fulfilled.
- **Privacy-Enhancing Technologies (PETs)** include differential privacy, homomorphic encryption, and tokenization.

## Architecture Exam Tips

- DMZ questions: a two-firewall DMZ is always more secure than a single-firewall screened subnet.
- Zero Trust vs. perimeter: the exam often presents a scenario where VPN and perimeter tools are insufficient. ZTNA and microsegmentation are the correct answers.
- Active-active vs. active-passive: choose active-active for performance, active-passive for simplicity.
- RBAC vs. ABAC: when coarse role assignment fails, ABAC provides the fine-grained control.
- OCSP stapling is the performance-friendly revocation check method — it appears on the exam regularly.

## Next Steps

With the architecture designed, move to [Security Engineering](/casp-plus/security-engineering/) to implement these controls. Then cover [Security Operations](/casp-plus/security-operations/) to run them. Return to [Governance, Risk, and Compliance](/casp-plus/governance-risk-compliance/) for the business context that drives architecture decisions, and to the [CompTIA SecurityX Course](/casp-plus-start/) for the full domain overview.
