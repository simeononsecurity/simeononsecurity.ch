---
title: "احمِ بيئة السحابة باستخدام Microsoft Defender for Cloud"
date: 2023-04-10
lastmod: 2026-11-20
toc: true
draft: false
description: "احمِ أحمال عمل Azure باستخدام Microsoft Defender for Cloud. راجع أسماء Azure Security Center القديمة وتوصياته وسياساته وخطوات الاستجابة."
tags: ["Azure", "Security Center", "أمن السحابة", "Azure Sentinel", "Azure Defender", "أمن الشبكات", "إدارة الهوية", "أمن البيانات", "كشف التهديدات", "الاستجابة للتهديدات", "MFA", "RBAC", "NSGs", "Azure Firewall", "WAF", "Azure AD", "Azure Information Protection", "Azure Storage Service Encryption", "Azure Disk Encryption"]
cover: "/img/cover/A_shield_icon_surrounded_by_cloud_symbols.webp"
coverAlt: "درع تحيط به رموز السحابة يمثل بيئة سحابية آمنة، ويحمل شعار Azure Security Center."
coverCaption: ""
---

**كيفية تأمين بيئة السحابة باستخدام Azure Security Center**

يساعد تأمين بيئة السحابة على حماية بيانات المؤسسة وتطبيقاتها وبنيتها التحتية من التهديدات. يتيح لك **Azure Security Center** من Microsoft تحسين وضع الأمان وتحديد المخاطر المحتملة في Azure بسرعة. يشرح هذا المقال استخدام Azure Security Center لحماية بيئة السحابة، ويعرض ممارسات لتطبيق ميزات الأمان. كما يقدم تفاصيل تقنية وأمثلة تساعدك على تنفيذ الخطوات.

*تغيّرت أسماء المنتجات منذ نشر هذا المقال أول مرة. أصبح Microsoft Azure Security Center يُسمى الآن Microsoft Defender for Cloud. وأصبح Azure Active Directory يُسمى Microsoft Entra ID. وأصبح Azure Sentinel يُسمى Microsoft Sentinel. يشير Azure Defender إلى خطط Defender وحماية أحمال العمل ضمن Defender for Cloud. تبقى الأسماء القديمة أدناه عند وصف مصطلحات عام 2023.*

يصف [التعريف الحالي بـ Defender for Cloud](https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-cloud-introduction) المنصة بأنها نظام لحماية التطبيقات السحابية الأصلية، ويشمل إدارة وضع الأمان السحابي وDevSecOps وحماية أحمال العمل السحابية. يعتمد توفر الميزات والترخيص على السحابة ونوع المورد والاشتراك والخطة.

______

## فهم Azure Security Center

Azure Security Center هو **نظام موحد لإدارة أمن البنية التحتية**. يساعدك على اكتشاف الثغرات المحتملة في بيئة السحابة ومعالجتها. تشمل ميزاته كشف التهديدات وإدارة وضع الأمان وإدارة الامتثال.

**التقييم المستمر للأمان** و**الحماية المتقدمة من التهديدات** ميزتان أساسيتان في Azure Security Center. يساعد التقييم المستمر على العثور على مشكلات الأمان المحتملة، بينما تساعد الحماية المتقدمة على كشف التهديدات والاستجابة لها.

______

## تطبيق سياسات الأمان ومعايير الامتثال

