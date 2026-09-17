---
title: "Module 14: Privileged Persistence and Process Migration"
date: 2026-09-12
toc: true
draft: false
description: "Install a Windows service which launches your implant as SYSTEM, migrate off rundll32, and keep the binpath valid by matching process architecture first."
genre: ["Red Team", "Offensive Security", "Persistence"]
tags: ["red team", "privileged persistence", "service", "sc.exe", "sc_create", "process migration", "sysnative", "inject", "red team course"]
cover: "/img/cover/windows-service-architecture-privileged-persistence-process-migration.webp"
coverAlt: "A digital illustration showing a Windows service architecture with vibrant colors, depicting a central service running in the background and pathways indicating process migration, all against a dark navy background."
coverCaption: "Module 14: SYSTEM-level persistence which outlives the session."
---

#### [← Return to the Red Team Course](/red-team-course-start/)

**Privileged persistence is a Windows service running as SYSTEM. A service starts at boot, before anyone logs in, and runs at the highest privilege on the box.** This is the persistence you want once you hold admin.

*This module takes about 14 minutes.*

> **Why it matters:** A service survives boot as SYSTEM before anyone logs in. Matching architecture and restoring the binpath keep it alive and clean.

______

## Key Terms

| Term | Plain meaning |
|------|---------------|
| **Service persistence** | an implant launched at boot as SYSTEM |
| **Windows Service EXE** | the payload speaking the SCM protocol |
| **`sysnative`** | the keyword cancelling 32-bit redirection |
| **Process migration** | moving the beacon into a clean process |
| **`sc_qc`** | the query returning a service's binpath |
______

## Where It Fits

Post exploitation breaks into five phases: user persistence, privilege escalation, privileged persistence, expanding access to the domain controller, and fortifying access. User persistence lived in a run key under the current user. Privileged persistence means a service. Other methods exist, but the service pattern is the one to learn first.

______

## Match Architecture Before You Touch sc.exe

Your service launches a Cobalt Strike executable, which must match the target architecture. Confirm what your Beacon runs as:

| Current process | Spawn path | Next step |
|-----------------|------------|-----------|
| **x64** | `C:\Windows\System32\` | install the service directly |
| **x86 on 64-bit host** | `C:\Windows\Sysnative\` | migrate, then install |

The reason is filesystem redirection. A 32-bit process asking for `System32` gets silently redirected to `SysWOW64`, so a beacon dropped there lands in the wrong folder and the service binpath points at nothing.

______

## Process Migration Workflow

When running as x86 on a 64-bit host:

```text
execute C:\Windows\Sysnative\upnpcont.exe
ps
inject PID x64 <listener>
kill <old-pid>
```

`Sysnative` is not a real directory. It is a hint telling Windows not to redirect the call into `SysWOW64`. Use `ps` to find the fresh process PID, then `inject` a matching Beacon into it.

______

## Safe Processes to Spawn

Migration is a tradeoff. Injecting into a live customer process blends in but drags a legitimate app down if Beacon hangs. Spawning your own disposable Windows process is the safer default:

- `C:\Windows\System32\upnpcont.exe`
- `C:\Windows\System32\rdpclip.exe`
- `C:\Windows\System32\logagent.exe`

Use `System32` when your process is x64, and `Sysnative` when it is x86.

______

## Create the Service

The Service Control tool `sc.exe` creates, queries, changes, and deletes services. It needs admin, which you already hold.

| Action | Native sc.exe | BOF |
|--------|---------------|-----|
| Query state | `sc.exe query <name>` | `sc_query vss` |
| Query config | `sc.exe qc <name>` | `sc_qc vss` |
| Start | `sc.exe start <name>` | `sc_start vss` |
| Stop | `sc.exe stop <name>` | `sc_stop vss` |
| Delete | `sc.exe delete <name>` | `sc_delete <name>` |
| Set description | `sc.exe description <name> "..."` | `sc_description <name> <desc>` |
| Create | `sc.exe create <name> ...` | `sc_create <name> <display> <binpath> <desc> <errmode> <startmode>` |

Build the payload as the Cobalt Strike **Windows Service EXE**, not a plain executable. A normal EXE does not speak the Service Control Manager protocol, so Windows times out and marks the launch failed.

______

## The Stopped Service Is Success

After you start the service it shows as stopped. This is expected. Windows starts the service EXE, which kicks off the Beacon, and once the Beacon runs the service stops itself while Beacon keeps running in its own process. A stopped service with a live callback is a success, not a failure.

Name and describe the service to blend in. Dozens of legitimate services already run, so one more with a credible description rarely stands out.

______

## Migrate Off rundll32

When the service launches, it runs `rundll32.exe` and injects Beacon into it, so `rundll32.exe` is the process calling out. Defenders signature it on sight, and a persistent callback tied to it is a liability. Migrate again with `inject`, this time into one of the safe process names above.

______

## Other Persistence Methods

Services are the pattern to learn, but not the only lever. WMI event subscriptions and process-list persistence extend the same idea without a service start event:

{{< youtube id="0SjMgnGwpq8" >}}

Watch how each persistence path works:

- [WMI event subscription persistence](https://www.youtube.com/watch?v=0SjMgnGwpq8)
- [Trust provider hijacking](https://www.youtube.com/watch?v=wxmxxgL6Nz8)
- [AddMonitor process persistence](https://www.youtube.com/watch?v=dq2Hv7J9fvk)

> **Operator takeaway:** build the Windows Service EXE, create the service with a blended name, expect it to read stopped after Beacon starts, then migrate off `rundll32.exe` immediately. Learn the service method first, then extend to WMI and process-list variants when the situation calls for it.

______

## Persist as SYSTEM

You hold admin and need SYSTEM persistence. Decide:

1. What do you build the payload as, and why?
2. Which command creates the service?
3. After the beacon starts, why does the service read stopped?
4. What do you do right after the callback arrives?

Answer from memory first. The explanations are in the Answer Key at the end.
______

## Why Privileged Persistence Is Risky

A service or migrated process gains durability through trusted operating-system behavior, which also gives defenders strong service, token, and process telemetry. Older service abuse ignored rollback, while current lab work records the original configuration before testing. A signed benign service and a documented process move demonstrate the evidence safely. **Restore the service and terminate the test process before leaving the VM.**

______

## Common Mistakes

- Installing the service from a 32-bit process and pointing the binpath at `SysWOW64`.
- Building the payload as a plain EXE instead of the Windows Service EXE.
- Forgetting to restore the original binpath after borrowing a service.
- Leaving the callback on `rundll32.exe` after the service starts.

______

## Self-Check

1. Why migrate out of a 32-bit process before installing the service?
2. Name two safe Windows processes to spawn for migration.
3. Why does a stopped service with a live callback mean success?
4. What does `sc_qc` show you?

______

## Answer Key

**Self-Check**

1. **Redirection sends `system32` writes to SysWOW64**, so the service binpath points at nothing.
2. **`upnpcont.exe`, `rdpclip.exe`, or `logagent.exe`.** Safe, windowless hosts.
3. **The service stops itself once the beacon runs.** A stopped service with a live callback is the expected state.
4. **The binpath and the account.** `sc_qc` confirms what the service runs and as whom.

**Exercise**

1. **The Windows Service EXE**, a plain EXE fails the Service Control Manager handshake.
2. **`sc_create`** with a display name, binpath, and description.
3. **It starts the beacon then stops itself** while the beacon keeps running.
4. **Migrate off `rundll32.exe`** into a safe process.
______

## Next Steps

Your foothold now survives as SYSTEM. Later you remove the earlier user-level run key so it stops being extra evidence on the host.

**[→ Module 15: Persistence Cleanup and Defense Evasion](/red-team-course/persistence-cleanup-and-defense-evasion/)**

Or return to the hub: **[Red Team Course](/red-team-course-start/)**
