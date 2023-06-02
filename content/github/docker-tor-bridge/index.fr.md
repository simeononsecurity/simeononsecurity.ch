---
title: "Comment créer et exécuter une image Docker Tor Bridge pour améliorer la confidentialité et l'anonymat ?"
date: 2022-07-06
toc: true
draft: false
description: "Apprenez à créer et à exécuter une image Docker Tor Bridge pour améliorer votre confidentialité et votre anonymat en ligne."
tags: ["Pont Docker Tor", "vie privée", "anonymat", "image docker", "torrc.default", "construction de docker", "conteneur docker", "IP actuel", "tor socks proxy", "sécurité en ligne", "une meilleure protection de la vie privée", "la mise en réseau", "dockérisation", "conteneurisation", "Tutoriel Docker", "Adresse IP", "confidentialité des réseaux", "serveur proxy", "anonymat du réseau", "Réseau Docker", "Réseau Tor", "cybersécurité", "internet privacy", "navigation anonyme", "Fichier Docker", "sécurité web", "protection du réseau", "cyberdéfense", "Déploiement Docker", "confidentialité des données"]
---

[![Docker Image CI](https://github.com/simeononsecurity/docker-tor-bridge/actions/workflows/docker-image.yml/badge.svg)](https://github.com/simeononsecurity/docker-tor-bridge/actions/workflows/docker-image.yml)[![VirusTotal Scan](https://github.com/simeononsecurity/docker-tor-bridge/actions/workflows/virustotal.yml/badge.svg)](https://github.com/simeononsecurity/docker-tor-bridge/actions/workflows/virustotal.yml)

## CRÉER UN TORRC.DEFAULT
Fichier : /torrc.default

La seule chose à changer par rapport au torrc par défaut est la ligne suivante :

```SocksPort 0.0.0.0:9050```

## CONSTRUIRE L'IMAGE DOCKER
Exécutez la commande suivante pour construire l'image docker.

```bash
docker build -t simeononsecurity/docker-tor-bridge .
```

 
## EXÉCUTER LE CONTENEUR DOCKER
```docker
docker run -d \
--restart always \
-p 9050:9050 \
--name torproxy \
simeononsecurity/docker-tor-bridge:latest
``` 

## TEST
Obtenir l'adresse IP actuelle

```curl -L http://ifconfig.me```

Obtenez votre adresse IP par le biais du proxy tor socks

```curl --socks5 http://localhost:9050 -L http://ifconfig.me```
 
