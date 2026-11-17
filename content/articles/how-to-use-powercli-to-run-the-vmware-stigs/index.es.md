---
title: "Domina la seguridad de VMware"
date: 2023-08-03
lastmod: 2026-11-13
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

#Conectar con cada servidor vCenter
ForEach ($vc in $vcenters) {
    Connect-VIServer -Server $vc
}

#Automatizado

Write-Host "ID de vulnerabilidad: V-243098 ID de regla: SV-243098r719537_rule ID de STIG: VCTR-67-000036"
Write-Host "Si el valor de 'config.log.level' no está establecido en "info" o no existe, se trata de un hallazgo."
ForEach ($vc in $vcenters) {
    Get-AdvancedSetting -Entity $vc -Name config.log.level | Set-AdvancedSetting -Value info
    Get-AdvancedSetting -Entity $vc -Name config.log.level
}

Write-Host "ID de vulnerabilidad: V-243090 ID de regla: SV-243090r719513_rule ID de STIG: VCTR-67-000024"
Write-Host "Si 'config.vpxd.hostPasswordLength' tiene un valor distinto de "32", se trata de un hallazgo.
Si la configuración no existe, no se trata de un hallazgo."
ForEach ($vc in $vcenters) {
    Get-AdvancedSetting -Entity $vc -Name config.vpxd.hostPasswordLength | Set-AdvancedSetting -Value 32
    Get-AdvancedSetting -Entity $vc -Name config.vpxd.hostPasswordLength
}


Write-Host "ID de vulnerabilidad: V-243089 ID de regla: SV-243089r719510_rule ID de STIG: VCTR-67-000023"
Write-Host "Si 'VirtualCenter.VimPasswordExpirationInDays' tiene un valor distinto de "30" o no existe, se trata de un hallazgo."
ForEach ($vc in $vcenters) {
    Try {
        Get-AdvancedSetting -Entity $vc -Name VirtualCenter.VimPasswordExpirationInDays | Set-AdvancedSetting -Value 30
    }
    Catch {
        New-AdvancedSetting -Entity $vc -Name VirtualCenter.VimPasswordExpirationInDays -Value 30
    }
}

Write-Host "ID de vulnerabilidad: V-243084 ID de regla: SV-243085r719498_rule ID de STIG: VCTR-67-000016"
Write-Host "Si NetFlow está configurado y la IP del recopilador no se conoce ni está documentada, se trata de un hallazgo."
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

Write-Host "ID de vulnerabilidad: V-243084 ID de regla: SV-243084r719495_rule ID de STIG: VCTR-67-000015"
Write-Host "El servidor vCenter debe establecer en rechazar la directiva Promiscuous Mode del grupo de puertos distribuido."
Get-VDSwitch | Get-VDSecurityPolicy | Set-VDSecurityPolicy -AllowPromiscuous $false
Get-VDPortgroup | Where-Object { $_.IsUplink -eq $false } | Get-VDSecurityPolicy | Set-VDSecurityPolicy -AllowPromiscuous $false
Get-VDSwitch | Get-VDSecurityPolicy
Get-VDPortgroup | Where-Object { $_.IsUplink -eq $false } | Get-VDSecurityPolicy


Write-Host "ID de vulnerabilidad: V-243083 ID de regla: SV-243083r719492_rule ID de STIG: VCTR-67-000014"
Write-Host "El servidor vCenter debe establecer en rechazar la directiva MAC Address Change del grupo de puertos distribuido."
Get-VDSwitch | Get-VDSecurityPolicy | Set-VDSecurityPolicy -MacChanges $false
Get-VDPortgroup | Where-Object { $_.IsUplink -eq $false } | Get-VDSecurityPolicy | Set-VDSecurityPolicy -MacChanges $false
Get-VDPortgroup | Where-Object { $_.IsUplink -eq $false } | Get-VDSecurityPolicy

Write-Host "ID de vulnerabilidad: V-243082 ID de regla: SV-243082r719489_rule ID de STIG: VCTR-67-000013"
Write-Host "El servidor vCenter debe establecer en rechazar la directiva Forged Transmits del grupo de puertos distribuido."
Get-VDSwitch | Get-VDSecurityPolicy | Set-VDSecurityPolicy -ForgedTransmits $false
Get-VDPortgroup | Where-Object { $_.IsUplink -eq $false } | Get-VDSecurityPolicy | Set-VDSecurityPolicy -ForgedTransmits $false
Get-VDSwitch | Get-VDSecurityPolicy
Get-VDPortgroup | Where-Object { $_.IsUplink -eq $false } | Get-VDSecurityPolicy

