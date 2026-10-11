---
title: "Proxmox VM Backup Restore Drill: Prove the Guest Works"
date: 2026-10-11
lastmod: 2026-10-11
toc: true
draft: false
description: "Test a Proxmox VM backup with an isolated restore. Check disk coverage, backup mode, guest data, service health, and recovery time without touching production."
genre: ["Virtualization", "Backup and Recovery", "Home Lab"]
tags: ["Proxmox backup restore test", "Proxmox VM backup", "Proxmox restore drill", "qmrestore", "vzdump", "Proxmox Backup Server verification", "Proxmox snapshot backup", "VM recovery test", "backup RPO RTO", "isolated VM restore", "Proxmox backup mode", "guest agent backup"]
cover: "/img/cover/proxmox-vm-backup-restore-drill.webp"
coverAlt: "A backup moves from an orange production VM through a storage vault to a blue isolated test VM with disk, service, and time checks."
coverCaption: "A completed backup job is the start of a recovery test."
---

A green backup task tells you Proxmox wrote a backup. The task does not show whether the guest boots, its data is recent, or its main service works. **Restore a copy under a new VM ID on an isolated network.** The result gives you evidence for recovery before an outage forces the test.

This drill covers one **Proxmox VE virtual machine**. Containers have different backup rules, especially for bind and device mounts. The site's [homelab backup restore drill](/articles/homelab-backup-restore-drill/) covers broader file recovery. Here, you will test a Proxmox VM backup and its workload.

## Key Takeaways

- **Define success first:** Name a data item, a service check, and an acceptable recovery time.
- **Inspect coverage:** A VM backup skips disks marked **No backup** and cannot recreate external services or omitted data.
- **Restore separately:** Use an unused VM ID and keep the restored network isolated from production.
- **Record evidence:** Measure backup age, restore time, boot, disk presence, and a real application check.

## Before You Begin

Choose a VM whose backup is safe to test. You need Proxmox administrator access, a completed backup on file storage or Proxmox Backup Server (PBS), enough space for a second VM, and an isolated bridge or disconnected network device. Keep the production VM running. Reserve a new VM ID, such as **920**, after checking whether another guest uses the ID. Plan enough time for a full restore and a workload test.

Write the pass condition before restoring. For a file server, pick a recent file and its expected checksum or contents. For a database, pick a safe read query and a record written before the backup. For a web service, pick a local health check and a representative page. Record the latest acceptable data timestamp, your **recovery point objective (RPO)**, and the time allowed to restore service, your **recovery time objective (RTO)**. A boot screen alone does not meet these checks.

| Record | Example evidence |
|---|---|
| Backup point | Snapshot time and the last expected data item |
| Recovery target | Unused VM ID, target storage, isolated bridge |
| Workload test | Login, volume mount, and application read |
| Time limit | Start and finish time of the restore and service check |

Do not attach the restored guest to the production network before reviewing its name, IP address, MAC address, scheduled jobs, and external integrations. A copied identity might conflict with the running VM or send duplicate work.

## Inspect What the Backup Covers

On a Proxmox node, the following read-only command shows the source VM configuration. Replace **120** with your source VM ID:

```bash
qm config 120
```

List every virtual disk and its backup setting. Proxmox's [VM disk documentation](https://github.com/proxmox/pve-docs/blob/master/qm.adoc) says the **No backup** option excludes a disk from VM backup. Check whether application data sits on an excluded disk, a host mount, passed-through hardware, or a remote service. Record its separate recovery procedure. A VM boot test does not prove excluded data is protected.

