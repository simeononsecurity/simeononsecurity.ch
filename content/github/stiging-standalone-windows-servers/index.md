---
title: "STIGing Standalone Windows Servers"
date: 2020-09-09-T11:59:03-05:00
toc: true
draft: false
description: "Automate STIGing Windows Server 2012, 2016, and 2019"
tags: ['Automation', 'How To Automate Windows STIG', 'Windows Updates', 'Compliance', 'Windows Server STIG', 'Windows Server 2012', 'Windows Server 2012 R2', 'Windows Server 2016', 'Windows Server 2019', 'Server 2012', 'Server 2016', 'Server 2019', 'Powershell', 'Script']
---
# STIGing Standalone Windows Servers

Download all the required files from the [GitHub Repository](https://github.com/simeononsecurity/Standalone-Windows-Server-STIG-Script)

## Introduction:

Windows Server 2012, 2016, and 2019 are insecure operating systems out of the box and requires many changes to insure [FISMA](https://www.cisa.gov/federal-information-security-modernization-act) compliance. 
[Microsoft](https://microsoft.com), [Cyber.mil](https://public.cyber.mil), the [Department of Defense](https://dod.gov), and the [National Security Agency](https://www.nsa.gov/) have recommended and required configuration changes to lockdown, harden, and secure the operating system and ensure government compliance. These changes cover a wide range of mitigations including blocking telemetry, macros, removing bloatware, and preventing many physical attacks on a system.

Standalone systems are some of the most difficult and annoying systems to secure. When not automated, they require manual changes of each STIG/SRG. Totalling over 1000 configuration changes on a typical deployment and an average of 5 minutes per change equaling 3.5 days worth of work. This script aims to speed up that process significantly.

## Notes: 

- This script is designed for operation in **Enterprise** environments and assumes you have hardware support for all the requirements.
- This script is not designed to bring a system to 100% compliance, rather it should be used as a stepping stone to complete most, if not all, the configuration changes that can be scripted. 
  - Minus system documentation, this collection should bring you up to about 95% compliance on all the STIGS/SRGs applied.

## Requirements:
- [X] Windows 10 Enterprise is **Required** per STIG.
- [x] [Standards](https://docs.microsoft.com/en-us/windows-hardware/design/device-experiences/oem-highly-secure) for a highly secure Windows 10 device
- [x] System is [fully up to date](https://support.microsoft.com/en-gb/help/4027667/windows-10-update)
  - Currently Windows 10 **v1909** or **v2004**. 
  - Run the [Windows 10 Upgrade Assistant](https://support.microsoft.com/en-us/help/3159635/windows-10-update-assistant) to be update and verify latest major release.
- [X] Hardware Requirements
  - [Hardware Requirements for Memory Integrity](https://docs.microsoft.com/en-us/windows/security/threat-protection/device-guard/requirements-and-deployment-planning-guidelines-for-virtualization-based-protection-of-code-integrity#baseline-protections) 
  - [Hardware Requirements for Windows Defender Application Guard](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-guard/reqs-wd-app-guard)
  - [Hardware Requirements for Windows Defender Credential Guard](https://docs.microsoft.com/en-us/windows/security/identity-protection/credential-guard/credential-guard-requirements)
  
## Recommended reading material:
  - [System Guard Secure Launch](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-system-guard/system-guard-secure-launch-and-smm-protection#requirements-met-by-system-guard-enabled-machines)
  - [System Guard Root of Trust](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-system-guard/system-guard-how-hardware-based-root-of-trust-helps-protect-windows)
  - [Hardware-based Isolation](https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-atp/overview-hardware-based-isolation)
  - [Memory integrity](https://docs.microsoft.com/en-us/windows/security/threat-protection/device-guard/memory-integrity)
  - [Windows Defender Application Guard](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-guard/wd-app-guard-overview)
  - [Windows Defender Credential Guard](https://docs.microsoft.com/en-us/windows/security/identity-protection/credential-guard/credential-guard-how-it-works)

## A list of scripts and tools this collection utilizes:

- [Microsoft Security Compliance Toolkit 1.0](https://www.microsoft.com/en-us/download/details.aspx?id=55319)

- [Cyber.mil - Group Policy Objects](https://public.cyber.mil/stigs/gpo/)

- [NSACyber - Bitlocker Guidance](https://github.com/nsacyber/BitLocker-Guidance)

## Additional configurations were considered from:

- [NSACyber - Hardware-and-Firmware-Security-Guidance](https://github.com/nsacyber/Hardware-and-Firmware-Security-Guidance)

- [NSACyber - Application Whitelisting Using Microsoft AppLocker](https://apps.nsa.gov/iad/library/ia-guidance/tech-briefs/application-whitelisting-using-microsoft-applocker.cfm)

## STIGS/SRGs Applied:

- [Windows Server 2012(R2)](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MS_Windows_2012_and_2012_R2_MS_V2R19_STIG_SCAP_1-2_Benchmark.zip) 

- [Windows Server 2016](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MS_Windows_Server_2016_V1R12_STIG.zip)

- [Windows Server 2019](#)

- [Windows Defender Antivirus V1R9](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MS_Windows_Defender_Antivirus_V1R9_STIG.zip)

- [Windows Firewall V1R7](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Windows_Firewall_V1R7_STIG.zip)

- [Internet Explorer 11 V1R19](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MS_IE11_V1R19_STIG.zip)

- [Google Chrome V1R19](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Google_Chrome_V1R19_STIG.zip)

- [Firefox V4R29](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MOZ_FireFox_V4R29_STIG.zip)

- [Microsoft .Net Framework 4 V1R9](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MS_DotNet_Framework_4-0_V1R9_STIG.zip) - **Work in Progress**

- [Oracle JRE 8 V1R5](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Oracle_JRE_8_Windows_V1R5_STIG.zip)

## How to run the script

**The script may be launched from the extracted GitHub download like this:**
```
.\sos-secure-standalone-server.ps1
```
The script we will be must be launched from the directory containing all the files from the [GitHub Repository](https://github.com/simeononsecurity/Standalone-Windows-Server-STIG-Script)
