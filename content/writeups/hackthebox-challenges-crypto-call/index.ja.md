---
title: "HackTheBox - チャレンジ - 暗号化 - 通話"
date: 2020-10-07
draft: false
description: "HackTheBox の Crypto - Call チャレンジを解決するために、素数暗号を使用して DTMF トーンを復号する方法を学びます。"
tags: ["ハックザボックス", "クリプトチャレンジ", "DTMF トーン", "素数暗号", "復号化", "パズルを解く", "暗号化", "オーディオ変換", "ダイヤルABC", "デコード.fr", "WAV", "MP3", "周波数", "数学的特性", "国旗", "大胆さ", "ソニックビジュアライザー", "数字", "現金自動預け払い機メニュー", "公衆電話"]
toc: true
cover: "/img/cover/A_cartoon_phone_with_a_green_screen_and_a_padlock_on_it.png"
coverAlt: "緑色の画面と南京錠が付いた漫画の電話。セキュリティと暗号化を象徴し、背景に DTMF トーンが描かれています。"
coverCaption: ""
---

sound.mp3 ファイル内の DTMF トーンをデコードして、HackTheBox の Crypto - Call チャレンジを解決します。ファイルを .wav に変換し、DialABC を使用して暗号テキストを取得します。数字を区切って、Decode.fr の素数暗号を使用してフラグを明らかにします。 HackTheBox のこのエキサイティングなチャレンジで、素数暗号のスキルを試す準備をしてください。」

______

## 提供されるファイル:

1 つのファイルが提供されます。
- サウンド.mp3

## ウォークスルー:

**sound.mp3** を再生すると、聞き覚えのある音が聞こえます。よく知らない方のために説明すると、聞こえている音は **DTMF** (デュアル トーン マルチ周波数) トーンのように聞こえます。公衆電話にダイヤルするときや現金自動預け払い機のメニューを利用するときに聞いていたのと同じトーンです。

各トーンには特定の周波数があります。数字を手動で取得することもできますが、そんな時間がある人はいないでしょう。[DialABC](http://www.dialabc.com/sound/detect/index.html) has a great tool for this, but doesn't support mp3 files. First, you'll have to convert it to .wav with this [tool](https://online-audio-converter.com/)

変換されたファイルを次の場所に持っていきます[DialABC](http://www.dialabc.com/sound/detect/index.html) 次の出力が得られます。
```
2331434783711923431767372331117714113
```
 
Take notice that if you listen to the audio file carefully or open it in **Audacity** or **Sonic Visualizer** that, with one exception, the numbers are paired in groups of two.
If you separate out the number you get the following:
```
23 31 43 47 83 71 19 23 43 17 67 37 23 31 11 7 71 41 13
```

Organized like this, you might be confused and think that it might be HEX. It isn't.  
Pay close attention to the numbers. What mathematical trait do each grouping of numbers share?....
They are all prime numbers. Which should bring you to try the lesser known **prime number cipher**.

We'll use [Decode.fr](https://www.dcode.fr/prime-numbers-cipher) to complete this challenge.   
Submit the cipher text from before we separated it out and you'll get the flag.
```
2331434783711923431767372331117714113
```

______

### Flag Example:
```
HTB{xxxxxxxxxxxxxxxxxxx}
```