---
title: "Optimisez et renforcez votre système Windows avec le script Windows-Optimize-Harden-Debloat"
date: 2020-12-29
toc: true
draft: false
description: "Ce guide complet fournit des instructions étape par étape sur la façon d'optimiser, de renforcer et de dégonfler votre système Windows pour améliorer les performances, la sécurité et la confidentialité."
tags: ["Optimisation Windows", "Durcissement de Windows", "Dégonflement de Windows", "Sécurité Windows", "Performances Windows", "Confidentialité Windows", "Mises à jour Windows", "Objets de stratégie de groupe", "Adobe Acrobat Reader", "Firefox", "Google Chrome", "Internet Explorer", "Microsoft Chrome Edge", "Filet à points 4", "Microsoft Office", "Onedrive", "OracleJava JRE 8", "fenêtre pare-feu", "Windows Defender", "Verrouillage d'applications"]
---
 Introduction:

Windows 10 et Windows 11 sont des systèmes d'exploitation invasifs et non sécurisés prêts à l'emploi.
Des organisations comme[PrivacyTools.io](https://PrivacyTools.io), [Microsoft](https://microsoft.com), [Cyber.mil](https://public.cyber.mil), the [Department of Defense](https://www.defense.gov/), and the [National Security Agency](https://www.nsa.gov/) ont recommandé des changements de configuration pour verrouiller, renforcer et sécuriser le système d'exploitation. Ces modifications couvrent un large éventail de mesures d'atténuation, notamment le blocage de la télémétrie, des macros, la suppression des bloatwares et la prévention de nombreuses attaques numériques et physiques sur un système. Ce script vise à automatiser les configurations recommandées par ces organisations.

## Remarques, avertissements et considérations :

**AVERTISSEMENT:**

Ce script devrait fonctionner sans problème pour la plupart des systèmes, sinon tous. Alors que[@SimeonOnSecurity](https://github.com/simeononsecurity) creates, reviews, and tests each repo intensively, we can not test every possible configuration nor does [@SimeonOnSecurity](https://github.com/simeononsecurity) take any responsibility for breaking your system. If something goes wrong, be prepared to submit an [issue](../../issues)

- Ce script est conçu pour fonctionner principalement dans des environnements **à usage personnel**. Dans cet esprit, certains paramètres de configuration d'entreprise ne sont pas implémentés. Ce script n'est pas conçu pour amener un système à 100 % de conformité. Il devrait plutôt être utilisé comme un tremplin pour compléter la plupart, sinon la totalité, des changements de configuration qui peuvent être scriptés tout en sautant les problèmes passés comme la marque et les bannières où ceux-ci ne devraient pas être mis en œuvre même dans un environnement d'utilisation personnelle durci.
- Ce script est conçu de manière à ce que les optimisations, contrairement à certains autres scripts, ne cassent pas la fonctionnalité principale de Windows.
- Des fonctionnalités telles que Windows Update, Windows Defender, le Windows Store et Cortona ont été restreintes, mais ne sont pas dans un état dysfonctionnel comme la plupart des autres scripts de confidentialité de Windows 10.
- Si vous recherchez un script réduit destiné uniquement aux environnements commerciaux, veuillez consulter ceci[GitHub Repository](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)


**N'exécutez pas ce script si vous ne comprenez pas ce qu'il fait. Il est de votre responsabilité d'examiner et de tester le script avant de l'exécuter.**

**PAR EXEMPLE, CE QUI SUIT SERA BRISÉ SI VOUS EXÉCUTEZ CELA SANS PRENDRE DES MESURES PRÉVENTIVES :**

- L'utilisation du compte administrateur par défaut nommé "Administrateur" est désactivée et renommée par DoD STIG

  - Ne s'applique pas au compte par défaut créé mais s'applique à l'utilisation du compte administrateur par défaut souvent trouvé sur les versions Enterprise, IOT et Windows Server

  - Créez un nouveau compte sous Gestion de l'ordinateur et définissez-le en tant qu'administrateur si vous le souhaitez. Copiez ensuite le contenu du dossier des utilisateurs précédents dans le nouveau après vous être connecté au nouvel utilisateur pour la première fois afin de contourner ce problème avant d'exécuter le script.

- La connexion à l'aide d'un compte Microsoft est désactivée par DoD STIG.

  - Lorsque vous essayez d'être sécurisé et privé, il n'est pas conseillé de vous connecter à votre compte local via un compte Microsoft. Ceci est appliqué par ce dépôt.

  - Créez un nouveau compte sous Gestion de l'ordinateur et définissez-le en tant qu'administrateur si vous le souhaitez. Copiez ensuite le contenu du dossier des utilisateurs précédents dans le nouveau après vous être connecté au nouvel utilisateur pour la première fois afin de contourner ce problème avant d'exécuter le script.

- Les codes PIN de compte sont désactivés par DoD STIG

  - Les codes PIN ne sont pas sécurisés lorsqu'ils sont utilisés uniquement à la place d'un mot de passe et peuvent être facilement contournés en quelques heures, voire quelques secondes ou minutes

  - Supprimez le code PIN du compte et/ou connectez-vous à l'aide d'un mot de passe après avoir exécuté le script.

- Les valeurs par défaut de Bitlocker sont modifiées et renforcées en raison de DoD STIG.

  - En raison de la façon dont bitlocker est implémenté, lorsque ces changements se produisent et si vous avez déjà activé bitlocker, cela interrompra l'implémentation de bitlocker.

  - Désactivez bitlocker, exécutez le script, puis réactivez bitlocker pour contourner ce problème.

## Exigences:

- [x] Windows 10/11 Entreprise (**Préféré**) ou Professionnel
  - Les éditions Windows 10/11 Home ne prennent pas en charge les configurations GPO et ne sont pas testées.
  - Les éditions Window "N" ne sont pas testées.
-[x] [Standards](https://docs.microsoft.com/en-us/windows-hardware/design/device-experiences/oem-highly-secure) pour un appareil Windows 10 hautement sécurisé
-[x] System is [fully up to date and supported](https://support.microsoft.com/en-gb/help/4027667/windows-10-update)
  - Exécutez le[Windows Upgrade Assistant](https://support.microsoft.com/en-us/help/3159635/windows-10-update-assistant) pour mettre à jour et vérifier la dernière version majeure.
- [x] Bitlocker doit être suspendu ou désactivé avant d'implémenter ce script, il peut être réactivé après le redémarrage.
  - Les exécutions de suivi de ce script peuvent être exécutées sans désactiver le bitlocker.
- [x] Configuration matérielle requise
  -[Hardware Requirements for Memory Integrity](https://docs.microsoft.com/en-us/windows/security/threat-protection/device-guard/requirements-and-deployment-planning-guidelines-for-virtualization-based-protection-of-code-integrity#baseline-protections)
  -[Hardware Requirements for Virtualization-Based Security](https://docs.microsoft.com/en-us/windows-hardware/design/device-experiences/oem-vbs)
  -[Hardware Requirements for Windows Defender Application Guard](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-guard/reqs-wd-app-guard)
  -[Hardware Requirements for Windows Defender Credential Guard](https://docs.microsoft.com/en-us/windows/security/identity-protection/credential-guard/credential-guard-requirements)

## Lectures recommandées :

-[System Guard Secure Launch](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-system-guard/system-guard-secure-launch-and-smm-protection#requirements-met-by-system-guard-enabled-machines)
-[System Guard Root of Trust](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-system-guard/system-guard-how-hardware-based-root-of-trust-helps-protect-windows)
-[Hardware-based Isolation](https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-atp/overview-hardware-based-isolation)
-[Memory integrity](https://docs.microsoft.com/en-us/windows/security/threat-protection/device-guard/memory-integrity)
-[Windows Defender Application Guard](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-guard/wd-app-guard-overview)
-[Windows Defender Credential Guard](https://docs.microsoft.com/en-us/windows/security/identity-protection/credential-guard/credential-guard-how-it-works)

## Ajouts, modifications notables et corrections de bugs :

**Ce script ajoute, supprime et modifie les paramètres de votre système. Veuillez revoir le script avant de l'exécuter.**

### Navigateurs :

- Les navigateurs auront des extensions supplémentaires installées pour aider à la confidentialité et à la sécurité.
  - Voir[here](https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/11) pour plus d'informations.
- En raison des STIG du DoD mis en œuvre pour les navigateurs, la gestion des extensions et d'autres paramètres d'entreprise sont définis. Pour savoir comment afficher ces options, vous devrez consulter les instructions GPO ci-dessous.

### Modules Powershell :

- Pour aider à automatiser les mises à jour Windows, le PowerShell[PSWindowsUpdate](https://www.powershellgallery.com/packages/PSWindowsUpdate/2.0.0.4) module sera ajouté à votre système.

### Correction du compte Microsoft, de la boutique ou des services Xbox :

En effet, nous bloquons la connexion aux comptes Microsoft. L'association télémétrie et identité de Microsoft est mal vue.
Toutefois, si vous souhaitez toujours utiliser ces services, consultez les tickets de problème suivants pour la résolution :

- https://github.com/simeononsecurity/Windows-Optimize-Debloat/issues/1
- https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/16
- https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/22

### Modification des stratégies dans la stratégie de groupe locale après coup :

Si vous avez besoin de modifier ou de changer un paramètre, ils sont très probablement configurables via GPO :

- Importez les définitions de stratégie ADMX à partir de ce[repo](https://github.com/simeononsecurity/STIG-Compliant-Domain-Prep/tree/master/Files/PolicyDefinitions) dans _C:\windows\PolicyDefinitions_ sur le système que vous essayez de modifier.

- Ouvrez `gpedit.msc` sur le système que vous essayez de modifier.

## Une liste de scripts et d'outils utilisés par cette collection :

### Première fête:

-[.NET-STIG-Script](https://github.com/simeononsecurity/.NET-STIG-Script)
-[Automate-Sysmon](https://github.com/simeononsecurity/Automate-Sysmon)
-[FireFox-STIG-Script](https://github.com/simeononsecurity/FireFox-STIG-Script)
-[JAVA-STIG-Script](https://github.com/simeononsecurity/JAVA-STIG-Script)
-[Standalone-Windows-STIG-Script](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)
-[Windows-Defender-STIG-Script](https://github.com/simeononsecurity/Windows-Defender-STIG-Script)
-[Windows-Optimize-Debloat](https://github.com/simeononsecurity/Windows-Optimize-Debloat)

### Tierce personne:

-[Cyber.mil - Group Policy Objects](https://public.cyber.mil/stigs/gpo/)
-[Microsoft Security Compliance Toolkit 1.0](https://www.microsoft.com/en-us/download/details.aspx?id=55319)
-[Microsoft Sysinternals - Sysmon](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon)

## STIGS/SRG appliqués :

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

## Des configurations supplémentaires ont été envisagées à partir de :

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

## Comment exécuter le script :
### GUI - Installation guidée :

Téléchargez la dernière version[here](https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat-GUI/releases/)choisissez les options que vous voulez et appuyez sur exécuter. <img src="https://raw.githubusercontent.com/simeononsecurity/Windows-Optimize-Harden-Debloat/master/.github/images/WOHD-GUI.gif" alt="Exemple d&#39;installation guidée basée sur l&#39;interface graphique Windows-Optimize-Harden-Debloat"> ### Installation automatisée : utilisez cette ligne pour télécharger automatiquement, décompressez tous les fichiers de prise en charge et exécutez la dernière version du script.```powershell
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
