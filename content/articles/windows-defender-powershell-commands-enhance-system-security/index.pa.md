---
title: "ਸਿਸਟਮ ਸੁਰੱਖਿਆ ਲਈ Windows Defender PowerShell ਕਮਾਂਡਾਂ"
date: 2023-07-27
lastmod: 2026-11-20
toc: true
draft: false
description: "Windows Defender PowerShell ਕਮਾਂਡਾਂ ਬਾਰੇ ਜਾਣੋ ਅਤੇ ਕਮਾਂਡ-ਲਾਈਨ ਕੰਟਰੋਲ ਨਾਲ ਆਪਣੇ ਸਿਸਟਮ ਦੀ ਸੁਰੱਖਿਆ ਵਧਾਓ।"
genre: ["Windows Defender", "PowerShell ਕਮਾਂਡਾਂ", "ਸਿਸਟਮ ਸੁਰੱਖਿਆ", "ਕਮਾਂਡ-ਲਾਈਨ ਕੰਟਰੋਲ", "ਐਂਟੀਵਾਇਰਸ", "Windows ਓਪਰੇਟਿੰਗ ਸਿਸਟਮ", "ਮੈਲਵੇਅਰ ਸੁਰੱਖਿਆ", "ਉੱਨਤ ਸੁਰੱਖਿਆ ਸੈਟਿੰਗਾਂ", "ਸੁਰੱਖਿਆ ਕਾਰਵਾਈਆਂ ਦਾ ਸਵੈਚਾਲਨ", "Windows PowerShell"]
tags: ["ਤਕਨਾਲੋਜੀ", "ਸਾਈਬਰ ਸੁਰੱਖਿਆ", "ਓਪਰੇਟਿੰਗ ਸਿਸਟਮ", "Windows", "ਕਮਾਂਡ-ਲਾਈਨ ਟੂਲ", "ਸਿਸਟਮ ਸੁਰੱਖਿਆ", "PowerShell", "ਐਂਟੀਵਾਇਰਸ", "ਮੈਲਵੇਅਰ ਸੁਰੱਖਿਆ", "ਸਕ੍ਰਿਪਟਿੰਗ"]
cover: "/img/cover/An_animated_illustration_depicting_a_shield_pr.webp"
coverAlt: "ਕਈ ਸਾਈਬਰ ਖ਼ਤਰਿਆਂ ਤੋਂ ਕੰਪਿਊਟਰ ਸਿਸਟਮ ਦੀ ਰੱਖਿਆ ਕਰਦੀ ਢਾਲ ਦੀ ਐਨੀਮੇਟਡ ਤਸਵੀਰ।"
coverCaption: "Windows Defender PowerShell ਕਮਾਂਡਾਂ ਨਾਲ ਆਪਣੇ ਸਿਸਟਮ ਦੀ ਸੁਰੱਖਿਆ ਵਧਾਓ।"
---

## ਜਾਣ-ਪਛਾਣ

Microsoft ਵੱਲੋਂ ਬਣਾਇਆ Windows Defender, Windows ਓਪਰੇਟਿੰਗ ਸਿਸਟਮਾਂ ਲਈ **ਇਕੱਠਾ ਐਂਟੀਵਾਇਰਸ ਅਤੇ ਸੁਰੱਖਿਆ ਹੱਲ** ਹੈ। ਇਹ ਸੁਰੱਖਿਆ ਸੈਟਿੰਗਾਂ ਸੰਭਾਲਣ ਲਈ ਸੌਖਾ ਇੰਟਰਫੇਸ ਦਿੰਦਾ ਹੈ। ਕਮਾਂਡ ਲਾਈਨ ਰਾਹੀਂ ਕੰਟਰੋਲ ਪਸੰਦ ਕਰਨ ਵਾਲੇ ਤਜਰਬੇਕਾਰ ਵਰਤੋਂਕਾਰ ਇਸ ਦੀਆਂ PowerShell ਕਮਾਂਡਾਂ ਵਰਤ ਸਕਦੇ ਹਨ। ਇਹ ਲੇਖ **Windows Defender PowerShell ਕਮਾਂਡਾਂ** ਅਤੇ Windows ਮਾਹੌਲ ਦੀ ਸੁਰੱਖਿਆ ਤੇ ਕੰਟਰੋਲ ਵਧਾਉਣ ਵਿੱਚ ਉਨ੍ਹਾਂ ਦੀ ਵਰਤੋਂ ਸਮਝਾਉਂਦਾ ਹੈ।

