---
title: "Neem controle over het browserbeleid van Brave met BraveADMX - Gewijzigde ADMX-sjablonen"
date: 2020-07-25
---


Brave, als bedrijf, heeft verzuimd ADMX-sjablonen uit te brengen voor de Brave-browser en duwt pure registers als de enige ondersteunde optie.
Aangezien de Brave Browser is gebaseerd op Chromium, zou het de meeste, zo niet alle, beleidsregels van de Chromium en Google Chrome ADMX-sjablonen moeten ondersteunen.
Met dat in gedachten hebben we de Google Chrome ADMX-sjablonen aangepast aan het registerpad van de Brave Browser. Na wat probleemoplossing en tests lijken de sjablonen te werken.

**Deze Policy Definitions zijn in een Pre-Alpha staat. Ze mogen alleen worden gebruikt voor testdoeleinden**

## Download de benodigde bestanden.

**Download de benodigde bestanden van de[GitHub Repository](https://github.com/simeononsecurity/BraveADMX)

## Notes

Gewijzigde Google Chrome-beleidsdefinities volgens:
[Brave Group Policy](https://support.brave.com/hc/en-us/articles/360039248271-Group-Policy)

**Noot:** Vervang "HKEY_LOCAL_MACHINE\Software\GoogleChrome" door "HKEY_LOCAL_MACHINE\Software\BraveSoftware\Brave".

**Noot:** Installeer SOS'es Chromium en Brave Browser ADMX sjablonen niet tegelijkertijd.

## Hoe te installeren

1.) Kopieer alle bestanden behalve readme.md naar "C:\WindowsPolicyDefinitions" en/of "\domain.tld".

2.) Winst?