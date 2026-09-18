---
title: "Module 11: Situational Awareness and Host Operations"
date: 2026-09-12
lastmod: 2026-09-17
toc: true
draft: false
description: "Build a current host-state record using Windows and Linux identity, process, socket, and routing evidence, with a worked snapshot comparison."
genre: ["Red Team", "Offensive Security", "Post Exploitation"]
tags: ["red team", "situational awareness", "post exploitation", "ipconfig", "netstat", "tasklist", "hashdump", "logonpasswords", "uname", "red team course"]
cover: "/img/cover/situational-awareness-post-exploitation-techniques.webp"
coverAlt: "A cybersecurity professional in a dark workspace is analyzing multiple computer screens showing network maps and system statistics, surrounded by data visualizations in vibrant colors."
coverCaption: "Module 11: identify the host context and know when observations become stale."
---

#### [← Return to the Red Team Course](/red-team-course-start/)

**Situational awareness** is a current, evidence-backed picture of the host and security context where an assessment action would run. It starts with identity and scope, then adds the process, network, and service facts needed for the next decision. Collecting every available field is less useful than answering the right questions accurately.

*Allow about 18 minutes, plus time to create the host-state record. Commands below inspect local state and do not require credential extraction.*

## What You Will Learn

- **Identify** the host, account, process, and network context separately.
- **Explain** why an interface address does not establish a usable route.
- **Apply** read-only Windows or Linux checks in a training environment.
- **Analyze** changes between two host snapshots.
- **Create** a handover record with freshness and collection limits.

| Term | Meaning |
|---|---|
| **Host identity** | Evidence tying the current system to an approved asset |
| **Security context** | Identity and permissions used by the current process or thread |
| **PID** | Process identifier, valid within its host and lifetime |
| **Listener** | Socket accepting incoming communication |
| **Route** | Rule selecting how traffic reaches a destination |
| **Snapshot** | Observations collected during a stated time window |

## Establish Identity Before Interpretation

**A hostname or IP address** is one part of an identity check. Match it against the approved inventory and available asset identifiers. DHCP changes, aliases, cloned lab systems, and virtual interfaces make a single label insufficient in some environments.

**The account context** is a separate fact. A visible desktop user, a remote session's user, and a service account need not be the same principal. Reuse the SID and token distinctions from [Module 4](/red-team-course/foundations-windows-internals-and-authentication/) before interpreting access results.

**Freshness** belongs beside each observation. A process list gathered before a service restart does not describe the replacement process. Record the collection window and repeat only the checks invalidated by a relevant state change.

| Question | Evidence | Common shortcut to avoid |
|---|---|---|
| **Which host?** | Inventory match plus local identifiers | One familiar name |
| **Which account?** | Current identity and authority | Visible desktop owner |
| **Which process?** | PID, image, start time, and context | Process filename alone |
| **When observed?** | Timestamp and collection window | Undated pasted output |

## Build a Minimal Snapshot

**Choose fields by purpose.** Before a local configuration check, you need the current account and target object's context. Before interpreting an outbound connection, you need the source process, route, destination, and relevant time. These questions call for different snapshots.

**Collection itself is activity.** Native commands, scripts, and in-process extensions differ in implementation, but all require evidence appropriate to their behavior. Avoid assuming a BOF is automatically quiet or a built-in executable automatically safe for any workload.

**Missing information** should stay visible. Permissions, process termination, tool filtering, and collection failures all affect completeness. Record “not collected” or “access denied” when appropriate rather than replacing uncertainty with an empty field.

{{< figure src="host-identity-process-network-snapshot.webp" alt="Four boxes organize host identity, security context, process and socket observations, and a time-bounded operator decision" caption="Refresh the fields affected by a change before relying on the snapshot" >}}

## Inspect Windows Identity

**Start with local identity** in a Windows training shell. **`hostname`** prints the computer name, **`whoami /user`** includes the current user SID, and **`whoami /groups`** shows group information for the current context. Compare the result with the approved inventory and account. [Read the whoami reference](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/whoami).

```text
hostname
whoami /user
whoami /groups
ipconfig /all
```

**`ipconfig /all`** displays detailed adapter configuration. Read the adapter names, addresses, masks, gateways, and DNS settings together. An address alone does not prove a network is reachable or in scope. [Read the ipconfig reference](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/ipconfig).

