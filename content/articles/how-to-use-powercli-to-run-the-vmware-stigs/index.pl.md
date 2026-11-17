---
title: "Poznaj zabezpieczenia VMware"
date: 2023-08-03
lastmod: 2026-11-13
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

#Połącz się z każdym serwerem vCenter
ForEach ($vc in $vcenters) {
    Connect-VIServer -Server $vc
}

#Automatycznie

Write-Host "ID podatności: V-243098 ID reguły: SV-243098r719537_rule ID STIG: VCTR-67-000036"
Write-Host "Jeśli wartość 'config.log.level' nie jest ustawiona na "info" lub nie istnieje, jest to niezgodność."
ForEach ($vc in $vcenters) {
    Get-AdvancedSetting -Entity $vc -Name config.log.level | Set-AdvancedSetting -Value info
    Get-AdvancedSetting -Entity $vc -Name config.log.level
}

Write-Host "ID podatności: V-243090 ID reguły: SV-243090r719513_rule ID STIG: VCTR-67-000024"
Write-Host "Jeśli 'config.vpxd.hostPasswordLength' ma wartość inną niż "32", jest to niezgodność.
Brak ustawienia nie stanowi niezgodności."
ForEach ($vc in $vcenters) {
    Get-AdvancedSetting -Entity $vc -Name config.vpxd.hostPasswordLength | Set-AdvancedSetting -Value 32
    Get-AdvancedSetting -Entity $vc -Name config.vpxd.hostPasswordLength
}


Write-Host "ID podatności: V-243089 ID reguły: SV-243089r719510_rule ID STIG: VCTR-67-000023"
Write-Host "Jeśli 'VirtualCenter.VimPasswordExpirationInDays' ma wartość inną niż "30" lub nie istnieje, jest to niezgodność."
ForEach ($vc in $vcenters) {
    Try {
        Get-AdvancedSetting -Entity $vc -Name VirtualCenter.VimPasswordExpirationInDays | Set-AdvancedSetting -Value 30
    }
    Catch {
        New-AdvancedSetting -Entity $vc -Name VirtualCenter.VimPasswordExpirationInDays -Value 30
    }
}

Write-Host "ID podatności: V-243084 ID reguły: SV-243085r719498_rule ID STIG: VCTR-67-000016"
Write-Host "Jeśli skonfigurowano NetFlow, a adres IP kolektora nie jest znany i udokumentowany, jest to niezgodność."
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

Write-Host "ID podatności: V-243084 ID reguły: SV-243084r719495_rule ID STIG: VCTR-67-000015"
Write-Host "Serwer vCenter musi ustawić zasady Promiscuous Mode dla rozproszonej grupy portów na odrzucanie."
Get-VDSwitch | Get-VDSecurityPolicy | Set-VDSecurityPolicy -AllowPromiscuous $false
Get-VDPortgroup | Where-Object { $_.IsUplink -eq $false } | Get-VDSecurityPolicy | Set-VDSecurityPolicy -AllowPromiscuous $false
Get-VDSwitch | Get-VDSecurityPolicy
Get-VDPortgroup | Where-Object { $_.IsUplink -eq $false } | Get-VDSecurityPolicy


Write-Host "ID podatności: V-243083 ID reguły: SV-243083r719492_rule ID STIG: VCTR-67-000014"
Write-Host "Serwer vCenter musi ustawić zasady MAC Address Change dla rozproszonej grupy portów na odrzucanie."
Get-VDSwitch | Get-VDSecurityPolicy | Set-VDSecurityPolicy -MacChanges $false
Get-VDPortgroup | Where-Object { $_.IsUplink -eq $false } | Get-VDSecurityPolicy | Set-VDSecurityPolicy -MacChanges $false
Get-VDPortgroup | Where-Object { $_.IsUplink -eq $false } | Get-VDSecurityPolicy

Write-Host "ID podatności: V-243082 ID reguły: SV-243082r719489_rule ID STIG: VCTR-67-000013"
Write-Host "Serwer vCenter musi ustawić zasady Forged Transmits dla rozproszonej grupy portów na odrzucanie."
Get-VDSwitch | Get-VDSecurityPolicy | Set-VDSecurityPolicy -ForgedTransmits $false
Get-VDPortgroup | Where-Object { $_.IsUplink -eq $false } | Get-VDSecurityPolicy | Set-VDSecurityPolicy -ForgedTransmits $false
Get-VDSwitch | Get-VDSecurityPolicy
Get-VDPortgroup | Where-Object { $_.IsUplink -eq $false } | Get-VDSecurityPolicy

