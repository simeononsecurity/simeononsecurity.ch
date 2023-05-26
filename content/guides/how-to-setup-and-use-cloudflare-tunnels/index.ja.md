---
title: "Cloudflare トンネルを設定する：ネットワークトラフィックを合理化し、安全にする"
draft: false
toc: true
date: 2023-05-26
description: "ネットワークトラフィックを合理化・保護し、パフォーマンスとセキュリティを強化するCloudflare Tunnelsのセットアップ方法をご紹介します。"
tags: ["クラウドフレア トンネル", "ネットワークセキュリティ", "ウェブサイトパフォーマンス", "プロキシサーバー", "ウェブトラフィック", "ネットワーク構成", "Ubuntuサーバー", "Cloudflareアカウント", "オーセンティケーション", "トンネルの作成", "トラフィックのルーティング", "DNSレコード", "セキュアコネクション", "ウェブサイトホスティング", "プロキシサービス", "ネットワーク保護", "パフォーマンスの最適化", "Cloudflareとの連携", "サーバー構成", "トラフィックエンクリプション", "ネットワークトラフィックマネジメント", "セキュアなウェブホスティング", "ウェブサイトセキュリティ", "Ubuntuのセットアップ", "トンネリング技術", "Cloudflareのサービス", "ネットワークパフォーマンス", "ウェブセキュリティ", "サーバーセキュリティ", "トラフィックマネジメント", "Cloudflare プロキシ"]
cover: "/img/cover/An_illustration_showing_a_network_tunnel_connecting_a_local.png"
coverAlt: "ローカルサーバーとCloudflareロゴを結ぶネットワークトンネルを示すイラストで、安全で合理的なネットワークトラフィックを象徴しています。"
coverCaption: ""
---

**Cloudflareトンネルの設定に関するガイド**」を掲載しました。

## はじめに
Cloudflare Tunnelsは、ローカルネットワークとCloudflareの間の直接接続を確立することにより、ウェブサイトを安全にホストする方法を提供します。このガイドでは、ウェブサイトのセキュリティとパフォーマンスを向上させるために、Cloudflare Tunnelsを設定するプロセスを説明します。

______

## なぜCloudflare Tunnelsなのか？
Cloudflare Tunnelsは、攻撃ベクトルの削減やネットワーク構成の簡素化など、いくつかのメリットを提供します。Cloudflareをプロキシとして利用することで、外部ポートを閉鎖し、すべてのトラフィックがCloudflareの安全なネットワークを経由するようにすることができます。これにより、お客様のウェブサイトをより一層保護することができます。

______

## 前提条件
Cloudflare Tunnelsをセットアップする前に、以下のことを確認してください：

1.アクティブなCloudflareアカウント。
2.Ubuntuが動作するサーバー。

______

## ステップ1：インストール
はじめに、UbuntuサーバーにCloudflare Tunnelsパッケージをインストールする必要があります。以下のステップに従ってください：

1.Ubuntu サーバーでターミナルを開きます。
2.以下のコマンドを実行し、Cloudflare Tunnelsパッケージの最新版をダウンロードします：

```shell
wget -q https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64.deb
```

## ステップ2：認証
次に、Cloudflare Tunnels サービスで Cloudflare アカウントを認証する必要があります。以下のステップに従ってください：

1.ターミナルで以下のコマンドを実行します：

```shell
cloudflared tunnel login
```

2.トンネルで使用するサイトをクリックし、認証を完了します。

## ステップ3：トンネルの作成

いよいよCloudflare Tunnelを作成する番です。以下のステップに従ってください：

1.ターミナルで以下のコマンドを実行し、トンネルを作成します：

```shell
cloudflared tunnel create name_of_tunnel
```

2.トンネルの名前は、覚えやすく、説明的なものを選んでください。トンネル名は後で変更できないので注意してください。

3.トンネルを作成すると、トンネルのUUIDを含む重要な情報が提供されます。このUUIDは、今後の設定に必要となりますので、メモしておいてください。

4.すべてのアクティブなトンネルのリストを表示するには、コマンドを使用します：

```shell
cloudflared tunnel list
```

