---
title: "Endurece la seguridad de tu ordenador desactivando SSL y TLS 1.2 e inferiores"
date: 2023-02-08
toc: true
draft: false
description: "Este artículo analiza los pasos para mejorar la seguridad de los datos deshabilitando versiones antiguas de los protocolos SSL y TLS, vulnerables a ciberamenazas como POODLE, BEAST y Heartbleed, en sistemas Windows y Linux."
tags: ["Endurecimiento de la seguridad informática", "Deshabilitar SSL y TLS", "Seguridad de datos", "POODLE", "BEAST", "Heartbleed", "Editor del registro de Windows", "Configuración de OpenSSL en Linux", "Apache", "Nginx"]
cover: "/img/cover/Ordenador_con_un_símbolo_de_bloqueo_que_representa_la_seguridad_de_los_datos.png"
coverAlt: "Un ordenador con el símbolo de un candado que representa la seguridad de los datos"
coverCaption: ""
---
```powershell
Función Disable-Protocol {
    param (
        [Parámetro(Obligatorio=$true)]
        [cadena]$Protocolo
    )
    $ServerPath = "HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\$Protocolo\Server"
    $ClientPath = "HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\$Protocol\Client"
    Nuevo elemento -Ruta $RutaServidor -Forzar
    Nuevo-elemento -Ruta $RutaCliente -Forzar
    Set-ItemProperty -Ruta $RutaServidor -Forzar -Nombre Enabled -Tipo "DWORD" -Valor 0
    Set-ItemProperty -Ruta $RutaServidor -Force -Nombre DeshabilitadoPorDefecto -Tipo "DWORD" -Valor 1
    Set-ItemProperty -Ruta $RutaCliente -Force -Nombre Activado -Tipo "DWORD" -Valor 0
    Set-ItemProperty -Ruta $RutaCliente -Force -Nombre DesactivadoPorDefecto -Tipo "DWORD" -Valor 1
}
# Desactivar SSL v2
Disable-Protocol -Protocolo "SSL 2.0"
# Desactivar SSL v3
Desactivar-Protocolo -Protocolo "SSL 3.0" # Desactivar TLS 1.0
# Desactivar TLS 1.0
Desactivar-Protocolo -Protocolo "TLS 1.0" # Desactivar DTLS 1.0
# Desactivar DTLS 1.0
Desactivar-Protocolo -Protocolo "DTLS 1.0" # Desactivar TLS 1.1
# Desactivar TLS 1.1
Disable-Protocol -Protocolo "TLS 1.1" # Desactivar TLS 1.1
# Desactivar DTLS 1.1
Disable-Protocol -Protocol "DTLS 1.1" # Desactivar DTLS 1.1

function Set-NETStrongAuthentication {
    param(
        [cadena]$RegistryPath,
        [cadena]$Nombre,
        [cadena]$Tipo,
        [int]$Valor
    )
    Set-ItemProperty -Ruta $RegistryPath -Force -Nombre $Nombre -Tipo $Tipo -Valor $Valor
}

$NETVersions = @("2.0.50727", "3.0", "4.0.30319")

foreach ($version en $NETVersions) {
    Set-NETStrongAuthentication -RegistryPath "HKLM:\SOFTWARE\Microsoft\.NETFramework\v$version" -Name SchUseStrongCrypto -Type "DWORD" -Value 0x00000001
    Set-NETStrongAuthentication -RegistryPath "HKLM:\SOFTWARE\Microsoft\.NETFramework\v$version" -Name SystemDefaultTlsVersions -Type "DWORD" -Value 0x00000001
    Set-NETStrongAuthentication -RegistryPath "HKLM:\SOFTWARE\WOW6432Node\Microsoft\.NETFramework\v$version" -Name SchUseStrongCrypto -Type "DWORD" -Value 0x00000001
    Set-NETStrongAuthentication -RegistryPath "HKLM:\SOFTWARE\WOW6432Node\Microsoft\.NETFramework\v$version" -Name SystemDefaultTlsVersions -Type "DWORD" -Value 0x00000001
}
```

 ## مقدمة:
 
 أصبحت أجهزة الكمبيوتر جانبًا حاسمًا في حياتنا اليومية ، ومع ذلك ، نمت الحاجة إلى أمان البيانات بشكل كبير. الطرق المختلفة لتأمين البيانات أثناء التحميل ، SSL (Secure Socket Layer) و TLS (بروتوكول أمان طبقة النقل) هما بروتوكولات تستخدم في نطاق واسع. الاتصالات الإلكترونية القديمة. هذه المقالة ، سنناقش خطوات تقوية أجهزة الكمبيوتر عن طريق تعطيل SSL وإصدارات TLS 1.2 وما يليها للحفاظ على أمان البيانات.
 
 ### لماذا تعطيل SSL و TLS 1.2 والإصدارات الأقدم؟
 
 الإصدارات الأقدم من SSL و TLS معرضة التهديدات من التهديدات الأمنية مثل POODLE (Padding Oracle Ongraded Legacy Encryption) و BEAST (متصفح استغلال ضد SSL / TLS) و Heartbleed. تلك الهجمات التي تؤدي إلى إطلاق النار على معلومات حساسة ، مما يجعل تشغيل استخدام البروتوكولات القديمة.
 
 ### تعطيل SSL و TLS 1.2 والإصدارات الأقدم في Windows:
 
 يمكن تعطيل عملية تعطيل SSL و TLS 1.2 والإصدارات الأقل من محرر التسجيل. إليك نص بوويرشيل لإنجاز المهمة:
 
 
 #### تعطيل SSL و TLS 1.2 والإصدارات الأقدم في Linux:
 
 في Linux ، يمكن تحقيق عملية تعطيل SSL و TLS 1.2 وما دونه من خلال تعديل ملف تكوين OpenSSL. فيما يلي الخطوات التي يجب اتباعها:
 
 1. افتح الجهاز وقم بتسجيل الدخول كجذر.
 2. انتقل إلى ملف تكوين OpenSSL. عادةً ما يكون موجودًا في /etc/ssl/openssl.cnf.
 3. افتح الملف باستخدام محرر نصوص مثل nano أو vim.
 4. حدد موقع توجيه SSLProtocol وقم بتعيين قيمته إلى -TLSv1.2.
 5. احفظ الملف وأغلق محرر النصوص.
 6. أعد تشغيل الخدمات التي تستخدم OpenSSL ، مثل Apache أو Nginx ، حتى تدخل التغييرات حيز التنفيذ.
 
 ## خاتمة:
 
 من خلال تعطيل SSL وجميع إصدارات TLS 1.2 وما دونها ، يمكنك تعزيز أمان الكمبيوتر وحماية المعلومات الحساسة من التهديدات السيبرانية المحتملة. إنها عملية بسيطة يمكن إنجازها بأقل جهد ، مما يجعلها جانبًا مهمًا للحفاظ على أمان جهاز الكمبيوتر الخاص بك. من خلال تنفيذ الخطوات الموضحة في هذه المقالة ، يمكنك الحفاظ على أمان بياناتك ومنع الهجمات الإلكترونية ، وبالتالي تقليل مخاطر الكشف عن المعلومات الحساسة.
 
 من المهم ملاحظة أنه في حين أن تعطيل هذه الإصدارات القديمة من بروتوكولات SSL و TLS يمكن أن يحسن أمان جهاز الكمبيوتر الخاص بك ، إلا أنه يمكن أن يؤثر أيضًا على التوافق مع بعض الأنظمة القديمة. لذلك ، من الضروري إجراء اختبار شامل للتغييرات التي تم إجراؤها والتأكد من عدم وجود آثار سلبية على نظامك قبل تنفيذها بالكامل.
 
 في الختام ، يعد تقوية جهاز الكمبيوتر الخاص بك عن طريق تعطيل SSL وجميع إصدارات TLS 1.2 وما بعدها خطوة مهمة في الحفاظ على أمان المعلومات الحساسة ومنع الهجمات الإلكترونية. توفر الخطوات الموضحة في هذه المقالة دليلًا مباشرًا لتأمين جهاز الكمبيوتر الخاص بك ، مما يسهل على الأفراد والمؤسسات تنفيذ الإجراءات الأمنية الضرورية.