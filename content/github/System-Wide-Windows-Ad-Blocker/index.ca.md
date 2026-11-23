---
title: "Windows 10 Script de bloqueig d'anuncis a tot el sistema per a una millor privadesa i seguretat"
date: 2021-04-02
lastmod: 2026-11-23
toc: true
draft: false
description: "Bloquegeu dominis de la llista StevenBlack al Windows amb un script de PowerShell que conserva les entrades personalitzades del fitxer hosts."
tags: ["Windows 10", "bloquejador d'anuncis", "bloqueig de telemetria", "Script de PowerShell", "bloqueig d'anuncis a tot el sistema", "privadesa", "seguretat"]
---

Bloquegeu dominis de la llista StevenBlack al Windows amb un script de PowerShell que conserva les entrades personalitzades del fitxer hosts.

## Preparació i previsualització

Baixeu i descomprimiu el repositori complet. Reviseu el [README de GitHub](https://github.com/simeononsecurity/System-Wide-Windows-Ad-Blocker/blob/main/README.md) i l'script abans d'executar-lo. Obriu Windows PowerShell 5.1 o PowerShell 7 com a administrador a la carpeta descomprimida. Proveu primer el DNS i les aplicacions necessàries en un sistema Windows de proves que pugueu descartar.

Previsualitzeu els canvis. Executeu la segona ordre per separat només quan vulgueu aplicar-los.

```powershell
.\sos-system-wide-windows-ad-block.ps1 -WhatIf
```

```powershell
.\sos-system-wide-windows-ad-block.ps1
```

## Restaureu el fitxer hosts original

Previsualitzeu la restauració. Executeu la segona ordre per separat només quan vulgueu restaurar el fitxer.

```powershell
.\sos-system-wide-windows-ad-block.ps1 -Mode Restore -WhatIf
```

```powershell
.\sos-system-wide-windows-ad-block.ps1 -Mode Restore
```

Conserveu intacta la còpia de seguretat fins que la restauració acabi correctament. Si algú o una aplicació modifica el fitxer hosts després d'aplicar els canvis, la restauració s'atura. Deseu i concilieu els canvis abans de tornar-ho a provar.

## Llista de bloqueig

- [StevenBlack/hosts](https://github.com/StevenBlack/hosts)
- [Informeu d'un problema](https://github.com/simeononsecurity/System-Wide-Windows-Ad-Blocker/issues)
