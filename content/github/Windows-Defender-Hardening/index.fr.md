---
title: "Amélioration de la sécurité de Windows 10 avec le script de durcissement Defender"
date: 2020-11-15
toc: true
draft: false
description: "Découvrez comment améliorer la sécurité de Windows 10 avec un script PowerShell qui renforce l'antivirus Windows Defender, en implémentant toutes les exigences de l'antivirus Windows Defender STIG V2R1."
tags: ["Windows Defender", "Windows 10", "Sécurité Windows 10", "Script PowerShell", "Durcissement", "Renforcement du défenseur", "Automatisation de la sécurité", "Conformité", "Accès contrôlé aux dossiers", "Système de prévention des intrusions", "Contrôle des applications", "Réduction de la surface d'attaque", "Protections contre les exploits", "Protections fournies par le cloud", "Protections réseau", "Script STIG Windows Defender", "Windows Defender STIG", "Antivirus Windows Defender STIG V2R1", "WDAC", "RSA"]
---


## Que fait ce script ?
- Active les protections fournies par le cloud
- Permet l'accès contrôlé aux dossiers
- Active les protections réseau
- Active le système de prévention des intrusions
-[Enables Windows Defender Application Control Policies](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/windows-defender-application-control)
-[Enables Windows Defender Attack Surface Reduction Rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-atp/attack-surface-reduction)
-[Enables Windows Defender Exploit Protections](https://docs.microsoft.com/en-us/microsoft-365/security/defender-endpoint/enable-exploit-protection?view=o365-worldwide#powershell)
- Met en œuvre toutes les exigences énumérées dans le[Windows Defender Antivirus STIG V2R1](https://dl.cyber.mil/stigs/zip/U_MS_Windows_Defender_Antivirus_V2R1_STIG.zip)

## Exigences:
- [x] Windows 10 Entreprise (**Préféré**) ou Windows 10 Professionnel
  - Windows 10 Home ne permet pas les configurations GPO ou[ASR](https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-atp/attack-surface-reduction) 
Bien que la plupart de ces configurations s'appliquent toujours.
  - Les éditions "N" de Windows 10 ne sont pas testées.

## Téléchargez les fichiers requis :

Téléchargez les fichiers requis à partir du[GitHub Repository](https://github.com/simeononsecurity/Windows-Defender-STIG-Script)

## Comment exécuter le script :

**Le script peut être lancé à partir du téléchargement GitHub extrait comme ceci :**
```
.\sos-windowsdefenderhardening.ps1
```
