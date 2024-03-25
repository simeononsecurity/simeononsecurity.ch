---
title: "Windows Server STIG-naleving automatiseren met STIG-scripts"
date: 2020-09-09
---

**Download alle benodigde bestanden van de[GitHub Repository](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)

**Noot:** Dit script zou voor de meeste, zo niet alle, systemen zonder problemen moeten werken. Terwijl[@SimeonOnSecurity](https://github.com/simeononsecurity) creates, reviews, and tests each repo intensively, we can not test every possible configuration nor does [@SimeonOnSecurity](https://github.com/simeononsecurity) take any responsibility for breaking your system. If something goes wrong, be prepared to submit an [issue](../../issues) Voer dit script niet uit als u niet begrijpt wat het doet. Het is uw verantwoordelijkheid om het script te controleren en te testen voordat u het uitvoert.

## Ansible:
We bieden nu een playbookverzameling voor dit script. Zie het volgende:
-[Github Repo](https://github.com/simeononsecurity/Windows_STIG_Ansible)
-[Ansible Galaxy](https://galaxy.ansible.com/simeononsecurity/windows_stigs)

## Introductie:

Windows 10 is onveilig besturingssysteem uit de doos en vereist veel veranderingen om te verzekeren[FISMA](https://www.cisa.gov/federal-information-security-modernization-act) naleving.
Organisaties zoals[Microsoft](https://microsoft.com), [Cyber.mil](https://public.cyber.mil), the [Department of Defense](https://www.defense.gov/), and the [National Security Agency](https://www.nsa.gov/) hebben aanbevolen en vereiste configuratiewijzigingen om het besturingssysteem te vergrendelen, te verharden en te beveiligen en de naleving door de overheid te waarborgen. Deze wijzigingen bestrijken een breed scala aan mitigaties, waaronder het blokkeren van telemetrie, macro's, het verwijderen van bloatware en het voorkomen van vele fysieke aanvallen op een systeem.

Standalone systemen behoren tot de moeilijkste en vervelendste systemen om te beveiligen. Wanneer ze niet geautomatiseerd zijn, moeten ze handmatig worden gewijzigd in elke STIG/SRG. In totaal meer dan 1000 configuratiewijzigingen bij een typische implementatie en een gemiddelde van 5 minuten per wijziging staat gelijk aan 3,5 dag werk. Dit script wil dat proces aanzienlijk versnellen.

## Opmerkingen:

- Dit script is ontworpen voor gebruik in **Enterprise** omgevingen en gaat ervan uit dat u hardware ondersteuning heeft voor alle vereisten.
  - Voor persoonlijke systemen zie dit[GitHub Repository](https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat)
- Dit script is niet ontworpen om een systeem tot 100% conformiteit te brengen, maar dient eerder als een opstapje om de meeste, zo niet alle, configuratiewijzigingen te voltooien die met een script kunnen worden uitgevoerd.
  - Zonder systeemdocumentatie zou deze verzameling u tot ongeveer 95% conformiteit moeten brengen voor alle toegepaste STIGS/SRG's.

## Vereisten:
- [X] Windows 10 Enterprise is vereist per STIG.
-[X] [Standards](https://docs.microsoft.com/en-us/windows-hardware/design/device-experiences/oem-highly-secure) voor een zeer veilig Windows 10-apparaat
-[X] System is [fully up to date](https://support.microsoft.com/en-gb/help/4027667/windows-10-update)
  - Voer de[Windows 10 Upgrade Assistant](https://support.microsoft.com/en-us/help/3159635/windows-10-update-assistant) om de laatste grote release bij te werken en te verifiëren.
- X] Bitlocker moet worden opgeschort of uitgeschakeld voordat dit script wordt uitgevoerd, het kan weer worden ingeschakeld na opnieuw opstarten.
  - Vervolg runs van dit script kunnen worden uitgevoerd zonder Bitlocker uit te schakelen.
- X] Hardwarevereisten
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

## Een lijst van scripts en gereedschappen die deze collectie gebruikt:
-[Cyber.mil - Group Policy Objects](https://public.cyber.mil/stigs/gpo/)
-[Microsoft Security Compliance Toolkit 1.0](https://www.microsoft.com/en-us/download/details.aspx?id=55319)

## Aanvullende configuraties werden overwogen van:
-[Microsoft - Recommended block rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules)
-[Microsoft - Recommended driver block rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules)
-[Microsoft - Windows Defender Application Control](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/windows-defender-application-control-design-guide)
-[NSACyber - Application Whitelisting Using Microsoft AppLocker](https://apps.nsa.gov/iad/library/ia-guidance/tech-briefs/application-whitelisting-using-microsoft-applocker.cfm)
-[NSACyber - Hardware-and-Firmware-Security-Guidance](https://github.com/nsacyber/Hardware-and-Firmware-Security-Guidance)
-[NSACyber - Windows Secure Host Baseline](https://github.com/nsacyber/Windows-Secure-Host-Baseline)

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
-[Windows Firewall V1R7](https://public.cyber.mil/stigs/downloads/)

## Beleid bewerken in Lokaal Groepsbeleid achteraf:
- Importeer de ADMX-beleidsdefinities van deze[repo](https://github.com/simeononsecurity/STIG-Compliant-Domain-Prep/tree/master/Files/PolicyDefinitions) in *C:\windowsPolicyDefinitions* op het systeem dat u probeert te wijzigen.
- Openen```gpedit.msc``` op het systeem dat je probeert aan te passen.


## Hoe voer je het script uit:
### Geautomatiseerde installatie:
Het script kan vanaf de uitgepakte GitHub-download als volgt worden gestart:
```powershell
iex ((New-Object System.Net.WebClient).DownloadString('https://simeononsecurity.com/scripts/standalonewindows.ps1'))
```

### Handmatige installatie:
Indien handmatig gedownload, moet het script gestart worden vanuit de map die alle andere bestanden van de[GitHub Repository](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)

Alle parameters in het script "secure-standalone.ps1" zijn optioneel, met als standaardwaarde $true. Dit betekent dat als voor een parameter geen waarde wordt opgegeven wanneer het script wordt uitgevoerd, deze wordt behandeld alsof deze is ingesteld op $true.

Het script gebruikt de volgende parameters, die allemaal optioneel zijn en standaard op $true staan als ze niet zijn opgegeven:

- **cleargpos**: (Boolean) Wis GPO's die niet worden gebruikt.
- **installupdates**: (Boolean) Installeer updates en herstart indien nodig.
- **adobe**: (Boolean) STIG Adobe Reader
- **firefox**: (Boolean) STIG Firefox
- **chrome**: (Booleaans) STIG Chrome
- **IE11**: (Booleaans) STIG Internet Explorer 11
- **edge**: (Booleaans) STIG Edge
- **dotnet**: (Booleaans) STIG .NET Framework
- **office**: (Boolean) STIG Office
- **onedrive**: (Booleaans) STIG OneDrive
- **java**: (Boolean) STIG Java
- **windows**: (Boolean) STIG Windows
- **defender**: (Boolean) STIG Windows Defender
- **firewall**: (Boolean) STIG Windows Firewall
- **mitigations**: (Boolean) STIG Mitigations
- **nessusPID**: (Boolean) Resolve Unquoted Strings in Path
- **horizon**: (Boolean) STIG VMware Horizon.
- **sosoptional**: (Boolean) Optionele STIG/Hardende items

Een voorbeeld van het uitvoeren van het script met alle standaardparameters zou zijn:

```powershell
.\secure-standalone.ps1
```
Als u voor een of meer van de parameters een andere waarde wilt opgeven, kunt u deze samen met de gewenste waarde in het commando opnemen. Als u bijvoorbeeld het script wilt uitvoeren en de parameter $firefox wilt instellen op $false, zou het commando zijn:

```powershell
.\secure-standalone.ps1 -firefox $false
```

U kunt ook meerdere parameters in het commando opgeven, zoals dit:

```powershell
.\secure-standalone.ps1 -firefox $false -chrome $false
```

Merk op dat in dit voorbeeld zowel de Firefox- als de Chrome-parameters zijn ingesteld op $false.



