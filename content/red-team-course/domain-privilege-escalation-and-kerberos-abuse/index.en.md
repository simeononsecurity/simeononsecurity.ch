---
title: "Module 16: Domain Privilege Escalation and Kerberos Abuse"
date: 2026-09-12
lastmod: 2026-09-17
toc: true
draft: false
description: "Analyze Kerberos service-ticket exposure, account privilege, encryption choices, and delegation evidence with a domain escalation review record."
genre: ["Red Team", "Offensive Security", "Active Directory", "Kerberos"]
tags: ["red team", "kerberoasting", "Kerberos", "SPN", "TGS", "gMSA", "delegation", "red team course"]
cover: "/img/cover/kerberoasting-domain-privilege-escalation-cyber-security.webp"
coverAlt: "An illustration of a dark server room with a glowing network diagram. Nodes represent users and service accounts, with a highlighted path showing the flow of Kerberos ticket exchange."
coverCaption: "Module 16: separate ticket exposure from account authority"
---

#### [← Return to the Red Team Course](/red-team-course-start/)

**Domain privilege escalation** combines identity, ticket, directory, and authorization evidence. Kerberoasting is one possible path. A service principal name (SPN) identifies a service account for Kerberos, but it does not grant administrative authority to the account.

This module builds a **ticket and privilege review**. You will distinguish a ticket request from offline password analysis, compare service-account designs, and produce a defensible decision about the next approved test.

*Allow 40–55 minutes. Difficulty: intermediate. Examples use synthetic account names and expected evidence.*

## Learning Outcomes

- **Define** KDC, TGT, TGS, SPN, service account, and delegation.
- **Explain** why ticket encryption and account privilege are separate questions.
- **Inspect** ticket-cache and directory evidence in an approved lab.
- **Compare** traditional service accounts with managed service accounts.
- **Create** a domain escalation review with evidence and limits.

## Before You Begin

Use the **domain lab and collection agreement** from [networking and Active Directory](/red-team-course/foundations-networking-and-active-directory/). Record the requesting principal, domain controller, account names, SPNs, encryption types, and the purpose of each service. Do not request tickets for customer accounts outside the approved scope.

| Record | Why it matters |
|---|---|
| **Requesting identity** | Attributes the ticket request to a real principal |
| **Service account** | Separates SPN ownership from authorization |
| **Encryption type** | Determines which analysis paths are relevant |
| **Group membership** | Establishes potential impact after authentication |
| **Collection window** | Connects directory and controller evidence |

## Map Kerberos Roles

{{< figure src="kerberos-ticket-exposure-and-impact.webp" alt="A Kerberos flow separates ticket request, encryption evidence, account authority, and service authorization" caption="Ticket exposure and account impact require separate evidence" >}}

**Kerberos** uses a key distribution center (KDC) to issue tickets. A **ticket-granting ticket (TGT)** represents an authenticated session. A **ticket-granting service ticket (TGS)** authorizes access to a named service and is issued for an SPN.

| Component | Role | Does it prove privilege? |
|---|---|---|
| **KDC** | Issues tickets for the domain | No |
| **TGT** | Requests later service tickets | No |
| **TGS** | Targets one service SPN | No |
| **SPN** | Maps a service name to an account | No |
| **Group membership** | Contributes to authorization | Sometimes, after policy evaluation |

An SPN is a **directory mapping**, not an access-control decision. A service account might have no elevated groups, or it might run a critical application with delegated rights. Review both the account and the service it supports.

## Separate Request and Crack

**Kerberoasting** describes requesting service tickets for SPN-associated accounts and analyzing the ticket material offline. The KDC request is a network event. The password-guessing phase runs against a captured representation and does not contact the KDC for each guess.

An **offline result is uncertain**. Long random passwords, AES keys, account rotation, and managed service accounts change the feasibility of guessing. A failed guess does not prove the account is safe, while a recovered password still requires an authorization review before any use.

{{< youtube id="PhNspeJ0r-4" enable="true" title="Kerberos Deep Dive Part 2 - Kerberoasting" >}}

