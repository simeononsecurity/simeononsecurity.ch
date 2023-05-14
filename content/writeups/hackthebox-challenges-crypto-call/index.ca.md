---
title: "HackTheBox - Reptes - Crypto - Truca"
date: 2020-10-07
draft: false
description: "Apreneu a desxifrar els tons DTMF mitjançant el xifrat de nombres primers per resoldre el repte Crypto - Call a HackTheBox."
tags: ["HackTheBox", "Crypto Challenge", "Tons DTMF", "Xifrat de nombre primer", "Desxifrat", "Resolució de trencaclosques", "Criptografia", "Conversió d'àudio", "Marqueu ABC", "Decode.fr", "WAV", "MP3", "Freqüència", "Tret matemàtic", "Bandera", "Audàcia", "Visualitzador sonor", "Nombres", "Menús de caixers automàtics", "Telèfon de pagament"]
toc: true
cover: "/img/cover/A_cartoon_phone_with_a_green_screen_and_a_padlock_on_it.png"
coverAlt: "Un telèfon de dibuixos animats amb una pantalla verda i un cadenat al damunt, que simbolitza la seguretat i el xifratge, amb tons DTMF representats al fons"
coverCaption: ""
---

Resoldre el repte Crypto - Call a HackTheBox descodificant els tons DTMF al fitxer sound.mp3. Converteix el fitxer a .wav i utilitza DialABC per obtenir el text xifrat. Separeu els números i utilitzeu el xifrat de nombres primers a Decode.fr per revelar la bandera. Prepareu-vos per posar a prova les vostres habilitats en xifrat de nombres primers en aquest emocionant repte a HackTheBox".

______

## Fitxers proporcionats:

Se us proporciona un fitxer:
- so.mp3

## Passejada:

En reproduir el **sound.mp3**, escoltaràs un so familiar. Si no coneixeu els sons que escolteu, escolteu els tons **DTMF** (doble to multifreqüència). Els mateixos tons que solia escoltar mentre marcava amb un telèfon públic o mentre passava pels menús dels caixers automàtics.

Cada to té una freqüència específica. Podeu obtenir els números manualment, però qui té temps per fer-ho?[DialABC](http://www.dialabc.com/sound/detect/index.html) has a great tool for this, but doesn't support mp3 files. First, you'll have to convert it to .wav with this [tool](https://online-audio-converter.com/)

Agafeu el fitxer convertit a[DialABC](http://www.dialabc.com/sound/detect/index.html) i obtindreu la següent sortida:
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