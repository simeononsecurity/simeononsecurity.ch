---
title: "Padroneggiare la sicurezza VMware"
date: 2023-08-03
lastmod: 2026-11-13
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

#Connettiti a ogni server vCenter
ForEach ($vc in $vcenters) {
    Connect-VIServer -Server $vc
}

#Automatizzato

Write-Host "ID della vulnerabilità: V-243098 ID della regola: SV-243098r719537_rule ID STIG: VCTR-67-000036"
Write-Host "Se il valore di 'config.log.level' non è impostato su "info" o non esiste, è una violazione."
ForEach ($vc in $vcenters) {
    Get-AdvancedSetting -Entity $vc -Name config.log.level | Set-AdvancedSetting -Value info
    Get-AdvancedSetting -Entity $vc -Name config.log.level
}

Write-Host "ID della vulnerabilità: V-243090 ID della regola: SV-243090r719513_rule ID STIG: VCTR-67-000024"
Write-Host "Se 'config.vpxd.hostPasswordLength' ha un valore diverso da "32", è una violazione.
Se l'impostazione non esiste, non è una violazione."
ForEach ($vc in $vcenters) {
    Get-AdvancedSetting -Entity $vc -Name config.vpxd.hostPasswordLength | Set-AdvancedSetting -Value 32
    Get-AdvancedSetting -Entity $vc -Name config.vpxd.hostPasswordLength
}


Write-Host "ID della vulnerabilità: V-243089 ID della regola: SV-243089r719510_rule ID STIG: VCTR-67-000023"
Write-Host "Se 'VirtualCenter.VimPasswordExpirationInDays' ha un valore diverso da "30" o non esiste, è una violazione."
ForEach ($vc in $vcenters) {
    Try {
        Get-AdvancedSetting -Entity $vc -Name VirtualCenter.VimPasswordExpirationInDays | Set-AdvancedSetting -Value 30
    }
    Catch {
        New-AdvancedSetting -Entity $vc -Name VirtualCenter.VimPasswordExpirationInDays -Value 30
    }
}

Write-Host "ID della vulnerabilità: V-243084 ID della regola: SV-243085r719498_rule ID STIG: VCTR-67-000016"
Write-Host "Se NetFlow è configurato e l’IP del collector non è noto e documentato, è una violazione."
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

Write-Host "ID della vulnerabilità: V-243084 ID della regola: SV-243084r719495_rule ID STIG: VCTR-67-000015"
Write-Host "Il server vCenter deve impostare su rifiuta la policy Promiscuous Mode del gruppo di porte distribuito."
Get-VDSwitch | Get-VDSecurityPolicy | Set-VDSecurityPolicy -AllowPromiscuous $false
Get-VDPortgroup | Where-Object { $_.IsUplink -eq $false } | Get-VDSecurityPolicy | Set-VDSecurityPolicy -AllowPromiscuous $false
Get-VDSwitch | Get-VDSecurityPolicy
Get-VDPortgroup | Where-Object { $_.IsUplink -eq $false } | Get-VDSecurityPolicy


Write-Host "ID della vulnerabilità: V-243083 ID della regola: SV-243083r719492_rule ID STIG: VCTR-67-000014"
Write-Host "Il server vCenter deve impostare su rifiuta la policy MAC Address Change del gruppo di porte distribuito."
Get-VDSwitch | Get-VDSecurityPolicy | Set-VDSecurityPolicy -MacChanges $false
Get-VDPortgroup | Where-Object { $_.IsUplink -eq $false } | Get-VDSecurityPolicy | Set-VDSecurityPolicy -MacChanges $false
Get-VDPortgroup | Where-Object { $_.IsUplink -eq $false } | Get-VDSecurityPolicy

Write-Host "ID della vulnerabilità: V-243082 ID della regola: SV-243082r719489_rule ID STIG: VCTR-67-000013"
Write-Host "Il server vCenter deve impostare su rifiuta la policy Forged Transmits del gruppo di porte distribuito."
Get-VDSwitch | Get-VDSecurityPolicy | Set-VDSecurityPolicy -ForgedTransmits $false
Get-VDPortgroup | Where-Object { $_.IsUplink -eq $false } | Get-VDSecurityPolicy | Set-VDSecurityPolicy -ForgedTransmits $false
Get-VDSwitch | Get-VDSecurityPolicy
Get-VDPortgroup | Where-Object { $_.IsUplink -eq $false } | Get-VDSecurityPolicy

Write-Host "ID della vulnerabilità: V-243081 ID della regola: SV-243081r719486_rule ID STIG: VCTR-67-000012"
Write-Host "Il server vCenter deve disabilitare il controllo di integrità dello switch virtuale distribuito."
Get-View -ViewType DistributedVirtualSwitch | Where-Object { ($_.config.HealthCheckConfig | Where-Object { $_.enable -notmatch "False" }) } | ForEach-Object { $_.UpdateDVSHealthCheckConfig(@((New-Object Vmware.Vim.VMwareDVSVlanMtuHealthCheckConfig -property @{enable = 0 }), (New-Object Vmware.Vim.VMwareDVSTeamingHealthCheckConfig -property @{enable = 0 }))) }
$vds = Get-VDSwitch
$vds.ExtensionData.Config.HealthCheckConfig

Write-Host "ID della vulnerabilità: V-243077 ID della regola: SV-243077r719474_rule ID STIG: VCTR-67-00000"
Write-Host "Il server vCenter deve gestire capacità, larghezza di banda o ridondanza aggiuntive per limitare gli effetti di inondazioni informative e attacchi DoS, abilitando Network I/O Control (NIOC)."
Write-Host "La mancata creazione e attivazione di un allarme per gli errori syslog è una violazione."
ForEach ($vdswitch in (Get-VDSwitch.name)){
    (Get-VDSwitch $vdswitch | Get-View).EnableNetworkResourceManagement($true)
}
Get-VDSwitch | Select-Object Name, @{N = "NIOC Enabled"; E = { $_.ExtensionData.config.NetworkResourceManagementEnabled } }

#Revisione manuale

Write-Host "ID della vulnerabilità: V-243076 ID della regola: SV-243076r719471_rule ID STIG: VCTR-67-000005"
Write-Host "Agli utenti del server vCenter devono essere assegnati i ruoli corretti."
Write-Host "I privilegi richiesti per account di servizio e utenti devono essere documentati.
Se un utente o un account di servizio ha più privilegi del necessario, è una violazione."
Get-VIPermission | Sort-Object Role | Select-Object Role, Principal, Entity, Propagate, IsGroup | Format-Table -Auto

Write-Host "ID della vulnerabilità: V-243119 ID della regola: SV-243119r719600_rule ID STIG: VCTR-67-000064"
Write-Host "Se un ruolo diverso da Administrator o un gruppo specifico del sito dispone di una di queste autorizzazioni, è una violazione."
$roles = Get-VIRole
ForEach ($role in $roles) {
    $privileges = $role.PrivilegeList
    If ($privileges -match "Crypto*" -or $privileges -match "Global.Diagnostics" -or $privileges -match "Host.Inventory.Add*" -or $privileges -match "Host.Local operations.Manage user groups") {
        Write-Host "$role dispone di privilegi crittografici"
    }
}

Write-Host "ID della vulnerabilità: V-243118 ID della regola: SV-243118r719597_rule ID STIG: VCTR-67-000063"
Write-Host "Se utenti diversi da Solution Users hanno il ruolo "Administrator" senza essere designati esplicitamente per operazioni crittografiche, è una violazione."
Get-VIPermission | Where-Object { $_.Role -eq "Admin" } | Select-Object Role, Principal, Entity, Propagate, IsGroup | Format-Table -Auto


Write-Host "ID della vulnerabilità: V-243111 ID della regola: SV-243111r719576_rule ID STIG: VCTR-67-000055"
Write-Host "Non applicabile se non è abilitato alcun cluster vSAN."
Write-host "Se vSAN è abilitato e il datastore si chiama 'vsanDatastore', è una violazione."
If ($(Get-Cluster | Where-Object { $_.VsanEnabled } | Measure-Object).Count -gt 0) {
    Write-Host "Trovato un cluster vSAN abilitato"
    $Clusters = Get-Cluster | Where-Object { $_.VsanEnabled } 
    Foreach ($clus in $clusters) {
        $clus | Get-Datastore | Where-Object { $_.type -match "vsan" } | Set-Datastore -Name $(($clus.name) + "_vSAN_Datastore")
    }
}
else {
    Write-Host "vSAN non è abilitato; questa violazione non è applicabile"
}

