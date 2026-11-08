---
title: "9 个用于研究、设计和开发的 AI 代理技能项目"
date: 2026-10-06
lastmod: 2026-11-08
toc: true
draft: false
description: "按工作流、宿主支持、依赖项和成本比较九个代理技能项目。了解如何安装、检查和测试所需技能。"
genre: ["人工智能", "开发者工具", "软件开发"]
tags: ["AI 代理技能", "Codex 技能", "Claude Code 技能", "last30days", "Impeccable", "gstack", "Superpowers", "Claude Video", "Humanizer", "NVIDIA SkillSpector", "HyperFrames", "Remotion", "SKILL.md", "代理工作流", "技能安装", "技能安全", "AI 研究", "前端设计", "视频生成", "开发工作流", "代理定制"]
cover: "/img/cover/agent-skill-workflow-library.webp"
coverAlt: "深色桌面上的托盘里放着象牙白说明卡片，旁边有放大镜、色卡和小型胶片卷。"
coverCaption: "任务专用代理技能库的概念插图。"
---
**安装代理技能，改进可重复执行的任务。**研究当前讨论、审查界面设计和渲染视频，需要不同的流程与依赖项。实用技能会为其中一项工作补充缺少的说明、参考资料或脚本。

**有九个项目值得评估：**last30days、Humanizer、Impeccable、Superpowers、gstack、Claude Video、Remotion、HyperFrames 和 NVIDIA SkillSpector。有些项目提供说明集合，有些附带可执行工具，还有些是配套技能齐全的框架。本指南比较它们文档所述的用途，并提供选择、安装和评估技能的实用方法。

**文档快照：2026 年 10 月 10 日。**这些建议依据项目文档和源码检查，不是对输出质量的比较基准。免费安装不代表推理、渲染、数据访问或商业用途免费。

<!--more-->

## 要点

- **从重复任务开始：**选择输出明确且有验收检查的技能。
- **区分技能与运行环境：**安装说明不会安装所有必需的可执行程序。
- **检查宿主：**Claude Code 集成正常，不代表 Codex 或 Cowork 的行为相同。
- **检查权限和依赖项：**软件包命令、钩子、外部服务和凭据都要分别审查。
- **测试后再定制：**以项目规则为准，并记录上游版本。

## 按交付物选择

| 所需输出 | 评估项目 | 首要检查 |
|---|---|---|
| **近期讨论简报** | last30days | 哪些来源提供了可用证据？ |
| **编辑后的文字** | Humanizer | 含义和来源归属是否保留？ |
| **改进后的界面** | Impeccable | 修改后的交互是否正常？ |
| **已规划并测试的改动** | Superpowers | 流程是否符合任务复杂度？ |
| **审查与 QA 工作流** | gstack | 哪些功能适用于你的代理宿主？ |
| **视频观察结果** | Claude Video / Watch | 画面或音频是否支持这些结论？ |
| **React 视频合成** | Remotion 技能 | 导出视频是否与预览一致？ |
| **HTML 视频合成** | HyperFrames 技能 | 跳转到指定时间时动画是否可复现？ |
| **技能检查报告** | SkillSpector | 分析是否完整？标记了哪些问题？ |

**技能不同于代理框架。**技能提供特定任务的指导，有时也附带脚本。代理框架决定代理如何加载说明、调用工具和执行权限。我们的[代理框架比较](/articles/best-ai-agent-harnesses/)介绍了这些配套系统。

**技能文件夹也不等同于插件安装。**插件有时会注册钩子或其他工具，而手动复制文件夹不会包含这些内容。请先阅读所用宿主和安装方式的说明，再判断两者行为是否相同。

## 研究与写作

### last30days

