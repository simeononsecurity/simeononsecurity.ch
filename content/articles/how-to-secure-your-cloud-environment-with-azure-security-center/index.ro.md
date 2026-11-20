---
title: "Protejați mediul cloud cu Microsoft Defender for Cloud"
date: 2023-04-10
lastmod: 2026-11-20
toc: true
draft: false
description: "Protejați încărcăturile de lucru Azure cu Microsoft Defender for Cloud. Consultați termenii vechi Azure Security Center, recomandările, politicile și pașii de răspuns."
tags: ["Azure", "Security Center", "securitate cloud", "Azure Sentinel", "Azure Defender", "securitatea rețelei", "gestionarea identității", "securitatea datelor", "detectarea amenințărilor", "răspuns la amenințări", "MFA", "RBAC", "NSGs", "Azure Firewall", "WAF", "Azure AD", "Azure Information Protection", "Azure Storage Service Encryption", "Azure Disk Encryption"]
cover: "/img/cover/A_shield_icon_surrounded_by_cloud_symbols.webp"
coverAlt: "Un scut înconjurat de simboluri cloud reprezintă un mediu cloud securizat. Scutul poartă sigla Azure Security Center."
coverCaption: ""
---

**Cum să vă securizați mediul cloud cu Azure Security Center**

Securizarea mediului cloud protejează datele, aplicațiile și infrastructura organizației împotriva amenințărilor. **Azure Security Center** de la Microsoft vă ajută să îmbunătățiți postura de securitate și să identificați rapid riscurile potențiale din Azure. Acest articol explică folosirea Azure Security Center și prezintă bune practici pentru implementarea funcțiilor de securitate. Include și detalii tehnice și exemple pentru aplicarea pașilor.

*Denumirile produselor s-au schimbat de la publicarea inițială a acestui articol. Microsoft Azure Security Center se numește acum Microsoft Defender for Cloud. Azure Active Directory se numește acum Microsoft Entra ID. Azure Sentinel se numește acum Microsoft Sentinel. Azure Defender desemnează planurile Defender și protecțiile încărcăturilor de lucru din Defender for Cloud. Numele vechi apar mai jos când descriu terminologia din 2023.*

[Prezentarea actuală Defender for Cloud](https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-cloud-introduction) descrie o platformă de protecție pentru aplicații cloud-native, cu gestionarea posturii de securitate cloud, DevSecOps și protecția încărcăturilor de lucru. Disponibilitatea funcțiilor și licențierea depind de cloud, tipul resursei, abonament și plan.

______

## Înțelegerea Azure Security Center

Azure Security Center este un **sistem unificat de gestionare a securității infrastructurii**. Vă ajută să identificați și să remediați vulnerabilitățile posibile din mediul cloud. Funcțiile sale includ detectarea amenințărilor, gestionarea posturii de securitate și gestionarea conformității.

**Evaluarea continuă a securității** și **Protecția avansată împotriva amenințărilor** sunt două funcții importante ale Azure Security Center. Evaluarea continuă identifică problemele potențiale de securitate. Protecția avansată ajută la detectarea și gestionarea amenințărilor.

______

## Implementarea politicilor de securitate și a standardelor de conformitate

