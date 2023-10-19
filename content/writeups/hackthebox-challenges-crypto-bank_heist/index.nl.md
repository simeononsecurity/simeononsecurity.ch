---
title: "HackTheBox - Uitdagingen - Crypto - Bankroof"
date: 2020-10-07
draft: false
toc: true
description: "Learn how to decode T9/Multitap and Atbash ciphers to solve the Bank Heist challenge on HackTheBox."
tags: ["hackthebox", "cryptografie", "T9-code", "multitap cijfer", "atbash cijfer", "cyberveiligheid", "decoderen", "cijfertekst", "uitdaging", "vlag", "cyberbeveiliging", "hacken", "leren", "handleiding", "decoderen van cijfers", "puzzels oplossen", "codebreker", "cryptografie-uitdaging", "cyberbeveiligingsvaardigheden", "online onderwijs"]
cover: "/img/cover/A_cartoon_vault_door_being_unlocked_with_a_key_revealing.png"
coverAlt: "een cartoonachtige kluisdeur die wordt ontgrendeld met een sleutel die een schatkist onthult, allemaal tegen een achtergrond van een Parijs stadslandschap bij zonsondergang."
coverCaption: ""
---

Een uitgebreide handleiding voor het oplossen van de Crypto-uitdaging "Bank Heist" op HackTheBox. De uitdaging bestaat uit het decoderen van een [T9](https://simeononsecurity.com/articles/introduction-to-t9-cipher/) or [Multitap cipher](https://simeononsecurity.com/articles/introduction-to-t9-cipher/) tekst met Decode.fr en een atbash-cryptekst met CyberChef om de vlag te onthullen. Een must voor aspirant cyberbeveiligingsprofessionals en iedereen die zijn vaardigheden in cryptografie wil verbeteren.

## Meegeleverde bestanden:

Voor deze uitdaging krijg je de volgende codeertekst:

```
444333 99966688 277733 7773323444664 84433 22244474433777, 99966688 277733 666552999. 99966688777 777744277733 666333 84433 443344477778 4447777 44466 99966688777 4466688777733. 84433 5533999 8666 84433 55566622255 4447777 22335556669. 4666 8666 727774447777.

47777888 995559888 4555 47777888 44999988 666555997 : 8555444888477744488866888648833369!!
```

______

## Doorlopen:

**Het is heel duidelijk dat dit of een T9 of een Multitap cijfer is.**
In dit geval is het echter Multitap. [Decode.fr](https://www.dcode.fr/multitap-abc-cipher) heeft een hulpmiddel om dit te decoderen.

Je krijgt dan deze platte tekst:
```
IF YOU ARE READING THE CIPHER, YOU ARE OKAY. YOUR SHARE OF THE HEIST IS IN YOUR HOUSE. THE KEY TO THE LOCK IS BELOW, GO TO PARIS GSV XLWV GL GSV HZU OLXP TLIVGRIVNVMGUFMW
```

**Wat is die troep aan het einde, vraag je je misschien af? Dat is eigenlijk een atbash-code.**

```
GSV XLWV GL GSV HZU OLXP TLIVGRIVNVMGUFMW
```


We gebruiken [CyberChef](<https://gchq.github.io/CyberChef-#recipe=Atbash_Cipher()&input=R1NWIFhMV1YgR0wgR1NWIEhaVSBPTFhQIApUTElWR1JJVk5WTUdVRk1X>) om nog een keer te ontcijferen. Dan heb je je vlag. Whoot!

______

### Voorbeeld van vlag:

```
HTB{XXXXXXXXXXXXXXXXX}
```
