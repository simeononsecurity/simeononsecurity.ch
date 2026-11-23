---
title: "Eye Spy: ESP32向けパッシブ監視・トラッカー検出器"
date: 2026-06-07
lastmod: 2026-11-22
toc: true
draft: false
description: "BLEとWiFiを使うESP32用パッシブ検出器、Eye Spy v1.1の技術資料です。カメラ、トラッカー、ドローンなどの信号を検出します。"
genre: ["プライバシーツール", "対監視", "IoTセキュリティ", "組み込みシステム", "セキュリティ研究", "WiFiセキュリティ", "Bluetoothセキュリティ", "ESP32プロジェクト", "ハードウェアセキュリティ", "オープンソースセキュリティ"]
tags: ["Eye Spy", "ESP32", "M5Stack Atom Lite", "監視検出", "対監視", "BLE検出", "WiFiスキャン", "AirTag検出", "ALPR検出", "Flock Safety", "ボディカメラ検出", "ドローン検出", "OpenDroneID", "NimBLE", "NeoPixel", "SK6812", "PlatformIO", "C++", "オープンソース", "プライバシー", "パッシブBLE", "モニターモード", "OUI検出", "トラッカー検出", "Axonボディカメラ", "Ray-Ban Meta", "Samsung SmartTag", "Tileトラッカー", "隠しカメラ", "simeononsecurity"]
canonical: "https://simeononsecurity.com/articles/eye-spy-passive-surveillance-detector-esp32-2026/"
cover: "/img/cover/eye-spy-passive-surveillance-detector-esp32-2026.webp"
coverAlt: "濃紺の背景に、色鮮やかな電波をまとった小型のM5Stack Atom Liteを描いたイラストです。BluetoothとWiFiによる監視検出を表しています。"
coverCaption: ""
---

**親指ほどの大きさで、何かに見られていると知らせるパッシブセンサー**

## はじめに: 見えない監視環境

物理環境には、監視、録画、追跡を行う装置が増えています。交差点のナンバープレートリーダー、法執行機関のボディカメラ、賃貸物件のカメラ、バッグや車に隠されたAirTagのような商用トラッカー、店舗入口の監視カメラなどです。これらの多くは**Bluetooth LE**または**WiFi**で無線通信します。*その通信の多くは周囲に向けてブロードキャストされるため、適切な受信機があれば誰でも検出できます。*

