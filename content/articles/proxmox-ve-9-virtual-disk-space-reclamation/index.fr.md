---
title: "Proxmox VE 9 : réduire l'espace disque des machines virtuelles et le récupérer"
date: 2026-11-09
lastmod: 2026-11-20
toc: true
draft: false
description: "Réduisez l'espace utilisé par les VM et conteneurs LXC sous Proxmox VE 9. Comparez les formats et stockages, activez discard, lancez trim et vérifiez les instantanés avant de récupérer de l'espace."
genre: ["Virtualisation", "Administration Linux", "plateforme Proxmox VE", "Stockage", "Laboratoire à domicile"]
tags: ["espace disque Proxmox VE 9", "allocation dynamique Proxmox", "notifications discard Proxmox", "commande TRIM Proxmox", "Windows ReTrim sur Proxmox", "Linux fstrim sur Proxmox", "espace disque LXC Proxmox", "allocation dynamique LVM Proxmox", "zvol sparse ZFS Proxmox", "périphériques bloc Ceph RBD Proxmox", "format qcow2 Proxmox", "disque raw Proxmox", "instantanés Proxmox", "récupération d espace disque virtuel", "types de stockage Proxmox", "contrôleur VirtIO SCSI", "détection des écritures nulles Proxmox", "stockage des sauvegardes Proxmox"]
cover: "/img/cover/proxmox-ve-9-virtual-disk-space-reclamation.webp"
coverAlt: "Deux grilles de blocs reliées par une flèche montrent les blocs utilisés d'un disque virtuel et la capacité libre d'un pool de stockage."
coverCaption: "La suppression dans l'invité, discard et la récupération du stockage sont des étapes distinctes."
---

**Un système de fichiers invité plus petit ne réduit pas toujours l'espace utilisé sur Proxmox.** Pour libérer de l'espace sur l'hôte, il faut un disque compatible avec le thin provisioning, un chemin discard fonctionnel pour les VM et un stockage de secours sans blocs retenus par des instantanés. Ce guide présente les réglages et vérifications pour les VM et conteneurs LXC de Proxmox VE 9.

<!--more-->

## Points clés

- **Choisissez d'abord le stockage de secours.** La taille annoncée d'un disque virtuel ne diffère de l'espace alloué sur l'hôte que si son format ou son stockage prend en charge le thin provisioning.
- **Activez discard pour la VM, puis lancez trim dans l'invité.** Windows ReTrim et Linux `fstrim` transmettent les demandes de blocs inutilisés par le disque virtuel.
- **Vérifiez séparément les instantanés et les sauvegardes.** Les anciens blocs restent alloués tant qu'un instantané y fait référence. Les fichiers de sauvegarde et blocs PBS suivent leurs propres règles de rétention.
- **Distinguez les types de montage LXC.** Les volumes rootfs et points de montage gérés, les bind mounts et les montages de périphériques ont des propriétaires et règles de sauvegarde différents.

## Avant de commencer

Il vous faut **un accès administrateur à Proxmox VE 9**, une sauvegarde vérifiée de chaque invité concerné et assez d'espace libre dans le pool pour l'opération. Notez l'ID de chaque invité, le bus du disque, l'ID de volume, l'ID de stockage, les instantanés et l'allocation actuelle avant de modifier les réglages. Utilisez le [test de restauration de VM](/articles/proxmox-vm-backup-restore-drill/) pour vérifier la reprise.

**Durée estimée :** 20 à 60 minutes par invité, plus tout travail important de trim ou de nettoyage. **Difficulté :** Intermédiaire. Commencez par une VM à faible risque et comparez son stockage avant et après.

> **Avertissement :** Un thin pool saturé provoque des erreurs d'E/S dans les invités et risque d'endommager les systèmes de fichiers. Ne surallouez pas la capacité sans surveiller l'espace libre de données et de métadonnées du pool. [Documentation du stockage Proxmox](https://github.com/proxmox/pve-docs/blob/master/pvesm.adoc)

## Suivre la chaîne de réservation

