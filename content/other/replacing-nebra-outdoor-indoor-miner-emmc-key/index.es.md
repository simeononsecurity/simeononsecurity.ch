---
title: "Reemplazando la Tarjeta SD de Nebra Helium Miner: Guía Paso a Paso"
draft: false
toc: true
date: 2022-02-13
description: "Aprenda a reemplazar o actualizar la tarjeta SD EMMC Key de Nebra Indoor y Outdoor, Primera y Segunda generación, y solucione los problemas de sincronización de Helium Miner con esta guía."
genre: ["Tecnología", "Criptomoneda", "Hardware", "Extracción de helio", "Solución de problemas", "Sustitución de tarjetas SD", "Problemas de sincronización", "Raspberry Pi", "Balena Etcher", "Minero de helio Nebra"]
tags: ["Minero de helio Nebra", "Sustitución de tarjetas SD", "Problemas de sincronización", "Extracción de helio", "Solución de problemas", "Raspberry Pi", "Balena Etcher", "Guía de hardware", "Actualización de tarjeta SD", "Resolución de problemas de sincronización", "Guía paso a paso", "Helium Miner Sync Fix", "Minero de interior Nebra", "Nebra Outdoor Miner", "Raspberry Pi Compute Módulo 3", "Balena Raspberry Pi CM3 Imagen", "Resolución de problemas de los mineros de helio", "Nebra Mining Equipment", "Programa Balena Etcher", "Sustitución de la llave EMMC en Nebra Miner", "Reparación de tarjetas SD para Helium Miner", "Solución de problemas de sincronización de Helium Miner", "Reemplazo de la tarjeta SD de Nebra Miner", "Guía para la resolución de problemas de Nebra Helium Miner", "Consejos para extraer helio", "Actualización de la tarjeta SD de Nebra Helium Miner", "Cómo desinfectar la tarjeta SD de Nebra Miner", "Solución de problemas de sincronización de Nebra Helium Miner"]
cover: "/img/cover/A_cartoon_illustration_of_a_person_holding_a_Nebra_Helium_M.png"
coverAlt: "Una ilustración de dibujos animados de una persona que sostiene un Nebra Helium Miner con un panel abierto que revela la ranura para tarjetas SD y los pasos de la guía que aparecen como una guía flotando por encima del dispositivo."
coverCaption: "Resuelve problemas de sincronización y actualiza tu Helium Miner con facilidad."
---

**Sustitución y reimagen de la llave EMMC / tarjeta SD de Nebra para interiores y exteriores**

Esta completa guía le guiará a través del proceso de sustitución o re-flasheo de la llave EMMC de Nebra Indoor y Outdoor / Tarjeta SD. Siguiendo estos pasos, puede resolver los problemas de sincronización con su Helium Miner y asegurar un funcionamiento sin problemas. La guía proporciona una explicación detallada de las herramientas y el software que necesitará, así como los pasos necesarios para adquirir el archivo config.json, flashear la nueva tarjeta SD utilizando Balena Raspberry Pi CM3 Image, y transferir el archivo config original a la nueva tarjeta SD.

## Introducción

Los Nebra Helium Miners, tanto el modelo Indoor como el Outdoor, dependen de la llave EMMC/Tarjeta SD para su funcionamiento. Con el tiempo, puede ser necesario reemplazar o actualizar esta tarjeta para solucionar problemas de sincronización y mantener un rendimiento óptimo. Esta guía le proporcionará los conocimientos e instrucciones necesarios para llevar a cabo esta tarea de forma eficaz.

