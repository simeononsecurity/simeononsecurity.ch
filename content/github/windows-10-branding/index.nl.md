---
title: "Geautomatiseerde branding voor Windows-systemen - Eenvoudig beheer van bureaublad, vergrendelingsscherm en meer"
date: 2020-08-14
---


Veel organisaties hebben een behoefte of willen de branding van een Windows systeem controleren.
Dit omvat de bureaubladachtergrond, de avatar van de gebruiker, het Windows-vergrendelingsscherm en soms het OEM-logo.
In Windows 10, Windows Server 2016 en Windows Server 2019 is dit niet bijzonder eenvoudig.
Maar met behulp van het gekoppelde script kunnen we het gedeeltelijk automatiseren en het proces veel gemakkelijker maken.

## Download de benodigde bestanden

**Download de benodigde bestanden van de[GitHub Repository](https://github.com/simeononsecurity/Windows-Branding-Script)

## Hoe de branding bestanden in te stellen

- X] Vervang alle afbeeldingen door uw merkafbeeldingen
  - X] OEM logo moet 95x95 of 120x20 zijn en in ".bmp" formaat.
  - X] Genereer de User Image samen met 32x32, 40x40, 48x48, 192x192 varianten.
  - X] Genereer of kopieer de gebruikersafbeelding voor de gastafbeelding.

## Hoe het script uit te voeren
```
.\sos-copybranding.ps1
```

## Dit script gebruikt het volgende gereedschap:

-[Microsoft Security Compliance Toolkit 1.0 - LGPO](https://www.microsoft.com/en-us/download/details.aspx?id=55319)
