---
title: "Hyper-V VMをProxmox VEへ移行する可逆チェックリスト"
date: 2026-10-11
lastmod: 2026-11-19
toc: true
draft: false
description: "Hyper-VのVMを、停止状態でのエクスポート、ファームウェアの一致、ディスクのインポート、分離した起動テスト、ロールバック計画を使ってProxmox VEへ移行します。"
genre: ["仮想化", "システム管理", "ホームラボ"]
tags: ["Hyper-VからProxmoxへの移行", "Hyper-V移行", "Proxmox VE移行", "VHDXインポート", "qm disk import", "VM切り替え", "Hyper-Vエクスポート", "Proxmox上のWindows VM", "Proxmox上のVirtIO", "VMロールバック", "UEFI移行", "Hyper-Vチェックポイント", "仮想TPM", "BitLocker回復", "ホームラボ移行"]
cover: "/img/cover/hyper-v-to-proxmox-migration-checklist.webp"
coverAlt: "ディスクが青いサーバーラックからオレンジ色のラックへ橋を渡り、別の戻り経路と移行先の盾が描かれています。"
coverCaption: "新しいゲストが切り替えチェックに合格するまで、移行元VMを利用可能な状態で維持します。"
---

**Hyper-Vのエクスポート** は仮想マシンのファイルを保持しますが、Proxmox VEでは新しいゲスト設定と、インポートしたVHDX仮想ディスクファイルが必要です。ファイルをコピーできても、ゲストの起動やサービス提供が保証されるわけではありません。このチェックリストでは、停止状態でのエクスポート、制御された起動テスト、明確な復帰手順を経て1台のVMを移行します。

<!--more-->

## 要点

- **移行元を記録：** エクスポート前にファームウェア世代、ディスクパス、チェックポイント、ネットワーク設定、暗号化を記録します。
- **書き込みを停止：** 最終エクスポート前にHyper-V VMをシャットダウンし、Proxmoxでのテスト中も停止状態を保ちます。
- **起動方式を一致：** Hyper-V第1世代はレガシーBIOS、第2世代はUEFIを使用します。
- **サービスを検証：** 移行元を廃止する前に、データ、ネットワークアクセス、バックアップ、ゲストの健全性を確認します。

## 作業前の準備

メンテナンス時間を確保し、使い捨てVMで先にテストします。Hyper-VとProxmox VEの管理者アクセス、エクスポート用ストレージ、移行コピーとは別の検証済みバックアップが必要です。すべての仮想ディスクを転送し、ゲストアプリケーションを試験する時間も見込みます。停止時間はディスク容量と転送速度で決まります。

この手順は仮想ディスクを使う一般的なVMを対象とします。 **シールドVM、パススルーディスク、共有ディスク、クラスターワークロード、ハードウェアに紐づくライセンス** には個別の計画が必要です。切り替えの決定者とロールバック期限を記録してください。本番ネットワーク上で、同じマシンIDを持つ複製VMを同時に起動しないでください。

| 移行元の情報 | 用途 |
|---|---|
| **VM世代とファームウェア** | ProxmoxでSeaBIOSまたはOVMFを選ぶ |
| **セキュアブートの状態とテンプレート** | 起動ポリシーを合わせ、互換性のあるキーを登録する |
| **ブートディスクとデータディスク** | 必要なVHDX仮想ディスクをすべて正しい順にインポートする |
| **チェックポイントとAVHDXファイル** | 差分ディスクを独立したベースディスクとして扱わない |
| **IP、DNS、MAC、VLAN** | IDを重複させずに接続を復元する |
| **vTPMとBitLocker** | 仮想ハードウェアを変える前に回復手段を準備する |
| **サービスとデータの確認項目** | 成功とロールバックの判断材料を定める |

