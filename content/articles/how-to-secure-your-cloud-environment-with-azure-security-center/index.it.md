---
title: "Azure Security Center: Proteggere l'ambiente cloud con sicurezza"
date: 2023-04-10
toc: true
draft: false
description: "Imparate a proteggere il vostro ambiente cloud utilizzando Azure Security Center, con best practice ed esempi reali."
tags: ["Azzurro", "Centro di sicurezza", "sicurezza del cloud", "Sentinella Azzurra", "Difensore dell'Azzurro", "sicurezza della rete", "gestione dell'identità", "sicurezza dei dati", "rilevamento delle minacce", "risposta alle minacce", "MFA", "RBAC", "NSG", "Firewall Azure", "WAF", "Azure AD", "Protezione delle informazioni di Azure", "Crittografia del servizio di archiviazione Azure", "Crittografia del disco di Azure"]
cover: "/img/cover/A_shield_icon_surrounded_by_cloud_symbols.png"
coverAlt: "Un'icona a forma di scudo circondata da simboli di nuvole, che rappresenta un ambiente cloud sicuro, con il logo del Centro sicurezza Azure sullo scudo."
coverCaption: ""
---

**Come proteggere l'ambiente cloud con Azure Security Center**

La protezione dell'ambiente cloud è essenziale per proteggere i dati, le applicazioni e l'infrastruttura dell'organizzazione dalle minacce. L'**Azure Security Center** di Microsoft è un potente strumento che vi aiuta a rafforzare la vostra posizione di sicurezza e a identificare rapidamente i potenziali rischi nel vostro ambiente Azure. In questo articolo, discuteremo di come proteggere il vostro ambiente cloud utilizzando Azure Security Center e tratteremo le best practice per l'implementazione di varie funzionalità di sicurezza. Inoltre, in questo articolo ci addentreremo in dettagli tecnici ed esempi per aiutarvi a capire meglio come proteggere il vostro ambiente cloud utilizzando Azure Security Center.

______

## Comprendere il Centro sicurezza di Azure

Azure Security Center è un **sistema unificato di gestione della sicurezza dell'infrastruttura** che consente di identificare e risolvere potenziali vulnerabilità nell'ambiente cloud. Offre diverse funzionalità, come il rilevamento delle minacce, la gestione della postura di sicurezza e la gestione della conformità, per garantire che il vostro ambiente Azure sia sempre sicuro.

La **Valutazione continua della sicurezza** e la **Protezione avanzata dalle minacce** sono due caratteristiche chiave di Azure Security Center. La valutazione continua della sicurezza aiuta a identificare potenziali problemi di sicurezza nell'ambiente, mentre la protezione avanzata dalle minacce aiuta a rilevare e rispondere a potenziali minacce.

______

## Implementazione dei criteri di sicurezza e degli standard di conformità

Azure Security Center consente di implementare e gestire i criteri di sicurezza nell'ambiente cloud. È possibile utilizzare il servizio **Azure Policy** per creare criteri di sicurezza personalizzati o utilizzare criteri integrati per applicare le best practice e gli standard di conformità. È inoltre possibile valutare la propria posizione di sicurezza rispetto a standard di settore quali[NIST 800-53](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final), [CIS](https://www.cisecurity.org/), and [ISO 27001](https://www.iso.org/isoiec-27001-information-security.html)

Azure Security Center offre anche funzionalità di gestione della conformità, consentendo di monitorare lo stato di conformità dell'organizzazione rispetto a vari quadri normativi, come ad esempio[GDPR](https://gdpr.eu/), [HIPAA](https://www.hhs.gov/hipaa/index.html), and [PCI DSS](https://www.pcisecuritystandards.org/)

______

## Protezione delle risorse Azure

**L'igiene della sicurezza delle risorse è un aspetto importante della protezione dell'ambiente cloud. L'Azure Security Center fornisce il **Secure Score**, una misurazione della postura di sicurezza, per aiutarvi a capire la sicurezza complessiva delle vostre risorse. Potete migliorare il vostro Secure Score seguendo le raccomandazioni fornite da Azure Security Center.

