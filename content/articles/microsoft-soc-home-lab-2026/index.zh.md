---
title: "Microsoft SOC 家庭实验室：在 2026 年积累网络安全经验"
date: 2026-09-11
lastmod: 2026-11-27
toc: true
draft: false
description: "使用 Sentinel、Defender、Intune 和 Entra 搭建 Microsoft SOC 家庭实验室。练习事件调查、验证通行密钥策略，并记录作品集证据。"
genre: ["网络安全", "云安全", "职业发展"]
tags: ["SOC 家庭实验室", "Microsoft Sentinel", "Microsoft Defender XDR", "Defender for Endpoint", "Defender for Cloud", "Defender for Servers", "Microsoft Intune", "Microsoft Entra ID", "Azure 家庭实验室", "网络安全经验", "SOC 分析师", "安全运营中心", "事件响应", "KQL", "Log Analytics", "Conditional Access (条件访问)", "抗钓鱼 MFA", "通行密钥", "身份安全", "网络安全作品集", "云成本管理", "端点安全"]
cover: "/img/cover/microsoft-soc-home-lab.webp"
coverAlt: "家中桌上的笔记本电脑显示安全事件时间线，上方的云中包含服务器和端点。"
coverCaption: ""
---

**安全运营中心（SOC）家庭实验室**为你提供调查警报、说明证据和测试防御变更的环境。搭建小型 Microsoft 环境，收集遥测数据，并记录每次调查。目标是形成有证据支持、可重复的调查过程。

本指南扩展了 Mad Hat 网络安全职业视频和所提供的 Cyber Range 操作手册中的实验室方案。产品要求以 Microsoft 文档为依据，并将配置、检测和验证拆分为可衡量的任务。

## 要点

- **从小规模开始：** 一台受管理的 Windows 客户端和一个测试身份即可支持初期练习。
- **验证遥测：** 设备可见或门户已连接，都不能证明日志正在到达。
- **完成调查：** 记录触发原因、证据、响应和复测结果。
- **控制支出：** 分别跟踪许可证、保留数据、网络和计算资源。
- **准确描述经验：** 在简历中将环境列为实验室项目。

## 开始之前

**前置知识：** 具备基础 Windows 管理和网络知识，并熟悉虚拟机。使用专用的 Microsoft Entra 租户和仅供实验室使用的 Azure 订阅。不要在练习中使用生产身份、个人文件或雇主系统。

**预计投入：** 初次配置预留一个周末，之后安排有针对性的调查时段。这只是规划估算。试用审批、配额和服务配置时间都会影响实际耗时。**难度：** 中级。

准备独立的管理员账户和无特权测试用户。测试访问策略之前，先建立并验证紧急访问方式。每项配置任务仅分配所需权限，日常调查使用权限较低的账户。

| 组件 | 实验室用途 |
|---|---|
| **Sentinel** | 为已连接的日志源提供安全信息和事件管理（SIEM） |
| **Defender XDR** | 关联并调查已获许可的 Microsoft 安全服务中的活动 |
| **Defender for Endpoint** (终端保护) | 对已接入设备进行端点检测与响应（EDR） |
| **Intune** | 设备注册和端点安全策略管理 |
| **Entra ID** | 身份、登录记录和访问策略评估 |
| **Defender for Servers** (服务器保护) | 通过 Defender for Cloud 保护服务器 |

## 先检查许可证

