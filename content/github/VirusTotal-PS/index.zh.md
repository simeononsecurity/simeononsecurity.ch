---
title: "使用 VirusTotal PowerShell 模块进行高效病毒扫描"
date: 2020-11-24
toc: true
draft: false
description: "通过自动化与 VirusTotal API 的交互并简化您的安全工作流程，使用 VirusTotal PowerShell 模块执行高效的病毒扫描。"
tags: ["PowerShell 模块", "电源外壳", "自动化", "病毒总数", "病毒扫描", "域扫描", "API密钥", "病毒总API", "VirusTotal 开发者页面", "系统管理", "安全工作流程", "高效的病毒扫描", "下载并安装", "GitHub 资料库", "API 使用示例"]
---
 用于与 VirusTotal API 交互的 PowerShell 模块集合

**笔记：**
- 您需要您的 VirusTotal API 密钥，可以在您的[Shodan Account](https://www.virustotal.com/gui/)
- 模块中使用的 API 示例可以在[VirusTotal Developers Page](https://developers.virustotal.com/reference#getting-started)

＃＃ 下载并安装
- 从下载模块[GitHub Repository](https://github.com/simeononsecurity/VirusTotal-PS)
- 安装所有模块
```ps
Get-ChildItem -Recurse *.ps1 | Import-Module
```