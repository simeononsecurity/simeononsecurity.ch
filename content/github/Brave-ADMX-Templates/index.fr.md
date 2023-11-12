---
title: "Prenez le contrôle des politiques de navigation de Brave avec BraveADMX - Modèles ADMX modifiés"
date: 2020-07-25
---


Brave, en tant que société, n'a pas publié de modèles ADMX pour le navigateur Brave, poussant les registres purs comme seule option supportée.
Comme le navigateur Brave est construit à partir de Chromium, il devrait supporter la plupart, si ce n'est toutes, les mêmes politiques des modèles ADMX de Chromium et de Google Chrome.
C'est pourquoi nous avons modifié les modèles ADMX de Google Chrome pour qu'ils reflètent le chemin d'accès au registre de Brave Browser. Après quelques recherches et tests initiaux, les modèles semblent fonctionner.

**Ces définitions de politiques sont dans un état pré-alpha. Elles ne doivent être utilisées qu'à des fins de test**

## Télécharger les fichiers nécessaires.

**Téléchargez les fichiers nécessaires à partir du site [GitHub Repository](https://github.com/simeononsecurity/BraveADMX)

## Notes

Définitions des règles de Google Chrome modifiées conformément à :
[Brave Group Policy](https://support.brave.com/hc/en-us/articles/360039248271-Group-Policy)

> **Note:** Remplacer "HKEY_LOCAL_MACHINE\Software\Policies\Google\Chrome" par "HKEY_LOCAL_MACHINE\Software\Policies\Brave\Brave".

> **Note:** N'installez pas les modèles ADMX de SOS's Chromium et Brave Browser en même temps.

## Comment installer

1.) Copier tous les fichiers sauf readme.md dans "C:\NWindows\NPolicyDefinitions" et/ou "\Ndomain.tld\Ndomain\NPolicies\NPolicyDefinitions".

2.) Profit ?