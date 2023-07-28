---
title: "Nebra Helium Miner SD-kaart vervangen: Stap-voor-stap handleiding"
draft: false
toc: true
date: 2022-02-13
description: "Leer hoe je de Nebra Indoor en Outdoor, Eerste en Tweede generatie, EMMC Key SD-kaart vervangt of opnieuw flasht en hoe je Helium Miner synchronisatieproblemen oplost met deze handleiding."
genre: ["Technologie", "Cryptocurrency", "Hardware", "Helium mijnbouw", "Problemen oplossen", "SD-kaart vervangen", "Problemen met synchroniseren", "Raspberry Pi", "Balena Escher", "Nebra Helium Miner"]
tags: ["Nebra Helium Miner", "SD-kaart vervangen", "Problemen met synchroniseren", "Helium mijnbouw", "Problemen oplossen", "Raspberry Pi", "Balena Escher", "Hardware Handleiding", "SD-kaart upgraden", "Synchronisatieproblemen oplossen", "Stap-voor-stap handleiding", "Heliumminer Sync Fix", "Nebra Indoor Miner", "Nebra mijnwerker voor buiten", "Raspberry Pi rekenmodule 3", "Balena Raspberry Pi CM3 Afbeelding", "Problemen oplossen met heliumminers", "Nebra mijnbouwapparatuur", "Balena Etcher Software", "EMMC-sleutel vervangen op Nebra Miner", "SD-kaart repareren voor Helium Miner", "Heliumminer synchronisatieproblemen oplossen", "Nebra Miner SD-kaart vervangen", "Gids voor het oplossen van problemen met de Nebra Helium Miner", "Tips voor heliumwinning", "Nebra Helium Miner SD-kaart upgraden", "Hoe Nebra Miner SD-kaart opnieuw te beveiligen", "Problemen met synchroniseren van Nebra Heliumminer oplossen"]
cover: "/img/cover/A_cartoon_illustration_of_a_person_holding_a_Nebra_Helium_M.png"
coverAlt: "Een cartoonillustratie van een persoon die een Nebra Helium Miner vasthoudt met een open paneel dat de SD-kaartsleuf onthult en de stappen van de gids die verschijnen als een gids die boven het apparaat zweeft."
coverCaption: "Los synchronisatieproblemen op en upgrade je Helium Miner met gemak."
---

**De Nebra Indoor en Outdoor EMMC Key / SD-kaart vervangen en opnieuw implementeren**

Deze uitgebreide handleiding helpt u bij het vervangen of re-flashen van de Nebra Indoor en Outdoor EMMC Key/SD Card. Door deze stappen te volgen, kunt u synchronisatieproblemen met uw Helium Miner oplossen en een probleemloze werking garanderen. De gids geeft een gedetailleerde uitleg van de tools en software die u nodig hebt, evenals de noodzakelijke stappen om het config.json-bestand te verkrijgen, de nieuwe SD-kaart te flashen met behulp van Balena Raspberry Pi CM3 Image, en het originele config-bestand over te zetten naar de nieuwe SD-kaart.

## Introductie

De Nebra Helium Miners, zowel de binnen- als de buitenmodellen, vertrouwen voor hun werking op de EMMC Key/SD-kaart. Na verloop van tijd kan het nodig zijn om deze kaart te vervangen of opnieuw te flashen om synchronisatieproblemen op te lossen en optimale prestaties te behouden. Deze handleiding voorziet u van de kennis en instructies die nodig zijn om deze taak effectief uit te voeren.

