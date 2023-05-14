---
title: "HackTheBox - 挑战 - 加密货币 - 电话"
date: 2020-10-07
draft: false
description: "了解如何使用素数密码解密 DTMF 音调以解决 HackTheBox 上的加密 - 呼叫挑战。"
tags: ["破解盒子", "加密挑战", "双音多频音", "质数密码", "解密", "解决难题", "密码学", "音频转换", "拨ABC", "解码.fr", "WAV格式", "MP3", "频率", "数学特质", "旗帜", "大胆", "声波展示台", "数字", "自动出纳菜单", "公用电话"]
toc: true
cover: "/img/cover/A_cartoon_phone_with_a_green_screen_and_a_padlock_on_it.png"
coverAlt: "带有绿色屏幕和挂锁的卡通电话，象征着安全和加密，背景中描绘了 DTMF 音调"
coverCaption: ""
---

通过解码 sound.mp3 文件中的 DTMF 音调解决 HackTheBox 上的 Crypto - Call 挑战。将文件转换为 .wav 并使用 DialABC 获取密文。分开数字并使用 Decode.fr 上的素数密码来揭示标志。准备好在 HackTheBox 上这个激动人心的挑战中测试您的素数密码技能。”

______

## 提供的文件：

为您提供了一个文件：
- 声音.mp3

## 遍历：

播放 **sound.mp3**，您会听到熟悉的声音。如果您不熟悉，您听到的声音就是 **DTMF**（双音多频）音调。您以前在拨打公用电话或通过自动柜员机菜单时听到的相同音调。

每个音调都有特定的频率。您可以手动获取数字，但谁有时间这样做呢？[DialABC](http://www.dialabc.com/sound/detect/index.html) has a great tool for this, but doesn't support mp3 files. First, you'll have to convert it to .wav with this [tool](https://online-audio-converter.com/)

将转换后的文件带到[DialABC](http://www.dialabc.com/sound/detect/index.html) 你会得到以下输出：
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