---
title: "ChromiumADMX: Plantilla ADMX adecuada para el navegador Chromium"
date: 2020-07-25
---


Plantilla ADMX adecuada para el navegador Chromium

Chromium, como empresa, no ha publicado plantillas ADMX para el Navegador Chromium que puedan instalarse al mismo tiempo que las plantillas de Google Chrome.
Teniendo esto en cuenta, hemos modificado las plantillas ADMX de Google Chrome para que reflejen la ruta de registro del navegador Chromium y las hemos colocado en tandum en la carpeta ADMX de Google en GPO.

**Estas Definiciones de Política se encuentran en estado Pre-Alpha. Deben usarse sólo con fines de prueba**.

## Descargar los archivos necesarios

**Descargue los archivos necesarios de la página [GitHub Repository](https://github.com/simeononsecurity/ChromiumADMX)

## Notas

Definiciones de política de Google Chrome modificadas según:
[Chromium Policy Templates](https://www.chromium.org/administrators/policy-templates)

**Nota:** Se ha sustituido "HKEY_LOCAL_MACHINE\Software\Policies\Google\Chrome" por "HKEY_LOCAL_MACHINE\Software\Policies\Chromium\".

**Nota:** No instale las plantillas ADMX de SOS'es Chromium y Brave Browser al mismo tiempo.

## Cómo instalar

1.) Copie todos los archivos excepto readme.md en "C:\Windows\PolicyDefinitions" y/o "\\domain.tld\domain\Policies\PolicyDefinitions".

2.) ¿Ganancias?




