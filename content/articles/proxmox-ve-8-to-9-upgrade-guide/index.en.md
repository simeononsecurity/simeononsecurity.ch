---
title: "Proxmox VE 8 to 9 Upgrade Guide: In-Place Upgrade with Automated Script"
date: 2026-07-22
lastmod: 2026-07-22
toc: true
draft: false
description: "Complete guide to upgrading Proxmox VE 8 (Debian Bookworm) to Proxmox VE 9 (Debian Trixie). Covers prerequisites, step-by-step manual upgrade, the pve8to9-upgrade.sh automation script, breaking changes, and known issues."
genre: ["Virtualization", "Linux Administration", "Proxmox", "Server Management", "Open Source", "Homelab"]
tags: ["Proxmox VE 9", "Proxmox upgrade", "PVE 8 to 9", "Debian Trixie", "Debian 13", "apt dist-upgrade", "pve8to9", "Proxmox Ceph", "proxmox-boot-tool", "grub-efi", "LVM upgrade", "ZFS upgrade", "NVIDIA vGPU", "cgroupv2", "Proxmox automation", "bash upgrade script", "Proxmox cluster upgrade", "in-place upgrade", "pve8to9-upgrade.sh", "Proxmox VE 9.0"]
cover: "/img/cover/proxmox-ve-8-to-9-upgrade-guide.webp"
coverAlt: "A dark-themed server rack illustration with two version labels — PVE 8 transitioning to PVE 9 — connected by a glowing upgrade arrow, surrounded by Debian and Proxmox logos on a deep navy background."
coverCaption: "Upgrading Proxmox VE 8 to 9: step-by-step in-place upgrade with an automated assistant script."
canonical: "https://simeononsecurity.com/articles/proxmox-ve-8-to-9-upgrade-guide/"
---

**Proxmox VE 9 is based on Debian 13 Trixie and ships with kernel 6.14, QEMU 10, LXC 6, and ZFS 2.3.** This guide covers both the manual in-place upgrade path and an automated bash script that detects your configuration and handles every repository change, known issue, and pre-flight check.

## What Is New in Proxmox VE 9

Proxmox VE 9 (released August 2025) is a major version upgrade. Key changes:

| Component | PVE 8 | PVE 9 |
|-----------|--------|--------|
| **Debian base** | Bookworm (12) | Trixie (13) |
| **Default kernel** | 6.8 | 6.14 |
| **QEMU** | 9.x | 10.x |
| **LXC** | 5.x | 6.x |
| **ZFS** | 2.2 | 2.3 |
| **Ceph** | Quincy / Reef / Squid | Squid (required) / Tentacle (optional) |
| **cgroup** | cgroupv2 (v1 still possible) | cgroupv2 only |

**Major new features in PVE 9.0+ include:**
- VM snapshots on thick-provisioned LVM via volume chains (tech preview → production in 9.1)
- High-Availability affinity rules replacing HA groups
- SDN Fabrics for OpenFabric and OSPF full-mesh Ceph networks
- New mobile web interface (Rust/Yew)
- ZFS RAIDZ device expansion without downtime
- Dynamic load balancing with the Cluster Resource Scheduler (PVE 9.2)
- WireGuard and BGP as SDN fabric protocols (PVE 9.2)
- `/tmp` is now a `tmpfs` (Debian Trixie change — files cleaned periodically)

______

## Before You Start: Prerequisites

**You must satisfy all of these before touching repositories.**

### 1. Proxmox VE 8.4 minimum

```bash
pveversion
```

Output must show `pve-manager/8.4.x` or higher. If not:

```bash
apt update && apt dist-upgrade
```

### 2. Ceph must be at Squid (19.x) — hyper-converged only

```bash
ceph --version
```

Output must show version 19.x (Squid). If you are on Reef (18.x) or Quincy (17.x), upgrade Ceph first. The upgrade path is always one step at a time:

- Quincy (17) → Reef (18) → Squid (19)

*Do not proceed to the PVE 9 upgrade until all Ceph nodes are on Squid.*

### 3. Co-installed Proxmox Backup Server

If PBS is installed on the same node, upgrade PBS 3 → 4 before touching the PVE repositories. Run `pbs3to4 --full` and resolve all issues first.

