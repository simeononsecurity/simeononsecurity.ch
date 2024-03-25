---
title: "Optimizați și întăriți-vă sistemul Windows cu scriptul Windows-Optimize-Harden-Debloat"
date: 2020-12-29
toc: true
draft: false
description: "Acest ghid cuprinzător oferă instrucțiuni pas cu pas despre cum să optimizați, să întăriți și să deblocați sistemul dvs. Windows pentru performanță, securitate și confidențialitate îmbunătățite."
tags: ["Optimizare Windows", "Întărirea ferestrelor", "Windows se deblochează", "securitate Windows", "Performanța Windows", "Confidențialitate Windows", "Actualizări Windows", "Obiecte de politică de grup", "Adobe Acrobat Reader", "Firefox", "Google Chrome", "Internet Explorer", "Microsoft Chromium Edge", "Dot Net 4", "Microsoft Office", "Onedrive", "Oracle Java JRE 8", "Windows Firewall", "Windows Defender", "Applocker"]
---
 Introducere:

Windows 10 și Windows 11 sunt sisteme de operare invazive și nesigure din cutie.
Organizații ca[PrivacyTools.io](https://PrivacyTools.io), [Microsoft](https://microsoft.com), [Cyber.mil](https://public.cyber.mil), the [Department of Defense](https://www.defense.gov/), and the [National Security Agency](https://www.nsa.gov/) au recomandat modificări de configurare pentru blocarea, consolidarea și securizarea sistemului de operare. Aceste modificări acoperă o gamă largă de atenuări, inclusiv blocarea telemetriei, macrocomenzi, eliminarea bloatware-ului și prevenirea multor atacuri digitale și fizice asupra unui sistem. Acest script are ca scop automatizarea configurațiilor recomandate de acele organizații.

## Note, avertismente și considerații:

**AVERTIZARE:**

Acest script ar trebui să funcționeze pentru majoritatea, dacă nu pentru toate, sistemele fără probleme. In timp ce[@SimeonOnSecurity](https://github.com/simeononsecurity) creates, reviews, and tests each repo intensively, we can not test every possible configuration nor does [@SimeonOnSecurity](https://github.com/simeononsecurity) take any responsibility for breaking your system. If something goes wrong, be prepared to submit an [issue](../../issues)

- Acest script este conceput pentru funcționarea în principal în medii de **Uz personal**. Având în vedere acest lucru, anumite setări de configurare a întreprinderii nu sunt implementate. Acest script nu este conceput pentru a aduce un sistem la conformitate 100%. Mai degrabă ar trebui să fie folosit ca o piatră de temelie pentru a finaliza majoritatea, dacă nu toate, modificările de configurare care pot fi scriptate în timp ce săriți peste problemele anterioare precum branding și bannere, unde acestea nu ar trebui implementate nici măcar într-un mediu de utilizare personală dur.
- Acest script este conceput în așa fel încât optimizările, spre deosebire de alte scripturi, să nu rupă funcționalitatea de bază a Windows.
- Funcții precum Windows Update, Windows Defender, Windows Store și Cortona au fost restricționate, dar nu sunt într-o stare disfuncțională ca majoritatea celorlalte scripturi de confidențialitate Windows 10.
- Dacă căutați un script minimizat țintit numai pentru medii comerciale, vă rugăm să vedeți acest lucru[GitHub Repository](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)


**Nu rulați acest script dacă nu înțelegeți ce face. Este responsabilitatea dvs. să revizuiți și să testați scriptul înainte de a-l rula.**

**DE EXEMPLU, URMĂTOARELE SE VOR RUPE DACĂ RELĂȚI ASTA FĂRĂ LUATĂ MĂSURI PREVENȚIVE:**

- Utilizarea contului de administrator implicit numit „Administrator” este dezactivată și redenumită conform DoD STIG

  - Nu se aplică contului implicit creat, dar se aplică utilizării contului de administrator implicit care se găsește adesea pe versiunile Enterprise, IOT și Windows Server

  - Creați un cont nou în Gestionare computer și setați-l ca administrator dacă doriți. Apoi copiați conținutul dosarului utilizatori anterior în cel nou după ce vă conectați la noul utilizator pentru prima dată pentru a rezolva acest lucru înainte de a rula scriptul.

- Conectarea folosind un cont Microsoft este dezactivată conform DoD STIG.

  - Când încercați să fiți sigur și privat, nu este recomandat să vă conectați la contul dvs. local printr-un cont Microsoft. Acest lucru este impus de acest repo.

  - Creați un cont nou în Gestionare computer și setați-l ca administrator dacă doriți. Apoi copiați conținutul dosarului utilizatori anterior în cel nou după ce vă conectați la noul utilizator pentru prima dată pentru a rezolva acest lucru înainte de a rula scriptul.

- PIN-urile contului sunt dezactivate conform DOD STIG

  - PIN-urile sunt nesigure atunci când sunt folosite numai în locul unei parole și pot fi ocolite cu ușurință în câteva ore sau eventual chiar secunde sau minute

  - Eliminați codul PIN din cont și/sau conectați-vă folosind parola după rularea scriptului.

- Valorile implicite ale Bitlocker sunt modificate și întărite datorită DoD STIG.

  - Datorită modului în care este implementat bitlocker, atunci când au loc aceste modificări și dacă aveți deja bitlocker activat, aceasta va întrerupe implementarea bitlocker.

  - Dezactivați bitlocker, rulați scriptul, apoi reactivați bitlocker pentru a rezolva această problemă.

## Cerințe:

- [x] Windows 10/11 Enterprise (**De preferat**) sau Professional
  - Edițiile Windows 10/11 Home nu acceptă configurații GPO și nu sunt testate.
  - Fereastra „N” Edițiile nu sunt testate.
-[x] [Standards](https://docs.microsoft.com/en-us/windows-hardware/design/device-experiences/oem-highly-secure) pentru un dispozitiv Windows 10 extrem de sigur
-[x] System is [fully up to date and supported](https://support.microsoft.com/en-gb/help/4027667/windows-10-update)
  - Rulați[Windows Upgrade Assistant](https://support.microsoft.com/en-us/help/3159635/windows-10-update-assistant) pentru a actualiza și a verifica cea mai recentă versiune majoră.
- [x] Bitlocker trebuie să fie suspendat sau dezactivat înainte de implementarea acestui script, acesta poate fi activat din nou după repornire.
  - Execuțiile ulterioare ale acestui script pot fi executate fără a dezactiva bitlocker.
- [x] Cerințe hardware
  -[Hardware Requirements for Memory Integrity](https://docs.microsoft.com/en-us/windows/security/threat-protection/device-guard/requirements-and-deployment-planning-guidelines-for-virtualization-based-protection-of-code-integrity#baseline-protections)
  -[Hardware Requirements for Virtualization-Based Security](https://docs.microsoft.com/en-us/windows-hardware/design/device-experiences/oem-vbs)
  -[Hardware Requirements for Windows Defender Application Guard](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-guard/reqs-wd-app-guard)
  -[Hardware Requirements for Windows Defender Credential Guard](https://docs.microsoft.com/en-us/windows/security/identity-protection/credential-guard/credential-guard-requirements)

## Material de lectură recomandat:

-[System Guard Secure Launch](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-system-guard/system-guard-secure-launch-and-smm-protection#requirements-met-by-system-guard-enabled-machines)
-[System Guard Root of Trust](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-system-guard/system-guard-how-hardware-based-root-of-trust-helps-protect-windows)
-[Hardware-based Isolation](https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-atp/overview-hardware-based-isolation)
-[Memory integrity](https://docs.microsoft.com/en-us/windows/security/threat-protection/device-guard/memory-integrity)
-[Windows Defender Application Guard](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-guard/wd-app-guard-overview)
-[Windows Defender Credential Guard](https://docs.microsoft.com/en-us/windows/security/identity-protection/credential-guard/credential-guard-how-it-works)

## Adăugiri, modificări notabile și remedieri de erori:

**Acest script adaugă, elimină și modifică setările sistemului dvs. Vă rugăm să examinați scriptul înainte de a-l rula.**

### Browsere:

- Browserele vor avea extensii suplimentare instalate pentru a ajuta la confidențialitate și securitate.
  - Vedea[here](https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/11) pentru informații suplimentare.
- Datorită STIG-urilor DoD implementate pentru browsere, managementul extensiilor și alte setări ale companiei sunt setate. Pentru instrucțiuni despre cum să vedeți aceste opțiuni, va trebui să vă uitați la instrucțiunile GPO de mai jos.

### Module Powershell:

- Pentru a ajuta la automatizarea actualizărilor Windows PowerShell[PSWindowsUpdate](https://www.powershellgallery.com/packages/PSWindowsUpdate/2.0.0.4) modulul va fi adăugat la sistemul dumneavoastră.

### Remedierea contului Microsoft, magazinului sau serviciilor Xbox:

Acest lucru se datorează faptului că blocăm conectarea la conturile Microsoft. Asocierea de telemetrie și identitate a Microsoft este descurajată.
Cu toate acestea, dacă încă doriți să utilizați aceste servicii, consultați următoarele bilete de emisiune pentru rezolvare:

- https://github.com/simeononsecurity/Windows-Optimize-Debloat/issues/1
- https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/16
- https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/22

### Editarea politicilor în Politica de grup local după fapt:

Dacă trebuie să modificați sau să schimbați o setare, acestea sunt cel mai probabil configurabile prin GPO:

- Importați definițiile politicii ADMX din aceasta[repo](https://github.com/simeononsecurity/STIG-Compliant-Domain-Prep/tree/master/Files/PolicyDefinitions) în _C:\windows\PolicyDefinitions_ pe sistemul pe care încercați să îl modificați.

- Deschideți `gpedit.msc` pe sistemul pe care încercați să îl modificați.

## O listă de scripturi și instrumente pe care le utilizează această colecție:

### Prima petrecere:

-[.NET-STIG-Script](https://github.com/simeononsecurity/.NET-STIG-Script)
-[Automate-Sysmon](https://github.com/simeononsecurity/Automate-Sysmon)
-[FireFox-STIG-Script](https://github.com/simeononsecurity/FireFox-STIG-Script)
-[JAVA-STIG-Script](https://github.com/simeononsecurity/JAVA-STIG-Script)
-[Standalone-Windows-STIG-Script](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)
-[Windows-Defender-STIG-Script](https://github.com/simeononsecurity/Windows-Defender-STIG-Script)
-[Windows-Optimize-Debloat](https://github.com/simeononsecurity/Windows-Optimize-Debloat)

### Terț:

-[Cyber.mil - Group Policy Objects](https://public.cyber.mil/stigs/gpo/)
-[Microsoft Security Compliance Toolkit 1.0](https://www.microsoft.com/en-us/download/details.aspx?id=55319)
-[Microsoft Sysinternals - Sysmon](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon)

## STIGS/SRG aplicate:

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

## Au fost luate în considerare configurații suplimentare din:

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

## Cum se rulează scriptul:
### GUI - Instalare ghidată:

Descărcați cea mai recentă versiune[here](https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat-GUI/releases/)alegeți opțiunile dorite și apăsați pe executare. <img src="https://raw.githubusercontent.com/simeononsecurity/Windows-Optimize-Harden-Debloat/master/.github/images/WOHD-GUI.gif" alt="Exemplu de instalare ghidată bazată pe GUI Windows-Optimize-Harden-Debloat"> ### Instalare automată: utilizați această linie pentru a descărca automat, a dezarhiva toate fișierele compatibile și a rula cea mai recentă versiune a scriptului.```powershell
iwr -useb 'https://simeononsecurity.com/scripts/windowsoptimizeandharden.ps1'|iex
```

<img src="https://raw.githubusercontent.com/simeononsecurity/Windows-Optimize-Harden-Debloat/master/.github/images/w10automatic.gif" alt="Example of 
Windows-Optimize-Harden-Debloat automatic install">

### Manual Install:

If manually downloaded, the script must be launched from an administrative powershell in the directory containing all the files from the [GitHub Repository](https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat)

The script "sos-optimize-windows.ps1" includes several parameters that allow for customization of the optimization process. Each parameter is a boolean value that defaults to true if not specified.

- **cleargpos**: Clears Group Policy Objects settings.
- **installupdates**: Installs updates to the system.
- **adobe**: Implements the Adobe Acrobat Reader STIGs.
- **firefox**: Implements the FireFox STIG.
- **chrome**: Implements the Google Chrome STIG.
- **IE11**: Implements the Internet Explorer 11 STIG.
- **edge**: Implements the Microsoft Chromium Edge STIG.
- **dotnet**: Implements the Dot Net 4 STIG.
- **office**: Implements the Microsoft Office Related STIGs.
- **onedrive**: Implements the Onedrive STIGs.
- **java**: Implements the Oracle Java JRE 8 STIG.
- **windows**: Implements the Windows Desktop STIGs.
- **defender**: Implements the Windows Defender STIG.
- **firewall**: Implements the Windows Firewall STIG.
- **mitigations**: Implements General Best Practice Mitigations.
- **defenderhardening**: Implements and Hardens Windows Defender Beyond STIG Requirements.
- **pshardening**: Implements PowerShell Hardening and Logging.
- **sslhardening**: Implements SSL Hardening.
- **smbhardening**: Hardens SMB Client and Server Settings.
- **applockerhardening**: Installs and Configures Applocker (In Audit Only Mode).
- **bitlockerhardening**: Harden Bitlocker Implementation.
- **removebloatware**: Removes unnecessary programs and features from the system.
- **disabletelemetry**: Disables data collection and telemetry.
- **privacy**: Makes changes to improve privacy.
- **imagecleanup**: Cleans up unneeded files from the system.
- **nessusPID**: Resolves Unquoted System Strings in Path.
- **sysmon**: Installs and configures sysmon to improve auditing capabilities.
- **diskcompression**: Compresses the system disk.
- **emet**: Implements STIG Requirements and Hardening for EMET on Windows 7 Systems.
- **updatemanagement**: Changes the way updates are managed and improved on the system.
- **deviceguard**: Enables Device Guard Hardening.
- **sosbrowsers**: Optimizes the system's web browsers.

An example of how to launch the script with specific parameters would be:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
Get-ChildItem -Recurse *.ps1 | Unblock-File
powershell.exe -ExecutionPolicy ByPass -File .\sos-optimize-windows.ps1 -cleargpos:$false -installupdates:$false
```
