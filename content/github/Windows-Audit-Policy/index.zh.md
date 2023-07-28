---
title: "使用 Windows 审计策略脚本最大化 Windows 审计功能"
date: 2021-05-10
toc: true
draft: false
description: "了解如何通过实施 Windows 审核策略脚本最大限度地提高 Windows 审核的安全性和监控能力。"
tags: ["Windows 审计策略", "视窗审计", "安全", "监测", "审计警察", "Windows 命令", "视窗安全", "审计配置", "安全政策", "事件日志", "系统监控", "Windows 服务器", "安全最佳做法", "网络安全", "日志分析", "安全合规性", "事件响应", "安全监控工具", "特权访问", "视窗管理", "脚本", "系统管理", "信息安全", "合规审计", "窗口加固", "安全控制", "安全自动化", "日志管理", "Windows 安全设置"]
---

## Windows 审计策略

[![VirusTotal Scan](https://github.com/simeononsecurity/Windows-Audit-Policy/actions/workflows/virustotal.yml/badge.svg)](https://github.com/simeononsecurity/Windows-Audit-Policy/actions/workflows/virustotal.yml)

最大化 Windows 审计功能

## 推荐阅读材料：
  - [auditpol](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/auditpol)
  - [auditpol clear](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/auditpol-clear)
  - [auditpol backup](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/auditpol-backup)
  - [auditpol restore](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/auditpol-restore)
  - [auditpol list](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/auditpol-list)

### 如何运行脚本
#### 手动安装：
如果手动下载，则必须从包含所有其他文件的目录中启动脚本。 [GitHub Repository](https://github.com/simeononsecurity/Windows-Audit-Policy)
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
Get-ChildItem -Recurse *.ps1 | Unblock-File
.\sos-auditpolicy.ps1
```
