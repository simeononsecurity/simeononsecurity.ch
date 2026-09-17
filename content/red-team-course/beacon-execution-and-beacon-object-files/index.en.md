---
title: "Module 6: Beacon Execution and Beacon Object Files"
date: 2026-09-12
toc: true
draft: false
description: "How the Cobalt Strike Beacon runs code: fork-and-run versus in-process Beacon Object Files (BOFs), loading aggressor scripts, and the BOF toolkits for enumeration and action."
genre: ["Red Team", "Offensive Security", "Command and Control"]
tags: ["red team", "Beacon Object File", "BOF", "Cobalt Strike", "fork and run", "aggressor script", "in-process execution", "code execution", "red team course"]
cover: "/img/cover/beacon-object-file-execution-process.webp"
coverAlt: "An abstract digital representation of a Beacon Object File execution, showing a dynamic flow of data within a computer interface against a dark background, with vibrant colors illustrating the concept of in-memory code execution."
coverCaption: "Module 6: run code inside the beacon, not beside it."
---

#### [← Return to the Red Team Course](/red-team-course-start/)

**A Beacon Object File (BOF) is how you run a small, custom action inside the beacon you already hold.** It trades a safety margin for stealth, and it changes which tools you reach for.

*This module takes about 12 minutes.*

> **Why it matters:** Every new process is a chance to get caught. A BOF runs inside the beacon you already hold, but it shares the process, so a crash costs access.

______

## Key Terms

| Term | Plain meaning |
|------|---------------|
| **Beacon Object File (BOF)** | a compiled C snippet running inside the beacon process |
| **COFF** | the object-file format a BOF compiles to |
| **Aggressor script (.cna)** | the script registering BOF commands |
| **Fork and run** | spawning a process to run code |
| **In-process** | running code inside the existing beacon |
| **Shellcode** | position-independent code injected into a process |

______

## What a BOF Is

A **Beacon Object File (BOF)** is a small compiled C program, a COFF object file (`.o`) executing inside the running beacon process. It calls Windows APIs directly and avoids spawning a new process.

This idea explains why BOFs exist. Older tooling spawned a fresh process to do its work, a pattern defenders catch. A BOF runs in the memory of the beacon you already have, does its job, and returns output. No new process, a much smaller footprint.

______

## Fork and Run vs In-Process

| Method | How it works | Noise |
|--------|--------------|-------|
| **Fork and run** | spawns a temporary process or injects into one | new process and thread defenders catch |
| **In-process (BOF)** | runs inside the existing beacon | no new process, less to signature |

Beacon also offers `shell`, `run`, and `execute` paths which call binaries already on the host. Those are living off the land, and operators steer away from them wherever a BOF exists.

> **Operator takeaway:** reach for the quietest method doing the job. For most enumeration, this is a BOF.

______

## Advantages and Limitations

| Side | Point |
|------|-------|
| **Advantage** | small and fast, low footprint |
| **Advantage** | extends the beacon without rebuilding it |
| **Limitation** | a crash takes the beacon down |
| **Limitation** | single-threaded, runs to completion |
| **Limitation** | takes real C and Windows API effort to write |

A BOF shares the beacon's process, so a badly-behaved BOF is a risk to your access, not only to the current task.

______

## Loading BOFs

BOF commands do not appear until you load the aggressor script (`.cna`) registering them.

1. Open the **Script Manager**.
2. Load the combined script file from your tooling directory.
3. Confirm the new commands appear in beacon help.

If a BOF command is not recognized mid-operation, check the script is loaded first.

> **Operator takeaway:** no aggressor script, no BOF commands. Load the combined script before you start working.

______

## BOF Toolkits

Most operators run a mix of public toolkits and in-house code:

| Toolkit | Purpose |
|---------|---------|
| **Situational awareness BOFs** | in-memory host, network, and AD enumeration |
| **Remote ops BOFs** | registry, service, and process actions |
| **Operator utilities** | additional operator support |
| **Custom tooling** | Kerberoasting, log queries, service manipulation |

You do not memorize every command. You learn which tool does which job, so you reach for the right one when a task asks you to enumerate a trust or act on a service.

______

## Off-Limits Commands

Some beacon commands are restricted unless told otherwise. The pattern covers destructive actions, loud operations, and shortcuts which skip a technique you are meant to run the quieter way.

Treat the off-limits list as a hard boundary, the same way you treat the out-of-scope list. Knowing what you are not allowed to run is part of operating cleanly.

______

## Process Injection

When no BOF exists, you inject shellcode into another process. Early Bird APC injection queues the payload so it runs before the thread's main routine, defeating a common detection window.

{{< youtube id="_sI76NLPMjI" >}}

Watch the technique: [Early Bird APC code injection](https://www.youtube.com/watch?v=_sI76NLPMjI)

______

## Choose the Execution Method

For each task, name the quietest execution path and why:

1. Enumerate domain trusts.
2. Run a .NET privilege-escalation checker with no native BOF.
3. Inject a payload queued to fire before a new thread's main routine.

Answer from memory first. The explanations are in the Answer Key at the end.

______

## Why Execution Location Matters

Execution location changes the telemetry footprint and the failure radius. A child process gives defenders a process tree, while in-process code avoids a child process but shares the host process and its crash risk. A benign BOF or test DLL in a snapshot demonstrates the tradeoff without deploying a payload to a production host. **Prefer a simulator when the code has destructive side effects.**

______

## Common Mistakes

- Expecting a BOF command to exist before loading its aggressor script.
- Using a fork-and-run tool where a quieter BOF does the job.
- Forgetting a BOF shares the beacon process, so a crash costs the beacon too.
- Running a restricted command instead of the quieter technique it masks.

______

## Self-Check

1. Where does a BOF execute, and why does it shrink the footprint?
2. Contrast fork-and-run against in-process execution.
3. Why does a BOF command not appear until the script loads?
4. Name one limitation of a BOF.

______

## Answer Key

**Self-Check**

1. **Inside the existing beacon process.** No new process means a much smaller footprint.
2. **Fork and run spawns a process, in-process runs in the beacon.** The latter is quieter.
3. **Aggressor scripts register the commands.** Without the .cna loaded, the command does not exist.
4. **A crash takes the beacon down.** A BOF shares the beacon's process.

**Exercise**

1. **A BOF, run in memory.**
2. **execute-assembly, fork and run.**
3. **Early Bird APC injection, shellcode into a fresh process.**

______

## Next Steps

You know how the beacon runs code. Next, how you shape the traffic it produces to avoid the most-signatured patterns in the field.

**[→ Module 7: Malleable C2 and Communication Evasion](/red-team-course/malleable-c2-and-communication-evasion/)**

Or return to the hub: **[Red Team Course](/red-team-course-start/)**
