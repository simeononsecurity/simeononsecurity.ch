---
title: "Discord Backdoors and Breaches Bot: Un compañero de juego de estrategia por turnos"
date: 2023-03-10
toc: true
draft: false
description: "Mejora tu experiencia de juego en Backdoors and Breaches con este bot de Discord prealfa, que proporciona comandos para facilitar el juego y la interacción."
tags: ["Bot de discordia", "Puertas traseras y brechas", "juego de estrategia por turnos", "compañero de juego", "comandos de juego", "juego de estrategia bot", "BHIS", "Black Hills InfoSec", "maestro de incidentes", "Equipo C2", "fases del juego", "configuración del juego", "instrucciones de juego", "canal de juegos", "Robot Python", "Bot Docker", "automatización de juegos", "colaboración en juegos", "coordinación de juegos", "juego de ciberseguridad", "seguridad de la información", "desarrollo de juegos", "consejos de juego", "juego multijugador", "roles de juego", "retos del juego", "fases del juego", "configuración del entorno de juego", "bot dockerizado", "Python dependencies"]
---

## Discord Backdoors and Breaches Bot - Pre Alpha

[![Docker Image CI](https://github.com/simeononsecurity/discord-backdoors-and-breaches/actions/workflows/docker-image.yml/badge.svg)](https://github.com/simeononsecurity/discord-backdoors-and-breaches/actions/workflows/docker-image.yml)

<img src="https://github.com/simeononsecurity/discord-backdoors-and-breaches/blob/main/.github/images/bnb-dark.png?raw=true" alt="Logotipo de Backdoors and Breaches" width="200"/>


Un bot de Discord para Backdoors and Breaches, un juego de estrategia por turnos de [BHIS](https://www.blackhillsinfosec.com/projects/backdoorsandbreaches/)

### Comandos disponibles

- `setup-game` Crea un id de juego y establece todas las variables necesarias.
- `start-game` Inicia un nuevo juego se debe ejecutar mi maestro incidente sólo después de `setup-game`
- `join-game` Permite a los jugadores unirse a la partida asignándoles el rol de "Jugador" y dándoles acceso al canal de juego.
- `play-procedure` Inicia la fase de Procedimiento del juego, en la que los jugadores deben completar una serie de desafíos para progresar.
- `play-incident-master` Inicia la fase de Jefe de Incidentes del juego, en la que los jugadores se turnan para ser el Jefe de Incidentes y dirigir a los demás jugadores sobre cómo responder a un incidente simulado.
- `play-c2` Inicia la fase de Mando y Control del juego, en la que los jugadores se turnan para ser el equipo C2 y deben coordinarse con los demás jugadores para completar una serie de tareas.
- `play-persistence` Inicia la fase de Persistencia del juego, en la que los jugadores deben encontrar y eliminar una puerta trasera oculta en el sistema.
- `play-pivot` Inicia la fase Pivot del juego, en la que los jugadores deben pivotar a una parte diferente del sistema y continuar su investigación.
- `end-game` Finaliza la partida actual y borra el canal de juego y los roles asociados.

Para ejecutar un comando, escribe `!` o `/` seguido del nombre del comando en el canal de juego. Por ejemplo, para iniciar una nueva partida, escribe `!start-game` Ten en cuenta que algunos comandos sólo pueden estar disponibles durante ciertas fases del juego.
### Configuración del Bot

#### Usando Python

1. Clona este repositorio usando `git clone https://github.com/simeononsecurity/discord-backdoors-and-breaches.git`
2. Instale las dependencias necesarias mediante `pip install -r requirements.txt`
3. Cree una `config.ini` en el directorio raíz del proyecto con el siguiente contenido:
```ini
[SETTINGS]
discordtoken = put_discord_bot_token_here
channel_id = put_game_channel_id_here
```
4. Sustituir `put_discord_bot_token_here` con tu ficha de bot de Discord y `put_game_channel_id_here` con el ID del canal en el que quieres que se juegue.
5. Ejecuta el bot usando `python main.py`

#### Uso de Docker

1. Clona el repositorio y navega hasta el directorio:
```
git clone https://github.com/simeononsecurity/discord-backdoors-and-breaches.git
cd discord-backdoors-and-breaches
```
2. Crear un `.env` en el directorio raíz del proyecto y añada las siguientes variables de entorno con sus valores correspondientes:
```env
BOT_TOKEN=<discord_bot_token_here>
CHANNEL_ID=<game_channel_id_here>
```
3. Cree la imagen Docker utilizando el archivo Dockerfile proporcionado:
```bash
docker build -t discord-backdoors-and-breaches .
```
4. Ejecute el contenedor Docker, introduciendo las variables de entorno del archivo `.env` archivos:
```bash
docker run --env-file .env discord-backdoors-and-breaches
```

Como alternativa, puede establecer las variables de entorno directamente durante el proceso `docker run` mando:
```bash
docker run -td --name bnbbot -e BOT_TOKEN=<discord_bot_token_here> -e CHANNEL_ID=<game_channel_id_here> discord-backdoors-and-breaches
```
o tire directamente de la imagen en [dockerhub](https://hub.docker.com/r/simeononsecurity/discord-backdoors-and-breaches)
```bash
docker run -td --name bnbbot -e BOT_TOKEN=<discord_bot_token_here> -e CHANNEL_ID=<game_channel_id_here> simeononsecurity/discord-backdoors-and-breaches:latest
```

