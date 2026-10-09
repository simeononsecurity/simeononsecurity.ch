---
title: "PowerShell DSC: ਇੱਕ ਸ਼ੁਰੂਆਤੀ ਮਾਰਗਦਰਸ਼ਕ"
date: 2023-04-02
toc: true
draft: false
description: PowerShell Desired State Configuration (DSC) ਦੀ ਤਾਕਤ ਨੂੰ ਖੋਜੋ ਤਾਂ ਜੋ ਸੁਰੱਖਿਅਤ ਅਤੇ ਅਨੁਕੂਲ ਵਾਤਾਵਰਣ ਲਈ ਸਿਸਟਮ ਸੰਰਚਨਾਵਾਂ ਨੂੰ ਆਟੋਮੇਟ ਅਤੇ ਪ੍ਰਬੰਧਿਤ ਕੀਤਾ ਜਾ ਸਕੇ।
tags:
- PowerShell
- DSC
- ਸੰਰਚਨਾ ਪ੍ਰਬੰਧਨ
- ਆਟੋਮੇਸ਼ਨ
- ਵਿੰਡੋਜ਼
- ਸਿਸਟਮ ਪ੍ਰਸ਼ਾਸਨ
- ਸਰਵੋਤਮ ਅਭਿਆਸ
- ਅਨੁਕੂਲਤਾ
- ਸੁਰੱਖਿਆ
- ਬੁਨਿਆਦੀ ਢਾਂਚਾ
- DevOps
- ਸਰਵਰ ਸੰਰਚਨਾ
- ਟੈਸਟਿੰਗ
- Git
- ਸਰੋਤ ਨਿਯੰਤਰਣ
- ਸਰਕਾਰੀ ਨਿਯਮ
- NIST
- CIS
- ਸੰਰਚਨਾ ਡ੍ਰਿਫਟ
- ਕਸਟਮ ਸਰੋਤ
cover: /img/cover/a-guide-to-using-powershell-desired-state-configuration-dsc-for-configuration-management.webp
coverAlt: ਇੱਕ ਚਿੱਤਰ ਜਿਸ ਵਿੱਚ ਇੱਕ ਸਟਾਈਲਾਈਜ਼ਡ PowerShell ਟਰਮੀਨਲ ਹੈ ਜਿਸਦੇ ਆਲੇ-ਦੁਆਲੇ ਅਬਸਟ੍ਰੈਕਟ ਚਿੰਨ੍ਹਾਂ ਹਨ, ਜੋ ਸੰਰਚਨਾ ਪ੍ਰਬੰਧਨ ਅਤੇ ਆਟੋਮੇਸ਼ਨ ਦਾ ਪ੍ਰਤੀਕ ਹਨ, ਅਤੇ ਇਹ ਗਹਿਰੇ ਨੈਵੀ ਪਿਛੋਕੜ ਦੇ ਖਿਲਾਫ ਸੈਟ ਕੀਤਾ ਗਿਆ ਹੈ।
coverCaption: ''
lastmod: 2026-10-08
---

**PowerShell Desired State Configuration (DSC) ਨੂੰ ਸੰਰਚਨਾ ਪ੍ਰਬੰਧਨ ਲਈ ਵਰਤਣ ਦਾ ਮਾਰਗਦਰਸ਼ਕ**

______

## ਪਰਿਚਯ

PowerShell Desired State Configuration (**DSC**) ਇੱਕ ਸ਼ਕਤੀਸ਼ਾਲੀ ਅਤੇ **ਅਹੰਕਾਰਪੂਰਕ ਸੰਦ** ਹੈ ਜੋ IT ਪ੍ਰਸ਼ਾਸਕਾਂ ਅਤੇ DevOps ਪੇਸ਼ੇਵਰਾਂ ਨੂੰ ਵਿੰਡੋਜ਼ ਅਤੇ ਲਿਨਕਸ ਸਿਸਟਮਾਂ ਦੀ ਤਾਇਨਾਤੀ ਅਤੇ ਸੰਰਚਨਾ ਨੂੰ ਆਟੋਮੇਟ ਕਰਨ ਦੀ ਆਗਿਆ ਦਿੰਦਾ ਹੈ। ਇਹ ਲੇਖ PowerShell DSC ਨੂੰ ਸੰਰਚਨਾ ਪ੍ਰਬੰਧਨ ਲਈ ਵਰਤਣ ਦਾ ਵਿਸਤ੍ਰਿਤ ਮਾਰਗਦਰਸ਼ਕ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ, ਜਿਸ ਵਿੱਚ ਸਰਵੋਤਮ ਅਭਿਆਸ, ਸਰਕਾਰੀ ਨਿਯਮ ਅਤੇ ਲਾਭਦਾਇਕ ਸੰਦਰਭ ਸ਼ਾਮਲ ਹਨ।

