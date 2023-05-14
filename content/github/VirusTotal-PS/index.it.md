---
title: "Scansioni virus efficienti con i moduli PowerShell di VirusTotal"
date: 2020-11-24
toc: true
draft: false
description: "Esegui scansioni antivirus efficienti con i moduli VirusTotal PowerShell automatizzando l'interazione con l'API VirusTotal e semplificando il tuo flusso di lavoro di sicurezza."
tags: ["Moduli di PowerShell", "PowerShell", "Automazione", "Virus Total", "Scansioni antivirus", "Scansioni del dominio", "Chiave dell'API", "API Virus Total", "Pagina degli sviluppatori di VirusTotal", "Amministrazione di sistema", "Flusso di lavoro sulla sicurezza", "Scansioni antivirus efficienti", "Scarica e installa", "Repository GitHub", "Esempi di utilizzo dell'API"]
---
 raccolta di moduli PowerShell per l'interazione con l'API VirusTotal

**Appunti:**
- Avrai bisogno della tua chiave API VirusTotal, che puoi trovare sul tuo[Shodan Account](https://www.virustotal.com/gui/)
- Esempi di API utilizzate nei moduli possono essere trovati su[VirusTotal Developers Page](https://developers.virustotal.com/reference#getting-started)

## Scarica e installa
- Scaricare i moduli dal[GitHub Repository](https://github.com/simeononsecurity/VirusTotal-PS)
- Installare tutti i moduli
```ps
Get-ChildItem -Recurse *.ps1 | Import-Module
```