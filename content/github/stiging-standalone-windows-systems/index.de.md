---
title: "Automatisieren der Windows 10 STIG-Konformität mit Powershell-Skript"
date: 2020-08-26
---

**Laden Sie alle erforderlichen Dateien von der Seite [GitHub Repository](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)

**Wir suchen Hilfe bei folgenden Aufgaben [.Net issue](https://github.com/simeononsecurity/W10-Optimize-and-Harden/issues/3) 

## Einleitung:

Windows 10 ist von Haus aus ein unsicheres Betriebssystem und erfordert viele Änderungen, um sicherzustellen, dass [FISMA](https://www.cisa.gov/federal-information-security-modernization-act) Einhaltung der Vorschriften.
Organisationen wie [Microsoft](https://microsoft.com), [Cyber.mil](https://public.cyber.mil), the [Department of Defense](https://dod.gov), and the [National Security Agency](https://www.nsa.gov/) haben empfohlene und erforderliche Konfigurationsänderungen vorgenommen, um das Betriebssystem zu sperren, zu härten und zu sichern und die Einhaltung der gesetzlichen Vorschriften zu gewährleisten. Diese Änderungen umfassen ein breites Spektrum an Abhilfemaßnahmen, darunter das Blockieren von Telemetrie, Makros, das Entfernen von Bloatware und das Verhindern vieler physischer Angriffe auf ein System.

Eigenständige Systeme gehören zu den am schwierigsten und lästigsten zu sichernden Systemen. Wenn sie nicht automatisiert sind, müssen die einzelnen STIG/SRGs manuell geändert werden. Bei einem typischen Einsatz werden insgesamt über 1000 Konfigurationsänderungen vorgenommen, und jede Änderung dauert durchschnittlich 5 Minuten, was einem Arbeitsaufwand von 3,5 Tagen entspricht. Dieses Skript zielt darauf ab, diesen Prozess erheblich zu beschleunigen.

## Anmerkungen:

- Dieses Skript ist für den Einsatz in **Unternehmen**-Umgebungen konzipiert und geht davon aus, dass Sie über Hardware-Unterstützung für alle Anforderungen verfügen.
  - Für persönliche Systeme lesen Sie bitte dieses [GitHub Repository](https://github.com/simeononsecurity/W10-Optimize-and-Harden)
- Dieses Skript ist nicht dazu gedacht, ein System zu 100 % konform zu machen. Es sollte vielmehr als Sprungbrett dienen, um die meisten, wenn nicht sogar alle Konfigurationsänderungen, die per Skript vorgenommen werden können, zu vollenden.
  - Abzüglich der Systemdokumentation sollte diese Sammlung die Konformität aller angewandten STIGS/SRGs auf etwa 95 % bringen.

## Anforderungen:
- [X] Windows 10 Enterprise wird pro STIG **erforderlich**.
- [x] [Standards](https://docs.microsoft.com/en-us/windows-hardware/design/device-experiences/oem-highly-secure) für ein hochsicheres Windows 10-Gerät
- [x] System is [fully up to date](https://support.microsoft.com/en-gb/help/4027667/windows-10-update)
  - Derzeit Windows 10 **v1909** oder **v2004**.
  - Führen Sie die [Windows 10 Upgrade Assistant](https://support.microsoft.com/en-us/help/3159635/windows-10-update-assistant) zu aktualisieren und die letzte Hauptversion zu überprüfen.
- [X] Hardware-Anforderungen
  - [Hardware Requirements for Memory Integrity](https://docs.microsoft.com/en-us/windows/security/threat-protection/device-guard/requirements-and-deployment-planning-guidelines-for-virtualization-based-protection-of-code-integrity#baseline-protections) 
  - [Hardware Requirements for Windows Defender Application Guard](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-guard/reqs-wd-app-guard)
  - [Hardware Requirements for Windows Defender Credential Guard](https://docs.microsoft.com/en-us/windows/security/identity-protection/credential-guard/credential-guard-requirements)
  
## Empfohlenes Lesematerial:
  - [System Guard Secure Launch](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-system-guard/system-guard-secure-launch-and-smm-protection#requirements-met-by-system-guard-enabled-machines)
  - [System Guard Root of Trust](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-system-guard/system-guard-how-hardware-based-root-of-trust-helps-protect-windows)
  - [Hardware-based Isolation](https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-atp/overview-hardware-based-isolation)
  - [Memory integrity](https://docs.microsoft.com/en-us/windows/security/threat-protection/device-guard/memory-integrity)
  - [Windows Defender Application Guard](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-guard/wd-app-guard-overview)
  - [Windows Defender Credential Guard](https://docs.microsoft.com/en-us/windows/security/identity-protection/credential-guard/credential-guard-how-it-works)

## Eine Liste von Skripten und Tools, die diese Sammlung verwendet:

- [Microsoft Security Compliance Toolkit 1.0](https://www.microsoft.com/en-us/download/details.aspx?id=55319)

- [Cyber.mil - Group Policy Objects](https://public.cyber.mil/stigs/gpo/)

- [NSACyber - Bitlocker Guidance](https://github.com/nsacyber/BitLocker-Guidance)

## Zusätzliche Konfigurationen wurden von berücksichtigt:

- [NSACyber - Hardware-and-Firmware-Security-Guidance](https://github.com/nsacyber/Hardware-and-Firmware-Security-Guidance)

- [NSACyber - Application Whitelisting Using Microsoft AppLocker](https://apps.nsa.gov/iad/library/ia-guidance/tech-briefs/application-whitelisting-using-microsoft-applocker.cfm)

## Angewandte STIGS/SRGs:
 
- [Windows 10 V1R23](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MS_Windows_10_V1R23_STIG.zip)

- [Windows Defender Antivirus V1R9](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MS_Windows_Defender_Antivirus_V1R9_STIG.zip)

- [Windows Firewall V1R7](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Windows_Firewall_V1R7_STIG.zip)

- [Internet Explorer 11 V1R19](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MS_IE11_V1R19_STIG.zip)

- [Adobe Reader Pro DC Continous V1R2](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Adobe_Acrobat_Pro_DC_Continuous_V1R2_STIG.zip)

- [Microsoft Office 2019/Office 365 Pro Plus V1R2](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MS_Office_365_ProPlus_V1R2_STIG.zip)

- [Microsoft Office 2016 V1R2](https://dl.dod.cyber.mil/wp-content/uploads/stigs/pdf/U_Microsoft_Office_2016_V1R2_Overview.pdf)

- [Microsoft Office 2013 V1R5](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MicrosoftOffice2013_V1R5_Overview.zip)

- [Google Chrome V1R19](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Google_Chrome_V1R19_STIG.zip)

- [Firefox V4R29](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MOZ_FireFox_V4R29_STIG.zip)

- [Microsoft .Net Framework 4 V1R9](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MS_DotNet_Framework_4-0_V1R9_STIG.zip) - **Arbeiten in Arbeit**

- [Oracle JRE 8 V1R5](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Oracle_JRE_8_Windows_V1R5_STIG.zip)

## So führen Sie das Skript aus

**Das Skript kann aus dem extrahierten GitHub-Download wie folgt gestartet werden:**
```
.\secure-standalone.ps1
```
Das Skript, das wir verwenden werden, muss aus dem Verzeichnis gestartet werden, das alle anderen Dateien aus dem [GitHub Repository](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)
