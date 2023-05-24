---
title: "HackTheBox - Desafíos - Cripto - Atraco bancario"
date: 2020-10-07
draft: false
toc: true
description: "Learn how to decode T9/Multitap and Atbash ciphers to solve the Bank Heist challenge on HackTheBox."
tags: ["piratear la caja", "criptografía", "cifrado T9", "cifrado multitap", "cifra atbash", "la seguridad cibernética", "descodificar", "texto cifrado", "desafío", "bandera", "la seguridad cibernética", "hackear", "aprender", "tutorial", "decodificación de cifrado", "resolución de rompecabezas", "desciframiento de códigos", "desafío de criptografía", "habilidades de ciberseguridad", "aprender en línea"]
cover: "/img/cover/A_cartoon_vault_door_being_unlocked_with_a_key_revealing.png"
coverAlt: "una puerta de la bóveda de dibujos animados que se abre con una llave que revela un cofre del tesoro, todo con el telón de fondo de un paisaje urbano parisino al atardecer."
coverCaption: ""
---

Una guía completa para resolver el desafío Crypto "Bank Heist" en HackTheBox. El desafío consiste en decodificar un texto cifrado T9 o Multitap usando Decode.fr y un texto cifrado atbash usando CyberChef para revelar la bandera. Una lectura obligada para los aspirantes a profesionales de la seguridad cibernética y cualquiera que busque mejorar sus habilidades en criptografía.

## Archivos proporcionados:

Para este desafío, se le proporciona el siguiente texto cifrado:

```
444333 99966688 277733 7773323444664 84433 22244474433777, 99966688 277733 666552999. 99966688777 777744277733 666333 84433 443344477778 4447777 44466 99966688777 4466688777733. 84433 5533999 8666 84433 55566622255 4447777 22335556669. 4666 8666 727774447777.

47777888 995559888 4555 47777888 44999988 666555997 : 8555444888477744488866888648833369!!
```

______

## Caminar a través de:

**Muy claramente, este es un cifrado T9 o Multitap.**
Sin embargo, Multitap es el cifrado en este caso. [Decode.fr](https://www.dcode.fr/multitap-abc-cipher) tiene una herramienta para decodificar esto.

Obtendrá este texto sin formato:
```
IF YOU ARE READING THE CIPHER, YOU ARE OKAY. YOUR SHARE OF THE HEIST IS IN YOUR HOUSE. THE KEY TO THE LOCK IS BELOW, GO TO PARIS GSV XLWV GL GSV HZU OLXP TLIVGRIVNVMGUFMW
```

** ¿Qué es esa basura al final, podrías preguntar? Bueno, en realidad es un texto cifrado atbash.**

```
GSV XLWV GL GSV HZU OLXP TLIVGRIVNVMGUFMW
```


usaremos [CyberChef](<https://gchq.github.io/CyberChef-#recipe=Atbash_Cipher()&input=R1NWIFhMV1YgR0wgR1NWIEhaVSBPTFhQIApUTElWR1JJVk5WTUdVRk1X>) para descifrar una vez más. Entonces tienes tu bandera. ¡Uau!

______

### Ejemplo de indicador:

```
HTB{XXXXXXXXXXXXXXXXX}
```
