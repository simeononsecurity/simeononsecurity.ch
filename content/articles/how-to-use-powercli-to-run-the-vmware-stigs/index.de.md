---
title: "VMware-Sicherheit meistern"
date: 2023-08-03
lastmod: 2026-11-12
toc: true
draft: false
description: "Erfahren Sie in diesem umfassenden Leitfaden, wie Sie mit PowerCLI VMware-STIGs anwenden und Ihre VMware-Umgebung absichern."
genre: ["Cybersicherheit", "Virtualisierung", "IT-Infrastruktur", "Automatisierung", "PowerShell", "VMware", "STIG", "Compliance", "Skripting", "Rechenzentrum"]
tags: ["PowerCLI", "VMware-STIG", "VMware-Sicherheit", "Automatisierung", "Skripting", "PowerShell", "ESXi", "Virtualisierung", "Compliance", "Cybersicherheit", "PowerCLI für VMware-STIGs verwenden", "VMware-Sicherheit mit PowerCLI automatisieren", "PowerCLI-Skript zur Umsetzung von VMware-STIGs", "PowerCLI-Automatisierung für ESXi-Sicherheit", "VMware-Umgebung mit PowerCLI absichern"]
cover: "/img/cover/An_illustration_depicting_a_computer_server_sh.webp"
coverAlt: "Illustration eines Computerservers mit Vorhängeschloss als Symbol für eine geschützte VMware-Infrastruktur."
coverCaption: "PowerCLI für den Schutz Ihrer VMware-Umgebung einsetzen"
---

**VMware-STIGs mit PowerCLI anwenden**

PowerCLI ist ein Automatisierungs- und Skriptingwerkzeug zur Verwaltung und Konfiguration von VMware-Umgebungen mit PowerShell. Dieser Artikel zeigt, wie Sie PowerCLI einsetzen, um den VMware STIG (Security Technical Implementation Guide) auf ESXi und virtuellen Maschinen umzusetzen.

## Einführung

Der **VMware STIG** enthält Richtlinien und Empfehlungen für die sichere Konfiguration und Verwaltung einer VMware-Infrastruktur. Die Umsetzung hilft Unternehmen, die Sicherheit ihrer VMware-Bereitstellungen zu verbessern und einschlägige staatliche Vorgaben wie den **STIG der Defense Information Systems Agency (DISA)** einzuhalten.

## Was ist PowerCLI?

**PowerCLI** ist eine Befehlszeilenschnittstelle und ein Skriptingwerkzeug für die Verwaltung von VMware-Umgebungen. Es basiert auf PowerShell und stellt zahlreiche speziell für die VMware-Administration entwickelte Cmdlets bereit. Administratoren automatisieren damit wiederkehrende Aufgaben, ändern Konfigurationen und erfassen Informationen aus der VMware-Infrastruktur.

### Installation und Voraussetzungen

Prüfen Sie vor der Arbeit mit PowerCLI und VMware STIG die folgenden Voraussetzungen:

- [**PowerCLI 11.3**](https://www.powershellgallery.com/packages/VMware.PowerCLI/11.3.0.13990089): Installieren Sie PowerCLI aus der PowerShell Gallery mit dem Befehl `Install-Module VMware.PowerCLI -force`.
- [**PowerShell 5 oder neuer**](https://docs.microsoft.com/en-us/skypeforbusiness/set-up-your-computer-for-windows-powershell/download-and-install-windows-powershell-5-1): Stellen Sie sicher, dass PowerShell 5 oder neuer installiert ist.
- [**ESXi 6.7 U2 oder neuer**](https://my.vmware.com/web/vmware/downloads/details?downloadGroup=ESXI670&productId=742): Verwenden Sie ESXi 6.7 U2 oder neuer.

## VMware-VCSA-STIG automatisieren

Der VMware-ESXi-STIG enthält Vorgaben zum Schutz von ESXi-Hosts. Wenn Sie STIG-Kontrollen automatisieren, vereinfachen Sie die Umsetzung und sorgen für eine einheitliche Konfiguration auf mehreren Hosts.

### Wichtige Punkte

Beachten Sie vor der Automatisierung Folgendes:

- **Stellen Sie sicher, dass keine virtuelle Maschine und kein Gast auf dem ESXi-Host oder Cluster CD-, USB- oder Diskettenfunktionen benötigt.**
- **Wenden Sie STIG auf alle ESXi-Hosts und Gäste an, die mit vCenter verbunden sind.**
- **Sie benötigen Fähigkeiten zur Fehlerbehebung, um mögliche Probleme während des Vorgangs zu lösen.**

### Skript: VMware-VCSA-STIG-Automatisierung

Das folgende PowerCLI-Skript automatisiert ausgewählte STIG-Kontrollen für VCSAs:

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

Das Skript erfüllt folgende Aufgaben:

- **Zu Beginn konfiguriert es PowerCLI, deaktiviert die Zertifikatsprüfung und die Teilnahme am Customer Experience Improvement Program (CEIP).**
- **Anschließend verbindet es sich mit den vCenter-Servern in der Variablen `$vcenters`.**
- **Es behandelt jede STIG-Kontrolle mit PowerCLI-Cmdlets. Zum Beispiel setzt es `config.log.level` für die angegebenen vCenter-Server auf info.**
- **Weitere Kontrollen betreffen unter anderem `config.vpxd.hostPasswordLength` und `VirtualCenter.VimPasswordExpirationInDays`.**
- **Zum Schluss prüft und konfiguriert es Sicherheitsrichtlinien und weitere Einstellungen.**
- **Das Skript dient als Beispiel. Passen Sie es an Ihre Umgebung und deren STIG-Anforderungen an.**

______

## VMware-VM-STIG automatisieren

Neben den ESXi-Hosts müssen Sie STIG-Kontrollen auch auf virtuellen Maschinen der VMware-Infrastruktur anwenden. Mit PowerCLI lässt sich deren Konfiguration nach den STIG-Vorgaben automatisieren.

## Skript: VMware-VM-STIG automatisieren

Das folgende PowerCLI-Skript zeigt, wie ausgewählte STIG-Kontrollen für virtuelle Maschinen automatisiert werden:

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

Das Skript erfüllt folgende Aufgaben:

- **Wie beim VMware-VCSA-STIG-Skript wird PowerCLI zu Beginn konfiguriert.**
- **Es verbindet sich mit vCenter und wählt den Cluster und Ordner aus, in denen sich die Ziel-VMs befinden.**
- **Die Variable `$vmconfig` enthält die STIG-Einstellungen für VMs. Dazu gehören erweiterte Einstellungen wie das Deaktivieren von Kopieren und Einfügen sowie das Begrenzen von Remotedisplayverbindungen.**
- **Es durchläuft jede VM im angegebenen Cluster und Ordner und wendet die STIG-Einstellungen an.**
- **Außerdem konfiguriert es die vMotion-Verschlüsselung der VMs.**

Das Skript ist ein Beispiel. Passen Sie es an Ihre Umgebung und die geltenden STIG-Anforderungen an.

_____

## Weitere Ressourcen

- **Das DoD-STIG-VIB** [war früher für Versionen 5.0 bis 6.7 verfügbar](https://flings.vmware.com/dod-security-technical-implementation-guide-stig-esxi-vib), ist aber nicht mehr erhältlich.
- **[Ryan Lakey](https://core.vmware.com/users/ryan-lakey)** bietet hilfreiche Hinweise zur Umsetzung der DoD-VMware-STIGs. Diese Ressourcen sind eine gute Ergänzung.
    - [VMware-vSphere-8-STIG](https://core.vmware.com/resource/vmware-vsphere-8-stig)
    - [VMware-vSphere-7-STIG](https://core.vmware.com/vsphere-7-stig)
    - [VMware-vSphere-6.7-STIG](https://core.vmware.com/vmware-vsphere-67-stig)
    - [VMware-STIG-PowerCLI](https://github.com/rlakey/vmware-stig-powercli)
        - [VMware-VCSA-6.7-STIG-Baseline](https://github.com/rlakey/vmware-vcsa-6.7-stig-baseline)
        - [VMware-VM-6.7-STIG-Baseline](https://github.com/rlakey/vmware-vm-6.7-stig-baseline)
_____

## Fazit

**Die Umsetzung des VMware STIG trägt zur Sicherheit der VMware-Infrastruktur bei und unterstützt die Einhaltung einschlägiger Vorgaben. PowerCLI automatisiert die Anwendung von STIG-Kontrollen auf ESXi-Hosts und virtuelle Maschinen.**

Dieser Artikel hat gezeigt, wie Sie VMware-ESXi- und VM-STIGs mit PowerCLI automatisieren. Er hat die Installationsvoraussetzungen erläutert, Beispielskripte bereitgestellt und die Anpassung an die jeweilige Umgebung hervorgehoben.

**Mit PowerCLI und den STIG-Vorgaben können Administratoren VMware-Bereitstellungen effizient absichern, manuelle Arbeit verringern und Konfigurationen konsistent halten.**

## Referenzen

- [DoD-STIG-VIB](https://flings.vmware.com/dod-security-technical-implementation-guide-stig-esxi-vib)
- [PowerCLI 11.3](https://www.powershellgallery.com/packages/VMware.PowerCLI/11.3.0.13990089)
- [PowerShell 5 oder neuer](https://docs.microsoft.com/en-us/skypeforbusiness/set-up-your-computer-for-windows-powershell/download-and-install-windows-powershell-5-1)
- [ESXi 6.7 U2 oder neuer](https://my.vmware.com/web/vmware/downloads/details?downloadGroup=ESXI670&productId=742)
