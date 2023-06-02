---
title: "Discord Typecast GPT Chatbot: Friendly and Knowledgeable Discord-Based Support Agent"
date: 2023-03-24
toc: true
draft: false
description: "Enhance your Discord server with a friendly and knowledgeable chatbot that provides helpful responses, assists with server-related questions, and creates engaging interactions."
tags: ["Discord chatbot", "support agent", "server assistance", "user queries", "relevant resources", "positive environment", "opinions", "preferences", "recommendations", "engaging interactions", "friendly bot", "knowledgeable bot", "Discord-based bot", "virtual assistant", "automated support", "conversation bot", "informational responses", "resourceful bot", "interactive chatbot", "server management", "user support", "AI-powered bot", "discord.io", "chatbot in action", "docker", "python", "bot deployment", "virtual environment", "bot architecture", "bot controllers", "bot services"]
---

**discord-typecast-gpt-chatbot**

[![Docker Image CI](https://github.com/CyberSentinels/discord-typecast-gpt-chatbot/actions/workflows/docker-image.yml/badge.svg)](https://github.com/CyberSentinels/discord-typecast-gpt-chatbot/actions/workflows/docker-image.yml)

This bot is a Discord-based support agent. It provides helpful responses to user queries, assists with server-related questions, and directs users to relevant resources. The bot is friendly, knowledgeable, and maintains a positive environment. It can also share opinions, preferences, and recommendations related to various topics, creating engaging and informative interactions with users.

[See the bot in action](https://discord.io/cybersentinels)

## How to run the bot
### Using docker
```bash
docker run -td --name cyberchatbot -e DISCORD_BOT_APP_TOKEN="INSERT YOUR BOT TOKEN HERE" -e OPENAI_API_KEY="INSERT YOUR OPENAI API KEY HERE" simeononsecurity/discord-typecast-gpt-chatbot:latest
```
### How to run the bot manually using python

To get started with running this repository, you need to perform the following steps:

1. Clone this repository and change into product root

```bash
git clone URL
cd repo_name
```
2. create an `.env` file in the project root (it will be `.gitignored`) and paste your discord bot token and openai token:

```env
DISCORD_BOT_APP_TOKEN=PASTE_DISCORD_TOKEN_HERE
OPENAI_API_KEY=PASTE_OPENAI_API_TOKEN_HERE
```

3. Create a new virtual environment using `venv`:
```bash
python3 -m venv venv
```

4. Activate the virtual environment:
```bash
source venv/bin/activate
```

5. Install the dependencies listed in `requirements.txt`:
   
```bash
pip install -r requirements.txt
```

6. If you install new dependencies with `pip install`, be sure to regenerate requirements.txt with:

```bash
pip freeze > requirements.txt
```
#### How to fix locales issue
```bash
sudo apt-get install locales -y
sudo locale-gen en_US.UTF-8 en_CA.UTF-8
sudo update-locale
```

## Architecture

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
