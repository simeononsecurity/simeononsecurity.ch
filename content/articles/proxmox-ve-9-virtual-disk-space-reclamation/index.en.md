---
title: "Proxmox VE 9: Minimize Virtual Disk Usage and Reclaim Space"
date: 2026-11-09
lastmod: 2026-11-09
toc: true
draft: false
description: "Reduce Proxmox VE 9 VM and LXC storage use. Compare disk formats and storage backends, enable discard, trim Windows and Linux guests, and check snapshots before reclaiming space."
genre: ["Virtualization", "Linux Administration", "Proxmox", "Storage", "Homelab"]
tags: ["Proxmox VE 9 disk space", "Proxmox thin provisioning", "Proxmox discard", "Proxmox trim", "Proxmox Windows ReTrim", "Proxmox Linux fstrim", "Proxmox LXC disk usage", "Proxmox LVM thin", "Proxmox ZFS sparse", "Proxmox Ceph RBD", "Proxmox qcow2", "Proxmox raw disk", "Proxmox snapshots", "virtual disk reclaim", "Proxmox storage types", "VirtIO SCSI", "Proxmox detect zeroes", "Proxmox backup storage"]
cover: "/img/cover/proxmox-ve-9-virtual-disk-space-reclamation.webp"
coverAlt: "Two block grids linked by an arrow show used virtual disk blocks and free capacity in a storage pool."
coverCaption: "Guest deletion, discard, and storage reclamation are separate steps."
---

**A smaller guest filesystem does not always mean a smaller Proxmox storage bill.** Freeing host space requires a thin-capable disk, a working discard path for VMs, and a backing store free of blocks retained by snapshots. This guide covers the settings and checks for Proxmox VE 9 VMs and LXC containers.

<!--more-->

## Key Takeaways

- **Choose the backing store first.** A virtual disk's advertised size differs from its allocated host space only when its image format or storage backend supports thin provisioning.
- **Enable VM discard, then trim inside the guest.** Windows ReTrim and Linux `fstrim` send unused-block requests through the virtual disk.
- **Check snapshots and backups separately.** Old blocks stay allocated while a snapshot references them. Backup files and PBS chunks follow their own retention rules.
- **Treat LXC mounts by type.** Managed rootfs and mount-point volumes, bind mounts, and device mounts have different ownership and backup behavior.

## Before You Begin

You need **Proxmox VE 9 administrator access**, a verified backup of each affected guest, and enough free pool space for the operation. Record each guest's ID, disk bus, volume ID, storage ID, snapshots, and current allocation before changing settings. Use the [VM restore drill](/articles/proxmox-vm-backup-restore-drill/) to test recovery.

**Estimated time:** 20 to 60 minutes per guest, plus any large trim or cleanup job. **Difficulty:** Intermediate. Start with one low-risk VM and compare its storage use before and after.

> **Warning:** A full thin pool produces guest I/O errors and risks filesystem damage. Do not overcommit capacity without monitoring the pool's free data and metadata space. [Proxmox storage documentation](https://github.com/proxmox/pve-docs/blob/master/pvesm.adoc)

## Follow the Allocation Chain

