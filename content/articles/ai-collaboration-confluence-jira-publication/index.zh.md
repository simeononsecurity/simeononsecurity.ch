---
title: "GitHub、Confluence 与 Jira 的 AI 发布工作流"
date: 2026-10-01
lastmod: 2026-11-08
toc: true
draft: false
description: "通过版本检查和部分发布恢复，在 Confluence、GitHub 与 Jira 中发布固定的保留期限提案。"
genre: ["人工智能", "团队协作", "软件工程"]
tags: ["AI 协作课程", "Confluence Cloud", "Jira Cloud", "跨系统发布", "版本检查", "发布台账", "部分发布"]
cover: "/img/cover/A_group_of_diverse_professionals_collaborating_on_a_cyberse.webp"
coverAlt: "网络安全工作区中，专业人员共同审查项目工作的插图"
coverCaption: ""
---

[返回 AI 协作课程](/ai-collaboration-course-start/)

**贡献者在负责人批准前冻结 PROP-042。** Confluence 发布者更新需求，GitHub 维护者合并实现，运维团队发布运行手册。Jira 记录每个步骤。请先核实权限，因为这三个系统不会构成一个原子事务。发布台账会显示未完成的交付。

## 关键要点

- **已批准的意图**与实际交付行为不同。
- **固定的提案修订版**将评审绑定到特定版本。
- **发布台账**会暴露未完成的步骤。
- **重新读取最新来源**可防范基线变化。

## 开始之前

**前置条件：**[工作环境设置](/articles/ai-collaboration-confluence-jira-setup/)、发布权限、负责人和仓库维护者。**预计时间：**两小时。**难度：**高级协调。

**基础界面：**在浏览器中读取，可选择在已批准的聊天中起草，由人工执行发布。此流程不假设你订阅了连接器。添加集成前，请检查租户中的可用性、权限范围、供应商的数据处理方式和身份映射。切勿将负责人的凭据分享给贡献者。

**读者成果：**完成后，你将拥有固定提案、按系统划分的发布台账、回读证据，以及针对第一个未完成步骤的恢复决策。本练习验证流程与证据处理，不验证生产环境中的保留行为。

## 记录当前来源

1. **读取 MAP-01**，然后通过映射的页面 ID 打开 REQ-17 和 RUN-04。
2. **打开页面菜单和 Page History**，记录数字版本、状态、措辞、负责人和例外。
3. **读取 Jira 项目**，并附上固定的提案导出文件或 GitHub commit。项目键本身无法冻结评审证据。
4. **读取已批准的 POL-01** 和受保护的配置基线。
5. **只向聊天提供必要的合成摘录**，标记为快照，并禁用所有可写操作。

```text
Task: PROP-042, propose only
Authority: Confluence REQ-17 for intent, GitHub for behavior
Read: mapped current pages, versions, scope, exceptions
Proposal: synthetic export retention from 7 to 30 days
Output: requirement wording, config diff, runbook, ledger
Evidence: source ID and captured revision for each factual claim
Unknowns: missing access and absent runtime observations
Stop: conflict, changed base, or denied access
```

**离线资料包仍基于快照。**发布者在写入前重新读取当前来源。访问被拒会阻止发布。旧导出文件不能替代当前授权。

## 固定提案

```json
{
  "proposal_id": "PROP-042",
  "proposal_revision": 1,
  "requirement_base_version": 1,
  "runbook_base_version": 1,
  "policy_version": 1,
  "from_days": 7,
  "to_days": 30,
  "status": "awaiting-owner-review",
  "publication_order": ["requirement", "implementation", "runbook", "delivery"]
}
```

**将示例页面版本替换为实际捕获的版本。**将固定 JSON 和拟议措辞附加到 Jira。每位负责人记录自己的角色、决定、提案修订版、来源版本和评审时间。任何实质性编辑都会让资料包返回 `Review`。

**产品团队评审意图和范围。运维团队评审清理和恢复。**维护者评审 diff。对可变聊天消息的回应不构成绑定到修订版的批准。

## 发布并回读

