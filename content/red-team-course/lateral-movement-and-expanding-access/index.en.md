---
title: "Module 17: Lateral Movement and Expanding Access"
date: 2026-09-12
toc: true
draft: false
description: "Move from a workstation to the domain controller with SMB beacons, service manipulation instead of signatured jump commands, and the link step which catches new operators."
genre: ["Red Team", "Offensive Security", "Lateral Movement", "Active Directory"]
tags: ["red team", "lateral movement", "domain controller", "SMB beacon", "service manipulation", "sc_query", "sc_qc", "pass the hash", "red team course"]
cover: "/img/cover/lateral-movement-domain-controller-cybersecurity.webp"
coverAlt: "An abstract illustration showing interconnected servers and data flows in cybersecurity, with a central domain controller and vibrant colors against a dark background."
coverCaption: "Module 17: reach the domain controller and hold it."
---

#### [← Return to the Red Team Course](/red-team-course-start/)

**The domain controller is the prize: it holds every password hash, it reaches every host, and it gates the trusts to other domains.** Getting a Beacon on it turns a single-host foothold into domain-wide control.

*This module takes about 18 minutes.*

______

## Key Terms

| Term | Plain meaning |
|------|---------------|
| **Domain controller** | the host holding the domain's hashes |
| **SMB beacon** | a callback riding internal 445 traffic |
| **Service manipulation** | borrowing a service to run a payload |
| **`link`** | connecting to a live SMB beacon |
| **`sc_qc`** | the query returning a service's binpath |
______

## Locate the DC and the Accounts

Two group reads answer both halves of the problem:

```text
netGroupListMembers "Domain Controllers" corp.local
netGroupListMembers "Domain Admins" corp.local
```

The first gives you the hostnames. The second gives you the accounts which log into them. Cross-reference those names against the credentials and tokens you already collected, and you have your target host and your key before you touch the DC.

______

## Test the Credential First

Before any jump, `ls` the admin share of the target and read the error code:

```text
ls \CORP-DC1.corp.local\c$
```

| Error | Meaning |
|-------|---------|
| Access denied (code 5) | connected, but the account lacks rights there |
| Logon failure (code 1326) | the credential itself is bad |
| Network path not found | the FQDN is not resolving |

Fix the account, fix the credential, or fix the name. Do not fire a payload at a target you have not confirmed as reachable.

______

## SMB, Not HTTPS, for the DC

On systems which do not normally reach the internet, use an SMB beacon. Domain controllers, file servers, and Exchange servers do not make outbound HTTPS, so an HTTPS beacon there stands out. SMB beacons never call the internet. They run over port 445 through a named pipe, linked through a Beacon you already hold.

______

## execute Runs Locally

New operators assume `execute` reaches across the network. It does not:

```text
execute \REMOTE\c$\windows\system32\implant.exe
```

It runs the remote file where you typed the command, on your current machine, the same way double-clicking a file on a share runs it locally. Remote execution needs a plugin built for it.

______

## Skip the Signatured Jump Commands

| Jump | Why to avoid |
|------|--------------|
| `psexec_psh` | encoded PowerShell, random service names |
| `psexec` / `psexec64` | random services and binaries |
| `winrm` / `winrm64` | PowerShell over WinRM |

All three are heavily signatured. Use service manipulation instead.

______

## Service Manipulation

Reconfigure an existing service instead of creating one:

```text
sc_query vss 192.168.1.10
sc_qc vss 192.168.1.10
```

Confirm the service is stopped and runs as Local System. Record the original binpath. Then the manual sequence:

1. Upload the beacon to blend into the file system.
2. Record the original binpath from `sc_qc`.
3. Change the binpath to your beacon.
4. Start the service, which launches the beacon.
5. Set the binpath back to the original.
6. Remove the uploaded beacon.

Restoring the binpath and deleting the beacon are the steps which keep it clean. Skip them and you have left a reconfigured service plus a payload on disk.

______

## Link Into the SMB Beacon

SMB sessions behave differently in the client:

- A chain link icon marks an SMB-linked session.
- The chain appears broken when the SMB link is not connected.
- SMB beacons incorrectly show the HTTPS listener name in the column. This is a display quirk, not a misconfiguration.

The step operators forget: after `servicemanip` runs, the SMB beacon is alive but not connected. Run `link` to link into it over the named pipe. Until you link, the chain stays broken and you have no interaction.

______

> **Operator takeaway:** enumerate with `sc_query` and `sc_qc`, confirm the service is stopped and runs as Local System, write down the original binpath, restore it after, delete the beacon, and remember to `link` when the SMB beacon lands.

______

## Reach the Controller

Plan the jump from a workstation to the DC:

1. Which two commands name the target host and the login account?
2. What do you do before any jump command?
3. Which transport does the DC beacon use?
4. What do you restore after borrowing a service?

Answer from memory first. The explanations are in the Answer Key at the end.
______

## Common Mistakes

- Assuming `execute` reaches a remote host when it runs locally.
- Firing a payload at a target before testing the `c$` share.
- Creating new jump commands instead of borrowing a service.
- Forgetting to `link` into the SMB beacon after `servicemanip`.

______

## Self-Check

1. Which two group reads locate the DC and the login accounts?
2. What does error code 5 versus 1326 tell you?
3. Why is SMB the right transport for the DC?
4. List the six steps of manual service manipulation.

______

## Answer Key

**Self-Check**

1. **`netGroupListMembers "Domain Controllers"` and `"Domain Admins"`.** One names the host, the other the login accounts.
2. **5 means connected but lacking rights, 1326 means bad credentials.** Fix the account or fix the credential.
3. **The DC never browses externally.** SMB rides internal 445 traffic instead of standing out.
4. **Upload, record binpath, swap binpath, start, restore binpath, delete beacon.**

**Exercise**

1. **The two `netGroupListMembers` reads** for Domain Controllers and Domain Admins.
2. **`ls` the `c$` share and read the error code.**
3. **SMB**, linked over a named pipe.
4. **The original binpath**, and remove the uploaded beacon.
______

## Next Steps

You have moved laterally and reached the controller. Next, read the directory itself with ldapsearch and pivot across domain trusts.

**[→ Module 18: Cross-Domain Pivoting and LDAP Enumeration](/red-team-course/cross-domain-pivoting-and-ldap-enumeration/)**

Or return to the hub: **[Red Team Course](/red-team-course-start/)**