Om de SD-kaart van de Nebra Helium Miner succesvol te vervangen, heb je specifiek gereedschap en software nodig. De gereedschappen omvatten een kruiskopschroevendraaier of [Allen Key Set](https://amzn.to/34SlnOS) (depending on the model), a [Micro SD Card Reader](https://amzn.to/3Jl3U0w), a [64GB A2 micro SD card](https://amzn.to/3oJtTqs) (or larger), and a [Micro USB 2.0 Cable](https://amzn.to/3LxXYmA). The essential software needed for this process includes [Balena Etcher](https://www.balena.io/etcher/), Balena Raspberry Pi Image, and [Raspberry Pi USB Boot](https://github.com/raspberrypi/usbboot/raw/master/win32/rpiboot_setup.exe) Met deze bronnen bij de hand bent u klaar om verder te gaan met het vervangen of opnieuw flashen van de SD-kaart.

## Vereist gereedschap:
- Een kruiskopschroevendraaier of [plastic pry bar](https://amzn.to/3rLXVfc) for the Nebra Indoor Miner or [allen key set](https://amzn.to/34SlnOS) voor Nebra Outdoor Miner
- Sterke vingernagels, pincet of naaldbektang om de oude SD-kaart te verwijderen
- [A Micro SD Card Reader](https://amzn.to/3Jl3U0w)
- [A 64gb (or larger) A2 micro sd card](https://amzn.to/3oJtTqs)
- [A Micro USB 2.0 Cable](https://amzn.to/3LxXYmA)
## Vereiste software:
- [Balena Etcher](https://www.balena.io/etcher/)
- [Raspberry Pi USB Boot](https://github.com/raspberrypi/usbboot/raw/master/win32/rpiboot_setup.exe)
- Nieuwste Nebra-afbeelding voor je specifieke apparaat:
*Als je niet weet welk apparaat je hebt, raadpleeg dan de [nebra documentatio](https://support.nebra.com/support/home) Als het ouder is, is het vrij veilig om aan te nemen dat je een apparaat van de eerste generatie hebt.*
  - [Nebra Outdoor 2](https://github.com/NebraLtd/helium-nebra-outdoor2/releases/)
  - [Nebra Indoor 2](https://github.com/NebraLtd/helium-nebra-indoor2/releases/)
  - [Nebra Outdoor 1](https://github.com/NebraLtd/helium-nebra-outdoor1/releases)
  - [Nebra Indoor 1](https://github.com/NebraLtd/helium-nebra-indoor1/releases)

## Binnen in de Nebra Helium Miners:
### Inhoud van de Nebra Indoor Miner:
{{< figure src="Indoor-internal-lights.png" alt="Nebra Indoor Miner" >}}
### Inhoud van de Nebra Outdoor Miner:
{{< figure src="Inside-Interfaces.jpg" alt="Nebra Outdoor Miner" >}}
 - 1.) 9-16V @ 15W DC 6,5MMx2,0MM Barrel Jack
 - 2.) Ethernet Aansluiting
 - 3.) LED-indicator
 - 4.) Interface knop
 - 5.) Aansluiting 4G/LTE-module
 - 6.) Sim-kaartsleuf

## De SD-kaart vervangen
### Stap 1: Verkrijg optioneel het config.json-bestand van de EMMC-sleutel:
- Downloaden en installeren [Raspberry Pi USB Boot](https://github.com/raspberrypi/usbboot/raw/master/win32/rpiboot_setup.exe) dit heb je nodig om de computermodule op te starten als een usb bestandssysteem
- Identificeer de en pas de jumper pinnen aan op het CM3 dochterbord voor de programmeermodus
 - {{< figure src="daughterboardBreakdown.png" alt="Nebra Daughterboard Overview" >}}
   - 5.) Micro USB-poort voor beeldvorming
   - 7.) JP4 USB Jumper - Gebruikt om te schakelen tussen normale werking en flashmodus, zorg ervoor dat deze in positie 1-2 staat voor normale werking en 2-3 voor programmeren.
   - 8.) JP3 Power Jumper - Hiermee kan de module worden gevoed via de micro-USB-connector. Alleen aansluiten bij programmeren vanaf de pc en zorgen dat het moederbord niet is aangesloten.
 - Zet de jumper JP4 in positie 2+3.
 - Sluit een usb-kabel aan en voer de [Raspberry Pi USB Boot](https://github.com/raspberrypi/usbboot/raw/master/win32/rpiboot_setup.exe) hulpprogramma
 - Open je bestandsverkenner en je ziet een schijf genaamd "resin-boot". Haal het "config.json" bestand uit de directory, je kunt het later nodig hebben en er zou een back-up van moeten zijn.
 - Koppel de usb-kabel los en zet de JP4-jumper terug op positie 1+2.
### Stap 2: Flash de nieuwe sd-kaart met de Balena Raspberry Pi CM3 Image:
- Download en pak de juiste image uit
  - [Nebra Outdoor 2](https://github.com/NebraLtd/helium-nebra-outdoor2/releases/)
  - [Nebra Indoor 2](https://github.com/NebraLtd/helium-nebra-indoor2/releases/)
  - [Nebra Outdoor 1](https://github.com/NebraLtd/helium-nebra-outdoor1/releases)
  - [Nebra Indoor 1](https://github.com/NebraLtd/helium-nebra-indoor1/releases)
- Gebruik [Balena Etcher](https://www.balena.io/etcher/) selecteer het onlangs uitgepakte .img-bestand en uw nieuwe microsd-kaart als doelapparaat
- Selecteer Flash
### Stap 3: Installeer de nieuwe sd-kaart en zet de Nebra Miner weer in elkaar:
 - Installeer de SD-kaart in de sleuf waarin eerder de EMMC-sleutel zat.
 - Zet de mijnwerker weer in elkaar
 - Wanneer u de pas geflashte Nebra Miner voor het eerst van stroom voorziet, sluit hem dan eerst 20-30 minuten aan op ethernet voordat u de wifi-verbinding weer tot stand brengt.
### Stap 4: Winst?




