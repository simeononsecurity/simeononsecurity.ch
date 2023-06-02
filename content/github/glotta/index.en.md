---
title: "Translation Automation Script for Hugo Markdown Files - Glotta"
date: 2023-05-02
toc: true
draft: false
description: "Glotta is a powerful command-line tool that automates the translation of Hugo markdown files into multiple languages, making localization a breeze."
tags: ["translation automation", "Hugo markdown", "localization", "multilingual content", "command-line tool", "language translation", "language localization", "automation script", "content translation", "multilingual website", "language support", "localization workflow", "translation process", "language integration", "Hugo static site generator", "Glotta", "language files", "translation API", "translation providers", "translation service", "language management", "multilingual SEO", "content localization", "website globalization", "language support tool", "language workflow", "translation efficiency", "localization efficiency", "automated translation", "Hugo multilingual support"]
---


## Glotta

Script that translates Hugo markdown file content into other languages.

#### Example command:

```sh
node src/index.js --source=__fixtures__ --recursive --force
# --source is the root dir to search for ".en.md" files. You may replace __fixtures__ with any other dir name.
# --recursive will include any nested directories in the root dir (default is false)
# --force will cause existing language files to be overwritten (default is to ignore existing language file)
# --targetLanguageIds is another option that can be specified (default target ids are: ar, bn, ca, zh, fr, de, hi, it, ja, pt, pa, ro, ru, es
```

#### Example output:
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

## How to change Translation API Provider

Set the `TRANSLATE_PROVIDER` environment variable to either `GOOGLE` or `DEEPL`, and be sure to set your `DEEPL_AUTH_KEY` as well.
The test suites will rely on these env variables so you can test your integration by running `npm test`

For example:
```sh
GOOGLE_APPLICATION_CREDENTIALS=./gcloud-keys/dev-service-account-keys.json
DEEPL_AUTH_KEY= **********
TRANSLATE_PROVIDER=DEEPL
```


## Author:

[1nf053c](https://github.com/1nf053c)

## Owner:

[simeononsecurity](https://github.com/simeononsecurity)

## License

[MIT](https://github.com/simeononsecurity/glotta/blob/main/LICENSE)
