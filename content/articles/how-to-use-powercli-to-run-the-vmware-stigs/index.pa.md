---
title: "VMware ਸੁਰੱਖਿਆ ਵਿੱਚ ਮਾਹਰ ਬਣੋ"
date: 2023-08-03
lastmod: 2026-11-12
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

ਇਹ ਸਕ੍ਰਿਪਟ ਹੇਠਾਂ ਦਿੱਤੇ ਕੰਮ ਕਰਦੀ ਹੈ:

- **VMware VCSA STIG ਸਕ੍ਰਿਪਟ ਵਾਂਗ ਸ਼ੁਰੂ ਵਿੱਚ PowerCLI ਵਾਤਾਵਰਣ ਸੰਰਚਿਤ ਕਰਦੀ ਹੈ।**
- **vCenter ਨਾਲ ਜੁੜਦੀ ਹੈ ਅਤੇ ਟੀਚਾ VM ਰੱਖਣ ਵਾਲਾ ਕਲੱਸਟਰ ਅਤੇ ਫੋਲਡਰ ਚੁਣਦੀ ਹੈ।**
- **`$vmconfig` ਵੇਰੀਏਬਲ ਵਿੱਚ VM ਲਈ STIG ਸੈਟਿੰਗਾਂ ਹਨ। ਇਨ੍ਹਾਂ ਵਿੱਚ ਕਾਪੀ ਅਤੇ ਪੇਸਟ ਬੰਦ ਕਰਨਾ ਅਤੇ ਰਿਮੋਟ ਡਿਸਪਲੇਅ ਕਨੈਕਸ਼ਨ ਸੀਮਿਤ ਕਰਨ ਵਰਗੀਆਂ ਉੱਨਤ ਸੈਟਿੰਗਾਂ ਸ਼ਾਮਲ ਹਨ।**
- **ਚੁਣੇ ਕਲੱਸਟਰ ਅਤੇ ਫੋਲਡਰ ਦੀ ਹਰੇਕ VM ਉੱਤੇ STIG ਸੈਟਿੰਗਾਂ ਲਾਗੂ ਕਰਦੀ ਹੈ।**
- **VM ਲਈ vMotion ਇਨਕ੍ਰਿਪਸ਼ਨ ਵੀ ਸੰਰਚਿਤ ਕਰਦੀ ਹੈ।**

ਇਹ ਉਦਾਹਰਨ ਸਕ੍ਰਿਪਟ ਹੈ। ਇਸਨੂੰ ਆਪਣੇ ਵਾਤਾਵਰਣ ਅਤੇ ਲਾਗੂ STIG ਲੋੜਾਂ ਮੁਤਾਬਕ ਬਦਲੋ।

_____

## ਹੋਰ ਸਰੋਤ

- **DoD STIG VIB** ਪਹਿਲਾਂ ਸੰਸਕਰਣ 5.0 ਤੋਂ 6.7 ਲਈ [ਉਪਲਬਧ ਸੀ](https://flings.vmware.com/dod-security-technical-implementation-guide-stig-esxi-vib), ਪਰ ਹੁਣ ਉਪਲਬਧ ਨਹੀਂ ਹੈ।
- **[Ryan Lakey](https://core.vmware.com/users/ryan-lakey)** VMware ਉੱਤੇ DoD STIG ਲਾਗੂ ਕਰਨ ਲਈ ਲਾਭਦਾਇਕ ਹਦਾਇਤਾਂ ਦਿੰਦੇ ਹਨ। ਇਨ੍ਹਾਂ ਨੂੰ ਪੜ੍ਹਨ ਦੀ ਸਿਫ਼ਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ।
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
