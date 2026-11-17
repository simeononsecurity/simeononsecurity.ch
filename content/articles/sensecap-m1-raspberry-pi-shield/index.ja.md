---
title: "SenseCAP M1 Raspberry Pi Shield: ピン配置とLoRaWANでの再利用"
date: 2026-09-12
lastmod: 2026-11-07
toc: true
draft: false
description: "SenseCAP M1シールドの構成、異なるGPIOマップ、ATECC608を確認し、新しいRaspberry Pi OSでLoRaWANゲートウェイを計画します。"
genre: ["Raspberry Pi", "IoT", "ハードウェアセキュリティ"]
tags: ["SenseCAP M1", "SenseCAP M1シールド", "SenseCAP M1ピン配置", "Raspberry Piシールド", "Raspberry Pi HAT", "LoRaWANゲートウェイ", "WM1302", "WM1303", "SX1302", "SX1303", "Seeed Studio", "Heliumホットスポット再利用", "LoRaコンセントレーター", "SPI GPIO", "GPIO17", "GPIO22 LED", "libgpiod", "Raspberry Pi OS", "ATECC608", "CryptoAuthLib", "I2C診断", "STTS751", "LoRa Basics Station", "ChirpStack", "The Things Stack", "ハードウェアリバースエンジニアリング"]
cover: "/img/cover/sensecap-wm1302-shield-hardware.webp"
coverAlt: "Seeed WM1302モジュール、Raspberry Piヘッダー、アンテナケーブル、USB-Cソケット、ファンコネクターを備えたSenseCAP M1シールド"
coverCaption: "基板写真: Clockwork Bird、2023年。出典とクレジットは記事末尾に記載しています。"
coverCredit: "Clockwork Bird"
coverCreditURL: "https://clockworkbird9.wordpress.com/2023/05/03/sensecap-m1-raspberry-pi-shield/"
---