1. **发布者核实两位负责人的评审且确认来源基线未变后，将 Jira 转为 `Publishing`。**
2. **发布 REQ-17**，将保留期限设为三十天，并添加待交付字段。记录结果页面版本、范围和例外。
3. **打开 GitHub 实现 PR**，引用已批准的页面版本。将配置改为三十天，并附上不具权威性的需求快照。
4. **仓库评审通过后合并**，并回读 **`main`**。分别记录仓库中的已提交行为和运行时行为。
5. **发布 RUN-04**，按 ID 回读并记录结果版本。发布者更新需求中的交付引用。
6. **仅在所有记录一致且附有最终回读证据后完成 Jira。**

**本地验证器仅用于检查快照一致性。**将变更前的 Confluence 需求复制到实验室基线 JSON 架构中并捕获，然后把候选版本改为三十天。递增本地快照修订版，同时在 Jira 中单独保留实际 Confluence 版本。以 GitHub 为根源的工作流不会验证实时 Confluence。不要把绿色状态说成已核验外部权威来源。

**本练习中不要部署删除功能。**真实服务需要部署证据、受控测试数据、临时暂停删除的机制和运行时边界测试。合并只能证明仓库状态，不能证明生产环境中的保留行为。

## 跟踪部分发布

| 步骤 | 初始状态 | 完成证据 |
|---|---|---|
| **REQ-17** | Pending | 结果页面版本 |
| **配置** | Pending | 已合并的 commit 和评审 |
| **RUN-04** | Pending | 结果页面版本 |
| **关闭 Jira** | Pending | 最终回读和状态转换 |

**先记录每项结果，再尝试下一步。**PROP-042 将各系统事件关联起来。完成一行并不表示整个变更已经完成。

**失败示例：**Confluence 已发布三十天，但 GitHub 拒绝合并。将 Jira 保持在 `Blocked`，并将需求标记为待交付。产品团队选择继续完成，或经评审后恢复为七天。不要把应急 README 副本提升为需求权威来源。

## 处理并发编辑

**浏览器基线：**在试点期间指定一位发布者。编辑前立即重新打开 Page History，并在发布后再次打开。如果其他作者修改了来源，请停止、比较、协调并重新审批。串行发布是一种流程，并不保证原子事务。

**API 扩展：**Confluence v2 文档说明了 **`GET /wiki/api/v2/pages/{id}?body-format=storage`** 和带版本对象的 **`PUT /wiki/api/v2/pages/{id}`**。经过评审的发布集成会将当前版本与已批准基线比较，提交下一版本并回读。不要自动刷新失败版本，也不要用旧正文重试。

**API 成功本身不够。**检查结果内容、来源 ID、范围和版本。本课程不提供可写 API 客户端。人工通过浏览器发布是非程序员可执行的基线流程。

## 验证负面情形

| 注入情形 | 预期判断 |
|---|---|
| **审批后更改来源** | 停止，并基于新版本重新审批 |
| **移除发布者的编辑权限** | 拒绝更新，并保留待处理台账 |
| **将 Jira 设为六十天** | 停止冲突，并保留 Confluence 的权威性 |
| **运行手册发布失败** | 保持交付未完成，并分配恢复工作 |

**记录沙箱中的实际结果**，包括执行者角色和前后修订版。不要在被拒用户的证据中包含受保护页面正文。预期结果不等于实测结果。

## 整理评审资料包

**冻结内容，而不只是提案标签。**PROP-042 会出现在每个系统中，但标签无法识别负责人评审的具体正文。将精确的需求措辞、实现 diff、运行手册措辞、来源版本和发布顺序放入同一个固定资料包。

```text
Package: PROP-042 revision 1, illustrative
Intent: synthetic export retention changes from 7 to 30 days
Exclusions: production data, backups, legal holds
Requirement amendment: fixed proposed REQ-17 wording
Implementation: fixed candidate diff and protected base reference
Runbook amendment: fixed RUN-04 wording and recovery limits
Review: product and operations decisions for this package
Delivery: requirement -> implementation -> runbook -> closure
Stop: changed source, missing review, denied write, failed read-back
```

