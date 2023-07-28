---
title: "使用 Windows Defender PowerShell 命令提高系统安全性"
date: 2023-07-27
toc: true
draft: false
description: "了解 Windows Defender PowerShell 命令的强大功能，学习如何通过命令行控制增强系统安全性。"
genre: ["Windows Defender", "PowerShell 命令", "系统安全", "命令行控制", "杀毒", "视窗操作系统", "恶意软件保护", "高级安全设置", "自动化安全操作", "Windows PowerShell"]
tags: ["技术", "网络安全", "操作系统", "视窗", "命令行工具", "系统安全", "PowerShell", "杀毒软件", "恶意软件保护", "脚本"]
cover: "/img/cover/An_animated_illustration_depicting_a_shield_pr.png"
coverAlt: "一幅动画插图，描绘了保护计算机系统免受各种网络威胁的防护罩。"
coverCaption: "使用 Windows Defender PowerShell 命令增强系统安全性。"
---

## 简介

Windows Defender 由 Microsoft 开发，是 Windows 操作系统的集成防病毒和安全解决方案。它提供友好的用户界面，可有效管理安全设置。不过，对于喜欢命令行控制的高级用户，Windows Defender 提供了一套功能强大的 PowerShell 命令。在本文中，我们将深入**Windows Defender PowerShell命令**的世界，探索它们如何增强系统安全性并为您的Windows环境提供更强的控制能力。

## Windows Defender PowerShell 命令的威力

Windows Defender PowerShell命令使用户能够使用命令行界面执行高级安全操作。这些命令提供了广泛的功能，从扫描恶意软件等简单操作到配置高级安全设置等复杂任务。通过使用 PowerShell，用户可以自动执行安全操作、创建自定义脚本，并将 Windows Defender 无缝集成到现有工作流中。

## Windows Defender PowerShell 入门

要访问 Windows Defender PowerShell 命令，您需要打开一个具有管理权限的 PowerShell 会话。以下是开始使用的方法：

1.按 `Win + X`并从菜单中选择 **Windows PowerShell (Admin)**。
2.2. 如果出现提示，请单击**是**，允许应用程序对设备进行更改。

打开 PowerShell 会话后，您就可以开始使用 Windows Defender PowerShell 命令了。

## 常用 Windows Defender PowerShell 命令

### 1.**Get-MpComputerStatus**：检查 Windows Defender 状态

查看 `Get-MpComputerStatus`命令可概述系统中 Windows Defender 的当前状态，包括防病毒引擎版本、上次扫描时间和实时保护状态。通过运行此命令，您可以快速评估 Windows Defender 的总体健康状况，确保其处于最佳运行状态。

要检查 Windows Defender 状态，请打开具有管理权限的 PowerShell 会话并执行以下命令：

```powershell
Get-MpComputerStatus
```

该命令将显示以下信息：

- **AntivirusEngineVersion**：Windows Defender 使用的杀毒引擎版本号。
- **LastFullScanTime**：Windows Defender 上次执行全面扫描的日期和时间。
- **LastQuickScanTime**：Windows Defender 上次执行快速扫描的日期和时间。
- **RealTimeProtectionEnabled**：表示是否启用或禁用实时保护。

使用以下工具定期监控 Windows Defender 的状态 `Get-MpComputerStatus`确保您随时了解系统对潜在威胁的防护水平。

### 2. [**Update-MpSignature**](https://learn.microsoft.com/en-us/powershell/module/defender/update-mpsignature?view=windowsserver2022-ps)

"(《世界人权宣言》) `Update-MpSignature`命令使您能够手动更新 Windows Defender 使用的防病毒签名。反病毒签名包含已知恶意软件的重要信息，使 Windows Defender 能够有效地检测和阻止威胁。通过运行此命令，您可以确保您的系统拥有最新的签名，从而提供更强的防护，抵御新出现的威胁。

要手动更新 Windows Defender 签名，请打开具有管理权限的 PowerShell 会话并执行以下命令：

```powershell
Update-MpSignature
```
此命令会触发更新过程，**Windows Defender** 会连接到**Microsoft 服务器**下载最新的**防病毒签名**。更新完成后，Windows Defender 将拥有关于已知恶意软件的最新信息，从而增强其识别和消除威胁的能力。

保持 Windows Defender 签名的最新版本对于针对不断变化的**恶意软件**和**网络威胁**保持最高级别的保护至关重要。通过使用 `Update-MpSignature`确保 Windows Defender 可以有效保护您的系统。

### 3. [**Set-MpPreference**](https://learn.microsoft.com/en-us/powershell/module/defender/set-mppreference?view=windowsserver2022-ps)

"(《世界人权宣言》) `Set-MpPreference`命令可让您自定义各种**Windows Defender**设置，从而调整其行为以满足您的特定安全要求。该命令可灵活配置**实时保护**、**基于云的保护**和**网络检测系统设置**等选项。

例如，您可以使用 `Set-MpPreference`命令。实时保护会主动监控系统中的恶意活动，并对威胁做出即时响应。要启用实时保护，请执行以下命令：

```powershell
Set-MpPreference -DisableRealtimeMonitoring:$false
```

此外，您还可以利用该命令调整基于云的保护设置。基于云的保护利用云资源来加强威胁检测，并对新出现的威胁做出更快的反应。要启用基于云的保护，请使用以下命令：

```powershell
Set-MpPreference -EnableCloudProtection:$true
```

此外 `Set-MpPreference`命令可以自定义网络检测系统的设置。网络检查系统会分析网络流量，查找可疑活动和潜在威胁。要调整网络检测系统设置，请执行以下命令：

```powershell
Set-MpPreference -DisableIOAVProtection:$false
```