### 4. Access requirements

- **Preferred**: console access via IPMI, iKVM, or physical keyboard — the SSH session will drop when services restart
- **SSH**: use `tmux` or `screen` so the upgrade continues if the connection drops:
  ```bash
  tmux new -s upgrade
  ```

### 5. Disk space

```bash
df -h /
```

Need at least **5 GB free**, ideally 10+ GB.

### 6. Valid backups

Back up all VMs and containers to external storage before proceeding. Test a restore. A valid backup is not optional.

______

## Breaking Changes You Must Know

Read these before upgrading. Several require action before or after the upgrade.

### cgroup V1 Is Gone

PVE 9 does not support the legacy cgroupv1 environment at all. If you previously enabled it:

```bash
grep -E 'cgroup_no_v1|systemd.unified_cgroup_hierarchy=0' /proc/cmdline
```

If that returns anything, remove the kernel parameter from `/etc/default/grub` and run `update-grub` before upgrading.

**Impact on containers**: Containers running systemd 230 or older (CentOS 7, Ubuntu 16.04) will not start under PVE 9. Migrate those workloads during the PVE 8 support window (EOL July 2026).

### HA Groups Deprecated

HA groups are replaced by HA rules. They migrate automatically once all cluster nodes are on PVE 9. No manual action required, but verify after upgrading the last node.

### VM.Monitor Privilege Removed

Custom roles that referenced `VM.Monitor` need updating. Use `Sys.Audit` for basic KVM monitor access instead. The `pve8to9` script detects affected roles.

### New Privilege: VM.Replicate

Creating or editing storage replication jobs now requires `VM.Replicate` on `/vms/<vmid>`. Adjust custom roles if needed.

### Privileged LXC Containers Require Sys.Modify

Creating new privileged containers now requires `Sys.Modify`. Restoring an existing privileged container in-place does not.

### systemd-sysctl No Longer Reads /etc/sysctl.conf

Any custom settings in `/etc/sysctl.conf` will be silently ignored after the upgrade. Migrate them to `/etc/sysctl.d/<NN>-name.conf` before rebooting.

```bash
# Check what's in sysctl.conf
grep -v '^\s*#\|^\s*$' /etc/sysctl.conf
```

### /tmp Is Now tmpfs

Debian Trixie mounts `/tmp` as tmpfs (up to 50% of RAM). Files are cleaned periodically while the system runs. If you use `/tmp` for large temporary files, move that work to `/var/tmp` or a dedicated mount.

### Veeam Backup Broken for QEMU Machine Version ≥ 10.0

Proxmox changed how disks attach to QEMU internally for machine version 10.0+. Veeam has not adapted yet. Either pin affected VMs to machine version `9.2+pve1` before upgrading, or postpone the upgrade if Veeam is critical.

### Network Interface Names May Change

Kernel 6.14 recognizes more NIC features than 6.8. Some NICs pick up additional naming suffixes. The `pve-network-interface-pinning` tool can pin all interfaces to stable `nicX` names before the upgrade:

```bash
pve-network-interface-pinning --help
```

______

## Option A: Manual In-Place Upgrade

