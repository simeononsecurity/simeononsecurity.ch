---
title: "Optymalizacja komputera z systemem Windows za pomocą Windows-Optimize-Debloat"
date: 2020-12-29
toc: true
draft: false
description: "Popraw wydajność i prywatność systemu operacyjnego Windows dzięki Windows-Optimize-Debloat, kompleksowemu skryptowi, który pomaga usunąć bloatware i zoptymalizować ustawienia systemu."
tags: ["Windows-Optimize-Debloat", "Optymalizacja systemu Windows", "Okna deblokujące", "Przyspieszenie działania systemu Windows", "Optymalizacja wydajności systemu Windows", "Zwiększenie wydajności systemu Windows", "Optymalizacja systemu Windows", "Microsoft", "Prywatność", "Usuwanie oprogramowania typu Bloatware", "Windows 10", "Windows 11", "Windows Defender", "Windows Update", "Cortona", "Obiekty polityki grupowej", "Telemetria", "Windows Store", "Windows 10 Professional", "Windows 10 Home"]
---


[![Test script against windows docker container](https://github.com/simeononsecurity/Windows-Optimize-Debloat/actions/workflows/test-with-docker.yml/badge.svg)](https://github.com/simeononsecurity/Windows-Optimize-Debloat/actions/workflows/test-with-docker.yml)

*Dla tych, którzy dążą do zminimalizowania swoich instalacji Windows 10 i 11.

**Uwaga:** Ten skrypt powinien działać dla większości, jeśli nie wszystkich, systemów bez problemu. Podczas gdy[@SimeonOnSecurity](https://github.com/simeononsecurity) creates, reviews, and tests each repo intensivly, we can not test every possible configuration nor does [@SimeonOnSecurity](https://github.com/simeononsecurity) take any responsibility for breaking your system. If something goes wrong, be prepared to submit an [issue](../../issues) Nie uruchamiaj tego skryptu, jeśli nie rozumiesz, co on robi.

## Wprowadzenie:
Windows 10 i 11 to inwazyjny i niezabezpieczony system operacyjny po wyjęciu z pudełka.
Organizacje takie jak np.[Microsoft](https://microsoft.com), [PrivacyTools.io](https://PrivacyTools.io) i inni zalecili zmiany w konfiguracji, aby zoptymalizować i zdebilizować system operacyjny Windows 10. Zmiany te obejmują blokowanie telemetrii, usuwanie logów i usuwanie bloatware, aby wymienić tylko kilka. Ten skrypt ma na celu zautomatyzowanie konfiguracji zalecanych przez te organizacje.

## Uwagi:
- Ten skrypt jest przeznaczony do pracy w środowiskach głównie **Personal Use**.
- Skrypt został zaprojektowany w taki sposób, aby optymalizacje, w przeciwieństwie do niektórych innych skryptów, nie naruszały podstawowych funkcji systemu Windows.
 - Funkcje takie jak Windows Update, Windows Defender, Windows Store i Cortona zostały ograniczone, ale nie są w stanie dysfunkcyjnym, jak większość innych skryptów Windows 10 Privacy.
- Jeśli szukasz zminimalizowanego skryptu skierowanego tylko do środowisk komercyjnych, zobacz to[GitHub Repository](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)

## Wymagania:
- [X] Windows 10/11 Enterprise, Windows 10 Professional lub Windows 10 Home.
  - Windows Home nie pozwala na konfiguracje GPO.
    - Skrypt nadal będzie działał, ale nie wszystkie ustawienia będą miały zastosowanie.
  - Windows "N" Editions nie są testowane.
  - Uruchom[Windows 10 Upgrade Assistant](https://support.microsoft.com/en-us/help/3159635/windows-10-update-assistant) aby zaktualizować i zweryfikować ostatnie główne wydanie.

## Naprawianie konta Microsoft lub usług Xbox:
Dzieje się tak dlatego, że blokujemy logowanie na konta microsoftowe. Telemetria Microsoftu i kojarzenie tożsamości są odrzucane.
Jednakże, jeśli nadal chcesz korzystać z tych usług, zobacz następujące issue tickets dla rozwiązania problemu:
- https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/1
- https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/16
- https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/22

## Lista skryptów i narzędzi, z których korzysta ta kolekcja:
-[Microsoft Security Compliance Toolkit 1.0](https://www.microsoft.com/en-us/download/details.aspx?id=55319)

## Rozważano dodatkowe konfiguracje z:
-[BuiltByBel - PrivateZilla](https://github.com/builtbybel/privatezilla)
-[MelodysTweaks - Basic Tweaks](https://sites.google.com/view/melodystweaks/basictweaks)
-[Microsoft - Managing Windows 10 Telemetry and Callbacks](https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services)
-[Microsoft - Windows 10 Privacy](https://docs.microsoft.com/en-us/windows/privacy/)
-[Microsoft - Windows 10 VDI Recomendations](https://docs.microsoft.com/en-us/windows-server/remote/remote-desktop-services/rds_vdi-recommendations-1909)
-[Mirinsoft - SharpApp](https://github.com/builtbybel/sharpapp)
-[Mirinsoft - debotnet](https://github.com/builtbybel/debotnet)
-[UnderGroundWires - Privacy.S**Y](https://github.com/undergroundwires/privacy.sexy)
-[Sycnex - Windows10Debloater](https://github.com/Sycnex/Windows10Debloater)
-[The-Virtual-Desktop-Team - Virtual-Desktop-Optimization-Tool](https://github.com/The-Virtual-Desktop-Team/Virtual-Desktop-Optimization-Tool)
-[TheVDIGuys - Windows 10 VDI Optimize](https://github.com/TheVDIGuys/Windows_10_VDI_Optimize)
-[W4H4WK - Debloat Windows 10](https://github.com/W4RH4WK/Debloat-Windows-10/tree/master/scripts)

## Jak uruchomić skrypt:
### Automated Install:
Skrypt można uruchomić z wyodrębnionego pobrania z GitHuba w ten sposób:
```powershell
iwr -useb 'https://simeononsecurity.ch/scripts/windowsoptimizeanddebloat.ps1'|iex
```
### Manual Install:
W przypadku ręcznego pobrania skryptu należy go uruchomić z administracyjnego powershella w katalogu zawierającym wszystkie pliki z.[GitHub Repository](https://github.com/simeononsecurity/Windows-Optimize-Debloat)

Skrypt "sos-optimize-windows.ps1" zawiera kilka parametrów, które pozwalają na dostosowanie procesu optymalizacji. Każdy parametr jest wartością logiczną, która domyślnie przyjmuje wartość true, jeśli nie jest określona.

- **$cleargpos**: Czyści ustawienia Group Policy Objects.
- **$installupdates**: Instaluje aktualizacje do systemu.
- **$removebloatware**: Usuwa z systemu niepotrzebne programy i funkcje.
- **$disabletelemetry**: Wyłącza zbieranie danych i telemetrię.
- **$privacy**: Wprowadza zmiany w celu poprawy prywatności.
- **$imagecleanup**: Czyści niepotrzebne pliki z systemu.
- **$diskcompression**: Kompresuje dysk systemowy.
- **$updatemanagement**: Zmienia sposób zarządzania i poprawiania aktualizacji w systemie.
- **$sosbrowsers**: Optymalizuje systemowe przeglądarki internetowe.

Przykładem uruchomienia skryptu z określonymi parametrami byłoby:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
Get-ChildItem -Recurse *.ps1 | Unblock-File
powershell.exe -ExecutionPolicy ByPass -File .\sos-optimize-windows.ps1 -cleargpos:$false -installupdates:$false
```

