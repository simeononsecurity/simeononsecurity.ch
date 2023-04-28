---
title: "Offline Install RSAT ActiveDirectory PowerShell Module"
date: 2020-12-16
draft: false
toc: true
description: "Learn how to install the RSAT ActiveDirectory PowerShell Module offline with a simple PowerShell script."
tags: ["Remote Server Administration Toolkit", "PowerShell RSAT ActiveDirectory Module", "Windows 10", "Offline Installer", "PowerShell Script", "PowerShell Module", "ActiveDirectory", "Windows", "Offline", "Install", "Server", "Administration", "Toolkit", "Scripting", "Module", "Windows Server", "PowerShell Core", "Windows PowerShell", "Microsoft", "IT Administration"]
---
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

  Installieren Sie das PowerShell-RSAT-ActiveDirectory-Modul offline  ### Wie installiert man: 1. [Skript herunterladen](https://github.com/simeononsecurity/Offine-PS-ActiveDirectory-Install/archive/master.zip) 2. Führen Sie im extrahierten Ordner „```.\sos-offlinepsadinstall.ps1``` aus 