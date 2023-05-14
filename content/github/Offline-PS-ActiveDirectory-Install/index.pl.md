---
title: "Instalacja offline modułu PowerShell RSAT ActiveDirectory"
date: 2020-12-16
draft: false
toc: true
description: "Dowiedz się, jak zainstalować moduł RSAT ActiveDirectory PowerShell Module w trybie offline za pomocą prostego skryptu PowerShell."
tags: ["Zestaw narzędzi do zdalnego administrowania serwerem", "PowerShell RSAT Moduł ActiveDirectory", "Windows 10", "Instalator offline", "Skrypt PowerShell", "Moduł PowerShell", "ActiveDirectory", "Windows", "Offline", "Zainstaluj", "Serwer", "Administracja", "Zestaw narzędzi", "Skryptowanie", "Moduł", "Windows Server", "PowerShell Core", "Windows PowerShell", "Microsoft", "Administracja IT"]
---

 Zainstaluj PowerShell RSAT ActiveDirectory Module Offline

### Jak zainstalować:
1.[Download the script](https://github.com/simeononsecurity/Offine-PS-ActiveDirectory-Install/archive/master.zip)
2. Z wyodrębnionego folderu uruchom```.\sos-offlinepsadinstall.ps1```

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
