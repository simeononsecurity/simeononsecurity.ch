---
title: "HackTheBox - 挑战 - 加密货币 - 银行抢劫"
date: 2020-10-07
draft: false
toc: true
description: "Learn how to decode T9/Multitap and Atbash ciphers to solve the Bank Heist challenge on HackTheBox."
tags: ["破解盒子", "密码学", "T9密码", "多次密码", "阿特巴什密码", "网络安全", "解码", "密文", "挑战", "旗帜", "网络安全", "骇客", "学习", "教程", "密码解码", "解谜", "密码破译", "密码挑战", "网络安全技能", "在线学习"]
cover: "/img/cover/A_cartoon_vault_door_being_unlocked_with_a_key_revealing.png"
coverAlt: "用钥匙打开的卡通金库门露出一个宝箱，所有这些都以日落时分的巴黎城市景观为背景。"
coverCaption: ""
---

解决 HackTheBox 上的“银行抢劫”加密挑战的综合指南。挑战涉及使用 Decode.fr 解码 T9 或 Multitap 密文，并使用 CyberChef 解码 atbash 密文以显示标志。有抱负的网络安全专业人士和任何希望提高密码学技能的人的必读之作。

## 提供的文件：

对于此挑战，您将获得以下密文：

```
444333 99966688 277733 7773323444664 84433 22244474433777, 99966688 277733 666552999. 99966688777 777744277733 666333 84433 443344477778 4447777 44466 99966688777 4466688777733. 84433 5533999 8666 84433 55566622255 4447777 22335556669. 4666 8666 727774447777.

47777888 995559888 4555 47777888 44999988 666555997 : 8555444888477744488866888648833369!!
```

______

## 遍历：

**很明显，这是 T9 或多抽头密码。**
不过，在这种情况下，多次击键是密码。 [Decode.fr](https://www.dcode.fr/multitap-abc-cipher) 有一个工具来解码这个。

你会得到这个纯文本：
```
IF YOU ARE READING THE CIPHER, YOU ARE OKAY. YOUR SHARE OF THE HEIST IS IN YOUR HOUSE. THE KEY TO THE LOCK IS BELOW, GO TO PARIS GSV XLWV GL GSV HZU OLXP TLIVGRIVNVMGUFMW
```

**你可能会问最后那个垃圾是什么？好吧，它实际上是一个 atbash 密文。**

```
GSV XLWV GL GSV HZU OLXP TLIVGRIVNVMGUFMW
```


我们将使用 [CyberChef](<https://gchq.github.io/CyberChef-#recipe=Atbash_Cipher()&input=R1NWIFhMV1YgR0wgR1NWIEhaVSBPTFhQIApUTElWR1JJVk5WTUdVRk1X>) 再破译一次。然后你就有了你的旗帜。哇！

______

### 标志示例：

```
HTB{XXXXXXXXXXXXXXXXX}
```
