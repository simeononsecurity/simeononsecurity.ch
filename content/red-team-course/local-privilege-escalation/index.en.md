---
title: "Module 13: Local Privilege Escalation"
date: 2026-09-12
toc: true
draft: false
description: "Climb from user to SYSTEM with in-memory tooling, execute-assembly, SharpUp path and service checks, and a DLL hijack against a writable PATH folder."
genre: ["Red Team", "Offensive Security", "Privilege Escalation"]
tags: ["red team", "privilege escalation", "execute-assembly", "SharpUp", "GhostPack", "DLL hijacking", "PATH", "red team course"]
cover: "/img/cover/local-privilege-escalation-techniques-windows-api.webp"
coverAlt: "A digital illustration of a Windows command window with code execution, surrounded by abstract representations of DLL files and data streams in a high-tech environment."
coverCaption: "Module 13: turn a low-privilege foothold into SYSTEM."
---

#### [← Return to the Red Team Course](/red-team-course-start/)

**Privilege escalation turns your low-privilege callback into admin or SYSTEM. The quiet paths come first, the exploits later.** Datamining and enumeration generate almost no signal, so exhaust them before you reach for anything louder.

*This module takes about 15 minutes.*

______

## Key Terms

| Term | Plain meaning |
|------|---------------|
| **execute-assembly** | running a .NET tool in-memory, fork and run |
| **SharpUp** | the C# privilege-escalation checker |
| **PATH** | the ordered folder list Windows searches |
| **DLL hijack** | planting a DLL where a service expects a missing one |
| **Fork and run** | spawning a process to run and collect output |
______

## Why Native Binaries Get You Caught

Defenders alert on `cmd.exe`, `net.exe`, `powershell.exe`, and `whoami.exe` spawning. Normal users rarely hand-launch them, so a process-creation event is a strong signal. Every `shell` command you run makes Beacon spawn `cmd.exe` to carry it, lighting up the exact binary defenders watch.

Plugins and BOFs avoid this by calling the Windows API inside the Beacon process, so no extra binary hits disk and no suspicious child process appears.

______

## execute-assembly

When no BOF or plugin exists for the job, reach for `execute-assembly`. It loads a locally hosted .NET binary into the target process memory and runs it fork and run. The binary never touches the target filesystem.

```text
execute-assembly /path/to/tool.exe
```

Fork and run spawns a temporary sacrificial process, injects the assembly, runs it, and collects the output. It is louder than a BOF, so treat it as the fallback when no in-process option exists.

______

## SharpUp

SharpUp is a C# privilege-escalation checker from GhostPack, an open-source collection of red team techniques ported to C#. Run it with:

```text
execute-assembly /path/to/SharpUp.exe
```

SharpUp scans for common local escalation openings:

- Unquoted service paths
- Weak service permissions
- Modifiable service binaries
- Writable folders in the system PATH

You get a fast read on whether the current user has a realistic path to SYSTEM, without touching disk or spawning a watched binary.

______

## DLL Hijacking: the PATH Variable

A hijack becomes possible when a writable folder appears in the Windows `PATH` variable. PATH is the ordered list Windows searches when a program asks for a resource without a full path. Whoever controls an early, writable PATH folder decides what gets loaded.

```text
PATH
```

Run SharpUp to walk every PATH folder and report which ones the current user is allowed to write to.

______

## The WptsExtensions.dll Case

A writable PATH folder alone is not enough. You also need something which tries to load a missing DLL, so your planted file is what Windows finds. On Windows 10, a service requests a missing DLL, and the absence gives you the opening.

Workflow:

1. Run SharpUp to confirm a writable PATH folder.
2. Upload a Cobalt Strike DLL to it, named to match the missing DLL.
3. Match the beacon architecture to the target. An x64 host needs an x64 DLL.
4. Reboot the box to trigger the load and get a fresh callback.

When the host returns, the service starts, searches PATH for its DLL, finds the beacon you planted, and loads it in the service context. The reboot exists only to test the hijack in a lab.

> **Operator takeaway:** a writable PATH folder plus a service looking for a missing DLL is the whole recipe. SharpUp finds the folder, and the payload is a correctly named, correctly architected DLL dropped in place before a reboot.

______

## Climb to SYSTEM

Pick the order and method for each step:

1. Which quiet read comes before any exploit?
2. Which tool checks writable PATH folders and service weaknesses?
3. What completes a DLL hijack after the writable folder is found?
4. Why does the planted binary's architecture matter?

Answer from memory first. The explanations are in the Answer Key at the end.
______

## Common Mistakes

- Shelling out to a watched binary when a BOF or plugin exists.
- Reaching for an exploit before exhausting datamining and enumeration.
- Mismatching the DLL architecture to the target.
- Skipping the reboot test in a lab, so the hijack never fires.

______

## Self-Check

1. What does `execute-assembly` run, and where?
2. Name three SharpUp checks.
3. Why is a writable PATH folder alone not enough?
4. What must match between the planted DLL and the host?

______

## Answer Key

**Self-Check**

1. **A .NET assembly, inside the target process.** Fork and run, off disk.
2. **Unquoted service paths, weak service permissions, writable PATH folders.** SharpUp scans these and more.
3. **A service must also look for a missing DLL.** The writable folder only sets the stage.
4. **The architecture.** An x64 host needs an x64 DLL.

**Exercise**

1. **Datamining and enumeration**, they generate almost no signal.
2. **SharpUp** via `execute-assembly`.
3. **A correctly named DLL**, planted and the box rebooted.
4. **A mismatch places the wrong bit-width payload**, which never loads.
______

## Next Steps

Local escalation is done. Next, persist at the elevated level with a service: privileged persistence.

**[→ Module 14: Privileged Persistence and Process Migration](/red-team-course/privileged-persistence-and-process-migration/)**

Or return to the hub: **[Red Team Course](/red-team-course-start/)**
