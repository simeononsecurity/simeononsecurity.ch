---
title: "CompTIA A+ (220-1202): Operating Systems"
date: 2025-01-01
toc: true
draft: false
description: "Master operating systems for the CompTIA A+ 220-1202 Core 2 exam. Learn OS types, installations, Windows editions, tools, command line, settings, networking, macOS, and Linux."
genre: ["CompTIA A+ Course", "Operating Systems", "Windows Administration", "Linux", "macOS", "IT Support", "CompTIA Certification", "Help Desk", "Command Line", "IT Fundamentals"]
tags: ["CompTIA A+", "220-1202", "operating systems", "Windows", "Linux", "macOS", "Chrome OS", "NTFS", "command line", "ipconfig", "Task Manager", "Registry Editor", "GPT", "MBR", "installations"]
cover: "/img/cover/comptia-a-plus-operating-systems-workspace.webp"
coverAlt: "An illustration of a modern workspace featuring three computer screens. One screen shows Windows with Task Manager, another displays macOS with its dock, and the third shows a Linux terminal."
coverCaption: "Master Operating Systems for the A+ 220-1202 Exam"
---

#### [Click Here to Return To the CompTIA A+ Course Page](/a-plus-start/)

**Operating Systems** is **28%** of the **CompTIA A+ 220-1202 Core 2** exam, the largest Core 2 domain. This module covers OS types, installations, Windows editions, tools, the command line, settings, and macOS and Linux. *Core 2 is software-focused, and this domain rewards hands-on practice in real systems.*

The operating system is where users and hardware meet. You install it, configure it, fix it, and secure it. This module covers the three desktop platforms and the Windows tools and commands you will use every shift.

## OS Types and Filesystems

You match the OS and filesystem to the device.

| OS | Common filesystem |
|----|-------------------|
| **Windows** | NTFS, ReFS, FAT32, exFAT |
| **macOS** | APFS, HFS+ |
| **Linux** | ext4, XFS, Btrfs |
| **Chrome OS** | Cloud-centric, ext4 underneath |
| **Mobile (Android/iOS)** | Sandboxed app storage |

**NTFS** supports permissions, encryption, and large files. **FAT32** is universal but caps files at 4 GB. **exFAT** removes that cap for large external drives.

## Installations and Upgrades

You deploy Windows the right way for the situation.

| Method | Use |
|--------|-----|
| **Clean install** | Fresh OS, wipes the disk |
| **In-place upgrade** | Keeps apps and files |
| **Image deployment** | Mass rollout from one image |
| **Repair install** | Fixes a broken OS, keeps data |

**Partition styles** matter at install: **GPT** supports drives larger than 2 TB and many partitions, while **MBR** is the legacy limit of four primary partitions and 2 TB.

## Windows Editions

You pick the edition by required features.

| Edition | Key features |
|---------|--------------|
| **Home** | Basic, no domain join |
| **Pro** | Domain join, BitLocker, Group Policy, RDP host |
| **Enterprise** | Volume licensing, advanced management |

*Only Pro and higher can join a domain and host Remote Desktop.*

## Windows Tools

You manage the system with built-in utilities.

- **Task Manager** shows processes, performance, startup apps, and services.
- **Event Viewer** logs system, application, and security events.
- **Disk Management** creates, formats, and resizes partitions.
- **Registry Editor (regedit)** edits the Windows configuration database. *Back up the registry before edits.*
- **MMC snap-ins** host tools like Device Manager and Local Users and Groups.

## Command-Line Tools

You troubleshoot fast from the command line.

```powershell
ipconfig /all          # View full IP configuration
ping 8.8.8.8           # Test connectivity
nslookup example.com   # Query DNS
netstat -ano           # List connections and owning PIDs
sfc /scannow           # Repair protected system files
chkdsk /f              # Check and fix the filesystem
robocopy C:\src D:\dst /E   # Mirror folders, including subdirs
```

For a deeper reference, read the [Windows command line guide](/guides/windows-command-line-guide/) and the [Windows directory structure guide](/articles/windows-directory-structure-guide/).

## Windows Settings and Networking

You configure how Windows joins and protects the network.

- **Workgroup vs domain**: a workgroup is peer-to-peer, a domain is centrally managed by Active Directory.
- **Windows Defender Firewall** filters inbound and outbound traffic.
- **VPN connections** tunnel traffic securely to a remote network.
- **Proxy settings** route web traffic through a filtering server.

## macOS and Linux

You support the other two desktop platforms.

- **macOS** uses **System Settings**, **Terminal**, **FileVault** disk encryption, **Time Machine** backups, and **Spotlight** search.
- **Linux** runs core commands you must know:

```bash
ls -l            # List files with permissions
chmod 755 file   # Set permissions
sudo apt update  # Update packages (Debian/Ubuntu)
sudo dnf install # Install packages (Fedora/RHEL)
```

New to Linux? Start with the [best Linux distros for beginners](/articles/best-linux-distros-for-beginners/).

## Next Steps

Continue Core 2 with [Security](/a-plus/security-threats-vulnerabilities-best-practices/) and [Software Troubleshooting](/a-plus/software-troubleshooting-windows-apps-malware/). Close out the exam with [Operational Procedures](/a-plus/operational-procedures-documentation-communication/). Return to the [CompTIA A+ Course](/a-plus-start/) and review [tips for passing CompTIA exams](/articles/tips-and-tricks-for-passing-comptia-exams/).
