---
title: "RSAT ActiveDirectory PowerShell モジュールのオフライン インストール"
date: 2020-12-16
draft: false
toc: true
description: "簡単な PowerShell スクリプトを使用して、RSAT ActiveDirectory PowerShell モジュールをオフラインでインストールする方法を学びます。"
tags: ["リモートサーバー管理ツールキット", "PowerShell RSAT ActiveDirectory モジュール", "ウィンドウズ10", "オフラインインストーラー", "PowerShell スクリプト", "パワーシェルモジュール", "アクティブディレクトリ", "ウィンドウズ", "オフライン", "インストール", "サーバ", "管理", "ツールキット", "スクリプト作成", "モジュール", "Windowsサーバー", "PowerShell コア", "Windows PowerShell", "マイクロソフト", "IT管理"]
---

 PowerShell RSAT ActiveDirectory モジュールをオフラインでインストールする

＃＃＃ インストールする方法：
1.[Download the script](https://github.com/simeononsecurity/Offine-PS-ActiveDirectory-Install/archive/master.zip)
2. 解凍したフォルダーから次のコマンドを実行します。```.\sos-offlinepsadinstall.ps1```

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
