---
title: "AI 工作流课程设置：终端、Git 与练习实验室"
date: 2026-10-10
lastmod: 2026-11-15
toc: true
draft: false
description: "准备安全的 AI 练习环境，学习课程中的终端和 Git 术语，并运行入门实验室。"
genre: ["人工智能", "软件工程", "教育"]
tags: ["AI 课程设置", "终端基础", "Git 基础", "编程代理前置条件", "AI 练习实验室", "初学者 AI 课程"]
cover: "/img/cover/effective-ai-course-setup.webp"
coverAlt: "初学者练习环境，包含终端、Python 和 Git 图标、已勾选的实验室文件夹以及重置存档"
coverCaption: ""
---

[返回实用 AI 工作流课程](/effective-ai-course-start/)

**使用代理前，先准备一个安全的练习空间。** 第 1 和第 2 课可在浏览器中完成，无需此实验室。如果要学习完整课程，请在第 3 课前回到这里。编程实践课需要 Git、Python 3.10 或更新版本，以及一个编程代理。学习路线会用标记的手动任务替代不可用的代理操作。

**学习成果：**你将运行入门实验室、保存本地基线，并说明如何重置一次性副本。

## 要点

- **浏览器路线：**在 ChatGPT 或 Claude 中完成聊天、规划、来源核验和审查练习。
- **本地路线：**使用终端和随附的 Python 实验室完成编程练习。
- **重置路线：**练习出错时，重新解压一份实验室副本。
- **安全规则：**私人文件、客户记录和凭据应留在实验室之外。

## 选择路线

| 路线 | 所需条件 | 练习内容 |
|---|---|---|
| **浏览器入门** | 当前浏览器和 ChatGPT 或 Claude 账号 | 第 1、2 课，以及第 1 课的聊天任务包 |
| **本地实践** | Git、Python 3.10 或更新版本、终端和一个编程代理 | 文件、差异、测试和代理修改 |
| **自学课程** | 浏览器、本地 Python 3.10 或更新版本以及 Git | 完整实验室检查；不可用的代理和 MCP 步骤标记为未运行 |

