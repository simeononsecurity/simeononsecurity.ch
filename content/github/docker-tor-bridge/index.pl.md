---
title: "Jak utworzyć i uruchomić obraz Docker Tor Bridge w celu zwiększenia prywatności i anonimowości"
date: 2022-07-06
toc: true
draft: false
description: "Dowiedz się, jak utworzyć i uruchomić obraz Docker Tor Bridge, aby poprawić swoją prywatność i anonimowość w Internecie."
tags: ["Docker Tor Bridge", "prywatność", "anonymity", "obraz docker", "torrc.default", "kompilacja docker", "kontener docker", "bieżący adres IP", "tor socks proxy", "bezpieczeństwo online", "Zwiększona prywatność", "networking", "dokowanie", "konteneryzacja", "Samouczek Docker", "Adres IP", "prywatność sieci", "serwer proxy", "anonimowość sieci", "Sieć Docker", "Sieć Tor", "cyberbezpieczeństwo", "prywatność w internecie", "anonimowe przeglądanie", "Plik Docker", "bezpieczeństwo sieci", "ochrona sieci", "cyberobrona", "Wdrożenie Docker", "prywatność danych"]
---

[![Docker Image CI](https://github.com/simeononsecurity/docker-tor-bridge/actions/workflows/docker-image.yml/badge.svg)](https://github.com/simeononsecurity/docker-tor-bridge/actions/workflows/docker-image.yml)[![VirusTotal Scan](https://github.com/simeononsecurity/docker-tor-bridge/actions/workflows/virustotal.yml/badge.svg)](https://github.com/simeononsecurity/docker-tor-bridge/actions/workflows/virustotal.yml)

## UTWÓRZ TORRC.DEFAULT
Plik: /torrc.default

Jedyną rzeczą, którą należy zmienić w domyślnym pliku torrc, jest następująca linia:

```SocksPort 0.0.0.0:9050```

## BUILD THE DOCKER IMAGE
Uruchom następujące polecenie, aby zbudować obraz docker.

```bash
docker build -t simeononsecurity/docker-tor-bridge .
```

 
## URUCHOMIĆ KONTENER DOCKER
```docker
docker run -d \
--restart always \
-p 9050:9050 \
--name torproxy \
simeononsecurity/docker-tor-bridge:latest
``` 

## TEST
Pobierz aktualny adres IP

```curl -L http://ifconfig.me```

Uzyskaj swój adres IP przez serwer proxy tor socks

```curl --socks5 http://localhost:9050 -L http://ifconfig.me```
 
