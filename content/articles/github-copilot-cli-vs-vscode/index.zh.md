---
title: "GitHub Copilot CLI 与 VS Code：2026 工作流对比"
date: 2026-10-06
lastmod: 2026-10-10
toc: true
draft: false
description: "比较 Copilot 终端代理与 VS Code 体验，涵盖编辑器上下文、可视化差异、Agent 模式、CLI 集成和账户策略。"
genre: ["开发者工具", "人工智能", "软件开发"]
tags: ["GitHub Copilot CLI 与 VS Code", "Copilot CLI", "GitHub Copilot", "VS Code", "Agent 模式", "CLI 与 GUI", "编辑器上下文", "内联建议", "可视化差异", "Copilot 会话", "终端代理", "GitHub 工作流", "代码审查", "IDE 集成", "MCP 工具", "代理权限", "AI Credits", "开发者工具", "编程助手", "自动化"]
cover: "/img/cover/github-copilot-cli-vs-vscode.webp"
coverAlt: "终端提示符连接到编辑器选择区域和蓝绿色编程工作区中的可视化差异"
coverCaption: ""
---

**GitHub Copilot CLI 和 VS Code 中的 Copilot 为编程工作提供不同入口。** CLI 从 shell 和任务提示开始。VS Code 结合编辑器上下文、建议、聊天和代理工作流。两者都要在相同的账户和仓库策略下评估。

**两种选择并不互斥。** GitHub 记录了 Copilot CLI 与 VS Code 的连接方式。明确连接两者后，终端任务仍能使用编辑器选择和可视化审查。

## 主要结论

- **使用 Copilot CLI 处理终端任务**以及受支持的程序化调用。
- **使用 VS Code 中的 Copilot 处理编辑器中心的工作**，包括内联辅助和 Agent 模式。
- **将 CLI 连接到 VS Code**，以获得带编辑器上下文和差异的终端提示。
- **核实账户、模型和策略设置**，即使它们属于同一产品系列。

**范围和日期：** 官方文档检查时间为 2026 年 10 月 10 日。本页比较独立的 `copilot` CLI 与 VS Code 中的 Copilot，不包括旧的 `gh copilot` 扩展，也不包括分配了 GitHub issue 的云代理。前提是拥有可测试的仓库和获准的 Copilot 访问权限。为试验预留一小时。

## 三种工作方式

| 工作流 | 主要交互 | 适合的试验任务 |
|---|---|---|
| **独立 CLI** | 终端提示和命令输出 | 解释并修复一个可复现的测试失败 |
| **VS Code 集成** | 编辑器选择、聊天、建议和差异 | 修改选定的函数及其测试 |
| **连接到 VS Code 的 CLI** | 带编辑器上下文和审查的终端任务 | 从 shell 调查并可视化检查补丁 |

**混合方式仍然是 CLI 会话。** 在集成终端中运行它，不会自动变成编辑器原生的 Agent 模式对话。检查活动会话和连接，不要只看显示提示符的窗口。

## CLI 提供什么

```bash
copilot
```