第1世代はレガシーBIOS、第2世代はUnified Extensible Firmware Interface（UEFI）を使用します。 **AVHDXファイル** はベースVHDXにリンクされたHyper-Vの差分ディスクです。 **vTPM** はBitLockerなどで使う仮想Trusted Platform Moduleです。 **VLAN** は共有ネットワーク機器上に作る独立した論理ネットワークです。

**SeaBIOS** はレガシーBIOSファームウェアを提供します。 **OVMF** はUEFIファームウェアを提供します。 **VirtIO** は高速な仮想デバイスインターフェイスで、ゲストドライバーが必要です。 **initramfs** はLinuxの初期起動用ファイルシステムで、メインシステムの起動前にドライバーを読み込みます。

## Hyper-Vの仮想マシンを調査する

Hyper-Vホスト上の管理者権限PowerShellで、次の読み取り専用コマンドを実行します。これらは未テストの例です。使用前に、インストール済みHyper-Vモジュールと変更手順に照らして各コマンドを確認してください。プロンプトにVM名を入力します。

```powershell
$vmName = Read-Host "Hyper-V VM名"
Get-VM -Name $vmName | Select-Object Name, State, Generation, ProcessorCount, MemoryAssigned
Get-VMHardDiskDrive -VMName $vmName | Select-Object ControllerType, ControllerNumber, ControllerLocation, Path
Get-VMSnapshot -VMName $vmName | Select-Object Name, CreationTime
Get-VMNetworkAdapter -VMName $vmName | Select-Object Name, SwitchName, MacAddress
```

