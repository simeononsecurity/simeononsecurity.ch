---
title: "HackTheBox - チャレンジ - 暗号化 - 通話"
date: 2020-10-07
draft: false
description: "HackTheBox の Crypto - Call チャレンジを解決するために、素数暗号を使用して DTMF トーンを復号する方法を学びます。"
tags: ["ハックザボックス", "クリプトチャレンジ", "DTMF トーン", "素数暗号", "復号化", "パズルを解く", "暗号化", "オーディオ変換", "ダイヤルABC", "デコード.fr", "WAV", "MP3", "周波数", "数学的特性", "国旗", "大胆さ", "ソニックビジュアライザー", "数字", "現金自動預け払い機メニュー", "公衆電話"]
toc: true
cover: "/img/cover/A_cartoon_phone_with_a_green_screen_and_a_padlock_on_it.png"
coverAlt: "背景に DTMF トーンが描かれた、セキュリティと暗号化を象徴する緑色の画面と南京錠が付いた漫画の電話"
coverCaption: ""
---

sound.mp3 ファイル内の DTMF トーンをデコードして、HackTheBox の Crypto - Call チャレンジを解決します。ファイルを .wav に変換し、DialABC を使用して暗号テキストを取得します。数字を区切って、Decode.fr の素数暗号を使用してフラグを明らかにします。 HackTheBox のこのエキサイティングなチャレンジで、素数暗号のスキルを試す準備をしてください。」

______

## 提供されるファイル:

1 つのファイルが提供されます。
- サウンド.mp3

## ウォークスルー:

**sound.mp3** を再生すると、聞き覚えのある音が聞こえます。よく知らない方のために説明すると、聞こえている音は **DTMF** (デュアル トーン マルチ周波数) トーンのように聞こえます。公衆電話にダイヤルするときや現金自動預け払い機のメニューを利用するときに聞いていたのと同じトーンです。

各トーンには特定の周波数があります。数字を手動で取得することもできますが、そんな時間がある人はいないでしょう。 [DialABC](http://www.dialabc.com/sound/detect/index.html) has a great tool for this, but doesn't support mp3 files. First, you'll have to convert it to .wav with this [tool](https://online-audio-converter.com/)

変換されたファイルを次の場所に持っていきます [DialABC](http://www.dialabc.com/sound/detect/index.html) 次の出力が得られます。
```
2331434783711923431767372331117714113
```
 
オーディオ ファイルを注意深く聞くか、**Audacity** または **Sonic Visualizer** で開くと、1 つの例外を除いて、数字が 2 つのグループでペアになっていることに注意してください。
数値を分解すると次のようになります。
```
23 31 43 47 83 71 19 23 43 17 67 37 23 31 11 7 71 41 13
```

このように整理すると、「HEX ではないか」と混乱してしまうかもしれません。そうではありません。
数字に細心の注意を払ってください。数字の各グループにはどのような数学的特徴がありますか?....
それらはすべて素数です。これにより、あまり知られていない **素数暗号**を試すことができます。

使用します [Decode.fr](https://www.dcode.fr/prime-numbers-cipher) このチャレンジを完了するには。
分離前の暗号文を送信するとフラグを取得できます。
```
2331434783711923431767372331117714113
```

______

### フラグの例:
```
HTB{xxxxxxxxxxxxxxxxxxx}
```