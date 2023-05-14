---
title: "Automatyzacja aktywacji Windows KMS za pomocą skryptu GLVK"
date: 2020-12-18
toc: true
draft: false
description: "Uprość proces aktywacji Windows 10 KMS za pomocą skryptu GLVK Auto Install SimeonOnSecurity i dowiedz się więcej o kluczach klienckich KMS i GLVK z zalecanej lektury Microsoftu."
tags: ["Aktywacja systemu Windows", "Klucze klienckie KMS", "GLVK", "Aktualizacje systemu Windows", "Zgodność", "Skrypt Powershell", "Usługa zarządzania kluczami", "Licencjonowanie objętościowe", "Aktywacja przedsiębiorstwa", "Serwer zarządzania kluczami", "Automatyka", "Produkty Microsoft", "System operacyjny", "Oprogramowanie", "Środowiska korporacyjne", "Powershell administracyjny", "Repozytorium GitHub", "Skryptowanie", "Cybersecurity", "SimeonOnSecurity"]
---

Skrypt automatycznej instalacji GLVK do aktywacji KMS

## Rekomendowana lektura:
-[Microsoft - KMS Client Keys (GLVK)](https://docs.microsoft.com/en-us/windows-server/get-started/kmsclientkeys)

## Jak uruchomić skrypt:
### Manual Install:
W przypadku ręcznego pobrania, skrypt należy uruchomić z administracyjnego powershella w katalogu zawierającym wszystkie pliki z.[GitHub Repository](https://github.com/simeononsecurity/KMS-Auto-PS/archive/main.zip)
```ps
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
Get-ChildItem -Recurse *.ps1 | Unblock-File
.\sos-kmsglvkactivationauto.ps1
```
