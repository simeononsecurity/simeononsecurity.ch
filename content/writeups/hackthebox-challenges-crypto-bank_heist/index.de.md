---
title: "HackTheBox – Herausforderungen – Krypto – Banküberfall"
date: 2020-10-07
draft: false
toc: true
description: "Learn how to decode T9/Multitap and Atbash ciphers to solve the Bank Heist challenge on HackTheBox."
tags: ["hackthebox", "Kryptographie", "T9-Verschlüsselung", "Multitap-Verschlüsselung", "Atbash-Chiffre", "Internet-Sicherheit", "dekodieren", "Geheimtext", "Herausforderung", "Flagge", "Internet-Sicherheit", "Hacken", "lernen", "Lernprogramm", "Chiffre-Dekodierung", "Puzzle lösen", "Code knacken", "Kryptographie-Herausforderung", "Cybersicherheitskompetenzen", "Online lernen"]
cover: "/img/cover/A_cartoon_vault_door_being_unlocked_with_a_key_revealing.png"
coverAlt: "Eine Cartoon-Tresortür, die mit einem Schlüssel aufgeschlossen wird und eine Schatzkiste zum Vorschein bringt, alles vor dem Hintergrund einer Pariser Stadtlandschaft bei Sonnenuntergang."
coverCaption: ""
---

Eine umfassende Anleitung zur Lösung der Krypto-Herausforderung „Bankraub“ auf HackTheBox. Die Herausforderung besteht darin, einen T9- oder Multitap-Verschlüsselungstext mit Decode.fr und einen Atbash-Verschlüsselungstext mit CyberChef zu dekodieren, um die Flagge aufzudecken. Eine Pflichtlektüre für angehende Cyber-Sicherheitsexperten und alle, die ihre Fähigkeiten in der Kryptographie verbessern möchten.

## Bereitgestellte Dateien:

Für diese Herausforderung erhalten Sie den folgenden Chiffriertext:

```
444333 99966688 277733 7773323444664 84433 22244474433777, 99966688 277733 666552999. 99966688777 777744277733 666333 84433 443344477778 4447777 44466 99966688777 4466688777733. 84433 5533999 8666 84433 55566622255 4447777 22335556669. 4666 8666 727774447777.

47777888 995559888 4555 47777888 44999988 666555997 : 8555444888477744488866888648833369!!
```

______

## Durchgehen:

**Ganz klar handelt es sich hierbei entweder um eine T9- oder Multitap-Verschlüsselung.**
In diesem Fall ist jedoch Multitap die Verschlüsselung. [Decode.fr](https://www.dcode.fr/multitap-abc-cipher) hat ein Tool, um dies zu entschlüsseln.

Sie erhalten diesen Klartext:
```
IF YOU ARE READING THE CIPHER, YOU ARE OKAY. YOUR SHARE OF THE HEIST IS IN YOUR HOUSE. THE KEY TO THE LOCK IS BELOW, GO TO PARIS GSV XLWV GL GSV HZU OLXP TLIVGRIVNVMGUFMW
```

**Was ist das für ein Blödsinn am Ende, fragen Sie sich vielleicht? Nun, es ist eigentlich ein Atbash-Chiffretext.**

```
GSV XLWV GL GSV HZU OLXP TLIVGRIVNVMGUFMW
```


Wir werden verwenden [CyberChef](<https://gchq.github.io/CyberChef-#recipe=Atbash_Cipher()&input=R1NWIFhMV1YgR0wgR1NWIEhaVSBPTFhQIApUTElWR1JJVk5WTUdVRk1X>) noch einmal zu entschlüsseln. Dann haben Sie Ihre Flagge. Whoot!

______

### Flag-Beispiel:

```
HTB{XXXXXXXXXXXXXXXXX}
```
