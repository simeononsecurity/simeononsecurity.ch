---
title: "إتقان أمان VMware"
date: 2023-08-03
lastmod: 2026-11-13
toc: true
draft: false
description: "تعرّف إلى استخدام PowerCLI لتطبيق معايير VMware STIG وتأمين بيئة VMware في هذا الدليل الشامل."
genre: ["الأمن السيبراني", "الافتراضية", "البنية التحتية لتقنية المعلومات", "الأتمتة", "PowerShell", "VMware", "STIG", "الامتثال", "البرمجة النصية", "مركز البيانات"]
tags: ["PowerCLI", "معايير VMware STIG", "أمان VMware", "الأتمتة", "البرمجة النصية", "PowerShell", "ESXi", "الافتراضية", "الامتثال", "الأمن السيبراني", "كيفية استخدام PowerCLI لمعايير VMware STIG", "أتمتة أمان VMware باستخدام PowerCLI", "برنامج PowerCLI لتطبيق VMware STIG", "أتمتة PowerCLI لتأمين ESXi", "تأمين بيئة VMware باستخدام PowerCLI"]
cover: "/img/cover/An_illustration_depicting_a_computer_server_sh.webp"
coverAlt: "رسم توضيحي لخادم حاسوب يحميه قفل، ويرمز إلى بنية VMware آمنة."
coverCaption: "استخدام PowerCLI لتأمين بيئة VMware"
---

**كيفية تطبيق VMware STIG باستخدام PowerCLI**

PowerCLI أداة للأتمتة والبرمجة النصية تتيح إدارة بيئات VMware وتهيئتها باستخدام PowerShell. يشرح هذا المقال استخدام PowerCLI لتطبيق دليل VMware STIG (Security Technical Implementation Guide) على ESXi والأجهزة الافتراضية.

## المقدمة

يوفر **VMware STIG** إرشادات وتوصيات لتهيئة بنية VMware وإدارتها بأمان. ويساعد اتباعه المؤسسات على تعزيز أمان عمليات نشر VMware والامتثال للمتطلبات الحكومية ذات الصلة، مثل **STIG الصادر عن Defense Information Systems Agency (DISA)**.

## ما PowerCLI؟

**PowerCLI** واجهة سطر أوامر وأداة برمجة نصية لإدارة بيئات VMware. وهي مبنية على PowerShell وتضم مجموعة كبيرة من أوامر cmdlet المخصصة لإدارة VMware. تتيح للمسؤولين أتمتة المهام المتكررة وتعديل الإعدادات وجمع المعلومات من بنية VMware.

### التثبيت والمتطلبات

قبل البدء باستخدام PowerCLI وVMware STIG، تأكد من استيفاء المتطلبات التالية:

