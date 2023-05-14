---
title: "HackTheBox - Challenge - Crypto - RSA feble"
draft: false
description: "Apreneu a utilitzar una eina d'atac RSA automatitzada, RsaCtfTool, per resoldre fàcilment el repte HackTheBox Weak RSA Crypto."
tags: ["HackTheBox", "Desafiaments", "Cripto", "RSA feble", "RsaCtfTool", "HTB Weak RSA Crypto", "Repte fàcil", "Xifrat RSA", "flag.enc", "key.pub", "Paquet OpenSSL", "eina automatitzada d'atac RSA", "script python", "RsaCtfTool", "python3", "clau pública", "desxifrar fitxer", "Exemple de bandera"]
toc: true
cover: "/img/cover/A_cartoon_hacker_wearing_a_cape_and_a_mask_standing.png"
coverAlt: "Un pirata informàtic de dibuixos animats amb una capa i una màscara, de peu davant d'una porta de la volta amb el logotip de HTB i sostenint una eina (com una clau anglesa o un tornavís) amb un fons verd que simbolitza l'èxit i la bandera en una bafarada a sobre el seu cap."
coverCaption: ""
---
 el repte HTB Weak RSA Crypto amb facilitat. Basat en el xifratge RSA, aquest repte fàcil requereix l'ús d'una eina d'atac RSA automatitzada com el RsaCtfTool. Aconsegueix la bandera amb una ordre senzilla i amplia les teves habilitats criptogràfiques amb els reptes HackTheBox.

______

## Fitxers proporcionats:

**Se li proporcionen els fitxers següents:**
- bandera.enc
- clau.pub

## Recorregut:

A primera vista, penseu que podeu desxifrar la bandera amb la clau pública.
Per això, podríem utilitzar el paquet OpenSSL per desxifrar la bandera.
Aquesta vegada és una mica diferent i trobareu que el paquet OpenSSL no funcionarà per a aquest repte.

Utilitzarem una eina d'atac RSA automatitzada. Un script Python comú és el[RsaCtfTool](https://github.com/Ganapati/RsaCtfTool)

```bash
python3 RsaCtfTool.py --publickey ./key.pub --uncipherfile ./flag.enc 
```
  
Simply put, this tool finds the flag easily for you in an automated fashion.

______

### Flag Example:
```
HTB{XXXXXX_XXXXXXX_XXXXXX}
```
