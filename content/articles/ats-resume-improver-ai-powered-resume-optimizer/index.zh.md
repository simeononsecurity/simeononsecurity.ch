---
title: "ATS Resume Improver：免费的 AI 简历优化工具"
date: 2026-07-22
lastmod: 2026-11-08
toc: true
draft: false
description: "ATS Resume Improver 是一款免费的开源客户端工具，可借助云端或本地模型分析、评分、匹配、优化并导出简历。"
genre: ["职业工具", "开源项目", "人工智能", "隐私技术", "开发者工具", "求职", "效率"]
tags: ["ATS Resume Improver", "ATS 优化", "简历扫描器", "AI 简历", "OpenAI 简历", "Claude 简历", "Ollama 本地 AI", "自行托管", "隐私优先", "求职工具", "关键词差距分析", "求职信", "简历评分", "React", "TypeScript", "Docker", "Vite", "开源", "PDF 导出", "DOCX 导出", "简历解析器", "职业工具", "面试准备", "薪资估算器", "简历类型检测", "ATS 评分", "免费简历工具", "GitHub", "不收集数据"]
cover: "/img/cover/ai-resume-optimizer-self-hosted-ats-analysis.webp"
coverAlt: "桌上的现代笔记本电脑显示着带图表的彩色简历优化界面，背景为深海军蓝。"
coverCaption: "ATS Resume Improver 完全在客户端分析和优化简历，不收集数据。"
canonical: "https://simeononsecurity.com/articles/ats-resume-improver-ai-powered-resume-optimizer/"
---

**免费、开源并支持自行托管。除非你使用 AI 服务提供商，否则简历不会发送到任何服务器。即使使用 AI，文本也会直接发送给该服务提供商，而不会发送给我们。**

## 什么是 ATS Resume Improver？

