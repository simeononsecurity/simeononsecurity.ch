---
title: "Anàlisis eficients de virus amb els mòduls VirusTotal PowerShell"
date: 2020-11-24
toc: true
draft: false
description: "Realitzeu exploracions eficients de virus amb els mòduls VirusTotal PowerShell automatitzant la interacció amb l'API de VirusTotal i racionalitzant el vostre flux de treball de seguretat."
tags: ["Mòduls PowerShell", "PowerShell", "Automatització", "VirusTotal", "Exploracions de virus", "Exploracions de dominis", "Clau de l'API", "API VirusTotal", "Pàgina de desenvolupadors de VirusTotal", "Administració de sistemes", "Flux de treball de seguretat", "Anàlisi de virus eficient", "Descarrega i instal·la", "Repositori GitHub", "Exemples d'ús de l'API"]
---
 col·lecció de mòduls de PowerShell per interactuar amb l'API VirusTotal

**Notes:**
- Necessitareu la vostra clau de l'API VirusTotal, que podeu trobar al vostre[Shodan Account](https://www.virustotal.com/gui/)
- Es poden trobar exemples de les API utilitzades en els mòduls a[VirusTotal Developers Page](https://developers.virustotal.com/reference#getting-started)

## Descarrega i instal·la
- Descarregar els mòduls des del[GitHub Repository](https://github.com/simeononsecurity/VirusTotal-PS)
- Instal·lar tots els mòduls
```ps
Get-ChildItem -Recurse *.ps1 | Import-Module
```