---
title: “HackTheBox - 挑战 - 加密货币 - 银行抢劫案”
date: 2020-10-07
draft: false
toc: true
description: "Learn how to decode T9/Multitap and Atbash ciphers to solve the Bank Heist challenge on HackTheBox."
tags: [“破解盒子”，“密码学”，“T9密码”，“多次密码”，“阿特巴什密码”，“网络安全”，“解码”，"密文",“挑战”，“旗帜”，“网络安全”，“黑客”，“学习”，“教程”，“密码解码”，“解谜”，“密码破译”，“密码挑战”，“网络安全技能”，“在线学习”]
cover: "/img/cover/A_cartoon_vault_door_being_unlocked_with_a_key_revealing.png"
coverAlt: “一扇卡通金库门被一把钥匙打开，里面是一个宝箱，所有这些都以巴黎城市景观为背景，落日余晖。”
coverCaption: “”
---

解决 HackTheBox 上的“银行抢劫”加密挑战的综合指南。挑战涉及使用 Decode.fr 解码 T9 或 Multitap 密文，并使用 CyberChef 解码 atbash 密文以显示标志。有抱负的网络安全专业人士和任何希望提高密码学技能的人的必读之作。

## 提供的文件：

对于此挑战，您将获得以下密文：

```
444333 99966688 277733 7773323444664 84433 22244474433777, 99966688 277733 666552999. 99966688777 777744277733 666333 84433 443344477778 4447777 44466 99966688777 4466688777733. 84433 5533999 8666 84433 55566622255 4447777 22335556669. 4666 8666 727774447777.

47777888 995559888 4555 47777888 44999988 666555997 : 8555444888477744488866888648833369!!
```

______

## Walk Through:

**Very clearly, this is either a T9 or Multitap cipher.**  
Multitap is the cipher in this instance though. [Decode.fr](https://www.dcode.fr/multitap-abc-cipher) has a tool to decode this.

You'll get this plain text:
```
IF YOU ARE READING THE CIPHER, YOU ARE OKAY. YOUR SHARE OF THE HEIST IS IN YOUR HOUSE. THE KEY TO THE LOCK IS BELOW, GO TO PARIS GSV XLWV GL GSV HZU OLXP TLIVGRIVNVMGUFMW
```

**What is that junk at the end you might ask? Well it's actually an atbash cipher text.**

```
GSV XLWV GL GSV HZU OLXP TLIVGRIVNVMGUFMW
```


We'll use [CyberChef](<https://gchq.github.io/CyberChef-#recipe=Atbash_Cipher()&input=R1NWIFhMV1YgR0wgR1NWIEhaVSBPTFhQIApUTElWR1JJVk5WTUdVRk1X>) to decipher one more time. Then you have your flag. Whoot!

______

### Flag Example:

```
HTB{XXXXXXXXXXXXXXXXX}
```
