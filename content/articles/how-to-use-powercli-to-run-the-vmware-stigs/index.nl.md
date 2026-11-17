---
title: "VMware-beveiliging beheersen"
date: 2023-08-03
lastmod: 2026-11-13
toc: true
draft: false
description: "Leer in deze uitgebreide gids hoe je met PowerCLI VMware-STIG’s toepast en je VMware-omgeving beveiligt."
genre: ["Cyberbeveiliging", "Virtualisatie", "IT-infrastructuur", "Automatisering", "PowerShell", "VMware", "STIG", "Compliance", "Scripting", "Datacenter"]
tags: ["PowerCLI", "VMware-STIG", "VMware-beveiliging", "automatisering", "scripting", "PowerShell", "ESXi", "virtualisatie", "compliance", "cyberbeveiliging", "PowerCLI gebruiken voor VMware-STIG’s", "VMware-beveiliging automatiseren met PowerCLI", "PowerCLI-script voor VMware-STIG-implementatie", "PowerCLI-automatisering voor ESXi-beveiliging", "VMware-omgeving beveiligen met PowerCLI"]
cover: "/img/cover/An_illustration_depicting_a_computer_server_sh.webp"
coverAlt: "Illustratie van een computerserver met een hangslot, als symbool voor een beveiligde VMware-infrastructuur."
coverCaption: "PowerCLI gebruiken om je VMware-omgeving te beveiligen"
---

**VMware-STIG’s toepassen met PowerCLI**

PowerCLI is een automatiserings- en scripthulpmiddel waarmee je VMware-omgevingen beheert en configureert met PowerShell. Dit artikel laat zien hoe je met PowerCLI de VMware STIG (Security Technical Implementation Guide) toepast op ESXi en virtuele machines.

## Inleiding

De **VMware STIG** bevat richtlijnen en aanbevelingen voor het veilig configureren en beheren van VMware-infrastructuur. Organisaties die deze richtlijnen volgen, verbeteren de beveiliging van VMware-implementaties en ondersteunen naleving van toepasselijke overheidsvoorschriften, zoals de **STIG van de Defense Information Systems Agency (DISA)**.

## Wat is PowerCLI?

**PowerCLI** is een opdrachtregelinterface en scripthulpmiddel voor het beheren van VMware-omgevingen. Het is gebouwd op PowerShell en biedt veel cmdlets die speciaal voor VMware-beheer zijn bedoeld. Beheerders automatiseren er herhaalde taken mee, wijzigen configuraties en verzamelen informatie uit VMware-infrastructuur.

### Installatie en vereisten

Controleer deze vereisten voordat je met PowerCLI en VMware STIG aan de slag gaat:

- [**PowerCLI 11.3**](https://www.powershellgallery.com/packages/VMware.PowerCLI/11.3.0.13990089): installeer PowerCLI vanuit PowerShell Gallery met de opdracht `Install-Module VMware.PowerCLI -force`.
- [**PowerShell 5 of hoger**](https://docs.microsoft.com/en-us/skypeforbusiness/set-up-your-computer-for-windows-powershell/download-and-install-windows-powershell-5-1): controleer of PowerShell 5 of hoger is geïnstalleerd.
- [**ESXi 6.7 U2 of hoger**](https://my.vmware.com/web/vmware/downloads/details?downloadGroup=ESXI670&productId=742): gebruik ESXi 6.7 U2 of hoger.

## VMware VCSA STIG automatiseren

De VMware ESXi STIG geeft richtlijnen voor het beveiligen van ESXi-hosts. Door STIG-controles te automatiseren, vereenvoudig je de uitvoering en houd je de configuratie op meerdere hosts consistent.

### Aandachtspunten

Houd rekening met het volgende voordat je de automatisering uitvoert:

- **Controleer of geen enkele virtuele machine of gast op de ESXi-host of het cluster CD-, USB- of diskettestations nodig heeft.**
- **Pas STIG toe op alle ESXi-hosts en gasten die aan vCenter zijn gekoppeld.**
- **Zorg voor probleemoplossingsvaardigheden om eventuele problemen tijdens het proces aan te pakken.**

### Script: VMware VCSA STIG automatiseren

Met het volgende PowerCLI-script automatiseer je geselecteerde STIG-controles voor VCSA’s:

```powershell
Set-PowerCLIConfiguration -InvalidCertificateAction Ignore -Confirm:$false
Set-PowerCLIConfiguration -Scope User -ParticipateInCEIP $false -Confirm:$false
$vcenters = 127.0.0.1, 127.0.0.2

#Verbinding maken met elke vCenter-server
ForEach ($vc in $vcenters) {
    Connect-VIServer -Server $vc
}

#Geautomatiseerd

Write-Host "Kwetsbaarheids-ID: V-243098 Regel-ID: SV-243098r719537_rule STIG-ID: VCTR-67-000036"
Write-Host "Als de waarde van 'config.log.level' niet op "info" staat of ontbreekt, is dit een bevinding."
ForEach ($vc in $vcenters) {
    Get-AdvancedSetting -Entity $vc -Name config.log.level | Set-AdvancedSetting -Value info
    Get-AdvancedSetting -Entity $vc -Name config.log.level
}

Write-Host "Kwetsbaarheids-ID: V-243090 Regel-ID: SV-243090r719513_rule STIG-ID: VCTR-67-000024"
Write-Host "Als 'config.vpxd.hostPasswordLength' op een andere waarde dan "32" staat, is dit een bevinding.
Als de instelling ontbreekt, is dit geen bevinding."
ForEach ($vc in $vcenters) {
    Get-AdvancedSetting -Entity $vc -Name config.vpxd.hostPasswordLength | Set-AdvancedSetting -Value 32
    Get-AdvancedSetting -Entity $vc -Name config.vpxd.hostPasswordLength
}


Write-Host "Kwetsbaarheids-ID: V-243089 Regel-ID: SV-243089r719510_rule STIG-ID: VCTR-67-000023"
Write-Host "Als 'VirtualCenter.VimPasswordExpirationInDays' op een andere waarde dan "30" staat of ontbreekt, is dit een bevinding."
ForEach ($vc in $vcenters) {
    Try {
        Get-AdvancedSetting -Entity $vc -Name VirtualCenter.VimPasswordExpirationInDays | Set-AdvancedSetting -Value 30
    }
    Catch {
        New-AdvancedSetting -Entity $vc -Name VirtualCenter.VimPasswordExpirationInDays -Value 30
    }
}

Write-Host "Kwetsbaarheids-ID: V-243084 Regel-ID: SV-243085r719498_rule STIG-ID: VCTR-67-000016"
Write-Host "Als NetFlow is ingesteld en het IP-adres van de collector niet bekend en gedocumenteerd is, is dit een bevinding."
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

Write-Host "Kwetsbaarheids-ID: V-243084 Regel-ID: SV-243084r719495_rule STIG-ID: VCTR-67-000015"
Write-Host "De vCenter Server moet het beleid voor de Promiscuous Mode van de distributed port group op weigeren instellen."
Get-VDSwitch | Get-VDSecurityPolicy | Set-VDSecurityPolicy -AllowPromiscuous $false
Get-VDPortgroup | Where-Object { $_.IsUplink -eq $false } | Get-VDSecurityPolicy | Set-VDSecurityPolicy -AllowPromiscuous $false
Get-VDSwitch | Get-VDSecurityPolicy
Get-VDPortgroup | Where-Object { $_.IsUplink -eq $false } | Get-VDSecurityPolicy


Write-Host "Kwetsbaarheids-ID: V-243083 Regel-ID: SV-243083r719492_rule STIG-ID: VCTR-67-000014"
Write-Host "De vCenter Server moet het beleid voor MAC Address Change van de distributed port group op weigeren instellen."
Get-VDSwitch | Get-VDSecurityPolicy | Set-VDSecurityPolicy -MacChanges $false
Get-VDPortgroup | Where-Object { $_.IsUplink -eq $false } | Get-VDSecurityPolicy | Set-VDSecurityPolicy -MacChanges $false
Get-VDPortgroup | Where-Object { $_.IsUplink -eq $false } | Get-VDSecurityPolicy

Write-Host "Kwetsbaarheids-ID: V-243082 Regel-ID: SV-243082r719489_rule STIG-ID: VCTR-67-000013"
Write-Host "De vCenter Server moet het beleid voor Forged Transmits van de distributed port group op weigeren instellen."
Get-VDSwitch | Get-VDSecurityPolicy | Set-VDSecurityPolicy -ForgedTransmits $false
Get-VDPortgroup | Where-Object { $_.IsUplink -eq $false } | Get-VDSecurityPolicy | Set-VDSecurityPolicy -ForgedTransmits $false
Get-VDSwitch | Get-VDSecurityPolicy
Get-VDPortgroup | Where-Object { $_.IsUplink -eq $false } | Get-VDSecurityPolicy

Write-Host "Kwetsbaarheids-ID: V-243081 Regel-ID: SV-243081r719486_rule STIG-ID: VCTR-67-000012"
Write-Host "De vCenter Server moet de healthcheck van de distributed virtual switch uitschakelen."
Get-View -ViewType DistributedVirtualSwitch | Where-Object { ($_.config.HealthCheckConfig | Where-Object { $_.enable -notmatch "False" }) } | ForEach-Object { $_.UpdateDVSHealthCheckConfig(@((New-Object Vmware.Vim.VMwareDVSVlanMtuHealthCheckConfig -property @{enable = 0 }), (New-Object Vmware.Vim.VMwareDVSTeamingHealthCheckConfig -property @{enable = 0 }))) }
$vds = Get-VDSwitch
$vds.ExtensionData.Config.HealthCheckConfig

Write-Host "Kwetsbaarheids-ID: V-243077 Regel-ID: SV-243077r719474_rule STIG-ID: VCTR-67-00000"
Write-Host "De vCenter Server moet overcapaciteit, bandbreedte of andere redundantie beheren om de effecten van informatieoverstroming en denial-of-service-aanvallen (DoS) te beperken door Network I/O Control (NIOC) in te schakelen."
Write-Host "Als er geen alarm is gemaakt en ingeschakeld voor syslog-fouten, is dit een bevinding."
ForEach ($vdswitch in (Get-VDSwitch.name)){
    (Get-VDSwitch $vdswitch | Get-View).EnableNetworkResourceManagement($true)
}
Get-VDSwitch | Select-Object Name, @{N = "NIOC Enabled"; E = { $_.ExtensionData.config.NetworkResourceManagementEnabled } }

#Handmatige controle

Write-Host "Kwetsbaarheids-ID: V-243076 Regel-ID: SV-243076r719471_rule STIG-ID: VCTR-67-000005"
Write-Host "Gebruikers van de vCenter Server moeten de juiste rollen toegewezen krijgen."
Write-Host "Vereiste rechten voor serviceaccounts en gebruikers moeten worden gedocumenteerd.
Als een gebruiker of serviceaccount meer rechten heeft dan nodig, is dit een bevinding."
Get-VIPermission | Sort-Object Role | Select-Object Role, Principal, Entity, Propagate, IsGroup | Format-Table -Auto

Write-Host "Kwetsbaarheids-ID: V-243119 Regel-ID: SV-243119r719600_rule STIG-ID: VCTR-67-000064"
Write-Host "Als een andere rol dan Administrator of een sitegebonden groep een van deze rechten heeft, is dit een bevinding."
$roles = Get-VIRole
ForEach ($role in $roles) {
    $privileges = $role.PrivilegeList
    If ($privileges -match "Crypto*" -or $privileges -match "Global.Diagnostics" -or $privileges -match "Host.Inventory.Add*" -or $privileges -match "Host.Local operations.Manage user groups") {
        Write-Host "$role heeft cryptografische rechten"
    }
}

Write-Host "Kwetsbaarheids-ID: V-243118 Regel-ID: SV-243118r719597_rule STIG-ID: VCTR-67-000063"
Write-Host "Als gebruikers buiten Solution Users de rol "Administrator" hebben zonder expliciet te zijn aangewezen voor cryptografische bewerkingen, is dit een bevinding."
Get-VIPermission | Where-Object { $_.Role -eq "Admin" } | Select-Object Role, Principal, Entity, Propagate, IsGroup | Format-Table -Auto


Write-Host "Kwetsbaarheids-ID: V-243111 Regel-ID: SV-243111r719576_rule STIG-ID: VCTR-67-000055"
Write-Host "Niet van toepassing als geen clusters voor vSAN zijn ingeschakeld."
Write-host "Als vSAN is ingeschakeld en de datastore 'vsanDatastore' heet, is dit een bevinding."
If ($(Get-Cluster | Where-Object { $_.VsanEnabled } | Measure-Object).Count -gt 0) {
    Write-Host "vSAN-cluster ingeschakeld gevonden"
    $Clusters = Get-Cluster | Where-Object { $_.VsanEnabled } 
    Foreach ($clus in $clusters) {
        $clus | Get-Datastore | Where-Object { $_.type -match "vsan" } | Set-Datastore -Name $(($clus.name) + "_vSAN_Datastore")
    }
}
else {
    Write-Host "vSAN is niet ingeschakeld; deze bevinding is niet van toepassing"
}

Write-Host "Als een gebruiker of serviceaccount meer rechten heeft dan nodig, is dit een bevinding."
Get-VIPermission | Sort-Object Role | Select-Object Role, Principal, Entity, Propagate, IsGroup | Format-Table -Auto

Write-Host "Kwetsbaarheids-ID: V-243088 Regel-ID: SV-243088r719507_rule STIG-ID: VCTR-67-000020"
Write-Host "Controleer de VLAN-tags van de port group en verifieer dat ze niet op een gereserveerde VLAN-ID staan."
Write-Host "Sommige fysieke switches reserveren VLAN-ID’s voor intern gebruik en blokkeren vaak verkeer dat daarop is ingesteld. Cisco Catalyst-switches reserveren bijvoorbeeld meestal VLAN’s 1001–1024 en 4094, terwijl Nexus-switches meestal 3968–4047 en 4094 reserveren."
Get-VDPortgroup | Select-Object Name, VlanConfiguration

Write-Host "Kwetsbaarheids-ID: V-243087 Regel-ID: SV-243087r719504_rule STIG-ID: VCTR-67-000019"
Write-Host "Als een port group is ingesteld op 'VLAN Trunk' zonder gedocumenteerde noodzakelijke uitzondering (zoals NSX-appliances), is dit een bevinding.
Als VLAN-trunking is toegestaan maar niet tot het kleinst noodzakelijke bereik is beperkt, is dit een bevinding."
Get-VDPortgroup | Where-Object { $_.ExtensionData.Config.Uplink -ne "True" } | Select-Object Name, VlanConfiguration

Write-Host "Kwetsbaarheids-ID: V-243078 Regel-ID: SV-243078r719644_rule STIG-ID: VCTR-67-000008"
Write-Host "De vCenter Server moet de SA en ISSO direct waarschuwen over alle auditfouten, ten minste in realtime."
Write-Host "Als er geen alarm is gemaakt en ingeschakeld voor syslog-fouten, is dit een bevinding."
Get-AlarmDefinition | Where-Object { $_.ExtensionData.Info.Expression.Expression.EventTypeId -eq "esx.problem.vmsyslogd.remote.failure" } | Select-Object Name, Enabled, @{N = "EventTypeId"; E = { $_.ExtensionData.Info.Expression.Expression.EventTypeId } }
```

Het script voert deze taken uit:

- **Eerst configureert het PowerCLI, schakelt het certificaatvalidatie uit en meldt het zich af voor deelname aan het Customer Experience Improvement Program (CEIP).**
- **Daarna maakt het verbinding met de vCenter-servers in de variabele `$vcenters`.**
- **Het past elke STIG-controle toe met PowerCLI-cmdlets. Zo stelt het `config.log.level` in op info voor de opgegeven vCenter-servers.**
- **Ook controles voor `config.vpxd.hostPasswordLength` en `VirtualCenter.VimPasswordExpirationInDays` komen aan bod.**
- **Tot slot controleert en configureert het beveiligingsbeleid en andere instellingen.**
- **Dit is een voorbeeldscript. Pas het aan je omgeving en de relevante STIG-vereisten aan.**

______

## VMware VM STIG automatiseren

Naast ESXi-hosts moet je ook STIG-controles toepassen op virtuele machines binnen de VMware-infrastructuur. PowerCLI helpt de configuratie van VM’s volgens STIG-richtlijnen te automatiseren.

## Script: VMware VM STIG automatiseren

Het volgende PowerCLI-script laat zien hoe je geselecteerde STIG-controles voor virtuele machines automatiseert:

```powershell
Set-PowerCLIConfiguration -InvalidCertificateAction Ignore -Confirm:$false
Set-PowerCLIConfiguration -Scope User -ParticipateInCEIP $false -Confirm:$false
Connect-VIServer -Server 127.0.0.1
$cluster = Get-Cluster -Name "Cluster"
$folder = Get-Folder -Name "Folder"

#Bron: https://github.com/rlakey/vmware-stig-powercli/blob/master/VMware_vSphere_6.7_VM_STIG_Remediation.ps1
$vmconfig = @{
    #Hardening-/STIG-instellingen
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
    Write-Output "...Geavanceerde instellingen op $vm in $vcenter herstellen"
    ForEach ($setting in ($vmconfig.vmAdvSettings.GetEnumerator() | Sort-Object Name)) {
        #Waarden ophalen voor elke opgegeven instelling
        $settingname = $setting.name
        $settingvalue = $setting.value
        If ($asetting = $vm | Get-AdvancedSetting -Name $settingname) {
            If ($asetting.value -eq $settingvalue) {
                Write-Output "...Instelling $settingname is al correct ingesteld op $settingvalue op $vm"
            }
            else {
                Write-Output "...Instelling $settingname staat onjuist op $($asetting.value) op $vm; instellen op $settingvalue"
                $asetting | Set-AdvancedSetting -Value $settingvalue -Confirm:$false
            }
        }
        else {
            Write-Output "...Instelling $settingname bestaat niet op $vm; instelling maken..."
            $vm | New-AdvancedSetting -Name $settingname -Value $settingvalue -Confirm:$false
        }
        Write-Output "...Geavanceerde instellingen verwijderen indien nodig op $vm in $vcenter"
        ForEach ($setting in ($vmconfig.vmAdvSettingsRemove | Sort-Object Name)) {
            #Controleren of de huidige instelling bestaat
            If ($asetting = $vm | Get-AdvancedSetting -Name $setting) {
                Write-Output "...Instelling $setting bestaat op $vm...instelling verwijderen"
                $asetting | Remove-AdvancedSetting -Confirm:$false
            }
            else {
                Write-Output "...Instelling $setting bestaat niet op $vm"
            }
        }   
        If ($vm.extensiondata.Config.MigrateEncryption -eq $vmconfig.vmotionEncryption) {
            Write-Output "...vMotion-versleuteling is correct ingesteld op $vm op $($vmconfig.vmotionEncryption)"
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

Het script voert deze taken uit:

- **Net als het VMware VCSA STIG-script configureert het eerst de PowerCLI-omgeving.**
- **Het maakt verbinding met vCenter en selecteert het cluster en de map met de doel-VM’s.**
- **De variabele `$vmconfig` bevat de STIG-instellingen voor VM’s. Daaronder vallen geavanceerde instellingen, zoals kopiëren en plakken uitschakelen en externe beeldschermverbindingen beperken.**
- **Het past de STIG-instellingen toe op elke VM in het geselecteerde cluster en de map.**
- **Het configureert ook vMotion-versleuteling voor de VM’s.**

Dit script is een voorbeeld. Pas het aan je omgeving en de toepasselijke STIG-vereisten aan.

_____

## Aanvullende bronnen

- **De DoD STIG VIB was eerder [beschikbaar voor versies 5.0 tot en met 6.7](https://flings.vmware.com/dod-security-technical-implementation-guide-stig-esxi-vib), maar is niet meer beschikbaar.**
- [Ryan Lakey](https://core.vmware.com/users/ryan-lakey) deelt nuttige richtlijnen voor het toepassen van DoD VMware STIG’s. We raden je aan deze te lezen.
    - [VMware vSphere 8 STIG](https://core.vmware.com/resource/vmware-vsphere-8-stig)
    - [VMware vSphere 7 STIG](https://core.vmware.com/vsphere-7-stig)
    - [VMware vSphere 6.7 STIG](https://core.vmware.com/vmware-vsphere-67-stig)
    - [VMware STIG PowerCLI](https://github.com/rlakey/vmware-stig-powercli)
        - [VMware VCSA 6.7 STIG-baseline](https://github.com/rlakey/vmware-vcsa-6.7-stig-baseline)
        - [VMware VM 6.7 STIG-baseline](https://github.com/rlakey/vmware-vm-6.7-stig-baseline)
_____

## Conclusie

**Het toepassen van de VMware STIG helpt VMware-infrastructuur te beveiligen en relevante voorschriften na te leven. PowerCLI automatiseert en vereenvoudigt de toepassing van STIG-controles op ESXi-hosts en virtuele machines.**

Dit artikel beschreef hoe je PowerCLI gebruikt om VMware ESXi- en VM-STIG’s te automatiseren. Het behandelde installatievereisten, gaf voorbeeldscripts en benadrukte dat je scripts aan je omgeving moet aanpassen.

**Met PowerCLI en de STIG-richtlijnen kunnen beheerders VMware-implementaties efficiënt beveiligen, handmatig werk verminderen en configuraties consistent houden.**

## Referenties

- [DoD STIG VIB](https://flings.vmware.com/dod-security-technical-implementation-guide-stig-esxi-vib)
- [PowerCLI 11.3](https://www.powershellgallery.com/packages/VMware.PowerCLI/11.3.0.13990089)
- [PowerShell 5 of hoger](https://docs.microsoft.com/en-us/skypeforbusiness/set-up-your-computer-for-windows-powershell/download-and-install-windows-powershell-5-1)
- [ESXi 6.7 U2 of hoger](https://my.vmware.com/web/vmware/downloads/details?downloadGroup=ESXI670&productId=742)
