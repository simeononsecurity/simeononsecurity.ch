---
title: "Optimaliseer en verhard uw Windows systeem met het Windows-Optimize-Harden-Debloat Script"
date: 2020-12-29
toc: true
draft: false
description: "Deze uitgebreide gids bevat stapsgewijze instructies voor het optimaliseren, harden en debloeden van uw Windows-systeem voor betere prestaties, beveiliging en privacy."
tags: ["Windows optimalisatie", "Ramen verharden", "Windows debloating", "Windows beveiliging", "Windows prestaties", "Windows privacy", "Windows updates", "Objecten voor groepsbeleid", "Adobe Acrobat Reader", "Firefox", "Google Chrome", "Internet Explorer", "Microsoft Chromium Edge", "Dot Net 4", "Microsoft Office", "Onedrive", "Oracle Java JRE 8", "Windows Firewall", "Windows Defender", "Applocker"]
---
 Inleiding:

Windows 10 en Windows 11 zijn invasieve en onveilige besturingssystemen uit de doos.
Organisaties zoals[PrivacyTools.io](https://PrivacyTools.io), [Microsoft](https://microsoft.com), [Cyber.mil](https://public.cyber.mil), the [Department of Defense](https://dod.gov), and the [National Security Agency](https://www.nsa.gov/) hebben configuratiewijzigingen aanbevolen om het besturingssysteem te vergrendelen, te verharden en te beveiligen. Deze veranderingen bestrijken een breed scala aan mitigaties, waaronder het blokkeren van telemetrie, macro's, het verwijderen van bloatware, en het voorkomen van vele digitale en fysieke aanvallen op een systeem. Dit script is bedoeld om de door die organisaties aanbevolen configuraties te automatiseren.

## Opmerkingen, waarschuwingen en overwegingen:

**WAARSCHUWING:**

Dit script zou voor de meeste, zo niet alle, systemen zonder problemen moeten werken. Hoewel[@SimeonOnSecurity](https://github.com/simeononsecurity) creates, reviews, and tests each repo intensively, we can not test every possible configuration nor does [@SimeonOnSecurity](https://github.com/simeononsecurity) take any responsibility for breaking your system. If something goes wrong, be prepared to submit an [issue](../../issues)

- Dit script is ontworpen voor gebruik in hoofdzakelijk **persoonlijke omgevingen**. Met dat in gedachten zijn bepaalde bedrijfsconfiguratie-instellingen niet geïmplementeerd. Dit script is niet ontworpen om een systeem 100% conform te maken. Het moet eerder worden gebruikt als een opstapje om de meeste, zo niet alle, configuratiewijzigingen te voltooien die met een script kunnen worden uitgevoerd, terwijl kwesties als branding en banners, die zelfs in een verharde omgeving voor persoonlijk gebruik niet moeten worden geïmplementeerd, worden overgeslagen.
- Dit script is zo ontworpen dat de optimalisaties, in tegenstelling tot sommige andere scripts, de kernfuncties van Windows niet verbreken.
- Functies zoals Windows Update, Windows Defender, de Windows Store en Cortona zijn beperkt, maar zijn niet in een disfunctionele staat zoals de meeste andere Windows 10 Privacy scripts.
- Als u een geminimaliseerd script zoekt dat alleen gericht is op commerciële omgevingen, bekijk dan dit[GitHub Repository](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)


**Voer dit script niet uit als u niet begrijpt wat het doet. Het is uw verantwoordelijkheid het script te controleren en te testen voordat u het uitvoert.**

**HET VOLGENDE ZAL BIJVOORBEELD BREKEN ALS U DIT UITVOERT ZONDER PREVENTIEVE MAATREGELEN TE NEMEN:**

- Het gebruik van de standaard administrator account genaamd "Administrator" is uitgeschakeld en hernoemd per DoD STIG

  - Is niet van toepassing op de standaardaccount die is aangemaakt, maar wel op het gebruik van de standaardbeheerdersaccount die vaak wordt aangetroffen op Enterprise, IOT en Windows Server-versies.

  - Maak een nieuwe account aan onder Computerbeheer en stel deze desgewenst in als beheerder. Kopieer vervolgens de inhoud van de vorige gebruikersmap naar de nieuwe nadat u zich voor het eerst bij de nieuwe gebruiker hebt aangemeld om dit te omzeilen voordat u het script uitvoert.

- Aanmelden met een Microsoft-account is uitgeschakeld volgens de DoD STIG.

  - Wanneer u probeert veilig en privé te zijn, wordt het aanmelden bij uw lokale account via een Microsoft-account afgeraden. Dit wordt afgedwongen door deze repo.

  - Maak een nieuw account aan onder Computerbeheer en stel het desgewenst in als beheerder. Kopieer vervolgens de inhoud van de vorige gebruikersmap naar de nieuwe nadat u zich voor de eerste keer hebt aangemeld bij de nieuwe gebruiker om dit te omzeilen voordat u het script uitvoert.

- Account-PIN's zijn uitgeschakeld per DoD STIG

  - Pincodes zijn onveilig als ze alleen worden gebruikt in plaats van een wachtwoord en kunnen gemakkelijk worden omzeild in enkele uren of mogelijk zelfs seconden of minuten.

  - Verwijder de pincode van de account en/of meld u aan met een wachtwoord na het uitvoeren van het script.

- De standaardinstellingen van Bitlocker zijn gewijzigd en verhard als gevolg van DoD STIG.

  - Door de manier waarop bitlocker is geïmplementeerd, zullen deze wijzigingen en als u bitlocker al hebt ingeschakeld, de bitlocker-implementatie verbreken.

  - Schakel bitlocker uit, voer het script uit en schakel bitlocker opnieuw in om dit probleem te omzeilen.

## Vereisten:

- Windows 10/11 Enterprise (**voorkeur**) of Professional.
  - Windows 10/11 Home-edities ondersteunen geen GPO-configuraties en zijn niet getest.
  - Windows "N" edities zijn niet getest.
-[x] [Standards](https://docs.microsoft.com/en-us/windows-hardware/design/device-experiences/oem-highly-secure) voor een zeer veilig Windows 10-apparaat
-[x] System is [fully up to date and supported](https://support.microsoft.com/en-gb/help/4027667/windows-10-update)
  - Voer de[Windows Upgrade Assistant](https://support.microsoft.com/en-us/help/3159635/windows-10-update-assistant) om de laatste grote release bij te werken en te verifiëren.
- x] Bitlocker moet worden opgeschort of uitgeschakeld voordat dit script wordt uitgevoerd, het kan weer worden ingeschakeld na opnieuw opstarten.
  - Vervolg runs van dit script kunnen worden uitgevoerd zonder Bitlocker uit te schakelen.
- x] Hardwarevereisten
  -[Hardware Requirements for Memory Integrity](https://docs.microsoft.com/en-us/windows/security/threat-protection/device-guard/requirements-and-deployment-planning-guidelines-for-virtualization-based-protection-of-code-integrity#baseline-protections)
  -[Hardware Requirements for Virtualization-Based Security](https://docs.microsoft.com/en-us/windows-hardware/design/device-experiences/oem-vbs)
  -[Hardware Requirements for Windows Defender Application Guard](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-guard/reqs-wd-app-guard)
  -[Hardware Requirements for Windows Defender Credential Guard](https://docs.microsoft.com/en-us/windows/security/identity-protection/credential-guard/credential-guard-requirements)

## Aanbevolen leesmateriaal:

-[System Guard Secure Launch](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-system-guard/system-guard-secure-launch-and-smm-protection#requirements-met-by-system-guard-enabled-machines)
-[System Guard Root of Trust](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-system-guard/system-guard-how-hardware-based-root-of-trust-helps-protect-windows)
-[Hardware-based Isolation](https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-atp/overview-hardware-based-isolation)
-[Memory integrity](https://docs.microsoft.com/en-us/windows/security/threat-protection/device-guard/memory-integrity)
-[Windows Defender Application Guard](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-guard/wd-app-guard-overview)
-[Windows Defender Credential Guard](https://docs.microsoft.com/en-us/windows/security/identity-protection/credential-guard/credential-guard-how-it-works)

## Toevoegingen, opvallende veranderingen en bugfixes:

**Dit script voegt instellingen toe, verwijdert ze en verandert ze op uw systeem. Bekijk het script voordat u het uitvoert.**

### Browsers:

- Voor browsers worden extra uitbreidingen geïnstalleerd om de privacy en veiligheid te bevorderen.
  - Zie[here](https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/11) voor aanvullende informatie.
- Als gevolg van de DoD STIG's die zijn geïmplementeerd voor browsers, worden extensiebeheer en andere bedrijfsinstellingen ingesteld. Voor instructies over hoe u deze opties kunt zien, moet u de onderstaande GPO-instructies raadplegen.

### Powershell-modules:

- Om te helpen bij het automatiseren van Windows Updates is de PowerShell[PSWindowsUpdate](https://www.powershellgallery.com/packages/PSWindowsUpdate/2.0.0.4) module wordt toegevoegd aan uw systeem.

### Microsoft Account, Store of Xbox Services repareren:

Dit komt omdat we het aanmelden bij Microsoft-accounts blokkeren. De telemetrie en identiteitsassociatie van Microsoft wordt afgekeurd.
Als u deze diensten toch wilt gebruiken, zie dan de volgende issue tickets voor de oplossing:

- https://github.com/simeononsecurity/Windows-Optimize-Debloat/issues/1
- https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/16
- https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/22

### Beleid in lokaal groepsbeleid achteraf bewerken:

Als u een instelling moet aanpassen of wijzigen, zijn deze hoogstwaarschijnlijk configureerbaar via GPO:

- Importeer de ADMX-beleidsdefinities van deze[repo](https://github.com/simeononsecurity/STIG-Compliant-Domain-Prep/tree/master/Files/PolicyDefinitions) in _C:\windows_PolicyDefinitions_ op het systeem dat je probeert te wijzigen.

- Openen`gpedit.msc` op het systeem dat je probeert aan te passen.

## Een lijst van scripts en gereedschappen die deze collectie gebruikt:

### Eerste partij:

-[.NET-STIG-Script](https://github.com/simeononsecurity/.NET-STIG-Script)
-[Automate-Sysmon](https://github.com/simeononsecurity/Automate-Sysmon)
-[FireFox-STIG-Script](https://github.com/simeononsecurity/FireFox-STIG-Script)
-[JAVA-STIG-Script](https://github.com/simeononsecurity/JAVA-STIG-Script)
-[Standalone-Windows-STIG-Script](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)
-[Windows-Defender-STIG-Script](https://github.com/simeononsecurity/Windows-Defender-STIG-Script)
-[Windows-Optimize-Debloat](https://github.com/simeononsecurity/Windows-Optimize-Debloat)

### Derde partij:

-[Cyber.mil - Group Policy Objects](https://public.cyber.mil/stigs/gpo/)
-[Microsoft Security Compliance Toolkit 1.0](https://www.microsoft.com/en-us/download/details.aspx?id=55319)
-[Microsoft Sysinternals - Sysmon](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon)

## STIGS/SRG's toegepast:

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

## Aanvullende configuraties werden overwogen van:

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

## Hoe voer je het script uit:
### GUI - Geleide installatie:

Download de laatste versie[here](https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat-GUI/releases/) kies de gewenste opties en druk op uitvoeren.

<img src="https://raw.githubusercontent.com/simeononsecurity/Windows-Optimize-Harden-Debloat/master/.github/images/WOHD-GUI.gif" alt="Voorbeeld van
Windows-Optimize-Harden-Debloat GUI gebaseerde geleide installatie">

### Geautomatiseerde installatie:

Gebruik deze one-liner om automatisch alle ondersteunende bestanden te downloaden, uit te pakken en de laatste versie van het script uit te voeren.

```powershell
iwr -useb 'https://simeononsecurity.com/scripts/windowsoptimizeandharden.ps1'|iex
```

<img src="https://raw.githubusercontent.com/simeononsecurity/Windows-Optimize-Harden-Debloat/master/.github/images/w10automatic.gif" alt="Voorbeeld van
Windows-Optimize-Harden-Debloat automatische installatie">

### Handmatige installatie:

Indien handmatig gedownload, moet het script worden gestart vanuit een administratieve powershell in de directory die alle bestanden van de[GitHub Repository](https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat)

Het script "sos-optimize-windows.ps1" bevat verschillende parameters waarmee het optimalisatieproces kan worden aangepast. Elke parameter is een booleaanse waarde die standaard op waar staat als hij niet is opgegeven.

- **cleargpos**: Wist de instellingen voor Group Policy Objects.
- **installupdates**: Installeert updates op het systeem.
- **adobe**: Implementeert de Adobe Acrobat Reader STIGs.
- **firefox**: Implementeert de FireFox STIG.
- **chrome**: Implementeert de STIG van Google Chrome.
- **IE11**: Implementeert de STIG voor Internet Explorer 11.
- **edge**: Implementeert de Microsoft Chromium Edge STIG.
- **dotnet**: Implementeert de Dot Net 4 STIG.
- **office**: Implementeert de Microsoft Office-gerelateerde STIG's.
- **onedrive**: Implementeert de Onedrive STIG's.
- **java**: Implementeert de Oracle Java JRE 8 STIG.
- **windows**: Implementeert de Windows Desktop STIG's.
- **defender**: Implementeert de Windows Defender STIG.
- **firewall**: Implementeert de Windows Firewall STIG.
- Beperkingen**: Implementeert algemene best practice mitigaties.
- **defenderhardening**: Implementeert en verstevigt Windows Defender voorbij de STIG-vereisten.
- **pshardening**: Implementeert PowerShell-verharding en logboekregistratie.
- **sslhardening**: Implementeert SSL-verharding.
- **smbhardening**: Verhardt SMB client en server instellingen.
- **applockerhardening**: Installeert en configureert Applocker (alleen in auditmodus).
- **bitlockerhardening**: Verhardt Bitlocker Implementatie.
- **removebloatware**: Verwijdert onnodige programma's en functies van het systeem.
- **disabletelemetry**: Gegevensverzameling en telemetrie uitschakelen.
- **privacy**: Brengt wijzigingen aan om de privacy te verbeteren.
- **imagecleanup**: Ruimt onnodige bestanden op van het systeem.
- **nessusPID**: Lost ongequoteerde systeemstrings in het pad op.
- **sysmon**: Installeert en configureert sysmon om de controlemogelijkheden te verbeteren.
- **schijfcompressie**: Comprimeert de systeemschijf.
- **emet**: Implementeert STIG vereisten en hardening voor EMET op Windows 7 systemen.
- **updatemanagement**: Verandert de manier waarop updates worden beheerd en verbeterd op het systeem.
- **deviceguard**: Maakt Device Guard Hardening mogelijk.
- **sosbrowsers**: Optimaliseert de webbrowsers van het systeem.

Een voorbeeld van hoe het script met specifieke parameters kan worden gestart is:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
Get-ChildItem -Recurse *.ps1 | Unblock-File
powershell.exe -ExecutionPolicy ByPass -File .\sos-optimize-windows.ps1 -cleargpos:$false -installupdates:$false
```
