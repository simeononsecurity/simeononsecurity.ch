---
title: "VMware सुरक्षा में निपुण बनें"
date: 2023-08-03
lastmod: 2026-11-13
toc: true
draft: false
description: "इस व्यापक मार्गदर्शिका में जानें कि PowerCLI से VMware STIG लागू करके VMware वातावरण को कैसे सुरक्षित करें।"
genre: ["साइबर सुरक्षा", "वर्चुअलाइजेशन", "आईटी अवसंरचना", "स्वचालन", "PowerShell", "VMware", "STIG", "अनुपालन", "स्क्रिप्टिंग", "डेटा सेंटर"]
tags: ["PowerCLI", "VMware STIG", "VMware सुरक्षा", "स्वचालन", "स्क्रिप्टिंग", "PowerShell", "ESXi", "वर्चुअलाइजेशन", "अनुपालन", "साइबर सुरक्षा", "VMware STIG के लिए PowerCLI का उपयोग कैसे करें", "PowerCLI से VMware सुरक्षा स्वचालित करें", "VMware STIG लागू करने की PowerCLI स्क्रिप्ट", "ESXi सुरक्षा के लिए PowerCLI स्वचालन", "PowerCLI से VMware वातावरण सुरक्षित करें"]
cover: "/img/cover/An_illustration_depicting_a_computer_server_sh.webp"
coverAlt: "ताले से सुरक्षित कंप्यूटर सर्वर का चित्र, जो सुरक्षित VMware अवसंरचना का प्रतीक है।"
coverCaption: "PowerCLI से अपने VMware वातावरण को सुरक्षित करें"
---

**PowerCLI से VMware STIG कैसे लागू करें**

PowerCLI, PowerShell के माध्यम से VMware वातावरण प्रबंधित और कॉन्फ़िगर करने वाला स्वचालन तथा स्क्रिप्टिंग टूल है। यह लेख बताता है कि ESXi और वर्चुअल मशीनों पर VMware STIG (Security Technical Implementation Guide) लागू करने के लिए PowerCLI का उपयोग कैसे करें।

## परिचय

**VMware STIG** VMware अवसंरचना को सुरक्षित रूप से कॉन्फ़िगर और प्रबंधित करने के लिए दिशानिर्देश और सुझाव देता है। इसका पालन करने से संगठन VMware परिनियोजन की सुरक्षा बेहतर कर सकते हैं और **Defense Information Systems Agency (DISA) STIG** जैसे लागू सरकारी नियमों का पालन कर सकते हैं।

## PowerCLI क्या है?

**PowerCLI** VMware वातावरणों के प्रबंधन के लिए कमांड-लाइन इंटरफ़ेस और स्क्रिप्टिंग टूल है। यह PowerShell पर आधारित है और VMware प्रशासन के लिए विशेष cmdlet का विस्तृत सेट देता है। प्रशासक इससे दोहराए जाने वाले काम स्वचालित करते हैं, कॉन्फ़िगरेशन बदलते हैं और VMware अवसंरचना से जानकारी जुटाते हैं।

### इंस्टॉलेशन और आवश्यकताएँ

PowerCLI और VMware STIG के साथ शुरू करने से पहले ये आवश्यकताएँ जाँचें:

- [**PowerCLI 11.3**](https://www.powershellgallery.com/packages/VMware.PowerCLI/11.3.0.13990089): PowerShell Gallery से `Install-Module VMware.PowerCLI -force` कमांड चलाकर PowerCLI इंस्टॉल करें।
- [**PowerShell 5 या नया**](https://docs.microsoft.com/en-us/skypeforbusiness/set-up-your-computer-for-windows-powershell/download-and-install-windows-powershell-5-1): सुनिश्चित करें कि PowerShell 5 या नया संस्करण इंस्टॉल है।
- [**ESXi 6.7 U2 या नया**](https://my.vmware.com/web/vmware/downloads/details?downloadGroup=ESXI670&productId=742): ESXi 6.7 U2 या नया संस्करण इस्तेमाल करें।

## VMware VCSA STIG स्वचालित करें

VMware ESXi STIG, ESXi होस्ट सुरक्षित करने के दिशानिर्देश देता है। STIG नियंत्रणों का स्वचालन प्रक्रिया आसान करता है और कई होस्ट पर एक जैसी कॉन्फ़िगरेशन बनाए रखता है।

### ध्यान देने योग्य बातें

स्वचालन से पहले इन बातों पर ध्यान दें:

- **पुष्टि करें कि ESXi होस्ट या क्लस्टर की किसी वर्चुअल मशीन या गेस्ट को CD, USB या फ्लॉपी डिस्क की सुविधा की आवश्यकता नहीं है।**
- **vCenter से जुड़े सभी ESXi होस्ट और गेस्ट सिस्टम पर STIG लागू करें।**
- **प्रक्रिया के दौरान आने वाली समस्याओं को हल करने के लिए ट्रबलशूटिंग कौशल रखें।**

### स्क्रिप्ट: VMware VCSA STIG स्वचालन

यह PowerCLI स्क्रिप्ट VCSA के लिए चुने गए STIG नियंत्रणों को स्वचालित रूप से लागू करती है:

```powershell
Set-PowerCLIConfiguration -InvalidCertificateAction Ignore -Confirm:$false
Set-PowerCLIConfiguration -Scope User -ParticipateInCEIP $false -Confirm:$false
$vcenters = 127.0.0.1, 127.0.0.2

#हर vCenter सर्वर से कनेक्ट करें
ForEach ($vc in $vcenters) {
    Connect-VIServer -Server $vc
}

#स्वचालित

Write-Host "भेद्यता ID: V-243098 नियम ID: SV-243098r719537_rule STIG ID: VCTR-67-000036"
Write-Host "यदि 'config.log.level' का मान "info" पर सेट नहीं है या मौजूद नहीं है, तो यह एक निष्कर्ष है।"
ForEach ($vc in $vcenters) {
    Get-AdvancedSetting -Entity $vc -Name config.log.level | Set-AdvancedSetting -Value info
    Get-AdvancedSetting -Entity $vc -Name config.log.level
}

Write-Host "भेद्यता ID: V-243090 नियम ID: SV-243090r719513_rule STIG ID: VCTR-67-000024"
Write-Host "यदि 'config.vpxd.hostPasswordLength' का मान "32" के अलावा है, तो यह एक निष्कर्ष है।
यदि सेटिंग मौजूद नहीं है, तो यह निष्कर्ष नहीं है।"
ForEach ($vc in $vcenters) {
    Get-AdvancedSetting -Entity $vc -Name config.vpxd.hostPasswordLength | Set-AdvancedSetting -Value 32
    Get-AdvancedSetting -Entity $vc -Name config.vpxd.hostPasswordLength
}


Write-Host "भेद्यता ID: V-243089 नियम ID: SV-243089r719510_rule STIG ID: VCTR-67-000023"
Write-Host "यदि 'VirtualCenter.VimPasswordExpirationInDays' का मान "30" के अलावा है या मौजूद नहीं है, तो यह एक निष्कर्ष है।"
ForEach ($vc in $vcenters) {
    Try {
        Get-AdvancedSetting -Entity $vc -Name VirtualCenter.VimPasswordExpirationInDays | Set-AdvancedSetting -Value 30
    }
    Catch {
        New-AdvancedSetting -Entity $vc -Name VirtualCenter.VimPasswordExpirationInDays -Value 30
    }
}

Write-Host "भेद्यता ID: V-243084 नियम ID: SV-243085r719498_rule STIG ID: VCTR-67-000016"
Write-Host "यदि NetFlow कॉन्फ़िगर है और कलेक्टर IP ज्ञात व दस्तावेज़ीकृत नहीं है, तो यह एक निष्कर्ष है।"
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

Write-Host "भेद्यता ID: V-243084 नियम ID: SV-243084r719495_rule STIG ID: VCTR-67-000015"
Write-Host "vCenter Server को वितरित पोर्ट समूह की Promiscuous Mode नीति को अस्वीकार पर सेट करना होगा।"
Get-VDSwitch | Get-VDSecurityPolicy | Set-VDSecurityPolicy -AllowPromiscuous $false
Get-VDPortgroup | Where-Object { $_.IsUplink -eq $false } | Get-VDSecurityPolicy | Set-VDSecurityPolicy -AllowPromiscuous $false
Get-VDSwitch | Get-VDSecurityPolicy
Get-VDPortgroup | Where-Object { $_.IsUplink -eq $false } | Get-VDSecurityPolicy


Write-Host "भेद्यता ID: V-243083 नियम ID: SV-243083r719492_rule STIG ID: VCTR-67-000014"
Write-Host "vCenter Server को वितरित पोर्ट समूह की MAC Address Change नीति को अस्वीकार पर सेट करना होगा।"
Get-VDSwitch | Get-VDSecurityPolicy | Set-VDSecurityPolicy -MacChanges $false
Get-VDPortgroup | Where-Object { $_.IsUplink -eq $false } | Get-VDSecurityPolicy | Set-VDSecurityPolicy -MacChanges $false
Get-VDPortgroup | Where-Object { $_.IsUplink -eq $false } | Get-VDSecurityPolicy

Write-Host "भेद्यता ID: V-243082 नियम ID: SV-243082r719489_rule STIG ID: VCTR-67-000013"
Write-Host "vCenter Server को वितरित पोर्ट समूह की Forged Transmits नीति को अस्वीकार पर सेट करना होगा।"
Get-VDSwitch | Get-VDSecurityPolicy | Set-VDSecurityPolicy -ForgedTransmits $false
Get-VDPortgroup | Where-Object { $_.IsUplink -eq $false } | Get-VDSecurityPolicy | Set-VDSecurityPolicy -ForgedTransmits $false
Get-VDSwitch | Get-VDSecurityPolicy
Get-VDPortgroup | Where-Object { $_.IsUplink -eq $false } | Get-VDSecurityPolicy

Write-Host "भेद्यता ID: V-243081 नियम ID: SV-243081r719486_rule STIG ID: VCTR-67-000012"
Write-Host "vCenter Server को वितरित वर्चुअल स्विच की स्वास्थ्य जाँच अक्षम करनी होगी।"
Get-View -ViewType DistributedVirtualSwitch | Where-Object { ($_.config.HealthCheckConfig | Where-Object { $_.enable -notmatch "False" }) } | ForEach-Object { $_.UpdateDVSHealthCheckConfig(@((New-Object Vmware.Vim.VMwareDVSVlanMtuHealthCheckConfig -property @{enable = 0 }), (New-Object Vmware.Vim.VMwareDVSTeamingHealthCheckConfig -property @{enable = 0 }))) }
$vds = Get-VDSwitch
$vds.ExtensionData.Config.HealthCheckConfig

Write-Host "भेद्यता ID: V-243077 नियम ID: SV-243077r719474_rule STIG ID: VCTR-67-00000"
Write-Host "सूचना-बाढ़ और सेवा-अस्वीकार (DoS) हमलों के प्रभाव सीमित करने के लिए vCenter Server को Network I/O Control (NIOC) सक्षम करके अतिरिक्त क्षमता, बैंडविड्थ या अन्य अतिरेक प्रबंधित करना होगा।"
Write-Host "यदि syslog विफलताओं की सूचना देने के लिए अलर्ट नहीं बनाया और सक्षम किया गया है, तो यह एक निष्कर्ष है।"
ForEach ($vdswitch in (Get-VDSwitch.name)){
    (Get-VDSwitch $vdswitch | Get-View).EnableNetworkResourceManagement($true)
}
Get-VDSwitch | Select-Object Name, @{N = "NIOC Enabled"; E = { $_.ExtensionData.config.NetworkResourceManagementEnabled } }

#मैन्युअल समीक्षा

Write-Host "भेद्यता ID: V-243076 नियम ID: SV-243076r719471_rule STIG ID: VCTR-67-000005"
Write-Host "vCenter Server उपयोगकर्ताओं को सही भूमिकाएँ दी जानी चाहिए।"
Write-Host "सेवा खातों और उपयोगकर्ताओं के आवश्यक विशेषाधिकार दस्तावेज़ किए जाने चाहिए।
यदि किसी उपयोगकर्ता या सेवा खाते के पास आवश्यकता से अधिक विशेषाधिकार हैं, तो यह एक निष्कर्ष है।"
Get-VIPermission | Sort-Object Role | Select-Object Role, Principal, Entity, Propagate, IsGroup | Format-Table -Auto

Write-Host "भेद्यता ID: V-243119 नियम ID: SV-243119r719600_rule STIG ID: VCTR-67-000064"
Write-Host "यदि Administrator के अलावा किसी अन्य भूमिका या साइट-विशिष्ट समूह के पास इनमें से कोई अनुमति है, तो यह एक निष्कर्ष है।"
$roles = Get-VIRole
ForEach ($role in $roles) {
    $privileges = $role.PrivilegeList
    If ($privileges -match "Crypto*" -or $privileges -match "Global.Diagnostics" -or $privileges -match "Host.Inventory.Add*" -or $privileges -match "Host.Local operations.Manage user groups") {
        Write-Host "$role के पास क्रिप्टोग्राफ़िक विशेषाधिकार हैं"
    }
}

Write-Host "भेद्यता ID: V-243118 नियम ID: SV-243118r719597_rule STIG ID: VCTR-67-000063"
Write-Host "यदि Solution Users के अलावा किसी उपयोगकर्ता के पास "Administrator" भूमिका है और उसे क्रिप्टोग्राफ़िक कार्यों के लिए स्पष्ट रूप से नामित नहीं किया गया है, तो यह एक निष्कर्ष है।"
Get-VIPermission | Where-Object { $_.Role -eq "Admin" } | Select-Object Role, Principal, Entity, Propagate, IsGroup | Format-Table -Auto


Write-Host "भेद्यता ID: V-243111 नियम ID: SV-243111r719576_rule STIG ID: VCTR-67-000055"
Write-Host "यदि कोई vSAN क्लस्टर सक्षम नहीं है, तो लागू नहीं।"
Write-host "यदि vSAN सक्षम है और डेटास्टोर का नाम 'vsanDatastore' है, तो यह एक निष्कर्ष है।"
If ($(Get-Cluster | Where-Object { $_.VsanEnabled } | Measure-Object).Count -gt 0) {
    Write-Host "सक्षम vSAN क्लस्टर मिला"
    $Clusters = Get-Cluster | Where-Object { $_.VsanEnabled } 
    Foreach ($clus in $clusters) {
        $clus | Get-Datastore | Where-Object { $_.type -match "vsan" } | Set-Datastore -Name $(($clus.name) + "_vSAN_Datastore")
    }
}
else {
    Write-Host "vSAN सक्षम नहीं है; यह निष्कर्ष लागू नहीं होता"
}

Write-Host "यदि किसी उपयोगकर्ता या सेवा खाते के पास आवश्यकता से अधिक विशेषाधिकार हैं, तो यह एक निष्कर्ष है।"
Get-VIPermission | Sort-Object Role | Select-Object Role, Principal, Entity, Propagate, IsGroup | Format-Table -Auto

Write-Host "भेद्यता ID: V-243088 नियम ID: SV-243088r719507_rule STIG ID: VCTR-67-000020"
Write-Host "पोर्ट समूह के VLAN टैग जाँचें और पुष्टि करें कि वे आरक्षित VLAN ID पर सेट नहीं हैं।"
Write-Host "कुछ भौतिक स्विच आंतरिक उपयोग के लिए VLAN ID आरक्षित रखते हैं और अक्सर इन मानों पर कॉन्फ़िगर ट्रैफ़िक रोकते हैं। उदाहरण के लिए, Cisco Catalyst आमतौर पर VLAN 1001–1024 और 4094 आरक्षित रखते हैं, जबकि Nexus 3968–4047 और 4094 आरक्षित रखते हैं।"
Get-VDPortgroup | Select-Object Name, VlanConfiguration

Write-Host "भेद्यता ID: V-243087 नियम ID: SV-243087r719504_rule STIG ID: VCTR-67-000019"
Write-Host "यदि पोर्ट समूह 'VLAN Trunk' पर कॉन्फ़िगर है और आवश्यक अपवाद (जैसे NSX उपकरण) दस्तावेज़ीकृत नहीं है, तो यह एक निष्कर्ष है।
यदि VLAN ट्रंकिंग की अनुमति है, लेकिन उसे आवश्यक न्यूनतम सीमा तक सीमित नहीं किया गया है, तो यह एक निष्कर्ष है।"
Get-VDPortgroup | Where-Object { $_.ExtensionData.Config.Uplink -ne "True" } | Select-Object Name, VlanConfiguration

Write-Host "भेद्यता ID: V-243078 नियम ID: SV-243078r719644_rule STIG ID: VCTR-67-000008"
Write-Host "vCenter Server को सभी ऑडिट विफलता घटनाओं के बारे में SA और ISSO को कम-से-कम तुरंत रीयल-टाइम अलर्ट देना होगा।"
Write-Host "यदि syslog विफलताओं की सूचना देने के लिए अलर्ट नहीं बनाया और सक्षम किया गया है, तो यह एक निष्कर्ष है।"
Get-AlarmDefinition | Where-Object { $_.ExtensionData.Info.Expression.Expression.EventTypeId -eq "esx.problem.vmsyslogd.remote.failure" } | Select-Object Name, Enabled, @{N = "EventTypeId"; E = { $_.ExtensionData.Info.Expression.Expression.EventTypeId } }
```

स्क्रिप्ट ये काम करती है:

- **शुरू में PowerCLI कॉन्फ़िगर करती है, प्रमाणपत्र सत्यापन बंद करती है और Customer Experience Improvement Program (CEIP) में भागीदारी रोकती है।**
- **फिर `$vcenters` वेरिएबल में दिए vCenter सर्वर से जुड़ती है।**
- **PowerCLI cmdlet से प्रत्येक STIG नियंत्रण लागू करती है। उदाहरण के लिए, निर्दिष्ट vCenter सर्वर पर `config.log.level` को info करती है।**
- **`config.vpxd.hostPasswordLength` और `VirtualCenter.VimPasswordExpirationInDays` जैसे नियंत्रण भी लागू करती है।**
- **अंत में सुरक्षा नीतियों और अन्य सेटिंग की जाँच तथा कॉन्फ़िगरेशन करती है।**
- **यह उदाहरण स्क्रिप्ट है। इसे अपने वातावरण और STIG आवश्यकताओं के अनुसार बदलें।**

______

## VMware VM STIG स्वचालित करें

ESXi होस्ट सुरक्षित करने के साथ VMware अवसंरचना में चल रही वर्चुअल मशीनों पर भी STIG नियंत्रण लागू करें। PowerCLI, STIG दिशानिर्देशों के अनुसार VM कॉन्फ़िगरेशन को स्वचालित करने में मदद करती है।

## स्क्रिप्ट: VMware VM STIG स्वचालन

यह PowerCLI स्क्रिप्ट वर्चुअल मशीनों पर चुने गए STIG नियंत्रणों को स्वचालित रूप से लागू करने का तरीका दिखाती है:

```powershell
Set-PowerCLIConfiguration -InvalidCertificateAction Ignore -Confirm:$false
Set-PowerCLIConfiguration -Scope User -ParticipateInCEIP $false -Confirm:$false
Connect-VIServer -Server 127.0.0.1
$cluster = Get-Cluster -Name "Cluster"
$folder = Get-Folder -Name "Folder"

#श्रेय: https://github.com/rlakey/vmware-stig-powercli/blob/master/VMware_vSphere_6.7_VM_STIG_Remediation.ps1
$vmconfig = @{
    #हार्डनिंग/STIG सेटिंग्स
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
    Write-Output "...$vcenter पर $vm की उन्नत सेटिंग ठीक की जा रही हैं"
    ForEach ($setting in ($vmconfig.vmAdvSettings.GetEnumerator() | Sort-Object Name)) {
        #हर निर्दिष्ट सेटिंग का मान प्राप्त करें
        $settingname = $setting.name
        $settingvalue = $setting.value
        If ($asetting = $vm | Get-AdvancedSetting -Name $settingname) {
            If ($asetting.value -eq $settingvalue) {
                Write-Output "...$vm पर $settingname पहले से सही रूप से $settingvalue पर सेट है"
            }
            else {
                Write-Output "...$vm पर $settingname गलत रूप से $($asetting.value) पर सेट था; इसे $settingvalue पर सेट किया जा रहा है"
                $asetting | Set-AdvancedSetting -Value $settingvalue -Confirm:$false
            }
        }
        else {
            Write-Output "...$vm पर $settingname मौजूद नहीं है; सेटिंग बनाई जा रही है..."
            $vm | New-AdvancedSetting -Name $settingname -Value $settingvalue -Confirm:$false
        }
        Write-Output "...आवश्यकता होने पर $vcenter पर $vm की उन्नत सेटिंग हटाई जा रही हैं"
        ForEach ($setting in ($vmconfig.vmAdvSettingsRemove | Sort-Object Name)) {
            #जाँचें कि मौजूदा सेटिंग मौजूद है या नहीं
            If ($asetting = $vm | Get-AdvancedSetting -Name $setting) {
                Write-Output "...$vm पर $setting मौजूद है...सेटिंग हटाई जा रही है"
                $asetting | Remove-AdvancedSetting -Confirm:$false
            }
            else {
                Write-Output "...$vm पर $setting मौजूद नहीं है"
            }
        }   
        If ($vm.extensiondata.Config.MigrateEncryption -eq $vmconfig.vmotionEncryption) {
            Write-Output "...$vm पर vMotion एन्क्रिप्शन सही रूप से $($vmconfig.vmotionEncryption) पर सेट है"
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

स्क्रिप्ट ये काम करती है:

- **VMware VCSA STIG स्क्रिप्ट की तरह यह शुरुआत में PowerCLI वातावरण कॉन्फ़िगर करती है।**
- **vCenter से जुड़कर लक्ष्य VM वाले क्लस्टर और फ़ोल्डर चुनती है।**
- **`$vmconfig` वेरिएबल में VM STIG सेटिंग होती हैं। इनमें कॉपी-पेस्ट बंद करने और रिमोट डिस्प्ले कनेक्शन सीमित करने जैसी उन्नत सेटिंग शामिल हैं।**
- **चुने गए क्लस्टर और फ़ोल्डर की हर VM पर STIG सेटिंग लागू करती है।**
- **VM के vMotion एन्क्रिप्शन को भी कॉन्फ़िगर करती है।**

यह उदाहरण स्क्रिप्ट है। इसे अपने वातावरण और लागू STIG आवश्यकताओं के अनुसार बदलें।

_____

## अतिरिक्त संसाधन

- **DoD STIG VIB पहले संस्करण 5.0 से 6.7 के लिए [उपलब्ध था](https://flings.vmware.com/dod-security-technical-implementation-guide-stig-esxi-vib), लेकिन अब उपलब्ध नहीं है।**
- [Ryan Lakey](https://core.vmware.com/users/ryan-lakey) VMware पर DoD STIG लागू करने के लिए उपयोगी मार्गदर्शन देते हैं। हम उन्हें पढ़ने की सलाह देते हैं।
    - [VMware vSphere 8 STIG](https://core.vmware.com/resource/vmware-vsphere-8-stig)
    - [VMware vSphere 7 STIG](https://core.vmware.com/vsphere-7-stig)
    - [VMware vSphere 6.7 STIG](https://core.vmware.com/vmware-vsphere-67-stig)
    - [VMware STIG PowerCLI](https://github.com/rlakey/vmware-stig-powercli)
        - [VMware VCSA 6.7 STIG आधाररेखा](https://github.com/rlakey/vmware-vcsa-6.7-stig-baseline)
        - [VMware VM 6.7 STIG आधाररेखा](https://github.com/rlakey/vmware-vm-6.7-stig-baseline)
_____

## निष्कर्ष

**VMware STIG लागू करने से VMware अवसंरचना सुरक्षित होती है और संबंधित नियमों के अनुपालन में मदद मिलती है। PowerCLI ESXi होस्ट तथा वर्चुअल मशीनों पर STIG नियंत्रण लागू करने की प्रक्रिया स्वचालित और सरल बनाती है।**

इस लेख में PowerCLI से VMware ESXi और VM STIG स्वचालित करने का तरीका बताया गया। इसमें इंस्टॉलेशन आवश्यकताएँ, उदाहरण स्क्रिप्ट और हर वातावरण की जरूरत के अनुसार स्क्रिप्ट बदलने का महत्व शामिल था।

**PowerCLI और STIG दिशानिर्देशों के साथ प्रशासक VMware परिनियोजन को प्रभावी ढंग से सुरक्षित कर सकते हैं, हाथ से किए जाने वाले काम को घटा सकते हैं और एक जैसी कॉन्फ़िगरेशन बनाए रख सकते हैं।**

## संदर्भ

- [DoD STIG VIB](https://flings.vmware.com/dod-security-technical-implementation-guide-stig-esxi-vib)
- [PowerCLI 11.3](https://www.powershellgallery.com/packages/VMware.PowerCLI/11.3.0.13990089)
- [PowerShell 5 या नया](https://docs.microsoft.com/en-us/skypeforbusiness/set-up-your-computer-for-windows-powershell/download-and-install-windows-powershell-5-1)
- [ESXi 6.7 U2 या नया](https://my.vmware.com/web/vmware/downloads/details?downloadGroup=ESXI670&productId=742)