Azure Security Center vă permite să implementați și să gestionați politici de securitate în mediul cloud. Folosiți serviciul **Azure Policy** pentru a crea politici personalizate sau politicile integrate pentru a aplica bune practici și standarde de conformitate. Comparați postura de securitate cu standarde din industrie precum [NIST 800-53](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final), [CIS](https://www.cisecurity.org/) și [ISO 27001](https://www.iso.org/isoiec-27001-information-security.html).

Azure Security Center oferă și funcții de gestionare a conformității. Acestea vă ajută să urmăriți situația organizației în raport cu cadre de reglementare precum [GDPR](https://gdpr.eu/), [HIPAA](https://www.hhs.gov/hipaa/index.html) și [PCI DSS](https://www.pcisecuritystandards.org/).

______

## Securizarea resurselor Azure

**Menținerea igienei de securitate a resurselor** este o parte importantă a protejării mediului cloud. Azure Security Center oferă **Secure Score**, o măsură a posturii de securitate care vă ajută să evaluați protecția generală a resurselor. Aplicați recomandările Azure Security Center pentru a îmbunătăți scorul.

### Securitatea rețelei

Măsuri precum **Network Security Groups (NSGs)**, **Azure Firewall** și **Web Application Firewall (WAF)** protejează Azure împotriva amenințărilor. Acestea controlează traficul de rețea de intrare și de ieșire și reduc riscul accesului neautorizat și al atacurilor.

#### Network Security Groups (NSGs)

NSG-urile funcționează ca firewalluri virtuale pentru resursele Azure. Definiți reguli care permit sau blochează traficul către și dinspre aceste resurse. Exemplul următor creează un NSG cu reguli pentru trafic:

```azurecli
# Creați un Network Security Group
az network nsg create --name MyNSG --resource-group MyResourceGroup

# Adăugați reguli pentru a permite sau a bloca traficul
az network nsg rule create --name MyNSGRule --nsg-name MyNSG --priority 100 --resource-group MyResourceGroup --access Allow --protocol Tcp --direction Inbound --source-address-prefixes '*' --source-port-ranges '*' --destination-address-prefixes '*' --destination-port-ranges '80'
```
Consultați documentația oficială despre [Network Security Groups](https://docs.microsoft.com/en-us/azure/virtual-network/security-overview).

Exemplul permite trafic TCP de intrare pe portul 80 de la orice sursă IPv4. În producție, folosiți un interval sursă cunoscut, un punct final privat sau o cale printr-un balansator de încărcare. Citiți [prezentarea securității NSG](https://learn.microsoft.com/en-us/azure/virtual-network/network-security-groups-overview) înainte de a folosi exemplul.

#### Azure Firewall

Azure Firewall este un serviciu gestionat de securitate a rețelei, bazat pe cloud. Protejează resursele Azure și oferă filtrare bazată pe informații despre amenințări, categorii Web și jurnalizare și analiză centralizate. Pentru configurare, urmați [instrucțiunile de pornire rapidă](https://learn.microsoft.com/en-us/azure/firewall-manager/quick-firewall-policy-bicep).

#### Web Application Firewall (WAF)

Web Application Firewall (WAF) este o funcție a **Azure Application Gateway**. Protejează aplicațiile Web împotriva atacurilor comune, precum injecția SQL, scripturile între site-uri și alte exploatări. Integrați WAF cu aplicațiile existente și configurați reguli proprii pentru anumite tipare de atac.

Exemplu de creare a unui Application Gateway cu WAF activat:

```azurecli
# Creați o politică WAF
az network application-gateway waf-policy create --name MyWafPolicy --resource-group MyResourceGroup --location EastUS

# Creați o rețea virtuală și o subrețea
az network vnet create --name MyVNet --resource-group MyResourceGroup --location EastUS --address-prefix 10.0.0.0/16
az network vnet subnet create --name MySubnet --resource-group MyResourceGroup --vnet-name MyVNet --address-prefix 10.0.0.0/24

# Creați o adresă IP publică
az network public-ip create --name MyPublicIP --resource-group MyResourceGroup --location EastUS --sku Standard

# Creați un Application Gateway cu WAF activat
az network application-gateway create --name MyAppGateway --resource-group MyResourceGroup --location EastUS --vnet-name MyVNet --subnet MySubnet --public-ip-address MyPublicIP --http-settings-cookie-based-affinity Enabled --sku WAF_v2 --waf-policy MyWafPolicy

```
Consultați documentația oficială despre [Web Application Firewall](https://docs.microsoft.com/en-us/azure/web-application-firewall/ag/ag-overview).

### Gestionarea identității și accesului

**Microsoft Entra ID, numit anterior Azure Active Directory (Azure AD),** este esențial pentru securizarea mediului cloud. Defender for Cloud recomandă măsuri pentru gestionarea identității și accesului, precum activarea **Multi-Factor Authentication (MFA)**, aplicarea **Role-Based Access Control (RBAC)** și monitorizarea activităților suspecte.

#### Multi-Factor Authentication (MFA)

MFA adaugă un nivel suplimentar de securitate conturilor Azure AD. Înainte de a acorda acces, solicită două sau mai multe forme de verificare. Pentru a activa MFA în organizație, urmați [ghidul pas cu pas](https://docs.microsoft.com/en-us/azure/active-directory/authentication/tutorial-enable-azure-mfa) de la Microsoft.

Exemplu: Activați MFA pentru un utilizator

```powershell
# Conectați-vă la Azure AD
Connect-AzureAD

# Activați MFA pentru un utilizator anume
$UserPrincipalName = "johndoe@example.com"
$StsUserObjectID = (Get-AzureADUser -Filter "UserPrincipalName eq '$UserPrincipalName'").ObjectId
$StrongAuthRequirements = @(@{"Location"=""; "SatisfactionFactor"="2"; "VerificationMethod"="1"};@{"Location"=""; "SatisfactionFactor"="2"; "VerificationMethod"="2"})
Set-AzureADUser -ObjectId $StsUserObjectID -StrongAuthenticationRequirements $StrongAuthRequirements
```
#### Role-Based Access Control (RBAC)

RBAC vă permite să definiți permisiuni detaliate pentru resursele Azure, astfel încât fiecare utilizator să aibă nivelul potrivit de acces. Atribuiți roluri utilizatorilor, grupurilor sau aplicațiilor pentru a gestiona accesul la resursele organizației. Pentru implementare, urmați [ghidul oficial](https://docs.microsoft.com/en-us/azure/role-based-access-control/overview) de la Microsoft.

Exemplu: Atribuiți un rol unui utilizator

```azurecli
# Atribuiți rolul Reader unui utilizator
az role assignment create --assignee johndoe@example.com --role "Reader" --scope "/subscriptions/your_subscription_id/resourceGroups/your_resource_group"
```
#### Monitorizarea activităților suspecte

Azure AD oferă funcțiile **Identity Protection** și **Conditional Access** pentru monitorizarea și gestionarea activităților suspecte. Identity Protection folosește învățarea automată pentru a detecta anomalii și conectări riscante. Conditional Access permite politici de control al accesului bazate pe factori precum dispozitivul, locația și riscul.

Pentru configurarea Azure AD Identity Protection, urmați [ghidul oficial](https://learn.microsoft.com/en-us/azure/active-directory/identity-protection/concept-identity-protection-b2b) de la Microsoft.

Exemplu: Creați o politică Conditional Access

```powershell
# Conectați-vă la Azure AD
Connect-AzureAD

# Creați o politică Conditional Access
$PolicyName = "BlockSignInFromUnknownLocations"
$PolicyDescription = "Blocați conectările utilizatorilor din locații necunoscute."
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
Consultați documentația oficială despre [Azure AD Identity Protection](https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/overview) și [Conditional Access](https://learn.microsoft.com/en-us/azure/active-directory/conditional-access/overview).

### Securitatea datelor

Protejarea datelor din cloud este esențială. Azure Security Center oferă **Azure Information Protection**, **Azure Storage Service Encryption** și **Azure Disk Encryption**. Aceste funcții ajută la criptarea datelor și gestionarea accesului la acestea.

#### Azure Information Protection

**Azure Information Protection (AIP)** este un serviciu cloud pentru clasificarea, etichetarea și protejarea documentelor și e-mailurilor confidențiale. AIP include etichete precum „Confidențial” și „Personal”, pe care le puteți adapta la nevoile organizației. Puteți configura aplicarea automată a etichetelor pe baza unor reguli predefinite. Pentru început, urmați [ghidul oficial](https://docs.microsoft.com/en-us/azure/information-protection/what-is-information-protection).

Exemplu: Creați o etichetă personalizată

```powershell
# Conectați-vă la serviciul AIP
Connect-AipService

# Creați o etichetă personalizată cu setări de protecție
$LabelName = "Sensibil - Numai pentru uz intern"
$LabelDescription = "Această etichetă aplică criptarea și o politică de acces doar pentru uz intern."
$LabelProtectionSettings = @{
    "ContentExpirationDate" = (Get-Date).AddMonths(6).ToUniversalTime();
    "OfflineAccessInterval" = "P7D";
    "UserRights" = @("domain\GroupA=View", "domain\GroupB=View,Edit,Print")
}
New-AipServiceLabel -Name $LabelName -Description $LabelDescription -ProtectionSettings $LabelProtectionSettings
```
#### Azure Storage Service Encryption

**Azure Storage Service Encryption (SSE)** criptează automat datele inactive din conturile Azure Storage, inclusiv Blob, File, Table și Queue. SSE folosește chei gestionate de Azure sau de client pentru criptarea la nivelul contului de stocare. Pentru activare, urmați [ghidul pas cu pas](https://docs.microsoft.com/en-us/azure/storage/common/storage-service-encryption) de la Microsoft.

Azure Information Protection este o denumire veche de produs. Documentația curentă despre disponibilitatea funcțiilor Sentinel îl listează ca retras. Consultați documentația Microsoft Purview Information Protection înainte de a începe o nouă implementare a etichetelor.

Exemplu: Activați SSE pentru un cont de stocare

```azurecli
# Activați SSE folosind chei gestionate de Azure
az storage account update --name mystorageaccount --resource-group myresourcegroup --encryption-services blob file
```
#### Azure Disk Encryption

**Azure Disk Encryption** protejează discurile mașinilor virtuale prin criptare cu BitLocker (Windows) sau dm-crypt (Linux). Azure Key Vault protejează cheile și secretele de criptare. Pentru activare, urmați [ghidul oficial](https://learn.microsoft.com/en-us/azure/virtual-machines/disk-encryption-overview) de la Microsoft.

Exemplu: Activați Azure Disk Encryption pentru o mașină virtuală

```azurecli
# Activați Azure Disk Encryption pentru o mașină virtuală Windows
az vm encryption enable --resource-group myResourceGroup --name myVM --disk-encryption-keyvault myKeyVault
```
Consultați documentația oficială despre [Azure Information Protection](https://docs.microsoft.com/en-us/azure/information-protection/what-is-information-protection), [Azure Storage Service Encryption](https://docs.microsoft.com/en-us/azure/storage/common/storage-service-encryption) și [Azure Disk Encryption](https://learn.microsoft.com/en-us/azure/virtual-machines/disk-encryption-overview).
______

## Detectarea și răspunsul la amenințări

Azure Security Center detectează amenințări potențiale și trimite alerte. Prin integrarea cu **Azure Sentinel**, puteți monitoriza, investiga și gestiona incidentele de securitate din întregul mediu.

### Detectarea amenințărilor

Azure Security Center folosește **Azure Defender** pentru a identifica amenințări potențiale. Azure Defender monitorizează resursele pentru indicatori de compromitere și oferă alerte și recomandări pentru răspuns. Pentru activare, urmați [ghidul oficial](https://docs.microsoft.com/en-us/azure/security-center/defender-for-cloud-enable).

Exemplu: Activați Azure Defender pentru un abonament

```azurecli
# Activați Azure Defender pentru un abonament
az security auto-provisioning-setting update --name default --auto-provision on
```
### Răspunsul la amenințări
Când detectați o amenințare, răspundeți rapid și eficient. Gestionarea **Security Incident** din Azure Security Center ajută la investigarea și gestionarea incidentelor. Puteți integra și **Azure Sentinel** pentru a crea playbook-uri automatizate și a coordona răspunsul. Consultați **documentația oficială** despre integrarea Azure Security Center cu Azure Sentinel.

Exemplu: Creați un playbook Logic App pentru Azure Sentinel
```azurecli
# Creați un grup de resurse
az group create --name MyResourceGroup --location EastUS

# Creați un Logic App
az logic workflow create --resource-group MyResourceGroup --location EastUS --name MyPlaybook --definition @playbook-definition.json
```
Fișierul `playbook-definition.json` trebuie să conțină definiția playbook-ului Logic App. Găsiți exemple în [depozitul Azure-Sentinel de pe GitHub](https://github.com/Azure/Azure-Sentinel/tree/master/Playbooks).

Combinați detectarea amenințărilor din Azure Security Center cu Azure Sentinel pentru a răspunde la amenințări din Azure. Consultați documentația oficială despre [Azure Defender](https://learn.microsoft.com/en-us/azure/defender-for-cloud/enable-enhanced-security) și [Azure Sentinel](https://docs.microsoft.com/en-us/azure/sentinel/overview).

Fluxul actual transmite alertele Defender for Cloud către Microsoft Sentinel prin [conectorul Defender for Cloud](https://learn.microsoft.com/en-us/azure/sentinel/connect-defender-for-cloud). Înainte de a vă baza pe automatizare, verificați conectorul, regulile de colectare a datelor, regulile analitice și fluxul incidentelor în portalul Defender sau Azure.
______

## Monitorizare și raportare

Monitorizarea și raportarea ajută la menținerea unui mediu cloud securizat. Azure Security Center oferă instrumente precum **Security Dashboard**, **Security Alerts** și **Compliance Reports**.

### Tabloul de bord de securitate

Security Dashboard din Azure Security Center prezintă postura de securitate. Afișează Secure Score, recomandările și alertele active. Tabloul de bord arată și situația conformității și permite urmărirea progresului în timp.

### Alerte de securitate

Azure Security Center generează alerte când detectează amenințări potențiale. Alertele oferă detalii despre amenințare și recomandări pentru reducerea riscului. Configurați notificări prin e-mail sau SMS ori integrați serviciul cu [Slack](https://slack.com/) sau [Microsoft Teams](https://www.microsoft.com/en-us/microsoft-teams/group-chat-software).

### Rapoarte de conformitate

Azure Security Center generează rapoarte pentru cadre de reglementare precum GDPR, HIPAA și PCI DSS. Folosiți-le pentru a urmări situația conformității organizației și a identifica aspectele care necesită îmbunătățiri.

______

## Bune practici pentru Azure Security Center

Aplicați aceste practici pentru a folosi eficient Azure Security Center:

1. **Activați Azure Security Center pentru toate abonamentele**: verificați că fiecare abonament Azure este protejat.
2. **Revizuiți regulat Secure Score**: urmăriți postura generală de securitate și identificați domeniile care necesită îmbunătățiri.
3. **Aplicați recomandările de securitate**: îmbunătățiți postura și reduceți riscurile urmând recomandările Azure Security Center.
4. **Monitorizați alertele de securitate**: revizuiți alertele și răspundeți pentru a reduce amenințările potențiale.
5. **Actualizați cerințele de conformitate**: revizuiți politicile și actualizați-le pentru a respecta cadrele de reglementare curente.

## Fluxul curent Defender for Cloud

Pentru o implementare actuală, urmați această ordine. Denumirile secțiunilor vechi ajută la căutările istorice, dar portalul și documentația folosesc terminologia Defender for Cloud.

1. **Inventariați abonamentele și conectorii.** Înregistrați abonamentele Azure, conectorii AWS sau GCP, proiectele DevOps și resursele esențiale.
2. **Activați planurile Defender necesare.** Alegeți planuri în funcție de încărcătura de lucru și confirmați licențierea înainte de activarea în abonamentele de producție.
3. **Revizuiți Cloud Secure Score și recomandările.** Prioritizați expunerea la Internet, riscurile de identitate, vulnerabilitățile exploatabile și lipsa jurnalizării. Scorul nu dovedește conformitatea completă.
4. **Configurați controalele Microsoft Entra.** Solicitați MFA rezistent la phishing pentru conturile importante, folosiți RBAC cu privilegii minime și revizuiți accesul privilegiat.
5. **Trimiteți alertele la Microsoft Sentinel.** Confirmați ingestia alertelor, regulile analitice, responsabilii, automatizarea răspunsului și retenția.
6. **Verificați din nou după modificări.** Revizuiți recomandările după aplicarea corecțiilor, schimbări de arhitectură, adăugarea conectorilor sau schimbarea planurilor.

## Listă practică de verificare

- **Identitate:** eliminați conturile vechi, reduceți accesul permanent de administrator și revizuiți excepțiile Conditional Access.
- **Rețea:** închideți porturile publice de administrare, restrângeți intervalele sursă NSG și verificați dacă jurnalele firewallului și WAF ajung în spațiul de monitorizare.
- **Date:** clasificați depozitele de date sensibile, confirmați criptarea și proprietatea cheilor și testați restaurarea copiilor de rezervă.
- **Detectare:** confirmați severitatea alertelor, direcționarea notificărilor, responsabilii incidentelor și playbook-urile de răspuns.
- **Guvernanță:** desemnați un responsabil, o dată de expirare a excepției și dovezile standardului cerut pentru fiecare inițiativă de politică.

______

## Referințe

- [Documentația Azure Security Center](https://docs.microsoft.com/en-us/azure/security-center/)
- [Serviciul Azure Policy](https://docs.microsoft.com/en-us/azure/governance/policy/)
- [NIST 800-53](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final)
- [CIS](https://www.cisecurity.org/)
- [ISO 27001](https://www.iso.org/isoiec-27001-information-security.html)
- [GDPR](https://gdpr.eu/)
- [HIPAA](https://www.hhs.gov/hipaa/index.html)
- [PCI DSS](https://www.pcisecuritystandards.org/)
