---
title: "Efficiënt Spacemesh-minen met meerdere GPU's - Maximaliseer uw beloning"
date: 2023-08-18
toc: true
draft: false
description: "Leer hoe je Spacemesh mining kunt optimaliseren met behulp van meerdere GPU's met het milieuvriendelijke PoST-algoritme en maximaliseer je beloningen."
genre: ["Cryptocurrency", "Blockchain", "Mijnbouw", "Technologie", "Gedecentraliseerd", "GPU-mijnbouw", "Bewijs van ruimte-tijd", "Milieuvriendelijk", "Cryptotips", "Digitale activa"]
tags: ["Spacemesh", "Mijnbouw", "GPU's", "Bewijs van ruimte-tijd", "Cryptocurrency", "Blockchain", "Milieuvriendelijk", "Gedecentraliseerd", "PoST-algoritme", "Mijngids", "Cryptotips", "Beloningen", "Optimalisatie", "Energiezuinig", "GPU-mijnbouw", "Digitale activa", "Technologie", "Decentralisatie", "Bewijs van ruimte", "Ruimte-tijd mijnbouw", "Mijnefficiëntie maximaliseren", "Milieuvriendelijke cryptocurrency", "Spacemesh netwerk", "GPU Mijnbouw Opstelling", "Mijnen met meerdere GPU's", "Gedecentraliseerde blockchain-mijnbouw", "Crypto mijnbouw tips", "Efficiënte GPU-mijnbouw", "Bewijs van ruimte-tijd-algoritme", "Beloningen voor cryptocurrency"]
cover: "/img/cover/spacemesh-mining-gpus.png"
coverAlt: "Een illustratie in cartoonstijl die laat zien hoe meerdere GPU's samenwerken om Spacemesh te ontginnen."
coverCaption: "Mijn slimmer, mijn groener!"
---
 Inleiding

Spacemesh is een baanbrekend cryptocurrency platform dat gebruik maakt van een energiezuinig consensus algoritme bekend als "Proof of Space-Time" (PoST) voor mining, waarmee een milieuvriendelijk alternatief wordt geboden voor traditionele Proof of Work (PoW) cryptocurrencies zoals Bitcoin. Als je meerdere GPU's hebt en geïnteresseerd bent in het delven van Spacemesh, zal deze uitgebreide gids je door het proces leiden om je mijnbouwpotentieel te maximaliseren met behulp van de krachtige postcli-toepassing.

## Vereisten

Voordat je aan het mijnproces begint, moet je ervoor zorgen dat je aan de volgende voorwaarden voldoet:

1. **Meerdere GPU's:** Zorg ervoor dat je minstens twee GPU's hebt die Spacemesh mining effectief aankunnen.