Write-Host "ID podatności: V-243081 ID reguły: SV-243081r719486_rule ID STIG: VCTR-67-000012"
Write-Host "Serwer vCenter musi wyłączyć kontrolę stanu rozproszonego przełącznika wirtualnego."
Get-View -ViewType DistributedVirtualSwitch | Where-Object { ($_.config.HealthCheckConfig | Where-Object { $_.enable -notmatch "False" }) } | ForEach-Object { $_.UpdateDVSHealthCheckConfig(@((New-Object Vmware.Vim.VMwareDVSVlanMtuHealthCheckConfig -property @{enable = 0 }), (New-Object Vmware.Vim.VMwareDVSTeamingHealthCheckConfig -property @{enable = 0 }))) }
$vds = Get-VDSwitch
$vds.ExtensionData.Config.HealthCheckConfig

Write-Host "ID podatności: V-243077 ID reguły: SV-243077r719474_rule ID STIG: VCTR-67-00000"
Write-Host "Serwer vCenter musi zarządzać nadmiarem przepustowości lub inną redundancją, aby ograniczyć skutki zalewania informacjami i ataków typu DoS, włączając Network I/O Control (NIOC)."
Write-Host "Brak utworzonego i włączonego alarmu o awarii syslog jest niezgodnością."
ForEach ($vdswitch in (Get-VDSwitch.name)){
    (Get-VDSwitch $vdswitch | Get-View).EnableNetworkResourceManagement($true)
}
Get-VDSwitch | Select-Object Name, @{N = "NIOC Enabled"; E = { $_.ExtensionData.config.NetworkResourceManagementEnabled } }

#Ręczny przegląd

Write-Host "ID podatności: V-243076 ID reguły: SV-243076r719471_rule ID STIG: VCTR-67-000005"
Write-Host "Użytkownikom serwera vCenter należy przypisać właściwe role."
Write-Host "Należy udokumentować wymagane uprawnienia kont usług i użytkowników.
Jeśli użytkownik lub konto usługi ma więcej uprawnień niż potrzeba, jest to niezgodność."
Get-VIPermission | Sort-Object Role | Select-Object Role, Principal, Entity, Propagate, IsGroup | Format-Table -Auto

Write-Host "ID podatności: V-243119 ID reguły: SV-243119r719600_rule ID STIG: VCTR-67-000064"
Write-Host "Jeśli dowolna rola poza Administrator lub grupa specyficzna dla witryny ma którekolwiek z tych uprawnień, jest to niezgodność."
$roles = Get-VIRole
ForEach ($role in $roles) {
    $privileges = $role.PrivilegeList
    If ($privileges -match "Crypto*" -or $privileges -match "Global.Diagnostics" -or $privileges -match "Host.Inventory.Add*" -or $privileges -match "Host.Local operations.Manage user groups") {
        Write-Host "$role ma uprawnienia kryptograficzne"
    }
}

Write-Host "ID podatności: V-243118 ID reguły: SV-243118r719597_rule ID STIG: VCTR-67-000063"
Write-Host "Jeśli użytkownik spoza Solution Users ma rolę "Administrator" i nie został wyraźnie wyznaczony do operacji kryptograficznych, jest to niezgodność."
Get-VIPermission | Where-Object { $_.Role -eq "Admin" } | Select-Object Role, Principal, Entity, Propagate, IsGroup | Format-Table -Auto


Write-Host "ID podatności: V-243111 ID reguły: SV-243111r719576_rule ID STIG: VCTR-67-000055"
Write-Host "Nie dotyczy, jeśli nie włączono żadnych klastrów vSAN."
Write-host "Jeśli vSAN jest włączony, a magazyn danych nazywa się 'vsanDatastore', jest to niezgodność."
If ($(Get-Cluster | Where-Object { $_.VsanEnabled } | Measure-Object).Count -gt 0) {
    Write-Host "Znaleziono włączony klaster vSAN"
    $Clusters = Get-Cluster | Where-Object { $_.VsanEnabled } 
    Foreach ($clus in $clusters) {
        $clus | Get-Datastore | Where-Object { $_.type -match "vsan" } | Set-Datastore -Name $(($clus.name) + "_vSAN_Datastore")
    }
}
else {
    Write-Host "vSAN nie jest włączony; ta niezgodność nie ma zastosowania"
}

