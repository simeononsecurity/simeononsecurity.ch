---
title: "تأمين بيئتك السحابية باستخدام Microsoft Defender for Cloud"
date: 2023-04-10
lastmod: 2026-11-14
toc: true
draft: false
description: "تعرّف على كيفية تأمين أحمال عمل Azure باستخدام Microsoft Defender for Cloud، مع مراجعة المصطلحات التاريخية لمركز أمان Azure والتوصيات والسياسات وخطوات الاستجابة."
tags: ["Azure", "Security Center", "أمن السحابة", "Azure Sentinel", "Azure Defender", "أمن الشبكات", "إدارة الهوية", "أمن البيانات", "كشف التهديدات", "الاستجابة للتهديدات", "MFA", "RBAC", "NSGs", "Azure Firewall", "WAF", "Azure AD", "Azure Information Protection", "Azure Storage Service Encryption", "Azure Disk Encryption"]
cover: "/img/cover/A_shield_icon_surrounded_by_cloud_symbols.webp"
coverAlt: "درع تحيط به رموز السحابة، يرمز إلى بيئة سحابية آمنة، ويحمل الدرع شعار Azure Security Center."
coverCaption: ""
---
```azurecli
# إنشاء مجموعة أمان الشبكة
az network nsg create --name MyNSG --resource-group MyResourceGroup

# إضافة قواعد للسماح بحركة المرور أو حظرها
az network nsg rule create --name MyNSGRule --nsg-name MyNSG --priority 100 --resource-group MyResourceGroup --access Allow --protocol Tcp --direction Inbound --source-address-prefixes '*' --source-port-ranges '*' --destination-address-prefixes '*' --destination-port-ranges '80'
```
```azurecli
# إنشاء نهج WAF
az network application-gateway waf-policy create --name MyWafPolicy --resource-group MyResourceGroup --location EastUS

# إنشاء شبكة افتراضية وشبكة فرعية
az network vnet create --name MyVNet --resource-group MyResourceGroup --location EastUS --address-prefix 10.0.0.0/16
az network vnet subnet create --name MySubnet --resource-group MyResourceGroup --vnet-name MyVNet --address-prefix 10.0.0.0/24

# إنشاء عنوان IP عام
az network public-ip create --name MyPublicIP --resource-group MyResourceGroup --location EastUS --sku Standard

# إنشاء بوابة Application Gateway مع تمكين WAF
az network application-gateway create --name MyAppGateway --resource-group MyResourceGroup --location EastUS --vnet-name MyVNet --subnet MySubnet --public-ip-address MyPublicIP --http-settings-cookie-based-affinity Enabled --sku WAF_v2 --waf-policy MyWafPolicy

```
```powershell
# الاتصال بـ Azure AD
Connect-AzureAD

# تفعيل MFA لمستخدم محدد
$UserPrincipalName = "johndoe@example.com"
$StsUserObjectID = (Get-AzureADUser -Filter "UserPrincipalName eq '$UserPrincipalName'").ObjectId
$StrongAuthRequirements = @(@{"Location"=""; "SatisfactionFactor"="2"; "VerificationMethod"="1"};@{"Location"=""; "SatisfactionFactor"="2"; "VerificationMethod"="2"})
Set-AzureADUser -ObjectId $StsUserObjectID -StrongAuthenticationRequirements $StrongAuthRequirements
```
```azurecli
# تعيين دور Reader لمستخدم
az role assignment create --assignee johndoe@example.com --role "Reader" --scope "/subscriptions/your_subscription_id/resourceGroups/your_resource_group"
```
```powershell
# الاتصال بـ Azure AD
Connect-AzureAD

# إنشاء نهج للوصول المشروط (Conditional Access)
$PolicyName = "BlockSignInFromUnknownLocations"
$PolicyDescription = "حظر تسجيل دخول المستخدمين من مواقع غير معروفة."
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
# الاتصال بخدمة AIP
Connect-AipService

# إنشاء تسمية مخصصة بإعدادات الحماية
$LabelName = "Sensitive - Internal Use Only"
$LabelDescription = "تطبق هذه التسمية التشفير وسياسة وصول للاستخدام الداخلي فقط."
$LabelProtectionSettings = @{
    "ContentExpirationDate" = (Get-Date).AddMonths(6).ToUniversalTime();
    "OfflineAccessInterval" = "P7D";
    "UserRights" = @("domain\GroupA=View", "domain\GroupB=View,Edit,Print")
}
New-AipServiceLabel -Name $LabelName -Description $LabelDescription -ProtectionSettings $LabelProtectionSettings
```
```azurecli
# تمكين SSE باستخدام مفاتيح Azure المُدارة
az storage account update --name mystorageaccount --resource-group myresourcegroup --encryption-services blob file
```
```azurecli
# تمكين Azure Disk Encryption لجهاز Windows ظاهري
az vm encryption enable --resource-group myResourceGroup --name myVM --disk-encryption-keyvault myKeyVault
```
```azurecli
# تمكين Azure Defender لاشتراك
az security auto-provisioning-setting update --name default --auto-provision on
```
```azurecli
# إنشاء مجموعة موارد
az group create --name MyResourceGroup --location EastUS

# إنشاء Logic App
az logic workflow create --resource-group MyResourceGroup --location EastUS --name MyPlaybook --definition @playbook-definition.json
```


 ** كيفية تأمين بيئة السحابة الخاصة؟

 تأمين بيئة العمل السريع مهمًا للعمل البحث. يعد متوسط ** بيئة قوية في بيئة Azure الخاصة. كيفية تأمين بيئة السحابة الخاصة في بيئة العمل في Azure ، بالإضافة إلى ذلك ، تم تطويره في المزيد من التفاصيل حول هذا ورمزه ورؤية أفضل لكيفية الحصول على تأمين السحابة الخاصة بـ Azure Security Center.

 ______

