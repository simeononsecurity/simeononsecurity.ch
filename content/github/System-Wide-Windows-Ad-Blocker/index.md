---
title: "Block Ads, Trackers, and Telemetry on Windows 10 with the System Wide Ad Blocker Script"
date: 2021-04-02
toc: true
draft: false
description: "This script provides an effective way to block telemetry-related domains and related IPs, increasing your privacy and security while browsing the internet. By utilizing the hosts file and Windows Firewall, this PowerShell script blocks ads and trackers system-wide on Windows 10. The script uses popular blocklists such as EasyList, Easy Privacy, NoCoin Filter List, AdGuard DNS filter, YoYo Lists, and Peter Lowe's ad/tracking/malware servers. Note that adding certain domains may cause issues with software such as iTunes or Skype, and entries related to Akamai have been reported to cause issues with Widevine DRM. The script can be easily executed by running the latest version. Get started with this powerful script today and enjoy a more secure and ad-free browsing experience."
tags: ["PowerShell, PowerShell Script, Automation, Windows Firewall, Windows AD Blocking, Ad Block, Domain Lists, Block Windows Trackers, Block Trackers, Block Tracking and Ads System Wide"]
---

## Description:
This script blocks Telemetry related domains via the hosts file and related IPs via Windows Firewall.

**Notes:**
- Adding these domains may break certain software like iTunes or Skype
- Entries related to Akamai have been reported to cause issues with Widevine DRM

### Lists Used:
- [EasyList](https://easylist.to/easylist/easylist.txt) / [JustDomains - EasyList](https://justdomains.github.io/blocklists/lists/easylist-justdomains.txt)
- [Easy Privacy](https://easylist.to/easylist/easyprivacy.txt) / [JustDomains - EasyPrivacy](https://justdomains.github.io/blocklists/lists/easyprivacy-justdomains.txt)
- [NoCoin Filter List](https://github.com/hoshsadiq/adblock-nocoin-list/) / [JustDomains - NoCoin Filter List](https://justdomains.github.io/blocklists/lists/nocoin-justdomains.txt)
- [AdGuard DNS filter](https://github.com/AdguardTeam/AdguardSDNSFilter) / [JustDomains - AdGuard Simplified Domain Names Filter](https://justdomains.github.io/blocklists/lists/adguarddns-justdomains.txt)
- [YoYo Lists](https://pgl.yoyo.org/adservers/serverlist.php)
- [Peter Lowe’s ad/tracking/malware servers](https://pgl.yoyo.org/adservers/policy.php)

### Example:

Run the latest version of the script automatically:
```powershell
iwr -useb 'https://raw.githubusercontent.com/simeononsecurity/System-Wide-Windows-Ad-Blocker/main/sos-system-wide-windows-ad-block.ps1' | iex
```
