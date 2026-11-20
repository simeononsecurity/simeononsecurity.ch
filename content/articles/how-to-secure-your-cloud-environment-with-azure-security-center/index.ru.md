---
title: "Защитите облачную среду с помощью Microsoft Defender for Cloud"
date: 2023-04-10
lastmod: 2026-11-20
toc: true
draft: false
description: "Защитите рабочие нагрузки Azure с помощью Microsoft Defender for Cloud. Изучите прежние термины Azure Security Center, рекомендации, политики и этапы реагирования."
tags: ["Azure", "Security Center", "безопасность облака", "Azure Sentinel", "Azure Defender", "безопасность сети", "управление удостоверениями", "защита данных", "обнаружение угроз", "реагирование на угрозы", "MFA", "RBAC", "NSGs", "Azure Firewall", "WAF", "Azure AD", "Azure Information Protection", "Azure Storage Service Encryption", "Azure Disk Encryption"]
cover: "/img/cover/A_shield_icon_surrounded_by_cloud_symbols.webp"
coverAlt: "Щит среди облачных символов обозначает защищённую облачную среду. На щите изображён логотип Azure Security Center."
coverCaption: ""
---

**Как защитить облачную среду с помощью Azure Security Center**

Защита облачной среды помогает уберечь данные, приложения и инфраструктуру организации от угроз. **Azure Security Center** от Microsoft помогает улучшить состояние безопасности и быстро выявлять потенциальные риски в Azure. В статье объясняется, как защищать облачную среду с помощью Azure Security Center, и приводятся рекомендации по настройке функций безопасности. Технические сведения и примеры помогут применить описанные действия.

*С момента первоначальной публикации названия продуктов изменились. Microsoft Azure Security Center теперь называется Microsoft Defender for Cloud. Azure Active Directory теперь называется Microsoft Entra ID. Azure Sentinel теперь называется Microsoft Sentinel. Azure Defender обозначает планы Defender и защиту рабочих нагрузок в Defender for Cloud. Старые названия сохранены ниже там, где они относятся к терминологии 2023 года.*

В актуальном [обзоре Defender for Cloud](https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-cloud-introduction) он описан как платформа защиты облачных приложений, включающая управление состоянием безопасности облака, DevSecOps и защиту рабочих нагрузок. Набор функций и условия лицензирования зависят от облака, типа ресурса, подписки и плана.

______

## Знакомство с Azure Security Center

Azure Security Center — это **единая система управления безопасностью инфраструктуры**. Она помогает выявлять и устранять уязвимости в облачной среде. Среди её функций — обнаружение угроз, управление состоянием безопасности и управление соответствием требованиям.

**Непрерывная оценка безопасности** и **расширенная защита от угроз** — две ключевые функции Azure Security Center. Непрерывная оценка помогает находить потенциальные проблемы безопасности. Расширенная защита помогает обнаруживать угрозы и реагировать на них.

______

## Настройка политик безопасности и стандартов соответствия

