---
title: "إدارة Active Directory باستخدام PowerShell"
date: 2023-07-25
toc: true
draft: false
description: اكتشف كيفية تثبيت واستخدام وحدة Active Directory لـ PowerShell بفعالية لتبسيط مهام إدارة Active Directory في Windows.
genre:
- تكنولوجيا
- ويندوز
- PowerShell
- Active Directory
- الإدارة
- البرمجة النصية
- تكنولوجيا المعلومات
- الأتمتة
- خادم ويندوز
- مايكروسوفت
tags:
- وحدة Active Directory لـ PowerShell
- استيراد وحدة Active Directory في PowerShell
- وحدة Active Directory لـ Windows PowerShell
- تثبيت Active Directory PowerShell
- تثبيت Active Directory PowerShell
- تثبيت وحدة Active Directory PowerShell على Windows 10
- تثبيت وحدة Active Directory PowerShell على Windows 10
- الحصول على وحدة Active Directory PowerShell
- إدارة AD
- Active Directory في ويندوز
- أوامر PowerShell
- استرجاع معلومات AD
- إنشاء كائنات AD
- تعديل كائنات AD
- إدارة أمان AD
- إدارة مستخدمي AD
- إدارة مجموعات AD
- إدارة وحدات تنظيمية AD
- البرمجة النصية في PowerShell
- إدارة خادم ويندوز
- Microsoft PowerShell
- أتمتة مهام AD
- تثبيت وحدة PowerShell
- دليل إدارة AD
- إدارة Active Directory
- إدارة أمان AD
- أتمتة PowerShell
- أوامر Active Directory PowerShell
- مرجع أوامر PowerShell
cover: /img/cover/active-directory-module-powershell-installation-usage-guide.webp
coverAlt: رسم توضيحي لشاشة كمبيوتر تعرض وحدة تحكم PowerShell مع أوامر ملونة، محاطة بتمثيلات مجردة لحسابات المستخدمين والمجموعات، على خلفية داكنة.
coverCaption: افتح قوة إدارة Active Directory باستخدام PowerShell.
lastmod: 2026-10-08
---

## المقدمة

اليوم، إدارة وصيانة حسابات المستخدمين، مجموعات الأمان، والموارد الأخرى في بيئة Active Directory (AD) على Windows تتطلب عمليات فعالة ومبسطة. يوفر PowerShell، لغة البرمجة النصية القوية التي طورتها مايكروسوفت، **وحدة Active Directory** لتسهيل مهام إدارة AD. تقدم هذه الوحدة العديد من الأوامر التي تمكن المسؤولين من أتمتة العمليات المختلفة وإدارة AD بفعالية. في هذه المقالة، سنستعرض كيفية تثبيت واستخدام وحدة Active Directory لـ PowerShell.

## تثبيت وحدة Active Directory لـ PowerShell

لبدء استخدام وحدة Active Directory لـ PowerShell، يجب التأكد من تثبيتها على نظامك. قد تختلف عملية التثبيت حسب نظام التشغيل. فيما يلي خطوات تثبيت الوحدة على **Windows 10**، **Windows 11**، و**Windows Server**:

### ويندوز 10 وويندوز 11 - PowerShell
1. افتح **Windows PowerShell** بصلاحيات المسؤول.
2. نفذ الأمر التالي لتثبيت الوحدة:

```powershell
Add-WindowsCapability -Name Rsat.ActiveDirectory.DS-LDS.Tools~~~~0.0.1.0 -Online
```

1. انتظر حتى تكتمل عملية التثبيت. بمجرد الانتهاء، يمكنك البدء في استخدام وحدة Active Directory.

### خادم ويندوز
1. افتح **Windows PowerShell** بصلاحيات المسؤول.
2. نفذ الأمر التالي لتثبيت الوحدة:

```powershell
Install-WindowsFeature -Name "RSAT-AD-PowerShell" -IncludeAllSubFeature
```

3. انتظر حتى تكتمل عملية التثبيت. بمجرد الانتهاء، يمكنك البدء في استخدام وحدة Active Directory.

### الأنظمة غير المتصلة بالإنترنت

