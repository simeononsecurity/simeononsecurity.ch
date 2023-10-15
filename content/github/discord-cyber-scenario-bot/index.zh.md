---
title: "Discord 网络情景机器人：增强网络安全培训和意识"
date: 2023-02-22
toc: true
draft: false
description: "了解 CyberScenarioBot 如何在 Discord 上提升网络安全培训和意识计划，提供测验、情景模拟、排行榜跟踪和强大的工具命令。"
tags: ["Discord 机器人", "网络安全培训", "网络安全意识", "情景机器人", "测验机器人", "排行榜", "工具命令", "Docker", "Python", "自动测试", "Discord API", "开发人员文档", "贡献", "MIT 许可", "网络情景机器人", "网络哨兵", "加强培训", "宣传计划", "网络安全情景", "服务器环境", "自定义命令", "部署和管理", "测验和情景模拟", "工具命令", "信息命令", "问题和贡献", "Discord 开发人员应用程序", "Discord.py 文档", "与开发人员合作", "社区 Discord 服务器"]
---


**网络情景机器人**

Discord 网络情景、测验和网络意识培训机器人。

您可以跳转到 [🚀 Quick Start](#quick-start)添加 `CyberScenarioBot`到您的服务器。

[![Docker Image CI](https://github.com/simeononsecurity/discord-cyber-scenario-bot/actions/workflows/docker-image.yml/badge.svg)](https://github.com/simeononsecurity/discord-cyber-scenario-bot/actions/workflows/docker-image.yml)

## 简介

该机器人可用于网络安全培训或提高认识计划，让用户接触各种网络安全情景，并学习如何预防或应对这些情景。通过使用 Discord 机器人，可以轻松地在服务器环境中与用户共享场景，还可以根据需要定制机器人，使其包含更多命令或功能。此外，机器人可以在 Docker 容器中运行，从而便于在各种环境中进行部署和管理。

[See the bot in action](https://discord.gg/CYVe2CyrXk)

## 🚀 快速入门

### 如何运行：
#### Python：
假设您使用的是 Unix 系统，请打开终端并导航到 bot.py 脚本所在的目录。然后，运行以下命令：
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
请注意，如果使用的是 Windows 系统，则需要使用稍有不同的命令来设置环境变量。下面是一个可以在 Windows 系统上运行的命令示例：
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
#### Docker：
运行 Docker 容器时，可以使用 -e 标志传递 BOT_TOKEN 环境变量，如下所示：

```bash
docker run -e BOT_TOKEN="INSERT YOUR BOT TOKEN HERE" -it --rm simeononsecurity/discord-cyber-scenario-bot:latest
```

在后台运行机器人：
```bash
docker run -td --name scenario-bot -e BOT_TOKEN="INSERT YOUR BOT TOKEN HERE" simeononsecurity/discord-cyber-scenario-bot:latest
```

在后台运行机器人，包含所有预定的提示和角色：
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

### 功能
### **可用命令**
*命令前缀：'！'、'/'*****

### 📝 **测验和情景命令**
- Aplus**：回复 CompTIA 的 A+ 相关提示。
- **Bluescenario**：回复蓝队情景。
- **CCNA**：使用 Cisco 的 CCNA 多选提示进行回复。
- **CEH**：使用 EC-Council 的 CEH 多选提示进行回复。
- **CISSP**：根据 ISC2 的 CISSP 多选提示回复。
- **Linuxplus**：根据 CompTIA 的 Linux+ 多选提示进行回复。
- **Netplus**：使用 CompTIA 的 Network+ 相关提示进行回复。
- **Quiz**：使用随机网络安全意识问题进行回复。
- **Redscenario**：回复一个红色团队场景。
- **Secplus**：回复 CompTIA 的 Security+ 相关提示。

#### 💯🎯 **Leaderboard**。
*多选题的动态权重与真实考试类似，取决于回答正确或错误*。

- 随着时间的推移跟踪您的进度，并查看您与服务器中其他人的比较情况* *查看每个测验类别的分数
- 查看每个测验类别的分数和总分

### 🛠️ **工具命令**
- Dns**：输入 `domain name`并返回 A、AAAA、NS、TXT 等记录。
- **哈希**：接收 `1 of 4 supported algos`和一个 `string`并输出相应的哈希值。
- **Ping**：接收一个 `IP address`并返回成功信息和平均延迟或失败信息。
- **Phonelookup**：接收一个 `phone number`并输出载体和位置。
- **Shodanip**：接收一个 `IP address`并从 https://internetdb.shodan.io/ 输出有用信息。
- 子网**：接收一个 `IP address`和一个 `Subnet Mask`并输出范围、可用 IP、网关地址、广播地址和支持的主机数量。
- **Whois**：接收一个 `domain name`并输出域名 WHOIS 信息。

### ℹ️ **信息命令**
- 命令**：回复此信息。
- **社交**：回复各种机器人社交媒体账户和网站。

### ⚙️ **轻松设置**
- 参见 [🚀 Quick Start](#🚀-quick-start)

## 即将推出的功能

这些功能已计划实施日期，但我们正在跟踪它们，我们希望 [contributions](#contributing)为他们。

- 先进的排行榜功能，包括每周和每月排名。
- 可定制的提示和测验，以满足特定的网络安全培训需求。
- 先进的报告和分析功能，用于跟踪用户的进度和表现。

## 使用方法

CyberScenarioBot 提供各种命令和功能，可增强网络安全培训和意识计划。以下是一些常见的使用案例：

1.**测验和情景**：使用 `/quiz`命令随机获取网络安全意识问题。使用以下命令 `/aplus` `/netplus` `/secplus`访问与 CompTIA 认证相关的特定提示。使用以下命令 `/bluescenario`和 `/redscenario`分别获得蓝队和红队的情景。

2.**排行榜**：通过回答测验和认证问题，跟踪用户进度并与服务器中的其他人比较分数。

3.**工具命令**：使用各种工具命令来执行与 DNS、哈希、ping、电话号码查询、Shodan IP 搜索、子网计算和域名 WHOIS 查询有关的任务。使用以下命令 `/dns` `/hash` `/ping` `/phonelookup` `/shodanip` `/subnet`和 `/whois`后跟适当的参数。

4.**信息命令**：使用 `/commands`命令获取可用命令列表。使用 `/socials`命令来获取机器人的社交媒体账户和网站信息。

请随意探索和尝试可用命令，以加强网络安全培训并吸引服务器成员参与。

## 问题

如果用户遇到任何问题或有改进建议，他们可以打开 GitHub 问题进行报告。鼓励用户提供有关问题的详细信息和重现问题的步骤。

要打开一个问题，请按照以下步骤操作：

1.转到项目 GitHub 仓库的 "问题 "选项卡： [Issues](https://github.com/CyberSentinels/discord-cyber-scenario-bot/issues)
2.点击 "新问题 "按钮。
3.提供描述性标题和清晰的问题描述。
4.包含任何相关日志、截图或代码片段，以帮助排除故障。
5.提交问题并等待项目维护者的进一步沟通。

## 投稿

我们欢迎所有贡献。
本项目旨在通过以下方式进行开发和学习 [the CyberSentinels club](https://cybersentinels.org)我们很乐意为您提供帮助并回答您的任何问题。

### Python 自动测试

此软件仓库包含自动化测试，您可以查看如何实现自动化测试的示例 [here](https://github.com/CyberSentinels/penguin-pie)

#### Discord API 和开发人员文档

要测试更改和实施功能，您需要一些东西。

- [Discord Developer Application](https://discord.com/developers/applications)
- [Discord Developers Documentation](https://discord.com/developers/docs/intro)
- [Discord.py Documentation](https://discordpy.readthedocs.io/en/stable/)

### 与开发人员合作

您可以在社区 discord 服务器中讨论开发工作 [here](https://discord.gg/CYVe2CyrXk)
  
## 许可证

[MIT](https://github.com/simeononsecurity/glotta/blob/main/LICENSE)
