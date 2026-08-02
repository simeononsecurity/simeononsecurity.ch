---
title: "Flock-You検出：カウンター監視セットアップガイド"
date: 2026-05-24
toc: true
draft: false
description: "ESP32ベースのハードウェアを使用してFlock Safety ALPRカメラを検出するオープンソースFlock-Youプロジェクトの包括的な技術ガイド。セットアップ手順、ファームウェアの詳細、購入オプションを含む。"
genre: ["セキュリティハードウェア", "カウンター監視", "プライバシー技術", "オープンソースプロジェクト", "ESP32開発", "WiFiモニタリング", "プライバシーツール", "デジタル権利", "ハードウェアハッキング", "ネットワークセキュリティ"]
tags: ["Flock-You Project", "ALPR Detection", "ESP32-S3", "WiFi OUI Detection", "Counter Surveillance Hardware", "Flock Safety Detection", "Open Source Security", "Privacy Hardware", "M5 Atom Lite", "OUI-SPY", "mesh-detect v2", "Promiscuous Mode WiFi", "802.11 Monitoring", "Colonel Panic Tech", "STS Collective", "Privacy Devices", "Surveillance Detection", "WiFi Scanning", "GitHub Project", "colonelpanichacks", "ESP32 Firmware", "Hardware Setup Guide", "DIY Privacy Tools", "Network Monitoring", "OUI Database", "Wildcard Probe Detection", "Frame Analysis", "ALPR Camera Detection", "Privacy Technology", "Detection Hardware", "Arduino ESP32", "Platform.io", "Embedded Systems", "RF Detection", "Signal Processing", "Privacy Engineering", "Counter Technology", "Security Research", "Privacy Advocacy", "Open Hardware", "Privacy Defense", "Detection Firmware", "Mobile Detection", "Privacy Projects", "Hardware Comparison"]
cover: "/img/cover/flock-you-detection-project-counter-surveillance-hardware-guide-2026.webp"
coverAlt: "前景にESP32ベースのデバイスが映り、WiFi信号をスキャンしている様子を示すイラスト。カラフルな波が異なる信号強度を表し、暗い背景に映えている。"
coverCaption: "ALPR監視カメラを検出するためのオープンソースハードウェアソリューション"
canonical: "https://simeononsecurity.com/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/"
---

**Flock-You検出デバイスの構築と使用に関する完全な技術ガイド**

## はじめに：オープンソースカウンター監視

**Flock-Youプロジェクト**は、Flock SafetyのALPR監視インフラを検出・マッピングするための**オープンソースのコミュニティ主導の取り組み**です。GitHubの**colonelpanichacks/flock-you**でホストされているこのプロジェクトは、手頃な価格のESP32ベースのハードウェアを使用して、**WiFiネットワーク署名**によってFlockカメラを識別します。

この包括的なガイドは、Flock検出の背後にある**技術的方法論**から、3つのハードウェアプラットフォームの**ステップバイステップのセットアップ手順**、**ファームウェアのインストール**、および**認定販売業者からの購入情報**まで、すべてをカバーしています。プライバシー支持者、セキュリティ研究者、または懸念を持つ市民であっても、このガイドにより、独自の検出デバイスを構築または購入できるようになります。

この技術が重要である理由と、より広い監視の状況については、コンパニオン記事をお読みください：**[Flock Safetyカメラ監視：普及、プライバシーの懸念、保護戦略](/articles/flock-safety-camera-surveillance-prevalence-privacy-protection-2026/)**。