Check the latest backup's timestamp, size, task log, and storage location. In the Proxmox interface, open the backup storage's **Backups** view or the VM's **Backup** tab. Confirm the job ended without errors. Proxmox's [backup documentation](https://github.com/proxmox/pve-docs/blob/master/vzdump.adoc) distinguishes regular backup files from PBS storage, which keeps deduplicated chunks and metadata.

| Backup mode | VM behavior | Decision for this drill |
|---|---|---|
| **Snapshot** | Backs up a running VM with low downtime. Guest writes introduce a small consistency risk. | Suitable for routine tests when the workload tolerates this recovery point. |
| **Stop** | Shuts down the guest for the backup start and gives the strongest consistency. | Use when the workload requires a clean shutdown and the downtime is acceptable. |
| **Suspend** | Suspends before snapshot mode and adds downtime without a general consistency benefit. | Avoid selecting suspend as a default improvement over snapshot. |

These mode tradeoffs come from [Proxmox's backup mode reference](https://github.com/proxmox/pve-docs/blob/master/vzdump.adoc). A running guest with its QEMU guest agent enabled and healthy supports filesystem freeze and thaw during snapshot backup. Filesystem freeze improves consistency but does not replace a database-specific recovery check. Record the actual mode and guest-agent state instead of assuming a scheduled job uses your preferred settings.

## Create or Select a Recovery Point

Use a recent successful scheduled backup if the drill tests routine recovery. If you need a fresh one-time backup, select the VM's **Backup** tab, choose **Backup now**, set the target storage and mode, and wait for the task log to report success. From a Proxmox shell, this example backs up VM **120** to a storage ID named **backup-nfs** in snapshot mode:

```bash
vzdump 120 --storage backup-nfs --mode snapshot
```

Replace both IDs with your own. Run the command only after confirming the storage accepts backups and has room for the job. The [Proxmox `vzdump` reference](https://github.com/proxmox/pve-docs/blob/master/vzdump.adoc) documents the mode and storage options. Check the task log after the command returns. Do not treat an old backup as a current recovery point because its filename looks recent.

If the target is **PBS**, run or inspect a verification job for the selected datastore. PBS [verification documentation](https://pbs.proxmox.com/docs/maintenance.html) explains how to verify backup data integrity and schedule repeated checks. Verification finds damaged backup chunks. **A clean verification does not prove a restored operating system, application, or external dependency works.** Continue with the restore drill even after a clean verification result.

## Restore to an Isolated VM

In the Proxmox interface, select the backup under the storage's **Backups** view and choose **Restore**. Enter an unused VM ID and the intended target storage. Leave **Start after restore** off. Review the option for generating a new MAC address. The [official `qmrestore` synopsis](https://github.com/proxmox/pve-docs/blob/master/generated/qmrestore.1-synopsis.adoc) defines a unique VM ID, the storage choice, `--unique` for a random Ethernet address, and the default of not starting the restored VM.

For a file-based `vzdump` archive, this shell command shows the equivalent pattern. Replace the archive path, new VM ID, and storage ID with values from your environment:

```bash
qmrestore /path/to/vzdump-qemu-120-2026_10_11-02_00_00.vma.zst 920 --storage local-lvm --unique 1
```

The [Proxmox restore description](https://github.com/proxmox/pve-docs/blob/master/qmrestore.adoc) says a restore without a target storage tries the original storage. Set **`--storage`** when the old storage does not exist on the test node. Do not use **`--force`** for a drill. The option permits overwriting an existing VM, while this procedure requires an unused ID. PBS backups also restore through the Proxmox interface. Select the storage entry for the PBS snapshot rather than treating the snapshot as a local `.vma.zst` file.

Before first boot, inspect the restored VM's hardware and **Network Device**. Disconnect the adapter or attach the adapter to an isolated bridge without a path to production. If the workload needs another test service, provide a test copy on the isolated network. Compare disk mappings, firmware, virtual TPM requirements, and any special devices with the source. External disks, passed-through devices, and secrets stored outside the VM need separate plans.

## Test the Guest and Workload

Start the restored VM and use its console first. Confirm the operating system boots, all expected volumes mount, the clock is sane, and the application starts. Then run the pass condition written earlier. Compare a known data item with its pre-backup value and timestamp. A login prompt or running process alone does not show the service holds the right data.

| Test | Pass condition |
|---|---|
| **Boot** | Guest reaches a normal login without repair mode or repeated recovery prompts. |
| **Disks** | Every disk included in the backup appears, mounts, and holds expected data. |
| **Service** | A representative local request or read succeeds. |
| **Recovery point** | The restored data meets the recorded RPO. |
| **Recovery time** | Restore plus boot and service validation meets the recorded RTO. |
| **Isolation** | No production address, job, or integration receives duplicate traffic. |

Keep the restored guest isolated while you inspect scheduled tasks, notification hooks, backup agents, and application credentials. Do not run a test sending live customer messages or writing to production services. If a check fails, record the exact stage. Separate **backup integrity failure**, **VM boot failure**, **missing data**, and **application failure**. Each points to a different repair.

Proxmox offers [single-file restore for PBS backups](https://github.com/proxmox/pve-docs/blob/master/vzdump.adoc). Use single-file restore to test a file recovery path when your workload needs one. A recovered file still does not replace a full VM boot and service test. Proxmox also offers live restore from PBS. Its documentation says a failed live restore leaves the VM in an undefined state, so use the normal completed restore for this planned drill.

## Record the Result and Close the Drill

Record the source VM ID, backup storage, backup timestamp, backup mode, new VM ID, target storage, network isolation, restore start and finish times, application test, data timestamp, and any failed checks. Compare the measured recovery point and time with your targets. A failure is useful evidence only if you change the backup plan and repeat the drill.

Shut down the restored VM when testing ends. Remove its test copy only after saving the result, and verify the production VM still runs as expected. Keep the backup under your normal retention policy. Do not change retention merely to make one drill pass.

Repeat the test after major storage, guest, or backup configuration changes. Rotate through important VMs, including guests with excluded disks or external dependencies. The [Hyper-V to Proxmox migration guide](/articles/hyper-v-to-proxmox-migration-checklist/) uses this recovery proof before retiring a source VM. **A usable backup has a known restore path, a tested workload, and a measured recovery point.**
