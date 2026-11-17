---
title: "VMware-Sicherheit meistern"
date: 2023-08-03
lastmod: 2026-11-13
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

#Mit jedem vCenter-Server verbinden
ForEach ($vc in $vcenters) {
    Connect-VIServer -Server $vc
}

#Automatisiert

Write-Host "Schwachstellen-ID: V-243098 Regel-ID: SV-243098r719537_rule STIG-ID: VCTR-67-000036"
Write-Host "Wenn 'config.log.level' nicht auf "info" gesetzt ist oder fehlt, liegt ein Befund vor."
ForEach ($vc in $vcenters) {
    Get-AdvancedSetting -Entity $vc -Name config.log.level | Set-AdvancedSetting -Value info
    Get-AdvancedSetting -Entity $vc -Name config.log.level
}

Write-Host "Schwachstellen-ID: V-243090 Regel-ID: SV-243090r719513_rule STIG-ID: VCTR-67-000024"
Write-Host "Wenn 'config.vpxd.hostPasswordLength' auf einen anderen Wert als "32" gesetzt ist, liegt ein Befund vor.
Fehlt die Einstellung, liegt kein Befund vor."
ForEach ($vc in $vcenters) {
    Get-AdvancedSetting -Entity $vc -Name config.vpxd.hostPasswordLength | Set-AdvancedSetting -Value 32
    Get-AdvancedSetting -Entity $vc -Name config.vpxd.hostPasswordLength
}


Write-Host "Schwachstellen-ID: V-243089 Regel-ID: SV-243089r719510_rule STIG-ID: VCTR-67-000023"
Write-Host "Wenn 'VirtualCenter.VimPasswordExpirationInDays' auf einen anderen Wert als "30" gesetzt ist oder fehlt, liegt ein Befund vor."
ForEach ($vc in $vcenters) {
    Try {
        Get-AdvancedSetting -Entity $vc -Name VirtualCenter.VimPasswordExpirationInDays | Set-AdvancedSetting -Value 30
    }
    Catch {
        New-AdvancedSetting -Entity $vc -Name VirtualCenter.VimPasswordExpirationInDays -Value 30
    }
}

Write-Host "Schwachstellen-ID: V-243084 Regel-ID: SV-243085r719498_rule STIG-ID: VCTR-67-000016"
Write-Host "Wenn NetFlow konfiguriert ist und die Collector-IP nicht bekannt und dokumentiert ist, liegt ein Befund vor."
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

Write-Host "Schwachstellen-ID: V-243084 Regel-ID: SV-243084r719495_rule STIG-ID: VCTR-67-000015"
Write-Host "Der vCenter Server muss die Richtlinie Promiscuous Mode der verteilten Portgruppe auf Ablehnen setzen."
Get-VDSwitch | Get-VDSecurityPolicy | Set-VDSecurityPolicy -AllowPromiscuous $false
Get-VDPortgroup | Where-Object { $_.IsUplink -eq $false } | Get-VDSecurityPolicy | Set-VDSecurityPolicy -AllowPromiscuous $false
Get-VDSwitch | Get-VDSecurityPolicy
Get-VDPortgroup | Where-Object { $_.IsUplink -eq $false } | Get-VDSecurityPolicy


Write-Host "Schwachstellen-ID: V-243083 Regel-ID: SV-243083r719492_rule STIG-ID: VCTR-67-000014"
Write-Host "Der vCenter Server muss die Richtlinie MAC Address Change der verteilten Portgruppe auf Ablehnen setzen."
Get-VDSwitch | Get-VDSecurityPolicy | Set-VDSecurityPolicy -MacChanges $false
Get-VDPortgroup | Where-Object { $_.IsUplink -eq $false } | Get-VDSecurityPolicy | Set-VDSecurityPolicy -MacChanges $false
Get-VDPortgroup | Where-Object { $_.IsUplink -eq $false } | Get-VDSecurityPolicy

Write-Host "Schwachstellen-ID: V-243082 Regel-ID: SV-243082r719489_rule STIG-ID: VCTR-67-000013"
Write-Host "Der vCenter Server muss die Richtlinie Forged Transmits der verteilten Portgruppe auf Ablehnen setzen."
Get-VDSwitch | Get-VDSecurityPolicy | Set-VDSecurityPolicy -ForgedTransmits $false
Get-VDPortgroup | Where-Object { $_.IsUplink -eq $false } | Get-VDSecurityPolicy | Set-VDSecurityPolicy -ForgedTransmits $false
Get-VDSwitch | Get-VDSecurityPolicy
Get-VDPortgroup | Where-Object { $_.IsUplink -eq $false } | Get-VDSecurityPolicy

