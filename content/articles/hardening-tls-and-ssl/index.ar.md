---
title: "تقوية أمان الكمبيوتر بتعطيل SSL وTLS 1.1 والإصدارات الأقدم"
date: 2023-02-08
lastmod: 2026-11-13
toc: true
draft: false
description: "عطّل SSL وإصدارات TLS القديمة مع إبقاء TLS 1.2 أو أحدث. يتناول الدليل Schannel و.NET في Windows وخدمات Linux."
tags: ['تقوية أمان الكمبيوتر', 'تعطيل SSL وTLS', 'أمن البيانات', 'POODLE', 'BEAST', 'Heartbleed', 'محرر سجل Windows', 'إعداد OpenSSL في Linux', 'Apache', 'Nginx']
cover: "/img/cover/A_computer_with_a_padlock_symbol_representing_data_security.webp"
coverAlt: "كمبيوتر عليه رمز قفل يمثّل أمان البيانات"
coverCaption: ""
---

## مقدمة:

أصبحت أجهزة الكمبيوتر جزءًا أساسيًا من حياتنا اليومية، وزادت معها الحاجة إلى حماية البيانات. يُستخدم SSL (طبقة المقابس الآمنة) وTLS (أمن طبقة النقل) لحماية البيانات أثناء انتقالها. لكن الإصدارات القديمة أصبحت عرضة للهجمات. يشرح هذا المقال كيفية إيقاف SSL وTLS 1.0 و1.1 مع إبقاء TLS 1.2 أو TLS 1.3 متاحًا.

