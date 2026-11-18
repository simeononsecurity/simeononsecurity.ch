---
title: "非编码人员的 GitHub AI 工作流：Issues 与拉取请求"
date: 2026-10-01
lastmod: 2026-11-12
toc: true
draft: false
description: "无需本地开发环境，即可使用浏览器编辑、Issues、聊天上下文包和经过审查的拉取请求。"
genre: ["人工智能", "团队协作", "软件工程"]
tags: ["AI 协作课程", "GitHub 浏览器编辑", "GitHub Issues", "拉取请求", "非编码贡献者", "上下文包", "审查交接"]
cover: "/img/cover/A_group_of_diverse_professionals_collaborating_on_a_cyberse.webp"
coverAlt: "插画展示专业人员在网络安全工作环境中审查共享项目工作"
coverCaption: ""
---

[返回 AI 协作课程](/ai-collaboration-course-start/)

**不编写代码的贡献者也可通过浏览器遵循相同的权限规则。**你在 GitHub 中读取源文件，使用已批准的聊天工具起草内容，然后提交 Issue 或分支编辑。维护者运行检查，并在审查后发布。请在仓库保护已启用后使用此工作流，确保浏览器访问不会绕过编码代理的控制。

## 要点

- **浏览器工作**无需本地终端。
- **上下文包**保留范围和修订证据。
- **Issues 和分支**仍是提案。
- **交接**说明待办事项和下一个角色。

## 开始之前

**前提条件：**[仓库边界课程](/articles/ai-collaboration-github-repository/)、实验室只读访问权限，以及可选的已批准聊天工具。**预计用时：**45 至 60 分钟。**难度：**入门。只提交 Issue 的贡献者可跳过本地 Git 和 Actions。提交 PR 的贡献者应与已完成[代理和 Actions 课程](/articles/ai-collaboration-github-agents-actions/)的维护者协调。

**不使用连接器的基线流程：**自行打开 GitHub，只提供合成摘录。不假设你有聊天订阅功能。如果服务提供商未获批准，请使用相同记录手动起草。

**完成目标：**交接一个 Issue 或 PR，其中包含固定的源修订版、建议措辞、受影响文件、排除项和未解决问题。

## 阅读源材料包

1. **在 `main` 上打开 MAP-01**，然后查找 POL-01、REQ-17 和 RUN-04。
2. **阅读每个来源**，并通过浏览器的提交视图记录其提交修订版。
3. **复制相关的合成内容**，并附上文件名、修订版、范围和例外。
4. 在维护者将其与当前来源比较并准备发布前，**将材料包标记为快照。**

```text
项目: export-service-lab
任务: PROP-042 draft, no publication permission
授权依据: requirement.json, REQ-17 revision 1
基准值: retention_days 7
策略: POL-01 version 1
请求的提案: retention_days 30
证据: attach browser-verified commit references
缺失证据: no runtime deletion observations
输出: proposed wording, affected files, questions, rollback
停止条件: source unavailable, changed revision, conflicting authority
```

**私下附上沙箱中的实际修订版。**模板不含已完成的证据。建议发布前，请助手找出缺失的记录。

**读取实时源文件前填写的合成材料包：**

```text
项目: export-service-lab
任务: draft PROP-042 in an Issue
已批准的基准值: REQ-17 revision 1, retention_days 7
提案: retention_days 30, synthetic export files only
受影响的记录: requirement.json, config.json, proposal.json, runbook.md
排除项: 生产数据、备份和法律保留内容
已知证据: supplied lab baseline files
缺失证据: current main commit, owner decisions, runtime deletion result
状态: Draft, publication blocked until current revisions and reviews exist
下一角色: maintainer supplies verified main commit and runs checks
```

**此材料包已构成完整的提案草稿。**缺失证据一项是刻意保留的。请求发布前，请用实时沙箱修订版替换提供的实验室基线。

## 创建 Issue

**选择 Issues、New issue**，标题填写 **`PROP-042: propose thirty-day synthetic retention`**。粘贴以下说明并附上源材料包。

```text
提案: PROP-042
状态: Draft
当前批准值: 7 days, REQ-17 revision 1
请求值: 30 days
原因: fictional pilot requirement, not compliance advice
范围: synthetic export records only
受影响的文件: requirement.json, config.json, runbook.md
证据: source revisions and policy version attached
审阅者: product-owner and operations-owner
实施审阅者: repository-maintainer
验收: consistent records, denied publication, fresh handoff
回滚: reviewed restoration of the approved baseline
```

**请聊天工具将提案与材料包进行比较，**列出假设并起草面向负责人的问题。将草稿保存到 Issue。不要要求它批准更改，也不要把聊天线程当作决策登记簿。

## 在浏览器中提交编辑

1. **打开仓库的 Code 选项卡。**在文件列表上方打开分支菜单，确认 **`main`**，输入 **`proposal-042`**，然后选择 **Create branch: proposal-042 from main**。如果无法创建分支，请使用已批准的 fork 或下面的 Issue 路径。
2. **打开文件前，在分支菜单中确认 `proposal-042`。**选择文件和铅笔图标进行编辑。GitHub 网页编辑器不会编辑受保护分支。
3. **将需求改为三十天并更新到修订版 2。**每次后续编辑前都重新打开分支菜单。在同一分支中编辑配置和运行手册。
4. **编辑 `proposal.json`**，设置 to_days 30、from_days 7 和 base_revision 1。
5. **预览 Markdown**并检查 JSON 标点。将每次浏览器编辑提交到 **`proposal-042`**。
6. **打开 Pull requests，然后选择 New pull request。**比较 **`proposal-042`** 与 **`main`**，检查四个文件的全部更改，并创建关联 Issue 的 PR。请维护者从受保护基线附加新的清单并运行一致性检查。
7. 在最终提案修订版上**请求负责人审查。**直到审查和回读均成功后，再完成交付。

**导航记录：**写下仓库名称、Issue 编号、提案分支、已更改文件路径、PR 编号、检查运行名称、审查的修订版和最终 `main` 提交。之后可在仓库的 Issues、Code、Pull requests、Actions 和 PR Checks/Reviews 视图中查找。如果 GitHub 移动了某个控件，请根据编号或提交 ID 找到同一记录，不要看着截图猜位置。导出一份私密证据说明，记录各条目的 URL 和观察到的状态。将说明分享给授权团队之外的人员前，删除账户名、电子邮件、令牌、租户标识符和无关仓库数据。未脱敏证据仅保存在批准的私密位置。

**GitHub 文档介绍了通过分支和 fork 贡献的路径。**没有仓库写入权限的贡献者应使用已批准的 fork 或 Issue 路径。Fork 不会授予向原仓库发布内容的权限。

## 检查已完成的 diff

| 文件 | 基线 | 候选版本 |
|---|---|---|
| **需求** | 修订版 1，七天 | 修订版 2，三十天 |
| **配置** | 七天 | 三十天 |
| **运行手册** | `Retention days: 7` | `Retention days: 30` |
| **提案** | 从 7 到 7 | 从 7 到 30，基数为 1 |
| **清单** | 未采集 | 变更前受保护源文件的哈希值 |

**清单描述的是基线**，不是三十天的提议措辞。对候选需求计算哈希并把它称为基线证据，会导致可信基线不匹配。

## 验证与交接

**正向测试：**负责人审查通过且检查成功后，维护者合并更改。打开 **`main`** 上的结果文件并确认一致。将生成的提交和回读结果附加到 Issue。这能证明配置已提交，不能证明运行时删除行为。

**负向测试：**要求聊天工具批准或发布提案。根据策略，它应只返回草稿。另以贡献者身份尝试直接发布，并记录平台拒绝和未变化的源修订版。将行为测试与访问控制测试分开。

```text
交接: HANDOFF-042
提案: PROP-042
策略: POL-01 version 1
来源: attach current requirement, runbook, and config revisions
已发布的值: record after reading main
已完成: merged files and check reference
剩余事项: runtime deletion service not tested
下一角色: operations-owner
下一步操作: independent source read and runbook verification
停止条件: changed source, missing access, conflicting authority
```

**新会话只提供映射和交接记录。**要求重新读取源文件，或明确要求提供浏览器证据。助手应根据源记录重建数值，而不是重复前一个助手的摘要。

## 起草时保留上下文

**浏览器贡献者仍需提出完整的问题。**“请将保留期改为三十天”没有说明当前权威来源、范围、审查状态和受影响记录。向聊天工具提供源材料包和起草指令。如果记录不可用，请维护者提供经授权的证据，不要用记忆中的文字替代。

```text
根据随附的合成资料包，为 PROP-042 起草一个 Issue。
将七天标记为已批准的基准值。
将三十天标记为提案。
保留对生产数据、备份和法律保留数据的排除项。
列出需求、配置、提案和运行手册的变更。
列出缺失的证据，不要用猜测的修订记录填补。
不要声称负责人已批准或交付已经完成。
```

**复制前先检查回答。**确认它有没有更改范围、虚构提交，或把批准描述为已完成。删除未经支持的说法，并在 Issue 中保留未解决的问题。聊天工具帮助撰写提案，不提供它从未读取的系统证据。

## 选择贡献路径

| 情况 | 路径 | 交付物 |
|---|---|---|
| **只有读取权限** | Issue 中包含固定的建议措辞 | 维护者可直接处理的更改请求 |
| **已批准的分支访问权限** | 在单个提案分支中通过浏览器编辑 | 包含相关文件更改的 PR |
| **已批准的 fork 路径** | Fork 后向上游提交 PR | 等待上游审查的候选版本 |
| **无法访问源文件** | 停止并请求经授权的证据 | 明确标记为受阻的任务 |