Write-Host "ID de vulnerabilidad: V-243081 ID de regla: SV-243081r719486_rule ID de STIG: VCTR-67-000012"
Write-Host "El servidor vCenter debe deshabilitar la comprobación de estado del conmutador virtual distribuido."
Get-View -ViewType DistributedVirtualSwitch | Where-Object { ($_.config.HealthCheckConfig | Where-Object { $_.enable -notmatch "False" }) } | ForEach-Object { $_.UpdateDVSHealthCheckConfig(@((New-Object Vmware.Vim.VMwareDVSVlanMtuHealthCheckConfig -property @{enable = 0 }), (New-Object Vmware.Vim.VMwareDVSTeamingHealthCheckConfig -property @{enable = 0 }))) }
$vds = Get-VDSwitch
$vds.ExtensionData.Config.HealthCheckConfig

Write-Host "ID de vulnerabilidad: V-243077 ID de regla: SV-243077r719474_rule ID de STIG: VCTR-67-00000"
Write-Host "El servidor vCenter debe administrar la capacidad, el ancho de banda u otra redundancia para limitar los efectos de los ataques de denegación de servicio (DoS) por inundación de información, mediante Network I/O Control (NIOC)."
Write-Host "Si no se crea y habilita una alarma para avisar de fallos de syslog, se trata de un hallazgo."
ForEach ($vdswitch in (Get-VDSwitch.name)){
    (Get-VDSwitch $vdswitch | Get-View).EnableNetworkResourceManagement($true)
}
Get-VDSwitch | Select-Object Name, @{N = "NIOC Enabled"; E = { $_.ExtensionData.config.NetworkResourceManagementEnabled } }

#Revisión manual

Write-Host "ID de vulnerabilidad: V-243076 ID de regla: SV-243076r719471_rule ID de STIG: VCTR-67-000005"
Write-Host "Los usuarios del servidor vCenter deben tener asignados los roles correctos."
Write-Host "Se deben documentar los privilegios necesarios para las cuentas de servicio y los usuarios.
Si una cuenta de usuario o de servicio tiene más privilegios de los necesarios, se trata de un hallazgo."
Get-VIPermission | Sort-Object Role | Select-Object Role, Principal, Entity, Propagate, IsGroup | Format-Table -Auto

Write-Host "ID de vulnerabilidad: V-243119 ID de regla: SV-243119r719600_rule ID de STIG: VCTR-67-000064"
Write-Host "Si un rol distinto de Administrator o algún grupo específico del sitio tiene alguno de estos permisos, se trata de un hallazgo."
$roles = Get-VIRole
ForEach ($role in $roles) {
    $privileges = $role.PrivilegeList
    If ($privileges -match "Crypto*" -or $privileges -match "Global.Diagnostics" -or $privileges -match "Host.Inventory.Add*" -or $privileges -match "Host.Local operations.Manage user groups") {
        Write-Host "$role tiene privilegios criptográficos"
    }
}

Write-Host "ID de vulnerabilidad: V-243118 ID de regla: SV-243118r719597_rule ID de STIG: VCTR-67-000063"
Write-Host "Si usuarios distintos de Solution Users tienen el rol "Administrator" y no están designados explícitamente para operaciones criptográficas, se trata de un hallazgo."
Get-VIPermission | Where-Object { $_.Role -eq "Admin" } | Select-Object Role, Principal, Entity, Propagate, IsGroup | Format-Table -Auto


Write-Host "ID de vulnerabilidad: V-243111 ID de regla: SV-243111r719576_rule ID de STIG: VCTR-67-000055"
Write-Host "No aplica si no hay clústeres vSAN habilitados."
Write-host "Si vSAN está habilitado y el almacén de datos se llama 'vsanDatastore', se trata de un hallazgo."
If ($(Get-Cluster | Where-Object { $_.VsanEnabled } | Measure-Object).Count -gt 0) {
    Write-Host "Se encontró un clúster vSAN habilitado"
    $Clusters = Get-Cluster | Where-Object { $_.VsanEnabled } 
    Foreach ($clus in $clusters) {
        $clus | Get-Datastore | Where-Object { $_.type -match "vsan" } | Set-Datastore -Name $(($clus.name) + "_vSAN_Datastore")
    }
}
else {
    Write-Host "vSAN no está habilitado; este hallazgo no aplica"
}

