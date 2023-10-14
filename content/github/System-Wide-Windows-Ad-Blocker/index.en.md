---
title: "Windows 10 System-Wide Ad Blocker Script for Better Privacy and Security"
date: 2021-04-02
toc: true
draft: false
description: "Block ads, trackers, and telemetry on Windows 10 using this powerful PowerShell script that utilizes the hosts file and Windows Firewall for system-wide ad-blocking."
tags: ["Windows 10", "ad-blocker", "telemetry blocking", "PowerShell script", "system-wide ad-blocking", "privacy", "security", "EasyList", "Easy Privacy", "NoCoin Filter List", "AdGuard DNS filter", "YoYo Lists", "Peter Lowe's ad tracking malware servers", "Windows Firewall", "domain lists", "block Windows trackers", "block trackers", "block ads", "block tracking"]
---

**System-Wide-Windows-Ad-Blocker**

[![VirusTotal Scan](https://github.com/simeononsecurity/System-Wide-Windows-Ad-Blocker/actions/workflows/virustotal.yml/badge.svg)](https://github.com/simeononsecurity/System-Wide-Windows-Ad-Blocker/actions/workflows/virustotal.yml)

This script is a Windows PowerShell script that downloads and applies the "StevenBlack/hosts" file to the system's "hosts" file, which can be used to block certain domains/websites by mapping them to an IP address of your choice (usually the IP address of the local machine). The script checks the internet connection and proxy settings, and tries downloading the latest version of the "hosts" file from two different sources: "https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts" and "http://sbc.io/hosts/hosts". If the download fails, the script continues with a local copy of the "hosts" file. The script requires elevated privileges to run and modifies the ".NETFramework" registry key to use only the latest version of the .NET framework.

*We are seeking all comments and concerns for this repo. Please submit an [issue](https://github.com/simeononsecurity/System-Wide-Windows-Ad-Blocker/issues) with any information you might have.*

### Lists Used:
- [StevenBlack/hosts - adware + malware](https://github.com/StevenBlack/hosts)

### Example:
#### Manual install:
**The script may be launched from the extracted GitHub download like this:**
```powershell
.\sos-system-wide-windows-ad-block.ps1
```
#### Automated install:
Run the latest version of the script automatically:
```powershell
iwr -useb 'https://simeononsecurity.com/scripts/soswindowsadblocker.ps1' | iex
```

