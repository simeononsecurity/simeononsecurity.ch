---
title: "برنامج Windows STIG المستقل: إنشاء حاسوب متوافق"
date: 2023-02-02
lastmod: 2026-11-09
toc: true
draft: false
description: "دليل خطوة بخطوة لاستخدام Standalone-Windows-STIG-Script لإعداد أنظمة Windows متوافقة، مع شرح المعلمات وطرق التحقق."
tags: ["برنامج STIG النصي", "أمن Windows", "نظام Windows متوافق", "تقوية النظام", "STIG لنظام Windows", "Windows آمن", "الامتثال لمتطلبات Windows", "التثبيت اليدوي", "تحديثات Windows", "Adobe Reader", "Firefox", "Chrome", "Internet Explorer 11", ".NET Framework", "Office", "OneDrive", "Java", "Windows Defender", "جدار حماية Windows", "إجراءات التخفيف", "Nessus PID", "VMware Horizon", "تقوية اختيارية"]
cover: "/img/cover/create-compliant-windows-desktop-systems-with-standalone-windows-stig-script.webp"
coverAlt: "رسم توضيحي لشاشة حاسوب تعرض واجهة امتثال أمني بأشرطة تقدم متحركة وتدفقات بيانات على خلفية كحلية داكنة مع ألوان بارزة."
coverCaption: ""
---

تُستخدم أنظمة Windows على نطاق واسع في الشركات والمؤسسات وحتى المنازل. ومع تزايد الهجمات الإلكترونية، عليك التأكد من أن هذه الأنظمة آمنة ومتوافقة مع المعايير المعتمدة. يساعدك Standalone-Windows-STIG-Script على تحقيق ذلك. يشرح هذا المقال ماهية البرنامج وكيفية عمله واستخدامه لإنشاء نظام Windows آمن ومتوافق.

## ما هو Standalone-Windows-STIG-Script؟

**Standalone-Windows-STIG-Script** برنامج نصي طوّرته Simeononsecurity لأتمتة تأمين نظام Windows ومواءمته مع دليل التنفيذ الفني للأمن (STIG). البرنامج مفتوح المصدر ومتاح على **GitHub**.

## كيف يعمل؟

ينفذ Standalone-Windows-STIG-Script الإرشادات الواردة في STIG لتأمين نظام Windows. شغّل البرنامج على نظام Windows، وسيجري التغييرات اللازمة لتحقيق الامتثال لـ STIG. ويغطي مجموعة من إجراءات الأمان، منها:

- سياسات الحسابات
- سياسات التدقيق
- خيارات الأمان
- إعدادات جدار الحماية
- إعدادات الخدمات

## فوائد استخدام Standalone-Windows-STIG-Script:

- **الأتمتة**: يؤتمت البرنامج عملية تأمين نظام Windows، ما يوفر الوقت ويقلل احتمال الخطأ البشري.

- **الامتثال**: يطبق البرنامج إرشادات STIG، ويساعد على جعل نظام Windows متوافقًا مع المعايير المعتمدة.

- **راحة البال**: يساعدك استخدام Standalone-Windows-STIG-Script على الاطمئنان إلى أمان نظام Windows وامتثاله للمعايير.

_________________________________________________________________________________________________________________________

## كيفية استخدام Standalone-Windows-STIG-Script:

1. استخدام Standalone-Windows-STIG-Script مباشر نسبيًا. اتبع الخطوات التالية:

2. **تنزيل البرنامج النصي**: يتوفر البرنامج على GitHub عبر https://github.com/simeononsecurity/Standalone-Windows-STIG-Script. نزّله واحفظه على نظام Windows.

3. **فتح موجه أوامر بصلاحيات مرتفعة**: انقر بزر الماوس الأيمن على زر ابدأ في Windows واختر "Windows PowerShell (Admin)".

4. **تشغيل البرنامج النصي**: انتقل إلى المجلد الذي حفظت فيه البرنامج وشغّله بإدخال الأمر التالي:

```powershell
powershell.exe -ExecutionPolicy Bypass -File Standalone-Windows-STIG-Script.ps1
```

5. راجع التغييرات: بعد انتهاء البرنامج، افحص التغييرات التي أُجريت على النظام للتأكد من ضبط كل شيء كما ينبغي.

## الخلاصة:

Standalone-Windows-STIG-Script أداة تساعد على تأمين نظام Windows ومواءمته مع المعايير المعتمدة. يتيح لك البرنامج أتمتة عملية التأمين وتطبيق إرشادات STIG. إذا أردت إنشاء نظام Windows آمن ومتوافق، ففكر في استخدام Standalone-Windows-STIG-Script.
