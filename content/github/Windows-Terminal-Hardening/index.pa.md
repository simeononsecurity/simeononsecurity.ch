---
title: "ਵਿੰਡੋਜ਼ ਕਮਾਂਡ ਪ੍ਰੋਂਪਟ ਅਤੇ ਪਾਵਰਸ਼ੇਲ ਹਾਰਡਨਿੰਗ"
date: 2020-11-18
toc: true
draft: false
description: "ਵਿੰਡੋਜ਼ ਕਮਾਂਡ ਪ੍ਰੋਂਪਟ ਅਤੇ ਪਾਵਰਸ਼ੇਲ ਨੂੰ ਸਾਡੀ ਵਿਆਪਕ ਹਾਰਡਨਿੰਗ ਸਕ੍ਰਿਪਟ ਅਤੇ ਦਸਤਾਵੇਜ਼ਾਂ ਨਾਲ ਸੁਰੱਖਿਅਤ ਕਰੋ, ਸਿਸਟਮ ਸੁਰੱਖਿਆ ਅਤੇ ਪਾਲਣਾ ਨੂੰ ਵਧਾਓ।"
tags: ["ਪਾਵਰਸ਼ੇਲ", "ਸਖਤ ਕਰਨਾ", "ਵਿੰਡੋਜ਼ ਕਮਾਂਡ ਪ੍ਰੋਂਪਟ", "ਸੁਰੱਖਿਆ", "ਪਾਲਣਾ", "ਆਟੋਮੇਸ਼ਨ", "ਸੀਮਤ ਭਾਸ਼ਾ ਮੋਡ", "PowerShell ਲਾਗਿੰਗ", "PowerShell ਸਕ੍ਰਿਪਟ", "WSMAN", "PSRemoting", "ਐਂਟਰਪ੍ਰਾਈਜ਼ ਸੁਰੱਖਿਆ", "ਬਲੂ ਟੀਮ", "ਸਾਈਬਰ ਸੁਰੱਖਿਆ", "ਵਧੀਆ ਅਭਿਆਸ", "ਕਮਾਂਡ ਪ੍ਰੋਂਪਟ ਨੂੰ ਅਸਮਰੱਥ ਬਣਾਓ", "PowerShell v2 ਨੂੰ ਅਸਮਰੱਥ ਕਰੋ", "GitHub ਰਿਪੋਜ਼ਟਰੀ", "ਵਿੰਡੋਜ਼ ਡਿਫੈਂਡਰ", "ਮਾਈਕ੍ਰੋਸਾਫਟ"]
---
 ਅਤੇ ਵਿੰਡੋਜ਼ ਕਮਾਂਡ ਪ੍ਰੋਂਪਟ ਅਤੇ ਪਾਵਰਸ਼ੇਲ ਨੂੰ ਸਖ਼ਤ ਕਰਨ ਲਈ ਦਸਤਾਵੇਜ਼

## ਇਹ ਸਕ੍ਰਿਪਟ ਕੀ ਕਰਦੀ ਹੈ?
- ਕਮਾਂਡ ਪ੍ਰੋਂਪਟ ਨੂੰ ਅਯੋਗ ਕਰਦਾ ਹੈ
- PowerShell v2 ਨੂੰ ਅਯੋਗ ਕਰਦਾ ਹੈ
- WSMAN ਅਤੇ PSRemoting ਨੂੰ ਅਸਮਰੱਥ ਬਣਾਉਂਦਾ ਹੈ
- PowerShell ਸੀਮਤ ਭਾਸ਼ਾ ਮੋਡ ਨੂੰ ਸਮਰੱਥ ਬਣਾਉਂਦਾ ਹੈ
- PowerShell ਲੌਗਿੰਗ ਨੂੰ ਸਮਰੱਥ ਬਣਾਉਂਦਾ ਹੈ

## ਸਿਫਾਰਸ਼ੀ ਰੀਡਿੰਗ:
-[PowerShell Best Practices](https://www.digitalshadows.com/blog-and-research/powershell-security-best-practices/)
-[PowerShell Constrained Language Mode](https://devblogs.microsoft.com/powershell/powershell-constrained-language-mode/)
-[Securing PowerShell in the Enterprise](https://www.cyber.gov.au/acsc/view-all-content/publications/securing-powershell-enterprise)
-[Windows Defender Hardening](https://github.com/simeononsecurity/Windows-Defender-Hardening)

## ਲੋੜੀਂਦੀਆਂ ਫਾਈਲਾਂ ਨੂੰ ਡਾਉਨਲੋਡ ਕਰੋ:

ਤੋਂ ਲੋੜੀਂਦੀਆਂ ਫਾਈਲਾਂ ਡਾਊਨਲੋਡ ਕਰੋ[GitHub Repository](https://github.com/simeononsecurity/Windows-Terminal-Hardening)

## ਸਕ੍ਰਿਪਟ ਨੂੰ ਕਿਵੇਂ ਚਲਾਉਣਾ ਹੈ:

**ਸਕ੍ਰਿਪਟ ਨੂੰ ਇਸ ਤਰ੍ਹਾਂ ਐਕਸਟਰੈਕਟ ਕੀਤੇ GitHub ਡਾਊਨਲੋਡ ਤੋਂ ਲਾਂਚ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ:**
```
.\sos-windowsterminalhardening.ps1
```