**SenseCAP M1シールドはLoRaWANゲートウェイのハードウェアとして役立ちますが、配線は一般的なRaspberry Pi HATの説明より慎重に確認する必要があります。** このガイドでは、[Clockwork Birdによる2023年の調査](https://clockworkbird9.wordpress.com/2023/05/03/sensecap-m1-raspberry-pi-shield/)に、メーカー資料、上流ドライバーの確認、現在のGPIOガイダンスを加えています。ハードウェアを特定し、確かな事実と不完全なピン配置の情報を区別し、再現可能な導入記録を作成します。

> **対象範囲:** これは資料に基づくハードウェアガイドです。この記事のコマンドと基板マッピングは、実機のM1でテストしていません。

## 要点

- **両方の基板を特定する:** M1キャリアと取り外し可能なコンセントレーターには、それぞれ別のモデル情報とリビジョン情報があります。
- **リセットスクリプトを監査する:** CoreCellの既定値は、公開されているM1のピン配置図の信号と競合します。
- **OSのインターフェースを確認する:** SPIデバイスファイル、GPIO番号、GPIOツールのバージョンは、それぞれ異なる情報を示します。
- **セキュアエレメントのプロビジョニングを維持する:** デバイス情報の読み取りと、設定や鍵の生成は別の操作です。
- **経路全体を検証する:** コンセントレーターの検出だけでは、センサーデータの配信を確認できません。

## 作業前の準備

**難易度: 中級。** 在庫確認、OS準備、資料の確認に約1〜2時間を見込みます。電気的な検証、ドライバーの調整、ネットワークサーバーの導入には別途作業が必要です。特に、基板リビジョンが不明な場合は時間を確保してください。

| 項目 | 目的 |
|---|---|
| **M1シールドとコンセントレーター** | キャリアのリビジョンとモジュール全体のラベルを確認する |
| **Raspberry Pi 4** | 元のM1設計で使われたホストから始める |
| **予備のmicroSDカード** | 元のインストールを残したまま別のOSを準備する |
| **適切な電源とアンテナ** | 組み立てたハードウェアとモジュールのRF帯域に合わせる |
| **SSHまたはローカルコンソール** | 診断結果を記録し、設定を編集する |
| **LoRaWANセンサーとサーバー** | ハードウェアの導入後にアプリケーションへの実配信を確認する |
| **テスターとハードウェアの知識** | 未記載の接続を駆動する前に解決する |

電源を切った状態で、取り外す前に組み立てた機器の両面を撮影します。コネクターの向き、ねじ、スペーサー、アンテナの経路を記録します。交換後のインストールが受け入れ条件を満たすまで、元のカードと設定を使える状態にしておきます。

## 3つの層を特定する

**完成したM1、キャリアシールド、コンセントレーターは別々の部品です。** Seeedの資料では、完成したホットスポットにRaspberry Pi 4と、WM1302/SX1302またはWM1303/SX1303のコンセントレーターを組み合わせています。「SenseCAP M1シールド」という製品名だけでは、どちらの部品が付属するか分かりません。[Seeed StudioのM1概要](https://www.sensecapmx.com/docs/sensecap-m1/overview/)

**キャリア**はPiとモジュールの間で電源と周辺信号を接続します。**コンセントレーター**は無線の送受信を処理します。ホスト上の**パケットフォワーダー**は、受信した無線パケットと予定されたダウンリンクをサーバーと交換します。[SemtechのSX1302 HAL概要](https://github.com/Lora-net/sx1302_hal)

具体例として、棚の温度センサーが無線でアップリンクを送ります。コンセントレーターが受信し、ホストが転送し、ネットワークとアプリケーションのサービスが処理します。Linuxが起動したことから分かるのは、この経路のホスト部分だけです。

Clockwork Birdの写真は、`WM1302-SPI-EU868`と明記されたモジュールを搭載したM1 v1.1キャリアを示しています。写真を参考に、自分の機器のラベル位置を確認してください。写真に写ったシリアル番号は撮影対象の識別情報です。別のゲートウェイの設定値として使わないでください。

{{< figure src="m1-carrier-wm1302-board.webp" alt="USB-C、ボタン、ファン端子、アンテナケーブルの横にラベル付きWM1302 SPI EU868モジュールを搭載した緑色のM1キャリア" caption="Clockwork Birdが撮影したM1 v1.1。この記事のカバーにも使用" credit="Clockwork Bird" attr="Clockwork Bird, 2023-05-03" attrlink="https://clockworkbird9.wordpress.com/2023/05/03/sensecap-m1-raspberry-pi-shield/" >}}

## 電源と無線の接続

**M1のUSB-Cコネクターは電源入力として扱います。** メーカーはゲートウェイ全体にDC 5 V、3 Aを指定し、USB-Cを電源インターフェースとしています。「充電ポート」と呼ぶと、仕様にないバッテリー機能があるように誤解されます。[SenseCAP M1の仕様](https://www.sensecapmx.com/docs/sensecap-m1/overview/)

メーカーのブロック図では、5 V電源とモジュール用の安定化3.3 Vレールを分けています。トラブルシューティングではこの違いが重要です。Piが動作していても、コンセントレーターに電源がない場合があります。信号ピンに5 Vを入力したり、2つの電源入力が互いに絶縁されていると仮定したりしないでください。

**SPIモデルとUSBモデルでは、ホストへの接続が異なります。** SeeedのWM1302資料では、SPIモデルは直接SPIに接続し、USBモデルはSTM32L4 USBブリッジを使います。mini-PCIe形状が示すのはモジュールのフォームファクターです。資料に記載された電気インターフェースはSPIまたはUSBです。形状が合うノートPC用ソケットだけでは互換性を確認できません。[SeeedのWM1302資料](https://github.com/seeed-lora/WM1302-doc)

組み立てに電源を入れる前に、モジュールを電源から切り離した状態で装着し、適切なアンテナを接続します。RFハードウェア、アンテナ、使用する地域の周波数プランを一致させてください。設定ファイル名を変更してもモジュールのRF部品は変わりません。また、M1の電源ソケットからUSBコンセントレーターへの対応は確認できません。

{{< figure src="m1-power-spi-system-diagram.webp" alt="電源、SPI、GPIO、I2CバスでRaspberry Pi 4とM1シールドを接続するブロック図" caption="Clockwork Birdの元記事に掲載されたSenseCAPメーカー図。WM1302設計を示す" credit="Seeed Studio / SenseCAP, via Clockwork Bird" attr="Seeed Studio / SenseCAP, via Clockwork Bird" attrlink="https://www.sensecapmx.com/docs/sensecap-m1/overview/" >}}

## ピン配置を慎重に読む

**BCM GPIO番号と物理ヘッダーピン番号を、記録では別々の列にします。** たとえばBCM GPIO17はPiヘッダーの物理ピン11です。モジュールのエッジコネクターには3つ目の番号体系があるため、そのリセットピン番号はRaspberry PiのGPIO番号ではありません。

次の表は、Clockwork Birdの注釈付きヘッダー画像にある接続を転記したものです。**コミュニティによる参考資料**であり、メーカー発行の完全な回路図でも、すべてのM1リビジョンを測定した結果でもありません。また、図には`SX1262`のラベルがありますが、Semtechの汎用リセットスクリプトは`SX1261`の名称を使用します。

| 図中の信号 | BCM / 物理ピン | 解釈 |
|---|---|---|
| **I2C SDA / SCL** | GPIO2 / 3、GPIO3 / 5 | 共有管理バス |
| **SX1302 reset** | GPIO17 / 11 | コンセントレーターのリセット候補 |
| **User LED** | GPIO22 / 15 | M1の注釈 |
| **SPI MOSI / MISO** | GPIO10 / 19、GPIO9 / 21 | SPIデータ信号 |
| **SPI clock** | GPIO11 / 23 | SPIクロック信号 |
| **SX1302 chip select** | GPIO8 / 24 | SPI0 CE0 |
| **SX1262 reset** | GPIO5 / 29 | 補助無線リセット候補 |
| **SX1262 chip select** | GPIO6 / 31 | GPIO6。SPI0 CE1とは別 |
| **SX1262 BUSY** | GPIO18 / 12 | 補助無線の状態出力 |
| **SX1262 IO1 / IO2** | GPIO23 / 16、GPIO24 / 18 | 補助信号。使用前に確認 |

取り消し線のあるGPS/UART注釈は、GPS搭載のM1を示すものではありません。実機にGPSがある場合を除き、GPS固有の設定を追加しないでください。公開図ではユーザーボタンとファン制御も未解決です。[Clockwork Birdによるピン配置調査](https://clockworkbird9.wordpress.com/2023/05/03/sensecap-m1-raspberry-pi-shield/)

{{< figure src="m1-community-header-pinout.webp" alt="M1のLED、コンセントレーターのリセット、SPI信号、取り消し線付きGPS接続を示すRaspberry Piヘッダー図" caption="未解決の基板リビジョン範囲を含むコミュニティ注釈付き資料。M1の完全な回路図ではない" credit="Clockwork Bird" attr="Clockwork Bird, 2023-05-03" attrlink="https://clockworkbird9.wordpress.com/2023/05/03/sensecap-m1-raspberry-pi-shield/" >}}

## リセットスクリプトの競合を解決する

**リセットスクリプトは電気的な出力を選択します。単なるソフトウェア設定ではありません。** Semtechの上流`reset_lgw.sh`はCoreCellリファレンス設計を対象とします。既定値には、コンセントレーターのリセット用GPIO23、電源有効化用GPIO18、補助リセット用GPIO22、AD5338Rリセット用GPIO13が含まれます。[Semtechのリセットスクリプト](https://github.com/Lora-net/sx1302_hal/blob/master/tools/reset_lgw.sh)

Seeedの古いセットアップ手順では、2つのリセット割り当てをGPIO17とGPIO5に変更しますが、他のリファレンス設計の項目は残します。例に従う前に、これらの値をM1の注釈付き画像と比較してください。[Seeed WM1302セットアップ手順](https://github.com/seeed-lora/WM1302-doc)

| 割り当て | 競合する情報 | 必要な判断 |
|---|---|---|
| **GPIO22を補助リセットに使用** | M1の図ではユーザーLEDと表示 | LEDを有効にする前にこの仮定を外す |
| **GPIO18を電源有効化に使用** | M1の図では補助BUSYと表示 | 駆動する前にネットと方向を確認 |
| **GPIO13をDACリセットに使用** | 汎用スクリプトは別のリファレンス設計を示す | 回路の有無を確認 |
| **補助SPIデバイス** | M1の図はCE1ではなくGPIO6を選択 | チップセレクトの配線とドライバー対応を確認 |

**推論:** 図のとおりGPIO18が補助無線の出力につながる場合、Pi側を出力にすると電気的な競合が起きるおそれがあります。情報の不一致は検証の必要性を示します。損傷の発生や、すべてのM1で共通する配線を証明するものではありません。

すべての電源を切り、ヘッダーとモジュールコネクターの間で確認可能な接続を追跡します。基板リビジョンと両端を記録してください。導通結果で分かるのは接続です。信号の方向と電気的な限界は部品資料で確認します。

以下のメーカーのモジュール図を使い、エッジコネクターのピンとPiヘッダーのピンを混同しないようにします。補助無線のラベルは公開されたモジュールのリファレンスを示します。各リビジョンで同じチップや機能が使われることを示すものではありません。[Seeed WM1302モジュールのピン配置](https://github.com/seeed-lora/WM1302-doc/blob/master/pinout.jpg)

{{< figure src="wm1302-module-edge-connector.webp" alt="WM1302モジュールのエッジコネクター両面に電源、SPI、I2C、補助無線信号を示すSeeedの図" caption="モジュールのエッジコネクター番号はRaspberry Piヘッダーの番号と異なる" credit="Seeed Studio" attr="Seeed Studio, WM1302-doc" attrlink="https://github.com/seeed-lora/WM1302-doc" >}}

## Raspberry Pi OSを準備する

予備のインストール環境でホスト情報を記録します。

```bash
cat /etc/os-release
uname -r
tr -d '\0' < /proc/device-tree/model
```

OSリリース、カーネル、Piモデルは再現性を確認する出発点です。古いチュートリアルと結果を比べる前に記録します。

確認用とビルド用のツールをインストールします。

```bash
sudo apt update
sudo apt install git build-essential i2c-tools gpiod
sudo raspi-config
```

**Interface Options**でSPIとI2Cを有効にし、再起動します。SPIはコンセントレーターの経路に、I2Cは後述する管理デバイスに使います。別のHAT向けチュートリアルから、関係のないGPSシリアルポート変更を取り込まないでください。

公開されているインターフェースを確認します。

```bash
ls -l /dev/spidev* /dev/i2c-*
i2cdetect -l
gpiodetect
gpioinfo
gpioset --version
```

これらのコマンドは、デバイスノード、アダプター、GPIOコントローラー、ライン情報、インストール済みGPIOツールのバージョンを表示します。**`i2cdetect -l`はアドレスをスキャンせずにアダプターを一覧表示します。** `/dev/spidev0.0`ファイルがあることから分かるのはSPIインターフェースが公開されていることです。動作するコンセントレーターとの通信は確認できません。[i2c-toolsマニュアル](https://kernel.googlesource.com/pub/scm/utils/i2c-tools/i2c-tools/+/refs/tags/v4.3/tools/i2cdetect.8)、[Raspberry Pi GPIOガイダンス](https://pip-assets.raspberrypi.com/categories/685-app-notes-guides-whitepapers/documents/RP-006553-WP/A-history-of-GPIO-usage-on-Raspberry-Pi-devices-and-current-best-practices)

### GPIOのバージョンを考慮する

**別のマシンのグローバルGPIO番号をコピーしないでください。** 古いスクリプトは`/sys/class/gpio`を使いますが、カーネルの文書では非推奨のインターフェースです。新しいユーザー空間の統合では、正しいコントローラーとラインオフセットでGPIOキャラクターデバイスのインターフェースを使います。[Linux GPIOの文書](https://www.kernel.org/doc/html/next/admin-guide/gpio/sysfs.html)

スクリプトを調整する前に`gpioset --help`も確認します。バージョン1と2では構文とプロセスの動作が異なります。現在のツールは要求したラインを既定で保持しますが、プロセス終了後の状態は移植可能な仕様で保証されていません。[libgpiod gpiosetの文書](https://libgpiod.readthedocs.io/en/master/gpioset.html)

Raspberry Piはカーネルの出力保持動作を文書化し、変更する方法も示しています。すべてのLinuxシステムが同じように動作すると仮定せず、実際のカーネル設定を記録します。番号体系やGPIOツールを更新しても、誤った電気的マッピングは解決しません。[Raspberry Pi GPIO使用ガイド](https://pip-assets.raspberrypi.com/categories/685-app-notes-guides-whitepapers/documents/RP-006553-WP/A-history-of-GPIO-usage-on-Raspberry-Pi-devices-and-current-best-practices)

## ユーザーLEDをテストする

GPIO22がLEDにつながることを確認し、競合するGPIO利用者を取り除いてから、起動設定を編集します。

```bash
sudoedit /boot/firmware/config.txt
```

新しいRaspberry Pi OSでは、起動設定は**`/boot/firmware/config.txt`**にあります。古いイメージでは、2023年の記事に記載された`/boot/config.txt`を使います。編集前に有効なファイルをバックアップしてください。[Raspberry Pi config.txtの文書](https://www.raspberrypi.com/documentation/computers/config_txt.html)

Piに適用されるセクション、たとえば`[all]`の下にLEDオーバーレイを追加します。

```ini
dtoverlay=gpio-led,gpio=22,label=lorawan,trigger=heartbeat
```

**`gpio`**パラメーターはBCM番号を使います。**`label`**はLinux LEDデバイスの名前を指定します。**`trigger=heartbeat`**はカーネルのheartbeatトリガーを割り当てます。Clockwork BirdはM1でこの割り当てを報告し、Raspberry Piのオーバーレイ資料もパラメーターを説明しています。[元のLED観察](https://clockworkbird9.wordpress.com/2023/05/03/sensecap-m1-raspberry-pi-shield/)、[gpio-ledオーバーレイ資料](https://github.com/raspberrypi/linux/blob/rpi-6.12.y/arch/arm/boot/dts/overlays/README)

再起動後、登録されたLEDを確認します。

```bash
ls -l /sys/class/leds/
cat /sys/class/leds/lorawan/trigger
```

期待する結果は、`heartbeat`が角括弧付きで選択された`lorawan` LEDです。LEDの点滅から分かるのはGPIOとドライバーの経路が動作することです。LoRaWANへの登録、無線受信、Heliumの状態は分かりません。

## I2Cデバイスを調べる

**I2Cアドレスは手がかりであり、デバイスの識別情報ではありません。** Clockwork Birdは`0x60`と`0x39`の応答を観察し、暗号ライブラリを使ってATECC608の情報を読み取りました。温度センサーの特定は元記事でも仮説の段階でした。

前のセクションのアダプター一覧から始めます。広範囲の`i2cdetect`スキャンは受動的な観察ではなく、プローブ用のトランザクションを送信します。上流マニュアルは中断の可能性を警告しています。稼働中のゲートウェイや未知の接続機器を日常的にスキャンしないでください。[i2c-toolsのプローブ動作](https://kernel.googlesource.com/pub/scm/utils/i2c-tools/i2c-tools/+/refs/tags/v4.3/tools/i2cdetect.8)

| 観察結果 | 判断できること | 未解決の問い |
|---|---|---|
| **`0x60`から応答** | 何かがプローブに応答した | 期待するセキュアエレメントか |
| **`0x39`から応答** | 何かがプローブに応答した | どの部品とリビジョンが応答したか |
| **スキャンで`UU`** | ドライバーがアドレスを使用しており、プローブは省略された | どのドライバーが使用しているか |
| **応答なし** | プローブで応答を受け取らなかった | 電源、バス、所有者、デバイスプロトコルのどれが原因か |

### 温度センサーの候補を絞る

**STTS751は資料に裏付けられた`0x39`の候補です。** Semtechの温度ドライバーヘッダーは、`0x39`を`STTS751-0DP3F`に明示的に関連付けています。元記事の仮説を強める情報ですが、このアドレスを使うすべての基板上の部品を特定するものではありません。[Semtech STTS751ドライバーヘッダー](https://github.com/Lora-net/sx1302_hal/blob/master/libloragw/inc/loragw_stts751.h)

互換性のある部品を特定し、別のプロセスが使用していないことを確認してから、次のコマンドで識別レジスターを読み取ります。

```bash
sudo i2cget 1 0x39 0xfd b
sudo i2cget 1 0x39 0xfe b
```

ここで**`1`**は確認済みのバス、**`0x39`**はデバイス、**`b`**はSMBusのバイトデータ読み取りを指定します。STTS751-0では、`0xFD`の製品IDは`0x00`、`0xFE`のメーカーIDは`0x53`と資料に記載されています。これらのトランザクションはレジスターアドレスを選びますが、設定値を書き込みません。[STTS751データシート、レジスターマップと識別レジスター](https://www.st.com/resource/en/datasheet/stts751.pdf)

読み取り値をチップの刻印と資料に照らして確認します。一致する値は識別の根拠を増やします。エラーが出た場合は、ハードウェア設定を変える前にバスと使用状況を確認してください。このセンサーが測定するのは周辺の温度です。PiのCPU温度とは別の値です。

## セキュアエレメントを調べる

**ATECC608は独立した認証部品です。** 設定、シリアル番号、公開鍵、保護された鍵データを別々の情報として扱います。公開鍵を読み取れても、対応する秘密鍵は分かりません。

Microchipの**CryptoAuthLib**はデバイス用のインターフェースを提供します。**cryptoauthtools**リポジトリにはライブラリを使う例が含まれています。例を実行する前に、対象システム向けの説明に従ってネイティブライブラリとPythonバインディングを準備します。無関係なPythonパッケージのインストールやスクリプト単体のコピーでは、I2Cバックエンドの動作を確認できません。[Microchip CryptoAuthLib](https://github.com/MicrochipTech/cryptoauthlib)、[Microchip cryptoauthtools](https://github.com/MicrochipTech/cryptoauthtools)

準備した`cryptoauthtools/python/examples`ディレクトリから、元記事の確認コマンドを実行します。

```bash
sudo python3 info.py -i i2c
```

**`-i i2c`**引数はインターフェースを選択します。仮想環境を使う場合は、その環境のPythonインタープリターを明示し、対応するネイティブライブラリが見つかるようにします。多くの環境で`sudo python3`はシステムのインタープリターを選ぶため、モジュールの読み込みに失敗することがあります。

確認済みの`info.py`はリビジョン情報、シリアル番号、設定、ロック状態を読み取ります。データゾーンがロックされている場合、スロット0の公開鍵を取得しようとします。プロビジョニング手順は実行しません。スロット0の公開鍵読み取りだけが失敗しても、デバイスの故障は証明されません。[Microchip info.pyのソース](https://github.com/MicrochipTech/cryptoauthtools/blob/master/python/examples/info.py)

| 出力または操作 | 意味 |
|---|---|
| **Configuration locked** | 設定に制限が適用されている |
| **Data zone locked** | 設定済みスロットポリシーに基づいてアクセスを解釈する |
| **公開鍵が表示された** | 公開情報を取得した。秘密鍵をエクスポートしたのではない |
| **`config.py`の実行** | 設定、ロック、鍵生成の操作を含むプロビジョニング例 |

**確認エラーを直す目的で`config.py`を実行しないでください。** このソースには設定の書き込み、ゾーンのロック、鍵生成の呼び出しが含まれています。既に設定済みのデバイスでは、既定の鍵生成経路にも注意が必要です。[Microchip config.pyのソース](https://github.com/MicrochipTech/cryptoauthtools/blob/master/python/examples/config.py)

Microchipのプロビジョニングプロファイルを見ると、データゾーンがロックされていても、すべてのスロットに同じアクセス権があるとは限らないことが分かります。そのプロファイルだけではM1の正確な設定は分かりません。既存の設定を保持し、鍵を再利用する計画を立てる前に、該当する部品の資料を確認してください。[Microchipのメモリーとスロットアクセスのポリシー](https://onlinedocs.microchip.com/oxy/GUID-8F01540E-14A9-479E-9D27-FFFB14DE474E-en-US-2/GUID-92031846-201F-42DA-831D-FA3B6CF79B9B.html)

## ファンとボタンの不明点を調べる

**3ピンのファンソケットだけでは、電圧、極性、制御方法を特定できません。** ピン番号を撮影し、ファンのラベルを読みます。交換品を接続したりGPIOオーバーレイを選んだりする前に、電源と制御の接続を確認してください。

同様に、元の調査ではボタンのGPIOが特定されていません。基板リビジョンに対応するドライバーまたは設定を探し、電源を切って導通を確認します。未使用に見えるGPIOをすべて出力にしてボタンを探さないでください。

| 周辺機器 | 集める情報 | 合格条件 |
|---|---|---|
| **ファン電源** | ファンの定格、コネクターのグラウンドと電源 | 測定した電源がファン仕様に一致する |
| **ファン制御** | ドライバー、設定、または追跡した制御回路 | 起動時と高温時の動作が定義されている |
| **ユーザーボタン** | 接点配線、GPIOマッピング、入力極性 | 意図した1回の押下で期待したイベントが発生する |

新しいOSを入れても、元の機器の冷却ポリシーが自動で再現されるわけではありません。初めて長時間テストするときは、ファンの動作と温度を同時に観察します。ケースの通気経路を維持し、必要な冷却が失われた場合はテストを中止してください。

## ゲートウェイのソフトウェアスタックを選ぶ

**基板の対応とサーバープロトコルを分けて考えます。** 互換性のあるLoRaWANサーバーを選んでも、不適切なリセット処理やRFキャリブレーションは解決しません。まず、コンセントレーター、キャリア配線、OS、地域設定に対応するソフトウェアを選びます。

| ソフトウェア | 役割 | 導入前に確認すること |
|---|---|---|
| **Semtech SX1302 HAL** | ソースレベルの立ち上げと診断ツール | 基板のリセット処理とモジュール設定 |
| **LoRa Basics Station** | 認証を使ったゲートウェイとサーバーの接続 | 動作する基板統合とサーバー認証情報 |
| **ChirpStack Concentratord** | 専用のコンセントレーターサービス | 対応モデル、キャリブレーション、GPIOマッピング |

ChirpStackはSPIの**`seeed_wm1302`**モデルを掲載しています。これはモジュールの対応を示します。完成したM1イメージやすべてのM1リビジョンへの対応を保証するものではありません。別製品SenseCAP M2のインストール手順をM1向けファームウェアの手順として扱わないでください。[ChirpStackハードウェア対応](https://www.chirpstack.io/docs/chirpstack-concentratord/hardware-support.html)、[ChirpStackのSeeedインストール対象](https://www.chirpstack.io/docs/chirpstack-gateway-os/install/seeed.html)

The Things Stackの資料は、従来のSemtech UDPフォワーダーより**LoRa Basics Station**を推奨しています。StationはTLSとトークン認証に加え、集中設定の機能を提供します。既存のUDPの例はパケット転送の理解に役立ちますが、サーバーアドレスの設定だけでは同じ保護は提供されません。[The Things StackのUDPガイダンス](https://www.thethingsindustries.com/docs/hardware/gateways/concepts/udp/)、[LoRa Basics Stationの文書](https://www.thethingsindustries.com/docs/hardware/gateways/concepts/lora-basics-station/)

### 上流ツールを準備する

対象のPi上の新しい作業ディレクトリでビルドします。

```bash
git clone https://github.com/Lora-net/sx1302_hal.git
cd sx1302_hal
git rev-parse HEAD
make
```

ビルド出力と一緒にコミットIDを保存します。ビルド完了から確認できるのはコンパイラーとの互換性です。無線を動かすには、検証済みのリセット処理と正しい設定も必要です。Semtechの資料ではHALと補助プログラムの役割を説明しています。[SX1302 HALのビルドとツールの文書](https://github.com/Lora-net/sx1302_hal)

ハードウェアアクセスツールを実行する前に、リセットファイルを確認します。

```bash
sed -n '1,180p' tools/reset_lgw.sh
```

このファイルを変更せずランタイムディレクトリへコピーしないでください。Semtechのハードウェアアクセスプログラムは、識別ツールなどの実行時にリセットスクリプトを自動で使う場合があります。担当するすべてのピン、信号方向、GPIO API、起動時と終了時の状態を確認します。

基板の検証を終えたら、選んだスタックの手順を使ってコンセントレーターのEUIを読み取り、ゲートウェイを登録します。サーバー設定を追加するときは、モジュールのキャリブレーションとRF設定を保持してください。Semtech UDP設定の`gateway_ID`はEUIを指します。一方、The Things StackコンソールのGateway IDは、登録時に使う人間が読む識別子です。[The Things Stackのゲートウェイ設定](https://www.thethingsindustries.com/docs/hardware/gateways/concepts/udp/)

## センサーの配信を証明する

**段階的な証拠で最初の失敗層を特定します。** ゲートウェイがオンラインと表示されても、サーバーへの接続しか確認できません。受け入れテストでは、既知のセンサー、周波数プラン、デコード済みのアプリケーションペイロードも確認します。

次の順序は提案するテスト計画であり、M1で測定した結果ではありません。

| チェックポイント | 保存する証拠 | 意味 |
|---|---|---|
| **ホスト準備完了** | OS、カーネル、電源、インターフェース一覧 | Linuxの準備が完了した |
| **コンセントレーター応答** | EUIと初期化成功ログ | ホストとコンセントレーターの通信が動作する |
| **無線受信** | 期待するセンサーパケットと受信メタデータ | 設定済みの受信経路が動作する |
| **サーバー受け入れ** | センサーと関連するゲートウェイイベント | 転送とサーバールーティングが動作する |
| **アプリケーションでデコード** | 期待する測定値とタイムスタンプ | アプリケーション経路が動作する |
| **再起動後の復旧** | 再起動後の同じ確認結果 | 起動設定を再現できる |

**OTAA**センサーでは、アクティベーション交換とその後のアップリンクも確認します。OTAAはOver-the-Air Activationの略で、セッションを確立するための参加手順です。参加要求を受信しただけでは、参加成功やダウンリンク経路を確認できません。[The Things Stackのアクティベーション資料](https://www.thethingsindustries.com/docs/hardware/devices/concepts/abp-vs-otaa/)

**診断例:** ゲートウェイはサーバーに接続しEUIを報告しますが、センサーが現れないとします。センサーの送信設定、選択した受信チャネル、アンテナ経路、無線ログを優先して確認します。この状況でATECC608を再プログラムしても、欠けている証拠は解決しません。

**別の診断例:** センサーパケットがローカルに現れるものの、アプリケーションに届かないとします。パケット時刻をゲートウェイとサーバーのイベントに照合し、ルーティング、デバイス登録、デコードを確認します。サーバーがイベントを受け取る前に、ログ上の無線パケットだけでペイロードデコーダーを原因と決めつけないでください。

## 症状別のトラブルシューティング

| 症状 | まず確認する項目 | 次の対応 |
|---|---|---|
| **SPIデバイスファイルがない** | 有効な起動設定とインターフェース設定 | 対象のインターフェースを有効にして再起動 |
| **SPIはあるが無線が動かない** | 電源、装着、リセット手順、チップセレクト | サーバー設定を変える前に電気経路を確認 |
| **GPIO exportエラー** | 古いsysfsの前提とインストール済みカーネル | GPIO APIを確認済みの実装を使う |
| **GPIOが使用中** | `gpioinfo`に表示された利用者 | 再試行前に使用者を確認 |
| **設定後にLEDが動かない** | オーバーレイの適用とGPIO22の競合 | 登録済みLEDデバイスとリセットスクリプトを確認 |
| **I2Cデバイスが見つからない** | バス番号、電源、既存の使用者 | 広範囲の再スキャンを避けて調べる |
| **暗号ライブラリを読み込めない** | インタープリター、バインディング、ネイティブライブラリのパス | ソフトウェア環境を修正 |
| **公開鍵の読み取りに失敗** | スロットポリシーと先行する読み取り結果 | プロビジョニングせずに設定を確認 |
| **ファンが動かない** | 確認済み電源と冷却制御の実装 | 長時間テスト前に冷却を復旧 |
| **アップリンクが届き、参加に失敗** | ダウンリンク経路と地域・デバイス設定 | 参加応答と受信ウィンドウを追跡 |

修正は1回につき1つの実験として扱います。変更前の設定を保存し、変数を1つ変更して同じ確認を繰り返し、期待した証拠の有無を記録します。

## ハードウェア記録を作る

調査結果を再現可能な引き継ぎ資料にするには、このテンプレートを使います。

```text
キャリアのリビジョンと写真:
コンセントレーターのモデル、インターフェース、RF帯域:
ホストのモデル / OS / カーネル / GPIOツールのバージョン:
電源 / アンテナ / 冷却構成:
検証済みのピンマッピングと証拠:
未解決の接続と対象外の機能:
ソフトウェアのリポジトリーとコミット:
リセット処理とGPIOの使用者:
ゲートウェイEUI / サーバー / 周波数プラン:
センサーのアクティベーションとデコード済みアップリンクの証拠:
再起動後の復旧結果:
元のカードの保管場所とロールバック手順:
```

**判断演習:** モジュールのラベルがなく安価なキャリアと、ラベルを読めて動作実績が資料にある高価な組み立て品があります。Pi、コンセントレーター、アンテナ、電源、検証に必要な時間も比較に加え、どちらがプロジェクトに合うか判断します。適切な選択は、キャリアの表示価格ではなく、目的のサービスに必要な総費用と証拠で決まります。

**期待する考え方:** 学習目的のプロジェクトでは、測定器と時間があれば未解決の配線を許容できます。運用中のセンサーを支えるゲートウェイでは、再現可能な起動、冷却、ソフトウェア対応、実証済みのデータ配信が必要です。導入を止める未解決事項を記録してください。

## 次の手順

まずハードウェア記録を完成させ、リセットスクリプトの不一致を解決します。その後、既知のセンサーを1台だけ起動し、アプリケーションでデコードするまでの証拠を保存してから、デバイスを追加します。

**受け入れ記録:** 基板リビジョン、モジュールラベル、無線帯域、電源測定値、有効なSPIデバイス、GPIOライン名、リセット手順、コンセントレーターログ、サーバー接続、デコード済みアップリンク1件を保存します。値ごとに「観測済み」「資料に記載」「仮定のまま」のいずれかを示してください。プロセスの起動成功をRF性能やアプリケーションへの配信の証明にしないでください。

目的がメッシュメッセージングなら、まず[Meshtastic、MeshCore、Reticulumの比較ガイド](/articles/meshtastic-vs-meshcore-vs-reticulum-comparison-guide/)でプロトコルの役割を比べてください。LoRa無線技術を共有してもファームウェアの互換性は確認できません。LoRaWAN手順をMeshtasticへの変換として扱わず、メッセージングを導入する場合は[MeshtasticDの対応ハードウェア資料](https://meshtastic.org/docs/meshtasticd/)を確認します。

## 出典と画像クレジット

調査確認日: 2026年9月12日。日付のない資料とリポジトリーリンクは、この記事で確認したバージョンを指します。ローカル画像は元のラベルとクレジット情報を保持しています。

| 発行元 | 出典と日付 |
|---|---|
| **Clockwork Bird** | [SenseCAP M1 Raspberry Pi Shield](https://clockworkbird9.wordpress.com/2023/05/03/sensecap-m1-raspberry-pi-shield/)、2023-05-03。基板写真、注釈付きヘッダー、転載したメーカーのブロック図 |
| **Seeed Studio / SenseCAP** | [M1概要と仕様](https://www.sensecapmx.com/docs/sensecap-m1/overview/)、日付なし。元のブロック図のクレジット |
| **Seeed Studio** | [WM1302の資料とモジュールピン配置](https://github.com/seeed-lora/WM1302-doc)、リポジトリー |
| **Semtech** | [SX1302/SX1303 HAL](https://github.com/Lora-net/sx1302_hal)。リンク先のリセットスクリプトと温度ドライバーのソースを含む |
| **Raspberry Pi** | [起動設定](https://www.raspberrypi.com/documentation/computers/config_txt.html)、[GPIO使用ガイド](https://pip-assets.raspberrypi.com/categories/685-app-notes-guides-whitepapers/documents/RP-006553-WP/A-history-of-GPIO-usage-on-Raspberry-Pi-devices-and-current-best-practices)、[オーバーレイ資料](https://github.com/raspberrypi/linux/blob/rpi-6.12.y/arch/arm/boot/dts/overlays/README) |
| **Linux / libgpiod** | [非推奨のGPIO sysfsインターフェース](https://www.kernel.org/doc/html/next/admin-guide/gpio/sysfs.html)、[gpiosetマニュアル](https://libgpiod.readthedocs.io/en/master/gpioset.html)、後者は2026年8月付 |
| **i2c-tools** | [i2cdetectマニュアル](https://kernel.googlesource.com/pub/scm/utils/i2c-tools/i2c-tools/+/refs/tags/v4.3/tools/i2cdetect.8)、v4.3ソース |
| **STMicroelectronics** | [STTS751データシート](https://www.st.com/resource/en/datasheet/stts751.pdf)、改訂7 |
| **Microchip** | [CryptoAuthLib](https://github.com/MicrochipTech/cryptoauthlib)、[cryptoauthtools](https://github.com/MicrochipTech/cryptoauthtools)、[スロットアクセスのポリシー資料](https://onlinedocs.microchip.com/oxy/GUID-8F01540E-14A9-479E-9D27-FFFB14DE474E-en-US-2/GUID-92031846-201F-42DA-831D-FA3B6CF79B9B.html) |
| **ChirpStack** | [Concentratordのハードウェア対応](https://www.chirpstack.io/docs/chirpstack-concentratord/hardware-support.html)、[Seeedのインストール対象](https://www.chirpstack.io/docs/chirpstack-gateway-os/install/seeed.html) |
| **The Things Industries** | [UDPフォワーダー](https://www.thethingsindustries.com/docs/hardware/gateways/concepts/udp/)、[LoRa Basics Station](https://www.thethingsindustries.com/docs/hardware/gateways/concepts/lora-basics-station/)、[デバイスのアクティベーション](https://www.thethingsindustries.com/docs/hardware/devices/concepts/abp-vs-otaa/) |
| **Meshtastic** | [MeshtasticDの文書](https://meshtastic.org/docs/meshtasticd/)、日付なし |
