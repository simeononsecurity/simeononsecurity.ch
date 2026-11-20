---
title: "Uw cloudomgeving beveiligen met Microsoft Defender for Cloud"
date: 2023-04-10
lastmod: 2026-11-20
toc: true
draft: false
description: "Beveilig Azure-workloads met Microsoft Defender for Cloud. Bekijk historische Azure Security Center-termen, aanbevelingen, beleidsregels en responsstappen."
tags: ["Azure", "Security Center", "cloudbeveiliging", "Azure Sentinel", "Azure Defender", "netwerkbeveiliging", "identiteitsbeheer", "gegevensbeveiliging", "dreigingsdetectie", "respons op dreigingen", "MFA", "RBAC", "NSGs", "Azure Firewall", "WAF", "Azure AD", "Azure Information Protection", "Azure Storage Service Encryption", "Azure Disk Encryption"]
cover: "/img/cover/A_shield_icon_surrounded_by_cloud_symbols.webp"
coverAlt: "Een schild tussen cloudsymbolen staat voor een veilige cloudomgeving. Op het schild staat het Azure Security Center-logo."
coverCaption: ""
---

**Hoe beveiligt u uw cloudomgeving met Azure Security Center**?

Het beveiligen van uw cloudomgeving is essentieel om de gegevens, toepassingen en infrastructuur van uw organisatie te beschermen tegen bedreigingen. Microsoft's **Azure Security Center** is een krachtig hulpmiddel waarmee u uw beveiligingshouding kunt versterken en snel potentiële risico's in uw Azure-omgeving kunt identificeren. In dit artikel bespreken we hoe u uw cloudomgeving kunt beveiligen met behulp van Azure Security Center, en behandelen we de aanbevolen werkwijzen voor het implementeren van verschillende beveiligingsfuncties. Daarnaast duiken we in dit artikel in meer technische details en voorbeelden, zodat u beter begrijpt hoe u uw cloudomgeving kunt beveiligen met behulp van Azure Security Center.

______

*Productnamen zijn sinds de oorspronkelijke publicatie gewijzigd. Microsoft Azure Security Center heet nu Microsoft Defender for Cloud. Azure Active Directory heet nu Microsoft Entra ID. Azure Sentinel heet nu Microsoft Sentinel. Azure Defender verwijst naar Defender-plannen en workloadbeveiliging binnen Defender for Cloud. De oude namen blijven staan waar ze de terminologie uit 2023 beschrijven.*

Het huidige [overzicht van Defender for Cloud](https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-cloud-introduction) beschrijft een Cloud Native Application Protection Platform met beheer van de cloudbeveiligingsstatus, DevSecOps en cloudworkloadbeveiliging. Beschikbaarheid en licenties hangen af van de cloud, het resourcetype, het abonnement en het plan.

## Inzicht in Azure Beveiligingscentrum

Azure Security Center is een **uniform beheersysteem voor infrastructuurbeveiliging** waarmee u potentiële kwetsbaarheden in uw cloudomgeving kunt identificeren en aanpakken. Het biedt verschillende functies, zoals dreigingsdetectie, beveiligingspostuurbeheer en compliancebeheer, om ervoor te zorgen dat uw Azure-omgeving altijd veilig is.

**Continuous Security Assessment** en **Advanced Threat Protection** zijn twee belangrijke functies van Azure Security Center. Met Continuous Security Assessment kunt u potentiële beveiligingsproblemen in uw omgeving identificeren, terwijl Advanced Threat Protection u helpt bij het detecteren van en reageren op potentiële bedreigingen.

______

## Beveiligingsbeleid en nalevingsnormen implementeren

