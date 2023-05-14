---
title: "ਡਿਫੈਂਡਰ ਹਾਰਡਨਿੰਗ ਸਕ੍ਰਿਪਟ ਨਾਲ ਵਿੰਡੋਜ਼ 10 ਸੁਰੱਖਿਆ ਨੂੰ ਵਧਾਉਣਾ"
date: 2020-11-15
toc: true
draft: false
description: "ਵਿੰਡੋਜ਼ ਡਿਫੈਂਡਰ ਐਂਟੀਵਾਇਰਸ STIG V2R1 ਦੀਆਂ ਸਾਰੀਆਂ ਜ਼ਰੂਰਤਾਂ ਨੂੰ ਲਾਗੂ ਕਰਦੇ ਹੋਏ, ਇੱਕ PowerShell ਸਕ੍ਰਿਪਟ ਨਾਲ Windows 10 ਸੁਰੱਖਿਆ ਨੂੰ ਕਿਵੇਂ ਵਧਾਉਣਾ ਹੈ ਬਾਰੇ ਜਾਣੋ ਜੋ Windows Defender ਐਂਟੀਵਾਇਰਸ ਨੂੰ ਸਖ਼ਤ ਬਣਾਉਂਦੀ ਹੈ।"
tags: ["ਵਿੰਡੋਜ਼ ਡਿਫੈਂਡਰ", "ਵਿੰਡੋਜ਼ 10", "ਵਿੰਡੋਜ਼ 10 ਸੁਰੱਖਿਆ", "PowerShell ਸਕ੍ਰਿਪਟ", "ਸਖਤ ਕਰਨਾ", "ਡਿਫੈਂਡਰ ਹਾਰਡਨਿੰਗ", "ਸੁਰੱਖਿਆ ਆਟੋਮੇਸ਼ਨ", "ਪਾਲਣਾ", "ਨਿਯੰਤਰਿਤ ਫੋਲਡਰ ਪਹੁੰਚ", "ਘੁਸਪੈਠ ਰੋਕਥਾਮ ਸਿਸਟਮ", "ਐਪਲੀਕੇਸ਼ਨ ਨਿਯੰਤਰਣ", "ਹਮਲੇ ਦੀ ਸਤਹ ਕਮੀ", "ਸੁਰੱਖਿਆ ਦਾ ਸ਼ੋਸ਼ਣ ਕਰੋ", "ਕਲਾਊਡ-ਡਿਲੀਵਰਡ ਪ੍ਰੋਟੈਕਸ਼ਨ", "ਨੈੱਟਵਰਕ ਸੁਰੱਖਿਆ", "ਵਿੰਡੋਜ਼ ਡਿਫੈਂਡਰ STIG ਸਕ੍ਰਿਪਟ", "ਵਿੰਡੋਜ਼ ਡਿਫੈਂਡਰ STIG", "ਵਿੰਡੋਜ਼ ਡਿਫੈਂਡਰ ਐਂਟੀਵਾਇਰਸ STIG V2R1", "ਡਬਲਯੂ.ਡੀ.ਏ.ਸੀ", "ਏ.ਐੱਸ.ਆਰ"]
---


## ਇਹ ਸਕ੍ਰਿਪਟ ਕੀ ਕਰਦੀ ਹੈ?
- ਕਲਾਉਡ ਦੁਆਰਾ ਪ੍ਰਦਾਨ ਕੀਤੀ ਸੁਰੱਖਿਆ ਨੂੰ ਸਮਰੱਥ ਬਣਾਉਂਦਾ ਹੈ
- ਨਿਯੰਤਰਿਤ ਫੋਲਡਰ ਪਹੁੰਚ ਨੂੰ ਸਮਰੱਥ ਬਣਾਉਂਦਾ ਹੈ
- ਨੈੱਟਵਰਕ ਸੁਰੱਖਿਆ ਨੂੰ ਸਮਰੱਥ ਬਣਾਉਂਦਾ ਹੈ
- ਘੁਸਪੈਠ ਰੋਕਥਾਮ ਪ੍ਰਣਾਲੀ ਨੂੰ ਸਮਰੱਥ ਬਣਾਉਂਦਾ ਹੈ
-[Enables Windows Defender Application Control Policies](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/windows-defender-application-control)
-[Enables Windows Defender Attack Surface Reduction Rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-atp/attack-surface-reduction)
-[Enables Windows Defender Exploit Protections](https://docs.microsoft.com/en-us/microsoft-365/security/defender-endpoint/enable-exploit-protection?view=o365-worldwide#powershell)
- ਵਿੱਚ ਸੂਚੀਬੱਧ ਸਾਰੀਆਂ ਲੋੜਾਂ ਨੂੰ ਲਾਗੂ ਕਰਦਾ ਹੈ[Windows Defender Antivirus STIG V2R1](https://dl.cyber.mil/stigs/zip/U_MS_Windows_Defender_Antivirus_V2R1_STIG.zip)

## ਲੋੜਾਂ:
- [x] Windows 10 Enterprise (**Preferred**) ਜਾਂ Windows 10 Professional
  - ਵਿੰਡੋਜ਼ 10 ਹੋਮ ਜੀਪੀਓ ਕੌਂਫਿਗਰੇਸ਼ਨਾਂ ਜਾਂ ਲਈ ਆਗਿਆ ਨਹੀਂ ਦਿੰਦਾ ਹੈ[ASR](https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-atp/attack-surface-reduction) 
ਹਾਲਾਂਕਿ ਇਹਨਾਂ ਵਿੱਚੋਂ ਜ਼ਿਆਦਾਤਰ ਸੰਰਚਨਾਵਾਂ ਅਜੇ ਵੀ ਲਾਗੂ ਹੋਣਗੀਆਂ।
  - Windows 10 "N" ਐਡੀਸ਼ਨਾਂ ਦੀ ਜਾਂਚ ਨਹੀਂ ਕੀਤੀ ਜਾਂਦੀ।

## ਲੋੜੀਂਦੀਆਂ ਫਾਈਲਾਂ ਨੂੰ ਡਾਉਨਲੋਡ ਕਰੋ:

ਤੋਂ ਲੋੜੀਂਦੀਆਂ ਫਾਈਲਾਂ ਡਾਊਨਲੋਡ ਕਰੋ[GitHub Repository](https://github.com/simeononsecurity/Windows-Defender-STIG-Script)

## ਸਕ੍ਰਿਪਟ ਨੂੰ ਕਿਵੇਂ ਚਲਾਉਣਾ ਹੈ:

**ਸਕ੍ਰਿਪਟ ਨੂੰ ਇਸ ਤਰ੍ਹਾਂ ਐਕਸਟਰੈਕਟ ਕੀਤੇ GitHub ਡਾਊਨਲੋਡ ਤੋਂ ਲਾਂਚ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ:**
```
.\sos-windowsdefenderhardening.ps1
```
