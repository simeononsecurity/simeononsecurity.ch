---
title: "使用 Microsoft Defender for Cloud 保护云环境"
date: 2023-04-10
lastmod: 2026-11-20
toc: true
draft: false
description: "使用 Microsoft Defender for Cloud 保护 Azure 工作负载。了解 Azure Security Center 的旧称、建议、策略和响应步骤。"
tags: ["Azure", "Security Center", "云安全", "Azure Sentinel", "Azure Defender", "网络安全", "身份管理", "数据安全", "威胁检测", "威胁响应", "MFA", "RBAC", "NSGs", "Azure Firewall", "WAF", "Azure AD", "Azure Information Protection", "Azure Storage Service Encryption", "Azure Disk Encryption"]
cover: "/img/cover/A_shield_icon_surrounded_by_cloud_symbols.webp"
coverAlt: "云朵符号环绕的盾牌代表安全的云环境。盾牌上有 Azure Security Center 标志。"
coverCaption: ""
---

**如何使用 Azure Security Center 保护云环境**

保护云环境有助于防止组织的数据、应用和基础设施受到威胁。Microsoft 的 **Azure Security Center** 可帮助你改善安全状况，并快速识别 Azure 环境中的潜在风险。本文介绍如何使用 Azure Security Center 保护云环境，并提供实施各种安全功能的实践建议。文中还包含技术细节和示例，便于你采取相应措施。

*本文最初发布后，产品名称有所变化。Microsoft Azure Security Center 现称为 Microsoft Defender for Cloud。Azure Active Directory 现称为 Microsoft Entra ID。Azure Sentinel 现称为 Microsoft Sentinel。Azure Defender 指 Defender 计划和 Defender for Cloud 中的工作负载保护。下文在描述 2023 年术语时保留旧名称。*

当前的 [Defender for Cloud 概述](https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-cloud-introduction)将其描述为云原生应用保护平台，涵盖云安全状况管理、DevSecOps 和云工作负载保护。功能可用性和许可取决于云、资源类型、订阅和计划。

______

## 了解 Azure Security Center

Azure Security Center 是**统一的基础设施安全管理系统**。它可帮助你识别并处理云环境中的潜在漏洞。其功能包括威胁检测、安全状况管理和合规管理。

**持续安全评估**和**高级威胁防护**是 Azure Security Center 的两项重要功能。持续安全评估用于发现环境中的潜在安全问题。高级威胁防护有助于检测和应对潜在威胁。

______

## 实施安全策略和合规标准