La **suppression**, **discard** et la **récupération** interviennent à des couches distinctes. L'invité supprime un fichier et marque ses blocs comme libres. Son système de fichiers envoie TRIM ou UNMAP pour ces blocs. QEMU relaie la demande si discard est activé sur le disque virtuel. Le stockage libère l'allocation physique si son format et son pool prennent l'opération en charge. [Documentation des disques VM Proxmox](https://github.com/proxmox/pve-docs/blob/master/qm.adoc)

| Couche | Élément à vérifier | Indice utile |
|---|---|---|
| **Fichiers de l'invité** | Espace libre du système de fichiers | Propriétés du volume Windows ou `df -h` sous Linux |
| **Disque virtuel** | Bus, discard, émulation SSD, format d'image | Onglet **Hardware** de la VM ou `qm config VMID` |
| **Volume PVE** | Propriétaire et taille configurée | Onglet **Content** du stockage ou `pvesm list STORAGE_ID` |
| **Pool de stockage** | Données et métadonnées libres, blocs retenus | `pvesm status` et outils propres au stockage |

**Un disque virtuel de 100 Gio fixe une limite de capacité, pas une allocation garantie de 100 Gio.** À l'inverse, si l'invité indique 20 Gio utilisés, cela ne prouve pas que l'hôte en utilise 20. Les métadonnées, instantanés, sauvegardes et blocs déjà écrits changent le résultat. [Documentation du stockage Proxmox](https://github.com/proxmox/pve-docs/blob/master/pvesm.adoc)

## Comparer les catégories de fichiers disque

