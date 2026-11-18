---
title: "ローカルモデルで Claude Cowork と Claude Code を使う: 2026年版セットアップガイド"
date: 2026-09-22
lastmod: 2026-11-12
toc: true
draft: false
description: "Anthropic互換APIを使って、OllamaをClaude DesktopおよびClaude Codeに接続します。2026年のモデル選択とクラウド限定機能も確認します。"
genre: ["ローカルAI", "AIコーディングツール", "セルフホストAI", "開発者ツール", "プライバシー", "オープンソースモデル", "自動化", "AIハードウェア"]
tags: ["claude cowork", "claude code", "claude desktopのローカルモデル", "ollama claude code", "anthropic base url", "anthropic_auth_token", "claude codeのローカルモデル", "claudeをオフラインで実行", "ローカルAIコーディングエージェント", "ollama launch claude", "claude desktop ollama", "ローカルLLMコーディング", "プライベートAIコーディング", "オフラインAIコーディング", "ローカルAIエージェント", "qwen3.8", "glmクラウドモデル", "ツール呼び出しモデル", "claude codeのセットアップ", "無料のclaude code", "APIキーなしでclaude", "ローカルモデルのコンテキストウィンドウ", "llama.cpp", "ollama cloud", "AIコーディングのプライバシー", "エアギャップAI", "DevOps向けAIツール"]
cover: "/img/cover/claude-cowork-setup-guide-local-models-2026.webp"
coverAlt: "コーディング画面を表示したコンピューター、タブレットやスマートスピーカーなどの機器が置かれた、光る色のアクセントがある濃紺のハイテク作業スペース。"
coverCaption: ""
ref: ["/articles/local-ai-2026-build-your-rig-now", "/articles/ai-models-raspberry-pi-4-5"]
---

**Claudeのエージェント機能を、自分のハードウェア上のモデルで実行できるようになりました。APIキーもサブスクリプションも不要で、データもマシンの外に送られません。** OllamaはAnthropic互換APIを提供し、Claude CodeとClaude Desktopは数個のコマンドで接続できます。

*多くのガイドは重要な点を一つ誤解しています。Claude Coworkを説明したあとで、実際にはコマンドラインツールを設定する手順を案内しています。この二つは別の連携であり、Coworkが使えるのは一方だけです。*

このガイドでは、二つの接続方法を分けて説明し、一般的なチュートリアルで省略される環境変数、2026年9月時点で各方法に合うモデル、どのように設定してもクラウド限定のまま残る機能を紹介します。

**読み終えたときにできること:** 必要な連携を選び、Ollamaの公式手順で接続し、ツール呼び出しテストを一度行ってエンドポイントを確認できます。ローカルモデルを選び、クラウドを使う機能を避けた場合に限り、推論リクエストはローカルにとどまります。

## 要点

**OllamaはClaudeに二つの方法で接続できます。間違った方法を選ぶと、ガイドどおりに設定してターミナルは動くのにCoworkが見つからない、という結果になりがちです。**

| 連携 | 利用できる機能 | 設定方法 | プラットフォーム |
|---|---|---|---|
| **Claude Desktop** | Cowork、サブエージェント、ウェブ検索、自動モード | Ollamaアプリで **Apps** を開き、**Connect Claude** を選択 | **macOSのみ** |
| **Claude Code** | ツール呼び出しとファイル編集に対応するCLIコーディングエージェント | `ollama launch claude` または環境変数 | macOS、Linux、Windows |

**Coworkが必要ならClaude Desktop連携を使います。** Ollamaアプリ内のGUI操作で設定します。Windows対応は「近日公開」とされているため、現時点ではmacOSのみです。

**ターミナルでエージェントを使うならClaude Codeを選びます。** コマンドは一つです。

*どちらも無料です。費用がかかるのはハードウェアと電気代だけです。*

## 連携は二つ

名前が混乱の原因です。**Claude CoworkはClaude Desktopの機能**で、別アプリでもClaude Codeの別名でもありません。

Ollamaのドキュメントでは、別のページと見出しでそれぞれ紹介されています。Claude DesktopはOpenClawやHermesと同じ **Assistants** にあり、Claude CodeはOpenCode、Cline、Codex CLIと同じ **Coding** にあります。

設定方法が大きく異なるため、この違いは重要です。