Azure Security Center 支持在整个云环境中实施和管理安全策略。你可以使用 **Azure Policy** 服务创建自定义策略，也可以使用内置策略来执行最佳实践和合规标准。还可以对照 [NIST 800-53](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final)、[CIS](https://www.cisecurity.org/) 和 [ISO 27001](https://www.iso.org/isoiec-27001-information-security.html) 等行业标准评估安全状况。

Azure Security Center 还提供合规管理功能，帮助你跟踪组织对各类法规框架的符合情况，例如 [GDPR](https://gdpr.eu/)、[HIPAA](https://www.hhs.gov/hipaa/index.html) 和 [PCI DSS](https://www.pcisecuritystandards.org/)。

______

## 保护 Azure 资源

**维护资源安全状态**是保护云环境的重要环节。Azure Security Center 提供 **Secure Score**，用于衡量资源的整体安全状况。按照 Azure Security Center 提供的建议修复问题，可提高此分数。

### 网络安全

**Network Security Groups (NSGs)**、**Azure Firewall** 和 **Web Application Firewall (WAF)** 等措施有助于保护 Azure 环境。它们控制入站和出站网络流量，降低未经授权访问和攻击的风险。

#### Network Security Groups (NSGs)

NSG 可充当 Azure 资源的虚拟防火墙。你可以定义规则，允许或拒绝进出资源的网络流量。以下示例创建 NSG 并设置流量规则：

```azurecli
# 创建 Network Security Group
az network nsg create --name MyNSG --resource-group MyResourceGroup

# 添加允许或拒绝流量的规则
az network nsg rule create --name MyNSGRule --nsg-name MyNSG --priority 100 --resource-group MyResourceGroup --access Allow --protocol Tcp --direction Inbound --source-address-prefixes '*' --source-port-ranges '*' --destination-address-prefixes '*' --destination-port-ranges '80'
```
请参阅官方文档中的 [Network Security Groups](https://docs.microsoft.com/en-us/azure/virtual-network/security-overview)。

以上示例允许来自任意 IPv4 源的入站 TCP 80 端口流量。生产环境应使用已知的源地址范围、专用终结点或负载均衡器路径。复制示例前，请阅读最新的 [NSG 安全概述](https://learn.microsoft.com/en-us/azure/virtual-network/network-security-groups-overview)。

#### Azure Firewall

Azure Firewall 是一种托管式云网络安全服务，可保护 Azure 资源。其功能包括基于威胁情报的筛选、网站类别以及集中式日志记录和分析。设置 Azure Firewall 时，请遵循[快速入门说明](https://learn.microsoft.com/en-us/azure/firewall-manager/quick-firewall-policy-bicep)。

#### Web Application Firewall (WAF)

Web Application Firewall (WAF) 是 **Azure Application Gateway** 的一项功能，可保护 Web 应用免受 SQL 注入、跨站脚本等常见 Web 攻击。你可以将 WAF 集成到现有 Web 应用，并配置自定义规则来防范特定攻击模式。

以下示例创建启用了 WAF 的 Application Gateway：

```azurecli
# 创建 WAF 策略
az network application-gateway waf-policy create --name MyWafPolicy --resource-group MyResourceGroup --location EastUS

# 创建虚拟网络和子网
az network vnet create --name MyVNet --resource-group MyResourceGroup --location EastUS --address-prefix 10.0.0.0/16
az network vnet subnet create --name MySubnet --resource-group MyResourceGroup --vnet-name MyVNet --address-prefix 10.0.0.0/24

# 创建公共 IP 地址
az network public-ip create --name MyPublicIP --resource-group MyResourceGroup --location EastUS --sku Standard

# 创建启用了 WAF 的 Application Gateway
az network application-gateway create --name MyAppGateway --resource-group MyResourceGroup --location EastUS --vnet-name MyVNet --subnet MySubnet --public-ip-address MyPublicIP --http-settings-cookie-based-affinity Enabled --sku WAF_v2 --waf-policy MyWafPolicy

```
请参阅官方文档中的 [Web Application Firewall](https://docs.microsoft.com/en-us/azure/web-application-firewall/ag/ag-overview)。

### 身份和访问管理

**Microsoft Entra ID**（以前称为 Azure Active Directory，简称 Azure AD）是保护云环境的重要组成部分。Defender for Cloud 会提供身份和访问管理建议，例如启用 **多因素身份验证（MFA）**、实施 **基于角色的访问控制（RBAC）** 并监控可疑活动。

#### 多因素身份验证（MFA）

MFA 要求用户在获得访问权限前通过两种或更多方式验证身份，为 Azure AD 帐户增加一道安全保护。若要在组织中启用 MFA，请遵循 Microsoft 提供的[分步指南](https://docs.microsoft.com/en-us/azure/active-directory/authentication/tutorial-enable-azure-mfa)。

示例：为用户启用 MFA

```powershell
# 连接到 Azure AD
Connect-AzureAD

# 为指定用户启用 MFA
$UserPrincipalName = "johndoe@example.com"
$StsUserObjectID = (Get-AzureADUser -Filter "UserPrincipalName eq '$UserPrincipalName'").ObjectId
$StrongAuthRequirements = @(@{"Location"=""; "SatisfactionFactor"="2"; "VerificationMethod"="1"};@{"Location"=""; "SatisfactionFactor"="2"; "VerificationMethod"="2"})
Set-AzureADUser -ObjectId $StsUserObjectID -StrongAuthenticationRequirements $StrongAuthRequirements
```
#### Role-Based Access Control (RBAC)

RBAC 支持为 Azure 资源设置细粒度权限，确保用户获得适当的访问级别。你可以为用户、组或应用分配角色，以管理其对组织资源的访问权限。若要实施 RBAC，请遵循 Microsoft 的[官方指南](https://docs.microsoft.com/en-us/azure/role-based-access-control/overview)。

示例：为用户分配角色

```azurecli
# 为用户分配 Reader 角色
az role assignment create --assignee johndoe@example.com --role "Reader" --scope "/subscriptions/your_subscription_id/resourceGroups/your_resource_group"
```
#### 监控可疑活动

Azure AD 提供 **Identity Protection** 和 **Conditional Access**，帮助你监控并应对可疑活动。Identity Protection 使用机器学习检测异常和高风险登录尝试。Conditional Access 可根据设备、位置和风险等因素设置访问控制策略。

若要设置 Azure AD Identity Protection，请遵循 Microsoft 的[官方指南](https://learn.microsoft.com/en-us/azure/active-directory/identity-protection/concept-identity-protection-b2b)。

示例：创建 Conditional Access 策略

```powershell
# 连接到 Azure AD
Connect-AzureAD

# 创建 Conditional Access 策略
$PolicyName = "BlockSignInFromUnknownLocations"
$PolicyDescription = "阻止用户从未知位置登录。"
$PolicyState = "Enabled"
$Conditions = @{
    "SignInRiskLevels" = @("medium","high");
    "Locations" = @{
        "Included" = @();
        "Excluded" = @("AllTrusted")
    }
}
$GrantControls = @{
    "Operator" = "OR";
    "BuiltInControls" = @("Block")
}
New-AzureADMSConditionalAccessPolicy -DisplayName $PolicyName -State $PolicyState -Conditions $Conditions -GrantControls $GrantControls -Description $PolicyDescription

```
请参阅官方文档中的 [Azure AD Identity Protection](https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/overview) 和 [Conditional Access](https://learn.microsoft.com/en-us/azure/active-directory/conditional-access/overview)。

### 数据安全

保护云中的数据至关重要。Azure Security Center 提供 **Azure Information Protection**、**Azure Storage Service Encryption** 和 **Azure Disk Encryption** 等功能，可帮助你加密数据并管理数据访问权限。

#### Azure Information Protection

**Azure Information Protection (AIP)** 是一项云服务，可用于分类、标记和保护敏感文档与电子邮件。AIP 提供“机密”和“个人”等内置标签，可按组织需求自定义。你还可以根据预定义规则配置自动标记。开始使用时，请遵循[官方指南](https://docs.microsoft.com/en-us/azure/information-protection/what-is-information-protection)。

示例：创建自定义标签

```powershell
# 连接到 AIP 服务
Connect-AipService

# 创建包含保护设置的自定义标签
$LabelName = "敏感 - 仅供内部使用"
$LabelDescription = "此标签仅对内部使用应用加密和访问策略。"
$LabelProtectionSettings = @{
    "ContentExpirationDate" = (Get-Date).AddMonths(6).ToUniversalTime();
    "OfflineAccessInterval" = "P7D";
    "UserRights" = @("domain\GroupA=View", "domain\GroupB=View,Edit,Print")
}
New-AipServiceLabel -Name $LabelName -Description $LabelDescription -ProtectionSettings $LabelProtectionSettings
```
#### Azure Storage Service Encryption

**Azure Storage Service Encryption (SSE)** 会自动加密 Azure Storage 帐户中的静态数据，包括 Blob、File、Table 和 Queue 存储。SSE 使用 Azure 管理的密钥或客户管理的密钥，在存储帐户级别提供加密。若要启用 SSE，请遵循 Microsoft 的[分步指南](https://docs.microsoft.com/en-us/azure/storage/common/storage-service-encryption)。

Azure Information Protection 是旧产品名称。Microsoft 当前关于 Sentinel 功能可用性的文档已将其列为弃用产品。开始新的标签部署前，请查阅当前的 Microsoft Purview Information Protection 文档。

示例：为存储帐户启用 SSE

```azurecli
# 使用 Azure 管理的密钥启用 SSE
az storage account update --name mystorageaccount --resource-group myresourcegroup --encryption-services blob file
```
#### Azure Disk Encryption

**Azure Disk Encryption** 使用 BitLocker (Windows) 或 dm-crypt (Linux) 加密虚拟机磁盘。Azure Key Vault 保护加密密钥和机密信息。若要启用 Azure Disk Encryption，请遵循 Microsoft 的[官方指南](https://learn.microsoft.com/en-us/azure/virtual-machines/disk-encryption-overview)。

示例：为虚拟机启用 Azure Disk Encryption

```azurecli
# 为 Windows VM 启用 Azure Disk Encryption
az vm encryption enable --resource-group myResourceGroup --name myVM --disk-encryption-keyvault myKeyVault
```
请参阅官方文档：[Azure Information Protection](https://docs.microsoft.com/en-us/azure/information-protection/what-is-information-protection)、[Azure Storage Service Encryption](https://docs.microsoft.com/en-us/azure/storage/common/storage-service-encryption) 和 [Azure Disk Encryption](https://learn.microsoft.com/en-us/azure/virtual-machines/disk-encryption-overview)。
______

## 检测和响应威胁

Azure Security Center 使用高级威胁检测功能识别潜在威胁并发出警报。与 **Azure Sentinel** 集成后，你可以监控、调查和响应整个环境中的安全事件。

### 威胁检测

Azure Security Center 使用 **Azure Defender** 识别潜在安全威胁。Azure Defender 会监控资源中的入侵迹象，并提供警报和建议，帮助你进行响应。若要启用 Azure Defender，请遵循[官方指南](https://docs.microsoft.com/en-us/azure/security-center/defender-for-cloud-enable)。

示例：为订阅启用 Azure Defender

```azurecli
# 为订阅启用 Azure Defender
az security auto-provisioning-setting update --name default --auto-provision on
```
### 威胁响应
检测到威胁后，应迅速采取有效措施。Azure Security Center 的 **Security Incident** 管理功能可帮助你调查并响应安全事件。你还可以集成 **Azure Sentinel**，创建自动化 playbook 并协调事件响应。有关 Azure Security Center 与 Azure Sentinel 的集成，请参阅**官方文档**。

示例：为 Azure Sentinel 创建 Logic App 响应流程
```azurecli
# 创建资源组
az group create --name MyResourceGroup --location EastUS

# 创建 Logic App
az logic workflow create --resource-group MyResourceGroup --location EastUS --name MyPlaybook --definition @playbook-definition.json
```
`playbook-definition.json` 文件应包含 Logic App 响应流程定义。你可以在 [Azure-Sentinel GitHub 存储库](https://github.com/Azure/Azure-Sentinel/tree/master/Playbooks)中查看 Azure Sentinel 响应流程示例。

将 Azure Security Center 的威胁检测与 Azure Sentinel 集成，可帮助你制定 Azure 环境中的威胁检测与响应策略。请参阅 [Azure Defender](https://learn.microsoft.com/en-us/azure/defender-for-cloud/enable-enhanced-security) 和 [Azure Sentinel](https://docs.microsoft.com/en-us/azure/sentinel/overview) 的官方文档。

当前集成方式通过 [Defender for Cloud 连接器](https://learn.microsoft.com/en-us/azure/sentinel/connect-defender-for-cloud)将 Defender for Cloud 警报发送到 Microsoft Sentinel。依赖自动化前，请在 Defender 门户或 Azure 门户中验证连接器、数据收集规则、分析规则和事件工作流。
______

## 监控和报告

监控和报告有助于维护安全的云环境。Azure Security Center 提供 **安全仪表板**、**安全警报**和**合规报告**等工具。

### 安全仪表板

Azure Security Center 的 Security Dashboard 展示整体安全状况，包括 Secure Score、安全建议和活动警报。仪表板还会显示合规状态，并可用于跟踪进展。

### 安全警报

检测到潜在威胁时，Azure Security Center 会生成安全警报。警报包含威胁详情和降低风险的建议。你可以通过电子邮件或短信接收通知，也可以将 Azure Security Center 与 [Slack](https://slack.com/) 或 [Microsoft Teams](https://www.microsoft.com/en-us/microsoft-teams/group-chat-software) 等工具集成。

### 合规报告

Azure Security Center 可针对 GDPR、HIPAA 和 PCI DSS 等法规框架生成合规报告。使用这些报告跟踪组织的合规状态，并找出需要改进的方面。

______

## Azure Security Center 的最佳实践

如需充分利用 Azure Security Center，请采用以下做法：

1. **为所有订阅启用 Azure Security Center**：确认所有 Azure 订阅均受到保护。
2. **定期检查 Secure Score**：了解整体安全状况并找出需要改进的方面。
3. **落实安全建议**：按照 Azure Security Center 的建议改善安全状况并降低潜在风险。
4. **监控安全警报**：定期查看警报并采取措施，降低潜在威胁。
5. **及时更新合规要求**：定期检查并更新合规策略，以满足当前法规框架的要求。

## 当前的 Defender for Cloud 工作流程

当前部署可按以下顺序进行。前文的旧名称仍有助于查找历史资料，但门户和文档使用 Defender for Cloud 术语。

1. **盘点订阅和连接器。** 记录 Azure 订阅、AWS 或 GCP 连接器、DevOps 项目和关键资源。
2. **启用所需的 Defender 计划。** 按工作负载选择计划，并在生产订阅中启用前确认许可。
3. **检查 Cloud Secure Score 和建议。** 优先处理互联网暴露、身份风险、可利用漏洞和日志缺失问题。分数不代表完全符合要求。
4. **配置 Microsoft Entra 控制。** 对重要帐户要求使用抗钓鱼 MFA，采用最小权限 RBAC，并检查特权访问。
5. **将警报发送到 Microsoft Sentinel。** 确认警报接收、分析规则、责任人、响应自动化和保留期限。
6. **变更后重新检查。** 应用补丁、调整架构、添加连接器或变更计划后，重新查看建议。

## 实用检查清单

- **身份：** 删除过期帐户，减少长期管理员权限，并检查 Conditional Access 例外。
- **网络：** 关闭公开的管理端口，收紧 NSG 源地址范围，并确认防火墙和 WAF 日志已发送到监控工作区。
- **数据：** 对敏感数据存储分类，确认加密和密钥所有权，并测试备份恢复。
- **检测：** 确认警报级别、通知路由、事件责任人和响应 playbook。
- **治理：** 为每项策略计划指定负责人和例外到期日期，并保存所需标准的证据。

______

## 参考资料

- [Azure Security Center 文档](https://docs.microsoft.com/en-us/azure/security-center/)
- [Azure Policy 服务](https://docs.microsoft.com/en-us/azure/governance/policy/)
- [NIST 800-53](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final)
- [CIS](https://www.cisecurity.org/)
- [ISO 27001](https://www.iso.org/isoiec-27001-information-security.html)
- [GDPR](https://gdpr.eu/)
- [HIPAA](https://www.hhs.gov/hipaa/index.html)
- [PCI DSS](https://www.pcisecuritystandards.org/)
