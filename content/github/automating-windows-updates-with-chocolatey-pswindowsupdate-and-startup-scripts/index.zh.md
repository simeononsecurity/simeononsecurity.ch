---
title: "使用 Chocolatey、PSWindowsUpdate 和启动脚本通过自动化简化 Windows 更新"
date: 2020-07-22
---
 使用 Chocolatey、PSWindowsUpdate 和启动脚本的 Windows 更新**

在当今快节奏的商业环境中，时间对于系统管理员来说至关重要。更新 Windows 计算机是系统管理的一个重要方面，如果系统足够多，可能需要长达一周的时间才能完成，这可能是一项极其耗时的任务。但是，在 Chocolatey、PSWindowsUpdates 和 Startup Scripts 的帮助下，现在只需每台机器重新启动一次即可推出更新，从而显着减少执行更新所需的时间。

## 通过自动化简化 Windows 更新

Windows 更新对于维护 Windows 机器的稳定性和安全性至关重要。在大量机器上执行更新可能是一项耗时的任务，尤其是对于资源有限的系统管理员而言。但是，通过使用 Chocolatey、PSWindowsUpdate 和 Startup Scripts 等自动化工具，可以简化此过程，使管理员能够以最少的工作量执行更新。

###巧克力

[Chocolatey](https://chocolatey.org/) 是 Windows 的包管理器，可用于在 Windows 机器上自动安装软件。它类似于 Ubuntu 上的 apt-get 或 macOS 上的 homebrew，可用于安装和管理各种软件包。 Chocolatey 可用于静默安装包，这意味着它们可以在没有用户干预的情况下安装。

### PSWindows更新

[PSWindowsUpdate](https://www.powershellgallery.com/packages/PSWindowsUpdate/2.0.0.4) 是一个 PowerShell 模块，可用于自动安装 Windows 更新。它提供可用于安装、卸载和列出 Windows 更新的 cmdlet。 PSWindowsUpdate 是一款强大的工具，可用于管理多台机器上的 Windows 更新，非常适合需要管理大量机器的系统管理员。

### 启动脚本

[Startup Scripts](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/dn789190(v=ws.11)) 是可用于自动执行机器启动或关闭时需要执行的任务的脚本。这些脚本可用于执行安装软件、配置设置和管理 Windows 更新等任务。

## 通过单次重启自动执行 Windows 更新

要使用 Chocolatey、PSWindowsUpdate 和启动脚本自动执行 Windows 更新，管理员可以按照下面的分步指南进行操作。

### 设置关机脚本
从下载所有支持文件[GitHub Repository](https://github.com/simeononsecurity/ChocoAutomateWindowsUpdates)

1. 通过按 **“Win + R”** 并键入 **“gpedit.msc”** 然后 **“Ctrl + Shift + Enter”** 打开本地组策略编辑器。
2. 导航到计算机 **配置\Windows 设置\脚本（启动/关机）**。
3. 在结果窗格中，双击关机。
4. 选择 PowerShell 选项卡。
5. 在“关机属性”对话框中，单击“添加”。
6. 在“脚本名称”框中，键入脚本的路径，或单击“浏览”在域控制器上的 Netlogon 共享文件夹中搜索“*chocoautomatewindowsupdates.ps1*”。
7. 重启。

现在，管理员所要做的就是重新启动计算机以执行 Windows 更新。

### 理解脚本

用于自动执行 Windows 更新的脚本名为“*chocoautomatewindowsupdates.ps1*”。它执行以下任务：

1. 安装 Chocolatey 包管理器。
2. 启用几个首选的 Chocolatey 配置更改。
3. 升级所有已安装的 Chocolatey 软件包。
4. 安装 PSWindowsUpdate PowerShell 模块。
5. 增加Windows 更新服务管理器。
6. 安装所有可用的 Windows 更新。
7. 安装任何缺失的驱动程序或先前安装的更新所需的更新。

### 自动化 Windows 更新的好处

使用 Chocolatey、PSWindowsUpdate 和启动脚本自动执行 Windows 更新对系统管理员有几个好处。这些好处包括：

- **省时**：自动执行 Windows 更新可显着减少执行更新所需的时间。管理员不再需要在每台机器上手动安装更新。
- **一致性**：自动执行 Windows 更新可确保在所有计算机上一致地安装更新。这减少了错误和安全漏洞的可能性。
- **集中管理**：Windows 更新自动化允许管理员从中央位置管理更新，从而更容易跟踪哪些更新已安装以及哪些机器需要更新。
- **增强的安全性**：自动执行 Windows 更新可确保机器始终安装最新的安全补丁，从而降低安全漏洞的风险。

＃＃＃ 结论

使用 Chocolatey、PSWindowsUpdate 和启动脚本自动执行 Windows 更新是一个强大的工具，可以为系统管理员节省大量时间和精力。它允许一致且高效地安装更新，确保机器与最新的安全补丁保持同步。通过遵循本教程中概述的步骤，管理员只需一次重新启动即可自动执行 Windows 更新，从而使更新 Windows 机器的过程变得更快、更容易。
