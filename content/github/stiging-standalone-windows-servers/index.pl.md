---
title: "Automatyzacja zgodności z Windows Server STIG za pomocą skryptów STIG"
date: 2020-09-09
---

**Pobierz wszystkie wymagane pliki z[GitHub Repository](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)

**Uwaga:** Ten skrypt powinien działać dla większości, jeśli nie wszystkich, systemów bez problemu. Podczas gdy[@SimeonOnSecurity](https://github.com/simeononsecurity) creates, reviews, and tests each repo intensively, we can not test every possible configuration nor does [@SimeonOnSecurity](https://github.com/simeononsecurity) take any responsibility for breaking your system. If something goes wrong, be prepared to submit an [issue](../../issues) Nie uruchamiaj tego skryptu, jeśli nie rozumiesz, co on robi. Twoim obowiązkiem jest przejrzenie i przetestowanie skryptu przed jego uruchomieniem.

## Ansible:
Obecnie oferujemy kolekcję playbooków dla tego skryptu. Proszę zapoznać się z następującymi informacjami:
-[Github Repo](https://github.com/simeononsecurity/Windows_STIG_Ansible)
-[Ansible Galaxy](https://galaxy.ansible.com/simeononsecurity/windows_stigs)

## Wprowadzenie:

Windows 10 jest niezabezpieczonym systemem operacyjnym po wyjęciu z pudełka i wymaga wielu zmian, aby ubezpieczyć[FISMA](https://www.cisa.gov/federal-information-security-modernization-act) zgodność.
Organizacje takie jak[Microsoft](https://microsoft.com), [Cyber.mil](https://public.cyber.mil), the [Department of Defense](https://dod.gov), and the [National Security Agency](https://www.nsa.gov/) mają zalecane i wymagane zmiany w konfiguracji w celu zablokowania, utwardzenia i zabezpieczenia systemu operacyjnego oraz zapewnienia zgodności z przepisami rządowymi. Zmiany te obejmują szeroki zakres środków zaradczych, w tym blokowanie telemetrii, makr, usuwanie bloatware i zapobieganie wielu fizycznym atakom na system.

Systemy autonomiczne są jednymi z najtrudniejszych i najbardziej irytujących systemów do zabezpieczenia. Jeśli nie są zautomatyzowane, wymagają ręcznych zmian w każdym STIG/SRG. W sumie ponad 1000 zmian konfiguracji w typowym wdrożeniu i średnio 5 minut na zmianę, co równa się 3,5 dnia pracy. Ten skrypt ma na celu znaczne przyspieszenie tego procesu.

## Uwagi:

- Ten skrypt jest przeznaczony do pracy w środowiskach **Enterprise** i zakłada, że masz wsparcie sprzętowe dla wszystkich wymagań.
  - Dla systemów osobistych proszę zobaczyć to[GitHub Repository](https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat)
- Ten skrypt nie jest przeznaczony do doprowadzenia systemu do 100% zgodności, raczej powinien być użyty jako krok do ukończenia większości, jeśli nie wszystkich, zmian konfiguracyjnych, które mogą być oskryptowane.
  - Pomijając dokumentację systemu, ten zbiór powinien doprowadzić Cię do około 95% zgodności ze wszystkimi zastosowanymi STIGS/SRGs.

## Wymagania:
- [X] Windows 10 Enterprise jest wymagany na STIG.
-[X] [Standards](https://docs.microsoft.com/en-us/windows-hardware/design/device-experiences/oem-highly-secure) dla wysoce bezpiecznego urządzenia z systemem Windows 10
-[X] System is [fully up to date](https://support.microsoft.com/en-gb/help/4027667/windows-10-update)
  - Uruchom[Windows 10 Upgrade Assistant](https://support.microsoft.com/en-us/help/3159635/windows-10-update-assistant) aby zaktualizować i sprawdzić najnowsze główne wydanie.
- X] Bitlocker musi być zawieszony lub wyłączony przed wykonaniem tego skryptu, może być ponownie włączony po ponownym uruchomieniu komputera.
  - Kolejne uruchomienia tego skryptu mogą być wykonywane bez wyłączania bitlockera.
- X] Wymagania sprzętowe.
  -[Hardware Requirements for Memory Integrity](https://docs.microsoft.com/en-us/windows/security/threat-protection/device-guard/requirements-and-deployment-planning-guidelines-for-virtualization-based-protection-of-code-integrity#baseline-protections) 
  -[Hardware Requirements for Virtualization-Based Security](https://docs.microsoft.com/en-us/windows-hardware/design/device-experiences/oem-vbs)
  -[Hardware Requirements for Windows Defender Application Guard](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-guard/reqs-wd-app-guard)
  -[Hardware Requirements for Windows Defender Credential Guard](https://docs.microsoft.com/en-us/windows/security/identity-protection/credential-guard/credential-guard-requirements)
  
## Zalecane materiały do czytania:
  -[System Guard Secure Launch](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-system-guard/system-guard-secure-launch-and-smm-protection#requirements-met-by-system-guard-enabled-machines)
  -[System Guard Root of Trust](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-system-guard/system-guard-how-hardware-based-root-of-trust-helps-protect-windows)
  -[Hardware-based Isolation](https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-atp/overview-hardware-based-isolation)
  -[Memory integrity](https://docs.microsoft.com/en-us/windows/security/threat-protection/device-guard/memory-integrity)
  -[Windows Defender Application Guard](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-guard/wd-app-guard-overview)
  -[Windows Defender Credential Guard](https://docs.microsoft.com/en-us/windows/security/identity-protection/credential-guard/credential-guard-how-it-works)

## Lista skryptów i narzędzi, które wykorzystuje ta kolekcja:
-[Cyber.mil - Group Policy Objects](https://public.cyber.mil/stigs/gpo/)
-[Microsoft Security Compliance Toolkit 1.0](https://www.microsoft.com/en-us/download/details.aspx?id=55319)

## Rozważano dodatkowe konfiguracje z:
-[Microsoft - Recommended block rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules)
-[Microsoft - Recommended driver block rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules)
-[Microsoft - Windows Defender Application Control](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/windows-defender-application-control-design-guide)
-[NSACyber - Application Whitelisting Using Microsoft AppLocker](https://apps.nsa.gov/iad/library/ia-guidance/tech-briefs/application-whitelisting-using-microsoft-applocker.cfm)
-[NSACyber - Hardware-and-Firmware-Security-Guidance](https://github.com/nsacyber/Hardware-and-Firmware-Security-Guidance)
-[NSACyber - Windows Secure Host Baseline](https://github.com/nsacyber/Windows-Secure-Host-Baseline)

## STIGS/SRGs Applied:
-[Adobe Acrobat Pro DC Continuous V2R1](https://public.cyber.mil/stigs/downloads/)
-[Adobe Acrobat Reader DC Continuous V2R1](https://public.cyber.mil/stigs/downloads/)
-[Firefox V5R2](https://public.cyber.mil/stigs/downloads/)
-[Google Chrome V2R4](https://public.cyber.mil/stigs/downloads/)
-[Internet Explorer 11 V1R19](https://public.cyber.mil/stigs/downloads/)
-[Microsoft Edge V1R2](https://public.cyber.mil/stigs/downloads/)
-[Microsoft .Net Framework 4 V1R9](https://public.cyber.mil/stigs/downloads/)
-[Microsoft Office 2013 V2R1](https://public.cyber.mil/stigs/downloads/)
-[Microsoft Office 2016 V2R1](https://public.cyber.mil/stigs/downloads/)
-[Microsoft Office 2019/Office 365 Pro Plus V2R3](https://public.cyber.mil/stigs/downloads/)
-[Microsoft OneDrive STIG V2R1](https://public.cyber.mil/stigs/downloads/)
-[Oracle JRE 8 V1R5](https://public.cyber.mil/stigs/downloads/)
-[Windows 10 V2R2](https://public.cyber.mil/stigs/downloads/)
-[Windows Firewall V1R7](https://public.cyber.mil/stigs/downloads/)

## Edycja polityk w Local Group Policy po fakcie:
- Zaimportuj definicje ADMX Policy z tego.[repo](https://github.com/simeononsecurity/STIG-Compliant-Domain-Prep/tree/master/Files/PolicyDefinitions) do *C:™WindowsPolicyDefinitions* na systemie, który próbujesz zmodyfikować.
- Otwórz```gpedit.msc``` w systemie, który próbujesz zmodyfikować.


## Jak uruchomić skrypt:
### Automated Install:
Skrypt można uruchomić z rozpakowanego pliku do pobrania z GitHuba w ten sposób:
```powershell
iex ((New-Object System.Net.WebClient).DownloadString('https://simeononsecurity.ch/scripts/standalonewindows.ps1'))
```

### Manual Install:
W przypadku ręcznego pobrania, skrypt musi być uruchomiony z katalogu zawierającego wszystkie pozostałe pliki z.[GitHub Repository](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)

Wszystkie parametry w skrypcie "secure-standalone.ps1" są opcjonalne i mają domyślną wartość $true. Oznacza to, że jeżeli podczas uruchamiania skryptu nie zostanie określona wartość parametru, będzie on traktowany tak, jakby był ustawiony na $true.

Skrypt przyjmuje następujące parametry, z których wszystkie są opcjonalne i domyślnie przyjmują wartość $true, jeżeli nie zostaną określone:

- **cleargpos**: (Boolean) Wyczyść GPO, które nie są używane.
- **installupdates**: (Boolean) Zainstaluj aktualizacje i zrestartuj w razie potrzeby.
- **adobe**: (Boolean) STIG Adobe Reader.
- **firefox**: (Boolean) STIG Firefox.
- **chrome**: (Boolean) STIG Chrome
- **IE11**: (Boolean) STIG Internet Explorer 11.
- **edge**: (Boolean) STIG Edge
- **dotnet**: (Boolean) STIG .NET Framework
- **office**: (Boolean) STIG Office
- **onedrive**: (Boolean) STIG OneDrive.
- **java**: (Boolean) STIG Java.
- **windows**: (Boolean) STIG Windows.
- **defender**: (Boolean) STIG Windows Defender.
- **firewall**: (Boolean) STIG Windows Firewall.
- **mitigations**: (Boolean) STIG Mitigations.
- **nessusPID**: (Boolean) Resolve Unquoted Strings in Path.
- **horizon**: (Boolean) STIG VMware Horizon
- **sosoptional**: (Boolean) Opcjonalne elementy STIG/Hardening

Przykładem uruchomienia skryptu ze wszystkimi domyślnymi parametrami byłoby:

```powershell
.\secure-standalone.ps1
```
Jeśli chcesz określić inną wartość dla jednego lub więcej parametrów, możesz dołączyć je do polecenia wraz z ich pożądaną wartością. Na przykład, gdybyś chciał uruchomić skrypt i ustawić parametr $firefox na $false, polecenie brzmiałoby:

```powershell
.\secure-standalone.ps1 -firefox $false
```

Można również określić wiele parametrów w poleceniu, jak np:

```powershell
.\secure-standalone.ps1 -firefox $false -chrome $false
```

Zauważ, że w tym przykładzie oba parametry Firefox i Chrome są ustawione na $false.



