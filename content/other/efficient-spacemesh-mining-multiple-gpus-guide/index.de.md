---
title: "Effizientes Spacemesh Mining mit mehreren GPUs - Maximieren Sie Ihre Belohnung"
date: 2023-08-18
toc: true
draft: false
description: "Erfahren Sie, wie Sie Ihr Spacemesh-Mining mit mehreren GPUs und dem umweltfreundlichen PoST-Algorithmus optimieren und Ihre Gewinne maximieren können."
genre: ["Kryptowährung", "Blockchain", "Bergbau", "Technologie", "Dezentralisiert", "GPU-Bergbau", "Beweis der Raum-Zeit", "Umweltfreundlich", "Krypto-Tipps", "Digitale Vermögenswerte"]
tags: ["Raumnetz", "Bergbau", "GPUs", "Beweis der Raum-Zeit", "Kryptowährung", "Blockchain", "Umweltfreundlich", "Dezentralisiert", "PoST-Algorithmus", "Bergbau-Leitfaden", "Krypto-Tipps", "Belohnungen", "Optimierung", "Energieeffizient", "GPU-Bergbau", "Digitale Vermögenswerte", "Technologie", "Dezentralisierung", "Nachweis des Weltraums", "Raum-Zeit-Bergbau", "Maximierung der Effizienz des Bergbaus", "Umweltfreundliche Kryptowährung", "Spacemesh-Netzwerk", "GPU-Bergbaueinrichtung", "Mining mit mehreren GPUs", "Dezentrales Blockchain-Mining", "Krypto Mining Tipps", "Effizientes GPU-Mining", "Nachweis des Raum-Zeit-Algorithmus", "Belohnungen für Kryptowährungen"]
cover: "/img/cover/spacemesh-mining-gpus.png"
coverAlt: "Eine Illustration im Cartoon-Stil, die zeigt, wie mehrere GPUs zusammenarbeiten, um Spacemesh abzubauen."
coverCaption: "Mine Smarter, Mine Greener!"
---
 Einführung

Spacemesh ist eine bahnbrechende Kryptowährungsplattform, die für das Mining einen energieeffizienten Konsensalgorithmus verwendet, der als "Proof of Space-Time" (PoST) bekannt ist und eine umweltfreundliche Alternative zu traditionellen Proof of Work (PoW) Kryptowährungen wie Bitcoin darstellt. Wenn Sie über mehrere Grafikprozessoren verfügen und Interesse am Mining von Spacemesh haben, führt Sie dieser umfassende Leitfaden durch den Prozess der Maximierung Ihres Mining-Potenzials mithilfe der leistungsstarken Anwendung postcli.

## Voraussetzungen

Bevor Sie in den Mining-Prozess einsteigen, sollten Sie sicherstellen, dass Sie die folgenden Voraussetzungen erfüllt haben:

1. **Mehrere GPUs:** Stellen Sie sicher, dass Sie mindestens zwei GPUs haben, die in der Lage sind, Spacemesh-Mining effektiv zu betreiben.

2. **postcli-Anwendung:** Laden Sie die postcli-Anwendung von [here](https://github.com/spacemeshos/post/) und stellen Sie sicher, dass es korrekt installiert und im Umgebungspfad Ihres Systems verfügbar ist.

## Mining Spacemesh mit mehreren GPUs

Um mit dem Mining von Spacemesh mit mehreren GPUs zu beginnen, folgen Sie diesen einfachen Schritten:

______

{{< inarticle-dark >}}

### Schritt 1: Variablen konfigurieren

Öffnen Sie einen Texteditor oder einen PowerShell-Skripteditor und stellen Sie die konfigurierbaren Variablen entsprechend Ihren Anforderungen ein.
Das mitgelieferte Skript enthält bereits einige Variablen, die Sie anpassen können, aber der Rest kann aus der json-Datei gezogen werden, die Sie erhalten, wenn Sie das Smeshing auf der spacemech GUI-Anwendung starten:

- `$numGpus` Legen Sie die Anzahl der GPUs fest, die Sie für das Mining verwenden möchten. Zum Beispiel, `2` für zwei GPUs.

- `$commitmentAtxId` Ersetzen Sie dies durch Ihre ATX-ID, eine eindeutige Kennung für Ihre Zusage zur Teilnahme am Spacemesh-Netzwerk.

- `$nodeId` Ersetzen Sie dies durch Ihre Node-ID, eine eindeutige Kennung für Ihren Knoten im Spacemesh-Netzwerk.

- `$LabelsPerUnit` Legen Sie die Anzahl der Etiketten pro Speichereinheit fest. Der Standardwert ist 4294967296.

- `$MaxFileSize` Legen Sie die maximale Dateigröße fest. Der Standardwert ist 2147483648.

- `$numUnits` Legen Sie die Anzahl der zu fördernden Speichereinheiten fest. Der Standardwert ist 16.

- `$datadir` Legen Sie den Pfad zum Datenverzeichnis fest, in dem Ihre Mining-Daten gespeichert werden sollen.

{{< inarticle-dark >}}

### Schritt 2: Ausführen des Skripts

Speichern Sie das Skript mit den definierten Variablen und führen Sie es in PowerShell aus. Das Skript wird die Mining-Arbeitslast automatisch auf die angegebenen GPUs aufteilen und so die Mining-Effizienz optimieren.

#### Fenster

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

### Schritt 3: Überwachung des Abbaufortschritts

Sobald das Skript läuft, können Sie den Fortschritt des Abbaus überwachen. Die postcli-Anwendung beginnt mit der Nutzung der angegebenen GPUs zum Abbau von Spacemesh unter Verwendung des PoST-Algorithmus. Jeder GPU wird ein bestimmter Bereich von Speichereinheiten zugewiesen, um eine faire Verteilung der Arbeit zu gewährleisten.

______

## Schlussfolgerung

Das Mining von Spacemesh mit mehreren GPUs ist ein effizienter Weg, um zum Netzwerk beizutragen und gleichzeitig das eigene Hardware-Potenzial zu maximieren. Durch den Einsatz des mitgelieferten PowerShell-Skripts zusammen mit der postcli-Anwendung können Sie Spacemesh nahtlos mit dem PoST-Algorithmus minen, ohne die energieintensiven Berechnungen, die für PoW-basierte Kryptowährungen erforderlich sind.

Denken Sie immer daran, Ihre postcli-Anwendung auf dem neuesten Stand zu halten und über alle Änderungen oder Aktualisierungen des Spacemesh-Netzwerks informiert zu bleiben. Viel Spaß beim Mining!

## Referenzen

1. [Spacemesh Official Website](https://spacemesh.io/)
2. [Spacemesh GitHub Repository](https://github.com/spacemeshos/)
3. [Spacemesh POST CLI Application](https://github.com/spacemeshos/post)
