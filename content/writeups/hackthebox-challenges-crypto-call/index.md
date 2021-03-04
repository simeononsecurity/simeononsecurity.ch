---
title: "HackTheBox - Challenges - Crypto - Call"
date: 2020-10-07T18:31:06-05:00
draft: false
description: "Writeup - HackTheBox - Challenges - Crypto - Call"
tags: ['HackTheBox', 'Challenges', 'Crypto', 'Call', 'DTMF', 'Prime Numbers']
toc: true
---
# HackTheBox - Challenges - Crypto - Call

## Provided Files:

You are provided one file:
- sound.mp3

## Walk Through:

Playing the **sound.mp3**, you'll hear a familiar sound. If you're not familiar the sounds you're hearing are hearing **DTMF** (dual tone multi frequency) tones. The same tones you used to hear while dialing on a pay phone or while getting through automated teller menus.

Each tone has a specific frequency. You could get the numbers manually, but who has the time for that? [DialABC](http://www.dialabc.com/sound/detect/index.html) has a great tool for this, but doesn't support mp3 files. First, you'll have to convert it to .wav with this [tool](https://online-audio-converter.com/)

Take the converted file to [DialABC](http://www.dialabc.com/sound/detect/index.html) and you'll get the following output:
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

### Flag Example:
```
HTB{xxxxxxxxxxxxxxxxxxx}
```