Para reemplazar con éxito la tarjeta SD del Nebra Helium Miner, necesitará herramientas específicas y software. Las herramientas incluyen un destornillador de cabeza Phillips o [Allen Key Set](https://amzn.to/34SlnOS) (depending on the model), a [Micro SD Card Reader](https://amzn.to/3Jl3U0w), a [64GB A2 micro SD card](https://amzn.to/3oJtTqs) (or larger), and a [Micro USB 2.0 Cable](https://amzn.to/3LxXYmA). The essential software needed for this process includes [Balena Etcher](https://www.balena.io/etcher/), Balena Raspberry Pi Image, and [Raspberry Pi USB Boot](https://github.com/raspberrypi/usbboot/raw/master/win32/rpiboot_setup.exe) Con estos recursos a mano, estarás listo para proceder al reemplazo o reflasheo de la tarjeta SD.

## Herramientas necesarias:
- Un destornillador de cabeza Phillips o [plastic pry bar](https://amzn.to/3rLXVfc) for the Nebra Indoor Miner or [allen key set](https://amzn.to/34SlnOS) para Nebra Outdoor Miner
- Uñas fuertes, pinzas o alicates de punta fina para extraer la tarjeta SD antigua
- [A Micro SD Card Reader](https://amzn.to/3Jl3U0w)
- [A 64gb (or larger) A2 micro sd card](https://amzn.to/3oJtTqs)
- [A Micro USB 2.0 Cable](https://amzn.to/3LxXYmA)
## Software requerido:
- [Balena Etcher](https://www.balena.io/etcher/)
- [Raspberry Pi USB Boot](https://github.com/raspberrypi/usbboot/raw/master/win32/rpiboot_setup.exe)
- Última imagen de Nebra para su dispositivo específico:
*Si no sabe qué dispositivo tiene, consulte el [nebra documentatio](https://support.nebra.com/support/home) Si es más antiguo, es bastante seguro asumir que tienes un dispositivo de primera generación.*
  - [Nebra Outdoor 2](https://github.com/NebraLtd/helium-nebra-outdoor2/releases/)
  - [Nebra Indoor 2](https://github.com/NebraLtd/helium-nebra-indoor2/releases/)
  - [Nebra Outdoor 1](https://github.com/NebraLtd/helium-nebra-outdoor1/releases)
  - [Nebra Indoor 1](https://github.com/NebraLtd/helium-nebra-indoor1/releases)

### Dentro del Minador de Helio Nebra:
### Contenido del Nebra Indoor Miner:
{{< figure src="Indoor-internal-lights.png" alt="Nebra Indoor Miner" >}}
### Contenido del Nebra Outdoor Miner:
{{< figure src="Inside-Interfaces.jpg" alt="Nebra Outdoor Miner" >}}
 - 1.) 9-16V @ 15W DC 6.5MMx2.0MM Barrel Jack
 - 2.) Conector Ethernet
 - 3.) Indicador LED
 - 4.) Botón de interfaz
 - 5.) Conector del módulo 4G / LTE
 - 6.) Ranura para tarjeta SIM

## Cómo reemplazar la Tarjeta SD
### Paso 1: Opcionalmente adquirir el archivo config.json de la llave EMMC:
- Descargar e instalar [Raspberry Pi USB Boot](https://github.com/raspberrypi/usbboot/raw/master/win32/rpiboot_setup.exe) usted necesitará esto para arrancar el módulo de cómputo como un sistema de archivos usb
- Identifique y ajuste los pines del puente en la tarjeta secundaria CM3 para el modo de programación
 - {{< figure src="daughterboardBreakdown.png" alt="Nebra Daughterboard Overview" >}}
   - 5.) Puerto Micro USB utilizado para imágenes
   - 7.) JP4 USB Jumper - Se utiliza para cambiar entre el funcionamiento normal y el modo flash, asegúrese de que está en la posición 1-2 para el funcionamiento normal y 2-3 para la programación.
   - 8.) JP3 Power Jumper - Permite alimentar el módulo desde el conector Micro USB. Conéctelo sólo cuando programe desde el PC y asegúrese de que la placa base no está conectada.
 - Mueva el Jumper JP4 a la posición 2+3
 - Conecte un cable usb y pase el [Raspberry Pi USB Boot](https://github.com/raspberrypi/usbboot/raw/master/win32/rpiboot_setup.exe) utilidad
 - Abra su explorador de archivos y verá una unidad llamada "resin-boot". Recupera el archivo "config.json" del directorio, puede que lo necesites más adelante y debería estar respaldado.
 - Desenchufa el cable usb y reinicia el jumper JP4 a la posición 1+2
### Paso 2: Flashear la nueva tarjeta sd con la imagen Balena Raspberry Pi CM3:
- Descarga y extrae la imagen apropiada
  - [Nebra Outdoor 2](https://github.com/NebraLtd/helium-nebra-outdoor2/releases/)
  - [Nebra Indoor 2](https://github.com/NebraLtd/helium-nebra-indoor2/releases/)
  - [Nebra Outdoor 1](https://github.com/NebraLtd/helium-nebra-outdoor1/releases)
  - [Nebra Indoor 1](https://github.com/NebraLtd/helium-nebra-indoor1/releases)
- Utilización [Balena Etcher](https://www.balena.io/etcher/) seleccione el archivo .img recién extraído y su nueva tarjeta microsd como dispositivo de destino
- Seleccione Flash
### Paso 3: Instale la nueva tarjeta sd y vuelva a montar el Nebra Miner:
 - Instale la tarjeta SD en la ranura en la que estaba anteriormente la llave EMMC.
 - Reensamble el minero
 - Cuando encienda por primera vez el Nebra Miner recién flasheado, conéctelo con ethernet durante 20-30 minutos antes de volver a establecer conexiones wifi.
### Paso 4: ¿Ganancias?




