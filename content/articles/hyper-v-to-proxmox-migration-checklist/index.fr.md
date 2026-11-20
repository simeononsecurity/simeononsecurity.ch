---
title: "Migrer une VM Hyper-V vers Proxmox VE : liste de contrôle réversible"
date: 2026-10-11
lastmod: 2026-11-19
toc: true
draft: false
description: "Migrez une machine virtuelle Hyper-V vers Proxmox VE avec une exportation source arrêtée, un firmware adapté, l’importation des disques, un démarrage de test isolé et un plan de retour arrière."
genre: ["Virtualisation", "Administration système", "Laboratoire à domicile"]
tags: ["Migration de Hyper-V vers Proxmox", "Migration Hyper-V", "Migration vers Proxmox VE", "Importation VHDX", "qm disk import", "Bascule de VM", "Export Hyper-V", "VM Windows sur Proxmox", "VirtIO sur Proxmox", "Retour arrière VM", "Migration UEFI", "Points de contrôle Hyper-V", "TPM virtuel", "Récupération BitLocker", "Migration de laboratoire à domicile"]
cover: "/img/cover/hyper-v-to-proxmox-migration-checklist.webp"
coverAlt: "Un disque traverse un pont entre une baie serveur bleue et une baie orange. Un chemin de retour séparé et un bouclier signalent la cible."
coverCaption: "Conservez la VM source jusqu’à la réussite des vérifications de bascule du nouvel invité."
---

Un **export Hyper-V** conserve les fichiers d’une machine virtuelle, tandis que Proxmox VE nécessite une nouvelle configuration d’invité et des fichiers de disques virtuels VHDX importés. Une copie réussie ne prouve pas que l’invité démarrera ou fournira ses services. Cette liste fait passer une VM par un export avec la source arrêtée, un test de démarrage contrôlé et une bascule assortie d’un chemin de retour clair.

<!--more-->

## Points clés

- **Inventoriez la source :** consignez la génération du firmware, les chemins des disques, les points de contrôle, le réseau et le chiffrement avant l’export.
- **Arrêtez les écritures :** éteignez la VM Hyper-V avant l’export final et laissez-la arrêtée pendant le test sur Proxmox.
- **Reproduisez le mode de démarrage :** Hyper-V Generation 1 utilise un BIOS hérité. Generation 2 utilise UEFI.
- **Validez le service :** vérifiez les données, l’accès réseau, les sauvegardes et l’état de l’invité avant de retirer la source.

## Avant de commencer

Planifiez une fenêtre de maintenance et testez d’abord la procédure sur une VM jetable. Vous avez besoin d’un accès administrateur à Hyper-V et à Proxmox VE, d’un stockage pour l’export et d’une sauvegarde vérifiée, distincte de la copie de migration. Prévoyez le temps nécessaire au transfert de chaque disque virtuel et au test de l’application invitée. La taille des disques et le débit de transfert déterminent la durée d’interruption.

Cette procédure couvre une VM classique avec des disques virtuels. **Les VM protégées, les disques en accès direct, les disques partagés, les charges en cluster et les licences liées au matériel** exigent un plan adapté à la charge. Déterminez qui autorise la bascule et fixez l’heure limite de retour arrière. Ne démarrez pas les deux copies sur le réseau de production avec la même identité machine.

| Détail de la source | Pourquoi le relever |
|---|---|
| **Génération et firmware de la VM** | Choisir SeaBIOS ou OVMF dans Proxmox |
| **État et modèle de Secure Boot** | Reproduire la politique de démarrage et inscrire des clés compatibles |
| **Disques de démarrage et de données** | Importer chaque fichier VHDX nécessaire dans le bon ordre |
| **Points de contrôle et fichiers AVHDX** | Ne pas traiter un disque différentiel comme un disque de base autonome |
| **IP, DNS, MAC et VLAN** | Rétablir l’accès sans dupliquer une identité |
| **vTPM et BitLocker** | Préparer la récupération avant de modifier le matériel virtuel |
| **Services et contrôles des données** | Définir les preuves de réussite et de retour arrière |

