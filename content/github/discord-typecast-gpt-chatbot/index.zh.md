---
title: "Discord Typecast GPT 聊天机器人：友好且知识渊博的基于 Discord 的支持代理"
date: 2023-03-24
toc: true
draft: false
description: "使用一个友好、知识丰富的聊天机器人来增强您的 Discord 服务器，它能提供有用的回复、协助解决与服务器相关的问题并创建吸引人的互动。"
tags: ["Discord 聊天机器人", "支持代理", "服务器协助", "用户查询", "相关资源", "积极的环境", "意见", "偏好", "建议", "吸引人的互动", "友好机器人", "知识渊博的机器人", "基于 Discord 的机器人", "虚拟助理", "自动支持", "对话机器人", "信息反馈", "机智的机器人", "互动聊天机器人", "服务器管理", "用户支持", "人工智能机器人", "discord.io", "行动中的聊天机器人", "装卸工", "蟒蛇", "机器人部署", "虚拟环境", "机器人架构", "机器人控制器", "机器人服务"]
---

** discord-typecast-gpt-chatbot**

[![Docker Image CI](https://github.com/CyberSentinels/discord-typecast-gpt-chatbot/actions/workflows/docker-image.yml/badge.svg)](https://github.com/CyberSentinels/discord-typecast-gpt-chatbot/actions/workflows/docker-image.yml)

该机器人是基于 Discord 的支持代理。它为用户的询问提供有用的回复，协助解决与服务器相关的问题，并引导用户访问相关资源。该机器人友好、知识渊博，并能维持一个积极的环境。它还可以分享与各种主题相关的意见、偏好和建议，与用户进行引人入胜、内容丰富的互动。

[See the bot in action](https://discord.gg/CYVe2CyrXk)

### 如何运行机器人
### 使用 docker
```bash
docker run -td --name cyberchatbot -e DISCORD_BOT_APP_TOKEN="INSERT YOUR BOT TOKEN HERE" -e OPENAI_API_KEY="INSERT YOUR OPENAI API KEY HERE" simeononsecurity/discord-typecast-gpt-chatbot:latest
```
### 如何使用 python 手动运行机器人

要开始运行该版本库，您需要执行以下步骤：

1.克隆此版本库并更改为产品根目录

```bash
git clone URL
cd repo_name
```
2. 创建一个 `.env`文件（它将是 `.gitignored`并粘贴您的 discord 机器人令牌和 openai 令牌：

```env
DISCORD_BOT_APP_TOKEN=PASTE_DISCORD_TOKEN_HERE
OPENAI_API_KEY=PASTE_OPENAI_API_TOKEN_HERE
```

3.使用 `venv`
```bash
python3 -m venv venv
```

4.激活虚拟环境：
```bash
source venv/bin/activate
```

5.安装 `requirements.txt`
   
```bash
pip install -r requirements.txt
```

6.如果使用 `pip install`请务必用以下命令重新生成 requirements.txt：

```bash
pip freeze > requirements.txt
```
#### 如何修复本地化问题
```bash
sudo apt-get install locales -y
sudo locale-gen en_US.UTF-8 en_CA.UTF-8
sudo update-locale
```

## 建筑

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
