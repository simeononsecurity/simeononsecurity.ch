---
title: "Docker in LXC on Proxmox: Reliability, Evidence, and VM Migration"
date: 2026-09-16
lastmod: 2026-09-16
toc: true
draft: false
description: "Evaluate Docker inside Proxmox LXC with a documented AppArmor failure, a careful reading of a host-freeze report, diagnostic commands, and a VM migration plan."
genre: ["Virtualization", "Linux Administration", "Homelab"]
tags: ["Docker in LXC", "Proxmox Docker", "Proxmox LXC", "Docker virtual machine", "homelab reliability", "Proxmox host freezes", "Debian Docker VM", "unprivileged containers", "container nesting", "Linux kernel isolation", "AppArmor", "runc", "lxc-pve", "Docker Compose", "Docker storage drivers", "containerd image store", "memory pressure", "Linux PSI", "persistent journal", "Proxmox backups", "bind mount backups", "VM migration", "failure domains", "GPU passthrough", "home server troubleshooting"]
cover: "/img/cover/docker-lxc-vm-homelab-isolation.webp"
coverAlt: "Isometric home server illustration showing nested workload boxes and a separate virtual machine compartment connected to shared hardware"
coverCaption: "Conceptual illustration of shared hardware and different workload isolation boundaries"
---

**Docker inside Linux Containers (LXC)** trades some infrastructure overhead for more interactions between the application runtime and the Proxmox host. For Docker services your household depends on, a Debian **virtual machine (VM)** is a practical starting point because it separates the guest kernel and simplifies the environment you must reproduce during troubleshooting. This article examines the supplied video, checks its underlying incident report, and adds documented failures and a migration plan.

<!--more-->

## Key Takeaways

- **Separate failure types:** A Docker startup error, a stalled VM, and an unresponsive physical host require different investigations.
- **Evaluate the evidence:** Stability after migration supports a recovery decision without proving the original cause.
- **Check current documentation:** Native OCI image support and Docker nested inside LXC are different deployment paths.
- **Protect persistent data:** Proxmox backups and Compose files do not automatically cover every application data location.
- **Test the recovery plan:** Measure restoration, reboot behavior, and service availability before retiring the old deployment.

## Before You Begin

**Difficulty:** Intermediate. **Audience:** Proxmox administrators choosing between nested Docker and Docker in a VM. You should recognize a Compose project, a container mount, and a Linux shell prompt before following the diagnostic examples.

**Estimated effort:** Allow 30–60 minutes for inventory and evidence collection. Migration time depends on database size, storage throughput, hardware access, and the outage window you choose. The examples below are documented procedures and illustrative reasoning, not benchmarks from a lab operated for this article.

| Requirement | Why it matters |
|---|---|
| **Host console access** | Distinguishes network failure from a host-wide stall |
| **Current backups** | Provides a recovery path before changing the deployment |
| **Container and VM IDs** | Keeps host commands directed at the intended workload |
| **Application data inventory** | Identifies volumes, bind mounts, databases, and external dependencies |
| **Separate test environment** | Supports migration rehearsal without duplicate production writers |

## Watch the Source Video

{{< youtube id="XyPBHhZg0Ok" enable="true" title="Proxmox: The Hidden Danger of Running Docker Inside LXC" description="An explainer about Docker nested inside Proxmox LXC, intermittent host freezes, and a migration to Debian virtual machines" uploadDate="2026-09-15T17:00:09-07:00" >}}

