---
title: "VMware ਸੁਰੱਖਿਆ ਵਿੱਚ ਮਾਹਰ ਬਣੋ"
date: 2023-08-03
lastmod: 2026-11-13
toc: true
draft: false
description: "ਇਸ ਵਿਸਥਾਰਪੂਰਵਕ ਗਾਈਡ ਵਿੱਚ PowerCLI ਨਾਲ VMware STIG ਲਾਗੂ ਕਰਕੇ VMware ਵਾਤਾਵਰਣ ਨੂੰ ਸੁਰੱਖਿਅਤ ਕਰਨ ਦਾ ਤਰੀਕਾ ਸਿੱਖੋ।"
genre: ["ਸਾਈਬਰ ਸੁਰੱਖਿਆ", "ਵਰਚੁਅਲਾਈਜ਼ੇਸ਼ਨ", "ਆਈਟੀ ਬੁਨਿਆਦੀ ਢਾਂਚਾ", "ਆਟੋਮੇਸ਼ਨ", "PowerShell", "VMware", "STIG", "ਪਾਲਣਾ", "ਸਕ੍ਰਿਪਟਿੰਗ", "ਡਾਟਾ ਸੈਂਟਰ"]
tags: ["PowerCLI", "VMware STIG", "VMware ਸੁਰੱਖਿਆ", "ਆਟੋਮੇਸ਼ਨ", "ਸਕ੍ਰਿਪਟਿੰਗ", "PowerShell", "ESXi", "ਵਰਚੁਅਲਾਈਜ਼ੇਸ਼ਨ", "ਪਾਲਣਾ", "ਸਾਈਬਰ ਸੁਰੱਖਿਆ", "VMware STIG ਲਈ PowerCLI ਕਿਵੇਂ ਵਰਤਣਾ ਹੈ", "PowerCLI ਨਾਲ VMware ਸੁਰੱਖਿਆ ਆਟੋਮੇਟ ਕਰਨਾ", "VMware STIG ਲਾਗੂ ਕਰਨ ਲਈ PowerCLI ਸਕ੍ਰਿਪਟ", "ESXi ਸੁਰੱਖਿਆ ਲਈ PowerCLI ਆਟੋਮੇਸ਼ਨ", "PowerCLI ਨਾਲ VMware ਵਾਤਾਵਰਣ ਸੁਰੱਖਿਅਤ ਕਰਨਾ"]
cover: "/img/cover/An_illustration_depicting_a_computer_server_sh.webp"
coverAlt: "ਤਾਲੇ ਨਾਲ ਸੁਰੱਖਿਅਤ ਕੰਪਿਊਟਰ ਸਰਵਰ ਦੀ ਤਸਵੀਰ, ਜੋ ਸੁਰੱਖਿਅਤ VMware ਬੁਨਿਆਦੀ ਢਾਂਚੇ ਦਾ ਪ੍ਰਤੀਕ ਹੈ।"
coverCaption: "PowerCLI ਨਾਲ ਆਪਣੇ VMware ਵਾਤਾਵਰਣ ਨੂੰ ਸੁਰੱਖਿਅਤ ਕਰੋ"
---

**PowerCLI ਨਾਲ VMware STIG ਕਿਵੇਂ ਲਾਗੂ ਕਰੀਏ**

PowerCLI ਆਟੋਮੇਸ਼ਨ ਅਤੇ ਸਕ੍ਰਿਪਟਿੰਗ ਟੂਲ ਹੈ, ਜਿਸ ਨਾਲ PowerShell ਰਾਹੀਂ VMware ਵਾਤਾਵਰਣਾਂ ਦਾ ਪ੍ਰਬੰਧਨ ਅਤੇ ਸੰਰਚਨਾ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਹ ਲੇਖ ਦੱਸਦਾ ਹੈ ਕਿ ESXi ਅਤੇ ਵਰਚੁਅਲ ਮਸ਼ੀਨਾਂ ਉੱਤੇ VMware STIG (Security Technical Implementation Guide) ਲਾਗੂ ਕਰਨ ਲਈ PowerCLI ਕਿਵੇਂ ਵਰਤਣਾ ਹੈ।

## ਜਾਣ-ਪਛਾਣ

**VMware STIG** VMware ਬੁਨਿਆਦੀ ਢਾਂਚੇ ਨੂੰ ਸੁਰੱਖਿਅਤ ਢੰਗ ਨਾਲ ਸੰਰਚਿਤ ਅਤੇ ਪ੍ਰਬੰਧਿਤ ਕਰਨ ਲਈ ਹਦਾਇਤਾਂ ਅਤੇ ਸਿਫ਼ਾਰਸ਼ਾਂ ਦਿੰਦਾ ਹੈ। ਇਸ ਦੀ ਪਾਲਣਾ ਨਾਲ ਸੰਸਥਾਵਾਂ ਆਪਣੇ VMware ਤੈਨਾਤੀਆਂ ਦੀ ਸੁਰੱਖਿਆ ਵਧਾ ਸਕਦੀਆਂ ਹਨ ਅਤੇ **Defense Information Systems Agency (DISA) STIG** ਵਰਗੀਆਂ ਲਾਗੂ ਸਰਕਾਰੀ ਲੋੜਾਂ ਪੂਰੀਆਂ ਕਰ ਸਕਦੀਆਂ ਹਨ।

## PowerCLI ਕੀ ਹੈ?

