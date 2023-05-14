---
title: "离线安装 RSAT ActiveDirectory PowerShell 模块"
date: 2020-12-16
draft: false
toc: true
description: "了解如何使用简单的 PowerShell 脚本离线安装 RSAT ActiveDirectory PowerShell 模块。"
tags: ["远程服务器管理工具包", "PowerShell RSAT ActiveDirectory 模块", "视窗 10", "离线安装程序", "PowerShell 脚本", "PowerShell 模块", "活动目录", "视窗", "离线", "安装", "服务器", "行政", "工具包", "脚本", "模块", "视窗伺服器", "PowerShell 内核", "Windows PowerShell", "微软", "资讯科技行政"]
---

 脱机安装 PowerShell RSAT ActiveDirectory 模块

＃＃＃ 如何安装：
1.[Download the script](https://github.com/simeononsecurity/Offine-PS-ActiveDirectory-Install/archive/master.zip)
2. 从提取的文件夹中，运行```.\sos-offlinepsadinstall.ps1```

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