**Source video:** [Proxmox: The Hidden Danger of Running Docker Inside LXC](https://www.youtube.com/watch?v=XyPBHhZg0Ok), published September 15, 2026, by *Proxmox x Kubernetes x Homelab x Backup*. The central question is useful: how much operational uncertainty accompanies a resource-saving architecture?

**Evidence boundary:** The video narrates an incident and proposes lessons. The sections below distinguish the owner’s observations, documented software behavior, and recommendations derived from them.

## What the Incident Establishes

The original report describes an **Intel Core i3-13100 and BIOSTAR H610MHP host**. The owner reported intermittent freezes affecting management access and LXC services. A connected display stopped responding, although the report explicitly says syslog continued producing output. This is more specific than treating the event as entirely log-free. [Original Proxmox forum report](https://forum.proxmox.com/threads/pve-host-freezes-every-2-3-weeks.185009/)

The owner later reported **improvement after migration**. In an August 3 follow-up, they described moving Docker workloads into Debian virtual machines and stopping the Docker-bearing LXCs. They reported no further freezes at the time of the update, while the video cites a 16-day stable period. Neither statement supplies a controlled reproduction or identifies a particular defective component. [Owner’s follow-up in the same thread](https://forum.proxmox.com/threads/pve-host-freezes-every-2-3-weeks.185009/)

| Observation | What it supports | What it does not establish |
|---|---|---|
| **Long initial uptime** | The earlier workload and software combination operated successfully | Reliability after every later update |
| **Host and services stall** | The outage extends beyond one application | Docker as the root cause |
| **Migration precedes improvement** | A useful operational workaround | Which changed interaction removed the trigger |
| **Sixteen stable days** | A bounded observation period | Resolution of every two-to-three-week failure pattern |

The **observation period** deserves scrutiny. Sixteen days falls inside a 14–21 day recurrence window. A longer observation period covering several former failure intervals, comparable workloads, and ordinary maintenance improves confidence, but still falls short of a controlled cause-and-effect demonstration.

**Operational success and root-cause proof** are separate outcomes. Restoring trusted household services is a valid reason to migrate. Describe the result as improved observed reliability until stronger evidence establishes the mechanism.

## Locate the Kernel Boundary

```text
Docker inside LXC:
Application -> Docker runtime -> LXC namespaces and policy
            -> Proxmox host kernel -> physical hardware

Docker inside a VM:
Application -> Docker runtime -> guest Linux kernel
            -> virtual hardware / KVM-QEMU
            -> Proxmox host kernel -> physical hardware
```

**LXC** uses the host kernel. Namespaces, control groups, capabilities, seccomp, and security profiles restrict processes without supplying a separate kernel. Adding Docker inside LXC creates another container-management layer around workloads using the same underlying host kernel. [LXC architecture and containment features](https://linuxcontainers.org/lxc/introduction/)

A **VM** introduces a guest kernel. A guest kernel failure normally affects its VM, while Proxmox continues managing the other guests. The VM still depends on the physical host, hypervisor, storage, and networking. Hardware failure or a host-kernel defect remains a shared dependency.

| Boundary | Docker inside LXC | Docker inside a VM |
|---|---|---|
| **Kernel used by applications** | Proxmox host kernel | Guest kernel |
| **Docker runtime environment** | Constrained by the outer container’s policy | Installed inside a conventional guest OS |
| **Guest kernel updates** | Tied to the host kernel | Managed inside the guest |
| **Physical host outage** | Stops dependent workloads | Stops dependent workloads |

A VM limits **some failure propagation**, not all of it. An application process crash inside LXC does not automatically crash Proxmox. Likewise, putting every household service into one Docker VM still groups those services behind one guest operating system and one maintenance schedule.

For the **broader conceptual comparison**, see [Docker containers versus virtual machines](/articles/docker-vs-vms/). Here, the decision concerns Docker’s placement within Proxmox and the resulting troubleshooting boundaries.

## Define Support Precisely

**“Unsupported”** needs a named component and version. Distinguish vendor-recommended deployment, documented features, distribution maintenance, and a contractual support entitlement. A working nested stack does not prove all its combinations receive equal testing, while a recommendation for VMs does not mean maintainers refuse every nesting-related bug.

**Current Proxmox documentation** adds an important distinction. Its container-toolkit source describes **Open Container Initiative (OCI)** application-image support as a technology preview, with images converted into the LXC framework. It also recommends containers inside a QEMU VM for requirements emphasizing isolation and live migration. Importing an OCI image into this framework differs from installing Docker Engine and running Compose inside an LXC guest. [Proxmox container-toolkit documentation](https://github.com/proxmox/pve-docs/blob/master/pct.adoc)

| Deployment | Question to verify |
|---|---|
| **Traditional LXC guest** | Does its OS template and application fit the documented container restrictions? |
| **Docker nested in LXC** | Which kernel, runtime, security-policy, and storage combinations have been tested? |
| **Native OCI image import** | Does the installed Proxmox version provide the documented feature and required behavior? |
| **Docker inside Debian VM** | Does the guest release meet Docker’s installation requirements? |

Docker publishes a **Debian installation path**. Use its supported-release list and repository instructions for the guest. Record the versions you deploy rather than assuming an older tutorial remains accurate. This provides a documented installation baseline, not a guarantee of uptime or an automatic paid-support contract. [Docker Engine on Debian](https://docs.docker.com/engine/install/debian/)

## A Confirmed Nesting Failure

The **2025 runc/AppArmor incompatibility** is a verifiable example. The runc maintainers documented a failure involving descriptor reopening inside an outer container with an AppArmor profile. AppArmor misinterpreted an access under **`/proc/sys`** as an access under **`/sys`**, causing a policy denial. [runc issue 4968](https://github.com/opencontainers/runc/issues/4968)

An **affected startup** reported this error fragment:

```text
open sysctl net.ipv4.ip_unprivileged_port_start file: reopen fd 8: permission denied
```

The recorded failure prevented **container startup**. It does not explain the forum owner’s host freezes. The issue records **`lxc-pve 6.0.5-2`** as a Proxmox fix for this specific problem, and the corresponding upstream LXC change merged on November 20, 2025. *Those are historical fix references, not a recommended package pin for a current installation.* [Maintainer’s fix summary](https://github.com/opencontainers/runc/issues/4968), [merged LXC change](https://github.com/lxc/lxc/pull/4609)

The lesson is **dependency coordination**. A runtime security change interacted with the outer container’s policy, and the fix required work in another layer. Prefer the appropriate maintained package update for your release over permanently disabling AppArmor or retaining an old vulnerable runtime.

> **Key takeaway:** This incident demonstrates a real nested-container compatibility problem and a real maintainer response. It establishes neither universal LXC instability nor the cause of a separate host lockup.

## Compare the Real Costs

Measure efficiency with your **actual workload**. Compare host memory pressure, CPU demand, storage latency, application response times, and recovery effort under equivalent conditions. Assigned VM RAM, guest free memory, and host resident memory represent different measurements.

| Claimed saving | Measurement to collect | Additional cost to record |
|---|---|---|
| **Lower memory overhead** | Host memory use and pressure during the same workload | Time spent managing nested limits and diagnosing contention |
| **Faster deployment** | Time to a working service with its data restored | Time to rebuild after a failed update |
| **Simpler hardware sharing** | Required devices, permissions, and successful application use | Host-driver dependency and migration constraints |
| **Easier backups** | A successful restore of all required data | External mounts and application consistency |

Docker documents **unrestricted CPU and memory use** by default unless constraints are applied. In an LXC deployment, the outer container adds its own limits. In a VM, the guest allocation adds another capacity boundary. A guest still needs capacity for its OS, Docker, caches, and peak application demand. [Docker resource constraints](https://docs.docker.com/engine/containers/resource_constraints/)

**Hardware access** is a workload requirement. Sharing a host graphics device with a container and assigning a PCI device to a VM involve different driver and isolation arrangements. List the exact device and application requirement before choosing. For example, a media workload requiring hardware decoding needs a successful decode test after migration, alongside ordinary HTTP health checks.

Avoid **universal overhead numbers**. This article supplies no fixed RAM penalty or performance percentage because those figures require a controlled workload, configuration, and measurement method. Use an observed result from your own comparison in the decision record below.

## Collect Evidence by Layer

**Begin on the Proxmox host**, using an administrative shell. Replace **`101`** with the LXC ID under investigation:

```bash
pveversion -v
uname -r
pct config 101
journalctl --list-boots
journalctl -k -b -1 --no-pager
```

**`pveversion -v`** records the installed Proxmox component versions. **`pct config`** records the outer container configuration. In **`journalctl`**, **`-k`** selects kernel messages, **`-b -1`** selects the previous boot, and **`--no-pager`** produces plain terminal output. Previous-boot messages require retained journal data. [Proxmox toolkit](https://github.com/proxmox/pve-docs/blob/master/pct.adoc), [systemd journalctl reference](https://github.com/systemd/systemd/blob/main/man/journalctl.xml)

**Then inspect the Docker host**, inside the LXC or VM running its daemon:

```bash
docker version
docker info
docker compose version
docker ps -a
docker stats --no-stream
```

Record **both environments**. The container image tag alone omits Docker, containerd, runc, the host kernel, security policy, and storage backend. Save the incident time, recent updates, and whether the local host console responded. Redact credentials and private application details before publishing diagnostic material.

**Inspect a specific workload**, replacing **`app`** with its container name:

```bash
docker inspect --format '{{json .State}}' app
docker inspect --format '{{.RestartCount}}' app
docker inspect --format '{{json .Mounts}}' app
```

**`docker inspect`** exposes state, restart count, and mount information for the named container. Treat a restart count as a clue to correlate with logs, not proof of a host-level defect. A recreated container also starts a new history. [Docker inspect reference](https://docs.docker.com/reference/cli/docker/inspect/)

## Distinguish Pressure From Lockups

**Capture Linux pressure information on the host** while the problem develops:

```bash
cat /proc/pressure/cpu
cat /proc/pressure/memory
cat /proc/pressure/io
```

**Pressure Stall Information**, or PSI, reports time lost while tasks wait for resources. Its **`some`** and **`full`** fields describe different stall conditions, while **`avg10`**, **`avg60`**, and **`avg300`** summarize recent intervals. Memory pressure differs from memory occupancy: a large cache alone does not establish a shortage. [Linux PSI documentation](https://docs.kernel.org/accounting/psi.html)

| Evidence | Useful interpretation | Next check |
|---|---|---|
| **One container repeatedly exits** | Application or container-runtime failure | Exit state, service logs, restart policy |
| **SSH fails, console works** | Network or management-path failure | Link state, NIC driver, bridge, firewall |
| **Memory PSI rises under load** | Tasks lose time to memory contention | Limits, reclaim activity, OOM records, workload growth |
| **Storage requests stall** | I/O dependency is delaying work | Device health, storage logs, latency and queueing |
| **Watchdog reports a lockup** | Kernel detector observed a defined stall condition | Full trace, kernel version, reproducible trigger |
| **No final log entry** | Evidence collection ended before useful output arrived | Persistent or external capture before recurrence |

A **Linux lockup report** has a technical meaning. Kernel watchdogs distinguish soft and hard lockup conditions. A browser timing out does not establish either condition, and a missing watchdog report does not prove the host remained healthy. [Linux lockup-detector documentation](https://docs.kernel.org/admin-guide/lockup-watchdogs.html)

**Firmware and power-state changes** are experiments. Record the previous setting, the reason for changing it, and the observation period. Disabling a CPU idle state changes power and thermal behavior, so a report involving another machine is insufficient evidence to prescribe the same setting universally.

## Preserve Useful Logs

**Persistent journaling** improves the chance of retaining evidence across a reboot. A journald configuration drop-in uses this setting:

```ini
[Journal]
Storage=persistent
```

**`Storage=persistent`** requests disk-backed journal storage when available. Configure retention limits and available disk capacity as part of the change, then verify earlier boots appear in **`journalctl --list-boots`**. Persistent logging still depends on the host completing writes before the failure. [systemd journald configuration](https://github.com/systemd/systemd/blob/main/man/journald.conf.xml)

**External observation** adds another perspective. Monitor the service from a different machine and record timestamps. A monitor running on the failing Proxmox host disappears during the same outage, reducing its value for distinguishing downtime from missing telemetry.

**Illustrative test:** Schedule a lightweight HTTP check from a separate system, then compare failures with host reachability and local-console behavior. An application timeout with a responsive host points to a different investigation than simultaneous application, management, and console failure. This is a diagnostic design, not an observed result from the source incident.

## Plan a Controlled Migration

Start with **one low-risk Compose project**. Prepare a Debian VM using a release listed in Docker’s installation documentation, establish backups, and configure resource allocations. Keep the original deployment available for rollback until the replacement passes its tests. [Docker’s Debian installation instructions](https://docs.docker.com/engine/install/debian/)

**Inventory the Compose project** from its working directory:

```bash
docker compose config --quiet
docker compose config --images
docker compose config --volumes
```

**`--quiet`** validates the configuration without printing it. **`--images`** lists referenced images, while **`--volumes`** lists named volumes. These commands do not export application data or provide a complete bind-mount inventory. Review the Compose file and each container’s mounts as well. [Docker Compose config reference](https://docs.docker.com/reference/cli/docker/compose/config/)

| Data or dependency | Migration action |
|---|---|
| **Compose definitions** | Transfer project files and retain the tested configuration |
| **Secrets and environment** | Recreate required values through the chosen secret-management process |
| **Named volumes** | Back up and restore their contents with application-consistent procedures |
| **Bind-mounted paths** | Transfer or reconnect the actual source data and verify ownership |
| **Databases** | Use the database’s supported backup/restore or quiesced-copy procedure |
| **Devices and shares** | Re-establish access and test application behavior |
| **Ports and DNS** | Stage the replacement address and plan the cutover |

**Volumes** outlive containers, but they do not migrate themselves. A Compose file names resources and defines services. Docker’s volume documentation describes separate backup and restore operations for persistent contents. Do not assume recreating the project restores its data. [Docker volume lifecycle and backups](https://docs.docker.com/engine/storage/volumes/)

Check **Proxmox backup coverage** separately. Its backup documentation excludes device and bind-mount contents from container backups. A successful backup of an LXC root filesystem therefore does not establish protection for every directory exposed inside it. [Proxmox backup documentation](https://github.com/proxmox/pve-docs/blob/master/vzdump.adoc)

### Check Storage Before Copying

**Inspect Docker’s actual storage configuration** on each Docker host:

```bash
docker info
findmnt -T /var/lib/docker
```

**`findmnt`** identifies the filesystem containing the specified path. Replace **`/var/lib/docker`** if your daemon uses a different data root, and inspect containerd’s storage path when applicable. Docker documents a distinction between the containerd image store and classic storage drivers, with backend-specific requirements. [Docker storage-backend selection](https://docs.docker.com/engine/storage/drivers/select-storage-driver/)

**Recreate images and restore application data** using the chosen backend’s documented procedures. Copying a live Docker data directory between different storage arrangements introduces additional assumptions about metadata, mount state, and consistency. It is a different operation from backing up a stopped application’s data volume.

### Cut Over With Rollback

1. **Rehearse restoration** in the VM using separate addresses and test data where appropriate.
2. **Stop production writes** during the agreed outage window and take the final consistent backup.
3. **Restore and validate** application data, permissions, credentials, and required hardware access.
4. **Switch service routing** after the replacement passes application-specific checks.
5. **Keep the original stopped** while retaining its configuration and recovery data.
6. **Document rollback handling** for data written after cutover before restarting the old system.

Avoid **two active writers** against the same database storage. A rollback involving new production data requires a plan for preserving or intentionally discarding those writes. Merely restarting an old container does not reconcile two diverging data histories.

## Test More Than Uptime

**Acceptance tests** should follow the service’s purpose. A green container status establishes a running process. A usable service also requires its data, network access, dependencies, and recovery behavior.

| Test | Evidence to retain |
|---|---|
| **Application function** | A successful real transaction, query, or media operation |
| **Data completeness** | Expected records, files, permissions, and recent changes |
| **Guest reboot** | Services return without manual repair |
| **Backup restoration** | The restored copy completes the same functional check |
| **Representative load** | Latency, CPU, memory pressure, and storage behavior |
| **Maintenance rehearsal** | A tested update and a usable recovery procedure |
| **Longer observation** | Availability records spanning several previous failure intervals |

**Worked decision:** A camera service and an experimental downloader currently share one nested stack. Moving both into one VM improves kernel separation but preserves a shared guest-maintenance boundary. If camera availability is the priority, evaluate separate maintenance groups and resource limits, then test recording continuity during downloader updates.

**Expected reasoning:** The best placement follows the service dependency you need to isolate. Two VMs on one physical server still share its power, storage, and host kernel. If the requirement includes surviving the server’s outage, the design needs an additional independent system or an acceptable manual fallback.

## Create Your Decision Record

**Use measured evidence** to choose a deployment and define when you will revisit it:

```text
Service and household impact:
Current host / kernel / LXC / Docker versions:
Required GPU, device, and network access:
Measured memory, CPU, storage, and latency:
Known failure signature and recurrence interval:
Backup coverage and successful restore evidence:
Chosen deployment and reason:
Permitted outage window and recovery target:
Cutover and post-cutover data rollback procedure:
Acceptance tests and observation period:
Condition requiring another architecture review:
```

**Choose LXC nesting deliberately** when its benefits justify the integration work and you have tested the recovery path. Choose a VM when a conventional Docker guest environment and a separate guest kernel simplify the service’s operation. Neither decision substitutes for backups, monitoring, and host maintenance.

## Next Steps

**Inventory one service** first. Identify its persistent data, physical dependencies, failure symptoms, and recovery target. Rehearse a restore before deciding whether a migration is necessary.

For **related work**, use the [Proxmox VE upgrade guide](/articles/proxmox-ve-8-to-9-upgrade-guide/) for upgrade planning and the [Docker and Kubernetes security guide](/articles/how-to-secure-your-docker-and-kubernetes-environment/) for workload hardening. Keep architecture selection, upgrade execution, and incident diagnosis as distinct decisions with their own evidence.

## Sources and Evidence

**Research checked:** September 16, 2026. The supplied transcript informed the topic. The video metadata, original incident report, upstream issue, and official documentation were checked separately. Illustrative exercises and proposed validation steps are labeled in the text.

| Source | Role |
|---|---|
| **[Source video](https://www.youtube.com/watch?v=XyPBHhZg0Ok)** | Original explainer and its reported stability interval |
| **[Proxmox incident thread](https://forum.proxmox.com/threads/pve-host-freezes-every-2-3-weeks.185009/)** | First-person observations and migration follow-up |
| **[Proxmox container toolkit](https://github.com/proxmox/pve-docs/blob/master/pct.adoc)** | Container architecture and current OCI distinction |
| **[runc issue 4968](https://github.com/opencontainers/runc/issues/4968)** | Documented startup failure and historical package fix |
| **[LXC pull request 4609](https://github.com/lxc/lxc/pull/4609)** | Merged upstream AppArmor change |
| **[Docker documentation](https://docs.docker.com/engine/install/debian/)** | Guest installation baseline, with specific runtime and storage references linked above |
| **[Linux PSI documentation](https://docs.kernel.org/accounting/psi.html)** | Resource-pressure interpretation |
| **[Linux watchdog documentation](https://docs.kernel.org/admin-guide/lockup-watchdogs.html)** | Defined kernel lockup conditions |
| **[Proxmox backup documentation](https://github.com/proxmox/pve-docs/blob/master/vzdump.adoc)** | Container mount exclusions and backup behavior |
