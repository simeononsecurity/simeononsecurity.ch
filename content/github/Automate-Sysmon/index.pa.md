---
title: "ਆਟੋਮੇਟ-ਸਿਸਮੋਨ: ਸਿਸਮੋਨ ਡਿਪਲਾਇਮੈਂਟ ਅਤੇ ਕੌਂਫਿਗਰੇਸ਼ਨ ਨੂੰ ਸਰਲ ਬਣਾਓ"
date: 2021-05-11
toc: true
draft: false
description: "ਆਟੋਮੇਟ-ਸਿਸਮੋਨ ਸਕ੍ਰਿਪਟ ਦੇ ਨਾਲ ਤੁਹਾਡੇ ਸਿਸਟਮ ਦੀ ਸੁਰੱਖਿਆ ਨੂੰ ਬਿਹਤਰ ਬਣਾਉਣ ਲਈ ਸਿਸਮੋਨ ਨੂੰ ਕਿਵੇਂ ਤੈਨਾਤ ਅਤੇ ਸੰਰਚਿਤ ਕਰਨਾ ਹੈ, ਬਾਰੇ ਜਾਣੋ, ਜੋ ਕਿ ਨਵੇਂ ਉਪਭੋਗਤਾਵਾਂ ਲਈ ਵੀ ਪ੍ਰਕਿਰਿਆ ਨੂੰ ਸਰਲ ਬਣਾਉਂਦਾ ਹੈ।"
tags: ["ਸਿਸਮੋਨ ਨੂੰ ਆਟੋਮੈਟਿਕ ਕਰੋ", "ਸਿਸਮੋਨ ਨੂੰ ਆਟੋਮੈਟਿਕ ਕਿਵੇਂ ਕਰੀਏ", "ਸਿਸਮੋਨ ਕੌਂਫਿਗਰੇਸ਼ਨ ਨੂੰ ਆਟੋਮੈਟਿਕ ਕਿਵੇਂ ਕਰੀਏ", "ਸਿਸਮੋਨ ਨੂੰ ਕਿਵੇਂ ਇੰਸਟਾਲ ਕਰਨਾ ਹੈ", "ਪਾਵਰਸ਼ੇਲ", "ਸਕ੍ਰਿਪਟ", "ਸਿਸਮੋਨ ਤੈਨਾਤੀ", "ਸਿਸਮੋਨ ਸੰਰਚਨਾ", "ਸਿਸਮੋਨ ਲੌਗਿੰਗ", "ਧਮਕੀ ਦਾ ਪਤਾ ਲਗਾਉਣਾ", "ਖ਼ਰਾਬ ਗਤੀਵਿਧੀ", "SwiftOnSecurity sysmon-config", "ਮਾਈਕਰੋਸਾਫਟ ਸਿਸਟਰਨਲ", "GitHub ਰਿਪੋਜ਼ਟਰੀ", "ਬੀ.ਐਚ.ਆਈ.ਐਸ", "ਸਿਸਟਮ ਨਿਗਰਾਨੀ", "ਸੁਰੱਖਿਆ ਖੋਜ", "ਪ੍ਰਕਿਰਿਆ ਰਚਨਾ", "ਨੈੱਟਵਰਕ ਕਨੈਕਸ਼ਨ"]
---

ਆਟੋਮੇਟ-ਸਿਸਮੋਨ ਇੱਕ ਉਪਯੋਗੀ ਸਕ੍ਰਿਪਟ ਹੈ ਜੋ ਕਿ ਸਿਸਮੋਨ ਦੀ ਤੈਨਾਤੀ ਅਤੇ ਸੰਰਚਨਾ ਨੂੰ ਸਰਲ ਬਣਾਉਂਦੀ ਹੈ, ਮਾਈਕ੍ਰੋਸਾੱਫਟ ਸਿਸਿਨਟਰਨਲਜ਼ ਤੋਂ ਇੱਕ ਸ਼ਕਤੀਸ਼ਾਲੀ ਸਿਸਟਮ ਨਿਗਰਾਨੀ ਸੰਦ ਹੈ। ਸਿਸਮੋਨ ਦੀ ਇੰਸਟਾਲੇਸ਼ਨ ਅਤੇ ਸੈਟਅਪ ਨੂੰ ਆਟੋਮੈਟਿਕ ਕਰਕੇ, ਇਹ ਸਕ੍ਰਿਪਟ ਤੁਹਾਡੇ ਸਿਸਟਮ ਦੀ ਲਾਗਿੰਗ ਯੋਗਤਾਵਾਂ ਨੂੰ ਵਧਾਉਂਦੀ ਹੈ ਅਤੇ ਧਮਕੀ ਖੋਜ ਸਮਰੱਥਾਵਾਂ ਨੂੰ ਵਧਾਉਂਦੀ ਹੈ।

