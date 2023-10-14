---
title: "تشغيل pfSense على جهاز HP t740 Thin Client: تلميحات ودليل استكشاف الأخطاء وإصلاحها"
draft: false
toc: true
date: 2023-04-29
description: "تعرف على كيفية إعداد pfSense على جهاز HP t740 Thin Client ، وكيفية استكشاف المشكلات المحتملة وإصلاحها مثل التجميد ومشاكل اكتشاف SSD."
tags: ["pfSense", "OPNsense", "تصلب", "طابعة HP t740", "عميل رفيع", "خادم المنزل", "PPPOE", "فري بي إس دي", "موجه التمهيد", "loader.conf.local", "محرر نانو", "كشف SSD", "محرك الأقراص M.2 SSD", "ويسترن ديجيتال", "استكشاف الأخطاء وإصلاحها", "بعد التثبيت", "UART", "ESXi", "بروكسموكس"]
cover: "/img/cover/A_cartoon_of_a_wizard_casting_a_spell_to_fix_a_frozen_computer.png"
coverAlt: "رسم كاريكاتوري لمعالج يلقي تعويذة لإصلاح جهاز كمبيوتر مجمّد ، مع فقاعة كلام تقول تم حل المشكلة"
coverCaption: ""
canonical: "https://simeononsecurity.com/guides/installing-pfsense-on-hp-t740-thin-client/"
---
 pfSense أو OPNsense أو HardenedBSD على جهاز HP t740 Thin Client **

إذا كنت تبحث عن جهاز قوي لتشغيل pfSense أو OPNsense أو HardenedBSD ، فقد يكون HP t740 Thin Client هو الخيار المناسب لك.

## خادم منزلي أكثر قوة ومضغوطًا

HP t740 Thin Client هو جهاز مضغوط يمكن استخدامه كصندوق pfSense قوي أو خادم منزلي مضغوط. إنه يوفر طاقة أكبر من t730 أو t620 Plus ، مما يجعله خيارًا مناسبًا لتشغيل PPPoE ، خاصة إذا كان لديك إنترنت فايبر. يمكن أن يوفر أيضًا مسار ترقية لشبكات 10 جيجابت.

## PS / 2 يتجمد

ومع ذلك ، إذا كنت تخطط لتشغيل FreeBSD أو مشتقاته مثل pfSense أو OPNsense أو HardenedBSD على المعدن العاري (على عكس ESXi أو Proxmox) ، فقد تواجه مشكلة حيث يتجمد النظام عند بدء تشغيل الرسالة `atkbd0: [GIANT-LOCKED]` لحسن الحظ ، يمكن حل هذه المشكلة عن طريق إدخال الأوامر التالية في موجه التمهيد:

```bash
unset hint.uart.0.at
unset hint.uart.1.at
```

* لاحظ أنك بحاجة إلى إلغاء ضبط كليهما ، وإلا فسيظل مغلقًا عند التمهيد. *

بعد تثبيت نظام التشغيل ، افتح shell بعد التثبيت وقم بتشغيل الأمر التالي:

```bash
vi /boot/loader.conf.local
```
ثم أضف هذين السطرين:
```bash
hint.uart.0.disabled="1"
hint.uart.1.disabled="1"
```

### استمر في التغييرات باستخدام VI
بالنسبة لأولئك الذين ليسوا على دراية بـ vi ، يمكنك إضافة السطر عن طريق القيام بما يلي:

مضيفا الخطوط `hint.uart.0.disabled="1"` و `hint.uart.1.disabled="1"` الى `/boot/loader.conf.local` باستخدام محرر vi ، يمكن القيام بالخطوات التالية:

1. افتح الجهاز على نظام FreeBSD الخاص بك.

2. النوع `vi /boot/loader.conf.local` واضغط على Enter لفتح الملف في محرر vi.

3. اضغط على `i` مفتاح للدخول في وضع الإدراج.

4. حرك المؤشر إلى أسفل الملف باستخدام مفاتيح الأسهم.

