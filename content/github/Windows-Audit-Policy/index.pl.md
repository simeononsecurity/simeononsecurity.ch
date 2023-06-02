---
title: "Maksymalizacja audytu systemu Windows za pomocą skryptu zasad audytu systemu Windows"
date: 2021-05-10
toc: true
draft: false
description: "Dowiedz się, jak zmaksymalizować audyt systemu Windows, wdrażając skrypt zasad audytu systemu Windows w celu zwiększenia bezpieczeństwa i monitorowania."
tags: ["Zasady audytu systemu Windows", "Audyt systemu Windows", "bezpieczeństwo", "monitoring", "auditpol", "Polecenia systemu Windows", "Bezpieczeństwo systemu Windows", "konfiguracja audytu", "polityki bezpieczeństwa", "dzienniki zdarzeń", "monitorowanie systemu", "Serwer Windows", "najlepsze praktyki bezpieczeństwa", "cyberbezpieczeństwo", "analiza dziennika", "zgodność z przepisami bezpieczeństwa", "reakcja na incydent", "narzędzia do monitorowania bezpieczeństwa", "uprzywilejowany dostęp", "Administracja systemem Windows", "skrypt", "administracja systemem", "bezpieczeństwo informacji", "audyt zgodności", "Hartowanie systemu Windows", "kontrole bezpieczeństwa", "automatyzacja zabezpieczeń", "zarządzanie logami", "Ustawienia zabezpieczeń systemu Windows"]
---

## Windows-Audit-Policy

[![VirusTotal Scan](https://github.com/simeononsecurity/Windows-Audit-Policy/actions/workflows/virustotal.yml/badge.svg)](https://github.com/simeononsecurity/Windows-Audit-Policy/actions/workflows/virustotal.yml)

Maksymalna wydajność audytu systemu Windows

## Zalecane materiały do czytania:
  - [auditpol](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/auditpol)
  - [auditpol clear](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/auditpol-clear)
  - [auditpol backup](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/auditpol-backup)
  - [auditpol restore](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/auditpol-restore)
  - [auditpol list](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/auditpol-list)

## Jak uruchomić skrypt
### Instalacja ręczna:
W przypadku ręcznego pobrania skrypt należy uruchomić z katalogu zawierającego wszystkie pozostałe pliki z pliku [GitHub Repository](https://github.com/simeononsecurity/Windows-Audit-Policy)
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
Get-ChildItem -Recurse *.ps1 | Unblock-File
.\sos-auditpolicy.ps1
```