**让两位负责人都能读懂资料包。**产品团队需要了解意图和排除项。运维团队需要了解操作变化和恢复边界。双方都要理解已批准意图与已交付配置不一致的时间段。对于不熟悉仓库文件的负责人，仅有代码 diff 不够。

**此合成示例的完整资料包内容：**

```text
REQ-17 proposed v5: "Synthetic export files are retained for 30 days from creation. This pilot excludes production data, backups, and legal holds. Delivery remains pending until the GitHub configuration and RUN-04 read-backs match this approved wording."

GitHub config.json, proposed change against base-001:
-  "retention_days": 7
+  "retention_days": 30

RUN-04 proposed v3: "Retention days: 30. Synthetic exports only. No deletion job runs in this lab. If publication fails, keep delivery pending, read back each source, and obtain owner approval before restoring the seven-day configuration or completing the thirty-day publication."
```

这些句子是示例提案文本，不是实时租户记录。评审前附上实际基线 commit 和页面版本。固定资料包必须包含完整的拟议正文，而不是让负责人自行推断内容的摘要。

**将离线快照与实时发布分开。**首次写入前，发布者重新检查映射页面，维护者重新检查受保护基线。任何一项发生变化，旧资料包都会停在 `Review`。

## 查看台账

**示例状态推进：**表格使用教学版本号，不代表观测结果。在沙箱中每次写入后填写真实的结果版本和 commit。

| 步骤 | 回读成功后的状态 | 剩余工作 |
|---|---|---|
| **负责人评审完成** | 提案已批准，所有已发布值为七天 | 全部发布步骤 |
| **REQ-17 已发布** | 意图设为三十天，交付待处理 | 配置和运行手册 |
| **GitHub 合并已回读** | 意图/配置为三十天，运行手册为七天 | 运行手册和最终协调 |
| **RUN-04 已发布** | 所有适用记录为三十天 | 独立最终回读 |
| **交付已关闭** | 台账完整并附证据 | 已声明的运行时差距仍存在 |

**交付待处理是有意义的状态。**在发布未完成时，它能避免把旧实现描述为符合新意图。在此期间，读者需要同时了解两个值，而不是只看到“保留期限为三十天”的摘要。

**将失败尝试追加为独立事件。**如果运行手册写入失败，保留需求和配置已成功发布的结果。记录尝试的操作、失败、未变化的版本、分配的角色和下一步。不要把已完成行重置为 Pending，也不要抹去已观察到的顺序。

**旧版本拒绝示例：**发布者读取 REQ-17 v4，另一位获授权的编辑者发布 v5，然后发布者尝试基于 v4 应用 PROP-042 r1。平台报告版本冲突，或写入前读取发现 v5。记录执行者 `publisher`、初始版本 `v4`、尝试的 `PROP-042 r1`、观察到的冲突或当前版本变化、此次尝试未改变的最终版本 `v5`，以及分配的负责人 `product owner`。保持 Jira 为 `Review`。重新读取 v5、协调措辞，并在再次写入前请求评审新的固定资料包。实时测试时使用实际平台响应和 Page History。此行是教学示例。

**已完成的教学示例，仅用合成值：**

| 系统 | 初始来源 | 固定评审 | 写入和回读 | 最终状态 |
|---|---|---|---|---|
| Confluence REQ-17 | v4，七天 | PROP-042 r1，产品团队批准从 v4 改为 v5 | 发布者写入 v5，评审者重新打开 v5 | 三十天，排除备份和法律保留 |
| GitHub 配置 | `main` commit `base-001`，七天 | PROP-042 r1，运维团队批准候选 diff | PR 合并为 `merge-002`，独立克隆读取到三十 | 受保护源中为三十天 |
| Confluence RUN-04 | v2，七天 | PROP-042 r1，运维团队批准从 v2 改为 v3 | 发布者写入 v3，评审者重新打开 v3 | 带回退方案的三十天操作步骤 |
| Jira PROP-042 | In Review | 两位负责人的决定绑定到 r1 | 交付负责人附上证据并转为 Done | 三项回读后关闭 |