*تغيّرت أسماء المنتجات منذ النشر الأصلي. أصبح Microsoft Azure Security Center يُعرف الآن باسم Microsoft Defender for Cloud، وأصبح Azure Active Directory يُعرف باسم Microsoft Entra ID، وأصبح Azure Sentinel يُعرف باسم Microsoft Sentinel. يشير Azure Defender إلى خطط الحماية وحماية أحمال العمل ضمن Defender for Cloud. تبقى الأسماء القديمة أدناه لوصف مصطلحات عام 2023.*

يصف [نظرة عامة على Defender for Cloud](https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-cloud-introduction) الحالية منصة لحماية التطبيقات السحابية الأصلية تشمل إدارة وضع الأمان السحابي وDevSecOps وحماية أحمال العمل السحابية. يعتمد توفر الميزات والترخيص على السحابة ونوع المورد والاشتراك والخطة.

 ## فهم مركز أمان Azure

 Azure Security Center الذي تم توفيره في بيئة المحيط الخاصة به. أرشادات وبيانات أرشادية.

 ** التقييم المستمر المستمر ** و ** الحماية من التهديدات ** ميزتان رئيسيتان مركز لم أمان Azure. في تحديد ما إذا كنت ترغب في تحديد الموعد.

 ______

 ## تنفيذ سياسات الأمن ومعايير الامتثال

 لك Azure Security Center تنفيذ سياسات وإدارتها عبر بيئة السحابة الخاصة. يمكنك استخدام خدمة ** سياسات الصناعة Azure ** أيضًا تقييم معايير معايير مثل [NIST 800-53](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final) ، [ CIS](https://www.cisecurity.org/) و [ISO 27001](https://www.iso.org/isoiec-27001-information-security.html).

 يوفر مركز أمان Azure أيضًا ، كما يظهر في حالة امتثال ، مما يجعله يظهر بحالة جيدة ، مثل [GDPR](https://gdpr.eu/) ، [HIPAA](https://www.hhs.gov/hipaa/index.html) و [PCI DSS](https://www.pcisecuritystandards.org/).

 ______

 ## تأمين مواردك في Azure

 يعد ** جانبًا مهمًا لتأمين بيئة السحابة الخاصة بك. يوفر مركز أمان Azure ** نقاط آمنة ** ، وهي مقياس الأمان لديك ، لمساعدتك في فهم الأمان العام لمواردك. يمكنك تحسين الأمان الخاصة بك عن طريق المساعدة من قبل Azure Security Center.

 ### أمان الشبكة

 تنفيذ تنفيذ تنفيذ تنفيذ الشبكة ، مثل ** مجموعات أمان الشبكة (NSGs) ** و ** جدار حماية Azure ** و ** تطبيق جدار حماية الويب (WAF) ** ، أمرًا ضروريًا بيئة لحماية Azure من الردود. تساعد هذه الرسالة في المساعدة في الحركة على المساعدة في الحركة.

 #### مجموعات أمان الشبكة (NSGs)

 هذا هو ما يسمح لك بإرسال الرسائل الإلكترونية ، وإدارة الرسائل الإلكترونية ، وإليها. على سبيل المثال ، إنشاء مجموعة NSG بقواعد أو رفض حركة مرور معينة:

 تعرف على المزيد حول [مجموعات أمان الشبكة](https://docs.microsoft.com/en-us/azure/virtual-network/security-overview) استخدم نطاقاً معروفاً بدلاً من السماح لكل مصادر IPv4 في الإنتاج؛ راجع [نظرة عامة على أمان NSG](https://learn.microsoft.com/en-us/azure/virtual-network/network-security-groups-overview).

 #### Azure Firewall
 شبكة مُدارة ومستندة إلى مجموعة النظراء تحمي موارد Azure الخاصة بك. وحدات تخزين وحدات التخزين حسن التدبير لتهيئة Azure Firewall، اتبع [دليل البدء السريع](https://learn.microsoft.com/en-us/azure/firewall-manager/quick-firewall-policy-bicep).

 #### جدار حماية تطبيقات الويب (WAF)
 حماية تطبيقات الويب (WAF) يمكن دمج WAF بسهولة مع تطبيقات الشاشة ، تكوين قواعد مخصصة للحماية من تعليمات محددة.

 فيما يلي مثال على كيفية إنشاء بوابة تطبيق مع WAF:
 تعرف على المزيد حول [جدار حماية تطبيق الويب](https://docs.microsoft.com/en-us/azure/web-application-firewall/ag/ag-overview)

 ### إدارة الهوية

 ** يعد Azure Active Directory (Azure AD) ** مكونًا أساسيًا لتأمين بيئة السحابة الخاصة بك. يوفر Azure Security Center توصيات لإدارة الهوية ، مثل تفعيل ** المصادقة متعددة العوامل (MFA) ** تنفيذ ** التحكم في المستند إلى الدور (RBAC) ** الأنشطة المشبوهة.

 #### المصادقة متعددة العوامل (MFA)

 تضيف المزيد من الأمان إلى حسابات Azure. يمكن تمكين العائالت المتعددة MFA لمؤسستك باتباع [الدليل التفصيلي](https://docs.microsoft.com/en-us/azure/active-directory/authentication/tutorial-enable-azure-mfa) المقدم بواسطة Microsoft.

 مثال: فتح MFA

 #### التحكم في الوصول المستند إلى الدور (RBAC)
 لقد كان ترتيبًا ضعيفًا. يمكنك تعيين أدوار أو مجموعات إدارة طلباتهم إلى إدارة مؤسستك. لتنفيذ RBAC ، اتبع [الدليل الرسمي](https://docs.microsoft.com/en-us/azure/role-based-access-control/overview) من Microsoft.

 مثال: تعيين دور لمستخدم
 #### مراقبة الأنشطة المشبوهة
 يوفر موقع Azure AD ميزات مثل ** حماية الهوية ** و ** الوصول المشروط ** التي على مراقبة أنشطة المشبوهة والاستجابة لها. تستخدم حماية الهوية خوارزميات التعلم الآلي في حالات الشاذة ومحاولات تسجيل الدخول المحفوفة بالمخاطر ، بينما يسمح لك الوصول إلى المحيط الهادئ

 لإعداد حماية هوية Azure AD ، اتبع [الدليل الرسمي](https://learn.microsoft.com/en-us/azure/active-directory/identity-protection/concept-identity-protection-b2b) من Microsoft.

 مثال: قم بسياسة وصول مشروط

 تعرف على المزيد حول [حماية هوية Azure AD](https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/overview) و [الوصول المشروط](https://learn.microsoft.com/en-us/azure/active-directory/conditional-access/overview).


 ### أمن البيانات

 حماية بياناتك في السحابة أمر بالغ الأهمية. يوفر رمز أمان بيانات Azure ، مثل ** حماية المعلومات في Azure ** و ** تشفير خدمة في Azure ** و ** تشفير خدمة في Azure **. حماية حفظ البيانات الآمنة.

 #### حماية معلومات Azure

 ** حماية المعلومات في Azure (AIP) ** هو حل قائم على السحابة على تصنيف ورسائل البريد الإلكتروني وتسميتها وحمايتها. يوفر AIP مجموعة من الملصقات المضمنة ، مثل "سري" و "شخصي" ، مشهد يمكن تخصيصها ، أيضًا تكوين AIP بدء استخدام AIP ، اتبع [الدليل الرسمي](https://docs.microsoft.com/en-us/azure/information-protection/what-is-information-protection) Azure Information Protection اسم تاريخي للمنتج وتشير وثائق Sentinel الحالية إلى إيقافه. راجع وثائق Microsoft Purview Information Protection قبل بدء نشر جديد..

 مثال: إنشاء مخصصة

 تسمّي وثائق Microsoft الحالية المنتج Azure Information Protection اسماً تاريخياً؛ وتذكر إرشادات توفر ميزات Sentinel أنه متوقف. راجع وثائق Microsoft Purview Information Protection الحالية قبل بدء نشر جديد.



#### تشفير خدمة تخزين Azure
 ** تشفير خدمة تخزين Azure (SSE **) يستخدم SSE المفاتيح المُدارة بواسطة العميل الخاضع تابع SSE ، اتبع [الدليل التفصيلي](https://docs.microsoft.com/en-us/azure/storage/common/storage-service-encryption) مقدم من Microsoft.

 مثال: تم فتح SSE لحسابها

 #### تشفير قرص Azure
 يساعدك على تشفير قرص Azure (Windows). تتم حماية مفاتيح التشفير بواسطة Azure Key Vault ، مما يضمن تأمين بياناتك في حالة السكون. تشفير قرص Azure ، اتبع [الدليل الرسمي](https://learn.microsoft.com/en-us/azure/virtual-machines/disk-encryption-overview) من Microsoft.

 مثال: تمكين تشفير قرص Azure لجهاز ظاهري
 تعرف على المزيد حول [حماية معلومات Azure](https://docs.microsoft.com/en-us/azure/information-protection/what-is-information-protection) ، [تشفير خدمة تخزين Azure](https://docs.microsoft.com/en-us/azure/storage/common/storage-service-encryption) و [Azure Disk Encryption](https://learn.microsoft.com/en-us/azure/virtual-machines/disk-encryption-overview).
 ______

 ## كشف الردود والاستجابة لها

 موقع Azure Security Center ، راهنًا ، راهنًا ، التكامل مع ** Azure Sentinel ** ، يمكنك مراقبة الحوادث والتحقيق فيها والاستجابة لها عبر بيئتك.

 ### كشف التهديد

 يستخدم Azure Security Center ** Azure Defender ** ، وهي مجموعة من الملابس الخارجية للهندسة ، والتهديدات ، وأمبيرات عروض الأسعار. عودة للخلفيات للخلفيات في Azure Defender موارد تصحيح Azure Defender ، اتبع [الدليل الرسمي](https://docs.microsoft.com/en-us/azure/security-center/defender-for-cloud-enable).

 مثال: تمكين Azure Defender للاشتراك

 ### الاستجابة للتهديد
 عند اكتشاف تهديد ، وشفاءه بسرعة وفاعلية. يوفر Azure Security Center إدارة ** Security Incident ** ، راقب التحقيق على التحقيق في الاستجابة لها. يمكنك أيضًا التكامل مع ** Azure Sentinel ** آلية تشغيل. تعرف على المزيد حول تكامل Azure Security Center مع Azure Sentinel في ** الصفحة الرسمية **.

 مثال: قم بتسابق دفتر تسجيل الدخول المنطق لـ Azure Sentinel
 أن يحتوي على ملف `playbook-definition.json` على تعريف كتاب قواعد اللعبة المنطقي. يمكنك العثور على المثال لكتب التشغيل الخاصة بـ Azure Sentinel في [مستودع Azure-Sentinel GitHub](https://github.com/Azure/Azure-Sentinel/tree/master/Playbooks).

 من خلال إمكانات الكامنة في Azure Security Center والتكامل في Azure Sentinel ، تعرف على المزيد حول [Azure Defender](https://learn.microsoft.com/en-us/azure/defender-for-cloud/enable-enhanced-security) و [Azure Sentinel](https://docs.microsoft.com/en-us/azure/sentinel/overview).
 ______

 يتبع التكامل الحالي إرسال تنبيهات Defender for Cloud إلى Microsoft Sentinel عبر [موصل Defender for Cloud](https://learn.microsoft.com/en-us/azure/sentinel/connect-defender-for-cloud). تحقّق من الموصل وقواعد جمع البيانات والتحليلات وسير عمل الحوادث في بوابة Defender أو Azure قبل الاعتماد على الأتمتة.** تحقق من استيعاب التنبيهات وقواعد التحليلات والملكية وأتمتة الاستجابة والاحتفاظ بالبيانات. يعرض [موصل Defender for

## المراقبة والإبلاغ

 تعدّ المراقبة يوفر Azure Security Center و Assure Security Center ، تقارير الامتثال **.

 ### لوحة القيادة الأمنية

 توفر لوحة معلومات الأمان في Azure Security Center نظرة عامة شاملة على وضع الأمان لديك. يعرض نقاط الأمان الخاصة بك وتوصيات الأمان وتنبيهات الأمان في المنطقة. توفر لوحة كبيرة أيضًا رؤى حول حالة الامتثال الخاصة بك وتسمح لك بتتبعك بمرور الوقت.

 ### تنبيهات الأمان

 يُنشئ Azure Security Center تنبيهات أمان عند اكتشاف تهديدات جديدة. توفر هذه التنبيهات معلومات مفصلة حول التهديد ، بالإضافة إلى التوصيات إلى السرعة. يمكنك تكوين Azure Security Center لإرسال إشعارات عبر البريد الإلكتروني أو الرسائل القصيرة أو الربط مع أدوات الجهات الخارجية مثل [Slack](https://slack.com/) أو [فرق Microsoft](https://www.microsoft.com/en-us/microsoft-teams/group-chat-software).

 ### تقارير الامتثال

 تقارير تقارير امتثال لأطر عمل تنظيم مختلف ، مثل GDPR و HIPAA و PCI DSS. قسم العلوم والتقارير.

 ______

 ## أفضل الممارسات لمركز أمان

 إلى أقصى استفادة من Azure Security Center ، ضع في اعتبارك تطبيق أفضل الممارسات التالية:

 1. ** تمكين Azure Security Center على جميع اشتراكاتك **: يعد ضمان حماية جميع اشتراكات Azure بواسطة Azure Security Center ، تأمين حماية البيئة سحابية آمنة.
 2. ** قم بمراجعة حساباتك الآمنة
 3. ** خدمات توصيات الأمان **: خدمات معالجة التوصيات المقدمة من Azure Security Center على تحسين وضع الأمان وتقليل الأسعار.
 4. ** مراقبة التنبيهات الأمنية **: مراجعة التنبيهات والرد عليها بيضا للتخفيف من الرطوبة والحفاظ على بيئة آمنة.
 5. ** ابق على اطلاع دائم على طلبات الامتثال **: تأكد من أن تجد نفسك تجد نفسك دائمًا في حالة مطبعة.

 ______
## سير العمل الحالي في Defender for Cloud

استخدم التسلسل التالي للنشر الحالي. تظل الأسماء الواردة في الأقسام الأصلية مفيدة عند البحث عن المعلومات التاريخية، لكن البوابة والوثائق تستخدمان مصطلحات Defender for Cloud.

1. **احصر الاشتراكات والموصلات.** سجّل اشتراكات Azure وموصلات AWS أو GCP ومشروعات DevOps والموارد المهمة.
2. **فعّل خطط Defender المطلوبة.** اختر الخطط حسب أحمال العمل، وتأكد من الترخيص قبل تفعيلها على اشتراكات الإنتاج.
3. **راجع Secure Score وتوصيات السحابة.** أعط الأولوية للتعرض للإنترنت ومخاطر الهوية والثغرات القابلة للاستغلال ونقص التسجيل. لا تعتبر الدرجة دليلاً على الامتثال الكامل.
4. **اضبط عناصر تحكم Microsoft Entra.** اشترط MFA مقاومة للتصيد للحسابات المهمة، واستخدم RBAC بأقل الامتيازات، وراجع الوصول المميز.
5. **أرسل التنبيهات إلى Microsoft Sentinel.** تحقّق من استيعاب التنبيهات وقواعد التحليلات والملكية وأتمتة الاستجابة والاحتفاظ بالبيانات.
6. **أعد الفحص بعد التغييرات.** راجع التوصيات بعد التصحيح أو تغييرات البنية أو إضافة موصلات أو تغيير الخطط.

## قائمة مراجعة عملية

- **الهوية:** أزل الحسابات القديمة، وقلّل صلاحيات المسؤول الدائمة، وراجع استثناءات الوصول المشروط.
- **الشبكة:** أزل منافذ الإدارة العامة، وضيّق نطاقات مصادر NSG، وتحقق من وصول سجلات الجدار الناري وWAF إلى مساحة عمل المراقبة.
- **البيانات:** صنّف مخازن البيانات الحساسة، وتحقق من التشفير وملكية المفاتيح، واختبر استعادة النسخ الاحتياطية.
- **الكشف:** تحقق من شدة التنبيهات وتوجيه الإشعارات وملكية الحوادث وإجراءات الاستجابة.
- **الحوكمة:** اربط كل مبادرة سياسة بمالك وتاريخ انتهاء للاستثناء وأدلة على الإطار المطلوب.


 ## مراجع
- [وثائق مركز أمان Azure](https://docs.microsoft.com/en-us/azure/security-center/)
- [خدمة سياسة Azure](https://docs.microsoft.com/en-us/azure/governance/policy/)
- [NIST 800-53](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final)
- [رابطة الدول المستقلة](https://www.cisecurity.org/)
- [ISO 27001](https://www.iso.org/isoiec-27001-information-security.html)
- [اللائحة العامة لحماية البيانات](https://gdpr.eu/)
- [HIPAA](https://www.hhs.gov/hipaa/index.html)
- [PCI DSS](https://www.pcisecuritystandards.org/)
