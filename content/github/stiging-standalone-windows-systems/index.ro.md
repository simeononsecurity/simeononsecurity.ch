---
title: "Automatizarea conformității Windows 10 STIG cu Powershell Script"
date: 2020-08-26
---

**Descărcați toate fișierele necesare din[GitHub Repository](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)

**Căutăm ajutor pentru următoarele[.Net issue](https://github.com/simeononsecurity/W10-Optimize-and-Harden/issues/3) 

## Introducere:

Windows 10 este un sistem de operare nesigur din cutie și necesită multe modificări pentru asigurare[FISMA](https://www.cisa.gov/federal-information-security-modernization-act) conformitate.
Organizații ca[Microsoft](https://microsoft.com), [Cyber.mil](https://public.cyber.mil), the [Department of Defense](https://www.defense.gov/), and the [National Security Agency](https://www.nsa.gov/) au recomandat și necesare modificări de configurare pentru blocarea, consolidarea și securizarea sistemului de operare și pentru a asigura conformitatea guvernamentală. Aceste modificări acoperă o gamă largă de atenuări, inclusiv blocarea telemetriei, macrocomenzi, eliminarea bloatware-ului și prevenirea multor atacuri fizice asupra unui sistem.

Sistemele de sine stătătoare sunt unele dintre cele mai dificil și enervant sisteme de securizat. Atunci când nu sunt automatizate, acestea necesită modificări manuale ale fiecărui STIG/SRG. Însumând peste 1000 de modificări de configurare la o implementare tipică și o medie de 5 minute per modificare, ceea ce înseamnă 3,5 zile de lucru. Acest script își propune să accelereze acest proces în mod semnificativ.

## Note:

- Acest script este conceput pentru funcționarea în medii **Enterprise** și presupune că aveți suport hardware pentru toate cerințele.
  - Pentru sistemele personale, vă rugăm să vedeți asta[GitHub Repository](https://github.com/simeononsecurity/W10-Optimize-and-Harden)
- Acest script nu este conceput pentru a aduce un sistem la conformitate 100%, mai degrabă ar trebui să fie folosit ca o piatră de temelie pentru a finaliza majoritatea, dacă nu toate, modificările de configurare care pot fi scriptate.
  - Minus documentația de sistem, această colecție ar trebui să vă aducă până la aproximativ 95% conformitate cu toate STIGS/SRG aplicate.

## Cerințe:
- [X] Windows 10 Enterprise este **Necesar** conform STIG.
-[x] [Standards](https://docs.microsoft.com/en-us/windows-hardware/design/device-experiences/oem-highly-secure) pentru un dispozitiv Windows 10 extrem de sigur
-[x] System is [fully up to date](https://support.microsoft.com/en-gb/help/4027667/windows-10-update)
  - În prezent, Windows 10 **v1909** sau **v2004**.
  - Rulați[Windows 10 Upgrade Assistant](https://support.microsoft.com/en-us/help/3159635/windows-10-update-assistant) să fie actualizat și să verifice ultima versiune majoră.
- [X] Cerințe hardware
  -[Hardware Requirements for Memory Integrity](https://docs.microsoft.com/en-us/windows/security/threat-protection/device-guard/requirements-and-deployment-planning-guidelines-for-virtualization-based-protection-of-code-integrity#baseline-protections) 
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

-[Microsoft Security Compliance Toolkit 1.0](https://www.microsoft.com/en-us/download/details.aspx?id=55319)

-[Cyber.mil - Group Policy Objects](https://public.cyber.mil/stigs/gpo/)

-[NSACyber - Bitlocker Guidance](https://github.com/nsacyber/BitLocker-Guidance)

## Au fost luate în considerare configurații suplimentare din:

-[NSACyber - Hardware-and-Firmware-Security-Guidance](https://github.com/nsacyber/Hardware-and-Firmware-Security-Guidance)

-[NSACyber - Application Whitelisting Using Microsoft AppLocker](https://apps.nsa.gov/iad/library/ia-guidance/tech-briefs/application-whitelisting-using-microsoft-applocker.cfm)

## STIGS/SRG aplicate:
 
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

-[Microsoft .Net Framework 4 V1R9](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MS_DotNet_Framework_4-0_V1R9_STIG.zip) - **Lucrare în curs**

-[Oracle JRE 8 V1R5](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Oracle_JRE_8_Windows_V1R5_STIG.zip)

## Cum se rulează scriptul

**Scriptul poate fi lansat din descărcarea GitHub extrasă astfel:**
```
.\secure-standalone.ps1
```
Scriptul pe care îl vom folosi trebuie să fie lansat din directorul care conține toate celelalte fișiere din[GitHub Repository](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)
