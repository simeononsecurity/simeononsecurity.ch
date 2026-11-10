---
title: "Installer les mises à jour cumulatives de sécurité dans Windows"
date: 2023-03-22
lastmod: 2026-11-07
toc: true
draft: false
description: "Apprenez à installer les mises à jour cumulatives de sécurité dans Windows et appliquez les bonnes pratiques pour protéger votre système contre les cyberattaques."
tags: ["Windows", "correctifs de sécurité", "cybersécurité", "sécurité du système", "Microsoft", "mises à jour cumulatives", "gestion des correctifs", "sauvegarde des données", "Spectre Meltdown", "chiffrement", "vulnérabilités du système", "mises à jour système", "déploiement de correctifs", "environnements hors production", "configuration du système", "sécurité informatique", "système de gestion des correctifs", "analyse des vulnérabilités", "notes de version", "maintenance du système"]
cover: "/img/cover/best-practices-for-installing-security-patches-on-windows.webp"
coverAlt: "Un technicien d'origines diverses est assis à un bureau devant un écran affichant une mise à jour Windows. Des appareils technologiques l'entourent, dans un décor sombre aux accents bleus et verts."
coverCaption: ""
---

**Installer les mises à jour cumulatives de sécurité dans Windows**

Les **cyberattaques** représentent aujourd'hui une menace importante pour la sécurité des systèmes informatiques. L'installation de **correctifs de sécurité** est l'un des moyens de réduire ce risque. Microsoft publie régulièrement des **mises à jour cumulatives de sécurité** pour Windows. Elles regroupent les correctifs précédents et les nouvelles mises à jour de sécurité.

## Pourquoi installer les mises à jour cumulatives de sécurité

Les **mises à jour cumulatives de sécurité** sont essentielles pour protéger Windows. Elles corrigent les vulnérabilités et les failles que des cybercriminels pourraient exploiter. Leur absence peut entraîner de graves problèmes de sécurité et des violations de données.

## Comprendre les mises à jour cumulatives de sécurité

Comme indiqué précédemment, Microsoft publie régulièrement des **mises à jour cumulatives de sécurité**. Elles comprennent toutes les mises à jour et corrections de sécurité déjà publiées, ainsi que les nouvelles. Une **mise à jour cumulative de sécurité** fait gagner du temps et réduit les efforts, car il n'est pas nécessaire d'installer chaque mise à jour séparément.

______

## Étapes d'installation des mises à jour cumulatives

L'installation d'une **mise à jour cumulative de sécurité** dans Windows se déroule en quelques étapes simples :

1. **Rechercher des mises à jour :** Vérifiez d'abord si une mise à jour cumulative de sécurité est disponible. Ouvrez **Windows Update** dans le **Panneau de configuration** ou recherchez **Windows Update** dans la barre de recherche de Windows. Cliquez ensuite sur **Rechercher des mises à jour**.

2. **Télécharger et installer :** Si des mises à jour sont disponibles, téléchargez-les et installez-les. Les mises à jour cumulatives de sécurité comprennent généralement toutes les mises à jour antérieures, vous n'avez donc pas besoin de les installer séparément. Téléchargez et installez la mise à jour la plus récente pour inclure les précédentes.

3. **Redémarrer :** Une fois l'installation terminée, redémarrez l'ordinateur pour appliquer les mises à jour. Faites-le même si Windows ne vous le demande pas, car certaines mises à jour ne prennent effet qu'après le redémarrage.

Certaines mises à jour nécessitent une configuration supplémentaire ou des changements de paramètres après l'installation. **Lisez les informations du correctif** pour vérifier qu'il est correctement installé et configuré. Certaines mises à jour imposent d'autres exigences. Par exemple, le correctif Spectre/Meltdown nécessite de définir des registres supplémentaires.

Ces étapes contribuent à maintenir Windows à jour et à protéger le système contre les cybermenaces.

______

## Bonnes pratiques pour installer les mises à jour cumulatives de sécurité

Suivez ces bonnes pratiques afin d'installer correctement les **mises à jour cumulatives de sécurité**.

