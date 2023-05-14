---
title: "HackTheBox – Herausforderungen – Krypto – Anruf"
date: 2020-10-07
draft: false
description: "Erfahren Sie, wie Sie DTMF-Töne mithilfe der Primzahlverschlüsselung entschlüsseln, um die Crypto-Call-Herausforderung auf HackTheBox zu lösen."
tags: ["HackTheBox", "Krypto-Herausforderung", "DTMF-Töne", "Primzahl-Chiffre", "Entschlüsselung", "Rätsel lösen", "Kryptographie", "Audiokonvertierung", "Wählen Sie ABC", "Decode.fr", "WAV", "MP3", "Frequenz", "Mathematische Eigenschaft", "Flagge", "Unverfrorenheit", "Sonic Visualizer", "Zahlen", "Automatisierte Tellermenüs", "Münztelefon"]
toc: true
cover: "/img/cover/A_cartoon_phone_with_a_green_screen_and_a_padlock_on_it.png"
coverAlt: "Ein Cartoon-Telefon mit einem grünen Bildschirm und einem Vorhängeschloss darauf, das Sicherheit und Verschlüsselung symbolisiert, mit DTMF-Tönen im Hintergrund"
coverCaption: ""
---

Lösen Sie die Crypto-Call-Challenge auf HackTheBox, indem Sie die DTMF-Töne in der Datei sound.mp3 dekodieren. Konvertieren Sie die Datei in .wav und verwenden Sie DialABC, um den Chiffriertext abzurufen. Trennen Sie die Zahlen und verwenden Sie die Primzahlverschlüsselung auf Decode.fr, um die Flagge anzuzeigen. Machen Sie sich bereit, Ihre Fähigkeiten in der Primzahlverschlüsselung in dieser spannenden Herausforderung auf HackTheBox unter Beweis zu stellen.“

______

## Bereitgestellte Dateien:

Ihnen wird eine Datei bereitgestellt:
- Ton.mp3

## Durchgehen:

Beim Abspielen der **sound.mp3** hören Sie einen vertrauten Ton. Wenn Sie nicht wissen, welche Geräusche Sie hören, hören Sie **DTMF**-Töne (Dual Tone Multi Frequency). Dieselben Töne, die Sie früher beim Wählen an einem Münztelefon oder beim Navigieren durch die Menüs des Geldautomaten hörten.

Jeder Ton hat eine bestimmte Frequenz. Sie könnten die Zahlen manuell abrufen, aber wer hat die Zeit dafür?[DialABC](http://www.dialabc.com/sound/detect/index.html) has a great tool for this, but doesn't support mp3 files. First, you'll have to convert it to .wav with this [tool](https://online-audio-converter.com/)

Nehmen Sie die konvertierte Datei mit[DialABC](http://www.dialabc.com/sound/detect/index.html) und Sie erhalten die folgende Ausgabe:
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