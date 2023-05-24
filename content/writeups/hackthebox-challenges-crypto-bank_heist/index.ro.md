---
title: "HackTheBox - Provocări - Crypto - Bank Heist"
date: 2020-10-07
draft: false
toc: true
description: "Learn how to decode T9/Multitap and Atbash ciphers to solve the Bank Heist challenge on HackTheBox."
tags: ["hackthebox", "criptografie", "Cifrul T9", "cifru multitap", "cifrul atbash", "securitate cibernetică", "decodifica", "text cifrat", "provocare", "steag", "securitate cibernetică", "hacking", "învăța", "tutorial", "decodificarea cifrului", "rezolvarea puzzle-urilor", "ruperea codurilor", "provocarea criptografiei", "abilități de securitate cibernetică", "învățarea online"]
cover: "/img/cover/A_cartoon_vault_door_being_unlocked_with_a_key_revealing.png"
coverAlt: "o ușă a seifului din desene animate fiind descuiată cu o cheie care dezvăluie un cufăr de comori, totul așezat pe fundalul unui peisaj urban parizian la apus."
coverCaption: ""
---

Un ghid cuprinzător pentru rezolvarea provocării „Bank Heist” Crypto pe HackTheBox. Provocarea implică decodarea unui text cifru T9 sau Multitap folosind Decode.fr și a unui text cifru atbash folosind CyberChef pentru a dezvălui steag. O lectură obligatorie pentru profesioniști în domeniul securității cibernetice care aspiră și pentru oricine dorește să-și îmbunătățească abilitățile în criptografie.

## Fișiere furnizate:

Pentru această provocare, vi se oferă următorul text cifrat:

```
444333 99966688 277733 7773323444664 84433 22244474433777, 99966688 277733 666552999. 99966688777 777744277733 666333 84433 443344477778 4447777 44466 99966688777 4466688777733. 84433 5533999 8666 84433 55566622255 4447777 22335556669. 4666 8666 727774447777.

47777888 995559888 4555 47777888 44999988 666555997 : 8555444888477744488866888648833369!!
```

______

## Plimbare prin:

**Foarte clar, acesta este fie un cifr T9, fie Multitap.**
Multitap este însă cifrul în acest caz. [Decode.fr](https://www.dcode.fr/multitap-abc-cipher) are un instrument pentru a decoda asta.

Veți primi acest text simplu:
```
IF YOU ARE READING THE CIPHER, YOU ARE OKAY. YOUR SHARE OF THE HEIST IS IN YOUR HOUSE. THE KEY TO THE LOCK IS BELOW, GO TO PARIS GSV XLWV GL GSV HZU OLXP TLIVGRIVNVMGUFMW
```

**Ce este acel gunoi la sfârșit pe care ai putea să o întrebi? Ei bine, este de fapt un text cifrat atbash.**

```
GSV XLWV GL GSV HZU OLXP TLIVGRIVNVMGUFMW
```


Vom folosi [CyberChef](<https://gchq.github.io/CyberChef-#recipe=Atbash_Cipher()&input=R1NWIFhMV1YgR0wgR1NWIEhaVSBPTFhQIApUTElWR1JJVk5WTUdVRk1X>) pentru a descifra încă o dată. Atunci ai steagul tău. Vai!

______

### Exemplu de semnalizare:

```
HTB{XXXXXXXXXXXXXXXXX}
```
