---
title: "Aujourd'hui, j'en ai appris plus sur la création et la mise en œuvre de la politique de la WDAC"
date: 2022-05-18
toc: true
draft: false
description: "Aujourd'hui, j'en ai appris plus sur les conditionnelles et la gestion des variables d'Ansible"
genre: ["Automatisation", "Sécurité Windows", "Contrôle de l'application", "Windows Defender", "WDAC", "Powershell", "Protection contre les menaces", "Windows Server 2019", "Sécurité des entreprises", "Gestion des politiques", "Meilleures pratiques en matière de sécurité"]
tags: ["automation", "WDAC", "contrôle de l'application", "Contrôle des applications Windows Defender", "Windows Defender", "Powershell", "Microsoft documentation", "Création de la politique du WDAC", "déploiement de la politique", "déploiement par script", "plusieurs politiques de la WDAC", "les dispositifs à charge de travail fixe", "applications de confiance", "refuser les politiques", "pratiques de sécurité", "gestion des politiques", "sécurité des entreprises", "protection contre les menaces", "Serveur Windows", "Sécurité Windows", "liste blanche des applications"]
---

**Ce que SimeonOnSecurity a appris et trouvé intéressant aujourd'hui**

Aujourd'hui, SimeonOnSecurity a mis à jour son référentiel Windows-Defender-Application-Control-Hardening et a découvert Windows Defender Application Control (WDAC), une fonctionnalité de Windows 10 Enterprise et Windows Server 2019 qui assure la sécurité en contrôlant ce qui est exécuté sur un appareil.

SimeonOnSecurity s'est plongé dans la documentation Microsoft sur le WDAC et a découvert plusieurs ressources clés pour créer et déployer des politiques. Il a découvert comment créer une politique WDAC pour les appareils à charge de travail fixe à l'aide d'un ordinateur de référence, comment déployer des politiques WDAC à l'aide d'un script et comment utiliser plusieurs politiques pour différents scénarios.

En outre, SimeonOnSecurity a eu un aperçu des conseils sur la création de politiques de refus WDAC, ce qui lui a permis de mieux comprendre le concept d'autoriser uniquement les applications de confiance à s'exécuter sur un appareil, tout en refusant toutes les autres.

Dans l'ensemble, l'exploration de Windows Defender Application Control par SimeonOnSecurity a renforcé sa compréhension de l'importance du contrôle des applications dans les pratiques de sécurité modernes.

## Repos mis à jour :
- [simeononsecurity/Windows-Defender-Application-Control-Hardening](https://github.com/simeononsecurity/Windows-Defender-Application-Control-Hardening)

## Lecture du WDAC :
- [Microsoft - Create a WDAC policy for fixed-workload devices using a reference computer](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/create-initial-default-policy)
- [Microsoft - Deploy WDAC policies using script](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deployment/deploy-wdac-policies-with-script)
- [Microsoft - Guidance on Creating WDAC Deny Policies](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/create-wdac-deny-policy)
- [Microsoft - Use multiple Windows Defender Application Control Policies](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-multiple-windows-defender-application-control-policies)
