---
title: "Automatisieren der Windows Server STIG-Konformität mit STIG-Skripten"
date: 2020-09-09
---

**Laden Sie alle erforderlichen Dateien von der Seite [GitHub Repository](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)

**Hinweis:** Dieses Skript sollte auf den meisten, wenn nicht allen Systemen problemlos funktionieren. Während [@SimeonOnSecurity](https://github.com/simeononsecurity) creates, reviews, and tests each repo intensively, we can not test every possible configuration nor does [@SimeonOnSecurity](https://github.com/simeononsecurity) take any responsibility for breaking your system. If something goes wrong, be prepared to submit an [issue](../../issues) Führen Sie dieses Skript nicht aus, wenn Sie nicht verstehen, was es tut. Es liegt in Ihrer Verantwortung, das Skript zu überprüfen und zu testen, bevor Sie es ausführen.

## Ansible:
Wir bieten jetzt eine Playbook-Sammlung für dieses Skript an. Bitte beachten Sie das Folgende:
- [Github Repo](https://github.com/simeononsecurity/Windows_STIG_Ansible)
- [Ansible Galaxy](https://galaxy.ansible.com/simeononsecurity/windows_stigs)

## Einleitung:

Windows 10 ist von Haus aus ein unsicheres Betriebssystem und erfordert viele Änderungen, um sicherzustellen, dass [FISMA](https://www.cisa.gov/federal-information-security-modernization-act) Einhaltung der Vorschriften.
Organisationen wie [Microsoft](https://microsoft.com), [Cyber.mil](https://public.cyber.mil), the [Department of Defense](https://dod.gov), and the [National Security Agency](https://www.nsa.gov/) haben empfohlene und erforderliche Konfigurationsänderungen vorgenommen, um das Betriebssystem zu sperren, zu härten und zu sichern und die Einhaltung der gesetzlichen Vorschriften zu gewährleisten. Diese Änderungen umfassen ein breites Spektrum an Abhilfemaßnahmen, darunter das Blockieren von Telemetrie, Makros, das Entfernen von Bloatware und das Verhindern vieler physischer Angriffe auf ein System.

Eigenständige Systeme gehören zu den am schwierigsten und lästigsten zu sichernden Systemen. Wenn sie nicht automatisiert sind, müssen die einzelnen STIG/SRGs manuell geändert werden. Bei einem typischen Einsatz werden insgesamt über 1000 Konfigurationsänderungen vorgenommen, und jede Änderung dauert durchschnittlich 5 Minuten, was einem Arbeitsaufwand von 3,5 Tagen entspricht. Dieses Skript zielt darauf ab, diesen Prozess erheblich zu beschleunigen.

## Anmerkungen:

- Dieses Skript ist für den Einsatz in **Unternehmen**-Umgebungen konzipiert und geht davon aus, dass Sie über Hardware-Unterstützung für alle Anforderungen verfügen.
  - Für persönliche Systeme lesen Sie bitte dieses [GitHub Repository](https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat)
- Dieses Skript ist nicht dazu gedacht, ein System zu 100 % konform zu machen. Es sollte vielmehr als Sprungbrett dienen, um die meisten, wenn nicht sogar alle Konfigurationsänderungen, die per Skript vorgenommen werden können, zu vollenden.
  - Abzüglich der Systemdokumentation sollte diese Sammlung die Konformität aller angewandten STIGS/SRGs auf etwa 95 % bringen.

## Anforderungen:
- [X] Windows 10 Enterprise ist pro STIG erforderlich.
- [X] [Standards](https://docs.microsoft.com/en-us/windows-hardware/design/device-experiences/oem-highly-secure) für ein hochsicheres Windows 10-Gerät
- [X] System is [fully up to date](https://support.microsoft.com/en-gb/help/4027667/windows-10-update)
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
- [Microsoft - Recommended block rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules)
- [Microsoft - Recommended driver block rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules)
- [Microsoft - Windows Defender Application Control](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/windows-defender-application-control-design-guide)
- [NSACyber - Application Whitelisting Using Microsoft AppLocker](https://apps.nsa.gov/iad/library/ia-guidance/tech-briefs/application-whitelisting-using-microsoft-applocker.cfm)
- [NSACyber - Hardware-and-Firmware-Security-Guidance](https://github.com/nsacyber/Hardware-and-Firmware-Security-Guidance)
- [NSACyber - Windows Secure Host Baseline](https://github.com/nsacyber/Windows-Secure-Host-Baseline)

## Angewandte STIGS/SRGs:
- [Adobe Acrobat Pro DC Continuous V2R1](https://public.cyber.mil/stigs/downloads/)
- [Adobe Acrobat Reader DC Continuous V2R1](https://public.cyber.mil/stigs/downloads/)
- [Firefox V5R2](https://public.cyber.mil/stigs/downloads/)
- [Google Chrome V2R4](https://public.cyber.mil/stigs/downloads/)
- [Internet Explorer 11 V1R19](https://public.cyber.mil/stigs/downloads/)
- [Microsoft Edge V1R2](https://public.cyber.mil/stigs/downloads/)
- [Microsoft .Net Framework 4 V1R9](https://public.cyber.mil/stigs/downloads/)
- [Microsoft Office 2013 V2R1](https://public.cyber.mil/stigs/downloads/)
- [Microsoft Office 2016 V2R1](https://public.cyber.mil/stigs/downloads/)
- [Microsoft Office 2019/Office 365 Pro Plus V2R3](https://public.cyber.mil/stigs/downloads/)
- [Microsoft OneDrive STIG V2R1](https://public.cyber.mil/stigs/downloads/)
- [Oracle JRE 8 V1R5](https://public.cyber.mil/stigs/downloads/)
- [Windows 10 V2R2](https://public.cyber.mil/stigs/downloads/)
- [Windows Firewall V1R7](https://public.cyber.mil/stigs/downloads/)

## Nachträgliches Bearbeiten von Richtlinien in der lokalen Gruppenrichtlinie:
- Importieren Sie die ADMX-Richtliniendefinitionen aus dieser [repo](https://github.com/simeononsecurity/STIG-Compliant-Domain-Prep/tree/master/Files/PolicyDefinitions) in *C:\windows\PolicyDefinitions* auf dem System, das Sie zu ändern versuchen.
- Öffnen ```gpedit.msc``` auf dem System, das Sie zu ändern versuchen.


## So führen Sie das Skript aus:
### Automatisierte Installation:
Das Skript kann wie folgt aus dem extrahierten GitHub-Download gestartet werden:
```powershell
iex ((New-Object System.Net.WebClient).DownloadString('https://simeononsecurity.com/scripts/standalonewindows.ps1'))
```

### Manuelle Installation:
Wenn das Skript manuell heruntergeladen wird, muss es aus dem Verzeichnis gestartet werden, das alle anderen Dateien aus dem [GitHub Repository](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)

Alle Parameter im Skript "secure-standalone.ps1" sind optional und haben den Standardwert $true. Das heißt, wenn bei der Ausführung des Skripts kein Wert für einen Parameter angegeben wird, wird er so behandelt, als wäre er auf $true gesetzt.

Das Skript benötigt die folgenden Parameter, die alle optional sind und standardmäßig auf $true gesetzt werden, wenn sie nicht angegeben werden:

- **cleargpos**: (Boolean) Löscht GPOs, die nicht verwendet werden
- **installupdates**: (Boolean) Installiert Updates und startet neu, wenn nötig
- **adobe**: (Boolean) STIG Adobe Reader
- **firefox**: (Boolean) STIG Firefox
- **chrome**: (Boolean) STIG Chrome
- **IE11**: (Boolescher Wert) STIG Internet Explorer 11
- **edge**: (Boolescher Wert) STIG Edge
- **dotnet**: (Boolescher Wert) STIG .NET Framework
- **office**: (Boolean) STIG Office
- **onedrive**: (Boolescher Wert) STIG OneDrive
- **java**: (Boolescher Wert) STIG Java
- **Windows**: (Boolean) STIG Windows
- **defender**: (Boolescher Wert) STIG Windows Defender
- **Firewall**: (Boolescher Wert) STIG Windows Firewall
- Mitigations**: (Boolean) STIG Mitigations
- **nessusPID**: (Boolean) Unquotierte Zeichenfolgen im Pfad auflösen
- Horizon**: (Boolean) STIG VMware Horizon
- **sosoptional**: (Boolean) Optionale STIG/Härtungselemente

Ein Beispiel für die Ausführung des Skripts mit allen Standardparametern wäre:

```powershell
.\secure-standalone.ps1
```
Wenn Sie für einen oder mehrere Parameter einen anderen Wert angeben möchten, können Sie sie zusammen mit dem gewünschten Wert in den Befehl aufnehmen. Wenn Sie zum Beispiel das Skript ausführen und den Parameter $firefox auf $false setzen möchten, würde der Befehl lauten:

```powershell
.\secure-standalone.ps1 -firefox $false
```

Sie können auch mehrere Parameter in dem Befehl angeben, etwa so:

```powershell
.\secure-standalone.ps1 -firefox $false -chrome $false
```

Beachten Sie, dass in diesem Beispiel sowohl der Firefox- als auch der Chrome-Parameter auf $false gesetzt sind.



