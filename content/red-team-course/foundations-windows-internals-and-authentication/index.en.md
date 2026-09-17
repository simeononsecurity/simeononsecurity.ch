---
title: "Module 4: Windows Internals and Authentication"
date: 2026-09-12
toc: true
draft: false
description: "How Windows stores configuration and credentials: the registry and hives, registry paths, NTLM hashes, and the difference between domain and local authentication."
genre: ["Red Team", "Offensive Security", "Windows Internals"]
tags: ["red team", "Windows internals", "registry", "HKLM", "HKCU", "NTLM", "pass the hash", "hashdump", "domain authentication", "local authentication", "red team course"]
cover: "/img/cover/windows-internals-authentication-registry-structure.webp"
coverAlt: "An illustration of the Windows Registry, showing a tree structure with folders and files, emphasizing HKLM and HKU hives, and abstract representations of NTLM hashes in vibrant colors on a dark background."
coverCaption: "Module 4: where Windows stores configuration and credentials."
---

#### [← Return to the Red Team Course](/red-team-course-start/)

**Module 3 covered the domain. This module drops to the host: how Windows stores its configuration, and how it stores and checks passwords.** You write to the registry when you persist, you pass hashes when you move, and you act as other users constantly. All of it starts here.

*This module takes about 12 minutes. It is the reference point for persistence and credential access later.*

______

## The Windows Registry

The **registry** stores configuration for the operating system and programs in a hierarchy, like a file system. Four terms carry the whole model:

| Term | Like a | Holds |
|------|--------|-------|
| **Key** | folder | other keys |
| **Value** | file | one configuration detail |
| **Type** | format | the data format, such as `REG_SZ` |
| **Data** | content | the actual value string |

A concrete `Run` entry reads value `Synapse3`, type `REG_SZ`, data pointing at a startup program. The `Run` key lives inside the `CurrentVersion` key. You read and write these directly when you set persistence, so the folder-and-file model is worth locking in now.

______

## Hives

A **hive** is a top-level branch of the registry. Two matter most:

- **`HKLM` (HKEY_LOCAL_MACHINE)** is the system hive. It holds most Windows configuration and needs administrative or SYSTEM privileges to edit.
- **`HKU` (HKEY_USERS)** is a set of per-user hives, each named by a user's security identifier (SID). One exists for every user who has logged on.

______

## HKCU and the SYSTEM Trap

**`HKCU` (HKEY_CURRENT_USER)** is not a separate hive. It is a pointer to the `HKU` hive of the user currently logged in. Two paths resolve to the same run key:

```text
HKCU\Software\Microsoft\Windows\CurrentVersion\Run
HKEY_USERS\S-1-5-21-<SID>\Software\Microsoft\Windows\CurrentVersion\Run
```

The trap shows up when you operate as SYSTEM. If you write user persistence under `HKCU` as your user, then return as a SYSTEM session and reference `HKCU`, it points at SYSTEM's hive, not the user's.

> **Operator takeaway:** to touch a user's run key from a SYSTEM callback, find the user's SID and go through `HKU` directly. Reading the pointer wrong is why cleanup misses.

______

## DHCP and Logging

**DHCP** assigns an IP address and network settings automatically. Verify a host with `ipconfig /all`.

The operational note is logging. A host with DHCP enabled comes back on a different IP. If your notes assume a fixed address, a lease change makes an old machine look new, or hides a machine you already own.

______

## Windows Hashes and NTLM

A **hash** is a one-way translation of a password into an encoded string. Windows hashes the plaintext and stores the result. Two properties drive the attacks:

- **NTLM hashes are not salted.** Two users with the same password receive identical hashes.
- **Storage splits by account type.** Domain hashes live on the Domain Controller. Local hashes live on the machine itself.

A `hashdump` yields the NTLM hash. The older LM hash is typically disabled in modern environments, so the NTLM hash is what you feed into **pass-the-hash**. No plaintext is required. NTLM is also unsalted, which means two users sharing a password produce matching hashes.

______

## Domain vs Local Authentication

