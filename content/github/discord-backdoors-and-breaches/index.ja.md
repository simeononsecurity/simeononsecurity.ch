---
title: "Discord Backdoors and Breaches Bot: A Turn-Based Strategy Game Companion（ターンベース戦略ゲームコンパニオン"
date: 2023-03-10
toc: true
draft: false
description: "このプレアルファ版Discordボットを使えば、『Backdoors and Breaches』をより快適にプレイすることができます。"
tags: ["ディスコード・ボット", "バックドアと不正侵入", "ターンベースストラテジーゲーム", "ゲームコンパニオン", "ゲームプレイコマンド", "ストラテジーゲームボット", "ビーエイチアイエス", "ブラックヒルズインフォセック", "インシデントマスター", "C2チーム", "ゲームフェイズ", "ゲームセット", "ゲームプレイの説明", "ゲームチャンネル", "Pythonボット", "ドッカーボット", "ゲームオートメーション", "ゲームコラボレーション", "ゲームコーディネイト", "サイバーセキュリティゲーム", "情報セキュリティ", "ゲーム開発", "ゲームプレイのヒント", "マルチプレイヤーゲーム", "ゲームロール", "ゲームチャレンジ", "ゲームフェイズ", "ゲーム環境設定", "ドッカーズボット", "Pythonの依存関係"]
---

## Discord Backdoors and Breaches Bot - Pre Alpha

[![Docker Image CI](https://github.com/simeononsecurity/discord-backdoors-and-breaches/actions/workflows/docker-image.yml/badge.svg)](https://github.com/simeononsecurity/discord-backdoors-and-breaches/actions/workflows/docker-image.yml)

<img src="https://github.com/simeononsecurity/discord-backdoors-and-breaches/blob/main/.github/images/bnb-dark.png?raw=true" alt="バックドアと侵害のロゴ" width="200"/> （注）1．


のターン制ストラテジーゲーム『Backdoors and Breaches』のDiscordボットです。 [BHIS](https://www.blackhillsinfosec.com/projects/backdoorsandbreaches/)

### 利用可能なコマンド

- `setup-game`ゲームIDを作成し、必要な変数をすべて設定します。
- `start-game`新しいゲームを開始した後、インシデントマスターを実行する必要があります。 `setup-game`
- `join-game`プレイヤー」ロールを割り当て、ゲームチャンネルへのアクセス権を付与することで、プレイヤーがゲームに参加することを許可する。
- `play-procedure`ゲームの手順フェーズを開始し、プレイヤーは一連の課題をクリアすることで進行します。
- `play-incident-master`ゲームのインシデントマスターフェーズを開始します。プレイヤーは交代でインシデントマスターとなり、他のプレイヤーに模擬的な事件への対応方法を指示することができます。
- `play-c2`ゲームのCommand and Controlフェーズを開始します。プレイヤーは交代でC2チームとなり、他のプレイヤーと協調して一連のタスクをこなす必要があります。
- `play-persistence`システム内に隠されたバックドアを発見して排除するゲームのPersistenceフェーズを開始します。
- `play-pivot`ゲームのピボットフェーズを開始します。プレイヤーはシステムの別の部分にピボットし、調査を継続する必要があります。
- `end-game`現在のゲームを終了し、ゲームチャンネルと関連するロールを削除します。

コマンドを実行するには、次のように入力します。 `!`または `/`の後に、ゲームチャンネルでのコマンド名を入力します。たとえば、新しいゲームを始めるには、次のように入力します。 `!start-game`なお、コマンドの中には、ゲームの特定の局面でのみ使用可能なものもあります。
### ボットのセットアップ

#### Pythonを使う

1.このリポジトリをクローンするには `git clone https://github.com/simeononsecurity/discord-backdoors-and-breaches.git`
2.を使用して必要な依存関係をインストールします。 `pip install -r requirements.txt`
3.を作成します。 `config.ini`ファイルを、プロジェクトのルート・ディレクトリに、以下の内容で作成します：
```ini
[SETTINGS]
discordtoken = put_discord_bot_token_here
channel_id = put_game_channel_id_here
```
4.交換する `put_discord_bot_token_here`をDiscordのボットトークンで入力し `put_game_channel_id_here`を、ゲームをプレイさせたいチャンネルのIDで入力します。
5.を使用してボットを実行します。 `python main.py`

#### Dockerの使用

1.リポジトリをクローンして、ディレクトリに移動します：
```
git clone https://github.com/simeononsecurity/discord-backdoors-and-breaches.git
cd discord-backdoors-and-breaches
```
2.を作成します。 `.env`ファイルをプロジェクトのルートディレクトリに作成し、以下の環境変数を対応する値で追加します：
```env
BOT_TOKEN=<discord_bot_token_here>
CHANNEL_ID=<game_channel_id_here>
```
3.提供されたDockerfileを使用してDockerイメージをビルドします：
```bash
docker build -t discord-backdoors-and-breaches .
```
4.の環境変数を渡し、Dockerコンテナを実行します。 `.env`のファイルです：
```bash
docker run --env-file .env discord-backdoors-and-breaches
```

また、環境変数を直接設定することもできます。 `docker run`コマンドを使用します：
```bash
docker run -td --name bnbbot -e BOT_TOKEN=<discord_bot_token_here> -e CHANNEL_ID=<game_channel_id_here> discord-backdoors-and-breaches
```
の画像から直接引き抜くか [dockerhub](https://hub.docker.com/r/simeononsecurity/discord-backdoors-and-breaches)
```bash
docker run -td --name bnbbot -e BOT_TOKEN=<discord_bot_token_here> -e CHANNEL_ID=<game_channel_id_here> simeononsecurity/discord-backdoors-and-breaches:latest
```

