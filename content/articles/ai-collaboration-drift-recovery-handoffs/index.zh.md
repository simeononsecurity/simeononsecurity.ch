---
title: "AI 代理偏差恢复与交接工作流"
date: 2026-10-01
lastmod: 2026-11-08
toc: true
draft: false
description: "识别过时的来源和策略适配器，恢复中断的发布，并验证代理之间的独立交接。"
genre: ["人工智能", "团队协作", "软件工程"]
tags: ["AI 协作课程", "来源偏差", "发布恢复", "代理交接", "最新来源验证", "补偿变更"]
cover: "/img/cover/A_group_of_diverse_professionals_collaborating_on_a_cyberse.webp"
coverAlt: "网络安全工作空间中，专业人员共同审查项目工作的插图"
coverCaption: ""
---
[返回 AI 协作课程](/ai-collaboration-course-start/)

**在任务开始前和发布中断后检查偏差。**在代码库或工作沙箱中比较来源版本、适配器版本和交付状态。完成一个工作轨道后执行此操作。这样可避免旧摘要被当成当前权威信息，并保留可审查的恢复历史。

## 要点

- **来源偏差**不同于适配器偏差。
- **部分发布**需要每个系统都有单独的台账。
- **恢复**会保留历史和经过审查的变更。
- **交接**要求另一位审查者独立读取当前来源。

## 开始之前

**前提条件：**[GitHub 浏览器工作流](/articles/ai-collaboration-github-browser-workflow/)或[混合发布工作流](/articles/ai-collaboration-confluence-jira-publication/)。**预计耗时：**60 至 90 分钟。**难度：**高级审查。

**安全：**仅使用合成记录。恢复测试前暂停自动发布。本文不提供正在运行的删除服务。

**读者成果：**完成状态清单、所有者决策、经过审查的修复，以及另一位审查者可依据当前来源重建的交接。完成练习不代表获得发布批准。

## 分类识别偏差

| 偏差类型 | 信号 | 修复负责人 |
|---|---|---|
| **需求** | 来源与清单不同 | 产品负责人 |
| **策略** | 适配器与 POL-01 不同 | 策略负责人 |
| **实现** | 配置与意图矛盾 | 维护者 |
| **运行手册** | 说明与已批准的行为矛盾 | 运维负责人 |
| **访问** | 以前可读的来源现在被拒绝 | 管理员，任务已停止 |
| **交付** | 台账未完成却标记为完成 | 交付负责人 |

**最新文本不一定是已批准的权威信息。**最近发生的未授权编辑需要调查，不能自动采用。复制值之前先确认状态和负责人。

## 执行预检

```text
Read MAP-01 and capture its revision.
Read POL-01 and compare active adapter versions.
Read REQ-17 and RUN-04 from mapped homes.
Read config.json at protected main.
Read frozen proposal and current role reviews.
Compare current sources with reviewed bases.
List mismatches, denied reads, and pending publications.
Stop consequential writes until owners resolve each mismatch.
```

**贡献者在起草前执行预检。发布者在写入前再次执行。**将版本比较记录与提案一同保存。每周检查可以补充这些读取，但不能替代它们。

**适配器偏差示例：**POL-01 已到版本 2，而 CLAUDE.md 仍写着版本 1。停止操作，阅读经过审查的策略变更，通过受保护的 PR 更新适配器，并启动新会话。如果没有加载策略，只改版本号无法修复上下文。

**在离线实验环境中引入来源偏差：**将提供的 ZIP 新副本解压到空的临时目录。从根目录将 `baseline/` 复制到 `candidate/`，运行 `python3 check.py capture --base baseline > candidate/context.json`，再运行 `python3 check.py validate --base baseline --candidate candidate`。记录第一次 `PASS`。在文本编辑器中打开 `baseline/requirement.json`，仅将 `"retention_days": 7` 改为 `"retention_days": 8`。再次运行相同的 validate 命令。预期退出状态为非零，并显示 `STALE_CONTEXT: capture the trusted base again`。记录两次输出和变更的来源路径。保存私人证据后删除临时解压目录，再解压一个新副本以重置环境。不要将八天变更应用到已发布的代码库，也不要把重新捕获视为所有者批准。

**在临时代码库中引入适配器偏差：**在新的提案分支上，将已批准的 POL-01 版本 1 适配器文本复制到 CLAUDE.md，并标记为版本 1。在单独的、经过审查的策略提案中，写明包含具体新停止条件的版本 2 变更。让适配器保持版本 1。合并或运行代理之前，请审查者比较两条记录并标记适配器已过时。关闭测试提案，或通过经过审查的 PR 更新适配器，以重置测试。然后打开新会话，验证两个版本和新的停止条件。保留旧 diff 和修正后的 diff。这是文档测试，不是模拟平台拒绝。

