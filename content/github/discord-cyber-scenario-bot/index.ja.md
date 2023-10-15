---
title: "Discord Cyber Scenario Bot：サイバーセキュリティの訓練と意識を高める"
date: 2023-02-22
toc: true
draft: false
description: "クイズ、シナリオ、リーダーボード、強力なツールコマンドを提供するCyberScenarioBotが、Discord上でサイバーセキュリティのトレーニングや意識向上プログラムをどのように向上させることができるかをご覧ください。"
tags: ["ディスコード・ボット", "サイバーセキュリティトレーニング", "サイバーセキュリティ意識", "シナリオ・ボット", "クイズボット", "リーダーボード", "ツールコマンド", "ドッカー", "パイソン", "自動化試験", "Discord API", "開発者向けドキュメント", "寄贈", "マイトライセンス", "CyberScenarioBot", "サイバーセンチネル", "トレーニングを強化する", "啓蒙活動", "サイバーセキュリティシナリオ", "サーバ環境", "カスタマイズコマンド", "配備・管理", "クイズとシナリオ", "ツールコマンド", "インフォメーションコマンド", "課題・貢献", "Discord開発者向けアプリケーション", "Discord.pyのドキュメント", "デベロッパーとの協働", "コミュニティDiscordサーバー"]
---


**CyberScenarioBot**（サイバーセナリオボット

Discord Cyber Scenario, Quiz, and Cyber Awareness Training Bot.

