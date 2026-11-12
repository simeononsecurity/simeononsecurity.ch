---
title: "Domina la seguridad de VMware"
date: 2023-08-03
lastmod: 2026-11-12
toc: true
draft: false
description: "Aprende a usar PowerCLI para aplicar los STIG de VMware y proteger tu entorno de VMware con esta guía completa."
genre: ["Ciberseguridad", "Virtualización", "Infraestructura de TI", "Automatización", "PowerShell", "VMware", "STIG", "Cumplimiento", "Scripting", "Centro de datos"]
tags: ["PowerCLI", "STIG de VMware", "seguridad de VMware", "automatización", "scripting", "PowerShell", "ESXi", "virtualización", "cumplimiento", "ciberseguridad", "cómo usar PowerCLI para los STIG de VMware", "automatizar la seguridad de VMware con PowerCLI", "script PowerCLI para implementar STIG de VMware", "automatización de PowerCLI para proteger ESXi", "proteger un entorno VMware con PowerCLI"]
cover: "/img/cover/An_illustration_depicting_a_computer_server_sh.webp"
coverAlt: "Ilustración de un servidor informático protegido por un candado, símbolo de una infraestructura VMware segura."
coverCaption: "Aprovecha PowerCLI para proteger tu entorno VMware"
---

**Cómo aplicar STIG de VMware con PowerCLI**

PowerCLI es una herramienta de automatización y scripting que permite administrar y configurar entornos VMware con PowerShell. En este artículo veremos cómo usar PowerCLI para aplicar el VMware STIG (Security Technical Implementation Guide) a ESXi y a las máquinas virtuales.

## Introducción

El **VMware STIG** ofrece pautas y recomendaciones para configurar y administrar de forma segura la infraestructura VMware. Seguirlo ayuda a las organizaciones a mejorar la seguridad de sus implementaciones de VMware y cumplir las normas gubernamentales pertinentes, como el **STIG de la Defense Information Systems Agency (DISA)**.

## ¿Qué es PowerCLI?

**PowerCLI** es una interfaz de línea de comandos y una herramienta de scripting para administrar entornos VMware. Está basada en PowerShell e incluye numerosos cmdlets diseñados para la administración de VMware. Los administradores pueden automatizar tareas repetitivas, cambiar configuraciones y recopilar información de la infraestructura VMware.

### Instalación y requisitos

Antes de empezar con PowerCLI y VMware STIG, confirma que cumples estos requisitos:

- [**PowerCLI 11.3**](https://www.powershellgallery.com/packages/VMware.PowerCLI/11.3.0.13990089): instala PowerCLI desde PowerShell Gallery con el comando `Install-Module VMware.PowerCLI -force`.
- [**PowerShell 5 o posterior**](https://docs.microsoft.com/en-us/skypeforbusiness/set-up-your-computer-for-windows-powershell/download-and-install-windows-powershell-5-1): comprueba que tienes instalada la versión 5 de PowerShell o una posterior.
- [**ESXi 6.7 U2 o posterior**](https://my.vmware.com/web/vmware/downloads/details?downloadGroup=ESXI670&productId=742): usa ESXi 6.7 U2 o una versión posterior.

## Automatizar el STIG de VMware VCSA

El STIG de VMware ESXi ofrece pautas para proteger los hosts ESXi. Automatizar sus controles permite simplificar el proceso y mantener una configuración coherente en varios hosts.

### Consideraciones

Antes de ejecutar la automatización, ten en cuenta lo siguiente:

- **Comprueba que ninguna máquina virtual ni ningún sistema invitado del host o clúster ESXi necesite funciones de CD, USB o disquete.**
- **Aplica STIG a todos los hosts ESXi y sistemas invitados vinculados a vCenter.**
- **Necesitas conocimientos de resolución de problemas para corregir los problemas que surjan durante el proceso.**

### Script: automatización del STIG de VMware VCSA

El siguiente script de PowerCLI automatiza una selección de controles STIG para VCSA:

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

Estas son las funciones del script:

- **Primero configura PowerCLI, desactiva la validación de certificados y desactiva la participación en el Programa de Mejora de la Experiencia del Cliente (CEIP).**
- **Después se conecta a los servidores vCenter indicados en la variable `$vcenters`.**
- **Aplica cada control STIG con cmdlets de PowerCLI. Por ejemplo, establece `config.log.level` en info para los servidores vCenter especificados.**
- **También trata controles como `config.vpxd.hostPasswordLength` y `VirtualCenter.VimPasswordExpirationInDays`.**
- **Por último, revisa y configura políticas de seguridad y otros parámetros.**
- **Este script es un ejemplo. Adáptalo a las necesidades de tu entorno y a sus requisitos STIG.**

______

## Automatizar el STIG de máquinas virtuales VMware

Además de proteger los hosts ESXi, debes aplicar controles STIG a las máquinas virtuales de la infraestructura VMware. PowerCLI ayuda a automatizar la configuración de las máquinas virtuales conforme a las pautas STIG.

## Script: automatización del STIG de máquinas virtuales VMware

El siguiente script de PowerCLI muestra cómo automatizar una selección de controles STIG para máquinas virtuales:

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

Estas son las funciones del script:

- **Al igual que el script STIG de VMware VCSA, configura el entorno de PowerCLI al inicio.**
- **Se conecta a vCenter y selecciona el clúster y la carpeta donde se encuentran las máquinas virtuales objetivo.**
- **La variable `$vmconfig` contiene los ajustes STIG de las máquinas virtuales. Incluye opciones avanzadas, como desactivar copiar y pegar, limitar las conexiones de pantalla remota y otras medidas.**
- **Recorre cada máquina virtual del clúster y la carpeta seleccionados para aplicar los ajustes STIG.**
- **También configura el cifrado de vMotion de las máquinas virtuales.**

Este script es un ejemplo. Modifícalo según tu entorno y los requisitos STIG aplicables.

_____

## Recursos adicionales

- **El VIB STIG del DoD** [estuvo disponible para las versiones 5.0 a 6.7](https://flings.vmware.com/dod-security-technical-implementation-guide-stig-esxi-vib), pero ya no está disponible.
- **[Ryan Lakey](https://core.vmware.com/users/ryan-lakey)** ofrece recomendaciones útiles para implementar los STIG del DoD en VMware. Te recomendamos leerlas.
    - [STIG de VMware vSphere 8](https://core.vmware.com/resource/vmware-vsphere-8-stig)
    - [STIG de VMware vSphere 7](https://core.vmware.com/vsphere-7-stig)
    - [STIG de VMware vSphere 6.7](https://core.vmware.com/vmware-vsphere-67-stig)
    - [PowerCLI STIG de VMware](https://github.com/rlakey/vmware-stig-powercli)
        - [Línea base STIG de VMware VCSA 6.7](https://github.com/rlakey/vmware-vcsa-6.7-stig-baseline)
        - [Línea base STIG de máquinas virtuales VMware 6.7](https://github.com/rlakey/vmware-vm-6.7-stig-baseline)
_____

## Conclusión

**Aplicar el STIG de VMware es importante para proteger la infraestructura VMware y cumplir las normas pertinentes. PowerCLI automatiza y simplifica la aplicación de controles STIG a hosts ESXi y máquinas virtuales.**

En este artículo vimos cómo usar PowerCLI para automatizar los STIG de VMware ESXi y máquinas virtuales. Repasamos los requisitos de instalación, mostramos scripts de ejemplo y destacamos la importancia de adaptarlos a las necesidades de cada entorno.

**Con PowerCLI y las pautas STIG, los administradores pueden proteger de forma eficiente sus implementaciones VMware, reducir el trabajo manual y mantener configuraciones coherentes.**

## Referencias

- [VIB STIG del DoD](https://flings.vmware.com/dod-security-technical-implementation-guide-stig-esxi-vib)
- [PowerCLI 11.3](https://www.powershellgallery.com/packages/VMware.PowerCLI/11.3.0.13990089)
- [PowerShell 5 o posterior](https://docs.microsoft.com/en-us/skypeforbusiness/set-up-your-computer-for-windows-powershell/download-and-install-windows-powershell-5-1)
- [ESXi 6.7 U2 o posterior](https://my.vmware.com/web/vmware/downloads/details?downloadGroup=ESXI670&productId=742)
