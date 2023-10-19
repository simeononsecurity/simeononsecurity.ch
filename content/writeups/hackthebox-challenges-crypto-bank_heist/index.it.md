---
title: "HackTheBox - Sfide - Criptovalute - Rapina in banca"
date: 2020-10-07
draft: false
toc: true
description: "Learn how to decode T9/Multitap and Atbash ciphers to solve the Bank Heist challenge on HackTheBox."
tags: ["hackthebox", "crittografia", "Cifrario T9", "cifrario multitap", "cifrario atbash", "sicurezza informatica", "decodificare", "testo cifrato", "sfida", "bandiera", "sicurezza informatica", "hacking", "imparare", "tutorial", "decodifica del cifrario", "risoluzione di puzzle", "decifrazione di codici", "sfida di crittografia", "competenze di cybersecurity", "apprendimento online"]
cover: "/img/cover/A_cartoon_vault_door_being_unlocked_with_a_key_revealing.png"
coverAlt: "una porta di un caveau a fumetti che viene aperta con una chiave e rivela un forziere, il tutto sullo sfondo di un paesaggio urbano parigino al tramonto."
coverCaption: ""
---

Una guida completa per risolvere la sfida Crypto "Bank Heist" su HackTheBox. La sfida prevede la decodifica di un [T9](https://simeononsecurity.ch/articles/introduction-to-t9-cipher/) or [Multitap cipher](https://simeononsecurity.ch/articles/introduction-to-t9-cipher/) e un testo cifrato atbash usando CyberChef per rivelare la bandiera. Una lettura imperdibile per gli aspiranti professionisti della sicurezza informatica e per chiunque voglia migliorare le proprie competenze in materia di crittografia.

## File forniti:

Per questa sfida vi viene fornito il seguente testo cifrato:

```
444333 99966688 277733 7773323444664 84433 22244474433777, 99966688 277733 666552999. 99966688777 777744277733 666333 84433 443344477778 4447777 44466 99966688777 4466688777733. 84433 5533999 8666 84433 55566622255 4447777 22335556669. 4666 8666 727774447777.

47777888 995559888 4555 47777888 44999988 666555997 : 8555444888477744488866888648833369!!
```

______

## Passeggiata:

**Molto chiaramente, questo è un cifrario T9 o Multitap.
In questo caso, però, il cifrario è Multitap. [Decode.fr](https://www.dcode.fr/multitap-abc-cipher) ha uno strumento per decodificarlo.

Si otterrà questo testo in chiaro:
```
IF YOU ARE READING THE CIPHER, YOU ARE OKAY. YOUR SHARE OF THE HEIST IS IN YOUR HOUSE. THE KEY TO THE LOCK IS BELOW, GO TO PARIS GSV XLWV GL GSV HZU OLXP TLIVGRIVNVMGUFMW
```

**Che cos'è quella robaccia alla fine, vi chiederete? Beh, in realtà è un testo cifrato atbash **.

```
GSV XLWV GL GSV HZU OLXP TLIVGRIVNVMGUFMW
```


Utilizzeremo [CyberChef](<https://gchq.github.io/CyberChef-#recipe=Atbash_Cipher()&input=R1NWIFhMV1YgR0wgR1NWIEhaVSBPTFhQIApUTElWR1JJVk5WTUdVRk1X>) da decifrare un'altra volta. Poi avrete la vostra bandiera. Che bello!

______

### Esempio di bandiera:

```
HTB{XXXXXXXXXXXXXXXXX}
```
