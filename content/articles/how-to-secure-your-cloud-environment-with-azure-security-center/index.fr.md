---
title: "Sécurisez votre environnement cloud avec Microsoft Defender for Cloud"
date: 2023-04-10
lastmod: 2026-11-20
toc: true
draft: false
description: "Protégez les charges de travail Azure avec Microsoft Defender for Cloud. Consultez les anciens termes d’Azure Security Center, ses recommandations, ses stratégies et les étapes de réponse."
tags: ["Azure", "Security Center", "sécurité cloud", "Azure Sentinel", "Azure Defender", "sécurité réseau", "gestion des identités", "sécurité des données", "détection des menaces", "réponse aux menaces", "MFA", "RBAC", "NSGs", "Azure Firewall", "WAF", "Azure AD", "Azure Information Protection", "Azure Storage Service Encryption", "Azure Disk Encryption"]
cover: "/img/cover/A_shield_icon_surrounded_by_cloud_symbols.webp"
coverAlt: "Un bouclier entouré de symboles de nuages représente un environnement cloud sécurisé. Le bouclier porte le logo Azure Security Center."
coverCaption: ""
---

**Comment sécuriser votre environnement cloud avec Azure Security Center**

Sécuriser votre environnement cloud protège les données, les applications et l’infrastructure de votre organisation contre les menaces. **Azure Security Center**, de Microsoft, vous aide à améliorer votre posture de sécurité et à repérer rapidement les risques potentiels dans Azure. Cet article explique comment protéger votre environnement avec Azure Security Center et présente des pratiques recommandées pour mettre en œuvre ses fonctions de sécurité. Il comprend aussi des détails techniques et des exemples pour vous aider à appliquer les étapes.

*Les noms des produits ont changé depuis la publication initiale de cet article. Microsoft Azure Security Center s’appelle désormais Microsoft Defender for Cloud. Azure Active Directory s’appelle désormais Microsoft Entra ID. Azure Sentinel s’appelle désormais Microsoft Sentinel. Azure Defender désigne les plans Defender et les protections des charges de travail dans Defender for Cloud. Les anciens noms sont conservés ci-dessous lorsqu’ils décrivent la terminologie de 2023.*

La [présentation actuelle de Defender for Cloud](https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-cloud-introduction) décrit une plateforme de protection des applications cloud natives, qui comprend la gestion de la posture de sécurité cloud, DevSecOps et la protection des charges de travail. La disponibilité des fonctionnalités et les licences dépendent du cloud, du type de ressource, de l’abonnement et du plan.

______

## Comprendre Azure Security Center

Azure Security Center est un **système unifié de gestion de la sécurité de l’infrastructure**. Il vous aide à repérer et à corriger les vulnérabilités potentielles de votre environnement cloud. Ses fonctions comprennent la détection des menaces, la gestion de la posture de sécurité et la gestion de la conformité.

**L’évaluation continue de la sécurité** et la **protection avancée contre les menaces** sont deux fonctions clés d’Azure Security Center. L’évaluation continue aide à repérer les problèmes de sécurité potentiels. La protection avancée aide à détecter les menaces et à y répondre.

______

## Mettre en œuvre les politiques de sécurité et les normes de conformité

