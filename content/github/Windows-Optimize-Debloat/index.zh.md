---
title: "使用 Windows-Optimize-Debloat 优化您的 Windows PC"
date: 2020-12-29
toc: true
draft: false
description: "使用 Windows-Optimize-Debloat 提高 Windows 操作系统的性能和隐私，这是一个帮助删除过时软件和优化系统设置的综合脚本。"
tags: ["Windows-优化-Debloat", "视窗优化", "消肿 Windows", "加速 Windows", "优化 Windows 性能", "Windows 性能提升", "Windows 系统优化", "微软", "隐私", "删除过时软件", "视窗 10", "视窗 11", "Windows Defender的", "Windows更新", "科尔托纳", "组策略对象", "遥测", "Windows 应用商店", "Windows 10 专业版", "Windows 10 主页"]
---


[![Test script against windows docker container](https://github.com/simeononsecurity/Windows-Optimize-Debloat/actions/workflows/test-with-docker.yml/badge.svg)](https://github.com/simeononsecurity/Windows-Optimize-Debloat/actions/workflows/test-with-docker.yml)

*对于那些寻求最小化 Windows 10 和 11 安装的用户。*

**注意：**此脚本应该适用于大多数（如果不是全部）系统而不会出现问题。尽管[@SimeonOnSecurity](https://github.com/simeononsecurity) creates, reviews, and tests each repo intensivly, we can not test every possible configuration nor does [@SimeonOnSecurity](https://github.com/simeononsecurity) take any responsibility for breaking your system. If something goes wrong, be prepared to submit an [issue](../../issues) 如果您不了解它的作用，请不要运行该脚本。

＃＃ 介绍：
Windows 10 和 11 是开箱即用的侵入性和不安全的操作系统。
组织喜欢[Microsoft](https://microsoft.com), [PrivacyTools.io](https://PrivacyTools.io) 和其他人建议更改配置以优化和消除 Windows 10 操作系统。这些更改包括阻止遥测、删除日志和删除过时软件等等。该脚本旨在自动化这些组织推荐的配置。

## 注意事项：
- 此脚本设计用于主要在**个人使用**环境中运行。
- 此脚本的设计方式使得优化与其他一些脚本不同，不会破坏核心 Windows 功能。
 - Windows Update、Windows Defender、Windows Store 和 Cortona 等功能受到限制，但并未像大多数其他 Windows 10 隐私脚本那样处于功能障碍状态。
- 如果您寻求仅针对商业环境的最小化脚本，请参阅此[GitHub Repository](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)

＃＃ 要求：
- [X] Windows 10/11 企业版、Windows 10 专业版或 Windows 10 家庭版
  - Windows Home 不允许 GPO 配置。
    - 脚本仍然有效，但并非所有设置都适用。
  - Windows“N”版本未经测试。
  - 跑过[Windows 10 Upgrade Assistant](https://support.microsoft.com/en-us/help/3159635/windows-10-update-assistant) 更新和验证最新的主要版本。

## 修复 Microsoft 帐户或 Xbox 服务：
这是因为我们阻止登录 Microsoft 帐户。微软的遥测和身份关联是不受欢迎的。
但是，如果您仍希望使用这些服务，请参阅以下问题单以解决问题：
- https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/1
- https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/16
- https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/22

## 该集合使用的脚本和工具列表：
-[Microsoft Security Compliance Toolkit 1.0](https://www.microsoft.com/en-us/download/details.aspx?id=55319)

## 额外的配置是从以下方面考虑的：
-[BuiltByBel - PrivateZilla](https://github.com/builtbybel/privatezilla)
-[MelodysTweaks - Basic Tweaks](https://sites.google.com/view/melodystweaks/basictweaks)
-[Microsoft - Managing Windows 10 Telemetry and Callbacks](https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services)
-[Microsoft - Windows 10 Privacy](https://docs.microsoft.com/en-us/windows/privacy/)
-[Microsoft - Windows 10 VDI Recomendations](https://docs.microsoft.com/en-us/windows-server/remote/remote-desktop-services/rds_vdi-recommendations-1909)
-[Mirinsoft - SharpApp](https://github.com/builtbybel/sharpapp)
-[Mirinsoft - debotnet](https://github.com/builtbybel/debotnet)
-[UnderGroundWires - Privacy.S**Y](https://github.com/undergroundwires/privacy.sexy)
-[Sycnex - Windows10Debloater](https://github.com/Sycnex/Windows10Debloater)
-[The-Virtual-Desktop-Team - Virtual-Desktop-Optimization-Tool](https://github.com/The-Virtual-Desktop-Team/Virtual-Desktop-Optimization-Tool)
-[TheVDIGuys - Windows 10 VDI Optimize](https://github.com/TheVDIGuys/Windows_10_VDI_Optimize)
-[W4H4WK - Debloat Windows 10](https://github.com/W4RH4WK/Debloat-Windows-10/tree/master/scripts)

## 如何运行脚本：
### 自动安装：
该脚本可以从提取的 GitHub 下载中启动，如下所示：
```powershell
iwr -useb 'https://simeononsecurity.ch/scripts/windowsoptimizeanddebloat.ps1'|iex
```
### Manual Install:
If manually downloaded, the script must be launched from an administrative powershell in the directory containing all the files from the [GitHub Repository](https://github.com/simeononsecurity/Windows-Optimize-Debloat)

The script "sos-optimize-windows.ps1" includes several parameters that allow for customization of the optimization process. Each parameter is a boolean value that defaults to true if not specified.

- **$cleargpos**: Clears Group Policy Objects settings.
- **$installupdates**: Installs updates to the system.
- **$removebloatware**: Removes unnecessary programs and features from the system.
- **$disabletelemetry**: Disables data collection and telemetry.
- **$privacy**: Makes changes to improve privacy.
- **$imagecleanup**: Cleans up unneeded files from the system.
- **$diskcompression**: Compresses the system disk.
- **$updatemanagement**: Changes the way updates are managed and improved on the system.
- **$sosbrowsers**: Optimizes the system's web browsers.

An example of how to launch the script with specific parameters would be:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
Get-ChildItem -Recurse *.ps1 | Unblock-File
powershell.exe -ExecutionPolicy ByPass -File .\sos-optimize-windows.ps1 -cleargpos:$false -installupdates:$false
```

