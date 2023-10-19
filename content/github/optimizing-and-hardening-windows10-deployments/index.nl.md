---
title: "Windows 10 implementaties optimaliseren, verstevigen en beveiligen met geautomatiseerde configuratiewijzigingen"
date: 2020-07-22
---
 Windows 10 implementaties verharden en deblokkeren**

**Download alle benodigde bestanden van de [GitHub Repository](https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat)

**We zoeken hulp bij het volgende [.Net issue](https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/3) 

## Introductie:
Windows 10 is een invasief en onveilig besturingssysteem uit de doos.
Organisaties zoals [PrivacyTools.io](https://PrivacyTools.io), [Microsoft](https://microsoft.com), [Cyber.mil](https://public.cyber.mil), the [Department of Defense](https://dod.gov), and the [National Security Agency](https://www.nsa.gov/) hebben configuratiewijzigingen aanbevolen om het besturingssysteem te vergrendelen, te harden en te beveiligen. Deze wijzigingen omvatten een breed scala aan mitigaties, waaronder het blokkeren van telemetrie, macro's, het verwijderen van bloatware en het voorkomen van vele digitale en fysieke aanvallen op een systeem. Dit script automatiseert de configuraties die door deze organisaties worden aanbevolen.

## Opmerkingen:
- Dit script is ontworpen voor gebruik in voornamelijk **Personal Use** omgevingen. Met dat in gedachten worden bepaalde bedrijfsconfiguratie-instellingen niet geïmplementeerd. Dit script is niet ontworpen om een systeem 100% conform te maken. Het moet eerder worden gebruikt als een opstapje om de meeste, zo niet alle, configuratiewijzigingen die kunnen worden gescript te voltooien, terwijl zaken als branding en banners worden overgeslagen, die zelfs in een verharde omgeving voor persoonlijk gebruik niet moeten worden geïmplementeerd.
- Dit script is zo ontworpen dat de optimalisaties, in tegenstelling tot sommige andere scripts, de kernfuncties van Windows niet zullen verbreken.
 - Functies zoals Windows Update, Windows Defender, de Windows Store en Cortona zijn beperkt, maar niet in een disfunctionele staat zoals de meeste andere Windows 10 privacyscripts.
- Als u op zoek bent naar een geminimaliseerd script dat alleen gericht is op commerciële omgevingen, raadpleeg dan dit [GitHub Repository](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)

## Vereisten:
- X] Windows 10 Enterprise (**Aanbevolen**) of Windows 10 Professional
  - Windows 10 Home staat geen GPO-configuraties toe.
  - Windows 10 "N" Editions zijn niet getest.
