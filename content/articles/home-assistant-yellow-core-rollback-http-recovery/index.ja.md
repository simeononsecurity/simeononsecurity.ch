---
title: Home Assistant Core 2026.11 から 2026.10.4 へのロールバック後に HTTP ストレージバージョン 3 を修復する
date: 2026-11-15
lastmod: '2026-11-18'
toc: true
draft: false
description: Yellow で Home Assistant Core 2026.11 が 2026.10.4 に戻った後に発生する HTTP ストレージバージョン 3 のエラーを修復します。安全策を組み込んだコマンドと検証済みの出力を示します。
genre:
- ホームオートメーション
- トラブルシューティング
tags:
- Home Assistant Yellow
- Home Assistant OS
- Core 2026.11 のロールバック
- Core 2026.10.4
- HTTP ストレージバージョン 3
- CM4
cover: /img/cover/home-assistant-yellow-core-rollback-http-recovery.webp
coverAlt: 黄色いコンピューターボード、切れた設定リンク、復旧したウェブダッシュボードのイラスト
coverCaption: ''
---

Home Assistant Core 2026.11 の更新に失敗し、手元の Yellow CM4 は 2026.10.4 に戻りました。Yellow はネットワーク上で到達可能でしたが、ダッシュボードを表示しなくなりました。ロールバック後の HTTP 設定ファイルはストレージバージョン 3.1 でしたが、Core 2026.10.4 が対応するのはバージョン 2.2 です。ファイルを保全し、厳密な検査を通したコピーを変換して HTTP アクセスを復旧した後、Core を 2026.11.1 に更新しました。

<!--more-->

## 要点

- **不一致を確認します。** Core のログエラーを、インストール済みリリースと HTTP ストレージバージョンに照らして確認します。
- **ファイルを保全します。** 復旧前に未変更のコピーと、デバイス外のバックアップを確保します。
- **結果を検証します。** Core の状態、保存済みリスナーポート、ダッシュボード、インストール済みバージョンを確認します。

