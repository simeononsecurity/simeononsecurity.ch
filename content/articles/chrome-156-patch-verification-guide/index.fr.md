---
title: "Mise à jour de sécurité de Chrome 156 : vérifier le correctif d’octobre"
date: 2026-10-28
lastmod: 2026-11-09
toc: true
draft: false
description: "Vérifiez la version de sécurité de Chrome 156 du 27 octobre sur Windows, macOS, Linux et Android. Comparez la version installée, terminez un redémarrage en attente et contrôlez séparément les appareils gérés."
genre: ["Navigateurs", "Sécurité", "Gestion des correctifs"]
tags: ["Chrome 156", "mise à jour de sécurité Chrome", "vérification du correctif Chrome", "vérification de la version Chrome", "Chrome 156 pour Windows", "Chrome 156 pour macOS", "Chrome 156 pour Linux", "Chrome 156 pour Android", "CVE-2026-118306", "CVE-2026-118331", "CVE-2026-118348", "CVE-2026-118344", "correctifs de navigateur", "Chrome Enterprise Core", "navigateurs gérés", "sécurité Chromium", "mises à jour de navigateur", "redémarrage de Chrome", "chrome://version", "chrome://settings/help", "mise à jour de Chrome sur Android", "mises à jour de sécurité Brave", "mises à jour de sécurité Edge"]
cover: "/img/cover/cybersecurity-padlock-shield.webp"
coverAlt: "Illustration d’un cadenas et d’un bouclier représentant une mise à jour de sécurité, et non un écran de version Chrome"
coverCaption: ""
---

