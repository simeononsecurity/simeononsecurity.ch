---
title: "STIG ਅਨੁਕੂਲ GPOs ਦੇ ਨਾਲ ਵਿੰਡੋਜ਼ ਡੋਮੇਨ ਦੀ ਪਾਲਣਾ ਨੂੰ ਆਟੋਮੈਟਿਕ ਕਰੋ"
date: 2020-09-08
---

ਤੁਹਾਡੇ ਡੋਮੇਨ ਨੂੰ ਸਾਰੇ ਲਾਗੂ STIGs ਅਤੇ SRGs ਨਾਲ ਅਨੁਕੂਲ ਬਣਾਉਣ ਵਿੱਚ ਸਹਾਇਤਾ ਲਈ SimeonOnSecurity ਦੁਆਰਾ ਪ੍ਰਦਾਨ ਕੀਤੇ ਗਏ ਸਾਰੇ GPOs ਨੂੰ ਆਯਾਤ ਕਰੋ।

## ਨੋਟ:

**ਇਹ ਸਕ੍ਰਿਪਟ ਐਂਟਰਪ੍ਰਾਈਜ਼ ਵਾਤਾਵਰਨ ਵਿੱਚ ਵਰਤਣ ਲਈ ਤਿਆਰ ਕੀਤੀ ਗਈ ਹੈ**

## STIGS/SRGs ਲਾਗੂ:
 
-[Windows 10 V1R23](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MS_Windows_10_V1R23_STIG.zip)

-[Windows Defender Antivirus V1R9](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MS_Windows_Defender_Antivirus_V1R9_STIG.zip)

-[Windows Firewall V1R7](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Windows_Firewall_V1R7_STIG.zip)

-[Internet Explorer 11 V1R19](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MS_IE11_V1R19_STIG.zip)

-[Adobe Reader Pro DC Continous V1R2](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Adobe_Acrobat_Pro_DC_Classic_V1R3_STIG.zip)

-[Adobe Reader Pro DC Classic V1R3](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Adobe_Acrobat_Pro_DC_Continuous_V1R2_STIG.zip)

-[Microsoft Office 2019/Office 365 Pro Plus V1R2](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MS_Office_365_ProPlus_V1R2_STIG.zip)

-[Microsoft Office 2016 V1R2](https://dl.dod.cyber.mil/wp-content/uploads/stigs/pdf/U_Microsoft_Office_2016_V1R2_Overview.pdf)

-[Microsoft Office 2013 V1R5](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MicrosoftOffice2013_V1R5_Overview.zip)

-[Google Chrome V1R19](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Google_Chrome_V1R19_STIG.zip)

-[Firefox V4R29](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MOZ_FireFox_V4R29_STIG.zip)

-[Microsoft .Net Framework 4 V1R9](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MS_DotNet_Framework_4-0_V1R9_STIG.zip) - **ਕੰਮ ਚੱਲ ਰਿਹਾ ਹੈ**

-[Oracle JRE 8 V1R5](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Oracle_JRE_8_Windows_V1R5_STIG.zip)

## ਇਸ ਤੋਂ ਵਧੀਕ ਸੰਰਚਨਾਵਾਂ 'ਤੇ ਵਿਚਾਰ ਕੀਤਾ ਗਿਆ ਸੀ:

-[NSACyber - Hardware-and-Firmware-Security-Guidance](https://github.com/nsacyber/Hardware-and-Firmware-Security-Guidance)

-[NSACyber - Application Whitelisting Using Microsoft AppLocker](https://apps.nsa.gov/iad/library/ia-guidance/tech-briefs/application-whitelisting-using-microsoft-applocker.cfm)

-[Whonix - Disable TCP Timestamps](https://www.whonix.org/wiki/Disable_TCP_and_ICMP_Timestamps)

-[CERT - IE Scripting Engine Memory Corruption](https://kb.cert.org/vuls/id/573168/)

-[Dirteam - SSL Hardening](https://dirteam.com/sander/2019/07/30/howto-disable-weak-protocols-cipher-suites-and-hashing-algorithms-on-web-application-proxies-ad-fs-servers-and-windows-servers-running-azure-ad-connect/)

-[Microsoft - Specture and Meltdown Mitigations](https://support.microsoft.com/en-us/help/4072698/windows-server-speculative-execution-side-channel-vulnerabilities)

-[Microsoft - Windows 10 Privacy](https://docs.microsoft.com/en-us/windows/privacy/)

-[Microsoft - Managing Windows 10 Telemetry and Callbacks](https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services)

-[Microsoft - Windows 10 VDI Recomendations](https://docs.microsoft.com/en-us/windows-server/remote/remote-desktop-services/rds_vdi-recommendations-1909)

## ਸਕ੍ਰਿਪਟ ਨੂੰ ਕਿਵੇਂ ਚਲਾਉਣਾ ਹੈ:

**ਸਕ੍ਰਿਪਟ ਨੂੰ ਇਸ ਤਰ੍ਹਾਂ ਐਕਸਟਰੈਕਟ ਕੀਤੇ GitHub ਡਾਊਨਲੋਡ ਤੋਂ ਲਾਂਚ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ:**
```
.\sos-stig-compliant-domain-prep.ps1
```
ਸਕ੍ਰਿਪਟ ਜੋ ਅਸੀਂ ਵਰਤ ਰਹੇ ਹਾਂ ਉਸ ਡਾਇਰੈਕਟਰੀ ਤੋਂ ਲਾਂਚ ਕੀਤੀ ਜਾਣੀ ਚਾਹੀਦੀ ਹੈ ਜਿਸ ਵਿੱਚ ਹੋਰ ਸਾਰੀਆਂ ਫਾਈਲਾਂ ਸ਼ਾਮਲ ਹਨ[GitHub Repository](https://github.com/simeononsecurity/STIG-Compliant-Domain-Prep)


