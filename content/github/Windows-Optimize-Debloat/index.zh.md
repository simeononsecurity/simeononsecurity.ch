---
title: "使用 Windows-Optimize-Debloat 优化您的 Windows 电脑"
date: 2020-12-29
toc: true
draft: false
description: "使用 Windows-Optimize-Debloat 提高 Windows 操作系统的性能和隐私保护，这是一个全面的脚本，可帮助删除臃肿软件并优化系统设置。"
tags: ["视窗-优化-去毛刺", "Windows 优化", "浮动窗口", "加速 Windows", "优化 Windows 性能", "提升 Windows 性能", "Windows 系统优化", "微软", "隐私权", "删除垃圾软件", "Windows 10", "视窗 11", "Windows Defender", "Windows 更新", "科尔托纳", "组策略对象", "遥测", "Windows 应用商店", "Windows 10 专业版", "Windows 10 家庭版"]
---


[![Test script against windows docker container](https://github.com/simeononsecurity/Windows-Optimize-Debloat/actions/workflows/test-with-docker.yml/badge.svg)](https://github.com/simeononsecurity/Windows-Optimize-Debloat/actions/workflows/test-with-docker.yml)

*适用于希望尽量减少 Windows 10 和 11 安装次数的用户。

**注：** 本脚本适用于大多数系统，甚至所有系统。虽然 [@SimeonOnSecurity](https://github.com/simeononsecurity) creates, reviews, and tests each repo intensivly, we can not test every possible configuration nor does [@SimeonOnSecurity](https://github.com/simeononsecurity) take any responsibility for breaking your system. If something goes wrong, be prepared to submit an [issue](../../issues)如果不了解该脚本的作用，请勿运行。

## 简介：
开箱即用的 Windows 10 和 11 操作系统具有入侵性且不安全。
像 [Microsoft](https://microsoft.com), [PrivacyTools.io](https://PrivacyTools.io)等人建议更改配置，以优化和简化 Windows 10 操作系统。这些更改包括阻止遥测、删除日志和删除臃肿软件等等。本脚本旨在自动执行这些组织推荐的配置。

## 注意：
- 本脚本主要用于**个人使用**环境。
- 与其他脚本不同，本脚本的优化设计不会破坏 Windows 的核心功能。
 - Windows Update、Windows Defender、Windows Store 和 Cortona 等功能已受到限制，但不会像其他大多数 Windows 10 隐私脚本一样处于失灵状态。
- 如果您正在寻找一款只针对商业环境的最小化脚本，请参阅以下内容 [GitHub Repository](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)

## 要求：
- [X] Windows 10/11 企业版、Windows 10 专业版或 Windows 10 家庭版
  - Windows Home 不支持 GPO 配置。
    - 脚本仍然有效，但并非所有设置都适用。
  - Windows "N" Editions 未进行测试。
  - 运行 [Windows 10 Upgrade Assistant](https://support.microsoft.com/en-us/help/3159635/windows-10-update-assistant)更新并验证最新的主要版本。

## 修复微软账户或 Xbox 服务：
这是因为我们阻止登录微软账户。微软的遥测和身份关联是不受欢迎的。
不过，如果您仍希望使用这些服务，请参阅以下问题单以获得解决：
- https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/1
- https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/16
- https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/22

## 本程序集使用的脚本和工具列表：
- [Microsoft Security Compliance Toolkit 1.0](https://www.microsoft.com/en-us/download/details.aspx?id=55319)

## 考虑了其他配置：
- [BuiltByBel - PrivateZilla](https://github.com/builtbybel/privatezilla)
- [MelodysTweaks - Basic Tweaks](https://sites.google.com/view/melodystweaks/basictweaks)
- [Microsoft - Managing Windows 10 Telemetry and Callbacks](https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services)
- [Microsoft - Windows 10 Privacy](https://docs.microsoft.com/en-us/windows/privacy/)
- [Microsoft - Windows 10 VDI Recomendations](https://docs.microsoft.com/en-us/windows-server/remote/remote-desktop-services/rds_vdi-recommendations-1909)
- [Mirinsoft - SharpApp](https://github.com/builtbybel/sharpapp)
- [Mirinsoft - debotnet](https://github.com/builtbybel/debotnet)
- [UnderGroundWires - Privacy.S**Y](https://github.com/undergroundwires/privacy.sexy)
- [Sycnex - Windows10Debloater](https://github.com/Sycnex/Windows10Debloater)
- [The-Virtual-Desktop-Team - Virtual-Desktop-Optimization-Tool](https://github.com/The-Virtual-Desktop-Team/Virtual-Desktop-Optimization-Tool)
- [TheVDIGuys - Windows 10 VDI Optimize](https://github.com/TheVDIGuys/Windows_10_VDI_Optimize)
- [W4H4WK - Debloat Windows 10](https://github.com/W4RH4WK/Debloat-Windows-10/tree/master/scripts)

### 如何运行脚本：
#### 自动安装：
可以像这样从 GitHub 下载的提取文件中启动脚本：
```powershell
iwr -useb 'https://simeononsecurity.com/scripts/windowsoptimizeanddebloat.ps1'|iex
```
#### 手动安装：
如果是手动下载，则必须在包含来自 [GitHub Repository](https://github.com/simeononsecurity/Windows-Optimize-Debloat)

脚本 "sos-optimize-windows.ps1 "包含几个参数，可以自定义优化过程。每个参数都是一个布尔值，如果未指定，默认为 true。

- **$cleargpos**：清除组策略对象设置。
- **$installupdates**：为系统安装更新。
- **$removebloatware**：删除系统中不必要的程序和功能。
- **$disabletelemetry**：禁用数据收集和遥测。
- **$privacy**：进行更改以改善隐私。
- **$imagecleanup**：清理系统中不需要的文件。
- **$diskcompression**：压缩系统磁盘。
- **$updatemanagement**：改变系统管理和改进更新的方式。
- **$sosbrowsers**：优化系统的网络浏览器。

使用特定参数启动脚本的示例如下

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
Get-ChildItem -Recurse *.ps1 | Unblock-File
powershell.exe -ExecutionPolicy ByPass -File .\sos-optimize-windows.ps1 -cleargpos:$false -installupdates:$false
```

