---
title: "AI 工作流综合实践：构建并验证 JSON 报告"
date: 2026-10-10
lastmod: 2026-11-15
toc: true
draft: false
description: "创建一份新的 JSON 任务报告，包含项目背景、范围明确的代理请求、独立测试、来源审查，以及交给新会话的交接记录。"
genre: ["人工智能", "软件工程", "教育"]
tags: ["AI 工作流综合实践", "编程代理项目", "AI 任务验证", "AGENTS.md", "MCP 练习", "代理交接"]
cover: "/img/cover/effective-ai-capstone.webp"
coverAlt: "已完成的工作坊软件任务，包含源文件、测试结果、代理审查和交接记录"
coverCaption: ""
---

[返回实用 AI 工作流课程](/effective-ai-course-start/)

**构建一种新的输出格式，并证明它的行为符合预期。** 之前你添加了状态筛选器。本次综合实践从一份全新的实验环境开始，新增一份供其他程序读取的 JSON 报告。新要求用于检查你是否能把工作流迁移到另一项功能。

**学习目标：**交付一份经过检查的 JSON 报告、一份来源与工具证据记录，以及一份新会话能够理解的交接说明。

## 要点

- **单独的需求**决定综合实践的功能。
- **编程代理的修改**仅限于指定文件。
- **独立检查**决定是否验收。
- **交给新会话的记录**能让对方还原结果。

## 开始之前

**先决条件：**完成第 0 至 10 课，包括仓库背景、第一次编程任务、MCP 或浏览器替代方案、任务委派和有界循环。第 11 课为选修。预留 90 至 120 分钟。难度为中级。

**重新解压一份**[入门实验包](/downloads/effective-ai-course-lab.zip)。修改前运行 `python3 task_report.py tasks.json` 和两项基线测试。在 Windows 上，如果设置使用 Python Launcher，请运行 `py -3`。按照课程设置创建本地 Git 基线。第 5 课的状态筛选器按设计不会出现在此实验中。

**阅读 `docs/capstone-requirements.md`，修订版 1。** 它要求支持 `--format text|json`。默认文本仍为 `Total tasks: 4`。JSON 输出包含数值总数，以及数据中每种状态的计数。测试空列表、缺少状态和不支持的格式。不要把 `docs/requirements.md` 当作此新功能的权威要求。

**选择路径。** 已连接路径使用可观察到的编程代理编辑、一次真实的只读 MCP 调用，以及原生 worker 或单独的 worker 会话。学习路径使用聊天助手提出代码建议，以浏览器来源替代 MCP，并用不同聊天模拟 worker。不可用的工具步骤标记为“未运行”。两种路径都要求本地测试和文件审查。下方答案提供完整文件作为恢复方案。先把第一次尝试记入笔记，再把答案复制到新解压的实验目录中。

## 检查点 1：项目简报

**打开合成的 ChatGPT 或 Claude 工作坊项目。** 请求一份两句话的提醒草稿。对照 `approved-schedule.md` 确认时间为晚上 7 点。提醒时间以日程为准。程序行为以综合实践需求为准。

**证据：**记录项目名称、来源修订版、观察到的草稿时间和任何修正。不要发送消息。

## 检查点 2：仓库背景

**打开新实验环境。** 创建一份简短的 `AGENTS.md`，指向 `docs/capstone-requirements.md`、`task_report.py`、测试，以及设置时已验证的测试命令。如果使用 Claude Code，请从 `CLAUDE.md` 导入共享文件。为这些指导文件创建人工设置提交，然后确认 `git status --short` 没有输出。编程代理不能提交功能修改。

**证据：**保存仓库地图和干净的指导文件快照。记录修订版 1 的 JSON 键名和无效输入行为。若旧聊天描述了状态筛选器，将其视为另一项任务的背景。

## 检查点 3：外部来源

