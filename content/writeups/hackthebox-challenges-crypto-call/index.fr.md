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
```
2331434783711923431767372331117714113
```
```
23 31 43 47 83 71 19 23 43 17 67 37 23 31 11 7 71 41 13
```
```
2331434783711923431767372331117714113
```
```
HTB{xxxxxxxxxxxxxxxxxxx}
```
 Résolvez le défi Crypto - Call sur HackTheBox en décodant les tonalités DTMF dans le fichier sound.mp3. Convertissez le fichier en .wav et utilisez DialABC pour obtenir le texte chiffré. Séparez les nombres et utilisez le chiffrement des nombres premiers sur Decode.fr pour révéler le drapeau. Préparez-vous à mettre vos compétences en chiffrement de nombres premiers à l'épreuve dans ce défi passionnant sur HackTheBox."  ______  ##Fichiers fournis :  Un fichier vous est fourni : - fils.mp3  ## Procédure pas à pas :  En jouant le **sound.mp3**, vous entendez un son familier. Si vous n'êtes pas familier avec les sons que vous entendez, ce sont les tonalités **DTMF** (double tonalité multifréquence). Les mêmes tonalités que vous entendez lorsque vous appelez sur un téléphone public ou lorsque vous parcourez les menus des guichets automatiques.  Chaque tonalité a une fréquence spécifique. Vous pourriez obtenir les chiffres manuellement, mais qui a le temps pour cela ? [DialABC](http://www.dialabc.com/sound/detect/index.html) dispose d'un excellent outil pour cela, mais ne prend pas en charge les fichiers mp3. Tout d'abord, vous devrez le convertir en .wav avec cet [outil](https://online-audio-converter.com/)  Transférez le fichier converti vers [DialABC](http://www.dialabc.com/sound/detect/index.html) et vous réussirez le résultat suivant :   Notez que si vous écoutez attentivement le fichier audio ou si vous l'ouvrez dans **Audacity** ou **Sonic Visualizer**, à une exception près, les numéros sont appariés par groupes de deux. Si vous séparez le nombre, vous obtenez ce qui suit :  Organisé comme ça, vous pourriez être confus et penser qu'il pourrait s'agir de HEX. Ce n'est pas le cas. Faites bien attention aux chiffres. Quel trait mathématique chaque groupe de nombres partage-t-il ?.... Ce sont tous des nombres premiers. Ce qui devrait vous amener à essayer le **chiffre des nombres premiers** moins connu.  Nous utiliserons [Decode.fr](https://www.dcode.fr/prime-numbers-cipher) pour relever ce défi. Soumettez le texte chiffré d'avant qu'on le sépare et vous aurez le drapeau.  ______  Exemple d'indicateur ### :