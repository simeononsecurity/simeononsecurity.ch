---
title: "Optimaliseer uw Windows PC met Windows-Optimize-Debloat"
date: 2020-12-29
toc: true
draft: false
description: "Verbeter de prestaties en privacy van uw Windows-besturingssysteem met Windows-Optimize-Debloat, een uitgebreid script dat helpt bloatware te verwijderen en systeeminstellingen te optimaliseren."
tags: ["Windows-Optimize-Debloat", "Windows Optimalisatie", "Deblokkerende ramen", "Windows versnellen", "De prestaties van Windows optimaliseren", "Windows Prestatieverhoging", "Windows Systeem Optimalisatie", "Microsoft", "Privacy", "Bloatware verwijderen", "Windows 10", "Windows 11", "Windows Defender", "Windows Update", "Cortona", "Objecten voor groepsbeleid", "Telemetrie", "Windows Store", "Windows 10 Professional", "Windows 10 Home"]
---


[![Test script against windows docker container](https://github.com/simeononsecurity/Windows-Optimize-Debloat/actions/workflows/test-with-docker.yml/badge.svg)](https://github.com/simeononsecurity/Windows-Optimize-Debloat/actions/workflows/test-with-docker.yml)

*Voor degenen die hun Windows 10 en 11 installaties willen minimaliseren.

**Noot:** Dit script zou voor de meeste, zo niet alle, systemen zonder problemen moeten werken. Terwijl[@SimeonOnSecurity](https://github.com/simeononsecurity) creates, reviews, and tests each repo intensivly, we can not test every possible configuration nor does [@SimeonOnSecurity](https://github.com/simeononsecurity) take any responsibility for breaking your system. If something goes wrong, be prepared to submit an [issue](../../issues) Voer dit script niet uit als je niet begrijpt wat het doet.

## Introductie:
Windows 10 en 11 is zijn invasieve en onveilige besturingssysteem uit de doos.
Organisaties zoals[Microsoft](https://microsoft.com), [PrivacyTools.io](https://PrivacyTools.io) en anderen hebben configuratiewijzigingen aanbevolen om het Windows 10-besturingssysteem te optimaliseren en te ontladen. Deze wijzigingen omvatten het blokkeren van telemetrie, het verwijderen van logboeken en het verwijderen van bloatware om er een paar te noemen. Dit script is bedoeld om de door die organisaties aanbevolen configuraties te automatiseren.

## Opmerkingen:
- Dit script is ontworpen voor gebruik in voornamelijk **Persoonlijk gebruik** omgevingen.
- Dit script is zo ontworpen dat de optimalisaties, in tegenstelling tot sommige andere scripts, de kernfuncties van Windows niet zullen verbreken.
 - Functies zoals Windows Update, Windows Defender, de Windows Store en Cortona zijn beperkt, maar zijn niet in een disfunctionele staat zoals de meeste andere Windows 10 Privacy scripts.
- Als u een geminimaliseerd script zoekt dat alleen gericht is op commerciële omgevingen, bekijk dan dit[GitHub Repository](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)

## Vereisten:
- [X] Windows 10/11 Enterprise, Windows 10 Professional of Windows 10 Home.
  - Windows Home staat geen GPO-configuraties toe.
    - Het script werkt nog steeds, maar niet alle instellingen zijn van toepassing.
  - Windows "N" Editions zijn niet getest.
  - Voer de[Windows 10 Upgrade Assistant](https://support.microsoft.com/en-us/help/3159635/windows-10-update-assistant) om de laatste grote release bij te werken en te verifiëren.

## Microsoft Account of Xbox Services repareren:
Dit is omdat we het aanmelden bij microsoft accounts blokkeren. Microsoft's telemetrie en identiteitsassociatie wordt afgekeurd.
Als u deze diensten toch wilt gebruiken, zie dan de volgende issue tickets voor de oplossing:
- https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/1
- https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/16
- https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/22

## Een lijst van scripts en tools die deze collectie gebruikt:
-[Microsoft Security Compliance Toolkit 1.0](https://www.microsoft.com/en-us/download/details.aspx?id=55319)

## Aanvullende configuraties werden overwogen van:
-[BuiltByBel - PrivateZilla](https://github.com/builtbybel/privatezilla)
-[MelodysTweaks - Basic Tweaks](https://sites.google.com/view/melodystweaks/basictweaks)
-[Microsoft - Managing Windows 10 Telemetry and Callbacks](https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services)
-[Microsoft - Windows 10 Privacy](https://docs.microsoft.com/en-us/windows/privacy/)
-[Microsoft - Windows 10 VDI Recomendations](https://docs.microsoft.com/en-us/windows-server/remote/remote-desktop-services/rds_vdi-recommendations-1909)
-[Mirinsoft - SharpApp](https://github.com/builtbybel/sharpapp)
-[Mirinsoft - debotnet](https://github.com/builtbybel/debotnet)
-[UnderGroundWires - Privacy.S**Y](https://github.com/undergroundwires/privacy.sexy)
-[Sycnex - Windows10Debloater](https://github.com/Sycnex/Windows10Debloater)
-[The-Virtual-Desktop-Team - Virtual-Desktop-Optimization-Tool](https://github.com/The-Virtual-Desktop-Team/Virtual-Desktop-Optimization-Tool)
-[TheVDIGuys - Windows 10 VDI Optimize](https://github.com/TheVDIGuys/Windows_10_VDI_Optimize)
-[W4H4WK - Debloat Windows 10](https://github.com/W4RH4WK/Debloat-Windows-10/tree/master/scripts)

## Hoe voer je het script uit:
### Geautomatiseerde installatie:
Het script kan vanaf de uitgepakte GitHub-download als volgt worden gestart:
```powershell
iwr -useb 'https://simeononsecurity.ch/scripts/windowsoptimizeanddebloat.ps1'|iex
```
### Handmatige installatie:
Indien handmatig gedownload, moet het script worden gestart vanuit een administratieve powershell in de directory die alle bestanden van de[GitHub Repository](https://github.com/simeononsecurity/Windows-Optimize-Debloat)

Het script "sos-optimize-windows.ps1" bevat verschillende parameters waarmee het optimalisatieproces kan worden aangepast. Elke parameter is een booleaanse waarde die standaard op waar staat als hij niet is opgegeven.

- **$cleargpos**: Wist de instellingen voor Group Policy Objects.
- **$installupdates**: Installeert updates op het systeem.
- **$removebloatware**: Verwijdert onnodige programma's en functies van het systeem.
- **$disabletelemetrie**: Schakelt gegevensverzameling en telemetrie uit.
- **$privacy**: Brengt wijzigingen aan om de privacy te verbeteren.
- **$imagecleanup**: Verwijdert onnodige bestanden van het systeem.
- **$schijfcompressie**: Comprimeert de systeemschijf.
- **$updatemanagement**: Verandert de manier waarop updates worden beheerd en verbeterd op het systeem.
- **$sosbrowsers**: Optimaliseert de webbrowsers van het systeem.

Een voorbeeld van hoe het script te starten met specifieke parameters zou zijn:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
Get-ChildItem -Recurse *.ps1 | Unblock-File
powershell.exe -ExecutionPolicy ByPass -File .\sos-optimize-windows.ps1 -cleargpos:$false -installupdates:$false
```

