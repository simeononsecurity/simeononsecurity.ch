---
title: "Discord Backdoors and Breaches Bot: A Turn-Based Strategy Game Companion"
date: 2023-03-10
toc: true
draft: false
description: "Enhance your experience playing Backdoors and Breaches with this pre-alpha Discord bot, providing commands to facilitate gameplay and interaction."
tags: ["Discord bot", "Backdoors and Breaches", "turn-based strategy game", "game companion", "gameplay commands", "strategy game bot", "BHIS", "Black Hills InfoSec", "incident master", "C2 team", "game phases", "game setup", "gameplay instructions", "game channel", "Python bot", "Docker bot", "game automation", "game collaboration", "game coordination", "cybersecurity game", "information security", "game development", "gameplay tips", "multiplayer game", "game roles", "game challenges", "game phases", "game environment setup", "dockerized bot", "Python dependencies"]
---

## Discord Backdoors and Breaches Bot - Pre Alpha

[![Docker Image CI](https://github.com/simeononsecurity/discord-backdoors-and-breaches/actions/workflows/docker-image.yml/badge.svg)](https://github.com/simeononsecurity/discord-backdoors-and-breaches/actions/workflows/docker-image.yml)

<img src="https://github.com/simeononsecurity/discord-backdoors-and-breaches/blob/main/.github/images/bnb-dark.png?raw=true" alt="Backdoors and Breaches logo" width="200"/>


A Discord bot for Backdoors and Breaches, a turn-based strategy game by [BHIS](https://www.blackhillsinfosec.com/projects/backdoorsandbreaches/).

### Available Commands

- `setup-game`: Creates a game id and sets all the needed variables.
- `start-game`: Starts a new game should be run my incident master only after `setup-game`
- `join-game`: Allows players to join the game by assigning them the "Player" role and granting them access to the game channel.
- `play-procedure`: Starts the Procedure phase of the game, where players must complete a series of challenges to progress.
- `play-incident-master`: Starts the Incident Master phase of the game, where players take turns being the Incident Master and directing the other players on how to respond to a simulated incident.
- `play-c2`: Starts the Command and Control phase of the game, where players take turns being the C2 team and must coordinate with the other players to complete a series of tasks.
- `play-persistence`: Starts the Persistence phase of the game, where players must find and eliminate a hidden backdoor in the system.
- `play-pivot`: Starts the Pivot phase of the game, where players must pivot to a different part of the system and continue their investigation.
- `end-game`: Ends the current game and deletes the game channel and associated roles.

To run a command, type `!` or `/` followed by the command name in the game channel. For example, to start a new game, type `!start-game`. Note that some commands may only be available during certain phases of the game.
### Setting up the Bot

#### Using Python

1. Clone this repository using `git clone https://github.com/simeononsecurity/discord-backdoors-and-breaches.git`.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Create a `config.ini` file in the root directory of the project with the following content:
```ini
[SETTINGS]
discordtoken = put_discord_bot_token_here
channel_id = put_game_channel_id_here
```
4. Replace `put_discord_bot_token_here` with your Discord bot token and `put_game_channel_id_here` with the ID of the channel where you want the game to be played.
5. Run the bot using `python main.py`.

#### Using Docker

1. Clone the repository and navigate to the directory:
```
git clone https://github.com/simeononsecurity/discord-backdoors-and-breaches.git
cd discord-backdoors-and-breaches
```
2. Create an `.env` file in the root directory of the project and add the following environment variables with their corresponding values:
```env
BOT_TOKEN=<discord_bot_token_here>
CHANNEL_ID=<game_channel_id_here>
```
3. Build the Docker image using the provided Dockerfile:
```bash
docker build -t discord-backdoors-and-breaches .
```
4. Run the Docker container, passing in the environment variables from the `.env` file:
```bash
docker run --env-file .env discord-backdoors-and-breaches
```

Alternatively, you can set the environment variables directly during the `docker run` command:
```bash
docker run -td --name bnbbot -e BOT_TOKEN=<discord_bot_token_here> -e CHANNEL_ID=<game_channel_id_here> discord-backdoors-and-breaches
```
or pull straight from the image on [dockerhub](https://hub.docker.com/r/simeononsecurity/discord-backdoors-and-breaches)
```bash
docker run -td --name bnbbot -e BOT_TOKEN=<discord_bot_token_here> -e CHANNEL_ID=<game_channel_id_here> simeononsecurity/discord-backdoors-and-breaches:latest
```

