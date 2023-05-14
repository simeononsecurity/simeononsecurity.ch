---
title: "ਬਿਹਤਰ ਗੋਪਨੀਯਤਾ ਅਤੇ ਸੁਰੱਖਿਆ ਲਈ Windows 10 ਸਿਸਟਮ-ਵਾਈਡ ਐਡ ਬਲੌਕਰ ਸਕ੍ਰਿਪਟ"
date: 2021-04-02
toc: true
draft: false
description: "ਇਸ ਸ਼ਕਤੀਸ਼ਾਲੀ PowerShell ਸਕ੍ਰਿਪਟ ਦੀ ਵਰਤੋਂ ਕਰਦੇ ਹੋਏ Windows 10 'ਤੇ ਵਿਗਿਆਪਨਾਂ, ਟਰੈਕਰਾਂ ਅਤੇ ਟੈਲੀਮੈਟਰੀ ਨੂੰ ਬਲਾਕ ਕਰੋ ਜੋ ਸਿਸਟਮ-ਵਿਆਪਕ ਵਿਗਿਆਪਨ-ਬਲੌਕਿੰਗ ਲਈ ਹੋਸਟ ਫਾਈਲ ਅਤੇ ਵਿੰਡੋਜ਼ ਫਾਇਰਵਾਲ ਦੀ ਵਰਤੋਂ ਕਰਦੀ ਹੈ।"
tags: ["ਵਿੰਡੋਜ਼ 10", "ਵਿਗਿਆਪਨ ਬਲੌਕਰ", "ਟੈਲੀਮੈਟਰੀ ਬਲਾਕਿੰਗ", "PowerShell ਸਕ੍ਰਿਪਟ", "ਸਿਸਟਮ-ਵਿਆਪੀ ਵਿਗਿਆਪਨ-ਬਲੌਕਿੰਗ", "ਗੋਪਨੀਯਤਾ", "ਸੁਰੱਖਿਆ", "EasyList", "ਆਸਾਨ ਪਰਦੇਦਾਰੀ", "NoCoin ਫਿਲਟਰ ਸੂਚੀ", "AdGuard DNS ਫਿਲਟਰ", "YoYo ਸੂਚੀਆਂ", "ਪੀਟਰ ਲੋਵੇ ਦਾ ਵਿਗਿਆਪਨ ਟਰੈਕਿੰਗ ਮਾਲਵੇਅਰ ਸਰਵਰ", "ਵਿੰਡੋਜ਼ ਫਾਇਰਵਾਲ", "ਡੋਮੇਨ ਸੂਚੀਆਂ", "ਵਿੰਡੋਜ਼ ਟਰੈਕਰਾਂ ਨੂੰ ਬਲੌਕ ਕਰੋ", "ਬਲਾਕ ਟਰੈਕਰ", "ਬਲਾਕ ਵਿਗਿਆਪਨ", "ਬਲਾਕ ਟਰੈਕਿੰਗ"]
---

## ਵਰਣਨ:
ਇਹ ਸਕ੍ਰਿਪਟ ਮੇਜ਼ਬਾਨ ਫਾਈਲ ਦੁਆਰਾ ਟੈਲੀਮੈਟਰੀ ਨਾਲ ਸਬੰਧਤ ਡੋਮੇਨ ਅਤੇ ਵਿੰਡੋਜ਼ ਫਾਇਰਵਾਲ ਦੁਆਰਾ ਸੰਬੰਧਿਤ IP ਨੂੰ ਬਲੌਕ ਕਰਦੀ ਹੈ।

**ਨੋਟ:**
- ਇਹਨਾਂ ਡੋਮੇਨਾਂ ਨੂੰ ਜੋੜਨ ਨਾਲ iTunes ਜਾਂ Skype ਵਰਗੇ ਕੁਝ ਸੌਫਟਵੇਅਰ ਟੁੱਟ ਸਕਦੇ ਹਨ
- Akamai ਨਾਲ ਸਬੰਧਤ ਐਂਟਰੀਆਂ ਨੂੰ Widevine DRM ਨਾਲ ਸਮੱਸਿਆਵਾਂ ਪੈਦਾ ਕਰਨ ਦੀ ਰਿਪੋਰਟ ਕੀਤੀ ਗਈ ਹੈ

### ਵਰਤੀਆਂ ਗਈਆਂ ਸੂਚੀਆਂ:
-[EasyList](https://easylist.to/easylist/easylist.txt) / [JustDomains - EasyList](https://justdomains.github.io/blocklists/lists/easylist-justdomains.txt)
-[Easy Privacy](https://easylist.to/easylist/easyprivacy.txt) / [JustDomains - EasyPrivacy](https://justdomains.github.io/blocklists/lists/easyprivacy-justdomains.txt)
-[NoCoin Filter List](https://github.com/hoshsadiq/adblock-nocoin-list/) / [JustDomains - NoCoin Filter List](https://justdomains.github.io/blocklists/lists/nocoin-justdomains.txt)
-[AdGuard DNS filter](https://github.com/AdguardTeam/AdguardSDNSFilter) / [JustDomains - AdGuard Simplified Domain Names Filter](https://justdomains.github.io/blocklists/lists/adguarddns-justdomains.txt)
-[YoYo Lists](https://pgl.yoyo.org/adservers/serverlist.php)
-[Peter Lowe’s ad/tracking/malware servers](https://pgl.yoyo.org/adservers/policy.php)

### ਉਦਾਹਰਨ:

ਸਕ੍ਰਿਪਟ ਦਾ ਨਵੀਨਤਮ ਸੰਸਕਰਣ ਆਪਣੇ ਆਪ ਚਲਾਓ:
```powershell
iwr -useb 'https://raw.githubusercontent.com/simeononsecurity/System-Wide-Windows-Ad-Blocker/main/sos-system-wide-windows-ad-block.ps1' | iex
```
