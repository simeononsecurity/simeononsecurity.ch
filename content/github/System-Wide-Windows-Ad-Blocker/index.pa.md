---
title: "ਬਿਹਤਰ ਗੋਪਨੀਯਤਾ ਅਤੇ ਸੁਰੱਖਿਆ ਲਈ Windows 10 ਸਿਸਟਮ-ਵਾਈਡ ਐਡ ਬਲੌਕਰ ਸਕ੍ਰਿਪਟ"
date: 2021-04-02
lastmod: 2026-11-23
toc: true
draft: false
description: "Windows ਵਿੱਚ StevenBlack ਸੂਚੀ ਦੇ ਡੋਮੇਨ ਬਲੌਕ ਕਰੋ। ਇਹ PowerShell ਸਕ੍ਰਿਪਟ ਤੁਹਾਡੀਆਂ ਕਸਟਮ hosts ਐਂਟਰੀਆਂ ਨੂੰ ਜਿਉਂ ਦਾ ਤਿਉਂ ਰੱਖਦੀ ਹੈ।"
tags: ["ਵਿੰਡੋਜ਼ 10", "ਵਿਗਿਆਪਨ ਬਲੌਕਰ", "ਟੈਲੀਮੈਟਰੀ ਬਲਾਕਿੰਗ", "PowerShell ਸਕ੍ਰਿਪਟ", "ਸਿਸਟਮ-ਵਿਆਪੀ ਵਿਗਿਆਪਨ-ਬਲੌਕਿੰਗ", "ਗੋਪਨੀਯਤਾ", "ਸੁਰੱਖਿਆ"]
---

Windows ਵਿੱਚ StevenBlack ਸੂਚੀ ਦੇ ਡੋਮੇਨ ਬਲੌਕ ਕਰੋ। ਇਹ PowerShell ਸਕ੍ਰਿਪਟ ਤੁਹਾਡੀਆਂ ਕਸਟਮ hosts ਐਂਟਰੀਆਂ ਨੂੰ ਜਿਉਂ ਦਾ ਤਿਉਂ ਰੱਖਦੀ ਹੈ।

## ਤਿਆਰੀ ਅਤੇ ਝਲਕ

ਪੂਰੀ ਰਿਪੋਜ਼ਟਰੀ ਡਾਊਨਲੋਡ ਕਰਕੇ ਖੋਲ੍ਹੋ। ਚਲਾਉਣ ਤੋਂ ਪਹਿਲਾਂ [GitHub README](https://github.com/simeononsecurity/System-Wide-Windows-Ad-Blocker/blob/main/README.md) ਅਤੇ ਸਕ੍ਰਿਪਟ ਪੜ੍ਹੋ। ਖੋਲ੍ਹੇ ਫੋਲਡਰ ਵਿੱਚ Windows PowerShell 5.1 ਜਾਂ PowerShell 7 ਨੂੰ ਪ੍ਰਬੰਧਕ ਵਜੋਂ ਖੋਲ੍ਹੋ। ਪਹਿਲਾਂ ਅਸਥਾਈ Windows ਸਿਸਟਮ ਉੱਤੇ DNS ਅਤੇ ਲੋੜੀਂਦੀਆਂ ਐਪਾਂ ਦੀ ਜਾਂਚ ਕਰੋ।

ਪਹਿਲਾਂ ਤਬਦੀਲੀਆਂ ਦੀ ਝਲਕ ਵੇਖੋ। ਲਾਗੂ ਕਰਨ ਲਈ ਤਿਆਰ ਹੋਵੋ ਤਾਂ ਦੂਜੀ ਕਮਾਂਡ ਵੱਖਰੇ ਤੌਰ ’ਤੇ ਚਲਾਓ।

```powershell
.\sos-system-wide-windows-ad-block.ps1 -WhatIf
```

```powershell
.\sos-system-wide-windows-ad-block.ps1
```

## ਅਸਲ hosts ਫਾਈਲ ਮੁੜ ਬਹਾਲ ਕਰੋ

ਪਹਿਲਾਂ ਬਹਾਲੀ ਦੀ ਝਲਕ ਵੇਖੋ। ਤਿਆਰ ਹੋਣ ’ਤੇ ਦੂਜੀ ਕਮਾਂਡ ਵੱਖਰੇ ਤੌਰ ’ਤੇ ਚਲਾਓ।

```powershell
.\sos-system-wide-windows-ad-block.ps1 -Mode Restore -WhatIf
```

```powershell
.\sos-system-wide-windows-ad-block.ps1 -Mode Restore
```

ਬਹਾਲੀ ਪੂਰੀ ਹੋਣ ਤੱਕ ਬੈਕਅੱਪ ਨੂੰ ਨਾ ਬਦਲੋ। ਜੇ ਲਾਗੂ ਕਰਨ ਤੋਂ ਬਾਅਦ ਕਿਸੇ ਵਿਅਕਤੀ ਜਾਂ ਐਪ ਨੇ hosts ਫਾਈਲ ਬਦਲੀ ਹੋਵੇ, ਤਾਂ ਬਹਾਲੀ ਰੁਕ ਜਾਂਦੀ ਹੈ। ਮੁੜ ਕੋਸ਼ਿਸ਼ ਤੋਂ ਪਹਿਲਾਂ ਤਬਦੀਲੀਆਂ ਸੰਭਾਲੋ ਅਤੇ ਉਨ੍ਹਾਂ ਦਾ ਮੇਲ ਕਰੋ।

## ਬਲੌਕ ਸੂਚੀ

- [StevenBlack/hosts](https://github.com/StevenBlack/hosts)
- [ਸਮੱਸਿਆ ਦੀ ਰਿਪੋਰਟ ਕਰੋ](https://github.com/simeononsecurity/System-Wide-Windows-Ad-Blocker/issues)
