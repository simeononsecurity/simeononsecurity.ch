---
title: "Use ChatGPT in your Terminal (Bash, PowerShell, Python): An Introduction to the ChatGPT CLI Tool for Developers"
date: 2023-02-07
toc: true
draft: false
description: "Learn how to use the OpenAI's ChatGPT model through the convenient Command Line Interface (CLI) for text generation and question answering with ease."
tags: ["ChatGPT", "OpenAI", "Command Line Interface", "CLI", "text generation", "question answering", "developer toolkit", "pip package manager", "Python 3.5", "PowerShell", "Bash"]
cover: "/img/cover/A_developer_sitting_at_their_computer_typing.png"
coverAlt: "A developer sitting at their computer, typing on their keyboard with the ChatGPT CLI open on their terminal."
coverCaption: ""
---
```bash

pip install chatgpt requests readline

```
```powershell

pip install chatgpt requests pyreadline3

```
```bash
chatgpt generate --prompt "What is the purpose of existence?"
```
```bash
chatgpt answer --question "What is the capital of France?"
```
```bash
prompt="What is the meaning of life?"
answer=$(chatgpt generate --prompt "$prompt")
echo "$answer"
```
```powershell
$prompt = "What is the meaning of life?"
$answer = chatgpt generate --prompt $prompt
Write-Host $answer
```
 Le modèle **ChatGPT**, développé par OpenAI, **est un modèle de langage de pointe** capable de générer du texte de type humain. Pour les développeurs, la CLI ChatGPT (interface de ligne de commande) offre un moyen pratique d'interagir avec le modèle ChatGPT via la ligne de commande. Avec la CLI ChatGPT, les développeurs peuvent facilement générer du texte, compléter du texte ou répondre à des questions en utilisant les fonctionnalités avancées du modèle.  L'installation de la CLI ChatGPT se fait sans effort et ne nécessite que Python 3.5 ou une version ultérieure pour être installée sur la machine du développeur. Le gestionnaire de packages pip peut être utilisé pour installer la CLI ChatGPT en exécutant la commande suivante :  **Linux :**  **Windows PowerShell**  Une fois installé, les développeurs peuvent utiliser la CLI ChatGPT pour générer du texte ou répondre automatiquement aux questions. Par exemple, pour générer du texte en fonction d'une invitation, les développeurs peuvent utiliser la commande suivante :   Ou, pour répondre à une question :   La CLI ChatGPT peut également être utilisée avec des scripts de base :  **Linux :**  **Windows PowerShell :**  Ce script produira le texte basé sur l'invite et affichera le texte généré dans la console.  En plus de la génération de texte et de la réponse aux questions, la CLI ChatGPT offre plusieurs autres options, telles que la spécification de la longueur du texte généré, l'ajustement de la température de la sortie et le choix du nombre de réponses à générer.  La **ChatGPT CLI est un ajout précieux à la boîte à outils de tout développeur**, offrant un moyen simple et direct d'interagir avec le modèle avancé ChatGPT. Qu'il s'agisse de générer du texte pour un chatbot, de compléter du texte pour un éditeur de texte ou de répondre à des questions pour un système de questions-réponses, la CLI ChatGPT peut aider les développeurs à atteindre facilement leurs objectifs.