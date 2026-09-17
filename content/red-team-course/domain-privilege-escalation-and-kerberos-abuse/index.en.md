---
title: "Module 16: Domain Privilege Escalation and Kerberos Abuse"
date: 2026-09-12
toc: true
draft: false
description: "Map who holds domain power, mine readable shares for credentials, then request and crack service tickets with Kerberoasting, plus RBCD, DNSAdmins, and DCShadow."
genre: ["Red Team", "Offensive Security", "Active Directory", "Kerberos"]
tags: ["red team", "kerberoasting", "Kerberos", "SPN", "TGS", "hashcat", "domain admins", "RBCD", "DNSAdmins", "DCShadow", "red team course"]
cover: "/img/cover/kerberoasting-domain-privilege-escalation-cyber-security.webp"
coverAlt: "An illustration of a dark server room with a glowing network diagram. Nodes represent users and service accounts, with a highlighted path showing the flow of Kerberos ticket exchange."
coverCaption: "Module 16: turn a normal user into domain privilege."
---

#### [← Return to the Red Team Course](/red-team-course-start/)

**Kerberoasting is the quiet road from a normal domain user to a valuable service account.** Any authenticated user requests a service ticket, take it offline, and crack it. The loud part never touches the network.

*This module takes about 18 minutes.*

______

## Key Terms

| Term | Plain meaning |
|------|---------------|
| **KDC** | the trusted third party issuing tickets |
| **TGS** | the service ticket you roast |
| **SPN** | the name marking an account as roastable |
| **Kerberoasting** | requesting and cracking a service ticket |
| **RBCD** | resource-based constrained delegation |
______

## Enumerate Who Holds Power

Before you roast anything, map the people and groups which matter:

| Goal | Native net.exe | BOF / plugin |
|------|----------------|--------------|
| List domain groups | `net group /domain` | `netGroupList` |
| Group members | `net group "domain admins" /domain` | `netGroupListMembers "domain admins"` |
| Local admins | `net localgroup administrators` | `netLocalGroupList` |
| User detail | `net user <name> /domain` | `netuser <name> <domain>` |
| Remote shares | `net view \<host> /all` | `netshares <host>` |
| Connections | `net use` | `netuse_list` |

Chase nested groups. A user who is not directly in `Domain Admins` still inherits it through a chain of memberships, and the indirect path is often the cleanest route up.

______

## Datamine First

Read what you already have access to before any exploit:

- Documents, Downloads, Desktop, and Recent Documents on the user folders.
- `C:\` setup scripts and `C:\Windows\Temp` log files.
- File servers and home directory shares on `net user` output.
- Password files named `pass.txt`, `password.txt`, or `key.txt`, and scripts with hardcoded credentials.

Datamining is the quietest escalation there is. Exhaust it before you touch an exploit.

______

## What Kerberos Is

Kerberos is the authentication protocol Active Directory uses. A handful of components exchange encrypted keys:

| Piece | Role |
|-------|------|
| **KDC** | trusted third party on the domain controller |
| **TGT** | ticket proving you authenticated, encrypted with the KDC key |
| **TGS** | the ticket you Kerberoast, encrypted with the service account hash |
| **SPN** | Service Principal Name which marks an account as roastable |
| **NTLM hash** | the service account key, your crack target |

Kerberos never sends a password over the network. It sends encrypted tickets instead, so most attacks impersonate a component and get the KDC to hand over tickets rather than attacking the crypto.

______

## Kerberoasting

The weakness is step four of the flow. Any domain-authenticated user requests a TGS for any account with an SPN attached, and the KDC does not check whether you should have access to the service. It encrypts a ticket with the service account's NTLM hash and hands it over.

Then you crack it offline:

```text
hashcat -m 13100 ticket.hash wordlist.txt
```

Service accounts are frequently over-privileged, so one cracked SPN hands you a large jump in access. The request and the crack happen off the domain controller, so the brute force never touches the target network.

{{< youtube id="nJSMJyRNvlM" >}}

Watch the technique: [Kerberoasting walkthrough](https://www.youtube.com/watch?v=nJSMJyRNvlM)

______

## Beyond Kerberoasting

Once you hold privileged tickets or admin rights, several follow-on abuses extend your reach:

- **Resource-based constrained delegation (RBCD)** lets you configure a service to impersonate users on your behalf.
- **DNSAdmins to SYSTEM** abuses DNS managers to load an attacker DLL into the DNS service.
- **DCShadow** plants a rogue domain controller to write directly to Active Directory replication.

{{< youtube id="RUbADHcBLKg" >}}
{{< youtube id="8KJebvmd1Fk" >}}
{{< youtube id="KILnU4FhQbc" >}}

- [Resource-based constrained delegation](https://www.youtube.com/watch?v=RUbADHcBLKg)
- [DNSAdmins to SYSTEM](https://www.youtube.com/watch?v=8KJebvmd1Fk)
- [DCShadow](https://www.youtube.com/watch?v=KILnU4FhQbc)
- [Detecting DCShadow](https://www.youtube.com/watch?v=yWFUKwZaT_4)

> **Operator takeaway:** find a service account with an SPN, request its TGS as any domain user, extract the ticket, and crack it offline with `hashcat`. The domain controller willingly gives you the ticket, so the whole thing is quiet until you crack.

______

## Roast a Service Account

Walk a Kerberoast from a normal domain user to a cracked ticket:

1. What do you enumerate before roasting?
2. Which ticket do you request, and from where?
3. What do you do with the ticket offline?
4. What raises your odds of a crack?

Answer from memory first. The explanations are in the Answer Key at the end.
______

## Common Mistakes

- Roasting before enumerating groups, so you chase the wrong accounts.
- Expecting a crack from a strong service password.
- Skipping datamining and reaching for the loud option first.
- Treating the SPN-tied account as the target instead of the over-privilege it reaches.

______

## Self-Check

1. Which Kerberos step lets any domain user request a service ticket?
2. Which component encrypts the roastable ticket?
3. What does `hashcat -m 13100` do?
4. Name two abuses beyond Kerberoasting.

______

## Answer Key

**Self-Check**

1. **Step four, the TGS exchange.** Any authenticated user requests a ticket for any SPN-tied account.
2. **The service account's NTLM hash** encrypts the TGS, so it is the crack target.
3. **It cracks the ticket offline.** Mode 13100 handles Kerberoast tickets.
4. **RBCD, DNSAdmins to SYSTEM, DCShadow, and more** extend reach beyond the roast.

**Exercise**

1. **Groups and administrators**, with `netGroupListMembers` and local admin reads.
2. **A TGS for an SPN-tied account**, requested as a normal domain user.
3. **Crack it with `hashcat -m 13100`** offline.
4. **A weak service password**, the only target worth roasting.
______

## Next Steps

You hold domain credentials and the map of who is where. Next, use those to move across the domain and reach more hosts.

**[→ Module 17: Lateral Movement and Expanding Access](/red-team-course/lateral-movement-and-expanding-access/)**

Or return to the hub: **[Red Team Course](/red-team-course-start/)**
