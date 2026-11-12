---
title: "VMware নিরাপত্তায় দক্ষতা অর্জন"
date: 2023-08-03
lastmod: 2026-11-12
toc: true
draft: false
description: "এই বিস্তৃত নির্দেশিকায় PowerCLI দিয়ে VMware STIG প্রয়োগ করে VMware পরিবেশ সুরক্ষিত করার পদ্ধতি জানুন।"
genre: ["সাইবার নিরাপত্তা", "ভার্চুয়ালাইজেশন", "আইটি অবকাঠামো", "অটোমেশন", "PowerShell", "VMware", "STIG", "সম্মতি", "স্ক্রিপ্টিং", "ডেটা সেন্টার"]
tags: ["PowerCLI", "VMware STIG", "VMware নিরাপত্তা", "অটোমেশন", "স্ক্রিপ্টিং", "PowerShell", "ESXi", "ভার্চুয়ালাইজেশন", "সম্মতি", "সাইবার নিরাপত্তা", "VMware STIG-এর জন্য PowerCLI ব্যবহারের পদ্ধতি", "PowerCLI দিয়ে VMware নিরাপত্তা স্বয়ংক্রিয় করা", "VMware STIG প্রয়োগের PowerCLI স্ক্রিপ্ট", "ESXi নিরাপত্তায় PowerCLI অটোমেশন", "PowerCLI দিয়ে VMware পরিবেশ সুরক্ষিত করা"]
cover: "/img/cover/An_illustration_depicting_a_computer_server_sh.webp"
coverAlt: "তালাবদ্ধ একটি কম্পিউটার সার্ভারের চিত্র, যা সুরক্ষিত VMware অবকাঠামোর প্রতীক।"
coverCaption: "PowerCLI দিয়ে VMware পরিবেশ সুরক্ষিত করা"
---

**PowerCLI দিয়ে VMware STIG প্রয়োগের পদ্ধতি**

PowerCLI হলো PowerShell ব্যবহার করে VMware পরিবেশ পরিচালনা ও কনফিগার করার অটোমেশন এবং স্ক্রিপ্টিং টুল। এই নিবন্ধে ESXi এবং ভার্চুয়াল মেশিন সুরক্ষায় VMware STIG (Security Technical Implementation Guide) প্রয়োগ করতে PowerCLI ব্যবহারের পদ্ধতি দেখানো হয়েছে।

## ভূমিকা

**VMware STIG** VMware অবকাঠামো নিরাপদে কনফিগার ও পরিচালনার নির্দেশনা এবং সুপারিশ দেয়। এটি অনুসরণ করলে প্রতিষ্ঠানগুলো VMware স্থাপনার নিরাপত্তা বাড়াতে এবং **Defense Information Systems Agency (DISA) STIG**-এর মতো প্রযোজ্য সরকারি নিয়ম মানতে পারে।

## PowerCLI কী?

**PowerCLI** VMware পরিবেশ পরিচালনার কমান্ড-লাইন ইন্টারফেস ও স্ক্রিপ্টিং টুল। এটি PowerShell-এর ওপর তৈরি এবং VMware প্রশাসনের জন্য বিশেষভাবে তৈরি বহু cmdlet দেয়। প্রশাসকেরা পুনরাবৃত্তিমূলক কাজ স্বয়ংক্রিয় করতে, কনফিগারেশন পরিবর্তন করতে এবং VMware অবকাঠামোর তথ্য সংগ্রহ করতে এটি ব্যবহার করেন।

### ইনস্টলেশন ও পূর্বশর্ত

PowerCLI এবং VMware STIG নিয়ে কাজ শুরুর আগে নিচের পূর্বশর্তগুলো নিশ্চিত করুন:

- [**PowerCLI 11.3**](https://www.powershellgallery.com/packages/VMware.PowerCLI/11.3.0.13990089): PowerShell Gallery থেকে `Install-Module VMware.PowerCLI -force` কমান্ড দিয়ে PowerCLI ইনস্টল করুন।
- [**PowerShell 5 বা পরের সংস্করণ**](https://docs.microsoft.com/en-us/skypeforbusiness/set-up-your-computer-for-windows-powershell/download-and-install-windows-powershell-5-1): PowerShell 5 বা পরের সংস্করণ ইনস্টল আছে কি না নিশ্চিত করুন।
- [**ESXi 6.7 U2 বা পরের সংস্করণ**](https://my.vmware.com/web/vmware/downloads/details?downloadGroup=ESXI670&productId=742): ESXi 6.7 U2 বা পরের সংস্করণ ব্যবহার করুন।

## VMware VCSA STIG স্বয়ংক্রিয় করা

VMware ESXi STIG-এ ESXi হোস্ট সুরক্ষার নির্দেশনা আছে। STIG নিয়ন্ত্রণগুলো স্বয়ংক্রিয়ভাবে প্রয়োগ করলে প্রক্রিয়াটি সহজ হয় এবং একাধিক হোস্টে একই ধরনের কনফিগারেশন বজায় থাকে।

### বিবেচ্য বিষয়

অটোমেশন শুরু করার আগে এসব বিষয় বিবেচনা করুন:

- **ESXi হোস্ট বা ক্লাস্টারের কোনো ভার্চুয়াল মেশিন বা গেস্টের CD, USB বা ফ্লপি ডিস্ক সুবিধা দরকার নেই কি না নিশ্চিত করুন।**
- **vCenter-এর সঙ্গে যুক্ত সব ESXi হোস্ট এবং গেস্টে STIG প্রয়োগ করুন।**
- **প্রক্রিয়ায় সমস্যা দেখা দিলে সমাধানের জন্য ট্রাবলশুটিং দক্ষতা প্রয়োজন।**

### স্ক্রিপ্ট: VMware VCSA STIG অটোমেশন

নিচের PowerCLI স্ক্রিপ্টটি VCSA-র জন্য নির্বাচিত STIG নিয়ন্ত্রণগুলো স্বয়ংক্রিয়ভাবে প্রয়োগ করে:

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

স্ক্রিপ্টটির কাজগুলো হলো:

- **প্রথমে PowerCLI কনফিগার করে, সার্টিফিকেট যাচাই বন্ধ করে এবং Customer Experience Improvement Program (CEIP)-এ অংশগ্রহণ বন্ধ করে।**
- **এরপর `$vcenters` ভেরিয়েবলে নির্দিষ্ট vCenter সার্ভারগুলোতে সংযোগ করে।**
- **প্রতিটি STIG নিয়ন্ত্রণ PowerCLI cmdlet দিয়ে প্রয়োগ করে। যেমন, নির্দিষ্ট vCenter সার্ভারের জন্য `config.log.level`-এর মান info সেট করে।**
- **`config.vpxd.hostPasswordLength` এবং `VirtualCenter.VimPasswordExpirationInDays`-এর মতো নিয়ন্ত্রণও সামলায়।**
- **শেষে নিরাপত্তা নীতি ও অন্যান্য সেটিং পরীক্ষা ও কনফিগার করে।**
- **এটি একটি উদাহরণ স্ক্রিপ্ট। আপনার পরিবেশ ও STIG-এর প্রয়োজন অনুযায়ী এটি পরিবর্তন করুন।**

______

## VMware VM STIG স্বয়ংক্রিয় করা

ESXi হোস্ট সুরক্ষার পাশাপাশি VMware অবকাঠামোর ভার্চুয়াল মেশিনেও STIG নিয়ন্ত্রণ প্রয়োগ করতে হবে। STIG নির্দেশনা অনুযায়ী VM কনফিগারেশন স্বয়ংক্রিয় করতে PowerCLI সহায়তা করে।

## স্ক্রিপ্ট: VMware VM STIG অটোমেশন

নিচের PowerCLI স্ক্রিপ্টটি VM-এর জন্য নির্বাচিত STIG নিয়ন্ত্রণ কীভাবে স্বয়ংক্রিয় করা যায় তা দেখায়:

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

স্ক্রিপ্টটির কাজগুলো হলো:

- **VMware VCSA STIG স্ক্রিপ্টের মতো শুরুতেই PowerCLI পরিবেশ কনফিগার করে।**
- **vCenter-এ সংযোগ করে এবং লক্ষ্য VM থাকা ক্লাস্টার ও ফোল্ডার নির্বাচন করে।**
- **`$vmconfig` ভেরিয়েবলে VM STIG সেটিং থাকে। এর মধ্যে কপি-পেস্ট বন্ধ করা ও রিমোট ডিসপ্লে সংযোগ সীমিত করার মতো উন্নত সেটিং রয়েছে।**
- **নির্বাচিত ক্লাস্টার ও ফোল্ডারের প্রতিটি VM-এ STIG সেটিং প্রয়োগ করে।**
- **VM-এর vMotion এনক্রিপশনও কনফিগার করে।**

এটি উদাহরণ স্ক্রিপ্ট। আপনার পরিবেশ ও প্রযোজ্য STIG-এর প্রয়োজন অনুযায়ী পরিবর্তন করুন।

_____

## অতিরিক্ত সম্পদ

- **DoD STIG VIB** আগে 5.0 থেকে 6.7 সংস্করণের জন্য [পাওয়া যেত](https://flings.vmware.com/dod-security-technical-implementation-guide-stig-esxi-vib), তবে এখন আর পাওয়া যায় না।
- **[Ryan Lakey](https://core.vmware.com/users/ryan-lakey)** VMware-এ DoD STIG প্রয়োগের জন্য উপযোগী নির্দেশনা দিয়েছেন। সেগুলো পড়ার সুপারিশ করছি।
    - [VMware vSphere 8 STIG](https://core.vmware.com/resource/vmware-vsphere-8-stig)
    - [VMware vSphere 7 STIG](https://core.vmware.com/vsphere-7-stig)
    - [VMware vSphere 6.7 STIG](https://core.vmware.com/vmware-vsphere-67-stig)
    - [VMware STIG PowerCLI](https://github.com/rlakey/vmware-stig-powercli)
        - [VMware VCSA 6.7 STIG বেসলাইন](https://github.com/rlakey/vmware-vcsa-6.7-stig-baseline)
        - [VMware VM 6.7 STIG বেসলাইন](https://github.com/rlakey/vmware-vm-6.7-stig-baseline)
_____

## উপসংহার

**VMware STIG প্রয়োগ VMware অবকাঠামো সুরক্ষিত করতে এবং প্রযোজ্য নিয়ম মানতে সহায়তা করে। PowerCLI ESXi হোস্ট ও ভার্চুয়াল মেশিনে STIG নিয়ন্ত্রণ প্রয়োগ স্বয়ংক্রিয় ও সহজ করে।**

এই নিবন্ধে PowerCLI দিয়ে VMware ESXi ও VM STIG স্বয়ংক্রিয় করার পদ্ধতি আলোচনা করা হয়েছে। ইনস্টলেশনের শর্তগুলো ব্যাখ্যা করা হয়েছে, উদাহরণ স্ক্রিপ্ট দেওয়া হয়েছে এবং পরিবেশের প্রয়োজন অনুযায়ী স্ক্রিপ্ট বদলানোর গুরুত্ব তুলে ধরা হয়েছে।

**PowerCLI এবং STIG নির্দেশনা অনুসরণ করে প্রশাসকেরা VMware স্থাপনা দক্ষতার সঙ্গে সুরক্ষিত করতে, হাতে করা কাজ কমাতে এবং সামঞ্জস্যপূর্ণ কনফিগারেশন বজায় রাখতে পারেন।**

## সূত্র

- [DoD STIG VIB](https://flings.vmware.com/dod-security-technical-implementation-guide-stig-esxi-vib)
- [PowerCLI 11.3](https://www.powershellgallery.com/packages/VMware.PowerCLI/11.3.0.13990089)
- [PowerShell 5 বা পরের সংস্করণ](https://docs.microsoft.com/en-us/skypeforbusiness/set-up-your-computer-for-windows-powershell/download-and-install-windows-powershell-5-1)
- [ESXi 6.7 U2 বা পরের সংস্করণ](https://my.vmware.com/web/vmware/downloads/details?downloadGroup=ESXI670&productId=742)