- [**PowerCLI 11.3**](https://www.powershellgallery.com/packages/VMware.PowerCLI/11.3.0.13990089): ثبّت PowerCLI من PowerShell Gallery باستخدام الأمر `Install-Module VMware.PowerCLI -force`.
- [**PowerShell 5 أو أحدث**](https://docs.microsoft.com/en-us/skypeforbusiness/set-up-your-computer-for-windows-powershell/download-and-install-windows-powershell-5-1): تأكد من تثبيت PowerShell بالإصدار 5 أو أحدث.
- [**ESXi 6.7 U2 أو أحدث**](https://my.vmware.com/web/vmware/downloads/details?downloadGroup=ESXI670&productId=742): استخدم ESXi 6.7 U2 أو إصدارًا أحدث.

## أتمتة VMware VCSA STIG

يقدم VMware ESXi STIG إرشادات لتأمين مضيفات ESXi. وتساعد أتمتة تطبيق ضوابط STIG المسؤولين على تبسيط العملية وتوحيد الإعدادات عبر عدة مضيفات.

### اعتبارات

قبل بدء الأتمتة، راعِ النقاط التالية:

- **تأكد من أن أي جهاز افتراضي أو نظام ضيف على مضيف ESXi أو عنقود ESXi لا يحتاج إلى وظائف الأقراص المضغوطة أو USB أو الأقراص المرنة.**
- **طبّق STIG على جميع مضيفات ESXi والأنظمة الضيفة المرتبطة بـ vCenter.**
- **تحتاج إلى مهارات استكشاف الأخطاء وإصلاحها لمعالجة المشكلات التي قد تظهر أثناء العملية.**

### نص برمجي: أتمتة VMware VCSA STIG

يمكن استخدام نص PowerCLI التالي لأتمتة تطبيق مجموعة مختارة من ضوابط STIG على VCSA:

```powershell
Set-PowerCLIConfiguration -InvalidCertificateAction Ignore -Confirm:$false
Set-PowerCLIConfiguration -Scope User -ParticipateInCEIP $false -Confirm:$false
$vcenters = 127.0.0.1, 127.0.0.2

#اتصل بكل خادم vCenter
ForEach ($vc in $vcenters) {
    Connect-VIServer -Server $vc
}

#مؤتمت

Write-Host "معرّف الثغرة: V-243098 معرّف القاعدة: SV-243098r719537_rule معرّف STIG: VCTR-67-000036"
Write-Host "إذا لم تُضبط قيمة 'config.log.level' على "info" أو لم تكن موجودة، فهذه ملاحظة."
ForEach ($vc in $vcenters) {
    Get-AdvancedSetting -Entity $vc -Name config.log.level | Set-AdvancedSetting -Value info
    Get-AdvancedSetting -Entity $vc -Name config.log.level
}

Write-Host "معرّف الثغرة: V-243090 معرّف القاعدة: SV-243090r719513_rule معرّف STIG: VCTR-67-000024"
Write-Host "إذا كانت قيمة 'config.vpxd.hostPasswordLength' غير "32"، فهذه ملاحظة.
إذا لم يكن الإعداد موجودًا، فلا توجد ملاحظة."
ForEach ($vc in $vcenters) {
    Get-AdvancedSetting -Entity $vc -Name config.vpxd.hostPasswordLength | Set-AdvancedSetting -Value 32
    Get-AdvancedSetting -Entity $vc -Name config.vpxd.hostPasswordLength
}


Write-Host "معرّف الثغرة: V-243089 معرّف القاعدة: SV-243089r719510_rule معرّف STIG: VCTR-67-000023"
Write-Host "إذا كانت قيمة 'VirtualCenter.VimPasswordExpirationInDays' غير "30" أو لم تكن موجودة، فهذه ملاحظة."
ForEach ($vc in $vcenters) {
    Try {
        Get-AdvancedSetting -Entity $vc -Name VirtualCenter.VimPasswordExpirationInDays | Set-AdvancedSetting -Value 30
    }
    Catch {
        New-AdvancedSetting -Entity $vc -Name VirtualCenter.VimPasswordExpirationInDays -Value 30
    }
}

Write-Host "معرّف الثغرة: V-243084 معرّف القاعدة: SV-243085r719498_rule معرّف STIG: VCTR-67-000016"
Write-Host "إذا كان NetFlow مُعدًّا وعنوان IP للمجمّع غير معروف وغير موثّق، فهذه ملاحظة."
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

Write-Host "معرّف الثغرة: V-243084 معرّف القاعدة: SV-243084r719495_rule معرّف STIG: VCTR-67-000015"
Write-Host "يجب على خادم vCenter ضبط سياسة Promiscuous Mode لمجموعة المنافذ الموزعة على الرفض."
Get-VDSwitch | Get-VDSecurityPolicy | Set-VDSecurityPolicy -AllowPromiscuous $false
Get-VDPortgroup | Where-Object { $_.IsUplink -eq $false } | Get-VDSecurityPolicy | Set-VDSecurityPolicy -AllowPromiscuous $false
Get-VDSwitch | Get-VDSecurityPolicy
Get-VDPortgroup | Where-Object { $_.IsUplink -eq $false } | Get-VDSecurityPolicy


Write-Host "معرّف الثغرة: V-243083 معرّف القاعدة: SV-243083r719492_rule معرّف STIG: VCTR-67-000014"
Write-Host "يجب على خادم vCenter ضبط سياسة MAC Address Change لمجموعة المنافذ الموزعة على الرفض."
Get-VDSwitch | Get-VDSecurityPolicy | Set-VDSecurityPolicy -MacChanges $false
Get-VDPortgroup | Where-Object { $_.IsUplink -eq $false } | Get-VDSecurityPolicy | Set-VDSecurityPolicy -MacChanges $false
Get-VDPortgroup | Where-Object { $_.IsUplink -eq $false } | Get-VDSecurityPolicy

Write-Host "معرّف الثغرة: V-243082 معرّف القاعدة: SV-243082r719489_rule معرّف STIG: VCTR-67-000013"
Write-Host "يجب على خادم vCenter ضبط سياسة Forged Transmits لمجموعة المنافذ الموزعة على الرفض."
Get-VDSwitch | Get-VDSecurityPolicy | Set-VDSecurityPolicy -ForgedTransmits $false
Get-VDPortgroup | Where-Object { $_.IsUplink -eq $false } | Get-VDSecurityPolicy | Set-VDSecurityPolicy -ForgedTransmits $false
Get-VDSwitch | Get-VDSecurityPolicy
Get-VDPortgroup | Where-Object { $_.IsUplink -eq $false } | Get-VDSecurityPolicy

Write-Host "معرّف الثغرة: V-243081 معرّف القاعدة: SV-243081r719486_rule معرّف STIG: VCTR-67-000012"
Write-Host "يجب على خادم vCenter تعطيل فحص سلامة المحوّل الافتراضي الموزع."
Get-View -ViewType DistributedVirtualSwitch | Where-Object { ($_.config.HealthCheckConfig | Where-Object { $_.enable -notmatch "False" }) } | ForEach-Object { $_.UpdateDVSHealthCheckConfig(@((New-Object Vmware.Vim.VMwareDVSVlanMtuHealthCheckConfig -property @{enable = 0 }), (New-Object Vmware.Vim.VMwareDVSTeamingHealthCheckConfig -property @{enable = 0 }))) }
$vds = Get-VDSwitch
$vds.ExtensionData.Config.HealthCheckConfig

Write-Host "معرّف الثغرة: V-243077 معرّف القاعدة: SV-243077r719474_rule معرّف STIG: VCTR-67-00000"
Write-Host "يجب على خادم vCenter إدارة السعة الزائدة أو عرض النطاق أو أي تكرار آخر للحد من آثار هجمات حجب الخدمة (DoS) القائمة على إغراق المعلومات، وذلك بتمكين Network I/O Control (NIOC)."
Write-Host "إذا لم يُنشأ تنبيه ويُفعّل للإبلاغ عن أعطال syslog، فهذه ملاحظة."
ForEach ($vdswitch in (Get-VDSwitch.name)){
    (Get-VDSwitch $vdswitch | Get-View).EnableNetworkResourceManagement($true)
}
Get-VDSwitch | Select-Object Name, @{N = "NIOC Enabled"; E = { $_.ExtensionData.config.NetworkResourceManagementEnabled } }

#مراجعة يدوية

Write-Host "معرّف الثغرة: V-243076 معرّف القاعدة: SV-243076r719471_rule معرّف STIG: VCTR-67-000005"
Write-Host "يجب تعيين الأدوار الصحيحة لمستخدمي خادم vCenter."
Write-Host "يجب توثيق الامتيازات المطلوبة لحسابات الخدمة والمستخدمين.
إذا امتلك مستخدم أو حساب خدمة امتيازات أكثر من اللازم، فهذه ملاحظة."
Get-VIPermission | Sort-Object Role | Select-Object Role, Principal, Entity, Propagate, IsGroup | Format-Table -Auto

Write-Host "معرّف الثغرة: V-243119 معرّف القاعدة: SV-243119r719600_rule معرّف STIG: VCTR-67-000064"
Write-Host "إذا امتلك أي دور غير Administrator أو أي مجموعة خاصة بالموقع أيًا من هذه الأذونات، فهذه ملاحظة."
$roles = Get-VIRole
ForEach ($role in $roles) {
    $privileges = $role.PrivilegeList
    If ($privileges -match "Crypto*" -or $privileges -match "Global.Diagnostics" -or $privileges -match "Host.Inventory.Add*" -or $privileges -match "Host.Local operations.Manage user groups") {
        Write-Host "لدى $role امتيازات تشفيرية"
    }
}

Write-Host "معرّف الثغرة: V-243118 معرّف القاعدة: SV-243118r719597_rule معرّف STIG: VCTR-67-000063"
Write-Host "إذا امتلك مستخدمون غير Solution Users دور "Administrator" من دون تعيينهم صراحةً للعمليات التشفيرية، فهذه ملاحظة."
Get-VIPermission | Where-Object { $_.Role -eq "Admin" } | Select-Object Role, Principal, Entity, Propagate, IsGroup | Format-Table -Auto


Write-Host "معرّف الثغرة: V-243111 معرّف القاعدة: SV-243111r719576_rule معرّف STIG: VCTR-67-000055"
Write-Host "لا ينطبق ذلك إذا لم تُفعّل أي عناقيد vSAN."
Write-host "إذا كان vSAN مفعّلًا وكان اسم مخزن البيانات 'vsanDatastore'، فهذه ملاحظة."
If ($(Get-Cluster | Where-Object { $_.VsanEnabled } | Measure-Object).Count -gt 0) {
    Write-Host "تم العثور على عنقود vSAN مفعّل"
    $Clusters = Get-Cluster | Where-Object { $_.VsanEnabled } 
    Foreach ($clus in $clusters) {
        $clus | Get-Datastore | Where-Object { $_.type -match "vsan" } | Set-Datastore -Name $(($clus.name) + "_vSAN_Datastore")
    }
}
else {
    Write-Host "vSAN غير مفعّل؛ لا تنطبق هذه الملاحظة"
}

Write-Host "إذا امتلك مستخدم أو حساب خدمة امتيازات أكثر من اللازم، فهذه ملاحظة."
Get-VIPermission | Sort-Object Role | Select-Object Role, Principal, Entity, Propagate, IsGroup | Format-Table -Auto

Write-Host "معرّف الثغرة: V-243088 معرّف القاعدة: SV-243088r719507_rule معرّف STIG: VCTR-67-000020"
Write-Host "راجع وسوم VLAN لمجموعة المنافذ وتحقق من عدم استخدام معرّف VLAN محجوز."
Write-Host "تحجز بعض المحوّلات المادية معرّفات VLAN للاستخدام الداخلي، وغالبًا تمنع حركة المرور المضبوطة على هذه القيم. مثلًا، تحجز محوّلات Cisco Catalyst عادةً VLAN 1001–1024 و4094، بينما تحجز Nexus عادةً 3968–4047 و4094."
Get-VDPortgroup | Select-Object Name, VlanConfiguration

Write-Host "معرّف الثغرة: V-243087 معرّف القاعدة: SV-243087r719504_rule معرّف STIG: VCTR-67-000019"
Write-Host "إذا ضُبطت مجموعة منافذ على 'VLAN Trunk' من دون توثيق استثناء مطلوب (مثل أجهزة NSX)، فهذه ملاحظة.
إذا سُمح بتمرير VLAN لكن لم يُحصر في أقل نطاق مطلوب، فهذه ملاحظة."
Get-VDPortgroup | Where-Object { $_.ExtensionData.Config.Uplink -ne "True" } | Select-Object Name, VlanConfiguration

Write-Host "معرّف الثغرة: V-243078 معرّف القاعدة: SV-243078r719644_rule معرّف STIG: VCTR-67-000008"
Write-Host "يجب على خادم vCenter إرسال تنبيه فوري وآني إلى SA وISSO، كحد أدنى، بشأن جميع أحداث فشل التدقيق."
Write-Host "إذا لم يُنشأ تنبيه ويُفعّل للإبلاغ عن أعطال syslog، فهذه ملاحظة."
Get-AlarmDefinition | Where-Object { $_.ExtensionData.Info.Expression.Expression.EventTypeId -eq "esx.problem.vmsyslogd.remote.failure" } | Select-Object Name, Enabled, @{N = "EventTypeId"; E = { $_.ExtensionData.Info.Expression.Expression.EventTypeId } }
```

يوضح النص البرمجي الوظائف التالية:

- **يضبط PowerCLI أولًا، ويعطّل التحقق من الشهادات، ويلغي المشاركة في برنامج تحسين تجربة العملاء (CEIP).**
- **ثم يتصل بخوادم vCenter المحددة في المتغير `$vcenters`.**
- **يعالج كل ضابط STIG باستخدام أوامر PowerCLI. مثلًا، يضبط `config.log.level` على info لخوادم vCenter المحددة.**
- **يعالج أيضًا ضوابط مثل `config.vpxd.hostPasswordLength` و`VirtualCenter.VimPasswordExpirationInDays`.**
- **وأخيرًا يفحص سياسات الأمان والإعدادات الأخرى ويهيئها.**
- **هذا النص مثال. عدّله ليتوافق مع متطلبات STIG وبيئتك.**

______

## أتمتة VMware VM STIG

إلى جانب تأمين مضيفات ESXi، يجب تطبيق ضوابط STIG على الأجهزة الافتراضية في بنية VMware. تساعد PowerCLI على أتمتة تهيئة الأجهزة وفق إرشادات STIG.

## نص برمجي: أتمتة VMware VM STIG

يوضح نص PowerCLI التالي كيفية أتمتة تطبيق مجموعة مختارة من ضوابط STIG على الأجهزة الافتراضية:

```powershell
Set-PowerCLIConfiguration -InvalidCertificateAction Ignore -Confirm:$false
Set-PowerCLIConfiguration -Scope User -ParticipateInCEIP $false -Confirm:$false
Connect-VIServer -Server 127.0.0.1
$cluster = Get-Cluster -Name "Cluster"
$folder = Get-Folder -Name "Folder"

#المصدر: https://github.com/rlakey/vmware-stig-powercli/blob/master/VMware_vSphere_6.7_VM_STIG_Remediation.ps1
$vmconfig = @{
    #إعدادات التقوية وSTIG
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
    Write-Output "...تتم معالجة الإعدادات المتقدمة على $vm في $vcenter"
    ForEach ($setting in ($vmconfig.vmAdvSettings.GetEnumerator() | Sort-Object Name)) {
        #سحب القيم المحددة لكل إعداد
        $settingname = $setting.name
        $settingvalue = $setting.value
        If ($asetting = $vm | Get-AdvancedSetting -Name $settingname) {
            If ($asetting.value -eq $settingvalue) {
                Write-Output "...الإعداد $settingname على $vm مضبوط بالفعل بشكل صحيح على $settingvalue"
            }
            else {
                Write-Output "...كان الإعداد $settingname على $vm مضبوطًا خطأً على $($asetting.value)، ويُضبط الآن على $settingvalue"
                $asetting | Set-AdvancedSetting -Value $settingvalue -Confirm:$false
            }
        }
        else {
            Write-Output "...الإعداد $settingname غير موجود على $vm؛ جارٍ إنشاؤه..."
            $vm | New-AdvancedSetting -Name $settingname -Value $settingvalue -Confirm:$false
        }
        Write-Output "...تتم إزالة الإعدادات المتقدمة على $vm في $vcenter عند الحاجة"
        ForEach ($setting in ($vmconfig.vmAdvSettingsRemove | Sort-Object Name)) {
            #التحقق من وجود الإعداد الحالي
            If ($asetting = $vm | Get-AdvancedSetting -Name $setting) {
                Write-Output "...الإعداد $setting موجود على $vm...تتم إزالته"
                $asetting | Remove-AdvancedSetting -Confirm:$false
            }
            else {
                Write-Output "...الإعداد $setting غير موجود على $vm"
            }
        }   
        If ($vm.extensiondata.Config.MigrateEncryption -eq $vmconfig.vmotionEncryption) {
            Write-Output "...تشفير vMotion مضبوط بشكل صحيح على $vm إلى $($vmconfig.vmotionEncryption)"
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

يوضح النص البرمجي الوظائف التالية:

- **يضبط بيئة PowerCLI في البداية، على غرار نص VMware VCSA STIG.**
- **يتصل بـ vCenter، ثم يحدد العنقود والمجلد اللذين يحتويان على الأجهزة الافتراضية المستهدفة.**
- **يحتوي المتغير `$vmconfig` على إعدادات STIG للأجهزة الافتراضية، ومنها إعدادات متقدمة مثل تعطيل النسخ واللصق وتقييد اتصالات العرض عن بُعد.**
- **يمر على كل جهاز افتراضي في العنقود والمجلد المحددين ويطبق إعدادات STIG.**
- **كما يتعامل مع تشفير vMotion للأجهزة الافتراضية.**

هذا النص البرمجي مثال. عدّله وفق بيئتك ومتطلبات STIG المعمول بها.

_____

## موارد إضافية

- **كان VIB الخاص بـ DoD STIG [متاحًا سابقًا للإصدارات من 5.0 إلى 6.7](https://flings.vmware.com/dod-security-technical-implementation-guide-stig-esxi-vib)، لكنه لم يعد متاحًا.**
- يقدم [Ryan Lakey](https://core.vmware.com/users/ryan-lakey) إرشادات مفيدة لتطبيق DoD VMware STIGs. نوصي بمراجعتها.
    - [VMware vSphere 8 STIG](https://core.vmware.com/resource/vmware-vsphere-8-stig)
    - [VMware vSphere 7 STIG](https://core.vmware.com/vsphere-7-stig)
    - [VMware vSphere 6.7 STIG](https://core.vmware.com/vmware-vsphere-67-stig)
    - [VMware STIG PowerCLI](https://github.com/rlakey/vmware-stig-powercli)
        - [خط أساس VMware VCSA 6.7 STIG](https://github.com/rlakey/vmware-vcsa-6.7-stig-baseline)
        - [خط أساس VMware VM 6.7 STIG](https://github.com/rlakey/vmware-vm-6.7-stig-baseline)
_____

## الخلاصة

**يساعد تطبيق VMware STIG على تعزيز أمان بنية VMware والامتثال للمتطلبات ذات الصلة. وتؤتمت PowerCLI تطبيق ضوابط STIG على مضيفات ESXi والأجهزة الافتراضية وتبسّطه.**

شرح هذا المقال كيفية استخدام PowerCLI لأتمتة VMware ESXi STIG وVM STIG. وتناول متطلبات التثبيت، وعرض نصوصًا برمجية نموذجية، وأكد أهمية تخصيص النصوص لتناسب احتياجات كل بيئة.

**باستخدام PowerCLI واتباع إرشادات STIG، يستطيع المسؤولون تأمين عمليات نشر VMware بكفاءة، وتقليل العمل اليدوي، والحفاظ على إعدادات متسقة.**

## المراجع

- [DoD STIG VIB](https://flings.vmware.com/dod-security-technical-implementation-guide-stig-esxi-vib)
- [PowerCLI 11.3](https://www.powershellgallery.com/packages/VMware.PowerCLI/11.3.0.13990089)
- [PowerShell 5 أو أحدث](https://docs.microsoft.com/en-us/skypeforbusiness/set-up-your-computer-for-windows-powershell/download-and-install-windows-powershell-5-1)
- [ESXi 6.7 U2 أو أحدث](https://my.vmware.com/web/vmware/downloads/details?downloadGroup=ESXI670&productId=742)
