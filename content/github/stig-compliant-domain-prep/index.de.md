---
title: "Erreichen Sie die STIG-Konformität: Stärken Sie die Domänensicherheit und gewährleisten Sie die regulatorischen Anforderungen"
date: 2020-09-08
---
 Einführung

In der heutigen, sich schnell entwickelnden Cybersicherheitslandschaft ist die Gewährleistung der Sicherheit und der Einhaltung von Vorschriften für Ihren Bereich von größter Bedeutung. Die **Einhaltung von STIGs (Security Technical Implementation Guides) und SRGs (Security Requirements Guides) ist entscheidend** für die Aufrechterhaltung einer **robusten und gut geschützten IT-Infrastruktur**. In diesem Artikel erfahren Sie, wie der umfassende Leitfaden von **SimeonOnSecurity Sie bei der Einhaltung der STIGs** für Ihre Domäne unterstützen kann, indem er Ihnen die notwendigen Werkzeuge und Erkenntnisse zur Verbesserung Ihrer **Sicherheitslage** zur Verfügung stellt.

## Begründung

Angesichts der **zunehmenden Zahl von Cyber-Bedrohungen und regulatorischen Anforderungen** müssen Organisationen eine starke **Sicherheitsgrundlage in ihren Bereichen** schaffen. STIGs und SRGs bieten eine Reihe von **Richtlinien und Best Practices** für die Sicherung verschiedener Software und Systeme. Durch die Implementierung dieser Standards können Unternehmen **Risiken mindern, sensible Daten schützen** und sicherstellen, dass ihre Systeme **sicher konfiguriert sind**. **Das Domänenvorbereitungsskript von SimeonOnSecurity stellt eine Sammlung von Gruppenrichtlinienobjekten (GPOs) und Konfigurationen aus vertrauenswürdigen Quellen** zusammen und hilft Organisationen, den Prozess der STIG-Konformität zu rationalisieren.

## Methoden

**Das Domänenvorbereitungsskript von SimeonOnSecurity bietet einen umfassenden Ansatz**, um Ihre Domäne mit den geltenden STIGs und SRGs konform zu machen. Der Leitfaden enthält ein Skript, das in einer Unternehmensumgebung ausgeführt werden kann, um die erforderlichen Konfigurationen anzuwenden. Wenn Sie diese Schritte befolgen, können Sie den Prozess **automatisieren und wertvolle Zeit sparen**.

Das Skript importiert die von **SimeonOnSecurity** bereitgestellten GPOs, die **ausführlich geprüft und getestet** wurden. Diese GPOs decken ein breites Spektrum an Software und Systemen ab, darunter **Adobe Acrobat, Webbrowser wie Firefox und Chrome, Microsoft Office, Windows-Betriebssysteme** und mehr. Das Skript stellt sicher, dass die Konfigurationen mit den **aktuellen STIG- und SRG-Richtlinien** übereinstimmen, damit Sie die erforderlichen Sicherheitsstandards einhalten können.

Darüber hinaus enthält das Skript zusätzliche Konfigurationen, die von angesehenen Organisationen wie **CERT, Microsoft und NSA Cyber** stammen. Diese Konfigurationen befassen sich unter anderem mit spezifischen Sicherheitsaspekten wie **Speicherkorruption, SSL-Härtung, Telemetrieverwaltung, Anwendungs-Whitelisting und Hardware-/Firmware-Sicherheit**.

Durch den Einsatz des Domain-Vorbereitungsskripts von SimeonOnSecurity können Unternehmen **die Sicherheitslage ihrer Domain verbessern, Schwachstellen reduzieren** und die Einhaltung relevanter Vorschriften und Standards nachweisen.
________


**STIG-konforme Domänenvorbereitung**
*Importieren Sie alle von SimeonOnSecurity bereitgestellten GPOs, um Ihre Domäne mit allen anwendbaren STIGs und SRGs konform zu machen.

