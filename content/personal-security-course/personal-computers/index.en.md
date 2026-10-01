---
title: "Module 8: Personal Computer Security"
date: 2026-09-30
lastmod: 2026-09-30
toc: true
draft: false
description: "Updates, encryption, and backups matter more than anything else on a desktop. This module covers those three, then least privilege, endpoint integrity, attack surface reduction, and isolation techniques."
genre: ["Personal Security", "Computer Security", "Endpoint Security", "Privacy", "Operating Systems"]
tags: ["computer security", "endpoint security", "full disk encryption", "bitlocker", "filevault", "luks", "least privilege", "secure boot", "ssh hardening", "rootkit", "keylogger", "usbguard", "virtual machines", "compartmentalization", "mandatory access control", "canary tokens", "personal security course"]
cover: "/img/cover/personal-computer-security-endpoint-illustration.webp"
coverAlt: "An illustration of a laptop with layered shield segments representing disk encryption, system updates, and privilege separation, on a dark background with pink accents."
coverCaption: "Module 8: three controls carry most of the weight"
---

#### [← Return to the Personal Security Course](/personal-security-course-start/)

**On a desktop, three controls carry more weight than everything else combined:** updates, disk encryption, and backups. The remaining controls reduce the consequences when one of those three fails.

This module covers those three first, then least privilege, endpoint integrity, attack surface reduction, and the isolation techniques which matter for readers who run untrusted software.

*Budget about 45 minutes. Encryption and the backup check are the two items to finish today.*

## What You Will Learn

- **Sequence** desktop controls by consequence rather than by popularity
- **Enable** full disk encryption on Windows, macOS, or Linux
- **Apply** least privilege to daily work rather than only to servers
- **Reduce** the listening attack surface by closing services and ports
- **Isolate** risky activity with virtual machines and separate accounts
- **Produce** a computer record listing encryption, backup, and privilege configuration

| Term | Meaning |
|---|---|
| **Full disk encryption** | Encrypting the entire volume so a stolen device yields no readable data |
| **Least privilege** | Operating with the minimum rights needed for the task at hand |
| **Attack surface** | The set of services, ports, and interfaces reachable by an attacker |
| **Keystroke injection** | A device which presents itself as a keyboard and types commands |
| **Mandatory access control** | A policy layer which restricts programs beyond file permissions |
| **Canary token** | A decoy file or credential which alerts you when it is touched |

## The Three Controls Which Matter Most

### 1. Automatic Updates

**Most successful compromises exploit a vulnerability with an available patch.** Update lag is the exploitable window.

- **Enable automatic updates** for the operating system and restart when prompted
- **Update applications separately.** Browsers, document readers, and media players are common targets
- **Include firmware and drivers** where the vendor supports automatic delivery

*A pending restart means a pending vulnerability. Treat the notification as unfinished work rather than an interruption.*

### 2. Full Disk Encryption

**Encryption converts a stolen device from a data breach into a hardware loss.** Without it, anyone holding the machine reads your vault, your sessions, and your files.

| Platform | Feature | Where to Check |
|---|---|---|
| **Windows** | BitLocker or Device Encryption | Settings, Privacy and Security, Device encryption |
| **macOS** | FileVault | System Settings, Privacy and Security, FileVault |
| **Linux** | LUKS | Confirm root and home volumes at install time |

**Verify your recovery key is stored somewhere other than the encrypted disk.** A recovery key only on the encrypted volume is not a recovery key.

*Turning the device fully off rather than leaving it in standby matters once encryption is enabled. A suspended machine often holds keys in memory.*

### 3. Backups

**A tested backup is the only control which survives ransomware, theft, and hardware failure alike.**

- **Keep one local copy** for fast restores
- **Keep one encrypted offsite copy** for fire and theft
- **Keep one offline or write-only copy** for ransomware which reaches your synced storage

**Test a restore.** A backup never restored is an assumption.

## Least Privilege on a Desktop

**Most people work as an administrator all day**, which means every process they launch inherits those rights. Least privilege is not a server-only concept.

| Practice | Why It Matters |
|---|---|
| **Use a standard account for daily work** | Malware inherits the account's rights, not the machine's |
| **Elevate only for administrative tasks** | Limits what runs with full rights |
| **Do not link the machine to a cloud account** | A local account avoids syncing settings and browsing data to a vendor |
| **Review installed applications** | Fewer applications means fewer update obligations and fewer targets |
| **Lock the screen on idle** | An unlocked machine is a complete compromise |

**Separate accounts are the simplest compartmentalization available.** One account for daily use, one for administrative work, and one for anything untrusted. On Linux and macOS the separation is native. On Windows it requires creating additional local accounts rather than using the built-in administrator.

*The measurement for this module is not how many controls you enabled. It is how much an attacker gains from compromising one account.*

## Endpoint Integrity

**These controls answer a different question: is the machine currently trustworthy?**

