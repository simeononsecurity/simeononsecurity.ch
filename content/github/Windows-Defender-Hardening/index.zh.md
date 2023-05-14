---
title: "使用 Defender 强化脚本增强 Windows 10 安全性"
date: 2020-11-15
toc: true
draft: false
description: "了解如何使用强化 Windows Defender 防病毒的 PowerShell 脚本增强 Windows 10 安全性，实现 Windows Defender 防病毒 STIG V2R1 的所有要求。"
tags: ["Windows Defender的", "视窗 10", "Windows 10 安全", "PowerShell 脚本", "硬化", "防御者强化", "安全自动化", "遵守", "受控文件夹访问", "入侵防御系统", "应用控制", "攻击面减少", "利用保护", "云提供的保护", "网络保护", "Windows Defender STIG 脚本", "Windows Defender STIG", "Windows Defender 防病毒软件 STIG V2R1", "世界数据中心", "自动识别率"]
---


## 这个脚本是做什么的？
- 启用云提供的保护
- 启用受控文件夹访问
- 启用网络保护
- 启用入侵防御系统
-[Enables Windows Defender Application Control Policies](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/windows-defender-application-control)
-[Enables Windows Defender Attack Surface Reduction Rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-atp/attack-surface-reduction)
-[Enables Windows Defender Exploit Protections](https://docs.microsoft.com/en-us/microsoft-365/security/defender-endpoint/enable-exploit-protection?view=o365-worldwide#powershell)
- 执行列在清单中的所有要求[Windows Defender Antivirus STIG V2R1](https://dl.cyber.mil/stigs/zip/U_MS_Windows_Defender_Antivirus_V2R1_STIG.zip)

＃＃ 要求：
- [x] Windows 10 企业版（**首选**）或 Windows 10 专业版
  - Windows 10 家庭版不允许 GPO 配置或[ASR](https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-atp/attack-surface-reduction) 
尽管这些配置中的大多数仍然适用。
  - Windows 10“N”版本未经测试。

## 下载所需文件：

从中下载所需的文件[GitHub Repository](https://github.com/simeononsecurity/Windows-Defender-STIG-Script)

## 如何运行脚本：

**脚本可以从提取的 GitHub 下载中启动，如下所示：**
```
.\sos-windowsdefenderhardening.ps1
```
