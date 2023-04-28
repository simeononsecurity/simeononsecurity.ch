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

 Una guía completa para resolver el desafío Crypto "Bank Heist" en HackTheBox. El desafío consiste en decodificar un texto activado T9 o Multitap usando Decode.fr y un texto activado atbash usando CyberChef para revelar la bandera. Una lectura obligada para los aspirantes a profesionales de la seguridad cibernética y cualquiera que busque mejorar sus habilidades en criptografía.  ##Archivos provistos:  Para este desafío, se le proporciona el siguiente texto grabado:   ______  ## Caminar a través de:  **Muy claramente, esto es un cifrado T9 o Multitap.** Sin embargo, Multitap es el grabado en este caso. [Decode.fr](https://www.dcode.fr/multitap-abc-cipher) tiene una herramienta para decodificar esto.  Obtendrá este texto sin formato:  ** ¿Qué es esa basura al final, podrías preguntar? Bueno, en realidad es un texto grabado atbash.**    Usaremos [CyberChef](<https://gchq.github.io/CyberChef-#recipe=Atbash_Cipher()&input=R1NWIFhMV1YgR0wgR1NWIEhaVSBPTFhQIApUTElWR1JJVk5WTUdVRk1X>) para descifrar una vez más. Entonces tienes tu bandera. ¡Uau!  ______  ### Ejemplo de indicador: 