يتيح Azure Security Center تطبيق سياسات الأمان وإدارتها في بيئة السحابة. استخدم خدمة **Azure Policy** لإنشاء سياسات مخصصة، أو استخدم السياسات المضمنة لتطبيق الممارسات الجيدة ومعايير الامتثال. ويمكنك تقييم وضع الأمان وفق معايير القطاع مثل [NIST 800-53](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final) و[CIS](https://www.cisecurity.org/) و[ISO 27001](https://www.iso.org/isoiec-27001-information-security.html).

يوفر Azure Security Center أيضاً ميزات لإدارة الامتثال، تتيح لك متابعة حالة مؤسستك وفق أطر تنظيمية مثل [GDPR](https://gdpr.eu/) و[HIPAA](https://www.hhs.gov/hipaa/index.html) و[PCI DSS](https://www.pcisecuritystandards.org/).

______

## تأمين موارد Azure

تُعد **المحافظة على سلامة أمان الموارد** جزءاً مهماً من حماية بيئة السحابة. يوفر Azure Security Center **Secure Score** لقياس وضع أمان الموارد ومساعدتك على فهم مستوى حمايتها. عالج توصيات Azure Security Center لتحسين النتيجة.

### أمن الشبكة

تساعد تدابير مثل **Network Security Groups (NSGs)** و**Azure Firewall** و**Web Application Firewall (WAF)** على حماية Azure من التهديدات المحتملة. تتحكم هذه الأدوات في حركة مرور الشبكة الواردة والصادرة، وتقلل خطر الوصول غير المصرح به والهجمات.

#### Network Security Groups (NSGs)

تعمل NSG كجدار حماية افتراضي لموارد Azure. يمكنك تحديد قواعد تسمح بحركة مرور الشبكة إلى الموارد ومنها أو تمنعها. يوضح المثال التالي إنشاء NSG بقواعد لحركة المرور:

```azurecli
# أنشئ Network Security Group
az network nsg create --name MyNSG --resource-group MyResourceGroup

# أضف قواعد للسماح بحركة المرور أو حظرها
az network nsg rule create --name MyNSGRule --nsg-name MyNSG --priority 100 --resource-group MyResourceGroup --access Allow --protocol Tcp --direction Inbound --source-address-prefixes '*' --source-port-ranges '*' --destination-address-prefixes '*' --destination-port-ranges '80'
```
راجع الوثائق الرسمية حول [Network Security Groups](https://docs.microsoft.com/en-us/azure/virtual-network/security-overview).

يسمح المثال بحركة مرور TCP الواردة على المنفذ 80 من أي مصدر IPv4. في بيئة الإنتاج، استخدم نطاق مصدر معروفاً أو نقطة نهاية خاصة أو مساراً عبر موزع أحمال. راجع [نظرة عامة على أمان NSG](https://learn.microsoft.com/en-us/azure/virtual-network/network-security-groups-overview) الحالية قبل استخدام المثال.

#### Azure Firewall

Azure Firewall خدمة مُدارة لأمن الشبكات السحابية، وتحمي موارد Azure. توفر تصفية قائمة على معلومات التهديدات، وفئات الويب، وتسجيل الأحداث والتحليلات المركزية. لإعدادها، اتبع [تعليمات البدء السريع](https://learn.microsoft.com/en-us/azure/firewall-manager/quick-firewall-policy-bicep).

#### Web Application Firewall (WAF)

يُعد Web Application Firewall (WAF) ميزة في **Azure Application Gateway**. يحمي تطبيقات الويب من الهجمات الشائعة، مثل حقن SQL والبرمجة النصية عبر المواقع وغيرها. ادمج WAF مع تطبيقات الويب الحالية واضبط قواعد مخصصة لأنماط الهجوم المحددة.

مثال على إنشاء Application Gateway مع تفعيل WAF:

```azurecli
# أنشئ سياسة WAF
az network application-gateway waf-policy create --name MyWafPolicy --resource-group MyResourceGroup --location EastUS

# أنشئ شبكة افتراضية وشبكة فرعية
az network vnet create --name MyVNet --resource-group MyResourceGroup --location EastUS --address-prefix 10.0.0.0/16
az network vnet subnet create --name MySubnet --resource-group MyResourceGroup --vnet-name MyVNet --address-prefix 10.0.0.0/24

# أنشئ عنوان IP عاماً
az network public-ip create --name MyPublicIP --resource-group MyResourceGroup --location EastUS --sku Standard

# أنشئ Application Gateway مع تفعيل WAF
az network application-gateway create --name MyAppGateway --resource-group MyResourceGroup --location EastUS --vnet-name MyVNet --subnet MySubnet --public-ip-address MyPublicIP --http-settings-cookie-based-affinity Enabled --sku WAF_v2 --waf-policy MyWafPolicy

```
راجع الوثائق الرسمية حول [Web Application Firewall](https://docs.microsoft.com/en-us/azure/web-application-firewall/ag/ag-overview).

### إدارة الهوية والوصول

**Microsoft Entra ID، الذي كان يسمى Azure Active Directory (Azure AD)،** عنصر أساسي في تأمين بيئة السحابة. يقدم Defender for Cloud توصيات لتحسين إدارة الهوية والوصول، منها تفعيل **Multi-Factor Authentication (MFA)** وتطبيق **Role-Based Access Control (RBAC)** ومراقبة الأنشطة المشبوهة.

#### Multi-Factor Authentication (MFA)

تضيف MFA طبقة حماية لحسابات Azure AD، إذ تطلب من المستخدم تقديم طريقتين أو أكثر للتحقق قبل منحه الوصول. لتفعيل MFA في مؤسستك، اتبع [الدليل خطوة بخطوة](https://docs.microsoft.com/en-us/azure/active-directory/authentication/tutorial-enable-azure-mfa) من Microsoft.

مثال: تفعيل MFA لمستخدم

```powershell
# اتصل بـ Azure AD
Connect-AzureAD

# فعّل MFA لمستخدم محدد
$UserPrincipalName = "johndoe@example.com"
$StsUserObjectID = (Get-AzureADUser -Filter "UserPrincipalName eq '$UserPrincipalName'").ObjectId
$StrongAuthRequirements = @(@{"Location"=""; "SatisfactionFactor"="2"; "VerificationMethod"="1"};@{"Location"=""; "SatisfactionFactor"="2"; "VerificationMethod"="2"})
Set-AzureADUser -ObjectId $StsUserObjectID -StrongAuthenticationRequirements $StrongAuthRequirements
```
#### Role-Based Access Control (RBAC)

يتيح RBAC تحديد أذونات دقيقة لموارد Azure، لضمان حصول كل مستخدم على مستوى الوصول المناسب. عيّن الأدوار للمستخدمين أو المجموعات أو التطبيقات لإدارة وصولهم إلى موارد المؤسسة. لتطبيق RBAC، اتبع [الدليل الرسمي](https://docs.microsoft.com/en-us/azure/role-based-access-control/overview) من Microsoft.

مثال: تعيين دور لمستخدم

```azurecli
# عيّن دور Reader لمستخدم
az role assignment create --assignee johndoe@example.com --role "Reader" --scope "/subscriptions/your_subscription_id/resourceGroups/your_resource_group"
```
#### مراقبة الأنشطة المشبوهة

توفر Azure AD ميزتي **Identity Protection** و**Conditional Access** لمراقبة الأنشطة المشبوهة والاستجابة لها. تستخدم Identity Protection التعلم الآلي لاكتشاف السلوك غير المعتاد ومحاولات تسجيل الدخول المحفوفة بالمخاطر. وتتيح Conditional Access وضع سياسات وصول تستند إلى الجهاز والموقع ومستوى المخاطر.

لإعداد Azure AD Identity Protection، اتبع [الدليل الرسمي](https://learn.microsoft.com/en-us/azure/active-directory/identity-protection/concept-identity-protection-b2b) من Microsoft.

مثال: إنشاء سياسة Conditional Access

```powershell
# اتصل بـ Azure AD
Connect-AzureAD

# أنشئ سياسة Conditional Access
$PolicyName = "BlockSignInFromUnknownLocations"
$PolicyDescription = "امنع تسجيل دخول المستخدمين من مواقع غير معروفة."
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
راجع الوثائق الرسمية حول [Azure AD Identity Protection](https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/overview) و[Conditional Access](https://learn.microsoft.com/en-us/azure/active-directory/conditional-access/overview).

### أمن البيانات

حماية البيانات في السحابة ضرورية. يقدم Azure Security Center ميزات مثل **Azure Information Protection** و**Azure Storage Service Encryption** و**Azure Disk Encryption**. تساعد هذه الميزات على تشفير البيانات وإدارة الوصول إليها.

#### Azure Information Protection

**Azure Information Protection (AIP)** خدمة سحابية لتصنيف المستندات والبريد الإلكتروني الحساس ووضع علامات عليهما وحمايتهما. تتضمن AIP علامات مدمجة مثل «سري» و«شخصي»، ويمكن تخصيصها لتناسب احتياجات المؤسسة. ويمكن أيضاً ضبط التطبيق التلقائي للعلامات وفق قواعد محددة مسبقاً. للبدء، اتبع [الدليل الرسمي](https://docs.microsoft.com/en-us/azure/information-protection/what-is-information-protection).

مثال: إنشاء علامة مخصصة

```powershell
# اتصل بخدمة AIP
Connect-AipService

# أنشئ علامة مخصصة بإعدادات حماية
$LabelName = "حساس - للاستخدام الداخلي فقط"
$LabelDescription = "تطبق هذه العلامة التشفير وسياسة وصول للاستخدام الداخلي فقط."
$LabelProtectionSettings = @{
    "ContentExpirationDate" = (Get-Date).AddMonths(6).ToUniversalTime();
    "OfflineAccessInterval" = "P7D";
    "UserRights" = @("domain\GroupA=View", "domain\GroupB=View,Edit,Print")
}
New-AipServiceLabel -Name $LabelName -Description $LabelDescription -ProtectionSettings $LabelProtectionSettings
```
#### Azure Storage Service Encryption

تشفّر **Azure Storage Service Encryption (SSE)** تلقائياً البيانات المخزنة في حسابات Azure Storage، بما في ذلك Blob وFile وTable وQueue. تستخدم SSE مفاتيح تديرها Azure أو مفاتيح يديرها العميل للتشفير على مستوى حساب التخزين. لتفعيل SSE، اتبع [الدليل خطوة بخطوة](https://docs.microsoft.com/en-us/azure/storage/common/storage-service-encryption) من Microsoft.

Azure Information Protection اسم قديم لمنتج. تدرجه وثائق Microsoft الحالية لتوفر ميزات Sentinel كمنتج متوقف. راجع وثائق Microsoft Purview Information Protection الحالية قبل بدء نشر جديد للتصنيفات.

مثال: تفعيل SSE لحساب تخزين

```azurecli
# فعّل SSE باستخدام مفاتيح تديرها Azure
az storage account update --name mystorageaccount --resource-group myresourcegroup --encryption-services blob file
```
#### Azure Disk Encryption

يساعد **Azure Disk Encryption** على حماية أقراص الأجهزة الافتراضية بتشفيرها باستخدام BitLocker (Windows) أو dm-crypt (Linux). يحمي Azure Key Vault مفاتيح التشفير والأسرار. لتفعيل Azure Disk Encryption، اتبع [الدليل الرسمي](https://learn.microsoft.com/en-us/azure/virtual-machines/disk-encryption-overview) من Microsoft.

مثال: تفعيل Azure Disk Encryption لجهاز افتراضي

```azurecli
# فعّل Azure Disk Encryption لجهاز Windows افتراضي
az vm encryption enable --resource-group myResourceGroup --name myVM --disk-encryption-keyvault myKeyVault
```
راجع الوثائق الرسمية حول [Azure Information Protection](https://docs.microsoft.com/en-us/azure/information-protection/what-is-information-protection) و[Azure Storage Service Encryption](https://docs.microsoft.com/en-us/azure/storage/common/storage-service-encryption) و[Azure Disk Encryption](https://learn.microsoft.com/en-us/azure/virtual-machines/disk-encryption-overview).
______

## كشف التهديدات والاستجابة لها

يستخدم Azure Security Center قدرات متقدمة لكشف التهديدات المحتملة وإرسال التنبيهات. يتيح التكامل مع **Azure Sentinel** مراقبة حوادث الأمان والتحقيق فيها والاستجابة لها في البيئة بأكملها.

### كشف التهديدات

يستخدم Azure Security Center **Azure Defender** لتحديد التهديدات الأمنية المحتملة. يراقب Azure Defender الموارد بحثاً عن مؤشرات الاختراق، ويرسل تنبيهات وتوصيات للاستجابة. لتفعيله، اتبع [الدليل الرسمي](https://docs.microsoft.com/en-us/azure/security-center/defender-for-cloud-enable).

مثال: تفعيل Azure Defender لاشتراك

```azurecli
# فعّل Azure Defender لاشتراك
az security auto-provisioning-setting update --name default --auto-provision on
```
### الاستجابة للتهديدات
عند اكتشاف تهديد، استجب بسرعة وفاعلية. تساعد إدارة **Security Incident** في Azure Security Center على التحقيق في الحوادث والاستجابة لها. ويمكنك دمج **Azure Sentinel** لإنشاء مسارات عمل مؤتمتة وتنسيق الاستجابة. راجع **الوثائق الرسمية** حول دمج Azure Security Center مع Azure Sentinel.

مثال: إنشاء مسار Logic App لـ Azure Sentinel
```azurecli
# أنشئ مجموعة موارد
az group create --name MyResourceGroup --location EastUS

# أنشئ Logic App
az logic workflow create --resource-group MyResourceGroup --location EastUS --name MyPlaybook --definition @playbook-definition.json
```
يجب أن يحتوي الملف `playbook-definition.json` على تعريف مسار Logic App. تجد أمثلة Azure Sentinel في [مستودع Azure-Sentinel على GitHub](https://github.com/Azure/Azure-Sentinel/tree/master/Playbooks).

ادمج قدرات كشف التهديدات في Azure Security Center مع Azure Sentinel لوضع استراتيجية لكشف التهديدات في Azure والاستجابة لها. راجع الوثائق الرسمية حول [Azure Defender](https://learn.microsoft.com/en-us/azure/defender-for-cloud/enable-enhanced-security) و[Azure Sentinel](https://docs.microsoft.com/en-us/azure/sentinel/overview).

يرسل مسار التكامل الحالي تنبيهات Defender for Cloud إلى Microsoft Sentinel عبر [موصل Defender for Cloud](https://learn.microsoft.com/en-us/azure/sentinel/connect-defender-for-cloud). قبل الاعتماد على الأتمتة، تحقّق من الموصل وقواعد جمع البيانات والقواعد التحليلية وسير الحوادث في مدخل Defender أو Azure.
______

## المراقبة وإعداد التقارير

تساعد المراقبة وإعداد التقارير على الحفاظ على أمان بيئة السحابة. يوفر Azure Security Center أدوات مثل **لوحة الأمان** و**تنبيهات الأمان** و**تقارير الامتثال**.

### لوحة الأمان

تعرض Security Dashboard في Azure Security Center نظرة عامة على وضع الأمان. وتعرض Secure Score والتوصيات والتنبيهات النشطة. كما توضح حالة الامتثال وتتيح متابعة التقدم بمرور الوقت.

### تنبيهات الأمان

ينشئ Azure Security Center تنبيهات عند اكتشاف تهديدات محتملة. تتضمن التنبيهات تفاصيل التهديد وتوصيات لتقليل المخاطر. يمكنك إعداد إشعارات عبر البريد الإلكتروني أو الرسائل النصية، أو دمج الخدمة مع [Slack](https://slack.com/) أو [Microsoft Teams](https://www.microsoft.com/en-us/microsoft-teams/group-chat-software).

### تقارير الامتثال

ينشئ Azure Security Center تقارير لأطر تنظيمية مثل GDPR وHIPAA وPCI DSS. استخدمها لمتابعة امتثال المؤسسة وتحديد الجوانب التي تحتاج إلى تحسين.

______

## أفضل الممارسات في Azure Security Center

للاستفادة من Azure Security Center، طبّق الممارسات التالية:

1. **فعّل Azure Security Center لجميع الاشتراكات**: تأكد من حماية كل اشتراك Azure.
2. **راجع Secure Score بانتظام**: تابع وضع الأمان العام وحدد الجوانب التي تحتاج إلى تحسين.
3. **طبّق توصيات الأمان**: حسّن وضع الأمان وقلل المخاطر باتباع توصيات Azure Security Center.
4. **راقب تنبيهات الأمان**: راجع التنبيهات واستجب لها لتقليل التهديدات المحتملة.
5. **حدّث متطلبات الامتثال**: راجع السياسات وحدّثها بانتظام لمواكبة الأطر التنظيمية الحالية.

## سير العمل الحالي في Defender for Cloud

اتبع التسلسل التالي للنشر الحالي. تفيد أسماء الأقسام السابقة في البحث عن المعلومات التاريخية، لكن البوابة والوثائق تستخدم مصطلحات Defender for Cloud.

1. **أعد قائمة بالاشتراكات والموصلات.** سجّل اشتراكات Azure وموصلات AWS أو GCP ومشروعات DevOps والموارد المهمة.
2. **فعّل خطط Defender المطلوبة.** اختر الخطط حسب أحمال العمل وتحقق من الترخيص قبل تفعيلها في اشتراكات الإنتاج.
3. **راجع Cloud Secure Score والتوصيات.** أعط الأولوية للموارد المكشوفة على الإنترنت ومخاطر الهوية والثغرات القابلة للاستغلال ونقص التسجيل. لا تعتبر الدرجة دليلاً على الامتثال الكامل.
4. **اضبط عناصر تحكم Microsoft Entra.** اشترط MFA مقاومة للتصيد للحسابات المهمة، واستخدم RBAC بأقل الامتيازات، وراجع الوصول المميز.
5. **أرسل التنبيهات إلى Microsoft Sentinel.** تحقّق من استقبال التنبيهات والقواعد التحليلية والمسؤولين وأتمتة الاستجابة ومدة الاحتفاظ.
6. **أعد الفحص بعد التغييرات.** راجع التوصيات بعد تثبيت التحديثات أو تغيير البنية أو إضافة موصلات أو تغيير الخطط.

## قائمة مراجعة عملية

- **الهوية:** أزل الحسابات القديمة، وقلل صلاحيات المسؤول الدائمة، وراجع استثناءات Conditional Access.
- **الشبكة:** أغلق منافذ الإدارة العامة، وضيّق نطاقات مصادر NSG، وتحقق من وصول سجلات الجدار الناري وWAF إلى مساحة عمل المراقبة.
- **البيانات:** صنّف مخازن البيانات الحساسة، وتحقق من التشفير وملكية المفاتيح، واختبر استعادة النسخ الاحتياطية.
- **الكشف:** تحقق من شدة التنبيهات وتوجيه الإشعارات وملكية الحوادث ومسارات الاستجابة.
- **الحوكمة:** عيّن مالكاً لكل مبادرة سياسة، وحدد تاريخ انتهاء الاستثناء، واجمع أدلة المعيار المطلوب.

______

## المراجع

- [وثائق Azure Security Center](https://docs.microsoft.com/en-us/azure/security-center/)
- [خدمة Azure Policy](https://docs.microsoft.com/en-us/azure/governance/policy/)
- [NIST 800-53](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final)
- [CIS](https://www.cisecurity.org/)
- [ISO 27001](https://www.iso.org/isoiec-27001-information-security.html)
- [GDPR](https://gdpr.eu/)
- [HIPAA](https://www.hhs.gov/hipaa/index.html)
- [PCI DSS](https://www.pcisecuritystandards.org/)