## ਸਿਸਮੋਨ ਕੀ ਹੈ?

ਸਿਸਮੋਨ ਇੱਕ ਸਿਸਟਮ ਨਿਗਰਾਨੀ ਟੂਲ ਹੈ ਜਿਸਦੀ ਵਰਤੋਂ ਸਿਸਟਮ ਉੱਤੇ ਖਤਰਨਾਕ ਗਤੀਵਿਧੀ ਦਾ ਪਤਾ ਲਗਾਉਣ ਲਈ ਕੀਤੀ ਜਾ ਸਕਦੀ ਹੈ। ਇਹ ਪ੍ਰਕਿਰਿਆ ਬਣਾਉਣ, ਨੈਟਵਰਕ ਕਨੈਕਸ਼ਨਾਂ, ਅਤੇ ਹੋਰ ਸਿਸਟਮ ਇਵੈਂਟਾਂ ਬਾਰੇ ਵਿਸਤ੍ਰਿਤ ਜਾਣਕਾਰੀ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ, ਇਸ ਨੂੰ ਸੁਰੱਖਿਆ ਪੇਸ਼ੇਵਰਾਂ ਲਈ ਇੱਕ ਅਨਮੋਲ ਸਾਧਨ ਬਣਾਉਂਦਾ ਹੈ। ਜਦੋਂ ਕਿ ਸਿਸਮੋਨ ਇੱਕ ਸ਼ਕਤੀਸ਼ਾਲੀ ਟੂਲ ਹੈ, ਇਹ ਸੈੱਟਅੱਪ ਅਤੇ ਕੌਂਫਿਗਰ ਕਰਨਾ ਚੁਣੌਤੀਪੂਰਨ ਹੋ ਸਕਦਾ ਹੈ।

## ਆਟੋਮੇਟ-ਸਿਸਮੋਨ ਕਿਵੇਂ ਮਦਦ ਕਰ ਸਕਦਾ ਹੈ?

ਆਟੋਮੇਟ-ਸਿਸਮੋਨ ਸਕ੍ਰਿਪਟ ਸਿਸਮੋਨ ਨੂੰ ਇੰਸਟੌਲ ਅਤੇ ਕੌਂਫਿਗਰ ਕਰਨਾ ਆਸਾਨ ਬਣਾਉਂਦੀ ਹੈ, ਇੱਥੋਂ ਤੱਕ ਕਿ ਉਹਨਾਂ ਲਈ ਵੀ ਜਿਨ੍ਹਾਂ ਕੋਲ ਜ਼ਿਆਦਾ ਤਜਰਬਾ ਨਹੀਂ ਹੈ। ਸਕ੍ਰਿਪਟ ਪ੍ਰਸਿੱਧ **SwiftOnSecurity/sysmon-config** ਮੋਡੀਊਲ ਦੀ ਵਰਤੋਂ ਕਰਦੀ ਹੈ, ਜੋ Sysmon ਲਈ ਪਹਿਲਾਂ ਤੋਂ ਸੰਰਚਿਤ ਨਿਯਮਾਂ ਦਾ ਸੈੱਟ ਪ੍ਰਦਾਨ ਕਰਦੀ ਹੈ। ਇਹ ਸੰਰਚਨਾ ਸਾਲਾਂ ਦੀ ਸੁਰੱਖਿਆ ਖੋਜ 'ਤੇ ਅਧਾਰਤ ਹੈ ਅਤੇ ਕਮਿਊਨਿਟੀ ਦੁਆਰਾ ਨਿਯਮਿਤ ਤੌਰ 'ਤੇ ਅੱਪਡੇਟ ਕੀਤੀ ਜਾਂਦੀ ਹੈ।

ਆਟੋਮੇਟ-ਸਿਸਮੋਨ ਦੇ ਨਾਲ, ਤੁਸੀਂ ਜਾਂ ਤਾਂ ਇੱਕ ਕਮਾਂਡ ਨਾਲ ਪੂਰੀ ਪ੍ਰਕਿਰਿਆ ਨੂੰ ਆਟੋਮੈਟਿਕ ਕਰ ਸਕਦੇ ਹੋ ਜਾਂ ਪ੍ਰਦਾਨ ਕੀਤੀਆਂ ਹਦਾਇਤਾਂ ਦੀ ਪਾਲਣਾ ਕਰਕੇ ਹੱਥੀਂ ਸਿਸਮੋਨ ਨੂੰ ਸਥਾਪਿਤ ਕਰ ਸਕਦੇ ਹੋ। ਇਹ ਲਚਕਤਾ ਉਪਭੋਗਤਾਵਾਂ ਲਈ ਉਹਨਾਂ ਦੀਆਂ ਖਾਸ ਲੋੜਾਂ ਨੂੰ ਪੂਰਾ ਕਰਨ ਲਈ ਇੰਸਟਾਲੇਸ਼ਨ ਅਤੇ ਸੰਰਚਨਾ ਨੂੰ ਅਨੁਕੂਲਿਤ ਕਰਨਾ ਆਸਾਨ ਬਣਾਉਂਦੀ ਹੈ।

