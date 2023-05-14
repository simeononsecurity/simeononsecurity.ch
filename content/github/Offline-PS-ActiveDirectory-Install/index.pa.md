---
title: "RSAT ActiveDirectory PowerShell ਮੋਡੀਊਲ ਨੂੰ ਔਫਲਾਈਨ ਇੰਸਟਾਲ ਕਰੋ"
date: 2020-12-16
draft: false
toc: true
description: "ਇੱਕ ਸਧਾਰਨ PowerShell ਸਕ੍ਰਿਪਟ ਨਾਲ RSAT ActiveDirectory PowerShell ਮੋਡੀਊਲ ਨੂੰ ਔਫਲਾਈਨ ਕਿਵੇਂ ਸਥਾਪਿਤ ਕਰਨਾ ਹੈ ਬਾਰੇ ਸਿੱਖੋ।"
tags: ["ਰਿਮੋਟ ਸਰਵਰ ਐਡਮਿਨਿਸਟ੍ਰੇਸ਼ਨ ਟੂਲਕਿੱਟ", "PowerShell RSAT ਐਕਟਿਵ ਡਾਇਰੈਕਟਰੀ ਮੋਡੀਊਲ", "ਵਿੰਡੋਜ਼ 10", "ਔਫਲਾਈਨ ਇੰਸਟਾਲਰ", "PowerShell ਸਕ੍ਰਿਪਟ", "PowerShell ਮੋਡੀਊਲ", "ਐਕਟਿਵ ਡਾਇਰੈਕਟਰੀ", "ਵਿੰਡੋਜ਼", "ਔਫਲਾਈਨ", "ਇੰਸਟਾਲ ਕਰੋ", "ਸਰਵਰ", "ਪ੍ਰਸ਼ਾਸਨ", "ਟੂਲਕਿੱਟ", "ਸਕ੍ਰਿਪਟਿੰਗ", "ਮੋਡੀਊਲ", "ਵਿੰਡੋਜ਼ ਸਰਵਰ", "ਪਾਵਰਸ਼ੇਲ ਕੋਰ", "ਵਿੰਡੋਜ਼ ਪਾਵਰਸ਼ੇਲ", "ਮਾਈਕ੍ਰੋਸਾਫਟ", "ਆਈਟੀ ਪ੍ਰਸ਼ਾਸਨ"]
---

 PowerShell RSAT ActiveDirectory ਮੋਡੀਊਲ ਔਫਲਾਈਨ ਸਥਾਪਿਤ ਕਰੋ

### ਕਿਵੇਂ ਇੰਸਟਾਲ ਕਰਨਾ ਹੈ:
1.[Download the script](https://github.com/simeononsecurity/Offine-PS-ActiveDirectory-Install/archive/master.zip)
2. ਐਕਸਟਰੈਕਟ ਕੀਤੇ ਫੋਲਡਰ ਤੋਂ, ਚਲਾਓ```.\sos-offlinepsadinstall.ps1```

```powershell
#Require elivation for script run
#Requires -RunAsAdministrator

#Copy Files
#Install PowerShell Modules
Copy-Item -Path .\Files\ActiveDirectory -Destination "C:\Windows\System32\WindowsPowerShell\v1.0\Modules\" -Force -Recurse
#Install Required DLLs
Copy-Item -Path .\Files\WinSxS\* -Destination "C:\Windows\WinSxS\" -Force -Recurse

#Unblock New PowerShell Modules and DLLs
Get-ChildItem "C:\Windows\System32\WindowsPowerShell\v1.0\Modules\ActiveDirectory\" -recurse | Unblock-File
Unblock-File -Path "C:\Windows\WinSxS\Microsoft.ActiveDirectory.Management.resources.dll"
Unblock-File -Path "C:\Windows\WinSxS\Microsoft.ActiveDirectory.Management.dll"

#Install PowerShell Modules and DLLs
Import-Module -Name ActiveDirectory -Force -Global
Import-Module "C:\Windows\WinSxS\Microsoft.ActiveDirectory.Management.resources.dll" -Force -Global
Import-Module "C:\Windows\WinSxS\Microsoft.ActiveDirectory.Management.dll" -Force -Global
```
