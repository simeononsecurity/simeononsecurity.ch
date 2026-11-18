---
title: "Sécuriser votre environnement cloud avec Microsoft Defender for Cloud"
date: 2023-04-10
lastmod: 2026-11-14
toc: true
draft: false
description: "Sécurisez les charges de travail Azure avec Microsoft Defender for Cloud. Retrouvez les anciens termes d’Azure Security Center, les recommandations, les stratégies et les étapes de réponse."
tags: ["Azure", "Security Center", "sécurité du cloud", "Azure Sentinel", "Azure Defender", "sécurité réseau", "gestion des identités", "sécurité des données", "détection des menaces", "réponse aux menaces", "MFA", "RBAC", "NSGs", "Azure Firewall", "WAF", "Azure AD", "Azure Information Protection", "Azure Storage Service Encryption", "Azure Disk Encryption"]
cover: "/img/cover/A_shield_icon_surrounded_by_cloud_symbols.webp"
coverAlt: "Un bouclier entouré de symboles de nuage représente un environnement cloud sécurisé. Le bouclier porte le logo Azure Security Center."
coverCaption: ""
---
```azurecli
# Créer un groupe de sécurité réseau
az network nsg create --name MyNSG --resource-group MyResourceGroup

# Ajouter des règles pour autoriser ou bloquer le trafic
az network nsg rule create --name MyNSGRule --nsg-name MyNSG --priority 100 --resource-group MyResourceGroup --access Allow --protocol Tcp --direction Inbound --source-address-prefixes '*' --source-port-ranges '*' --destination-address-prefixes '*' --destination-port-ranges '80'
```
```azurecli
# Créer une stratégie WAF
az network application-gateway waf-policy create --name MyWafPolicy --resource-group MyResourceGroup --location EastUS

# Créer un réseau virtuel et un sous-réseau
az network vnet create --name MyVNet --resource-group MyResourceGroup --location EastUS --address-prefix 10.0.0.0/16
az network vnet subnet create --name MySubnet --resource-group MyResourceGroup --vnet-name MyVNet --address-prefix 10.0.0.0/24

# Créer une adresse IP publique
az network public-ip create --name MyPublicIP --resource-group MyResourceGroup --location EastUS --sku Standard

# Créer une passerelle Application Gateway avec WAF activé
az network application-gateway create --name MyAppGateway --resource-group MyResourceGroup --location EastUS --vnet-name MyVNet --subnet MySubnet --public-ip-address MyPublicIP --http-settings-cookie-based-affinity Enabled --sku WAF_v2 --waf-policy MyWafPolicy

```
```powershell
# Se connecter à Azure AD
Connect-AzureAD

# Activer la MFA pour un utilisateur donné
$UserPrincipalName = "johndoe@example.com"
$StsUserObjectID = (Get-AzureADUser -Filter "UserPrincipalName eq '$UserPrincipalName'").ObjectId
$StrongAuthRequirements = @(@{"Location"=""; "SatisfactionFactor"="2"; "VerificationMethod"="1"};@{"Location"=""; "SatisfactionFactor"="2"; "VerificationMethod"="2"})
Set-AzureADUser -ObjectId $StsUserObjectID -StrongAuthenticationRequirements $StrongAuthRequirements
```
```azurecli
# Attribuer le rôle Reader à un utilisateur
az role assignment create --assignee johndoe@example.com --role "Reader" --scope "/subscriptions/your_subscription_id/resourceGroups/your_resource_group"
```
```powershell
# Se connecter à Azure AD
Connect-AzureAD

# Créer une stratégie d’accès conditionnel
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
```powershell
# Se connecter au service AIP
Connect-AipService

