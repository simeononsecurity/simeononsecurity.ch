---
title: "Maîtriser PowerCLI pour administrer vSphere"
date: 2023-08-02
lastmod: 2026-11-12
toc: true
draft: false
description: "Apprenez à utiliser PowerCLI pour administrer VMware vSphere, automatiser les tâches et gagner en productivité."
genre: ["Technologie", "Virtualisation", "VMware", "Gestion informatique", "Automatisation", "Interface en ligne de commande", "Scripting", "Administration système", "Cloud", "Gestion de centre de données"]
tags: ["PowerCLI", "VMware PowerCLI", "Installation de PowerCLI", "Installer PowerCLI", "Télécharger PowerCLI", "Téléchargement PowerCLI", "Connexion PowerCLI à vCenter", "Gestion vSphere", "Gestion des machines virtuelles", "Gestion des hôtes", "Automatisation", "Scripting", "Virtualisation", "Serveur vCenter", "Hôtes ESXi", "Gestion des banques de données", "Gestion des cartes réseau", "Création de machines virtuelles", "Suppression de machines virtuelles", "Paramètres des machines virtuelles", "Ressources des hôtes", "Allocation CPU", "Allocation mémoire", "Paramètres de stockage", "Exemples PowerCLI", "Documentation PowerCLI", "Gestion informatique", "Administration système", "Cloud"]
cover: "/img/cover/An_illustrated_cartoon_image_showcasing_a_pers.webp"
coverAlt: "Illustration d’une personne qui utilise les commandes PowerCLI pour gérer des machines virtuelles et des hôtes dans un environnement vSphere."
coverCaption: "Améliorez la gestion de vSphere avec PowerCLI"
---

## Introduction

**PowerCLI** est un outil d’**interface en ligne de commande (CLI)** fourni par **VMware**. Il aide les administrateurs à **gérer et automatiser** leurs environnements **VMware vSphere**. Ses nombreux **cmdlets** simplifient les tâches administratives, que vous débutiez ou soyez expérimenté. Cet article présente l’installation, la connexion à vCenter et l’utilisation efficace de PowerCLI.

______

## Installer PowerCLI

Pour commencer, installez PowerCLI sur votre ordinateur :