## ਆਟੋਮੇਟ-ਸਿਸਮੋਨ ਦੀ ਵਰਤੋਂ ਕਿਵੇਂ ਕਰੀਏ?

ਆਟੋਮੇਟ-ਸਿਸਮੋਨ ਦੀ ਵਰਤੋਂ ਕਰਨ ਦੇ ਦੋ ਤਰੀਕੇ ਹਨ:

### ਸਵੈਚਲਿਤ ਸਥਾਪਨਾ:

ਆਟੋਮੈਟਿਕ ਇੰਸਟਾਲੇਸ਼ਨ ਦੀ ਵਰਤੋਂ ਕਰਨ ਲਈ, PowerShell ਵਿੱਚ ਸਿਰਫ਼ ਹੇਠ ਦਿੱਤੀ ਕਮਾਂਡ ਚਲਾਓ:
```powershell
iwr -useb 'https://simeononsecurity.com/scripts/sosautomatesysmon.ps1'|iex
```

This will automatically download and run the Automate-Sysmon script.

### Manual Install:

If you prefer to install Sysmon manually, follow these steps:

1. Download the script and other required files from the [GitHub repository](https://github.com/simeononsecurity/Automate-Sysmon).
2. Launch PowerShell with administrator privileges.
3. Navigate to the directory containing the downloaded files.
4. Run the following command to change the PowerShell execution policy: ```Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force```
5. Unblock all the script files by running the following command: ```Get-ChildItem -Recurse *.ps1 | Unblock-File```
6. Run the following command to launch the Automate-Sysmon script: ```.\sos-automate-sysmon.ps1```


## ਸਿੱਟਾ

ਸਿੱਟੇ ਵਜੋਂ, ਆਟੋਮੇਟ-ਸਿਸਮੋਨ ਸੁਰੱਖਿਆ ਪੇਸ਼ੇਵਰਾਂ ਲਈ ਇੱਕ ਜ਼ਰੂਰੀ ਸਾਧਨ ਹੈ ਜੋ ਆਪਣੀਆਂ ਲੌਗਿੰਗ ਯੋਗਤਾਵਾਂ ਨੂੰ ਵਧਾਉਣਾ ਚਾਹੁੰਦੇ ਹਨ ਅਤੇ ਆਪਣੇ ਸਿਸਟਮ ਦੀ ਧਮਕੀ ਖੋਜ ਸਮਰੱਥਾਵਾਂ ਨੂੰ ਵਧਾਉਣਾ ਚਾਹੁੰਦੇ ਹਨ। ਸਿਸਮੋਨ ਦੀ ਤੈਨਾਤੀ ਅਤੇ ਸੰਰਚਨਾ ਨੂੰ ਸਵੈਚਲਿਤ ਕਰਨ ਦੀ ਯੋਗਤਾ ਦੇ ਨਾਲ, ਇਹ ਟੂਲ ਸਿਸਮੋਨ ਦਾ ਵੱਧ ਤੋਂ ਵੱਧ ਲਾਭ ਲੈਣ ਲਈ ਨਵੇਂ ਉਪਭੋਗਤਾਵਾਂ ਦੀ ਵੀ ਮਦਦ ਕਰ ਸਕਦਾ ਹੈ। **simeononsecurity/Automate-Sysmon** ਮੋਡੀਊਲ ਦੀ ਵਰਤੋਂ ਕਰਕੇ, ਉਪਭੋਗਤਾ ਭਾਈਚਾਰੇ ਦੀ ਮੁਹਾਰਤ ਤੋਂ ਲਾਭ ਉਠਾ ਸਕਦੇ ਹਨ ਅਤੇ ਨਵੀਨਤਮ ਸੁਰੱਖਿਆ ਖੋਜਾਂ ਨਾਲ ਅੱਪ ਟੂ ਡੇਟ ਰਹਿ ਸਕਦੇ ਹਨ। ਇਸ ਲਈ, ਜੇਕਰ ਤੁਸੀਂ ਆਪਣੇ ਸਿਸਟਮ ਦੀ ਸੁਰੱਖਿਆ ਨੂੰ ਬਿਹਤਰ ਬਣਾਉਣਾ ਚਾਹੁੰਦੇ ਹੋ, ਤਾਂ Automate-Sysmon ਨੂੰ ਅਜ਼ਮਾਓ!