## Windows Defender PowerShell ਕਮਾਂਡਾਂ ਦੀ ਸਮਰੱਥਾ

ਇਹ ਕਮਾਂਡਾਂ ਕਮਾਂਡ-ਲਾਈਨ ਇੰਟਰਫੇਸ ਰਾਹੀਂ **ਉੱਨਤ ਸੁਰੱਖਿਆ ਕਾਰਵਾਈਆਂ** ਕਰਨ ਦਿੰਦੀਆਂ ਹਨ। ਇਨ੍ਹਾਂ ਵਿੱਚ ਮੈਲਵੇਅਰ ਸਕੈਨ ਕਰਨ ਤੋਂ ਲੈ ਕੇ ਉੱਨਤ ਸੁਰੱਖਿਆ ਸੈਟਿੰਗਾਂ ਬਦਲਣ ਤੱਕ ਦੇ ਕੰਮ ਹਨ। PowerShell ਨਾਲ ਤੁਸੀਂ ਸੁਰੱਖਿਆ ਕਾਰਵਾਈਆਂ ਸਵੈਚਾਲਿਤ ਕਰ ਸਕਦੇ ਹੋ, ਆਪਣੇ ਸਕ੍ਰਿਪਟ ਬਣਾ ਸਕਦੇ ਹੋ ਅਤੇ Windows Defender ਨੂੰ ਮੌਜੂਦਾ ਕੰਮਕਾਜ ਵਿੱਚ ਜੋੜ ਸਕਦੇ ਹੋ।

## Windows Defender PowerShell ਸ਼ੁਰੂ ਕਰੋ

ਇਨ੍ਹਾਂ ਕਮਾਂਡਾਂ ਲਈ **ਪ੍ਰਸ਼ਾਸਕੀ ਅਧਿਕਾਰਾਂ ਨਾਲ PowerShell ਸੈਸ਼ਨ** ਖੋਲ੍ਹੋ:

1. `Win + X` ਦਬਾਓ ਅਤੇ ਮੀਨੂ ਵਿੱਚੋਂ **Windows PowerShell (Admin)** (ਪ੍ਰਸ਼ਾਸਕ ਵਜੋਂ) ਚੁਣੋ।
2. ਪੁੱਛਣ 'ਤੇ ਐਪ ਨੂੰ ਡਿਵਾਈਸ ਵਿੱਚ ਤਬਦੀਲੀਆਂ ਕਰਨ ਦੀ ਇਜਾਜ਼ਤ ਦੇਣ ਲਈ **Yes** (ਹਾਂ) ਦਬਾਓ।

PowerShell ਸੈਸ਼ਨ ਖੁੱਲ੍ਹਣ ਮਗਰੋਂ Windows Defender PowerShell ਕਮਾਂਡਾਂ ਵਰਤੋ।

## ਆਮ Windows Defender PowerShell ਕਮਾਂਡਾਂ

### 1. **Get-MpComputerStatus**: Windows Defender ਦੀ ਸਥਿਤੀ ਵੇਖੋ

`Get-MpComputerStatus` ਸਿਸਟਮ ਵਿੱਚ Windows Defender ਦੀ ਮੌਜੂਦਾ ਸਥਿਤੀ ਦਿਖਾਉਂਦਾ ਹੈ, ਜਿਸ ਵਿੱਚ **ਐਂਟੀਵਾਇਰਸ ਇੰਜਣ ਦਾ ਵਰਜਨ**, ਪਿਛਲੇ ਸਕੈਨ ਦਾ ਸਮਾਂ ਅਤੇ ਰੀਅਲ-ਟਾਈਮ ਸੁਰੱਖਿਆ ਦੀ ਸਥਿਤੀ ਸ਼ਾਮਲ ਹਨ। ਇਸਨੂੰ ਚਲਾ ਕੇ Windows Defender ਦੀ ਕੁੱਲ ਹਾਲਤ ਜਲਦੀ ਜਾਂਚੋ।

ਸਥਿਤੀ ਵੇਖਣ ਲਈ ਪ੍ਰਸ਼ਾਸਕੀ ਅਧਿਕਾਰਾਂ ਵਾਲੇ PowerShell ਸੈਸ਼ਨ ਵਿੱਚ ਇਹ ਕਮਾਂਡ ਚਲਾਓ:

```powershell
Get-MpComputerStatus
```

ਇਹ ਜਾਣਕਾਰੀ ਦਿਖਾਉਂਦਾ ਹੈ, ਜਿਵੇਂ:

- **AntivirusEngineVersion**: Windows Defender ਵੱਲੋਂ ਵਰਤੇ ਜਾਂਦੇ ਐਂਟੀਵਾਇਰਸ ਇੰਜਣ ਦਾ ਵਰਜਨ ਨੰਬਰ।
- **LastFullScanTime**: ਆਖਰੀ ਪੂਰੇ ਸਕੈਨ ਦੀ ਮਿਤੀ ਅਤੇ ਸਮਾਂ।
- **LastQuickScanTime**: ਆਖਰੀ ਤੇਜ਼ ਸਕੈਨ ਦੀ ਮਿਤੀ ਅਤੇ ਸਮਾਂ।
- **RealTimeProtectionEnabled**: ਰੀਅਲ-ਟਾਈਮ ਸੁਰੱਖਿਆ ਚਾਲੂ ਹੈ ਜਾਂ ਬੰਦ, ਇਹ ਦੱਸਦਾ ਹੈ।

`Get-MpComputerStatus` ਨਾਲ ਨਿਯਮਿਤ ਜਾਂਚ **ਸੰਭਾਵੀ ਖ਼ਤਰਿਆਂ** ਵਿਰੁੱਧ ਸਿਸਟਮ ਦੀ ਸੁਰੱਖਿਆ ਬਾਰੇ ਜਾਣੂ ਰੱਖਦੀ ਹੈ।

### 2. [**Update-MpSignature**](https://learn.microsoft.com/en-us/powershell/module/defender/update-mpsignature?view=windowsserver2022-ps)

`Update-MpSignature` Windows Defender ਦੀਆਂ ਐਂਟੀਵਾਇਰਸ ਸਿਗਨੇਚਰਾਂ ਨੂੰ ਹੱਥੀਂ ਅੱਪਡੇਟ ਕਰਦਾ ਹੈ। ਇਨ੍ਹਾਂ ਸਿਗਨੇਚਰਾਂ ਵਿੱਚ ਜਾਣੇ-ਪਛਾਣੇ ਮੈਲਵੇਅਰ ਦੀ ਅਹਿਮ ਜਾਣਕਾਰੀ ਹੁੰਦੀ ਹੈ, ਜਿਸ ਨਾਲ Windows Defender ਖ਼ਤਰੇ ਪਛਾਣ ਕੇ ਰੋਕਦਾ ਹੈ। ਕਮਾਂਡ ਚਲਾਉਣ ਨਾਲ ਨਵੀਆਂ ਸਿਗਨੇਚਰਾਂ ਮਿਲਦੀਆਂ ਹਨ ਅਤੇ ਨਵੇਂ ਖ਼ਤਰਿਆਂ ਵਿਰੁੱਧ ਸੁਰੱਖਿਆ ਵਧਦੀ ਹੈ।

ਸਿਗਨੇਚਰਾਂ ਨੂੰ ਹੱਥੀਂ ਅੱਪਡੇਟ ਕਰਨ ਲਈ ਪ੍ਰਸ਼ਾਸਕੀ ਅਧਿਕਾਰਾਂ ਵਾਲੇ PowerShell ਸੈਸ਼ਨ ਵਿੱਚ ਇਹ ਚਲਾਓ:

```powershell
Update-MpSignature
```

ਇਹ ਅੱਪਡੇਟ ਸ਼ੁਰੂ ਕਰਦਾ ਹੈ। Windows Defender, Microsoft ਸਰਵਰਾਂ ਨਾਲ ਜੁੜ ਕੇ **ਨਵੀਆਂ ਐਂਟੀਵਾਇਰਸ ਸਿਗਨੇਚਰਾਂ** ਡਾਊਨਲੋਡ ਕਰਦਾ ਹੈ। ਅੱਪਡੇਟ ਪੂਰਾ ਹੋਣ 'ਤੇ ਇਸ ਕੋਲ ਜਾਣੇ-ਪਛਾਣੇ ਮੈਲਵੇਅਰ ਬਾਰੇ ਤਾਜ਼ਾ ਜਾਣਕਾਰੀ ਹੁੰਦੀ ਹੈ ਅਤੇ ਇਹ ਖ਼ਤਰੇ ਪਛਾਣਨ ਤੇ ਹਟਾਉਣ ਵਿੱਚ ਮਦਦ ਕਰਦਾ ਹੈ।

