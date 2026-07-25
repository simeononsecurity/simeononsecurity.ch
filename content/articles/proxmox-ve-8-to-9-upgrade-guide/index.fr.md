---
title: "Guide de mise à niveau Proxmox VE 8 vers 9 : mise à niveau sur place avec script automatisé"
date: 2026-07-22
lastmod: 2026-07-22
toc: true
draft: false
description: "Guide complet pour mettre à niveau Proxmox VE 8 (Debian Bookworm) vers Proxmox VE 9 (Debian Trixie). Couvre les prérequis, la mise à niveau manuelle étape par étape, le script d'automatisation pve8to9-upgrade.sh, les changements majeurs et les problèmes connus."
genre: ["Virtualisation", "Administration Linux", "Proxmox", "Gestion de serveurs", "Open Source", "Homelab"]
tags: ["Proxmox VE 9", "mise à niveau Proxmox", "PVE 8 vers 9", "Debian Trixie", "Debian 13", "apt dist-upgrade", "pve8to9", "Proxmox Ceph", "proxmox-boot-tool", "grub-efi", "mise à niveau LVM", "mise à niveau ZFS", "NVIDIA vGPU", "cgroupv2", "automatisation Proxmox", "script bash de mise à niveau", "mise à niveau cluster Proxmox", "mise à niveau sur place", "pve8to9-upgrade.sh", "Proxmox VE 9.0"]
cover: "/img/cover/proxmox-ve-8-to-9-upgrade-guide-automation.webp"
coverAlt: "Une salle de serveurs moderne avec des icônes lumineuses représentant des machines virtuelles sur des écrans. Un technicien travaille sur un ordinateur portable, entouré d'équipements bleu marine avec des accents bleus, verts et violets."
coverCaption: "Mise à niveau de Proxmox VE 8 vers 9 : mise à niveau sur place étape par étape avec un script assistant automatisé."
canonical: "https://simeononsecurity.com/articles/proxmox-ve-8-to-9-upgrade-guide/"
---

**Proxmox VE 9 est basé sur Debian 13 Trixie et est livré avec le noyau 6.14, QEMU 10, LXC 6 et ZFS 2.3.** Ce guide couvre à la fois le chemin de mise à niveau manuelle sur place et un script bash automatisé qui détecte votre configuration et gère chaque changement de dépôt, problème connu et vérification préalable.

## Nouveautés de Proxmox VE 9

Proxmox VE 9 (publié en août 2025) est une mise à niveau de version majeure. Modifications clés :

| Composant | PVE 8 | PVE 9 |
|-----------|--------|--------|
| **Base Debian** | Bookworm (12) | Trixie (13) |
| **Noyau par défaut** | 6.8 | 6.14 |
| **QEMU** | 9.x | 10.x |
| **LXC** | 5.x | 6.x |
| **ZFS** | 2.2 | 2.3 |
| **Ceph** | Quincy / Reef / Squid | Squid (requis) / Tentacle (optionnel) |
| **cgroup** | cgroupv2 (v1 encore possible) | cgroupv2 uniquement |

**Nouvelles fonctionnalités majeures dans PVE 9.0+ :**
- Instantanés VM sur LVM à provisionnement épais via des chaînes de volumes (aperçu technique en production dans la version 9.1)
- Règles d'affinité haute disponibilité remplaçant les groupes HA
- SDN Fabrics pour les réseaux Ceph OpenFabric et OSPF full-mesh
- Nouvelle interface web mobile (Rust/Yew)
- Extension de périphérique ZFS RAIDZ sans temps d'arrêt
- Équilibrage de charge dynamique avec le planificateur de ressources cluster (PVE 9.2)
- WireGuard et BGP comme protocoles de fabric SDN (PVE 9.2)
- `/tmp` est maintenant un `tmpfs` (changement Debian Trixie : fichiers nettoyés périodiquement)

______

## Avant de commencer : prérequis

