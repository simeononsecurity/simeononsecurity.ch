---
title: "コーディングエージェントで最初のリポジトリ作業を実行する"
date: 2026-10-10
lastmod: 2026-11-15
toc: true
draft: false
description: "コーディングエージェントの操作画面を選び、サンプルリポジトリを開き、提案された変更を確認してからチェックを実行し、変更を残します。"
genre: ["人工知能", "ソフトウェアエンジニアリング"]
tags: ["Codex CLI チュートリアル", "Codex アプリ", "Claude Code CLI", "OpenCode チュートリアル", "コーディングエージェントのワークフロー", "AI コーディングツール"]
cover: "/img/cover/effective-ai-coding-agent-first-task.webp"
coverAlt: "確認済みのファイル差分の横に、ターミナルとデスクトップで別々に表示されたエージェントを備えるコードリポジトリ"
coverCaption: ""
---

[実践的な AI ワークフローコースに戻る](/effective-ai-course-start/)

**コーディングエージェントは、作業領域内のファイルを読み、変更を提案し、ツールを実行します。** このレッスンでは、小さなリポジトリ作業を行います。ChatGPT デスクトップアプリまたは CLI の Codex、Claude Code CLI、OpenCode TUI から選びます。変更を受け入れる前に、その内容を確認します。

**学習目標:** 範囲を限定した変更を実行するか手動で適用し、差分と動作を確認します。

## 要点

- **ChatGPT デスクトップアプリの Codex** は、作業やレビューのための視覚的な環境を提供します。
- **Codex CLI** はターミナルから Codex セッションを起動します。
- **Claude Code CLI** はターミナルから Claude のコーディングワークフローを実行します。
- **OpenCode TUI** は、プロバイダーと権限を設定できるターミナルワークフローを提供します。
- **差分とテスト結果**は、アシスタントの完了メッセージより重要です。

## 始める前に

**前提条件:** [コースのセットアップ](/articles/effective-ai-course-setup/)を完了します。ベースライン実行とローカル Git スナップショットも含みます。このレッスンの前に、[リポジトリのコンテキスト](/articles/effective-ai-agents-md-context/)と[タスクパケット](/articles/effective-ai-task-packets/)を完了します。利用を許可されているコーディングエージェントを使います。所要時間は45分です。難易度は初級から中級です。

**[コースのスターターラボ](/downloads/effective-ai-course-lab.zip)**を使い捨てのフォルダーに展開します。アーカイブには小さなタスクレポートプログラム、サンプルデータ、テストが含まれます。最初の編集に本番リポジトリを使わないでください。既存の合計数を維持しながら `--status` フィルターを追加します。

## コーディングエージェントを使わない学習方法

**コーディングエージェントを使えない場合は、**チャットアシスタントに同じ変更を提案させます。合成ラボの `docs/requirements.md`、`task_report.py`、対象のテストファイルだけを貼り付けます。統一 diff と短い説明を求めます。統一 diff では旧行に `-`、新しい行に `+` が付きます。指定されたファイルをテキストエディターで開き、古い行を提案された行に置き換えて保存します。その後、「結果を確認する」のすべてのコマンドを実行します。`tasks.json` は変更しません。エージェントの手順を実行しなかったことを記録します。最終課題には別の JSON 機能があるため、フィルターの解決策をレッスン5の要件とチェックに照らして確認します。

## インターフェイスを選ぶ

**まずレビュー環境を選びます。** ChatGPT デスクトップアプリの Codex は、視覚的なプロジェクトや差分レビューに向いています。展開したラボフォルダーで作業するなら、ターミナルインターフェイスが適しています。ターミナルの選択肢を比較します。

| ターミナルツール | アカウントまたはプロバイダーの確認 | 起動コマンド |
|---|---|---|
| **Codex CLI** | Codex にサインイン済みで、ローカル権限があることを確認 | `codex` |
| **Claude Code CLI** | Claude Code を利用でき、ローカル権限があることを確認 | `claude` |
| **OpenCode TUI** | 対応するモデルプロバイダーと権限を設定 | `opencode` |