これにより、トンネルの名前とUUIDが表示されます。

### ステップ 4: トンネルを設定する

トンネルを設定し、トラフィックのルーティングを開始するには、次の手順に従います：

1.サーバーの Cloudflare Tunnels ディレクトリに移動します。デフォルトのロケーションは `/etc/cloudflared`

2.このディレクトリの中に、新しいファイル名 `config.yml`を、お好みのテキストエディターで編集してください。

3.config.ymlファイルに、以下の内容を入力します：

```yaml
tunnel: <your_tunnels_uuid>
credentials-file: /path/to/credentials/<UUID>.json
```

必ず交換してください。 `<your_tunnels_uuid>`をトンネルのUUIDに変更し、必要に応じて資格情報ファイルのパスを更新してください。

## ステップ5：トラフィックをルーティングする

トンネルを通じて提供する内部サービスを指定するには、次の手順に従います：

1. `Open the `ファイルを再度作成します。

2.ファイルにイングレスパラメータを追加して、Cloudflareを経由させたいサービスを定義します。例えば、以下のような感じです：

```yaml
tunnel: <your_tunnels_uuid>
credentials-file: /path/to/credentials/<UUID>.json

ingress:
  - hostname: example.com
    service: http://10.10.10.123:1234
  - hostname: subdomain.example.com
    service: http://10.10.10.123:8888
  - service: http_status:404

```

リプレース `<your_tunnels_uuid>`をトンネルのUUIDに変換し、ホスト名とサービスの詳細を設定に従って更新します。

3.config.yml ファイルを保存します。


## ステップ6：DNSレコードの作成

トンネルのホスト名とサービスのDNSレコードを作成するには、次の手順に従います：

1.ターミナルを開きます。

2.以下のコマンドで、DNSレコードを作成します：

```shell
cloudflared tunnel route dns <UUID or NAME of tunnel> <hostname>
```
リプレース `<UUID or NAME of tunnel>`を、トンネルのUUIDまたは名前で指定します。 `<hostname>`を、サービスに必要なホスト名で入力してください。

3.例えば、example.comのDNSレコードを作成するには、次のコマンドを実行します：

```shell
cloudflared tunnel route dns <UUID or NAME of tunnel> example.com
```

なお、変更はCloudflareダッシュボードのDNSセクションに反映されます。

## ステップ7：トンネルの開始

Cloudflare Tunnelをテストして開始するには、以下のステップに従います：

1.ターミナルを開く。

2.以下のコマンドを実行し、トンネルを起動します：

```shell
cloudflared tunnel run <UUID or NAME of tunnel>
```

リプレース `<UUID or NAME of tunnel>`を、トンネルのUUIDまたは名前に置き換えてください。

3.Cloudflaredがお客様のトンネルをセットアップし、そのステータスに関する情報を表示します。トンネルが正常に起動したら、次のステップに進むことができます。

4.ターミナルを終了するときにトンネルが閉じないようにするには、Cloudflaredをsystemdサービスとして実行する必要があります。次のコマンドを使用します：

```shell
cloudflared --config /path/to/config.yml service install
```

リプレース `/path/to/config.yml`へのパスと一緒に `config.yml`ファイルを作成します。

## 結論

このガイドでは、UbuntuでCloudflare Tunnelsをセットアップする手順について説明しました。これらの手順に従うことで、Cloudflareのネットワークを活用し、ウェブサイトのセキュリティとパフォーマンスを強化することができます。定期的にトンネルを監視し、必要に応じて設定を調整することを忘れないでください。

問題が発生した場合、またはさらなる支援が必要な場合は、以下のサイトを参照してください。 [official Cloudflare Tunnels documentation](https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/install-and-setup/tunnel-guide/)


## リファレンス
- [Cloudflare Tunnels Documentation](https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/install-and-setup/tunnel-guide/)
- [Cloudflare Tunnels GitHub Repository](https://github.com/cloudflare/cloudflared)
- [tcude - How to Set Up Cloudflare Tunnels on Ubuntu](https://tcude.net/creating-cloudflare-tunnels-on-ubuntu/)