Write-Host "Se un utente o un account di servizio ha più privilegi del necessario, è una violazione."
Get-VIPermission | Sort-Object Role | Select-Object Role, Principal, Entity, Propagate, IsGroup | Format-Table -Auto

Write-Host "ID della vulnerabilità: V-243088 ID della regola: SV-243088r719507_rule ID STIG: VCTR-67-000020"
Write-Host "Controlla i tag VLAN del gruppo di porte e verifica che non usino un ID VLAN riservato."
Write-Host "Alcuni switch fisici riservano ID VLAN per uso interno e spesso bloccano il traffico configurato con questi valori. Per esempio, gli switch Cisco Catalyst riservano in genere le VLAN 1001–1024 e 4094, mentre i Nexus riservano 3968–4047 e 4094."
Get-VDPortgroup | Select-Object Name, VlanConfiguration

Write-Host "ID della vulnerabilità: V-243087 ID della regola: SV-243087r719504_rule ID STIG: VCTR-67-000019"
Write-Host "Se un gruppo di porte è configurato come 'VLAN Trunk' senza un’eccezione necessaria documentata (come per le appliance NSX), è una violazione.
Se il trunking VLAN è autorizzato ma non è limitato all’intervallo minimo necessario, è una violazione."
Get-VDPortgroup | Where-Object { $_.ExtensionData.Config.Uplink -ne "True" } | Select-Object Name, VlanConfiguration

Write-Host "ID della vulnerabilità: V-243078 ID della regola: SV-243078r719644_rule ID STIG: VCTR-67-000008"
Write-Host "Il server vCenter deve inviare un avviso immediato in tempo reale a SA e ISSO per tutti gli errori di audit."
Write-Host "La mancata creazione e attivazione di un allarme per gli errori syslog è una violazione."
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

#Fonte: https://github.com/rlakey/vmware-stig-powercli/blob/master/VMware_vSphere_6.7_VM_STIG_Remediation.ps1
$vmconfig = @{
    #Impostazioni di hardening/STIG
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
    Write-Output "...Correzione delle impostazioni avanzate su $vm in $vcenter"
    ForEach ($setting in ($vmconfig.vmAdvSettings.GetEnumerator() | Sort-Object Name)) {
        #Recupera i valori per ogni impostazione indicata
        $settingname = $setting.name
        $settingvalue = $setting.value
        If ($asetting = $vm | Get-AdvancedSetting -Name $settingname) {
            If ($asetting.value -eq $settingvalue) {
                Write-Output "...L’impostazione $settingname su $vm è già configurata correttamente su $settingvalue"
            }
            else {
                Write-Output "...L’impostazione $settingname su $vm era impostata in modo errato su $($asetting.value); la imposto su $settingvalue"
                $asetting | Set-AdvancedSetting -Value $settingvalue -Confirm:$false
            }
        }
        else {
            Write-Output "...L’impostazione $settingname non esiste su $vm; creazione..."
            $vm | New-AdvancedSetting -Name $settingname -Value $settingvalue -Confirm:$false
        }
        Write-Output "...Rimozione delle impostazioni avanzate su $vm in $vcenter se necessario"
        ForEach ($setting in ($vmconfig.vmAdvSettingsRemove | Sort-Object Name)) {
            #Verifica se l’impostazione corrente esiste
            If ($asetting = $vm | Get-AdvancedSetting -Name $setting) {
                Write-Output "...L’impostazione $setting esiste su $vm...rimozione"
                $asetting | Remove-AdvancedSetting -Confirm:$false
            }
            else {
                Write-Output "...L’impostazione $setting non esiste su $vm"
            }
        }   
        If ($vm.extensiondata.Config.MigrateEncryption -eq $vmconfig.vmotionEncryption) {
            Write-Output "...La crittografia vMotion è impostata correttamente su $vm su $($vmconfig.vmotionEncryption)"
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

- **Il VIB STIG del DoD [era disponibile per le versioni dalla 5.0 alla 6.7](https://flings.vmware.com/dod-security-technical-implementation-guide-stig-esxi-vib), ma non è più disponibile.**
- [Ryan Lakey](https://core.vmware.com/users/ryan-lakey) offre indicazioni utili per applicare gli STIG DoD a VMware. Ti consigliamo di leggerle.
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