### Sicurezza di rete

L'implementazione di misure di sicurezza di rete adeguate, come **Gruppi di sicurezza di rete (NSG)**, **Azure Firewall** e **Web Application Firewall (WAF)**, è fondamentale per proteggere il vostro ambiente Azure da potenziali minacce. Questi strumenti aiutano a controllare il traffico di rete in entrata e in uscita, proteggendo le risorse da accessi non autorizzati e potenziali attacchi.

#### Gruppi di sicurezza di rete (NSG)

Gli NSG agiscono come un firewall virtuale per le risorse Azure, consentendo di definire regole che permettono o negano il traffico di rete da e verso le risorse. Ad esempio, è possibile creare un NSG con regole per consentire o negare un traffico specifico:

```azurecli
# Create a Network Security Group
az network nsg create --name MyNSG --resource-group MyResourceGroup

# Add rules to allow or deny traffic
az network nsg rule create --name MyNSGRule --nsg-name MyNSG --priority 100 --resource-group MyResourceGroup --access Allow --protocol Tcp --direction Inbound --source-address-prefixes '*' --source-port-ranges '*' --destination-address-prefixes '*' --destination-port-ranges '80'
```
Per saperne di più[Network Security Groups](https://docs.microsoft.com/en-us/azure/virtual-network/security-overview) nella documentazione ufficiale.

#### Azure Firewall
Azure Firewall è un servizio di sicurezza di rete gestito e basato sul cloud che protegge le risorse di Azure. Offre funzionalità avanzate come il filtraggio basato sulle informazioni sulle minacce, le categorie web e la registrazione e l'analisi centralizzate. Per configurare Azure Firewall, è possibile seguire le seguenti istruzioni[quickstart instructions](https://learn.microsoft.com/en-us/azure/firewall-manager/quick-firewall-policy-bicep)

#### Web Application Firewall (WAF)
Il Web Application Firewall (WAF) è una funzionalità di **Azure Application Gateway** che fornisce protezione alle applicazioni web contro gli exploit web più comuni, come SQL injection, cross-site scripting e altre minacce. Il WAF può essere facilmente integrato con le applicazioni web esistenti ed è possibile configurare regole personalizzate per proteggere da specifici modelli di attacco.

Ecco un esempio di come creare un Application Gateway con WAF abilitato:
```azurecli
# Create a WAF policy
az network application-gateway waf-policy create --name MyWafPolicy --resource-group MyResourceGroup --location EastUS

# Create a virtual network and subnet
az network vnet create --name MyVNet --resource-group MyResourceGroup --location EastUS --address-prefix 10.0.0.0/16
az network vnet subnet create --name MySubnet --resource-group MyResourceGroup --vnet-name MyVNet --address-prefix 10.0.0.0/24

# Create a public IP address
az network public-ip create --name MyPublicIP --resource-group MyResourceGroup --location EastUS --sku Standard

# Create an Application Gateway with WAF enabled
az network application-gateway create --name MyAppGateway --resource-group MyResourceGroup --location EastUS --vnet-name MyVNet --subnet MySubnet --public-ip-address MyPublicIP --http-settings-cookie-based-affinity Enabled --sku WAF_v2 --waf-policy MyWafPolicy

```
Per saperne di più[Web Application Firewall](https://docs.microsoft.com/en-us/azure/web-application-firewall/ag/ag-overview) nella documentazione ufficiale.

### Gestione dell'identità e degli accessi

L'**Azure Active Directory (Azure AD)** è un componente essenziale per la protezione dell'ambiente cloud. Azure Security Center fornisce raccomandazioni per migliorare la gestione dell'identità e dell'accesso, come l'abilitazione dell'autenticazione a più fattori (MFA)**, l'implementazione del controllo dell'accesso basato sui ruoli (RBAC)** e il monitoraggio delle attività sospette.

#### Autenticazione a più fattori (MFA)

L'MFA aggiunge un ulteriore livello di sicurezza agli account Azure AD richiedendo agli utenti di fornire due o più forme di verifica prima di concedere l'accesso. È possibile abilitare l'MFA per l'organizzazione seguendo la procedura di cui sopra.[step-by-step guide](https://docs.microsoft.com/en-us/azure/active-directory/authentication/tutorial-enable-azure-mfa) fornito da Microsoft.

Esempio: Abilitare l'MFA per un utente

```powershell
# Connect to Azure AD
Connect-AzureAD

# Enable MFA for a specific user
$UserPrincipalName = "johndoe@example.com"
$StsUserObjectID = (Get-AzureADUser -Filter "UserPrincipalName eq '$UserPrincipalName'").ObjectId
$StrongAuthRequirements = @(@{"Location"=""; "SatisfactionFactor"="2"; "VerificationMethod"="1"};@{"Location"=""; "SatisfactionFactor"="2"; "VerificationMethod"="2"})
Set-AzureADUser -ObjectId $StsUserObjectID -StrongAuthenticationRequirements $StrongAuthRequirements
```
#### Controllo dell'accesso basato sui ruoli (RBAC)
RBAC consente di definire autorizzazioni granulari per le risorse di Azure, assicurando che gli utenti abbiano il livello di accesso appropriato. È possibile assegnare ruoli a utenti, gruppi o applicazioni per gestire il loro accesso alle risorse dell'organizzazione. Per implementare RBAC, seguite la procedura[official guide](https://docs.microsoft.com/en-us/azure/role-based-access-control/overview) da Microsoft.

Esempio: Assegnare un ruolo a un utente
```azurecli
# Assign a Reader role to a user
az role assignment create --assignee johndoe@example.com --role "Reader" --scope "/subscriptions/your_subscription_id/resourceGroups/your_resource_group"
```
#### Monitoraggio delle attività sospette
Azure AD offre funzionalità come **Protezione dell'identità** e **Accesso condizionato** che aiutano a monitorare e rispondere alle attività sospette. Identity Protection utilizza algoritmi di apprendimento automatico per rilevare anomalie e tentativi di accesso rischiosi, mentre Conditional Access consente di impostare criteri che controllano l'accesso in base a fattori quali il dispositivo, la posizione e il livello di rischio.

Per configurare Azure AD Identity Protection, seguite la seguente procedura[official guide](https://learn.microsoft.com/en-us/azure/active-directory/identity-protection/concept-identity-protection-b2b) da Microsoft.

Esempio: Creare un criterio di accesso condizionato

```powershell
# Connect to Azure AD
Connect-AzureAD

# Create a Conditional Access policy
$PolicyName = "BlockSignInFromUnknownLocations"
$PolicyDescription = "Block sign-ins for users from unknown locations."
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
Per saperne di più[Azure AD Identity Protection](https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/overview) and [Conditional Access](https://learn.microsoft.com/en-us/azure/active-directory/conditional-access/overview) nella documentazione ufficiale.


### Sicurezza dei dati

La protezione dei dati nel cloud è fondamentale. Azure Security Center offre diverse funzioni di sicurezza dei dati, come **Azure Information Protection**, **Azure Storage Service Encryption** e **Azure Disk Encryption**. Queste funzioni consentono di crittografare e gestire l'accesso ai dati, garantendo la sicurezza delle informazioni sensibili.

#### Protezione delle informazioni di Azure

**Azure Information Protection (AIP)** è una soluzione basata sul cloud che aiuta a classificare, etichettare e proteggere i documenti e le e-mail sensibili. AIP fornisce una serie di etichette integrate, come "Riservato" e "Personale", che possono essere personalizzate in base alle esigenze dell'organizzazione. È anche possibile configurare AIP per applicare automaticamente le etichette in base a regole predefinite. Per iniziare a usare AIP, seguite la procedura[official guide](https://docs.microsoft.com/en-us/azure/information-protection/what-is-information-protection)

Esempio: Creazione di un'etichetta personalizzata

```powershell
# Connect to the AIP service
Connect-AipService

# Create a custom label with protection settings
$LabelName = "Sensitive - Internal Use Only"
$LabelDescription = "This label applies encryption and an access policy for internal use only."
$LabelProtectionSettings = @{
    "ContentExpirationDate" = (Get-Date).AddMonths(6).ToUniversalTime();
    "OfflineAccessInterval" = "P7D";
    "UserRights" = @("domain\GroupA=View", "domain\GroupB=View,Edit,Print")
}
New-AipServiceLabel -Name $LabelName -Description $LabelDescription -ProtectionSettings $LabelProtectionSettings
```
#### Crittografia del servizio di archiviazione di Azure
L'opzione **Azure Storage Service Encryption (SSE**) cripta automaticamente i dati a riposo negli account di Azure Storage, compresi gli archivi Blob, File, Table e Queue. SSE utilizza chiavi gestite da Azure o dal cliente per fornire la crittografia a livello di account di archiviazione. Per abilitare SSE, seguire la procedura[step-by-step guide](https://docs.microsoft.com/en-us/azure/storage/common/storage-service-encryption) fornito da Microsoft.

Esempio: Abilitazione di SSE per un account di archiviazione

```azurecli
# Enable SSE using Azure-managed keys
az storage account update --name mystorageaccount --resource-group myresourcegroup --encryption-services blob file
```
#### Crittografia disco di Azure
La **Crittografia disco di Azure** consente di proteggere i dischi delle macchine virtuali crittografandoli con BitLocker (Windows) o dm-crypt (Linux). Le chiavi di crittografia e i segreti sono protetti da Azure Key Vault, garantendo la sicurezza dei dati a riposo. Per abilitare la crittografia del disco di Azure, seguire la procedura[official guide](https://learn.microsoft.com/en-us/azure/virtual-machines/disk-encryption-overview) da Microsoft.

Esempio: Abilitazione di Azure Disk Encryption per una macchina virtuale
```azurecli
# Enable Azure Disk Encryption for a Windows VM
az vm encryption enable --resource-group myResourceGroup --name myVM --disk-encryption-keyvault myKeyVault
```
Per saperne di più[Azure Information Protection](https://docs.microsoft.com/en-us/azure/information-protection/what-is-information-protection), [Azure Storage Service Encryption](https://docs.microsoft.com/en-us/azure/storage/common/storage-service-encryption), and [Azure Disk Encryption](https://learn.microsoft.com/en-us/azure/virtual-machines/disk-encryption-overview) nella documentazione ufficiale.
______

## Rilevare e rispondere alle minacce

Azure Security Center utilizza funzionalità avanzate di rilevamento delle minacce per identificare e avvisare l'utente di potenziali minacce. Integrandosi con **Azure Sentinel**, è possibile monitorare, indagare e rispondere agli incidenti di sicurezza nell'intero ambiente.

### Rilevamento delle minacce

Azure Security Center utilizza **Azure Defender**, un insieme di funzionalità avanzate di rilevamento delle minacce, per identificare potenziali minacce alla sicurezza. Azure Defender monitora le risorse alla ricerca di indicatori di compromissione e fornisce avvisi e raccomandazioni per aiutarvi a rispondere alle potenziali minacce. Per abilitare Azure Defender, seguire la procedura[official guide](https://docs.microsoft.com/en-us/azure/security-center/defender-for-cloud-enable)

Esempio: Abilitazione di Azure Defender per un abbonamento

```azurecli
# Enable Azure Defender for a subscription
az security auto-provisioning-setting update --name default --auto-provision on
```
### Risposta alle minacce
Quando viene rilevata una minaccia, è essenziale rispondere in modo rapido ed efficace. Azure Security Center offre la gestione degli **incidenti di sicurezza**, che aiuta a indagare e rispondere agli incidenti di sicurezza. È inoltre possibile integrarsi con **Azure Sentinel** per creare playbook automatizzati e orchestrare la risposta agli incidenti di sicurezza. Per saperne di più sull'integrazione di Azure Security Center con Azure Sentinel, consultate la **documentazione ufficiale**.

Esempio: Creare un playbook di Logic App per Azure Sentinel
```azurecli
# Create a resource group
az group create --name MyResourceGroup --location EastUS

# Create a Logic App
az logic workflow create --resource-group MyResourceGroup --location EastUS --name MyPlaybook --definition @playbook-definition.json
```
Il`playbook-definition.json` deve contenere la definizione del playbook di Logic App. Si possono trovare esempi di playbook per Azure Sentinel nel file[Azure-Sentinel GitHub repository](https://github.com/Azure/Azure-Sentinel/tree/master/Playbooks)

Sfruttando le funzionalità di rilevamento delle minacce di Azure Security Center e integrandosi con Azure Sentinel, è possibile creare una solida strategia di sicurezza per rilevare e rispondere alle minacce nell'ambiente Azure. Per saperne di più[Azure Defender](https://learn.microsoft.com/en-us/azure/defender-for-cloud/enable-enhanced-security) and [Azure Sentinel](https://docs.microsoft.com/en-us/azure/sentinel/overview) nella documentazione ufficiale.
______

## Monitoraggio e reportistica

Il monitoraggio e il reporting sono componenti essenziali per mantenere un ambiente cloud sicuro. Azure Security Center fornisce diversi strumenti per il monitoraggio e la creazione di report, come **Security Dashboard**, **Avvisi di sicurezza** e **Rapporti di conformità**.

### Cruscotto di sicurezza

La Security Dashboard di Azure Security Center fornisce una panoramica completa della vostra posizione di sicurezza. Mostra il punteggio di sicurezza, le raccomandazioni di sicurezza e gli avvisi di sicurezza attivi. Il dashboard fornisce anche informazioni sullo stato di conformità e consente di monitorare i progressi nel tempo.

### Avvisi di sicurezza

Azure Security Center genera avvisi di sicurezza quando vengono rilevate potenziali minacce. Questi avvisi forniscono informazioni dettagliate sulla minaccia e consigli per ridurre il rischio. È possibile configurare il Centro sicurezza di Azure per inviare notifiche via e-mail, SMS o integrarsi con strumenti di terze parti quali[Slack](https://slack.com/) or [Microsoft Teams](https://www.microsoft.com/en-us/microsoft-teams/group-chat-software)

### Rapporti di conformità

Azure Security Center consente di generare rapporti di conformità per vari quadri normativi, come GDPR, HIPAA e PCI DSS. Questi rapporti aiutano a monitorare lo stato di conformità dell'organizzazione e a identificare le aree che richiedono miglioramenti.

______

## Migliori pratiche per Azure Security Center

Per ottenere il massimo da Azure Security Center, considerate l'implementazione delle seguenti best practice:

1. **Abilitare Azure Security Center su tutte le sottoscrizioni**: Assicurarsi che tutte le sottoscrizioni Azure siano protette da Azure Security Center è fondamentale per mantenere un ambiente cloud sicuro.
2. **Controllare regolarmente il vostro Secure Score**: Il monitoraggio del vostro Secure Score vi aiuta a comprendere la vostra postura di sicurezza complessiva e a identificare le aree che richiedono miglioramenti.
3. **Implementare le raccomandazioni di sicurezza**: L'applicazione delle raccomandazioni di sicurezza fornite da Azure Security Center vi aiuta a migliorare la vostra posizione di sicurezza e a ridurre i rischi potenziali.
4. **Monitorare gli avvisi di sicurezza**: Esaminate e rispondete regolarmente agli avvisi di sicurezza per ridurre le minacce potenziali e mantenere un ambiente sicuro.
5. **Mantenersi aggiornati sui requisiti di conformità**: Assicuratevi che la vostra organizzazione sia conforme ai più recenti quadri normativi rivedendo e aggiornando regolarmente le vostre politiche di conformità.

______

## Riferimenti

-[Azure Security Center Documentation](https://docs.microsoft.com/en-us/azure/security-center/)
-[Azure Policy Service](https://docs.microsoft.com/en-us/azure/governance/policy/)
-[NIST 800-53](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final)
-[CIS](https://www.cisecurity.org/)
-[ISO 27001](https://www.iso.org/isoiec-27001-information-security.html)
-[GDPR](https://gdpr.eu/)
-[HIPAA](https://www.hhs.gov/hipaa/index.html)
-[PCI DSS](https://www.pcisecuritystandards.org/)

