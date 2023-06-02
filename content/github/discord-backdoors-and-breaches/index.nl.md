---
title: "Discord Backdoors and Breaches Bot: Een Turn-Based Strategy Game Companion"
date: 2023-03-10
toc: true
draft: false
description: "Verbeter je ervaring met het spelen van Backdoors en Breaches met deze pre-alpha Discord bot, die commando's geeft om de gameplay en interactie te vergemakkelijken."
tags: ["Discord bot", "Backdoors en inbraken", "turn-based strategie spel", "spelpartner", "spelopdrachten", "strategiespel bot", "BHIS", "Black Hills InfoSec", "incident meester", "C2 team", "spelfasen", "spelopstelling", "spelinstructies", "spelkanaal", "Python bot", "Docker bot", "spelautomatisering", "spelsamenwerking", "spelcoördinatie", "cyberbeveiligingsspel", "informatiebeveiliging", "game-ontwikkeling", "gameplay tips", "multiplayer spel", "spelrollen", "speluitdagingen", "spelfasen", "opzet van de spelomgeving", "dockerized bot", "Python afhankelijkheden"]
---

## Discord Backdoors and Breaches Bot - Pre Alpha

[![Docker Image CI](https://github.com/simeononsecurity/discord-backdoors-and-breaches/actions/workflows/docker-image.yml/badge.svg)](https://github.com/simeononsecurity/discord-backdoors-and-breaches/actions/workflows/docker-image.yml)

<img src="https://github.com/simeononsecurity/discord-backdoors-and-breaches/blob/main/.github/images/bnb-dark.png?raw=true" alt="Backdoors and Breaches logo" width="200"/>


Een Discord bot voor Backdoors and Breaches, een turn-based strategie spel van [BHIS](https://www.blackhillsinfosec.com/projects/backdoorsandbreaches/)

### Beschikbare commando's

- `setup-game` Creëert een game id en stelt alle benodigde variabelen in.
- `start-game` Start een nieuw spel moet worden uitgevoerd mijn incident master alleen na `setup-game`
- `join-game` Laat spelers toe tot het spel door hen de rol "Speler" toe te kennen en hen toegang te verlenen tot het spelkanaal.
- `play-procedure` Start de procedurefase van het spel, waarin spelers een reeks uitdagingen moeten voltooien om verder te komen.
- `play-incident-master` Start de Incident Master-fase van het spel, waarin spelers om de beurt de Incident Master zijn en de andere spelers aansturen op een gesimuleerd incident.
- `play-c2` Start de Command and Control-fase van het spel, waarin de spelers om beurten het C2-team zijn en moeten coördineren met de andere spelers om een reeks taken te voltooien.
- `play-persistence` Start de Persistence-fase van het spel, waarin spelers een verborgen achterdeur in het systeem moeten vinden en uitschakelen.
- `play-pivot` Start de Pivot-fase van het spel, waarbij de spelers naar een ander deel van het systeem moeten pivotten en hun onderzoek moeten voortzetten.
- `end-game` Beëindigt het huidige spel en verwijdert het spelkanaal en de bijbehorende rollen.

Om een commando uit te voeren, typ je `!` of `/` gevolgd door de naam van het commando in het spelkanaal. Om bijvoorbeeld een nieuw spel te starten, typ je `!start-game` Sommige commando's zijn alleen beschikbaar tijdens bepaalde fasen van het spel.
### De Bot instellen

#### Python gebruiken

1. Kloon dit archief met `git clone https://github.com/simeononsecurity/discord-backdoors-and-breaches.git`
2. Installeer de vereiste afhankelijkheden met `pip install -r requirements.txt`
3. Maak een `config.ini` bestand in de hoofddirectory van het project met de volgende inhoud:
```ini
[SETTINGS]
discordtoken = put_discord_bot_token_here
channel_id = put_game_channel_id_here
```
4. Vervang `put_discord_bot_token_here` met je Discord bot token en `put_game_channel_id_here` met de ID van het kanaal waar u het spel wilt spelen.
5. Start de bot met `python main.py`

#### met behulp van Docker

1. Kloon de repository en navigeer naar de directory:
```
git clone https://github.com/simeononsecurity/discord-backdoors-and-breaches.git
cd discord-backdoors-and-breaches
```
2. Maak een `.env` bestand in de hoofdmap van het project en voeg de volgende omgevingsvariabelen toe met de bijbehorende waarden:
```env
BOT_TOKEN=<discord_bot_token_here>
CHANNEL_ID=<game_channel_id_here>
```
3. Bouw het Docker image met behulp van het meegeleverde Dockerfile:
```bash
docker build -t discord-backdoors-and-breaches .
```
4. Voer de Docker-container uit en geef de omgevingsvariabelen van de `.env` bestanden:
```bash
docker run --env-file .env discord-backdoors-and-breaches
```

Als alternatief kunt u de omgevingsvariabelen rechtstreeks instellen tijdens het `docker run` commando:
```bash
docker run -td --name bnbbot -e BOT_TOKEN=<discord_bot_token_here> -e CHANNEL_ID=<game_channel_id_here> discord-backdoors-and-breaches
```
of rechtstreeks van het beeld op [dockerhub](https://hub.docker.com/r/simeononsecurity/discord-backdoors-and-breaches)
```bash
docker run -td --name bnbbot -e BOT_TOKEN=<discord_bot_token_here> -e CHANNEL_ID=<game_channel_id_here> simeononsecurity/discord-backdoors-and-breaches:latest
```

