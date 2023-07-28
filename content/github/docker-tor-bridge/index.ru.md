---
title: "Как создать и запустить образ моста Docker Tor для повышения уровня конфиденциальности и анонимности"
date: 2022-07-06
toc: true
draft: false
description: "Узнайте, как создать и запустить образ Docker Tor Bridge для повышения уровня конфиденциальности и анонимности в Интернете."
tags: ["Мост Docker Tor", "конфиденциальность", "анонимность", "образ докера", "torrc.default", "сборка в докере", "контейнер docker", "текущий IP", "tor socks proxy", "безопасность в Интернете", "повышенная конфиденциальность", "работа в сети", "Докеризация", "контейнеризация", "Учебное пособие по Docker", "IP-адрес", "конфиденциальность сети", "прокси-сервер", "сетевая анонимность", "Сетевое взаимодействие Docker", "Сеть Tor", "кибербезопасность", "конфиденциальность в интернете", "анонимный просмотр", "Dockerfile", "веб-безопасность", "защита сети", "кибернетическая защита", "Развертывание Docker", "конфиденциальность данных"]
---

[![Docker Image CI](https://github.com/simeononsecurity/docker-tor-bridge/actions/workflows/docker-image.yml/badge.svg)](https://github.com/simeononsecurity/docker-tor-bridge/actions/workflows/docker-image.yml)[![VirusTotal Scan](https://github.com/simeononsecurity/docker-tor-bridge/actions/workflows/virustotal.yml/badge.svg)](https://github.com/simeononsecurity/docker-tor-bridge/actions/workflows/virustotal.yml)

## СОЗДАНИЕ ФАЙЛА TORRC.DEFAULT
Файл: /torrc.default

Единственное, что нужно изменить в torrc по умолчанию, - это следующая строка:

```SocksPort 0.0.0.0:9050```

## СБОРКА ОБРАЗА DOCKER
Выполните следующую команду для сборки образа docker.

```bash
docker build -t simeononsecurity/docker-tor-bridge .
```

 
## ЗАПУСТИТЬ КОНТЕЙНЕР DOCKER
```docker
docker run -d \
--restart always \
-p 9050:9050 \
--name torproxy \
simeononsecurity/docker-tor-bridge:latest
``` 

## TEST
Получение текущего ip

```curl -L http://ifconfig.me```

Получение своего ip через прокси tor socks

```curl --socks5 http://localhost:9050 -L http://ifconfig.me```
 
