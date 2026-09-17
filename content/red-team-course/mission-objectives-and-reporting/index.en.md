---
title: "Module 20: Mission Objectives and Reporting"
date: 2026-09-12
toc: true
draft: false
description: "Turn a domain compromise into demonstrable impact by locating the objective, reaching Linux targets over port forwards, and closing out with a clean report."
genre: ["Red Team", "Offensive Security", "Reporting"]
tags: ["red team", "mission objective", "event log", "eventlog_query", "keylogger", "port forwarding", "SSH", "reporting", "red team course"]
cover: "/img/cover/cybersecurity-mission-objectives-network-analysis.webp"
coverAlt: "A cybersecurity professional operates a laptop in a dark, high-tech environment filled with glowing screens displaying network maps and code, emphasizing a modern and technical atmosphere."
coverCaption: "Module 20: prove impact against the thing which matters."
---

#### [← Return to the Red Team Course](/red-team-course-start/)

**The mission objective is the reason the customer hired you. Owning the domain proves your access, but the objective proves impact against something the customer cares about.** This module closes the loop from discovery to report.

*This module takes about 18 minutes.*

> **Why it matters:** Impact, not access, is what the customer pays for. Reaching the objective and documenting evidence and cleanup is the whole point.

______

## Key Terms

| Term | Plain meaning |
|------|---------------|
| **Mission objective** | the reason the customer hired the team |
| **Event ID** | the number naming a logged Windows event |
| **Keylogger** | the plugin capturing keystrokes from `explorer.exe` |
| **Port forward** | a tunnel hauling traffic through Beacon |
| **Report** | the deliverable listing impact and cleanup |
______

## What Objectives Look Like

Customers spell out objectives which fall into a few shapes:

- **Generate effects**, like taking down an external server to test failover speed.
- **Find specific files**, like changing a record on one person's workstation.
- **Reach specific systems**, like a Linux server storing customer data.

Each starts the same way: figure out where the thing lives, then which box you have to be on to touch it.

______

## Locate the Objective With ldapsearch

```text
ldapsearch "(name=*account*)" --attributes name samaccountname objectclass
ldapsearch "(description=*account*)" --attributes name samaccountname objectclass
```

Point these at names and descriptions to find the objects tied to the target function. Return `objectclass` so you see whether a hit is a user, group, or machine, which decides your next move.

______

## Find the Workstation

- **`ldapsearch`** on `description` or a custom last-logon attribute, when the org records who uses each box.
- **`eventlog_query`**, a BOF which reads logon events without touching `wevtutil.exe` on disk.
- **`net session`** on a file server, to tie a username to a machine IP through mapped drives.

______

## Windows Event Logs

| Event ID | Meaning |
|----------|---------|
| `4624` | successful logon |
| `4625` | failed logon |
| `4688` | process creation |
| `4740` | account lockout |

Use the BOF instead of `wevtutil.exe`:

```text
eventlog_query 4740 Administrator 5
eventlog_query 4624 target.user 10
```

`<eventid>` is required, `[username]` is optional, and `[count]` defaults to 10 when omitted.

______

## Locate Linux Targets

Linux boxes are usually not Active Directory objects, so find them indirectly:

- Identify the admin responsible for the server.
- `nmap` to fingerprint hosts and spot the non-Windows box.
- Dump DNS records for hostnames which never appear as AD computer objects.
- From the admin's box, run `ps` and `netstat` to spot a live SSH connection out to the server.

______

## Reach Linux: Keylog, then Forward

SSH needs cleartext credentials. Pass-the-hash does not work against Linux, and the SSH username is usually not an AD account, so domain credentials often will not work. Catch credentials three ways:

- Datamine the admin's workstation and shares.
- Keylog the admin's session with the `keylogger` plugin injected into `explorer.exe`.
- Check stored client configs and registry values.

Then bridge to the target with a port forward, because the Linux box sits inside the victim network with no direct route from yours:

```text
portfwd 192.168.1.45 1337
portfwd stop 1337
```

The first opens a tunnel on port `1337` through Beacon to the target. Then SSH to the team server on the port, and the connection is hauled through Beacon to the remote Linux host.

```text
keylogger
jobs
jobkill 0
```

`keylogger` runs in memory only, so a reboot stops it. `jobs` lists it, and `jobkill <n>` stops it.

______

## Report What You Did

A clean report is the deliverable which makes the operation land:

- Record the objective, the findings, and the evidence for each.
- List every credential, persistence artifact, and modified setting you touched.
- Confirm what you cleaned up and what you left in place.
- Note anything the customer should remediate, mapped back to the path you took.

> **Operator takeaway:** the objective tells you what to find, `ldapsearch` tells you which objects relate to it, logon and session data tell you which workstation to pivot to, and a port forward plus SSH gets you onto Linux targets with no direct route. Close it out with a report which captures impact, evidence, and cleanup.

______

## Prove the Impact

Close out the operation with impact and a report:

1. Which three objective shapes might the customer name?
2. How do you pin a user to their workstation?
3. How do you reach a Linux box with no direct route?
4. What does the final report list?

Answer from memory first. The explanations are in the Answer Key at the end.
______

## Why Reporting Matters

A technical action has value only when it answers the customer question and leaves reproducible evidence. Older reports listed tools and screenshots, while modern reports connect impact, control failure, timeline, and fix. A fictional objective with sanitized evidence gives analysts the same writing practice. **Remove secrets and unrelated personal data before delivery.**

______

## Common Mistakes

- Confusing access with impact, and reporting a foothold instead of the objective.
- Assuming pass-the-hash works against a Linux target.
- Keylogging the wrong process instead of `explorer.exe`.
- Omitting cleanup and touch inventory from the report.

______

## Self-Check

1. Name the three kinds of mission objective.
2. Which event ID marks a successful logon?
3. Why does reaching a Linux box need cleartext credentials?
4. What does `portfwd` bridge?

______

## Answer Key

**Self-Check**

1. **Network effects, specific information, demonstrated impact.** The three shapes of an objective.
2. **4624.** Successful logon.
3. **Pass-the-hash does not work on Linux.** SSH needs a cleartext password or key.
4. **Your attack machine to the LAN target**, tunnelling traffic through Beacon.

**Exercise**

1. **Effects, files, or systems.** Take down a server, change a record, or reach a Linux box.
2. **`eventlog_query` for 4624**, or `net session` on a file server.
3. **`portfwd` then SSH**, through the team server.
4. **The objective, findings, evidence, credentials touched, and cleanup.**
______

## Course Complete

You started with the operating methodology and finished by carrying a full operation through post exploitation to a real objective. Prepare, recon, exploit, persist, expand, act on the objective. The methodology carries forward even as the tools change.

**[→ Return to the Red Team Course hub](/red-team-course-start/)**