ਬਦਲਦੇ ਮੈਲਵੇਅਰ ਅਤੇ ਸਾਈਬਰ ਖ਼ਤਰਿਆਂ ਤੋਂ ਸੁਰੱਖਿਆ ਲਈ ਸਿਗਨੇਚਰਾਂ ਤਾਜ਼ਾ ਰੱਖੋ। `Update-MpSignature` ਨਿਯਮਿਤ ਚਲਾਓ ਤਾਂ ਜੋ Windows Defender ਤੁਹਾਡੇ ਸਿਸਟਮ ਦੀ ਪ੍ਰਭਾਵਸ਼ਾਲੀ ਰੱਖਿਆ ਕਰੇ।

### 3. [**Set-MpPreference**](https://learn.microsoft.com/en-us/powershell/module/defender/set-mppreference?view=windowsserver2022-ps)

`Set-MpPreference` ਨਾਲ ਤੁਸੀਂ **Windows Defender** ਦੀਆਂ ਸੈਟਿੰਗਾਂ ਆਪਣੀਆਂ ਸੁਰੱਖਿਆ ਲੋੜਾਂ ਮੁਤਾਬਕ ਬਦਲ ਸਕਦੇ ਹੋ। ਇਸ ਵਿੱਚ **ਰੀਅਲ-ਟਾਈਮ ਸੁਰੱਖਿਆ**, **ਕਲਾਊਡ-ਅਧਾਰਿਤ ਸੁਰੱਖਿਆ** ਅਤੇ **ਨੈੱਟਵਰਕ ਜਾਂਚ ਸਿਸਟਮ** ਦੀਆਂ ਸੈਟਿੰਗਾਂ ਸ਼ਾਮਲ ਹਨ।

ਮਿਸਾਲ ਵਜੋਂ `Set-MpPreference` ਨਾਲ ਰੀਅਲ-ਟਾਈਮ ਸੁਰੱਖਿਆ ਚਾਲੂ ਜਾਂ ਬੰਦ ਕਰੋ। ਇਹ ਸਿਸਟਮ ਵਿੱਚ ਨੁਕਸਾਨਦਾਇਕ ਕਾਰਵਾਈਆਂ ਵੇਖਦੀ ਹੈ ਅਤੇ ਖ਼ਤਰਿਆਂ ਦਾ ਤੁਰੰਤ ਜਵਾਬ ਦਿੰਦੀ ਹੈ। ਚਾਲੂ ਕਰਨ ਲਈ:

```powershell
Set-MpPreference -DisableRealtimeMonitoring:$false
```

ਕਲਾਊਡ-ਅਧਾਰਿਤ ਸੁਰੱਖਿਆ ਵੀ ਬਦਲੀ ਜਾ ਸਕਦੀ ਹੈ। ਇਹ ਖ਼ਤਰੇ ਪਛਾਣਨ ਅਤੇ ਨਵੇਂ ਖ਼ਤਰਿਆਂ ਦਾ ਤੇਜ਼ ਜਵਾਬ ਦੇਣ ਲਈ ਕਲਾਊਡ ਸਰੋਤ ਵਰਤਦੀ ਹੈ। ਚਾਲੂ ਕਰਨ ਲਈ:

```powershell
Set-MpPreference -EnableCloudProtection:$true
```

`Set-MpPreference` ਨੈੱਟਵਰਕ ਜਾਂਚ ਸਿਸਟਮ ਦੀਆਂ ਸੈਟਿੰਗਾਂ ਵੀ ਬਦਲਦਾ ਹੈ। ਇਹ ਸ਼ੱਕੀ ਕਾਰਵਾਈਆਂ ਅਤੇ ਸੰਭਾਵੀ ਖ਼ਤਰਿਆਂ ਲਈ ਨੈੱਟਵਰਕ ਆਵਾਜਾਈ ਦਾ ਵਿਸ਼ਲੇਸ਼ਣ ਕਰਦਾ ਹੈ। ਸੈਟਿੰਗ ਬਦਲਣ ਲਈ:

```powershell
Set-MpPreference -DisableIOAVProtection:$false
```

`Set-MpPreference` ਨਾਲ ਇਹ ਚੋਣਾਂ ਆਪਣੀਆਂ ਲੋੜਾਂ ਅਨੁਸਾਰ ਕਰੋ ਅਤੇ **Windows Defender** ਨੂੰ ਮੈਲਵੇਅਰ ਤੇ ਹੋਰ ਨੁਕਸਾਨਦਾਇਕ ਕਾਰਵਾਈਆਂ ਵਿਰੁੱਧ ਸਿਸਟਮ ਦੀ ਰੱਖਿਆ ਲਈ ਵਰਤੋ।