**Compass Security's Kerberos presentation** supplements the ticket flow. Track which claims describe protocol behavior and which depend on an account's password, groups, or delegation settings. [Watch the presentation on YouTube](https://www.youtube.com/watch?v=PhNspeJ0r-4).

## Review Encryption Evidence

**RC4-HMAC** and **AES** are different Kerberos encryption choices. Hashcat mode 13100 is commonly associated with Kerberoastable RC4 ticket material. It is not a universal mode for every ticket representation or encryption type. Confirm the format and encryption field before selecting an analysis method.

Event 4769 records a **Kerberos service-ticket request** on a domain controller when auditing is enabled. Current Windows documentation includes fields for the requesting account, service name, ticket encryption type, client address, and status. The event shows a request, not a password crack or successful service use. [Microsoft's event 4769 reference](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/event-4769).

| Evidence | Supports | Does not support |
|---|---|---|
| **4769 success** | A TGS request reached the KDC | Password recovery |
| **RC4 encryption field** | RC4-specific review path | Weak password by itself |
| **Offline candidate** | A possible secret match | Authorization to use it |
| **Privileged group member** | Potential high impact | Current session access |

## Compare Account Designs

**Traditional user service accounts** often keep long-lived secrets managed by a team. **Group Managed Service Accounts (gMSAs)** allow Windows to manage password retrieval and rotation for approved hosts. Neither design removes the need to review SPNs, delegation, groups, or service scope. [Microsoft's gMSA overview](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/group-managed-service-accounts/group-managed-service-accounts/group-managed-service-accounts-overview).

| Design | Secret management | Review focus |
|---|---|---|
| **Traditional account** | Team-managed password and rotation | Age, length, reuse, and owner |
| **gMSA** | Directory-managed rotation | Allowed hosts and delegated use |
| **Computer account** | Machine-managed secret | SPNs, delegation, and machine role |
| **Disabled account** | Authentication disabled | Stale SPNs and ownership cleanup |

**SPN ownership** also needs review. Duplicate SPNs, stale registrations, and undocumented services create confusing ticket evidence. Resolve the directory object and application owner before assigning impact.

## Examine Delegation Carefully

**Delegation** permits one service or computer to act toward another service under defined conditions. Unconstrained, constrained, and resource-based constrained delegation use different directory attributes and trust assumptions. A delegation flag alone does not identify which users or services are impersonated in the observed scenario.

Use the **[MITRE ATT&CK Kerberoasting reference](https://attack.mitre.org/techniques/T1558/003/)** as a taxonomy aid, then validate the actual domain configuration. Record the relevant attribute, object owner, allowed principals, target service, and time of observation. Avoid treating a technique label as evidence of successful abuse.

## Inspect a Lab Ticket Cache

```powershell
klist.exe
klist.exe get cifs/fileserver.corp.example
```

**`klist.exe`** displays and requests tickets for the current logon session. Use the second command only against the named lab service and within the approved window. Preserve the output without publishing ticket blobs or secrets. [Microsoft's klist reference](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/klist).

**Expected result:** The lab either shows a TGS for the requested SPN or returns an error because the service, DNS record, or policy is unavailable. Either result needs the requesting identity, target SPN, time, and controller evidence. This command was documentation-reviewed and not executed on the macOS authoring host.

## Analyze a Synthetic Case

Assume **analyst.user** requests a TGS for `HTTP/reporting.corp.example`. Event 4769 records success with AES encryption. The service account is a gMSA allowed on two application hosts and has no privileged group membership. No offline candidate matches the captured lab fixture.

The **defensible conclusion** is a successful service-ticket request for a managed account. The evidence does not show password recovery, domain privilege, or unauthorized service use. A follow-up should review the gMSA host scope and SPN ownership rather than escalate the severity solely because a ticket exists.

| Observation | Correct interpretation |
|---|---|
| **Ticket request** | KDC issued or attempted a TGS |
| **AES type** | Encryption choice recorded in the event |
| **gMSA owner** | Rotation and host policy apply |
| **No password match** | Offline test did not recover the lab secret |
| **No privileged group** | No group-based domain-admin claim |

## Choose the Next Test

A **bounded next test** should resolve one uncertainty. If the question is SPN ownership, query directory metadata. If it is ticket monitoring, correlate event 4769 with the requesting host. If it is service authorization, inspect the application's access control. Do not combine password analysis, delegation changes, and remote access in one unexplained action.

| Uncertainty | Smallest useful evidence |
|---|---|
| **Who owns the SPN?** | Directory object and owner record |
| **Which encryption was used?** | Event 4769 encryption field |
| **Account resource reachability** | Approved authorization test |
| **Did a password guess succeed?** | Reproducible lab fixture result |

## Create the Review Record

Produce a **ticket and privilege review** for the synthetic case. Include the request event, account design, group and delegation evidence, offline result, and one condition able to change your conclusion.

```text
Requesting principal and host:
Domain controller and event reference:
Target SPN and owning object:
Ticket type and encryption evidence:
Account design, groups, and delegation:
Offline analysis scope and result:
Authorization impact established / untested:
Next approved observation and stopping condition:
Owner, timestamp, and retention location:
```

**Completion standard:** A reviewer sees which fact came from the KDC, directory, endpoint, or offline analysis. The record states what remains untested.

## Self-Check and Answers

| Question | Expected reasoning |
|---|---|
| **Does an SPN grant admin rights?** | No, it maps a service name to an account |
| **What does event 4769 show?** | A service-ticket request on the domain controller |
| **Does RC4 prove a weak password?** | No, it identifies an encryption path for review |
| **Does a recovered secret prove authorization?** | No, groups, ACLs, and policy still determine access |
| **Why review gMSAs separately?** | Their managed rotation and host scope alter exposure |
| **What makes a conclusion defensible?** | Source-specific evidence plus explicit untested conditions |

## Next Steps

Carry the **ticket and privilege review** into [Module 17: Lateral Movement and Expanding Access](/red-team-course/lateral-movement-and-expanding-access/). The next module uses it to test path prerequisites without assuming every credential reaches every host.

Return to the **[Red Team Course](/red-team-course-start/)** for the complete sequence.
