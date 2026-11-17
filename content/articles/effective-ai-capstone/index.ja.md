---
title: "AIワークフロー実践課題: JSONレポートを作成して検証する"
date: 2026-10-10
lastmod: 2026-11-15
toc: true
draft: false
description: "プロジェクトの背景、範囲を限定したエージェントへの依頼、独立したテスト、ソース確認、新しいセッションへの引き継ぎを含むJSONタスクレポートを作成します。"
genre: ["人工知能", "ソフトウェアエンジニアリング", "教育"]
tags: ["AIワークフロー実践課題", "コーディングエージェントのプロジェクト", "AIタスクの検証", "AGENTS.md", "MCP演習", "エージェント間の引き継ぎ"]
cover: "/img/cover/effective-ai-capstone.webp"
coverAlt: "ソースファイル、テスト結果、エージェントレビュー、引き継ぎ記録を含むワークショップのソフトウェア課題の完了状態"
coverCaption: ""
---

[実践的なAIワークフローコースに戻る](/effective-ai-course-start/)

**新しい出力形式を追加し、その動作を証明します。** 前の課題ではステータスフィルターを追加しました。この実践課題は新しいラボから始め、別のプログラムが読み取るJSONレポートを追加します。新しい要件では、別の機能にもワークフローを適用できるかを確認します。

**学習目標:** 検証済みのJSONレポート、ソースとツールの証拠記録、新しいセッションが理解できる引き継ぎを作成します。

## 要点

- **別の要件**が実践課題の機能を定めます。
- **コーディングエージェントの変更**は指定ファイル内に限定します。
- **独立した確認**で合否を決めます。
- **新しいセッションへの引き継ぎ**で結果を再構成できるようにします。

## 始める前に

**前提条件:** リポジトリの背景、最初のコーディング課題、MCPまたはブラウザーでの代替、委任、範囲を限定したループを含むレッスン0～10を完了してください。レッスン11は任意です。90～120分を確保してください。難易度は中級です。

[スターターラボ](/downloads/effective-ai-course-lab.zip)を**新しく展開**します。編集前に`python3 task_report.py tasks.json`と2つのベースラインテストを実行します。Windowsでは、Python Launcherを使う構成なら`py -3`を使ってください。コースのセットアップと同様にローカルGitのベースラインを作成します。レッスン5のステータスフィルターは意図的にありません。

**`docs/capstone-requirements.md`のリビジョン1を読みます。** `--format text|json`が必要です。既定のテキストは`Total tasks: 4`のままです。JSON出力には数値の合計と、データにある各ステータスの件数が入ります。空のリスト、欠落したステータス、未対応の形式をテストします。この新機能の根拠として`docs/requirements.md`を使わないでください。

**進め方を選びます。** 接続ルートでは、観察可能なコーディングエージェントの編集、実際の読み取り専用MCP呼び出し、ネイティブワーカーまたは別のワーカーセッションを使います。学習ルートでは、チャットアシスタントにコードを提案させ、MCPの代わりにブラウザーのソースを使い、別々のチャットをシミュレーション用ワーカーとして使います。利用できないツールの手順には「未実行」と記録します。どちらのルートでもローカルテストとファイルレビューが必要です。以下の解答には復旧用の完成ファイルがあります。解答を新しい展開先にコピーする前に、最初の試行をメモに保存してください。

## チェックポイント1: プロジェクト概要

**合成されたChatGPTまたはClaudeのワークショッププロジェクトを開きます。** 2文のリマインダー案を依頼します。`approved-schedule.md`で午後7時の予定と照合します。リマインダーの時刻は予定表を基準にします。プログラムの動作は実践課題の要件を基準にします。

**証拠:** プロジェクト名、ソースのリビジョン、案で確認した時刻、修正点を記録します。メッセージは送信しません。

## チェックポイント2: リポジトリの背景

**新しいラボを開きます。** 短い`AGENTS.md`を作成し、`docs/capstone-requirements.md`、`task_report.py`、テスト、セットアップ時に確認したテストコマンドを記載します。Claude Codeを使う場合は、`CLAUDE.md`から共有ファイルを読み込みます。これらの案内ファイルを人がセットアップコミットし、`git status --short`が空であることを確認します。コーディングエージェントは機能変更をコミットしません。

