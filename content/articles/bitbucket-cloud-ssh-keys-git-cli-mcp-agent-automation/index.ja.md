---
title: "Bitbucket Cloud SSHキー：AIエージェント向け読み取り専用Gitアクセス"
date: 2026-10-11
lastmod: 2026-11-13
toc: true
draft: false
description: "AIエージェントの読み取り専用ワークフロー向けに、Bitbucket CloudのSSHキー、Git CLIアクセス、REST APIトークン、1Password、MCPツールを設定します。"
genre: ["クラウドセキュリティ", "開発者ツール", "システム管理"]
tags: ["Bitbucket Cloud", "Bitbucket SSHキー", "リポジトリアクセスキー", "プロジェクトアクセスキー", "ワークスペースアクセスキー", "Git CLI", "Bitbucket CLI", "1Password CLI", "1Password SSH Agent", "MCP", "Model Context Protocol", "REST API", "APIトークンのスコープ", "エージェントの権限", "読み取り専用自動化", "SSHホストキー"]
cover: "/img/cover/bitbucket-cloud-ssh-keys-git-cli-mcp-agent-automation.webp"
coverAlt: "Bitbucket CloudのGitアクセス、スコープ付きSSHキー、1Password、REST API読み取り、MCPツールを結ぶターミナルのワークフロー"
coverCaption: ""
---

**制限付きのエージェントワークフローでは、リポジトリの読み取り、APIの読み取り、シークレット管理、リモートへの書き込みを分けます。**ソースへのアクセスにはSecure Shell（SSH）経由のGitを使い、自動チェックアウトには読み取り専用のBitbucketアクセスキーを使います。メタデータにはREST API、承認済みツールにはModel Context Protocol（MCP）サーバーを使います。秘密鍵とAPIトークンは1Passwordに保管します。書き込みには人の承認を必須にします。

<!--more-->

## 要点

- **既定は読み取り専用：**エージェントのチェックアウトにはリポジトリまたはプロジェクトのアクセスキーを使います。どちらもpush権限を付与しません。
- **個人のID：**ユーザーアカウントに紐づく対話型作業には個人用SSHキーを使います。
- **シークレットの保管：**1Password SSH Agentを使うと、Gitは秘密鍵を読み取らずに許可された署名処理を要求できます。
- **CLIの意味：**`git`、`curl`、監査済みの小さなAPIラッパーを、実用的なBitbucketコマンドラインとして扱います。
- **MCPの境界：**範囲を絞った読み取りツールを公開します。書き込みツールは無効にするか、別の承認手順の後ろに置きます。
- **書き込みの承認：**エージェントには調査、比較、変更案の準備を許可します。push、pull request、merge、設定変更の前に人の承認を求めます。

## 始める前に

**前提条件：**Bitbucket Cloudへのアクセス、Git、OpenSSHクライアント、1Password 8、1Password CLI、サインイン済みCLIまたは承認済みサービスアカウント、サーバー承認を制御できるMCPホストが必要です。所要時間は45分です。難易度は中級です。

最初はテスト用リポジトリを使います。例にあるすべてのプレースホルダーを置き換えてください。以下のコマンドは未テストの例であり、稼働中のBitbucketアカウントやリポジトリを示すものではありません。

**バージョン：**この記事は設計上の指針であり、特定バージョンに固定した手順書ではありません。テスト前にGit、OpenSSH、1Password CLI、Teamwork Graph CLI、MCPホスト、MCPサーバーのインストール済みバージョンを確認してください。`ssh-add -l`を使う前に、現在のOS向けに1Password SSH Agentを設定します。

**認証情報をシェル、ログ、URL、Gitリモート、ソースファイルに置かないでください。**`<workspace>`、`<repository>`、`<api-token>`、`<socket-path>`などのプレースホルダーを使います。実際の秘密鍵をターミナルの記録に貼り付けないでください。

## アクセス境界を選ぶ

