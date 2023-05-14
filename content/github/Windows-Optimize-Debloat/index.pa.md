---
title: "ਵਿੰਡੋਜ਼-ਓਪਟੀਮਾਈਜ਼-ਡੈਬਲੋਟ ਨਾਲ ਆਪਣੇ ਵਿੰਡੋਜ਼ ਪੀਸੀ ਨੂੰ ਅਨੁਕੂਲ ਬਣਾਓ"
date: 2020-12-29
toc: true
draft: false
description: "Windows-Optimize-Debloat ਨਾਲ ਆਪਣੇ ਵਿੰਡੋਜ਼ ਓਪਰੇਟਿੰਗ ਸਿਸਟਮ ਦੀ ਕਾਰਗੁਜ਼ਾਰੀ ਅਤੇ ਗੋਪਨੀਯਤਾ ਵਿੱਚ ਸੁਧਾਰ ਕਰੋ, ਇੱਕ ਵਿਆਪਕ ਸਕ੍ਰਿਪਟ ਜੋ ਬਲੋਟਵੇਅਰ ਨੂੰ ਹਟਾਉਣ ਅਤੇ ਸਿਸਟਮ ਸੈਟਿੰਗਾਂ ਨੂੰ ਅਨੁਕੂਲ ਬਣਾਉਣ ਵਿੱਚ ਮਦਦ ਕਰਦੀ ਹੈ।"
tags: ["ਵਿੰਡੋਜ਼-ਓਪਟੀਮਾਈਜ਼-ਡੀਬਲੋਟ", "ਵਿੰਡੋਜ਼ ਓਪਟੀਮਾਈਜੇਸ਼ਨ", "ਵਿੰਡੋਜ਼ ਨੂੰ ਡੀਬਲੋ ਕਰਨਾ", "ਵਿੰਡੋਜ਼ ਨੂੰ ਤੇਜ਼ ਕਰੋ", "ਵਿੰਡੋਜ਼ ਪ੍ਰਦਰਸ਼ਨ ਨੂੰ ਅਨੁਕੂਲ ਬਣਾਓ", "ਵਿੰਡੋਜ਼ ਪਰਫਾਰਮੈਂਸ ਬੂਸਟ", "ਵਿੰਡੋਜ਼ ਸਿਸਟਮ ਓਪਟੀਮਾਈਜੇਸ਼ਨ", "ਮਾਈਕ੍ਰੋਸਾਫਟ", "ਗੋਪਨੀਯਤਾ", "ਬਲੋਟਵੇਅਰ ਹਟਾਉਣਾ", "ਵਿੰਡੋਜ਼ 10", "ਵਿੰਡੋਜ਼ 11", "ਵਿੰਡੋਜ਼ ਡਿਫੈਂਡਰ", "ਵਿੰਡੋਜ਼ ਅੱਪਡੇਟ", "ਕੋਰਟੋਨਾ", "ਸਮੂਹ ਨੀਤੀ ਆਬਜੈਕਟ", "ਟੈਲੀਮੈਟਰੀ", "ਵਿੰਡੋਜ਼ ਸਟੋਰ", "ਵਿੰਡੋਜ਼ 10 ਪ੍ਰੋਫੈਸ਼ਨਲ", "ਵਿੰਡੋਜ਼ 10 ਹੋਮ"]
---