تكون الأنظمة غير المتصلة بالإنترنت أكثر تعقيدًا قليلاً. هناك عدة طرق، لكن الطريقة التي نوصي بها هي استخدام البرنامج النصي التالي:
- [Offine-PS-ActiveDirectory-Install](https://github.com/simeononsecurity/Offine-PS-ActiveDirectory-Install)

## استيراد وحدة Active Directory في PowerShell

قبل أن تتمكن من استخدام وحدة Active Directory في PowerShell، تحتاج إلى استيرادها في الجلسة الحالية. اتبع الخطوات التالية لاستيراد الوحدة:

1. افتح **Windows PowerShell** بصلاحيات المسؤول.
2. نفذ الأمر التالي لاستيراد الوحدة:

```powershell
Import-Module ActiveDirectory
```

3. سيتم استيراد وحدة Active Directory، ويمكنك الآن الوصول إلى أوامرها ووظائفها.

## استخدام وحدة Active Directory لـ PowerShell

بعد استيراد وحدة Active Directory، يمكنك الاستفادة من مجموعة الأوامر الغنية لأداء مهام إدارية مختلفة. إليك نظرة على بعض الأوامر الشائعة ووظائفها:

### استرجاع معلومات Active Directory

لإدارة بيئة Active Directory (AD) بفعالية، تحتاج إلى استرجاع معلومات حول كائنات AD المختلفة، مثل المستخدمين، المجموعات، والوحدات التنظيمية (OUs). يوفر PowerShell أوامر قوية تبسط عملية الاسترجاع.

- [**Get-ADUser**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-aduser?view=windowsserver2022-ps): يتيح لك هذا الأمر استرجاع معلومات مفصلة عن مستخدمي AD. يمكنك الحصول على خصائص مثل اسم المستخدم، اسم العرض، عنوان البريد الإلكتروني، والمزيد. على سبيل المثال، لاسترجاع جميع المستخدمين الذين تبدأ أسماؤهم بـ "johndoe"، يمكنك تنفيذ الأمر التالي:

  ```powershell
  Get-ADUser -Filter 'SamAccountName -like "johndoe*"'
  ```

  سيُرجع هذا الأمر قائمة بكائنات المستخدمين التي تطابق الفلتر المحدد.

- [**Get-ADGroup**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-adgroup?view=windowsserver2022-ps): باستخدام أمر Get-ADGroup، يمكنك جلب معلومات عن مجموعات AD. يوفر الوصول إلى تفاصيل مثل اسم المجموعة، الأعضاء، الوصف، والمزيد. على سبيل المثال، لاسترجاع جميع مجموعات الأمان في بيئة AD، يمكنك تنفيذ الأمر التالي:

  ```powershell
  Get-ADGroup -Filter 'GroupCategory -eq "Security"'
  ```

  سيعرض هذا قائمة بمجموعات الأمان في Active Directory.

- [**Get-ADOrganizationalUnit**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-adorganizationalunit?view=windowsserver2022-ps): يستخدم أمر Get-ADOrganizationalUnit لاسترجاع معلومات عن الوحدات التنظيمية (OUs) في AD. يسمح بالوصول إلى خصائص مثل اسم الوحدة التنظيمية، الوصف، الوحدة التنظيمية الأم، والمزيد. لاسترجاع جميع الوحدات التنظيمية في النطاق، يمكنك استخدام الأمر التالي:

  ```powershell
  Get-ADOrganizationalUnit -Filter *
  ```

  عند تنفيذ هذا الأمر، ستظهر قائمة بجميع الوحدات التنظيمية في Active Directory.

باستخدام هذه الأوامر القوية، يمكنك بسهولة استرجاع معلومات محددة عن مستخدمي AD، المجموعات، والوحدات التنظيمية، مما يتيح إدارة فعالة وفعالة لبيئة Active Directory الخاصة بك.


تتيح لك هذه الأوامر استرجاع خصائص محددة، تصفية النتائج، وإجراء استعلامات متقدمة لجلب المعلومات المطلوبة.

### إنشاء وإدارة كائنات Active Directory

عند العمل مع Active Directory (AD)، توفر وحدة Active Directory في PowerShell أوامر قوية لإنشاء وإدارة كائنات AD. إليك نظرة على بعض الأوامر الأساسية لإنشاء مستخدمي AD، المجموعات، والوحدات التنظيمية (OUs).

- [**New-ADUser**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/new-aduser?view=windowsserver2022-ps): يتيح لك هذا الأمر إنشاء مستخدم جديد في AD. يمكنك تحديد خصائص مثل اسم المستخدم، كلمة المرور، عنوان البريد الإلكتروني، والمزيد. على سبيل المثال، لإنشاء مستخدم جديد باسم المستخدم "john.doe" واسم العرض "John Doe"، يمكنك استخدام الأمر التالي:

  ```powershell
  New-ADUser -SamAccountName "john.doe" -Name "John Doe"
  ```

  سينشئ هذا الأمر مستخدمًا جديدًا في Active Directory.

- [**New-ADGroup**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/new-adgroup?view=windowsserver2022-ps): يمكّنك أمر New-ADGroup من إنشاء مجموعة جديدة في AD. يمكنك تعيين خصائص مثل اسم المجموعة، الوصف، نطاق المجموعة، والمزيد. لإنشاء مجموعة جديدة باسم "Marketing" مع وصف، يمكنك تنفيذ الأمر التالي:

  ```powershell
  New-ADGroup -Name "Marketing" -Description "Marketing Team"
  ```

  سينشئ هذا الأمر مجموعة جديدة في Active Directory.

- [**New-ADOrganizationalUnit**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/new-adorganizationalunit?view=windowsserver2022-ps): باستخدام الأمر New-ADOrganizationalUnit، يمكنك إنشاء وحدة تنظيمية جديدة في Active Directory. يمكنك تحديد خصائص مثل اسم الوحدة التنظيمية، الوحدة التنظيمية الأصل، والمزيد. على سبيل المثال، لإنشاء وحدة تنظيمية جديدة باسم "المبيعات" تحت وحدة "الأقسام"، يمكنك تشغيل الأمر التالي:

  ```powershell
  New-ADOrganizationalUnit -Name "Sales" -Path "OU=Departments,DC=contoso,DC=com"
  ```

  سيقوم هذا الأمر بإنشاء وحدة تنظيمية جديدة في هيكل Active Directory.

باستخدام هذه الأوامر، يمكنك بسهولة إنشاء مستخدمين جدد في AD، مجموعات، ووحدات تنظيمية بالخصائص والتكوينات المطلوبة، مما يتيح إدارة فعالة لبيئة Active Directory الخاصة بك.


### تعديل كائنات Active Directory

عندما يتعلق الأمر بتعديل خصائص وسمات كائنات Active Directory (AD) الموجودة، يوفر لك موديل Active Directory في PowerShell عدة أوامر مفيدة. فيما يلي نظرة على هذه الأوامر لتعديل مستخدمي AD، المجموعات، والوحدات التنظيمية (OUs).

- [**Set-ADUser**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/set-aduser?view=windowsserver2022-ps): يتيح لك الأمر Set-ADUser تعديل خصائص مستخدم AD. يمكنك تحديث سمات مثل اسم العرض، عنوان البريد الإلكتروني، رقم الهاتف، والمزيد. على سبيل المثال، لتغيير رقم هاتف مستخدم باسم المستخدم "john.doe"، يمكنك استخدام الأمر التالي:

  ```powershell
  Set-ADUser -Identity "john.doe" -PhoneNumber "123456789"
  ```

  سيقوم هذا الأمر بتعديل رقم الهاتف للمستخدم المحدد في Active Directory.

- [**Set-ADGroup**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/set-adgroup?view=windowsserver2022-ps): باستخدام الأمر Set-ADGroup، يمكنك تعديل خصائص مجموعة AD. يمكنك تحديث سمات مثل وصف المجموعة، العضوية، نطاق المجموعة، والمزيد. لتغيير وصف مجموعة باسم "التسويق" إلى "فريق التسويق"، يمكنك تنفيذ الأمر التالي:

  ```powershell
  Set-ADGroup -Identity "Marketing" -Description "Marketing Team"
  ```

  سيقوم هذا الأمر بتحديث وصف المجموعة المحددة في Active Directory.

- [**Set-ADOrganizationalUnit**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/set-adorganizationalunit?view=windowsserver2022-ps): يتيح لك الأمر Set-ADOrganizationalUnit تعديل خصائص وحدة تنظيمية في AD. يمكنك تغيير سمات مثل اسم الوحدة التنظيمية، الوصف، والمزيد. على سبيل المثال، لتعديل وصف وحدة تنظيمية باسم "المبيعات" إلى "قسم المبيعات"، يمكنك تشغيل الأمر التالي:

  ```powershell
  Set-ADOrganizationalUnit -Identity "OU=Sales,DC=contoso,DC=com" -Description "Sales Department"
  ```

  سيقوم هذا الأمر بتحديث وصف الوحدة التنظيمية المحددة في هيكل Active Directory.

باستخدام هذه الأوامر، يمكنك بسهولة تعديل خصائص وسمات كائنات AD، وإجراء التحديثات والتعديلات اللازمة لتلبية متطلبات مؤسستك.


### إدارة أمان Active Directory

بالإضافة إلى إدارة كائنات Active Directory (AD)، يوفر لك موديل Active Directory في PowerShell أوامر مخصصة للتعامل مع الجوانب الأمنية في AD. تساعد هذه الأوامر المسؤولين على إدارة وصول المستخدمين، عضويات المجموعات، والمهام المتعلقة بكلمات المرور بكفاءة داخل بيئة AD.

فيما يلي بعض الأوامر الشائعة المتعلقة بالأمان:

- [**Add-ADGroupMember**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/add-adgroupmember?view=windowsserver2022-ps): يتيح لك هذا الأمر إضافة أعضاء إلى مجموعة AD. من خلال تحديد المجموعة وحسابات المستخدمين أو المجموعات التي تريد إضافتها، يمكنك إدارة التحكم في الوصول بسهولة. على سبيل المثال، لإضافة مستخدم باسم "JohnDoe" إلى مجموعة "المديرون"، يمكنك استخدام الأمر التالي:

  ```powershell
  Add-ADGroupMember -Identity "Managers" -Members "JohnDoe"
  ```

- [**Remove-ADGroupMember**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/remove-adgroupmember?view=windowsserver2022-ps): باستخدام هذا الأمر، يمكنك إزالة أعضاء من مجموعة AD. من خلال تحديد المجموعة وحسابات المستخدمين أو المجموعات التي تريد إزالتها، يمكنك إدارة عضويات المجموعات بفعالية. على سبيل المثال، لإزالة مستخدم باسم "JaneSmith" من مجموعة "المطورون"، يمكنك استخدام الأمر التالي:

  ```powershell
  Remove-ADGroupMember -Identity "Developers" -Members "JaneSmith"
  ```

- [**Set-ADUserPassword**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/set-adaccountpassword?view=windowsserver2022-ps): يتيح لك هذا الأمر تعيين كلمة مرور لمستخدم AD. من خلال تحديد حساب المستخدم وتوفير كلمة مرور جديدة، يمكنك فرض سياسات كلمات المرور وضمان مصادقة المستخدم بشكل آمن. إليك مثالاً على تعيين كلمة مرور جديدة لمستخدم باسم "AmyJohnson":

  ```powershell
  Set-ADUserPassword -Identity "AmyJohnson" -NewPassword (ConvertTo-SecureString -AsPlainText "NewPassword123" -Force)
  ```

باستخدام هذه الأوامر المتعلقة بالأمان، يمكن للمسؤولين إدارة وصول المستخدمين، عضويات المجموعات، وسياسات كلمات المرور بفعالية داخل بيئة Active Directory.

## مثال على سكربت لموديل Active Directory في PowerShell
```powershell
# Import Active Directory module
Import-Module ActiveDirectory

# Retrieve Active Directory information
Get-ADUser -Filter 'SamAccountName -like "johndoe*"'
Get-ADGroup -Filter 'GroupCategory -eq "Security"'
Get-ADOrganizationalUnit -Filter *

# Create a new Active Directory user
New-ADUser -SamAccountName "john.doe" -Name "John Doe"

# Create a new Active Directory group
New-ADGroup -Name "Marketing" -Description "Marketing Team"

# Create a new Active Directory organizational unit
New-ADOrganizationalUnit -Name "Sales" -Path "OU=Departments,DC=contoso,DC=com"

# Modify Active Directory objects
Set-ADUser -Identity "john.doe" -PhoneNumber "123456789"
Set-ADGroup -Identity "Marketing" -Description "Marketing Team"
Set-ADOrganizationalUnit -Identity "OU=Sales,DC=contoso,DC=com" -Description "Sales Department"

# Manage Active Directory security
Add-ADGroupMember -Identity "Managers" -Members "JohnDoe"
Remove-ADGroupMember -Identity "Developers" -Members "JaneSmith"
Set-ADUserPassword -Identity "AmyJohnson" -NewPassword (ConvertTo-SecureString -AsPlainText "NewPassword123" -Force)
```

## الخاتمة

في الختام، يُعد **موديل Active Directory لـ PowerShell** أداة قوية تتيح إدارة فعالة ومريحة لـ Windows Active Directory. من خلال تثبيت واستيراد الموديل، تحصل على مجموعة شاملة من **الأوامر** التي تبسط مختلف المهام المتعلقة بـ AD.

مع موديل Active Directory، يمكنك تنفيذ العديد من العمليات مثل استرجاع المعلومات عن كائنات AD، إنشاء كائنات جديدة، تعديل الخصائص، وإدارة الأمان. يساعد هذا الموديل المسؤولين على أتمتة المهام الإدارية، تبسيط سير العمل، وضمان سير عمل سلس لبيئات Active Directory.

باستخدام **PowerShell** و**موديل Active Directory**، يمكنك تعزيز قدرات إدارة AD وتحسين كفاءة عمليات إدارة AD. سواء كنت مسؤول نظام، محترف تكنولوجيا معلومات، أو مدير Active Directory، يزودك موديل Active Directory بالأدوات اللازمة لإدارة بنية AD الخاصة بك بفعالية.

استفد من قوة **PowerShell** و**موديل Active Directory** لتبسيط مهام إدارة AD، زيادة الإنتاجية، والحفاظ على بيئة Active Directory آمنة ومنظمة بشكل جيد.

## المراجع

- [Install-WindowsFeature cmdlet - مستندات مايكروسوفت](https://docs.microsoft.com/en-us/powershell/module/servermanager/install-windowsfeature)
- [Import-Module cmdlet - مستندات مايكروسوفت](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/import-module)
- [أوامر Active Directory في PowerShell - مستندات مايكروسوفت](https://docs.microsoft.com/en-us/powershell/module/activedirectory)
