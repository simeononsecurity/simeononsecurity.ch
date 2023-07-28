---
title: "Înlocuirea cardului SD Nebra Helium Miner: Ghid pas cu pas"
draft: false
toc: true
date: 2022-02-13
description: "Aflați cum să înlocuiți sau să reîncărcați cardul SD Nebra Indoor și Outdoor, prima și a doua generație, EMMC Key SD Card și să remediați problemele de sincronizare Helium Miner cu acest ghid."
genre: ["Tehnologie", "Criptomonedă", "Hardware", "Mineritul de heliu", "Depanare", "Înlocuirea cardului SD", "Probleme de sincronizare", "Raspberry Pi", "Balena Etcher", "Nebra Helium Miner"]
tags: ["Nebra Helium Miner", "Înlocuirea cardului SD", "Probleme de sincronizare", "Mineritul de heliu", "Depanare", "Raspberry Pi", "Balena Etcher", "Ghid hardware", "Actualizare card SD", "Rezolvarea problemelor de sincronizare", "Ghid pas cu pas", "Helium Miner Fix sincronizare", "Nebra Indoor Miner", "Nebra Miner în aer liber", "Raspberry Pi Compute Modulul 3", "Balena Raspberry Pi CM3 Imagine", "Depanarea minerilor cu heliu", "Nebra Mining Equipment", "Balena Etcher Software", "Înlocuirea cheii EMMC pe Nebra Miner", "Repararea cardului SD pentru Helium Miner", "Corectarea problemelor de sincronizare Helium Miner", "Înlocuirea cardului SD Nebra Miner", "Ghid pentru de depanare Nebra Helium Miner", "Sfaturi pentru minerit cu heliu", "Actualizarea cardului SD al Nebra Helium Miner", "Cum să ștergeți Reimage Nebra Miner SD Card", "Depanarea problemelor de sincronizare Nebra Helium Miner Probleme de sincronizare"]
cover: "/img/cover/A_cartoon_illustration_of_a_person_holding_a_Nebra_Helium_M.png"
coverAlt: "O ilustrație de desen animat a unei persoane care ține în mână un Nebra Helium Miner cu un panou deschis care dezvăluie slotul pentru cardul SD și pașii ghidului care apar ca un ghid care plutește deasupra dispozitivului."
coverCaption: "Rezolvă problemele de sincronizare și actualizează-ți cu ușurință Helium Miner."
---

**Înlocuirea și reimaginarea cheii EMMC / cardului SD pentru interior și exterior Nebra**

Acest ghid cuprinzător vă va ghida prin procesul de înlocuire sau de reimaginare a cardului EMMC Key/SD Card Nebra Indoor și Outdoor. Urmând acești pași, puteți rezolva problemele de sincronizare cu Helium Minerul dumneavoastră și puteți asigura o funcționare fără probleme. Ghidul oferă o explicație detaliată a instrumentelor și a software-ului de care veți avea nevoie, precum și a pașilor necesari pentru a achiziționa fișierul config.json, pentru a flasha noul card SD utilizând Balena Raspberry Pi CM3 Image și pentru a transfera fișierul config original pe noul card SD.

## Introducere

Minerii cu heliu Nebra, atât modelul de interior, cât și cel de exterior, se bazează pe cheia EMMC/carte SD pentru funcționarea lor. În timp, poate deveni necesară înlocuirea sau re-flasharea acestui card pentru a rezolva problemele de sincronizare și pentru a menține performanțele optime. Acest ghid vă va dota cu cunoștințele și instrucțiunile necesare pentru a îndeplini eficient această sarcină.

