---
title: "Освойте защиту VMware"
date: 2023-08-03
lastmod: 2026-11-13
toc: true
draft: false
description: "В этом подробном руководстве вы узнаете, как применять VMware STIG с помощью PowerCLI и защищать среду VMware."
genre: ["Кибербезопасность", "Виртуализация", "ИТ-инфраструктура", "Автоматизация", "PowerShell", "VMware", "STIG", "Соответствие требованиям", "Скрипты", "Центр обработки данных"]
tags: ["PowerCLI", "VMware STIG", "безопасность VMware", "автоматизация", "скрипты", "PowerShell", "ESXi", "виртуализация", "соответствие требованиям", "кибербезопасность", "как использовать PowerCLI для VMware STIG", "автоматизация защиты VMware с PowerCLI", "скрипт PowerCLI для применения VMware STIG", "автоматизация защиты ESXi с PowerCLI", "защита среды VMware с PowerCLI"]
cover: "/img/cover/An_illustration_depicting_a_computer_server_sh.webp"
coverAlt: "Иллюстрация компьютерного сервера под замком, символизирующая защищённую инфраструктуру VMware."
coverCaption: "Защита среды VMware с помощью PowerCLI"
---

**Как применять VMware STIG с помощью PowerCLI**

PowerCLI представляет собой средство автоматизации и создания скриптов для управления и настройки сред VMware с помощью PowerShell. В статье показано, как применять VMware STIG (Security Technical Implementation Guide) к ESXi и виртуальным машинам с помощью PowerCLI.

## Введение

**VMware STIG** содержит рекомендации по безопасной настройке и администрированию инфраструктуры VMware. Их соблюдение помогает организациям повысить безопасность развертываний VMware и выполнить применимые государственные требования, например **STIG Defense Information Systems Agency (DISA)**.

## Что такое PowerCLI?

**PowerCLI** представляет собой интерфейс командной строки и инструмент для создания скриптов управления средами VMware. Он построен на PowerShell и включает множество командлетов для администрирования VMware. Администраторы используют его для автоматизации повторяющихся задач, изменения конфигураций и сбора сведений об инфраструктуре VMware.

### Установка и требования

Перед началом работы с PowerCLI и VMware STIG проверьте следующие требования:

- [**PowerCLI 11.3**](https://www.powershellgallery.com/packages/VMware.PowerCLI/11.3.0.13990089): установите PowerCLI из PowerShell Gallery командой `Install-Module VMware.PowerCLI -force`.
- [**PowerShell 5 или новее**](https://docs.microsoft.com/en-us/skypeforbusiness/set-up-your-computer-for-windows-powershell/download-and-install-windows-powershell-5-1): убедитесь, что установлена PowerShell 5 или более новая версия.
- [**ESXi 6.7 U2 или новее**](https://my.vmware.com/web/vmware/downloads/details?downloadGroup=ESXI670&productId=742): используйте ESXi 6.7 U2 или более новую версию.

## Автоматизация VMware VCSA STIG

VMware ESXi STIG содержит рекомендации по защите хостов ESXi. Автоматизация применения контролей STIG упрощает процесс и обеспечивает единообразную конфигурацию нескольких хостов.

### Важные замечания

Перед запуском автоматизации учтите следующее:

- **Убедитесь, что ни одной виртуальной машине или гостевой системе на хосте либо в кластере ESXi не требуются CD, USB или дискета.**
- **Примените STIG ко всем хостам ESXi и гостевым системам, подключённым к vCenter.**
- **Подготовьтесь устранять неполадки, которые могут возникнуть во время процесса.**

### Скрипт: автоматизация VMware VCSA STIG

Следующий скрипт PowerCLI автоматизирует применение выбранных контролей STIG для VCSA:

```powershell
Set-PowerCLIConfiguration -InvalidCertificateAction Ignore -Confirm:$false
Set-PowerCLIConfiguration -Scope User -ParticipateInCEIP $false -Confirm:$false
$vcenters = 127.0.0.1, 127.0.0.2

#Подключиться к каждому серверу vCenter
ForEach ($vc in $vcenters) {
    Connect-VIServer -Server $vc
}

#Автоматически

Write-Host "ID уязвимости: V-243098 ID правила: SV-243098r719537_rule ID STIG: VCTR-67-000036"
Write-Host "Если 'config.log.level' не задано как "info" или отсутствует, это считается нарушением."
ForEach ($vc in $vcenters) {
    Get-AdvancedSetting -Entity $vc -Name config.log.level | Set-AdvancedSetting -Value info
    Get-AdvancedSetting -Entity $vc -Name config.log.level
}

Write-Host "ID уязвимости: V-243090 ID правила: SV-243090r719513_rule ID STIG: VCTR-67-000024"
Write-Host "Если 'config.vpxd.hostPasswordLength' имеет значение, отличное от "32", это считается нарушением.
Если параметр отсутствует, это не считается нарушением."
ForEach ($vc in $vcenters) {
    Get-AdvancedSetting -Entity $vc -Name config.vpxd.hostPasswordLength | Set-AdvancedSetting -Value 32
    Get-AdvancedSetting -Entity $vc -Name config.vpxd.hostPasswordLength
}


Write-Host "ID уязвимости: V-243089 ID правила: SV-243089r719510_rule ID STIG: VCTR-67-000023"
Write-Host "Если 'VirtualCenter.VimPasswordExpirationInDays' имеет значение, отличное от "30", или отсутствует, это считается нарушением."
ForEach ($vc in $vcenters) {
    Try {
        Get-AdvancedSetting -Entity $vc -Name VirtualCenter.VimPasswordExpirationInDays | Set-AdvancedSetting -Value 30
    }
    Catch {
        New-AdvancedSetting -Entity $vc -Name VirtualCenter.VimPasswordExpirationInDays -Value 30
    }
}

Write-Host "ID уязвимости: V-243084 ID правила: SV-243085r719498_rule ID STIG: VCTR-67-000016"
Write-Host "Если NetFlow настроен, но IP-адрес коллектора неизвестен и не задокументирован, это считается нарушением."
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

Write-Host "ID уязвимости: V-243084 ID правила: SV-243084r719495_rule ID STIG: VCTR-67-000015"
Write-Host "Сервер vCenter должен установить для политики Promiscuous Mode распределённой группы портов значение «отклонять»."
Get-VDSwitch | Get-VDSecurityPolicy | Set-VDSecurityPolicy -AllowPromiscuous $false
Get-VDPortgroup | Where-Object { $_.IsUplink -eq $false } | Get-VDSecurityPolicy | Set-VDSecurityPolicy -AllowPromiscuous $false
Get-VDSwitch | Get-VDSecurityPolicy
Get-VDPortgroup | Where-Object { $_.IsUplink -eq $false } | Get-VDSecurityPolicy


Write-Host "ID уязвимости: V-243083 ID правила: SV-243083r719492_rule ID STIG: VCTR-67-000014"
Write-Host "Сервер vCenter должен установить для политики MAC Address Change распределённой группы портов значение «отклонять»."
Get-VDSwitch | Get-VDSecurityPolicy | Set-VDSecurityPolicy -MacChanges $false
Get-VDPortgroup | Where-Object { $_.IsUplink -eq $false } | Get-VDSecurityPolicy | Set-VDSecurityPolicy -MacChanges $false
Get-VDPortgroup | Where-Object { $_.IsUplink -eq $false } | Get-VDSecurityPolicy

Write-Host "ID уязвимости: V-243082 ID правила: SV-243082r719489_rule ID STIG: VCTR-67-000013"
Write-Host "Сервер vCenter должен установить для политики Forged Transmits распределённой группы портов значение «отклонять»."
Get-VDSwitch | Get-VDSecurityPolicy | Set-VDSecurityPolicy -ForgedTransmits $false
Get-VDPortgroup | Where-Object { $_.IsUplink -eq $false } | Get-VDSecurityPolicy | Set-VDSecurityPolicy -ForgedTransmits $false
Get-VDSwitch | Get-VDSecurityPolicy
Get-VDPortgroup | Where-Object { $_.IsUplink -eq $false } | Get-VDSecurityPolicy

Write-Host "ID уязвимости: V-243081 ID правила: SV-243081r719486_rule ID STIG: VCTR-67-000012"
Write-Host "Сервер vCenter должен отключить проверку состояния распределённого виртуального коммутатора."
Get-View -ViewType DistributedVirtualSwitch | Where-Object { ($_.config.HealthCheckConfig | Where-Object { $_.enable -notmatch "False" }) } | ForEach-Object { $_.UpdateDVSHealthCheckConfig(@((New-Object Vmware.Vim.VMwareDVSVlanMtuHealthCheckConfig -property @{enable = 0 }), (New-Object Vmware.Vim.VMwareDVSTeamingHealthCheckConfig -property @{enable = 0 }))) }
$vds = Get-VDSwitch
$vds.ExtensionData.Config.HealthCheckConfig

Write-Host "ID уязвимости: V-243077 ID правила: SV-243077r719474_rule ID STIG: VCTR-67-00000"
Write-Host "Сервер vCenter должен управлять резервом ёмкости, пропускной способности и другой избыточностью, чтобы ограничить последствия информационного потока и DoS-атак, включив Network I/O Control (NIOC)."
Write-Host "Если оповещение об ошибках syslog не создано и не включено, это считается нарушением."
ForEach ($vdswitch in (Get-VDSwitch.name)){
    (Get-VDSwitch $vdswitch | Get-View).EnableNetworkResourceManagement($true)
}
Get-VDSwitch | Select-Object Name, @{N = "NIOC Enabled"; E = { $_.ExtensionData.config.NetworkResourceManagementEnabled } }

#Ручная проверка

Write-Host "ID уязвимости: V-243076 ID правила: SV-243076r719471_rule ID STIG: VCTR-67-000005"
Write-Host "Пользователям сервера vCenter должны быть назначены правильные роли."
Write-Host "Необходимые привилегии сервисных учётных записей и пользователей должны быть задокументированы.
Если у пользователя или сервисной учётной записи привилегий больше, чем нужно, это считается нарушением."
Get-VIPermission | Sort-Object Role | Select-Object Role, Principal, Entity, Propagate, IsGroup | Format-Table -Auto

Write-Host "ID уязвимости: V-243119 ID правила: SV-243119r719600_rule ID STIG: VCTR-67-000064"
Write-Host "Если любая роль, кроме Administrator, или любая группа конкретного сайта имеет одно из этих разрешений, это считается нарушением."
$roles = Get-VIRole
ForEach ($role in $roles) {
    $privileges = $role.PrivilegeList
    If ($privileges -match "Crypto*" -or $privileges -match "Global.Diagnostics" -or $privileges -match "Host.Inventory.Add*" -or $privileges -match "Host.Local operations.Manage user groups") {
        Write-Host "$role имеет криптографические привилегии"
    }
}

Write-Host "ID уязвимости: V-243118 ID правила: SV-243118r719597_rule ID STIG: VCTR-67-000063"
Write-Host "Если у пользователя, не относящегося к Solution Users, есть роль "Administrator" и он явно не назначен для криптографических операций, это считается нарушением."
Get-VIPermission | Where-Object { $_.Role -eq "Admin" } | Select-Object Role, Principal, Entity, Propagate, IsGroup | Format-Table -Auto


Write-Host "ID уязвимости: V-243111 ID правила: SV-243111r719576_rule ID STIG: VCTR-67-000055"
Write-Host "Не применимо, если кластеры vSAN не включены."
Write-host "Если vSAN включён, а хранилище данных называется 'vsanDatastore', это считается нарушением."
If ($(Get-Cluster | Where-Object { $_.VsanEnabled } | Measure-Object).Count -gt 0) {
    Write-Host "Обнаружен включённый кластер vSAN"
    $Clusters = Get-Cluster | Where-Object { $_.VsanEnabled } 
    Foreach ($clus in $clusters) {
        $clus | Get-Datastore | Where-Object { $_.type -match "vsan" } | Set-Datastore -Name $(($clus.name) + "_vSAN_Datastore")
    }
}
else {
    Write-Host "vSAN не включён; это нарушение не применимо"
}

Write-Host "Если у пользователя или сервисной учётной записи привилегий больше, чем нужно, это считается нарушением."
Get-VIPermission | Sort-Object Role | Select-Object Role, Principal, Entity, Propagate, IsGroup | Format-Table -Auto

Write-Host "ID уязвимости: V-243088 ID правила: SV-243088r719507_rule ID STIG: VCTR-67-000020"
Write-Host "Проверьте теги VLAN группы портов и убедитесь, что им не назначен зарезервированный ID VLAN."
Write-Host "Некоторые физические коммутаторы резервируют VLAN ID для внутренних целей и часто блокируют трафик, настроенный на эти значения. Например, Cisco Catalyst обычно резервирует VLAN 1001–1024 и 4094, а Nexus — 3968–4047 и 4094."
Get-VDPortgroup | Select-Object Name, VlanConfiguration

Write-Host "ID уязвимости: V-243087 ID правила: SV-243087r719504_rule ID STIG: VCTR-67-000019"
Write-Host "Если для группы портов задан 'VLAN Trunk' без документированного необходимого исключения (например, для устройств NSX), это считается нарушением.
Если транкинг VLAN разрешён, но не ограничен минимально необходимым диапазоном, это считается нарушением."
Get-VDPortgroup | Where-Object { $_.ExtensionData.Config.Uplink -ne "True" } | Select-Object Name, VlanConfiguration

Write-Host "ID уязвимости: V-243078 ID правила: SV-243078r719644_rule ID STIG: VCTR-67-000008"
Write-Host "Сервер vCenter должен немедленно, в реальном времени, оповещать SA и ISSO обо всех сбоях аудита."
Write-Host "Если оповещение об ошибках syslog не создано и не включено, это считается нарушением."
Get-AlarmDefinition | Where-Object { $_.ExtensionData.Info.Expression.Expression.EventTypeId -eq "esx.problem.vmsyslogd.remote.failure" } | Select-Object Name, Enabled, @{N = "EventTypeId"; E = { $_.ExtensionData.Info.Expression.Expression.EventTypeId } }
```

Скрипт выполняет следующие действия:

- **Сначала настраивает PowerCLI, отключает проверку сертификатов и отказывается от участия в программе улучшения качества обслуживания клиентов (CEIP).**
- **Затем подключается к серверам vCenter, указанным в переменной `$vcenters`.**
- **Применяет каждый контроль STIG с помощью командлетов PowerCLI. Например, устанавливает `config.log.level` в значение info для указанных серверов vCenter.**
- **Также обрабатывает настройки `config.vpxd.hostPasswordLength` и `VirtualCenter.VimPasswordExpirationInDays`.**
- **В завершение проверяет и настраивает политики безопасности и другие параметры.**
- **Это пример скрипта. Измените его с учётом своей среды и требований STIG.**

______

## Автоматизация VMware VM STIG

Помимо защиты хостов ESXi, необходимо применять контроли STIG к виртуальным машинам инфраструктуры VMware. PowerCLI помогает автоматизировать настройку ВМ в соответствии с рекомендациями STIG.

## Скрипт: автоматизация VMware VM STIG

Следующий скрипт PowerCLI показывает, как автоматизировать выбранные контроли STIG для виртуальных машин:

```powershell
Set-PowerCLIConfiguration -InvalidCertificateAction Ignore -Confirm:$false
Set-PowerCLIConfiguration -Scope User -ParticipateInCEIP $false -Confirm:$false
Connect-VIServer -Server 127.0.0.1
$cluster = Get-Cluster -Name "Cluster"
$folder = Get-Folder -Name "Folder"

#Источник: https://github.com/rlakey/vmware-stig-powercli/blob/master/VMware_vSphere_6.7_VM_STIG_Remediation.ps1
$vmconfig = @{
    #Параметры усиления/STIG
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
    Write-Output "...Исправление расширенных параметров на $vm в $vcenter"
    ForEach ($setting in ($vmconfig.vmAdvSettings.GetEnumerator() | Sort-Object Name)) {
        #Получить значения для каждого указанного параметра
        $settingname = $setting.name
        $settingvalue = $setting.value
        If ($asetting = $vm | Get-AdvancedSetting -Name $settingname) {
            If ($asetting.value -eq $settingvalue) {
                Write-Output "...Параметр $settingname на $vm уже правильно настроен на значение $settingvalue"
            }
            else {
                Write-Output "...Параметр $settingname на $vm задан неверно: $($asetting.value); устанавливается $settingvalue"
                $asetting | Set-AdvancedSetting -Value $settingvalue -Confirm:$false
            }
        }
        else {
            Write-Output "...Параметр $settingname отсутствует на $vm; создание..."
            $vm | New-AdvancedSetting -Name $settingname -Value $settingvalue -Confirm:$false
        }
        Write-Output "...Удаление расширенных параметров на $vm в $vcenter при необходимости"
        ForEach ($setting in ($vmconfig.vmAdvSettingsRemove | Sort-Object Name)) {
            #Проверить наличие текущего параметра
            If ($asetting = $vm | Get-AdvancedSetting -Name $setting) {
                Write-Output "...Параметр $setting существует на $vm...удаление параметра"
                $asetting | Remove-AdvancedSetting -Confirm:$false
            }
            else {
                Write-Output "...Параметр $setting отсутствует на $vm"
            }
        }   
        If ($vm.extensiondata.Config.MigrateEncryption -eq $vmconfig.vmotionEncryption) {
            Write-Output "...Шифрование vMotion на $vm настроено правильно: $($vmconfig.vmotionEncryption)"
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

Скрипт выполняет следующие действия:

- **Как и скрипт VMware VCSA STIG, вначале настраивает среду PowerCLI.**
- **Подключается к vCenter и выбирает кластер и папку с целевыми виртуальными машинами.**
- **Переменная `$vmconfig` содержит параметры STIG для ВМ, в том числе расширенные настройки, например отключение копирования и вставки и ограничение количества подключений к удаленному дисплею.**
- **Перебирает все ВМ в выбранном кластере и папке и применяет к ним настройки STIG.**
- **Также настраивает шифрование vMotion для виртуальных машин.**

Это пример скрипта. Измените его с учётом своей среды и применимых требований STIG.

_____

## Дополнительные материалы

- **VIB DoD STIG раньше был [доступен для версий 5.0–6.7](https://flings.vmware.com/dod-security-technical-implementation-guide-stig-esxi-vib), но теперь недоступен.**
- [Ryan Lakey](https://core.vmware.com/users/ryan-lakey) публикует полезные рекомендации по применению DoD VMware STIG. Советуем ознакомиться с ними.
    - [VMware vSphere 8 STIG](https://core.vmware.com/resource/vmware-vsphere-8-stig)
    - [VMware vSphere 7 STIG](https://core.vmware.com/vsphere-7-stig)
    - [VMware vSphere 6.7 STIG](https://core.vmware.com/vmware-vsphere-67-stig)
    - [VMware STIG PowerCLI](https://github.com/rlakey/vmware-stig-powercli)
        - [Базовый профиль VMware VCSA 6.7 STIG](https://github.com/rlakey/vmware-vcsa-6.7-stig-baseline)
        - [Базовый профиль VMware VM 6.7 STIG](https://github.com/rlakey/vmware-vm-6.7-stig-baseline)
_____

## Заключение

**Применение VMware STIG помогает защитить инфраструктуру VMware и выполнить соответствующие требования. PowerCLI автоматизирует и упрощает применение контролей STIG к хостам ESXi и виртуальным машинам.**

В статье рассмотрено использование PowerCLI для автоматизации VMware ESXi STIG и VM STIG. Мы описали требования к установке, привели примеры скриптов и подчеркнули важность их адаптации к конкретной среде.

**С помощью PowerCLI и рекомендаций STIG администраторы могут эффективно защищать развертывания VMware, сокращать ручную работу и поддерживать единообразную конфигурацию.**

## Источники

- [VIB DoD STIG](https://flings.vmware.com/dod-security-technical-implementation-guide-stig-esxi-vib)
- [PowerCLI 11.3](https://www.powershellgallery.com/packages/VMware.PowerCLI/11.3.0.13990089)
- [PowerShell 5 или новее](https://docs.microsoft.com/en-us/skypeforbusiness/set-up-your-computer-for-windows-powershell/download-and-install-windows-powershell-5-1)
- [ESXi 6.7 U2 или новее](https://my.vmware.com/web/vmware/downloads/details?downloadGroup=ESXI670&productId=742)