**選んだツールの最新の公式ガイドに従ってインストールし、サインインします。** [Codex CLI](https://learn.chatgpt.com/docs/codex/cli)、[ChatGPT デスクトップアプリ](https://learn.chatgpt.com/docs/app)、[Claude Code](https://code.claude.com/docs/en/overview)、[OpenCode](https://opencode.ai/docs/)を読みます。コマンド、対応プラットフォーム、アカウント要件は変わります。このレッスンでは、安定した起動名と共通のレビュー手順を使います。

**製品を詳しく選ぶには、**サイトの[CLI コーディングエージェント比較](/articles/cli-coding-agents-comparison/)または[GUI コーディングエージェント比較](/articles/gui-coding-agents-comparison/)を読みます。[Codex CLI とデスクトップ](/articles/codex-cli-vs-desktop/)、[Claude Code CLI とデスクトップ](/articles/claude-code-cli-vs-desktop/)、[OpenCode CLI とデスクトップ](/articles/opencode-cli-vs-desktop/)のガイドでは、各製品のインターフェイスを比較しています。

**ラボフォルダーから始めます。** どのインターフェイスでも、作業領域を明示的に選ぶ必要があります。

1. **Codex デスクトップ:** ChatGPT デスクトップアプリを開き、展開したラボをローカルプロジェクトとして選び、そのプロジェクトでローカルタスクを始めます。編集前にフォルダーのパスと承認プロンプトを確認します。ホストされたタスクでは別の作業コピーを使います。
2. **Codex CLI:** `cd /path/to/effective-ai-course-lab` を実行し、続いて `codex` を実行します。表示された作業フォルダーと承認モードを確認します。
3. **Claude Code CLI:** 同じ `cd` コマンドを実行し、続いて `claude` を実行します。プロジェクトフォルダーとツール権限を確認します。
4. **OpenCode TUI:** 同じ `cd` コマンドを実行し、続いて `opencode` を実行します。選択したプロバイダー、プロジェクト、権限設定を確認します。

**ChatGPT chat と Claude Projects は会話や共有の参考ファイルを扱います。** Codex と Claude Code は、ファイルやコマンドを扱うツールを備えたコード作業領域で動作します。OpenCode にはデスクトップや IDE の画面もありますが、このレッスンではターミナルを使います。プロバイダー、アカウント、ローカル実行かホスト実行かは異なります。すべてを同じ実行として扱わず、選んだ画面を記録します。

**ラボを開く前に5点を確認します:** 対応 OS、認証、プロバイダーまたはアカウントの費用、ファイルとコマンドの権限、実行場所がローカルかリモートホストか。選択を記録します。デスクトップアプリとターミナルツールが同じ作業領域を使うと思い込まないでください。

## スターターを確認する

**リポジトリコンテキストのレッスンで使ったクリーンなラボフォルダーを開き直します。** このコピーにはコミット済みの `AGENTS.md` と、任意のガイダンス `CLAUDE.md` があります。エージェントに編集を頼む前にファイルを確認します。このフォルダーからベースラインテストを実行します。

```bash
python3 -m unittest discover -s tests -v
python3 task_report.py tasks.json
```

**ベースラインの期待結果:** レポートには `Total tasks: 4` と表示されます。テスト実行では2つのテスト名が示され、最後に `OK` が表示されます。どちらかが失敗したら止まり、展開したファイルを確認します。壊れた開始状態をエージェントが修正したと見なさないでください。

**コース設定とリポジトリコンテキストのレッスンで作ったローカル Git スナップショットを使います。** `AGENTS.md` と任意の `CLAUDE.md` はコミット済みのはずです。機能を編集する前に `git status --short` を実行し、何も表示されないことを確認します。エージェントもコミットしてはいけません。アーカイブには Git 履歴がありません。 その `.gitignore` はテスト実行で生成される Python バイトコードを除外します。別のコピーを展開した場合は、そのフォルダーでコース設定とコンテキストのレッスンをやり直します。機能編集の前にガイダンスファイルをコミットします。まずスターターを初期化してコミットします。

```bash
git init
git add .
git commit -m "コースラボのベース"
```

**次に `AGENTS.md` と任意の `CLAUDE.md` を追加します。** リポジトリコンテキストのレッスンで承認されたソースとテストコマンドを記載します。ファイルをコミットし、`git status --short` がクリーンであることを確認してから機能を編集します。これらのコマンドは展開した練習用フォルダーで実行し、別のリポジトリのルートでは実行しません。

## 範囲を限定した依頼を送る

**選んだコーディングエージェントでラボフォルダーを開きます。** 次のタスクパケットを送ります。

```text
task_report.py に任意の --status 引数を追加してください。
指定できる値は open と done です。
省略時は現在の合計数の出力を変更しないでください。
指定時は一致するタスクだけを数え、Total tasks: N を出力してください。
両方の値、無効な値、変更されない既定出力を確認するテストを追加してください。
tasks.json や無関係なファイルを変更しないでください。
テストを実行し、正確なコマンドと結果を報告してください。
コードとテストが終わったら停止してください。コミットもプッシュもしないでください。
```

**Windows では、** セットアップ中に確認した `py -3` を `python3` の代わりに使います。保存するリポジトリガイダンスやタスクパケットも同様に更新します。

**コードが分からない場合は、編集前に短い計画を求めます。** エージェントには使い捨てのラボフォルダーだけを編集する許可を与えます。権限設定はツールごとに異なります。シェルコマンドやファイル書き込みを許可する前に、現在の設定を確認します。

## 結果を確認する

**差分を読みます。** フィルターなしの出力が変わらないこと、フィルターが2つの値だけを受け付けること、エラーケースと既定出力をテストが確認していることを確認します。テストが成功しても、要求された動作を検証していなければ変更の根拠にはなりません。

```bash
git status --short
git diff -- task_report.py tests
python3 -m unittest discover -s tests -v
python3 task_report.py tasks.json
python3 task_report.py tasks.json --status open
python3 task_report.py tasks.json --status done
python3 task_report.py tasks.json --status invalid
```

**期待される結果:** 最初の3つのレポートコマンドは 4、2、2 を表示します。無効な値では明確なエラーが出て、終了コードは0以外になります。エラー文は実装によって異なります。macOS または Linux では、無効なコマンドの直後に `echo $?` を実行して終了コードを読みます。PowerShell では `$LASTEXITCODE` を確認します。

| 証拠 | 確認する内容 |
|---|---|
| **ファイル一覧** | 変更されたのはプログラムとテストだけ |
| **差分** | フィルターのロジックが依頼に一致 |
| **テスト出力** | 新しいケースが実行され、合格 |
| **手動実行** | 既定、`open`、`done` の件数が `tasks.json` と一致 |

**エージェントがテストを実行せずに結果を報告した場合は、**自分でコマンドを実行します。変更範囲がタスクパケットを超えたら、限定した修正を依頼します。状態が分からなければ、展開した練習用コピーを削除し、元の ZIP を再展開します。

## 学習ルートの解答例

**手動パッチに失敗した場合は、以下のファイル全体を使います。** 新しく展開したラボを使い、最初のブロックを `task_report.py`、2つ目を `tests/test_task_report.py` として保存し、「結果を確認する」のコマンドを実行します。`tasks.json` と `docs/requirements.md` は変更しません。ファイルをコピーする前に、最初の失敗を記録します。

`task_report.py`:

```python
"""JSON ファイルのタスク数を表示します。"""

import argparse
import json
import sys
from pathlib import Path


def count_tasks(path: Path, status: str | None = None) -> int:
    """すべてのタスク、または許可された状態のタスクを数えます。"""
    tasks = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(tasks, list):
        raise ValueError("task data must be a list")
    if status not in (None, "open", "done"):
        raise ValueError("status must be open or done")
    if status is None:
        return len(tasks)
    return sum(1 for task in tasks if task["status"] == status)


def main() -> int:
    parser = argparse.ArgumentParser(description="ワークショップのタスクを数える")
    parser.add_argument("path", type=Path, help="JSON タスクリストへのパス")
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

`tests/test_task_report.py`:

```python
"""ワークショップのタスクレポートのテスト。"""

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

**コンテキストと結果確認のレッスンでは、フィルターのテストに合格した編集済みコピーを保管します。** この例を使って復旧した場合も、後のレッスン用に新しいコピーと合格したテストを残します。diff とテスト記録はラボの外に保管します。委任のレッスン前にスターターへ戻すか、失敗した試行を削除してやり直します。

## 練習と確認

**成果物:** ラボの diff と、ファイル範囲、既定の動作、フィルターの動作、無効な入力を記した4行のレビュー記録。バージョン固有の問題を再現できるよう、ツール名とバージョンを個人メモに記録します。

**期待される考え方:** 自分の作業方法に合う画面を選び、範囲を限定した依頼を送り、実際の変更を調べ、エージェントの報告とは独立したチェックを実行しました。

## 理解度を確認する

1. **質問:** 状態フィルターの変更が機能したと何で分かりますか。**回答:** 範囲を限定した diff、合格したテスト、既定、open、done、無効値それぞれの実測結果です。
2. **質問:** エージェントがテストを実行したという報告は、自分のテスト結果になりますか。**回答:** いいえ。コマンドを実行するか、出力を確認します。

## トラブルシューティング

- **コマンドが見つからない:** リンク先のベンダーガイドでインストールを終え、ターミナルを開き直します。
- **ファイルにアクセスできない:** 展開したラボフォルダーを開き、作業領域の権限を確認します。
- **予期しないファイルが変更された:** 次の依頼を送る前に止まり、`git status --short` を確認します。
- **テストは成功するが動作が違う:** 手動ケース、または不足している要件を確認するテストを追加します。

## 次のステップ

**[コンテキストウィンドウと引き継ぎ](/articles/effective-ai-context-window-management/)**に進みます。新しいセッションで役立つ記録を残します。

**コースナビゲーション:** [前へ: タスクパケット](/articles/effective-ai-task-packets/)、[コース概要](/effective-ai-course-start/)。
