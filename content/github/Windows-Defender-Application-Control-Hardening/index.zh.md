---
title: "使用 Windows Defender 应用程序控制 WDAC 强化 Windows 的完整指南"
date: 2020-12-16
toc: true
draft: false
description: "了解如何使用 Windows Defender Application Control WDAC 通过脚本和工具强化您的 Windows 操作系统。"
tags: ["Windows Defender 应用程序控制 WDAC 加固", "电源外壳", "PowerShell 脚本", "自动化", "遵守", "蓝队", "Windows Defender STIG 脚本", "Windows Defender 强化", "Windows Defender STIG", "后卫斯蒂格", "Windows Defender 漏洞利用保护 WDEP", "Windows Defender 攻击面减少 ASR", "Windows 服务器 2016 2019", "Windows 服务器核心", "Microsoft WDAC-工具包", "刷新 CI 策略", "微软推荐的阻止规则", "Microsoft 推荐的驱动程序块规则", "XML 政策", "BIN政策", "组策略", "微软 Intune"]
---

**使用 Windows Defender 应用程序控制 WDAC 强化 Windows**

## 注意事项：
- Windows Server 2016/2019 或版本 1903 之前的任何版本一次仅支持一个遗留策略。
- Windows Server Core 版本支持 WDAC，但某些依赖于 AppLocker 的组件将无法运行
- 请阅读[Recommended Reading](https://github.com/simeononsecurity/Windows-Defender-Application-Control-Hardening#recommended-reading) 在实施甚至测试之前。

## 该集合使用的脚本和工具列表：

-[MicrosoftDocs - WDAC-Toolkit](https://github.com/MicrosoftDocs/WDAC-Toolkit)
-[Microsoft - Refresh CI Policy ](https://www.microsoft.com/en-us/download/details.aspx?id=102925)

## 额外的配置被认为来自：

-[Microsoft - Recommended block rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules)
-[Microsoft - Recommended driver block rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules)
-[Microsoft - Windows Defender Application Control](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/windows-defender-application-control-design-guide)

＃＃ 解释：

### XML 与 BIN：

- 简而言之，**“XML”** 策略用于在本地应用到机器，而**“BIN”** 文件用于强制执行它们[Group Policy](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-windows-defender-application-control-policies-using-group-policy) or [Microsoft Intune](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-windows-defender-application-control-policies-using-intune) 虽然您可以在本地部署中使用 XML、BIN 或 CIP 策略，但一般来说，您应该尽可能坚持使用 XML，尤其是在审计或故障排除时。

###政策说明：

- **默认策略：**
  - “默认”策略仅使用 WDAC 工具包中可用的默认功能。
- **推荐政策：**
  - “推荐”策略使用默认功能以及 Microsoft 推荐的功能[blocks](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules) and [driver block](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules) 规则。
- **审计政策：**
  - “审计”政策，只记录规则的例外情况。这是为了在您的环境中进行测试，以便您可以随意修改策略以满足您的环境需求。
- **强制政策：**
  - “强制”策略不允许任何规则例外，应用程序、驱动程序、dll 等如果不遵守将被阻止。

### 可用政策：

- **XML：**
  - **仅审计：**
    -`WDAC_V1_Default_Audit_{version}.xml`
    -`WDAC_V1_Recommended_Audit_{version}.xml`
  - **强制执行：**
    -`WDAC_V1_Default_Enforced_{version}.xml`
    -`WDAC_V1_Recommended_Enforced_{version}.xml`
- **垃圾桶：**
  - **仅审计：**
    -`WDAC_V1_Default_Audit_{version}.bin`
    -`WDAC_V1_Recommended_Audit_{version}.bin`
  - **强制执行：**
    -`WDAC_V1_Default_Enforced_{version}.bin`
    -`WDAC_V1_Recommended_Enforced_{version}.bin`
- **CIP：**
  - **仅审计：**
    -`WDAC_V1_Default_Audit\{uid}.cip`
    -`WDAC_V1_Recommended_Audit\{uid}.cip`
  - **强制执行：**
    -`WDAC_V1_Default_Enforced\{uid}.cip`
    -`WDAC_V1_Recommended_Enforced\{uid}.cip`

更新脚本中的以下行以在本地使用您需要的策略：

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

Alternatively, you may use [Group Policy](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-windows-defender-application-control-policies-using-group-policy) or [Microsoft Intune](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-windows-defender-application-control-policies-using-intune) to enforce the WDAC policies.

## Auditing:

You can view the WDAC event logs in event viewer under:

`Applications and Services Logs\Microsoft\Windows\CodeIntegrity\Operational`

## Recommended Reading:

- [Argonsys - Deploying Windows 10 Application Control Policy](https://argonsys.com/microsoft-cloud/library/deploying-windows-10-application-control-policy/)
- [Microsoft - Audit Windows Defender Application Control Policies](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/audit-windows-defender-application-control-policies)
- [Microsoft - Create a WDAC policy for fixed-workload devices using a reference computer](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/create-initial-default-policy)
- [Microsoft - Deploy Windows Defender Application Control policies by using Group Policy](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-windows-defender-application-control-policies-using-group-policy)
- [Microsoft - Deploy Windows Defender Application Control policies by using Microsoft Intune](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-windows-defender-application-control-policies-using-intune)
- [Microsoft - Deploy WDAC policies using script](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deployment/deploy-wdac-policies-with-script)
- [Microsoft - Enforce Windows Defencer Application Control Policies](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/enforce-windows-defender-application-control-policies)
- [Microsoft - Guidance on Creating WDAC Deny Policies](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/create-wdac-deny-policy)
- [Microsoft - Use multiple Windows Defender Application Control Policies](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-multiple-windows-defender-application-control-policies)

## How to run the script:

### Manual Install:

If manually downloaded, the script must be launched from an administrative powershell in the directory containing all the files from the [GitHub Repository](https://github.com/simeononsecurity/Windows-Defender-Application-Control-Hardening/archive/main.zip)

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
Get-ChildItem -Recurse *.ps1 | Unblock-File
.\sos-wdachardening.ps1
```
