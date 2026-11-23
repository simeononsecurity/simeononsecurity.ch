---
title: "Windows 10 Systemweites Werbeblocker-Skript für mehr Datenschutz und Sicherheit"
date: 2021-04-02
lastmod: 2026-11-23
toc: true
draft: false
description: "Blockieren Sie unter Windows Domains aus der StevenBlack-Liste mit einem PowerShell-Skript, das eigene Einträge in der Hosts-Datei erhält."
tags: ["Windows 10", "Werbeblocker", "Telemetrieblockierung", "PowerShell-Skript", "systemweiter Werbeblocker", "Datenschutz", "Sicherheit"]
---

Blockieren Sie unter Windows Domains aus der StevenBlack-Liste mit einem PowerShell-Skript, das eigene Einträge in der Hosts-Datei erhält.

## Vorbereiten und prüfen

Laden Sie das vollständige Repository herunter und entpacken Sie es. Lesen Sie vor der Ausführung die [GitHub-README](https://github.com/simeononsecurity/System-Wide-Windows-Ad-Blocker/blob/main/README.md) und prüfen Sie das Skript. Öffnen Sie im entpackten Ordner Windows PowerShell 5.1 oder PowerShell 7 als Administrator. Testen Sie zuerst DNS und benötigte Anwendungen auf einem entbehrlichen Windows-Testsystem.

Zeigen Sie die Änderungen zunächst in der Vorschau an. Führen Sie den zweiten Befehl erst dann separat aus, wenn Sie die Änderungen übernehmen möchten.

```powershell
.\sos-system-wide-windows-ad-block.ps1 -WhatIf
```

```powershell
.\sos-system-wide-windows-ad-block.ps1
```

## Ursprüngliche Hosts-Datei wiederherstellen

Zeigen Sie zunächst die Vorschau der Wiederherstellung an. Führen Sie den zweiten Befehl erst dann separat aus, wenn Sie die Datei wiederherstellen möchten.

```powershell
.\sos-system-wide-windows-ad-block.ps1 -Mode Restore -WhatIf
```

```powershell
.\sos-system-wide-windows-ad-block.ps1 -Mode Restore
```

Bewahren Sie die Sicherung bis zur erfolgreichen Wiederherstellung unverändert auf. Wenn jemand oder eine Anwendung die Hosts-Datei nach der Anwendung geändert hat, bricht die Wiederherstellung ab. Sichern und übernehmen Sie diese Änderungen vor einem erneuten Versuch.

## Sperrliste

- [StevenBlack/hosts](https://github.com/StevenBlack/hosts)
- [Problem melden](https://github.com/simeononsecurity/System-Wide-Windows-Ad-Blocker/issues)
