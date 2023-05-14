---
title: "Centrum Bezpieczeństwa Azure: Zabezpiecz swoje środowisko chmurowe w sposób pewny"
date: 2023-04-10
toc: true
draft: false
description: "Dowiedz się, jak zabezpieczyć środowisko chmurowe za pomocą Azure Security Center, korzystając z najlepszych praktyk i rzeczywistych przykładów."
tags: ["Lazurowy", "Centrum Bezpieczeństwa", "bezpieczeństwo w chmurze", "Lazurowy Sentinel", "Azure Defender", "bezpieczeństwo sieci", "zarządzanie tożsamością", "bezpieczeństwo danych", "wykrywanie zagrożeń", "reagowanie na zagrożenia", "MFA", "RBAC", "NSGs", "Azure Firewall", "WAF", "Azure AD", "Ochrona informacji w środowisku Azure", "Szyfrowanie usługi Azure Storage", "Szyfrowanie dysków w środowisku Azure"]
cover: "/img/cover/A_shield_icon_surrounded_by_cloud_symbols.png"
coverAlt: "Ikona tarczy otoczona symbolami chmur, reprezentująca bezpieczne środowisko chmurowe, z logo Azure Security Center na tarczy."
coverCaption: ""
---

**Jak zabezpieczyć środowisko chmurowe za pomocą Azure Security Center**.

Zabezpieczenie środowiska chmury jest niezbędne do ochrony danych, aplikacji i infrastruktury organizacji przed zagrożeniami. Centrum Bezpieczeństwa Azure** firmy Microsoft to potężne narzędzie, które pomaga wzmocnić postawę bezpieczeństwa i szybko zidentyfikować potencjalne zagrożenia w środowisku Azure. W tym artykule omówimy, jak zabezpieczyć środowisko chmurowe za pomocą Azure Security Center, oraz przedstawimy najlepsze praktyki wdrażania różnych funkcji bezpieczeństwa. Dodatkowo w tym artykule zanurzymy się w więcej szczegółów technicznych i przykładów, aby pomóc lepiej zrozumieć, jak zabezpieczyć środowisko chmury za pomocą Azure Security Center.

______

## Zrozumieć Azure Security Center

Azure Security Center to **unifikowany system zarządzania bezpieczeństwem infrastruktury**, który pomaga identyfikować i eliminować potencjalne luki w środowisku chmury. Oferuje on kilka funkcji, takich jak wykrywanie zagrożeń, zarządzanie postawą bezpieczeństwa i zarządzanie zgodnością, aby zapewnić, że środowisko Azure jest zawsze bezpieczne.

**Ciągła ocena bezpieczeństwa** i zaawansowana ochrona przed zagrożeniami** to dwie kluczowe funkcje Azure Security Center. Ciągła ocena bezpieczeństwa pomaga zidentyfikować potencjalne problemy z bezpieczeństwem w środowisku, natomiast zaawansowana ochrona przed zagrożeniami pomaga wykrywać i reagować na potencjalne zagrożenia.

______

## Wdrażanie polityk bezpieczeństwa i standardów zgodności