**Identity and network fields** need separate interpretation. A domain account does not establish organizational ownership of every listed network. A successful local identity query also does not establish the account's permissions on a remote resource.

| Output field | Use in the snapshot |
|---|---|
| **Computer name** | Correlation with approved asset records |
| **Account SID** | Stable identity reference within its authority |
| **Group state** | Context for later permission interpretation |
| **Adapter and gateway** | Starting point for route analysis |

## Correlate Processes and Sockets

**Process and connection lists** provide complementary observations. **`tasklist /v`** adds verbose process information, while **`netstat -ano`** displays connections and listeners numerically with associated PIDs. Read both during a short collection window. [Read tasklist](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/tasklist) and [netstat](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/netstat).

```text
tasklist /v
netstat -ano
```

**Flag meanings:** **`/v`** requests verbose task information. For netstat, **`-a`** includes connections and listening endpoints, **`-n`** keeps numeric addresses and ports, and **`-o`** includes the owning PID. These flags inspect state rather than proving application purpose.

**PID correlation has a time boundary.** A process might exit between commands, and a later process might reuse its identifier. Include image path and start-time evidence where available before joining records from distant timestamps.

| Socket observation | Interpretation limit |
|---|---|
| **Loopback listener** | Local binding does not establish remote exposure |
| **Wildcard listener** | Listening scope does not prove firewall permission |
| **Established connection** | Connection state does not establish authorized application behavior |
| **PID match** | Correlate within the correct host and process lifetime |

## Use Process Explorer Carefully

