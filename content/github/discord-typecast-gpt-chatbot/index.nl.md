---
title: "Discord Typecast GPT Chatbot: Vriendelijke en deskundige discord-gebaseerde support agent"
date: 2023-03-24
toc: true
draft: false
description: "Verbeter je Discord-server met een vriendelijke en deskundige chatbot die nuttige antwoorden geeft, helpt bij server-gerelateerde vragen en zorgt voor boeiende interacties."
tags: ["Discord chatbot", "ondersteuningsagent", "serverondersteuning", "gebruikersvragen", "relevante bronnen", "positieve omgeving", "meningen", "voorkeuren", "aanbevelingen", "boeiende interacties", "vriendelijke bot", "goed geïnformeerde bot", "Op Discord gebaseerde bot", "virtuele assistent", "geautomatiseerde ondersteuning", "conversatiebot", "informatieve reacties", "vindingrijke bot", "interactieve chatbot", "serverbeheer", "gebruikersondersteuning", "AI-gestuurde bot", "discord.io", "chatbot in actie", "docker", "python", "bot inzet", "virtuele omgeving", "bot architectuur", "bot controllers", "bot diensten"]
---

**discord-typecast-gpt-chatbot**

[![Docker Image CI](https://github.com/CyberSentinels/discord-typecast-gpt-chatbot/actions/workflows/docker-image.yml/badge.svg)](https://github.com/CyberSentinels/discord-typecast-gpt-chatbot/actions/workflows/docker-image.yml)

Deze bot is een op Discord gebaseerde support agent. Hij geeft nuttige antwoorden op vragen van gebruikers, helpt met server-gerelateerde vragen en verwijst gebruikers naar relevante bronnen. De bot is vriendelijk, deskundig, en onderhoudt een positieve omgeving. Het kan ook meningen, voorkeuren en aanbevelingen delen met betrekking tot verschillende onderwerpen, waardoor boeiende en informatieve interacties met gebruikers ontstaan.

[See the bot in action](https://discord.io/cybersentinels)

## Hoe de bot te draaien
### Met behulp van docker
```bash
docker run -td --name cyberchatbot -e DISCORD_BOT_APP_TOKEN="INSERT YOUR BOT TOKEN HERE" -e OPENAI_API_KEY="INSERT YOUR OPENAI API KEY HERE" simeononsecurity/discord-typecast-gpt-chatbot:latest
```
### Hoe de bot handmatig draaien met python

Om te beginnen met het draaien van deze repository, moet u de volgende stappen uitvoeren:

1. Kloon deze repository en verander in product root

```bash
git clone URL
cd repo_name
```
2. een `.env` bestand in de project root (het zal `.gitignored` en plak je discord bot token en openai token:

```env
DISCORD_BOT_APP_TOKEN=PASTE_DISCORD_TOKEN_HERE
OPENAI_API_KEY=PASTE_OPENAI_API_TOKEN_HERE
```

3. Maak een nieuwe virtuele omgeving aan met `venv`
```bash
python3 -m venv venv
```

4. Activeer de virtuele omgeving:
```bash
source venv/bin/activate
```

5. Installeer de afhankelijkheden vermeld in `requirements.txt`
   
```bash
pip install -r requirements.txt
```

6. Als u nieuwe afhankelijkheden installeert met `pip install` zorg ervoor dat je requirements.txt regenereert met:

```bash
pip freeze > requirements.txt
```
#### Hoe locales op te lossen
```bash
sudo apt-get install locales -y
sudo locale-gen en_US.UTF-8 en_CA.UTF-8
sudo update-locale
```

## Architectuur

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
