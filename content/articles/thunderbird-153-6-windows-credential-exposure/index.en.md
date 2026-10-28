---
title: "Thunderbird 153.6: Windows NTLM Credential Exposure and How to Update (2026)"
date: 2026-10-28
lastmod: 2026-10-28
toc: true
draft: false
description: "Two high-impact Thunderbird flaws expose Windows NTLM authentication data when a crafted email is displayed. Learn the two paths, check your version, and limit outbound SMB while updating."
genre: ["Cybersecurity", "Email Security", "Windows Security"]
tags: ["Thunderbird 153.6", "Thunderbird 153.6.0esr", "Thunderbird security update", "Thunderbird Windows vulnerability", "Thunderbird NTLM leak", "Thunderbird SMB authentication", "CVE-2026-118174", "CVE-2026-118176", "MFSA 2026-122", "OpenPGP key attachment", "external attachment", "remote content blocking", "mailbox URL", "extended-length UNC path", "Windows account name", "NTLM authentication data", "SMB credential exposure", "outbound SMB", "TCP port 445", "email security", "Windows mail client", "Thunderbird version check", "Thunderbird update", "NTLM relay", "offline password cracking"]
cover: ""
coverAlt: ""
coverCaption: ""
---

Mozilla fixed two **high-impact Windows credential-exposure flaws** in Thunderbird 153.6. Displaying a malicious email was enough to trigger either network request described in [MFSA 2026-122](https://www.mozilla.org/en-US/security/advisories/mfsa2026-122/). The advisory describes possible NTLM disclosure, not a confirmed breach of every recipient's credentials.

<!--more-->

## Key takeaways

- **CVE-2026-118174** involved an externally hosted OpenPGP key attachment. Displaying the message prompted a request without user interaction, even with remote content blocked.
- **CVE-2026-118176** involved a specially formed `mailbox:` URL using an extended-length UNC path. Displaying the message prompted an SMB connection to a server selected by the sender.
- **Update Thunderbird on Windows** and verify its installed version. The advisory names Thunderbird 153.6 as fixed. Thunderbird's release notes identify the corresponding 153.6.0esr build.

## What the email triggers

**The two flaws have different entry points.** Neither requires the recipient to click a link in the email, according to Mozilla's descriptions. Their Windows credential risk depends on a network request reaching an attacker-controlled share and the resulting authentication exchange. Mozilla does not report active exploitation in the advisory.

| Issue | Trigger when the email is displayed | Windows credential risk |
| --- | --- | --- |
| **CVE-2026-118174** | Thunderbird loads the content of an OpenPGP key attachment to offer key import. A sender marks it as an external attachment with an attacker-chosen URL. | A URL to a network share exposes the user's NTLM credentials if the request reaches the share. |
| **CVE-2026-118176** | An extended-length UNC path bypasses Thunderbird's restriction on remote shares in `mailbox:` URLs. | Thunderbird connects to an attacker-chosen SMB server and discloses the Windows account name and NTLM authentication data. |

For the **OpenPGP attachment** path, Mozilla explicitly says the request bypassed remote content blocking and required no user interaction. On systems other than Windows, this issue still permitted a remote request contrary to the remote-content setting, but Mozilla limits the NTLM credential leak to Windows. For the **`mailbox:` URL** path, Mozilla says other operating systems are unaffected. See the individual entries for [CVE-2026-118174](https://www.mozilla.org/en-US/security/advisories/mfsa2026-122/#CVE-2026-118174) and [CVE-2026-118176](https://www.mozilla.org/en-US/security/advisories/mfsa2026-122/#CVE-2026-118176).

**NTLM authentication data is not a plaintext password.** Mozilla says the data disclosed through the SMB path poses a risk of offline password cracking or relay attacks. A successful attack is not established merely because someone received a crafted message. The advisory also lists other Thunderbird flaws, including separate calendar and RSS paths. This guide addresses the two email-display paths above rather than treating all issues in the release as identical.

## Check and update Thunderbird

The affected workflow is **reading email in Thunderbird on Windows** before the relevant fix. Mozilla names **Thunderbird 153.6** as the fixed version in its advisory, without specifying a complete earliest-affected version range for these two issues. Its [153.6.0esr release notes](https://www.thunderbird.net/en-US/thunderbird/153.6.0esr/releasenotes/) identify an ESR build released on October 27, 2026. Do not infer the patch status of another channel, fork, or repackaged build from its version label alone.

1. On Windows, open **Help > About Thunderbird**. Read the version shown in the About window, which also checks for updates. Mozilla's [update instructions](https://support.mozilla.org/en-US/kb/updating-thunderbird) describe this path.
2. If an update is available, let Thunderbird download it, then select **Restart Thunderbird to Update**. Reopen **Help > About Thunderbird** and confirm the installed version after restart.
3. For the **153 ESR line**, compare the resulting version with **153.6.0esr** in Thunderbird's release notes. If you manage updates through an organization, ask the administrator to verify the deployed vendor fix rather than assuming an update is already installed.

> **Version caveat:** A 153.6.0esr release note confirms the release exists, while MFSA 2026-122 ties the security fixes to Thunderbird 153.6. The release notes do not describe each of these two CVEs individually. Use the advisory for the vulnerability details.

## Reduce exposure while updating

**Install the vendor fix first.** Disabling remote content alone does not stop CVE-2026-118174, since the reported request bypassed the setting. Avoid treating "do not click" advice as sufficient. Mozilla describes requests triggered by displaying the message.

As **defense in depth**, restrict outbound SMB from Windows clients to the internet, including **TCP port 445**, at the corporate firewall or on managed endpoints. [Microsoft's SMB traffic guidance](https://learn.microsoft.com/en-us/windows-server/storage/file-server/smb-secure-traffic) recommends blocking outbound TCP 445 to the internet and limiting access to required file servers. Inventory needed shares before enforcing a rule, especially if your environment uses a cloud file service or remote workers outside the perimeter. This network control limits the described SMB path but does not repair Thunderbird or address every remote-request issue in the advisory.

If a Windows machine running an older Thunderbird build displayed a suspicious message, **treat exposure as a question to investigate**, not proof of compromise. Review available outbound SMB connection records and authentication logs with your security team. The vendor advisory does not provide an exposure test or a blanket instruction to rotate every password.

## Sources

- [Mozilla Foundation Security Advisory 2026-122: Security Vulnerabilities fixed in Thunderbird 153.6](https://www.mozilla.org/en-US/security/advisories/mfsa2026-122/)
- [Thunderbird Desktop release notes: 153.6.0esr](https://www.thunderbird.net/en-US/thunderbird/153.6.0esr/releasenotes/)
- [Mozilla Support: Update Thunderbird to the latest version](https://support.mozilla.org/en-US/kb/updating-thunderbird)
- [Microsoft Learn: Secure SMB Traffic in Windows Server](https://learn.microsoft.com/en-us/windows-server/storage/file-server/smb-secure-traffic)
