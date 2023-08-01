---
title: "今天我学习了 Auditpol、Sysmon 和 Sysmon 配置"
date: 2021-05-11
toc: true
draft: false
description: ""
genre: ["PowerShell", "自动化", "Sysmon", "配置", "视窗安全", "事件监测", "视窗管理", "安全审计", "威胁猎杀", "恶意软件分析"]
tags: ["PowerShell", "自动化", "Sysmon", "配置", "SwiftOnSecurity", "视窗安全", "事件监测", "审计极", "Windows 审计策略", "自动系统监控", "Windows 审计策略", "开始使用 Sysmon", "恶意软件考古指南", "微软 Sysinternals", "Sysmon 配置", "Auditpol 命令", "审计政策备份", "审计政策明确", "审计极列表", "审计政策恢复", "Sysmon-Modular", "Windows 管理工具", "安全日志", "威胁检测", "事件记录", "安全监控", "Windows 安全最佳实践", "自动化解决方案", "安全审计技术"]
---

**SimeonOnSecurity 今天了解到的有趣内容**

SimeonOnSecurity 今天学习并发现了几件与 Windows 安全和事件监控有关的有趣事情。

首先，我们发现了两个新的和更新的资源库。Automate-Sysmon 资源库为 Sysmon 的自动化安装、配置和管理提供了解决方案，Sysmon 是一种用于监控和记录 Windows 系统上系统活动的流行工具。Windows-Audit-Policy 资源库为 Windows 审计策略的自动化配置提供了解决方案，该策略可控制对 Windows 系统上各种安全相关事件的审计。

SimeonOnSecurity 还找到了一些与 Windows 安全和事件监控相关的学习资源。Sysmon 入门》一文全面介绍了 Sysmon，包括其功能、优点以及如何有效使用。Malware Archaeology Cheat Sheets 提供了与恶意软件分析和威胁猎取相关的各种主题的简明可行的信息。Microsoft Sysinternals - Sysmon 文档提供有关 Sysmon 功能和使用的信息。sysmon-config 资源库提供一组预配置的 Sysmon 规则，可用作自定义 Sysmon 配置的起点。

最后，SimeonOnSecurity 找到了几个与 Windows 审计策略命令行工具 (auditpol) 相关的资源。auditpol backup、auditpol clear、auditpol list 和 auditpol restore 文档提供了如何使用这些命令管理 Windows 审计策略的信息。auditpol 文档全面介绍了 auditpol 工具及其功能。最后，sysmon-modular 资源库提供了一种配置 Sysmon 的模块化方法，这对具有复杂安全需求的大型企业非常有用。

## 新版本库/更新版本库：

- [simeononsecurity/Automate-Sysmon](https://github.com/simeononsecurity/Automate-Sysmon)
- [simeononsecurity/Windows-Audit-Policy](https://github.com/simeononsecurity/Windows-Audit-Policy)

## 学习资源：

- [BHIS - Getting Started With Sysmon](https://www.blackhillsinfosec.com/getting-started-with-sysmon/)
- [Malware Archaeology Cheat Sheets](https://www.malwarearchaeology.com/cheat-sheets)
- [Microsoft Sysinternals - Sysmon](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon)
- [SwiftOnSecurity/sysmon-config](https://github.com/SwiftOnSecurity/sysmon-config)
- [auditpol backup](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/auditpol-backup)
- [auditpol clear](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/auditpol-clear)
- [auditpol list](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/auditpol-list)
- [auditpol restore](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/auditpol-restore)
- [auditpol](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/auditpol)
- [olafhartong/sysmon-modular](https://github.com/olafhartong/sysmon-modular)
