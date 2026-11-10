---
title: "Standalone-Windows-STIG-Script: ਮਿਆਰਾਂ ਦੇ ਅਨੁਕੂਲ PC ਬਣਾਓ"
date: 2023-02-02
lastmod: 2026-11-09
toc: true
draft: false
description: "ਪੈਰਾਮੀਟਰਾਂ ਅਤੇ ਤਸਦੀਕ ਸਮੇਤ, ਮਿਆਰਾਂ ਦੇ ਅਨੁਕੂਲ Windows ਸਿਸਟਮ ਬਣਾਉਣ ਲਈ Standalone-Windows-STIG-Script ਦੀ ਕਦਮ-ਦਰ-ਕਦਮ ਜਾਣਕਾਰੀ।"
tags: ["STIG ਸਕ੍ਰਿਪਟ", "Windows ਸੁਰੱਖਿਆ", "ਮਿਆਰਾਂ ਦੇ ਅਨੁਕੂਲ Windows ਸਿਸਟਮ", "ਸਿਸਟਮ ਸਖ਼ਤੀਕਰਨ", "Windows STIG", "ਸੁਰੱਖਿਅਤ Windows", "Windows ਅਨੁਕੂਲਤਾ", "ਹੱਥੀਂ ਸਥਾਪਨਾ", "Windows ਅੱਪਡੇਟ", "Adobe Reader", "Firefox", "Chrome", "Internet Explorer 11", ".NET Framework", "Office", "OneDrive", "Java", "Windows Defender", "Windows Firewall", "ਖ਼ਤਰਾ ਘਟਾਉਣ ਦੇ ਉਪਾਅ", "Nessus PID", "VMware Horizon", "ਵਿਕਲਪਿਕ ਸਖ਼ਤੀਕਰਨ"]
cover: "/img/cover/create-compliant-windows-desktop-systems-with-standalone-windows-stig-script.webp"
coverAlt: "ਗੂੜ੍ਹੇ ਨੀਲੇ ਪਿਛੋਕੜ ਉੱਤੇ ਚਮਕਦਾਰ ਰੰਗਾਂ ਵਾਲੀਆਂ ਤਰੱਕੀ ਪੱਟੀਆਂ ਅਤੇ ਡਾਟਾ-ਧਾਰਾਵਾਂ ਸਮੇਤ ਸੁਰੱਖਿਆ ਅਨੁਕੂਲਤਾ ਇੰਟਰਫੇਸ ਦਿਖਾਉਂਦੀ ਕੰਪਿਊਟਰ ਸਕ੍ਰੀਨ ਦੀ ਤਸਵੀਰ।"
coverCaption: ""
---

Windows ਸਿਸਟਮ ਕਾਰੋਬਾਰਾਂ, ਸੰਸਥਾਵਾਂ ਅਤੇ ਘਰਾਂ ਵਿੱਚ ਵਿਆਪਕ ਤੌਰ 'ਤੇ ਵਰਤੇ ਜਾਂਦੇ ਹਨ। ਸਾਈਬਰ ਹਮਲਿਆਂ ਦੀ ਵਧਦੀ ਗਿਣਤੀ ਦੇ ਮੱਦੇਨਜ਼ਰ ਇਹ ਯਕੀਨੀ ਬਣਾਉਣਾ ਲਾਜ਼ਮੀ ਹੈ ਕਿ ਇਹ ਸਿਸਟਮ ਸੁਰੱਖਿਅਤ ਹੋਣ ਅਤੇ ਉਦਯੋਗਕ ਮਿਆਰਾਂ ਦੀ ਪਾਲਣਾ ਕਰਨ। Standalone-Windows-STIG-Script ਇਸ ਕੰਮ ਵਿੱਚ ਮਦਦ ਕਰਦਾ ਹੈ। ਇਹ ਲੇਖ ਦੱਸਦਾ ਹੈ ਕਿ ਸਕ੍ਰਿਪਟ ਕੀ ਹੈ, ਕਿਵੇਂ ਕੰਮ ਕਰਦੀ ਹੈ ਅਤੇ ਸੁਰੱਖਿਅਤ, ਮਿਆਰਾਂ ਦੇ ਅਨੁਕੂਲ Windows ਸਿਸਟਮ ਬਣਾਉਣ ਲਈ ਇਸਨੂੰ ਕਿਵੇਂ ਵਰਤਣਾ ਹੈ।