**当前的独立命令会启动终端代理。** GitHub 的 [Copilot CLI 概览](https://docs.github.com/en/copilot/concepts/copilot-surfaces/copilot-cli)说明交互式和程序化用法，也说明计划和工具权限。终端输出是主要证据时，适合在此处评估它。

**好的第一项任务应有具体故障。** 提供失败命令、预期行为，以及禁止无关重构的限制。要求代理先复现问题再改文件，并检查最终解释是否符合观察到的测试输出。

**自动化需要明确边界。** 使用 GitHub 的 [CLI 使用指南](https://docs.github.com/en/copilot/how-tos/copilot-cli/use-copilot-cli)了解当前调用和控制选项。在无人值守任务前定义允许的工具、时间限制和输出处理方式。不要把交互式权限策略变成流水线的全面授权。

**沙箱会改变试验边界。** GitHub 记录了针对文件系统、网络和系统限制的本地沙箱，也记录了隔离执行的云沙箱。可信目录提示和批准标志不能替代这些边界。让无害 fixture 先验证沙箱、网络访问和写入范围，再允许真实仓库变更。

## VS Code 增加什么

**Copilot 的 IDE 体验包括建议、聊天和代理任务。** [IDE 概览](https://docs.github.com/en/copilot/concepts/copilot-surfaces/copilot-in-ides)区分这些功能。你仍是主要编辑者时，内联辅助更合适。需要跨文件改动的限定结果适合 Agent 模式。

**Agent 模式会迭代编辑并运行命令。** GitHub 的 [Agent 模式指南](https://docs.github.com/en/copilot/how-tos/copilot-in-your-ide/use-copilot-agents/use-agent-mode?tool=vscode)说明如何在聊天中选择 Agent、审查更改并通过 MCP 扩展工具。可用性和命令批准行为还取决于配置与管理。

**有意识地评估上下文传递。** 选择一个函数，要求解释其错误处理，再要求带独立测试的小改动。记录是否需要提供相邻文件，以及是否需要纠正代理对选中代码的假设。

{{< figure src="copilot-terminal-editor-bridge.webp" alt="终端提示符连接到编辑器选择区域和同一仓库工作区中的并排代码差异" caption="连接的 CLI 会话把终端输入与编辑器审查结合起来" >}}

## 连接两个界面

```text
/ide
```

**在交互式 Copilot CLI 会话中使用 `/ide`**，检查或修改 VS Code 连接。[连接指南](https://docs.github.com/en/copilot/how-tos/copilot-cli/use-copilot-cli/connecting-vs-code)说明可信工作区匹配、编辑器选择共享，以及将拟议文件编辑显示为差异。

**自动连接取决于工作区匹配。** 本地 CLI 不会仅因仓库名称相同就连接远程 Codespace。要在对应环境运行 CLI。宽泛的编辑授权也会绕过拟议编辑的差异批准流程。预期提示消失时检查权限。

**CLI 转录内容会出现在 VS Code 的 Sessions 视图中**，并可通过 Resume in Terminal 继续。这保留了终端工作流，但不要认为对话已变成可互换的原生编辑器代理会话。

| 连接前 | 核实 |
|---|---|
| **工作区** | 目标文件夹已打开并受信任 |
| **执行位置** | CLI 和编辑器集成指向同一环境 |
| **选择区域** | 高亮代码符合当前请求 |
| **权限** | 需要时拟议编辑审查仍保持启用 |
| **会话** | 正在继续目标对话 |

## 模型、计费和策略

**在可用时用同一选定模型测试两个界面。** 如果模型选项不同，记录差异。模型、上下文选择或工具集不同，会让试验超出图形与终端的区别。

**核实账户中的当前用量计算。** GitHub 的 Agent 模式文档提到 AI Credits。不要在未检查当前计费安排前套用旧的高级请求估算。CLI 提示和编辑器任务不自动等价于相同工作量。

**组织访问是前提。** 缺少功能时，先检查策略，再重新安装扩展。记录两种界面获准的工具和集成。提供商登录不会自动授权修改每个仓库或联系每个外部服务。

## 执行配对试验

**准备同一初始修订的两份副本。** 使用匹配的说明和验收测试。第一次在独立 CLI 中执行，第二次在 VS Code Agent 模式中执行。只有混合交互符合日常工作时，才增加连接 CLI 的第三次试验。

| 测量项 | 记录原因 |
|---|---|
| **提供的上下文** | 揭示隐藏的手动准备工作 |
| **正确性** | 区分看似合理的代码和已验证修复 |
| **批准步骤** | 显示相同策略下的监督负担 |
| **审查时间** | 衡量理解完整补丁的时间 |
| **手动修复** | 记录代理完成后的剩余工作 |
| **用量** | 将成本与接受的结果关联 |

**把恢复过程保留在测试中。** 拒绝一个拟议方案并说明原因。观察下一次尝试是否保留有用工作并遵守修正。这比一次不间断演示更能反映日常使用。

## 故障排查和下一步

**如果 CLI 连接到错误的编辑器窗口**，检查 `/ide` 并选择目标工作区。如果可视化批准停止出现，检查宽泛编辑权限。如果 Agent 模式不可用，检查扩展状态和组织策略。

**选择独立 CLI**，当 shell 上下文和可重复调用占主导。**选择 VS Code**，当基于选择的上下文、内联工作和图形审查占主导。**使用连接 CLI**，当终端任务输入和编辑器检查配合良好。

**进行跨供应商比较时**，阅读 [CLI 主比较](/articles/cli-coding-agents-comparison/)或 [GUI 主比较](/articles/gui-coding-agents-comparison/)。将这些评估与本次同系列界面试验分开。