*TLS 1.2 ليس بروتوكولًا متقادمًا. الحد الأدنى الحالي هو TLS 1.2 أو أحدث. يعرّف [RFC 8446](https://www.rfc-editor.org/rfc/rfc8446) الإصدار TLS 1.3، بينما يعلن [RFC 8996](https://www.rfc-editor.org/rfc/rfc8996) رسميًا إيقاف TLS 1.0 وTLS 1.1.*

### لماذا نعطّل SSL وTLS 1.1 والإصدارات الأقدم؟

تتعرّض إصدارات SSL وTLS القديمة لتهديدات مثل POODLE (هجوم Padding Oracle على التشفير القديم بعد خفض الإصدار) وBEAST (استغلال المتصفح ضد SSL/TLS) وHeartbleed. قد تكشف هذه الهجمات معلومات حساسة، لذا يجب إيقاف البروتوكولات القديمة. أثّر Heartbleed في تطبيقات OpenSSL الضعيفة، ولم يكن إصدارًا من البروتوكول بحد ذاته. أصلح المكتبة وغيّر بيانات الاعتماد التي ربما انكشفت.

تسرد [إرشادات سجل Schannel الحالية من Microsoft](https://learn.microsoft.com/en-us/windows-server/security/tls/tls-registry-settings) إعدادات البروتوكولات لإصدارات Windows المدعومة. توصي Microsoft باستخدام نهج المجموعة أو أدوات الإدارة المدعومة الأخرى عند توفرها، وتخصّص تعديل السجل يدويًا للحالات التي لا يتوفر فيها خيار أفضل.

### تعطيل SSL وTLS 1.1 والإصدارات الأقدم في Windows:

في Windows، يمكن تعطيل البروتوكولات عبر سجل النظام. يضبط البرنامج النصي التالي إعدادات Schannel للعملاء والخوادم، ويطلب من .NET استخدام إعدادات TLS الافتراضية للنظام والتشفير القوي.

```powershell
Function Disable-Protocol {
    param (
        [Parameter(Mandatory=$true)]
        [string]$Protocol
    )
    $ServerPath = "HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\$Protocol\Server"
    $ClientPath = "HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\$Protocol\Client"
    New-Item -Path $ServerPath -Force
    New-Item -Path $ClientPath -Force
    Set-ItemProperty -Path $ServerPath -Force -Name Enabled -Type "DWORD" -Value 0
    Set-ItemProperty -Path $ServerPath -Force -Name DisabledByDefault -Type "DWORD" -Value 1
    Set-ItemProperty -Path $ClientPath -Force -Name Enabled -Type "DWORD" -Value 0
    Set-ItemProperty -Path $ClientPath -Force -Name DisabledByDefault -Type "DWORD" -Value 1
}
# Disable SSL v2
Disable-Protocol -Protocol "SSL 2.0"
# Disable SSL v3
Disable-Protocol -Protocol "SSL 3.0"
# Disable TLS 1.0
Disable-Protocol -Protocol "TLS 1.0"
# Disable DTLS 1.0
Disable-Protocol -Protocol "DTLS 1.0"
# Disable TLS 1.1
Disable-Protocol -Protocol "TLS 1.1"
# There is no DTLS 1.1 protocol. RFC 8996 deprecates DTLS 1.0 and retains DTLS 1.2.

function Set-NETStrongAuthentication {
    param(
        [string]$RegistryPath,
        [string]$Name,
        [string]$Type,
        [int]$Value
    )
    Set-ItemProperty -Path $RegistryPath -Force -Name $Name -Type $Type -Value $Value
}

$NETVersions = @("2.0.50727", "3.0", "4.0.30319")

foreach ($version in $NETVersions) {
    Set-NETStrongAuthentication -RegistryPath "HKLM:\SOFTWARE\Microsoft\.NETFramework\v$version" -Name SchUseStrongCrypto -Type "DWORD" -Value 0x00000001
    Set-NETStrongAuthentication -RegistryPath "HKLM:\SOFTWARE\Microsoft\.NETFramework\v$version" -Name SystemDefaultTlsVersions -Type "DWORD" -Value 0x00000001
    Set-NETStrongAuthentication -RegistryPath "HKLM:\SOFTWARE\WOW6432Node\Microsoft\.NETFramework\v$version" -Name SchUseStrongCrypto -Type "DWORD" -Value 0x00000001
    Set-NETStrongAuthentication -RegistryPath "HKLM:\SOFTWARE\WOW6432Node\Microsoft\.NETFramework\v$version" -Name SystemDefaultTlsVersions -Type "DWORD" -Value 0x00000001
}
```

#### تعطيل SSL وTLS 1.1 والإصدارات الأقدم في Linux:

في Linux، يعتمد تعطيل الإصدارات القديمة على التطبيق والمكتبة. لا يتجاوز تعديل `/etc/ssl/openssl.cnf` إعدادات كل خدمة أو مكتبة TLS مضمّنة. اتبع الخطوات التالية:

1. افتح الطرفية وسجّل الدخول بصلاحيات root.
2. انتقل إلى ملف إعداد OpenSSL، وغالبًا ما يوجد في /etc/ssl/openssl.cnf.
3. افتح الملف بمحرر نصوص مثل nano أو vim.
4. ابحث عن توجيه البروتوكول الخاص بالخدمة واضبط الحد الأدنى على TLS 1.2. كان الخيار القديم `-TLSv1.2` يعطّل TLS 1.2، لذا لا تستخدمه كحد حديث.
5. احفظ الملف وأغلق محرر النصوص.
6. أعد تشغيل الخدمات التي تستخدم OpenSSL، مثل Apache أو Nginx، لتطبيق التغييرات.

## الخلاصة:

يعزّز تعطيل SSL وTLS 1.1 والإصدارات الأقدم أمان الكمبيوتر مع إبقاء عملاء TLS الحديثة متوافقة. ينتمي الإعداد الصحيح إلى الخدمة التي تفاوض اتصال TLS، لذا اختبر كل تطبيق بدل افتراض أن ملف OpenSSL واحدًا يتحكم في جميع الخدمات.

قد يؤثر تعطيل هذه الإصدارات القديمة في التوافق مع بعض الأنظمة القديمة. اختبر التغييرات جيدًا وتأكد من عدم تسببها بمشكلات قبل تطبيقها بالكامل.

اتبع الخطوات الواردة في هذا المقال لحماية المعلومات الحساسة والحد من الهجمات. ابدأ بتحديد البروتوكول الذي تفاوضه كل خدمة، ثم وثّق الاستثناءات المؤقتة.

## قائمة التحقق الحالية

- **تحقق من البروتوكول المتفاوض عليه.** اختبر العميل والخادم باستخدام ماسح TLS أو اختبار داخلي معتمد من طرفي الاتصال.
- **أبقِ TLS 1.2 مفعّلًا.** ما زالت بعض التطبيقات القديمة تحتاج إليه، بينما يعتمد دعم TLS 1.3 على نظام التشغيل والمكتبة.
- **راجع DTLS على حدة.** يعلن RFC 8996 إيقاف DTLS 1.0، ولا يعرّف بروتوكول DTLS 1.1.
- **أعد تشغيل الخدمات المتأثرة.** غالبًا ما تحتاج إعدادات Schannel والتطبيقات إلى إعادة تشغيل الخدمة أو النظام كي تسري.
- **وثّق الاستثناءات.** سجّل كل نقطة قديمة تحتاج مؤقتًا إلى إعداد توافق، وحدد موعدًا لإيقافها.
