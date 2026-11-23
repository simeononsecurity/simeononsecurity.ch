---
title: "Proxmox VE 8から9へのアップグレードガイド"
date: 2026-07-22
lastmod: 2026-11-23
toc: true
draft: false
description: "Proxmox VE 8から9へアップグレードする手順を解説します。事前確認、手動手順、自動化、互換性に関わる変更、復旧方法を紹介します。"
genre: ["仮想化", "Linux管理", "Proxmox仮想化", "サーバー管理", "オープンソースソフトウェア", "ホームラボ"]
tags: ["Proxmox VE 9版", "Proxmoxのアップグレード", "PVE 8から9", "Debian Trixie", "Debian 13版", "apt dist-upgrade", "pve8to9", "Proxmox上のCeph", "proxmox-boot-tool", "grub-efi", "LVMのアップグレード", "ZFSのアップグレード", "NVIDIA vGPU", "cgroupv2", "Proxmoxの自動化", "Bashアップグレードスクリプト", "Proxmoxクラスターのアップグレード", "インプレースアップグレード", "pve8to9-upgrade.sh", "Proxmox VE 9.0版"]
cover: "/img/cover/proxmox-ve-8-to-9-upgrade-guide-automation.webp"
coverAlt: "仮想マシンを表すアイコンが画面に光る、現代的なサーバールーム。技術者がノートパソコンで作業し、濃紺の機器を青、緑、紫の鮮やかなアクセントが彩る。"
coverCaption: "Proxmox VE 8から9へのアップグレード。自動化アシスタントスクリプトを使ったインプレース更新の手順。"
canonical: "https://simeononsecurity.com/articles/proxmox-ve-8-to-9-upgrade-guide/"
---

**Proxmox VE 9.0はDebian 13 Trixie、カーネル6.14、QEMU 10、LXC 6、ZFS 2.3を採用してリリースされました。** このガイドでは、手動のインプレースアップグレードと、構成を検出してリポジトリ変更、既知の問題、事前確認を処理する自動化Bashスクリプトを説明します。

## Proxmox VE 9の新機能

Proxmox VE 9は2025年8月にリリースされたメジャーバージョンです。主な変更点は次のとおりです。

| コンポーネント | PVE 8 | PVE 9.0 |
|-----------|--------|--------|
| **Debianベース** | Bookworm (12) | Trixie (13) |
| **既定のカーネル** | 6.8 | 6.14 |
| **QEMU** | 9.x | 10.x |
| **LXC** | 5.x | 6.x |
| **ZFS** | 2.2 | 2.3 |
| **Ceph** | Quincy / Reef / Squid | Squid (19.2) |
| **cgroup** | cgroupv2 (v1も利用可能) | cgroupv2のみ |

