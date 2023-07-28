---
title: "如何创建和运行 Docker Tor Bridge 映像以增强隐私性和匿名性"
date: 2022-07-06
toc: true
draft: false
description: "了解如何创建和运行 Docker Tor Bridge 镜像，以改善您的在线隐私和匿名性。"
tags: ["Docker Tor 桥接器", "隐私", "匿名性", "docker 映像", "torrc.default", "docker 构建", "docker 容器", "当前IP", "tor socks 代理", "在线安全", "增强隐私", "网络", "对接", "容器化", "Docker 教程", "IP 地址", "网络隐私", "代理服务器", "网络匿名性", "Docker 网络", "Tor 网络", "网络安全", "网络隐私", "匿名浏览", "Dockerfile", "网络安全", "网络保护", "网络防御", "Docker 部署", "数据隐私"]
---

[![Docker Image CI](https://github.com/simeononsecurity/docker-tor-bridge/actions/workflows/docker-image.yml/badge.svg)](https://github.com/simeononsecurity/docker-tor-bridge/actions/workflows/docker-image.yml)[![VirusTotal Scan](https://github.com/simeononsecurity/docker-tor-bridge/actions/workflows/virustotal.yml/badge.svg)](https://github.com/simeononsecurity/docker-tor-bridge/actions/workflows/virustotal.yml)

## 创建 torrc.default
文件： /torrc.default

与默认 torrc 相比，唯一需要更改的是以下一行：

```SocksPort 0.0.0.0:9050```

## 构建 docker 镜像
运行以下命令来构建 docker 镜像。

```bash
docker build -t simeononsecurity/docker-tor-bridge .
```

 
## 运行 docker 容器
```docker
docker run -d \
--restart always \
-p 9050:9050 \
--name torproxy \
simeononsecurity/docker-tor-bridge:latest
```

## 测试
获取您当前的 IP 地址

```curl -L http://ifconfig.me```

通过 tor socks 代理获取您的 IP 地址

```curl --socks5 http://localhost:9050 -L http://ifconfig.me```
 
