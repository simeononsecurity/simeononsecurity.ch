---
title: "Poznaj zabezpieczenia VMware"
date: 2023-08-03
lastmod: 2026-11-12
toc: true
draft: false
description: "W tym obszernym przewodniku dowiesz się, jak używać PowerCLI do wdrażania STIG VMware i zabezpieczania środowiska VMware."
genre: ["Cyberbezpieczeństwo", "Wirtualizacja", "Infrastruktura IT", "Automatyzacja", "PowerShell", "VMware", "STIG", "Zgodność", "Skrypty", "Centrum danych"]
tags: ["PowerCLI", "STIG VMware", "bezpieczeństwo VMware", "automatyzacja", "skrypty", "PowerShell", "ESXi", "wirtualizacja", "zgodność", "cyberbezpieczeństwo", "jak używać PowerCLI do STIG VMware", "automatyzacja bezpieczeństwa VMware za pomocą PowerCLI", "skrypt PowerCLI do wdrażania STIG VMware", "automatyzacja PowerCLI dla bezpieczeństwa ESXi", "zabezpieczanie środowiska VMware za pomocą PowerCLI"]
cover: "/img/cover/An_illustration_depicting_a_computer_server_sh.webp"
coverAlt: "Ilustracja serwera komputerowego chronionego kłódką, symbolizująca bezpieczną infrastrukturę VMware."
coverCaption: "Zabezpiecz środowisko VMware za pomocą PowerCLI"
---

**Jak stosować STIG VMware za pomocą PowerCLI**

PowerCLI to narzędzie do automatyzacji i skryptów, które pozwala zarządzać środowiskami VMware i konfigurować je za pomocą PowerShell. W tym artykule pokazujemy, jak używać PowerCLI do wdrażania VMware STIG (Security Technical Implementation Guide) na ESXi i maszynach wirtualnych.

## Wprowadzenie

**VMware STIG** zawiera wskazówki i zalecenia dotyczące bezpiecznej konfiguracji oraz zarządzania infrastrukturą VMware. Stosowanie tych zaleceń pomaga organizacjom zwiększyć bezpieczeństwo wdrożeń VMware i spełnić właściwe wymagania rządowe, takie jak **STIG Defense Information Systems Agency (DISA)**.

## Czym jest PowerCLI?

**PowerCLI** to interfejs wiersza poleceń i narzędzie skryptowe do zarządzania środowiskami VMware. Działa na bazie PowerShell i udostępnia wiele poleceń cmdlet przeznaczonych do administrowania VMware. Administratorzy automatyzują nim powtarzalne zadania, zmieniają konfigurację i zbierają informacje o infrastrukturze VMware.

### Instalacja i wymagania

Przed rozpoczęciem pracy z PowerCLI i VMware STIG sprawdź następujące wymagania:

- [**PowerCLI 11.3**](https://www.powershellgallery.com/packages/VMware.PowerCLI/11.3.0.13990089): zainstaluj PowerCLI z PowerShell Gallery poleceniem `Install-Module VMware.PowerCLI -force`.
- [**PowerShell 5 lub nowszy**](https://docs.microsoft.com/en-us/skypeforbusiness/set-up-your-computer-for-windows-powershell/download-and-install-windows-powershell-5-1): upewnij się, że masz PowerShell 5 lub nowszy.
- [**ESXi 6.7 U2 lub nowszy**](https://my.vmware.com/web/vmware/downloads/details?downloadGroup=ESXI670&productId=742): używaj ESXi 6.7 U2 lub nowszego.

## Automatyzacja VMware VCSA STIG

VMware ESXi STIG zawiera wskazówki dotyczące zabezpieczania hostów ESXi. Automatyzacja wdrażania kontroli STIG upraszcza proces i zapewnia spójną konfigurację na wielu hostach.

### Uwagi

Przed rozpoczęciem automatyzacji uwzględnij następujące kwestie:

- **Upewnij się, że żadna maszyna wirtualna ani system gościa na hoście lub klastrze ESXi nie wymaga napędu CD, USB ani dyskietek.**
- **Zastosuj STIG na wszystkich hostach ESXi i systemach gości powiązanych z vCenter.**
- **Przygotuj się do rozwiązywania problemów, które mogą wystąpić w trakcie procesu.**

### Skrypt: automatyzacja VMware VCSA STIG

Poniższy skrypt PowerCLI automatyzuje wdrożenie wybranych kontroli STIG dla VCSA:

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

Skrypt wykonuje następujące zadania:

- **Na początku konfiguruje PowerCLI, wyłącza weryfikację certyfikatów i rezygnuje z udziału w programie Customer Experience Improvement Program (CEIP).**
- **Następnie łączy się z serwerami vCenter wskazanymi w zmiennej `$vcenters`.**
- **Obsługuje każdą kontrolę STIG za pomocą poleceń cmdlet PowerCLI. Na przykład ustawia `config.log.level` na info dla wskazanych serwerów vCenter.**
- **Wykonuje też kontrole dotyczące między innymi `config.vpxd.hostPasswordLength` i `VirtualCenter.VimPasswordExpirationInDays`.**
- **Na końcu sprawdza i konfiguruje zasady bezpieczeństwa oraz inne ustawienia.**
- **To przykładowy skrypt. Dostosuj go do swojego środowiska i wymagań STIG.**

______

## Automatyzacja VMware VM STIG

Oprócz zabezpieczenia hostów ESXi należy zastosować kontrole STIG na maszynach wirtualnych w infrastrukturze VMware. PowerCLI pomaga automatyzować ich konfigurację zgodnie z wytycznymi STIG.

## Skrypt: automatyzacja VMware VM STIG

Poniższy skrypt PowerCLI pokazuje, jak zautomatyzować wybrane kontrole STIG dla maszyn wirtualnych:

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

Skrypt wykonuje następujące zadania:

- **Podobnie jak skrypt VMware VCSA STIG, na początku konfiguruje środowisko PowerCLI.**
- **Łączy się z vCenter i wybiera klaster oraz folder zawierające docelowe maszyny wirtualne.**
- **Zmienna `$vmconfig` przechowuje ustawienia STIG dla maszyn wirtualnych, w tym zaawansowane opcje, takie jak wyłączenie kopiowania i wklejania oraz ograniczenie połączeń zdalnego wyświetlania.**
- **Przechodzi przez każdą maszynę wirtualną w wybranym klastrze i folderze, a następnie stosuje ustawienia STIG.**
- **Konfiguruje również szyfrowanie vMotion maszyn wirtualnych.**

To przykładowy skrypt. Zmień go zgodnie ze swoim środowiskiem i obowiązującymi wymaganiami STIG.

_____

## Dodatkowe materiały

- **DoD STIG VIB** [był wcześniej dostępny dla wersji 5.0–6.7](https://flings.vmware.com/dod-security-technical-implementation-guide-stig-esxi-vib), lecz nie jest już dostępny.
- **[Ryan Lakey](https://core.vmware.com/users/ryan-lakey)** udostępnia przydatne wskazówki dotyczące wdrażania DoD VMware STIG. Polecamy zapoznać się z tymi materiałami.
    - [VMware vSphere 8 STIG](https://core.vmware.com/resource/vmware-vsphere-8-stig)
    - [VMware vSphere 7 STIG](https://core.vmware.com/vsphere-7-stig)
    - [VMware vSphere 6.7 STIG](https://core.vmware.com/vmware-vsphere-67-stig)
    - [VMware STIG PowerCLI](https://github.com/rlakey/vmware-stig-powercli)
        - [Baza STIG VMware VCSA 6.7](https://github.com/rlakey/vmware-vcsa-6.7-stig-baseline)
        - [Baza STIG VMware VM 6.7](https://github.com/rlakey/vmware-vm-6.7-stig-baseline)
_____

## Podsumowanie

**Wdrożenie VMware STIG pomaga chronić infrastrukturę VMware i spełniać obowiązujące wymagania. PowerCLI automatyzuje i upraszcza stosowanie kontroli STIG na hostach ESXi i maszynach wirtualnych.**

W artykule pokazaliśmy, jak używać PowerCLI do automatyzacji VMware ESXi STIG i VM STIG. Omówiliśmy wymagania instalacyjne, przedstawiliśmy przykładowe skrypty i podkreśliliśmy znaczenie dostosowania ich do konkretnego środowiska.

**Za pomocą PowerCLI i zgodnie z wytycznymi STIG administratorzy mogą skutecznie zabezpieczać wdrożenia VMware, ograniczyć pracę ręczną i utrzymywać spójną konfigurację.**

## Źródła

- [DoD STIG VIB](https://flings.vmware.com/dod-security-technical-implementation-guide-stig-esxi-vib)
- [PowerCLI 11.3](https://www.powershellgallery.com/packages/VMware.PowerCLI/11.3.0.13990089)
- [PowerShell 5 lub nowszy](https://docs.microsoft.com/en-us/skypeforbusiness/set-up-your-computer-for-windows-powershell/download-and-install-windows-powershell-5-1)
- [ESXi 6.7 U2 lub nowszy](https://my.vmware.com/web/vmware/downloads/details?downloadGroup=ESXI670&productId=742)
