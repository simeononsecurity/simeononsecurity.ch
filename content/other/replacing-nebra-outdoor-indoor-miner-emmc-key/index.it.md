---
title: "Sostituzione della scheda SD di Nebra Helium Miner: Guida passo passo"
draft: false
toc: true
date: 2022-02-13
description: "Scopri come sostituire o riflashare la scheda SD Nebra Indoor e Outdoor, di prima e seconda generazione, EMMC Key e risolvere i problemi di sincronizzazione di Helium Miner con questa guida."
genre: ["Tecnologia", "Criptovalute", "Hardware", "Miniere di elio", "Risoluzione dei problemi", "Sostituzione della scheda SD", "Problemi di sincronizzazione", "Raspberry Pi", "Balena Etcher", "Minatore di elio Nebra"]
tags: ["Minatore di elio Nebra", "Sostituzione della scheda SD", "Problemi di sincronizzazione", "Miniere di elio", "Risoluzione dei problemi", "Raspberry Pi", "Balena Etcher", "Guida all'hardware", "Aggiornamento della scheda SD", "Risoluzione dei problemi di sincronizzazione", "Guida passo passo", "Correzione della sincronizzazione del minatore di elio", "Minatore interno Nebra", "Minatore esterno Nebra", "Modulo di calcolo Raspberry Pi 3", "Immagine Balena Raspberry Pi CM3", "Risoluzione dei problemi dei minatori di elio", "Attrezzatura mineraria Nebra", "Software Balena Etcher", "Sostituzione della chiave EMMC su Nebra Miner", "Riparazione della scheda SD per Helium Miner", "Correzione dei problemi di sincronizzazione di Helium Miner", "Sostituzione della scheda SD di Nebra Miner", "Guida alla risoluzione dei problemi di Nebra Helium Miner", "Suggerimenti per l'estrazione dell'elio", "Aggiornamento della scheda SD di Nebra Helium Miner", "Come reimpostare la scheda SD di Nebra Miner", "Risoluzione dei problemi di sincronizzazione di Nebra Helium Miner"]
cover: "/img/cover/A_cartoon_illustration_of_a_person_holding_a_Nebra_Helium_M.png"
coverAlt: "Illustrazione a fumetti di una persona che tiene in mano un Nebra Helium Miner con un pannello aperto che rivela lo slot per la scheda SD e i passi della guida che appaiono come una guida che fluttua sopra il dispositivo."
coverCaption: "Risolvete i problemi di sincronizzazione e aggiornate il vostro Helium Miner con facilità."
---

**Sostituzione e reimpostazione della chiave EMMC / scheda SD di Nebra Indoor e Outdoor**

Questa guida completa vi guiderà attraverso il processo di sostituzione o re-flashing della chiave EMMC/scheda SD di Nebra Indoor e Outdoor. Seguendo questi passaggi, è possibile risolvere i problemi di sincronizzazione con Helium Miner e garantire un funzionamento regolare. La guida fornisce una spiegazione dettagliata degli strumenti e del software necessari, nonché i passaggi necessari per acquisire il file config.json, eseguire il flash della nuova scheda SD utilizzando Balena Raspberry Pi CM3 Image e trasferire il file di configurazione originale sulla nuova scheda SD.

## Introduzione

I Nebra Helium Miner, sia i modelli Indoor che Outdoor, si affidano alla chiave EMMC/scheda SD per il loro funzionamento. Nel corso del tempo, potrebbe essere necessario sostituire o riflashare questa scheda per risolvere i problemi di sincronizzazione e mantenere le prestazioni ottimali. Questa guida vi fornirà le conoscenze e le istruzioni necessarie per eseguire questa operazione in modo efficace.