**已连接路径：**通过受支持的客户端使用[只读 OpenAI Docs MCP 服务器](https://learn.chatgpt.com/learn/docs-mcp)。让一个 MCP 工具提供当前的 `AGENTS.md` 指引。记录工具名称、来源 URL，以及一项适用于实验的内容。之后移除练习连接。

**学习路径：**在浏览器中打开[`AGENTS.md` 官方文档](https://learn.chatgpt.com/docs/agent-configuration/agents-md)。记录标题、URL 和一项相关内容。将 MCP 发现和执行标记为“未运行”。

**证据：**配置服务器条目不能证明执行过调用。已连接路径需要可见的工具调用和返回的来源内容。

## 检查点 4：委派一次审查

**请一名只读 worker**检查 `docs/capstone-requirements.md`、`task_report.py` 和基线测试。要求报告最多五行，列出缺失的检查和文件路径。学习路径中使用另一个聊天，并标记为模拟 worker。

**预期发现：**初始测试检查总数和一个非列表 JSON 值。它们没有检查 JSON 输出、空列表、缺少状态或无效格式。你要亲自打开测试文件验证这份报告。验收标准与第 5 课不同，因此一次简短的独立审查很有价值。

**证据：**保存简短报告和一句话的集成决定。将 worker 对话记录放在主任务记录之外。

## 检查点 5：请求修改

**把以下任务包交给编程代理。**学习路径中由聊天助手提出补丁，再由你手动应用到实验环境。

```text
目标：在 JSON 路径后添加 --format text|json。
来源：docs/capstone-requirements.md，修订版 1。
允许修改：task_report.py 和 tests/test_task_report.py。
保留：默认输出 Total tasks: 4，tasks.json 保持不变。
JSON：一个包含 total 和 by_status 计数的对象，stdout 不得有额外文本。
必需检查：默认和显式文本格式、JSON 4/2/2、空列表、
缺少状态、无效格式和基线测试。
停止条件：来源冲突、无关的基线失败或修改超出范围。
报告：修改文件、命令、观察到的输出、未解决问题。
不得提交、推送、发布或发送消息。
```

**先审查计划**，再开始编辑。模式选择很重要：`total` 是数字，不是字符串 `"4"`。`by_status` 包含输入中的每种状态，也涵盖未来新增的状态。只在解压后的实验目录内修改。

## 检查点 6：测试和审查

**亲自运行这些检查。** 在 Windows 上，如果需要将 `python3` 替换为 `py -3`。JSON 键顺序和空白格式不重要。将输出解析为 JSON，并比较值的类型。

```bash
git status --short
git diff -- task_report.py tests/test_task_report.py
python3 -m unittest discover -s tests -v
python3 task_report.py tasks.json
python3 task_report.py tasks.json --format text
python3 task_report.py tasks.json --format json
python3 task_report.py tasks.json --format invalid
```

**预期行为：**测试通过。两个文本命令都输出 `Total tasks: 4`。JSON 命令返回一个对象，其中 `total` 为 4，`by_status.open` 为 2，`by_status.done` 为 2。无效格式以非零代码退出。测试还会覆盖空输入和缺少字符串类型 `status` 的任务。阅读这些情况的实际错误输出和退出代码。

| 检查点 | 通过证据 | 失败后的恢复方法 |
|---|---|---|
| **项目简报** | 提醒时间为晚上 7 点 | 更新日程来源 |
| **仓库地图** | 写明需求和测试路径 | 修正指导文件 |
| **外部来源** | 阅读 MCP 来源或记录浏览器替代方案 | 检查连接或 URL |
| **Worker 审查** | 在文件中确认缺失测试 | 修正 worker 报告 |
| **文件范围** | 只有程序和测试 | 逐项检查不需要的修改 |
| **行为** | 检查文本、JSON、空值和错误 | 找出一个原因后重试 |
| **交接** | 新会话能还原状态 | 补充缺失的来源或结果 |

**用新的解压副本安全重置。** 将笔记保存在实验目录外，只删除一次性解压副本，然后重新解压原始 ZIP。不要在包含需要保留工作的仓库中执行大范围 Git 重置。

## 检查点 7：交接给新会话

**在实验目录外写一份少于 180 词的交接说明。** 包括需求修订版、修改文件、准确的测试命令和结果、文本与 JSON 输出、无效输入检查、使用记录和待办事项。打开新会话，让它指出 JSON 键名并判断功能是否通过。

**预期回答：**新会话指出 `total` 和 `by_status`，引用修订版 1，只报告实际观察到的检查，并标出缺失的检查。

## 答案与评分标准

**一种有效实现**如下。将第一个代码块保存为 `task_report.py`，第二个保存为 `tests/test_task_report.py`，放在新解压的实验目录中。保持 `tasks.json` 和两个需求文件不变。运行检查点 6 的检查。将其他方案与要求和实际行为对照。

`task_report.py`：

```python
"""以文本数量或 JSON 摘要输出工作坊任务。"""

import argparse
import json
import sys
from collections import Counter
from pathlib import Path


def load_tasks(path: Path) -> list:
    tasks = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(tasks, list):
        raise ValueError("task data must be a list")
    for index, task in enumerate(tasks, start=1):
        if not isinstance(task, dict) or not isinstance(task.get("status"), str):
            raise ValueError(f"task {index} needs a string status")
    return tasks


def count_tasks(path: Path) -> int:
    return len(load_tasks(path))


def summarize_tasks(path: Path) -> dict:
    tasks = load_tasks(path)
    counts = Counter()
    for task in tasks:
        counts[task["status"]] += 1
    return {"total": len(tasks), "by_status": dict(sorted(counts.items()))}


def main() -> int:
    parser = argparse.ArgumentParser(description="工作坊任务报告")
    parser.add_argument("path", type=Path, help="JSON 任务列表的路径")
    parser.add_argument("--format", choices=("text", "json"), default="text")
    args = parser.parse_args()
    try:
        if args.format == "json":
            print(json.dumps(summarize_tasks(args.path)))
        else:
            print(f"Total tasks: {count_tasks(args.path)}")
    except (OSError, ValueError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

`tests/test_task_report.py`：

```python
"""检查工作坊任务的文本报告和 JSON 报告。"""

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


def run_report(path: Path, *options: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, str(ROOT / "task_report.py"), str(path), *options],
        capture_output=True, text=True, check=False,
    )


class TaskReportTests(unittest.TestCase):
    def test_counts_four_sample_tasks(self):
        self.assertEqual(count_tasks(ROOT / "tasks.json"), 4)

    def test_rejects_non_list_data(self):
        with tempfile.TemporaryDirectory() as directory:
            sample = Path(directory) / "invalid.json"
            sample.write_text(json.dumps({"tasks": []}), encoding="utf-8")
            with self.assertRaises(ValueError):
                count_tasks(sample)

    def test_default_and_explicit_text(self):
        for options in ((), ("--format", "text")):
            result = run_report(ROOT / "tasks.json", *options)
            self.assertEqual(result.returncode, 0)
            self.assertEqual(result.stdout.strip(), "Total tasks: 4")

    def test_json_counts_and_types(self):
        result = run_report(ROOT / "tasks.json", "--format", "json")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(json.loads(result.stdout), {
            "total": 4, "by_status": {"open": 2, "done": 2},
        })

    def test_empty_list(self):
        with tempfile.TemporaryDirectory() as directory:
            sample = Path(directory) / "empty.json"
            sample.write_text("[]", encoding="utf-8")
            result = run_report(sample, "--format", "json")
            self.assertEqual(result.returncode, 0)
            self.assertEqual(json.loads(result.stdout), {
                "total": 0, "by_status": {},
            })

    def test_missing_status(self):
        with tempfile.TemporaryDirectory() as directory:
            sample = Path(directory) / "missing.json"
            sample.write_text('[{"id": 1}]', encoding="utf-8")
            for options in ((), ("--format", "json")):
                result = run_report(sample, *options)
                self.assertNotEqual(result.returncode, 0)
                self.assertIn("status", result.stderr)

    def test_invalid_format(self):
        result = run_report(ROOT / "tasks.json", "--format", "invalid")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("invalid", result.stderr)


if __name__ == "__main__":
    unittest.main()
```

**使用答案后重置：**把笔记保存在实验目录外，删除此解压副本，再次解压原始入门实验包。新副本包含两项基线测试，不包含该功能实现。

**按上表的每个检查点计一分。**如果外部来源行包含真实 MCP 调用，且 worker 行记录了真实会话，七分即可完成已连接路径。如果来源是已核验的浏览器页面，且工具步骤明确标为未运行，七分即可完成学习路径。缺少行为、来源或文件范围检查会阻止两种路径的完成。

## 检查理解

1. **哪项要求决定此功能？** `docs/capstone-requirements.md`，修订版 1。之前的状态筛选要求属于第 5 课。
2. **什么能证明 JSON 契约？** 解析命令输出，比较数值和每种状态的计数，并检查空输入和无效输入。格式精美的代理摘要不够。

## 故障排查

- **编辑前基线测试失败：**从 ZIP 恢复实验环境并重新设置。
- **代理修改了其他文件：**检查 diff，只恢复不需要的实验改动。
- **MCP 连接失败：**使用浏览器来源，并将检查点标记为学习路径。
- **Worker 重复错误数值：**重新阅读综合实践要求并修正报告。
- **重试次数用尽：**保存错误记录，并请人工审查者指出下一步。

## 下一步

**保存完成的证据记录。**如需学习进阶团队发布和跨系统授权，请继续学习[AI 协作实施课程](/ai-collaboration-course-start/)。

**课程导航：**[上一项必修课：有界循环](/articles/effective-ai-bounded-agent-loops/)，[选修：专用代理评估](/articles/effective-ai-specialized-agent-evaluation/)，[课程大纲](/effective-ai-course-start/)。