### 4. [**Start-MpScan**](https://learn.microsoft.com/en-us/powershell/module/defender/start-mpscan?view=windowsserver2022-ps)

`Start-MpScan` ਸਿਸਟਮ 'ਤੇ ਮੈਲਵੇਅਰ ਸਕੈਨ ਸ਼ੁਰੂ ਕਰਦਾ ਹੈ ਤਾਂ ਜੋ ਤੁਸੀਂ ਨੁਕਸਾਨਦਾਇਕ ਫ਼ਾਈਲਾਂ ਲੱਭ ਕੇ ਹਟਾ ਸਕੋ। ਇਸ ਨਾਲ **ਤੇਜ਼**, **ਪੂਰੇ** ਅਤੇ ਖਾਸ ਰਾਹਾਂ ਲਈ **ਕਸਟਮ ਸਕੈਨ** ਕੀਤੇ ਜਾ ਸਕਦੇ ਹਨ।

`Start-MpScan` ਨਾਲ **ਤੇਜ਼ ਸਕੈਨ** ਕਰਨ ਲਈ ਇਹ PowerShell ਕਮਾਂਡ ਚਲਾਓ:

```powershell
Start-MpScan -ScanType QuickScan
```

ਤੇਜ਼ ਸਕੈਨ ਸਿਸਟਮ ਦੇ ਅਹਿਮ ਹਿੱਸਿਆਂ 'ਤੇ ਧਿਆਨ ਦਿੰਦਾ ਹੈ ਜਿੱਥੇ ਮੈਲਵੇਅਰ ਅਕਸਰ ਮਿਲਦਾ ਹੈ ਅਤੇ ਸੰਭਾਵੀ ਖ਼ਤਰਿਆਂ ਦੀ ਜਲਦੀ ਜਾਂਚ ਕਰਦਾ ਹੈ।

ਸਾਰੀਆਂ ਫ਼ਾਈਲਾਂ ਅਤੇ ਡਾਇਰੈਕਟਰੀਆਂ ਜਾਂਚਣ ਲਈ `Start-MpScan` ਨਾਲ **ਪੂਰਾ ਸਕੈਨ** ਸ਼ੁਰੂ ਕਰੋ:

```powershell
Start-MpScan -ScanType FullScan
```

**ਪੂਰਾ ਸਕੈਨ** ਮੈਲਵੇਅਰ ਦੀ ਵਿਸਥਾਰ ਨਾਲ ਜਾਂਚ ਕਰਦਾ ਹੈ, ਪਰ ਤੇਜ਼ ਸਕੈਨ ਨਾਲੋਂ ਵੱਧ ਸਮਾਂ ਲੈ ਸਕਦਾ ਹੈ।

ਪਹਿਲਾਂ ਤੋਂ ਬਣੇ ਸਕੈਨਾਂ ਤੋਂ ਇਲਾਵਾ, `Start-MpScan` ਨਾਲ ਖਾਸ ਰਾਹ ਜਾਂ ਫ਼ਾਈਲ ਜਾਂਚੋ। ਮਿਸਾਲ ਵਜੋਂ ਕਿਸੇ ਡਾਇਰੈਕਟਰੀ ਨੂੰ ਸਕੈਨ ਕਰਨ ਲਈ:

```powershell
Start-MpScan -ScanType CustomScan -ScanPath "C:\Path\To\Directory"
```

ਇਹ ਕਮਾਂਡ ਚੁਣੀ ਡਾਇਰੈਕਟਰੀ ਵਿੱਚ ਕਸਟਮ ਸਕੈਨ ਸ਼ੁਰੂ ਕਰਦੀ ਹੈ ਅਤੇ ਮੈਲਵੇਅਰ ਦੀ ਜਾਂਚ ਸਿਸਟਮ ਦੇ ਖਾਸ ਹਿੱਸੇ ਤੱਕ ਸੀਮਿਤ ਕਰਦੀ ਹੈ।

`Start-MpScan` ਨਾਲ ਸਕੈਨ ਤੈਅ ਕਰੋ, ਸੁਰੱਖਿਆ ਪ੍ਰਕਿਰਿਆਵਾਂ ਸਵੈਚਾਲਿਤ ਕਰੋ ਅਤੇ ਮੈਲਵੇਅਰ ਦੀ ਨਿਯਮਿਤ ਪਛਾਣ ਤੇ ਸੰਭਾਲ ਯਕੀਨੀ ਬਣਾਓ।

### 5. [**Get-MpThreatCatalog**](https://learn.microsoft.com/en-us/powershell/module/defender/get-mpthreatcatalog?view=windowsserver2022-ps)

