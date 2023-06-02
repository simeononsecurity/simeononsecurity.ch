---
title: "Skript zur Übersetzungsautomatisierung für Hugo Markdown-Dateien - Glotta"
date: 2023-05-02
toc: true
draft: false
description: "Glotta ist ein leistungsstarkes Kommandozeilen-Tool, das die Übersetzung von Hugo-Markdown-Dateien in mehrere Sprachen automatisiert und die Lokalisierung zum Kinderspiel macht."
tags: ["Übersetzungsautomatisierung", "Hugo Abschlag", "Lokalisierung", "mehrsprachige Inhalte", "Kommandozeilentool", "Sprachübersetzung", "Sprachlokalisierung", "Automatisierungsskript", "Inhaltsübersetzung", "mehrsprachige Website", "Sprachunterstützung", "Lokalisierungs-Workflow", "Übersetzungsprozess", "sprachliche Integration", "Hugo Generator für statische Websites", "Glotta", "Sprachdateien", "Übersetzungs-API", "Übersetzungsdienstleister", "Übersetzungsdienst", "Sprachverwaltung", "mehrsprachiges SEO", "Lokalisierung von Inhalten", "Website-Globalisierung", "Sprachunterstützungstool", "Sprach-Workflow", "Übersetzungseffizienz", "Lokalisierungseffizienz", "automatisierte Übersetzung", "Hugo mehrsprachige Unterstützung"]
---


## Glotta

Skript, das den Inhalt von Hugo-Markdown-Dateien in andere Sprachen übersetzt.

#### Beispielbefehl:

```sh
node src/index.js --source=__fixtures__ --recursive --force
# --source is the root dir to search for ".en.md" files. You may replace __fixtures__ with any other dir name.
# --recursive will include any nested directories in the root dir (default is false)
# --force will cause existing language files to be overwritten (default is to ignore existing language file)
# --targetLanguageIds is another option that can be specified (default target ids are: ar, bn, ca, zh, fr, de, hi, it, ja, pt, pa, ro, ru, es
```

#### Beispielhafte Ausgabe:
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

## So ändern Sie den Übersetzungs-API-Anbieter

Setzen Sie die `TRANSLATE_PROVIDER` Umgebungsvariable entweder auf `GOOGLE` oder `DEEPL` und stellen Sie sicher, dass Sie Ihre `DEEPL_AUTH_KEY` auch.
Die Testsuiten werden sich auf diese Umgebungsvariablen stützen, so dass Sie Ihre Integration testen können, indem Sie `npm test`

Zum Beispiel:
```sh
GOOGLE_APPLICATION_CREDENTIALS=./gcloud-keys/dev-service-account-keys.json
DEEPL_AUTH_KEY= **********
TRANSLATE_PROVIDER=DEEPL
```


## Autor:

[1nf053c](https://github.com/1nf053c)

## Eigentümer:

[simeononsecurity](https://github.com/simeononsecurity)

## Lizenz

[MIT](https://github.com/simeononsecurity/glotta/blob/main/LICENSE)