## 恢复中断的发布

1. **暂停 PROP-042 发布**并指定恢复负责人。
2. **读取所有参与系统的实际状态。**区分已完成、失败和未尝试的操作。
3. **请产品团队选择**继续完成、经过审查的回退或暂缓。
4. **准备恢复提案，**采用最新基准，并保持范围和例外不变，除非它们经过明确审查。
5. **每次执行一个经过审查的步骤，**记录并回读每项结果。
6. **恢复日常工作前，**验证最终状态和剩余限制。

```yaml
recovery_id: RECOVERY-042
proposal_id: PROP-042
mode: awaiting-owner-choice
illustrative_state:
  requirement: thirty-days-published
  implementation: seven-days-on-main
  runbook: seven-days
  delivery: blocked
choices:
  forward: finish approved implementation and runbook
  backout: restore baseline through reviewed changes
  hold: wait for evidence or access
```

**将示例状态替换为观察到的修订版本和值。**以前的台账条目或助手声明都不能证明已回读结果。

| 选择 | 适用情况 | 限制 |
|---|---|---|
| **继续完成** | 批准仍有效且来源一致 | 需要重新验证 |
| **回退** | 所有者撤回变更或实现失败 | 无法恢复已删除的数据 |
| **暂缓** | 缺少证据或访问权限 | 交付仍未完成 |

**缺少证据时选择暂缓。**合成练习没有盲目覆盖的紧迫理由。明确下一角色和缺失的证据。

**GitHub 恢复**使用经过审查的 revert 或补偿变更。**Confluence 恢复**比较历史记录，并进行经过审查的恢复或补偿。**Jira 恢复**保留提案历史，同时重新打开或阻止交付。读取最终修订版本，不要假设历史编号会重置。

## 验证独立交接

```text
Handoff: HANDOFF-042
Task: PROP-042
Map and policy: attach current approved revisions
Evidence: requirement, runbook, configuration references
Ledger: completed, failed, pending
Decision: owner choice and fixed proposal revision
Limits: no runtime deletion test or production data
Next role: accountable role
Next action: one bounded step
Stop: changed base, access denial, conflicting authority
```

**使用地图和交接信息打开另一个工具或干净会话，**不要沿用之前的对话。要求重新读取来源、生成新清单并指出待处理操作。如果将手动浏览器证据标注为快照，并在写入前重新检查，这些证据仍然有效。

**负向交接：**拒绝访问 REQ-17。预期结果应是明确阻断，而不是猜测值或特权摘录。通过管理流程仅恢复已批准的访问，然后重新验证。

## 先诊断再修复

**从状态清单开始。**“助手意见不一致”描述的是回答症状，不是底层来源问题。要求任何助手修复之前，先分别读取映射的需求、配置、运行手册、策略和交付记录。

| 观察结果 | 诊断 | 首要操作 |
|---|---|---|
| **两个来源一致，旧回答不同** | 回答上下文过时 | 根据最新读取结果重建 |
| **需求三十天，配置七天** | 交付或实现不一致 | 检查已批准的包和台账 |
| **适配器一，策略二** | 指令版本不一致 | 阅读策略变更并修复适配器 |
| **来源以前可读，现在被拒绝** | 访问权限变更 | 停止任务并请求授权审查 |
| **台账已完成，运行手册为七天** | 未有效回读便关闭 | 重新打开或阻止交付并调查 |

**不要把每项不一致都视为模型问题。**刷新会话能修复过时的对话上下文，但不会发布运行手册、恢复缺失权限或调和所有者之间相互矛盾的决定。选择工具操作前先指定修复负责人。

## 实施补偿

**中断示例：**REQ-17 中有已批准的三十天意图，交付仍待处理。配置和运行手册仍写着七天。维护者报告存在未解决的实现故障。产品团队选择恢复，而不是继续完成。

1. **记录当前版本：**需求三十天，配置七天，运行手册七天，交付已阻止。
2. **冻结待处理提案：**保留审查记录和发布失败证据。
3. **准备需求补偿修订：**恢复到七天，同时保留期间新增的排除项和备注。
4. **取得所有者审查：**注明当前来源版本和准确的恢复措辞。
5. **通过授权流程发布：**回读生成的需求版本。
6. **核对台账：**所有适用的已发布值均为七，原始变更未交付。

