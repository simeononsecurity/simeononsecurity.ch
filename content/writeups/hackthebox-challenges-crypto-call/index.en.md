---
title: "HackTheBox - Challenges - Crypto - Call"
date: 2020-10-07
draft: false
description: "Learn how to decrypt DTMF tones using prime number cipher to solve the Crypto - Call challenge on HackTheBox."
tags: ["HackTheBox", "Crypto Challenge", "DTMF Tones", "Prime Number Cipher", "Decryption", "Solving Puzzles", "Cryptography", "Audio Conversion", "DialABC", "Decode.fr", "WAV", "MP3", "Frequency", "Mathematical Trait", "Flag", "Audacity", "Sonic Visualizer", "Numbers", "Automated Teller Menus", "Pay Phone"]
toc: true
cover: "/img/cover/A_cartoon_phone_with_a_green_screen_and_a_padlock_on_it.png"
coverAlt: "A cartoon phone with a green screen and a padlock on it, symbolizing security and encryption, with DTMF tones depicted in the backgroun"
coverCaption: ""
---

Solve the Crypto - Call challenge on HackTheBox by decoding the DTMF tones in the sound.mp3 file. Convert the file to .wav and use DialABC to get the cipher text. Separate the numbers and use the prime number cipher on Decode.fr to reveal the flag. Get ready to put your skills in prime number cipher to the test in this exciting challenge on HackTheBox."

______

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

______

### Flag Example:
```
HTB{xxxxxxxxxxxxxxxxxxx}
```