---
title: "Proxmox VE 9: ਵਰਚੁਅਲ ਡਿਸਕ ਦੀ ਵਰਤੋਂ ਘਟਾਓ ਅਤੇ ਥਾਂ ਵਾਪਸ ਲਵੋ"
date: 2026-11-09
lastmod: 2026-11-20
toc: true
draft: false
description: "Proxmox VE 9 ਵਿੱਚ VM ਅਤੇ LXC ਕੰਟੇਨਰਾਂ ਦੀ ਸਟੋਰੇਜ ਵਰਤੋਂ ਘਟਾਓ। ਫਾਰਮੈਟ ਅਤੇ ਬੈਕਐਂਡ ਦੀ ਤੁਲਨਾ ਕਰੋ, discard ਚਾਲੂ ਕਰੋ, trim ਚਲਾਓ ਅਤੇ ਥਾਂ ਵਾਪਸ ਲੈਣ ਤੋਂ ਪਹਿਲਾਂ ਸਨੈਪਸ਼ਾਟ ਜਾਂਚੋ।"
genre: ["ਵਰਚੁਅਲਾਈਜ਼ੇਸ਼ਨ", "Linux ਪ੍ਰਸ਼ਾਸਨ", "Proxmox VE ਪਲੇਟਫਾਰਮ", "ਸਟੋਰੇਜ", "ਘਰੇਲੂ ਲੈਬ"]
tags: ["Proxmox VE 9 ਡਿਸਕ ਥਾਂ", "Proxmox ਵਿੱਚ ਪਤਲੀ ਵੰਡ", "Proxmox discard ਸੂਚਨਾ", "Proxmox TRIM ਕਮਾਂਡ", "Proxmox Windows ਗੈਸਟ ਦੀ ReTrim", "Proxmox Linux ਗੈਸਟ ਲਈ fstrim", "Proxmox LXC ਡਿਸਕ ਵਰਤੋਂ", "Proxmox LVM ਪਤਲੀ ਵੰਡ", "Proxmox ZFS sparse zvol", "Proxmox Ceph RBD ਬਲਾਕ ਡਿਵਾਈਸ", "Proxmox qcow2 ਫਾਰਮੈਟ", "Proxmox raw ਡਿਸਕ", "Proxmox ਸਨੈਪਸ਼ਾਟ", "ਵਰਚੁਅਲ ਡਿਸਕ ਥਾਂ ਮੁੜ ਪ੍ਰਾਪਤ ਕਰਨਾ", "Proxmox ਸਟੋਰੇਜ ਕਿਸਮਾਂ", "VirtIO SCSI ਕੰਟਰੋਲਰ", "Proxmox ਜ਼ੀਰੋ ਲਿਖਤ ਪਛਾਣ", "Proxmox ਬੈਕਅੱਪ ਸਟੋਰੇਜ"]
cover: "/img/cover/proxmox-ve-9-virtual-disk-space-reclamation.webp"
coverAlt: "ਤੀਰ ਨਾਲ ਜੁੜੀਆਂ ਦੋ ਬਲਾਕ ਗਰਿੱਡਾਂ ਵਰਚੁਅਲ ਡਿਸਕ ਦੇ ਵਰਤੇ ਬਲਾਕ ਅਤੇ ਸਟੋਰੇਜ ਪੂਲ ਦੀ ਖਾਲੀ ਸਮਰੱਥਾ ਦਿਖਾਉਂਦੀਆਂ ਹਨ।"
coverCaption: "ਗੈਸਟ ਵਿੱਚੋਂ ਫ਼ਾਈਲਾਂ ਮਿਟਾਉਣਾ, discard ਭੇਜਣਾ ਅਤੇ ਸਟੋਰੇਜ ਤੋਂ ਥਾਂ ਵਾਪਸ ਲੈਣਾ ਵੱਖਰੇ ਕਦਮ ਹਨ।"
---

**ਗੈਸਟ ਦਾ ਛੋਟਾ ਫ਼ਾਈਲ ਸਿਸਟਮ ਹਮੇਸ਼ਾ Proxmox ਸਟੋਰੇਜ ਦੀ ਵਰਤੋਂ ਘੱਟ ਨਹੀਂ ਕਰਦਾ।** ਹੋਸਟ ਉੱਤੇ ਥਾਂ ਖਾਲੀ ਕਰਨ ਲਈ ਪਤਲੀ ਵੰਡ ਵਾਲੀ ਡਿਸਕ, VM ਲਈ ਚੱਲਦਾ discard ਰਸਤਾ ਅਤੇ ਸਨੈਪਸ਼ਾਟਾਂ ਵੱਲੋਂ ਰੋਕੇ ਬਲਾਕਾਂ ਤੋਂ ਮੁਕਤ ਬੈਕਐਂਡ ਚਾਹੀਦਾ ਹੈ। ਇਹ ਗਾਈਡ Proxmox VE 9 VM ਅਤੇ LXC ਕੰਟੇਨਰਾਂ ਲਈ ਸੈਟਿੰਗਾਂ ਅਤੇ ਜਾਂਚਾਂ ਦੱਸਦੀ ਹੈ।

<!--more-->

## ਮੁੱਖ ਗੱਲਾਂ

- **ਪਹਿਲਾਂ ਬੈਕਿੰਗ ਸਟੋਰੇਜ ਚੁਣੋ।** ਵਰਚੁਅਲ ਡਿਸਕ ਦਾ ਦੱਸਿਆ ਆਕਾਰ ਹੋਸਟ ਉੱਤੇ ਦਿੱਤੀ ਥਾਂ ਤੋਂ ਸਿਰਫ਼ ਉਦੋਂ ਵੱਖਰਾ ਹੁੰਦਾ ਹੈ ਜਦੋਂ ਇਮੇਜ ਫਾਰਮੈਟ ਜਾਂ ਬੈਕਐਂਡ ਪਤਲੀ ਵੰਡ ਸਹਾਇਕ ਹੋਵੇ।
- **VM ਲਈ discard ਚਾਲੂ ਕਰੋ, ਫਿਰ ਗੈਸਟ ਵਿੱਚ trim ਚਲਾਓ।** Windows ReTrim ਅਤੇ Linux `fstrim` ਵਰਚੁਅਲ ਡਿਸਕ ਰਾਹੀਂ ਨਾ ਵਰਤੇ ਬਲਾਕਾਂ ਲਈ ਬੇਨਤੀਆਂ ਭੇਜਦੇ ਹਨ।
- **ਸਨੈਪਸ਼ਾਟਾਂ ਅਤੇ ਬੈਕਅੱਪਾਂ ਦੀ ਵੱਖ-ਵੱਖ ਜਾਂਚ ਕਰੋ।** ਪੁਰਾਣੇ ਬਲਾਕ ਉਦੋਂ ਤੱਕ ਦਿੱਤੇ ਰਹਿੰਦੇ ਹਨ ਜਦੋਂ ਤੱਕ ਕੋਈ ਸਨੈਪਸ਼ਾਟ ਉਹਨਾਂ ਦਾ ਹਵਾਲਾ ਦਿੰਦਾ ਹੈ। ਬੈਕਅੱਪ ਫ਼ਾਈਲਾਂ ਅਤੇ PBS ਡਾਟਾ ਖੰਡ ਦੀ ਆਪਣੀ retention ਨੀਤੀ ਹੁੰਦੀ ਹੈ।
- **LXC ਮਾਊਂਟ ਨੂੰ ਕਿਸਮ ਅਨੁਸਾਰ ਦੇਖੋ।** ਪ੍ਰਬੰਧਿਤ rootfs ਅਤੇ ਮਾਊਂਟ-point ਵਾਲਿਊਮ, bind ਮਾਊਂਟ ਅਤੇ device ਮਾਊਂਟ ਦੀ ਮਾਲਕੀ ਅਤੇ ਬੈਕਅੱਪ ਵਿਹਾਰ ਵੱਖਰਾ ਹੁੰਦਾ ਹੈ।

## ਸ਼ੁਰੂ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ

ਤੁਹਾਨੂੰ **Proxmox VE 9 ਦਾ ਪ੍ਰਸ਼ਾਸਕ ਪਹੁੰਚ**, ਪ੍ਰਭਾਵਿਤ ਹਰ ਗੈਸਟ ਦਾ ਜਾਂਚਿਆ ਬੈਕਅੱਪ ਅਤੇ ਕਾਰਵਾਈ ਲਈ ਪੂਲ ਵਿੱਚ ਕਾਫ਼ੀ ਖਾਲੀ ਥਾਂ ਚਾਹੀਦੀ ਹੈ। ਸੈਟਿੰਗਾਂ ਬਦਲਣ ਤੋਂ ਪਹਿਲਾਂ ਗੈਸਟ ID, ਡਿਸਕ ਬੱਸ, ਵਾਲਿਊਮ ID, ਸਟੋਰੇਜ ID, ਸਨੈਪਸ਼ਾਟ ਅਤੇ ਮੌਜੂਦਾ ਵਰਤੋਂ ਲਿਖੋ। ਰਿਕਵਰੀ ਦੀ ਜਾਂਚ ਲਈ [VM ਮੁੜ-ਬਹਾਲੀ ਅਭਿਆਸ](/articles/proxmox-vm-backup-restore-drill/) ਵਰਤੋ।

**ਅੰਦਾਜ਼ੀ ਸਮਾਂ:** ਹਰ ਗੈਸਟ ਲਈ 20 ਤੋਂ 60 ਮਿੰਟ, ਨਾਲ ਵੱਡੇ trim ਜਾਂ ਸਫ਼ਾਈ ਕੰਮ ਦਾ ਵਾਧੂ ਸਮਾਂ। **ਮੁਸ਼ਕਲ:** ਦਰਮਿਆਨੀ। ਘੱਟ ਜੋਖਮ ਵਾਲੀ ਇੱਕ VM ਨਾਲ ਸ਼ੁਰੂ ਕਰੋ ਅਤੇ ਪਹਿਲਾਂ ਤੇ ਬਾਅਦ ਦੀ ਸਟੋਰੇਜ ਵਰਤੋਂ ਦੀ ਤੁਲਨਾ ਕਰੋ।