**Vous devez satisfaire tous ces points avant de modifier les dépôts.** Consultez la liste complète des prérequis sur le [wiki officiel de mise à niveau](https://pve.proxmox.com/wiki/Upgrade_from_8_to_9#Prerequisites).

### 1. Proxmox VE 8.4 minimum

```bash
pveversion
```

La sortie doit afficher `pve-manager/8.4.x` ou supérieur. Sinon :

```bash
apt update && apt dist-upgrade
```

### 2. Ceph doit être à Squid (19.x), hyper-convergé uniquement

```bash
ceph --version
```

La sortie doit afficher la version 19.x (Squid). Si vous êtes sur Reef (18.x) ou Quincy (17.x), mettez d'abord à niveau Ceph. Le chemin de mise à niveau se fait toujours étape par étape :

- Quincy (17) → Reef (18) → Squid (19)

*Ne procédez pas à la mise à niveau PVE 9 tant que tous les nœuds Ceph ne sont pas sur Squid.*

### 3. Proxmox Backup Server co-installé

Si PBS est installé sur le même nœud, mettez à niveau PBS 3 → 4 avant de toucher aux dépôts PVE. Exécutez `pbs3to4 --full` et résolvez d'abord tous les problèmes.

### 4. Exigences d'accès

- **Préféré** : accès console via IPMI, iKVM ou clavier physique. La session SSH sera interrompue lors du redémarrage des services.
- **SSH** : utilisez `tmux` ou `screen` pour que la mise à niveau continue si la connexion est interrompue :
  ```bash
  tmux new -s upgrade
  ```

### 5. Espace disque

```bash
df -h /
```

Au moins **5 Go libres**, idéalement 10+ Go.

### 6. Sauvegardes valides

Sauvegardez toutes les VM et conteneurs sur un stockage externe avant de continuer. Testez une restauration. Une sauvegarde valide n'est pas optionnelle.

______

## Changements majeurs que vous devez connaître

Lisez ces points avant la mise à niveau. Plusieurs nécessitent une action avant ou après.

### cgroup V1 est supprimé

PVE 9 ne prend plus du tout en charge l'environnement cgroupv1 hérité. Si vous l'aviez activé précédemment :

```bash
grep -E 'cgroup_no_v1|systemd.unified_cgroup_hierarchy=0' /proc/cmdline
```

Si cela retourne quelque chose, supprimez le paramètre du noyau de `/etc/default/grub` et exécutez `update-grub` avant la mise à niveau.

**Impact sur les conteneurs** : les conteneurs exécutant systemd 230 ou plus ancien (CentOS 7, Ubuntu 16.04) ne démarreront pas sous PVE 9. Migrez ces charges de travail pendant la fenêtre de support PVE 8 (fin de vie juillet 2026).

### Groupes HA dépréciés

Les groupes HA sont remplacés par des règles HA. Ils migrent automatiquement une fois que tous les nœuds du cluster sont sur PVE 9. Aucune action manuelle requise, mais vérifiez après la mise à niveau du dernier nœud.

### Privilège VM.Monitor supprimé

Les rôles personnalisés qui référençaient `VM.Monitor` doivent être mis à jour. Utilisez `Sys.Audit` pour l'accès basique au moniteur KVM à la place. Le script `pve8to9` détecte les rôles affectés.

### Nouveau privilège : VM.Replicate

La création ou la modification de tâches de réplication de stockage nécessite maintenant `VM.Replicate` sur `/vms/<vmid>`. Ajustez les rôles personnalisés si nécessaire.

### Les conteneurs LXC privilégiés nécessitent Sys.Modify

La création de nouveaux conteneurs privilégiés nécessite maintenant `Sys.Modify`. La restauration d'un conteneur privilégié existant sur place ne le nécessite pas.

### systemd-sysctl ne lit plus /etc/sysctl.conf

Tous les paramètres personnalisés dans `/etc/sysctl.conf` seront silencieusement ignorés après la mise à niveau. Migrez-les vers `/etc/sysctl.d/<NN>-name.conf` avant le redémarrage.

```bash
# Vérifier ce qui est dans sysctl.conf
grep -v '^\s*#\|^\s*$' /etc/sysctl.conf
```

### /tmp est maintenant tmpfs

Debian Trixie monte `/tmp` en tant que tmpfs (jusqu'à 50 % de la RAM). Les fichiers sont nettoyés périodiquement pendant que le système fonctionne. Si vous utilisez `/tmp` pour de grands fichiers temporaires, déplacez ce travail vers `/var/tmp` ou un point de montage dédié.

### Veeam Backup défaillant pour la version machine QEMU >= 10.0

Proxmox a modifié la façon dont les disques s'attachent à QEMU en interne pour la version machine 10.0+. Veeam ne s'est pas encore adapté. Fixez les VM affectées à la version machine `9.2+pve1` avant la mise à niveau, ou reportez la mise à niveau si Veeam est critique.

### Les noms d'interface réseau peuvent changer

Le noyau 6.14 reconnaît plus de fonctionnalités NIC que le 6.8. Certaines cartes NIC reçoivent des suffixes de nommage supplémentaires. L'outil `pve-network-interface-pinning` peut fixer toutes les interfaces à des noms `nicX` stables avant la mise à niveau :

```bash
pve-network-interface-pinning --help
```

______

## Option A : mise à niveau manuelle sur place

Suivez les étapes officielles de [pve.proxmox.com/wiki/Upgrade_from_8_to_9](https://pve.proxmox.com/wiki/Upgrade_from_8_to_9).

### Étape 1 : exécutez la liste de contrôle pve8to9

```bash
pve8to9 --full
```

Résolvez chaque élément `FAIL` avant de continuer. Relancez après chaque correction.

### Étape 2 : migrez les VM en cours d'exécution (si dans un cluster)

```bash
qm migrate <vmid> <target-node>
pct migrate <ctid> <target-node>
```

### Étape 3 : mettez à jour PVE 8 entièrement

```bash
apt update && apt dist-upgrade
pveversion   # doit afficher 8.4.1 ou plus récent
```

### Étape 4 : mettez à jour les dépôts de base Debian

```bash
sed -i 's/bookworm/trixie/g' /etc/apt/sources.list
sed -i 's/bookworm/trixie/g' /etc/apt/sources.list.d/pve-enterprise.list
```

Commentez ou supprimez les lignes de dépôt spécifiques à Bookworm restantes.

### Étape 5 : ajoutez le dépôt de paquets PVE 9

**Enterprise (abonnement requis) :**

```bash
cat > /etc/apt/sources.list.d/pve-enterprise.sources << EOF
Types: deb
URIs: https://enterprise.proxmox.com/debian/pve
Suites: trixie
Components: pve-enterprise
Signed-By: /usr/share/keyrings/proxmox-archive-keyring.gpg
EOF
```

**Sans abonnement :**

```bash
cat > /etc/apt/sources.list.d/proxmox.sources << EOF
Types: deb
URIs: http://download.proxmox.com/debian/pve
Suites: trixie
Components: pve-no-subscription
Signed-By: /usr/share/keyrings/proxmox-archive-keyring.gpg
EOF
```

Vérifiez avec `apt update && apt policy` que le nouveau dépôt apparaît sans erreurs. Supprimez ou commentez ensuite l'ancien fichier `.list`.

### Étape 6 : mettez à jour le dépôt Ceph (hyper-convergé uniquement)

```bash
cat > /etc/apt/sources.list.d/ceph.sources << EOF
Types: deb
URIs: https://enterprise.proxmox.com/debian/ceph-squid
Suites: trixie
Components: enterprise
Signed-By: /usr/share/keyrings/proxmox-archive-keyring.gpg
EOF
```

Utilisez `http://download.proxmox.com/debian/ceph-squid` avec `pve-no-subscription` pour les configurations sans abonnement.

### Étape 7 : actualisez l'index des paquets

```bash
apt update
```

Vérifiez l'absence d'erreurs.

### Étape 8 : exécutez le dist-upgrade

```bash
apt dist-upgrade
```

Cela prend 5 à 60+ minutes selon la vitesse du stockage. Pendant la mise à niveau :

- **`/etc/issue`** : gardez votre version actuelle (sûr)
- **`/etc/lvm/lvm.conf`** : installez la version du mainteneur (recommandé)
- **`/etc/ssh/sshd_config`** : installez la version du mainteneur si vous ne l'avez pas personnalisée
- **`/etc/default/grub`** : gardez votre version actuelle si vous l'avez personnalisée
- **`/etc/chrony/chrony.conf`** : installez la version du mainteneur si non personnalisée

### Étape 9 : redémarrez

```bash
reboot
```

Même si le noyau 6.14 était déjà installé comme opt-in sur PVE 8, le redémarrage est nécessaire. Le noyau est reconstruit avec les toolchains PVE 9.

### Étape 10 : étapes post-mise à niveau

```bash
# Vider le cache du navigateur : Ctrl+Maj+R (ou ⌘+Alt+R sur macOS)
# Vérifier tous les nœuds du cluster :
pvesh get /nodes

# Pour les clusters : les groupes HA migrent automatiquement vers les règles HA
# après que tous les nœuds sont sur PVE 9
journalctl -eu pve-ha-crm  # vérifier les erreurs
```

______

## Option B : script automatisé (pve8to9-upgrade.sh)

Le processus manuel comporte de nombreuses étapes conditionnelles qui varient selon la configuration. Le script `pve8to9-upgrade.sh` les automatise toutes.

**Source du script :** [gist.github.com/simeononsecurity/ba3831f487c4e960f9e218c7da5c4b8d](https://gist.github.com/simeononsecurity/ba3831f487c4e960f9e218c7da5c4b8d)

### Ce que fait le script

Le script gère la mise à niveau complète automatiquement, notamment :

| Détection | Action |
|-----------|--------|
| Dépôts enterprise vs. sans abonnement | Utilise le type de dépôt **activement activé**. N'active pas enterprise sur les nœuds sans abonnement. |
| Version Ceph | Bloque si Quincy ou Reef, affiche le guide de mise à niveau Ceph étape par étape |
| Type de dépôt Ceph | Écrit un nouveau `ceph.sources` correspondant à votre type de dépôt actuel |
| Pilote NVIDIA vGPU | Bloque si pilote < 570.158.02 (minimum GRID 18.3) |
| Passthrough GPU NVIDIA | Avertit et génère un rappel de test post-mise à niveau |
| Dépôts CUDA | Met à jour `debian12` → `debian13` dans les chemins URI |
| Méta-paquet systemd-boot | Le supprime (corrige le bogue Debian #1110177 qui interrompt dist-upgrade) |
| Paramètres personnalisés `sysctl.conf` | Migre vers `/etc/sysctl.d/99-pve8to9-migrated.conf` |
| Interblocage FRR post-up | Corrige `/etc/network/interfaces` avant le redémarrage |
| `systemd-journald-audit.socket` | Désactive pour éviter l'inondation des journaux pendant la mise à niveau |
| Problème grub UEFI + LVM | Installe `grub-efi-amd64` et écrit une feuille de triche dans `/root/` |
| Dépôts `bookworm` tiers | Les commente avec un rappel de mise à jour |
| Conflit `linux-image-amd64` | Le supprime si présent |
| Activation automatique LVM | Exécute le script de migration avant et après la mise à niveau |
| Proxmox Backup Server | Exécute la vérification `pbs3to4 --full` ; met à jour les dépôts PBS pour Trixie |
| Racine ZFS | Détecte et confirme (aucune action spéciale requise) |

Toutes les modifications sont entièrement journalisées dans `/var/log/pve8to9-upgrade-<horodatage>.log`.

### Installation et utilisation

```bash
# Télécharger le script
curl -fsSL https://gist.githubusercontent.com/simeononsecurity/ba3831f487c4e960f9e218c7da5c4b8d/raw/pve8to9-upgrade.sh \
  -o pve8to9-upgrade.sh

# Rendre exécutable
chmod +x pve8to9-upgrade.sh

# Vérifiez avant d'exécuter (lisez toujours les scripts avant de les exécuter en tant que root)
less pve8to9-upgrade.sh
```

**Modes d'exécution :**

```bash
# Mode interactif complet (recommandé)
./pve8to9-upgrade.sh

# Approuver automatiquement toutes les corrections sûres et non destructives
./pve8to9-upgrade.sh --yes

# Simulation : afficher chaque modification sans rien appliquer
./pve8to9-upgrade.sh --dry-run

# Ignorer le pré-vol pve8to9 --full (non recommandé)
./pve8to9-upgrade.sh --skip-preflight
```

*Exécutez dans `tmux` ou `screen` si vous vous connectez via SSH.*

### Vérifications de sécurité bloquantes du script

Le script **refusera de continuer** si l'une de ces conditions est vraie :

- cgroup V1 est explicitement activé dans la ligne de commande du noyau
- Ceph est encore à Quincy (17.x) ou Reef (18.x). Le script affiche les commandes exactes de mise à niveau Ceph.
- Le pilote NVIDIA vGPU est inférieur à la version 570 (GRID 18.3)
- La version PVE est inférieure à 8.4

Pour chaque problème bloquant, le script imprime les commandes exactes pour le résoudre avant de relancer.

______

## Problèmes de mise à niveau connus

### GRUB ne démarre pas à partir de LVM en mode UEFI

**Concerné** : systèmes avec racine sur LVM, démarrant en mode UEFI, mis à niveau depuis PVE 7.x

```bash
# Correction (exécuter sur le système en direct après la mise à niveau) :
[ -d /sys/firmware/efi ] && apt install grub-efi-amd64
```

Le script `pve8to9-upgrade.sh` détecte UEFI+LVM et installe cela automatiquement. Il écrit également une feuille de triche de récupération dans `/root/GRUB-RECOVERY-CHEATSHEET.txt`.

**Si le nœud est déjà bloqué** à `grub rescue>` ou "disk 'lvmid/...' not found" :

1. Démarrez l'ISO PVE → Avancé → **Rescue Boot**
2. Ou suivez la [section Recover From Grub Failure — LVM](https://pve.proxmox.com/wiki/Recover_From_Grub_Failure#Recovering_from_grub_.22disk_not_found.22_error_when_booting_from_LVM) sur le wiki officiel

### Le méta-paquet systemd-boot interrompt dist-upgrade

Le méta-paquet `systemd-boot` a été auto-installé sur tous les systèmes ISO PVE 8.1-8.4. Dans Trixie, il contient des hooks qui s'activent lors de la mise à niveau d'autres paquets et peuvent interrompre `dist-upgrade` si l'ESP n'est pas monté (bogue Debian #1110177).

```bash
# Supprimez-le avant dist-upgrade :
apt remove systemd-boot
# Ne supprimez PAS systemd-boot-efi ou systemd-boot-tools. Ceux-ci restent.
```

Le script `pve8to9-upgrade.sh` gère cela automatiquement.

### Passthrough PCI parfois défaillant avec le noyau 6.14

Certains utilisateurs signalent que les VM avec passthrough PCI ne démarrent pas avec le noyau 6.14. Si concerné :

```bash
# Fixer temporairement l'ancien noyau :
proxmox-boot-tool kernel pin 6.8.12-4-pve
```

### Les configurations Ceph full mesh se bloquent au redémarrage

Si votre `/etc/network/interfaces` contient :

```
post-up /usr/bin/systemctl restart frr.service
```

Changez-le en :

```
post-up /usr/bin/systemctl is-active --quiet frr.service && /usr/bin/systemctl restart frr.service || true
```

Faites cela **avant le redémarrage**. Le script détecte et corrige automatiquement ce schéma.

### Le pool LVM Thin nécessite une réparation

Sur certains systèmes après la mise à niveau :

```
Check of pool pve/data failed (status:64). Manual repair required!
```

Correction :

```bash
lvconvert --repair pve/data
```

### Version minimale du pilote NVIDIA vGPU

Doit être au moins le **pilote 570.158.02** (GRID 18.3) avant la mise à niveau. Les pilotes plus anciens sont incompatibles avec le noyau 6.x.

```bash
nvidia-smi --query-gpu=driver_version --format=csv,noheader
```

______

## Ordre de mise à niveau du cluster

Mettez à niveau les nœuds un à la fois. Vérifiez que chaque nœud est en bonne santé avant de commencer le suivant.

```bash
# Vérifier la santé du cluster avant chaque mise à niveau de nœud :
pvecm status
ceph -s   # si Ceph est déployé
```

**Règles de migration lors des mises à niveau partielles :**

- VM/CT de PVE 8 → PVE 9 : fonctionne toujours
- VM/CT de PVE 9 → PVE 8 : généralement non pris en charge

Après que tous les nœuds sont sur PVE 9, les groupes HA migrent automatiquement vers les règles d'affinité HA. Vérifiez les erreurs :

```bash
journalctl -eu pve-ha-crm
```

______

## Dépannage

### La mise à niveau se bloque / "proxmox-ve serait supprimé"

Si vous voyez :
```
W: (pve-apt-hook) You are attempting to remove the meta-package 'proxmox-ve'!
```

Un ou plusieurs paquets ne peuvent pas être mis à niveau car un dépôt Bookworm est encore configuré. Trouvez les entrées Bookworm restantes :

```bash
grep -r 'bookworm' /etc/apt/sources.list /etc/apt/sources.list.d/
```

Commentez-les, puis :

```bash
apt update && apt dist-upgrade
```

Si partiellement terminé :

```bash
apt -f install
```

### Échec du démarrage après la mise à niveau ZFS

Si vous utilisez ZFS root avec un démarrage BIOS hérité, consultez [ZFS: Switch Legacy-Boot to Proxmox Boot Tool](https://pve.proxmox.com/wiki/ZFS:_Switch_Legacy-Boot_to_Proxmox_Boot_Tool). Le `proxmox-boot-tool` doit gérer le démarrage sur les systèmes ZFS, pas GRUB directement, pour survivre aux mises à niveau de fonctionnalités ZFS.

______

## Liste de contrôle post-mise à niveau

Après le redémarrage de chaque nœud :

- [ ] Vider le cache du navigateur (`Ctrl+Maj+R` / `⌘+Alt+R`)
- [ ] `pveversion` affiche 9.x
- [ ] `uname -r` affiche 6.14.x ou plus récent
- [ ] Toutes les VM et CT démarrent correctement
- [ ] Santé Ceph : `ceph -s` affiche HEALTH_OK
- [ ] Si UEFI+LVM : vérifier que le mtime de `grubx64.efi` est récent
- [ ] Si passthrough NVIDIA : tester une VM hors production
- [ ] Mettre à jour les dépôts tiers commentés lors de la mise à niveau
- [ ] Déplacer les paramètres personnalisés de `/etc/sysctl.conf` vers `/etc/sysctl.d/`

______

## Références

1. [Officiel : mise à niveau Proxmox VE de 8 à 9](https://pve.proxmox.com/wiki/Upgrade_from_8_to_9)
2. [Officiel : mise à niveau de 8 à 9 — prérequis](https://pve.proxmox.com/wiki/Upgrade_from_8_to_9#Prerequisites)
3. [Script d'automatisation pve8to9-upgrade.sh](https://gist.github.com/simeononsecurity/ba3831f487c4e960f9e218c7da5c4b8d)
4. [Proxmox VE 9.0 problèmes connus (feuille de route)](https://pve.proxmox.com/wiki/Roadmap#9.0-known-issues)
5. [Récupération après échec de Grub — erreur LVM "disk not found"](https://pve.proxmox.com/wiki/Recover_From_Grub_Failure#Recovering_from_grub_.22disk_not_found.22_error_when_booting_from_LVM)
6. [ZFS : passer du démarrage hérité à Proxmox Boot Tool](https://pve.proxmox.com/wiki/ZFS:_Switch_Legacy-Boot_to_Proxmox_Boot_Tool)
7. [Guide de mise à niveau de Ceph Reef vers Squid](https://pve.proxmox.com/wiki/Ceph_Reef_to_Squid)
8. [Épinglage des interfaces réseau Proxmox](https://pve.proxmox.com/pve-docs/chapter-sysadmin.html)
9. [Notes de version Debian 13 Trixie](https://www.debian.org/releases/trixie/releasenotes)
