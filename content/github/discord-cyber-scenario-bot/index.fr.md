---
title: "Scénario cybernétique de Discord : améliorer la formation et la sensibilisation à la cybersécurité"
date: 2023-02-22
toc: true
draft: false
description: "Découvrez comment le CyberScenarioBot peut améliorer votre programme de formation et de sensibilisation à la cybersécurité sur Discord, en proposant des quiz, des scénarios, des classements et de puissants outils de commande."
tags: ["Bot Discord", "formation à la cybersécurité", "sensibilisation à la cybersécurité", "scénario bot", "quiz bot", "classement", "commandes d'outils", "Docker", "Python", "tests automatisés", "API Discord", "documentation pour les développeurs", "contribuant", "Licence MIT", "CyberScenarioBot", "CyberSentinelles", "améliorer la formation", "programme de sensibilisation", "scénarios de cybersécurité", "environnement serveur", "commandes personnalisées", "déployer et gérer", "quiz et scénarios", "commandes d'outils", "commandes d'information", "questions et contributions", "Application Discord pour les développeurs", "Documentation Discord.py", "travailler avec les développeurs", "communauté Serveur Discord"]
---


**CyberScenarioBot**

Scénario Cyber Discord, Quiz, et Bot de formation à la cybersensibilisation.

Vous pouvez passer à [🚀 Quick Start](#quick-start) pour ajouter `CyberScenarioBot` sur votre serveur.

[![Docker Image CI](https://github.com/simeononsecurity/discord-cyber-scenario-bot/actions/workflows/docker-image.yml/badge.svg)](https://github.com/simeononsecurity/discord-cyber-scenario-bot/actions/workflows/docker-image.yml)

## Introduction

Ce robot peut être utile dans le cadre d'un programme de formation ou de sensibilisation à la cybersécurité, où les utilisateurs peuvent être exposés à divers scénarios de cybersécurité et apprendre à les prévenir ou à y répondre. En utilisant un bot Discord, les scénarios peuvent être facilement partagés avec les utilisateurs dans un environnement serveur, et le bot peut être personnalisé pour inclure des commandes ou des fonctionnalités supplémentaires selon les besoins. En outre, le bot peut être exécuté dans un conteneur Docker, ce qui facilite son déploiement et sa gestion dans divers environnements.

[See the bot in action](https://discord.gg/CYVe2CyrXk)

## 🚀 Démarrage rapide

### Comment exécuter :
#### Python :
Si vous utilisez un système Unix, ouvrez un terminal et naviguez jusqu'au répertoire où se trouve le script bot.py. Exécutez ensuite la commande suivante :
```bash
export BOT_TOKEN="INSERT YOUR BOT TOKEN HERE"
export GUILD_ID="INSERT YOUR GUILD ID HERE (only needed for timed quizes and leaderboard)"
export LEADERBOARD_CHANNEL_ID="INSERT YOUR LEADERBOARD CHANNEL ID HERE (Only needed for leaderboard for prompts)" 
export CHANNEL_ID="INSERT YOUR CHANNEL ID HERE (only needed for timed quizes)"
export APLUSROLE="INSERT YOUR A+ ROLE ID HERE (only needed for timed quizes)"
export NETPLUSROLE="INSERT YOUR Network+ ROLE ID HERE (only needed for timed quizes)"
export SECPLUSROLE="INSERT YOUR Security+ ROLE ID HERE (only needed for timed quizes)"
export QUIZROLE="INSERT YOUR QUIZ ROLE ID HERE (only needed for timed quizes)"
python bot.py
```
Notez que si vous utilisez un système Windows, vous devrez utiliser une commande légèrement différente pour définir la variable d'environnement. Voici un exemple de commande qui devrait fonctionner sous Windows :
```shell
set BOT_TOKEN="INSERT YOUR BOT TOKEN HERE"
set GUILD_ID="INSERT YOUR GUILD ID HERE (only needed for timed quizes)"
set LEADERBOARD_CHANNEL_ID="INSERT YOUR LEADERBOARD CHANNEL ID HERE (Only needed for leaderboard for prompts)" 
set LEADERBOARD_PERSIST_CHANNEL_ID="INSERT YOUR LEADERBOARD PERSIST CHANNEL ID HERE (Only needed for leaderboard for prompts)" 
set CHANNEL_ID="INSERT YOUR CHANNEL ID HERE (only needed for timed quizes)"
set APLUSROLE="INSERT YOUR A+ ROLE ID HERE (only needed for timed quizes)"
set NETPLUSROLE="INSERT YOUR Network+ ROLE ID HERE (only needed for timed quizes)"
set SECPLUSROLE="INSERT YOUR Security+ ROLE ID HERE (only needed for timed quizes)"
set QUIZROLE="INSERT YOUR QUIZ ROLE ID HERE (only needed for timed quizes)"
python bot.py
```
#### Docker :
Lors de l'exécution du conteneur Docker, vous pouvez passer la variable d'environnement BOT_TOKEN en utilisant l'option -e comme suit :

```bash
docker run -e BOT_TOKEN="INSERT YOUR BOT TOKEN HERE" -it --rm simeononsecurity/discord-cyber-scenario-bot:latest
```

Pour exécuter le robot en arrière-plan :
```bash
docker run -td --name scenario-bot -e BOT_TOKEN="INSERT YOUR BOT TOKEN HERE" simeononsecurity/discord-cyber-scenario-bot:latest
```

Pour exécuter le robot en arrière-plan avec toutes les invites et tous les rôles programmés :
```bash
docker run -td --name scenario-bot \
-e BOT_TOKEN="INSERT YOUR BOT TOKEN HERE" \
-e GUILD_ID="INSERT YOUR GUILD ID HERE" \
-e LEADERBOARD_CHANNEL_ID="INSERT YOUR LEADERBOARD CHANNEL ID HERE" \
-e LEADERBOARD_PERSIST_CHANNEL_ID="INSERT YOUR LEADERBOARD PERSIST CHANNEL ID HERE" \
-e CHANNEL_ID="INSERT YOUR CHANNEL ID HERE" \
-e APLUSROLE="INSERT YOUR A+ ROLE ID HERE" \
-e NETPLUSROLE="INSERT YOUR NET+ ROLE ID HERE" \
-e SECPLUSROLE="INSERT YOUR SEC+ ROLE ID HERE" \
-e QUIZROLE="INSERT YOUR QUIZ ROLE ID HERE" \
simeononsecurity/discord-cyber-scenario-bot:latest
```

## Caractéristiques
### **Commandes disponibles**
*Préfixe de la commande : '!', '/'*****

### 📝 **Commandes de questionnaire et de scénario**
- **Aplus** : Répond à l'invite A+ de CompTIA.
- Bluecenario** : Répond avec un scénario de l'équipe bleue : Répond avec un scénario de l'équipe bleue.
- CCNA** : Répond à la question à choix multiples CCNA de Cisco.
- **CEH** : Répond aux questions à choix multiples du CEH de EC-Council.
- **CISSP** : Répond aux questions à choix multiples du CISSP de l'ISC2.
- Linuxplus** : Répond à la question à choix multiples Linux+ de CompTIA.
- Netplus** : Répond à la question à choix multiples Network+ du CompTIA.
- **Quiz** : Répond à une question aléatoire de sensibilisation à la cybersécurité.
- Redcenario** : Répond à un scénario de l'équipe d'intervention.
- **Secplus** : Répond à une question de CompTIA relative à la sécurité+.

#### 💯🎯 **Leaderboard**
*Les questions à choix multiples sont dynamiquement pondérées, comme dans les examens réels, en fonction des réponses correctes ou incorrectes.

- *Suivez votre progression au fil du temps et comparez vos résultats à ceux des autres membres de votre serveur*
- Voir les scores pour chaque catégorie de quiz ainsi que les scores globaux.

### 🛠️ **Commandes d'outils**
- **Dns** : Prend en charge un `domain name` et renvoie les enregistrements A, AAAA, NS, TXT, etc.
- **Hash** : Prend en compte `1 of 4 supported algos` et un `string` et produit un hachage correspondant.
- **Ping** : Prend en entrée un `IP address` et renvoie un message de succès et de latence moyenne ou un message d'échec.
- **Recherche de téléphones** : Prend en compte un `phone number` et indique le transporteur et l'emplacement.
- **Shodanip** : Prend en charge un `IP address` et fournit des informations utiles à partir de https://internetdb.shodan.io/.
- **Sous-réseau** : Prend en charge un `IP address` et un `Subnet Mask` et indique la plage, les adresses IP utilisables, l'adresse de la passerelle, l'adresse de diffusion et le nombre d'hôtes pris en charge.
- **Whois** : Prend en charge un `domain name` et fournit des informations sur le whois d'un domaine.

### ℹ️ **Commandes d'information**
- **Commandes** : Répond avec ce message.
- **Socials** : Répond avec les différents comptes de médias sociaux et sites web du bot.

### ⚙️ **Facile à installer**
- Voir [🚀 Quick Start](#🚀-quick-start)

## Fonctionnalités à venir

Ces fonctionnalités ont une date de mise en œuvre planifiée, mais nous les suivons et nous aimerions [contributions](#contributing) pour eux.

- Des fonctions avancées de classement, y compris des classements hebdomadaires et mensuels.
- Des messages-guides et des questionnaires personnalisables pour répondre aux besoins spécifiques en matière de formation à la cybersécurité.
- Rapports et analyses avancés pour suivre les progrès et les performances des utilisateurs.

## Usage

Le CyberScenarioBot offre diverses commandes et fonctionnalités pour améliorer votre programme de formation et de sensibilisation à la cybersécurité. Voici quelques cas d'utilisation courants :

1. **Questionnaires et scénarios** : Utilisez le `/quiz` pour obtenir une question aléatoire de sensibilisation à la cybersécurité. Utilisez des commandes telles que `/aplus` `/netplus` `/secplus` pour accéder à des invites spécifiques liées aux certifications CompTIA. Utilisez des commandes telles que `/bluescenario` et `/redscenario` pour obtenir respectivement les scénarios de l'équipe bleue et de l'équipe rouge.

2. **Leaderboard** : Suivez les progrès de l'utilisateur et comparez vos scores avec ceux des autres membres de votre serveur en répondant aux questions du quiz et de la certification.

3. **Commandes d'outils** : Utilisez diverses commandes d'outils pour effectuer des tâches liées au DNS, au hachage, au ping, à la recherche de numéros de téléphone, à la recherche d'IP Shodan, aux calculs de sous-réseaux et à la recherche de domaines WHOIS. Utilisez des commandes telles que `/dns` `/hash` `/ping` `/phonelookup` `/shodanip` `/subnet` et `/whois` suivi des arguments appropriés.

4. **Commandes d'information** : Utiliser la commande `/commands` pour obtenir une liste des commandes disponibles. Utilisez la commande `/socials` pour obtenir des informations sur les comptes de médias sociaux et les sites web du robot.

N'hésitez pas à explorer et à expérimenter les commandes disponibles afin d'améliorer votre formation à la cybersécurité et d'impliquer les membres de votre serveur.

## Questions

Si les utilisateurs rencontrent des problèmes ou ont des suggestions d'amélioration, ils peuvent ouvrir un dossier GitHub pour les signaler. Encouragez les utilisateurs à fournir des informations détaillées sur le problème et les étapes pour le reproduire.

Pour ouvrir un problème, suivez les étapes suivantes :

1. Allez dans l'onglet Problèmes sur le dépôt GitHub du projet : [Issues](https://github.com/CyberSentinels/discord-cyber-scenario-bot/issues)
2. Cliquez sur le bouton "New Issue".
3. Donnez un titre descriptif et une description claire du problème.
4. Incluez tous les journaux, captures d'écran ou extraits de code pertinents pour faciliter le dépannage.
5. Soumettre le problème et attendre une communication ultérieure de la part des responsables du projet.

## Contribuer

Toutes les contributions sont les bienvenues.
Ce projet a été conçu comme un effort de développement et d'apprentissage de la part de [the CyberSentinels club](https://cybersentinels.org) et nous serons ravis de vous aider à contribuer et de répondre à vos questions.

### Tests automatisés en Python

Ce repo inclut des tests automatisés, vous pouvez voir des exemples sur la façon d'implémenter cela [here](https://github.com/CyberSentinels/penguin-pie)

### Discord API et documentation pour les développeurs

Pour tester les changements et implémenter les fonctionnalités, vous aurez besoin de quelques éléments.

- [Discord Developer Application](https://discord.com/developers/applications)
- [Discord Developers Documentation](https://discord.com/developers/docs/intro)
- [Discord.py Documentation](https://discordpy.readthedocs.io/en/stable/)

### Travailler avec les développeurs

Vous pouvez discuter des efforts de développement sur le serveur discord de la communauté [here](https://discord.gg/CYVe2CyrXk)
  
## Licence

[MIT](https://github.com/simeononsecurity/glotta/blob/main/LICENSE)
