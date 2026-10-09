---
title: "Guide complet pour renforcer Windows avec Windows Defender..."
date: 2020-12-16
toc: true
draft: false
description: Apprenez à utiliser Windows Defender Application Control WDAC pour renforcer votre système d'exploitation Windows avec des scripts et des outils.
tags:
- Renforcement de Windows Defender Application Control WDAC
- PowerShell
- Script PowerShell
- Automatisation
- Conformité
- Équipe Bleue
- Script STIG Windows Defender
- Renforcement de Windows Defender
- STIG Windows Defender
- STIG Defender
- Protection contre les exploits Windows Defender WDEP
- Réduction de la surface d'attaque Windows Defender ASR
- Windows Server 2016 2019
- Windows Server Core
- Microsoft WDAC-Toolkit
- Actualiser la politique CI
- Règles de blocage recommandées par Microsoft
- Règles de blocage des pilotes recommandées par Microsoft
- Politiques XML
- Politiques BIN
- Stratégie de groupe
- Microsoft Intune
cover: /img/cover/Windows-Defender-Application-Control-Hardening.webp
coverAlt: Une illustration d'une salle de serveurs futuriste avec des écrans lumineux affichant des structures de fichiers XML et BIN liées à Windows Defender Application Control. Le fond sombre met en valeur les couleurs vives.
coverCaption: ''
lastmod: 2026-10-08
---

**Renforcer Windows avec Windows Defender Application Control WDAC**

