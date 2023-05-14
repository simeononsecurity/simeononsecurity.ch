---
title: "GLVK ਸਕ੍ਰਿਪਟ ਨਾਲ ਵਿੰਡੋਜ਼ KMS ਐਕਟੀਵੇਸ਼ਨ ਨੂੰ ਆਟੋਮੈਟਿਕ ਕਰੋ"
date: 2020-12-18
toc: true
draft: false
description: "SimeonOnSecurity ਦੀ GLVK ਆਟੋ ਇੰਸਟੌਲ ਸਕ੍ਰਿਪਟ ਦੀ ਵਰਤੋਂ ਕਰਦੇ ਹੋਏ Windows 10 KMS ਐਕਟੀਵੇਸ਼ਨ ਪ੍ਰਕਿਰਿਆ ਨੂੰ ਸਰਲ ਬਣਾਓ, ਅਤੇ Microsoft ਦੀ ਸਿਫ਼ਾਰਿਸ਼ ਕੀਤੀ ਰੀਡਿੰਗ ਤੋਂ KMS ਅਤੇ GLVK ਕਲਾਇੰਟ ਕੁੰਜੀਆਂ ਬਾਰੇ ਹੋਰ ਜਾਣੋ।"
tags: ["ਵਿੰਡੋਜ਼ ਐਕਟੀਵੇਸ਼ਨ", "KMS ਕਲਾਇੰਟ ਕੁੰਜੀਆਂ", "ਜੀ.ਐਲ.ਵੀ.ਕੇ", "ਵਿੰਡੋਜ਼ ਅੱਪਡੇਟ", "ਪਾਲਣਾ", "ਪਾਵਰਸ਼ੇਲ ਸਕ੍ਰਿਪਟ", "ਕੁੰਜੀ ਪ੍ਰਬੰਧਨ ਸੇਵਾ", "ਵਾਲੀਅਮ ਲਾਇਸੰਸਿੰਗ", "ਐਂਟਰਪ੍ਰਾਈਜ਼ ਐਕਟੀਵੇਸ਼ਨ", "ਕੁੰਜੀ ਪ੍ਰਬੰਧਨ ਸਰਵਰ", "ਆਟੋਮੇਸ਼ਨ", "ਮਾਈਕ੍ਰੋਸਾੱਫਟ ਉਤਪਾਦ", "ਆਪਰੇਟਿੰਗ ਸਿਸਟਮ", "ਸਾਫਟਵੇਅਰ", "ਐਂਟਰਪ੍ਰਾਈਜ਼ ਵਾਤਾਵਰਨ", "ਪ੍ਰਬੰਧਕੀ ਪਾਵਰਸ਼ੇਲ", "GitHub ਰਿਪੋਜ਼ਟਰੀ", "ਸਕ੍ਰਿਪਟਿੰਗ", "ਸਾਈਬਰ ਸੁਰੱਖਿਆ", "SimeonOnSecurity"]
---

KMS ਐਕਟੀਵੇਸ਼ਨ ਲਈ GLVK ਆਟੋ ਇੰਸਟੌਲ ਸਕ੍ਰਿਪਟ

## ਸਿਫਾਰਿਸ਼ ਕੀਤੀ ਰੀਡਿੰਗ:
-[Microsoft - KMS Client Keys (GLVK)](https://docs.microsoft.com/en-us/windows-server/get-started/kmsclientkeys)

## ਸਕ੍ਰਿਪਟ ਨੂੰ ਕਿਵੇਂ ਚਲਾਉਣਾ ਹੈ:
### ਦਸਤੀ ਸਥਾਪਨਾ:
ਜੇਕਰ ਮੈਨੂਅਲੀ ਡਾਉਨਲੋਡ ਕੀਤੀ ਜਾਂਦੀ ਹੈ, ਤਾਂ ਸਕ੍ਰਿਪਟ ਨੂੰ ਡਾਇਰੈਕਟਰੀ ਵਿੱਚ ਇੱਕ ਪ੍ਰਬੰਧਕੀ ਪਾਵਰਸ਼ੇਲ ਤੋਂ ਲਾਂਚ ਕੀਤਾ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ ਜਿਸ ਵਿੱਚ ਸਾਰੀਆਂ ਫਾਈਲਾਂ ਸ਼ਾਮਲ ਹਨ।[GitHub Repository](https://github.com/simeononsecurity/KMS-Auto-PS/archive/main.zip)
```ps
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
Get-ChildItem -Recurse *.ps1 | Unblock-File
.\sos-kmsglvkactivationauto.ps1
```
