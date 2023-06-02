---
title: "Script de automatización de la traducción para archivos Hugo Markdown - Glotta"
date: 2023-05-02
toc: true
draft: false
description: "Glotta es una potente herramienta de línea de comandos que automatiza la traducción de archivos markdown de Hugo a varios idiomas, haciendo que la localización sea pan comido."
tags: ["automatización de la traducción", "Reducción de Hugo", "localización", "multilingual content", "herramienta de línea de comandos", "traducción de idiomas", "localización lingüística", "script de automatización", "traducción de contenidos", "sitio web multilingüe", "apoyo lingüístico", "flujo de trabajo de localización", "proceso de traducción", "integración lingüística", "Generador de sitios estáticos Hugo", "Glotta", "archivos de idioma", "API de traducción", "proveedores de traducción", "servicio de traducción", "gestión lingüística", "SEO multilingüe", "localización de contenidos", "globalización de sitios web", "herramienta de apoyo lingüístico", "flujo de trabajo lingüístico", "eficacia de la traducción", "eficacia de la localización", "traducción automática", "Soporte multilingüe Hugo"]
---


## Glotta

Script que traduce el contenido de los archivos markdown de Hugo a otros idiomas.

#### Ejemplo de comando:

```sh
node src/index.js --source=__fixtures__ --recursive --force
# --source is the root dir to search for ".en.md" files. You may replace __fixtures__ with any other dir name.
# --recursive will include any nested directories in the root dir (default is false)
# --force will cause existing language files to be overwritten (default is to ignore existing language file)
# --targetLanguageIds is another option that can be specified (default target ids are: ar, bn, ca, zh, fr, de, hi, it, ja, pt, pa, ro, ru, es
```

#### Ejemplo de salida:
```txt
========== glotta ============
dir: __fixtures__/simeon-usecase-dir/content/articles/a-beginners-guide-to-setting-up-a-secure-and-resilient-vpn-for-remote-workers
Input file(s):  [
  '__fixtures__/simeon-usecase-dir/content/articles/a-beginners-guide-to-setting-up-a-secure-and-resilient-vpn-for-remote-workers/index.en.md'
]
targetLanguageIds: ar, bn, ca, zh, fr, de, hi, it, ja, pt, pa, ro, ru, es
force overwrite if file exists?: true
==============================

parsing input file...
translating text into...  es
writing new file...
translating text into...  ru
writing new file...
translating text into...  ro
writing new file...
translating text into...  pa
```

## Cómo cambiar el proveedor de la API de traducción

Establezca el `TRANSLATE_PROVIDER` a la variable de entorno `GOOGLE` o `DEEPL` y asegúrese de configurar su `DEEPL_AUTH_KEY` también.
Las suites de prueba se basarán en estas variables env para que pueda probar su integración mediante la ejecución de `npm test`

Por ejemplo:
```sh
GOOGLE_APPLICATION_CREDENTIALS=./gcloud-keys/dev-service-account-keys.json
DEEPL_AUTH_KEY= **********
TRANSLATE_PROVIDER=DEEPL
```


## Autor:

[1nf053c](https://github.com/1nf053c)

## Propietario:

[simeononsecurity](https://github.com/simeononsecurity)

## Licencia

[MIT](https://github.com/simeononsecurity/glotta/blob/main/LICENSE)