**La version de sécurité de Chrome publiée le 27 octobre 2026** comprend 52 correctifs. Pour vérifier votre installation, comparez son numéro de version complet à celui de la version publiée pour votre système d’exploitation, puis redémarrez Chrome afin de terminer toute mise à jour en attente. L’annonce d’une version ne prouve pas que votre appareil a reçu la mise à jour. ([Version Chrome pour ordinateur](https://chromereleases.googleblog.com/2026/10/stable-channel-update-for-desktop_0562499947.html))

<!--more-->

## Quelle version devez-vous voir ?

Google a publié les versions Stable suivantes le 27 octobre 2026. L’annonce pour ordinateur donne des numéros de build distincts pour Windows et macOS, ainsi que pour Linux. L’[annonce Android](https://chromereleases.googleblog.com/2026/10/chrome-for-android-update_0160078013.html) indique son propre build et précise que les versions Android contiennent les mêmes correctifs de sécurité que les versions correspondantes pour ordinateur, « sauf indication contraire ».

| Plateforme | Build de l’annonce Google du 27 octobre |
|---|---|
| **Windows** | 156.0.8078.73 ou 156.0.8078.74 |
| **macOS** | 156.0.8078.73 ou 156.0.8078.74 |
| **Linux** | 156.0.8078.73 |
| **Android** | 156.0.8078.73 |

*Utilisez ce tableau pour la version du 27 octobre, et non comme numéro cible permanent. Consultez le [flux actuel des versions Chrome](https://chromereleases.googleblog.com/) pour les prochaines mises à jour de sécurité.* Google a indiqué que le déploiement sur ordinateur prendrait « les prochains jours ou semaines » et que le build Android arriverait sur Google Play dans les prochains jours. Un appareil dont la version est inférieure à celle du tableau doit toujours être vérifié, même pendant un déploiement progressif. ([Annonce pour ordinateur](https://chromereleases.googleblog.com/2026/10/stable-channel-update-for-desktop_0562499947.html), [annonce Android](https://chromereleases.googleblog.com/2026/10/chrome-for-android-update_0160078013.html))

La [liste des correctifs de sécurité pour ordinateur](https://chromereleases.googleblog.com/2026/10/stable-channel-update-for-desktop_0562499947.html) classe quatre vulnérabilités signalées comme **Critical** : corruption mémoire dans FileSystem [CVE-2026-118306](https://nvd.nist.gov/vuln/detail/CVE-2026-118306), validation incorrecte des entrées dans FileAPI CVE-2026-118331, validation incorrecte des entrées dans Skia CVE-2026-118348 et use-after-free dans Layout CVE-2026-118344. La même annonce recense d’autres CVE classées **High** et **Medium**. Le chiffre 52 désigne les correctifs de sécurité inclus dans la version, et non 52 rapports d’exploitation confirmés de manière indépendante. ([Fiche NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-118306))

**L’annonce ne prétend pas que les vulnérabilités répertoriées font l’objet d’une exploitation active.** L’avertissement porte sur le calendrier de divulgation : « L’accès aux détails des bugs et aux liens peut rester restreint jusqu’à ce que la majorité des utilisateurs ait reçu un correctif. » Ne considérez pas la restriction d’accès aux détails comme une preuve d’exploitation. ([Annonce pour ordinateur](https://chromereleases.googleblog.com/2026/10/stable-channel-update-for-desktop_0562499947.html))

## Vérifier et terminer la mise à jour sur ordinateur

1. Ouvrez **`chrome://version`** dans l’installation de Chrome que vous utilisez. Notez la version complète et le système d’exploitation, pas seulement le numéro majeur 156. Vérifiez séparément une fenêtre Chrome d’un autre canal ou une installation située ailleurs.
2. Ouvrez **`chrome://settings/help`**, ou sélectionnez **Plus > Aide > À propos de Google Chrome**. Google indique que Chrome recherche les mises à jour sur cette page. Attendez la fin de la vérification. ([Instructions Google de mise à jour sur ordinateur](https://support.google.com/chrome/answer/95414?co=GENIE.Platform%3DDesktop&hl=en))
3. Sélectionnez **Relancer** si la page le propose. Enregistrez votre travail en cours au préalable. Fermez les autres fenêtres Chrome, rouvrez le navigateur, puis vérifiez de nouveau **`chrome://version`**. Comparez au tableau la version affichée après le redémarrage.
4. Si la version reste inférieure au build annoncé, recherchez de nouveau une mise à jour. Si une organisation gère le navigateur ou si le programme de mise à jour signale une erreur, contactez l’administrateur. Un téléchargement réussi ne prouve pas que le navigateur en cours d’exécution a changé de version.

> **Résultat attendu :** Après le redémarrage, le build Stable de Chrome en cours d’exécution correspond à la version indiquée pour la plateforme dans l’annonce du 27 octobre, ou à une version ultérieure annoncée par le fournisseur. Un bouton Relancer en attente ne prouve pas que la mise à jour est terminée.

Sur **Android**, ouvrez Play Store > icône du profil > Gérer les applications et l’appareil, puis mettez Chrome à jour dans la section des mises à jour disponibles si l’option apparaît. Dans Chrome, ouvrez Plus > Paramètres > À propos de Chrome pour afficher la version installée. Comparez-la à la ligne Android après la mise à jour de l’application. Ces chemins de menu suivent les [instructions Google pour Android](https://support.google.com/chrome/answer/95414?co=GENIE.Platform%3DAndroid&hl=en).

## Vérifier un parc géré

Pour les navigateurs inscrits, utilisez le **rapport sur les versions de Chrome** de la console d’administration Google pour repérer les anciens builds par système d’exploitation. Ouvrez la vue Browser Versions, sélectionnez l’unité organisationnelle concernée, examinez le numéro complet de version mineure et exportez le CSV si vous avez besoin d’une liste d’appareils à traiter. Selon Google, le rapport inclut les navigateurs ayant transmis des rapports au cours des 28 derniers jours. Google signale des retards possibles, surtout pour les grands parcs. ([Consulter les détails de version de Chrome](https://support.google.com/chrome/a/answer/10025748?hl=en))

**Distinguez l’inventaire déclaré de la vérification en direct.** Examinez l’heure du dernier rapport et le canal de chaque appareil, puis confirmez les cas atypiques directement dans le navigateur ou via l’inventaire des terminaux gérés. Google comptabilise séparément les installations distinctes de Chrome, telles que Stable et Beta. Le reporting de navigateur exige l’inscription et l’activation du [reporting des navigateurs gérés](https://support.google.com/chrome/a/answer/9301421?hl=en). L’absence d’une machine dans un rapport ne prouve pas qu’elle dispose du correctif.

## Vérifier séparément les navigateurs dérivés de Chromium

**Le tableau des versions de Chrome concerne Google Chrome.** Microsoft Edge, Brave et les autres navigateurs basés sur Chromium ont leurs propres paquets, numéros de version et calendriers de mise à jour. L’annonce Chrome ne confirme pas leur état de correctif. Vérifiez la version installée de chaque navigateur ainsi que son propre avis de sécurité ou ses notes de version pour les correctifs Chromium concernés. Ne comparez pas directement une version d’Edge ou de Brave au numéro 156.0.8078.73 de Chrome pour conclure qu’elle est corrigée.

Pour chaque navigateur dérivé, notez le nom du produit, le canal, le build installé, l’URL de l’avis du fournisseur et le build que celui-ci indique comme corrigé. Si le fournisseur n’a pas confirmé le correctif, indiquez le statut **non vérifié** et suivez ses consignes de mise à jour. Consignez séparément les résultats de Chrome et des navigateurs dérivés.

## Sources et références

- [Chrome Releases : mise à jour Stable Channel pour ordinateur, 27 octobre 2026](https://chromereleases.googleblog.com/2026/10/stable-channel-update-for-desktop_0562499947.html). Builds pour ordinateur, 52 correctifs, CVE et formulation du fournisseur sur la divulgation.
- [Chrome Releases : mise à jour de Chrome pour Android, 27 octobre 2026](https://chromereleases.googleblog.com/2026/10/chrome-for-android-update_0160078013.html). Build Android et réserve sur les correctifs correspondants pour ordinateur.
- [Suivi des problèmes Chromium : recherche des correctifs de sécurité M156](https://issues.chromium.org/issues?q=customfield1223088:1-M156). Lien de l’annonce pour ordinateur. L’accès aux détails individuels dépend des restrictions de divulgation.
- [NVD : CVE-2026-118306](https://nvd.nist.gov/vuln/detail/CVE-2026-118306) et [CVE-2026-118331](https://nvd.nist.gov/vuln/detail/CVE-2026-118331). Descriptions des vulnérabilités et versions Chrome concernées. Les niveaux de gravité ci-dessus suivent l’annonce de Google, pas une évaluation CVSS de la NVD.
- [Aide Google Chrome : mettre à jour Chrome sur ordinateur](https://support.google.com/chrome/answer/95414?co=GENIE.Platform%3DDesktop&hl=en) et [sur Android](https://support.google.com/chrome/answer/95414?co=GENIE.Platform%3DAndroid&hl=en). Vérification des mises à jour et chemins de menu pour la version.
- [Aide Chrome Enterprise : consulter les détails de version de Chrome](https://support.google.com/chrome/a/answer/10025748?hl=en) et [activer le reporting des navigateurs gérés](https://support.google.com/chrome/a/answer/9301421?hl=en). Prérequis et limites du reporting de parc.
