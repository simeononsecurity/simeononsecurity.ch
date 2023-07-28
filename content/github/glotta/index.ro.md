---
title: "Script de automatizare a traducerii pentru fișierele Hugo Markdown - Glotta"
date: 2023-05-02
toc: true
draft: false
description: "Glotta este un instrument puternic de linie de comandă care automatizează traducerea fișierelor Hugo markdown în mai multe limbi, făcând localizarea o joacă de copii."
tags: ["automatizarea traducerilor", "Hugo markdown", "localizare", "conținut multilingv", "instrument de linie de comandă", "traducere lingvistică", "localizare lingvistică", "script de automatizare", "traducere de conținut", "site multilingv", "suport lingvistic", "fluxul de lucru pentru localizare", "procesul de traducere", "integrarea lingvistică", "Hugo generator de site-uri statice", "Glotta", "fișiere de limbă", "API de traducere", "furnizori de traduceri", "serviciu de traducere", "managementul limbilor", "SEO multilingv", "localizarea conținutului", "globalizarea site-ului web", "instrument de sprijin lingvistic", "fluxul de lucru lingvistic", "eficiența traducerii", "eficiența localizării", "traducere automată", "Suport multilingv Hugo"]
---


## Glotta

Script care traduce conținutul fișierului Hugo markdown în alte limbi.

#### Exemplu de comandă:

```sh
node src/index.js --source=__fixtures__ --recursive --force
# --source is the root dir to search for ".en.md" files. You may replace __fixtures__ with any other dir name.
# --recursive will include any nested directories in the root dir (default is false)
# --force will cause existing language files to be overwritten (default is to ignore existing language file)
# --targetLanguageIds is another option that can be specified (default target ids are: ar, bn, ca, zh, fr, de, hi, it, ja, pt, pa, ro, ru, es
```

#### Exemplu de ieșire:
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

## Cum să schimbați furnizorul API de traducere

Setați `TRANSLATE_PROVIDER` fie la variabila de mediu `GOOGLE` sau `DEEPL` și asigurați-vă că ați setat `DEEPL_AUTH_KEY` de asemenea.
Suitele de testare se vor baza pe aceste variabile de mediu, astfel încât puteți testa integrarea prin rularea `npm test`

De exemplu:
```sh
GOOGLE_APPLICATION_CREDENTIALS=./gcloud-keys/dev-service-account-keys.json
DEEPL_AUTH_KEY= **********
TRANSLATE_PROVIDER=DEEPL
```


## Autor:

[1nf053c](https://github.com/1nf053c)

## Proprietar:

[simeononsecurity](https://github.com/simeononsecurity)

## Licență

[MIT](https://github.com/simeononsecurity/glotta/blob/main/LICENSE)
