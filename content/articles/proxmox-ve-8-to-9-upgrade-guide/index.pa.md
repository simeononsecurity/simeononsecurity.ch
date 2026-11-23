---
title: "Proxmox VE 8 ਤੋਂ 9 ਅੱਪਗ੍ਰੇਡ ਗਾਈਡ"
date: 2026-07-22
lastmod: 2026-11-23
toc: true
draft: false
description: "Proxmox VE 8 ਨੂੰ 9 ਵਿੱਚ ਅੱਪਗ੍ਰੇਡ ਕਰਨ ਲਈ ਪਹਿਲਾਂ ਦੀਆਂ ਜਾਂਚਾਂ, ਹੱਥੀਂ ਕਦਮ, ਆਟੋਮੇਸ਼ਨ, ਅਣਅਨੁਕੂਲ ਬਦਲਾਅ ਅਤੇ ਰਿਕਵਰੀ ਦੀਆਂ ਹਦਾਇਤਾਂ ਵੇਖੋ।"
genre: ["ਵਰਚੁਅਲਾਈਜ਼ੇਸ਼ਨ", "Linux ਪ੍ਰਸ਼ਾਸਨ", "Proxmox", "ਸਰਵਰ ਪ੍ਰਬੰਧਨ", "ਓਪਨ ਸੋਰਸ", "ਘਰੇਲੂ ਲੈਬ"]
tags: ["Proxmox VE 9", "Proxmox ਅੱਪਗ੍ਰੇਡ", "PVE 8 ਤੋਂ 9", "Debian Trixie", "Debian 13", "apt dist-upgrade", "pve8to9", "Proxmox Ceph", "proxmox-boot-tool", "grub-efi", "LVM ਅੱਪਗ੍ਰੇਡ", "ZFS ਅੱਪਗ੍ਰੇਡ", "NVIDIA vGPU", "cgroupv2", "Proxmox ਆਟੋਮੇਸ਼ਨ", "Bash ਅੱਪਗ੍ਰੇਡ ਸਕ੍ਰਿਪਟ", "Proxmox ਕਲੱਸਟਰ ਅੱਪਗ੍ਰੇਡ", "ਇਨ-ਪਲੇਸ ਅੱਪਗ੍ਰੇਡ", "pve8to9-upgrade.sh", "Proxmox VE 9.0"]
cover: "/img/cover/proxmox-ve-8-to-9-upgrade-guide-automation.webp"
coverAlt: "ਆਧੁਨਿਕ ਸਰਵਰ ਕਮਰੇ ਦੀਆਂ ਸਕ੍ਰੀਨਾਂ ਉੱਤੇ ਵਰਚੁਅਲ ਮਸ਼ੀਨਾਂ ਦੇ ਚਮਕਦੇ ਚਿੰਨ੍ਹ ਹਨ। ਇੱਕ ਤਕਨੀਕੀ ਕਰਮਚਾਰੀ ਗੂੜ੍ਹੇ ਨੀਲੇ ਸਾਜ਼ੋ-ਸਾਮਾਨ ਵਿਚਕਾਰ ਲੈਪਟਾਪ ਉੱਤੇ ਕੰਮ ਕਰਦਾ ਹੈ, ਆਲੇ-ਦੁਆਲੇ ਨੀਲੀਆਂ, ਹਰੀਆਂ ਅਤੇ ਜਾਮਣੀ ਰੌਸ਼ਨੀਆਂ ਹਨ।"
coverCaption: "Proxmox VE 8 ਤੋਂ 9 ਅੱਪਗ੍ਰੇਡ: ਆਟੋਮੈਟਿਕ ਸਹਾਇਕ ਸਕ੍ਰਿਪਟ ਨਾਲ ਇਨ-ਪਲੇਸ ਅੱਪਗ੍ਰੇਡ ਦੇ ਕਦਮ।"
canonical: "https://simeononsecurity.com/articles/proxmox-ve-8-to-9-upgrade-guide/"
---

**Proxmox VE 9.0, Debian 13 Trixie, kernel 6.14, QEMU 10, LXC 6 ਅਤੇ ZFS 2.3 ਨਾਲ ਜਾਰੀ ਹੋਇਆ।** ਇਹ ਗਾਈਡ ਹੱਥੀਂ ਇਨ-ਪਲੇਸ ਅੱਪਗ੍ਰੇਡ ਅਤੇ ਇੱਕ ਆਟੋਮੈਟਿਕ Bash ਸਕ੍ਰਿਪਟ ਦੋਵੇਂ ਸਮਝਾਉਂਦੀ ਹੈ। ਸਕ੍ਰਿਪਟ ਤੁਹਾਡੀ ਸੰਰਚਨਾ ਪਛਾਣ ਕੇ ਰਿਪੋਜ਼ਟਰੀਆਂ ਦੇ ਬਦਲਾਅ, ਜਾਣੀਆਂ ਸਮੱਸਿਆਵਾਂ ਅਤੇ ਪਹਿਲਾਂ ਦੀਆਂ ਸਾਰੀਆਂ ਜਾਂਚਾਂ ਸੰਭਾਲਦੀ ਹੈ।

## Proxmox VE 9 ਵਿੱਚ ਨਵਾਂ ਕੀ ਹੈ

Proxmox VE 9 ਅਗਸਤ 2025 ਵਿੱਚ ਜਾਰੀ ਹੋਇਆ ਅਤੇ ਇਹ ਮੁੱਖ ਸੰਸਕਰਣ ਅੱਪਗ੍ਰੇਡ ਹੈ। ਮੁੱਖ ਬਦਲਾਅ:

| ਘਟਕ | PVE 8 | PVE 9.0 |
|-----------|--------|--------|
| **Debian ਆਧਾਰ** | Bookworm (12) | Trixie (13) |
| **ਮੂਲ kernel** | 6.8 | 6.14 |
| **QEMU** | 9.x | 10.x |
| **LXC** | 5.x | 6.x |
| **ZFS** | 2.2 | 2.3 |
| **Ceph** | Quincy / Reef / Squid | Squid (19.2) |
| **cgroup** | cgroupv2 (v1 ਹਾਲੇ ਸੰਭਵ) | ਸਿਰਫ਼ cgroupv2 |