- [X] [Standards](https://docs.microsoft.com/en-us/windows-hardware/design/device-experiences/oem-highly-secure) voor een zeer veilig Windows 10-apparaat
- [X] System is [fully up to date](https://support.microsoft.com/en-gb/help/4027667/windows-10-update)
  - Momenteel Windows 10 **v1909**, **v2004**, of **20H2**.
  - Voer de [Windows 10 Upgrade Assistant](https://support.microsoft.com/en-us/help/3159635/windows-10-update-assistant) om de laatste grote release bij te werken en te verifiëren.
- X] Bitlocker moet worden opgeschort of uitgeschakeld voordat dit script wordt uitgevoerd, het kan weer worden ingeschakeld na opnieuw opstarten.
  - Vervolg runs van dit script kunnen worden uitgevoerd zonder Bitlocker uit te schakelen.
- X] Hardwarevereisten
  - [Hardware Requirements for Memory Integrity](https://docs.microsoft.com/en-us/windows/security/threat-protection/device-guard/requirements-and-deployment-planning-guidelines-for-virtualization-based-protection-of-code-integrity#baseline-protections) 
  - [Hardware Requirements for Virtualization-Based Security](https://docs.microsoft.com/en-us/windows-hardware/design/device-experiences/oem-vbs)
  - [Hardware Requirements for Windows Defender Application Guard](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-guard/reqs-wd-app-guard)
  - [Hardware Requirements for Windows Defender Credential Guard](https://docs.microsoft.com/en-us/windows/security/identity-protection/credential-guard/credential-guard-requirements)


## Aanbevolen leesmateriaal:
  - [System Guard Secure Launch](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-system-guard/system-guard-secure-launch-and-smm-protection#requirements-met-by-system-guard-enabled-machines)
  - [System Guard Root of Trust](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-system-guard/system-guard-how-hardware-based-root-of-trust-helps-protect-windows)
  - [Hardware-based Isolation](https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-atp/overview-hardware-based-isolation)
  - [Memory integrity](https://docs.microsoft.com/en-us/windows/security/threat-protection/device-guard/memory-integrity)
  - [Windows Defender Application Guard](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-guard/wd-app-guard-overview)
  - [Windows Defender Credential Guard](https://docs.microsoft.com/en-us/windows/security/identity-protection/credential-guard/credential-guard-how-it-works)

## Een lijst van scripts en gereedschappen die deze collectie gebruikt:
- [Cyber.mil - Group Policy Objects](https://public.cyber.mil/stigs/gpo/)
- [Microsoft Security Compliance Toolkit 1.0](https://www.microsoft.com/en-us/download/details.aspx?id=55319)

## Aanvullende configuraties werden overwogen van:
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

## Toegepaste STIGS/SRG's:
- [Adobe Reader Pro DC Classic V1R3](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Adobe_Acrobat_Pro_DC_Continuous_V1R2_STIG.zip)
- [Adobe Reader Pro DC Continous V1R2](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Adobe_Acrobat_Pro_DC_Classic_V1R3_STIG.zip)
- [Firefox V4R29](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MOZ_FireFox_V4R29_STIG.zip)
- [Google Chrome V1R19](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Google_Chrome_V1R19_STIG.zip)
- [Internet Explorer 11 V1R19](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MS_IE11_V1R19_STIG.zip)
- [Microsoft .Net Framework 4 V1R9](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MS_DotNet_Framework_4-0_V1R9_STIG.zip) - **Werk in uitvoering**
- [Microsoft Office 2013 V1R5](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MicrosoftOffice2013_V1R5_Overview.zip)
- [Microsoft Office 2016 V1R2](https://dl.dod.cyber.mil/wp-content/uploads/stigs/pdf/U_Microsoft_Office_2016_V1R2_Overview.pdf)
- [Microsoft Office 2019/Office 365 Pro Plus V1R2](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MS_Office_365_ProPlus_V1R2_STIG.zip)
- [Microsoft OneDrive STIG V2R1](https://dl.cyber.mil/stigs/zip/U_MS_OneDrive_V2R1_STIG.zip)
- [Oracle JRE 8 V1R5](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Oracle_JRE_8_Windows_V1R5_STIG.zip)
- [Windows 10 V2R1](https://dl.cyber.mil/stigs/zip/U_MS_Windows_Defender_Antivirus_V2R1_STIG.zip)
- [Windows Defender Antivirus V2R1](https://dl.cyber.mil/stigs/zip/U_MS_Windows_Defender_Antivirus_V2R1_STIG.zip)
- [Windows Firewall V1R7](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Windows_Firewall_V1R7_STIG.zip)

## Hoe voer ik het script uit?
### Handmatig installeren:
Als het script handmatig is gedownload, moet het worden gestart vanuit een administratieve powershell in de map met alle bestanden van de [GitHub Repository](https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat)
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
Get-ChildItem -Recurse *.ps1 | Unblock-File
.\sos-optimize-windows.ps1
```
### Geautomatiseerde installatie:
Het script kan als volgt worden gestart vanaf de uitgepakte GitHub-download:
```powershell
iex ((New-Object System.Net.WebClient).DownloadString('https://simeononsecurity.com/scripts/windowsoptimizeandharden.ps1'))
```
<img src="https://raw.githubusercontent.com/simeononsecurity/Windows-Optimize-Harden-Debloat/master/.github/images/w10automatic.gif" alt="Voorbeeld van
Windows-Optimize-Harden-Debloat automatische installatie">
