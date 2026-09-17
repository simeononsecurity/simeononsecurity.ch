---
title: "Module 12: User Persistence"
date: 2026-09-12
toc: true
draft: false
description: "Hold a low-privilege foothold across reboots with registry run keys, blending the value in, and hiding the payload next to files which belong there."
genre: ["Red Team", "Offensive Security", "Persistence"]
tags: ["red team", "persistence", "run key", "registry", "reg_set", "reg_query", "timestomp", "HKCU", "red team course"]
cover: "/img/cover/user-persistence-techniques-windows-registry.webp"
coverAlt: "An illustration of a computer screen showing a Windows registry editor. The focus is on the 'Run' key path, with vibrant colors highlighting the persistence techniques. The background is dark."
coverCaption: "Module 12: hold the foothold across reboots."
---

#### [← Return to the Red Team Course](/red-team-course-start/)

**Persistence is the first goal once you have access. If the machine restarts or the user logs out, an unmanaged foothold is gone.** Many techniques exist, and picking the right one for the situation is a core operator skill, not a checkbox.

*This module takes about 12 minutes.*

______

## Key Terms

| Term | Plain meaning |
|------|---------------|
| **Run key** | registry value launching a program at login |
| **HKCU** | the per-user hive pointer |
| **Timestomp** | editing a file's timestamps to blend |
| **BOF** | the in-memory `reg_set` / `reg_query` form |
| **Roaming profile** | the profile following a user between machines |
______

## Two Methods

| Method | Requires | Notes |
|--------|----------|-------|
| **Service persistence** | admin | launches the implant at startup as SYSTEM, covered in privileged persistence |
| **Run key persistence** | basic user or admin | starts on login, works from the low-privilege context |

For this module the focus is the run key, since it works from the low-privilege context most initial callbacks land in.

______

## The Run Key

You add a value to the `Run` key in the registry. The user-level location is `HKCU\Software\Microsoft\Windows\CurrentVersion\Run`. Because `HKCU` is per user, a roaming profile carries the run key to any system the user logs into, quietly widening your reach.

______

## Building a Run Key

The workflow:

1. Upload the executable to a quiet place, usually under the user's appdata folder.
2. Timestomp the executable so it blends with the surrounding folder.
3. Add the run key value.

The native form:

```text
REG ADD "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" /V "My App" /t REG_SZ /F /D "C:\MyAppPath\MyApp.exe"
```

The native form uses `reg.exe`, so operators prefer the Cobalt Strike BOFs:

```text
reg_set HKCU SOFTWARE\microsoft\windows\currentversion\run testValue REG_SZ C:\beacon.exe
reg_query HKCU SOFTWARE\microsoft\windows\currentversion\run
reg_delete HKCU SOFTWARE\microsoft\windows\currentversion\run testValue
reboot 127.0.0.1
```

`reboot` exists so you prove the beacon returns. Do not reboot a customer host to test persistence on a real operation.

> **Operator takeaway:** query before you add, and query again after. Keep a precise log of what you set and where, because this run key gets cleaned up later.

______

## Blending In

Run key value names matter. Real entries look like `Synapse3`, `OneDrive`, or `Spotify`, and none carries a `.exe` in the name. Name your value the way legitimate software names its own, so a defender scrolling the `Run` key sees nothing unexpected.

______

## Hiding Files on Target

Place the payload next to files which already belong there:

- Running as a **user**: upload to the user directory. Survey the appdata folders, find an existing file, and match the beacon's filename to it.
- Running as **SYSTEM**: payloads go to `C:\Windows\System32` or `SysWOW64`, remembering the 32-bit filesystem redirection rule.

Do not forget to timestomp where possible. A file dated today in a folder full of three-year-old files is an easy flag.

______

## Hold a Foothold

A normal user callback must survive reboot. Answer:

1. Which persistence method works from this low-privilege context?
2. Where do you drop the executable so it blends?
3. What do you set with the `reg_set` BOF?
4. What do you do to the file's timestamp before finishing?

Answer from memory first. The explanations are in the Answer Key at the end.
______

## Common Mistakes

- Naming the run key value with a file extension, unlike legitimate software.
- Placing the payload alone in an odd directory instead of beside similar files.
- Skipping timestomp and leaving a fresh creation date in an old folder.
- Rebooting a customer host to test persistence.

______

## Self-Check

1. Why does `HKCU` persist a roaming profile across machines?
2. Give the three-step BOF workflow for a run key.
3. How should you name the value, and why?
4. Where do user payloads land versus SYSTEM payloads?

______

## Answer Key

**Self-Check**

1. **HKCU is per user, so a roaming profile carries the key to each machine the user logs into.**
2. **`reg_set` to add, `reg_query` to verify, `reboot` to test** the value in a lab.
3. **Like legitimate software, no `.exe` in the name.** A file-extension value stands out in the key.
4. **User payloads go to the user's appdata, SYSTEM payloads to System32 or SysWOW64.**

**Exercise**

1. **The run key**, it works from low privilege.
2. **The user's appdata folder**, beside files which belong there.
3. **A value pointing at the beacon** under the `Run` key.
4. **Timestomp it** to match the surrounding files.
______

## Next Steps

Your low-privilege foothold now survives. Next, climb out of the low-privilege context: local privilege escalation.

**[→ Module 13: Local Privilege Escalation](/red-team-course/local-privilege-escalation/)**

Or return to the hub: **[Red Team Course](/red-team-course-start/)**
