---
title: "使用本地模型运行 Claude Cowork 和 Claude Code：2026 设置指南"
date: 2026-09-22
lastmod: 2026-11-12
toc: true
draft: false
description: "通过兼容 Anthropic 的 API 配置 Ollama 与 Claude Desktop、Claude Code。了解 2026 年的模型选择和云端专属功能。"
genre: ["本地 AI", "AI 编程工具", "自托管 AI", "开发者工具", "隐私", "开源模型", "自动化", "AI 硬件"]
tags: ["claude cowork", "claude code", "claude desktop 本地模型", "ollama claude code", "anthropic base url", "anthropic_auth_token", "claude code 本地模型", "离线运行 claude", "本地 AI 编程代理", "ollama launch claude", "claude desktop ollama", "本地 llm 编程", "私有 AI 编程", "离线 AI 编程", "本地 AI 代理", "qwen3.8", "glm 云模型", "工具调用模型", "配置 claude code", "免费 claude code", "无需 API 密钥运行 claude", "本地模型上下文窗口", "llama.cpp", "ollama cloud", "AI 编程隐私", "隔离网络的 AI", "devops AI 工具"]
cover: "/img/cover/claude-cowork-setup-guide-local-models-2026.webp"
coverAlt: "现代工作区中的电脑显示编程界面，旁边有平板电脑和智能音箱，背景为深蓝色并带有彩色发光点缀。"
coverCaption: ""
ref: ["/articles/local-ai-2026-build-your-rig-now", "/articles/ai-models-raspberry-pi-4-5"]
---

**Claude 的代理工具现在可以调用你自己硬件上的模型，无需 API 密钥或订阅，也不会把数据发送到设备之外。** Ollama 提供兼容 Anthropic 的 API，Claude Code 和 Claude Desktop 只需几条命令即可连接。

*许多指南漏掉了一个关键细节。它们介绍 Claude Cowork，随后却给出配置命令行工具的步骤。这是两种不同的集成方式，只有一种支持 Cowork。*

本指南分别介绍两种方式、常见教程遗漏的环境变量、2026 年 9 月适用于各方式的模型，以及无论如何配置都只能在云端使用的功能。

**读完后，你将能够：**确定需要哪种集成，通过 Ollama 文档中的路径完成连接，并用一次工具调用测试确认端点。只有选择本地模型并避开云端功能时，本地推理才会让模型请求留在设备上。

## 简短答案

**Ollama 有两种不同方式连接 Claude。选错方式后，终端虽然能用，却无法使用 Cowork，这是最常见的问题。**

| 集成方式 | 可用功能 | 设置路径 | 平台 |
|---|---|---|---|
| **Claude Desktop** | Cowork、子代理、网页搜索、自动模式 | Ollama 应用，然后选择 **Apps** 和 **Connect Claude** | **仅 macOS** |
| **Claude Code** | 支持工具调用和文件编辑的 CLI 编程代理 | `ollama launch claude` 或环境变量 | macOS、Linux、Windows |

**需要 Cowork 时，请使用 Claude Desktop 集成。** 此方式在 Ollama 应用中通过图形界面配置，目前仅支持 macOS。文档仍将 Windows 支持列为即将推出。

**需要终端代理时，请使用 Claude Code。** 一条命令即可启动。

*两者都免费。成本只有硬件和电费。*

## 两种集成方式

名称容易造成混淆。**Claude Cowork 是 Claude Desktop 中的一项功能**，既不是独立应用，也不是 Claude Code 的别称。

Ollama 文档在不同页面和栏目中分别介绍它们。Claude Desktop 位于 **Assistants** 下，与 OpenClaw 和 Hermes 并列。Claude Code 位于 **Coding** 下，与 OpenCode、Cline 和 Codex CLI 并列。

这一区别很重要，因为两者的设置完全不同：

- **Claude Desktop** 通过 Ollama 应用界面配置，无需修改 shell 配置文件。
- **Claude Code** 通过环境变量或单条启动命令配置。

如果指南要求你导出 `ANTHROPIC_BASE_URL`，然后运行 `claude`，它配置的是命令行工具。如果你期待的是 Cowork 桌面体验，**配置没有出错。你设置的是另一个产品。**

## 设置 Claude Desktop 和 Cowork

此路径使用 Ollama 应用，而不是终端。

### 前提条件

- 在 macOS 上**安装 Ollama**。文档将 Windows 支持列为即将推出。
- 如果要本地运行，先**下载一个模型**。使用云模型时，登录 Ollama 并启用云模型。部分模型需要付费计划。
- **安装 Claude。** 如果尚未安装，Ollama 会在设置过程中提供下载选项。

### 操作步骤