Generation 1 utilise un BIOS hérité. Generation 2 utilise l’interface micrologicielle extensible unifiée (UEFI). Un **fichier AVHDX** est un disque différentiel Hyper-V lié à un VHDX de base. Un **vTPM** est un module de plateforme sécurisée virtuel utilisé par BitLocker et d’autres fonctions de sécurité. Un **VLAN** est un réseau logique distinct transporté sur du matériel réseau partagé.

**SeaBIOS** fournit un firmware de type BIOS hérité. **OVMF** fournit un firmware UEFI. **VirtIO** est une interface rapide pour périphériques virtuels qui nécessite des pilotes dans l’invité. Un **initramfs** est le système de fichiers initial de Linux qui charge les pilotes avant le démarrage du système principal.

## Faire l’inventaire de la machine virtuelle hébergée par Hyper-V

Exécutez ces commandes en lecture seule dans une session PowerShell élevée sur l’hôte Hyper-V. Ce sont des exemples non testés. Vérifiez chaque commande avec le module Hyper-V installé et votre procédure de changement. Saisissez le nom de la VM à l’invite :

```powershell
$vmName = Read-Host "Nom de la VM Hyper-V"
Get-VM -Name $vmName | Select-Object Name, State, Generation, ProcessorCount, MemoryAssigned
Get-VMHardDiskDrive -VMName $vmName | Select-Object ControllerType, ControllerNumber, ControllerLocation, Path
Get-VMSnapshot -VMName $vmName | Select-Object Name, CreationTime
Get-VMNetworkAdapter -VMName $vmName | Select-Object Name, SwitchName, MacAddress
```

