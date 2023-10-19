---
title: "HackTheBox - 挑战 - 加密货币 - 银行劫案"
date: 2020-10-07
draft: false
toc: true
description: "Learn how to decode T9/Multitap and Atbash ciphers to solve the Bank Heist challenge on HackTheBox."
tags: ["黑客盒子", "加密", "T9 密码", "多字节密码", "atbash 密码", "网络安全", "译码", "密码", "挑战", "国旗", "网络安全", "黑客行为", "学习", "教程", "密码解码", "解谜", "破译", "密码挑战", "网络安全技能", "在线学习"]
cover: "/img/cover/A_cartoon_vault_door_being_unlocked_with_a_key_revealing.png"
coverAlt: "卡通金库门被一把钥匙打开，露出一个宝箱，背景是日落时分的巴黎城市景观。"
coverCaption: ""
---

破解 HackTheBox 上 "银行劫案 "加密挑战的综合指南。该挑战涉及解码一个 [T9](https://simeononsecurity.ch/articles/introduction-to-t9-cipher/) or [Multitap cipher](https://simeononsecurity.ch/articles/introduction-to-t9-cipher/)使用 Decode.fr 阅读文本，并使用 CyberChef 阅读 atbash 密码文本，从而揭示旗帜。对于有抱负的网络安全专业人士和任何希望提高密码学技能的人来说，这是一本必读书。

## 提供的文件：

本挑战为您提供以下密码文本：

```
444333 99966688 277733 7773323444664 84433 22244474433777, 99966688 277733 666552999. 99966688777 777744277733 666333 84433 443344477778 4447777 44466 99966688777 4466688777733. 84433 5533999 8666 84433 55566622255 4447777 22335556669. 4666 8666 727774447777.

47777888 995559888 4555 47777888 44999988 666555997 : 8555444888477744488866888648833369!!
```

______

## Walk Through：

**很明显，这要么是 T9 密码，要么是 Multitap 密码。
不过，在这种情况下，Multitap 才是密码。 [Decode.fr](https://www.dcode.fr/multitap-abc-cipher)有一个解码工具。

你会得到这个纯文本：
```
IF YOU ARE READING THE CIPHER, YOU ARE OKAY. YOUR SHARE OF THE HEIST IS IN YOUR HOUSE. THE KEY TO THE LOCK IS BELOW, GO TO PARIS GSV XLWV GL GSV HZU OLXP TLIVGRIVNVMGUFMW
```

**你可能会问，最后的垃圾是什么？它实际上是一个atbash密码文本。

```
GSV XLWV GL GSV HZU OLXP TLIVGRIVNVMGUFMW
```


我们将使用 [CyberChef](<https://gchq.github.io/CyberChef-#recipe=Atbash_Cipher()&input=R1NWIFhMV1YgR0wgR1NWIEhaVSBPTFhQIApUTElWR1JJVk5WTUdVRk1X>)再破译一次。然后你就有国旗了。呜呜呜

______

###旗帜示例：

```
HTB{XXXXXXXXXXXXXXXXX}
```
