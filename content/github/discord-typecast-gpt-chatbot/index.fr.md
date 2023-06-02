---
title: "Discord Typecast GPT Chatbot : Agent d'assistance amical et compétent basé sur Discord"
date: 2023-03-24
toc: true
draft: false
description: "Améliorez votre serveur Discord avec un chatbot amical et compétent qui fournit des réponses utiles, répond aux questions liées au serveur et crée des interactions intéressantes."
tags: ["Chatbot Discord", "agent d'assistance", "assistance au serveur", "user queries", "ressources pertinentes", "environnement positif", "avis", "préférences", "recommendations", "des interactions engageantes", "bot amical", "bot bien informé", "Bot basé sur Discord", "assistant virtuel", "soutien automatisé", "bot de conversation", "réponses informatives", "bot ingénieux", "chatbot interactif", "gestion des serveurs", "l'assistance aux utilisateurs", "Un robot doté d'une intelligence artificielle", "discord.io", "chatbot en action", "docker", "python", "Déploiement de robots", "environnement virtuel", "architecture des robots", "contrôleurs de robots", "Services de robots"]
---

**discord-typecast-gpt-chatbot**

[![Docker Image CI](https://github.com/CyberSentinels/discord-typecast-gpt-chatbot/actions/workflows/docker-image.yml/badge.svg)](https://github.com/CyberSentinels/discord-typecast-gpt-chatbot/actions/workflows/docker-image.yml)

Ce bot est un agent d'assistance basé sur Discord. Il fournit des réponses utiles aux questions des utilisateurs, aide à résoudre les problèmes liés au serveur et dirige les utilisateurs vers les ressources appropriées. Le bot est amical, bien informé et maintient un environnement positif. Il peut également partager des opinions, des préférences et des recommandations sur divers sujets, créant ainsi des interactions intéressantes et informatives avec les utilisateurs.

[See the bot in action](https://discord.io/cybersentinels)

## Comment exécuter le bot
### Utilisation de docker
```bash
docker run -td --name cyberchatbot -e DISCORD_BOT_APP_TOKEN="INSERT YOUR BOT TOKEN HERE" -e OPENAI_API_KEY="INSERT YOUR OPENAI API KEY HERE" simeononsecurity/discord-typecast-gpt-chatbot:latest
```
### Comment exécuter le bot manuellement en utilisant python

Pour commencer à faire fonctionner ce dépôt, vous devez effectuer les étapes suivantes :

1. Clonez ce référentiel et passez à la racine du produit

```bash
git clone URL
cd repo_name
```
2. créer un `.env` à la racine du projet (ce sera `.gitignored` et collez votre token discord bot et votre token openai :

```env
DISCORD_BOT_APP_TOKEN=PASTE_DISCORD_TOKEN_HERE
OPENAI_API_KEY=PASTE_OPENAI_API_TOKEN_HERE
```

3. Créez un nouvel environnement virtuel en utilisant `venv`
```bash
python3 -m venv venv
```

4. Activez l'environnement virtuel :
```bash
source venv/bin/activate
```

5. Installez les dépendances listées dans `requirements.txt`
   
```bash
pip install -r requirements.txt
```

6. Si vous installez de nouvelles dépendances avec `pip install` veillez à régénérer le fichier requirements.txt avec :

```bash
pip freeze > requirements.txt
```
#### Comment résoudre le problème des locales
```bash
sudo apt-get install locales -y
sudo locale-gen en_US.UTF-8 en_CA.UTF-8
sudo update-locale
```

## Architecture

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