1. 打开 Ollama 并选择 **Apps**。
2. 选择 **Connect Claude**。
3. 按照设置提示操作。出现提示时安装 Claude，并按要求重启。

整个流程就是这些步骤。以后要更换模型时，打开 **Ollama Settings**，进入 **Apps**，选择模型，然后点击 **Restart Claude**。

### 支持的功能

Ollama 文档列出了此集成支持的四项功能：

- **Cowork**，用于完成复杂任务
- **Subagents**，用于把大型任务拆分给多个代理
- **Web search**，默认由 Ollama 提供
- **Auto mode**，由代理决定何时在修改前征求许可

*列表中包含 Cowork。这项功能由此集成提供，命令行集成不支持。*

### 断开连接

断开连接会恢复 Claude 之前的配置，因此此操作不会造成破坏。

- 在界面中打开 **Apps**，断开 Claude，然后按提示重启。
- 在终端中运行 `ollama launch claude-desktop --restore`。
- **Claude 连接期间退出 Ollama，也会恢复 Claude 的常用配置。** 如果要保留本地设置，请让 Ollama 保持运行。

{{< figure src="claude-desktop-ollama-integration-flow.webp" alt="示意图展示 Ollama 应用通过 Apps 面板连接 Claude Desktop、在 Ollama 设置中选择模型，以及恢复原始配置的路径" >}}

## 从 CLI 设置 Claude Code

几乎所有指南都会介绍此方式。对于终端工作，这是合适的选择。

### 一条命令设置

```bash
ollama launch claude
```

此命令会设置所需的环境变量，将 Claude Code 指向本地 Ollama 实例并启动程序。从列表中选择模型，然后按 Enter。要提前指定模型，请添加参数：

```bash
ollama launch claude --model qwen3.5
```

*包装命令会处理环境设置。仍建议阅读下一节，了解这些设置有助于之后排查问题。*

### 手动设置环境变量

```bash
export ANTHROPIC_AUTH_TOKEN=ollama
export ANTHROPIC_API_KEY=""
export ANTHROPIC_BASE_URL=http://localhost:11434

claude --model qwen3.5
```

**许多常见指南漏掉第二行。** 将 `ANTHROPIC_API_KEY` 设为空字符串，可以避免环境中已有的真实密钥干扰本地连接。已发布的指南如果省略此行，已经导出密钥的读者会遇到难以理解的错误。

如果不想修改 shell 配置文件，请将所有值直接写在命令中：

```bash
ANTHROPIC_AUTH_TOKEN=ollama ANTHROPIC_BASE_URL=http://localhost:11434 ANTHROPIC_API_KEY="" claude --model kimi-k2.7-code:cloud
```

官方文档中还有两点值得了解：

- **`ANTHROPIC_AUTH_TOKEN` 保存 bearer 身份验证信息**，因此本地模式下其字面值为 `ollama`。
- **Claude 自己的设置文件优先于 shell 变量。** 导出新值后如果连接异常，请检查这些设置，然后在 Claude Code 中运行 `/status`，查看当前使用的端点。

### 直接连接 Ollama Cloud

此路径无需安装 Ollama。设置 API 密钥，并将 Claude Code 指向 Ollama 托管的端点：

```bash
ANTHROPIC_BASE_URL=https://ollama.com \
ANTHROPIC_AUTH_TOKEN="$OLLAMA_API_KEY" \
ANTHROPIC_API_KEY="" \
claude --model glm-5.3-flash
```

**此路径有一项限制。** Ollama 文档指出，托管式网页搜索和高级工具控制尚未得到完整支持。兼容模型仍可用于基本聊天、文件编辑和工具调用。

## 2026 年 9 月的模型选择

2026 年的模型阵容变化很大，春季发布的建议值得重新检查。

| 模型 | 类型 | 上下文 | 选择理由 |
|---|---|---|---|
| **Qwen3.8 27B** | 本地，18 GB | 256K | 当前出色的本地通用模型，支持视觉、工具调用和思考控制 |
| **Qwen3 Coder Next** | 本地，MoE 总计 80B / 激活 3B | 256K | 为持续运行的编程代理设计，支持更快的非思考模式 |
| **Qwen3.6 35B A3B** | 本地，MoE 35B / 激活 3B | 262K | Apache 2.0 许可，在内存有限时效率较高 |
| **kimi-k2.7-code:cloud** | 云端 | 大 | 面向编程的云模型，无需本地硬件 |
| **glm-5.3-flash** | 云端 | 大 | Ollama 自家文档首先推荐的模型 |

**内存充足时，从 Qwen3.8 27B 开始。** 它可在本地运行，支持 256K 上下文窗口、原生视觉、工具调用，以及按请求切换的思考模式。显存至少 24 GB 的显卡适合日常使用。

