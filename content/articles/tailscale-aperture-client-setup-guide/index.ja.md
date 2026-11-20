---
title: "Tailscale Aperture：2026年にAIクライアントの推論とMCPを設定する"
date: 2026-11-09
lastmod: 2026-11-20
toc: true
draft: false
description: "モデルリクエストとMCPツールをTailscale Aperture経由でルーティングします。別のデバイスやゲートウェイでCodex、Claude Code、Claude Desktop、OpenCode、Hermesを設定します。"
genre: ["人工知能", "開発者ツール", "ネットワーク"]
tags: ["Tailscale Aperture", "Apertureの設定", "AIプロキシ", "LLMゲートウェイ", "MCPゲートウェイ", "Codex Aperture", "Claude Code Aperture", "Claude Desktop Aperture", "OpenCode Aperture", "Hermes Agent Aperture", "Codex MCP", "Claude MCP", "OpenCode MCP", "Hermes MCP", "AI推論プロキシ", "Responses API", "Anthropic Messages API", "リモートMCP", "Streamable HTTP", "Tailscale", "セルフホストAI", "コーディングエージェント", "AIクライアント設定"]
cover: "/img/cover/tailscale-aperture-agent-setup.webp"
coverAlt: "Apertureは、推論用の青いルートとツール用の緑のルートを分けて、クライアントパネルをモデルおよびMCPツールサービスに接続します"
coverCaption: ""
---

## はじめに

Tailscale Apertureは、モデル推論とModel Context Protocol（MCP）ツール向けにtailnetへ接続する単一のゲートウェイをAIクライアントに提供します。各クライアントは、使用するAPIプロトコルに合ったルートを使う必要があります。MCPツールには専用のエンドポイントがあり、Apertureのgrantは各Tailscale IDが利用できるモデルとコネクタを制御します。

このガイドでは、macOS、Linux、WindowsでCodex、Claude Code、Claude Desktop、OpenCode、Hermesを設定します。CLIとデスクトップの設定を説明し、自分のIDで利用できるモデルIDを確認する方法を示します。また、別のデバイスやApertureインスタンスを設定するときに再利用できる匿名化済みプロンプトも含みます。

**ルートの選択：** エンドポイントのパスはゲートウェイとAPIプロトコルによって異なります。`/codex`のようなResponsesルートはAnthropic MessagesやMCPのトラフィックを処理しません。ゲートウェイのホスト名と各クライアントの推論ルートを確認してください。クライアント設定を変更する前に、自分のApertureアクセスでモデルIDを確認してください。

## 要点

- **モデルのトラフィック**には、クライアントのプロトコルに対応するAPIルートが必要です。
- **MCPのトラフィック**は専用の`/v1/mcp`エンドポイントを使います。
- **ゲートウェイ権限**は、自分のTailscale IDに各モデルとコネクタの使用を許可する必要があります。
- **クライアント設定**は設定が保存されたことしか証明しません。実際のリクエストとMCPツール呼び出しを確認してください。

## ルートの関係

| 目的 | クライアントのリクエスト | Apertureルート | ルートが処理する内容 |
|---|---|---|---|
| CodexとResponses互換モデル | OpenAI Responses API | 通常は`/v1`。`/codex`などのカスタムパスはデプロイによって異なります。 | モデル推論 |
| Claudeモデル推論 | Anthropic Messages API | ゲートウェイのベースURL。Apertureは`/v1/messages`を処理します。 | Claude互換の推論 |
| MCPツール | Streamable HTTP MCP | `/v1/mcp` | 設定済みコネクタのツールとリソース |

{{< figure src="aperture-client-routes.webp" alt="CodexとHermesはResponsesルート、ClaudeはAnthropic Messages、MCPクライアントは専用の/v1/mcpルートを使ってApertureコネクタに接続します" caption="モデル推論とMCPのトラフィックは別のApertureエンドポイントを使います" >}}