`Get-MpThreatCatalog` ਜਾਣੇ-ਪਛਾਣੇ ਖ਼ਤਰਿਆਂ ਅਤੇ ਉਨ੍ਹਾਂ ਦੀਆਂ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਬਾਰੇ ਵੇਰਵੇ ਦਿੰਦਾ ਹੈ। ਸੂਚੀ ਵਿੱਚ ਗੰਭੀਰਤਾ, ਸੰਬੰਧਿਤ ਫ਼ਾਈਲਾਂ ਦੇ ਨਾਂ ਅਤੇ ਖ਼ਤਰਾ ਘਟਾਉਣ ਲਈ ਸੁਝਾਏ ਕਦਮ ਸ਼ਾਮਲ ਹਨ।

`Get-MpThreatCatalog` ਨਾਲ ਕਿਸੇ ਖਾਸ ਖ਼ਤਰੇ ਦੀ ਜਾਣਕਾਰੀ ਲੈਣ ਲਈ:

1. ਪ੍ਰਸ਼ਾਸਕੀ ਅਧਿਕਾਰਾਂ ਵਾਲਾ PowerShell ਸੈਸ਼ਨ ਖੋਲ੍ਹੋ।
2. ਇਹ ਕਮਾਂਡ ਚਲਾਓ:

```powershell
   Get-MpThreatCatalog
```

ਇਹ ਕਮਾਂਡ ਜਾਣੇ-ਪਛਾਣੇ ਖ਼ਤਰਿਆਂ ਅਤੇ ਉਨ੍ਹਾਂ ਦੇ ਵੇਰਵਿਆਂ ਦੀ ਸੂਚੀ ਦਿਖਾਉਂਦੀ ਹੈ।

`Get-MpThreatCatalog` ਦੇ ਨਤੀਜੇ ਵਿੱਚ ਅਹਿਮ ਜਾਣਕਾਰੀ ਹੁੰਦੀ ਹੈ, ਜਿਵੇਂ:

- **ThreatID**: ਖ਼ਤਰੇ ਦਾ ਵਿਲੱਖਣ ਪਛਾਣ ਨੰਬਰ।
- **Severity**: ਖ਼ਤਰੇ ਦੀ ਗੰਭੀਰਤਾ, Low (ਘੱਟ) ਤੋਂ Severe (ਬਹੁਤ ਗੰਭੀਰ) ਤੱਕ।
- **Name**: ਖ਼ਤਰੇ ਦਾ ਨਾਂ ਜਾਂ ਵੇਰਵਾ।
- **Path**: ਖ਼ਤਰੇ ਨਾਲ ਜੁੜੀ ਫ਼ਾਈਲ ਦਾ ਰਾਹ।
- **RecommendedAction**: ਖ਼ਤਰਾ ਘਟਾਉਣ ਲਈ ਸੁਝਾਏ ਕਦਮ।

`Get-MpThreatCatalog` ਦੀ ਜਾਣਕਾਰੀ ਸੰਭਾਵੀ ਖ਼ਤਰਿਆਂ ਨੂੰ ਸਮਝਣ ਅਤੇ ਢੁਕਵੀਂ ਕਾਰਵਾਈ ਚੁਣਨ ਵਿੱਚ ਮਦਦ ਕਰਦੀ ਹੈ। ਖ਼ਤਰੇ ਨੂੰ ਅਲੱਗ ਕਰਨਾ, ਹਟਾਉਣਾ ਜਾਂ ਨਿਗਰਾਨੀ ਕਰਨੀ ਹੋਵੇ, ਵੇਰਵੇਦਾਰ ਸੂਚੀ ਸੁਰੱਖਿਆ ਘਟਨਾਵਾਂ ਦਾ ਪ੍ਰਭਾਵਸ਼ਾਲੀ ਜਵਾਬ ਦੇਣ ਵਿੱਚ ਮਦਦ ਕਰਦੀ ਹੈ।

`Get-MpThreatCatalog` ਵਰਤਣ ਅਤੇ ਨਤੀਜੇ ਸਮਝਣ ਲਈ Microsoft ਦੇ ਅਧਿਕਾਰਤ ਦਸਤਾਵੇਜ਼ ਵੇਖੋ।

ਚੌਕਸ ਰਹੋ ਅਤੇ ਬਦਲਦੇ ਖ਼ਤਰਿਆਂ ਤੋਂ ਜਾਣੂ ਰਹਿਣ ਤੇ ਸਿਸਟਮ ਦੀ ਸੁਰੱਖਿਆ ਵਧਾਉਣ ਲਈ `Get-MpThreatCatalog` ਨਿਯਮਿਤ ਚਲਾਓ।