Azure Security Center позволяет внедрять и управлять политиками безопасности во всей облачной среде. Используйте службу **Azure Policy**, чтобы создавать собственные политики, или применяйте встроенные политики для выполнения рекомендаций и стандартов соответствия. Сравнивайте состояние безопасности с отраслевыми стандартами, например [NIST 800-53](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final), [CIS](https://www.cisecurity.org/) и [ISO 27001](https://www.iso.org/isoiec-27001-information-security.html).

Azure Security Center также предоставляет функции управления соответствием требованиям. Они помогают отслеживать состояние организации по таким нормативным стандартам, как [GDPR](https://gdpr.eu/), [HIPAA](https://www.hhs.gov/hipaa/index.html) и [PCI DSS](https://www.pcisecuritystandards.org/).

______

## Защита ресурсов Azure

**Поддержание безопасного состояния ресурсов** — важная часть защиты облачной среды. Azure Security Center показывает **Secure Score**, показатель состояния безопасности ресурсов. Улучшайте его, выполняя рекомендации Azure Security Center.

### Безопасность сети

**Network Security Groups (NSGs)**, **Azure Firewall** и **Web Application Firewall (WAF)** помогают защищать среду Azure от угроз. Эти средства контролируют входящий и исходящий сетевой трафик, снижая риск несанкционированного доступа и атак.

#### Network Security Groups (NSGs)

NSG работают как виртуальные брандмауэры для ресурсов Azure. С их помощью задают правила, разрешающие или блокирующие сетевой трафик к ресурсам и от них. Пример создания NSG с правилами для трафика:

```azurecli
# Создайте Network Security Group
az network nsg create --name MyNSG --resource-group MyResourceGroup

# Добавьте правила для разрешения или блокировки трафика
az network nsg rule create --name MyNSGRule --nsg-name MyNSG --priority 100 --resource-group MyResourceGroup --access Allow --protocol Tcp --direction Inbound --source-address-prefixes '*' --source-port-ranges '*' --destination-address-prefixes '*' --destination-port-ranges '80'
```
Дополнительные сведения см. в официальной документации [Network Security Groups](https://docs.microsoft.com/en-us/azure/virtual-network/security-overview).

В примере разрешён входящий трафик TCP на порт 80 от любого источника IPv4. В рабочей среде укажите известный диапазон источников, частную конечную точку или маршрут через балансировщик нагрузки. Перед использованием примера изучите актуальный [обзор безопасности NSG](https://learn.microsoft.com/en-us/azure/virtual-network/network-security-groups-overview).

#### Azure Firewall

Azure Firewall — управляемая облачная служба сетевой безопасности для защиты ресурсов Azure. Она поддерживает фильтрацию на основе аналитики угроз, категории веб-сайтов, централизованное ведение журналов и аналитику. Для настройки следуйте [инструкциям быстрого запуска](https://learn.microsoft.com/en-us/azure/firewall-manager/quick-firewall-policy-bicep).

#### Web Application Firewall (WAF)

Web Application Firewall (WAF) — функция **Azure Application Gateway**. Она защищает веб-приложения от распространённых атак, включая внедрение SQL-кода и межсайтовый скриптинг. Подключите WAF к существующим приложениям и настройте правила для определённых типов атак.

Пример создания Application Gateway с включённым WAF:

```azurecli
# Создайте политику WAF
az network application-gateway waf-policy create --name MyWafPolicy --resource-group MyResourceGroup --location EastUS

# Создайте виртуальную сеть и подсеть
az network vnet create --name MyVNet --resource-group MyResourceGroup --location EastUS --address-prefix 10.0.0.0/16
az network vnet subnet create --name MySubnet --resource-group MyResourceGroup --vnet-name MyVNet --address-prefix 10.0.0.0/24

# Создайте общедоступный IP-адрес
az network public-ip create --name MyPublicIP --resource-group MyResourceGroup --location EastUS --sku Standard

# Создайте Application Gateway с включённым WAF
az network application-gateway create --name MyAppGateway --resource-group MyResourceGroup --location EastUS --vnet-name MyVNet --subnet MySubnet --public-ip-address MyPublicIP --http-settings-cookie-based-affinity Enabled --sku WAF_v2 --waf-policy MyWafPolicy

```
Дополнительные сведения см. в официальной документации [Web Application Firewall](https://docs.microsoft.com/en-us/azure/web-application-firewall/ag/ag-overview).

### Управление удостоверениями и доступом

**Microsoft Entra ID, ранее Azure Active Directory (Azure AD),** — важная часть защиты облачной среды. Defender for Cloud рекомендует меры по управлению удостоверениями и доступом, в том числе включение **Multi-Factor Authentication (MFA)**, применение **Role-Based Access Control (RBAC)** и мониторинг подозрительных действий.

#### Multi-Factor Authentication (MFA)

MFA добавляет дополнительный уровень защиты учётных записей Azure AD. Перед предоставлением доступа пользователю нужно пройти два или более вида проверки. Чтобы включить MFA в организации, следуйте [пошаговому руководству](https://docs.microsoft.com/en-us/azure/active-directory/authentication/tutorial-enable-azure-mfa) Microsoft.

Пример: включение MFA для пользователя

```powershell
# Подключитесь к Azure AD
Connect-AzureAD

# Включите MFA для выбранного пользователя
$UserPrincipalName = "johndoe@example.com"
$StsUserObjectID = (Get-AzureADUser -Filter "UserPrincipalName eq '$UserPrincipalName'").ObjectId
$StrongAuthRequirements = @(@{"Location"=""; "SatisfactionFactor"="2"; "VerificationMethod"="1"};@{"Location"=""; "SatisfactionFactor"="2"; "VerificationMethod"="2"})
Set-AzureADUser -ObjectId $StsUserObjectID -StrongAuthenticationRequirements $StrongAuthRequirements
```
#### Role-Based Access Control (RBAC)

RBAC позволяет задавать детальные разрешения для ресурсов Azure, чтобы пользователи получали нужный уровень доступа. Назначайте роли пользователям, группам или приложениям для управления доступом к ресурсам организации. Для настройки RBAC следуйте [официальному руководству](https://docs.microsoft.com/en-us/azure/role-based-access-control/overview) Microsoft.

Пример: назначение роли пользователю

```azurecli
# Назначьте пользователю роль Reader
az role assignment create --assignee johndoe@example.com --role "Reader" --scope "/subscriptions/your_subscription_id/resourceGroups/your_resource_group"
```
#### Мониторинг подозрительной активности

Azure AD предоставляет **Identity Protection** и **Conditional Access** для мониторинга подозрительной активности и реагирования на неё. Identity Protection использует машинное обучение для обнаружения аномалий и рискованных попыток входа. Conditional Access позволяет задавать политики доступа на основе устройства, местоположения и уровня риска.

Чтобы настроить Azure AD Identity Protection, следуйте [официальному руководству](https://learn.microsoft.com/en-us/azure/active-directory/identity-protection/concept-identity-protection-b2b) Microsoft.

Пример: создание политики Conditional Access

```powershell
# Подключитесь к Azure AD
Connect-AzureAD

# Создайте политику Conditional Access
$PolicyName = "BlockSignInFromUnknownLocations"
$PolicyDescription = "Блокировать вход пользователей из неизвестных местоположений."
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
Дополнительные сведения см. в документации [Azure AD Identity Protection](https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/overview) и [Conditional Access](https://learn.microsoft.com/en-us/azure/active-directory/conditional-access/overview).

### Защита данных

Защита данных в облаке необходима. Azure Security Center предлагает **Azure Information Protection**, **Azure Storage Service Encryption** и **Azure Disk Encryption**. Эти функции помогают шифровать данные и управлять доступом к ним.

#### Azure Information Protection

**Azure Information Protection (AIP)** — облачная служба для классификации, маркировки и защиты конфиденциальных документов и писем. В AIP есть встроенные метки, например «Конфиденциально» и «Личное», которые можно настроить под нужды организации. Также можно настроить автоматическое применение меток по заданным правилам. Для начала следуйте [официальному руководству](https://docs.microsoft.com/en-us/azure/information-protection/what-is-information-protection).

Пример: создание пользовательской метки

```powershell
# Подключитесь к службе AIP
Connect-AipService

# Создайте метку с параметрами защиты
$LabelName = "Конфиденциально - только для внутреннего использования"
$LabelDescription = "Эта метка применяет шифрование и политику доступа только для внутреннего использования."
$LabelProtectionSettings = @{
    "ContentExpirationDate" = (Get-Date).AddMonths(6).ToUniversalTime();
    "OfflineAccessInterval" = "P7D";
    "UserRights" = @("domain\GroupA=View", "domain\GroupB=View,Edit,Print")
}
New-AipServiceLabel -Name $LabelName -Description $LabelDescription -ProtectionSettings $LabelProtectionSettings
```
#### Azure Storage Service Encryption

**Azure Storage Service Encryption (SSE)** автоматически шифрует данные в состоянии покоя в учётных записях Azure Storage, включая хранилища Blob, File, Table и Queue. SSE использует ключи Azure или ключи клиента для шифрования на уровне учётной записи хранилища. Чтобы включить SSE, следуйте [пошаговому руководству](https://docs.microsoft.com/en-us/azure/storage/common/storage-service-encryption) Microsoft.

Azure Information Protection — прежнее название продукта. В актуальной документации о доступности функций Sentinel продукт отмечен как устаревший. Перед новым развёртыванием маркировки ознакомьтесь с текущей документацией Microsoft Purview Information Protection.

Пример: включение SSE для учётной записи хранилища

```azurecli
# Включите SSE с ключами Azure
az storage account update --name mystorageaccount --resource-group myresourcegroup --encryption-services blob file
```
#### Azure Disk Encryption

**Azure Disk Encryption** защищает диски виртуальных машин, шифруя их с помощью BitLocker (Windows) или dm-crypt (Linux). Ключи шифрования и секреты защищены Azure Key Vault. Чтобы включить Azure Disk Encryption, следуйте [официальному руководству](https://learn.microsoft.com/en-us/azure/virtual-machines/disk-encryption-overview) Microsoft.

Пример: включение Azure Disk Encryption для виртуальной машины

```azurecli
# Включите Azure Disk Encryption для виртуальной машины Windows
az vm encryption enable --resource-group myResourceGroup --name myVM --disk-encryption-keyvault myKeyVault
```
Дополнительные сведения см. в документации [Azure Information Protection](https://docs.microsoft.com/en-us/azure/information-protection/what-is-information-protection), [Azure Storage Service Encryption](https://docs.microsoft.com/en-us/azure/storage/common/storage-service-encryption) и [Azure Disk Encryption](https://learn.microsoft.com/en-us/azure/virtual-machines/disk-encryption-overview).
______

## Обнаружение угроз и реагирование на них

Azure Security Center обнаруживает потенциальные угрозы и отправляет оповещения. Интеграция с **Azure Sentinel** позволяет отслеживать, расследовать и устранять инциденты безопасности во всей среде.

### Обнаружение угроз

Azure Security Center использует **Azure Defender** для выявления потенциальных угроз безопасности. Azure Defender отслеживает признаки компрометации ресурсов и предоставляет оповещения и рекомендации по реагированию. Чтобы включить Azure Defender, следуйте [официальному руководству](https://docs.microsoft.com/en-us/azure/security-center/defender-for-cloud-enable).

Пример: включение Azure Defender для подписки

```azurecli
# Включите Azure Defender для подписки
az security auto-provisioning-setting update --name default --auto-provision on
```
### Реагирование на угрозы
Если обнаружена угроза, реагируйте быстро и эффективно. Управление **Security Incident** в Azure Security Center помогает расследовать инциденты безопасности и реагировать на них. Интегрируйте **Azure Sentinel**, чтобы создавать автоматизированные сценарии playbook и координировать реагирование. Сведения об интеграции Azure Security Center с Azure Sentinel приведены в **официальной документации**.

Пример: создание сценария Logic App для Azure Sentinel
```azurecli
# Создайте группу ресурсов
az group create --name MyResourceGroup --location EastUS

# Создайте Logic App
az logic workflow create --resource-group MyResourceGroup --location EastUS --name MyPlaybook --definition @playbook-definition.json
```
В файле `playbook-definition.json` должно быть описание сценария Logic App. Примеры для Azure Sentinel приведены в [репозитории Azure-Sentinel на GitHub](https://github.com/Azure/Azure-Sentinel/tree/master/Playbooks).

Объедините обнаружение угроз в Azure Security Center с Azure Sentinel, чтобы выявлять угрозы в Azure и реагировать на них. Сведения см. в документации [Azure Defender](https://learn.microsoft.com/en-us/azure/defender-for-cloud/enable-enhanced-security) и [Azure Sentinel](https://docs.microsoft.com/en-us/azure/sentinel/overview).

Текущий путь интеграции передаёт оповещения Defender for Cloud в Microsoft Sentinel через [соединитель Defender for Cloud](https://learn.microsoft.com/en-us/azure/sentinel/connect-defender-for-cloud). Прежде чем полагаться на автоматизацию, проверьте соединитель, правила сбора данных, аналитические правила и рабочий процесс инцидентов в портале Defender или Azure.
______

## Мониторинг и отчётность

Мониторинг и отчётность помогают поддерживать безопасность облачной среды. Azure Security Center предлагает такие средства, как **панель безопасности**, **оповещения безопасности** и **отчёты о соответствии**.

### Панель безопасности

Панель безопасности Azure Security Center показывает общее состояние защиты. На ней отображаются Secure Score, рекомендации и активные оповещения. Панель также показывает состояние соответствия и помогает отслеживать изменения со временем.

### Оповещения безопасности

При обнаружении потенциальных угроз Azure Security Center формирует оповещения. В них есть сведения об угрозе и рекомендации по снижению риска. Настройте уведомления по электронной почте или SMS либо интегрируйте службу с [Slack](https://slack.com/) и [Microsoft Teams](https://www.microsoft.com/en-us/microsoft-teams/group-chat-software).

### Отчёты о соответствии

Azure Security Center формирует отчёты по таким нормативным стандартам, как GDPR, HIPAA и PCI DSS. Используйте их, чтобы отслеживать соответствие организации и выявлять области для улучшения.

______

## Рекомендации по использованию Azure Security Center

Чтобы эффективнее использовать Azure Security Center, следуйте этим рекомендациям:

1. **Включите Azure Security Center для всех подписок**: убедитесь, что защита действует для каждой подписки Azure.
2. **Регулярно проверяйте Secure Score**: отслеживайте общее состояние безопасности и находите области для улучшения.
3. **Выполняйте рекомендации по безопасности**: улучшайте защиту и снижайте риски, выполняя рекомендации Azure Security Center.
4. **Следите за оповещениями безопасности**: проверяйте оповещения и реагируйте, чтобы снизить потенциальные угрозы.
5. **Обновляйте требования соответствия**: регулярно пересматривайте политики с учётом актуальных нормативных стандартов.

## Текущий рабочий процесс Defender for Cloud

Для текущего развёртывания используйте такую последовательность. Названия в предыдущих разделах помогают искать исторические сведения, но портал и документация используют терминологию Defender for Cloud.

1. **Составьте перечень подписок и соединителей.** Запишите подписки Azure, соединители AWS или GCP, проекты DevOps и критически важные ресурсы.
2. **Включите необходимые планы Defender.** Выберите планы для рабочих нагрузок и проверьте лицензирование до включения в производственных подписках.
3. **Проверьте Cloud Secure Score и рекомендации.** В первую очередь рассмотрите доступность из Интернета, риски удостоверений, эксплуатируемые уязвимости и отсутствие журналирования. Оценка не доказывает полного соответствия требованиям.
4. **Настройте средства управления Microsoft Entra.** Требуйте устойчивую к фишингу MFA для важных учётных записей, применяйте RBAC с минимальными привилегиями и проверяйте привилегированный доступ.
5. **Передавайте оповещения в Microsoft Sentinel.** Проверьте получение оповещений, аналитические правила, ответственных, автоматизацию реагирования и срок хранения.
6. **Проводите повторную проверку после изменений.** Проверяйте рекомендации после установки исправлений, изменений архитектуры, добавления соединителей или смены планов.

## Практический список проверки

- **Удостоверения:** удалите старые учётные записи, сократите постоянный административный доступ и проверьте исключения Conditional Access.
- **Сеть:** закройте общедоступные порты управления, сузьте диапазоны источников NSG и убедитесь, что журналы брандмауэра и WAF поступают в рабочую область мониторинга.
- **Данные:** классифицируйте хранилища конфиденциальных данных, подтвердите шифрование и владельцев ключей, проверьте восстановление резервных копий.
- **Обнаружение:** проверьте критичность оповещений, маршрутизацию уведомлений, ответственных за инциденты и сценарии реагирования.
- **Управление:** назначьте владельца каждой инициативе политики, укажите срок действия исключения и соберите доказательства для нужного стандарта.

______

## Источники

- [Документация Azure Security Center](https://docs.microsoft.com/en-us/azure/security-center/)
- [Служба Azure Policy](https://docs.microsoft.com/en-us/azure/governance/policy/)
- [NIST 800-53](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final)
- [CIS](https://www.cisecurity.org/)
- [ISO 27001](https://www.iso.org/isoiec-27001-information-security.html)
- [GDPR](https://gdpr.eu/)
- [HIPAA](https://www.hhs.gov/hipaa/index.html)
- [PCI DSS](https://www.pcisecuritystandards.org/)
