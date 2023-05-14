---
title: "Protéger Windows contre les attaques par canal latéral de l'exécution spéculative"
date: 2020-06-18
toc: true
draft: false
description: "Apprenez à protéger votre système Windows contre les attaques par canal latéral de l'exécution spéculative grâce au script d'atténuation et aux mises à jour du micrologiciel de Microsoft."
tags: ["Script d'atténuation des effets de Spectre et de Meltdown sur Windows", "Attaques par canal latéral de l'exécution spéculative", "Microsoft", "Intel", "AMD", "VIA", "ARM", "Android", "Chrome", "iOS", "macOS", "Injection de la cible de la branche", "Contrôle des limites Contournement", "Rogue Data Cache Load", "Contournement des magasins spéculatifs", "Échantillonnage des données microarchitecturales", "CVE", "Mises à jour des microprogrammes", "Dépôt GitHub", "PowerShell"]
---
 https://support.microsoft.com/en-us/help/4073119/protect-against-speculative-execution-side-channel-vulnerabilities-in
**Script simple pour implémenter des protections contre les vulnérabilités de canal latéral d'exécution spéculative dans les systèmes Windows.

Microsoft a connaissance d'une nouvelle catégorie de vulnérabilités divulguées publiquement, appelées "attaques par canal latéral d'exécution spéculative", qui affectent de nombreux processeurs modernes, notamment Intel, AMD, VIA et ARM.

**Ce problème affecte également d'autres systèmes d'exploitation, tels qu'Android, Chrome, iOS et macOS. Par conséquent, nous conseillons aux clients de se renseigner auprès de ces fournisseurs.

Nous avons publié plusieurs mises à jour pour atténuer ces vulnérabilités. Nous avons également pris des mesures pour sécuriser nos services en nuage. Voir les sections suivantes pour plus de détails.

Nous n'avons pas encore reçu d'informations indiquant que ces vulnérabilités ont été utilisées pour attaquer des clients. Nous travaillons en étroite collaboration avec nos partenaires industriels, notamment les fabricants de puces, les équipementiers et les fournisseurs d'applications, afin de protéger nos clients. Pour bénéficier de toutes les protections disponibles, des mises à jour des microcodes et des logiciels sont nécessaires. Il s'agit notamment du microcode des équipementiers et, dans certains cas, des mises à jour des logiciels antivirus.

**Cet article traite des vulnérabilités suivantes:**.
- CVE-2017-5715 - "Injection de cible de branche"
- CVE-2017-5753 - "Contournement du contrôle des limites"
- CVE-2017-5754 - "Chargement d'un cache de données illicite".
- CVE-2018-3639 - "Contournement du magasin spéculatif"
- CVE-2018-11091 - "Microarchitectural Data Sampling Uncacheable Memory (MDSUM)"
- CVE-2018-12126 - "Microarchitectural Store Buffer Data Sampling (MSBDS)"
- CVE-2018-12127 - "Microarchitectural Fill Buffer Data Sampling (MFBDS)"
- CVE-2018-12130 - "Échantillonnage des données du port de chargement microarchitectural (MLPDS)"

**MIS À JOUR LE 6 AOÛT 2019** Le 6 août 2019, Intel a publié des détails sur une vulnérabilité de divulgation d'informations du noyau Windows. Cette vulnérabilité est une variante de la vulnérabilité de canal latéral d'exécution spéculative Spectre Variant 1 et a été assignée CVE-2019-1125.

**MIS À JOUR LE 12 NOVEMBRE 2019** Le 12 novembre 2019, Intel a publié un avis technique autour de la vulnérabilité Intel® Transactional Synchronization Extensions (Intel® TSX) Transaction Asynchronous Abort qui est assignée CVE-2019-11135. Microsoft a publié des mises à jour pour aider à atténuer cette vulnérabilité et les protections du système d'exploitation sont activées par défaut pour les éditions du système d'exploitation Windows Client.

## Actions recommandées
Les clients doivent prendre les mesures suivantes pour se protéger contre les vulnérabilités :

- Appliquer toutes les mises à jour disponibles du système d'exploitation Windows, y compris les mises à jour de sécurité mensuelles de Windows.
- Appliquer la mise à jour du microcode fournie par le fabricant de l'appareil.
- Évaluez le risque pour votre environnement sur la base des informations fournies dans les avis de sécurité de Microsoft : ADV180002, ADV180012, ADV190013 et les informations fournies dans cet article de la base de connaissances.
- Prenez les mesures nécessaires en utilisant les avis et les informations sur les clés de registre fournis dans cet article de la base de connaissances.

## Télécharger les fichiers nécessaires :

Téléchargez les fichiers nécessaires à partir du site[GitHub Repository](https://github.com/simeononsecurity/Windows-Spectre-Meltdown-Mitigation-Script)

## Comment exécuter le script :

**Le script peut être lancé à partir du téléchargement GitHub extrait comme suit:**
```
.\sos-spectre-meltdown-mitigations.ps1
```
