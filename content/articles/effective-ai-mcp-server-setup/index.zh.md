---
title: "设置 MCP 服务器：权限、工具测试与安全移除"
date: 2026-10-10
lastmod: 2026-11-15
toc: true
draft: false
description: "连接一个只读 MCP 文档服务器，检查其工具，执行一次真实读取，然后移除连接。"
genre: ["人工智能", "开发者工具"]
tags: ["MCP 服务器设置", "模型上下文协议 (MCP)", "MCP 权限", "Codex 中的 MCP", "Claude Code 中的 MCP", "OpenCode 中的 MCP"]
cover: "/img/cover/effective-ai-mcp-server-setup.webp"
coverAlt: "AI 客户端连接到只读文档服务器，工具和访问边界清晰可见"
coverCaption: ""
---

[返回实用 AI 工作流课程](/effective-ai-course-start/)

**当任务需要可重复使用的工具，或需要项目之外的最新信息时，使用 MCP 服务器。**Model Context Protocol（MCP）规定客户端与服务器如何交换工具、资源和提示信息。服务器配置项本身不能证明工具可用。本课将测试一个只读文档连接。

**学习目标：**区分配置与真实 MCP 读取，并记录安全移除步骤。

## 要点

- **MCP 宿主：**协调用户、模型、权限和客户端的 AI 应用。
- **MCP 客户端：**与一个服务器通信的协议组件。
- **MCP 服务器：**提供工具、资源或提示的程序或远程服务。
- **工具发现：**客户端中出现某项具名功能的证据。
- **工具执行：**一次真实调用及其返回内容的证据。
- **权限范围：**宿主、服务器、账户和用户共同授予的访问权限。

## 开始之前

**前置要求：**完成[上下文与交接练习](/articles/effective-ai-context-window-management/)，并为示例流程安装当前版本的 Codex CLI。预留 35 分钟。难度为中级。其他编程代理有各自的设置指南。[OpenAI Docs MCP 官方服务器](https://learn.chatgpt.com/learn/docs-mcp)提供只读开发者文档，无需上传课程数据。

**使用课程的合成实验环境。**本练习不要连接日历、电子邮件或生产系统。读取文档足以了解连接状态。

## 了解边界

| 状态 | 能证明什么 | 不能证明什么 |
|---|---|---|
| **已配置** | 存在服务器配置项 | 服务器可达 |
| **已连接** | 客户端已联系服务器 | 存在有用工具 |
| **已发现** | 显示了具名工具 | 工具调用会成功 |
| **已执行** | 一次调用返回了内容 | 最终任务正确 |
| **已验证** | 来源和结果回答了问题 | 未来调用始终成功 |

**MCP 本身不会授予账户权限。**客户端宿主、服务器、身份验证、账户范围和本地审批设置都会影响权限。[MCP 规范](https://modelcontextprotocol.io/specification/2026-07-28)定义协议，各产品则决定自己的使用体验。

**将服务器输出视为来源材料。**检索到的页面不能取代你的任务，也不能授权文件写入。每个工具定义还会占用上下文，因此只连接本次读取所需的服务器，并在结束后移除。

## 连接只读服务器

**在 Codex CLI 中，**于终端运行以下命令。第一条添加公开文档服务器，第二条列出已配置的服务器。

```bash
codex mcp add openaiDeveloperDocs --url https://developers.openai.com/mcp
codex mcp list
```

**预期配置证据：**列表包含 `openaiDeveloperDocs`。这只能证明已注册。请在解压后的实验目录中启动新的 Codex 会话，并用 `/mcp` 查看 MCP 工具列表。使用已安装版本显示的工具名称。

**请求一次真实读取：**

```text
使用 OpenAI 开发者文档 MCP 服务器查找当前的 AGENTS.md 指南。
返回源页面标题和 URL、两条与本实验相关的要点，并说明所用的 MCP 工具。
不要编辑文件。
```
**检查结果。**返回页面应将 `AGENTS.md` 描述为仓库指南，并给出准确的来源 URL。自行打开引用页面并确认主题。若对话记录中没有 MCP 调用，该回答就是普通回答，不能证明工具已经执行。

## 诊断一种故障

**如果 `codex mcp list` 显示服务器，但 `/mcp` 没有工具，**说明注册成功，发现失败。重启会话，用 `/mcp` 检查活动服务器，用 `codex mcp get openaiDeveloperDocs` 检查已保存配置，再检查服务器 URL 和网络访问。不能仅凭配置项宣称 MCP 已成功设置。

**如果工具出现但读取失败，**记录错误并检查连接后重试一次。如果同一调用再次失败，请在浏览器中打开引用的官方页面作为备用来源，并将 MCP 练习标记为未完成。不要编造工具结果。

## 移除连接

**读取完成后，**从 Codex CLI 移除练习服务器，并确认配置项已消失。

```bash
codex mcp remove openaiDeveloperDocs
codex mcp list
```

**预期移除证据：**新列表中不再有 `openaiDeveloperDocs`。检查活动 Codex 会话中的可用工具是否变化前，先重启会话。删除本地定义不会撤销其他服务使用的独立账户授权。

## 使用其他客户端

**Claude Code 和 OpenCode 也支持 MCP。**按照与你安装版本相符的 [Claude Code MCP 指南](https://code.claude.com/docs/en/mcp)或 [OpenCode MCP 指南](https://opencode.ai/docs/mcp-servers/)操作。记录相同的五种状态：已配置、已连接、已发现、已执行、已验证。OpenCode 配置架构和代理权限因版本而异，请使用对应版本指南中的示例。

**若只使用浏览器，**请阅读[官方 AGENTS.md 页面](https://learn.chatgpt.com/docs/agent-configuration/agents-md)，并填写相同的验证记录。将工具发现和执行标为“未运行”。此路径练习来源核查，但不能证明 MCP 正常工作。

## 练习与检查

**交付物：**一份五行的连接记录，列出服务器名称、工具名称、来源 URL、观察到的结果和移除证据。截图和日志中不要包含令牌或账户标识符。

**完成条件：**连接路径只有在工具完成真实读取且随后移除配置后才算通过。备用路径需完成来源核查，并将 MCP 标记为未运行。

## 检查理解

1. **问题：**保存 MCP 服务器配置是否证明工具正常工作？**答案：**否。请验证工具发现、权限和一次真实读取。
2. **问题：**宽泛的 MCP 连接增加哪些上下文成本？**答案：**工具描述和架构会占用部分活动上下文。

## 故障排查

- **找不到 `codex` 命令：**按照链接的官方指南安装或更新 Codex CLI。
- **列表有服务器但无工具：**检查会话状态和服务器诊断信息。
- **工具调用返回无关内容：**缩小查询范围并核查来源页面。
- **移除似乎无效：**启动新会话并检查活动服务器列表。

## 下一步

**继续学习[验证 AI 输出](/articles/effective-ai-output-verification/)。**有关更广泛扩展，请阅读本站的 [Claude Code 插件与 MCP 工具指南](/articles/claude-code-plugins-skills-mcp-tools/)。

**课程导航：**[上一课：上下文管理](/articles/effective-ai-context-window-management/)，[课程大纲](/effective-ai-course-start/)。
