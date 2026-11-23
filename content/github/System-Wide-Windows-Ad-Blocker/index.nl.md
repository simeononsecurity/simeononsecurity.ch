---
title: "Windows 10-systeemwijde advertentieblokkeringsscript voor betere privacy en beveiliging"
date: 2021-04-02
lastmod: 2026-11-23
toc: true
draft: false
description: "Blokkeer domeinen uit de StevenBlack-lijst in Windows met een PowerShell-script dat aangepaste vermeldingen in het hosts-bestand behoudt."
tags: ["Windows 10", "ad-blocker", "telemetrie blokkering", "PowerShell script", "systeemwijde advertentieblokkering", "privacy", "beveiliging"]
---

Blokkeer domeinen uit de StevenBlack-lijst in Windows met een PowerShell-script dat aangepaste vermeldingen in het hosts-bestand behoudt.

## Voorbereiden en vooraf controleren

Download de volledige repository en pak deze uit. Lees de [GitHub-README](https://github.com/simeononsecurity/System-Wide-Windows-Ad-Blocker/blob/main/README.md) en controleer het script voordat je het uitvoert. Open Windows PowerShell 5.1 of PowerShell 7 als beheerder in de uitgepakte map. Test DNS en de benodigde apps eerst op een Windows-testsysteem dat je daarna kunt verwijderen.

Bekijk eerst welke wijzigingen het script voorstelt. Voer het tweede commando pas afzonderlijk uit als je de wijzigingen wilt toepassen.

```powershell
.\sos-system-wide-windows-ad-block.ps1 -WhatIf
```

```powershell
.\sos-system-wide-windows-ad-block.ps1
```

## Het oorspronkelijke hosts-bestand herstellen

Controleer eerst wat het herstel zal doen. Voer het tweede commando pas afzonderlijk uit als je het bestand wilt herstellen.

```powershell
.\sos-system-wide-windows-ad-block.ps1 -Mode Restore -WhatIf
```

```powershell
.\sos-system-wide-windows-ad-block.ps1 -Mode Restore
```

Laat de back-up intact tot het herstel is geslaagd. Als iemand of een app het hosts-bestand tussentijds heeft gewijzigd, stopt het herstel. Bewaar die wijzigingen en breng ze met elkaar in overeenstemming voordat je het opnieuw probeert.

## Blokkeerlijst

- [StevenBlack/hosts](https://github.com/StevenBlack/hosts)
- [Een probleem melden](https://github.com/simeononsecurity/System-Wide-Windows-Ad-Blocker/issues)
