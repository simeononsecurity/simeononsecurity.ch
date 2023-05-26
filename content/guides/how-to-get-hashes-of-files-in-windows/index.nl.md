---
title: "Complete gids: Bestandshashes op Windows met PowerShell"
draft: false
toc: true
date: 2023-05-25
description: "Leer hoe u met PowerShell hashes van bestanden in Windows verkrijgt, waaronder SHA256, MD5 en SHA1, met stapsgewijze instructies en voorbeelden."
tags: ["bestandshashes", "PowerShell", "SHA256 hash", "MD5 hash", "SHA1 hash", "bestandsintegriteit", "gegevensauthenticatie", "bestandsverificatie", "hashing-algoritmen", "Windows-besturingssysteem", "scripttaal", "commandoregel", "gegevensbeveiliging", "digitaal forensisch onderzoek", "cyberbeveiliging", "hashberekening", "geknoei met bestanden", "gegevensintegriteit", "authenticiteit van het bestand", "Windows beveiliging", "bestandsidentificatie", "cyberdefensie", "bestandsbeveiliging", "gegevensbescherming", "gegevenscontrole", "bestandsvalidatie", "Windows PowerShell", "hash generatie", "hash-algoritmen", "hashfuncties"]
cover: "/img/cover/A_cartoon_illustration_showing_a_file_with_a_lock_symbol.png"
coverAlt: "Een cartoonillustratie van een bestand met een slotsymbool en een vergrootglas, voor verificatie en beveiliging van de hash van een bestand."
coverCaption: ""
---

**Hoe verkrijg ik hashes van bestanden in Windows met PowerShell**.

Op het gebied van computerbeveiliging is het verkrijgen van bestandshashes een cruciale stap in het waarborgen van gegevensintegriteit en het verifiëren van de authenticiteit van bestanden. Hashes zijn unieke identificatiecodes die voor bestanden worden gegenereerd, zodat gebruikers pogingen tot knoeien kunnen detecteren en de integriteit van gegevens kunnen valideren. In deze uitgebreide gids onderzoeken we het proces voor het verkrijgen van **SHA256**, **MD5** en **SHA1** hashes van bestanden onder Windows met behulp van de krachtige scripttaal **PowerShell**. Volg de stap-voor-stap instructies en neem een diepe duik in specifieke voorbeelden. Aan de slag!

______

## Hashes verkrijgen op Windows met PowerShell

PowerShell, een veelzijdige scripttaal en commandoregel-shell voor Windows, biedt het cmdlet **Get-FileHash**, waarmee gebruikers moeiteloos de hash van een bestand kunnen berekenen.

### De SHA256-hash verkrijgen

Volg deze eenvoudige stappen om de hash** van een bestand te verkrijgen met PowerShell:

1. Start PowerShell door het **Startmenu** te openen, te zoeken naar **PowerShell** en **Windows PowerShell** te selecteren.
2. Navigeer naar de directory waar het bestand zich bevindt. Gebruik de `cd` commando gevolgd door het pad naar de directory.
3. Voer het volgende commando uit om de SHA256 hash van het bestand te verkrijgen:
```powershell
   Get-FileHash -Algorithm SHA256 -Path "file_path"
```
### De MD5- en SHA1-hashes verkrijgen
U kunt ook de `MD5` en `SHA1` hashes van een bestand met behulp van PowerShell. Gebruik de volgende commando's:

- Om de `MD5 hash`
  
```powershell
Get-FileHash -Algorithm MD5 -Path "file_path"
```

- Om de `SHA1 hash`

```powershell
Get-FileHash -Algorithm SHA1 -Path "file_path"
```

Vergeet niet in beide commando's "file_path" te vervangen door het pad naar uw bestand.

## Voorbeelden
Laten we ons verdiepen in specifieke voorbeelden om het proces van het verkrijgen van hashes met PowerShell onder Windows te illustreren.

{{< youtube id="UrHhsF1q3rU" >}}

### Voorbeeld 1: SHA256 Hash verkrijgen
Stel u heeft een bestand met de naam `document.pdf` in de directory `C:\Files` Om de `SHA256 hash` van dit bestand met behulp van PowerShell, voer het volgende commando uit:

```powershell
Get-FileHash -Algorithm SHA256 -Path "C:\Files\document.pdf"
```

De uitvoer toont de SHA256 hash-waarde van het bestand.

### Voorbeeld 2: MD5-hash verkrijgen

Stel, u bezit een bestand met de naam `image.jpg` opgeslagen in de directory `C:\Photos` Om de `MD5 hash` van dit bestand met behulp van PowerShell, voer het volgende commando uit:

```powershell
Get-FileHash -Algorithm MD5 -Path "C:\Photos\image.jpg"
```

De terminal toont de MD5-hashwaarde van het bestand.

### Voorbeeld 3: SHA1-hash verkrijgen

Beschouw een scenario waarin u een bestand hebt met de naam `data.txt` in de directory `C:\Documents` Om de `SHA1 hash` van dit bestand met behulp van PowerShell, voer het volgende commando uit:

```powershell
Get-FileHash -Algorithm SHA1 -Path "C:\Documents\data.txt"
```

De uitvoer toont de SHA1 hash-waarde van het bestand.