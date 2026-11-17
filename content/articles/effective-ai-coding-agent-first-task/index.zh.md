---
title: "使用编程代理完成你的第一个代码仓库任务"
date: 2026-10-10
lastmod: 2026-11-15
toc: true
draft: false
description: "选择编程代理界面，打开示例代码仓库，检查建议的更改，并在保留更改前运行检查。"
genre: ["人工智能", "软件工程"]
tags: ["Codex CLI 教程", "Codex 应用", "Claude Code CLI", "OpenCode 教程", "编程代理工作流程", "AI 编程工具"]
cover: "/img/cover/effective-ai-coding-agent-first-task.webp"
coverAlt: "代码仓库中的终端与桌面代理视图，以及旁边经过审查的文件差异"
coverCaption: ""
---

[返回实用 AI 工作流程课程](/effective-ai-course-start/)

**编程代理会在工作区中读取文件、提出修改建议并运行工具。** 本课将带你完成一个小型代码仓库任务。选择 ChatGPT 桌面应用或 CLI 中的 Codex、Claude Code CLI，或 OpenCode TUI。接受更改之前，先检查它。

**学习目标：** 你将执行或手动应用一项范围明确的更改，并检查其差异和行为。

## 重点

- **ChatGPT 桌面应用中的 Codex** 提供可视化的任务与审查工作区。
- **Codex CLI** 从终端启动 Codex 会话。
- **Claude Code CLI** 在终端运行 Claude 的编程工作流。
- **OpenCode TUI** 提供可配置模型提供商和权限的终端工作流。
- **差异和测试结果**比助手的完成消息更重要。

## 开始之前

**先决条件：**完成[课程设置](/articles/effective-ai-course-setup/)，包括基线运行和本地 Git 快照。开始本课前，完成[代码仓库上下文](/articles/effective-ai-agents-md-context/)和[任务包](/articles/effective-ai-task-packets/)。使用你获准访问的编程代理。预留 45 分钟。难度为初级到中级。

**在一次性文件夹中使用[课程入门实验室](/downloads/effective-ai-course-lab.zip)**。压缩包包含一个小型任务报告程序、示例数据和测试。第一次编辑不要使用生产代码仓库。添加 `--status` 筛选器，同时保留现有的总数。

## 不使用编程代理的学习路线

**如果无法使用编程代理，请让聊天助手提出相同的更改。**仅粘贴合成实验室中的 `docs/requirements.md`、`task_report.py` 和指定测试文件。要求提供统一差异和简短说明。统一差异用 `-` 标记旧行，用 `+` 标记新行。在文本编辑器中打开指定文件，用建议内容替换旧行并保存。然后运行“检查结果”中的所有命令。不要更改 `tasks.json`。记录未运行编程代理步骤。结业项目还有一个单独的 JSON 功能，因此请将筛选器方案与第 5 课的要求和检查进行比较。

## 选择界面

**先选择审查界面。** ChatGPT 桌面应用中的 Codex 适合可视化项目和差异审查。要在解压后的实验室文件夹中工作，可以使用终端界面。比较终端工具：

| 终端工具 | 账户或提供商检查 | 启动命令 |
|---|---|---|
| **Codex CLI** | 确认已登录 Codex，并检查本地权限 | `codex` |
| **Claude Code CLI** | 确认可以访问 Claude Code，并检查本地权限 | `claude` |
| **OpenCode TUI** | 配置受支持的模型提供商和权限 | `opencode` |