Per sostituire con successo la scheda SD di Nebra Helium Miner, sono necessari strumenti e software specifici. Gli strumenti comprendono un cacciavite a croce o un cacciavite a stella. [Allen Key Set](https://amzn.to/34SlnOS) (depending on the model), a [Micro SD Card Reader](https://amzn.to/3Jl3U0w), a [64GB A2 micro SD card](https://amzn.to/3oJtTqs) (or larger), and a [Micro USB 2.0 Cable](https://amzn.to/3LxXYmA). The essential software needed for this process includes [Balena Etcher](https://www.balena.io/etcher/), Balena Raspberry Pi Image, and [Raspberry Pi USB Boot](https://github.com/raspberrypi/usbboot/raw/master/win32/rpiboot_setup.exe) Con queste risorse a portata di mano, sarete pronti a procedere con la sostituzione o il re-flash della scheda SD.

## Strumenti necessari:
- Cacciavite a croce o [plastic pry bar](https://amzn.to/3rLXVfc) for the Nebra Indoor Miner or [allen key set](https://amzn.to/34SlnOS) per Nebra Outdoor Miner
- Unghie forti, pinzette o pinze ad ago per rimuovere la vecchia scheda SD
- [A Micro SD Card Reader](https://amzn.to/3Jl3U0w)
- [A 64gb (or larger) A2 micro sd card](https://amzn.to/3oJtTqs)
- [A Micro USB 2.0 Cable](https://amzn.to/3LxXYmA)
## Software richiesto:
- [Balena Etcher](https://www.balena.io/etcher/)
- [Raspberry Pi USB Boot](https://github.com/raspberrypi/usbboot/raw/master/win32/rpiboot_setup.exe)
- L'ultima immagine Nebra per il dispositivo specifico:
*Se non si sa quale dispositivo si possiede, consultare la sezione [nebra documentatio](https://support.nebra.com/support/home) Se è più vecchio, si può presumere che si tratti di un dispositivo di prima generazione.
  - [Nebra Outdoor 2](https://github.com/NebraLtd/helium-nebra-outdoor2/releases/)
  - [Nebra Indoor 2](https://github.com/NebraLtd/helium-nebra-indoor2/releases/)
  - [Nebra Outdoor 1](https://github.com/NebraLtd/helium-nebra-outdoor1/releases)
  - [Nebra Indoor 1](https://github.com/NebraLtd/helium-nebra-indoor1/releases)

## Contenuto del minatore Nebra Helium:
### Contenuto del Nebra Indoor Miner:
{{< figure src="Indoor-internal-lights.png" alt="Nebra Indoor Miner" >}}
### Contenuto del Nebra Outdoor Miner:
{{< figure src="Inside-Interfaces.jpg" alt="Nebra Outdoor Miner" >}}
 - 1.) Jack a cilindro da 9-16 V @ 15 W CC 6,5 mmx2,0 mm
 - 2.) Connettore Ethernet
 - 3.) Indicatore LED
 - 4.) Pulsante di interfaccia
 - 5.) Connettore modulo 4G / LTE
 - 6.) Slot per scheda Sim

## Come sostituire la scheda SD
### Passo 1: acquisire facoltativamente il file config.json dalla chiave EMMC:
- Scaricare e installare [Raspberry Pi USB Boot](https://github.com/raspberrypi/usbboot/raw/master/win32/rpiboot_setup.exe) è necessario per avviare il modulo di calcolo come file system usb
- Identificare e regolare i pin dei ponticelli sulla scheda figlia CM3 per la modalità di programmazione
 - {{< figure src="daughterboardBreakdown.png" alt="Nebra Daughterboard Overview" >}}
   - 5.) Porta micro USB utilizzata per l'imaging
   - 7.) Jumper USB JP4 - Utilizzato per passare dal funzionamento normale alla modalità flash; assicurarsi che sia in posizione 1-2 per il funzionamento normale e 2-3 per la programmazione.
   - 8.) JP3 Jumper di alimentazione - Consente di alimentare il modulo dal connettore Micro USB. Collegare solo quando si programma dal PC e assicurarsi che la scheda madre non sia collegata.
 - Spostare il ponticello JP4 in posizione 2+3.
 - Collegare un cavo USB e far passare il [Raspberry Pi USB Boot](https://github.com/raspberrypi/usbboot/raw/master/win32/rpiboot_setup.exe) utilità
 - Aprire il file explorer e vedere un'unità chiamata "resin-boot". Recuperare il file "config.json" dalla directory, che potrebbe servire in seguito e di cui dovrebbe essere stato fatto un backup.
 - Scollegare il cavo USB e reimpostare il ponticello JP4 in posizione 1+2.
### Fase 2: Flash della nuova scheda sd con l'immagine Balena Raspberry Pi CM3:
- Scaricare ed estrarre l'immagine appropriata
  - [Nebra Outdoor 2](https://github.com/NebraLtd/helium-nebra-outdoor2/releases/)
  - [Nebra Indoor 2](https://github.com/NebraLtd/helium-nebra-indoor2/releases/)
  - [Nebra Outdoor 1](https://github.com/NebraLtd/helium-nebra-outdoor1/releases)
  - [Nebra Indoor 1](https://github.com/NebraLtd/helium-nebra-indoor1/releases)
- Utilizzo [Balena Etcher](https://www.balena.io/etcher/) selezionare il file .img estratto di recente e la nuova scheda microsd come dispositivo di destinazione.
- Selezionare Flash
### Fase 3: installare la nuova scheda SD e riassemblare Nebra Miner:
 - Installare la scheda SD nello slot in cui si trovava precedentemente la chiave EMMC.
 - Riassemblare il miner
 - Quando si accende per la prima volta il Nebra Miner appena flashato, collegarlo alla rete Ethernet per 20-30 minuti prima di impostare nuovamente la connessione wifi.
### Fase 4: Profitto?




