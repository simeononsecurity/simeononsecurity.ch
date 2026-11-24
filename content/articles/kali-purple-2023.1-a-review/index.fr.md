---
title: "Kali Purple 2023.1 : nouveautés et fonctions essentielles"
date: 2023-04-08
lastmod: 2026-11-24
toc: true
draft: false
description: "Retour sur Kali Purple 2023.1, ses outils et améliorations, avec des références actuelles pour les laboratoires de sécurité."
tags: ["Kali Linux", "Kali Purple", "2023.1", "hacking éthique", "tests d’intrusion", "cybersécurité", "outils", "framework d’exploitation", "mises à jour Kali ARM", "Kali NetHunter", "documentation Kali", "prise en charge du noyau", "prise en charge du Bluetooth", "LineageOS", "OneUI", "Radxa Zero", "ordinateur monocarte", "correctifs du noyau", "contributions de la communauté", "Discord Kali", "mises à jour Linux", "distribution de hacking éthique", "nouvelles fonctionnalités", "améliorations", "Xfce", "KDE", "GNOME", "Xfce 4.18", "KDE Plasma 5.27", "nouveaux outils et paquets", "prise en charge des appareils ARM", "documentation Kali", "réglementation gouvernementale"]
cover: "/img/cover/A_3D_animated_Kali_Linux_dragon_mascot_surrounded.webp"
coverAlt: "Un dragon Kali Linux animé en 3D est assis sur un bouclier et entouré d’outils de cybersécurité."
coverCaption: ""
---

**Kali Purple 2023.1 : un bilan**

Kali Purple 2023.1 était la première préversion technique de l’orientation défensive de Kali. Cette version n’est plus la plus récente. Cet article revient sur sa publication et ajoute des références actuelles afin que vous ne preniez pas les versions des paquets de 2023.1 pour les versions actuelles.

## État actuel de Kali