**补偿不会删除历史。**将尝试改为三十天、该变更失败和后续恢复分别作为独立记录保留。最终来源写明七天，交付历史说明已批准的提案为何未完成。

```text
Recovery decision: illustrative compensation
Original proposal: PROP-042 revision 1
Observed mismatch: requirement 30, configuration/runbook 7
Owner decision: restore approved baseline intent
Review object: fixed compensation against current requirement version
Result: capture resulting revision and seven-day read-back
Original delivery: withdrawn or blocked with explanation
Limit: no runtime deletion or data restoration performed
```

**明确保留其他作者添加的例外。**盲目粘贴旧页面内容可能会移除有效的中间变更。比较当前文本和预期文本，再根据当前版本审查最小补偿变更。

## 测试新的交接

**使用干净会话和另一位审查者。**提供地图、固定版本的包、台账和恢复决策，不提供之前的聊天记录。请接收者说明当前意图、配置、操作指南和下一项获准操作。

```text
Read the mapped current sources independently.
Distinguish approved intent, committed configuration, and delivery state.
Compare them with the reviewed package and ledger.
List missing reads and changed bases.
Recommend one bounded next action with its accountable role.
Do not treat this handoff as approval or publication permission.
```

**预期推理：**接收者在描述基准已恢复之前先验证补偿结果。如果只重复交接信息中的“七天”，就没有测试独立读取要求。应要求来源证据，而不是另一份摘要。

**已完成的教学清单，合成中断：**

| 记录 | 观察到的状态 | 应保留的证据 | 下一负责人 |
|---|---|---|---|
| REQ-17 | v5 写明三十天，排除备份 | 页面历史和最新读取 | 产品 |
| 受保护配置 | `main` 上的 `base-001` 写明七天 | 提交回读和合并被拒事件 | 代码库维护者 |
| RUN-04 | v2 仍写明七天 | 最新页面读取 | 运维 |
| PROP-042 | r1 已批准，交付被阻止 | 固定版本的审查记录和台账 | 交付负责人 |

将此清单交给第二位读者，不提供旧聊天记录。只有当读者独立找到全部四种状态、指出备份排除项、确认 `base-001` 是当前受保护修订版本，并建议由所有者审查的恢复步骤时，交接才算通过。修订版本错误、遗漏例外或无依据恢复均判定失败。再次写入前记录读者引用的来源和任何修正。

## 决定是否恢复工作

| 预检结果 | 恢复决定 |
|---|---|
| **来源符合固定批准内容** | 继续获准的待处理步骤 |
| **来源变更超出审查范围** | 暂停，进行比较并重新审查 |
| **缺少读取权限** | 暂缓并指定访问审查者 |
| **策略已变更** | 修复适配器并重新评估任务权限 |
| **写入结果未知** | 重试前读取目标位置 |

**明确恢复的验收标准。**要求回读结果一致、审查对象处于当前状态、台账已核对且有新的交接。不要因为助手声称问题已解决就关闭恢复流程。

**完成检查：**提供观察到的状态清单、所有者决策、经过审查的修复、最终回读和独立重建。如果访问权限阻止读取，请记录阻断情况。将此证据标准用于最终项目。

## 故障排查与回退

**revert 冲突：**根据当前状态准备补偿变更。**恢复时丢失例外：**写入前比较整个相关部分。**旧记忆控制回答：**从已批准来源重新开始，并移除过时草稿上下文。

**回退恢复操作：**停在最后一个已验证状态，并追加台账条目。不要删除原生审计事件，也不要强制重置受保护的历史记录。将未解决的权限问题升级给产品团队。

## 练习与自检

**引入过时证据、旧策略适配器和部分发布。**不作说明地将记录交给另一位审查者，并请其指出修复负责人。

**预期推理：**产品团队负责协调需求，策略负责人负责适配器对齐，交付恢复协调人负责协调各参与方。“刷新上下文”无法完整修复所有这些情况。

## 主要参考资料

- **代码库恢复控制：**[受保护分支](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches)。
- **页面历史：**[Confluence 文档](https://support.atlassian.com/confluence-cloud/docs/use-confluence-for-technical-documentation/)。
- **指令检查：**[Claude Code 记忆](https://code.claude.com/docs/en/memory)。

## 后续步骤

**使用两条工作轨道和第二位读者完成 [Retention Capstone](/articles/ai-collaboration-retention-capstone/)。**展示最新来源读取、版本偏差、决策负责人、经过审查的恢复、回读和独立重建。
