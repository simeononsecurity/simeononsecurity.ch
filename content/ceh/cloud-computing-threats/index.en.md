---
title: "CEH v13: Cloud Computing Threats"
date: 2025-01-01
toc: true
draft: false
description: "Master cloud computing threats for the EC-Council Certified Ethical Hacker (CEH v13) exam. Learn the shared responsibility model, cloud misconfigurations, IAM weaknesses, ScoutSuite, Pacu, container escape, and CSPM."
genre: ["EC-Council CEH Course", "Ethical Hacking", "Penetration Testing", "Offensive Security", "Cybersecurity", "Network Security", "Security Testing", "Hacking Techniques", "CEH Certification", "Information Security"]
tags: ["CEH", "CEH v13", "ethical hacking", "EC-Council", "penetration testing", "cloud computing threats", "offensive security", "cybersecurity", "hacking", "security testing"]
cover: "/img/cover/cloud-computing-threats-ceh-v13.webp"
coverAlt: "An illustration of a cloud computing environment showing stylized cloud icons and digital locks, set against a dark background with abstract network connections, depicting threats to cloud security."
coverCaption: "Master Cloud Computing Threats for the CEH v13 Exam"
---

#### [Click Here to Return To the Certified Ethical Hacker (CEH v13) Course Page](/ceh-start/)

**Cloud Computing Threats** targets cloud environments in the **EC-Council CEH v13** course. This module covers the shared responsibility model, common misconfigurations, identity attacks, container risks, and the controls that secure cloud workloads. *Cloud providers require written authorization and often a formal pen-test request before any testing, so confirm the rules before you scan.*

Most cloud breaches come from customer misconfiguration, not a flaw in the provider. You learn where those gaps appear and how attackers exploit them.

## Shared Responsibility Model

The provider secures the cloud, and you secure what you put in it. The split shifts by service model.

| Model | Provider secures | You secure |
|-------|------------------|------------|
| **IaaS** | Hardware, hypervisor | OS, apps, data, IAM |
| **PaaS** | OS, runtime | Apps, data, access |
| **SaaS** | Most of the stack | Data, user access |

*A misread of this model is the root cause of most cloud incidents.*

To compare the major platforms, see [AWS vs Azure vs Google Cloud Platform](/articles/aws-vs-azure-vs-google-cloud-platform/).

## Common Cloud Misconfigurations

Attackers scan for predictable mistakes that expose data and control.

- **Open storage buckets** leave S3 or blob storage public to the internet.
- **Exposed APIs** and metadata endpoints leak credentials and tokens.
- **Weak IAM policies** grant broad permissions with wildcards.
- **Hardcoded keys** sit in source code, containers, and config files.

The **instance metadata service** is a frequent target. A server-side request forgery flaw can pull temporary credentials from it.

```bash
# Classic IMDSv1 credential theft from a vulnerable host
curl http://169.254.169.254/latest/meta-data/iam/security-credentials/
```

IMDSv2 requires a session token and blocks this simple request, so enforce it.

## Cloud Auditing Tools

You assess cloud posture with purpose-built tools.

| Tool | Use |
|------|-----|
| **ScoutSuite** | Multi-cloud configuration audit |
| **Pacu** | AWS exploitation framework |
| **CloudSploit** | Misconfiguration scanning |

These tools map permissions, find public resources, and flag risky settings across an account.

## Container and Serverless Risks

Containers add their own attack surface. **Container escape** breaks out of a container to the host when the runtime is misconfigured or over-privileged.

- **Privileged containers** share the host kernel with full rights.
- **Exposed Docker sockets** hand an attacker control of the host.
- **Vulnerable images** ship with known CVEs and embedded secrets.

To understand the isolation tradeoffs, read [Docker vs VMs](/articles/docker-vs-vms/).

## Cloud Defense

| Control | Purpose |
|---------|---------|
| **CSPM** | Finds and fixes misconfigurations continuously |
| **Least privilege** | Limits IAM roles to required actions |
| **Encryption** | Protects data at rest and in transit |
| **Logging** | Records API calls for detection and forensics |

Least-privilege IAM and continuous posture management stop most cloud attacks before they start.

## Next Steps

Continue with [Cryptography and PKI](/ceh/cryptography-and-pki/). Review the previous module on [IoT and OT Hacking](/ceh/iot-ot-hacking/), compare providers in [AWS vs Azure vs Google Cloud Platform](/articles/aws-vs-azure-vs-google-cloud-platform/), and study isolation in [Docker vs VMs](/articles/docker-vs-vms/). Return to the [Certified Ethical Hacker (CEH v13) Course](/ceh-start/).
