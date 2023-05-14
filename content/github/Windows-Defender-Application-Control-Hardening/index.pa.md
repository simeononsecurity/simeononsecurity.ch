---
title: "ਵਿੰਡੋਜ਼ ਡਿਫੈਂਡਰ ਐਪਲੀਕੇਸ਼ਨ ਕੰਟਰੋਲ ਡਬਲਯੂਡੀਏਸੀ ਨਾਲ ਵਿੰਡੋਜ਼ ਨੂੰ ਸਖ਼ਤ ਕਰਨ ਲਈ ਪੂਰੀ ਗਾਈਡ"
date: 2020-12-16
toc: true
draft: false
description: "ਆਪਣੇ ਵਿੰਡੋਜ਼ ਓਪਰੇਟਿੰਗ ਸਿਸਟਮ ਨੂੰ ਸਕ੍ਰਿਪਟਾਂ ਅਤੇ ਟੂਲਸ ਨਾਲ ਸਖ਼ਤ ਕਰਨ ਲਈ ਵਿੰਡੋਜ਼ ਡਿਫੈਂਡਰ ਐਪਲੀਕੇਸ਼ਨ ਕੰਟਰੋਲ WDAC ਦੀ ਵਰਤੋਂ ਕਿਵੇਂ ਕਰਨੀ ਹੈ ਬਾਰੇ ਜਾਣੋ।"
tags: ["ਵਿੰਡੋਜ਼ ਡਿਫੈਂਡਰ ਐਪਲੀਕੇਸ਼ਨ ਕੰਟਰੋਲ WDAC ਹਾਰਡਨਿੰਗ", "ਪਾਵਰਸ਼ੇਲ", "PowerShell ਸਕ੍ਰਿਪਟ", "ਆਟੋਮੇਸ਼ਨ", "ਪਾਲਣਾ", "ਬਲੂ-ਟੀਮ", "ਵਿੰਡੋਜ਼ ਡਿਫੈਂਡਰ STIG ਸਕ੍ਰਿਪਟ", "ਵਿੰਡੋਜ਼ ਡਿਫੈਂਡਰ ਹਾਰਡਨਿੰਗ", "ਵਿੰਡੋਜ਼ ਡਿਫੈਂਡਰ STIG", "ਡਿਫੈਂਡਰ STIG", "ਵਿੰਡੋਜ਼ ਡਿਫੈਂਡਰ ਐਕਸਪਲੋਇਟ ਪ੍ਰੋਟੈਕਸ਼ਨ WDEP", "ਵਿੰਡੋਜ਼ ਡਿਫੈਂਡਰ ਅਟੈਕ ਸਰਫੇਸ ਰਿਡਕਸ਼ਨ ASR", "ਵਿੰਡੋਜ਼ ਸਰਵਰ 2016 2019", "ਵਿੰਡੋਜ਼ ਸਰਵਰ ਕੋਰ", "Microsoft WDAC-ਟੂਲਕਿੱਟ", "CI ਨੀਤੀ ਨੂੰ ਤਾਜ਼ਾ ਕਰੋ", "ਮਾਈਕ੍ਰੋਸਾੱਫਟ ਨੇ ਬਲੌਕ ਨਿਯਮ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ", "ਮਾਈਕਰੋਸਾਫਟ ਡ੍ਰਾਈਵਰ ਬਲਾਕ ਨਿਯਮਾਂ ਦੀ ਸਿਫਾਰਸ਼ ਕਰਦਾ ਹੈ", "XML ਨੀਤੀਆਂ", "BIN ਨੀਤੀਆਂ", "ਸਮੂਹ ਨੀਤੀ", "ਮਾਈਕਰੋਸਾਫਟ ਇੰਟਿਊਨ"]
---

**ਵਿੰਡੋਜ਼ ਡਿਫੈਂਡਰ ਐਪਲੀਕੇਸ਼ਨ ਕੰਟਰੋਲ WDAC ਨਾਲ ਵਿੰਡੋਜ਼ ਨੂੰ ਸਖਤ ਕਰੋ**