### 6. [**Add-MpPreference**](https://learn.microsoft.com/en-us/powershell/module/defender/add-mppreference?view=windowsserver2022-ps)

`Add-MpPreference` Windows Defender ਵਿੱਚ ਛੋਟਾਂ ਜੋੜਦਾ ਹੈ ਅਤੇ ਸਕੈਨ ਤੇ ਰੀਅਲ-ਟਾਈਮ ਸੁਰੱਖਿਆ ਦਾ ਵਿਹਾਰ ਬਦਲਦਾ ਹੈ। ਛੋਟਾਂ ਰਾਹੀਂ ਤੁਸੀਂ ਉਹ ਫ਼ਾਈਲਾਂ, ਫੋਲਡਰ ਜਾਂ ਪ੍ਰਕਿਰਿਆਵਾਂ ਦੱਸਦੇ ਹੋ ਜਿਨ੍ਹਾਂ ਨੂੰ ਸੁਰੱਖਿਆ ਸਕੈਨ ਜਾਂ ਰੀਅਲ-ਟਾਈਮ ਸੁਰੱਖਿਆ ਦੌਰਾਨ ਛੱਡਣਾ ਹੈ।

`Add-MpPreference` ਨਾਲ ਛੋਟ ਜੋੜਨ ਲਈ, ਛੱਡਣ ਵਾਲੀ ਫ਼ਾਈਲ, ਫੋਲਡਰ ਜਾਂ ਪ੍ਰਕਿਰਿਆ ਦਾ ਰਾਹ ਜਾਂ ਨਾਂ ਦਿਓ। ਇਹ ਮਿਸਾਲ ਫੋਲਡਰ ਲਈ ਛੋਟ ਜੋੜਦੀ ਹੈ:

```powershell
Add-MpPreference -ExclusionPath "C:\MyFolder"
```

ਇਸ ਨਾਲ Windows Defender ਚੁਣੇ ਫੋਲਡਰ ਨੂੰ ਸਕੈਨ ਨਹੀਂ ਕਰਦਾ, ਜਿਸ ਨਾਲ ਬੇਲੋੜੀਆਂ ਚੇਤਾਵਨੀਆਂ ਅਤੇ ਕੰਮ ਵਿੱਚ ਰੁਕਾਵਟ ਘਟਦੀ ਹੈ।

ਭਰੋਸੇਯੋਗ ਐਪਾਂ, ਵਿਕਾਸ ਮਾਹੌਲਾਂ ਜਾਂ ਗਲਤ ਪਛਾਣ ਪੈਦਾ ਕਰਨ ਵਾਲੀਆਂ ਖਾਸ ਫ਼ਾਈਲਾਂ ਲਈ ਛੋਟਾਂ ਲਾਭਦਾਇਕ ਹਨ। `Add-MpPreference` ਨਾਲ Windows Defender ਨੂੰ ਆਪਣੀਆਂ ਸੁਰੱਖਿਆ ਲੋੜਾਂ ਮੁਤਾਬਕ ਕਰੋ।

`Add-MpPreference` ਦੀਆਂ ਛੋਟਾਂ ਵਰਤ ਕੇ ਸਿਸਟਮ ਸੁਰੱਖਿਅਤ ਰੱਖੋ ਅਤੇ ਗਲਤ ਪਛਾਣ ਤੇ ਬੇਲੋੜੀਆਂ ਸਕੈਨ ਰੁਕਾਵਟਾਂ ਘਟਾਓ।

## 2026 Defender ਕਮਾਂਡ ਜਾਂਚਾਂ

Defender ਕਮਾਂਡਾਂ ਉੱਚੇ ਅਧਿਕਾਰਾਂ ਵਾਲੇ ਸੈਸ਼ਨ ਤੋਂ ਸਿਰਫ਼ ਉਦੋਂ ਚਲਾਓ ਜਦੋਂ ਕੰਮ ਲਈ ਇਹ ਅਧਿਕਾਰ ਲੋੜੀਂਦੇ ਹੋਣ। ਪੈਰਾਮੀਟਰ ਵਰਤਣ ਤੋਂ ਪਹਿਲਾਂ ਟੀਚੇ ਵਾਲੇ Windows ਵਰਜਨ ਲਈ ਮੌਜੂਦਾ ਮੋਡੀਊਲ ਮਦਦ ਵੇਖੋ। ਮੌਜੂਦਾ ਸੰਰਚਨਾ ਦਰਜ ਕਰੋ, ਇੱਕ ਵਾਰ ਵਿੱਚ ਇੱਕ ਸੈਟਿੰਗ ਬਦਲੋ, ਨਤੀਜਾ ਜਾਂਚੋ ਅਤੇ ਵਾਪਸੀ ਕਮਾਂਡ ਲਿਖੋ।

