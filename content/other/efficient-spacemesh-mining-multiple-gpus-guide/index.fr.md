---
title: "Exploitation efficace de Spacemesh avec plusieurs GPU - Maximisez vos gains"
date: 2023-08-18
toc: true
draft: false
description: "Apprenez à optimiser votre exploitation minière de Spacemesh en utilisant plusieurs GPU avec l'algorithme PoST respectueux de l'environnement et maximisez vos récompenses."
genre: ["Crypto-monnaie", "Blockchain", "Exploitation minière", "Technologie", "Décentralisé", "Exploitation minière du GPU", "Preuve de l'espace-temps", "Respect de l'environnement", "Conseils sur les cryptomonnaies", "Actifs numériques"]
tags: ["Spacemesh", "Exploitation minière", "GPU", "Preuve de l'espace-temps", "Crypto-monnaie", "Blockchain", "Respect de l'environnement", "Décentralisé", "Algorithme PoST", "Guide de l'exploitation minière", "Conseils sur les cryptomonnaies", "Récompenses", "Optimisation", "Efficacité énergétique", "Exploitation minière du GPU", "Actifs numériques", "Technologie", "Décentralisation", "Preuve d'espace", "Exploitation minière de l'espace-temps", "Maximiser l'efficacité de l'exploitation minière", "Crypto-monnaie écologique", "Réseau Spacemesh", "Configuration de l'exploitation minière par GPU", "Exploitation minière avec plusieurs GPU", "Exploitation minière décentralisée de la blockchain", "Conseils pour l'exploitation minière de cryptomonnaies", "Efficient GPU Mining", "Preuve de l'algorithme spatio-temporel", "Récompenses en crypto-monnaies"]
cover: "/img/cover/spacemesh-mining-gpus.png"
coverAlt: "Illustration de style bande dessinée montrant plusieurs GPU travaillant ensemble pour exploiter Spacemesh."
coverCaption: "Mine Smarter, Mine Greener !"
---
 Introduction

Spacemesh est une plateforme de crypto-monnaie révolutionnaire qui utilise un algorithme de consensus économe en énergie connu sous le nom de "Proof of Space-Time" (PoST) pour le minage, présentant une alternative écologique aux crypto-monnaies traditionnelles de type Proof of Work (PoW) comme le Bitcoin. Si vous disposez de plusieurs GPU et que vous êtes intéressé par le minage de Spacemesh, ce guide complet vous guidera à travers le processus de maximisation de votre potentiel de minage en utilisant la puissante application postcli.

## Prérequis

Avant de plonger dans le processus d'exploitation minière, assurez-vous d'avoir les prérequis suivants en place :

1. **Multiples GPUs:** Assurez-vous d'avoir au moins deux GPUs capables de gérer efficacement le minage de Spacemesh.

2. **Application postcli:** Téléchargez l'application postcli à partir de [here](https://github.com/spacemeshos/post/) et assurez-vous qu'il est correctement installé et disponible dans le chemin d'accès à l'environnement de votre système.

## Exploiter Spacemesh avec plusieurs GPU

Pour commencer à exploiter Spacemesh avec plusieurs GPU, suivez ces étapes simples :

______

{{< inarticle-dark >}}

### Étape 1 : Configuration des variables

Ouvrez un éditeur de texte ou un éditeur de script PowerShell et définissez les variables configurables en fonction de vos besoins.
Le script fourni comprend déjà quelques variables que vous pouvez ajuster, mais le reste peut être tiré du fichier json que vous obtenez lorsque vous lancez le smeshing sur l'application GUI de spacemech :

- `$numGpus` Définissez le nombre de GPU que vous souhaitez utiliser pour l'exploitation minière. Par exemple, `2` pour deux GPU.

- `$commitmentAtxId` Remplacez-le par l'identifiant ATX de votre engagement, un identifiant unique pour votre engagement à participer au réseau Spacemesh.

- `$nodeId` Remplacez-le par votre Node ID, un identifiant unique pour votre nœud sur le réseau Spacemesh.

- `$LabelsPerUnit` Définir le nombre d'étiquettes par unité de stockage. La valeur par défaut est 4294967296.

- `$MaxFileSize` Définir la taille maximale du fichier. La valeur par défaut est 2147483648.

- `$numUnits` Définir le nombre d'unités de stockage à exploiter. La valeur par défaut est 16.

- `$datadir` Définissez le chemin d'accès au répertoire de données dans lequel vos données minières seront stockées.

{{< inarticle-dark >}}

### Étape 2 : Exécuter le script

Enregistrez le script avec les variables définies et exécutez-le dans PowerShell. Le script répartira automatiquement la charge de travail d'extraction entre les GPU spécifiés, optimisant ainsi l'efficacité de l'extraction.

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

### Étape 3 : Contrôler les progrès de l'exploitation minière

Une fois le script exécuté, vous pouvez surveiller la progression du minage. L'application postcli commencera à utiliser les GPU spécifiés pour miner Spacemesh à l'aide de l'algorithme PoST. Chaque GPU se verra attribuer une plage spécifique d'unités de stockage afin de garantir une répartition équitable du travail.

______

## Conclusion

Le minage de Spacemesh avec plusieurs GPU est un moyen efficace de contribuer au réseau tout en maximisant le potentiel de votre matériel. En utilisant le script PowerShell fourni avec l'application postcli, vous pouvez miner Spacemesh de manière transparente en utilisant l'algorithme PoST sans les calculs énergivores requis par les crypto-monnaies basées sur PoW.

N'oubliez pas de maintenir votre application postcli à jour et de rester informé de tout changement ou mise à jour du réseau Spacemesh. Bonne exploitation minière !

## Références

1. [Spacemesh Official Website](https://spacemesh.io/)
2. [Spacemesh GitHub Repository](https://github.com/spacemeshos/)
3. [Spacemesh POST CLI Application](https://github.com/spacemeshos/post)