# Créer une étiquette personnalisée avec des paramètres de protection
$LabelName = "Sensitive - Internal Use Only"
$LabelDescription = "Cette étiquette applique le chiffrement et une stratégie d’accès réservés à un usage interne."
$LabelProtectionSettings = @{
"ContentExpirationDate" = (Get-Date).AddMonths(6).ToUniversalTime();
"OfflineAccessInterval" = "P7D";
"UserRights" = @("domain\GroupA=View", "domain\GroupB=View,Edit,Print")
}
New-AipServiceLabel -Name $LabelName -Description $LabelDescription -ProtectionSettings $LabelProtectionSettings
```
```azurecli
# Activer SSE avec des clés gérées par Azure
az storage account update --name mystorageaccount --resource-group myresourcegroup --encryption-services blob file
```
```azurecli
# Activer Azure Disk Encryption pour une machine virtuelle Windows
az vm encryption enable --resource-group myResourceGroup --name myVM --disk-encryption-keyvault myKeyVault
```
```azurecli
# Activer Azure Defender pour un abonnement
az security auto-provisioning-setting update --name default --auto-provision on
```
```azurecli
# Créer un groupe de ressources
az group create --name MyResourceGroup --location EastUS

# Créer une Logic App
az logic workflow create --resource-group MyResourceGroup --location EastUS --name MyPlaybook --definition @playbook-definition.json
```

**Comment sécuriser votre environnement cloud avec Azure Security Center** La sécurisation de votre environnement cloud est essentielle pour protéger les données, les applications et l'infrastructure de votre organisation contre les menaces. **Azure Security Center** de Microsoft est un outil puissant qui vous aide à renforcer votre posture de sécurité et à identifier rapidement les risques potentiels dans votre environnement Azure. Dans cet article, nous expliquerons comment sécuriser votre environnement cloud à l'aide d'Azure Security Center et couvrirons les meilleures pratiques pour la mise en œuvre de diverses fonctionnalités de sécurité. De plus, dans cet article, nous aborderons plus de détails techniques et d'exemples pour vous aider à mieux comprendre comment sécuriser votre environnement cloud à l'aide d'Azure Security Center.
______

*Les noms des produits ont changé depuis la publication originale. Microsoft Azure Security Center s’appelle désormais Microsoft Defender for Cloud. Azure Active Directory s’appelle désormais Microsoft Entra ID. Azure Sentinel s’appelle désormais Microsoft Sentinel. Azure Defender désigne les plans Defender et les protections de charges de travail dans Defender for Cloud. Les anciens noms sont conservés lorsqu’ils décrivent le contexte de 2023.*

La [présentation actuelle de Defender for Cloud](https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-cloud-introduction) décrit une plateforme de protection des applications cloud natives, avec gestion de la posture de sécurité cloud, DevSecOps et protection des charges de travail cloud. La disponibilité et les licences dépendent du cloud, du type de ressource, de l’abonnement et du plan.

## Comprendre Azure Security Center

Azure Security Center est un **système unifié de gestion de la sécurité de l'infrastructure** qui vous aide à identifier et à résoudre les vulnérabilités potentielles dans votre environnement cloud. Il offre plusieurs fonctionnalités, telles que la détection des menaces, la gestion de la posture de sécurité et la gestion de la conformité, pour garantir que votre environnement Azure est toujours sécurisé. **Évaluation continue de la sécurité** et **Protection avancée contre les menaces** sont deux fonctionnalités clés d'Azure Security Center. L'évaluation continue de la sécurité vous aide à identifier les problèmes de sécurité potentiels dans votre environnement, tandis qu'Advanced Threat Protection vous aide à détecter et à répondre aux menaces potentielles.
______

## Mise en œuvre des politiques de sécurité et des normes de conformité

Azure Security Center vous permet d'implémenter et de gérer des politiques de sécurité dans votre environnement cloud. Vous pouvez utiliser le service **Azure Policy** pour créer des politiques de sécurité personnalisées ou utiliser des politiques intégrées pour appliquer les bonnes pratiques et les normes de conformité. Vous pouvez également évaluer votre posture de sécurité par rapport aux normes de l'industrie telles que [NIST 800-53](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final), [CIS](https://www.cisecurity.org/) et [ISO 27001](https://www.iso.org/isoiec-27001-information-security.html). Azure Security Center fournit également des fonctionnalités de gestion de la conformité, vous permettant de suivre l'état de conformité de votre organisation par rapport à divers cadres réglementaires, tels que [RGPD](https://gdpr.eu/), [HIPAA ](https://www.hhs.gov/hipaa/index.html) et [PCI DSS](https://www.pcisecuritystandards.org/).
______

## Sécuriser vos ressources Azure

**L'hygiène de la sécurité des ressources** est un aspect important de la sécurisation de votre environnement cloud. Azure Security Center fournit **Secure Score**, une mesure de votre état de sécurité, pour vous aider à comprendre la sécurité globale de vos ressources. Vous pouvez améliorer votre score de sécurité en suivant les recommandations fournies par Azure Security Center.

### Sécurité Internet

La mise en œuvre de mesures de sécurité réseau améliorées, telles que les **groupes de sécurité réseau (NSG)**, le **pare-feu Azure** et le **pare-feu d'application Web (WAF)* *, est essentielle pour protéger votre environnement Azure contre les menaces potentielles. Ces outils vous permettent d'accéder à contrôler le trafic réseau entrant et sortant, en protégeant vos ressources contre les non autorisés et les attaques potentielles.

#### Groupes de sécurité réseau (NSG)

Les NSG concernés comme un pare-feu virtuel pour vos ressources Azure, vous permettant de définir des règles qui autorisent ou refusent le trafic réseau vers et depuis vos ressources. Par exemple, vous pouvez créer un NSG avec des règles pour autoriser ou refuser un trafic spécifique : En savoir plus sur les [groupes de sécurité réseau](https://docs.microsoft.com/en-us/azure/virtual-network/security-overview) En production, utilisez une plage source connue plutôt que toutes les sources IPv4. Consultez la [présentation de la sécurité des NSG](https://learn.microsoft.com/en-us/azure/virtual-network/network-security-groups-overview). dans la documentation officielle.

#### Pare-feu Azur

Le pare-feu Azure est un service de sécurité réseau géré basé sur le cloud qui protège vos ressources Azure. Il fournit des fonctionnalités avancées telles que le filtrage basé sur les renseignements sur les menaces, les catégories Web et la journalisation et l'analyse centralisée. Pour configurer le pare-feu Azure, vous pouvez suivre ces [instructions de démarrage rapide](https://learn.microsoft.com/en-us/azure/firewall-manager/quick-firewall-policy-bicep).

#### Pare-feu d'application Web (WAF)

Le pare-feu d'application Web (WAF) est une fonctionnalité de **Azure Application Gateway** qui protège vos applications Web contre les exploits Web courants tels que l' injection SQL, les scripts intersites et d'autres menaces. WAF peut être facilement intégré à vos applications Web existantes et vous pouvez configurer des règles personnalisées pour vous protéger contre des modèles d'attaque spécifiques. Voici un exemple de création d'Application Gateway avec WAF activé : En savoir plus sur [Web Application Firewall](https://docs.microsoft.com/en-us/azure/web-application-firewall/ag/ag-overview) dans la documentation officielle.

### Gestion des identités et des accès

**Azure Active Directory (Azure AD)** est un composant essentiel de la sécurisation de votre environnement cloud. Azure Security Center fournit des recommandations pour améliorer la gestion des identités et des accès, telles que l'activation de l'**authentification multifacteur (MFA)**, la mise en œuvre du **contrôle d'accès basé sur les rôles ( RBAC)** et la surveillance des activités suspectes.

#### Authentification multifacteur (MFA)

MFA ajoute une couche de sécurité supplémentaire à vos comptes Azure AD en demandant aux utilisateurs de fournir au moins deux formes de vérification avant d'accorder l'accès. Vous pouvez activer MFA pour votre organisation en suivant le [guide pas à pas](https://docs.microsoft.com/en-us/azure/active-directory/authentication/tutorial-enable-azure-mfa) fourni par Microsoft . Exemple : Activer MFA pour un utilisateur

#### Contrôle d'accès basé sur les rôles (RBAC)

RBAC vous permet de définir des autorisations granulaires pour vos ressources Azure, garantissant que les utilisateurs disposent du niveau d'accès approprié. Vous pouvez attribuer des rôles à des utilisateurs, des groupes ou des applications pour gérer leur accès aux ressources au sein de votre organisation. Pour implémenter RBAC, suivez le [guide officiel](https://docs.microsoft.com/en-us/azure/role-based-access-control/overview) de Microsoft. Exemple : Attribuer un rôle à un utilisateur

#### La surveillance des activités suspectes

Azure AD fournit des fonctionnalités telles que **Identity Protection** et **Conditional Access** qui vous permettent de surveiller et de répondre aux activités suspectes. Identity Protection use des algorithmes d'apprentissage automatique pour détecter les anomalies et les tentatives de connexion risquées, tandis que l'accès conditionnel vous permet de définir des politiques qui contrôlent l'accès en fonction de facteurs tels que l'appareil, l'emplacement et le niveau de risque. Pour configurer Azure AD Identity Protection, suivez le [guide officiel](https://learn.microsoft.com/en-us/azure/active-directory/identity-protection/concept-identity-protection-b2b) de Microsoft. Exemple : créer une stratégie d'accès conditionnel En savoir plus sur [Azure AD Identity Protection](https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/overview) et [Conditional Access ](https://learn.microsoft.com/en-us/azure/active-directory/conditional-access/overview) dans la documentation officielle.

### Sécurité des données

La protection de vos données dans le cloud est cruciale. Azure Security Center offre plusieurs fonctionnalités de sécurité des données, telles que **Azure Information Protection**, **Azure Storage Service Encryption** et **Azure Disk Encryption**. Ces fonctionnalités vous permettent de chiffrer et de gérer l'accès à vos données, garantissant ainsi la sécurité des informations sensibles.

#### Protection des informations Azure

**Azure Information Protection (AIP)** est une solution basée sur le cloud qui vous aide à classer, étiqueter et protéger les documents et e-mails sensibles. AIP fournit un ensemble d'étiquettes intégrées, telles que "Confidentiel" et "Personnel", qui peuvent être personnalisées en fonction des besoins de votre organisation. Vous pouvez également configurer AIP pour appliquer automatiquement des étiquettes en fonction de règles prédéfinies. Pour démarrer avec AIP, suivez le [guide officiel](https://docs.microsoft.com/en-us/azure/information-protection/what-is-information-protection) Azure Information Protection est un ancien nom de produit et la documentation Sentinel actuelle le signale comme obsolète. Consultez la documentation Microsoft Purview Information Protection avant tout nouveau déploiement.. Exemple : Création d'une étiquette personnalisée

#### Chiffrement du service de stockage Azure

**Azure Storage Service Encryption (SSE**) chiffre automatiquement vos données au dépôt dans les comptes de stockage Azure, y compris le stockage Blob, File, Table et file d'attente. SSE utilise des clés gérées par Azure ou des clés gérées par le client pour assurer le chiffrement au niveau du compte de stockage. Pour activer SSE, suivez le [guide pas à pas](https://docs.microsoft.com/en-us/azure/storage/common/storage-service-encryption) fourni par Microsoft. Exemple : Activer SSE pour un compte de stockage

#### Chiffrement de disque Azure

**Azure Disk Encryption** vous aide à protéger les disques des machines virtuelles en les chiffrant avec BitLocker (Windows) ou dm-crypt (Linux). Les clés de chiffrement et les secrets sont protégés par Azure Key Vault, garantissant que vos données sont sécurisées au repos. Pour activer Azure Disk Encryption, suivez le [guide officiel](https://learn.microsoft.com/en-us/azure/virtual-machines/disk-encryption-overview) de Microsoft. Exemple : Activer Azure Disk Encryption pour une machine virtuelle En savoir plus sur [Azure Information Protection](https://docs.microsoft.com/en-us/azure/information-protection/what-is-information-protection), [ Azure Storage Service Encryption](https://docs.microsoft.com/en-us/azure/storage/common/storage-service-encryption) et [Azure Disk Encryption](https://learn.microsoft.com/en-us/azure/virtual-machines/disk-encryption-overview) dans la documentation officielle.
______

## Détecter et répondre aux menaces

Azure Security Center utilise des fonctionnalités avancées de détection des menaces pour identifier et vous alerter des menaces potentielles. En vous intégrant à **Azure Sentinel**, vous pouvez surveiller, enquêter et répondre aux incidents de sécurité dans l'ensemble de votre environnement.

### Détection des menaces

Azure Security Center use **Azure Defender**, un ensemble d'options avancées de détection des menaces, pour identifier les menaces de sécurité potentielles. Azure Defender surveille vos ressources à la recherche d'indicateurs de compromission et fournit des alertes et des recommandations pour vous aider à répondre aux menaces potentielles. Pour activer Azure Defender, suivez le [guide officiel](https://docs.microsoft.com/en-us/azure/security-center/defender-for-cloud-enable). Exemple : Activer Azure Defender pour un abonnement

### Réponse aux menaces

Lorsqu'une menace est détectée, il est essentiel de réagir rapidement et efficacement. Azure Security Center fournit la gestion des **incidents de sécurité**, qui vous aide à enquêter sur les incidents de sécurité et à y répondre. Vous pouvez également intégrer **Azure Sentinel** pour créer des playbooks automatisés et orchestrer votre réponse aux incidents de sécurité. En savoir plus sur l'intégration d'Azure Security Center avec Azure Sentinel dans la **documentation officielle**. Exemple : Créer un playbook d'application logique pour Azure Sentinel Le fichier `playbook-definition.json` doit contenir la définition du playbook de l'application logique. Vous pouvez trouver des exemples de playbooks pour Azure Sentinel dans le [référentiel Azure-Sentinel GitHub](https://github.com/Azure/Azure-Sentinel/tree/master/Playbooks). En tirant parti des capacités de détection des menaces d'Azure Security Center et en s'intégrant à Azure Sentinel, vous pouvez créer une stratégie de sécurité robuste pour détecter et répondre aux menaces dans votre environnement Azure. En savoir plus sur [Azure Defender](https://learn.microsoft.com/en-us/azure/defender-for-cloud/enable-enhanced-security) et [Azure Sentinel](https://docs.microsoft.com/en-us/azure/sentinel/overview) dans la documentation officielle.
______

Le [connecteur Defender for Cloud](https://learn.microsoft.com/en-us/azure/sentinel/connect-defender-for-cloud) transmet les alertes à Microsoft Sentinel. Vérifiez le connecteur, les règles de collecte et d’analyse des données ainsi que le processus des incidents avant de compter sur l’automatisation.

## Surveillance et rapports

La surveillance et la création de rapports sont des éléments essentiels du maintien d'un environnement cloud sécurisé. Azure Security Center fournit plusieurs outils de surveillance et de création de rapports, tels que **Tableau de bord de sécurité**, **Alertes de sécurité** et **Rapports de conformité**.

### Tableau de bord de sécurité

Le tableau de bord de sécurité dans Azure Security Center fournit une vue d'ensemble complète de votre posture de sécurité. Il affiche votre score de sécurité, des recommandations de sécurité et des alertes de sécurité actives. Le tableau de bord fournit également des informations sur votre statut de conformité et vous permet de suivre vos progrès au fil du temps.

### Alertes de sécurité

Azure Security Center génère des alertes de sécurité lorsque des menaces potentielles sont détectées. Ces alertes fournissent des informations détaillées sur la menace, ainsi que des recommandations pour atténuer le risque. Vous pouvez configurer Azure Security Center pour envoyer des notifications par e-mail, SMS ou intégrer des outils tiers tels que [Slack](https://slack.com/) ou [Microsoft Teams](https://www.microsoft.com/en-us/microsoft-teams/group-chat-software).

### Rapports de conformité

Azure Security Center vous permet de produire des rapports de conformité pour divers cadres réglementaires, tels que GDPR, HIPAA et PCI DSS. Ces rapports vous aident à suivre l'état de conformité de votre organisation et à identifier les domaines nécessitant des améliorations.
______

## Meilleures pratiques pour Azure Security Center

Pour tirer le meilleur parti d'Azure Security Center, envisagez de mettre en œuvre les bonnes pratiques suivantes :
1. **Activez Azure Security Center sur tous vos abonnements** : S'assurer que tous vos abonnements Azure sont protégés par Azure Security Center est essentiel pour maintenir un environnement cloud sécurisé.
2. **Examinez régulièrement votre score de sécurité** : la surveillance de votre score de sécurité vous aide à comprendre votre état de sécurité global et à identifier les domaines qui évoluent des améliorations.
3. **Mettre en œuvre les recommandations de sécurité** : le respect des recommandations de sécurité fournies par Azure Security Center vous aide à améliorer votre sécurité et à réduire les risques potentiels.
4. **Surveillez les alertes de sécurité** : examinez régulièrement les alertes de sécurité et répondez-y afin d'atténuer les menaces potentielles et de maintenir un environnement sécurisé.
5. **Restez à jour avec les exigences de conformité** : spécifiez-vous que votre organisation reste conforme aux derniers cadres réglementaires en examinant et en mettant à jour régulièrement vos politiques de conformité.
______

## Parcours actuel dans Defender for Cloud

Pour un déploiement actuel, suivez cette séquence. Les noms des sections d’origine restent utiles pour les recherches historiques, mais le portail et la documentation emploient la terminologie Defender for Cloud.

1. **Inventoriez les abonnements et les connecteurs.** Recensez les abonnements Azure, les connecteurs AWS ou GCP, les projets DevOps et les ressources critiques.
2. **Activez les plans Defender nécessaires.** Choisissez les plans selon les charges de travail et vérifiez les licences avant de les activer sur les abonnements de production.
3. **Examinez le Secure Score cloud et les recommandations.** Priorisez l’exposition à Internet, les risques liés aux identités, les vulnérabilités exploitables et l’absence de journaux. Un score ne prouve pas une conformité complète.
4. **Configurez les contrôles Microsoft Entra.** Exigez une MFA résistante au hameçonnage pour les comptes sensibles, appliquez le principe du moindre privilège avec RBAC et examinez les accès privilégiés.
5. **Envoyez les alertes à Microsoft Sentinel.** Vérifiez l’ingestion des alertes, les règles analytiques, les responsabilités, l’automatisation des réponses et la conservation.
6. **Revérifiez après les changements.** Examinez les recommandations après les correctifs, les changements d’architecture, l’ajout de connecteurs ou la modification des plans.

## Liste de vérification pratique

- **Identité :** supprimez les comptes obsolètes, réduisez les droits d’administrateur permanents et examinez les exclusions de l’accès conditionnel.
- **Réseau :** supprimez les ports de gestion publics, réduisez les plages source des NSG et vérifiez que les journaux du pare-feu et du WAF arrivent dans l’espace de supervision.
- **Données :** classez les stockages sensibles, vérifiez le chiffrement et la propriété des clés, puis testez la restauration des sauvegardes.
- **Détection :** vérifiez la gravité des alertes, leur acheminement, la responsabilité des incidents et les playbooks de réponse.
- **Gouvernance :** attribuez à chaque initiative de stratégie un responsable, une date d’expiration des exceptions et des preuves pour le cadre exigé.

## Les références
- [Documentation du Centre de sécurité Azure](https://docs.microsoft.com/en-us/azure/security-center/)
- [Service de politique Azure](https://docs.microsoft.com/en-us/azure/governance/policy/)
- [NIST 800-53](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final)
- [CIS](https://www.cisecurity.org/)
- [ISO 27001](https://www.iso.org/isoiec-27001-information-security.html)
- [RGPD](https://gdpr.eu/)
- [HIPAA](https://www.hhs.gov/hipaa/index.html)
- [PCI DSS](https://www.pcisecuritystandards.org/)
