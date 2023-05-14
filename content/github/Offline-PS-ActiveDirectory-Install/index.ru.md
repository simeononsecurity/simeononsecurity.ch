---
title: "Автономная установка модуля RSAT ActiveDirectory PowerShell"
date: 2020-12-16
draft: false
toc: true
description: "Узнайте, как установить модуль PowerShell RSAT ActiveDirectory в автономном режиме с помощью простого сценария PowerShell."
tags: ["Инструментарий удаленного администрирования сервера", "Модуль PowerShell RSAT ActiveDirectory", "Windows 10", "Автономный установщик", "Сценарий PowerShell", "Модуль PowerShell", "Активдиректори", "Окна", "Не в сети", "Установить", "Сервер", "Администрация", "Инструментарий", "Скрипты", "Модуль", "Windows-сервер", "Ядро PowerShell", "Windows PowerShell", "Майкрософт", "ИТ-администрирование"]
---

 Установите модуль PowerShell RSAT ActiveDirectory в автономном режиме

### Как установить:
1.[Download the script](https://github.com/simeononsecurity/Offine-PS-ActiveDirectory-Install/archive/master.zip)
2. Из извлеченной папки запустите```.\sos-offlinepsadinstall.ps1```

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