**内存不足时，从云模型开始。** 使用托管模型试用 Claude Code 无需付费，也不需要考虑硬件，但代码会离开本机。

### 关于三值模型的警告

我们的**[本地 AI 指南](/articles/local-ai-2026-build-your-rig-now/)**介绍了三值 Bonsai 2 27B，它能在 **5.53 GiB** 内存中运行完整的 27B 模型。这里也很容易想到用它。

**此工作流无法运行它。** 三值内核位于 Prism ML 的 llama.cpp 分支中，标准 Ollama 无法加载这些文件。运行 `ollama launch claude --model Ternary-Bonsai-2-27B` 之类的命令，会在推理开始前失败。Claude Code 请使用标准 Qwen3.8 27B 包，将三值包留给兼容的运行时。

*便利性和最高效率在这里需要不同的选择。集成工具需要标准 GGUF 文件。*

## 先将上下文设为 64K，再判断模型表现

Ollama 文档针对代码仓库提供了一项明确建议：选择模型并**将上下文窗口设为至少 64K**，大型仓库还应继续调高。

Claude Code 会把文件内容、差异和命令输出放进上下文窗口。默认值太小时，任务执行到一半就会耗尽空间。这看起来像推理能力不足，实际原因是设置不当。

| 上下文 | 适用场景 |
|---|---|
| 低于 32K | 单文件编辑和快速提问 |
| **64K** | 中小型仓库中的多文件工作 |
| 128K | 较大仓库和较长命令输出 |
| 256K | Qwen3.8 27B 的完整窗口 |

*Claude Code 如果在任务中途失去上下文，先检查上下文设置，再考虑更换模型。*

## 用一条命令验证工具调用

工具调用是代理与文本生成器的区别。应先验证它是否工作。

Claude Code 启动后，向它提出请求：

```text
读取当前目录并列出所有文件
```

**如果它列出真实文件，说明工具调用正常。** 如果它说自己会读取目录，却只能描述预期内容，说明工具调用没有接通。你面对的是附带编程提示的聊天模型，而不是代理。继续修改提示词无法修复此问题。

按以下顺序排查：

1. **换成已确认支持工具调用的模型。** 并非所有模型都支持，参数数量也看不出这一差别。
2. **确认环境指向 Ollama。** 运行 `ollama --version`，并检查 `ANTHROPIC_BASE_URL` 是否指向本地端点。
3. **在 Claude Code 中运行 `/status`。** Claude 设置文件中的基础 URL 或凭据优先于刚导出的 shell 变量。

## 仍仅限云端的功能

围绕本地推理重建工作流之前，先了解这些界限。

| 功能 | 本地模型 | 云端 |
|---|---|---|
| 聊天和文件编辑 | 支持 | 支持 |
| 工具调用 | 取决于模型 | 支持 |
| 子代理 | 支持 | 支持 |
| 网页搜索 | 由 Ollama 提供 | 支持 |
| **Cowork** | 通过 Claude Desktop 集成 | 支持 |
| 自动模式 | 通过 Claude Desktop 集成 | 支持 |
| 定时提示 | 通过 Claude Code 中的 `/loop` | 支持 |

本地使用有三项限制：

- **多文件推理能力会先于速度下降。** 本地模型能较好地处理一个文件，处理三个文件尚可，但处理整个仓库较弱。应据此确定任务规模。
- **部分云模型需要 Ollama 付费计划。** 你还需要登录并启用这些模型。
- **直接使用云端时功能受限。** 跳过本地安装后，托管式网页搜索和高级工具控制无法获得完整支持。

*本地推理适合范围明确且可验证的工作，不适合大范围、定义模糊的任务。规划时要考虑这一界限。*

## 自动化

两项功能让使用方式不止于交互会话。

### 在脚本和 CI 中无界面运行

`--yes` 参数会跳过交互选择，并在需要时拉取模型。它需要 `--model`，而 `--` 后的内容会直接传递给 Claude Code：

```bash
ollama launch claude --model gemma4:cloud --yes -- -p "how does this repository work?"
```

**留意权限模型。** Claude Code 大多数操作前都会询问确认，因此无界面运行需要预先配置权限规则或隔离环境。不要让无人监督的代理操作重要仓库。

### 使用 `/loop` 安排提示

在 Claude Code 会话中，`/loop` 会按指定间隔运行提示或斜杠命令：

```text
/loop 30m 检查我未完成的 PR 并总结其状态
/loop 1h 搜索最新 AI 新闻并总结重要进展
/loop 15m 检查新的 GitHub 问题并按优先级分类
```

*会话保持打开时，该命令才会运行。它不是后台守护进程，会随会话关闭而停止。*

## 故障排查

