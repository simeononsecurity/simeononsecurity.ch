---
title: "Réaliser un exercice de restauration de sauvegarde homelab avec Restic"
date: 2026-10-10
lastmod: 2026-11-12
toc: true
draft: false
description: "Vérifiez si une sauvegarde homelab permet de restaurer des fichiers utilisables. Définissez un objectif de reprise, restaurez avec Restic vers un autre emplacement, contrôlez les données et consignez le résultat."
genre: ["Homelab", "Sauvegarde", "Reprise après sinistre"]
tags: ["sauvegarde homelab", "exercice de restauration", "restauration Restic", "vérification de sauvegarde", "test de reprise", "reprise après sinistre", "RPO", "RTO", "dépôt de sauvegarde", "vérification Restic", "sauvegarde NAS", "sauvegarde serveur", "reprise de VM", "restauration de fichiers", "chiffrement de sauvegarde", "surveillance des sauvegardes", "plan de reprise", "test de sauvegarde", "sauvegarde hors site", "intégrité des données"]
cover: "/img/cover/homelab-backup-restore-drill.webp"
coverAlt: "Un serveur homelab et un NAS sauvegardés sur un disque séparé, avec un dossier de restauration vérifié sur un ordinateur de test isolé et un chronomètre."
coverCaption: "Restaurez vers une cible séparée, vérifiez les données et mesurez le temps nécessaire."
---

Un travail de sauvegarde signalé comme réussi ne prouve pas que vous pourrez récupérer un fichier utilisable. Un **exercice de restauration** vérifie le parcours entre la sauvegarde stockée et des données fonctionnelles sans remplacer vos fichiers actifs. Ce guide présente un exemple de restauration de fichiers avec Restic et fournit un compte rendu que vous pourrez répéter après une modification du laboratoire.

<!--more-->

Restic est un programme de sauvegarde. Un **dépôt** est l’espace de stockage protégé qui contient les données sauvegardées. Un **instantané** est un point de sauvegarde enregistré.

## Points essentiels

- **Choisissez un objectif :** Sélectionnez les fichiers ou le service à récupérer et définissez un point de reprise et un délai acceptables.
- **Restaurez séparément :** Utilisez une destination de test vide pour éviter d’écraser les données actives.
- **Vérifiez le résultat :** Ouvrez les fichiers restaurés, contrôlez les données applicatives lorsque c’est possible et mesurez le temps écoulé.
- **Consignez les échecs :** Notez l’identifiant de l’instantané, les éléments manquants, les autorisations et les réparations dans votre plan de reprise.

## Avant de commencer

