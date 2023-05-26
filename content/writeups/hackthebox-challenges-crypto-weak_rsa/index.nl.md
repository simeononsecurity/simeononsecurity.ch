---
title: "HackTheBox - Uitdaging - Crypto - Zwakke RSA"
draft: false
description: "Leer hoe u een geautomatiseerd RSA-aanvalshulpmiddel, RsaCtfTool, kunt gebruiken om de HackTheBox Weak RSA Crypto uitdaging eenvoudig op te lossen."
tags: ["HackTheBox", "Uitdagingen", "Crypto", "Zwakke RSA", "RsaCtfTool", "HTB Zwakke RSA Crypto", "Eenvoudige uitdaging", "RSA-cijfer", "flag.enc", "key.pub", "OpenSSL pakket", "geautomatiseerd RSA-aanvalsinstrument", "python-script", "RsaCtfTool", "python3", "openbare sleutel", "uncipherfile", "Voorbeeld vlag"]
toc: true
cover: "/img/cover/A_cartoon_hacker_wearing_a_cape_and_a_mask_standing.png"
coverAlt: "Een cartoonhacker met een cape en een masker, staand voor een kluisdeur met het HTB-logo erop en met een gereedschap (zoals een moersleutel of een schroevendraaier) in de hand, met een groene achtergrond die succes symboliseert en de vlag in een tekstballon boven zijn hoofd."
coverCaption: ""
---
 de HTB Weak RSA Crypto uitdaging met gemak. Gebaseerd op het RSA-cijfer, vereist deze eenvoudige uitdaging het gebruik van een geautomatiseerd RSA-aanvalshulpmiddel zoals het RsaCtfTool. Haal de vlag binnen met een eenvoudig commando en breid uw crypto-vaardigheden uit met HackTheBox-uitdagingen.

______

## Geleverde bestanden:

**U krijgt de volgende bestanden:**
- flag.enc
- key.pub

## Walk-through:

Op het eerste gezicht zou je denken dat je de vlag kunt decoderen met de publieke sleutel.   
Daarvoor zouden we het OpenSSL pakket kunnen gebruiken om de vlag te decoderen.
Deze keer is het een beetje anders en je zult zien dat het OpenSSL pakket niet werkt voor deze uitdaging.

We gebruiken een geautomatiseerd RSA-aanvalsprogramma. Een veelgebruikt python script is de [RsaCtfTool](https://github.com/Ganapati/RsaCtfTool)

```bash
python3 RsaCtfTool.py --publickey ./key.pub --uncipherfile ./flag.enc 
```
  
Eenvoudig gezegd, dit hulpmiddel vindt de vlag gemakkelijk voor u op een geautomatiseerde manier.

______

### Voorbeeld van een vlag:
```
HTB{XXXXXX_XXXXXXX_XXXXXX}
```
