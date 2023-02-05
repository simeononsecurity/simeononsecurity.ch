---
title: "Hardening Windows Defender Antivirus with PowerShell Script - Enhancing Security in Windows 10 Enterprise & Professional"
date: 2020-11-15
toc: true
draft: false
description: "Windows Defender Hardening is a PowerShell script that enhances the security of Windows Defender Antivirus on Windows 10 Enterprise or Windows 10 Professional. The script enables cloud-delivered protections, controlled folder access, network protections, intrusion prevention system, Windows Defender Application Control policies, Windows Defender Attack Surface Reduction rules, and Windows Defender Exploit Protections. The script also implements all the requirements listed in the Windows Defender Antivirus STIG V2R1. The script is compatible with Windows 10 Home, but it may not allow for GPO configurations or Attack Surface Reduction. Windows 10 "N" Editions are not tested."
tags: ["PowerShell", "PowerShell Script", "Automation", "Compliance", "Windows Defender STIG Script", "Windows Defender", "Windows Defender Hardening", "Windows Defender STIG", "Defender STIG", "Windows Defender Application Control", "WDAC", "Windows Defender Exploit Protection", "WDEP", "Windows Defender Attack Surface Reduction", "ASR"]
---

# Windows-Defender-Hardening

## What does this script do?
- Enables Cloud-delivered Protections
- Enables Controlled Folder Access
- Enables Network Protections
- Enables Intrusion Prevention System
- [Enables Windows Defender Application Control Policies](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/windows-defender-application-control)
- [Enables Windows Defender Attack Surface Reduction Rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-atp/attack-surface-reduction)
- [Enables Windows Defender Exploit Protections](https://docs.microsoft.com/en-us/microsoft-365/security/defender-endpoint/enable-exploit-protection?view=o365-worldwide#powershell)
- Implements all requirements listed in the [Windows Defender Antivirus STIG V2R1](https://dl.cyber.mil/stigs/zip/U_MS_Windows_Defender_Antivirus_V2R1_STIG.zip)

## Requirements:
- [x] Windows 10 Enterprise (**Preferred**) or Windows 10 Professional
  - Windows 10 Home does not allow for GPO configurations or [ASR](https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-atp/attack-surface-reduction). 
Though most of these configurations will still apply. 
  - Windows 10 "N" Editions are not tested.

## Download the required files:

Download the required files from the [GitHub Repository](https://github.com/simeononsecurity/Windows-Defender-STIG-Script)

## How to run the script:

**The script may be lauched from the extracted GitHub download like this:**
```
.\sos-windowsdefenderhardening.ps1
```
