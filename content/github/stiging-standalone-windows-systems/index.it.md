---
title: "Automazione della conformità STIG di Windows 10 con lo script PowerShell"
date: 2020-08-26
---

**Scarica tutti i file richiesti dal file[GitHub Repository](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)

**Stiamo cercando aiuto con quanto segue[.Net issue](https://github.com/simeononsecurity/W10-Optimize-and-Harden/issues/3) 

## Introduzione:

Windows 10 è un sistema operativo non sicuro pronto all'uso e richiede molte modifiche per essere assicurato[FISMA](https://www.cisa.gov/federal-information-security-modernization-act) conformità.
Organizzazioni come[Microsoft](https://microsoft.com), [Cyber.mil](https://public.cyber.mil), the [Department of Defense](https://dod.gov), and the [National Security Agency](https://www.nsa.gov/) hanno raccomandato e richiesto modifiche alla configurazione per bloccare, rafforzare e proteggere il sistema operativo e garantire la conformità del governo. Queste modifiche coprono un'ampia gamma di mitigazioni, tra cui il blocco della telemetria, delle macro, la rimozione di bloatware e la prevenzione di molti attacchi fisici a un sistema.

I sistemi autonomi sono alcuni dei sistemi più difficili e fastidiosi da proteggere. Quando non sono automatizzati, richiedono modifiche manuali di ogni STIG/SRG. Totale di oltre 1000 modifiche alla configurazione su un'implementazione tipica e una media di 5 minuti per modifica pari a 3,5 giorni di lavoro. Questo script mira ad accelerare significativamente tale processo.

## Appunti:

- Questo script è progettato per funzionare in ambienti **Enterprise** e presuppone che tu disponga del supporto hardware per tutti i requisiti.
  - Per i sistemi personali vedere questo[GitHub Repository](https://github.com/simeononsecurity/W10-Optimize-and-Harden)
- Questo script non è progettato per portare un sistema al 100% di conformità, piuttosto dovrebbe essere utilizzato come trampolino di lancio per completare la maggior parte, se non tutte, le modifiche alla configurazione che possono essere scriptate.
  - Meno la documentazione di sistema, questa raccolta dovrebbe portare fino a circa il 95% di conformità su tutti gli STIGS/SRG applicati.

## Requisiti:
- [X] Windows 10 Enterprise è **Richiesto** per STIG.
-[x] [Standards](https://docs.microsoft.com/en-us/windows-hardware/design/device-experiences/oem-highly-secure) per un dispositivo Windows 10 altamente sicuro
-[x] System is [fully up to date](https://support.microsoft.com/en-gb/help/4027667/windows-10-update)
  - Attualmente Windows 10 **v1909** o **v2004**.
  - Corri il[Windows 10 Upgrade Assistant](https://support.microsoft.com/en-us/help/3159635/windows-10-update-assistant) per essere aggiornato e verificare l'ultima versione principale.
- [X] Requisiti hardware
  -[Hardware Requirements for Memory Integrity](https://docs.microsoft.com/en-us/windows/security/threat-protection/device-guard/requirements-and-deployment-planning-guidelines-for-virtualization-based-protection-of-code-integrity#baseline-protections) 
  -[Hardware Requirements for Windows Defender Application Guard](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-guard/reqs-wd-app-guard)
  -[Hardware Requirements for Windows Defender Credential Guard](https://docs.microsoft.com/en-us/windows/security/identity-protection/credential-guard/credential-guard-requirements)
  
## Materiale di lettura consigliato:
  -[System Guard Secure Launch](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-system-guard/system-guard-secure-launch-and-smm-protection#requirements-met-by-system-guard-enabled-machines)
  -[System Guard Root of Trust](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-system-guard/system-guard-how-hardware-based-root-of-trust-helps-protect-windows)
  -[Hardware-based Isolation](https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-atp/overview-hardware-based-isolation)
  -[Memory integrity](https://docs.microsoft.com/en-us/windows/security/threat-protection/device-guard/memory-integrity)
  -[Windows Defender Application Guard](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-guard/wd-app-guard-overview)
  -[Windows Defender Credential Guard](https://docs.microsoft.com/en-us/windows/security/identity-protection/credential-guard/credential-guard-how-it-works)

## Un elenco di script e strumenti utilizzati da questa raccolta:

-[Microsoft Security Compliance Toolkit 1.0](https://www.microsoft.com/en-us/download/details.aspx?id=55319)

-[Cyber.mil - Group Policy Objects](https://public.cyber.mil/stigs/gpo/)

-[NSACyber - Bitlocker Guidance](https://github.com/nsacyber/BitLocker-Guidance)

## Ulteriori configurazioni sono state prese in considerazione da:

-[NSACyber - Hardware-and-Firmware-Security-Guidance](https://github.com/nsacyber/Hardware-and-Firmware-Security-Guidance)

-[NSACyber - Application Whitelisting Using Microsoft AppLocker](https://apps.nsa.gov/iad/library/ia-guidance/tech-briefs/application-whitelisting-using-microsoft-applocker.cfm)

## STIGS/SRG applicati:
 
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

-[Microsoft .Net Framework 4 V1R9](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MS_DotNet_Framework_4-0_V1R9_STIG.zip) - **Lavori in corso**

-[Oracle JRE 8 V1R5](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Oracle_JRE_8_Windows_V1R5_STIG.zip)

## Come eseguire lo script

**Lo script può essere avviato dal download GitHub estratto in questo modo:**
```
.\secure-standalone.ps1
```
Lo script che useremo deve essere lanciato dalla directory contenente tutti gli altri file dal file[GitHub Repository](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)
