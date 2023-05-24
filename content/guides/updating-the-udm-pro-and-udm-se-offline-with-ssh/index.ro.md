---
title: "Actualizare offline de firmware pentru Ubiquiti Unifi UDM Pro și UDM SE prin linia de comandă SSH"
draft: false
toc: true
date: 2023-05-28
description: "Aflați cum să actualizați firmware-ul Ubiquiti Unifi UDM Pro și UDM SE offline prin linia de comandă SSH pentru performanță și securitate optime."
tags: ["Actualizare firmware Ubiquiti", "UDM Pro", "UDM SE", "actualizare offline de firmware", "linia de comandă SSH", "administrare rețea", "securitatea retelei", "upgrade de firmware", "Conexiune SSH", "fișier firmware", "Controler de rețea UniFi", "corectarea erorilor", "imbunatatiri ale performantei", "patch-uri de securitate", "rețele", "dispozitive de rețea", "tehnologie", "management IT", "procesul de actualizare a firmware-ului", "optimizarea rețelei", "Actualizare firmware Ubiquiti Networks", "Actualizare firmware UDM Pro", "Actualizare firmware UDM SE", "procesul de actualizare offline a firmware-ului", "Actualizare firmware SSH", "managementul dispozitivelor de rețea", "actualizări de securitate a rețelei", "strategii de actualizare a firmware-ului", "management offline de firmware", "optimizarea performanței rețelei", "managementul corecțiilor de securitate", "actualizări de tehnologie de rețea"]
cover: "/img/cover/A_colorful_illustration_depicting_a_computer_connecting.png"
coverAlt: "O ilustrație colorată care ilustrează un computer care se conectează la un router prin SSH, simbolizând procesul de actualizare offline a firmware-ului pentru dispozitivele Ubiquiti Unifi UDM Pro și UDM SE."
coverCaption: ""
---

**Actualizați Ubiquiti Unifi UDM Pro și UDM SE offline prin SSH**

În lumea rețelelor, **Ubiquiti Networks** a câștigat recunoaștere pentru soluțiile sale inovatoare. **Ubiquiti Unifi Dream Machine Pro (UDM Pro)** și **Unifi Dream Machine SE (UDM SE)** sunt două produse populare care oferă caracteristici complete de gestionare a rețelei. Actualizarea firmware-ului acestor dispozitive este crucială pentru a asigura performanță și securitate optime. În acest articol, vom explora cum să actualizați firmware-ul UDM Pro și UDM SE **offline** utilizând linia de comandă SSH.

______

## De ce să actualizezi firmware-ul?

Actualizările de firmware sunt esențiale pentru orice dispozitiv de rețea, deoarece conțin adesea remedieri de erori, îmbunătățiri de performanță și corecții de securitate. Actualizarea regulată a firmware-ului UDM Pro și UDM SE este crucială pentru a vă asigura că rețeaua rămâne sigură și funcționează fără probleme.

______

## Actualizare de firmware offline

Actualizarea firmware-ului UDM Pro și UDM SE se poate face prin intermediul **UniFi Dashboard**. Cu toate acestea, în unele scenarii, este posibil ca o conexiune la internet să nu fie disponibilă sau de dorit. În astfel de cazuri, o actualizare offline folosind linia de comandă SSH oferă o soluție alternativă.

______

## Pregătirea pentru actualizarea offline

Înainte de a continua cu actualizarea offline, asigurați-vă că aveți următoarele cerințe preliminare:

1. Un computer sau un dispozitiv cu un client SSH instalat.
2. Cel mai recent fișier firmware pentru UDM Pro sau UDM SE. Puteți obține fișierul firmware de la [Ubiquiti Downloads](https://www.ui.com/download/unifi) for the [UDM Pro](https://www.ui.com/download/unifi/unifi-dream-machine-pro) page. For early access firmwares, you can see them on the [community releases page](https://community.ui.com/releases) once you've signed into your.[**ui.com**](https://account.ui.com/) cont

______

## Stabilirea conexiunii SSH

Pentru a actualiza UDM Pro sau UDM SE prin linia de comandă SSH, urmați acești pași:

1. Asigurați-vă că computerul sau dispozitivul este conectat la aceeași rețea ca UDM Pro sau UDM SE.
2. Deschideți clientul SSH preferat și stabiliți o conexiune SSH la **UDM Pro sau adresa IP a UDM SE**. De exemplu, folosind **clientul OpenSSH** în Linux sau macOS, puteți folosi următoarea comandă:

```bash
ssh root@<UDM_IP_ADDRESS>
```

A inlocui `<UDM_IP_ADDRESS>` cu adresa IP reală a UDM Pro sau UDM SE.

3. Introduceți **numele de utilizator** și **parola** când vi se solicită. Acreditările implicite pentru dispozitivele Ubiquiti sunt de obicei `ubnt` atât pentru numele de utilizator, cât și pentru parola.

______

## Actualizarea firmware-ului

După ce ați stabilit conexiunea SSH, puteți continua cu actualizarea firmware-ului:

1. Încărcați fișierul firmware în UDM Pro sau UDM SE utilizând **SCP (Secure Copy)**. SCP permite transferul securizat de fișiere prin SSH. Presupunând că fișierul firmware se află pe mașina dvs. locală, puteți utiliza următoarea comandă:

```bash
scp <FIRMWARE_FILE_PATH> ubnt@<UDM_IP_ADDRESS>:/root/fwupdate.bin
```

A inlocui `<FIRMWARE_FILE_PATH>` cu calea către fișierul firmware de pe mașina dvs. locală și `<UDM_IP_ADDRESS>` cu adresa IP a UDM Pro sau UDM SE.

2. Odată ce fișierul firmware este încărcat, puteți iniția procesul de actualizare a firmware-ului. Executați următoarea comandă:

```bash
ssh ubnt@<UDM_IP_ADDRESS> "ubnt-tools fwupdate /root/fwupdate.bin"
```

3. UDM Pro sau UDM SE va începe procesul de actualizare a firmware-ului. Ar putea dura câteva minute. **Nu întrerupeți procesul** până la finalizarea actualizării.

4. După terminarea actualizării, puteți verifica versiunea firmware-ului conectându-vă la UniFi Network Controller sau executând următoarea comandă:

```bash
ssh ubnt@<UDM_IP_ADDRESS> "show version"
```
Vă rugăm să rețineți că procesul de mai sus presupune că aveți fișierul firmware necesar pentru UDM Pro sau UDM SE. Asigurați-vă că aveți fișierul firmware corect pentru modelul și versiunea dispozitivului dvs.

## Concluzie

Actualizarea firmware-ului dispozitivelor Ubiquiti Unifi UDM Pro și UDM SE este un pas crucial pentru a asigura performanță și securitate optime. În timp ce UniFi Network Controller oferă o modalitate convenabilă de a actualiza firmware-ul, efectuarea unei actualizări offline prin linia de comandă SSH oferă o soluție viabilă atunci când o conexiune la internet nu este disponibilă sau de dorit.

Urmând pașii prezentați în acest articol, puteți actualiza cu succes firmware-ul dispozitivelor UDM Pro și UDM SE folosind linia de comandă SSH. Nu uitați să utilizați întotdeauna cea mai recentă versiune de firmware furnizată de Ubiquiti Networks pentru a profita de remedieri de erori, îmbunătățiri de performanță și corecții de securitate.

## Referințe

- [Ubiquiti Downloads](https://www.ui.com/download/unifi/) - Pagina oficială de descărcări Ubiquiti pentru fișierele firmware.
- [Unifi Advanced Updating Techniques](https://help.ui.com/hc/en-us/articles/204910064-UniFi-Upgrade-the-Firmware-of-a-UniFi-Device)
