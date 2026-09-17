---
title: "Module 9: Active Reconnaissance and Scanning"
date: 2026-09-12
toc: true
draft: false
description: "Touch the target for the first time: run quiet Nmap scans from a redirector, plan the phishing campaign, and log every action."
genre: ["Red Team", "Offensive Security", "Reconnaissance"]
tags: ["red team", "active reconnaissance", "Nmap", "SYN scan", "connect scan", "port scan", "phishing planning", "logging", "red team course"]
cover: "/img/cover/active-reconnaissance-cybersecurity-scanning.webp"
coverAlt: "An illustration of a shadowy figure at a computer, scanning a digital network map with flowing data streams, set against a dark background with vibrant colors."
coverCaption: "Module 9: the first touch, done quietly and logged."
---

#### [← Return to the Red Team Course](/red-team-course-start/)

**Active reconnaissance is the first time you touch the customer's infrastructure, so your activity gets logged on their side and on yours.** The job is a balance: scan quietly while still pulling the information the assessment needs.

*This module takes about 12 minutes.*

______

## Key Terms

| Term | Plain meaning |
|------|---------------|
| **SYN scan (`-sS`)** | half-open scan, abnormal in bulk |
| **Connect scan (`-sT`)** | full handshake, looks ordinary |
| **Redirector** | the disposable host you scan from |
| **Attack plan** | the prioritized target list recon produces |
| **Deconfliction** | the customer's log-back to your activity |
______

## What Changes Now

OSINT read what the internet already knew. Active recon targets and touches customer infrastructure, traffic a defender flags. Common tools here are `Nmap`, DNS reconnaissance tools, and web proxies.

The default posture is quiet and careful. Exceptions exist where a red team is deliberately loud, such as white-box testing, but quiet is the norm.

______

## Nmap and Staying Stealthy

`Nmap` fingerprints hosts and devices. It offers low-level TCP options, speed presets, log formats other tools ingest, and include and exclude lists.

Two rules shape how you use it:

- **Scan from a redirector**, never from your real infrastructure. A burned source address should be disposable.
- **Scan as slowly as the operation allows.** Loud, fast scans are easy to spot and block.

Connection type matters as much as speed:

| Scan | Behavior | Signature |
|------|----------|-----------|
| `-sS` SYN | half-open connections | looks abnormal in bulk |
| `-sT` connect | completes the handshake | looks like ordinary traffic |

Quiet recon favors `-sT` over a short port list, run slow from a disposable redirector, with a randomized and resumable target list. Common external ports: `443`, `80`, `8080`, `8443`, `5985`, `5986`, `3389`, `25`, `110`, `22`, `445`.

> **Operator takeaway:** quiet recon is `-sT` over a short port list, run slow from a disposable redirector, with a randomized target list. Speed is what you trade away to stay unseen.

______

## Phishing Planning Starts Here

Phishing planning belongs in active recon, before you execute anything:

- Build the target email list from OSINT.
- Prepare a malicious attachment, such as a macro-enabled Office document.
- Write the email content which carries it.

Phishing remains an easy way in and is often the low-hanging fruit. One well-crafted campaign skips hours of web application testing, so the planning starts early.

______

## Logging

Accurate logs of every action on a customer network are not optional. They support deconfliction, the final report, and operator rotation.

Log as you go. Reconstructing activity after the fact is where mistakes and missed cleanup come from.

______

## Web Application Enumeration

Web applications hide a large share of the attack surface. SQL injection and cross-site scripting surface when you enumerate input paths and test for reflected output.

{{< youtube id="Rqt_BgG5YyI" >}}

Watch the lab: [SQL injection and XSS](https://www.youtube.com/watch?v=Rqt_BgG5YyI)

______

## Plan the Scan

You must map a set of customer hosts without burning your source. Decide each point:

1. Where do you scan from, and why?
2. Which scan type fits a quiet run over a short port list?
3. Which ports do you include first?
4. What do you log as you go?

Answer from memory first. The explanations are in the Answer Key at the end.
______

## Common Mistakes

- Scanning from your real infrastructure instead of a redirector.
- Running a fast, broad scan which trips detection.
- Skipping the log entry for a recon action.
- Favoring `-sS` where a quieter `-sT` fits.

______

## Self-Check

1. Why scan from a redirector?
2. Contrast `-sS` and `-sT` signatures.
3. Name two things phased into active recon before execution.
4. Why are recon logs not optional?

______

## Answer Key

**Self-Check**

1. **The redirector is disposable.** A burned source address costs you nothing.
2. **`-sS` half-opens, `-sT` completes the handshake.** The full handshake reads as ordinary traffic.
3. **A target email list and a payload.** Plan the phishing campaign before touching anything.
4. **Logs feed deconfliction, the report, and operator rotation.** Reconstructing after the fact loses cleanup.

**Exercise**

1. **From a redirector**, not your real infrastructure.
2. **`-sT`** over a short port list, run slow.
3. **443, 80, 8080, 8443 and the management ports** first.
4. **Every action**, as it happens.
______

## Next Steps

Recon is done and the plan is set. Next, execution: turning the plan into the first foothold.

**[→ Module 10: Initial Access: Phishing and Delivery](/red-team-course/initial-access-phishing-and-delivery/)**

Or return to the hub: **[Red Team Course](/red-team-course-start/)**
