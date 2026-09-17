---
title: "Module 5: Command and Control Operations"
date: 2026-09-12
toc: true
draft: false
description: "How command and control works with Cobalt Strike: the team server, client, and beacon, asynchronous check-ins, sleep time, and the listener workflow."
genre: ["Red Team", "Offensive Security", "Command and Control"]
tags: ["red team", "command and control", "Cobalt Strike", "C2", "team server", "beacon", "listener", "asynchronous C2", "red team course"]
cover: "/img/cover/command-and-control-operations-cybersecurity.webp"
coverAlt: "An illustration showing three components of command and control operations: a secure fortress as the team server, a high-tech console as the client, and a glowing implant representing the beacon, all against a dark background."
coverCaption: "Module 5: the flow from beacon to team server."
---

#### [← Return to the Red Team Course](/red-team-course-start/)

**Command and control is how you drive an implant after it lands.** Cobalt Strike splits this across three components, and keeping them straight makes everything downstream clearer.

*This module takes about 12 minutes.*

______

## Key Terms

| Term | Plain meaning |
|------|---------------|
| **Team server** | the shared backend holding the operation's data |
| **Client** | your window into the team server |
| **Beacon** | the implant running on the target |
| **Listener** | the named transport tying a beacon to its traffic |
| **Sleep time** | the gap between a beacon's check-ins |
| **Redirector** | the outside host which forwards beacon traffic |

______

## The Three Components

Cobalt Strike is the remote access tool this course uses for command and control:

| Component | Role |
|-----------|------|
| **Team Server** | the central server holding the operation |
| **Client** | what you run to connect and issue commands |
| **Beacon** | the implant running on the target |

Logs, screenshots, downloads, and keylogs land on the team server. Most are reachable through the client interface.

______

## Asynchronous C2 and Why It Hides

The beacon does not hold an open connection. It makes an outbound request on a schedule, asks for new instructions, then goes quiet. The request is shaped to look like a normal web request.

The connection originates from the target, so it reads like a workstation browsing a website, not an external attacker reaching in.

The gap between check-ins is the **sleep time**:

| Sleep time | Result |
|------------|--------|
| Longer | quieter, slower to respond |
| Shorter | more responsive, noisier |

Tune this trade-off constantly.

______

## The Basic Workflow

The standard startup sequence, in order:

1. Start the **team server**, giving it an address and a password, plus an optional Malleable profile and kill date.
2. Start the **client** and connect to the team server with the shared password.
3. Create a **listener**, naming it after the redirector domain and transport, for example `mydomain.com_HTTPS`.
4. Confirm traffic to the redirector forwards back to the team server.
5. Browse the redirector and create a test implant to prove the full chain.
6. Load any extension scripts for additional tools.

```text
./teamserver <team-server-ip> <password> [c2-profile] [kill-date]
```

*The client runs from its own directory because it depends on relative paths.*

______

## The Team Server and the Client

The **team server** is the shared backend for the whole operation. Logging, downloads, and screenshots all land there, so it is also the record deconfliction and reporting depend on.

The **client** is your window into the team server. Multiple operators connect to the same team server at once, which is what makes this a team tool. From the client you drive beacons, create listeners, and read logs.

______

## How the Pieces Connect

End to end: the beacon on the target calls out through a redirector, the redirector forwards traffic to the team server, and you interact through the client. The listener, named after the redirector domain, ties a given beacon's traffic to the right transport.

> **Operator takeaway:** three components, one flow. Beacon calls out, redirector forwards, team server holds the operation, client drives it. Asynchronous check-ins over shaped HTTPS are what let the traffic pass as ordinary browsing.

______

## Stand Up Your Own C2

Describe the startup sequence for a fresh operation:

1. What values does `./teamserver` take, in order?
2. What do you create after the client connects?
3. How do you prove the full beacon-to-server chain works?
4. Which sleep time do you pick for a quiet operation?

Answer from memory first. The explanations are in the Answer Key at the end.

______

## Common Mistakes

- Naming the listener after something other than the redirector domain, so mapping gets muddled.
- Forgetting the client depends on relative paths, then launching it from the wrong directory.
- Setting sleep too short on a quiet operation and lighting up the traffic.
- Assuming the team server is reachable without testing the full beacon-to-server chain.

______

## Self-Check

1. Name the three Cobalt Strike components and their roles.
2. Why is asynchronous C2 stealthier than a held-open connection?
3. What does a longer sleep time cost you?
4. In what order do you start the team server, client, and listener?

______

## Answer Key

**Self-Check**

1. **Team server holds the operation, the client drives it, the beacon runs on target.**
2. **It connects, exchanges, and disconnects.** A held-open connection is what monitoring catches.
3. **It trades responsiveness for quiet.** Longer sleep means slower commands but less traffic.
4. **Team server, then client, then listener.**

**Exercise**

1. **Address, password, optional profile, optional kill date.**
2. **A listener named after the redirector domain and transport.**
3. **Browse the redirector and drop a test implant.**
4. **A long sleep for a quiet operation.**

______

## Next Steps

Command and control is up. Next: running payloads on the beacon, and extending it with Beacon Object Files.

**[→ Module 6: Beacon Execution and BOFs](/red-team-course/beacon-execution-and-beacon-object-files/)**

Or return to the hub: **[Red Team Course](/red-team-course-start/)**
