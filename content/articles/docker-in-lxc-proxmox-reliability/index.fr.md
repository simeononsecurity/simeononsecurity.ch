---
title: "Docker dans LXC sur Proxmox : fiabilité, preuves et migration vers une VM"
date: 2026-09-16
lastmod: 2026-11-13
toc: true
draft: false
description: "Évaluez Docker dans Proxmox LXC à partir d’un échec AppArmor documenté, d’une analyse attentive d’un signalement de blocage de l’hôte, de commandes de diagnostic et d’un plan de migration vers une VM."
genre: ["Virtualisation", "Administration Linux", "laboratoire domestique"]
tags: ["Docker dans LXC", "Docker sur Proxmox", "LXC Proxmox", "machine virtuelle Docker", "fiabilité du homelab", "blocages de l’hôte Proxmox", "VM Debian pour Docker", "conteneurs sans privilèges", "conteneurs imbriqués", "isolation du noyau Linux", "AppArmor", "runc", "lxc-pve", "Docker Compose", "pilotes de stockage Docker", "magasin d’images containerd", "pression mémoire", "Linux PSI", "journal persistant", "sauvegardes Proxmox", "sauvegardes de bind mounts", "migration de VM", "domaines de panne", "passage de GPU", "dépannage du serveur domestique"]
cover: "/img/cover/docker-lxc-vm-homelab-isolation.webp"
coverAlt: "Illustration isométrique d’un serveur domestique montrant des charges imbriquées et un compartiment distinct pour une machine virtuelle reliée au matériel partagé"
coverCaption: "Illustration conceptuelle du matériel partagé et de différentes frontières d’isolation des charges"
---
**Docker dans Linux Containers (LXC)** réduit certains frais d’infrastructure, mais multiplie les interactions entre l’environnement d’exécution des applications et l’hôte Proxmox. Pour les services Docker dont votre foyer dépend, une **machine virtuelle (VM) Debian** constitue un point de départ pratique. Elle sépare le noyau invité et simplifie l’environnement à reproduire lors du dépannage. Cet article examine la vidéo fournie, vérifie le rapport d’incident associé et ajoute des défaillances documentées ainsi qu’un plan de migration.

<!--more-->

## Points clés

- **Distinguez les types de défaillance :** une erreur de démarrage Docker, une VM bloquée et un hôte physique qui ne répond plus exigent des enquêtes différentes.
- **Évaluez les preuves :** la stabilité après migration étaye une décision de rétablissement sans prouver la cause initiale.
- **Consultez la documentation actuelle :** la prise en charge native des images OCI et Docker imbriqué dans LXC correspondent à deux voies de déploiement différentes.
- **Protégez les données persistantes :** les sauvegardes Proxmox et les fichiers Compose ne couvrent pas automatiquement tous les emplacements de données applicatives.
- **Testez le plan de reprise :** mesurez la restauration, le comportement au redémarrage et la disponibilité des services avant de retirer l’ancien déploiement.

## Avant de commencer

**Difficulté :** intermédiaire. **Public :** administrateurs Proxmox qui choisissent entre Docker imbriqué et Docker dans une VM. Vous devez reconnaître un projet Compose, un montage de conteneur et une invite de shell Linux avant de suivre les exemples de diagnostic.

**Temps estimé :** prévoyez 30 à 60 minutes pour l’inventaire et la collecte des éléments. La durée de migration dépend de la taille de la base de données, du débit de stockage, de l’accès au matériel et de la fenêtre d’interruption choisie. Les exemples ci-dessous sont des procédures documentées et des raisonnements illustratifs, pas des benchmarks réalisés dans un laboratoire pour cet article.

| Exigence | Pourquoi c’est important |
|---|---|
| **Accès à la console de l’hôte** | Distingue une panne réseau d’un blocage de l’ensemble de l’hôte |
| **Sauvegardes récentes** | Offre une voie de reprise avant une modification du déploiement |
| **Identifiants de conteneurs et de VM** | Dirige les commandes de l’hôte vers la charge prévue |
| **Inventaire des données applicatives** | Repère les volumes, montages liés, bases de données et dépendances externes |
| **Environnement de test séparé** | Permet de répéter la migration sans doubler les écritures de production |

