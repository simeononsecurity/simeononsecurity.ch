---
title: "Automating Windows 10 STIG Compliance with Powershell Script"
date: 2020-08-26T11:59:03-05:00
toc: true
draft: false
description: "Learn how to automate the STIGing process of Windows 10 systems with the Standalone Windows STIG Script, saving time and improving efficiency for securing standalone systems in enterprise environments."
tags: ["Automation", "Windows STIG Compliance", "Powershell Scripting", "Windows 10 Enterprise", "Windows Updates", "FISMA Compliance", "Windows 10 Hardening", "Cybersecurity", "National Security Agency", "Department of Defense", "Microsoft Security Compliance Toolkit", "Windows Defender Application Guard", "Windows Defender Credential Guard", "System Guard Secure Launch", "Memory Integrity", "Microsoft Office", "Adobe Reader", "Google Chrome", "Mozilla Firefox", "Oracle JRE"]

---

**Download all the required files from the [GitHub Repository](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)**

**We are seeking help with the following [.Net issue](https://github.com/simeononsecurity/W10-Optimize-and-Harden/issues/3)** 

## Introduction:

Windows 10 is insecure operating system out of the box and requires many changes to insure [FISMA](https://www.cisa.gov/federal-information-security-modernization-act) compliance. 
Organizations like [Microsoft](https://microsoft.com), [Cyber.mil](https://public.cyber.mil), the [Department of Defense](https://www.defense.gov/), and the [National Security Agency](https://www.nsa.gov/) have recommended and required configuration changes to lockdown, harden, and secure the operating system and ensure government compliance. These changes cover a wide range of mitigations including blocking telemetry, macros, removing bloatware, and preventing many physical attacks on a system.

Standalone systems are some of the most difficult and annoying systems to secure. When not automated, they require manual changes of each [STIG/SRG](https://simeononsecurity.com/github/stiging-standalone-windows-servers/). Totalling over 1000 configuration changes on a typical deployment and an average of 5 minutes per change equaling 3.5 days worth of work. This script aims to speed up that process significantly.

## Notes: 

- This script is designed for operation in **Enterprise** environments and assumes you have hardware support for all the requirements.
  - For personal systems please see this [GitHub Repository](https://github.com/simeononsecurity/W10-Optimize-and-Harden)
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
 
- [Windows 10 V1R23](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MS_Windows_10_V1R23_STIG.zip)

- [Windows Defender Antivirus V1R9](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MS_Windows_Defender_Antivirus_V1R9_STIG.zip)

- [Windows Firewall V1R7](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Windows_Firewall_V1R7_STIG.zip)

- [Internet Explorer 11 V1R19](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MS_IE11_V1R19_STIG.zip)

- [Adobe Reader Pro DC Continous V1R2](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Adobe_Acrobat_Pro_DC_Continuous_V1R2_STIG.zip)

- [Microsoft Office 2019/Office 365 Pro Plus V1R2](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MS_Office_365_ProPlus_V1R2_STIG.zip)

- [Microsoft Office 2016 V1R2](https://dl.dod.cyber.mil/wp-content/uploads/stigs/pdf/U_Microsoft_Office_2016_V1R2_Overview.pdf)

- [Microsoft Office 2013 V1R5](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MicrosoftOffice2013_V1R5_Overview.zip)

- [Google Chrome V1R19](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Google_Chrome_V1R19_STIG.zip)

- [Firefox V4R29](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MOZ_FireFox_V4R29_STIG.zip)

- [Microsoft .Net Framework 4 V1R9](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MS_DotNet_Framework_4-0_V1R9_STIG.zip) - **Work in Progress**

- [Oracle JRE 8 V1R5](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Oracle_JRE_8_Windows_V1R5_STIG.zip)

## How to run the script

**The script may be lauched from the extracted GitHub download like this:**
```
.\secure-standalone.ps1
```
The script we will be using must be launched from the directory containing all the other files from the [GitHub Repository](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)


## Why we implement DISA and DoD STIG/SRG Guidance
### DISA and DoD Compliance Standards

The Defense Information Systems Agency (DISA) and the Department of Defense (DoD) have established comprehensive security standards to safeguard information systems against cyber threats. These standards, often referred to as the Security Technical Implementation Guide (STIG) configuration standard, provide technical guidance and requirements for achieving robust security measures. By adhering to DISA STIG compliance, organizations ensure that their systems are fortified against potential vulnerabilities that could otherwise leave them susceptible to various cyber risks.

### Implementing Specific Product STIGs

The DISA STIG compliance framework encompasses a wide array of specific product configurations, ranging from operating systems to software applications. Each STIG offers tailored security guidelines for a specific product, addressing potential vulnerabilities and providing step-by-step instructions to enhance system defenses. By meticulously implementing these specific product STIGs, organizations can fortify their hardware and software environments, ensuring that potential weaknesses are adequately addressed. This systematic approach helps create a more secure configuration standard in line with DISA's rigorous technical guidance.

### Strengthening Security with Automated Compliance

Automating the process of DISA STIG compliance is a strategic approach to enhance overall security posture. This automation streamlines the application of numerous configuration changes, reducing the potential for human error and ensuring consistent adherence to security guidelines. The automated approach not only accelerates the compliance process but also strengthens security by swiftly addressing potential vulnerabilities that could otherwise be missed in manual configurations. By utilizing automation tools and scripts, such as the provided PowerShell script, organizations can efficiently implement DISA STIG compliance measures and reduce the window of exposure to cyber threats.

### Critical Role of Hardware and Software Requirements

Hardware and software requirements play a pivotal role in achieving DISA STIG compliance. These requirements encompass various aspects, such as memory integrity, virtualization-based security, and system protection mechanisms. Adhering to these stipulated hardware and software prerequisites is essential for implementing the recommended security controls. Organizations must ensure that their systems meet or exceed these requirements to effectively apply DISA STIG compliance measures. Meeting these prerequisites is a critical step toward establishing a robust defense against potential cyberattacks.

### Safeguarding Against Department of Defense (DoD) Mandates

The Department of Defense (DoD) places paramount importance on information system security to safeguard sensitive data and support mission-critical operations. DISA STIG compliance aligns with DoD mandates, providing a comprehensive framework to enhance security measures across the organization's technological landscape. By implementing DISA STIG compliance, organizations demonstrate their commitment to meeting DoD's stringent security standards. This alignment not only strengthens the organization's cybersecurity posture but also ensures readiness to navigate evolving cyber threats in line with DoD's strategic directives.
