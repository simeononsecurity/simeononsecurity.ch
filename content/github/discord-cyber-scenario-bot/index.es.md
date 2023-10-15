---
title: "Discord Cyber Scenario Bot: mejorar la formación y la concienciación sobre ciberseguridad"
date: 2023-02-22
toc: true
draft: false
description: "Descubra cómo el CyberScenarioBot puede elevar su programa de formación y concienciación sobre ciberseguridad en Discord, ofreciendo cuestionarios, escenarios, seguimiento de tablas de clasificación y potentes comandos de herramientas."
tags: ["Bot de discordia", "formación en ciberseguridad", "concienciación sobre ciberseguridad", "scenario bot", "bot de preguntas", "tabla de clasificación", "comandos de herramientas", "Docker", "Python", "pruebas automatizadas", "API de discordia", "documentación para desarrolladores", "Contribución", "Licencia MIT", "CyberScenarioBot", "Cibersentinelas", "mejorar la formación", "programa de sensibilización", "escenarios de ciberseguridad", "entorno de servidor", "comandos personalizados", "desplegar y gestionar", "cuestionarios y escenarios", "comandos de herramientas", "comandos informativos", "cuestiones y contribuciones", "Aplicación Discord para desarrolladores", "Documentación de Discord.py", "trabajar con desarrolladores", "servidor Discord de la comunidad"]
---


**CyberScenarioBot**

Discord Cyber Scenario, Quiz, Y Cyber Awareness Training Bot.