Bitbucket Cloudは、リポジトリ、プロジェクト、ワークスペースの各レベルでアクセスキーをサポートします。キーをコピーされた場合の影響はスコープで変わります。[公式のアクセスキー比較](https://support.atlassian.com/bitbucket-cloud/kb/difference-between-repository-project-and-workspace-access-keys/)では権限の違いを明示しています。

| アクセス方法 | スコープ | 書き込み可否 | 適した用途 |
|---|---|---:|---|
| **リポジトリアクセスキー** | 1つのリポジトリ | なし | エージェントの標準チェックアウト |
| **プロジェクトアクセスキー** | 1つのプロジェクト内のリポジトリ | なし | 少数のリポジトリ群に対する読み取り専用ジョブ |
| **ワークスペースアクセスキー** | 1つのワークスペース内のリポジトリ | あり | 書き込み計画を分けた制御下のサービス自動化 |
| **個人用SSHキー** | 1ユーザーに許可されたリポジトリ | ユーザーアカウントに従う | 対話型の管理 |
| **APIトークン** | ユーザーに紐づくAPIスコープとアカウントのアクセス範囲 | スコープによる | REST API読み取り、または一時的な書き込み作業 |

**必要な範囲で最小の境界から始めます。**リポジトリが1つで足りるなら、リポジトリキーを選びます。複数のリポジトリが同じプロジェクトにあり、読み取り専用で足りるなら、プロジェクトキーを選びます。ワークスペースキーは便利な既定値ではなく、書き込み用IDとして扱います。

Bitbucketの該当する設定画面から、最小権限のキーを作成して登録します。

1. 1つのリポジトリでRepository settings、Access keys、Add keyを開きます。公開鍵を貼り付け、キーを読み取り専用にします。
2. 複数のリポジトリにプロジェクト範囲の読み取りIDが必要な場合は、Project settings、Access keys、Add keyを開きます。
3. ワークスペースアクセスキーは、承認済みの書き込み設計がある共有ワークスペースでのみ使います。個人ワークスペースには同じワークスペースレベルの手順はありません。
4. キーのラベル、スコープ、公開鍵のフィンガープリント、所有者、ローテーション日を記録します。秘密鍵は1Passwordに保管します。

登録後、読み取り専用の接続テストを1回実行します。

```bash
git ls-remote git@bitbucket.org:<workspace>/<repository>.git HEAD
```

**期待される出力：**`HEAD`のcommit参照が1つ表示されます。未テストの例です。成功すれば、許可されたSSH IDで指定したリポジトリに到達できたことが分かります。登録したキーが選ばれたことや、書き込み権限があることまでは証明しません。リポジトリごとにキーを1つ使う設定をした後、もう一度テストしてください。

秘密鍵の保管と1Password SSH Agentの同意については、[1Password CLIとSSH Agent：AIエージェント向けのSSHキー保護](/articles/1password-cli-ssh-keys-mcp-agent-administration/)を参照してください。

## 「Bitbucket CLI」を正しく定義する

**Bitbucket CLI**という表現は、3種類のインターフェースを混同しがちです。別々に扱ってください。

- **Git CLI：**`git clone`と`git fetch`はSSHまたはHTTPSでリポジトリデータを転送します。`git diff`はローカルファイルやリビジョンを比較します。
- **RESTクライアント：**`curl`またはレビュー済みのラッパーでBitbucket Cloud Representational State Transfer（REST）APIを呼び出します。APIはデータや操作を要求するプログラム用インターフェースです。[Bitbucket Cloud REST APIリファレンス](https://developer.atlassian.com/cloud/bitbucket/rest/)には、リポジトリ、ソース、ブランチ、pull request、パイプライン、ステータスのリソースが記載されています。
- **Atlassian CLI：**`acli`はAtlassian公式のコマンドラインです。[紹介ページ](https://developer.atlassian.com/cloud/acli/guides/introduction/)で製品を説明し、[コマンドリファレンス](https://developer.atlassian.com/cloud/acli/reference/commands/)には`admin`、`jira`、`feedback`、`rovodev`の機能が載っています。このリファレンスにはBitbucket Cloudのコマンドはありません。

**Atlassian公式の`acli`コマンドリファレンスには、Bitbucket Cloudのコマンドは記載されていません。**`acli bitbucket clone`のようなコマンドを作らないでください。Git操作にはGitを、Bitbucket CloudのデータにはREST APIを使います。

### 任意のTeamwork Graph CLI

**AtlassianはTeamwork Graph CLI（`twg`）も公開しています。**[概要](https://developer.atlassian.com/cloud/twg-cli/)と[コマンド一覧](https://developer.atlassian.com/platform/teamwork-graph/twg-cli/commands/commands-catalog/)にはBitbucketのコマンド群が記載されています。セットアップコマンドは次のとおりです。

```bash
twg setup
```

このコマンドはローカルの認証状態を変更します。Bitbucketトークンを任意で設定する場合は、インストール済みバージョンのプロンプトに従います。CLIのBitbucketトークン経路はAtlassian OAuthとは別です。コマンド構文は、インストール済みバージョンと最新のコマンド一覧に合わせてください。変更操作には別のプロファイル、制限付きトークン、レビュー済みのインストール済みスキル、人の承認を使います。

**期待される結果、未テスト：**隔離したプロファイルにBitbucket認証設定が入ります。セットアップ前のプロファイル状態を記録してください。ロールバックでは、インストール済みバージョンの文書にあるログアウトまたは設定削除の手順で保存済み認証情報を削除します。

サードパーティのプロジェクトが自らをBitbucket CLIと称している場合、ソース、リリース手順、チェックサム、更新経路、認証方法、要求スコープ、ネットワーク接続先、ログ処理、書き込みコマンドを監査します。見慣れたバイナリ名だけでは、ベンダーのサポートや安全な権限を証明できません。

## SSHキーを1Passwordで管理する

[1Password SSH Agent](https://www.1password.dev/ssh/agent)は、1Passwordに保存したSSHキーをGitやSSHクライアントから使えるようにします。クライアントは許可された署名処理を要求します。秘密鍵は1Passwordアプリ内に残り、承認済みクライアントがキーを使う前に1Passwordが同意を求めます。

[1Password CLIリファレンス](https://www.1password.dev/cli/reference)は別の役割を担います。`op`はアイテム、APIトークン、サービスアカウント、自動化設定への制御されたアクセスに使います。SSH署名にはSSH Agentを使います。エージェントの作業を簡単にするためだけに、秘密鍵を一時ファイルへエクスポートしないでください。

読み取り専用コマンドでローカルCLIとAgentの状態を確認します。

```bash
op --version
ssh-add -l
```

**期待される出力：**1Password CLIのバージョンと、アクティブなAgentの公開鍵フィンガープリントが1つ以上表示されます。未テストの例です。`ssh-add -l`が空なら、選択したAgentソケットから利用できるキーはありません。

新しいキーは、1PasswordにEd25519 SSH Keyアイテムを作るか、信頼できるローカル手順で生成したキーをインポートします。用途、スコープ、ローテーション日に基づくラベルを付けます。Bitbucket Cloudには公開鍵だけを追加します。[Linux向けリポジトリアクセスキーガイド](https://support.atlassian.com/bitbucket-cloud/docs/set-up-repository-access-keys-on-linux/)には、リポジトリ設定の手順と読み取り専用の制限が記載されています。

## 最初にBitbucketのホストキーを検証する

SSHユーザー認証だけではサーバーの身元を証明できません。認証要求を送る前に、クライアントはBitbucket Cloudのホストキーを検証する必要があります。Atlassianの[SSHと2段階認証ガイド](https://support.atlassian.com/bitbucket-cloud/docs/configure-ssh-and-two-step-verification/)には公開ホストキーとknown-hostエントリー取得用の公式エンドポイントが記載されています。

比較用に公開ホストキーのデータを取得します。

```bash
curl --fail --silent --show-error https://bitbucket.org/site/ssh
```

**期待される出力：**`bitbucket.org`のOpenSSH `known_hosts`行です。未テストの例です。`~/.ssh/known_hosts`に追加する前に、返されたキーまたはフィンガープリントを独立した信頼できるコピーと比較します。

承認済みのエントリーを追加した後、厳格なホストチェックを使います。

```sshconfig
Host bitbucket.org
    StrictHostKeyChecking yes
    UserKnownHostsFile ~/.ssh/known_hosts
```

**エージェント実行中に変更されたホストキーを受け入れないでください。**実行を停止し、Bitbucket Cloudの最新ホストキーレコードを確認して、ローカルの`known_hosts`エントリーを調べます。自動受け入れはキーによるセキュリティ境界をなくします。

## リポジトリごとにキーを1つ選ぶ

1台のデバイスに複数のBitbucketキーがあることは珍しくありません。広い範囲のSSH Agentは、1回の接続で複数のIDを提示します。認証試行回数の上限が小さいサーバーやポリシーでは、先に提示したキーが失敗すると正しいキーまで拒否されることがあります。

Atlassianの[複数リポジトリアクセスキーガイド](https://support.atlassian.com/bitbucket-cloud/docs/managing-multiple-repository-access-keys-on-one-device/)は、リポジトリのGit設定ファイルに`core.sshCommand`を、グローバルGit設定に`includeIf`を使います。リポジトリごとにキーを1つ使う場合も同じパターンにします。

ファイルを使うポータブルな例：

```ini
# 1 つのローカルリポジトリ内の .gitconfig
[core]
    sshCommand = ssh -o IdentitiesOnly=yes -i ~/.ssh/<repository-automation-key>
```

```ini
# ~/.gitconfig
[includeIf "gitdir:~/src/<repository>/"]
    path = ~/src/<repository>/.gitconfig
```

上のブロックは、専用の自動化ID向けに秘密鍵ファイルを使う例外設定です。1Password SSH Agentは設定しません。1Password SSH Agentでは、[1Passwordセットアップガイド](https://www.1password.dev/ssh/get-started)にあるプラットフォーム別の`IdentityAgent`または`SSH_AUTH_SOCK`を設定します。一部のOpenSSH設定では`.pub`ファイルをAgent IDの選択子として使います。使う前にプラットフォームの対応を確認します。ファイル方式には対応する秘密鍵のパスが必要です。秘密鍵を求めるコマンドに`.pub`ファイルを渡したり、個人用秘密鍵をエクスポートしたりしないでください。

ローカルクローンでキーを指定する必要があれば、リポジトリ設定を明示します。同じアクセス境界を共有する複数クローンを1つのディレクトリに置く場合は`includeIf`を使います。[複数キーのガイド](https://support.atlassian.com/bitbucket-cloud/docs/managing-multiple-repository-access-keys-on-one-device/)ではBitbucketの両設定を紹介しています。

SSH経由でGitクローンを実行します。

```bash
git clone git@bitbucket.org:<workspace>/<repository>.git <local-directory>
```

**期待される出力：**Gitが`<local-directory>`を作成し、`bitbucket.org`経由でリポジトリを取得します。未テストの例です。リポジトリアクセスキーで許可されるのはcloneとpullだけです。

## 限定したREST読み取りにAPIトークンを使う

Git転送にはSSHを使います。Git転送以外のメタデータや操作にはREST APIを使います。[APIトークン権限ガイド](https://support.atlassian.com/bitbucket-cloud/docs/api-token-permissions/)には、Read、Write、Admin、Deleteなどのリポジトリスコープが記載されています。Repository Readは`read:repository:bitbucket`に対応し、pull requestへのアクセスは含みません。

読み取り自動化では、対象が必要なエンドポイントに対応していれば、Bitbucketのリポジトリまたはプロジェクトアクセストークンを優先します。ユーザーAPIトークンは、ユーザーアカウントの広いアクセス範囲を引き継ぎます。ワークスペースアクセストークンは、作業記録で広い範囲が指定されている場合のみ使います。種類を選ぶ前に[Bitbucketアクセストークンガイド](https://support.atlassian.com/bitbucket-cloud/docs/access-tokens/)を確認してください。

エージェントの読み取りには`read:repository:bitbucket`から始めます。pull requestデータが必要な場合のみ`read:pullrequest:bitbucket`を追加します。作業記録でエンドポイントと結果が指定されている場合のみ、ワークスペースまたはパイプラインのスコープを追加します。WriteとAdminのスコープには別の承認手順が必要です。

APIトークンは用途ごとに作成し、有効期限を設定してローテーション記録に残し、期限前に交換します。Atlassianの[APIトークン作成ガイド](https://support.atlassian.com/bitbucket-cloud/docs/create-an-api-token/)では、名前、有効期限、アプリの選択、スコープが必要です。作成後にトークンが表示されるのは1回だけです。

値は1Passwordまたは管理された実行時シークレットに保管します。リモートURLには入れません。1回の読み取りが必要なプロセスに限り、環境変数経由でbearerトークンを渡します。

```bash
op run --env-file=/path/to/agent.env -- \
sh -c 'curl --fail --silent --show-error \
  --request GET \
  --url "https://api.bitbucket.org/2.0/repositories/<workspace>/<repository>" \
  --header "Authorization: Bearer ${BITBUCKET_API_TOKEN}" \
  --header "Accept: application/json"'
```

`/path/to/agent.env`はリポジトリの外に置きます。ファイルには`BITBUCKET_API_TOKEN=op://synthetic-vault/synthetic-api-token/credential`のような参照を保存します。`op run`は参照を解決し、サブプロセスの実行中にcurlの子プロセスへ値を渡します。子プロセスが環境変数の値を読んだりログに記録したりするのを防ぐものではありません。プレースホルダーを実際のトークンに置き換えないでください。

**期待される出力：**選択したリポジトリのJSONメタデータです。未テストの例です。プレースホルダーがコミット対象のファイルやログで実トークンになることはありません。

長時間の自動化では、対応するCLIまたはサービスアカウントの手順で、1Passwordからプロセス環境へシークレットを渡します。トークンの有効期間を作業に合わせます。作業が早く終了した場合やホストの所有者が変わった場合はトークンを失効させます。

## MCPの読み取り範囲を小さく保つ

新しいサーバーのレビューでは、[現行のMCP仕様](https://modelcontextprotocol.io/specification/2026-07-28)と[認可ルール](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization)を使います。HTTPサーバーではトークンのaudienceチェックと401、403応答の明確な処理が必要です。

MCPホストはユーザーの同意を得ます。クライアントは1つのサーバーとの接続を維持します。サーバーはツール、リソース、プロンプトを公開します。ソース、通信方式、アカウント、権限のレビューが終わるまで、各サーバーを信頼できないコードとして扱います。

次の段落にある2025-06-18仕様のURLは過去のバージョンです。新しいレビューでは現行の2026-07-28仕様を使います。

[MCP仕様](https://modelcontextprotocol.io/specification/2025-06-18)はMCPホスト、クライアント、サーバー間の通信を定義します。サーバーはプロトコルを通じてツール、リソース、プロンプトを公開します。MCPは接続形式を標準化します。呼び出しが何に到達できるかは、ホスト、サーバー実装、アカウント、トークンスコープ、承認ポリシーで決まります。

MCPサーバーは、GitとBitbucket Cloud REST APIの範囲を絞ったアダプターとして使います。

このアダプターを、トークンの受け渡し、サーバー側リクエストフォージェリ（SSRF）、混乱した代理人の動作から保護します。SSRFではサーバーが意図しない宛先にリクエストを送ります。混乱した代理人の動作では、サーバーが呼び出し元の代わりに広い権限を使います。悪意のあるローカルサーバー、安全でないOAuthリダイレクト、過大なソースデータ応答からも保護します。許可するBitbucketのオリジンとリポジトリIDを固定します。専用のOSユーザーでローカルサーバーをサンドボックス内で実行します。ツールの結果とログからシークレットを除去します。

この節は設計を説明するもので、テスト済みMCP設定ではありません。クライアント、サーバー、通信方式、バージョン、フィクスチャは指定していません。本番リポジトリにエージェントを接続する前に、別のテストプロファイルで読み取り専用サーバーを検証してください。

読み取りツールの例：

| ツール | 制限された結果 |
|---|---|
| **`get_repository_metadata`** | 1つのリポジトリのメタデータを返す |
| **`read_source_file`** | 指定リビジョンの1つのパスを読み取る |
| **`list_branches`** | 1つのリポジトリのブランチを一覧表示する |
| **`get_pull_request`** | トークンにpull requestの読み取りスコープがある場合、1件返す |
| **`get_build_status`** | 1つのcommitのステータスデータを返す |

これらの名前は設計例であり、Atlassianのコマンド名ではありません。任意のURL、任意のシェルコマンド、生のトークン、秘密鍵のエクスポート要求、制限のないリポジトリIDをサーバーに受け入れさせないでください。

4層で権限を設定します。

1. **Bitbucket Cloud：**Gitにはリポジトリまたはプロジェクトの読み取りキーを使い、REST読み取りには最小限のAPIトークンスコープを使います。
2. **1Password：**作業用の保管庫またはサービスアカウントを1つ使い、秘密鍵のエクスポート経路は設けません。
3. **MCPサーバー：**読み取りツールの許可リスト、固定したBitbucket Cloudエンドポイント、入力検証、タイムアウト制限、シークレットを除いたログを設定します。
4. **MCPホスト：**サーバーと書き込み可能な各操作についてユーザーの承認を求め、既定プロファイルでは書き込みツールを無効にします。

*MCPツール一覧は検出できたことを示します。認可、適切なスコープ、安全な入力処理、結果の正しさまでは証明しません。*

## エージェントのワークフローを段階化する

ワークフローを明確にします。各段階で次の段階に必要な証拠を残します。

| 段階 | エージェントの操作 | 権限 | 人の確認 |
|---|---|---|---|
| **準備** | 設定、ホストキーレコード、キーのラベル、トークンスコープ、有効期限を読む | ローカル読み取り | セットアップ記録を承認 |
| **調査** | SSH経由でGit cloneまたはfetchを行い、RESTメタデータを照会する | リポジトリとAPIの読み取り | 設定後は不要 |
| **分析** | 承認済みツールでファイル、ブランチ、pull request、ビルド状態を読む | 読み取り専用MCPツール | 範囲内の読み取りでは不要 |
| **変更準備** | ローカル環境でパッチ、ブランチ計画、pull requestの草案を作る | ローカル書き込みのみ | diffと対象をレビュー |
| **書き込み承認** | リモート操作、スコープ、ロールバック手順を提示する | リモート書き込み前 | 人の承認 |
| **書き込み実行** | ブランチをpushし、pull requestを作成するか、書き込みエンドポイントを呼び出す | 短期間の書き込みID | 各操作を確認 |
| **確認** | 結果のcommit、pull request、ステータスを読む | 再び読み取り専用 | 期待した結果を確認 |

既定のエージェントプロファイルは**分析**または**変更準備**で停止します。書き込み用の別プロファイルでは、別のトークンまたはキー、短い有効期限、固定した対象、承認プロンプトを使います。リポジトリアクセスキーでは書き込み段階を実行できず、有用な技術的境界になります。

## ロールバックと削除

アクセスを削除してから、ローカル設定を整理します。

1. 該当するBitbucket設定ページで、リポジトリ、プロジェクト、ワークスペースのアクセスキーを削除します。
2. 該当するBitbucketのセキュリティページで、リポジトリ、プロジェクト、ワークスペース、ユーザーのAPIトークンを失効させます。
3. インストール済みCLIバージョンの[認証手順](https://developer.atlassian.com/platform/teamwork-graph/twg-cli/getting-started/how-authentication-works/)に従って、保存済みTeamwork Graph認証情報を削除します。以前の認証情報は承認済みのシークレット管理ツールだけに保管します。隔離プロファイルからテスト認証情報が消えたことを確認します。
4. テスト終了後、リポジトリの`.gitconfig`と`includeIf`設定を削除します。関係のないGit設定は変更しません。
5. テスト用に追加した、検証済みのBitbucketホストキー行だけを削除します。その他の承認済みホストキーは残します。
6. 外部の`agent.env`ファイルと一時出力を削除します。ホスト設定からMCPサーバーの登録を削除して、ホストを再起動します。

削除ごとに実行者と時刻を記録します。予期しないログ、プロセス記録、トランスクリプトに値が出た場合は、キーまたはトークンをローテーションします。

## ローカル参照を更新するリモート読み取りループ

リポジトリを定期的に調べるには、次の短いループを使います。

```bash
LOCAL_REPO="<local-directory>"
git -C "$LOCAL_REPO" fetch --no-tags
git -C "$LOCAL_REPO" status --short --branch
git -C "$LOCAL_REPO" log -1 --format='%H %ad %s' --date=iso-strict
```

`HEAD`はリポジトリで現在チェックアウト中の参照です。成功結果は、許可されたSSH IDが指定したリポジトリに到達したことを示します。使用されたキーやpush権限の有無は示しません。

**期待される出力：**fetchの結果、ブランチ状態、commit行が1つ表示されます。未テストの例です。`fetch`はリモートに書き込みませんが、ローカル参照と`FETCH_HEAD`を更新します。このループはpushもブランチ変更もしません。

MCPサーバーにも名前付き操作で同じ読み取り境界を設けます。ローカルシェルラッパーまたはMCPツールは、リクエスト送信前に書き込み動詞を拒否します。ツール名、リポジトリのプレースホルダー、リビジョン、結果の分類、所要時間を記録します。作業で特定ファイルが明示的に必要な場合を除き、トークン、Cookie、プライベートパス、ファイル内容をログから除外します。

## トラブルシューティング

### `Permission denied (publickey)`

アクティブなAgentソケット、選択した公開鍵、リポジトリアクセスキーの登録、`IdentitiesOnly`を確認します。リポジトリキーは対象リポジトリまたはプロジェクトに登録されている必要があります。個人キーにはアカウント権限が必要です。ワークスペースアクセスキーの書き込み境界は異なります。

### 間違ったリポジトリキーが提示される

リポジトリごとに1つのキーを`core.sshCommand`で指定するか、`includeIf`で制御するディレクトリにクローンをまとめます。`ssh-add -l`でAgentのキーを一覧表示します。1Passwordキーが多い場合は、ID選択子を明示するか、1Password SSHブックマークを使います。[1Password Agentガイド](https://www.1password.dev/ssh/agent)ではキー数とブックマークに関する注意事項を説明しています。

### SSHがホストキーの変更を報告する

エージェントを停止します。最初に`known_hosts`を削除しないでください。独立した経路でBitbucket Cloudの最新ホストキーレコードとローカルエントリーを比較します。照合できた場合に限ってエントリーを削除または置換します。

### APIが`401`または`403`を返す

トークンの有効期限と種類、エンドポイントのスコープ、アカウントまたはワークスペースの境界を確認します。リポジトリの読み取りスコープにpull requestは含まれません。書き込みエンドポイントには書き込みスコープと承認済みの書き込みプロファイルが必要です。失敗したエンドポイントを特定する前にスコープを広げないでください。

### APIはリポジトリデータを返すがpull requestがない

新規またはローテーション後のトークンに、必要最小限のpull request読み取りスコープを追加します。読み取り専用MCPサーバーで広範なユーザートークンを再利用しないでください。

### MCPサーバーにツールは表示されるが呼び出しが失敗する

サーバー登録、接続、ツール検出、実行、結果検証を分けて確認します。トークンを漏らさずにサーバーログを調べます。エンドポイントと入力形式を確認します。接続を確認してから1回だけ再試行します。2回目も失敗したら操作を未完了として記録します。

### サードパーティのBitbucket CLIが広いアクセスを求める

インストールを停止します。要求されたアクセスを作業記録と照合します。ソース、リリース署名またはチェックサム、ネットワーク接続先、シークレット保管、書き込み動作をレビューします。Atlassian CLIの公式コマンドリファレンスは、サードパーティのBitbucketバイナリをサポートしている証拠にはなりません。

## 次の手順

リポジトリまたはプロジェクトの範囲、キーのラベル、ホストキー確認日、APIスコープ、トークンの有効期限、1Passwordの所有者、MCPツール許可リスト、ログポリシー、書き込み承認者を記載した簡潔なアクセス記録を作ります。

トランスクリプトではプレースホルダーを使い、読み取り専用クローン、RESTメタデータ読み取り、MCPツール読み取りを各1回行います。結果を比較します。アクセス記録とログのレビューが終わるまで、エージェントプロファイルを読み取り専用にします。

書き込み作業が発生したら、まずローカルdiffを準備します。対象ブランチ、変更パス、要求するAPIメソッド、トークンスコープ、ロールバック手順を提示します。正確な操作について人の承認を得てから、短期間の別書き込みIDを使います。
