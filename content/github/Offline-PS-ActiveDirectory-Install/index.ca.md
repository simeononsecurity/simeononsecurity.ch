---
title: "Instal·leu fora de línia el mòdul PowerShell de RSAT ActiveDirectory"
date: 2020-12-16
draft: false
toc: true
description: "Apreneu a instal·lar el mòdul RSAT ActiveDirectory PowerShell fora de línia amb un script de PowerShell senzill."
tags: ["Kit d'eines d'administració de servidors remots", "Mòdul PowerShell RSAT ActiveDirectory", "Windows 10", "Instal·lador fora de línia", "Script de PowerShell", "Mòdul PowerShell", "Directori actiu", "Windows", "Fora de línia", "Instal·lar", "Servidor", "Administració", "Kit d'eines", "Guió", "Mòdul", "Windows Server", "PowerShell Core", "Windows PowerShell", "Microsoft", "Administració informàtica"]
---

 Instal·leu el mòdul PowerShell RSAT ActiveDirectory fora de línia

### Com instal · lar:
1.[Download the script](https://github.com/simeononsecurity/Offine-PS-ActiveDirectory-Install/archive/master.zip)
2. Des de la carpeta extreta, executeu```.\sos-offlinepsadinstall.ps1```

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