## Regarder la vidéo source

{{< youtube id="XyPBHhZg0Ok" enable="true" title="Proxmox: The Hidden Danger of Running Docker Inside LXC" description="Présentation de Docker imbriqué dans Proxmox LXC, des blocages intermittents de l’hôte et d’une migration vers des VM Debian" uploadDate="2026-09-15T17:00:09-07:00" >}}

**Vidéo source :** [Proxmox: The Hidden Danger of Running Docker Inside LXC](https://www.youtube.com/watch?v=XyPBHhZg0Ok), publiée le 15 septembre 2026 par *Proxmox x Kubernetes x Homelab x Backup*. La question centrale est la suivante : quelle incertitude opérationnelle accompagne une architecture économe en ressources ?

**Limites des éléments disponibles :** la vidéo raconte un incident et en propose des leçons. Les sections suivantes distinguent les observations du propriétaire, le comportement logiciel documenté et les recommandations qui en découlent.

## Ce que l’incident établit

Le rapport d’origine décrit un **hôte équipé d’un Intel Core i3-13100 et d’une BIOSTAR H610MHP**. Le propriétaire a signalé des blocages intermittents qui affectaient l’accès à l’administration et les services LXC. Un écran connecté a cessé de répondre, bien que le rapport précise que syslog continuait de produire des messages. Cette description est plus précise que celle d’un événement sans aucun journal. [Rapport original sur le forum Proxmox](https://forum.proxmox.com/threads/pve-host-freezes-every-2-3-weeks.185009/)

Le propriétaire a ensuite signalé une **amélioration après la migration**. Dans un suivi du 3 août, il a décrit le déplacement des charges Docker vers des VM Debian et l’arrêt des LXC qui hébergeaient Docker. Il n’avait signalé aucun autre blocage au moment de la mise à jour. La vidéo mentionne une période stable de 16 jours. Aucun de ces éléments ne fournit de reproduction contrôlée ni ne désigne un composant défectueux particulier. [Suivi du propriétaire dans le même fil](https://forum.proxmox.com/threads/pve-host-freezes-every-2-3-weeks.185009/)

| Observation | Ce qu’elle étaye | Ce qu’elle ne démontre pas |
|---|---|---|
| **Longue période initiale de fonctionnement** | L’ancienne combinaison de charge et de logiciels fonctionnait | La fiabilité après chaque mise à jour ultérieure |
| **L’hôte et les services se bloquent** | La panne dépasse une application | Docker comme cause première |
| **La migration précède l’amélioration** | Une solution opérationnelle utile | L’interaction modifiée qui a supprimé le déclencheur |
| **Seize jours de stabilité** | Une période d’observation limitée | La résolution de tous les incidents récurrents sur deux à trois semaines |

La **période d’observation** mérite un examen attentif. Seize jours se situent dans une fenêtre de récurrence de 14 à 21 jours. Une observation plus longue, couvrant plusieurs anciens intervalles de panne, des charges comparables et la maintenance ordinaire, renforce la confiance sans démontrer une relation causale contrôlée.

**La réussite opérationnelle et la preuve de la cause première** sont deux résultats distincts. Le rétablissement de services domestiques fiables justifie une migration. Décrivez le résultat comme une amélioration de fiabilité observée jusqu’à ce que des preuves plus solides établissent le mécanisme.

## Repérer la frontière du noyau

```text
Docker dans LXC :
Application -> environnement d’exécution Docker -> espaces de noms et règles LXC
                 -> noyau de l’hôte Proxmox -> matériel physique

Docker dans une machine virtuelle :
Application -> environnement d’exécution Docker -> noyau Linux invité
                 -> matériel virtuel / KVM-QEMU
                 -> noyau de l’hôte Proxmox -> matériel physique
```

**LXC** utilise le noyau de l’hôte. Les espaces de noms, groupes de contrôle, capacités, seccomp et profils de sécurité limitent les processus sans fournir un noyau distinct. Ajouter Docker dans LXC crée une autre couche de gestion de conteneurs pour des charges qui utilisent le même noyau hôte. [Architecture et fonctionnalités de confinement LXC](https://linuxcontainers.org/lxc/introduction/)

Une **VM** apporte un noyau invité. Une panne du noyau invité touche normalement cette VM, tandis que Proxmox continue de gérer les autres invités. La VM dépend toujours de l’hôte physique, de l’hyperviseur, du stockage et du réseau. Une panne matérielle ou un défaut du noyau hôte reste une dépendance commune.

| Frontière | Docker dans LXC | Docker dans une VM |
|---|---|---|
| **Noyau utilisé par les applications** | Noyau de l’hôte Proxmox | Noyau invité |
| **Environnement du runtime Docker** | Limité par les règles du conteneur externe | Installé dans un système invité classique |
| **Mises à jour du noyau invité** | Liées au noyau de l’hôte | Gérées dans l’invité |
| **Panne de l’hôte physique** | Arrête les charges dépendantes | Arrête les charges dépendantes |

Une VM limite **une partie de la propagation des défaillances**, pas la totalité. Le plantage d’un processus applicatif dans LXC ne fait pas automatiquement planter Proxmox. De même, placer tous les services domestiques dans une seule VM Docker les regroupe derrière un système invité et un calendrier de maintenance communs.

Pour une **comparaison conceptuelle plus large**, consultez [Conteneurs Docker et machines virtuelles](/articles/docker-vs-vms/). Ici, la décision porte sur le placement de Docker dans Proxmox et les limites de dépannage qui en résultent.

## Définir précisément le support

Le terme **« non pris en charge »** exige de nommer un composant et une version. Distinguez le déploiement recommandé par le fournisseur, les fonctionnalités documentées, la maintenance de la distribution et le droit contractuel à une assistance. Une pile imbriquée fonctionnelle ne prouve pas que toutes les combinaisons sont testées au même niveau. Une recommandation en faveur des VM ne signifie pas que les mainteneurs refusent tout bug lié à l’imbrication.

**La documentation actuelle de Proxmox** apporte une distinction importante. Le code source de la boîte à outils des conteneurs décrit la prise en charge des images applicatives **Open Container Initiative (OCI)** comme un aperçu technologique qui convertit les images au format du framework LXC. Pour les besoins privilégiant l’isolation et la migration à chaud, il recommande aussi les conteneurs dans une VM QEMU. L’importation d’une image OCI dans ce framework diffère de l’installation de Docker Engine et du lancement de Compose dans un invité LXC. [Documentation de la boîte à outils de conteneurs Proxmox](https://github.com/proxmox/pve-docs/blob/master/pct.adoc)

| Déploiement | Question à vérifier |
|---|---|
| **Invité LXC classique** | Son modèle de système et son application respectent-ils les restrictions documentées des conteneurs ? |
| **Docker imbriqué dans LXC** | Quelles combinaisons de noyau, runtime, règles de sécurité et stockage ont été testées ? |
| **Importation native d’image OCI** | La version Proxmox installée offre-t-elle la fonctionnalité documentée et le comportement requis ? |
| **Docker dans une VM Debian** | La version invitée répond-elle aux exigences d’installation de Docker ? |

Docker publie une **procédure d’installation pour Debian**. Utilisez la liste des versions prises en charge et les instructions du dépôt pour l’invité. Notez les versions déployées plutôt que de supposer qu’un ancien tutoriel est toujours valable. Il s’agit d’une base d’installation documentée, pas d’une garantie de disponibilité ni d’un contrat d’assistance payant automatique. [Docker Engine sur Debian](https://docs.docker.com/engine/install/debian/)

## Une défaillance d’imbrication confirmée

L’**incompatibilité runc/AppArmor de 2025** est un exemple vérifiable. Les mainteneurs de runc ont documenté un échec lors de la réouverture d’un descripteur dans un conteneur externe doté d’un profil AppArmor. AppArmor interprétait à tort un accès sous **`/proc/sys`** comme un accès sous **`/sys`**, ce qui entraînait un refus de la politique. [problème runc 4968](https://github.com/opencontainers/runc/issues/4968)

Un **démarrage affecté** signalait cet extrait d’erreur :

```text
open sysctl net.ipv4.ip_unprivileged_port_start file: reopen fd 8: permission denied
```

La défaillance documentée empêchait le **démarrage du conteneur**. Elle n’explique pas les blocages de l’hôte rapportés sur le forum. L’issue indique **`lxc-pve 6.0.5-2`** comme correctif Proxmox pour ce problème précis. La modification correspondante de LXC en amont a été fusionnée le 20 novembre 2025. *Il s’agit de références à des correctifs historiques, pas d’une recommandation de figer un paquet dans une installation actuelle.* [Résumé du correctif par les mainteneurs](https://github.com/opencontainers/runc/issues/4968), [modification LXC fusionnée](https://github.com/lxc/lxc/pull/4609)

La leçon porte sur la **coordination des dépendances**. Un changement de sécurité du runtime interagissait avec la politique du conteneur externe, et le correctif a nécessité une intervention dans une autre couche. Préférez la mise à jour maintenue adaptée à votre version plutôt que de désactiver AppArmor de façon permanente ou de conserver un ancien runtime vulnérable.

> **À retenir :** cet incident démontre un vrai problème de compatibilité des conteneurs imbriqués et une réponse réelle des mainteneurs. Il ne prouve ni une instabilité générale de LXC ni la cause d’un blocage distinct de l’hôte.

## Comparer les coûts réels

Mesurez l’efficacité avec votre **charge de travail réelle**. Dans des conditions équivalentes, comparez la pression mémoire de l’hôte, la demande CPU, la latence de stockage, les temps de réponse applicatifs et l’effort de reprise. La RAM attribuée à la VM, la mémoire libre de l’invité et la mémoire résidente de l’hôte sont des mesures différentes.

| Économie annoncée | Mesure à recueillir | Coût supplémentaire à noter |
|---|---|---|
| **Moins de surcharge mémoire** | Utilisation et pression mémoire de l’hôte pour une même charge | Temps de gestion des limites imbriquées et de diagnostic des conflits |
| **Déploiement plus rapide** | Temps nécessaire pour obtenir un service opérationnel avec ses données restaurées | Temps de reconstruction après une mise à jour échouée |
| **Partage matériel simplifié** | Appareils requis, autorisations et bon fonctionnement de l’application | Dépendance au pilote de l’hôte et contraintes de migration |
| **Sauvegardes simplifiées** | Restauration réussie de toutes les données requises | Montages externes et cohérence applicative |

Par défaut, Docker autorise une **utilisation illimitée du CPU et de la mémoire** si aucune limite n’est appliquée. Dans LXC, le conteneur externe ajoute ses propres limites. Dans une VM, l’allocation de l’invité ajoute une autre frontière de capacité. L’invité a aussi besoin de ressources pour son système, Docker, les caches et les pics de demande applicative. [Limites des ressources Docker](https://docs.docker.com/engine/containers/resource_constraints/)

**L’accès au matériel** relève des besoins de la charge. Partager un périphérique graphique de l’hôte avec un conteneur et attribuer un périphérique PCI à une VM impliquent des configurations différentes de pilotes et d’isolation. Précisez l’appareil et le besoin applicatif avant de choisir. Une charge média qui exige le décodage matériel doit par exemple réussir un test de décodage après la migration, en plus des contrôles HTTP habituels.

Évitez les **chiffres universels de surcharge**. Cet article ne donne aucun coût fixe en RAM ni pourcentage de performance, car ces valeurs exigent une charge, une configuration et une méthode de mesure contrôlées. Inscrivez le résultat de votre propre comparaison dans la fiche de décision ci-dessous.

## Recueillir des preuves par couche

**Commencez sur l’hôte Proxmox** avec un shell d’administration. Remplacez **`101`** par l’ID LXC étudié :

```bash
pveversion -v
uname -r
pct config 101
journalctl --list-boots
journalctl -k -b -1 --no-pager
```

**`pveversion -v`** consigne les versions des composants Proxmox installés. **`pct config`** consigne la configuration du conteneur externe. Dans **`journalctl`**, **`-k`** sélectionne les messages du noyau, **`-b -1`** le démarrage précédent et **`--no-pager`** produit une sortie texte dans le terminal. Les messages du démarrage précédent nécessitent des journaux conservés. [Boîte à outils Proxmox](https://github.com/proxmox/pve-docs/blob/master/pct.adoc), [référence systemd journalctl](https://github.com/systemd/systemd/blob/main/man/journalctl.xml)

**Inspectez ensuite l’hôte Docker**, dans le LXC ou la VM qui exécute son démon :

```bash
docker version
docker info
docker compose version
docker ps -a
docker stats --no-stream
```

Consignez **les deux environnements**. L’étiquette de l’image de conteneur seule n’indique ni Docker, containerd, runc, le noyau hôte, la politique de sécurité ni le backend de stockage. Notez l’heure de l’incident, les mises à jour récentes et la réponse de la console locale. Supprimez les identifiants et détails privés des applications avant de publier les éléments de diagnostic.

**Inspectez une charge précise** en remplaçant **`app`** par son nom de conteneur :

```bash
docker inspect --format '{{json .State}}' app
docker inspect --format '{{.RestartCount}}' app
docker inspect --format '{{json .Mounts}}' app
```

**`docker inspect`** expose l’état, le nombre de redémarrages et les montages du conteneur indiqué. Utilisez le compteur de redémarrages comme indice à corréler aux journaux, pas comme preuve d’un défaut de l’hôte. Un conteneur recréé repart aussi avec un historique neuf. [Référence docker inspect](https://docs.docker.com/reference/cli/docker/inspect/)

## Distinguer pression et blocage

**Capturez les informations de pression Linux sur l’hôte** pendant que le problème se développe :

```bash
cat /proc/pressure/cpu
cat /proc/pressure/memory
cat /proc/pressure/io
```

**Pressure Stall Information**, ou PSI, indique le temps perdu par les tâches en attente de ressources. Les champs **`some`** et **`full`** décrivent des conditions d’arrêt distinctes, tandis que **`avg10`**, **`avg60`** et **`avg300`** résument les intervalles récents. La pression mémoire diffère de l’occupation mémoire : un cache volumineux ne suffit pas à démontrer une pénurie. [Documentation Linux PSI](https://docs.kernel.org/accounting/psi.html)

| Élément observé | Interprétation utile | Vérification suivante |
|---|---|---|
| **Un conteneur s’arrête à répétition** | Défaillance de l’application ou du runtime de conteneur | État de sortie, journaux du service, règle de redémarrage |
| **SSH échoue, la console fonctionne** | Panne réseau ou du chemin d’administration | État du lien, pilote NIC, bridge, pare-feu |
| **La mémoire PSI augmente sous charge** | Les tâches perdent du temps à cause de la concurrence mémoire | Limites, récupération mémoire, entrées OOM, hausse de la charge |
| **Les requêtes de stockage bloquent** | Une dépendance d’E/S retarde le travail | État du périphérique, journaux de stockage, latence et files d’attente |
| **Le watchdog signale un lockup** | Le détecteur du noyau a observé un blocage défini | Trace complète, version du noyau, déclencheur reproductible |
| **Aucune dernière entrée de journal** | La collecte s’est arrêtée avant l’arrivée d’une sortie utile | Capture persistante ou externe avant la récurrence |

Un **signalement de lockup Linux** a un sens technique précis. Les watchdogs du noyau distinguent les soft lockups et les hard lockups. Le délai dépassé d’un navigateur ne démontre ni l’un ni l’autre. L’absence d’un signalement watchdog ne prouve pas non plus que l’hôte est resté sain. [Documentation du détecteur de lockup Linux](https://docs.kernel.org/admin-guide/lockup-watchdogs.html)

**Les changements de micrologiciel et d’état d’alimentation** sont des expériences. Notez le paramètre précédent, la raison du changement et la durée d’observation. Désactiver un état de veille du CPU modifie les comportements électrique et thermique. Le signalement d’une autre machine ne suffit pas à recommander partout le même paramètre.

## Conserver des journaux utiles

**La journalisation persistante** augmente les chances de conserver les éléments après un redémarrage. Un fichier de configuration journald utilise ce paramètre :

```ini
[Journal]
Storage=persistent
```

**`Storage=persistent`** demande le stockage des journaux sur disque lorsqu’il est disponible. Configurez la rétention et l’espace disque, puis vérifiez que les anciens démarrages apparaissent dans **`journalctl --list-boots`**. La journalisation persistante dépend toujours de l’écriture des données par l’hôte avant la panne. [Configuration de systemd journald](https://github.com/systemd/systemd/blob/main/man/journald.conf.xml)

**Une observation externe** apporte un autre point de vue. Surveillez le service depuis une autre machine et consignez les horaires. Un moniteur exécuté sur l’hôte Proxmox défaillant disparaît pendant la même panne et distingue moins bien l’indisponibilité d’une télémétrie manquante.

**Test illustratif :** planifiez une vérification HTTP légère depuis un autre système, puis comparez les échecs à la joignabilité de l’hôte et au comportement de la console locale. Un délai dépassé de l’application alors que l’hôte répond appelle une enquête différente d’une panne simultanée de l’application, de l’administration et de la console. Il s’agit d’une conception diagnostique, pas d’un résultat observé lors de l’incident source.

## Planifier une migration contrôlée

Commencez par **un projet Compose à faible risque**. Préparez une VM Debian avec une version répertoriée dans la documentation d’installation Docker, configurez les sauvegardes et attribuez les ressources. Gardez le déploiement d’origine disponible pour le retour arrière jusqu’à ce que le remplacement réussisse ses tests. [Instructions d’installation de Docker sur Debian](https://docs.docker.com/engine/install/debian/)

**Inventoriez le projet Compose** depuis son répertoire de travail :

```bash
docker compose config --quiet
docker compose config --images
docker compose config --volumes
```

**`--quiet`** valide la configuration sans l’afficher. **`--images`** liste les images référencées et **`--volumes`** les volumes nommés. Ces commandes n’exportent pas les données applicatives et ne fournissent pas d’inventaire complet des montages liés. Examinez aussi le fichier Compose et les montages de chaque conteneur. [Référence Docker Compose config](https://docs.docker.com/reference/cli/docker/compose/config/)

| Données ou dépendance | Action de migration |
|---|---|
| **Définitions Compose** | Transférer les fichiers du projet et conserver la configuration testée |
| **Secrets et environnement** | Recréer les valeurs nécessaires via le processus choisi de gestion des secrets |
| **Volumes nommés** | Sauvegarder et restaurer leur contenu selon des procédures cohérentes avec l’application |
| **Chemins montés par liaison** | Transférer ou reconnecter les données source, puis vérifier leur propriétaire |
| **Bases de données** | Utiliser la procédure de sauvegarde/restauration prise en charge ou une copie après suspension des écritures |
| **Périphériques et partages** | Rétablir l’accès et tester le comportement applicatif |
| **Ports et DNS** | Préparer l’adresse de remplacement et planifier la bascule |

Les **volumes** survivent aux conteneurs, mais ne migrent pas d’eux-mêmes. Un fichier Compose nomme les ressources et définit les services. La documentation des volumes Docker décrit des opérations séparées de sauvegarde et de restauration des données persistantes. Ne supposez pas que recréer le projet restaure ses données. [Cycle de vie et sauvegardes des volumes Docker](https://docs.docker.com/engine/storage/volumes/)

Vérifiez séparément la **couverture des sauvegardes Proxmox**. La documentation exclut des sauvegardes de conteneurs le contenu des périphériques et des montages liés. Une sauvegarde réussie du système de fichiers racine LXC ne prouve donc pas que chaque répertoire exposé est protégé. [Documentation des sauvegardes Proxmox](https://github.com/proxmox/pve-docs/blob/master/vzdump.adoc)

### Vérifier le stockage avant la copie

**Inspectez la configuration réelle du stockage Docker** sur chaque hôte Docker :

```bash
docker info
findmnt -T /var/lib/docker
```

**`findmnt`** identifie le système de fichiers qui contient le chemin indiqué. Remplacez **`/var/lib/docker`** si le démon utilise une autre racine de données, et inspectez le chemin de stockage containerd si nécessaire. Docker distingue le magasin d’images containerd des pilotes de stockage classiques, avec des exigences propres à chaque backend. [Sélection du backend de stockage Docker](https://docs.docker.com/engine/storage/drivers/select-storage-driver/)

**Recréez les images et restaurez les données applicatives** selon les procédures documentées du backend choisi. Copier un répertoire de données Docker actif entre des configurations de stockage différentes suppose des éléments supplémentaires sur les métadonnées, les montages et la cohérence. C’est une opération différente de la sauvegarde du volume de données d’une application arrêtée.

### Basculer avec un retour arrière

1. **Répétez la restauration** dans la VM avec des adresses distinctes et des données de test si nécessaire.
2. **Arrêtez les écritures de production** pendant la fenêtre convenue et effectuez la dernière sauvegarde cohérente.
3. **Restaurez et validez** les données applicatives, les autorisations, les identifiants et l’accès matériel requis.
4. **Basculez le routage des services** après la réussite des contrôles propres à l’application.
5. **Laissez l’ancien environnement arrêté** tout en conservant sa configuration et ses données de reprise.
6. **Documentez le retour arrière** des données écrites après la bascule avant de redémarrer l’ancien système.

Évitez **deux processus d’écriture actifs** sur le même stockage de base de données. Un retour arrière après de nouvelles écritures en production exige un plan pour les conserver ou les supprimer intentionnellement. Relancer un ancien conteneur ne réconcilie pas deux historiques de données divergents.

## Tester plus que la disponibilité

Les **tests d’acceptation** doivent suivre l’objectif du service. Un état de conteneur vert confirme qu’un processus tourne. Un service utilisable exige aussi ses données, l’accès réseau, ses dépendances et son comportement de reprise.

| Vérification | Élément à conserver |
|---|---|
| **Fonctionnement applicatif** | Transaction, requête ou opération multimédia réelle réussie |
| **Exhaustivité des données** | Enregistrements, fichiers, autorisations et modifications récentes attendus |
| **Redémarrage de l’invité** | Les services reviennent sans réparation manuelle |
| **Restauration de sauvegarde** | La copie restaurée réussit la même vérification fonctionnelle |
| **Charge représentative** | Latence, CPU, pression mémoire et comportement du stockage |
| **Répétition de maintenance** | Mise à jour testée et procédure de reprise utilisable |
| **Observation prolongée** | Relevés de disponibilité couvrant plusieurs anciens intervalles de panne |

**Décision illustrée :** un service de caméra et un téléchargeur expérimental partagent actuellement une pile imbriquée. Les déplacer tous deux dans une VM améliore la séparation des noyaux, mais conserve une frontière de maintenance commune pour l’invité. Si la disponibilité de la caméra est prioritaire, évaluez des groupes de maintenance et des limites de ressources distincts, puis testez la continuité de l’enregistrement pendant les mises à jour du téléchargeur.

**Raisonnement attendu :** choisissez le placement selon la dépendance du service que vous devez isoler. Deux VM sur un même serveur physique partagent toujours son alimentation, son stockage et son noyau hôte. Si le besoin inclut la survie à une panne du serveur, il faut un système indépendant supplémentaire ou une solution manuelle de repli acceptable.

## Créer votre fiche de décision

**Utilisez des mesures** pour choisir un déploiement et définir quand le réexaminer :

```text
Impact sur le service et le foyer :
Versions actuelles de l’hôte / noyau / LXC / Docker :
Accès requis au GPU, aux appareils et au réseau :
Mémoire, CPU, stockage et latence mesurés :
Symptôme de panne connu et intervalle de récurrence :
Couverture des sauvegardes et preuve de restauration réussie :
Architecture choisie et raison :
Fenêtre d’interruption autorisée et objectif de reprise :
Procédure de bascule et de retour des données après bascule :
Tests d’acceptation et période d’observation :
Condition nécessitant une nouvelle révision de l’architecture :
```

**Choisissez délibérément l’imbrication LXC** lorsque ses avantages justifient le travail d’intégration et que vous avez testé la reprise. Choisissez une VM si un environnement Docker invité classique et un noyau invité distinct simplifient l’exploitation du service. Aucune de ces décisions ne remplace les sauvegardes, la surveillance et la maintenance de l’hôte.

## Valider le changement avant la migration

Traitez la migration comme un **changement contrôlé**, pas comme la preuve de la cause de l’incident d’origine. Avant la bascule, consignez la configuration du conteneur, les empreintes des images, les chemins de montage lié, les clés d’environnement, les mappages de périphériques et la dernière restauration réussie. Après la bascule, comparez les mêmes contrôles de service et mesures de ressources. Gardez l’ancienne charge arrêtée jusqu’à ce que la nouvelle copie passe sa période d’acceptation.

Si l’incident revient après la migration, comparez le noyau hôte, le stockage, la pression mémoire, l’accès aux périphériques et les versions de Docker des deux déploiements. Cette comparaison resserre l’enquête. Une migration réussie ne devient pas une expérience causale si les variables pertinentes n’ont pas été contrôlées.

## Étapes suivantes

**Inventoriez d’abord un service.** Repérez ses données persistantes, ses dépendances physiques, les symptômes de panne et l’objectif de reprise. Répétez une restauration avant de décider si une migration est nécessaire.

Pour les **sujets connexes**, consultez le [guide de mise à niveau Proxmox VE](/articles/proxmox-ve-8-to-9-upgrade-guide/) pour planifier les mises à niveau et le [guide de sécurité Docker et Kubernetes](/articles/how-to-secure-your-docker-and-kubernetes-environment/) pour renforcer la sécurité des charges. Gardez le choix d’architecture, l’exécution des mises à niveau et le diagnostic d’incident comme des décisions distinctes, étayées par leurs propres éléments.

## Sources et éléments de preuve

**Recherche vérifiée :** 16 septembre 2026. La transcription fournie a servi à définir le sujet. Les métadonnées vidéo, le rapport d’incident d’origine, l’issue amont et la documentation officielle ont été vérifiés séparément. Les exercices illustratifs et les étapes de validation proposées sont signalés dans le texte.

| Source | Rôle |
|---|---|
| **[Vidéo source](https://www.youtube.com/watch?v=XyPBHhZg0Ok)** | Présentation initiale et durée de stabilité signalée |
| **[Discussion de l’incident Proxmox](https://forum.proxmox.com/threads/pve-host-freezes-every-2-3-weeks.185009/)** | Observations de première main et suivi de migration |
| **[Boîte à outils de conteneurs Proxmox](https://github.com/proxmox/pve-docs/blob/master/pct.adoc)** | Architecture des conteneurs et distinction OCI actuelle |
| **[problème runc 4968](https://github.com/opencontainers/runc/issues/4968)** | Échec de démarrage documenté et correctif historique de paquet |
| **[demande de modification LXC 4609](https://github.com/lxc/lxc/pull/4609)** | Modification AppArmor amont fusionnée |
| **[Documentation Docker](https://docs.docker.com/engine/install/debian/)** | Base d’installation de l’invité, avec les références au runtime et au stockage ci-dessus |
| **[Documentation Linux PSI](https://docs.kernel.org/accounting/psi.html)** | Interprétation de la pression sur les ressources |
| **[Documentation Linux watchdog](https://docs.kernel.org/admin-guide/lockup-watchdogs.html)** | Conditions de blocage définies par le noyau |
| **[Documentation des sauvegardes Proxmox](https://github.com/proxmox/pve-docs/blob/master/vzdump.adoc)** | Exclusions des montages de conteneurs et comportement des sauvegardes |