Met Azure Security Center kunt u beveiligingsbeleid implementeren en beheren in uw cloudomgeving. U kunt de **Azure Policy**-service gebruiken om aangepaste beveiligingsbeleidslijnen te maken of ingebouwde beleidslijnen gebruiken om aanbevolen werkwijzen en nalevingsnormen af te dwingen. U kunt ook uw beveiligingsstatus toetsen aan industrienormen zoals [NIST 800-53](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final), [CIS](https://www.cisecurity.org/) en [ISO 27001](https://www.iso.org/isoiec-27001-information-security.html).

Azure Security Center biedt ook functies voor compliancebeheer, waarmee u de compliance-status van uw organisatie kunt volgen ten opzichte van verschillende regelgevingskaders, zoals [GDPR](https://gdpr.eu/), [HIPAA](https://www.hhs.gov/hipaa/index.html) en [PCI DSS](https://www.pcisecuritystandards.org/).

______

## Uw Azure-middelen beveiligen

**Beveiligingshygiëne** is een belangrijk aspect van de beveiliging van uw cloudomgeving. Azure Security Center biedt **Secure Score**, een meting van uw beveiligingshouding, om u te helpen inzicht te krijgen in de algehele beveiliging van uw resources. U kunt uw Secure Score verbeteren door de aanbevelingen van Azure Security Center op te volgen.

### Netwerkbeveiliging

Het implementeren van goede netwerkbeveiligingsmaatregelen, zoals **Network Security Groups (NSG's)**, **Azure Firewall** en **Web Application Firewall (WAF)**, is cruciaal om uw Azure-omgeving te beschermen tegen potentiële bedreigingen. Deze tools helpen u inkomend en uitgaand netwerkverkeer te controleren en beschermen uw bronnen tegen ongeautoriseerde toegang en potentiële aanvallen.

#### Netwerkbeveiligingsgroepen (NSG's)

NSG's fungeren als een virtuele firewall voor uw Azure resources, waarmee u regels kunt definiëren die netwerkverkeer van en naar uw resources toestaan of weigeren. U kunt bijvoorbeeld een NSG maken met regels om specifiek verkeer toe te staan of te weigeren:

```azurecli
# Een netwerkbeveiligingsgroep maken
az network nsg create --name MyNSG --resource-group MyResourceGroup

# Regels toevoegen om verkeer toe te staan of te blokkeren
az network nsg rule create --name MyNSGRule --nsg-name MyNSG --priority 100 --resource-group MyResourceGroup --access Allow --protocol Tcp --direction Inbound --source-address-prefixes '*' --source-port-ranges '*' --destination-address-prefixes '*' --destination-port-ranges '80'
```
Lees meer over [Network Security Groups](https://docs.microsoft.com/en-us/azure/virtual-network/security-overview) in de officiële documentatie.

Het bovenstaande voorbeeld staat inkomend TCP-verkeer op poort 80 toe vanaf alle IPv4-bronnen. Gebruik voor productie een bekend bronbereik, een privé-eindpunt of een route via een load balancer. Raadpleeg het actuele [NSG-beveiligingsoverzicht](https://learn.microsoft.com/en-us/azure/virtual-network/network-security-groups-overview) voordat u het voorbeeld kopieert.

#### Azure Firewall
Azure Firewall is een beheerde, cloudgebaseerde netwerkbeveiligingsdienst die uw Azure-bronnen beschermt. Het biedt geavanceerde functies zoals filteren op basis van dreigingsinformatie, webcategorieën en gecentraliseerde registratie en analyse. Om Azure Firewall in te stellen, volgt u de [snelstartinstructies](https://learn.microsoft.com/en-us/azure/firewall-manager/quick-firewall-policy-bicep).

#### Web Application Firewall (WAF)
Web Application Firewall (WAF) is een functie van **Azure Application Gateway** die uw web applicaties beschermt tegen veelvoorkomende web exploits zoals SQL injectie, cross-site scripting en andere bedreigingen. WAF kan eenvoudig worden geïntegreerd met uw bestaande webapplicaties en u kunt aangepaste regels configureren om bescherming te bieden tegen specifieke aanvalspatronen.

Hier is een voorbeeld van hoe u een Application Gateway maakt met WAF ingeschakeld:
```azurecli
# Een WAF-beleid maken
az network application-gateway waf-policy create --name MyWafPolicy --resource-group MyResourceGroup --location EastUS

# Een virtueel netwerk en subnet maken
az network vnet create --name MyVNet --resource-group MyResourceGroup --location EastUS --address-prefix 10.0.0.0/16
az network vnet subnet create --name MySubnet --resource-group MyResourceGroup --vnet-name MyVNet --address-prefix 10.0.0.0/24

# Een openbaar IP-adres maken
az network public-ip create --name MyPublicIP --resource-group MyResourceGroup --location EastUS --sku Standard

# Een Application Gateway met ingeschakelde WAF maken
az network application-gateway create --name MyAppGateway --resource-group MyResourceGroup --location EastUS --vnet-name MyVNet --subnet MySubnet --public-ip-address MyPublicIP --http-settings-cookie-based-affinity Enabled --sku WAF_v2 --waf-policy MyWafPolicy

```
Meer informatie over [Web Application Firewall](https://docs.microsoft.com/en-us/azure/web-application-firewall/ag/ag-overview) in de officiële documentatie.

### Identiteit en toegangsbeheer

**Azure Active Directory (Azure AD)** is een essentieel onderdeel van de beveiliging van uw cloudomgeving. Azure Security Center biedt aanbevelingen voor het verbeteren van het identiteits- en toegangsbeheer, zoals het inschakelen van **Multi-Factor Authentication (MFA)**, het implementeren van **Role-Based Access Control (RBAC)** en het monitoren van verdachte activiteiten.

#### Multi-Factor Authenticatie (MFA)

MFA voegt een extra beveiligingslaag toe aan uw Azure AD-accounts door gebruikers te vragen om twee of meer vormen van verificatie voordat toegang wordt verleend. U kunt MFA voor uw organisatie inschakelen met de [stapsgewijze handleiding](https://docs.microsoft.com/en-us/azure/active-directory/authentication/tutorial-enable-azure-mfa) van Microsoft.

Voorbeeld: MFA inschakelen voor een gebruiker

```powershell
# Verbinden met Azure AD
Connect-AzureAD

# MFA inschakelen voor een specifieke gebruiker
$UserPrincipalName = "johndoe@example.com"
$StsUserObjectID = (Get-AzureADUser -Filter "UserPrincipalName eq '$UserPrincipalName'").ObjectId
$StrongAuthRequirements = @(@{"Location"=""; "SatisfactionFactor"="2"; "VerificationMethod"="1"};@{"Location"=""; "SatisfactionFactor"="2"; "VerificationMethod"="2"})
Set-AzureADUser -ObjectId $StsUserObjectID -StrongAuthenticationRequirements $StrongAuthRequirements
```
#### Rolgebaseerde toegangscontrole (RBAC)
Met RBAC kunt u granulaire machtigingen definiëren voor uw Azure resources, zodat gebruikers het juiste toegangsniveau hebben. U kunt rollen toewijzen aan gebruikers, groepen of applicaties om hun toegang tot resources binnen uw organisatie te beheren. Om RBAC te implementeren, volgt u de [officiële handleiding](https://docs.microsoft.com/en-us/azure/role-based-access-control/overview) van Microsoft.

Voorbeeld: Een rol toewijzen aan een gebruiker
```azurecli
# De rol Reader aan een gebruiker toewijzen
az role assignment create --assignee johndoe@example.com --role "Reader" --scope "/subscriptions/your_subscription_id/resourceGroups/your_resource_group"
```
#### Toezicht op verdachte activiteiten
Azure AD biedt functies zoals **Identity Protection** en **Conditional Access** waarmee u verdachte activiteiten kunt bewaken en erop kunt reageren. Identity Protection gebruikt machine learning-algoritmes om anomalieën en riskante aanmeldingspogingen te detecteren, terwijl u met Conditional Access beleidsregels kunt instellen die de toegang controleren op basis van factoren zoals apparaat, locatie en risiconiveau.

Volg de [officiële handleiding](https://learn.microsoft.com/en-us/azure/active-directory/identity-protection/concept-identity-protection-b2b) om Azure AD Identity Protection in te stellen.

Voorbeeld: Een beleid voor voorwaardelijke toegang maken

```powershell
# Verbinden met Azure AD
Connect-AzureAD

# Beleid voor voorwaardelijke toegang maken
$PolicyName = "BlockSignInFromUnknownLocations"
$PolicyDescription = "Aanmeldingen van gebruikers vanaf onbekende locaties blokkeren."
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
Meer informatie over [Azure AD Identity Protection](https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/overview) en [Conditional Access](https://learn.microsoft.com/en-us/azure/active-directory/conditional-access/overview) vindt u in de officiële documentatie.


### Gegevensbeveiliging

De bescherming van uw gegevens in de cloud is van cruciaal belang. Azure Security Center biedt verschillende functies voor gegevensbeveiliging, zoals **Azure Information Protection**, **Azure Storage Service Encryption** en **Azure Disk Encryption**. Met deze functies kunt u de toegang tot uw gegevens versleutelen en beheren, zodat gevoelige informatie veilig blijft.

#### Azure Information Protection

**Azure Information Protection (AIP)** is een cloud-based oplossing waarmee u gevoelige documenten en e-mails kunt classificeren, labelen en beschermen. AIP biedt een reeks ingebouwde labels, zoals "Vertrouwelijk" en "Persoonlijk", die kunnen worden aangepast aan de behoeften van uw organisatie. U kunt AIP ook configureren om automatisch labels toe te passen op basis van vooraf gedefinieerde regels. Om aan de slag te gaan met AIP, volgt u de [officiële handleiding](https://docs.microsoft.com/en-us/azure/information-protection/what-is-information-protection). Azure Information Protection is een historische productnaam en staat in de actuele Sentinel-documentatie als verouderd. Raadpleeg de documentatie over Microsoft Purview Information Protection voordat u een nieuwe implementatie start.

Voorbeeld: Een aangepast etiket maken

```powershell
# Verbinden met de AIP-service
Connect-AipService

# Een aangepast label met beveiligingsinstellingen maken
$LabelName = "Gevoelig - Alleen intern gebruik"
$LabelDescription = "Dit label past versleuteling en een toegangsbeleid voor uitsluitend intern gebruik toe."
$LabelProtectionSettings = @{
    "ContentExpirationDate" = (Get-Date).AddMonths(6).ToUniversalTime();
    "OfflineAccessInterval" = "P7D";
    "UserRights" = @("domain\GroupA=View", "domain\GroupB=View,Edit,Print")
}
New-AipServiceLabel -Name $LabelName -Description $LabelDescription -ProtectionSettings $LabelProtectionSettings
```
#### Azure Storage Service Encryption
**Azure Storage Service Encryption (SSE)** versleutelt automatisch uw gegevens in rust in Azure Storage-accounts, inclusief Blob-, Bestands-, Tabel- en Wachtrij-opslag. SSE maakt gebruik van door Azure beheerde sleutels of door de klant beheerde sleutels om encryptie op opslagaccountniveau te bieden. Om SSE in te schakelen, volgt u de [stapsgewijze handleiding](https://docs.microsoft.com/en-us/azure/storage/common/storage-service-encryption) van Microsoft.

Voorbeeld: SSE inschakelen voor een opslagaccount

```azurecli
# SSE inschakelen met door Azure beheerde sleutels
az storage account update --name mystorageaccount --resource-group myresourcegroup --encryption-services blob file
```
#### Azure Schijfversleuteling
**Azure Disk Encryption** helpt u schijven van virtuele machines te beveiligen door ze te versleutelen met BitLocker (Windows) of dm-crypt (Linux). De encryptiesleutels en -geheimen worden beschermd door Azure Key Vault, zodat uw gegevens in rust worden beveiligd. Om Azure Disk Encryption in te schakelen, volgt u de [officiële handleiding](https://learn.microsoft.com/en-us/azure/virtual-machines/disk-encryption-overview) van Microsoft.

Voorbeeld: Azure-schijfversleuteling inschakelen voor een virtuele machine
```azurecli
# Azure Disk Encryption inschakelen voor een Windows-VM
az vm encryption enable --resource-group myResourceGroup --name myVM --disk-encryption-keyvault myKeyVault
```
Meer informatie over [Azure Information Protection](https://docs.microsoft.com/en-us/azure/information-protection/what-is-information-protection), [Azure Storage Service Encryption](https://docs.microsoft.com/en-us/azure/storage/common/storage-service-encryption) en [Azure Disk Encryption](https://learn.microsoft.com/en-us/azure/virtual-machines/disk-encryption-overview) vindt u in de officiële documentatie.
______

## Detecteren van en reageren op bedreigingen

Azure Security Center gebruikt geavanceerde mogelijkheden voor detectie van bedreigingen om potentiële bedreigingen te identificeren en u daarvoor te waarschuwen. Door integratie met **Azure Sentinel** kunt u beveiligingsincidenten in uw hele omgeving bewaken, onderzoeken en erop reageren.

### Bedreigingsdetectie

Azure Security Center gebruikt **Azure Defender**, een set geavanceerde mogelijkheden voor detectie van bedreigingen, om potentiële beveiligingsbedreigingen te identificeren. Azure Defender controleert uw bronnen op indicatoren voor compromittering en biedt waarschuwingen en aanbevelingen om u te helpen reageren op potentiële bedreigingen. Volg de [officiële handleiding](https://docs.microsoft.com/en-us/azure/security-center/defender-for-cloud-enable) om Azure Defender in te schakelen.

Voorbeeld: Azure Defender inschakelen voor een abonnement

```azurecli
# Azure Defender inschakelen voor een abonnement
az security auto-provisioning-setting update --name default --auto-provision on
```
### Reactie op bedreigingen
Wanneer een bedreiging wordt gedetecteerd, is het essentieel om snel en effectief te reageren. Azure Security Center biedt **Security Incident** management, waarmee u beveiligingsincidenten kunt onderzoeken en erop kunt reageren. U kunt ook integreren met **Azure Sentinel** om geautomatiseerde playbooks te maken en uw reactie op beveiligingsincidenten te orkestreren. Lees meer over de integratie van Azure Security Center met Azure Sentinel in de **officiële documentatie**.

Voorbeeld: Maak een Logic App playbook voor Azure Sentinel
```azurecli
# Een resourcegroep maken
az group create --name MyResourceGroup --location EastUS

# Een Logic App maken
az logic workflow create --resource-group MyResourceGroup --location EastUS --name MyPlaybook --definition @playbook-definition.json
```
Het bestand `playbook-definition.json` moet de definitie van de Logic App-playbook bevatten. Voorbeelden van Azure Sentinel-playbooks vindt u in de [Azure Sentinel-repository op GitHub](https://github.com/Azure/Azure-Sentinel/tree/master/Playbooks).

Door gebruik te maken van de mogelijkheden van Azure Security Center voor detectie van bedreigingen en te integreren met Azure Sentinel, kunt u een robuuste beveiligingsstrategie opzetten om bedreigingen in uw Azure-omgeving te detecteren en erop te reageren. Meer informatie over [Azure Defender](https://learn.microsoft.com/en-us/azure/defender-for-cloud/enable-enhanced-security) en [Azure Sentinel](https://docs.microsoft.com/en-us/azure/sentinel/overview) vindt u in de officiële documentatie.
______

De [Defender for Cloud-connector](https://learn.microsoft.com/en-us/azure/sentinel/connect-defender-for-cloud) stuurt waarschuwingen naar Microsoft Sentinel. Controleer de connector, regels voor gegevensverzameling en analyse en de incidentworkflow voordat u op automatisering vertrouwt.

## Toezicht en Rapportage

Monitoring en rapportage zijn essentiële onderdelen van het onderhouden van een veilige cloudomgeving. Azure Security Center biedt verschillende tools voor monitoring en rapportage, zoals **Security Dashboard**, **Security Alerts** en **Compliance Reports**.

### Beveiligingsdashboard

Het beveiligingsdashboard in Azure Security Center biedt een uitgebreid overzicht van uw beveiligingsstatus. Het toont uw Secure Score, beveiligingsaanbevelingen en actieve beveiligingswaarschuwingen. Het dashboard geeft ook inzicht in uw compliance status en stelt u in staat om uw vooruitgang in de tijd te volgen.

### Beveiligingswaarschuwingen

Azure Security Center genereert beveiligingswaarschuwingen wanneer potentiële bedreigingen worden gedetecteerd. Deze waarschuwingen geven gedetailleerde informatie over de bedreiging, evenals aanbevelingen om het risico te beperken. U kunt Azure Security Center configureren om meldingen via e-mail, SMS of integratie met tools van derden, zoals [Slack](https://slack.com/) of [Microsoft Teams](https://www.microsoft.com/en-us/microsoft-teams/group-chat-software).

### Nalevingsrapporten

Met Azure Security Center kunt u nalevingsrapporten genereren voor verschillende regelgevingskaders, zoals GDPR, HIPAA en PCI DSS. Met deze rapporten kunt u de nalevingsstatus van uw organisatie volgen en gebieden identificeren die verbetering behoeven.

______

## Aanbevolen werkwijzen voor Azure Security Center

Om het meeste uit Azure Security Center te halen, kunt u overwegen de volgende aanbevolen werkwijzen toe te passen:

1. **Schakel Azure Security Center in op al uw abonnementen**: Ervoor zorgen dat al uw Azure-abonnementen worden beschermd door Azure Security Center is cruciaal voor het behoud van een veilige cloudomgeving.
2. **Bekijk regelmatig uw Secure Score**: Het monitoren van uw Secure Score helpt u inzicht te krijgen in uw algehele beveiligingshouding en gebieden te identificeren die verbetering behoeven.
3. **Implementeer beveiligingsaanbevelingen**: Door de beveiligingsaanbevelingen van Azure Security Center op te volgen, kunt u uw beveiligingshouding verbeteren en potentiële risico's verminderen.
4. **Bewaak beveiligingswaarschuwingen**: Bekijk en reageer regelmatig op beveiligingswaarschuwingen om potentiële bedreigingen te beperken en een veilige omgeving te handhaven.
5. **Blijf op de hoogte van compliancevereisten**: Zorg ervoor dat uw organisatie blijft voldoen aan de nieuwste regelgevingskaders door uw compliancebeleid regelmatig te herzien en bij te werken.

______
## Huidige Defender for Cloud-werkwijze

Gebruik deze volgorde voor een huidige implementatie. De namen in de oorspronkelijke secties blijven nuttig voor historische zoekopdrachten, maar de portal en documentatie gebruiken de terminologie van Defender for Cloud.

1. **Breng abonnementen en connectors in kaart.** Leg Azure-abonnementen, AWS- of GCP-connectors, DevOps-projecten en kritieke resources vast.
2. **Schakel de vereiste Defender-plannen in.** Kies plannen per workload en controleer de licenties voordat u ze inschakelt voor productieabonnementen.
3. **Controleer Cloud Secure Score en aanbevelingen.** Geef prioriteit aan internetblootstelling, identiteitsrisico’s, misbruikbare kwetsbaarheden en ontbrekende logging. Een score bewijst geen volledige naleving.
4. **Configureer Microsoft Entra-controles.** Vereis phishingbestendige MFA voor belangrijke accounts, pas RBAC met minimale rechten toe en controleer bevoorrechte toegang.
5. **Stuur waarschuwingen naar Microsoft Sentinel.** Controleer opname van waarschuwingen, analytische regels, eigenaarschap, automatisering van respons en bewaartermijnen.
6. **Controleer opnieuw na wijzigingen.** Bekijk aanbevelingen na patches, architectuurwijzigingen, nieuwe connectors of planwijzigingen.

## Praktische controlelijst

- **Identiteit:** verwijder verouderde accounts, beperk permanente beheerdersrechten en controleer uitsluitingen voor voorwaardelijke toegang.
- **Netwerk:** verwijder openbare beheerpoorten, beperk NSG-bronbereiken en controleer of firewall- en WAF-logboeken de bewakingswerkruimte bereiken.
- **Gegevens:** classificeer gevoelige opslag, controleer versleuteling en sleutelbeheer en test herstel van back-ups.
- **Detectie:** controleer de ernst van waarschuwingen, meldingsroutes, incidenteigenaarschap en respons-playbooks.
- **Governance:** wijs elke beleidsactie toe aan een eigenaar, een vervaldatum voor uitzonderingen en bewijs voor het vereiste raamwerk.


## Referenties
- [Documentatie van Azure Security Center](https://docs.microsoft.com/en-us/azure/security-center/)
- [Azure Policy-service](https://docs.microsoft.com/en-us/azure/governance/policy/)
- [NIST 800-53](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final)
- [CIS](https://www.cisecurity.org/)
- [ISO 27001](https://www.iso.org/isoiec-27001-information-security.html)
- [GDPR](https://gdpr.eu/)
- [HIPAA](https://www.hhs.gov/hipaa/index.html)
- [PCI DSS](https://www.pcisecuritystandards.org/)

