---
title: "Minería Spacemesh eficiente con varias GPU: maximiza tu recompensa"
date: 2023-08-18
toc: true
draft: false
description: "Aprende a optimizar tu minería Spacemesh usando múltiples GPUs con el algoritmo PoST ecológico y maximiza tus recompensas."
genre: ["Criptomoneda", "Blockchain", "Minería", "Tecnología", "Descentralizado", "Minería en la GPU", "Prueba del espacio-tiempo", "Ecológico", "Consejos sobre criptomonedas", "Activos digitales"]
tags: ["Spacemesh", "Minería", "GPUs", "Prueba del espacio-tiempo", "Criptomoneda", "Blockchain", "Ecológico", "Descentralizado", "Algoritmo PoST", "Guía Minera", "Consejos sobre criptomonedas", "Recompensas", "Optimización", "Eficiencia energética", "Minería en la GPU", "Activos digitales", "Tecnología", "Descentralización", "Prueba del espacio", "Minería espacio-temporal", "Maximizar la eficiencia minera", "Criptomoneda ecológica", "Red Spacemesh", "Configuración de GPU Mining", "Minería con varias GPU", "Minería descentralizada de Blockchain", "Consejos para la minería de criptomonedas", "Minería eficiente en la GPU", "Prueba del algoritmo espacio-tiempo", "Recompensas de criptomonedas"]
cover: "/img/cover/spacemesh-mining-gpus.png"
coverAlt: "Ilustración de dibujos animados que muestra varias GPU trabajando juntas para minar Spacemesh."
coverCaption: "Más inteligente, más ecológico"
---
 Introducción

Spacemesh es una innovadora plataforma de criptomonedas que emplea un algoritmo de consenso energéticamente eficiente conocido como "Proof of Space-Time" (PoST) para el minado, presentando una alternativa ecológica a las criptomonedas tradicionales Proof of Work (PoW) como Bitcoin. Si tienes varias GPUs y estás interesado en minar Spacemesh, esta completa guía te guiará a través del proceso para maximizar tu potencial minero utilizando la potente aplicación postcli.

## Prerrequisitos

Antes de sumergirte en el proceso de minería, asegúrate de que tienes los siguientes requisitos previos:

1. **Asegúrate de que tienes al menos dos GPUs capaces de manejar la minería Spacemesh con eficacia.

2. **Aplicación postcli:** Descarga la aplicación postcli desde [here](https://github.com/spacemeshos/post/) y asegúrese de que está correctamente instalado y disponible en la ruta del entorno de su sistema.

## Minado de Spacemesh con varias GPUs

Para empezar a minar Spacemesh con múltiples GPUs, sigue estos sencillos pasos:

______

### Paso 1: Configurar variables

Abra un editor de texto o un editor de scripts PowerShell y establezca las variables configurables según sus necesidades.
El script proporcionado ya incluye algunas variables que puede ajustar, pero el resto se puede extraer del archivo json que se obtiene al iniciar smeshing en la aplicación spacemech GUI:

- `$numGpus` Establece el número de GPUs que quieres utilizar para minar. Por ejemplo, `2` para dos GPU.

- `$commitmentAtxId` Sustitúyalo por su ID ATX de compromiso, un identificador único de su compromiso de participación en la red Spacemesh.

- `$nodeId` Sustitúyelo por tu ID de nodo, un identificador único para tu nodo en la red Spacemesh.

- `$LabelsPerUnit` Establezca el número de etiquetas por unidad de almacenamiento. El valor por defecto es 4294967296.

- `$MaxFileSize` Establece el tamaño máximo del archivo. El valor por defecto es 2147483648.

- `$numUnits` Establece el número de unidades de almacenamiento a minar. El valor predeterminado es 16.

- `$datadir` Establezca la ruta del directorio de datos donde se almacenarán sus datos de minería.

### Paso 2: Ejecutar el Script

Guarde el script con las variables definidas y ejecútelo en PowerShell. El script dividirá automáticamente la carga de trabajo de minería entre las GPU especificadas, optimizando la eficiencia de la minería.

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

### Paso 3: Supervisar el progreso de la minería

Una vez ejecutado el script, puedes monitorizar el progreso de la minería. La aplicación postcli comenzará a utilizar las GPUs especificadas para minar Spacemesh utilizando el algoritmo PoST. A cada GPU se le asignará un rango específico de unidades de almacenamiento para garantizar una distribución equitativa del trabajo.

______

## Conclusión

Minar Spacemesh con varias GPU es una forma eficiente de contribuir a la red al tiempo que maximizas tu potencial de hardware. Empleando el script PowerShell proporcionado junto con la aplicación postcli, puedes minar Spacemesh sin problemas utilizando el algoritmo PoST sin los cálculos de alto consumo energético que requieren las criptomonedas basadas en PoW.

Recuerda siempre mantener tu aplicación postcli actualizada y estar informado sobre cualquier cambio o actualización de la red Spacemesh. ¡Feliz minería!

## Referencias

1. [Spacemesh Official Website](https://spacemesh.io/)
2. [Spacemesh GitHub Repository](https://github.com/spacemeshos/)
3. [Spacemesh POST CLI Application](https://github.com/spacemeshos/post)
