---
title: "CompTIA Security+ (SY0-801): Security Architecture"
date: 2025-01-01
toc: true
draft: false
description: "Study Security Architecture for CompTIA Security+ SY0-801. Compare deployment models, secure infrastructure access, protect sensitive data, and choose recovery designs based on business requirements."
genre: ["CompTIA Security+ Course", "SY0-801", "Security Architecture", "Cybersecurity"]
tags: ["CompTIA Security+", "SY0-801", "security architecture", "network segmentation", "zero trust", "data protection", "disaster recovery", "RTO", "RPO"]
cover: "/img/cover/comptia-security-plus-sy0-801-security-architecture.webp"
coverAlt: "Blue network paths connect separate zones containing servers, workstations, and database storage."
coverCaption: "Security architecture for CompTIA Security+ SY0-801"
---

#### [Click Here to Return To the CompTIA Security+ SY0-801 Course Page](/security-plus-sy0-801-start/)

**Security Architecture accounts for 19% of the CompTIA Security+ SY0-801 exam. You compare deployment models, choose trust boundaries, protect data through its life cycle, and design recovery around business limits.**

*For scenario questions, identify the requirement the design must satisfy before comparing controls.*

## 3.1: Compare Architecture Models

A trust boundary separates systems with different access rules or administrative authority. Draw the boundary around what you need to protect. Then identify who runs each side, what crosses it, and which failures both sides share.

| Architecture | When it fits | What you still need to manage |
|---|---|---|
| **On-premises or private cloud** | The organization needs dedicated infrastructure, direct control, or predictable local access. A private cloud is dedicated to one organization and is not always on premises. | Staffing, power, maintenance, and off-site recovery if you operate the equipment. |
| **Public cloud** | A provider's shared infrastructure offers capacity without buying equipment. | Tenant identities, data, and configuration. In infrastructure as a service (IaaS), the customer typically manages the guest operating system. |
| **Serverless** | Event-driven workloads need variable capacity and do not depend on local state. | Code, execution roles, input handling, logs, and quotas. The provider manages the runtime infrastructure. |
| **Hybrid** | Local systems and cloud services serve different requirements. | Trust between environments, consistent policy, and exactly which data crosses the boundary. |
| **Multicloud** | Separate providers meet distinct workload needs or reduce dependence on one provider. | Identity, data movement, monitoring, and failover across different platforms. |
| **Community cloud** | Organizations with shared requirements pool infrastructure under a common governance model. | Participation rules, tenant separation, and responsibility for controls and incident handling. |

**Infrastructure as code (IaC)** stores infrastructure definitions in version control. Review changes before deployment and use approved templates to reproduce the same network during recovery. Check for drift, which occurs when the deployed state differs from its approved definition. A weak shared template spreads mistakes as readily as a strong template spreads controls.

**Microservices** split an application into independently deployed services. The split helps limit change and scale individual components but adds service identities, API connections, and dependencies. A service boundary does not establish isolation unless the network and authorization policies enforce it.

**Operational technology (OT)** controls physical processes and often has strict timing, uptime, and safety requirements. Place a legacy controller without a supported patch in a separate zone when direct enterprise access creates an unacceptable risk. A **data diode** enforces one-way transfer when the receiver must never communicate back. An **air gap** removes the network connection entirely but complicates updates, monitoring, and file handling.

VLANs and subnets provide logical separation. Apply routing and filtering rules at the boundary to enforce it. Physical segmentation uses separate equipment and paths, which costs more but removes shared equipment from the trust model. A hospital with a contract forbidding shared hypervisors needs dedicated hosts, not another VLAN.

Weigh availability, ease of recovery, usability, environmental requirements, and compute and power needs alongside cost and scalability. Confirm data sovereignty, meaning the jurisdiction governing the data, and who owns and operates the hardware. For open-source versus proprietary platforms, compare the support and patching capacity you have, not the license price alone.

## 3.2: Protect Infrastructure With Zones and Access Controls

**Device placement** sets the starting trust boundary. Put an internet-facing service in a screened subnet, often called a demilitarized zone (DMZ). Allow only required traffic to internal services. For example, a public appointment service needs its scheduling API, not a route to the patient database. Keep the management path separate from normal application traffic. Reducing the number of reachable interfaces, services, and administration paths reduces the attack surface.

