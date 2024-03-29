---
title: "HackTheBox - Herausforderungen - Krypto - Banküberfall"
date: 2020-10-07
draft: false
toc: true
description: "Learn how to decode T9/Multitap and Atbash ciphers to solve the Bank Heist challenge on HackTheBox."
tags: ["hackthebox", "Kryptographie", "T9-Chiffre", "Multitap-Verschlüsselung", "atbash-Chiffre", "Cybersicherheit", "dekodieren", "Chiffretext", "challenge", "Flagge", "Cybersicherheit", "Hacken", "lernen", "Lehrgang", "Chiffrier-Entschlüsselung", "Rätsellösen", "Code-Knacken", "Kryptographie-Herausforderung", "Cybersicherheitsfähigkeiten", "Online-Lernen"]
cover: "/img/cover/A_cartoon_vault_door_being_unlocked_with_a_key_revealing.png"
coverAlt: "eine Cartoon-Tresortür, die mit einem Schlüssel aufgeschlossen wird und eine Schatztruhe freigibt, und das alles vor dem Hintergrund einer Pariser Stadtlandschaft bei Sonnenuntergang."
coverCaption: ""
---

Eine umfassende Anleitung zum Lösen der "Bank Heist" Krypto-Herausforderung auf HackTheBox. Die Herausforderung beinhaltet die Entschlüsselung einer [T9](https://simeononsecurity.com/articles/introduction-to-t9-cipher/) or [Multitap cipher](https://simeononsecurity.com/articles/introduction-to-t9-cipher/) Text mit Decode.fr und einen atbash-Chiffretext mit CyberChef, um die Flagge zu enthüllen. Eine Pflichtlektüre für angehende Cybersicherheitsexperten und alle, die ihre Kryptografiekenntnisse verbessern möchten.

## Bereitgestellte Dateien:

Für diese Aufgabe wird Ihnen der folgende Chiffriertext zur Verfügung gestellt:

```
444333 99966688 277733 7773323444664 84433 22244474433777, 99966688 277733 666552999. 99966688777 777744277733 666333 84433 443344477778 4447777 44466 99966688777 4466688777733. 84433 5533999 8666 84433 55566622255 4447777 22335556669. 4666 8666 727774447777.

47777888 995559888 4555 47777888 44999988 666555997 : 8555444888477744488866888648833369!!
```

______

## Walk Through:

**Es handelt sich ganz klar entweder um eine T9- oder eine Multitap-Chiffre.
In diesem Fall ist Multitap jedoch die Chiffre. [Decode.fr](https://www.dcode.fr/multitap-abc-cipher) verfügt über ein Werkzeug, um dies zu entschlüsseln.

Sie erhalten diesen Klartext:
```
IF YOU ARE READING THE CIPHER, YOU ARE OKAY. YOUR SHARE OF THE HEIST IS IN YOUR HOUSE. THE KEY TO THE LOCK IS BELOW, GO TO PARIS GSV XLWV GL GSV HZU OLXP TLIVGRIVNVMGUFMW
```

**Was ist dieser Müll am Ende, werden Sie sich fragen? Nun, es ist eigentlich ein atbash-Chiffretext.**

```
GSV XLWV GL GSV HZU OLXP TLIVGRIVNVMGUFMW
```


Wir verwenden [CyberChef](<https://gchq.github.io/CyberChef-#recipe=Atbash_Cipher()&input=R1NWIFhMV1YgR0wgR1NWIEhaVSBPTFhQIApUTElWR1JJVk5WTUdVRk1X>) ein weiteres Mal zu entziffern. Dann haben Sie Ihre Flagge. Puh!

______

### Flagge Beispiel:

```
HTB{XXXXXXXXXXXXXXXXX}
```