Puede saltar a [🚀 Quick Start](#quick-start) añadir `CyberScenarioBot` a su servidor ahora.

[![Docker Image CI](https://github.com/simeononsecurity/discord-cyber-scenario-bot/actions/workflows/docker-image.yml/badge.svg)](https://github.com/simeononsecurity/discord-cyber-scenario-bot/actions/workflows/docker-image.yml)

## Introducción

Este bot puede ser útil en un programa de formación o concienciación sobre ciberseguridad, donde los usuarios pueden ser expuestos a varios escenarios de ciberseguridad y aprender cómo prevenirlos o responder a ellos. Mediante el uso de un bot Discord, los escenarios pueden ser fácilmente compartidos con los usuarios en un entorno de servidor, y el bot puede ser personalizado para incluir comandos adicionales o funcionalidad según sea necesario. Además, el bot puede ejecutarse en un contenedor Docker, lo que facilita su despliegue y gestión en diversos entornos.

[See the bot in action](https://discord.gg/CYVe2CyrXk)

## 🚀 Inicio rápido

### Cómo ejecutar:
#### Python:
Suponiendo que estás utilizando un sistema basado en Unix, abre un terminal y navega hasta el directorio donde se encuentra el script bot.py. A continuación, ejecute el siguiente comando:
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
Tenga en cuenta que si está utilizando un sistema basado en Windows, tendrá que utilizar un comando ligeramente diferente para establecer la variable de entorno. Aquí tienes un ejemplo de comando que debería funcionar en Windows:
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
#### Docker:
Al ejecutar el contenedor Docker, puede pasar la variable de entorno BOT_TOKEN utilizando la bandera -e de la siguiente manera:

```bash
docker run -e BOT_TOKEN="INSERT YOUR BOT TOKEN HERE" -it --rm simeononsecurity/discord-cyber-scenario-bot:latest
```

Para ejecutar el bot en segundo plano:
```bash
docker run -td --name scenario-bot -e BOT_TOKEN="INSERT YOUR BOT TOKEN HERE" simeononsecurity/discord-cyber-scenario-bot:latest
```

Para ejecutar el bot en segundo plano con todos los avisos y roles programados:
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

## Features
### **Comandos disponibles**
*Prefijo del comando: '!', '/'*****

### 📝 **Comandos para pruebas y escenarios**
- **Aplus**: Responde con el prompt relacionado con A+ de CompTIA.
- **Bluescenario**: Responde con un escenario del equipo azul.
- CCNA**: Responde con la pregunta de opción múltiple CCNA de Cisco.
- CEH**: Responde con la opción múltiple CEH de EC-Council.
- **CISSP**: Responde a la pregunta de opción múltiple CISSP de ISC2.
- Linuxplus**: Responde a la pregunta de opción múltiple Linux+ de CompTIA.
- Netplus**: Responde con la pregunta relacionada con Network+ de CompTIA.
- **Cuestionario**: Responde con una pregunta aleatoria de concientización de seguridad cibernética.
- **Escenario Rojo**: Responde con un escenario de redteam.
- **Secplus**: Responde con una pregunta relacionada con Security+ de CompTIA.

#### 💯🎯 **Leaderboard**
*Las preguntas de opción múltiple se ponderan dinámicamente de forma similar a los exámenes reales en función de si se responden correcta o incorrectamente*.

- Seguimiento de su progreso en el tiempo y ver cómo se compara con los demás en su servidor *.
- Consulta las puntuaciones de cada categoría del cuestionario y las puntuaciones generales.

### 🛠️ **Comandos de herramientas**
- DNS**: Toma un `domain name` y devuelve registros A, AAAA, NS, TXT, etc.
- Hash**: Devuelve `1 of 4 supported algos` y un `string` y genera el hash correspondiente.
- Ping**: Recibe un `IP address` y devuelve un mensaje de éxito y latencia media o un mensaje de fallo.
- Búsqueda de teléfono**: Toma un `phone number` y emite el portador y la ubicación.
- Shodanip**: Recibe un `IP address` y emite información útil de https://internetdb.shodan.io/.
- Subred**: Toma un `IP address` y un `Subnet Mask` y muestra el rango, las IPs utilizables, la dirección de la puerta de enlace, la dirección de difusión y el número de hosts soportados.
- Whois**: Toma una `domain name` y emite la información whois del dominio.

### ℹ️ **Comandos informativos**
- Comandos**: Responde con este mensaje.
- **Socials**: Responde con las distintas cuentas de redes sociales y sitios web del bot.

### ⚙️ **Fácil Configuración**
- Ver [🚀 Quick Start](#🚀-quick-start)

## Próximas funciones

Estas características tienen fecha prevista de implantación, pero las estamos siguiendo y nos encantaría [contributions](#contributing) para ellos.

- Tablas de clasificación avanzadas, con clasificaciones semanales y mensuales.
- Preguntas y cuestionarios personalizables para satisfacer las necesidades específicas de formación en ciberseguridad.
- Informes y análisis avanzados para seguir el progreso y el rendimiento de los usuarios.

## Uso

CyberScenarioBot ofrece varios comandos y funciones para mejorar su programa de formación y concienciación en ciberseguridad. Estos son algunos casos de uso común:

1. **Cuestionarios y Escenarios**: Utilice el `/quiz` para obtener una pregunta aleatoria sobre ciberseguridad. Utilice comandos como `/aplus` `/netplus` `/secplus` para acceder a solicitudes específicas relacionadas con certificaciones de CompTIA. Utilice comandos como `/bluescenario` y `/redscenario` para obtener los escenarios del equipo azul y del equipo rojo, respectivamente.

2. **Pizarra de líderes**: Realiza un seguimiento del progreso del usuario y compara puntuaciones con otros usuarios de tu servidor respondiendo a las preguntas del cuestionario y de la certificación.

3. **Comandos de herramientas**: Utilice varios comandos de herramientas para realizar tareas relacionadas con DNS, hashing, ping, búsqueda de números de teléfono, búsqueda de IP Shodan, cálculos de subred y búsqueda WHOIS de dominios. Utilice comandos como `/dns` `/hash` `/ping` `/phonelookup` `/shodanip` `/subnet` y `/whois` seguido de los argumentos apropiados.

4. **Comandos informativos**: Utilice el botón `/commands` para obtener una lista de los comandos disponibles. Utiliza el comando `/socials` para obtener información sobre las cuentas de redes sociales y sitios web del bot.

No dudes en explorar y experimentar con los comandos disponibles para mejorar tu formación en ciberseguridad e involucrar a los miembros de tu servidor.

## Temas

Si los usuarios encuentran algún problema o tienen sugerencias de mejora, pueden abrir una incidencia en GitHub para informar de ello. Anima a los usuarios a proporcionar información detallada sobre el problema y los pasos para reproducirlo.

Para abrir una incidencia, siga estos pasos:

1. Vaya a la pestaña Issues (Incidencias) del repositorio GitHub del proyecto: [Issues](https://github.com/CyberSentinels/discord-cyber-scenario-bot/issues)
2. Haga clic en el botón "Nueva edición".
3. Proporcione un título descriptivo y una descripción clara de la incidencia.
4. 4. Incluya todos los registros, capturas de pantalla o fragmentos de código relevantes que le ayuden a solucionar el problema.
5. Envíe la incidencia y espere a que los responsables del proyecto se pongan en contacto con usted.

## Contribuir

Todas las contribuciones son bienvenidas.
Este proyecto fue concebido como un esfuerzo de desarrollo y aprendizaje por parte de [the CyberSentinels club](https://cybersentinels.org) y nos encantará ayudarle a contribuir y responder a cualquier pregunta que pueda tener.

### Automated Python Testing

Este repositorio incluye pruebas automatizadas, puedes ver ejemplos de cómo implementarlas [here](https://github.com/CyberSentinels/penguin-pie)

### API de Discord y documentación para desarrolladores

Para probar cambios e implementar funciones, necesitarás algunas cosas.

- [Discord Developer Application](https://discord.com/developers/applications)
- [Discord Developers Documentation](https://discord.com/developers/docs/intro)
- [Discord.py Documentation](https://discordpy.readthedocs.io/en/stable/)

### Trabajar con los desarrolladores

Puedes discutir los esfuerzos de desarrollo en el servidor discord de la comunidad [here](https://discord.gg/CYVe2CyrXk)
  
## Licencia

[MIT](https://github.com/simeononsecurity/glotta/blob/main/LICENSE)
