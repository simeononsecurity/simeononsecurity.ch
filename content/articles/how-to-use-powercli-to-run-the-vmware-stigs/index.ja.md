---
title: "VMwareセキュリティを極める"
date: 2023-08-03
lastmod: 2026-11-13
toc: true
draft: false
description: "この包括的なガイドでは、PowerCLIでVMware STIGを適用し、VMware環境を保護する方法を説明します。"
genre: ["サイバーセキュリティ", "仮想化", "ITインフラストラクチャ", "自動化", "PowerShell", "VMware", "STIG", "コンプライアンス", "スクリプト", "データセンター"]
tags: ["PowerCLI", "VMware STIG", "VMwareセキュリティ", "自動化", "スクリプト", "PowerShell", "ESXi", "仮想化", "コンプライアンス", "サイバーセキュリティ", "VMware STIGにPowerCLIを使う方法", "PowerCLIでVMwareセキュリティを自動化", "VMware STIG適用用PowerCLIスクリプト", "ESXiセキュリティのPowerCLI自動化", "PowerCLIでVMware環境を保護"]
cover: "/img/cover/An_illustration_depicting_a_computer_server_sh.webp"
coverAlt: "南京錠で守られたコンピューターサーバーのイラスト。安全なVMwareインフラストラクチャを表しています。"
coverCaption: "PowerCLIでVMware環境を保護する"
---

**PowerCLIでVMware STIGを適用する方法**

PowerCLIは、PowerShellを使ってVMware環境を管理、設定するための自動化およびスクリプトツールです。この記事では、PowerCLIでVMware STIG（Security Technical Implementation Guide）をESXiと仮想マシンに適用する方法を説明します。

## はじめに

**VMware STIG**は、VMwareインフラストラクチャを安全に構成、管理するための指針と推奨事項を示します。これに従うことで、組織はVMware環境のセキュリティを高め、**Defense Information Systems Agency（DISA）STIG**など、該当する政府要件への準拠を支援できます。

## PowerCLIとは

**PowerCLI**は、VMware環境を管理するためのコマンドラインインターフェイス兼スクリプトツールです。PowerShellを基盤とし、VMware管理専用の多数のコマンドレットを備えています。管理者は、定型作業の自動化、構成変更、VMwareインフラストラクチャからの情報収集に利用できます。

### インストールと要件

PowerCLIとVMware STIGを使い始める前に、次の要件を確認してください。