に飛ばすことができます。 [🚀 Quick Start](#quick-start)を追加する `CyberScenarioBot`を今すぐサーバーに送信してください。

[![Docker Image CI](https://github.com/simeononsecurity/discord-cyber-scenario-bot/actions/workflows/docker-image.yml/badge.svg)](https://github.com/simeononsecurity/discord-cyber-scenario-bot/actions/workflows/docker-image.yml)

## はじめに

このボットは、サイバーセキュリティのトレーニングや意識向上プログラムにおいて、ユーザーが様々なサイバーセキュリティのシナリオに触れ、その予防や対応方法を学ぶのに有用であると考えられる。Discordボットを使用することで、シナリオをサーバー環境のユーザーと簡単に共有することができ、ボットは必要に応じて追加のコマンドや機能を含むようにカスタマイズすることができます。さらに、ボットはDockerコンテナで実行できるため、さまざまな環境での展開や管理が容易です。

[See the bot in action](https://discord.gg/CYVe2CyrXk)

## 🚀クイックスタート

### 実行方法
#### Pythonを使用します：
Unixベースのシステムを使用していると仮定して、ターミナルを開き、bot.pyスクリプトが配置されているディレクトリに移動します。次に、以下のコマンドを実行します：
```bash
export BOT_TOKEN="INSERT YOUR BOT TOKEN HERE"
export GUILD_ID="INSERT YOUR GUILD ID HERE (only needed for timed quizes and leaderboard)"
export LEADERBOARD_CHANNEL_ID="INSERT YOUR LEADERBOARD CHANNEL ID HERE (Only needed for leaderboard for prompts)" 
export CHANNEL_ID="INSERT YOUR CHANNEL ID HERE (only needed for timed quizes)"
export APLUSROLE="INSERT YOUR A+ ROLE ID HERE (only needed for timed quizes)"
export NETPLUSROLE="INSERT YOUR Network+ ROLE ID HERE (only needed for timed quizes)"
export SECPLUSROLE="INSERT YOUR Security+ ROLE ID HERE (only needed for timed quizes)"
export QUIZROLE="INSERT YOUR QUIZ ROLE ID HERE (only needed for timed quizes)"
python bot.py
```
Windowsベースのシステムを使用している場合、環境変数を設定するために少し異なるコマンドを使用する必要があることに注意してください。以下は、Windowsで動作するはずのコマンドの例です：
```shell
set BOT_TOKEN="INSERT YOUR BOT TOKEN HERE"
set GUILD_ID="INSERT YOUR GUILD ID HERE (only needed for timed quizes)"
set LEADERBOARD_CHANNEL_ID="INSERT YOUR LEADERBOARD CHANNEL ID HERE (Only needed for leaderboard for prompts)" 
set LEADERBOARD_PERSIST_CHANNEL_ID="INSERT YOUR LEADERBOARD PERSIST CHANNEL ID HERE (Only needed for leaderboard for prompts)" 
set CHANNEL_ID="INSERT YOUR CHANNEL ID HERE (only needed for timed quizes)"
set APLUSROLE="INSERT YOUR A+ ROLE ID HERE (only needed for timed quizes)"
set NETPLUSROLE="INSERT YOUR Network+ ROLE ID HERE (only needed for timed quizes)"
set SECPLUSROLE="INSERT YOUR Security+ ROLE ID HERE (only needed for timed quizes)"
set QUIZROLE="INSERT YOUR QUIZ ROLE ID HERE (only needed for timed quizes)"
python bot.py
```
#### Docker
Dockerコンテナを実行する際、以下のように-eフラグを使用して環境変数BOT_TOKENを渡すことができます：

```bash
docker run -e BOT_TOKEN="INSERT YOUR BOT TOKEN HERE" -it --rm simeononsecurity/discord-cyber-scenario-bot:latest
```

バックグラウンドでボットを実行するため：
```bash
docker run -td --name scenario-bot -e BOT_TOKEN="INSERT YOUR BOT TOKEN HERE" simeononsecurity/discord-cyber-scenario-bot:latest
```

スケジュールされたすべてのプロンプトとロールでボットをバックグラウンドで実行するため：
```bash
docker run -td --name scenario-bot \
-e BOT_TOKEN="INSERT YOUR BOT TOKEN HERE" \
-e GUILD_ID="INSERT YOUR GUILD ID HERE" \
-e LEADERBOARD_CHANNEL_ID="INSERT YOUR LEADERBOARD CHANNEL ID HERE" \
-e LEADERBOARD_PERSIST_CHANNEL_ID="INSERT YOUR LEADERBOARD PERSIST CHANNEL ID HERE" \
-e CHANNEL_ID="INSERT YOUR CHANNEL ID HERE" \
-e APLUSROLE="INSERT YOUR A+ ROLE ID HERE" \
-e NETPLUSROLE="INSERT YOUR NET+ ROLE ID HERE" \
-e SECPLUSROLE="INSERT YOUR SEC+ ROLE ID HERE" \
-e QUIZROLE="INSERT YOUR QUIZ ROLE ID HERE" \
simeononsecurity/discord-cyber-scenario-bot:latest
```

## 機能
### 利用可能なコマンド
*コマンドプレフィックス: '!', '/'*****.

### クイズとシナリオのコマンドです。
- **Aplus**：CompTIA の A+ 関連のプロンプトに返信します。
- **Bluescenario**：ブルーチームのシナリオで返信します。
- **CCNA**：CiscoのCCNAマルチプルチョイスのプロンプトで返信します。
- **CEH**：EC-CouncilのCEHの多肢選択式プロンプトで返信します。
- **CISSP**：ISC2 の CISSP の選択式プロンプトで返信します。
- **Linuxplus**：CompTIAのLinux+の選択式プロンプトで返信します。
- Netplus**：CompTIAのNetwork+関連のプロンプトで返信します。
- **Quiz**：Cyber Security Awarenessに関するランダムな質問で返信します。
- **Redscenario**：レッドチームのシナリオを返信します。
- **Secplus**：CompTIAのSecurity+関連のプロンプトを返信します。

#### 💯 **Leaderboard** **多肢選択問題は、動的に重み付けされます。
*多肢選択問題は、実際の試験と同様に、正解か不正解かに基づいて動的に加重されます。

- **Track your progress over time and see how you compare against others in your server*（時間の経過とともにあなたの進歩を追跡し、あなたのサーバーの他の人と比較する方法を見ます。
- 各クイズのカテゴリと同様に、全体的な*のスコアを参照してください。

### 🛠️ **ツールコマンド**について
- **Dns**：を取り込みます。 `domain name`で、A、AAAA、NS、TXTなどのレコードを返します。
- **Hash**：を取り込みます。 `1 of 4 supported algos`となっており `string`で、対応するハッシュを出力する。
- **Ping**：を受け取り `IP address`を実行し、成功メッセージと平均レイテンシ、または失敗メッセージを返します。
- **Phonelookup**：を取り込みます。 `phone number`で、キャリアとロケーションを出力します。
- **ショウダニップ**です：を取り込みます。 `IP address`で、https://internetdb.shodan.io/ から有用な情報を出力します。
- **Subnet**：を取り込みます。 `IP address`となっており `Subnet Mask`と表示され、Range、Usable IPs、Gateway Address、Broadcast Address、Supported Hostsの数が出力されます。
- **Whois**：を取り込みます。 `domain name`と、ドメインのwhois情報を出力します。

### ℹ️ **情報提供のためのコマンド**です。
- **Commands**：このメッセージで返信します。
- **Socials**：各種ボットソーシャルメディアのアカウントとウェブサイトを返信します。

### ⚙️ **簡単なセットアップ**。
- *See [🚀 Quick Start](#🚀-quick-start)

## これからの機能

これらの機能は実装が予定されていますが、私たちはそれらを追跡しており、私たちは喜んでいます。 [contributions](#contributing)を、彼らのために。

- 週間ランキングや月間ランキングなど、高度なリーダーボード機能。
- サイバーセキュリティのトレーニングのニーズに合わせて、プロンプトやクイズをカスタマイズすることができます。
- ユーザーの進歩やパフォーマンスを追跡するための高度なレポートと分析。

## 使用方法

CyberScenarioBotは、サイバーセキュリティのトレーニングや意識向上プログラムを強化するための様々なコマンドや機能を提供します。ここでは、一般的な使用例をいくつか紹介します：

1.**クイズとシナリオ**：を使用します。 `/quiz`コマンドを使用すると、ランダムなサイバーセキュリティの認識に関する質問を得ることができます。以下のようなコマンドを使用します `/aplus` `/netplus` `/secplus`をクリックすると、CompTIA認定資格に関連する特定のプロンプトにアクセスできます。以下のようなコマンドを使用します。 `/bluescenario`と `/redscenario`で、それぞれブルーチームとレッドチームのシナリオを得ることができます。

2.**Leaderboard**：クイズや認定問題に答えることで、ユーザーの進捗状況を把握し、サーバー内の他のユーザーとスコアを比較することができます。

3.**ツールコマンド**：DNS、ハッシュ、Ping、電話番号検索、Shodan IP検索、サブネット計算、ドメインWHOIS検索に関するタスクを実行するために、さまざまなツールコマンドを活用する。以下のようなコマンドを使用する。 `/dns` `/hash` `/ping` `/phonelookup` `/shodanip` `/subnet`と `/whois`の後に、適切な引数が続きます。

4.**Informational Commands**：を使用します。 `/commands`コマンドを使用して、利用可能なコマンドのリストを取得します。を使用します。 `/socials`コマンドを使用して、ボットのソーシャルメディアアカウントやウェブサイトに関する情報を取得します。

サイバーセキュリティのトレーニングを強化し、サーバーメンバーの関心を高めるために、利用可能なコマンドを自由に探索し、試してみてください。

## 問題

ユーザーが何らかの問題に遭遇したり、改善の提案がある場合は、GitHubのissueを開いて報告することができます。問題についての詳細な情報と、それを再現するための手順を提供するよう、ユーザーを奨励しています。

課題を開くには、以下の手順に従います：

1.プロジェクトの GitHub リポジトリの Issues タブに移動します： [Issues](https://github.com/CyberSentinels/discord-cyber-scenario-bot/issues)
2.新規発行」ボタンをクリックします。
3.タイトルと課題の内容を明確に記述してください。
4.トラブルシューティングに役立つ、関連するログ、スクリーンショット、コードスニペットを記載する。
5.問題を提出し、プロジェクトメンテナからの連絡を待ちます。

## 貢献

私たちはすべての貢献を歓迎します。
このプロジェクトは、以下のような開発および学習のための取り組みとして意図されています。 [the CyberSentinels club](https://cybersentinels.org)私たちは、あなたの貢献のお手伝いをし、あなたが持っているかもしれない質問に答えるのが大好きです。

### Pythonの自動テスト

このレポには自動化されたテストが含まれており、その実装方法の例を見ることができます。 [here](https://github.com/CyberSentinels/penguin-pie)

### Discord APIと開発者向けドキュメント

変更のテストや機能の実装には、いくつかのものが必要です。

- [Discord Developer Application](https://discord.com/developers/applications)
- [Discord Developers Documentation](https://discord.com/developers/docs/intro)
- [Discord.py Documentation](https://discordpy.readthedocs.io/en/stable/)

### 開発者との協働

開発の取り組みについては、コミュニティのdiscordサーバーで議論することができます。 [here](https://discord.gg/CYVe2CyrXk)
  
#ライセンス

[MIT](https://github.com/simeononsecurity/glotta/blob/main/LICENSE)
