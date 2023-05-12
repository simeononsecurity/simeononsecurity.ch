---
title: "HackTheBox - Sfida - Cripto - RSA debole"
draft: false
description: "Scopri come utilizzare uno strumento di attacco RSA automatizzato, RsaCtfTool, per risolvere facilmente la sfida HackTheBox Weak RSA Crypto."
tags: ["HackTheBox","Sfide","Crittografia","RSA debole","Strumento RsaCtf","HTB Debole RSA Crypto","Sfida facile","cifratura RSA","flag.enc", "key.pub", "Pacchetto OpenSSL","strumento di attacco RSA automatizzato","sceneggiatura Python","Strumento RsaCtf","python3","chiave pubblica","file non cifrato","Esempio di bandiera"]
toc: true
cover: "/img/cover/A_cartoon_hacker_wearing_a_cape_and_a_mask_standing.png"
coverAlt: "Un hacker di cartoni animati che indossa un mantello e una maschera, in piedi davanti a una porta del caveau con il logo HTB sopra e con in mano uno strumento (come una chiave inglese o un cacciavite) con uno sfondo verde che simboleggia il successo e la bandiera in un fumetto sopra la loro testa”.
coverCaption: ""
---
 la sfida HTB Weak RSA Crypto con facilità. Basato sul codice RSA, questa semplice sfida richiede l'uso di uno strumento di attacco RSA automatizzato come RsaCtfTool. Ottieni la bandiera con un semplice comando ed espandi le tue abilità crittografiche con le sfide di HackTheBox.

______

## File forniti:

**Ti vengono forniti i seguenti file:**
- flag.enc
- key.pub

## Procedura dettagliata:

A prima vista, penseresti di poter decifrare il flag con la chiave pubblica.
Per questo, potremmo usare il pacchetto OpenSSL per decifrare il flag.
Questa volta è un po' diverso e scoprirai che il pacchetto OpenSSL non funzionerà per questa sfida.

Useremo uno strumento di attacco RSA automatizzato. Uno script python comune è il[RsaCtfTool](https://github.com/Ganapati/RsaCtfTool)

```bash
python3 RsaCtfTool.py --publickey ./key.pub --uncipherfile ./flag.enc 
```
  
Simply put, this tool finds the flag easily for you in an automated fashion.

______

### Flag Example:
```
HTB{XXXXXX_XXXXXXX_XXXXXX}
```