- **Claude Desktop** はOllamaアプリの画面で設定します。シェルプロファイルを編集する必要はありません。
- **Claude Code** は環境変数または一つの起動コマンドで設定します。

`ANTHROPIC_BASE_URL` をエクスポートして `claude` を実行するよう案内するガイドは、コマンドラインツールを設定しています。Coworkのデスクトップ体験を期待していた場合、**設定が壊れているわけではありません。別の製品を設定しただけです。**

## Claude DesktopとCoworkの設定

この方法ではターミナルではなくOllamaアプリを使います。

### 前提条件

- **macOSにOllamaがインストール済みであること。** Windows対応は近日公開と記載されています。
- **ローカル実行なら、モデルを先にダウンロードしておくこと。** クラウドモデルを使う場合はOllamaにサインインし、クラウドモデルを有効にします。一部のクラウドモデルには有料プランが必要です。
- **Claudeがインストール済みであること。** 見つからない場合、セットアップ中にOllamaがダウンロードを提案します。

### 手順

1. Ollamaを開いて **Apps** を選択します。
2. **Connect Claude** を選択します。
3. セットアップ画面の指示に従います。求められた場合はClaudeをインストールし、指示が表示されたら再起動します。

これで設定は完了です。あとでモデルを変更するには、**Ollama Settings** を開いて **Apps** に進み、モデルを選択して **Restart Claude** を選びます。

### 引き継がれる機能

Ollamaのドキュメントでは、この連携で次の四つの機能がサポートされています。

- **Cowork** は難しいタスクを完了します。
- **サブエージェント** は大きなタスクを複数のエージェントに分けます。
- **ウェブ検索** はOllamaが標準で提供します。
- **自動モード**では、変更前に確認を求めるタイミングをエージェントが決めます。

*この一覧にCoworkが含まれている点が重要です。この連携ではCoworkを使えますが、コマンドライン連携では使えません。*

### 接続解除

接続を解除するとClaudeの以前の設定に戻るため、変更で設定が壊れることはありません。

- 画面から解除するには、**Apps** でClaudeを切断し、求められたらClaudeを再起動します。
- ターミナルからは `ollama launch claude-desktop --restore` を実行します。
- **Claudeの接続中にOllamaを終了すると、Claudeの通常の設定も復元されます。** ローカル設定を維持するには、Ollamaを起動したままにします。

{{< figure src="claude-desktop-ollama-integration-flow.webp" alt="OllamaアプリのAppsパネルからClaude Desktopへ接続し、モデル選択をOllama設定経由で行い、元の設定へ戻す手順を示す図" >}}

## CLIからClaude Codeを設定

ほとんどのガイドが扱う方法です。ターミナルで作業する場合はこちらを使います。

### 一つのコマンドで設定

```bash
ollama launch claude
```

このコマンドは必要な環境変数を設定し、Claude CodeをローカルのOllamaインスタンスに接続して起動します。一覧からモデルを選び、Enterを押します。モデル名を最初から指定する場合は、フラグを追加します。

```bash
ollama launch claude --model qwen3.5
```

*ラッパーが環境変数を設定します。それでも次のセクションを読んでください。設定内容を知っておけば、あとで問題を診断できます。*

### 環境変数を手動設定

```bash
export ANTHROPIC_AUTH_TOKEN=ollama
export ANTHROPIC_API_KEY=""
export ANTHROPIC_BASE_URL=http://localhost:11434

claude --model qwen3.5
```

**よくあるガイドが省略するのは二行目です。** `ANTHROPIC_API_KEY` を空文字列にすると、環境内にエクスポート済みの実際のキーがローカル接続に干渉しません。変数だけを説明するガイドを公開してこの行を省くと、キーを設定済みの読者は原因の分かりにくいエラーに遭遇します。

シェルプロファイルを変更せずに使うには、すべてを一行で渡します。

```bash
ANTHROPIC_AUTH_TOKEN=ollama ANTHROPIC_BASE_URL=http://localhost:11434 ANTHROPIC_API_KEY="" claude --model kimi-k2.7-code:cloud
```

公式ドキュメントで知っておくべき点は二つです。

