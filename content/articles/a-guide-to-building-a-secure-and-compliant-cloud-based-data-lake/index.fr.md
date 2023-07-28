---
title: "Construire un lac de données sécurisé et conforme basé sur le cloud : Meilleures pratiques pour protéger les données stockées"
date: 2023-04-16
toc: true
draft: false
description: "Ce guide complet présente les meilleures pratiques en matière de sécurité et de conformité lors de la planification, de la création et de la gestion de lacs de données basés sur le cloud."
tags: ["lac de données", "sécurité des nuages", "règles de conformité", "les contrôles d'accès", "chiffrement", "AWS", "Azure", "HIPAA", "GDPR", "contrôle", "rapiéçage", "cybersécurité", "Solution SIEM", "Équipes d'assistance informatique", "paysage des menaces", "migration dans le nuage", "gouvernance du cloud"]
cover: "/img/cover/A_cartoon_image_of_a_castle_being_guarded_by_a_warrior.png"
coverAlt: "Une image de dessin animé représentant un château gardé par un chevalier guerrier, symbolisant le concept de protection forte pour un stockage en nuage sécurisé et conforme"
coverCaption: ""
---

**Un guide pour construire un lac de données sécurisé et conforme basé sur l'informatique en nuage**

Un lac de données basé sur le cloud est un outil précieux pour le stockage et l'analyse de grands ensembles de données. Cependant, il présente des défis uniques en matière de sécurité qui doivent être relevés pour garantir la conformité avec les réglementations gouvernementales. Dans ce guide, nous aborderons les meilleures pratiques pour créer un lac de données sécurisé et conforme basé sur le cloud.

## Planification du lac de données

Avant de commencer à construire un lac de données, **il est essentiel de créer un plan qui prend en compte les exigences de sécurité et de conformité** de votre organisation. Commencez par créer un cadre qui adhère aux normes du secteur, telles que le Règlement général sur la protection des données (RGPD) ou la loi sur la portabilité et la responsabilité en matière d'assurance maladie (HIPAA).

Il est important de choisir le bon fournisseur de cloud, un fournisseur qui a une expérience avérée dans la fourniture de solutions sécurisées qui peuvent répondre à ces réglementations de conformité. Parmi les fournisseurs de cloud les plus populaires figurent Amazon Web Services (AWS), Microsoft Azure et Google Cloud Platform.

En outre, **définissez des contrôles d'accès clairs** pour les utilisateurs, les rôles et les autorisations. Cela concerne les membres de votre équipe interne ainsi que les fournisseurs ou partenaires externes qui peuvent parfois avoir besoin d'un accès.

## Construire le lac de données

Lors de la construction d'un lac de données, **le chiffrement et les contrôles d'accès doivent être mis en œuvre dès la conception** à toutes les étapes du mouvement des données vers, dans et à partir du lac de données. Les processus d'ingestion doivent chiffrer les données pendant le transit et le repos lorsque cela est possible. Utilisez les meilleures pratiques telles que les protocoles de sécurité de la couche de transport sur votre client d'ingestion ou les protocoles de réseau, tels que le protocole de transfert de fichiers sécurisé (SFTP), ou un service Apache Kafka géré.

Les clients ou applications d'ingestion qui copient des données à partir de différents systèmes devraient appliquer des politiques d'accès fondées sur le principe du moindre privilège : n'accorder que les autorisations nécessaires pour copier des informations pertinentes à partir d'une source externe.

En ce qui concerne le stockage, il convient de sélectionner des plateformes qui prennent en charge le chiffrement au repos ou qui offrent d'autres fonctions de cryptographie avancée telles que la gestion des clés, y compris le chiffrement côté serveur avec des clés appartenant au client (CMK).

**Un contrôle strict de l'accès aux données est essentiel**, et des solutions comme AWS Identity and Access Management ou Azure Active Directory offrent un moyen efficace de contrôler les autorisations au niveau de l'objet et au niveau de la gestion.

## Surveillance et gestion du lac de données

Une **surveillance précise de votre infrastructure de lac de données permet d'identifier les failles de sécurité** ou les activités suspectes qui se produisent dans votre lac de données. **Les données sont stockées dans un compte d'audit distinct afin d'éviter qu'elles ne soient supprimées ou modifiées par des pirates. Cela permettra de détecter rapidement les activités suspectes, telles que le balayage de ports, les attaques DDos, les attaques par force brute ou les attaques basées sur le réseau.

Utilisez une solution de gestion des informations et des événements de sécurité (SIEM) telle que AWS CloudTrail ou Azure Monitor pour centraliser la journalisation, automatiser les alertes et effectuer des analyses avancées.

Veillez également à ce que **des correctifs réguliers soient apportés aux composants critiques**. Les mises à jour régulières des progiciels pour les systèmes sous-jacents tels que les systèmes d'exploitation, les bases de données, les serveurs web ou les bibliothèques tierces devraient faire partie de votre modèle de support afin de garantir que les vulnérabilités connues sont corrigées par des équipes de support informatique qualifiées.

## Suivre l'évolution du paysage des menaces

**En raison de l'évolution constante du paysage de la sécurité, les contrôles de sécurité en nuage doivent s'adapter rapidement aux nouvelles menaces.

Si vous cherchez à vous conformer à des réglementations spécifiques régissant le stockage des données, prenez des mesures pour maintenir ces exigences de conformité par le biais d'audits de conformité et de rapports réguliers générés par les services respectifs.

## Conclusion

La mise en œuvre d'un lac de données basé sur le cloud offre des avantages significatifs, mais s'accompagne également d'une charge accrue en matière de sécurité et de conformité. Mais le respect des meilleures pratiques du secteur, telles que le cryptage au repos et en transit, la gestion des contrôles d'accès à un niveau élevé via la gestion des identités et des accès (IAM), la surveillance de votre mise en œuvre via une journalisation avancée et l'utilisation de correctifs continus, vous aideront à construire un lac de données basé sur le cloud sécurisé et conforme.

De concert avec le maintien de contrôles de migration et de gouvernance appropriés, votre organisation peut tirer pleinement parti des services basés sur le cloud tout en maintenant la conformité et la sécurité.

_______

## Références

1. [Guide to using AWS EBS encryption](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIEncryption.html)
2. [Microsoft - HIPAA overview](https://learn.microsoft.com/en-us/azure/compliance/offerings/offering-hipaa-us)
3. [What is SIEM?](https://www.varonis.com/blog/what-is-siem)
4. [AWS - Data ingestion methods](https://docs.aws.amazon.com/whitepapers/latest/building-data-lakes/data-ingestion-methods.html)
5. [HIPAA Security Rule Standards and Implementation Specifications](https://www.hhs.gov/hipaa/for-professionals/security/laws-regulations/index.html)