---
title: "Optimieren und härten Sie Ihr Windows-System mit dem Windows-Optimize-Harden-Debloat-Skript"
date: 2020-12-29
toc: true
draft: false
description: "Diese umfassende Anleitung bietet Schritt-für-Schritt-Anleitungen zum Optimieren, Härten und Entlasten Ihres Windows-Systems für mehr Leistung, Sicherheit und Datenschutz."
tags: ["Windows-Optimierung", "Windows-Härtung", "Windows debloiert", "Windows-Sicherheit", "Windows-Leistung", "Windows-Datenschutz", "Windows-Updates", "Gruppenrichtlinienobjekte", "Adobe Acrobat Reader", "Feuerfuchs", "Google Chrome", "Internet Explorer", "Microsoft Chromium Edge", "Punktnetz 4", "Microsoft Office", "Eine Fahrt", "Oracle Java JRE 8", "Windows-Firewall", "Windows Defender", "Applocker"]
---
 Einführung:

Windows 10 und Windows 11 sind standardmäßig invasive und unsichere Betriebssysteme.
Organisationen mögen[PrivacyTools.io](https://PrivacyTools.io), [Microsoft](https://microsoft.com), [Cyber.mil](https://public.cyber.mil), the [Department of Defense](https://www.defense.gov/), and the [National Security Agency](https://www.nsa.gov/) Wir haben Konfigurationsänderungen empfohlen, um das Betriebssystem zu sperren, zu härten und zu sichern. Diese Änderungen decken ein breites Spektrum an Abhilfemaßnahmen ab, darunter das Blockieren von Telemetriedaten und Makros, das Entfernen von Bloatware und das Verhindern zahlreicher digitaler und physischer Angriffe auf ein System. Dieses Skript zielt darauf ab, die von diesen Organisationen empfohlenen Konfigurationen zu automatisieren.

## Hinweise, Warnungen und Überlegungen:

**WARNUNG:**

Dieses Skript sollte auf den meisten, wenn nicht allen Systemen problemlos funktionieren. Während[@SimeonOnSecurity](https://github.com/simeononsecurity) creates, reviews, and tests each repo intensively, we can not test every possible configuration nor does [@SimeonOnSecurity](https://github.com/simeononsecurity) take any responsibility for breaking your system. If something goes wrong, be prepared to submit an [issue](../../issues)

– Dieses Skript ist hauptsächlich für den Einsatz in Umgebungen zur **persönlichen Nutzung** konzipiert. Aus diesem Grund sind bestimmte Unternehmenskonfigurationseinstellungen nicht implementiert. Dieses Skript ist nicht dazu gedacht, ein System zu 100 % konform zu machen. Vielmehr sollte es als Sprungbrett genutzt werden, um die meisten, wenn nicht alle Konfigurationsänderungen, die per Skript vorgenommen werden können, abzuschließen und gleichzeitig Probleme wie Branding und Banner zu überspringen, bei denen diese nicht einmal in einer gehärteten Umgebung für den persönlichen Gebrauch implementiert werden sollten.
– Dieses Skript ist so konzipiert, dass die Optimierungen im Gegensatz zu einigen anderen Skripten die Kernfunktionen von Windows nicht beeinträchtigen.
– Funktionen wie Windows Update, Windows Defender, der Windows Store und Cortona wurden eingeschränkt, befinden sich jedoch nicht in einem dysfunktionalen Zustand wie die meisten anderen Windows 10-Datenschutzskripte.
- Wenn Sie ein minimiertes Skript suchen, das nur für kommerzielle Umgebungen gedacht ist, sehen Sie sich bitte dieses an[GitHub Repository](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)


**Führen Sie dieses Skript nicht aus, wenn Sie nicht verstehen, was es tut. Es liegt in Ihrer Verantwortung, das Skript vor der Ausführung zu überprüfen und zu testen.**

**Beispielsweise führt Folgendes zu Fehlfunktionen, wenn Sie dies ausführen, ohne vorbeugende Maßnahmen zu ergreifen:**

– Die Verwendung des Standardadministratorkontos mit dem Namen „Administrator“ ist gemäß DoD STIG deaktiviert und umbenannt

  – Gilt nicht für das erstellte Standardkonto, sondern für die Verwendung des Standardadministratorkontos, das häufig in Enterprise-, IOT- und Windows Server-Versionen zu finden ist

  - Erstellen Sie unter Computerverwaltung ein neues Konto und legen Sie es bei Bedarf als Administrator fest. Kopieren Sie dann den Inhalt des vorherigen Benutzerordners in den neuen, nachdem Sie sich zum ersten Mal beim neuen Benutzer angemeldet haben, um dieses Problem zu umgehen, bevor Sie das Skript ausführen.

– Die Anmeldung mit einem Microsoft-Konto ist gemäß DoD STIG deaktiviert.

  - Wenn Sie Sicherheit und Privatsphäre gewährleisten möchten, wird davon abgeraten, sich über ein Microsoft-Konto bei Ihrem lokalen Konto anzumelden. Dies wird durch dieses Repo erzwungen.

  - Erstellen Sie unter Computerverwaltung ein neues Konto und legen Sie es bei Bedarf als Administrator fest. Kopieren Sie dann den Inhalt des vorherigen Benutzerordners in den neuen, nachdem Sie sich zum ersten Mal beim neuen Benutzer angemeldet haben, um dieses Problem zu umgehen, bevor Sie das Skript ausführen.

- Konto-PINs sind gemäß DoD STIG deaktiviert

  - PINs sind unsicher, wenn sie ausschließlich anstelle eines Passworts verwendet werden, und können innerhalb weniger Stunden oder möglicherweise sogar Sekunden oder Minuten leicht umgangen werden

  - Entfernen Sie die PIN vom Konto und/oder melden Sie sich mit dem Passwort an, nachdem Sie das Skript ausgeführt haben.

– Bitlocker-Standardeinstellungen wurden aufgrund von DoD STIG geändert und gehärtet.

  – Aufgrund der Art und Weise, wie Bitlocker implementiert ist, wird die Bitlocker-Implementierung unterbrochen, wenn diese Änderungen auftreten und wenn Sie Bitlocker bereits aktiviert haben.

  – Deaktivieren Sie Bitlocker, führen Sie das Skript aus und aktivieren Sie Bitlocker dann erneut, um dieses Problem zu umgehen.

## Anforderungen:

- [x] Windows 10/11 Enterprise (**Bevorzugt**) oder Professional
  – Windows 10/11 Home-Editionen unterstützen keine GPO-Konfigurationen und wurden nicht getestet.
  - Windows „N“-Editionen werden nicht getestet.
-[x] [Standards](https://docs.microsoft.com/en-us/windows-hardware/design/device-experiences/oem-highly-secure) für ein hochsicheres Windows 10-Gerät
-[x] System is [fully up to date and supported](https://support.microsoft.com/en-gb/help/4027667/windows-10-update)
  - Führen Sie das aus[Windows Upgrade Assistant](https://support.microsoft.com/en-us/help/3159635/windows-10-update-assistant) um die neueste Hauptversion zu aktualisieren und zu überprüfen.
- [x] Bitlocker muss vor der Implementierung dieses Skripts angehalten oder ausgeschaltet werden, es kann nach einem Neustart wieder aktiviert werden.
  – Folgeläufe dieses Skripts können ausgeführt werden, ohne Bitlocker zu deaktivieren.
- [x] Hardwareanforderungen
  -[Hardware Requirements for Memory Integrity](https://docs.microsoft.com/en-us/windows/security/threat-protection/device-guard/requirements-and-deployment-planning-guidelines-for-virtualization-based-protection-of-code-integrity#baseline-protections)
  -[Hardware Requirements for Virtualization-Based Security](https://docs.microsoft.com/en-us/windows-hardware/design/device-experiences/oem-vbs)
  -[Hardware Requirements for Windows Defender Application Guard](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-guard/reqs-wd-app-guard)
  -[Hardware Requirements for Windows Defender Credential Guard](https://docs.microsoft.com/en-us/windows/security/identity-protection/credential-guard/credential-guard-requirements)

## Empfohlener Lesestoff:

-[System Guard Secure Launch](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-system-guard/system-guard-secure-launch-and-smm-protection#requirements-met-by-system-guard-enabled-machines)
-[System Guard Root of Trust](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-system-guard/system-guard-how-hardware-based-root-of-trust-helps-protect-windows)
-[Hardware-based Isolation](https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-atp/overview-hardware-based-isolation)
-[Memory integrity](https://docs.microsoft.com/en-us/windows/security/threat-protection/device-guard/memory-integrity)
-[Windows Defender Application Guard](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-guard/wd-app-guard-overview)
-[Windows Defender Credential Guard](https://docs.microsoft.com/en-us/windows/security/identity-protection/credential-guard/credential-guard-how-it-works)

## Ergänzungen, bemerkenswerte Änderungen und Fehlerbehebungen:

**Dieses Skript fügt Einstellungen auf Ihrem System hinzu, entfernt und ändert sie. Bitte überprüfen Sie das Skript, bevor Sie es ausführen.**

### Browser:

- In Browsern werden zusätzliche Erweiterungen installiert, um den Datenschutz und die Sicherheit zu verbessern.
  - Sehen[here](https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/11) für weitere Informationen.
- Aufgrund der für Browser implementierten DoD-STIGs werden Erweiterungsverwaltung und andere Unternehmenseinstellungen festgelegt. Anweisungen zum Anzeigen dieser Optionen finden Sie in den GPO-Anweisungen unten.

### Powershell-Module:

– Zur Unterstützung bei der Automatisierung von Windows-Updates der PowerShell[PSWindowsUpdate](https://www.powershellgallery.com/packages/PSWindowsUpdate/2.0.0.4) Das Modul wird Ihrem System hinzugefügt.

### Microsoft-Konto, Store oder Xbox-Dienste reparieren:

Dies liegt daran, dass wir die Anmeldung bei Microsoft-Konten blockieren. Die Telemetrie- und Identitätszuordnung von Microsoft ist verpönt.
Wenn Sie diese Dienste dennoch nutzen möchten, sehen Sie sich die folgenden Problemtickets zur Lösung an:

- https://github.com/simeononsecurity/Windows-Optimize-Debloat/issues/1
- https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/16
- https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/22

### Nachträgliches Bearbeiten von Richtlinien in der lokalen Gruppenrichtlinie:

Wenn Sie eine Einstellung ändern oder ändern müssen, können diese höchstwahrscheinlich über GPO konfiguriert werden:

- Importieren Sie die ADMX-Richtliniendefinitionen daraus[repo](https://github.com/simeononsecurity/STIG-Compliant-Domain-Prep/tree/master/Files/PolicyDefinitions) in _C:\windows\PolicyDefinitions_ auf dem System, das Sie ändern möchten.

- Öffnen Sie „gpedit.msc“ auf dem System, das Sie ändern möchten.

## Eine Liste der Skripte und Tools, die diese Sammlung verwendet:

### Erste Party:

-[.NET-STIG-Script](https://github.com/simeononsecurity/.NET-STIG-Script)
-[Automate-Sysmon](https://github.com/simeononsecurity/Automate-Sysmon)
-[FireFox-STIG-Script](https://github.com/simeononsecurity/FireFox-STIG-Script)
-[JAVA-STIG-Script](https://github.com/simeononsecurity/JAVA-STIG-Script)
-[Standalone-Windows-STIG-Script](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)
-[Windows-Defender-STIG-Script](https://github.com/simeononsecurity/Windows-Defender-STIG-Script)
-[Windows-Optimize-Debloat](https://github.com/simeononsecurity/Windows-Optimize-Debloat)

### Dritte Seite:

-[Cyber.mil - Group Policy Objects](https://public.cyber.mil/stigs/gpo/)
-[Microsoft Security Compliance Toolkit 1.0](https://www.microsoft.com/en-us/download/details.aspx?id=55319)
-[Microsoft Sysinternals - Sysmon](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon)

## Angewandte STIGS/SRGs:

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

## Zusätzliche Konfigurationen wurden berücksichtigt von:

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

## So führen Sie das Skript aus:
### GUI – Geführte Installation:

Laden Sie die neueste Version herunter[here](https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat-GUI/releases/)Wählen Sie die gewünschten Optionen und klicken Sie auf „Ausführen“. <img src="https://raw.githubusercontent.com/simeononsecurity/Windows-Optimize-Harden-Debloat/master/.github/images/WOHD-GUI.gif" alt="Beispiel einer GUI-basierten geführten Windows-Optimize-Harden-Debloat-Installation"> ### Automatisierte Installation: Verwenden Sie diesen Einzeiler, um alle unterstützenden Dateien automatisch herunterzuladen, zu entpacken und die neueste Version des Skripts auszuführen.```powershell
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