- **`ANTHROPIC_AUTH_TOKEN` はBearer認証を渡します。** そのためローカルモードでは、値として文字列 `ollama` を指定します。
- **Claude自身の設定ファイルはシェル変数より優先されます。** 新しい値をエクスポートしたあとに接続がおかしい場合は、設定ファイルを確認し、Claude Code内で `/status` を実行して使用中のエンドポイントを確認します。

### Ollama Cloudに直接接続

この方法ではOllamaをインストールする必要はありません。APIキーを設定し、Claude CodeをOllamaのホスト済みエンドポイントに接続します。

```bash
ANTHROPIC_BASE_URL=https://ollama.com \
ANTHROPIC_AUTH_TOKEN="$OLLAMA_API_KEY" \
ANTHROPIC_API_KEY="" \
claude --model glm-5.3-flash
```

**この方法には注意点があります。** Ollamaのドキュメントによると、ホスト型のウェブ検索と高度なツール制御は完全にはサポートされません。互換モデルなら基本的なチャット、ファイル編集、ツール呼び出しは使えます。

## 2026年9月時点のモデル選択

2026年にモデルのラインナップは大きく変わりました。春に書かれた情報は再確認しましょう。現状は次のとおりです。

| モデル | 種類 | コンテキスト | 選ぶ理由 |
|---|---|---|---|
| **Qwen3.8 27B** | ローカル、18 GB | 256K | 画像入力、ツール呼び出し、思考制御に対応する、現時点で最も汎用的なローカルモデル |
| **Qwen3 Coder Next** | ローカル、MoEは合計80B / 有効3B | 256K | 常時稼働するコーディングエージェント向け。思考なしモードは高速 |
| **Qwen3.6 35B A3B** | ローカル、MoEは35B / 有効3B | 262K | Apache 2.0で、控えめなメモリでも効率的 |
| **kimi-k2.7-code:cloud** | クラウド | 大 | ローカルハードウェア不要のコーディング向けクラウドモデル |
| **glm-5.3-flash** | クラウド | 大 | Ollamaのドキュメントが最初に推奨するモデル |

**メモリに余裕があれば、Qwen3.8 27Bから始めます。** 256Kのコンテキスト、ネイティブ画像入力、ツール呼び出し、リクエストごとに切り替えられる思考機能を備え、ローカルで動作します。24 GB以上のGPUなら日常利用にも適しています。

**足りない場合はクラウドモデルから始めます。** Claude Codeをホスト型モデルに向ければ、ハードウェアの問題はなくなります。その代わり、コードはマシンの外に送られます。

### 三値モデルについての注意

**[2026年のローカルAIガイド](/articles/local-ai-2026-build-your-rig-now/)**を読んだ方は、三値のBonsai 2 27Bが**5.53 GiB**で完全な27Bモデルを動かすことをご存じでしょう。ここでも使いたくなります。

**このワークフローでは動きません。** 三値カーネルはPrism MLのllama.cppフォークにあり、標準のOllamaはそのファイルを読み込めません。`ollama launch claude --model Ternary-Bonsai-2-27B` のようなコマンドは推論前に失敗します。Claude Codeには標準のQwen3.8 27Bパッケージを使い、三値パッケージは対応ランタイム用に残してください。

*ここでは利便性と最大効率が別の方向に向かいます。統合ツールは標準GGUFを必要とします。*

## モデルを責める前にコンテキストを64Kに設定

Ollamaのドキュメントは、リポジトリ作業について一つ明確に指示しています。モデルを選び、**コンテキストウィンドウを64K以上に設定**し、大きなリポジトリではさらに増やします。

理由は技術的なものです。Claude Codeはファイル内容、差分、コマンド出力をコンテキストウィンドウに取り込みます。小さな初期値のままだと、タスクの途中で容量が尽きます。設定の問題なのに、推論能力の問題のように見えます。

| コンテキスト | 対応する作業 |
|---|---|
| 32K未満 | 単一ファイルの編集や短い質問 |
| **64K** | 小規模リポジトリで複数ファイルを扱う作業 |
| 128K | 大きなリポジトリや長いコマンド出力 |
| 256K | Qwen3.8 27Bの最大ウィンドウ |

*Claude Codeがタスクの途中で流れを見失ったら、モデルを変える前にコンテキスト設定を確認してください。*

## 一つのリクエストでツール呼び出しを確認

ツール呼び出しがあるかどうかで、エージェントとテキスト生成モデルが分かれます。想定だけで済ませず、確認してください。

