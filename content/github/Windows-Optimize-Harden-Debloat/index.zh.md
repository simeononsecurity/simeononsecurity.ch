---
title: "使用 Windows-Optimize-Harden-Debloat 脚本优化和加固您的 Windows 系统"
date: 2020-12-29
toc: true
draft: false
description: "这份综合指南提供了有关如何优化、强化和消除 Windows 系统膨胀以提高性能、安全性和隐私的分步说明。"
tags: ["视窗优化", "Windows强化", "Windows 去肿", "Windows 安全", "Windows 性能", "Windows 隐私", "Windows 更新", "组策略对象", "Adobe Acrobat 阅读器", "火狐", "谷歌浏览器", "IE浏览器", "微软铬边缘", "点网4", "微软办公软件", "一个驱动器", "甲骨文Java JRE 8", "Windows 防火墙", "Windows Defender的", "应用锁"]
---
 介绍：

Windows 10 和 Windows 11 是开箱即用的侵入性和不安全的操作系统。
组织喜欢[PrivacyTools.io](https://PrivacyTools.io), [Microsoft](https://microsoft.com), [Cyber.mil](https://public.cyber.mil), the [Department of Defense](https://dod.gov), and the [National Security Agency](https://www.nsa.gov/) 已建议更改配置以锁定、强化和保护操作系统。这些更改涵盖了广泛的缓解措施，包括阻止遥测、宏、删除过时软件以及防止对系统的许多数字和物理攻击。该脚本旨在自动化这些组织推荐的配置。

## 注意、警告和注意事项：

**警告：**

该脚本应该适用于大多数（如果不是全部）系统而不会出现问题。尽管[@SimeonOnSecurity](https://github.com/simeononsecurity) creates, reviews, and tests each repo intensively, we can not test every possible configuration nor does [@SimeonOnSecurity](https://github.com/simeononsecurity) take any responsibility for breaking your system. If something goes wrong, be prepared to submit an [issue](../../issues)

- 此脚本设计用于主要在**个人使用**环境中运行。考虑到这一点，某些企业配置设置未实施。此脚本并非旨在使系统 100% 合规。相反，它应该被用作完成大部分（如果不是全部）配置更改的垫脚石，这些配置更改可以编写脚本，同时跳过品牌和横幅等问题，即使在强化的个人使用环境中也不应该实施这些问题。
- 此脚本的设计方式使得优化与其他一些脚本不同，不会破坏核心 Windows 功能。
- Windows Update、Windows Defender、Windows Store 和 Cortona 等功能受到限制，但不像大多数其他 Windows 10 隐私脚本那样处于功能失调状态。
- 如果您寻求仅针对商业环境的最小化脚本，请参阅此[GitHub Repository](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)


**如果您不了解它的作用，请不要运行此脚本。您有责任在运行之前检查和测试脚本。**

**例如，如果您在不采取预防措施的情况下运行它，以下内容将会中断：**

- 使用名为“Administrator”的默认管理员帐户被禁用并根据 DoD STIG 重命名

  - 不适用于创建的默认帐户，但适用于使用企业、物联网和 Windows 服务器版本中常见的默认管理员帐户

  - 在“计算机管理”下创建一个新帐户，并根据需要将其设置为管理员。然后在第一次登录新用户后将先前用户文件夹的内容复制到新用户文件夹中，以在运行脚本之前解决此问题。

- 根据 DoD STIG 禁用使用 Microsoft 帐户登录。

  - 尝试确保安全和私密时，不建议通过 Microsoft 帐户登录本地帐户。这是由这个 repo 强制执行的。

  - 在“计算机管理”下创建一个新帐户，并根据需要将其设置为管理员。然后在第一次登录新用户后将先前用户文件夹的内容复制到新用户文件夹中，以在运行脚本之前解决此问题。

- 根据 DoD STIG 禁用帐户 PIN

  - 单独使用 PIN 代替密码时是不安全的，并且可以在几小时甚至几秒或几分钟内轻松绕过

  - 运行脚本后从帐户中删除 PIN 和/或使用密码登录。

- 由于 DoD STIG，Bitlocker 默认值已更改和强化。

  - 由于 bitlocker 的实现方式，当发生此更改时，如果您已经启用了 bitlocker，它将破坏 bitlocker 的实现。

  - 禁用 bitlocker，运行脚本，然后重新启用 bitlocker 以解决此问题。

＃＃ 要求：

- [x] Windows 10/11 企业版（**首选**）或专业版
  - Windows 10/11 家庭版不支持 GPO 配置，未经测试。
  - 未测试窗口“N”版本。
-[x] [Standards](https://docs.microsoft.com/en-us/windows-hardware/design/device-experiences/oem-highly-secure) 适用于高度安全的 Windows 10 设备
-[x] System is [fully up to date and supported](https://support.microsoft.com/en-gb/help/4027667/windows-10-update)
  - 跑过[Windows Upgrade Assistant](https://support.microsoft.com/en-us/help/3159635/windows-10-update-assistant) 更新和验证最新的主要版本。
- [x] 在执行此脚本之前必须暂停或关闭 Bitlocker，它可以在重新启动后再次启用。
  - 可以在不禁用 bitlocker 的情况下运行此脚本的后续运行。
- [x] 硬件要求
  -[Hardware Requirements for Memory Integrity](https://docs.microsoft.com/en-us/windows/security/threat-protection/device-guard/requirements-and-deployment-planning-guidelines-for-virtualization-based-protection-of-code-integrity#baseline-protections)
  -[Hardware Requirements for Virtualization-Based Security](https://docs.microsoft.com/en-us/windows-hardware/design/device-experiences/oem-vbs)
  -[Hardware Requirements for Windows Defender Application Guard](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-guard/reqs-wd-app-guard)
  -[Hardware Requirements for Windows Defender Credential Guard](https://docs.microsoft.com/en-us/windows/security/identity-protection/credential-guard/credential-guard-requirements)

## 推荐阅读材料：

-[System Guard Secure Launch](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-system-guard/system-guard-secure-launch-and-smm-protection#requirements-met-by-system-guard-enabled-machines)
-[System Guard Root of Trust](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-system-guard/system-guard-how-hardware-based-root-of-trust-helps-protect-windows)
-[Hardware-based Isolation](https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-atp/overview-hardware-based-isolation)
-[Memory integrity](https://docs.microsoft.com/en-us/windows/security/threat-protection/device-guard/memory-integrity)
-[Windows Defender Application Guard](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-guard/wd-app-guard-overview)
-[Windows Defender Credential Guard](https://docs.microsoft.com/en-us/windows/security/identity-protection/credential-guard/credential-guard-how-it-works)

## 添加、显着更改和错误修复：

**此脚本在您的系统上添加、删除和更改设置。请在运行前检查脚本。**

### 浏览器：

- 浏览器将安装额外的扩展程序以帮助保护隐私和安全。
  - 看[here](https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/11) 了解更多信息。
- 由于为浏览器实施的 DoD STIG，设置了扩展管理和其他企业设置。有关如何查看这些选项的说明，您需要查看下面的 GPO 说明。

### Powershell 模块：

- 帮助自动化 Windows 更新 PowerShell[PSWindowsUpdate](https://www.powershellgallery.com/packages/PSWindowsUpdate/2.0.0.4) 模块将添加到您的系统中。

### 修复 Microsoft 帐户、商店或 Xbox 服务：

这是因为我们阻止登录 Microsoft 帐户。微软的遥测和身份关联是不受欢迎的。
但是，如果您仍希望使用这些服务，请参阅以下问题单以解决问题：

- https://github.com/simeononsecurity/Windows-Optimize-Debloat/issues/1
- https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/16
- https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/22

###事后在本地组策略中编辑策略：

如果您需要修改或更改设置，它们很可能可以通过 GPO 进行配置：

- 从此导入 ADMX 策略定义[repo](https://github.com/simeononsecurity/STIG-Compliant-Domain-Prep/tree/master/Files/PolicyDefinitions) 进入您要修改的系统上的 _C:\windows\PolicyDefinitions_。

- 在您尝试修改的系统上打开“gpedit.msc”。

## 该集合使用的脚本和工具列表：

### 第一方：

-[.NET-STIG-Script](https://github.com/simeononsecurity/.NET-STIG-Script)
-[Automate-Sysmon](https://github.com/simeononsecurity/Automate-Sysmon)
-[FireFox-STIG-Script](https://github.com/simeononsecurity/FireFox-STIG-Script)
-[JAVA-STIG-Script](https://github.com/simeononsecurity/JAVA-STIG-Script)
-[Standalone-Windows-STIG-Script](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)
-[Windows-Defender-STIG-Script](https://github.com/simeononsecurity/Windows-Defender-STIG-Script)
-[Windows-Optimize-Debloat](https://github.com/simeononsecurity/Windows-Optimize-Debloat)

＃＃＃ 第三者：

-[Cyber.mil - Group Policy Objects](https://public.cyber.mil/stigs/gpo/)
-[Microsoft Security Compliance Toolkit 1.0](https://www.microsoft.com/en-us/download/details.aspx?id=55319)
-[Microsoft Sysinternals - Sysmon](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon)

## STIGS/SRGs 应用：

-[Adobe Acrobat Pro DC Continuous V2R1](https://public.cyber.mil/stigs/downloads/)
-[Adobe Acrobat Reader DC Continuous V2R1](https://public.cyber.mil/stigs/downloads/)
-[Firefox V5R2](https://public.cyber.mil/stigs/downloads/)
-[Google Chrome V2R4](https://public.cyber.mil/stigs/downloads/)
-[Internet Explorer 11 V1R19](https://public.cyber.mil/stigs/downloads/)
-[Microsoft Edge V1R2](https://public.cyber.mil/stigs/downloads/)
-[Microsoft .Net Framework 4 V1R9](https://public.cyber.mil/stigs/downloads/)
-[Microsoft Office 2013 V2R1](https://public.cyber.mil/stigs/downloads/)
-[Microsoft Office 2016 V2R1](https://public.cyber.mil/stigs/downloads/)
-[Microsoft Office 2019/Office 365 Pro Plus V2R3](https://public.cyber.mil/stigs/downloads/)
-[Microsoft OneDrive STIG V2R1](https://public.cyber.mil/stigs/downloads/)
-[Oracle JRE 8 V1R5](https://public.cyber.mil/stigs/downloads/)
-[Windows 10 V2R2](https://public.cyber.mil/stigs/downloads/)
-[Windows Defender Antivirus V2R2](https://public.cyber.mil/stigs/downloads/)
-[Windows Firewall V1R7](https://public.cyber.mil/stigs/downloads/)

## 额外的配置被认为来自：

-[BuiltByBel - PrivateZilla](https://github.com/builtbybel/privatezilla)
-[CERT - IE Scripting Engine Memory Corruption](https://kb.cert.org/vuls/id/573168/)
-[Dirteam - SSL Hardening](https://dirteam.com/sander/2019/07/30/howto-disable-weak-protocols-cipher-suites-and-hashing-algorithms-on-web-application-proxies-ad-fs-servers-and-windows-servers-running-azure-ad-connect/)
-[MelodysTweaks - Basic Tweaks](https://sites.google.com/view/melodystweaks/basictweaks)
-[Microsoft - Managing Windows 10 Telemetry and Callbacks](https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services)
-[Microsoft - Reduce attack surfaces with attack surface reduction rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-atp/attack-surface-reduction)
-[Microsoft - Recommended block rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules)
-[Microsoft - Recommended driver block rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules)
-[Microsoft - Specture and Meltdown Mitigations](https://support.microsoft.com/en-us/help/4072698/windows-server-speculative-execution-side-channel-vulnerabilities)
-[Microsoft - Windows 10 Privacy](https://docs.microsoft.com/en-us/windows/privacy/)
-[Microsoft - Windows 10 VDI Recomendations](https://docs.microsoft.com/en-us/windows-server/remote/remote-desktop-services/rds_vdi-recommendations-1909)
-[Microsoft - Windows Defender Application Control](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/windows-defender-application-control-design-guide)
-[Mirinsoft - SharpApp](https://github.com/builtbybel/sharpapp)
-[Mirinsoft - debotnet](https://github.com/builtbybel/debotnet)
-[NSACyber - Application Whitelisting Using Microsoft AppLocker](https://apps.nsa.gov/iad/library/ia-guidance/tech-briefs/application-whitelisting-using-microsoft-applocker.cfm)
-[NSACyber - Bitlocker Guidance](https://github.com/nsacyber/BitLocker-Guidance)
-[NSACyber - Hardware-and-Firmware-Security-Guidance](https://github.com/nsacyber/Hardware-and-Firmware-Security-Guidance)
-[NSACyber - Windows Secure Host Baseline](https://github.com/nsacyber/Windows-Secure-Host-Baseline)
-[UnderGroundWires - Privacy.S\*\*Y](https://github.com/undergroundwires/privacy.sexy)
-[Sycnex - Windows10Debloater](https://github.com/Sycnex/Windows10Debloater)
-[The-Virtual-Desktop-Team - Virtual-Desktop-Optimization-Tool](https://github.com/The-Virtual-Desktop-Team/Virtual-Desktop-Optimization-Tool)
-[TheVDIGuys - Windows 10 VDI Optimize](https://github.com/TheVDIGuys/Windows_10_VDI_Optimize)
-[VectorBCO - windows-path-enumerate](https://github.com/VectorBCO/windows-path-enumerate)
-[W4H4WK - Debloat Windows 10](https://github.com/W4RH4WK/Debloat-Windows-10/tree/master/scripts)
-[Whonix - Disable TCP Timestamps](https://www.whonix.org/wiki/Disable_TCP_and_ICMP_Timestamps)

## 如何运行脚本：
### GUI - 引导式安装：

下载最新版本[here](https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat-GUI/releases/)选择你想要的选项并点击执行。 <img src="https://raw.githubusercontent.com/simeononsecurity/Windows-Optimize-Harden-Debloat/master/.github/images/WOHD-GUI.gif" alt="基于 Windows-Optimize-Harden-Debloat GUI 的引导式安装示例"> ### 自动安装：使用这一行自动下载、解压缩所有支持文件，并运行最新版本的脚本。```powershell
iwr -useb 'https://simeononsecurity.com/scripts/windowsoptimizeandharden.ps1'|iex
```

<img src="https://raw.githubusercontent.com/simeononsecurity/Windows-Optimize-Harden-Debloat/master/.github/images/w10automatic.gif" alt="Example of 
Windows-Optimize-Harden-Debloat automatic install">

### Manual Install:

If manually downloaded, the script must be launched from an administrative powershell in the directory containing all the files from the [GitHub Repository](https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat)

The script "sos-optimize-windows.ps1" includes several parameters that allow for customization of the optimization process. Each parameter is a boolean value that defaults to true if not specified.

- **cleargpos**: Clears Group Policy Objects settings.
- **installupdates**: Installs updates to the system.
- **adobe**: Implements the Adobe Acrobat Reader STIGs.
- **firefox**: Implements the FireFox STIG.
- **chrome**: Implements the Google Chrome STIG.
- **IE11**: Implements the Internet Explorer 11 STIG.
- **edge**: Implements the Microsoft Chromium Edge STIG.
- **dotnet**: Implements the Dot Net 4 STIG.
- **office**: Implements the Microsoft Office Related STIGs.
- **onedrive**: Implements the Onedrive STIGs.
- **java**: Implements the Oracle Java JRE 8 STIG.
- **windows**: Implements the Windows Desktop STIGs.
- **defender**: Implements the Windows Defender STIG.
- **firewall**: Implements the Windows Firewall STIG.
- **mitigations**: Implements General Best Practice Mitigations.
- **defenderhardening**: Implements and Hardens Windows Defender Beyond STIG Requirements.
- **pshardening**: Implements PowerShell Hardening and Logging.
- **sslhardening**: Implements SSL Hardening.
- **smbhardening**: Hardens SMB Client and Server Settings.
- **applockerhardening**: Installs and Configures Applocker (In Audit Only Mode).
- **bitlockerhardening**: Harden Bitlocker Implementation.
- **removebloatware**: Removes unnecessary programs and features from the system.
- **disabletelemetry**: Disables data collection and telemetry.
- **privacy**: Makes changes to improve privacy.
- **imagecleanup**: Cleans up unneeded files from the system.
- **nessusPID**: Resolves Unquoted System Strings in Path.
- **sysmon**: Installs and configures sysmon to improve auditing capabilities.
- **diskcompression**: Compresses the system disk.
- **emet**: Implements STIG Requirements and Hardening for EMET on Windows 7 Systems.
- **updatemanagement**: Changes the way updates are managed and improved on the system.
- **deviceguard**: Enables Device Guard Hardening.
- **sosbrowsers**: Optimizes the system's web browsers.

An example of how to launch the script with specific parameters would be:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
Get-ChildItem -Recurse *.ps1 | Unblock-File
powershell.exe -ExecutionPolicy ByPass -File .\sos-optimize-windows.ps1 -cleargpos:$false -installupdates:$false
```
