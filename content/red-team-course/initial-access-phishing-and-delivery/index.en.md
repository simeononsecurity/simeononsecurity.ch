---
title: "Module 10: Initial Access: Phishing and Delivery"
date: 2026-09-12
toc: true
draft: false
description: "Turn the plan into a foothold: exploitation, phishing campaigns with GoPhish and Cobalt Strike, listener selection, off-limits callbacks, and 32-bit filesystem redirection."
genre: ["Red Team", "Offensive Security", "Initial Access", "Phishing"]
tags: ["red team", "initial access", "phishing", "GoPhish", "Cobalt Strike", "web shell", "RCE", "listener", "HTTPS", "SMB", "syswow64", "sysnative", "red team course"]
cover: "/img/cover/initial-access-phishing-cybersecurity-illustration.webp"
coverAlt: "An illustration showing a digital scene with abstract representations of phishing emails, malicious links, and weaponized attachments. The background is dark with vibrant colors highlighting the phishing elements."
coverCaption: "Module 10: phishing and delivery, the path in."
---

#### [← Return to the Red Team Course](/red-team-course-start/)

**Target exploitation is where the plan runs. The goal is simple: gain access to the customer network.** Phishing is the most reliable path, and this module walks the delivery end to end with the tools to run it.

*This module takes about 15 minutes.*

______

## Key Terms

| Term | Plain meaning |
|------|---------------|
| **Web shell** | an uploaded file executing system commands |
| **RCE** | remote code execution on a vulnerable service |
| **GoPhish** | the framework running phishing at scale |
| **Listener** | the transport a beacon calls back to |
| **Sysnative** | the keyword cancelling 32-bit redirection |
______

## Exploitation Techniques

Access arrives several ways:

| Technique | What it is | Risk |
|-----------|-----------|------|
| **Web shell** | an upload file executing system commands | common, frequent win |
| **RCE** | remote code execution on a vulnerable service | less common, high risk |

RCE is worth probing by checking for outdated services and systems, but an attempt crashes a service or trips an IDS. Use it carefully.

A **web shell** is a web page file submitting system commands to the underlying server, turning an upload feature into command execution. Upload forms, authenticated or not, remain a frequent win.

______

## Phishing as the Path In

Phishing targets people rather than patched software, so no security appliance fully protects an untrained workforce. Two email approaches:

- A malicious **link** to a page exploiting the browser or a plugin.
- A malicious **attachment**, a weaponized PDF or Office document.

Standing rules apply. Do not impersonate real entities, avoid harmful topics, and keep content lawful. The customer approves the campaign in advance.

> **Operator takeaway:** off-limits callbacks always happen during a campaign. A payload lands outside scope when a user checks email from home or forwards it. Check every callback against your allow and deny lists, then report any out-of-scope one immediately.

______

## GoPhish and Cobalt Strike Delivery

**GoPhish** is an open-source framework for running phishing campaigns at scale. Its pieces snap together:

| Piece | What it is |
|-------|-----------|
| **Sending profile** | the spoofed sender and SMTP relay |
| **Landing page** | usually a cloned login portal to capture credentials |
| **Email template** | the HTML lure |
| **Users and groups** | the target list |

GoPhish launches the campaign and reports who received, opened, and acted. For this delivery method, you use GoPhish to send an **attachment**, not to harvest credentials on a cloned portal.

{{< youtube id="mRUGEygkDEQ" >}}

Setting up the sending relay: [SMTP server setup for phishing infrastructure](https://www.youtube.com/watch?v=mRUGEygkDEQ)

______

## Choosing the Listener

Once the payload runs, the beacon needs a listener. Cobalt Strike offers two which fit different hosts:

| Listener | Port | Looks like | Best on |
|----------|------|-----------|---------|
| **HTTPS** | `443` | a user browsing the web | workstations which browse external sites |
| **SMB** | `445` | general SMB traffic | servers which never browse out: DCs, file, and Exchange |

Match the listener to the host. HTTPS blends on a workstation. On a domain controller which never touches an external site, outbound HTTPS stands out, so an SMB beacon riding internal `445` traffic is quieter.

______

## Weaponizing an Office Attachment

The attachment path in practice is a macro-enabled Office document. Cobalt Strike generates the payload:

{{< youtube id="xY2DIRfqNvA" >}}

Watch: [Phishing with .slk Excel payloads](https://www.youtube.com/watch?v=xY2DIRfqNvA)

______

## Filesystem Redirection

After you run `spawnas` or install a service, you land in a 32-bit process. On a 64-bit host, which changes where your files go:

| You run as | `system32` resolves to | To reach true 64-bit `system32` |
|------------|------------------------|---------------------------------|
| x86 on 64-bit host | `syswow64` (redirected) | use `c:\windows\sysnative` |
| x64 on 64-bit host | real `system32` | use `system32` directly |
| 32-bit host | real `system32` | no redirection to worry about |

A 32-bit process writing to `c:\windows\system32` lands in `c:\windows\syswow64`. When your service or run key points at the intended path, nothing is there.

The fix is `c:\windows\sysnative`, a keyword telling Windows not to redirect the call. It is not a real folder.

> **Operator takeaway:** check your process architecture before you upload or install anything. If you are x86 on a 64-bit host, migrate first or use `sysnative` in your paths.

______

## Living Off the Land

Once inside, prefer tools already on the host over dropping new binaries. PowerShell runs without spawning the tracked `powershell.exe` process, leaving less for defenders to signature.

{{< youtube id="7tvfb9poTKg" >}}

Watch: [PowerShell without powershell.exe](https://www.youtube.com/watch?v=7tvfb9poTKg)

______

## Route the Payload Home

Your payload landed on a workstation and on a file server. For each host, pick the callback and explain:

1. A user's workstation browsing the web all day.
2. A file server which never touches external sites.
3. A 32-bit process dropped on a 64-bit host.

Answer from memory first. The explanations are in the Answer Key at the end.
______

## Common Mistakes

- Choosing an HTTPS listener inside a network where only SMB traffic is normal.
- Ignoring an out-of-scope callback instead of reporting it.
- Falling into 32-bit filesystem redirection and pointing a service at the wrong path.
- Using RCE where a web shell does the same job more quietly.

______

## Self-Check

1. Name the four GoPhish pieces and each role.
2. When is an SMB listener the right choice?
3. Where does a 32-bit process writing to `system32` land?
4. What is `sysnative`?

______

## Answer Key

**Self-Check**

1. **Sending profile, landing page, email template, users and groups.** The four pieces of a GoPhish campaign.
2. **When the host never browses externally.** SMB rides internal 445 traffic instead.
3. **SysWOW64.** 32-bit redirection sends `system32` writes there.
4. **A keyword cancelling redirection.** It is not a real folder.

**Exercise**

1. **HTTPS**, reads as browsing.
2. **SMB**, blends with internal traffic.
3. **`sysnative` or migrate to x64 first**, so paths resolve correctly.
______

## Next Steps

You are inside. Next, the discipline underneath all of post-exploitation: knowing the state of the box before you act.

**[→ Module 11: Situational Awareness and Host Operations](/red-team-course/situational-awareness-and-host-operations/)**

Or return to the hub: **[Red Team Course](/red-team-course-start/)**
