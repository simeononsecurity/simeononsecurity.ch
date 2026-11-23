---
title: "Windows 10 System-Wide Ad Blocker Script dla lepszej prywatności i bezpieczeństwa"
date: 2021-04-02
lastmod: 2026-11-23
toc: true
draft: false
description: "Blokuj w systemie Windows domeny z listy StevenBlack za pomocą skryptu PowerShell, który zachowuje własne wpisy w pliku hosts."
tags: ["Windows 10", "ad-blocker", "blokowanie telemetrii", "Skrypt PowerShell", "systemowe blokowanie reklam", "prywatność", "bezpieczeństwo"]
---

Blokuj w systemie Windows domeny z listy StevenBlack za pomocą skryptu PowerShell, który zachowuje własne wpisy w pliku hosts.

## Przygotowanie i podgląd

Pobierz i rozpakuj całe repozytorium. Przed uruchomieniem przeczytaj [plik README w serwisie GitHub](https://github.com/simeononsecurity/System-Wide-Windows-Ad-Blocker/blob/main/README.md) i przejrzyj skrypt. W rozpakowanym folderze otwórz Windows PowerShell 5.1 lub PowerShell 7 jako administrator. Najpierw sprawdź DNS i potrzebne aplikacje na tymczasowym systemie Windows.

Najpierw sprawdź podgląd zmian. Drugie polecenie uruchom osobno dopiero wtedy, gdy chcesz je zastosować.

```powershell
.\sos-system-wide-windows-ad-block.ps1 -WhatIf
```

```powershell
.\sos-system-wide-windows-ad-block.ps1
```

## Przywracanie oryginalnego pliku hosts

Najpierw sprawdź podgląd przywracania. Drugie polecenie uruchom osobno dopiero wtedy, gdy chcesz przywrócić plik.

```powershell
.\sos-system-wide-windows-ad-block.ps1 -Mode Restore -WhatIf
```

```powershell
.\sos-system-wide-windows-ad-block.ps1 -Mode Restore
```

Nie zmieniaj kopii zapasowej do czasu pomyślnego przywrócenia. Jeśli ktoś lub aplikacja zmieni plik hosts po zastosowaniu zmian, przywracanie się zatrzyma. Zapisz i uzgodnij te zmiany przed ponowną próbą.

## Lista blokowania

- [StevenBlack/hosts](https://github.com/StevenBlack/hosts)
- [Zgłoś problem](https://github.com/simeononsecurity/System-Wide-Windows-Ad-Blocker/issues)
