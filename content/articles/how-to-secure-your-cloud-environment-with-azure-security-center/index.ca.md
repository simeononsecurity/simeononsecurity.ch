---
title: "Protegiu el vostre entorn de núvol amb Microsoft Defender for Cloud"
date: 2023-04-10
lastmod: 2026-11-20
toc: true
draft: false
description: "Protegiu les càrregues de treball d'Azure amb Microsoft Defender for Cloud. Consulteu els termes antics d'Azure Security Center, les recomanacions, les polítiques i els passos de resposta."
tags: ["Azure", "Security Center", "seguretat al núvol", "Azure Sentinel", "Azure Defender", "seguretat de xarxa", "gestió d'identitats", "seguretat de dades", "detecció d'amenaces", "resposta a amenaces", "MFA", "RBAC", "NSGs", "Azure Firewall", "WAF", "Azure AD", "Azure Information Protection", "Azure Storage Service Encryption", "Azure Disk Encryption"]
cover: "/img/cover/A_shield_icon_surrounded_by_cloud_symbols.webp"
coverAlt: "Un escut envoltat de símbols de núvol representa un entorn de núvol segur. L'escut mostra el logotip d'Azure Security Center."
coverCaption: ""
---

**Com protegir el vostre entorn de núvol amb Azure Security Center**

Protegir l'entorn de núvol és essencial per defensar les dades, les aplicacions i la infraestructura de l'organització de les amenaces. **Azure Security Center**, de Microsoft, us ajuda a millorar la postura de seguretat i a identificar ràpidament els riscos potencials d'Azure. Aquest article explica com protegir l'entorn amb Azure Security Center i presenta bones pràctiques per implementar funcions de seguretat. També inclou detalls tècnics i exemples per ajudar-vos a aplicar els passos.

*Els noms dels productes han canviat des de la publicació original de l'article. Microsoft Azure Security Center ara es diu Microsoft Defender for Cloud. Azure Active Directory ara es diu Microsoft Entra ID. Azure Sentinel ara es diu Microsoft Sentinel. Azure Defender fa referència als plans Defender i a la protecció de càrregues de treball de Defender for Cloud. A continuació es mantenen els noms antics quan descriuen la terminologia de 2023.*

La [visió general actual de Defender for Cloud](https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-cloud-introduction) el descriu com una plataforma de protecció d'aplicacions natives del núvol, amb gestió de la postura de seguretat al núvol, DevSecOps i protecció de càrregues de treball. La disponibilitat de les funcions i les llicències depenen del núvol, del tipus de recurs, de la subscripció i del pla.

______

## Entendre Azure Security Center

Azure Security Center és un **sistema unificat de gestió de la seguretat de la infraestructura**. Ajuda a identificar i corregir vulnerabilitats potencials de l'entorn de núvol. Inclou funcions de detecció d'amenaces, gestió de la postura de seguretat i gestió del compliment.

**L'avaluació contínua de la seguretat** i la **protecció avançada contra amenaces** són dues funcions clau d'Azure Security Center. L'avaluació contínua ajuda a trobar possibles problemes de seguretat. La protecció avançada ajuda a detectar les amenaces potencials i respondre-hi.

______

## Implementar polítiques de seguretat i estàndards de compliment

Azure Security Center permet implementar i gestionar polítiques de seguretat a tot l'entorn de núvol. Feu servir el servei **Azure Policy** per crear polítiques personalitzades, o bé apliqueu les polítiques integrades per fer complir les bones pràctiques i els estàndards de compliment. També podeu comparar la postura de seguretat amb estàndards del sector com [NIST 800-53](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final), [CIS](https://www.cisecurity.org/) i [ISO 27001](https://www.iso.org/isoiec-27001-information-security.html).