**PowerCLI** VMware ਵਾਤਾਵਰਣਾਂ ਦੇ ਪ੍ਰਬੰਧਨ ਲਈ ਕਮਾਂਡ-ਲਾਈਨ ਇੰਟਰਫੇਸ ਅਤੇ ਸਕ੍ਰਿਪਟਿੰਗ ਟੂਲ ਹੈ। ਇਹ PowerShell ਉੱਤੇ ਬਣਿਆ ਹੈ ਅਤੇ VMware ਪ੍ਰਬੰਧਨ ਲਈ ਕਈ ਖ਼ਾਸ cmdlet ਦਿੰਦਾ ਹੈ। ਪ੍ਰਸ਼ਾਸਕ ਇਸ ਨਾਲ ਦੁਹਰਾਏ ਜਾਣ ਵਾਲੇ ਕੰਮ ਆਟੋਮੇਟ ਕਰਦੇ, ਸੰਰਚਨਾਵਾਂ ਬਦਲਦੇ ਅਤੇ VMware ਬੁਨਿਆਦੀ ਢਾਂਚੇ ਤੋਂ ਜਾਣਕਾਰੀ ਇਕੱਠੀ ਕਰਦੇ ਹਨ।

### ਇੰਸਟਾਲੇਸ਼ਨ ਅਤੇ ਲੋੜਾਂ

PowerCLI ਅਤੇ VMware STIG ਨਾਲ ਕੰਮ ਸ਼ੁਰੂ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ ਇਹ ਲੋੜਾਂ ਜਾਂਚੋ:

- [**PowerCLI 11.3**](https://www.powershellgallery.com/packages/VMware.PowerCLI/11.3.0.13990089): PowerShell Gallery ਤੋਂ `Install-Module VMware.PowerCLI -force` ਕਮਾਂਡ ਨਾਲ PowerCLI ਇੰਸਟਾਲ ਕਰੋ।
- [**PowerShell 5 ਜਾਂ ਇਸ ਤੋਂ ਨਵਾਂ**](https://docs.microsoft.com/en-us/skypeforbusiness/set-up-your-computer-for-windows-powershell/download-and-install-windows-powershell-5-1): ਪੱਕਾ ਕਰੋ ਕਿ PowerShell 5 ਜਾਂ ਇਸ ਤੋਂ ਨਵਾਂ ਸੰਸਕਰਣ ਇੰਸਟਾਲ ਹੈ।
- [**ESXi 6.7 U2 ਜਾਂ ਇਸ ਤੋਂ ਨਵਾਂ**](https://my.vmware.com/web/vmware/downloads/details?downloadGroup=ESXI670&productId=742): ESXi 6.7 U2 ਜਾਂ ਇਸ ਤੋਂ ਨਵਾਂ ਸੰਸਕਰਣ ਵਰਤੋ।

## VMware VCSA STIG ਆਟੋਮੇਟ ਕਰੋ

VMware ESXi STIG ਵਿੱਚ ESXi ਹੋਸਟਾਂ ਦੀ ਸੁਰੱਖਿਆ ਲਈ ਹਦਾਇਤਾਂ ਹਨ। STIG ਨਿਯੰਤਰਣ ਲਾਗੂ ਕਰਨ ਨੂੰ ਆਟੋਮੇਟ ਕਰਕੇ ਪ੍ਰਕਿਰਿਆ ਸੌਖੀ ਬਣਾਈ ਜਾ ਸਕਦੀ ਹੈ ਅਤੇ ਕਈ ਹੋਸਟਾਂ ਉੱਤੇ ਇੱਕੋ ਜਿਹੀ ਸੰਰਚਨਾ ਰੱਖੀ ਜਾ ਸਕਦੀ ਹੈ।

### ਧਿਆਨਯੋਗ ਗੱਲਾਂ

ਆਟੋਮੇਸ਼ਨ ਤੋਂ ਪਹਿਲਾਂ ਇਨ੍ਹਾਂ ਗੱਲਾਂ ਦਾ ਧਿਆਨ ਰੱਖੋ:

- **ਪੱਕਾ ਕਰੋ ਕਿ ESXi ਹੋਸਟ ਜਾਂ ਕਲੱਸਟਰ ਉੱਤੇ ਕਿਸੇ ਵਰਚੁਅਲ ਮਸ਼ੀਨ ਜਾਂ ਗੈਸਟ ਨੂੰ CD, USB ਜਾਂ ਫਲੌਪੀ ਡਿਸਕ ਦੀ ਲੋੜ ਨਹੀਂ ਹੈ।**
- **vCenter ਨਾਲ ਜੁੜੇ ਸਾਰੇ ESXi ਹੋਸਟਾਂ ਅਤੇ ਗੈਸਟ ਸਿਸਟਮਾਂ ਉੱਤੇ STIG ਲਾਗੂ ਕਰੋ।**
- **ਪ੍ਰਕਿਰਿਆ ਦੌਰਾਨ ਆਉਣ ਵਾਲੀਆਂ ਸਮੱਸਿਆਵਾਂ ਹੱਲ ਕਰਨ ਲਈ ਟ੍ਰਬਲਸ਼ੂਟਿੰਗ ਦਾ ਗਿਆਨ ਲਾਜ਼ਮੀ ਹੈ।**

### ਸਕ੍ਰਿਪਟ: VMware VCSA STIG ਆਟੋਮੇਸ਼ਨ

ਹੇਠਾਂ ਦਿੱਤੀ PowerCLI ਸਕ੍ਰਿਪਟ VCSA ਲਈ ਚੁਣੇ ਹੋਏ STIG ਨਿਯੰਤਰਣ ਆਪਣੇ ਆਪ ਲਾਗੂ ਕਰਦੀ ਹੈ:

```powershell
Set-PowerCLIConfiguration -InvalidCertificateAction Ignore -Confirm:$false
Set-PowerCLIConfiguration -Scope User -ParticipateInCEIP $false -Confirm:$false
$vcenters = 127.0.0.1, 127.0.0.2

#ਹਰੇਕ vCenter ਸਰਵਰ ਨਾਲ ਜੁੜੋ
ForEach ($vc in $vcenters) {
    Connect-VIServer -Server $vc
}

#ਆਟੋਮੈਟਿਕ

Write-Host "ਕਮਜ਼ੋਰੀ ID: V-243098 ਨਿਯਮ ID: SV-243098r719537_rule STIG ID: VCTR-67-000036"
Write-Host "ਜੇ 'config.log.level' ਦਾ ਮੁੱਲ "info" 'ਤੇ ਸੈੱਟ ਨਾ ਹੋਵੇ ਜਾਂ ਮੌਜੂਦ ਨਾ ਹੋਵੇ, ਤਾਂ ਇਹ ਇੱਕ ਖੋਜ ਹੈ।"
ForEach ($vc in $vcenters) {
    Get-AdvancedSetting -Entity $vc -Name config.log.level | Set-AdvancedSetting -Value info
    Get-AdvancedSetting -Entity $vc -Name config.log.level
}

Write-Host "ਕਮਜ਼ੋਰੀ ID: V-243090 ਨਿਯਮ ID: SV-243090r719513_rule STIG ID: VCTR-67-000024"
Write-Host "ਜੇ 'config.vpxd.hostPasswordLength' ਦਾ ਮੁੱਲ "32" ਤੋਂ ਵੱਖਰਾ ਹੋਵੇ, ਤਾਂ ਇਹ ਇੱਕ ਖੋਜ ਹੈ।
ਜੇ ਸੈਟਿੰਗ ਮੌਜੂਦ ਨਹੀਂ, ਤਾਂ ਇਹ ਖੋਜ ਨਹੀਂ ਹੈ।"
ForEach ($vc in $vcenters) {
    Get-AdvancedSetting -Entity $vc -Name config.vpxd.hostPasswordLength | Set-AdvancedSetting -Value 32
    Get-AdvancedSetting -Entity $vc -Name config.vpxd.hostPasswordLength
}


Write-Host "ਕਮਜ਼ੋਰੀ ID: V-243089 ਨਿਯਮ ID: SV-243089r719510_rule STIG ID: VCTR-67-000023"
Write-Host "ਜੇ 'VirtualCenter.VimPasswordExpirationInDays' ਦਾ ਮੁੱਲ "30" ਤੋਂ ਵੱਖਰਾ ਹੋਵੇ ਜਾਂ ਮੌਜੂਦ ਨਾ ਹੋਵੇ, ਤਾਂ ਇਹ ਇੱਕ ਖੋਜ ਹੈ।"
ForEach ($vc in $vcenters) {
    Try {
        Get-AdvancedSetting -Entity $vc -Name VirtualCenter.VimPasswordExpirationInDays | Set-AdvancedSetting -Value 30
    }
    Catch {
        New-AdvancedSetting -Entity $vc -Name VirtualCenter.VimPasswordExpirationInDays -Value 30
    }
}

Write-Host "ਕਮਜ਼ੋਰੀ ID: V-243084 ਨਿਯਮ ID: SV-243085r719498_rule STIG ID: VCTR-67-000016"
Write-Host "ਜੇ NetFlow ਕੌਂਫਿਗਰ ਹੈ ਪਰ collector IP ਜਾਣਿਆ ਅਤੇ ਦਰਜ ਨਹੀਂ ਹੈ, ਤਾਂ ਇਹ ਇੱਕ ਖੋਜ ਹੈ।"
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

Write-Host "ਕਮਜ਼ੋਰੀ ID: V-243084 ਨਿਯਮ ID: SV-243084r719495_rule STIG ID: VCTR-67-000015"
Write-Host "vCenter Server ਨੂੰ ਵੰਡੇ ਹੋਏ port group ਦੀ Promiscuous Mode ਨੀਤੀ reject ਕਰਨ ਲਈ ਸੈੱਟ ਕਰਨੀ ਚਾਹੀਦੀ ਹੈ।"
Get-VDSwitch | Get-VDSecurityPolicy | Set-VDSecurityPolicy -AllowPromiscuous $false
Get-VDPortgroup | Where-Object { $_.IsUplink -eq $false } | Get-VDSecurityPolicy | Set-VDSecurityPolicy -AllowPromiscuous $false
Get-VDSwitch | Get-VDSecurityPolicy
Get-VDPortgroup | Where-Object { $_.IsUplink -eq $false } | Get-VDSecurityPolicy


Write-Host "ਕਮਜ਼ੋਰੀ ID: V-243083 ਨਿਯਮ ID: SV-243083r719492_rule STIG ID: VCTR-67-000014"
Write-Host "vCenter Server ਨੂੰ ਵੰਡੇ ਹੋਏ port group ਦੀ MAC Address Change ਨੀਤੀ reject ਕਰਨ ਲਈ ਸੈੱਟ ਕਰਨੀ ਚਾਹੀਦੀ ਹੈ।"
Get-VDSwitch | Get-VDSecurityPolicy | Set-VDSecurityPolicy -MacChanges $false
Get-VDPortgroup | Where-Object { $_.IsUplink -eq $false } | Get-VDSecurityPolicy | Set-VDSecurityPolicy -MacChanges $false
Get-VDPortgroup | Where-Object { $_.IsUplink -eq $false } | Get-VDSecurityPolicy

Write-Host "ਕਮਜ਼ੋਰੀ ID: V-243082 ਨਿਯਮ ID: SV-243082r719489_rule STIG ID: VCTR-67-000013"
Write-Host "vCenter Server ਨੂੰ ਵੰਡੇ ਹੋਏ port group ਦੀ Forged Transmits ਨੀਤੀ reject ਕਰਨ ਲਈ ਸੈੱਟ ਕਰਨੀ ਚਾਹੀਦੀ ਹੈ।"
Get-VDSwitch | Get-VDSecurityPolicy | Set-VDSecurityPolicy -ForgedTransmits $false
Get-VDPortgroup | Where-Object { $_.IsUplink -eq $false } | Get-VDSecurityPolicy | Set-VDSecurityPolicy -ForgedTransmits $false
Get-VDSwitch | Get-VDSecurityPolicy
Get-VDPortgroup | Where-Object { $_.IsUplink -eq $false } | Get-VDSecurityPolicy

Write-Host "ਕਮਜ਼ੋਰੀ ID: V-243081 ਨਿਯਮ ID: SV-243081r719486_rule STIG ID: VCTR-67-000012"
Write-Host "vCenter Server ਨੂੰ ਵੰਡੇ ਹੋਏ virtual switch ਦੀ health check ਬੰਦ ਕਰਨੀ ਚਾਹੀਦੀ ਹੈ।"
Get-View -ViewType DistributedVirtualSwitch | Where-Object { ($_.config.HealthCheckConfig | Where-Object { $_.enable -notmatch "False" }) } | ForEach-Object { $_.UpdateDVSHealthCheckConfig(@((New-Object Vmware.Vim.VMwareDVSVlanMtuHealthCheckConfig -property @{enable = 0 }), (New-Object Vmware.Vim.VMwareDVSTeamingHealthCheckConfig -property @{enable = 0 }))) }
$vds = Get-VDSwitch
$vds.ExtensionData.Config.HealthCheckConfig

Write-Host "ਕਮਜ਼ੋਰੀ ID: V-243077 ਨਿਯਮ ID: SV-243077r719474_rule STIG ID: VCTR-67-00000"
Write-Host "ਜਾਣਕਾਰੀ ਦੀ ਭਰਮਾਰ ਅਤੇ denial-of-service (DoS) ਹਮਲਿਆਂ ਦੇ ਅਸਰ ਘਟਾਉਣ ਲਈ vCenter Server ਨੂੰ Network I/O Control (NIOC) ਚਾਲੂ ਕਰਕੇ ਵਾਧੂ ਸਮਰੱਥਾ, bandwidth ਜਾਂ ਹੋਰ redundancy ਦਾ ਪ੍ਰਬੰਧ ਕਰਨਾ ਚਾਹੀਦਾ ਹੈ।"
Write-Host "ਜੇ syslog ਅਸਫਲਤਾਵਾਂ ਦੀ ਚੇਤਾਵਨੀ ਲਈ ਕੋਈ alert ਬਣਾਇਆ ਅਤੇ ਚਾਲੂ ਨਹੀਂ ਕੀਤਾ ਗਿਆ, ਤਾਂ ਇਹ ਇੱਕ ਖੋਜ ਹੈ।"
ForEach ($vdswitch in (Get-VDSwitch.name)){
    (Get-VDSwitch $vdswitch | Get-View).EnableNetworkResourceManagement($true)
}
Get-VDSwitch | Select-Object Name, @{N = "NIOC Enabled"; E = { $_.ExtensionData.config.NetworkResourceManagementEnabled } }

#ਦਸਤੀ ਸਮੀਖਿਆ

Write-Host "ਕਮਜ਼ੋਰੀ ID: V-243076 ਨਿਯਮ ID: SV-243076r719471_rule STIG ID: VCTR-67-000005"
Write-Host "vCenter Server ਦੇ ਵਰਤੋਂਕਾਰਾਂ ਨੂੰ ਸਹੀ roles ਦਿੱਤੇ ਜਾਣੇ ਚਾਹੀਦੇ ਹਨ।"
Write-Host "service accounts ਅਤੇ ਵਰਤੋਂਕਾਰਾਂ ਲਈ ਲੋੜੀਂਦੇ privileges ਦਰਜ ਹੋਣੇ ਚਾਹੀਦੇ ਹਨ।
ਜੇ ਕਿਸੇ ਵਰਤੋਂਕਾਰ ਜਾਂ service account ਕੋਲ ਲੋੜ ਤੋਂ ਵੱਧ privileges ਹਨ, ਤਾਂ ਇਹ ਇੱਕ ਖੋਜ ਹੈ।"
Get-VIPermission | Sort-Object Role | Select-Object Role, Principal, Entity, Propagate, IsGroup | Format-Table -Auto

Write-Host "ਕਮਜ਼ੋਰੀ ID: V-243119 ਨਿਯਮ ID: SV-243119r719600_rule STIG ID: VCTR-67-000064"
Write-Host "ਜੇ Administrator ਤੋਂ ਇਲਾਵਾ ਕੋਈ role ਜਾਂ site-specific group ਇਹਨਾਂ ਵਿੱਚੋਂ ਕੋਈ permission ਰੱਖਦਾ ਹੈ, ਤਾਂ ਇਹ ਇੱਕ ਖੋਜ ਹੈ।"
$roles = Get-VIRole
ForEach ($role in $roles) {
    $privileges = $role.PrivilegeList
    If ($privileges -match "Crypto*" -or $privileges -match "Global.Diagnostics" -or $privileges -match "Host.Inventory.Add*" -or $privileges -match "Host.Local operations.Manage user groups") {
        Write-Host "$role ਕੋਲ cryptographic privileges ਹਨ"
    }
}

Write-Host "ਕਮਜ਼ੋਰੀ ID: V-243118 ਨਿਯਮ ID: SV-243118r719597_rule STIG ID: VCTR-67-000063"
Write-Host "ਜੇ Solution Users ਤੋਂ ਇਲਾਵਾ ਕਿਸੇ ਵਰਤੋਂਕਾਰ ਕੋਲ "Administrator" role ਹੈ ਅਤੇ ਉਸਨੂੰ cryptographic ਕੰਮਾਂ ਲਈ ਸਪਸ਼ਟ ਤੌਰ ’ਤੇ ਨਿਯੁਕਤ ਨਹੀਂ ਕੀਤਾ ਗਿਆ, ਤਾਂ ਇਹ ਇੱਕ ਖੋਜ ਹੈ।"
Get-VIPermission | Where-Object { $_.Role -eq "Admin" } | Select-Object Role, Principal, Entity, Propagate, IsGroup | Format-Table -Auto


Write-Host "ਕਮਜ਼ੋਰੀ ID: V-243111 ਨਿਯਮ ID: SV-243111r719576_rule STIG ID: VCTR-67-000055"
Write-Host "ਜੇ ਕੋਈ vSAN cluster ਚਾਲੂ ਨਹੀਂ, ਤਾਂ ਲਾਗੂ ਨਹੀਂ।"
Write-host "ਜੇ vSAN ਚਾਲੂ ਹੈ ਅਤੇ datastore ਦਾ ਨਾਮ 'vsanDatastore' ਹੈ, ਤਾਂ ਇਹ ਇੱਕ ਖੋਜ ਹੈ।"
If ($(Get-Cluster | Where-Object { $_.VsanEnabled } | Measure-Object).Count -gt 0) {
    Write-Host "ਚਾਲੂ vSAN cluster ਮਿਲਿਆ"
    $Clusters = Get-Cluster | Where-Object { $_.VsanEnabled } 
    Foreach ($clus in $clusters) {
        $clus | Get-Datastore | Where-Object { $_.type -match "vsan" } | Set-Datastore -Name $(($clus.name) + "_vSAN_Datastore")
    }
}
else {
    Write-Host "vSAN ਚਾਲੂ ਨਹੀਂ ਹੈ; ਇਹ ਖੋਜ ਲਾਗੂ ਨਹੀਂ ਹੁੰਦੀ"
}

Write-Host "ਜੇ ਕਿਸੇ ਵਰਤੋਂਕਾਰ ਜਾਂ service account ਕੋਲ ਲੋੜ ਤੋਂ ਵੱਧ privileges ਹਨ, ਤਾਂ ਇਹ ਇੱਕ ਖੋਜ ਹੈ।"
Get-VIPermission | Sort-Object Role | Select-Object Role, Principal, Entity, Propagate, IsGroup | Format-Table -Auto

Write-Host "ਕਮਜ਼ੋਰੀ ID: V-243088 ਨਿਯਮ ID: SV-243088r719507_rule STIG ID: VCTR-67-000020"
Write-Host "port group ਦੇ VLAN tags ਵੇਖੋ ਅਤੇ ਪੁਸ਼ਟੀ ਕਰੋ ਕਿ ਉਹ reserved VLAN ID ਨਹੀਂ ਵਰਤਦੇ।"
Write-Host "ਕੁਝ physical switches ਅੰਦਰੂਨੀ ਵਰਤੋਂ ਲਈ VLAN IDs ਰਾਖਵੇਂ ਰੱਖਦੇ ਹਨ ਅਤੇ ਅਕਸਰ ਇਹਨਾਂ ਮੁੱਲਾਂ ਨਾਲ ਕੌਂਫਿਗਰ traffic ਰੋਕਦੇ ਹਨ। ਉਦਾਹਰਨ ਲਈ, Cisco Catalyst ਆਮ ਤੌਰ ’ਤੇ VLAN 1001–1024 ਅਤੇ 4094 ਰਾਖਵੇਂ ਰੱਖਦੇ ਹਨ, ਜਦਕਿ Nexus 3968–4047 ਅਤੇ 4094 ਰਾਖਵੇਂ ਰੱਖਦੇ ਹਨ।"
Get-VDPortgroup | Select-Object Name, VlanConfiguration

Write-Host "ਕਮਜ਼ੋਰੀ ID: V-243087 ਨਿਯਮ ID: SV-243087r719504_rule STIG ID: VCTR-67-000019"
Write-Host "ਜੇ port group 'VLAN Trunk' ਵਜੋਂ ਕੌਂਫਿਗਰ ਹੈ ਅਤੇ ਲੋੜੀਂਦੀ ਛੋਟ (ਜਿਵੇਂ NSX appliances ਲਈ) ਦਰਜ ਨਹੀਂ, ਤਾਂ ਇਹ ਇੱਕ ਖੋਜ ਹੈ।
ਜੇ VLAN trunking ਮਨਜ਼ੂਰ ਹੈ ਪਰ ਲੋੜੀਂਦੀ ਘੱਟੋ-ਘੱਟ range ਤੱਕ ਸੀਮਿਤ ਨਹੀਂ, ਤਾਂ ਇਹ ਇੱਕ ਖੋਜ ਹੈ।"
Get-VDPortgroup | Where-Object { $_.ExtensionData.Config.Uplink -ne "True" } | Select-Object Name, VlanConfiguration

Write-Host "ਕਮਜ਼ੋਰੀ ID: V-243078 ਨਿਯਮ ID: SV-243078r719644_rule STIG ID: VCTR-67-000008"
Write-Host "vCenter Server ਨੂੰ ਸਾਰੇ audit failure events ਬਾਰੇ SA ਅਤੇ ISSO ਨੂੰ ਘੱਟੋ-ਘੱਟ ਤੁਰੰਤ real-time alert ਦੇਣਾ ਚਾਹੀਦਾ ਹੈ।"
Write-Host "ਜੇ syslog ਅਸਫਲਤਾਵਾਂ ਦੀ ਚੇਤਾਵਨੀ ਲਈ ਕੋਈ alert ਬਣਾਇਆ ਅਤੇ ਚਾਲੂ ਨਹੀਂ ਕੀਤਾ ਗਿਆ, ਤਾਂ ਇਹ ਇੱਕ ਖੋਜ ਹੈ।"
Get-AlarmDefinition | Where-Object { $_.ExtensionData.Info.Expression.Expression.EventTypeId -eq "esx.problem.vmsyslogd.remote.failure" } | Select-Object Name, Enabled, @{N = "EventTypeId"; E = { $_.ExtensionData.Info.Expression.Expression.EventTypeId } }
```

ਇਹ ਸਕ੍ਰਿਪਟ ਹੇਠਾਂ ਦਿੱਤੇ ਕੰਮ ਕਰਦੀ ਹੈ:

- **ਪਹਿਲਾਂ PowerCLI ਸੰਰਚਿਤ ਕਰਦੀ ਹੈ, ਸਰਟੀਫਿਕੇਟ ਦੀ ਜਾਂਚ ਬੰਦ ਕਰਦੀ ਹੈ ਅਤੇ Customer Experience Improvement Program (CEIP) ਵਿੱਚ ਸ਼ਾਮਲ ਹੋਣਾ ਬੰਦ ਕਰਦੀ ਹੈ।**
- **ਫਿਰ `$vcenters` ਵੇਰੀਏਬਲ ਵਿੱਚ ਦਿੱਤੇ vCenter ਸਰਵਰਾਂ ਨਾਲ ਜੁੜਦੀ ਹੈ।**
- **PowerCLI cmdlet ਨਾਲ ਹਰੇਕ STIG ਨਿਯੰਤਰਣ ਲਾਗੂ ਕਰਦੀ ਹੈ। ਮਿਸਾਲ ਵਜੋਂ, ਦਿੱਤੇ vCenter ਸਰਵਰਾਂ ਲਈ `config.log.level` ਨੂੰ info ਕਰਦੀ ਹੈ।**
- **`config.vpxd.hostPasswordLength` ਅਤੇ `VirtualCenter.VimPasswordExpirationInDays` ਨਾਲ ਜੁੜੇ ਨਿਯੰਤਰਣ ਵੀ ਲਾਗੂ ਕਰਦੀ ਹੈ।**
- **ਅਖੀਰ ਵਿੱਚ ਸੁਰੱਖਿਆ ਨੀਤੀਆਂ ਅਤੇ ਹੋਰ ਸੈਟਿੰਗਾਂ ਦੀ ਜਾਂਚ ਅਤੇ ਸੰਰਚਨਾ ਕਰਦੀ ਹੈ।**
- **ਇਹ ਮਿਸਾਲੀ ਸਕ੍ਰਿਪਟ ਹੈ। ਇਸਨੂੰ ਆਪਣੇ ਵਾਤਾਵਰਣ ਅਤੇ STIG ਲੋੜਾਂ ਮੁਤਾਬਕ ਬਦਲੋ।**

______

## VMware VM STIG ਆਟੋਮੇਟ ਕਰੋ

ESXi ਹੋਸਟਾਂ ਦੀ ਸੁਰੱਖਿਆ ਦੇ ਨਾਲ VMware ਬੁਨਿਆਦੀ ਢਾਂਚੇ ਦੀਆਂ ਵਰਚੁਅਲ ਮਸ਼ੀਨਾਂ ਉੱਤੇ ਵੀ STIG ਨਿਯੰਤਰਣ ਲਾਗੂ ਕਰੋ। PowerCLI STIG ਹਦਾਇਤਾਂ ਅਨੁਸਾਰ VM ਸੰਰਚਨਾ ਆਟੋਮੇਟ ਕਰਨ ਵਿੱਚ ਮਦਦ ਕਰਦਾ ਹੈ।

## ਸਕ੍ਰਿਪਟ: VMware VM STIG ਆਟੋਮੇਸ਼ਨ

ਹੇਠਾਂ ਦਿੱਤੀ PowerCLI ਸਕ੍ਰਿਪਟ ਦਿਖਾਉਂਦੀ ਹੈ ਕਿ ਵਰਚੁਅਲ ਮਸ਼ੀਨਾਂ ਲਈ ਚੁਣੇ STIG ਨਿਯੰਤਰਣ ਕਿਵੇਂ ਆਟੋਮੇਟ ਕਰਨੇ ਹਨ:

```powershell
Set-PowerCLIConfiguration -InvalidCertificateAction Ignore -Confirm:$false
Set-PowerCLIConfiguration -Scope User -ParticipateInCEIP $false -Confirm:$false
Connect-VIServer -Server 127.0.0.1
$cluster = Get-Cluster -Name "Cluster"
$folder = Get-Folder -Name "Folder"

#ਸਰੋਤ: https://github.com/rlakey/vmware-stig-powercli/blob/master/VMware_vSphere_6.7_VM_STIG_Remediation.ps1
$vmconfig = @{
    #ਹਾਰਡਨਿੰਗ/STIG ਸੈਟਿੰਗਾਂ
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
    Write-Output "...$vcenter ਦੇ $vm ਉੱਤੇ advanced settings ਠੀਕ ਕੀਤੀਆਂ ਜਾ ਰਹੀਆਂ ਹਨ"
    ForEach ($setting in ($vmconfig.vmAdvSettings.GetEnumerator() | Sort-Object Name)) {
        #ਦਿੱਤੀ ਹਰ ਸੈਟਿੰਗ ਲਈ ਮੁੱਲ ਪ੍ਰਾਪਤ ਕਰੋ
        $settingname = $setting.name
        $settingvalue = $setting.value
        If ($asetting = $vm | Get-AdvancedSetting -Name $settingname) {
            If ($asetting.value -eq $settingvalue) {
                Write-Output "...$vm ਉੱਤੇ $settingname ਪਹਿਲਾਂ ਹੀ $settingvalue ਲਈ ਠੀਕ ਕੌਂਫਿਗਰ ਹੈ"
            }
            else {
                Write-Output "...$vm ਉੱਤੇ $settingname ਦਾ ਮੁੱਲ ਗਲਤ $($asetting.value) ਸੀ; $settingvalue ਸੈੱਟ ਕੀਤਾ ਜਾ ਰਿਹਾ ਹੈ"
                $asetting | Set-AdvancedSetting -Value $settingvalue -Confirm:$false
            }
        }
        else {
            Write-Output "...$vm ਉੱਤੇ $settingname ਮੌਜੂਦ ਨਹੀਂ; ਬਣਾਈ ਜਾ ਰਹੀ ਹੈ..."
            $vm | New-AdvancedSetting -Name $settingname -Value $settingvalue -Confirm:$false
        }
        Write-Output "...ਲੋੜ ਪੈਣ ’ਤੇ $vcenter ਦੇ $vm ਤੋਂ advanced settings ਹਟਾਈਆਂ ਜਾ ਰਹੀਆਂ ਹਨ"
        ForEach ($setting in ($vmconfig.vmAdvSettingsRemove | Sort-Object Name)) {
            #ਜਾਂਚੋ ਕਿ ਮੌਜੂਦਾ ਸੈਟਿੰਗ ਮੌਜੂਦ ਹੈ
            If ($asetting = $vm | Get-AdvancedSetting -Name $setting) {
                Write-Output "...$vm ਉੱਤੇ $setting ਮੌਜੂਦ ਹੈ...ਹਟਾਈ ਜਾ ਰਹੀ ਹੈ"
                $asetting | Remove-AdvancedSetting -Confirm:$false
            }
            else {
                Write-Output "...$vm ਉੱਤੇ $setting ਮੌਜੂਦ ਨਹੀਂ"
            }
        }   
        If ($vm.extensiondata.Config.MigrateEncryption -eq $vmconfig.vmotionEncryption) {
            Write-Output "...$vm ਉੱਤੇ vMotion encryption ਠੀਕ ਤਰ੍ਹਾਂ $($vmconfig.vmotionEncryption) ਲਈ ਸੈੱਟ ਹੈ"
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

ਇਹ ਸਕ੍ਰਿਪਟ ਹੇਠਾਂ ਦਿੱਤੇ ਕੰਮ ਕਰਦੀ ਹੈ:

- **VMware VCSA STIG ਸਕ੍ਰਿਪਟ ਵਾਂਗ ਸ਼ੁਰੂ ਵਿੱਚ PowerCLI ਵਾਤਾਵਰਣ ਸੰਰਚਿਤ ਕਰਦੀ ਹੈ।**
- **vCenter ਨਾਲ ਜੁੜਦੀ ਹੈ ਅਤੇ ਟੀਚਾ VM ਰੱਖਣ ਵਾਲਾ ਕਲੱਸਟਰ ਅਤੇ ਫੋਲਡਰ ਚੁਣਦੀ ਹੈ।**
- **`$vmconfig` ਵੇਰੀਏਬਲ ਵਿੱਚ VM ਲਈ STIG ਸੈਟਿੰਗਾਂ ਹਨ। ਇਨ੍ਹਾਂ ਵਿੱਚ ਕਾਪੀ ਅਤੇ ਪੇਸਟ ਬੰਦ ਕਰਨਾ ਅਤੇ ਰਿਮੋਟ ਡਿਸਪਲੇਅ ਕਨੈਕਸ਼ਨ ਸੀਮਿਤ ਕਰਨ ਵਰਗੀਆਂ ਉੱਨਤ ਸੈਟਿੰਗਾਂ ਸ਼ਾਮਲ ਹਨ।**
- **ਚੁਣੇ ਕਲੱਸਟਰ ਅਤੇ ਫੋਲਡਰ ਦੀ ਹਰੇਕ VM ਉੱਤੇ STIG ਸੈਟਿੰਗਾਂ ਲਾਗੂ ਕਰਦੀ ਹੈ।**
- **VM ਲਈ vMotion ਇਨਕ੍ਰਿਪਸ਼ਨ ਵੀ ਸੰਰਚਿਤ ਕਰਦੀ ਹੈ।**

ਇਹ ਉਦਾਹਰਨ ਸਕ੍ਰਿਪਟ ਹੈ। ਇਸਨੂੰ ਆਪਣੇ ਵਾਤਾਵਰਣ ਅਤੇ ਲਾਗੂ STIG ਲੋੜਾਂ ਮੁਤਾਬਕ ਬਦਲੋ।

_____

## ਹੋਰ ਸਰੋਤ

- **DoD STIG VIB ਪਹਿਲਾਂ ਸੰਸਕਰਣ 5.0 ਤੋਂ 6.7 ਲਈ [ਉਪਲਬਧ ਸੀ](https://flings.vmware.com/dod-security-technical-implementation-guide-stig-esxi-vib), ਪਰ ਹੁਣ ਉਪਲਬਧ ਨਹੀਂ ਹੈ।**
- [Ryan Lakey](https://core.vmware.com/users/ryan-lakey) VMware ਉੱਤੇ DoD STIG ਲਾਗੂ ਕਰਨ ਲਈ ਲਾਭਦਾਇਕ ਹਦਾਇਤਾਂ ਦਿੰਦੇ ਹਨ। ਇਨ੍ਹਾਂ ਨੂੰ ਪੜ੍ਹਨ ਦੀ ਸਿਫ਼ਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ।
    - [VMware vSphere 8 STIG](https://core.vmware.com/resource/vmware-vsphere-8-stig)
    - [VMware vSphere 7 STIG](https://core.vmware.com/vsphere-7-stig)
    - [VMware vSphere 6.7 STIG](https://core.vmware.com/vmware-vsphere-67-stig)
    - [VMware STIG PowerCLI](https://github.com/rlakey/vmware-stig-powercli)
        - [VMware VCSA 6.7 STIG ਬੇਸਲਾਈਨ](https://github.com/rlakey/vmware-vcsa-6.7-stig-baseline)
        - [VMware VM 6.7 STIG ਬੇਸਲਾਈਨ](https://github.com/rlakey/vmware-vm-6.7-stig-baseline)
_____

## ਨਤੀਜਾ

**VMware STIG ਲਾਗੂ ਕਰਨ ਨਾਲ VMware ਬੁਨਿਆਦੀ ਢਾਂਚੇ ਦੀ ਸੁਰੱਖਿਆ ਅਤੇ ਲਾਗੂ ਲੋੜਾਂ ਦੀ ਪਾਲਣਾ ਵਿੱਚ ਮਦਦ ਮਿਲਦੀ ਹੈ। PowerCLI ESXi ਹੋਸਟਾਂ ਅਤੇ ਵਰਚੁਅਲ ਮਸ਼ੀਨਾਂ ਉੱਤੇ STIG ਨਿਯੰਤਰਣ ਲਾਗੂ ਕਰਨ ਦੀ ਪ੍ਰਕਿਰਿਆ ਆਟੋਮੇਟ ਅਤੇ ਸੌਖੀ ਕਰਦਾ ਹੈ।**

ਇਸ ਲੇਖ ਵਿੱਚ PowerCLI ਨਾਲ VMware ESXi ਅਤੇ VM STIG ਆਟੋਮੇਟ ਕਰਨ ਬਾਰੇ ਦੱਸਿਆ ਗਿਆ। ਇਸ ਵਿੱਚ ਇੰਸਟਾਲੇਸ਼ਨ ਦੀਆਂ ਲੋੜਾਂ, ਮਿਸਾਲੀ ਸਕ੍ਰਿਪਟਾਂ ਅਤੇ ਉਨ੍ਹਾਂ ਨੂੰ ਆਪਣੇ ਵਾਤਾਵਰਣ ਮੁਤਾਬਕ ਢਾਲਣ ਦੀ ਮਹੱਤਤਾ ਸ਼ਾਮਲ ਸੀ।

**PowerCLI ਅਤੇ STIG ਹਦਾਇਤਾਂ ਨਾਲ ਪ੍ਰਸ਼ਾਸਕ VMware ਤੈਨਾਤੀਆਂ ਨੂੰ ਕੁਸ਼ਲਤਾ ਨਾਲ ਸੁਰੱਖਿਅਤ ਕਰ ਸਕਦੇ ਹਨ, ਹੱਥੀਂ ਕੰਮ ਘਟਾ ਸਕਦੇ ਹਨ ਅਤੇ ਇਕਸਾਰ ਸੰਰਚਨਾ ਕਾਇਮ ਰੱਖ ਸਕਦੇ ਹਨ।**

## ਹਵਾਲੇ

- [DoD STIG VIB](https://flings.vmware.com/dod-security-technical-implementation-guide-stig-esxi-vib)
- [PowerCLI 11.3](https://www.powershellgallery.com/packages/VMware.PowerCLI/11.3.0.13990089)
- [PowerShell 5 ਜਾਂ ਇਸ ਤੋਂ ਨਵਾਂ](https://docs.microsoft.com/en-us/skypeforbusiness/set-up-your-computer-for-windows-powershell/download-and-install-windows-powershell-5-1)
- [ESXi 6.7 U2 ਜਾਂ ਇਸ ਤੋਂ ਨਵਾਂ](https://my.vmware.com/web/vmware/downloads/details?downloadGroup=ESXI670&productId=742)
