---
title: "HackTheBox - Desafío - Cripto - RSA débil"
draft: false
description: "Aprenda a usar una herramienta de ataque RSA automatizada, RsaCtfTool, para resolver fácilmente el desafío HackTheBox Weak RSA Crypto."
tags: ["HackTheBox", "Desafíos", "Cripto", "RSA débil", "RsaCtfHerramienta", "Cripto RSA débil HTB", "Desafío fácil", "cifrado RSA", "flag.enc", "key.pub", "Paquete OpenSSL", "herramienta de ataque RSA automatizada", "secuencia de comandos de pitón", "RsaCtfHerramienta", "pitón3", "Llave pública", "descifrar archivo", "Ejemplo de bandera"]
toc: true
cover: "/img/cover/A_cartoon_hacker_wearing_a_cape_and_a_mask_standing.png"
coverAlt: "Un hacker de dibujos animados con una capa y una máscara, parado frente a la puerta de una bóveda con el logotipo de HTB y sosteniendo una herramienta (como una llave inglesa o un destornillador) con un fondo verde que simboliza el éxito y la bandera en una burbuja de diálogo arriba su cabeza"
coverCaption: ""
---
 el desafío HTB Weak RSA Crypto con facilidad. Basado en el cifrado RSA, este sencillo desafío requiere el uso de una herramienta de ataque RSA automatizada como RsaCtfTool. Obtenga la bandera con un simple comando y amplíe sus habilidades criptográficas con los desafíos de HackTheBox.

______

## Archivos proporcionados:

**Se le proporcionan los siguientes archivos:**
- bandera.enc
- clave.pub

## Tutorial:

A primera vista, pensaría que puede descifrar la bandera con la clave pública.
Para eso, podríamos usar el paquete OpenSSL para descifrar la bandera.
Esta vez es un poco diferente y encontrará que el paquete OpenSSL no funcionará para este desafío.

Usaremos una herramienta de ataque RSA automatizada. Un script de Python común es el[RsaCtfTool](https://github.com/Ganapati/RsaCtfTool)

```bash
python3 RsaCtfTool.py --publickey ./key.pub --uncipherfile ./flag.enc 
```
  
Simply put, this tool finds the flag easily for you in an automated fashion.

______

### Flag Example:
```
HTB{XXXXXX_XXXXXXX_XXXXXX}
```
