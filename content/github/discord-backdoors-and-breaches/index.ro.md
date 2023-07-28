---
title: "Discord Backdoors și spargeri Bot: Un companion de joc de strategie pe rând de joc"
date: 2023-03-10
toc: true
draft: false
description: "Îmbunătățește-ți experiența de joc în Backdoors and Breaches cu acest robot Discord pre-alpha, care oferă comenzi pentru a facilita jocul și interacțiunea."
tags: ["Discord bot", "Backdoors și breșe", "joc de strategie bazat pe turnuri", "partener de joc", "comenzi de joc", "joc de strategie bot", "BHIS", "Black Hills InfoSec", "comandantul incidentului", "Echipa C2", "faze de joc", "configurare joc", "instrucțiuni de joc", "canal de joc", "Python bot", "Docker bot", "automatizarea jocurilor", "joc de colaborare", "coordonarea jocului", "joc de securitate cibernetică", "securitatea informațiilor", "dezvoltarea de jocuri", "sfaturi de joc", "joc multiplayer", "roluri de joc", "provocări de joc", "faze de joc", "configurarea mediului de joc", "bot dockerizat", "Dependențe Python"]
---

## Discord Backdoors și Breaches Bot - Pre Alpha

[![Docker Image CI](https://github.com/simeononsecurity/discord-backdoors-and-breaches/actions/workflows/docker-image.yml/badge.svg)](https://github.com/simeononsecurity/discord-backdoors-and-breaches/actions/workflows/docker-image.yml)

<img src="https://github.com/simeononsecurity/discord-backdoors-and-breaches/blob/main/.github/images/bnb-dark.png?raw=true" alt="Backdoors and Breaches logo" width="200"/>


Un bot de Discord pentru Backdoors and Breaches, un joc de strategie pe rând de către [BHIS](https://www.blackhillsinfosec.com/projects/backdoorsandbreaches/)

### Comenzi disponibile

- `setup-game` Creează un id de joc și setează toate variabilele necesare.
- `start-game` Începe un nou joc ar trebui să fie rulat maestrul meu incident numai după ce `setup-game`
- `join-game` Permite jucătorilor să se alăture jocului prin atribuirea rolului "Player" și acordarea accesului la canalul de joc.
- `play-procedure` Începe faza de procedură a jocului, în care jucătorii trebuie să completeze o serie de provocări pentru a progresa.
- `play-incident-master` Începe faza Incident Master a jocului, în care jucătorii sunt, pe rând, Incident Master și îi îndrumă pe ceilalți jucători cum să răspundă la un incident simulat.
- `play-c2` Începe faza de comandă și control a jocului, în care jucătorii sunt pe rând echipa C2 și trebuie să se coordoneze cu ceilalți jucători pentru a îndeplini o serie de sarcini.
- `play-persistence` Începe faza de persistență a jocului, în care jucătorii trebuie să găsească și să elimine un backdoor ascuns în sistem.
- `play-pivot` Începe faza de Pivot a jocului, în care jucătorii trebuie să pivoteze către o altă parte a sistemului și să-și continue investigația.
- `end-game` Încheie jocul curent și șterge canalul de joc și rolurile asociate.

Pentru a rula o comandă, tastați `!` sau `/` urmată de numele comenzii în canalul de joc. De exemplu, pentru a începe un joc nou, tastați `!start-game` Rețineți că este posibil ca unele comenzi să fie disponibile doar în anumite faze ale jocului.
### Configurarea robotului

#### Folosind Python

1. Clonați acest depozit folosind `git clone https://github.com/simeononsecurity/discord-backdoors-and-breaches.git`
2. Instalați dependențele necesare utilizând `pip install -r requirements.txt`
3. Creați un `config.ini` în directorul rădăcină al proiectului, cu următorul conținut:
```ini
[SETTINGS]
discordtoken = put_discord_bot_token_here
channel_id = put_game_channel_id_here
```
4. Înlocuiți `put_discord_bot_token_here` cu simbolul tău de robot Discord și `put_game_channel_id_here` cu ID-ul canalului pe care doriți ca jocul să fie jucat.
5. Rulați robotul folosind `python main.py`

#### Folosind Docker

1. Clonați depozitul și navigați în director:
```
git clone https://github.com/simeononsecurity/discord-backdoors-and-breaches.git
cd discord-backdoors-and-breaches
```
2. Creați un `.env` în directorul rădăcină al proiectului și adăugați următoarele variabile de mediu cu valorile lor corespunzătoare:
```env
BOT_TOKEN=<discord_bot_token_here>
CHANNEL_ID=<game_channel_id_here>
```
3. Construiți imaginea Docker utilizând fișierul Docker furnizat:
```bash
docker build -t discord-backdoors-and-breaches .
```
4. Rulați containerul Docker, trecând variabilele de mediu din fișierul `.env` fișiere:
```bash
docker run --env-file .env discord-backdoors-and-breaches
```

Alternativ, puteți seta variabilele de mediu direct în timpul procesului `docker run` comandă:
```bash
docker run -td --name bnbbot -e BOT_TOKEN=<discord_bot_token_here> -e CHANNEL_ID=<game_channel_id_here> discord-backdoors-and-breaches
```
sau trageți direct din imaginea de pe [dockerhub](https://hub.docker.com/r/simeononsecurity/discord-backdoors-and-breaches)
```bash
docker run -td --name bnbbot -e BOT_TOKEN=<discord_bot_token_here> -e CHANNEL_ID=<game_channel_id_here> simeononsecurity/discord-backdoors-and-breaches:latest
```

