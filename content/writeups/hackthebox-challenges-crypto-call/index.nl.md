---
title: "HackTheBox - Uitdagingen - Crypto - Oproep"
date: 2020-10-07
draft: false
description: "Leer hoe DTMF-tonen kunnen worden ontcijferd met behulp van een priemgetal om de Crypto - Call-uitdaging op HackTheBox op te lossen."
tags: ["HackTheBox", "Crypto Uitdaging", "DTMF-tonen", "Prime Number Cipher", "Ontcijfering", "Puzzels oplossen", "Cryptografie", "Audio Conversie", "DialABC", "Decode.fr", "WAV", "MP3", "Frequentie", "Wiskundige eigenschap", "Vlag", "Audacity", "Sonic Visualizer", "Nummers", "Menu's voor geautomatiseerde kassa's", "Betaaltelefoon"]
toc: true
cover: "/img/cover/A_cartoon_phone_with_a_green_screen_and_a_padlock_on_it.png"
coverAlt: "Een cartoontelefoon met een groen scherm en een hangslot erop, als symbool voor veiligheid en encryptie, met DTMF-tonen op de achtergrond."
coverCaption: ""
---

Los de Crypto - Call uitdaging op HackTheBox op door de DTMF tonen in het sound.mp3 bestand te decoderen. Converteer het bestand naar .wav en gebruik DialABC om de cijfertekst te krijgen. Scheid de nummers en gebruik de priemgetallencode op Decode.fr om de vlag te onthullen. Maak je klaar om je vaardigheden in priemgetalvercijfering op de proef te stellen in deze spannende uitdaging op HackTheBox."

______

## Geleverde bestanden:

U krijgt één bestand:
- sound.mp3

## Doorlopen:

Als je de **sound.mp3** afspeelt, hoor je een bekend geluid. Als u niet bekend bent, zijn de geluiden die u hoort **DTMF** (dual tone multi frequency) tonen. Dezelfde tonen die u vroeger hoorde bij het bellen met een telefooncel of bij het doorlopen van een kassaregister.

Elke toon heeft een specifieke frequentie. U kunt de nummers handmatig invoeren, maar wie heeft daar tijd voor?[DialABC](http://www.dialabc.com/sound/detect/index.html) has a great tool for this, but doesn't support mp3 files. First, you'll have to convert it to .wav with this [tool](https://online-audio-converter.com/)

Neem het geconverteerde bestand mee naar[DialABC](http://www.dialabc.com/sound/detect/index.html) en je krijgt de volgende uitvoer:
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