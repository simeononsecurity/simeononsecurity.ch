---
title: "Cómo crear y ejecutar una imagen Docker Tor Bridge para mejorar la privacidad y el anonimato"
date: 2022-07-06
toc: true
draft: false
description: "Aprenda a crear y ejecutar una imagen Docker Tor Bridge para mejorar su privacidad y anonimato en línea."
tags: ["Puente Docker Tor", "privacidad", "anonimato", "imagen docker", "torrc.default", "construcción docker", "contenedor docker", "IP actual", "tor socks proxy", "seguridad en línea", "mayor privacidad", "red", "dockerización", "contenedorización", "Tutorial de Docker", "Dirección IP", "privacidad de la red", "servidor proxy", "anonimato en la red", "Redes Docker", "Red Tor", "ciberseguridad", "privacidad en internet", "navegación anónima", "Dockerfile", "seguridad web", "protección de la red", "ciberdefensa", "Despliegue de Docker", "privacidad de los datos"]
---

[![Docker Image CI](https://github.com/simeononsecurity/docker-tor-bridge/actions/workflows/docker-image.yml/badge.svg)](https://github.com/simeononsecurity/docker-tor-bridge/actions/workflows/docker-image.yml)[![VirusTotal Scan](https://github.com/simeononsecurity/docker-tor-bridge/actions/workflows/virustotal.yml/badge.svg)](https://github.com/simeononsecurity/docker-tor-bridge/actions/workflows/virustotal.yml)

## CREAR UN TORRC.DEFAULT
Archivo: /torrc.default

Lo único que hay que cambiar del torrc por defecto es la siguiente línea:

```SocksPort 0.0.0.0:9050```

## CONSTRUIR LA IMAGEN DOCKER
Ejecute el siguiente comando para construir la imagen docker.

```bash
docker build -t simeononsecurity/docker-tor-bridge .
```

 
## EJECUTAR EL CONTENEDOR DOCKER
```docker
docker run -d \
--restart always \
-p 9050:9050 \
--name torproxy \
simeononsecurity/docker-tor-bridge:latest
``` 

## TEST
Obtén tu ip actual

```curl -L http://ifconfig.me```

Consigue tu ip a través del proxy tor socks

```curl --socks5 http://localhost:9050 -L http://ifconfig.me```
 