Write-Host "Schwachstellen-ID: V-243081 Regel-ID: SV-243081r719486_rule STIG-ID: VCTR-67-000012"
Write-Host "Der vCenter Server muss die Integritätsprüfung des verteilten virtuellen Switches deaktivieren."
Get-View -ViewType DistributedVirtualSwitch | Where-Object { ($_.config.HealthCheckConfig | Where-Object { $_.enable -notmatch "False" }) } | ForEach-Object { $_.UpdateDVSHealthCheckConfig(@((New-Object Vmware.Vim.VMwareDVSVlanMtuHealthCheckConfig -property @{enable = 0 }), (New-Object Vmware.Vim.VMwareDVSTeamingHealthCheckConfig -property @{enable = 0 }))) }
$vds = Get-VDSwitch
$vds.ExtensionData.Config.HealthCheckConfig

Write-Host "Schwachstellen-ID: V-243077 Regel-ID: SV-243077r719474_rule STIG-ID: VCTR-67-00000"
Write-Host "Der vCenter Server muss Überkapazität, Bandbreite oder andere Redundanz verwalten, um die Auswirkungen von Informationsfluten und DoS-Angriffen zu begrenzen, indem Network I/O Control (NIOC) aktiviert wird."
Write-Host "Ein fehlender oder nicht aktivierter Alarm für Syslog-Fehler ist ein Befund."
ForEach ($vdswitch in (Get-VDSwitch.name)){
    (Get-VDSwitch $vdswitch | Get-View).EnableNetworkResourceManagement($true)
}
Get-VDSwitch | Select-Object Name, @{N = "NIOC Enabled"; E = { $_.ExtensionData.config.NetworkResourceManagementEnabled } }

#Manuelle Prüfung

Write-Host "Schwachstellen-ID: V-243076 Regel-ID: SV-243076r719471_rule STIG-ID: VCTR-67-000005"
Write-Host "Den Benutzern des vCenter Servers müssen die richtigen Rollen zugewiesen sein."
Write-Host "Erforderliche Berechtigungen für Dienstkonten und Benutzer müssen dokumentiert sein.
Hat ein Benutzer oder Dienstkonto mehr Rechte als nötig, liegt ein Befund vor."
Get-VIPermission | Sort-Object Role | Select-Object Role, Principal, Entity, Propagate, IsGroup | Format-Table -Auto

Write-Host "Schwachstellen-ID: V-243119 Regel-ID: SV-243119r719600_rule STIG-ID: VCTR-67-000064"
Write-Host "Hat eine andere Rolle als Administrator oder eine standortspezifische Gruppe eine dieser Berechtigungen, liegt ein Befund vor."
$roles = Get-VIRole
ForEach ($role in $roles) {
    $privileges = $role.PrivilegeList
    If ($privileges -match "Crypto*" -or $privileges -match "Global.Diagnostics" -or $privileges -match "Host.Inventory.Add*" -or $privileges -match "Host.Local operations.Manage user groups") {
        Write-Host "$role verfügt über kryptografische Berechtigungen"
    }
}

Write-Host "Schwachstellen-ID: V-243118 Regel-ID: SV-243118r719597_rule STIG-ID: VCTR-67-000063"
Write-Host "Haben andere Benutzer als Solution Users die Rolle "Administrator", ohne ausdrücklich für kryptografische Vorgänge bestimmt zu sein, liegt ein Befund vor."
Get-VIPermission | Where-Object { $_.Role -eq "Admin" } | Select-Object Role, Principal, Entity, Propagate, IsGroup | Format-Table -Auto


Write-Host "Schwachstellen-ID: V-243111 Regel-ID: SV-243111r719576_rule STIG-ID: VCTR-67-000055"
Write-Host "Nicht zutreffend, wenn kein vSAN-Cluster aktiviert ist."
Write-host "Ist vSAN aktiviert und heißt der Datenspeicher 'vsanDatastore', liegt ein Befund vor."
If ($(Get-Cluster | Where-Object { $_.VsanEnabled } | Measure-Object).Count -gt 0) {
    Write-Host "Aktivierter vSAN-Cluster gefunden"
    $Clusters = Get-Cluster | Where-Object { $_.VsanEnabled } 
    Foreach ($clus in $clusters) {
        $clus | Get-Datastore | Where-Object { $_.type -match "vsan" } | Set-Datastore -Name $(($clus.name) + "_vSAN_Datastore")
    }
}
else {
    Write-Host "vSAN ist nicht aktiviert; dieser Befund ist nicht zutreffend"
}

