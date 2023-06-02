---
title: "Windows Hardening CTF: Wzmocnij zabezpieczenia swojego urządzenia z systemem Windows na potrzeby wydarzeń Capture the Flag"
date: 2020-10-19
toc: true
draft: false
description: "Odkryj potężny skrypt, który zwiększa bezpieczeństwo systemu Windows, wdrażając różne środki zabezpieczające przed kompromitacją."
tags: ["Hartowanie systemu Windows", "Bezpieczeństwo systemu Windows", "scenariusz", "Urządzenie z systemem Windows", "wiersz polecenia", "LLMNR", "PowerShell", "SMB", "Znaczniki czasu TCP", "AppLocker", "Rejestrowanie systemu Windows", "DEP", "Konfiguracje EMET", "Tryb ograniczonego języka PowerShell", "Szyfrowanie SMB", "Łagodzenie skutków Spectre i Meltdown", "Windows Defender", "Zapora systemu Windows", "PSWindowsUpdate", "Aktualizacje systemu Windows", "skrypt utwardzający", "Zalecane zasady NSA", "Rejestrowanie systemu Windows i kontrole bezpieczeństwa", "Kontrola aplikacji Windows Defender", "Procedury redukcji powierzchni ataku w usłudze Windows Defender", "Ochrona w chmurze w usłudze Windows Defender", "Ochrona przed exploitami w usłudze Windows Defender", "Instalacja PSWindowsUpdate", "Ulepszenie zabezpieczeń urządzeń z systemem Windows", "Środki zabezpieczające system Windows", "wzmocnienie bezpieczeństwa systemu Windows"]
---

**Windows-Hardening-CTF**
Skrypt do hartowania systemu Windows, który utrudnia i utrudnia kompromitację urządzenia z systemem Windows.

## Co robi ten skrypt?
- Wyłącza wiersz polecenia
- Wyłącza LLMNR
- Wyłącza PowerShell v2
- Wyłącza kompresję SMB
- Wyłącza SMB v1
- Wyłącza SMB v2
- Wyłącza znaczniki czasu TCP
- Wyłącza WSMAN i PSRemoting
- Włącza funkcję AppLocker z zasadami zalecanymi przez NSA
- Włącza najlepsze praktyki rejestrowania i kontroli zabezpieczeń systemu Windows
- Włącza DEP
- Włącza konfiguracje EMET (dotyczy tylko systemów z zainstalowanym EMET)
- Włącza tryb języka powiązanego PowerShell
- Włącza rejestrowanie PowerShell
- Włącza szyfrowanie SMB
- Włącza łagodzenie skutków Spectre i Meltdown
- Włącza kontrolę aplikacji w usłudze Windows Defender
- Włącza funkcje redukcji powierzchni ataku w usłudze Windows Defender
- Włącza ochronę opartą na chmurze w usłudze Windows Defender
- Włącza ochronę przed exploitami w usłudze Windows Defender
- Włącza Zaporę systemu Windows i rejestrowanie
- Instaluje PSWindowsUpdate i instaluje wszystkie dostępne aktualizacje systemu Windows

## Pobierz wymagane pliki:

Pobierz wymagane pliki z witryny [GitHub Repository](https://github.com/simeononsecurity/Windows-Hardening-CTF)

## Jak uruchomić skrypt:

**Skrypt można uruchomić z wyodrębnionego pliku do pobrania z GitHub w następujący sposób:**.
```
.\sos-windows-hardening-ctf.ps1
```