Pentru a înlocui cu succes cardul SD al Nebra Helium Miner, veți avea nevoie de instrumente și software specifice. Printre aceste unelte se numără o șurubelniță cu cap Phillips sau [Allen Key Set](https://amzn.to/34SlnOS) (depending on the model), a [Micro SD Card Reader](https://amzn.to/3Jl3U0w), a [64GB A2 micro SD card](https://amzn.to/3oJtTqs) (or larger), and a [Micro USB 2.0 Cable](https://amzn.to/3LxXYmA). The essential software needed for this process includes [Balena Etcher](https://www.balena.io/etcher/), Balena Raspberry Pi Image, and [Raspberry Pi USB Boot](https://github.com/raspberrypi/usbboot/raw/master/win32/rpiboot_setup.exe) Cu aceste resurse la îndemână, veți fi gata să procedați la înlocuirea cardului SD sau la reîncărcarea acestuia.

## Instrumente necesare:
- O șurubelniță cu cap Phillips sau [plastic pry bar](https://amzn.to/3rLXVfc) for the Nebra Indoor Miner or [allen key set](https://amzn.to/34SlnOS) pentru Nebra Outdoor Miner
- Unghii puternice, pensete sau clești cu vârf de ac pentru a îndepărta vechiul card SD
- [A Micro SD Card Reader](https://amzn.to/3Jl3U0w)
- [A 64gb (or larger) A2 micro sd card](https://amzn.to/3oJtTqs)
- [A Micro USB 2.0 Cable](https://amzn.to/3LxXYmA)
## Software necesar:
- [Balena Etcher](https://www.balena.io/etcher/)
- [Raspberry Pi USB Boot](https://github.com/raspberrypi/usbboot/raw/master/win32/rpiboot_setup.exe)
- Cea mai recentă imagine Nebra pentru dispozitivul dvs. specific:
*Dacă nu știți ce dispozitiv aveți, vă rugăm să consultați pagina de [nebra documentatio](https://support.nebra.com/support/home) Dacă este mai veche, este destul de sigur să presupunem că aveți un dispozitiv de prima generație.*
  - [Nebra Outdoor 2](https://github.com/NebraLtd/helium-nebra-outdoor2/releases/)
  - [Nebra Indoor 2](https://github.com/NebraLtd/helium-nebra-indoor2/releases/)
  - [Nebra Outdoor 1](https://github.com/NebraLtd/helium-nebra-outdoor1/releases)
  - [Nebra Indoor 1](https://github.com/NebraLtd/helium-nebra-indoor1/releases)

## În interiorul minerilor Nebra Helium:
### Conținutul minerului de interior Nebra:
{{< figure src="Indoor-internal-lights.png" alt="Nebra Indoor Miner" >}}
### Conținutul Nebra Outdoor Miner:
{{< figure src="Inside-Interfaces.jpg" alt="Nebra Outdoor Miner" >}}
 - 1.) 9-16V @ 15W DC 6.5MMx2.0MM Barrel Jack 6.5MMx2.0MM
 - 2.) Conector Ethernet
 - 3.) Indicator LED
 - 4.) Butonul de interfață
 - 5.) Conectorul modulului 4G / LTE
 - 6.) Fantă pentru cartela Sim

## Cum se înlocuiește cardul SD
### Pasul 1: Opțional, dobândiți fișierul config.json din cheia EMMC:
- Descărcați și instalați [Raspberry Pi USB Boot](https://github.com/raspberrypi/usbboot/raw/master/win32/rpiboot_setup.exe) veți avea nevoie de acest lucru pentru a porni modulul de calcul ca un sistem de fișiere USB
- Identificați și ajustați pinii jumper de pe placa fiică CM3 pentru modul de programare
 - {{< figure src="daughterboardBreakdown.png" alt="Nebra Daughterboard Overview" >}}
   - 5.) Port Micro USB utilizat pentru imagistică
   - 7.) Jumper USB JP4 - Utilizat pentru a comuta între modul de funcționare normală și modul flash, asigurați-vă că este în poziția 1-2 pentru funcționarea normală și 2-3 pentru programare.
   - 8.) JP3 Power Jumper (Jumper de alimentare JP3) - Permite ca modulul să fie alimentat de la conectorul Micro USB. Conectați-l numai atunci când programați de pe PC și asigurați-vă că placa de bază nu este conectată.
 - Mutați jumperul JP4 în poziția 2+3
 - Conectați un cablu USB și rulați [Raspberry Pi USB Boot](https://github.com/raspberrypi/usbboot/raw/master/win32/rpiboot_setup.exe) utilitate
 - Deschideți exploratorul de fișiere și veți vedea o unitate numită "resin-boot". Recuperați fișierul "config.json" din acest director, este posibil să aveți nevoie de el mai târziu și ar trebui să fie salvat.
 - Deconectați cablul USB și resetați jumperul JP4 în poziția 1+2
### Pasul 2: Flash noul card sd cu imaginea Balena Raspberry Pi CM3 Image:
- Descărcați și extrageți imaginea corespunzătoare
  - [Nebra Outdoor 2](https://github.com/NebraLtd/helium-nebra-outdoor2/releases/)
  - [Nebra Indoor 2](https://github.com/NebraLtd/helium-nebra-indoor2/releases/)
  - [Nebra Outdoor 1](https://github.com/NebraLtd/helium-nebra-outdoor1/releases)
  - [Nebra Indoor 1](https://github.com/NebraLtd/helium-nebra-indoor1/releases)
- Utilizarea [Balena Etcher](https://www.balena.io/etcher/) selectați fișierul .img extras recent și noul card microsd ca dispozitiv țintă
- Selectați Flash
### Pasul 3: Instalați noul card sd și reasamblați Nebra Miner:
 - Instalați cardul SD în slotul în care se afla anterior cheia EMMC.
 - Reasamblați minerul
 - La prima alimentare a Nebra Minerului nou flasheat, conectați-l cu ethernet timp de 20-30 de minute înainte de a seta din nou conexiunile wifi.
### Pasul 4: Profit?




