---
title: "Estrazione efficiente di Spacemesh con più GPU - massimizzate i vostri guadagni"
date: 2023-08-18
toc: true
draft: false
description: "Scoprite come ottimizzare il mining di Spacemesh utilizzando più GPU con l'algoritmo ecologico PoST e massimizzare i vostri guadagni."
genre: ["Criptovalute", "Blockchain", "Miniere", "Tecnologia", "Decentrato", "Estrazione di GPU", "Prova dello spazio-tempo", "Eco-compatibile", "Suggerimenti per le criptovalute", "Beni digitali"]
tags: ["Maglia spaziale", "Miniere", "GPU", "Prova dello spazio-tempo", "Criptovalute", "Blockchain", "Eco-compatibile", "Decentrato", "Algoritmo PoST", "Guida alle miniere", "Suggerimenti per le criptovalute", "Premi", "Ottimizzazione", "Efficienza energetica", "Estrazione di GPU", "Beni digitali", "Tecnologia", "Decentramento", "Prova dello spazio", "Estrazione spazio-temporale", "Massimizzare l'efficienza mineraria", "Criptovaluta ecologica", "Rete Spacemesh", "Configurazione per il mining su GPU", "Estrazione con più GPU", "Estrazione decentralizzata su blockchain", "Suggerimenti per l'estrazione di criptovalute", "Estrazione efficiente su GPU", "Prova dell'algoritmo spazio-tempo", "Premi in criptovaluta"]
cover: "/img/cover/spacemesh-mining-gpus.png"
coverAlt: "Un'illustrazione in stile cartone animato che mostra più GPU che lavorano insieme per estrarre Spacemesh."
coverCaption: "Più intelligente, più verde!"
---
 Introduzione

Spacemesh è una piattaforma di criptovaluta innovativa che impiega un algoritmo di consenso ad alta efficienza energetica noto come "Proof of Space-Time" (PoST) per il mining, presentando un'alternativa ecologica alle tradizionali criptovalute Proof of Work (PoW) come Bitcoin. Se avete più GPU e siete interessati al mining di Spacemesh, questa guida completa vi guiderà attraverso il processo di massimizzazione del vostro potenziale di mining utilizzando la potente applicazione postcli.

## Prerequisiti

Prima di immergersi nel processo di mining, assicurarsi di disporre dei seguenti prerequisiti:

1. **Assicuratevi di avere almeno due GPU in grado di gestire efficacemente il mining Spacemesh.

2. **Applicazione postcli:** Scaricare l'applicazione postcli da [here](https://github.com/spacemeshos/post/) e assicurarsi che sia correttamente installato e disponibile nel percorso dell'ambiente del sistema.

## Estrazione di Spacemesh con più GPU

Per iniziare il mining di Spacemesh con più GPU, seguite questi semplici passaggi:

______

{{< inarticle-dark >}}

### Passo 1: Configurazione delle variabili

Aprire un editor di testo o un editor di script PowerShell e impostare le variabili configurabili in base alle proprie esigenze.
Lo script fornito include già alcune variabili che si possono regolare, ma il resto può essere estratto dal file json che si ottiene quando si avvia lo smeshing sull'applicazione GUI di spacemech:

- `$numGpus` Impostare il numero di GPU che si desidera utilizzare per il mining. Ad esempio, `2` per due GPU.

- `$commitmentAtxId` Sostituire con l'ID ATX dell'impegno, un identificativo unico per l'impegno a partecipare alla rete Spacemesh.

- `$nodeId` Sostituire questo valore con l'ID del nodo, un identificativo univoco del nodo sulla rete Spacemesh.

- `$LabelsPerUnit` Impostare il numero di etichette per unità di memorizzazione. Il valore predefinito è 4294967296.

- `$MaxFileSize` Imposta la dimensione massima del file. Il valore predefinito è 2147483648.

- `$numUnits` Impostare il numero di unità di archiviazione da estrarre. Il valore predefinito è 16.

- `$datadir` Impostare il percorso della directory dei dati in cui saranno memorizzati i dati di mining.

{{< inarticle-dark >}}

### Passo 2: Esecuzione dello script

Salvare lo script con le variabili definite ed eseguirlo in PowerShell. Lo script dividerà automaticamente il carico di lavoro del mining tra le GPU specificate, ottimizzando l'efficienza del mining.

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

### Fase 3: Monitorare i progressi dell'attività estrattiva

Una volta che lo script è in esecuzione, è possibile monitorare l'avanzamento del mining. L'applicazione postcli inizierà a utilizzare le GPU specificate per estrarre Spacemesh utilizzando l'algoritmo PoST. A ogni GPU verrà assegnata una gamma specifica di unità di storage per garantire una distribuzione equa del lavoro.

______

## Conclusione

Il mining di Spacemesh con più GPU è un modo efficiente per contribuire alla rete massimizzando il proprio potenziale hardware. Utilizzando lo script PowerShell fornito insieme all'applicazione postcli, è possibile minare Spacemesh senza problemi utilizzando l'algoritmo PoST senza i calcoli ad alto consumo energetico richiesti dalle criptovalute basate su PoW.

Ricordate sempre di mantenere aggiornata l'applicazione postcli e di rimanere informati su qualsiasi modifica o aggiornamento della rete Spacemesh. Buon mining!

## Riferimenti

1. [Spacemesh Official Website](https://spacemesh.io/)
2. [Spacemesh GitHub Repository](https://github.com/spacemeshos/)
3. [Spacemesh POST CLI Application](https://github.com/spacemeshos/post)
