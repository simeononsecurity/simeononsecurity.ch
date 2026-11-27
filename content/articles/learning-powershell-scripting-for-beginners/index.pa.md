---
title: "PowerShell ਸਕ੍ਰਿਪਟਿੰਗ"
draft: false
toc: true
date: 2023-02-25
lastmod: 2026-11-27
description: "ਕਮਾਂਡਲੇਟ, ਲੂਪ, ਫੰਕਸ਼ਨ ਅਤੇ ਹੋਰ ਵਿਸ਼ਿਆਂ ਵਾਲੀ ਇਸ ਕਦਮ-ਦਰ-ਕਦਮ ਸ਼ੁਰੂਆਤੀ ਗਾਈਡ ਨਾਲ PowerShell ਸਕ੍ਰਿਪਟਿੰਗ ਦੀਆਂ ਬੁਨਿਆਦਾਂ ਸਿੱਖੋ ਅਤੇ ਕੰਮ ਸਵੈਚਾਲਿਤ ਕਰੋ।"
genre: ["ਤਕਨਾਲੋਜੀ", "ਪ੍ਰੋਗਰਾਮਿੰਗ", "ਸਵੈਚਾਲਨ", "Windows", "ਸਕ੍ਰਿਪਟਿੰਗ", "ਆਈਟੀ", "ਪ੍ਰਸ਼ਾਸਕੀ ਕੰਮ", "ਕੰਪਿਊਟਰ ਪ੍ਰਬੰਧਨ", "ਸਾਫਟਵੇਅਰ ਵਿਕਾਸ", "ਕੋਡਿੰਗ"]
tags: ["PowerShell ਸਕ੍ਰਿਪਟਿੰਗ", "PowerShell ਸਵੈਚਾਲਨ", "Windows ਸਕ੍ਰਿਪਟਿੰਗ", "PowerShell ਕਮਾਂਡਲੇਟ", "PowerShell ਮੋਡੀਊਲ", "PowerShell ਲੂਪ", "PowerShell ਸ਼ਰਤੀ ਕਥਨ", "PowerShell ਫੰਕਸ਼ਨ", "PowerShell ਦੇ ਚੰਗੇ ਤਰੀਕੇ", "PowerShell ਡੀਬੱਗਿੰਗ", "PowerShell ਟੈਸਟਿੰਗ", "PowerShell ਵੇਰੀਏਬਲ", "PowerShell ISE", "PowerShell Remoting", "Microsoft ਤਕਨਾਲੋਜੀਆਂ", "ਆਈਟੀ ਸਵੈਚਾਲਨ", "ਕੰਪਿਊਟਰ ਪ੍ਰਬੰਧਨ", "ਸ਼ੁਰੂਆਤੀਆਂ ਲਈ ਕੋਡਿੰਗ", "ਪ੍ਰਸ਼ਾਸਕੀ ਕੰਮ", "PowerShell ਸਕ੍ਰਿਪਟ ਵਿਚਾਰ", "ਆਟੋਮੈਟਿਕ ਬੈਕਅੱਪ", "ਫਾਈਲ ਪ੍ਰਬੰਧਨ", "ਸਿਸਟਮ ਜਾਣਕਾਰੀ", "ਵਰਤੋਂਕਾਰ ਪ੍ਰਬੰਧਨ", "ਸਾਫਟਵੇਅਰ ਇੰਸਟਾਲੇਸ਼ਨ", "ਨੈੱਟਵਰਕ ਸੰਰਚਨਾ", "ਸੁਰੱਖਿਆ ਸਵੈਚਾਲਨ", "ਕੰਮਾਂ ਦੀ ਸਮਾਂ-ਸਾਰਣੀ", "ਰਜਿਸਟਰੀ ਵਿੱਚ ਤਬਦੀਲੀ", "ਦੂਰ-ਵਰਤੀ ਪ੍ਰਸ਼ਾਸਨ"]
cover: "/img/cover/A_cartoon_character_holding_a_script_and_standing.webp"
coverAlt: "PowerShell ਪ੍ਰੌਂਪਟ ਵਾਲੇ ਕੰਪਿਊਟਰ ਅੱਗੇ ਸਕ੍ਰਿਪਟ ਫੜਿਆ ਕਾਰਟੂਨ ਪਾਤਰ, ਜੋ ਸ਼ੁਰੂਆਤੀਆਂ ਲਈ PowerShell ਸਕ੍ਰਿਪਟਿੰਗ ਦੀ ਸੌਖ ਦਰਸਾਉਂਦਾ ਹੈ"
coverCaption: ""
---
**ਸ਼ੁਰੂਆਤੀਆਂ ਲਈ PowerShell ਸਕ੍ਰਿਪਟਿੰਗ**

PowerShell, Microsoft ਵੱਲੋਂ ਬਣਾਇਆ ਕਮਾਂਡ-ਲਾਈਨ ਸ਼ੈੱਲ ਅਤੇ ਸਕ੍ਰਿਪਟਿੰਗ ਭਾਸ਼ਾ ਹੈ। ਇਸ ਵਿੱਚ Windows ਓਪਰੇਟਿੰਗ ਸਿਸਟਮ ਅਤੇ ਹੋਰ Microsoft ਤਕਨਾਲੋਜੀਆਂ ਦੇ ਵੱਖ-ਵੱਖ ਹਿੱਸਿਆਂ ਨੂੰ ਸੰਭਾਲਣ ਅਤੇ ਸਵੈਚਾਲਿਤ ਕਰਨ ਲਈ ਬਹੁਤ ਸਾਰੇ ਕਮਾਂਡ ਅਤੇ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਹਨ। ਇਸ ਲੇਖ ਵਿੱਚ ਅਸੀਂ PowerShell ਸਕ੍ਰਿਪਟਿੰਗ ਦੀਆਂ ਬੁਨਿਆਦਾਂ ਸਮਝਾਵਾਂਗੇ ਅਤੇ ਸ਼ੁਰੂਆਤ ਲਈ ਕਦਮ-ਦਰ-ਕਦਮ ਗਾਈਡ ਦੇਵਾਂਗੇ।

## PowerShell ਨਾਲ ਜਾਣ-ਪਛਾਣ

**PowerShell** ਇੱਕ ਕਮਾਂਡ-ਲਾਈਨ ਸ਼ੈੱਲ ਹੈ, ਜਿਸ ਨਾਲ ਵਰਤੋਂਕਾਰ Windows ਓਪਰੇਟਿੰਗ ਸਿਸਟਮ ਅਤੇ ਹੋਰ Microsoft ਤਕਨਾਲੋਜੀਆਂ ਨੂੰ ਸਵੈਚਾਲਿਤ ਅਤੇ ਸੰਭਾਲ ਸਕਦੇ ਹਨ। ਫਾਈਲਾਂ ਅਤੇ ਡਾਇਰੈਕਟਰੀਆਂ ਦਾ ਪ੍ਰਬੰਧ, ਨੈੱਟਵਰਕ ਸੰਰਚਨਾ ਅਤੇ ਸਿਸਟਮ ਪ੍ਰਬੰਧਨ ਵਰਗੇ ਪ੍ਰਸ਼ਾਸਕੀ ਕੰਮਾਂ ਲਈ ਇਸ ਵਿੱਚ ਕਮਾਂਡਾਂ ਅਤੇ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਦਾ ਵਿਸ਼ਾਲ ਸਮੂਹ ਹੈ। PowerShell ਵਿੱਚ ਸਕ੍ਰਿਪਟਿੰਗ ਭਾਸ਼ਾ ਵੀ ਹੈ, ਜਿਸ ਨਾਲ ਗੁੰਝਲਦਾਰ ਸਕ੍ਰਿਪਟਾਂ ਬਣਾਈਆਂ ਅਤੇ ਵਾਰ-ਵਾਰ ਹੋਣ ਵਾਲੇ ਕੰਮ ਸਵੈਚਾਲਿਤ ਕੀਤੇ ਜਾ ਸਕਦੇ ਹਨ।

