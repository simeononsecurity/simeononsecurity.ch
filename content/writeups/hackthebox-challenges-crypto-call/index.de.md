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

Jeder Ton hat eine bestimmte Frequenz. Sie könnten die Zahlen manuell abrufen, aber wer hat die Zeit dafür? [DialABC](http://www.dialabc.com/sound/detect/index.html) has a great tool for this, but doesn't support mp3 files. First, you'll have to convert it to .wav with this [tool](https://online-audio-converter.com/)

Nehmen Sie die konvertierte Datei mit [DialABC](http://www.dialabc.com/sound/detect/index.html) und Sie erhalten die folgende Ausgabe:
```
2331434783711923431767372331117714113
```
 
Beachten Sie, dass die Zahlen mit einer Ausnahme in Zweiergruppen gepaart sind, wenn Sie sich die Audiodatei genau anhören oder sie in **Audacity** oder **Sonic Visualizer** öffnen.
Wenn man die Zahl heraustrennt, erhält man Folgendes:
```
23 31 43 47 83 71 19 23 43 17 67 37 23 31 11 7 71 41 13
```

Wenn Sie so organisiert sind, könnten Sie verwirrt sein und denken, dass es HEX sein könnte. Das ist es nicht.
Achten Sie genau auf die Zahlen. Welches mathematische Merkmal haben die einzelnen Zahlengruppierungen gemeinsam?
Es sind alles Primzahlen. Das sollte Sie dazu bringen, die weniger bekannte **Primzahl-Chiffre** auszuprobieren.

Wir werden verwenden [Decode.fr](https://www.dcode.fr/prime-numbers-cipher) um diese Herausforderung zu meistern.
Reichen Sie den Chiffretext ein, bevor wir ihn herausgetrennt haben, und Sie erhalten die Flagge.
```
2331434783711923431767372331117714113
```

______

### Flag-Beispiel:
```
HTB{xxxxxxxxxxxxxxxxxxx}
```