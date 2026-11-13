---
title: "AI 任务包：更好的提示词与验收标准"
date: 2026-10-10
lastmod: 2026-11-12
toc: true
draft: false
description: "将含糊的 AI 请求整理成任务包，明确结果、来源、文件范围、检查项和停止条件。"
genre: ["人工智能", "效率", "软件工程"]
tags: ["AI 提示词编写", "任务包", "编程代理提示词", "验收标准", "AI 工作流", "AI 代理指令"]
cover: "/img/cover/effective-ai-task-packets.webp"
coverAlt: "将含糊请求改写为简短任务包，并注明来源、范围、检查项和停止条件"
coverCaption: ""
---

[返回实用 AI 工作流课程](/effective-ai-course-start/)

**好的提示词会说明要做什么，以及如何判断结果。** 增加文字无法弥补范围缺失。本课会把含糊请求改写成课程实验所用的任务包。

**学习目标：** 你将编写一个边界明确的任务包，其中包含来源、文件范围、检查项和停止条件。

## 要点

- **结果** 指明所需的产物或行为。
- **范围** 指明允许修改的文件和排除的操作。
- **来源** 标明已批准的要求。
- **验收检查** 让成功变得可观察。
- **停止条件** 防止代理猜测或擅自开展后续工作。

## 开始之前

**准备事项：** 已解压的实验文件、其中的 `docs/requirements.md`，以及[仓库上下文课程](/articles/effective-ai-agents-md-context/)。预留 30 分钟。难度为初级。本练习以一份书面任务包结束。暂时无需修改代码。

## 比较两种请求

**含糊的请求：**“改进任务脚本。”代理可能会重写输出、添加依赖、修改示例数据或跳过测试。请求并未确定这些选择。

**边界明确的请求：**“为 `task_report.py` 添加可选的状态筛选，依据 `docs/requirements.md` 第 1 版。保留默认输出。添加测试。不要修改示例数据。提交前停止。”代理仍可决定实现细节，而任务本身定义了成功标准。

| 任务包部分 | 实验示例 | 检查方式 |
|---|---|---|
| **结果** | 为报告添加 `--status` | 两个允许的值都能正常工作 |
| **来源** | `docs/requirements.md`，第 1 版 | 代码符合已批准的值 |
| **范围** | 仅程序和测试 | diff 不包含其他文件 |
| **约束** | 保留默认输出和示例数据 | 基线输出仍为 `Total tasks: 4` |
| **证据** | 测试命令和手动运行 | 输出符合预期计数 |
| **停止** | 不提交、不推送 | Git 历史和远程仓库保持不变 |

## 使用可复用模板

**复制此模板**，用于小型编程或研究任务。删除无关字段，不要用含糊文字填充它们。

```text
Outcome:
Authoritative source and revision:
Relevant files or records:
Allowed changes:
Excluded changes and actions:
Examples of desired behavior:
Completion checks:
Stop or ask when:
Report back with:
```

**实验任务的完整任务包**如下：

```text
Outcome: Add an optional --status filter to task_report.py.
Source: docs/requirements.md, revision 1.
Relevant files: task_report.py, tasks.json, tests/.
Allowed changes: task_report.py and focused tests.
Excluded: tasks.json, new dependencies, commits, pushes.
Examples: no filter prints Total tasks: 4. Open and done each print 2.
Checks: run unit tests and four manual commands: no filter, open, done, and invalid.
The invalid value must exit nonzero with a clear error.
Stop or ask: source conflict, missing file, unrelated failing baseline.
Report: changed files, commands, observed outputs, unresolved issues.
```

**在 Windows 上，**如果环境使用 Python 启动器，请在任务包中的命令使用 `py -3`。

**任务包不会规定每一行代码。** 它让代理选择小规模实现，同时保证结果可检查。

## 谨慎添加示例

**准确的示例能消除歧义。** `open` 和 `done` 示例规定了所提供的四项任务文件应有的输出。它们不构成适用于所有文件的一般规则。对其他文件，计数取决于其中的记录。

**区分预期结果和实际观察。** 运行程序前，`Total tasks: 2` 是每种状态的预期结果。运行之后，终端输出才是观察结果。如果数值不同，应检查数据和实现，再报告成功。

## 练习设置停止条件

**假设要求文件缺失。** 任务包将该文件列为已批准来源。此时应停止并询问要求，不要从旧聊天或示例问题中推断允许值。

**假设基线测试在修改前失败。** 记录失败，并询问是否先修复初始状态。之后测试通过也无法区分差异来自状态筛选还是起始状态。

**假设代理想要提交更改。** 任务包排除了提交操作。请代理在 diff 和测试完成后停止。你再决定后续提交是否符合项目流程。

## 检查任务包

**每项回答计一分：** 结果是否具体？是否写明依据来源？文件范围是否清楚？是否至少列出两项可观察的检查？是否包含停止条件？低于五分时，应在交给代理前修改任务包。

**你的成果：** 保存最终任务包，并用一句话解释一项停止条件。在下一节实践课中交给编程代理，或在学习路径中手动回答预期结果。

## 检查理解

1. **问题：** 什么让任务包可检查？**答案：** 来源、允许修改的文件、可观察的检查项和停止条件。
2. **问题：** 如果来源缺少必要细节，代理应怎么做？**答案：** 停止并报告缺失细节，不要自行编造。

## 故障排查

- **代理改动过多：** 在任务包中列出文件和排除的操作。
- **代理提问太多：** 提供缺失来源或具体示例。
- **代理过早宣称成功：** 要求提供实际命令输出并检查文件。
- **任务包太长：** 用来源路径和版本替代复制的来源内容。

## 后续步骤

**继续学习[你的第一个编程代理任务](/articles/effective-ai-coding-agent-first-task/)**。使用任务包指导一次小型实验修改。

**课程导航：** [上一课：仓库上下文](/articles/effective-ai-agents-md-context/)，[课程大纲](/effective-ai-course-start/)。