## Standalone-Windows-STIG-Script ਕੀ ਹੈ?

**Standalone-Windows-STIG-Script** Simeononsecurity ਵੱਲੋਂ ਬਣਾਈ ਗਈ ਸਕ੍ਰਿਪਟ ਹੈ, ਜੋ Security Technical Implementation Guide (STIG) ਅਨੁਸਾਰ Windows ਸਿਸਟਮ ਨੂੰ ਸੁਰੱਖਿਅਤ ਬਣਾਉਣ ਦੀ ਪ੍ਰਕਿਰਿਆ ਸਵੈਚਾਲਿਤ ਕਰਦੀ ਹੈ। ਇਹ ਓਪਨ ਸੋਰਸ ਹੈ ਅਤੇ **GitHub** ਉੱਤੇ ਉਪਲਬਧ ਹੈ।

## ਇਹ ਕਿਵੇਂ ਕੰਮ ਕਰਦੀ ਹੈ?

Standalone-Windows-STIG-Script Windows ਸਿਸਟਮ ਨੂੰ ਸੁਰੱਖਿਅਤ ਕਰਨ ਲਈ STIG ਦੀਆਂ ਹਦਾਇਤਾਂ ਲਾਗੂ ਕਰਦੀ ਹੈ। ਇਸਨੂੰ Windows ਸਿਸਟਮ ਉੱਤੇ ਚਲਾਉਣ ਨਾਲ STIG ਦੀ ਪਾਲਣਾ ਲਈ ਲੋੜੀਂਦੀਆਂ ਤਬਦੀਲੀਆਂ ਹੁੰਦੀਆਂ ਹਨ। ਇਹ ਕਈ ਸੁਰੱਖਿਆ ਉਪਾਅ ਲਾਗੂ ਕਰਦੀ ਹੈ, ਜਿਵੇਂ:

- ਖਾਤਾ ਨੀਤੀਆਂ
- ਆਡਿਟ ਨੀਤੀਆਂ
- ਸੁਰੱਖਿਆ ਵਿਕਲਪ
- ਫਾਇਰਵਾਲ ਸੈਟਿੰਗਾਂ
- ਸੇਵਾ ਸੈਟਿੰਗਾਂ

## Standalone-Windows-STIG-Script ਵਰਤਣ ਦੇ ਫ਼ਾਇਦੇ:

- **ਸਵੈਚਾਲਨ**: ਸਕ੍ਰਿਪਟ Windows ਸਿਸਟਮ ਨੂੰ ਸੁਰੱਖਿਅਤ ਕਰਨ ਦੀ ਪ੍ਰਕਿਰਿਆ ਸਵੈਚਾਲਿਤ ਕਰਦੀ ਹੈ, ਜਿਸ ਨਾਲ ਸਮਾਂ ਬਚਦਾ ਹੈ ਅਤੇ ਮਨੁੱਖੀ ਗਲਤੀ ਦੀ ਸੰਭਾਵਨਾ ਘਟਦੀ ਹੈ।

- **ਅਨੁਕੂਲਤਾ**: ਸਕ੍ਰਿਪਟ STIG ਦੀਆਂ ਹਦਾਇਤਾਂ ਲਾਗੂ ਕਰਦੀ ਹੈ ਅਤੇ Windows ਸਿਸਟਮ ਨੂੰ ਉਦਯੋਗਕ ਮਿਆਰਾਂ ਦੇ ਅਨੁਕੂਲ ਬਣਾਉਣ ਵਿੱਚ ਮਦਦ ਕਰਦੀ ਹੈ।

- **ਮਨ ਦੀ ਤਸੱਲੀ**: Standalone-Windows-STIG-Script ਦੀ ਵਰਤੋਂ ਨਾਲ ਤੁਸੀਂ ਯਕੀਨ ਕਰ ਸਕਦੇ ਹੋ ਕਿ ਤੁਹਾਡਾ Windows ਸਿਸਟਮ ਸੁਰੱਖਿਅਤ ਹੈ ਅਤੇ ਉਦਯੋਗਕ ਮਿਆਰਾਂ ਦੀ ਪਾਲਣਾ ਕਰਦਾ ਹੈ।

