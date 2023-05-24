---
title: "HackTheBox - Reptes - Crypto - Bank Heist"
date: 2020-10-07
draft: false
toc: true
description: "Learn how to decode T9/Multitap and Atbash ciphers to solve the Bank Heist challenge on HackTheBox."
tags: ["pirateja la caixa", "criptografia", "Xifrat T9", "xifrat multitap", "xifrat atbash", "seguretat cibernètica", "descodificar", "text xifrat", "desafiament", "bandera", "seguretat cibernètica", "pirateig", "aprendre", "tutorial", "descodificació de xifratge", "resolució de trencaclosques", "trencament de codi", "repte de criptografia", "habilitats de ciberseguretat", "aprenentatge en línia"]
cover: "/img/cover/A_cartoon_vault_door_being_unlocked_with_a_key_revealing.png"
coverAlt: "una porta de la volta de dibuixos animats que s'obre amb una clau que revela un cofre del tresor, tot amb un teló de fons d'un paisatge urbà parisenc al capvespre."
coverCaption: ""
---

Una guia completa per resoldre el repte de criptografia "Bank Heist" a HackTheBox. El repte consisteix a descodificar un text xifrat T9 o Multitap amb Decode.fr i un text xifrat atbash amb CyberChef per revelar la bandera. Una lectura obligada per als aspirants a professionals de la ciberseguretat i qualsevol persona que vulgui millorar les seves habilitats en criptografia.

## Fitxers proporcionats:

Per a aquest repte se us proporciona el text xifrat següent:

```
444333 99966688 277733 7773323444664 84433 22244474433777, 99966688 277733 666552999. 99966688777 777744277733 666333 84433 443344477778 4447777 44466 99966688777 4466688777733. 84433 5533999 8666 84433 55566622255 4447777 22335556669. 4666 8666 727774447777.

47777888 995559888 4555 47777888 44999988 666555997 : 8555444888477744488866888648833369!!
```

______

## Passejada:

**Molt clarament, això és un xifratge T9 o Multitap.**
Tanmateix, el multitap és el xifrat en aquest cas. [Decode.fr](https://www.dcode.fr/multitap-abc-cipher) té una eina per descodificar-ho.

Obtindreu aquest text senzill:
```
IF YOU ARE READING THE CIPHER, YOU ARE OKAY. YOUR SHARE OF THE HEIST IS IN YOUR HOUSE. THE KEY TO THE LOCK IS BELOW, GO TO PARIS GSV XLWV GL GSV HZU OLXP TLIVGRIVNVMGUFMW
```

**Què és aquesta brossa al final que podríeu preguntar? Bé, en realitat és un text xifrat atbash.**

```
GSV XLWV GL GSV HZU OLXP TLIVGRIVNVMGUFMW
```


Farem servir [CyberChef](<https://gchq.github.io/CyberChef-#recipe=Atbash_Cipher()&input=R1NWIFhMV1YgR0wgR1NWIEhaVSBPTFhQIApUTElWR1JJVk5WTUdVRk1X>) per desxifrar una vegada més. Llavors tens la teva bandera. Vaja!

______

### Exemple de bandera:

```
HTB{XXXXXXXXXXXXXXXXX}
```