[Hyper-V PowerShellモジュール](https://learn.microsoft.com/en-us/powershell/module/hyper-v/)には、これらの調査コマンドが記載されています。ディスクパスをVM設定と照合し、接続されたISO、データディスク、仮想スイッチ、固定アドレス、DHCP予約を記録します。ゲストOSとアプリケーションのバージョンも記録します。テストコピーを復元するか、最近の復元記録を確認してバックアップを検証してください。復旧テストなしのファイルコピーでは証拠として不十分です。

**第2世代** VMでは、ファームウェアとセキュリティ設定も記録します。

```powershell
Get-VMFirmware -VMName $vmName | Format-List *
Get-VMSecurity -VMName $vmName | Format-List *
```

**セキュアブート** の状態、テンプレート、vTPM設定を記録します。Microsoftの[**`Get-VMFirmware`** リファレンス](https://learn.microsoft.com/en-us/powershell/module/hyper-v/get-vmfirmware)によると、このコマンドは第2世代専用です。[**`Get-VMSecurity`**](https://learn.microsoft.com/en-us/powershell/module/hyper-v/get-vmsecurity)はVMのセキュリティ設定を表示します。第1世代ゲストでは **`Get-VMFirmware`** を実行しないでください。 **MACアドレス** はネットワークインターフェイスを識別します。 **DNS** は名前をアドレスに対応付けます。 **DHCP** はネットワーク設定を割り当てます。 **EFIディスク** はUEFI設定を保存します。

**最終エクスポート前にチェックポイントを解決してください。** Microsoftによると、Hyper-VのエクスポートにはチェックポイントファイルとVHDXディスクが含まれます。Hyper-Vでチェックポイントを削除すると差分ディスクが統合されます。チェックポイントを消すためにファイルシステムから **`.avhdx`** ファイルを削除しないでください。統合が失敗するかディスクチェーンが不完全なら作業を止め、[Microsoftのチェックポイント復旧ガイダンス](https://learn.microsoft.com/en-us/troubleshoot/windows-server/virtualization/hyper-v-snapshots-checkpoints-differencing-disks)に従ってください。[Microsoftのチェックポイントガイド](https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/checkpoints)には通常の削除と統合が説明されています。

**BitLocker** または **仮想TPM** を使うWindowsゲストでは、仮想ハードウェアの変更前に回復キーを取得して確認します。Hyper-Vの[第2世代VMセキュリティ資料](https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/generation-2-virtual-machine-security-features)はvTPMを使った暗号化を説明しています。Microsoftの[BitLockerに関するよくある質問](https://learn.microsoft.com/en-us/windows/security/information-protection/bitlocker/bitlocker-key-management-faq)は、起動変更が回復を要求する理由を説明します。新しいProxmox TPMデバイスは古いTPM状態を再現しません。キーはエクスポートしたVMの外に保管してください。

## 停止中のVMをエクスポートする

ゲストを正常にシャットダウンします。Hyper-Vの状態がSaved (保存済み)ではなく **Off** (停止) であることを確認します。チェックポイント統合の完了を待ち、十分な空き容量のある場所へVMをエクスポートします。Hyper-V ManagerでVMを右クリックし、 **Export** (エクスポート) を選んで保存先を指定します。PowerShellでの方法は次のとおりです。

```powershell
$vmName = Read-Host "停止中のHyper-V VM名"
$exportPath = Read-Host "エクスポート先ディレクトリ"
$vm = Get-VM -Name $vmName -ErrorAction Stop
if ($vm.State -ne 'Off') { throw "VMを停止し、Hyper-Vの状態がOff (停止)になってからエクスポートしてください。" }
Export-VM -Name $vmName -Path $exportPath
```

[Microsoftのエクスポートガイド](https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/deploy/export-and-import-virtual-machines)によると、エクスポートには仮想ディスク、構成、チェックポイントファイルが含まれます。[**`Export-VM`** リファレンス](https://learn.microsoft.com/en-us/powershell/module/hyper-v/export-vm)でコマンドの仕様を確認してください。保存先で想定したディスクファイルとサイズを確認します。停止した移行元VMと独立バックアップは保持してください。 **インポート中にエクスポートファイルを変更しないでください。**

VHDXファイルをProxmoxホストからアクセスできる場所へ転送します。エクスポートには機密性のあるゲストデータが含まれます。暗号化した転送を使い、転送先と保存先へのアクセスを制限し、検証後に一時コピーを削除します。転送場所と移行先ストレージの空き容量を確認します。ロールバック用に未変更のエクスポートを保管してください。 **`.avhdx`** が含まれる場合、ファイル名だけでベース **`.vhdx`** を選び、それに最新の書き込みが含まれると判断しないでください。続行前にHyper-Vでディスクチェーンを解決します。

## Proxmoxの仮想マシンを作成する

ProxmoxのWeb UIで、記録済みのゲストOS種別、CPU、メモリを使って新しいVMを作ります。未使用のVM IDを選びます。新しいOSをインストールしないでください。ソースディスクのインポート前に、ウィザードが作った空ディスクを削除します。初回起動時はネットワークアダプターを本番ブリッジから切り離すか、隔離テストネットワークに接続します。

| Hyper-Vの移行元 | Proxmoxの移行先 |
|---|---|
| **第1世代、レガシーBIOS** | SeaBIOS |
| **第2世代、UEFI** | OVMF、EFIディスク、同等のセキュアブートポリシー |
| **VirtIOストレージドライバーがないWindowsブートディスク** | 最初はSATAで接続 |
| **vTPMまたはBitLockerを使うWindows** | 必要なら新しいTPM状態デバイスを追加し、初回起動前に回復キーを用意 |

[MicrosoftのVM世代ガイド](https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/plan/Should-I-create-a-generation-1-or-2-virtual-machine-in-Hyper-V)は第1世代をレガシーBIOS、第2世代をUEFIに対応付けています。Proxmoxの[VM資料](https://github.com/proxmox/pve-docs/blob/master/qm.adoc)にはSeaBIOS、OVMF、UEFI設定を保持するEFIディスクが説明されています。 **移行元の起動方式に合わせます。** 移行中に変更すると、別の起動問題が発生します。

第2世代では **セキュアブート** が有効だったかも合わせます。移行元テンプレートを確認し、ゲスト用に互換性のある登録済みキーを選びます。Hyper-Vのテンプレート名はProxmoxには移りません。Proxmoxの4 MB EFIディスクと **Pre-Enroll keys**（キーを事前登録する）オプションはセキュアブート用キーを提供し、既定でセキュアブートを有効にします。切り替え前に移行先の起動を確認してください。[Microsoftのファームウェア資料](https://learn.microsoft.com/en-us/powershell/module/hyper-v/set-vmfirmware)は移行元テンプレートの要件を説明し、[ProxmoxのEFIディスク資料](https://github.com/proxmox/pve-docs/blob/master/qm.adoc)は移行先キーを説明しています。

EFIキーを変更する前に回復キーが保管済みであることを確認し、現在のプロテクターIDを記録します。インストール済みProxmox VEとOVMFの資料に従ってEFIキーを登録します。回復キーを再確認し、初回起動前に `manage-bde -status` を確認してください。プロテクターの一時停止、無効化、削除を一般的な移行手順にしないでください。ファームウェアパッケージ、セキュアブート状態とファームウェアの各バージョン、BitLocker状態を記録します。

移行元が **vTPM** を使う場合、初回起動前にProxmoxのHardware (ハードウェア)パネルで **TPM State** (TPM状態) を追加します。ゲストに記録済みの1.2要件がなければ **バージョン2.0** を選びます。これは新しいTPM状態を作成し、Hyper-VのvTPMを複製しません。BitLockerを使うゲストでは初回起動時に検証済みの回復キーが必要です。[Proxmox TPM資料](https://github.com/proxmox/pve-docs/blob/master/qm.adoc)にはHardware (ハードウェア)操作とバージョンが説明されています。

Windowsでは、必要なVirtIOストレージドライバーが既に入っていない限り、最初はSATAブートディスクを使います。起動できたら対応するVirtIOドライバーをインストールし、仮想デバイスを1つずつ変更します。Proxmoxは性能面でVirtIO SCSIを推奨しますが、ブートドライバーがなければWindowsはシステムディスクにアクセスできません。Linuxではバスを変える前にinitramfsに移行先ストレージドライバーが含まれることを確認します。[Proxmox VM資料](https://github.com/proxmox/pve-docs/blob/master/qm.adoc)はディスクコントローラーを説明しています。

## ディスクをインポートして接続する

Proxmoxホストでコピー済みVHDXのパスを確認します。次の例ではVM ID **230** のディスクを、ストレージID **`local-lvm`** にインポートします。3つの値を自分の環境に置き換えてください。

```bash
qm disk import 230 /path/to/exported/boot.vhdx local-lvm
```

Proxmoxの[**`qm disk import`** リファレンス](https://github.com/proxmox/pve-docs/blob/master/generated/qm.1-synopsis.adoc)によると、ソースイメージは **未使用ディスク** としてインポートされます。[QEMUのイメージ資料](https://www.qemu.org/docs/master/system/images)ではVHDXが対応する変換形式に挙げられています。追加のデータディスクも個別にインポートします。各タスクの完了を待ち、インポート後のサイズを移行元の記録と比較してください。

VMの **Hardware** (ハードウェア) パネルで、Windowsの初回起動時は未使用のブートディスクを **SATA** として接続します。記録した順でデータディスクを接続します。 **Options > Boot Order** (オプション > 起動順序) でブートディスクを選びます。第2世代ゲストでは **OVMF** とEFIディスクを確認してください。検証が完了するまでインポートファイルと移行元VMを保管します。

## 切り替え前のテスト

Proxmoxゲストを隔離ネットワークで起動します。コンソールで起動画面、OSログイン、ディスクボリューム、アプリケーションデータ、サービスログを確認します。ログイン画面が出ても移行成功とは限りません。エクスポート前に記録した検査を行い、代表的な処理や最新データの読み取りも確認します。

BitLockerゲストで求められた場合は回復キーでロックを解除します。Windows起動後、管理者権限のプロンプトでシステムボリュームの保護状態とプロテクターを確認します。

```powershell
manage-bde -status C:
manage-bde -protectors -get C:
```

Microsoftの[BitLocker運用ガイド](https://learn.microsoft.com/en-us/windows/security/operating-system-security/data-protection/bitlocker/operations-guide)はプロテクター確認と回復キーのバックアップを説明しています。出力には機密性のある回復情報が含まれます。チケットや公開ログに貼り付けないでください。ポリシーに従って必要なプロテクターを確認し、現在の回復方法を保管します。切り替え前にゲストを再起動し、回復要求なしで起動することを確認します。回復が繰り返し要求される場合は移行チェック失敗です。元のキーを捨てる理由にはなりません。

| テスト | 合格条件 |
|---|---|
| **起動とディスク** | ゲストが起動し、想定したすべてのボリュームがマウントされる |
| **セキュアブートとBitLocker** | 起動ポリシーが維持され、暗号化ゲストが回復要求を繰り返さず再起動する |
| **アプリケーション** | 代表的な読み取りまたは処理が成功する |
| **ネットワーク** | 必要な接続元が指定ポートでテストゲストに到達する |
| **復旧** | 移行元の廃止前にProxmoxバックアップと隔離復元テストが成功する |
| **運用** | 監視、時刻同期、シャットダウン、ゲストエージェントが想定どおり動作する |

アプリケーションのテストが通ったら、メンテナンス時間中に本番ネットワーク経路またはアドレスを切り替えます。Hyper-Vは停止状態に保ちます。仮想NICの変更に伴いDHCP予約やゲスト内の固定アドレスの修正が必要になることがあります。別のクライアントからDNS、ファイアウォール規則、依存サービスを確認します。Proxmoxの[VM資料](https://github.com/proxmox/pve-docs/blob/master/qm.adoc)はネットワークデバイスとゲストエージェントの設定を説明しています。

## トラブルシューティングとロールバック

| 症状 | 最初に確認する項目 |
|---|---|
| **起動デバイスがない** | 起動順序、インポートしたブートディスク、BIOS/UEFI方式、セキュアブートキー |
| **Windowsのストレージエラー** | SATA接続と不足しているVirtIOストレージドライバー |
| **BitLocker回復が繰り返される** | 新しいTPM状態、セキュアブートポリシー、起動測定、プロテクター |
| **ゲスト起動後にネットワークがない** | 新しい仮想NIC、ブリッジ、VLAN、DHCP予約、固定アドレス |
| **データが古い、または見当たらない** | VHDXの選択ミス、不完全なエクスポート、チェックポイントチェーン、データディスク不足 |

ロールバック期限までに必須テストに失敗したら、Proxmox VMを停止して本番ネットワークから切り離します。移行元のネットワーク経路を戻し、元のHyper-V VMを起動します。 **同じ本番IDを持つ2つのコピーを同時に動かさないでください。** Hyper-Vに戻す前にProxmox側で受け付けた書き込みを記録します。移行元ディスクには反映されていないため、別途復元または調整が必要です。

Proxmoxゲストがサービス検査、新しいバックアップ、隔離復元テストを通過し、合意した観察期間が終わるまで、移行元VMとエクスポートを保持します。サイトの[仮想化比較](/articles/vmware-esxi-citrix-xenserver-hyper-v-comparison/)はプラットフォーム選択に役立ちます。[Proxmox VEアップグレードガイド](/articles/proxmox-ve-8-to-9-upgrade-guide/)は後の保守作業を扱います。 **ディスクのインポートが終わった時点ではなく、新しいホストでワークロードと復旧経路が動作して初めて移行完了です。**

## 次の手順

ワークロード、バックアップ、ロールバックの確認が合意した観察期間中に通るまで、移行元VMとエクスポートを保持します。移行元を廃止する前に、[Proxmox VMバックアップ復元ドリル](/articles/proxmox-vm-backup-restore-drill/)を確認してください。
