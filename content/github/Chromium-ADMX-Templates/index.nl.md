---
title: "ChromiumADMX: Juiste ADMX-sjabloon voor Chromium-browser"
date: 2020-07-25
---


Juiste ADMX-sjabloon voor de Chromium-browser

Chromium heeft als bedrijf geen ADMX-sjablonen uitgebracht voor de Chromium-browser die tegelijk met de Google Chrome-sjablonen kunnen worden geïnstalleerd.
Met dat in gedachten hebben we de Google Chrome ADMX-sjablonen aangepast zodat ze het registerpad van de Chromium-browser weergeven en in tandum in de Google ADMX-map in GPO geplaatst.

**Deze beleidsdefinities bevinden zich in een pre-alfastatus. Ze mogen alleen worden gebruikt voor testdoeleinden**

## Download de benodigde bestanden

**Download de benodigde bestanden van de [GitHub Repository](https://github.com/simeononsecurity/ChromiumADMX)

## Opmerkingen

Gewijzigde Google Chrome-beleidsdefinities volgens:
[Chromium Policy Templates](https://www.chromium.org/administrators/policy-templates)

**Let op:** Vervang "HKEY_LOCAL_MACHINE\Software\GoogleChrome" door "HKEY_LOCAL_MACHINE\Software\Policies\Chromium".

**Noot:** Installeer SOS'es Chromium en Brave Browser ADMX-sjablonen niet tegelijkertijd.

## Hoe te installeren

1.) Kopieer alle bestanden behalve readme.md naar "C:\WindowsPolicyDefinitions" en/of "\domain.tld".

2.) Winst?




