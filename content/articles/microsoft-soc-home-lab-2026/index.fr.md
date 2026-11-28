---
title: "Laboratoire SOC Microsoft à domicile : acquérir une expérience en cybersécurité en 2026"
date: 2026-09-11
lastmod: 2026-11-27
toc: true
draft: false
description: "Créez un laboratoire SOC Microsoft avec Sentinel, Defender, Intune et Entra. Enquêtez sur des incidents, vérifiez les règles de clés d’accès et documentez des preuves pour votre portfolio."
genre: ["Cybersécurité", "Sécurité cloud", "Développement de carrière"]
tags: ["laboratoire SOC à domicile", "Microsoft Sentinel", "Microsoft Defender XDR", "Defender for Endpoint", "Defender for Cloud", "Defender for Servers", "Microsoft Intune", "Microsoft Entra ID", "laboratoire Azure à domicile", "expérience en cybersécurité", "analyste SOC", "centre des opérations de sécurité", "réponse aux incidents", "KQL", "Log Analytics", "Conditional Access", "MFA résistante à l’hameçonnage", "clés d’accès", "sécurité des identités", "portfolio cybersécurité", "gestion des coûts cloud", "sécurité des terminaux"]
cover: "/img/cover/microsoft-soc-home-lab.webp"
coverAlt: "Un ordinateur portable affiche une chronologie d’incidents de sécurité sur un bureau à domicile, sous un nuage contenant des serveurs et des terminaux."
coverCaption: ""
---

Un **laboratoire SOC à domicile** vous permet d’examiner des alertes, d’expliquer les preuves et de tester des changements défensifs. Créez un petit environnement Microsoft, recueillez sa télémétrie et consignez chaque enquête. Le résultat utile est une enquête reproductible étayée par des preuves.

Ce guide développe l’approche de laboratoire décrite dans la vidéo sur les carrières en cybersécurité de Mad Hat et dans le runbook Cyber Range fourni. Il s’appuie sur la documentation Microsoft pour les exigences produit et sépare configuration, détection et validation en tâches mesurables.

## Principaux enseignements

- **Commencez petit :** un client Windows géré et une identité de test suffisent pour les premiers exercices.
- **Vérifiez la télémétrie :** voir un appareil ou un portail connecté ne prouve pas que les journaux arrivent.
- **Terminez l’enquête :** consignez le déclencheur, les preuves, la réponse et le nouveau test.
- **Maîtrisez les dépenses :** suivez séparément licences, rétention des données, réseau et calcul.
- **Décrivez votre expérience avec exactitude :** présentez l’environnement comme un projet de laboratoire sur votre CV.

## Avant de commencer

**Prérequis :** notions d’administration Windows et de réseau, ainsi qu’une familiarité avec les machines virtuelles. Utilisez un tenant Microsoft Entra dédié et un abonnement Azure réservé au laboratoire. Gardez les identités de production, fichiers personnels et systèmes de l’employeur hors de l’exercice.

**Durée estimée :** prévoyez un week-end pour la configuration initiale, puis des séances d’enquête ciblées. Il s’agit d’une estimation de planification. L’approbation de l’essai, les quotas et la mise à disposition des services influent sur la durée réelle. **Difficulté :** intermédiaire.

Préparez un compte d’administration distinct et un utilisateur de test sans privilèges. Avant de tester les règles d’accès, établissez et vérifiez un accès d’urgence. Accordez les privilèges nécessaires à chaque tâche de configuration, puis utilisez un compte moins privilégié pour les enquêtes courantes.

| Composant | Rôle dans le laboratoire |
|---|---|
| **Sentinel** | Gestion des informations et événements de sécurité (SIEM) pour les sources de journaux connectées |
| **Defender XDR** | Corrélation et enquête dans les services de sécurité Microsoft sous licence |
| **Defender for Endpoint** (protection des terminaux) | Détection et réponse aux incidents sur les appareils intégrés |
| **Intune** | Inscription des appareils et gestion des règles de sécurité des terminaux |
| **Entra ID** | Identités, journaux de connexion et évaluation des règles d’accès |
| **Defender for Servers** (protection des serveurs) | Protection des serveurs par Defender for Cloud |

