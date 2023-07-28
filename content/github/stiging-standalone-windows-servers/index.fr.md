---
title: "Automatiser la conformité STIG du serveur Windows avec les scripts STIG"
date: 2020-09-09
---

**Téléchargez tous les fichiers nécessaires à partir du site web [GitHub Repository](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)

**Note:** Ce script devrait fonctionner sans problème sur la plupart des systèmes, si ce n'est sur tous. Tout en [@SimeonOnSecurity](https://github.com/simeononsecurity) creates, reviews, and tests each repo intensively, we can not test every possible configuration nor does [@SimeonOnSecurity](https://github.com/simeononsecurity) take any responsibility for breaking your system. If something goes wrong, be prepared to submit an [issue](../../issues) N'exécutez pas ce script si vous ne comprenez pas ce qu'il fait. Il est de votre responsabilité de revoir et de tester le script avant de l'exécuter.

## Ansible :
Nous proposons désormais une collection de playbooks pour ce script. Veuillez consulter ce qui suit :
- [Github Repo](https://github.com/simeononsecurity/Windows_STIG_Ansible)
- [Ansible Galaxy](https://galaxy.ansible.com/simeononsecurity/windows_stigs)

## Introduction :

Windows 10 est un système d'exploitation non sécurisé dès sa sortie de l'emballage et nécessite de nombreux changements pour assurer la sécurité de l'utilisateur. [FISMA](https://www.cisa.gov/federal-information-security-modernization-act) la conformité.
Des organisations comme [Microsoft](https://microsoft.com), [Cyber.mil](https://public.cyber.mil), the [Department of Defense](https://dod.gov), and the [National Security Agency](https://www.nsa.gov/) ont recommandé et exigé des changements de configuration pour verrouiller, durcir et sécuriser le système d'exploitation et assurer la conformité avec le gouvernement. Ces modifications couvrent un large éventail de mesures d'atténuation, notamment le blocage de la télémétrie et des macros, la suppression des logiciels gonflants et la prévention de nombreuses attaques physiques sur un système.

Les systèmes autonomes sont parmi les plus difficiles et les plus ennuyeux à sécuriser. Lorsqu'ils ne sont pas automatisés, ils nécessitent des modifications manuelles de chaque STIG/SRG. Cela représente plus de 1000 changements de configuration pour un déploiement typique et une moyenne de 5 minutes par changement, ce qui équivaut à 3,5 jours de travail. Ce script a pour but d'accélérer ce processus de manière significative.

## Notes :

- Ce script est conçu pour fonctionner dans des environnements **Entreprise** et suppose que vous disposez d'un support matériel pour toutes les exigences.
  - Pour les systèmes personnels, veuillez consulter le document suivant [GitHub Repository](https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat)
- Ce script n'est pas conçu pour amener un système à 100% de conformité, il devrait plutôt être utilisé comme un tremplin pour compléter la plupart, sinon la totalité, des changements de configuration qui peuvent être scriptés.
  - Sans la documentation du système, cette collection devrait vous amener à une conformité d'environ 95 % pour tous les STIGS/SRG appliqués.

## Exigences :
- [X] Windows 10 Enterprise est requis par STIG.
- [X] [Standards](https://docs.microsoft.com/en-us/windows-hardware/design/device-experiences/oem-highly-secure) pour un appareil Windows 10 hautement sécurisé
- [X] System is [fully up to date](https://support.microsoft.com/en-gb/help/4027667/windows-10-update)
  - Exécuter le [Windows 10 Upgrade Assistant](https://support.microsoft.com/en-us/help/3159635/windows-10-update-assistant) pour mettre à jour et vérifier la dernière version majeure.
- X] Bitlocker doit être suspendu ou désactivé avant l'exécution de ce script, il peut être réactivé après le redémarrage.
  - Les exécutions suivantes de ce script peuvent être exécutées sans désactiver Bitlocker.
- X] Configuration matérielle requise
  - [Hardware Requirements for Memory Integrity](https://docs.microsoft.com/en-us/windows/security/threat-protection/device-guard/requirements-and-deployment-planning-guidelines-for-virtualization-based-protection-of-code-integrity#baseline-protections) 
  - [Hardware Requirements for Virtualization-Based Security](https://docs.microsoft.com/en-us/windows-hardware/design/device-experiences/oem-vbs)
  - [Hardware Requirements for Windows Defender Application Guard](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-guard/reqs-wd-app-guard)
  - [Hardware Requirements for Windows Defender Credential Guard](https://docs.microsoft.com/en-us/windows/security/identity-protection/credential-guard/credential-guard-requirements)
  
## Matériel de lecture recommandé :
  - [System Guard Secure Launch](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-system-guard/system-guard-secure-launch-and-smm-protection#requirements-met-by-system-guard-enabled-machines)
  - [System Guard Root of Trust](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-system-guard/system-guard-how-hardware-based-root-of-trust-helps-protect-windows)
  - [Hardware-based Isolation](https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-atp/overview-hardware-based-isolation)
  - [Memory integrity](https://docs.microsoft.com/en-us/windows/security/threat-protection/device-guard/memory-integrity)
  - [Windows Defender Application Guard](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-guard/wd-app-guard-overview)
  - [Windows Defender Credential Guard](https://docs.microsoft.com/en-us/windows/security/identity-protection/credential-guard/credential-guard-how-it-works)

## Liste des scripts et des outils utilisés par cette collection :
- [Cyber.mil - Group Policy Objects](https://public.cyber.mil/stigs/gpo/)
- [Microsoft Security Compliance Toolkit 1.0](https://www.microsoft.com/en-us/download/details.aspx?id=55319)

## Des configurations supplémentaires ont été prises en compte à partir de :
- [Microsoft - Recommended block rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules)
- [Microsoft - Recommended driver block rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules)
- [Microsoft - Windows Defender Application Control](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/windows-defender-application-control-design-guide)
- [NSACyber - Application Whitelisting Using Microsoft AppLocker](https://apps.nsa.gov/iad/library/ia-guidance/tech-briefs/application-whitelisting-using-microsoft-applocker.cfm)
- [NSACyber - Hardware-and-Firmware-Security-Guidance](https://github.com/nsacyber/Hardware-and-Firmware-Security-Guidance)
- [NSACyber - Windows Secure Host Baseline](https://github.com/nsacyber/Windows-Secure-Host-Baseline)

## STIGS/SRGs appliqués :
- [Adobe Acrobat Pro DC Continuous V2R1](https://public.cyber.mil/stigs/downloads/)
- [Adobe Acrobat Reader DC Continuous V2R1](https://public.cyber.mil/stigs/downloads/)
- [Firefox V5R2](https://public.cyber.mil/stigs/downloads/)
- [Google Chrome V2R4](https://public.cyber.mil/stigs/downloads/)
- [Internet Explorer 11 V1R19](https://public.cyber.mil/stigs/downloads/)
- [Microsoft Edge V1R2](https://public.cyber.mil/stigs/downloads/)
- [Microsoft .Net Framework 4 V1R9](https://public.cyber.mil/stigs/downloads/)
- [Microsoft Office 2013 V2R1](https://public.cyber.mil/stigs/downloads/)
- [Microsoft Office 2016 V2R1](https://public.cyber.mil/stigs/downloads/)
- [Microsoft Office 2019/Office 365 Pro Plus V2R3](https://public.cyber.mil/stigs/downloads/)
- [Microsoft OneDrive STIG V2R1](https://public.cyber.mil/stigs/downloads/)
- [Oracle JRE 8 V1R5](https://public.cyber.mil/stigs/downloads/)
- [Windows 10 V2R2](https://public.cyber.mil/stigs/downloads/)
- [Windows Firewall V1R7](https://public.cyber.mil/stigs/downloads/)

## Modifier les stratégies dans la stratégie de groupe locale après coup :
- Importer les définitions de la stratégie ADMX à partir de cette page [repo](https://github.com/simeononsecurity/STIG-Compliant-Domain-Prep/tree/master/Files/PolicyDefinitions) dans *C:\NWindows\NPolicyDefinitions* sur le système que vous essayez de modifier.
- Ouvrir ```gpedit.msc``` sur le système que vous essayez de modifier.


## Comment exécuter le script :
### Installation automatisée :
Le script peut être lancé à partir du téléchargement GitHub extrait comme suit :
```powershell
iex ((New-Object System.Net.WebClient).DownloadString('https://simeononsecurity.ch/scripts/standalonewindows.ps1'))
```

### Installation manuelle :
S'il est téléchargé manuellement, le script doit être lancé à partir du répertoire contenant tous les autres fichiers du fichier [GitHub Repository](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)

Tous les paramètres du script "secure-standalone.ps1" sont facultatifs, avec une valeur par défaut de $true. Cela signifie que si aucune valeur n'est spécifiée pour un paramètre lors de l'exécution du script, celui-ci sera traité comme s'il avait la valeur $true.

Le script prend les paramètres suivants, qui sont tous facultatifs et dont la valeur par défaut est $true s'ils ne sont pas spécifiés :

- **cleargpos** : (booléen) Efface les GPOs qui ne sont pas utilisées.
- **installupdates** : (booléen) Installer les mises à jour et redémarrer si nécessaire.
- **adobe** : (booléen) STIG Adobe Reader
- **firefox** : (Booléen) STIG Firefox
- **chrome** : (booléen) STIG Chrome
- **IE11** : (booléen) STIG Internet Explorer 11
- **edge** : (booléen) STIG Edge
- **dotnet** : (booléen) STIG .NET Framework
- Office** : (booléen) STIG Office
- **onedrive** : (booléen) STIG OneDrive
- **java** : (booléen) STIG Java
- **windows** : (Booléen) STIG Windows
- **defender** : (Booléen) STIG Windows Defender
- **firewall** : (Booléen) STIG Windows Firewall
- **mitigations** : (Booléen) STIG Mitigations
- **nessusPID** : (Booléen) Résoudre les chaînes non quotées dans le chemin d'accès
- **horizon** : (booléen) STIG VMware Horizon
- **sosoptional** : (Booléen) Éléments STIG/Durcissement optionnels

Voici un exemple d'exécution du script avec tous les paramètres par défaut :

```powershell
.\secure-standalone.ps1
```
Si vous souhaitez spécifier une valeur différente pour un ou plusieurs paramètres, vous pouvez les inclure dans la commande avec la valeur souhaitée. Par exemple, si vous souhaitez exécuter le script et définir le paramètre $firefox à $false, la commande serait la suivante :

```powershell
.\secure-standalone.ps1 -firefox $false
```

Vous pouvez également spécifier plusieurs paramètres dans la commande, comme suit :

```powershell
.\secure-standalone.ps1 -firefox $false -chrome $false
```

Notez que dans cet exemple, les paramètres Firefox et Chrome sont tous deux fixés à $false.



