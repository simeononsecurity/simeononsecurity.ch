---
title: "AI 协作综合实践：GitHub、Confluence 与 Jira"
date: 2026-10-01
lastmod: 2026-11-08
toc: true
draft: false
description: "通过以 GitHub 为先的工作流以及 Confluence/Jira 工作流交付合成数据保留期限变更，并记录失败证据和独立审查结果。"
genre: ["Artificial Intelligence", "Team Collaboration", "Software Engineering"]
tags: ["AI collaboration course", "retention proposal", "GitHub review", "Confluence Jira workflow", "failure matrix", "independent acceptance"]
cover: "/img/cover/A_group_of_diverse_professionals_collaborating_on_a_cyberse.webp"
coverAlt: "专业人士在网络安全工作环境中共同审查项目工作内容的插图"
coverCaption: ""
---

[返回 AI 协作课程](/ai-collaboration-course-start/)

**通过两种方式交付 PROP-042**：使用以 GitHub 为先的流程，以及使用 GitHub 配合 Confluence/Jira 的流程。你负责提交，独立负责人负责审查，获授权的发布者负责应用变更。完成前置课程后，请在隔离的合成数据沙箱中操作。本综合实践会检验完整流程，包括拒绝、恢复和独立交接，而不只是助手生成文本的质量。

## 关键要点

- **同一项变更**用于比较两种权威来源模型。
- **负向测试**与成功交付同样重要。
- **证据包**支持独立审查。
- **实验室完成**不等于获准部署到生产环境。

## 开始之前

**先决条件：**完成前置[课程模块](/ai-collaboration-course-start/)，获得已批准的沙箱访问权限，并安排不同的审查者。**计划用时：**分多次完成，预计八至十二小时，另加独立审查时间。实际用时取决于账户设置和修复工作。**难度：**高级。

**所需产物：**章程、映射、策略、适配器、基线、清单、固定提案、负责人审查、台账、恢复记录和交接记录。若缺少计划所需的权限，应阻止完成，不得假定检查已通过。

**测试前，请为每条流程准备独立的证据目录。**审查者应能在不依赖聊天摘要的情况下，识别操作者、来源版本、尝试的操作、观察到的结果和最终状态。

## 建立两套基线

1. **创建隔离的运行环境**，分别命名为 GitHub-first 和 Mixed。版本和审查记录必须分开。
2. **通过各流程已批准的步骤恢复七天基线**，并记录恢复后的版本。
3. **使用贡献者和被排除用户账户验证拒绝控制。**
4. **捕获当前上下文**，并确认适配器与策略一致。
5. **声明范围：**合成导出数据保留三十天，不包括真实数据、备份和法律保留数据。

**PROP-042 是关联标签，不是可重复使用的批准。**每次运行都需要独立冻结的版本和来源证据。报告中应包含运行 ID。

## 通过 GitHub-first 流程交付

**按照 GitHub 课程的说明创建 Issue 和候选 PR。**同时修改要求、配置、提案和运行手册。捕获受保护的基线，运行可信检查，并让产品和运营负责人针对最终提交进行审查。

```text
Run: GitHub-first
Change: synthetic retention 7 -> 30 days
Requirement: REQ-17 revision 2
Configuration: retention_days 30
Runbook: Retention days: 30
Proposal: base revision 1, from 7, to 30
Manifest: protected pre-change source hashes
Review: product and operations at final proposal revision
Publication: merged commit and read-back
Limit: no running deletion service exercised
```

**填写沙箱中的实际引用。**上面的内容是预期映射示例，不是已完成的证据。维护者只能在审查通过后合并，然后独立读取 **`main`**。Issue 关闭前，应先关联最终记录。

## 通过 Mixed 流程交付

**读取 Confluence 版本并冻结 Jira 提案。**取得两位负责人的审查。发布标记为待交付的要求，合并配置，发布运行手册，并在将状态设为 Done 前重新读取所有系统。

**记录每次发布**及其页面版本、提交或状态转换证据。仓库中的要求副本只是快照。本地检查器无法证明 Confluence 当前的权威内容。

