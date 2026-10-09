---
title: "使用 Windows Defender 完整加固 Windows 的指南..."
date: 2020-12-16
toc: true
draft: false
description: 学习如何使用 Windows Defender 应用程序控制 WDAC 通过脚本和工具加固您的 Windows 操作系统。
tags:
- Windows Defender 应用程序控制 WDAC 加固
- PowerShell
- PowerShell 脚本
- 自动化
- 合规性
- 蓝队
- Windows Defender STIG 脚本
- Windows Defender 加固
- Windows Defender STIG
- Defender STIG
- Windows Defender 漏洞防护 WDEP
- Windows Defender 攻击面缩减 ASR
- Windows Server 2016 2019
- Windows Server Core
- Microsoft WDAC-Toolkit
- 刷新 CI 策略
- 微软推荐的阻止规则
- 微软推荐的驱动阻止规则
- XML 策略
- BIN 策略
- 组策略
- Microsoft Intune
cover: /img/cover/Windows-Defender-Application-Control-Hardening.webp
coverAlt: 未来感服务器机房的插图，发光屏幕显示与 Windows Defender 应用程序控制相关的 XML 和 BIN 文件结构。深色背景增强了鲜艳的色彩。
coverCaption: ''
lastmod: 2026-10-08
---

**使用 Windows Defender 应用程序控制 WDAC 加固 Windows**

## 注意事项：
- Windows Server 2016/2019 或 1903 版本之前的系统仅支持一次使用单个传统策略。
- Windows Server Core 版本支持 [WDAC](https://simeononsecurity.com/til/2022-05-18/)，但某些依赖 AppLocker 的组件将无法工作。
- 请在实施或测试前阅读 [推荐阅读](https://github.com/simeononsecurity/Windows-Defender-Application-Control-Hardening#recommended-reading)。

## 本集合使用的脚本和工具列表：

- [MicrosoftDocs - WDAC-Toolkit](https://github.com/MicrosoftDocs/WDAC-Toolkit)
- [Microsoft - 刷新 CI 策略](https://www.microsoft.com/en-us/download/details.aspx?id=102925)

## 参考的其他配置来源：

- [微软 - 推荐的阻止规则](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules)
- [微软 - 推荐的驱动阻止规则](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules)
- [微软 - Windows Defender 应用程序控制](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/windows-defender-application-control-design-guide)

## 说明：

### XML 与 BIN：

- 简单来说，**“XML”** 策略用于本地应用于机器，**“BIN”** 文件用于通过 [组策略](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-windows-defender-application-control-policies-using-group-policy) 或 [Microsoft Intune](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-windows-defender-application-control-policies-using-intune) 强制执行。虽然本地部署可以使用 XML、BIN 或 CIP 策略，但一般建议尽可能使用 XML，尤其是在审计或故障排除时。

### 策略说明：

- **默认策略：**
  - “默认”策略仅使用 WDAC-Toolkit 中的默认功能。
- **推荐策略：**
  - “推荐”策略使用默认功能以及微软推荐的[阻止](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules)和[驱动阻止](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules)规则。
- **审计策略：**
  - “审计”策略仅记录规则的例外情况。用于在您的环境中测试，以便您可以根据需要修改策略以适应环境需求。
- **强制策略：**
  - “强制”策略不允许任何规则例外，应用程序、驱动程序、dll 等如果不符合将被阻止。

### 可用策略：

- **XML：**
  - **仅审计：**
    - `WDAC_V1_Default_Audit_{version}.xml`
    - `WDAC_V1_Recommended_Audit_{version}.xml`
  - **强制执行：**
    - `WDAC_V1_Default_Enforced_{version}.xml`
    - `WDAC_V1_Recommended_Enforced_{version}.xml`
- **BIN：**
  - **仅审计：**
    - `WDAC_V1_Default_Audit_{version}.bin`
    - `WDAC_V1_Recommended_Audit_{version}.bin`
  - **强制执行：**
    - `WDAC_V1_Default_Enforced_{version}.bin`
    - `WDAC_V1_Recommended_Enforced_{version}.bin`
- **CIP：**
  - **仅审计：**
    - `WDAC_V1_Default_Audit\{uid}.cip`
    - `WDAC_V1_Recommended_Audit\{uid}.cip`
  - **强制执行：**
    - `WDAC_V1_Default_Enforced\{uid}.cip`
    - `WDAC_V1_Recommended_Enforced\{uid}.cip`

在脚本中更新以下行以本地使用您想要的策略：

```powershell
$PolicyPath = "C:\temp\Windows Defender\CIP\WDAC_V1_Recommended_Enforced\*.cip"
#https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deployment/deploy-wdac-policies-with-script
ForEach ($Policy in (Get-ChildItem -Recurse $PolicyPath).Fullname) {
  $PolicyBinary = "$Policy"
  $DestinationFolder = $env:windir+"\System32\CodeIntegrity\CIPolicies\Active\"
  $RefreshPolicyTool = "./Files/EXECUTABLES/RefreshPolicy(AMD64).exe"
  Copy-Item -Path $PolicyBinary -Destination $DestinationFolder -Force
  & $RefreshPolicyTool
}
```

或者，您可以使用 [组策略](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-windows-defender-application-control-policies-using-group-policy) 或 [Microsoft Intune](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-windows-defender-application-control-policies-using-intune) 来强制执行 WDAC 策略。

## 审计：

您可以在事件查看器中查看 WDAC 事件日志，路径如下：

`Applications and Services Logs\Microsoft\Windows\CodeIntegrity\Operational`

## 推荐阅读：

- [Argonsys - 部署 Windows 10 应用程序控制策略](https://argonsys.com/microsoft-cloud/library/deploying-windows-10-application-control-policy/)
- [微软 - 审计 Windows Defender 应用程序控制策略](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/audit-windows-defender-application-control-policies)
- [微软 - 使用参考计算机为固定工作负载设备创建 WDAC 策略](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/create-initial-default-policy)
- [微软 - 通过组策略部署 Windows Defender 应用程序控制策略](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-windows-defender-application-control-policies-using-group-policy)
- [微软 - 通过 Microsoft Intune 部署 Windows Defender 应用程序控制策略](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-windows-defender-application-control-policies-using-intune)
- [微软 - 使用脚本部署 WDAC 策略](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deployment/deploy-wdac-policies-with-script)
- [微软 - 强制执行 Windows Defender 应用程序控制策略](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/enforce-windows-defender-application-control-policies)
- [微软 - 创建 WDAC 拒绝策略的指导](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/create-wdac-deny-policy)
- [微软 - 使用多个 Windows Defender 应用程序控制策略](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-multiple-windows-defender-application-control-policies)

## 如何运行脚本：

### 手动安装：

如果是手动下载，必须从包含所有文件的目录中以管理员权限的 PowerShell 启动脚本，文件来自 [GitHub 仓库](https://github.com/simeononsecurity/Windows-Defender-Application-Control-Hardening/archive/main.zip)

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
Get-ChildItem -Recurse *.ps1 | Unblock-File
.\sos-wdachardening.ps1
```
