---
title: "Discord Backdoors and Breaches Bot: Ein Begleiter für das rundenbasierte Strategiespiel"
date: 2023-03-10
toc: true
draft: false
description: "Verbessert euer Spielerlebnis in Backdoors and Breaches mit diesem Pre-Alpha-Discord-Bot, der Befehle zur Erleichterung des Gameplays und der Interaktion bereitstellt."
tags: ["Diskord-Bot", "Hintertüren und Sicherheitslücken", "rundenbasiertes Strategiespiel", "Spielbegleiter", "Gameplay-Befehle", "Strategie-Spiel-Bot", "BHIS", "Black Hills InfoSec", "Incident Master", "C2-Team", "Spielphasen", "Spielablauf", "Spielanleitung", "Spielkanal", "Python-Bot", "Docker-Bot", "Spiele-Automatisierung", "Spiel-Kollaboration", "Spielkoordination", "Cybersicherheitsspiel", "Informationssicherheit", "Spieleentwicklung", "Spieltipps", "Multiplayer-Spiel", "Spielrollen", "Spiel-Herausforderungen", "Spielphasen", "Einrichtung der Spielumgebung", "dockerisierter Bot", "Python-Abhängigkeiten"]
---

## Discord Backdoors and Breaches Bot - Pre Alpha

[![Docker Image CI](https://github.com/simeononsecurity/discord-backdoors-and-breaches/actions/workflows/docker-image.yml/badge.svg)](https://github.com/simeononsecurity/discord-backdoors-and-breaches/actions/workflows/docker-image.yml)

<img src="https://github.com/simeononsecurity/discord-backdoors-and-breaches/blob/main/.github/images/bnb-dark.png?raw=true" alt="Backdoors and Breaches logo" width="200"/>


Ein Discord-Bot für Backdoors and Breaches, ein rundenbasiertes Strategiespiel von [BHIS](https://www.blackhillsinfosec.com/projects/backdoorsandbreaches/)

### Verfügbare Befehle

- `setup-game` Erzeugt eine Spiel-ID und setzt alle benötigten Variablen.
- `start-game` Startet ein neues Spiel sollte mein Incident Master erst nach `setup-game`
- `join-game` Ermöglicht es Spielern, dem Spiel beizutreten, indem ihnen die Rolle "Spieler" zugewiesen wird und sie Zugriff auf den Spielkanal erhalten.
- `play-procedure` Startet die Verfahrensphase des Spiels, in der die Spieler eine Reihe von Herausforderungen bewältigen müssen, um weiterzukommen.
- `play-incident-master` Startet die "Incident Master"-Phase des Spiels, in der die Spieler abwechselnd der "Incident Master" sind und den anderen Spielern Anweisungen geben, wie sie auf einen simulierten Vorfall reagieren sollen.
- `play-c2` Startet die Kommando- und Kontrollphase des Spiels, in der die Spieler abwechselnd das C2-Team sind und sich mit den anderen Spielern abstimmen müssen, um eine Reihe von Aufgaben zu erfüllen.
- `play-persistence` Startet die Persistenzphase des Spiels, in der die Spieler eine versteckte Hintertür im System finden und beseitigen müssen.
- `play-pivot` Startet die Pivot-Phase des Spiels, in der die Spieler zu einem anderen Teil des Systems schwenken und ihre Untersuchungen fortsetzen müssen.
- `end-game` Beendet das aktuelle Spiel und löscht den Spielkanal und die zugehörigen Rollen.

Um einen Befehl auszuführen, geben Sie `!` oder `/` gefolgt von dem Befehlsnamen im Spielkanal. Um zum Beispiel ein neues Spiel zu starten, geben Sie ein `!start-game` Beachten Sie, dass einige Befehle nur in bestimmten Phasen des Spiels verfügbar sind.
### Einrichten des Bots

#### Python verwenden

1. Klonen Sie dieses Repository mit `git clone https://github.com/simeononsecurity/discord-backdoors-and-breaches.git`
2. Installieren Sie die erforderlichen Abhängigkeiten mit `pip install -r requirements.txt`
3. Erstellen einer `config.ini` im Stammverzeichnis des Projekts mit folgendem Inhalt:
```ini
[SETTINGS]
discordtoken = put_discord_bot_token_here
channel_id = put_game_channel_id_here
```
4. Ersetzen Sie `put_discord_bot_token_here` mit Ihrem Discord-Bot-Token und `put_game_channel_id_here` mit der ID des Kanals, auf dem das Spiel gespielt werden soll.
5. Starten Sie den Bot mit `python main.py`

#### Docker verwenden

1. Klonen Sie das Repository und navigieren Sie zu dem Verzeichnis:
```
git clone https://github.com/simeononsecurity/discord-backdoors-and-breaches.git
cd discord-backdoors-and-breaches
```
2. Erstellen einer `.env` im Stammverzeichnis des Projekts und fügen Sie die folgenden Umgebungsvariablen mit den entsprechenden Werten hinzu:
```env
BOT_TOKEN=<discord_bot_token_here>
CHANNEL_ID=<game_channel_id_here>
```
3. Erstellen Sie das Docker-Image mithilfe der bereitgestellten Dockerdatei:
```bash
docker build -t discord-backdoors-and-breaches .
```
4. Führen Sie den Docker-Container aus und übergeben Sie die Umgebungsvariablen aus der Datei `.env` Dateien:
```bash
docker run --env-file .env discord-backdoors-and-breaches
```

Alternativ können Sie die Umgebungsvariablen auch direkt während der `docker run` Befehl:
```bash
docker run -td --name bnbbot -e BOT_TOKEN=<discord_bot_token_here> -e CHANNEL_ID=<game_channel_id_here> discord-backdoors-and-breaches
```
oder ziehen Sie direkt vom Bild auf [dockerhub](https://hub.docker.com/r/simeononsecurity/discord-backdoors-and-breaches)
```bash
docker run -td --name bnbbot -e BOT_TOKEN=<discord_bot_token_here> -e CHANNEL_ID=<game_channel_id_here> simeononsecurity/discord-backdoors-and-breaches:latest
```