> **ਚੇਤਾਵਨੀ:** ਭਰਿਆ ਪਤਲਾ ਪੂਲ ਗੈਸਟਾਂ ਵਿੱਚ I/O ਗਲਤੀਆਂ ਪੈਦਾ ਕਰਦਾ ਹੈ ਅਤੇ ਫ਼ਾਈਲ ਸਿਸਟਮ ਨੂੰ ਨੁਕਸਾਨ ਪਹੁੰਚਾ ਸਕਦਾ ਹੈ। ਪੂਲ ਦੀ ਖਾਲੀ ਡਾਟਾ ਅਤੇ ਮੈਟਾਡੇਟਾ ਥਾਂ ਦੀ ਨਿਗਰਾਨੀ ਤੋਂ ਬਿਨਾਂ ਸਮਰੱਥਾ ਤੋਂ ਵੱਧ ਥਾਂ ਨਾ ਦਿਓ। [Proxmox ਸਟੋਰੇਜ ਦਸਤਾਵੇਜ਼](https://github.com/proxmox/pve-docs/blob/master/pvesm.adoc)

## ਅਲਾਟਮੈਂਟ ਲੜੀ ਦੀ ਜਾਂਚ ਕਰੋ

**ਮਿਟਾਉਣਾ**, **discard** ਅਤੇ **ਥਾਂ ਵਾਪਸ ਲੈਣਾ** ਵੱਖਰੀਆਂ ਪਰਤਾਂ ਉੱਤੇ ਹੁੰਦਾ ਹੈ। ਗੈਸਟ ਫ਼ਾਈਲ ਮਿਟਾ ਕੇ ਫ਼ਾਈਲ ਸਿਸਟਮ ਬਲਾਕਾਂ ਨੂੰ ਖਾਲੀ ਨਿਸ਼ਾਨ ਲਗਾਉਂਦਾ ਹੈ। ਫ਼ਾਈਲ ਸਿਸਟਮ ਉਹਨਾਂ ਬਲਾਕਾਂ ਲਈ TRIM ਜਾਂ UNMAP ਭੇਜਦਾ ਹੈ। ਵਰਚੁਅਲ ਡਿਸਕ ਉੱਤੇ discard ਚਾਲੂ ਹੋਵੇ ਤਾਂ QEMU ਬੇਨਤੀ ਅੱਗੇ ਭੇਜਦਾ ਹੈ। ਫਾਰਮੈਟ ਅਤੇ ਪੂਲ ਸਹਾਇਕ ਹੋਣ ਉੱਤੇ ਬੈਕਐਂਡ ਭੌਤਿਕ ਅਲਾਟਮੈਂਟ ਛੱਡਦਾ ਹੈ। [Proxmox VM ਡਿਸਕ ਦਸਤਾਵੇਜ਼](https://github.com/proxmox/pve-docs/blob/master/qm.adoc)

| ਪਰਤ | ਕੀ ਜਾਂਚਣਾ ਹੈ | ਲਾਭਦਾਇਕ ਸਬੂਤ |
|---|---|---|
| **ਗੈਸਟ ਫ਼ਾਈਲਾਂ** | ਫ਼ਾਈਲ ਸਿਸਟਮ ਦੀ ਖਾਲੀ ਥਾਂ | Windows ਵਾਲਿਊਮ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਜਾਂ Linux `df -h` |
| **ਵਰਚੁਅਲ ਡਿਸਕ** | ਬੱਸ, discard, SSD ਦੀ ਨਕਲ, ਇਮੇਜ ਫਾਰਮੈਟ | VM ਦਾ **Hardware** ਟੈਬ ਜਾਂ `qm config VMID` |
| **PVE ਵਾਲਿਊਮ** | ਮਾਲਕ ਅਤੇ ਕੌਂਫਿਗਰ ਆਕਾਰ | ਸਟੋਰੇਜ ਦਾ **Content** ਟੈਬ ਜਾਂ `pvesm list STORAGE_ID` |
| **ਸਟੋਰੇਜ ਪੂਲ** | ਖਾਲੀ ਡਾਟਾ, ਮੈਟਾਡੇਟਾ ਅਤੇ ਰੋਕੇ ਬਲਾਕ | `pvesm status` ਅਤੇ ਬੈਕਐਂਡ ਦੇ ਖ਼ਾਸ ਟੂਲ |

**100 GiB ਦੀ ਵਰਚੁਅਲ ਡਿਸਕ ਸਮਰੱਥਾ ਹੱਦ ਹੈ, 100 GiB ਅਲਾਟ ਹੋਣ ਦੀ ਗਾਰੰਟੀ ਨਹੀਂ।** ਇਸੇ ਤਰ੍ਹਾਂ ਗੈਸਟ ਵੱਲੋਂ 20 GiB ਵਰਤੋਂ ਦਿਖਾਉਣਾ ਇਹ ਸਾਬਤ ਨਹੀਂ ਕਰਦਾ ਕਿ ਹੋਸਟ ਵੀ 20 GiB ਵਰਤਦਾ ਹੈ। ਮੈਟਾਡੇਟਾ, ਸਨੈਪਸ਼ਾਟ, ਬੈਕਅੱਪ ਕਾਪੀਆਂ ਅਤੇ ਪਹਿਲਾਂ ਲਿਖੇ ਬਲਾਕ ਅੰਕੜਾ ਬਦਲਦੇ ਹਨ। [Proxmox ਸਟੋਰੇਜ ਦਸਤਾਵੇਜ਼](https://github.com/proxmox/pve-docs/blob/master/pvesm.adoc)

## ਡਿਸਕ ਫਾਰਮੈਟਾਂ ਦੀ ਤੁਲਨਾ ਕਰੋ

**ਸਟੋਰੇਜ ਬੈਕਐਂਡ ਨਿਰਧਾਰਤ ਕਰਦਾ ਹੈ ਕਿ Proxmox ਕਿਹੜੇ ਇਮੇਜ ਫਾਰਮੈਟ ਦਿੰਦਾ ਹੈ।** ZFS zvol ਅਤੇ Ceph RBD ਵਰਚੁਅਲ raw ਡਿਸਕਾਂ ਵਰਤਦੇ ਹਨ। LVM ਆਮ ਤੌਰ ਉੱਤੇ raw ਵਰਤਦਾ ਹੈ, ਹੇਠਾਂ ਦੱਸੀ Proxmox VE 9 ਵਾਲਿਊਮ-chain ਛੋਟ ਤੋਂ ਇਲਾਵਾ। directory ਅਤੇ NFS ਵਰਗੇ ਫ਼ਾਈਲ ਬੈਕਐਂਡ raw ਜਾਂ qcow2 ਸਹਾਇਕ ਕਰਦੇ ਹਨ। Raw ਇਕੱਲਾ ਪਤਲਾ ਅਲਾਟਮੈਂਟ ਜਾਂ ਸਨੈਪਸ਼ਾਟ ਨਹੀਂ ਦਿੰਦਾ। ਇਹ ਗੁਣ ਹੇਠਲੀ ਸਟੋਰੇਜ ਨੂੰ ਦੇਣੇ ਪੈਂਦੇ ਹਨ। Qcow2 ਇਮੇਜ ਪਰਤ ਉੱਤੇ copy-on-write ਅਲਾਟਮੈਂਟ ਅਤੇ ਸਨੈਪਸ਼ਾਟ ਦਿੰਦਾ ਹੈ। [Proxmox VM ਡਿਸਕ ਦਸਤਾਵੇਜ਼](https://github.com/proxmox/pve-docs/blob/master/qm.adoc)

| ਫਾਰਮੈਟ | ਅਲਾਟਮੈਂਟ ਤਰੀਕਾ | ਥਾਂ ਦਾ ਸਮਝੌਤਾ |
|---|---|---|
| **ਫ਼ਾਈਲ ਸਟੋਰੇਜ ਉੱਤੇ qcow2** | ਲਿਖਣ ਵੇਲੇ qcow2 clusters ਅਲਾਟ ਕਰਦਾ ਹੈ | ਇਮੇਜ ਮੈਟਾਡੇਟਾ ਅਤੇ ਸਨੈਪਸ਼ਾਟ ਲੜੀਆਂ ਥਾਂ ਲੈਂਦੀਆਂ ਹਨ |
| **ਫ਼ਾਈਲ ਸਟੋਰੇਜ ਉੱਤੇ raw ਫ਼ਾਈਲ** | ਸਹਾਇਕ ਹੋਵੇ ਤਾਂ ਫ਼ਾਈਲ ਸਿਸਟਮ ਦਾ sparse-ਫ਼ਾਈਲ ਵਿਹਾਰ | Raw ਇਕੱਲਾ ਪਤਲੀ ਵੰਡ ਜਾਂ ਸਨੈਪਸ਼ਾਟ ਨਹੀਂ ਦਿੰਦਾ |
| **Raw ਬਲਾਕ ਵਾਲਿਊਮ** | ਪਤਲੀ ਵੰਡ ਵਾਲਾ LVM, ZFS, Ceph RBD ਜਾਂ ਹੋਰ ਬੈਕਿੰਗ ਸਟੋਰੇਜ | ਪੂਲ ਅਲਾਟਮੈਂਟ ਅਤੇ ਸਨੈਪਸ਼ਾਟ ਬੈਕਐਂਡ ਉੱਤੇ ਨਿਰਭਰ ਹਨ |

**Proxmox VE 9 ਮੋਟਾ LVM ਵਿੱਚ ਸਨੈਪਸ਼ਾਟ ਦਾ ਖ਼ਾਸ ਮੋਡ ਹੈ।** `snapshot-as-volume-chain` ਮੋਟਾ LVM ਤਰਕਸੰਗਤ ਵਾਲਿਊਮ ਵਿਚਕਾਰ qcow2 ਦਾ ਆਧਾਰ ਸੰਬੰਧ ਵਰਤਦਾ ਹੈ। ਇਹ qcow2 ਦੇ ਅੰਦਰੂਨੀ ਸਨੈਪਸ਼ਾਟ ਨਹੀਂ ਵਰਤਦਾ। ਇਹ ਚੋਣ ਸਿਰਫ਼ ਨਵੀਆਂ VM ਡਿਸਕਾਂ ਉੱਤੇ ਅਸਰ ਕਰਦੀ ਹੈ ਅਤੇ ਮੌਜੂਦਾ Proxmox ਦਸਤਾਵੇਜ਼ ਵਿੱਚ ਤਕਨੀਕੀ preview ਹੈ। PVE ਹਰ ਸਨੈਪਸ਼ਾਟ ਨੂੰ ਪੂਰੀ ਤਰ੍ਹਾਂ ਅਲਾਟ ਦਿਖਾਉਂਦਾ ਹੈ। SAN ਦੀ ਅਸਲ ਅਲਾਟਮੈਂਟ ਸਿਰਫ਼ ਉਦੋਂ ਘੱਟ ਹੁੰਦੀ ਹੈ ਜਦੋਂ ਬੈਕਿੰਗ ਸਟੋਰੇਜ ਪਤਲੀ ਵੰਡ ਅਤੇ discard ਸਹਾਇਕ ਕਰੇ। [Proxmox LVM ਸਟੋਰੇਜ ਦਸਤਾਵੇਜ਼](https://github.com/proxmox/pve-docs/blob/master/pve-storage-lvm.adoc)

**ਸਿਰਫ਼ `.raw` ਐਕਸਟੈਂਸ਼ਨ ਕਰਕੇ ਡਿਸਕ convert ਨਾ ਕਰੋ।** ਪਹਿਲਾਂ ਸਟੋਰੇਜ plugin ਅਤੇ ਅਲਾਟ ਬਲਾਕ ਜਾਂਚੋ। `local-lvm` ਦੀ raw ਡਿਸਕ ਦਾ ਅਲਾਟਮੈਂਟ ਆਮ directory ਸਟੋਰੇਜ ਦੀ ਪੂਰੀ ਅਲਾਟ raw ਫ਼ਾਈਲ ਤੋਂ ਵੱਖਰਾ ਹੁੰਦਾ ਹੈ।

## ਸਟੋਰੇਜ ਕਿਸਮਾਂ ਦੀ ਤੁਲਨਾ ਕਰੋ

Proxmox **ਫ਼ਾਈਲ ਸਟੋਰੇਜ** ਅਤੇ **ਬਲਾਕ ਸਟੋਰੇਜ** ਵੱਖ ਕਰਦਾ ਹੈ। ਸਟੋਰੇਜ plugin ਸਨੈਪਸ਼ਾਟ, ਕਲੋਨ, ਸਾਂਝੀ ਵਰਤੋਂ ਅਤੇ ਹਰ ਪੂਲ ਵੱਲੋਂ ਮਨਜ਼ੂਰ content ਕਿਸਮਾਂ ਵੀ ਨਿਰਧਾਰਤ ਕਰਦਾ ਹੈ। ਕਿਸੇ ਫਾਰਮੈਟ ਜਾਂ ਗੁਣ ਉੱਤੇ ਨਿਰਭਰ ਹੋਣ ਤੋਂ ਪਹਿਲਾਂ **Datacenter > ਸਟੋਰੇਜ** ਦੀ ਐਂਟਰੀ ਜਾਂਚੋ। [Proxmox ਸਟੋਰੇਜ ਕਿਸਮਾਂ ਦੀ ਸਾਰਣੀ](https://github.com/proxmox/pve-docs/blob/master/pvesm.adoc)

| ਸਟੋਰੇਜ | VM ਡਿਸਕ ਦਾ ਵਿਹਾਰ | ਵਾਪਸੀ ਜਾਂਚ |
|---|---|---|
| **Directory, ext4, XFS** | Raw ਜਾਂ qcow2 ਫ਼ਾਈਲਾਂ | `du` ਦੇ ਅਲਾਟ bytes ਦੀ ਇਮੇਜ ਦੇ ਵਰਚੁਅਲ ਆਕਾਰ ਨਾਲ ਤੁਲਨਾ ਕਰੋ। ਜੇ ਹੋਰ ਪਰਤ ਸਨੈਪਸ਼ਾਟ ਦਿੰਦੀ ਹੈ ਤਾਂ ਉਹ ਵੀ ਜਾਂਚੋ। |
| **NFS, CIFS** | ਸਾਂਝੀ ਸਟੋਰੇਜ ਉੱਤੇ raw ਜਾਂ qcow2 ਫ਼ਾਈਲਾਂ | ਸਰਵਰ ਉੱਤੇ ਅਲਾਟ ਥਾਂ ਜਾਂਚੋ। ਗੈਸਟ trim ਨਤੀਜਾ ਸਰਵਰ ਦੀ ਥਾਂ ਘਟਣ ਦਾ ਸਬੂਤ ਨਹੀਂ। |
| **LVM ਦੀ ਪਤਲੀ ਵੰਡ (`local-lvm`)** | ਸਿਰਫ਼ ਸਥਾਨਕ ਪਤਲਾ raw ਤਰਕਸੰਗਤ ਵਾਲਿਊਮ | `lvs` ਨਾਲ ਪਤਲਾ ਪੂਲ ਦੇ ਡਾਟਾ ਅਤੇ ਮੈਟਾਡੇਟਾ ਪ੍ਰਤੀਸ਼ਤ ਵੇਖੋ। |
| **LVM thick** | Raw LVs ਜਾਂ VE 9 qcow2 ਵਾਲਿਊਮ chains | ਗੈਸਟ ਵਿੱਚੋਂ ਮਿਟਾਉਣਾ LV ਦੀ ਪੱਕੀ reserve ਘਟਾਉਂਦਾ ਨਹੀਂ। SAN ਪਤਲਾ ਅਲਾਟਮੈਂਟ ਵੱਖਰੇ ਤੌਰ ਉੱਤੇ ਜਾਂਚੋ। |
| **ZFS ਸਟੋਰੇਜ (`local-zfs`)** | raw zvol ਜਾਂ ਕੰਟੇਨਰ subvolumes | `sparse`, dataset ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ, ਪੂਲ ਵਰਤੋਂ ਅਤੇ ਸਨੈਪਸ਼ਾਟ ਜਾਂਚੋ। |
| **Ceph RBD** | ਸਾਂਝੀ ਸਟੋਰੇਜ ਉੱਤੇ ਪਤਲਾ `raw RBD` ਚਿੱਤਰ | Ceph ਪੂਲ ਸਮਰੱਥਾ, ਇਮੇਜ ਵਰਤੋਂ, ਸਨੈਪਸ਼ਾਟ ਅਤੇ discard ਜਾਂਚੋ। |
| **Btrfs** | Raw images ਲਈ Btrfs ਉਪ-ਵਾਲਿਊਮ ਵਾਲੇ ਫ਼ਾਈਲ-backed ਵਾਲਿਊਮ | PVE Btrfs ਪਲੱਗਇਨ ਨੂੰ ਤਕਨੀਕੀ preview ਸਮਝੋ ਅਤੇ ਸਨੈਪਸ਼ਾਟ ਤੇ ਫ਼ਾਈਲ ਸਿਸਟਮ ਵਰਤੋਂ ਜਾਂਚੋ। |

**ਹੋਰ ਸਟੋਰੇਜ plugins ਦੇ ਕੰਮ ਵੱਖਰੇ ਹਨ।** CephFS ਸਾਂਝੀ ਫ਼ਾਈਲ ਸਟੋਰੇਜ ਦਿੰਦਾ ਹੈ। iSCSI ਅਤੇ Fibre Channel ਸਾਂਝੇ ਬਲਾਕ ਯੰਤਰ ਦਿੰਦੇ ਹਨ, ਜਿਨ੍ਹਾਂ ਨੂੰ ਅਕਸਰ LVM ਨਾਲ VM ਵਾਲਿਊਮਾਂ ਵਿੱਚ ਵੰਡਿਆ ਜਾਂਦਾ ਹੈ। iSCSI ਉੱਤੇ ZFS ਦੂਰਲੀ ZFS-ਆਧਾਰਿਤ ਬਲਾਕ ਸਟੋਰੇਜ ਵਰਤਦਾ ਹੈ। Proxmox ਬੈਕਅੱਪ ਸਰਵਰ (PBS) ਬੈਕਅੱਪ ਰੱਖਦਾ ਹੈ, ਸਰਗਰਮ VM ਡਿਸਕਾਂ ਨਹੀਂ। `images`, `rootdir`, `backup` ਜਾਂ `iso` ਡਾਟਾ ਰੱਖਣ ਤੋਂ ਪਹਿਲਾਂ ਚਾਲੂ **Content** ਕਿਸਮਾਂ ਜਾਂਚੋ। [Proxmox ਸਟੋਰੇਜ ਕਿਸਮਾਂ ਦੀ ਸਾਰਣੀ](https://github.com/proxmox/pve-docs/blob/master/pvesm.adoc)

**ਫ਼ਾਈਲ ਸਟੋਰੇਜ ਦੇ ਅਲਾਟਮੈਂਟ flags ਡਿਸਕ ਬਣਾਉਂਦੇ ਸਮੇਂ ਮਹੱਤਵ ਰੱਖਦੇ ਹਨ।** ਸਟੋਰੇਜ ਦਾ `format` ਸਮਰੱਥ ਹੋਣ ਉੱਤੇ `raw`, `qcow2` ਜਾਂ `vmdk` ਚੁਣਦਾ ਹੈ। Raw ਅਤੇ qcow2 ਫ਼ਾਈਲਾਂ ਲਈ `preallocation` ਵਿੱਚ `off`, `metadata`, `falloc` ਜਾਂ `full` ਆ ਸਕਦਾ ਹੈ। ਡਿਫ਼ਾਲਟ `metadata` ਹੈ, ਜੋ raw ਲਈ `off` ਮੰਨਿਆ ਜਾਂਦਾ ਹੈ। `full` ਫ਼ਾਈਲ ਥਾਂ ਪਹਿਲਾਂ ਹੀ ਰੱਖਦਾ ਹੈ ਅਤੇ ਸ਼ੁਰੂਆਤੀ ਘੱਟ ਵਰਤੋਂ ਦਾ ਲਾਭ ਖਤਮ ਕਰਦਾ ਹੈ। ਵੱਡੀ ਡਿਸਕ ਬਣਾਉਣ ਤੋਂ ਪਹਿਲਾਂ ਸਟੋਰੇਜ ਕੌਂਫਿਗਰੇਸ਼ਨ ਵੇਖੋ। `shared` flag ਸਿਰਫ਼ ਮੌਜੂਦਾ ਸਾਂਝੀ ਪਹੁੰਚ ਘੋਸ਼ਿਤ ਕਰਦਾ ਹੈ। ਇਹ ਸਥਾਨਕ ਸਟੋਰੇਜ ਨੂੰ ਸਾਂਝਾ ਨਹੀਂ ਬਣਾਉਂਦਾ। [Proxmox ਦੀਆਂ ਆਮ ਸਟੋਰੇਜ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ](https://github.com/proxmox/pve-docs/blob/master/pvesm.adoc)

**ZFS `sparse` ਪਤਲਾ zvol ਬਣਾਉਣ ਲਈ ਸਟੋਰੇਜ ਸੈਟਿੰਗ ਹੈ।** Sparse zvol ਤੋਂ ਬਿਨਾਂ, ਵਾਲਿਊਮ ਦੇ ਕੌਂਫਿਗਰ ਵਿਹਾਰ ਮੁਤਾਬਕ ਥਾਂ reserve ਹੁੰਦੀ ਹੈ। ਮੌਜੂਦਾ ਤੈਨਾਤੀ ਬਦਲਣ ਤੋਂ ਪਹਿਲਾਂ ਅਸਲ ਸਟੋਰੇਜ ਕੌਂਫਿਗਰੇਸ਼ਨ ਅਤੇ ਪੂਲ ਜਾਂਚੋ। [Proxmox ZFS ਸਟੋਰੇਜ ਦਸਤਾਵੇਜ਼](https://github.com/proxmox/pve-docs/blob/master/pve-storage-zfspool.adoc)

**Directory ਸਟੋਰੇਜ ਲਈ ਦੂਜੀ ਜਾਂਚ ਲੋੜੀਂਦੀ ਹੈ।** qcow2 ਫ਼ਾਈਲ ਦੀ ਤਰਕਸੰਗਤ ਲੰਬਾਈ, ਗੈਸਟ ਨੂੰ ਦਿਸਦੀ ਵਰਚੁਅਲ ਸਮਰੱਥਾ ਨਹੀਂ ਹੁੰਦੀ। `du -h` ਇਮੇਜ ਲਈ ਅਲਾਟ ਫ਼ਾਈਲ ਸਿਸਟਮ ਬਲਾਕ ਦੱਸਦਾ ਹੈ। `ls -lh` ਫ਼ਾਈਲ ਦੀ ਤਰਕਸੰਗਤ ਲੰਬਾਈ ਦਿਖਾਉਂਦਾ ਹੈ। ਬੰਦ VM ਲਈ `qemu-img info` ਵਰਚੁਅਲ ਸਮਰੱਥਾ ਅਤੇ ਹੋਸਟ ਡਿਸਕ ਆਕਾਰ ਦੱਸਦਾ ਹੈ। NFS ਉੱਤੇ ਅੰਤਿਮ ਸਮਰੱਥਾ ਫ਼ੈਸਲੇ ਲਈ ਸਰਵਰ ਦੇ ਹਿਸਾਬ ਉੱਤੇ ਭਰੋਸਾ ਕਰੋ। [QEMU `qemu-img` ਹਵਾਲਾ](https://www.qemu.org/docs/master/tools/qemu-img.html)

**NFS ਵਿੱਚ ਅਲਾਟਮੈਂਟ ਦੀ ਇੱਕ ਹੋਰ ਹੱਦ ਹੈ।** qcow2 ਵੱਲੋਂ ਆਪਣੀ ਫ਼ਾਈਲ ਦੇ ਖਾਲੀ cluster ਨੂੰ ਮੁੜ ਵਰਤਣਾ ਇਹ ਨਹੀਂ ਦੱਸਦਾ ਕਿ NFS ਸਰਵਰ ਫ਼ਾਈਲ ਦੇ ਬਲਾਕ ਛੱਡ ਰਿਹਾ ਹੈ। ਖਾਲੀ ਬਲਾਕ ਛੱਡਣਾ ਲਈ client, ਸਹਿਮਤ ਪ੍ਰੋਟੋਕੋਲ, ਸਰਵਰ ਅਤੇ ਸਰਵਰ ਫ਼ਾਈਲ ਸਿਸਟਮ ਦਾ ਸਮਰਥਨ ਚਾਹੀਦਾ ਹੈ। NFSv4.2 `DEALLOCATE` ਪਰਿਭਾਸ਼ਿਤ ਕਰਦਾ ਹੈ, ਪਰ ਵਰਜਨ ਨੰਬਰ ਇਹ ਸਾਬਤ ਨਹੀਂ ਕਰਦਾ ਕਿ ਸਰਵਰ ਨੇ ਥਾਂ ਵਾਪਸ ਕੀਤੀ। Negotiated NFS ਮਾਊਂਟ ਵੇਖੋ ਅਤੇ ਸਰਵਰ ਉੱਤੇ ਅਲਾਟਮੈਂਟ ਮਾਪੋ। [NFSv4.2 `DEALLOCATE` ਨਿਰਧਾਰਨ](https://www.rfc-editor.org/rfc/rfc7862.html#section-6.2.2)

## VM ਡਿਸਕ ਦੇ ਚੋਣ ਨਿਸ਼ਾਨ ਸੈੱਟ ਕਰੋ

Proxmox ਇੰਟਰਫੇਸ ਵਿੱਚ **VM > Hardware > Hard ਡਿਸਕ > Edit** ਖੋਲ੍ਹੋ। ਡਿਸਕ ਬੱਸ ਅਤੇ advanced ਚੋਣਾਂ ਵੇਖੋ। ਇਹ flags ਅਲਾਟਮੈਂਟ ਬਦਲਦੇ ਹਨ ਜਾਂ ਦੱਸਦੇ ਹਨ ਕਿ ਅਨੁਕੂਲਤਾ ਲਾਭਦਾਇਕ ਹੈ ਜਾਂ ਨਹੀਂ। [ਅਧਿਕਾਰਤ `qm` ਚੋਣ ਹਵਾਲਾ](https://github.com/proxmox/pve-docs/blob/master/generated/qm.conf.5-opts.adoc) ਬੱਸ ਅਨੁਸਾਰ ਉਪਲਬਧਤਾ ਦਿੰਦਾ ਹੈ।

| ਬੱਸ | ਥਾਂ ਨਾਲ ਜੁੜੀ ਚੋਣ |
|---|---|
| **IDE** | ਪੁਰਾਣੇ ਸਿਸਟਮਾਂ ਨਾਲ ਅਨੁਕੂਲਤਾ। ਸਿਰਫ਼ ਜਦੋਂ ਗੈਸਟ ਕੋਲ ਨਵਾਂ ਡਰਾਈਵਰ ਨਾ ਹੋਵੇ। |
| **SATA** | ਵਿਆਪਕ ਤੌਰ ਉੱਤੇ ਸਮਰਥਿਤ emulation। ਵਾਪਸੀ ਉੱਤੇ ਨਿਰਭਰ ਹੋਣ ਤੋਂ ਪਹਿਲਾਂ ਗੈਸਟ trim ਅਤੇ ਡਿਸਕ ਚੋਣਾਂ ਜਾਂਚੋ। |
| **VirtIO SCSI ਨਾਲ SCSI** | discard ਅਤੇ ਪ੍ਰਤੀ-ਡਿਸਕ ਸੈਟਿੰਗਾਂ ਲਈ ਪਸੰਦੀਦਾ ਆਧੁਨਿਕ ਰਸਤਾ। Windows ਨੂੰ VirtIO ਡਰਾਈਵਰ ਚਾਹੀਦਾ ਹੈ। |
| **VirtIO ਬਲਾਕ** | Paravirtualized ਡਿਸਕ। Linux ਦਾ discard ਸੰਕੇਤ ਲਈ kernel 5.0 ਜਾਂ ਨਵਾਂ ਚਾਹੀਦਾ ਹੈ। SSD ਦੀ ਨਕਲ ਨਹੀਂ। |

| ਸੈਟਿੰਗ | ਅਸਰ | ਸਲਾਹ |
|---|---|---|
| **discard ਚਾਲੂ (`on`)** | ਗੈਸਟ TRIM ਜਾਂ UNMAP ਅੱਗੇ ਭੇਜਦਾ ਹੈ | ਸਹਾਇਕ ਪਤਲਾ backend ਉੱਤੇ ਗੈਸਟ ਵੱਲੋਂ ਥਾਂ ਵਾਪਸ ਲੈਣ ਲਈ ਲਾਜ਼ਮੀ। ਡਿਫ਼ਾਲਟ `ignore` forwarding ਰੋਕਦਾ ਹੈ। |
| **SSD ਦੀ ਨਕਲ `ssd=1`** | ਗੈਸਟ ਨੂੰ ਡਿਸਕ SSD ਵਜੋਂ ਦਿਖਾਉਂਦਾ ਹੈ | ਕੁਝ ਗੈਸਟ trim ਭੇਜਣ ਤੋਂ ਪਹਿਲਾਂ ਇਹ ਪਛਾਣ ਚਾਹੁੰਦੇ ਹਨ। ਇਹ ਭੌਤਿਕ ਸਟੋਰੇਜ ਤੇਜ਼ ਨਹੀਂ ਕਰਦਾ। VirtIO ਬਲਾਕ ਵਿੱਚ ਇਹ flag ਨਹੀਂ। |
| **ਜ਼ੀਰੋ ਲਿਖਤ ਪਛਾਣ `detect_zeroes=1`** | ਜ਼ੀਰੋ ਲਿਖਤਾਂ ਪਛਾਣ ਕੇ ਸੁਧਾਰਨ ਦੀ ਕੋਸ਼ਿਸ਼ | ਚੋਣਵਾਂ I/O optimization। ਗੈਸਟ trim ਦੀ ਥਾਂ ਨਹੀਂ ਲੈਂਦਾ ਅਤੇ ਥਾਂ ਵਾਪਸ ਮਿਲਣ ਦੀ ਗਾਰੰਟੀ ਨਹੀਂ। |
| **Bus: SCSI / VirtIO SCSI ਸਿੰਗਲ** | VirtIO ਕੰਟਰੋਲਰ ਰਾਹੀਂ SCSI ਡਿਸਕ ਦਿੰਦਾ ਹੈ | ਆਧੁਨਿਕ Windows ਅਤੇ Linux ਗੈਸਟਾਂ ਲਈ ਵਾਜਬ default। Windows VirtIO ਡਰਾਈਵਰ ਇੰਸਟਾਲ ਕਰੋ। |
| **Bus: VirtIO ਬਲਾਕ** | VirtIO ਬਲਾਕ ਡਿਵਾਈਸ ਵਰਤਦਾ ਹੈ | Linux ਦਾ discard ਸੰਕੇਤ ਲਈ kernel 5.0 ਜਾਂ ਨਵਾਂ ਚਾਹੀਦਾ ਹੈ। SSD ਦੀ ਨਕਲ ਨਹੀਂ। |
| **I/O thread `iothread=1`** | Drive I/O ਵੱਖਰੇ thread ਨੂੰ ਦਿੰਦਾ ਹੈ | VirtIO ਬਲਾਕ ਜਾਂ VirtIO SCSI ਸਿੰਗਲ ਕੰਟਰੋਲਰ ਉੱਤੇ SCSI ਨਾਲ ਵਰਤੋ। ਇਹ ਕਾਰਗੁਜ਼ਾਰੀ ਸੈਟਿੰਗ ਹੈ, ਥਾਂ ਵਾਪਸੀ switch ਨਹੀਂ। |
| **ਕੈਸ਼ ਅਤੇ AIO** | I/O buffering ਅਤੇ asynchronous I/O ਬਦਲਦੇ ਹਨ | Workload ਅਤੇ backend ਮੁਤਾਬਕ ਠੀਕ ਕਰੋ। ਕੋਈ ਵੀ ਡਿਸਕ ਨਹੀਂ ਘਟਾਉਂਦਾ। |
| **ਬੈਕਅੱਪ `backup=0`** | ਡਿਸਕ ਨੂੰ VM ਬੈਕਅੱਪ ਤੋਂ ਬਾਹਰ ਰੱਖਦਾ ਹੈ | ਬੈਕਅੱਪ ਦਾ ਘੇਰਾ ਘਟਾਉਂਦਾ ਅਤੇ ਡਿਸਕ ਡਾਟਾ ਨੂੰ VM recovery ਤੋਂ ਹਟਾਉਂਦਾ ਹੈ। ਵੱਖਰਾ ਬੈਕਅੱਪ ਦਰਜ ਕਰੋ। |
| **Replicate `replicate=0`** | ਡਿਸਕ ਨੂੰ ਸਟੋਰੇਜ replication ਤੋਂ ਬਾਹਰ ਰੱਖਦਾ ਹੈ | Replicated ਡਾਟਾ ਘਟਾਉਂਦਾ ਅਤੇ ਡਿਸਕ ਨੂੰ replica ਤੋਂ ਹਟਾਉਂਦਾ ਹੈ। |

**Drive ਦੀਆਂ ਹੋਰ ਚੋਣਾਂ ਵਿਹਾਰ ਦੱਸਦੀਆਂ ਹਨ, ਥਾਂ ਵਾਪਸੀ ਨਹੀਂ।** `format` ਕਈ ਇਮੇਜ ਫਾਰਮੈਟਾਂ ਵਾਲੇ backend ਉੱਤੇ ਡਿਸਕ ਅਲਾਟ ਕਰਦੇ ਸਮੇਂ ਲਾਗੂ ਹੁੰਦਾ ਹੈ। `size` ਵਰਚੁਅਲ ਸਮਰੱਥਾ ਹੈ, ਅਲਾਟ bytes ਨਹੀਂ। `ro=1` ਡਿਸਕ ਨੂੰ ਸਿਰਫ਼ ਪੜ੍ਹਨਯੋਗ ਕਰਦਾ ਹੈ। `snapshot=1` QEMU ਦਾ ਆਰਜ਼ੀ ਸਨੈਪਸ਼ਾਟ ਮੋਡ ਚਾਲੂ ਕਰਦਾ ਹੈ, ਜੋ VM ਬੰਦ ਹੋਣ ਤੇ ਡਿਸਕ ਬਦਲਾਅ ਛੱਡ ਦਿੰਦਾ ਹੈ। ਇਹ Proxmox VM ਸਨੈਪਸ਼ਾਟ ਵਿੱਚ ਡਿਸਕ ਸ਼ਾਮਲ ਕਰਨ ਵਾਲੀ ਚੋਣ ਨਹੀਂ। ਸਥਾਈ ਡਾਟੇ ਲਈ ਇਸ ਤੋਂ ਬਚੋ। `backup=0` ਜਾਂ `replicate=0` ਵਰਤਣ ਤੋਂ ਪਹਿਲਾਂ ਮੁੜ-ਬਹਾਲੀ ਕਵਰੇਜ ਜਾਂਚੋ। [Proxmox VM ਡਿਸਕ ਚੋਣਾਂ](https://github.com/proxmox/pve-docs/blob/master/generated/qm.conf.5-opts.adoc)

**ਮੌਜੂਦਾ drive ਉੱਤੇ ਛੋਟੀ `qm set --scsi0` ਲਾਈਨ ਨਾ ਚਿਪਕਾਓ।** **`qm config VMID`** ਵੇਖੋ ਅਤੇ ਸੋਧਦੇ ਸਮੇਂ ਪੂਰਾ ਵਾਲਿਊਮ ID ਅਤੇ ਮੌਜੂਦਾ ਚੋਣਾਂ ਰੱਖੋ। ਛੋਟੀ ਡਰਾਈਵ ਵੰਡ ਦੂਜੀਆਂ ਡਿਸਕ ਸੈਟਿੰਗਾਂ ਹਟਾ ਸਕਦੀ ਹੈ। ਹਰ ਬਦਲਾਅ ਪਿੱਛੋਂ ਇੰਟਰਫੇਸ ਵਿੱਚ ਸੇਵ ਕੀਤੀਆਂ ਚੋਣਾਂ ਜਾਂਚੋ।

```bash
qm config 100
pvesm status
```

`100` ਉਦਾਹਰਨ VM ID ਹੈ। ਮੌਜੂਦਾ VM ਉੱਤੇ **ਨਵੀਂ** 64 GiB SCSI ਡਿਸਕ ਲਈ, ਜਿਸਦਾ controller **VirtIO SCSI ਸਿੰਗਲ** ਹੈ ਅਤੇ ਗੈਸਟ ਕੋਲ ਲੋੜੀਂਦਾ ਡਰਾਈਵਰ ਹੈ, ਇਹ ਕਮਾਂਡ ਅਲਾਟਮੈਂਟ syntax ਦਿਖਾਉਂਦੀ ਹੈ। VM ID ਅਤੇ ਸਟੋਰੇਜ ID ਆਪਣੇ ਮੁੱਲਾਂ ਨਾਲ ਬਦਲੋ।

```bash
qm set 100 --scsi0 local-lvm:64,discard=on,ssd=1,iothread=1
```

**ਉਦਾਹਰਨ ਵਰਤਣ ਤੋਂ ਪਹਿਲਾਂ ਜਾਂਚੋ ਕਿ `scsi0` ਪਹਿਲਾਂ ਹੀ ਮੌਜੂਦ ਤਾਂ ਨਹੀਂ।** ਇਹ ਕਮਾਂਡ ਉਸ slot ਨੂੰ ਬਦਲਦੀ ਹੈ। ਮੌਜੂਦਾ ਡਿਸਕ ਲਈ ਜੇ ਸਹੀ ਵਿਕਲਪ ਲੜੀ ਬਚਾਉਣਾ ਸੌਖਾ ਹੋਵੇ ਤਾਂ ਇੰਟਰਫੇਸ ਵਰਤੋ। [Proxmox `qm` ਕਮਾਂਡ ਹਵਾਲਾ](https://github.com/proxmox/pve-docs/blob/master/generated/qm.1-synopsis.adoc) ਵੇਖੋ।

## ਗੈਸਟ ਸਿਸਟਮ ਦੀਆਂ ਫ਼ਾਈਲਾਂ ਸਾਫ਼ ਕਰੋ

**ਪਹਿਲਾਂ ਗੈਸਟ ਫ਼ਾਈਲਾਂ ਖਾਲੀ ਕਰੋ।** Windows ਸਟੋਰੇਜ ਸੈਟਿੰਗਾਂ, ਅਸਥਾਈ ਫ਼ਾਈਲਾਂ, ਪੁਰਾਣੇ installers, ਐਪਲੀਕੇਸ਼ਨ ਕੈਸ਼ ਅਤੇ ਰੱਦੀਦਾਨ ਜਾਂਚੋ। Database ਅਤੇ container runtime ਨੂੰ ਉਹਨਾਂ ਦੇ ਆਪਣੇ ਇੰਟਰਫੇਸ ਰਾਹੀਂ ਸਾਫ਼ ਕਰੋ। ਸਿਰਫ਼ ਅਲਾਟਮੈਂਟ ਘਟਾਉਣ ਲਈ ਸਰਗਰਮ ਐਪਲੀਕੇਸ਼ਨ ਦਾ ਡਾਟਾ ਮਿਟਾਉਣ ਨਾਲ ਡਾਟਾ ਗੁਆਚ ਸਕਦਾ ਹੈ।

**ਪੁਸ਼ਟੀ ਕਰੋ ਕਿ ਵਾਲਿਊਮ discard-ਸਹਾਇਕ ਵਰਚੁਅਲ ਡਿਸਕ ਵਰਤਦਾ ਹੈ**, ਫਿਰ Windows VM ਵਿੱਚ ਉੱਚੇ ਅਧਿਕਾਰਾਂ ਵਾਲਾ PowerShell ਸੈਸ਼ਨ ਖੋਲ੍ਹੋ:

```powershell
fsutil behavior query DisableDeleteNotify
Optimize-Volume -DriveLetter C -ReTrim -Verbose
```

`DisableDeleteNotify = 0` ਦੱਸਦਾ ਹੈ ਕਿ Windows ਨੇ ਰਿਪੋਰਟ ਕੀਤੇ ਫ਼ਾਈਲ ਸਿਸਟਮ ਲਈ ਮਿਟਾਉਣ ਦੀਆਂ ਸੂਚਨਾਵਾਂ ਚਾਲੂ ਕੀਤੀਆਂ ਹਨ। **ReTrim** ਮੌਜੂਦਾ ਖਾਲੀ ਵਾਲਿਊਮ ਖੇਤਰਾਂ ਲਈ trim ਬੇਨਤੀਆਂ ਮੁੜ ਭੇਜਦਾ ਹੈ। ਕਮਾਂਡ ਸਫਲ ਹੋਣਾ ਇਹ ਪੁਸ਼ਟੀ ਕਰਦਾ ਹੈ ਕਿ ਗੈਸਟ ਨੇ ਕਾਰਵਾਈ ਭੇਜੀ, ਨਾ ਕਿ ਹੋਸਟ ਨੂੰ ਕਿੰਨੇ bytes ਵਾਪਸ ਮਿਲੇ। ਕੰਮ ਮੁੱਕਣ ਪਿੱਛੋਂ ਹੋਸਟ ਜਾਂਚੋ। [Microsoft `Optimize-Volume` ਹਵਾਲਾ](https://learn.microsoft.com/en-us/powershell/module/storage/optimize-volume?view=windowsserver2025-ps) ਅਤੇ [Proxmox VM ਡਿਸਕ ਦਸਤਾਵੇਜ਼](https://github.com/proxmox/pve-docs/blob/master/qm.adoc)

**QEMU ਗੈਸਟ ਏਜੰਟ ਨੂੰ TRIM ਨਾ ਸਮਝੋ।** Agent ਗੈਸਟ ਕੰਟਰੋਲ ਅਤੇ ਬੈਕਅੱਪ consistency ਗੁਣ ਦਿੰਦਾ ਹੈ। ਫ਼ਾਈਲ ਸਿਸਟਮ ਦੀਆਂ ਮਿਟਾਉਣ ਦੀਆਂ ਸੂਚਨਾਵਾਂ ਵਰਚੁਅਲ ਡਿਸਕ ਰਾਹੀਂ ਜਾਂਦੀਆਂ ਹਨ। ਸਿਰਫ਼ agent ਇੰਸਟਾਲ ਕਰਨ ਨਾਲ ਬਲਾਕ ਵਾਪਸ ਨਹੀਂ ਮਿਲਦੇ। [Proxmox VM ਗੈਸਟ ਏਜੰਟ ਦਸਤਾਵੇਜ਼](https://github.com/proxmox/pve-docs/blob/master/qm.adoc)

## ਫ਼ਾਈਲ ਸਿਸਟਮ ਦੇ ਖਾਲੀ ਬਲਾਕ ਦਰਜ ਕਰੋ

**Trim ਤੋਂ ਪਹਿਲਾਂ ਬਲਾਕ ਰਾਹ ਅਤੇ ਫ਼ਾਈਲ ਸਿਸਟਮ ਜਾਂਚੋ।** ਆਧੁਨਿਕ distribution ਅਕਸਰ `fstrim.timer` ਨੂੰ ਨਿਯਮਿਤ ਚਲਾਉਂਦੀ ਹੈ। ਇਸਦਾ status ਵੇਖੋ, ਫਿਰ ਬੇਲੋੜਾ ਗੈਸਟ ਡਾਟਾ ਮਿਟਾਉਣ ਤੋਂ ਬਾਅਦ mounted ਫ਼ਾਈਲ ਸਿਸਟਮਾਂ ਉੱਤੇ trim ਚਲਾਓ।

```bash
lsblk -D
systemctl status fstrim.timer
sudo fstrim -av
```

**`lsblk -D`** ਦਿਸਦੇ ਬਲਾਕ devices ਲਈ discard ਬਾਰੀਕੀ ਅਤੇ limits ਦੱਸਦਾ ਹੈ। **`fstrim -av`** ਸਹਾਇਕ mounted ਫ਼ਾਈਲ ਸਿਸਟਮਾਂ ਨੂੰ trim ਕਰਦਾ ਅਤੇ ਭੇਜੇ ranges ਦੱਸਦਾ ਹੈ। ਭੇਜੇ bytes ਪੂਲ ਨੂੰ ਵਾਪਸ ਆਏ bytes ਦੇ ਬਰਾਬਰ ਨਹੀਂ। Encrypted, LVM, RAID ਅਤੇ ਹੋਰ ਪਰਤਦਾਰ ਡਿਵਾਈਸ ਦੀ ਹਰ ਪਰਤ ਨੂੰ discard ਸਹਾਇਤਾ ਚਾਹੀਦੀ ਹੈ। [Red Hat ਨਾ ਵਰਤੇ ਬਲਾਕਾਂ ਬਾਰੇ ਰਹਿਨੁਮਾਈ](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/8/html/managing_file_systems/discarding-unused-blocks_managing-file-systems)

ਤੈਅਸ਼ੁਦਾ trim ਜਾਂ ਸੋਚੀ-ਸਮਝੀ ਚਾਲੂ discard ਨੀਤੀ ਵਰਤੋ। **ਸਟੋਰੇਜ ਰਸਤਾ ਜਾਂਚਣ ਦੀ ਥਾਂ ਹਰ ਫ਼ਾਈਲ ਸਿਸਟਮ ਉੱਤੇ ਲਗਾਤਾਰ `discard` ਚਾਲੂ ਨਾ ਕਰੋ।** ਗੈਸਟ ਵਿੱਚ trim ਪਿੱਛੋਂ PVE ਵਾਲਿਊਮ ਅਤੇ ਪੂਲ ਵੇਖੋ। ਜੇ ਮਿਟਾਏ records ਹਾਲੇ ਫ਼ਾਈਲਾਂ ਵਿੱਚ ਥਾਂ ਲੈਂਦੇ ਹਨ, ਤਾਂ database ਜਾਂ service ਦੀ ਆਪਣੀ compact ਕਰਨ ਦੀ ਨੀਤੀ ਜਾਂਚੋ।

## ਕੰਟੇਨਰ ਸਟੋਰੇਜ ਦੇ ਨਿਯਮ ਵੱਖਰੇ ਜਾਂਚੋ

**LXC ਦੇ root ਫ਼ਾਈਲ ਸਿਸਟਮ ਲਈ VM ਵਾਲੀ emulated ਡਿਸਕ ਬੱਸ ਨਹੀਂ ਹੁੰਦੀ।** `pct config CTID` ਨਾਲ ਸ਼ੁਰੂ ਕਰੋ ਅਤੇ ਹਰ `rootfs` ਤੇ `mpN` entry ਪਛਾਣੋ। Proxmox ਸਟੋਰੇਜ-backed ਮਾਊਂਟ, bind ਮਾਊਂਟ ਅਤੇ device ਮਾਊਂਟ ਵੱਖ ਕਰਦਾ ਹੈ। ਕੰਟੇਨਰ ਵਿੱਚ ਦਿਸਦਾ ਰਾਹ ਇਹ ਨਹੀਂ ਦੱਸਦਾ ਕਿ ਬਲਾਕਾਂ ਦਾ ਮਾਲਕ ਕਿਹੜਾ ਹੋਸਟ ਵਾਲਿਊਮ ਹੈ। [Proxmox ਕੰਟੇਨਰ ਮਾਊਂਟ ਪੁਆਇੰਟ](https://github.com/proxmox/pve-docs/blob/master/pct.adoc)

```bash
pct config 101
pct exec 101 -- df -h
pvesm status
```

**ਪ੍ਰਬੰਧਿਤ rootfs ਜਾਂ ਮਾਊਂਟ ਬਿੰਦੂ** ਲਈ ਕੰਟੇਨਰ ਜਾਂ ਉਸਦੀ application ਵਿੱਚੋਂ ਫ਼ਾਈਲਾਂ ਮਿਟਾਓ, ਫਿਰ ਹੋਸਟ ਉੱਤੇ ਬੈਕਿੰਗ ਵਾਲਿਊਮ ਅਤੇ ਸਨੈਪਸ਼ਾਟ ਜਾਂਚੋ। **CT ਉੱਤੇ VM ਦੇ `qm` discard ਕਮਾਂਡ ਨਾ ਚਲਾਓ।** ZFS ਉਪ-ਵਾਲਿਊਮ ਉੱਤੇ ਸਨੈਪਸ਼ਾਟ ਮਿਟਾਏ ਬਲਾਕ ਰੋਕਦੇ ਹਨ। directory ਅਤੇ ਪਤਲੀ ਵੰਡ ਵਾਲਾ LVM ਉੱਤੇ ਸੰਰਚਿਤ CT ਆਕਾਰ ਦੀ ਥਾਂ ਅਸਲ ਬੈਕਐਂਡ ਅਲਾਟਮੈਂਟ ਵੇਖੋ।

ਜੇ ਬੈਕਿੰਗ ਸਟੋਰੇਜ discard ਸਹਾਇਕ ਕਰਦੀ ਹੈ, ਤਾਂ CT ਦੀ ਸਫ਼ਾਈ ਪਿੱਛੋਂ **Proxmox ਹੋਸਟ ਉੱਤੇ `pct fstrim` ਚਲਾਓ।** Proxmox CT rootfs ਅਤੇ ਯੋਗ ਪ੍ਰਬੰਧਿਤ ਮਾਊਂਟ ਬਿੰਦੂ ਨੂੰ trim ਕਰਦਾ ਹੈ। ਇਹ bind ਮਾਊਂਟ ਅਤੇ ਸਿਰਫ਼ ਪੜ੍ਹਨ ਵਾਲਾ ਮਾਊਂਟ points ਛੱਡ ਦਿੰਦਾ ਹੈ। ਸਿਰਫ਼ rootfs trim ਕਰਨ ਲਈ `--ignore-mountpoints` ਵਰਤੋ। ਪਹਿਲਾਂ ਤੇ ਬਾਅਦ ਦੀ ਸਟੋਰੇਜ ਵਰਤੋਂ ਤੁਲਨਾ ਕਰੋ। [Proxmox `pct fstrim` ਹਵਾਲਾ](https://github.com/proxmox/pve-docs/blob/master/generated/pct.1-synopsis.adoc)

```bash
pct fstrim 101
pct fstrim 101 --ignore-mountpoints 1
```

ਇਹ ਕਮਾਂਡ ਉਦਾਹਰਨ CT ID `101` ਲਈ **ਵੱਖਰੇ ਦਾਇਰੇ** ਦਿਖਾਉਂਦੀਆਂ ਹਨ। ਆਪਣੇ ਸਟੋਰੇਜ ਲੇਆਉਟ ਵਾਲਾ ਇੱਕ ਦਾਇਰਾ ਚਲਾਓ। ਸਫਲ trim ਨਾਲ ਬਰਾਬਰ bytes ਵਾਪਸ ਮਿਲਣ ਦੀ ਗਾਰੰਟੀ ਨਹੀਂ, ਜੇ ਸਨੈਪਸ਼ਾਟ ਪੁਰਾਣੇ ਬਲਾਕ ਰੋਕਦੇ ਹੋਣ।

**Proxmox bind ਮਾਊਂਟ ਅਤੇ device ਮਾਊਂਟ ਦਾ ਪ੍ਰਬੰਧ ਨਹੀਂ ਕਰਦਾ।** ਉਹਨਾਂ ਦਾ ਸਰੋਤ ਡਾਟਾ ਹੋਸਟ ਜਾਂ ਬਾਹਰੀ ਯੰਤਰ ਉੱਤੇ ਰਹਿੰਦਾ ਹੈ। ਕੰਟੇਨਰ ਦੇ `vzdump` ਬੈਕਅੱਪ ਉਹਨਾਂ ਦੀ ਸਮੱਗਰੀ ਛੱਡ ਦਿੰਦੇ ਹਨ। ਵਾਧੂ ਸਟੋਰੇਜ-backed ਮਾਊਂਟ ਬਿੰਦੂ ਵੀ ਮੂਲ ਰੂਪ ਵਿੱਚ ਬਾਹਰ ਰਹਿੰਦੇ ਹਨ, ਜਦ ਤੱਕ `backup` ਵਿਕਲਪ ਉਹਨਾਂ ਨੂੰ ਸ਼ਾਮਲ ਨਾ ਕਰੇ। ਸਫ਼ਾਈ ਤੋਂ ਪਹਿਲਾਂ ਅਸਲ ਬੈਕਅੱਪ ਨੀਤੀ ਜਾਂਚੋ। [Proxmox ਬੈਕਅੱਪ ਦਸਤਾਵੇਜ਼](https://github.com/proxmox/pve-docs/blob/master/vzdump.adoc)

Nested Docker ਲਈ Docker ਸਫ਼ਾਈ ਕਮਾਂਡ ਚਲਾਉਣ ਤੋਂ ਪਹਿਲਾਂ ਅਸਲ ਸਟੋਰੇਜ ਮਾਲਕ ਵਿੱਚ ਚਿੱਤਰ layers, ਵਾਲਿਊਮ ਅਤੇ logs ਜਾਂਚੋ। [LXC ਵਿੱਚ Docker ਭਰੋਸੇਯੋਗਤਾ ਗਾਈਡ](/articles/docker-in-lxc-proxmox-reliability/) ਮਾਊਂਟ ਅਤੇ ਬੈਕਅੱਪ ਦੀਆਂ ਹੱਦਾਂ ਦੱਸਦੀ ਹੈ। Container ਚਿੱਤਰ ਮਿਟਾਉਣ ਨਾਲ ਸਥਾਈ ਵਾਲਿਊਮ ਮੂਲ ਰੂਪ ਵਿੱਚ ਨਹੀਂ ਮਿਟਦਾ।

## ਹੋਸਟ ਨੂੰ ਸਹੀ ਤਰ੍ਹਾਂ ਮਾਪੋ

**ਸਫ਼ਾਈ ਤੋਂ ਪਹਿਲਾਂ ਅਤੇ ਬਾਅਦ ਇੱਕੋ ਜਿਹੇ ਮਾਪ ਦਰਜ ਕਰੋ।** ਪੂਲ ਦੀ ਖਾਲੀ ਥਾਂ ਅੰਤਿਮ ਸਮਰੱਥਾ ਸੰਕੇਤ ਹੈ। ਵਧੇਰੇ ਵਰਤੋਂ ਵਾਲੇ ਗੈਸਟ ਨੂੰ ਲੱਭਣ ਲਈ ਵਾਲਿਊਮ ਪੱਧਰ ਦੇ ਅੰਕੜੇ ਵਰਤੋ।

```bash
pvesm status
pvesm list local-lvm
qm config 100
pct config 101
```

**`pvesm list`** ਪ੍ਰਬੰਧਿਤ ਵਾਲਿਊਮ ਅਤੇ ਸੰਰਚਿਤ ਆਕਾਰ ਦੀ ਸੂਚੀ ਦਿੰਦਾ ਹੈ। ਇਹ ਪਤਲੀ ਸਟੋਰੇਜ ਵਿੱਚ ਅਲਾਟ bytes ਨਹੀਂ ਮਾਪਦਾ। **Directory ਸਟੋਰੇਜ** ਲਈ ਸਹੀ mounted ਰਾਹ ਅਤੇ ਜਾਣੀ ਇਮੇਜ ਫ਼ਾਈਲ ਵੇਖੋ। **Datacenter > ਸਟੋਰੇਜ** ਅਤੇ VM config ਵਾਲੇ paths ਪਾਓ।

```bash
df -hT /var/lib/vz
du -h /var/lib/vz/images/100/vm-100-disk-0.qcow2
ls -lh /var/lib/vz/images/100/vm-100-disk-0.qcow2
```

**ਬੰਦ VM** ਲਈ ਫ਼ਾਈਲ ਬਦਲੇ ਬਿਨਾਂ ਇਮੇਜ ਦੀ ਵਰਚੁਅਲ ਸਮਰੱਥਾ ਅਤੇ ਹੋਸਟ ਅਲਾਟਮੈਂਟ ਦੀ ਤੁਲਨਾ ਕਰੋ:

```bash
qemu-img info /var/lib/vz/images/100/vm-100-disk-0.qcow2
```

**ਪਤਲੀ ਵੰਡ ਵਾਲਾ LVM** ਲਈ ਪੂਲ ਦੇ ਡਾਟਾ ਅਤੇ ਮੈਟਾਡੇਟਾ ਵੇਖੋ:

```bash
lvs -a -o lv_name,vg_name,lv_size,data_percent,metadata_percent,segtype
```

**ZFS** ਲਈ ਸਰਗਰਮ dataset ਡਾਟਾ ਅਤੇ ਸਨੈਪਸ਼ਾਟ ਵੱਲੋਂ ਰੋਕੇ ਡਾਟਾ ਵੱਖ ਵੇਖੋ:

```bash
zpool list
zfs list -o name,used,available,referenced,usedbysnapshots -r POOL_OR_DATASET
zfs list -t snapshot -o name,used,referenced,written -r DATASET
```

**`usedbysnapshots`** dataset ਦੇ ਸਾਰੇ ਸਨੈਪਸ਼ਾਟ ਵੱਲੋਂ ਰੋਕੇ ਬਲਾਕ ਦੱਸਦਾ ਹੈ। ਸਨੈਪਸ਼ਾਟ `used` ਅੰਕ ਜੋੜੇ ਨਹੀਂ ਜਾ ਸਕਦੇ, ਕਿਉਂਕਿ ਸਨੈਪਸ਼ਾਟ ਬਲਾਕ ਸਾਂਝੇ ਕਰਦੇ ਹਨ। ਮਿਟਾਈ ਫ਼ਾਈਲ ਨਾਲ ਪੂਲ ਵਰਤੋਂ ਉਹਨਾਂ ਸਾਰੇ ਸਨੈਪਸ਼ਾਟ ਦੇ expire ਜਾਂ ਨੀਤੀ ਮੁਤਾਬਕ ਮਿਟਣ ਤੱਕ ਬਦਲਣੀ ਲਾਜ਼ਮੀ ਨਹੀਂ, ਜੋ ਉਸਦੇ ਬਲਾਕਾਂ ਦਾ ਹਵਾਲਾ ਦਿੰਦੇ ਹਨ। [OpenZFS ਸਨੈਪਸ਼ਾਟ ਅਤੇ clones](https://openzfs.github.io/openzfs-docs/Basic%20Concepts/Datasets/Snapshots%20and%20Clones.html)

**Ceph RBD** ਲਈ Ceph ਕਮਾਂਡ ਚਲਾਉਣ ਤੋਂ ਪਹਿਲਾਂ Proxmox ਵਾਲਿਊਮ ID ਨੂੰ map ਕਰੋ। **`qm config VMID`** ਵਿੱਚ `STORAGE_ID:IMAGE` ਦਿਸਦਾ ਹੈ। **Datacenter > ਸਟੋਰੇਜ** ਵਿੱਚ RBD ਐਂਟਰੀ ਖੋਲ੍ਹ ਕੇ **ਪੂਲ** ਅਤੇ ਚੋਣਵੇਂ **namespace** ਲੱਭੋ। ਸਟੋਰੇਜ ID ਦਾ ਪੂਲ name ਨਾਲ ਮਿਲਣਾ ਲਾਜ਼ਮੀ ਨਹੀਂ। ਪੂਲ ਅਤੇ ਚਿੱਤਰ ਮੁੱਲਾਂ ਨਾਲ `POOL/IMAGE` ਬਣਾਓ। ਇਹ ਕਮਾਂਡ ਨਿਰਧਾਰਤ Ceph ਕਲੱਸਟਰ ਲਈ configured client ਅਤੇ ਠੀਕ credentials ਨਾਲ ਚਲਾਓ। [Proxmox RBD ਸਟੋਰੇਜ ਦਸਤਾਵੇਜ਼](https://github.com/proxmox/pve-docs/blob/master/pve-storage-rbd.adoc)

```bash
ceph df
rbd du POOL/IMAGE
rbd snap ls POOL/IMAGE
```

**`rbd du`** ਚਿੱਤਰ ਦੀ provisioned ਅਤੇ ਅਸਲ ਵਰਤੋਂ, ਜੁੜੇ ਸਨੈਪਸ਼ਾਟ ਸਮੇਤ, ਦੱਸਦਾ ਹੈ। `fast-diff` ਚਿੱਤਰ ਵਿਸ਼ੇਸ਼ਤਾ ਨਾ ਹੋਵੇ ਤਾਂ ਇਹ ਸੰਭਾਵੀ objects ਲਈ OSDs ਤੋਂ ਪੁੱਛਦਾ ਹੈ ਅਤੇ ਵੱਧ ਕੰਮ ਕਰਦਾ ਹੈ। **`ceph df`** ਪੂਲ ਅਤੇ cluster ਸਮਰੱਥਾ ਦਿਖਾਉਂਦਾ ਹੈ। Replication, ਇਰੇਜ਼ਰ ਕੋਡਿੰਗ ਅਤੇ ਸਨੈਪਸ਼ਾਟ ਕਲੱਸਟਰ ਦੀ raw ਵਰਤੋਂ ਵਰਤੋਂ ਬਦਲਦੇ ਹਨ, ਇਸ ਲਈ ਚਿੱਤਰ ਅਤੇ ਪੂਲ bytes ਵੱਖਰੇ ਹੁੰਦੇ ਹਨ। [Ceph RBD ਕਮਾਂਡ ਹਵਾਲਾ](https://docs.ceph.com/en/squid/man/8/rbd/) ਅਤੇ [Ceph ਪੂਲ ਵਰਤੋਂ ਰਹਿਨੁਮਾਈ](https://docs.ceph.com/en/squid/rados/operations/monitoring/)

ਜੇ RBD ਸਟੋਰੇਜ namespace ਵਰਤਦੀ ਹੈ, ਤਾਂ ਹਰ `rbd` ਕਮਾਂਡ ਵਿੱਚ **`--namespace NAMESPACE`** ਜੋੜੋ। Proxmox ਸਟੋਰੇਜ entry ਵਿੱਚ configured namespace ਵਰਤੋ, Proxmox ਸਟੋਰੇਜ ID ਨਹੀਂ।

## ਸਨੈਪਸ਼ਾਟਾਂ ਅਤੇ ਬੈਕਅੱਪਾਂ ਦਾ ਹਿਸਾਬ ਰੱਖੋ

**ਸਨੈਪਸ਼ਾਟ ਬਲਾਕਾਂ ਦੇ ਪੁਰਾਣੇ ਰੂਪ ਸੰਭਾਲਦੇ ਹਨ।** Trim ਪਿੱਛੋਂ ਵਰਤੋਂ ਨਾ ਘਟੇ ਤਾਂ VM ਜਾਂ CT ਦਾ **ਸਨੈਪਸ਼ਾਟ** ਟੈਬ ਅਤੇ ਬੈਕਐਂਡ ਦੀ ਸਨੈਪਸ਼ਾਟ ਸੂਚੀ ਵੇਖੋ। ਮਿਟਾਉਣ ਤੋਂ ਪਹਿਲਾਂ ਮਾਲਕੀ ਅਤੇ ਨਿਰਭਰਤਾਵਾਂ ਜਾਂਚੋ। ਬੈਕਅੱਪ ਵੱਖਰੀ ਕਾਪੀ ਹੈ ਅਤੇ ਬੈਕਅੱਪ ਸਟੋਰੇਜ ਦੀ retention ਅਨੁਸਾਰ ਚੱਲਦਾ ਹੈ, ਗੈਸਟ ਦੇ ਮੌਜੂਦਾ `df` ਅਨੁਸਾਰ ਨਹੀਂ।

**PBS ਵਿੱਚ ਡੁਪਲੀਕੇਟ ਡਾਟਾ ਹਟਾਉਣਾ ਹਿਸਾਬ ਬਦਲਦੀ ਹੈ।** Datastore ਵਿੱਚ ਬੈਕਅੱਪਾਂ ਵੱਲੋਂ ਸਾਂਝੇ chunks ਹੁੰਦੇ ਹਨ। Pruning ਬੈਕਅੱਪ ਸਨੈਪਸ਼ਾਟ ਮੈਟਾਡੇਟਾ ਹਟਾਉਂਦਾ ਹੈ। ਫਿਰ ਉਡੀਕ ਸਮਾਂ ਪਿੱਛੋਂ ਬੇਕਾਰ ਡਾਟਾ ਸਫ਼ਾਈ ਬਿਨਾਂ ਹਵਾਲੇ ਵਾਲੇ chunks ਹਟਾਉਂਦੀ ਹੈ। ਬੈਕਅੱਪ ਥਾਂ ਵਾਪਸ ਮਿਲਣ ਦਾ ਦਾਅਵਾ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ ਦੋਵੇਂ ਕੰਮ ਜਾਂਚੋ। [PBS ਰੱਖ-ਰਖਾਅ ਦਸਤਾਵੇਜ਼](https://pbs.proxmox.com/docs/maintenance.html)

> **ਚੇਤਾਵਨੀ:** Proxmox-ਪ੍ਰਬੰਧਿਤ ਵਾਲਿਊਮ ਫ਼ਾਈਲ, zvol ਜਾਂ ਸਨੈਪਸ਼ਾਟ ਨੂੰ ਸਿਰਫ਼ ਨਾਮ ਵੇਖ ਕੇ ਕਦੇ ਨਾ ਮਿਟਾਓ। ਪਹਿਲਾਂ ਗੈਸਟ ਅਤੇ retention ਨੀਤੀ ਪਛਾਣੋ। ਸਟੋਰੇਜ ਸਫ਼ਾਈ ਵਿੱਚ ਬੈਕਅੱਪ ਅਤੇ ਵਾਪਸੀ ਦਾ ਰਸਤਾ ਬਚਣਾ ਚਾਹੀਦਾ ਹੈ।

## VM ਬੰਦ ਕਰਕੇ ਡਿਸਕ ਚਿੱਤਰ ਮੁੜ ਬਣਾਓ

**ਬੰਦ ਹਾਲਤ ਵਿੱਚ conversion ਸਿਰਫ਼ ਉਦੋਂ ਵਰਤੋ ਜਦੋਂ ਆਮ ਗੈਸਟ trim ਅਤੇ ਬੈਕਐਂਡ ਰਸਤਾ qcow2 ਅਲਾਟਮੈਂਟ ਸਮੱਸਿਆ ਹੱਲ ਨਾ ਕਰਨ।** VM ਬੰਦ ਕਰੋ, ਬੈਕਅੱਪ ਪੱਕਾ ਕਰੋ, ਸਾਰੇ ਸਨੈਪਸ਼ਾਟ ਅਤੇ backing-chain ਸੰਬੰਧ ਪਛਾਣੋ ਅਤੇ ਵੱਖਰੀ ਮੰਜ਼ਿਲ ਚਿੱਤਰ ਲਿਖੋ। QEMU ਦੂਜੇ ਪ੍ਰਕਿਰਿਆ ਵੱਲੋਂ ਵਰਤੀ ਜਾ ਰਹੀ ਇਮੇਜ ਬਦਲਣ ਤੋਂ ਸਾਵਧਾਨ ਕਰਦਾ ਹੈ। [QEMU `qemu-img` ਦਸਤਾਵੇਜ਼](https://www.qemu.org/docs/master/tools/qemu-img.html)

**ਜੇ ਡਿਸਕ ਉੱਤੇ ਸਨੈਪਸ਼ਾਟ ਹੋਣ ਜਾਂ ਪ੍ਰਬੰਧਿਤ ਬਲਾਕ ਸਟੋਰੇਜ ਉੱਤੇ ਹੋਵੇ, ਤਾਂ Proxmox-ਪ੍ਰਬੰਧਿਤ move ਜਾਂ ਬੈਕਅੱਪ ਅਤੇ ਮੁੜ-ਬਹਾਲੀ ਤਰੀਕਾ ਚੁਣੋ।** PVE-owned ਚਿੱਤਰ ਉੱਤੇ ਇਕੱਲਾ `qemu-img convert` VM config, ਵਾਲਿਊਮ ਮਾਲਕੀ ਜਾਂ ਸਨੈਪਸ਼ਾਟ references ਆਪਣੇ ਆਪ ਨਹੀਂ ਬਦਲਦਾ। ਮਿਟਾਈਆਂ ਫ਼ਾਈਲਾਂ ਵਾਪਸ ਲੈਣ ਲਈ `qemu-img resize --shrink` ਨਾ ਵਰਤੋ। ਗੈਸਟ ਨੂੰ ਦਿਸਦੀ ਸਮਰੱਥਾ ਘਟਾਉਣ ਨਾਲ ਡਾਟਾ ਕੱਟਿਆ ਜਾ ਸਕਦਾ ਹੈ ਜੇ partitions ਅਤੇ ਫ਼ਾਈਲ ਸਿਸਟਮ ਪਹਿਲਾਂ ਛੋਟੇ ਨਾ ਕੀਤੇ ਹੋਣ।

## ਥਾਂ ਵਾਪਸ ਨਾ ਮਿਲੇ ਤਾਂ ਨਿਪਟਾਰਾ ਕਰੋ

| ਲੱਛਣ | ਸੰਭਾਵੀ ਜਾਂਚ | ਅਗਲਾ ਕਦਮ |
|---|---|---|
| **ਗੈਸਟ `df` ਘਟੇ, ਹੋਸਟ ਨਾ ਬਦਲੇ** | VM discard ਨਿਸ਼ਾਨ, ਗੈਸਟ trim, ਸਨੈਪਸ਼ਾਟ | ਪੂਰਾ discard ਰਸਤਾ ਅਤੇ ਰੋਕੇ ਸਨੈਪਸ਼ਾਟ ਜਾਂਚੋ। |
| **`fstrim` ਅਸਮਰਥਿਤ ਦੱਸੇ** | ਗੈਸਟ ਡਿਸਕ ਬੱਸ, stacked ਬਲਾਕ devices, ਬੈਕਐਂਡ | `lsblk -D`, ਗੈਸਟ kernel ਅਤੇ ਵਿਚਕਾਰਲੀ ਹਰ ਪਰਤ ਵੇਖੋ। |
| **Windows ReTrim ਮੁੱਕੇ, ਹੋਸਟ ਨਾ ਬਦਲੇ** | ਬੈਕਐਂਡ ਅਲਾਟਮੈਂਟ, ਸਨੈਪਸ਼ਾਟ, ਸਰਵਰ ਹਿਸਾਬ | ਵਾਲਿਊਮ ਅਤੇ ਪੂਲ ਦੀ ਤੁਲਨਾ ਕਰੋ। ਪੱਕਾ ਕਰੋ ਕਿ ਡਿਸਕ ਪਤਲੀ ਸਟੋਰੇਜ ਵਰਤਦੀ ਹੈ। |
| **`ls -lh` ਅਤੇ `du -h` ਵੱਖਰੇ ਹੋਣ** | Sparse ਜਾਂ qcow2 ਫ਼ਾਈਲ | ਅਲਾਟ ਫ਼ਾਈਲ ਸਿਸਟਮ ਬਲਾਕਾਂ ਲਈ `du` ਵਰਤੋ। |
| **LVM ਪਤਲਾ ਪੂਲ ਭਰਿਆ ਰਹੇ** | ਡਾਟਾ, ਮੈਟਾਡੇਟਾ, ਸਨੈਪਸ਼ਾਟ | ਕੁਝ ਹਟਾਉਣ ਤੋਂ ਪਹਿਲਾਂ `lvs` ਅਤੇ PVE ਸਨੈਪਸ਼ਾਟ ਵੇਖੋ। |
| **ZFS ਪੂਲ ਭਰਿਆ ਰਹੇ** | ਸਨੈਪਸ਼ਾਟ-held ਬਲਾਕ ਅਤੇ ਰਿਜ਼ਰਵੇਸ਼ਨ | `usedbysnapshots`, zvol ਸੈਟਿੰਗਾਂ ਅਤੇ ਪੂਲ ਸਮਰੱਥਾ ਜਾਂਚੋ। |
| **CT `df` ਅਤੇ ਪੂਲ ਨਾ ਮਿਲਣ** | Bind ਮਾਊਂਟ, ਮਾਊਂਟ ਬਿੰਦੂ, ਸਨੈਪਸ਼ਾਟ | `rootfs` ਅਤੇ ਹਰ `mpN` ਨੂੰ ਹੋਸਟ ਉੱਤੇ ਉਸਦੇ ਮਾਲਕ ਨਾਲ ਜੋੜੋ। |

**Background ਕੰਮ ਮੁੱਕਣ ਪਿੱਛੋਂ ਮੁੜ ਜਾਂਚੋ।** Trim, ਸਨੈਪਸ਼ਾਟ ਮਿਟਾਉਣ ਜਾਂ backend ਬੇਕਾਰ ਡਾਟਾ ਸਫ਼ਾਈ ਪਿੱਛੋਂ ਸਟੋਰੇਜ ਹਿਸਾਬ ਦੇਰ ਨਾਲ ਬਦਲ ਸਕਦਾ ਹੈ। ਮਾਪੀ ਪੂਲ ਖਾਲੀ ਥਾਂ ਦੀ ਸ਼ੁਰੂਆਤੀ ਮੁੱਲ ਨਾਲ ਤੁਲਨਾ ਕਰੋ। ਸਿਰਫ਼ ਗੈਸਟ ਕਮਾਂਡ ਦੇ ਨਿਕਾਸ ਕੋਡ ਤੋਂ ਸਫਲਤਾ ਨਾ ਮੰਨੋ।

## ਅਗਲੇ ਕਦਮ

**ਹਰ ਗੈਸਟ ਲਈ ਸਟੋਰੇਜ ਰਿਕਾਰਡ ਬਣਾਓ:** ਵਰਚੁਅਲ ਆਕਾਰ, ਅਲਾਟ bytes, ਬੈਕਐਂਡ, ਬੱਸ, discard ਨਿਸ਼ਾਨ, ਸਨੈਪਸ਼ਾਟ ਗਿਣਤੀ, ਬੈਕਅੱਪ ਕਵਰੇਜ ਅਤੇ ਪੂਲ ਦੀ ਖਾਲੀ ਥਾਂ। ਇੱਕ VM ਚੁਣੋ, ਸਹਾਇਕ discard ਰਸਤਾ ਚਾਲੂ ਕਰੋ, ਗੈਸਟ ਵਿੱਚ trim ਚਲਾਓ ਅਤੇ ਦਰਜ ਮੁੱਲਾਂ ਦੀ ਤੁਲਨਾ ਕਰੋ। ਪਹਿਲੀ VM ਦਾ ਨਤੀਜਾ ਬੈਕਐਂਡ ਦੇ ਉਮੀਦਵਾਰ ਵਿਹਾਰ ਨਾਲ ਮਿਲੇ ਤਾਂ ਹੀ ਦੁਹਰਾਓ।

ਵਿਆਪਕ ਰਿਕਵਰੀ ਯੋਜਨਾ ਲਈ [Proxmox ਬੈਕਅੱਪ ਅਤੇ ਮੁੜ-ਬਹਾਲੀ drill](/articles/proxmox-vm-backup-restore-drill/) ਅਤੇ [Proxmox VE 8 ਤੋਂ 9 ਅਪਗ੍ਰੇਡ ਗਾਈਡ](/articles/proxmox-ve-8-to-9-upgrade-guide/) ਵੇਖੋ।

## ਸਰੋਤ

- [Proxmox VE ਸਟੋਰੇਜ ਪ੍ਰਸ਼ਾਸਨ](https://github.com/proxmox/pve-docs/blob/master/pvesm.adoc), ਸਟੋਰੇਜ ਕਿਸਮਾਂ, ਪਤਲੀ ਵੰਡ ਅਤੇ ਸਮਰੱਥਾ ਜੋਖਮ।
- [Proxmox VE LVM ਸਟੋਰੇਜ](https://github.com/proxmox/pve-docs/blob/master/pve-storage-lvm.adoc), VE 9 ਸਨੈਪਸ਼ਾਟ ਵਾਲਿਊਮ chains ਅਤੇ ਅਲਾਟਮੈਂਟ।
- [Proxmox VE RBD ਸਟੋਰੇਜ](https://github.com/proxmox/pve-docs/blob/master/pve-storage-rbd.adoc), ਪੂਲ ਅਤੇ namespace ਕੌਂਫਿਗਰੇਸ਼ਨ।
- [Proxmox VE ਵਰਚੁਅਲ ਮਸ਼ੀਨਾਂ](https://github.com/proxmox/pve-docs/blob/master/qm.adoc), ਡਿਸਕ ਬੱਸਾਂ, ਫਾਰਮੈਟ, discard ਅਤੇ ਗੈਸਟ ਏਜੰਟ।
- [Proxmox VE VM ਡਿਸਕ ਚੋਣਾਂ](https://github.com/proxmox/pve-docs/blob/master/generated/qm.conf.5-opts.adoc), ਬੱਸ ਅਨੁਸਾਰ flags।
- [Proxmox VE ਕੰਟੇਨਰ](https://github.com/proxmox/pve-docs/blob/master/pct.adoc), root ਫ਼ਾਈਲ ਸਿਸਟਮ ਅਤੇ ਮਾਊਂਟ-point ਮਾਲਕੀ।
- [Proxmox VE ਕੰਟੇਨਰ ਕਮਾਂਡ](https://github.com/proxmox/pve-docs/blob/master/generated/pct.1-synopsis.adoc), ਹੋਸਟ ਤੋਂ ਕੰਟੇਨਰ trim।
- [Proxmox VE ਬੈਕਅੱਪ ਅਤੇ ਮੁੜ-ਬਹਾਲੀ](https://github.com/proxmox/pve-docs/blob/master/vzdump.adoc), VM ਅਤੇ CT ਬੈਕਅੱਪ ਕਵਰੇਜ।
- [Microsoft Optimize-ਵਾਲਿਊਮ ਹਵਾਲਾ](https://learn.microsoft.com/en-us/powershell/module/storage/optimize-volume?view=windowsserver2025-ps), Windows ReTrim ਦਾ ਸਿੰਟੈਕਸ।
- [Red Hat ਨਾ ਵਰਤੇ ਬਲਾਕਾਂ ਬਾਰੇ ਰਹਿਨੁਮਾਈ](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/8/html/managing_file_systems/discarding-unused-blocks_managing-file-systems), Linux `fstrim` ਵਿਹਾਰ।
- [OpenZFS ਸਨੈਪਸ਼ਾਟ ਅਤੇ clones](https://openzfs.github.io/openzfs-docs/Basic%20Concepts/Datasets/Snapshots%20and%20Clones.html), ਸਨੈਪਸ਼ਾਟਾਂ ਵੱਲੋਂ ਰੋਕੇ ਬਲਾਕ।
- [Ceph RBD ਕਮਾਂਡ ਹਵਾਲਾ](https://docs.ceph.com/en/squid/man/8/rbd/), ਇਮੇਜ ਵਰਤੋਂ ਅਤੇ ਸਨੈਪਸ਼ਾਟ।
- [NFSv4.2 ਨਿਰਧਾਰਨ](https://www.rfc-editor.org/rfc/rfc7862.html#section-6.2.2), ਸਰਵਰ ਪਾਸੇ ਥਾਂ ਛੱਡਣਾ।
- [PBS ਰੱਖ-ਰਖਾਅ ਦਸਤਾਵੇਜ਼](https://pbs.proxmox.com/docs/maintenance.html), pruning ਅਤੇ ਬੇਕਾਰ ਡਾਟਾ ਸਫ਼ਾਈ।
- [QEMU ਡਿਸਕ ਇਮੇਜ ਟੂਲ](https://www.qemu.org/docs/master/tools/qemu-img.html), ਬੰਦ ਹਾਲਤ ਵਿੱਚ ਇਮੇਜ conversion ਸੁਰੱਖਿਆ।