[![VirusTotal Scan](https://github.com/simeononsecurity/STIG-Compliant-Domain-Prep/actions/workflows/virustotal.yml/badge.svg)](https://github.com/simeononsecurity/STIG-Compliant-Domain-Prep/actions/workflows/virustotal.yml)

**Hinweis:** Dieses Skript sollte auf den meisten, wenn nicht allen Systemen problemlos funktionieren. Während [@SimeonOnSecurity](https://github.com/simeononsecurity) creates, reviews, and tests each repo intensivly, we can not test every possible configuration nor does [@SimeonOnSecurity](https://github.com/simeononsecurity) take any responsibility for breaking your system. If something goes wrong, be prepared to submit an [issue](../../issues) Führen Sie dieses Skript nicht aus, wenn Sie nicht verstehen, was es tut.

## Hinweise:

**Dieses Skript ist für den Einsatz in Unternehmensumgebungen konzipiert**

## Ansible:
Wir bieten jetzt eine Playbook-Sammlung für dieses Skript an. Bitte beachten Sie das Folgende:
- [Github Repo](https://github.com/simeononsecurity/Windows_STIG_Ansible)
- [Ansible Galaxy](https://galaxy.ansible.com/simeononsecurity/windows_stigs)

## Zusätzliche Konfigurationen wurden berücksichtigt von:
- [CERT - IE Scripting Engine Memory Corruption](https://kb.cert.org/vuls/id/573168/)
- [Dirteam - SSL Hardening](https://dirteam.com/sander/2019/07/30/howto-disable-weak-protocols-cipher-suites-and-hashing-algorithms-on-web-application-proxies-ad-fs-servers-and-windows-servers-running-azure-ad-connect/)
- [Microsoft - Managing Windows 10 Telemetry and Callbacks](https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services)
- [Microsoft - Specture and Meltdown Mitigations](https://support.microsoft.com/en-us/help/4072698/windows-server-speculative-execution-side-channel-vulnerabilities)
- [Microsoft - Windows 10 Privacy](https://docs.microsoft.com/en-us/windows/privacy/)
- [Microsoft - Windows 10 VDI Recomendations](https://docs.microsoft.com/en-us/windows-server/remote/remote-desktop-services/rds_vdi-recommendations-1909)
- [Microsoft - Windows Defender Application Control](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/windows-defender-application-control-design-guide)
- [NSACyber - Application Whitelisting Using Microsoft AppLocker](https://apps.nsa.gov/iad/library/ia-guidance/tech-briefs/application-whitelisting-using-microsoft-applocker.cfm)
- [NSACyber - Hardware-and-Firmware-Security-Guidance](https://github.com/nsacyber/Hardware-and-Firmware-Security-Guidance)
- [Whonix - Disable TCP Timestamps](https://www.whonix.org/wiki/Disable_TCP_and_ICMP_Timestamps)

## Angewandte STIGS/SRGs:
- [Adobe Acrobat Pro DC Continuous V2R1](https://public.cyber.mil/stigs/downloads/)
- [Adobe Acrobat Reader DC Continuous V2R1](https://public.cyber.mil/stigs/downloads/)
- [Firefox V5R2](https://public.cyber.mil/stigs/downloads/) - **[Requires Separate Script](https://github.com/simeononsecurity/FireFox-STIG-Script)
- [Google Chrome V2R4](https://public.cyber.mil/stigs/downloads/)
- [Internet Explorer 11 V1R19](https://public.cyber.mil/stigs/downloads/)
- [Microsoft Edge V1R2](https://public.cyber.mil/stigs/downloads/)
- [Microsoft .Net Framework 4 V1R9](https://public.cyber.mil/stigs/downloads/) - **[Requires Separate Script](https://github.com/simeononsecurity/.NET-STIG-Script)
- [Microsoft Office 2013 V2R1](https://public.cyber.mil/stigs/downloads/)
- [Microsoft Office 2016 V2R1](https://public.cyber.mil/stigs/downloads/)
- [Microsoft Office 2019/Office 365 Pro Plus V2R3](https://public.cyber.mil/stigs/downloads/)
- [Microsoft OneDrive STIG V2R1](https://public.cyber.mil/stigs/downloads/)
- [Oracle JRE 8 V1R5](https://public.cyber.mil/stigs/downloads/) - **[Requires Separate Script](https://github.com/simeononsecurity/Oracle-JRE-8-STIG-Script)
- [Windows 10 V2R2](https://public.cyber.mil/stigs/downloads/)
- [Windows Defender Antivirus V2R2](https://public.cyber.mil/stigs/downloads/) - **[Requires Separate Script](https://github.com/simeononsecurity/Windows-Defender-STIG-Script)
- [Windows Firewall V1R7](https://public.cyber.mil/stigs/downloads/)
- [Windows Server 2012(R2) V3R2](https://public.cyber.mil/stigs/downloads/)
- [Windows Server 2016 V2R2](https://public.cyber.mil/stigs/downloads/)
- [Windows Server 2019 V2R2](https://public.cyber.mil/stigs/downloads/)
- [VMWare Horizon Agent V1R1](https://public.cyber.mil/stigs/downloads/)
- [VMWare Horizon Client V1R1](https://public.cyber.mil/stigs/downloads/)


## Verwendung:
### PowerShell-Skript:

**Das Skript kann von dem extrahierten GitHub-Download wie folgt gestartet werden:**
```
.\sos-stig-compliant-domain-prep.ps1
```
Das Skript, das wir verwenden werden, muss aus dem Verzeichnis gestartet werden, das alle anderen Dateien aus dem [GitHub Repository](https://github.com/simeononsecurity/STIG-Compliant-Domain-Prep)