[Proxmox VE 9.2版](https://forum.proxmox.com/threads/proxmox-virtual-environment-9-2-available.183742/)では、カーネル7.0、QEMU 11、LXC 7、ZFS 2.4が既定で提供されます。9.2ではCeph Tentacleが既定ですが、Squidも引き続き利用できます。VE 8のCephクラスターをアップグレードする前にSquidへ移行する必要がある点は、別途満たすべき前提条件です。

**PVE 9.0以降の主な新機能:**
- ボリュームチェーンを使ったシックプロビジョニングLVM上のVMスナップショット (技術プレビューから9.1で本番対応)
- HAグループに代わる高可用性アフィニティルール
- OpenFabricおよびOSPFのフルメッシュCephネットワーク向けSDN Fabrics
- 新しいモバイルWebインターフェイス (Rust/Yew)
- 停止時間なしでのZFS RAIDZデバイス拡張
- Cluster Resource Schedulerによる動的な負荷分散 (PVE 9.2)
- SDNファブリックのプロトコルとしてのWireGuardとBGP (PVE 9.2)
- `/tmp`が`tmpfs`としてマウントされる (Debian Trixieの変更。ファイルは定期的に削除)

{{< figure src="proxmox-ve-8-to-9-component-changes.webp" alt="Proxmox VE 8とVE 9の比較図。カーネル、QEMU、LXC、ZFS、Cephのバージョン変更を示す" >}}

______

## 開始前の前提条件

**リポジトリを変更する前に、以下の条件をすべて満たしてください。** 詳細な確認項目は[公式アップグレードWikiの前提条件](https://pve.proxmox.com/wiki/Upgrade_from_8_to_9#Prerequisites)を参照してください。

### 1. Proxmox VE 8.4以降が必要

```bash
pveversion
```

出力に`pve-manager/8.4.x`以降が表示される必要があります。満たさない場合:

```bash
apt update && apt dist-upgrade
```

### 2. CephはSquid (19.x) が必要、ハイパーコンバージド構成のみ

```bash
ceph --version
```

出力にバージョン19.x (Squid) が表示される必要があります。Reef (18.x) またはQuincy (17.x) の場合は、先にCephをアップグレードしてください。アップグレードは常に1段階ずつ行います。

- Quincy (17) → Reef (18) → Squid (19)

*すべてのCephノードがSquidになるまでPVE 9へのアップグレードを開始しないでください。*

### 3. Proxmox Backup Serverを同じノードにインストールしている場合

PBS 3.4とPVE 8.4を同じノードで実行している場合は、[同時インストール手順](https://pbs.proxmox.com/wiki/Upgrade_from_3_to_4#Installed_alongside_Proxmox_VE)に従い、1回のAPT操作で両方をアップグレードしてください。バックアップから復元できることを確認し、リポジトリ変更前に`pve8to9 --full`と`pbs3to4 --full`を実行します。報告された問題は続行前に解決してください。

### 4. アクセス要件

- **推奨**: IPMI、iKVM、または物理キーボードを使ったコンソールアクセス。サービスの再起動時にSSHセッションが切断されます。
- **SSH**: 接続が切れてもアップグレードを続けられるよう、`tmux`または`screen`を使います。
  ```bash
  tmux new -s upgrade
  ```

### 5. ディスク容量

```bash
df -h /
```

最低でも**5 GBの空き容量**が必要です。10 GB以上を推奨します。

### 6. 有効なバックアップ

続行前にすべてのVMとコンテナを外部ストレージへバックアップしてください。復元をテストします。有効なバックアップは必須です。

______

## 把握しておくべき互換性のない変更

アップグレード前に以下を確認してください。アップグレード前後に対応が必要な変更があります。

### cgroup V1は廃止

PVE 9は旧式のcgroupv1環境をサポートしません。以前に有効化していた場合:

```bash
grep -E 'cgroup_no_v1|systemd.unified_cgroup_hierarchy=0' /proc/cmdline
```

何かが返された場合は、`/etc/default/grub`からカーネルパラメーターを削除し、アップグレード前に`update-grub`を実行します。

**コンテナへの影響**: systemd 230以前 (CentOS 7、Ubuntu 16.04) を実行するコンテナはPVE 9で起動しません。PVE 9へ移行する前に、該当するワークロードを移動してください。Proxmox VE 8.4のベンダーサポートは2026年8月に終了しました。

### HAグループは非推奨

HAグループはHAルールに置き換わります。クラスター内の全ノードがPVE 9になると自動的に移行します。手動操作は不要ですが、最後のノードの更新後に確認してください。

### VM.Monitor権限は削除

`VM.Monitor`を参照するカスタムロールは更新が必要です。基本的なKVMモニターアクセスには`Sys.Audit`を使います。`pve8to9`スクリプトが該当するロールを検出します。

### 新しい権限: VM.Replicate

ストレージレプリケーションジョブの作成または編集には、`/vms/<vmid>`上の`VM.Replicate`が必要です。必要に応じてカスタムロールを調整してください。

### 特権LXCコンテナにはSys.Modifyが必要

新しい特権コンテナの作成には`Sys.Modify`が必要になりました。既存の特権コンテナを同じ場所に復元する場合は必要ありません。

### systemd-sysctlは/etc/sysctl.confを読み込まない

アップグレード後、`/etc/sysctl.conf`のカスタム設定は通知なしで無視されます。再起動前に`/etc/sysctl.d/<NN>-name.conf`へ移してください。

```bash
# sysctl.confの内容を確認
grep -v '^\s*#\|^\s*$' /etc/sysctl.conf
```

### /tmpはtmpfsに変更

Debian Trixieは`/tmp`をRAMの最大50%を使うtmpfsとしてマウントします。システム稼働中にファイルは定期的に削除されます。大きな一時ファイルを`/tmp`に置く場合は、`/var/tmp`または専用マウントへ移動してください。

### Veeamのバックアップと復元の互換性 {#veeam-backup-broken-for-qemu-machine-version--100}

アップグレード前に、[Veeam Backup & ReplicationとProxmoxプラグインのビルド](https://helpcenter.veeam.com/docs/vbr/userguide/pve_system_requirements.html)を確認してください。現行要件では、公式Proxmox ISOでインストールしたx86-64ホスト上のProxmox VE 8.2から9.2までが対象です。旧バージョンのVeeamにはそれぞれ別のサポート範囲があります。

現行の[Veeam制限事項](https://helpcenter.veeam.com/docs/vbr/userguide/pve_limitations.html)では、Snapshots as Volume Chains (SAVC) を有効にしたLVMベースのストレージからVMをバックアップできます。ただし、SAVCがVeeamワーカーのファイル保存先やInstant Recoveryの復旧先としてサポートされるわけではありません。[KB4773に記載された別の復元問題](https://www.veeam.com/kb4773)は、PVE 9上のSAVCストレージに復元したQCOW2ディスクを持つ、QEMUマシンタイプ10未満に影響します。SAVC以外の復旧先を選ぶか、ドキュメントの説明に従ってディスクをRAWとして復元してください。これは復元時の回避策であり、全環境でマシンタイプを固定する理由にはなりません。アップグレードに依存する前に、予定しているストレージでバックアップと復元をテストしてください。

### ネットワークインターフェイス名が変わる場合がある

カーネル6.14は6.8より多くのNIC機能を認識します。一部のNICでは、名前に追加の接尾辞が付きます。アップグレード前に`pve-network-interface-pinning`ツールを使い、すべてのインターフェイスを安定した`nicX`名に固定できます。

```bash
pve-network-interface-pinning --help
```

______

## オプションA: 手動でインプレースアップグレード

[Proxmox VEの公式アップグレード手順](https://pve.proxmox.com/wiki/Upgrade_from_8_to_9)に従います。

### 手順1: pve8to9のチェックリストを実行

```bash
pve8to9 --full
```

続行前にすべての`FAIL`項目を解決し、修正のたびに再実行します。

### 手順2: 実行中のVMを移行、クラスター内の場合

```bash
qm migrate <vmid> <target-node>
pct migrate <ctid> <target-node>
```

### 手順3: PVE 8を完全に更新

```bash
apt update && apt dist-upgrade
pveversion   # 8.4.1以降を表示すること
```

### 手順4: Debianのベースリポジトリを更新

```bash
sed -i 's/bookworm/trixie/g' /etc/apt/sources.list
sed -i 's/bookworm/trixie/g' /etc/apt/sources.list.d/pve-enterprise.list
```

残っているBookworm専用のリポジトリ行はコメントアウトするか削除します。

### 手順5: PVE 9のパッケージリポジトリを追加

**Enterprise (サブスクリプションが必要):**

```bash
cat > /etc/apt/sources.list.d/pve-enterprise.sources << EOF
Types: deb
URIs: https://enterprise.proxmox.com/debian/pve
Suites: trixie
Components: pve-enterprise
Signed-By: /usr/share/keyrings/proxmox-archive-keyring.gpg
EOF
```

**サブスクリプションなし:**

```bash
cat > /etc/apt/sources.list.d/proxmox.sources << EOF
Types: deb
URIs: http://download.proxmox.com/debian/pve
Suites: trixie
Components: pve-no-subscription
Signed-By: /usr/share/keyrings/proxmox-archive-keyring.gpg
EOF
```

`apt update && apt policy`を実行し、新しいリポジトリがエラーなく表示されることを確認します。その後、古い`.list`ファイルを削除するかコメントアウトします。

### 手順6: Cephリポジトリを更新、ハイパーコンバージド構成のみ

```bash
cat > /etc/apt/sources.list.d/ceph.sources << EOF
Types: deb
URIs: https://enterprise.proxmox.com/debian/ceph-squid
Suites: trixie
Components: enterprise
Signed-By: /usr/share/keyrings/proxmox-archive-keyring.gpg
EOF
```

サブスクリプションなしの構成では、`pve-no-subscription`と`http://download.proxmox.com/debian/ceph-squid`を使います。

### 手順7: パッケージインデックスを更新

```bash
apt update
```

エラーがないことを確認します。

### 手順8: dist-upgradeを実行

```bash
apt dist-upgrade
```

ストレージ速度によって5分から60分以上かかります。アップグレード中に表示された場合:

- **`/etc/issue`**: 現在のバージョンを維持 (安全)
- **`/etc/lvm/lvm.conf`**: パッケージ保守担当者のバージョンをインストール (推奨)
- **`/etc/ssh/sshd_config`**: カスタマイズしていなければ保守担当者のバージョンをインストール
- **`/etc/default/grub`**: カスタマイズしている場合は現在のバージョンを維持
- **`/etc/chrony/chrony.conf`**: カスタマイズしていなければ保守担当者のバージョンをインストール

### 手順9: 再起動

```bash
reboot
```

PVE 8でカーネル6.14をオプションとして導入済みでも、再起動は必要です。カーネルはPVE 9のツールチェーンで再構築されます。

### 手順10: アップグレード後の操作

```bash
# ブラウザーのキャッシュを消去: Ctrl+Shift+R (macOSでは⌘+Alt+R)
# クラスター内の全ノードを確認:
pvesh get /nodes

# 全ノードがPVE 9になると、HAグループはHAルールへ自動移行
journalctl -eu pve-ha-crm  # エラーを確認
```

______

## オプションB: 自動化スクリプト (pve8to9-upgrade.sh)

手動手順には構成によって変わる条件付きの操作が多数あります。`pve8to9-upgrade.sh`はそれらを自動化します。

**スクリプトの出典:** [スクリプトのGistリポジトリ](https://gist.github.com/simeononsecurity/ba3831f487c4e960f9e218c7da5c4b8d)

### スクリプトの処理内容

スクリプトは次のようなアップグレード処理全体を自動化します。

| 検出項目 | 処理 |
|-----------|--------|
| Enterpriseまたはサブスクリプションなしのリポジトリ | **現在有効な**リポジトリ種別を使い、契約なしのノードでEnterpriseを有効にしない |
| Cephのバージョン | QuincyまたはReefの場合は停止し、手順別のCephアップグレードガイドを表示 |
| Cephリポジトリの種類 | 現在のリポジトリ種別に合わせて`ceph.sources`を作成 |
| NVIDIA vGPUドライバー | 570未満 (GRID 18.3最小要件) の場合は停止 |
| NVIDIA GPUパススルー | 警告し、アップグレード後のテストを促す |
| CUDAリポジトリ | URI内の`debian12`を`debian13`へ更新 |
| systemd-bootメタパッケージ | dist-upgradeを中断するDebianバグ#1110177への対処として削除 |
| sysctl.confのカスタム設定 | `/etc/sysctl.d/99-pve8to9-migrated.conf`へ移行 |
| 再起動後のFRRデッドロック | 再起動前に`/etc/network/interfaces`を修正 |
| `systemd-journald-audit.socket` | アップグレード中のログ増加を防ぐため無効化 |
| UEFIとLVMに関するGRUB問題 | `grub-efi-amd64`をインストールし、`/root/`に復旧メモを作成 |
| サードパーティの`bookworm`リポジトリ | コメントアウトし、更新するよう通知 |
| `linux-image-amd64`の競合 | インストール済みなら削除 |
| LVMの自動有効化 | アップグレード前後に移行スクリプトを実行 |
| Proxmox Backup Server (Proxmoxのバックアップサーバー) | `pbs3to4 --full`を実行し、PBSリポジトリをTrixie向けに更新 |
| ZFSルート | 構成を検出して確認。特別な操作は不要 |

変更はすべて`/var/log/pve8to9-upgrade-<timestamp>.log`に記録されます。APTリポジトリのバックアップは`/root/pve8to9-apt-backups/`に保存されます。`/etc/apt/sources.list.d/`内に`.bak`としてコピーするとWeb UIに「invalid extension」（拡張子が無効）エラーが表示されるため、その方法は使いません。

### インストールと使用方法

```bash
# スクリプトをダウンロード
curl -fsSL https://gist.githubusercontent.com/simeononsecurity/ba3831f487c4e960f9e218c7da5c4b8d/raw/pve8to9-upgrade.sh \
  -o pve8to9-upgrade.sh

# 実行可能にする
chmod +x pve8to9-upgrade.sh

# 実行前に内容を確認 (rootで実行するスクリプトは必ず読む)
less pve8to9-upgrade.sh
```

**実行モード:**

```bash
# 完全な対話モード (推奨)
./pve8to9-upgrade.sh

# 安全で破壊的でない修正をすべて自動承認
./pve8to9-upgrade.sh --yes

# ドライラン: 適用せずにすべての変更を表示
./pve8to9-upgrade.sh --dry-run

# pve8to9 --fullの事前確認を省略 (非推奨)
./pve8to9-upgrade.sh --skip-preflight
```

*SSH経由で接続する場合は、`tmux`または`screen`内で実行してください。*

### スクリプトの出力例

続行を確認する前に、検出した構成の概要を表示します。

```
══════════════════════════════════════════
  SUMMARY of detected configuration
══════════════════════════════════════════

  PVE version      : pve-manager/8.4.3/...
  Debian           : bookworm
  Subscription     : true (status: Active)
  PVE repo type    : enterprise  (enterprise was active: true)
  Ceph             : YES (v19.2.3, enterprise repos)
  ZFS root         : false
  UEFI boot        : true
  LVM root         : true
  NVIDIA           : NO
  CUDA repos       : NO
  systemd-boot     : meta=true efi=true
  sysctl.conf      : custom=false (0 lines)
  cgroupv1         : false (must be false for PVE 9)
  FRR post-up      : false (broken pattern)
  LVM autoact.     : false
  PBS co-install   : NO
  3rd-party bookwm : none
```

### スクリプトが実行を停止する安全確認

次のいずれかに当てはまる場合、スクリプトは**続行を拒否します**。

- カーネルのコマンドラインでcgroup V1が明示的に有効
- CephがQuincy (17.x) またはReef (18.x) のまま。Cephのアップグレードに必要なコマンドを表示
- NVIDIA vGPUドライバーがバージョン570未満 (GRID 18.3)
- PVEのバージョンが8.4未満

停止条件ごとに、解決後に再確認するための正確なコマンドを表示します。

______

## 既知のアップグレード問題

### UEFIモードでGRUBがLVMから起動できない

**該当する構成**: ルートがLVM上にあり、UEFIモードで起動し、PVE 7.xからアップグレードしたシステム。

```bash
# 修正 (アップグレード後、稼働中のシステムで実行):
[ -d /sys/firmware/efi ] && apt install grub-efi-amd64
```

`pve8to9-upgrade.sh`はUEFIとLVMの組み合わせを検出して、このパッケージを自動でインストールします。`/root/GRUB-RECOVERY-CHEATSHEET.txt`にも復旧方法を記録します。

**ノードがすでに**`grub rescue>`や「disk 'lvmid/...' not found」（ディスクが見つからない）で停止している場合:

1. PVE ISOから起動し、Advanced → **Rescue Boot**を選択
2. または公式Wikiの[GRUB障害からLVMを復旧する手順](https://pve.proxmox.com/wiki/Recover_From_Grub_Failure#Recovering_from_grub_.22disk_not_found.22_error_when_booting_from_LVM)に従う

### systemd-bootメタパッケージがdist-upgradeを中断

systemd-bootメタパッケージはPVE 8.1～8.4のISOインストール時に自動導入されました。Trixieでは他のパッケージの更新時に動くフックが含まれ、ESPがマウントされていないと`dist-upgrade`が途中で停止する場合があります (Debianバグ#1110177)。

```bash
# dist-upgradeの前に削除
apt remove systemd-boot
# systemd-boot-efiとsystemd-boot-toolsは削除しない。これらは残す
```

`pve8to9-upgrade.sh`はこの状況を自動で処理し、理由も詳しく説明します。

### カーネル6.14ではPCIパススルーが動作しない場合がある

一部のユーザーから、PCIパススルーを使うVMがカーネル6.14で起動しないとの報告があります。該当する場合:

```bash
# 以前のカーネルを一時的に固定
proxmox-boot-tool kernel pin 6.8.12-4-pve
```

### Cephフルメッシュ構成で再起動時にデッドロックする

`/etc/network/interfaces`に次の行がある場合:

```
post-up /usr/bin/systemctl restart frr.service
```

次のように変更します。

```
post-up /usr/bin/systemctl is-active --quiet frr.service && /usr/bin/systemctl restart frr.service || true
```

再起動**前に**実行してください。スクリプトはこのパターンを自動検出して修正します。

### LVM thin poolの修復が必要

アップグレード後、一部のシステムで次のエラーが発生します。

```
Check of pool pve/data failed (status:64). Manual repair required!
```

修復コマンド:

```bash
lvconvert --repair pve/data
```

### NVIDIA vGPUドライバーの最小バージョン

アップグレード前に**ドライバー570.158.02**以上 (GRID 18.3) が必要です。それ以前のドライバーはカーネル6.xと互換性がありません。

```bash
nvidia-smi --query-gpu=driver_version --format=csv,noheader
```

______

## クラスターのアップグレード順序

ノードは一度に1台ずつアップグレードします。次のノードを開始する前に、各ノードが正常であることを確認します。

```bash
# 各ノードのアップグレード前にクラスターの状態を確認:
pvecm status
ceph -s   # Cephを導入している場合
```

**部分アップグレード中の移行ルール:**

- PVE 8からPVE 9へのVM/CT移行: 常に動作
- PVE 9からPVE 8へのVM/CT移行: 通常は非対応

全ノードがPVE 9になった後、HAグループはHAアフィニティルールに自動移行します。エラーを確認します。

```bash
journalctl -eu pve-ha-crm
```

______

## トラブルシューティング

### アップグレードが停止する、またはproxmox-veの削除メッセージが表示される

次の表示がある場合:

```
W: (pve-apt-hook) You are attempting to remove the meta-package 'proxmox-ve'!
```

Bookwormのリポジトリが残っているため、1つ以上のパッケージを更新できません。残存するBookwormの設定を探します。

```bash
grep -r 'bookworm' /etc/apt/sources.list /etc/apt/sources.list.d/
```

該当行をコメントアウトしてから実行します。

```bash
apt update && apt dist-upgrade
```

途中まで完了している場合:

```bash
apt -f install
```

### ZFSの更新後に起動できない

レガシーBIOS起動でZFSルートを使う場合は、[ZFS: Legacy-BootからProxmox Boot Toolへの切り替え](https://pve.proxmox.com/wiki/ZFS:_Switch_Legacy-Boot_to_Proxmox_Boot_Tool)を参照してください。ZFSシステムの起動はGRUBに直接任せず`proxmox-boot-tool`で管理します。そうすることでZFS機能の更新後も起動できます。

______

## アップグレード後のチェックリスト

各ノードの再起動後に確認します。

- [ ] ブラウザーのキャッシュを消去 (`Ctrl+Shift+R` / `⌘+Alt+R`)
- [ ] `pveversion`が9.xを表示
- [ ] `uname -r`が6.14.x以降を表示
- [ ] すべてのVMとCTが正常に起動
- [ ] Cephの状態: `ceph -s`がHEALTH_OKを表示
- [ ] UEFIとLVMを使う場合: `grubx64.efi`の更新日時が新しいことを確認
- [ ] NVIDIA GPUパススルーを使う場合: 本番以外のVMでテスト
- [ ] アップグレード中にコメントアウトしたサードパーティーリポジトリを更新
- [ ] `/etc/sysctl.conf`のカスタム設定を`/etc/sysctl.d/`へ移行

## アップグレード後の検証

更新後、リポジトリ設定、クラスターのクォーラム、ストレージ状態、ゲストの起動、バックアップ、ファイアウォールルール、管理アクセスを確認します。完了と判断する前にシステムログを確認してください。クラスターが対応している場合は、別ホストでゲストを1台復元してテストします。

バージョンに応じたコマンドは、最新の[Proxmox VE管理ガイド](https://pve.proxmox.com/pve-docs/)と[リリースノート](https://pve.proxmox.com/wiki/Roadmap)を参照してください。対象バージョンとバックアップの状態を確認せずに、古いリリースのコマンドをコピーしないでください。

## 参考資料

1. [公式: Proxmox VE 8から9へのアップグレード](https://pve.proxmox.com/wiki/Upgrade_from_8_to_9)
2. [公式: 8から9へのアップグレード、前提条件](https://pve.proxmox.com/wiki/Upgrade_from_8_to_9#Prerequisites)
3. [pve8to9-upgrade.sh自動化スクリプト](https://gist.github.com/simeononsecurity/ba3831f487c4e960f9e218c7da5c4b8d)
4. [Proxmox VE 9.0の既知の問題 (Roadmap)](https://pve.proxmox.com/wiki/Roadmap#9.0-known-issues)
5. [GRUB障害からの復旧、LVMの「disk not found」（ディスクが見つからない）エラー](https://pve.proxmox.com/wiki/Recover_From_Grub_Failure#Recovering_from_grub_.22disk_not_found.22_error_when_booting_from_LVM)
6. [ZFS: Legacy-BootからProxmox Boot Toolへの切り替え](https://pve.proxmox.com/wiki/ZFS:_Switch_Legacy-Boot_to_Proxmox_Boot_Tool)
7. [Ceph ReefからSquidへのアップグレードガイド](https://pve.proxmox.com/wiki/Ceph_Reef_to_Squid)
8. [Proxmoxネットワークインターフェイスの固定](https://pve.proxmox.com/pve-docs/chapter-sysadmin.html)
9. [Debian 13 Trixieリリースノート](https://www.debian.org/releases/trixie/releasenotes)
