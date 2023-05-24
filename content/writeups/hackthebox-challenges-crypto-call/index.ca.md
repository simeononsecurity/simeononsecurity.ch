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

Cada to té una freqüència específica. Podeu obtenir els números manualment, però qui té temps per fer-ho? [DialABC](http://www.dialabc.com/sound/detect/index.html) has a great tool for this, but doesn't support mp3 files. First, you'll have to convert it to .wav with this [tool](https://online-audio-converter.com/)

Agafeu el fitxer convertit a [DialABC](http://www.dialabc.com/sound/detect/index.html) i obtindreu la següent sortida:
```
2331434783711923431767372331117714113
```
 
Tingueu en compte que si escolteu el fitxer d'àudio amb atenció o l'obreu a **Audacity** o **Sonic Visualizer**, amb una excepció, els números s'aparellen en grups de dos.
Si separeu el número obtindreu el següent:
```
23 31 43 47 83 71 19 23 43 17 67 37 23 31 11 7 71 41 13
```

Organitzat així, podríeu estar confós i pensar que podria ser HEX. No ho és.
Presta molta atenció als números. Quin tret matemàtic comparteix cada agrupació de nombres?...
Tots són nombres primers. Això us hauria de portar a provar el menys conegut **xifrat de nombres primers**.

Farem servir [Decode.fr](https://www.dcode.fr/prime-numbers-cipher) per completar aquest repte.
Envieu el text xifrat d'abans de separar-lo i obtindreu la bandera.
```
2331434783711923431767372331117714113
```

______

### Exemple de bandera:
```
HTB{xxxxxxxxxxxxxxxxxxx}
```