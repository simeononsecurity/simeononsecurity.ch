---
title: "Discord Typecast GPT Chatbot: Agente di supporto amichevole e competente basato su Discord"
date: 2023-03-24
toc: true
draft: false
description: "Migliorate il vostro server Discord con un chatbot amichevole e competente che fornisce risposte utili, assiste nelle domande relative al server e crea interazioni coinvolgenti."
tags: ["Chatbot Discord", "agente di supporto", "assistenza al server", "query dell'utente", "risorse rilevanti", "ambiente positivo", "opinioni", "preferenze", "raccomandazioni", "interazioni coinvolgenti", "bot amichevole", "bot esperto", "Bot basato su Discord", "assistente virtuale", "supporto automatico", "bot di conversazione", "risposte informative", "bot pieno di risorse", "chatbot interattivo", "gestione del server", "supporto agli utenti", "Bot con intelligenza artificiale", "discord.io", "chatbot in azione", "docker", "pitone", "distribuzione dei bot", "ambiente virtuale", "architettura bot", "controllori bot", "servizi bot"]
---

**discorso-typecast-gpt-chatbot**

[![Docker Image CI](https://github.com/CyberSentinels/discord-typecast-gpt-chatbot/actions/workflows/docker-image.yml/badge.svg)](https://github.com/CyberSentinels/discord-typecast-gpt-chatbot/actions/workflows/docker-image.yml)

Questo bot è un agente di supporto basato su Discord. Fornisce risposte utili alle domande degli utenti, assiste nelle questioni relative al server e indirizza gli utenti verso le risorse più importanti. Il bot è amichevole, competente e mantiene un ambiente positivo. Può anche condividere opinioni, preferenze e raccomandazioni relative a vari argomenti, creando interazioni coinvolgenti e informative con gli utenti.

[See the bot in action](https://discord.gg/CYVe2CyrXk)

## Come eseguire il bot
### Usando docker
```bash
docker run -td --name cyberchatbot -e DISCORD_BOT_APP_TOKEN="INSERT YOUR BOT TOKEN HERE" -e OPENAI_API_KEY="INSERT YOUR OPENAI API KEY HERE" simeononsecurity/discord-typecast-gpt-chatbot:latest
```
### Come eseguire il bot manualmente usando python

Per iniziare a eseguire questo repository, è necessario eseguire i seguenti passaggi:

1. Clonare questo repository e passare alla root del prodotto

```bash
git clone URL
cd repo_name
```
2. creare un `.env` nella radice del progetto (sarà `.gitignored` e incollare il token del bot discord e il token openai:

```env
DISCORD_BOT_APP_TOKEN=PASTE_DISCORD_TOKEN_HERE
OPENAI_API_KEY=PASTE_OPENAI_API_TOKEN_HERE
```

3. Creare un nuovo ambiente virtuale utilizzando `venv`
```bash
python3 -m venv venv
```

4. Attivare l'ambiente virtuale:
```bash
source venv/bin/activate
```

5. Installare le dipendenze elencate in `requirements.txt`
   
```bash
pip install -r requirements.txt
```

6. Se si installano nuove dipendenze con `pip install` assicurarsi di rigenerare requirements.txt con:

```bash
pip freeze > requirements.txt
```
#### Come risolvere il problema dei locales
```bash
sudo apt-get install locales -y
sudo locale-gen en_US.UTF-8 en_CA.UTF-8
sudo update-locale
```

## Architettura

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
