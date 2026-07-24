---
title: "完全ガイド：Google PixelデバイスへのGrapheneOSのインストール"
draft: false
toc: true
date: 2023-05-21
lastmod: 2026-05-24
description: "Webインストーラーまたはコマンドライン（CLI）を使用して、プライバシーとセキュリティを強化したGrapheneOSをGoogle Pixelデバイスにインストールする方法を解説します。"
tags: ["GrapheneOS", "Google Pixel", "プライバシー", "セキュリティ", "Android", "モバイルデバイス", "オペレーティングシステム", "インストールガイド", "カスタムROM", "データ保護", "セキュアOS", "オープンソース", "fastboot", "ブートローダー", "検証済みブート", "Pixel 10", "Pixel 9"]
cover: "/img/cover/how-to-install-graphine-os.webp"
coverAlt: "USB-Cケーブルでコンピューターに接続されたGoogle Pixelスマートフォンをデータ転送とセキュリティを表すカラフルなグラフィック要素で囲んだ抽象的なデジタルイラスト。"
coverCaption: ""
---

**Google PixelデバイスへのGrapheneOSのインストール方法**

GrapheneOSはAndroidをベースとしたオープンソースのプライバシー重視のオペレーティングシステムです。優れたセキュリティ強化とプライバシー保護機能を提供しており、データのプライバシーとセキュリティを重視するすべての方にとって優れた選択肢です。対応するGoogle Pixelデバイスをお持ちで、GrapheneOSに移行したい場合、このガイドでは推奨される**Webインストーラー**方式と、従来の**コマンドライン（CLI）**方式の両方を解説します。

