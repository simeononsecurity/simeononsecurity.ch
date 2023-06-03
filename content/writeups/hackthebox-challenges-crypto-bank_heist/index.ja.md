---
title: "HackTheBox - Challenges - Crypto - Bank Heist"
date: 2020-10-07
draft: false
toc: true
description: "Learn how to decode T9/Multitap and Atbash ciphers to solve the Bank Heist challenge on HackTheBox."
tags: ["ハックザボックス", "あんごうぎじゅつ", "ティーナイン暗号", "マルチタップサイファー", "アットバッシュサイファー", "サイバーセキュリティ", "デコード", "暗号文", "挑戦", "フラグ", "サイバーセキュリティ", "ハッキング", "学ぶ", "チュートリアル", "ふごうあんごうか", "謎解き", "コードブレーキング", "あんごうチャレンジ", "サイバーセキュリティスキル", "オンライン学習"]
cover: "/img/cover/A_cartoon_vault_door_being_unlocked_with_a_key_revealing.png"
coverAlt: "夕暮れ時のパリの街並みを背景に、金庫の扉を鍵で開けると宝箱が出てくるという漫画のようなストーリーです。"
coverCaption: ""
---

HackTheBoxのCryptoチャレンジ「Bank Heist」を解くための包括的なガイドです。このチャレンジでは、暗号を解読するために [T9](https://simeononsecurity.ch/articles/introduction-to-t9-cipher/) or [Multitap cipher](https://simeononsecurity.ch/articles/introduction-to-t9-cipher/)Decode.frを使ったテキストとCyberChefを使ったatbashの暗号テキストからフラグを明らかにする。サイバーセキュリティのプロを目指す人、暗号技術のスキルアップを目指す人は必読の書です。

## Provided Files：

この課題では、以下の暗号テキストが提供されます：

```
444333 99966688 277733 7773323444664 84433 22244474433777, 99966688 277733 666552999. 99966688777 777744277733 666333 84433 443344477778 4447777 44466 99966688777 4466688777733. 84433 5533999 8666 84433 55566622255 4447777 22335556669. 4666 8666 727774447777.

47777888 995559888 4555 47777888 44999988 666555997 : 8555444888477744488866888648833369!!
```

______

## ウォークスルー

**これはT9かMultitapのどちらかの暗号です。
しかし、この例ではMultitapが暗号である。 [Decode.fr](https://www.dcode.fr/multitap-abc-cipher)は、これを解読するツールがあります。

このプレーンテキストが得られます：
```
IF YOU ARE READING THE CIPHER, YOU ARE OKAY. YOUR SHARE OF THE HEIST IS IN YOUR HOUSE. THE KEY TO THE LOCK IS BELOW, GO TO PARIS GSV XLWV GL GSV HZU OLXP TLIVGRIVNVMGUFMW
```

**最後に出てくるゴミは何なのか？実はこれ、アットバッシュの暗号文なんです。

```
GSV XLWV GL GSV HZU OLXP TLIVGRIVNVMGUFMW
```


を使うことにします。 [CyberChef](<https://gchq.github.io/CyberChef-#recipe=Atbash_Cipher()&input=R1NWIFhMV1YgR0wgR1NWIEhaVSBPTFhQIApUTElWR1JJVk5WTUdVRk1X>)をもう一回読み解く。そして、あなたの旗が出来ました。フート！

______

### 旗の例です：

```
HTB{XXXXXXXXXXXXXXXXX}
```
