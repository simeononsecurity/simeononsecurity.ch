---
title: "ChromiumADMX : Modèle ADMX approprié pour le navigateur Chromium"
date: 2020-07-25
---


Modèle ADMX approprié pour le navigateur Chromium

La société Chromium n'a pas publié de modèles ADMX pour le navigateur Chromium qui peuvent être installés en même temps que les modèles Google Chrome.
C'est pourquoi nous avons modifié les modèles ADMX de Google Chrome afin de refléter le chemin d'accès au registre du navigateur Chromium et nous les avons placés dans le dossier ADMX de Google dans la GPO.

**Ces définitions de politiques sont à l'état de pré-alpha. Elles ne doivent être utilisées qu'à des fins de test**

## Télécharger les fichiers nécessaires

**Téléchargez les fichiers nécessaires à partir du site [GitHub Repository](https://github.com/simeononsecurity/ChromiumADMX)

## Notes

Définitions des règles de Google Chrome modifiées conformément à :
[Chromium Policy Templates](https://www.chromium.org/administrators/policy-templates)

**Note:** Remplacer "HKEY_LOCAL_MACHINE\Software\Policies\Google\Chrome" par "HKEY_LOCAL_MACHINE\Software\Policies\Chromium".

**Note:** N'installez pas les modèles ADMX de SOS's Chromium et Brave Browser en même temps.

## Comment installer

1.) Copier tous les fichiers sauf readme.md dans "C:\NWindows\NPolicyDefinitions" et/ou "\Ndomain.tld\Ndomain\NPolicies\NPolicyDefinitions".

2.) Profit ?




