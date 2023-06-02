---
title: "How to Create and Run a Docker Tor Bridge Image for Enhanced Privacy and Anonymity"
date: 2022-07-06
toc: true
draft: false
description: "Learn how to create and run a Docker Tor Bridge image to improve your online privacy and anonymity."
tags: ["Docker Tor Bridge", "privacy", "anonymity", "docker image", "torrc.default", "docker build", "docker container", "current IP", "tor socks proxy", "online security", "enhanced privacy", "networking", "dockerization", "containerization", "Docker tutorial", "IP address", "network privacy", "proxy server", "network anonymity", "Docker networking", "Tor network", "cybersecurity", "internet privacy", "anonymous browsing", "Dockerfile", "web security", "network protection", "cyber defense", "Docker deployment", "data privacy"]
---

[![Docker Image CI](https://github.com/simeononsecurity/docker-tor-bridge/actions/workflows/docker-image.yml/badge.svg)](https://github.com/simeononsecurity/docker-tor-bridge/actions/workflows/docker-image.yml)[![VirusTotal Scan](https://github.com/simeononsecurity/docker-tor-bridge/actions/workflows/virustotal.yml/badge.svg)](https://github.com/simeononsecurity/docker-tor-bridge/actions/workflows/virustotal.yml)

## CREATE A TORRC.DEFAULT
File: /torrc.default

The only thing to change from the default torrc is the following line:

```SocksPort 0.0.0.0:9050```

## BUILD THE DOCKER IMAGE
Run the following command to build the docker image.

```bash
docker build -t simeononsecurity/docker-tor-bridge .
```

 
## RUN THE DOCKER CONTAINER
```docker
docker run -d \
--restart always \
-p 9050:9050 \
--name torproxy \
simeononsecurity/docker-tor-bridge:latest
``` 

## TEST
Get your current ip

```curl -L http://ifconfig.me```

Get your ip through the tor socks proxy

```curl --socks5 http://localhost:9050 -L http://ifconfig.me```
 
