---
title: "Module 11: Situational Awareness and Host Operations"
date: 2026-09-12
toc: true
draft: false
description: "Know the state of a host before you act: Windows and Linux situational-awareness commands, and when to run the quieter BOF or plugin form."
genre: ["Red Team", "Offensive Security", "Post Exploitation"]
tags: ["red team", "situational awareness", "post exploitation", "ipconfig", "netstat", "tasklist", "hashdump", "logonpasswords", "uname", "red team course"]
cover: "/img/cover/situational-awareness-post-exploitation-techniques.webp"
coverAlt: "A cybersecurity professional in a dark workspace is analyzing multiple computer screens showing network maps and system statistics, surrounded by data visualizations in vibrant colors."
coverCaption: "Module 11: know the box before you change it."
---

#### [← Return to the Red Team Course](/red-team-course-start/)

**You have a callback. Post-exploitation begins, and situational awareness is the discipline running underneath all of it.** Learn what a tool is for, not the exact syntax, and run the quiet commands before every loud action.

*This module takes about 12 minutes.*

______

## Key Terms

| Term | Plain meaning |
|------|---------------|
| **Situational awareness** | knowing box and network state before acting |
| **BOF enumeration** | the in-memory, quiet form of a command |
| **Dual-homed host** | a box with a second interface into another segment |
| **hashdump** | the plugin pulling hashes from the SAM (SYSTEM) |
| **logonpasswords** | the plugin pulling plaintext credentials (SYSTEM) |
______

## What Situational Awareness Buys You

Situational awareness (SA) means knowing the state of the box and the network around it before you act. Run SA at three moments:

- Before anything with large system impact, such as a privilege-escalation exploit.
- Right after access, to understand where you landed.
- Periodically while operating, because the picture goes stale.

In Cobalt Strike terms, SA is mostly quiet enumeration you run from Beacon. Some of it is not quiet, and those commands are deliberate moves.

______

## Windows SA Commands

The recommended initial set, with the quieter BOF or plugin form noted:

| Goal | Native command | Quieter form |
|------|----------------|--------------|
| Confirm in scope | `ipconfig /all` | `ipconfig` BOF |
| List processes | `tasklist` | `ps` plugin or `tasklist` BOF |
| User details | `net user <user> /domain` | `netuser` BOF |
| Connections | `netstat -anop tcp` | `netstat` BOF |
| Dump hashes (SYSTEM) | `hashdump` plugin | (high risk, deliberate) |
| Credentials (SYSTEM) | `logonpasswords` plugin | (high risk, deliberate) |

`hashdump` and `logonpasswords` carry a high chance of being discovered or scooped. Run them only when you hold SYSTEM and have decided the noise is worth it.

> **Operator takeaway:** prefer the BOF and plugin forms over shelling out to native binaries. They run in Beacon memory and avoid spawning noisy child processes.

______

## Linux SA Commands

If you land on a Linux host, the set is short:

- `ip addr`: verify scope, and check for a second IP.
- `netstat -pantu`: active connections in, out, and listening.
- `uname -a`: version and distribution.
- `w`: who is logged on, and what they are doing.
- `last`: recently logged-on users.

The two-IP check matters. A dual-homed host bridges into a segment you have not seen, which is often the whole reason to care about a Linux box in a Windows-heavy environment.

______

## Check a Fresh Callback

You landed a new callback. Walk the first moments:

1. What do you confirm before anything else?
2. Which two commands show the host's processes and connections?
3. On a Linux box, what reveals a second network path?
4. Which reads do you hold until you have SYSTEM, and why?

Answer from memory first. The explanations are in the Answer Key at the end.
______

## Common Mistakes

- Running a loud SA command where a quiet BOF does the same thing.
- Dumping hashes before you hold SYSTEM.
- Forgetting the dual-homed Linux check and missing a bridged segment.
- Acting before confirming you are in scope.

______

## Self-Check

1. When should you run situational awareness?
2. Give two Windows SA commands with a quieter form.
3. Why does the two-IP check on Linux matter?
4. Which SA commands are deliberately loud, and why?

______

## Answer Key

**Self-Check**

1. **Before loud actions, right after access, and periodically.** The picture goes stale as you operate.
2. **`ipconfig /all` becomes the `ipconfig` BOF, `netstat -anop tcp` becomes the `netstat` BOF.** The quieter form runs in Beacon memory.
3. **A second IP bridges a segment you have not seen.** The dual-homed host is often the real reason to care.
4. **`hashdump` and `logonpasswords`.** They are easy to spot, so run them only with SYSTEM and a decision the noise is worth it.

**Exercise**

1. **Scope**, confirm you are on the right host.
2. **`ps` (or `tasklist`) and `netstat`.**
3. **`ip addr`** showing two addresses.
4. **`hashdump` and `logonpasswords`**, deferred until SYSTEM.
______

## Next Steps

You know the box. Next, the first of the five post-exploitation phases: holding access across reboots.

**[→ Module 12: User Persistence](/red-team-course/user-persistence/)**

Or return to the hub: **[Red Team Course](/red-team-course-start/)**
