---
title: "Discord Backdoors and Breaches Bot: A Turn-Based Strategy Game Companion"
date: 2023-03-10
toc: true
draft: false
description: "Улучшите свой опыт игры в Backdoors and Breaches с помощью этого пре-альфа Discord-бота, предоставляющего команды для облегчения игрового процесса и взаимодействия."
tags: ["Discord бот", "Бэкдоры и взломы", "пошаговая стратегическая игра", "игровой компаньон", "игровые команды", "стратегический игровой бот", "BHIS", "Black Hills InfoSec", "мастер инцидента", "Команда C2", "этапы игры", "настройка игры", "инструкции по игре", "игровой канал", "Python-бот", "Docker-бот", "автоматизация игр", "игровое сотрудничество", "координация игры", "игра по кибербезопасности", "информационная безопасность", "разработка игр", "советы по геймплею", "многопользовательская игра", "игровые роли", "игровые задачи", "этапы игры", "настройка игрового окружения", "докеризованный бот", "Зависимости Python"]
---

## Discord Backdoors and Breaches Bot - Pre Alpha

[![Docker Image CI](https://github.com/simeononsecurity/discord-backdoors-and-breaches/actions/workflows/docker-image.yml/badge.svg)](https://github.com/simeononsecurity/discord-backdoors-and-breaches/actions/workflows/docker-image.yml)

<img src="https://github.com/simeononsecurity/discord-backdoors-and-breaches/blob/main/.github/images/bnb-dark.png?raw=true" alt="Логотип Backdoors and Breaches" width="200"/>


Discord-бот для Backdoors and Breaches, пошаговой стратегической игры от [BHIS](https://www.blackhillsinfosec.com/projects/backdoorsandbreaches/)

### Доступные команды

- `setup-game` Создает идентификатор игры и устанавливает все необходимые переменные.
- `start-game` Запуск новой игры должен осуществляться моим мастером инцидентов только после `setup-game`
- `join-game` Позволяет игрокам присоединиться к игре, назначив им роль "Игрок" и предоставив доступ к игровому каналу.
- `play-procedure` Начинает процедурный этап игры, в котором игроки должны выполнить ряд заданий, чтобы продвинуться вперед.
- `play-incident-master` Начинает фазу игры "Инцидент-мастер", в которой игроки по очереди становятся инцидент-мастерами и дают указания другим игрокам, как реагировать на смоделированный инцидент.
- `play-c2` Начинается командно-контрольная фаза игры, в которой игроки по очереди выступают в роли команды C2 и должны координировать свои действия с другими игроками для выполнения ряда задач.
- `play-persistence` Начинает фазу игры "Настойчивость", в которой игроки должны найти и устранить скрытый бэкдор в системе.
- `play-pivot` Начинает фазу игры Pivot, в которой игроки должны переместиться в другую часть системы и продолжить исследование.
- `end-game` Завершает текущую игру и удаляет игровой канал и связанные с ним роли.

Чтобы запустить команду, введите `!` или `/` после чего следует название команды в игровом канале. Например, чтобы начать новую игру, введите `!start-game` Обратите внимание, что некоторые команды могут быть доступны только на определенных этапах игры.
### Настройка бота

#### Использование Python

1. Клонируйте этот репозиторий с помощью `git clone https://github.com/simeononsecurity/discord-backdoors-and-breaches.git`
2. Установите необходимые зависимости с помощью `pip install -r requirements.txt`
3. Создать `config.ini` файл в корневом каталоге проекта со следующим содержанием:
```ini
[SETTINGS]
discordtoken = put_discord_bot_token_here
channel_id = put_game_channel_id_here
```
4. Заменить `put_discord_bot_token_here` с вашим токеном бота Discord и `put_game_channel_id_here` с идентификатором канала, на котором будет проходить игра.
5. Запустите бота, используя `python main.py`

#### Использование Docker

1. Клонируйте репозиторий и перейдите в каталог:
```
git clone https://github.com/simeononsecurity/discord-backdoors-and-breaches.git
cd discord-backdoors-and-breaches
```
2. Создать `.env` файл в корневом каталоге проекта и добавьте следующие переменные окружения с соответствующими значениями:
```env
BOT_TOKEN=<discord_bot_token_here>
CHANNEL_ID=<game_channel_id_here>
```
3. Соберите образ Docker, используя предоставленный Dockerfile:
```bash
docker build -t discord-backdoors-and-breaches .
```
4. Запустите контейнер Docker, передав в него переменные окружения из раздела `.env` файлы:
```bash
docker run --env-file .env discord-backdoors-and-breaches
```

В качестве альтернативы можно задать переменные окружения непосредственно во время выполнения команды `docker run` команда:
```bash
docker run -td --name bnbbot -e BOT_TOKEN=<discord_bot_token_here> -e CHANNEL_ID=<game_channel_id_here> discord-backdoors-and-breaches
```
или взять прямо из изображения на [dockerhub](https://hub.docker.com/r/simeononsecurity/discord-backdoors-and-breaches)
```bash
docker run -td --name bnbbot -e BOT_TOKEN=<discord_bot_token_here> -e CHANNEL_ID=<game_channel_id_here> simeononsecurity/discord-backdoors-and-breaches:latest
```