以上标签仅作说明，不是租户证据。台账需要原生页面版本链接和 commit ID。将 Jira 转为 Done 前，附上冻结提案、两种角色的评审、来源基线记录、每项发布回读、负面测试结果和未解决的运行时限制。缺少任何一项时，保持交付开放或 `Blocked`。

**资料包门槛：**将五项检查分别标记为 `Supported` 或 `Blocked`：来源修订版是最新的，两位负责人批准了相同的固定修订版，所有必要发布都与回读一致，运行时限制仍明确，恢复状态已协调。`Done` 要求五项检查全部为 `Supported`，且没有未授权写入。

## 处理不确定的写入

**超时会让结果处于未知状态。**它既不能证明成功，也不能证明失败。在浏览器基线流程中，先重新打开映射来源并检查当前内容和历史，再决定是否重试。

1. **暂停下一步：**保持交付未完成。
2. **读取目标：**将当前措辞、版本和范围与固定资料包比较。
3. **记录观察结果：**已完成、未变化、冲突或无法访问。
4. **选择下一步：**从已验证的完成状态继续，重试未变化且已获授权的步骤，或上报冲突。
5. **保留不确定性：**将失败/未知尝试与后续回读一起保留。

**不要盲目重放整个流程。**重复已完成的步骤会增加修订版，并可能覆盖无关编辑。应从已验证状态继续。如果无法访问来源，选择 `Hold`，不要根据旧台账猜测。

## 比较恢复决策

| 情况 | 要评审的决策 | 原因 |
|---|---|---|
| **需求已变更，合并被拒** | 继续完成需求，或对需求做补偿 | 意图与行为不同 |
| **配置已变更，运行手册被拒** | 完成运行手册，或回退配置 | 操作指导已过时 |
| **另一位负责人更改范围** | 返回 `Review` | 固定批准描述的是另一份正文 |
| **写入结果未知** | 先读取目标 | 重试取决于观察到的状态 |
| **发布者失去访问权限** | 保持 `Hold` 并申请获授权的管理支持 | 旧授权不允许新的写入 |

**根据当前状态和负责人决定选择。**继续完成需要当前批准和有效控制。补偿需要结合期间发生的编辑评审恢复方案。恢复变更是另一次发布，不是流程的特权例外。

## 发布完成检查

**交付一份独立评审者能够核对的资料包。**评审者应能找到确切的已评审提案、来源基线、两种角色的评审、每项写入结果、最终值和剩余运行时限制。请他们找出中断后的第一个未完成步骤。

**预期判断：**下一步取决于最新来源和台账，而不是先前助手的信心。将最终映射引用带入检索测试，确保发现流程保留相同的权威区分。

## 故障排查与恢复

**版本已变更：**比较历史并重新评审。**快照检查通过但 wiki 不同：**重新获取当前 Confluence 来源。**过早设为 Done：**通过允许的流程重新打开并记录缺失步骤。

**恢复：**使用 Page History 比较，并执行负责人评审过的恢复或补偿性编辑。记录结果版本，不要假设恢复会重置编号。如果产品选择回退，通过受保护的 PR 回退配置。已删除文件不在回退承诺范围内。

## 练习与自查

**在发布 REQ-17 后中断流程**，只向另一位发布者提供映射和台账。

**预期判断：**对方获取当前来源，确认固定批准，然后只继续获授权的待处理步骤。证据缺失时，工作返回 `Review`。

## 主要参考资料

- **历史与恢复：**[Confluence 技术文档](https://support.atlassian.com/confluence-cloud/docs/use-confluence-for-technical-documentation/).
- **版本化 API 操作：**[Confluence REST API v2 页面](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-page/).
- **工作流控制：**[Jira 高级工作流](https://support.atlassian.com/jira-cloud-administration/docs/configure-advanced-issue-workflows/).
- **集成安全：**[MCP 安全最佳实践](https://modelcontextprotocol.io/docs/latest/tutorials/security/security_best_practices).

## 下一步

**完成经评审的发布练习后，继续阅读[地图优先检索](/articles/ai-collaboration-map-first-retrieval/)。**
