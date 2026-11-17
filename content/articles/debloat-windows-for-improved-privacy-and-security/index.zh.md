---
title: "提升安全性与隐私保护"
date: 2023-02-02
lastmod: 2026-11-09
toc: true
draft: false
description: "保持网络安全。了解加固 Windows 和移除不必要软件为何有助于提升安全性和隐私保护。"
tags: ["Windows 加固", "移除 Windows 中不必要的软件", "提升安全性", "隐私", "网络攻击", "操作系统安全", "Windows 操作系统", "数据隐私", "网络犯罪分子", "攻击面", "漏洞", "安全更新", "身份验证机制", "不需要的软件", "性能提升", "数据收集", "双因素身份验证", "防病毒软件", "反恶意软件", "敏感信息", "综合指南"]
cover: "/img/cover/debloat-windows-for-improved-privacy-and-security.webp"
coverAlt: "一幅电脑屏幕插画，显示加固 Windows 和移除不必要软件的进度条。深色背景上环绕着抽象的数字安全元素。"
coverCaption: ""
---

**Windows** 是全球使用最广泛的操作系统，因此经常成为网络犯罪分子的攻击目标。要保护数据和隐私，你需要采取安全措施来**加固系统并移除不必要的软件**。本指南会说明加固 Windows 和移除不必要软件的重要性，以及这些措施如何提升整体安全性和隐私保护。

## 什么是 Windows 加固？
Windows 加固是通过减少攻击面和漏洞来保护 Windows 操作系统的过程。具体做法包括**禁用或移除不需要的功能和服务**、安装安全更新，以及使用[强密码](https://simeononsecurity.com/articles/how-to-create-strong-passwords/)和身份验证机制。

## 为什么 Windows 加固很重要？
Windows 加固通过**减少潜在攻击途径的数量**，帮助抵御网络攻击。网络犯罪分子经常利用操作系统或应用程序中的漏洞访问系统或窃取敏感数据。加固系统可以**缩小攻击面**，增加攻击者入侵数据或侵犯隐私的难度。

## 什么是移除 Windows 中不必要的软件？
移除 Windows 中不必要的软件，是从 Windows 操作系统中**移除不需要或不想要的软件和服务**的过程。此举可以**提升系统性能和稳定性**，也能减少 Microsoft 和其他第三方软件收集与存储的数据，从而加强隐私保护。

## 为什么移除 Windows 中不必要的软件很重要？
从 Windows 系统中移除不必要的软件有助于**缩小攻击面并加强隐私保护**。许多不需要的软件和服务会收集你的使用习惯和个人信息，这些数据可能被出售或用于定向广告。移除这些不必要的功能，可以**减少收集和存储的数据量**，从而加强隐私和安全。

______

## 如何加固 Windows 并移除不必要的软件？
你可以按以下步骤加固 Windows 系统并移除不需要的软件：

1. **安装更新**：及时安装所有可用的安全更新，让系统保持最新状态。这有助于修补漏洞，防止网络犯罪分子加以利用。

2. **禁用不需要的服务**：许多在后台运行的服务都可以**禁用，以缩小攻击面并提升性能**。例如 Print Spooler 服务、Remote Registry 服务和 Remote Procedure Call (RPC) 服务。

3. **移除不需要的软件**：**卸载不再使用或不再需要的软件**，因为这些软件可能降低性能并带来安全漏洞。

4. **使用强密码**：为所有账户使用**强且唯一的密码**，并尽可能启用**双因素身份验证**。

5. **使用防病毒和反恶意软件**：安装并定期更新**防病毒和反恶意软件**，以抵御网络攻击。

## 更安全的移除顺序

移除组件会更改已安装的应用程序、计划任务、服务、策略和数据收集设置。应将每项操作视为配置变更，而不是一场清理竞赛。

1. 记录 Windows 版本和内部版本、已安装应用程序、启动项、服务、计划任务和当前隐私设置。
2. 创建经过测试的备份，并确认可通过本地管理员账户恢复系统。
3. 通过“设置”或供应商支持的卸载程序卸载未使用的应用程序。
4. 更改服务前，检查其用途、依赖项、启动模式、账户和工作负载。
5. 启用阻止功能前，先以审核模式测试 Defender 的攻击面缩减功能。检查事件，并在测试后仅添加范围明确的允许规则。
6. 按所有者和用途检查可选 Windows 功能和计划任务。不要仅因名称陌生就移除组件。
7. 重启并测试登录、网络、打印、更新、备份、VPN、辅助功能工具和业务应用程序。
8. 保留变更日志。如果测试失败，每次只恢复一项。

Microsoft 说明了攻击面缩减功能的审核模式，包括受控文件夹访问。审核模式会记录预期阻止的操作，但不会强制执行阻止。请参阅 [Microsoft 的攻击面缩减概述](https://learn.microsoft.com/en-us/defender-endpoint/attack-surface-reduction-overview?view=o365-worldwide)。

## 服务审查与回滚

原有示例需要补充说明。**远程过程调用 (RPC) 支持许多 Windows 组件，不应将其作为通用隐私措施禁用**。是否保留 Print Spooler 服务取决于计算机的用途。打印服务器需要此服务。即使计算机不需要打印，也应在更改前测试相关依赖项和应用程序。Remote Registry 也为一些管理工具提供支持。

更改服务前，先记录其当前状态：

```powershell
$name = 'Spooler'
Get-CimInstance Win32_Service -Filter "Name='$name'" |
    Select-Object Name, State, StartMode, StartName, PathName |
    Export-Csv "C:\Temp\$name-before.csv" -NoTypeInformation
Get-Service -Name $name -RequiredServices
Get-Service -Name $name -DependentServices
```

如果 Windows 或应用程序需要按需启动服务，先选 **Manual**，再考虑 **Disabled**。每次更改后都要测试。回滚时，恢复记录的启动模式并检查事件查看器：

```powershell
Set-Service -Name $name -StartupType Manual
Start-Service -Name $name
Get-Service -Name $name
```

不要在生产系统上运行未经审核的精简脚本。将脚本版本、导出的设置、服务原始值和恢复密钥记录保存在变更工单中。

## 隐私保护的局限

移除应用程序并不能证明 Windows 或其他已安装应用程序已停止发送遥测数据。隐私设置、账户配置、诊断策略、应用权限、网络控制和供应商条款都会影响数据流。应使用产品文档以及本地网络或事件证据，核实隐私变更是否有效。

Windows 10 的常规支持也已于 2025 年 10 月 14 日结束。精简后的 Windows 10 安装仍需要受支持的更新路径，或获批的生命周期例外。请参阅 [Microsoft 关于 Windows 10 停止支持的通知](https://learn.microsoft.com/en-us/lifecycle/announcements/windows-10-end-of-support)。

______

总之，加固 Windows 和移除不必要的软件是提升安全性与隐私保护的重要步骤。缩小攻击面并减少收集和存储的数据量，可以保护敏感信息并降低网络攻击风险。**今天就采取这些措施，让 Windows 系统保持安全可靠**。
