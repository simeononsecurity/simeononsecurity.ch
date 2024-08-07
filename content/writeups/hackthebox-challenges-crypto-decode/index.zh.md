---
title: "HackTheBox - 挑战 - 加密 - 解码"
date: 2020-10-07
draft: false
description: "了解如何解码 Fernet 和 Malboge 密码以解决 HackTheBox 加密挑战并揭开隐藏的旗帜。"
tags: ["破解盒子", "挑战", "加密货币", "解码", "写上去", "费内特密码", "马尔博格密码", "对称加密", "网络安全", "密码学", "渗透测试", "Python", "安全", "挑战", "周大福", "旗帜", "加密", "解密", "Base64"]
toc: true
cover: "/img/cover/A_cartoon_hacker_standing_next_to_a_large_lock_with_one_hand.png"
coverAlt: "一位卡通黑客站在一把大锁旁边，一只手拿着 Fernet 标志钥匙，另一只手拿着 Malboge 标志钥匙，锁内有一面旗帜"
coverCaption: ""
---

详细了解 HackTheBox 加密解码挑战。给定两串信息，本文将指导您完成解码 Fernet 密码和 Malboge 密码以揭示标志的过程。利用 asecuritysite.com 和 base64decode.org 提供的工具来实现解决方案。

______

## 提供的文件：

在此挑战中，您将获得两串信息。

```
993gmULBNujjrZCDev3W8kAVaLkXiyHhCL3500188bA=
```
和
```
gAAAAABboRUb0FsuiYBk1tsXRDr6KAzU1xrNSUv7grB-G-dAEeyqj99kUebz466I2VcH5xDa5HEc5KkbgTklQ7tm9JCRPlJtRng1Ns3VEvbrk7B835OINfPnRbc-UIOnnCmW3CgMdMtf5wGLN299AZEzxIvuy71WC5d9xJDchyiORycuzCth95-4nTKphlNQQ2ko3DX72RxWeEjwt3mavnFXqcOCkGxUhJYmFltz_6ND56VGTrXZi_CK5xLODOX4sj1GNwN_CrU3sJ0obTdA2wF5OaDZLbA1GBPfK0PDlC9WxoUf85K0tFXKfqbt3c5YqtqfytNG5gTkbDFM2NjE7BveBf1DP9ca8g==
```

## 遍历：

乍一看，这似乎是某种密钥和一些密文。
搜索一圈后，你会发现这是一个Fernet cypher。
[Asecuritysite.com](https://asecuritysite.com/encryption/ferdecode) 有一个很棒的工具可以为您解码。

上述信息中的纯文本为您提供了一个 base64 编码的字符串

```
RCdgTl45OFs8O3tGMlZVNTRRPythcUw6bVxJNmlYJmYkMEBSeFBfdSldeHFwdW5tM3Fwb2htZmUrTGJnZl9eXSNhYFleV1Z6VFNyUVZVTnJMUVBPTkdrS0QsSEFlKERDPDtfPz5+fTVZOTg3dzUuUjJyMC8oJyZKKikoJyYlfHtBeX53djx6eXhxWTZ0c1VUcG9oLnk=
```

要对此进行解码，我们将使用提供的工具 [base64decode.org](https://www.base64decode.org/)

再次解码为您提供以下内容：
```
D'`N^98[<;{F2VU54Q?+aqL:m\I6iX&f$0@RxP_u)]xqpunm3qpohmfe+Lbgf_^]#a`
```

This was a new one for me. But you'll find after some careful research that it is a Malboge cipher.
Decoding it with [this](http://malbolge.doleczek.pl/) tool will give you the flag.

______

### Flag Ex:
```
HTB{x_xxx_xxxx}
```

