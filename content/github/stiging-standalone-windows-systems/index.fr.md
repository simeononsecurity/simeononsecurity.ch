---
title: "Automatiser la conformité à la STIG de Windows 10 avec un script Powershell"
date: 2020-08-26
---

**Téléchargez tous les fichiers nécessaires à partir du site web [GitHub Repository](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)

**Nous recherchons de l'aide pour les tâches suivantes [.Net issue](https://github.com/simeononsecurity/W10-Optimize-and-Harden/issues/3) 

## Introduction :

Windows 10 est un système d'exploitation non sécurisé dès sa sortie de l'emballage et nécessite de nombreux changements pour assurer la sécurité de l'utilisateur. [FISMA](https://www.cisa.gov/federal-information-security-modernization-act) la conformité.
Des organisations comme [Microsoft](https://microsoft.com), [Cyber.mil](https://public.cyber.mil), the [Department of Defense](https://dod.gov), and the [National Security Agency](https://www.nsa.gov/) ont recommandé et exigé des changements de configuration pour verrouiller, durcir et sécuriser le système d'exploitation et assurer la conformité avec le gouvernement. Ces modifications couvrent un large éventail de mesures d'atténuation, notamment le blocage de la télémétrie et des macros, la suppression des logiciels gonflants et la prévention de nombreuses attaques physiques sur un système.

Les systèmes autonomes sont parmi les plus difficiles et les plus ennuyeux à sécuriser. Lorsqu'ils ne sont pas automatisés, ils nécessitent des modifications manuelles de chaque STIG/SRG. Cela représente plus de 1000 changements de configuration pour un déploiement typique et une moyenne de 5 minutes par changement, ce qui équivaut à 3,5 jours de travail. Ce script a pour but d'accélérer ce processus de manière significative.

## Notes :

- Ce script est conçu pour fonctionner dans des environnements **Entreprise** et suppose que vous disposez d'un support matériel pour toutes les exigences.
  - Pour les systèmes personnels, veuillez consulter le document suivant [GitHub Repository](https://github.com/simeononsecurity/W10-Optimize-and-Harden)
- Ce script n'est pas conçu pour amener un système à 100% de conformité, il devrait plutôt être utilisé comme un tremplin pour compléter la plupart, sinon la totalité, des changements de configuration qui peuvent être scriptés.
  - Sans la documentation du système, cette collection devrait vous amener à une conformité d'environ 95 % pour tous les STIGS/SRG appliqués.

## Exigences :
- [X] Windows 10 Enterprise est **Exigé** par STIG.
- [x] [Standards](https://docs.microsoft.com/en-us/windows-hardware/design/device-experiences/oem-highly-secure) pour un appareil Windows 10 hautement sécurisé
- [x] System is [fully up to date](https://support.microsoft.com/en-gb/help/4027667/windows-10-update)
  - Actuellement Windows 10 **v1909** ou **v2004**.
  - Exécutez l'application [Windows 10 Upgrade Assistant](https://support.microsoft.com/en-us/help/3159635/windows-10-update-assistant) à mettre à jour et à vérifier la dernière version majeure.
- [X] Configuration matérielle requise
  - [Hardware Requirements for Memory Integrity](https://docs.microsoft.com/en-us/windows/security/threat-protection/device-guard/requirements-and-deployment-planning-guidelines-for-virtualization-based-protection-of-code-integrity#baseline-protections) 
  - [Hardware Requirements for Windows Defender Application Guard](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-guard/reqs-wd-app-guard)
  - [Hardware Requirements for Windows Defender Credential Guard](https://docs.microsoft.com/en-us/windows/security/identity-protection/credential-guard/credential-guard-requirements)
  
## Matériel de lecture recommandé :
  - [System Guard Secure Launch](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-system-guard/system-guard-secure-launch-and-smm-protection#requirements-met-by-system-guard-enabled-machines)
  - [System Guard Root of Trust](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-system-guard/system-guard-how-hardware-based-root-of-trust-helps-protect-windows)
  - [Hardware-based Isolation](https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-atp/overview-hardware-based-isolation)
  - [Memory integrity](https://docs.microsoft.com/en-us/windows/security/threat-protection/device-guard/memory-integrity)
  - [Windows Defender Application Guard](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-guard/wd-app-guard-overview)
  - [Windows Defender Credential Guard](https://docs.microsoft.com/en-us/windows/security/identity-protection/credential-guard/credential-guard-how-it-works)

## Une liste de scripts et d'outils utilisés par cette collection :

- [Microsoft Security Compliance Toolkit 1.0](https://www.microsoft.com/en-us/download/details.aspx?id=55319)

- [Cyber.mil - Group Policy Objects](https://public.cyber.mil/stigs/gpo/)

- [NSACyber - Bitlocker Guidance](https://github.com/nsacyber/BitLocker-Guidance)

## D'autres configurations ont été prises en compte à partir de :

- [NSACyber - Hardware-and-Firmware-Security-Guidance](https://github.com/nsacyber/Hardware-and-Firmware-Security-Guidance)

- [NSACyber - Application Whitelisting Using Microsoft AppLocker](https://apps.nsa.gov/iad/library/ia-guidance/tech-briefs/application-whitelisting-using-microsoft-applocker.cfm)

## STIGS/SRGs appliqués :
 
- [Windows 10 V1R23](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MS_Windows_10_V1R23_STIG.zip)

- [Windows Defender Antivirus V1R9](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MS_Windows_Defender_Antivirus_V1R9_STIG.zip)

- [Windows Firewall V1R7](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Windows_Firewall_V1R7_STIG.zip)

- [Internet Explorer 11 V1R19](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MS_IE11_V1R19_STIG.zip)

- [Adobe Reader Pro DC Continous V1R2](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Adobe_Acrobat_Pro_DC_Continuous_V1R2_STIG.zip)

- [Microsoft Office 2019/Office 365 Pro Plus V1R2](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MS_Office_365_ProPlus_V1R2_STIG.zip)

- [Microsoft Office 2016 V1R2](https://dl.dod.cyber.mil/wp-content/uploads/stigs/pdf/U_Microsoft_Office_2016_V1R2_Overview.pdf)

- [Microsoft Office 2013 V1R5](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MicrosoftOffice2013_V1R5_Overview.zip)

- [Google Chrome V1R19](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Google_Chrome_V1R19_STIG.zip)

- [Firefox V4R29](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MOZ_FireFox_V4R29_STIG.zip)

- [Microsoft .Net Framework 4 V1R9](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MS_DotNet_Framework_4-0_V1R9_STIG.zip) - **Travaux en cours**

- [Oracle JRE 8 V1R5](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Oracle_JRE_8_Windows_V1R5_STIG.zip)

## Comment exécuter le script

**Le script peut être lancé à partir du téléchargement GitHub extrait comme ceci:**
```
.\secure-standalone.ps1
```
Le script que nous allons utiliser doit être lancé à partir du répertoire contenant tous les autres fichiers de l'application [GitHub Repository](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)
