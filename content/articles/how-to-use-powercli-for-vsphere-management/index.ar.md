---
title: "إتقان PowerCLI لإدارة vSphere"
date: 2023-08-02
lastmod: 2026-11-14
toc: true
draft: false
description: "تعرّف على استخدام PowerCLI لإدارة VMware vSphere وأتمتة المهام وتحسين الإنتاجية."
genre: ["التقنية", "الافتراضية", "VMware", "إدارة تقنية المعلومات", "الأتمتة", "واجهة سطر الأوامر", "البرمجة النصية", "إدارة الأنظمة", "الحوسبة السحابية", "إدارة مراكز البيانات"]
tags: ["PowerCLI", "VMware PowerCLI", "تثبيت PowerCLI", "تنزيل PowerCLI", "الاتصال بـ vCenter عبر PowerCLI", "إدارة vSphere", "إدارة الأجهزة الافتراضية", "إدارة المضيفين", "الأتمتة", "البرمجة النصية", "الافتراضية", "خادم vCenter", "مضيفو ESXi", "إدارة مخازن البيانات", "إدارة محولات الشبكة", "إنشاء الأجهزة الافتراضية", "إزالة الأجهزة الافتراضية", "إعدادات الأجهزة الافتراضية", "إدارة موارد المضيف", "تخصيص CPU", "تخصيص الذاكرة", "إعدادات التخزين", "أمثلة PowerCLI", "وثائق PowerCLI", "إدارة تقنية المعلومات", "إدارة الأنظمة", "الحوسبة السحابية"]
cover: "/img/cover/An_illustrated_cartoon_image_showcasing_a_pers.webp"
coverAlt: "رسم توضيحي لشخص يستخدم أوامر PowerCLI لإدارة الأجهزة الافتراضية والمضيفين في بيئة vSphere."
coverCaption: "حسّن إدارة vSphere باستخدام PowerCLI"
---

## مقدمة

**PowerCLI** أداة **واجهة سطر أوامر (CLI)** تقدمها **VMware**، وتتيح للمسؤولين **إدارة بيئات VMware vSphere وأتمتتها**. تساعد مجموعة **cmdlets** الواسعة على تبسيط المهام الإدارية وزيادة الإنتاجية، للمبتدئين وذوي الخبرة. يشرح هذا المقال التثبيت والاتصال بـ vCenter واستخدام PowerCLI بفاعلية.

______

## تثبيت PowerCLI

ثبّت PowerCLI على جهازك باتباع الخطوات التالية:

1. **نزّل** أداة تثبيت PowerCLI من موقع VMware الرسمي. ستجد الرابط في [وثائق PowerCLI](https://code.vmware.com/web/dp/tool/vmware-powercli). اختر الإصدار المناسب لنظام التشغيل.
2. **شغّل** أداة التثبيت واتبع التعليمات. اختر موقع التثبيت والخيارات المناسبة.
3. انقر على «Finish» لإكمال التثبيت. أصبح PowerCLI جاهزًا للاستخدام.

______

## الاتصال بـ vCenter باستخدام PowerCLI

بعد تثبيت PowerCLI، اتصل بخادم vCenter لإدارة البنية التحتية الافتراضية باستخدام cmdlets.

1. شغّل PowerCLI من قائمة Start أو اختصار سطح المكتب.
2. نفّذ الأمر التالي للاتصال بـ vCenter:

```powershell
Connect-VIServer -Server <vCenter IP or hostname>
```

استبدل `<vCenter IP or hostname>` بعنوان IP الفعلي أو اسم المضيف لخادم vCenter.

3. أدخل بيانات اعتماد حساب لديه صلاحيات كافية لإدارة vCenter عندما يُطلب منك ذلك.
4. تحقّق من الاتصال بأمر بسيط مثل **Get-VMHost**. ظهور قائمة مضيفي ESXi يعني نجاح الاتصال.

______

## استخدام PowerCLI لإدارة vSphere

بعد الاتصال بـ vCenter، يمكنك تنفيذ مهام شائعة.

### استرداد المعلومات

يوفر PowerCLI أوامر cmdlet لاسترداد معلومات بيئة vSphere:

- **Get-VM**: يسترد معلومات الأجهزة الافتراضية.
- **Get-VMHost**: يسترد معلومات مضيفي ESXi.
- **Get-Datastore**: يسترد معلومات مخازن البيانات.
- **Get-NetworkAdapter**: يسترد معلومات محولات الشبكة.

استخدم المعلمات لتصفية النتائج وتنسيقها.

### أتمتة المهام

تتمثل إحدى مزايا PowerCLI في أتمتة المهام المتكررة. تنفّذ بضعة أسطر عمليات معقدة على عدة كائنات.

#### إنشاء لقطات لجميع الأجهزة الافتراضية في مجلد

```PowerShell
## إيقاف تشغيل جميع الأجهزة الافتراضية على مضيف محدد
Get-VMHost -Name "MyHost" | Get-VM | Stop-VM

## إنشاء لقطة لجميع الأجهزة الافتراضية في مجلد محدد
Get-Folder -Name "MyFolder" | Get-VM | New-Snapshot -Name "DailySnapshot" -Description "Daily Backup"
```

يوضح هذا البرنامج النصي كيفية إيقاف الأجهزة الافتراضية على مضيف محدد وإنشاء لقطات للأجهزة الموجودة في مجلد.

#### إيقاف جميع الأجهزة الافتراضية في مجلد بأمان

```PowerShell
## استرداد المجلد الذي يحتوي على الأجهزة الافتراضية المطلوب إيقافها
$folder = Get-Folder -Name "MyFolder"

## استرداد جميع الأجهزة الافتراضية ضمن المجلد المحدد
$vms = Get-VM -Location $folder

## إيقاف تشغيل جميع الأجهزة الافتراضية بطريقة منظمة
foreach ($vm in $vms) {
    if ($vm.PowerState -eq "PoweredOn") {
        $vm | Shutdown-VMGuest -Confirm:$false
    }
}
```

يسترد البرنامج النصي المجلد باستخدام `Get-Folder` ثم أجهزته الافتراضية باستخدام `Get-VM`. تتحقق حلقة `foreach` من كل جهاز. إذا كانت حالته «PoweredOn»، يبدأ `Shutdown-VMGuest` إيقاف التشغيل المنظم. يتجاوز `-Confirm:$false` مطالبة التأكيد. بهذه الطريقة تتوقف الأجهزة في المجلد بترتيب آمن. تتيح لك إمكانات البرمجة النصية في PowerCLI إنشاء تدفقات عمل آلية تناسب متطلباتك.

### إدارة الأجهزة الافتراضية والمضيفين

يدعم PowerCLI مهام إدارة متنوعة:

- **إنشاء الأجهزة الافتراضية وإزالتها**: استخدم **`New-VM`** و **`Remove-VM`**. يقبل **[الأمر New-VM](https://developer.vmware.com/docs/powercli/latest/vmware.vimautomation.core/commands/new-vm/#DefaultParameterSet)** إعدادات CPU والذاكرة والقرص والشبكة أثناء الإنشاء.
- **تعديل إعدادات الأجهزة الافتراضية**: غيّر CPU والذاكرة والقرص والشبكة. يتيح **[الأمر Set-VM](https://developer.vmware.com/docs/powercli/latest/vmware.vimautomation.core/commands/set-vm/#DefaultSet)** تعديل تخصيص CPU والذاكرة.
- **إدارة موارد المضيف**: أدر CPU والذاكرة والشبكة والتخزين. يغيّر **[الأمر Set-VMHost](https://vdc-repo.vmware.com/vmwb-repository/dcr-public/e7c1a32c-a3c6-4d7c-91bb-18a86a38daf7/12353298-ce6e-4d3f-bd8d-ab9f5ab044cc/doc/Set-VMHost.html)** إعدادات شبكة المضيف وتخزينه.

هذه بعض أمثلة إدارة vSphere باستخدام PowerCLI. تساعد مجموعة cmdlets الواسعة على أتمتة المهام الإدارية وتبسيطها.

## الخلاصة

**PowerCLI** أداة مفيدة لإدارة بيئات VMware vSphere وأتمتتها. تبسّط cmdlets المهام الإدارية وتحسن الإنتاجية. بعد التثبيت والاتصال بـ vCenter، يمكنك استرداد المعلومات وأتمتة المهام وإدارة الأجهزة الافتراضية والمضيفين بكفاءة.

استكشف PowerCLI لتبسيط إدارة vSphere.


## المراجع
- [وثائق PowerCLI](https://code.vmware.com/web/dp/tool/vmware-powercli)
- [Connect-VIServer: مرجع أوامر VMware PowerCLI](https://docs.vmware.com/en/VMware-PowerCLI/latest/VMware.VimAutomation.Core/Connect-VIServer.html)
- [Get-VM: مرجع أوامر VMware PowerCLI](https://developer.vmware.com/docs/powercli/latest/vmware.vimautomation.core/commands/get-vm/#Default)
