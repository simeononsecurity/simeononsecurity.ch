---
title: "Discord Typecast GPT Chatbot: Agent de asistență prietenos și bine informat bazat pe Discord"
date: 2023-03-24
toc: true
draft: false
description: "Îmbunătățiți-vă serverul Discord cu un chatbot prietenos și bine informat care oferă răspunsuri utile, vă ajută cu întrebări legate de server și creează interacțiuni captivante."
tags: ["Discord chatbot", "agent de suport", "asistență server", "interogări ale utilizatorului", "resurse relevante", "mediu pozitiv", "opinii", "preferințe", "recomandări", "interacțiuni captivante", "bot prietenos", "bot cunoscător", "Bot bazat pe Discord", "asistent virtual", "suport automatizat", "conversație bot", "răspunsuri informaționale", "bot ingenios", "chatbot interactiv", "gestionarea serverului", "asistență pentru utilizatori", "Robot cu AI", "discord.io", "chatbot în acțiune", "docker", "python", "implementarea botului", "mediu virtual", "arhitectura bot", "controlere bot", "servicii bot"]
---

**discord-typecast-gpt-chatbot**

[![Docker Image CI](https://github.com/CyberSentinels/discord-typecast-gpt-chatbot/actions/workflows/docker-image.yml/badge.svg)](https://github.com/CyberSentinels/discord-typecast-gpt-chatbot/actions/workflows/docker-image.yml)

Acest robot este un agent de asistență bazat pe Discord. Acesta oferă răspunsuri utile la întrebările utilizatorilor, ajută la rezolvarea întrebărilor legate de server și îndrumă utilizatorii către resurse relevante. Robotul este prietenos, bine informat și menține un mediu pozitiv. De asemenea, poate împărtăși opinii, preferințe și recomandări legate de diverse subiecte, creând interacțiuni atractive și informative cu utilizatorii.

[See the bot in action](https://discord.io/cybersentinels)

## Cum se execută robotul
### Folosind docker
```bash
docker run -td --name cyberchatbot -e DISCORD_BOT_APP_TOKEN="INSERT YOUR BOT TOKEN HERE" -e OPENAI_API_KEY="INSERT YOUR OPENAI API KEY HERE" simeononsecurity/discord-typecast-gpt-chatbot:latest
```
### Cum să rulați manual robotul folosind python

Pentru a începe să rulați acest depozit, trebuie să efectuați următorii pași:

1. Clonați acest depozit și schimbați în rădăcina produsului

```bash
git clone URL
cd repo_name
```
2. creați un `.env` din rădăcina proiectului (va fi `.gitignored` și lipiți token-ul robotului discord și token-ul openai:

```env
DISCORD_BOT_APP_TOKEN=PASTE_DISCORD_TOKEN_HERE
OPENAI_API_KEY=PASTE_OPENAI_API_TOKEN_HERE
```

3. Creați un nou mediu virtual utilizând `venv`
```bash
python3 -m venv venv
```

4. Activați mediul virtual:
```bash
source venv/bin/activate
```

5. Instalați dependențele enumerate în `requirements.txt`
   
```bash
pip install -r requirements.txt
```

6. Dacă instalați noi dependențe cu `pip install` asigurați-vă că ați regenerat requirements.txt cu:

```bash
pip freeze > requirements.txt
```
#### Cum se remediază problema locale
```bash
sudo apt-get install locales -y
sudo locale-gen en_US.UTF-8 en_CA.UTF-8
sudo update-locale
```

## Arhitectura

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
