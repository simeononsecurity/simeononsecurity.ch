---
title: "Чатбот Discord Typecast GPT: Дружелюбный и знающий агент поддержки на базе Discord"
date: 2023-03-24
toc: true
draft: false
description: "Усовершенствуйте свой сервер Discord с помощью дружелюбного и компетентного чат-бота, который будет давать полезные ответы, помогать в решении вопросов, связанных с сервером, и создавать увлекательные взаимодействия."
tags: ["Чатбот Discord", "агент поддержки", "поддержка сервера", "запросы пользователей", "соответствующие ресурсы", "позитивная среда", "мнения", "предпочтения", "рекомендации", "вовлекающее взаимодействие", "дружественный бот", "знающий бот", "Бот на основе Discord", "виртуальный ассистент", "автоматизированная поддержка", "разговорный бот", "информационные ответы", "находчивый бот", "интерактивный чатбот", "управление сервером", "поддержка пользователей", "Бот с искусственным интеллектом", "discord.io", "чатбот в действии", "docker", "python", "развертывание ботов", "виртуальная среда", "архитектура ботов", "контроллеры ботов", "бот-сервисы"]
---

**дискорд-типекаст-гпт-чатбот**

[![Docker Image CI](https://github.com/CyberSentinels/discord-typecast-gpt-chatbot/actions/workflows/docker-image.yml/badge.svg)](https://github.com/CyberSentinels/discord-typecast-gpt-chatbot/actions/workflows/docker-image.yml)

Этот бот представляет собой агент поддержки на базе Discord. Он дает полезные ответы на запросы пользователей, помогает в решении вопросов, связанных с сервером, и направляет пользователей на соответствующие ресурсы. Бот дружелюбен, хорошо осведомлен и поддерживает позитивную атмосферу. Он также может делиться мнениями, предпочтениями и рекомендациями по различным темам, создавая увлекательное и информативное взаимодействие с пользователями.

[See the bot in action](https://discord.io/cybersentinels)

## Как запустить бота
### Использование docker
```bash
docker run -td --name cyberchatbot -e DISCORD_BOT_APP_TOKEN="INSERT YOUR BOT TOKEN HERE" -e OPENAI_API_KEY="INSERT YOUR OPENAI API KEY HERE" simeononsecurity/discord-typecast-gpt-chatbot:latest
```
### Как запустить бота вручную с помощью python

Чтобы начать работу с этим репозиторием, необходимо выполнить следующие действия:

1. Клонируйте этот репозиторий и перейдите в корень продукта

```bash
git clone URL
cd repo_name
```
2. создать `.env` файл в корне проекта (это будет `.gitignored` и вставьте свой токен бота discord и токен openai:

```env
DISCORD_BOT_APP_TOKEN=PASTE_DISCORD_TOKEN_HERE
OPENAI_API_KEY=PASTE_OPENAI_API_TOKEN_HERE
```

3. Создайте новую виртуальную среду с помощью `venv`
```bash
python3 -m venv venv
```

4. Активируйте виртуальную среду:
```bash
source venv/bin/activate
```

5. Установите зависимости, перечисленные в `requirements.txt`
   
```bash
pip install -r requirements.txt
```

6. При установке новых зависимостей с помощью `pip install` обязательно перегенерируйте файл requirements.txt с:

```bash
pip freeze > requirements.txt
```
#### Как исправить проблему с локалями
```bash
sudo apt-get install locales -y
sudo locale-gen en_US.UTF-8 en_CA.UTF-8
sudo update-locale
```

## Архитектура

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
