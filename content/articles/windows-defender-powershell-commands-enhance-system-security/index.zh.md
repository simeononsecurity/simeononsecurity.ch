---
title: "用于系统安全的 Windows Defender PowerShell 命令"
date: 2023-07-27
lastmod: 2026-11-20
toc: true
draft: false
description: "了解 Windows Defender PowerShell 命令的强大功能，学习如何通过命令行控制增强系统安全性。"
genre: ["Windows Defender", "PowerShell 命令", "系统安全", "命令行控制", "杀毒", "Windows 操作系统", "恶意软件保护", "高级安全设置", "自动化安全操作", "Windows PowerShell"]
tags: ["技术", "网络安全", "操作系统", "Windows", "命令行工具", "系统安全", "PowerShell", "杀毒软件", "恶意软件保护", "脚本"]
cover: "/img/cover/An_animated_illustration_depicting_a_shield_pr.webp"
coverAlt: "一幅动画插图，描绘了保护计算机系统免受各种网络威胁的防护罩。"
coverCaption: "使用 Windows Defender PowerShell 命令增强系统安全性。"
---

## 简介

Windows Defender 由 Microsoft 开发，是 Windows 操作系统的集成防病毒和安全解决方案。它提供友好的用户界面，可有效管理安全设置。不过，对于喜欢命令行控制的高级用户，Windows Defender 提供了一套功能强大的 PowerShell 命令。在本文中，我们将深入**Windows Defender PowerShell命令**的世界，探索它们如何增强系统安全性并为您的Windows环境提供更强的控制能力。

## Windows Defender PowerShell 命令的威力

Windows Defender PowerShell命令使用户能够使用命令行界面执行高级安全操作。这些命令提供了广泛的功能，从扫描恶意软件等简单操作到配置高级安全设置等复杂任务。通过使用 PowerShell，用户可以自动执行安全操作、创建自定义脚本，并将 Windows Defender 无缝集成到现有工作流中。

## Windows Defender PowerShell 入门

要访问 Windows Defender PowerShell 命令，您需要打开一个具有管理权限的 PowerShell 会话。以下是开始使用的方法：

1. 按 `Win + X`，再从菜单中选择 **Windows PowerShell (Admin)**（管理员）。
2. 如果出现提示，请单击**Yes** (是)，允许应用程序对设备进行更改。

打开 PowerShell 会话后，您就可以开始使用 Windows Defender PowerShell 命令了。

## 常用 Windows Defender PowerShell 命令

### 1. **Get-MpComputerStatus**：检查 Windows Defender 状态

`Get-MpComputerStatus` 命令可概述系统中 Windows Defender 的当前状态，包括防病毒引擎版本、上次扫描时间和实时保护状态。运行该命令可快速评估 Windows Defender 的运行状况。

要检查 Windows Defender 状态，请打开具有管理权限的 PowerShell 会话并执行以下命令：

```powershell
Get-MpComputerStatus
```

该命令将显示以下信息：

- **AntivirusEngineVersion**：Windows Defender 使用的杀毒引擎版本号。
- **LastFullScanTime**：Windows Defender 上次执行全面扫描的日期和时间。
- **LastQuickScanTime**：Windows Defender 上次执行快速扫描的日期和时间。
- **RealTimeProtectionEnabled**：表示是否启用或禁用实时保护。

定期使用 `Get-MpComputerStatus` 监控 Windows Defender 状态，有助于了解系统抵御潜在威胁的保护水平。

### 2. [**Update-MpSignature**](https://learn.microsoft.com/en-us/powershell/module/defender/update-mpsignature?view=windowsserver2022-ps)

`Update-MpSignature` 命令可让您手动更新 Windows Defender 使用的防病毒签名。签名包含已知恶意软件的重要信息，可帮助 Windows Defender 检测并阻止威胁。运行该命令可获取最新签名，增强对新出现威胁的防护。

要手动更新 Windows Defender 签名，请打开具有管理权限的 PowerShell 会话并执行以下命令：

```powershell
Update-MpSignature
```
此命令会触发更新过程，**Windows Defender** 会连接到**Microsoft 服务器**下载最新的**防病毒签名**。更新完成后，Windows Defender 将拥有关于已知恶意软件的最新信息，从而增强其识别和消除威胁的能力。

保持 Windows Defender 签名为最新版本，有助于抵御不断变化的 **恶意软件** 和 **网络威胁**。定期使用 `Update-MpSignature` 更新签名，可帮助 Windows Defender 有效保护系统。

### 3. [**Set-MpPreference**](https://learn.microsoft.com/en-us/powershell/module/defender/set-mppreference?view=windowsserver2022-ps)

`Set-MpPreference` 命令可让您自定义各种 **Windows Defender** 设置，以满足特定安全要求。该命令可配置 **实时保护**、**基于云的保护** 和 **网络检查系统设置** 等选项。

例如，您可以使用 `Set-MpPreference` 启用或禁用实时保护。实时保护会主动监控系统中的恶意活动并及时响应威胁。要启用实时保护，请执行以下命令：

```powershell
Set-MpPreference -DisableRealtimeMonitoring:$false
```

此外，您还可以利用该命令调整基于云的保护设置。基于云的保护利用云资源来加强威胁检测，并对新出现的威胁做出更快的反应。要启用基于云的保护，请使用以下命令：

```powershell
Set-MpPreference -EnableCloudProtection:$true
```

此外，您可以使用 `Set-MpPreference` 自定义网络检查系统的设置。该系统会分析网络流量，查找可疑活动和潜在威胁。要调整这些设置，请执行以下命令：

```powershell
Set-MpPreference -DisableIOAVProtection:$false
```

