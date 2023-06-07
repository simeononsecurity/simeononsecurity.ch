---
title: "Optymalizacja, zabezpieczanie i ochrona wdrożeń systemu Windows 10 dzięki zautomatyzowanym zmianom konfiguracji"
date: 2020-07-22
---
 Utwardzanie i usuwanie wdrożeń systemu Windows 10**

**Pobierz wszystkie wymagane pliki ze strony [GitHub Repository](https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat)

**Poszukujemy pomocy w następujących kwestiach [.Net issue](https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/3) 

## Wprowadzenie:
Windows 10 jest inwazyjnym i niezabezpieczonym systemem operacyjnym po wyjęciu z pudełka.
Organizacje takie jak [PrivacyTools.io](https://PrivacyTools.io), [Microsoft](https://microsoft.com), [Cyber.mil](https://public.cyber.mil), the [Department of Defense](https://dod.gov), and the [National Security Agency](https://www.nsa.gov/) zaleciły zmiany konfiguracji w celu zablokowania, wzmocnienia i zabezpieczenia systemu operacyjnego. Zmiany te obejmują szeroki zakres środków zaradczych, w tym blokowanie telemetrii, makr, usuwanie oprogramowania typu bloatware oraz zapobieganie wielu cyfrowym i fizycznym atakom na system. Ten skrypt ma na celu zautomatyzowanie konfiguracji zalecanych przez te organizacje.

## Uwagi:
- Ten skrypt został zaprojektowany do działania głównie w środowiskach **użytku osobistego**. Mając to na uwadze, niektóre ustawienia konfiguracji korporacyjnej nie zostały zaimplementowane. Skrypt ten nie został zaprojektowany w celu zapewnienia 100% zgodności systemu. Powinien być raczej używany jako odskocznia do ukończenia większości, jeśli nie wszystkich, zmian konfiguracji, które można skryptować, pomijając kwestie takie jak branding i banery, które nie powinny być wdrażane nawet w zahartowanym środowisku do użytku osobistego.
- Ten skrypt został zaprojektowany w taki sposób, że optymalizacje, w przeciwieństwie do niektórych innych skryptów, nie złamią podstawowych funkcji systemu Windows.
 - Funkcje takie jak Windows Update, Windows Defender, Windows Store i Cortona zostały ograniczone, ale nie są w stanie niefunkcjonalnym, jak większość innych skryptów Windows 10 Privacy.
- Jeśli szukasz zminimalizowanego skryptu przeznaczonego tylko dla środowisk komercyjnych, zobacz to [GitHub Repository](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)

## Wymagania:
- [X] Windows 10 Enterprise (**preferowany**) lub Windows 10 Professional
  - Windows 10 Home nie zezwala na konfiguracje GPO.
  - Edycje "N" systemu Windows 10 nie są testowane.
- [X] [Standards](https://docs.microsoft.com/en-us/windows-hardware/design/device-experiences/oem-highly-secure) dla wysoce bezpiecznego urządzenia z systemem Windows 10
- [X] System is [fully up to date](https://support.microsoft.com/en-gb/help/4027667/windows-10-update)
  - Obecnie Windows 10 **v1909**, **v2004** lub **20H2**.
  - Uruchom aplikację [Windows 10 Upgrade Assistant](https://support.microsoft.com/en-us/help/3159635/windows-10-update-assistant) aby zaktualizować i zweryfikować najnowszą wersję główną.
- X] Bitlocker musi zostać zawieszony lub wyłączony przed wykonaniem tego skryptu, można go ponownie włączyć po ponownym uruchomieniu komputera.
  - Kolejne uruchomienia tego skryptu mogą być uruchamiane bez wyłączania bitlockera.
- X] Wymagania sprzętowe
  - [Hardware Requirements for Memory Integrity](https://docs.microsoft.com/en-us/windows/security/threat-protection/device-guard/requirements-and-deployment-planning-guidelines-for-virtualization-based-protection-of-code-integrity#baseline-protections) 
  - [Hardware Requirements for Virtualization-Based Security](https://docs.microsoft.com/en-us/windows-hardware/design/device-experiences/oem-vbs)
  - [Hardware Requirements for Windows Defender Application Guard](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-guard/reqs-wd-app-guard)
  - [Hardware Requirements for Windows Defender Credential Guard](https://docs.microsoft.com/en-us/windows/security/identity-protection/credential-guard/credential-guard-requirements)


## Zalecane materiały do czytania:
  - [System Guard Secure Launch](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-system-guard/system-guard-secure-launch-and-smm-protection#requirements-met-by-system-guard-enabled-machines)
  - [System Guard Root of Trust](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-system-guard/system-guard-how-hardware-based-root-of-trust-helps-protect-windows)
  - [Hardware-based Isolation](https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-atp/overview-hardware-based-isolation)
  - [Memory integrity](https://docs.microsoft.com/en-us/windows/security/threat-protection/device-guard/memory-integrity)
  - [Windows Defender Application Guard](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-guard/wd-app-guard-overview)
  - [Windows Defender Credential Guard](https://docs.microsoft.com/en-us/windows/security/identity-protection/credential-guard/credential-guard-how-it-works)

## Lista skryptów i narzędzi wykorzystywanych przez tę kolekcję:
- [Cyber.mil - Group Policy Objects](https://public.cyber.mil/stigs/gpo/)
- [Microsoft Security Compliance Toolkit 1.0](https://www.microsoft.com/en-us/download/details.aspx?id=55319)

## Uwzględniono dodatkowe konfiguracje z:
- [BuiltByBel - PrivateZilla](https://github.com/builtbybel/privatezilla)
- [CERT - IE Scripting Engine Memory Corruption](https://kb.cert.org/vuls/id/573168/)
- [Dirteam - SSL Hardening](https://dirteam.com/sander/2019/07/30/howto-disable-weak-protocols-cipher-suites-and-hashing-algorithms-on-web-application-proxies-ad-fs-servers-and-windows-servers-running-azure-ad-connect/)
- [Microsoft - Managing Windows 10 Telemetry and Callbacks](https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services)
- [Microsoft - Reduce attack surfaces with attack surface reduction rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-atp/attack-surface-reduction)
- [Microsoft - Recommended block rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules)
- [Microsoft - Recommended driver block rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules)
- [Microsoft - Specture and Meltdown Mitigations](https://support.microsoft.com/en-us/help/4072698/windows-server-speculative-execution-side-channel-vulnerabilities)
- [Microsoft - Windows 10 Privacy](https://docs.microsoft.com/en-us/windows/privacy/)
- [Microsoft - Windows 10 VDI Recomendations](https://docs.microsoft.com/en-us/windows-server/remote/remote-desktop-services/rds_vdi-recommendations-1909)
- [Microsoft - Windows Defender Application Control](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/windows-defender-application-control-design-guide)
- [Mirinsoft - SharpApp](https://github.com/builtbybel/sharpapp)
- [Mirinsoft - debotnet](https://github.com/builtbybel/debotnet)
- [NSACyber - Application Whitelisting Using Microsoft AppLocker](https://apps.nsa.gov/iad/library/ia-guidance/tech-briefs/application-whitelisting-using-microsoft-applocker.cfm)
- [NSACyber - Bitlocker Guidance](https://github.com/nsacyber/BitLocker-Guidance)
- [NSACyber - Hardware-and-Firmware-Security-Guidance](https://github.com/nsacyber/Hardware-and-Firmware-Security-Guidance)
- [NSACyber - Windows Secure Host Baseline](https://github.com/nsacyber/Windows-Secure-Host-Baseline)
- [UnderGroundWires - Privacy.S**Y](https://github.com/undergroundwires/privacy.sexy)
- [Sycnex - Windows10Debloater](https://github.com/Sycnex/Windows10Debloater)
- [The-Virtual-Desktop-Team - Virtual-Desktop-Optimization-Tool](https://github.com/The-Virtual-Desktop-Team/Virtual-Desktop-Optimization-Tool)
- [TheVDIGuys - Windows 10 VDI Optimize](https://github.com/TheVDIGuys/Windows_10_VDI_Optimize)
- [W4H4WK - Debloat Windows 10](https://github.com/W4RH4WK/Debloat-Windows-10/tree/master/scripts)
- [Whonix - Disable TCP Timestamps](https://www.whonix.org/wiki/Disable_TCP_and_ICMP_Timestamps)

## STIGS/SRGs Applied:
- [Adobe Reader Pro DC Classic V1R3](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Adobe_Acrobat_Pro_DC_Continuous_V1R2_STIG.zip)
- [Adobe Reader Pro DC Continous V1R2](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Adobe_Acrobat_Pro_DC_Classic_V1R3_STIG.zip)
- [Firefox V4R29](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MOZ_FireFox_V4R29_STIG.zip)
- [Google Chrome V1R19](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Google_Chrome_V1R19_STIG.zip)
- [Internet Explorer 11 V1R19](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MS_IE11_V1R19_STIG.zip)
- [Microsoft .Net Framework 4 V1R9](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MS_DotNet_Framework_4-0_V1R9_STIG.zip) - **Praca w toku**
- [Microsoft Office 2013 V1R5](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MicrosoftOffice2013_V1R5_Overview.zip)
- [Microsoft Office 2016 V1R2](https://dl.dod.cyber.mil/wp-content/uploads/stigs/pdf/U_Microsoft_Office_2016_V1R2_Overview.pdf)
- [Microsoft Office 2019/Office 365 Pro Plus V1R2](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MS_Office_365_ProPlus_V1R2_STIG.zip)
- [Microsoft OneDrive STIG V2R1](https://dl.cyber.mil/stigs/zip/U_MS_OneDrive_V2R1_STIG.zip)
- [Oracle JRE 8 V1R5](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Oracle_JRE_8_Windows_V1R5_STIG.zip)
- [Windows 10 V2R1](https://dl.cyber.mil/stigs/zip/U_MS_Windows_Defender_Antivirus_V2R1_STIG.zip)
- [Windows Defender Antivirus V2R1](https://dl.cyber.mil/stigs/zip/U_MS_Windows_Defender_Antivirus_V2R1_STIG.zip)
- [Windows Firewall V1R7](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Windows_Firewall_V1R7_STIG.zip)

## Jak uruchomić skrypt
### Instalacja ręczna:
W przypadku ręcznego pobrania skrypt należy uruchomić z poziomu administracyjnego powershell w katalogu zawierającym wszystkie pliki z pliku [GitHub Repository](https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat)
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
Get-ChildItem -Recurse *.ps1 | Unblock-File
.\sos-optimize-windows.ps1
```
### Automatyczna instalacja:
Skrypt można uruchomić z wyodrębnionego pliku do pobrania z GitHub w następujący sposób:
```powershell
iex ((New-Object System.Net.WebClient).DownloadString('https://simeononsecurity.ch/scripts/windowsoptimizeandharden.ps1'))
```
<img src="https://raw.githubusercontent.com/simeononsecurity/Windows-Optimize-Harden-Debloat/master/.github/images/w10automatic.gif" alt="Przykład automatycznej instalacji
Automatyczna instalacja Windows-Optimize-Harden-Debloat">.
