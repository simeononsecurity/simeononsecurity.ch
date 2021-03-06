---
title: 'Block Ads and Trackers System Wide on Windows 10'
date: 2021-04-02
toc: true
draft: false
description: "This script blocks Telemetry related domains via the hosts file and related IPs via Windows Firewall."
tags: ['PowerShell', 'PowerShell Script', 'Automation', 'Windows Firewall', 'Windows AD Blocking', 'Ad Block', 'Domain Lists', 'Block Windows Trackers', 'Block Trackers', 'Block Tracking and Ads System Wide']
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
