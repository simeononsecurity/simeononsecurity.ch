---
title: "使用 Powershell 脚本自动化 Windows 10 STIG 合规性"
date: 2020-08-26
---

**从下载所有需要的文件[GitHub Repository](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)

**我们正在寻求以下帮助[.Net issue](https://github.com/simeononsecurity/W10-Optimize-and-Harden/issues/3) 

＃＃ 介绍：

Windows 10 是开箱即用的不安全操作系统，需要进行许多更改才能确保[FISMA](https://www.cisa.gov/federal-information-security-modernization-act) 遵守。
组织喜欢[Microsoft](https://microsoft.com), [Cyber.mil](https://public.cyber.mil), the [Department of Defense](https://dod.gov), and the [National Security Agency](https://www.nsa.gov/) 建议并要求更改配置以锁定、强化和保护操作系统并确保政府合规。这些更改涵盖了广泛的缓解措施，包括阻止遥测、宏、删除过时软件以及防止对系统的许多物理攻击。

独立系统是最难保护的系统之一。如果不是自动化的，它们需要手动更改每个 STIG/SRG。在典型部署中总共进行了 1000 多次配置更改，每次更改平均需要 5 分钟，相当于 3.5 天的工作量。该脚本旨在显着加快该过程。

## 注意事项：

- 此脚本专为在 **Enterprise** 环境中运行而设计，并假定您拥有满足所有要求的硬件支持。
  - 对于个人系统，请参阅此[GitHub Repository](https://github.com/simeononsecurity/W10-Optimize-and-Harden)
- 此脚本并非旨在使系统 100% 合规，而是应将其用作完成大部分（如果不是全部）可以编写脚本的配置更改的垫脚石。
  - 减去系统文档，此集合应使您对所有应用的 STIGS/SRG 的合规性达到约 95%。

＃＃ 要求：
- [X] 根据 STIG，Windows 10 Enterprise 是**必需的**。
-[x] [Standards](https://docs.microsoft.com/en-us/windows-hardware/design/device-experiences/oem-highly-secure) 适用于高度安全的 Windows 10 设备
-[x] System is [fully up to date](https://support.microsoft.com/en-gb/help/4027667/windows-10-update)
  - 目前是 Windows 10 **v1909** 或 **v2004**。
  - 跑过[Windows 10 Upgrade Assistant](https://support.microsoft.com/en-us/help/3159635/windows-10-update-assistant) 更新并验证最新的主要版本。
- [X] 硬件要求
  -[Hardware Requirements for Memory Integrity](https://docs.microsoft.com/en-us/windows/security/threat-protection/device-guard/requirements-and-deployment-planning-guidelines-for-virtualization-based-protection-of-code-integrity#baseline-protections) 
  -[Hardware Requirements for Windows Defender Application Guard](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-guard/reqs-wd-app-guard)
  -[Hardware Requirements for Windows Defender Credential Guard](https://docs.microsoft.com/en-us/windows/security/identity-protection/credential-guard/credential-guard-requirements)
  
## 推荐阅读材料：
  -[System Guard Secure Launch](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-system-guard/system-guard-secure-launch-and-smm-protection#requirements-met-by-system-guard-enabled-machines)
  -[System Guard Root of Trust](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-system-guard/system-guard-how-hardware-based-root-of-trust-helps-protect-windows)
  -[Hardware-based Isolation](https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-atp/overview-hardware-based-isolation)
  -[Memory integrity](https://docs.microsoft.com/en-us/windows/security/threat-protection/device-guard/memory-integrity)
  -[Windows Defender Application Guard](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-guard/wd-app-guard-overview)
  -[Windows Defender Credential Guard](https://docs.microsoft.com/en-us/windows/security/identity-protection/credential-guard/credential-guard-how-it-works)

## 该集合使用的脚本和工具列表：

-[Microsoft Security Compliance Toolkit 1.0](https://www.microsoft.com/en-us/download/details.aspx?id=55319)

-[Cyber.mil - Group Policy Objects](https://public.cyber.mil/stigs/gpo/)

-[NSACyber - Bitlocker Guidance](https://github.com/nsacyber/BitLocker-Guidance)

## 额外的配置被认为来自：

-[NSACyber - Hardware-and-Firmware-Security-Guidance](https://github.com/nsacyber/Hardware-and-Firmware-Security-Guidance)

-[NSACyber - Application Whitelisting Using Microsoft AppLocker](https://apps.nsa.gov/iad/library/ia-guidance/tech-briefs/application-whitelisting-using-microsoft-applocker.cfm)

## STIGS/SRGs 应用：
 
-[Windows 10 V1R23](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MS_Windows_10_V1R23_STIG.zip)

-[Windows Defender Antivirus V1R9](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MS_Windows_Defender_Antivirus_V1R9_STIG.zip)

-[Windows Firewall V1R7](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Windows_Firewall_V1R7_STIG.zip)

-[Internet Explorer 11 V1R19](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MS_IE11_V1R19_STIG.zip)

-[Adobe Reader Pro DC Continous V1R2](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Adobe_Acrobat_Pro_DC_Continuous_V1R2_STIG.zip)

-[Microsoft Office 2019/Office 365 Pro Plus V1R2](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MS_Office_365_ProPlus_V1R2_STIG.zip)

-[Microsoft Office 2016 V1R2](https://dl.dod.cyber.mil/wp-content/uploads/stigs/pdf/U_Microsoft_Office_2016_V1R2_Overview.pdf)

-[Microsoft Office 2013 V1R5](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MicrosoftOffice2013_V1R5_Overview.zip)

-[Google Chrome V1R19](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Google_Chrome_V1R19_STIG.zip)

-[Firefox V4R29](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MOZ_FireFox_V4R29_STIG.zip)

-[Microsoft .Net Framework 4 V1R9](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MS_DotNet_Framework_4-0_V1R9_STIG.zip) - **工作正在进行中**

-[Oracle JRE 8 V1R5](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Oracle_JRE_8_Windows_V1R5_STIG.zip)

## 如何运行脚本

**脚本可以从提取的 GitHub 下载中启动，如下所示：**
```
.\secure-standalone.ps1
```
我们将使用的脚本必须从包含所有其他文件的目录中启动[GitHub Repository](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)