ਲਾਭਦਾਇਕ ਜਾਂਚਾਂ ਵਿੱਚ ਸੁਰੱਖਿਆ ਸਥਿਤੀ, ਸਿਗਨੇਚਰਾਂ ਦੀ ਉਮਰ, ਛੋਟਾਂ, ਤਰਜੀਹਾਂ, ਸਕੈਨ ਇਤਿਹਾਸ ਅਤੇ ਹਾਲੀਆ ਪਛਾਣਾਂ ਵੇਖਣਾ ਸ਼ਾਮਲ ਹੈ। ਛੋਟਾਂ ਸੀਮਿਤ ਰੱਖੋ ਅਤੇ ਜ਼ਿੰਮੇਵਾਰ ਵਿਅਕਤੀ ਤੇ ਮਿਆਦ ਮੁੱਕਣ ਦੀ ਤਾਰੀਖ ਦਰਜ ਕਰੋ। ਮੌਜੂਦਾ cmdlet ਅਤੇ ਵਿਹਾਰ ਲਈ [Microsoft Defender PowerShell ਮੋਡੀਊਲ ਦੇ ਦਸਤਾਵੇਜ਼](https://learn.microsoft.com/en-us/powershell/module/defender/) ਅਤੇ [Microsoft Defender Antivirus ਦੇ ਦਸਤਾਵੇਜ਼](https://learn.microsoft.com/en-us/defender-endpoint/microsoft-defender-antivirus-windows) ਵੇਖੋ।

## ਸਿੱਟਾ

Windows Defender PowerShell ਕਮਾਂਡਾਂ Windows ਸਿਸਟਮ ਦੀ ਸੁਰੱਖਿਆ ਸੰਭਾਲਣ ਅਤੇ ਵਧਾਉਣ ਲਈ **ਔਜ਼ਾਰਾਂ ਦਾ ਮਜ਼ਬੂਤ ਸਮੂਹ** ਦਿੰਦੀਆਂ ਹਨ। ਇਨ੍ਹਾਂ ਨਾਲ *ਸੁਰੱਖਿਆ ਕਾਰਵਾਈਆਂ ਸਵੈਚਾਲਿਤ*, *ਉੱਨਤ ਸੈਟਿੰਗਾਂ ਸੰਰਚਿਤ* ਅਤੇ Windows Defender ਨੂੰ ਕੰਮਕਾਜ ਵਿੱਚ ਸ਼ਾਮਲ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ। ਤੁਸੀਂ ਸਿਸਟਮ ਪ੍ਰਸ਼ਾਸਕ ਹੋਵੋ ਜਾਂ ਤਜਰਬੇਕਾਰ ਵਰਤੋਂਕਾਰ, ਇਹ ਕਮਾਂਡਾਂ ਸਿਸਟਮ ਦੀ ਸੁਰੱਖਿਆ ਮਜ਼ਬੂਤ ਕਰਦੀਆਂ ਹਨ।

PowerShell ਕਮਾਂਡਾਂ ਚਲਾਉਣ ਤੋਂ ਪਹਿਲਾਂ ਸਾਵਧਾਨ ਰਹੋ ਅਤੇ ਉਨ੍ਹਾਂ ਦਾ ਅਸਰ ਸਮਝੋ। Windows Defender PowerShell ਕਮਾਂਡਾਂ ਬਾਰੇ ਆਪਣਾ ਗਿਆਨ ਵਰਤ ਕੇ ਬਦਲਦੇ ਖ਼ਤਰਿਆਂ ਤੋਂ ਸਿਸਟਮ ਦੀ ਸਰਗਰਮ ਰੱਖਿਆ ਕਰੋ।

## ਹਵਾਲੇ

1. Microsoft Docs - [Windows PowerShell ਵਿੱਚ Windows Defender Cmdlet](https://docs.microsoft.com/en-us/powershell/module/defender/?view=windowsserver2019-ps)
2. Microsoft Docs - [Windows PowerShell ਦੀ ਜਾਣ-ਪਛਾਣ](https://docs.microsoft.com/en-us/powershell/scripting/overview?view=powershell-7.1)
