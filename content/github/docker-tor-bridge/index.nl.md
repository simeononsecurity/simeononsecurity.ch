---
title: "Hoe een Docker Tor Bridge Image maken en uitvoeren voor verbeterde privacy en anonimiteit"
date: 2022-07-06
toc: true
draft: false
description: "Leer hoe je een Docker Tor Bridge image maakt en draait om je online privacy en anonimiteit te verbeteren."
tags: ["Docker Tor Brug", "privacy", "anonimiteit", "docker image", "torrc.default", "docker bouwen", "dokterscontainer", "huidige IP", "tor sokken proxy", "online beveiliging", "verbeterde privacy", "netwerken", "dockerization", "containerisatie", "Docker handleiding", "IP-adres", "netwerkprivacy", "proxyserver", "netwerk anonimiteit", "Docker netwerken", "Tor netwerk", "cyberbeveiliging", "internetprivacy", "anoniem browsen", "Dockerfile", "webbeveiliging", "netwerkbeveiliging", "cyberdefensie", "Docker inzet", "gegevensprivacy"]
---

[![Docker Image CI](https://github.com/simeononsecurity/docker-tor-bridge/actions/workflows/docker-image.yml/badge.svg)](https://github.com/simeononsecurity/docker-tor-bridge/actions/workflows/docker-image.yml)[![VirusTotal Scan](https://github.com/simeononsecurity/docker-tor-bridge/actions/workflows/virustotal.yml/badge.svg)](https://github.com/simeononsecurity/docker-tor-bridge/actions/workflows/virustotal.yml)

## MAAK EEN TORRC.DEFAULT
Bestand: /torrc.default

Het enige wat u moet veranderen van de standaard torrc is de volgende regel:

```SocksPort 0.0.0.0:9050```

## BOUW HET DOCKER IMAGE
Voer het volgende commando uit om het docker image te bouwen.

```bash
docker build -t simeononsecurity/docker-tor-bridge .
```

 
## DRAAI DE DOCKER CONTAINER
```docker
docker run -d \
--restart always \
-p 9050:9050 \
--name torproxy \
simeononsecurity/docker-tor-bridge:latest
``` 

## TEST
Krijg je huidige ip

```curl -L http://ifconfig.me```

Krijg je ip via de tor socks proxy

```curl --socks5 http://localhost:9050 -L http://ifconfig.me```
 
