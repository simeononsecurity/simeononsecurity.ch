---
title: "Script d'automatisation de la traduction pour les fichiers Hugo Markdown - Glotta"
date: 2023-05-02
toc: true
draft: false
description: "Glotta est un puissant outil en ligne de commande qui automatise la traduction des fichiers markdown d'Hugo en plusieurs langues, ce qui facilite la localisation."
tags: ["automatisation de la traduction", "Hugo markdown", "localisation", "contenu multilingue", "outil en ligne de commande", "traduction linguistique", "localisation des langues", "automation script", "traduction du contenu", "site web multilingue", "Soutien linguistique", "flux de travail pour la localisation", "processus de traduction", "l'intégration linguistique", "Générateur de site statique Hugo", "Glotta", "fichiers de langues", "API de traduction", "les prestataires de services de traduction", "service de traduction", "gestion des langues", "SEO multilingue", "localisation du contenu", "mondialisation du site web", "outil d'aide linguistique", "flux linguistique", "efficacité de la traduction", "efficacité de la localisation", "traduction automatique", "Soutien multilingue d'Hugo"]
---


## Glotta

Script qui traduit le contenu du fichier Hugo markdown dans d'autres langues.

#### Exemple de commande :

```sh
node src/index.js --source=__fixtures__ --recursive --force
# --source is the root dir to search for ".en.md" files. You may replace __fixtures__ with any other dir name.
# --recursive will include any nested directories in the root dir (default is false)
# --force will cause existing language files to be overwritten (default is to ignore existing language file)
# --targetLanguageIds is another option that can be specified (default target ids are: ar, bn, ca, zh, fr, de, hi, it, ja, pt, pa, ro, ru, es
```

#### Exemple de sortie :
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

## Comment changer de fournisseur d'API de traduction

Définir le `TRANSLATE_PROVIDER` à l'une ou l'autre des variables d'environnement suivantes `GOOGLE` ou `DEEPL` et veillez à définir votre `DEEPL_AUTH_KEY` également.
Les suites de tests s'appuieront sur ces variables env. Vous pouvez donc tester votre intégration en lançant `npm test`

Par exemple :
```sh
GOOGLE_APPLICATION_CREDENTIALS=./gcloud-keys/dev-service-account-keys.json
DEEPL_AUTH_KEY= **********
TRANSLATE_PROVIDER=DEEPL
```


## Auteur :

[1nf053c](https://github.com/1nf053c)

## Propriétaire :

[simeononsecurity](https://github.com/simeononsecurity)

## Licence

[MIT](https://github.com/simeononsecurity/glotta/blob/main/LICENSE)
