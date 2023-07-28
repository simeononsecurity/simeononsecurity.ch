---
title: "Exploatarea eficientă a Spacemesh cu mai multe GPU-uri - Maximizează-ți recompensa"
date: 2023-08-18
toc: true
draft: false
description: "Aflați cum să vă optimizați mineritul Spacemesh folosind mai multe GPU-uri cu ajutorul algoritmului PoST ecologic și să vă maximizați recompensele."
genre: ["Criptomonedă", "Blockchain", "Minerit", "Tehnologie", "Descentralizat", "GPU Mining", "Dovada spațiului-timp", "Ecologic", "Sfaturi Crypto", "Activele digitale"]
tags: ["Spacemesh", "Minerit", "GPU-uri", "Dovada spațiului-timp", "Criptomonedă", "Blockchain", "Ecologic", "Descentralizat", "Algoritmul PoST", "Ghidul minier", "Sfaturi Crypto", "Recompense", "Optimizare", "Eficiență energetică", "GPU Mining", "Activele digitale", "Tehnologie", "Descentralizare", "Dovada de spațiu", "Mineritul spațiu-timp", "Maximizarea eficienței miniere", "Criptomonedă ecologică", "Rețeaua Spacemesh", "GPU Mining Setup", "Mineritul cu mai multe GPU-uri", "Minerit descentralizat Blockchain", "Sfaturi Crypto Mining", "Minerit eficient pe GPU", "Dovada algoritmului spațiu-timp", "Recompense pentru criptomonede"]
cover: "/img/cover/spacemesh-mining-gpus.png"
coverAlt: "O ilustrație în stil de desen animat care arată mai multe GPU-uri care lucrează împreună pentru a extrage Spacemesh."
coverCaption: "Mine Smarter, Mine Greener!"
---
 Introducere

Spacemesh este o platformă revoluționară de criptomonede care utilizează un algoritm de consens eficient din punct de vedere energetic cunoscut sub numele de "Proof of Space-Time" (PoST) pentru minerit, prezentând o alternativă ecologică la criptomonedele tradiționale de tip Proof of Work (PoW), precum Bitcoin. Dacă aveți mai multe GPU-uri și sunteți interesat să mineriți Spacemesh, acest ghid cuprinzător vă va conduce prin procesul de maximizare a potențialului de minerit folosind puternica aplicație postcli.

## Condiții prealabile

Înainte de a vă scufunda în procesul de minerit, asigurați-vă că aveți următoarele condiții prealabile:

1. **Multiple GPU-uri:** Asigurați-vă că aveți cel puțin două GPU-uri capabile să gestioneze eficient minarea Spacemesh.

2. **aplicația postcli:** Descărcați aplicația postcli de la [here](https://github.com/spacemeshos/post/) și asigurați-vă că este instalat corect și disponibil în calea de mediu a sistemului dumneavoastră.

## Exploatarea Spacemesh cu mai multe GPU-uri

Pentru a începe să mineriți Spacemesh cu mai multe GPU-uri, urmează acești pași simpli:

______

{{< inarticle-dark >}}

### Pasul 1: Configurarea variabilelor

Deschideți un editor de text sau un editor de script PowerShell și setați variabilele configurabile în funcție de cerințele dumneavoastră.
Scriptul furnizat include deja unele variabile pe care le puteți ajusta, dar restul pot fi extrase din fișierul json pe care îl primiți atunci când începeți smeshingul pe aplicația GUI spacemech:

- `$numGpus` Setați numărul de GPU-uri pe care doriți să le utilizați pentru minerit. De exemplu, `2` pentru două GPU.

- `$commitmentAtxId` Înlocuiți acest câmp cu ID-ul ATX al angajamentului dumneavoastră, un identificator unic pentru angajamentul dumneavoastră de a participa la rețeaua Spacemesh.

- `$nodeId` Înlocuiți acest câmp cu ID-ul dvs. de nod, un identificator unic pentru nodul dvs. în rețeaua Spacemesh.

- `$LabelsPerUnit` Setați numărul de etichete pe unitate de stocare. Valoarea implicită este 4294967296.

- `$MaxFileSize` Setați dimensiunea maximă a fișierului. Valoarea implicită este 2147483648.

- `$numUnits` Setați numărul de unități de stocare care urmează să fie exploatate. Valoarea implicită este 16.

- `$datadir` Setați calea către directorul de date în care vor fi stocate datele de minerit.

{{< inarticle-dark >}}

### Pasul 2: Executarea scriptului

Salvați scriptul cu variabilele definite și executați-l în PowerShell. Scriptul va împărți automat volumul de muncă de minerit între GPU-urile specificate, optimizând eficiența mineritului.

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

### Pasul 3: Monitorizarea progresului minier

Odată ce scriptul rulează, puteți monitoriza progresul mineritului. Aplicația postcli va începe să utilizeze GPU-urile specificate pentru a mina Spacemesh folosind algoritmul PoST. Fiecărui GPU i se va atribui un anumit interval de unități de stocare pentru a asigura o distribuție echitabilă a muncii.

______

## Concluzie

Mineritul Spacemesh cu mai multe GPU-uri este o modalitate eficientă de a contribui la rețea, maximizând în același timp potențialul tău hardware. Prin utilizarea scriptului PowerShell furnizat, alături de aplicația postcli, puteți mina fără probleme Spacemesh folosind algoritmul PoST, fără calculele energofage necesare criptomonedelor bazate pe PoW.

Nu uitați întotdeauna să vă mențineți aplicația postcli actualizată și să rămâneți informat cu privire la orice modificări sau actualizări ale rețelei Spacemesh. Minare fericită!

## Referințe

1. [Spacemesh Official Website](https://spacemesh.io/)
2. [Spacemesh GitHub Repository](https://github.com/spacemeshos/)
3. [Spacemesh POST CLI Application](https://github.com/spacemeshos/post)
