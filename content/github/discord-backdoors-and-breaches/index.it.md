---
title: "Discord Backdoors and Breaches Bot: un compagno di gioco di strategia a turni"
date: 2023-03-10
toc: true
draft: false
description: "Migliora la tua esperienza di gioco con Backdoors and Breaches con questo bot Discord pre-alpha, che fornisce comandi per facilitare il gioco e l'interazione."
tags: ["Bot di discordia", "Backdoor e violazioni", "gioco di strategia a turni", "compagno di gioco", "comandi di gioco", "gioco di strategia bot", "BHIS", "Black Hills InfoSec", "maestro dell'incidente", "Squadra C2", "fasi di gioco", "impostazione del gioco", "istruzioni di gioco", "canale di gioco", "Bot Python", "Bot Docker", "automazione del gioco", "collaborazione di gioco", "coordinamento del gioco", "gioco di cybersicurezza", "sicurezza delle informazioni", "sviluppo di giochi", "Suggerimenti per il gameplay", "gioco multiplayer", "ruoli di gioco", "sfide di gioco", "fasi di gioco", "impostazione dell'ambiente di gioco", "bot dockerizzato", "Dipendenze di Python"]
---

## Bot Discord Backdoors and Breaches - Pre Alpha

[![Docker Image CI](https://github.com/simeononsecurity/discord-backdoors-and-breaches/actions/workflows/docker-image.yml/badge.svg)](https://github.com/simeononsecurity/discord-backdoors-and-breaches/actions/workflows/docker-image.yml)

<img src="https://github.com/simeononsecurity/discord-backdoors-and-breaches/blob/main/.github/images/bnb-dark.png?raw=true" alt="Logo Backdoors and Breaches" width="200"/>


Un bot Discord per Backdoors and Breaches, un gioco di strategia a turni di [BHIS](https://www.blackhillsinfosec.com/projects/backdoorsandbreaches/)

### Comandi disponibili

- `setup-game` Crea un id di gioco e imposta tutte le variabili necessarie.
- `start-game` Avvio di una nuova partita dovrebbe essere eseguito il mio master incidenti solo dopo `setup-game`
- `join-game` Permette ai giocatori di unirsi al gioco assegnando loro il ruolo di "Giocatore" e concedendo loro l'accesso al canale di gioco.
- `play-procedure` Inizia la fase di Procedura del gioco, in cui i giocatori devono completare una serie di sfide per avanzare.
- `play-incident-master` Inizia la fase Incident Master del gioco, in cui i giocatori si alternano nei panni dell'Incident Master e dirigono gli altri giocatori su come rispondere a un incidente simulato.
- `play-c2` Inizia la fase di comando e controllo del gioco, in cui i giocatori sono a turno la squadra C2 e devono coordinarsi con gli altri giocatori per completare una serie di compiti.
- `play-persistence` Inizia la fase di persistenza del gioco, in cui i giocatori devono trovare ed eliminare una backdoor nascosta nel sistema.
- `play-pivot` Inizia la fase Pivot del gioco, in cui i giocatori devono spostarsi in un'altra parte del sistema e continuare la loro indagine.
- `end-game` Termina la partita in corso e cancella il canale di gioco e i ruoli associati.

Per eseguire un comando, digitare `!` o `/` seguito dal nome del comando nel canale di gioco. Ad esempio, per iniziare una nuova partita, digitare `!start-game` Si noti che alcuni comandi possono essere disponibili solo durante alcune fasi del gioco.
### Impostazione del Bot

#### Usare Python

1. Clonare questo repository usando `git clone https://github.com/simeononsecurity/discord-backdoors-and-breaches.git`
2. Installare le dipendenze necessarie utilizzando `pip install -r requirements.txt`
3. Creare un `config.ini` nella cartella principale del progetto con il seguente contenuto:
```ini
[SETTINGS]
discordtoken = put_discord_bot_token_here
channel_id = put_game_channel_id_here
```
4. Sostituire `put_discord_bot_token_here` con il token del bot Discord e `put_game_channel_id_here` con l'ID del canale su cui si vuole giocare.
5. Eseguire il bot utilizzando `python main.py`

#### Utilizzando Docker

1. Clonare il repository e navigare nella directory:
```
git clone https://github.com/simeononsecurity/discord-backdoors-and-breaches.git
cd discord-backdoors-and-breaches
```
2. Creare un `.env` nella directory principale del progetto e aggiungere le seguenti variabili d'ambiente con i valori corrispondenti:
```env
BOT_TOKEN=<discord_bot_token_here>
CHANNEL_ID=<game_channel_id_here>
```
3. Costruire l'immagine Docker utilizzando il file Docker fornito:
```bash
docker build -t discord-backdoors-and-breaches .
```
4. Eseguire il contenitore Docker, inserendo le variabili d'ambiente del file `.env` file:
```bash
docker run --env-file .env discord-backdoors-and-breaches
```

In alternativa, è possibile impostare le variabili d'ambiente direttamente durante l'esecuzione del file `docker run` comando:
```bash
docker run -td --name bnbbot -e BOT_TOKEN=<discord_bot_token_here> -e CHANNEL_ID=<game_channel_id_here> discord-backdoors-and-breaches
```
o estrarre direttamente dall'immagine su [dockerhub](https://hub.docker.com/r/simeononsecurity/discord-backdoors-and-breaches)
```bash
docker run -td --name bnbbot -e BOT_TOKEN=<discord_bot_token_here> -e CHANNEL_ID=<game_channel_id_here> simeononsecurity/discord-backdoors-and-breaches:latest
```