### Lire les informations sur les correctifs

Avant d'installer une **mise à jour cumulative de sécurité**, lisez attentivement les **notes de version**. Elles contiennent des renseignements importants sur le correctif, notamment les problèmes connus, les exigences système et les prérequis. Vous pourrez ainsi vérifier sa compatibilité et éviter les problèmes liés à l'installation.

Par exemple, la **mise à jour cumulative de mai 2021** pour **Windows 10 versions 2004 et 20H2 présentait un problème connu** qui provoquait des plantages avec certains pilotes d'imprimante. **Ce problème figurait dans les notes de version**, qui conseillaient aux utilisateurs de désinstaller le correctif s'ils le rencontraient.

**Certains correctifs peuvent nécessiter une configuration supplémentaire ou des changements de paramètres après l'installation.** Les notes de version de chaque mise à jour précisent ces éléments. Suivez soigneusement les consignes pour installer et configurer correctement le correctif.

En bref, lire les notes de version avant d'installer une mise à jour cumulative de sécurité aide à éviter les problèmes et à installer la mise à jour correctement.```

### Correctifs cumulatifs

Avant d'installer des **correctifs cumulatifs** dans Windows, il est important de comprendre leur fonctionnement. Comme leur nom l'indique, ils comprennent les mises à jour de sécurité et les correctifs précédents. Vous pouvez donc installer le dernier correctif sans installer d'abord chacun des précédents.

**Consultez tout de même les notes de version de chaque correctif pour vérifier que les versions antérieures sont bien incluses.** C'est généralement le cas, mais il existe des exceptions. Un correctif publié après la dernière mise à jour cumulative peut ne pas figurer dans la plus récente et devra alors être installé séparément.

**Les notes du correctif de sécurité le plus récent ne décrivent pas toujours les configurations supplémentaires requises par les correctifs précédents.** **Le correctif Spectre/Meltdown exige, par exemple, de définir des registres supplémentaires.** Pour protéger entièrement votre système, **consultez les notes de tous les correctifs** et appliquez les configurations supplémentaires nécessaires.

Les correctifs cumulatifs comprennent généralement toutes les mises à jour de sécurité et tous les correctifs antérieurs. Vérifiez tout de même les notes de version pour confirmer que votre système est protégé.

### Exigences supplémentaires

En plus de lire les notes de version d'une **mise à jour cumulative de sécurité**, vérifiez si le correctif impose des exigences supplémentaires. Par exemple, le correctif Spectre/Meltdown nécessite de définir des registres supplémentaires. Une mauvaise configuration peut nuire aux performances du système.

**Pour éviter les problèmes, consultez les notes de version et respectez les exigences supplémentaires.** Il peut s'agir de définir de nouveaux paramètres ou de modifier la configuration existante. Assurez-vous de bien comprendre votre système avant de le modifier.

Connaître les exigences supplémentaires d'une **mise à jour cumulative de sécurité** contribue à maintenir votre système protégé. Prenez le temps d'examiner les notes de version et les exigences.

### Sauvegarder vos données

Il est recommandé de sauvegarder vos données avant d'installer une mise à jour ou un correctif, en particulier une **mise à jour cumulative de sécurité**. Celle-ci peut avoir un impact important sur votre système. En cas de problème pendant l'installation, vous pourrez restaurer vos données depuis une sauvegarde.

Vous pouvez utiliser un disque dur externe, un service cloud comme Dropbox ou Google Drive, ou un logiciel de sauvegarde comme Acronis ou EaseUS. Quelle que soit la méthode retenue, créez une sauvegarde complète du système et des données, puis conservez-la dans un endroit sûr.

Il est également conseillé de créer un point de restauration avant d'installer le correctif. Ce point est un instantané de la configuration et des paramètres du système. Il vous permettra de revenir à un état antérieur en cas de problème.

La sauvegarde des données et la création d'un point de restauration avant l'installation d'une **mise à jour cumulative de sécurité** protègent votre système et vos données si l'installation rencontre un problème.

### Installer régulièrement les correctifs

