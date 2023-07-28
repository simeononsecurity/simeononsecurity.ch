---
title: "HackTheBox - Provocări - Crypto - Bank Heist"
date: 2020-10-07
draft: false
toc: true
description: "Learn how to decode T9/Multitap and Atbash ciphers to solve the Bank Heist challenge on HackTheBox."
tags: ["hackthebox", "criptografie", "Cifru T9", "cifru multitap", "cifru atbash", "securitate cibernetică", "decodificare", "Textul cifrat", "provocare", "steag", "securitate cibernetică", "hacking", "învață", "tutorial", "decodarea cifrului", "rezolvarea puzzle-urilor", "spargerea codurilor", "provocare criptografică", "competențe în domeniul securității cibernetice", "învățare online"]
cover: "/img/cover/A_cartoon_vault_door_being_unlocked_with_a_key_revealing.png"
coverAlt: "o ușă de seif din desene animate care se deschide cu o cheie și dezvăluie un cufăr cu comori, totul pe fundalul unui peisaj urban parizian la apus."
coverCaption: ""
---

Un ghid complet pentru a rezolva provocarea Crypto "Bank Heist" pe HackTheBox. Provocarea presupune decodarea unui [T9](https://simeononsecurity.ch/articles/introduction-to-t9-cipher/) or [Multitap cipher](https://simeononsecurity.ch/articles/introduction-to-t9-cipher/) text folosind Decode.fr și un text cifrat atbash folosind CyberChef pentru a descoperi steagul. O lectură obligatorie pentru profesioniștii aspiranți la securitate cibernetică și pentru oricine dorește să își îmbunătățească abilitățile în domeniul criptografiei.

## Fișiere furnizate:

Pentru această provocare vi se pune la dispoziție următorul text cifrat:

```
444333 99966688 277733 7773323444664 84433 22244474433777, 99966688 277733 666552999. 99966688777 777744277733 666333 84433 443344477778 4447777 44466 99966688777 4466688777733. 84433 5533999 8666 84433 55566622255 4447777 22335556669. 4666 8666 727774447777.

47777888 995559888 4555 47777888 44999988 666555997 : 8555444888477744488866888648833369!!
```

______

## Walk Through:

**Este foarte clar că acesta este un cifru T9 sau Multitap.**
Multitap este totuși cifrul în acest caz. [Decode.fr](https://www.dcode.fr/multitap-abc-cipher) are un instrument pentru a decoda acest lucru.

Veți obține acest text simplu:
```
IF YOU ARE READING THE CIPHER, YOU ARE OKAY. YOUR SHARE OF THE HEIST IS IN YOUR HOUSE. THE KEY TO THE LOCK IS BELOW, GO TO PARIS GSV XLWV GL GSV HZU OLXP TLIVGRIVNVMGUFMW
```

**Ce este acel gunoi de la sfârșit, ați putea întreba? Ei bine, este de fapt un text cifrat atbash.**

```
GSV XLWV GL GSV HZU OLXP TLIVGRIVNVMGUFMW
```


Vom folosi [CyberChef](<https://gchq.github.io/CyberChef-#recipe=Atbash_Cipher()&input=R1NWIFhMV1YgR0wgR1NWIEhaVSBPTFhQIApUTElWR1JJVk5WTUdVRk1X>) pentru a descifra încă o dată. Apoi aveți steagul dumneavoastră. Whoot!

______

### Exemplu de steag:

```
HTB{XXXXXXXXXXXXXXXXX}
```
