---
title: "Offline Installa RSAT ActiveDirectory PowerShell Module"
date: 2020-12-16
draft: false
toc: true
description: "Informazioni su come installare il modulo RSAT ActiveDirectory PowerShell offline con un semplice script PowerShell."
tags: ["Kit di strumenti per l'amministrazione remota del server", "Modulo PowerShell RSAT ActiveDirectory", "Windows 10", "Programma di installazione offline", "Script di PowerShell", "Modulo PowerShell", "Directory attiva", "finestre", "disconnesso", "Installare", "server", "Amministrazione", "Kit di strumenti", "Scripting", "Modulo", "Server Windows", "Nucleo di PowerShell", "Windows PowerShell", "Microsoft", "Amministrazione informatica"]
---

 Installa il modulo PowerShell RSAT ActiveDirectory offline

### Come installare:
1.[Download the script](https://github.com/simeononsecurity/Offine-PS-ActiveDirectory-Install/archive/master.zip)
2. Dalla cartella estratta, esegui```.\sos-offlinepsadinstall.ps1```

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
