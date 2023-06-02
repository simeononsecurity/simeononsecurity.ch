---
title: "Skrypt automatyzacji tłumaczeń dla plików Hugo Markdown - Glotta"
date: 2023-05-02
toc: true
draft: false
description: "Glotta to potężne narzędzie wiersza poleceń, które automatyzuje tłumaczenie plików Hugo markdown na wiele języków, dzięki czemu lokalizacja staje się dziecinnie prosta."
tags: ["automatyzacja tłumaczeń", "Hugo markdown", "lokalizacja", "Wielojęzyczna zawartość", "narzędzie wiersza poleceń", "tłumaczenie językowe", "lokalizacja językowa", "skrypt automatyzacji", "tłumaczenie treści", "Wielojęzyczna strona internetowa", "wsparcie językowe", "przepływ pracy lokalizacji", "proces tłumaczenia", "integracja językowa", "Generator stron statycznych Hugo", "Glotta", "pliki językowe", "API tłumaczenia", "dostawcy usług tłumaczeniowych", "usługi tłumaczeniowe", "zarządzanie językiem", "wielojęzyczne SEO", "lokalizacja treści", "globalizacja strony internetowej", "narzędzie wsparcia językowego", "przepływ pracy językowej", "wydajność tłumaczenia", "skuteczność lokalizacji", "automatyczne tłumaczenie", "Wielojęzyczne wsparcie Hugo"]
---


## Glotta

Skrypt tłumaczący zawartość pliku Hugo markdown na inne języki.

#### Przykładowe polecenie:

```sh
node src/index.js --source=__fixtures__ --recursive --force
# --source is the root dir to search for ".en.md" files. You may replace __fixtures__ with any other dir name.
# --recursive will include any nested directories in the root dir (default is false)
# --force will cause existing language files to be overwritten (default is to ignore existing language file)
# --targetLanguageIds is another option that can be specified (default target ids are: ar, bn, ca, zh, fr, de, hi, it, ja, pt, pa, ro, ru, es
```

#### Przykładowe dane wyjściowe:
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

## Jak zmienić dostawcę Translation API

Ustawić `TRANSLATE_PROVIDER` zmienną środowiskową na `GOOGLE` lub `DEEPL` i pamiętaj, aby ustawić `DEEPL_AUTH_KEY` również.
Zestawy testowe będą polegać na tych zmiennych env, więc możesz przetestować swoją integrację, uruchamiając `npm test`

Na przykład:
```sh
GOOGLE_APPLICATION_CREDENTIALS=./gcloud-keys/dev-service-account-keys.json
DEEPL_AUTH_KEY= **********
TRANSLATE_PROVIDER=DEEPL
```


## Autor:

[1nf053c](https://github.com/1nf053c)

## Właściciel:

[simeononsecurity](https://github.com/simeononsecurity)

## Licencja

[MIT](https://github.com/simeononsecurity/glotta/blob/main/LICENSE)
