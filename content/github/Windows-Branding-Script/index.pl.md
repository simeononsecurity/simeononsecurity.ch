---
title: "Ulepszanie systemów Windows i serwerów: Przewodnik konfiguracji marki niestandardowej"
date: 2020-08-13
toc: true
draft: false
description: "Learn how to set up custom branding on Windows 10 and Server 2016/2019/2022 systems to personalize your user experience."
tags: ["Branding systemu Windows", "Branding serwera", "niestandardowy branding", "dostosowanie systemu", "konfiguracja marki", "Windows 10", "Server 2016", "Serwer 2019", "Serwer 2022", "doświadczenie użytkownika", "przewodnik dostosowywania systemu", "personalizacja", "branding systemu", "Dostosowywanie systemu Windows", "Dostosowywanie serwera", "Logo OEM", "obraz użytkownika", "wizerunek gościa", "skrypt brandingowy", "Microsoft Security Compliance Toolkit", "Konfiguracja marki Windows", "Konfiguracja marki serwera", "Niestandardowy przewodnik po marce", "spersonalizowany branding", "samouczek dostosowywania systemu", "Dostosowywanie systemu Windows", "Dostosowywanie systemu serwera", "obrazy brandingowe", "najlepsze praktyki brandingowe", "Wskazówki dotyczące dostosowywania systemu Windows", "Techniki dostosowywania serwera"]
---

**Setup branding w systemach Windows 10 i Server 2016/2019/2022**.

[![VirusTotal Scan](https://github.com/simeononsecurity/Windows-Branding-Script/actions/workflows/virustotal.yml/badge.svg)](https://github.com/simeononsecurity/Windows-Branding-Script/actions/workflows/virustotal.yml)

## Jak skonfigurować pliki brandingowe
- X] Zastąp wszystkie obrazy swoimi obrazami brandingowymi.
  - X] Logo OEM musi mieć wymiary 95x95 lub 120x20 i format ".bmp".
  - X] Wygeneruj obraz użytkownika wraz z wariantami 32x32, 40x40, 48x48, 192x192.
  - X] Wygeneruj lub skopiuj obraz użytkownika dla obrazu gościa.
  
## Ten skrypt wykorzystuje następujące narzędzie:
- [Microsoft Security Compliance Toolkit 1.0 - LGPO](https://www.microsoft.com/en-us/download/details.aspx?id=55319)

## Jak uruchomić skrypt
### Instalacja ręczna:
W przypadku ręcznego pobrania skrypt należy uruchomić z poziomu administracyjnego powershell w katalogu zawierającym wszystkie pliki z pliku [GitHub Repository](https://github.com/simeononsecurity/Windows-Branding-Script)
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
Get-ChildItem -Recurse *.ps1 | Unblock-File
.\sos-copybranding.ps1
```
### Automatyczna instalacja:
Skrypt można uruchomić z wyodrębnionego pliku do pobrania z GitHub w następujący sposób:
```powershell
iwr -useb 'https://simeononsecurity.ch/scripts/sosbranding.ps1'|iex
```

