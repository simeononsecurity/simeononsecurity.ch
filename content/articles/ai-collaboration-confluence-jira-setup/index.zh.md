---
title: "Confluence 与 Jira AI 设置：权限与职责"
date: 2026-10-01
lastmod: 2026-11-08
toc: true
draft: false
description: "配置 Confluence 正式依据页面和公司管理的 Jira 权限，以支持经过审查的跨团队协作。"
genre: ["人工智能", "团队协作", "软件工程"]
tags: ["AI 协作课程", "Confluence Cloud", "Jira Cloud", "正式依据页面", "Jira 权限方案", "工作流转换", "访问测试"]
cover: "/img/cover/A_group_of_diverse_professionals_collaborating_on_a_cyberse.webp"
coverAlt: "插画展示专业人员在网络安全工作环境中审查共享项目工作"
coverCaption: ""
---

[返回 AI 协作课程](/ai-collaboration-course-start/)

**管理员先设定工作场所的权限职责，再连接聊天工具。** 产品和运营负责人在 Confluence Cloud 中发布需求和运行手册。Jira Cloud 协调交付。GitHub 负责实现。基础搭建完成后，再创建专用沙箱，因为权限授予错误会泄露信息，与模型行为无关。

## 要点

- **Confluence** 保存已批准的需求措辞。
- **Jira** 管理交付状态，不管理保留策略。
- **GitHub** 管理配置和共享策略。
- **权限测试**需要合适的套餐和独立用户。

## 开始之前

**前提条件：**[基础课程](/articles/ai-collaboration-pilot-foundation/)、实验室仓库、Confluence 空间管理权限、Jira 管理权限，以及分别用于贡献者、负责人和发布者的独立用户。**预计用时：**90 至 120 分钟。**难度：**高级管理。

**套餐要求：**Confluence Free 不支持内容限制。Jira Free 缺少可配置的权限方案、空间角色和工作项安全方案。本步骤需使用 Standard 或更高套餐的合适沙箱。测试前，请根据参考资料确认实际套餐和权限。

**导航说明：**当前 Jira 文档使用“space”和“work item”。部分租户仍显示“project”和“issue”。请选择公司管理的配置。本流程不涵盖团队管理配置中的权限行为。无需使用 Rovo、Marketplace 应用、Jira Service Management 审批或付费聊天连接器。

**预期结果：**完成权限矩阵、命名的正式依据页面、仅供实验室使用的 Jira 工作流，以及由独立用户提供的拒绝访问证据。请在测试结果旁记录租户套餐和角色假设。

**创建记录前请检查：**

| 检查项 | 可用时 | 不可用时 |
|---|---|---|
| Confluence 页面限制和空间管理 | 分别创建已批准页面和排除页面 | 将页面编辑和拒绝读取测试标记为“已阻止” |
| 公司管理 Jira 权限方案和工作流编辑器 | 复制仅供实验室使用的方案和工作流 | 将转换测试标记为“已阻止” |
| 为贡献者、负责人、发布者和排除用户创建独立账户 | 按角色执行允许和拒绝测试 | 将未测试的角色标记为“已阻止” |
| 仓库维护者和受保护分支 | 链接经过审查的实现路径 | 混合发布前先完成 GitHub 优先路径 |