## Vérifiez d’abord les licences

**Microsoft 365 E5** constitue une option pour un laboratoire étendu, mais l’accès dépend des plans de service et des licences attribués aux utilisateurs concernés. Office 365 E5 et Microsoft 365 E5 sont des offres différentes. La licence d’un administrateur ne couvre pas automatiquement chaque utilisateur de test ou charge de travail. Consultez les [prérequis de Defender XDR](https://learn.microsoft.com/en-us/defender-xdr/prerequisites) avant de choisir un abonnement.

**Sentinel dans le portail Defender** fonctionne sans E5 ni Defender XDR. L’ajout de XDR entraîne ses propres exigences de licence et de configuration. Une vue des incidents vide ne prouve pas l’absence de licence E5. La [documentation d’intégration de Sentinel](https://learn.microsoft.com/en-us/unified-secops/microsoft-sentinel-onboard) décrit les deux configurations.

**La protection des serveurs** suit une voie de licence distincte. Defender for Servers s’intègre à Defender for Endpoint pour les charges serveur prises en charge. Les systèmes Windows clients ont besoin d’une couverture client appropriée. Ne supposez pas que chaque VM Azure dispose automatiquement d’une licence serveur. Consultez la documentation Microsoft sur [l’intégration de Defender for Endpoint](https://learn.microsoft.com/en-us/azure/defender-for-cloud/integration-defender-for-endpoint).

**Préparez l’essai :** vérifiez l’éligibilité, l’expiration, le renouvellement et les services inclus dans votre compte. Ne fondez pas votre budget sur une durée d’essai promise ou sur un montant mensuel fixe tiré d’une vidéo.

## Établissez un budget

**Les budgets Azure** envoient des notifications. Ils n’arrêtent pas la consommation lorsque vous atteignez un seuil. Les rapports de coûts sont également différés. Créez des alertes tôt et vérifiez les dépenses après chaque séance en suivant le [guide Microsoft de création de budget](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/tutorial-acm-create-budgets).

| Catégorie de coût | Question de planification |
|---|---|
| **Licences utilisateur** | Quels utilisateurs ont besoin de quels plans de service, et quand les essais expirent-ils ? |
| **Calcul** | Combien d’heures de VM chaque exercice demande-t-il ? |
| **Stockage** | Quels disques et instantanés restent après l’arrêt ? |
| **Collecte des journaux** | Quelles tables doivent être ingérées et combien de temps garder les données ? |
| **Réseau** | Le plan prévoit-il Bastion payant, adresses IP publiques ou services sortants ? |
| **Protection des serveurs** | Quelles charges ont un plan Defender payant activé ? |

**Choix de conception :** commencez par un client. Ajoutez un serveur lorsqu’un exercice exige sa télémétrie. Quatre clients et plusieurs serveurs augmentent l’administration et les coûts avant d’améliorer la pratique d’enquête.

## Construisez le réseau

**Disposition proposée :** regroupez les ressources Azure sous un nom clair, par exemple **`rg-soc-lab`**. Séparez les sous-réseaux client et serveur, définissez explicitement les règles NSG et utilisez un accès d’administration privé. La séparation des sous-réseaux ne bloque pas à elle seule le trafic entre charges.

Pour un déploiement dédié **Azure Bastion**, respectez les exigences SKU, dont le nom réservé **`AzureBastionSubnet`** et un sous-réseau de **`/26`** ou plus pour les déploiements actuels. Le SKU Developer suit un autre modèle. Consultez les [paramètres de configuration Bastion](https://learn.microsoft.com/en-us/azure/bastion/configuration-settings) avant de choisir.

Laissez RDP et SSH fermés à Internet. Limitez l’administration au chemin choisi. Autorisez les connexions sortantes nécessaires à l’inscription et à la télémétrie de sécurité.

**Validation :** établissez l’accès d’administration privé et vérifiez les règles réseau effectives avant d’installer les charges. Si vous ajoutez ensuite une application volontairement vulnérable, gardez-la dans le réseau d’exercice et limitez l’accès aux machines de test.

## Connectez Sentinel et les journaux

**Configuration du portail :** créez un espace de travail Log Analytics et activez-y Sentinel. S’il n’apparaît pas dans le portail Defender, ouvrez **System > Settings > Microsoft Sentinel > Connect a workspace** (Système > Paramètres > Microsoft Sentinel > Connecter un espace de travail). Vérifiez le tenant et les rôles Azure et Entra requis dans les [prérequis d’intégration](https://learn.microsoft.com/en-us/unified-secops/microsoft-sentinel-onboard).

**La collecte des journaux est une étape distincte.** Dans Entra, configurez les paramètres de diagnostic pour envoyer les catégories d’activité requises au même espace de travail. Commencez par les connexions interactives et les événements d’audit. Le [guide d’intégration des journaux Entra](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/howto-integrate-activity-logs-with-azure-monitor-logs) détaille les autorisations et la destination.

Le flux Sentinel actuel prend aussi en charge la connexion via le portail Microsoft Defender. Avant de diagnostiquer une table vide, confirmez que l’espace de travail principal est le bon, que le tenant correspond aux identités de test et que le compte possède les rôles requis. La visibilité dans le portail ne prouve pas l’ingestion. [Intégration Sentinel dans le portail Defender](https://learn.microsoft.com/en-us/azure/sentinel/microsoft-sentinel-onboard)

```kusto
SigninLogs
| where TimeGenerated > ago(24h)
| where UserPrincipalName =~ "soc-test@YOUR-TENANT.onmicrosoft.com"
| project TimeGenerated, UserPrincipalName, AppDisplayName,
          IPAddress, ResultType, ConditionalAccessStatus, CorrelationId
| order by TimeGenerated desc
```

Exécutez cet exemple en **Kusto Query Language (KQL)** dans la vue Logs de l’espace de travail après avoir généré une nouvelle connexion de test. Remplacez l’UPN d’exemple par celui de votre utilisateur de laboratoire. Les colonnes suivent le [schéma de la table SigninLogs](https://learn.microsoft.com/en-us/azure/azure-monitor/reference/tables/signinlogs).

**Résultat attendu :** une ligne correspondant au compte et à l’heure de connexion du test. Sans ligne, vérifiez la période, l’identité, les paramètres de collecte, la destination et le délai d’ingestion. Une table absente indique d’abord un problème de collecte ou d’espace de travail, avant un problème de détection.

## Intégrez le premier terminal

**L’inscription Intune et l’intégration EDR** sont deux étapes distinctes. Connectez Intune et Defender for Endpoint, inscrivez un client Windows pris en charge, puis attribuez une règle d’intégration EDR à son groupe de laboratoire. L’inscription Entra seule ne valide aucune de ces étapes.

Dans Intune, vérifiez **Endpoint security > Defender for Endpoint** (Sécurité des terminaux > Defender for Endpoint (protection des terminaux)). Si la connexion n’est pas disponible, activez la connexion Intune dans les fonctions avancées des terminaux de Defender. Suivez les étapes propres à la plateforme dans le [guide d’intégration Intune et Defender](https://learn.microsoft.com/en-us/intune/device-security/microsoft-defender/configure-integration).

| Point de contrôle | Preuve à recueillir |
|---|---|
| **Inscription** | Le client apparaît dans Intune avec une synchronisation récente |
| **Attribution de la règle** | La règle d’intégration s’applique au groupe d’appareils visé |
| **Rapport du capteur** | Defender indique l’intégration et une télémétrie récente |
| **Test de détection** | Un test documenté produit le signal attendu |

**Pour les serveurs**, activez le plan Defender for Servers choisi et son intégration de terminal, puis vérifiez le déploiement et les rapports du capteur. Defender for Cloud découvre les machines avant la fin de l’intégration. La seule présence dans l’inventaire ne suffit pas, comme l’explique le guide de [découverte et intégration des ressources](https://learn.microsoft.com/en-us/azure/defender-for-cloud/integration-defender-for-endpoint).

## Enquêtez sur une alerte de test

**Commencez par le test de détection EDR documenté par Microsoft** sur le terminal de laboratoire. Suivez les [instructions de test actuelles](https://learn.microsoft.com/en-us/defender-endpoint/edr-detection), y compris les prérequis de plateforme et le dépannage. Notez l’heure d’exécution avant d’ouvrir la file d’alertes.

Traitez l’alerte générée comme un exercice d’analyse. Le titre donné par le produit est un point de départ. Vous devez établir ce qui s’est passé et étayer votre décision avec des preuves.

1. **Triage :** identifiez la source de l’alerte, l’appareil, le compte et l’heure de l’événement.
2. **Inspection :** examinez l’arbre de processus, la ligne de commande, les détails du fichier et l’activité réseau disponible.
3. **Périmètre :** recherchez les activités liées sur l’identité de test et les autres appareils du laboratoire.
4. **Évaluation :** expliquez si les preuves correspondent à l’exercice prévu ou à un événement sans lien.
5. **Réponse :** consignez la réponse choisie, son impact et les étapes de rétablissement. N’effectuez une mise en confinement prise en charge que si l’exercice l’exige.
6. **Nouveau test :** après une modification de contrôle, répétez le test pertinent et comparez les preuves.

**N’inventez pas les résultats manquants.** Si l’alerte n’arrive pas, conservez la trace d’exécution et dépannez la collecte. Si un contrôle bloque le test avant l’événement attendu, consignez le résultat de prévention.

## Testez les contrôles d’identité

**L’hameçonnage adversary-in-the-middle (AiTM)** place un intermédiaire contrôlé par l’attaquant dans le flux de connexion. Le runbook fourni s’appuie sur ce scénario pour justifier une authentification plus forte. Pour le premier exercice d’identité, testez directement le comportement des règles avec votre compte sans privilèges.

Commencez par consigner une connexion légitime et ses détails d’authentification. Consultez la [référence Microsoft sur la détection des risques Entra](https://learn.microsoft.com/en-us/entra/id-protection/concept-identity-protection-risks) avant d’interpréter les signaux. Les prérequis et le traitement diffèrent selon le signal. Une nouvelle adresse IP ou une connexion échouée ne garantit pas une alerte AiTM.

**Les clés d’accès (FIDO2)** utilisent des identifiants liés au service légitime plutôt que des codes réutilisables saisis sur une page de connexion relayée. Activez un profil adapté pour le groupe pilote et inscrivez la méthode avant d’appliquer une règle. Consultez le [guide Microsoft de configuration des clés d’accès](https://learn.microsoft.com/en-us/entra/identity/authentication/how-to-authentication-passkeys-fido2) pour les authentificateurs pris en charge et leurs limites.

**Exercice Conditional Access (accès conditionnel) :** créez une règle ciblant uniquement le groupe pilote du laboratoire, excluez les comptes d’accès d’urgence et choisissez **Require authentication strength > Phishing-resistant MFA strength** (niveau d’authentification et MFA résistante à l’hameçonnage). Commencez en mode **Report-only (rapport uniquement)**, examinez l’impact, puis activez la règle. Adaptez l’[exemple de règle administrateur Microsoft](https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-admin-phish-resistant-mfa) à un petit groupe de test.

| Vérification | Preuve à recueillir |
|---|---|
| **Règle en mode Report-only (rapport uniquement)** | Enregistrement de connexion montrant l’évaluation de la règle proposée |
| **Règle appliquée, méthode plus faible** | Une nouvelle authentification exige une méthode plus forte avant l’accès |
| **Règle appliquée, clé d’accès inscrite** | Connexion réussie qui satisfait au niveau de sécurité exigé |

Utilisez une nouvelle authentification pour chaque comparaison et vérifiez les détails de la règle. Les sessions existantes compliquent les comparaisons. **Portée de la preuve :** cet exercice valide l’exigence d’authentification. Il ne prouve pas une protection universelle contre la compromission d’un terminal ou le vol d’une session existante.

## Rédigez des preuves pour votre portfolio

**Une entrée de portfolio utile** explique une décision de manière à ce qu’un autre analyste puisse l’évaluer. Ajoutez une brève description de l’architecture, les prérequis de collecte, la chronologie des événements et le raisonnement de votre réponse.

```text
Exercice :
Date et plage horaire UTC :
Périmètre du laboratoire et prérequis :
Déclencheur et signal attendu :
Alerte observée ou prévention :
Preuves et requêtes :
Identités et appareils concernés :
Conclusion et raisonnement :
Réponse et rétablissement :
Modification du contrôle et nouveau test :
Limites et suivi :
```

Remplacez chaque champ par vos propres observations. **Assainissez les exports :** avant de publier des captures ou des résultats de requête, retirez les identifiants, données de session, informations personnelles et identifiants superflus.

**Exemple de CV :** « J’ai créé un laboratoire de sécurité Microsoft, connecté les journaux d’identité à Sentinel, enquêté sur des alertes de test des terminaux et documenté la validation Conditional Access. » N’utilisez cette formulation qu’après avoir réalisé ces tâches. Placez-la dans les projets ou la formation pratique en indiquant les dates et le périmètre réels.

Un laboratoire montre une pratique individuelle. **Le travail dans un SOC de production** implique aussi l’impact métier, l’escalade, les engagements de service et la coordination avec d’autres équipes. Précisez les éléments pratiqués et ceux qui restent hors de votre expérience.

## Dépannage

| Symptôme | Première vérification |
|---|---|
| **Espace de travail absent de Defender** | Même tenant, Sentinel activé et rôles d’intégration requis |
| **SigninLogs absent ou vide** | Catégories de diagnostic, espace de destination, nouveaux événements et période |
| **Client absent d’Intune** | Prérequis et état de l’inscription |
| **Appareil visible sans télémétrie** | État réel d’intégration, santé du capteur et connectivité sortante |
| **Règle d’intégration non appliquée** | Périmètre d’attribution, plateforme et synchronisation récente |
| **Aucune alerte de risque d’identité** | Prérequis du signal et activité enregistrée, sans supposer une détection déterministe |
| **Accès autorisé de façon inattendue** | Mode Report-only (rapport uniquement), exclusions, périmètre de ressource et session existante |
| **Frais après arrêt** | État d’allocation et ressources facturées indépendamment du calcul |

**Ordre de dépannage :** prouvez d’abord que l’événement s’est produit, puis que la collecte a fonctionné, puis examinez la logique de détection. Notez chaque panne et sa correction dans les notes du projet.

## Mettez le laboratoire en pause ou supprimez-le

**La désallocation** libère l’allocation de calcul d’une VM. Arrêter seulement le système invité ne garantit pas cette désallocation. Vérifiez l’état d’alimentation affiché dans Azure et consultez la documentation Microsoft sur les [états et la facturation des VM](https://learn.microsoft.com/en-us/azure/virtual-machines/states-billing).

**Les ressources conservées** nécessitent aussi un suivi. Disques, instantanés, services réseau, rétention des journaux et abonnements utilisateur ont des cycles de vie distincts. Programmez un rappel avant l’expiration de chaque essai et vérifiez le prochain rapport d’utilisation après le nettoyage.

Avant de supprimer le groupe de ressources du laboratoire, exportez les preuves à conserver et inspectez-les. **La suppression d’un groupe de ressources détruit** les ressources qu’il contient. Les utilisateurs du tenant, règles Intune, règles Conditional Access, abonnements et paramètres de sécurité au niveau de l’abonnement peuvent nécessiter un nettoyage séparé.

## Étapes suivantes

**Terminez une enquête documentée** avant d’ajouter une autre charge. Ajoutez ensuite un serveur, un exercice d’identité ou une règle de détection avec une condition de test claire. Notez ce que le composant apporte et son coût.

Utilisez le [guide du laboratoire informatique](/it-career-playbook/getting-started-in-it/building-an-it-home-lab/) pour pratiquer l’infrastructure et le [guide du CV informatique](/it-career-playbook/getting-a-job-in-it/it-resume-writing-tips/) pour présenter votre travail. Gardez le prochain projet assez restreint pour expliquer la configuration, les preuves et le nettoyage.
