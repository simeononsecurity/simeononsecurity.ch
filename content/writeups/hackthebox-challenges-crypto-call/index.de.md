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
 Löse die Crypto - Call Challenge auf HackTheBox, indes du die DTMF-Töne in der sound.mp3-Datei entschlüsselst. Konvertieren Sie die Datei in .wav und verwenden Sie DialABC, um den verschlüsselten Text zu erhalten. Trennen Sie die Zahlen und verwenden Sie die Primzahlchiffre auf Decode.fr, um die Flagge aufzudecken. Machen Sie sich bereit, Ihre Fähigkeiten in der Primzahlenverschlüsselung in dieser spannenden Herausforderung auf HackTheBox auf die Probe zu stellen."  ______  ## Bereitgestellte Dateien:  Sie erhalten eine Datei: - Ton.mp3  ##Durchgang:  Wenn Sie die **sound.mp3** abspielen, hören Sie einen vertrauten Sound. Wenn Sie die Geräusche sterben, sterben Sie hören, nicht kennen, hören Sie **DTMF** (Dual Tone Multi Frequency)-Töne. Die gleichen Töne, sterben Sie früher beim Wählen mit einem Münztelefon oder beim Durchlaufen der Menüs von Geldautomaten gehört Haben.  Jeder Ton hat eine bestimmte Frequenz. Sie könnten die Zahlen manuell abrufen, aber was hat die Zeit dafür getan? [DialABC](http://www.dialabc.com/sound/detect/index.html) hat ein hervorragendes Tool dafür, unterstützt aber keine MP3-Dateien. Zuerst müssen Sie es mit diesem [Tool] (https://online-audio-converter.com/) in .wav konvertieren.  Bringen SIE sterben konvertierte Datei zu [DialABC](http://www.dialabc.com/sound/detect/index.html) und Sie erhalten folgende Ausgabe:   Beachten Sie, dass, wenn Sie sich die Audiodatei genau anhören oder sie in **Audacity** oder **Sonic Visualizer** öffnen, die Zahlen mit einer Ausnahme in Zweiergruppen gepaart sind. Trennt man die Zahl heraus, erhält man folgendes:  So organisiert, könnten Sie verwirrt sein und denken, dass es sich um HEX handeln könnte. Es ist nicht. Achten Sie genau auf die Zahlen. Welches mathematische Merkmal haben alle Zahlengruppierungen gemeinsam? .... Das sind alles Primzahlen. Was Sie dazu bringen sollten, die weniger bekannten **Primzahlchiffre** auszuprobieren.  Wir verwenden [Decode.fr](https://www.dcode.fr/prime-numbers-cipher), um diese Herausforderung zu meistern. Reichen Sie den verschlüsselten Text ein, bevor wir ihn getrennt haben, und Sie erhalten das Flag.  ______  ### Flag-Beispiel: