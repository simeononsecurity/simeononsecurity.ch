---
title: "Conformité à la STIG : Renforcer la sécurité du domaine et garantir le respect des exigences réglementaires"
date: 2020-09-08
---
 Introduction

Dans le paysage actuel de la cybersécurité, qui évolue rapidement, il est de la plus haute importance de garantir la sécurité et la conformité de votre domaine. **Le respect des STIG (Security Technical Implementation Guides) et des SRG (Security Requirements Guides) est crucial** pour maintenir une **infrastructure informatique solide et bien protégée**. Dans cet article, nous allons explorer comment le guide complet de **SimeonOnSecurity peut vous aider à atteindre la conformité STIG** pour votre domaine, en vous fournissant les outils et les informations nécessaires pour améliorer votre **posture de sécurité**.

## Raisonnement

Avec le **nombre croissant de cybermenaces et d'exigences réglementaires**, les organisations doivent établir une **fondation de sécurité solide dans leurs domaines**. Les STIG et les SRG offrent un ensemble de **guidelines et de meilleures pratiques** pour sécuriser divers logiciels et systèmes. En mettant en œuvre ces normes, les organisations peuvent **atténuer les risques, protéger les données sensibles** et s'assurer que leurs systèmes sont **configurés de manière sécurisée**. **Le script de préparation de domaine de SiméonOnSecurity rassemble une collection de GPO (objets de stratégie de groupe) et de configurations provenant de sources fiables**, aidant les organisations à rationaliser le processus de mise en conformité avec la STIG.

## Méthodes

**Le script de préparation de domaine de SiméonOnSecurity fournit une approche complète** pour rendre votre domaine conforme aux STIG et SRG applicables. Le guide comprend un script qui peut être exécuté dans un environnement d'entreprise pour appliquer les configurations nécessaires. En suivant ces étapes, vous pouvez **automatiser le processus et gagner un temps précieux**.

Le script importe les GPOs fournis par **SimeonOnSecurity**, qui ont été **extensively reviewed and tested**. Ces GPO couvrent un large éventail de logiciels et de systèmes, notamment **Adobe Acrobat, des navigateurs web tels que Firefox et Chrome, Microsoft Office, les systèmes d'exploitation Windows**, et bien d'autres encore. Le script garantit que les configurations sont conformes aux **dernières directives STIG et SRG**, ce qui vous aide à respecter les normes de sécurité nécessaires.

En outre, le script intègre des configurations supplémentaires provenant d'organisations réputées telles que **CERT, Microsoft et NSA Cyber**. Ces configurations répondent à des considérations de sécurité spécifiques telles que **la corruption de la mémoire, le renforcement du SSL, la gestion de la télémétrie, la mise en liste blanche des applications et la sécurité du matériel/firmware**, entre autres.

En utilisant le script de préparation de domaine de SimeonOnSecurity, les organisations peuvent **améliorer la posture de sécurité de leur domaine, réduire les vulnérabilités** et démontrer leur conformité avec les réglementations et les normes pertinentes.
________


**Préparation de domaine conforme au STIG**
*Importez toutes les GPO fournies par SimeonOnSecurity pour vous aider à rendre votre domaine conforme à toutes les STIG et SRG applicables.

