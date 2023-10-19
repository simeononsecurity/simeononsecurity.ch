---
title: "Optymalizacja komputera z systemem Windows za pomocą Windows-Optimize-Debloat"
date: 2020-12-29
toc: true
draft: false
description: "Popraw wydajność i prywatność swojego systemu operacyjnego Windows za pomocą Windows-Optimize-Debloat, kompleksowego skryptu, który pomaga usunąć bloatware i zoptymalizować ustawienia systemowe."
tags: ["Windows-Optimize-Debloat", "Optymalizacja systemu Windows", "Debloating Windows", "Przyspieszenie systemu Windows", "Optymalizacja wydajności systemu Windows", "Zwiększenie wydajności systemu Windows", "Optymalizacja systemu Windows", "Microsoft", "Prywatność", "Usuwanie zbędnego oprogramowania", "Windows 10", "Windows 11", "Windows Defender", "Windows Update", "Cortona", "Obiekty zasad grupy", "Telemetria", "Sklep Windows", "Windows 10 Professional", "Windows 10 Home"]
---


[![Test script against windows docker container](https://github.com/simeononsecurity/Windows-Optimize-Debloat/actions/workflows/test-with-docker.yml/badge.svg)](https://github.com/simeononsecurity/Windows-Optimize-Debloat/actions/workflows/test-with-docker.yml)

*Dla tych, którzy chcą zminimalizować instalację Windows 10 i 11.

**Uwaga:** Ten skrypt powinien działać na większości, jeśli nie na wszystkich, systemach. Podczas gdy [@SimeonOnSecurity](https://github.com/simeononsecurity) creates, reviews, and tests each repo intensivly, we can not test every possible configuration nor does [@SimeonOnSecurity](https://github.com/simeononsecurity) take any responsibility for breaking your system. If something goes wrong, be prepared to submit an [issue](../../issues) Nie uruchamiaj tego skryptu, jeśli nie rozumiesz jego działania.

## Wprowadzenie:
Windows 10 i 11 są inwazyjnymi i niezabezpieczonymi systemami operacyjnymi po wyjęciu z pudełka.
Organizacje takie jak [Microsoft](https://microsoft.com), [PrivacyTools.io](https://PrivacyTools.io) i inni zalecili zmiany w konfiguracji w celu optymalizacji i zmniejszenia obciążenia systemu operacyjnego Windows 10. Zmiany te obejmują między innymi blokowanie telemetrii, usuwanie dzienników i usuwanie oprogramowania typu bloatware. Ten skrypt ma na celu zautomatyzowanie konfiguracji zalecanych przez te organizacje.

## Uwagi:
- Ten skrypt jest przeznaczony do działania głównie w środowiskach **użytku osobistego**.
- Ten skrypt został zaprojektowany w taki sposób, że optymalizacje, w przeciwieństwie do niektórych innych skryptów, nie złamią podstawowych funkcji systemu Windows.
 - Funkcje takie jak Windows Update, Windows Defender, Windows Store i Cortona zostały ograniczone, ale nie są w stanie niefunkcjonalnym, jak większość innych skryptów Windows 10 Privacy.
- Jeśli szukasz zminimalizowanego skryptu przeznaczonego tylko dla środowisk komercyjnych, zobacz to [GitHub Repository](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)

## Wymagania:
- [X] Windows 10/11 Enterprise, Windows 10 Professional lub Windows 10 Home
  - Windows Home nie pozwala na konfiguracje GPO.
    - Skrypt będzie nadal działał, ale nie wszystkie ustawienia zostaną zastosowane.
  - Edycje "N" systemu Windows nie są testowane.
  - Uruchom skrypt [Windows 10 Upgrade Assistant](https://support.microsoft.com/en-us/help/3159635/windows-10-update-assistant) aby zaktualizować i zweryfikować najnowszą wersję główną.

## Naprawianie konta Microsoft lub usług Xbox:
Dzieje się tak, ponieważ blokujemy logowanie do kont Microsoft. Telemetria i powiązanie tożsamości Microsoftu są źle widziane.
Jeśli jednak nadal chcesz korzystać z tych usług, zapoznaj się z poniższymi zgłoszeniami problemów, aby uzyskać rozwiązanie:
- https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/1
- https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/16
- https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/22

## Lista skryptów i narzędzi wykorzystywanych przez tę kolekcję:
- [Microsoft Security Compliance Toolkit 1.0](https://www.microsoft.com/en-us/download/details.aspx?id=55319)

## Uwzględniono dodatkowe konfiguracje z:
- [BuiltByBel - PrivateZilla](https://github.com/builtbybel/privatezilla)
- [MelodysTweaks - Basic Tweaks](https://sites.google.com/view/melodystweaks/basictweaks)
- [Microsoft - Managing Windows 10 Telemetry and Callbacks](https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services)
- [Microsoft - Windows 10 Privacy](https://docs.microsoft.com/en-us/windows/privacy/)
- [Microsoft - Windows 10 VDI Recomendations](https://docs.microsoft.com/en-us/windows-server/remote/remote-desktop-services/rds_vdi-recommendations-1909)
- [Mirinsoft - SharpApp](https://github.com/builtbybel/sharpapp)
- [Mirinsoft - debotnet](https://github.com/builtbybel/debotnet)
- [UnderGroundWires - Privacy.S**Y](https://github.com/undergroundwires/privacy.sexy)
- [Sycnex - Windows10Debloater](https://github.com/Sycnex/Windows10Debloater)
- [The-Virtual-Desktop-Team - Virtual-Desktop-Optimization-Tool](https://github.com/The-Virtual-Desktop-Team/Virtual-Desktop-Optimization-Tool)
- [TheVDIGuys - Windows 10 VDI Optimize](https://github.com/TheVDIGuys/Windows_10_VDI_Optimize)
- [W4H4WK - Debloat Windows 10](https://github.com/W4RH4WK/Debloat-Windows-10/tree/master/scripts)

## Jak uruchomić skrypt:
### Automatyczna instalacja:
Skrypt można uruchomić z wyodrębnionego pliku do pobrania z GitHub w następujący sposób:
```powershell
iwr -useb 'https://simeononsecurity.com/scripts/windowsoptimizeanddebloat.ps1'|iex
```
### Instalacja ręczna:
W przypadku ręcznego pobrania skrypt należy uruchomić z poziomu administracyjnego powershell w katalogu zawierającym wszystkie pliki z pliku [GitHub Repository](https://github.com/simeononsecurity/Windows-Optimize-Debloat)

Skrypt "sos-optimize-windows.ps1" zawiera kilka parametrów, które pozwalają na dostosowanie procesu optymalizacji. Każdy parametr jest wartością logiczną, która domyślnie przyjmuje wartość true, jeśli nie zostanie określona.

- **$cleargpos**: Czyści ustawienia obiektów zasad grupy.
- **$installupdates**: Instaluje aktualizacje w systemie.
- **$removebloatware**: Usuwa niepotrzebne programy i funkcje z systemu.
- **$disabletelemetry**: Wyłącza zbieranie danych i telemetrię.
- **$privacy**: Wprowadza zmiany poprawiające prywatność.
- **$imagecleanup**: Usuwa niepotrzebne pliki z systemu.
- **$diskcompression**: Kompresuje dysk systemowy.
- **$updatemanagement**: Zmienia sposób, w jaki aktualizacje są zarządzane i ulepszane w systemie.
- **$sosbrowsers**: Optymalizuje systemowe przeglądarki internetowe.

Przykładem uruchomienia skryptu z określonymi parametrami może być:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
Get-ChildItem -Recurse *.ps1 | Unblock-File
powershell.exe -ExecutionPolicy ByPass -File .\sos-optimize-windows.ps1 -cleargpos:$false -installupdates:$false
```

