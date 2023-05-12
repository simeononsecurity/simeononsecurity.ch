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

 Un guide complet pour résoudre le défi Crypto "Bank Heist" sur HackTheBox. Le défi consiste à décoder un texte chiffré T9 ou Multitap à l'aide de Decode.fr et un texte chiffré atbash à l'aide de CyberChef pour révéler le drapeau. Une conférence incontournable pour les aspirants professionnels de la cybersécurité et tous ceux qui cherchent à améliorer leurs compétences en cryptographie.  ##Fichiers fournis :  Pour ce défi, le texte chiffré suivant vous est fourni :   ______  ## Procédure pas à pas :  **Très clairement, il s'agit d'un chiffrement T9 ou Multitap.** Multitap est le chiffrement dans ce cas cependant. [Decode.fr](https://www.dcode.fr/multitap-abc-cipher) un outil pour décoder cela.  Vous autorisez ce texte brut :  ** Quelle est cette ordonnance à la fin que vous pourriez demander ? Eh bien, c'est en fait un texte chiffré atbash. **    Nous utiliserons [CyberChef](<https://gchq.github.io/CyberChef-#recipe=Atbash_Cipher()&input=R1NWIFhMV1YgR0wgR1NWIEhaVSBPTFhQIApUTElWR1JJVk5WTUdVRk1X>) pour déchiffrer une fois de plus. Ensuite, vous avez votre drapeau. Ouah !  ______  Exemple d'indicateur ### : 