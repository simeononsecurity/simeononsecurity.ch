---
title: "Domina la seguretat de VMware"
date: 2023-08-03
lastmod: 2026-11-13
toc: true
draft: false
description: "Aprèn a fer servir PowerCLI per aplicar els STIG de VMware i protegir el teu entorn VMware amb aquesta guia completa."
genre: ["Ciberseguretat", "Virtualització", "Infraestructura de TI", "Automatització", "PowerShell", "VMware", "STIG", "Compliment normatiu", "Scripts", "Centre de dades"]
tags: ["PowerCLI", "STIG de VMware", "seguretat de VMware", "automatització", "scripts", "PowerShell", "ESXi", "virtualització", "compliment normatiu", "ciberseguretat", "com fer servir PowerCLI per als STIG de VMware", "automatitzar la seguretat de VMware amb PowerCLI", "script PowerCLI per aplicar els STIG de VMware", "automatització PowerCLI per protegir ESXi", "protegir un entorn VMware amb PowerCLI"]
cover: "/img/cover/An_illustration_depicting_a_computer_server_sh.webp"
coverAlt: "Il·lustració d’un servidor informàtic protegit amb un cadenat, símbol d’una infraestructura VMware segura."
coverCaption: "Fes servir PowerCLI per protegir l’entorn VMware"
---

**Com aplicar els STIG de VMware amb PowerCLI**

PowerCLI és una eina d’automatització i scripts que permet gestionar i configurar entorns VMware amb PowerShell. Aquest article explica com fer servir PowerCLI per aplicar el VMware STIG (Security Technical Implementation Guide) a ESXi i a les màquines virtuals.

## Introducció

El **VMware STIG** ofereix directrius i recomanacions per configurar i gestionar de manera segura una infraestructura VMware. Seguir-lo ajuda les organitzacions a millorar la seguretat dels desplegaments VMware i a complir els requisits governamentals aplicables, com ara l’**STIG de la Defense Information Systems Agency (DISA)**.

## Què és PowerCLI?

**PowerCLI** és una interfície de línia d’ordres i una eina de scripts per administrar entorns VMware. Es basa en PowerShell i inclou nombrosos cmdlets dissenyats específicament per a l’administració de VMware. Els administradors poden automatitzar tasques repetitives, canviar configuracions i recopilar informació de la infraestructura VMware.

### Instal·lació i requisits

Abans de començar amb PowerCLI i VMware STIG, comprova aquests requisits previs:

- [**PowerCLI 11.3**](https://www.powershellgallery.com/packages/VMware.PowerCLI/11.3.0.13990089): instal·la PowerCLI des de PowerShell Gallery amb l’ordre `Install-Module VMware.PowerCLI -force`.
- [**PowerShell 5 o posterior**](https://docs.microsoft.com/en-us/skypeforbusiness/set-up-your-computer-for-windows-powershell/download-and-install-windows-powershell-5-1): comprova que tens instal·lat PowerShell 5 o una versió posterior.
- [**ESXi 6.7 U2 o posterior**](https://my.vmware.com/web/vmware/downloads/details?downloadGroup=ESXI670&productId=742): fes servir ESXi 6.7 U2 o una versió posterior.

## Automatitzar l’STIG de VMware VCSA

L’STIG de VMware ESXi proporciona directrius per protegir els hosts ESXi. Automatitzar-ne els controls simplifica el procés i manté una configuració coherent en diversos hosts.

### Consideracions

Abans d’executar l’automatització, tingues en compte aquests punts:

- **Comprova que cap màquina virtual ni sistema convidat de l’host o del clúster ESXi necessiti funcions de CD, USB o disquet.**
- **Aplica els STIG a tots els hosts ESXi i sistemes convidats connectats a vCenter.**
- **Cal tenir coneixements de resolució de problemes per corregir els incidents que apareguin durant el procés.**

### Script: automatització de l’STIG de VMware VCSA

El següent script de PowerCLI automatitza l’aplicació d’un conjunt seleccionat de controls STIG a les VCSA:

```powershell
Set-PowerCLIConfiguration -InvalidCertificateAction Ignore -Confirm:$false
Set-PowerCLIConfiguration -Scope User -ParticipateInCEIP $false -Confirm:$false
$vcenters = 127.0.0.1, 127.0.0.2

#Connecta’t a cada servidor vCenter
ForEach ($vc in $vcenters) {
    Connect-VIServer -Server $vc
}

#Automatitzat

Write-Host "ID de vulnerabilitat: V-243098 ID de regla: SV-243098r719537_rule ID de STIG: VCTR-67-000036"
Write-Host "Si el valor de 'config.log.level' no està establert en "info" o no existeix, és una troballa."
ForEach ($vc in $vcenters) {
    Get-AdvancedSetting -Entity $vc -Name config.log.level | Set-AdvancedSetting -Value info
    Get-AdvancedSetting -Entity $vc -Name config.log.level
}

Write-Host "ID de vulnerabilitat: V-243090 ID de regla: SV-243090r719513_rule ID de STIG: VCTR-67-000024"
Write-Host "Si 'config.vpxd.hostPasswordLength' té un valor diferent de "32", és una troballa.
Si la configuració no existeix, no és una troballa."
ForEach ($vc in $vcenters) {
    Get-AdvancedSetting -Entity $vc -Name config.vpxd.hostPasswordLength | Set-AdvancedSetting -Value 32
    Get-AdvancedSetting -Entity $vc -Name config.vpxd.hostPasswordLength
}


Write-Host "ID de vulnerabilitat: V-243089 ID de regla: SV-243089r719510_rule ID de STIG: VCTR-67-000023"
Write-Host "Si 'VirtualCenter.VimPasswordExpirationInDays' té un valor diferent de "30" o no existeix, és una troballa."
ForEach ($vc in $vcenters) {
    Try {
        Get-AdvancedSetting -Entity $vc -Name VirtualCenter.VimPasswordExpirationInDays | Set-AdvancedSetting -Value 30
    }
    Catch {
        New-AdvancedSetting -Entity $vc -Name VirtualCenter.VimPasswordExpirationInDays -Value 30
    }
}

Write-Host "ID de vulnerabilitat: V-243084 ID de regla: SV-243085r719498_rule ID de STIG: VCTR-67-000016"
Write-Host "Si NetFlow està configurat i la IP del col·lector no es coneix ni està documentada, és una troballa."
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

Write-Host "ID de vulnerabilitat: V-243084 ID de regla: SV-243084r719495_rule ID de STIG: VCTR-67-000015"
Write-Host "El servidor vCenter ha d’establir en rebutjar la política Promiscuous Mode del grup de ports distribuït."
Get-VDSwitch | Get-VDSecurityPolicy | Set-VDSecurityPolicy -AllowPromiscuous $false
Get-VDPortgroup | Where-Object { $_.IsUplink -eq $false } | Get-VDSecurityPolicy | Set-VDSecurityPolicy -AllowPromiscuous $false
Get-VDSwitch | Get-VDSecurityPolicy
Get-VDPortgroup | Where-Object { $_.IsUplink -eq $false } | Get-VDSecurityPolicy


Write-Host "ID de vulnerabilitat: V-243083 ID de regla: SV-243083r719492_rule ID de STIG: VCTR-67-000014"
Write-Host "El servidor vCenter ha d’establir en rebutjar la política MAC Address Change del grup de ports distribuït."
Get-VDSwitch | Get-VDSecurityPolicy | Set-VDSecurityPolicy -MacChanges $false
Get-VDPortgroup | Where-Object { $_.IsUplink -eq $false } | Get-VDSecurityPolicy | Set-VDSecurityPolicy -MacChanges $false
Get-VDPortgroup | Where-Object { $_.IsUplink -eq $false } | Get-VDSecurityPolicy

Write-Host "ID de vulnerabilitat: V-243082 ID de regla: SV-243082r719489_rule ID de STIG: VCTR-67-000013"
Write-Host "El servidor vCenter ha d’establir en rebutjar la política Forged Transmits del grup de ports distribuït."
Get-VDSwitch | Get-VDSecurityPolicy | Set-VDSecurityPolicy -ForgedTransmits $false
Get-VDPortgroup | Where-Object { $_.IsUplink -eq $false } | Get-VDSecurityPolicy | Set-VDSecurityPolicy -ForgedTransmits $false
Get-VDSwitch | Get-VDSecurityPolicy
Get-VDPortgroup | Where-Object { $_.IsUplink -eq $false } | Get-VDSecurityPolicy

Write-Host "ID de vulnerabilitat: V-243081 ID de regla: SV-243081r719486_rule ID de STIG: VCTR-67-000012"
Write-Host "El servidor vCenter ha de desactivar la comprovació d’estat del commutador virtual distribuït."
Get-View -ViewType DistributedVirtualSwitch | Where-Object { ($_.config.HealthCheckConfig | Where-Object { $_.enable -notmatch "False" }) } | ForEach-Object { $_.UpdateDVSHealthCheckConfig(@((New-Object Vmware.Vim.VMwareDVSVlanMtuHealthCheckConfig -property @{enable = 0 }), (New-Object Vmware.Vim.VMwareDVSTeamingHealthCheckConfig -property @{enable = 0 }))) }
$vds = Get-VDSwitch
$vds.ExtensionData.Config.HealthCheckConfig

Write-Host "ID de vulnerabilitat: V-243077 ID de regla: SV-243077r719474_rule ID de STIG: VCTR-67-00000"
Write-Host "El servidor vCenter ha de gestionar la capacitat, l’amplada de banda o altres redundàncies per limitar els efectes dels atacs de denegació de servei (DoS) per inundació d’informació, activant Network I/O Control (NIOC)."
Write-Host "Si no es crea i s’habilita cap alerta per avisar dels errors de syslog, és una troballa."
ForEach ($vdswitch in (Get-VDSwitch.name)){
    (Get-VDSwitch $vdswitch | Get-View).EnableNetworkResourceManagement($true)
}
Get-VDSwitch | Select-Object Name, @{N = "NIOC Enabled"; E = { $_.ExtensionData.config.NetworkResourceManagementEnabled } }

#Revisió manual

Write-Host "ID de vulnerabilitat: V-243076 ID de regla: SV-243076r719471_rule ID de STIG: VCTR-67-000005"
Write-Host "Els usuaris del servidor vCenter han de tenir assignats els rols correctes."
Write-Host "Cal documentar els privilegis necessaris dels comptes de servei i dels usuaris.
Si un usuari o un compte de servei té més privilegis dels necessaris, és una troballa."
Get-VIPermission | Sort-Object Role | Select-Object Role, Principal, Entity, Propagate, IsGroup | Format-Table -Auto

Write-Host "ID de vulnerabilitat: V-243119 ID de regla: SV-243119r719600_rule ID de STIG: VCTR-67-000064"
Write-Host "Si un rol diferent d’Administrator o algun grup específic del lloc té qualsevol d’aquests permisos, és una troballa."
$roles = Get-VIRole
ForEach ($role in $roles) {
    $privileges = $role.PrivilegeList
    If ($privileges -match "Crypto*" -or $privileges -match "Global.Diagnostics" -or $privileges -match "Host.Inventory.Add*" -or $privileges -match "Host.Local operations.Manage user groups") {
        Write-Host "$role té privilegis criptogràfics"
    }
}

Write-Host "ID de vulnerabilitat: V-243118 ID de regla: SV-243118r719597_rule ID de STIG: VCTR-67-000063"
Write-Host "Si usuaris diferents de Solution Users tenen el rol «Administrator» sense estar designats explícitament per a operacions criptogràfiques, és una troballa."
Get-VIPermission | Where-Object { $_.Role -eq "Admin" } | Select-Object Role, Principal, Entity, Propagate, IsGroup | Format-Table -Auto


Write-Host "ID de vulnerabilitat: V-243111 ID de regla: SV-243111r719576_rule ID de STIG: VCTR-67-000055"
Write-Host "No és aplicable si no hi ha cap clúster vSAN habilitat."
Write-host "Si vSAN està habilitat i el magatzem de dades s’anomena 'vsanDatastore', és una troballa."
If ($(Get-Cluster | Where-Object { $_.VsanEnabled } | Measure-Object).Count -gt 0) {
    Write-Host "S’ha trobat un clúster vSAN habilitat"
    $Clusters = Get-Cluster | Where-Object { $_.VsanEnabled } 
    Foreach ($clus in $clusters) {
        $clus | Get-Datastore | Where-Object { $_.type -match "vsan" } | Set-Datastore -Name $(($clus.name) + "_vSAN_Datastore")
    }
}
else {
    Write-Host "vSAN no està habilitat; aquesta troballa no és aplicable"
}

Write-Host "Si un usuari o un compte de servei té més privilegis dels necessaris, és una troballa."
Get-VIPermission | Sort-Object Role | Select-Object Role, Principal, Entity, Propagate, IsGroup | Format-Table -Auto

Write-Host "ID de vulnerabilitat: V-243088 ID de regla: SV-243088r719507_rule ID de STIG: VCTR-67-000020"
Write-Host "Reviseu les etiquetes VLAN del grup de ports i comproveu que no facin servir un ID de VLAN reservat."
Write-Host "Alguns commutadors físics reserven ID de VLAN per a ús intern i sovint bloquegen el trànsit configurat amb aquests valors. Per exemple, els Cisco Catalyst solen reservar les VLAN 1001–1024 i 4094, mentre que els Nexus solen reservar 3968–4047 i 4094."
Get-VDPortgroup | Select-Object Name, VlanConfiguration

Write-Host "ID de vulnerabilitat: V-243087 ID de regla: SV-243087r719504_rule ID de STIG: VCTR-67-000019"
Write-Host "Si un grup de ports està configurat com a 'VLAN Trunk' sense una excepció necessària documentada (com ara dispositius NSX), és una troballa.
Si es permet l'encaminament VLAN però no es limita a l'interval mínim necessari, és una troballa."
Get-VDPortgroup | Where-Object { $_.ExtensionData.Config.Uplink -ne "True" } | Select-Object Name, VlanConfiguration

Write-Host "ID de vulnerabilitat: V-243078 ID de regla: SV-243078r719644_rule ID de STIG: VCTR-67-000008"
Write-Host "El servidor vCenter ha d’avisar immediatament SA i ISSO, com a mínim en temps real, de tots els errors d’auditoria."
Write-Host "Si no es crea i s’habilita cap alerta per avisar dels errors de syslog, és una troballa."
Get-AlarmDefinition | Where-Object { $_.ExtensionData.Info.Expression.Expression.EventTypeId -eq "esx.problem.vmsyslogd.remote.failure" } | Select-Object Name, Enabled, @{N = "EventTypeId"; E = { $_.ExtensionData.Info.Expression.Expression.EventTypeId } }
```

Aquestes són les funcions de l’script:

- **Primer configura PowerCLI, desactiva la validació dels certificats i rebutja la participació al Customer Experience Improvement Program (CEIP).**
- **Després es connecta als servidors vCenter indicats a la variable `$vcenters`.**
- **Aplica cada control STIG amb cmdlets de PowerCLI. Per exemple, estableix `config.log.level` en info als servidors vCenter especificats.**
- **També tracta controls com `config.vpxd.hostPasswordLength` i `VirtualCenter.VimPasswordExpirationInDays`.**
- **Finalment, revisa i configura polítiques de seguretat i altres paràmetres.**
- **Aquest script és un exemple. Adapta’l al teu entorn i als requisits STIG corresponents.**

______

## Automatitzar l’STIG de les màquines virtuals VMware

A més de protegir els hosts ESXi, has d’aplicar controls STIG a les màquines virtuals de la infraestructura VMware. PowerCLI permet automatitzar-ne la configuració segons les directrius STIG.

## Script: automatització de l’STIG de les màquines virtuals VMware

El següent script de PowerCLI mostra com automatitzar controls STIG seleccionats per a les màquines virtuals:

```powershell
Set-PowerCLIConfiguration -InvalidCertificateAction Ignore -Confirm:$false
Set-PowerCLIConfiguration -Scope User -ParticipateInCEIP $false -Confirm:$false
Connect-VIServer -Server 127.0.0.1
$cluster = Get-Cluster -Name "Cluster"
$folder = Get-Folder -Name "Folder"

#Crèdit: https://github.com/rlakey/vmware-stig-powercli/blob/master/VMware_vSphere_6.7_VM_STIG_Remediation.ps1
$vmconfig = @{
    #Configuració d’enduriment/STIG
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
    Write-Output "...S’estan corregint els paràmetres avançats de $vm a $vcenter"
    ForEach ($setting in ($vmconfig.vmAdvSettings.GetEnumerator() | Sort-Object Name)) {
        #Recull els valors de cada paràmetre indicat
        $settingname = $setting.name
        $settingvalue = $setting.value
        If ($asetting = $vm | Get-AdvancedSetting -Name $settingname) {
            If ($asetting.value -eq $settingvalue) {
                Write-Output "...El paràmetre $settingname de $vm ja està configurat correctament amb el valor $settingvalue"
            }
            else {
                Write-Output "...El paràmetre $settingname de $vm tenia el valor incorrecte $($asetting.value); s’estableix a $settingvalue"
                $asetting | Set-AdvancedSetting -Value $settingvalue -Confirm:$false
            }
        }
        else {
            Write-Output "...El paràmetre $settingname no existeix a $vm; s’està creant..."
            $vm | New-AdvancedSetting -Name $settingname -Value $settingvalue -Confirm:$false
        }
        Write-Output "...S’eliminen els paràmetres avançats de $vm a $vcenter si cal"
        ForEach ($setting in ($vmconfig.vmAdvSettingsRemove | Sort-Object Name)) {
            #Comprova si ja existeix el paràmetre actual
            If ($asetting = $vm | Get-AdvancedSetting -Name $setting) {
                Write-Output "...El paràmetre $setting existeix a $vm...s’elimina"
                $asetting | Remove-AdvancedSetting -Confirm:$false
            }
            else {
                Write-Output "...El paràmetre $setting no existeix a $vm"
            }
        }   
        If ($vm.extensiondata.Config.MigrateEncryption -eq $vmconfig.vmotionEncryption) {
            Write-Output "...El xifratge vMotion està configurat correctament a $vm amb el valor $($vmconfig.vmotionEncryption)"
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

Aquestes són les funcions de l’script:

- **Com el script STIG de VMware VCSA, configura PowerCLI al començament.**
- **Es connecta a vCenter i selecciona el clúster i la carpeta que contenen les màquines virtuals objectiu.**
- **La variable `$vmconfig` conté la configuració STIG de les màquines virtuals. Inclou opcions avançades, com ara desactivar copiar i enganxar i limitar les connexions de visualització remota.**
- **Recorre cada màquina virtual del clúster i de la carpeta seleccionats i hi aplica la configuració STIG.**
- **També configura el xifratge vMotion de les màquines virtuals.**

Aquest script és un exemple. Modifica’l segons el teu entorn i els requisits STIG aplicables.

_____

## Recursos addicionals

- **El VIB STIG del DoD [havia estat disponible per a les versions de la 5.0 a la 6.7](https://flings.vmware.com/dod-security-technical-implementation-guide-stig-esxi-vib), però ja no està disponible.**
- [Ryan Lakey](https://core.vmware.com/users/ryan-lakey) ofereix consells útils per aplicar els STIG del DoD a VMware. Et recomanem que els llegeixis.
    - [STIG de VMware vSphere 8](https://core.vmware.com/resource/vmware-vsphere-8-stig)
    - [STIG de VMware vSphere 7](https://core.vmware.com/vsphere-7-stig)
    - [STIG de VMware vSphere 6.7](https://core.vmware.com/vmware-vsphere-67-stig)
    - [PowerCLI STIG de VMware](https://github.com/rlakey/vmware-stig-powercli)
        - [Línia de base STIG de VMware VCSA 6.7](https://github.com/rlakey/vmware-vcsa-6.7-stig-baseline)
        - [Línia de base STIG de màquines virtuals VMware 6.7](https://github.com/rlakey/vmware-vm-6.7-stig-baseline)
_____

## Conclusió

**Aplicar l’STIG de VMware ajuda a protegir la infraestructura VMware i a complir els requisits aplicables. PowerCLI automatitza i simplifica l’aplicació de controls STIG als hosts ESXi i a les màquines virtuals.**

Aquest article ha explicat com fer servir PowerCLI per automatitzar els STIG de VMware ESXi i de màquines virtuals. Hem descrit els requisits d’instal·lació, hem inclòs scripts d’exemple i hem destacat la importància d’adaptar-los a cada entorn.

**Amb PowerCLI i seguint les directrius STIG, els administradors poden protegir amb eficàcia els desplegaments VMware, reduir la feina manual i mantenir configuracions coherents.**

## Referències

- [VIB STIG del DoD](https://flings.vmware.com/dod-security-technical-implementation-guide-stig-esxi-vib)
- [PowerCLI 11.3](https://www.powershellgallery.com/packages/VMware.PowerCLI/11.3.0.13990089)
- [PowerShell 5 o posterior](https://docs.microsoft.com/en-us/skypeforbusiness/set-up-your-computer-for-windows-powershell/download-and-install-windows-powershell-5-1)
- [ESXi 6.7 U2 o posterior](https://my.vmware.com/web/vmware/downloads/details?downloadGroup=ESXI670&productId=742)
