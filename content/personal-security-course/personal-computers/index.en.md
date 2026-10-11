---
title: "Module 8: Personal Computer Security"
date: 2026-09-30
lastmod: 2026-10-10
toc: true
draft: false
description: "Verify computer encryption, recovery keys, backups, updates, account privilege, listening services, malware protection, and safe isolation with safe rollback."
genre: ["Personal Security", "Computer Security", "Endpoint Security", "Privacy", "Operating Systems"]
tags: ["computer security", "endpoint security", "full disk encryption", "bitlocker", "filevault", "luks", "least privilege", "secure boot", "ssh hardening", "rootkit", "keylogger", "usbguard", "virtual machines", "compartmentalization", "mandatory access control", "canary tokens", "personal security course"]
cover: "/img/cover/personal-computer-security-controls-updates-encryption-backups.webp"
coverAlt: "An illustration of a modern desktop computer setup showcasing three key security concepts: automatic updates, full disk encryption, and backups, with vibrant colors against a dark background."
coverCaption: "Module 8: verify updates, encryption, and backups"
---

[← Return to the Personal Security Course](/personal-security-course-start/)

**Start a desktop review with updates, disk encryption, and tested backups.** Updates close known flaws. Encryption protects data after powered-off device theft. Backups support recovery after loss, failure, or destructive malware. The remaining controls reduce exposure and limit damage.

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
| **Full disk encryption** | Protecting data at rest when the device is powered off and keys remain unavailable |
| **Least privilege** | Operating with the minimum rights needed for the task at hand |
| **Attack surface** | The set of services, ports, and interfaces reachable by an attacker |
| **Keystroke injection** | A device which presents itself as a keyboard and types commands |
| **Mandatory access control** | A policy layer which restricts programs beyond file permissions |
| **Canary token** | A decoy file or credential which alerts you when it is touched |

## Three Starting Controls

### 1. Automatic Updates

**Supported updates close known flaws and reduce exposure time.** They do not repair stolen credentials, unsafe configuration, or unsupported hardware.

- **Enable automatic updates** for the operating system and restart when prompted
- **Update applications separately.** Browsers, document readers, and media players are common targets
- **Include firmware and drivers** where the vendor supports automatic delivery

*A restart prompt might complete an update, driver change, or maintenance task. Read the update status and finish security updates promptly.*

### 2. Full Disk Encryption

**Full-disk encryption reduces data exposure after powered-off device theft when keys and recovery methods remain protected.** Without effective encryption, storage might expose files or application data, subject to separate application encryption and account controls.

| Platform | Feature | Where to Check |
|---|---|---|
| **Windows** | BitLocker or Device Encryption | Settings, Privacy and Security, Device encryption |
| **macOS** | FileVault | System Settings, Privacy and Security, FileVault |
| **Linux** | LUKS | Confirm root and home volumes at install time |

**Verify your recovery key is stored somewhere other than the encrypted disk.** A recovery key only on the encrypted volume is not a recovery key.

*Turning the device fully off rather than leaving it in standby matters once encryption is enabled. A suspended machine often holds keys in memory.*

### 3. Backups

**A tested backup supports recovery from ransomware, theft, and hardware failure.** Account security, encryption, and incident response address different parts of those events.

- **Keep one local copy** for fast restores
- **Keep one encrypted offsite copy** for fire and theft
- **Keep one offline or write-only copy** for ransomware which reaches your synced storage

**Test a restore.** A backup never restored is an assumption.

## Least Privilege on a Desktop

**Daily administrator use gives launched processes broad rights.** A standard daily account reduces the authority available to routine applications and mistakes.

| Practice | Why It Matters |
|---|---|
| **Use a standard account for daily work** | Routine processes start with fewer rights, while privilege escalation remains a separate risk |
| **Elevate only for administrative tasks** | Limits what runs with full rights |
| **Review local and cloud account trade-offs** | Cloud accounts add sync and recovery features plus provider dependency. Local accounts reduce selected sharing but need separate recovery |
| **Review installed applications** | Fewer applications means fewer update obligations and fewer targets |
| **Lock the screen on idle** | Reduces casual access while the machine is unattended. Active sessions and unlocked data still need protection |

**Separate accounts provide one useful compartment boundary.** Use a standard account for daily work and an administrative account for elevation. Windows, macOS, and Linux support separate local accounts, while some platforms also support provider-linked accounts with different sync and recovery behavior.

*The measurement for this module is not how many controls you enabled. It is how much an attacker gains from compromising one account.*

## Endpoint Integrity

**These controls answer a different question: is the machine currently trustworthy?**

| Control | What It Addresses |
|---|---|
| **Built-in platform protections** | Defender, Gatekeeper, and distribution security controls provide a supported baseline |
| **Additional endpoint software** | Evaluate support, detection evidence, privacy terms, accessibility, and compatibility before installation |
| **Targeted integrity checks** | Use platform logs, security tools, or specialist help after a concrete warning. A periodic scanner result alone does not prove trust |
| **Watch for hardware keyloggers** | Inspect the connection between keyboard and machine after the device has been unattended |
| **Guard against keystroke injection** | A device presenting as a keyboard types commands instantly. USB filtering tools address it |
| **Use physical camera covers or microphone disconnects where suitable** | A camera cover blocks the lens. Microphone protection requires a hardware disconnect, trusted mute design, or device without a microphone |

