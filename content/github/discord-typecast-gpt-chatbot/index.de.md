---
title: "Discord Typecast GPT Chatbot: Freundlicher und sachkundiger Discord-basierter Support-Agent"
date: 2023-03-24
toc: true
draft: false
description: "Verbessern Sie Ihren Discord-Server mit einem freundlichen und sachkundigen Chatbot, der hilfreiche Antworten gibt, bei serverbezogenen Fragen hilft und ansprechende Interaktionen schafft."
tags: ["Discord-Chatbot", "Support-Mitarbeiter", "Serverbetreuung", "user queries", "relevante Ressourcen", "positives Umfeld", "Meinungen", "Einstellungen", "Empfehlungen", "verbindliche Interaktionen", "freundlicher Bot", "erfahrener Bot", "Discord-basierter Bot", "virtueller Assistent", "automatisierte Unterstützung", "Konversationsbot", "informatorische Antworten", "findiger Bot", "interaktiver Chatbot", "Serververwaltung", "Benutzerunterstützung", "KI-gestützter Bot", "discord.io", "Chatbot in Aktion", "Docker", "python", "Bot-Einsatz", "virtuelle Umgebung", "Bot-Architektur", "Bot-Controller", "Bot-Dienste"]
---

**discord-typecast-gpt-chatbot**

[![Docker Image CI](https://github.com/CyberSentinels/discord-typecast-gpt-chatbot/actions/workflows/docker-image.yml/badge.svg)](https://github.com/CyberSentinels/discord-typecast-gpt-chatbot/actions/workflows/docker-image.yml)

Dieser Bot ist ein Discord-basierter Support-Agent. Er gibt hilfreiche Antworten auf Benutzeranfragen, hilft bei Fragen zum Server und verweist die Benutzer auf relevante Ressourcen. Der Bot ist freundlich, kenntnisreich und sorgt für ein positives Umfeld. Er kann auch Meinungen, Vorlieben und Empfehlungen zu verschiedenen Themen weitergeben und so für eine ansprechende und informative Interaktion mit den Benutzern sorgen.

[See the bot in action](https://discord.gg/CYVe2CyrXk)

## Wie man den Bot ausführt
### Docker verwenden
```bash
docker run -td --name cyberchatbot -e DISCORD_BOT_APP_TOKEN="INSERT YOUR BOT TOKEN HERE" -e OPENAI_API_KEY="INSERT YOUR OPENAI API KEY HERE" simeononsecurity/discord-typecast-gpt-chatbot:latest
```
### Wie man den Bot manuell mit Python startet

Um mit der Ausführung dieses Repositorys zu beginnen, müssen Sie die folgenden Schritte durchführen:

1. Klonen Sie dieses Repository und wechseln Sie in das Produkt-Root

```bash
git clone URL
cd repo_name
```
2. Erstellen einer `.env` Datei im Stammverzeichnis des Projekts (sie lautet `.gitignored` und fügen Sie Ihren Discord-Bot-Token und Ihren Openai-Token ein:

```env
DISCORD_BOT_APP_TOKEN=PASTE_DISCORD_TOKEN_HERE
OPENAI_API_KEY=PASTE_OPENAI_API_TOKEN_HERE
```

3. Erstellen Sie eine neue virtuelle Umgebung mit `venv`
```bash
python3 -m venv venv
```

4. Aktivieren Sie die virtuelle Umgebung:
```bash
source venv/bin/activate
```

5. Installieren Sie die Abhängigkeiten, die in `requirements.txt`
   
```bash
pip install -r requirements.txt
```

6. Wenn Sie neue Abhängigkeiten mit `pip install` stellen Sie sicher, dass Sie die Datei requirements.txt mit neu generieren:

```bash
pip freeze > requirements.txt
```
#### Wie behebt man das Problem mit den Gebietsschemata?
```bash
sudo apt-get install locales -y
sudo locale-gen en_US.UTF-8 en_CA.UTF-8
sudo update-locale
```

## Architektur

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
