---
title: "Exercice de restauration d’une VM Proxmox : vérifier le fonctionnement du système invité"
date: 2026-10-11
lastmod: 2026-11-15
toc: true
draft: false
description: "Testez une sauvegarde de VM Proxmox par une restauration isolée. Vérifiez les disques couverts, le mode de sauvegarde, les données invitées, l’état du service et le temps de reprise sans toucher à la production."
genre: ["Virtualisation", "Sauvegarde et restauration", "Laboratoire domestique"]
tags: ["test de restauration Proxmox", "sauvegarde de VM Proxmox", "exercice de restauration Proxmox", "qmrestore", "vzdump", "vérification de Proxmox Backup Server", "sauvegarde par snapshot Proxmox", "test de reprise de VM", "RPO et RTO des sauvegardes", "restauration isolée de VM", "mode de sauvegarde Proxmox", "sauvegarde avec agent invité"]
cover: "/img/cover/proxmox-vm-backup-restore-drill.webp"
coverAlt: "Une sauvegarde passe d’une VM de production orange par un coffre de stockage à une VM de test isolée bleue. Des vérifications portent sur les disques, les services et le temps."
coverCaption: "La fin d’une tâche de sauvegarde marque le début d’un test de restauration."
---

Une tâche de sauvegarde verte indique que Proxmox a écrit une sauvegarde. Elle ne montre pas si le système invité démarre, si ses données sont récentes ni si son service principal fonctionne. **Restaurez une copie sous un nouvel ID de VM sur un réseau isolé.** Le résultat fournit une preuve de reprise avant qu’une panne ne vous impose le test.

<!--more-->

Cet exercice porte sur une **machine virtuelle Proxmox VE**. Les conteneurs suivent d’autres règles de sauvegarde, surtout pour les montages liés et les montages de périphériques. Le [test de sauvegarde et de restauration du homelab](/articles/homelab-backup-restore-drill/) du site traite la récupération de fichiers au sens large. Ici, vous testerez une sauvegarde de VM Proxmox et sa charge de travail.

Un **invité** est le système d’exploitation qui s’exécute dans une machine virtuelle. Les **montages liés** et les **montages de périphériques** exposent des ressources de l’hôte à l’invité. Testez ces ressources au moyen d’un plan de reprise distinct.

## Points clés

- **Définissez d’abord la réussite :** choisissez un élément de données, un contrôle de service et un délai de reprise acceptable.
- **Vérifiez la couverture :** une sauvegarde de VM ignore les disques marqués **No backup** et ne recrée ni services externes ni données exclues.
- **Restaurez séparément :** utilisez un ID de VM libre et gardez le réseau restauré isolé de la production.
- **Consignez les preuves :** mesurez l’âge de la sauvegarde, le temps de restauration, le démarrage, la présence des disques et un véritable contrôle applicatif.

## Avant de commencer

Choisissez une VM dont la sauvegarde peut être testée sans risque. Il vous faut un accès administrateur à Proxmox, une sauvegarde terminée sur un stockage de fichiers ou Proxmox Backup Server (PBS), assez d’espace pour une deuxième VM et un bridge isolé ou un périphérique réseau déconnecté. Un bridge isolé est un réseau virtuel Proxmox sans route vers votre LAN de production. À défaut, utilisez un adaptateur déconnecté ou un VLAN de test. Laissez la VM de production en marche. Réservez un nouvel ID de VM, par exemple **920**, après avoir vérifié qu’aucun autre invité ne l’utilise. Prévoyez assez de temps pour une restauration complète et un test de charge de travail.

Écrivez les critères de réussite avant la restauration. Pour un serveur de fichiers, choisissez un fichier récent et son empreinte ou son contenu attendu. Pour une base de données, choisissez une requête de lecture sans risque et un enregistrement écrit avant la sauvegarde. Pour un service Web, choisissez un contrôle de santé local et une page représentative. Consignez la date la plus récente acceptable pour les données, votre **objectif de point de reprise (RPO)**, et le délai autorisé pour rétablir le service, votre **objectif de délai de reprise (RTO)**. Un écran de démarrage ne suffit pas.

