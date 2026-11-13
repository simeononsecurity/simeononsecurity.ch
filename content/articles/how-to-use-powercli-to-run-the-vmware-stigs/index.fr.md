---
title: "Maîtriser la sécurité VMware"
date: 2023-08-03
lastmod: 2026-11-13
toc: true
draft: false
description: "Apprenez à utiliser PowerCLI pour appliquer les STIG VMware et sécuriser votre environnement VMware dans ce guide complet."
genre: ["Cybersécurité", "Virtualisation", "Infrastructure informatique", "Automatisation", "PowerShell", "VMware", "STIG", "Conformité", "Scripting", "Centre de données"]
tags: ["PowerCLI", "STIG VMware", "Sécurité VMware", "automatisation", "scripts", "PowerShell", "ESXi", "virtualisation", "conformité", "cybersécurité", "utiliser PowerCLI pour les STIG VMware", "automatiser la sécurité VMware avec PowerCLI", "script PowerCLI pour appliquer les STIG VMware", "automatisation PowerCLI pour la sécurité ESXi", "sécuriser un environnement VMware avec PowerCLI"]
cover: "/img/cover/An_illustration_depicting_a_computer_server_sh.webp"
coverAlt: "Illustration d’un serveur informatique protégé par un cadenas, symbole d’une infrastructure VMware sécurisée."
coverCaption: "Exploiter PowerCLI pour sécuriser votre environnement VMware"
---

**Comment appliquer les STIG VMware avec PowerCLI**

PowerCLI est un outil d’automatisation et de script qui permet de gérer et de configurer des environnements VMware avec PowerShell. Cet article explique comment utiliser PowerCLI pour appliquer le guide STIG VMware (Security Technical Implementation Guide) à ESXi et aux machines virtuelles.

## Introduction

Le **STIG VMware** fournit des consignes et des recommandations pour configurer et administrer une infrastructure VMware de façon sécurisée. Son application aide les organisations à renforcer la sécurité de leurs déploiements VMware et à respecter les exigences gouvernementales applicables, notamment celles des **STIG de la Defense Information Systems Agency (DISA)**.

## Qu’est-ce que PowerCLI ?

**PowerCLI** est une interface en ligne de commande et un outil de script pour administrer les environnements VMware. Il repose sur PowerShell et fournit de nombreuses applets de commande dédiées à l’administration VMware. Les administrateurs s’en servent pour automatiser les tâches répétitives, modifier des configurations et recueillir des informations sur l’infrastructure VMware.

### Installation et prérequis

Avant de commencer avec PowerCLI et les STIG VMware, vérifiez les prérequis suivants :