Installez régulièrement les **mises à jour cumulatives de sécurité** pour protéger votre système. Elles corrigent les nouvelles vulnérabilités et les problèmes de sécurité.

En 2021, Microsoft a publié plusieurs correctifs pour la vulnérabilité PrintNightmare. Celle-ci permettait à des attaquants de prendre le contrôle à distance du système d'une victime. L'installation du correctif de Microsoft protégeait contre ce type d'attaque.

L'installation rapide des correctifs maintient votre système à jour avec les dernières mesures de sécurité. Elle contribue à prévenir les attaques et à assurer le bon fonctionnement du système.

### Tester dans un environnement hors production

Testez les **mises à jour cumulatives de sécurité** dans un environnement hors production avant de les installer en production. Cela permet de repérer les problèmes potentiels liés au correctif.

Supposons qu'une application web fonctionne dans un environnement de production. Avant d'installer un nouveau correctif de sécurité, testez-le dans un environnement hors production afin de détecter d'éventuels problèmes de compatibilité ou de performances.

Un test dans un environnement hors production permet de détecter et de corriger les problèmes avant qu'ils affectent l'application en service. Vous réduisez ainsi le risque d'interruption ou de perte de données causée par un correctif non testé.

Les tests hors production permettent de vérifier qu'un correctif n'aura pas d'effet négatif sur l'environnement de production.

### Utiliser un système de gestion des correctifs

Un **système de gestion des correctifs** est un outil automatisé qui aide à gérer et à déployer les **mises à jour cumulatives de sécurité** sur plusieurs systèmes. Il automatise le déploiement et réduit le temps et les efforts nécessaires pour maintenir les systèmes à jour.

**Microsoft System Center Configuration Manager (SCCM)** est un système de gestion des correctifs courant. Il permet de gérer et de déployer des correctifs dans une organisation. Une console centralisée facilite leur suivi et leur déploiement sur plusieurs systèmes.

Un système de gestion des correctifs présente plusieurs avantages :

- **Déploiement automatisé des correctifs :** automatise le déploiement et réduit le temps et les efforts requis pour maintenir les systèmes à jour.
- **Gestion centralisée :** fournit une console unique pour suivre les correctifs et les déployer sur plusieurs systèmes.
- **Rapports et conformité :** aide à vérifier que les systèmes sont à jour et respectent les politiques de sécurité.

Un système de gestion des correctifs simplifie leur déploiement et contribue à maintenir tous les systèmes à jour, ce qui réduit les risques d'incident de sécurité et d'interruption.```

______

## Conclusion

L'installation de **mises à jour cumulatives de sécurité** dans Windows est essentielle pour protéger votre système. Suivez les étapes et les bonnes pratiques de cet article pour installer correctement les mises à jour et maintenir le système à jour. Sauvegardez toujours vos données avant une mise à jour et testez régulièrement les correctifs dans un environnement hors production avant leur déploiement en production. Ces bonnes pratiques réduisent le risque de cyberattaque et contribuent à protéger votre système.

## Références :

[1] Microsoft. (2021, 12 janvier). Security Update Guide. Consulté le 22 mars 2023 sur https://msrc.microsoft.com/update-guide/

[2] Microsoft. (2021, 11 août). System Center Configuration Manager (SCCM). Consulté le 22 mars 2023 sur https://docs.microsoft.com/en-us/mem/configmgr/core/understand/introduction

[3] Acronis. (2022). Acronis True Image. Consulté le 22 mars 2023 sur https://www.acronis.com/en-us/products/true-image/

[4] EaseUS. (2022). Todo Backup. Consulté le 22 mars 2023 sur https://www.easeus.com/backup-software/

[5] National Institute of Standards and Technology. (2022, 10 février). Guide to Enterprise Patch Management Technologies. Consulté le 22 mars 2023 sur https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-40r3.pdf

[6] National Cyber Security Centre. (2021). 10 Steps to Cyber Security. Consulté le 22 mars 2023 sur https://www.ncsc.gov.uk/guidance/10-steps-to-cyber-security
