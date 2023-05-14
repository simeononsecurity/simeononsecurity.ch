---
title: "PowerShell ਸਕ੍ਰਿਪਟਾਂ ਦੇ ਨਾਲ ਫਾਇਰਫਾਕਸ STIG ਪਾਲਣਾ ਨੂੰ ਆਟੋਮੈਟਿਕ ਕਰੋ"
date: 2020-08-15
---

ਫਾਇਰਫਾਕਸ STIG ਸਕ੍ਰਿਪਟ

ਦ[Firefox V4R29](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MOZ_FireFox_V4R29_STIG.zip) STIGs ਨੂੰ ਲਾਗੂ ਕਰਨਾ ਸਭ ਤੋਂ ਆਸਾਨ ਨਹੀਂ ਹੈ।
ਇਹ ਸਕ੍ਰਿਪਟ ਜ਼ਿਆਦਾਤਰ ਲੋੜੀਂਦੀਆਂ ਫਾਇਰਫਾਕਸ ਨੀਤੀਆਂ ਨੂੰ ਲਾਗੂ ਕਰੇਗੀ। ਭਵਿੱਖ ਵਿੱਚ, ਫਾਇਰਫਾਕਸ ADMX ਟੈਂਪਲੇਟਸ ਅਤੇ ਜੀਪੀਓਜ਼ ਇਸ ਸਕ੍ਰਿਪਟ ਵਿੱਚ ਲਾਗੂ ਕੀਤੇ ਜਾਣਗੇ।

**ਕੰਮ ਚੱਲ ਰਿਹਾ ਹੈ**

## ਲੋੜੀਂਦੀਆਂ ਫਾਈਲਾਂ ਨੂੰ ਡਾਉਨਲੋਡ ਕਰੋ

ਤੋਂ ਲੋੜੀਂਦੀਆਂ ਫਾਈਲਾਂ ਡਾਊਨਲੋਡ ਕਰੋ[GitHub Repository](https://github.com/simeononsecurity/FireFox-STIG-Script)

## ਸਕ੍ਰਿਪਟ ਨੂੰ ਕਿਵੇਂ ਚਲਾਉਣਾ ਹੈ


**ਸਕ੍ਰਿਪਟ ਨੂੰ ਇਸ ਤਰ੍ਹਾਂ ਐਕਸਟਰੈਕਟ ਕੀਤੇ GitHub ਡਾਊਨਲੋਡ ਤੋਂ ਲਾਂਚ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ:**
```
.\sos-firefoxstig.ps1
```