_________________________________________________________________________________________________________________________

## Standalone-Windows-STIG-Script ਕਿਵੇਂ ਵਰਤਣਾ ਹੈ:

1. Standalone-Windows-STIG-Script ਵਰਤਣਾ ਕਾਫ਼ੀ ਸੌਖਾ ਹੈ। ਇਸਨੂੰ ਵਰਤਣ ਦੇ ਕਦਮ ਹੇਠਾਂ ਦਿੱਤੇ ਹਨ:

2. **ਸਕ੍ਰਿਪਟ ਡਾਊਨਲੋਡ ਕਰੋ**: ਸਕ੍ਰਿਪਟ GitHub ਉੱਤੇ https://github.com/simeononsecurity/Standalone-Windows-STIG-Script ਤੋਂ ਮਿਲਦੀ ਹੈ। ਇਸਨੂੰ ਡਾਊਨਲੋਡ ਕਰਕੇ ਆਪਣੇ Windows ਸਿਸਟਮ ਉੱਤੇ ਸੰਭਾਲੋ।

3. **ਉੱਚੇ ਅਧਿਕਾਰਾਂ ਵਾਲਾ ਕਮਾਂਡ ਪ੍ਰੋਂਪਟ ਖੋਲ੍ਹੋ**: Windows Start ਬਟਨ ਉੱਤੇ ਸੱਜਾ-ਕਲਿੱਕ ਕਰੋ ਅਤੇ "Windows PowerShell (Admin)" ਚੁਣੋ।

4. **ਸਕ੍ਰਿਪਟ ਚਲਾਓ**: ਜਿੱਥੇ ਸਕ੍ਰਿਪਟ ਸੰਭਾਲੀ ਹੈ ਉਸ ਥਾਂ ਜਾਓ ਅਤੇ ਹੇਠਾਂ ਦਿੱਤੀ ਕਮਾਂਡ ਦਰਜ ਕਰਕੇ ਚਲਾਓ:

```powershell
powershell.exe -ExecutionPolicy Bypass -File Standalone-Windows-STIG-Script.ps1
```

5. ਤਬਦੀਲੀਆਂ ਦੀ ਜਾਂਚ ਕਰੋ: ਸਕ੍ਰਿਪਟ ਮੁਕੰਮਲ ਹੋਣ ਤੋਂ ਬਾਅਦ ਸਿਸਟਮ ਵਿੱਚ ਕੀਤੀਆਂ ਤਬਦੀਲੀਆਂ ਵੇਖੋ ਅਤੇ ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਹਰ ਚੀਜ਼ ਠੀਕ ਤਰ੍ਹਾਂ ਸੰਰਚਿਤ ਹੈ।

## ਨਤੀਜਾ:

Standalone-Windows-STIG-Script ਤੁਹਾਡੇ Windows ਸਿਸਟਮ ਨੂੰ ਸੁਰੱਖਿਅਤ ਕਰਨ ਅਤੇ ਉਦਯੋਗਕ ਮਿਆਰਾਂ ਦੀ ਪਾਲਣਾ ਵਿੱਚ ਮਦਦਗਾਰ ਸਾਧਨ ਹੈ। ਇਹ ਸੁਰੱਖਿਆ ਦੀ ਪ੍ਰਕਿਰਿਆ ਸਵੈਚਾਲਿਤ ਕਰਦਾ ਹੈ ਅਤੇ STIG ਦੀਆਂ ਹਦਾਇਤਾਂ ਲਾਗੂ ਕਰਦਾ ਹੈ। ਜੇ ਤੁਸੀਂ ਸੁਰੱਖਿਅਤ ਅਤੇ ਮਿਆਰਾਂ ਦੇ ਅਨੁਕੂਲ Windows ਸਿਸਟਮ ਬਣਾਉਣਾ ਚਾਹੁੰਦੇ ਹੋ, ਤਾਂ Standalone-Windows-STIG-Script ਵਰਤਣ ਬਾਰੇ ਸੋਚੋ।
