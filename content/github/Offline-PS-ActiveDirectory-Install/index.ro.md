---
title: "Instalați offline modulul RSAT ActiveDirectory PowerShell"
date: 2020-12-16
draft: false
toc: true
description: "Aflați cum să instalați offline modulul RSAT ActiveDirectory PowerShell cu un script PowerShell simplu."
tags: ["Kit de instrumente de administrare a serverului la distanță", "Modulul PowerShell RSAT ActiveDirectory", "Windows 10", "Instalator offline", "Script PowerShell", "Modulul PowerShell", "Director activ", "Windows", "Deconectat", "Instalare", "Server", "Administrare", "Trusa de instrumente", "Scripting", "Modul", "Windows Server", "PowerShell Core", "Windows PowerShell", "Microsoft", "Administrare IT"]
---

 Instalați offline modulul PowerShell RSAT ActiveDirectory

### Cum să instalați:
1.[Download the script](https://github.com/simeononsecurity/Offine-PS-ActiveDirectory-Install/archive/master.zip)
2. Din folderul extras, rulați```.\sos-offlinepsadinstall.ps1```

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
