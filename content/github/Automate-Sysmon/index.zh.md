---
title: "Automate-Sysmon：简化 Sysmon 部署和配置"
date: 2021-05-11
toc: true
draft: false
description: "了解如何使用 Automate-Sysmon 脚本部署和配置 Sysmon 以提高系统的安全性，该脚本甚至可以为新手用户简化流程。"
tags: ["自动化 Sysmon", "如何自动化 Sysmon", "如何自动化 Sysmon 配置", "如何安装 Sysmon", "电源外壳", "脚本", "系统部署", "系统配置", "系统日志", "威胁检测", "恶意活动", "SwiftOnSecurity 系统配置", "微软系统内部", "GitHub 资料库", "BHIS", "系统监控", "安全研究", "进程创建", "网络连接"]
---

Automate-Sysmon 是一个有用的脚本，可以简化 Sysmon 的部署和配置，Sysmon 是 Microsoft Sysinternals 的一个强大的系统监控工具。通过自动安装和设置 Sysmon，此脚本可提高系统的日志记录能力并增强威胁检测能力。

## 什么是 Sysmon？

Sysmon 是一种系统监控工具，可用于检测系统上的恶意活动。它提供有关进程创建、网络连接和其他系统事件的详细信息，使其成为安全专业人员的宝贵工具。虽然 Sysmon 是一个强大的工具，但设置和配置它可能具有挑战性。

## Automate-Sysmon 如何提供帮助？

Automate-Sysmon 脚本使安装和配置 Sysmon 变得容易，即使对于那些没有太多经验的人也是如此。该脚本使用流行的 **SwiftOnSecurity/sysmon-config** 模块，它为 Sysmon 提供了一组预配置的规则。此配置基于多年的安全研究，并由社区定期更新。

使用 Automate-Sysmon，您可以使用单个命令自动执行整个过程，也可以按照提供的说明手动安装 Sysmon。这种灵活性使用户可以轻松地自定义安装和配置以满足他们的特定需求。

## 如何使用Automate-Sysmon？

Automate-Sysmon 有两种使用方式：

### 自动安装：

要使用自动安装，只需在 PowerShell 中运行以下命令：
```powershell
iwr -useb 'https://simeononsecurity.ch/scripts/sosautomatesysmon.ps1'|iex
```

This will automatically download and run the Automate-Sysmon script.

### Manual Install:

If you prefer to install Sysmon manually, follow these steps:

1. Download the script and other required files from the [GitHub repository](https://github.com/simeononsecurity/Automate-Sysmon).
2. Launch PowerShell with administrator privileges.
3. Navigate to the directory containing the downloaded files.
4. Run the following command to change the PowerShell execution policy: ```Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force```
5. Unblock all the script files by running the following command: ```Get-ChildItem -Recurse *.ps1 | Unblock-File```
6. Run the following command to launch the Automate-Sysmon script: ```.\sos-automate-sysmon.ps1```


＃＃ 结论

总之，Automate-Sysmon 是安全专业人员的必备工具，他们希望提高日志记录能力并增强系统的威胁检测能力。凭借自动部署和配置 Sysmon 的能力，该工具甚至可以帮助新手用户充分利用 Sysmon。通过使用 **simeononsecurity/Automate-Sysmon** 模块，用户可以从社区的专业知识中受益，并了解最新的安全研究。因此，如果您想提高系统的安全性，请尝试使用 Automate-Sysmon！



