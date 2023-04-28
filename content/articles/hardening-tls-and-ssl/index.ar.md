---
title: "Hardening Your Computer's Security by Disabling SSL and TLS 1.2 and Below"
date: 2023-02-08
toc: true
draft: false
description: "This article discusses the steps to improve data security by disabling older versions of SSL and TLS protocols, which are vulnerable to cyber threats such as POODLE, BEAST, and Heartbleed, in Windows and Linux systems."
tags: ["Hardening computer security", "Disabling SSL and TLS", "Data security", "POODLE", "BEAST", "Heartbleed", "Windows registry editor", "Linux OpenSSL configuration", "Apache", "Nginx"]
cover: "/img/cover/A_computer_with_a_padlock_symbol_representing_data_security.png"
coverAlt: "A computer with a padlock symbol representing data security"
coverCaption: ""
---
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
# Disable DTLS 1.1
Disable-Protocol -Protocol "DTLS 1.1"

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
 ## مقدمة:  أصبحت أجهزة الكمبيوتر جانبًا حاسمًا في حياتنا اليومية ، ومع ذلك ، نمت الحاجة إلى أمان البيانات بشكل كبير. الطرق المختلفة لتأمين البيانات أثناء التحميل ، SSL (Secure Socket Layer) و TLS (بروتوكول أمان طبقة النقل) هما بروتوكولات تستخدم في نطاق واسع. الاتصالات الإلكترونية القديمة. هذه المقالة ، سنناقش خطوات تقوية أجهزة الكمبيوتر عن طريق تعطيل SSL وإصدارات TLS 1.2 وما يليها للحفاظ على أمان البيانات.  ### لماذا تعطيل SSL و TLS 1.2 والإصدارات الأقدم؟  الإصدارات الأقدم من SSL و TLS معرضة التهديدات من التهديدات الأمنية مثل POODLE (Padding Oracle Ongraded Legacy Encryption) و BEAST (متصفح استغلال ضد SSL / TLS) و Heartbleed. تلك الهجمات التي تؤدي إلى إطلاق النار على معلومات حساسة ، مما يجعل تشغيل استخدام البروتوكولات القديمة.  ### تعطيل SSL و TLS 1.2 والإصدارات الأقدم في Windows:  يمكن تعطيل عملية تعطيل SSL و TLS 1.2 والإصدارات الأقل من محرر التسجيل. إليك نص بوويرشيل لإنجاز المهمة:   #### تعطيل SSL و TLS 1.2 والإصدارات الأقدم في Linux:  في Linux ، يمكن تحقيق عملية تعطيل SSL و TLS 1.2 وما دونه من خلال تعديل ملف تكوين OpenSSL. فيما يلي الخطوات التي يجب اتباعها:  1. افتح الجهاز وقم بتسجيل الدخول كجذر. 2. انتقل إلى ملف تكوين OpenSSL. عادةً ما يكون موجودًا في /etc/ssl/openssl.cnf. 3. افتح الملف باستخدام محرر نصوص مثل nano أو vim. 4. حدد موقع توجيه SSLProtocol وقم بتعيين قيمته إلى -TLSv1.2. 5. احفظ الملف وأغلق محرر النصوص. 6. أعد تشغيل الخدمات التي تستخدم OpenSSL ، مثل Apache أو Nginx ، حتى تدخل التغييرات حيز التنفيذ.  ## خاتمة:  من خلال تعطيل SSL وجميع إصدارات TLS 1.2 وما دونها ، يمكنك تعزيز أمان الكمبيوتر وحماية المعلومات الحساسة من التهديدات السيبرانية المحتملة. إنها عملية بسيطة يمكن إنجازها بأقل جهد ، مما يجعلها جانبًا مهمًا للحفاظ على أمان جهاز الكمبيوتر الخاص بك. من خلال تنفيذ الخطوات الموضحة في هذه المقالة ، يمكنك الحفاظ على أمان بياناتك ومنع الهجمات الإلكترونية ، وبالتالي تقليل مخاطر الكشف عن المعلومات الحساسة.  من المهم ملاحظة أنه في حين أن تعطيل هذه الإصدارات القديمة من بروتوكولات SSL و TLS يمكن أن يحسن أمان جهاز الكمبيوتر الخاص بك ، إلا أنه يمكن أن يؤثر أيضًا على التوافق مع بعض الأنظمة القديمة. لذلك ، من الضروري إجراء اختبار شامل للتغييرات التي تم إجراؤها والتأكد من عدم وجود آثار سلبية على نظامك قبل تنفيذها بالكامل.  في الختام ، يعد تقوية جهاز الكمبيوتر الخاص بك عن طريق تعطيل SSL وجميع إصدارات TLS 1.2 وما بعدها خطوة مهمة في الحفاظ على أمان المعلومات الحساسة ومنع الهجمات الإلكترونية. توفر الخطوات الموضحة في هذه المقالة دليلًا مباشرًا لتأمين جهاز الكمبيوتر الخاص بك ، مما يسهل على الأفراد والمؤسسات تنفيذ الإجراءات الأمنية الضرورية.