| 比较项 | GitHub-first | Mixed 工作场景 |
|---|---|---|
| **要求** | 受保护仓库中的审查 | 经 Confluence 负责人审查后发布 |
| **协调** | Issue/PR | 固定的 Jira 提案 |
| **发布单位** | 仓库合并 | 分别写入页面并合并 |
| **新鲜度** | 受保护的提交 | 页面版本和提交 |
| **恢复** | 经审查的还原或补偿 | 依据台账进行补偿 |

**根据所有权需求选择流程。**GitHub-first 减少跨系统协调。Mixed 流程保留现有工作场所中的内容，并增加发布和访问检查。

## 运行失败矩阵

| 案例 | 注入的情况 | 必须观察到的证据 |
|---|---|---|
| **已批准的变更** | 提交经审查的三十天提案 | 一致的回读结果和审查记录 |
| **上下文过时** | 捕获后更改来源 | 拒绝、协调和重新批准 |
| **未经授权的写入** | 由贡献者发布 | 拒绝结果和未更改的版本 |
| **冲突** | Jira 为六十天，Confluence 为七天 | 阻止操作并由负责人协调 |
| **部分发布** | 一次写入后中断 | 待处理台账和恢复记录 |
| **访问被拒** | 移除任务读取权限 | 未泄露受保护文本，也未发布 |
| **恢复** | 经批准的完成或回退 | 新的、经过审查的版本 |
| **交接** | 新会话仅获得映射和台账 | 重新读取来源并采取正确的下一步操作 |

**跨系统冲突属于 Mixed 流程。**在 GitHub-first 流程中，测试 Issue 描述与已批准文件冲突的情况。其他适用案例应在两种流程中都运行。本地验证器失败不能替代真实的权限证据。

| 案例和证据文件 | GitHub-first 运行 | Mixed 运行 |
|---|---|---|
| **已批准的变更** `01-approved-change.md` | 已审查的 PR 和回读 | 已审查的页面、合并和台账 |
| **上下文过时** `02-stale-context.md` | 捕获后更改受保护的基线 | 捕获后更改权威页面 |
| **未经授权的写入** `03-unauthorized-write.md` | 拒绝贡献者直接推送 | 拒绝贡献者编辑页面并转换状态 |
| **冲突** `04-conflict.md` | Issue 与已批准文件意见不一 | Jira 文本与 Confluence 意见不一 |
| **部分发布** `05-partial-publication.md` | 合并或回读前停止 | 写入一个页面后停止 |
| **访问被拒** `06-access-denial.md` | 不向用户提供受保护的仓库来源 | 将用户排除在受限页面之外 |
| **恢复** `07-recovery.md` | 经审查的还原或完成 | 依照台账进行补偿 |
| **交接** `08-handoff.md` | 新会话读取受保护文件 | 新会话读取映射的页面和台账 |

**测试前先创建每个证据文件。**记录预期结果、观察结果、操作者角色、初始和最终版本、原生证据引用以及审查者决定。浏览器路由提示不等同于直接推送被拒。两种流程的目录应保持分开。

**将预期结果和观察结果分开记录。**每个案例都应记录运行 ID、操作者角色、初始版本、尝试的操作、预期结果、观察结果、结果版本和审查者决定。共享报告中应遮盖凭据和账户标识符。

## 评估完成情况

**只有所有适用项目都有观察到的证据并获得独立认可，才算通过。**审查者除了检查一致性日志，还要检查权限、来源新鲜度、角色审查、部分发布和交接重建情况。

**出现未经授权的发布、拒绝访问的文本进入模型，或静默覆盖已更改基线时，立即判定失败。**在修正问题并通过重复测试前，工作应保持阻塞状态。不要把这些失败平均计算成通过。

**衡量已完成和受阻案例数、被拒的过时提案数、被拒写入数、恢复次数和审查者耗时。**预期结果在实际观察前仍只是预期。提供的十项单元测试只检查一致性，不验证实时租户安全性。

## 规划两次运行

**不要在两条流程之间重复使用批准。**两次运行的目标值相同，但来源位置、捕获的版本、权限和发布步骤各不相同。每次运行都要使用独立的证据目录和审查材料。

```text
capstone-evidence/
  github-first/
    charter-and-map
    captured-sources
    fixed-proposal
    role-reviews
    consistency-results
    permission-results
    publication-readback
    recovery-and-handoff
  mixed/
    same evidence categories, independently captured
```

