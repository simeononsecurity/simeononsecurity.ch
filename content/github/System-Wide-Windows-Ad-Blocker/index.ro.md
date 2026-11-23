---
title: "Windows 10 Script de blocare a reclamelor la nivel de sistem pentru o mai bună confidențialitate și securitate"
date: 2021-04-02
lastmod: 2026-11-23
toc: true
draft: false
description: "Blochează domeniile din lista StevenBlack în Windows cu un script PowerShell care păstrează intrările personalizate din fișierul hosts."
tags: ["Windows 10", "blocant de anunțuri", "blocarea telemetriei", "Script PowerShell", "blocarea reclamelor la nivelul întregului sistem", "intimitate", "Securitate"]
---

Blochează domeniile din lista StevenBlack în Windows cu un script PowerShell care păstrează intrările personalizate din fișierul hosts.

## Pregătire și previzualizare

Descarcă și extrage întregul depozit. Citește [fișierul README de pe GitHub](https://github.com/simeononsecurity/System-Wide-Windows-Ad-Blocker/blob/main/README.md) și verifică scriptul înainte de a-l rula. În dosarul extras, deschide Windows PowerShell 5.1 sau PowerShell 7 ca administrator. Testează mai întâi DNS și aplicațiile necesare pe un sistem Windows temporar.

Verifică întâi ce modificări ar fi făcute. Rulează a doua comandă separat numai când vrei să le aplici.

```powershell
.\sos-system-wide-windows-ad-block.ps1 -WhatIf
```

```powershell
.\sos-system-wide-windows-ad-block.ps1
```

## Restabilirea fișierului hosts original

Previzualizează mai întâi restabilirea. Rulează a doua comandă separat numai când vrei să restabilești fișierul.

```powershell
.\sos-system-wide-windows-ad-block.ps1 -Mode Restore -WhatIf
```

```powershell
.\sos-system-wide-windows-ad-block.ps1 -Mode Restore
```

Păstrează copia de rezervă intactă până când restabilirea reușește. Dacă cineva sau o aplicație modifică fișierul hosts după aplicare, restabilirea se oprește. Salvează și reconciliază aceste modificări înainte de a încerca din nou.

## Listă de blocare

- [StevenBlack/hosts](https://github.com/StevenBlack/hosts)
- [Raportează o problemă](https://github.com/simeononsecurity/System-Wide-Windows-Ad-Blocker/issues)
