---
title: "STIG ਸਕ੍ਰਿਪਟਾਂ ਦੇ ਨਾਲ ਵਿੰਡੋਜ਼ ਸਰਵਰ STIG ਪਾਲਣਾ ਨੂੰ ਸਵੈਚਾਲਤ ਕਰਨਾ"
date: 2020-09-09
---

** ਤੋਂ ਸਾਰੀਆਂ ਲੋੜੀਂਦੀਆਂ ਫਾਈਲਾਂ ਨੂੰ ਡਾਊਨਲੋਡ ਕਰੋ[GitHub Repository](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)

**ਨੋਟ:** ਇਹ ਸਕ੍ਰਿਪਟ ਜ਼ਿਆਦਾਤਰ, ਜੇਕਰ ਸਾਰੇ ਨਹੀਂ, ਬਿਨਾਂ ਕਿਸੇ ਸਮੱਸਿਆ ਦੇ ਸਿਸਟਮਾਂ ਲਈ ਕੰਮ ਕਰੇਗੀ। ਜਦਕਿ[@SimeonOnSecurity](https://github.com/simeononsecurity) creates, reviews, and tests each repo intensively, we can not test every possible configuration nor does [@SimeonOnSecurity](https://github.com/simeononsecurity) take any responsibility for breaking your system. If something goes wrong, be prepared to submit an [issue](../../issues) ਇਸ ਸਕ੍ਰਿਪਟ ਨੂੰ ਨਾ ਚਲਾਓ ਜੇਕਰ ਤੁਸੀਂ ਇਹ ਨਹੀਂ ਸਮਝਦੇ ਕਿ ਇਹ ਕੀ ਕਰਦੀ ਹੈ। ਇਸ ਨੂੰ ਚਲਾਉਣ ਤੋਂ ਪਹਿਲਾਂ ਸਕ੍ਰਿਪਟ ਦੀ ਸਮੀਖਿਆ ਅਤੇ ਜਾਂਚ ਕਰਨਾ ਤੁਹਾਡੀ ਜ਼ਿੰਮੇਵਾਰੀ ਹੈ।

## ਜਵਾਬ:
ਅਸੀਂ ਹੁਣ ਇਸ ਸਕ੍ਰਿਪਟ ਲਈ ਪਲੇਬੁੱਕ ਸੰਗ੍ਰਹਿ ਦੀ ਪੇਸ਼ਕਸ਼ ਕਰਦੇ ਹਾਂ। ਕਿਰਪਾ ਕਰਕੇ ਹੇਠ ਲਿਖੇ ਨੂੰ ਵੇਖੋ:
-[Github Repo](https://github.com/simeononsecurity/Windows_STIG_Ansible)
-[Ansible Galaxy](https://galaxy.ansible.com/simeononsecurity/windows_stigs)

## ਜਾਣ-ਪਛਾਣ:

Windows 10 ਬਾਕਸ ਤੋਂ ਬਾਹਰ ਅਸੁਰੱਖਿਅਤ ਓਪਰੇਟਿੰਗ ਸਿਸਟਮ ਹੈ ਅਤੇ ਬੀਮੇ ਲਈ ਬਹੁਤ ਸਾਰੇ ਬਦਲਾਅ ਦੀ ਲੋੜ ਹੈ[FISMA](https://www.cisa.gov/federal-information-security-modernization-act) ਪਾਲਣਾ
ਵਰਗੀਆਂ ਸੰਸਥਾਵਾਂ[Microsoft](https://microsoft.com), [Cyber.mil](https://public.cyber.mil), the [Department of Defense](https://www.defense.gov/), and the [National Security Agency](https://www.nsa.gov/) ਨੇ ਓਪਰੇਟਿੰਗ ਸਿਸਟਮ ਨੂੰ ਲਾਕਡਾਊਨ, ਸਖ਼ਤ ਅਤੇ ਸੁਰੱਖਿਅਤ ਕਰਨ ਅਤੇ ਸਰਕਾਰੀ ਪਾਲਣਾ ਨੂੰ ਯਕੀਨੀ ਬਣਾਉਣ ਲਈ ਸੰਰਚਨਾ ਤਬਦੀਲੀਆਂ ਦੀ ਸਿਫ਼ਾਰਸ਼ ਕੀਤੀ ਹੈ ਅਤੇ ਲੋੜੀਂਦਾ ਹੈ। ਇਹ ਤਬਦੀਲੀਆਂ ਟੈਲੀਮੈਟਰੀ ਨੂੰ ਰੋਕਣਾ, ਮੈਕਰੋਜ਼ ਨੂੰ ਰੋਕਣਾ, ਬਲੋਟਵੇਅਰ ਨੂੰ ਹਟਾਉਣਾ, ਅਤੇ ਸਿਸਟਮ ਉੱਤੇ ਬਹੁਤ ਸਾਰੇ ਭੌਤਿਕ ਹਮਲਿਆਂ ਨੂੰ ਰੋਕਣਾ ਸਮੇਤ ਬਹੁਤ ਸਾਰੀਆਂ ਕਮੀਆਂ ਨੂੰ ਕਵਰ ਕਰਦਾ ਹੈ।

ਸਟੈਂਡਅਲੋਨ ਸਿਸਟਮ ਸੁਰੱਖਿਅਤ ਕਰਨ ਲਈ ਕੁਝ ਸਭ ਤੋਂ ਮੁਸ਼ਕਲ ਅਤੇ ਤੰਗ ਕਰਨ ਵਾਲੇ ਸਿਸਟਮ ਹਨ। ਸਵੈਚਲਿਤ ਨਾ ਹੋਣ 'ਤੇ, ਉਹਨਾਂ ਨੂੰ ਹਰੇਕ STIG/SRG ਦੇ ਦਸਤੀ ਬਦਲਾਅ ਦੀ ਲੋੜ ਹੁੰਦੀ ਹੈ। ਇੱਕ ਆਮ ਤੈਨਾਤੀ 'ਤੇ ਕੁੱਲ 1000 ਤੋਂ ਵੱਧ ਸੰਰਚਨਾ ਤਬਦੀਲੀਆਂ ਅਤੇ ਔਸਤਨ 5 ਮਿੰਟ ਪ੍ਰਤੀ ਤਬਦੀਲੀ 3.5 ਦਿਨਾਂ ਦੇ ਕੰਮ ਦੇ ਬਰਾਬਰ ਹੈ। ਇਸ ਸਕ੍ਰਿਪਟ ਦਾ ਉਦੇਸ਼ ਉਸ ਪ੍ਰਕਿਰਿਆ ਨੂੰ ਮਹੱਤਵਪੂਰਨ ਤੌਰ 'ਤੇ ਤੇਜ਼ ਕਰਨਾ ਹੈ।

## ਨੋਟ:

- ਇਹ ਸਕ੍ਰਿਪਟ **ਐਂਟਰਪ੍ਰਾਈਜ਼** ਵਾਤਾਵਰਣਾਂ ਵਿੱਚ ਸੰਚਾਲਨ ਲਈ ਤਿਆਰ ਕੀਤੀ ਗਈ ਹੈ ਅਤੇ ਇਹ ਮੰਨਦੀ ਹੈ ਕਿ ਤੁਹਾਡੇ ਕੋਲ ਸਾਰੀਆਂ ਲੋੜਾਂ ਲਈ ਹਾਰਡਵੇਅਰ ਸਮਰਥਨ ਹੈ।
  - ਨਿੱਜੀ ਪ੍ਰਣਾਲੀਆਂ ਲਈ ਕਿਰਪਾ ਕਰਕੇ ਇਸਨੂੰ ਦੇਖੋ[GitHub Repository](https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat)
- ਇਹ ਸਕ੍ਰਿਪਟ ਇੱਕ ਸਿਸਟਮ ਨੂੰ 100% ਅਨੁਪਾਲਨ ਵਿੱਚ ਲਿਆਉਣ ਲਈ ਤਿਆਰ ਨਹੀਂ ਕੀਤੀ ਗਈ ਹੈ, ਸਗੋਂ ਇਸਨੂੰ ਜ਼ਿਆਦਾਤਰ ਨੂੰ ਪੂਰਾ ਕਰਨ ਲਈ ਇੱਕ ਸਟੈਪਿੰਗ ਸਟੋਨ ਵਜੋਂ ਵਰਤਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ, ਜੇਕਰ ਸਭ ਨਹੀਂ, ਤਾਂ ਸੰਰਚਨਾ ਵਿੱਚ ਤਬਦੀਲੀਆਂ ਜੋ ਸਕਰਿਪਟ ਕੀਤੀਆਂ ਜਾ ਸਕਦੀਆਂ ਹਨ।
  - ਮਾਇਨਸ ਸਿਸਟਮ ਦਸਤਾਵੇਜ਼, ਇਹ ਸੰਗ੍ਰਹਿ ਤੁਹਾਨੂੰ ਲਾਗੂ ਕੀਤੇ ਗਏ ਸਾਰੇ STIGS/SRGs 'ਤੇ ਲਗਭਗ 95% ਪਾਲਣਾ ਲਿਆਉਣਾ ਚਾਹੀਦਾ ਹੈ।

## ਲੋੜਾਂ:
- [X] Windows 10 ਐਂਟਰਪ੍ਰਾਈਜ਼ ਪ੍ਰਤੀ STIG ਦੀ ਲੋੜ ਹੈ।
-[X] [Standards](https://docs.microsoft.com/en-us/windows-hardware/design/device-experiences/oem-highly-secure) ਇੱਕ ਬਹੁਤ ਹੀ ਸੁਰੱਖਿਅਤ Windows 10 ਡਿਵਾਈਸ ਲਈ
-[X] System is [fully up to date](https://support.microsoft.com/en-gb/help/4027667/windows-10-update)
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
-[Microsoft - Recommended block rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules)
-[Microsoft - Recommended driver block rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules)
-[Microsoft - Windows Defender Application Control](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/windows-defender-application-control-design-guide)
-[NSACyber - Application Whitelisting Using Microsoft AppLocker](https://apps.nsa.gov/iad/library/ia-guidance/tech-briefs/application-whitelisting-using-microsoft-applocker.cfm)
-[NSACyber - Hardware-and-Firmware-Security-Guidance](https://github.com/nsacyber/Hardware-and-Firmware-Security-Guidance)
-[NSACyber - Windows Secure Host Baseline](https://github.com/nsacyber/Windows-Secure-Host-Baseline)

## STIGS/SRGs ਲਾਗੂ:
-[Adobe Acrobat Pro DC Continuous V2R1](https://public.cyber.mil/stigs/downloads/)
-[Adobe Acrobat Reader DC Continuous V2R1](https://public.cyber.mil/stigs/downloads/)
-[Firefox V5R2](https://public.cyber.mil/stigs/downloads/)
-[Google Chrome V2R4](https://public.cyber.mil/stigs/downloads/)
-[Internet Explorer 11 V1R19](https://public.cyber.mil/stigs/downloads/)
-[Microsoft Edge V1R2](https://public.cyber.mil/stigs/downloads/)
-[Microsoft .Net Framework 4 V1R9](https://public.cyber.mil/stigs/downloads/)
-[Microsoft Office 2013 V2R1](https://public.cyber.mil/stigs/downloads/)
-[Microsoft Office 2016 V2R1](https://public.cyber.mil/stigs/downloads/)
-[Microsoft Office 2019/Office 365 Pro Plus V2R3](https://public.cyber.mil/stigs/downloads/)
-[Microsoft OneDrive STIG V2R1](https://public.cyber.mil/stigs/downloads/)
-[Oracle JRE 8 V1R5](https://public.cyber.mil/stigs/downloads/)
-[Windows 10 V2R2](https://public.cyber.mil/stigs/downloads/)
-[Windows Firewall V1R7](https://public.cyber.mil/stigs/downloads/)

## ਤੱਥਾਂ ਤੋਂ ਬਾਅਦ ਸਥਾਨਕ ਸਮੂਹ ਨੀਤੀ ਵਿੱਚ ਨੀਤੀਆਂ ਨੂੰ ਸੰਪਾਦਿਤ ਕਰਨਾ:
- ਇਸ ਤੋਂ ADMX ਨੀਤੀ ਪਰਿਭਾਸ਼ਾਵਾਂ ਨੂੰ ਆਯਾਤ ਕਰੋ[repo](https://github.com/simeononsecurity/STIG-Compliant-Domain-Prep/tree/master/Files/PolicyDefinitions) ਜਿਸ ਸਿਸਟਮ ਨੂੰ ਤੁਸੀਂ ਸੋਧਣ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰ ਰਹੇ ਹੋ ਉਸ 'ਤੇ *C:\windows\PolicyDefinitions* ਵਿੱਚ।
- ਖੋਲ੍ਹੋ```gpedit.msc``` on on the system you're trying to modify. 


## How to run the script:
### Automated Install:
The script may be launched from the extracted GitHub download like this:
```powershell
iex ((New-Object System.Net.WebClient).DownloadString('https://simeononsecurity.com/scripts/standalonewindows.ps1'))
```

### Manual Install:
If manually downloaded, the script must be launched from the directory containing all the other files from the [GitHub Repository](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)

All of the parameters in the "secure-standalone.ps1" script are optional, with a default value of $true. This means that if no value is specified for a parameter when the script is run, it will be treated as if it were set to $true.

The script takes the following parameters, all of which are optional and default to $true if not specified:

- **cleargpos**: (Boolean) Clear GPOs not being used
- **installupdates**: (Boolean) Install updates and reboot if necessary
- **adobe**: (Boolean) STIG Adobe Reader
- **firefox**: (Boolean) STIG Firefox
- **chrome**: (Boolean) STIG Chrome
- **IE11**: (Boolean) STIG Internet Explorer 11
- **edge**: (Boolean) STIG Edge
- **dotnet**: (Boolean) STIG .NET Framework
- **office**: (Boolean) STIG Office
- **onedrive**: (Boolean) STIG OneDrive
- **java**: (Boolean) STIG Java
- **windows**: (Boolean) STIG Windows
- **defender**: (Boolean) STIG Windows Defender
- **firewall**: (Boolean) STIG Windows Firewall
- **mitigations**: (Boolean) STIG Mitigations
- **nessusPID**: (Boolean) Resolve Unquoted Strings in Path
- **horizon**: (Boolean) STIG VMware Horizon
- **sosoptional**: (Boolean) Optional STIG/Hardening items

An example of how to run the script with all default parameters would be:

```powershell
.\secure-standalone.ps1
```
If you want to specify a different value for one or more of the parameters, you can include them in the command along with their desired value. For example, if you wanted to run the script and set the $firefox parameter to $false, the command would be:

```powershell
.\secure-standalone.ps1 -firefox $false
```

You can also specify multiple parameters in the command like this:

```powershell
.\secure-standalone.ps1 -firefox $false -chrome $false
```

ਨੋਟ ਕਰੋ ਕਿ ਇਸ ਉਦਾਹਰਨ ਵਿੱਚ, ਫਾਇਰਫਾਕਸ ਅਤੇ ਕਰੋਮ ਪੈਰਾਮੀਟਰ $false 'ਤੇ ਸੈੱਟ ਕੀਤੇ ਗਏ ਹਨ।



