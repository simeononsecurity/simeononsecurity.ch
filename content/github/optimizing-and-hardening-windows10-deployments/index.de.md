---
title: "Optimieren, härten und sichern Sie Windows 10-Bereitstellungen mit automatisierten Konfigurationsänderungen"
date: 2020-07-22
---
 Härten und Debloaten von Windows 10-Bereitstellungen**

**Laden Sie alle erforderlichen Dateien von der [GitHub Repository](https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat)

**Wir suchen Hilfe bei folgenden Aufgaben [.Net issue](https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/3) 

## Einführung:
Windows 10 ist von Haus aus ein invasives und unsicheres Betriebssystem.
Organisationen wie [PrivacyTools.io](https://PrivacyTools.io), [Microsoft](https://microsoft.com), [Cyber.mil](https://public.cyber.mil), the [Department of Defense](https://dod.gov), and the [National Security Agency](https://www.nsa.gov/) haben Konfigurationsänderungen empfohlen, um das Betriebssystem abzuschotten, zu härten und zu sichern. Diese Änderungen decken ein breites Spektrum von Maßnahmen ab, darunter das Blockieren von Telemetrie, Makros, das Entfernen von Bloatware und das Verhindern zahlreicher digitaler und physischer Angriffe auf ein System. Dieses Skript zielt darauf ab, die von diesen Organisationen empfohlenen Konfigurationen zu automatisieren.

## Hinweise:
- Dieses Skript ist in erster Linie für den Einsatz in **Personal Use**-Umgebungen konzipiert. Aus diesem Grund sind bestimmte Konfigurationseinstellungen für Unternehmen nicht implementiert. Dieses Skript ist nicht dazu gedacht, ein System auf 100%ige Konformität zu bringen. Es sollte vielmehr als Sprungbrett dienen, um die meisten, wenn nicht sogar alle Konfigurationsänderungen, die per Skript vorgenommen werden können, zu vervollständigen, wobei Probleme wie Branding und Banner übersprungen werden, die selbst in einer gehärteten persönlichen Umgebung nicht implementiert werden sollten.
- Dieses Skript ist so konzipiert, dass die Optimierungen, im Gegensatz zu anderen Skripten, die Kernfunktionen von Windows nicht beeinträchtigen.
 - Funktionen wie Windows Update, Windows Defender, der Windows Store und Cortona wurden zwar eingeschränkt, sind aber nicht in einem funktionsuntüchtigen Zustand wie die meisten anderen Skripte zum Schutz der Privatsphäre in Windows 10.
- Wenn Sie ein minimiertes Skript suchen, das nur auf kommerzielle Umgebungen ausgerichtet ist, lesen Sie bitte dieses [GitHub Repository](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)

## Anforderungen:
- [X] Windows 10 Enterprise (**Bevorzugt**) oder Windows 10 Professional
  - Windows 10 Home lässt keine GPO-Konfigurationen zu.
  - Windows 10 "N"-Editionen werden nicht getestet.
- [X] [Standards](https://docs.microsoft.com/en-us/windows-hardware/design/device-experiences/oem-highly-secure) für ein hochsicheres Windows 10-Gerät
- [X] System is [fully up to date](https://support.microsoft.com/en-gb/help/4027667/windows-10-update)
  - Derzeit Windows 10 **v1909**, **v2004**, oder **20H2**.
  - Führen Sie die [Windows 10 Upgrade Assistant](https://support.microsoft.com/en-us/help/3159635/windows-10-update-assistant) um die letzte Hauptversion zu aktualisieren und zu verifizieren.
- X] Bitlocker muss vor der Implementierung dieses Skripts angehalten oder deaktiviert werden, es kann nach einem Neustart wieder aktiviert werden.
  - Nachfolgende Durchläufe dieses Skripts können ohne Deaktivierung von Bitlocker ausgeführt werden.
- X] Hardware-Anforderungen
  - [Hardware Requirements for Memory Integrity](https://docs.microsoft.com/en-us/windows/security/threat-protection/device-guard/requirements-and-deployment-planning-guidelines-for-virtualization-based-protection-of-code-integrity#baseline-protections) 
  - [Hardware Requirements for Virtualization-Based Security](https://docs.microsoft.com/en-us/windows-hardware/design/device-experiences/oem-vbs)
  - [Hardware Requirements for Windows Defender Application Guard](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-guard/reqs-wd-app-guard)
  - [Hardware Requirements for Windows Defender Credential Guard](https://docs.microsoft.com/en-us/windows/security/identity-protection/credential-guard/credential-guard-requirements)


## Empfohlenes Lesematerial:
  - [System Guard Secure Launch](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-system-guard/system-guard-secure-launch-and-smm-protection#requirements-met-by-system-guard-enabled-machines)
  - [System Guard Root of Trust](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-system-guard/system-guard-how-hardware-based-root-of-trust-helps-protect-windows)
  - [Hardware-based Isolation](https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-atp/overview-hardware-based-isolation)
  - [Memory integrity](https://docs.microsoft.com/en-us/windows/security/threat-protection/device-guard/memory-integrity)
  - [Windows Defender Application Guard](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-guard/wd-app-guard-overview)
  - [Windows Defender Credential Guard](https://docs.microsoft.com/en-us/windows/security/identity-protection/credential-guard/credential-guard-how-it-works)

## Eine Liste der Skripte und Werkzeuge, die diese Sammlung verwendet:
- [Cyber.mil - Group Policy Objects](https://public.cyber.mil/stigs/gpo/)
- [Microsoft Security Compliance Toolkit 1.0](https://www.microsoft.com/en-us/download/details.aspx?id=55319)

## Zusätzliche Konfigurationen wurden berücksichtigt von:
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

## Angewandte STIGS/SRGs:
- [Adobe Reader Pro DC Classic V1R3](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Adobe_Acrobat_Pro_DC_Continuous_V1R2_STIG.zip)
- [Adobe Reader Pro DC Continous V1R2](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Adobe_Acrobat_Pro_DC_Classic_V1R3_STIG.zip)
- [Firefox V4R29](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MOZ_FireFox_V4R29_STIG.zip)
- [Google Chrome V1R19](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Google_Chrome_V1R19_STIG.zip)
- [Internet Explorer 11 V1R19](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MS_IE11_V1R19_STIG.zip)
- [Microsoft .Net Framework 4 V1R9](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MS_DotNet_Framework_4-0_V1R9_STIG.zip) - **Arbeiten in Arbeit**
- [Microsoft Office 2013 V1R5](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MicrosoftOffice2013_V1R5_Overview.zip)
- [Microsoft Office 2016 V1R2](https://dl.dod.cyber.mil/wp-content/uploads/stigs/pdf/U_Microsoft_Office_2016_V1R2_Overview.pdf)
- [Microsoft Office 2019/Office 365 Pro Plus V1R2](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MS_Office_365_ProPlus_V1R2_STIG.zip)
- [Microsoft OneDrive STIG V2R1](https://dl.cyber.mil/stigs/zip/U_MS_OneDrive_V2R1_STIG.zip)
- [Oracle JRE 8 V1R5](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Oracle_JRE_8_Windows_V1R5_STIG.zip)
- [Windows 10 V2R1](https://dl.cyber.mil/stigs/zip/U_MS_Windows_Defender_Antivirus_V2R1_STIG.zip)
- [Windows Defender Antivirus V2R1](https://dl.cyber.mil/stigs/zip/U_MS_Windows_Defender_Antivirus_V2R1_STIG.zip)
- [Windows Firewall V1R7](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Windows_Firewall_V1R7_STIG.zip)

## So führen Sie das Skript aus
### Manuelle Installation:
Wenn das Skript manuell heruntergeladen wird, muss es von einer administrativen Powershell aus in dem Verzeichnis gestartet werden, das alle Dateien aus der [GitHub Repository](https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat)
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
Get-ChildItem -Recurse *.ps1 | Unblock-File
.\sos-optimize-windows.ps1
```
### Automatisierte Installation:
Das Skript kann aus dem extrahierten GitHub-Download wie folgt gestartet werden:
```powershell
iex ((New-Object System.Net.WebClient).DownloadString('https://simeononsecurity.ch/scripts/windowsoptimizeandharden.ps1'))
```
<img src="https://raw.githubusercontent.com/simeononsecurity/Windows-Optimize-Harden-Debloat/master/.github/images/w10automatic.gif" alt="Beispiel für
Windows-Optimieren-Härten-Entbloaten automatische Installation">
