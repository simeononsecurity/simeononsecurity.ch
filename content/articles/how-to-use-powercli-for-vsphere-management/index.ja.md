---
title: "vSphere 管理のための PowerCLI 活用ガイド"
date: 2023-08-02
lastmod: 2026-11-14
toc: true
draft: false
description: "PowerCLI を使って VMware vSphere を管理し、作業を自動化して生産性を高める方法を紹介します。"
genre: ["テクノロジー", "仮想化", "VMware", "IT 管理", "自動化", "コマンドラインインターフェース", "スクリプト", "システム管理", "クラウドコンピューティング", "データセンター管理"]
tags: ["PowerCLI", "VMware PowerCLI", "PowerCLI のインストール", "PowerCLI をインストール", "PowerCLI のダウンロード", "PowerCLI をダウンロード", "PowerCLI で vCenter に接続", "vSphere 管理", "仮想マシン管理", "ホスト管理", "自動化", "スクリプト", "仮想化", "vCenter Server", "ESXi ホスト", "データストア管理", "ネットワークアダプター管理", "仮想マシン作成", "仮想マシン削除", "仮想マシン設定", "ホストリソース管理", "CPU 割り当て", "メモリ割り当て", "ストレージ設定", "PowerCLI の例", "PowerCLI ドキュメント", "IT 管理", "システム管理", "クラウドコンピューティング"]
cover: "/img/cover/An_illustrated_cartoon_image_showcasing_a_pers.webp"
coverAlt: "PowerCLI コマンドを使って vSphere 環境の仮想マシンとホストを管理する人のイラスト。"
coverCaption: "PowerCLI で vSphere 管理を効率化"
---

## はじめに

**PowerCLI** は **VMware** が提供する**コマンドラインインターフェース（CLI）**ツールです。管理者はこれを使って **VMware vSphere 環境を管理、自動化**できます。初心者にも経験者にも役立つ豊富な **cmdlet** が、管理作業を簡素化し生産性を高めます。この記事では、PowerCLI のインストール、vCenter への接続、機能の活用方法を説明します。

______

## PowerCLI のインストール

まず、PowerCLI をコンピューターにインストールします。