**プロバイダーのルートURL：** ApertureはクライアントのリクエストパスをプロバイダーのベースURLに追加します。プロバイダーの`baseurl`にはAPIのルートURLを設定します。受信パスにすでに`/v1`が含まれている場合、上流のベースURLに`/v1`を追加しないでください。URLの構成、モデル登録、grantについては[Aperture設定リファレンス](https://tailscale.com/docs/aperture/configuration)を参照してください。

## ゲートウェイの準備

**編集を始める前に、**Aperture管理者から次の情報を入手してください。

- **ゲートウェイのホスト名：** tailnetに接続した大半のクライアントでは`http://`を使います。Claude Desktopの推論には、信頼済み証明書を使用する`https://`が必要です。
- **推論ルート：** OpenAI ResponsesとAnthropic Messagesではリクエスト形式が異なります。
- **モデルID：** 下記のモデル一覧エンドポイントで、自分のTailscale IDから利用可能なモデルを確認します。そのIDに対して返されたIDをそのまま使ってください。
- **認証：** クライアントが仮のAPIキーを送るか、ユーザー認証情報を送るか確認します。
- **MCPエンドポイント：** tailnetクライアントでは通常`http://<APERTURE_HOST>/v1/mcp`です。Claude Desktopの推論には、信頼済み証明書を使用するHTTPSが必要です。
- **アクセスgrant：** 自分のTailscale IDに対するモデルとコネクタの権限を確認します。

**ネットワークアクセス：** クライアントデバイスからtailnet経由でゲートウェイに到達できる必要があります。ホスト名だけではモデルやツールへのアクセス権は得られません。該当するgrantでモデルまたはコネクタが許可されていなければ、Apertureはアクセスを拒否します。

### 自分のユーザーが利用できるモデルを確認する

**同じtailnetに接続したデバイスからモデル一覧を照会します。** ApertureはデバイスのTailscale IDを使い、そのユーザーにgrantされたモデルを返します。詳しくは[モデルgrantのガイド](https://tailscale.com/docs/aperture/how-to/grant-model-access)を参照してください。

```sh
# macOSまたはLinux
curl -fsS http://<APERTURE_HOST>/v1/models
```

```powershell
# Windows PowerShellでは、旧式のcurlエイリアスを避けるためcurl.exeを使います
curl.exe -fsS http://<APERTURE_HOST>/v1/models
```

**結果を読む：** 返された各`id`をモデルIDとして使います。`metadata.provider.id`でApertureプロバイダーを確認します。クライアントのAPI形式をサポートするモデルを選んでください。たとえばClaude DesktopにはAnthropic Messagesモデルが必要です。Apertureの[モデルディレクトリ](https://tailscale.com/docs/aperture/reference/chat)にも、サインインユーザーが利用できるIDが掲載されています。

**モデルが表示されない場合：** 期待するモデルがない場合は、Aperture管理者にプロバイダー設定と自分のモデル利用許可を確認してもらいます。このエンドポイントからユーザーが自分にアクセス権を付与することはできません。

**URLスキーム：** Tailscaleは同じtailnetに接続した多くのクライアントに`http://`を推奨しています。WireGuardが通信を暗号化します。Claude Desktopには`https://`とOSが信頼する証明書が必要です。各クライアントでは以下に示すスキームを使います。

### 推論プロバイダーを追加する

**OpenAI Responses：** 上流プロバイダーをApertureに追加し、クライアントが使うAPI形式を有効にします。OpenAIの場合は次のような設定を追加します。

```json
{
  "providers": {
    "openai": {
      "baseurl": "https://api.openai.com",
      "apikey": "<UPSTREAM_PROVIDER_KEY>",
      "models": ["<MODEL_ID>"],
      "compatibility": {
        "openai_chat": true,
        "openai_responses": true
      }
    }
  }
}
```

**Anthropic Messages：** Anthropic APIのルートURL、`x-api-key`認証形式、`anthropic_messages`互換性を使います。モデルIDはプロバイダーの`models`一覧にも必要です。次の設定例を追加します。

```json
{
  "providers": {
    "anthropic": {
      "baseurl": "https://api.anthropic.com",
      "apikey": "<UPSTREAM_PROVIDER_KEY>",
      "authorization": "x-api-key",
      "models": ["<CLAUDE_MODEL_ID>"],
      "compatibility": {
        "anthropic_messages": true
      }
    }
  }
}
```

**設定の変更：** 各プレースホルダーを上流プロバイダーの値に置き換えます。既存のAperture設定に追加し、ファイルの他の設定は維持します。プロバイダーが対応するAPIの互換性フラグを有効にしてください。

**アクセスgrant：** Apertureは各ユーザーのモデルおよびコネクタへのアクセスを制御します。必要な権限だけを各Tailscaleユーザーに付与します。この例では1人のユーザーに1つのモデルと1つのコネクタを許可します。

```json
{
  "grants": [
    {
      "src": ["<TAILSCALE_USER>"],
      "app": {
        "tailscale.com/cap/aperture": [
          {"role": "user", "models": "openai/<MODEL_ID>"},
          {"connectors": ["teamtools/**"]}
        ]
      }
    }
  ]
}
```

**モデルgrant：** grantパターンにはプロバイダーIDとモデルIDを指定します。[コネクタ設定ガイド](https://tailscale.com/docs/aperture/connectors/get-started)には現在の`connectors.servers`設定が記載されています。旧式のトップレベル`mcp.servers`設定は非推奨です。

### MCPコネクタを追加する

**MCPコネクタ：** Apertureは上流のMCPサーバーに接続し、`/v1/mcp`でツールを公開します。

```json
{
  "connectors": {
    "servers": {
      "teamtools": {
        "protocol": "mcp",
        "url": "<UPSTREAM_MCP_ENDPOINT>"
      }
    }
  }
}
```

**コネクタURL：** 上流サーバーの完全なMCPエンドポイントを指定します。その後、Tailscaleユーザーに`teamtools/**`または、より狭いツールパターンのアクセスをgrantします。[MCPプロキシリファレンス](https://tailscale.com/docs/aperture/mcp-server)で、単一のクライアントエンドポイントとコネクタの動作を確認してください。

## Codex CLIとデスクトップ

**共通設定：** Codex CLIとデスクトップアプリは同じ設定を使います。macOSとLinuxでは`~/.codex/config.toml`を編集します。Windowsでは`%USERPROFILE%\.codex\config.toml`を編集します（ホームディレクトリを展開するシェルでは`~/.codex/config.toml`も使えます）。[Codexアプリの概要](https://openai.com/index/introducing-the-codex-app/)によると、デスクトップアプリはCodex CLIの設定を読み込みます。Codexのユーザー設定は`~/.codex/config.toml`にあります。[設定の基本](https://learn.chatgpt.com/docs/config-file/config-basic)にはユーザー単位のプロバイダーとMCPの項目が記載されています。このファイルにプロバイダーを追加し、アプリを再起動して、UIにプロバイダーとモデルが表示されることを確認してください。

```toml
model = "<MODEL_ID>"
model_provider = "aperture"

[model_providers.aperture]
name = "Aperture Proxy"
base_url = "http://<APERTURE_HOST>/v1"
wire_api = "responses"
requires_openai_auth = true
supports_websockets = false
```

**オプション項目：** これらの2つの値は、Codexプロバイダー設定の一例に対応します。ゲートウェイとCodex設定で必要な場合だけ残します。Tailscaleの現行[Codex Apertureガイド](https://tailscale.com/docs/aperture/how-to/use-codex)ではこれらを省略し、`wire_api = "responses"`を使い、Apertureが上流認証情報を挿入すると説明しています。ゲートウェイ管理者から指定された正確なResponses URLを使ってください。`/codex`はデプロイ固有のルートです。Tailscaleが案内する既定ルートは`/v1`です。

**MCP設定：** 同じユーザー設定にサーバーを追加します。

```toml
[mcp_servers.aperture]
url = "http://<APERTURE_HOST>/v1/mcp"
enabled = true
```

**Codexの確認：** `codex mcp list`を実行し、新しいセッションを開始して`/mcp`を確認します。サーバー一覧は登録を示します。ツールが表示され、呼び出しに成功すれば、検出と実行も確認できます。[Codex設定リファレンス](https://learn.chatgpt.com/docs/config-file/config-reference)にはユーザー単位のプロバイダーとMCP設定が記載されています。

## Claude Code CLI

**プロトコル：** Claude CodeはAnthropic Messagesを使います。Claude Codeのグローバル設定ファイルをAnthropic互換のApertureゲートウェイに向けます。macOSとLinuxでは`~/.claude/settings.json`、Windowsでは`%USERPROFILE%\.claude\settings.json`を使います。PowerShellでは同等の`$HOME\.claude\settings.json`を使います。ルートは`/v1/messages`を処理する必要があります。Codex Responsesは別のプロトコルとルートを使います。WireGuardが接続を暗号化するため、Tailscaleはtailnet上のClaude CodeにHTTPを推奨しています。

```json
{
  "apiKeyHelper": "echo '-'",
  "env": {
    "ANTHROPIC_BASE_URL": "http://<APERTURE_HOST>"
  }
}
```

**クライアント認証：** Apertureのクライアントガイドは、Apertureが上流認証情報を挿入するため、`apiKeyHelper`にプレースホルダーを使います。Claudeのサブスクリプションをパススルーする場合、ApertureのAnthropicプロバイダーはユーザーのClaude認証情報を転送する必要があります。その場合は`ANTHROPIC_API_KEY`と`ANTHROPIC_AUTH_TOKEN`を設定しません。これらの環境変数はサブスクリプション認証情報を置き換えます。Claude Codeのバージョンに合わせて[Claude Code Aperture手順](https://tailscale.com/docs/aperture/how-to/use-claude-code)を参照し、認証方式は[Anthropicのゲートウェイガイド](https://code.claude.com/docs/en/llm-gateway-connect)で確認してください。

**HTTP経由のMCP：** 次のコマンドでエンドポイントを追加します。

```sh
claude mcp add --transport http --scope user aperture http://<APERTURE_HOST>/v1/mcp
claude mcp list
```

**Claude Codeの確認：** セッションを開始し、`/mcp`を実行して接続を確認します。Anthropicは[MCPドキュメント](https://code.claude.com/docs/en/mcp)で、リモートMCPサーバーにHTTPを推奨しています。

## Claude Desktop GUI

**別々の設定：** Claude Desktopにはサードパーティ推論の画面があります。この設定はClaude DesktopのモデルリクエストをAperture経由にします。MCP設定は別途行います。

1. macOSまたはWindows版Claude Desktopで、**ヘルプ > トラブルシューティング > 開発者モードを有効にする**を選びます。Linuxベータ版でもメニューがあれば同じ操作をします。求められた場合はアプリを再起動します。メニューがない場合はClaude Desktopを更新し、プラットフォーム固有のリリースノートを確認してください。
2. **開発者 > サードパーティ推論を設定**を選択します。
3. **接続タイプ**に**ゲートウェイ**、**認証情報の種類**に**静的APIキー**を選びます。
4. **ゲートウェイのベースURL**に`https://<APERTURE_HOST>`を入力します。信頼済みTLS証明書で保護される完全なホスト名を使います。
5. ゲートウェイキーに`aperture`などの空でないプレースホルダーを入力します。Apertureはこれを無視し、tailnet経由で認証します。
6. カスタム推論ヘッダーは空欄にします。
7. 自分のTailscale IDで`GET /v1/models`を実行して返された正確なIDを使い、有効なモデルを追加します。Anthropic Messagesモデルを選択してください。モデルID、表示名、必要ならtierの別名を手入力します。この画面でClaude Desktopがモデルを検出することはありません。
8. **変更を保存**、続いて**変更を適用**を選択します。Claude Desktopを終了して再度開きます。

**プロトコルの確認：** [ApertureのClaude Desktopガイド](https://tailscale.com/docs/aperture/how-to/use-claude-desktop)では、Claude Desktopは`/v1/messages`でAnthropic Messagesを使うと説明しています。Codexルートの`/codex`を入力したり、OpenAI互換の接続タイプを選んだりしないでください。

### Claude DesktopをMCPに接続する

**プライベートMCPアクセス：** Claude Desktopと同じコンピューターで、ローカルのstdioブリッジを実行します。Claude DesktopのローカルMCP設定に次を追加します。

```json
{
  "mcpServers": {
    "aperture": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "http://<APERTURE_HOST>/v1/mcp"]
    }
  }
}
```

**ブリッジの動作：** ローカルプロセスはコンピューターのTailscale接続を通じてApertureに接続します。OS別の設定パスを使います。macOSは`~/Library/Application Support/Claude/claude_desktop_config.json`、Windowsは`%APPDATA%\Claude\claude_desktop_config.json`です。Linuxベータ版では**設定 > 開発者 > 設定を編集**を開き、Claude Desktopが開くパスを使います。Linuxのパスはパッケージごとに異なります。Claude Desktopを再起動し、コネクタ一覧を確認して、安全なツールを1つ呼び出します。[`mcp-remote`プロジェクト](https://github.com/punkpeye/mcp-remote)にローカルからリモートへのブリッジが記載されています。

**リモートコネクタ：** Anthropicの「設定 > コネクタ」では、Anthropicのサービスから到達できるリモートサーバーが必要です。tailnet限定のホスト名はデバイスからのみ利用できるため、プライベートエンドポイントにはローカルブリッジを使います。公開MCPサービスを提供する場合は、クラウドコネクタに追加する前に認証と権限を設定してください。[AnthropicのリモートMCPコネクタガイド](https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp)を参照してください。

## OpenCode CLIとデスクトップ

**共通設定：** OpenCode CLIとデスクトップは同じOpenCode設定を読み込みます。現行のOpenCode V2ドキュメントでは、カスタムプロバイダーに`providers`マップを使い、MCPサーバーを`mcp.servers`に配置します。この例は`/v1`のOpenAI互換チャットエンドポイントを使います。このモデルルートを使う前に、ApertureプロバイダーがOpenAI Chat Completionsをサポートすることを確認してください。

**グローバル設定：** macOSとLinuxでは`~/.config/opencode/opencode.json`、Windowsでは`%USERPROFILE%\.config\opencode\opencode.json`を編集します。OpenAI互換プロバイダーを追加し、`<MODEL_ID>`をApertureの正確なモデルIDに置き換えます。コメントには同じディレクトリの`opencode.jsonc`も使えます。[設定リファレンス](https://opencode.ai/docs/config/)にグローバル設定とプロジェクト設定の優先順位が記載されています。

```jsonc
{
  "$schema": "https://opencode.ai/config.json",
  "model": "aperture/<MODEL_ID>",
  "providers": {
    "aperture": {
      "env": ["APERTURE_API_KEY"],
      "package": "@opencode/ai/providers/openai-compatible",
      "settings": {
        "baseURL": "http://<APERTURE_HOST>/v1"
      },
      "models": {
        "<MODEL_ID>": { "modelID": "<MODEL_ID>" }
      }
    }
  },
  "mcp": {
    "servers": {
      "aperture": {
        "type": "remote",
        "url": "http://<APERTURE_HOST>/v1/mcp",
        "oauth": false
      }
    }
  }
}
```

**クライアント認証：** `oauth: false`はOpenCodeの既定OAuthフローを省略します。ApertureはTailscaleで呼び出し元を識別します。OpenCodeにはプロバイダー認証項目も必要なので、ローカル環境に`APERTURE_API_KEY=-`を設定します。デスクトップアプリにも変数を渡してください。シェル環境を継承しない場合は、アプリで`/connect`を実行し、Apertureには`-`を入力します。上流プロバイダーキーをこのファイルに記録しないでください。現行形式はOpenCodeの[プロバイダーガイド](https://opencode.ai/docs/providers/)と[MCPガイド](https://opencode.ai/docs/mcp-servers/)を参照してください。`opencode mcp list`でサーバーを確認し、アプリ内の`/mcps`で状態を確認します。

## Hermes CLIとデスクトップ

**共通設定：** Hermes AgentはmacOSとLinuxで、名前付きプロバイダーとMCPサーバーを`~/.hermes/config.yaml`に保存します。Windowsネイティブ版では`%LOCALAPPDATA%\hermes\config.yaml`を使います。`hermes config path`を実行して有効なファイルを確認します。`HERMES_HOME`で既定の場所を変更できます。ローカルのHermes DesktopはCLIと同じHermesホームとプロファイルを使います。DesktopからリモートHermesゲートウェイに接続する場合は、Hermesを実行するマシンでApertureを設定し、サーバーがtailnetに接続できることを確認します。ローカルとリモートの構成は[Hermes Desktopガイド](https://hermes-agent.nousresearch.com/docs/user-guide/desktop)を参照してください。

**Responsesプロバイダー：** 名前付きプロバイダーを追加します。`api`にはApertureインスタンスのResponsesエンドポイントを指定します。

```yaml
providers:
  aperture:
    api: "http://<APERTURE_HOST>/v1"
    transport: codex_responses
    default_model: "<MODEL_ID>"
    # Apertureの設定でクライアントキーが必要な場合だけkey_envを追加します。
    # key_env: APERTURE_API_KEY

model:
  provider: "custom:aperture"
  default: "<MODEL_ID>"
```

**プロトコルの選択：** OpenAI Chat Completionsでは`transport: chat_completions`を設定します。Anthropic Messagesでは`transport: anthropic_messages`を選び、Anthropic MessagesゲートウェイURLを使います。Hermesの名前付きプロバイダーが使う`api`、`transport`、`default_model`については現行の[プロバイダーガイド](https://hermes-agent.nousresearch.com/docs/integrations/providers)を参照してください。

**MCP設定：** 同じYAMLファイルにAperture MCPを追加します。

```yaml
mcp_servers:
  aperture:
    url: "http://<APERTURE_HOST>/v1/mcp"
    enabled: true
```

**Hermesの確認：** `hermes mcp`を実行し、対話型サーバー選択画面で各接続を確認します。ローカルDesktopも同じ設定プロファイルを使います。Hermesの[リモートHTTP MCPサーバー](https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp)と[MCP設定リファレンス](https://hermes-agent.nousresearch.com/docs/reference/mcp-config-reference)を参照してください。

## 2つの経路を確認する

**モデル推論とMCPを別々に確認します。**

1. Tailscale接続とゲートウェイへの到達性を確認します。Claude Desktopでは、ゲートウェイが信頼済みTLS証明書を提示することも確認します。
2. 設定した各クライアントから短いプロンプトを送ります。Apertureのセッション一覧に対応するリクエストが表示されることを確認します。
3. 選択したモデルIDが、自分のTailscale IDにgrantされたモデルと一致することを確認します。
4. クライアントのMCP状態画面または一覧コマンドを使います。Apertureサーバーが接続し、想定するツールを公開していることを確認します。
5. 読み取り専用ツールを1つ呼び出します。返された内容を上流の情報源と照合します。
6. モデルまたはツールの呼び出しに失敗した場合はApertureログを確認します。設定を保存しただけではリクエスト成功の証明になりません。

| 症状 | 確認内容 |
|---|---|
| モデルリクエストが404または405を返す | クライアントのエンドポイントが正しいルートとプロトコルを使っているか確認します。Anthropic MessagesやMCPに`/codex`を使わないでください。 |
| モデルが利用できない | 対象のTailscaleユーザーとして`/v1/models`を照会します。正確なIDが表示され、API形式がクライアントに合うことを確認します。プロバイダーやgrantの不足を管理者に確認してもらいます。 |
| リクエストが未認証になる | クライアントが仮の値、ベアラートークン、サブスクリプションのパススルーのどれを必要とするか確認します。上流プロバイダーキーを公開プロジェクトファイルにコピーしないでください。 |
| MCPサーバーは一覧にあるがツールが表示されない | `/v1/mcp`、コネクタの状態とgrant、クライアントからApertureへのネットワーク経路を確認します。 |
| Claude DesktopがプライベートMCP URLに接続できない | `mcp-remote`などのローカルブリッジを使うか、適切な認証を設定した承認済みの公開コネクタを使います。 |

## 別のデバイスで設定を再現する

**新しいデバイス：** 同じクライアントをインストールし、先にデバイスをtailnetへ接続します。新しいデバイスから`/v1/models`を照会し、そのTailscale IDにgrantされたモデルを確認します。設定の構造を使い、認証情報はローカルに保管します。`<APERTURE_HOST>`、`<MODEL_ID>`、`<UPSTREAM_MCP_ENDPOINT>`を対象Apertureインスタンスの値に置き換えます。APIプロトコルごとに別のエンドポイントを使い、ツール用に`/v1/mcp`を設定します。最後にモデルリクエストとMCPツール呼び出しを1つずつ確認します。

**複数のゲートウェイ：** Apertureインスタンスごとに設定を分けます。CodexとHermesにはResponses、ClaudeにはAnthropic Messages、ツールにはMCP集約エンドポイントが必要です。API認証情報は各クライアントのローカルシークレットストアまたは環境変数に保存します。共有の`config.toml`、`opencode.json`、`config.yaml`や公開リポジトリにAPIキーをコピーしないでください。

## 再利用できるAperture設定プロンプト

**この匿名化済みプロンプトを**コーディングアシスタントにコピーし、プレースホルダーをゲートウェイの情報に置き換えます。モデルIDを選ぶ前に、アシスタントは自分のTailscale IDとしてApertureを照会する必要があります。

```text
このデバイスにある既存のTailscale ApertureゲートウェイとAIクライアントを設定してください。

対象クライアント：Codex CLIとデスクトップ、Claude Code、Claude Desktop、OpenCode CLIとデスクトップ、Hermes CLIとデスクトップ。

まずデバイスがmacOS、Linux、Windowsのどれを実行しているか検出し、現在のシェル（zsh、bash、PowerShellなど）を特定してください。そのOSに合うパスとコマンド構文を一貫して使います。現在のゲートウェイ、Tailscale接続、クライアントのバージョン、既存の設定を先に調べてください。最新の公式ドキュメントを読みます。無関係な設定を維持し、各ファイルを編集する前にバックアップします。ホスト名、モデルID、APIルート、認証情報を推測しないでください。上流プロバイダーキーはApertureに保管し、クライアントファイルやこのリポジトリには保存しません。

このTailscale接続デバイスから使えるモデルを調べてください。
1. クライアントが使うTailscale IDで`http://<APERTURE_HOST>/v1/models`を照会します。ゲートウェイが異なるモデル一覧URLを指定している場合はそれを使います。
2. 各モデルの`id`と`metadata.provider.id`を読みます。この一覧は自分のIDにgrantされたモデルを示します。管理者の一覧で代用したり、IDを作ったりしません。
3. 各クライアントに適したAPI形式のモデルを選びます。CodexはOpenAI Responses、ClaudeクライアントはAnthropic Messagesを使います。OpenCodeとHermesには互換プロバイダーとtransportが必要です。
4. 可能なら既存のデフォルトモデルを維持します。クライアントにデフォルトが必要で、私に希望がなければ、互換モデルを示して選択を尋ねます。Claude Desktopでは正確なモデルIDを手入力します。
5. 適切なモデルが返らない場合、管理者権限があるときだけプロバイダーとgrantの設定を確認します。権限がなければ、管理者が追加すべきモデルアクセスを報告します。自分にアクセスを付与しません。

Apertureのデプロイと設定元を見つけます。ファイルパスを決めつけたり、設定全体を置き換えたりしません。OpenAI Responsesには`openai_responses`、Anthropicには`anthropic_messages`が必要です。MCPコネクタは現在の`connectors.servers`設定に置き、クライアントは`/v1/mcp`に接続します。

共有ゲートウェイを変更する前に、プロバイダー、コネクタ、grantの最小diffを作ります。私に管理者権限があり、この依頼がゲートウェイ変更を許可する場合だけ適用します。権限がなければ、インスタンス所有者向けに正確な変更案を示します。所有者の明示的な許可なくgrantを作成したり拡大したりしません。既存のゲートウェイ設定を維持します。

インストール済みクライアントを、現在の公式形式とOS別のパスで設定します。
- Codex CLIとデスクトップはmacOS/Linuxの`~/.codex/config.toml`、Windowsの`%USERPROFILE%\.codex\config.toml`を共有します。Apertureプロバイダー、互換モデル、`wire_api = "responses"`、`mcp_servers`内のMCPを設定します。
- Claude Codeは`ANTHROPIC_BASE_URL`とHTTPリモートMCPを使います。macOS/Linuxでは`~/.claude/settings.json`、Windowsでは`%USERPROFILE%\.claude\settings.json`を使います。
- Claude Desktopでは開発者モード、サードパーティ推論、Gateway、静的APIキー、信頼済み証明書を持つHTTPSゲートウェイURL、自分のユーザーで確認したモデルIDを使います。プライベートtailnet上のMCPにはローカル`mcp-remote`ブリッジを使います。利用可能なら「設定 > 開発者 > 設定を編集」でMCP設定を探し、なければOS別の公式パスを使います。
- OpenCodeは現在のV2 `providers`スキーマと`mcp.servers`を使います。グローバル設定はmacOS/Linuxで`~/.config/opencode/opencode.json`、Windowsで`%USERPROFILE%\.config\opencode\opencode.json`です。Aperture MCPでは`oauth: false`にします。必要ならローカルの仮APIキーを使います。
- Hermesは名前付きプロバイダー、モデルAPIに合うtransport、`mcp_servers`を使います。macOS/Linuxでは`~/.hermes/config.yaml`を使います。Windowsでは`hermes config path`を確認し、通常は`%LOCALAPPDATA%\hermes\config.yaml`です。Hermes Desktopがローカルプロファイルを共有するか確認します。

クライアントが対応する場合、tailnet通信にはHTTPを使います。Claude Desktop推論には、信頼済み証明書を使うHTTPSが必要です。ゲートウェイが別ルートを指定していなければ`/v1`を使います。

設定したクライアントを再起動します。Apertureでクライアントごとにモデルリクエストを1回確認し、読み取り専用の安全なMCPツールを1つ呼び出します。自分のIDで利用できたモデル、変更したクライアントとファイル、検証結果、残る管理者作業を報告します。ソフトウェアをインストールせず、ゲートウェイを公開せず、commitや公開を行いません。
```

## まとめ

Apertureを正しく使うには、到達可能なゲートウェイ、クライアントプロトコルに合うモデルルート、必要なモデルとMCPコネクタへのgrantが必要です。同じ設定パターンはmacOS、Linux、Windowsで使えますが、設定の保存場所はクライアントとOSによって異なります。

モデルを使うTailscale IDとしてモデルIDを確認します。モデル推論と`/v1/mcp`を別々に設定し、実際のリクエストと読み取り専用ツール呼び出しを確認してください。別のデバイスやApertureインスタンスへ移るときは、このガイドの構成を再利用し、そのインスタンスのルートとgrantを確認し、認証情報をローカルのシークレットストアに保存します。

## 次のステップ

**MCPの実践：** 保存済みサーバーと検証済みツール呼び出しの違いは、[MCPサーバー設定：権限、ツールテスト、安全な削除](/articles/effective-ai-mcp-server-setup/)を参照してください。セルフホスト構成全体については、[ハイブリッドAIエージェントフリート：Tailscale、LiteLLM、Hermes](/articles/hybrid-agentic-ai-fleet-tailscale-litellm-hermes/)を参照してください。