| 现象 | 可能原因 | 解决方法 |
|---|---|---|
| **连接被拒绝** | Ollama 未运行 | 运行 `ollama serve`，并使用 `curl http://localhost:11434/api/tags` 确认 |
| **只描述操作，不实际执行** | 所选模型不支持工具调用 | 换成已确认支持工具调用的模型 |
| **使用了真实 API 密钥，而非本地端点** | `ANTHROPIC_API_KEY` 仍处于导出状态 | 按上文所示将其设为空字符串 |
| **设置后找不到 Cowork** | 配置的是 Claude Code CLI，而不是 Claude Desktop | 使用 Ollama 的 **Apps** 流程启用 Cowork |
| **生成速度慢** | 上下文设置过大，或选了稠密模型而非足够用的稀疏模型 | 降低上下文，然后尝试混合专家模型 |
| **导出的变量没有效果** | Claude 设置文件优先于 shell 变量 | 检查设置文件，然后运行 `/status` |
| **后台请求失败** | Claude Code 为内部任务改用小模型 | 将小模型覆盖设置指向同一本地模型 |

*七项问题中有两项源自同一原因。大多数设置问题来自端点错误或模型不支持工具调用。*

## 要点

- **Claude Desktop 和 Claude Code 是两种独立集成。** Cowork 位于 Claude Desktop 中，可在 macOS 上通过 Ollama 的 **Apps** 面板设置。CLI 路径不提供 Cowork。
- **启动 CLI 只需一条命令：** `ollama launch claude`。手动配置需要三个变量，**许多指南漏掉了 `ANTHROPIC_API_KEY=""`**。
- **不需要本地安装。** 使用 API 密钥将 Claude Code 指向 `https://ollama.com`。
- **评估模型前先将上下文设为至少 64K。** 窗口太小会让模型看起来像是推理失败。
- **通过一次请求验证工具调用。** 如果模型只描述自己会怎么做，你使用的是文本生成器，而不是代理。
- **三值 Bonsai 包在这里无法运行。** 它们需要 Prism ML 的 llama.cpp 分支，标准 Ollama 无法加载。
- **断开连接是安全的。** 退出 Ollama 会恢复 Claude 的先前设置，也可以在终端运行 `ollama launch claude-desktop --restore`。

## 后续步骤

1. 配置 Claude 之前，**安装 Ollama 并下载已确认支持工具调用的模型**：**[Ollama 模型库](https://ollama.com/library)**
2. **阅读 Ollama 的 Claude Code 页面**，查看当前参数和模型：**[Claude Code 集成](https://docs.ollama.com/integrations/claude-code)**
3. 需要 Cowork 时，**查看 Claude Desktop 页面**：**[Claude Desktop 集成](https://docs.ollama.com/integrations/claude-desktop)**
4. **购买硬件前先确定需求**，参考本地推理指南中的内存等级：**[2026 年本地 AI：27B 模型胜过 Sonnet 4.6](/articles/local-ai-2026-build-your-rig-now/)**
5. 如果要在低功耗设备上运行常驻代理，**查看小型硬件能处理哪些工作**：**[哪些 AI 模型可在 Raspberry Pi 4 或 5 上运行？](/articles/ai-models-raspberry-pi-4-5/)**

## 相关文章

| 文章 | 内容 |
|---|---|
| **[2026 年本地 AI：27B 模型胜过 Sonnet 4.6](/articles/local-ai-2026-build-your-rig-now/)** | 本地推理基准、三值量化和硬件选择 |
| **[哪些 AI 模型可在 Raspberry Pi 4 或 5 上运行？](/articles/ai-models-raspberry-pi-4-5/)** | 适用于小型常驻助手的本地推理 |
| **[为 Meshtastic 构建保护隐私的 AI 助手](/articles/building-a-privacy-preserving-meshtastic-ai-assistant/)** | 驱动离网无线设备的本地模型，以隐私为重点 |
| **[AI 开发必备 VS Code 扩展](/articles/best-visual-studio-code-extensions-for-ai/)** | 可与本地编程代理搭配的编辑器工具 |

## 参考资料

1. [Claude Code 集成 - Ollama 文档](https://docs.ollama.com/integrations/claude-code)
2. [Claude Desktop 集成 - Ollama 文档](https://docs.ollama.com/integrations/claude-desktop)
3. [Ollama 模型库](https://ollama.com/library)
4. [Qwen3.8 - Ollama 模型库](https://ollama.com/library/qwen3.8)
5. [使用本地模型运行 Claude Cowork - PromptSpace](https://www.promptspace.in/blog/how-to-use-claude-cowork-with-local-models-2026-guide)
6. [Prism ML 的 llama.cpp 分支 - 三值内核](https://github.com/PrismML-Eng/llama.cpp)
