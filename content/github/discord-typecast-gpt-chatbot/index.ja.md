---
title: "Discord Typecast GPT Chatbot：親切で知識のあるDiscordベースのサポート・エージェント"
date: 2023-03-24
toc: true
draft: false
description: "親切な応答、サーバーに関する質問のサポート、魅力的なインタラクションを生み出す、フレンドリーで知識豊富なチャットボットで、Discordサーバーを強化しましょう。"
tags: ["Discordチャットボット", "サポートエージェント", "サーバ支援", "ユーザークエリ", "関連資料", "プラスアルファの環境", "しょし", "好き嫌い", "おすすめ", "交流会", "フレンドリーボット", "知恵袋", "Discordベースのボット", "バーチャルアシスタント", "自動化対応", "カンバセーションボット", "インフォメーションレスポンス", "知恵袋", "対話型チャットボット", "サーバー管理", "ユーザーサポート", "AI搭載ボット", "discord.io", "チャットボットの動作", "ドッカー", "パイソン", "ボットデプロイメント", "仮想環境", "ボットアーキテクチャ", "ボットコントローラー", "ボットサービス"]
---

**ディスクコード・タイペキャスト・GPT・チャットボット＊＊。

[![Docker Image CI](https://github.com/CyberSentinels/discord-typecast-gpt-chatbot/actions/workflows/docker-image.yml/badge.svg)](https://github.com/CyberSentinels/discord-typecast-gpt-chatbot/actions/workflows/docker-image.yml)

このボットは、Discordベースのサポートエージェントです。ユーザーの問い合わせに親切な回答を提供し、サーバー関連の質問をサポートし、関連するリソースにユーザーを誘導します。このボットは、フレンドリーで知識が豊富で、ポジティブな環境を維持することができます。また、さまざまなトピックに関する意見、好み、推奨事項を共有し、ユーザーとの魅力的で有益な対話を実現します。

[See the bot in action](https://discord.gg/CYVe2CyrXk)

## ボットの実行方法
### dockerを使う
```bash
docker run -td --name cyberchatbot -e DISCORD_BOT_APP_TOKEN="INSERT YOUR BOT TOKEN HERE" -e OPENAI_API_KEY="INSERT YOUR OPENAI API KEY HERE" simeononsecurity/discord-typecast-gpt-chatbot:latest
```
### Python を使って手動でボットを動かす方法

このリポジトリの実行を開始するには、次の手順を実行する必要があります：

1.このリポジトリをクローンし、product rootに変更する

```bash
git clone URL
cd repo_name
```
2.作成する `.env`ファイルをプロジェクトルートに作成します（このファイルは `.gitignored`をクリックし、discord botトークンとopenaiトークンを貼り付けてください：

```env
DISCORD_BOT_APP_TOKEN=PASTE_DISCORD_TOKEN_HERE
OPENAI_API_KEY=PASTE_OPENAI_API_TOKEN_HERE
```

3.を使用して新しい仮想環境を作成します。 `venv`
```bash
python3 -m venv venv
```

4.仮想環境をアクティベートする：
```bash
source venv/bin/activate
```

5.に記載されている依存関係をインストールします。 `requirements.txt`
   
```bash
pip install -r requirements.txt
```

6.で新しい依存関係をインストールした場合 `pip install`でrequirements.txtを必ず再生成してください：

```bash
pip freeze > requirements.txt
```
#### ロケールの問題を解決する方法
```bash
sudo apt-get install locales -y
sudo locale-gen en_US.UTF-8 en_CA.UTF-8
sudo update-locale
```

## アーキテクチャ

```text
./
project root

bot/
discord bot's source

bot/main.py:
This is the main entry point for your application

bot/controllers/
This directory contains code that controls the main program and provides inputs into services

bot/services/
This directory contains code that do small, specific tasks

requirements.txt:
This file lists the dependencies required for your application to run
```