使用 `Set-MpPreference`，您可以优化 **Windows Defender**，使其符合您的特定安全需求，并确保提供强大的保护，防止恶意软件和其他恶意活动。

### 4. [**Start-MpScan**](https://learn.microsoft.com/en-us/powershell/module/defender/start-mpscan?view=windowsserver2022-ps)

`Start-MpScan` 命令可启动系统恶意软件扫描，帮助您主动发现并清除恶意文件。它支持 **快速扫描**、**全面扫描** 以及针对特定路径的 **自定义扫描**。

要使用 `Start-MpScan` 执行 **快速扫描**，请运行以下 PowerShell 命令：

```powershell
Start-MpScan -ScanType QuickScan
```

快速扫描侧重于恶意软件常见的系统关键区域，可迅速评估潜在威胁。

若要检查系统中的所有文件和目录，可以启动 **全面扫描**。使用 `Start-MpScan` 执行以下命令：

```powershell
Start-MpScan -ScanType FullScan
```

全面扫描可确保彻底检测和清除系统中的恶意软件，但与快速扫描相比，全面扫描可能需要更长的时间才能完成。

除预定义扫描类型外，`Start-MpScan` 还支持指定路径或文件进行自定义扫描。例如，您可以使用以下命令扫描系统中的特定目录：

```powershell
Start-MpScan -ScanType CustomScan -ScanPath "C:\Path\To\Directory"
```

该命令将启动对指定目录的自定义扫描，允许你针对系统中的特定区域进行恶意软件检测。

利用 `Start-MpScan`，您可以安排扫描、自动执行安全流程，并定期检测和缓解系统中的恶意软件。

### 5. [**Get-MpThreatCatalog**](https://learn.microsoft.com/en-us/powershell/module/defender/get-mpthreatcatalog?view=windowsserver2022-ps)

`Get-MpThreatCatalog` 命令可提供已知威胁及其属性的详细信息。该目录包括威胁严重性、关联文件名和建议的缓解措施等数据。

要使用 `Get-MpThreatCatalog` 检索特定威胁的信息，请按以下步骤操作：

1. 打开具有管理权限的 PowerShell 会话。
2. 执行以下命令

```powershell
   Get-MpThreatCatalog
```
该命令将显示已知威胁及其相应详细信息的列表。

`Get-MpThreatCatalog` 命令的输出包括以下重要信息：

- **ThreatID**：威胁的唯一标识符。
- **Severity**：表示威胁的严重程度，范围从 Low 到 Severe。
- **Name**：威胁的名称或描述。
- **Path**：与威胁相关的文件路径。
- **RecommendedAction**：提供减轻威胁的建议操作。

`Get-MpThreatCatalog` 提供的信息有助于评估潜在威胁并决定适当的处置方式。您可以隔离、删除或监控特定威胁。详细目录有助于有效应对安全事件。

有关 `Get-MpThreatCatalog` 的使用方法和结果解读，请参阅 Microsoft 官方文档。

定期使用 `Get-MpThreatCatalog` 了解不断变化的威胁，并增强系统安全性。

### 6. [**Add-MpPreference**](https://learn.microsoft.com/en-us/powershell/module/defender/add-mppreference?view=windowsserver2022-ps)

`Add-MpPreference` 命令可向 Windows Defender 添加排除项，以自定义扫描和实时保护行为。您可以指定在安全扫描或实时保护期间应忽略的文件、文件夹或进程。

要使用 `Add-MpPreference` 添加排除项，请提供要排除的文件、文件夹或进程的路径或名称。以下示例将文件夹添加到排除项：

```powershell
Add-MpPreference -ExclusionPath "C:\MyFolder"
```

此命令可确保 Windows Defender 跳过对指定文件夹的扫描，从而减少不必要的警报和对工作流程的潜在干扰。

排除项适用于受信任的应用程序、开发环境或可能触发误报的特定文件。使用 `Add-MpPreference` 可按安全需求调整 Windows Defender 并优化其性能。

使用 `Add-MpPreference` 的排除功能保护系统，同时减少误报和不必要的扫描中断。

## 2026 Defender 命令检查

仅当任务需要提升权限时，才在提升权限的会话中运行 Defender 命令。使用参数前，请查看目标 Windows 版本对应的最新模块帮助。记录现有配置，每次只更改一项设置，验证结果，并记下回滚命令。

可检查的项目包括保护状态、签名更新时间、排除项、首选项、扫描历史记录和近期检测结果。将排除范围限定在必要内容，并记录负责人和到期日期。当前 cmdlet 及其行为请参阅 [Microsoft Defender PowerShell 模块文档](https://learn.microsoft.com/en-us/powershell/module/defender/)和 [Microsoft Defender 防病毒文档](https://learn.microsoft.com/en-us/defender-endpoint/microsoft-defender-antivirus-windows)。

## 结论

Windows Defender PowerShell 命令提供一套**强大的工具**，用于管理和增强 Windows 系统安全。利用这些命令，您可以*自动化安全操作*、*配置高级设置*，并将 Windows Defender 融入现有工作流程。无论您是**系统管理员**还是**高级用户**，掌握这些命令都有助于显著改善系统安全态势。

请记住，权力越大，责任越大。在使用 PowerShell 命令时，请谨慎行事，并确保在执行命令前了解其影响。通过将您的知识与 Windows Defender PowerShell 命令的强大功能相结合，您可以采取积极主动的措施来保护系统免受不断演变的威胁。

## 参考资料

1. 微软文档 [Windows PowerShell 中的 Windows Defender cmdlet](https://docs.microsoft.com/en-us/powershell/module/defender/?view=windowsserver2019-ps)
2. 微软文档 [Windows PowerShell 简介](https://docs.microsoft.com/en-us/powershell/scripting/overview?view=powershell-7.1)