[![VirusTotal Scan](https://github.com/simeononsecurity/STIG-Compliant-Domain-Prep/actions/workflows/virustotal.yml/badge.svg)](https://github.com/simeononsecurity/STIG-Compliant-Domain-Prep/actions/workflows/virustotal.yml)

**Note:** Ce script devrait fonctionner sans problème sur la plupart des systèmes, si ce n'est sur tous. Tout en [@SimeonOnSecurity](https://github.com/simeononsecurity) creates, reviews, and tests each repo intensivly, we can not test every possible configuration nor does [@SimeonOnSecurity](https://github.com/simeononsecurity) take any responsibility for breaking your system. If something goes wrong, be prepared to submit an [issue](../../issues) N'exécutez pas ce script si vous ne comprenez pas ce qu'il fait.

## Notes :

**Ce script est conçu pour être utilisé dans des environnements d'entreprise**

## Ansible :
Nous proposons désormais une collection de playbooks pour ce script. Veuillez consulter ce qui suit :
- [Github Repo](https://github.com/simeononsecurity/Windows_STIG_Ansible)
- [Ansible Galaxy](https://galaxy.ansible.com/simeononsecurity/windows_stigs)

## Des configurations supplémentaires ont été prises en compte à partir de :
- [CERT - IE Scripting Engine Memory Corruption](https://kb.cert.org/vuls/id/573168/)
- [Dirteam - SSL Hardening](https://dirteam.com/sander/2019/07/30/howto-disable-weak-protocols-cipher-suites-and-hashing-algorithms-on-web-application-proxies-ad-fs-servers-and-windows-servers-running-azure-ad-connect/)
- [Microsoft - Managing Windows 10 Telemetry and Callbacks](https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services)
- [Microsoft - Specture and Meltdown Mitigations](https://support.microsoft.com/en-us/help/4072698/windows-server-speculative-execution-side-channel-vulnerabilities)
- [Microsoft - Windows 10 Privacy](https://docs.microsoft.com/en-us/windows/privacy/)
- [Microsoft - Windows 10 VDI Recomendations](https://docs.microsoft.com/en-us/windows-server/remote/remote-desktop-services/rds_vdi-recommendations-1909)
- [Microsoft - Windows Defender Application Control](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/windows-defender-application-control-design-guide)
- [NSACyber - Application Whitelisting Using Microsoft AppLocker](https://apps.nsa.gov/iad/library/ia-guidance/tech-briefs/application-whitelisting-using-microsoft-applocker.cfm)
- [NSACyber - Hardware-and-Firmware-Security-Guidance](https://github.com/nsacyber/Hardware-and-Firmware-Security-Guidance)
- [Whonix - Disable TCP Timestamps](https://www.whonix.org/wiki/Disable_TCP_and_ICMP_Timestamps)

## STIGS/SRGs appliqués :
- [Adobe Acrobat Pro DC Continuous V2R1](https://public.cyber.mil/stigs/downloads/)
- [Adobe Acrobat Reader DC Continuous V2R1](https://public.cyber.mil/stigs/downloads/)
- [Firefox V5R2](https://public.cyber.mil/stigs/downloads/) - **[Requires Separate Script](https://github.com/simeononsecurity/FireFox-STIG-Script)
- [Google Chrome V2R4](https://public.cyber.mil/stigs/downloads/)
- [Internet Explorer 11 V1R19](https://public.cyber.mil/stigs/downloads/)
- [Microsoft Edge V1R2](https://public.cyber.mil/stigs/downloads/)
- [Microsoft .Net Framework 4 V1R9](https://public.cyber.mil/stigs/downloads/) - **[Requires Separate Script](https://github.com/simeononsecurity/.NET-STIG-Script)
- [Microsoft Office 2013 V2R1](https://public.cyber.mil/stigs/downloads/)
- [Microsoft Office 2016 V2R1](https://public.cyber.mil/stigs/downloads/)
- [Microsoft Office 2019/Office 365 Pro Plus V2R3](https://public.cyber.mil/stigs/downloads/)
- [Microsoft OneDrive STIG V2R1](https://public.cyber.mil/stigs/downloads/)
- [Oracle JRE 8 V1R5](https://public.cyber.mil/stigs/downloads/) - **[Requires Separate Script](https://github.com/simeononsecurity/Oracle-JRE-8-STIG-Script)
- [Windows 10 V2R2](https://public.cyber.mil/stigs/downloads/)
- [Windows Defender Antivirus V2R2](https://public.cyber.mil/stigs/downloads/) - **[Requires Separate Script](https://github.com/simeononsecurity/Windows-Defender-STIG-Script)
- [Windows Firewall V1R7](https://public.cyber.mil/stigs/downloads/)
- [Windows Server 2012(R2) V3R2](https://public.cyber.mil/stigs/downloads/)
- [Windows Server 2016 V2R2](https://public.cyber.mil/stigs/downloads/)
- [Windows Server 2019 V2R2](https://public.cyber.mil/stigs/downloads/)
- [VMWare Horizon Agent V1R1](https://public.cyber.mil/stigs/downloads/)
- [VMWare Horizon Client V1R1](https://public.cyber.mil/stigs/downloads/)


## Utilisation :
### Script PowerShell :

**Le script peut être lancé à partir du téléchargement GitHub extrait comme ceci:**
```
.\sos-stig-compliant-domain-prep.ps1
```
Le script que nous allons utiliser doit être lancé à partir du répertoire contenant tous les autres fichiers de l'application [GitHub Repository](https://github.com/simeononsecurity/STIG-Compliant-Domain-Prep)


