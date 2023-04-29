---
title: "PowerShell DSC: Guía de inicio"
date: 2023-04-02
toc: true
draft: false
descripción: "Explora el poder de PowerShell Desired State Configuration (DSC) para automatizar y gestionar las configuraciones del sistema para un entorno seguro y compatible."
tags: ["PowerShell", "DSC", "Configuration Management", "Automation", "Windows", "System Administration", "Best Practices", "Compliance", "Security", "Infrastructure", "DevOps", "Server Configuration", "Testing", "Git", "Source Control", "Government Regulations", "NIST", "CIS", "Configuration Drift", "Custom Resources"]
cover: "/img/cover/A_cartoon_image_of_a_confident_system_administrator.png"
coverAlt: "Una imagen de dibujos animados de un administrador de sistemas seguro de sí mismo con una capa de superhéroe, de pie junto a un rack de servidores bien organizado, sosteniendo un script DSC de PowerShell en una mano y un escudo con el logotipo de Windows en la otra, protegiendo los servidores de la desviación de la configuración y las amenazas de seguridad."
coverCaption: ""
---
```powershell
Configuración InstallIIS {
    Import-DscResource -ModuleName PSDesiredStateConfiguration

    Nodo 'localhost' {
        WindowsFeature IIS {
            Ensure = 'Presente
            Name = 'Servidor Web
        }
    }
}
```
```powershell
InstallIIS
```
``powershell
Start-DscConfiguration -Path .\InstallIIS -Wait -Verbose
```


 ** دليل تكوين الحالة المرغوبة (DSC) من PowerShell ابتتكار التكوين **
 
 ______
 
 ## مقدمة
 
 يعد Configuración del estado deseado de PowerShell (** DSC **) أداة قوية و ** أساسية ** لمسؤولي تكنولوجيا المعلومات ومحترفي DevOps ، مما يسمح لهم بأتمتة نشر وتكوين أنظمة Windows و Linux. توفر هذه الحلول دليلاً شاملاً لاستخدام PowerShell DSC التكوين ، بما في ذلك أفضل الأنظمة واللوائح والمجلس.
 
 ______
 
 ## الشروع في تكوين الحالة المرغوبة لـ PowerShell
 
 ### ما هو تكوين الحالة الحالة في PowerShell؟
 
 تكوين الحالة المطلوبة لـ PowerShell (** DSC **) هي ** لغة تعريفية ** مدمجة في PowerShell المسؤولين عن الإدارة أتمتة تكوين الأنظمة الإلكترونية والتطبيقات. يوفر طريقة ** وسيطة ** لإدارة المعلومات والتأكد من بقاء المعلومات في الحالة المرغوبة.
 
 ### تثبيت PowerShell DSC
 
 ممارسة استخدام PowerShell DSC ، كساد إلى تثبيت ** Windows Management Framework (WMF) **. حزمة البيانات الخاصة بجماعة WMF ، يمكنك تنزيل أحدث إصدار من WMF من [مركز التنزيل لـ Microsoft] (https://www.microsoft.com/en-us/download/details.aspx؟id=54616).
 
 ______
 
 ## إنشاء أنت تكوينات DSC
 
 ### كتابة تكوينات DSC
 
 تكوين DSC هو ** نص برمجي PowerShell ** يصف الحالة المرغوبة الساعة. المساحة المطلوبة من DSC. فيما يلي مثال على تكوين DSC بسيط يقوم بتثبيت دور خادم الويب (IIS) على خادم Windows:
 
 ### تطبيق تكوينات DSC
 يمكنك وضع نموذج في DSC ، يمكنك تطبيقه على النظام الأول ، قم بتجميع البرنامج للتكوين عن طريقه في PowerShell:
 
 
 تحميل ملف ** MOF ** (تنسيق حدث مُدار) التكوين على التكوين المترجم. بعد ذلك ، كان الجزء الأول من الركب ، الذي وصفه بهذا الوصف:
 
 
 ## أفضل استخدام لاستخدام PowerShell DSC
 
 ### إضفاء الطابع النمطي على التكوينات الخاصة بك
 
 أنشئ ** تكوينات معيارية وقابلة للاستمرار في الاستخدام **. يتيح لك هذا سهولة التوسع في توسيع نطاقها ** مع نمو بيئتك.
 
 ### استخدام التحكم في المصدر
 
 قم بحفظ البيانات بتخزين تكوينات DSC والربط في ** نظام التحكم في المصدر ** مثل Git. تمكنك هذه من السابق
 
 ### اختبر التكوينات الخاصة بك
 
 يعتبر الاختبار ** جانبًا مهمًا من جوانب التكوين. قبل نشر تهيئة DSC ، اختبرها في ** إنشاء إنتاجية ** للتأكد من أنها تعمل كما هو متوقع ولا تقدم عواقب غير مقصودة. يمكنك أيضًا استخدام أدوات مثل [Pester] (https://github.com/pester/Pester) للاختبار التلقائي لتكوينينات DSC الخاصة بك.
 
 ______
 
 ## اللوائح والإرشادات الحكومية
 
 ### تلقَّى NIST
 
 يوفر المعهد الوطني للمعايير والتكنولوجيا (NIST) لتقديم تكوين النظام. على وجه الخصوص ، منشور منشور [NIST SP 800-53] (https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r5.pdf) على قسم (CM-2) حول تكوينات خط الأساس ، مشاهدة ذات صلة بالمشاهدة المباشرة. تؤكد المبادئ على الحفاظ على التغييرات في تكوينات النظام والمراقبتها والتحكم فيها. يمكن أن يساعد يساعد PowerShell DSC على الامتثال للاتفاق من خلال تقديم طريقة متسقة ومؤتمتة تكوينات النظام.
 
 ### قانون إدارة أمن المعلومات الفيدرالي (FISMA)
 
 FISMA (FISMA) (https: //www.dhs.gov/cisa/federal-information-security-modernization-act) إعداد القانون الرئيسي لأداء العمل في قانون العمل
 ______
 
 ## خاتمة
 
 يعد Configuración de estado fácil (DSC) de PowerShell أداة قوية ومرنة لأتمتة نشر وإدارة تكوينات النظام. باتباع أفضل الممارسات والالتزام باللوائح الحكومية ، يمكنك أن تشجع على المنافسة. لقد تم فتح باب السؤال في PowerShell DSC وتحسين عمليات إدارة التكوين الخاصة.
 ______
 
 ## مراجع
 
 - [المصدر الرسمي لـ Configuración de estado deseado (DSC) de PowerShell] (https://learn.microsoft.com/en-us/powershell/dsc/getting-started/wingettingstarted؟view=dsc-1.1)
 - [NIST SP 800-53 - ضوابط كبيرة لمنظومة الطوابع ff ff ff ff (https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r5.pdf)
 - [القانون الفيدرالي لإدارة أمن المعلومات (FISMA)] (https://www.dhs.gov/cisa/federal-information-security-modernization-act)
 - [Pester - إطار اختبار PowerShell] (https://github.com/pester/Pester)
 - [دليل المبتدئين التشفير] (https://simeononsecurity.ch/articles/a-beginners-guide-to-using-encryption-for-data-protection/)
 - [أفضل التصميمات في تصحيحات الأمان على Windows] (https://simeononsecurity.ch/articles/best-practices-for-installing-security-patches-on-windows/)
 
 
 
 