______

## PowerShell Desired State Configuration ਨਾਲ ਸ਼ੁਰੂਆਤ

### PowerShell Desired State Configuration ਕੀ ਹੈ?

PowerShell Desired State Configuration (**DSC**) PowerShell ਵਿੱਚ ਬਣੀ ਇੱਕ **ਘੋਸ਼ਣਾਤਮਕ ਭਾਸ਼ਾ** ਹੈ ਜੋ ਪ੍ਰਸ਼ਾਸਕਾਂ ਨੂੰ ਸਿਸਟਮਾਂ, ਐਪਲੀਕੇਸ਼ਨਾਂ ਅਤੇ ਸੇਵਾਵਾਂ ਦੀ ਸੰਰਚਨਾ ਆਟੋਮੇਟ ਕਰਨ ਦੀ ਆਗਿਆ ਦਿੰਦੀ ਹੈ। ਇਹ ਸੰਰਚਨਾਵਾਂ ਨੂੰ ਪ੍ਰਬੰਧਿਤ ਕਰਨ ਅਤੇ ਇਹ ਯਕੀਨੀ ਬਣਾਉਣ ਲਈ ਇੱਕ **ਮਿਆਰੀ ਅਤੇ ਸਥਿਰ** ਤਰੀਕਾ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ ਕਿ ਸਿਸਟਮ ਚਾਹੀਦੇ ਹਾਲਤ ਵਿੱਚ ਰਹਿਣ।

### PowerShell DSC ਦੀ ਇੰਸਟਾਲੇਸ਼ਨ