**各产品自行设定套餐和限制。**依赖某项功能前，请查看 [ChatGPT Projects](https://help.openai.com/en/articles/10169521-projects-in-chatgpt) 和 [Claude Projects](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects)。自学路线无法证明你已掌握不可用编程代理的实操技能。请在完成记录中注明此区别。

**采用一条默认路径：**用浏览器中的 ChatGPT 完成聊天练习，再用本地实验室配合一个可用的编程代理。Claude 可作为同等的聊天选择。编程阶段可选 Codex CLI、Claude Code CLI 或 OpenCode。你不必注册所有供应商的账号。

**打开编程代理前，记录五项预检信息。**这有助于区分本地实验室检查与对账号或托管工作区的声明。

| 检查项 | 记录内容 |
|---|---|
| **工作区** | 代理将读取的实验室解压目录的准确路径 |
| **执行位置** | 本地计算机或选定的远程工作区 |
| **提供方** | 此任务使用的账号或模型提供方 |
| **权限** | 是否允许写入文件和执行 shell 命令，或是否需要审批 |
| **基线** | 修改前观察到的数量和两项通过的测试 |

**缩小练习根目录范围。**托管工作区需要自己的合成实验室副本。本地运行无法证明远程副本或账号拥有相同文件和权限。

## 学习本地术语

| 术语 | 简明解释 |
|---|---|
| **终端** | 输入命令的应用程序 |
| **Shell** | 解释这些命令的软件 |
| **CLI** | 程序的命令行界面 |
| **工作目录** | 命令默认使用的文件夹 |
| **仓库** | 由 Git 跟踪的项目 |
| **提交** | 已保存的 Git 快照 |
| **分支** | 一条命名的 Git 更改线 |
| **差异** | 显示新增或删除行的内容 |
| **测试** | 可重复执行的预期行为检查 |
| **退出代码** | 表示命令成功或失败的数字 |

**入门实验室不需要 GitHub。**Git 在你的计算机上运行。GitHub 是单独的托管服务。本地提交会保存快照，不会把文件发送到其他地方。

## 准备实验室

**下载[课程入门实验室](/downloads/effective-ai-course-lab.zip)**，并解压到由你控制的新文件夹。打开该文件夹中的终端。在 macOS 或 Linux 上，打开 Terminal 并用 `cd` 进入解压目录。在 Windows 上，使用 PowerShell 或 Windows Terminal 并运行 `cd`。Windows 上的 Python 命令通常是 `py -3`，而不是 `python3`。

**如有需要，安装 [Python 3.10 或更新版本](https://www.python.org/downloads/) 和 [Git](https://git-scm.com/downloads)。**运行实验室前先检查已安装的工具。前两个命令会打印版本号。`cd` 用来更改工作目录，`ls` 用来列出文件。将示例路径替换为解压目录的实际路径。

```bash
python3 --version
git --version
cd /path/to/effective-ai-course-lab
ls
```

**在 Windows PowerShell 中，**运行 `py -3 --version`、`git --version`、`cd C:\path\to\effective-ai-course-lab` 和 `Get-ChildItem`。列表中应包含 `task_report.py`、`tasks.json`、`tests` 和 `docs`。版本命令失败时，请先完成安装。

```bash
pwd
python3 task_report.py tasks.json
python3 -m unittest discover -s tests -v
```

**在 Windows PowerShell 中，**如果愿意，可用 `Get-Location` 替换 `pwd`；如果 Python 使用启动器，可用 `py -3` 替换 `python3`。第一条命令会显示路径，路径末尾应为解压后的实验室文件夹。还要检查文件名。`AGENTS.md.txt` 不能代替 `AGENTS.md`。在 Windows 文件资源管理器中启用文件扩展名，以查看完整名称。

**预期输出：**报告显示 `Total tasks: 4`。测试命令列出两个测试并以 `OK` 结束。成功时 shell 返回退出代码 0。若数量不同或出现 traceback，请检查文件夹和 Python 环境。

**拆解命令的各个部分。**在 `python3 task_report.py tasks.json` 中，`python3` 启动 Python，`task_report.py` 是程序，`tasks.json` 指定输入数据。打印出的数量是输出，不是另一条命令。命令失败后，macOS 和 Linux 使用 `echo $?` 显示状态。PowerShell 通过 `$LASTEXITCODE` 提供上一个本机程序的状态。

**Python 安装完成后，为首次运行预留约十分钟：**解压实验室、运行报告，并将总数与 `tasks.json` 中四条记录核对。用文本编辑器打开 JSON 文件并自行计数。

## 安全练习 Git

**只在解压后的实验室文件夹内启动 Git。**以下命令会保存本地快照。`git status` 显示有更改的文件。编辑受 Git 跟踪的文件后，`git diff` 显示更改行。

```bash
git init
git add .
git commit -m "课程实验室基线"
git status --short
```

**预期状态：**提交后不会显示任何文件名。如果 Git 要求提供姓名和邮箱，请在此文件夹中设置仅供实验室使用的身份信息，然后重新提交。将示例值换成你自己的私有值。不要把身份信息或凭据输出粘贴到公开聊天中。

```bash
git config --local user.name "课程学员"
git config --local user.email "learner@example.invalid"
git commit -m "课程实验室基线"
git status --short
```

**重置无需 Git 命令。**把笔记保存在实验室之外，删除解压的练习副本，再解压原始 ZIP。当课程编辑让程序处于未知状态时，使用此方法重置。

## 保护练习空间

**使用合成示例。**不要把私人文档上传到课程项目。不要把 API 密钥放入提示词、源文件、截图或提交中。编程代理对文件和命令的访问取决于权限和打开的文件夹。允许它运行前，要检查这两项。

**上传前检查共享设置。**项目成员可能有权访问项目文件。实际工作中请遵守组织政策。课程使用虚构数据，因此实验室本身无需特别审批。

## 练习和检查

**你的成果：**记录所选路线、五项预检内容、报告数量、测试结果和重置方法。使用一份新的实验室副本，确认自己知道如何重置。

**预期理解：**你知道命令影响哪个文件夹，能区分本地 Git 与托管服务，并能在代理修改文件前进行恢复。

## 检查理解情况

1. **问题：**只在浏览器中学习能完成本地实验室路线吗？**答案：**不能。完整路线需要本地 Python 和 Git 基线。

2. **问题：**修改一次性实验室前应该保存什么？**答案：**已通过的初始测试结果和一个干净的重置点。

## 故障排查

- **找不到 Python 命令：**从官方发行渠道安装 Python 3，然后重新打开终端。
- **找不到文件：**检查工作目录并列出解压文件夹中的文件。
- **测试无法运行：**使用解压实验室 README 中的准确命令。
- **Git 要求提交身份：**在本地配置 Git，并将所选值留在课程笔记之外。

## 下一步

**继续学习[可靠的 AI 工作流](/articles/effective-ai-workflow-foundations/)**。第一个练习会在任何工具接触真实文件前使用同一个合成工作区。

**课程导航：**[课程大纲](/effective-ai-course-start/)。
