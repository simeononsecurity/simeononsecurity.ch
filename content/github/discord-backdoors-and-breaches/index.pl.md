---
title: "Discord Backdoors and Breaches Bot: Towarzysz turowej gry strategicznej"
date: 2023-03-10
toc: true
draft: false
description: "Zwiększ swoje wrażenia z gry w Backdoors and Breaches dzięki temu botowi Discord w wersji pre-alpha, dostarczającemu polecenia ułatwiające rozgrywkę i interakcję."
tags: ["Bot Discorda", "Backdoory i włamania", "Turowa gra strategiczna", "towarzysz gry", "polecenia rozgrywki", "bot gry strategicznej", "BHIS", "Black Hills InfoSec", "mistrz incydentów", "Zespół C2", "fazy gry", "konfiguracja gry", "Instrukcje dotyczące rozgrywki", "kanał gry", "Bot Python", "Bot Docker", "automatyzacja gier", "współpraca przy grze", "koordynacja gry", "gra cyberbezpieczeństwa", "bezpieczeństwo informacji", "tworzenie gier", "Wskazówki dotyczące rozgrywki", "gra wieloosobowa", "role w grze", "wyzwania w grach", "fazy gry", "Konfiguracja środowiska gry", "bot dokowany", "Zależności Pythona"]
---

## Discord Backdoors and Breaches Bot - Pre Alpha

[![Docker Image CI](https://github.com/simeononsecurity/discord-backdoors-and-breaches/actions/workflows/docker-image.yml/badge.svg)](https://github.com/simeononsecurity/discord-backdoors-and-breaches/actions/workflows/docker-image.yml)

<img src="https://github.com/simeononsecurity/discord-backdoors-and-breaches/blob/main/.github/images/bnb-dark.png?raw=true" alt="Backdoors and Breaches logo" width="200"/>


Bot Discord dla Backdoors and Breaches, turowej gry strategicznej autorstwa [BHIS](https://www.blackhillsinfosec.com/projects/backdoorsandbreaches/)

### Dostępne polecenia

- `setup-game` Tworzy identyfikator gry i ustawia wszystkie potrzebne zmienne.
- `start-game` Nowa gra powinna zostać uruchomiona przez mistrza incydentów dopiero po `setup-game`
- `join-game` Umożliwia graczom dołączenie do gry poprzez przypisanie im roli "Gracza" i przyznanie im dostępu do kanału gry.
- `play-procedure` Rozpoczyna fazę procedury gry, w której gracze muszą ukończyć serię wyzwań, aby przejść dalej.
- `play-incident-master` Rozpoczyna fazę Mistrza Incydentu, w której gracze na zmianę wcielają się w rolę Mistrza Incydentu i instruują innych graczy, jak reagować na symulowany incydent.
- `play-c2` Rozpoczyna się faza dowodzenia i kontroli, w której gracze na zmianę stają się zespołem C2 i muszą koordynować działania z innymi graczami, aby wykonać serię zadań.
- `play-persistence` Rozpoczyna fazę Wytrwałości w grze, w której gracze muszą znaleźć i wyeliminować ukrytego backdoora w systemie.
- `play-pivot` Rozpoczyna fazę Pivot gry, w której gracze muszą przejść do innej części systemu i kontynuować śledztwo.
- `end-game` Kończy bieżącą grę i usuwa kanał gry oraz powiązane z nim role.

Aby uruchomić polecenie, wpisz `!` lub `/` po którym następuje nazwa polecenia w kanale gry. Na przykład, aby rozpocząć nową grę, wpisz `!start-game` Należy pamiętać, że niektóre polecenia mogą być dostępne tylko w określonych fazach gry.
### Konfiguracja bota

#### Używanie Pythona

1. Sklonuj to repozytorium używając `git clone https://github.com/simeononsecurity/discord-backdoors-and-breaches.git`
2. Zainstaluj wymagane zależności za pomocą `pip install -r requirements.txt`
3. Utwórz `config.ini` w katalogu głównym projektu z następującą zawartością:
```ini
[SETTINGS]
discordtoken = put_discord_bot_token_here
channel_id = put_game_channel_id_here
```
4. Wymienić `put_discord_bot_token_here` z tokenem bota Discord i `put_game_channel_id_here` z identyfikatorem kanału, na którym ma być rozgrywana gra.
5. Uruchom bota używając `python main.py`

#### Korzystanie z platformy Docker

1. Sklonuj repozytorium i przejdź do katalogu:
```
git clone https://github.com/simeononsecurity/discord-backdoors-and-breaches.git
cd discord-backdoors-and-breaches
```
2. Utwórz `.env` w katalogu głównym projektu i dodać następujące zmienne środowiskowe wraz z odpowiadającymi im wartościami:
```env
BOT_TOKEN=<discord_bot_token_here>
CHANNEL_ID=<game_channel_id_here>
```
3. Zbuduj obraz Docker przy użyciu dostarczonego pliku Dockerfile:
```bash
docker build -t discord-backdoors-and-breaches .
```
4. Uruchom kontener Docker, przekazując zmienne środowiskowe z pliku `.env` pliki:
```bash
docker run --env-file .env discord-backdoors-and-breaches
```

Alternatywnie, można ustawić zmienne środowiskowe bezpośrednio podczas wykonywania polecenia `docker run` polecenie:
```bash
docker run -td --name bnbbot -e BOT_TOKEN=<discord_bot_token_here> -e CHANNEL_ID=<game_channel_id_here> discord-backdoors-and-breaches
```
lub pobrać bezpośrednio z obrazu na stronie [dockerhub](https://hub.docker.com/r/simeononsecurity/discord-backdoors-and-breaches)
```bash
docker run -td --name bnbbot -e BOT_TOKEN=<discord_bot_token_here> -e CHANNEL_ID=<game_channel_id_here> simeononsecurity/discord-backdoors-and-breaches:latest
```