PowerShell DSC ਨਾਲ ਸ਼ੁਰੂਆਤ ਕਰਨ ਲਈ, ਤੁਹਾਨੂੰ **Windows Management Framework (WMF)** ਇੰਸਟਾਲ ਕਰਨਾ ਪਵੇਗਾ। WMF ਇੱਕ ਪੈਕੇਜ ਹੈ ਜਿਸ ਵਿੱਚ PowerShell, DSC ਅਤੇ ਹੋਰ ਜਰੂਰੀ ਪ੍ਰਬੰਧਨ ਸੰਦ ਸ਼ਾਮਲ ਹਨ। ਤੁਸੀਂ WMF ਦਾ ਨਵਾਂ ਵਰਜਨ [Microsoft Download Center](https://www.microsoft.com/en-us/download/details.aspx?id=54616) ਤੋਂ ਡਾਊਨਲੋਡ ਕਰ ਸਕਦੇ ਹੋ।

______

## DSC ਸੰਰਚਨਾਵਾਂ ਬਣਾਉਣਾ ਅਤੇ ਲਾਗੂ ਕਰਨਾ

### DSC ਸੰਰਚਨਾਵਾਂ ਲਿਖਣਾ

ਇੱਕ DSC ਸੰਰਚਨਾ ਇੱਕ **PowerShell ਸਕ੍ਰਿਪਟ** ਹੁੰਦੀ ਹੈ ਜੋ ਸਿਸਟਮ ਦੀ ਚਾਹੀਦੀ ਹਾਲਤ ਦਾ ਵਰਣਨ ਕਰਦੀ ਹੈ। ਇਹ ਇੱਕ ਜਾਂ ਵੱਧ **DSC ਸਰੋਤਾਂ** ਤੋਂ ਬਣੀ ਹੁੰਦੀ ਹੈ ਜੋ ਸਿਸਟਮ ਦੇ ਭਾਗਾਂ ਲਈ ਲੋੜੀਂਦੇ ਸੈਟਿੰਗ ਅਤੇ ਗੁਣਾਂ ਨੂੰ ਪਰਿਭਾਸ਼ਿਤ ਕਰਦੇ ਹਨ। ਇੱਥੇ ਇੱਕ ਸਧਾਰਣ DSC ਸੰਰਚਨਾ ਦਾ ਉਦਾਹਰਨ ਹੈ ਜੋ ਵਿੰਡੋਜ਼ ਸਰਵਰ 'ਤੇ ਵੈੱਬ ਸਰਵਰ (IIS) ਰੋਲ ਇੰਸਟਾਲ ਕਰਦੀ ਹੈ:

```powershell
Configuration InstallIIS {
    Import-DscResource -ModuleName PSDesiredStateConfiguration

    Node 'localhost' {
        WindowsFeature IIS {
            Ensure = 'Present'
            Name   = 'Web-Server'
        }
    }
}
```
### DSC ਸੰਰਚਨਾਵਾਂ ਲਾਗੂ ਕਰਨਾ
ਜਦੋਂ ਤੁਸੀਂ DSC ਸੰਰਚਨਾ ਲਿਖ ਲੈਂਦੇ ਹੋ, ਤਾਂ ਤੁਸੀਂ ਇਸਨੂੰ ਟਾਰਗਟ ਸਿਸਟਮ 'ਤੇ **Start-DscConfiguration** ਕਮਾਂਡਲੈੱਟ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਲਾਗੂ ਕਰ ਸਕਦੇ ਹੋ। ਪਹਿਲਾਂ, PowerShell ਵਿੱਚ ਸਕ੍ਰਿਪਟ ਚਲਾ ਕੇ ਸੰਰਚਨਾ ਨੂੰ ਕੰਪਾਇਲ ਕਰੋ:

```powershell
InstallIIS
```

ਇਸ ਨਾਲ ਇੱਕ **MOF** ਫਾਈਲ (Managed Object Format) ਬਣੇਗੀ ਜਿਸ ਵਿੱਚ ਕੰਪਾਇਲ ਕੀਤੀ ਗਈ ਸੰਰਚਨਾ ਹੋਵੇਗੀ। ਫਿਰ, ਹੇਠਾਂ ਦਿੱਤੀ ਕਮਾਂਡ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਸੰਰਚਨਾ ਨੂੰ ਟਾਰਗਟ ਸਿਸਟਮ 'ਤੇ ਲਾਗੂ ਕਰੋ:

```powershell
Start-DscConfiguration -Path .\InstallIIS -Wait -Verbose
```

## PowerShell DSC ਵਰਤਣ ਲਈ ਸਰਵੋਤਮ ਅਭਿਆਸ

### ਆਪਣੀਆਂ ਸੰਰਚਨਾਵਾਂ ਨੂੰ ਮੋਡੀਊਲਰ ਬਣਾਓ

ਆਪਣੇ ਬੁਨਿਆਦੀ ਢਾਂਚੇ ਦੇ ਵੱਖ-ਵੱਖ ਭਾਗਾਂ ਨੂੰ **ਵੱਖ-ਵੱਖ DSC ਸਰੋਤਾਂ** ਵਿੱਚ ਵੰਡ ਕੇ **ਮੋਡੀਊਲਰ ਅਤੇ ਦੁਬਾਰਾ ਵਰਤਣਯੋਗ** ਸੰਰਚਨਾਵਾਂ ਬਣਾਓ। ਇਹ ਤਰੀਕਾ ਤੁਹਾਨੂੰ ਆਪਣੇ ਵਾਤਾਵਰਣ ਦੇ ਵਧਣ ਨਾਲ ਆਪਣੀਆਂ ਸੰਰਚਨਾਵਾਂ ਨੂੰ ਆਸਾਨੀ ਨਾਲ **ਰੱਖ-ਰਖਾਵ ਅਤੇ ਵਧਾਉਣ** ਦੀ ਆਗਿਆ ਦਿੰਦਾ ਹੈ।

### ਸਰੋਤ ਨਿਯੰਤਰਣ ਦੀ ਵਰਤੋਂ ਕਰੋ

ਹਮੇਸ਼ਾ ਆਪਣੀਆਂ DSC ਸੰਰਚਨਾਵਾਂ ਅਤੇ ਕਸਟਮ ਸਰੋਤਾਂ ਨੂੰ Git ਵਰਗੇ **ਸਰੋਤ ਨਿਯੰਤਰਣ ਪ੍ਰਣਾਲੀ** ਵਿੱਚ ਸਟੋਰ ਕਰੋ। ਇਹ ਅਭਿਆਸ ਤੁਹਾਨੂੰ ਬਦਲਾਵਾਂ ਨੂੰ ਟਰੈਕ ਕਰਨ, ਆਪਣੀ ਟੀਮ ਨਾਲ ਸਹਿਯੋਗ ਕਰਨ ਅਤੇ ਜਰੂਰਤ ਪੈਣ 'ਤੇ ਆਪਣੀਆਂ ਸੰਰਚਨਾਵਾਂ ਦੇ ਪਿਛਲੇ ਵਰਜਨਾਂ 'ਤੇ ਆਸਾਨੀ ਨਾਲ ਵਾਪਸ ਜਾਣ ਦੀ ਆਗਿਆ ਦਿੰਦਾ ਹੈ।

### ਆਪਣੀਆਂ ਸੰਰਚਨਾਵਾਂ ਦੀ ਜਾਂਚ ਕਰੋ

**ਟੈਸਟਿੰਗ** ਸੰਰਚਨਾ ਪ੍ਰਬੰਧਨ ਦਾ ਇੱਕ ਅਹੰਕਾਰਪੂਰਕ ਪੱਖ ਹੈ। DSC ਸੰਰਚਨਾ ਨੂੰ ਤਾਇਨਾਤ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ, ਇਸਨੂੰ ਇੱਕ **ਗੈਰ-ਉਤਪਾਦਨ ਵਾਤਾਵਰਣ** 'ਤੇ ਟੈਸਟ ਕਰੋ ਤਾਂ ਜੋ ਇਹ ਯਕੀਨੀ ਬਣਾਇਆ ਜਾ ਸਕੇ ਕਿ ਇਹ ਉਮੀਦ ਮੁਤਾਬਕ ਕੰਮ ਕਰਦੀ ਹੈ ਅਤੇ ਕੋਈ ਅਣਚਾਹੇ ਨਤੀਜੇ ਨਹੀਂ ਲਿਆਉਂਦੀ। ਤੁਸੀਂ ਆਪਣੇ DSC ਸੰਰਚਨਾਵਾਂ ਦੀ ਆਟੋਮੇਟਿਕ ਟੈਸਟਿੰਗ ਲਈ [Pester](https://github.com/pester/Pester) ਵਰਗੇ ਸੰਦ ਵੀ ਵਰਤ ਸਕਦੇ ਹੋ।

______

## ਸਰਕਾਰੀ ਨਿਯਮ ਅਤੇ ਮਾਰਗਦਰਸ਼ਕ

### NIST ਮਾਰਗਦਰਸ਼ਕ

National Institute of Standards and Technology (NIST) ਸਿਸਟਮ ਸੰਰਚਨਾ ਪ੍ਰਬੰਧਨ ਲਈ ਮਾਰਗਦਰਸ਼ਕ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ। ਖਾਸ ਕਰਕੇ, [NIST SP 800-53](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r5.pdf) ਪ੍ਰਕਾਸ਼ਨ ਵਿੱਚ ਇੱਕ ਭਾਗ (CM-2) ਬੇਸਲਾਈਨ ਸੰਰਚਨਾਵਾਂ ਬਾਰੇ ਹੈ, ਜੋ DSC ਦੀ ਵਰਤੋਂ ਨਾਲ ਸੰਬੰਧਿਤ ਹੈ। ਇਹ ਮਾਰਗਦਰਸ਼ਕ ਸਿਸਟਮ ਸੰਰਚਨਾਵਾਂ ਵਿੱਚ ਬਦਲਾਵਾਂ ਨੂੰ ਬਣਾਈ ਰੱਖਣ, ਨਿਗਰਾਨੀ ਕਰਨ ਅਤੇ ਨਿਯੰਤਰਿਤ ਕਰਨ ਦੀ ਮਹੱਤਤਾ 'ਤੇ ਜ਼ੋਰ ਦਿੰਦੇ ਹਨ। PowerShell DSC ਸੰਗਠਨਾਂ ਨੂੰ ਇਹ ਮਾਰਗਦਰਸ਼ਕ ਪਾਲਣ ਵਿੱਚ ਮਦਦ ਕਰ ਸਕਦਾ ਹੈ ਕਿਉਂਕਿ ਇਹ ਸਿਸਟਮ ਸੰਰਚਨਾਵਾਂ ਨੂੰ ਪ੍ਰਬੰਧਿਤ ਕਰਨ ਲਈ ਇੱਕ ਸਥਿਰ ਅਤੇ ਆਟੋਮੇਟ ਤਰੀਕਾ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ।

### Federal Information Security Management Act (FISMA)

Federal Information Security Management Act [FISMA](https://www.dhs.gov/cisa/federal-information-security-modernization-act) ਫੈਡਰਲ ਏਜੰਸੀਆਂ ਨੂੰ ਆਪਣੀਆਂ ਜਾਣਕਾਰੀ ਸੁਰੱਖਿਆ ਨਿਯੰਤਰਣਾਂ ਦੀ ਪ੍ਰਭਾਵਸ਼ੀਲਤਾ ਯਕੀਨੀ ਬਣਾਉਣ ਲਈ ਇੱਕ ਵਿਸਤ੍ਰਿਤ ਢਾਂਚਾ ਲਾਗੂ ਕਰਨ ਦੀ ਲੋੜ ਰੱਖਦਾ ਹੈ। ਸੰਰਚਨਾ ਪ੍ਰਬੰਧਨ FISMA ਅਨੁਕੂਲਤਾ ਦਾ ਇੱਕ ਮੁੱਖ ਹਿੱਸਾ ਹੈ, ਅਤੇ PowerShell DSC ਸੰਗਠਨਾਂ ਨੂੰ ਇਹ ਲੋੜਾਂ ਪੂਰੀਆਂ ਕਰਨ ਵਿੱਚ ਅਹੰਕਾਰਪੂਰਕ ਭੂਮਿਕਾ ਨਿਭਾ ਸਕਦਾ ਹੈ।
______

## ਨਤੀਜਾ

PowerShell Desired State Configuration (DSC) ਸਿਸਟਮ ਸੰਰਚਨਾਵਾਂ ਦੀ ਤਾਇਨਾਤੀ ਅਤੇ ਪ੍ਰਬੰਧਨ ਨੂੰ ਆਟੋਮੇਟ ਕਰਨ ਲਈ ਇੱਕ ਸ਼ਕਤੀਸ਼ਾਲੀ ਅਤੇ ਲਚਕੀਲਾ ਸੰਦ ਹੈ। ਸਰਵੋਤਮ ਅਭਿਆਸਾਂ ਦੀ ਪਾਲਣਾ ਕਰਕੇ ਅਤੇ ਸਰਕਾਰੀ ਨਿਯਮਾਂ ਦੀ ਪਾਬੰਦੀ ਕਰਕੇ, ਤੁਸੀਂ ਯਕੀਨੀ ਬਣਾਉ ਸਕਦੇ ਹੋ ਕਿ ਤੁਹਾਡੇ ਸੰਗਠਨ ਦੇ ਸਿਸਟਮ ਚਾਹੀਦੇ ਹਾਲਤ ਵਿੱਚ ਰਹਿਣਗੇ ਅਤੇ ਅਨੁਕੂਲਤਾ ਬਣੀ ਰਹੇਗੀ। ਇਸ ਲੇਖ ਵਿੱਚ ਦਿੱਤੇ ਗਏ ਸਰੋਤਾਂ ਦਾ ਲਾਭ ਉਠਾਉਣਾ ਨਾ ਭੁੱਲੋ ਤਾਂ ਜੋ PowerShell DSC ਦੀ ਸਮਝ ਵਧੇ ਅਤੇ ਤੁਹਾਡੇ ਸੰਰਚਨਾ ਪ੍ਰਬੰਧਨ ਪ੍ਰਕਿਰਿਆਵਾਂ ਵਿੱਚ ਸੁਧਾਰ ਹੋਵੇ।
______

## ਸੰਦਰਭ

- [PowerShell Desired State Configuration (DSC) ਅਧਿਕਾਰਿਕ ਦਸਤਾਵੇਜ਼](https://learn.microsoft.com/en-us/powershell/dsc/getting-started/wingettingstarted?view=dsc-1.1)
- [NIST SP 800-53 - ਫੈਡਰਲ ਜਾਣਕਾਰੀ ਸਿਸਟਮਾਂ ਅਤੇ ਸੰਗਠਨਾਂ ਲਈ ਸੁਰੱਖਿਆ ਅਤੇ ਗੋਪਨੀਯਤਾ ਨਿਯੰਤਰਣ](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r5.pdf)
- [Federal Information Security Management Act (FISMA)](https://www.dhs.gov/cisa/federal-information-security-modernization-act)
- [Pester - PowerShell ਟੈਸਟਿੰਗ ਫਰੇਮਵਰਕ](https://github.com/pester/Pester)
- [ਡਾਟਾ ਸੁਰੱਖਿਆ ਲਈ ਇਨਕ੍ਰਿਪਸ਼ਨ ਵਰਤਣ ਦਾ ਸ਼ੁਰੂਆਤੀ ਮਾਰਗਦਰਸ਼ਕ](https://simeononsecurity.com/articles/a-beginners-guide-to-using-encryption-for-data-protection/)
- [ਵਿੰਡੋਜ਼ 'ਤੇ ਸੁਰੱਖਿਆ ਪੈਚ ਇੰਸਟਾਲ ਕਰਨ ਲਈ ਸਰਵੋਤਮ ਅਭਿਆਸ](https://simeononsecurity.com/articles/best-practices-for-installing-security-patches-on-windows/)