**この事例に対する修復手順:** [HTTP ファイルを保全し](#preserve-recovery-options)、[バージョン 2.2 の候補を作成して検証し](#apply-the-tested-fix-for-version-31)、[Core を停止してからインストールし](#apply-the-tested-fix-for-version-31)、[更新後の状態を確認します](#verify-the-update-outcome)。変換処理は元のフィールドを確認し、差異があれば停止します。確認していない HTTP ファイルには適用しないでください。

## 作業を始める前に

Yellow CM4 への物理アクセス、USB-C データケーブル、動作するシリアルコンソール、利用可能なバックアップまたは保全済みの設定が必要です。手動手順ではホストシェルへのアクセスと、JSON の慎重な確認が必要です。診断と修復に少なくとも 30 分を見込んでください。大規模な環境では Core の起動やバックアップの復元にさらに時間がかかります。

## 障害を特定する

Core のログには、決定的なエラーが表示されていました。

```text
Storage file http has version 3 which is newer than the max supported version 2
```

旧バージョンの Core は `http` を読み込めませんでした。フロントエンドや HTTP に依存する他のコンポーネントも失敗しました。ルーターからリースを取得できたことや Observer ページが正常だったことは、ダッシュボードにアクセスできる証拠にはなりません。[Home Assistant Core の問題 #190583](https://github.com/home-assistant/core/issues/190583) には、Yellow を含む複数の環境で同じロールバック障害が記録されています。[私のコメント](https://github.com/home-assistant/core/issues/190583#issuecomment-6908185955) には、この Yellow で検証した復旧方法と、最終的な Core の状態を記録しました。

**Web にアクセスできなくなった原因:** Core 2026.11 は `.storage/http` を形式 3.1 で書き込みました。ロールバックで Core 2026.10.4 は戻りましたが、互換性のある HTTP ファイルは復元されませんでした。Core 2026.10.4 はストレージバージョン 3 を拒否します。この Yellow に保存されていた `intermediate_v6` プロファイルも、旧スキーマに適合しません。最初の更新が失敗してロールバックに至った理由は不明です。2026-11-15 時点でリンク先の Issue は未解決で、メンテナーが確認した修正方法は議論にありませんでした。

ファイルを変更する前に、インストール済みの Core リリースと HTTP ストアを確認します。

```bash
ha core info --raw-json | jq -r '.data.version'

storage=/mnt/data/supervisor/homeassistant/.storage
jq '{version, minor_version, pending_present: (.data.pending != null), profile: .data.stable.ssl_profile}' "$storage/http"
ha core logs | grep -F 'Storage file http has version 3'
```

以下の出力は、タイムスタンプと個人情報を削除したこの事例の結果です。

```text
2026.10.4
{
  "version": 3,
  "minor_version": 1,
  "pending_present": false,
  "profile": "intermediate_v6"
}
Storage file http has version 3 which is newer than the max supported version 2
```

以下の復旧コマンドは、Supervisor に保存されたリスナーポートと HTTP ファイルの値を比較しますが、どちらの値も表示しません。不一致の場合は、ファイルを変更する前に Core の実際のリスナーポートを確認してください。

| 状況 | 意味 |
| --- | --- |
| Core が対応するストレージバージョンは 2、ファイルの値は 3 | 旧バージョンは保存済みの HTTP 設定を読み込めません |
| HTTP ファイルと Supervisor の一覧に異なるリスナーポートがある | 原因を判断する前に Core の実際のリスナーポートを確認します |
| トップページは応答するが、Core の状態は STARTING のまま | フロントエンドの応答だけでは起動完了を確認できません |

## 復旧手段を確保する {#preserve-recovery-options}

次の更新を行う前に、Yellow の外部に利用可能なバックアップを保管してください。[Home Assistant のバックアップガイド](https://www.home-assistant.io/common-tasks/general/backups/) では、クラウドやデバイス外の保存先を説明しています。暗号化されたバックアップには復旧キーが必要です。このストレージ不整合を調査している間、NVMe データディスクを消去しないでください。

編集する前に HTTP ファイルをコピーします。

```bash
storage=/mnt/data/supervisor/homeassistant/.storage
test ! -e "$storage/http.before-recovery" &&
  cp -p "$storage/http" "$storage/http.before-recovery" &&
  cmp -s "$storage/http" "$storage/http.before-recovery"
```

コマンドが失敗したら停止してください。同名の既存の復旧コピーは変更しないでください。新しい名前を選び、続行前に確認をやり直します。

ダッシュボードを利用できない場合は、Yellow のシリアルコンソールを使います。[Linux と macOS 向け Nabu Casa ガイド](https://support.nabucasa.com/hc/en-us/articles/25454972435357-Using-the-serial-console-on-Home-Assistant-Yellow-for-debugging-Linux-macOS) に USB-C の接続方法と JP1 UART の位置があります。使用するハードウェアに対応した CM4 の手順に従ってください。

## バージョン 3.1 向けに検証した修復方法を適用する {#apply-the-tested-fix-for-version-31}

更新前の互換性がある HTTP ファイルを使う方法が最適です。完全復元が適切な場合は、Home Assistant の文書化された手順でバックアップを復元してください。単一ファイルを取り出す場合は、稼働中のファイルを置き換える前にストレージバージョンと保存済みリスナーポートを確認します。互換性がある HTTP ファイルを利用できないとき、この Yellow で検証した直接の修復手順が以下のコマンドです。

[Issue に記載された当初の回避策](https://github.com/home-assistant/core/issues/190583) は `.storage/http` を移動し、旧バージョンの Core に新しいファイルを作らせます。後続の [Yellow に関する報告](https://github.com/home-assistant/core/issues/190583#issuecomment-6749568119) では、再生成されたファイルのリスナーポートが異なっています。Web インターフェイスが復旧したと判断する前に、新しいファイルと `ha core info` を確認してください。

私の環境には `http:` の YAML ブロックも、保留中の HTTP 設定もありませんでした。また、安定設定に TLS 証明書やキーもありませんでした。保存済みプロファイルは `intermediate_v6` でした。この限定的な条件で、既存のリスナーポートを維持したバージョン 2.2 の候補ファイルを別に作成しました。

```bash
storage=/mnt/data/supervisor/homeassistant/.storage

expected=$(ha core info --raw-json | jq -r '.data.port') &&
stored=$(jq -r '.data.stable.server_port' "$storage/http") &&
test -n "$expected" &&
test "$expected" != null &&
test "$expected" = "$stored" &&
test ! -e "$storage/http.v2-candidate" &&
jq -e '
  if .version == 3 and .minor_version == 1 and
     .data.pending == null and
     .data.stable.ssl_profile == "intermediate_v6" and
     (.data.stable | has("ssl_certificate") | not) and
     (.data.stable | has("ssl_peer_certificate") | not) and
     (.data.stable | has("ssl_key") | not) and
     (.data.stable | has("trusted_proxies") | not) and
     (.data.stable | has("use_x_forwarded_for") | not)
  then .version = 2 | .minor_version = 2 | .data.stable.ssl_profile = "intermediate"
  else error("Unexpected HTTP config. Stop and inspect")
  end
' \
  "$storage/http" > "$storage/http.v2-candidate" &&

jq -e '.version == 2 and .minor_version == 2 and .data.pending == null and .data.stable.ssl_profile == "intermediate"' \
  "$storage/http.v2-candidate" >/dev/null &&

test "$(jq -r '.data.stable.server_port' "$storage/http")" = \
  "$(jq -r '.data.stable.server_port' "$storage/http.v2-candidate")"
```

稼働中のファイルを置き換える前に、上記の全コマンドが成功する必要があります。`jq` が失敗したら、候補ファイルを削除して再試行する前に内容を確認してください。[Core 2026.10.4 の HTTP ソース](https://github.com/home-assistant/core/blob/2026.10.4/homeassistant/components/http/config.py) はストレージバージョン 2.2 を定義し、`intermediate` プロファイルを受け入れます。[Core 2026.11.1 のソース](https://github.com/home-assistant/core/blob/2026.11.1/homeassistant/components/http/config.py) はバージョン 3.1 とバージョン付きのプロファイル名を使います。インストール前に、候補ファイルをインストール済みの旧 Core の `HTTP_STORAGE_SCHEMA` でも検証しました。

コンテナが稼働している間に、インストール済みの旧 Core のスキーマ検査を実行します。

```bash
docker exec homeassistant python3 -c '
import json
from homeassistant.components.http.config import HTTP_STORAGE_SCHEMA
with open("/config/.storage/http.v2-candidate") as source:
    data = json.load(source)
stable = {
    key: value for key, value in data["data"]["stable"].items()
    if key not in ("created_at", "error", "error_message")
}
HTTP_STORAGE_SCHEMA(stable)
print("Schema accepted")
'
```

スキーマが候補ファイルを拒否したら停止してください。この手順では、すべてのインテグレーションや未検証の HTTP ストア形式までは確認しません。

この候補に対するスキーマ検査では `Schema accepted` と表示されました。それ以外の結果なら、この復旧手順を中止してください。

この手動変換は、記載したフィールド構成で検証しました。TLS 設定、信頼済みプロキシ、または保留中の設定があるファイルは、個別の確認が必要です。最上位のバージョン番号だけを変更すると、旧 Core が受け入れないプロファイルが残ります。

私の環境では Supervisor に Core のジョブがあり、`ha core stop` は拒否されました。ホストコンソールから Core のコンテナを停止し、検証済みの候補を配置してから起動しました。

```bash
storage=/mnt/data/supervisor/homeassistant/.storage
jq -e '.version == 2 and .minor_version == 2 and .data.pending == null and .data.stable.ssl_profile == "intermediate"' \
  "$storage/http.v2-candidate" >/dev/null &&
  docker stop homeassistant &&
  test "$(docker inspect -f '{{.State.Running}}' homeassistant)" = false &&
  cmp -s "$storage/http" "$storage/http.before-recovery" &&
  mv "$storage/http.v2-candidate" "$storage/http" &&
  docker start homeassistant
```

停止後にコマンドが失敗した場合は、`docker start homeassistant` を実行する前に稼働中の HTTP ファイルを確認してください。ファイルが変更されていたら、最新の内容から新しい候補を作成します。この手順の後に HTTP ページが復旧しました。HTTP 応答だけでは Core の起動完了を確認できなかったため、システムの復旧を判断する前に Supervisor の状態を確認しました。

この Yellow では、その後 `docker inspect -f '{{.State.Status}}' homeassistant` が `running` を返しました。次の更新を依頼する前に `ha core info` とダッシュボードを確認してください。

## 更新後の結果を確認する {#verify-the-update-outcome}

HTTP アクセスが戻った後、Core を 2026.11.1 に更新しました。このリリースを指定するには次を実行します。

```bash
ha core update --version 2026.11.1
```

起動に時間がかかった後、コマンドは失敗を報告しました。その後 Supervisor は Core を RUNNING と記録し、`Successfully started Home Assistant 2026.11.1` と出力しました。状態を確認すると、インストール済みリリースは最新で、HTTP ファイルはストレージバージョン 3.1 に戻り、観察中にコンテナは再起動していませんでした。認証済みのダッシュボードも表示されました。**更新コマンドが失敗を報告した場合でも、最終状態を確認してください。**

長時間の更新後は、使用環境のリリース、Supervisor の健全性、コンテナの状態を確認してください。

```bash
ha core info --raw-json | jq '{version: .data.version, update_available: .data.update_available}'
ha supervisor info --raw-json | jq '{healthy: .data.healthy, supported: .data.supported}'
docker inspect -f '{{.State.Status}} restarts={{.RestartCount}}' homeassistant
```

この事例では、1 つ目と 3 つ目のコマンドから次のように個人情報を除いた結果が得られました。

```text
{
  "version": "2026.11.1",
  "update_available": false
}
running restarts=0
```

次に、通常使うローカルアドレスからダッシュボードを開き、現在の状態が読み込まれることを確認してください。次のバックアップが完了し、通常の動作を確認するまで、保存した HTTP ファイルを残しておきます。

私の Yellow で得られた証拠からは、最初の更新が失敗した原因は特定できませんでした。後のジョブの失敗メッセージにも原因は示されていません。インストール済みバージョンと正常なダッシュボードは、CLI メッセージだけより復旧後の状態を強く示しますが、Supervisor がジョブを失敗と判断した理由までは説明しません。

## 次の手順

HTTP ストレージエラーが続く場合は、保全したファイルを確認し、互換性のあるバックアップを復元するか、そのストレージバージョンを読み取れる Core リリースを実行してください。旧 Core の下で保存済みのバージョン 3 ファイルを戻すと、同じ障害が再発します。Core が RUNNING になっても個別のデバイスが利用できない場合は、そのインテグレーションを個別に調査してください。次のバックアップが完了し、ダッシュボードが応答し続けるまで、復旧コピーとクラウドバックアップを保管してください。
