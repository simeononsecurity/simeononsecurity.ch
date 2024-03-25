---
title: "Automatització del compliment STIG de Windows Server amb scripts STIG"
date: 2020-09-09
---

** Baixeu tots els fitxers necessaris des del[GitHub Repository](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)

**Nota:** Aquest script hauria de funcionar per a la majoria, si no tots, els sistemes sense problemes. Mentre[@SimeonOnSecurity](https://github.com/simeononsecurity) creates, reviews, and tests each repo intensively, we can not test every possible configuration nor does [@SimeonOnSecurity](https://github.com/simeononsecurity) take any responsibility for breaking your system. If something goes wrong, be prepared to submit an [issue](../../issues) No executeu aquest script si no enteneu què fa. És la vostra responsabilitat revisar i provar l'script abans d'executar-lo.

## Ansible:
Ara oferim una col·lecció de llibres de jocs per a aquest guió. Si us plau, consulteu el següent:
-[Github Repo](https://github.com/simeononsecurity/Windows_STIG_Ansible)
-[Ansible Galaxy](https://galaxy.ansible.com/simeononsecurity/windows_stigs)

## Introducció:

Windows 10 és un sistema operatiu insegur des de la caixa i requereix molts canvis per assegurar-lo[FISMA](https://www.cisa.gov/federal-information-security-modernization-act) compliment.
Organitzacions com[Microsoft](https://microsoft.com), [Cyber.mil](https://public.cyber.mil), the [Department of Defense](https://www.defense.gov/), and the [National Security Agency](https://www.nsa.gov/) han recomanat i requerit canvis de configuració per bloquejar, endurir i assegurar el sistema operatiu i garantir el compliment del govern. Aquests canvis cobreixen una àmplia gamma de mitigacions, com ara el bloqueig de la telemetria, les macros, l'eliminació de bloatware i la prevenció de molts atacs físics a un sistema.

Els sistemes autònoms són alguns dels sistemes més difícils i molestos de protegir. Quan no estan automatitzats, requereixen canvis manuals de cada STIG/SRG. En total, més de 1.000 canvis de configuració en una implementació típica i una mitjana de 5 minuts per canvi equivalent a 3,5 dies de treball. Aquest script pretén accelerar aquest procés de manera significativa.

## Notes:

- Aquest script està dissenyat per funcionar en entorns **Empresa** i suposa que teniu suport de maquinari per a tots els requisits.
  - Per a sistemes personals, consulteu això[GitHub Repository](https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat)
- Aquest script no està dissenyat per fer que un sistema compleixi al 100%, sinó que s'hauria d'utilitzar com a trampolí per completar la majoria, si no tots, els canvis de configuració que es poden programar.
  - Menys la documentació del sistema, aquesta recollida us hauria d'aportar fins a un 95% de compliment de tots els STIGS/SRG aplicats.

## Requisits:
- [X] Es requereix Windows 10 Enterprise per STIG.
-[X] [Standards](https://docs.microsoft.com/en-us/windows-hardware/design/device-experiences/oem-highly-secure) per a un dispositiu Windows 10 altament segur
-[X] System is [fully up to date](https://support.microsoft.com/en-gb/help/4027667/windows-10-update)
  - Executar el[Windows 10 Upgrade Assistant](https://support.microsoft.com/en-us/help/3159635/windows-10-update-assistant) per actualitzar i verificar la darrera versió principal.
- [X] Bitlocker s'ha de suspendre o desactivar abans d'implementar aquest script, es pot tornar a activar després de reiniciar.
  - Les execucions de seguiment d'aquest script es poden executar sense desactivar Bitlocker.
- [X] Requisits de maquinari
  -[Hardware Requirements for Memory Integrity](https://docs.microsoft.com/en-us/windows/security/threat-protection/device-guard/requirements-and-deployment-planning-guidelines-for-virtualization-based-protection-of-code-integrity#baseline-protections) 
  -[Hardware Requirements for Virtualization-Based Security](https://docs.microsoft.com/en-us/windows-hardware/design/device-experiences/oem-vbs)
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
-[Cyber.mil - Group Policy Objects](https://public.cyber.mil/stigs/gpo/)
-[Microsoft Security Compliance Toolkit 1.0](https://www.microsoft.com/en-us/download/details.aspx?id=55319)

## S'han considerat configuracions addicionals de:
-[Microsoft - Recommended block rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules)
-[Microsoft - Recommended driver block rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules)
-[Microsoft - Windows Defender Application Control](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/windows-defender-application-control-design-guide)
-[NSACyber - Application Whitelisting Using Microsoft AppLocker](https://apps.nsa.gov/iad/library/ia-guidance/tech-briefs/application-whitelisting-using-microsoft-applocker.cfm)
-[NSACyber - Hardware-and-Firmware-Security-Guidance](https://github.com/nsacyber/Hardware-and-Firmware-Security-Guidance)
-[NSACyber - Windows Secure Host Baseline](https://github.com/nsacyber/Windows-Secure-Host-Baseline)

## STIGS/SRG aplicats:
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

## Edició de polítiques a la política de grup local després del fet:
- Importeu les definicions de la política ADMX d'aquesta[repo](https://github.com/simeononsecurity/STIG-Compliant-Domain-Prep/tree/master/Files/PolicyDefinitions) a *C:\windows\PolicyDefinitions* al sistema que esteu intentant modificar.
- Obert```gpedit.msc``` on on the system you're trying to modify. 


## How to run the script:
### Automated Install:
The script may be launched from the extracted GitHub download like this:
```powershell
iex ((New-Object System.Net.WebClient).DownloadString('https://simeononsecurity.com/scripts/standalonewindows.ps1'))
```

### Manual Install:
If manually downloaded, the script must be launched from the directory containing all the other files from the [GitHub Repository](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)

All of the parameters in the "secure-standalone.ps1" script are optional, with a default value of $true. This means that if no value is specified for a parameter when the script is run, it will be treated as if it were set to $true.

The script takes the following parameters, all of which are optional and default to $true if not specified:

- **cleargpos**: (Boolean) Clear GPOs not being used
- **installupdates**: (Boolean) Install updates and reboot if necessary
- **adobe**: (Boolean) STIG Adobe Reader
- **firefox**: (Boolean) STIG Firefox
- **chrome**: (Boolean) STIG Chrome
- **IE11**: (Boolean) STIG Internet Explorer 11
- **edge**: (Boolean) STIG Edge
- **dotnet**: (Boolean) STIG .NET Framework
- **office**: (Boolean) STIG Office
- **onedrive**: (Boolean) STIG OneDrive
- **java**: (Boolean) STIG Java
- **windows**: (Boolean) STIG Windows
- **defender**: (Boolean) STIG Windows Defender
- **firewall**: (Boolean) STIG Windows Firewall
- **mitigations**: (Boolean) STIG Mitigations
- **nessusPID**: (Boolean) Resolve Unquoted Strings in Path
- **horizon**: (Boolean) STIG VMware Horizon
- **sosoptional**: (Boolean) Optional STIG/Hardening items

An example of how to run the script with all default parameters would be:

```powershell
.\secure-standalone.ps1
```
If you want to specify a different value for one or more of the parameters, you can include them in the command along with their desired value. For example, if you wanted to run the script and set the $firefox parameter to $false, the command would be:

```powershell
.\secure-standalone.ps1 -firefox $false
```

You can also specify multiple parameters in the command like this:

```powershell
.\secure-standalone.ps1 -firefox $false -chrome $false
```

Tingueu en compte que en aquest exemple, tant els paràmetres de Firefox com de Chrome s'estableixen en $false.