- [**PowerCLI 11.3**](https://www.powershellgallery.com/packages/VMware.PowerCLI/11.3.0.13990089): PowerShell Galleryから`Install-Module VMware.PowerCLI -force`を実行してインストールします。
- [**PowerShell 5以降**](https://docs.microsoft.com/en-us/skypeforbusiness/set-up-your-computer-for-windows-powershell/download-and-install-windows-powershell-5-1): PowerShell 5以降がインストールされていることを確認します。
- [**ESXi 6.7 U2以降**](https://my.vmware.com/web/vmware/downloads/details?downloadGroup=ESXI670&productId=742): ESXi 6.7 U2以降を使用します。

## VMware VCSA STIGの自動化

VMware ESXi STIGは、ESXiホストを保護するための指針を示します。STIGコントロールの適用を自動化すれば、作業を簡略化し、複数のホストに一貫した構成を適用できます。

### 注意事項

自動化を始める前に、次の点を確認してください。

- **ESXiホストまたはクラスター上の仮想マシンやゲストが、CD、USB、フロッピーディスク機能を必要としていないことを確認します。**
- **vCenterに接続されたすべてのESXiホストとゲストにSTIGを適用します。**
- **処理中に問題が起きた場合に備え、トラブルシューティングの知識を用意します。**

### スクリプト: VMware VCSA STIGの自動化

次のPowerCLIスクリプトは、VCSA向けに選択したSTIGコントロールを自動的に適用します。

```powershell
Set-PowerCLIConfiguration -InvalidCertificateAction Ignore -Confirm:$false
Set-PowerCLIConfiguration -Scope User -ParticipateInCEIP $false -Confirm:$false
$vcenters = 127.0.0.1, 127.0.0.2

#各 vCenter サーバーに接続
ForEach ($vc in $vcenters) {
    Connect-VIServer -Server $vc
}

#自動処理

Write-Host "脆弱性 ID: V-243098 ルール ID: SV-243098r719537_rule STIG ID: VCTR-67-000036"
Write-Host "'config.log.level' の値が "info" に設定されていない、または存在しない場合は、指摘事項です。"
ForEach ($vc in $vcenters) {
    Get-AdvancedSetting -Entity $vc -Name config.log.level | Set-AdvancedSetting -Value info
    Get-AdvancedSetting -Entity $vc -Name config.log.level
}

Write-Host "脆弱性 ID: V-243090 ルール ID: SV-243090r719513_rule STIG ID: VCTR-67-000024"
Write-Host "'config.vpxd.hostPasswordLength' が "32" 以外に設定されている場合は、指摘事項です。
設定が存在しない場合は、指摘事項ではありません。"
ForEach ($vc in $vcenters) {
    Get-AdvancedSetting -Entity $vc -Name config.vpxd.hostPasswordLength | Set-AdvancedSetting -Value 32
    Get-AdvancedSetting -Entity $vc -Name config.vpxd.hostPasswordLength
}


Write-Host "脆弱性 ID: V-243089 ルール ID: SV-243089r719510_rule STIG ID: VCTR-67-000023"
Write-Host "'VirtualCenter.VimPasswordExpirationInDays' が "30" 以外に設定されている、または存在しない場合は、指摘事項です。"
ForEach ($vc in $vcenters) {
    Try {
        Get-AdvancedSetting -Entity $vc -Name VirtualCenter.VimPasswordExpirationInDays | Set-AdvancedSetting -Value 30
    }
    Catch {
        New-AdvancedSetting -Entity $vc -Name VirtualCenter.VimPasswordExpirationInDays -Value 30
    }
}

Write-Host "脆弱性 ID: V-243084 ルール ID: SV-243085r719498_rule STIG ID: VCTR-67-000016"
Write-Host "NetFlow が設定されているのに、コレクターの IP が不明で文書化されていない場合は、指摘事項です。"
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

Write-Host "脆弱性 ID: V-243084 ルール ID: SV-243084r719495_rule STIG ID: VCTR-67-000015"
Write-Host "vCenter Server は分散ポート グループの Promiscuous Mode ポリシーを拒否に設定する必要があります。"
Get-VDSwitch | Get-VDSecurityPolicy | Set-VDSecurityPolicy -AllowPromiscuous $false
Get-VDPortgroup | Where-Object { $_.IsUplink -eq $false } | Get-VDSecurityPolicy | Set-VDSecurityPolicy -AllowPromiscuous $false
Get-VDSwitch | Get-VDSecurityPolicy
Get-VDPortgroup | Where-Object { $_.IsUplink -eq $false } | Get-VDSecurityPolicy


Write-Host "脆弱性 ID: V-243083 ルール ID: SV-243083r719492_rule STIG ID: VCTR-67-000014"
Write-Host "vCenter Server は分散ポート グループの MAC Address Change ポリシーを拒否に設定する必要があります。"
Get-VDSwitch | Get-VDSecurityPolicy | Set-VDSecurityPolicy -MacChanges $false
Get-VDPortgroup | Where-Object { $_.IsUplink -eq $false } | Get-VDSecurityPolicy | Set-VDSecurityPolicy -MacChanges $false
Get-VDPortgroup | Where-Object { $_.IsUplink -eq $false } | Get-VDSecurityPolicy

Write-Host "脆弱性 ID: V-243082 ルール ID: SV-243082r719489_rule STIG ID: VCTR-67-000013"
Write-Host "vCenter Server は分散ポート グループの Forged Transmits ポリシーを拒否に設定する必要があります。"
Get-VDSwitch | Get-VDSecurityPolicy | Set-VDSecurityPolicy -ForgedTransmits $false
Get-VDPortgroup | Where-Object { $_.IsUplink -eq $false } | Get-VDSecurityPolicy | Set-VDSecurityPolicy -ForgedTransmits $false
Get-VDSwitch | Get-VDSecurityPolicy
Get-VDPortgroup | Where-Object { $_.IsUplink -eq $false } | Get-VDSecurityPolicy

Write-Host "脆弱性 ID: V-243081 ルール ID: SV-243081r719486_rule STIG ID: VCTR-67-000012"
Write-Host "vCenter Server は分散仮想スイッチのヘルスチェックを無効にする必要があります。"
Get-View -ViewType DistributedVirtualSwitch | Where-Object { ($_.config.HealthCheckConfig | Where-Object { $_.enable -notmatch "False" }) } | ForEach-Object { $_.UpdateDVSHealthCheckConfig(@((New-Object Vmware.Vim.VMwareDVSVlanMtuHealthCheckConfig -property @{enable = 0 }), (New-Object Vmware.Vim.VMwareDVSTeamingHealthCheckConfig -property @{enable = 0 }))) }
$vds = Get-VDSwitch
$vds.ExtensionData.Config.HealthCheckConfig

Write-Host "脆弱性 ID: V-243077 ルール ID: SV-243077r719474_rule STIG ID: VCTR-67-00000"
Write-Host "vCenter Server は Network I/O Control (NIOC) を有効にして、過剰な容量や帯域幅、その他の冗長性を管理し、情報の大量送信や DoS 攻撃の影響を抑える必要があります。"
Write-Host "syslog 障害を通知するアラームが作成・有効化されていない場合は、指摘事項です。"
ForEach ($vdswitch in (Get-VDSwitch.name)){
    (Get-VDSwitch $vdswitch | Get-View).EnableNetworkResourceManagement($true)
}
Get-VDSwitch | Select-Object Name, @{N = "NIOC Enabled"; E = { $_.ExtensionData.config.NetworkResourceManagementEnabled } }

#手動レビュー

Write-Host "脆弱性 ID: V-243076 ルール ID: SV-243076r719471_rule STIG ID: VCTR-67-000005"
Write-Host "vCenter Server のユーザーには適切なロールを割り当てる必要があります。"
Write-Host "サービス アカウントとユーザーに必要な権限を文書化する必要があります。
ユーザーまたはサービス アカウントが必要以上の権限を持つ場合は、指摘事項です。"
Get-VIPermission | Sort-Object Role | Select-Object Role, Principal, Entity, Propagate, IsGroup | Format-Table -Auto

Write-Host "脆弱性 ID: V-243119 ルール ID: SV-243119r719600_rule STIG ID: VCTR-67-000064"
Write-Host "Administrator 以外のロール、またはサイト固有のグループがこれらの権限を持つ場合は、指摘事項です。"
$roles = Get-VIRole
ForEach ($role in $roles) {
    $privileges = $role.PrivilegeList
    If ($privileges -match "Crypto*" -or $privileges -match "Global.Diagnostics" -or $privileges -match "Host.Inventory.Add*" -or $privileges -match "Host.Local operations.Manage user groups") {
        Write-Host "$role には暗号化関連の権限があります"
    }
}

Write-Host "脆弱性 ID: V-243118 ルール ID: SV-243118r719597_rule STIG ID: VCTR-67-000063"
Write-Host "Solution Users 以外のユーザーに "Administrator" ロールがあり、暗号化操作の担当者として明示されていない場合は、指摘事項です。"
Get-VIPermission | Where-Object { $_.Role -eq "Admin" } | Select-Object Role, Principal, Entity, Propagate, IsGroup | Format-Table -Auto


Write-Host "脆弱性 ID: V-243111 ルール ID: SV-243111r719576_rule STIG ID: VCTR-67-000055"
Write-Host "vSAN が有効なクラスターがない場合は、対象外です。"
Write-host "vSAN が有効で、データストア名が 'vsanDatastore' の場合は、指摘事項です。"
If ($(Get-Cluster | Where-Object { $_.VsanEnabled } | Measure-Object).Count -gt 0) {
    Write-Host "vSAN が有効なクラスターを検出しました"
    $Clusters = Get-Cluster | Where-Object { $_.VsanEnabled } 
    Foreach ($clus in $clusters) {
        $clus | Get-Datastore | Where-Object { $_.type -match "vsan" } | Set-Datastore -Name $(($clus.name) + "_vSAN_Datastore")
    }
}
else {
    Write-Host "vSAN は有効ではありません。この指摘事項は対象外です"
}

Write-Host "ユーザーまたはサービス アカウントが必要以上の権限を持つ場合は、指摘事項です。"
Get-VIPermission | Sort-Object Role | Select-Object Role, Principal, Entity, Propagate, IsGroup | Format-Table -Auto

Write-Host "脆弱性 ID: V-243088 ルール ID: SV-243088r719507_rule STIG ID: VCTR-67-000020"
Write-Host "ポート グループの VLAN タグを確認し、予約済み VLAN ID が設定されていないことを確認してください。"
Write-Host "一部の物理スイッチは内部用途に VLAN ID を予約し、その値に設定されたトラフィックを許可しない場合があります。Cisco Catalyst は通常 VLAN 1001～1024 と 4094 を、Nexus は通常 3968～4047 と 4094 を予約します。"
Get-VDPortgroup | Select-Object Name, VlanConfiguration

Write-Host "脆弱性 ID: V-243087 ルール ID: SV-243087r719504_rule STIG ID: VCTR-67-000019"
Write-Host "ポート グループが 'VLAN Trunk' に設定され、NSX アプライアンスなどの必要な例外が文書化されていない場合は、指摘事項です。
VLAN トランキングが許可されていても、必要最小限の範囲に制限されていない場合は、指摘事項です。"
Get-VDPortgroup | Where-Object { $_.ExtensionData.Config.Uplink -ne "True" } | Select-Object Name, VlanConfiguration

Write-Host "脆弱性 ID: V-243078 ルール ID: SV-243078r719644_rule STIG ID: VCTR-67-000008"
Write-Host "vCenter Server は、すべての監査失敗イベントを SA と ISSO に少なくともリアルタイムで直ちに通知する必要があります。"
Write-Host "syslog 障害を通知するアラームが作成・有効化されていない場合は、指摘事項です。"
Get-AlarmDefinition | Where-Object { $_.ExtensionData.Info.Expression.Expression.EventTypeId -eq "esx.problem.vmsyslogd.remote.failure" } | Select-Object Name, Enabled, @{N = "EventTypeId"; E = { $_.ExtensionData.Info.Expression.Expression.EventTypeId } }
```

このスクリプトの処理内容は次のとおりです。

- **最初にPowerCLIを設定し、証明書の検証を無効にして、カスタマーエクスペリエンス向上プログラム（CEIP）への参加を無効にします。**
- **次に、変数`$vcenters`で指定されたvCenterサーバーに接続します。**
- **PowerCLIコマンドレットで各STIGコントロールを処理します。たとえば、指定したvCenterサーバーの`config.log.level`をinfoに設定します。**
- **`config.vpxd.hostPasswordLength`や`VirtualCenter.VimPasswordExpirationInDays`に関するコントロールも扱います。**
- **最後に、セキュリティポリシーやその他の設定を確認、構成します。**
- **これはサンプルスクリプトです。環境とSTIG要件に合わせて変更してください。**

______

## VMware VM STIGの自動化

ESXiホストだけでなく、VMwareインフラストラクチャ上の仮想マシンにもSTIGコントロールを適用する必要があります。PowerCLIを使うと、STIGの指針に沿ったVMの構成を自動化できます。

## スクリプト: VMware VM STIGの自動化

次のPowerCLIスクリプトは、仮想マシンに選択したSTIGコントロールを自動適用する例です。

```powershell
Set-PowerCLIConfiguration -InvalidCertificateAction Ignore -Confirm:$false
Set-PowerCLIConfiguration -Scope User -ParticipateInCEIP $false -Confirm:$false
Connect-VIServer -Server 127.0.0.1
$cluster = Get-Cluster -Name "Cluster"
$folder = Get-Folder -Name "Folder"

#出典: https://github.com/rlakey/vmware-stig-powercli/blob/master/VMware_vSphere_6.7_VM_STIG_Remediation.ps1
$vmconfig = @{
    #ハードニング/STIG 設定
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
    Write-Output "...$vm の $vcenter 上で詳細設定を修復中"
    ForEach ($setting in ($vmconfig.vmAdvSettings.GetEnumerator() | Sort-Object Name)) {
        #指定された各設定の値を取得
        $settingname = $setting.name
        $settingvalue = $setting.value
        If ($asetting = $vm | Get-AdvancedSetting -Name $settingname) {
            If ($asetting.value -eq $settingvalue) {
                Write-Output "...$vm の $settingname は $settingvalue に正しく設定済みです"
            }
            else {
                Write-Output "...$vm の $settingname は誤って $($asetting.value) に設定されています。$settingvalue に変更します"
                $asetting | Set-AdvancedSetting -Value $settingvalue -Confirm:$false
            }
        }
        else {
            Write-Output "...$vm に $settingname がありません。作成します..."
            $vm | New-AdvancedSetting -Name $settingname -Value $settingvalue -Confirm:$false
        }
        Write-Output "...必要に応じて $vm の $vcenter 上の詳細設定を削除中"
        ForEach ($setting in ($vmconfig.vmAdvSettingsRemove | Sort-Object Name)) {
            #現在の設定が存在するか確認
            If ($asetting = $vm | Get-AdvancedSetting -Name $setting) {
                Write-Output "...$vm に $setting があります...設定を削除します"
                $asetting | Remove-AdvancedSetting -Confirm:$false
            }
            else {
                Write-Output "...$vm に $setting はありません"
            }
        }   
        If ($vm.extensiondata.Config.MigrateEncryption -eq $vmconfig.vmotionEncryption) {
            Write-Output "...$vm の vMotion 暗号化は $($vmconfig.vmotionEncryption) に正しく設定されています"
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

このスクリプトの処理内容は次のとおりです。

- **VMware VCSA STIGのスクリプトと同様に、最初にPowerCLI環境を設定します。**
- **vCenterに接続し、対象VMがあるクラスターとフォルダーを選択します。**
- **変数`$vmconfig`にVM向けのSTIG設定を格納します。コピーと貼り付けの無効化、リモートディスプレイ接続の制限など、高度な設定も含みます。**
- **選択したクラスターとフォルダー内の各VMにSTIG設定を適用します。**
- **VMのvMotion暗号化も設定します。**

このスクリプトは例です。環境と適用するSTIG要件に合わせて修正してください。

_____

## 追加リソース

- **DoD STIG VIBは、以前はバージョン5.0から6.7向けに[公開されていました](https://flings.vmware.com/dod-security-technical-implementation-guide-stig-esxi-vib)が、現在は入手できません。**
- [Ryan Lakey](https://core.vmware.com/users/ryan-lakey)は、DoD VMware STIGの導入に役立つ情報を提供しています。次の資料を確認してください。
    - [VMware vSphere 8 STIG](https://core.vmware.com/resource/vmware-vsphere-8-stig)
    - [VMware vSphere 7 STIG](https://core.vmware.com/vsphere-7-stig)
    - [VMware vSphere 6.7 STIG](https://core.vmware.com/vmware-vsphere-67-stig)
    - [VMware STIG PowerCLI](https://github.com/rlakey/vmware-stig-powercli)
        - [VMware VCSA 6.7 STIGベースライン](https://github.com/rlakey/vmware-vcsa-6.7-stig-baseline)
        - [VMware VM 6.7 STIGベースライン](https://github.com/rlakey/vmware-vm-6.7-stig-baseline)
_____

## まとめ

**VMware STIGの適用はVMwareインフラストラクチャの保護と、該当する要件への準拠に役立ちます。PowerCLIを使うと、ESXiホストと仮想マシンへのSTIGコントロール適用を自動化し、簡略化できます。**

この記事では、PowerCLIでVMware ESXiおよびVM STIGを自動化する方法を取り上げました。インストール要件とサンプルスクリプトを示し、環境に合わせてスクリプトを調整する重要性を説明しました。

**PowerCLIとSTIGの指針を使うことで、管理者はVMware環境を効率よく保護し、手作業を減らし、一貫した構成を維持できます。**

## 参考資料

- [DoD STIG VIB](https://flings.vmware.com/dod-security-technical-implementation-guide-stig-esxi-vib)
- [PowerCLI 11.3](https://www.powershellgallery.com/packages/VMware.PowerCLI/11.3.0.13990089)
- [PowerShell 5以降](https://docs.microsoft.com/en-us/skypeforbusiness/set-up-your-computer-for-windows-powershell/download-and-install-windows-powershell-5-1)
- [ESXi 6.7 U2以降](https://my.vmware.com/web/vmware/downloads/details?downloadGroup=ESXI670&productId=742)
