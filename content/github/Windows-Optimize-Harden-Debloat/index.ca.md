---
title: "Optimitzeu i enduriu el vostre sistema Windows amb l'script Windows-Optimize-Harden-Debloat"
date: 2020-12-29
toc: true
draft: false
description: "Aquesta guia completa proporciona instruccions pas a pas sobre com optimitzar, endurir i desbloquejar el vostre sistema Windows per millorar el rendiment, la seguretat i la privadesa."
tags: ["Optimització de Windows", "Enduriment de finestres", "Windows desinflat", "Seguretat de Windows", "Rendiment de Windows", "Privadesa de Windows", "Actualitzacions de Windows", "Objectes de política de grup", "Adobe Acrobat Reader", "Firefox", "Google Chrome", "Internet Explorer", "Microsoft Chromium Edge", "Dot Net 4", "Microsoft Office", "Onedrive", "Oracle Java JRE 8", "Firewall de Windows", "Windows Defender", "Applocker"]
---
 Introducció:

Windows 10 i Windows 11 són sistemes operatius invasius i insegurs des de la caixa.
Organitzacions com[PrivacyTools.io](https://PrivacyTools.io), [Microsoft](https://microsoft.com), [Cyber.mil](https://public.cyber.mil), the [Department of Defense](https://dod.gov), and the [National Security Agency](https://www.nsa.gov/) han recomanat canvis de configuració per bloquejar, endurir i protegir el sistema operatiu. Aquests canvis cobreixen una àmplia gamma de mitigacions, com ara el bloqueig de la telemetria, les macros, l'eliminació de bloatware i la prevenció de molts atacs digitals i físics a un sistema. Aquest script pretén automatitzar les configuracions recomanades per aquestes organitzacions.

## Notes, advertències i consideracions:

**ADVERTIMENT:**

Aquest script hauria de funcionar per a la majoria, si no tots, els sistemes sense problemes. Mentre[@SimeonOnSecurity](https://github.com/simeononsecurity) creates, reviews, and tests each repo intensively, we can not test every possible configuration nor does [@SimeonOnSecurity](https://github.com/simeononsecurity) take any responsibility for breaking your system. If something goes wrong, be prepared to submit an [issue](../../issues)

- Aquest script està dissenyat per funcionar principalment en entorns d'**Ús personal**. Tenint això en compte, alguns paràmetres de configuració de l'empresa no estan implementats. Aquest script no està dissenyat per fer que un sistema compleixi al 100%. Més aviat s'hauria d'utilitzar com a trampolí per completar la majoria, si no tots, els canvis de configuració que es poden escriure mentre es salten problemes anteriors com la marca i els bàners on no s'han d'implementar fins i tot en un entorn d'ús personal endurit.
- Aquest script està dissenyat de manera que les optimitzacions, a diferència d'altres scripts, no trencaran la funcionalitat bàsica de Windows.
- S'han restringit funcions com Windows Update, Windows Defender, Windows Store i Cortona, però no es troben en un estat disfuncional com la majoria dels altres scripts de privadesa de Windows 10.
- Si cerqueu un script minimitzat dirigit només a entorns comercials, consulteu això[GitHub Repository](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)


**No executeu aquest script si no enteneu què fa. És responsabilitat vostra revisar i provar l'script abans d'executar-lo.**

**PER EXEMPLE, EL SEGÜENT ES TRALLARÀ SI HO EXECUTIU SENSE FER MESURES PREVENTIVAS:**

- L'ús del compte d'administrador predeterminat anomenat "Administrador" està desactivat i canviat de nom segons DoD STIG

  - No s'aplica al compte predeterminat creat, però sí a l'ús del compte d'administrador predeterminat que es troba sovint a les versions Enterprise, IOT i Windows Server

  - Creeu un compte nou a Gestió d'ordinadors i configureu-lo com a administrador si ho voleu. A continuació, copieu el contingut de la carpeta d'usuaris anteriors a la nova després d'iniciar la sessió amb l'usuari nou per primera vegada per solucionar-ho abans d'executar l'script.

- L'inici de sessió amb un compte de Microsoft està desactivat segons DoD STIG.

  - Quan intenteu ser segur i privat, no es recomana iniciar la sessió al vostre compte local mitjançant un compte de Microsoft. Això s'aplica amb aquest repo.

  - Creeu un compte nou a Gestió d'ordinadors i configureu-lo com a administrador si ho voleu. A continuació, copieu el contingut de la carpeta d'usuaris anteriors a la nova després d'iniciar la sessió amb l'usuari nou per primera vegada per solucionar-ho abans d'executar l'script.

- Els PIN del compte estan desactivats segons DoD STIG

  - Els PIN són insegurs quan s'utilitzen únicament en lloc d'una contrasenya i es poden evitar fàcilment en qüestió d'hores o fins i tot de segons o minuts

  - Traieu el pin del compte i/o inicieu la sessió amb la contrasenya després d'executar l'script.

- Els valors predeterminats de Bitlocker es canvien i s'endureixen a causa del DoD STIG.

  - A causa de com s'implementa bitlocker, quan es produeixin aquests canvis i si ja el teniu habilitat, trencarà la implementació de bitlocker.

  - Desactiveu Bitlocker, executeu l'script i, a continuació, torneu a activar Bitlocker per solucionar aquest problema.

## Requisits:

- [x] Windows 10/11 Enterprise (**Preferit**) o Professional
  - Les edicions de Windows 10/11 Home no admeten configuracions GPO i no s'han provat.
  - Finestra "N" Edicions no estan provades.
-[x] [Standards](https://docs.microsoft.com/en-us/windows-hardware/design/device-experiences/oem-highly-secure) per a un dispositiu Windows 10 altament segur
-[x] System is [fully up to date and supported](https://support.microsoft.com/en-gb/help/4027667/windows-10-update)
  - Executar el[Windows Upgrade Assistant](https://support.microsoft.com/en-us/help/3159635/windows-10-update-assistant) per actualitzar i verificar la darrera versió principal.
- [x] Bitlocker s'ha de suspendre o desactivar abans d'implementar aquest script, es pot tornar a activar després de reiniciar.
  - Les execucions de seguiment d'aquest script es poden executar sense desactivar Bitlocker.
- [x] Requisits de maquinari
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

## Addicions, canvis notables i correccions d'errors:

**Aquest script afegeix, elimina i canvia la configuració del vostre sistema. Reviseu l'script abans d'executar-lo.**

### Navegadors:

- Els navegadors tindran extensions addicionals instal·lades per ajudar a la privadesa i la seguretat.
  - Mira[here](https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/11) per obtenir informació addicional.
- A causa dels STIG del DoD implementats per als navegadors, s'estableix la gestió d'extensions i altres configuracions empresarials. Per obtenir instruccions sobre com veure aquestes opcions, haureu de consultar les instruccions GPO a continuació.

### Mòduls Powershell:

- Per ajudar a automatitzar les actualitzacions de Windows de PowerShell[PSWindowsUpdate](https://www.powershellgallery.com/packages/PSWindowsUpdate/2.0.0.4) el mòdul s'afegirà al vostre sistema.

### Arreglar el compte de Microsoft, la botiga o els serveis de Xbox:

Això es deu al fet que bloquegem la sessió als comptes de Microsoft. L'associació de telemetria i identitat de Microsoft està mal vista.
Tanmateix, si encara voleu utilitzar aquests serveis, consulteu els següents tiquets d'emissió per a la resolució:

- https://github.com/simeononsecurity/Windows-Optimize-Debloat/issues/1
- https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/16
- https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/22

### Edició de polítiques a la política de grup local després del fet:

Si necessiteu modificar o canviar una configuració, és probable que es puguin configurar mitjançant GPO:

- Importeu les definicions de la política ADMX d'aquesta[repo](https://github.com/simeononsecurity/STIG-Compliant-Domain-Prep/tree/master/Files/PolicyDefinitions) a _C:\windows\PolicyDefinitions_ al sistema que esteu intentant modificar.

- Obriu `gpedit.msc` al sistema que esteu intentant modificar.

## Una llista de scripts i eines que utilitza aquesta col·lecció:

### Primera part:

-[.NET-STIG-Script](https://github.com/simeononsecurity/.NET-STIG-Script)
-[Automate-Sysmon](https://github.com/simeononsecurity/Automate-Sysmon)
-[FireFox-STIG-Script](https://github.com/simeononsecurity/FireFox-STIG-Script)
-[JAVA-STIG-Script](https://github.com/simeononsecurity/JAVA-STIG-Script)
-[Standalone-Windows-STIG-Script](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)
-[Windows-Defender-STIG-Script](https://github.com/simeononsecurity/Windows-Defender-STIG-Script)
-[Windows-Optimize-Debloat](https://github.com/simeononsecurity/Windows-Optimize-Debloat)

### Tercera festa:

-[Cyber.mil - Group Policy Objects](https://public.cyber.mil/stigs/gpo/)
-[Microsoft Security Compliance Toolkit 1.0](https://www.microsoft.com/en-us/download/details.aspx?id=55319)
-[Microsoft Sysinternals - Sysmon](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon)

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
-[Windows Defender Antivirus V2R2](https://public.cyber.mil/stigs/downloads/)
-[Windows Firewall V1R7](https://public.cyber.mil/stigs/downloads/)

## S'han considerat configuracions addicionals de:

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

## Com executar l'script:
### GUI - Instal·lació guiada:

Descarrega l'última versió[here](https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat-GUI/releases/)trieu les opcions que vulgueu i premeu executa. <img src="https://raw.githubusercontent.com/simeononsecurity/Windows-Optimize-Harden-Debloat/master/.github/images/WOHD-GUI.gif" alt="Exemple d&#39;instal·lació guiada basada en la GUI de Windows-Optimize-Harden-Debloat"> ### Instal·lació automàtica: utilitzeu aquesta línia única per descarregar automàticament, descomprimir tots els fitxers compatibles i executar la darrera versió de l&#39;script.```powershell
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