**[ATS Resume Improver](https://atsresumeimprover.netlify.app/)** 是一款在浏览器中运行的开源简历优化工具。它会根据职位描述分析简历，帮助你缩小个人经历与申请人跟踪系统（ATS）评估标准之间的差距。该工具使用 React 19、Vite 和 TypeScript 构建。**解析和评分流程完全在浏览器中运行**，没有后端服务器。

源代码位于 **[github.com/simeononsecurity/ats-resume-improver](https://github.com/simeononsecurity/ats-resume-improver)**。你可以使用托管版，也可以一键部署到 Vercel、Netlify、Cloudflare 或 GitHub Pages，或使用 Docker 在本地运行。

### 它解决的隐私问题

大多数简历优化服务会把简历上传到自己的服务器，执行不透明的评分并保留数据。ATS Resume Improver 采用不同方式。

| 模式 | 离开你设备的数据 |
|------|------------------------|
| **不使用 AI 密钥** | 无。所有处理都在本地浏览器中完成。 |
| **OpenAI / Anthropic** | 简历文本和职位描述通过你的密钥直接发送到 AI 提供商的 API。中间没有服务器。 |
| **Ollama（本地）** | 无。模型在你自己的计算机上运行。 |

**API 密钥只保存在内存中**，关闭标签页后就会清除。没有分析、跟踪或 Cookie。

______

## 主要功能

### 不使用 AI 密钥时可用的功能

你无需 API 密钥也能获得有用结果。无密钥模式包括：

- **上传简历**：支持 PDF、DOCX、TXT 或 Markdown
- **提取 ATS 文本**：准确显示 ATS 从文件中读取的内容，包括因格式而丢失的信息
- **简历类型检测**：从 7 种档案中识别与你的简历相符的类型，并相应调整章节顺序
- **章节检测和格式警告**：指出缺失的章节和解析器难以处理的格式
- **ATS 评分（0–100）**，附带 5 个维度的细分结果
- **关键词差距分析**：根据规则与职位描述进行字符串匹配
- **确定性 ATS 优化**：使用本地规则重组内容
- **前后差异查看器**：准确查看所有改动
- **专业 PDF、DOCX、TXT 和 Markdown 导出**

### AI 带来的功能

连接 OpenAI、Anthropic Claude 或本地 Ollama 后，即可使用：

- **语义关键词分析**：理解上下文，而非只匹配字符串。显示匹配强度（强/中等/部分）、匹配位置（“在技能和 3 个工作经历中找到”）、每个关键词的重要程度（关键/高/中/低），并生成 2–3 句 AI 摘要
- **AI 简历优化**：使用 ATS 最佳实践提示词进行完整 AI 改写
- **AI 增强导出**：由 AI 在下载前排版 PDF/DOCX
- **生成求职信**：使用自然化规则消除 AI 写作痕迹（见下文）
- **预测面试问题**：根据职位描述生成
- **估算薪资范围**

______

## 简历类型检测

应用会将简历归入 7 种档案之一，并根据相应职业阶段招聘人员和 ATS 的预期调整章节顺序：

| 档案 | 适用对象 | 章节优先级 |
|---------|----------|-----------------|
| 🏢 **资深专业人士** | 5 年以上，职业经历连贯 | 工作经历 → 技能 → 教育 |
| 🌱 **中级** | 2–5 年 | 工作经历 → 技能 → 教育 |
| 🎓 **初级** | 0–2 年 | 技能 → 教育 → 项目 → 工作经历 |
| 🎒 **学生 / 应届毕业生** | 仍在就读 | 教育 → 项目 → 技能 → 工作经历 |
| 🔬 **学术 / 研究人员** | 博士、发表成果 | 教育 → 研究 → 发表成果 → 工作经历 |
| 📜 **证书为主** | 证书比学位更重要 | 证书 → 技能 → 工作经历 → 教育 |
| 🔄 **转行者** | 检测到职业空档或转向 | 摘要 → 可迁移技能 → 教育 → 工作经历 |

*在优化以及 PDF、DOCX、TXT 和 Markdown 导出中，章节顺序保持一致，而不只是屏幕上的显示顺序。*

______

## AI 语义关键词分析

这正是本工具区别于基础关键词计数器的地方。配置 AI 服务提供商后，关键词差距分析会从简单的字符串匹配升级为语义推理：

| 维度 | 不使用 AI | 使用 AI |
|-----------|-----------|---------|
| **匹配方法** | 只匹配完全相同的字符串 | 语义理解上下文 |
| **匹配强度** | — | 强 / 中等 / 部分评级 |
| **匹配上下文** | — | “在技能和 3 个工作经历中找到” |
| **差距重要性** | 所有差距同等处理 | 关键 / 高 / 中 / 低 |
| **建议** | 通用提示 | 每个关键词的可执行建议 |
| **覆盖率 %** | 根据字符串计数 | 按语义加权 |
| **摘要** | — | 2–3 句 AI 叙述摘要 |

*本地规则分析仍会即时运行。你查看结果时，AI 分析会在后台异步补充。*

______

## 支持的 AI 提供商

所有 AI 调用都包含基于 Harvard OCS 和 Columbia CCE 指南制定的 ATS 最佳实践提示词。

### OpenAI

| 模型 | 适用场景 |
|-------|----------|
| **GPT-4.1 mini**（默认） | 智能、快速且经济，推荐使用 |
| GPT-4o mini | 经典的快速经济选择 |
| GPT-4.1 | 最新 GPT-4.1，准确遵循指令 |
| GPT-4o | 高质量旗舰模型 |
| GPT-4 Turbo | 上下文窗口大 |
| GPT-3.5 Turbo | 速度最快、成本最低 |

**估算费用**：每份简历分析约 0.002–0.05 美元。

### Anthropic Claude

| 模型 | 适用场景 |
|-------|----------|
| **Claude Sonnet 4.5**（默认） | 快速且智能，推荐使用 |
| Claude Opus 4.5 | 能力最强，适合复杂任务 |
| Claude Haiku 4.5 | 速度最快、成本最低 |
| Claude 3.5 Sonnet | 可靠且经过充分测试 |
| Claude 3.5 Haiku | 快速且经济的 3.5 版本 |

### Ollama（本地 / 自行托管）

无需 API 密钥。你可以在自己的硬件上运行模型。设置 `OLLAMA_ORIGINS=*` 以允许浏览器访问。

| 模型 | 备注 |
|-------|-------|
| **Llama 3.3**（默认） | Meta 的最新模型，推荐使用 |
| Llama 3.2 | Meta 模型 |
| Mistral 7B | 快速且能力强 |
| Mixtral 8x7B | 专家模型混合体 |
| Qwen 2.5 | Alibaba Qwen 2.5 |
| DeepSeek R1 | 推理能力强 |
| Phi-4 | Microsoft 模型 |
| Gemma 3 | Google 模型 |

在本地运行 Ollama 可让整个工具完全离线。任何时候都不会有数据离开你的计算机。

______

## 让求职信写得更自然

求职信生成器会应用一套专门的写作风格规则，消除 AI 生成文本的明显特征。该规则集参考了 [Sabrina Ramonov 的自然化写作框架](https://www.sabrina.dev/p/best-ai-prompt-to-humanize-ai-writing)，每封生成的信都会遵守以下要求：

- **不使用 em dash**：完全移除最明显的 AI 写作标志
- **禁用 50 多个词和短语**：leverage、utilize、dive deep、delve、embark、game-changer、groundbreaking、cutting-edge、pivotal、tapestry、harness、moreover、in conclusion、it's worth noting、ever-evolving、landscape、testament、not only...but also 等
- **信件正文不使用 Markdown**：不使用粗体星号、话题标签或分号
- **默认使用主动语态**：只有在动作执行者确实不重要时才使用被动语态
- **必须使用缩写**：“I've”“I'm”“it's”，不能写成“I have”“I am”“it is”
- **句子长短有变化**：短促有力的句子与较长句子交替
- **不使用空洞开场白**：“请注意，X”应直接改为陈述 X
- **第一段包含职位描述中的具体细节**：证明求职信不是套用模板

*这些规则要求模型模仿人的写法，因此生成结果读起来像真人写的。*

______

## 导出质量

| 格式 | 内容 |
|--------|-------------|
| **PDF** | 专业字体、章节分隔线、项目符号和联系信息标题 |
| **DOCX** | 结构规范的 Word 文档（`Packer.toBlob`，兼容浏览器） |
| **TXT** | 间距统一的纯文本，适合 ATS |
| **Markdown** | 带标题和项目列表的 `.md` 结构化文件 |

配置 AI 提供商后，AI 会在下载前排版导出文件，并添加 ✨ AI 增强徽标。

______

## 自行托管选项

### 托管版本（无需设置）

访问正在运行的应用 **[atsresumeimprover.netlify.app](https://atsresumeimprover.netlify.app/)**。无需账户、注册或信用卡。

### 一键云部署

| 平台 | 链接 |
|----------|------|
| **Vercel** | 从仓库一键部署 |
| **Cloudflare Pages** | 一键部署 |
| **Netlify** | 一键部署 |
| **GitHub Pages** | Fork → Settings → Pages → GitHub Actions → 自动部署 |

### 本地开发

```bash
git clone https://github.com/simeononsecurity/ats-resume-improver
cd ats-resume-improver

make install
make dev           # http://localhost:5173
```

### Docker（推荐用于可复现环境）

```bash
# Development — hot-reload on http://localhost:5173
make docker-dev

# Production — nginx on http://localhost:8080
make docker-prod

# Dev + Ollama together (full local AI stack)
make docker-dev-with-ollama
```

### 完全离线的 Ollama 技术栈

```bash
# Start Ollama container (persists models across restarts)
make ollama

# Pull a model
make ollama-pull MODEL=llama3.2

# Start dev app + Ollama side-by-side
make docker-dev-with-ollama
```

打开应用，进入 API 密钥面板，选择 **Ollama (Local)**，将 URL 设为 `http://localhost:11434`，然后选择模型。没有数据会离开你的计算机。

______

## 技术栈

| 层 | 技术 |
|-------|-----------|
| **框架** | React 19 + TypeScript |
| **构建** | Vite 8 |
| **样式** | Tailwind CSS v4 |
| **图标** | Lucide React |
| **PDF 解析** | pdfjs-dist |
| **DOCX 解析** | mammoth |
| **PDF 导出** | jsPDF |
| **DOCX 导出** | docx（`Packer.toBlob`） |
| **AI** | OpenAI · Anthropic Claude · Ollama |
| **容器** | Docker + nginx（多阶段）+ Ollama 服务 |

整个评分和解析流程（`atsAnalyzer.ts`、`keywordMatcher.ts`、`resumeTypeDetector.ts`）都在浏览器中运行。`aiProvider.ts` 中的 AI 集成会从客户端直接调用服务提供商 API，没有代理服务器。

______

## 实用使用指南

### 第 1 步：上传简历

上传 PDF、DOCX、TXT 或 Markdown 文件。切换到 **“What the ATS Sees”** 标签，检查解析器是否正确提取了内容。如果此视图中有章节缺失或文本混乱，招聘人员使用的 ATS 也会遇到同样的问题。

### 第 2 步：粘贴职位描述

将完整招聘信息粘贴到 Job Description 面板。职位描述越完整，关键词分析效果越好。不要删掉要求部分。

### 第 3 步：查看 ATS 评分

评分面板显示 0–100 的总分和 5 个维度的细分结果。细分结果会告诉你重点改进方向：格式问题会降低一个维度，缺失关键词会降低另一个维度，工作经历描述薄弱则会降低第三个维度。

### 第 4 步：检查关键词差距

Keyword Analysis 视图会显示职位描述中的哪些关键词出现在简历中，哪些没有。启用 AI 后，你会获得语义匹配和重要性评级。核心技术技能的“Critical”差距比软技能套话中的“Low”差距更值得关注。

### 第 5 步：优化

- **确定性模式**：应用基于规则的重组。安全、快速且不产生 API 费用。
- **AI 模式**：使用 ATS 最佳实践提示词进行完整的 LLM 改写。

接受改动之前，先查看**前后差异**，了解每项变更。

### 第 6 步：导出

导出为 PDF、DOCX、TXT 或 Markdown。启用 AI 后，导出文件会经过 AI 格式化，以便专业展示。PDF 模板使用适合招聘人员的字体和布局。

______

## 简历技巧集成

工具附带一份配套参考资料 `RESUME_TIPS.md`（也在 GitHub 仓库中），内容包括：

- ATS 系统如何评估简历
- 重要格式规则以及会破坏解析器的格式
- 如何撰写摘要、项目符号和技能部分
- 避免堆砌关键词的策略
- 求职信的语气和结构
- 提交前检查清单

*运行工具前先阅读该文件，了解评分的含义。*

______

## 常见问题

### 工具会保存我的简历吗？

不会。应用完全在客户端运行。任何数据都不会保存到服务器。会话数据保存在浏览器内存中，关闭标签页后就会消失。

### 我的简历得分很低，我应该担心吗？

ATS 分数表示改进方向，而不是通过或淘汰。工具中的 60 分不代表 ATS 会拒绝你的简历，而是表示你的简历与所分析的具体职位描述之间存在可量化的差距。用分数安排编辑优先级，不要把它当作结论。

### 我能否用它分析多个职位描述？

可以。随时粘贴新的职位描述。关键词分析和优化会针对新职位重新运行。每次分析彼此独立。

### Ollama 集成真的能离线运行吗？

可以，只要 Ollama 在你的计算机或本地网络中的设备上运行。应用通过 HTTP 将文本发送到你的 Ollama 实例，不会连接任何外部服务。

### 简历类型检测有多准确？

检测器会根据简历内容应用规则启发式方法，查看提到的工作年限、教育标记、出版或研究章节以及职业空档信号。它适用于大多数简历，但可能不适合特殊职业档案。你始终可以调整它设置的章节顺序。

______

## 项目路线图

正在开发或计划中的功能：

- 通过 IndexedDB 保存简历版本历史
- LinkedIn 个人资料优化器
- 支持 Google Gemini 提供商
- 更多 Ollama 模型

项目采用 MIT 许可证，欢迎提交 pull request。进行重大更改前请先创建 issue。

______

## 结语

**ATS Resume Improver** 填补了一个实际空白：认真分析简历，同时不把你的数据转交给任何人。无密钥模式会立即提供格式和关键词覆盖方面的实用反馈。添加 AI 密钥后，就能启用语义推理、求职信撰写和面试准备，每次分析只需几美分；使用 Ollama 则完全免费。

托管版本位于 **[atsresumeimprover.netlify.app](https://atsresumeimprover.netlify.app/)**。完整源代码位于 **[github.com/simeononsecurity/ats-resume-improver](https://github.com/simeononsecurity/ats-resume-improver)**。

如果你要为自己的求职过程自行托管，或想针对某个行业调整评分权重和提示词，Docker 设置和清晰的项目结构会让 fork 和修改变得简单。

______

## 简历优化课程

如果你需要结构化的分步指南来应用此工具评估的内容，请阅读配套课程：

**[简历优化课程：击败 ATS 系统并获得更多面试机会](/resume-optimization-course-start/)**。课程包含 9 个模块，涵盖 ATS 评分、格式、项目符号、关键词、针对职位调整、求职信和提交前检查清单。将工具与课程配合使用，可在每一步获得即时反馈。

______

## 参考资料

1. [ATS Resume Improver — 在线工具](https://atsresumeimprover.netlify.app/)
2. [ATS Resume Improver — GitHub 仓库](https://github.com/simeononsecurity/ats-resume-improver)
3. [简历技巧 — RESUME_TIPS.md](https://github.com/simeononsecurity/ats-resume-improver/blob/main/RESUME_TIPS.md)
4. [Sabrina Ramonov — 让 AI 写作更自然的最佳提示词](https://www.sabrina.dev/p/best-ai-prompt-to-humanize-ai-writing)
5. [OpenAI API 文档](https://platform.openai.com/docs/)
6. [Anthropic Claude 文档](https://docs.anthropic.com/)
7. [Ollama — 本地 LLM 服务器](https://ollama.com/)
