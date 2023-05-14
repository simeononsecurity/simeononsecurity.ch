---
title: "Instalação off-line do módulo RSAT ActiveDirectory PowerShell"
date: 2020-12-16
draft: false
toc: true
description: "Aprenda a instalar o RSAT ActiveDirectory PowerShell Module offline com um script simples do PowerShell."
tags: ["Kit de ferramentas de administração de servidor remoto", "Módulo PowerShell RSAT ActiveDirectory", "Windows 10", "Instalador offline", "Script do PowerShell", "Módulo PowerShell", "ActiveDirectory", "janelas", "desligada", "Instalar", "Servidor", "Administração", "Conjunto de ferramentas", "Scripts", "Módulo", "Windows Server", "Núcleo do PowerShell", "Windows PowerShell", "Microsoft", "Administração de TI"]
---

 Instale o módulo PowerShell RSAT ActiveDirectory offline

### Como instalar:
1.[Download the script](https://github.com/simeononsecurity/Offine-PS-ActiveDirectory-Install/archive/master.zip)
2. Na pasta extraída, execute```.\sos-offlinepsadinstall.ps1```

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
