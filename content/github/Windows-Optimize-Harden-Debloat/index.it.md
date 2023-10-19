---
title: "Ottimizza e rafforza il tuo sistema Windows con lo script Windows-Optimize-Harden-Debloat"
date: 2020-12-29
toc: true
draft: false
description: "Questa guida completa fornisce istruzioni dettagliate su come ottimizzare, rafforzare e sbloccare il sistema Windows per migliorare le prestazioni, la sicurezza e la privacy."
tags: ["Ottimizzazione Windows", "Indurimento di Windows", "Debloating di Windows", "Sicurezza Windows", "Prestazioni Windows", "Privacy di Windows", "Aggiornamenti di Windows", "Oggetti Criteri di gruppo", "Adobe Acrobat Reader", "Firefox", "Google Chrome", "Internet Explorer", "Bordo del cromo di Microsoft", "Punto netto 4", "Microsoft Office", "Una guida", "Oracle JRE 8", "firewall di Windows", "Difensore di Windows", "Blocco applicazioni"]
---
 Introduzione:

Windows 10 e Windows 11 sono sistemi operativi invasivi e non sicuri pronti all'uso.
Organizzazioni come[PrivacyTools.io](https://PrivacyTools.io), [Microsoft](https://microsoft.com), [Cyber.mil](https://public.cyber.mil), the [Department of Defense](https://dod.gov), and the [National Security Agency](https://www.nsa.gov/) hanno consigliato modifiche alla configurazione per bloccare, rafforzare e proteggere il sistema operativo. Queste modifiche coprono un'ampia gamma di mitigazioni, tra cui il blocco della telemetria, delle macro, la rimozione di bloatware e la prevenzione di molti attacchi digitali e fisici a un sistema. Questo script ha lo scopo di automatizzare le configurazioni consigliate da tali organizzazioni.

## Note, avvertenze e considerazioni:

**AVVERTIMENTO:**

Questo script dovrebbe funzionare per la maggior parte, se non per tutti, i sistemi senza problemi. Mentre[@SimeonOnSecurity](https://github.com/simeononsecurity) creates, reviews, and tests each repo intensively, we can not test every possible configuration nor does [@SimeonOnSecurity](https://github.com/simeononsecurity) take any responsibility for breaking your system. If something goes wrong, be prepared to submit an [issue](../../issues)

- Questo script è progettato per funzionare principalmente in ambienti di **uso personale**. Con questo in mente, alcune impostazioni di configurazione aziendale non sono implementate. Questo script non è progettato per portare un sistema al 100% di conformità. Piuttosto dovrebbe essere utilizzato come trampolino di lancio per completare la maggior parte, se non tutte, le modifiche alla configurazione che possono essere programmate saltando problemi passati come branding e banner in cui questi non dovrebbero essere implementati nemmeno in un ambiente di uso personale rafforzato.
- Questo script è progettato in modo tale che le ottimizzazioni, a differenza di altri script, non interrompano le funzionalità di base di Windows.
- Funzionalità come Windows Update, Windows Defender, Windows Store e Cortona sono state limitate, ma non sono in uno stato disfunzionale come la maggior parte degli altri script Privacy di Windows 10.
- Se cerchi uno script ridotto a icona destinato solo ad ambienti commerciali, consulta questo[GitHub Repository](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)


**Non eseguire questo script se non capisci cosa fa. È tua responsabilità rivedere e testare lo script prima di eseguirlo.**

**AD ESEMPIO, QUANTO SEGUENTE SI INTERROMPERÀ SE LO ESEGUITI SENZA PRENDERE MISURE PREVENTIVE:**

- L'utilizzo dell'account amministratore predefinito denominato "Administrator" è disabilitato e rinominato per DoD STIG

  - Non si applica all'account predefinito creato ma si applica all'utilizzo dell'account amministratore predefinito che si trova spesso nelle versioni Enterprise, IOT e Windows Server

  - Crea un nuovo account in Gestione computer e impostalo come amministratore, se lo desideri. Quindi copia il contenuto della cartella degli utenti precedenti in quella nuova dopo aver effettuato l'accesso al nuovo utente per la prima volta per aggirare il problema prima di eseguire lo script.

- L'accesso tramite un account Microsoft è disabilitato per DoD STIG.

  - Quando cerchi di essere sicuro e privato, non è consigliabile accedere al tuo account locale tramite un account Microsoft. Questo è applicato da questo repository.

  - Crea un nuovo account in Gestione computer e impostalo come amministratore, se lo desideri. Quindi copia il contenuto della cartella degli utenti precedenti in quella nuova dopo aver effettuato l'accesso al nuovo utente per la prima volta per aggirare il problema prima di eseguire lo script.

- I PIN dell'account sono disabilitati per DoD STIG

  - I PIN non sono sicuri se utilizzati esclusivamente al posto di una password e possono essere facilmente aggirati in poche ore o potenzialmente anche in secondi o minuti

  - Rimuovi il pin dall'account e/o accedi utilizzando la password dopo aver eseguito lo script.

- Le impostazioni predefinite di Bitlocker sono state modificate e rafforzate grazie a DoD STIG.

  - A causa di come viene implementato il bitlocker, quando si verificano queste modifiche e se hai già abilitato il bitlocker, l'implementazione del bitlocker verrà interrotta.

  - Disattiva bitlocker, esegui lo script, quindi riattiva bitlocker per risolvere questo problema.

## Requisiti:

- [x] Windows 10/11 Enterprise (**Preferito**) o Professional
  - Le edizioni Home di Windows 10/11 non supportano le configurazioni GPO e non sono testate.
  - Le edizioni Window "N" non sono testate.
-[x] [Standards](https://docs.microsoft.com/en-us/windows-hardware/design/device-experiences/oem-highly-secure) per un dispositivo Windows 10 altamente sicuro
-[x] System is [fully up to date and supported](https://support.microsoft.com/en-gb/help/4027667/windows-10-update)
  - Corri il[Windows Upgrade Assistant](https://support.microsoft.com/en-us/help/3159635/windows-10-update-assistant) per aggiornare e verificare l'ultima major release.
- [x] Bitlocker deve essere sospeso o disattivato prima di implementare questo script, può essere riattivato dopo il riavvio.
  - Le esecuzioni successive di questo script possono essere eseguite senza disabilitare il bitlocker.
- [x] Requisiti hardware
  -[Hardware Requirements for Memory Integrity](https://docs.microsoft.com/en-us/windows/security/threat-protection/device-guard/requirements-and-deployment-planning-guidelines-for-virtualization-based-protection-of-code-integrity#baseline-protections)
  -[Hardware Requirements for Virtualization-Based Security](https://docs.microsoft.com/en-us/windows-hardware/design/device-experiences/oem-vbs)
  -[Hardware Requirements for Windows Defender Application Guard](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-guard/reqs-wd-app-guard)
  -[Hardware Requirements for Windows Defender Credential Guard](https://docs.microsoft.com/en-us/windows/security/identity-protection/credential-guard/credential-guard-requirements)

## Materiale di lettura consigliato:

-[System Guard Secure Launch](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-system-guard/system-guard-secure-launch-and-smm-protection#requirements-met-by-system-guard-enabled-machines)
-[System Guard Root of Trust](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-system-guard/system-guard-how-hardware-based-root-of-trust-helps-protect-windows)
-[Hardware-based Isolation](https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-atp/overview-hardware-based-isolation)
-[Memory integrity](https://docs.microsoft.com/en-us/windows/security/threat-protection/device-guard/memory-integrity)
-[Windows Defender Application Guard](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-guard/wd-app-guard-overview)
-[Windows Defender Credential Guard](https://docs.microsoft.com/en-us/windows/security/identity-protection/credential-guard/credential-guard-how-it-works)

## Aggiunte, modifiche importanti e correzioni di bug:

**Questo script aggiunge, rimuove e modifica le impostazioni del tuo sistema. Si prega di rivedere lo script prima di eseguirlo.**

### Browser:

- I browser avranno estensioni aggiuntive installate per favorire la privacy e la sicurezza.
  - Vedere[here](https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/11) per ulteriori informazioni.
- A causa degli STIG DoD implementati per i browser, vengono impostate la gestione delle estensioni e altre impostazioni aziendali. Per istruzioni su come visualizzare queste opzioni, è necessario consultare le istruzioni dell'oggetto Criteri di gruppo di seguito.

### Moduli PowerShell:

- Per aiutare ad automatizzare gli aggiornamenti di Windows PowerShell[PSWindowsUpdate](https://www.powershellgallery.com/packages/PSWindowsUpdate/2.0.0.4) verrà aggiunto al tuo sistema.

### Correzione dell'account Microsoft, dello Store o dei servizi Xbox:

Questo perché blocchiamo l'accesso agli account Microsoft. La telemetria e l'associazione di identità di Microsoft sono disapprovate.
Tuttavia, se desideri ancora utilizzare questi servizi, consulta i seguenti ticket di emissione per la risoluzione:

- https://github.com/simeononsecurity/Windows-Optimize-Debloat/issues/1
- https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/16
- https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/22

### Modifica dei criteri in Criteri di gruppo locali dopo il fatto:

Se è necessario modificare o modificare un'impostazione, molto probabilmente sono configurabili tramite GPO:

- Importa le definizioni dei criteri ADMX da questo[repo](https://github.com/simeononsecurity/STIG-Compliant-Domain-Prep/tree/master/Files/PolicyDefinitions) in _C:\windows\PolicyDefinitions_ sul sistema che stai tentando di modificare.

- Apri `gpedit.msc` sul sistema che stai tentando di modificare.

## Un elenco di script e strumenti utilizzati da questa raccolta:

### Prima festa:

-[.NET-STIG-Script](https://github.com/simeononsecurity/.NET-STIG-Script)
-[Automate-Sysmon](https://github.com/simeononsecurity/Automate-Sysmon)
-[FireFox-STIG-Script](https://github.com/simeononsecurity/FireFox-STIG-Script)
-[JAVA-STIG-Script](https://github.com/simeononsecurity/JAVA-STIG-Script)
-[Standalone-Windows-STIG-Script](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)
-[Windows-Defender-STIG-Script](https://github.com/simeononsecurity/Windows-Defender-STIG-Script)
-[Windows-Optimize-Debloat](https://github.com/simeononsecurity/Windows-Optimize-Debloat)

### Terzo:

-[Cyber.mil - Group Policy Objects](https://public.cyber.mil/stigs/gpo/)
-[Microsoft Security Compliance Toolkit 1.0](https://www.microsoft.com/en-us/download/details.aspx?id=55319)
-[Microsoft Sysinternals - Sysmon](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon)

## STIGS/SRG applicati:

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

## Ulteriori configurazioni sono state prese in considerazione da:

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

## Come eseguire lo script:
### GUI - Installazione guidata:

Scarica l'ultima versione[here](https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat-GUI/releases/)scegli le opzioni che desideri e premi esegui. <img src="https://raw.githubusercontent.com/simeononsecurity/Windows-Optimize-Harden-Debloat/master/.github/images/WOHD-GUI.gif" alt="Esempio di installazione guidata basata su GUI Windows-Optimize-Harden-Debloat"> ### Installazione automatica: usa questo one-liner per scaricare automaticamente, decomprimere tutti i file di supporto ed eseguire l&#39;ultima versione dello script.```powershell
iwr -useb 'https://simeononsecurity.com/scripts/windowsoptimizeandharden.ps1'|iex
```

<img src="https://raw.githubusercontent.com/simeononsecurity/Windows-Optimize-Harden-Debloat/master/.github/images/w10automatic.gif" alt="Example of 
Windows-Optimize-Harden-Debloat automatic install">

### Manual Install:

If manually downloaded, the script must be launched from an administrative powershell in the directory containing all the files from the [GitHub Repository](https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat)

The script "sos-optimize-windows.ps1" includes several parameters that allow for customization of the optimization process. Each parameter is a boolean value that defaults to true if not specified.

- **cleargpos**: Clears Group Policy Objects settings.
- **installupdates**: Installs updates to the system.
- **adobe**: Implements the Adobe Acrobat Reader STIGs.
- **firefox**: Implements the FireFox STIG.
- **chrome**: Implements the Google Chrome STIG.
- **IE11**: Implements the Internet Explorer 11 STIG.
- **edge**: Implements the Microsoft Chromium Edge STIG.
- **dotnet**: Implements the Dot Net 4 STIG.
- **office**: Implements the Microsoft Office Related STIGs.
- **onedrive**: Implements the Onedrive STIGs.
- **java**: Implements the Oracle Java JRE 8 STIG.
- **windows**: Implements the Windows Desktop STIGs.
- **defender**: Implements the Windows Defender STIG.
- **firewall**: Implements the Windows Firewall STIG.
- **mitigations**: Implements General Best Practice Mitigations.
- **defenderhardening**: Implements and Hardens Windows Defender Beyond STIG Requirements.
- **pshardening**: Implements PowerShell Hardening and Logging.
- **sslhardening**: Implements SSL Hardening.
- **smbhardening**: Hardens SMB Client and Server Settings.
- **applockerhardening**: Installs and Configures Applocker (In Audit Only Mode).
- **bitlockerhardening**: Harden Bitlocker Implementation.
- **removebloatware**: Removes unnecessary programs and features from the system.
- **disabletelemetry**: Disables data collection and telemetry.
- **privacy**: Makes changes to improve privacy.
- **imagecleanup**: Cleans up unneeded files from the system.
- **nessusPID**: Resolves Unquoted System Strings in Path.
- **sysmon**: Installs and configures sysmon to improve auditing capabilities.
- **diskcompression**: Compresses the system disk.
- **emet**: Implements STIG Requirements and Hardening for EMET on Windows 7 Systems.
- **updatemanagement**: Changes the way updates are managed and improved on the system.
- **deviceguard**: Enables Device Guard Hardening.
- **sosbrowsers**: Optimizes the system's web browsers.

An example of how to launch the script with specific parameters would be:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
Get-ChildItem -Recurse *.ps1 | Unblock-File
powershell.exe -ExecutionPolicy ByPass -File .\sos-optimize-windows.ps1 -cleargpos:$false -installupdates:$false
```