**Le stockage détermine les formats d'image proposés par Proxmox.** Les zvols ZFS et Ceph RBD utilisent des disques virtuels raw. LVM utilise généralement raw, avec une exception de chaîne de volumes de Proxmox VE 9 décrite plus loin. Les stockages de fichiers comme directory et NFS prennent en charge raw ou qcow2. Raw ne fournit à lui seul ni allocation thin ni instantanés. Le stockage sous-jacent doit assurer ces fonctions. Qcow2 fournit l'allocation par copie à l'écriture et les instantanés au niveau de l'image. [Documentation des disques VM Proxmox](https://github.com/proxmox/pve-docs/blob/master/qm.adoc)

| Format | Mécanisme d'allocation | Compromis d'espace |
|---|---|---|
| **qcow2 sur stockage de fichiers** | Qcow2 alloue les clusters à l'écriture | Métadonnées d'image et chaînes d'instantanés consomment de l'espace |
| **Fichier raw sur stockage de fichiers** | Fichier creux du système de fichiers, si pris en charge | Raw seul ne fournit ni thin provisioning ni instantanés |
| **Volume bloc raw** | LVM thin, ZFS, Ceph RBD ou autre stockage sous-jacent | Allocation du pool et instantanés dépendent du stockage |

**Proxmox VE 9 thick LVM propose un mode d'instantané particulier.** `snapshot-as-volume-chain` utilise des relations qcow2 entre volumes logiques thick LVM. Il n'utilise pas les instantanés internes qcow2. L'option concerne uniquement les nouveaux disques VM et reste une préversion technologique dans la documentation Proxmox actuelle. PVE considère chaque instantané comme entièrement alloué. L'allocation réelle sur la SAN est plus faible seulement si le stockage prend en charge le thin provisioning et discard. [Documentation du stockage LVM Proxmox](https://github.com/proxmox/pve-docs/blob/master/pve-storage-lvm.adoc)

**Ne convertissez pas un disque uniquement parce que son extension est `.raw`.** Vérifiez d'abord le module de stockage et ses blocs alloués. Un disque raw sur `local-lvm` n'a pas le même comportement qu'un fichier raw entièrement alloué sur un stockage directory ordinaire.

## Comparer les catégories de stockage

Proxmox distingue le **stockage de fichiers** du **stockage bloc**. Le module contrôle aussi les instantanés, clones, partages et types de contenu acceptés par chaque pool. Vérifiez l'entrée **Datacenter > Storage** avant de compter sur un format ou une fonction. [Tableau des types de stockage Proxmox](https://github.com/proxmox/pve-docs/blob/master/pvesm.adoc)

| Stockage | Comportement du disque VM | Vérification de récupération |
|---|---|---|
| **Directory, ext4, XFS** | Fichiers raw ou qcow2 | Comparez les octets alloués de `du` à la taille virtuelle. Vérifiez les instantanés si une autre couche en fournit. |
| **NFS, CIFS** | Fichiers raw ou qcow2 sur stockage partagé | Vérifiez l'espace alloué sur le serveur. Le résultat trim de l'invité ne prouve pas que le serveur a libéré de l'espace. |
| **LVM à allocation fine (`local-lvm`)** | Volumes logiques raw thin, locaux uniquement | Surveillez les pourcentages de données et métadonnées du thin pool avec `lvs`. |
| **LVM thick** | LV raw ou chaînes de volumes qcow2 VE 9 | La suppression dans l'invité ne réduit pas la réservation fixe du LV. Vérifiez séparément l'allocation thin de la SAN. |
| **Stockage ZFS (`local-zfs`)** | zvols raw ou sous-volumes de conteneur | Vérifiez `sparse`, les propriétés du dataset, l'usage du pool et les instantanés. |
| **Ceph RBD** | Images RBD raw thin sur stockage partagé | Vérifiez la capacité du pool Ceph, l'usage de l'image, ses instantanés et discard. |
| **Btrfs** | Volumes fichiers, avec sous-volumes Btrfs pour images raw | Considérez le module Btrfs de PVE comme une préversion technologique et vérifiez les instantanés et l'usage du système de fichiers. |

**D'autres modules répondent à d'autres besoins.** CephFS fournit un stockage de fichiers partagé. iSCSI et Fibre Channel exposent des périphériques blocs partagés, souvent divisés en volumes VM avec LVM. ZFS over iSCSI utilise des blocs distants adossés à ZFS. Proxmox Backup Server (PBS) stocke des sauvegardes, pas des disques VM actifs. Vérifiez les types de **Content** activés avant d'y placer des données `images`, `rootdir`, `backup` ou `iso`. [Tableau des types de stockage Proxmox](https://github.com/proxmox/pve-docs/blob/master/pvesm.adoc)

**Les indicateurs d'allocation des stockages fichiers comptent lors de la création.** Le `format` du stockage choisit `raw`, `qcow2` ou `vmdk` si disponible. `preallocation` pour raw et qcow2 accepte `off`, `metadata`, `falloc` ou `full`. La valeur par défaut est `metadata`, traitée comme `off` pour raw. `full` réserve tout l'espace à l'avance et annule la petite empreinte initiale habituelle. Vérifiez la configuration avant de créer un grand disque. L'indicateur `shared` déclare uniquement un accès partagé existant. Il ne rend pas un stockage local partagé. [Propriétés communes du stockage Proxmox](https://github.com/proxmox/pve-docs/blob/master/pvesm.adoc)

**`sparse` de ZFS est le réglage de stockage qui crée des zvols thin.** Sans zvol sparse, la création réserve une capacité selon le comportement configuré du volume. Vérifiez la configuration du stockage et le pool avant de modifier un déploiement existant. [Documentation du stockage ZFS Proxmox](https://github.com/proxmox/pve-docs/blob/master/pve-storage-zfspool.adoc)

**Le stockage directory nécessite une seconde vérification.** La longueur logique d'un fichier qcow2 n'est pas sa capacité virtuelle visible par l'invité. `du -h` indique les blocs de système de fichiers alloués à l'image. `ls -lh` affiche sa longueur logique. Pour une VM arrêtée, `qemu-img info` indique la capacité virtuelle et la taille sur l'hôte. Sur NFS, fiez-vous à la comptabilité du serveur pour les décisions de capacité. [Référence QEMU `qemu-img`](https://www.qemu.org/docs/master/tools/qemu-img.html)

**NFS comporte une autre limite d'allocation.** La réutilisation par qcow2 d'un cluster vide dans son fichier ne signifie pas que le serveur NFS libère les blocs du fichier. La libération de trous exige la prise en charge du client, du protocole négocié, du serveur et de son système de fichiers. NFSv4.2 définit `DEALLOCATE`, mais le numéro de version ne prouve pas que le serveur a rendu l'espace. Vérifiez le montage NFS négocié et mesurez l'allocation sur le serveur. [Spécification NFSv4.2 `DEALLOCATE`](https://www.rfc-editor.org/rfc/rfc7862.html#section-6.2.2)

## Régler les indicateurs du disque VM

Dans l'interface Proxmox, ouvrez **VM > Hardware > Hard Disk > Edit**. Vérifiez le bus du disque et les options avancées. Ces indicateurs influent sur l'allocation ou déterminent si une optimisation est utile. La [référence officielle des options `qm`](https://github.com/proxmox/pve-docs/blob/master/generated/qm.conf.5-opts.adoc) donne les disponibilités selon le bus.

| Bus | Choix lié à l'espace |
|---|---|
| **IDE** | Compatibilité ancienne. À utiliser seulement si l'invité n'a pas de pilote plus récent. |
| **SATA** | Émulation largement prise en charge. Vérifiez trim et les options du disque avant de compter sur la récupération. |
| **SCSI avec VirtIO SCSI** | Chemin moderne recommandé pour discard et les réglages par disque. Windows a besoin du pilote VirtIO. |
| **VirtIO Block** | Disque paravirtualisé. discard Linux exige le noyau 5.0 ou plus récent. Pas d'émulation SSD. |

| Réglage | Effet | Conseil |
|---|---|---|
| **Transmettre discard (`on`)** | Transmet TRIM ou UNMAP de l'invité | Nécessaire à la récupération initiée par l'invité sur un stockage thin compatible. La valeur par défaut `ignore` bloque la transmission. |
| **Émulation SSD `ssd=1`** | Présente le disque comme SSD à l'invité | Certains invités doivent voir ce type avant d'émettre trim. Ce réglage n'accélère pas le stockage physique. VirtIO Block ne le propose pas. |
| **Detect zeroes `detect_zeroes=1`** | Détecte et tente d'optimiser les écritures de zéros | Optimisation E/S facultative. Ne remplace pas trim et ne garantit pas d'espace récupéré. |
| **Bus : SCSI / VirtIO SCSI single** | Expose un disque SCSI par le contrôleur VirtIO | Choix pratique pour les invités Windows et Linux modernes. Installez les pilotes VirtIO sous Windows. |
| **Bus : VirtIO Block** | Utilise le périphérique bloc VirtIO | discard Linux exige le noyau 5.0 ou plus récent. Pas d'émulation SSD. |
| **Thread E/S `iothread=1`** | Affecte les E/S du disque à un autre thread | À utiliser avec VirtIO Block ou SCSI sur un contrôleur VirtIO SCSI single. Réglage de performance, pas de récupération. |
| **Cache et AIO** | Modifient la mise en tampon et les E/S asynchrones | À régler selon la charge et le stockage. Aucun ne réduit le disque. |
| **Sauvegarde `backup=0`** | Exclut le disque des sauvegardes VM | Réduit la portée de la sauvegarde et supprime ses données de la restauration VM. Documentez une autre sauvegarde. |
| **Réplication `replicate=0`** | Exclut le disque de la réplication | Réduit les données répliquées et exclut le disque de la réplique. |

**D'autres options de lecteur décrivent un comportement, pas la récupération.** `format` s'applique lors de l'allocation sur un stockage proposant plusieurs formats. `size` est la capacité virtuelle, pas les octets alloués. `ro=1` rend le disque en lecture seule. `snapshot=1` active le mode instantané temporaire de QEMU, qui abandonne les changements à l'arrêt de la VM. Ce n'est pas le réglage qui inclut un disque dans les instantanés Proxmox. Évitez-le pour les données persistantes. Vérifiez la couverture de restauration avant `backup=0` ou `replicate=0`. [Options de disque VM Proxmox](https://github.com/proxmox/pve-docs/blob/master/generated/qm.conf.5-opts.adoc)

**Ne collez pas une commande `qm set --scsi0` abrégée sur un disque existant.** Inspectez **`qm config VMID`** et préservez l'ID de volume complet et les options existantes. Une affectation abrégée risque de supprimer d'autres réglages du disque. Dans l'interface, vérifiez les options enregistrées après chaque changement.

```bash
qm config 100
pvesm status
```

`100` est un ID VM d'exemple. Pour un **nouveau** disque SCSI de 64 Gio sur une VM existante dont le contrôleur est **VirtIO SCSI single** et dont l'invité a le pilote nécessaire, cette commande montre la syntaxe d'allocation. Remplacez les ID VM et stockage par les vôtres.

```bash
qm set 100 --scsi0 local-lvm:64,discard=on,ssd=1,iothread=1
```

**Vérifiez si `scsi0` existe déjà avant l'exemple.** La commande modifie cet emplacement. Pour un disque existant, utilisez l'interface s'il est plus simple d'en conserver exactement les options. Voir la [référence des commandes `qm` de Proxmox](https://github.com/proxmox/pve-docs/blob/master/generated/qm.1-synopsis.adoc).

## Nettoyer les fichiers du système invité

**Libérez d'abord les fichiers de l'invité.** Vérifiez les paramètres Stockage Windows, fichiers temporaires, anciens installateurs, caches d'applications et corbeille. Nettoyez les bases de données et runtimes de conteneurs depuis leur propre interface. Supprimer des données d'application actives uniquement pour réduire l'allocation risque de les perdre.

**Confirmez que le volume utilise un disque virtuel compatible discard**, puis lancez une session PowerShell élevée dans la VM Windows :

```powershell
fsutil behavior query DisableDeleteNotify
Optimize-Volume -DriveLetter C -ReTrim -Verbose
```

`DisableDeleteNotify = 0` signifie que Windows a activé les notifications de suppression pour le système de fichiers indiqué. **ReTrim** renvoie les demandes trim pour les régions actuellement inutilisées. Une commande réussie confirme que l'invité a envoyé l'opération, pas le nombre d'octets récupérés sur l'hôte. Vérifiez l'hôte à la fin. [Référence Microsoft `Optimize-Volume`](https://learn.microsoft.com/en-us/powershell/module/storage/optimize-volume?view=windowsserver2025-ps) et [documentation des disques VM Proxmox](https://github.com/proxmox/pve-docs/blob/master/qm.adoc)

**Ne confondez pas QEMU guest agent et TRIM.** L'agent permet le contrôle de l'invité et la cohérence des sauvegardes. Les notifications de suppression du système de fichiers passent par le disque virtuel. Installer l'agent seul ne récupère aucun bloc. [Documentation Proxmox de l'agent invité VM](https://github.com/proxmox/pve-docs/blob/master/qm.adoc)

## Signaler les blocs inutilisés du système de fichiers

**Vérifiez le chemin bloc et le système de fichiers avant trim.** Une distribution moderne lance souvent périodiquement `fstrim.timer`. Vérifiez son état, puis appliquez trim aux systèmes de fichiers montés après suppression des données inutiles.

```bash
lsblk -D
systemctl status fstrim.timer
sudo fstrim -av
```

**`lsblk -D`** affiche la granularité et les limites discard des périphériques visibles. **`fstrim -av`** applique trim aux systèmes montés compatibles et indique les plages envoyées. Les octets envoyés ne sont pas les octets rendus au pool. Les couches chiffrées, LVM, RAID et autres périphériques empilés doivent toutes prendre discard en charge. [Guide Red Hat sur les blocs inutilisés](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/8/html/managing_file_systems/discarding-unused-blocks_managing-file-systems)

Utilisez trim planifié ou une politique discard en ligne réfléchie. **N'activez pas discard continu sur chaque système de fichiers pour éviter de vérifier le chemin de stockage.** Après trim dans l'invité, inspectez le volume et le pool PVE. Vérifiez la politique de compactage propre à une base de données ou un service si des enregistrements supprimés occupent encore ses fichiers.

## Vérifier séparément le stockage des conteneurs

**LXC n'a pas de bus de disque émulé pour son système de fichiers root.** Commencez par `pct config CTID` et repérez chaque entrée `rootfs` et `mpN`. Proxmox définit des montages adossés au stockage, bind mounts et montages de périphériques. Un chemin visible dans le conteneur ne révèle pas le volume hôte qui possède ses blocs. [Points de montage des conteneurs Proxmox](https://github.com/proxmox/pve-docs/blob/master/pct.adoc)

```bash
pct config 101
pct exec 101 -- df -h
pvesm status
```

Pour un **rootfs ou point de montage géré**, supprimez les fichiers depuis le conteneur ou son application, puis vérifiez le volume sous-jacent et ses instantanés sur l'hôte. **N'exécutez pas les commandes `qm` discard d'une VM sur un CT.** Sur les sous-volumes ZFS, les instantanés retiennent les blocs supprimés. Sur directory et LVM thin, vérifiez l'allocation réelle du stockage, pas la taille configurée du CT.

Lancez **`pct fstrim` sur l'hôte Proxmox** après nettoyage du CT si le stockage prend discard en charge. Proxmox applique trim au rootfs du CT et aux points de montage gérés éligibles. Il ignore les bind mounts et les montages en lecture seule. Utilisez `--ignore-mountpoints` pour ne trimmer que le rootfs. Comparez l'usage du stockage avant et après. [Référence Proxmox `pct fstrim`](https://github.com/proxmox/pve-docs/blob/master/generated/pct.1-synopsis.adoc)

```bash
pct fstrim 101
pct fstrim 101 --ignore-mountpoints 1
```

Ces commandes montrent **deux périmètres possibles** pour le CT d'exemple `101`. Utilisez celui qui correspond à votre stockage. Une opération réussie ne garantit pas le même espace libéré si des instantanés retiennent les anciens blocs.

**Proxmox ne gère pas les bind mounts ni les montages de périphériques.** Leurs données sources restent sur l'hôte ou un périphérique externe. Les sauvegardes `vzdump` excluent leur contenu. Les points de montage additionnels adossés à un stockage sont également exclus par défaut, sauf si leur option `backup` les inclut. Vérifiez la vraie politique de sauvegarde avant nettoyage. [Documentation Proxmox des sauvegardes](https://github.com/proxmox/pve-docs/blob/master/vzdump.adoc)

Pour Docker imbriqué, inspectez les couches d'images, volumes et journaux dans le stockage qui les détient avant d'utiliser les commandes de nettoyage Docker. Le [Fiabilité des services exécutés en conteneur](/articles/docker-in-lxc-proxmox-reliability/) couvre les limites de montage et de sauvegarde. Supprimer une image de conteneur ne supprime pas un volume persistant par défaut.

## Mesurer correctement l'hôte

**Prenez les mêmes mesures avant et après le nettoyage.** L'espace libre du pool indique la capacité finale. Utilisez les mesures par volume pour trouver l'invité responsable de la croissance.

```bash
pvesm status
pvesm list local-lvm
qm config 100
pct config 101
```

**`pvesm list`** inventorie les volumes gérés et leurs tailles configurées. Il ne mesure pas les octets alloués sur un stockage thin. Pour **directory**, inspectez le chemin monté exact et un fichier image connu. Remplacez les chemins par ceux de **Datacenter > Storage** et de la configuration VM.

```bash
df -hT /var/lib/vz
du -h /var/lib/vz/images/100/vm-100-disk-0.qcow2
ls -lh /var/lib/vz/images/100/vm-100-disk-0.qcow2
```

Pour une VM **arrêtée**, comparez la capacité virtuelle et l'allocation hôte sans modifier le fichier :

```bash
qemu-img info /var/lib/vz/images/100/vm-100-disk-0.qcow2
```

Pour **LVM thin**, surveillez données et métadonnées du pool :

```bash
lvs -a -o lv_name,vg_name,lv_size,data_percent,metadata_percent,segtype
```

Pour **ZFS**, distinguez les données du dataset actif de celles retenues par les instantanés :

```bash
zpool list
zfs list -o name,used,available,referenced,usedbysnapshots -r POOL_OR_DATASET
zfs list -t snapshot -o name,used,referenced,written -r DATASET
```

**`usedbysnapshots`** indique les blocs retenus par tous les instantanés d'un dataset. Les valeurs `used` des instantanés ne s'additionnent pas, car ils partagent des blocs. La suppression d'un fichier peut ne pas réduire l'usage du pool tant que chaque instantané qui référence ses blocs n'a pas expiré ou été supprimé selon la politique de rétention. [Instantanés et clones OpenZFS](https://openzfs.github.io/openzfs-docs/Basic%20Concepts/Datasets/Snapshots%20and%20Clones.html)

Pour **Ceph RBD**, identifiez l'ID de volume Proxmox avant les commandes Ceph. **`qm config VMID`** affiche `STORAGE_ID:IMAGE`. Ouvrez l'entrée RBD sous **Datacenter > Storage** pour trouver son **pool** et son **espace de noms** facultatif. L'ID de stockage peut différer du nom du pool. Construisez `POOL/IMAGE` avec les valeurs du pool et de l'image. Exécutez ces commandes depuis un client configuré pour le cluster Ceph voulu et muni de justificatifs valides. [Documentation Proxmox du stockage RBD](https://github.com/proxmox/pve-docs/blob/master/pve-storage-rbd.adoc)

```bash
ceph df
rbd du POOL/IMAGE
rbd snap ls POOL/IMAGE
```

**`rbd du`** affiche l'usage provisionné et réel de l'image, y compris ses instantanés. Sans la fonction d'image `fast-diff`, la commande interroge les OSD pour repérer les objets et demande plus de travail. **`ceph df`** affiche la capacité du pool et du cluster. Réplication, codage d'effacement et instantanés influent sur l'usage brut du cluster. Les octets de l'image et du pool diffèrent donc. [Référence des commandes Ceph RBD](https://docs.ceph.com/en/squid/man/8/rbd/) et [guide d'usage des pools Ceph](https://docs.ceph.com/en/squid/rados/operations/monitoring/)

Si le stockage RBD utilise un espace de noms, ajoutez **`--namespace NAMESPACE`** à chaque commande `rbd`. Utilisez l'espace de noms configuré dans l'entrée de stockage Proxmox, pas l'ID de stockage Proxmox.

## Tenir compte des instantanés et des sauvegardes

**Les instantanés conservent d'anciennes versions des blocs.** Si l'usage ne baisse pas après trim, vérifiez l'onglet **Snapshots** de la VM ou du CT et l'inventaire d'instantanés du stockage. Contrôlez le propriétaire et les dépendances avant toute suppression. Une sauvegarde est une copie distincte soumise à la rétention du stockage de sauvegarde, pas au résultat `df` actuel de l'invité.

**La déduplication PBS modifie les comptes.** Son datastore contient des blocs partagés entre les sauvegardes. L'élagage retire les métadonnées des instantanés de sauvegarde. Le ramasse-miettes supprime ensuite les blocs sans référence après un délai de grâce. Vérifiez les deux tâches avant d'affirmer que l'espace de sauvegarde a été récupéré. [Documentation de maintenance PBS](https://pbs.proxmox.com/docs/maintenance.html)

> **Avertissement :** Ne supprimez jamais un fichier de volume géré par Proxmox, un zvol ou un instantané en vous fiant uniquement à son nom. Identifiez d'abord l'invité et sa politique de rétention. Le nettoyage doit préserver la sauvegarde et la possibilité de retour arrière.

## Reconstruire le fichier disque VM arrêtée

**N'effectuez une conversion hors ligne que si trim normal de l'invité et chemin du stockage ne résolvent pas un problème d'allocation qcow2.** Arrêtez la VM, vérifiez sa sauvegarde, identifiez les liens d'instantanés et chaînes de base, puis écrivez une image de destination distincte. QEMU déconseille de modifier une image utilisée par un autre processus. [Documentation QEMU `qemu-img`](https://www.qemu.org/docs/master/tools/qemu-img.html)

**Préférez un déplacement géré par Proxmox ou une sauvegarde puis restauration** si le disque possède des instantanés ou réside sur un stockage bloc géré. Un `qemu-img convert` autonome sur une image appartenant à PVE ne met pas à jour la configuration VM, la propriété du volume ou les références d'instantanés. N'utilisez pas `qemu-img resize --shrink` pour récupérer des fichiers supprimés. Réduire la capacité visible risque de tronquer les données si vous n'avez pas d'abord réduit les partitions et systèmes de fichiers.

## Diagnostiquer un échec de récupération

| Symptôme | Vérification probable | Action suivante |
|---|---|---|
| **`df` baisse dans l'invité, pas sur l'hôte** | discard de la VM, trim invité, instantanés | Vérifiez le chemin discard complet et les instantanés conservés. |
| **`fstrim` indique une fonction non prise en charge** | Bus du disque, périphériques empilés, stockage | Inspectez `lsblk -D`, le noyau invité et chaque couche intermédiaire. |
| **Windows ReTrim finit, l'hôte reste stable** | Allocation du stockage, instantanés, compte serveur | Comparez volume et pool. Vérifiez que le disque utilise du stockage thin. |
| **`ls -lh` et `du -h` diffèrent** | Fichier sparse ou qcow2 | Utilisez `du` pour les blocs alloués au fichier. |
| **Thin pool LVM toujours plein** | Données, métadonnées, instantanés | Vérifiez `lvs` et instantanés PVE avant toute suppression. |
| **Pool ZFS toujours plein** | Blocs retenus par instantanés et réservations | Vérifiez `usedbysnapshots`, réglages zvol et capacité du pool. |
| **`df` du CT ne correspond pas au pool** | Bind mounts, points de montage, instantanés | Reliez `rootfs` et chaque `mpN` à son propriétaire sur l'hôte. |

**Vérifiez de nouveau après la fin du travail en arrière-plan.** La comptabilité peut prendre du retard après trim, suppression d'instantané ou collecte des déchets du stockage. Comparez l'espace libre mesuré au point de départ. Ne concluez pas à la réussite sur le seul code de sortie d'une commande invitée.

## Étapes suivantes

**Tenez un registre de stockage pour chaque invité :** taille virtuelle, octets alloués, stockage, bus, discard, nombre d'instantanés, couverture des sauvegardes et espace libre du pool. Choisissez une VM, activez le chemin discard pris en charge, lancez trim dans l'invité et comparez les mesures. Ne répétez que si le résultat de la première VM correspond au comportement attendu du stockage.

Pour planifier la récupération, suivez le [test de sauvegarde et restauration Proxmox](/articles/proxmox-vm-backup-restore-drill/) et le [Migration de la version 8 vers la version 9 de la plateforme](/articles/proxmox-ve-8-to-9-upgrade-guide/).

## Références

- [Administration du stockage Proxmox VE](https://github.com/proxmox/pve-docs/blob/master/pvesm.adoc), types de stockage, thin provisioning et risques de capacité.
- [Stockage LVM Proxmox VE](https://github.com/proxmox/pve-docs/blob/master/pve-storage-lvm.adoc), chaînes de volumes d'instantanés VE 9 et allocation.
- [Stockage RBD Proxmox VE](https://github.com/proxmox/pve-docs/blob/master/pve-storage-rbd.adoc), configuration des pools et espaces de noms.
- [Machines virtuelles Proxmox VE](https://github.com/proxmox/pve-docs/blob/master/qm.adoc), bus disque, formats, discard et agent invité.
- [Options de disque VM Proxmox VE](https://github.com/proxmox/pve-docs/blob/master/generated/qm.conf.5-opts.adoc), indicateurs selon le bus.
- [Conteneurs Proxmox VE](https://github.com/proxmox/pve-docs/blob/master/pct.adoc), systèmes de fichiers root et propriété des points de montage.
- [Commandes de conteneur Proxmox VE](https://github.com/proxmox/pve-docs/blob/master/generated/pct.1-synopsis.adoc), trim des conteneurs depuis l'hôte.
- [Sauvegarde et restauration Proxmox VE](https://github.com/proxmox/pve-docs/blob/master/vzdump.adoc), couverture des sauvegardes VM et CT.
- [documentation Microsoft sur la commande `Optimize-Volume`](https://learn.microsoft.com/en-us/powershell/module/storage/optimize-volume?view=windowsserver2025-ps), syntaxe Windows ReTrim.
- [Guide Red Hat sur les blocs inutilisés](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/8/html/managing_file_systems/discarding-unused-blocks_managing-file-systems), comportement Linux `fstrim`.
- [Instantanés et clones OpenZFS](https://openzfs.github.io/openzfs-docs/Basic%20Concepts/Datasets/Snapshots%20and%20Clones.html), blocs retenus par les instantanés.
- [Référence des commandes Ceph RBD](https://docs.ceph.com/en/squid/man/8/rbd/), usage d'image et instantanés.
- [Spécification NFSv4.2](https://www.rfc-editor.org/rfc/rfc7862.html#section-6.2.2), désallocation d'espace côté serveur.
- [Documentation de maintenance PBS](https://pbs.proxmox.com/docs/maintenance.html), élagage et ramasse-miettes.
- [Utilitaire d'image disque QEMU](https://www.qemu.org/docs/master/tools/qemu-img.html), sécurité de conversion hors ligne.