[![Test script against windows docker container](https://github.com/simeononsecurity/Windows-Optimize-Debloat/actions/workflows/test-with-docker.yml/badge.svg)](https://github.com/simeononsecurity/Windows-Optimize-Debloat/actions/workflows/test-with-docker.yml)

*ਉਨ੍ਹਾਂ ਲਈ ਜੋ ਆਪਣੇ ਵਿੰਡੋਜ਼ 10 ਅਤੇ 11 ਦੀ ਸਥਾਪਨਾ ਨੂੰ ਘੱਟ ਤੋਂ ਘੱਟ ਕਰਨਾ ਚਾਹੁੰਦੇ ਹਨ।*

**ਨੋਟ:** ਇਹ ਸਕ੍ਰਿਪਟ ਜ਼ਿਆਦਾਤਰ, ਜੇਕਰ ਸਾਰੇ ਨਹੀਂ, ਬਿਨਾਂ ਕਿਸੇ ਸਮੱਸਿਆ ਦੇ ਸਿਸਟਮਾਂ ਲਈ ਕੰਮ ਕਰੇਗੀ। ਜਦਕਿ[@SimeonOnSecurity](https://github.com/simeononsecurity) creates, reviews, and tests each repo intensivly, we can not test every possible configuration nor does [@SimeonOnSecurity](https://github.com/simeononsecurity) take any responsibility for breaking your system. If something goes wrong, be prepared to submit an [issue](../../issues) ਇਸ ਸਕ੍ਰਿਪਟ ਨੂੰ ਨਾ ਚਲਾਓ ਜੇਕਰ ਤੁਸੀਂ ਇਹ ਨਹੀਂ ਸਮਝਦੇ ਕਿ ਇਹ ਕੀ ਕਰਦੀ ਹੈ।

## ਜਾਣ-ਪਛਾਣ:
ਵਿੰਡੋਜ਼ 10 ਅਤੇ 11 ਬਾਕਸ ਦੇ ਬਾਹਰ ਹਮਲਾਵਰ ਅਤੇ ਅਸੁਰੱਖਿਅਤ ਓਪਰੇਟਿੰਗ ਸਿਸਟਮ ਹਨ।
ਵਰਗੀਆਂ ਸੰਸਥਾਵਾਂ[Microsoft](https://microsoft.com), [PrivacyTools.io](https://PrivacyTools.io) ਅਤੇ ਹੋਰਾਂ ਨੇ Windows 10 ਓਪਰੇਟਿੰਗ ਸਿਸਟਮ ਨੂੰ ਅਨੁਕੂਲਿਤ ਅਤੇ ਡੀਬਲੋਟ ਕਰਨ ਲਈ ਸੰਰਚਨਾ ਤਬਦੀਲੀਆਂ ਦੀ ਸਿਫ਼ਾਰਸ਼ ਕੀਤੀ ਹੈ। ਇਹਨਾਂ ਤਬਦੀਲੀਆਂ ਵਿੱਚ ਟੈਲੀਮੈਟਰੀ ਨੂੰ ਬਲੌਕ ਕਰਨਾ, ਲੌਗਸ ਨੂੰ ਮਿਟਾਉਣਾ, ਅਤੇ ਕੁਝ ਨਾਮ ਦੇਣ ਲਈ ਬਲੋਟਵੇਅਰ ਨੂੰ ਹਟਾਉਣਾ ਸ਼ਾਮਲ ਹੈ। ਇਸ ਸਕ੍ਰਿਪਟ ਦਾ ਉਦੇਸ਼ ਉਹਨਾਂ ਸੰਸਥਾਵਾਂ ਦੁਆਰਾ ਸਿਫ਼ਾਰਿਸ਼ ਕੀਤੀਆਂ ਸੰਰਚਨਾਵਾਂ ਨੂੰ ਸਵੈਚਾਲਤ ਕਰਨਾ ਹੈ।

## ਨੋਟ:
- ਇਹ ਸਕ੍ਰਿਪਟ ਮੁੱਖ ਤੌਰ 'ਤੇ **ਨਿੱਜੀ ਵਰਤੋਂ** ਵਾਤਾਵਰਣਾਂ ਵਿੱਚ ਕੰਮ ਕਰਨ ਲਈ ਤਿਆਰ ਕੀਤੀ ਗਈ ਹੈ।
- ਇਸ ਸਕ੍ਰਿਪਟ ਨੂੰ ਇਸ ਤਰੀਕੇ ਨਾਲ ਡਿਜ਼ਾਇਨ ਕੀਤਾ ਗਿਆ ਹੈ ਕਿ ਕੁਝ ਹੋਰ ਸਕ੍ਰਿਪਟਾਂ ਦੇ ਉਲਟ ਓਪਟੀਮਾਈਜੇਸ਼ਨ, ਕੋਰ ਵਿੰਡੋਜ਼ ਕਾਰਜਕੁਸ਼ਲਤਾ ਨੂੰ ਨਹੀਂ ਤੋੜਨਗੀਆਂ।
 - ਵਿੰਡੋਜ਼ ਅੱਪਡੇਟ, ਵਿੰਡੋਜ਼ ਡਿਫੈਂਡਰ, ਵਿੰਡੋਜ਼ ਸਟੋਰ, ਅਤੇ ਕੋਰਟੋਨਾ ਵਰਗੀਆਂ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਨੂੰ ਪ੍ਰਤਿਬੰਧਿਤ ਕੀਤਾ ਗਿਆ ਹੈ, ਪਰ ਜ਼ਿਆਦਾਤਰ ਹੋਰ ਵਿੰਡੋਜ਼ 10 ਗੋਪਨੀਯਤਾ ਸਕ੍ਰਿਪਟਾਂ ਵਾਂਗ ਵਿਗਾੜ ਵਾਲੀ ਸਥਿਤੀ ਵਿੱਚ ਨਹੀਂ ਹਨ।
- ਜੇਕਰ ਤੁਸੀਂ ਸਿਰਫ਼ ਵਪਾਰਕ ਵਾਤਾਵਰਣਾਂ ਨੂੰ ਨਿਸ਼ਾਨਾ ਬਣਾਉਣ ਵਾਲੀ ਇੱਕ ਛੋਟੀ ਜਿਹੀ ਸਕ੍ਰਿਪਟ ਦੀ ਭਾਲ ਕਰਦੇ ਹੋ, ਤਾਂ ਕਿਰਪਾ ਕਰਕੇ ਇਸਨੂੰ ਦੇਖੋ[GitHub Repository](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)

## ਲੋੜਾਂ:
- [X] ਵਿੰਡੋਜ਼ 10/11 ਐਂਟਰਪ੍ਰਾਈਜ਼, ਵਿੰਡੋਜ਼ 10 ਪ੍ਰੋਫੈਸ਼ਨਲ, ਜਾਂ ਵਿੰਡੋਜ਼ 10 ਹੋਮ
  - ਵਿੰਡੋਜ਼ ਹੋਮ ਜੀਪੀਓ ਕੌਂਫਿਗਰੇਸ਼ਨਾਂ ਦੀ ਆਗਿਆ ਨਹੀਂ ਦਿੰਦਾ ਹੈ।
    - ਸਕ੍ਰਿਪਟ ਅਜੇ ਵੀ ਕੰਮ ਕਰੇਗੀ ਪਰ ਸਾਰੀਆਂ ਸੈਟਿੰਗਾਂ ਲਾਗੂ ਨਹੀਂ ਹੋਣਗੀਆਂ।
  - ਵਿੰਡੋਜ਼ "ਐਨ" ਐਡੀਸ਼ਨ ਦੀ ਜਾਂਚ ਨਹੀਂ ਕੀਤੀ ਜਾਂਦੀ।
  - ਚਲਾਓ[Windows 10 Upgrade Assistant](https://support.microsoft.com/en-us/help/3159635/windows-10-update-assistant) ਨਵੀਨਤਮ ਮੁੱਖ ਰੀਲੀਜ਼ ਨੂੰ ਅੱਪਡੇਟ ਕਰਨ ਅਤੇ ਤਸਦੀਕ ਕਰਨ ਲਈ।

## ਮਾਈਕ੍ਰੋਸਾਫਟ ਅਕਾਉਂਟ ਜਾਂ ਐਕਸਬਾਕਸ ਸੇਵਾਵਾਂ ਨੂੰ ਠੀਕ ਕਰਨਾ:
ਇਹ ਇਸ ਲਈ ਹੈ ਕਿਉਂਕਿ ਅਸੀਂ ਮਾਈਕ੍ਰੋਸੌਫਟ ਖਾਤਿਆਂ ਵਿੱਚ ਸਾਈਨ ਇਨ ਕਰਨ ਨੂੰ ਬਲੌਕ ਕਰਦੇ ਹਾਂ। ਮਾਈਕ੍ਰੋਸਾੱਫਟ ਦੀ ਟੈਲੀਮੈਟਰੀ ਅਤੇ ਪਛਾਣ ਐਸੋਸੀਏਸ਼ਨ ਨੂੰ ਭੜਕਾਇਆ ਗਿਆ ਹੈ।
ਹਾਲਾਂਕਿ, ਜੇਕਰ ਤੁਸੀਂ ਅਜੇ ਵੀ ਇਹਨਾਂ ਸੇਵਾਵਾਂ ਦੀ ਵਰਤੋਂ ਕਰਨਾ ਚਾਹੁੰਦੇ ਹੋ ਤਾਂ ਰੈਜ਼ੋਲਿਊਸ਼ਨ ਲਈ ਨਿਮਨਲਿਖਤ ਮੁੱਦੇ ਦੀਆਂ ਟਿਕਟਾਂ ਵੇਖੋ:
- https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/1
- https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/16
- https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/22

## ਸਕ੍ਰਿਪਟਾਂ ਅਤੇ ਸਾਧਨਾਂ ਦੀ ਇੱਕ ਸੂਚੀ ਜੋ ਇਹ ਸੰਗ੍ਰਹਿ ਵਰਤਦਾ ਹੈ:
-[Microsoft Security Compliance Toolkit 1.0](https://www.microsoft.com/en-us/download/details.aspx?id=55319)

## ਇਸ ਤੋਂ ਵਧੀਕ ਸੰਰਚਨਾਵਾਂ 'ਤੇ ਵਿਚਾਰ ਕੀਤਾ ਗਿਆ ਸੀ:
-[BuiltByBel - PrivateZilla](https://github.com/builtbybel/privatezilla)
-[MelodysTweaks - Basic Tweaks](https://sites.google.com/view/melodystweaks/basictweaks)
-[Microsoft - Managing Windows 10 Telemetry and Callbacks](https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services)
-[Microsoft - Windows 10 Privacy](https://docs.microsoft.com/en-us/windows/privacy/)
-[Microsoft - Windows 10 VDI Recomendations](https://docs.microsoft.com/en-us/windows-server/remote/remote-desktop-services/rds_vdi-recommendations-1909)
-[Mirinsoft - SharpApp](https://github.com/builtbybel/sharpapp)
-[Mirinsoft - debotnet](https://github.com/builtbybel/debotnet)
-[UnderGroundWires - Privacy.S**Y](https://github.com/undergroundwires/privacy.sexy)
-[Sycnex - Windows10Debloater](https://github.com/Sycnex/Windows10Debloater)
-[The-Virtual-Desktop-Team - Virtual-Desktop-Optimization-Tool](https://github.com/The-Virtual-Desktop-Team/Virtual-Desktop-Optimization-Tool)
-[TheVDIGuys - Windows 10 VDI Optimize](https://github.com/TheVDIGuys/Windows_10_VDI_Optimize)
-[W4H4WK - Debloat Windows 10](https://github.com/W4RH4WK/Debloat-Windows-10/tree/master/scripts)

## ਸਕ੍ਰਿਪਟ ਨੂੰ ਕਿਵੇਂ ਚਲਾਉਣਾ ਹੈ:
### ਸਵੈਚਲਿਤ ਸਥਾਪਨਾ:
ਸਕ੍ਰਿਪਟ ਨੂੰ ਇਸ ਤਰ੍ਹਾਂ ਐਕਸਟਰੈਕਟ ਕੀਤੇ GitHub ਡਾਊਨਲੋਡ ਤੋਂ ਲਾਂਚ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ:
```powershell
iwr -useb 'https://simeononsecurity.ch/scripts/windowsoptimizeanddebloat.ps1'|iex
```
### Manual Install:
If manually downloaded, the script must be launched from an administrative powershell in the directory containing all the files from the [GitHub Repository](https://github.com/simeononsecurity/Windows-Optimize-Debloat)

The script "sos-optimize-windows.ps1" includes several parameters that allow for customization of the optimization process. Each parameter is a boolean value that defaults to true if not specified.

- **$cleargpos**: Clears Group Policy Objects settings.
- **$installupdates**: Installs updates to the system.
- **$removebloatware**: Removes unnecessary programs and features from the system.
- **$disabletelemetry**: Disables data collection and telemetry.
- **$privacy**: Makes changes to improve privacy.
- **$imagecleanup**: Cleans up unneeded files from the system.
- **$diskcompression**: Compresses the system disk.
- **$updatemanagement**: Changes the way updates are managed and improved on the system.
- **$sosbrowsers**: Optimizes the system's web browsers.

An example of how to launch the script with specific parameters would be:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
Get-ChildItem -Recurse *.ps1 | Unblock-File
powershell.exe -ExecutionPolicy ByPass -File .\sos-optimize-windows.ps1 -cleargpos:$false -installupdates:$false
```

