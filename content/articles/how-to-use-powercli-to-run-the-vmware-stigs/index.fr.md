---
title: "Maîtriser la sécurité VMware"
date: 2023-08-03
lastmod: 2026-11-12
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

#Connect to each vcenter server
ForEach ($vc in $vcenters) {
    Connect-VIServer -Server $vc
}

#Automated

Write-Host "Vul ID: V-243098 Rule ID: SV-243098r719537_rule STIG ID: VCTR-67-000036"
Write-Host "If the 'config.log.level' value is not set to "info" or does not exist, this is a finding."
ForEach ($vc in $vcenters) {
    Get-AdvancedSetting -Entity $vc -Name config.log.level | Set-AdvancedSetting -Value info
    Get-AdvancedSetting -Entity $vc -Name config.log.level
}

Write-Host "Vul ID: V-243090 Rule ID: SV-243090r719513_rule STIG ID: VCTR-67-000024"
Write-Host "If the 'config.vpxd.hostPasswordLength' is set to a value other than "32", this is a finding. 
If the setting does not exist, this is not a finding."
ForEach ($vc in $vcenters) {
    Get-AdvancedSetting -Entity $vc -Name config.vpxd.hostPasswordLength | Set-AdvancedSetting -Value 32
    Get-AdvancedSetting -Entity $vc -Name config.vpxd.hostPasswordLength
}


Write-Host "Vul ID: V-243089 Rule ID: SV-243089r719510_rule STIG ID: VCTR-67-000023"
Write-Host "If the 'VirtualCenter.VimPasswordExpirationInDays' is set to a value other than "30" or does not exist, this is a finding."
ForEach ($vc in $vcenters) {
    Try {
        Get-AdvancedSetting -Entity $vc -Name VirtualCenter.VimPasswordExpirationInDays | Set-AdvancedSetting -Value 30
    }
    Catch {
        New-AdvancedSetting -Entity $vc -Name VirtualCenter.VimPasswordExpirationInDays -Value 30
    }
}

Write-Host "Vul ID: V-243084 Rule ID: SV-243085r719498_rule STIG ID: VCTR-67-000016"
Write-Host "If NetFlow is configured and the collector IP is not known and documented, this is a finding."
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

Write-Host "Vul ID: V-243084 Rule ID: SV-243084r719495_rule STIG ID: VCTR-67-000015"
Write-Host "The vCenter Server must set the distributed port group Promiscuous Mode policy to reject."
Get-VDSwitch | Get-VDSecurityPolicy | Set-VDSecurityPolicy -AllowPromiscuous $false
Get-VDPortgroup | Where-Object { $_.IsUplink -eq $false } | Get-VDSecurityPolicy | Set-VDSecurityPolicy -AllowPromiscuous $false
Get-VDSwitch | Get-VDSecurityPolicy
Get-VDPortgroup | Where-Object { $_.IsUplink -eq $false } | Get-VDSecurityPolicy


Write-Host "Vul ID: V-243083 Rule ID: SV-243083r719492_rule STIG ID: VCTR-67-000014"
Write-Host "The vCenter Server must set the distributed port group MAC Address Change policy to reject."
Get-VDSwitch | Get-VDSecurityPolicy | Set-VDSecurityPolicy -MacChanges $false
Get-VDPortgroup | Where-Object { $_.IsUplink -eq $false } | Get-VDSecurityPolicy | Set-VDSecurityPolicy -MacChanges $false
Get-VDPortgroup | Where-Object { $_.IsUplink -eq $false } | Get-VDSecurityPolicy

Write-Host "Vul ID: V-243082 Rule ID: SV-243082r719489_rule STIG ID: VCTR-67-000013"
Write-Host "The vCenter Server must set the distributed port group Forged Transmits policy to reject."
Get-VDSwitch | Get-VDSecurityPolicy | Set-VDSecurityPolicy -ForgedTransmits $false
Get-VDPortgroup | Where-Object { $_.IsUplink -eq $false } | Get-VDSecurityPolicy | Set-VDSecurityPolicy -ForgedTransmits $false
Get-VDSwitch | Get-VDSecurityPolicy
Get-VDPortgroup | Where-Object { $_.IsUplink -eq $false } | Get-VDSecurityPolicy

