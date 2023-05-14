---
title: "ChromiumADMX: Juiste ADMX-sjabloon voor Chromium Browser"
date: 2020-07-25
---


Juiste ADMX-sjabloon voor de Chromium-browser

Chromium heeft als bedrijf nagelaten ADMX-sjablonen voor de Chromium Browser uit te brengen die tegelijk met de Google Chrome-sjablonen kunnen worden geïnstalleerd.
Daarom hebben we de Google Chrome ADMX-sjablonen aangepast aan het registerpad van de Chromium Browser en in tandum geplaatst in de Google ADMX-map in GPO.

**Deze beleidsdefinities bevinden zich in een pre-alfa-staat. Ze mogen alleen worden gebruikt voor testdoeleinden**

## Download de benodigde bestanden

**Download de benodigde bestanden van de[GitHub Repository](https://github.com/simeononsecurity/ChromiumADMX)

## Notes

Gewijzigde Google Chrome-beleidsdefinities volgens:
[Chromium Policy Templates](https://www.chromium.org/administrators/policy-templates)

**Noot:** Vervang "HKEY_LOCAL_MACHINE\Software\GoogleChrome" door "HKEY_LOCAL_MACHINE\Software\PoliciesChromium".

**Noot:** Installeer SOS'es Chromium en Brave Browser ADMX sjablonen niet tegelijkertijd.

## Hoe te installeren

1.) Kopieer alle bestanden behalve readme.md naar "C:\WindowsPolicyDefinitions" en/of "\domain.tld".

2.) Winst?