**Process Explorer** adds an interactive view of running processes, handles, DLLs, and mapped files. Its lower-pane modes help connect a selected process with resources it has opened. Use this to investigate a specific question rather than treating a large tree as a conclusion. [Read Microsoft's Process Explorer overview](https://learn.microsoft.com/en-us/sysinternals/downloads/process-explorer).

**A useful observation** includes the selected process, timestamp, relevant properties, and what the view establishes. An image with a familiar name still needs context such as path, signer information, parentage, and behavior. A signature is evidence about provenance, not a blanket approval of every action.

**Pavel Yosifovich's demonstration** explains Process Explorer features in Microsoft's Sysinternals series. Watch for the distinction between process identity and loaded resources. Then choose one view which would improve your own host-state record.

{{< youtube id="ZqZvzA4OGDA" enable="true" title="Sysinternals: Process Explorer deep dive (demo) | ProcExp, DLL, Windows | Microsoft" >}}

**Watch on YouTube:** [Sysinternals: Process Explorer deep dive](https://www.youtube.com/watch?v=ZqZvzA4OGDA).

## Inspect Linux Context

**Kernel and distribution identity** answer different questions. **`uname -a`** reports kernel and machine information, while **`/etc/os-release`** provides distribution identification fields on systems implementing this interface. Neither replaces a package inventory or patch assessment. [Read uname](https://man7.org/linux/man-pages/man1/uname.1.html) and [os-release](https://man7.org/linux/man-pages/man5/os-release.5.html).

```bash
id
uname -a
cat /etc/os-release
ip address show
ip route show
ss -lnt
```

**`id`** reports user and group identity for the invoking context. **`ip address show`** lists address assignments, and **`ip route show`** displays routes in the default listing context. More complex policy routing requires additional interpretation beyond this initial view. [Read the address](https://man7.org/linux/man-pages/man8/ip-address.8.html) and [route](https://man7.org/linux/man-pages/man8/ip-route.8.html) references.

**`ss -lnt`** displays listening TCP sockets using numeric values. **`-l`** selects listeners, **`-n`** avoids service-name resolution, and **`-t`** selects TCP. Add process information only when needed and available under the current permissions. [Read the ss reference](https://man7.org/linux/man-pages/man8/ss.8.html).

| Linux evidence | Useful distinction |
|---|---|
| **User and groups** | Current identity versus another logged-in session |
| **Kernel release** | Kernel information versus distribution branding |
| **Addresses** | Assigned interfaces versus reachable destinations |
| **Routes** | Selected forwarding path versus permitted application access |
| **Listening socket** | Bound endpoint versus an external reachability result |

## Avoid the Two-Address Shortcut

**Multiple addresses** do not automatically make a host a bridge into another network. One interface might have several addresses, a VPN might contribute a route, or a virtual interface might belong to a local container network. Identify the interface type and routing context before drawing a topology conclusion.

**Forwarding** is another condition. A host having interfaces on two networks does not establish forwarding between them. Routes, forwarding settings, firewall policy, and application behavior determine which communication is possible.

**Authorization remains independent.** Learning about another network does not make it part of the assessment. Record the relationship as an unresolved topology observation and ask the agreed owner to confirm the permitted next step.

| Observation | Follow-up question |
|---|---|
| **Second address** | Same interface, different interface, or virtual endpoint? |
| **Additional route** | Which destinations and policy context use it? |
| **Two connected networks** | Is forwarding enabled and permitted? |
| **New reachable service** | Is the asset and proposed action in scope? |

## Work a Snapshot Difference

**Illustrative scenario:** at 09:00, PID 4200 runs the approved training service and listens on loopback port 8765. At 09:10, PID 4200 belongs to a different program, while the training service has PID 6100. Its replacement listener binds to all IPv4 interfaces.

**Analyze the change:** identify which old observations are stale and which new exposure question needs validation. Decide whether the PID reuse proves the original process changed its identity. Keep process lifetime and socket binding separate in your answer.

**Expected reasoning:** the 09:00 PID-to-process association is stale. The new program's reuse of PID 4200 does not make it the same process. The binding change warrants a scoped reachability review, but it does not prove the service is reachable through every firewall or network path.

| Evidence needed | Purpose |
|---|---|
| **Process start times** | Distinguish old and replacement processes |
| **Image and service association** | Identify the new service instance |
| **Current socket binding** | Confirm the changed local endpoint |
| **Approved external check** | Determine reachability from the relevant source |

## Keep Privilege Claims Precise

**Elevated privileges** affect available operations but do not prove any particular credential material is present. Authentication method, logon state, operating-system protections, and configuration all matter. Microsoft's Credential Guard documentation describes isolation of certain secrets using virtualization-based security. [Read the Credential Guard overview](https://learn.microsoft.com/en-us/windows/security/identity-protection/credential-guard/).

**Credential extraction** is a separate assessment action, not a required step in a basic host snapshot. A host-awareness objective is often satisfied by identity, process, network, and service observations. Keep the collected fields tied to the actual decision.

**Read-only does not mean free of effects.** An expansive query still consumes resources and produces activity. Bound repeated collection by need, particularly on systems with strict availability requirements.

| Claim | More precise record |
|---|---|
| **“Administrator means all secrets available”** | Current privileges observed, credential availability untested |
| **“No output means no process”** | Query returned no record under the stated context |
| **“Two addresses mean a pivot”** | Additional address observed, route and permission unresolved |

## Create a Host-State Record

**Your deliverable** is a concise snapshot for one disposable Windows or Linux system. Collect the smallest set of fields needed to explain its identity, current context, one process, and one socket. Include an explicit freshness limit or event which would invalidate the record.

```text
Approved asset and inventory reference:
Collection start/end time:
Host and account identity:
Current process architecture and security context:
Relevant process PID, image, and start time:
Relevant adapter, route, and socket:
Command or tool version:
Raw output location:
Missing fields or access limitations:
Change which requires a refresh:
Supported next action:
```

**Review the record** by handing it to another reader. They should identify what is known, which facts are time-sensitive, and what remains untested. Avoid turning a snapshot into a permanent description of the host.

## Check Your Understanding

1. **Identity:** why is a hostname insufficient in some environments?
2. **Processes:** what makes a PID-only correlation unreliable over time?
3. **Networks:** why do two addresses fail to prove forwarding?
4. **Linux:** which source distinguishes distribution identity from kernel information?

| Question | Expected reasoning |
|---|---|
| **Identity** | Names, aliases, and cloned systems require inventory correlation |
| **Processes** | PIDs are reused after process exit |
| **Networks** | Address assignment, routing, forwarding, and policy are separate conditions |
| **Linux** | os-release provides distribution identification fields |

## Next Steps

**User persistence** introduces changes whose trigger, identity, and removal need separate evidence. Continue to [Module 12: User Persistence](/red-team-course/user-persistence/) to examine the lifecycle of a user-context startup entry. Return to the [Red Team Course hub](/red-team-course-start/) for the full sequence.
