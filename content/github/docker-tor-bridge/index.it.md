---
title: "Come creare ed eseguire un'immagine Docker Tor Bridge per migliorare la privacy e l'anonimato"
date: 2022-07-06
toc: true
draft: false
description: "Imparate a creare ed eseguire un'immagine Docker Tor Bridge per migliorare la vostra privacy e il vostro anonimato online."
tags: ["Ponte Docker Tor", "privacy", "anonimato", "immagine docker", "torrc.default", "costruire con docker", "contenitore docker", "IP corrente", "tor socks proxy", "sicurezza online", "privacy migliorata", "rete", "dockerizzazione", "containerizzazione", "Docker tutorial", "Indirizzo IP", "privacy di rete", "server proxy", "anonimato in rete", "Rete Docker", "Rete Tor", "sicurezza informatica", "privacy in internet", "navigazione anonima", "Profilo Docker", "sicurezza web", "protezione della rete", "difesa informatica", "Distribuzione Docker", "data privacy"]
---

[![Docker Image CI](https://github.com/simeononsecurity/docker-tor-bridge/actions/workflows/docker-image.yml/badge.svg)](https://github.com/simeononsecurity/docker-tor-bridge/actions/workflows/docker-image.yml)[![VirusTotal Scan](https://github.com/simeononsecurity/docker-tor-bridge/actions/workflows/virustotal.yml/badge.svg)](https://github.com/simeononsecurity/docker-tor-bridge/actions/workflows/virustotal.yml)

## CREARE UN FILE TORRC.DEFAULT
File: /torrc.default

L'unica cosa da cambiare rispetto al torrc predefinito è la riga seguente:

```SocksPort 0.0.0.0:9050```

## COSTRUIRE L'IMMAGINE DOCKER
Eseguire il seguente comando per creare l'immagine docker.

```bash
docker build -t simeononsecurity/docker-tor-bridge .
```

 
## ESEGUIRE IL CONTENITORE DOCKER
```docker
docker run -d \
--restart always \
-p 9050:9050 \
--name torproxy \
simeononsecurity/docker-tor-bridge:latest
``` 

## TEST
Ottenere l'ip corrente

```curl -L http://ifconfig.me```

Ottenere l'ip attraverso il proxy tor socks

```curl --socks5 http://localhost:9050 -L http://ifconfig.me```
 
