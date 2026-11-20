---
title: "Proxmox VE 9: 仮想ディスクの使用量を抑え、空き領域を回収する"
date: 2026-11-09
lastmod: 2026-11-20
toc: true
draft: false
description: "Proxmox VE 9 の VM と LXC のストレージ使用量を減らします。ディスク形式とストレージバックエンドを比較し、discard を有効にして、Windows と Linux のゲストで trim を実行し、領域回収前にスナップショットを確認します。"
genre: ["仮想化", "Linux 管理", "Proxmox VE プラットフォーム", "ストレージ", "家庭用ラボ"]
tags: ["Proxmox VE 9 のディスク領域", "Proxmox のシンプロビジョニング", "Proxmox の discard 通知", "Proxmox の TRIM コマンド", "Proxmox Windows ゲストの ReTrim", "Proxmox Linux ゲストの fstrim", "Proxmox LXC のディスク使用量", "Proxmox LVM シンプロビジョニング", "Proxmox ZFS スパース zvol", "Proxmox Ceph RBD ブロックデバイス", "Proxmox qcow2 形式", "Proxmox raw ディスク", "Proxmox スナップショット", "仮想ディスク領域の回収", "Proxmox のストレージ種別", "VirtIO SCSI コントローラー", "Proxmox のゼロ書き込み検出", "Proxmox バックアップストレージ"]
cover: "/img/cover/proxmox-ve-9-virtual-disk-space-reclamation.webp"
coverAlt: "使用中の仮想ディスクブロックとストレージプールの空き容量を、矢印で結んだ2つのブロック図で示しています。"
coverCaption: "ゲスト内の削除、discard、ストレージ領域の回収はそれぞれ別の処理です。"
---

**ゲストのファイルシステムが小さくなっても、Proxmox のストレージ使用量が減るとは限りません。** ホストの領域を空けるには、シンプロビジョニングに対応したディスク、VM で機能する discard 経路、スナップショットが保持するブロックのないバックエンドが必要です。このガイドでは Proxmox VE 9 の VM と LXC コンテナーの設定と確認方法を説明します。

<!--more-->

## 要点

- **まずバックエンドを選びます。** 仮想ディスクの公称サイズとホストで割り当てられた領域が異なるのは、イメージ形式またはストレージバックエンドがシンプロビジョニングに対応する場合だけです。
- **VM の discard を有効にし、ゲスト内で trim を実行します。** Windows の ReTrim と Linux の `fstrim` は、未使用ブロックの要求を仮想ディスク経由で送ります。
- **スナップショットとバックアップを別々に確認します。** スナップショットが参照する古いブロックは割り当てられたままです。バックアップファイルと PBS チャンクには、それぞれ独自の保持ルールがあります。
- **LXC のマウントは種類ごとに扱います。** 管理対象の rootfs とマウントポイント、バインドマウント、デバイスマウントでは、所有者とバックアップ動作が異なります。

## 作業前の確認

**Proxmox VE 9 の管理者アクセス権**、対象ゲストの検証済みバックアップ、処理に必要な空きプール容量を用意します。設定を変える前に、各ゲストの ID、ディスクバス、ボリューム ID、ストレージ ID、スナップショット、現在の割り当て量を記録します。復元手順は[VM 復元ドリル](/articles/proxmox-vm-backup-restore-drill/)で確認します。

**所要時間の目安:** ゲストごとに20〜60分。大規模な trim やクリーンアップには追加時間が必要です。**難易度:** 中級。まずリスクの低い VM 1台で実施し、前後のストレージ使用量を比較します。

