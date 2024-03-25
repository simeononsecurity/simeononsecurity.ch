---
title: "Powershell ਸਕ੍ਰਿਪਟ ਦੇ ਨਾਲ Windows 10 STIG ਪਾਲਣਾ ਨੂੰ ਸਵੈਚਾਲਤ ਕਰਨਾ"
date: 2020-08-26
---

** ਤੋਂ ਸਾਰੀਆਂ ਲੋੜੀਂਦੀਆਂ ਫਾਈਲਾਂ ਨੂੰ ਡਾਊਨਲੋਡ ਕਰੋ[GitHub Repository](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)

**ਅਸੀਂ ਨਿਮਨਲਿਖਤ ਲਈ ਮਦਦ ਮੰਗ ਰਹੇ ਹਾਂ[.Net issue](https://github.com/simeononsecurity/W10-Optimize-and-Harden/issues/3) 

## ਜਾਣ-ਪਛਾਣ:

Windows 10 ਬਾਕਸ ਤੋਂ ਬਾਹਰ ਅਸੁਰੱਖਿਅਤ ਓਪਰੇਟਿੰਗ ਸਿਸਟਮ ਹੈ ਅਤੇ ਬੀਮੇ ਲਈ ਬਹੁਤ ਸਾਰੇ ਬਦਲਾਅ ਦੀ ਲੋੜ ਹੈ[FISMA](https://www.cisa.gov/federal-information-security-modernization-act) ਪਾਲਣਾ
ਵਰਗੀਆਂ ਸੰਸਥਾਵਾਂ[Microsoft](https://microsoft.com), [Cyber.mil](https://public.cyber.mil), the [Department of Defense](https://www.defense.gov/), and the [National Security Agency](https://www.nsa.gov/) ਨੇ ਓਪਰੇਟਿੰਗ ਸਿਸਟਮ ਨੂੰ ਲਾਕਡਾਊਨ, ਸਖ਼ਤ ਅਤੇ ਸੁਰੱਖਿਅਤ ਕਰਨ ਅਤੇ ਸਰਕਾਰੀ ਪਾਲਣਾ ਨੂੰ ਯਕੀਨੀ ਬਣਾਉਣ ਲਈ ਸੰਰਚਨਾ ਤਬਦੀਲੀਆਂ ਦੀ ਸਿਫ਼ਾਰਸ਼ ਕੀਤੀ ਹੈ ਅਤੇ ਲੋੜੀਂਦਾ ਹੈ। ਇਹ ਤਬਦੀਲੀਆਂ ਟੈਲੀਮੈਟਰੀ ਨੂੰ ਰੋਕਣਾ, ਮੈਕਰੋਜ਼ ਨੂੰ ਰੋਕਣਾ, ਬਲੋਟਵੇਅਰ ਨੂੰ ਹਟਾਉਣਾ, ਅਤੇ ਸਿਸਟਮ ਉੱਤੇ ਬਹੁਤ ਸਾਰੇ ਭੌਤਿਕ ਹਮਲਿਆਂ ਨੂੰ ਰੋਕਣਾ ਸਮੇਤ ਬਹੁਤ ਸਾਰੀਆਂ ਕਮੀਆਂ ਨੂੰ ਕਵਰ ਕਰਦਾ ਹੈ।

ਸਟੈਂਡਅਲੋਨ ਸਿਸਟਮ ਸੁਰੱਖਿਅਤ ਕਰਨ ਲਈ ਕੁਝ ਸਭ ਤੋਂ ਮੁਸ਼ਕਲ ਅਤੇ ਤੰਗ ਕਰਨ ਵਾਲੇ ਸਿਸਟਮ ਹਨ। ਸਵੈਚਲਿਤ ਨਾ ਹੋਣ 'ਤੇ, ਉਹਨਾਂ ਨੂੰ ਹਰੇਕ STIG/SRG ਦੇ ਦਸਤੀ ਬਦਲਾਅ ਦੀ ਲੋੜ ਹੁੰਦੀ ਹੈ। ਇੱਕ ਆਮ ਤੈਨਾਤੀ 'ਤੇ ਕੁੱਲ 1000 ਤੋਂ ਵੱਧ ਸੰਰਚਨਾ ਤਬਦੀਲੀਆਂ ਅਤੇ ਔਸਤਨ 5 ਮਿੰਟ ਪ੍ਰਤੀ ਤਬਦੀਲੀ 3.5 ਦਿਨਾਂ ਦੇ ਕੰਮ ਦੇ ਬਰਾਬਰ ਹੈ। ਇਸ ਸਕ੍ਰਿਪਟ ਦਾ ਉਦੇਸ਼ ਉਸ ਪ੍ਰਕਿਰਿਆ ਨੂੰ ਮਹੱਤਵਪੂਰਨ ਤੌਰ 'ਤੇ ਤੇਜ਼ ਕਰਨਾ ਹੈ।

## ਨੋਟ:

- ਇਹ ਸਕ੍ਰਿਪਟ **ਐਂਟਰਪ੍ਰਾਈਜ਼** ਵਾਤਾਵਰਨ ਵਿੱਚ ਕੰਮ ਕਰਨ ਲਈ ਤਿਆਰ ਕੀਤੀ ਗਈ ਹੈ ਅਤੇ ਇਹ ਮੰਨਦੀ ਹੈ ਕਿ ਤੁਹਾਡੇ ਕੋਲ ਸਾਰੀਆਂ ਲੋੜਾਂ ਲਈ ਹਾਰਡਵੇਅਰ ਸਮਰਥਨ ਹੈ।
  - ਨਿੱਜੀ ਪ੍ਰਣਾਲੀਆਂ ਲਈ ਕਿਰਪਾ ਕਰਕੇ ਇਸਨੂੰ ਦੇਖੋ[GitHub Repository](https://github.com/simeononsecurity/W10-Optimize-and-Harden)
- ਇਹ ਸਕ੍ਰਿਪਟ ਇੱਕ ਸਿਸਟਮ ਨੂੰ 100% ਅਨੁਪਾਲਨ ਵਿੱਚ ਲਿਆਉਣ ਲਈ ਤਿਆਰ ਨਹੀਂ ਕੀਤੀ ਗਈ ਹੈ, ਸਗੋਂ ਇਸਨੂੰ ਜ਼ਿਆਦਾਤਰ ਨੂੰ ਪੂਰਾ ਕਰਨ ਲਈ ਇੱਕ ਸਟੈਪਿੰਗ ਸਟੋਨ ਵਜੋਂ ਵਰਤਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ, ਜੇਕਰ ਸਭ ਨਹੀਂ, ਤਾਂ ਸੰਰਚਨਾ ਵਿੱਚ ਤਬਦੀਲੀਆਂ ਜੋ ਸਕਰਿਪਟ ਕੀਤੀਆਂ ਜਾ ਸਕਦੀਆਂ ਹਨ।
  - ਮਾਇਨਸ ਸਿਸਟਮ ਦਸਤਾਵੇਜ਼, ਇਹ ਸੰਗ੍ਰਹਿ ਤੁਹਾਨੂੰ ਲਾਗੂ ਕੀਤੇ ਗਏ ਸਾਰੇ STIGS/SRGs 'ਤੇ ਲਗਭਗ 95% ਪਾਲਣਾ ਲਿਆਉਣਾ ਚਾਹੀਦਾ ਹੈ।

## ਲੋੜਾਂ:
- [X] Windows 10 ਐਂਟਰਪ੍ਰਾਈਜ਼ ਪ੍ਰਤੀ STIG **ਲੋੜੀਂਦਾ** ਹੈ।
-[x] [Standards](https://docs.microsoft.com/en-us/windows-hardware/design/device-experiences/oem-highly-secure) ਇੱਕ ਬਹੁਤ ਹੀ ਸੁਰੱਖਿਅਤ Windows 10 ਡਿਵਾਈਸ ਲਈ
-[x] System is [fully up to date](https://support.microsoft.com/en-gb/help/4027667/windows-10-update)
  - ਵਰਤਮਾਨ ਵਿੱਚ Windows 10 **v1909** ਜਾਂ **v2004**।
  - ਚਲਾਓ[Windows 10 Upgrade Assistant](https://support.microsoft.com/en-us/help/3159635/windows-10-update-assistant) ਨਵੀਨਤਮ ਮੁੱਖ ਰੀਲੀਜ਼ ਨੂੰ ਅਪਡੇਟ ਕਰਨ ਅਤੇ ਤਸਦੀਕ ਕਰਨ ਲਈ।
- [X] ਹਾਰਡਵੇਅਰ ਲੋੜਾਂ
  -[Hardware Requirements for Memory Integrity](https://docs.microsoft.com/en-us/windows/security/threat-protection/device-guard/requirements-and-deployment-planning-guidelines-for-virtualization-based-protection-of-code-integrity#baseline-protections) 
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

-[Microsoft Security Compliance Toolkit 1.0](https://www.microsoft.com/en-us/download/details.aspx?id=55319)

-[Cyber.mil - Group Policy Objects](https://public.cyber.mil/stigs/gpo/)

-[NSACyber - Bitlocker Guidance](https://github.com/nsacyber/BitLocker-Guidance)

## ਇਸ ਤੋਂ ਵਧੀਕ ਸੰਰਚਨਾਵਾਂ 'ਤੇ ਵਿਚਾਰ ਕੀਤਾ ਗਿਆ ਸੀ:

-[NSACyber - Hardware-and-Firmware-Security-Guidance](https://github.com/nsacyber/Hardware-and-Firmware-Security-Guidance)

-[NSACyber - Application Whitelisting Using Microsoft AppLocker](https://apps.nsa.gov/iad/library/ia-guidance/tech-briefs/application-whitelisting-using-microsoft-applocker.cfm)

## STIGS/SRGs ਲਾਗੂ:
 
-[Windows 10 V1R23](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MS_Windows_10_V1R23_STIG.zip)

-[Windows Defender Antivirus V1R9](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MS_Windows_Defender_Antivirus_V1R9_STIG.zip)

-[Windows Firewall V1R7](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Windows_Firewall_V1R7_STIG.zip)

-[Internet Explorer 11 V1R19](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MS_IE11_V1R19_STIG.zip)

-[Adobe Reader Pro DC Continous V1R2](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Adobe_Acrobat_Pro_DC_Continuous_V1R2_STIG.zip)

-[Microsoft Office 2019/Office 365 Pro Plus V1R2](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MS_Office_365_ProPlus_V1R2_STIG.zip)

-[Microsoft Office 2016 V1R2](https://dl.dod.cyber.mil/wp-content/uploads/stigs/pdf/U_Microsoft_Office_2016_V1R2_Overview.pdf)

-[Microsoft Office 2013 V1R5](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MicrosoftOffice2013_V1R5_Overview.zip)

-[Google Chrome V1R19](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Google_Chrome_V1R19_STIG.zip)

-[Firefox V4R29](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MOZ_FireFox_V4R29_STIG.zip)

-[Microsoft .Net Framework 4 V1R9](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MS_DotNet_Framework_4-0_V1R9_STIG.zip) - **ਕੰਮ ਚੱਲ ਰਿਹਾ ਹੈ**

-[Oracle JRE 8 V1R5](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Oracle_JRE_8_Windows_V1R5_STIG.zip)

## ਸਕ੍ਰਿਪਟ ਨੂੰ ਕਿਵੇਂ ਚਲਾਉਣਾ ਹੈ

**ਸਕ੍ਰਿਪਟ ਨੂੰ ਇਸ ਤਰ੍ਹਾਂ ਐਕਸਟਰੈਕਟ ਕੀਤੇ GitHub ਡਾਊਨਲੋਡ ਤੋਂ ਲਾਂਚ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ:**
```
.\secure-standalone.ps1
```
ਸਕ੍ਰਿਪਟ ਜੋ ਅਸੀਂ ਵਰਤ ਰਹੇ ਹਾਂ, ਉਸ ਡਾਇਰੈਕਟਰੀ ਤੋਂ ਲਾਂਚ ਕੀਤੀ ਜਾਣੀ ਚਾਹੀਦੀ ਹੈ ਜਿਸ ਵਿੱਚ ਹੋਰ ਸਾਰੀਆਂ ਫਾਈਲਾਂ ਸ਼ਾਮਲ ਹਨ[GitHub Repository](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)