使用 `Set-MpPreference`您可以优化**Windows Defender**，使其符合您的特定安全需求，并确保提供强大的保护，防止恶意软件和其他恶意活动。

### 4. [**Start-MpScan**](https://learn.microsoft.com/en-us/powershell/module/defender/start-mpscan?view=windowsserver2022-ps)

"(《世界人权宣言》) `Start-MpScan`命令是在系统中启动恶意软件扫描的强大工具，可让您主动识别并消除恶意文件。该命令可灵活执行不同类型的扫描，包括**快速扫描**、**全面扫描**和**自定义扫描**，并提供特定路径。

要执行**快速扫描**，请使用 `Start-MpScan`命令，执行以下 PowerShell 命令：

```powershell
Start-MpScan -ScanType QuickScan
```

快速扫描侧重于恶意软件常见的系统关键区域，可迅速评估潜在威胁。

要进行更全面的扫描，检查系统中的所有文件和目录，可以启动**全面扫描**。使用以下命令执行全面扫描 `Start-MpScan`

```powershell
Start-MpScan -ScanType FullScan
```

全面扫描可确保彻底检测和清除系统中的恶意软件，但与快速扫描相比，全面扫描可能需要更长的时间才能完成。

除了预定义的扫描类型外，还可以使用 `Start-MpScan`命令可以通过指定要扫描的特定路径或文件来执行自定义扫描。例如，您可以使用以下命令扫描系统中的特定目录：

```powershell
Start-MpScan -ScanType CustomScan -ScanPath "C:\Path\To\Directory"
```

该命令将启动对指定目录的自定义扫描，允许你针对系统中的特定区域进行恶意软件检测。

通过利用 `Start-MpScan`通过该命令，您可以安排扫描、自动执行安全流程，并确保定期检测和减轻系统中的恶意软件。

### 5. [**Get-MpThreatCatalog**](https://learn.microsoft.com/en-us/powershell/module/defender/get-mpthreatcatalog?view=windowsserver2022-ps)

"(《世界人权宣言》) `Get-MpThreatCatalog`命令是获取已知威胁及其属性详细信息的宝贵资源。通过执行该命令，您可以访问全面的威胁目录，包括有关威胁严重性的数据、相关文件名以及建议采取的缓解措施。

要检索有关特定威胁的信息，请使用 `Get-MpThreatCatalog`请按照以下步骤操作：

1.打开具有管理权限的 PowerShell 会话。
2.执行以下命令

```powershell
   Get-MpThreatCatalog
```
该命令将显示已知威胁及其相应详细信息的列表。

输出的 `Get-MpThreatCatalog`指挥包括以下基本信息

- 威胁 ID**：威胁的唯一标识符。
- 严重性**：表示威胁的严重程度，从低到严重不等。
- **名称**：威胁的名称或描述。
- **路径**：与威胁相关的文件路径。
- **RecommendedAction**：为减轻威胁而建议采取的行动提供指导。

通过利用从 `Get-MpThreatCatalog`您可以获得有关潜在威胁的宝贵见解，并就采取适当行动减轻威胁做出明智决策。无论是隔离、移除还是监控特定威胁，详细的目录都能让您有效应对安全事件。

有关使用 `Get-MpThreatCatalog`和解释其结果，请参阅微软官方文档。

保持警惕，定期使用 `Get-MpThreatCatalog`命令，随时了解不断变化的威胁情况，并增强系统的安全性。

### 6. [**Add-MpPreference**](https://learn.microsoft.com/en-us/powershell/module/defender/add-mppreference?view=windowsserver2022-ps)

"(《世界人权宣言》) `Add-MpPreference`命令使您能够向 Windows Defender 添加排除项，从而自定义扫描和实时保护行为。通过添加排除项，您可以指定希望 Windows Defender 在安全扫描或实时保护过程中忽略的文件、文件夹或进程。

要添加排除项，请使用 `Add-MpPreference`你需要提供要排除的文件、文件夹或进程的路径或名称。下面是一个为文件夹添加排除项的示例：

```powershell
Add-MpPreference -ExclusionPath "C:\MyFolder"
```

此命令可确保 Windows Defender 跳过对指定文件夹的扫描，从而减少不必要的警报和对工作流程的潜在干扰。

排除在各种情况下都很有用，例如排除受信任的应用程序、开发环境或可能触发误报的特定文件。通过利用 `Add-MpPreference`您可以对 Windows Defender 进行微调，以满足您特定的安全需求并优化其性能。

利用 Windows Defender 提供的强大排除功能，在有效保护系统的同时，尽量减少误报和不必要的扫描中断。 `Add-MpPreference`

## 结论

Windows Defender PowerShell 命令提供了一套**强大的工具，**用于管理和增强 Windows 系统的安全性。利用这些命令，您可以**自动化安全操作*、**配置高级设置*，并将 Windows Defender 无缝地融入您的工作流程。无论您是**系统管理员**还是**高级用户**，探索 Windows Defender PowerShell 命令的功能都能显著改善您系统的安全状况。

请记住，权力越大，责任越大。在使用 PowerShell 命令时，请谨慎行事，并确保在执行命令前了解其影响。通过将您的知识与 Windows Defender PowerShell 命令的强大功能相结合，您可以采取积极主动的措施来保护系统免受不断演变的威胁。

## 参考资料

1.微软文档 [Windows Defender Cmdlets in Windows PowerShell](https://docs.microsoft.com/en-us/powershell/module/defender/?view=windowsserver2019-ps)
微软文档 [Introduction to Windows PowerShell](https://docs.microsoft.com/en-us/powershell/scripting/overview?view=powershell-7.1)