Le [module PowerShell Hyper-V](https://learn.microsoft.com/en-us/powershell/module/hyper-v/) documente ces commandes d’inventaire. Comparez les chemins des disques aux paramètres de la VM. Relevez toute image ISO, tout disque de données, commutateur virtuel, adresse statique ou réservation DHCP associé. Notez le système d’exploitation invité et les versions des applications. Vérifiez la sauvegarde en restaurant une copie de test ou en examinant un résultat récent et documenté de restauration. Une copie de fichiers sans test de restauration apporte moins de garanties.

Pour une VM **Generation 2**, consignez aussi le firmware et les paramètres de sécurité :

```powershell
Get-VMFirmware -VMName $vmName | Format-List *
Get-VMSecurity -VMName $vmName | Format-List *
```

Notez l’état de **Secure Boot**, le modèle et le paramètre vTPM. La référence Microsoft de [**`Get-VMFirmware`**](https://learn.microsoft.com/en-us/powershell/module/hyper-v/get-vmfirmware) limite cette commande à Generation 2. [**`Get-VMSecurity`**](https://learn.microsoft.com/en-us/powershell/module/hyper-v/get-vmsecurity) affiche la configuration de sécurité de la VM. N’exécutez pas **`Get-VMFirmware`** sur un invité Generation 1. Une **adresse MAC** identifie une interface réseau. **DNS** associe les noms aux adresses. **DHCP** attribue les paramètres réseau. Un **disque EFI** stocke les paramètres UEFI.

**Résolvez les points de contrôle avant l’export final.** Microsoft indique qu’un export Hyper-V rassemble aussi les fichiers de points de contrôle et les disques VHDX. La suppression d’un point de contrôle depuis Hyper-V fusionne son disque différentiel. Ne supprimez jamais un fichier **`.avhdx`** dans le système de fichiers pour effacer un point de contrôle. Si une fusion échoue ou si la chaîne de disques semble incomplète, arrêtez-vous et suivez les [instructions Microsoft de récupération des points de contrôle](https://learn.microsoft.com/en-us/troubleshoot/windows-server/virtualization/hyper-v-snapshots-checkpoints-differencing-disks). Le [guide Microsoft des points de contrôle](https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/checkpoints) décrit leur suppression et fusion normales.

Pour un invité Windows avec **BitLocker** ou un **vTPM**, obtenez et vérifiez la clé de récupération avant de modifier le matériel virtuel. La [documentation de sécurité Hyper-V Generation 2](https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/generation-2-virtual-machine-security-features) décrit le chiffrement adossé au vTPM. La [FAQ BitLocker de Microsoft](https://learn.microsoft.com/en-us/windows/security/information-protection/bitlocker/bitlocker-key-management-faq) explique pourquoi une modification du démarrage déclenche la récupération. Un nouveau périphérique TPM Proxmox ne reproduit pas l’ancien état du TPM. Conservez la clé hors de la VM exportée.

## Exporter une VM arrêtée

Arrêtez proprement l’invité. Vérifiez que Hyper-V affiche **Off** (arrêtée), et non Saved (enregistrée). Attendez la fin de toute fusion de point de contrôle, puis exportez la VM vers un emplacement disposant d’assez d’espace libre. Dans Hyper-V Manager, cliquez avec le bouton droit sur la VM, choisissez **Export** (exporter), puis sélectionnez la destination. L’équivalent PowerShell est :

```powershell
$vmName = Read-Host "Nom de la VM Hyper-V arrêtée"
$exportPath = Read-Host "Répertoire de destination de l’export"
$vm = Get-VM -Name $vmName -ErrorAction Stop
if ($vm.State -ne 'Off') { throw "Arrêtez la VM et attendez que Hyper-V affiche Off (arrêtée) avant l’export." }
Export-VM -Name $vmName -Path $exportPath
```

Le [guide d’export Microsoft](https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/deploy/export-and-import-virtual-machines) indique qu’un export contient les disques virtuels, la configuration et les fichiers de points de contrôle. La référence de [**`Export-VM`**](https://learn.microsoft.com/en-us/powershell/module/hyper-v/export-vm) définit la commande. Vérifiez la présence et la taille des fichiers attendus à destination. Conservez la VM source arrêtée et sa sauvegarde indépendante. **Ne modifiez pas les fichiers exportés pendant leur importation.**

Transférez les fichiers VHDX vers un chemin accessible depuis l’hôte Proxmox. Traitez l’export comme des données sensibles de l’invité. Utilisez un transport chiffré, limitez l’accès à l’emplacement de transfert et au stockage cible, puis supprimez les copies temporaires après validation. Vérifiez la capacité disponible sur la zone de transfert et le stockage cible. Conservez un export intact pour le retour arrière. Si l’export contient des fichiers **`.avhdx`**, ne choisissez pas un **`.vhdx`** de base par son nom en supposant qu’il contient les dernières écritures. Résolvez la chaîne de disques dans Hyper-V avant de continuer.

## Préparer la machine virtuelle cible dans Proxmox

Créez une nouvelle VM dans l’interface Web Proxmox avec le type de système d’exploitation invité, le processeur et la mémoire relevés auparavant. Choisissez un nouvel ID de VM inutilisé. N’installez pas un nouveau système d’exploitation. Retirez le disque vide créé par l’assistant avant d’importer le disque source. Laissez l’adaptateur réseau déconnecté du pont de production pour le premier démarrage, ou connectez-le à un réseau de test isolé.

| Source Hyper-V | Cible Proxmox |
|---|---|
| **Generation 1, BIOS hérité** | SeaBIOS |
| **Generation 2, UEFI** | OVMF avec disque EFI et politique Secure Boot correspondante |
| **Disque de démarrage Windows sans pilote de stockage VirtIO** | Connexion initiale en SATA |
| **Windows avec vTPM ou BitLocker** | Nouveau périphérique d’état TPM si nécessaire, clé de récupération prête avant le premier démarrage |

Le [guide Microsoft des générations de VM](https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/plan/Should-I-create-a-generation-1-or-2-virtual-machine-in-Hyper-V) associe Generation 1 au BIOS hérité et Generation 2 à UEFI. La [documentation VM Proxmox](https://github.com/proxmox/pve-docs/blob/master/qm.adoc) décrit SeaBIOS, OVMF et le disque EFI qui conserve les paramètres UEFI. **Reproduisez le mode de démarrage de la source.** Le modifier pendant la migration crée un autre problème à diagnostiquer.

Pour une source Generation 2, reproduisez l’état activé ou non de **Secure Boot**. Vérifiez le modèle source et choisissez des clés inscrites compatibles avec l’invité. Les noms de modèles Hyper-V ne sont pas transférés vers Proxmox. Le disque EFI Proxmox de 4 Mo et l’option **Pre-Enroll keys** (inscription préalable des clés) fournissent des clés Secure Boot et activent Secure Boot par défaut. Vérifiez le démarrage cible avant la bascule. La [référence du firmware Microsoft](https://learn.microsoft.com/en-us/powershell/module/hyper-v/set-vmfirmware) décrit l’exigence de modèle source. La [documentation Proxmox du disque EFI](https://github.com/proxmox/pve-docs/blob/master/qm.adoc) décrit les clés cibles.

Avant de modifier les clés EFI, vérifiez que la clé de récupération est déposée dans un emplacement sécurisé et notez les ID des protecteurs actuels. Suivez la documentation installée de Proxmox VE et d’OVMF pour inscrire les clés EFI. Vérifiez de nouveau la clé de récupération et exécutez `manage-bde -status` avant le premier démarrage. Ne suspendez, désactivez ou supprimez pas les protecteurs comme étape générique de migration. Notez la version du paquet firmware, l’état et la version du firmware Secure Boot, ainsi que l’état BitLocker.

Si la source utilise un **vTPM**, ajoutez **TPM State** (état du TPM) dans le panneau Hardware (matériel) de Proxmox avant le premier démarrage. Choisissez la **version 2.0**, sauf exigence documentée de l’invité pour la version 1.2. Cela crée un nouvel état TPM, et non une copie du vTPM Hyper-V. Un invité BitLocker nécessite sa clé de récupération vérifiée au premier démarrage. La [documentation TPM de Proxmox](https://github.com/proxmox/pve-docs/blob/master/qm.adoc) décrit l’action Hardware (matériel) et les versions disponibles.

Pour Windows, démarrez avec un disque de démarrage SATA, sauf si l’invité dispose déjà du pilote de stockage VirtIO requis. Après un démarrage réussi, installez les pilotes VirtIO pris en charge et ne changez qu’un périphérique virtuel à la fois. Proxmox recommande VirtIO SCSI pour ses performances, mais sans pilote de démarrage Windows ne peut pas accéder à son disque système. Pour Linux, vérifiez que l’initramfs comprend le pilote de stockage cible avant de changer de bus. La [documentation VM Proxmox](https://github.com/proxmox/pve-docs/blob/master/qm.adoc) décrit les contrôleurs de disque.

## Importer et connecter les disques

Sur l’hôte Proxmox, vérifiez le chemin du VHDX copié. La commande suivante illustre un import pour l’ID de VM **230** dans un stockage dont l’ID est **`local-lvm`**. Remplacez ces trois valeurs par les vôtres :

```bash
qm disk import 230 /path/to/exported/boot.vhdx local-lvm
```

La référence Proxmox [**`qm disk import`**](https://github.com/proxmox/pve-docs/blob/master/generated/qm.1-synopsis.adoc) indique que l’image source est importée comme **disque inutilisé**. La [documentation des images QEMU](https://www.qemu.org/docs/master/system/images) cite VHDX parmi les formats de conversion pris en charge. Importez chaque disque de données supplémentaire séparément. Attendez la fin de chaque tâche et comparez les tailles importées à l’inventaire source.

Dans le panneau **Hardware** (matériel) de la VM, connectez le disque de démarrage inutilisé en **SATA** pour le premier démarrage Windows. Connectez les disques de données dans l’ordre documenté. Dans **Options > Boot Order** (options > ordre de démarrage), choisissez le disque de démarrage. Pour un invité Generation 2, vérifiez **OVMF** et le disque EFI. Laissez les fichiers d’import et la VM source intacts jusqu’à la réussite de la validation.

## Tester avant la bascule

Démarrez l’invité Proxmox sur le réseau isolé. Utilisez la console pour vérifier l’écran de démarrage, la connexion au système d’exploitation, les volumes, les données applicatives et les journaux des services. Un écran de connexion seul ne prouve pas la réussite de la migration. Reprenez les contrôles définis avant l’export, y compris une transaction représentative ou la lecture de données récentes.

Pour un invité BitLocker, déverrouillez-le avec la clé de récupération si nécessaire. Après le démarrage de Windows, vérifiez l’état de protection du volume système et ses protecteurs depuis une invite élevée :

```powershell
manage-bde -status C:
manage-bde -protectors -get C:
```

Le [guide opérationnel BitLocker de Microsoft](https://learn.microsoft.com/en-us/windows/security/operating-system-security/data-protection/bitlocker/operations-guide) décrit l’inspection des protecteurs et la sauvegarde de la clé de récupération. La sortie contient des données de récupération sensibles. Ne la collez pas dans un ticket ou un journal public. Vérifiez le protecteur voulu et consignez une méthode de récupération actuelle conformément à votre politique. Redémarrez l’invité et confirmez qu’il démarre sans nouvelle demande de récupération avant la bascule. Une demande répétée signifie que le contrôle de migration a échoué, pas qu’il faut abandonner la clé d’origine.

| Essai | Condition de réussite |
|---|---|
| **Démarrage et disques** | L’invité démarre et tous les volumes attendus sont montés |
| **Secure Boot et BitLocker** | La politique de démarrage prévue est respectée et l’invité chiffré redémarre sans répétition de récupération |
| **Application** | Une lecture ou une transaction représentative réussit |
| **Réseau** | Les pairs nécessaires atteignent l’invité de test sur les ports prévus |
| **Récupération** | La sauvegarde Proxmox et le test de restauration isolée réussissent avant le retrait de la source |
| **Exploitation** | La supervision, la synchronisation horaire, l’arrêt et l’agent invité fonctionnent comme prévu |

Lorsque les tests applicatifs réussissent, basculez le chemin ou l’adresse du réseau de production pendant la fenêtre de maintenance. Gardez Hyper-V éteint. Une carte réseau virtuelle différente peut nécessiter une nouvelle réservation DHCP ou une adresse statique corrigée dans l’invité. Depuis un client distinct, vérifiez DNS, règles de pare-feu et services dépendants. La [documentation VM Proxmox](https://github.com/proxmox/pve-docs/blob/master/qm.adoc) décrit les périphériques réseau et les options de l’agent invité.

## Dépanner et revenir en arrière

| Symptôme | Première vérification |
|---|---|
| **Aucun périphérique de démarrage** | Ordre de démarrage, disque de démarrage importé, mode BIOS ou UEFI et clés Secure Boot |
| **Erreur de stockage Windows** | Connexion SATA et pilote de stockage VirtIO absent |
| **Demande BitLocker répétée** | Nouvel état TPM, politique Secure Boot, mesures de démarrage et protecteurs |
| **L’invité démarre sans réseau** | Nouvelle carte réseau virtuelle, pont, VLAN, réservation DHCP et adresse statique |
| **Données anciennes ou manquantes** | Mauvais VHDX, export incomplet, chaîne de points de contrôle ou disque de données manquant |

Si un test obligatoire échoue avant la date limite de retour arrière, arrêtez la VM Proxmox et déconnectez son réseau de production. Rétablissez le chemin réseau source, puis démarrez la VM Hyper-V d’origine. **N’exécutez jamais les deux copies avec la même identité de production.** Relevez les écritures acceptées par la copie Proxmox avant le retour à Hyper-V. Elles exigent une récupération ou une réconciliation distincte, car elles ne figurent pas sur le disque source.

Conservez la VM source et l’export jusqu’à ce que l’invité Proxmox ait passé les tests de service, une nouvelle sauvegarde, un test de restauration isolée et une période d’observation convenue. La [comparaison de virtualisation du site](/articles/vmware-esxi-citrix-xenserver-hyper-v-comparison/) aide au choix de plateforme. Le [Guide de mise à niveau Proxmox VE 8 vers 9 : mise à niveau sur place avec script automatisé](/articles/proxmox-ve-8-to-9-upgrade-guide/) couvre une opération de maintenance ultérieure. **La migration est terminée lorsque la charge et son chemin de récupération fonctionnent sur le nouvel hôte, pas à la fin de l’import du disque.**

## Étapes suivantes

Conservez la VM source et l’export jusqu’à la réussite des contrôles de la charge, des sauvegardes et du retour arrière pendant la période d’observation convenue. Consultez le [test de restauration des sauvegardes VM Proxmox](/articles/proxmox-vm-backup-restore-drill/) avant de retirer la source.
