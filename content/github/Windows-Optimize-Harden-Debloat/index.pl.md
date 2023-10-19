---
title: "Optymalizacja i wzmocnienie systemu Windows za pomocą skryptu Windows-Optimize-Harden-Debloat"
date: 2020-12-29
toc: true
draft: false
description: "Ten kompleksowy przewodnik zawiera instrukcje krok po kroku, jak zoptymalizować, utwardzić i usunąć z systemu Windows, aby zwiększyć jego wydajność, bezpieczeństwo i prywatność."
tags: ["Optymalizacja systemu Windows", "Hartowanie systemu Windows", "Usuwanie skutków awarii systemu Windows", "Bezpieczeństwo systemu Windows", "Wydajność systemu Windows", "Prywatność systemu Windows", "Aktualizacje systemu Windows", "Obiekty polityki grupowej", "Adobe Acrobat Reader", "Firefox", "Google Chrome", "Internet Explorer", "Microsoft Chromium Edge", "Dot Net 4", "Microsoft Office", "Onedrive", "Oracle Java JRE 8", "Zapora systemu Windows", "Windows Defender", "Applocker"]
---
 Wprowadzenie:

Windows 10 i Windows 11 to inwazyjny i niezabezpieczony system operacyjny po wyjęciu z pudełka.
Organizacje takie jak np.[PrivacyTools.io](https://PrivacyTools.io), [Microsoft](https://microsoft.com), [Cyber.mil](https://public.cyber.mil), the [Department of Defense](https://dod.gov), and the [National Security Agency](https://www.nsa.gov/) zalecają zmiany w konfiguracji, aby zablokować, utwardzić i zabezpieczyć system operacyjny. Zmiany te obejmują szeroki zakres zabezpieczeń, w tym blokowanie telemetrii, makr, usuwanie bloatware'u oraz zapobieganie wielu cyfrowym i fizycznym atakom na system. Ten skrypt ma na celu zautomatyzowanie konfiguracji zalecanych przez te organizacje.

## Uwagi, ostrzeżenia i rozważania:

**OSTRZEŻENIE:**

Ten skrypt powinien działać dla większości, jeśli nie wszystkich systemów bez problemu. Podczas gdy[@SimeonOnSecurity](https://github.com/simeononsecurity) creates, reviews, and tests each repo intensively, we can not test every possible configuration nor does [@SimeonOnSecurity](https://github.com/simeononsecurity) take any responsibility for breaking your system. If something goes wrong, be prepared to submit an [issue](../../issues)

- Ten skrypt jest przeznaczony do pracy w środowiskach głównie **Użytku osobistego**. W związku z tym niektóre ustawienia konfiguracji przedsiębiorstwa nie są zaimplementowane. Ten skrypt nie jest przeznaczony do doprowadzenia systemu do 100% zgodności. Powinien być raczej wykorzystany jako krok do ukończenia większości, jeśli nie wszystkich, zmian konfiguracyjnych, które mogą być oskryptowane, pomijając takie kwestie jak branding i banery, które nie powinny być wdrożone nawet w utwardzonym środowisku użytku osobistego.
- Skrypt ten został zaprojektowany w taki sposób, że optymalizacje, w przeciwieństwie do niektórych innych skryptów, nie będą łamać podstawowych funkcji Windows.
- Funkcje takie jak Windows Update, Windows Defender, Sklep Windows i Cortona zostały ograniczone, ale nie są w stanie dysfunkcyjnym jak większość innych skryptów Windows 10 Privacy.
- Jeśli szukasz zminimalizowanego skryptu skierowanego tylko do środowisk komercyjnych, zobacz to[GitHub Repository](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)


**Nie uruchamiaj tego skryptu, jeśli nie rozumiesz, co on robi. Twoim obowiązkiem jest przejrzenie i przetestowanie skryptu przed jego uruchomieniem.**

**PRZYKŁADOWO, JEŚLI URUCHOMISZ TEN SKRYPT BEZ PODJĘCIA ODPOWIEDNICH KROKÓW ZAPOBIEGAWCZYCH, USZKODZENIU ULEGNĄ NASTĘPUJĄCE ELEMENTY:**

- Używanie domyślnego konta administratora o nazwie "Administrator" jest wyłączone i zmieniono jego nazwę zgodnie z DoD STIG.

  - Nie dotyczy domyślnie utworzonego konta, ale dotyczy korzystania z domyślnego konta administratora często występującego w wersjach Enterprise, IOT i Windows Server

  - Utwórz nowe konto w Zarządzaniu komputerem i ustaw je jako administratora, jeśli chcesz. Następnie skopiuj zawartość folderu poprzedniego użytkownika do nowego po pierwszym zalogowaniu się na nowego użytkownika, aby obejść ten problem przed uruchomieniem skryptu.

- Logowanie przy użyciu konta microsoft jest wyłączone zgodnie z DoD STIG.

  - Gdy staramy się być bezpieczni i prywatni, logowanie się na konto lokalne za pomocą konta Microsoft nie jest zalecane. Jest to wymuszone przez to repo.

  - Utwórz nowe konto w Zarządzaniu komputerem i ustaw je jako administrator, jeśli chcesz. Następnie skopiuj zawartość folderu poprzedniego użytkownika do nowego po pierwszym zalogowaniu się na nowego użytkownika, aby obejść ten problem przed uruchomieniem skryptu.

- PINy do kont są wyłączone zgodnie z DoD STIG

  - PIN-y są niezbyt bezpieczne, gdy są używane wyłącznie zamiast hasła i można je łatwo obejść w ciągu kilku godzin, a potencjalnie nawet sekund lub minut.

  - Usuń PIN z konta i/lub zaloguj się przy użyciu hasła po uruchomieniu skryptu.

- Domyślne ustawienia Bitlockera zostały zmienione i utwardzone w związku z DoD STIG.

  - Ze względu na to, jak Bitlocker jest zaimplementowany, kiedy te zmiany wystąpią i jeśli masz już włączony Bitlocker, złamie to implementację Bitlockera.

  - Wyłącz Bitlocker, uruchom skrypt, a następnie ponownie włącz Bitlocker, aby obejść ten problem.

## Wymagania:

- [x] Windows 10/11 Enterprise (**Preferowany**) lub Professional.
  - Edycje domowe Windows 10/11 nie obsługują konfiguracji GPO i nie są testowane.
  - Nie są testowane edycje Windows "N".
-[x] [Standards](https://docs.microsoft.com/en-us/windows-hardware/design/device-experiences/oem-highly-secure) dla wysoce bezpiecznego urządzenia z systemem Windows 10
-[x] System is [fully up to date and supported](https://support.microsoft.com/en-gb/help/4027667/windows-10-update)
  - Uruchom[Windows Upgrade Assistant](https://support.microsoft.com/en-us/help/3159635/windows-10-update-assistant) aby zaktualizować i sprawdzić najnowsze główne wydanie.
- x] Bitlocker musi być zawieszony lub wyłączony przed wykonaniem tego skryptu, może być ponownie włączony po ponownym uruchomieniu.
  - Kolejne uruchomienia tego skryptu mogą być wykonywane bez wyłączania bitlockera.
- Wymagania sprzętowe
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

## Dodatki, istotne zmiany i poprawki błędów:

**Ten skrypt dodaje, usuwa i zmienia ustawienia w systemie. Prosimy o zapoznanie się z treścią skryptu przed jego uruchomieniem.**

### Przeglądarki:

- Przeglądarki będą miały zainstalowane dodatkowe rozszerzenia pomagające w zachowaniu prywatności i bezpieczeństwa.
  - Zobacz.[here](https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/11) w celu uzyskania dodatkowych informacji.
- Ze względu na DoD STIGs wdrożone dla przeglądarek, zarządzanie rozszerzeniami i inne ustawienia przedsiębiorstwa są ustawione. Aby uzyskać instrukcje, jak zobaczyć te opcje, musisz spojrzeć na instrukcje GPO poniżej.

### Moduły Powershell:

- Aby pomóc w automatyzacji aktualizacji systemu Windows, PowerShell.[PSWindowsUpdate](https://www.powershellgallery.com/packages/PSWindowsUpdate/2.0.0.4) moduł zostanie dodany do twojego systemu.

### Naprawianie konta Microsoft, sklepu lub usług Xbox:

Dzieje się tak, ponieważ blokujemy logowanie na konta microsoftowe. Telemetria Microsoftu i kojarzenie tożsamości są odrzucane.
Jednakże, jeśli nadal chcesz korzystać z tych usług zobacz następujące issue tickets dla rozwiązania:

- https://github.com/simeononsecurity/Windows-Optimize-Debloat/issues/1
- https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/16
- https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/22

### Edycja polityk w Local Group Policy po fakcie:

Jeśli potrzebujesz zmodyfikować lub zmienić ustawienie, najprawdopodobniej są one konfigurowalne za pośrednictwem GPO:

- Zaimportuj definicje ADMX Policy z tego.[repo](https://github.com/simeononsecurity/STIG-Compliant-Domain-Prep/tree/master/Files/PolicyDefinitions) do _C:\NPolicyDefinitions_ na systemie, który próbujesz zmodyfikować.

- Otwórz`gpedit.msc` w systemie, który próbujesz zmodyfikować.

## Lista skryptów i narzędzi, z których korzysta ta kolekcja:

### Pierwsza strona:

-[.NET-STIG-Script](https://github.com/simeononsecurity/.NET-STIG-Script)
-[Automate-Sysmon](https://github.com/simeononsecurity/Automate-Sysmon)
-[FireFox-STIG-Script](https://github.com/simeononsecurity/FireFox-STIG-Script)
-[JAVA-STIG-Script](https://github.com/simeononsecurity/JAVA-STIG-Script)
-[Standalone-Windows-STIG-Script](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)
-[Windows-Defender-STIG-Script](https://github.com/simeononsecurity/Windows-Defender-STIG-Script)
-[Windows-Optimize-Debloat](https://github.com/simeononsecurity/Windows-Optimize-Debloat)

### Strona trzecia:

-[Cyber.mil - Group Policy Objects](https://public.cyber.mil/stigs/gpo/)
-[Microsoft Security Compliance Toolkit 1.0](https://www.microsoft.com/en-us/download/details.aspx?id=55319)
-[Microsoft Sysinternals - Sysmon](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon)

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
-[Windows Defender Antivirus V2R2](https://public.cyber.mil/stigs/downloads/)
-[Windows Firewall V1R7](https://public.cyber.mil/stigs/downloads/)

## Dodatkowe konfiguracje były rozważane od:

-[BuiltByBel - PrivateZilla](https://github.com/builtbybel/privatezilla)
-[CERT - IE Scripting Engine Memory Corruption](https://kb.cert.org/vuls/id/573168/)
-[Dirteam - SSL Hardening](https://dirteam.com/sander/2019/07/30/howto-disable-weak-protocols-cipher-suites-and-hashing-algorithms-on-web-application-proxies-ad-fs-servers-and-windows-servers-running-azure-ad-connect/)
-[MelodysTweaks - Basic Tweaks](https://sites.google.com/view/melodystweaks/basictweaks)
-[Microsoft - Managing Windows 10 Telemetry and Callbacks](https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services)
-[Microsoft - Reduce attack surfaces with attack surface reduction rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-atp/attack-surface-reduction)
-[Microsoft - Recommended block rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules)
-[Microsoft - Recommended driver block rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules)
-[Microsoft - Specture and Meltdown Mitigations](https://support.microsoft.com/en-us/help/4072698/windows-server-speculative-execution-side-channel-vulnerabilities)
-[Microsoft - Windows 10 Privacy](https://docs.microsoft.com/en-us/windows/privacy/)
-[Microsoft - Windows 10 VDI Recomendations](https://docs.microsoft.com/en-us/windows-server/remote/remote-desktop-services/rds_vdi-recommendations-1909)
-[Microsoft - Windows Defender Application Control](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/windows-defender-application-control-design-guide)
-[Mirinsoft - SharpApp](https://github.com/builtbybel/sharpapp)
-[Mirinsoft - debotnet](https://github.com/builtbybel/debotnet)
-[NSACyber - Application Whitelisting Using Microsoft AppLocker](https://apps.nsa.gov/iad/library/ia-guidance/tech-briefs/application-whitelisting-using-microsoft-applocker.cfm)
-[NSACyber - Bitlocker Guidance](https://github.com/nsacyber/BitLocker-Guidance)
-[NSACyber - Hardware-and-Firmware-Security-Guidance](https://github.com/nsacyber/Hardware-and-Firmware-Security-Guidance)
-[NSACyber - Windows Secure Host Baseline](https://github.com/nsacyber/Windows-Secure-Host-Baseline)
-[UnderGroundWires - Privacy.S\*\*Y](https://github.com/undergroundwires/privacy.sexy)
-[Sycnex - Windows10Debloater](https://github.com/Sycnex/Windows10Debloater)
-[The-Virtual-Desktop-Team - Virtual-Desktop-Optimization-Tool](https://github.com/The-Virtual-Desktop-Team/Virtual-Desktop-Optimization-Tool)
-[TheVDIGuys - Windows 10 VDI Optimize](https://github.com/TheVDIGuys/Windows_10_VDI_Optimize)
-[VectorBCO - windows-path-enumerate](https://github.com/VectorBCO/windows-path-enumerate)
-[W4H4WK - Debloat Windows 10](https://github.com/W4RH4WK/Debloat-Windows-10/tree/master/scripts)
-[Whonix - Disable TCP Timestamps](https://www.whonix.org/wiki/Disable_TCP_and_ICMP_Timestamps)

## Jak uruchomić skrypt:
### GUI - Guided Install:

Pobierz najnowszą wersję[here](https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat-GUI/releases/) wybierz żądane opcje i naciśnij execute.

<img src="https://raw.githubusercontent.com/simeononsecurity/Windows-Optimize-Harden-Debloat/master/.github/images/WOHD-GUI.gif" alt="Przykład
Windows-Optimize-Harden-Debloat GUI Based Guided Install">.

### Automatyzacja instalacji:

Użyj tego one-linera, aby automatycznie pobrać, rozpakować wszystkie pliki pomocnicze i uruchomić najnowszą wersję skryptu.

```powershell
iwr -useb 'https://simeononsecurity.com/scripts/windowsoptimizeandharden.ps1'|iex
```

<img src="https://raw.githubusercontent.com/simeononsecurity/Windows-Optimize-Harden-Debloat/master/.github/images/w10automatic.gif" alt="Przykład
Automatyczna instalacja Windows-Optimize-Harden-Debloat">.

### Manual Install:

W przypadku ręcznego pobrania, skrypt należy uruchomić z administracyjnego powershella w katalogu zawierającym wszystkie pliki z[GitHub Repository](https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat)

Skrypt "sos-optimize-windows.ps1" zawiera kilka parametrów, które pozwalają na dostosowanie procesu optymalizacji. Każdy parametr jest wartością logiczną, która domyślnie przyjmuje wartość true, jeśli nie jest określona.

- **cleargpos**: Czyści ustawienia Group Policy Objects.
- **installupdates**: Instaluje aktualizacje do systemu.
- **adobe**: Implementuje STIGs Adobe Acrobat Reader.
- **firefox**: Implementuje STIG FireFox.
- **chrome**: Implementuje STIG Google Chrome.
- **IE11**: Implementuje STIG Internet Explorer 11.
- **edge**: Implementuje STIG Microsoft Chromium Edge.
- **dotnet**: Implementuje STIG Dot Net 4.
- **office**: Implementuje STIGs związane z Microsoft Office.
- **onedrive**: Implementuje STIGs związane z Onedrive.
- **java**: Implementuje STIG Oracle Java JRE 8.
- **windows**: Implementuje STIGs Windows Desktop.
- **defender**: Implementuje STIG Windows Defender.
- **firewall**: Implementuje STIG Windows Firewall.
- **mitigacje**: Implementuje ogólne najlepsze praktyki łagodzące.
- **defenderhardening**: Implementuje i wzmacnia Windows Defender poza wymaganiami STIG.
- **pshardening**: Implementuje PowerShell Hardening i Logging.
- **sslhardening**: Implementuje SSL Hardening.
- **smbhardening**: Wzmacnia ustawienia klienta i serwera SMB.
- **applockerhardening**: Instaluje i konfiguruje Applocker (w trybie Audit Only).
- **bitlockerhardening**: Hartuje implementację Bitlockera.
- **removebloatware**: Usuwa z systemu niepotrzebne programy i funkcje.
- **disabletelemetry**: Wyłącza zbieranie danych i telemetrię.
- **privacy**: Wprowadza zmiany mające na celu poprawę prywatności.
- **imagecleanup**: Czyści niepotrzebne pliki z systemu.
- **nessusPID**: Rozwiązuje niecytowane ciągi systemowe w ścieżce.
- **sysmon**: Instaluje i konfiguruje sysmon, aby poprawić możliwości audytu.
- **diskcompression**: Kompresuje dysk systemowy.
- **emet**: Implementuje wymagania STIG i utwardzenie dla EMET na systemach Windows 7.
- **updatemanagement**: Zmienia sposób zarządzania i poprawiania aktualizacji w systemie.
- **deviceguard**: Włącza Hardening Device Guard.
- **sosbrowsers**: Optymalizuje systemowe przeglądarki internetowe.

Przykładem uruchomienia skryptu z określonymi parametrami będzie:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
Get-ChildItem -Recurse *.ps1 | Unblock-File
powershell.exe -ExecutionPolicy ByPass -File .\sos-optimize-windows.ps1 -cleargpos:$false -installupdates:$false
```
