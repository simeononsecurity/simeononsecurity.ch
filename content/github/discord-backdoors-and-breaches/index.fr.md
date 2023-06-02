---
title: "Discord Backdoors and Breaches Bot : un compagnon de jeu de stratégie au tour par tour"
date: 2023-03-10
toc: true
draft: false
description: "Améliorez votre expérience de jeu avec Backdoors and Breaches grâce à ce bot Discord pré-alpha, qui fournit des commandes pour faciliter le jeu et l'interaction."
tags: ["Bot Discord", "Portes dérobées et brèches", "jeu de stratégie au tour par tour", "compagnon de jeu", "commandes de jeu", "jeu de stratégie bot", "BHIS", "Black Hills InfoSec", "maître de l'incident", "Équipe C2", "phases de jeu", "configuration du jeu", "instructions de jeu", "canal de jeu", "Bot Python", "Docker bot", "automatisation des jeux", "collaboration en matière de jeux", "coordination du jeu", "jeu sur la cybersécurité", "la sécurité de l'information", "développement de jeux", "conseils de jeu", "jeu multijoueur", "rôles dans le jeu", "défis du jeu", "phases de jeu", "configuration de l'environnement de jeu", "robot dockerisé", "Dépendances Python"]
---

## Discord Backdoors and Breaches Bot - Pre Alpha

[![Docker Image CI](https://github.com/simeononsecurity/discord-backdoors-and-breaches/actions/workflows/docker-image.yml/badge.svg)](https://github.com/simeononsecurity/discord-backdoors-and-breaches/actions/workflows/docker-image.yml)

<img src="https://github.com/simeononsecurity/discord-backdoors-and-breaches/blob/main/.github/images/bnb-dark.png?raw=true" alt="Backdoors and Breaches logo" width="200"/>


Un bot Discord pour Backdoors and Breaches, un jeu de stratégie au tour par tour par [BHIS](https://www.blackhillsinfosec.com/projects/backdoorsandbreaches/)

### Commandes disponibles

- `setup-game` Crée un identifiant de jeu et définit toutes les variables nécessaires.
- `start-game` Commence un nouveau jeu devrait être exécuté par le maître de l'incident seulement après `setup-game`
- `join-game` Permet aux joueurs de participer au jeu en leur attribuant le rôle de "joueur" et en leur donnant accès au canal du jeu.
- `play-procedure` Lance la phase de procédure du jeu, où les joueurs doivent relever une série de défis pour progresser.
- `play-incident-master` Lance la phase de maîtrise de l'incident du jeu, où les joueurs jouent à tour de rôle le rôle de maître de l'incident et dirigent les autres joueurs sur la façon de répondre à un incident simulé.
- `play-c2` Lance la phase de commandement et de contrôle du jeu, où les joueurs sont à tour de rôle l'équipe C2 et doivent se coordonner avec les autres joueurs pour accomplir une série de tâches.
- `play-persistence` Lance la phase de persistance du jeu, au cours de laquelle les joueurs doivent trouver et éliminer une porte dérobée cachée dans le système.
- `play-pivot` Lance la phase Pivot du jeu, au cours de laquelle les joueurs doivent pivoter vers une autre partie du système et poursuivre leur enquête.
- `end-game` Met fin au jeu en cours et supprime le canal de jeu et les rôles associés.

Pour exécuter une commande, tapez `!` ou `/` suivi du nom de la commande dans le canal de jeu. Par exemple, pour commencer un nouveau jeu, tapez `!start-game` Notez que certaines commandes ne sont disponibles que pendant certaines phases du jeu.
### Configuration du robot

#### Utilisation de Python

1. Clonez ce dépôt en utilisant `git clone https://github.com/simeononsecurity/discord-backdoors-and-breaches.git`
2. Installez les dépendances requises en utilisant `pip install -r requirements.txt`
3. Créer un `config.ini` dans le répertoire racine du projet avec le contenu suivant :
```ini
[SETTINGS]
discordtoken = put_discord_bot_token_here
channel_id = put_game_channel_id_here
```
4. Remplacer `put_discord_bot_token_here` avec votre jeton de bot Discord et `put_game_channel_id_here` avec l'ID de la chaîne sur laquelle vous voulez jouer.
5. Exécutez le bot en utilisant `python main.py`

#### en utilisant Docker

1. Clonez le dépôt et naviguez jusqu'au répertoire :
```
git clone https://github.com/simeononsecurity/discord-backdoors-and-breaches.git
cd discord-backdoors-and-breaches
```
2. Créer un `.env` dans le répertoire racine du projet et ajoutez les variables d'environnement suivantes avec leurs valeurs correspondantes :
```env
BOT_TOKEN=<discord_bot_token_here>
CHANNEL_ID=<game_channel_id_here>
```
3. Construisez l'image Docker en utilisant le fichier Dockerfile fourni :
```bash
docker build -t discord-backdoors-and-breaches .
```
4. Exécutez le conteneur Docker, en lui passant les variables d'environnement de la section `.env` des dossiers :
```bash
docker run --env-file .env discord-backdoors-and-breaches
```

Vous pouvez également définir les variables d'environnement directement lors de l'exécution de la commande `docker run` commande :
```bash
docker run -td --name bnbbot -e BOT_TOKEN=<discord_bot_token_here> -e CHANNEL_ID=<game_channel_id_here> discord-backdoors-and-breaches
```
ou tirer directement de l'image sur [dockerhub](https://hub.docker.com/r/simeononsecurity/discord-backdoors-and-breaches)
```bash
docker run -td --name bnbbot -e BOT_TOKEN=<discord_bot_token_here> -e CHANNEL_ID=<game_channel_id_here> simeononsecurity/discord-backdoors-and-breaches:latest
```