Flockカメラがすでにどこにマッピングされているか確認したいですか？**[Flock Finder](https://simeononsecurity.github.io/flock-finder/)**は、WiGLE WiFiデータとOUIフィンガープリンティングを使用して、世界中の40,000以上の疑わしいFlock Safetyカメラをプロットするオープンソースツールです — 毎日更新されます。ソースは**[GitHub](https://github.com/simeononsecurity/flock-finder)**にあります。

______

## Flock-You検出方法論の理解

### 技術的基盤

Flock Safetyカメラには、接続性とリモート管理のための**組み込みWiFiモジュール**が含まれています。これらのモジュールは、**プロミスキャスWiFiモニタリングモード**で動作するデバイスによって検出可能な識別可能なネットワーク署名をブロードキャストします。Flock-Youプロジェクトは、この特性を以下の方法で活用します：

#### 1. WiFi OUI（組織固有識別子）検出

すべてのネットワークインターフェースには、以下で構成される**MACアドレス**があります：
- **最初の3バイト（24ビット）**：OUI、製造者を識別
- **最後の3バイト**：デバイス固有の識別子

研究者**@NitekryDPaul**と**DeFlockJoplin**コミュニティは、Flock Safetyカメラの展開に常に存在する**31の特定のOUI**を発見しました：

```
Primary Espressif OUIs (ESP32-based modules):
D4:AD:FC - Espressif Inc. (Common ESP32-S3)
AC:67:B2 - Espressif Inc. (ESP32-WROOM)
84:F3:EB - Espressif Inc. (ESP32-S3 variants)
B4:E6:2D - Espressif Inc. (ESP32-C3)
CC:DB:A7 - Espressif Inc. (ESP32-based)
24:0A:C4 - Espressif Inc. (ESP32-SOLO)
30:AE:A4 - Espressif Inc. (ESP32-WROVER)
94:B9:7E - Espressif Inc. (ESP32-based)
A4:CF:12 - Espressif Inc. (ESP32-S2)
C0:49:EF - Espressif Inc. (ESP32-C6)

Additional OUIs identified in Flock deployments:
[... 21 additional manufacturer OUIs ...]
```

検出デバイスがプロミスキャスモードでWiFiトラフィックをスキャンすると、**これらのOUIを持つフレームをブロードキャストしているデバイスを識別します**。

#### 2. ワイルドカードプローブリクエスト検出

Flockカメラは定期的に利用可能なネットワークを検索するために**ワイルドカードプローブリクエスト**を送信します。これらには独特の特徴があります：

- **802.11管理フレーム**：Type=0、Subtype=4
- **SSID情報要素**：Length=0（空/ワイルドカード）
- **フレーム構造**：プローブタイミングの予測可能なパターン
- **ベンダー固有のIE**：フレームペイロードの追加指標

検出ファームウェアはこれらの**プローブリクエストパターン**を分析して、単純なOUIマッチング以上のFlockカメラ識別の信頼性を高めます。

#### 3. プロミスキャスモードWiFiモニタリング

標準のWiFi動作は、デバイス宛てのフレームのみを受信します。**プロミスキャスモード**は範囲内のすべてのWiFiフレームをキャプチャします：

- **802.11フレーム構造**：addr1、addr2、addr3フィールドの分析
- **管理フレーム**：プローブリクエスト、ビーコンフレーム、アソシエーションリクエスト
- **データフレーム**：ネットワーク動作パターンを明らかにする
- **制御フレーム**：ACK、RTS、CTSはタイミング情報を提供

ESP32マイクロコントローラーは**esp_wifi API**を通じてプロミスキャスモードをサポートし、低コストの検出ハードウェアを可能にします。

#### 4. 信号強度分析

検出デバイスは**RSSI（受信信号強度インジケーター）**を測定して：
- 検出されたカメラへの**距離を推定**
- 複数の測定値で**場所を三角測量**
- 予想される信号特性に基づいて**誤検知をフィルタリング**
- カメラ密度の**ヒートマップを作成**

### 検出精度と誤検知

Flock-You方法論は高い精度を達成します：

- **真陽性率**：範囲内の確認されたFlockカメラに対して~95%
- **偽陽性率**：環境によって~5-10%
- **検出範囲**：障害物とアンテナによって15～90メートル
- **信頼スコアリング**：多要素分析により誤警報を低減

**一般的な誤検知源**：
- 他のIoTデバイスで使用されている**ESP32開発ボード**
- **商用ESP32ベース製品**（スマートホーム、センサー）
- 同様のコンポーネントを使用する**その他の監視カメラ**
- 技術者が操作する**WiFiテスト機器**

**軽減戦略**：
- **マルチシグネチャ検出**：OUI + プローブパターン + 物理検証の組み合わせ
- **場所の相関**：既知のカメラ位置との相互参照
- **視覚的確認**：電子検出後の物理的検査
- **コミュニティデータベース**：検出のクラウドソース検証

______

## ハードウェアプラットフォーム比較

Flock-You検出には3つの主要プラットフォームが利用可能で、それぞれに異なる利点があります：

### プラットフォーム概要テーブル

| 機能 | DIY ESP32 | M5 Atom Lite（事前フラッシュ済み） | OUI-SPY |
|---------|-----------|---------------------------|---------|
| **メーカー** | DIY / 複数ベンダー | STS Collective | Colonel Panic Tech |
| **価格** | $5-12 | $39.99 | $85 |
| **プロセッサ** | ESP32-WROOM | ESP32-PICO | ESP32-S3 |
| **すぐに使える** | いいえ（DIYビルド） | はい（事前フラッシュ済み） | はい（マルチモード） |
| **ディスプレイ** | オプション | RGB LED（5×5マトリックス） | なし |
| **バッテリー** | オプション | 外部推奨 | 付属なし |
| **GPS** | オプション | いいえ | いいえ |
| **アラート** | ブザー + LED | RGB LED（青=検出） | 内蔵ブザー |
| **データログ** | オプション | いいえ | いいえ |
| **エンクロージャー** | 3Dプリントまたはなし | コンパクトプラスチックモジュール | なし（ベアPCB） |
| **ファームウェア** | 手動フラッシュ | プリロードFlockYou | マルチモード（4ファームウェア） |
| **最適** | DIY愛好家、学習 | 予算内のすぐに使えるもの | 多目的検出 |
| **セットアップ難易度** | 中級-上級 | プラグアンドプレイ | プラグアンドプレイ |
| **重量** | 20-50g（様々） | 18g（ベア） | ~40g |
| **寸法** | 様々 | 24×24×14mm | PCBボード |

### 詳細プラットフォーム分析

#### 1. DIY ESP32ビルド（$5-12）

**概要**：オープンソースファームウェアを使用した標準ESP32開発ボードを使用する最も手頃なオプション。

**ハードウェア仕様**：
- **マイクロコントローラー**：ESP32-WROOM-32または類似（デュアルコア、240MHz）
- **WiFi**：802.11 b/g/n、プロミスキャスモード対応
- **メモリ**：520KB SRAM、4MB以上フラッシュ
- **ディスプレイ**：オプション（オンボードLEDで十分）
- **電源**：USB電源またはバッテリーパック
- **ブザー**：オプションのパッシブブザーモジュール（KY-006）
- **インジケーター**：オンボードLED + オプションブザー
- **拡張性**：ブレッドボード対応、簡単な改造

**ファームウェア**：**simeononsecurity/flock-you-esp32**のオープンソースフォーク：
- 標準ESP32ハードウェア（GPIO 25、2、17）用に修正
- Super Mario Bros.起動メロディ（ブザーの動作確認）
- 新規検出時に2回の素早い上昇ビープ
- トラッキングアクティブ時の10秒ハートビートビープ
- GPS wardrivingのためのFlaskダッシュボードサポート
- JSON、CSV、KML形式へのエクスポート

**ビルドオプション**：
- **LEDのみ（$5）**：ベアESP32 + USBケーブル、視覚的フィードバックのみ
- **ブレッドボード（$9-11）**：パッシブブザー + ブレッドボード + ジャンパーを追加、音声アラート
- **エンクロージャー付き（$10-12）**：スナップフィットリッド付き3Dプリントケースを追加

**メリット**：
- ✅ 最も安価なオプション（OUI-SPYと比べて85-95%のコスト削減）
- ✅ 完全にオープンソースで変更可能
- ✅ 広く利用可能なESP32ボードを使用
- ✅ 教育的、組み込みシステムを学習
- ✅ 豊富なドキュメントとガイド
- ✅ 3Dプリント可能なケースファイルが利用可能
- ✅ **プレミアムデバイスと同じ検出精度**

**デメリット**：
- ❌ DIY組み立てが必要（ハンダなしブレッドボードまたは3Dケース）
- ❌ 手動でのファームウェアフラッシュが必要
- ❌ 内蔵バッテリーなし（USB電源または外部パック）
- ❌ 基本的な音声フィードバックのみ（ディスプレイなし）
- ❌ コンポーネントの調達に時間がかかる

**最適**：メーカー、学生、予算の限られたプライバシー支持者、検出の仕組みを学びたい人、DIYプロジェクトを楽しむ人。

**コンポーネントの購入**：
- **Amazon**：「ESP32 DevKit」または「ESP32 Breadboard Kit」で検索
- **AliExpress/eBay**：バルク割引あり
- **Adafruit**：チュートリアル付きの厳選された高品質パーツ

**セットアップリソース**：
- **GitHubリポジトリ**：[github.com/simeononsecurity/flock-you-esp32](https://github.com/simeononsecurity/flock-you-esp32)
- **ビルドガイド**：10-15分でのハンダなし組み立て
- **ケースファイル**：OpenSCadパラメトリックデザイン + STLファイル

---

#### 2. STS CollectiveによるM5 Atom Lite事前フラッシュ済み（$39.99）

**概要**：事前フラッシュ済みのコンパクトな検出デバイス、箱から出してすぐに使用可能。

**ハードウェア仕様**：
- **マイクロコントローラー**：ESP32-PICO-D4（デュアルコア、240MHz）
- **WiFi**：802.11 b/g/n、プロミスキャス対応
- **メモリ**：520KB SRAM、4MBフラッシュ
- **ディスプレイ**：5×5 RGB LEDマトリックス（WS2812C NeoPixel）
- **電源**：USB-CまたはGroveコネクタ経由5V
- **バッテリー**：付属なし（外部USBパワーバンク推奨）
- **インジケーター**：プログラマブルRGB LED（青=検出）
- **ボタン**：プログラマブルボタン1個
- **I/O**：拡張用Groveコネクタ
- **サイズ**：ウルトラコンパクト24×24×14mm
- **エンクロージャー**：耐久性のあるプラスチックモジュール

**ファームウェア**：STS CollectiveによるカスタムFlockYouポート（プロプライエタリ）：
- プリロードされてすぐに使用可能
- Flockカメラ検出時の青色LEDアラート
- colonelpanichacks FlockYou研究に基づく
- セットアップやフラッシュ不要
- シンプルなプラグアンドプレイ操作
- オプションのダッシュボードサポート

**メリット**：
- ✅ 事前フラッシュ済み、技術的なセットアップ不要
- ✅ 手頃な価格のすぐに使えるソリューション
- ✅ 非常にコンパクトで携帯性が高い
- ✅ 実績のあるハードウェアプラットフォーム
- ✅ シンプルな青色LED = 検出
- ✅ USB-C電源（車、パワーバンク、ラップトップ）
- ✅ 品質保証済みベンダーサポート
- ✅ 通常価格$99.99、セール価格$39.99

**デメリット**：
- ❌ 内蔵バッテリーなし（USB電源が必要）
- ❌ 限定的なディスプレイ（RGB LEDのみ、スクリーンなし）
- ❌ *ファームウェアはプロプライエタリ、現時点ではオープンソースではない*
- ❌ コンピューター接続なしではデータログが不可
- ❌ シングルボタンで機能が制限される

**最適**：DIY作業なしに即座の検出を求めるユーザー、携帯性優先、シンプルなLEDフィードバックで満足できる人、既製品を求める予算意識の高い購入者。

**購入**：[stscollective.com/products/flockyou-m5-atom-lite-flock-camera-detector](https://stscollective.com/products/flockyou-m5-atom-lite-flock-camera-detector)

> 💰 **限定割引**：STS Collective製品を最大20%割引 — チェックアウト時にコード **SIMEONONSECURITY** を使用するか、[割引を適用してショッピングするにはここをクリック](https://stscollective.com/discount/SIMEONONSECURITY)。

---

#### 3. Colonel Panic TechによるOUI-SPY（$85）

**概要**：WiFiメニューから選択可能な4つの異なるファームウェアモードを備えたマルチモード監視検出ボード。

**ハードウェア仕様**：
- **マイクロコントローラー**：ESP32-S3デュアルコアXtensa LX7、8MBフラッシュ
- **WiFi**：802.11 b/g/n、プロミスキャスモード対応
- **メモリ**：8MBフラッシュ
- **ディスプレイ**：なし（LEDインジケーター付きベアPCB）
- **バッテリー**：付属なし
- **充電**：USB-C電源とプログラミング
- **ストレージ**：なし（検出専用モード）
- **インジケーター**：モード固有のメロディを持つ内蔵PWMブザー
- **ボタン**：モード切り替え用ブートボタン
- **アンテナ**：**切替可能**、オンボード2.4GHzセラミックまたはMMCXコネクタ経由の外部アンテナ
- **エンクロージャー**：なし（PCBアート付きベアPCB）
- **ユニークな特徴**：起動ごとのMAC無作為化

**ファームウェア**：OUI-SPY Unified Blue、**4つの選択可能モード**：
1. **Detectorモード**：OUIフィルタリング + Webコンフィグポータル付きマルチターゲットBLEスキャナー
2. **Foxhunterモード**：無線方向探知のシングルターゲットRSSI近接トラッカー
3. **Flock-Youモード**：GPS wardriving、JSON/CSV/KMLエクスポート付きFlock SafetyおよびRavenカメラ検出
4. **Sky Spyモード**：マルチドローントラッキング付きドローンRemoteID（OpenDroneID / ASTM F3411）検出器

**モード選択**：
- 192.168.4.1のWiFiブートメニュー
- セレクターに戻るにはBOOTボタンを2秒間押し続ける
- 電源サイクル間で最後のモードを記憶
- モードごとのブートメロディ（レトロチップチューンアラート）
- 検出専用操作（何も送信しない）

**メリット**：
- ✅ 1台のデバイスで4つのファームウェアモード
- ✅ 切替可能なアンテナ（オンボードまたは外部MMCX）
- ✅ カスタムブートメロディ付き内蔵ブザー
- ✅ プロフェッショナルグレードのPCBデザイン
- ✅ 多目的：ALPR、ドローン、BLE、RF方向探知
- ✅ 拡張範囲のための外部アンテナサポート
- ✅ オリジナルFlock-Youプロジェクト作成者から
- ✅ アクティブな開発とアップデート

**デメリット**：
- ❌ 単一目的のFlock検出では最高価格
- ❌ エンクロージャー付属なし（ベアPCB）
- ❌ 内蔵バッテリーなし
- ❌ ディスプレイなし（ほとんどのモードで音声フィードバックのみ）
- ❌ *基本的な検出には不必要な複雑さ*
- ❌ wardriving機能には外部GPSが必要

**最適**：多目的監視検出、1台のデバイスでドローン + ALPR + BLE検出を望むユーザー、RF方向探知アプリケーション、切替可能なアンテナと高度な機能を重視する人。

**購入**：[colonelpanic.tech](https://colonelpanic.tech/products/oui-spy)


______

## ステップバイステップのセットアップ手順

### セットアップガイド1：DIY ESP32ビルド

**完全な詳細手順については**、GitHubリポジトリをご覧ください：[github.com/simeononsecurity/flock-you-esp32](https://github.com/simeononsecurity/flock-you-esp32)

#### クイックスタート概要

1. **必要なハードウェア**：
   - ESP32 DevKitボード（$5-6）
   - USBケーブル（ボードによってMicro-USBまたはUSB-C）
   - オプション：パッシブブザーモジュール（KY-006）、ブレッドボード、ジャンパー
   - オプション：3Dプリントケース

2. **ソフトウェアセットアップ**：
   ```bash
   # Install PlatformIO
   pip install platformio
   
   # Clone repository
   git clone https://github.com/simeononsecurity/flock-you-esp32.git
   cd flock-you-esp32
   
   # Flash firmware
   pio run -t upload
   pio device monitor
   ```

3. **ハードウェア組み立て**（ブザー使用の場合）：
   - ブザープラス → GPIO 25
   - ブザーマイナス → GND
   - LEDインジケーター → GPIO 2（オンボード）
   - USB経由で電源供給

4. **起動確認**：
   - Super Mario Bros. 1-2メロディが再生される（ブザー接続の場合）
   - スキャン中にLEDが点滅
   - シリアルモニターに「Flock-You ESP32」の初期化が表示

5. **検出アラート**：
   - **新規検出**：2回の素早い上昇ビープ（2000→2800 Hz）
   - **ハートビート**：トラッキング中に10秒ごとに2回のビープ
   - **LED**：検出のたびに点滅

6. **GPS Wardriving**（オプション）：
   - USB経由でコンピューターに接続
   - Flaskダッシュボードを実行：`cd api && python flockyou.py`
   - http://localhost:5000を開く
   - GPSデバイスを接続またはブラウザの位置を使用
   - JSON/CSV/KMLに検出をエクスポート

**完全なビルドガイド、ケースファイル、トラブルシューティング**：GitHubのREADMEをご参照ください

---

### セットアップガイド2：M5 Atom Lite事前フラッシュ済み（STS Collective）

#### クイックスタート

1. **開封**：
   - M5 Atom Liteデバイス（FlockYouファームウェアで事前フラッシュ済み）
   - USB-Cケーブルの同梱については製品リストを確認

2. **電源オン**：
   - USB-C電源に接続（パワーバンク、車のUSB、ウォールアダプター、コンピューター）
   - デバイスが自動的に起動
   - RGB LEDマトリックスが初期化

3. **操作**：
   - **アイドル/スキャン**：LEDがスキャンパターンを表示
   - **検出**：Flockカメラ検出時にLEDが**青**に変わる
   - **ボタン**：手動で再スキャンまたはリセットするためにプレス

4. **ポータブル使用**：
   - USBバッテリーパックに接続（5000mAh = 約20時間）
   - カップホルダー、バッグ、ポケットに入れる
   - 半透明ケースを通してLEDが見える

5. **ダッシュボード接続**（オプション）：
   - USB-C経由でデバイスをコンピューターに接続
   - STS Collectiveの指示に従いFlockYouダッシュボードをインストール
   - ブラウザインターフェースでライブ検出を表示

**警告**：*これはプロプライエタリファームウェアです。オープンソースバージョンで再フラッシュすると、STSファームウェアが永久に削除されます。*

---

### セットアップガイド3：OUI-SPYマルチモードボード

#### 初期セットアップ

1. **パッケージ内容**：
   - OUI-SPYベアPCBボード
   - USB-Cケーブル
   - クイックスタートガイド

2. **初回電源オン**：
   - USB-C電源に接続（コンピューター、ウォールアダプター、またはパワーバンク）
   - デバイスがWiFiネットワークをブロードキャスト：`OUISPY-[ID]`
   - ブザーがモード固有の起動メロディを再生

3. **WiFiモード選択**：
   - 電話/コンピューターをOUI-SPY WiFiネットワークに接続
   - ブラウザで開く：`http://192.168.4.1`
   - Webインターフェースが4つのファームウェアモードを表示：
     1. **Detector** - マルチターゲットBLEスキャナー
     2. **Foxhunter** - RF方向探知  
     3. **Flock-You** - ALPRカメラ検出
     4. **Sky Spy** - ドローンRemoteID検出器
   - 希望のモードを選択して「Activate」をクリック

4. **Flock-Youモード操作**：
   - デバイスがFlock-Youモードで再起動
   - ブザーがFlock-You起動メロディを再生
   - 31の既知のOUIのスキャンを開始
   - **検出アラート**：ブザーが独特のパターンで鳴く
   - 電源サイクル間で最後のモードを記憶

5. **モード切り替え**：
   - **BOOTボタン**を2秒間押し続ける
   - デバイスがWiFiモードセレクターに戻る
   - WiFiに再接続して新しいモードを選択

#### 高度：外部アンテナ

6. **アンテナ切り替え**（拡張範囲のため）：
   - デフォルト：オンボードセラミックアンテナを使用
   - MMCXコネクターにMMCXアンテナを接続
   - ファームウェアが自動的に外部アンテナに切り替え
   - 長距離検出には指向性/八木アンテナを使用

#### マウンティング

7. **車両/固定設置**：
   - *エンクロージャー付属なし、マウント前にベアPCBの保護が必要*
   - オプション：
     - カスタムエンクロージャーを3Dプリント
     - ダッシュボードにベルクロマウント
     - 両面テープを使用
     - DIYプロジェクトボックス
   - 電源のためにUSB-Cポートをアクセス可能に保つ

#### データエクスポート（Flock-Youモード）

8. **GPS Wardriving**：
   - 外部GPSモジュールを接続（付属なし）
   - デバイスが座標付きで検出を記録
   - Webインターフェース経由でデータファイルをダウンロード
   - エクスポート形式：JSON、CSV、KML

**注意**：OUI-SPY Unified Blue固有のファームウェアアップデートとドキュメントについては、colonelpanic.techをご確認ください。

---



______

## 購入ガイドと販売業者情報

### 認定販売業者

#### Colonel Panic Tech (colonelpanic.tech)

**提供製品**：
- **OUI-SPY**（$85）：すぐに使えるFlock検出デバイス
- **DIYキット**（$55）：コンポーネント + PCB + 組み立てガイド
- **GPSモジュールアドオン**（$18）：互換性のあるGPS-6Mモジュール
- **アクセサリー**：アンテナ、ケース、バッテリーアップグレード

**Colonel Panicから購入する理由**：
- ✅ OUI-SPYハードウェア開発者から直接
- ✅ 最新ファームウェアがプリインストール済み
- ✅ テクニカルサポート付き
- ✅ オープンソース精神（回路図あり）
- ✅ アクティブなコミュニティフォーラム

**配送**：
- 米国内：3-5営業日
- 国際：7-14営業日
- $100以上の注文は送料無料

**保証**：90日間ハードウェア保証、生涯ファームウェアアップデート

**ウェブサイト**：[https://colonelpanic.tech](https://colonelpanic.tech)

---

#### STS Collective (stscollective.com)

**提供製品**：
- **M5 Atom Lite事前フラッシュ済み**（$39.99）：すぐに使えるFlock検出デバイス
- **アクセサリー**：さまざまなESP32プラットフォームと互換性あり

**STS Collectiveから購入する理由**：
- ✅ 事前フラッシュ済みですぐに使えるデバイス
- ✅ 品質保証とテスト
- ✅ 手頃な価格
- ✅ カスタマーサポート

**配送**：
- 米国内：2-4営業日（プライオリティメール）
- 国際：7-21営業日
- 速達オプションあり

**保証**：ハードウェアの標準保証

**ウェブサイト**：[https://stscollective.com](https://stscollective.com)

> 💰 **読者割引**：STS Collective製品を最大20%割引するには、コード **SIMEONONSECURITY** を使用 — [stscollective.com/discount/SIMEONONSECURITY](https://stscollective.com/discount/SIMEONONSECURITY)。

---

#### M5 Atom Liteのその他の購入先

**M5Stack公式ストア**：
- ウェブサイト：[shop.m5stack.com](https://shop.m5stack.com)
- 価格：ベアAtom Liteで$9.95
- アクセサリー：バッテリーモジュール、Groveセンサー、ケース
- 配送：国際、7-14日

**Amazon**：「M5Stack Atom Lite」で検索
- 価格：約$12-15（販売業者により異なる）
- Primeシッピング対応
- アクセサリー付きバンドルオプション

**Adafruit**：[adafruit.com](https://adafruit.com)
- 厳選された電子部品リテーラー
- 優れた学習リソース
- 米国拠点の速い配送

**注意**：*ベアのM5 Atom Liteを購入する場合、上記のDIYガイドに従って別途ファームウェアをインストールする必要があります。事前フラッシュ済みのSTS Collective版は別の製品です。*

### 価格比較まとめ

| デバイス | 基本価格 | オプションアドオン | 総投資 | セットアップ時間 |
|--------|------------|------------------|------------------|------------|
| **DIY ESP32** | $5-12 | 3Dケース、バッテリー | $5-20 | 15-30分 |
| **M5 Atom Lite** | $39.99 | バッテリーパック$10 | $40-50 | プラグアンドプレイ |
| **OUI-SPY** | $85 | 外部アンテナ$20、エンクロージャー | $85-115 | プラグアンドプレイ |

______

## 検出デバイスの使用：実際のシナリオ

### シナリオ1：毎日の通勤マッピング

**目的**：日常的な経路に沿ったFlockカメラの場所を記録する。

**セットアップ**：
- GPS機能付きデバイスを使用（GPSモジュール付きDIY ESP32またはGPS付きOUI-SPY）
- 自動ログを有効化
- 車両に取り付けるか、ポケットに携帯
- 誤検知を減らすために感度をMEDIUMに設定

**手順**：
1. 出発前に検出デバイスを起動
2. 通常のルートを走行
3. Flockカメラが検出されたときにデバイスがアラート
4. GPS座標が自動的に記録される
5. 家に帰ってデータをエクスポート
6. GPX/CSVをマッピングソフトウェアにインポート
7. 個人のカメラ位置マップを作成

**メリット**：
- 経路上の監視カバレッジの認識
- カメラのない代替ルートを特定
- コミュニティマッピングプロジェクトへの貢献
- 時間の経過による配置変更の追跡

### シナリオ2：近隣監視評価

**目的**：居住エリアのFlockカメラカバレッジを確認する。

**セットアップ**：
- ポータブルデバイスを使用（M5 Atom Lite、DIY ESP32、またはOUI-SPY）
- 徒歩または自転車でのサーベイ
- 主要な交差点での静止モニタリング

**手順**：
1. 近隣の通りを徒歩/自転車で移動
2. 各交差点で30-60秒間停止
3. 地図に検出を記録
4. 信号強度を使用して距離/方向を推定
5. 可能な場合、カメラの位置を視覚的に確認
6. 写真で調査結果を記録（公共エリアから）

**結果**：
- 地域の監視インフラの完全なマップ
- コミュニティ組織活動のための証拠
- 公開記録申請のためのデータ
- 個人のプライバシー判断のための認識

### シナリオ3：旅行プライバシー評価

**目的**：移動中の監視露出を理解する。

**セットアップ**：
- コンパクトなデバイスを携帯（ポケットのM5 Atom LiteまたはDIY ESP32）
- 継続的なログを有効化
- 旅行後にデータを確認

**用途**：
- 医療予約：クリニック近くの監視を評価
- 法律相談：弁護士事務所エリアのカバレッジを確認
- 宗教サービス：礼拝所近くのモニタリングを理解
- 政治活動：イベント/抗議での監視を評価
- 家庭の状況：居住地が監視されているか確認

### シナリオ4：コミュニティアドボカシー

**目的**：政策論争と公衆への認識向上のためのデータを提供する。

**応用**：
- 市議会会議で調査結果を発表
- 公開記録申請に含める
- プライバシー擁護組織と共有
- 研究プロジェクトに貢献
- 近隣団体に情報を提供

**データプレゼンテーション**：
- カメラ密度を示すヒートマップを作成
- カバレッジの格差に関するレポートを生成
- 配置拡大のタイムラインを作成
- 犯罪統計（またはその欠如）との相関

______

## 技術的詳細分析：コードの理解

### コア検出アルゴリズム（簡略化）

技術的な実装に興味がある方のために、検出ロジックの簡略化されたビューを示します：

```cpp
// Flock-You Detection Core (Conceptual - not full code)

// OUI Database (31 known Flock-associated OUIs)
const uint8_t FLOCK_OUI_LIST[][3] = {
    {0xD4, 0xAD, 0xFC}, // Espressif ESP32-S3
    {0xAC, 0x67, 0xB2}, // Espressif ESP32-WROOM
    {0x84, 0xF3, 0xEB}, // Espressif ESP32-S3 variant
    // ... 28 more OUIs ...
};

// Promiscuous mode callback
void wifi_sniffer_callback(void* buf, wifi_promiscuous_pkt_type_t type) {
    wifi_promiscuous_pkt_t *pkt = (wifi_promiscuous_pkt_t*)buf;
    
    // Extract MAC address from frame
    uint8_t *mac = pkt->payload + 10; // addr2 field position
    
    // Check against OUI database
    for (int i = 0; i < NUM_OUIS; i++) {
        if (memcmp(mac, FLOCK_OUI_LIST[i], 3) == 0) {
            // OUI match found
            int rssi = pkt->rx_ctrl.rssi;
            
            // Check signal strength threshold
            if (rssi > RSSI_THRESHOLD) {
                // Analyze frame for additional signatures
                if (is_wildcard_probe_request(pkt)) {
                    // High confidence detection
                    trigger_alert(mac, rssi, HIGH_CONFIDENCE);
                } else {
                    // OUI match only
                    trigger_alert(mac, rssi, MEDIUM_CONFIDENCE);
                }
            }
        }
    }
}

// Wildcard probe detection
bool is_wildcard_probe_request(wifi_promiscuous_pkt_t *pkt) {
    // Management frame, subtype probe request
    if ((pkt->payload[0] & 0x0F) != 0x04) return false;
    
    // Check for empty SSID IE (wildcard)
    // Position depends on frame structure
    uint8_t *ie = &pkt->payload[24]; // Start of IEs
    if (ie[0] == 0x00 && ie[1] == 0x00) {
        return true; // Wildcard probe
    }
    return false;
}
```

### 主要な技術的概念の説明

**プロミスキャスモード**：デバイス宛てのフレームのみを受信する代わりに、ESP32は範囲内のすべてのWiFiフレームをキャプチャします。**これは、検出器と通信していない近くのデバイスを検出するために不可欠です。**

**MACアドレス構造**：すべてのWiFiフレームには複数のMACアドレスが含まれます：
- `addr1`：受信者アドレス
- `addr2`：送信者アドレス（OUIを含む）
- `addr3`：最終宛先/ソースのアドレス

**RSSI（受信信号強度インジケーター）**：dBmでの信号強度（1ミリワットを基準とした負のデシベル）。典型的な値：
- -30 dBm：非常に強力（非常に近い）
- -50 dBm：強い信号
- -70 dBm：弱いが使用可能
- -90 dBm：非常に弱い（範囲の端）

**プローブリクエスト**：WiFiデバイスは利用可能なネットワークを発見するためにプローブリクエストを送信します。*ワイルドカードプローブ（空のSSID）は任意のネットワークを検索し、これはFlockカメラなどのIoTデバイスでは一般的であり、確実に検出可能です。*

______

## 一般的な問題のトラブルシューティング

### 問題：既知のカメラが近くにあるにもかかわらず検出されない

**考えられる原因**：
1. **カメラがオフライン/電源オフ**：Flockカメラは一時的に非アクティブになることがある
2. **信号がブロック**：建材がWiFiを吸収する（金属、コンクリート）
3. **範囲外**：障害物によって有効範囲は約30-90メートル
4. **ファームウェアの問題**：古いファームウェアでは新しいOUIバリアントを見逃す

**解決策**：
- カメラが見えて動作しているように見えることを確認（ソーラーパネル、ライト）
- 疑わしいカメラの位置に近づく
- 異なるアンテナの向きを試す
- 最新のFlock-Youファームウェアに更新
- **デバイスがアクティブにスキャンしていることを確認**（LED/ディスプレイのアクティビティを確認）

### 問題：誤検知が多すぎる

**考えられる原因**：
1. **ESP32デバイスの高密度**：スマートホーム、IoTデバイスは一般的
2. **感度が高すぎる**：遠い/無関係なデバイスを検出
3. **その他の監視カメラ**：多くがESP32モジュールを使用

**解決策**：
- 感度設定を下げる
- ワイルドカードプローブ検出を有効化（高い信頼度）
- 記録前に検出を物理的に確認
- 信号強度でフィルタリング（強い信号のみにアラート）
- 確認されたFlock OUIに焦点を当てるためにOUIデータベースを更新

### 問題：バッテリーが素早く消耗する

**考えられる原因**：
1. **継続的なスキャン**：スリープ/電力管理なし
2. **ディスプレイが常にオン**：画面が大量の電力を消費
3. **GPSアクティブ**：GPSモジュールは電力を大量に消費
4. **古いバッテリー**：Li-Poバッテリーは時間とともに劣化

**解決策**：
- パッシブスキャンモードを有効化（間欠的vs継続的）
- ディスプレイタイムアウトを設定
- マッピングが不要なときはGPSを無効化
- バッテリーを交換（OUI-SPY/mesh-detect v2は交換可能なバッテリーを搭載）
- 長時間セッションには外部バッテリーパックを使用

### 問題：GPSがロックを取得しない

**考えられる原因**：
1. **屋内使用**：GPSは空の視界が必要
2. **アンテナが接続されていない**：mesh-detect v2は外部アンテナの接続が必要
3. **コールドスタート**：最初のGPSロックには5-15分かかる
4. **干渉**：近くの電子機器が信号に干渉

**解決策**：
- 空が見える場所に移動
- アンテナが正しく接続されていることを確認（SMAコネクター）
- 初期ロックを待つ（その後のロックは速い）
- RF干渉源から離れる
- GPSが設定で有効になっていることを確認

### 問題：SDカードにデータが記録されない

**考えられる原因**：
1. **SDカードが未フォーマット**：FAT32形式でなければならない
2. **SDカードが満杯**：空き容量なし
3. **カードが検出されない**：完全に挿入されていない
4. **ファイルシステムの破損**：カードが損傷

**解決策**：
- **SDカードをFAT32でフォーマット**（互換性のため最大32GB）
- 古いログを削除するか、大容量カードを使用
- カードを完全に再挿入（クリック音がするはず）
- カードを再フォーマットするか、損傷している場合は交換
- デバイスがカードを認識していることを確認（メニューにSDのステータスが表示される）

______

## 法的および倫理的考慮事項

### 検出デバイスの法的地位

**WiFiスキャンの合法性**：
- ✅ **米国では合法**：受動的なWiFiモニタリング（受信のみ）は合法
- ✅ **傍受なし**：デバイスは公開でブロードキャストされたフレームのみを監視
- ✅ **復号なし**：データの復号やネットワークへの接続を試みない
- ✅ **ラジオスキャナーと同様**：警察スキャナーと同等の法的地位

**重要な区別**：
- ❌ **違法**：カメラ操作の積極的なジャミング/干渉
- ❌ **違法**：カメラシステムへのハッキングやアクセスの試み
- ❌ **違法**：物理的なカメラの破壊や改ざん
- ⚠️ **グレーゾーン**：*一部の管轄区域ではより厳しいプライバシー法がある。使用前に地域の規制を確認すること。*

**推奨**：**検出デバイスは認識のためだけです。カメラの操作に干渉しないでください。**

### 倫理的使用ガイドライン

**責任ある使用**：
- ✅ 監視の個人的な認識のために使用
- ✅ アドボカシーと政策議論のために記録
- ✅ プライバシー組織と集計データを共有
- ✅ コミュニティマッピングプロジェクトに貢献
- ✅ 監視インフラについて他の人を教育

**避けるべきこと**：
- ❌ 違法活動を促進するためにデータを使用
- ❌ カメラを設置した建物の所有者に嫌がらせ
- ❌ カメラの場所を確認するための不法侵入
- ❌ 監視インフラに対する自警行動

### プライバシーの考慮事項

**あなたのデータプライバシー**：
- **検出デバイスはあなたの位置を記録する**（GPSを介して）
- このデータを安全に保管する
- 法的手続きに関与している場合は**召喚状リスクに注意する**
- 機密のログファイルには暗号化を検討する
- クラウド接続デバイスのベンダープライバシーポリシーを理解する

**他者への配慮**：
- プライベートスペースで検出デバイスを使用する際は注意する
- 他の個人を追跡するために使用しない
- データ共有の倫理的影響を考慮する

______

## コミュニティとオープンソース開発

### Flock-Youプロジェクトへの貢献

Flock-Youプロジェクトはコミュニティの貢献で成り立っています：

**GitHubリポジトリ**：[github.com/colonelpanichacks/flock-you](https://github.com/colonelpanichacks/flock-you)

**貢献方法**：
1. **新しいOUIの発見**：新たに識別されたFlockカメラのOUIを提出
2. **コードの改善**：ファームウェア強化のためのプルリクエストを提出
3. **ハードウェア設計**：カスタム検出デバイスの設計を共有
4. **ドキュメント**：セットアップガイド、翻訳の改善
5. **テスト**：バグを報告し、デバイスを通じた機能を検証
6. **マッピング**：クラウドソースのカメラ位置データベースに貢献

### コミュニティリソース

**フォーラムとディスカッション**：
- **Reddit**：r/privacy、r/privacytoolsIO、活発なディスカッション
- **Discord**：Colonel Panic Techサーバー、リアルタイムチャット
- **GitHub Issues**：テクニカルサポートと機能リクエスト

**研究論文**：
- ALPR監視に関する学術研究
- プライバシー影響評価
- 検出デバイスの合法性の法的分析

**アドボカシー組織**：
- **Electronic Frontier Foundation** (EFF)：ALPRトラッキング
- **ACLU**：監視とプライバシーの権利
- **地域グループ**：DeFlockJoplinと同様のコミュニティイニシアチブ

### 今後の開発ロードマップ

**計画中の機能**（プロジェクトGitHubより）：
- **機械学習**：より高い精度のためのパターン認識
- **クラウド同期**：オプションのクラウドソース検出データベース
- **モバイルアプリ**：強化されたインターフェースのためのスマートフォン統合
- **追加検出モード**：その他の監視技術
- **リアルタイムアラート**：セルラー/WiFi経由のプッシュ通知

______

## 結論：技術によるプライバシーの支援

**Flock-You検出プロジェクト**は、カウンター監視技術の強力な民主化を表しています。毎月のストリーミングサブスクリプションのコスト以下で、個人は周囲の監視インフラを認識できます。**DIY ESP32ビルド（$5-12）**、**すぐに使えるM5 Atom Lite（$40）**、または**マルチモードOUI-SPY（$85）**のいずれかを選択しても、プライバシーの認識とデジタル自律性への投資をしています。

### 主なポイント

✅ **オープンソースのエンパワーメント**：コミュニティ主導の開発がアクセシビリティを確保
✅ **手頃な技術**：コンシューマーグレードのハードウェア（ESP32）で検出をアクセス可能に
✅ **複数のプラットフォーム**：さまざまな予算と技術スキルレベルのためのオプション
✅ **アクティブな開発**：新しいOUI署名と機能を含む定期的な更新
✅ **法的かつ倫理的**：受動的モニタリングは通信法に準拠
✅ **コミュニティへの恩恵**：公衆の認識と政策議論への貢献

### 次のステップ

1. **詳細を学ぶ**：検出が重要な理由：[Flock Safetyカメラ監視：普及とプライバシーの懸念](/articles/flock-safety-camera-surveillance-prevalence-privacy-protection-2026/)
2. **プラットフォームを選択**：ニーズと予算に合ったデバイスを決定
3. **ハードウェアを注文**：認定販売業者から購入
4. **セットアップと設定**：この記事の詳細ガイドに従う
5. **コミュニティに参加**：他のユーザーと関わり、調査結果を共有し、改善に貢献
6. **行動する**：アドボカシー、認識、情報に基づいた決断のためにデータを活用

ALPR監視の普及は、プライバシーのダイナミクスにおける重大な変化を表しています。Flock-Youのようなカウンター監視技術は重要な能力を提供します：**認識**。監視の範囲とスケールを理解するとき、私たちは移動、アドボカシー、公共スペースでのプライバシーの期待について情報に基づいた決断を下します。

**技術が広範な監視を可能にしました。技術はプライバシーを重視する人々も支援します。** Flock-Youプロジェクトは、市民的自由の保護におけるオープンソース協力の力の証明です。

______

## 関連記事

| 記事 | 説明 |
|---------|-------------|
| **[Flock Safetyカメラ監視：普及、プライバシーの懸念、保護戦略](/articles/flock-safety-camera-surveillance-prevalence-privacy-protection-2026/)** | Flock SafetyのALPRネットワーク、記録された悪用、コミュニティ組織リソース、および自己保護のためにできることの決定版ガイド |
| **[Flock Finder：近くの疑わしいFlock Safetyカメラをすべてマップ](/articles/flock-finder-alpr-surveillance-mapping-tool/)** | WiGLEデータとOUIフィンガープリンティングを使用して世界中の40,000以上の疑わしいFlockカメラを可視化するオープンソースFlock Finderツールの使い方 |
| **[IMSIキャッチャー検出デバイスにRayhunterをフラッシュする方法](/articles/how-to-flash-rayhunter-devices-complete-guide/)** | IMSIキャッチャーとスティングレイを検出するためのRayhunterファームウェアのフラッシュに関するステップバイステップガイド — ALPR検出を補完 |
| **[Orbic RCL400のDagShellカスタムファームウェア](/articles/dagshell-orbic-rcl400-custom-firmware-guide-2026/)** | 高度な携帯電話ネットワーク監視とIMSIキャッチャー検出のためのOrbic RCL400へのDagShellインストールの完全ガイド |
| **[Rayhunterデバイス比較2026](/articles/rayhunter-device-comparison-2026-complete-review/)** | カウンター監視ツールキットに最適なハードウェアを選ぶのに役立つRayhunterサポートデバイスの並べて比較 |

______

## 参考文献

1. [Flock-You GitHub Repository - colonelpanichacks](https://github.com/colonelpanichacks/flock-you)
2. [Flock Finder - Interactive ALPR Camera Map](https://simeononsecurity.github.io/flock-finder/)
3. [Flock Finder - GitHub Repository](https://github.com/simeononsecurity/flock-finder)
4. [Colonel Panic Tech - Official Vendor](https://colonelpanic.tech)
5. [STS Collective - M5 Atom Lite Pre-Flashed](https://stscollective.com)
4. [M5Stack Official Documentation](https://docs.m5stack.com/en/core/atom_lite)
5. [Espressif ESP32 Technical Documentation](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/)
6. [WiFi Promiscuous Mode Tutorial](https://esp32developer.com/wifi-promiscuous-mode)
7. [DeFlockJoplin Community Research](https://deflockjoplin.org/)
8. [Electronic Frontier Foundation - ALPR](https://www.eff.org/issues/automated-license-plate-readers)
9. [Arduino IDE Official Download](https://www.arduino.cc/en/software)
10. [Platform.io Documentation](https://docs.platformio.org/)
11. [OUI Database - IEEE Standards](https://standards.ieee.org/products-programs/regauth/)
12. [802.11 Frame Structure Reference](https://mrncciew.com/2014/10/08/802-11-mgmt-beacon-frame/)