## Notes :
- Windows Server 2016/2019 ou toute version antérieure à la 1903 ne supporte qu'une seule politique héritée à la fois.
- L'édition Windows Server Core supporte [WDAC](https://simeononsecurity.com/til/2022-05-18/) mais certains composants dépendant d'AppLocker ne fonctionneront pas
- Veuillez lire les [Lectures recommandées](https://github.com/simeononsecurity/Windows-Defender-Application-Control-Hardening#recommended-reading) avant de mettre en œuvre ou même de tester.

## Une liste des scripts et outils utilisés dans cette collection :

- [MicrosoftDocs - WDAC-Toolkit](https://github.com/MicrosoftDocs/WDAC-Toolkit)
- [Microsoft - Actualiser la politique CI](https://www.microsoft.com/en-us/download/details.aspx?id=102925)

## Configurations supplémentaires prises en compte :

- [Microsoft - Règles de blocage recommandées](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules)
- [Microsoft - Règles de blocage des pilotes recommandées](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules)
- [Microsoft - Windows Defender Application Control](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/windows-defender-application-control-design-guide)

## Explication :

### XML vs. BIN :

- En termes simples, les politiques **"XML"** sont destinées à être appliquées localement sur une machine et les fichiers **"BIN"** servent à les appliquer via [Stratégie de groupe](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-windows-defender-application-control-policies-using-group-policy) ou [Microsoft Intune](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-windows-defender-application-control-policies-using-intune). Bien que vous puissiez utiliser des politiques XML, BIN ou CIP en déploiement local, il est généralement conseillé de privilégier XML lorsque c'est possible, surtout lors d'audits ou de dépannage.

### Descriptions des politiques :

- **Politiques par défaut :**
  - Les politiques "Par défaut" utilisent uniquement les fonctionnalités par défaut disponibles dans le WDAC-Toolkit.
- **Politiques recommandées :**
  - Les politiques "Recommandées" utilisent les fonctionnalités par défaut ainsi que les [règles de blocage](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules) et [règles de blocage des pilotes](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules) recommandées par Microsoft.
- **Politiques d'audit :**
  - Les politiques "Audit" ne font que consigner les exceptions aux règles. Ceci est destiné aux tests dans votre environnement, afin que vous puissiez modifier les politiques librement pour répondre aux besoins de votre environnement.
- **Politiques appliquées :**
  - Les politiques "Appliquées" n'autorisent aucune exception aux règles, les applications, pilotes, dll, etc. seront bloqués s'ils ne sont pas conformes.

### Politiques disponibles :

- **XML :**
  - **Audit uniquement :**
    - `WDAC_V1_Default_Audit_{version}.xml`
    - `WDAC_V1_Recommended_Audit_{version}.xml`
  - **Appliquées :**
    - `WDAC_V1_Default_Enforced_{version}.xml`
    - `WDAC_V1_Recommended_Enforced_{version}.xml`
- **BIN :**
  - **Audit uniquement :**
    - `WDAC_V1_Default_Audit_{version}.bin`
    - `WDAC_V1_Recommended_Audit_{version}.bin`
  - **Appliquées :**
    - `WDAC_V1_Default_Enforced_{version}.bin`
    - `WDAC_V1_Recommended_Enforced_{version}.bin`
- **CIP :**
  - **Audit uniquement :**
    - `WDAC_V1_Default_Audit\{uid}.cip`
    - `WDAC_V1_Recommended_Audit\{uid}.cip`
  - **Appliquées :**
    - `WDAC_V1_Default_Enforced\{uid}.cip`
    - `WDAC_V1_Recommended_Enforced\{uid}.cip`

Mettez à jour la ligne suivante dans le script pour utiliser la politique souhaitée localement :

```powershell
$PolicyPath = "C:\temp\Windows Defender\CIP\WDAC_V1_Recommended_Enforced\*.cip"
#https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deployment/deploy-wdac-policies-with-script
ForEach ($Policy in (Get-ChildItem -Recurse $PolicyPath).Fullname) {
  $PolicyBinary = "$Policy"
  $DestinationFolder = $env:windir+"\System32\CodeIntegrity\CIPolicies\Active\"
  $RefreshPolicyTool = "./Files/EXECUTABLES/RefreshPolicy(AMD64).exe"
  Copy-Item -Path $PolicyBinary -Destination $DestinationFolder -Force
  & $RefreshPolicyTool
}
```

Alternativement, vous pouvez utiliser [Stratégie de groupe](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-windows-defender-application-control-policies-using-group-policy) ou [Microsoft Intune](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-windows-defender-application-control-policies-using-intune) pour appliquer les politiques WDAC.

## Audit :

Vous pouvez consulter les journaux d'événements WDAC dans l'observateur d'événements sous :

`Applications and Services Logs\Microsoft\Windows\CodeIntegrity\Operational`

## Lectures recommandées :

- [Argonsys - Déploiement de la politique de contrôle des applications Windows 10](https://argonsys.com/microsoft-cloud/library/deploying-windows-10-application-control-policy/)
- [Microsoft - Auditer les politiques Windows Defender Application Control](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/audit-windows-defender-application-control-policies)
- [Microsoft - Créer une politique WDAC pour les appareils à charge de travail fixe en utilisant un ordinateur de référence](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/create-initial-default-policy)
- [Microsoft - Déployer les politiques Windows Defender Application Control via la stratégie de groupe](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-windows-defender-application-control-policies-using-group-policy)
- [Microsoft - Déployer les politiques Windows Defender Application Control via Microsoft Intune](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-windows-defender-application-control-policies-using-intune)
- [Microsoft - Déployer les politiques WDAC via script](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deployment/deploy-wdac-policies-with-script)
- [Microsoft - Appliquer les politiques Windows Defender Application Control](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/enforce-windows-defender-application-control-policies)
- [Microsoft - Guide pour créer des politiques WDAC de refus](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/create-wdac-deny-policy)
- [Microsoft - Utiliser plusieurs politiques Windows Defender Application Control](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-multiple-windows-defender-application-control-policies)

## Comment exécuter le script :

### Installation manuelle :

Si téléchargé manuellement, le script doit être lancé depuis un PowerShell administrateur dans le répertoire contenant tous les fichiers du [dépôt GitHub](https://github.com/simeononsecurity/Windows-Defender-Application-Control-Hardening/archive/main.zip)

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
Get-ChildItem -Recurse *.ps1 | Unblock-File
.\sos-wdachardening.ps1
```
