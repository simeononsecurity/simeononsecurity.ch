---
title: "Automatització del compliment de Windows 10 STIG amb Powershell Script"
date: 2020-08-26
---

** Baixeu tots els fitxers necessaris des del[GitHub Repository](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)

** Estem buscant ajuda amb el següent[.Net issue](https://github.com/simeononsecurity/W10-Optimize-and-Harden/issues/3) 

## Introducció:

Windows 10 és un sistema operatiu insegur des de la caixa i requereix molts canvis per assegurar-lo[FISMA](https://www.cisa.gov/federal-information-security-modernization-act) compliment.
Organitzacions com[Microsoft](https://microsoft.com), [Cyber.mil](https://public.cyber.mil), the [Department of Defense](https://dod.gov), and the [National Security Agency](https://www.nsa.gov/) han recomanat i requerit canvis de configuració per bloquejar, endurir i assegurar el sistema operatiu i garantir el compliment del govern. Aquests canvis cobreixen una àmplia gamma de mitigacions, com ara el bloqueig de la telemetria, les macros, l'eliminació de bloatware i la prevenció de molts atacs físics a un sistema.

Els sistemes autònoms són alguns dels sistemes més difícils i molestos de protegir. Quan no estan automatitzats, requereixen canvis manuals de cada STIG/SRG. En total, més de 1.000 canvis de configuració en una implementació típica i una mitjana de 5 minuts per canvi equivalent a 3,5 dies de treball. Aquest script pretén accelerar aquest procés de manera significativa.

## Notes:

- Aquest script està dissenyat per funcionar en entorns **Empresa** i suposa que teniu suport de maquinari per a tots els requisits.
  - Per a sistemes personals, consulteu això[GitHub Repository](https://github.com/simeononsecurity/W10-Optimize-and-Harden)
- Aquest script no està dissenyat per fer que un sistema compleixi al 100%, sinó que s'hauria d'utilitzar com a trampolí per completar la majoria, si no tots, els canvis de configuració que es poden programar.
  - Menys la documentació del sistema, aquesta recollida us hauria d'aportar fins a un 95% de compliment de tots els STIGS/SRG aplicats.

## Requisits:
- [X] Windows 10 Enterprise és **obligatori** per STIG.
-[x] [Standards](https://docs.microsoft.com/en-us/windows-hardware/design/device-experiences/oem-highly-secure) per a un dispositiu Windows 10 altament segur
-[x] System is [fully up to date](https://support.microsoft.com/en-gb/help/4027667/windows-10-update)
  - Actualment Windows 10 **v1909** o **v2004**.
  - Executar el[Windows 10 Upgrade Assistant](https://support.microsoft.com/en-us/help/3159635/windows-10-update-assistant) per actualitzar-se i verificar la darrera versió principal.
- [X] Requisits de maquinari
  -[Hardware Requirements for Memory Integrity](https://docs.microsoft.com/en-us/windows/security/threat-protection/device-guard/requirements-and-deployment-planning-guidelines-for-virtualization-based-protection-of-code-integrity#baseline-protections) 
  -[Hardware Requirements for Windows Defender Application Guard](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-guard/reqs-wd-app-guard)
  -[Hardware Requirements for Windows Defender Credential Guard](https://docs.microsoft.com/en-us/windows/security/identity-protection/credential-guard/credential-guard-requirements)
  
## Material de lectura recomanat:
  -[System Guard Secure Launch](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-system-guard/system-guard-secure-launch-and-smm-protection#requirements-met-by-system-guard-enabled-machines)
  -[System Guard Root of Trust](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-system-guard/system-guard-how-hardware-based-root-of-trust-helps-protect-windows)
  -[Hardware-based Isolation](https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-atp/overview-hardware-based-isolation)
  -[Memory integrity](https://docs.microsoft.com/en-us/windows/security/threat-protection/device-guard/memory-integrity)
  -[Windows Defender Application Guard](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-guard/wd-app-guard-overview)
  -[Windows Defender Credential Guard](https://docs.microsoft.com/en-us/windows/security/identity-protection/credential-guard/credential-guard-how-it-works)

## Una llista de scripts i eines que utilitza aquesta col·lecció:

-[Microsoft Security Compliance Toolkit 1.0](https://www.microsoft.com/en-us/download/details.aspx?id=55319)

-[Cyber.mil - Group Policy Objects](https://public.cyber.mil/stigs/gpo/)

-[NSACyber - Bitlocker Guidance](https://github.com/nsacyber/BitLocker-Guidance)

## S'han considerat configuracions addicionals de:

-[NSACyber - Hardware-and-Firmware-Security-Guidance](https://github.com/nsacyber/Hardware-and-Firmware-Security-Guidance)

-[NSACyber - Application Whitelisting Using Microsoft AppLocker](https://apps.nsa.gov/iad/library/ia-guidance/tech-briefs/application-whitelisting-using-microsoft-applocker.cfm)

## STIGS/SRG aplicats:
 
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

-[Microsoft .Net Framework 4 V1R9](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MS_DotNet_Framework_4-0_V1R9_STIG.zip) - **Obres en curs**

-[Oracle JRE 8 V1R5](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Oracle_JRE_8_Windows_V1R5_STIG.zip)

## Com executar l'script

**L'script es pot llançar des de la descàrrega de GitHub extreta així:**
```
.\secure-standalone.ps1
```
L'script que farem servir s'ha de llançar des del directori que conté tots els altres fitxers de l'[GitHub Repository](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)