**这些名称只是组织示例**，不是已提供的归档文件。实际证据应私下保存在已批准的沙箱中。共享的课程提交应使用角色标签和脱敏引用，审查者仍需能够访问原生记录。

**在运行失败测试前指定测试观察者。**贡献者执行尝试的操作。观察者记录初始状态、结果和最终状态。审查者随后判断证据是否支持相关结论。若角色重叠，应如实披露，不要暗示存在独立认可。

## 隔离运行失败测试

**每个案例之间都要恢复到已验证并经审查的状态。**同时注入来源漂移、访问撤销和运行手册不匹配，会让人难以确定哪个控制拒绝了提案。每次运行只注入一种失败，审查者更容易追溯拒绝原因。

1. **捕获初始状态：**来源版本、配置、交付状态和操作者角色。
2. **注入一种合成情况：**通过获授权的测试途径更改一个相关条件。
3. **尝试有界操作：**验证、读取、发布或交接。
4. **记录观察结果：**实际输出和来源最终状态。
5. **通过审查进行修复：**恢复控制前保留失败证据。
6. **重复成功案例：**确认修正后的流程仍能交付获准的工作。

**计划中的失败仍是一次失败观察。**不要仅因你想测试问题，就把未经授权的发布称为成功测试。测试成功揭示了缺陷，但发布边界失效，必须修复。

**为每个案例填写注入和重置卡片：**为下一行测试使用新的合成提案，或恢复经过审查的基线。观察者记录前置条件并确认重置完成。不得从台账中删除失败尝试。

| 案例 | GitHub-first 注入和检查 | Mixed 工作场景注入和检查 | 下个案例前重置 |
|---|---|---|---|
| 已批准的变更 | 提交固定 PR，取得两项审查，合并并重新打开 `main` | 发布 REQ-17，合并经审查的差异，发布 RUN-04，然后重新打开所有记录 | 将最终版本捕获为下一个基线 |
| 上下文过时 | 捕获清单，然后通过另一项经审查的 PR 更改受保护的测试基线，再验证旧提案 | 捕获页面版本后，让获授权的编辑者在预写入读取前修改测试页面 | 停止操作、比较版本、重新捕获来源并审查新的固定材料包 |
| 未经授权的写入 | 贡献者尝试向受保护的 `main` 直接推送无害变更，并记录服务器拒绝结果 | 贡献者尝试编辑 REQ-17 并转换为 Approved 状态 | 重新读取受保护的提交、页面版本和 Jira 状态，确认均未更改 |
| 冲突 | 在草稿 Issue 中写入六十天，而已批准文件仍写七天 | 在草稿 Jira 中写入六十天，而 REQ-17 仍写七天 | 产品负责人协调草稿内容，并在审查前记录决定 |
| 部分发布 | 批准后、合并或最终回读前停止，并保持 Issue 开启 | 重新读取 REQ-17 后停止，配置和 RUN-04 仍为七天 | 保持交付待处理状态，然后取得负责人审查过的完成或补偿决定 |
| 访问被拒 | 使用被排除在单独私有测试仓库之外的测试身份，并尝试读取其中的合成来源 | 使用被排除的身份访问单独受限的合成页面 | 仅恢复获准的测试访问，并确认普通读者仍能成功访问 |
| 恢复 | 中断一项已批准的测试变更，然后提出经审查的完成方案或还原方案 | 使用部分发布台账提出经审查的完成方案或补偿方案 | 重新读取每个结果来源并核对台账 |
| 交接 | 在不提供旧聊天记录的情况下，将 MAP-01 和台账交给新的审查者 | 在不提供旧聊天记录的情况下，将映射的页面 ID 和台账交给新的审查者 | 审查者打开当前来源并记录下一项获授权的操作 |

每个拒绝案例都要记录平台响应，并再次读取受保护记录。对于被排除用户的案例，应检查提供方支持的工具追踪、检索日志或审计记录，以确认受保护文本没有进入任务上下文。若缺少这类证据，应将此访问安全检查标记为 Blocked，不要把界面上显示的拒绝当成没有返回缓存摘录的证明。如果计划不提供某项控制，或缺少获批测试身份，应记录为 Blocked，不得模拟通过。