**Microsoft 365 E5**是搭建综合实验室的一种方式，但访问能力取决于分配给参与用户的服务计划和许可证。Office 365 E5 与 Microsoft 365 E5 是不同的套餐。管理员拥有许可证，并不代表每个测试用户或工作负载都已覆盖。选择订阅前，请查看[Defender XDR 前置要求](https://learn.microsoft.com/en-us/defender-xdr/prerequisites)。

**Defender 门户中的 Sentinel**无需 E5 或 Defender XDR 即可运行。添加 XDR 后会引入独立的许可和配置要求。事件列表为空，并不能证明缺少 E5 许可证。Microsoft 的[Sentinel 接入文档](https://learn.microsoft.com/en-us/unified-secops/microsoft-sentinel-onboard)介绍了两种配置。

**服务器保护**有单独的许可路径。对于受支持的服务器工作负载，Defender for Servers 会与 Defender for Endpoint 集成。Windows 客户端操作系统需要适当的客户端覆盖。不要认为每台 Azure VM 都自动取得服务器许可证。请参阅 Microsoft 的[Defender for Endpoint 集成文档](https://learn.microsoft.com/en-us/azure/defender-for-cloud/integration-defender-for-endpoint)。

**试用规划：** 在自己的账户中确认资格、到期时间、续订设置和所含服务。不要根据视频承诺的试用期限或固定月费制定预算。

## 制定支出计划

**Azure 预算**会发送通知，但达到阈值后不会停止资源消耗。成本报告也有延迟。尽早创建警报，并在每次实验后检查支出，参考 Microsoft 的[预算设置指南](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/tutorial-acm-create-budgets)。

| 成本类别 | 规划问题 |
|---|---|
| **用户许可证** | 哪些用户需要哪些服务计划，试用何时到期？ |
| **计算资源** | 每项练习需要多少 VM 小时？ |
| **存储** | 关机后会留下哪些磁盘和快照？ |
| **日志收集** | 哪些表需要引入，数据应保留多久？ |
| **网络** | 设计是否包含付费 Bastion、公网 IP 或出站服务？ |
| **服务器保护** | 哪些工作负载启用了付费 Defender 计划？ |

**设计选择：** 从一台客户端开始。只有在练习需要服务器遥测时才添加服务器。四台客户端和多台服务器会先增加管理工作和成本，未必能提升调查练习的价值。

## 构建网络

**建议布局：** 将 Azure 资源放入名称清晰的资源组，例如 **`rg-soc-lab`**。将客户端和服务器放入不同子网，明确设置网络安全组规则，并使用私有管理访问。仅靠子网隔离无法阻止工作负载之间的流量。

部署专用的 **Azure Bastion** 时，请遵循 SKU 要求。当前部署需要使用保留名称 **`AzureBastionSubnet`**，并配置 **`/26`** 或更大的子网。Developer SKU 使用不同的部署模式。选择设计前，请查看 [Bastion 配置设置](https://learn.microsoft.com/en-us/azure/bastion/configuration-settings)。

不要将 RDP 和 SSH 暴露到公网。将管理流量限制在选定的管理路径内。允许注册和安全遥测所需的出站连接。

**验证：** 安装工作负载前，建立私有管理访问并检查生效的网络规则。如果之后添加故意存在漏洞的应用，将它留在练习网络内，并把访问限制在测试设备。

## 连接 Sentinel 和日志

**门户配置：** 创建 Log Analytics 工作区并启用 Sentinel。如果 Defender 门户中没有该工作区，请打开 **System > Settings > Microsoft Sentinel > Connect a workspace** (系统 > 设置 > Microsoft Sentinel > 连接工作区)。按照[接入前置要求](https://learn.microsoft.com/en-us/unified-secops/microsoft-sentinel-onboard)检查租户以及所需的 Azure 和 Entra 角色。

**日志收集是单独的步骤。** 在 Entra 中配置诊断设置，将所需活动类别发送到同一工作区。先从交互式登录和审核事件开始。[Entra 日志集成指南](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/howto-integrate-activity-logs-with-azure-monitor-logs)说明了权限和目标位置。

当前 Sentinel 工作流也支持通过 Microsoft Defender 门户连接。排查空表之前，确认所选工作区是预期的主工作区、租户与测试身份一致，并且账户具有所需角色。门户中可见并不能证明数据已引入。[在 Defender 门户中接入 Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/microsoft-sentinel-onboard)

```kusto
SigninLogs
| where TimeGenerated > ago(24h)
| where UserPrincipalName =~ "soc-test@YOUR-TENANT.onmicrosoft.com"
| project TimeGenerated, UserPrincipalName, AppDisplayName,
          IPAddress, ResultType, ConditionalAccessStatus, CorrelationId
| order by TimeGenerated desc
```

生成新的测试登录后，在工作区的 Logs 视图中运行此 **Kusto Query Language (KQL)** 示例。将示例用户主体名称替换为实验室用户。列名遵循 [SigninLogs 表架构](https://learn.microsoft.com/en-us/azure/azure-monitor/reference/tables/signinlogs)。

**预期结果：** 出现与测试账户和登录时间相符的行。如果没有行，检查时间范围、身份、收集设置、目标位置和引入延迟。表缺失时，应先排查收集或工作区问题，再考虑检测问题。

## 接入第一台端点

**Intune 注册和 EDR 接入**是两个独立检查点。连接 Intune 和 Defender for Endpoint，注册受支持的 Windows 客户端，然后向实验室设备组分配端点检测与响应接入策略。仅在 Entra 中注册并不能证明任何一个检查点已完成。

在 Intune 中查看 **Endpoint security > Defender for Endpoint** (终结点安全 > Defender for Endpoint)。如果无法连接，请在 Defender 的端点高级功能中启用 Intune 连接。按照 Microsoft 的 [Intune 与 Defender 集成指南](https://learn.microsoft.com/en-us/intune/device-security/microsoft-defender/configure-integration)完成对应平台的步骤。

| 检查点 | 要收集的证据 |
|---|---|
| **注册** | 客户端显示在 Intune 中，且最近有签到记录 |
| **策略分配** | 接入策略已应用于目标设备组 |
| **传感器报告** | Defender 显示已接入状态和近期遥测 |
| **检测测试** | 有文档记录的测试产生预期安全信号 |

**服务器方面，**启用选定的 Defender for Servers 计划及其端点集成，然后确认传感器已部署并报告。Defender for Cloud 会在接入完成前发现机器。仅出现在资产清单中并不足够。请参阅 Microsoft 的[资源发现和接入指南](https://learn.microsoft.com/en-us/azure/defender-for-cloud/integration-defender-for-endpoint)。

## 调查测试警报

先在实验室端点上运行 **Microsoft 有文档记录的 EDR 检测测试**。按照[当前测试说明](https://learn.microsoft.com/en-us/defender-endpoint/edr-detection)操作，包括平台前置要求和故障排查。打开警报队列前先记录执行时间。

把生成的警报作为调查练习。安全产品给出的标题只是起点。你需要查明发生了什么，并用证据支持处置结论。

1. **初步分类：** 确认警报来源、设备、账户和事件时间。
2. **检查：** 查看进程树、命令行、文件详情和可用的网络活动。
3. **确定范围：** 搜索测试身份和其他实验室设备上的相关活动。
4. **评估：** 说明证据是否符合计划中的练习，或属于无关事件。
5. **响应：** 记录所选响应、影响和恢复步骤。只有练习要求时才执行受支持的隔离。
6. **复测：** 更改控制后重复相关测试并比较证据。

**不要编造缺失的结果。** 如果警报没有到达，保留执行记录并排查收集问题。如果控制在预期事件发生前阻止了测试，记录预防结果。

## 测试身份控制

**中间人攻击式钓鱼（AiTM）**会在登录流程中加入由攻击者控制的中间方。提供的操作手册以此场景说明加强身份验证的必要性。首次身份练习应使用你自己的无特权账户，直接测试策略行为。

先记录一次正常登录及其身份验证详情。解释风险信号前，请查看 Microsoft 的 [Entra 风险检测参考](https://learn.microsoft.com/en-us/entra/id-protection/concept-identity-protection-risks)。不同信号的检测前置条件和处理方式各不相同。新的 IP 地址或登录失败都不保证触发 AiTM 警报。

**通行密钥（FIDO2）**使用绑定到合法服务的凭据，而不是在中继登录页中输入的可重复使用代码。为试点组启用适当的通行密钥配置，并在强制策略前注册此方法。支持的验证器和限制见[通行密钥配置指南](https://learn.microsoft.com/en-us/entra/identity/authentication/how-to-authentication-passkeys-fido2)。

**Conditional Access (条件访问) 练习：** 创建只针对实验室试点组的策略，排除紧急访问账户，然后选择 **Require authentication strength > Phishing-resistant MFA strength** (要求身份验证强度 > 抗网络钓鱼的 MFA 强度)。先使用 **Report-only (仅报告)** 模式并检查影响，再启用策略。这是将 Microsoft 的[管理员策略示例](https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-admin-phish-resistant-mfa)调整为小范围测试组。

| 测试 | 要收集的证据 |
|---|---|
| **Report-only (仅报告) 策略** | 显示建议策略评估结果的登录记录 |
| **强制策略，较弱方法** | 新身份验证要求在允许访问前使用更强的方法 |
| **强制策略，已注册通行密钥** | 满足所需强度的成功登录 |

每次比较都使用新的身份验证，并检查策略详情。现有会话会使比较变得复杂。**证据范围：** 此练习验证身份验证要求，不代表对端点失陷或现有会话被盗等情况提供全面保护。

## 编写作品集证据

**有价值的作品集条目**应说明一项决定，使其他分析人员能够复核。加入简短的架构说明、数据收集前置条件、事件时间线以及响应理由。

```text
练习：
日期和 UTC 时间范围：
实验室范围和前置条件：
触发条件和预期信号：
观察到的警报或预防结果：
证据和查询：
受影响的身份和设备：
结论和理由：
响应和恢复：
控制变更和复测：
限制和后续事项：
```

每个字段都填写自己的观察结果。发布截图或查询结果前，**清理导出内容：** 删除凭据、会话资料、个人信息和不必要的标识符。

**简历示例：**“搭建 Microsoft 安全实验室，将身份日志连接到 Sentinel，调查端点测试警报，并记录 Conditional Access (条件访问) 验证结果。”只有完成这些任务后才使用此描述。将其放在项目或实践培训部分，并标注真实日期和范围。

实验室能够证明自主练习。**生产环境中的 SOC 工作**还涉及业务影响、升级处理、服务承诺以及与其他团队协调。说明你练习了哪些内容，哪些内容超出了实际经验。

## 故障排查

| 症状 | 首先检查 |
|---|---|
| **Defender 中没有工作区** | 是否为同一租户、Sentinel 是否启用、是否满足接入角色要求 |
| **SigninLogs 缺失或为空** | 诊断类别、目标工作区、新事件和时间范围 |
| **Intune 中没有客户端** | 注册前置要求和注册状态 |
| **设备可见但没有遥测** | 实际接入状态、传感器运行状况和出站连接 |
| **接入策略未应用** | 分配范围、设备平台和最近签到时间 |
| **没有身份风险警报** | 信号前置要求和已记录的活动，不要假设检测必然发生 |
| **意外允许访问** | Report-only (仅报告) 状态、排除项、资源范围和现有会话 |
| **关机后仍产生费用** | 资源分配状态以及计算资源以外的计费项目 |

**故障排查顺序：** 先证明事件发生，再确认数据收集有效，最后调查检测逻辑。在项目记录中写下每次故障和修复。

## 暂停或删除实验室

**取消分配**会释放 VM 计算资源。仅关闭来宾操作系统不保证资源已取消分配。查看 Azure 显示的电源状态，并参阅 Microsoft 的 [VM 状态和计费文档](https://learn.microsoft.com/en-us/azure/virtual-machines/states-billing)。

**保留的资源**也需要检查。磁盘、快照、网络服务、日志保留和用户订阅都有独立的生命周期。每个试用到期前设置提醒，清理后再检查下一份使用报告。

删除实验室资源组之前，先导出计划保留的证据并检查内容。**删除资源组会破坏其中的资源。** 租户用户、Intune 策略、Conditional Access (条件访问) 策略、订阅和订阅级安全设置在适用时需要单独清理。

## 后续步骤

增加其他工作负载前，**先完成并记录一次调查**。然后添加服务器、身份练习或检测规则，并设定清晰的测试条件。记录新增组件带来的学习内容和成本。

使用[IT 家庭实验室指南](/it-career-playbook/getting-started-in-it/building-an-it-home-lab/)练习基础设施，用[IT 简历指南](/it-career-playbook/getting-a-job-in-it/it-resume-writing-tips/)展示成果。下一个项目应保持足够小，便于说明配置、证据和清理过程。