**Zero trust** grants access based on identity, device condition, and resource policy instead of network location. A supplier with valid multifactor authentication still loses access if its laptop falls out of compliance. Inventory identifies the device, posture checks assess its current condition, and application policy limits access to the needed resource.

| Access requirement | Design choice |
|---|---|
| Protect traffic between two networks | Use a site-to-site virtual private network (VPN) with restricted routes and rules. A tunnel protects traffic in transit without granting appropriate application permissions by itself. |
| Give a contractor access to one private application | Use an application access broker with user authentication, device checks, and app-specific authorization. |
| Manage web, SaaS, and private application access together | Use a security service edge (SSE) combining web filtering, SaaS controls, and private application access. |
| Recover a firewall after production routing fails | Use an out-of-band console on independent connectivity with controlled emergency authentication. A separate VLAN over the failed link does not provide independence. |
| Exchange sensitive messages or files | Use end-to-end encrypted messaging when intermediaries must not read messages. For file transfer, use an approved encrypted channel with scoped recipient access and audit records. |

Authentication verifies an identity, authorization sets its permissions, and accounting records its activities. Apply **least privilege** to human accounts, service identities, and management systems. Review access when staff change roles to avoid privilege creep, the buildup of permissions no longer needed. In supported Windows environments, a group managed service account lets Active Directory manage the service credential. Limit which hosts use it and which resources it reaches.

**Fail-open** behavior continues access or traffic when a control fails. **Fail-closed** behavior denies it. Judge the outcome against safety, security, and operational needs. If a shelter entrance must admit people during a power failure, choose fail-open entry. Choose fail-closed entry for a records vault required to deny new access during an outage. Emergency egress has its own safety requirements. For critical services, test both the security and availability impact of each failure mode before choosing it.

## 3.3: Protect Data Across Its Life Cycle

**Structured data** follows defined fields, such as rows in a database. **Unstructured data** includes files such as images and free-text documents. Both need classification and handling rules. Public data still needs integrity protection. Confidential or restricted data needs tighter access. Criticality describes the impact of losing the data or its availability, not whether it is secret. Formal labels such as Secret and Top Secret belong to specific classification systems and are not interchangeable with business labels.

| Data state | Example | Protection decision |
|---|---|---|
| **At rest** | A database export in object storage | Encrypt the export, restrict keys and storage access, and apply retention and deletion rules. |
| **In transit** | A records file moving between organizations | Encrypt and authenticate the connection. Verify the recipient and restrict file access as well. |
| **In use** | A workload processing sensitive input in memory | Restrict process access. Where the threat includes the host's privileged layer, evaluate a trusted execution environment with attestation and conditional key release. |

Choose an operation based on whether the recipient needs the original data:

- **Masking** shows a partial or substitute value. Apply it to exports and APIs as well as screens.
- **Tokenization** substitutes an identifier. A protected mapping preserves a route back to the original for authorized workflows.
- **Hashing** maps inputs to a fixed-size digest without a decryption key. Use it for integrity checks, not when an authorized user must retrieve the original. Predictable values still need protection against guessing.
- **Encryption** protects confidentiality when keys and decryption rights remain controlled. It does not limit what a user already authorized to decrypt sees.
- **Filtering and redaction** withhold disallowed fields from a copy. **Obfuscation** or reordering values in a transformed copy is not a substitute for encryption or verified de-identification.
- **De-identification** reduces links to people. Removing names is insufficient when exact timestamps and rare combinations still identify someone. For a department-by-hour report, release aggregates and suppress small groups.

During creation, mark the data and collect only what you need. During use and distribution, enforce endpoint rules, authorized recipients, and approved storage locations. Location-based access or geofencing limits where requests originate but does not prove where records, logs, or backups reside. Specify placement separately. Apply retention limits, honor authorized investigation holds, and verify disposal after the hold ends.

The **data owner** sets classification and access rules. A **steward** coordinates data quality and governance, a **custodian** implements and maintains protection, and an **operator** handles data under approved procedures. In privacy regimes using these terms, a **controller** determines the purposes and means of processing. A **subprocessor** performs delegated processing for a processor. Confirm which definitions apply to your contract or legal framework. Health, child, financial, personal, legal, and intellectual property records have distinct handling obligations. Choose controls after identifying the applicable requirement.