## PowerShell ਨਾਲ ਸ਼ੁਰੂਆਤ

### PowerShell ਇੰਸਟਾਲ ਕਰਨਾ

Windows ਦੇ ਬਹੁਤੇ ਸੰਸਕਰਣਾਂ ਵਿੱਚ PowerShell ਪਹਿਲਾਂ ਤੋਂ ਇੰਸਟਾਲ ਹੁੰਦਾ ਹੈ। ਜੇ ਤੁਸੀਂ Windows ਦਾ ਪੁਰਾਣਾ ਸੰਸਕਰਣ ਵਰਤ ਰਹੇ ਹੋ ਜਾਂ PowerShell ਦਾ ਨਵਾਂ ਸੰਸਕਰਣ ਚਾਹੀਦਾ ਹੈ, ਤਾਂ ਇਸਨੂੰ Microsoft ਦੀ ਵੈੱਬਸਾਈਟ ਤੋਂ ਡਾਊਨਲੋਡ ਕਰੋ। PowerShell ਡਾਊਨਲੋਡ ਅਤੇ ਇੰਸਟਾਲ ਕਰਨ ਲਈ ਇਹ ਕਦਮ ਚੁੱਕੋ:

1. [Microsoft PowerShell ਵੈੱਬਸਾਈਟ](https://docs.microsoft.com/en-us/powershell/scripting/install/installing-powershell?view=powershell-7.2) ਖੋਲ੍ਹੋ ਅਤੇ ਇੰਸਟਾਲ ਕਰਨ ਲਈ ਸੰਸਕਰਣ ਚੁਣੋ।
2. ਇੰਸਟਾਲੇਸ਼ਨ ਫਾਈਲ ਡਾਊਨਲੋਡ ਕਰਕੇ ਚਲਾਓ।
3. ਇੰਸਟਾਲੇਸ਼ਨ ਪੂਰੀ ਕਰਨ ਲਈ ਸਕ੍ਰੀਨ ਉੱਤੇ ਦਿੱਤੀਆਂ ਹਦਾਇਤਾਂ ਮੰਨੋ।

### PowerShell ਚਾਲੂ ਕਰਨਾ

PowerShell ਇੰਸਟਾਲ ਕਰਨ ਮਗਰੋਂ ਇਸਨੂੰ ਚਲਾਉਣ ਲਈ ਇਹ ਕਦਮ ਚੁੱਕੋ:

1. Start ਮੀਨੂ ਖੋਲ੍ਹੋ ਅਤੇ ਖੋਜ ਪੱਟੀ ਵਿੱਚ "PowerShell" ਲਿਖੋ।
2. ਖੋਜ ਨਤੀਜਿਆਂ ਵਿੱਚੋਂ "Windows PowerShell" ਚੁਣੋ।
3. PowerShell ਨਵੀਂ ਵਿੰਡੋ ਵਿੱਚ ਖੁੱਲ੍ਹੇਗਾ।

### Visual Studio Code ਵਿੱਚ PowerShell ਸਕ੍ਰਿਪਟਿੰਗ

ਸਕ੍ਰਿਪਟ ਲਿਖਣ ਦਾ ਬਿਹਤਰ ਤਜਰਬਾ ਲੈਣ ਲਈ ਤੁਸੀਂ ਪ੍ਰਸਿੱਧ ਇਕੱਠੇ ਵਿਕਾਸ ਵਾਤਾਵਰਣ (IDE) Visual Studio Code (VS Code) ਵਰਤ ਸਕਦੇ ਹੋ। VS Code ਵਿੱਚ ਸਿੰਟੈਕਸ ਹਾਈਲਾਈਟਿੰਗ, ਕੋਡ ਪੂਰਾ ਕਰਨ ਦੇ ਸੁਝਾਅ, ਡੀਬੱਗਿੰਗ ਅਤੇ ਇਕੱਠਾ ਟਰਮੀਨਲ ਹੈ, ਇਸ ਲਈ ਇਹ PowerShell ਸਕ੍ਰਿਪਟਿੰਗ ਲਈ ਚੰਗਾ ਵਿਕਲਪ ਹੈ। VS Code ਵਿੱਚ ਸ਼ੁਰੂ ਕਰਨ ਲਈ:

1. [ਅਧਿਕਾਰਤ ਵੈੱਬਸਾਈਟ](https://code.visualstudio.com/) ਤੋਂ Visual Studio Code ਇੰਸਟਾਲ ਕਰੋ।
2. VS Code ਦੇ Extensions ਬਾਜ਼ਾਰ ਤੋਂ Microsoft ਦਾ "PowerShell" ਐਕਸਟੈਂਸ਼ਨ ਇੰਸਟਾਲ ਕਰੋ।
3. VS Code ਵਿੱਚ PowerShell ਸਕ੍ਰਿਪਟ ਫਾਈਲ (.ps1) ਖੋਲ੍ਹੋ ਅਤੇ ਲਿਖਣਾ ਸ਼ੁਰੂ ਕਰੋ।

### ਸਿਸਟਮ ਪ੍ਰਸ਼ਾਸਨ ਲਈ PowerShell

PowerShell ਸਿਸਟਮ ਪ੍ਰਸ਼ਾਸਨ ਦੇ ਕੰਮਾਂ ਲਈ ਬਹੁਮੁਖੀ ਸਾਧਨ ਹੈ। ਇੱਕ-ਲਾਈਨ ਕਮਾਂਡਾਂ ਤੋਂ ਲੈ ਕੇ ਗੁੰਝਲਦਾਰ ਸਵੈਚਾਲਨ ਕਾਰਜ-ਪ੍ਰਵਾਹਾਂ ਤੱਕ, ਇਹ ਉਹ ਕੰਮ ਆਸਾਨ ਕਰਦਾ ਹੈ ਜਿਨ੍ਹਾਂ ਲਈ ਨਹੀਂ ਤਾਂ ਹੱਥੀਂ ਦਖ਼ਲ ਦੀ ਲੋੜ ਹੁੰਦੀ। ਇਹ Windows, Linux ਅਤੇ macOS ਲਈ ਇਕਸਾਰ ਸਕ੍ਰਿਪਟਿੰਗ ਮੰਚ ਦਿੰਦਾ ਹੈ, ਤਾਂ ਜੋ ਪ੍ਰਸ਼ਾਸਕ ਵੱਖ-ਵੱਖ ਵਾਤਾਵਰਣਾਂ ਲਈ ਇੱਕੋ ਜਿਹੇ ਸਾਧਨ ਵਰਤ ਸਕਣ।

### Command Prompt ਤੋਂ Windows PowerShell ਵੱਲ ਜਾਣਾ

ਜੇ ਤੁਸੀਂ Command Prompt ਨਾਲ ਜਾਣੂ ਹੋ ਅਤੇ Windows PowerShell ਵੱਲ ਜਾਣਾ ਚਾਹੁੰਦੇ ਹੋ, ਤਾਂ ਸਿੱਖਣ ਦਾ ਰਾਹ ਸੌਖਾ ਹੋ ਸਕਦਾ ਹੈ। Windows PowerShell ਸਕ੍ਰਿਪਟਿੰਗ Command Prompt ਦੀਆਂ ਧਾਰਣਾਵਾਂ ਉੱਤੇ ਬਣੀ ਹੈ ਅਤੇ ਹੋਰ ਉੱਨਤ ਸਮਰੱਥਾਵਾਂ ਦਿੰਦੀ ਹੈ। ਆਪਣੇ ਮੌਜੂਦਾ ਗਿਆਨ ਦੀ ਵਰਤੋਂ ਕਰਕੇ PowerShell ਦੀਆਂ ਵਾਧੂ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਅਤੇ ਕਮਾਂਡਲੇਟ ਹੌਲੀ-ਹੌਲੀ ਸਿੱਖੋ।

### PowerShell ਦੀਆਂ ਬੁਨਿਆਦਾਂ

PowerShell ਓਪਰੇਟਿੰਗ ਸਿਸਟਮ ਨਾਲ ਕੰਮ ਕਰਨ ਲਈ ਕਮਾਂਡ-ਲਾਈਨ ਇੰਟਰਫੇਸ ਦਿੰਦਾ ਹੈ। ਇਸ ਦੀਆਂ ਕਮਾਂਡਾਂ ਨੂੰ ਕਮਾਂਡਲੇਟ ਕਿਹਾ ਜਾਂਦਾ ਹੈ ਅਤੇ ਉਹ ਮੋਡੀਊਲਾਂ ਵਿੱਚ ਸਜਾਈਆਂ ਹੁੰਦੀਆਂ ਹਨ। ਉਪਲਬਧ ਮੋਡੀਊਲਾਂ ਦੀ ਸੂਚੀ ਦੇਖਣ ਲਈ Get-Module ਕਮਾਂਡ ਵਰਤੋ:

```powershell
Get-Module
```

ਕਿਸੇ ਮੋਡੀਊਲ ਵਿੱਚ ਉਪਲਬਧ ਕਮਾਂਡਲੇਟ ਦੇਖਣ ਲਈ Get-Command ਵਰਤੋ:
```powershell
Get-Command -Module <module name>
```

ਕਿਸੇ ਕਮਾਂਡਲੇਟ ਬਾਰੇ ਮਦਦ ਲੈਣ ਲਈ Get-Help ਵਰਤੋ:
```powershell
Get-Help <ਕਮਾਂਡਲੇਟ name>
```

PowerShell alias ਵੀ ਦਿੰਦਾ ਹੈ, ਜੋ ਕਮਾਂਡਲੇਟ ਦੇ ਛੋਟੇ ਨਾਂ ਹੁੰਦੇ ਹਨ। ਉਪਲਬਧ alias ਦੇਖਣ ਲਈ Get-Alias ਵਰਤੋ:
```powershell
Get-Alias
```

## ਸਕ੍ਰਿਪਟ ਫਾਈਲਾਂ ਅਤੇ ਚਲਾਉਣ ਦੀ ਨੀਤੀ

PowerShell ਸਕ੍ਰਿਪਟ ਫਾਈਲਾਂ ਦਾ ਐਕਸਟੈਂਸ਼ਨ .ps1 ਹੁੰਦਾ ਹੈ। ਸਕ੍ਰਿਪਟ ਚਲਾਉਣ ਤੋਂ ਪਹਿਲਾਂ ਤੁਹਾਨੂੰ ਚਲਾਉਣ ਦੀ ਨੀਤੀ ਸੈੱਟ ਕਰਨੀ ਪੈ ਸਕਦੀ ਹੈ। ਇਹ ਨੀਤੀ ਤੈਅ ਕਰਦੀ ਹੈ ਕਿ ਸਕ੍ਰਿਪਟਾਂ ਚੱਲ ਸਕਦੀਆਂ ਹਨ ਜਾਂ ਨਹੀਂ ਅਤੇ ਕਿਹੜੀਆਂ ਕਿਸਮਾਂ ਮਨਜ਼ੂਰ ਹਨ। ਇਸਨੂੰ ਸੈੱਟ ਕਰਨ ਲਈ Set-ExecutionPolicy ਕਮਾਂਡਲੇਟ ਵਰਤੋ। ਉਦਾਹਰਨ ਵਜੋਂ, ਸਕ੍ਰਿਪਟਾਂ ਚਲਾਉਣ ਦੀ ਇਜਾਜ਼ਤ ਲਈ:

```powershell
Set-ExecutionPolicy RemoteSigned
```

ਜਾਂ (ਸਿਰਫ਼ ਜਾਂਚ ਲਈ)

```powershell
Set-ExecutionPolicy Undefined
```

### PowerShell ਸਕ੍ਰਿਪਟਿੰਗ

PowerShell ਸਕ੍ਰਿਪਟਿੰਗ ਕਈ ਪ੍ਰਸ਼ਾਸਕੀ ਕੰਮ ਸਵੈਚਾਲਿਤ ਕਰਦੀ ਹੈ। ਇਸ ਵਿੱਚ ਵੇਰੀਏਬਲ, ਲੂਪ, ਸ਼ਰਤੀ ਕਥਨ ਅਤੇ ਫੰਕਸ਼ਨ ਸਮਰਥਿਤ ਹਨ, ਜਿਸ ਕਰਕੇ ਇਹ ਸਵੈਚਾਲਨ ਲਈ ਲਾਹੇਵੰਦ ਹੈ।

#### ਵੇਰੀਏਬਲ

PowerShell ਸਕ੍ਰਿਪਟਾਂ ਵਿੱਚ ਡਾਟਾ ਸੰਭਾਲਣ ਲਈ ਵੇਰੀਏਬਲ ਵਰਤੇ ਜਾਂਦੇ ਹਨ। ਇਨ੍ਹਾਂ ਦੇ ਨਾਂ ਡਾਲਰ ਚਿੰਨ੍ਹ ($) ਨਾਲ ਸ਼ੁਰੂ ਹੁੰਦੇ ਹਨ। ਵੇਰੀਏਬਲ ਨੂੰ ਮੁੱਲ ਦੇਣ ਲਈ ਇਹ ਰੂਪ ਵਰਤੋ:
```powershell
$variable_name = value
```
ਮਿਸਾਲ ਵਜੋਂ:
```powershell
$name = "John"
```
#### ਲੂਪ

ਲੂਪ ਕੋਡ ਦੇ ਹਿੱਸੇ ਨੂੰ ਨਿਸ਼ਚਿਤ ਗਿਣਤੀ ਵਿੱਚ ਦੁਹਰਾਉਂਦੇ ਹਨ। PowerShell ਇਹ ਲੂਪ ਸਮਰਥਿਤ ਕਰਦਾ ਹੈ:

- **For ਲੂਪ**: ਕੋਡ ਦੇ ਹਿੱਸੇ ਨੂੰ ਨਿਸ਼ਚਿਤ ਗਿਣਤੀ ਵਿੱਚ ਦੁਹਰਾਉਂਦਾ ਹੈ।
- **While ਲੂਪ**: ਸ਼ਰਤ ਸਹੀ ਰਹਿਣ ਤੱਕ ਕੋਡ ਦੁਹਰਾਉਂਦਾ ਹੈ।
- **Do-While ਲੂਪ**: ਕੋਡ ਘੱਟੋ-ਘੱਟ ਇੱਕ ਵਾਰ ਚਲਾਉਂਦਾ ਹੈ ਅਤੇ ਫਿਰ ਸ਼ਰਤ ਸਹੀ ਰਹਿਣ ਤੱਕ ਦੁਹਰਾਉਂਦਾ ਹੈ।
- **ForEach ਲੂਪ**: ਸਮੂਹ ਦੇ ਹਰ ਆਈਟਮ ਲਈ ਕੋਡ ਦੁਹਰਾਉਂਦਾ ਹੈ।

ਹੇਠਾਂ ਦਿੱਤਾ ਕੋਡ For ਲੂਪ ਨਾਲ 1 ਤੋਂ 5 ਤੱਕ ਦੇ ਅੰਕ ਦਿਖਾਉਂਦਾ ਹੈ:
```powershell
for($i=1; $i -le 5; $i++) {
Write-Host $i
}
```

#### ਸ਼ਰਤੀ ਕਥਨ

ਸ਼ਰਤੀ ਕਥਨ

ਸ਼ਰਤੀ ਕਥਨ ਨਿਰਧਾਰਤ ਸ਼ਰਤ ਸਹੀ ਹੋਣ ਉੱਤੇ ਕੋਡ ਦਾ ਹਿੱਸਾ ਚਲਾਉਂਦੇ ਹਨ। PowerShell ਇਹ ਕਿਸਮਾਂ ਸਮਰਥਿਤ ਕਰਦਾ ਹੈ:

- **If ਕਥਨ**: ਸ਼ਰਤ ਸਹੀ ਹੋਵੇ ਤਾਂ ਕੋਡ ਚਲਾਉਂਦਾ ਹੈ।
- **If-Else ਕਥਨ**: ਸ਼ਰਤ ਸਹੀ ਹੋਵੇ ਤਾਂ ਇੱਕ ਹਿੱਸਾ ਅਤੇ ਗਲਤ ਹੋਵੇ ਤਾਂ ਦੂਜਾ ਹਿੱਸਾ ਚਲਾਉਂਦਾ ਹੈ।
- **Switch ਕਥਨ**: ਮੁੱਲ ਨੂੰ ਸੰਭਾਵੀ ਮਿਲਾਣਾਂ ਨਾਲ ਤੁਲਨਾ ਕਰਦਾ ਹੈ ਅਤੇ ਪਹਿਲੇ ਮਿਲਾਣ ਦਾ ਹਿੱਸਾ ਚਲਾਉਂਦਾ ਹੈ।

ਮਿਸਾਲ ਵਜੋਂ, ਹੇਠਾਂ ਦਿੱਤਾ ਕੋਡ ਜਾਂਚਦਾ ਹੈ ਕਿ ਕੋਈ ਅੰਕ 5 ਤੋਂ ਵੱਡਾ ਹੈ ਜਾਂ ਨਹੀਂ:

```powershell
$number = 10
if ($number -gt 5) {
    Write-Host "ਅੰਕ 5 ਤੋਂ ਵੱਡਾ ਹੈ"
}
```
#### ਫੰਕਸ਼ਨ

ਫੰਕਸ਼ਨ ਕਿਸੇ ਖਾਸ ਕੰਮ ਲਈ ਦੁਬਾਰਾ ਵਰਤੇ ਜਾ ਸਕਣ ਵਾਲੇ ਕੋਡ ਹਿੱਸੇ ਹਨ। ਇਹ ਇਨਪੁੱਟ ਪੈਰਾਮੀਟਰ ਲੈਂਦੇ ਅਤੇ ਨਤੀਜੇ ਵਾਪਸ ਕਰਦੇ ਹਨ। PowerShell ਇਹ ਫੰਕਸ਼ਨ ਕਿਸਮਾਂ ਸਮਰਥਿਤ ਕਰਦਾ ਹੈ:

- **ਸਕ੍ਰਿਪਟ ਬਲਾਕ**: ਕੋਡ ਦਾ ਉਹ ਹਿੱਸਾ ਜੋ ਚਲਾਇਆ ਜਾ ਸਕਦਾ ਹੈ।
- **ਉੱਨਤ ਫੰਕਸ਼ਨ**: ਮੈਟਾਡਾਟਾ ਅਤੇ ਪੈਰਾਮੀਟਰ ਦੀ ਜਾਂਚ ਵਾਲਾ ਫੰਕਸ਼ਨ।

ਹੇਠਾਂ ਦਿੱਤਾ ਕੋਡ ਦੋ ਅੰਕ ਜੋੜਨ ਵਾਲਾ ਫੰਕਸ਼ਨ ਪਰਿਭਾਸ਼ਿਤ ਕਰਦਾ ਹੈ:
```powershell
function Add-Numbers {
    param (
        [int]$num1,
        [int]$num2
    )
    $result = $num1 + $num2
    return $result
}

$result = Add-Numbers -num1 5 -num2 10
Write-Host "ਨਤੀਜਾ $result ਹੈ"
```
### PowerShell ISE

PowerShell ISE (ਇਕੱਠਾ ਸਕ੍ਰਿਪਟਿੰਗ ਵਾਤਾਵਰਣ) PowerShell ਸਕ੍ਰਿਪਟਿੰਗ ਲਈ ਗ੍ਰਾਫ਼ਿਕਲ ਇੰਟਰਫੇਸ ਹੈ। ਇਸ ਵਿੱਚ ਲਿਖਤ ਸੰਪਾਦਕ, ਡੀਬੱਗਿੰਗ ਸਾਧਨ ਅਤੇ ਹੋਰ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਹਨ, ਜੋ ਸਕ੍ਰਿਪਟ ਲਿਖਣਾ ਤੇ ਜਾਂਚਣਾ ਸੌਖਾ ਕਰਦੀਆਂ ਹਨ। ਇਸਨੂੰ ਖੋਲ੍ਹਣ ਲਈ:

1. Start ਮੀਨੂ ਖੋਲ੍ਹੋ ਅਤੇ ਖੋਜ ਪੱਟੀ ਵਿੱਚ "PowerShell ISE" ਲਿਖੋ।
2. ਖੋਜ ਨਤੀਜਿਆਂ ਵਿੱਚ "Windows PowerShell ISE" ਚੁਣੋ।
3. PowerShell ISE ਨਵੀਂ ਵਿੰਡੋ ਵਿੱਚ ਖੁੱਲ੍ਹੇਗਾ।

### PowerShell Remoting

PowerShell Remoting ਨਾਲ ਦੂਰਲੇ ਕੰਪਿਊਟਰਾਂ ਉੱਤੇ PowerShell ਕਮਾਂਡਾਂ ਅਤੇ ਸਕ੍ਰਿਪਟਾਂ ਚਲਾਈਆਂ ਜਾ ਸਕਦੀਆਂ ਹਨ। ਸਥਾਨਕ ਅਤੇ ਦੂਰਲੇ ਦੋਵੇਂ ਕੰਪਿਊਟਰਾਂ ਉੱਤੇ WinRM ਸੇਵਾ ਚੱਲਣੀ ਲਾਜ਼ਮੀ ਹੈ। PowerShell Remoting ਚਾਲੂ ਕਰਨ ਲਈ:

1. ਪ੍ਰਸ਼ਾਸਕ ਅਧਿਕਾਰਾਂ ਨਾਲ PowerShell ਪ੍ਰੌਂਪਟ ਖੋਲ੍ਹੋ।
2. PowerShell Remoting ਚਾਲੂ ਕਰਨ ਲਈ ਇਹ ਕਮਾਂਡ ਚਲਾਓ:
```powershell
   Enable-PSRemoting -Force
```
3. ਦੂਰਲੇ ਕੰਪਿਊਟਰ ਨੂੰ TrustedHosts ਸੂਚੀ ਵਿੱਚ ਜੋੜਨ ਲਈ ਇਹ ਕਮਾਂਡ ਚਲਾਓ:
```powershell
Set-Item wsman:\localhost\Client\TrustedHosts -Value <computer name> -Force
```
4. WinRM ਸੇਵਾ ਮੁੜ ਚਾਲੂ ਕਰੋ।
```powershell
Restart-Service WinRM
```

ਦੂਰਲੇ ਕੰਪਿਊਟਰ ਉੱਤੇ PowerShell ਕਮਾਂਡ ਚਲਾਉਣ ਲਈ Invoke-Command ਕਮਾਂਡਲੇਟ ਵਰਤੋ:
```powershell
Invoke-Command -ComputerName <computer name> -ScriptBlock { <command> }
```
### PowerShell ਮੋਡੀਊਲ

PowerShell ਮੋਡੀਊਲ ਖਾਸ ਕੰਮਾਂ ਲਈ ਬਣੇ ਕਮਾਂਡਲੇਟ, ਫੰਕਸ਼ਨ ਅਤੇ ਸਕ੍ਰਿਪਟਾਂ ਦੇ ਸਮੂਹ ਹਨ। PowerShell Gallery ਰਾਹੀਂ ਇਨ੍ਹਾਂ ਨੂੰ ਇੰਸਟਾਲ ਅਤੇ ਸੰਭਾਲਿਆ ਜਾ ਸਕਦਾ ਹੈ। ਇਹ PowerShell ਮੋਡੀਊਲਾਂ ਦਾ ਕੇਂਦਰੀ ਭੰਡਾਰ ਹੈ।

PowerShell Gallery ਤੋਂ ਮੋਡੀਊਲ ਇੰਸਟਾਲ ਕਰਨ ਲਈ:
```powershell
Install-Module <module name>
```

ਇੰਸਟਾਲ ਕੀਤੇ PowerShell ਮੋਡੀਊਲ ਦੇਖਣ ਲਈ Get-InstalledModule ਵਰਤੋ:
```powershell
Get-InstalledModule
```

### PowerShell ਸਕ੍ਰਿਪਟਿੰਗ ਦੇ ਚੰਗੇ ਤਰੀਕੇ

**PowerShell ਸਕ੍ਰਿਪਟਾਂ** ਲਿਖਦੇ ਸਮੇਂ ਇਹ ਚੰਗੇ ਤਰੀਕੇ ਅਪਣਾਓ ਤਾਂ ਜੋ ਉਹ **ਸੁਰੱਖਿਅਤ**, **ਭਰੋਸੇਯੋਗ** ਅਤੇ **ਸੰਭਾਲਣ ਵਿੱਚ ਆਸਾਨ** ਹੋਣ:

- **ਵੇਰੀਏਬਲ ਦੇ ਸਪਸ਼ਟ ਨਾਂ ਰੱਖੋ**: ਉਦੇਸ਼ ਦੱਸਣ ਵਾਲੇ ਨਾਂ ਚੁਣੋ।
- **ਟਿੱਪਣੀਆਂ ਲਿਖੋ**: ਕੋਡ ਦਾ ਮਕਸਦ ਸਮਝਾਓ।
- **ਗਲਤੀਆਂ ਸੰਭਾਲੋ**: ਗਲਤੀਆਂ ਅਤੇ ਅਪਵਾਦਾਂ ਨਾਲ ਢੰਗ ਨਾਲ ਨਜਿੱਠੋ। PowerShell ਦਾ `Try...Catch...Finally` ਢਾਂਚਾ ਅਪਵਾਦ ਫੜ ਕੇ ਢੁਕਵੇਂ ਕਦਮ ਚੁੱਕਣ ਦਿੰਦਾ ਹੈ। [Microsoft ਦਸਤਾਵੇਜ਼](https://docs.microsoft.com/en-us/powershell/scripting/learn/deep-dives/everything-about-try-catch-finally?view=powershell-7.1)
- **ਸਕ੍ਰਿਪਟਾਂ ਦੀ ਚੰਗੀ ਤਰ੍ਹਾਂ ਜਾਂਚ ਕਰੋ**: ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਉਹ ਉਮੀਦ ਅਨੁਸਾਰ ਕੰਮ ਕਰਦੀਆਂ ਹਨ। **Pester**, PowerShell ਲਈ ਟੈਸਟਿੰਗ ਢਾਂਚਾ, ਨਾਲ ਯੂਨਿਟ ਟੈਸਟ ਲਿਖੇ ਅਤੇ ਚਲਾਏ ਜਾ ਸਕਦੇ ਹਨ। [Pester ਦਸਤਾਵੇਜ਼](https://pester.dev/)
- **ਫੰਕਸ਼ਨ ਅਤੇ ਮੋਡੀਊਲ ਵਰਤੋ**: ਕੋਡ ਨੂੰ ਸੰਗਠਿਤ ਕਰੋ ਅਤੇ ਮੁੜ ਵਰਤੋਂ ਸੁਧਾਰੋ। ਫੰਕਸ਼ਨ ਕੋਡ ਨੂੰ ਛੋਟੇ ਹਿੱਸਿਆਂ ਵਿੱਚ ਵੰਡਦੇ ਹਨ, ਜਦਕਿ ਮੋਡੀਊਲ ਕੋਡ ਪੈਕੇਜ ਅਤੇ ਵੰਡਣ ਦਿੰਦੇ ਹਨ। [ਫੰਕਸ਼ਨਾਂ ਬਾਰੇ](https://docs.microsoft.com/en-us/powershell/scripting/learn/deep-dives/everything-about-functions?view=powershell-7.1), [ਮੋਡੀਊਲਾਂ ਬਾਰੇ](https://docs.microsoft.com/en-us/powershell/scripting/learn/deep-dives/everything-about-modules?view=powershell-7.1)
- **ਮੁੱਲ ਕੋਡ ਵਿੱਚ ਪੱਕੇ ਨਾ ਲਿਖੋ**: ਪੈਰਾਮੀਟਰ ਜਾਂ ਵੇਰੀਏਬਲ ਵਰਤਣ ਨਾਲ ਸਕ੍ਰਿਪਟ ਲਚਕਦਾਰ ਅਤੇ ਮੁੜ ਵਰਤਣਯੋਗ ਬਣਦੀ ਹੈ। `param` ਕੀਵਰਡ ਨਾਲ ਸਕ੍ਰਿਪਟ ਨੂੰ ਪੈਰਾਮੀਟਰ ਦਿਓ। [Microsoft ਦਸਤਾਵੇਜ਼](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_functions_advanced_parameters?view=powershell-7.1)
- **ਵਿਸਤ੍ਰਿਤ ਆਉਟਪੁੱਟ ਵਰਤੋ**: ਸਕ੍ਰਿਪਟ ਦੀ ਤਰੱਕੀ ਬਾਰੇ ਵਾਧੂ ਜਾਣਕਾਰੀ ਦੇਣ ਲਈ `Write-Verbose` ਕਮਾਂਡਲੇਟ ਵਰਤੋ। [Microsoft ਦਸਤਾਵੇਜ਼](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/write-verbose?view=powershell-7.1)

### PowerShell ਸਕ੍ਰਿਪਟਿੰਗ ਦੇ ਚੰਗੇ ਤਰੀਕਿਆਂ ਦੀ ਵਿਆਖਿਆ

#### ਗਲਤੀਆਂ ਸੰਭਾਲੋ

PowerShell ਸਕ੍ਰਿਪਟਿੰਗ ਵਿੱਚ ਗਲਤੀ ਸੰਭਾਲਣਾ ਜ਼ਰੂਰੀ ਹੈ, ਤਾਂ ਜੋ ਸਕ੍ਰਿਪਟ ਗਲਤੀਆਂ ਅਤੇ ਅਪਵਾਦਾਂ ਨਾਲ ਢੰਗ ਨਾਲ ਨਜਿੱਠ ਸਕੇ। PowerShell ਵਿੱਚ Try-Catch ਕਥਨ, Trap ਕਥਨ ਅਤੇ ErrorAction ਪੈਰਾਮੀਟਰ ਵਰਗੇ ਕਈ ਤਰੀਕੇ ਹਨ। Try-Catch ਅਪਵਾਦ ਫੜ ਕੇ ਸੰਭਾਲਦਾ ਹੈ, Trap ਗਲਤੀਆਂ ਫੜ ਕੇ ਸੰਭਾਲਦਾ ਹੈ ਅਤੇ ErrorAction ਤੈਅ ਕਰਦਾ ਹੈ ਕਿ ਸਕ੍ਰਿਪਟ ਗਲਤੀ ਆਉਣ ਉੱਤੇ ਕਿਵੇਂ ਵਰਤੇ।

ਗਲਤੀ ਸੰਭਾਲਣ ਲਈ Try-Catch ਦੀ ਮਿਸਾਲ:
```powershell
try {
    # ਉਹ ਕੋਡ ਜਿਸ ਨਾਲ ਗਲਤੀ ਆ ਸਕਦੀ ਹੈ
}
catch {
    Write-Error "ਗਲਤੀ ਆਈ: $_"
}
```

#### ਸਕ੍ਰਿਪਟਾਂ ਦੀ ਚੰਗੀ ਤਰ੍ਹਾਂ ਜਾਂਚ ਕਰੋ

PowerShell ਸਕ੍ਰਿਪਟਾਂ ਦੀ ਜਾਂਚ ਕਰਨੀ ਜ਼ਰੂਰੀ ਹੈ ਤਾਂ ਜੋ ਪਤਾ ਲੱਗੇ ਕਿ ਉਹ ਉਮੀਦ ਅਨੁਸਾਰ ਚੱਲਦੀਆਂ ਹਨ। Pester ਵਰਗੇ ਟੈਸਟਿੰਗ ਸਾਧਨ ਅਤੇ ਢਾਂਚੇ ਟੈਸਟ ਲਿਖਣ ਤੇ ਚਲਾਉਣ ਦਿੰਦੇ ਹਨ। ਇਹ ਕੋਡ ਦੀਆਂ ਸਮੱਸਿਆਵਾਂ ਲੱਭਣ ਅਤੇ ਵੱਖ ਕਰਨ ਅਤੇ ਲੋੜਾਂ ਦੀ ਪੂਰਤੀ ਦੀ ਪੁਸ਼ਟੀ ਕਰਨ ਵਿੱਚ ਮਦਦ ਕਰਦੇ ਹਨ।

PowerShell ਸਕ੍ਰਿਪਟ ਜਾਂਚਣ ਲਈ Pester ਦੀ ਮਿਸਾਲ:
```powershell
Describe "ਮੇਰੀ PowerShell ਸਕ੍ਰਿਪਟ" {
    It "ਦਿੱਤਾ ਕੰਮ ਕਰਦੀ ਹੈ" {
        # ਉਹ ਕੋਡ ਜਿਸ ਤੋਂ ਉਮੀਦ ਕੀਤੀ ਜਾਂਦੀ ਹੈ ਕਿ ਨਤੀਜਾ ਵਾਪਸ ਕਰੇ
        $result = Do-Something
        $result | Should -Be "ਉਮੀਦ ਕੀਤਾ ਨਤੀਜਾ"
    }
}
```

#### ਫੰਕਸ਼ਨ ਅਤੇ ਮੋਡੀਊਲ ਵਰਤੋ

ਫੰਕਸ਼ਨ ਅਤੇ ਮੋਡੀਊਲ ਕੋਡ ਸੰਗਠਿਤ ਕਰਨ ਅਤੇ ਮੁੜ ਵਰਤਣ ਵਿੱਚ ਮਦਦ ਕਰਦੇ ਹਨ। ਫੰਕਸ਼ਨ ਕੋਡ ਨੂੰ ਮੁੜ ਵਰਤੇ ਜਾਣ ਵਾਲੇ ਹਿੱਸਿਆਂ ਵਿੱਚ ਰੱਖਦੇ ਹਨ, ਜਦਕਿ ਮੋਡੀਊਲ ਕੋਡ ਪੈਕੇਜ ਕਰਕੇ ਹੋਰਨਾਂ ਨਾਲ ਸਾਂਝਾ ਕਰਨ ਦਿੰਦੇ ਹਨ। ਇਨ੍ਹਾਂ ਨਾਲ ਸਕ੍ਰਿਪਟਾਂ ਹੋਰ ਮੋਡੀਊਲਰ, ਕਾਰਗਰ ਅਤੇ ਸੰਭਾਲਣ ਵਿੱਚ ਆਸਾਨ ਬਣਦੀਆਂ ਹਨ।

PowerShell ਫੰਕਸ਼ਨ ਦੀ ਮਿਸਾਲ:
```powershell
function Get-ProcessCount {
    $processes = Get-Process
    $count = $processes.Count
    return $count
}

$count = Get-ProcessCount
Write-Host "$count ਪ੍ਰਕਿਰਿਆਵਾਂ ਚੱਲ ਰਹੀਆਂ ਹਨ।"
```

#### ਮੁੱਲ ਕੋਡ ਵਿੱਚ ਪੱਕੇ ਨਾ ਲਿਖੋ

PowerShell ਸਕ੍ਰਿਪਟ ਵਿੱਚ ਮੁੱਲ ਪੱਕੇ ਲਿਖਣ ਨਾਲ ਲਚਕ ਘਟਦੀ ਅਤੇ ਸੰਭਾਲਣਾ ਔਖਾ ਹੁੰਦਾ ਹੈ। ਇਸ ਦੀ ਥਾਂ ਪੈਰਾਮੀਟਰ ਜਾਂ ਵੇਰੀਏਬਲ ਵਰਤੋ, ਤਾਂ ਜੋ ਵਰਤੋਂਕਾਰ ਚਲਾਉਂਦੇ ਸਮੇਂ ਮੁੱਲ ਦੇ ਸਕਣ। ਇਸ ਨਾਲ ਸਕ੍ਰਿਪਟ ਮੁੜ ਵਰਤਣ ਅਤੇ ਬਦਲਦੀਆਂ ਹਾਲਤਾਂ ਅਨੁਸਾਰ ਢਾਲਣੀ ਸੌਖੀ ਹੁੰਦੀ ਹੈ।

PowerShell ਪੈਰਾਮੀਟਰ ਦੀ ਮਿਸਾਲ:
```powershell
param (
    [string]$name
)

Write-Host "ਸਤ ਸ੍ਰੀ ਅਕਾਲ, $name!"
```

#### ਵਿਸਤ੍ਰਿਤ ਆਉਟਪੁੱਟ ਵਰਤੋ

ਵਿਸਤ੍ਰਿਤ ਆਉਟਪੁੱਟ ਸਕ੍ਰਿਪਟ ਦੀ ਤਰੱਕੀ ਬਾਰੇ ਵਾਧੂ ਜਾਣਕਾਰੀ ਦਿੰਦੀ ਹੈ ਅਤੇ ਡੀਬੱਗਿੰਗ ਤੇ ਸਮੱਸਿਆ ਹੱਲ ਕਰਨ ਵਿੱਚ ਕੰਮ ਆਉਂਦੀ ਹੈ। Write-Verbose ਕਮਾਂਡਲੇਟ ਕੰਸੋਲ ਉੱਤੇ ਜਾਣਕਾਰੀ ਦਿਖਾਉਂਦਾ ਹੈ ਅਤੇ ਸਕ੍ਰਿਪਟ ਸਮਝਣ ਤੇ ਡੀਬੱਗ ਕਰਨ ਵਿੱਚ ਸਹਾਇਤਾ ਕਰਦਾ ਹੈ।

PowerShell ਵਿੱਚ ਵਿਸਤ੍ਰਿਤ ਆਉਟਪੁੱਟ ਦੀ ਮਿਸਾਲ:
```powershell
function Get-ProcessCount {
    Write-Verbose "ਪ੍ਰਕਿਰਿਆਵਾਂ ਪ੍ਰਾਪਤ ਕੀਤੀਆਂ ਜਾ ਰਹੀਆਂ ਹਨ..."
    $processes = Get-Process
    $count = $processes.Count
    return $count
}

$count = Get-ProcessCount -Verbose
Write-Host "$count ਪ੍ਰਕਿਰਿਆਵਾਂ ਚੱਲ ਰਹੀਆਂ ਹਨ।"
```

### ਸ਼ੁਰੂਆਤੀਆਂ ਲਈ PowerShell ਸਕ੍ਰਿਪਟ ਦੇ ਦਸ ਵਿਚਾਰ

ਜੇ ਤੁਸੀਂ PowerShell ਸਕ੍ਰਿਪਟਿੰਗ ਵਿੱਚ ਨਵੇਂ ਹੋ, ਤਾਂ ਸ਼ੁਰੂ ਕਰਨ ਲਈ ਇਹ ਦਸ ਵਿਚਾਰ ਅਜ਼ਮਾਓ:

- **ਆਟੋਮੈਟਿਕ ਬੈਕਅੱਪ**: ਮਹੱਤਵਪੂਰਨ ਫਾਈਲਾਂ ਅਤੇ ਡਾਇਰੈਕਟਰੀਆਂ ਦਾ ਬੈਕਅੱਪ ਬਾਹਰੀ ਹਾਰਡ ਡਰਾਈਵ ਜਾਂ ਕਲਾਊਡ ਸਟੋਰੇਜ ਵਿੱਚ ਕਰਨ ਵਾਲੀ ਸਕ੍ਰਿਪਟ ਬਣਾਓ। ਫਾਈਲਾਂ ਕਾਪੀ ਕਰਨ ਲਈ `Copy-Item` ਅਤੇ ਬੈਕਅੱਪ ਪਿੱਛੇ ਚਲਾਉਣ ਲਈ `Start-Job` ਵਰਤੋ। [Microsoft ਦਸਤਾਵੇਜ਼](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/copy-item?view=powershell-7.1)

- **ਫਾਈਲ ਪ੍ਰਬੰਧਨ**: ਫਾਈਲਾਂ ਅਤੇ ਡਾਇਰੈਕਟਰੀਆਂ ਨੂੰ ਕਿਸਮ, ਆਕਾਰ ਜਾਂ ਹੋਰ ਮਾਪਦੰਡਾਂ ਮੁਤਾਬਕ ਫੋਲਡਰਾਂ ਵਿੱਚ ਰੱਖਣ ਵਾਲੀ ਸਕ੍ਰਿਪਟ ਬਣਾਓ। ਫਾਈਲਾਂ ਲੱਭਣ ਲਈ `Get-ChildItem` ਅਤੇ ਉਨ੍ਹਾਂ ਨੂੰ ਚਾਹੀਦੀ ਥਾਂ ਲਿਜਾਣ ਲਈ `Move-Item` ਵਰਤੋ। [Microsoft ਦਸਤਾਵੇਜ਼](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-childitem?view=powershell-7.1), [Microsoft ਦਸਤਾਵੇਜ਼](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/move-item?view=powershell-7.1)

- **ਸਿਸਟਮ ਜਾਣਕਾਰੀ**: CPU ਅਤੇ ਮੈਮੋਰੀ ਦੀ ਵਰਤੋਂ, ਡਿਸਕ ਦੀ ਥਾਂ ਅਤੇ ਨੈੱਟਵਰਕ ਸੈਟਿੰਗਾਂ ਵਰਗੀ ਜਾਣਕਾਰੀ ਇਕੱਠੀ ਕਰਕੇ ਪੜ੍ਹਨਯੋਗ ਰੂਪ ਵਿੱਚ ਦਿਖਾਉਣ ਵਾਲੀ ਸਕ੍ਰਿਪਟ ਬਣਾਓ। ਜਾਣਕਾਰੀ ਲੈਣ ਲਈ `Get-WmiObject` ਅਤੇ ਇਸਨੂੰ ਸਜਾਉਣ ਲਈ `Format-Table` ਜਾਂ `Out-GridView` ਵਰਤੋ। [Microsoft ਦਸਤਾਵੇਜ਼](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-wmiobject?view=powershell-7.1)

- **ਵਰਤੋਂਕਾਰ ਪ੍ਰਬੰਧਨ**: Windows ਵਿੱਚ ਵਰਤੋਂਕਾਰ ਅਤੇ ਸਮੂਹ ਜੋੜਨ, ਬਦਲਣ ਜਾਂ ਮਿਟਾਉਣ ਦਾ ਕੰਮ ਸਵੈਚਾਲਿਤ ਕਰਨ ਵਾਲੀ ਸਕ੍ਰਿਪਟ ਬਣਾਓ। ਵਰਤੋਂਕਾਰਾਂ ਲਈ `New-LocalUser`, `Set-LocalUser` ਅਤੇ `Remove-LocalUser`, ਅਤੇ ਸਮੂਹਾਂ ਲਈ `New-LocalGroup`, `Add-LocalGroupMember` ਅਤੇ `Remove-LocalGroup` ਵਰਤੋ। [Microsoft ਦਸਤਾਵੇਜ਼](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.localaccounts/new-localuser?view=powershell-7.1), [Microsoft ਦਸਤਾਵੇਜ਼](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.localaccounts/new-localgroup?view=powershell-7.1)

- **ਸਾਫਟਵੇਅਰ ਇੰਸਟਾਲੇਸ਼ਨ**: ਕਈ ਕੰਪਿਊਟਰਾਂ ਉੱਤੇ ਇੱਕੋ ਵੇਲੇ ਸਾਫਟਵੇਅਰ ਇੰਸਟਾਲ ਅਤੇ ਸੰਰਚਿਤ ਕਰਨ ਵਾਲੀ ਸਕ੍ਰਿਪਟ ਬਣਾਓ। ਦੂਰਲੇ ਕੰਪਿਊਟਰਾਂ ਉੱਤੇ ਇੰਸਟਾਲੇਸ਼ਨ ਕਮਾਂਡ ਚਲਾਉਣ ਲਈ `Invoke-Command` ਵਰਤੋ। [Microsoft ਦਸਤਾਵੇਜ਼](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/invoke-command?view=powershell-7.1)

- **ਨੈੱਟਵਰਕ ਸੰਰਚਨਾ**: IP ਪਤਾ, ਸਬਨੈੱਟ ਮਾਸਕ ਅਤੇ ਡਿਫਾਲਟ ਗੇਟਵੇ ਵਰਗੀਆਂ ਸੈਟਿੰਗਾਂ ਸੰਭਾਲਣ ਵਾਲੀ ਸਕ੍ਰਿਪਟ ਬਣਾਓ। ਇਨ੍ਹਾਂ ਲਈ `Set-NetIPAddress`, `Set-NetIPInterface` ਅਤੇ `Set-DnsClientServerAddress` ਵਰਤੋ। [Microsoft ਦਸਤਾਵੇਜ਼](https://docs.microsoft.com/en-us/powershell/module/nettcpip/set-netipaddress?view=win10-ps), [Microsoft ਦਸਤਾਵੇਜ਼](https://docs.microsoft.com/en-us/powershell/module/nettcpip/set-netipinterface?view=win10-ps), [Microsoft ਦਸਤਾਵੇਜ਼](https://docs.microsoft.com/en-us/powershell/module/dnsclient/set-dnsclientserveraddress?view=win10-ps)

- **ਸੁਰੱਖਿਆ**: ਸੁਰੱਖਿਆ ਸੈਟਿੰਗਾਂ ਦਾ ਆਡਿਟ ਅਤੇ ਨਿਗਰਾਨੀ ਕਰਕੇ ਤਬਦੀਲੀ ਮਿਲਣ ਉੱਤੇ ਵਰਤੋਂਕਾਰ ਨੂੰ ਸੁਚੇਤ ਕਰਨ ਵਾਲੀ ਸਕ੍ਰਿਪਟ ਬਣਾਓ। ਆਡਿਟ ਨੀਤੀਆਂ ਲੈਣ ਲਈ `Get-AuditPolicy` ਅਤੇ ਈਮੇਲ ਸੁਨੇਹੇ ਭੇਜਣ ਲਈ `Send-MailMessage` ਵਰਤੋ। [Microsoft ਦਸਤਾਵੇਜ਼](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.security/get-auditpolicy?view=powershell-7.1), [Microsoft ਦਸਤਾਵੇਜ਼](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/send-mailmessage?view=powershell-7.1)

- **ਕੰਮਾਂ ਦੀ ਸਮਾਂ-ਸਾਰਣੀ**: ਬੈਕਅੱਪ, ਅੱਪਡੇਟ ਅਤੇ ਸਿਸਟਮ ਜਾਂਚ ਵਰਗੇ ਦੁਹਰਾਏ ਕੰਮ ਤੈਅ ਅਤੇ ਸਵੈਚਾਲਿਤ ਕਰਨ ਵਾਲੀ ਸਕ੍ਰਿਪਟ ਬਣਾਓ। ਤੈਅ ਕੀਤੇ ਕੰਮ ਬਣਾਉਣ ਲਈ `Register-ScheduledTask` ਅਤੇ ਚਲਾਉਣ ਲਈ `Start-ScheduledTask` ਵਰਤੋ। [Microsoft ਦਸਤਾਵੇਜ਼](https://docs.microsoft.com/en-us/powershell/module/scheduledtasks/register-scheduledtask?view=win10-ps), [Microsoft ਦਸਤਾਵੇਜ਼](https://docs.microsoft.com/en-us/powershell/module/scheduledtasks/start-scheduledtask?view=win10-ps)

- **ਰਜਿਸਟਰੀ ਵਿੱਚ ਤਬਦੀਲੀ**: ਖਾਸ ਰਜਿਸਟਰੀ ਕੁੰਜੀਆਂ ਜਾਂ ਮੁੱਲਾਂ ਨੂੰ ਪੜ੍ਹਨ ਜਾਂ ਬਦਲਣ ਵਾਲੀ ਸਕ੍ਰਿਪਟ ਬਣਾਓ। ਰਜਿਸਟਰੀ ਨਾਲ ਕੰਮ ਕਰਨ ਲਈ `Get-ItemProperty` ਅਤੇ `Set-ItemProperty` ਵਰਤੋ। [Microsoft ਦਸਤਾਵੇਜ਼](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-itemproperty?view=powershell-7.1), [Microsoft ਦਸਤਾਵੇਜ਼](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/set-itemproperty?view=powershell-7.1)

- **ਦੂਰ-ਵਰਤੀ ਪ੍ਰਸ਼ਾਸਨ**: Windows ਕੰਪਿਊਟਰਾਂ ਦਾ ਦੂਰੋਂ ਪ੍ਰਬੰਧ ਚਾਲੂ ਕਰਨ ਵਾਲੀ ਸਕ੍ਰਿਪਟ ਬਣਾਓ, ਤਾਂ ਜੋ ਦੂਰਲੀਆਂ ਮਸ਼ੀਨਾਂ ਉੱਤੇ ਕਮਾਂਡਾਂ ਅਤੇ ਸਕ੍ਰਿਪਟਾਂ ਚਲ ਸਕਣ। ਦੂਰਲੇ ਕੰਪਿਊਟਰਾਂ ਉੱਤੇ ਕਮਾਂਡ ਚਲਾਉਣ ਲਈ `Enter-PSSession` ਜਾਂ `Invoke-Command` ਵਰਤੋ। [Microsoft ਦਸਤਾਵੇਜ਼](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/enter-pssession?view=powershell-7.1), [Microsoft ਦਸਤਾਵੇਜ਼](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/invoke-command?view=powershell-7.1)

ਅਮਲੀ ਤਜਰਬਾ ਲੈਣ ਅਤੇ PowerShell ਸਕ੍ਰਿਪਟਿੰਗ ਦਾ ਗਿਆਨ ਵਧਾਉਣ ਲਈ ਇਨ੍ਹਾਂ ਵਿਚਾਰਾਂ ਤੋਂ ਸ਼ੁਰੂ ਕਰੋ।

## ਸਿੱਟਾ

PowerShell Windows ਓਪਰੇਟਿੰਗ ਸਿਸਟਮ ਅਤੇ ਹੋਰ Microsoft ਤਕਨਾਲੋਜੀਆਂ ਦੇ ਪ੍ਰਬੰਧਨ ਅਤੇ ਸਵੈਚਾਲਨ ਲਈ ਸ਼ਕਤੀਸ਼ਾਲੀ ਸਾਧਨ ਹੈ। ਇਸ ਲੇਖ ਵਿੱਚ ਅਸੀਂ ਸ਼ੁਰੂਆਤੀਆਂ ਲਈ ਸਕ੍ਰਿਪਟਿੰਗ ਦੀਆਂ ਬੁਨਿਆਦਾਂ ਵੇਖੀਆਂ: ਇੰਸਟਾਲ ਅਤੇ ਚਾਲੂ ਕਰਨਾ, ਕਮਾਂਡਲੇਟ, ਵੇਰੀਏਬਲ, ਲੂਪ, ਸ਼ਰਤੀ ਕਥਨ ਅਤੇ ਫੰਕਸ਼ਨ ਵਰਤਣਾ, ਨਾਲ ਹੀ PowerShell ISE, PowerShell Remoting ਅਤੇ ਮੋਡੀਊਲ। ਚੰਗੇ ਤਰੀਕੇ ਅਪਣਾਉਣ ਨਾਲ ਸਕ੍ਰਿਪਟਾਂ ਸੁਰੱਖਿਅਤ, ਭਰੋਸੇਯੋਗ ਅਤੇ ਸੰਭਾਲਣ ਵਿੱਚ ਆਸਾਨ ਬਣਦੀਆਂ ਹਨ। ਅਭਿਆਸ ਨਾਲ ਤੁਸੀਂ PowerShell ਵਿੱਚ ਮਾਹਰ ਹੋ ਕੇ ਕਈ ਪ੍ਰਸ਼ਾਸਕੀ ਕੰਮ ਆਸਾਨੀ ਨਾਲ ਸਵੈਚਾਲਿਤ ਕਰ ਸਕਦੇ ਹੋ।
