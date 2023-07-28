---
title: "Tome el control de las políticas del navegador Brave con BraveADMX - Plantillas ADMX modificadas"
date: 2020-07-25
---


Brave, como compañía, ha fallado en liberar plantillas ADMX para el sitio del navegador brave empujando registros puros como la única opción soportada.
Como el navegador Brave está basado en Chromium, debería soportar la mayoría, si no todas, las mismas políticas de las plantillas ADMX de Chromium y Google Chrome.
Con esto en mente, hemos modificado las plantillas ADMX de Google Chrome para reflejar la ruta del registro del Navegador Brave. Después de algunas pruebas iniciales, las plantillas parecen funcionar.

**Estas Definiciones de Política están en un estado Pre-Alpha. Deben usarse sólo con fines de prueba**.

## Descargue los archivos necesarios.

**Descargue los archivos necesarios de la página [GitHub Repository](https://github.com/simeononsecurity/BraveADMX)

## Notas

Definiciones de política de Google Chrome modificadas según:
[Brave Group Policy](https://support.brave.com/hc/en-us/articles/360039248271-Group-Policy)

**Nota:** Se ha sustituido "HKEY_LOCAL_MACHINE\Software\Policies\Google\Chrome" por "HKEY_LOCAL_MACHINE\Software\Policies\BraveSoftware\Brave".

**Nota:** No instale las plantillas ADMX de SOS'es Chromium y Brave Browser al mismo tiempo.

## Cómo instalar

1.) Copie todos los archivos excepto readme.md en "C:\Windows\PolicyDefinitions" y/o "\\domain.tld\domain\Policies\PolicyDefinitions".

2.) ¿Ganancias?