- [**PowerCLI 11.3**](https://www.powershellgallery.com/packages/VMware.PowerCLI/11.3.0.13990089) : installez PowerCLI depuis PowerShell Gallery avec la commande `Install-Module VMware.PowerCLI -force`.
- [**PowerShell 5 ou version ultérieure**](https://docs.microsoft.com/en-us/skypeforbusiness/set-up-your-computer-for-windows-powershell/download-and-install-windows-powershell-5-1) : vérifiez qu’une version 5 ou ultérieure de PowerShell est installée.
- [**ESXi 6.7 U2 ou version ultérieure**](https://my.vmware.com/web/vmware/downloads/details?downloadGroup=ESXI670&productId=742) : utilisez ESXi 6.7 U2 ou une version ultérieure.

## Automatiser le STIG de VMware VCSA

Le STIG VMware ESXi fournit des consignes pour sécuriser les hôtes ESXi. Automatiser l’application de ses contrôles aide les administrateurs à simplifier le processus et à appliquer une configuration cohérente à plusieurs hôtes.

### Points à examiner

Avant de lancer l’automatisation, tenez compte des points suivants :

- **Vérifiez qu’aucune machine virtuelle ni aucun système invité de l’hôte ou du cluster ESXi n’a besoin des fonctions CD, USB ou lecteur de disquette.**
- **Appliquez les STIG à tous les hôtes ESXi et à toutes les machines invitées associés à vCenter.**
- **Prévoyez des compétences de dépannage pour résoudre les problèmes qui surviennent pendant l’opération.**

### Script : automatiser le STIG VMware VCSA

Le script PowerCLI suivant automatise l’application d’une sélection de contrôles STIG aux VCSA :

```powershell
Set-PowerCLIConfiguration -InvalidCertificateAction Ignore -Confirm:$false
Set-PowerCLIConfiguration -Scope User -ParticipateInCEIP $false -Confirm:$false
$vcenters = 127.0.0.1, 127.0.0.2

#Se connecter à chaque serveur vCenter
ForEach ($vc in $vcenters) {
    Connect-VIServer -Server $vc
}

#Automatisé

Write-Host "ID de vulnérabilité: V-243098 ID de règle: SV-243098r719537_rule ID STIG: VCTR-67-000036"
Write-Host "Si la valeur de 'config.log.level' n'est pas définie sur "info" ou n'existe pas, il s'agit d'une non-conformité."
ForEach ($vc in $vcenters) {
    Get-AdvancedSetting -Entity $vc -Name config.log.level | Set-AdvancedSetting -Value info
    Get-AdvancedSetting -Entity $vc -Name config.log.level
}

Write-Host "ID de vulnérabilité: V-243090 ID de règle: SV-243090r719513_rule ID STIG: VCTR-67-000024"
Write-Host "Si 'config.vpxd.hostPasswordLength' a une valeur autre que "32", il s'agit d'une non-conformité.
Si le paramètre n'existe pas, il n'y a pas de non-conformité."
ForEach ($vc in $vcenters) {
    Get-AdvancedSetting -Entity $vc -Name config.vpxd.hostPasswordLength | Set-AdvancedSetting -Value 32
    Get-AdvancedSetting -Entity $vc -Name config.vpxd.hostPasswordLength
}


Write-Host "ID de vulnérabilité: V-243089 ID de règle: SV-243089r719510_rule ID STIG: VCTR-67-000023"
Write-Host "Si 'VirtualCenter.VimPasswordExpirationInDays' a une valeur autre que "30" ou n'existe pas, il s'agit d'une non-conformité."
ForEach ($vc in $vcenters) {
    Try {
        Get-AdvancedSetting -Entity $vc -Name VirtualCenter.VimPasswordExpirationInDays | Set-AdvancedSetting -Value 30
    }
    Catch {
        New-AdvancedSetting -Entity $vc -Name VirtualCenter.VimPasswordExpirationInDays -Value 30
    }
}

Write-Host "ID de vulnérabilité: V-243084 ID de règle: SV-243085r719498_rule ID STIG: VCTR-67-000016"
Write-Host "Si NetFlow est configuré et que l’adresse IP du collecteur est inconnue ou non documentée, il s’agit d’une non-conformité."
$pgs = Get-VDPortgroup | Get-View
ForEach ($pg in $pgs) {
    $spec = New-Object VMware.Vim.DVPortgroupConfigSpec
    $spec.configversion = $pg.Config.ConfigVersion
    $spec.defaultPortConfig = New-Object VMware.Vim.VMwareDVSPortSetting
    $spec.defaultPortConfig.ipfixEnabled = New-Object VMware.Vim.BoolPolicy
    $spec.defaultPortConfig.ipfixEnabled.inherited = $false
    $spec.defaultPortConfig.ipfixEnabled.value = $false
    $pg.ReconfigureDVPortgroup_Task($spec)
}
Get-VDPortgroup | Select-Object Name, VirtualSwitch, @{N = "NetFlowEnabled"; E = { $_.Extensiondata.Config.defaultPortConfig.ipfixEnabled.Value } }

Write-Host "ID de vulnérabilité: V-243084 ID de règle: SV-243084r719495_rule ID STIG: VCTR-67-000015"
Write-Host "Le serveur vCenter doit définir sur Rejeter la stratégie Promiscuous Mode du groupe de ports distribué."
Get-VDSwitch | Get-VDSecurityPolicy | Set-VDSecurityPolicy -AllowPromiscuous $false
Get-VDPortgroup | Where-Object { $_.IsUplink -eq $false } | Get-VDSecurityPolicy | Set-VDSecurityPolicy -AllowPromiscuous $false
Get-VDSwitch | Get-VDSecurityPolicy
Get-VDPortgroup | Where-Object { $_.IsUplink -eq $false } | Get-VDSecurityPolicy


Write-Host "ID de vulnérabilité: V-243083 ID de règle: SV-243083r719492_rule ID STIG: VCTR-67-000014"
Write-Host "Le serveur vCenter doit définir sur Rejeter la stratégie MAC Address Change du groupe de ports distribué."
Get-VDSwitch | Get-VDSecurityPolicy | Set-VDSecurityPolicy -MacChanges $false
Get-VDPortgroup | Where-Object { $_.IsUplink -eq $false } | Get-VDSecurityPolicy | Set-VDSecurityPolicy -MacChanges $false
Get-VDPortgroup | Where-Object { $_.IsUplink -eq $false } | Get-VDSecurityPolicy

Write-Host "ID de vulnérabilité: V-243082 ID de règle: SV-243082r719489_rule ID STIG: VCTR-67-000013"
Write-Host "Le serveur vCenter doit définir sur Rejeter la stratégie Forged Transmits du groupe de ports distribué."
Get-VDSwitch | Get-VDSecurityPolicy | Set-VDSecurityPolicy -ForgedTransmits $false
Get-VDPortgroup | Where-Object { $_.IsUplink -eq $false } | Get-VDSecurityPolicy | Set-VDSecurityPolicy -ForgedTransmits $false
Get-VDSwitch | Get-VDSecurityPolicy
Get-VDPortgroup | Where-Object { $_.IsUplink -eq $false } | Get-VDSecurityPolicy

Write-Host "ID de vulnérabilité: V-243081 ID de règle: SV-243081r719486_rule ID STIG: VCTR-67-000012"
Write-Host "Le serveur vCenter doit désactiver le contrôle d’intégrité du commutateur virtuel distribué."
Get-View -ViewType DistributedVirtualSwitch | Where-Object { ($_.config.HealthCheckConfig | Where-Object { $_.enable -notmatch "False" }) } | ForEach-Object { $_.UpdateDVSHealthCheckConfig(@((New-Object Vmware.Vim.VMwareDVSVlanMtuHealthCheckConfig -property @{enable = 0 }), (New-Object Vmware.Vim.VMwareDVSTeamingHealthCheckConfig -property @{enable = 0 }))) }
$vds = Get-VDSwitch
$vds.ExtensionData.Config.HealthCheckConfig

Write-Host "ID de vulnérabilité: V-243077 ID de règle: SV-243077r719474_rule ID STIG: VCTR-67-00000"
Write-Host "Le serveur vCenter doit gérer les capacités excédentaires, la bande passante ou toute autre redondance afin de limiter les effets des attaques par saturation et par déni de service (DoS), en activant Network I/O Control (NIOC)."
Write-Host "Si aucune alarme n’est créée et activée pour signaler les défaillances syslog, il s’agit d’une non-conformité."
ForEach ($vdswitch in (Get-VDSwitch.name)){
    (Get-VDSwitch $vdswitch | Get-View).EnableNetworkResourceManagement($true)
}
Get-VDSwitch | Select-Object Name, @{N = "NIOC Enabled"; E = { $_.ExtensionData.config.NetworkResourceManagementEnabled } }

#Vérification manuelle

Write-Host "ID de vulnérabilité: V-243076 ID de règle: SV-243076r719471_rule ID STIG: VCTR-67-000005"
Write-Host "Les utilisateurs du serveur vCenter doivent avoir les rôles appropriés."
Write-Host "Les privilèges requis des comptes de service et des utilisateurs doivent être documentés.
Si un utilisateur ou un compte de service possède plus de privilèges que nécessaire, il s’agit d’une non-conformité."
Get-VIPermission | Sort-Object Role | Select-Object Role, Principal, Entity, Propagate, IsGroup | Format-Table -Auto

Write-Host "ID de vulnérabilité: V-243119 ID de règle: SV-243119r719600_rule ID STIG: VCTR-67-000064"
Write-Host "Si un rôle autre qu’Administrator ou un groupe propre au site possède l’une de ces autorisations, il s’agit d’une non-conformité."
$roles = Get-VIRole
ForEach ($role in $roles) {
    $privileges = $role.PrivilegeList
    If ($privileges -match "Crypto*" -or $privileges -match "Global.Diagnostics" -or $privileges -match "Host.Inventory.Add*" -or $privileges -match "Host.Local operations.Manage user groups") {
        Write-Host "$role possède des privilèges cryptographiques"
    }
}

Write-Host "ID de vulnérabilité: V-243118 ID de règle: SV-243118r719597_rule ID STIG: VCTR-67-000063"
Write-Host "Si des utilisateurs autres que Solution Users ont le rôle « Administrator » sans être explicitement désignés pour des opérations cryptographiques, il s’agit d’une non-conformité."
Get-VIPermission | Where-Object { $_.Role -eq "Admin" } | Select-Object Role, Principal, Entity, Propagate, IsGroup | Format-Table -Auto


Write-Host "ID de vulnérabilité: V-243111 ID de règle: SV-243111r719576_rule ID STIG: VCTR-67-000055"
Write-Host "Sans objet si aucun cluster vSAN n’est activé."
Write-host "Si vSAN est activé et que la banque de données s’appelle 'vsanDatastore', il s’agit d’une non-conformité."
If ($(Get-Cluster | Where-Object { $_.VsanEnabled } | Measure-Object).Count -gt 0) {
    Write-Host "Cluster vSAN activé détecté"
    $Clusters = Get-Cluster | Where-Object { $_.VsanEnabled } 
    Foreach ($clus in $clusters) {
        $clus | Get-Datastore | Where-Object { $_.type -match "vsan" } | Set-Datastore -Name $(($clus.name) + "_vSAN_Datastore")
    }
}
else {
    Write-Host "vSAN n’est pas activé; cette non-conformité est sans objet"
}

Write-Host "Si un utilisateur ou un compte de service possède plus de privilèges que nécessaire, il s’agit d’une non-conformité."
Get-VIPermission | Sort-Object Role | Select-Object Role, Principal, Entity, Propagate, IsGroup | Format-Table -Auto

Write-Host "ID de vulnérabilité: V-243088 ID de règle: SV-243088r719507_rule ID STIG: VCTR-67-000020"
Write-Host "Vérifiez les balises VLAN du groupe de ports et assurez-vous qu’elles n’utilisent pas un ID VLAN réservé."
Write-Host "Certains commutateurs physiques réservent des ID VLAN à des usages internes et bloquent souvent le trafic configuré avec ces valeurs. Par exemple, les commutateurs Cisco Catalyst réservent généralement les VLAN 1001–1024 et 4094, tandis que les Nexus réservent généralement 3968–4047 et 4094."
Get-VDPortgroup | Select-Object Name, VlanConfiguration

Write-Host "ID de vulnérabilité: V-243087 ID de règle: SV-243087r719504_rule ID STIG: VCTR-67-000019"
Write-Host "Si un groupe de ports est configuré en 'VLAN Trunk' sans exception nécessaire documentée (par exemple pour les appliances NSX), il s’agit d’une non-conformité.
Si le trunking VLAN est autorisé mais n’est pas limité à la plage minimale nécessaire, il s’agit d’une non-conformité."
Get-VDPortgroup | Where-Object { $_.ExtensionData.Config.Uplink -ne "True" } | Select-Object Name, VlanConfiguration

Write-Host "ID de vulnérabilité: V-243078 ID de règle: SV-243078r719644_rule ID STIG: VCTR-67-000008"
Write-Host "Le serveur vCenter doit envoyer immédiatement une alerte en temps réel à SA et ISSO pour tous les échecs d’audit, au minimum."
Write-Host "Si aucune alarme n’est créée et activée pour signaler les défaillances syslog, il s’agit d’une non-conformité."
Get-AlarmDefinition | Where-Object { $_.ExtensionData.Info.Expression.Expression.EventTypeId -eq "esx.problem.vmsyslogd.remote.failure" } | Select-Object Name, Enabled, @{N = "EventTypeId"; E = { $_.ExtensionData.Info.Expression.Expression.EventTypeId } }
```

Voici les fonctions du script :

- **Il configure d’abord PowerCLI, désactive la validation des certificats et désactive la participation au programme d’amélioration de l’expérience client (CEIP).**
- **Il se connecte ensuite aux serveurs vCenter définis dans la variable `$vcenters`.**
- **Il traite chaque contrôle STIG avec les applets de commande PowerCLI. Par exemple, il définit `config.log.level` sur info pour les serveurs vCenter indiqués.**
- **Il applique d’autres contrôles, notamment ceux liés à `config.vpxd.hostPasswordLength` et `VirtualCenter.VimPasswordExpirationInDays`.**
- **Il vérifie et configure enfin des règles de sécurité et d’autres paramètres.**
- **Ce script est un exemple. Adaptez-le aux exigences STIG et à la configuration de votre environnement.**

______

## Automatiser le STIG des machines virtuelles VMware

En plus des hôtes ESXi, vous devez appliquer les contrôles STIG aux machines virtuelles de l’infrastructure VMware. PowerCLI permet d’automatiser leur configuration selon les consignes STIG.

## Script : automatiser le STIG des machines virtuelles VMware

Le script PowerCLI suivant illustre l’automatisation d’une sélection de contrôles STIG pour les machines virtuelles :

```powershell
Set-PowerCLIConfiguration -InvalidCertificateAction Ignore -Confirm:$false
Set-PowerCLIConfiguration -Scope User -ParticipateInCEIP $false -Confirm:$false
Connect-VIServer -Server 127.0.0.1
$cluster = Get-Cluster -Name "Cluster"
$folder = Get-Folder -Name "Folder"

#Source : https://github.com/rlakey/vmware-stig-powercli/blob/master/VMware_vSphere_6.7_VM_STIG_Remediation.ps1
$vmconfig = @{
    #Paramètres de renforcement/STIG
    vmAdvSettings       = @{
        "isolation.tools.copy.disable"          = $true
        "isolation.tools.dnd.disable"           = $true
        "isolation.tools.paste.disable"         = $true
        "isolation.tools.diskShrink.disable"    = $true
        "isolation.tools.diskWiper.disable"     = $true
        "isolation.tools.hgfsServerSet.disable" = $true
        "RemoteDisplay.maxConnections"          = "1"
        "RemoteDisplay.vnc.enabled"             = $false
        "tools.setinfo.sizeLimit"               = "1048576"
        "isolation.device.connectable.disable"  = $true
        "tools.guestlib.enableHostInfo"         = $false
        "tools.guest.desktop.autolock"          = $true
        "mks.enable3d"                          = $false
    }
    vmAdvSettingsRemove = ("sched.mem.pshare.salt")
    vmotionEncryption   = "opportunistic" #disabled, required, opportunistic
}

ForEach ($vm in (Get-VM -Location $cluster | Where-Object { (Get-VM -Location $folder) -contains $_ } )) {
    Write-Output "...Correction des paramètres avancés sur $vm dans $vcenter"
    ForEach ($setting in ($vmconfig.vmAdvSettings.GetEnumerator() | Sort-Object Name)) {
        #Récupérer les valeurs de chaque paramètre indiqué
        $settingname = $setting.name
        $settingvalue = $setting.value
        If ($asetting = $vm | Get-AdvancedSetting -Name $settingname) {
            If ($asetting.value -eq $settingvalue) {
                Write-Output "...Le paramètre $settingname de $vm est déjà correctement défini sur $settingvalue"
            }
            else {
                Write-Output "...Le paramètre $settingname de $vm avait la valeur incorrecte $($asetting.value); définition sur $settingvalue"
                $asetting | Set-AdvancedSetting -Value $settingvalue -Confirm:$false
            }
        }
        else {
            Write-Output "...Le paramètre $settingname n’existe pas sur $vm; création..."
            $vm | New-AdvancedSetting -Name $settingname -Value $settingvalue -Confirm:$false
        }
        Write-Output "...Suppression des paramètres avancés de $vm dans $vcenter si nécessaire"
        ForEach ($setting in ($vmconfig.vmAdvSettingsRemove | Sort-Object Name)) {
            #Vérifier si le paramètre actuel existe
            If ($asetting = $vm | Get-AdvancedSetting -Name $setting) {
                Write-Output "...Le paramètre $setting existe sur $vm...suppression"
                $asetting | Remove-AdvancedSetting -Confirm:$false
            }
            else {
                Write-Output "...Le paramètre $setting n’existe pas sur $vm"
            }
        }   
        If ($vm.extensiondata.Config.MigrateEncryption -eq $vmconfig.vmotionEncryption) {
            Write-Output "...Le chiffrement vMotion est correctement défini sur $vm à $($vmconfig.vmotionEncryption)"
        }
        else {
            $vmv = $vm | get-view
            $config = new-object VMware.Vim.VirtualMachineConfigSpec
            $config.MigrateEncryption = New-object VMware.Vim.VirtualMachineConfigSpecEncryptedVMotionModes
            $config.MigrateEncryption = "$($vmconfig.vmotionEncryption)"
            $vmv.ReconfigVM($config)
        }
    }
}
```

Voici les fonctions du script :

- **Comme dans le script STIG VMware VCSA, il configure PowerCLI au début.**
- **Il se connecte à vCenter, puis sélectionne le cluster et le dossier qui contiennent les machines virtuelles ciblées.**
- **La variable `$vmconfig` contient les paramètres STIG des machines virtuelles. Elle comprend des réglages avancés, comme la désactivation du copier-coller, la limitation des connexions d’affichage à distance et d’autres contrôles.**
- **Il parcourt chaque machine virtuelle du cluster et du dossier définis et lui applique les paramètres STIG.**
- **Il configure aussi le chiffrement vMotion des machines virtuelles.**

Ce script est fourni à titre d’exemple. Modifiez-le selon votre environnement et les exigences STIG applicables.

_____

## Ressources complémentaires

- **Le VIB STIG du DoD [existait auparavant pour les versions 5.0 à 6.7](https://flings.vmware.com/dod-security-technical-implementation-guide-stig-esxi-vib), mais il n’est plus disponible.**
- [Ryan Lakey](https://core.vmware.com/users/ryan-lakey) propose des recommandations utiles pour appliquer les STIG DoD à VMware. Nous vous conseillons de les consulter.
    - [STIG VMware vSphere 8](https://core.vmware.com/resource/vmware-vsphere-8-stig)
    - [STIG VMware vSphere 7](https://core.vmware.com/vsphere-7-stig)
    - [STIG VMware vSphere 6.7](https://core.vmware.com/vmware-vsphere-67-stig)
    - [PowerCLI STIG VMware](https://github.com/rlakey/vmware-stig-powercli)
        - [Base de référence STIG VMware VCSA 6.7](https://github.com/rlakey/vmware-vcsa-6.7-stig-baseline)
        - [Base de référence STIG VMware VM 6.7](https://github.com/rlakey/vmware-vm-6.7-stig-baseline)
_____

## Conclusion

**L’application des STIG VMware contribue à sécuriser l’infrastructure VMware et à respecter les exigences applicables. PowerCLI automatise et simplifie l’application des contrôles STIG aux hôtes ESXi et aux machines virtuelles.**

Cet article a présenté l’utilisation de PowerCLI pour automatiser les STIG VMware ESXi et VM. Il a décrit les prérequis d’installation, fourni des scripts d’exemple et souligné l’importance d’adapter les scripts aux besoins de chaque environnement.

**Avec PowerCLI et les consignes STIG, les administrateurs peuvent sécuriser les déploiements VMware de façon plus efficace, réduire le travail manuel et appliquer des configurations cohérentes.**

## Références

- [VIB STIG du DoD](https://flings.vmware.com/dod-security-technical-implementation-guide-stig-esxi-vib)
- [PowerCLI 11.3](https://www.powershellgallery.com/packages/VMware.PowerCLI/11.3.0.13990089)
- [PowerShell 5 ou version ultérieure](https://docs.microsoft.com/en-us/skypeforbusiness/set-up-your-computer-for-windows-powershell/download-and-install-windows-powershell-5-1)
- [ESXi 6.7 U2 ou version ultérieure](https://my.vmware.com/web/vmware/downloads/details?downloadGroup=ESXI670&productId=742)
