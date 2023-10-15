---
title: "Discord Typecast GPT Chatbot: Agente de asistencia basado en Discord, amable y experto"
date: 2023-03-24
toc: true
draft: false
description: "Mejore su servidor Discord con un chatbot amable y experto que proporcione respuestas útiles, ayude con preguntas relacionadas con el servidor y cree interacciones atractivas."
tags: ["Chatbot de Discordia", "agente de apoyo", "asistencia al servidor", "consultas de usuarios", "recursos pertinentes", "ambiente positivo", "opiniones", "preferencias", "recomendaciones", "interacciones atractivas", "bot amigo", "bot experto", "Bot basado en Discord", "asistente virtual", "asistencia automatizada", "bot de conversación", "respuestas informativas", "bot ingenioso", "chatbot interactivo", "gestión de servidores", "asistencia al usuario", "Robot con IA", "discord.io", "chatbot en acción", "docker", "python", "despliegue de bots", "entorno virtual", "arquitectura bot", "controladores bot", "servicios bot"]
---

**discord-typecast-gpt-chatbot**

[![Docker Image CI](https://github.com/CyberSentinels/discord-typecast-gpt-chatbot/actions/workflows/docker-image.yml/badge.svg)](https://github.com/CyberSentinels/discord-typecast-gpt-chatbot/actions/workflows/docker-image.yml)

Este bot es un agente de soporte basado en Discord. Proporciona respuestas útiles a las consultas de los usuarios, ayuda con preguntas relacionadas con el servidor y dirige a los usuarios a los recursos pertinentes. El bot es amable, está bien informado y mantiene un ambiente positivo. También puede compartir opiniones, preferencias y recomendaciones relacionadas con diversos temas, creando interacciones atractivas e informativas con los usuarios.

[See the bot in action](https://discord.gg/CYVe2CyrXk)

## Cómo ejecutar el bot
### Usando docker
```bash
docker run -td --name cyberchatbot -e DISCORD_BOT_APP_TOKEN="INSERT YOUR BOT TOKEN HERE" -e OPENAI_API_KEY="INSERT YOUR OPENAI API KEY HERE" simeononsecurity/discord-typecast-gpt-chatbot:latest
```
### Cómo ejecutar el bot manualmente usando python

Para empezar a ejecutar este repositorio, necesitas realizar los siguientes pasos:

1. Clone este repositorio y cambie a la raíz del producto

```bash
git clone URL
cd repo_name
```
2. crear un `.env` en la raíz del proyecto (será `.gitignored` y pega tu discord bot token y openai token:

```env
DISCORD_BOT_APP_TOKEN=PASTE_DISCORD_TOKEN_HERE
OPENAI_API_KEY=PASTE_OPENAI_API_TOKEN_HERE
```

3. Cree un nuevo entorno virtual utilizando `venv`
```bash
python3 -m venv venv
```

4. Active el entorno virtual:
```bash
source venv/bin/activate
```

5. Instale las dependencias enumeradas en `requirements.txt`
   
```bash
pip install -r requirements.txt
```

6. Si instala nuevas dependencias con `pip install` asegúrese de regenerar requirements.txt con:

```bash
pip freeze > requirements.txt
```
#### Cómo solucionar el problema de las configuraciones regionales
```bash
sudo apt-get install locales -y
sudo locale-gen en_US.UTF-8 en_CA.UTF-8
sudo update-locale
```

## Arquitectura

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