Write-Host "Si una cuenta de usuario o de servicio tiene más privilegios de los necesarios, se trata de un hallazgo."
Get-VIPermission | Sort-Object Role | Select-Object Role, Principal, Entity, Propagate, IsGroup | Format-Table -Auto

Write-Host "ID de vulnerabilidad: V-243088 ID de regla: SV-243088r719507_rule ID de STIG: VCTR-67-000020"
Write-Host "Revise las etiquetas VLAN del grupo de puertos y compruebe que no usen un ID de VLAN reservado."
Write-Host "Algunos conmutadores físicos reservan ciertos ID de VLAN para uso interno y suelen bloquear el tráfico configurado con esos valores. Por ejemplo, Cisco Catalyst suele reservar las VLAN 1001–1024 y 4094, mientras que Nexus suele reservar 3968–4047 y 4094."
Get-VDPortgroup | Select-Object Name, VlanConfiguration

Write-Host "ID de vulnerabilidad: V-243087 ID de regla: SV-243087r719504_rule ID de STIG: VCTR-67-000019"
Write-Host "Si un grupo de puertos está configurado como 'VLAN Trunk' y no existe una excepción necesaria documentada (como los dispositivos NSX), se trata de un hallazgo.
Si se permite el trunking VLAN, pero no se limita al rango mínimo necesario, se trata de un hallazgo."
Get-VDPortgroup | Where-Object { $_.ExtensionData.Config.Uplink -ne "True" } | Select-Object Name, VlanConfiguration

Write-Host "ID de vulnerabilidad: V-243078 ID de regla: SV-243078r719644_rule ID de STIG: VCTR-67-000008"
Write-Host "El servidor vCenter debe alertar de inmediato y en tiempo real a SA e ISSO, como mínimo, sobre todos los fallos de auditoría."
Write-Host "Si no se crea y habilita una alarma para avisar de fallos de syslog, se trata de un hallazgo."
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

#Crédito: https://github.com/rlakey/vmware-stig-powercli/blob/master/VMware_vSphere_6.7_VM_STIG_Remediation.ps1
$vmconfig = @{
    #Configuración de refuerzo/STIG
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
    Write-Output "...Corrigiendo la configuración avanzada de $vm en $vcenter"
    ForEach ($setting in ($vmconfig.vmAdvSettings.GetEnumerator() | Sort-Object Name)) {
        #Obtener los valores de cada ajuste especificado
        $settingname = $setting.name
        $settingvalue = $setting.value
        If ($asetting = $vm | Get-AdvancedSetting -Name $settingname) {
            If ($asetting.value -eq $settingvalue) {
                Write-Output "...La configuración $settingname ya tiene el valor correcto $settingvalue en $vm"
            }
            else {
                Write-Output "...La configuración $settingname tenía el valor incorrecto $($asetting.value) en $vm; se establecerá en $settingvalue"
                $asetting | Set-AdvancedSetting -Value $settingvalue -Confirm:$false
            }
        }
        else {
            Write-Output "...La configuración $settingname no existe en $vm; creando configuración..."
            $vm | New-AdvancedSetting -Name $settingname -Value $settingvalue -Confirm:$false
        }
        Write-Output "...Quitando la configuración avanzada de $vm en $vcenter si es necesario"
        ForEach ($setting in ($vmconfig.vmAdvSettingsRemove | Sort-Object Name)) {
            #Comprobar si existe el ajuste actual
            If ($asetting = $vm | Get-AdvancedSetting -Name $setting) {
                Write-Output "...La configuración $setting existe en $vm...quitándola"
                $asetting | Remove-AdvancedSetting -Confirm:$false
            }
            else {
                Write-Output "...La configuración $setting no existe en $vm"
            }
        }   
        If ($vm.extensiondata.Config.MigrateEncryption -eq $vmconfig.vmotionEncryption) {
            Write-Output "...El cifrado vMotion está configurado correctamente en $vm como $($vmconfig.vmotionEncryption)"
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

- **El VIB STIG del DoD [estuvo disponible para las versiones 5.0 a 6.7](https://flings.vmware.com/dod-security-technical-implementation-guide-stig-esxi-vib), pero ya no está disponible.**
- [Ryan Lakey](https://core.vmware.com/users/ryan-lakey) ofrece recomendaciones útiles para implementar los STIG del DoD en VMware. Te recomendamos leerlas.
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