Write-Host "Jeśli użytkownik lub konto usługi ma więcej uprawnień niż potrzeba, jest to niezgodność."
Get-VIPermission | Sort-Object Role | Select-Object Role, Principal, Entity, Propagate, IsGroup | Format-Table -Auto

Write-Host "ID podatności: V-243088 ID reguły: SV-243088r719507_rule ID STIG: VCTR-67-000020"
Write-Host "Sprawdź tagi VLAN grupy portów i upewnij się, że nie używają zarezerwowanego identyfikatora VLAN."
Write-Host "Niektóre przełączniki fizyczne rezerwują identyfikatory VLAN do użytku wewnętrznego i często blokują ruch skonfigurowany dla tych wartości. Na przykład przełączniki Cisco Catalyst zwykle rezerwują VLAN 1001–1024 i 4094, a Nexus 3968–4047 i 4094."
Get-VDPortgroup | Select-Object Name, VlanConfiguration

Write-Host "ID podatności: V-243087 ID reguły: SV-243087r719504_rule ID STIG: VCTR-67-000019"
Write-Host "Jeśli grupa portów ma ustawienie 'VLAN Trunk' bez udokumentowanego wyjątku (np. dla urządzeń NSX), jest to niezgodność.
Jeśli trunking VLAN jest dozwolony, ale nie ograniczono go do najmniejszego potrzebnego zakresu, jest to niezgodność."
Get-VDPortgroup | Where-Object { $_.ExtensionData.Config.Uplink -ne "True" } | Select-Object Name, VlanConfiguration

Write-Host "ID podatności: V-243078 ID reguły: SV-243078r719644_rule ID STIG: VCTR-67-000008"
Write-Host "Serwer vCenter musi natychmiast alarmować SA i ISSO o wszystkich błędach audytu, co najmniej w czasie rzeczywistym."
Write-Host "Brak utworzonego i włączonego alarmu o awarii syslog jest niezgodnością."
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

#Źródło: https://github.com/rlakey/vmware-stig-powercli/blob/master/VMware_vSphere_6.7_VM_STIG_Remediation.ps1
$vmconfig = @{
    #Ustawienia hardeningu/STIG
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
    Write-Output "...Przywracanie ustawień zaawansowanych na $vm w $vcenter"
    ForEach ($setting in ($vmconfig.vmAdvSettings.GetEnumerator() | Sort-Object Name)) {
        #Pobierz wartości dla każdego wskazanego ustawienia
        $settingname = $setting.name
        $settingvalue = $setting.value
        If ($asetting = $vm | Get-AdvancedSetting -Name $settingname) {
            If ($asetting.value -eq $settingvalue) {
                Write-Output "...Ustawienie $settingname na $vm jest już poprawnie skonfigurowane jako $settingvalue"
            }
            else {
                Write-Output "...Ustawienie $settingname na $vm ma błędną wartość $($asetting.value); ustawiam $settingvalue"
                $asetting | Set-AdvancedSetting -Value $settingvalue -Confirm:$false
            }
        }
        else {
            Write-Output "...Ustawienie $settingname nie istnieje na $vm; tworzenie..."
            $vm | New-AdvancedSetting -Name $settingname -Value $settingvalue -Confirm:$false
        }
        Write-Output "...Usuwanie ustawień zaawansowanych z $vm w $vcenter, jeśli to konieczne"
        ForEach ($setting in ($vmconfig.vmAdvSettingsRemove | Sort-Object Name)) {
            #Sprawdź, czy bieżące ustawienie istnieje
            If ($asetting = $vm | Get-AdvancedSetting -Name $setting) {
                Write-Output "...Ustawienie $setting istnieje na $vm...usuwanie ustawienia"
                $asetting | Remove-AdvancedSetting -Confirm:$false
            }
            else {
                Write-Output "...Ustawienie $setting nie istnieje na $vm"
            }
        }   
        If ($vm.extensiondata.Config.MigrateEncryption -eq $vmconfig.vmotionEncryption) {
            Write-Output "...Szyfrowanie vMotion jest poprawnie ustawione na $vm jako $($vmconfig.vmotionEncryption)"
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

- **DoD STIG VIB [był wcześniej dostępny dla wersji 5.0–6.7](https://flings.vmware.com/dod-security-technical-implementation-guide-stig-esxi-vib), lecz nie jest już dostępny.**
- [Ryan Lakey](https://core.vmware.com/users/ryan-lakey) udostępnia przydatne wskazówki dotyczące wdrażania DoD VMware STIG. Polecamy zapoznać się z tymi materiałami.
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
