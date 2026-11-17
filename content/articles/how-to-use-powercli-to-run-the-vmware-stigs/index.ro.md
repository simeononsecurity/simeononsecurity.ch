---
title: "Stăpânește securitatea VMware"
date: 2023-08-03
lastmod: 2026-11-13
toc: true
draft: false
description: "În acest ghid cuprinzător, află cum să folosești PowerCLI pentru a aplica STIG-urile VMware și a securiza mediul VMware."
genre: ["Securitate cibernetică", "Virtualizare", "Infrastructură IT", "Automatizare", "PowerShell", "VMware", "STIG", "Conformitate", "Scripting", "Centru de date"]
tags: ["PowerCLI", "STIG VMware", "securitate VMware", "automatizare", "scripting", "PowerShell", "ESXi", "virtualizare", "conformitate", "securitate cibernetică", "cum să folosești PowerCLI pentru STIG-urile VMware", "automatizarea securității VMware cu PowerCLI", "script PowerCLI pentru aplicarea STIG VMware", "automatizare PowerCLI pentru securitatea ESXi", "securizarea unui mediu VMware cu PowerCLI"]
cover: "/img/cover/An_illustration_depicting_a_computer_server_sh.webp"
coverAlt: "Ilustrație a unui server de computer protejat cu un lacăt, simbolizând o infrastructură VMware securizată."
coverCaption: "Folosește PowerCLI pentru a securiza mediul VMware"
---

**Cum aplici STIG-urile VMware cu PowerCLI**

PowerCLI este un instrument de automatizare și scripting care permite administrarea și configurarea mediilor VMware cu PowerShell. Acest articol explică modul în care poți folosi PowerCLI pentru a aplica VMware STIG (Security Technical Implementation Guide) pe ESXi și pe mașinile virtuale.

## Introducere

**VMware STIG** oferă îndrumări și recomandări pentru configurarea și administrarea în siguranță a infrastructurii VMware. Respectarea lor ajută organizațiile să îmbunătățească securitatea implementărilor VMware și să îndeplinească cerințele guvernamentale aplicabile, precum **STIG-ul Defense Information Systems Agency (DISA)**.

## Ce este PowerCLI?

**PowerCLI** este o interfață de linie de comandă și un instrument de scripting pentru administrarea mediilor VMware. Se bazează pe PowerShell și oferă numeroase cmdlet-uri create special pentru administrarea VMware. Administratorii îl folosesc pentru a automatiza sarcini repetitive, a modifica setări și a colecta informații din infrastructura VMware.

### Instalare și cerințe

Înainte de a începe cu PowerCLI și VMware STIG, verifică următoarele cerințe preliminare:

- [**PowerCLI 11.3**](https://www.powershellgallery.com/packages/VMware.PowerCLI/11.3.0.13990089): instalează PowerCLI din PowerShell Gallery cu comanda `Install-Module VMware.PowerCLI -force`.
- [**PowerShell 5 sau o versiune mai nouă**](https://docs.microsoft.com/en-us/skypeforbusiness/set-up-your-computer-for-windows-powershell/download-and-install-windows-powershell-5-1): verifică dacă este instalat PowerShell 5 sau mai nou.
- [**ESXi 6.7 U2 sau o versiune mai nouă**](https://my.vmware.com/web/vmware/downloads/details?downloadGroup=ESXI670&productId=742): folosește ESXi 6.7 U2 sau mai nou.

## Automatizarea VMware VCSA STIG

VMware ESXi STIG oferă îndrumări pentru securizarea gazdelor ESXi. Automatizarea aplicării controalelor STIG simplifică procesul și păstrează o configurație consecventă pe mai multe gazde.

### Aspecte de luat în considerare

Înainte de automatizare, ține cont de următoarele:

- **Asigură-te că nicio mașină virtuală sau niciun sistem invitat de pe gazda ori clusterul ESXi nu are nevoie de funcțiile CD, USB sau dischetă.**
- **Aplică STIG pe toate gazdele ESXi și sistemele invitate conectate la vCenter.**
- **Ai nevoie de competențe de depanare pentru a rezolva problemele apărute în timpul procesului.**

### Script: automatizarea VMware VCSA STIG

Următorul script PowerCLI automatizează aplicarea unor controale STIG selectate pentru VCSA:

```powershell
Set-PowerCLIConfiguration -InvalidCertificateAction Ignore -Confirm:$false
Set-PowerCLIConfiguration -Scope User -ParticipateInCEIP $false -Confirm:$false
$vcenters = 127.0.0.1, 127.0.0.2

#Conectează-te la fiecare server vCenter
ForEach ($vc in $vcenters) {
    Connect-VIServer -Server $vc
}

#Automatizat

Write-Host "ID-ul vulnerabilității: V-243098 ID-ul regulii: SV-243098r719537_rule ID STIG: VCTR-67-000036"
Write-Host "Dacă valoarea 'config.log.level' nu este setată la "info" sau nu există, aceasta este o constatare."
ForEach ($vc in $vcenters) {
    Get-AdvancedSetting -Entity $vc -Name config.log.level | Set-AdvancedSetting -Value info
    Get-AdvancedSetting -Entity $vc -Name config.log.level
}

Write-Host "ID-ul vulnerabilității: V-243090 ID-ul regulii: SV-243090r719513_rule ID STIG: VCTR-67-000024"
Write-Host "Dacă 'config.vpxd.hostPasswordLength' are o valoare diferită de "32", aceasta este o constatare.
Dacă setarea nu există, nu este o constatare."
ForEach ($vc in $vcenters) {
    Get-AdvancedSetting -Entity $vc -Name config.vpxd.hostPasswordLength | Set-AdvancedSetting -Value 32
    Get-AdvancedSetting -Entity $vc -Name config.vpxd.hostPasswordLength
}


Write-Host "ID-ul vulnerabilității: V-243089 ID-ul regulii: SV-243089r719510_rule ID STIG: VCTR-67-000023"
Write-Host "Dacă 'VirtualCenter.VimPasswordExpirationInDays' are o valoare diferită de "30" sau nu există, aceasta este o constatare."
ForEach ($vc in $vcenters) {
    Try {
        Get-AdvancedSetting -Entity $vc -Name VirtualCenter.VimPasswordExpirationInDays | Set-AdvancedSetting -Value 30
    }
    Catch {
        New-AdvancedSetting -Entity $vc -Name VirtualCenter.VimPasswordExpirationInDays -Value 30
    }
}

Write-Host "ID-ul vulnerabilității: V-243084 ID-ul regulii: SV-243085r719498_rule ID STIG: VCTR-67-000016"
Write-Host "Dacă NetFlow este configurat, iar IP-ul colectorului nu este cunoscut și documentat, aceasta este o constatare."
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

Write-Host "ID-ul vulnerabilității: V-243084 ID-ul regulii: SV-243084r719495_rule ID STIG: VCTR-67-000015"
Write-Host "Serverul vCenter trebuie să seteze politica Promiscuous Mode a grupului de porturi distribuit la respingere."
Get-VDSwitch | Get-VDSecurityPolicy | Set-VDSecurityPolicy -AllowPromiscuous $false
Get-VDPortgroup | Where-Object { $_.IsUplink -eq $false } | Get-VDSecurityPolicy | Set-VDSecurityPolicy -AllowPromiscuous $false
Get-VDSwitch | Get-VDSecurityPolicy
Get-VDPortgroup | Where-Object { $_.IsUplink -eq $false } | Get-VDSecurityPolicy


Write-Host "ID-ul vulnerabilității: V-243083 ID-ul regulii: SV-243083r719492_rule ID STIG: VCTR-67-000014"
Write-Host "Serverul vCenter trebuie să seteze politica MAC Address Change a grupului de porturi distribuit la respingere."
Get-VDSwitch | Get-VDSecurityPolicy | Set-VDSecurityPolicy -MacChanges $false
Get-VDPortgroup | Where-Object { $_.IsUplink -eq $false } | Get-VDSecurityPolicy | Set-VDSecurityPolicy -MacChanges $false
Get-VDPortgroup | Where-Object { $_.IsUplink -eq $false } | Get-VDSecurityPolicy

Write-Host "ID-ul vulnerabilității: V-243082 ID-ul regulii: SV-243082r719489_rule ID STIG: VCTR-67-000013"
Write-Host "Serverul vCenter trebuie să seteze politica Forged Transmits a grupului de porturi distribuit la respingere."
Get-VDSwitch | Get-VDSecurityPolicy | Set-VDSecurityPolicy -ForgedTransmits $false
Get-VDPortgroup | Where-Object { $_.IsUplink -eq $false } | Get-VDSecurityPolicy | Set-VDSecurityPolicy -ForgedTransmits $false
Get-VDSwitch | Get-VDSecurityPolicy
Get-VDPortgroup | Where-Object { $_.IsUplink -eq $false } | Get-VDSecurityPolicy

Write-Host "ID-ul vulnerabilității: V-243081 ID-ul regulii: SV-243081r719486_rule ID STIG: VCTR-67-000012"
Write-Host "Serverul vCenter trebuie să dezactiveze verificarea de sănătate a comutatorului virtual distribuit."
Get-View -ViewType DistributedVirtualSwitch | Where-Object { ($_.config.HealthCheckConfig | Where-Object { $_.enable -notmatch "False" }) } | ForEach-Object { $_.UpdateDVSHealthCheckConfig(@((New-Object Vmware.Vim.VMwareDVSVlanMtuHealthCheckConfig -property @{enable = 0 }), (New-Object Vmware.Vim.VMwareDVSTeamingHealthCheckConfig -property @{enable = 0 }))) }
$vds = Get-VDSwitch
$vds.ExtensionData.Config.HealthCheckConfig

Write-Host "ID-ul vulnerabilității: V-243077 ID-ul regulii: SV-243077r719474_rule ID STIG: VCTR-67-00000"
Write-Host "Serverul vCenter trebuie să gestioneze capacitatea suplimentară, lățimea de bandă sau alte redundanțe pentru a limita efectele atacurilor DoS prin inundarea cu informații, activând Network I/O Control (NIOC)."
Write-Host "Dacă nu este creată și activată o alertă pentru eșecurile syslog, aceasta este o constatare."
ForEach ($vdswitch in (Get-VDSwitch.name)){
    (Get-VDSwitch $vdswitch | Get-View).EnableNetworkResourceManagement($true)
}
Get-VDSwitch | Select-Object Name, @{N = "NIOC Enabled"; E = { $_.ExtensionData.config.NetworkResourceManagementEnabled } }

#Revizuire manuală

Write-Host "ID-ul vulnerabilității: V-243076 ID-ul regulii: SV-243076r719471_rule ID STIG: VCTR-67-000005"
Write-Host "Utilizatorii serverului vCenter trebuie să aibă rolurile corecte atribuite."
Write-Host "Privilegiile necesare conturilor de serviciu și utilizatorilor trebuie documentate.
Dacă un utilizator sau un cont de serviciu are mai multe privilegii decât este necesar, aceasta este o constatare."
Get-VIPermission | Sort-Object Role | Select-Object Role, Principal, Entity, Propagate, IsGroup | Format-Table -Auto

Write-Host "ID-ul vulnerabilității: V-243119 ID-ul regulii: SV-243119r719600_rule ID STIG: VCTR-67-000064"
Write-Host "Dacă orice rol în afară de Administrator sau orice grup specific site-ului are aceste permisiuni, aceasta este o constatare."
$roles = Get-VIRole
ForEach ($role in $roles) {
    $privileges = $role.PrivilegeList
    If ($privileges -match "Crypto*" -or $privileges -match "Global.Diagnostics" -or $privileges -match "Host.Inventory.Add*" -or $privileges -match "Host.Local operations.Manage user groups") {
        Write-Host "$role are privilegii criptografice"
    }
}

Write-Host "ID-ul vulnerabilității: V-243118 ID-ul regulii: SV-243118r719597_rule ID STIG: VCTR-67-000063"
Write-Host "Dacă utilizatori diferiți de Solution Users au rolul „Administrator” fără să fie desemnați explicit pentru operațiuni criptografice, aceasta este o constatare."
Get-VIPermission | Where-Object { $_.Role -eq "Admin" } | Select-Object Role, Principal, Entity, Propagate, IsGroup | Format-Table -Auto


Write-Host "ID-ul vulnerabilității: V-243111 ID-ul regulii: SV-243111r719576_rule ID STIG: VCTR-67-000055"
Write-Host "Nu se aplică dacă nu este activat niciun cluster vSAN."
Write-host "Dacă vSAN este activat și depozitul de date se numește 'vsanDatastore', aceasta este o constatare."
If ($(Get-Cluster | Where-Object { $_.VsanEnabled } | Measure-Object).Count -gt 0) {
    Write-Host "A fost găsit un cluster vSAN activat"
    $Clusters = Get-Cluster | Where-Object { $_.VsanEnabled } 
    Foreach ($clus in $clusters) {
        $clus | Get-Datastore | Where-Object { $_.type -match "vsan" } | Set-Datastore -Name $(($clus.name) + "_vSAN_Datastore")
    }
}
else {
    Write-Host "vSAN nu este activat; această constatare nu se aplică"
}

Write-Host "Dacă un utilizator sau un cont de serviciu are mai multe privilegii decât este necesar, aceasta este o constatare."
Get-VIPermission | Sort-Object Role | Select-Object Role, Principal, Entity, Propagate, IsGroup | Format-Table -Auto

Write-Host "ID-ul vulnerabilității: V-243088 ID-ul regulii: SV-243088r719507_rule ID STIG: VCTR-67-000020"
Write-Host "Verificați etichetele VLAN ale grupului de porturi și confirmați că nu folosesc un ID VLAN rezervat."
Write-Host "Unele comutatoare fizice rezervă ID-uri VLAN pentru uz intern și blochează adesea traficul configurat cu aceste valori. De exemplu, Cisco Catalyst rezervă de obicei VLAN-urile 1001–1024 și 4094, iar Nexus rezervă 3968–4047 și 4094."
Get-VDPortgroup | Select-Object Name, VlanConfiguration

Write-Host "ID-ul vulnerabilității: V-243087 ID-ul regulii: SV-243087r719504_rule ID STIG: VCTR-67-000019"
Write-Host "Dacă un grup de porturi este configurat cu 'VLAN Trunk' fără o excepție necesară documentată (de exemplu, pentru dispozitive NSX), aceasta este o constatare.
Dacă trunking-ul VLAN este permis, dar nu este limitat la intervalul minim necesar, aceasta este o constatare."
Get-VDPortgroup | Where-Object { $_.ExtensionData.Config.Uplink -ne "True" } | Select-Object Name, VlanConfiguration

Write-Host "ID-ul vulnerabilității: V-243078 ID-ul regulii: SV-243078r719644_rule ID STIG: VCTR-67-000008"
Write-Host "Serverul vCenter trebuie să trimită imediat alerte în timp real către SA și ISSO pentru toate eșecurile de audit."
Write-Host "Dacă nu este creată și activată o alertă pentru eșecurile syslog, aceasta este o constatare."
Get-AlarmDefinition | Where-Object { $_.ExtensionData.Info.Expression.Expression.EventTypeId -eq "esx.problem.vmsyslogd.remote.failure" } | Select-Object Name, Enabled, @{N = "EventTypeId"; E = { $_.ExtensionData.Info.Expression.Expression.EventTypeId } }
```

Scriptul îndeplinește următoarele funcții:

- **Mai întâi configurează PowerCLI, dezactivează validarea certificatelor și renunță la participarea la Customer Experience Improvement Program (CEIP).**
- **Apoi se conectează la serverele vCenter indicate în variabila `$vcenters`.**
- **Aplică fiecare control STIG prin cmdlet-uri PowerCLI. De exemplu, setează `config.log.level` la info pentru serverele vCenter indicate.**
- **Abordează și controale precum `config.vpxd.hostPasswordLength` și `VirtualCenter.VimPasswordExpirationInDays`.**
- **La final verifică și configurează politicile de securitate și alte setări.**
- **Acesta este un script demonstrativ. Adaptează-l la mediul și cerințele tale STIG.**

______

## Automatizarea VMware VM STIG

Pe lângă gazdele ESXi, trebuie să aplici controale STIG și pe mașinile virtuale din infrastructura VMware. PowerCLI te ajută să automatizezi configurarea VM-urilor conform îndrumărilor STIG.

## Script: automatizarea VMware VM STIG

Următorul script PowerCLI arată cum poți automatiza controale STIG selectate pentru mașini virtuale:

```powershell
Set-PowerCLIConfiguration -InvalidCertificateAction Ignore -Confirm:$false
Set-PowerCLIConfiguration -Scope User -ParticipateInCEIP $false -Confirm:$false
Connect-VIServer -Server 127.0.0.1
$cluster = Get-Cluster -Name "Cluster"
$folder = Get-Folder -Name "Folder"

#Sursă: https://github.com/rlakey/vmware-stig-powercli/blob/master/VMware_vSphere_6.7_VM_STIG_Remediation.ps1
$vmconfig = @{
    #Setări de consolidare/STIG
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
    Write-Output "...Se remediază setările avansate pe $vm în $vcenter"
    ForEach ($setting in ($vmconfig.vmAdvSettings.GetEnumerator() | Sort-Object Name)) {
        #Preia valorile pentru fiecare setare specificată
        $settingname = $setting.name
        $settingvalue = $setting.value
        If ($asetting = $vm | Get-AdvancedSetting -Name $settingname) {
            If ($asetting.value -eq $settingvalue) {
                Write-Output "...Setarea $settingname este deja configurată corect la $settingvalue pe $vm"
            }
            else {
                Write-Output "...Setarea $settingname avea valoarea incorectă $($asetting.value) pe $vm; se setează la $settingvalue"
                $asetting | Set-AdvancedSetting -Value $settingvalue -Confirm:$false
            }
        }
        else {
            Write-Output "...Setarea $settingname nu există pe $vm; se creează..."
            $vm | New-AdvancedSetting -Name $settingname -Value $settingvalue -Confirm:$false
        }
        Write-Output "...Se elimină setările avansate de pe $vm în $vcenter dacă este necesar"
        ForEach ($setting in ($vmconfig.vmAdvSettingsRemove | Sort-Object Name)) {
            #Verifică dacă există setarea curentă
            If ($asetting = $vm | Get-AdvancedSetting -Name $setting) {
                Write-Output "...Setarea $setting există pe $vm...se elimină"
                $asetting | Remove-AdvancedSetting -Confirm:$false
            }
            else {
                Write-Output "...Setarea $setting nu există pe $vm"
            }
        }   
        If ($vm.extensiondata.Config.MigrateEncryption -eq $vmconfig.vmotionEncryption) {
            Write-Output "...Criptarea vMotion este configurată corect pe $vm la $($vmconfig.vmotionEncryption)"
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

Scriptul îndeplinește următoarele funcții:

- **La fel ca scriptul VMware VCSA STIG, configurează mediul PowerCLI la început.**
- **Se conectează la vCenter și selectează clusterul și folderul în care se află mașinile virtuale vizate.**
- **Variabila `$vmconfig` conține setările STIG pentru VM-uri. Include setări avansate, precum dezactivarea copierii și lipirii și limitarea conexiunilor de afișare la distanță.**
- **Trece prin fiecare VM din clusterul și folderul selectate și aplică setările STIG.**
- **Configurează și criptarea vMotion pentru VM-uri.**

Acest script este un exemplu. Modifică-l pentru mediul tău și cerințele STIG aplicabile.

_____

## Resurse suplimentare

- **VIB-ul DoD STIG [a fost disponibil anterior pentru versiunile 5.0–6.7](https://flings.vmware.com/dod-security-technical-implementation-guide-stig-esxi-vib), dar nu mai este disponibil.**
- [Ryan Lakey](https://core.vmware.com/users/ryan-lakey) oferă îndrumări utile pentru implementarea DoD VMware STIG. Îți recomandăm să le citești.
    - [VMware vSphere 8 STIG](https://core.vmware.com/resource/vmware-vsphere-8-stig)
    - [VMware vSphere 7 STIG](https://core.vmware.com/vsphere-7-stig)
    - [VMware vSphere 6.7 STIG](https://core.vmware.com/vmware-vsphere-67-stig)
    - [VMware STIG PowerCLI](https://github.com/rlakey/vmware-stig-powercli)
        - [Linia de bază VMware VCSA 6.7 STIG](https://github.com/rlakey/vmware-vcsa-6.7-stig-baseline)
        - [Linia de bază VMware VM 6.7 STIG](https://github.com/rlakey/vmware-vm-6.7-stig-baseline)
_____

## Concluzie

**Aplicarea VMware STIG contribuie la securizarea infrastructurii VMware și la respectarea cerințelor relevante. PowerCLI automatizează și simplifică aplicarea controalelor STIG pe gazdele ESXi și pe mașinile virtuale.**

Acest articol a prezentat utilizarea PowerCLI pentru automatizarea VMware ESXi STIG și VM STIG. A trecut în revistă cerințele de instalare, a inclus scripturi demonstrative și a evidențiat importanța adaptării lor la fiecare mediu.

**Cu PowerCLI și îndrumările STIG, administratorii pot securiza eficient implementările VMware, pot reduce munca manuală și pot menține configurații consecvente.**

## Referințe

- [VIB DoD STIG](https://flings.vmware.com/dod-security-technical-implementation-guide-stig-esxi-vib)
- [PowerCLI 11.3](https://www.powershellgallery.com/packages/VMware.PowerCLI/11.3.0.13990089)
- [PowerShell 5 sau o versiune mai nouă](https://docs.microsoft.com/en-us/skypeforbusiness/set-up-your-computer-for-windows-powershell/download-and-install-windows-powershell-5-1)
- [ESXi 6.7 U2 sau o versiune mai nouă](https://my.vmware.com/web/vmware/downloads/details?downloadGroup=ESXI670&productId=742)
