---
title: "HackTheBox - Challenges - Crypto - Bank Heist"
date: 2020-10-07
draft: false
toc: true
description: "Learn how to decode T9/Multitap and Atbash ciphers to solve the Bank Heist challenge on HackTheBox."
tags: ["hackthebox", "cryptographie", "Chiffre T9", "cryptogramme multitap", "cryptogramme atbash", "la cybersécurité", "décoder", "texte chiffré", "challenge", "drapeau", "cybersécurité", "piratage", "apprendre", "tutoriel", "décodage du code", "résolution d'énigmes", "décryptage", "défi de la cryptographie", "compétences en matière de cybersécurité", "apprentissage en ligne"]
cover: "/img/cover/A_cartoon_vault_door_being_unlocked_with_a_key_revealing.png"
coverAlt: "une porte de coffre-fort en bande dessinée qui s'ouvre avec une clé révélant un coffre au trésor, le tout sur fond de paysage urbain parisien au coucher du soleil."
coverCaption: ""
---

Un guide complet pour résoudre le défi Crypto "Bank Heist" sur HackTheBox. Le défi consiste à décoder un [T9](https://simeononsecurity.com/articles/introduction-to-t9-cipher/) or [Multitap cipher](https://simeononsecurity.com/articles/introduction-to-t9-cipher/) Le texte chiffré de l'attaque de l'armée française a été révélé à l'aide de Decode.fr et le texte chiffré de l'attaque à l'aide de CyberChef pour dévoiler le drapeau. Une lecture incontournable pour les professionnels de la cybersécurité en herbe et pour tous ceux qui cherchent à améliorer leurs compétences en cryptographie.

## Fichiers fournis :

Pour ce défi, vous recevrez le texte chiffré suivant :

```
444333 99966688 277733 7773323444664 84433 22244474433777, 99966688 277733 666552999. 99966688777 777744277733 666333 84433 443344477778 4447777 44466 99966688777 4466688777733. 84433 5533999 8666 84433 55566622255 4447777 22335556669. 4666 8666 727774447777.

47777888 995559888 4555 47777888 44999988 666555997 : 8555444888477744488866888648833369!!
```

______

## Walk Through :

**Très clairement, il s'agit soit d'un chiffrement T9, soit d'un chiffrement Multitap**.
Dans ce cas, c'est Multitap qui est le cryptogramme. [Decode.fr](https://www.dcode.fr/multitap-abc-cipher) dispose d'un outil de décodage.

Vous obtiendrez ce texte en clair :
```
IF YOU ARE READING THE CIPHER, YOU ARE OKAY. YOUR SHARE OF THE HEIST IS IN YOUR HOUSE. THE KEY TO THE LOCK IS BELOW, GO TO PARIS GSV XLWV GL GSV HZU OLXP TLIVGRIVNVMGUFMW
```

**Qu'est-ce que c'est que cette saloperie à la fin, me direz-vous ? Il s'agit en fait d'un texte chiffré atbash**.

```
GSV XLWV GL GSV HZU OLXP TLIVGRIVNVMGUFMW
```


Nous utiliserons [CyberChef](<https://gchq.github.io/CyberChef-#recipe=Atbash_Cipher()&input=R1NWIFhMV1YgR0wgR1NWIEhaVSBPTFhQIApUTElWR1JJVk5WTUdVRk1X>) à déchiffrer une fois de plus. Ensuite, vous avez votre drapeau. Whoot !

______

### Exemple de drapeau :

```
HTB{XXXXXXXXXXXXXXXXX}
```
