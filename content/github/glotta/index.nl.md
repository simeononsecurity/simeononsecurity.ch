---
title: "Vertaalautomatiseringsscript voor Hugo Markdown-bestanden - Glotta"
date: 2023-05-02
toc: true
draft: false
description: "Glotta is een krachtig opdrachtregelprogramma dat de vertaling van Hugo markdown-bestanden naar meerdere talen automatiseert, waardoor lokalisatie een fluitje van een cent wordt."
tags: ["vertaalautomatisering", "Hugo markdown", "lokalisatie", "meertalige inhoud", "commandoregelhulpmiddel", "taalvertaling", "taallokalisatie", "automatiseringsscript", "inhoudelijke vertaling", "veeltalige website", "taalondersteuning", "lokalisatieworkflow", "vertaalproces", "taalintegratie", "Hugo statische site generator", "Glotta", "taalbestanden", "vertaal-API", "aanbieders van vertalingen", "vertaaldienst", "taalbeheer", "meertalige SEO", "lokalisatie van inhoud", "website globalisering", "hulpmiddel voor taalondersteuning", "taal workflow", "vertaalefficiëntie", "lokalisatie efficiëntie", "geautomatiseerde vertaling", "Hugo meertalige ondersteuning"]
---


## Glotta

Script dat de inhoud van Hugo markdown-bestanden in andere talen vertaalt.

#### Voorbeeld commando:

```sh
node src/index.js --source=__fixtures__ --recursive --force
# --source is the root dir to search for ".en.md" files. You may replace __fixtures__ with any other dir name.
# --recursive will include any nested directories in the root dir (default is false)
# --force will cause existing language files to be overwritten (default is to ignore existing language file)
# --targetLanguageIds is another option that can be specified (default target ids are: ar, bn, ca, zh, fr, de, hi, it, ja, pt, pa, ro, ru, es
```

#### Voorbeelduitvoer:
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

## Hoe Vertaal API Provider te veranderen

Stel de `TRANSLATE_PROVIDER` omgevingsvariabele naar ofwel `GOOGLE` of `DEEPL` en zorg ervoor dat u uw `DEEPL_AUTH_KEY` ook.
De testsuites vertrouwen op deze env-variabelen, zodat u uw integratie kunt testen door het volgende uit te voeren `npm test`

Bijvoorbeeld:
```sh
GOOGLE_APPLICATION_CREDENTIALS=./gcloud-keys/dev-service-account-keys.json
DEEPL_AUTH_KEY= **********
TRANSLATE_PROVIDER=DEEPL
```


## Auteur:

[1nf053c](https://github.com/1nf053c)

## Eigenaar:

[simeononsecurity](https://github.com/simeononsecurity)

## License

[MIT](https://github.com/simeononsecurity/glotta/blob/main/LICENSE)
