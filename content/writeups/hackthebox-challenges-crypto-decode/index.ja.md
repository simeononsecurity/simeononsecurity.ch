---
title: "HackTheBox - チャレンジ - 暗号化 - デコード"
date: 2020-10-07
draft: false
description: "フェルネット暗号とマルボゲ暗号を解読して HackTheBox 暗号チャレンジを解決し、隠されたフラグを明らかにする方法を学びます。"
tags: ["ハックザボックス", "課題", "暗号", "デコード", "書き上げる", "フェルネット暗号", "マルボゲ暗号", "対称暗号化", "サイバーセキュリティ", "暗号化", "侵入テスト", "パイソン", "安全", "チャレンジ", "CTF", "国旗", "暗号化", "復号化", "Base64"]
toc: true
cover: "/img/cover/A_cartoon_hacker_standing_next_to_a_large_lock_with_one_hand.png"
coverAlt: "大きな錠の横に立っている漫画のハッカー。片手でフェルネットのロゴの鍵を持ち、もう一方の手でマルボゲのロゴの鍵を持ち、錠の内側に旗が見える"
coverCaption: ""
---

HackTheBox Crypto Decode チャレンジの詳細なウォークスルーをご覧ください。この記事では、2 つの情報文字列を考慮して、フェルネット暗号とマルボゲ暗号を解読してフラグを明らかにするプロセスを説明します。解決策を達成するには、asecuritysite.com およびbase64decode.org が提供するツールを利用します。

______

## 提供されるファイル:

このチャレンジでは、2 つの情報列が提供されます。

```
993gmULBNujjrZCDev3W8kAVaLkXiyHhCL3500188bA=
```
と
```
gAAAAABboRUb0FsuiYBk1tsXRDr6KAzU1xrNSUv7grB-G-dAEeyqj99kUebz466I2VcH5xDa5HEc5KkbgTklQ7tm9JCRPlJtRng1Ns3VEvbrk7B835OINfPnRbc-UIOnnCmW3CgMdMtf5wGLN299AZEzxIvuy71WC5d9xJDchyiORycuzCth95-4nTKphlNQQ2ko3DX72RxWeEjwt3mavnFXqcOCkGxUhJYmFltz_6ND56VGTrXZi_CK5xLODOX4sj1GNwN_CrU3sJ0obTdA2wF5OaDZLbA1GBPfK0PDlC9WxoUf85K0tFXKfqbt3c5YqtqfytNG5gTkbDFM2NjE7BveBf1DP9ca8g==
```

## ウォークスルー:

一見すると、これはある種の鍵と暗号文であるように見えます。
調べてみると、それはフェルネットの暗号であることがわかります。
[Asecuritysite.com](https://asecuritysite.com/encryption/ferdecode) にはそれをデコードするための優れたツールがあります。

上記の情報のプレーン テキストから、base64 でエンコードされた文字列が得られます。

```
RCdgTl45OFs8O3tGMlZVNTRRPythcUw6bVxJNmlYJmYkMEBSeFBfdSldeHFwdW5tM3Fwb2htZmUrTGJnZl9eXSNhYFleV1Z6VFNyUVZVTnJMUVBPTkdrS0QsSEFlKERDPDtfPz5+fTVZOTg3dzUuUjJyMC8oJyZKKikoJyYlfHtBeX53djx6eXhxWTZ0c1VUcG9oLnk=
```

これをデコードするには、から提供されるツールを使用します。 [base64decode.org](https://www.base64decode.org/)

再度デコードすると次のようになります。
「」
D'`N^98[<;{F2VU54Q?+aqL:m\I6iX&f$0@RxP_u)]xqpunm3qpohmfe+Lbgf_^]#a`
```

This was a new one for me. But you'll find after some careful research that it is a Malboge cipher.
Decoding it with [this](http://malbolge.doleczek.pl/) tool will give you the flag.

______

### Flag Ex:
```
HTB{x_xxx_xxxx}
「」