Claude Codeの起動後、次のように依頼します。

```text
現在のディレクトリを読み、すべてのファイルを一覧表示します
```

**実際のファイル一覧が返れば、ツール呼び出しは動作しています。** ディレクトリを読んだ場合の説明だけを返すなら、ツール呼び出しは接続されていません。コーディング用の指示を付けたチャットモデルを使っている状態で、プロンプトを工夫しても直りません。

次の順番で確認します。

1. **ツール対応が確認されているモデルに切り替えます。** 対応していないモデルもあり、パラメーター数を見ても違いは分かりません。
2. **環境がOllamaを指していることを確認します。** `ollama --version` を実行し、`ANTHROPIC_BASE_URL` がローカルのエンドポイントを指すか確認します。
3. **Claude Code内で `/status` を実行します。** Claude独自の設定にあるベースURLや認証情報は、最近エクスポートしたシェル変数より優先されます。

## クラウド限定の機能

ローカル推論を中心にワークフローを組み直す前に、境界を確認しましょう。

| 機能 | ローカルモデル | クラウド |
|---|---|---|
| チャットとファイル編集 | 対応 | 対応 |
| ツール呼び出し | モデルによる | 対応 |
| サブエージェント | 対応 | 対応 |
| ウェブ検索 | Ollama経由で提供 | 対応 |
| **Cowork** | Claude Desktop連携経由 | 対応 |
| 自動モード | Claude Desktop連携経由 | 対応 |
| スケジュール済みプロンプト | Claude Code内の `/loop` 経由 | 対応 |

ローカル側には三つの注意点があります。

- **速度が落ちる前に、複数ファイルをまたぐ推論の質が落ちます。** ローカルモデルは1ファイルなら得意で、3ファイルなら許容範囲ですが、リポジトリ全体は苦手です。作業の規模をモデルに合わせます。
- **一部のクラウドモデルには有料のOllamaプランが必要です。** クラウドモデルを有効にしてサインインする必要もあります。
- **クラウドへ直接接続すると一部の機能を使えません。** ローカルのOllamaを使わない場合、ホスト型ウェブ検索と高度なツール制御は完全にはサポートされません。

*ローカル推論は範囲が明確で検証可能な作業に優れ、大規模で曖昧な作業には向きません。この境界に合わせて計画します。*

## 自動化

二つの機能で、対話型ツールの枠を超えた使い方ができます。

### スクリプトやCIでのヘッドレス実行

`--yes` フラグは対話型の選択を省略し、必要ならモデルを取得します。`--model` が必要で、`--` より後の内容はClaude Codeにそのまま渡されます。

```bash
ollama launch claude --model gemma4:cloud --yes -- -p "how does this repository work?"
```

**権限モデルに注意してください。** Claude Codeはほとんどの操作の前に確認します。そのためヘッドレス実行には、設定済みの権限ルールか隔離環境が必要です。大切なリポジトリを無人のエージェントに向けないでください。

### `/loop` を使ったスケジュール済みプロンプト

Claude Codeのセッション内で `/loop` を使うと、指定間隔でプロンプトまたはスラッシュコマンドを実行できます。

```text
/loop 30m 未対応のPRを確認し、状態を要約します
/loop 1h 最新のAIニュースを調べ、主な動向を要約します
/loop 15m 新しいGitHub issueを確認し、優先度順に整理します
```

*セッションが開いている間だけ実行されます。バックグラウンドデーモンではないため、セッションを閉じると停止します。*

## トラブルシューティング

| 症状 | 考えられる原因 | 対処方法 |
|---|---|---|
| **接続拒否** | Ollamaが起動していない | `ollama serve` を実行し、`curl http://localhost:11434/api/tags` で確認します |
| **操作を実行せず説明する** | 選択したモデルにツール呼び出し機能がない | ツール対応が確認されたモデルに切り替えます |
| **ローカルエンドポイントではなく実APIキーを使う** | `ANTHROPIC_API_KEY` がまだエクスポートされている | 上記のように空文字列を設定します |
| **設定後にCoworkが表示されない** | Claude DesktopではなくClaude Code CLIを設定した | CoworkにはOllamaの **Apps** 連携を使います |
| **生成が遅い** | コンテキストが大きすぎる、または疎なモデルより密なモデルを選んでいる | コンテキストを小さくし、次にMixture of Expertsモデルを試します |
| **エクスポートした変数が効かない** | Claudeの設定ファイルがシェル変数より優先される | 設定ファイルを確認してから `/status` を実行します |
| **バックグラウンドリクエストが失敗する** | Claude Codeが内部タスクに小型モデルを使おうとする | 小型モデルの上書き先を同じローカルモデルにします |

