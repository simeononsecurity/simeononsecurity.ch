---
title: "HackTheBox - Wyzwania - Kryptowaluty - Napad na bank"
date: 2020-10-07
draft: false
toc: true
description: "Learn how to decode T9/Multitap and Atbash ciphers to solve the Bank Heist challenge on HackTheBox."
tags: ["hackthebox", "kryptografia", "Szyfr T9", "szyfr multitap", "szyfr atbash", "cyberbezpieczeństwo", "dekodowanie", "szyfrogram", "wyzwanie", "flaga", "cyberbezpieczeństwo", "hakowanie", "uczyć się", "samouczek", "dekodowanie szyfru", "rozwiązywanie zagadek", "łamanie kodów", "wyzwanie kryptograficzne", "umiejętności w zakresie cyberbezpieczeństwa", "nauka online"]
cover: "/img/cover/A_cartoon_vault_door_being_unlocked_with_a_key_revealing.png"
coverAlt: "kreskówkowe drzwi skarbca otwierane kluczem, odsłaniające skrzynię ze skarbem, a wszystko to na tle paryskiego krajobrazu o zachodzie słońca."
coverCaption: ""
---

Kompleksowy przewodnik po rozwiązaniu wyzwania kryptograficznego "Napad na bank" w HackTheBox. Wyzwanie polega na zdekodowaniu [T9](https://simeononsecurity.ch/articles/introduction-to-t9-cipher/) or [Multitap cipher](https://simeononsecurity.ch/articles/introduction-to-t9-cipher/) przy użyciu Decode.fr i szyfrogramu atbash przy użyciu CyberChef w celu ujawnienia flagi. Lektura obowiązkowa dla aspirujących specjalistów ds. cyberbezpieczeństwa i każdego, kto chce podnieść swoje umiejętności w zakresie kryptografii.

## Dostarczone pliki:

W tym wyzwaniu otrzymasz następujący tekst szyfrujący:

```
444333 99966688 277733 7773323444664 84433 22244474433777, 99966688 277733 666552999. 99966688777 777744277733 666333 84433 443344477778 4447777 44466 99966688777 4466688777733. 84433 5533999 8666 84433 55566622255 4447777 22335556669. 4666 8666 727774447777.

47777888 995559888 4555 47777888 44999988 666555997 : 8555444888477744488866888648833369!!
```

______

## Walk Through:

**Bardzo wyraźnie widać, że jest to szyfr T9 lub Multitap**.
Multitap jest jednak szyfrem w tym przypadku. [Decode.fr](https://www.dcode.fr/multitap-abc-cipher) ma narzędzie do dekodowania tego.

Otrzymasz ten zwykły tekst:
```
IF YOU ARE READING THE CIPHER, YOU ARE OKAY. YOUR SHARE OF THE HEIST IS IN YOUR HOUSE. THE KEY TO THE LOCK IS BELOW, GO TO PARIS GSV XLWV GL GSV HZU OLXP TLIVGRIVNVMGUFMW
```

**Co to za śmieci na końcu? W rzeczywistości jest to tekst zaszyfrowany atbash.**.

```
GSV XLWV GL GSV HZU OLXP TLIVGRIVNVMGUFMW
```


Będziemy używać [CyberChef](<https://gchq.github.io/CyberChef-#recipe=Atbash_Cipher()&input=R1NWIFhMV1YgR0wgR1NWIEhaVSBPTFhQIApUTElWR1JJVk5WTUdVRk1X>) rozszyfrować jeszcze raz. Wtedy masz swoją flagę. Whoot!

______

### Przykład flagi:

```
HTB{XXXXXXXXXXXXXXXXX}
```