Write-Host "Hat ein Benutzer oder Dienstkonto mehr Rechte als nötig, liegt ein Befund vor."
Get-VIPermission | Sort-Object Role | Select-Object Role, Principal, Entity, Propagate, IsGroup | Format-Table -Auto

Write-Host "Schwachstellen-ID: V-243088 Regel-ID: SV-243088r719507_rule STIG-ID: VCTR-67-000020"
Write-Host "Prüfen Sie die VLAN-Tags der Portgruppe und stellen Sie sicher, dass keine reservierte VLAN-ID verwendet wird."
Write-Host "Bestimmte physische Switches reservieren VLAN-IDs für interne Zwecke und blockieren häufig entsprechend konfigurierten Datenverkehr. Cisco Catalyst reserviert zum Beispiel meist die VLANs 1001–1024 und 4094, Nexus meist 3968–4047 und 4094."
Get-VDPortgroup | Select-Object Name, VlanConfiguration

Write-Host "Schwachstellen-ID: V-243087 Regel-ID: SV-243087r719504_rule STIG-ID: VCTR-67-000019"
Write-Host "Ist eine Portgruppe als 'VLAN Trunk' konfiguriert und keine erforderliche Ausnahme (etwa für NSX-Appliances) dokumentiert, liegt ein Befund vor.
Ist VLAN-Trunking erlaubt, aber nicht auf den kleinstmöglichen erforderlichen Bereich begrenzt, liegt ein Befund vor."
Get-VDPortgroup | Where-Object { $_.ExtensionData.Config.Uplink -ne "True" } | Select-Object Name, VlanConfiguration

Write-Host "Schwachstellen-ID: V-243078 Regel-ID: SV-243078r719644_rule STIG-ID: VCTR-67-000008"
Write-Host "Der vCenter Server muss SA und ISSO mindestens in Echtzeit sofort über alle Auditfehler alarmieren."
Write-Host "Ein fehlender oder nicht aktivierter Alarm für Syslog-Fehler ist ein Befund."
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

#Quelle: https://github.com/rlakey/vmware-stig-powercli/blob/master/VMware_vSphere_6.7_VM_STIG_Remediation.ps1
$vmconfig = @{
    #Härtungs-/STIG-Einstellungen
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
    Write-Output "...Erweiterte Einstellungen auf $vm in $vcenter korrigieren"
    ForEach ($setting in ($vmconfig.vmAdvSettings.GetEnumerator() | Sort-Object Name)) {
        #Werte für jede angegebene Einstellung abrufen
        $settingname = $setting.name
        $settingvalue = $setting.value
        If ($asetting = $vm | Get-AdvancedSetting -Name $settingname) {
            If ($asetting.value -eq $settingvalue) {
                Write-Output "...Einstellung $settingname auf $vm ist bereits korrekt auf $settingvalue gesetzt"
            }
            else {
                Write-Output "...Einstellung $settingname auf $vm war falsch auf $($asetting.value) gesetzt; setze auf $settingvalue"
                $asetting | Set-AdvancedSetting -Value $settingvalue -Confirm:$false
            }
        }
        else {
            Write-Output "...Einstellung $settingname ist auf $vm nicht vorhanden; erstelle sie..."
            $vm | New-AdvancedSetting -Name $settingname -Value $settingvalue -Confirm:$false
        }
        Write-Output "...Erweiterte Einstellungen auf $vm in $vcenter bei Bedarf entfernen"
        ForEach ($setting in ($vmconfig.vmAdvSettingsRemove | Sort-Object Name)) {
            #Prüfen, ob die aktuelle Einstellung vorhanden ist
            If ($asetting = $vm | Get-AdvancedSetting -Name $setting) {
                Write-Output "...Einstellung $setting ist auf $vm vorhanden...entferne Einstellung"
                $asetting | Remove-AdvancedSetting -Confirm:$false
            }
            else {
                Write-Output "...Einstellung $setting ist auf $vm nicht vorhanden"
            }
        }   
        If ($vm.extensiondata.Config.MigrateEncryption -eq $vmconfig.vmotionEncryption) {
            Write-Output "...vMotion-Verschlüsselung ist auf $vm korrekt auf $($vmconfig.vmotionEncryption) gesetzt"
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

- **Das DoD-STIG-VIB [war früher für Versionen 5.0 bis 6.7 verfügbar](https://flings.vmware.com/dod-security-technical-implementation-guide-stig-esxi-vib), ist aber nicht mehr erhältlich.**
- [Ryan Lakey](https://core.vmware.com/users/ryan-lakey) bietet hilfreiche Hinweise zur Umsetzung der DoD-VMware-STIGs. Diese Ressourcen sind eine gute Ergänzung.
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