*この七つのうち二つは同じ原因です。設定トラブルの多くは、エンドポイントの誤りかツール呼び出し非対応モデルに起因します。*

## 主なポイント

- **Claude DesktopとClaude Codeは別々の連携です。** CoworkはClaude Desktopにあり、macOS上でOllamaの **Apps** パネルから設定します。CLIではCoworkを使えません。
- **CLIは `ollama launch claude` の一コマンドで起動します。** 手動では三つの変数が必要で、**多くのガイドが `ANTHROPIC_API_KEY=""` を省略します**。
- **ローカルインストールは必須ではありません。** APIキーを設定して、Claude Codeを `https://ollama.com` に接続できます。
- **モデルを評価する前に、コンテキストを64K以上にします。** 小さなウィンドウは推論の失敗に見えることがあります。
- **一つのリクエストでツール呼び出しを確認します。** モデルが実行内容の説明だけを返すなら、エージェントではなくテキスト生成モデルです。
- **三値Bonsaiパッケージはここでは動きません。** Prism MLのllama.cppフォークが必要で、標準のOllamaでは読み込めません。
- **接続解除は安全です。** Ollamaを終了するとClaudeの以前の設定に戻り、ターミナルでは `ollama launch claude-desktop --restore` を実行できます。

## 次のステップ

1. ツール呼び出し対応が確認されているモデルを用意してから、Claudeの設定に進みます: **[Ollamaモデルライブラリ](https://ollama.com/library)**
2. 現行のフラグとモデル一覧は、OllamaのClaude Codeページで確認します: **[Claude Code連携](https://docs.ollama.com/integrations/claude-code)**
3. Coworkを使う場合はClaude Desktopのページを参照します: **[Claude Desktop連携](https://docs.ollama.com/integrations/claude-desktop)**
4. 購入前に、ローカル推論ガイドのメモリ区分で必要な機器を決めます: **[2026年のローカルAI: 27BモデルがSonnet 4.6を上回る](/articles/local-ai-2026-build-your-rig-now/)**
5. 低消費電力の小型機で常時稼働エージェントを動かす場合は、対応モデルを確認します: **[Raspberry Pi 4または5で動くAIモデルは？](/articles/ai-models-raspberry-pi-4-5/)**

## 関連記事

| 記事 | 内容 |
|---|---|
| **[2026年のローカルAI: 27BモデルがSonnet 4.6を上回る](/articles/local-ai-2026-build-your-rig-now/)** | ローカル推論のベンチマーク、三値量子化、ハードウェア選び |
| **[Raspberry Pi 4または5で動くAIモデルは？](/articles/ai-models-raspberry-pi-4-5/)** | 常時稼働する小型アシスタント向けのローカル推論 |
| **[プライバシーを守るMeshtastic向けAIアシスタントを構築](/articles/building-a-privacy-preserving-meshtastic-ai-assistant/)** | プライバシーを重視し、オフグリッド無線で動くローカルモデル |
| **[AI開発向けのおすすめVS Code拡張機能](/articles/best-visual-studio-code-extensions-for-ai/)** | ローカルコーディングエージェントと組み合わせるエディター用ツール |

## 参考資料

1. [Claude Code連携 - Ollamaドキュメント](https://docs.ollama.com/integrations/claude-code)
2. [Claude Desktop連携 - Ollamaドキュメント](https://docs.ollama.com/integrations/claude-desktop)
3. [Ollamaモデルライブラリ](https://ollama.com/library)
4. [Qwen3.8 - Ollamaモデルライブラリ](https://ollama.com/library/qwen3.8)
5. [ローカルモデルでClaude Coworkを使う - PromptSpace](https://www.promptspace.in/blog/how-to-use-claude-cowork-with-local-models-2026-guide)
6. [Prism ML llama.cppフォーク - 三値カーネル](https://github.com/PrismML-Eng/llama.cpp)
