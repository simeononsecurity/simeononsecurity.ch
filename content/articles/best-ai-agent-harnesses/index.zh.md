---
title: "2026 年最佳 AI Agent 框架：按工作流选择"
date: 2026-10-06
lastmod: 2026-11-08
toc: true
draft: false
description: "比较 Deep Agents、Claude Agent SDK、OpenAI Agents SDK、Pydantic AI、Pi 和 LangGraph 的工具执行、记忆、恢复与集成成本。"
genre: ["人工智能", "软件开发", "AI 安全"]
tags: ["AI Agent 框架", "最佳 Agent 框架", "Deep Agents", "Claude Agent SDK", "OpenAI Agents SDK", "Pydantic AI", "Pi 编码 Agent", "LangGraph", "Agent 运行时", "工具调用", "Agent 记忆", "上下文管理", "持久化执行", "Agent 权限", "AI Agent 安全", "本地 AI Agent", "Agent 评估", "人在回路", "Agent SDK 比较", "生产环境 Agent"]
cover: "/img/cover/ai-agent-execution-components.webp"
coverAlt: "深色工作台上，模块化金属部件通过青绿色和橙色路径连接到发光的中央处理器。"
coverCaption: "AI 模型周围各组件的概念插图。"
---

**对于通用 Agent，我会优先评估 Deep Agents，因为它支持配置模型并内置上下文管理。** Claude Agent SDK 适合在应用中嵌入 Claude Code 的执行行为。OpenAI Agents SDK 和 Pydantic AI 值得用于应用专用 Agent。Pi 提供精简且可扩展的核心，LangGraph 则侧重明确的工作流控制。

**最佳选择取决于你打算让系统执行哪些工作。** 研究助手、代码库编辑器和处理客户请求的服务需要不同的工具与恢复规则。这些建议是根据截至 **2026 年 10 月 10 日**查阅的官方文档作出的编辑判断，并非实测性能基准。

<!--more-->

## 关键要点

- **先选抽象层：** 已组装的 Agent、应用 SDK 或工作流运行时。
- **检查执行边界：** 工具审批、文件系统隔离和网络策略解决的是不同问题。
- **测试恢复能力：** 保存对话历史并不能防止重复执行外部操作。
- **衡量被接受的工作：** 成本比较要计入失败、审核时间和基础设施。
- **明确指定模型：** 同时更换模型和 Agent 软件，测量的是完整系统，而非软件本身。

## 框架提供什么

**Agent 框架**是模型调用周围的软件。它准备上下文、提供工具、执行获准操作、把结果交还给模型，并决定继续还是停止。根据具体实现，它还会管理记忆、任务委派、权限和恢复。

**模型**提出下一步动作。**工具**执行操作。**运行时**运行并保存工作流。打包产品可能把这些职责组合起来，但把它们分开有助于找出缺失的能力。

| 组件 | 要问的问题 |
|---|---|
| **上下文管理** | 长时间运行后，哪些要求仍会保留？ |
| **工具执行** | 谁验证参数并限制权限？ |
| **状态存储** | 进程重启后哪些状态仍然存在？ |
| **验证** | 哪些证据能够证明任务已完成？ |

例如，可以设想一个**客服 Agent**收到检查订单并准备更换商品申请的任务。读取订单、提出更换方案和提交申请应拥有不同权限。解释听起来合理，不等于获准提交。保存对话记录，也无法证明申请是否已经提交。

**范围：** 本指南比较可嵌入的软件和运行时。日常开发者界面请参阅独立的[命令行编码 Agent 比较](/articles/cli-coding-agents-comparison/)或[图形界面编码 Agent 比较](/articles/gui-coding-agents-comparison/)。SDK 比较不应悄悄变成终端工具与编辑器扩展的排名。

## 实用候选清单

| 起始需求 | 优先评估的选项 | 你仍需负责的主要工作 |
|---|---|---|
| **通用 Agent** | Deep Agents | 配置后端、权限和模型 |
| **在应用中使用 Claude Code** | Claude Agent SDK | 运行并隔离执行进程 |
| **应用工具工作流** | OpenAI Agents SDK | 定义工具、审批和验收标准 |
| **带类型的 Python 应用** | Pydantic AI 及其 Harness 包 | 选择能力和工作区 |
| **精简的可嵌入编码核心** | Pi SDK | 组装扩展和执行策略 |
| **明确的持久化工作流** | LangGraph | 设计图状态和恢复行为 |