**通过 Issue 贡献也是完整成果**，不是失败的编程练习。你提供预期更改、证据、范围和审查问题。维护者提供补丁和清单。之后你检查补丁是否符合请求。

| 路径 | 贡献者完成条件 | 交接给维护者 |
|---|---|---|
| **仅 Issue** | Issue 包含已验证的源材料包、固定建议措辞、排除项和开放问题 | 维护者创建分支、运行检查并链接 PR |
| **PR** | 一个分支包含所有受影响文件，PR diff 符合提案，审查者收到最终修订版 | 维护者运行检查、获取负责人审查、合并更改并记录回读结果 |

**通过浏览器编辑时，请留在提案分支。**第一次编辑创建分支后，通过同一分支选择器重新打开其余文件。最后检查 PR diff。创建四个互不相关的分支会得到四项不完整更改，而不是一个可供审查的材料包。

## 检查建议措辞

**不妥措辞示例：**“导出内容现在可以保留三十天。”这句话把交付说成已完成，还漏掉了合成数据范围。审查期间请使用提案表述。

```text
提议意图:
合成导出文件保留 30 天。
排除生产数据、备份和法律保留内容。

当前批准意图:
按照 REQ-17 修订版 1，将合成导出文件保留 7 天。

交付:
尚未发布。未测试运行时删除服务。
```

**根据这段措辞检查每个受影响文件。**候选版本中的需求修订号递增。配置改为三十天。运行手册首行也改为三十，同时保留实验室限制。提案仍将七天标为原值，将修订版 1 标为基线。

**遇到不一致时先提问，不要修改陌生的控件。**如果维护者的补丁还削弱了保护或删除了策略，请要求解释并单独审查。你无需理解每一行工作流，也能识别范围之外的更改。

## 回复审查意见

**审查意见示例：**运营团队要求增加一句说明，配置回滚不会恢复已删除文件。在同一分支上更新草稿，并告知审查者范围已经变化。最终审查必须针对修改后的提案，而不是早先的聊天副本。

| 审查意见 | 贡献者的操作 |
|---|---|
| **缺少排除项** | 恢复相关措辞并请求审查意图 |
| **源修订版过期** | 获取新的授权材料包并协调差异 |
| **缺少清单** | 请维护者采集受保护基线 |
| **无关的控件更改** | 审查前分开或删除该更改 |
| **运行时说法未经测试** | 替换为准确的实验室限制 |

**在问题解决前保持其可见。**只关闭评论而不解决根本问题，会丢失有用信号。在回复中链接修改或证据，让其他审查者无需阅读整段对话也能了解决定。

## 浏览器工作完成检查

**提交 Issue 或 PR，让其他维护者无需猜测即可执行。**其中应包含源材料包、建议措辞、受影响记录、排除项、负责人角色和未解决问题。发布后记录回读结果，并与原始提案分开保存。

**自检：**将材料包交给不了解你聊天内容的人。请他们区分请求值、批准值和发布值。如果合并前他们认为三十天已正式生效，请修正材料包标签。将相同纪律用于工作场所路径。

| 审查关卡 | 通过条件 |
|---|---|
| **源修订版** | 每个引用的提交或页面版本都能在沙箱中打开。未知修订版标记为“缺失”。 |
| **排除项** | 生产数据、备份和法律保留内容不进入提案。 |
| **问题** | 未解决的负责人或源文件问题在 Issue 或 PR 中保持可见。 |
| **批准有效性** | 审查针对最终提案修订版。早先的批准不涵盖后续编辑。 |

**任何关卡失败都会使发布继续等待。**仅创建 Issue 的贡献者将结果交给维护者。PR 贡献者修复后请求重新审查。

## 故障排查与回滚

**没有编辑权限：**使用 Issue 或已批准的 fork。**提交引用是虚构的：**用已验证证据替换，并重新审查草稿。**批准早于编辑：**重新请求批准。

**回滚：**关闭未合并的 PR，同时保留证据。若内容已合并，请维护者准备受保护的 revert 提案。不要更改基线来伪造恢复成功。

## 练习与自测

**不要把需求记录提供给新助手，**然后询问它是否建议发布。

**预期推理：**它会请求权威证据，或将回答标记为基于快照。必须重新读取并成功后，发布才能解除阻止。

## 主要参考资料

- **浏览器步骤：**[编辑文件](https://docs.github.com/en/repositories/working-with-files/managing-files/editing-files)。
- **审查边界：**[受保护分支](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches)。

## 后续步骤

**继续阅读[Confluence 和 Jira 设置](/articles/ai-collaboration-confluence-jira-setup/)**，在工作场所系统中重复应用此工作模式。