[Proxmox VE 9.2](https://forum.proxmox.com/threads/proxmox-virtual-environment-9-2-available.183742/) ਵਿੱਚ ਮੂਲ ਰੂਪ ਵਿੱਚ kernel 7.0, QEMU 11, LXC 7 ਅਤੇ ZFS 2.4 ਹਨ। Ceph Tentacle, 9.2 ਦਾ ਮੂਲ ਸੰਸਕਰਣ ਹੈ ਪਰ Squid ਵੀ ਉਪਲਬਧ ਹੈ। VE 8 Ceph ਕਲੱਸਟਰ ਅੱਪਗ੍ਰੇਡ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ Squid ਵੱਲ ਜਾਣਾ ਵੱਖਰੀ ਪਹਿਲਾਂ ਦੀ ਸ਼ਰਤ ਹੈ।

**PVE 9.0 ਅਤੇ ਬਾਅਦ ਦੀਆਂ ਮੁੱਖ ਨਵੀਆਂ ਸਹੂਲਤਾਂ:**
- ਵਾਲਿਊਮ ਲੜੀਆਂ ਰਾਹੀਂ ਪੂਰੀ ਤਰ੍ਹਾਂ ਦਿੱਤੀ LVM ਉੱਤੇ VM snapshots (ਤਕਨੀਕੀ ਝਲਕ, 9.1 ਤੋਂ production ਲਈ)
- HA groups ਦੀ ਥਾਂ high-availability affinity ਨਿਯਮ
- OpenFabric ਅਤੇ OSPF ਪੂਰਾ-ਜਾਲ Ceph ਨੈੱਟਵਰਕਾਂ ਲਈ SDN Fabrics
- ਨਵਾਂ ਮੋਬਾਈਲ ਵੈੱਬ ਇੰਟਰਫੇਸ (Rust/Yew)
- ਬਿਨਾਂ ਰੁਕਾਵਟ ZFS RAIDZ devices ਦਾ ਵਿਸਥਾਰ
- Cluster Resource Scheduler ਨਾਲ ਗਤੀਸ਼ੀਲ ਲੋਡ ਸੰਤੁਲਨ (PVE 9.2)
- SDN ਨੈੱਟਵਰਕ ਪ੍ਰੋਟੋਕੋਲ ਵਜੋਂ WireGuard ਅਤੇ BGP (PVE 9.2)
- `/tmp` ਹੁਣ `tmpfs` ਹੈ (Debian Trixie ਬਦਲਾਅ, ਫ਼ਾਈਲਾਂ ਸਮੇਂ-ਸਮੇਂ ਸਾਫ਼ ਹੁੰਦੀਆਂ ਹਨ)

{{< figure src="proxmox-ve-8-to-9-component-changes.webp" alt="Proxmox VE 8 ਅਤੇ VE 9 ਦੀ ਤੁਲਨਾ, ਜਿਸ ਵਿੱਚ kernel, QEMU, LXC, ZFS ਅਤੇ Ceph ਸੰਸਕਰਣਾਂ ਦੇ ਬਦਲਾਅ ਹਨ" >}}

______

## ਸ਼ੁਰੂ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ: ਪਹਿਲਾਂ ਦੀਆਂ ਸ਼ਰਤਾਂ

**ਰਿਪੋਜ਼ਟਰੀਆਂ ਬਦਲਣ ਤੋਂ ਪਹਿਲਾਂ ਇਹ ਸਾਰੀਆਂ ਸ਼ਰਤਾਂ ਪੂਰੀਆਂ ਕਰੋ।** [ਅਧਿਕਾਰਕ ਅੱਪਗ੍ਰੇਡ Wiki ਦੀ prerequisites ਸੂਚੀ](https://pve.proxmox.com/wiki/Upgrade_from_8_to_9#Prerequisites) ਵੇਖੋ।

### 1. ਘੱਟੋ-ਘੱਟ Proxmox VE 8.4 ਹੋਵੇ

```bash
pveversion
```

ਨਤੀਜੇ ਵਿੱਚ `pve-manager/8.4.x` ਜਾਂ ਇਸ ਤੋਂ ਨਵਾਂ ਸੰਸਕਰਣ ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ। ਨਹੀਂ ਤਾਂ ਚਲਾਓ:

```bash
apt update && apt dist-upgrade
```

### 2. Ceph Squid (19.x) ਉੱਤੇ ਹੋਵੇ, ਸਿਰਫ਼ hyper-converged ਮਾਹੌਲ ਲਈ

```bash
ceph --version
```

ਨਤੀਜੇ ਵਿੱਚ 19.x (Squid) ਦਿਖਣਾ ਚਾਹੀਦਾ ਹੈ। ਜੇ Reef (18.x) ਜਾਂ Quincy (17.x) ਹੈ, ਪਹਿਲਾਂ Ceph ਅੱਪਗ੍ਰੇਡ ਕਰੋ। ਇੱਕ ਵਾਰ ਵਿੱਚ ਇੱਕ ਮੁੱਖ ਸੰਸਕਰਣ ਅੱਗੇ ਵਧੋ:

- Quincy (17) → Reef (18) → Squid (19)

*ਸਾਰੇ Ceph ਨੋਡ ਉੱਤੇ Squid ਚੱਲਣ ਤੱਕ PVE 9 ਅੱਪਗ੍ਰੇਡ ਸ਼ੁਰੂ ਨਾ ਕਰੋ।*

### 3. ਉਸੇ node ਉੱਤੇ Proxmox Backup Server ਹੋਵੇ

ਜੇ PBS 3.4 ਅਤੇ PVE 8.4 ਇੱਕ node ਸਾਂਝਾ ਕਰਦੇ ਹਨ, [ਸਾਂਝੀ ਇੰਸਟਾਲੇਸ਼ਨ ਦੀਆਂ ਹਦਾਇਤਾਂ](https://pbs.proxmox.com/wiki/Upgrade_from_3_to_4#Installed_alongside_Proxmox_VE) ਮੰਨੋ ਅਤੇ ਦੋਵੇਂ ਅੱਪਗ੍ਰੇਡ ਇੱਕ APT ਕਾਰਵਾਈ ਵਿੱਚ ਮਿਲਾ ਕੇ ਕਰੋ। ਯਕੀਨੀ ਬਣਾਓ ਕਿ backups restore ਹੋ ਸਕਦੇ ਹਨ ਅਤੇ repositories ਬਦਲਣ ਤੋਂ ਪਹਿਲਾਂ `pve8to9 --full` ਅਤੇ `pbs3to4 --full` ਚਲਾਓ। ਰਿਪੋਰਟ ਕੀਤੀਆਂ ਸਮੱਸਿਆਵਾਂ ਪਹਿਲਾਂ ਹੱਲ ਕਰੋ।

### 4. ਪਹੁੰਚ ਦੀਆਂ ਲੋੜਾਂ

- **ਤਰਜੀਹੀ**: IPMI, iKVM ਜਾਂ ਭੌਤਿਕ keyboard ਰਾਹੀਂ ਕੰਸੋਲ ਪਹੁੰਚ। Services ਮੁੜ ਚੱਲਣ ਵੇਲੇ SSH ਸੈਸ਼ਨ ਟੁੱਟੇਗਾ।
- **SSH**: connection ਟੁੱਟਣ ਉੱਤੇ ਵੀ ਅੱਪਗ੍ਰੇਡ ਜਾਰੀ ਰੱਖਣ ਲਈ `tmux` ਜਾਂ `screen` ਵਰਤੋ:
  ```bash
  tmux new -s upgrade
  ```

### 5. ਡਿਸਕ ਥਾਂ

```bash
df -h /
```

ਘੱਟੋ-ਘੱਟ **5 GB ਖਾਲੀ**, ਵਧੀਆ ਤੌਰ ’ਤੇ 10 GB ਜਾਂ ਵੱਧ ਰੱਖੋ।

### 6. ਠੀਕ backups

ਅੱਗੇ ਵਧਣ ਤੋਂ ਪਹਿਲਾਂ ਸਾਰੀਆਂ VMs ਅਤੇ containers ਨੂੰ ਬਾਹਰੀ ਸਟੋਰੇਜ ਉੱਤੇ backup ਕਰੋ। Restore ਦੀ ਜਾਂਚ ਕਰੋ। ਠੀਕ backup ਲਾਜ਼ਮੀ ਹੈ।

______

## ਅਣਅਨੁਕੂਲ ਬਦਲਾਅ ਜਿਨ੍ਹਾਂ ਬਾਰੇ ਜਾਣੋ

ਅੱਪਗ੍ਰੇਡ ਤੋਂ ਪਹਿਲਾਂ ਇਹ ਪੜ੍ਹੋ। ਕੁਝ ਲਈ ਪਹਿਲਾਂ ਜਾਂ ਬਾਅਦ ਕਾਰਵਾਈ ਲੋੜੀਂਦੀ ਹੈ।

### cgroup V1 ਹਟਾਇਆ ਗਿਆ

PVE 9 ਪੁਰਾਣੇ cgroupv1 ਮਾਹੌਲ ਦਾ ਬਿਲਕੁਲ ਸਮਰਥਨ ਨਹੀਂ ਕਰਦਾ। ਜੇ ਤੁਸੀਂ ਪਹਿਲਾਂ ਇਸਨੂੰ ਚਾਲੂ ਕੀਤਾ ਸੀ:

```bash
grep -E 'cgroup_no_v1|systemd.unified_cgroup_hierarchy=0' /proc/cmdline
```

ਜੇ ਕੁਝ ਵੀ ਵਾਪਸ ਆਵੇ, ਅੱਪਗ੍ਰੇਡ ਤੋਂ ਪਹਿਲਾਂ `/etc/default/grub` ਵਿੱਚੋਂ kernel ਪੈਰਾਮੀਟਰ ਹਟਾਓ ਅਤੇ `update-grub` ਚਲਾਓ।

**Containers ਉੱਤੇ ਅਸਰ**: systemd 230 ਜਾਂ ਪੁਰਾਣੇ ਸੰਸਕਰਣ ਵਾਲੇ containers (CentOS 7, Ubuntu 16.04) PVE 9 ਵਿੱਚ ਸ਼ੁਰੂ ਨਹੀਂ ਹੋਣਗੇ। ਅੱਪਗ੍ਰੇਡ ਤੋਂ ਪਹਿਲਾਂ ਇਹ workloads migrate ਕਰੋ। Proxmox VE 8.4 ਲਈ ਵਿਕਰੇਤਾ ਸਹਾਇਤਾ ਅਗਸਤ 2026 ਵਿੱਚ ਖ਼ਤਮ ਹੋਇਆ।

### HA groups ਪੁਰਾਣੇ ਹੋ ਗਏ ਹਨ

HA rules, HA groups ਦੀ ਥਾਂ ਲੈਂਦੇ ਹਨ। ਸਾਰੇ ਕਲੱਸਟਰ ਨੋਡ PVE 9 ਉੱਤੇ ਆਉਣ ਤੋਂ ਬਾਅਦ migration ਆਪਣੇ ਆਪ ਹੁੰਦੀ ਹੈ। ਹੱਥੀਂ ਕਾਰਵਾਈ ਦੀ ਲੋੜ ਨਹੀਂ, ਪਰ ਆਖ਼ਰੀ node ਅੱਪਗ੍ਰੇਡ ਹੋਣ ਮਗਰੋਂ ਨਤੀਜਾ ਜਾਂਚੋ।

### VM.Monitor privilege ਹਟਾਇਆ ਗਿਆ

`VM.Monitor` ਵਰਤਣ ਵਾਲੇ ਕਸਟਮ ਭੂਮਿਕਾਵਾਂ ਅੱਪਡੇਟ ਕਰਨੇ ਪੈਣਗੇ। ਮੁੱਢਲੀ KVM ਮਾਨੀਟਰ ਪਹੁੰਚ ਲਈ `Sys.Audit` ਵਰਤੋ। `pve8to9` ਪ੍ਰਭਾਵਿਤ roles ਪਛਾਣਦਾ ਹੈ।

### ਨਵਾਂ privilege: VM.Replicate

Storage ਨਕਲ ਦੇ ਕੰਮ ਬਣਾਉਣ ਜਾਂ ਸੋਧਣ ਲਈ ਹੁਣ `/vms/<vmid>` ਉੱਤੇ `VM.Replicate` ਚਾਹੀਦਾ ਹੈ। ਲੋੜ ਅਨੁਸਾਰ ਕਸਟਮ ਭੂਮਿਕਾਵਾਂ ਸੋਧੋ।

### Privileged LXC containers ਨੂੰ Sys.Modify ਚਾਹੀਦਾ ਹੈ

ਨਵੇਂ ਵਧੇਰੇ ਅਧਿਕਾਰ ਵਾਲੇ ਕੰਟੇਨਰ ਬਣਾਉਣ ਲਈ ਹੁਣ `Sys.Modify` ਲੋੜੀਂਦਾ ਹੈ। ਮੌਜੂਦਾ ਵਧੇਰੇ ਅਧਿਕਾਰ ਵਾਲਾ ਕੰਟੇਨਰ ਨੂੰ in-place restore ਕਰਨ ਲਈ ਨਹੀਂ।

### systemd-sysctl ਹੁਣ /etc/sysctl.conf ਨਹੀਂ ਪੜ੍ਹਦਾ

ਅੱਪਗ੍ਰੇਡ ਤੋਂ ਬਾਅਦ `/etc/sysctl.conf` ਦੀਆਂ ਕਸਟਮ ਸੈਟਿੰਗਾਂ ਬਿਨਾਂ ਦੱਸੇ ਅਣਡਿੱਠੀਆਂ ਹੋਣਗੀਆਂ। Reboot ਤੋਂ ਪਹਿਲਾਂ ਉਨ੍ਹਾਂ ਨੂੰ `/etc/sysctl.d/<NN>-name.conf` ਵਿੱਚ ਲਿਜਾਓ।

```bash
# sysctl.conf ਵਿੱਚਲੀ ਸਮੱਗਰੀ ਵੇਖੋ
grep -v '^\s*#\|\s*$' /etc/sysctl.conf
```

### /tmp ਹੁਣ tmpfs ਹੈ

Debian Trixie `/tmp` ਨੂੰ tmpfs ਵਜੋਂ mount ਕਰਦਾ ਹੈ (RAM ਦਾ ਵੱਧ ਤੋਂ ਵੱਧ 50%)। ਚੱਲਦੇ ਸਿਸਟਮ ਵਿੱਚ ਫ਼ਾਈਲਾਂ ਸਮੇਂ-ਸਮੇਂ ਸਾਫ਼ ਹੁੰਦੀਆਂ ਹਨ। ਵੱਡੀਆਂ ਅਸਥਾਈ ਫ਼ਾਈਲਾਂ ਲਈ `/var/tmp` ਜਾਂ ਵੱਖਰਾ mount ਵਰਤੋ।

### Veeam ਬੈਕਅੱਪ ਅਤੇ ਰੀਸਟੋਰ ਅਨੁਕੂਲਤਾ {#veeam-backup-broken-for-qemu-machine-version--100}

ਅੱਪਗ੍ਰੇਡ ਤੋਂ ਪਹਿਲਾਂ [Veeam Backup & Replication ਅਤੇ Proxmox plugin builds](https://helpcenter.veeam.com/docs/vbr/userguide/pve_system_requirements.html) ਜਾਂਚੋ। ਮੌਜੂਦਾ requirements ਵਿੱਚ ਅਧਿਕਾਰਕ Proxmox ISO ਨਾਲ ਇੰਸਟਾਲ x86-64 hosts ਲਈ Proxmox VE 8.2 ਤੋਂ 9.2 ਸ਼ਾਮਲ ਹਨ। ਪੁਰਾਣੇ Veeam ਰੂਪ ਦੀਆਂ ਸਹਾਇਤਾ ਅੰਤਰਾਲ ਵੱਖਰੀਆਂ ਹਨ।

ਮੌਜੂਦਾ [Veeam ਸੀਮਾਵਾਂ](https://helpcenter.veeam.com/docs/vbr/userguide/pve_limitations.html), Snapshots as Volume Chains (SAVC) ਚਾਲੂ LVM storage ਉੱਤੇ VM backups ਦੀ ਆਗਿਆ ਦਿੰਦੀਆਂ ਹਨ। ਇਸ ਕਰਕੇ SAVC, Veeam ਸੇਵਾ-ਪ੍ਰਕਿਰਿਆ ਦੀਆਂ ਫ਼ਾਈਲਾਂ ਜਾਂ Instant ਰਿਕਵਰੀ ਮੰਜ਼ਿਲ ਲਈ ਮਨਜ਼ੂਰ ਥਾਂ ਨਹੀਂ ਬਣਦਾ। ਵੱਖਰੀ [KB4773 restore ਸਮੱਸਿਆ](https://www.veeam.com/kb4773), PVE 9 ਵਿੱਚ SAVC ਸਟੋਰੇਜ ਉੱਤੇ restore ਕੀਤੀਆਂ QCOW2 ਡਿਸਕਾਂ ਵਾਲੀਆਂ QEMU 10 ਤੋਂ ਪੁਰਾਣੀਆਂ ਮਸ਼ੀਨ ਕਿਸਮਾਂ ਨੂੰ ਪ੍ਰਭਾਵਿਤ ਕਰਦੀ ਹੈ। SAVC ਤੋਂ ਬਿਨਾਂ destination ਵਰਤੋ ਜਾਂ ਦਸਤਾਵੇਜ਼ ਮੁਤਾਬਕ disk ਨੂੰ RAW ਵਜੋਂ restore ਕਰੋ। ਇਹ restore ਉਪਾਅ ਹਨ, ਪੂਰੇ fleet ਵਿੱਚ ਮਸ਼ੀਨ ਕਿਸਮ ਪੱਕਾ ਕਰਨ ਦਾ ਕਾਰਨ ਨਹੀਂ। ਅੱਪਗ੍ਰੇਡ ਉੱਤੇ ਨਿਰਭਰ ਹੋਣ ਤੋਂ ਪਹਿਲਾਂ ਚੁਣੀ storage ਉੱਤੇ backup ਅਤੇ restore ਜਾਂਚੋ।

### Network interface ਦੇ ਨਾਂ ਬਦਲ ਸਕਦੇ ਹਨ

Kernel 6.14, 6.8 ਨਾਲੋਂ ਵੱਧ NIC ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਪਛਾਣਦਾ ਹੈ। ਕੁਝ NIC ਨਾਂਵਾਂ ਵਿੱਚ ਵਾਧੂ suffix ਆਉਂਦੇ ਹਨ। ਅੱਪਗ੍ਰੇਡ ਤੋਂ ਪਹਿਲਾਂ `pve-network-interface-pinning` tool ਸਾਰੇ interfaces ਨੂੰ ਸਥਿਰ `nicX` ਨਾਂ ਦੇ ਸਕਦਾ ਹੈ:

```bash
pve-network-interface-pinning --help
```

______

## ਵਿਕਲਪ A: ਹੱਥੀਂ ਇਨ-ਪਲੇਸ ਅੱਪਗ੍ਰੇਡ

[ਅਧਿਕਾਰਕ pve.proxmox.com/wiki/Upgrade_from_8_to_9](https://pve.proxmox.com/wiki/Upgrade_from_8_to_9) ਦੇ ਕਦਮ ਮੰਨੋ।

### ਕਦਮ 1: pve8to9 ਜਾਂਚ-ਸੂਚੀ ਚਲਾਓ

```bash
pve8to9 --full
```

ਅੱਗੇ ਵਧਣ ਤੋਂ ਪਹਿਲਾਂ ਹਰ `FAIL` ਹੱਲ ਕਰੋ। ਹਰ ਸੁਧਾਰ ਮਗਰੋਂ ਮੁੜ ਚਲਾਓ।

### ਕਦਮ 2: ਚੱਲ ਰਹੀਆਂ VMs migrate ਕਰੋ (ਜੇ cluster ਵਿੱਚ ਹੋ)

```bash
qm migrate <vmid> <target-node>
pct migrate <ctid> <target-node>
```

### ਕਦਮ 3: PVE 8 ਨੂੰ ਪੂਰੀ ਤਰ੍ਹਾਂ ਅੱਪਡੇਟ ਕਰੋ

```bash
apt update && apt dist-upgrade
pveversion   # 8.4.1 ਜਾਂ ਨਵਾਂ ਦਿਖਣਾ ਚਾਹੀਦਾ ਹੈ
```

### ਕਦਮ 4: Debian ਅਧਾਰ ਰਿਪੋਜ਼ਟਰੀਆਂ ਅੱਪਡੇਟ ਕਰੋ

```bash
sed -i 's/bookworm/trixie/g' /etc/apt/sources.list
sed -i 's/bookworm/trixie/g' /etc/apt/sources.list.d/pve-enterprise.list
```

ਬਚੀਆਂ Bookworm repository lines comment ਜਾਂ remove ਕਰੋ।

### ਕਦਮ 5: PVE 9 ਪੈਕੇਜ ਰਿਪੋਜ਼ਟਰੀ ਜੋੜੋ

**Enterprise (subscription ਲੋੜੀਂਦੀ):**

```bash
cat > /etc/apt/sources.list.d/pve-enterprise.sources << EOF
Types: deb
URIs: https://enterprise.proxmox.com/debian/pve
Suites: trixie
Components: pve-enterprise
Signed-By: /usr/share/keyrings/proxmox-archive-keyring.gpg
EOF
```

**Subscription ਤੋਂ ਬਿਨਾਂ:**

```bash
cat > /etc/apt/sources.list.d/proxmox.sources << EOF
Types: deb
URIs: http://download.proxmox.com/debian/pve
Suites: trixie
Components: pve-no-subscription
Signed-By: /usr/share/keyrings/proxmox-archive-keyring.gpg
EOF
```

`apt update && apt policy` ਨਾਲ ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਨਵੀਂ repository ਬਿਨਾਂ error ਆਉਂਦੀ ਹੈ। ਫਿਰ ਪੁਰਾਣੀ `.list` file ਹਟਾਓ ਜਾਂ comment ਕਰੋ।

### ਕਦਮ 6: Ceph ਰਿਪੋਜ਼ਟਰੀ ਅੱਪਡੇਟ ਕਰੋ (ਸਿਰਫ਼ hyper-converged ਮਾਹੌਲ ਵਿੱਚ)

```bash
cat > /etc/apt/sources.list.d/ceph.sources << EOF
Types: deb
URIs: https://enterprise.proxmox.com/debian/ceph-squid
Suites: trixie
Components: enterprise
Signed-By: /usr/share/keyrings/proxmox-archive-keyring.gpg
EOF
```

Subscription ਤੋਂ ਬਿਨਾਂ setup ਲਈ `http://download.proxmox.com/debian/ceph-squid` ਅਤੇ `pve-no-subscription` ਵਰਤੋ।

### ਕਦਮ 7: ਪੈਕੇਜ ਸੂਚੀ refresh ਕਰੋ

```bash
apt update
```

ਕੋਈ error ਨਾ ਹੋਣ ਦੀ ਪੁਸ਼ਟੀ ਕਰੋ।

### ਕਦਮ 8: dist-upgrade ਚਲਾਓ

```bash
apt dist-upgrade
```

Storage speed ਮੁਤਾਬਕ 5 ਤੋਂ 60 ਮਿੰਟ ਜਾਂ ਵੱਧ ਲੱਗ ਸਕਦੇ ਹਨ। ਅੱਪਗ੍ਰੇਡ ਦੌਰਾਨ:

- **`/etc/issue`**: ਮੌਜੂਦਾ version ਰੱਖੋ (ਸੁਰੱਖਿਅਤ)
- **`/etc/lvm/lvm.conf`**: ਸੰਭਾਲਕ ਸੰਸਕਰਣ install ਕਰੋ (ਸਿਫ਼ਾਰਸ਼ੀ)
- **`/etc/ssh/sshd_config`**: ਜੇ customize ਨਹੀਂ ਕੀਤੀ, ਸੰਭਾਲਕ ਸੰਸਕਰਣ ਲਵੋ
- **`/etc/default/grub`**: ਜੇ customize ਕੀਤੀ, ਮੌਜੂਦਾ version ਰੱਖੋ
- **`/etc/chrony/chrony.conf`**: ਜੇ customize ਨਹੀਂ, ਸੰਭਾਲਕ ਸੰਸਕਰਣ ਲਵੋ

### ਕਦਮ 9: reboot ਕਰੋ

```bash
reboot
```

PVE 8 ਵਿੱਚ kernel 6.14 opt-in ਵਜੋਂ ਪਹਿਲਾਂ install ਹੋਵੇ ਤਾਂ ਵੀ reboot ਲਾਜ਼ਮੀ ਹੈ, ਕਿਉਂਕਿ kernel PVE 9 toolchains ਨਾਲ ਮੁੜ ਬਣਦਾ ਹੈ।

### ਕਦਮ 10: ਅੱਪਗ੍ਰੇਡ ਤੋਂ ਬਾਅਦ ਦੇ ਕਦਮ

```bash
# Browser cache ਸਾਫ਼ ਕਰੋ: Ctrl+Shift+R (macOS ਉੱਤੇ ⌘+Alt+R)
# Cluster ਦੇ ਸਾਰੇ nodes ਵੇਖੋ:
pvesh get /nodes

# ਸਾਰੇ nodes PVE 9 ਉੱਤੇ ਹੋਣ ਮਗਰੋਂ HA groups ਆਪਣੇ ਆਪ HA rules ਵਿੱਚ migrate ਹੁੰਦੇ ਹਨ
journalctl -eu pve-ha-crm  # errors ਵੇਖੋ
```

______

## ਵਿਕਲਪ B: ਆਟੋਮੈਟਿਕ script (pve8to9-upgrade.sh)

ਹੱਥੀਂ ਪ੍ਰਕਿਰਿਆ ਵਿੱਚ configuration ਮੁਤਾਬਕ ਕਈ conditional ਕਦਮ ਹਨ। `pve8to9-upgrade.sh` script ਉਹਨਾਂ ਨੂੰ automate ਕਰਦੀ ਹੈ।

**ਸਕ੍ਰਿਪਟ ਸਰੋਤ:** [gist.github.com/simeononsecurity/ba3831f487c4e960f9e218c7da5c4b8d](https://gist.github.com/simeononsecurity/ba3831f487c4e960f9e218c7da5c4b8d)

### Script ਕੀ ਕਰਦੀ ਹੈ

Script ਪੂਰਾ ਅੱਪਗ੍ਰੇਡ ਆਪਣੇ ਆਪ ਸੰਭਾਲਦੀ ਹੈ, ਜਿਸ ਵਿੱਚ:

| ਪਛਾਣ | ਕਾਰਵਾਈ |
|-----------|--------|
| Enterprise ਜਾਂ ਬਿਨਾਂ subscription ਵਾਲੀਆਂ ਰਿਪੋਜ਼ਟਰੀਆਂ | ਜੋ ਕਿਸਮ **ਅਸਲ ਵਿੱਚ ਚਾਲੂ** ਸੀ ਉਹੀ ਵਰਤਦੀ ਹੈ; ਬਿਨਾਂ subscription ਵਾਲੇ nodes ਉੱਤੇ Enterprise ਨਹੀਂ ਚਾਲੂ ਕਰਦੀ |
| Ceph ਸੰਸਕਰਣ | Quincy ਜਾਂ Reef ਹੋਵੇ ਤਾਂ ਰੋਕਦੀ ਹੈ ਅਤੇ Ceph ਅੱਪਗ੍ਰੇਡ ਗਾਈਡ ਦਿਖਾਉਂਦੀ ਹੈ |
| Ceph ਰਿਪੋਜ਼ਟਰੀ ਕਿਸਮ | ਮੌਜੂਦਾ ਕਿਸਮ ਨਾਲ ਮਿਲਦੀ ਨਵੀਂ `ceph.sources` ਲਿਖਦੀ ਹੈ |
| NVIDIA vGPU ਡਰਾਈਵਰ | 570.158.02 ਤੋਂ ਪੁਰਾਣਾ ਹੋਵੇ ਤਾਂ ਰੋਕਦੀ ਹੈ (GRID 18.3 ਘੱਟੋ-ਘੱਟ) |
| NVIDIA GPU ਪਾਸਥਰੂ | ਚੇਤਾਵਨੀ ਦਿੰਦੀ ਹੈ ਅਤੇ ਬਾਅਦ ਦੀ ਜਾਂਚ ਯਾਦ ਦਿਵਾਉਂਦੀ ਹੈ |
| CUDA ਰਿਪੋਜ਼ਟਰੀਆਂ | URI ਰਸਤੇ ਵਿੱਚ `debian12` ਨੂੰ `debian13` ਕਰਦੀ ਹੈ |
| systemd-boot ਮੈਟਾ-ਪੈਕੇਜ | ਹਟਾਉਂਦੀ ਹੈ (dist-upgrade ਰੋਕਣ ਵਾਲਾ Debian ਬੱਗ #1110177 ਠੀਕ ਕਰਦੀ ਹੈ) |
| `sysctl.conf` ਕਸਟਮ ਸੈਟਿੰਗਾਂ | `/etc/sysctl.d/99-pve8to9-migrated.conf` ਵਿੱਚ ਲਿਜਾਂਦੀ ਹੈ |
| FRR post-up ਰੁਕਾਵਟ | reboot ਤੋਂ ਪਹਿਲਾਂ `/etc/network/interfaces` ਠੀਕ ਕਰਦੀ ਹੈ |
| `systemd-journald-audit.socket` | ਲਾਗਾਂ ਦੀ ਭਰਮਾਰ ਰੋਕਣ ਲਈ ਬੰਦ ਕਰਦੀ ਹੈ |
| UEFI + LVM GRUB ਸਮੱਸਿਆ | `grub-efi-amd64` install ਕਰਦੀ ਹੈ ਅਤੇ `/root/` ਵਿੱਚ cheat-sheet ਲਿਖਦੀ ਹੈ |
| ਤੀਜੀ ਧਿਰ ਦੀਆਂ `bookworm` ਰਿਪੋਜ਼ਟਰੀਆਂ | comment ਕਰਕੇ ਅੱਪਡੇਟ ਕਰਨ ਦੀ ਯਾਦ ਦਿਵਾਉਂਦੀ ਹੈ |
| `linux-image-amd64` conflict | ਮੌਜੂਦ ਹੋਵੇ ਤਾਂ ਹਟਾਉਂਦੀ ਹੈ |
| LVM ਆਪਣੇ ਆਪ ਸਰਗਰਮ ਹੋਣਾ | ਮਾਈਗ੍ਰੇਸ਼ਨ ਸਕ੍ਰਿਪਟ, ਅੱਪਗ੍ਰੇਡ ਤੋਂ ਪਹਿਲਾਂ ਅਤੇ ਬਾਅਦ ਚਲਾਉਂਦੀ ਹੈ |
| Proxmox ਬੈਕਅੱਪ ਸਰਵਰ | `pbs3to4 --full` ਜਾਂਚ ਚਲਾ ਕੇ PBS ਰਿਪੋਜ਼ਟਰੀਆਂ ਨੂੰ Trixie ਲਈ ਅੱਪਡੇਟ ਕਰਦੀ ਹੈ |
| ZFS ਮੂਲ ਸਿਸਟਮ | ਪਛਾਣ ਕੇ ਦਰਜ ਕਰਦੀ ਹੈ (ਖਾਸ ਕਾਰਵਾਈ ਨਹੀਂ) |

ਸਾਰੇ ਬਦਲਾਅ `/var/log/pve8to9-upgrade-<timestamp>.log` ਵਿੱਚ ਦਰਜ ਹੁੰਦੇ ਹਨ। APT ਰਿਪੋਜ਼ਟਰੀ ਬੈਕਅੱਪ `/root/pve8to9-apt-backups/` ਵਿੱਚ ਲਿਖੇ ਜਾਂਦੇ ਹਨ, `/etc/apt/sources.list.d/` ਵਿੱਚ `.bak` ਵਜੋਂ ਕਦੇ ਨਹੀਂ (ਇਸ ਨਾਲ web UI ਵਿੱਚ “invalid extension” (ਅਵੈਧ ਐਕਸਟੈਂਸ਼ਨ) error ਆਵੇਗਾ)।

### ਇੰਸਟਾਲੇਸ਼ਨ ਅਤੇ ਵਰਤੋਂ

```bash
# Script ਡਾਊਨਲੋਡ ਕਰੋ
curl -fsSL https://gist.githubusercontent.com/simeononsecurity/ba3831f487c4e960f9e218c7da5c4b8d/raw/pve8to9-upgrade.sh \
  -o pve8to9-upgrade.sh

# Executable ਬਣਾਓ
chmod +x pve8to9-upgrade.sh

# ਚਲਾਉਣ ਤੋਂ ਪਹਿਲਾਂ ਵੇਖੋ (root ਵਜੋਂ ਚਲਾਉਣ ਤੋਂ ਪਹਿਲਾਂ script ਪੜ੍ਹੋ)
less pve8to9-upgrade.sh
```

**ਚਲਾਉਣ ਦੇ ਢੰਗ:**

```bash
# ਪੂਰਾ interactive mode (ਸਿਫ਼ਾਰਸ਼ੀ)
./pve8to9-upgrade.sh

# ਸਾਰੇ ਸੁਰੱਖਿਅਤ, ਗੈਰ-ਵਿਨਾਸ਼ਕਾਰੀ ਸੁਧਾਰ ਆਪਣੇ ਆਪ ਮਨਜ਼ੂਰ ਕਰੋ
./pve8to9-upgrade.sh --yes

# Dry run: ਬਦਲਾਅ ਦਿਖਾਓ, ਲਾਗੂ ਨਾ ਕਰੋ
./pve8to9-upgrade.sh --dry-run

# pve8to9 --full ਪਹਿਲਾਂ ਦੀ ਜਾਂਚ ਛੱਡੋ (ਸਿਫ਼ਾਰਸ਼ੀ ਨਹੀਂ)
./pve8to9-upgrade.sh --skip-preflight
```

*SSH ਰਾਹੀਂ ਜੁੜੇ ਹੋਵੋ ਤਾਂ `tmux` ਜਾਂ `screen` ਵਿੱਚ ਚਲਾਓ।*

### Script ਦਾ output ਕਿਹੋ ਜਿਹਾ ਹੁੰਦਾ ਹੈ

ਅੱਗੇ ਵਧਣ ਲਈ ਪੁੱਛਣ ਤੋਂ ਪਹਿਲਾਂ script configuration ਦਾ ਸਾਰ ਦਿਖਾਉਂਦੀ ਹੈ:

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

### Script ਦੀਆਂ ਰੋਕਣ ਵਾਲੀਆਂ ਸੁਰੱਖਿਆ ਜਾਂਚਾਂ

ਹੇਠਾਂ ਵਿੱਚੋਂ ਕੋਈ ਵੀ ਹਾਲਤ ਹੋਵੇ ਤਾਂ script **ਅੱਗੇ ਚੱਲਣ ਤੋਂ ਇਨਕਾਰ ਕਰਦੀ ਹੈ**:

- Kernel command line ਵਿੱਚ cgroup V1 ਸਪਸ਼ਟ ਤੌਰ ’ਤੇ ਚਾਲੂ ਹੈ
- Ceph ਹਾਲੇ Quincy (17.x) ਜਾਂ Reef (18.x) ਉੱਤੇ ਹੈ; script ਸਹੀ Ceph ਅੱਪਗ੍ਰੇਡ ਕਮਾਂਡਾਂ ਦਿਖਾਉਂਦੀ ਹੈ
- NVIDIA vGPU ਡਰਾਈਵਰ version 570 (GRID 18.3) ਤੋਂ ਪੁਰਾਣਾ ਹੈ
- PVE ਸੰਸਕਰਣ 8.4 ਤੋਂ ਪੁਰਾਣਾ ਹੈ

ਹਰ ਰੋਕਣ ਵਾਲੀ ਸਮੱਸਿਆ ਲਈ script ਹੱਲ ਕਰਨ ਅਤੇ ਮੁੜ ਚਲਾਉਣ ਦੀਆਂ ਸਹੀ commands ਦਿੰਦੀ ਹੈ।

______

## ਜਾਣੀਆਂ ਅੱਪਗ੍ਰੇਡ ਸਮੱਸਿਆਵਾਂ

### UEFI ਮੋਡ ਵਿੱਚ GRUB, LVM ਤੋਂ boot ਨਹੀਂ ਕਰਦਾ

**ਪ੍ਰਭਾਵਿਤ**: PVE 7.x ਤੋਂ ਅੱਪਗ੍ਰੇਡ ਕੀਤੇ, UEFI ਨਾਲ boot ਹੁੰਦੇ ਅਤੇ LVM root ਵਾਲੇ ਸਿਸਟਮ

```bash
# ਸੁਧਾਰ (ਅੱਪਗ੍ਰੇਡ ਮਗਰੋਂ ਚੱਲਦੇ ਸਿਸਟਮ ਉੱਤੇ ਚਲਾਓ):
[ -d /sys/firmware/efi ] && apt install grub-efi-amd64
```

`pve8to9-upgrade.sh` UEFI+LVM ਪਛਾਣ ਕੇ package ਆਪਣੇ ਆਪ install ਕਰਦੀ ਹੈ। ਇਹ `/root/GRUB-RECOVERY-CHEATSHEET.txt` ਵਿੱਚ ਰਿਕਵਰੀ ਸਹਾਇਕ-ਪੱਤਰ ਵੀ ਲਿਖਦੀ ਹੈ।

**ਜੇ node `grub rescue>` ਉੱਤੇ ਅਟਕ ਗਿਆ ਹੋਵੇ** ਜਾਂ “disk 'lvmid/...' not found” (ਡਿਸਕ ਨਹੀਂ ਮਿਲੀ) ਦਿਖਾਵੇ:

1. PVE ISO ਤੋਂ boot ਕਰੋ → Advanced → **Rescue Boot**
2. ਜਾਂ ਅਧਿਕਾਰਕ Wiki ਦਾ [Recover From Grub Failure — LVM ਭਾਗ](https://pve.proxmox.com/wiki/Recover_From_Grub_Failure#Recovering_from_grub_.22disk_not_found.22_error_when_booting_from_LVM) ਮੰਨੋ

### systemd-boot ਮੈਟਾ-ਪੈਕੇਜ dist-upgrade ਰੋਕਦਾ ਹੈ

PVE 8.1–8.4 ISO ਵਾਲੇ ਸਾਰੇ ਸਿਸਟਮਾਂ ਵਿੱਚ `systemd-boot` meta-package ਆਪਣੇ ਆਪ install ਹੁੰਦਾ ਸੀ। Trixie ਵਿੱਚ ਇਸਦੇ hooks ਹੋਰ packages ਦੇ upgrade ਵੇਲੇ ਚਲਦੇ ਹਨ ਅਤੇ ESP mount ਨਾ ਹੋਵੇ ਤਾਂ `dist-upgrade` ਵਿਚਕਾਰ ਰੋਕ ਸਕਦੇ ਹਨ (Debian Bug #1110177)।

```bash
# dist-upgrade ਤੋਂ ਪਹਿਲਾਂ ਹਟਾਓ:
apt remove systemd-boot
# systemd-boot-efi ਜਾਂ systemd-boot-tools ਨਾ ਹਟਾਓ; ਇਹ ਰਹਿਣੇ ਚਾਹੀਦੇ ਹਨ
```

`pve8to9-upgrade.sh` ਇਹ ਆਪਣੇ ਆਪ ਸੰਭਾਲਦੀ ਅਤੇ ਕਾਰਨ ਸਮਝਾਉਂਦੀ ਹੈ।

### Kernel 6.14 ਨਾਲ PCI ਪਾਸਥਰੂ ਕਦੇ-ਕਦੇ ਟੁੱਟਦਾ ਹੈ

ਕੁਝ ਵਰਤੋਂਕਾਰਾਂ ਨੇ ਦੱਸਿਆ ਕਿ PCI ਪਾਸਥਰੂ ਵਾਲੀਆਂ VMs kernel 6.14 ਉੱਤੇ ਸ਼ੁਰੂ ਨਹੀਂ ਹੁੰਦੀਆਂ। ਪ੍ਰਭਾਵਿਤ ਹੋਵੋ ਤਾਂ:

```bash
# ਪੁਰਾਣਾ kernel ਅਸਥਾਈ ਤੌਰ ’ਤੇ pin ਕਰੋ:
proxmox-boot-tool kernel pin 6.8.12-4-pve
```

### Ceph full-mesh setup reboot ਵੇਲੇ deadlock ਕਰਦੇ ਹਨ

ਜੇ `/etc/network/interfaces` ਵਿੱਚ ਇਹ ਹੋਵੇ:

```
post-up /usr/bin/systemctl restart frr.service
```

ਇਸਦੀ ਥਾਂ ਇਹ ਕਰੋ:

```
post-up /usr/bin/systemctl is-active --quiet frr.service && /usr/bin/systemctl restart frr.service || true
```

ਇਹ **reboot ਤੋਂ ਪਹਿਲਾਂ** ਕਰੋ। Script ਇਹ pattern ਆਪਣੇ ਆਪ ਪਛਾਣ ਕੇ ਠੀਕ ਕਰਦੀ ਹੈ।

### LVM thin pool ਦੀ ਮੁਰੰਮਤ ਲੋੜੀਂਦੀ ਹੈ

ਅੱਪਗ੍ਰੇਡ ਤੋਂ ਬਾਅਦ ਕੁਝ ਸਿਸਟਮ ਇਹ ਦਿਖਾ ਸਕਦੇ ਹਨ:

```
Check of pool pve/data failed (status:64). Manual repair required!
```

ਇਸ ਤਰ੍ਹਾਂ ਠੀਕ ਕਰੋ:

```bash
lvconvert --repair pve/data
```

### NVIDIA vGPU ਡਰਾਈਵਰ ਦਾ ਘੱਟੋ-ਘੱਟ ਸੰਸਕਰਣ

ਅੱਪਗ੍ਰੇਡ ਤੋਂ ਪਹਿਲਾਂ driver ਘੱਟੋ-ਘੱਟ **570.158.02** (GRID 18.3) ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ। ਪੁਰਾਣੇ drivers kernel 6.x ਨਾਲ ਅਨੁਕੂਲ ਨਹੀਂ।

```bash
nvidia-smi --query-gpu=driver_version --format=csv,noheader
```

______

## Cluster ਅੱਪਗ੍ਰੇਡ ਕ੍ਰਮ

Nodes ਨੂੰ ਇੱਕ-ਇੱਕ ਕਰਕੇ ਅੱਪਗ੍ਰੇਡ ਕਰੋ। ਅਗਲਾ ਸ਼ੁਰੂ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ ਹਰ node ਠੀਕ ਹੈ, ਇਹ ਜਾਂਚੋ।

```bash
# ਹਰ node upgrade ਤੋਂ ਪਹਿਲਾਂ cluster health ਜਾਂਚੋ:
pvecm status
ceph -s   # ਜੇ Ceph deploy ਕੀਤਾ ਹੈ
```

**ਅਧੂਰੇ ਅੱਪਗ੍ਰੇਡ ਵੇਲੇ migration ਦੇ ਨਿਯਮ:**

- PVE 8 ਤੋਂ PVE 9 VM/CT: ਹਮੇਸ਼ਾ ਕੰਮ ਕਰਦਾ ਹੈ
- PVE 9 ਤੋਂ PVE 8 VM/CT: ਆਮ ਤੌਰ ’ਤੇ ਸਮਰਥਿਤ ਨਹੀਂ

ਸਾਰੇ nodes PVE 9 ਉੱਤੇ ਹੋਣ ਮਗਰੋਂ HA groups ਆਪਣੇ ਆਪ HA affinity ਨਿਯਮ ਵਿੱਚ migrate ਹੁੰਦੇ ਹਨ। Errors ਵੇਖੋ:

```bash
journalctl -eu pve-ha-crm
```

______

## ਸਮੱਸਿਆ ਨਿਵਾਰਨ

### ਅੱਪਗ੍ਰੇਡ ਰੁਕ ਜਾਵੇ: `proxmox-ve` ਪੈਕੇਜ ਹਟਾਉਣ ਦੀ ਚੇਤਾਵਨੀ

ਜੇ ਇਹ ਵੇਖੋ:
```
W: (pve-apt-hook) You are attempting to remove the meta-package 'proxmox-ve'!
```

ਇੱਕ ਜਾਂ ਵੱਧ packages ਅੱਪਗ੍ਰੇਡ ਨਹੀਂ ਹੋ ਸਕਦੇ ਕਿਉਂਕਿ Bookworm repository ਹਾਲੇ ਸੰਰਚਿਤ ਹੈ। ਬਚੀਆਂ entries ਲੱਭੋ:

```bash
grep -r 'bookworm' /etc/apt/sources.list /etc/apt/sources.list.d/
```

ਉਨ੍ਹਾਂ ਨੂੰ comment ਕਰੋ, ਫਿਰ ਚਲਾਓ:

```bash
apt update && apt dist-upgrade
```

ਜੇ ਕੰਮ ਅਧੂਰਾ ਮੁੱਕਿਆ ਹੋਵੇ:

```bash
apt -f install
```

### ZFS ਅੱਪਗ੍ਰੇਡ ਮਗਰੋਂ boot ਨਾ ਹੋਵੇ

ਜੇ ਪੁਰਾਣੇ BIOS ਬੂਟ ਨਾਲ ZFS ਮੂਲ ਸਿਸਟਮ ਵਰਤਦੇ ਹੋ, [ZFS: Legacy-Boot ਤੋਂ Proxmox Boot Tool ਵੱਲ ਜਾਓ](https://pve.proxmox.com/wiki/ZFS:_Switch_Legacy-Boot_to_Proxmox_Boot_Tool) ਵੇਖੋ। ZFS ਸਿਸਟਮਾਂ ਵਿੱਚ boot ਦਾ ਪ੍ਰਬੰਧ `proxmox-boot-tool` ਕਰੇ, ਸਿੱਧਾ GRUB ਨਹੀਂ, ਤਾਂ ਜੋ ZFS ਵਿਸ਼ੇਸ਼ਤਾ ਅੱਪਗ੍ਰੇਡ ਮਗਰੋਂ boot ਚੱਲੇ।

______

## ਅੱਪਗ੍ਰੇਡ ਮਗਰੋਂ checklist

ਹਰ node reboot ਹੋਣ ਮਗਰੋਂ:

- [ ] Browser cache ਸਾਫ਼ ਕਰੋ (`Ctrl+Shift+R` / `⌘+Alt+R`)
- [ ] `pveversion` ਵਿੱਚ 9.x ਹੋਵੇ
- [ ] `uname -r` ਵਿੱਚ 6.14.x ਜਾਂ ਨਵਾਂ ਹੋਵੇ
- [ ] ਸਾਰੀਆਂ VMs ਅਤੇ CTs ਠੀਕ ਸ਼ੁਰੂ ਹੋਣ
- [ ] Ceph ਸਿਹਤ: `ceph -s` ਵਿੱਚ HEALTH_OK ਹੋਵੇ
- [ ] UEFI+LVM ਹੋਵੇ ਤਾਂ `grubx64.efi` ਦਾ mtime ਨਵਾਂ ਹੋਵੇ
- [ ] NVIDIA ਪਾਸਥਰੂ ਹੋਵੇ ਤਾਂ non-production VM ਜਾਂਚੋ
- [ ] ਅੱਪਗ੍ਰੇਡ ਦੌਰਾਨ comment ਕੀਤੀਆਂ ਤੀਜੀ-ਧਿਰ ਰਿਪੋਜ਼ਟਰੀਆਂ ਅੱਪਡੇਟ ਕਰੋ
- [ ] `/etc/sysctl.conf` ਦੀਆਂ ਕਸਟਮ ਸੈਟਿੰਗਾਂ `/etc/sysctl.d/` ਵਿੱਚ ਲਿਜਾਓ

______

## ਅੱਪਗ੍ਰੇਡ ਮਗਰੋਂ ਜਾਂਚ

ਅੱਪਗ੍ਰੇਡ ਤੋਂ ਬਾਅਦ repositories ਦੀ ਸੰਰਚਨਾ, ਕਲੱਸਟਰ ਕੋਰਮ, storage ਦੀ ਹਾਲਤ, ਮਹਿਮਾਨ ਬੂਟ, backups, ਫਾਇਰਵਾਲ ਨਿਯਮ ਅਤੇ ਪ੍ਰਬੰਧਨ ਪਹੁੰਚ ਜਾਂਚੋ। ਅੱਪਗ੍ਰੇਡ ਮੁਕੰਮਲ ਕਹਿਣ ਤੋਂ ਪਹਿਲਾਂ ਸਿਸਟਮ ਲਾਗ ਵੇਖੋ। ਜੇ cluster ਮਨਜ਼ੂਰੀ ਦੇਵੇ ਤਾਂ ਵੱਖਰੇ host ਉੱਤੇ ਮਹਿਮਾਨ ਰੀਸਟੋਰ ਜਾਂਚੋ।

Version-specific commands ਲਈ ਮੌਜੂਦਾ [Proxmox VE ਪ੍ਰਸ਼ਾਸਨ ਗਾਈਡ](https://pve.proxmox.com/pve-docs/) ਅਤੇ [ਰੀਲੀਜ਼ ਨੋਟ](https://pve.proxmox.com/wiki/Roadmap) ਵੇਖੋ। Target version ਅਤੇ backup ਦੀ ਹਾਲਤ ਜਾਂਚੇ ਬਿਨਾਂ ਪੁਰਾਣੇ release ਦੀ command ਨਾ ਲਵੋ।

## ਹਵਾਲੇ

1. [ਅਧਿਕਾਰਕ: Proxmox VE 8 ਤੋਂ 9 ਅੱਪਗ੍ਰੇਡ](https://pve.proxmox.com/wiki/Upgrade_from_8_to_9)
2. [ਅਧਿਕਾਰਕ: 8 ਤੋਂ 9 ਅੱਪਗ੍ਰੇਡ — ਪਹਿਲਾਂ ਦੀਆਂ ਸ਼ਰਤਾਂ](https://pve.proxmox.com/wiki/Upgrade_from_8_to_9#Prerequisites)
3. [pve8to9-upgrade.sh ਆਟੋਮੇਸ਼ਨ ਸਕ੍ਰਿਪਟ](https://gist.github.com/simeononsecurity/ba3831f487c4e960f9e218c7da5c4b8d)
4. [Proxmox VE 9.0 ਜਾਣੀਆਂ ਸਮੱਸਿਆਵਾਂ (Roadmap)](https://pve.proxmox.com/wiki/Roadmap#9.0-known-issues)
5. [LVM ਕਰਕੇ GRUB boot failure ਤੋਂ ਰਿਕਵਰੀ, “disk not found” (ਡਿਸਕ ਨਹੀਂ ਮਿਲੀ) error](https://pve.proxmox.com/wiki/Recover_From_Grub_Failure#Recovering_from_grub_.22disk_not_found.22_error_when_booting_from_LVM)
6. [ZFS: Legacy-Boot ਤੋਂ Proxmox Boot Tool ਵੱਲ ਜਾਓ](https://pve.proxmox.com/wiki/ZFS:_Switch_Legacy-Boot_to_Proxmox_Boot_Tool)
7. [Ceph Reef ਤੋਂ Squid ਅੱਪਗ੍ਰੇਡ ਗਾਈਡ](https://pve.proxmox.com/wiki/Ceph_Reef_to_Squid)
8. [Proxmox network interface pinning](https://pve.proxmox.com/pve-docs/chapter-sysadmin.html)
9. [Debian 13 Trixie ਰੀਲੀਜ਼ ਨੋਟ](https://www.debian.org/releases/trixie/releasenotes)
