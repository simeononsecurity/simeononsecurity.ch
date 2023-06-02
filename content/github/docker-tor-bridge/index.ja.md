---
title: "プライバシーと匿名性を強化するDocker Tor Bridgeイメージの作成と実行方法"
date: 2022-07-06
toc: true
draft: false
description: "オンラインプライバシーと匿名性を向上させるためのDocker Tor Bridgeイメージの作成と実行方法について説明します。"
tags: ["Docker Torブリッジ", "プライバシー", "匿名性", "ドッカーイメージ", "torrc.default", "ドッカービルド", "ドッカーコンテナ", "カレントIP", "トルソックスプロキシ", "オンラインセキュリティ", "エンハンストプライバシー", "ネットワーキング", "ドッカライゼーション", "コンテナリゼーション", "Dockerチュートリアル", "IPアドレス", "ネットワークプライバシー", "プロキシサーバー", "ネットワークアノニマス", "Dockerネットワーキング", "トーアネットワーク", "サイバーセキュリティ", "インターネットプライバシー", "えんかくブラウズ", "Dockerfile（ドッカーファイル", "ウェブセキュリティ", "ネットワークプロテクション", "サイバーディフェンス", "Dockerのデプロイメント", "データプライバシー"]
---

[![Docker Image CI](https://github.com/simeononsecurity/docker-tor-bridge/actions/workflows/docker-image.yml/badge.svg)](https://github.com/simeononsecurity/docker-tor-bridge/actions/workflows/docker-image.yml)[![VirusTotal Scan](https://github.com/simeononsecurity/docker-tor-bridge/actions/workflows/virustotal.yml/badge.svg)](https://github.com/simeononsecurity/docker-tor-bridge/actions/workflows/virustotal.yml)

## torrc.defaultを作成する
ファイル：/torrc.default

デフォルトのtorrcから変更するのは、以下の行だけです：

```SocksPort 0.0.0.0:9050```

## dockerイメージの構築
以下のコマンドを実行し、dockerイメージをビルドします。

```bash
docker build -t simeononsecurity/docker-tor-bridge .
```

 
## dockerコンテナを実行する
```docker
docker run -d \
--restart always \
-p 9050:9050 \
--name torproxy \
simeononsecurity/docker-tor-bridge:latest
```

## TEST
現在のIPを取得する

```curl -L http://ifconfig.me```

tor socksプロキシで自分のIPを取得する

```curl --socks5 http://localhost:9050 -L http://ifconfig.me```
 