Azure Security Center permet de mettre en œuvre et de gérer des politiques de sécurité dans l’ensemble de votre environnement cloud. Utilisez le service **Azure Policy** pour créer des politiques personnalisées, ou les politiques intégrées pour appliquer les pratiques recommandées et les normes de conformité. Vous pouvez aussi évaluer votre posture de sécurité par rapport à des normes du secteur telles que [NIST 800-53](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final), [CIS](https://www.cisecurity.org/) et [ISO 27001](https://www.iso.org/isoiec-27001-information-security.html).

Azure Security Center fournit aussi des fonctions de gestion de la conformité qui vous aident à suivre l’état de conformité de votre organisation selon des cadres réglementaires comme le [RGPD](https://gdpr.eu/), [HIPAA](https://www.hhs.gov/hipaa/index.html) et [PCI DSS](https://www.pcisecuritystandards.org/).

______

## Sécuriser vos ressources Azure

**Maintenir l’hygiène de sécurité des ressources** joue un rôle important dans la protection de votre environnement cloud. Azure Security Center fournit **Secure Score**, une mesure de la posture de sécurité qui vous aide à évaluer la protection globale de vos ressources. Appliquez les recommandations d’Azure Security Center pour améliorer ce score.

### Sécurité réseau

Les **Network Security Groups (NSGs)**, **Azure Firewall** et **Web Application Firewall (WAF)** contribuent à protéger votre environnement Azure contre les menaces. Ces outils contrôlent le trafic réseau entrant et sortant et réduisent les risques d’accès non autorisé et d’attaque.

#### Network Security Groups (NSGs)

Les NSG agissent comme des pare-feu virtuels pour vos ressources Azure. Vous définissez des règles qui autorisent ou refusent le trafic réseau vers ces ressources et depuis celles-ci. Voici un exemple de création d’un NSG avec des règles de trafic :

```azurecli
# Créez un Network Security Group
az network nsg create --name MyNSG --resource-group MyResourceGroup

# Ajoutez des règles pour autoriser ou refuser le trafic
az network nsg rule create --name MyNSGRule --nsg-name MyNSG --priority 100 --resource-group MyResourceGroup --access Allow --protocol Tcp --direction Inbound --source-address-prefixes '*' --source-port-ranges '*' --destination-address-prefixes '*' --destination-port-ranges '80'
```
Consultez la documentation officielle sur les [Network Security Groups](https://docs.microsoft.com/en-us/azure/virtual-network/security-overview).

L’exemple autorise le trafic TCP entrant sur le port 80 depuis toute source IPv4. En production, utilisez une plage source connue, un point de terminaison privé ou un chemin via un équilibreur de charge. Consultez la [présentation de la sécurité des NSG](https://learn.microsoft.com/en-us/azure/virtual-network/network-security-groups-overview) avant d’utiliser l’exemple.

#### Azure Firewall

Azure Firewall est un service géré de sécurité réseau dans le cloud qui protège les ressources Azure. Il offre le filtrage basé sur le renseignement sur les menaces, les catégories Web et la journalisation et l’analyse centralisées. Pour le configurer, suivez les [instructions de démarrage rapide](https://learn.microsoft.com/en-us/azure/firewall-manager/quick-firewall-policy-bicep).

#### Web Application Firewall (WAF)

Web Application Firewall (WAF) est une fonction d’**Azure Application Gateway**. Il protège les applications Web contre les attaques courantes, comme l’injection SQL et les scripts intersites. Intégrez WAF à vos applications existantes et configurez des règles personnalisées contre des types d’attaque précis.

Exemple de création d’un Application Gateway avec WAF activé :

```azurecli
# Créez une politique WAF
az network application-gateway waf-policy create --name MyWafPolicy --resource-group MyResourceGroup --location EastUS

# Créez un réseau virtuel et un sous-réseau
az network vnet create --name MyVNet --resource-group MyResourceGroup --location EastUS --address-prefix 10.0.0.0/16
az network vnet subnet create --name MySubnet --resource-group MyResourceGroup --vnet-name MyVNet --address-prefix 10.0.0.0/24

# Créez une adresse IP publique
az network public-ip create --name MyPublicIP --resource-group MyResourceGroup --location EastUS --sku Standard

# Créez un Application Gateway avec WAF activé
az network application-gateway create --name MyAppGateway --resource-group MyResourceGroup --location EastUS --vnet-name MyVNet --subnet MySubnet --public-ip-address MyPublicIP --http-settings-cookie-based-affinity Enabled --sku WAF_v2 --waf-policy MyWafPolicy

```
Consultez la documentation officielle sur [Web Application Firewall](https://docs.microsoft.com/en-us/azure/web-application-firewall/ag/ag-overview).

### Gestion des identités et des accès

**Microsoft Entra ID, anciennement Azure Active Directory (Azure AD),** est essentiel pour protéger votre environnement cloud. Defender for Cloud recommande des mesures de gestion des identités et des accès, comme l’activation de **Multi-Factor Authentication (MFA)**, la mise en œuvre de **Role-Based Access Control (RBAC)** et la surveillance des activités suspectes.

#### Multi-Factor Authentication (MFA)

MFA ajoute une couche de sécurité aux comptes Azure AD. Avant d’accorder l’accès, elle exige au moins deux formes de vérification. Pour activer MFA dans votre organisation, suivez le [guide pas à pas](https://docs.microsoft.com/en-us/azure/active-directory/authentication/tutorial-enable-azure-mfa) de Microsoft.

Exemple : activer MFA pour un utilisateur

```powershell
# Connectez-vous à Azure AD
Connect-AzureAD

# Activez MFA pour un utilisateur précis
$UserPrincipalName = "johndoe@example.com"
$StsUserObjectID = (Get-AzureADUser -Filter "UserPrincipalName eq '$UserPrincipalName'").ObjectId
$StrongAuthRequirements = @(@{"Location"=""; "SatisfactionFactor"="2"; "VerificationMethod"="1"};@{"Location"=""; "SatisfactionFactor"="2"; "VerificationMethod"="2"})
Set-AzureADUser -ObjectId $StsUserObjectID -StrongAuthenticationRequirements $StrongAuthRequirements
```
#### Role-Based Access Control (RBAC)

RBAC permet de définir des autorisations détaillées pour vos ressources Azure afin que chaque utilisateur ait le niveau d’accès approprié. Attribuez des rôles aux utilisateurs, aux groupes ou aux applications pour gérer leur accès aux ressources de l’organisation. Pour mettre en œuvre RBAC, suivez le [guide officiel](https://docs.microsoft.com/en-us/azure/role-based-access-control/overview) de Microsoft.

Exemple : attribuer un rôle à un utilisateur

```azurecli
# Attribuez le rôle Reader à un utilisateur
az role assignment create --assignee johndoe@example.com --role "Reader" --scope "/subscriptions/your_subscription_id/resourceGroups/your_resource_group"
```
#### Surveiller les activités suspectes

Azure AD fournit **Identity Protection** et **Conditional Access** pour surveiller les activités suspectes et y répondre. Identity Protection utilise l’apprentissage automatique pour détecter les anomalies et les tentatives de connexion à risque. Conditional Access permet de définir des politiques d’accès selon l’appareil, l’emplacement et le niveau de risque.

Pour configurer Azure AD Identity Protection, suivez le [guide officiel](https://learn.microsoft.com/en-us/azure/active-directory/identity-protection/concept-identity-protection-b2b) de Microsoft.

Exemple : créer une politique Conditional Access

```powershell
# Connectez-vous à Azure AD
Connect-AzureAD

# Créez une politique Conditional Access
$PolicyName = "BlockSignInFromUnknownLocations"
$PolicyDescription = "Bloquer les connexions des utilisateurs depuis des emplacements inconnus."
$PolicyState = "Enabled"
$Conditions = @{
    "SignInRiskLevels" = @("medium","high");
    "Locations" = @{
        "Included" = @();
        "Excluded" = @("AllTrusted")
    }
}
$GrantControls = @{
    "Operator" = "OR";
    "BuiltInControls" = @("Block")
}
New-AzureADMSConditionalAccessPolicy -DisplayName $PolicyName -State $PolicyState -Conditions $Conditions -GrantControls $GrantControls -Description $PolicyDescription

```
Consultez la documentation officielle sur [Azure AD Identity Protection](https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/overview) et [Conditional Access](https://learn.microsoft.com/en-us/azure/active-directory/conditional-access/overview).

### Sécurité des données

La protection des données dans le cloud est essentielle. Azure Security Center propose **Azure Information Protection**, **Azure Storage Service Encryption** et **Azure Disk Encryption**. Ces fonctions aident à chiffrer les données et à gérer les accès.

#### Azure Information Protection

**Azure Information Protection (AIP)** est un service cloud qui classe, étiquette et protège les documents et courriels sensibles. AIP comprend des étiquettes comme « Confidentiel » et « Personnel », que vous pouvez personnaliser selon les besoins de votre organisation. Vous pouvez aussi configurer l’application automatique d’étiquettes selon des règles prédéfinies. Pour commencer, suivez le [guide officiel](https://docs.microsoft.com/en-us/azure/information-protection/what-is-information-protection).

Exemple : créer une étiquette personnalisée

```powershell
# Connectez-vous au service AIP
Connect-AipService

# Créez une étiquette personnalisée avec des paramètres de protection
$LabelName = "Sensible - Usage interne uniquement"
$LabelDescription = "Cette étiquette applique le chiffrement et une politique d’accès réservés à l’usage interne."
$LabelProtectionSettings = @{
    "ContentExpirationDate" = (Get-Date).AddMonths(6).ToUniversalTime();
    "OfflineAccessInterval" = "P7D";
    "UserRights" = @("domain\GroupA=View", "domain\GroupB=View,Edit,Print")
}
New-AipServiceLabel -Name $LabelName -Description $LabelDescription -ProtectionSettings $LabelProtectionSettings
```
#### Azure Storage Service Encryption

**Azure Storage Service Encryption (SSE)** chiffre automatiquement les données au repos des comptes Azure Storage, notamment Blob, File, Table et Queue. SSE utilise des clés gérées par Azure ou par le client pour chiffrer les données au niveau du compte de stockage. Pour activer SSE, suivez le [guide pas à pas](https://docs.microsoft.com/en-us/azure/storage/common/storage-service-encryption) de Microsoft.

Azure Information Protection est un ancien nom de produit. La documentation actuelle de Microsoft sur la disponibilité des fonctions Sentinel le répertorie comme obsolète. Avant un nouveau déploiement d’étiquettes, consultez la documentation actuelle de Microsoft Purview Information Protection.

Exemple : activer SSE pour un compte de stockage

```azurecli
# Activez SSE avec des clés gérées par Azure
az storage account update --name mystorageaccount --resource-group myresourcegroup --encryption-services blob file
```
#### Azure Disk Encryption

**Azure Disk Encryption** protège les disques des machines virtuelles en les chiffrant avec BitLocker (Windows) ou dm-crypt (Linux). Azure Key Vault protège les clés et secrets de chiffrement. Pour activer Azure Disk Encryption, suivez le [guide officiel](https://learn.microsoft.com/en-us/azure/virtual-machines/disk-encryption-overview) de Microsoft.

Exemple : activer Azure Disk Encryption pour une machine virtuelle

```azurecli
# Activez Azure Disk Encryption pour une machine virtuelle Windows
az vm encryption enable --resource-group myResourceGroup --name myVM --disk-encryption-keyvault myKeyVault
```
Consultez la documentation officielle sur [Azure Information Protection](https://docs.microsoft.com/en-us/azure/information-protection/what-is-information-protection), [Azure Storage Service Encryption](https://docs.microsoft.com/en-us/azure/storage/common/storage-service-encryption) et [Azure Disk Encryption](https://learn.microsoft.com/en-us/azure/virtual-machines/disk-encryption-overview).
______

## Détecter les menaces et y répondre

Azure Security Center détecte les menaces potentielles et envoie des alertes. L’intégration avec **Azure Sentinel** permet de surveiller, d’enquêter et de traiter les incidents de sécurité dans l’ensemble de l’environnement.

### Détection des menaces

Azure Security Center utilise **Azure Defender** pour détecter les menaces de sécurité potentielles. Azure Defender surveille les ressources à la recherche d’indicateurs de compromission et fournit des alertes et des recommandations pour faciliter la réponse. Pour activer Azure Defender, suivez le [guide officiel](https://docs.microsoft.com/en-us/azure/security-center/defender-for-cloud-enable).

Exemple : activer Azure Defender pour un abonnement

```azurecli
# Activez Azure Defender pour un abonnement
az security auto-provisioning-setting update --name default --auto-provision on
```
### Réponse aux menaces
Lorsqu’une menace est détectée, réagissez rapidement et efficacement. La gestion **Security Incident** d’Azure Security Center vous aide à enquêter sur les incidents et à y répondre. Vous pouvez aussi intégrer **Azure Sentinel** pour créer des scénarios automatisés et coordonner la réponse. Consultez la **documentation officielle** sur l’intégration d’Azure Security Center avec Azure Sentinel.

Exemple : créer un scénario Logic App pour Azure Sentinel
```azurecli
# Créez un groupe de ressources
az group create --name MyResourceGroup --location EastUS

# Créez une Logic App
az logic workflow create --resource-group MyResourceGroup --location EastUS --name MyPlaybook --definition @playbook-definition.json
```
Le fichier `playbook-definition.json` doit contenir la définition du scénario Logic App. Consultez les exemples Azure Sentinel dans le [dépôt Azure-Sentinel sur GitHub](https://github.com/Azure/Azure-Sentinel/tree/master/Playbooks).

Combinez la détection des menaces d’Azure Security Center avec Azure Sentinel pour repérer les menaces dans Azure et y répondre. Consultez la documentation officielle sur [Azure Defender](https://learn.microsoft.com/en-us/azure/defender-for-cloud/enable-enhanced-security) et [Azure Sentinel](https://docs.microsoft.com/en-us/azure/sentinel/overview).

L’intégration actuelle envoie les alertes Defender for Cloud à Microsoft Sentinel via le [connecteur Defender for Cloud](https://learn.microsoft.com/en-us/azure/sentinel/connect-defender-for-cloud). Avant de dépendre de l’automatisation, validez le connecteur, les règles de collecte des données, les règles analytiques et le processus de gestion des incidents dans le portail Defender ou Azure.
______

## Surveillance et rapports

La surveillance et les rapports aident à maintenir un environnement cloud sécurisé. Azure Security Center fournit des outils comme le **tableau de bord de sécurité**, les **alertes de sécurité** et les **rapports de conformité**.

### Tableau de bord de sécurité

Le Security Dashboard d’Azure Security Center présente une vue d’ensemble de la posture de sécurité. Il affiche Secure Score, les recommandations et les alertes actives. Il indique aussi l’état de conformité et permet de suivre l’évolution dans le temps.

### Alertes de sécurité

Azure Security Center génère des alertes lorsqu’il détecte des menaces potentielles. Elles décrivent la menace et recommandent des mesures pour réduire le risque. Configurez les notifications par courriel ou SMS, ou intégrez le service à [Slack](https://slack.com/) ou [Microsoft Teams](https://www.microsoft.com/en-us/microsoft-teams/group-chat-software).

### Rapports de conformité

Azure Security Center génère des rapports pour des cadres réglementaires comme le RGPD, HIPAA et PCI DSS. Utilisez-les pour suivre la conformité de l’organisation et repérer les domaines à améliorer.

______

## Pratiques recommandées pour Azure Security Center

Pour tirer parti d’Azure Security Center, appliquez les pratiques suivantes :

1. **Activez Azure Security Center pour tous les abonnements** : vérifiez que chaque abonnement Azure est protégé.
2. **Vérifiez régulièrement Secure Score** : suivez la posture de sécurité globale et repérez les points à améliorer.
3. **Appliquez les recommandations de sécurité** : améliorez la posture et réduisez les risques en suivant les recommandations d’Azure Security Center.
4. **Surveillez les alertes de sécurité** : examinez les alertes et répondez-y pour réduire les menaces potentielles.
5. **Tenez à jour les exigences de conformité** : révisez et mettez à jour les politiques pour respecter les cadres réglementaires actuels.

## Flux de travail actuel de Defender for Cloud

Pour un déploiement actuel, suivez cette séquence. Les anciens noms des sections aident à trouver les informations historiques, mais le portail et la documentation utilisent la terminologie Defender for Cloud.

1. **Inventoriez les abonnements et les connecteurs.** Consignez les abonnements Azure, les connecteurs AWS ou GCP, les projets DevOps et les ressources critiques.
2. **Activez les plans Defender requis.** Choisissez les plans selon les charges de travail et confirmez les licences avant de les activer dans les abonnements de production.
3. **Examinez Cloud Secure Score et les recommandations.** Priorisez l’exposition à Internet, les risques d’identité, les vulnérabilités exploitables et les journaux manquants. Le score ne prouve pas une conformité complète.
4. **Configurez les contrôles Microsoft Entra.** Exigez une MFA résistante à l’hameçonnage pour les comptes importants, utilisez RBAC avec le minimum de privilèges et vérifiez les accès privilégiés.
5. **Envoyez les alertes à Microsoft Sentinel.** Confirmez leur réception, les règles analytiques, les responsables, l’automatisation des réponses et la durée de conservation.
6. **Vérifiez à nouveau après les changements.** Réexaminez les recommandations après les correctifs, les changements d’architecture, l’ajout de connecteurs ou la modification des plans.

## Liste de vérification pratique

- **Identité :** supprimez les anciens comptes, réduisez les accès permanents d’administrateur et examinez les exceptions Conditional Access.
- **Réseau :** fermez les ports d’administration publics, réduisez les plages sources des NSG et vérifiez que les journaux du pare-feu et de WAF atteignent l’espace de surveillance.
- **Données :** classez les dépôts de données sensibles, confirmez le chiffrement et la propriété des clés, puis testez la restauration des sauvegardes.
- **Détection :** confirmez la gravité des alertes, le routage des notifications, les responsables des incidents et les scénarios de réponse.
- **Gouvernance :** désignez un responsable, une date d’expiration pour les exceptions et les preuves requises pour chaque initiative de politique.

______

## Références

- [Documentation Azure Security Center](https://docs.microsoft.com/en-us/azure/security-center/)
- [Service Azure Policy](https://docs.microsoft.com/en-us/azure/governance/policy/)
- [NIST 800-53](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final)
- [CIS](https://www.cisecurity.org/)
- [ISO 27001](https://www.iso.org/isoiec-27001-information-security.html)
- [RGPD](https://gdpr.eu/)
- [HIPAA](https://www.hhs.gov/hipaa/index.html)
- [PCI DSS](https://www.pcisecuritystandards.org/)
