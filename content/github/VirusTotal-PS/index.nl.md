---
title: "Efficiënte virusscans met VirusTotal PowerShell-modules"
date: 2020-11-24
toc: true
draft: false
description: "Voer efficiënte virusscans uit met de VirusTotal PowerShell-modules door de interactie met de VirusTotal API te automatiseren en uw beveiligingsworkflow te stroomlijnen."
tags: ["PowerShell modules", "PowerShell", "Automatisering", "VirusTotal", "Virusscans", "Domeinscans", "API sleutel", "VirusTotal API", "VirusTotal Ontwikkelaars Pagina", "Systeembeheer", "Beveiligingsworkflow", "Efficiënte virusscans", "Downloaden en installeren", "GitHub archief", "Voorbeelden van API-gebruik"]
---
 verzameling PowerShell-modules voor interactie met de VirusTotal API

**Noten:**
- U hebt uw VirusTotal API-sleutel nodig, die u kunt vinden op uw[Shodan Account](https://www.virustotal.com/gui/)
- Voorbeelden van de in de modules gebruikte API's zijn te vinden op de[VirusTotal Developers Page](https://developers.virustotal.com/reference#getting-started)

## Downloaden en installeren
- Download de modules van de[GitHub Repository](https://github.com/simeononsecurity/VirusTotal-PS)
- Alle modules installeren
```ps
Get-ChildItem -Recurse *.ps1 | Import-Module
```