Write-Host "Vul ID: V-243081 Rule ID: SV-243081r719486_rule STIG ID: VCTR-67-000012"
Write-Host "The vCenter Server must disable the distributed virtual switch health check."
Get-View -ViewType DistributedVirtualSwitch | Where-Object { ($_.config.HealthCheckConfig | Where-Object { $_.enable -notmatch "False" }) } | ForEach-Object { $_.UpdateDVSHealthCheckConfig(@((New-Object Vmware.Vim.VMwareDVSVlanMtuHealthCheckConfig -property @{enable = 0 }), (New-Object Vmware.Vim.VMwareDVSTeamingHealthCheckConfig -property @{enable = 0 }))) }
$vds = Get-VDSwitch
$vds.ExtensionData.Config.HealthCheckConfig

Write-Host "Vul ID: V-243077 Rule ID: SV-243077r719474_rule STIG ID: VCTR-67-00000"
Write-Host "The vCenter Server must manage excess capacity, bandwidth, or other redundancy to limit the effects of information-flooding types of denial-of-service (DoS) attacks by enabling Network I/O Control (NIOC)."
Write-Host "If an alarm is not created and enabled to alert when syslog failures occur, this is a finding."
ForEach ($vdswitch in (Get-VDSwitch.name)){
    (Get-VDSwitch $vdswitch | Get-View).EnableNetworkResourceManagement($true)
}
Get-VDSwitch | Select-Object Name, @{N = "NIOC Enabled"; E = { $_.ExtensionData.config.NetworkResourceManagementEnabled } }

#Manual Review

Write-Host "Vul ID: V-243076 Rule ID: SV-243076r719471_rule STIG ID: VCTR-67-000005"
Write-Host "The vCenter Server users must have the correct roles assigned."
Write-Host "Application service account and user required privileges should be documented.
If any user or service account has more privileges than required, this is a finding."
Get-VIPermission | Sort-Object Role | Select-Object Role, Principal, Entity, Propagate, IsGroup | Format-Table -Auto

Write-Host "Vul ID: V-243119 Rule ID: SV-243119r719600_rule STIG ID: VCTR-67-000064"
Write-Host "If any role other than Administrator and any site-specific group(s) have any of these permissions, this is a finding."
$roles = Get-VIRole
ForEach ($role in $roles) {
    $privileges = $role.PrivilegeList
    If ($privileges -match "Crypto*" -or $privileges -match "Global.Diagnostics" -or $privileges -match "Host.Inventory.Add*" -or $privileges -match "Host.Local operations.Manage user groups") {
        Write-Host "$role has Cryptographic privileges"
    }
}

Write-Host "Vul ID: V-243118 Rule ID: SV-243118r719597_rule STIG ID: VCTR-67-000063"
Write-Host "If there are any users other than Solution Users with the "Administrator" role that are not explicitly designated for cryptographic operations, this is a finding."
Get-VIPermission | Where-Object { $_.Role -eq "Admin" } | Select-Object Role, Principal, Entity, Propagate, IsGroup | Format-Table -Auto


Write-Host "Vul ID: V-243111 Rule ID: SV-243111r719576_rule STIG ID: VCTR-67-000055"
Write-Host "If no clusters are enabled for vSAN, this is not applicable."
Write-host "If vSAN is enabled and the datastore is named 'vsanDatastore', this is a finding."
If ($(Get-Cluster | Where-Object { $_.VsanEnabled } | Measure-Object).Count -gt 0) {
    Write-Host "vSAN Enabled Cluster found"
    $Clusters = Get-Cluster | Where-Object { $_.VsanEnabled } 
    Foreach ($clus in $clusters) {
        $clus | Get-Datastore | Where-Object { $_.type -match "vsan" } | Set-Datastore -Name $(($clus.name) + "_vSAN_Datastore")
    }
}
else {
    Write-Host "vSAN is not enabled, this finding is not applicable"
}