```bash
# Linux: check what is listening on external interfaces
ss -tulpn

# Inventory attached USB devices for comparison with your own baseline
lsusb
```

**Physical access threatens a running or unlocked computer.** Full-disk encryption protects powered-off storage when keys stay unavailable. A firmware password adds friction but does not replace encryption or a strong device lock.

*Canary tokens are worth knowing about. A decoy file or credential which alerts you when opened gives early warning something has access it should not. Self-hosted canary services and file-integrity monitoring both implement the idea.*

## Attack Surface Reduction

**A listening service adds reachable code and configuration.** Keep services with a documented purpose, supported version, and suitable access policy.

| Target | Action |
|---|---|
| **Listening ports** | Identify what listens, then disable what you do not use |
| **SSH** | Validate key login, then disable password authentication where recovery access exists. Restrict exposure and source addresses |
| **File and print sharing** | Disable protocols you do not use, especially legacy SMB versions |
| **Remote access features** | Disable remote desktop and remote assistance unless actively used |
| **Voice assistants** | Disable or limit always-listening features |
| **Vendor telemetry** | Reduce usage data and diagnostic reporting to the minimum offered |
| **Secure Boot** | Keep it enabled, which complicates bootloader tampering |

```bash
# Linux: ask sshd for the effective policy, including defaults and included files
# This read-only command often needs root privileges to access host keys and configuration.
sudo sshd -T | grep -E '^(passwordauthentication|permitrootlogin) '

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
| **Dedicated hardware** | Strong device boundary | Work which needs separation from daily files and accounts. Network, payment, behavior, and identity links still allow correlation |
| **Mandatory access control** | Orthogonal, restricts programs | Confining applications even after compromise |

**A virtual machine adds a boundary for controlled testing.** Disable shared folders, clipboard, host integration, and unneeded networking. Take a clean snapshot and delete the test VM afterward. VM escapes and user mistakes still expose the host. A dedicated spare device gives a stronger boundary for high-risk files.

**Mandatory access control** is worth knowing on Linux. An enforced AppArmor or SELinux policy limits a process according to defined rules. Coverage, policy quality, kernel security, privileged access, and escape paths bound the protection.

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
  Security warnings:     reviewed / unresolved
  Camera cover:          yes / no
```

## Practice and Verify

Work from a standard user account. Keep the encryption recovery key and backup outside the computer.

1. Install supported operating-system and application updates.
2. Confirm full-disk encryption status through the operating-system settings.
3. Locate the recovery-key record without displaying or copying the key into this worksheet.
4. Restore one harmless file from backup to a new folder and compare its contents.
5. List listening services. Identify the owner and purpose of each externally reachable entry.
6. If SSH is enabled, prove key login in a second session before changing password authentication. Keep the first session open until validation ends.

> **Expected Result:** updates complete, encryption reports active, recovery material is reachable away from the device, the restored file opens correctly, and each listening service has a reason.

If the recovery key is missing, do not trigger a recovery prompt. Follow the vendor backup process first. If an update or service change breaks a needed function, revert the one change through the operating-system history or saved configuration. Never restart SSH after a syntax or key-login failure.

```text
REDACTED EXAMPLE
Platform:              Windows 11
Updates:               current on 2026-10-10
Disk encryption:       on
Recovery key:          verified in separate account
Restore test:          one document opened and matched
Listening services:    4 reviewed, 4 explained
Daily account:         standard
```

**Pass checklist**

- [ ] Encryption status and separate recovery-key access are verified
- [ ] One file restore succeeded
- [ ] Daily work uses the intended account privilege
- [ ] Every reachable service has an owner and purpose
- [ ] Isolation settings and cleanup match the risk of the tested file

**Primary references, checked 2026-10-10:** [Microsoft BitLocker recovery-key backup](https://support.microsoft.com/en-us/windows/security/encryption/back-up-your-bitlocker-recovery-key), [Apple FileVault guidance](https://support.apple.com/guide/mac-help/protect-data-on-your-mac-with-filevault-mh11785/mac), and [CISA ransomware backup guidance](https://www.cisa.gov/resources-tools/resources/stopransomware-guide).

## Next Steps

1. **Continue to Module 9** and decide what earns a place on your network: **[Smart Home and IoT](/personal-security-course/smart-home/)**
2. **Confirm disk encryption is on** and the recovery key is stored off the device
3. **Restore one file from your backup** to prove the backup works
4. **Review what listens on external interfaces** and disable anything you do not recognize
5. **Read the container boundary analysis** before treating a container as isolation: **[Containers Are No Longer a Security Boundary](/articles/containers-no-longer-security-boundary-2026/)**
6. **Read the organizational counterpart**: **[Patch Management Checklist](/checklists/patch-management-checklist/)**