**根据所选工具的最新官方指南完成安装和登录。**阅读 [Codex CLI](https://learn.chatgpt.com/docs/codex/cli)、[ChatGPT 桌面应用](https://learn.chatgpt.com/docs/app)、[Claude Code](https://code.claude.com/docs/en/overview) 或 [OpenCode](https://opencode.ai/docs/)。命令、受支持的平台和账户要求会变化。本课只使用稳定的启动名称和通用审查流程。

**若要深入选择产品，**请阅读网站上的 [CLI 编程代理对比](/articles/cli-coding-agents-comparison/)或[图形界面编程代理对比](/articles/gui-coding-agents-comparison/)。[Codex CLI 与桌面版](/articles/codex-cli-vs-desktop/)、[Claude Code CLI 与桌面版](/articles/claude-code-cli-vs-desktop/)和 [OpenCode CLI 与桌面版](/articles/opencode-cli-vs-desktop/)指南介绍各产品的界面差异。

**从实验室文件夹开始。**每种界面都需要明确选择工作区：

1. **Codex 桌面版：**打开 ChatGPT 桌面应用，将解压的实验室选为本地项目，然后在该项目中启动本地任务。编辑前检查文件夹路径和审批提示。托管任务使用另一份工作区副本。
2. **Codex CLI：**运行 `cd /path/to/effective-ai-course-lab`，然后运行 `codex`。确认显示的工作文件夹和审批模式。
3. **Claude Code CLI：**运行相同的 `cd` 命令，然后运行 `claude`。确认项目文件夹和工具权限。
4. **OpenCode TUI：**运行相同的 `cd` 命令，然后运行 `opencode`。确认所选提供商、项目和权限设置。

**ChatGPT chat 和 Claude Projects 用于管理对话及共享参考文件。**Codex 和 Claude Code 在具有文件与命令工具的代码工作区中运行。OpenCode 也提供桌面和 IDE 界面，但本课使用终端界面。提供商、账户以及本地或托管执行方式各不相同，因此请记录所选界面，不要将不同会话当成同一次运行。

**打开实验室之前检查五项内容：**受支持的操作系统、身份验证、提供商或账户费用、文件和命令权限，以及任务是在本地还是远程主机上执行。记录你的选择。不要假设桌面应用和终端工具使用同一个工作区。

## 检查起始项目

**重新打开代码仓库上下文课程中的干净实验室文件夹。**此副本包含你已提交的 `AGENTS.md` 和可选的 `CLAUDE.md` 指引。让代理编辑前，先检查文件。从此文件夹运行基线测试。

```bash
python3 -m unittest discover -s tests -v
python3 task_report.py tasks.json
```

**预期基线结果：**报告显示 `Total tasks: 4`。测试运行列出两个测试，并以 `OK` 结束。任一测试失败时，请停止并检查解压的文件。不要让代理为有缺陷的起始状态负责。

**使用课程设置和代码仓库上下文课程中的本地 Git 快照。**`AGENTS.md` 和可选的 `CLAUDE.md` 应已提交。编辑功能前运行 `git status --short`，并确认没有文件列出。代理也不得提交更改。压缩包不包含 Git 历史。 其中的 `.gitignore` 会排除运行测试时生成的 Python 字节码。如果重新解压了副本，请在新文件夹中重做课程设置和上下文课程。先提交指引文件，再编辑功能。首先初始化并提交起始项目：

```bash
git init
git add .
git commit -m "课程实验室基线"
```

**然后添加 `AGENTS.md` 和可选的 `CLAUDE.md`**，内容使用上下文课程认可的来源和测试命令。提交这些文件，确认 `git status --short` 没有输出，再开始编辑功能。在解压的练习文件夹中运行这些命令，不要在其他代码仓库的根目录运行。

## 提出范围明确的请求

**在所选编程代理中打开实验室文件夹。**发送以下任务包：

```text
task_report.py 添加可选的 --status 参数。
允许的值：open 和 done。
未提供参数时，保持当前总数输出不变。
提供参数时，只统计匹配的任务并输出 Total tasks: N。
为两个值、无效值和保持不变的默认输出添加测试。
不要更改 tasks.json 或无关文件。
运行测试并报告准确的命令和结果。
代码和测试完成后停止。不要提交或推送。
```

**在 Windows 上，**将 `python3` 替换为设置期间验证过的 `py -3`，包括保存在代码仓库中的指引和任务包。

**如果还不了解代码，先要求代理提供简短计划。**只允许代理编辑一次性实验室文件夹。不同工具的权限控制不同，因此允许 shell 命令或文件写入前，先检查当前设置。

## 检查结果

**阅读差异。**确认未筛选时的输出保持不变，筛选器只接受两个值，并且测试覆盖错误输入和不变的默认输出。测试通过只有在它们检查了要求的行为时，才能支持这项更改。

```bash
git status --short
git diff -- task_report.py tests
python3 -m unittest discover -s tests -v
python3 task_report.py tasks.json
python3 task_report.py tasks.json --status open
python3 task_report.py tasks.json --status done
python3 task_report.py tasks.json --status invalid
```

**预期结果：**前三条报告命令分别显示 4、2 和 2。无效值会显示明确错误，并以非零状态退出。错误文字取决于实现。在 macOS 或 Linux 上，无效命令后立即运行 `echo $?` 查看退出码。在 PowerShell 中检查 `$LASTEXITCODE`。

| 证据 | 检查内容 |
|---|---|
| **文件列表** | 只有程序和测试发生变化 |
| **差异** | 筛选逻辑符合请求 |
| **测试输出** | 新测试用例已运行并通过 |
| **手动运行** | 默认、`open` 和 `done` 的计数与 `tasks.json` 一致 |

**如果代理没有运行测试就报告结果，**请自行运行命令。如果更改超出任务包范围，请要求代理进行有限修正。如果状态不明确，请删除解压的练习副本并重新解压原始 ZIP。

## 学习路线参考答案

**如果手动补丁失败，请使用以下完整文件。**重新解压一个实验室，将第一个代码块保存为 `task_report.py`，第二个保存为 `tests/test_task_report.py`，然后运行“检查结果”中的命令。不要更改 `tasks.json` 和 `docs/requirements.md`。复制文件前，记录最初的失败。

`task_report.py`：

```python
"""显示 JSON 文件中的任务数量。"""

import argparse
import json
import sys
from pathlib import Path


def count_tasks(path: Path, status: str | None = None) -> int:
    """统计所有任务或具有允许状态的任务。"""
    tasks = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(tasks, list):
        raise ValueError("task data must be a list")
    if status not in (None, "open", "done"):
        raise ValueError("status must be open or done")
    if status is None:
        return len(tasks)
    return sum(1 for task in tasks if task["status"] == status)


def main() -> int:
    parser = argparse.ArgumentParser(description="统计工作坊任务")
    parser.add_argument("path", type=Path, help="JSON 任务列表的路径")
    parser.add_argument("--status", choices=("open", "done"))
    args = parser.parse_args()
    try:
        total = count_tasks(args.path, args.status)
    except (OSError, ValueError, KeyError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    print(f"Total tasks: {total}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

`tests/test_task_report.py`：

```python
"""工作坊任务报告的测试。"""

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from sys import path as module_path

ROOT = Path(__file__).resolve().parents[1]
module_path.insert(0, str(ROOT))
from task_report import count_tasks  # noqa: E402


class TaskReportTests(unittest.TestCase):
    def test_counts_four_sample_tasks(self):
        self.assertEqual(count_tasks(ROOT / "tasks.json"), 4)

    def test_rejects_non_list_data(self):
        with tempfile.TemporaryDirectory() as directory:
            sample = Path(directory) / "invalid.json"
            sample.write_text(json.dumps({"tasks": []}), encoding="utf-8")
            with self.assertRaises(ValueError):
                count_tasks(sample)

    def test_counts_each_approved_status(self):
        sample = ROOT / "tasks.json"
        self.assertEqual(count_tasks(sample, "open"), 2)
        self.assertEqual(count_tasks(sample, "done"), 2)

    def test_rejects_invalid_status_in_function(self):
        with self.assertRaises(ValueError):
            count_tasks(ROOT / "tasks.json", "pending")

    def test_default_command_stays_unchanged(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "task_report.py"), str(ROOT / "tasks.json")],
            capture_output=True, text=True, check=False,
        )
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout.strip(), "Total tasks: 4")

    def test_invalid_command_exits_nonzero(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "task_report.py"), str(ROOT / "tasks.json"),
             "--status", "invalid"],
            capture_output=True, text=True, check=False,
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("invalid", result.stderr)


