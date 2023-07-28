---
title: "Discord 后门和漏洞机器人：回合制策略游戏伴侣"
date: 2023-03-10
toc: true
draft: false
description: "这款 Discord 前期版本的机器人可为游戏和互动提供指令，从而增强您在《后门与入侵》中的游戏体验。"
tags: ["Discord 机器人", "后门和漏洞", "回合制策略游戏", "游戏伙伴", "游戏指令", "策略游戏机器人", "BHIS", "黑山信息安全", "事件主控", "C2 小组", "游戏阶段", "游戏设置", "游戏说明", "游戏频道", "Python 机器人", "Docker 机器人", "游戏自动化", "游戏合作", "游戏协调", "网络安全游戏", "信息安全", "游戏开发", "游戏技巧", "多人游戏", "游戏角色", "游戏挑战", "游戏阶段", "游戏环境设置", "对接机器人", "Python 依赖项"]
---

## Discord 后门和漏洞机器人 - 预阿尔法版

[![Docker Image CI](https://github.com/simeononsecurity/discord-backdoors-and-breaches/actions/workflows/docker-image.yml/badge.svg)](https://github.com/simeononsecurity/discord-backdoors-and-breaches/actions/workflows/docker-image.yml)

<img src="https://github.com/simeononsecurity/discord-backdoors-and-breaches/blob/main/.github/images/bnb-dark.png?raw=true" alt="Backdoors and Breaches 徽标" width="200"/>


为《Backdoors and Breaches》设计的 Discord 机器人，这是一款回合制策略游戏，由 [BHIS](https://www.blackhillsinfosec.com/projects/backdoorsandbreaches/)

### 可用命令

- `setup-game`创建游戏 ID 并设置所有需要的变量。
- `start-game`开始一个新游戏后，我的事件主控程序才会运行。 `setup-game`
- `join-game`通过为玩家分配 "玩家 "角色并授予其游戏频道访问权限，允许玩家加入游戏。
- `play-procedure`开始游戏的 "程序 "阶段，玩家必须完成一系列挑战才能取得进展。
- `play-incident-master`开始游戏的 "事件主控 "阶段，玩家轮流担任 "事件主控"，指导其他玩家如何应对模拟事件。
- `play-c2`开始游戏的指挥和控制阶段，玩家轮流担任 C2 小组，必须与其他玩家协调完成一系列任务。
- `play-persistence`开始游戏的 "坚持 "阶段，玩家必须找到并消除系统中隐藏的后门。
- `play-pivot`开始游戏的 "支点 "阶段，在这一阶段，玩家必须支点到系统的不同部分，继续进行调查。
- `end-game`结束当前游戏并删除游戏频道和相关角色。

要运行命令，请键入 `!`或 `/`后跟游戏频道中的命令名称。例如，要开始一个新游戏，键入 `!start-game`请注意，有些命令可能只在游戏的某些阶段可用。
### 设置机器人

#### 使用 Python

1.使用 `git clone https://github.com/simeononsecurity/discord-backdoors-and-breaches.git`
2.使用 `pip install -r requirements.txt`
3.创建一个 `config.ini`文件，内容如下：
```ini
[SETTINGS]
discordtoken = put_discord_bot_token_here
channel_id = put_game_channel_id_here
```
4.更换 `put_discord_bot_token_here`使用您的 Discord 机器人令牌和 `put_game_channel_id_here`输入您希望进行游戏的频道 ID。
5.使用 `python main.py`

#### 使用 Docker

1.克隆版本库并导航至目录：
```
git clone https://github.com/simeononsecurity/discord-backdoors-and-breaches.git
cd discord-backdoors-and-breaches
```
2.创建一个 `.env`文件，并添加以下环境变量及其相应值：
```env
BOT_TOKEN=<discord_bot_token_here>
CHANNEL_ID=<game_channel_id_here>
```
3.使用提供的 Dockerfile 构建 Docker 映像：
```bash
docker build -t discord-backdoors-and-breaches .
```
4.运行 Docker 容器，并将环境变量从 `.env`文件
```bash
docker run --env-file .env discord-backdoors-and-breaches
```

或者，您也可以在运行 `docker run`指挥：
```bash
docker run -td --name bnbbot -e BOT_TOKEN=<discord_bot_token_here> -e CHANNEL_ID=<game_channel_id_here> discord-backdoors-and-breaches
```
或直接从 [dockerhub](https://hub.docker.com/r/simeononsecurity/discord-backdoors-and-breaches)
```bash
docker run -td --name bnbbot -e BOT_TOKEN=<discord_bot_token_here> -e CHANNEL_ID=<game_channel_id_here> simeononsecurity/discord-backdoors-and-breaches:latest
```