L’historique officiel des versions de Kali désigne Kali 2026.2, publiée le 29 juin 2026, comme la deuxième version rolling de 2026. Elle utilise le noyau Linux 6.19 et Xfce 4.20.7. Les [notes de version de Kali 2026.2](https://www.kali.org/blog/kali-linux-2026-2-release/) décrivent aussi GNOME 50, KDE Plasma 6.6, le passage de `sources.list` à `sources.list.d/kali.source` et des changements au démarrage des machines virtuelles.

Kali Purple représente une orientation défensive et purple team au sein de Kali. L’annonce de 2023.1 présentait une préversion technique avec une architecture de référence SOC-in-a-box, des outils défensifs et des catégories de menu issues du NIST Cybersecurity Framework. Ces éléments décrivent le périmètre historique. Pour choisir des paquets actuels, consultez la [documentation des métapaquets](https://www.kali.org/docs/general-use/metapackages/) de Kali et sélectionnez uniquement les groupes d’outils nécessaires à votre laboratoire.

*Réalisez tout exercice offensif ou défensif dans un laboratoire isolé et autorisé. Installer Kali ne vous autorise pas à tester des systèmes que vous ne possédez pas ou n’administrez pas.*

______

## Mises à jour des fonds d'écran et du bureau de Kali

Kali Purple 2023.1 introduit un **nouveau fond d'écran par défaut** appelé Kali Sticker, avec un fond violet et divers autocollants liés à Kali-. Ce nouveau fond d'écran a été inspiré par le travail de /u/Albert-III- et TJ_Null.

En plus du nouveau fond d'écran, Kali Purple 2023.1 met également à jour ses trois principaux environnements de bureau : **Xfce, KDE et GNOME**. Ces mises à jour incluent de nouvelles fonctionnalités, des améliorations de performance et des corrections de bugs.

______

## Xfce 4.18

**Xfce 4.18** apporte plusieurs améliorations notables, notamment :

- Prise en charge améliorée de la mise à l'échelle de l'interface utilisateur
- Mises à jour du gestionnaire de fichiers Thunar
- Profils de panneaux pour une personnalisation facile

______

## KDE Plasma 5.27

La mise à jour **KDE Plasma 5.27** introduit :

- Un nouveau système de mosaïque de fenêtres
- Un thème d'application plus élégant
- Des outils et des widgets plus propres et plus utilisables

______

## Mises à jour de GNOME

Pour GNOME, Kali Purple 2023.1 apporte quelques améliorations d'utilisation, comme la possibilité d'ouvrir rapidement un terminal dans le dossier courant du gestionnaire de fichiers en appuyant sur la touche F4.

______

## Paramètres par défaut du noyau et problèmes connus

Kali Purple 2023.1 met à jour certaines valeurs par défaut du noyau pour une meilleure utilisation.

______

## Nouveaux outils et paquets

Kali Purple 2023.1 ajoute des outils et paquets pour les **tests d’intrusion** et le **hacking éthique**. Parmi les nouveautés :

- **Rizin 0.3.0** : un framework moderne de rétro-ingénierie
- **Ghidra 10.1** : une suite open source de rétro-ingénierie logicielle
- **Python 3.10** : la dernière version du langage de programmation

Ces outils et les mises à jour des paquets existants ont enrichi la préversion 2023.1 pour les professionnels de la sécurité. Les versions indiquées ici décrivent la publication 2023.1, pas celles de Kali 2026.2.

______

## Prise en charge des périphériques ARM

Kali Purple 2023.1 continue d'étendre sa prise en charge des périphériques ARM, en ajoutant la compatibilité avec de nouveaux périphériques comme le **Radxa Zero** et en améliorant la prise en charge existante pour des périphériques comme le **LG V20**. Cette large gamme de support garantit que Kali peut être utilisé sur une variété de matériel, des petits ordinateurs monocartes aux puissants smartphones.

______

## Documentation et communauté

L'équipe Kali a mis à jour sa **documentation** avec de nouveaux guides, tutoriels et conseils de dépannage pour aider les utilisateurs à tirer le meilleur parti de Kali Purple 2023.1. Ils ont également reconnu plusieurs membres de la communauté pour leurs contributions à Kali, mettant en évidence la puissance de la collaboration open-source et la force de la communauté Kali.

______

## Réglementation gouvernementale

Bien que cet article ne traite pas des réglementations gouvernementales spécifiques liées au piratage éthique ou aux tests de pénétration, il est important de noter que ces activités sont réglementées dans de nombreuses juridictions. Assurez-vous toujours d'avoir les autorisations nécessaires et de respecter les lois applicables lorsque vous effectuez des évaluations de sécurité. Pour en savoir plus sur les réglementations pertinentes, consultez les ressources suivantes :

- [The Computer Fraud and Abuse Act (CFAA)](https://en.wikipedia.org/wiki/Computer_Fraud_and_Abuse_Act#:~:text=The%20Computer%20Fraud%20and%20Abuse%20Act%20of%201986,without%20authorization%2C%20or%20in%20excess%20of%20authorization.%20)
- [The General Data Protection Regulation (GDPR)](https://gdpr.eu/)

______

## Conclusion

**Kali Purple 2023.1** était la première préversion de l’orientation défensive de Kali. Elle ajoutait des outils, améliorait la prise en charge d’ARM et enrichissait la documentation. Pour une installation actuelle, consultez les notes de version de Kali et choisissez les paquets adaptés à votre laboratoire. Respectez les règles applicables et ne testez des systèmes qu’avec une autorisation explicite.

______

## Références

1. [Site officiel de Kali Linux](https://www.kali.org/)
2. [Documentation de Kali Linux](https://www.kali.org/docs/)
3. [Téléchargements de Kali Linux](https://www.kali.org/get-kali/)
4. [Computer Fraud and Abuse Act (CFAA)](https://en.wikipedia.org/wiki/Computer_Fraud_and_Abuse_Act#:~:text=The%20Computer%20Fraud%20and%20Abuse%20Act%20of%201986,without%20authorization%2C%20or%20in%20excess%20of%20authorization.%20)
5. [General Data Protection Regulation (GDPR)](https://gdpr.eu/)

______

## Ressources complémentaires

- [Forums officiels de Kali Linux](https://forums.kali.org/)
- [Blog de Kali Linux](https://www.kali.org/blog/)
- [Formation et certification Kali Linux](https://www.offensive-security.com/)

______

## Liste de mise à jour

- **Consultez l’historique des versions.** Lisez l’[historique actuel des versions de Kali](https://www.kali.org/releases/) avant de télécharger une image.
- **Utilisez les images officielles.** Téléchargez-les depuis [Get Kali](https://www.kali.org/get-kali/) et vérifiez les sommes de contrôle publiées.
- **Mettez à jour les installations rolling.** Suivez la [documentation actuelle de mise à jour de Kali](https://www.kali.org/docs/general-use/updating-kali/), plutôt que de reprendre sans vérification l’exemple de dépôt de 2023.1.
- **Choisissez les métapaquets avec soin.** Un laboratoire standard ou orienté Purple n’a pas besoin de tous les paquets Kali.
- **Définissez le périmètre du laboratoire.** Précisez les systèmes autorisés, les périodes de test, la journalisation et le nettoyage avant d’utiliser les outils.