## 3.4: Design for Resilience and Recovery

**High availability** reduces interruption during component failures. **Disaster recovery** restores systems and data after a major disruption. **Business continuity** keeps essential work going, for example through an approved manual process while a system is restored. A second server does not protect against the loss of a shared storage array, identity provider, or power feed.

| Recovery site | Starting condition | Tradeoff |
|---|---|---|
| **Hot** | Infrastructure and service stack are ready, with recent data under the replication design. | Fastest activation in a typical design, but higher operating cost. |
| **Warm** | Some infrastructure is ready. Data restore or service startup takes additional time. | Lower standby cost in exchange for a longer recovery. |
| **Cold** | Space and basic facilities exist. Hardware or applications still need setup. | Lower recurring cost and usually the longest recovery. |

Use load balancing to distribute requests and clustering to provide service across nodes. Autoscaling adds capacity within configured quotas and depends on the services scaling alongside it. Test a surviving site at peak load, including its identity, storage, and network dependencies. Put recovery infrastructure outside shared environmental hazards. Platform diversity reduces some common failures, but introduces more software, hardware, or vendors to maintain.

**Power and storage redundancy** address different failures. An uninterruptible power supply (UPS) bridges short outages or the interval before a generator starts. Redundant power supplies need independent feeds to survive a feed failure. A surge protector does not supply backup power. Redundant storage protects service availability after component failure, but it is not a backup. Replication copies unwanted changes as well as valid ones when the replication policy does not distinguish between them.

Define backup scope, retention, and immutability. Include configuration, keys, and dependencies needed to restore service. Separate backup administrative access from production and test restores using emergency credentials. Use simulations to test decisions, parallel processing to compare results on both systems, and controlled failover to measure actual service recovery under load.

| Metric | Question it answers |
|---|---|
| **Recovery time objective (RTO)** | How long is the outage allowed to last? |
| **Recovery point objective (RPO)** | How much recent data is the business willing to lose, measured in time? |
| **Mean time to repair (MTTR)** | On average, how long does a repair take under the stated measurement rules? |
| **Mean time between failures (MTBF)** | On average, how much operating time passes between failures of a repairable system? |

If dispatch must return within 45 minutes and lose no more than 10 minutes of updates, a tested 30-minute restore with five-minute replication meets those targets in the stated scenario. A 25-minute restore from an hourly backup meets the RTO but not the RPO. Check which scenario the recovery test represents before treating those timings as dependable.

## Self-Check: Recover the Dispatch Portal

A regional transit operator must recover its public incident portal within 45 minutes if it loses the primary site. The public portal must never reach the rider records database directly. The portal serves public incident updates from a private API and does not need to query rider records. The operator accepts losing up to 10 minutes of portal updates and does not have funds to operate a second production stack continuously.

Which option best meets the constraints?

1. Put the web tier in a screened subnet with API-only access and use a warm site tested at a 35-minute recovery with five-minute replication.
2. Put the web tier in a screened subnet with read-only database access and use a hot site tested at a 10-minute recovery with synchronous replication.
3. Keep the web tier on the records subnet with a direct but authenticated database connection and use a warm site tested at a 25-minute recovery with five-minute replication.
4. Put the web tier in a screened subnet with API-only access and use a cold site tested at a 90-minute recovery with five-minute backups.

Option 1 meets the network boundary, RTO, RPO, and operating budget. Option 2 gives the web tier a forbidden direct path and uses an always-on secondary. Option 3 meets both recovery metrics but keeps the forbidden database path. Option 4 protects the database and limits data loss but misses the outage target.

## Next Steps

- Review [Threats, Vulnerabilities, and Attacks](/security-plus-sy0-801/threats-vulnerabilities-and-attacks/).
- Continue to [Security Operations](/security-plus-sy0-801/security-operations/).
- Test your decisions with the [SY0-801 practice test](/security-plus-sy0-801-practice-test/).
- Return to the [Security+ SY0-801 course page](/security-plus-sy0-801-start/).