## 解读混合结果

**示例证据包：**本地一致性检查通过，产品和运营负责人审查了固定材料包，要求发布成功，但运行手册编辑权限被拒。配置尚未合并。Jira 仍处于 Blocked 状态。

| 声明 | 判定 | 原因 |
|---|---|---|
| **候选记录一致** | 本地检查支持 | 提供的记录通过比较 |
| **负责人接受意图和运营方案** | 需要固定版本的原生审查 | 仅有角色标签并不足够 |
| **三十天交付已完成** | 不支持 | 必需的发布步骤尚未完成 |
| **每个角色的权限边界都有效** | 不支持 | 一项拒绝操作的覆盖范围有限 |
| **恢复负责人应采取行动** | 支持作为下一步 | 部分交付需要经过审查的决定 |

**预期判断：**保持运行未完成状态，验证当前来源，并请求相应负责人的决定。不要通过放宽权限来结束流程，也不要将快照检查描述为实时发布证据。

**已填写的 Mixed 流程教学数据包，仅为合成示例，不代表租户证据：**

```text
Run: MIXED-042-example
Captured base: REQ-17 v4 = 7 days, RUN-04 v2 = 7 days,
  GitHub main base-001 config.json = {"retention_days": 7}, Jira PROP-042 r1 = In Review
Fixed proposal: REQ-17 v5 wording says synthetic exports 30 days,
  excluding production data, backups, and legal holds.
  GitHub config.json changes retention_days from 7 to 30.
  RUN-04 v3 wording says 30 days, no deletion service runs in this lab,
  and incomplete publication stays pending.
Review: product owner approved the exact requirement wording at PROP-042 r1.
  Operations owner approved the exact config diff and runbook wording at r1.
Publication: publisher reopened REQ-17 v5 and read 30 days.
  Maintainer reopened main at merge-002 and read retention_days 30.
  Publisher reopened RUN-04 v3 and read 30 days.
Denied action: contributor tried an edit to restricted REQ-17 from v5.
  Platform denied the edit, the publisher reread v5 unchanged, and the
  observer saved the native denial. No edit was applied and v5 stayed unchanged.
Recovery: after a separate simulated failed RUN-04 attempt, Jira stayed
  Blocked. Operations approved a retry against the current version.
  Publisher reread v3 after the authorized retry before Jira moved to Done.
Handoff: a new reviewer received MAP-01 and the ledger, reopened the three
  sources and Jira, and named the current 30-day state and remaining runtime gap.
Limit: source publication is shown. Actual deletion timing is Not run.
```

在将实时案例标记为 Supported 前，必须用原生记录替换每个示例版本、操作者、拒绝和回读信息。如果计划或角色不允许测试，应将该项标记为 Blocked，并保持两条课程流程未完成。

## 由独立审查者复核

**请审查者重建事件过程**，不要只看结论。他们应能在没有你解说的情况下，找到已批准的基线、固定提案、负责人决定、结果版本、失败尝试、修复记录和剩余缺口。

```text
Reviewer questions:
Which source governs retention intent in this track?
Which exact package did each owner review?
Did any source change after review?
What was published, and what remains pending?
Which denied action was observed under which role?
Did protected text reach an excluded user's context?
Which repair was reviewed and read back?
Does the fresh handoff reconstruct current state independently?
```

**分别评估每项要求。**使用 Supported、Failed、Blocked 或 Not run，并附上证据引用。一致性、批准、权限、恢复和交接是不同的要求。一组本地测试全绿，无法抵消实时发布边界失效。

```text
Run ID and track:
Reviewer role and review date:
Case 01 approved change: status ___ evidence ___ gap ___
Case 02 stale context: status ___ evidence ___ gap ___
Case 03 unauthorized write: status ___ evidence ___ gap ___
Case 04 conflict: status ___ evidence ___ gap ___
Case 05 partial publication: status ___ evidence ___ gap ___
Case 06 access denial: status ___ evidence ___ gap ___
Case 07 recovery: status ___ evidence ___ gap ___
Case 08 handoff: status ___ evidence ___ gap ___
Overall decision: Supported / Failed / Blocked / Not run
Next accountable role and action:
```

