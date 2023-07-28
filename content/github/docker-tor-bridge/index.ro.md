---
title: "Cum să creați și să rulați o imagine Docker Tor Bridge pentru confidențialitate și anonimat sporite"
date: 2022-07-06
toc: true
draft: false
description: "Aflați cum să creați și să rulați o imagine Docker Tor Bridge pentru a vă îmbunătăți confidențialitatea și anonimatul online."
tags: ["Podul Docker Tor", "confidențialitate", "anonimat", "imagine docker", "torrc.default", "docker build", "container docker", "IP curent", "tor socks proxy", "securitate online", "confidențialitate sporită", "rețea", "dockerizare", "containerizare", "Tutorial Docker", "Adresa IP", "confidențialitatea rețelei", "server proxy", "anonimatul rețelei", "Rețele Docker", "Rețeaua Tor", "securitate cibernetică", "confidențialitatea pe internet", "navigare anonimă", "Dockerfile", "securitate web", "protecția rețelei", "apărare cibernetică", "Implementarea Docker", "confidențialitatea datelor"]
---

[![Docker Image CI](https://github.com/simeononsecurity/docker-tor-bridge/actions/workflows/docker-image.yml/badge.svg)](https://github.com/simeononsecurity/docker-tor-bridge/actions/workflows/docker-image.yml)[![VirusTotal Scan](https://github.com/simeononsecurity/docker-tor-bridge/actions/workflows/virustotal.yml/badge.svg)](https://github.com/simeononsecurity/docker-tor-bridge/actions/workflows/virustotal.yml)

## CREAȚI UN TORRC.DEFAULT
Fișier: /torrc.default

Singurul lucru care trebuie schimbat față de torrc implicit este următoarea linie:

```SocksPort 0.0.0.0:9050```

## CONSTRUIEȘTE IMAGINEA DOCKER
Rulați următoarea comandă pentru a construi imaginea docker.

```bash
docker build -t simeononsecurity/docker-tor-bridge .
```

 
## RULAȚI CONTAINERUL DOCKER
```docker
docker run -d \
--restart always \
-p 9050:9050 \
--name torproxy \
simeononsecurity/docker-tor-bridge:latest
``` 

## TEST
Obține ip-ul tău curent

```curl -L http://ifconfig.me```

Obțineți ip-ul prin proxy-ul tor socks

```curl --socks5 http://localhost:9050 -L http://ifconfig.me```
 
