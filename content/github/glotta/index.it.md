---
title: "Script di automazione della traduzione per i file Markdown di Hugo - Glotta"
date: 2023-05-02
toc: true
draft: false
description: "Glotta è un potente strumento a riga di comando che automatizza la traduzione dei file markdown di Hugo in più lingue, rendendo la localizzazione un gioco da ragazzi."
tags: ["automazione della traduzione", "Hugo markdown", "localizzazione", "contenuti multilingue", "strumento a riga di comando", "traduzione linguistica", "localizzazione linguistica", "script di automazione", "traduzione di contenuti", "sito web multilingue", "supporto linguistico", "flusso di lavoro della localizzazione", "processo di traduzione", "integrazione linguistica", "Generatore di siti statici Hugo", "Glotta", "file di lingua", "traduzione API", "fornitori di traduzioni", "servizio di traduzione", "gestione della lingua", "SEO multilingue", "localizzazione dei contenuti", "globalizzazione del sito web", "strumento di supporto linguistico", "flusso di lavoro linguistico", "efficienza della traduzione", "efficienza di localizzazione", "traduzione automatica", "Hugo multilingual support"]
---


## Glotta

Script che traduce il contenuto del file markdown Hugo in altre lingue.

#### Esempio di comando:

```sh
node src/index.js --source=__fixtures__ --recursive --force
# --source is the root dir to search for ".en.md" files. You may replace __fixtures__ with any other dir name.
# --recursive will include any nested directories in the root dir (default is false)
# --force will cause existing language files to be overwritten (default is to ignore existing language file)
# --targetLanguageIds is another option that can be specified (default target ids are: ar, bn, ca, zh, fr, de, hi, it, ja, pt, pa, ro, ru, es
```

#### Esempio di uscita:
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

## Come cambiare il fornitore di API di traduzione

Impostare il `TRANSLATE_PROVIDER` a una variabile d'ambiente `GOOGLE` o `DEEPL` e assicuratevi di impostare il vostro `DEEPL_AUTH_KEY` anche.
Le suite di test si baseranno su queste variabili env, quindi è possibile testare l'integrazione eseguendo `npm test`

Ad esempio:
```sh
GOOGLE_APPLICATION_CREDENTIALS=./gcloud-keys/dev-service-account-keys.json
DEEPL_AUTH_KEY= **********
TRANSLATE_PROVIDER=DEEPL
```


## Autore:

[1nf053c](https://github.com/1nf053c)

## Proprietario:

[simeononsecurity](https://github.com/simeononsecurity)

## Licenza

[MIT](https://github.com/simeononsecurity/glotta/blob/main/LICENSE)