> **警告:** シンプールが満杯になると、ゲストで I/O エラーが発生し、ファイルシステムが損傷する恐れがあります。プールのデータ領域とメタデータ領域の空きを監視せずに容量を過剰割り当てしないでください。[Proxmox ストレージのドキュメント](https://github.com/proxmox/pve-docs/blob/master/pvesm.adoc)

## 割り当ての経路をたどる

**削除**、**discard**、**領域回収**は別々の層で起きます。ゲストがファイルを削除すると、ファイルシステムはブロックを空きとして記録します。ファイルシステムはそのブロックに対して TRIM または UNMAP を送ります。仮想ディスクで discard が有効なら QEMU が要求を転送します。形式とプールが対応していれば、ストレージバックエンドが物理領域の割り当てを解除します。[Proxmox VM ディスクのドキュメント](https://github.com/proxmox/pve-docs/blob/master/qm.adoc)

| 層 | 確認項目 | 参考になる情報 |
|---|---|---|
| **ゲストのファイル** | ファイルシステムの空き容量 | Windows のボリュームのプロパティ、または Linux の `df -h` |
| **仮想ディスク** | バス、discard、SSD エミュレーション、イメージ形式 | VM の **ハードウェア** タブ、または `qm config VMID` |
| **PVE ボリューム** | 所有者と設定サイズ | ストレージの **コンテンツ** タブ、または `pvesm list STORAGE_ID` |
| **ストレージプール** | 空きデータ領域、メタデータ、保持ブロック | `pvesm status` とバックエンド固有のツール |

**100 GiB の仮想ディスクは容量上限であり、100 GiB が割り当て済みという意味ではありません。** 逆に、ゲストが使用中と報告する領域が20 GiBでも、ホストが20 GiBしか使用していない証拠にはなりません。メタデータ、スナップショット、バックアップコピー、過去に書き込まれたブロックで数値は変わります。[Proxmox ストレージのドキュメント](https://github.com/proxmox/pve-docs/blob/master/pvesm.adoc)

## ディスク形式を比較する

**Proxmox が提示するイメージ形式はストレージバックエンドで決まります。** ZFS zvol と Ceph RBD は raw 仮想ディスクを使います。LVM は通常 raw を使いますが、以下で説明する Proxmox VE 9 のボリュームチェーン例外があります。directory や NFS などのファイルバックエンドは raw または qcow2 に対応します。raw 自体はシン割り当てもスナップショットも提供しません。基盤ストレージ側でその機能を提供する必要があります。qcow2 はイメージ層でコピーオンライト割り当てとスナップショットを提供します。[Proxmox VM ディスクのドキュメント](https://github.com/proxmox/pve-docs/blob/master/qm.adoc)

| 形式 | 割り当て方式 | 容量上のトレードオフ |
|---|---|---|
| **ファイルストレージ上の qcow2** | 書き込みに応じて qcow2 がクラスタを割り当てる | イメージメタデータとスナップショットチェーンが領域を使う |
| **ファイルストレージ上の raw ファイル** | 対応する場合はファイルシステムのスパースファイル動作 | raw 単体ではシンプロビジョニングもスナップショットも提供しない |
| **raw ブロックボリューム** | LVM のシンプロビジョニング、ZFS、Ceph RBD などのバックエンドストア | プール割り当てとスナップショットはバックエンドに依存する |

**Proxmox VE 9 のシック LVM には専用のスナップショットモードがあります。** `snapshot-as-volume-chain` はシック LVM 論理ボリューム間で qcow2 バッキング関係を使います。qcow2 の内部スナップショットは使いません。このオプションは新規作成する VM ディスクだけに適用され、現行の Proxmox ドキュメントでは技術プレビューです。PVE 上では各スナップショットが全容量割り当て済みのように見えます。SAN の割り当てが実際に小さくなるのは、基盤ストレージがシンプロビジョニングと discard に対応するときだけです。[Proxmox LVM ストレージのドキュメント](https://github.com/proxmox/pve-docs/blob/master/pve-storage-lvm.adoc)

**拡張子が `.raw` という理由だけでディスクを変換しないでください。** 先にストレージプラグインと割り当て済みブロックを確認します。`local-lvm` 上の raw ディスクと、通常の directory ストレージ上で全領域が割り当てられた raw ファイルでは、割り当て動作が異なります。

## ストレージ種別を比較する

Proxmox は**ファイルストレージ**と**ブロックストレージ**を区別します。ストレージプラグインは、スナップショット、クローン、共有、各プールで受け入れるコンテンツ種別も制御します。形式や機能を前提にする前に **Datacenter > Storage** の登録内容を確認してください。[Proxmox ストレージ種別一覧](https://github.com/proxmox/pve-docs/blob/master/pvesm.adoc)

| ストレージ | VM ディスクの動作 | 領域回収の確認 |
|---|---|---|
| **Directory、ext4、XFS** | raw または qcow2 ファイル | `du` の割り当て済みバイト数とイメージの仮想サイズを比較します。別のストレージ層がスナップショットを提供する場合はそれも確認します。 |
| **NFS、CIFS** | 共有ストレージ上の raw または qcow2 ファイル | サーバー側の割り当て量を確認します。ゲストの trim だけではサーバーの使用量低下を証明できません。 |
| **LVM シンプロビジョニング (`local-lvm`)** | ローカル限定の thin raw 論理ボリューム | `lvs` でシンプールのデータ使用率とメタデータ使用率を監視します。 |
| **シック LVM** | raw LV、または VE 9 の qcow2 ボリュームチェーン | ゲスト内の削除では固定 LV 予約量は減りません。SAN のシン割り当ては別に確認します。 |
| **ZFS ストレージ (`local-zfs`)** | raw zvol またはコンテナーのサブボリューム | `sparse`、データセットのプロパティ、プール使用量、スナップショットを確認します。 |
| **Ceph RBD** | 共有ストレージ上の thin `raw RBD` イメージ | Ceph プール容量、イメージ使用量、スナップショット、discard の動作を確認します。 |
| **Btrfs** | raw イメージ向け Btrfs サブボリュームを使うファイルベースのボリューム | PVE Btrfs プラグインを技術プレビューとして扱い、スナップショットとファイルシステム使用量を調べます。 |

**他のストレージプラグインは別の役割を担います。** CephFS は共有ファイルストレージを提供します。iSCSI と Fibre Channel は共有ブロックデバイスを公開し、多くの場合 LVM で VM ボリュームに分割します。`iSCSI 接続の ZFS iSCSI` はリモートの ZFS ベースのブロックストレージを使います。Proxmox Backup Server (PBS) は稼働中の VM ディスクではなくバックアップを保存します。`images`、`rootdir`、`backup`、`iso` のデータを置く前に、各ストレージで有効な **Content** 種別を確認してください。[Proxmox ストレージ種別一覧](https://github.com/proxmox/pve-docs/blob/master/pvesm.adoc)

**ファイルストレージの割り当てフラグは作成時に重要です。** ストレージレベルの `format` 既定値は、対応する場合に `raw`、`qcow2`、`vmdk` を選びます。raw と qcow2 ファイルの `preallocation` 設定は `off`、`metadata`、`falloc`、`full` を受け付けます。既定値は `metadata` で、raw では `off` として扱われます。`full` はファイル領域を先に予約するため、通常の小さな初期使用量という利点が失われます。大きなディスクを作成する前にストレージ設定を確認してください。ストレージレベルの `shared` フラグは、既に存在する共有アクセスを宣言するだけです。ローカルストレージを共有ストレージに変えるものではありません。[Proxmox 共通ストレージプロパティ](https://github.com/proxmox/pve-docs/blob/master/pvesm.adoc)

**ZFS で zvol を thin 作成する設定は `sparse` です。** sparse zvol を使わない場合、作成時に設定済みボリュームの動作に応じて容量を予約します。既存環境を変更する前に、実際のストレージ設定とプールを調べてください。[Proxmox ZFS ストレージのドキュメント](https://github.com/proxmox/pve-docs/blob/master/pve-storage-zfspool.adoc)

**Directory ストレージでは追加確認が必要です。** qcow2 ファイルの論理長は、ゲストから見える仮想容量ではありません。`du -h` はイメージファイル用に割り当てられたファイルシステムブロックを示します。`ls -lh` はイメージファイルの論理長を表示します。停止中の VM では `qemu-img info` が仮想容量とホストディスクサイズを報告します。NFS では、最終的な容量判断にサーバーの計上値を使います。[QEMU `qemu-img` リファレンス](https://www.qemu.org/docs/master/tools/qemu-img.html)

**NFS にはもう1つの割り当て境界があります。** qcow2 ファイル内で空のクラスタを再利用することと、NFS サーバーがファイルブロックを解放することは別です。ホールパンチには、クライアント、ネゴシエート済みプロトコル、サーバー、サーバー側ファイルシステムすべての対応が必要です。NFSv4.2 は `DEALLOCATE` を定義しますが、バージョン番号だけではサーバーが領域を返した証拠になりません。ネゴシエート済みの NFS マウントを調べ、サーバー側で割り当てを測定してください。[NFSv4.2 `DEALLOCATE` 仕様](https://www.rfc-editor.org/rfc/rfc7862.html#section-6.2.2)

## VM ディスクのフラグを設定する

Proxmox の画面で **VM > Hardware > Hard Disk > Edit** を開きます。ディスクバスと詳細オプションを確認します。以下のフラグは割り当てに影響するか、最適化が役立つかを決めます。[公式 `qm` オプションリファレンス](https://github.com/proxmox/pve-docs/blob/master/generated/qm.conf.5-opts.adoc)にバスごとの対応状況があります。

| バス | 領域関連の選択肢 |
|---|---|
| **IDE** | 古い互換性用です。新しいドライバーのないゲストでのみ使用します。 |
| **SATA** | 広く対応するエミュレーションです。領域回収を前提にする前にゲストの trim とディスク設定を確認します。 |
| **VirtIO SCSI を使う SCSI** | discard とディスクごとの設定に適した現代的な経路です。Windows には VirtIO ドライバーが必要です。 |
| **VirtIO Block** | 準仮想化ディスクです。Linux の discard にはカーネル5.0以降が必要です。SSD エミュレーションには対応しません。 |

| 設定 | 効果 | 指針 |
|---|---|---|
| **discard を有効化 (`on`)** | ゲストの TRIM または UNMAP を転送する | 対応する thin バックエンドでゲスト主導の領域回収を行う場合に必要です。既定値の `ignore` は転送を止めます。 |
| **SSD エミュレーション `ssd=1`** | ディスクを SSD としてゲストに提示する | trim を発行する前に SSD という識別が必要なゲストがあります。物理ストレージを高速化する設定ではありません。VirtIO Block では使えません。 |
| **ゼロ書き込みの検出 `detect_zeroes=1`** | ゼロ書き込みを検出し最適化を試みる | 任意の I/O 最適化です。ゲスト trim の代わりにはならず、領域回収も保証しません。 |
| **バス: SCSI / VirtIO `SCSI single`** | VirtIO コントローラー経由で SCSI ディスクを公開する | 現代的な Windows と Linux ゲストの実用的な既定値です。Windows VirtIO ドライバーをインストールします。 |
| **バス: VirtIO Block** | VirtIO ブロックデバイスを使う | Linux の discard にはカーネル5.0以降が必要です。SSD エミュレーションには対応しません。 |
| **I/O スレッド `iothread=1`** | ドライブ I/O を別スレッドに割り当てる | VirtIO Block、または VirtIO `SCSI single` コントローラー上の SCSI で使います。性能設定であり、領域回収スイッチではありません。 |
| **キャッシュと AIO** | I/O バッファリングと非同期 I/O を変更する | ワークロードとバックエンドに合わせて調整します。どちらもディスクを縮小しません。 |
| **Backup `backup=0`** | ディスクを VM バックアップから除外する | バックアップ範囲を減らし、VM バックアップからの復旧対象外にします。別のバックアップ方法を記録します。 |
| **Replicate `replicate=0`** | ディスクをストレージレプリケーションから除外する | 複製データを減らし、レプリカにディスクを含めません。 |

**他のドライブオプションは動作を定義するもので、領域回収設定ではありません。** `format` は複数形式に対応するバックエンドでディスクを割り当てるときに適用されます。`size` は仮想容量であり割り当てバイト数ではありません。`ro=1` はディスクを読み取り専用にします。`snapshot=1` は QEMU の一時スナップショットモードを有効にし、VM のシャットダウン時にディスク変更を破棄します。Proxmox VM スナップショットへのディスク参加を指定するスイッチではありません。永続データには使わないでください。`backup=0` または `replicate=0` を使う前に復旧対象を確認します。[Proxmox VM ディスクオプション](https://github.com/proxmox/pve-docs/blob/master/generated/qm.conf.5-opts.adoc)

**短縮した `qm set --scsi0` 文字列を既存ドライブに貼り付けないでください。** **`qm config VMID`** を調べ、編集時に完全なボリューム ID と既存オプションを保持します。短縮したドライブ割り当ては他のディスク設定を失わせる恐れがあります。画面から変更した後も保存済みのディスクオプションを確認してください。

```bash
qm config 100
pvesm status
```

`100` は VM ID の例です。コントローラーが **VirtIO `SCSI single`** で、ゲストに必要なドライバーが入っている既存 VM に**新しい**64 GiB の SCSI ディスクを追加する場合、次のコマンドで割り当て構文を確認できます。VM ID とストレージ ID を自分の値に置き換えてください。

```bash
qm set 100 --scsi0 local-lvm:64,discard=on,ssd=1,iothread=1
```

**例を使う前に `scsi0` が既存か確認してください。** このコマンドはスロットを変更します。既存ディスクの正確なオプション文字列を保持しやすい場合は GUI を使います。[Proxmox `qm` コマンドリファレンス](https://github.com/proxmox/pve-docs/blob/master/generated/qm.1-synopsis.adoc)

## ゲストのファイルを整理する

**最初にゲストのファイルを整理します。** Windows のストレージ設定、一時ファイル、古いインストーラー、アプリケーションキャッシュ、ごみ箱を確認します。データベースやコンテナーランタイムは、それぞれのインターフェースでクリーンアップします。割り当てを減らす目的だけでアプリケーションの稼働データを削除すると、データ損失につながります。

**ボリュームが discard 対応の仮想ディスクを使うことを確認してから** Windows VM で管理者 PowerShell を開きます。

```powershell
fsutil behavior query DisableDeleteNotify
Optimize-Volume -DriveLetter C -ReTrim -Verbose
```

`DisableDeleteNotify = 0` は、表示されたファイルシステムで Windows の削除通知が有効であることを示します。**ReTrim** は現在未使用のボリューム領域について trim 要求を再送します。コマンドの成功はゲストが処理を発行したことを示すだけで、ホストで回収したバイト数を示しません。ジョブ完了後にホストを確認します。[Microsoft `Optimize-Volume` リファレンス](https://learn.microsoft.com/en-us/powershell/module/storage/optimize-volume?view=windowsserver2025-ps)および[Proxmox VM ディスクのドキュメント](https://github.com/proxmox/pve-docs/blob/master/qm.adoc)

**QEMU ゲストエージェントを TRIM と混同しないでください。** エージェントはゲスト制御やバックアップ整合性機能を支援します。ファイルシステムの削除通知は仮想ディスクの経路を通ります。エージェントを入れただけではブロックは回収されません。[Proxmox VM ゲストエージェントのドキュメント](https://github.com/proxmox/pve-docs/blob/master/qm.adoc)

## ファイルシステムの未使用ブロックを通知する

**trim の前にブロック経路とファイルシステムを確認します。** 最新のディストリビューションでは `fstrim.timer` が定期実行される場合があります。状態を調べ、不要なゲストデータを削除した後にマウント済みファイルシステムを trim します。

```bash
lsblk -D
systemctl status fstrim.timer
sudo fstrim -av
```

**`lsblk -D`** は可視ブロックデバイスの discard の粒度と上限を報告します。**`fstrim -av`** は対応するマウント済みファイルシステムを trim し、送信した範囲を表示します。送信バイト数はプールに返されたバイト数と同じではありません。暗号化、LVM、RAID などの積層デバイスでは、各層が discard に対応する必要があります。[Red Hat の未使用ブロックのガイド](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/8/html/managing_file_systems/discarding-unused-blocks_managing-file-systems)

スケジュール済み trim、または意図的に設定したオンライン discard ポリシーを使います。**ストレージ経路を調べずに、すべてのファイルシステムで連続 `discard` を有効にしないでください。** ゲストの trim 後に PVE ボリュームとプールを確認します。削除済みレコードが引き続きファイルを占有する場合は、データベースまたはサービス固有の圧縮ポリシーも確認してください。

## コンテナーのストレージは別に確認する

**LXC の rootfs にはエミュレート VM ディスクバスがありません。** `pct config CTID` を開始点にし、すべての `rootfs` と `mpN` エントリーを特定します。Proxmox はストレージ管理マウント、バインドマウント、デバイスマウントを区別します。コンテナー内のパスだけでは、どのホストボリュームがブロックを所有するか分かりません。[Proxmox コンテナのマウントポイント](https://github.com/proxmox/pve-docs/blob/master/pct.adoc)

```bash
pct config 101
pct exec 101 -- df -h
pvesm status
```

**管理対象 rootfs またはマウントポイント**では、コンテナーまたはそのアプリケーションからファイルを削除し、ホストでバックエンドボリュームとスナップショットを調べます。**CT に VM 用 `qm` discard コマンドを実行しないでください。** ZFS サブボリュームではスナップショットが削除済みブロックを保持します。directory と thin-LVM ストレージでは、設定済み CT サイズではなく実際の割り当て量を確認します。

クリーンアップ後、バックエンドが discard に対応するときは**Proxmox ホストで `pct fstrim` を実行します。** Proxmox は CT の rootfs と対象となる管理マウントポイントを trim します。バインドマウントと読み取り専用マウントポイントはスキップします。`--ignore-mountpoints` を使うと rootfs だけを trim します。実行前後のバックエンド使用量を比べてください。[Proxmox `pct fstrim` リファレンス](https://github.com/proxmox/pve-docs/blob/master/generated/pct.1-synopsis.adoc)

```bash
pct fstrim 101
pct fstrim 101 --ignore-mountpoints 1
```

このコマンドは CT ID `101` を例に**異なる対象範囲**を示します。ストレージ構成に合わせ、どちらか一方を実行します。trim が成功しても、スナップショットが古いブロックを保持する場合は同じバイト数が解放されるとは限りません。

**バインドマウントとデバイスマウントは Proxmox の管理対象外です。** ソースデータはホストまたは外部デバイスに残ります。コンテナーの `vzdump` バックアップには内容が含まれません。ストレージ管理の追加マウントポイントも、`backup` オプションで指定しない限り既定でバックアップ対象外です。クリーンアップの前にマウントのバックアップポリシーを確認してください。[Proxmox バックアップのドキュメント](https://github.com/proxmox/pve-docs/blob/master/vzdump.adoc)

Docker をネストして使う場合は、Docker のクリーンアップコマンドを使う前に、実際のストレージ所有者内でイメージレイヤー、ボリューム、ログを調べます。[Docker on LXC の信頼性ガイド](/articles/docker-in-lxc-proxmox-reliability/)でマウントとバックアップの境界を説明しています。コンテナーイメージを削除しても、永続ボリュームは既定では削除されません。

## ホストの数値を正しく測る

**クリーンアップ前後で同じ測定値を記録します。** ストレージプールの空き容量が最終的な容量の指標です。ゲストごとの数値で、増加の原因となったゲストを特定します。

```bash
pvesm status
pvesm list local-lvm
qm config 100
pct config 101
```

**`pvesm list` は管理ボリュームと設定サイズを一覧表示します。** thin ストレージの割り当て済みバイト数は測定しません。**Directory ストレージ**では、正確なマウントパスと既知のイメージファイルを調べます。**Datacenter > Storage** と VM 設定に示されるパスに置き換えてください。

```bash
df -hT /var/lib/vz
du -h /var/lib/vz/images/100/vm-100-disk-0.qcow2
ls -lh /var/lib/vz/images/100/vm-100-disk-0.qcow2
```

**停止中の VM** では、ファイルを変更せずにイメージの仮想容量とホスト割り当てを比較します。

```bash
qemu-img info /var/lib/vz/images/100/vm-100-disk-0.qcow2
```

**LVM のシンプロビジョニング** では、プールのデータとメタデータの両方を監視します。

```bash
lvs -a -o lv_name,vg_name,lv_size,data_percent,metadata_percent,segtype
```

**ZFS** では、稼働中データセットのデータとスナップショット保持データを分けて確認します。

```bash
zpool list
zfs list -o name,used,available,referenced,usedbysnapshots -r POOL_OR_DATASET
zfs list -t snapshot -o name,used,referenced,written -r DATASET
```

**`usedbysnapshots`** はデータセットの全スナップショットが保持するブロックを報告します。スナップショットはブロックを共有するため、各スナップショットの `used` の値を合計できません。削除済みファイルのブロックを参照するすべてのスナップショットが保持ポリシーに従って期限切れまたは削除されるまで、プール使用量が変わらないことがあります。[OpenZFS のスナップショットとクローン](https://openzfs.github.io/openzfs-docs/Basic%20Concepts/Datasets/Snapshots%20and%20Clones.html)

**Ceph RBD** では Ceph コマンドの前に Proxmox ボリューム ID を対応付けます。**`qm config VMID`** は `STORAGE_ID:IMAGE` を示します。**Datacenter > Storage** の RBD エントリーで**プール**と任意の**名前空間**を確認します。ストレージ ID はプール名と同じとは限りません。プール値とイメージ値から `POOL/IMAGE` を組み立てます。対象の Ceph クラスター向けに設定済みで有効な認証情報を持つクライアントからコマンドを実行します。[Proxmox RBD ストレージのドキュメント](https://github.com/proxmox/pve-docs/blob/master/pve-storage-rbd.adoc)

```bash
ceph df
rbd du POOL/IMAGE
rbd snap ls POOL/IMAGE
```

**`rbd du`** は関連スナップショットを含め、プロビジョニング量と実使用量を報告します。イメージに `fast-diff` 機能がない場合、潜在オブジェクトを OSD に問い合わせるため、より多くの処理が必要です。**`ceph df`** はプールとクラスターの容量を示します。レプリケーション、イレージャーコーディング、スナップショットで、生のクラスター使用量とイメージのバイト数は異なります。[Ceph RBD コマンドリファレンス](https://docs.ceph.com/en/squid/man/8/rbd/)および[Ceph プール使用量のガイド](https://docs.ceph.com/en/squid/rados/operations/monitoring/)

RBD ストレージが名前空間を使う場合、各 `rbd` コマンドに **`--namespace NAMESPACE`** を追加します。Proxmox のストレージエントリーに設定した名前空間を使い、Proxmox のストレージ ID は使いません。

## スナップショットとバックアップを考慮する

**スナップショットは古いブロックのバージョンを保持します。** trim 後に使用量が減らない場合は、VM または CT の **Snapshots** タブとバックエンドのスナップショット一覧を確認します。削除前にスナップショットの所有関係と依存関係を調べてください。バックアップは別のコピーであり、ゲストの現在の `df` 結果ではなくバックアップストレージの保持ルールに従います。

**PBS の重複排除は計上方法を変えます。** データストアは複数バックアップ間で共有されるチャンクを保持します。prune はバックアップスナップショットのメタデータを削除します。その後のガベージコレクションで、猶予期間などの条件に従って参照されないチャンクを削除します。バックアップ領域を回収したと報告する前に、両方のタスクを確認します。[PBS メンテナンスのドキュメント](https://pbs.proxmox.com/docs/maintenance.html)

> **警告:** 名前から推測して Proxmox 管理下のボリュームファイル、zvol、スナップショットを削除しないでください。最初にゲストと保持ポリシーを特定します。ストレージクリーンアップでは、バックアップとロールバックの経路を保持してください。

## オフラインでイメージを再構築する

**通常のゲスト trim とバックエンド経路で qcow2 の割り当て問題を解決できない場合に限り、オフライン変換を使います。** VM をシャットダウンし、バックアップを確認し、すべてのスナップショットとバッキングチェーンの関係を特定して、別の宛先イメージに書き込みます。QEMU は、別のプロセスが使用中のイメージを変更しないよう警告しています。[QEMU `qemu-img` ドキュメント](https://www.qemu.org/docs/master/tools/qemu-img.html)

**スナップショットのあるディスクや管理対象ブロックストレージ上のディスクには、Proxmox 管理下の移動、またはバックアップと復元の手順を優先します。** PVE 所有イメージに対する単独の `qemu-img convert` では、VM 設定、ボリューム所有権、スナップショット参照は更新されません。削除済みファイルの領域回収に `qemu-img resize --shrink` を使わないでください。先にパーティションとファイルシステムを縮小しないと、ゲストから見える容量を減らしてデータを切り捨てる恐れがあります。

## 領域を回収できないとき

| 症状 | 確認する項目 | 次の対応 |
|---|---|---|
| **ゲストの `df` は減るがホストは変わらない** | VM discard フラグ、ゲスト trim、スナップショット | discard 経路全体と保持中のスナップショットを確認します。 |
| **`fstrim` が未対応と表示する** | ゲストのディスクバス、積層ブロックデバイス、バックエンド | `lsblk -D`、ゲストカーネル、途中の各層を調べます。 |
| **Windows ReTrim は完了するがホストは変わらない** | バックエンド割り当て、スナップショット、サーバーの計上 | ボリュームとプールの使用量を比較します。ディスクが thin ストレージを使うことを確認します。 |
| **`ls -lh` と `du -h` の値が異なる** | スパースまたは qcow2 ファイル | 割り当て済みファイルシステムブロックには `du` を使います。 |
| **LVM のシンプロビジョニング プールの使用率が高いまま** | データ、メタデータ、スナップショット | 削除前に `lvs` と PVE スナップショットを確認します。 |
| **ZFS プールの使用率が高いまま** | スナップショット保持ブロックと予約 | `usedbysnapshots`、zvol 設定、プール容量を調べます。 |
| **CT の `df` とプールが一致しない** | バインドマウント、マウントポイント、スナップショット | `rootfs` と各 `mpN` のホスト側所有者を対応付けます。 |

**バックグラウンド処理の完了後に再確認します。** trim、スナップショット削除、バックエンドのガベージコレクションでは、ストレージ計上が遅れる場合があります。プールの空き容量を開始時の値と比較します。ゲストコマンドの終了コードだけで成功と判断しないでください。

## 次の手順

**ゲストごとにストレージ記録を作成します:** 仮想サイズ、割り当て済みバイト数、バックエンド、バス、discard フラグ、スナップショット数、バックアップ範囲、プール空き容量です。VM を1台選び、対応 discard 経路を有効にし、ゲスト内で trim を実行して、記録した値を比較します。最初の結果がバックエンドの予想動作と一致してから次へ進みます。

復旧計画を広げる場合は、[Proxmox バックアップと復元のドリル](/articles/proxmox-vm-backup-restore-drill/)と[Proxmox VE 8 から 9 へのアップグレードガイド](/articles/proxmox-ve-8-to-9-upgrade-guide/)を参照してください。

## 参考資料

- [Proxmox VE ストレージ管理](https://github.com/proxmox/pve-docs/blob/master/pvesm.adoc)、ストレージ種別、シンプロビジョニング、容量リスク。
- [Proxmox VE LVM ストレージ](https://github.com/proxmox/pve-docs/blob/master/pve-storage-lvm.adoc)、VE 9 のスナップショットボリュームチェーンと割り当て。
- [Proxmox VE RBD ストレージ](https://github.com/proxmox/pve-docs/blob/master/pve-storage-rbd.adoc)、プールと名前空間の設定。
- [Proxmox VE 仮想マシン](https://github.com/proxmox/pve-docs/blob/master/qm.adoc)、ディスクバス、形式、discard、ゲストエージェント。
- [Proxmox VE VM ディスクオプション](https://github.com/proxmox/pve-docs/blob/master/generated/qm.conf.5-opts.adoc)、バス固有のフラグ。
- [Proxmox VE コンテナー](https://github.com/proxmox/pve-docs/blob/master/pct.adoc)、rootfs とマウントポイントの所有関係。
- [Proxmox VE コンテナーコマンド](https://github.com/proxmox/pve-docs/blob/master/generated/pct.1-synopsis.adoc)、ホスト側のコンテナー trim。
- [Proxmox VE バックアップと復元](https://github.com/proxmox/pve-docs/blob/master/vzdump.adoc)、VM と CT のバックアップ対象。
- [Microsoft の `Optimize-Volume` ドキュメント](https://learn.microsoft.com/en-us/powershell/module/storage/optimize-volume?view=windowsserver2025-ps)、Windows ReTrim の構文。
- [Red Hat の未使用ブロックのガイド](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/8/html/managing_file_systems/discarding-unused-blocks_managing-file-systems)、Linux `fstrim` の動作。
- [OpenZFS のスナップショットとクローン](https://openzfs.github.io/openzfs-docs/Basic%20Concepts/Datasets/Snapshots%20and%20Clones.html)、スナップショットが保持するブロック。
- [Ceph RBD コマンドリファレンス](https://docs.ceph.com/en/squid/man/8/rbd/)、イメージ使用量とスナップショット。
- [NFSv4.2 仕様](https://www.rfc-editor.org/rfc/rfc7862.html#section-6.2.2)、サーバー側の領域解放。
- [PBS メンテナンスのドキュメント](https://pbs.proxmox.com/docs/maintenance.html)、prune とガベージコレクション。
- [QEMU ディスクイメージユーティリティ](https://www.qemu.org/docs/master/tools/qemu-img.html)、オフラインイメージ変換の安全性。