**这些选项的起点不同。** Deep Agents 已经使用 LangGraph，因此选择 Deep Agents 并不一定意味着二选一。Pydantic AI 也把核心 Agent 框架与组装好的 Harness 能力分开。比较你需要自行维护的应用代码量，而不要把每一行都当成可互换的库。

**从满足验收测试的最小层开始。** 对边界清晰的工具调用，使用带类型的应用框架。对开放式文件处理或研究任务，使用已组装的 Agent。如果恢复和状态转换必须明确表达，再考虑工作流图。只有测试证明较简单方案不够时，才添加记忆、Shell 访问或子 Agent。

## Deep Agents：组装好的能力

**如果 Agent 要处理文件、工具和较长对话，可以优先评估 Deep Agents。** 其[官方概览](https://docs.langchain.com/oss/python/deepagents/overview)介绍了文件系统后端、上下文卸载、摘要、子 Agent 和人工审批。它建立在 LangChain 与 LangGraph 运行时之上，并集成多个模型提供商。

**配置仍然决定实际行为。** 当前文档说明，从 0.7 版开始，任务规划需要选择启用。不要假设旧版教程描述了当前默认值。评估时记录软件包版本和已启用的中间件。

**仔细检查权限范围。** 文档中的文件系统规则适用于内置文件工具，不涵盖通过沙箱后端执行的任意 Shell 命令。如果其他执行路径仍能访问同一文件，仅拒绝文件工具请求并不够。要同时测试后端与 Shell 边界。

**我的建议：** 如果文档分析或代码库服务需要组装好的能力和模型提供商选择，可将其列入候选。若任务只有两个定义明确的 API 调用和经过验证的响应，则从更小的方案开始。额外工具会增加需要评估的行为。

## Claude：嵌入式执行

**如果要在应用中使用 Claude Code 的 Agent，评估 Claude Agent SDK。** Anthropic 将其描述为 Python 和 TypeScript 库，使用与 Claude Code 相同的执行循环、工具和上下文管理。SDK 在你负责运行的进程中启动 Claude Code 二进制程序。它不同于 Anthropic 的基础 API 客户端和托管 Managed Agents。[Agent SDK 概览](https://code.claude.com/docs/en/agent-sdk/overview)。

**优势在于复用现有执行系统。** 文件操作、命令、钩子、权限、会话和子 Agent 都作为文档化能力提供。集成由你负责应用边界和针对具体任务的验收检查。

**托管方式仍需由工程团队决定。** Anthropic 的[部署指南](https://code.claude.com/docs/en/agent-sdk/secure-deployment)介绍了文件系统控制、网络限制和隔离。应围绕进程配置这些措施，不要把权限提示当作操作系统边界。

**我的建议：** 如果自动化任务大量涉及文件和命令，可评估它在以 Claude 为中心的文档或编码工作中的表现。如果产品核心需求是比较本地模型和多个托管提供商，则选择支持多提供商的方案。

| 已组装的选项 | 集成重点 |
|---|---|
| **Deep Agents** | 模型选择、中间件和后端配置 |
| **Claude Agent SDK** | 在应用进程中执行 Claude Code |

## OpenAI：应用工具工作流

**如果应用围绕函数、委派任务和明确输出构建，可评估 OpenAI Agents SDK。** 其[概览](https://openai.github.io/openai-agents-python/)介绍了 Agent 循环、交接、护栏、追踪和沙箱 Agent 能力。SDK 面向应用构建者，与 Codex 开发者应用不同。

**审批属于可配置行为。** [人工参与指南](https://openai.github.io/openai-agents-python/human_in_the_loop/)说明了如何中断运行，并序列化状态以便在决策后恢复。对于本地 Shell 和补丁工具，审批默认选择加入。单独添加审批回调并不会启用审批要求。

**模型支持不限于 OpenAI。** [提供商文档](https://openai.github.io/openai-agents-python/models/)介绍了外部提供商的集成接口和适配器。应针对所选端点验证结构化输出、工具调用和传输支持，不要假设功能完全一致。

**我的建议：** 如果有用操作已经封装为定义明确的应用函数，可将此 SDK 列入候选。例如，获取订单、用普通代码计算资格，并准备结构化请求。即使由模型选择下一个工具，也要在应用中保留授权和资格检查。

## Pydantic AI：带类型的应用

**如果 Python 类型和经过验证的输出是应用核心，可评估 Pydantic AI。** 其[核心文档](https://pydantic.dev/docs/ai/overview/)介绍了带类型的工具、依赖注入、结构化输出和持久化执行集成。验证能确认输出符合所需结构，但不能证明每个字段都真实。

**独立的 Harness 软件包提供了组装好的能力。** 其[文档](https://pydantic.dev/docs/ai/harness/)包括 Coder 和 Researcher 技术栈、文件系统与 Shell 访问、记忆和工作区集成。本地工作区与隔离沙箱是不同的执行选择。相关 Harness 能力需要工作区，不会静默替你选择。

**我的建议：** 对返回带类型记录的 Python 服务，优先评估核心框架。只有任务还需要探索工作区或开放式研究时，再增加 Harness 能力。这样可避免让边界明确的数据提取服务无故获得 Shell 访问权限。

以**发票审核 Agent**为例，模式验证可以检查总额是否为数字、币种是否属于允许集合。应用逻辑还要单独核对总额与明细，并验证来源证据。试验中应同时执行这两类检查。

| 应用关注点 | 验收检查 |
|---|---|
| **结构化输出** | 验证字段结构，并独立核实字段含义 |
| **审批暂停** | 持久化确切的待处理操作和决策 |
| **更换提供商** | 重复执行工具调用和输出兼容性测试 |

## Pi：精简且可扩展的核心

**如果要直接控制紧凑型编码 Agent，可评估 Pi 的 SDK。** [项目文档](https://github.com/earendil-works/pi/tree/main/packages/coding-agent)介绍了 SDK、RPC 集成和交互式界面。默认工具集包含读取、写入、编辑和 Shell 执行，可通过扩展添加其他行为。

**精简意味着集成方需要承担更多工作。** Pi 有意省略内置权限弹窗和子 Agent 编排。文档建议通过容器或自定义扩展实现确认流程。这里评估的是嵌入式 SDK，而不是将它的终端界面与其他厂商的图形编辑器比较。

**我的建议：** 如果愿意自行负责执行限制、扩展审查和恢复策略，可将 Pi 列入定制编码服务的候选。它的核心较小，便于理解和修改行为。如果主要需求是现成的审批和编排系统，它就不适合作为首选起点。

## LangGraph：明确的工作流控制

**如果工作流需要明确的状态和转换，可评估 LangGraph。** 其[持久化文档](https://docs.langchain.com/oss/python/langgraph/persistence)区分了线程范围的检查点和跨线程存储。持久化检查点支持进程重启后的恢复，内存检查点则不支持。

**LangGraph 是运行时基础。** 你需要定义工作流，并决定模型驱动行为应出现在哪些环节。Deep Agents 已经使用这一基础，因此当你需要更直接控制执行路径时，再直接使用 LangGraph。

**我的建议：** 对具有明确阶段、审核暂停和不同恢复规则的流程，可将其列入候选。例如，文档接收工作流可以提取字段、验证字段、请求审核，再发布已批准记录。当模型负责选择内容、但不应自行发明业务流程时，固定转换很有用。

| 工作流阶段 | 完成证据 |
|---|---|
| **提取** | 附带来源链接的候选记录 |
| **验证** | 确定性检查和异常情况 |
| **审核** | 针对具体候选记录保存的决策 |
| **发布** | 与该操作关联的外部回执 |

**外部副作用需要单独设计恢复机制。** 保存图状态并不能让远程服务事务与检查点形成原子操作。请使用操作标识符，并在重试提交前核对外部结果。

## 测试缺失的能力

**功能清单只是起点。** 使用接近实际工作负载的故障测试每个候选方案。请使用一次性工作区和包含合成记录的测试服务。

| 测试 | 要保留的证据 |
|---|---|
| **提交中断** | 恢复后只产生一次外部操作 |
| **长对话** | 仍满足原始要求 |
| **拒绝的操作** | 没有通过其他工具产生副作用 |
| **不可信文档指令** | 文档内容不能获得操作权限 |
| **格式错误的工具参数** | 应用修改前先拒绝请求 |
| **预算耗尽** | 停止有明确边界，并能检查部分结果 |

**明确规定重复执行的处理方式。** 对于商品更换申请服务，在测试服务接受请求、但本地尚未保存完成状态时停止工作进程。重启后，工作流应查询操作标识符，而不是盲目再次提交。这是拟议的测试，并非对上述产品进行实测后得出的结果。

**检查上下文压缩后的证据。** 在任务早期加入重要要求，然后提供足以触发配置中上下文策略的真实材料。要求 Agent 提交最终产物和支持来源的引用。[CLM 与 Agent 记忆分析](/articles/context-language-models-agent-memory-hallucinations/)解释了为什么保留笔记与保留准确证据是不同问题。

**检查遥测数据去向。** 工具追踪和记忆存储通常会包含任务数据。记录哪些系统会接收这些数据，以及数据会保留多久。使用本地模型推理，并不代表日志、检索或执行也仅限本地。

## 比较每项验收任务的成本

**使用两条评估路线。** 在可行时，受控比较应固定模型、工具、任务集和预算。部署比较则使用每个候选方案的预期配置。第一种方法能隔离部分软件因素。第二种方法回答哪种完整方案更适合实际工作。

**不要把不受支持的配置强行纳入受控比较。** 如果两个候选方案没有共同的模型或工具接口，应将比较报告为系统评估。记录设置工作量和人工引导。

```yaml
# Illustrative trial record, not a framework configuration file
candidate: "package and pinned version"
model: "provider and exact model identifier"
workspace: "isolated test environment"
task_set: "frozen fixtures and acceptance checks"
limits:
  elapsed_minutes: 15
  model_calls: 30
  tool_calls: 60
record:
  - accepted_result
  - unsupported_claims
  - duplicate_external_actions
  - inference_cost
  - infrastructure_cost
  - human_review_minutes
  - recovery_outcome
```

**每项任务执行多次试验。** 失败尝试仍应计入分母，并在报告百分比的同时提供原始计数。少量试验能揭示故障模式，但不能得出稳定的行业排名。

**成本计算示例：** 方案 A 进行十次尝试共花费 12 美元，产生八项被接受的结果。每项被接受任务的推理成本为 1.50 美元。方案 B 花费 8 美元，但只有四项被接受，因此相应成本为 2.00 美元。这两个数字都不包含人工审核或基础设施费用，应另行记录。

**测试前先确定淘汰条件。** 未经授权的提交或跨用户数据泄露不应被平均质量分数掩盖。落实这些要求后，再比较正确性、恢复能力、审核工作量和成本。

## 做出有边界的选择

**从两个候选方案和一个实际工作流开始。** 对于支持多模型提供商的组装型 Agent，可将 Deep Agents 与更符合应用需求的精简方案比较。要在服务中使用 Claude Code 行为，可试用 Claude Agent SDK。对带类型的应用工作，可比较 Pydantic AI 与 OpenAI Agents SDK。如果愿意承担额外集成工作，可选择 Pi。如果优先考虑明确的工作流控制，可选择 LangGraph。

**试验前提：** 已批准的模型访问权限、合成测试数据、必要时隔离的工作区，以及书面验收标准。先用一个下午完成设置和基本故障测试，再收集多次运行结果后作出生产决策。难度为中级到高级，具体取决于外部操作和恢复要求。

**选择满足要求的最小系统。** 保存测试数据、软件包版本和故障记录。更换模型、上下文策略、工具或执行后端时，重新运行测试。这些变化会改变受评估的系统。

## 参考资料

- [LangChain：Deep Agents 概览](https://docs.langchain.com/oss/python/deepagents/overview)
- [Anthropic：Claude Agent SDK 概览](https://code.claude.com/docs/en/agent-sdk/overview)
- [Anthropic：安全部署](https://code.claude.com/docs/en/agent-sdk/secure-deployment)
- [OpenAI：Agents SDK](https://openai.github.io/openai-agents-python/)
- [OpenAI：人在回路执行](https://openai.github.io/openai-agents-python/human_in_the_loop/)
- [OpenAI：模型与提供商集成](https://openai.github.io/openai-agents-python/models/)
- [Pydantic：AI 框架概览](https://pydantic.dev/docs/ai/overview/)
- [Pydantic：AI Harness](https://pydantic.dev/docs/ai/harness/)
- [Earendil：Pi 编码 Agent SDK 与集成模式](https://github.com/earendil-works/pi/tree/main/packages/coding-agent)
- [LangChain：LangGraph 持久化](https://docs.langchain.com/oss/python/langgraph/persistence)
