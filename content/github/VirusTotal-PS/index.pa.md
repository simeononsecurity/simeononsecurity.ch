---
title: "VirusTotal PowerShell ਮੋਡੀਊਲ ਨਾਲ ਕੁਸ਼ਲ ਵਾਇਰਸ ਸਕੈਨ"
date: 2020-11-24
toc: true
draft: false
description: "VirusTotal API ਨਾਲ ਆਪਸੀ ਤਾਲਮੇਲ ਨੂੰ ਸਵੈਚਲਿਤ ਕਰਕੇ ਅਤੇ ਆਪਣੇ ਸੁਰੱਖਿਆ ਵਰਕਫਲੋ ਨੂੰ ਸੁਚਾਰੂ ਬਣਾ ਕੇ VirusTotal PowerShell ਮੋਡੀਊਲ ਨਾਲ ਕੁਸ਼ਲ ਵਾਇਰਸ ਸਕੈਨ ਕਰੋ।"
tags: ["PowerShell ਮੋਡੀਊਲ", "ਪਾਵਰਸ਼ੇਲ", "ਆਟੋਮੇਸ਼ਨ", "ਵਾਇਰਸ ਕੁੱਲ", "ਵਾਇਰਸ ਸਕੈਨ", "ਡੋਮੇਨ ਸਕੈਨ", "API ਕੁੰਜੀ", "VirusTotal API", "ਵਾਇਰਸ ਟੋਟਲ ਡਿਵੈਲਪਰ ਪੰਨਾ", "ਸਿਸਟਮ ਪ੍ਰਸ਼ਾਸਨ", "ਸੁਰੱਖਿਆ ਵਰਕਫਲੋ", "ਕੁਸ਼ਲ ਵਾਇਰਸ ਸਕੈਨ", "ਡਾਊਨਲੋਡ ਕਰੋ ਅਤੇ ਸਥਾਪਿਤ ਕਰੋ", "GitHub ਰਿਪੋਜ਼ਟਰੀ", "API ਵਰਤੋਂ ਦੀਆਂ ਉਦਾਹਰਨਾਂ"]
---
 VirusTotal API ਨਾਲ ਇੰਟਰੈਕਟ ਕਰਨ ਲਈ PowerShell ਮੋਡੀਊਲ ਦਾ ਸੰਗ੍ਰਹਿ

**ਨੋਟ:**
- ਤੁਹਾਨੂੰ ਆਪਣੀ VirusTotal API ਕੁੰਜੀ ਦੀ ਲੋੜ ਪਵੇਗੀ, ਜੋ ਤੁਹਾਡੇ 'ਤੇ ਲੱਭੀ ਜਾ ਸਕਦੀ ਹੈ[Shodan Account](https://www.virustotal.com/gui/)
- ਮੋਡਿਊਲਾਂ ਵਿੱਚ ਵਰਤੇ ਗਏ APIs ਦੀਆਂ ਉਦਾਹਰਨਾਂ 'ਤੇ ਮਿਲ ਸਕਦੀਆਂ ਹਨ[VirusTotal Developers Page](https://developers.virustotal.com/reference#getting-started)

## ਡਾਉਨਲੋਡ ਅਤੇ ਸਥਾਪਿਤ ਕਰੋ
- ਤੋਂ ਮੋਡੀਊਲ ਡਾਊਨਲੋਡ ਕਰੋ[GitHub Repository](https://github.com/simeononsecurity/VirusTotal-PS)
- ਸਾਰੇ ਮੋਡੀਊਲ ਸਥਾਪਿਤ ਕਰੋ
```ps
Get-ChildItem -Recurse *.ps1 | Import-Module
```