Azure Security Center umożliwia wdrożenie i zarządzanie zasadami bezpieczeństwa w całym środowisku chmury. Za pomocą usługi **Azure Policy** można tworzyć niestandardowe polityki bezpieczeństwa lub używać wbudowanych polityk w celu egzekwowania najlepszych praktyk i standardów zgodności. Można również ocenić stan bezpieczeństwa w odniesieniu do standardów branżowych, takich jak[NIST 800-53](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final), [CIS](https://www.cisecurity.org/), and [ISO 27001](https://www.iso.org/isoiec-27001-information-security.html)

Azure Security Center oferuje również funkcje zarządzania zgodnością, pozwalające śledzić status zgodności organizacji z różnymi ramami prawnymi, takimi jak[GDPR](https://gdpr.eu/), [HIPAA](https://www.hhs.gov/hipaa/index.html), and [PCI DSS](https://www.pcisecuritystandards.org/)

______

## Securing Your Azure Resources

**Higiena bezpieczeństwa zasobów** jest ważnym aspektem zabezpieczania środowiska chmury. Azure Security Center zapewnia **Secure Score**, pomiar postawy bezpieczeństwa, aby pomóc zrozumieć ogólne bezpieczeństwo zasobów. Możesz poprawić swój Secure Score, stosując się do zaleceń dostarczonych przez Azure Security Center.

### Bezpieczeństwo sieci

Wdrożenie odpowiednich środków bezpieczeństwa sieci, takich jak **Network Security Groups (NSGs)**, **Azure Firewall** i **Web Application Firewall (WAF)**, jest kluczowe dla ochrony środowiska Azure przed potencjalnymi zagrożeniami. Narzędzia te pomagają kontrolować przychodzący i wychodzący ruch sieciowy, chroniąc zasoby przed nieautoryzowanym dostępem i potencjalnymi atakami.

#### Grupy zabezpieczeń sieciowych (NSG)

Grupy NSG działają jak wirtualna zapora dla zasobów Azure, umożliwiając definiowanie reguł, które zezwalają lub odmawiają ruchu sieciowego do i z zasobów. Na przykład, można utworzyć NSG z regułami zezwalającymi lub odmawiającymi określonego ruchu:

```azurecli
# Create a Network Security Group
az network nsg create --name MyNSG --resource-group MyResourceGroup

# Add rules to allow or deny traffic
az network nsg rule create --name MyNSGRule --nsg-name MyNSG --priority 100 --resource-group MyResourceGroup --access Allow --protocol Tcp --direction Inbound --source-address-prefixes '*' --source-port-ranges '*' --destination-address-prefixes '*' --destination-port-ranges '80'
```
Dowiedz się więcej o[Network Security Groups](https://docs.microsoft.com/en-us/azure/virtual-network/security-overview) w oficjalnej dokumentacji.

#### Azure Firewall
Azure Firewall to zarządzana, oparta na chmurze usługa bezpieczeństwa sieciowego, która chroni zasoby Azure. Zapewnia ona zaawansowane funkcje, takie jak filtrowanie oparte na inteligencji zagrożeń, kategorie stron internetowych oraz scentralizowane rejestrowanie i analiza. Aby skonfigurować usługę Azure Firewall, można wykonać następujące czynności[quickstart instructions](https://learn.microsoft.com/en-us/azure/firewall-manager/quick-firewall-policy-bicep)

#### Web Application Firewall (WAF)
Web Application Firewall (WAF) to funkcja **Azure Application Gateway**, która zapewnia ochronę aplikacji internetowych przed typowymi atakami typu SQL injection, cross-site scripting i innymi zagrożeniami. Funkcja WAF może być łatwo zintegrowana z istniejącymi aplikacjami internetowymi, a użytkownik może skonfigurować niestandardowe reguły w celu ochrony przed określonymi wzorcami ataków.

Oto przykład tworzenia bramy aplikacji z włączoną funkcją WAF:
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
Dowiedz się więcej o[Web Application Firewall](https://docs.microsoft.com/en-us/azure/web-application-firewall/ag/ag-overview) w oficjalnej dokumentacji.

### Zarządzanie tożsamością i dostępem

Usługa **Azure Active Directory (Azure AD)** jest podstawowym elementem zabezpieczenia środowiska chmury. Azure Security Center zapewnia zalecenia dotyczące poprawy zarządzania tożsamością i dostępem, takie jak włączenie **Multi-Factor Authentication (MFA)**, wdrożenie **Role-Based Access Control (RBAC)** oraz monitorowanie podejrzanych działań.

#### Uwierzytelnianie wieloczynnikowe (MFA)

Funkcja MFA zapewnia dodatkową warstwę bezpieczeństwa kont w usłudze Azure AD, wymagając od użytkowników dwóch lub więcej form weryfikacji przed przyznaniem dostępu. Funkcję MFA można włączyć w swojej organizacji, postępując zgodnie z następującymi zasadami[step-by-step guide](https://docs.microsoft.com/en-us/azure/active-directory/authentication/tutorial-enable-azure-mfa) dostarczonych przez Microsoft.

Przykład: Włączenie MFA dla użytkownika

```powershell
# Connect to Azure AD
Connect-AzureAD

# Enable MFA for a specific user
$UserPrincipalName = "johndoe@example.com"
$StsUserObjectID = (Get-AzureADUser -Filter "UserPrincipalName eq '$UserPrincipalName'").ObjectId
$StrongAuthRequirements = @(@{"Location"=""; "SatisfactionFactor"="2"; "VerificationMethod"="1"};@{"Location"=""; "SatisfactionFactor"="2"; "VerificationMethod"="2"})
Set-AzureADUser -ObjectId $StsUserObjectID -StrongAuthenticationRequirements $StrongAuthRequirements
```
#### Role-Based Access Control (RBAC)
RBAC pozwala zdefiniować granularne uprawnienia do zasobów Azure, zapewniając użytkownikom odpowiedni poziom dostępu. Możesz przypisać role do użytkowników, grup lub aplikacji, aby zarządzać ich dostępem do zasobów w Twojej organizacji. Aby wdrożyć RBAC, należy wykonać następujące czynności[official guide](https://docs.microsoft.com/en-us/azure/role-based-access-control/overview) od Microsoftu.

Przykład: Przypisanie roli do użytkownika
```azurecli
# Assign a Reader role to a user
az role assignment create --assignee johndoe@example.com --role "Reader" --scope "/subscriptions/your_subscription_id/resourceGroups/your_resource_group"
```
#### Monitorowanie podejrzanych działań
Azure AD oferuje funkcje takie jak **Ochrona tożsamości** i **Dostęp warunkowy**, które pomagają monitorować i reagować na podejrzane działania. Funkcja Identity Protection wykorzystuje algorytmy uczenia maszynowego w celu wykrywania anomalii i ryzykownych prób logowania, natomiast funkcja Conditional Access pozwala określić zasady kontroli dostępu w oparciu o takie czynniki, jak urządzenie, lokalizacja i poziom ryzyka.

Aby skonfigurować usługę Azure AD Identity Protection, należy wykonać następujące czynności[official guide](https://learn.microsoft.com/en-us/azure/active-directory/identity-protection/concept-identity-protection-b2b) od Microsoftu.

Przykład: Tworzenie polityki dostępu warunkowego (Conditional Access)

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
Dowiedz się więcej o[Azure AD Identity Protection](https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/overview) and [Conditional Access](https://learn.microsoft.com/en-us/azure/active-directory/conditional-access/overview) w oficjalnej dokumentacji.


### Bezpieczeństwo danych

Ochrona danych w chmurze ma kluczowe znaczenie. Azure Security Center oferuje kilka funkcji bezpieczeństwa danych, takich jak **Azure Information Protection**, **Azure Storage Service Encryption** i **Azure Disk Encryption**. Funkcje te pomagają szyfrować i zarządzać dostępem do danych, zapewniając, że wrażliwe informacje pozostają bezpieczne.

#### Azure Information Protection

**Azure Information Protection (AIP)** to oparte na chmurze rozwiązanie, które pomaga klasyfikować, oznaczać i chronić poufne dokumenty i wiadomości e-mail. AIP zapewnia zestaw wbudowanych etykiet, takich jak "Poufne" i "Osobiste", które można dostosować do potrzeb organizacji. Można również skonfigurować AIP tak, aby automatycznie stosował etykiety na podstawie wcześniej zdefiniowanych reguł. Aby rozpocząć pracę z AIP, należy postępować zgodnie z[official guide](https://docs.microsoft.com/en-us/azure/information-protection/what-is-information-protection)

Przykład: Tworzenie etykiety niestandardowej

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
#### Szyfrowanie usługi Azure Storage
**Usługa Azure Storage Service Encryption (SSE**) automatycznie szyfruje dane w stanie spoczynku na kontach Azure Storage, w tym na kontach Blob, File, Table i Queue. SSE wykorzystuje klucze zarządzane przez Azure lub klucze zarządzane przez klienta, aby zapewnić szyfrowanie na poziomie konta pamięci masowej. Aby włączyć SSE, wykonaj następujące czynności[step-by-step guide](https://docs.microsoft.com/en-us/azure/storage/common/storage-service-encryption) dostarczonych przez Microsoft.

Przykład: Włączenie SSE dla konta pamięci masowej

```azurecli
# Enable SSE using Azure-managed keys
az storage account update --name mystorageaccount --resource-group myresourcegroup --encryption-services blob file
```
#### Azure Disk Encryption
**Azure Disk Encryption** pomaga zabezpieczyć dyski maszyn wirtualnych poprzez zaszyfrowanie ich za pomocą BitLocker (Windows) lub dm-crypt (Linux). Klucze szyfrujące i sekrety są chronione przez Azure Key Vault, dzięki czemu dane są zabezpieczone w spoczynku. Aby włączyć funkcję Azure Disk Encryption, wykonaj następujące czynności[official guide](https://learn.microsoft.com/en-us/azure/virtual-machines/disk-encryption-overview) od Microsoftu.

Przykład: Włączenie Azure Disk Encryption dla maszyny wirtualnej
```azurecli
# Enable Azure Disk Encryption for a Windows VM
az vm encryption enable --resource-group myResourceGroup --name myVM --disk-encryption-keyvault myKeyVault
```
Dowiedz się więcej o[Azure Information Protection](https://docs.microsoft.com/en-us/azure/information-protection/what-is-information-protection), [Azure Storage Service Encryption](https://docs.microsoft.com/en-us/azure/storage/common/storage-service-encryption), and [Azure Disk Encryption](https://learn.microsoft.com/en-us/azure/virtual-machines/disk-encryption-overview) w oficjalnej dokumentacji.
______

## Wykrywanie i reagowanie na zagrożenia

Centrum zabezpieczeń Azure wykorzystuje zaawansowane funkcje wykrywania zagrożeń w celu identyfikacji i ostrzegania o potencjalnych zagrożeniach. Dzięki integracji z **Azure Sentinel** można monitorować, badać i reagować na incydenty bezpieczeństwa w całym środowisku.

### Wykrywanie zagrożeń

Centrum zabezpieczeń Azure wykorzystuje **Azure Defender**, zestaw zaawansowanych funkcji wykrywania zagrożeń, w celu identyfikacji potencjalnych zagrożeń bezpieczeństwa. Program Azure Defender monitoruje zasoby pod kątem wskaźników zagrożenia i dostarcza ostrzeżenia oraz zalecenia, które pomagają w reagowaniu na potencjalne zagrożenia. Aby włączyć program Azure Defender, należy wykonać następujące czynności[official guide](https://docs.microsoft.com/en-us/azure/security-center/defender-for-cloud-enable)

Przykład: Włączenie Azure Defender dla subskrypcji

```azurecli
# Enable Azure Defender for a subscription
az security auto-provisioning-setting update --name default --auto-provision on
```
### Reakcja na zagrożenia
Po wykryciu zagrożenia konieczna jest szybka i skuteczna reakcja. Azure Security Center zapewnia **Zarządzanie incydentami bezpieczeństwa**, które pomaga badać i reagować na incydenty bezpieczeństwa. Można również zintegrować się z **Azure Sentinel**, aby utworzyć zautomatyzowane zestawy działań i zaaranżować reakcję na incydenty bezpieczeństwa. Więcej informacji o integracji Azure Security Center z Azure Sentinel można znaleźć w **oficjalnej dokumentacji**.

Przykład: Utwórz playbook Logic App dla Azure Sentinel
```azurecli
# Create a resource group
az group create --name MyResourceGroup --location EastUS

# Create a Logic App
az logic workflow create --resource-group MyResourceGroup --location EastUS --name MyPlaybook --definition @playbook-definition.json
```
Na stronie`playbook-definition.json` Plik powinien zawierać definicję playbooka Logic App. Przykłady playbooków dla Azure Sentinel można znaleźć w dokumencie[Azure-Sentinel GitHub repository](https://github.com/Azure/Azure-Sentinel/tree/master/Playbooks)

Wykorzystując możliwości wykrywania zagrożeń przez Azure Security Center i integrując się z programem Azure Sentinel, można stworzyć solidną strategię bezpieczeństwa w celu wykrywania i reagowania na zagrożenia w środowisku Azure. Dowiedz się więcej o[Azure Defender](https://learn.microsoft.com/en-us/azure/defender-for-cloud/enable-enhanced-security) and [Azure Sentinel](https://docs.microsoft.com/en-us/azure/sentinel/overview) w oficjalnej dokumentacji.
______

## Monitoring i raportowanie

Monitorowanie i raportowanie to istotne elementy utrzymania bezpiecznego środowiska chmury. Azure Security Center zapewnia kilka narzędzi do monitorowania i raportowania, takich jak **Security Dashboard**, **Alerty bezpieczeństwa** i **Raporty zgodności**.

### Security Dashboard

Security Dashboard w Azure Security Center zapewnia kompleksowy przegląd stanu bezpieczeństwa. Wyświetlany jest wynik Secure Score, zalecenia dotyczące bezpieczeństwa oraz aktywne alerty bezpieczeństwa. Pulpit nawigacyjny zapewnia również wgląd w status zgodności i pozwala śledzić postępy w czasie.

### Alerty bezpieczeństwa

Azure Security Center generuje alerty bezpieczeństwa w przypadku wykrycia potencjalnych zagrożeń. Alerty te dostarczają szczegółowych informacji o zagrożeniu, a także zaleceń dotyczących ograniczania ryzyka. Można skonfigurować Azure Security Center do wysyłania powiadomień za pośrednictwem poczty elektronicznej, wiadomości SMS lub zintegrować się z narzędziami innych firm, np.[Slack](https://slack.com/) or [Microsoft Teams](https://www.microsoft.com/en-us/microsoft-teams/group-chat-software)

### Raporty zgodności

Azure Security Center umożliwia generowanie raportów zgodności dla różnych ram regulacyjnych, takich jak GDPR, HIPAA i PCI DSS. Raporty te pomagają śledzić status zgodności organizacji i identyfikować obszary, które wymagają poprawy.

______

## Najlepsze praktyki dla Azure Security Center

Aby w pełni wykorzystać możliwości Azure Security Center, rozważ wdrożenie następujących najlepszych praktyk:

1. **Włącz Azure Security Center na wszystkich swoich subskrypcjach**: Zapewnienie, że wszystkie Twoje subskrypcje Azure są chronione przez Azure Security Center jest kluczowe dla utrzymania bezpiecznego środowiska chmury.
2. **Regularnie przeglądaj swój Secure Score**: Monitorowanie Secure Score pomaga zrozumieć ogólną postawę bezpieczeństwa i zidentyfikować obszary, które wymagają poprawy.
3. **Wdrażanie zaleceń dotyczących bezpieczeństwa**: Zastosowanie się do zaleceń dotyczących bezpieczeństwa dostarczonych przez Azure Security Center pomaga poprawić postawę bezpieczeństwa i zmniejszyć potencjalne ryzyko.
4. **Monitorowanie alertów bezpieczeństwa**: Regularnie przeglądaj i reaguj na alerty bezpieczeństwa, aby złagodzić potencjalne zagrożenia i utrzymać bezpieczne środowisko.
5. **Bądź na bieżąco z wymogami zgodności**: Zapewnij, że Twoja organizacja pozostaje zgodna z najnowszymi ramami regulacyjnymi poprzez regularny przegląd i aktualizację polityki zgodności.

______

## Referencje

-[Azure Security Center Documentation](https://docs.microsoft.com/en-us/azure/security-center/)
-[Azure Policy Service](https://docs.microsoft.com/en-us/azure/governance/policy/)
-[NIST 800-53](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final)
-[CIS](https://www.cisecurity.org/)
-[ISO 27001](https://www.iso.org/isoiec-27001-information-security.html)
-[GDPR](https://gdpr.eu/)
-[HIPAA](https://www.hhs.gov/hipaa/index.html)
-[PCI DSS](https://www.pcisecuritystandards.org/)

