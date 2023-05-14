---
title: "Proteger Windows de los ataques de canal lateral de ejecución especulativa"
date: 2020-06-18
toc: true
draft: false
description: "Aprenda a proteger su sistema Windows contra los ataques de canal lateral de ejecución especulativa con el script de mitigación de Microsoft y las actualizaciones de firmware."
tags: ["Script de mitigación de Windows Spectre Meltdown", "Ataques de canal lateral de ejecución especulativa", "Microsoft", "Intel", "AMD", "VIA", "ARM", "Android", "Cromo", "iOS", "macOS", "Rama Inyección de destino", "Bypass de comprobación de límites", "Carga de la caché de datos", "Bypass de almacenamiento especulativo", "Muestreo de datos microarquitectónicos", "CVEs", "Actualizaciones de firmware", "Repositorio GitHub", "PowerShell"]
---
 https://support.microsoft.com/en-us/help/4073119/protect-against-speculative-execution-side-channel-vulnerabilities-in
**Script sencillo para implementar protecciones contra vulnerabilidades de canal lateral de ejecución especulativa en sistemas Windows.

Microsoft es consciente de una nueva clase de vulnerabilidades divulgadas públicamente que se denominan "ataques de canal lateral de ejecución especulativa" y que afectan a muchos procesadores modernos, incluidos Intel, AMD, VIA y ARM.

**Nota:** Este problema también afecta a otros sistemas operativos, como Android, Chrome, iOS y macOS. Por lo tanto, aconsejamos a los clientes que busquen orientación de esos proveedores.

Hemos publicado varias actualizaciones para ayudar a mitigar estas vulnerabilidades. También hemos tomado medidas para proteger nuestros servicios en la nube. Consulte las siguientes secciones para obtener más detalles.

Todavía no hemos recibido ninguna información que indique que estas vulnerabilidades se hayan utilizado para atacar a clientes. Estamos trabajando estrechamente con socios de la industria, incluidos fabricantes de chips, fabricantes de equipos originales de hardware y proveedores de aplicaciones, para proteger a los clientes. Para obtener todas las protecciones disponibles, es necesario actualizar el firmware (microcódigo) y el software. Esto incluye el microcódigo de los OEM de los dispositivos y, en algunos casos, actualizaciones del software antivirus.

**Este artículo aborda las siguientes vulnerabilidades:**
- CVE-2017-5715 - "Rama de inyección de destino" (Branch Target Injection)
- CVE-2017-5753 - "Elusión de comprobación de límites"
- CVE-2017-5754 - "Carga de caché de datos fraudulenta"
- CVE-2018-3639 - "Anulación de almacenamiento especulativo"
- CVE-2018-11091 - "Memoria no almacenable en caché de muestreo de datos microarquitectónicos (MDSUM)"
- CVE-2018-12126 - "Muestreo de datos del búfer de almacenamiento microarquitectónico (MSBDS)"
- CVE-2018-12127 - "Muestreo de datos de búfer de relleno microarquitectónico (MFBDS)"
- CVE-2018-12130 - "Muestreo de datos de puerto de carga microarquitectónica (MLPDS)"

**ACTUALIZADO EL 6 DE AGOSTO DE 2019** El 6 de agosto de 2019 Intel publicó detalles sobre una vulnerabilidad de divulgación de información del kernel de Windows. Esta vulnerabilidad es una variante de la vulnerabilidad de canal lateral de ejecución especulativa Spectre Variant 1 y se le ha asignado CVE-2019-1125.

**ACTUALIZADO EL 12 DE NOVIEMBRE DE 2019** El 12 de noviembre de 2019, Intel publicó un aviso técnico en torno a la vulnerabilidad Intel® Transactional Synchronization Extensions (Intel® TSX) Transaction Asynchronous Abort a la que se ha asignado CVE-2019-11135. Microsoft ha publicado actualizaciones para ayudar a mitigar esta vulnerabilidad y las protecciones del sistema operativo están habilitadas de forma predeterminada para las ediciones del sistema operativo cliente de Windows.

## Acciones recomendadas
Los clientes deben tomar las siguientes medidas para ayudar a protegerse contra las vulnerabilidades:

- Aplique todas las actualizaciones disponibles del sistema operativo Windows, incluidas las actualizaciones mensuales de seguridad de Windows.
- Aplique la actualización de firmware (microcódigo) correspondiente proporcionada por el fabricante del dispositivo.
- Evalúe el riesgo para su entorno basándose en la información proporcionada en los avisos de seguridad de Microsoft: ADV180002, ADV180012, ADV190013 y la información proporcionada en este artículo de la Base de conocimientos.
- Tome las medidas necesarias utilizando los avisos y la información sobre claves de registro que se proporcionan en este artículo de la Base de conocimientos.

## Descargue los archivos necesarios:

Descargue los archivos necesarios del[GitHub Repository](https://github.com/simeononsecurity/Windows-Spectre-Meltdown-Mitigation-Script)

## Cómo ejecutar el script:

**El script puede ser descargado desde GitHub de la siguiente manera:**
```
.\sos-spectre-meltdown-mitigations.ps1
```