> **ヒント：** インストール中に問題が発生した場合は、[GrapheneOSの公式チャットチャンネル](https://grapheneos.org/contact#community)でサポートを求めてください。サポートを依頼する前に、まず自分でガイドに従い、詰まった箇所について質問するようにしてください。

## 前提条件

### ハードウェア・システム要件

- 少なくとも**2GBの空きメモリ**と**32GBの空きストレージ**を持つコンピューター。
- デバイスに同梱の**高品質なUSB-Cケーブル**（必要に応じてUSB-C〜USB-Aケーブルも可）。USBハブは避け、デスクトップの背面ポートまたはノートPCのポートに直接接続してください。
- 仮想マシンからのインストールはUSBパススルーが不安定なため**推奨しません**。

> GrapheneOSをインストールする前にPixelデバイスを最新の状態にアップデートしておくことをお勧めします。なお、GrapheneOSはインストールプロセスの初期に最新ファームウェアをフラッシュします。

### 公式サポートOS

#### Webインストーラー

- Windows 10 / Windows 11
- macOS Sonoma (14)、macOS Sequoia (15)、macOS Tahoe (26)
- Arch Linux
- Debian 12 (bookworm)、Debian 13 (trixie)
- Ubuntu 22.04 LTS、Ubuntu 24.04 LTS、Ubuntu 25.04
- Linux Mint 21（Ubuntu 22.04 LTSの手順に従う）、Linux Mint 22（Ubuntu 24.04 LTSの手順に従う）
- Linux Mint Debian Edition 6（Debian 12の手順に従う）
- ChromeOS
- GrapheneOS
- Play Protect認定を受けたAndroid 13、14、15、16

#### CLIメソッド

ChromeOS、GrapheneOS、Android（Webインストーラーのみ対応）を除く上記すべて。

サポートが終了した古いバージョンのプラットフォームも使用できますが、公式にはサポートされていません。**続行する前にOSが最新の状態であることを確認してください。**

### 公式サポートブラウザー（Webインストーラーのみ）

- **Chromium**（Ubuntu以外 — UbuntuのSnapパッケージはWebUSBが動作しない）
- **Vanadium**（GrapheneOS）
- **Google Chrome**
- **Microsoft Edge**
- **Brave**（Brave Shieldsを無効にして使用 — フィンガープリント対策でストレージ使用量を制限するため）

> - Androidでは、ブラウザーの**デスクトップモードを無効**にしてください。デスクトップモードはWebインストーラーがAndroidを検出してリブート後の再接続許可を要求するのを妨げます。8GB以上のRAMを搭載した大型タブレット（例：Pixel Tablet）ではデフォルトで有効になっています。
> - FlatpakおよびSnapのブラウザーバージョンはインストール中に問題を引き起こすため使用しないでください。
> - シークレット/プライベートブラウジングモードは**使用しないでください** — ダウンロードしたリリースの展開に必要なストレージ容量が制限されます。

### 対応デバイス

[公式サポートのPixelデバイス](https://grapheneos.org/faq#supported-devices)のいずれかが必要です。**キャリアバリアントは避けてください** — キャリア向けPixelは工場でゼロ以外のキャリアIDが書き込まれており、ブートローダーとキャリアのアンロックが無効になります。キャリア非専用（SIMフリー）デバイスを入手してください。

---

## OEMアンロックの有効化

作業を進める前に、OSの中からOEMアンロックを有効にする必要があります。

1. **設定 → デバイス情報（About phone/tablet）** に移動し、**ビルド番号** を開発者モードが有効になるまで繰り返しタップします。
2. **設定 → システム → 開発者向けオプション** に移動し、**OEMロック解除** をオンにします。一部のキャリア対応SKUでは、デバイスがキャリアロック端末として販売されていないことを確認するために、ストックOSがアクティブなインターネット接続を必要とします。

> **Pixel 6aに関する注意：** 工場出荷状態のOSバージョンではOEMアンロックが機能しません。OTA経由で**2022年6月**以降のリリースにアップデートし、その後工場出荷状態にリセットしてOEMアンロックの問題を修正してください。

---

## インストール方法1：Webインストーラー（推奨）

[GrapheneOS Webインストーラー](https://grapheneos.org/install/web)はほとんどのユーザーに推奨される方法です。ブラウザーで直接WebUSBを使用するため、ソフトウェアのインストールは不要です。

### ステップ1：fwupdのバグを回避する（Linuxのみ）

Linuxでは、`fwupd`がfastbootプロトコルを使用してデバイスに誤って接続し、インストーラーをブロックすることが知られています。デバイスを接続する前に停止させてください：

```bash
sudo systemctl stop fwupd.service
```

この設定は再起動後に持続しません。

### ステップ2：udevルールの設定（Linuxのみ）

Arch Linuxの場合：

```bash
sudo pacman -S android-udev
```

DebianおよびUbuntuの場合：

```bash
sudo apt install android-sdk-platform-tools-common
```

### ステップ3：ブートローダーインターフェースで起動

デバイスの起動中に**音量ダウン**ボタンを押し続けます（電源オフの状態から音量ダウンを押しながら電源を入れるか、再起動して押し続けてください）。デバイスに**赤い警告トライアングル**と**"Fastboot Mode"**の文字が表示される必要があります。電源ボタンを押して"Start"を選択しないでください。

### ステップ4：デバイスを接続する

USBでデバイスをコンピューターに接続します。Linuxでは、最初の接続前にudevルールを設定していなかった場合は、ケーブルを再接続してください。

> **Pixel Tablet：** USBで接続する前にスタンドから取り外してください。タブレットは両方を同時に使用できません。

> **Windows：** 現在のWindows 10/11にはPixel 4a（5G）以降向けの汎用fastbootドライバーが含まれています。古いPixelまたは古いWindowsの場合は、Windows Updateからドライバーをインストールしてください（「オプションの更新プログラムを表示」→「LeMobile Android Device」を探してください）。

### ステップ5：ブートローダーをアンロックする

[https://grapheneos.org/install/web](https://grapheneos.org/install/web) を開き、**Unlock the bootloader** ボタンをクリックします。デバイスで音量ボタンで選択を切り替え、電源ボタンで確認します。**これによりすべてのデータが消去されます。**

### ステップ6：ファクトリーイメージの取得とフラッシュ

1. **Download release** をクリックしてデバイス用のファクトリーイメージをダウンロードします。
2. **Flash factory images** をクリックし、完了するまで待ちます。自動的にファームウェアをフラッシュし、ブートローダーインターフェースに再起動し、OSをフラッシュします。**完了するまでデバイスを操作しないでください。**

### ステップ7：ブートローダーをロックする

フラッシュ後、Webインストーラーで **Lock the bootloader** をクリックします。デバイスで確認します。**これにより再度すべてのデータが消去されます** — ブートローダーをロックすると完全な検証済みブートが有効になります。

---

## インストール方法2：コマンドライン（CLI）

### ステップ1：ターミナルを開く

Windowsでは、**通常（非管理者）のPowerShell**ウィンドウを開きます。レガシーの`curl`エイリアスを削除します：

```powershell
Remove-Item Alias:Curl
```

### ステップ2：fastbootのインストール

fastbootのバージョン **≥ 35.0.1** が必要です。

**Arch Linux：**

```bash
sudo pacman -S android-tools
```

**Debian / Ubuntu** — パッケージが古くなっています。スタンドアロンリリースを使用してください：

```bash
# Debian / Ubuntu
sudo apt install libarchive-tools
curl -O https://dl.google.com/android/repository/platform-tools_r35.0.2-linux.zip
echo 'acfdcccb123a8718c46c46c059b2f621140194e5ec1ac9d81715be3d6ab6cd0a  platform-tools_r35.0.2-linux.zip' | sha256sum -c
bsdtar xvf platform-tools_r35.0.2-linux.zip
export PATH="$PWD/platform-tools:$PATH"
```

**macOS：**

```bash
curl -O https://dl.google.com/android/repository/platform-tools_r35.0.2-darwin.zip
echo 'SHA256 (platform-tools_r35.0.2-darwin.zip) = 1820078db90bf21628d257ff052528af1c61bb48f754b3555648f5652fa35d78' | shasum -c
tar xvf platform-tools_r35.0.2-darwin.zip
export PATH="$PWD/platform-tools:$PATH"
```

**Windows：**

```powershell
curl -O https://dl.google.com/android/repository/platform-tools_r35.0.2-win.zip
(Get-FileHash platform-tools_r35.0.2-win.zip).hash -eq "2975a3eac0b19182748d64195375ad056986561d994fffbdc64332a516300bb9"
tar xvf platform-tools_r35.0.2-win.zip
$env:Path = "$pwd\platform-tools;$env:Path"
```

バージョンを確認します：

```bash
fastboot --version
# 期待される出力: fastboot version 35.0.2-12147458
```

### ステップ3：udevルールの設定（Linuxのみ）

Arch Linux：

```bash
sudo pacman -S android-udev
```

Debian / Ubuntu：

```bash
sudo apt install android-sdk-platform-tools-common
```

### ステップ4：fwupdのバグを回避する（Linuxのみ）

```bash
sudo systemctl stop fwupd.service
```

### ステップ5：ブートローダーインターフェースで起動

デバイスに**"Fastboot Mode"**と赤い警告トライアングルが表示されるまで、起動時に**音量ダウン**を押し続けます。

### ステップ6：接続してブートローダーをアンロックする

USBで接続し、以下を実行します：

```bash
fastboot flashing unlock
```

デバイスで確認します（音量ボタンで選択、電源ボタンで確定）。**これによりすべてのデータが消去されます。**

### ステップ7：OpenSSHのインストール（イメージ検証用）

macOSとWindowsにはOpenSSHがデフォルトで含まれています。

Arch Linux：

```bash
sudo pacman -S openssh
```

Debian / Ubuntu：

```bash
sudo apt install openssh-client
```

### ステップ8：ファクトリーイメージのダウンロードと検証

署名キーをダウンロードします：

```bash
curl -O https://releases.grapheneos.org/allowed_signers
```

期待されるコンテンツ：

```
contact@grapheneos.org ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIIUg/m5CoP83b0rfSCzYSVA4cw4ir49io5GPoxbgxdJE
```

ファクトリーイメージをダウンロードします（`DEVICE_NAME`と`VERSION`を実際の値に置き換えてください）：

```bash
curl -O https://releases.grapheneos.org/DEVICE_NAME-install-VERSION.zip
curl -O https://releases.grapheneos.org/DEVICE_NAME-install-VERSION.zip.sig
```

署名を検証します（Linux / macOS）：

```bash
ssh-keygen -Y verify -f allowed_signers -I contact@grapheneos.org -n "factory images" \
  -s DEVICE_NAME-install-VERSION.zip.sig < DEVICE_NAME-install-VERSION.zip
```

Windows：

```powershell
cmd /c 'ssh-keygen -Y verify -f allowed_signers -I contact@grapheneos.org -n "factory images" -s DEVICE_NAME-install-VERSION.zip.sig < DEVICE_NAME-install-VERSION.zip'
```

期待される出力：

```
Good "factory images" signature for contact@grapheneos.org with ED25519 key SHA256:AhgHif0mei+9aNyKLfMZBh2yptHdw/aN7Tlh/j2eFwM
```

### ステップ9：ファクトリーイメージをフラッシュする

イメージを展開します：

```bash
# Linux
bsdtar xvf DEVICE_NAME-install-VERSION.zip

# macOS / Windows
tar xvf DEVICE_NAME-install-VERSION.zip
```

ディレクトリに移動してフラッシュスクリプトを実行します：

```bash
cd DEVICE_NAME-install-VERSION

# Linux / macOS
bash flash-all.sh

# Windows
./flash-all.bat
```

プロセスが完了するまで待ちます。ファームウェアのフラッシュ、ブートローダーの再起動、OSのフラッシュが自動的に処理されます。**完了するまでデバイスを操作しないでください。**

> **Linux tmpfsのトラブルシューティング：** `/tmp`に十分な空き容量がない場合は以下を使用してください：
> ```bash
> mkdir tmp && TMPDIR="$PWD/tmp" ./flash-all.sh
> ```

### ステップ10：ブートローダーをロックする

```bash
fastboot flashing lock
```

デバイスで確認します。**これにより再度すべてのデータが消去されます。** ロックにより完全な検証済みブートが有効になり、fastbootによるパーティションの変更が防止されます。

---

## インストール後の作業

### 起動

ブートローダーインターフェースでデフォルトの **Start** オプションが選択された状態で電源ボタンを押してGrapheneOSを起動します。

### OEMアンロックの無効化

初期設定時の最後の画面にOEMアンロックのトグルがあります（デフォルトでチェックあり — チェックを入れたままにすると**OEMアンロックが無効**になります）。これを推奨します。後で**開発者向けオプション**で変更できます。

### インストールの確認

GrapheneOSは検証済みブートとハードウェアアテステーションを活用しています。検証済みブートは起動時にSoCのフューズに書き込まれたキーに対してすべてのファームウェアとOSイメージを検証します。GrapheneOSは自身の検証済みブート公開鍵をセキュアエレメントにフラッシュします — 各起動時にこのキーがOSを検証します。

#### 検証済みブートキーハッシュ

代替OSが読み込まれると、デバイスはOS識別子（検証済みブートキーのsha256）と共に**黄色の通知**を表示します。第4世代・第5世代Pixelは最初の32ビットのみ表示します。**第6世代以降のPixelはフルハッシュを表示します**。公式ハッシュと照合してください：

| デバイス | 検証済みブートキーハッシュ |
|----------|--------------------------|
| Pixel 10a | `d8f879d10419eddc9fcda6280718be763f6bf12299e1f72df3ea8ad8a8eb7f80` |
| Pixel 10 Pro Fold | `55a2d44103e56d5ec65496399c417987ba77730e6488fc60ba058d09fc3caee3` |
| Pixel 10 Pro XL | `141d7fc32af7958a416f2661b37cf6f27bfb376fb5ce616aeaa27a82c7a04f74` |
| Pixel 10 Pro | `4e8ee8f717754052198ca6d2d3aaa232e2461b4293c0d6f297e519cc778de093` |
| Pixel 10 | `3f7415ea26f5df5b14ea6d153256071a7a1af9ce7b0970b7311cc463c7ea02c7` |
| Pixel 9a | `0508de44ee00bfb49ece32c418af1896391abde0f05b64f41bc9a2dfb589445b` |
| Pixel 9 Pro Fold | `af4d2c6e62be0fec54f0271b9776ff061dd8392d9f51cf6ab1551d346679e24c` |
| Pixel 9 Pro XL | `55d3c2323db91bb91f20d38d015e85112d038f6b6b5738fe352c1a80dba57023` |
| Pixel 9 Pro | `f729cab861da1b83fdfab402fc9480758f2ae78ee0b61c1f2137dd1ab7076e86` |
| Pixel 9 | `9e6a8f3e0d761a780179f93acd5721ba1ab7c8c537c7761073c0a754b0e932de` |
| Pixel 8a | `096b8bd6d44527a24ac1564b308839f67e78202185cbff9cfdcb10e63250bc5e` |
| Pixel 8 Pro | `896db2d09d84e1d6bb747002b8a114950b946e5825772a9d48ba7eb01d118c1c` |
| Pixel 8 | `cd7479653aa88208f9f03034810ef9b7b0af8a9d41e2000e458ac403a2acb233` |
| Pixel Fold | `ee0c9dfef6f55a878538b0dbf7e78e3bc3f1a13c8c44839b095fe26dd5fe2842` |
| Pixel Tablet | `94df136e6c6aa08dc26580af46f36419b5f9baf46039db076f5295b91aaff230` |
| Pixel 7a | `508d75dea10c5cbc3e7632260fc0b59f6055a8a49dd84e693b6d8899edbb01e4` |
| Pixel 7 Pro | `bc1c0dd95664604382bb888412026422742eb333071ea0b2d19036217d49182f` |
| Pixel 7 | `3efe5392be3ac38afb894d13de639e521675e62571a8a9b3ef9fc8c44fd17fa1` |
| Pixel 6a | `08c860350a9600692d10c8512f7b8e80707757468e8fbfeea2a870c0a83d6031` |
| Pixel 6 Pro | `439b76524d94c40652ce1bf0d8243773c634d2f99ba3160d8d02aa5e29ff925c` |
| Pixel 6 | `f0a890375d1405e62ebfd87e8d3f475f948ef031bbf9ddd516d5f600a23677e8` |

#### Auditorアプリによるハードウェアベースのアテステーション

GrapheneOSは[Auditorアプリ](https://attestation.app/)を提供しており、検証済みブートとリモートアテステーションを使用してハードウェア、ファームウェア、OSの整合性を確認できます。結果は検証対象のデバイスではなく、Auditorを実行している別のAndroidデバイスに表示されます。または[オプションのデバイス整合性モニタリングサービス](https://attestation.app/)を使用してメールアラート付きで自動スケジュール検証を行うこともできます。

---

## GrapheneOSをストックOSに戻す

Googleの[Webフラッシュツール](https://flash.android.com/)を使用したストックOSのインストールは上記のプロセスと同様です。ただし、フラッシュとロックの前に、ストックに完全に戻すためにGrapheneOSの検証済みブートキーを消去する必要があります：

**Webインストーラー：** GrapheneOSのWebインストーラーの "Erase non-stock key" ボタンを使用します。

**CLI：**

```bash
fastboot erase avb_custom_key
```

その後、ストックOSのファクトリーイメージをフラッシュしてブートローダーをロックします。

---

## まとめ

Google PixelデバイスにGrapheneOSをインストールすると、業界最高水準のプライバシーとセキュリティ機能が利用できます。最も簡単な方法として [grapheneos.org/install/web](https://grapheneos.org/install/web) の**Webインストーラー**を使用するか、上記のCLI手順で従来の方法で行ってください。フラッシュ後は必ずブートローダーをロックして完全な検証済みブートを有効にし、必要に応じてAuditorアプリでインストールの整合性を確認してください。

## 参考文献

1. [GrapheneOS Webサイト](https://grapheneos.org/)
2. [GrapheneOS Webインストーラー](https://grapheneos.org/install/web)
3. [GrapheneOS CLIインストールガイド](https://grapheneos.org/install/cli)
4. [GrapheneOSリリース](https://grapheneos.org/releases)
5. [GrapheneOS使用ガイド](https://grapheneos.org/usage)
6. [GrapheneOS FAQ](https://grapheneos.org/faq)
7. [Auditorアプリ](https://attestation.app/)
8. [Android Platform Tools](https://developer.android.com/studio/releases/platform-tools)
