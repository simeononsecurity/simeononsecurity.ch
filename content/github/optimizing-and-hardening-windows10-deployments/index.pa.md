---
title: "ਆਟੋਮੇਟਿਡ ਕੌਂਫਿਗਰੇਸ਼ਨ ਬਦਲਾਅ ਦੇ ਨਾਲ ਵਿੰਡੋਜ਼ 10 ਤੈਨਾਤੀਆਂ ਨੂੰ ਅਨੁਕੂਲ ਬਣਾਓ, ਸਖ਼ਤ ਅਤੇ ਸੁਰੱਖਿਅਤ ਕਰੋ"
date: 2020-07-22
---
 ਹਾਰਡਨ, ਅਤੇ ਡੀਬਲੋਟ ਵਿੰਡੋਜ਼ 10 ਡਿਪਲਾਇਮੈਂਟ**

** ਤੋਂ ਸਾਰੀਆਂ ਲੋੜੀਂਦੀਆਂ ਫਾਈਲਾਂ ਨੂੰ ਡਾਊਨਲੋਡ ਕਰੋ[GitHub Repository](https://github.com/smiltech/Windows-Optimize-Harden-Debloat)

**ਅਸੀਂ ਨਿਮਨਲਿਖਤ ਲਈ ਮਦਦ ਮੰਗ ਰਹੇ ਹਾਂ[.Net issue](https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/3) 

## ਜਾਣ-ਪਛਾਣ:
ਵਿੰਡੋਜ਼ 10 ਬਾਕਸ ਤੋਂ ਬਾਹਰ ਇੱਕ ਹਮਲਾਵਰ ਅਤੇ ਅਸੁਰੱਖਿਅਤ ਓਪਰੇਟਿੰਗ ਸਿਸਟਮ ਹੈ।
ਵਰਗੀਆਂ ਸੰਸਥਾਵਾਂ[PrivacyTools.io](https://PrivacyTools.io), [Microsoft](https://microsoft.com), [Cyber.mil](https://public.cyber.mil), the [Department of Defense](https://dod.gov), and the [National Security Agency](https://www.nsa.gov/) ਨੇ ਓਪਰੇਟਿੰਗ ਸਿਸਟਮ ਨੂੰ ਲੌਕਡਾਊਨ, ਸਖ਼ਤ ਅਤੇ ਸੁਰੱਖਿਅਤ ਕਰਨ ਲਈ ਸੰਰਚਨਾ ਤਬਦੀਲੀਆਂ ਦੀ ਸਿਫ਼ਾਰਸ਼ ਕੀਤੀ ਹੈ। ਇਹ ਤਬਦੀਲੀਆਂ ਟੈਲੀਮੈਟਰੀ ਨੂੰ ਰੋਕਣਾ, ਮੈਕਰੋਜ਼ ਨੂੰ ਰੋਕਣਾ, ਬਲੋਟਵੇਅਰ ਨੂੰ ਹਟਾਉਣਾ, ਅਤੇ ਸਿਸਟਮ ਉੱਤੇ ਬਹੁਤ ਸਾਰੇ ਡਿਜੀਟਲ ਅਤੇ ਭੌਤਿਕ ਹਮਲਿਆਂ ਨੂੰ ਰੋਕਣਾ ਸਮੇਤ ਬਹੁਤ ਸਾਰੀਆਂ ਕਮੀਆਂ ਨੂੰ ਕਵਰ ਕਰਦਾ ਹੈ। ਇਸ ਸਕ੍ਰਿਪਟ ਦਾ ਉਦੇਸ਼ ਉਹਨਾਂ ਸੰਸਥਾਵਾਂ ਦੁਆਰਾ ਸਿਫ਼ਾਰਿਸ਼ ਕੀਤੀਆਂ ਸੰਰਚਨਾਵਾਂ ਨੂੰ ਸਵੈਚਾਲਤ ਕਰਨਾ ਹੈ।

## ਨੋਟ:
- ਇਹ ਸਕ੍ਰਿਪਟ ਮੁੱਖ ਤੌਰ 'ਤੇ **ਨਿੱਜੀ ਵਰਤੋਂ** ਵਾਤਾਵਰਣਾਂ ਵਿੱਚ ਕੰਮ ਕਰਨ ਲਈ ਤਿਆਰ ਕੀਤੀ ਗਈ ਹੈ। ਇਸ ਨੂੰ ਧਿਆਨ ਵਿੱਚ ਰੱਖਦੇ ਹੋਏ, ਕੁਝ ਐਂਟਰਪ੍ਰਾਈਜ਼ ਕੌਂਫਿਗਰੇਸ਼ਨ ਸੈਟਿੰਗਾਂ ਲਾਗੂ ਨਹੀਂ ਕੀਤੀਆਂ ਜਾਂਦੀਆਂ ਹਨ। ਇਹ ਸਕ੍ਰਿਪਟ ਇੱਕ ਸਿਸਟਮ ਨੂੰ 100% ਅਨੁਪਾਲਨ ਵਿੱਚ ਲਿਆਉਣ ਲਈ ਤਿਆਰ ਨਹੀਂ ਕੀਤੀ ਗਈ ਹੈ। ਇਸ ਦੀ ਬਜਾਏ ਇਸਨੂੰ ਜ਼ਿਆਦਾਤਰ ਪੂਰਾ ਕਰਨ ਲਈ ਇੱਕ ਸਟੈਪਿੰਗ ਸਟੋਨ ਵਜੋਂ ਵਰਤਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ, ਜੇ ਸਭ ਨਹੀਂ, ਤਾਂ ਸੰਰਚਨਾ ਤਬਦੀਲੀਆਂ ਜੋ ਕਿ ਬ੍ਰਾਂਡਿੰਗ ਅਤੇ ਬੈਨਰਾਂ ਵਰਗੇ ਪੁਰਾਣੇ ਮੁੱਦਿਆਂ ਨੂੰ ਛੱਡਣ ਵੇਲੇ ਸਕ੍ਰਿਪਟ ਕੀਤੀਆਂ ਜਾ ਸਕਦੀਆਂ ਹਨ ਜਿੱਥੇ ਉਹਨਾਂ ਨੂੰ ਸਖਤ ਨਿੱਜੀ ਵਰਤੋਂ ਵਾਲੇ ਮਾਹੌਲ ਵਿੱਚ ਵੀ ਲਾਗੂ ਨਹੀਂ ਕੀਤਾ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ।
- ਇਸ ਸਕ੍ਰਿਪਟ ਨੂੰ ਇਸ ਤਰੀਕੇ ਨਾਲ ਡਿਜ਼ਾਇਨ ਕੀਤਾ ਗਿਆ ਹੈ ਕਿ ਕੁਝ ਹੋਰ ਸਕ੍ਰਿਪਟਾਂ ਦੇ ਉਲਟ ਓਪਟੀਮਾਈਜੇਸ਼ਨ, ਕੋਰ ਵਿੰਡੋਜ਼ ਕਾਰਜਕੁਸ਼ਲਤਾ ਨੂੰ ਨਹੀਂ ਤੋੜਨਗੀਆਂ।
 - ਵਿੰਡੋਜ਼ ਅੱਪਡੇਟ, ਵਿੰਡੋਜ਼ ਡਿਫੈਂਡਰ, ਵਿੰਡੋਜ਼ ਸਟੋਰ, ਅਤੇ ਕੋਰਟੋਨਾ ਵਰਗੀਆਂ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਨੂੰ ਪ੍ਰਤਿਬੰਧਿਤ ਕੀਤਾ ਗਿਆ ਹੈ, ਪਰ ਜ਼ਿਆਦਾਤਰ ਹੋਰ ਵਿੰਡੋਜ਼ 10 ਗੋਪਨੀਯਤਾ ਸਕ੍ਰਿਪਟਾਂ ਵਾਂਗ ਵਿਗਾੜ ਵਾਲੀ ਸਥਿਤੀ ਵਿੱਚ ਨਹੀਂ ਹਨ।
- ਜੇਕਰ ਤੁਸੀਂ ਸਿਰਫ ਵਪਾਰਕ ਵਾਤਾਵਰਣਾਂ ਨੂੰ ਨਿਸ਼ਾਨਾ ਬਣਾਉਣ ਵਾਲੀ ਇੱਕ ਛੋਟੀ ਜਿਹੀ ਸਕ੍ਰਿਪਟ ਦੀ ਭਾਲ ਕਰਦੇ ਹੋ, ਤਾਂ ਕਿਰਪਾ ਕਰਕੇ ਇਸਨੂੰ ਦੇਖੋ[GitHub Repository](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)

## ਲੋੜਾਂ:
- [X] Windows 10 Enterprise (**Preferred**) ਜਾਂ Windows 10 Professional
  - ਵਿੰਡੋਜ਼ 10 ਹੋਮ ਜੀਪੀਓ ਕੌਂਫਿਗਰੇਸ਼ਨਾਂ ਦੀ ਆਗਿਆ ਨਹੀਂ ਦਿੰਦਾ ਹੈ।
  - ਵਿੰਡੋਜ਼ 10 "ਐਨ" ਐਡੀਸ਼ਨ ਦੀ ਜਾਂਚ ਨਹੀਂ ਕੀਤੀ ਜਾਂਦੀ ਹੈ।
-[X] [Standards](https://docs.microsoft.com/en-us/windows-hardware/design/device-experiences/oem-highly-secure) ਇੱਕ ਬਹੁਤ ਹੀ ਸੁਰੱਖਿਅਤ Windows 10 ਡਿਵਾਈਸ ਲਈ
-[X] System is [fully up to date](https://support.microsoft.com/en-gb/help/4027667/windows-10-update)
  - ਵਰਤਮਾਨ ਵਿੱਚ Windows 10 **v1909**, **v2004**, ਜਾਂ **20H2**।
  - ਚਲਾਓ[Windows 10 Upgrade Assistant](https://support.microsoft.com/en-us/help/3159635/windows-10-update-assistant) ਨਵੀਨਤਮ ਮੁੱਖ ਰੀਲੀਜ਼ ਨੂੰ ਅੱਪਡੇਟ ਕਰਨ ਅਤੇ ਤਸਦੀਕ ਕਰਨ ਲਈ।
- [X] ਇਸ ਸਕ੍ਰਿਪਟ ਨੂੰ ਲਾਗੂ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ ਬਿਟਲੌਕਰ ਨੂੰ ਮੁਅੱਤਲ ਜਾਂ ਬੰਦ ਕੀਤਾ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ, ਇਸਨੂੰ ਰੀਬੂਟ ਕਰਨ ਤੋਂ ਬਾਅਦ ਦੁਬਾਰਾ ਚਾਲੂ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ।
  - ਇਸ ਸਕ੍ਰਿਪਟ ਦੇ ਫਾਲੋ-ਅਪ ਰਨ ਬਿਟਲਾਕਰ ਨੂੰ ਅਯੋਗ ਕੀਤੇ ਬਿਨਾਂ ਚਲਾਇਆ ਜਾ ਸਕਦਾ ਹੈ।
- [X] ਹਾਰਡਵੇਅਰ ਲੋੜਾਂ
  -[Hardware Requirements for Memory Integrity](https://docs.microsoft.com/en-us/windows/security/threat-protection/device-guard/requirements-and-deployment-planning-guidelines-for-virtualization-based-protection-of-code-integrity#baseline-protections) 
  -[Hardware Requirements for Virtualization-Based Security](https://docs.microsoft.com/en-us/windows-hardware/design/device-experiences/oem-vbs)
  -[Hardware Requirements for Windows Defender Application Guard](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-guard/reqs-wd-app-guard)
  -[Hardware Requirements for Windows Defender Credential Guard](https://docs.microsoft.com/en-us/windows/security/identity-protection/credential-guard/credential-guard-requirements)


## ਸਿਫਾਰਸ਼ੀ ਪੜ੍ਹਨ ਸਮੱਗਰੀ:
  -[System Guard Secure Launch](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-system-guard/system-guard-secure-launch-and-smm-protection#requirements-met-by-system-guard-enabled-machines)
  -[System Guard Root of Trust](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-system-guard/system-guard-how-hardware-based-root-of-trust-helps-protect-windows)
  -[Hardware-based Isolation](https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-atp/overview-hardware-based-isolation)
  -[Memory integrity](https://docs.microsoft.com/en-us/windows/security/threat-protection/device-guard/memory-integrity)
  -[Windows Defender Application Guard](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-guard/wd-app-guard-overview)
  -[Windows Defender Credential Guard](https://docs.microsoft.com/en-us/windows/security/identity-protection/credential-guard/credential-guard-how-it-works)

## ਸਕ੍ਰਿਪਟਾਂ ਅਤੇ ਸਾਧਨਾਂ ਦੀ ਇੱਕ ਸੂਚੀ ਜੋ ਇਹ ਸੰਗ੍ਰਹਿ ਵਰਤਦਾ ਹੈ:
-[Cyber.mil - Group Policy Objects](https://public.cyber.mil/stigs/gpo/)
-[Microsoft Security Compliance Toolkit 1.0](https://www.microsoft.com/en-us/download/details.aspx?id=55319)

## ਇਸ ਤੋਂ ਵਧੀਕ ਸੰਰਚਨਾਵਾਂ 'ਤੇ ਵਿਚਾਰ ਕੀਤਾ ਗਿਆ ਸੀ:
-[BuiltByBel - PrivateZilla](https://github.com/builtbybel/privatezilla)
-[CERT - IE Scripting Engine Memory Corruption](https://kb.cert.org/vuls/id/573168/)
-[Dirteam - SSL Hardening](https://dirteam.com/sander/2019/07/30/howto-disable-weak-protocols-cipher-suites-and-hashing-algorithms-on-web-application-proxies-ad-fs-servers-and-windows-servers-running-azure-ad-connect/)
-[Microsoft - Managing Windows 10 Telemetry and Callbacks](https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services)
-[Microsoft - Reduce attack surfaces with attack surface reduction rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-atp/attack-surface-reduction)
-[Microsoft - Recommended block rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules)
-[Microsoft - Recommended driver block rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules)
-[Microsoft - Specture and Meltdown Mitigations](https://support.microsoft.com/en-us/help/4072698/windows-server-speculative-execution-side-channel-vulnerabilities)
-[Microsoft - Windows 10 Privacy](https://docs.microsoft.com/en-us/windows/privacy/)
-[Microsoft - Windows 10 VDI Recomendations](https://docs.microsoft.com/en-us/windows-server/remote/remote-desktop-services/rds_vdi-recommendations-1909)
-[Microsoft - Windows Defender Application Control](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/windows-defender-application-control-design-guide)
-[Mirinsoft - SharpApp](https://github.com/builtbybel/sharpapp)
-[Mirinsoft - debotnet](https://github.com/builtbybel/debotnet)
-[NSACyber - Application Whitelisting Using Microsoft AppLocker](https://apps.nsa.gov/iad/library/ia-guidance/tech-briefs/application-whitelisting-using-microsoft-applocker.cfm)
-[NSACyber - Bitlocker Guidance](https://github.com/nsacyber/BitLocker-Guidance)
-[NSACyber - Hardware-and-Firmware-Security-Guidance](https://github.com/nsacyber/Hardware-and-Firmware-Security-Guidance)
-[NSACyber - Windows Secure Host Baseline](https://github.com/nsacyber/Windows-Secure-Host-Baseline)
-[UnderGroundWires - Privacy.S**Y](https://github.com/undergroundwires/privacy.sexy)
-[Sycnex - Windows10Debloater](https://github.com/Sycnex/Windows10Debloater)
-[The-Virtual-Desktop-Team - Virtual-Desktop-Optimization-Tool](https://github.com/The-Virtual-Desktop-Team/Virtual-Desktop-Optimization-Tool)
-[TheVDIGuys - Windows 10 VDI Optimize](https://github.com/TheVDIGuys/Windows_10_VDI_Optimize)
-[W4H4WK - Debloat Windows 10](https://github.com/W4RH4WK/Debloat-Windows-10/tree/master/scripts)
-[Whonix - Disable TCP Timestamps](https://www.whonix.org/wiki/Disable_TCP_and_ICMP_Timestamps)

## STIGS/SRGs ਲਾਗੂ:
-[Adobe Reader Pro DC Classic V1R3](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Adobe_Acrobat_Pro_DC_Continuous_V1R2_STIG.zip)
-[Adobe Reader Pro DC Continous V1R2](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Adobe_Acrobat_Pro_DC_Classic_V1R3_STIG.zip)
-[Firefox V4R29](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MOZ_FireFox_V4R29_STIG.zip)
-[Google Chrome V1R19](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Google_Chrome_V1R19_STIG.zip)
-[Internet Explorer 11 V1R19](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MS_IE11_V1R19_STIG.zip)
-[Microsoft .Net Framework 4 V1R9](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MS_DotNet_Framework_4-0_V1R9_STIG.zip) - **ਕੰਮ ਚੱਲ ਰਿਹਾ ਹੈ**
-[Microsoft Office 2013 V1R5](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MicrosoftOffice2013_V1R5_Overview.zip)
-[Microsoft Office 2016 V1R2](https://dl.dod.cyber.mil/wp-content/uploads/stigs/pdf/U_Microsoft_Office_2016_V1R2_Overview.pdf)
-[Microsoft Office 2019/Office 365 Pro Plus V1R2](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MS_Office_365_ProPlus_V1R2_STIG.zip)
-[Microsoft OneDrive STIG V2R1](https://dl.cyber.mil/stigs/zip/U_MS_OneDrive_V2R1_STIG.zip)
-[Oracle JRE 8 V1R5](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Oracle_JRE_8_Windows_V1R5_STIG.zip)
-[Windows 10 V2R1](https://dl.cyber.mil/stigs/zip/U_MS_Windows_Defender_Antivirus_V2R1_STIG.zip)
-[Windows Defender Antivirus V2R1](https://dl.cyber.mil/stigs/zip/U_MS_Windows_Defender_Antivirus_V2R1_STIG.zip)
-[Windows Firewall V1R7](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Windows_Firewall_V1R7_STIG.zip)

## ਸਕ੍ਰਿਪਟ ਨੂੰ ਕਿਵੇਂ ਚਲਾਉਣਾ ਹੈ
### ਦਸਤੀ ਸਥਾਪਨਾ:
ਜੇਕਰ ਮੈਨੂਅਲੀ ਡਾਉਨਲੋਡ ਕੀਤੀ ਜਾਂਦੀ ਹੈ, ਤਾਂ ਸਕ੍ਰਿਪਟ ਨੂੰ ਡਾਇਰੈਕਟਰੀ ਵਿੱਚ ਇੱਕ ਪ੍ਰਬੰਧਕੀ ਪਾਵਰਸ਼ੇਲ ਤੋਂ ਲਾਂਚ ਕੀਤਾ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ ਜਿਸ ਵਿੱਚ ਸਾਰੀਆਂ ਫਾਈਲਾਂ ਸ਼ਾਮਲ ਹਨ।[GitHub Repository](https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat)
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
Get-ChildItem -Recurse *.ps1 | Unblock-File
.\sos-optimize-windows.ps1
```
### Automated Install:
The script may be launched from the extracted GitHub download like this:
```powershell
iex ((New-Object System.Net.WebClient).DownloadString('https://simeononsecurity.ch/scripts/windowsoptimizeandharden.ps1'))
```<img src="https://raw.githubusercontent.com/simeononsecurity/Windows-Optimize-Harden-Debloat/master/.github/images/w10automatic.gif" alt="ਵਿੰਡੋਜ਼-ਓਪਟੀਮਾਈਜ਼-ਹਾਰਡਨ-ਡੀਬਲੋਟ ਆਟੋਮੈਟਿਕ ਸਥਾਪਨਾ ਦੀ ਉਦਾਹਰਨ">