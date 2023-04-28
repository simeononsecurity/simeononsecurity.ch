---
title: "HackTheBox - Challenges - Crypto - Bank Heist"
date: 2020-10-07
draft: false
toc: true
description: "Learn how to decode T9/Multitap and Atbash ciphers to solve the Bank Heist challenge on HackTheBox."
tags: ["hackthebox", "cryptography", "T9 cipher", "multitap cipher", "atbash cipher", "cyber security", "decode", "ciphertext", "challenge", "flag", "cybersecurity", "hacking", "learn", "tutorial", "cipher decoding", "puzzle solving", "codebreaking", "cryptography challenge", "cybersecurity skills", "online learning"]
cover: "/img/cover/A_cartoon_vault_door_being_unlocked_with_a_key_revealing.png"
coverAlt: "a cartoon vault door being unlocked with a key revealing a treasure chest, all set against a backdrop of a Parisian cityscape at sunset."
coverCaption: ""
---
```
444333 99966688 277733 7773323444664 84433 22244474433777, 99966688 277733 666552999. 99966688777 777744277733 666333 84433 443344477778 4447777 44466 99966688777 4466688777733. 84433 5533999 8666 84433 55566622255 4447777 22335556669. 4666 8666 727774447777.

47777888 995559888 4555 47777888 44999988 666555997 : 8555444888477744488866888648833369!!
```
```
IF YOU ARE READING THE CIPHER, YOU ARE OKAY. YOUR SHARE OF THE HEIST IS IN YOUR HOUSE. THE KEY TO THE LOCK IS BELOW, GO TO PARIS GSV XLWV GL GSV HZU OLXP TLIVGRIVNVMGUFMW
```
```
GSV XLWV GL GSV HZU OLXP TLIVGRIVNVMGUFMW
```
```
HTB{XXXXXXXXXXXXXXXXX}
```

 Eine umfassende Anleitung zum Lösen der Krypto-Herausforderung „Banküberfall“ auf HackTheBox. Die Herausforderung besteht darin, einen T9- oder Multitap-Chiffriertext mit Decode.fr und einen Atbash-Chiffriertext mit CyberChef zu entschlüsseln, um die Flagge aufzudecken. Ein Muss für angehende Cybersicherheitsexperten und alle, die ihre Kenntnisse in Kryptografie verbessern möchten.  ## Bereitgestellte Dateien:  Für diese Herausforderung erhalten Sie den folgenden verschlüsselten Text:   ______  ##Durchgang:  **Ganz klar, das ist entweder eine T9- oder eine Multitap-Chiffre.** Multitap ist in diesem Fall jedoch die Chiffre. [Decode.fr](https://www.dcode.fr/multitap-abc-cipher) hat ein Tool, um dies zu entschlüsseln.  Sie erhalten diesen Klartext:  **Was ist das für ein Müll am Ende, fragen Sie sich vielleicht? Nun, es ist eigentlich ein Atbash-Chiffriertext.**    Wir verwenden [CyberChef](<https://gchq.github.io/CyberChef-#recipe=Atbash_Cipher()&input=R1NWIFhMV1YgR0wgR1NWIEhaVSBPTFhQIApUTElWR1JJVk5WTUdVRk1X>), um noch einmal zu entschlüsseln. Dann hast du deine Flagge. Hurra!  ______  ### Flag-Beispiel: 