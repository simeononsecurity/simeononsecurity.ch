---
title: "Automatyzacja zgodności z Windows 10 STIG za pomocą skryptu Powershell"
date: 2020-08-26
---

**Pobierz wszystkie wymagane pliki z[GitHub Repository](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)

**Szukamy pomocy w[.Net issue](https://github.com/simeononsecurity/W10-Optimize-and-Harden/issues/3) 

## Wprowadzenie:

Windows 10 jest niezabezpieczonym systemem operacyjnym po wyjęciu z pudełka i wymaga wielu zmian, aby ubezpieczyć[FISMA](https://www.cisa.gov/federal-information-security-modernization-act) zgodność.
Organizacje takie jak[Microsoft](https://microsoft.com), [Cyber.mil](https://public.cyber.mil), the [Department of Defense](https://dod.gov), and the [National Security Agency](https://www.nsa.gov/) mają zalecane i wymagane zmiany w konfiguracji w celu zablokowania, utwardzenia i zabezpieczenia systemu operacyjnego oraz zapewnienia zgodności z przepisami rządowymi. Zmiany te obejmują szeroki zakres środków zaradczych, w tym blokowanie telemetrii, makr, usuwanie bloatware i zapobieganie wielu fizycznym atakom na system.

Systemy autonomiczne są jednymi z najtrudniejszych i najbardziej irytujących systemów do zabezpieczenia. Jeśli nie są zautomatyzowane, wymagają ręcznych zmian w każdym STIG/SRG. W sumie ponad 1000 zmian konfiguracji w typowym wdrożeniu i średnio 5 minut na zmianę, co równa się 3,5 dnia pracy. Ten skrypt ma na celu znaczne przyspieszenie tego procesu.

## Uwagi:

- Ten skrypt jest przeznaczony do pracy w środowiskach **Enterprise** i zakłada, że masz wsparcie sprzętowe dla wszystkich wymagań.
  - Dla systemów osobistych proszę zobaczyć to[GitHub Repository](https://github.com/simeononsecurity/W10-Optimize-and-Harden)
- Ten skrypt nie jest przeznaczony do doprowadzenia systemu do 100% zgodności, raczej powinien być użyty jako krok do ukończenia większości, jeśli nie wszystkich, zmian konfiguracyjnych, które mogą być oskryptowane.
  - Pomijając dokumentację systemu, ten zbiór powinien doprowadzić Cię do około 95% zgodności ze wszystkimi zastosowanymi STIGS/SRGs.

## Wymagania:
- [X] Windows 10 Enterprise is **Required** per STIG.
-[x] [Standards](https://docs.microsoft.com/en-us/windows-hardware/design/device-experiences/oem-highly-secure) dla wysoce bezpiecznego urządzenia z systemem Windows 10
-[x] System is [fully up to date](https://support.microsoft.com/en-gb/help/4027667/windows-10-update)
  - Obecnie w systemie Windows 10 **v1909** lub **v2004**.
  - Uruchom.[Windows 10 Upgrade Assistant](https://support.microsoft.com/en-us/help/3159635/windows-10-update-assistant) do aktualizacji i weryfikacji najnowszego głównego wydania.
- Wymagania sprzętowe [X]
  -[Hardware Requirements for Memory Integrity](https://docs.microsoft.com/en-us/windows/security/threat-protection/device-guard/requirements-and-deployment-planning-guidelines-for-virtualization-based-protection-of-code-integrity#baseline-protections) 
  -[Hardware Requirements for Windows Defender Application Guard](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-guard/reqs-wd-app-guard)
  -[Hardware Requirements for Windows Defender Credential Guard](https://docs.microsoft.com/en-us/windows/security/identity-protection/credential-guard/credential-guard-requirements)
  
## Zalecane materiały do czytania:
  -[System Guard Secure Launch](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-system-guard/system-guard-secure-launch-and-smm-protection#requirements-met-by-system-guard-enabled-machines)
  -[System Guard Root of Trust](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-system-guard/system-guard-how-hardware-based-root-of-trust-helps-protect-windows)
  -[Hardware-based Isolation](https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-atp/overview-hardware-based-isolation)
  -[Memory integrity](https://docs.microsoft.com/en-us/windows/security/threat-protection/device-guard/memory-integrity)
  -[Windows Defender Application Guard](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-guard/wd-app-guard-overview)
  -[Windows Defender Credential Guard](https://docs.microsoft.com/en-us/windows/security/identity-protection/credential-guard/credential-guard-how-it-works)

## Lista skryptów i narzędzi, z których korzysta ta kolekcja:

-[Microsoft Security Compliance Toolkit 1.0](https://www.microsoft.com/en-us/download/details.aspx?id=55319)

-[Cyber.mil - Group Policy Objects](https://public.cyber.mil/stigs/gpo/)

-[NSACyber - Bitlocker Guidance](https://github.com/nsacyber/BitLocker-Guidance)

## Dodatkowe konfiguracje były rozważane od:

-[NSACyber - Hardware-and-Firmware-Security-Guidance](https://github.com/nsacyber/Hardware-and-Firmware-Security-Guidance)

-[NSACyber - Application Whitelisting Using Microsoft AppLocker](https://apps.nsa.gov/iad/library/ia-guidance/tech-briefs/application-whitelisting-using-microsoft-applocker.cfm)

## STIGS/SRGs Applied:
 
-[Windows 10 V1R23](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MS_Windows_10_V1R23_STIG.zip)

-[Windows Defender Antivirus V1R9](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MS_Windows_Defender_Antivirus_V1R9_STIG.zip)

-[Windows Firewall V1R7](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Windows_Firewall_V1R7_STIG.zip)

-[Internet Explorer 11 V1R19](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MS_IE11_V1R19_STIG.zip)

-[Adobe Reader Pro DC Continous V1R2](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Adobe_Acrobat_Pro_DC_Continuous_V1R2_STIG.zip)

-[Microsoft Office 2019/Office 365 Pro Plus V1R2](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MS_Office_365_ProPlus_V1R2_STIG.zip)

-[Microsoft Office 2016 V1R2](https://dl.dod.cyber.mil/wp-content/uploads/stigs/pdf/U_Microsoft_Office_2016_V1R2_Overview.pdf)

-[Microsoft Office 2013 V1R5](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MicrosoftOffice2013_V1R5_Overview.zip)

-[Google Chrome V1R19](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Google_Chrome_V1R19_STIG.zip)

-[Firefox V4R29](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MOZ_FireFox_V4R29_STIG.zip)

-[Microsoft .Net Framework 4 V1R9](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MS_DotNet_Framework_4-0_V1R9_STIG.zip) - **Work in Progress**

-[Oracle JRE 8 V1R5](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Oracle_JRE_8_Windows_V1R5_STIG.zip)

## Jak uruchomić skrypt

**Skrypt można uruchomić z wyodrębnionego pliku do pobrania z GitHuba w następujący sposób:**.
```
.\secure-standalone.ps1
```
Skrypt, którego będziemy używać musi być uruchomiony z katalogu zawierającego wszystkie pozostałe pliki z[GitHub Repository](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)