Windows authentication in this course uses the `DOMAIN\username` form.

| Account | Form | Example |
|---------|------|---------|
| **Domain** | `DOMAIN\user` | `CORP\Bob` |
| **Local** | `MACHINE\user` or `.\user` | `WIN7-WS\Admin` |

A prefix mismatch trips people up. If the prefix does not resolve to a valid domain, Windows falls back to local authentication. This is why a local account uses the computer name as its prefix. Get the prefix wrong and your token behaves in ways you did not plan.

> **Operator takeaway:** domain hashes come from the DC, local hashes from the box. NTLM is unsalted, and the hash alone authenticates via pass-the-hash.

______

## These Concepts Feed Your Tooling

| Concept | Tool it feeds | What you do with it |
|---------|---------------|---------------------|
| **Registry run key** | `reg_set` / `reg_query` | write and verify persistence |
| **`HKU` hive by SID** | `reg_query` | reach a user key from SYSTEM |
| **NTLM hash** | `pth` | authenticate without plaintext |
| **Realm naming** | `spawnas` / `make_token` | act as another account |

> **Why it matters:** Where Windows keeps configuration and credentials decides where persistence lands and how you move. The HKCU pointer and unsalted NTLM are the two details which trip operators.

______

## Key Terms

| Term | What it is | Red team angle |
|------|-----------|----------------|
| Registry key | folder of config | where run-key persistence lives |
| `HKLM` | system hive | needs admin or SYSTEM |
| `HKU` | per-user hives by SID | reach user run keys from SYSTEM |
| `HKCU` | pointer to the current user | resolves wrong from SYSTEM |
| NTLM hash | unsalted password hash | pass-the-hash material |
| `DOMAIN\user` | auth naming | wrong prefix triggers local fallback |

______

## Trace a Persistence Path

You hold a SYSTEM callback on a workstation and need to read a run key a low-privilege user planted earlier:

1. Which hive holds the user's run key?
2. Why does `HKCU` point to the wrong place from a SYSTEM session?
3. How do you locate the user's hive?
4. Where do domain hashes live versus local hashes?

Answer from memory first. The explanations are in the Answer Key at the end.

______

## Why Windows Internals Matter

Authentication artifacts explain what a token proves and what a password exchange exposes. Legacy NTLM habits still work in some environments, but modern policy favors Kerberos, credential isolation, and multifactor authentication. Security logs, token inspection, and a disposable VM demonstrate the distinction without collecting real credentials. **Stop when the exercise reaches a real user secret.**

______

## Common Mistakes

- Referencing `HKCU` from a SYSTEM callback and cleaning the wrong hive.
- Assuming a host keeps a fixed IP when DHCP is enabled.
- Writing persistence under `HKLM` without admin rights.
- Treating the LM hash as live when modern environments disable it.

______

## Self-Check

1. What is the relationship between `HKCU` and `HKU`?
2. Why are NTLM hashes unsalted, and why does it matter?
3. Where do domain hashes live versus local hashes?
4. What happens when an auth prefix does not resolve to a valid domain?

______

## Answer Key

**Self-Check**

1. **HKCU is a pointer to the current user's HKU hive.** They resolve to the same keys, but only for whoever is logged on now.
2. **Unsalted means equal passwords give equal hashes.** Reuse and cracking both lean on it.
3. **Domain hashes live on the DC, local hashes on the box.** Storage splits by account type.
4. **Windows falls back to local authentication.** An unresolvable prefix quietly tries local auth, and the token behaves unexpectedly.

**Exercise**

1. **The user's own HKU hive.**
2. **HKCU resolves to SYSTEM, not the user.** The SYSTEM session points at its own hive.
3. **By SID, found with whoami or wmi_query.** Then reference HKU with the SID.
4. **Domain on the DC, local on the box.**

______

## Next Steps

You now know where Windows keeps configuration and credentials. Next comes the tooling driving the beacon: command and control.

**[→ Module 5: Command and Control Operations](/red-team-course/command-and-control-operations/)**

Or return to the hub: **[Red Team Course](/red-team-course-start/)**