**Deletion**, **discard**, and **reclamation** occur at different layers. A guest deletes a file and marks filesystem blocks free. Its filesystem sends TRIM or UNMAP for those blocks. QEMU forwards the request when the virtual disk has discard enabled. The storage backend releases physical allocation if its format and pool support the operation. [Proxmox VM disk documentation](https://github.com/proxmox/pve-docs/blob/master/qm.adoc)

| Layer | What to check | Useful evidence |
|---|---|---|
| **Guest files** | Filesystem free space | Windows volume properties or Linux `df -h` |
| **Virtual disk** | Bus, discard, SSD emulation, image format | VM **Hardware** tab or `qm config VMID` |
| **PVE volume** | Owner and configured size | Storage **Content** tab or `pvesm list STORAGE_ID` |
| **Storage pool** | Free data, metadata, and retained blocks | `pvesm status` and backend-specific tools |

**A 100 GiB virtual disk is a capacity limit, not a promise of 100 GiB allocated.** Conversely, a guest reporting 20 GiB in use does not prove the host uses 20 GiB. Metadata, snapshots, backup copies, and previously written blocks alter the figure. [Proxmox storage documentation](https://github.com/proxmox/pve-docs/blob/master/pvesm.adoc)

## Compare Disk Formats

**The storage backend decides which image formats Proxmox offers.** ZFS zvols and Ceph RBD use raw virtual disks. LVM normally uses raw, with a Proxmox VE 9 volume-chain exception described below. File backends such as directory and NFS storage support raw or qcow2. Raw does not provide thin allocation or snapshots by itself. The underlying storage needs to supply those features. Qcow2 supplies copy-on-write allocation and snapshots at the image layer. [Proxmox VM disk documentation](https://github.com/proxmox/pve-docs/blob/master/qm.adoc)

| Format | Allocation mechanism | Space tradeoff |
|---|---|---|
| **qcow2 on file storage** | Qcow2 allocates clusters as written | Image metadata and snapshot chains consume space |
| **raw file on file storage** | Filesystem sparse-file behavior, where supported | Raw alone does not supply thin provisioning or snapshots |
| **raw block volume** | LVM thin, ZFS, Ceph RBD, or another backing store | Pool allocation and snapshots depend on the backend |

**Proxmox VE 9 thick LVM has a special snapshot mode.** `snapshot-as-volume-chain` uses qcow2 backing relationships across thick LVM logical volumes. It does not use qcow2 internal snapshots. The option affects only newly created VM disks and remains a technology preview in the current Proxmox documentation. Each snapshot looks fully allocated to PVE. Actual SAN allocation is smaller only when the backing storage supports thin provisioning and discard. [Proxmox LVM storage documentation](https://github.com/proxmox/pve-docs/blob/master/pve-storage-lvm.adoc)

**Do not convert a disk solely because its extension is `.raw`.** First check the storage plugin and its allocated blocks. A raw disk on `local-lvm` has different allocation behavior from a fully allocated raw file on ordinary directory storage.

## Compare Storage Types

Proxmox separates **file storage** from **block storage**. The storage plugin also controls snapshots, clones, sharing, and the content types accepted on each pool. Check the storage's **Datacenter > Storage** entry before relying on a format or feature. [Proxmox storage type table](https://github.com/proxmox/pve-docs/blob/master/pvesm.adoc)

| Storage | VM disk behavior | Reclaim check |
|---|---|---|
| **Directory, ext4, XFS** | Raw or qcow2 files | Compare `du` allocated bytes with image virtual size. Check snapshots if another storage layer provides them. |
| **NFS, CIFS** | Raw or qcow2 files on shared storage | Check the server's allocated space. A guest trim result alone does not prove server space fell. |
| **LVM thin (`local-lvm`)** | Thin raw logical volumes, local only | Watch thin-pool data and metadata percentages with `lvs`. |
| **Thick LVM** | Raw LVs or VE 9 qcow2 volume chains | Guest deletion does not reduce a fixed LV reservation. Check SAN thin allocation separately. |
| **ZFS (`local-zfs`)** | Raw zvols or container subvolumes | Check `sparse`, dataset properties, pool use, and snapshots. |
| **Ceph RBD** | Thin raw RBD images on shared storage | Check Ceph pool capacity, image use, snapshots, and discard behavior. |
| **Btrfs** | File-backed volumes with Btrfs subvolumes for raw images | Treat the PVE Btrfs plugin as a technology preview and inspect snapshots and filesystem usage. |

**Other storage plugins serve different roles.** CephFS provides shared file storage. iSCSI and Fibre Channel expose shared block devices, often divided into VM volumes with LVM. ZFS over iSCSI uses remote ZFS-backed block storage. Proxmox Backup Server (PBS) stores backups, not active VM disks. Check the **Content** types enabled for each storage before placing `images`, `rootdir`, `backup`, or `iso` data there. [Proxmox storage type table](https://github.com/proxmox/pve-docs/blob/master/pvesm.adoc)

**File-storage allocation flags matter at creation time.** The storage-level `format` default chooses `raw`, `qcow2`, or `vmdk` where supported. The `preallocation` setting for raw and qcow2 files accepts `off`, `metadata`, `falloc`, or `full`. The default is `metadata`, treated as `off` for raw. `full` reserves file space up front, which defeats the usual small initial footprint. Check the storage configuration before creating a large disk. The storage-level `shared` flag only declares existing shared access. It does not make local storage shared. [Proxmox common storage properties](https://github.com/proxmox/pve-docs/blob/master/pvesm.adoc)

**ZFS `sparse` is the storage setting for thin zvol creation.** Without sparse zvols, creation reserves capacity according to the configured volume behavior. Inspect the actual storage configuration and pool before changing an existing deployment. [Proxmox ZFS storage documentation](https://github.com/proxmox/pve-docs/blob/master/pve-storage-zfspool.adoc)

**Directory storage needs a second check.** A qcow2 file's logical length is not its guest-visible virtual capacity. `du -h` reports filesystem blocks allocated to the image file. `ls -lh` shows the image file's logical length. For a stopped VM, `qemu-img info` reports virtual capacity and host disk size. On NFS, trust the server's accounting for final capacity decisions. [QEMU `qemu-img` reference](https://www.qemu.org/docs/master/tools/qemu-img.html)

**NFS has another allocation boundary.** Qcow2 reusing an empty cluster inside its own file differs from an NFS server freeing file blocks. Hole punching needs support across the client, negotiated protocol, server, and server filesystem. NFSv4.2 defines `DEALLOCATE`, but a version number alone does not prove the server returned space. Inspect the negotiated NFS mount and measure allocation on the server. [NFSv4.2 `DEALLOCATE` specification](https://www.rfc-editor.org/rfc/rfc7862.html#section-6.2.2)

## Set the VM Disk Flags

In the Proxmox interface, open **VM > Hardware > Hard Disk > Edit**. Inspect the disk's bus and advanced options. The following flags affect allocation or determine whether an optimization is useful. The [official `qm` option reference](https://github.com/proxmox/pve-docs/blob/master/generated/qm.conf.5-opts.adoc) lists bus-specific availability.

| Bus | Space-related choice |
|---|---|
| **IDE** | Legacy compatibility. Use only when the guest lacks a newer driver. |
| **SATA** | Widely supported emulation. Verify guest trim and disk options before relying on reclaim. |
| **SCSI with VirtIO SCSI** | Preferred modern path for discard and per-disk settings. Windows needs the VirtIO driver. |
| **VirtIO Block** | Paravirtualized disk. Linux discard requires kernel 5.0 or newer. SSD emulation is unavailable. |

| Setting | Effect | Guidance |
|---|---|---|
| **Discard `on`** | Forwards guest TRIM or UNMAP | Required for guest-driven reclaim on a supported thin backend. The default `ignore` blocks forwarding. |
| **SSD emulation `ssd=1`** | Presents the disk as an SSD to the guest | Some guests need this identity before issuing trim. The flag does not make physical storage faster. VirtIO Block lacks this flag. |
| **Detect zeroes `detect_zeroes=1`** | Detects and tries to optimize zero writes | Optional I/O optimization. It does not replace guest trim or guarantee reclaimed space. |
| **Bus: SCSI / VirtIO SCSI single** | Exposes a SCSI disk through the VirtIO controller | A practical default for modern Windows and Linux guests. Install Windows VirtIO drivers. |
| **Bus: VirtIO Block** | Uses the VirtIO block device | Linux discard needs kernel 5.0 or newer. SSD emulation is unavailable. |
| **I/O thread `iothread=1`** | Assigns drive I/O to a separate thread | Use with VirtIO Block or SCSI on a VirtIO SCSI single controller. It is a performance setting, not a reclaim switch. |
| **Cache and AIO** | Change I/O buffering and asynchronous I/O | Tune for workload and backend behavior. Neither setting shrinks a disk. |
| **Backup `backup=0`** | Excludes the disk from VM backups | Reduces backup scope and removes its data from VM backup recovery. Document a separate backup. |
| **Replicate `replicate=0`** | Excludes the disk from storage replication | Reduces replicated data and removes the disk from the replica. |

**Other drive options describe behavior rather than reclaim.** `format` applies when allocating a disk on a backend with multiple image formats. `size` is the virtual capacity, not allocated bytes. `ro=1` makes a disk read-only. `snapshot=1` enables QEMU's temporary snapshot mode, which discards disk changes when the VM shuts down. It is not the switch for including a disk in Proxmox VM snapshots. Avoid it for persistent data. Check recovery coverage before using `backup=0` or `replicate=0`. [Proxmox VM disk options](https://github.com/proxmox/pve-docs/blob/master/generated/qm.conf.5-opts.adoc)

**Do not paste a shortened `qm set --scsi0` string over an existing drive.** Inspect **`qm config VMID`** and preserve the full volume ID and existing options when editing it. An abbreviated drive assignment risks dropping other per-disk settings. In the GUI, verify the saved disk options after each change.

```bash
qm config 100
pvesm status
```

The `100` is an example VM ID. For a **new** 64 GiB SCSI disk on an existing VM whose controller is **VirtIO SCSI single** and whose guest has the required driver, this command shows the allocation syntax. Replace both the VM ID and storage ID with your own values.

```bash
qm set 100 --scsi0 local-lvm:64,discard=on,ssd=1,iothread=1
```

**Check for an existing `scsi0` before using the example.** The command changes the slot. Use the GUI for an existing disk when preserving its exact option string is easier. See the [Proxmox `qm` command reference](https://github.com/proxmox/pve-docs/blob/master/generated/qm.1-synopsis.adoc).

## Reclaim Space in Windows

**Free guest files first.** Review Windows Storage settings, temporary files, old installers, application caches, and the recycle bin. Run application cleanup through its own interface for databases and container runtimes. Deleting active application data solely to reduce allocation risks data loss.

**Confirm the volume uses a discard-capable virtual disk**, then run an elevated PowerShell session in the Windows VM:

```powershell
fsutil behavior query DisableDeleteNotify
Optimize-Volume -DriveLetter C -ReTrim -Verbose
```

`DisableDeleteNotify = 0` indicates Windows has delete notifications enabled for the reported filesystem. **ReTrim** resends trim requests for currently unused volume regions. A successful command confirms the guest issued the operation, not the number of host bytes recovered. Check the host after the job finishes. [Microsoft `Optimize-Volume` reference](https://learn.microsoft.com/en-us/powershell/module/storage/optimize-volume?view=windowsserver2025-ps) and [Proxmox VM disk documentation](https://github.com/proxmox/pve-docs/blob/master/qm.adoc)

**Do not confuse the QEMU guest agent with TRIM.** The agent supports guest control and backup consistency features. Filesystem delete notifications travel through the virtual disk path. Installing the agent alone does not reclaim blocks. [Proxmox VM guest agent documentation](https://github.com/proxmox/pve-docs/blob/master/qm.adoc)

## Reclaim Space in Linux

**Check the block path and filesystem before trimming.** A modern distribution often runs a periodic `fstrim.timer`. Inspect its state, then trim mounted filesystems after deleting unneeded guest data.

```bash
lsblk -D
systemctl status fstrim.timer
sudo fstrim -av
```

**`lsblk -D`** reports discard granularity and limits for visible block devices. **`fstrim -av`** trims mounted filesystems where supported and reports submitted ranges. Submitted bytes do not equal bytes returned to the pool. Encrypted, LVM, RAID, and other stacked devices need discard support at each layer. [Red Hat unused-block guidance](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/8/html/managing_file_systems/discarding-unused-blocks_managing-file-systems)

Use a scheduled trim or a deliberate online discard policy. **Do not enable continuous `discard` on every filesystem as a substitute for checking the storage path.** Once the guest has trimmed, inspect the PVE volume and pool. Check a database or service's own compaction policy if deleted records still occupy its files.

## Handle LXC Separately

**LXC has no emulated VM disk bus for its root filesystem.** Start with `pct config CTID` and identify every `rootfs` and `mpN` entry. Proxmox defines storage-backed mounts, bind mounts, and device mounts. A path visible inside the container does not establish which host volume owns its blocks. [Proxmox container mount points](https://github.com/proxmox/pve-docs/blob/master/pct.adoc)

```bash
pct config 101
pct exec 101 -- df -h
pvesm status
```

For a **managed rootfs or mount point**, remove files through the container or its application, then inspect the backing volume and snapshots on the host. **Do not run VM `qm` discard commands against a CT.** On ZFS subvolumes, snapshots retain deleted blocks. On directory and thin-LVM storage, check the actual backing allocation rather than the configured CT size.

Run **`pct fstrim` on the Proxmox host** after CT cleanup when the backing storage supports discard. Proxmox trims the CT rootfs and eligible managed mount points. It skips bind mounts and read-only mount points. Use `--ignore-mountpoints` to trim only the rootfs. Compare backing storage use before and after. [Proxmox `pct fstrim` reference](https://github.com/proxmox/pve-docs/blob/master/generated/pct.1-synopsis.adoc)

```bash
pct fstrim 101
pct fstrim 101 --ignore-mountpoints 1
```

The commands show **alternative scopes** for example CT ID `101`. Run one scope for your storage layout. A successful trim does not promise equal bytes freed when snapshots retain old blocks.

**Bind and device mounts are unmanaged by Proxmox.** Their source data remains on the host or external device. Container `vzdump` backups exclude their contents. Storage-backed additional mount points are also excluded from backups by default unless their `backup` option includes them. Check the mount's actual backup policy before cleanup. [Proxmox backup documentation](https://github.com/proxmox/pve-docs/blob/master/vzdump.adoc)

For nested Docker, inspect image layers, volumes, and logs inside the actual storage owner before using Docker cleanup commands. The [Docker in LXC reliability guide](/articles/docker-in-lxc-proxmox-reliability/) covers mount and backup boundaries. Removing a container image does not remove a persistent volume by default.

## Measure the Host Correctly

**Record the same measurements before and after cleanup.** A storage pool's free space is the final capacity signal. Use volume-level figures to locate the guest responsible for growth.

```bash
pvesm status
pvesm list local-lvm
qm config 100
pct config 101
```

**`pvesm list` inventories managed volumes and configured sizes.** It does not measure allocated bytes on thin storage. For **directory storage**, inspect the exact mounted path and one known image file. Substitute the paths from **Datacenter > Storage** and the VM configuration.

```bash
df -hT /var/lib/vz
du -h /var/lib/vz/images/100/vm-100-disk-0.qcow2
ls -lh /var/lib/vz/images/100/vm-100-disk-0.qcow2
```

For a **stopped VM**, compare the image's virtual capacity and host allocation without modifying the file:

```bash
qemu-img info /var/lib/vz/images/100/vm-100-disk-0.qcow2
```

For **LVM thin**, watch both pool data and metadata:

```bash
lvs -a -o lv_name,vg_name,lv_size,data_percent,metadata_percent,segtype
```

For **ZFS**, separate live dataset data from snapshot-held data:

```bash
zpool list
zfs list -o name,used,available,referenced,usedbysnapshots -r POOL_OR_DATASET
zfs list -t snapshot -o name,used,referenced,written -r DATASET
```

**`usedbysnapshots`** reports blocks retained across all snapshots for a dataset. Snapshot `used` figures are not additive because snapshots share blocks. A deleted file might leave pool usage unchanged until every snapshot referencing its blocks expires or is removed under your retention policy. [OpenZFS snapshots and clones](https://openzfs.github.io/openzfs-docs/Basic%20Concepts/Datasets/Snapshots%20and%20Clones.html)

For **Ceph RBD**, map the Proxmox volume ID before running Ceph commands. **`qm config VMID`** shows `STORAGE_ID:IMAGE`. Open the RBD entry under **Datacenter > Storage** to find its **pool** and optional **namespace**. The storage ID need not match the pool name. Build `POOL/IMAGE` from the pool and image values. Run these commands on a client configured for the intended Ceph cluster with valid credentials. [Proxmox RBD storage documentation](https://github.com/proxmox/pve-docs/blob/master/pve-storage-rbd.adoc)

```bash
ceph df
rbd du POOL/IMAGE
rbd snap ls POOL/IMAGE
```

**`rbd du`** reports provisioned and actual image usage, including associated snapshots. Without the `fast-diff` image feature, it queries OSDs for potential objects and takes more work. **`ceph df`** shows pool and cluster capacity. Replication, erasure coding, and snapshots affect raw cluster use, so image bytes and pool bytes differ. [Ceph RBD command reference](https://docs.ceph.com/en/squid/man/8/rbd/) and [Ceph pool usage guidance](https://docs.ceph.com/en/squid/rados/operations/monitoring/)

If the RBD storage uses a namespace, add **`--namespace NAMESPACE`** to each `rbd` command. Use the namespace configured on the Proxmox storage entry, not the Proxmox storage ID.

## Account for Snapshots and Backups

**Snapshots preserve old block versions.** Review a VM or CT's **Snapshots** tab and its backend's snapshot inventory when usage fails to fall after trim. Inspect snapshot ownership and dependencies before deleting one. A backup is a separate copy and follows backup storage retention, not the guest's current `df` result.

**PBS deduplication changes the accounting.** Its datastore holds chunks shared across backups. Pruning removes backup snapshot metadata. Garbage collection later removes unreferenced chunks, subject to a grace period. Check both tasks before claiming recovered backup capacity. [PBS maintenance documentation](https://pbs.proxmox.com/docs/maintenance.html)

> **Warning:** Never delete a Proxmox-managed volume file, zvol, or snapshot by guessing from its name. Identify the guest and retention policy first. A storage cleanup task must preserve the backup and rollback path.

## Offline Image Rebuilds

**Use an offline conversion only when ordinary guest trim and the backend path do not solve a qcow2 allocation problem.** Shut the VM down, verify its backup, identify all snapshot and backing-chain relationships, and write a separate destination image. QEMU warns against modifying an image in use by another process. [QEMU `qemu-img` documentation](https://www.qemu.org/docs/master/tools/qemu-img.html)

**Prefer a Proxmox-managed move or backup and restore workflow** when the disk has snapshots or lives on managed block storage. A standalone `qemu-img convert` against a PVE-owned image does not update VM configuration, volume ownership, or snapshot references by itself. Do not use `qemu-img resize --shrink` to reclaim deleted files. Shrinking reduces the guest-visible capacity and risks truncating data if partitions and filesystems were not shrunk first.

## Troubleshoot a Failed Reclaim

| Symptom | Likely check | Next action |
|---|---|---|
| **Guest `df` falls, host stays flat** | VM discard flag, guest trim, snapshots | Verify the full discard path and retained snapshots. |
| **`fstrim` says unsupported** | Guest disk bus, stacked block devices, backend | Inspect `lsblk -D`, guest kernel, and each intervening layer. |
| **Windows ReTrim finishes, host stays flat** | Backend allocation, snapshots, server accounting | Compare volume and pool use. Confirm the disk uses thin storage. |
| **`ls -lh` and `du -h` differ** | Sparse or qcow2 file | Use `du` for allocated filesystem blocks. |
| **LVM thin pool stays high** | Data, metadata, snapshots | Check `lvs` and PVE snapshots before any removal. |
| **ZFS pool stays high** | Snapshot-held blocks and reservations | Check `usedbysnapshots`, zvol settings, and pool capacity. |
| **CT `df` and pool disagree** | Bind mounts, mount points, snapshots | Map `rootfs` and each `mpN` to its host owner. |

**Recheck after background work finishes.** Storage accounting might lag a trim, snapshot deletion, or backend garbage collection. Compare measured pool free space with your starting value. Do not infer success from a guest command's exit code alone.

## Next Steps

**Create a storage record for each guest:** virtual size, allocated bytes, backend, bus, discard flag, snapshot count, backup coverage, and pool free space. Pick one VM, enable the supported discard path, trim inside the guest, and compare the recorded values. Repeat only after the first guest's result matches the expected backend behavior.

For broader recovery planning, follow the [Proxmox backup and restore drill](/articles/proxmox-vm-backup-restore-drill/) and the [Proxmox VE 8 to 9 upgrade guide](/articles/proxmox-ve-8-to-9-upgrade-guide/).

## Sources

- [Proxmox VE storage administration](https://github.com/proxmox/pve-docs/blob/master/pvesm.adoc), storage types, thin provisioning, and capacity risk.
- [Proxmox VE LVM storage](https://github.com/proxmox/pve-docs/blob/master/pve-storage-lvm.adoc), VE 9 snapshot volume chains and allocation.
- [Proxmox VE RBD storage](https://github.com/proxmox/pve-docs/blob/master/pve-storage-rbd.adoc), pool and namespace configuration.
- [Proxmox VE virtual machines](https://github.com/proxmox/pve-docs/blob/master/qm.adoc), disk buses, formats, discard, and guest agent.
- [Proxmox VE VM disk options](https://github.com/proxmox/pve-docs/blob/master/generated/qm.conf.5-opts.adoc), bus-specific flags.
- [Proxmox VE containers](https://github.com/proxmox/pve-docs/blob/master/pct.adoc), root filesystems and mount point ownership.
- [Proxmox VE container commands](https://github.com/proxmox/pve-docs/blob/master/generated/pct.1-synopsis.adoc), host-side container trim.
- [Proxmox VE backup and restore](https://github.com/proxmox/pve-docs/blob/master/vzdump.adoc), VM and CT backup coverage.
- [Microsoft Optimize-Volume](https://learn.microsoft.com/en-us/powershell/module/storage/optimize-volume?view=windowsserver2025-ps), Windows ReTrim syntax.
- [Red Hat unused-block guidance](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/8/html/managing_file_systems/discarding-unused-blocks_managing-file-systems), Linux `fstrim` behavior.
- [OpenZFS snapshots and clones](https://openzfs.github.io/openzfs-docs/Basic%20Concepts/Datasets/Snapshots%20and%20Clones.html), blocks held by snapshots.
- [Ceph RBD command reference](https://docs.ceph.com/en/squid/man/8/rbd/), image usage and snapshots.
- [NFSv4.2 specification](https://www.rfc-editor.org/rfc/rfc7862.html#section-6.2.2), server-side space deallocation.
- [PBS maintenance documentation](https://pbs.proxmox.com/docs/maintenance.html), pruning and garbage collection.
- [QEMU disk image utility](https://www.qemu.org/docs/master/tools/qemu-img.html), offline image conversion safety.
