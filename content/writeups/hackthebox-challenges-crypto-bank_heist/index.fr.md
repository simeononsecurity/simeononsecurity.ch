---
title: "HackTheBox - Défis - Crypto - Bank Heist"
date: 2020-10-07
draft: false
toc: true
description: "Learn how to decode T9/Multitap and Atbash ciphers to solve the Bank Heist challenge on HackTheBox."
tags: ["pirater la boîte", "cryptographie", "Chiffrement T9", "chiffrement multitap", "chiffrement atbash", "la cyber-sécurité", "décoder", "texte chiffré", "défi", "drapeau", "la cyber-sécurité", "le piratage", "apprendre", "Didacticiel", "décodage chiffré", "résolution d'énigmes", "briser le code", "défi cryptographie", "compétences en cybersécurité", "apprentissage en ligne"]
cover: "/img/cover/A_cartoon_vault_door_being_unlocked_with_a_key_revealing.png"
coverAlt: "une porte de coffre-fort de dessin animé déverrouillée avec une clé révélant un coffre au trésor, le tout sur fond de paysage urbain parisien au coucher du soleil."
coverCaption: ""
---

Un guide complet pour résoudre le défi Crypto "Bank Heist" sur HackTheBox. Le défi consiste à décoder un texte chiffré T9 ou Multitap à l'aide de Decode.fr et un texte chiffré atbash à l'aide de CyberChef pour révéler le drapeau. Une lecture incontournable pour les aspirants professionnels de la cybersécurité et tous ceux qui cherchent à améliorer leurs compétences en cryptographie.

## Fichiers fournis :

Pour ce défi, le texte chiffré suivant vous est fourni :

```
444333 99966688 277733 7773323444664 84433 22244474433777, 99966688 277733 666552999. 99966688777 777744277733 666333 84433 443344477778 4447777 44466 99966688777 4466688777733. 84433 5533999 8666 84433 55566622255 4447777 22335556669. 4666 8666 727774447777.

47777888 995559888 4555 47777888 44999988 666555997 : 8555444888477744488866888648833369!!
```

______

## Procédure pas à pas:

**Très clairement, il s'agit d'un chiffrement T9 ou Multitap.**
Multitap est le chiffrement dans ce cas cependant. [Decode.fr](https://www.dcode.fr/multitap-abc-cipher) a un outil pour décoder cela.

Vous obtiendrez ce texte brut :
```
IF YOU ARE READING THE CIPHER, YOU ARE OKAY. YOUR SHARE OF THE HEIST IS IN YOUR HOUSE. THE KEY TO THE LOCK IS BELOW, GO TO PARIS GSV XLWV GL GSV HZU OLXP TLIVGRIVNVMGUFMW
```

** Quelle est cette ordure à la fin que vous pourriez demander ? Eh bien, c'est en fait un texte chiffré atbash. **

```
GSV XLWV GL GSV HZU OLXP TLIVGRIVNVMGUFMW
```


Nous utiliserons [CyberChef](<https://gchq.github.io/CyberChef-#recipe=Atbash_Cipher()&input=R1NWIFhMV1YgR0wgR1NWIEhaVSBPTFhQIApUTElWR1JJVk5WTUdVRk1X>) à déchiffrer une fois de plus. Ensuite, vous avez votre drapeau. Wouh !

______

Exemple d'indicateur ### :

```
HTB{XXXXXXXXXXXXXXXXX}
```