**用 last30days 研究近期讨论。**该[项目](https://github.com/mvanhorn/last30days-skill)汇集 Reddit、Hacker News、YouTube、X 和网络等来源。实际覆盖范围取决于选定来源、已安装工具、身份验证和服务提供方访问权限。它的预检模式会说明计划访问哪些来源并生成哪些文件，但不会开始研究。

**要求提供证据链。**有用的结果应包含日期、链接、反复出现的问题和分歧。不可用的来源应标为覆盖缺口。互动量只反映已收集帖子的活跃度，不代表对所有用户的抽样调查。

**示例任务：**调查近期发布的某个库反复出现的安装故障。按版本和操作系统归类报告，再通过该库的问题跟踪器或文档核实建议的修复方法。不要把流行的临时解决方案当作上游正式支持的方案。

### Humanizer

**把 Humanizer 用作编辑环节。**该[技能](https://github.com/blader/humanizer)针对重复对比、刻意铺垫、夸大表述等写作习惯。它接受语气样例，并力求保留原意。

**提交草稿时同时说明约束。**指出目标读者、必须保留的事实，以及必须继续关联的引文。编辑后，将事实性主张与原文对比。行文更流畅有帮助，但无法证明一项缺乏依据的统计数据正确。

| 写作检查 | 通过标准 |
|---|---|
| **含义** | 主张、限定条件和范围均保持一致 |
| **来源** | 对借用结论的归属说明仍在附近 |
| **语气** | 符合目标读者和提供的样例 |
| **原创性** | 加入独立推理，而非掩饰复制的文字 |

**在不同阶段使用这些项目。**last30days 收集调查材料。Humanizer 编辑表达。两者都不能替代来源核实或独立创作。

## 界面与开发工作

### Impeccable

**用 Impeccable 处理范围明确的设计任务。**其[网站](https://impeccable.style/)和[代码库](https://github.com/pbakaus/impeccable)介绍了设计流程，涵盖评审、字体、布局、清晰度、动效和润色。先提出具体的用户问题，不要笼统要求页面看起来更出色。

**示例设计说明：**让订阅设置页面更容易浏览，同时不隐藏取消订阅选项，也不改变键盘导航。先要求评审，再实施选定的修改。之后检查移动布局、焦点顺序、对比度，以及原始任务是否仍能完成。

**安装方式会影响结果。**当前 Codex 说明区分技能本身和项目本地设计钩子。在 Codex 中，信任钩子需要单独审批。复制技能文件夹并不能证明钩子已启用。

### Superpowers

**用 Superpowers 执行结构化开发流程。**其[代码库](https://github.com/obra/superpowers)打包了构思、规划、测试、调试和审查工作流。它也记录了各宿主的插件安装方式，包括 Codex。

**让流程匹配任务。**涉及数据存储、界面和测试的功能适合先制定明确计划。拼写更正不需要太多流程。明确授权范围，避免通用开发流程把小请求扩展成相邻工作。

**项目规则仍然适用。**技能偏好的测试方法、工作树方式或委派模式，必须符合代码库规范和用户请求。安装一种方法论，不等于授权执行其中描述的所有操作。

### gstack

**用 gstack 执行带有可运行工具的广泛工程流程。**其[文档](https://github.com/garrytan/gstack)包含规划、审查、浏览器 QA、调查和发布类技能。安装时会构建辅助工具，而不只是复制文字说明。

**Codex 支持目前仍属实验阶段。**该项目区分 Claude Code 由钩子强制执行的安全功能，以及 Codex 上的建议行为。不要假设同名命令在不同宿主上具有相同的执行约束。

**我的选择规则：**缺少可重复的开发流程时，试用 Superpowers；当前需求由 gstack 的具体审查或浏览器工具解决时，试用 gstack。如果两者都已安装，每项任务选一个主要工作流，并让另一个只承担明确指定的工作。

| 开发问题 | 有用的评估任务 |
|---|---|
| **范围不明确** | 制定范围受限并含验收标准的计划 |
| **实现脆弱** | 修复预置回归问题并保持现有行为 |
| **交互故障** | 重现浏览器故障并保留证据 |
| **工作流冲突** | 确认只有选定流程在指导任务 |

## 视频证据与制作

### Claude Video / Watch

**用 Claude Video 收集视频证据。**尽管仓库名称中带有 Claude Video，它的 [Watch 技能](https://github.com/bradautomates/claude-video)也支持 Codex 等本地代理。本地流程会下载视频、抽取采样帧，并生成字幕或转录文本。配置单独的 Gemini 路径后，也能将视频发送给模型分析。

**检查当前宿主支持情况。**README 将 Claude Chat 和 Cowork 列为不支持。本地运行需要 FFmpeg、yt-dlp 等媒体工具，各网站也可能限制访问。

**区分视觉与音频结论。**转录文本支持对口语内容的判断。画面帧只支持采样时间点上可见的细节。两者都不能证明采样之间发生了什么。要求提供时间戳和未解决的观察结果，不要笼统声称已理解整段视频。

### Remotion

**用 Remotion 制作以 React 编写的视频合成。**[框架代码库](https://github.com/remotion-dev/remotion)链接到单独的[代理技能集合](https://www.remotion.dev/docs/ai/skills)。该集合涵盖项目创建、标记语言、地图、字幕、Studio 和渲染。安装技能集合不会创建视频项目，也不会安装项目的全部依赖项。

**单独检查许可，不要只看技能下载。**Remotion 的[定价页面](https://www.remotion.dev/docs/license/pricing)说明，个人和不超过三人的公司可使用免费许可。规模更大的组织及特定合作方式需要公司许可。请按自己的用途核对当前条款。

### HyperFrames

**用 HyperFrames 制作基于 HTML 的视频。**其[代码库](https://github.com/heygen-com/hyperframes)介绍了如何把 HTML、CSS、媒体和可定位动画渲染成 MP4。发布的技能会指导合成、预览、验证和渲染。

**从文档指定的核心技能开始。**当前安装指南区分核心技能、较大的已发布集合和仓库内部技能。无差别安装所有文件夹会带入无关说明，并增加维护难度。

| 视频工作流 | 重要验收检查 |
|---|---|
| **Watch** | 带时间戳的观察结果与已检查的媒体一致 |
| **Remotion** | 最终导出保留时间、字体、音频和布局 |
| **HyperFrames** | 跳到某一帧时显示预期画面状态 |

**用受控样例进行选择。**给 Remotion 和 HyperFrames 提供相同的说明、素材、时长和输出尺寸。例如，为一个三步维护流程制作带字幕和一张图表的动画。比较导出文件、编辑工作量和渲染失败情况。一次好看的演示不能证明某个工具普遍更优。

## 检查 SkillSpector

```bash
skillspector scan ./downloaded-skill --no-llm --format json --output report.json
```

**NVIDIA SkillSpector 是扫描器，不是视频或写作技能。**该[项目](https://github.com/NVIDIA/SkillSpector)说明，它能对代理技能包执行静态检查，也支持可选的模型辅助分析。上述命令假设 CLI 已安装，只扫描本地文件夹，不会执行目标技能。

**结合发现结果和覆盖范围阅读报告。**检查被标记的文件及其周边代码，再记录哪些检查已完成。扫描不完整时不能给出干净结论。关键词命中也需要上下文：服务提供方文档中公开的地图令牌，与代码收集无关凭据并非一回事。

**仅静态分析不代表完全离线。**据项目说明，即使使用 **`--no-llm`**，依赖名称和版本仍会发送到 OSV 查询漏洞。启用模型分析后，还会将符合条件的文件内容发送给已配置的服务提供方。请选择适合待审材料的模式。

**把报告作为决策证据。**说明每项发现对目标任务是否必要、哪些数据会离开设备，以及运行环境授予了什么权限。低分不等于安全，项目声誉也无法解释未解决的发现。

## 安装正确的软件包

**先确认技能的规范分发渠道。**Remotion 框架与其技能位于不同代码库。Claude Video 提供名为 Watch 的技能。SkillSpector 以 CLI 安装，代理集成则需单独处理。这些区别说明，克隆项目并不总是足够。

**以下示例命令来自项目当前的安装文档。**只运行所选项目的命令。软件包运行器会下载并执行安装代码，因此运行前应检查上游项目并选择安装范围。

```bash
# Humanizer: user-wide Codex installation
npx skills add blader/humanizer --global --agent codex

# last30days: user-wide Codex installation
npx skills add mvanhorn/last30days-skill -g -a codex

# Remotion: official skill collection, not the framework repository
npx skills add remotion-dev/skills
```

**第三条命令会打开安装流程。**请选择目标代理和安装范围，不要假设默认值与上面明确指定范围的命令一致。插件安装器和独立文件夹安装也有不同的更新机制。

**保留现有安装信息。**替换技能前，检查其版本、本地修改和安装管理器。除非宿主说明如何处理多份副本，否则不要同时在用户、项目和插件目录中保留彼此冲突的版本。

| 安装状态 | 能证明什么 |
|---|---|
| **文件已存在** | 说明和引用资源已就位 |
| **宿主能发现技能** | 代理识别技能名称和描述 |
| **依赖项就绪** | 必需的可执行程序和软件包可用 |
| **任务已验证** | 代表性结果通过独立检查 |

**按顺序验证每个阶段。**成功复制文件夹只能证明安装文件存在，不能证明浏览器、下载、转录或渲染功能正常。把可选服务提供方配置与基础安装分开，并避免将凭据保存在技能文件中。

**每次试用都记录宿主和版本。**注明技能运行在 Claude Code、Codex、Cowork 还是其他宿主中。将上游提交或软件包版本与验收结果一起保存。技能名称相似，不代表发现机制、钩子、权限或工具访问相同。

## 定制前先测试

**用一项已保存任务作为基线。**先在未安装新技能时运行，再在安装后运行。尽可能保持模型、输入、工具和验收标准不变。将失败情况和人工修正与最终结果一起记录。

```yaml
# Illustrative evaluation record, not a skill configuration schema
job: "review a settings page"
input: "same source revision and test data"
variants:
  - "agent without the selected skill"
  - "same agent with the selected skill"
acceptance:
  - "required actions remain visible"
  - "keyboard navigation works"
  - "mobile layout remains usable"
record:
  - "skill source and revision"
  - "model and enabled tools"
  - "completed checks and retained evidence"
  - "elapsed time and manual corrections"
  - "external service usage"
```

**针对反复出现的问题定制，不要改造整个软件包。**如果研究摘要遗漏相互冲突的证据，就增加保留异议来源的要求。如果设计流程更改了既有颜色，就让它参考设计令牌。如果视频字幕溢出，就增加导出分辨率检查。

**让本地补充内容可追溯。**记录上游版本、你的修改和促使你修改的任务。新增触发条件、脚本或依赖项会改变先前评估过的工作流，因此更新后应重新试用。

**留意说明之间的重叠。**开发套件、设计技能和文字编辑器都会表达偏好。发生冲突时，以仓库规则和用户当前请求为准。风格技能不应删除必需的无障碍标签、引文，或只为换词而改写技术术语。

## 构建实用技能库

**从最常重复的任务开始。**写作者可以试用 last30days 和 Humanizer。前端开发者可以从 Impeccable 和一个开发工作流开始。视频制作者应先选择制作框架；如果任务包含源视频分析，再添加 Watch。

**将运行成本与安装成本分开预算。**考虑模型调用、可选搜索服务、转录、媒体生成、渲染基础设施和适用许可。免费代码库只能回答成本问题的一部分。

**首次试用前：**准备获批的模型访问权限、可丢弃的项目或样例输入，以及书面验收标准。基础说明类技能适合初学者。浏览器工具、媒体依赖和云渲染需要更多配置。先预留一小时进行范围受限的试用，再使用有代表性的输入重复测试，之后才将工作流常态化。

**保留经验证有价值的技能。**留下能减少遗漏步骤或审查工作量的技能，删除会带来冲突行为的重复项。代理环境变化时，重新检查宿主兼容性和依赖项。

{{< youtube id="3fdb_giOrLo" enable="true" title="9 个值得立即安装的免费 AI 代理技能" >}}

## 参考资料

- [last30days：研究技能与安装](https://github.com/mvanhorn/last30days-skill)
- [Humanizer：写作技能](https://github.com/blader/humanizer)
- [Impeccable：设计工作流](https://impeccable.style/)
- [Impeccable：代码库与宿主专用设置](https://github.com/pbakaus/impeccable)
- [Superpowers：开发技能](https://github.com/obra/superpowers)
- [gstack：工程工具与宿主支持](https://github.com/garrytan/gstack)
- [Claude Video：Watch 技能与运行要求](https://github.com/bradautomates/claude-video)
- [Remotion：React 视频框架](https://github.com/remotion-dev/remotion)
- [Remotion：代理技能](https://www.remotion.dev/docs/ai/skills)
- [Remotion：许可与定价](https://www.remotion.dev/docs/license/pricing)
- [HyperFrames：框架与技能分发](https://github.com/heygen-com/hyperframes)
- [NVIDIA SkillSpector：扫描器行为与数据处理](https://github.com/NVIDIA/SkillSpector)
- [Futurepedia：9 个值得立即安装的免费 AI 代理技能](https://www.youtube.com/watch?v=3fdb_giOrLo)