Vous avez besoin d’un dépôt de sauvegarde fonctionnel, de son mot de passe ou de sa clé, d’une destination avec assez d’espace libre et d’autorisations de lecture sur la sauvegarde et l’emplacement de test. Cet exemple suppose que Restic est installé et que le dépôt contient une sauvegarde récente de fichiers. Le [guide de démarrage rapide de Restic](https://restic.readthedocs.io/en/stable/010_introduction.html) explique la création d’un dépôt et les premières sauvegardes. Le [guide des sauvegardes 3-2-1](/articles/what-is-the-3-2-1-backup-rule-and-why-you-should-use-it/) du site traite de l’emplacement des copies. La [présentation homelab](/articles/what-is-a-homelab-and-should-you-have-one/) propose une courte liste de contrôle des sauvegardes.

Cet exercice vérifie les fichiers d’un instantané. Une base de données, une machine virtuelle ou une application nécessite aussi ses propres étapes de reprise. Isolez le système de test si le démarrage du service restauré risque d’interférer avec le service actif. Une copie de fichiers réussie ne prouve pas que chaque service démarrera.

> **Avertissement :** Pour le premier test, ne restaurez pas vers un chemin actif. Utilisez un répertoire de test vide sur un autre système de fichiers ou un autre hôte. Ne placez pas le mot de passe du dépôt dans des captures d’écran, des tickets ou l’historique du shell.

## Définir l’objectif de reprise

Notez ce dont vous aurez besoin après une panne. L’**objectif de point de reprise (RPO)** indique jusqu’à quel moment les données doivent être récupérées après une interruption. Il représente la perte de données maximale acceptable. L’**objectif de délai de reprise (RTO)** indique combien de temps le service peut rester indisponible. Le NIST définit les deux dans son [guide de planification de continuité](https://nvlpubs.nist.gov/nistpubs/legacy/sp/nistspecialpublication800-34r1.pdf). Vos objectifs doivent tenir compte de la fréquence de modification des données et du temps de restauration sur votre matériel.

| Élément | Objectif illustratif | Informations à consigner |
|---|---|---|
| **Documents familiaux** | Dernière sauvegarde nocturne | Heure du dernier instantané et fichiers ouverts |
| **Configuration d’un service domestique** | Dernière modification connue comme fonctionnelle | Version de configuration et secrets requis |
| **Bibliothèque multimédia de stockage en réseau (NAS)** | Sauvegarde hebdomadaire | Lecture d’un échantillon et temps de restauration |

Ces objectifs sont des exemples, pas des résultats mesurés. Dans votre plan de reprise, notez l’emplacement de la sauvegarde et la manière dont une personne autorisée récupère le mot de passe du dépôt ou la clé de chiffrement. Ne placez aucune valeur secrète dans le plan ou le compte rendu de l’exercice. Stockez les secrets par une voie protégée et indépendante de l’hôte en panne. Un dépôt qui survit alors que son unique mot de passe est perdu n’est pas récupérable.

Choisissez un **ensemble de fichiers critiques** pour cet exercice. Ajoutez un petit fichier que vous savez présent dans l’instantané le plus récent. Pour un service, répertoriez aussi la configuration, l’export de base de données, les certificats et la version de l’application nécessaires à son démarrage. Vérifiez que votre méthode de sauvegarde capture des données applicatives cohérentes avant de compter sur une copie au niveau fichier d’une base de données en cours d’exécution.

## Trouver un instantané

Utilisez l’accès au dépôt autorisé pour l’exercice. Restic pose un verrou temporaire sur le dépôt pendant la lecture ou la modification des données de sauvegarde. Les commandes ci-dessous supposent que le dépôt autorise cette opération. Gardez la source active et la cible de test séparées. Remplacez `/path/to/repository` par le véritable chemin de votre dépôt Restic, puis affichez les instantanés :

```bash
restic -r /path/to/repository snapshots
```

Restic demande le mot de passe du dépôt si vous ne l’avez pas fourni par une méthode de gestion des secrets configurée. Sa [liste des instantanés](https://restic.readthedocs.io/en/stable/010_introduction.html) indique l’identifiant, la date, l’hôte et les chemins sources. Notez l’identifiant et l’horodatage de l’instantané à tester. Comparez l’horodatage à votre RPO. Le journal récent d’une tâche ne remplace pas cette vérification, car l’instantané nécessaire peut être plus ancien que prévu.

Si l’instantané attendu manque, arrêtez l’exercice et examinez la planification des sauvegardes, la sélection de la source et le chemin du dépôt. Ne choisissez pas discrètement un instantané plus ancien en déclarant que l’objectif de reprise est atteint.

## Restaurer vers une cible vide

Créez un **répertoire de destination vide** sur un système de fichiers de test disposant d’assez d’espace pour l’instantané. N’indiquez pas à Restic la source d’origine, un partage de production monté ou un dossier existant contenant des données à conserver. Remplacez `SNAPSHOT_ID` et les deux chemins d’exemple avant d’exécuter cette commande :

```bash
restic -r /path/to/repository restore SNAPSHOT_ID \
  --target /path/to/empty-restore-drill
```

Le [guide de restauration de Restic](https://restic.readthedocs.io/en/stable/050_restore.html) décrit l’identifiant d’instantané et le chemin `--target`. L’arborescence restaurée conserve le chemin source sous le répertoire cible. Localisez les fichiers réels avant d’évaluer le résultat. Si vous n’avez besoin que d’un petit sous-ensemble, utilisez les [filtres d’inclusion documentés](https://restic.readthedocs.io/en/stable/050_restore.html) et notez les exclusions. N’utilisez pas `--delete` pendant un exercice. Restic précise que cette option supprime de la cible les fichiers absents de l’instantané.

Démarrez un chronomètre au début de la restauration. Arrêtez-le lorsque les fichiers requis sont présents et utilisables, pas au premier affichage de progression de la commande. Notez l’emplacement du dépôt, la liaison réseau, la taille des données et l’hôte de test, car ces conditions affecteront une reprise ultérieure.

> **Résultat attendu :** L’instantané choisi est restauré vers une cible distincte sans modifier la source active.

## Vérifier les données et le service

Ouvrez quelques fichiers restaurés avec l’application qui les lit habituellement. Incluez un fichier récent, un ancien et un fichier d’un répertoire imbriqué. Comparez les tailles ou sommes de contrôle connues si vous les avez enregistrées avant la sauvegarde. Sous Linux, contrôlez le propriétaire et les autorisations, car un fichier lisible par le compte de test peut rester inaccessible au compte du service.

Pour un service, restaurez-le dans une instance de test isolée. Contrôlez sa configuration, les secrets requis, la cohérence de la base de données, le démarrage et une action représentative d’un utilisateur. Une restauration de fichiers qui omet une base de données ou un secret ne constitue pas une reprise complète du service. Ne démarrez jamais l’instance de test sur la base de données active ou une adresse de production sans plan de bascule contrôlé.

Après la restauration de l’échantillon, lancez la vérification du dépôt Restic :

```bash
restic -r /path/to/repository check
```

Pour lire toutes les données du dépôt, utilisez `check --read-data` pendant une fenêtre de maintenance. Restic avertit que cette commande lit l’intégralité du dépôt et peut télécharger beaucoup de données depuis un stockage distant. Le [guide de dépannage de Restic](https://restic.readthedocs.io/en/stable/077_troubleshooting.html) décrit cette vérification et son coût. Une vérification sans erreur renforce la confiance, mais ne remplace pas l’ouverture des fichiers restaurés ou le démarrage du service.

```bash
restic -r /path/to/repository check --read-data
```

Comparez l’âge de l’instantané à votre RPO et le temps de reprise mesuré à votre RTO. Si l’un des objectifs n’est pas atteint, l’exercice a échoué même si Restic s’est terminé sans erreur. Modifiez la fréquence des sauvegardes, l’emplacement du stockage, la bande passante ou la procédure de reprise, puis recommencez le test.

## Tenir un compte rendu

Après chaque exercice, rédigez un bref compte rendu. Le [contrôle de sauvegarde SP 800-53](https://csrc.nist.gov/CSRC/media/Projects/risk-management/800-53%20Downloads/800-53r5/SP_800-53_v5_1-derived-OSCAL.pdf) du NIST cite la restauration d’exemples de fonctions système comme méthode de test de la reprise. Un compte rendu reproductible permet de vérifier si le plan progresse.

| Champ | Résultat à saisir |
|---|---|
| **Date et opérateur** | Date de l’exercice et personne qui l’a effectué |
| **Dépôt et instantané** | Emplacement, identifiant, horodatage et chemins sources |
| **Objectif de reprise** | Fichiers ou service testés, avec RPO et RTO |
| **Résultat mesuré** | Âge de l’instantané, temps de restauration et vérifications des fichiers ou du service |
| **Échecs** | Données manquantes, accès à la clé, autorisations, réseau ou problèmes de démarrage |
| **Action suivante** | Responsable, réparation et date du prochain test |

Ne consignez ni le mot de passe du dépôt, ni la clé de reprise, ni le contenu de fichiers sensibles. Conservez-les dans un coffre de secrets protégé et indiquez comment une personne autorisée les récupère pendant une panne.

## Dépannage

- **Mot de passe indisponible :** Vérifiez la voie indépendante de dépôt de la clé. Ne supposez pas que l’hôte en panne sera disponible pour récupérer sa propre clé.
- **Instantané trop ancien :** Vérifiez la planification, les échecs de tâches, les chemins sources et si l’hôte attendu a sauvegardé vers un autre dépôt.
- **Restauration trop lente :** Mesurez la vitesse de lecture du stockage, la liaison réseau et le volume de données. Testez un sous-ensemble critique plus petit, puis révisez le RTO ou la conception de reprise.
- **Fichier présent, service en panne :** Vérifiez les exports de base de données, la version de l’application, le propriétaire, les autorisations, les certificats et les secrets manquants.
- **La vérification du dépôt signale des erreurs :** Conservez la sortie et, si possible, une copie du dépôt. Suivez le guide Restic sur la [recherche des dommages](https://restic.readthedocs.io/en/stable/077_troubleshooting.html) avant toute réparation.
- **Le test a modifié les données actives :** Arrêtez le service de test, vérifiez les données de production et corrigez le plan d’isolation avant de recommencer.

## Étapes suivantes

Répétez cet exercice après toute modification du logiciel de sauvegarde, du stockage, des clés de chiffrement ou des services critiques. Alternez les ensembles de fichiers et les reprises complètes de service au fil du temps. Conservez une copie indépendante selon votre [plan 3-2-1](/articles/what-is-the-3-2-1-backup-rule-and-why-you-should-use-it/). L’objectif est de mesurer une restauration que vous pourrez répéter lorsque l’hôte d’origine aura disparu.