截至 2026 年 10 月，使用页面上的 **Share** 或限制控件管理页面访问；在 Confluence 的 **Space settings** 权限区域设置更广泛的授权；在 Jira 中打开 **Settings > Work items > Permission schemes** 配置实验室方案。公司管理 Jira 的工作流编辑器控制状态转换。不同租户的 UI 标签和套餐功能可能不同。执行这些步骤前，请在证据中记录实际路径和套餐。请参阅 [Confluence 页面级权限](https://support.atlassian.com/confluence-cloud/docs/manage-permissions-on-the-page-level/)和 [Jira 权限方案](https://support.atlassian.com/jira-cloud-administration/docs/manage-project-permissions/)。

## 创建正式依据页面

1. **创建一个名为 `Export Service Lab` 的 Confluence 空间。**通过可用的网站或空间控件关闭匿名访问和公开共享。
2. **创建已发布页面**，不要创建实时文档。页面名称为 **`REQ-17 Export Retention`**、**`RUN-04 Export Cleanup`** 和 **`Decision Register`**。
3. 以产品负责人的身份，**发布下面的初始需求。**在仓库映射中记录实际页面 ID 和版本。
4. 以运营负责人的身份，**发布 RUN-04**，注明七天保留期，并说明本实验室不会运行删除任务。
5. 在每个正式依据页面上**打开 Share**。对符合条件的空间成员设置只读访问，并单独授予指定负责人和发布者编辑权限。保存后，用贡献者账户验证。

```text
Source ID: REQ-17
Owner role: product-owner
Status: Approved baseline
Scope: synthetic export files only
Retention: 7 days
Delivery state: baseline lab configuration
Exceptions: production data, backups, and legal holds excluded
Approval evidence: DEC-12 baseline review
Implementation reference: attach protected GitHub baseline commit
```

**对每个正式依据页面设置限制。**不要假设父页面的编辑限制也会保护子页面。读取权限和编辑权限的继承方式不同，空间权限仍然适用。仅有链接不会授予访问权限。如果本应只读的用户仍能编辑，请检查所有成员身份。

**其他两个页面请使用以下起始正文。**将临时审核字段替换为沙箱中的实际证据，然后再批准记录。

```text
Source ID: RUN-04
Owner role: operations-owner
Status: Approved baseline
Scope: synthetic export files only
Configured retention: 7 days
Procedure: compare REQ-17 with config.json before a reviewed change
Runtime limit: this lab has no deletion job and produces no deletion evidence
Recovery: restore the prior approved configuration through review
Recovery limit: restoring configuration does not restore deleted files
Review evidence: add actual reviewer, page version, and decision reference
```

```text
Page: Decision Register
Entry ID: DEC-12
Decision: use seven days as the synthetic baseline
Scope: export-service-lab only
Requirement: REQ-17 page version, record after publication
Runbook: RUN-04 page version, record after publication
Policy: POL-01 protected GitHub revision, record after review
Product review: pending until the named owner records a decision
Operations review: pending until the named owner records a decision
Status: draft example, replace with observed review evidence
```

## 更新映射

```yaml
track: mixed-workplace
policy: {source_id: POL-01, home: GitHub, version: 1}
requirements: {source_id: REQ-17, home: Confluence, owner_role: product-owner}
runbook: {source_id: RUN-04, home: Confluence, owner_role: operations-owner}
decisions: {source_id: DEC-12, home: Confluence, owner_role: project-lead}
implementation: {home: GitHub, file: config.json}
delivery: {home: Jira, proposal_id: PROP-042}
snapshot_rule: repository requirement copies are not authoritative
```

**将沙箱的实际私有位置和页面 ID 添加到映射中。**模板标明了正式依据页面，不会假装包含真实地址。请删除 README 中将复制的 JSON 文件指定为混合路径需求权威来源的文字。

**两个路径都将 POL-01 保留在 GitHub 中。**Confluence 链接到经过审查的修订版。任务期间迁移策略权威来源，需要再次审查权限移交。

## 设置 Jira 权限

1. **创建公司管理的实验室空间**，并将权限方案复制到专用实验室方案。不要修改共享的生产方案。
2. **打开 Settings、Work items、Permission Schemes**，选择实验室方案并更新授权。
3. **授予贡献者浏览、创建和评论权限。**限制管理权限。明确检查编辑权限和 **Transition work items** 权限。
4. **将方案关联到实验室空间**，并确认没有生产空间共享该方案。
5. **创建 PROP-042 工作项。**在映射中记录生成的键，并在描述中保留 PROP-042 作为逻辑提案 ID。

**将此草案粘贴到 PROP-042。**Jira 工作项负责跟踪交付。其内容不能替代 Confluence 中已批准的措辞。

```text
Proposal ID: PROP-042
Status: Draft
Current approved value: 7 days, REQ-17 page version to record
Proposed value: 30 days for synthetic export files
Exclusions: production data, backups, legal holds
Affected records: REQ-17, RUN-04, config.json, proposal.json
Fixed proposal attachment: pending
Product-owner review: pending
Operations-owner review: pending
Publication ledger: pending
Stop on changed source version, missing review, or denied access
```

| 角色 | Confluence | Jira | GitHub |
|---|---|---|---|
| **贡献者** | 阅读已批准页面 | 创建草案并发表评论 | 提案分支或 Issue |
| **产品负责人** | 审查需求 | 记录需求审查 | 审查 PR 证据 |
| **运营负责人** | 审查运行手册 | 记录运营审查 | 审查运营影响 |
| **发布者** | 编辑已批准页面 | 记录发布状态 | 无自动合并权限 |
| **维护者** | 阅读需求 | 记录实现 | 审查并合并受保护的 PR |

**不同组授予的权限会累加。**请在实验室中移除意外的宽泛授权，不要假设较窄授权会覆盖较宽授权。不要将连接器身份加入管理组。

## 设置交付状态

**复制公司管理的工作流**，创建仅供实验室使用的工作流。添加“草稿”“审查”“已批准”“发布中”“已完成”和“已阻止”状态。添加提交、批准、发布、完成、阻止和退回审查的转换。仅将其关联到实验室工作类型。

1. 在工作流编辑器中**选择进入“已批准”的转换。**
2. **添加条件或限制**，将执行者限定为指定的负责人/发布者角色或组。使用文档说明的条件控件，并以管理员身份发布工作流草案。
3. 转换前**手动检查两位负责人的审查结果。**每份审查都要标明固定的提案和源版本。
4. **将“已完成”状态**限制给交付负责人。删除绕过此边界的替代或全局转换。

**受限转换不等于双人批准。**它只控制执行转换的人。在本试点中，两种角色的证据检查仍是流程步骤。请明确记录此限制。

**转换记录示例：**对于**审查到已批准**，仅允许指定的负责人/发布者组执行转换。执行前，操作者打开固定的 PROP-042 附件，核对同一提案修订版上的产品负责人和运营负责人决定。如果缺少任一决定，或决定引用较旧修订版，就让工作项留在“审查”状态并记录缺口。工作流限制控制操作者。证据检查是单独的人工步骤。

## 验证拒绝访问

**以贡献者身份**读取 REQ-17、尝试编辑、创建 Jira 草案，并尝试转换到“已批准”。预期结果是：需求可读、编辑被拒绝、提案创建成功、批准转换被拒绝。比较拒绝操作前后的源版本。

**以排除用户身份**打开单独限制的合成页面。预期无法访问内容。单独测试子页面。不要把受保护文本粘贴到排除用户的聊天中来绕过限制。

## 调整仓库映射

**源位置变化时，保持源 ID 不变。**REQ-17 仍代表已批准的保留意图，但在混合路径中，其来源是 Confluence 页面。仓库快照用于检查和审查，不能替代正式依据页面。

| 记录 | 权威来源 | 仓库中的处理方式 |
|---|---|---|
| **REQ-17** | 映射的 Confluence 需求页面 | 保存页面修订证据快照 |
| **RUN-04** | 映射的 Confluence 运行手册页面 | 保存操作摘要以保持一致 |
| **POL-01** | GitHub 中受保护的策略 | 共享代理说明引用此策略 |
| **配置** | GitHub 中受保护的记录 | 提议的实现差异 |
| **交付** | Jira 工作项 | 用于关联的链接，不是策略副本 |

**为快照添加来源信息。**在私有提案包中记录源 ID、页面引用、页面版本、采集时间和采集者角色。不要在公开课程提交中包含页面原生 ID。如果发布者发现不同的当前版本，请先协调差异，再使用快照。

**不要为了适配工具而重命名权威来源。**可编辑的 Jira 描述便于讨论，但它仍是交付记录。Jira 中的“三十天”说法不能取代 Confluence 中的“七天”要求。

## 设计访问测试

**将读取、起草和发布分开。**贡献者需要足够的权限来理解合成需求并提交提案，但不需要编辑正式依据页面，也不需要批准自己的提案。

```text
Test record: PERM-REQ-EDIT
Role: contributor
Source: REQ-17
Precondition: source is readable, published revision captured
Attempt: edit the authoritative requirement
Expected: edit denied, published revision unchanged
Observed: fill from the sandbox
Evidence: native result and independent revision read-back
Reviewer: administrator or independent permission reviewer
```

**使用单独记录测试拒绝读取。**贡献者能读取需求，测试的是发布与编辑的分离。排除用户无法访问页面，测试的是机密性。将两项合并到一行会掩盖实际测试的边界。

**也要测试允许的访问。**负责人和发布者必须能够使用分配给他们的路径。如果所有用户都被拒绝，沙箱虽有限制，却无法使用。请在一次性测试页面上保留成功的授权编辑证据，诊断权限时不要修改已批准需求。

## 演练 Jira 审查

**将状态名称视为本试点的设计。**“草稿”包含请求。“审查”包含固定的软件包。“已批准”表示负责人已完成审查。“发布中”表示交付尚未完成。“已完成”需要回读确认。“已阻止”表示缺少证据或访问权限，或存在未解决冲突。

| 转换 | 所需材料 | 责任检查 |
|---|---|---|
| **草稿到审查** | 固定提案和源版本 | 贡献者确认材料完整 |
| **审查到已批准** | 产品和运营决定 | 授权操作者检查两个角色 |
| **已批准到发布中** | 与当前来源进行比较 | 发布者确认基础版本未变 |
| **发布中到已完成** | 每个系统的完整记录 | 交付负责人检查回读结果 |
| **任何支持的步骤到已阻止** | 失败和待办事项 | 指定恢复负责人 |

**用不完整的合成材料进行演练。**只提交产品审查，并请有权执行转换的人评估。预期做法是让工作项停留在“审查”，并要求补充运营审查。这将程序审查与贡献者遭遇的平台拒绝分开测试。

**有意检查替代路径。**在沙箱工作流视图中检查所有通往“已批准”和“已完成”的路径。如果其他可用路径能绕过相同的审查边界，仅限制一个命名转换并不够。记录检查过的路径和操作者，不要因为点击一次就声称覆盖完整。

## 诊断意外访问

**从有效身份开始。**确认浏览器会话属于预期的测试角色。然后使用产品的管理工具检查组成员身份、空间授权、页面访问和工作流关联。不要同时更改多个控件，否则拒绝结果将失去诊断价值。

1. **确认身份：**分别使用贡献者、发布者和排除用户会话。
2. **查找授权来源：**确定哪个成员关系或设置允许了尝试的操作。
3. **调整实验室控件：**保留负责人的合法访问权限。
4. **重复同一尝试：**遭拒后记录未变更的源版本。
5. **重复允许的案例：**确认授权发布仍能正常运行。

**最终证据清单：**记录 Confluence 页面树和映射页面 ID、Jira 实验室方案关联、实验室工作流关联、每个测试角色的组成员身份、允许读取需求、拒绝编辑且版本未变、允许创建草案、拒绝转换到“已批准”且状态未变、拒绝排除用户读取，以及清理负责人。每行保留操作者角色、起始和最终版本或状态、原生结果和独立审查者。记录在租户中观察到的导航路径，因为不同套餐提供的标签和控件各异。

**完成检查：**交付映射的正式依据页面、仅供实验室使用的工作流、预期角色矩阵和观察到的权限记录。如果套餐缺少所需控件，将相应行标记为“已阻止”。发布经验的前提是这些测试已经成功，而不只是存在设置截图。

## 故障排查与回滚

**贡献者仍能编辑：**检查页面访问、空间权限和成员身份。**转换仍然成功：**检查工作流关联和绕过路径。**找不到设置：**确认管理类型、版本和管理员权限。

**回滚：**移除连接器授权并归档草案。保留证据后，再解除仅供实验室使用的方案和工作流。通过审查过的历史记录或补偿性编辑恢复已批准的页面措辞。不要删除审计证据。

## 练习与自测

**Jira 显示三十天，REQ-17 显示七天。**找出实现输入值和负责协调差异的人。

**预期推理：**Confluence 决定意图。Jira 中存在提案或交付错误。暂停发布并请产品负责人协调差异，不要自行选择最新时间戳。

## 主要参考资料

- **限制和套餐：**[Confluence 权限](https://support.atlassian.com/confluence-cloud/docs/manage-permissions-on-the-page-level/)。
- **共享控件：**[特定内容访问](https://support.atlassian.com/confluence-cloud/docs/add-or-remove-page-restrictions/)。
- **方案管理：**[Jira 权限方案](https://support.atlassian.com/jira-cloud-administration/docs/grant-or-revoke-permissions-in-a-scheme/)。
- **转换条件：**[高级工作流](https://support.atlassian.com/jira-cloud-administration/docs/configure-advanced-issue-workflows/)。

## 后续步骤

**访问测试通过后，继续阅读[跨系统发布](/articles/ai-collaboration-confluence-jira-publication/)**。
