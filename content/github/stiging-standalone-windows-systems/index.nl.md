---
title: "Windows 10 STIG-naleving automatiseren met Powershell Script"
date: 2020-08-26
---

**Download alle benodigde bestanden van de[GitHub Repository](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)

**Wij zoeken hulp bij het volgende[.Net issue](https://github.com/simeononsecurity/W10-Optimize-and-Harden/issues/3) 

## Introductie:

Windows 10 is onveilig besturingssysteem uit de doos en vereist veel veranderingen om te verzekeren[FISMA](https://www.cisa.gov/federal-information-security-modernization-act) naleving.
Organisaties zoals[Microsoft](https://microsoft.com), [Cyber.mil](https://public.cyber.mil), the [Department of Defense](https://www.defense.gov/), and the [National Security Agency](https://www.nsa.gov/) hebben aanbevolen en vereiste configuratiewijzigingen om het besturingssysteem te vergrendelen, te verharden en te beveiligen en de naleving door de overheid te waarborgen. Deze wijzigingen bestrijken een breed scala aan mitigaties, waaronder het blokkeren van telemetrie, macro's, het verwijderen van bloatware en het voorkomen van vele fysieke aanvallen op een systeem.

Standalone systemen behoren tot de moeilijkste en vervelendste systemen om te beveiligen. Wanneer ze niet geautomatiseerd zijn, moeten ze handmatig worden gewijzigd in elke STIG/SRG. In totaal meer dan 1000 configuratiewijzigingen bij een typische implementatie en een gemiddelde van 5 minuten per wijziging staat gelijk aan 3,5 dag werk. Dit script wil dat proces aanzienlijk versnellen.

## Opmerkingen:

- Dit script is ontworpen voor gebruik in **Enterprise** omgevingen en gaat ervan uit dat u hardware ondersteuning heeft voor alle vereisten.
  - Voor persoonlijke systemen zie dit[GitHub Repository](https://github.com/simeononsecurity/W10-Optimize-and-Harden)
- Dit script is niet ontworpen om een systeem tot 100% conformiteit te brengen, maar dient eerder als een opstapje om de meeste, zo niet alle, configuratiewijzigingen te voltooien die met een script kunnen worden uitgevoerd.
  - Zonder systeemdocumentatie zou deze verzameling u tot ongeveer 95% conformiteit moeten brengen voor alle toegepaste STIGS/SRG's.

## Vereisten:
- [X] Windows 10 Enterprise is **vereist** per STIG.
-[x] [Standards](https://docs.microsoft.com/en-us/windows-hardware/design/device-experiences/oem-highly-secure) voor een zeer veilig Windows 10-apparaat
-[x] System is [fully up to date](https://support.microsoft.com/en-gb/help/4027667/windows-10-update)
  - Momenteel Windows 10 **v1909** of **v2004**.
  - Voer de[Windows 10 Upgrade Assistant](https://support.microsoft.com/en-us/help/3159635/windows-10-update-assistant) bij te werken en de laatste grote release te verifiëren.
- X] Hardwarevereisten
  -[Hardware Requirements for Memory Integrity](https://docs.microsoft.com/en-us/windows/security/threat-protection/device-guard/requirements-and-deployment-planning-guidelines-for-virtualization-based-protection-of-code-integrity#baseline-protections) 
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

-[Microsoft Security Compliance Toolkit 1.0](https://www.microsoft.com/en-us/download/details.aspx?id=55319)

-[Cyber.mil - Group Policy Objects](https://public.cyber.mil/stigs/gpo/)

-[NSACyber - Bitlocker Guidance](https://github.com/nsacyber/BitLocker-Guidance)

## Aanvullende configuraties werden overwogen van:

-[NSACyber - Hardware-and-Firmware-Security-Guidance](https://github.com/nsacyber/Hardware-and-Firmware-Security-Guidance)

-[NSACyber - Application Whitelisting Using Microsoft AppLocker](https://apps.nsa.gov/iad/library/ia-guidance/tech-briefs/application-whitelisting-using-microsoft-applocker.cfm)

## STIGS/SRG's toegepast:
 
-[Windows 10 V1R23](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MS_Windows_10_V1R23_STIG.zip)

-[Windows Defender Antivirus V1R9](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MS_Windows_Defender_Antivirus_V1R9_STIG.zip)

-[Windows Firewall V1R7](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Windows_Firewall_V1R7_STIG.zip)

-[Internet Explorer 11 V1R19](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MS_IE11_V1R19_STIG.zip)

-[Adobe Reader Pro DC Continous V1R2](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Adobe_Acrobat_Pro_DC_Continuous_V1R2_STIG.zip)

-[Microsoft Office 2019/Office 365 Pro Plus V1R2](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MS_Office_365_ProPlus_V1R2_STIG.zip)

-[Microsoft Office 2016 V1R2](https://dl.dod.cyber.mil/wp-content/uploads/stigs/pdf/U_Microsoft_Office_2016_V1R2_Overview.pdf)

-[Microsoft Office 2013 V1R5](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MicrosoftOffice2013_V1R5_Overview.zip)

-[Google Chrome V1R19](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Google_Chrome_V1R19_STIG.zip)

-[Firefox V4R29](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MOZ_FireFox_V4R29_STIG.zip)

-[Microsoft .Net Framework 4 V1R9](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MS_DotNet_Framework_4-0_V1R9_STIG.zip) - **Werk in uitvoering**

-[Oracle JRE 8 V1R5](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Oracle_JRE_8_Windows_V1R5_STIG.zip)

## Hoe voer je het script uit

**Het script kan worden gelanceerd vanaf de uitgepakte GitHub download als volgt:**
```
.\secure-standalone.ps1
```
Het script dat we gaan gebruiken moet worden gestart vanuit de directory met alle andere bestanden uit de[GitHub Repository](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)
