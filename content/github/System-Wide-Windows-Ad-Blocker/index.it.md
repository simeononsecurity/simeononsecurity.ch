---
title: "Script di blocco degli annunci a livello di sistema di Windows 10 per una migliore privacy e sicurezza"
date: 2021-04-02
lastmod: 2026-11-23
toc: true
draft: false
description: "Blocca in Windows i domini dell’elenco StevenBlack con uno script PowerShell che conserva le voci personalizzate del file hosts."
tags: ["Windows 10", "blocco per annunci pubblicitari", "blocco della telemetria", "Script di PowerShell", "blocco degli annunci a livello di sistema", "intimità", "sicurezza"]
---

Blocca in Windows i domini dell’elenco StevenBlack con uno script PowerShell che conserva le voci personalizzate del file hosts.

## Preparazione e anteprima

Scarica ed estrai l’intero repository. Leggi il [README su GitHub](https://github.com/simeononsecurity/System-Wide-Windows-Ad-Blocker/blob/main/README.md) e controlla lo script prima di eseguirlo. Nella cartella estratta, apri Windows PowerShell 5.1 o PowerShell 7 come amministratore. Verifica prima il DNS e le applicazioni necessarie su un sistema Windows di prova che puoi eliminare.

Controlla prima l’anteprima delle modifiche. Esegui il secondo comando separatamente solo quando vuoi applicarle.

```powershell
.\sos-system-wide-windows-ad-block.ps1 -WhatIf
```

```powershell
.\sos-system-wide-windows-ad-block.ps1
```

## Ripristinare il file hosts originale

Controlla prima l’anteprima del ripristino. Esegui il secondo comando separatamente solo quando vuoi ripristinare il file.

```powershell
.\sos-system-wide-windows-ad-block.ps1 -Mode Restore -WhatIf
```

```powershell
.\sos-system-wide-windows-ad-block.ps1 -Mode Restore
```

Mantieni intatto il backup fino al completamento del ripristino. Se qualcuno o un’app modifica il file hosts dopo l’applicazione delle modifiche, il ripristino si interrompe. Salva e riconcilia le modifiche prima di riprovare.

## Elenco di blocco

- [StevenBlack/hosts](https://github.com/StevenBlack/hosts)
- [Segnala un problema](https://github.com/simeononsecurity/System-Wide-Windows-Ad-Blocker/issues)