5. النوع `hint.uart.0.disabled="1"` بدون اقتباس.

6. اضغط على Enter لبدء سطر جديد.

7. النوع `hint.uart.1.disabled="1"` بدون اقتباس.

8. اضغط على `Esc` مفتاح للخروج من وضع الإدراج.

9. النوع `:wq` واضغط على Enter لحفظ الملف والخروج منه.

سيؤدي هذا إلى إضافة السطرين إلى `/boot/loader.conf.local` الذي سيعطل UARTs ويصلح مشكلة التجميد أثناء التمهيد على أجهزة HP t740 "Thin Client" معينة عند تشغيل FreeBSD أو مشتقاته مثل pfSense أو OPNsense أو HardenedBSD.

سيؤدي هذا إلى إصلاح المشكلة عبر عمليات إعادة التشغيل وترقيات البرامج الثابتة على pfSense / OPNsense.

## SSD

إذا كنت تستخدم HP M.2 eMMC ، فلن يتم اكتشافه في تثبيت FreeBSD خارج الصندوق. في هذه الحالة ، ستحتاج إلى محرك أقراص M.2 SSD تابع لجهة خارجية. يمكن لأي M.2 SSD أن يعمل ، SATA أو NVMe.

إذا كنت تبحث عن محرك أقراص M.2 SSD تابع لجهة خارجية لجهاز الكمبيوتر التابع جزئيًا HP t740 ، فنحن نوصي بالنظر في [Western Digital 500GB WD Blue SN570 NVMe](https://amzn.to/44bFCBk) or the [Western Digital 500GB WD Blue SA510 SATA](https://amzn.to/3AEbd0V) كل من هذين الخيارين موثوق به ويجب أن يعمل بشكل جيد مع جهازك. إذا كنت ترغب في الاستفادة من كلتا الفتحتين ، فستحتاج إلى كليهما. ستضحي بسرعات NVME ، لكنك ستحصل على بعض التكرار وهذا مهم جدًا.

لاحظ أن مؤلف هذه المقالة قد نجح في تشغيل pfSense CE 2.5.2 و OPNsense 22.1 على t740 دون أي مشاكل بعد اتباع الخطوات المذكورة أعلاه.

## استكشاف الأخطاء وإصلاحها وما بعد التثبيت

بعد التثبيت ، إذا واجهت أي مشاكل في تحرير الملفات ، يمكنك تثبيت محرر nano باستخدام `pkg update` و `pkg install nano` سيساعدك هذا في تحرير الملفات النصية بسهولة.

للتأكد من أن التغييرات التي تم إجراؤها على `/boot/loader.conf.local` يظل الملف موجودًا عبر ترقيات إصدار pfSense ، فأنت بحاجة إلى إضافة الأسطر التالية إلى `/boot/loader.conf` و `/etc/rc.conf.local` 
```bash
hint.uart.0.disabled="1"
hint.uart.1.disabled="1"
```

ومع ذلك ، في بعض الأحيان تحرير `/boot/loader.conf.local` الملف قبل إعادة التشغيل لا يحل المشكلة. في مثل هذه الحالات ، قد يكون من الضروري إضافة الأسطر التالية في بداية التمهيد الأول:

```bash
unset hint.uart.0.at
unset hint.uart.1.at
```

يجب أن تحل هذه الخطوات معظم المشكلات التي قد تنشأ أثناء عملية التثبيت وبعدها.

### مراجع:
- [HP t740 "Thin Client"](https://www8.hp.com/us/en/thin-clients/t740.html)
- [pfSense](https://www.pfsense.org/)
- [OPNsense](https://opnsense.org/)
- [HardenedBSD](https://hardenedbsd.org/)
- [ServeTheHome](https://www.servethehome.com/hp-t740-thin-client-review/)
- [FreeBSD (or pfSense/OPNsense) on the HP t740 Thin Client](https://www.neelc.org/posts/hp-t740-freebsd/)