if __name__ == "__main__":
    unittest.main()
```

**在上下文和结果检查课程中保留通过筛选器测试的修改副本。**如果通过此答案恢复了代码，也要为后续课程保留这个新副本和通过的筛选器测试。将差异和测试记录保存在实验室之外。委派课程开始前恢复起始项目；如果尝试失败，则删除它并重新开始。

## 练习和检查

**你的成果：**实验室差异，以及一份四行审查记录，覆盖文件范围、默认行为、筛选行为和无效输入。将工具名称和版本记录在私人笔记中，方便复现特定版本的问题。

**预期思路：**你选择了适合自己的界面，给出了范围明确的任务，检查了实际更改，并独立于代理的报告执行了一项验证。

## 检查理解情况

1. **问题：**什么证据能够证明状态筛选器修改有效？**答案：**范围明确的差异、通过的测试，以及默认、open、done 和无效输入的实际结果。
2. **问题：**代理说它运行过测试，这算你的测试结果吗？**答案：**不算。请运行命令或检查测试输出。

## 故障排除

- **找不到命令：**按照链接的供应商指南完成安装，然后重新打开终端。
- **无法访问文件：**打开解压的实验室文件夹，然后检查工作区权限。
- **意外文件发生变化：**停止操作，并在提出其他请求前检查 `git status --short`。
- **测试通过但行为不对：**添加手动测试用例，或为缺少的要求添加测试。

## 后续步骤

**继续学习[上下文窗口与交接](/articles/effective-ai-context-window-management/)**。你将为新的会话保留一份有用记录。

**课程导航：**[上一课：任务包](/articles/effective-ai-task-packets/)、[课程大纲](/effective-ai-course-start/)。