Write-Host "If any user or service account has more privileges than required, this is a finding."
Get-VIPermission | Sort-Object Role | Select-Object Role, Principal, Entity, Propagate, IsGroup | Format-Table -Auto

Write-Host "Vul ID: V-243088 Rule ID: SV-243088r719507_rule STIG ID: VCTR-67-000020"
Write-Host "Review the port group VLAN tags and verify they are not set to a reserved VLAN ID."
Write-Host "Certain physical switches reserve certain VLAN IDs for internal purposes and often disallow traffic configured to these values. For example, Cisco Catalyst switches typically reserve VLANs 1001–1024 and 4094, while Nexus switches typically reserve 3968–4047 and 4094."
Get-VDPortgroup | Select-Object Name, VlanConfiguration

Write-Host "Vul ID: V-243087 Rule ID: SV-243087r719504_rule STIG ID: VCTR-67-000019"
Write-Host "If any port group is configured with 'VLAN Trunk' and is not documented as a needed exception (such as NSX appliances), this is a finding.
If any port group is authorized to be configured with 'VLAN trunking' but is not configured with the most limited range necessary, this is a finding."
Get-VDPortgroup | Where-Object { $_.ExtensionData.Config.Uplink -ne "True" } | Select-Object Name, VlanConfiguration

Write-Host "Vul ID: V-243078 Rule ID: SV-243078r719644_rule STIG ID: VCTR-67-000008"
Write-Host "The vCenter Server must provide an immediate real-time alert to the SA and ISSO, at a minimum, of all audit failure events."
Write-Host "If an alarm is not created and enabled to alert when syslog failures occur, this is a finding."
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

# Credit to https://github.com/rlakey/vmware-stig-powercli/blob/master/VMware_vSphere_6.7_VM_STIG_Remediation.ps1
$vmconfig = @{
    #Hardening/STIG Settings
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
    Write-Output "...Remediating advanced settings on $vm on $vcenter"
    ForEach ($setting in ($vmconfig.vmAdvSettings.GetEnumerator() | Sort-Object Name)) {
        #Pulling values for each setting specified
        $settingname = $setting.name
        $settingvalue = $setting.value
        If ($asetting = $vm | Get-AdvancedSetting -Name $settingname) {
            If ($asetting.value -eq $settingvalue) {
                Write-Output "...Setting $settingname is already configured correctly to $settingvalue on $vm"
            }
            else {
                Write-Output "...Setting $settingname was incorrectly set to $($asetting.value) on $vm setting to $settingvalue"
                $asetting | Set-AdvancedSetting -Value $settingvalue -Confirm:$false
            }
        }
        else {
            Write-Output "...Setting $settingname does not exist on $vm creating setting..."
            $vm | New-AdvancedSetting -Name $settingname -Value $settingvalue -Confirm:$false
        }
        Write-Output "...Removing advanced settings if necessary on $vm on $vcenter"
        ForEach ($setting in ($vmconfig.vmAdvSettingsRemove | Sort-Object Name)) {
            #Checking to see if current setting exists
            If ($asetting = $vm | Get-AdvancedSetting -Name $setting) {
                Write-Output "...Setting $setting exists on $vm...removing setting"
                $asetting | Remove-AdvancedSetting -Confirm:$false
            }
            else {
                Write-Output "...Setting $setting does not exist on $vm"
            }
        }   
        If ($vm.extensiondata.Config.MigrateEncryption -eq $vmconfig.vmotionEncryption) {
            Write-Output "...vMotion encryption set correctly on $vm to $($vmconfig.vmotionEncryption)"
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

- **Le VIB STIG du DoD** [existait auparavant pour les versions 5.0 à 6.7](https://flings.vmware.com/dod-security-technical-implementation-guide-stig-esxi-vib), mais il n’est plus disponible.
- **[Ryan Lakey](https://core.vmware.com/users/ryan-lakey)** propose des recommandations utiles pour appliquer les STIG DoD à VMware. Nous vous conseillons de les consulter.
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
