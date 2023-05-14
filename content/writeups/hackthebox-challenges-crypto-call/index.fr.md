---
title: "HackTheBox - Défis - Crypto - Appel"
date: 2020-10-07
draft: false
description: "Apprenez à décrypter les tonalités DTMF à l'aide du chiffrement des nombres premiers pour résoudre le défi Crypto - Call sur HackTheBox."
tags: ["HackTheBox", "Défi Crypto", "Tonalités DTMF", "Chiffrement des nombres premiers", "Décryptage", "Résoudre des puzzles", "Cryptographie", "Conversion audio", "ComposezABC", "Decode.fr", "WAV", "MP3", "Fréquence", "Trait mathématique", "Drapeau", "Audace", "Visualiseur sonique", "Nombres", "Menus des guichets automatiques", "Téléphone public"]
toc: true
cover: "/img/cover/A_cartoon_phone_with_a_green_screen_and_a_padlock_on_it.png"
coverAlt: "Un téléphone de dessin animé avec un écran vert et un cadenas dessus, symbolisant la sécurité et le cryptage, avec des tonalités DTMF représentées dans le motif"
coverCaption: ""
---

Résolvez le défi Crypto - Call sur HackTheBox en décodant les tonalités DTMF dans le fichier sound.mp3. Convertissez le fichier en .wav et utilisez DialABC pour obtenir le texte chiffré. Séparez les nombres et utilisez le chiffrement des nombres premiers sur Decode.fr pour révéler le drapeau. Préparez-vous à mettre vos compétences en chiffrement de nombres premiers à l'épreuve dans ce défi passionnant sur HackTheBox."

______

## Fichiers fournis :

Un fichier vous est fourni :
- son.mp3

## Procédure pas à pas:

En jouant le **sound.mp3**, vous entendrez un son familier. Si vous n'êtes pas familier avec les sons que vous entendez, ce sont les tonalités **DTMF** (double tonalité multifréquence). Les mêmes tonalités que vous entendiez lorsque vous appelez sur un téléphone public ou lorsque vous parcourez les menus des guichets automatiques.

Chaque tonalité a une fréquence spécifique. Vous pourriez obtenir les chiffres manuellement, mais qui a le temps pour cela ?[DialABC](http://www.dialabc.com/sound/detect/index.html) has a great tool for this, but doesn't support mp3 files. First, you'll have to convert it to .wav with this [tool](https://online-audio-converter.com/)

Prenez le fichier converti dans[DialABC](http://www.dialabc.com/sound/detect/index.html) et vous obtiendrez la sortie suivante :
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