| Élément consigné | Exemple de preuve |
|---|---|
| **Point de sauvegarde** | Heure du snapshot et dernier élément de données attendu |
| **Cible de reprise** | ID de VM libre, stockage cible, bridge isolé |
| **Test de charge** | Connexion, montage du volume et lecture applicative |
| **Délai limite** | Heures de début et de fin de la restauration et du contrôle du service |

Ne connectez pas l’invité restauré au réseau de production avant d’avoir vérifié son nom, son adresse IP, son adresse MAC, ses tâches planifiées et ses intégrations externes. Une identité copiée pourrait entrer en conflit avec la VM en marche ou envoyer des tâches en double.

## Vérifier la couverture de la sauvegarde

**Portée des versions :** ces exemples n’ont pas été exécutés pendant la rédaction de l’article. Consignez la sortie de `pveversion --verbose` avant le test. Consultez la documentation qui correspond à la version de Proxmox VE installée. Notez le backend de stockage, le type d’invité et la sortie des commandes dans le compte rendu.

Sur un nœud Proxmox, la commande en lecture seule suivante affiche la configuration de la VM source. Remplacez **120** par l’ID de votre VM source :

```bash
qm config 120
```

Listez tous les disques virtuels et leur réglage de sauvegarde. La [documentation Proxmox sur les disques de VM](https://github.com/proxmox/pve-docs/blob/master/qm.adoc) précise que l’option **No backup** exclut un disque de la sauvegarde de la VM. Vérifiez si des données applicatives se trouvent sur un disque exclu, un montage hôte, du matériel passé en direct ou un service distant. Consignez leur procédure de reprise distincte. Un test de démarrage de VM ne prouve pas que les données exclues sont protégées.

Vérifiez l’horodatage, la taille, le journal de tâche et l’emplacement de la sauvegarde la plus récente. Dans l’interface Proxmox, ouvrez la vue **Backups** du stockage de sauvegarde ou l’onglet **Backup** de la VM. Vérifiez que la tâche s’est terminée sans erreur. La [documentation Proxmox sur les sauvegardes](https://github.com/proxmox/pve-docs/blob/master/vzdump.adoc) distingue les fichiers de sauvegarde ordinaires du stockage PBS, qui conserve des blocs et métadonnées dédupliqués.

| Mode de sauvegarde | Comportement de la VM | Décision pour cet exercice |
|---|---|---|
| **Snapshot** | Sauvegarde une VM en marche avec peu d’interruption. Les écritures de l’invité présentent un léger risque d’incohérence. | Convient aux tests habituels si la charge tolère ce point de reprise. |
| **Stop** | Arrête l’invité au début de la sauvegarde et offre la meilleure cohérence. | À utiliser si la charge exige un arrêt propre et si l’interruption est acceptable. |
| **Suspend** | Suspend l’invité avant le mode snapshot et ajoute une interruption sans gain général de cohérence. | Ne choisissez pas suspend par défaut comme amélioration de snapshot. |

Ces compromis sont décrits dans la [référence Proxmox sur les modes de sauvegarde](https://github.com/proxmox/pve-docs/blob/master/vzdump.adoc). Un **QEMU Guest Agent** est un service dans l’invité qui permet à Proxmox de demander des actions telles que le gel et le dégel du système de fichiers. Un invité en marche, avec son agent activé et en bon état, prend en charge ces actions pendant une sauvegarde snapshot. Le gel du système de fichiers améliore la cohérence, mais ne remplace pas un contrôle de reprise propre à la base de données. Consignez le mode réel et l’état de l’agent au lieu de supposer qu’une tâche planifiée utilise les réglages souhaités.

## Créer ou sélectionner un point de reprise

Utilisez une sauvegarde planifiée récente et réussie si l’exercice porte sur la reprise habituelle. Si vous avez besoin d’une nouvelle sauvegarde ponctuelle, ouvrez l’onglet **Backup** de la VM, choisissez **Backup now**, définissez le stockage cible et le mode, puis attendez la réussite indiquée dans le journal. Depuis un shell Proxmox, cet exemple sauvegarde la VM **120** vers un ID de stockage nommé **backup-nfs** en mode snapshot :

```bash
vzdump 120 --storage backup-nfs --mode snapshot
```

Remplacez les deux ID par les vôtres. N’exécutez la commande qu’après avoir confirmé que le stockage accepte les sauvegardes et dispose de la place nécessaire. La [référence Proxmox de `vzdump`](https://github.com/proxmox/pve-docs/blob/master/vzdump.adoc) décrit les options de mode et de stockage. Vérifiez le journal de tâche après le retour de la commande. Ne considérez pas une ancienne sauvegarde comme un point de reprise actuel sous prétexte que son nom de fichier semble récent.

Si la cible est **PBS**, exécutez ou inspectez une tâche de vérification pour le datastore sélectionné. La [documentation PBS sur la vérification](https://pbs.proxmox.com/docs/maintenance.html) explique comment vérifier l’intégrité des données de sauvegarde et planifier des contrôles répétés. La vérification détecte les blocs de sauvegarde endommagés. **Une vérification réussie ne prouve pas qu’un système d’exploitation restauré, une application ou une dépendance externe fonctionne.** Poursuivez l’exercice même si le résultat est bon.

## Restaurer sur une VM isolée

Dans l’interface Proxmox, sélectionnez la sauvegarde dans la vue **Backups** du stockage et choisissez **Restore**. Saisissez un ID de VM libre et le stockage cible prévu. Laissez **Start after restore** désactivé. Vérifiez l’option de création d’une nouvelle adresse MAC. La [synopsis officielle de `qmrestore`](https://github.com/proxmox/pve-docs/blob/master/generated/qmrestore.1-synopsis.adoc) définit un ID de VM unique, le choix du stockage, `--unique` pour générer une adresse Ethernet aléatoire et le comportement par défaut qui ne démarre pas la VM restaurée.

Pour une archive `vzdump` basée sur un fichier, cette commande shell présente le même principe. Remplacez le chemin de l’archive, le nouvel ID de VM et l’ID de stockage par les valeurs de votre environnement :

```bash
qmrestore /path/to/vzdump-qemu-120-2026_10_11-02_00_00.vma.zst 920 --storage local-lvm --unique 1
```

La [description de restauration Proxmox](https://github.com/proxmox/pve-docs/blob/master/qmrestore.adoc) indique qu’en l’absence de stockage cible, la restauration essaie le stockage d’origine. Définissez **`--storage`** si l’ancien stockage n’existe pas sur le nœud de test. N’utilisez pas **`--force`** pour un exercice : cette option autorise l’écrasement d’une VM existante alors que cette procédure exige un ID libre. Les sauvegardes PBS se restaurent également dans l’interface Proxmox. Sélectionnez l’entrée du snapshot PBS au lieu de traiter celui-ci comme un fichier `.vma.zst` local.

Avant le premier démarrage, inspectez chaque interface réseau restaurée, y compris les interfaces secondaires et passées en direct. Une **adresse MAC** identifie une interface réseau. **DNS** associe les noms aux adresses. **DHCP** attribue la configuration réseau. Un **VLAN** est un réseau logique transporté sur du matériel partagé. Un **TPM virtuel** stocke l’état de sécurité d’un invité. Déconnectez chaque interface ou reliez-la uniquement à un segment de test isolé. Vérifiez qu’aucune route de production, voie DNS, service DHCP, réseau de gestion ou intégration externe ne reste accessible. Si la charge nécessite un autre service de test, fournissez-en une copie sur le réseau isolé. Comparez les mappages de disques, le firmware, les besoins en TPM virtuel et les périphériques particuliers avec la source. Les disques externes, périphériques passés en direct et secrets stockés hors de la VM nécessitent des plans distincts.

## Tester l’invité et sa charge de travail

Démarrez la VM restaurée et utilisez d’abord sa console. Vérifiez que le système d’exploitation démarre, que tous les volumes attendus sont montés, que l’horloge est cohérente et que l’application démarre. Exécutez ensuite les critères de réussite définis plus tôt. Comparez un élément de données connu à sa valeur et son horodatage avant la sauvegarde. Une invite de connexion ou un processus actif ne prouve pas à lui seul que le service contient les bonnes données.

| Test | Critère de réussite |
|---|---|
| **Démarrage** | L’invité atteint une connexion normale sans mode réparation ni demandes de récupération répétées. |
| **Disques** | Chaque disque inclus apparaît, se monte et contient les données attendues. |
| **Service** | Une requête ou lecture locale représentative réussit. |
| **Point de reprise** | Les données restaurées respectent le RPO consigné. |
| **Délai de reprise** | La restauration, le démarrage et le contrôle du service respectent le RTO consigné. |
| **Isolation** | Aucune adresse, tâche ou intégration de production ne reçoit de trafic en double. |

Gardez l’invité restauré isolé pendant l’inspection des tâches planifiées, hooks de notification, agents de sauvegarde et identifiants applicatifs. N’exécutez pas de test envoyant de vrais messages aux clients ou écrivant dans des services de production. Si un contrôle échoue, consignez l’étape exacte. Distinguez **échec d’intégrité de sauvegarde**, **échec de démarrage de VM**, **données manquantes** et **échec applicatif**. Chaque cas appelle une correction différente.

| Catégorie d’échec | Preuve de confirmation | Première correction | Nouveau test |
|---|---|---|---|
| **Intégrité de sauvegarde** | La tâche de vérification ou de restauration signale des données endommagées | Choisissez un autre point de reprise vérifié et inspectez l’état du stockage | Répétez la vérification et la restauration |
| **Démarrage de VM** | La console affiche des erreurs de firmware, disque ou récupération | Comparez firmware, mappage des disques et ordre de démarrage avec la source | Démarrez la copie isolée et consignez le résultat de la console |
| **Données manquantes** | Le fichier, volume ou enregistrement attendu manque | Vérifiez les disques exclus, montages, snapshots et dépendances externes | Recommencez le contrôle du fichier ou des données nommé |
| **Application** | L’invité démarre mais le contrôle de service échoue | Inspectez journaux, identifiants, dépendances et étapes de reprise du service | Relancez le même contrôle de santé local et test de charge |

Proxmox propose une [restauration de fichiers individuels pour les sauvegardes PBS](https://github.com/proxmox/pve-docs/blob/master/vzdump.adoc). Utilisez-la pour tester un chemin de récupération de fichier si votre charge en a besoin. Un fichier récupéré ne remplace pas le démarrage complet de la VM et le test de service. Proxmox propose aussi la restauration en direct depuis PBS. Sa documentation indique qu’une restauration en direct échouée laisse la VM dans un état indéfini. Pour cet exercice planifié, utilisez une restauration normale et terminée.

## Consigner le résultat et terminer l’exercice

Consignez l’ID de la VM source, le stockage de sauvegarde, l’horodatage de sauvegarde, le mode, le nouvel ID de VM, le stockage cible, l’isolation réseau, les heures de début et de fin de restauration, le test applicatif, l’horodatage des données et les contrôles échoués. Comparez le point et le délai de reprise mesurés à vos objectifs. Un échec n’est une preuve utile que si vous modifiez le plan de sauvegarde et répétez l’exercice.

Éteignez la VM restaurée à la fin du test. Ne supprimez sa copie de test qu’après avoir enregistré le résultat et vérifié que la VM de production fonctionne toujours comme prévu. Conservez la sauvegarde selon votre politique habituelle de rétention. Ne changez pas cette rétention pour faire réussir un seul exercice.

Répétez le test après des modifications majeures du stockage, de l’invité ou de la configuration de sauvegarde. Alternez entre les VM importantes, y compris celles avec disques exclus ou dépendances externes. Le [guide de migration d’Hyper-V vers Proxmox](/articles/hyper-v-to-proxmox-migration-checklist/) exige cette preuve de reprise avant de retirer une VM source. **Une sauvegarde exploitable possède un chemin de restauration connu, une charge testée et un point de reprise mesuré.**

## Étapes suivantes

Répétez l’exercice après des modifications du stockage, de l’invité ou de la sauvegarde. Consultez le [test de sauvegarde et de restauration du homelab](/articles/homelab-backup-restore-drill/) pour la récupération de fichiers.