Azure Security Center també ofereix funcions de gestió del compliment, que ajuden a seguir l'estat de l'organització segons marcs normatius com [GDPR](https://gdpr.eu/), [HIPAA](https://www.hhs.gov/hipaa/index.html) i [PCI DSS](https://www.pcisecuritystandards.org/).

______

## Protegir els recursos d'Azure

**Mantenir una bona higiene de seguretat dels recursos** és una part important de la protecció de l'entorn de núvol. Azure Security Center proporciona **Secure Score**, una mesura de la postura de seguretat que us ajuda a valorar la protecció general dels recursos. Apliqueu les recomanacions d'Azure Security Center per millorar-ne la puntuació.

### Seguretat de xarxa

Mesures com **Network Security Groups (NSGs)**, **Azure Firewall** i **Web Application Firewall (WAF)** protegeixen l'entorn d'Azure de les amenaces potencials. Controlen el trànsit de xarxa entrant i sortint i redueixen el risc d'accés no autoritzat i d'atacs.

#### Network Security Groups (NSGs)

Els NSG funcionen com a tallafocs virtuals per als recursos d'Azure. Permeten definir regles per autoritzar o denegar el trànsit de xarxa cap als recursos i des dels recursos. Aquest exemple crea un NSG amb regles de trànsit:

```azurecli
# Creeu un Network Security Group
az network nsg create --name MyNSG --resource-group MyResourceGroup

# Afegiu regles per permetre o denegar el trànsit
az network nsg rule create --name MyNSGRule --nsg-name MyNSG --priority 100 --resource-group MyResourceGroup --access Allow --protocol Tcp --direction Inbound --source-address-prefixes '*' --source-port-ranges '*' --destination-address-prefixes '*' --destination-port-ranges '80'
```
Consulteu la documentació oficial sobre [Network Security Groups](https://docs.microsoft.com/en-us/azure/virtual-network/security-overview).

L'exemple permet el trànsit TCP entrant pel port 80 des de qualsevol origen IPv4. En producció, feu servir un interval d'origen conegut, un punt final privat o una ruta a través d'un equilibrador de càrrega. Abans de copiar l'exemple, llegiu la [visió general de seguretat dels NSG](https://learn.microsoft.com/en-us/azure/virtual-network/network-security-groups-overview).

#### Azure Firewall

Azure Firewall és un servei gestionat de seguretat de xarxa basat en el núvol, que protegeix els recursos d'Azure. Ofereix filtratge basat en intel·ligència sobre amenaces, categories web i registre i anàlisi centralitzats. Per configurar-lo, seguiu les [instruccions d'inici ràpid](https://learn.microsoft.com/en-us/azure/firewall-manager/quick-firewall-policy-bicep).

#### Web Application Firewall (WAF)

Web Application Firewall (WAF) és una funció d'**Azure Application Gateway**. Protegeix les aplicacions web d'atacs habituals, com ara la injecció SQL, l'script entre llocs i altres explotacions. Integreu WAF amb les aplicacions existents i configureu regles pròpies per als patrons d'atac concrets.

Exemple de creació d'un Application Gateway amb WAF activat:

```azurecli
# Creeu una política WAF
az network application-gateway waf-policy create --name MyWafPolicy --resource-group MyResourceGroup --location EastUS

# Creeu una xarxa virtual i una subxarxa
az network vnet create --name MyVNet --resource-group MyResourceGroup --location EastUS --address-prefix 10.0.0.0/16
az network vnet subnet create --name MySubnet --resource-group MyResourceGroup --vnet-name MyVNet --address-prefix 10.0.0.0/24

# Creeu una adreça IP pública
az network public-ip create --name MyPublicIP --resource-group MyResourceGroup --location EastUS --sku Standard

# Creeu un Application Gateway amb WAF activat
az network application-gateway create --name MyAppGateway --resource-group MyResourceGroup --location EastUS --vnet-name MyVNet --subnet MySubnet --public-ip-address MyPublicIP --http-settings-cookie-based-affinity Enabled --sku WAF_v2 --waf-policy MyWafPolicy

```
Consulteu la documentació oficial sobre [Web Application Firewall](https://docs.microsoft.com/en-us/azure/web-application-firewall/ag/ag-overview).

### Gestió de la identitat i l'accés

**Microsoft Entra ID, abans Azure Active Directory (Azure AD),** és essencial per protegir l'entorn de núvol. Defender for Cloud recomana accions per millorar la gestió de la identitat i l'accés, com ara activar **Multi-Factor Authentication (MFA)**, aplicar **Role-Based Access Control (RBAC)** i supervisar les activitats sospitoses.

#### Multi-Factor Authentication (MFA)

MFA afegeix una capa de seguretat als comptes d'Azure AD perquè exigeix dues o més formes de verificació abans de concedir accés. Per activar MFA a l'organització, seguiu la [guia pas a pas](https://docs.microsoft.com/en-us/azure/active-directory/authentication/tutorial-enable-azure-mfa) de Microsoft.

Exemple: activar MFA per a un usuari

```powershell
# Connecteu-vos a Azure AD
Connect-AzureAD

# Activeu MFA per a un usuari concret
$UserPrincipalName = "johndoe@example.com"
$StsUserObjectID = (Get-AzureADUser -Filter "UserPrincipalName eq '$UserPrincipalName'").ObjectId
$StrongAuthRequirements = @(@{"Location"=""; "SatisfactionFactor"="2"; "VerificationMethod"="1"};@{"Location"=""; "SatisfactionFactor"="2"; "VerificationMethod"="2"})
Set-AzureADUser -ObjectId $StsUserObjectID -StrongAuthenticationRequirements $StrongAuthRequirements
```
#### Role-Based Access Control (RBAC)

RBAC permet definir permisos detallats per als recursos d'Azure i assegurar que cada usuari té el nivell d'accés adequat. Assigneu rols a usuaris, grups o aplicacions per gestionar l'accés als recursos de l'organització. Per implementar RBAC, seguiu la [guia oficial](https://docs.microsoft.com/en-us/azure/role-based-access-control/overview) de Microsoft.

Exemple: assignar un rol a un usuari

```azurecli
# Assigneu el rol Reader a un usuari
az role assignment create --assignee johndoe@example.com --role "Reader" --scope "/subscriptions/your_subscription_id/resourceGroups/your_resource_group"
```
#### Supervisar activitats sospitoses

Azure AD ofereix **Identity Protection** i **Conditional Access** per supervisar i respondre a activitats sospitoses. Identity Protection fa servir l'aprenentatge automàtic per detectar anomalies i inicis de sessió de risc. Conditional Access permet definir polítiques de control d'accés segons factors com el dispositiu, la ubicació i el risc.

Per configurar Azure AD Identity Protection, seguiu la [guia oficial](https://learn.microsoft.com/en-us/azure/active-directory/identity-protection/concept-identity-protection-b2b) de Microsoft.

Exemple: crear una política de Conditional Access

```powershell
# Connecteu-vos a Azure AD
Connect-AzureAD

# Creeu una política de Conditional Access
$PolicyName = "BlockSignInFromUnknownLocations"
$PolicyDescription = "Bloqueja els inicis de sessió d'usuaris des d'ubicacions desconegudes."
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
Consulteu la documentació oficial sobre [Azure AD Identity Protection](https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/overview) i [Conditional Access](https://learn.microsoft.com/en-us/azure/active-directory/conditional-access/overview).

### Seguretat de les dades

Protegir les dades al núvol és essencial. Azure Security Center ofereix **Azure Information Protection**, **Azure Storage Service Encryption** i **Azure Disk Encryption**. Aquestes funcions ajuden a xifrar les dades i gestionar-ne l'accés.

#### Azure Information Protection

**Azure Information Protection (AIP)** és un servei al núvol per classificar, etiquetar i protegir documents i correus electrònics sensibles. AIP inclou etiquetes com ara «Confidencial» i «Personal», que podeu adaptar a les necessitats de l'organització. També podeu configurar l'aplicació automàtica d'etiquetes segons regles predefinides. Per començar, seguiu la [guia oficial](https://docs.microsoft.com/en-us/azure/information-protection/what-is-information-protection).

Exemple: crear una etiqueta personalitzada

```powershell
# Connecteu-vos al servei AIP
Connect-AipService

# Creeu una etiqueta personalitzada amb paràmetres de protecció
$LabelName = "Sensible - Només per a ús intern"
$LabelDescription = "Aquesta etiqueta aplica xifratge i una política d'accés només per a ús intern."
$LabelProtectionSettings = @{
    "ContentExpirationDate" = (Get-Date).AddMonths(6).ToUniversalTime();
    "OfflineAccessInterval" = "P7D";
    "UserRights" = @("domain\GroupA=View", "domain\GroupB=View,Edit,Print")
}
New-AipServiceLabel -Name $LabelName -Description $LabelDescription -ProtectionSettings $LabelProtectionSettings
```
#### Azure Storage Service Encryption

**Azure Storage Service Encryption (SSE)** xifra automàticament les dades en repòs dels comptes d'Azure Storage, inclosos Blob, File, Table i Queue. SSE fa servir claus gestionades per Azure o pel client per xifrar les dades a escala del compte d'emmagatzematge. Per activar SSE, seguiu la [guia pas a pas](https://docs.microsoft.com/en-us/azure/storage/common/storage-service-encryption) de Microsoft.

Azure Information Protection és un nom antic de producte. La documentació actual sobre la disponibilitat de funcions de Sentinel el marca com a obsolet. Abans d'iniciar un desplegament nou d'etiquetes, consulteu la documentació actual de Microsoft Purview Information Protection.

Exemple: activar SSE per a un compte d'emmagatzematge

```azurecli
# Activeu SSE amb claus gestionades per Azure
az storage account update --name mystorageaccount --resource-group myresourcegroup --encryption-services blob file
```
#### Azure Disk Encryption

**Azure Disk Encryption** protegeix els discos de màquines virtuals xifrant-los amb BitLocker (Windows) o dm-crypt (Linux). Azure Key Vault protegeix les claus i els secrets de xifratge. Per activar Azure Disk Encryption, seguiu la [guia oficial](https://learn.microsoft.com/en-us/azure/virtual-machines/disk-encryption-overview) de Microsoft.

Exemple: activar Azure Disk Encryption per a una màquina virtual

```azurecli
# Activeu Azure Disk Encryption per a una màquina virtual Windows
az vm encryption enable --resource-group myResourceGroup --name myVM --disk-encryption-keyvault myKeyVault
```
Consulteu la documentació oficial d'[Azure Information Protection](https://docs.microsoft.com/en-us/azure/information-protection/what-is-information-protection), [Azure Storage Service Encryption](https://docs.microsoft.com/en-us/azure/storage/common/storage-service-encryption) i [Azure Disk Encryption](https://learn.microsoft.com/en-us/azure/virtual-machines/disk-encryption-overview).
______

## Detectar amenaces i respondre-hi

Azure Security Center detecta amenaces potencials i n'envia alertes. La integració amb **Azure Sentinel** permet supervisar, investigar i respondre als incidents de seguretat de tot l'entorn.

### Detecció d'amenaces

Azure Security Center fa servir **Azure Defender** per identificar possibles amenaces de seguretat. Azure Defender supervisa els recursos per trobar indicadors de compromís i proporciona alertes i recomanacions per respondre-hi. Per activar Azure Defender, seguiu la [guia oficial](https://docs.microsoft.com/en-us/azure/security-center/defender-for-cloud-enable).

Exemple: activar Azure Defender per a una subscripció

```azurecli
# Activeu Azure Defender per a una subscripció
az security auto-provisioning-setting update --name default --auto-provision on
```
### Resposta a les amenaces
Quan detecteu una amenaça, responeu-hi de manera ràpida i efectiva. La gestió **Security Incident** d'Azure Security Center ajuda a investigar i gestionar incidents. També podeu integrar **Azure Sentinel** per crear fluxos automatitzats i coordinar la resposta. Consulteu la **documentació oficial** sobre la integració d'Azure Security Center amb Azure Sentinel.

Exemple: crear un flux Logic App per a Azure Sentinel
```azurecli
# Creeu un grup de recursos
az group create --name MyResourceGroup --location EastUS

# Creeu un Logic App
az logic workflow create --resource-group MyResourceGroup --location EastUS --name MyPlaybook --definition @playbook-definition.json
```
El fitxer `playbook-definition.json` ha de contenir la definició del flux de Logic App. Trobareu exemples per a Azure Sentinel al [repositori Azure-Sentinel de GitHub](https://github.com/Azure/Azure-Sentinel/tree/master/Playbooks).

Combineu la detecció d'amenaces d'Azure Security Center amb Azure Sentinel per detectar i respondre a les amenaces de l'entorn d'Azure. Consulteu la documentació oficial d'[Azure Defender](https://learn.microsoft.com/en-us/azure/defender-for-cloud/enable-enhanced-security) i [Azure Sentinel](https://docs.microsoft.com/en-us/azure/sentinel/overview).

La integració actual envia les alertes de Defender for Cloud a Microsoft Sentinel mitjançant el [connector de Defender for Cloud](https://learn.microsoft.com/en-us/azure/sentinel/connect-defender-for-cloud). Abans de dependre de l'automatització, valideu el connector, les regles de recollida de dades, les regles d'anàlisi i el flux de gestió d'incidents al portal de Defender o d'Azure.
______

## Supervisió i informes

La supervisió i els informes ajuden a mantenir un entorn de núvol segur. Azure Security Center ofereix eines com ara el **tauler de seguretat**, les **alertes de seguretat** i els **informes de compliment**.

### Tauler de seguretat

El Security Dashboard d'Azure Security Center mostra una visió general de la postura de seguretat. Hi apareixen Secure Score, recomanacions i alertes actives. El tauler també mostra l'estat de compliment i permet seguir-ne l'evolució.

### Alertes de seguretat

Azure Security Center genera alertes quan detecta amenaces potencials. Les alertes inclouen detalls sobre l'amenaça i recomanacions per reduir-ne el risc. Podeu configurar avisos per correu electrònic o SMS, o integrar el servei amb [Slack](https://slack.com/) o [Microsoft Teams](https://www.microsoft.com/en-us/microsoft-teams/group-chat-software).

### Informes de compliment

Azure Security Center genera informes per a marcs normatius com GDPR, HIPAA i PCI DSS. Feu-los servir per seguir l'estat de compliment de l'organització i identificar els aspectes que cal millorar.

______

## Bones pràctiques per a Azure Security Center

Per aprofitar Azure Security Center, apliqueu aquestes pràctiques:

1. **Activeu Azure Security Center a totes les subscripcions**: confirmeu que totes les subscripcions d'Azure estan protegides.
2. **Reviseu Secure Score regularment**: superviseu la postura general de seguretat i identifiqueu els aspectes que cal millorar.
3. **Apliqueu les recomanacions de seguretat**: milloreu la postura de seguretat i reduïu els riscos seguint les recomanacions d'Azure Security Center.
4. **Superviseu les alertes de seguretat**: reviseu les alertes i responeu-hi per reduir les amenaces potencials.
5. **Manteniu actualitzats els requisits de compliment**: reviseu i actualitzeu les polítiques per complir els marcs normatius actuals.

## Flux actual de Defender for Cloud

Per a un desplegament actual, seguiu aquesta seqüència. Els noms antics de les seccions ajuden a trobar informació històrica, però el portal i la documentació fan servir la terminologia de Defender for Cloud.

1. **Inventarieu les subscripcions i els connectors.** Registreu les subscripcions d'Azure, els connectors d'AWS o GCP, els projectes DevOps i els recursos crítics.
2. **Activeu els plans Defender necessaris.** Trieu plans per càrrega de treball i confirmeu la llicència abans d'activar-los a les subscripcions de producció.
3. **Reviseu Cloud Secure Score i les recomanacions.** Prioritzeu l'exposició a Internet, els riscos d'identitat, les vulnerabilitats explotables i la manca de registres. La puntuació no demostra el compliment complet.
4. **Configureu els controls de Microsoft Entra.** Exigiu MFA resistent a la pesca per als comptes importants, feu servir RBAC amb privilegis mínims i reviseu l'accés privilegiat.
5. **Envieu alertes a Microsoft Sentinel.** Confirmeu la recepció de les alertes, les regles d'anàlisi, els responsables, l'automatització de resposta i el període de retenció.
6. **Torneu a comprovar-ho després dels canvis.** Reviseu les recomanacions després d'aplicar pedaços, canviar l'arquitectura, afegir connectors o modificar plans.

## Llista pràctica de verificació

- **Identitat:** elimineu els comptes antics, reduïu l'accés permanent d'administrador i reviseu les excepcions de Conditional Access.
- **Xarxa:** tanqueu els ports públics d'administració, restringiu els intervals d'origen dels NSG i confirmeu que els registres del tallafoc i WAF arriben a l'espai de supervisió.
- **Dades:** classifiqueu els repositoris de dades sensibles, confirmeu el xifratge i la propietat de les claus i proveu la restauració de les còpies de seguretat.
- **Detecció:** confirmeu la gravetat de les alertes, l'encaminament de notificacions, els responsables dels incidents i els fluxos de resposta.
- **Governança:** assigneu un responsable, una data de caducitat de les excepcions i les proves de l'estàndard requerit a cada iniciativa de política.

______

## Referències

- [Documentació d'Azure Security Center](https://docs.microsoft.com/en-us/azure/security-center/)
- [Servei Azure Policy](https://docs.microsoft.com/en-us/azure/governance/policy/)
- [NIST 800-53](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final)
- [CIS](https://www.cisecurity.org/)
- [ISO 27001](https://www.iso.org/isoiec-27001-information-security.html)
- [GDPR](https://gdpr.eu/)
- [HIPAA](https://www.hhs.gov/hipaa/index.html)
- [PCI DSS](https://www.pcisecuritystandards.org/)
