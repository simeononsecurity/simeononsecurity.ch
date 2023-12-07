---
title: "Wydajne wydobywanie Spacemesh przy użyciu wielu układów GPU - zmaksymalizuj swoją nagrodę"
date: 2023-08-18
toc: true
draft: false
description: "Dowiedz się, jak zoptymalizować wydobywanie Spacemesh przy użyciu wielu procesorów graficznych z przyjaznym dla środowiska algorytmem PoST i zmaksymalizować swoje nagrody."
genre: ["Kryptowaluta", "Blockchain", "Górnictwo", "Technologia", "Zdecentralizowany", "GPU Mining", "Dowód czasoprzestrzeni", "Przyjazny dla środowiska", "Wskazówki dotyczące kryptowalut", "Zasoby cyfrowe"]
tags: ["Spacemesh", "Górnictwo", "Procesory graficzne", "Dowód czasoprzestrzeni", "Kryptowaluta", "Blockchain", "Przyjazny dla środowiska", "Zdecentralizowany", "Algorytm PoST", "Przewodnik górniczy", "Wskazówki dotyczące kryptowalut", "Nagrody", "Optymalizacja", "Efektywność energetyczna", "GPU Mining", "Zasoby cyfrowe", "Technologia", "Decentralizacja", "Dowód przestrzeni", "Górnictwo czasoprzestrzenne", "Maksymalizacja wydajności wydobycia", "Kryptowaluta przyjazna dla środowiska", "Sieć Spacemesh", "Konfiguracja GPU Mining", "Wydobywanie przy użyciu wielu procesorów graficznych", "Zdecentralizowane wydobycie blockchain", "Wskazówki dotyczące wydobywania kryptowalut", "Wydajne górnictwo na GPU", "Dowód algorytmu czasoprzestrzennego", "Nagrody kryptowalutowe"]
cover: "/img/cover/spacemesh-mining-gpus.png"
coverAlt: "Ilustracja w stylu kreskówki przedstawiająca wiele procesorów graficznych współpracujących ze sobą przy wydobywaniu Spacemesh."
coverCaption: "Mój mądrzejszy, mój bardziej ekologiczny!"
---
 Wprowadzenie

Spacemesh to przełomowa platforma kryptowalutowa, która wykorzystuje energooszczędny algorytm konsensusu znany jako "Proof of Space-Time" (PoST) do wydobywania, stanowiąc przyjazną dla środowiska alternatywę dla tradycyjnych kryptowalut Proof of Work (PoW), takich jak Bitcoin. Jeśli posiadasz wiele procesorów graficznych i jesteś zainteresowany wydobywaniem Spacemesh, ten kompleksowy przewodnik przeprowadzi Cię przez proces maksymalizacji potencjału wydobywczego przy użyciu potężnej aplikacji postcli.

## Wymagania wstępne

Przed rozpoczęciem procesu wydobywania należy upewnić się, że spełnione są następujące warunki wstępne:

1. **Wiele procesorów graficznych:** Upewnij się, że masz co najmniej dwa procesory graficzne zdolne do efektywnego wydobywania Spacemesh.

2. **Aplikacja postcli:** Pobierz aplikację postcli ze strony [here](https://github.com/spacemeshos/post/) i upewnić się, że jest poprawnie zainstalowany i dostępny w ścieżce środowiskowej systemu.

## Wydobywanie Spacemesh przy użyciu wielu GPU

Aby rozpocząć wydobywanie Spacemesh za pomocą wielu procesorów graficznych, wykonaj następujące proste kroki:

______

### Krok 1: Konfiguracja zmiennych

Otwórz edytor tekstu lub edytor skryptów PowerShell i ustaw konfigurowalne zmienne zgodnie ze swoimi wymaganiami.
Dostarczony skrypt zawiera już kilka zmiennych, które można dostosować, ale resztę można pobrać z pliku json, który otrzymasz po uruchomieniu smeshingu w aplikacji spacemech GUI:

- `$numGpus` Ustaw liczbę procesorów graficznych, które chcesz wykorzystać do wydobywania. Na przykład, `2` dla dwóch procesorów graficznych.

- `$commitmentAtxId` W to miejsce wpisz ATX ID swojego zobowiązania, unikalny identyfikator zobowiązania do uczestnictwa w sieci Spacemesh.

- `$nodeId` Zastąp to swoim Node ID, unikalnym identyfikatorem węzła w sieci Spacemesh.

- `$LabelsPerUnit` Ustaw liczbę etykiet na jednostkę pamięci. Wartość domyślna to 4294967296.

- `$MaxFileSize` Ustaw maksymalny rozmiar pliku. Wartość domyślna to 2147483648.

- `$numUnits` Ustaw liczbę jednostek pamięci do wydobycia. Domyślną wartością jest 16.

- `$datadir` Ustaw ścieżkę do katalogu danych, w którym będą przechowywane dane wydobywcze.

### Krok 2: Wykonanie skryptu

Zapisz skrypt ze zdefiniowanymi zmiennymi i wykonaj go w PowerShell. Skrypt automatycznie podzieli obciążenie wydobywcze pomiędzy określone układy GPU, optymalizując wydajność wydobycia.

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

### Krok 3: Monitorowanie postępów wydobycia

Po uruchomieniu skryptu można monitorować postęp wydobycia. Aplikacja postcli zacznie wykorzystywać określone układy GPU do wydobywania Spacemesh przy użyciu algorytmu PoST. Każdemu procesorowi GPU zostanie przypisany określony zakres jednostek pamięci, aby zapewnić sprawiedliwy podział pracy.

______

## Wnioski

Wydobywanie Spacemesh za pomocą wielu procesorów graficznych to skuteczny sposób na wniesienie wkładu do sieci przy jednoczesnej maksymalizacji potencjału sprzętowego. Wykorzystując dostarczony skrypt PowerShell wraz z aplikacją postcli, można płynnie wydobywać Spacemesh przy użyciu algorytmu PoST bez energochłonnych obliczeń wymaganych przez kryptowaluty oparte na PoW.

Zawsze pamiętaj, aby aktualizować aplikację postcli i być na bieżąco z wszelkimi zmianami lub aktualizacjami sieci Spacemesh. Udanego wydobycia!

## Referencje

1. [Spacemesh Official Website](https://spacemesh.io/)
2. [Spacemesh GitHub Repository](https://github.com/spacemeshos/)
3. [Spacemesh POST CLI Application](https://github.com/spacemeshos/post)
