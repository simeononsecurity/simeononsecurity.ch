---
title: "Discord Typecast GPT Chatbot: Przyjazny i kompetentny agent wsparcia oparty na Discordzie"
date: 2023-03-24
toc: true
draft: false
description: "Wzbogać swój serwer Discord o przyjaznego i kompetentnego chatbota, który udziela pomocnych odpowiedzi, pomaga w pytaniach związanych z serwerem i tworzy angażujące interakcje."
tags: ["Chatbot Discord", "agent wsparcia", "pomoc serwera", "zapytania użytkowników", "odpowiednie zasoby", "pozytywne środowisko", "opinie", "preferencje", "zalecenia", "Angażujące interakcje", "przyjazny bot", "kompetentny bot", "Bot oparty na Discordzie", "wirtualny asystent", "zautomatyzowane wsparcie", "bot konwersacyjny", "odpowiedzi informacyjne", "zaradny bot", "interaktywny chatbot", "zarządzanie serwerem", "wsparcie użytkownika", "Bot oparty na sztucznej inteligencji", "discord.io", "chatbot w akcji", "doker", "pyton", "wdrożenie bota", "środowisko wirtualne", "architektura bota", "kontrolery botów", "usługi botów"]
---

**discord-typecast-gpt-chatbot**

[![Docker Image CI](https://github.com/CyberSentinels/discord-typecast-gpt-chatbot/actions/workflows/docker-image.yml/badge.svg)](https://github.com/CyberSentinels/discord-typecast-gpt-chatbot/actions/workflows/docker-image.yml)

Ten bot jest agentem wsparcia opartym na Discordzie. Zapewnia pomocne odpowiedzi na pytania użytkowników, pomaga w kwestiach związanych z serwerem i kieruje użytkowników do odpowiednich zasobów. Bot jest przyjazny, kompetentny i utrzymuje pozytywne środowisko. Może również dzielić się opiniami, preferencjami i zaleceniami związanymi z różnymi tematami, tworząc angażujące i pouczające interakcje z użytkownikami.

[See the bot in action](https://discord.gg/CYVe2CyrXk)

## Jak uruchomić bota
### Korzystanie z dockera
```bash
docker run -td --name cyberchatbot -e DISCORD_BOT_APP_TOKEN="INSERT YOUR BOT TOKEN HERE" -e OPENAI_API_KEY="INSERT YOUR OPENAI API KEY HERE" simeononsecurity/discord-typecast-gpt-chatbot:latest
```
### Jak uruchomić bota ręcznie za pomocą Pythona

Aby rozpocząć uruchamianie tego repozytorium, należy wykonać następujące kroki:

1. Sklonuj to repozytorium i przejdź do katalogu głównego produktu

```bash
git clone URL
cd repo_name
```
2. utworzyć `.env` w katalogu głównym projektu (będzie to `.gitignored` i wklej swój token bota discord i token openai:

```env
DISCORD_BOT_APP_TOKEN=PASTE_DISCORD_TOKEN_HERE
OPENAI_API_KEY=PASTE_OPENAI_API_TOKEN_HERE
```

3. Utwórz nowe środowisko wirtualne przy użyciu `venv`
```bash
python3 -m venv venv
```

4. Aktywuj środowisko wirtualne:
```bash
source venv/bin/activate
```

5. Zainstaluj zależności wymienione w sekcji `requirements.txt`
   
```bash
pip install -r requirements.txt
```

6. Jeśli zainstalujesz nowe zależności za pomocą `pip install` upewnij się, że zregenerowałeś plik requirements.txt z:

```bash
pip freeze > requirements.txt
```
#### Jak naprawić problem z ustawieniami lokalnymi
```bash
sudo apt-get install locales -y
sudo locale-gen en_US.UTF-8 en_CA.UTF-8
sudo update-locale
```

## Architektura

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
