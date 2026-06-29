---
title: "CompTIA A+ (220-1201): Virtualization and Cloud Computing"
date: 2025-01-01
toc: true
draft: false
description: "Master virtualization and cloud computing for the CompTIA A+ 220-1201 Core 1 exam. Learn virtual machines, hypervisors, VDI, containers, cloud models, and cloud characteristics."
genre: ["CompTIA A+ Course", "Virtualization", "Cloud Computing", "Hypervisors", "IT Support", "CompTIA Certification", "Help Desk", "Containers", "VDI", "IT Fundamentals"]
tags: ["CompTIA A+", "220-1201", "virtualization", "cloud computing", "hypervisor", "VDI", "containers", "IaaS", "SaaS", "PaaS", "private cloud", "public cloud", "hybrid cloud", "elasticity"]
cover: "/img/cover/comptia-a-plus-virtualization-cloud-computing.webp"
coverAlt: "An abstract digital illustration showing interconnected virtual machines and hypervisors, layered representations of various cloud models, all against a dark background with vibrant blue and green accents."
coverCaption: "Master Virtualization and Cloud Computing for the A+ 220-1201 Exam"
---

#### [Click Here to Return To the CompTIA A+ Course Page](/a-plus-start/)

**Virtualization and Cloud Computing** is **11%** of the **CompTIA A+ 220-1201 Core 1** exam. This module covers virtual machines, hypervisor types, VDI, containers, cloud models, and cloud characteristics. *This is the smallest Core 1 domain, but the concepts appear across modern IT support.*

Virtualization runs many systems on one machine. Cloud computing rents that capacity from a provider so you pay only for what you use. Together they power most of the infrastructure you support today. This module gives you the vocabulary and the models.

## Virtualization Concepts

You run software-defined computers on physical hardware.

- A **virtual machine (VM)** emulates a full computer with its own OS, isolated from the host.
- A **sandbox** runs untrusted code in isolation so it cannot harm the host.
- **Test and development environments** let you try changes without risking production.
- **Snapshots** capture a VM state so you roll back after a failed change.

*Virtualization saves money by packing many workloads onto fewer physical servers.*

## Hypervisor Types

You pick the hypervisor that fits the workload.

| Type | Runs on | Example | Use |
|------|---------|---------|-----|
| **Type 1 (bare metal)** | Directly on hardware | ESXi, Hy-V, Proxmox | Data centers, servers |
| **Type 2 (hosted)** | On top of an OS | VirtualBox, VMware Workstation | Desktops, labs, testing |

**Type 1** hypervisors are faster and more secure because no host OS sits between them and the hardware. **Type 2** hypervisors are easier to install on a normal desktop.

## Virtualization Requirements

You meet the prerequisites before a VM runs well.

- **CPU support** for **Intel VT-x** or **AMD-V**, enabled in UEFI.
- Enough **RAM** to allocate to each guest plus the host.
- **Storage** for virtual disks, ideally on fast SSDs.
- **Network** configuration with bridged, NAT, or host-only adapters.
- **Security** isolation so a compromised guest cannot reach the host.

## Desktop Virtualization and Containers

You deliver desktops and apps without local installs.

- **Virtual Desktop Infrastructure (VDI)** hosts user desktops on a central server, streamed to thin clients.
- **Containers** package an app with its dependencies but share the host OS kernel, so they are lighter than VMs.

Containers start in seconds and use less memory than full VMs. To understand the trade-offs, read [Docker vs VMs](/articles/docker-vs-vms/).

## Cloud Computing Models

You choose a deployment model by who owns and uses the resources.

| Model | Who uses it |
|-------|-------------|
| **Public** | Shared infrastructure from a provider like AWS or Azure |
| **Private** | Dedicated infrastructure for one organization |
| **Hybrid** | A mix of public and private |
| **Community** | Shared by organizations with common needs |

## Cloud Service Models

You match the service model to how much you want to manage.

| Model | You manage | Provider manages |
|-------|------------|------------------|
| **IaaS** | OS, apps, data | Hardware, network, virtualization |
| **PaaS** | Apps and data | OS, runtime, infrastructure |
| **SaaS** | Just your data | Everything else |

**IaaS** gives the most control, **SaaS** gives the least responsibility. Compare the major providers in [AWS vs Azure vs Google Cloud Platform](/articles/aws-vs-azure-vs-google-cloud-platform/).

## Cloud Characteristics

You recognize the traits that define cloud services.

- **Shared vs dedicated resources** trade cost for isolation.
- **Metered utilization** charges by actual usage.
- **Rapid elasticity** scales capacity up or down on demand.
- **High availability** keeps services running through failures.
- **Multitenancy** lets many customers share infrastructure securely.

*Elasticity is what lets a website handle a traffic spike without buying permanent hardware.*

## Next Steps

You have now covered all five Core 1 domains. Consolidate with [Hardware and Network Troubleshooting](/a-plus/hardware-network-troubleshooting-core1/), then begin Core 2 with [Operating Systems](/a-plus/operating-systems-windows-linux-macos/). Review [Hardware Components](/a-plus/hardware-components-cpu-ram-storage-motherboards/) for virtualization hardware. Return to the [CompTIA A+ Course](/a-plus-start/).