[**Eye Spy**](https://github.com/simeononsecurity/eye-spy)は、この性質を利用するパッシブ監視検出ツールです。Eye Spyは、角砂糖ほどの大きさのESP32-PICO-D4開発ボード、**M5Stack Atom Lite**上で動作します。BLEとWiFiの周波数帯を継続的に監視し、録画装置、監視カメラ、**ALPR**（自動ナンバープレート認識）システム、ドローン、個人用トラッカーの電子的な特徴を探します。信号を検出するとRGB LEDの色が変わります。

*何にも接続せず、何も送信しません。* 受信してスコアを付け、光で知らせます。

この記事では、Eye Spyが検出する対象、信頼度スコアの仕組み、各検出エンジンの設計、デバイスの組み立てと書き込み方法、実用上の制限を詳しく説明します。

**自分で組み立てたくない場合は、**STS Collectiveで、すぐに使えるファームウェア書き込み済みの**[Eye Spy検出器](https://stscollective.com/collections/eye-spy-passive-surveillance-detectors)**を購入できます。読者コード**SIMEONONSECURITY**で最大20%割引になります。

{{< stscollective-ad "eyespy" >}}

---

## LEDインジケーター: これがユーザーインターフェースのすべて

[ESP32 WiFi Canary: 2.4 GHz帯のパッシブ脅威検出](https://simeononsecurity.com/articles/esp32-wifi-canary-passive-wifi-threat-detection-2026/)と同様に、Eye Spyの出力はM5Stack Atom LiteのGPIO 27に接続されたSK6812 RGB NeoPixel 1個だけです。LEDは常に4段階の脅威レベルを示します。

| 色 | 意味 | スコア範囲 |
|-------|-------------|---------------------|
| 🔵 青の点滅 | 起動中 / 初回スキャン | -- |
| 🟢 緑の点灯 | 問題なし、未検出 | 0–2 |
| 🟡 黄の点灯 | 注意: 近くに録画装置がある可能性 | 3–5 |
| 🔴 赤の点滅 | 警告: 監視または追跡装置を検出 | 6+ |

**高い信頼度の検出が1件あれば（Axonボディカメラ、Flock Safetyカメラ、ALPRのOUI一致、AirTag）、1回の検出サイクルでスコアが十分に上がり、LEDがすぐに赤になります。** 中程度の信頼度の検出が複数あるとスコアが累積して黄色になり、さらに赤に達する場合もあります。

---

## ハードウェア

### 主な対象: M5Stack Atom Lite

| 部品 | 詳細 |
|-----------|--------|
| ボード | M5Stack Atom Lite |
| MCU | ESP32-PICO-D4 |
| LED | GPIO 27のSK6812 NeoPixel |
| ボタン | GPIO 39（入力専用） |
| フラッシュ | 4 MB |

Atom Liteは単体で動作する完全なプラットフォームです。**はんだ付け、ブレッドボード、外付け部品は不要です。** USBに接続すれば動作します。

### 汎用ESP32 DevKit

2つ目のPlatformIOビルド環境（`esp32dev`）は、GPIO 2にオンボードLEDを備えた標準的なESP32 DevKitを対象にしています。検出ロジックは同じように動作します。Atom Liteの形状が不要な場合や、検出ロジックを開発・テストする場合に役立ちます。

---

## スコアリングシステム

Eye Spyは、各検出エンジンからの信号を1つの整数にまとめる**信頼度スコアモデル**を使います。スコアがLEDの状態（緑、黄、赤）を決め、2つの自動管理機能が働きます。

### スコアの減衰

新しい検出がなければ、スコアは**60秒ごとに1点下がります**。検出した装置から離れると、操作しなくても数分でLEDが緑に戻ります。

### 再加点までのクールダウン

各検出*タイプ*には**120秒のクールダウン**があり、同じ信号源から再び加点するまで待ちます。*これにより、1台の装置が常時スコアを積み上げるのを防ぎます。* 検出範囲内にFlock Safetyカメラが留まると、まず+5点を加え、次に加点できるまで120秒待ちます。

この2つの仕組みを組み合わせると、次のようになります。

- **一時的な検出**（AirTagを積んだ車が通過するなど）は自動的に解消されます。
- **継続的な監視**（固定位置でのボディカメラ運用など）は、検出範囲内にいる間、LEDを警告状態に保ちます。
- **同じ装置を繰り返し検出しても**、スコアが際限なく増えることはありません。

---

## 検出エンジン

{{< figure src="eye-spy-ble-wifi-detection-engines-overview.webp" alt="Eye Spyの並列BLE・WiFi検出エンジンの図です。AirTag、ボディカメラ、ALPRシステム、ドローンを探し、信頼度スコアの脅威モデルに結果を送ります" >}}

Eye Spyは、次の3段階のスキャンを継続的に切り替えます。

**BLEパッシブ（9秒）→ WiFiスキャン（約3秒）→ プロミスキャススニフ（5秒）→ 繰り返し**

ESP32の無線を共有するため、WiFi操作の前にBLEを明示的に停止します。各サイクルの開始時にBLEを再起動します。

---

### エンジン1: BLEパッシブスキャン

BLEスキャンには、**スキャン要求を送信しないNimBLE**を使います。デバイスはBLEアドバタイズパケットを受信し、応答しません。*そのためEye Spyは検出対象から電子的に見えません。パッシブスキャナーは対象側から検出されないためです。*

混雑した環境での誤検出を減らすため、信号が**−90 dBm**より弱いデバイスは無視します。

#### BLE検出テーブル

| # | 対象 | 検出方法 | スコア |
|---|--------|-----------------|-------|
| 1 | **Axonボディカメラ** | BLE MAC OUI `00:25:df`（Axonのボディカメラ、Taser、法執行機関向け機器） | +5 🔴 |
| 2 | **Ray-Ban Metaスマートグラス** | BLEサービスUUID `0xFD5F` | +5 🔴 |
| 3 | **Flock Safety BLE** | BLEデバイス名に`Flock`、`Penguin`、`Pigvision`、`FS Ext Battery`のいずれかを含む | +5 🔴 |
| 4 | **カードスキマー（HC-03/05/06）** | BLEデバイス名の完全一致。決済端末スキマーでよく見つかるBluetoothモジュール | +5 🔴 |
| 5 | **Apple AirTag** | メーカー情報`0x004C`のサブタイプ`0x12`/`0x1E`、または生ペイロード`1E FF 4C 00` / `4C 00 12` | +4 🔴 |
| 6 | **ドローン（OpenDroneID BLE）** | BLEサービスUUID `0xFFFA`、またはアプリコード`0x0D`を含むADサービスデータペイロード | +4 🔴 |
| 7 | **Samsung SmartTag** | BLEサービスUUID `0xFD5A` | +3 🟡 |
| 8 | **Tileトラッカー** | BLEサービスUUID `0xFEED`または`0xFEEC` | +3 🟡 |
| 9 | **MeshCoreノード** | BLEデバイス名の接頭辞`MeshCore-` | +2 🟡 |
| 10 | **iBeacon（店舗・施設での追跡）** | メーカー情報`0x004C 0x02 0x15`。店舗、空港、スタジアムで移動を追跡するために使用 | +2 🟡 |
| 11 | **不明な持続デバイス** | 未分類のBLE MACが5分以上にわたって3回以上検出された場合（偵察・追尾デバイスの検出） | +2 🟡 |

#### 主なBLE検出の詳細

**Axonボディカメラ（+5）**: Axon（旧TASER International）は、米国の法執行機関で広く導入されているボディカメラシステムを製造しています。OUI `00:25:df`はAxonに登録され、同社のウェアラブル機器に使われています。**1回検出するだけで警告のしきい値に達します。**

**Ray-Ban Metaスマートグラス（+5）**: Ray-Ban Metaの共同開発製品には、動画や写真を撮影できる一般消費者向けスマートグラスがあります。BLEサービスUUID `0xFD5F`は、この機器の特徴的なアドバタイズに使われています。*一般向け製品のため、人が多い公共の場所でも見つかる可能性があります。* 所有者の意図にかかわらず、このスコアの検出には注意してください。

**カードスキマーのBluetoothモジュール（+5）**: HC-03、HC-05、HC-06は安価なBluetoothシリアルモジュールで、決済端末のオーバーレイやATMスキマーでよく見つかります。既知のモジュールファームウェアのデフォルト名とデバイス名を完全一致で照合します。**赤い警告が出た場合は、近くの決済端末をすぐに目視確認してください。**

**Apple AirTag（+4）**: AirTagはApple独自の**Nearby Interaction**プロトコルでアドバタイズします。検出処理はメーカー固有データヘッダー（`0x004C` = Apple）とAirTag固有のサブタイプ（通常のアドバタイズは`0x12`、紛失物のアドバタイズは`0x1E`）を探します。生ペイロードのパターンも使い、検出経路を補います。

**OpenDroneID BLE（+4）**: **ASTM F3411 Remote ID**規格は、米国で商用ドローン向けにFAAも採用している、ドローンが識別情報と位置を送信するためのブロードキャストプロトコルです。Eye Spyは、指定されたRemote IDサービスのGATT UUID `0xFFFA`と、ADサービスデータペイロードのアプリケーションコード`0x0D`を探します。*近くで規格に準拠した商用ドローンが動作すると、この検出が作動します。*

**不明な持続デバイス（+2）**: これは**追尾検出**エンジンです。上記の特定検出に分類されないBLE MACを追跡します。同じ未分類MACが5分以上にわたって3回以上現れると、スコアを加算します。デバイス持続トラッカーは最大50個の不明なMACを同時に監視し、30分検出されなければ登録を削除します。**既知のサービスUUIDやメーカーのパターンに一致しない、独自または改造されたトラッカーも検出できます。**

**iBeacon（+2）**: 小売店、空港、スタジアムでは、AppleのiBeacon形式（`0x4C 0x00 0x02 0x15`）を使って物理空間内のデバイスの移動を追跡します。UUIDにかかわらず標準アドバタイズ形式を検出します。これは特定のUUIDではなく、導入形態を対象にしています。*検出された場合は、その場所でBluetooth機器の存在が追跡されている可能性があります。*

---

### エンジン2: WiFiスキャン、アクティブなチャネル探索

WiFiスキャンエンジンは、ESP32標準のAPスキャン機能を使って近くのアクセスポイントを列挙し、BSSIDとSSIDを既知の監視装置の特徴と照合します。

#### WiFi検出テーブル

| # | 対象 | 検出方法 | スコア |
|---|--------|-----------------|-------|
| 12 | **Flock Safetyカメラ（OUI）** | 22件のFlock Safety OUIテーブル（`d4:bb:e6`、`3c:61:05`、FS-Ext-Battery接頭辞）とBSSIDを照合 | +5 🔴 |
| 13 | **ALPR / LPRカメラ（OUI）** | Motorola Solutions / Vigilant SolutionsのOUI `00:0e:58`とBSSIDを照合 | +5 🔴 |
| 14 | **FlockキーワードSSID** | SSIDに`flock`、`flocksafety`、`fs ext`、`penguin`、`pigvision`のいずれかを含む | +5 🔴 |
| 15 | **ALPRキーワードSSID** | SSIDに`alpr`、`lpr`、`vigilant`、`plateread`、`licenseplat`、`motorola`、`automate`のいずれかを含む | +4 🔴 |
| 16 | **監視カメラのメーカー（OUI）** | 31件のカメラOUIテーブルとBSSIDを照合。Hikvision、Dahua、Axis、Ring、Nest、Arlo、Wyze、Reolink、FLIR、Amcrest、Vivotek、Hanwha、Mobotix、Ubiquiti UniFiなど | +3 🟡 |
| 17 | **カメラキーワードSSID** | SSIDに`cam`、`ipcam`、`cctv`、`nvr`、`dvr`、`doorbell`、`surv`、`blink`、`lorex`、`protect`、`genetec`などを含む | +2 🟡 |

#### Flock Safety OUIテーブル

22件の`FLOCK_OUIS`テーブルは、このプロジェクトで最も詳細な検索表です。内容は次のとおりです。

- `d4:bb:e6`: IEEE登録済みのFlock Safety OUI。
- `3c:61:05`: IEEE登録済みのFlock Safety OUI。
- 現場のFlock FS-Ext-BatteryとFlock WiFiカメラで観測された追加のMAC接頭辞20件。

これら22件は、導入済みのFlock Safety ALPRカメラシステムで観測されたハードウェアMACアドレス範囲です。**OUIによる検出はSSIDに依存しません。** キーワードを含まないSSIDのFlockカメラでも、BSSIDのOUIが一致すれば+5点になります。

Flock SafetyとVigilant SolutionsのOUIは別々の表にあります。同じスキャンサイクルで両方の種類を独立して加点できます。*両方のメーカーの装置がある場所では、1回のWiFiスキャンで合計+10点になる場合があります。*

#### 監視カメラメーカーのOUIテーブル

31件の監視カメラテーブルには、店舗、商業施設、住宅で使われる主要なIPカメラメーカーが含まれています。

- **企業・商業施設**: Hikvision、Dahua、Axis、Vivotek、Hanwha（Samsung Techwin）、Mobotix、Genetec。
- **消費者向け・小規模オフィス**: Ring、Nest、Arlo、Wyze、Reolink、Blink、Lorex、Amcrest。
- **インフラ**: Ubiquiti UniFi（アクセスポイントとカメラでOUIの範囲を共有）、FLIR。

キーワードが一致しなくても、ここで一致すれば注意レベルの+3点になります。SSIDのキーワードも一致すると、同じカメラネットワークでOUIの+3点にSSIDの+2点が加わり、1回のスキャンサイクルで警告に達します。

---

### エンジン3: WiFiプロミスキャス、パッシブフレームスニッフィング

プロミスキャスエンジンはESP32の無線を**モニターモード**に切り替え、未加工の802.11管理フレームを取得します。SSIDをアドバタイズしない装置、特に**WiFi Neighbor Awareness Networking（NaN）**経由で**Remote ID**を使うドローンを検出できます。

プロミスキャス処理中は、ドローンNaNフレームの受信範囲を広げるため、無線が400 msごとに`{1, 6, 11, 3, 8, 13}`の**チャネルを切り替えます**。

#### プロミスキャス検出テーブル

| # | 対象 | 検出方法 | スコア |
|---|--------|-----------------|-------|
| 18 | **ドローン（OpenDroneID WiFi NaN）** | 宛先`51:6f:9a:01:00:00`への802.11管理フレーム。ASTM F3411 Remote IDのブロードキャスト | +4 🔴 |

**OpenDroneID WiFi NaN（+4）**: ASTM F3411規格では、Remote IDのWiFi NaNフレームにマルチキャスト宛先アドレス`51:6f:9a:01:00:00`を定めています。WiFiで位置と識別情報を送信する規制対象の商用ドローンは、この宛先にフレームを送信します。Eye Spyは、このマルチキャストMAC宛ての管理フレームを受動的に監視します。*ドローン運用者が検出を回避するにはRemote IDを無効にする必要がありますが、それ自体が規制違反になります。*

この検出はBLEのOpenDroneIDエンジン（検出#6）を補完します。*ハードウェアと設定によって、ドローンはBLE、WiFi、または両方でアドバタイズします。* Eye Spyは両方に対応します。

---

## フェーズのスケジュールと無線管理

```
BLEパッシブ（9秒）→ WiFiスキャン（約3秒）→ プロミスキャススニフ（5秒）→ 繰り返し
```

ESP32-PICO-D4は、BLEとWiFiの両方で使う**単一の共有2.4 GHz無線**を備えています。Eye Spyは次のように管理します。

1. **BLEフェーズ**（9秒）: NimBLEスタックを動かし、スキャン要求を送信せずにパッシブスキャンを実行。
2. **BLE停止**: WiFiを使う前にBLEスタックを明示的に停止。
3. **WiFiスキャン**（約3秒）: 全チャネルでAPをアクティブスキャンし、OUIとSSIDを照合。
4. **プロミスキャススニフ**（5秒）: チャネルを切り替えながら802.11フレームをパッシブに取得。
5. **WiFi停止**: WiFiを停止し、次のサイクルに向けてBLEを再起動。

このようにフェーズを明示的に管理することで無線の競合を防ぎ、各サイクルでBLEとWiFiの両エンジンが順番に無線を使えるようにします。

---

## シリアル出力

すべての行に`[eyespy]`が付くため、簡単に絞り込めます。シリアルモニターは**115200 baud**で動作します。

### 起動

```
[eyespy] Eye Spy v1.1 starting
[eyespy] init OK
```

### 通常サイクル

```
[eyespy] BLE scan start
[eyespy] WiFi scan
[eyespy] WiFi done  score=0
[eyespy] promisc ON
[eyespy] status  score=0  CLEAR  phase=PROMISC  tracked=3
```

### 検出イベント

```
[eyespy] Flock-cam OUI d4:bb:e6  "Flock_CAM_0032"
[eyespy] +5 (Flock-cam-OUI)  score=5
[eyespy] WiFi done  score=5
[eyespy] promisc ON
[eyespy] status  score=5  CAUTION  phase=PROMISC  tracked=12
[eyespy] Axon-cam  RSSI=-62
[eyespy] +5 (Axon-cam)  score=10
[eyespy] status  score=10  ALERT  phase=BLE  tracked=12
[eyespy] decay  score=9
```

`tracked=N`は、現在、持続トラッカーに登録されている固有BLE MACアドレスの数を示します。BLE環境の密度を把握するのに役立ちます。

### スコア項目

各ステータス行には次の情報があります。

- **score**: 現在の脅威スコア。
- **state**: `CLEAR` / `CAUTION` / `ALERT`。
- **phase**: 現在のエンジン（`BLE` / `WIFI` / `PROMISC`）。
- **tracked**: 持続トラッカーテーブル内の固有BLE MACアドレス数。

---

## ビルドと書き込み

### 必要なもの

- **PlatformIO**（CLIまたはVS Code拡張機能）。
- **M5Stack Atom Lite**または任意のESP32 DevKit。
- USB-Cケーブル。

### 依存関係

PlatformIOが自動的にインストールします。

```ini
lib_deps =
    adafruit/Adafruit NeoPixel @ ^1.15.1
    h2zero/NimBLE-Arduino @ ^1.4.3
```

**Adafruit NeoPixel**はSK6812 RGB LEDを制御します。**NimBLE-Arduino**はパッシブBLEスキャンスタックを提供します。パッシブスキャンモードを適切にサポートし、スキャン要求パケットの送信を避け、メモリ使用量も少ないため、標準のESP32 BLEライブラリより適しています。

### M5Stack Atom Liteへの書き込み

```bash
git clone https://github.com/simeononsecurity/eye-spy.git
cd eye-spy

# Atom Lite向けにビルドして書き込む
pio run -e atom-lite -t upload

# 115200 baudでシリアルモニターを開く
pio device monitor -b 115200
```

### 汎用ESP32 DevKitへの書き込み

```bash
pio run -e esp32dev -t upload
```

### プロジェクト構成

```
eye-spy/
├── src/
│   └── main.cpp          # ファームウェアの全ロジック
├── platformio.ini         # ビルド環境（atom-lite、esp32dev）
├── partitions_4mb.csv     # 4 MBフラッシュのパーティションテーブル
└── README.md
```

### platformio.ini

```ini
[env:atom-lite]
platform = espressif32
board = m5stick-c
framework = arduino

[env:esp32dev]
platform = espressif32
board = esp32dev
framework = arduino
```

*`atom-lite`環境は`m5stick-c`ボード定義を使います。同じESP32-PICO-D4チップを備え、GPIO 27 NeoPixelに対応するピン配置です。*

---

## 検出についての補足と実用上の制限

{{< figure src="eye-spy-m5stack-atom-lite-pocket-size.webp" alt="角砂糖ほどの大きさのM5Stack Atom Lite Eye Spyを2本の指で持った写真風イラストです。小型なサイズを示しています" >}}

### Eye Spyでできないこと

**5 GHz WiFi**: ESP32は**2.4 GHz専用**です。5 GHz帯だけで動作する監視カメラ、ALPRシステム、アクセスポイントは、WiFiスキャンでもプロミスキャスエンジンでも見えません。*最新のIPカメラの多くは5 GHzに加えて2.4 GHzにも対応しますが、5 GHzだけを使う設備は検出できません。*

**暗号化BLE**: 高性能な監視製品の中には、BLEアドバタイズを暗号化または難読化するものがあります。Eye Spyは、OUI、サービスUUID、メーカー情報などの識別可能な特徴を平文で送信する装置を検出します。*MACアドレスをローテーションする装置（一般消費者向けトラッカーで増えているプライバシー機能）はMACベースの検出を回避できます。* ローテーションが5分より長い間隔の場合、持続トラッカーだけで検出できる可能性があります。

**有線カメラ**: **Ethernetで接続され、WiFi無線を動作させないIPカメラは、Eye Spyが検出できる無線信号を発しません。** ネットワークに接続せずローカルだけに録画する隠しカメラもRF信号を出しません。

**通信範囲の限界**: 屋内でESP32のアンテナが受信できる強い信号の実用範囲は**20～40メートル**です。弱い信号や遮蔽物がある場合は短くなります。*通信範囲の端にある装置や強いRF遮蔽の背後にある装置は、スコアが付かなかったり、RSSIしきい値の−90 dBmを下回ったりする可能性があります。*

### 想定される誤検出

**近隣住宅の一般向けカメラ**: Ring、Nest、Wyze、Arlo、Reolinkのカメラは住宅街で一般的です。OUIは31件のカメラテーブルに含まれています。*住宅環境では、近隣のドアベルカメラによる黄色の注意表示（+3）が出る場合があります。* 技術的には*実際にカメラを検出している*ため誤検出ではありません。状況を踏まえて判断してください。

**小売店のiBeacon**: 大手小売店は、ほぼすべての店舗にiBeaconを導入しています。*ショッピングモールや食料品店に行くと、iBeacon検出（+2）が作動する可能性があります。* 店舗の追跡設備が実際に存在するため、デバイスは正しく動作しています。

**Ubiquiti UniFiインフラ**: Ubiquitiはネットワーク機器とセキュリティカメラの両方を製造し、OUIの範囲が重なるため、UniFiアクセスポイントも監視カメラのOUIテーブルに含まれています。*WiFiスキャンエンジンが、UniFiネットワーク機器のOUI一致に+3点を付ける場合があります。*

**Samsung SmartTagと一般向けデバイス**: SmartTagのUUID（`0xFD5A`）はSamsungに登録されたサービスです。*Samsung SmartTagは正当な個人用途もある一般向けトラッカーです。* 近くに所有者がいれば検出されます。

### 各スコアの実際の意味

| スコア | 現実に考えられる状況 |
|-------|-----------------------------|
| 6～10（🔴） | 信頼度の高い検出: 約30 m以内のAxonカメラ、OUIが一致するFlock Safetyカメラ、追跡パターンが確認されたAirTag、Remote IDを送信するドローン |
| 3～5（🟡） | 複数の一般向けトラッカー、近隣カメラの累積、Flockカメラの可能性、またはOpenDroneIDの単独検出 |
| 0～2（🟢） | 重大な監視シグネチャは未検出。通常の一般向け機器の通信はあるものの、しきい値を下回る状態 |

---

## 関連プロジェクトとの比較

Eye Spyは周囲の物理的な監視を対象にします。[ESP32 WiFi Canary: 2.4 GHz帯のパッシブ脅威検出](https://simeononsecurity.com/articles/esp32-wifi-canary-passive-wifi-threat-detection-2026/)は、自分のデバイスを狙うネットワーク層のWiFi攻撃を検出します。*異なる脅威モデルに対応する補完的なツールです。*

| 機能 | Eye Spy | ESP32 WiFi Canary |
|------------|---------|------------------|
| AirTag・トラッカー検出 | ✅ | ❌ |
| ALPR・Flockカメラ検出 | ✅ | ❌ |
| ボディカメラ検出 | ✅ | ❌ |
| ドローン（Remote ID）検出 | ✅ | ❌ |
| Evil twin AP検出 | ❌ | ✅ |
| Deauth攻撃検出 | ❌ | ✅ |
| セキュリティダウングレード検出 | ❌ | ✅ |
| ベースライン学習 | ❌ | ✅ |
| パッシブBLE | ✅ | ❌ |
| 同じハードウェアプラットフォーム | ✅ | ✅ |

両プロジェクトは、同じM5Stack Atom Liteハードウェア、LEDインジケーター、PlatformIOビルドシステムを使います。物理監視とネットワーク監視の両方を把握するには、別々のAtom Liteにそれぞれ書き込み、併用できます。

Eye Spyは、ALPR監視インフラに関心のあるユーザー向けに、[Flock You検出プロジェクト](https://simeononsecurity.com/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/)も補完します。

---

## 使用例

### 周囲の監視状況を把握する

Eye Spyの主な対象は、身近な場所にある監視インフラを把握したい人です。街を歩くとき、交差点を通過するとき、公共イベントに参加するときに、Eye Spyは複雑なRF分析を**リアルタイムのLED表示1つ**にまとめます。

### AirTagによるストーキングの検出

AirTagを使ったストーキングは、実際に報告されている問題です。Eye Spyの**追尾検出エンジン**（不明なBLE MACが5分以上にわたって3回以上検出されるかどうかを確認）は、Appleの既知のアドバタイズ形式に一致しない改造・独自トラッカーを対象にしています。AirTagの直接検出と合わせて、**追跡してくるトラッカーを2つの独立した方法で検出できます。**

### 賃貸物件・ホテル客室の確認

ホテルや賃貸物件に到着してEye Spyを動かすと、予期しないBLE・WiFi装置がないか初期確認できます。カメラのキーワードを含むSSIDやWiFiスキャンの監視OUIが見つかると、注意レベルの点数が加わります。*本格的なRFスイープの代わりにはなりません*が、物理点検にパッシブな確認手段を追加できます。

### ALPR設備・プライバシーの調査

監視インフラを記録する研究者、監視環境で働くジャーナリスト、プライバシー擁護者は、安価で携帯しやすい検出器としてEye Spyを使えます。シリアル出力には検出ごとのRSSIが記録されるため、簡易的なデータ収集装置としても利用できます。

### 旅行時のセキュリティ

WiFi Canaryと同様に、Eye Spyは旅行に適した形状です。Atom Liteはポケットに入れたり、バッグに取り付けたりできます。監視の多い空港、駅、公共イベントを移動するときに、操作せずに継続的なパッシブ監視を行えます。

---

## アーキテクチャの補足

### パッシブBLEが重要な理由

スキャン要求を送らないパッシブBLEスキャンを選ぶことは、セキュリティ上の意味があります。標準のBLEスキャンでは、スキャナーが各アドバタイザーに追加情報を求める**SCAN_REQ**パケットを送信します。*そのため、アクティブBLEスキャンは双方から観測できます。* スキャン対象の装置は、要求内のスキャナーアドレスを確認できます。

NimBLEのパッシブモードは、非指向アドバタイズパケット（ADV_IND、ADV_NONCONN_IND、ADV_SCAN_IND）だけを受信し、SCAN_REQを送信しません。**スキャン中、Eye SpyはBLE通信を一切送信しません。** 検出対象のAxonボディカメラ、Flock装置、AirTagがスキャナーの存在を確認したり、それに反応したりすることはありません。

### デバイス持続トラッカーの設計

不明な装置の持続トラッカーは、最大**50個のBLE MACアドレス**と初回・最終検出時刻を保持します。MACが5分以上の期間に3回以上現れると検出します。

登録上限50件と30分後の削除は、検出感度とESP32のRAM制限のバランスを取る設計上の選択です。*交通機関、会議、ショッピングモールなどBLE機器が多い環境では、一般向けデバイスで表がすぐに埋まる場合があります。* RSSIしきい値−90 dBmで遠方の装置を除外し、近くの持続的な信号源を追跡しやすくします。

### スコア減衰とクールダウンの関係

**120秒の再加点クールダウン**により、検出範囲に留まる装置が9秒ごとのBLEサイクルでスコアを積み上げるのを防ぎます。クールダウンがなければ、Flockカメラ1台で15秒ごとに+5点となり、数分で数百点に達します。

**60秒ごとに1点のスコア減衰**があるため、装置が範囲外に出てクールダウンの間に再検出されなければ、スコアが下がります。*再検出されない+5点の単発検出は5分でゼロになります。* 通常の移動で自然に問題なしの状態へ戻ります。

---

## 貢献とプロジェクトの状況

Eye SpyはApache-2.0ライセンスで[github.com/simeononsecurity/eye-spy](https://github.com/simeononsecurity/eye-spy)から入手できます。

今後の拡張候補:

- **OUIの追加**: 現場で新しいハードウェアMACが確認されたら、Flock SafetyとカメラのOUIテーブルを追加します。
- **BLEサービスUUIDの追加**: 新しいスマートグラス、カメラ、トラッカーに応じてUUIDを追加します。
- **持続トラッカーの調整**: 登録上限50件、検出回数3回、期間5分は変更可能な定数です。
- **シリアルデータの記録**: シリアル出力形式はプログラムによる解析を想定しています。外部ロガーで複数のEye Spyからの検出イベントを集約できます。

ファームウェアは`src/`ディレクトリ内の単一ファイル`main.cpp`にあるため、読み取り、監査、変更が簡単です。

---

## まとめ

Eye Spyは、範囲を絞った重要な問題に対処します。身の回りの物理環境には監視装置が増え、その多くが検出可能なRF信号を発しています。**15ドルのM5Stack Atom LiteでEye Spyファームウェアを動かすと、周囲を継続的にスキャンできます。** 複雑なBLEパケット分析やWiFi OUI検索を、RGB LED 1つの表示に変換します。

信頼度スコアは現実的な脅威の重み付けを反映します。法執行機関の活動中に近くのAxonボディカメラが検出されると+5点で赤く点灯し、店舗のiBeaconは+2点となって状況認識に寄与しますが、単独で警告を引き起こしません。スコアの減衰とクールダウンにより、一時的または低レベルの信号に過剰反応しません。

対監視、旅行時のセキュリティ、AirTagの検出、または単に近くで何かが自分を見ているか知りたい場合に、Eye Spyは実用的でオープンソースのパッシブツールとして、セキュリティ担当者の装備に加える価値があります。

**GitHub**: [github.com/simeononsecurity/eye-spy](https://github.com/simeononsecurity/eye-spy)

{{< centerbutton href="https://stscollective.com/discount/SIMEONONSECURITY" >}}
  Eye Spy検出器を購入して20%節約
{{< /centerbutton >}}
