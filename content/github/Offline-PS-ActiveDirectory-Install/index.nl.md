---
title: "Offline installatie RSAT ActiveDirectory PowerShell-module"
date: 2020-12-16
draft: false
toc: true
description: "Leer hoe u de RSAT ActiveDirectory PowerShell-module offline kunt installeren met een eenvoudig PowerShell-script."
tags: ["Toolkit voor serverbeheer op afstand", "PowerShell RSAT ActiveDirectory Module", "Windows 10", "Offline Installer", "PowerShell Script", "PowerShell-module", "ActiveDirectory", "Windows", "Offline", "Installeer", "Server", "Administratie", "Toolkit", "Scripting", "Module", "Windows Server", "PowerShell Kern", "Windows PowerShell", "Microsoft", "IT-administratie"]
---

 De PowerShell RSAT ActiveDirectory-module offline installeren

### Hoe te installeren:
1.[Download the script](https://github.com/simeononsecurity/Offine-PS-ActiveDirectory-Install/archive/master.zip)
2. Start vanuit de uitgepakte map```.\sos-offlinepsadinstall.ps1```

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
