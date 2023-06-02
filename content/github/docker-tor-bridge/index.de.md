---
title: "Wie man ein Docker-Tor-Bridge-Image für mehr Privatsphäre und Anonymität erstellt und betreibt"
date: 2022-07-06
toc: true
draft: false
description: "Erfahren Sie, wie Sie ein Docker Tor Bridge-Image erstellen und ausführen, um Ihre Online-Privatsphäre und Anonymität zu verbessern."
tags: ["Docker-Tor-Brücke", "Datenschutz", "Anonymität", "Docker-Image", "torrc.default", "Docker bauen", "Docker-Container", "aktuelle IP", "Tor-Socken-Proxy", "Online-Sicherheit", "verbesserte Privatsphäre", "Vernetzung", "Dockerisierung", "Containerisierung", "Docker-Tutorial", "IP-Adresse", "Datenschutz im Netz", "Proxyserver", "Netzanonymität", "Docker-Vernetzung", "Tor-Netzwerk", "Cybersicherheit", "Internetprivatsphäre", "anonymes Surfen", "Dockerdatei", "Web-Sicherheit", "Netzwerkschutz", "Cyber-Abwehr", "Docker-Bereitstellung", "Datenschutz"]
---

[![Docker Image CI](https://github.com/simeononsecurity/docker-tor-bridge/actions/workflows/docker-image.yml/badge.svg)](https://github.com/simeononsecurity/docker-tor-bridge/actions/workflows/docker-image.yml)[![VirusTotal Scan](https://github.com/simeononsecurity/docker-tor-bridge/actions/workflows/virustotal.yml/badge.svg)](https://github.com/simeononsecurity/docker-tor-bridge/actions/workflows/virustotal.yml)

## ERSTELLEN EINER TORRC.DEFAULT
Datei: /torrc.default

Das Einzige, was gegenüber der Standard-Torrc geändert werden muss, ist die folgende Zeile:

```SocksPort 0.0.0.0:9050```

## DAS DOCKER-IMAGE ERSTELLEN
Führen Sie den folgenden Befehl aus, um das Docker-Image zu erstellen.

```bash
docker build -t simeononsecurity/docker-tor-bridge .
```

 
## DEN DOCKER-CONTAINER AUSFÜHREN
```docker
docker run -d \
--restart always \
-p 9050:9050 \
--name torproxy \
simeononsecurity/docker-tor-bridge:latest
``` 

## TEST
Abfrage der aktuellen IP

```curl -L http://ifconfig.me```

Erhalte deine IP durch den Tor-Socken-Proxy

```curl --socks5 http://localhost:9050 -L http://ifconfig.me```
 