| Control | What It Addresses |
|---|---|
| **Built-in platform protections** | Defender, Gatekeeper, or the Linux equivalents, which are adequate for most users |
| **Avoid commercial free antivirus** | Many monetize telemetry, and some add attack surface rather than reducing it |
| **Periodic rootkit checks** | Tools such as `chkrootkit` or `rkhunter` on Linux, and vendor tooling elsewhere |
| **Watch for hardware keyloggers** | Inspect the connection between keyboard and machine after the device has been unattended |
| **Guard against keystroke injection** | A device presenting as a keyboard types commands instantly. USB filtering tools address it |
| **Block camera and microphone physically** | A physical cover defeats software which has already compromised the device |

```bash
# Linux: check what is listening on external interfaces
ss -tulpn

# Confirm a hardware keystroke filter is active before trusting the machine
lsusb | head
```

**Physical access defeats most software controls.** A BIOS or UEFI password raises the effort for casual access, and it does not stop someone with the disk removed. Treat it as friction rather than protection.

*Canary tokens are worth knowing about. A decoy file or credential which alerts you when opened gives early warning something has access it should not. Self-hosted canary services and file-integrity monitoring both implement the idea.*

## Attack Surface Reduction

**Every listening service is a path in.** The goal is a smaller list, not a longer one.

| Target | Action |
|---|---|
| **Listening ports** | Identify what listens, then disable what you do not use |
| **SSH** | Disable password authentication in favor of keys, change the default port, and restrict source addresses |
| **File and print sharing** | Disable protocols you do not use, especially legacy SMB versions |
| **Remote access features** | Disable remote desktop and remote assistance unless actively used |
| **Voice assistants** | Disable or limit always-listening features |
| **Vendor telemetry** | Reduce usage data and diagnostic reporting to the minimum offered |
| **Secure Boot** | Keep it enabled, which complicates bootloader tampering |

```bash
# Linux: verify SSH will not accept passwords
grep -E '^PasswordAuthentication|^PermitRootLogin' /etc/ssh/sshd_config

# List enabled services to decide what deserves to stay
systemctl list-unit-files --state=enabled
```

**On Windows, the equivalent exercise is reviewing startup items and optional features.** Disabling unused services reduces both collection and attack surface, at the cost of some convenience.

*Our organizational counterpart covers the server-side version of this exercise: **[Patch Management Checklist](/checklists/patch-management-checklist/)**.*

## Isolation for Risky Activity

**When you must run something untrusted, isolation limits what a compromise reaches.** These techniques cost convenience, so reserve them for the cases which justify it.

| Technique | Isolation Level | Best For |
|---|---|---|
| **Separate user account** | Low, shares the kernel | Keeping work and personal data apart |
| **Container** | Moderate, shares the kernel | Running a service in a defined environment |
| **Virtual machine** | High, separate kernel | Testing unknown software and browsing risky sites |
| **Dedicated hardware** | Highest | Any activity you never want correlated with your identity |
| **Mandatory access control** | Orthogonal, restricts programs | Confining applications even after compromise |

**A virtual machine is the practical option for most readers** who want to inspect suspicious files or software. Remember containers share the host kernel, so a kernel vulnerability crosses the boundary. Our analysis of **[why containers are no longer a security boundary](/articles/containers-no-longer-security-boundary-2026/)** covers exactly this failure mode for the 2026 vulnerability families.

**Mandatory access control** is worth knowing on Linux, where AppArmor or SELinux confines what an application does regardless of its user's rights. Enabling it adds a layer which survives a compromised process.

*Compartmentalization is the underlying principle for all five rows. Ask what a compromise of this account or this virtual machine would reach, then reduce it until the answer is acceptable.*

{{< figure src="personal-computer-controls-by-consequence.webp" alt="Diagram ranking desktop security controls by consequence, with updates, disk encryption, and tested backups at the top and isolation techniques such as virtual machines and compartmentalization at the bottom" >}}

## The Computer Record

```text
COMPUTER RECORD
Device:                  ______________________
OS and version:          ______________________  auto-update: on / off

The three controls:
  Disk encryption:       enabled / disabled   recovery key stored at: __________
  Backup local:          ______________________  last restore test: __________
  Backup offsite:        ______________________  encrypted: yes / no
  Backup offline:        ______________________

Privilege:
  Daily account type:    standard / administrator
  Separate admin account: yes / no
  Cloud account linked:  yes / no

Attack surface:
  Listening ports reviewed: yes / no
  SSH password auth:     disabled / not applicable / not reviewed
  Sharing services off:  file / print / both / none
  Remote desktop:        disabled / enabled
  Secure Boot:           enabled / disabled / unavailable

Integrity:
  Platform protections:  enabled / disabled
  Rootkit check run:     yes / never
  Camera cover:          yes / no
```

## Next Steps

1. **Continue to Module 9** and decide what earns a place on your network: **[Smart Home and IoT](/personal-security-course/smart-home/)**
2. **Confirm disk encryption is on** and the recovery key is stored off the device
3. **Restore one file from your backup** to prove the backup works
4. **Review what listens on external interfaces** and disable anything you do not recognize
5. **Read the container boundary analysis** before treating a container as isolation: **[Containers Are No Longer a Security Boundary](/articles/containers-no-longer-security-boundary-2026/)**
6. **Read the organizational counterpart**: **[Patch Management Checklist](/checklists/patch-management-checklist/)**