1. **Téléchargez** l’installateur depuis le site officiel VMware. Le lien figure dans la [documentation PowerCLI](https://code.vmware.com/web/dp/tool/vmware-powercli). Choisissez la version adaptée à votre système.
2. **Lancez** l’installateur et suivez les instructions à l’écran. Choisissez l’emplacement et les options souhaités.
3. Cliquez sur « Finish » pour terminer. PowerCLI est prêt à l’emploi.

______

## Se connecter à vCenter avec PowerCLI

Après l’installation, connectez-vous à votre serveur vCenter pour gérer l’infrastructure virtuelle avec les cmdlets PowerCLI.

1. Ouvrez PowerCLI depuis le menu Démarrer ou le raccourci du bureau.
2. Connectez-vous à vCenter avec cette commande :

```powershell
Connect-VIServer -Server <vCenter IP or hostname>
```

Remplacez `<vCenter IP or hostname>` par l’adresse IP ou le nom d’hôte de votre serveur vCenter.

3. À l’invite, entrez les identifiants d’un compte ayant les privilèges nécessaires pour administrer vCenter.
4. Vérifiez la connexion avec une commande comme **Get-VMHost**. Si la liste des hôtes ESXi s’affiche, la connexion a réussi.

______

## Utiliser PowerCLI pour gérer vSphere

Une fois connecté, vous pouvez effectuer des tâches courantes.

### Récupérer des informations

PowerCLI fournit des cmdlets pour consulter l’environnement vSphere :

- **Get-VM** : récupère les informations sur les machines virtuelles.
- **Get-VMHost** : récupère les informations sur les hôtes ESXi.
- **Get-Datastore** : récupère les informations sur les banques de données.
- **Get-NetworkAdapter** : récupère les informations sur les cartes réseau.

Utilisez des paramètres pour filtrer et formater les résultats.

### Automatiser des tâches

PowerCLI automatise les tâches répétitives. Quelques lignes de code peuvent exécuter des opérations complexes sur plusieurs objets.

#### Créer un instantané de toutes les VM d’un dossier

```PowerShell
## Power off all virtual machines on a specific host
Get-VMHost -Name "MyHost" | Get-VM | Stop-VM

## Take a snapshot of all virtual machines in a specific folder
Get-Folder -Name "MyFolder" | Get-VM | New-Snapshot -Name "DailySnapshot" -Description "Daily Backup"
```

Ce script montre comment arrêter les VM d’un hôte précis et créer un instantané pour les VM d’un dossier avec PowerCLI.

#### Arrêter toutes les VM d’un dossier en toute sécurité

```PowerShell
## Retrieve the folder containing the virtual machines to be shutdown
$folder = Get-Folder -Name "MyFolder"

## Retrieve all virtual machines within the specified folder
$vms = Get-VM -Location $folder

## Shutdown all virtual machines gracefully
foreach ($vm in $vms) {
    if ($vm.PowerState -eq "PoweredOn") {
        $vm | Shutdown-VMGuest -Confirm:$false
    }
}
```

Ce script arrête correctement toutes les VM du dossier. `Get-Folder` trouve le dossier, puis `Get-VM` en récupère les machines. La boucle `foreach` examine chaque VM. Si son état est « PoweredOn », `Shutdown-VMGuest` lance l’arrêt propre et `-Confirm:$false` supprime l’invite de confirmation.

Cette méthode assure l’arrêt ordonné des machines virtuelles du dossier. Les scripts PowerCLI permettent de créer des automatisations adaptées à vos besoins.

### Gérer les machines virtuelles et les hôtes

PowerCLI permet diverses opérations de gestion :

- **Créer et supprimer des machines virtuelles** : utilisez **`New-VM`** et **`Remove-VM`**. Le cmdlet **[cmdlet New-VM](https://developer.vmware.com/docs/powercli/latest/vmware.vimautomation.core/commands/new-vm/#DefaultParameterSet)** accepte des paramètres de processeur, mémoire, disque et réseau lors de la création.
- **Modifier les paramètres des VM** : changez le processeur, la mémoire, le disque et le réseau. **[cmdlet Set-VM](https://developer.vmware.com/docs/powercli/latest/vmware.vimautomation.core/commands/set-vm/#DefaultSet)** modifie notamment l’allocation CPU et mémoire.
- **Gérer les ressources des hôtes** : administrez processeur, mémoire, réseau et stockage. **[cmdlet Set-VMHost](https://vdc-repo.vmware.com/vmwb-repository/dcr-public/e7c1a32c-a3c6-4d7c-91bb-18a86a38daf7/12353298-ce6e-4d3f-bd8d-ab9f5ab044cc/doc/Set-VMHost.html)** modifie la configuration réseau et stockage de l’hôte.

Ce ne sont que quelques exemples. Le vaste ensemble de cmdlets PowerCLI aide à automatiser et simplifier les tâches d’administration vSphere.

## Conclusion

**PowerCLI** est un outil utile pour gérer et automatiser VMware vSphere. Ses cmdlets simplifient l’administration et améliorent la productivité. Après l’installation et la connexion à vCenter, vous pouvez consulter des informations, automatiser des tâches et gérer efficacement les machines virtuelles et les hôtes.

Explorez PowerCLI pour simplifier la gestion de vSphere.


## Références
- [Documentation PowerCLI](https://code.vmware.com/web/dp/tool/vmware-powercli)
- [Connect-VIServer : référence du cmdlet VMware PowerCLI](https://docs.vmware.com/en/VMware-PowerCLI/latest/VMware.VimAutomation.Core/Connect-VIServer.html)
- [Get-VM : référence du cmdlet VMware PowerCLI](https://developer.vmware.com/docs/powercli/latest/vmware.vimautomation.core/commands/get-vm/#Default)