2. **Postcli-toepassing:** Download de postcli-toepassing van [here](https://github.com/spacemeshos/post/) en zorg ervoor dat het correct is geïnstalleerd en beschikbaar is in het omgevingspad van je systeem.

## Spacemesh delven met meerdere GPU's

Volg deze eenvoudige stappen om te beginnen met het delven van Spacemesh met meerdere GPU's:

______

### Stap 1: Variabelen configureren

Open een teksteditor of PowerShell scripteditor en stel de configureerbare variabelen in volgens je vereisten.
Het meegeleverde script bevat al enkele variabelen die je kunt aanpassen, maar de rest kun je uit het json-bestand halen dat je krijgt als je smeshing start in de spacemech GUI-toepassing:

- `$numGpus` Stel het aantal GPU's in dat je wilt gebruiken voor mijnbouw. Bijvoorbeeld, `2` voor twee GPU's.

- `$commitmentAtxId` Vervang dit door uw ATX ID, een unieke identificatie voor uw verplichting om deel te nemen aan het Spacemesh netwerk.

- `$nodeId` Vervang dit door uw knooppunt-ID, een unieke identificatie voor uw knooppunt op het Spacemesh-netwerk.

- `$LabelsPerUnit` Stel het aantal labels per opslageenheid in. De standaardwaarde is 4294967296.

- `$MaxFileSize` Stel de maximale bestandsgrootte in. De standaardwaarde is 2147483648.

- `$numUnits` Stel het aantal opslageenheden in om te ontginnen. De standaardwaarde is 16.

- `$datadir` Stel het pad in naar de datamap waar je mijnbouwgegevens worden opgeslagen.

### Stap 2: Het script uitvoeren

Sla het script op met de gedefinieerde variabelen en voer het uit in PowerShell. Het script zal automatisch de mijnbouwbelasting verdelen over de opgegeven GPU's, waardoor de mijnbouwefficiëntie wordt geoptimaliseerd.

#### Windows

```powershell
## Configurable Variables
$numGpus = 2
$commitmentAtxId = ""
$nodeId = ""
$LabelsPerUnit = 4294967296
$MaxFileSize = 2147483648
$numUnits = 16
$datadir = "C:\root\post\data"

## Script
foreach ($gpuIndex in 0..($numGpus - 1)) {
    $fromFile = $gpuIndex * ($numUnits * 32 / $numGpus)
    $toFile = ($gpuIndex + 1) * ($numUnits * 32 / $numGpus) - 1
    
    Start-Process -NoNewWindow -FilePath "postcli" -ArgumentList "-provider $gpuIndex", "-commitmentAtxId", $commitmentAtxId, "-id", $nodeId, "-labelsPerUnit", $LabelsPerUnit, "-maxFileSize", $MaxFileSize , "-numUnits", $numUnits, "-datadir", $datadir, "-fromFile", $fromFile, "-toFile", $toFile
}
```

#### Linux
```bash
#!/bin/bash

# Configurable Variables
numGpus=2
commitmentAtxId=""
nodeId=""
LabelsPerUnit=4294967296
MaxFileSize=2147483648
numUnits=16
datadir="\root\post\data"

# Script
for ((gpuIndex=0; gpuIndex<numGpus; gpuIndex++)); do
    fromFile=$((gpuIndex * (numUnits * 32 / numGpus)))
    toFile=$(( (gpuIndex + 1) * (numUnits * 32 / numGpus) - 1 ))
    
    postcli -provider $gpuIndex -commitmentAtxId "$commitmentAtxId" -id "$nodeId" -labelsPerUnit $LabelsPerUnit -maxFileSize $MaxFileSize -numUnits $numUnits -datadir "$datadir" -fromFile $fromFile -toFile $toFile &
done
```
______

### Stap 3: De voortgang van de mijnbouw bewaken

Zodra het script draait, kunt u de voortgang van de mijnbouw controleren. De postcli-toepassing begint de opgegeven GPU's te gebruiken om Spacemesh te delven met behulp van het PoST-algoritme. Elke GPU krijgt een specifieke reeks opslageenheden toegewezen om een eerlijke verdeling van het werk te garanderen.

______

## Conclusie

Spacemesh delven met meerdere GPU's is een efficiënte manier om bij te dragen aan het netwerk en tegelijkertijd je hardwarepotentieel te maximaliseren. Door gebruik te maken van het meegeleverde PowerShell-script naast de postcli-toepassing kun je naadloos Spacemesh delven met behulp van het PoST-algoritme zonder de energie-intensieve berekeningen die nodig zijn voor PoW-gebaseerde cryptocurrencies.

Denk er altijd aan om je postcli-toepassing up-to-date te houden en op de hoogte te blijven van wijzigingen of updates van het Spacemesh-netwerk. Veel mijnbouwplezier!

## Referenties

1. [Spacemesh Official Website](https://spacemesh.io/)
2. [Spacemesh GitHub Repository](https://github.com/spacemeshos/)
3. [Spacemesh POST CLI Application](https://github.com/spacemeshos/post)
