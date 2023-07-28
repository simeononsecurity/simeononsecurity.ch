---
title: "Analyses de virus efficaces avec les modules PowerShell de VirusTotal"
date: 2020-11-24
toc: true
draft: false
description: "Effectuez des analyses de virus efficaces avec les modules PowerShell de VirusTotal en automatisant l'interaction avec l'API de VirusTotal et en rationalisant votre flux de travail en matière de sécurité."
tags: ["Modules PowerShell", "PowerShell", "Automatisation", "VirusTotal", "Analyse des virus", "Balayage des domaines", "Clé API", "API de VirusTotal", "Page des développeurs de VirusTotal", "Administration des systèmes", "Flux de travail en matière de sécurité", "Analyse efficace des virus", "Télécharger et installer", "Dépôt GitHub", "Exemples d'utilisation de l'API"]
---
 Collection de modules PowerShell pour interagir avec l'API de VirusTotal

**Notes:**
- Vous aurez besoin de votre clé API VirusTotal, qui peut être trouvée sur votre compte [Shodan Account](https://www.virustotal.com/gui/)
- Des exemples d'API utilisées dans les modules peuvent être trouvés sur le site Web de la Commission européenne. [VirusTotal Developers Page](https://developers.virustotal.com/reference#getting-started)

## Téléchargement et installation
- Télécharger les modules à partir du site [GitHub Repository](https://github.com/simeononsecurity/VirusTotal-PS)
- Installer tous les modules
```ps
Get-ChildItem -Recurse *.ps1 | Import-Module
```