**Supported 表示审查者找到了所有适用案例的观察证据。**如果观察到控制失效，记录 Failed；如果缺少访问权限或控制，记录 Blocked；如果尚未尝试，记录 Not run。每项案例的原生引用应保存在对应的命名证据文件中。

**课程通过门槛：**完成 GitHub-first 和 Mixed 两条流程。每条流程中的上述八个适用案例都需要有 Supported 证据。发生边界失效或缺少原生回读时，该流程即受阻。缺少付费计划或测试身份时，应标记为 Blocked，不得猜测通过。只完成一条流程时，应报告为课程部分完成，不得报告为课程已完成。

**脱敏的示例模型材料包，仅供说明：**

```text
Track: github-first | Run: G-01 | Reviewer: separate pilot role
Base: protected commit base-001 | Fixed proposal: PROP-042 r1
Approvals: product review ref P-01, operations review ref O-01
Consistency: local check pass, saved output ref C-01
Permission: contributor direct push denied, native event ref D-01
Publication: merged commit merge-002, fresh clone confirms thirty
Exception: backups and legal holds remain excluded
Recovery: interruption case R-01 read back and resolved through review
Handoff: second reader found current base, exception, and next action
Runtime limit: no production deletion or deployment claim
Decision: Supported for synthetic GitHub-first track only
```

将所有示例引用替换为实际观察到的沙箱产物。Mixed 流程也要用自己的来源版本和审查记录重复完整材料包。审查者应拒绝复制到 Mixed 材料包中的 GitHub 批准。

## 写出有界决策

**有用的结尾决策应指出下一个试点，而不是无限制地推广。**例如，选择另一个合成导出设置，使用相同角色和直接查询路径，同时将真实数据和自动发布排除在范围之外。

| 决策要素 | 所需细节 |
|---|---|
| **范围** | 一项后续变更及其明确排除项 |
| **证据** | 已支持的案例和未解决的失败 |
| **控制措施** | 分别列出平台强制措施和流程要求 |
| **负责人** | 每个剩余缺口的责任角色 |
| **运行时缺口** | 尚未测试的删除或部署行为 |
| **停止条件** | 访问缺失、权威来源变更或未经授权的发布 |

**完成检查：**两份运行材料包都能通过独立重建，适用的失败案例都有观察证据，未解决的控制问题仍清晰可见。如果只完成 GitHub 流程，应报告课程部分完成，不要假定 Mixed 流程表现相同。

## 故障排除和回退

**只有成功路径证据：**重新运行拒绝和中断测试。**角色重叠：**如实披露，并使用不同用户重新测试。**缺少计划控制：**停止并申请已批准的沙箱。

**回退：**通过经审查的 PR 和 Confluence 编辑恢复基线，撤销临时集成，归档 Jira 证据，并在获批准的证据保留期结束后，由负责人批准清理合成数据。保留恢复历史。

## 创建发布决策

```text
Decision: another synthetic pilot, blocked, or rejected
Evidence: both run packages and failure matrix
Unenforced requirements: procedural controls listed explicitly
Provider review: input scope and retention handling
Owner coverage: product, operations, policy, repository, delivery
Production gaps: runtime tests, secrets, deployment, access review
Next action: one bounded follow-up with accountable role
Review date: assigned by pilot owners
```

**预期判断：**合成测试成功支持开展另一个有界试点。生产环境需要单独批准真实数据、部署、提供方处理和运行时行为。助手回答成功不等于获准部署。

## 主要参考资料

- **仓库控制：**[受保护分支](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches)。
- **工作场所访问：**[Confluence 权限](https://support.atlassian.com/confluence-cloud/docs/manage-permissions-on-the-page-level/)。
- **交付控制：**[Jira 权限方案](https://support.atlassian.com/jira-cloud-administration/docs/grant-or-revoke-permissions-in-a-scheme/)。

## 下一步

**返回[课程主页](/ai-collaboration-course-start/)**查看缺少的控制措施。在选择另一个试点前，请将你的实施与[框架文章](/articles/one-source-many-tools-ai-collaboration-framework/)进行比较。
