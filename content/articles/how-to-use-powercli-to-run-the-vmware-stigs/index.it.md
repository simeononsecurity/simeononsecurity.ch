---
title: "Padroneggiare la sicurezza VMware"
date: 2023-08-03
lastmod: 2026-11-12
toc: true
draft: false
description: "Scopri come usare PowerCLI per applicare gli STIG VMware e proteggere il tuo ambiente VMware con questa guida completa."
genre: ["Sicurezza informatica", "Virtualizzazione", "Infrastruttura IT", "Automazione", "PowerShell", "VMware", "STIG", "Conformità", "Scripting", "Data center"]
tags: ["PowerCLI", "STIG VMware", "sicurezza VMware", "automazione", "scripting", "PowerShell", "ESXi", "virtualizzazione", "conformità", "sicurezza informatica", "come usare PowerCLI per gli STIG VMware", "automatizzare la sicurezza VMware con PowerCLI", "script PowerCLI per applicare gli STIG VMware", "automazione PowerCLI per la sicurezza ESXi", "proteggere un ambiente VMware con PowerCLI"]
cover: "/img/cover/An_illustration_depicting_a_computer_server_sh.webp"
coverAlt: "Illustrazione di un server informatico protetto da un lucchetto, simbolo di un’infrastruttura VMware sicura."
coverCaption: "Usare PowerCLI per proteggere l’ambiente VMware"
---

**Applicare gli STIG VMware con PowerCLI**

PowerCLI è uno strumento di automazione e scripting che permette di gestire e configurare gli ambienti VMware con PowerShell. In questo articolo vediamo come usare PowerCLI per applicare il VMware STIG (Security Technical Implementation Guide) a ESXi e alle macchine virtuali.

## Introduzione

Il **VMware STIG** fornisce linee guida e raccomandazioni per configurare e gestire in modo sicuro l’infrastruttura VMware. Seguirlo aiuta le organizzazioni a migliorare la sicurezza delle implementazioni VMware e a rispettare i requisiti governativi applicabili, come lo **STIG della Defense Information Systems Agency (DISA)**.

## Che cos’è PowerCLI?

**PowerCLI** è un’interfaccia a riga di comando e uno strumento di scripting per amministrare gli ambienti VMware. Si basa su PowerShell e mette a disposizione numerosi cmdlet pensati per l’amministrazione VMware. Gli amministratori lo usano per automatizzare attività ripetitive, modificare configurazioni e raccogliere informazioni sull’infrastruttura VMware.

### Installazione e requisiti

Prima di iniziare con PowerCLI e VMware STIG, verifica questi prerequisiti:

- [**PowerCLI 11.3**](https://www.powershellgallery.com/packages/VMware.PowerCLI/11.3.0.13990089): installa PowerCLI da PowerShell Gallery con il comando `Install-Module VMware.PowerCLI -force`.
- [**PowerShell 5 o versioni successive**](https://docs.microsoft.com/en-us/skypeforbusiness/set-up-your-computer-for-windows-powershell/download-and-install-windows-powershell-5-1): verifica di avere PowerShell 5 o una versione successiva.
- [**ESXi 6.7 U2 o versioni successive**](https://my.vmware.com/web/vmware/downloads/details?downloadGroup=ESXI670&productId=742): usa ESXi 6.7 U2 o una versione successiva.

## Automatizzare lo STIG di VMware VCSA

Lo STIG VMware ESXi fornisce indicazioni per proteggere gli host ESXi. Automatizzare l’applicazione dei controlli STIG semplifica il processo e rende coerente la configurazione di più host.

### Aspetti da considerare

Prima di procedere con l’automazione, considera quanto segue:

- **Verifica che nessuna macchina virtuale o sistema guest sull’host o cluster ESXi richieda funzioni CD, USB o floppy.**
- **Applica gli STIG a tutti gli host ESXi e ai guest collegati a vCenter.**
- **Servono competenze di risoluzione dei problemi per gestire eventuali inconvenienti durante il processo.**

### Script: automazione dello STIG di VMware VCSA

Il seguente script PowerCLI automatizza l’applicazione di alcuni controlli STIG alle VCSA:

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

Lo script svolge queste funzioni:

- **All’inizio configura PowerCLI, disabilita la convalida dei certificati e disattiva la partecipazione al Customer Experience Improvement Program (CEIP).**
- **Poi si connette ai server vCenter specificati nella variabile `$vcenters`.**
- **Gestisce ogni controllo STIG con cmdlet PowerCLI. Per esempio, imposta `config.log.level` su info per i server vCenter indicati.**
- **Applica anche altri controlli, tra cui quelli relativi a `config.vpxd.hostPasswordLength` e `VirtualCenter.VimPasswordExpirationInDays`.**
- **Infine esamina e configura le policy di sicurezza e altre impostazioni.**
- **Questo script è un esempio. Adattalo all’ambiente e ai relativi requisiti STIG.**

______

## Automatizzare lo STIG delle macchine virtuali VMware

Oltre agli host ESXi, devi applicare i controlli STIG anche alle macchine virtuali dell’infrastruttura VMware. PowerCLI aiuta ad automatizzarne la configurazione secondo le linee guida STIG.

## Script: automazione dello STIG delle macchine virtuali VMware

Il seguente script PowerCLI mostra come automatizzare alcuni controlli STIG per le macchine virtuali:

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

Lo script svolge queste funzioni:

- **Come nello script STIG VMware VCSA, configura l’ambiente PowerCLI all’avvio.**
- **Si connette a vCenter e seleziona il cluster e la cartella in cui si trovano le macchine virtuali interessate.**
- **La variabile `$vmconfig` contiene le impostazioni STIG delle VM. Include impostazioni avanzate come la disattivazione di copia e incolla, la limitazione delle connessioni di visualizzazione remota e altro.**
- **Il ciclo applica le impostazioni STIG a ogni macchina virtuale nel cluster e nella cartella selezionati.**
- **Lo script gestisce anche la cifratura vMotion delle macchine virtuali.**

Lo script è un esempio. Modificalo in base al tuo ambiente e ai requisiti STIG applicabili.

_____

## Risorse aggiuntive

- **Il VIB STIG del DoD** [era disponibile per le versioni dalla 5.0 alla 6.7](https://flings.vmware.com/dod-security-technical-implementation-guide-stig-esxi-vib), ma non è più disponibile.
- **[Ryan Lakey](https://core.vmware.com/users/ryan-lakey)** offre indicazioni utili per applicare gli STIG DoD a VMware. Ti consigliamo di leggerle.
    - [STIG VMware vSphere 8](https://core.vmware.com/resource/vmware-vsphere-8-stig)
    - [STIG VMware vSphere 7](https://core.vmware.com/vsphere-7-stig)
    - [STIG VMware vSphere 6.7](https://core.vmware.com/vmware-vsphere-67-stig)
    - [PowerCLI STIG VMware](https://github.com/rlakey/vmware-stig-powercli)
        - [Baseline STIG VMware VCSA 6.7](https://github.com/rlakey/vmware-vcsa-6.7-stig-baseline)
        - [Baseline STIG VMware VM 6.7](https://github.com/rlakey/vmware-vm-6.7-stig-baseline)
_____

## Conclusione

**Applicare lo STIG VMware aiuta a proteggere l’infrastruttura VMware e a rispettare i requisiti applicabili. PowerCLI automatizza e semplifica l’applicazione dei controlli STIG agli host ESXi e alle macchine virtuali.**

Questo articolo ha illustrato come usare PowerCLI per automatizzare gli STIG VMware ESXi e VM. Abbiamo descritto i requisiti di installazione, fornito script di esempio e sottolineato l’importanza di adattarli alle esigenze del proprio ambiente.

**Con PowerCLI e seguendo le linee guida STIG, gli amministratori possono proteggere in modo efficiente le implementazioni VMware, ridurre il lavoro manuale e mantenere configurazioni coerenti.**

## Riferimenti

- [VIB STIG del DoD](https://flings.vmware.com/dod-security-technical-implementation-guide-stig-esxi-vib)
- [PowerCLI 11.3](https://www.powershellgallery.com/packages/VMware.PowerCLI/11.3.0.13990089)
- [PowerShell 5 o versioni successive](https://docs.microsoft.com/en-us/skypeforbusiness/set-up-your-computer-for-windows-powershell/download-and-install-windows-powershell-5-1)
- [ESXi 6.7 U2 o versioni successive](https://my.vmware.com/web/vmware/downloads/details?downloadGroup=ESXI670&productId=742)