Follow the official steps from [pve.proxmox.com/wiki/Upgrade_from_8_to_9](https://pve.proxmox.com/wiki/Upgrade_from_8_to_9).

### Step 1: Run the pve8to9 checklist

```bash
pve8to9 --full
```

Resolve every `FAIL` item before continuing. Re-run after each fix.

### Step 2: Migrate away running VMs (if in a cluster)

```bash
qm migrate <vmid> <target-node>
pct migrate <ctid> <target-node>
```

### Step 3: Fully update PVE 8

```bash
apt update && apt dist-upgrade
pveversion   # must show 8.4.1 or newer
```

### Step 4: Update Debian base repositories

```bash
sed -i 's/bookworm/trixie/g' /etc/apt/sources.list
sed -i 's/bookworm/trixie/g' /etc/apt/sources.list.d/pve-enterprise.list
```

Comment out or remove any remaining Bookworm-specific repo lines.

### Step 5: Add PVE 9 package repository

**Enterprise (subscription required):**

```bash
cat > /etc/apt/sources.list.d/pve-enterprise.sources << EOF
Types: deb
URIs: https://enterprise.proxmox.com/debian/pve
Suites: trixie
Components: pve-enterprise
Signed-By: /usr/share/keyrings/proxmox-archive-keyring.gpg
EOF
```

**No-subscription:**

```bash
cat > /etc/apt/sources.list.d/proxmox.sources << EOF
Types: deb
URIs: http://download.proxmox.com/debian/pve
Suites: trixie
Components: pve-no-subscription
Signed-By: /usr/share/keyrings/proxmox-archive-keyring.gpg
EOF
```

Verify with `apt update && apt policy` that the new repo appears without errors. Then remove or comment out the old `.list` file.

### Step 6: Update Ceph repository (hyper-converged only)

```bash
cat > /etc/apt/sources.list.d/ceph.sources << EOF
Types: deb
URIs: https://enterprise.proxmox.com/debian/ceph-squid
Suites: trixie
Components: enterprise
Signed-By: /usr/share/keyrings/proxmox-archive-keyring.gpg
EOF
```

Use `http://download.proxmox.com/debian/ceph-squid` with `pve-no-subscription` for no-subscription setups.

### Step 7: Refresh package index

```bash
apt update
```

Verify no errors.

### Step 8: Run the dist-upgrade

```bash
apt dist-upgrade
```

This takes 5–60+ minutes depending on storage speed. During the upgrade:

- **`/etc/issue`**: keep your current version (safe)
- **`/etc/lvm/lvm.conf`**: install maintainer version (recommended)
- **`/etc/ssh/sshd_config`**: install maintainer version if you haven't customized it
- **`/etc/default/grub`**: keep your current version if you've customized it
- **`/etc/chrony/chrony.conf`**: install maintainer version if uncustomized

### Step 9: Reboot

```bash
reboot
```

Even if kernel 6.14 was already installed as an opt-in on PVE 8, reboot is required — the kernel is rebuilt with PVE 9 toolchains.

### Step 10: Post-upgrade steps

```bash
# Empty browser cache: Ctrl+Shift+R (or ⌘+Alt+R on macOS)
# Verify all nodes in cluster:
pvesh get /nodes

# For clusters: HA groups auto-migrate to HA rules after all nodes are on PVE 9
journalctl -eu pve-ha-crm  # check for errors
```

______

## Option B: Automated Script (pve8to9-upgrade.sh)

The manual process has many conditional steps that vary by configuration. The `pve8to9-upgrade.sh` script automates all of them.

**Script source:** [gist.github.com/simeononsecurity/ba3831f487c4e960f9e218c7da5c4b8d](https://gist.github.com/simeononsecurity/ba3831f487c4e960f9e218c7da5c4b8d)

### What the Script Does

The script handles the full upgrade automatically, including:

| Detection | Action |
|-----------|--------|
| Enterprise vs. no-subscription repos | Uses the repo type that was **actively enabled** — does not enable enterprise on no-sub nodes |
| Ceph version | Blocks if Quincy or Reef, shows the step-by-step Ceph upgrade guide |
| Ceph repo type | Writes a new `ceph.sources` matching your existing repo type |
| NVIDIA vGPU driver | Blocks if driver < 570.158.02 (GRID 18.3 minimum) |
| NVIDIA GPU passthrough | Warns; generates post-upgrade test reminder |
| CUDA repos | Updates `debian12` → `debian13` in URI paths |
| systemd-boot meta-package | Removes it (fixes Debian bug #1110177 that aborts dist-upgrade) |
| `sysctl.conf` custom settings | Migrates to `/etc/sysctl.d/99-pve8to9-migrated.conf` |
| FRR post-up deadlock | Fixes `/etc/network/interfaces` before reboot |
| `systemd-journald-audit.socket` | Disables to prevent log flooding during upgrade |
| UEFI + LVM grub issue | Installs `grub-efi-amd64` and writes a cheat-sheet to `/root/` |
| Third-party `bookworm` repos | Comments them out with a reminder to update |
| `linux-image-amd64` conflict | Removes it if present |
| LVM autoactivation | Runs the migration script pre- and post-upgrade |
| Proxmox Backup Server | Runs `pbs3to4 --full` check; updates PBS repos for Trixie |
| ZFS root | Detects and acknowledges (no special action needed) |

All changes are fully logged to `/var/log/pve8to9-upgrade-<timestamp>.log`. APT repo backups are written to `/root/pve8to9-apt-backups/` — never copied as `.bak` inside `/etc/apt/sources.list.d/` (which would cause "invalid extension" errors in the web UI).

### Installation and Usage

```bash
# Download the script
curl -fsSL https://gist.githubusercontent.com/simeononsecurity/ba3831f487c4e960f9e218c7da5c4b8d/raw/pve8to9-upgrade.sh \
  -o pve8to9-upgrade.sh

# Make executable
chmod +x pve8to9-upgrade.sh

# Review it before running (always read scripts before executing as root)
less pve8to9-upgrade.sh
```

**Run modes:**

```bash
# Full interactive mode (recommended)
./pve8to9-upgrade.sh

# Auto-approve all safe, non-destructive fixes
./pve8to9-upgrade.sh --yes

# Dry run: show every change without applying anything
./pve8to9-upgrade.sh --dry-run

# Skip the pve8to9 --full pre-flight (not recommended)
./pve8to9-upgrade.sh --skip-preflight
```

*Run inside `tmux` or `screen` if connecting via SSH.*

### What the Script Output Looks Like

The script provides a configuration summary before asking you to proceed:

```
══════════════════════════════════════════
  SUMMARY of detected configuration
══════════════════════════════════════════

  PVE version      : pve-manager/8.4.3/...
  Debian           : bookworm
  Subscription     : true (status: Active)
  PVE repo type    : enterprise  (enterprise was active: true)
  Ceph             : YES (v19.2.3, enterprise repos)
  ZFS root         : false
  UEFI boot        : true
  LVM root         : true
  NVIDIA           : NO
  CUDA repos       : NO
  systemd-boot     : meta=true efi=true
  sysctl.conf      : custom=false (0 lines)
  cgroupv1         : false (must be false for PVE 9)
  FRR post-up      : false (broken pattern)
  LVM autoact.     : false
  PBS co-install   : NO
  3rd-party bookwm : none
```

### The Script's Blocking Safety Checks

The script will **refuse to continue** if any of these conditions are true:

- cgroup V1 is explicitly enabled in the kernel cmdline
- Ceph is still at Quincy (17.x) or Reef (18.x) — shows the exact Ceph upgrade commands
- NVIDIA vGPU driver is below version 570 (GRID 18.3)
- PVE version is below 8.4

For each blocking issue, the script prints the exact commands to resolve it before re-running.

______

## Known Upgrade Issues

### GRUB Fails to Boot from LVM in UEFI Mode

**Affects**: Systems with root on LVM, booting in UEFI mode, upgraded from PVE 7.x

```bash
# Fix (run on the live system after upgrade):
[ -d /sys/firmware/efi ] && apt install grub-efi-amd64
```

The `pve8to9-upgrade.sh` script detects UEFI+LVM and installs this automatically. It also writes a recovery cheat-sheet to `/root/GRUB-RECOVERY-CHEATSHEET.txt`.

**If the node is already stuck** at `grub rescue>` or "disk 'lvmid/...' not found":

1. Boot the PVE ISO → Advanced → **Rescue Boot**
2. Or follow the [Recover From Grub Failure](https://pve.proxmox.com/wiki/Recover_From_Grub_Failure) wiki page

### systemd-boot Meta-Package Aborts dist-upgrade

The `systemd-boot` meta-package was auto-installed on all PVE 8.1–8.4 ISO systems. In Trixie, it contains hooks that fire when other packages upgrade and can abort `dist-upgrade` mid-run if the ESP is not mounted (Debian Bug #1110177).

```bash
# Remove it before the dist-upgrade:
apt remove systemd-boot
# Do NOT remove systemd-boot-efi or systemd-boot-tools — those stay
```

The `pve8to9-upgrade.sh` script handles this automatically and explains why in detail.

### PCI Passthrough Sometimes Broken with Kernel 6.14

Some users report VMs with PCI passthrough fail to start with kernel 6.14. If affected:

```bash
# Pin the old kernel temporarily:
proxmox-boot-tool kernel pin 6.8.12-4-pve
```

### Ceph Full Mesh Setups Deadlock on Reboot

If your `/etc/network/interfaces` contains:

```
post-up /usr/bin/systemctl restart frr.service
```

Change it to:

```
post-up /usr/bin/systemctl is-active --quiet frr.service && /usr/bin/systemctl restart frr.service || true
```

Do this **before rebooting**. The script auto-detects and fixes this pattern.

### LVM Thin Pool Needs Repair

On some systems after upgrade:

```
Check of pool pve/data failed (status:64). Manual repair required!
```

Fix:

```bash
lvconvert --repair pve/data
```

### NVIDIA vGPU Minimum Driver Version

Must be at least **driver 570.158.02** (GRID 18.3) before upgrading — older drivers are incompatible with kernel 6.x.

```bash
nvidia-smi --query-gpu=driver_version --format=csv,noheader
```

______

## Cluster Upgrade Order

Upgrade nodes one at a time. Verify each node is healthy before starting the next.

```bash
# Check cluster health before each node upgrade:
pvecm status
ceph -s   # if Ceph is deployed
```

**Migration rules during partial upgrades:**

- VM/CT from PVE 8 → PVE 9: always works
- VM/CT from PVE 9 → PVE 8: generally not supported

After all nodes are on PVE 9, HA groups auto-migrate to HA affinity rules. Check for errors:

```bash
journalctl -eu pve-ha-crm
```

______

## Troubleshooting

### Upgrade Gets Stuck / "proxmox-ve would be removed"

If you see:
```
W: (pve-apt-hook) You are attempting to remove the meta-package 'proxmox-ve'!
```

One or more packages can't be upgraded because a Bookworm repo is still configured. Find stray Bookworm entries:

```bash
grep -r 'bookworm' /etc/apt/sources.list /etc/apt/sources.list.d/
```

Comment them out, then:

```bash
apt update && apt dist-upgrade
```

If partially complete:

```bash
apt -f install
```

### Failing to Boot after ZFS Upgrade

If using ZFS root with legacy BIOS boot, see [ZFS: Switch Legacy-Boot to Proxmox Boot Tool](https://pve.proxmox.com/wiki/ZFS:_Switch_Legacy-Boot_to_Proxmox_Boot_Tool). The `proxmox-boot-tool` must manage boot on ZFS systems — not GRUB directly — to survive ZFS feature upgrades.

______

## Post-Upgrade Checklist

After rebooting each node:

- [ ] Clear browser cache (`Ctrl+Shift+R` / `⌘+Alt+R`)
- [ ] `pveversion` shows 9.x
- [ ] `uname -r` shows 6.14.x or newer
- [ ] All VMs and CTs start correctly
- [ ] Ceph health: `ceph -s` shows HEALTH_OK
- [ ] If UEFI+LVM: verify `grubx64.efi` mtime is recent
- [ ] If NVIDIA passthrough: test a non-production VM
- [ ] Update third-party repos that were commented out during upgrade
- [ ] Move any `/etc/sysctl.conf` custom settings to `/etc/sysctl.d/`

______

## References

1. [Official: Proxmox VE Upgrade from 8 to 9](https://pve.proxmox.com/wiki/Upgrade_from_8_to_9)
2. [pve8to9-upgrade.sh Automation Script](https://gist.github.com/simeononsecurity/ba3831f487c4e960f9e218c7da5c4b8d)
3. [Proxmox VE 9.0 Release Notes / Roadmap](https://pve.proxmox.com/wiki/Roadmap#9.0-known-issues)
4. [Proxmox VE 9.2 Release Notes](https://pve.proxmox.com/wiki/Roadmap#9.2-known-issues)
5. [Recover From Grub Failure](https://pve.proxmox.com/wiki/Recover_From_Grub_Failure)
6. [ZFS: Switch Legacy-Boot to Proxmox Boot Tool](https://pve.proxmox.com/wiki/ZFS:_Switch_Legacy-Boot_to_Proxmox_Boot_Tool)
7. [Ceph Reef to Squid Upgrade Guide](https://pve.proxmox.com/wiki/Ceph_Reef_to_Squid)
8. [Proxmox Network Interface Pinning](https://pve.proxmox.com/pve-docs/chapter-sysadmin.html)
9. [Debian 13 Trixie Release Notes](https://www.debian.org/releases/trixie/releasenotes)
