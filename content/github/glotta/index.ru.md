---
title: "Скрипт автоматизации перевода для Markdown-файлов Hugo - Glotta"
date: 2023-05-02
toc: true
draft: false
description: "Glotta - это мощный инструмент командной строки, автоматизирующий перевод маркдаун-файлов Hugo на несколько языков, что значительно упрощает процесс локализации."
tags: ["автоматизация перевода", "Hugo markdown", "локализация", "многоязычный контент", "инструмент командной строки", "языковой перевод", "языковая локализация", "сценарий автоматизации", "перевод контента", "многоязычный сайт", "языковая поддержка", "рабочий процесс локализации", "процесс перевода", "языковая интеграция", "Генератор статических сайтов Hugo", "Glotta", "языковые файлы", "API перевода", "поставщики услуг перевода", "услуга перевода", "управление языком", "многоязычное SEO", "локализация контента", "глобализация веб-сайтов", "инструмент языковой поддержки", "языковой документооборот", "эффективность перевода", "эффективность локализации", "автоматизированный перевод", "Многоязычная поддержка Hugo"]
---


## Glotta

Скрипт, переводящий содержимое файла Hugo markdown на другие языки.

#### Пример команды:

```sh
node src/index.js --source=__fixtures__ --recursive --force
# --source is the root dir to search for ".en.md" files. You may replace __fixtures__ with any other dir name.
# --recursive will include any nested directories in the root dir (default is false)
# --force will cause existing language files to be overwritten (default is to ignore existing language file)
# --targetLanguageIds is another option that can be specified (default target ids are: ar, bn, ca, zh, fr, de, hi, it, ja, pt, pa, ro, ru, es
```

#### Пример вывода:
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

## Как изменить поставщика API переводов

Установите `TRANSLATE_PROVIDER` переменной окружения либо `GOOGLE` или `DEEPL` и не забудьте установить свой `DEEPL_AUTH_KEY` также.
Тестовые пакеты будут опираться на эти переменные env, поэтому вы можете протестировать свою интеграцию, запустив `npm test`

Например:
```sh
GOOGLE_APPLICATION_CREDENTIALS=./gcloud-keys/dev-service-account-keys.json
DEEPL_AUTH_KEY= **********
TRANSLATE_PROVIDER=DEEPL
```


## Автор:

[1nf053c](https://github.com/1nf053c)

## Владелец:

[simeononsecurity](https://github.com/simeononsecurity)

## Лицензия

[MIT](https://github.com/simeononsecurity/glotta/blob/main/LICENSE)
