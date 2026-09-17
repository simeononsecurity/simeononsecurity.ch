---
title: "Module 15: Persistence Cleanup and Defense Evasion"
date: 2026-09-12
toc: true
draft: false
description: "Remove the run key and binary cleanly with a query-remove-query loop, fix the SID trap when cleaning from SYSTEM, and blunt command-line detection."
genre: ["Red Team", "Offensive Security", "Persistence"]
tags: ["red team", "persistence cleanup", "reg_delete", "HKU", "SID", "wmi_query", "obfuscation", "defense evasion", "red team course"]
cover: "/img/cover/persistence-cleanup-defense-evasion-cybersecurity.webp"
coverAlt: "A digital illustration of a computer interface showing registry hives and file paths, highlighting actions for querying and removing persistence artifacts in a cybersecurity context."
coverCaption: "Module 15: leave the host free of your user-level artifacts."
---

#### [← Return to the Red Team Course](/red-team-course-start/)

**Once privileged persistence is in, the earlier user-level run key has done its job. Leaving it means extra evidence with no upside.** Two artifacts must go: the run key value in the user's registry hive, and the executable on disk.

*This module takes about 10 minutes.*

> **Why it matters:** Leftover artifacts are evidence with no upside. Query, remove, query is what lets you honestly mark a box clean.

______

## Key Terms

| Term | Plain meaning |
|------|---------------|
| **Query-remove-query** | the cleanup rhythm proving an artifact is gone |
| **SID** | the identifier naming each user's hive |
| **`HKU`** | the hive root holding each user's keys |
| **Access denied** | a file still held by a running process |
______

## Query, Remove, Query

Every cleanup follows the same rhythm. Query first to confirm the artifact and point at the right one. Remove it. Query again to prove it is gone. The second query is what lets you honestly mark it cleaned in your operational log.

```text
reg_query HKCU software\Microsoft\Windows\Currentversion\Run
reg_delete HKCU SOFTWARE\microsoft\windows\currentversion\run testValue
reg_query HKCU software\Microsoft\Windows\Currentversion\Run
```

Accurate cleanup logging feeds the final report and deconfliction. Mark the host free only after the confirming query returns empty.

______

## The SID Trap

If your session is a SYSTEM callback and you touch an `HKCU` path, you query the wrong hive. `HKCU` points to the current user's SID, and from a SYSTEM context the current user is SYSTEM. Your run key is not there, and you might wrongly think it is already gone.

Find the user's SID, then reference it under `HKU`:

```text
whoami
wmi_query "SELECT SID FROM Win32_UserAccount WHERE Name = 'target.user'"
```

From a SYSTEM session, swap `HKCU` for `HKU\<user-SID>` so you hit the user's hive instead of SYSTEM's. If you cannot recall the SID, run `reg_query HKU` to list every loaded hive. Domain SIDs are longer than local SIDs and do not carry `_Classes` in the name.

______

## Remove the Binary

Same query-remove-query rhythm for the file:

```text
ls C:\path\to\binary.exe
rm C:\path\to\binary.exe
ls C:\path\to\binary.exe
```

If `rm` returns access denied, the binary is still in use and calling back. Migrate or kill the Beacon before you retry. A file locked by a running process does not remove until the process lets go.

______

## Blunting Command-Line Detection

Command lines are one of the first things EDR inspects. Keep your process invocations quiet where possible, and prefer Beacon Object Files which run in memory over spawning host binaries. The fewer native tools you launch, the less defenders have to signature.

{{< youtube id="mej5L9PE1fs" >}}

Watch the technique explained: [Command-line obfuscation walkthrough](https://www.youtube.com/watch?v=mej5L9PE1fs)

> **Operator takeaway:** query, remove, query, every time, and log the result. The one thing which catches operators is running cleanup from SYSTEM and forgetting `HKCU` no longer means the user.

______

## Clean Your Trail

You must remove the run key and payload from a SYSTEM session. Decide:

1. What do you do before deleting anything?
2. Which prefix do you swap `HKCU` for?
3. How do you get the user's SID?
4. What does a failed `rm` warn about?

Answer from memory first. The explanations are in the Answer Key at the end.
______

## Why Cleanup Is Part of the Test

Cleanup proves whether the operator understood the artifact rather than relying on memory. Older operations often deleted the obvious file and missed registry hives, scheduled tasks, event records, or alternate user profiles. A before-and-after inventory makes those gaps measurable. **Never delete customer logs or evidence. Mark them for the report instead.**

______

## Common Mistakes

- Running cleanup from SYSTEM and touching `HKCU`, which resolves to the wrong hive.
- Removing the binary while it is still in use and calling back.
- Skipping the confirming query before marking the artifact cleaned.
- Keeping the user run key after privileged persistence replaced it.

______

## Self-Check

1. What is the query-remove-query rhythm?
2. Why does `HKCU` from SYSTEM hit the wrong hive?
3. How do you find the user's SID?
4. What does an access-denied on `rm` tell you?

______

## Answer Key

**Self-Check**

1. **Query, remove, query.** Confirm the artifact, delete it, then re-query to prove it is gone.
2. **HKCU resolves to the current user, and SYSTEM is the current user.** The pointer hits SYSTEM's hive, not the user's.
3. **With `whoami` or a WMI SID query**, then reference `HKU` by the SID.
4. **The binary is still in use and calling back.** Migrate or kill the beacon before retrying.

**Exercise**

1. **Query first** to confirm the artifact exists and you point at the right one.
2. **`HKU`** with the user's SID.
3. **`whoami`** or `wmi_query` on the account.
4. **A live process holds the file**, migrate or kill it first.
______

## Next Steps

User-level persistence is gone. Next, abuse domain trust to reach admin: Kerberoasting and domain privilege escalation.

**[→ Module 16: Domain Privilege Escalation and Kerberos Abuse](/red-team-course/domain-privilege-escalation-and-kerberos-abuse/)**

Or return to the hub: **[Red Team Course](/red-team-course-start/)**