1. VMware 公式サイトから PowerCLI インストーラーを**ダウンロード**します。リンクは [PowerCLI ドキュメント](https://code.vmware.com/web/dp/tool/vmware-powercli)にあります。OS に合ったバージョンを選んでください。
2. インストーラーを**実行**し、画面の指示に従います。インストール先やオプションを選択します。
3. 「Finish」をクリックして完了します。これで PowerCLI を利用できます。

______

## PowerCLI で vCenter に接続

インストール後、vCenter Server に接続すると、PowerCLI の cmdlet で仮想インフラを管理できます。

1. スタートメニューまたはデスクトップのショートカットから PowerCLI を起動します。
2. 次のコマンドを実行して vCenter に接続します。

```powershell
Connect-VIServer -Server <vCenter IP or hostname>
```

`<vCenter IP or hostname>` を vCenter Server の実際の IP アドレスまたはホスト名に置き換えます。

3. プロンプトが表示されたら、vCenter の管理に十分な権限を持つアカウントの認証情報を入力します。
4. **Get-VMHost** などの簡単なコマンドで接続を確認します。ESXi ホストの一覧が表示されれば接続成功です。

______

## PowerCLI による vSphere 管理

vCenter に接続したら、次のような一般的な作業を実行できます。

### 情報の取得

PowerCLI には vSphere 環境の情報を取得する cmdlet が用意されています。

- **Get-VM**：仮想マシンの情報を取得します。
- **Get-VMHost**：ESXi ホストの情報を取得します。
- **Get-Datastore**：データストアの情報を取得します。
- **Get-NetworkAdapter**：ネットワークアダプターの情報を取得します。

パラメーターを使うと、出力を絞り込み、形式を調整できます。

### タスクの自動化

PowerCLI の利点は、繰り返し作業を自動化できることです。数行のコードで複数のオブジェクトに複雑な処理を実行できます。

#### フォルダー内の全 VM のスナップショットを作成

```PowerShell
## 指定したホスト上のすべての仮想マシンを停止
Get-VMHost -Name "MyHost" | Get-VM | Stop-VM

## 指定したフォルダー内のすべての仮想マシンのスナップショットを作成
Get-Folder -Name "MyFolder" | Get-VM | New-Snapshot -Name "DailySnapshot" -Description "Daily Backup"
```

この PowerShell スクリプトは、特定のホスト上の全 VM を停止し、指定フォルダー内の VM のスナップショットを作成する方法を示します。

#### フォルダー内の全 VM を安全にシャットダウン

```PowerShell
## 停止対象の仮想マシンを含むフォルダーを取得
$folder = Get-Folder -Name "MyFolder"

## 指定したフォルダー内のすべての仮想マシンを取得
$vms = Get-VM -Location $folder

## すべての仮想マシンを正常にシャットダウン
foreach ($vm in $vms) {
    if ($vm.PowerState -eq "PoweredOn") {
        $vm | Shutdown-VMGuest -Confirm:$false
    }
}
```

このスクリプトは指定フォルダー内の VM を適切にシャットダウンします。まず `Get-Folder` でフォルダーを取得し、`Get-VM` で VM を列挙します。`foreach` で各 VM を調べ、電源状態が「PoweredOn」の場合は `Shutdown-VMGuest` で正常に停止します。`-Confirm:$false` は確認プロンプトを省略します。

この方法でフォルダー内の全 VM を順序よく停止できます。PowerCLI のスクリプト機能を使えば、要件に合わせた自動化ワークフローも作成できます。

### 仮想マシンとホストの管理

PowerCLI では、仮想マシンやホストに対して次の管理作業を行えます。

- **仮想マシンの作成と削除**：**`New-VM`** や **`Remove-VM`** を使います。**[コマンドレット New-VM](https://developer.vmware.com/docs/powercli/latest/vmware.vimautomation.core/commands/new-vm/#DefaultParameterSet)** では作成時に CPU、メモリ、ディスク、ネットワークを指定できます。
- **仮想マシン設定の変更**：CPU、メモリ、ディスク、ネットワークを変更します。**[コマンドレット Set-VM](https://developer.vmware.com/docs/powercli/latest/vmware.vimautomation.core/commands/set-vm/#DefaultSet)** では CPU とメモリの割り当てを変更できます。
- **ホストリソースの管理**：CPU、メモリ、ネットワーク、ストレージを管理します。**[コマンドレット Set-VMHost](https://vdc-repo.vmware.com/vmwb-repository/dcr-public/e7c1a32c-a3c6-4d7c-91bb-18a86a38daf7/12353298-ce6e-4d3f-bd8d-ab9f5ab044cc/doc/Set-VMHost.html)** でホストのネットワークやストレージ設定を変更できます。

これらは PowerCLI による vSphere 管理の一例です。豊富な cmdlet を使うと、さまざまな管理作業を自動化し簡素化できます。

## まとめ

**PowerCLI** は VMware vSphere 環境の管理と自動化に役立つツールです。多数の cmdlet が管理作業を簡素化し、生産性を高めます。インストールして vCenter に接続すれば、情報取得、タスク自動化、仮想マシンとホストの効率的な管理を行えます。

PowerCLI を試して、vSphere 管理を効率化しましょう。


## 参考資料
- [PowerCLI ドキュメント](https://code.vmware.com/web/dp/tool/vmware-powercli)
- [Connect-VIServer：VMware PowerCLI コマンドレット リファレンス](https://docs.vmware.com/en/VMware-PowerCLI/latest/VMware.VimAutomation.Core/Connect-VIServer.html)
- [Get-VM：VMware PowerCLI コマンドレット リファレンス](https://developer.vmware.com/docs/powercli/latest/vmware.vimautomation.core/commands/get-vm/#Default)