**証拠:** マップと案内ファイルのクリーンな状態を保存します。リビジョン1で指定されたJSONキーと無効な入力への動作を記録します。以前のチャットがステータスフィルターを説明していた場合は、別の作業の背景情報として扱います。

## チェックポイント3: 外部ソース

**接続ルート:** 対応クライアントで[読み取り専用のOpenAI Docs MCPサーバー](https://learn.chatgpt.com/learn/docs-mcp)を使います。MCPツールに、最新の`AGENTS.md`ガイダンスを問い合わせます。ツール名、ソースURL、ラボに関係するポイントを1つ記録します。その後、練習用接続を削除します。

**学習ルート:** ブラウザーで[公式の`AGENTS.md`ドキュメント](https://learn.chatgpt.com/docs/agent-configuration/agents-md)を開きます。タイトル、URL、関連するポイントを1つ記録します。MCPの検出と実行は「未実行」とします。

**証拠:** サーバー設定があるだけでは、実行した証拠になりません。接続ルートでは、表示されたツール呼び出しと返されたソース内容が必要です。

## チェックポイント4: レビューを1件委任

**読み取り専用のワーカーに**`docs/capstone-requirements.md`、`task_report.py`、ベースラインテストを確認してもらいます。不足している確認項目とファイルパスを挙げる5行以内のレポートを依頼します。学習ルートでは別のチャットを使い、シミュレーション用ワーカーと記録します。

**想定される指摘:** 初期テストは合計数と、リストではないJSON値を確認します。JSON出力、空のリスト、ステータス欠落、無効な形式は確認しません。テストファイルを自分で開き、レポートを確かめます。レッスン5とは受け入れ条件が異なるため、短い独立レビューに意味があります。

**証拠:** 短いレポートと、1文の統合判断を保存します。ワーカーの記録はメインの作業記録とは別に保管します。

## チェックポイント5: 編集を依頼

**コーディングエージェントに**次の指示一式を渡します。学習ルートでは、チャットアシスタントがパッチを提案し、ラボには自分で適用します。

```text
目的: JSONパスの後ろに --format text|json を追加する。
ソース: docs/capstone-requirements.md、リビジョン1。
変更可能: task_report.py と tests/test_task_report.py。
維持: 既定の Total tasks: 4 と、変更しない tasks.json。
JSON: total と by_status の件数を持つ単一オブジェクト。stdoutに追加テキストを出さない。
必須確認: 既定と明示的なテキスト、JSON 4/2/2、空リスト、
ステータス欠落、無効な形式、ベースラインテスト。
停止条件: ソースの矛盾、無関係なベースライン失敗、範囲外の変更。
報告: 変更ファイル、コマンド、確認した出力、未解決の問題。
コミット、push、公開、メッセージ送信は禁止。
```

**編集前に計画を確認します。** スキーマの選択は重要です。`total`は数値であり、文字列`"4"`ではありません。`by_status`には入力に含まれるすべてのステータスを入れ、将来追加される値も数えます。編集を展開済みのラボ内に限定します。

## チェックポイント6: テストとレビュー

**次の確認を自分で実行します。** Windowsでは`python3`を`py -3`に置き換えます。JSONキーの順序や空白は問いません。出力をJSONとして解析し、型も含めて値を比較します。

```bash
git status --short
git diff -- task_report.py tests/test_task_report.py
python3 -m unittest discover -s tests -v
python3 task_report.py tasks.json
python3 task_report.py tasks.json --format text
python3 task_report.py tasks.json --format json
python3 task_report.py tasks.json --format invalid
```

**想定される動作:** テストは成功します。どちらのテキストコマンドも`Total tasks: 4`を出力します。JSONコマンドは`total`が4、`by_status.open`が2、`by_status.done`が2の単一オブジェクトを返します。無効な形式では0以外の終了コードになります。テストには空の入力と、文字列の`status`がないタスクも含まれます。それらのエラー出力と終了コードを読みます。

| チェックポイント | 成功の証拠 | 失敗時の復旧 |
|---|---|---|
| **プロジェクト概要** | リマインダーが午後7時を示す | 予定表ソースを更新する |
| **リポジトリマップ** | 要件とテストパスを記録 | 案内ファイルを修正する |
| **外部ソース** | MCPを読んだ、またはブラウザー代替を記録 | 接続またはURLを確認する |
| **ワーカーレビュー** | 不足テストをファイルで確認 | レポートを修正する |
| **ファイル範囲** | プログラムとテストのみ | 望まない変更を個別に確認する |
| **動作** | テキスト、JSON、空入力、エラーを確認 | 原因を1つ特定して再試行する |
| **引き継ぎ** | 新しいセッションが状態を再構成できる | 不足しているソースや結果を追加する |

**安全なリセットには新しい展開先を使います。** メモをラボ外に保存し、使い捨ての展開済みコピーだけを削除して、元のZIPを再展開します。残したい作業があるリポジトリで、広範囲のGitリセットをしないでください。

## チェックポイント7: 新しいセッションへの引き継ぎ

ラボの外に**180語未満の引き継ぎを書きます。** 要件のリビジョン、変更ファイル、正確なテストコマンドと結果、テキストとJSONの出力、無効入力の確認、利用記録、未対応の作業を含めます。新しいセッションを開き、JSONキーと機能の合否を答えるよう依頼します。

**想定される回答:** 新しいセッションは`total`と`by_status`を挙げ、リビジョン1を参照し、確認した事実だけを報告し、不足している確認項目を指摘します。

## 解答と評価基準

**有効な実装例**を以下に示します。最初のブロックを`task_report.py`、次を`tests/test_task_report.py`として新しいラボに保存します。`tasks.json`と両方の要件ファイルは変更しません。チェックポイント6の確認を実行します。別の実装も要件と観察した動作に照らして確認します。

`task_report.py`:

```python
"""ワークショップのタスク数をテキストまたはJSONで出力します。"""

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
    parser = argparse.ArgumentParser(description="ワークショップのタスクレポート")
    parser.add_argument("path", type=Path, help="JSONタスクリストのパス")
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

`tests/test_task_report.py`:

```python
"""ワークショップのタスクについてテキストとJSONレポートを確認します。"""

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

**解答を使った後にリセットします。** メモをラボの外に保存し、この展開済みコピーを削除して、元のスターターラボを再展開します。新しいコピーには2つのベースラインテストがあり、機能実装はありません。

**上の表のチェックポイントごとに1点を付けます。** 外部ソース欄に実際のMCP呼び出しがあり、ワーカー欄に実際のセッションが記録されていれば、接続ルートは7点です。ソース欄が確認済みのブラウザページで、ツール手順が明示的に未実行であれば、学習ルートは7点です。動作、ソース、ファイル範囲の確認が欠けると、どちらのルートも完了しません。

## 理解度を確認

1. **この機能を定める要件はどれですか。** `docs/capstone-requirements.md`のリビジョン1です。以前のステータスフィルター要件はレッスン5に属します。
2. **JSON契約の証拠は何ですか。** コマンド出力を解析し、数値と各ステータスの件数を比較し、空や無効な入力を確認します。エージェントの整った要約だけでは不十分です。

## トラブルシューティング

- **編集前にベースラインテストが失敗する:** ZIPからラボを戻し、セットアップをやり直します。
- **エージェントが別ファイルを変更する:** diffを確認し、不要なラボの変更だけを戻します。
- **MCP接続に失敗する:** ブラウザーのソースを使い、学習ルートとして記録します。
- **ワーカーが誤った値を繰り返す:** 実践課題の要件を読み直し、レポートを修正します。
- **再試行の上限に達する:** エラーログを保存し、人間のレビュー担当者に次の手順を尋ねます。

## 次のステップ

**完成した証拠記録を保存します。** チームでの高度な公開とシステム間の権限については、[AIコラボレーション実装コース](/ai-collaboration-course-start/)に進んでください。

**コース内の移動:** [前の必須レッスン: 範囲を限定したループ](/articles/effective-ai-bounded-agent-loops/)、[任意: 専門エージェントの評価](/articles/effective-ai-specialized-agent-evaluation/)、[コース概要](/effective-ai-course-start/)。
