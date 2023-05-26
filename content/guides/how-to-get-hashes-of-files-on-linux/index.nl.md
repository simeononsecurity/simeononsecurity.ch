---
title: "Linux bestandshashes: Een gids voor het verkrijgen van SHA256-, MD5- en SHA1-hashes met behulp van ingebouwde tools"
draft: false
toc: true
date: 2023-05-25
description: "Leer hoe u SHA256-, MD5- en SHA1-hashes van bestanden op Linux kunt verkrijgen met behulp van ingebouwde tools, waarbij de integriteit van de gegevens en de authenticiteit van het bestand worden gewaarborgd."
tags: ["Linux bestandshashes", "SHA256 hash", "MD5 hash", "SHA1 hash", "Linux commandoregel", "bestandsintegriteit", "datavalidatie", "Linux beveiliging", "ingebouwde instrumenten", "bestandsverificatie", "authenticiteit van de gegevens", "hashing algoritmen voor bestanden", "Linux systeembeheer", "commandoregeltools", "bestandscontrolesommen", "Linux hulpprogramma's", "integriteitscontroles van bestanden", "verificatie van de integriteit van de gegevens", "bestands hash voorbeelden", "Linux hash-commando's", "hashingmethoden voor bestanden", "Linux beveiligingsmaatregelen", "Linux gegevensbescherming", "Linux bestandsbeheer", "Linux bestandsverificatie", "Linux bestandsintegriteit", "gegevensbeveiliging", "Validatie van Linux-gegevens", "Linux systeembeveiliging", "hashing technieken voor bestanden", "waarborging van de integriteit van bestanden", "veilige bestandsvalidatie", "Linux gegevensintegriteit"]
cover: "/img/cover/A_digital_representation_of_file_hashes_being_calculated.png"
coverAlt: "Een digitale weergave van bestandshashes die worden berekend op een Linux-terminalscherm, als symbool voor gegevensintegriteit en -beveiliging."
coverCaption: ""
---

**Gids: Verkrijgen van hashes van bestanden op Linux met behulp van ingebouwde tools**

## Inleiding

In de wereld van Linux systemen is het verkrijgen van bestandshashes essentieel voor het waarborgen van gegevensintegriteit en het verifiëren van de authenticiteit van bestanden. Bestandshashes dienen als unieke identificatiemiddelen waarmee gebruikers pogingen tot knoeien kunnen detecteren en de integriteit van gegevens kunnen valideren. In deze uitgebreide gids wordt onderzocht hoe **SHA256**, **MD5** en **SHA1** hashes van bestanden op Linux kunnen worden verkregen met behulp van ingebouwde tools. Volg de stapsgewijze instructies en leer aan de hand van specifieke voorbeelden.

______

## Hashes verkrijgen op Linux met behulp van ingebouwde tools

Linux heeft verschillende ingebouwde gereedschappen waarmee gebruikers bestands-hashes kunnen berekenen zonder extra software te hoeven installeren. We zullen drie veelgebruikte hashing-algoritmen onderzoeken: **SHA256**, **MD5**, en **SHA1**.

### De SHA256-hash verkrijgen

Om de **SHA256 hash** van een bestand op Linux te verkrijgen, kunt u het programma `sha256sum` commando. Open een terminal en navigeer naar de directory waar het bestand zich bevindt. Voer vervolgens het volgende commando uit:

```bash
sha256sum file_path
```
Vervang `file_path` met het werkelijke pad naar uw bestand.

### De MD5- en SHA1-hashes verkrijgen
U kunt ook de `MD5` en `SHA1 hashes` van een bestand op Linux met soortgelijke commando's:

- Om de `MD5 hash`

```bash
md5sum file_path
```

- Om de `SHA1 hash`

```bash
sha1sum file_path
```
Vervang `file_path` met het pad naar uw bestand in beide commando's.

## Voorbeelden
Laten we ons verdiepen in specifieke voorbeelden om het proces van het verkrijgen van hashes met behulp van ingebouwde gereedschappen op Linux te illustreren.

{{< youtube id="3aX9zK88X9M" >}}

### Voorbeeld 1: SHA256-hash verkrijgen
Stel u heeft een bestand met de naam `document.pdf` in de directory `/home/user/docs` Om de `SHA256 hash` van dit bestand op Linux, voer het volgende commando uit:

```bash
sha256sum /home/user/docs/document.pdf
```

De uitvoer toont de `SHA256 hash` waarde van het bestand.

### Voorbeeld 2: MD5 Hash verkrijgen

Stel u heeft een bestand met de naam `image.jpg` opgeslagen in de directory `/home/user/pictures` Om de `MD5 hash` van dit bestand op Linux, voer het volgende commando uit:

```bash
md5sum /home/user/pictures/image.jpg
```

De terminal zal de `MD5 hash` waarde van het bestand.

## Voorbeeld 3: SHA1 Hash verkrijgen

Beschouw een scenario waarin u een bestand hebt met de naam `data.txt` in de directory `/home/user/files` Om de `SHA1 hash` van dit bestand op Linux, voer het volgende commando uit:

```bash
sha1sum /home/user/files/data.txt
```
De uitvoer toont de `SHA1 hash` waarde van het bestand.

## Conclusie
Het verkrijgen van bestands-hashes op Linux met behulp van ingebouwde tools is een eenvoudige maar krachtige methode om de integriteit van gegevens te waarborgen en de authenticiteit van bestanden te valideren. Door de instructies in deze gids te volgen, kunt u met vertrouwen SHA256-, MD5- en SHA1-hashes van uw bestanden op Linux-systemen berekenen.

## Referenties

1. [sha256sum - Linux man page](https://man7.org/linux/man-pages/man1/sha256sum.1.html)
2. [md5sum - Linux man page](https://man7.org/linux/man-pages/man1/md5sum.1.html)
3. [sha1sum - Linux man page](https://man7.org/linux/man-pages/man1/sha1sum.1.html)
