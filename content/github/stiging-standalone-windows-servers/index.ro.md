---
title: "Automatizarea conformității Windows Server STIG cu scripturi STIG"
date: 2020-09-09
---

**Descărcați toate fișierele necesare din[GitHub Repository](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)

**Notă:** Acest script ar trebui să funcționeze pentru majoritatea, dacă nu pentru toate, sistemele fără probleme. In timp ce[@SimeonOnSecurity](https://github.com/simeononsecurity) creates, reviews, and tests each repo intensively, we can not test every possible configuration nor does [@SimeonOnSecurity](https://github.com/simeononsecurity) take any responsibility for breaking your system. If something goes wrong, be prepared to submit an [issue](../../issues) Nu rulați acest script dacă nu înțelegeți ce face. Este responsabilitatea dumneavoastră să revizuiți și să testați scriptul înainte de a-l rula.

## Ansible:
Oferim acum o colecție de manuale pentru acest scenariu. Vă rugăm să vedeți următoarele:
-[Github Repo](https://github.com/simeononsecurity/Windows_STIG_Ansible)
-[Ansible Galaxy](https://galaxy.ansible.com/simeononsecurity/windows_stigs)

## Introducere:

Windows 10 este un sistem de operare nesigur din cutie și necesită multe modificări pentru asigurare[FISMA](https://www.cisa.gov/federal-information-security-modernization-act) conformitate.
Organizații ca[Microsoft](https://microsoft.com), [Cyber.mil](https://public.cyber.mil), the [Department of Defense](https://dod.gov), and the [National Security Agency](https://www.nsa.gov/) au recomandat și necesare modificări de configurare pentru blocarea, consolidarea și securizarea sistemului de operare și pentru a asigura conformitatea guvernamentală. Aceste modificări acoperă o gamă largă de atenuări, inclusiv blocarea telemetriei, macrocomenzi, eliminarea bloatware-ului și prevenirea multor atacuri fizice asupra unui sistem.

Sistemele de sine stătătoare sunt unele dintre cele mai dificil și enervant sisteme de securizat. Atunci când nu sunt automatizate, acestea necesită modificări manuale ale fiecărui STIG/SRG. Însumând peste 1000 de modificări de configurare la o implementare tipică și o medie de 5 minute per modificare, ceea ce înseamnă 3,5 zile de lucru. Acest script își propune să accelereze acest proces în mod semnificativ.

## Note:

- Acest script este conceput pentru funcționarea în medii **Enterprise** și presupune că aveți suport hardware pentru toate cerințele.
  - Pentru sistemele personale, vă rugăm să vedeți asta[GitHub Repository](https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat)
- Acest script nu este conceput pentru a aduce un sistem la conformitate 100%, mai degrabă ar trebui să fie folosit ca o piatră de temelie pentru a finaliza majoritatea, dacă nu toate, modificările de configurare care pot fi scriptate.
  - Minus documentația de sistem, această colecție ar trebui să vă aducă până la aproximativ 95% conformitate cu toate STIGS/SRG aplicate.

## Cerințe:
- [X] Windows 10 Enterprise este necesar pentru STIG.
-[X] [Standards](https://docs.microsoft.com/en-us/windows-hardware/design/device-experiences/oem-highly-secure) pentru un dispozitiv Windows 10 extrem de sigur
-[X] System is [fully up to date](https://support.microsoft.com/en-gb/help/4027667/windows-10-update)
  - Rulați[Windows 10 Upgrade Assistant](https://support.microsoft.com/en-us/help/3159635/windows-10-update-assistant) pentru a actualiza și a verifica cea mai recentă versiune majoră.
- [X] Bitlocker trebuie să fie suspendat sau dezactivat înainte de implementarea acestui script, acesta poate fi activat din nou după repornire.
  - Execuțiile ulterioare ale acestui script pot fi executate fără a dezactiva bitlocker.
- [X] Cerințe hardware
  -[Hardware Requirements for Memory Integrity](https://docs.microsoft.com/en-us/windows/security/threat-protection/device-guard/requirements-and-deployment-planning-guidelines-for-virtualization-based-protection-of-code-integrity#baseline-protections) 
  -[Hardware Requirements for Virtualization-Based Security](https://docs.microsoft.com/en-us/windows-hardware/design/device-experiences/oem-vbs)
  -[Hardware Requirements for Windows Defender Application Guard](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-guard/reqs-wd-app-guard)
  -[Hardware Requirements for Windows Defender Credential Guard](https://docs.microsoft.com/en-us/windows/security/identity-protection/credential-guard/credential-guard-requirements)
  
## Material de lectură recomandat:
  -[System Guard Secure Launch](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-system-guard/system-guard-secure-launch-and-smm-protection#requirements-met-by-system-guard-enabled-machines)
  -[System Guard Root of Trust](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-system-guard/system-guard-how-hardware-based-root-of-trust-helps-protect-windows)
  -[Hardware-based Isolation](https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-atp/overview-hardware-based-isolation)
  -[Memory integrity](https://docs.microsoft.com/en-us/windows/security/threat-protection/device-guard/memory-integrity)
  -[Windows Defender Application Guard](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-guard/wd-app-guard-overview)
  -[Windows Defender Credential Guard](https://docs.microsoft.com/en-us/windows/security/identity-protection/credential-guard/credential-guard-how-it-works)

## O listă de scripturi și instrumente pe care le utilizează această colecție:
-[Cyber.mil - Group Policy Objects](https://public.cyber.mil/stigs/gpo/)
-[Microsoft Security Compliance Toolkit 1.0](https://www.microsoft.com/en-us/download/details.aspx?id=55319)

## Au fost luate în considerare configurații suplimentare din:
-[Microsoft - Recommended block rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules)
-[Microsoft - Recommended driver block rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules)
-[Microsoft - Windows Defender Application Control](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/windows-defender-application-control-design-guide)
-[NSACyber - Application Whitelisting Using Microsoft AppLocker](https://apps.nsa.gov/iad/library/ia-guidance/tech-briefs/application-whitelisting-using-microsoft-applocker.cfm)
-[NSACyber - Hardware-and-Firmware-Security-Guidance](https://github.com/nsacyber/Hardware-and-Firmware-Security-Guidance)
-[NSACyber - Windows Secure Host Baseline](https://github.com/nsacyber/Windows-Secure-Host-Baseline)

## STIGS/SRG aplicate:
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

## Modificarea politicilor în Politica de grup local după fapt:
- Importați definițiile politicii ADMX din aceasta[repo](https://github.com/simeononsecurity/STIG-Compliant-Domain-Prep/tree/master/Files/PolicyDefinitions) în *C:\windows\PolicyDefinitions* pe sistemul pe care încercați să îl modificați.
- Deschis```gpedit.msc``` on on the system you're trying to modify. 


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

Rețineți că în acest exemplu, atât parametrii Firefox, cât și Chrome sunt setați la $false.