## ਨੋਟ:
- ਵਿੰਡੋਜ਼ ਸਰਵਰ 2016/2019 ਜਾਂ ਸੰਸਕਰਣ 1903 ਤੋਂ ਪਹਿਲਾਂ ਦੀ ਕੋਈ ਵੀ ਚੀਜ਼ ਇੱਕ ਸਮੇਂ ਵਿੱਚ ਸਿਰਫ ਇੱਕ ਵਿਰਾਸਤੀ ਨੀਤੀ ਦਾ ਸਮਰਥਨ ਕਰਦੀ ਹੈ।
- ਵਿੰਡੋਜ਼ ਸਰਵਰ ਕੋਰ ਐਡੀਸ਼ਨ ਡਬਲਯੂਡੀਏਸੀ ਦਾ ਸਮਰਥਨ ਕਰਦਾ ਹੈ ਪਰ ਕੁਝ ਭਾਗ ਜੋ ਐਪਲੌਕਰ 'ਤੇ ਨਿਰਭਰ ਕਰਦੇ ਹਨ ਕੰਮ ਨਹੀਂ ਕਰਨਗੇ।
- ਕਿਰਪਾ ਕਰਕੇ ਪੜ੍ਹੋ[Recommended Reading](https://github.com/simeononsecurity/Windows-Defender-Application-Control-Hardening#recommended-reading) ਲਾਗੂ ਕਰਨ ਜਾਂ ਟੈਸਟ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ.

## ਸਕ੍ਰਿਪਟਾਂ ਅਤੇ ਸਾਧਨਾਂ ਦੀ ਇੱਕ ਸੂਚੀ ਜੋ ਇਹ ਸੰਗ੍ਰਹਿ ਵਰਤਦਾ ਹੈ:

-[MicrosoftDocs - WDAC-Toolkit](https://github.com/MicrosoftDocs/WDAC-Toolkit)
-[Microsoft - Refresh CI Policy ](https://www.microsoft.com/en-us/download/details.aspx?id=102925)

## ਇਸ ਤੋਂ ਵਧੀਕ ਸੰਰਚਨਾਵਾਂ 'ਤੇ ਵਿਚਾਰ ਕੀਤਾ ਗਿਆ ਸੀ:

-[Microsoft - Recommended block rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules)
-[Microsoft - Recommended driver block rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules)
-[Microsoft - Windows Defender Application Control](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/windows-defender-application-control-design-guide)

## ਵਿਆਖਿਆ:

### XML ਬਨਾਮ BIN:

- ਸਾਦੇ ਸ਼ਬਦਾਂ ਵਿਚ, **"XML"** ਨੀਤੀਆਂ ਸਥਾਨਕ ਤੌਰ 'ਤੇ ਮਸ਼ੀਨ 'ਤੇ ਲਾਗੂ ਕਰਨ ਲਈ ਹਨ ਅਤੇ **"BIN"** ਫਾਈਲਾਂ ਉਹਨਾਂ ਨੂੰ ਲਾਗੂ ਕਰਨ ਲਈ ਹਨ।[Group Policy](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-windows-defender-application-control-policies-using-group-policy) or [Microsoft Intune](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-windows-defender-application-control-policies-using-intune) ਜਦੋਂ ਤੁਸੀਂ ਸਥਾਨਕ ਤੈਨਾਤੀ ਵਿੱਚ XML, BIN, ਜਾਂ CIP ਨੀਤੀਆਂ ਦੀ ਵਰਤੋਂ ਕਰ ਸਕਦੇ ਹੋ, ਆਮ ਤੌਰ 'ਤੇ ਤੁਹਾਨੂੰ XML ਨਾਲ ਜੁੜੇ ਰਹਿਣਾ ਚਾਹੀਦਾ ਹੈ ਜਿੱਥੇ ਸੰਭਵ ਹੋਵੇ ਅਤੇ ਖਾਸ ਤੌਰ 'ਤੇ ਆਡਿਟ ਜਾਂ ਸਮੱਸਿਆ-ਨਿਪਟਾਰਾ ਕਰਨ ਵੇਲੇ।

### ਨੀਤੀ ਵਰਣਨ:

- **ਪੂਰਵ-ਨਿਰਧਾਰਤ ਨੀਤੀਆਂ:**
  - "ਡਿਫਾਲਟ" ਨੀਤੀਆਂ ਸਿਰਫ WDAC-ਟੂਲਕਿੱਟ ਵਿੱਚ ਉਪਲਬਧ ਡਿਫੌਲਟ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਦੀ ਵਰਤੋਂ ਕਰਦੀਆਂ ਹਨ।
- **ਸਿਫਾਰਿਸ਼ ਕੀਤੀਆਂ ਨੀਤੀਆਂ:**
  - "ਸਿਫਾਰਿਸ਼ ਕੀਤੀਆਂ" ਨੀਤੀਆਂ ਡਿਫੌਲਟ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਦੇ ਨਾਲ-ਨਾਲ ਮਾਈਕ੍ਰੋਸਾੱਫਟ ਦੀਆਂ ਸਿਫ਼ਾਰਿਸ਼ਾਂ ਦੀ ਵਰਤੋਂ ਕਰਦੀਆਂ ਹਨ[blocks](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules) and [driver block](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules) ਨਿਯਮ
- **ਆਡਿਟ ਨੀਤੀਆਂ:**
  - "ਆਡਿਟ" ਨੀਤੀਆਂ, ਨਿਯਮਾਂ ਦੇ ਅਪਵਾਦਾਂ ਨੂੰ ਲੌਗ ਕਰੋ। ਇਹ ਤੁਹਾਡੇ ਵਾਤਾਵਰਣ ਵਿੱਚ ਜਾਂਚ ਲਈ ਹੈ, ਤਾਂ ਜੋ ਤੁਸੀਂ ਆਪਣੀਆਂ ਵਾਤਾਵਰਣ ਦੀਆਂ ਲੋੜਾਂ ਨੂੰ ਪੂਰਾ ਕਰਨ ਲਈ, ਆਪਣੀ ਮਰਜ਼ੀ ਨਾਲ ਨੀਤੀਆਂ ਨੂੰ ਸੋਧ ਸਕੋ।
- **ਲਾਗੂ ਕੀਤੀਆਂ ਨੀਤੀਆਂ:**
  - "ਲਾਗੂ" ਨੀਤੀਆਂ ਨਿਯਮਾਂ ਦੇ ਕਿਸੇ ਵੀ ਅਪਵਾਦ ਦੀ ਇਜਾਜ਼ਤ ਨਹੀਂ ਦੇਣਗੀਆਂ, ਐਪਲੀਕੇਸ਼ਨਾਂ, ਡਰਾਈਵਰਾਂ, dlls, ਆਦਿ ਨੂੰ ਬਲੌਕ ਕੀਤਾ ਜਾਵੇਗਾ ਜੇਕਰ ਉਹ ਪਾਲਣਾ ਨਹੀਂ ਕਰਦੇ ਹਨ।

### ਉਪਲਬਧ ਨੀਤੀਆਂ:

- **XML:**
  - **ਕੇਵਲ ਆਡਿਟ:**
    - `WDAC_V1_Default_Audit_{version}.xml`
    - `WDAC_V1_Recommended_Audit_{version}.xml`
  - **ਲਾਗੂ ਕੀਤਾ:**
    - `WDAC_V1_Default_Enforced_{version}.xml`
    - `WDAC_V1_Recommended_Enforced_{version}.xml`
- **ਬਿਨ:**
  - **ਕੇਵਲ ਆਡਿਟ:**
    - `WDAC_V1_Default_Audit_{version}.bin`
    - `WDAC_V1_Recommended_Audit_{version}.bin`
  - **ਲਾਗੂ ਕੀਤਾ:**
    - `WDAC_V1_Default_Enforced_{version}.bin`
    - `WDAC_V1_Recommended_Enforced_{version}.bin`
- **ਸੀਆਈਪੀ:**
  - **ਕੇਵਲ ਆਡਿਟ:**
    - `WDAC_V1_Default_Audit\{uid}.cip`
    - `WDAC_V1_Recommended_Audit\{uid}.cip`
  - **ਲਾਗੂ ਕੀਤਾ:**
    - `WDAC_V1_Default_Enforced\{uid}.cip`
    - `WDAC_V1_Recommended_Enforced\{uid}.cip`

ਉਸ ਨੀਤੀ ਦੀ ਵਰਤੋਂ ਕਰਨ ਲਈ ਸਕ੍ਰਿਪਟ ਵਿੱਚ ਹੇਠਾਂ ਦਿੱਤੀ ਲਾਈਨ ਨੂੰ ਅੱਪਡੇਟ ਕਰੋ ਜੋ ਤੁਸੀਂ ਸਥਾਨਕ ਤੌਰ 'ਤੇ ਚਾਹੁੰਦੇ ਹੋ:

```powershell
$PolicyPath = "C:\temp\Windows Defender\CIP\WDAC_V1_Recommended_Enforced\*.cip"
#https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deployment/deploy-wdac-policies-with-script
ForEach ($Policy in (Get-ChildItem -Recurse $PolicyPath).Fullname) {
  $PolicyBinary = "$Policy"
  $DestinationFolder = $env:windir+"\System32\CodeIntegrity\CIPolicies\Active\"
  $RefreshPolicyTool = "./Files/EXECUTABLES/RefreshPolicy(AMD64).exe"
  Copy-Item -Path $PolicyBinary -Destination $DestinationFolder -Force
  & $RefreshPolicyTool
}
```

Alternatively, you may use [Group Policy](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-windows-defender-application-control-policies-using-group-policy) or [Microsoft Intune](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-windows-defender-application-control-policies-using-intune) to enforce the WDAC policies.

## Auditing:

You can view the WDAC event logs in event viewer under:

`Applications and Services Logs\Microsoft\Windows\CodeIntegrity\Operational`

## Recommended Reading:

- [Argonsys - Deploying Windows 10 Application Control Policy](https://argonsys.com/microsoft-cloud/library/deploying-windows-10-application-control-policy/)
- [Microsoft - Audit Windows Defender Application Control Policies](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/audit-windows-defender-application-control-policies)
- [Microsoft - Create a WDAC policy for fixed-workload devices using a reference computer](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/create-initial-default-policy)
- [Microsoft - Deploy Windows Defender Application Control policies by using Group Policy](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-windows-defender-application-control-policies-using-group-policy)
- [Microsoft - Deploy Windows Defender Application Control policies by using Microsoft Intune](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-windows-defender-application-control-policies-using-intune)
- [Microsoft - Deploy WDAC policies using script](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deployment/deploy-wdac-policies-with-script)
- [Microsoft - Enforce Windows Defencer Application Control Policies](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/enforce-windows-defender-application-control-policies)
- [Microsoft - Guidance on Creating WDAC Deny Policies](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/create-wdac-deny-policy)
- [Microsoft - Use multiple Windows Defender Application Control Policies](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-multiple-windows-defender-application-control-policies)

## How to run the script:

### Manual Install:

If manually downloaded, the script must be launched from an administrative powershell in the directory containing all the files from the [GitHub Repository](https://github.com/simeononsecurity/Windows-Defender-Application-Control-Hardening/archive/main.zip)

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
Get-ChildItem -Recurse *.ps1 | Unblock-File
.\sos-wdachardening.ps1
```
