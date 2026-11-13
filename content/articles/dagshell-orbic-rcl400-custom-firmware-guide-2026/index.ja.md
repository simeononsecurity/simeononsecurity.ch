---
title: "Orbic RCL400向けDagShellカスタムファームウェアガイド 2026年版"
date: 2026-05-28
lastmod: 2026-11-13
toc: true
draft: false
description: "Orbic RCL400用DagShellファームウェアの技術ガイドです。インストール、プライバシーツール、ウォードライビング、調査の限界を説明します。"
genre: ["カスタムファームウェア", "モバイルセキュリティ", "プライバシーツール", "ネットワークセキュリティ", "ウォードライビング", "ペネトレーションテスト", "IoTハッキング", "セキュリティ調査", "ハードウェアハッキング", "プライバシー技術"]
tags: ["DagShell", "Orbic RCL400", "カスタムファームウェア", "ホットスポットハッキング", "プライバシーツール", "TTL補正", "MACアドレススプーフィング", "IMSIキャッチャー検出", "ウォードライビング", "GPS追跡", "Evil Twin攻撃", "Captive Portal", "DNSスニファー", "ARPスキャナー", "ポートスキャナー", "Raspberry Piコンパニオン", "Wi-Fiセキュリティ", "モバイルホットスポット", "ネットワーク監視", "ペネトレーションテスト", "セキュリティ調査", "Bluetoothスキャン", "デオーセンティケーション攻撃", "Wi-Fiスキャン", "OUI検索", "Wigleアップロード", "携帯電話基地局監視", "ATコマンド", "ファイアウォール管理", "広告ブロック", "TLS暗号化", "RayHunter連携", "STS Collective", "モバイルセキュリティラボ", "ネットワーク分析", "プライバシーファームウェア", "オープンソースセキュリティ", "ARMクロスコンパイル", "組み込みLinux", "セキュリティツールキット", "ハッキングツール", "レッドチーム", "ネットワーク探索"]
canonical: "https://simeononsecurity.com/articles/dagshell-orbic-rcl400-custom-firmware-guide-2026/"
cover: "/img/cover/dagshell-orbic-rcl400-custom-firmware-guide-2026.webp"
coverAlt: "鮮やかな緑色のインターフェースを表示するOrbic RCL400モバイルホットスポットのイラスト。濃紺の背景で、図表や地図などセキュリティツールを抽象的に表現した図が端末を囲んでいます。"
coverCaption: ""
---

**Orbic RCL400をモバイルセキュリティ調査ラボに変えましょう**

## はじめに: ハッカー向けホットスポット

**DagShell**は、**Orbic RCL400モバイルホットスポット**向けのオープンソースカスタムファームウェアです。一般的な携帯通信端末を、**セキュリティ調査とプライバシー保護のための携帯型ツールセット**に変えます。セキュリティ研究者の「dag」が、ターミナル風のインターフェースを備えたこのファームウェアを開発しました。黒い背景に緑色のハッカー風デザインで、**ハッキングツール、プライバシー機能、ネットワーク監視**を提供します。

この詳細ガイドでは、次の内容を説明します。
- **DagShellとは何か**、どのような機能があるか
- ウェブフラッシャーと手動インストールの**手順**
- **すべてのツールと機能**の詳細
- 拡張機能を利用するための**Raspberry Piコンパニオン**の設定
- **DagShellとRayHunterを組み合わせる理由**
- セキュリティ研究者やプライバシー擁護者向けの**実用例**
- **法律と倫理に関する考慮事項**

**概要:** Orbic RCL400でDagShellとRayHunterを組み合わせると、IMSIキャッチャー検出、ウォードライビング、ネットワーク分析、プライバシー保護のための**完全なモバイルセキュリティラボ**になります。

**ファームウェア導入済み端末:** この記事は**STS Collective**の協賛を受けています。同社では、RayHunterとDagShellを導入したOrbic RCL400ホットスポットをすぐ使える状態で販売しています: [stscollective.com/products/orbic-rcl400-rayhunter-dagshell-hotspot](https://stscollective.com/products/orbic-rcl400-rayhunter-dagshell-hotspot)

> 💰 **読者限定割引:** ファームウェア導入済みOrbic RCL400など、STS Collectiveの商品を最大20%割引で購入できます。支払い時にコード **SIMEONONSECURITY** を入力するか、[割引を適用して購入](https://stscollective.com/discount/SIMEONONSECURITY)してください。

______

## DagShellとは

### 概要

**DagShell**は、Orbic RCL400の標準ウェブインターフェースを**包括的なセキュリティツールキット**に置き換えるオープンソースファームウェアです。次の機能があります。

- ASCIIアートとハッカー風デザインを備えた**ターミナル風インターフェース**
- 自己署名証明書を使う**TLS 1.2+暗号化ウェブインターフェース**
- TTLマスキング、MACスプーフィング、DNSベースの広告ブロックなどの**プライバシーツール**
- アクティブ接続、ルーティングテーブル、DNSクエリの**ネットワーク監視**
- IMSIキャッチャー検出、ポートスキャン、ARP探索向けの**ハッキングツール**
- Evil Twin AP、キャプティブポータルフィッシング、デオーセンティケーション攻撃などの**攻撃機能**
- Wigle互換CSVエクスポートを使った**GPS追跡とウォードライビング**
- GPS、Bluetoothスキャン、Wi-Fi探索に使う**Raspberry Piコンパニオン**
- ブラウザ内ファイルマネージャーによる**ファイルシステムアクセス**
- ATコマンドによる**SMS機能**
- **永続化**。DagShellは起動時に自動実行されます

### 技術仕様

**プラットフォーム:** Orbic RCL400モバイルホットスポット\
**アーキテクチャ:** ARM Linux (カーネル3.18)\
**言語:** C/C++ (静的ARMバイナリ)\
**暗号化:** 自己署名証明書によるTLS 1.2+ (2階層PKI)\
**ウェブサーバー:** 独自の組み込みHTTPSサーバー (ポート8443)\
**インターフェース:** ブラウザベースのターミナルインターフェース\
**ライセンス:** MIT (オープンソース)\
**GitHub:** [github.com/dagnazty/DagShell](https://github.com/dagnazty/DagShell)

### ビジュアルデザイン

DagShellは**レトロなハッカー風デザイン**を採用しています。
- 各ページに**ASCIIロゴ**を表示
- **黒い背景に緑色の文字**を使ったMatrix風の配色
- **等幅フォント** (Fira Code)
- **走査線効果**と光る文字
- **ターミナルを意識したレイアウト**

{{< figure src="dagshell-orbic-rcl400-hacker-terminal-interface-feature-overview.webp" alt="Orbic RCL400で動作するDagShellカスタムファームウェア。緑色のターミナル画面、ASCIIアート、セキュリティツールメニューを表示" >}}

______

## 機能の詳細

### 🏠 ダッシュボード

**システム概要**:
- **稼働時間表示**。端末の起動後の経過時間
- **ATコマンドインターフェース**。上級者向けのモデム直接制御
- **クイックステータス**。IPアドレスと接続状態

**ATコマンド**でモデムを低レベルで制御できます。
```
Example AT Commands:
AT+CSQ       - Signal quality
AT+COPS?     - Current network operator  
AT+CREG?     - Network registration status
AT+CIMI      - Get IMSI (subscriber identity)
AT+CGSN      - Get IMEI (device identifier)
```

### 🌐 ネットワークツール

**現在のネットワーク情報**:
- **IPアドレスとインターフェース**の詳細
- **サブネットマスク、ゲートウェイ**、ブロードキャストアドレス
- **ネットワーク統計** (送受信パケット数)

**ルーティングテーブルビューアー**:
- すべてのネットワークルートを表示
- デフォルトゲートウェイの情報
- インターフェースの対応関係

**アクティブ接続モニター**:
- すべてのTCP/UDP接続をリアルタイムで一覧表示
- ローカルとリモートのIPアドレス
- ポート番号と接続状態
- **端末が通信している相手の監視**に役立ちます

### 🔒 プライバシー保護機能

#### TTL補正

**目的**: ホットスポット通信を通信事業者の検出から隠します。

**仕組み**:
- IPパケットの**Time To Live (TTL)**値を**65**に変更します
- 事業者はTTLの減少でテザリングを検出します (電話は64、接続端末は63)
- TTLを65に設定すると、**すべての通信が端末内の通信に見える**ようになります

**用途**: 事業者によるテザリング制限や速度制限の回避。

**コマンド**:
```bash
# TTL 修正を有効化
iptables -t mangle -A POSTROUTING -j TTL --ttl-set 65

# TTL 修正を無効化
iptables -t mangle -D POSTROUTING -j TTL --ttl-set 65
```

#### MACアドレススプーフィング

**目的**: プライバシー保護のため端末のMACアドレスをランダム化します。

**仕組み**:
- Wi-Fiインターフェース **wlan0** のMACアドレスを変更
- **ランダムなMACアドレス**を生成するか、任意の値を設定
- セッション間で端末を**追跡されにくく**します

**用途**: 接続先ネットワークによるMACアドレス追跡の防止。

**手順**:
1. インターフェースを停止
2. 新しいMACアドレスを適用
3. インターフェースを再度起動
4. 接続を再確立

#### DNSベースの広告ブロック

**目的**: DNSレベルで広告とトラッカーをブロックします。

**仕組み**:
- **ブロックリスト**で`/etc/hosts`ファイルを変更
- リスト内のドメインを**127.0.0.1** (localhost) に解決
- **接続中のすべての端末**の広告をブロック

**用途**: 各端末を個別設定せず、ネットワーク全体で広告をブロックします。

**ブロックリストの提供元**: 一般的な広告・追跡ドメイン。リストはカスタマイズできます。


### 📱 SMS管理

**SMSの送信**:
- モデムへの**ATコマンド**でテキストメッセージを送信
- **リモート通知**やテストに便利

**メッセージの表示**:
- Orbic標準の受信トレイへのリンク
- 受信したSMSを読む

**使用するATコマンド**:
```
AT+CMGS="PHONE_NUMBER"
Message text here^Z
```

### 🔧 ハッキングツール

#### IMSIキャッチャー検出器

**目的**: 携帯電話基地局の情報を監視し、**IMSIキャッチャー/Stingray**を示す異常を検出します。

**仕組み**:
- モデムから**基地局データ**を取得します:
  - **Cell ID** (基地局識別子)
  - **LAC** (位置エリアコード)
  - **MCC/MNC** (国・携帯通信網コード)
  - **信号強度** (RSSI)
  - **ネットワーク世代** (2G/3G/4G)
- **変化を記録**し、疑わしい基地局切り替えを検出
- **基準値を追跡**し、地域内の通常の基地局を把握

**検出の兆候**:
- 端末が静止しているのに**基地局が突然切り替わる**
- **2Gへダウングレード**する *(IMSIキャッチャーは暗号化を無効にするため2Gを強制することがあります)*
- **未知のCell ID**が現れる
- 偽基地局からの**弱い信号**
- **頻繁な再接続**

**RayHunterとの相乗効果**: DagShellは**基地局を監視**し、RayHunterはより高度な解析で**専用のIMSIキャッチャー検出**を行います (後述のセクションを参照)。

#### ポートスキャナー

**目的**: 対象IPアドレスの開放ポートをスキャンします。

**仕組み**:
- **TCP SYNスキャン**。対象ポートへSYNパケットを送信
- **タイムアウト検出**。ポートが開放、閉鎖、またはフィルター済みかを判定
- **範囲指定**。単一ポートまたはポート範囲をスキャン

**用途**:
- **ネットワーク偵察**
- **IoT端末の検出**
- ローカルネットワークの**セキュリティ監査**
- **サービスの識別**

**コマンド**:
```bash
# target のポート 1～1000 をスキャン
nc -zv -w 2 TARGET_IP 1-1000 2>&1
```

#### ファイアウォール管理

**目的**: iptablesでIPアドレスをブロックまたは解除します。

**仕組み**:
- 指定したIPとの送受信パケットをDROPする**iptablesルール**
- 保存すれば再起動後も有効な**永続ルール**
- **許可リスト/ブロックリスト**機能

**用途**:
- **悪意あるIPのブロック**
- **不正アクセスの防止**
- **トラフィック制御/フィルタリング**
- **ペアレンタルコントロール**

**コマンド**:
```bash
# IP をブロック
iptables -I INPUT -s IP_ADDRESS -j DROP
iptables -I OUTPUT -d IP_ADDRESS -j DROP

# IP のブロックを解除
iptables -D INPUT -s IP_ADDRESS -j DROP
iptables -D OUTPUT -d IP_ADDRESS -j DROP
```

### ⚔️ 攻撃ツール

**重要な法的免責事項**: これらのツールは**許可を得たセキュリティテストのみ**を目的としています。所有していないネットワークや、明示的な書面の許可を得ていないネットワークに対して使うことは、多くの法域で**違法**です (米国のComputer Fraud and Abuse Act、英国のComputer Misuse Actなど)。**自分のネットワーク**または**管理されたラボ環境**でのみ使用してください。

#### DNSスニファー

**目的**: 接続クライアントからのDNSクエリを記録します。

**仕組み**:
- DNSポート53を**iptablesでログ記録**
- **プロミスキャスモードは不要**
- ホットスポットのクライアントからのDNS要求をすべて記録
- クライアントが**アクセスしているウェブサイトやサービス**を把握

**用途** (許可を得た場合):
- **ネットワークトラフィック分析**
- **ペアレンタルモニタリング** (自分の家族)
- 自分の端末での**セキュリティ調査**
- **マルウェアの挙動分析**

*接続クライアントが訪問したドメインなどのメタデータを取得します。所有または管理するネットワークでのみ使用してください。*

#### ARPスキャナー

**目的**: ローカルネットワーク上の端末を検出します。

**仕組み**:
- サブネット内のすべてのIPに**ARP要求**を送信
- 端末は自身の**MACアドレス**を応答
- **OUI検索**でメーカーを特定 (Apple、Samsungなど)
- 稼働中の端末の**ネットワークマップ**を作成

**用途**:
- **ネットワーク資産の棚卸し**
- **未知の端末の検出**
- **BYODネットワーク分析**
- **IoT端末の検出**

**出力例**:
```
IP: 192.168.1.50
MAC: A4:83:E7:XX:XX:XX
Vendor: Apple, Inc.

IP: 192.168.1.75
MAC: 2C:54:91:XX:XX:XX
Vendor: Samsung Electronics
```

#### Traceroute

**目的**: 宛先までのネットワーク経路を可視化します。

**仕組み**:
- **TTLを段階的に増やした**パケットを送信
- 各ホップでTTLが減少し、**ICMP Time Exceeded**が返る
- 宛先までの**ルーターと経路**を表示
- 各ホップの**往復時間 (RTT)**を計測

**用途**:
- **ネットワークのトラブルシューティング**
- **経路分析**
- **遅延の診断**
- **ISPピアリングの調査**

#### Evil Twin AP

**目的**: 既存SSIDを複製した偽のWi-Fiアクセスポイントを作成します。

**仕組み**:
- **wlan1**を使用 (Piコンパニオンで利用可能な場合は2つ目のWi-Fiインターフェース)
- 対象ネットワークの**SSIDと暗号化方式**を複製
- 接続しようとするクライアントを**捕捉**
- 認証情報を取得するための**キャプティブポータル**を表示

**攻撃シナリオ** (ラボ環境):
1. 正規のWi-Fiネットワークをスキャン
2. 同じSSIDの**偽AP**を作成
3. **デオーセンティケーション攻撃**でクライアントを正規APから切断
4. クライアントが**偽AP**へ自動再接続
5. キャプティブポータルで認証情報を取得

*検出方法: 両方のAPが同時に見える場合、クライアントに**同じSSIDが重複して表示**されます。*

#### Captive Portal

**目的**: 認証情報を取得するためのフィッシングページテンプレートです。

**収録テンプレート**:
- ISPやホテル風の一般的な**Wi-Fiログインページ**
- Facebook、Twitter、Instagramに似せた**ソーシャルメディアログイン**
- **企業ログイン**ポータル
- **空港やコーヒーショップ**のWi-Fiゲート

**仕組み**:
1. Evil Twin APが**すべての通信**をポータルへ転送
2. クライアントに**ログインページ**を表示
3. クライアントが認証情報を入力
4. 認証情報を**ファイルに記録**
5. クライアントにインターネットを許可するか、エラーを表示

**教育目的**: **ソーシャルエンジニアリングのリスク**と、URL確認の重要性を示します。

### 📍 GPSトラッカーとウォードライビング

#### GPS機能

**GPSソース**: **Raspberry Piコンパニオンのみ**
- *Orbic RCL400には**GPSが内蔵されていません**。Piコンパニオンを使わない場合、位置情報は取得できません。*
- Piに**USB GPSドングル** (U-Blox 7チップセット) を接続
- **共有データファイル**を介してPiからOrbicへ座標を送信
- **ECEFから緯度・経度への変換**を自動処理

**ダッシュボード表示**:
- **緯度/経度** (10進度)
- 海抜高度
- **GPS測位状態** (精度)
- 5秒ごとの**自動更新**
- ブラウザの位置情報確認は表示されません (ブラウザAPIを使わないため)

**共有GPS状態**:
- GPSデータは**すべてのDagShellプロセス**で利用可能
- ウォードライビングはGPSを自動使用
- 各機能は互いに競合しません

#### ウォードライビングモード

**目的**: GPS座標付きでWi-Fiネットワークをスキャンし、マッピングします。

**仕組み**:
1. **有効なGPS測位**を待機 (0,0座標は記録しません)
2. 連続ループで5秒ごとにWi-Fiネットワークをスキャン
3. ネットワークデータを記録:
   - **SSID** (ネットワーク名)
   - **BSSID** (MACアドレス)
   - **暗号化方式** (WPA2、WPA3、Open)
   - **信号強度** (RSSI、dBm)
   - **チャンネル番号**
   - **GPS座標** (緯度/経度)
   - **タイムスタンプ**
4. **Wigle互換CSV**形式でエクスポート

**Wigleとの連携**:
- **WiGLE** (wigle.net) は世界規模のWi-Fiマッピングプロジェクトです
- DagShellのCSVはWiGLEへ**そのままアップロード可能**です
- 外部ツールなしで、Filesページから**ブラウザでアップロード**できます
- Wi-Fiの位置情報を含む**公開データベース**に情報を提供します

**用途**:
- **Wi-Fiカバレッジのマッピング**
- ISP向けの**ネットワーク調査**
- **信号強度分析**
- **セキュリティ調査** (オープンネットワークや弱い暗号化)
- **位置情報に基づく分析**

**CSV形式の例**:
```csv
MAC,SSID,AuthMode,FirstSeen,Channel,RSSI,Latitude,Longitude,AltitudeMeters
A1:B2:C3:D4:E5:F6,HomeNetwork,WPA2,2026-05-28 10:30:15,6,-45,40.7128,-74.0060,10
```

{{< figure src="dagshell-wardriving-gps-wifi-network-mapping-wigle-csv-export.webp" alt="DagShellのウォードライビングモード。GPS座標とスキャンしたSSID、BSSID、暗号化方式、信号強度をWigle互換CSVへ記録" >}}

### 🥧 Raspberry Piコンパニオン

**Raspberry Piコンパニオン**は、**外部ハードウェア**を使ってDagShellの機能を拡張します。

#### ハードウェア要件

**最低要件**:
- **Raspberry Pi 3B+**以降 *(Pi Zeroは周辺機器へ十分なUSB電力を供給できません)*
- **USB GPSドングル** (U-Blox 7チップセットを推奨)
- **電源** *(Piには別電源が必要です。OrbicのUSBポートだけでは電力が不足します)*

**オプション**:
- **Wi-Fiアダプター** (接続を維持しながらスキャンするための2つ目のインターフェース)
- **Bluetoothドングル** (Pi内蔵Bluetoothの性能が低い場合)

#### GPSモジュール (U-Blox 7)

**接続:** USB GPSドングルをPiに接続\
**プロトコル:** シリアル経由のNMEAセンテンス\
**変換:** PiがECEFを緯度/経度へ自動変換\
**データ共有:** Orbic上の**共有ファイル**にGPS座標を書き込み

**センテンスの解析**:
```
$GPGGA,123519,4807.038,N,01131.000,E,1,08,0.9,545.4,M,46.9,M,,*47
       |       |          |           |  |  |   |
       Time    Latitude   Longitude   Fix Sats  Altitude
```

#### Bluetoothスキャン (BLE)

**目的**: 近くのBluetooth端末を検出します。

**仕組み**:
- **BLEアドバタイズ**をスキャン
- **MACアドレス**を取得
- **OUI検索**でメーカーを特定
- **CSV形式**で記録

**リモート操作**:
- DagShellウェブUIからスキャンを**開始/停止**
- PiへSSH接続する必要はありません
- ステータスをリアルタイムで更新

**用途**:
- **端末の追跡と台数計測**
- **通行量分析**
- **Bluetooth端末の検出**
- **IoTセキュリティ調査**

**CSV出力**:
```csv
Timestamp,MAC,RSSI,Name,Manufacturer
2026-05-28 10:30:15,AA:BB:CC:DD:EE:FF,-65,Fitbit Charge,Fitbit Inc.
```

#### Wi-Fiスキャン

**目的**: PiでWi-Fiネットワークをスキャンし、Orbicへデータを送信します。

**利点**: **Orbicがホットスポットを維持**しながら、専用インターフェースでスキャンできます。

**仕組み**:
- Piで**2つ目のWi-Fiアダプター**、または接続に使っていない場合は内蔵Wi-Fiを使用
- **全チャンネル**をスキャン (2.4GHzは1～14、対応する場合は5GHzの36～165)
- 共有ストレージ経由で結果をOrbicへ送信
- DagShellが**ウォードライバーCSV**へ記録

**連携**:
- PiとOrbicがGPSタイムスタンプで**同期**
- 重複記録を防止
- **両方のスキャンデータ**を1つのログに統合

#### デオーセンティケーション攻撃

**目的**: (ラボでのテストとして) Wi-Fiネットワークからクライアントを切断します。

**仕組み**:
- **802.11デオーセンティケーションフレーム**を送信
- **APのMACアドレス**を偽装
- クライアントはAPから「切断」の通知を受信
- クライアントが**接続を切り、再接続を試行**

**操作方法**:
- **単発のデオーセンティケーション**: フレームを1回送信
- **継続的なデオーセンティケーション**: 再接続を妨害 (DoS)
- **リモート操作**: DagShellのスキャンページから実行

**用途** (許可を得た場合):
- 自分のネットワークからの**不正端末の除去**
- 許可を得た**ペネトレーションテスト**
- ラボでの**Evil Twin攻撃** (クライアントを偽APへ誘導)

**⚠️ 法的警告**: 所有していないネットワークへのデオーセンティケーション攻撃は**違法**です。FCC規則違反やCFAA違反に問われる可能性があります。

#### 自動起動サービス

**systemdサービス**: Piコンパニオンは起動時に自動実行します。

**サービスファイル** (`/etc/systemd/system/pi-companion.service`):
```ini
[Unit]
Description=DagShell Pi Companion
After=network.target

[Service]
ExecStart=/usr/bin/python3 /opt/dagshell/pi_companion.py
Restart=always
User=root

[Install]
WantedBy=multi-user.target
```

**コマンド**:
```bash
# 自動起動を有効化
sudo systemctl enable pi-companion

# サービスを開始
sudo systemctl start pi-companion

# 状態を確認
sudo systemctl status pi-companion
```

#### OUIデータベース

**目的**: MACアドレスからベンダー/メーカーを調べます。

**データベース**: [OUI Master Database](https://standards.ieee.org/products-programs/regauth/)のプレフィックス検索API。

**仕組み**:
- MACアドレスの**先頭3バイト** (OUIプレフィックス) を抽出
- APIへ照会: `api.example.com/oui/A4:83:E7`
- **メーカー名**を返す

**例**:
```
MAC: A4:83:E7:12:34:56
OUI: A4:83:E7
Vendor: Apple, Inc.
```

**連携機能**: ARPスキャナー、BLEスキャナー、Wi-Fiウォードライビングで使用します。

### 📁 ファイルエクスプローラー

**目的**: 端末内のファイルを閲覧、管理します。

**場所**: `/data/` ディレクトリー (書き込み可能なパーティション)

**機能**:
- ファイルとサブディレクトリーの**閲覧**
- ファイルをコンピューターへ**ダウンロード**
- (確認後に) ファイルを**削除**
- **ファイルサイズ**とタイムスタンプを表示

**よく使うファイル**:
- `wardrive_log.csv`：Wi-Fiスキャンデータ
- `bluetooth_scan.csv`：BLE端末データ
- `gps_track.gpx`：GPSトラック
- `dns_queries.log`：取得したDNSクエリ
- `arp_scan.txt`：ネットワーク端末一覧

**Wigleへのアップロード**:
- Filesページから**ブラウザーで直接アップロード**
- WiGLEアカウントで認証
- CSVを端末へダウンロードせずにアップロード

______

{{< stscollective-ad "rayhunter" >}}

## インストールガイド

### 前提条件

**ハードウェア**:
- **Orbic RCL400**モバイルホットスポット
- **コンピューター** (Windows、macOS、Linux)
- ファームウェアを直接書き込む場合は**USBケーブル**

**ソフトウェア**:
- `requests`と`cryptography`モジュールを含む**Python 3**
- **ウェブブラウザー** (Chrome、Firefox、Edge、Safari)

**オプション**:
- **Raspberry Pi 3B+**以降 (GPSや拡張機能用)
- **USB GPSドングル** (U-Blox 7チップセット)

### 方法1: ウェブフラッシャー (推奨)

**最も簡単な方法**です。コマンドラインは不要です。

**手順1**: DagShell Webflasherを開く
- URL: [dagnazty.github.io/DagShell/orbic.html](https://dagnazty.github.io/DagShell/orbic.html)

**手順2**: PKI証明書を生成
- **「Generate Certificates」**ボタンをクリック
- ブラウザーが**2階層PKI** (ルートCAとサーバー証明書) を生成
- **ファイルをダウンロード**: `root.der`と`server.der`

**手順3**: OrbicでRoot Shellを有効化
- OrbicのWi-Fiネットワークへ接続
- ウェブフォームに**管理者パスワード**を入力
- **「Enable Shell」**をクリック
- ウェブページがOrbic APIの脆弱性を利用して、**ポート24でRoot Shell**を開く

**手順4**: ファームウェアを導入
- **「Deploy DagShell」**ボタンをクリック
- スクリプトが次のファイルをアップロード:
  - `orbic_app` (メインのファームウェアバイナリー)
  - `root.der` (ルート証明書)
  - `server.der` (TLSサーバー証明書)
  - `dagshell_boot.sh` (永続化スクリプト)
- インストールに**2～3分**かかります

**手順5**: Orbicを再起動
- 端末の電源を入れ直す
- DagShellが起動時に自動実行

**手順6**: DagShellへアクセス
- ブラウザーで `https://192.168.1.1:8443/` を開く
- **セキュリティ警告**を承認 (自己署名証明書のため。これは想定された動作です)
- 表示された場合、既定の認証情報でログイン

### 方法2: 手動インストール

ソースからビルドしたい**上級者向け**です。

#### 手順1: 依存関係をインストール

**Windows**:
```powershell
# Python 3 をインストール
# python.org からダウンロード

# 必要なモジュールをインストール
pip install requests cryptography

# ARM クロスコンパイラーは gcc_win フォルダーに含まれます
```

**macOS**:
```bash
# Homebrew が未導入ならインストール
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Python 3 をインストール
brew install python3

# 必要なモジュールをインストール
pip3 install requests cryptography

# ARM ツールチェーンは gcc_mac フォルダーに含まれます
```

**Linux**:
```bash
# Python 3 と pip をインストール
sudo apt-get update
sudo apt-get install python3 python3-pip

# 必要なモジュールをインストール
pip3 install requests cryptography

# ARM クロスコンパイラーをインストール
sudo apt-get install gcc-arm-linux-gnueabihf
```

#### 手順2: リポジトリーをクローン

```bash
git clone https://github.com/dagnazty/DagShell.git
cd DagShell
```

#### 手順3: ファームウェアをビルド

**Windows**:
```powershell
cd orbic_fw_c
python gen_pki.py          # 証明書を生成
.\build.ps1                # ファームウェアをコンパイル
```

**macOS/Linux**:
```bash
cd orbic_fw_c
python3 gen_pki.py         # 証明書を生成
./build.sh                 # ファームウェアをコンパイル (BearSSL も自動ビルド)
```

**出力**: `orbic_app` (静的ARMバイナリー)とDER証明書ファイル。

**⚠️ macOSの注意**: `gcc_mac/`フォルダーには、Orbicのカーネル3.18との互換性を確保するため、**Linuxカーネル3.2**ヘッダーを対象に**crosstool-ng**でビルドした独自ARMツールチェーンがあります。*標準のHomebrew ARMコンパイラーは新しいカーネルを対象としているため、**動作しません**。*

#### 手順4: OrbicでRoot Shellを有効化

```bash
# Orbic WiFi に接続
# YOUR_ADMIN_PASSWORD を実際のパスワードに置き換え

python enable_shell.py YOUR_ADMIN_PASSWORD
```

このスクリプトはOrbicウェブAPIの脆弱性を利用して、**ポート24**でRoot Shellを開きます。

#### 手順5: ファームウェアを導入

```bash
python deploy_base64.py
```

このスクリプトは次をアップロードしてインストールします。
- `orbic_app`を`/data/orbic_app`へ
- 証明書を`/data/root.der`と`/data/server.der`へ
- 起動スクリプトを`/etc/rc.d/dagshell_boot.sh`へ

**永続化**: initスクリプトによって、再起動後もファームウェアが自動実行します。

#### 手順6: 再起動してアクセス

```bash
# Orbic を再起動 (電源を入れ直すか SSH を使用)
reboot

# 再起動後に DagShell にアクセス
# ブラウザー: https://192.168.1.1:8443/
```

### セキュリティ証明書の警告

DagShellへアクセスすると、**「安全ではありません」または「信頼されていません」**という警告が表示されます。

**デスクトップブラウザー**:
- **「詳細設定」**をクリック
- **「192.168.1.1に進む (安全ではありません)」**をクリック

**モバイルブラウザー**:
- **「詳細を表示」**をタップ
- **「このウェブサイトにアクセス」**をタップ

**警告が表示される理由**:
- 証明書は**自己署名**です (Let's Encryptのような信頼されたCAが発行したものではありません)
- 端末の信頼ストアにルート証明書がありません
- *カスタムファームウェアでは**想定された動作**であり、侵害を意味しません。*

**接続は本当に安全ですか?**:
- **はい**。接続は**TLS 1.2+で暗号化**されています
- データを傍受できません
- *証明書が公開CAの信頼チェーンにつながらないだけで、暗号化は有効です。*

**オプション**: `root.der`を端末の信頼ストアにインストールすると警告が消えます。

______

## Raspberry Piコンパニオンのセットアップ

全機能を使うには**必須ではありませんが、強く推奨します**。

### ハードウェアのセットアップ

**手順1**: 部品を用意
- **Raspberry Pi 3B+**以降 (35～55ドル)
- U-Blox 7チップセット搭載の**USB GPSドングル** (15～30ドル)
- Pi OS用の**16GB以上のmicroSDカード** (10ドル)
- Pi用**電源** (10ドル)

**手順2**: Raspberry Pi OSをインストール
```bash
# Raspberry Pi Imager をダウンロード
# https://www.raspberrypi.org/software/

# SD カードに Raspberry Pi OS Lite を書き込む
# Pi を起動してセットアップを完了
```

**手順3**: GPSドングルを接続
- USB GPSをPiに接続
- 認識を確認: `lsusb` (GPS端末が表示されるはずです)
- シリアルポートを確認: `ls /dev/ttyUSB*`または`/dev/ttyACM*`

### ソフトウェアのインストール

**手順1**: PiにDagShellリポジトリーをクローン

```bash
git clone https://github.com/dagnazty/DagShell.git
cd DagShell/pi_companion
```

**手順2**: 依存関係をインストール

```bash
# パッケージ一覧を更新
sudo apt-get update

# 必要なパッケージをインストール
sudo apt-get install python3-serial python3-requests gpsd gpsd-clients

# Python モジュールをインストール
pip3 install pyserial gps3 bluetooth pybluez
```

**手順3**: GPSデーモンを設定

```bash
# gpsd の設定を編集
sudo nano /etc/default/gpsd

# DEVICES 行に GPS のシリアルポートを設定
DEVICES="/dev/ttyUSB0"  # 必要に応じて調整

# gpsd を再起動
sudo systemctl restart gpsd

# GPS をテスト
cgps -s  # 約 30 秒後に衛星データが表示されることを確認
```

**手順4**: Piコンパニオンを設定

```bash
# 設定ファイルを編集
nano pi_companion/config.py

# Orbic の IP アドレスを設定
ORBIC_IP = "192.168.1.1"
ORBIC_PORT = "8443"

# GPS のシリアルポートを設定
GPS_DEVICE = "/dev/ttyUSB0"

# 保存して終了
```

**手順5**: systemdサービスをインストール

```bash
# サービスファイルをコピー
sudo cp pi_companion.service /etc/systemd/system/

# systemd を再読み込み
sudo systemctl daemon-reload

# 自動起動を有効化
sudo systemctl enable pi-companion

# サービスを開始
sudo systemctl start pi-companion

# 状態を確認
sudo systemctl status pi-companion
```

**手順6**: 通信を確認

```bash
# ログを確認
journalctl -u pi-companion -f

# GPS 座標が Orbic に送信されることを確認
```

### ネットワーク設定

**方法A**: Wi-Fi接続

```bash
# Pi が Orbic のホットスポットに接続
# wpa_supplicant の設定を編集
sudo nano /etc/wpa_supplicant/wpa_supplicant.conf

# ネットワークを追加
network={
    ssid="Orbic_SSID"
    psk="PASSWORD"
}

# WiFi を再起動
sudo systemctl restart networking
```

**方法B**: USB Ethernet (推奨)

- PiのUSBポートとOrbicのUSBポートを**USBケーブル**で接続
- Piで**USBガジェットモード**を有効化
- Piを**USB Ethernet端末**として動作させる
- *継続的なデータ転送ではWi-Fiより安定します。*
- PiはOrbic経由でインターネットに接続

**USBガジェットの設定**:
```bash
# config.txt を編集
sudo nano /boot/config.txt

# 末尾に追加
dtoverlay=dwc2

# cmdline.txt を編集
sudo nano /boot/cmdline.txt

# rootwait の後に追加
modules-load=dwc2,g_ether

# 再起動
sudo reboot
```

______

## DagShellとRayHunterを組み合わせる理由

{{< figure src="dagshell-rayhunter-complementary-capabilities.webp" alt="同じOrbic RCL400ホットスポットで動作するDagShellのWi-Fiウォードライビングとネットワーク攻撃ツール、RayHunterの携帯電話プロトコル異常検出機能を比較" >}}

### 相互補完する機能

**DagShell**と**RayHunter**は、モバイルセキュリティ調査の異なる側面をカバーする、**相互補完的な**セキュリティツールです。

| 機能 | DagShell | RayHunter |
|---------|----------|-----------|
| **IMSIキャッチャー検出** | 基本的な基地局監視 | 高度なパターン分析 |
| **GPS追跡** | あり (Pi経由) | あり (モデム経由) |
| **Wi-Fiウォードライビング** | あり | なし |
| **Bluetoothスキャン** | あり (Pi経由) | なし |
| **ネットワークツール** | あり (DNSスニファー、ARP、ポートスキャン) | なし |
| **攻撃ツール** | あり (Evil Twin、キャプティブポータル、デオーセンティケーション) | なし |
| **プライバシーツール** | あり (TTL補正、MACスプーフィング、広告ブロック) | 最小限 |
| **基地局データベース** | 基本 | 包括的 |
| **AI/ML分析** | なし | あり (異常検出) |
| **通信事業者プロトコル分析** | 限定的 | 詳細 (SS7/Diameter) |

### 連携して使うシナリオ

#### 1. **IMSIキャッチャーへの包括的な防御**

**シナリオ**: 監視の厳しい地域への旅行。

**DagShellの役割**:
- 基地局の変化を**リアルタイムで監視**
- 不審な切り替え時の**GPS位置を記録**
- 後で分析できるよう**基地局データを記録**

**RayHunterの役割**:
- 携帯電話プロトコルに対する**MLベースの異常検出**
- 高度な攻撃を対象にした**SS7/Diameterパケット検査**
- 比較用の**既知の正常な基地局データベース**

**組み合わせによる効果**: DagShellが**継続的な監視**を行い、RayHunterが**詳細な分析**を行います。

#### 2. **セキュリティを考慮したウォードライビング**

**シナリオ**: 市街地でWi-Fiネットワークをマッピング。

**DagShellの役割**:
- GPS座標付きで**Wi-Fiをスキャン**
- **ネットワーク分析** (信号強度、暗号化方式)
- マッピング用に**Wigle CSVをエクスポート**

**RayHunterの役割**:
- ウォードライビング中に**基地局を追跡**
- Wi-Fiスキャン中に**IMSIキャッチャーを検出**
- 携帯電話のセキュリティ侵害を**警告**

**組み合わせによる効果**: **携帯電話の安全性を把握しながら**ウォードライビングできます。

#### 3. **セキュリティ調査ラボ**

**シナリオ**: レッドチーム演習やペネトレーションテスト。

**DagShellの役割**:
- Wi-Fiテスト向けの**Evil Twin AP**
- ソーシャルエンジニアリングの実演向け**キャプティブポータル**
- 耐性テスト向けの**デオーセンティケーション攻撃**
- **ネットワーク偵察**ツール

**RayHunterの役割**:
- テスト中に自分が監視されていないか**検出**
- **携帯電話のセキュリティ**を把握
- テスト中の**対抗監視を防止**

**組み合わせによる効果**: 防御状況を把握しながら攻撃ツールを使えます。

#### 4. **プライバシーを重視した旅行**

**シナリオ**: 監視リスクのある環境にいるジャーナリストや活動家。

**DagShellの役割**:
- **TTLマスキング**でテザリングを隠す
- **MACスプーフィング**で端末の匿名性を高める
- **広告ブロック**で追跡を防ぐ
- **IMSIキャッチャーを監視**

**RayHunterの役割**:
- **高度なIMSIキャッチャー検出**
- **プロトコルレベルの攻撃検出**
- 携帯電話セキュリティの**アラート**

**組み合わせによる効果**: **多層防御**による高いプライバシー保護。

### 併用インストール

**ファームウェア導入済みモデル** (最も簡単):
- **STS Collective**から購入: [RayHunterとDagShellを導入済みのOrbic RCL400](https://stscollective.com/products/orbic-rcl400-rayhunter-dagshell-hotspot)
- 箱から出してすぐに**使用可能**
- 両方のファームウェアを**テスト・検証済み**
- **面倒なインストールは不要**

**DIYインストール**:
1. 先に**RayHunterを導入** ([RayHunterデバイスのフラッシュ方法ガイド](/articles/how-to-flash-rayhunter-devices-complete-guide/)を参照)
2. 次に**DagShellを導入** (両方を共存させられます)
3. **RayHunter**は標準ポートを使用
4. **DagShell**はポート8443を使用
5. それぞれ別のブラウザータブでアクセス

**競合はありません**:
- RayHunterはポート**80/443**を使用
- DagShellはポート**8443**を使用
- 相互に干渉しません
- **同時に実行**できます

DIYを避けたい場合は、ファームウェア導入済みの**[RayHunterとDagShellを搭載したOrbic RCL400](https://stscollective.com/products/orbic-rcl400-rayhunter-dagshell-hotspot)**が届いてすぐに使えます。STS Collectiveで読者コード **SIMEONONSECURITY** を使うと最大20%割引になります。

{{< centerbutton href="https://stscollective.com/discount/SIMEONONSECURITY" >}}
  ファームウェア導入済みRCL400を購入、20%割引
{{< /centerbutton >}}

______

## 実際の利用例

### 利用例1: セキュリティ研究者

**プロフィール**: Wi-Fiセキュリティ評価を行うペネトレーションテスター。

**使用するDagShellツール**:
- クライアントのネットワークをマッピングする**Wi-Fiウォードライビング**
- 端末を検出する**ARPスキャナー**
- サービスを特定する**ポートスキャナー**
- ソーシャルエンジニアリング耐性を試す**Evil Twin/キャプティブポータル**
- 結果を取り出す**ファイルエクスプローラー**

**作業の流れ**:
1. クライアント施設の周囲を走行
2. Wi-Fiのカバレッジをウォードライビングでマッピング
3. 許可を得てクライアントのネットワークのEvil Twinを作成
4. クライアントの接続試行を監視
5. 収集データを使ってレポートを作成

**RayHunterとの連携**: 評価中に研究者が監視されていないことを確認します。

### 利用例2: プライバシー擁護者

**プロフィール**: 海外を移動するジャーナリスト。

**使用するDagShellツール**:
- 事業者の制限を回避する**TTL補正**
- 端末を匿名化する**MACスプーフィング**
- 監視に備える**IMSIキャッチャー検出器**
- 端末から情報が漏れていないか確認する**DNSスニファー**
- 追跡を防ぐ**広告ブロック**

**作業の流れ**:
1. 端末を使う前にTTL補正を有効化
2. MACアドレスをランダム化
3. IMSIキャッチャー検出器を常時監視
4. 接続中のすべての端末で広告ブロックを使用
5. 不審な携帯通信の動作を記録

**RayHunterとの連携**: 基本監視を超える高度なIMSIキャッチャー検出を行います。

### 利用例3: ネットワーク管理者

**プロフィール**: 複数施設を管理するIT管理者。

**使用するDagShellツール**:
- カバレッジを確認する**Wi-Fiウォードライビング**
- 端末一覧を作る**ARPスキャナー**
- セキュリティ監査向けの**ポートスキャナー**
- 不正通信を確認する**アクティブ接続モニター**
- IPをブロックする**ファイアウォール管理**

**作業の流れ**:
1. 施設の周囲をウォードライビングし、Wi-Fiカバレッジを確認
2. ARPスキャンですべてのネットワーク端末を検出
3. サーバーをポートスキャンして公開サービスを確認
4. ファイアウォールで悪意のあるIPをブロック
5. 記録用にレポートをエクスポート

**RayHunterとの連携**: モバイル端末がある施設の携帯電話セキュリティを監視します。

### 利用例4: IoTセキュリティ研究者

**プロフィール**: IoT端末のセキュリティを分析する研究者。

**使用するDagShellツール**:
- OUI検索付き**ARPスキャナー**でIoT端末を特定
- 開放サービスを見つける**ポートスキャナー**
- IoT通信のパターンを取得する**DNSスニファー**
- BLE対応IoT端末向けの**Bluetoothスキャナー** (Pi)
- 接続を分析する**Traceroute**

**作業の流れ**:
1. テスト環境にOrbicとPiを配置
2. ARPスキャンでIoT端末を検出
3. ポートスキャンで脆弱なサービスを探す
4. BLEスキャンでBluetooth IoT端末を検出
5. DNSスニファーで端末が外部へ通信する動作を分析
6. 脆弱性を記録

**RayHunterとの連携**: IoT端末の携帯通信接続を検出し、異常を監視します。

{{< figure src="dagshell-rayhunter-combined-mobile-security-research-use-cases.webp" alt="DagShellとRayHunterを組み合わせた4つの利用例。セキュリティ研究者、プライバシー擁護者、ネットワーク管理者、IoT研究者" >}}

______

## 法律と倫理に関する考慮事項

### 法的枠組み

**DagShellのようなツールの使用には法的なグレーゾーンがあります**。

**合法的な使用**:
✅ **自分のネットワーク**。自分の端末とネットワークをテストする\
✅ **許可されたテスト**。他人のシステムをテストする前に書面で許可を得る\
✅ **教育目的**。隔離されたラボ環境で学習する\
✅ **プライバシー保護**。自分の端末でTTL補正やMACスプーフィングを使う\
✅ **セキュリティ調査**。脆弱性を責任を持って開示する

**違法な使用**:
❌ **不正アクセス**。自分が所有していないネットワークへの攻撃 (CFAA違反)\
❌ 他人のネットワークへの**デオーセンティケーション攻撃** (FCC規則違反、重罪の可能性)\
❌ 公衆への**Evil Twin攻撃** (通信詐欺、個人情報の盗用)\
❌ 同意を得ずに他人の**DNS通信を盗聴**\
❌ 詐欺を行うための**セキュリティ対策回避**

### 知っておくべき法律

**米国**:
- **Computer Fraud and Abuse Act (CFAA)**：コンピューターやネットワークへの不正アクセス
- **Wiretap Act**：電子通信の傍受
- **FCC規則**：デオーセンティケーション攻撃などの無線周波数干渉

**英国**:
- **Computer Misuse Act 1990**：CFAAに類似
- **Regulation of Investigatory Powers Act (RIPA)**：傍受に関する制限

**欧州連合**:
- **GDPR**：BLEやWi-Fiで識別可能なデータをスキャンする場合を含むデータ保護
- *各国の規制や執行状況は異なります。*

### 倫理ガイドライン

**実施すること**:
- ✅ **自分の端末**とネットワークで使用
- ✅ 他人のシステムをテストする前に**書面で許可を得る**
- ✅ 脆弱性を発見したら**責任を持って開示する**
- ✅ 管理された環境で**教育目的に使用する**
- ✅ **自分のプライバシー**を保護する

**実施しないこと**:
- ❌ 所有していないネットワークを攻撃する
- ❌ 見知らぬ人の認証情報を収集する
- ❌ 重要インフラの妨害
- ❌ 悪意をもってツールを使う
- ❌ 取得したデータを配布する

### 責任ある使用に関する声明

DagShellは**セキュリティ調査とプライバシー保護のツール**です。機能は**Kali Linux**、**WiFi Pineapple**、**HackRF**などの専門的なペネトレーションテストツールに似ています。

**意図が重要です**。**悪意のあるハッカー**と**セキュリティ専門家**が同じツールを使うことがあります。違いは次の点です。
- **許可** (テストの承認)
- **意図** (セキュリティ改善か、危害を与えるか)
- **開示** (調査結果を報告するか、悪用するか)

DagShellを**責任を持って**、**倫理的に**使ってください。*行為が合法か分からない場合は、作業を止めて弁護士に相談してください。*

{{< figure src="dagshell-legal-ethical-security-research-responsible-use.webp" alt="DagShellを使うセキュリティ調査の法的・倫理的枠組み。許可された使用、許可されない使用、関連法を表示" >}}

______

## トラブルシューティング

### インストール時の問題

**問題**: `enable_shell.py`が接続に失敗する

**解決方法**:
- **OrbicのWi-Fi**に接続していることを確認
- IPアドレスが**192.168.1.1** (既定値) であることを確認
- 管理者パスワードを再入力 (大文字と小文字を区別)
- ポート80にアクセスできるか確認: `telnet 192.168.1.1 80`

**問題**: ファームウェアのアップロードに失敗する

**解決方法**:
- まずRoot Shellを有効化 (`enable_shell.py`が成功していること)
- ネットワークが安定していることを確認 (可能なら有線接続を使用)
- `deploy_base64.py`の代わりに`deploy_net.py`を試す
- `/data`パーティションの空き容量を確認: `df -h /data`

**問題**: 証明書の警告が消えない

**解決方法**:
- *自己署名証明書では**通常の動作**です。接続は引き続き暗号化されています。*
- 毎回「詳細設定」->「続行」をクリック
- **オプション**: `root.der`を端末の信頼ストアへインストール (上級者向け)

### 実行時の問題

**問題**: 起動時にDagShellが開始しない

**解決方法**:
- 起動スクリプトを確認: `ls -la /etc/rc.d/dagshell_boot.sh`
- 実行可能か確認: `chmod +x /etc/rc.d/dagshell_boot.sh`
- ログを確認: `logread | grep dagshell`
- 手動で起動: `/data/orbic_app &`

**問題**: GPSが動作しない

**解決方法**:
- **Piコンパニオン**が動作しているか確認: `systemctl status pi-companion`
- GPSが衛星を捕捉しているか確認: `cgps -s` (Pi上で実行)
- GPSドングルが接続されているか確認: `lsusb`
- *コールドスタートではGPS測位まで5～10分待ちます。初回起動時は屋外でも時間がかかります。*

**問題**: ウォードライビングの記録が行われない

**解決方法**:
- 開始前にGPS測位を確認
- `/data`への書き込み権限を確認
- CSVファイルが作成されているか確認: `ls -la /data/wardrive_log.csv`
- Wi-Fiインターフェースが起動しているか確認: `ifconfig wlan0`

**問題**: PiコンパニオンがOrbicと通信しない

**解決方法**:
- ネットワーク接続を確認: `ping 192.168.1.1`
- 設定ファイルのIPが正しいことを確認
- ポート8443が開いているか確認: `telnet 192.168.1.1 8443`
- Piコンパニオンのログを確認: `journalctl -u pi-companion`

### パフォーマンスの問題

**問題**: ウェブインターフェースが遅い、または反応しない

**解決方法**:
- ブラウザーのキャッシュを消去
- ブラウザーの拡張機能を無効化 (広告ブロッカーが干渉する場合があります)
- Wi-Fiではなく**有線**でOrbicに接続
- DagShellを再起動: `killall orbic_app && /data/orbic_app &`

**問題**: ウォードライビングのスキャンに時間がかかる

**解決方法**:
- 設定でスキャン間隔を長くする (頻度と性能を調整)
- スキャンするチャンネル数を減らす
- *GPS測位が弱いとスキャンが遅くなります。有効な座標が得られるまで記録を待つためです。*

{{< figure src="dagshell-troubleshooting-installation-gps-wardriving-common-issues.webp" alt="DagShellのトラブルシューティング。インストール、GPS、ウォードライビングの問題と手順別の解決方法" >}}


______

## 詳細設定

### DagShellのカスタマイズ

**ソースコードの変更**:
- `orbic_fw_c/`ディレクトリー内のファイルを編集
- `build.sh`または`build.ps1`で再ビルド
- ファームウェアを再導入

**カスタムページの追加**:
- DagShellはC++コードに埋め込んだHTMLを使用
- `main.cpp`を編集して新しいルートを追加
- 再コンパイルして導入

**独自証明書**:
- `gen_pki.py`で独自PKIを生成
- または**OpenSSL**を使って証明書を作成
- `root.der`と`server.der`を置き換え

### 他のツールとの連携

**Wiresharkへのデータエクスポート**:
```bash
# pcap ファイルを取得
tcpdump -i wlan0 -w /data/capture.pcap

# ファイルブラウザーでダウンロード
# PC の Wireshark で開く
```

**GPSトラックをQGISにインポート**:
```bash
# GPX 形式でエクスポート
python gps_to_gpx.py /data/gps_coords.txt

# QGIS にベクターレイヤーとしてインポート
```

**外部データベースとの同期**:
```python
# wardrive データを MySQL にアップロードするカスタムスクリプト
import mysql.connector
import csv

conn = mysql.connector.connect(
    host="your_server",
    user="username",
    password="password",
    database="wardriving"
)

with open('/data/wardrive_log.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        cursor.execute("INSERT INTO networks (ssid, bssid, lat, lon) VALUES (%s, %s, %s, %s)",
                      (row['SSID'], row['MAC'], row['Latitude'], row['Longitude']))
conn.commit()
```

### パフォーマンス調整

**スキャン速度の最適化**:
```bash
# wardrive のスキャン間隔を編集
# DagShell の Web UI で 5 秒から 3 秒に変更してスキャンを高速化
# その代わり CPU 使用率が上がり、一部のネットワークを見逃す可能性があります
```

**バッテリーの最適化** (バッテリーパックを使用する場合):
```bash
# Orbic の画面の明るさを下げる
# 使わない機能を無効化 (不要なときは BT と GPS)
# wardrive セッションの間はスリープモードを使用
```

______

## 他の製品との比較

### DagShellとWiFi Pineapple

| 機能 | DagShell (Orbic RCL400) | WiFi Pineapple |
|---------|------------------------|----------------|
| **価格** | 60～80ドル+端末 | 99～299ドル |
| **携帯電話通信** | ✅ 4G LTE内蔵 | ❌ Wi-Fiのみ |
| **GPS** | ✅ Piコンパニオン経由 | ⚠️ USBドングル経由 |
| **Evil Twin** | ✅ 対応 | ✅ 対応 |
| **キャプティブポータル** | ✅ 対応 | ✅ 対応 |
| **デオーセンティケーション** | ✅ 対応 (Pi経由) | ✅ 対応 |
| **ウォードライビング** | ✅ 対応 | ✅ 対応 |
| **IMSI検出** | ✅ 基本的 | ❌ 非対応 |
| **携帯性** | ✅ 非常に高い | ⚠️ 普通 |
| **バッテリー** | ✅ 内蔵 | ⚠️ 外部電源が必要 |
| **習得の難しさ** | 普通 | 低い (洗練されたUI) |

**おすすめ**: **モバイル携帯電話セキュリティ**にはDagShell、簡単なUIで行う**Wi-Fi限定テスト**にはPineapple。

### DagShellとPi上のKali Linux

| 機能 | DagShell | Pi上のKali |
|---------|----------|-----------|
| **セットアップ時間** | 15分 | 2～3時間 |
| **携帯電話LTE** | ✅ 内蔵 | ❌ USBモデムが必要 |
| **ウェブインターフェース** | ✅ あり | ⚠️ 制限あり (VNC/SSHが必要) |
| **ツール数** | 約15 | 600以上 |
| **専門分野** | モバイルセキュリティ | 汎用ペネトレーションテスト |
| **携帯性** | ✅ ポケットサイズ | ⚠️ 画面と電源が必要 |
| **バッテリー駆動時間** | 8～10時間 | 2～4時間 |

**おすすめ**: **モバイル特化の作業**にはDagShell、**総合的なツールキット**にはKali。

### DagShellとOrbic標準ファームウェア

| 機能 | DagShell | 標準ファームウェア |
|---------|----------|----------------|
| **セキュリティツール** | ✅ 豊富 | ❌ なし |
| **プライバシー機能** | ✅ あり | ❌ 最小限 |
| **カスタマイズ** | ✅ 完全に可能 | ❌ ロック済み |
| **ウォードライビング** | ✅ 対応 | ❌ 非対応 |
| **GPS** | ✅ あり (Pi経由) | ❌ なし |
| **オープンソース** | ✅ はい | ❌ プロプライエタリー |
| **サポート** | ⚠️ コミュニティ | ✅ 公式 |
| **安定性** | ⚠️ ベータ版 | ✅ 製品版 |

**おすすめ**: **研究者**にはDagShell、**一般利用**には標準ファームウェア。

______

## 結論: 究極のモバイルラボ

**DagShell**は、シンプルな**Orbic RCL400ホットスポット**を次の機能を備えた**強力なモバイルセキュリティラボ**へ変えます。

✅ **プライバシー保護** (TTLマスキング、MACスプーフィング、広告ブロック)\
✅ **ネットワーク監視** (接続、DNS、ルーティング)\
✅ **ハッキングツール** (IMSI検出、ポートスキャン、ARP探索)\
✅ **攻撃機能** (Evil Twin、キャプティブポータル、デオーセンティケーション)\
✅ Wigle連携の**GPSウォードライビング**\
✅ **Raspberry Piによる拡張** (BLE、Wi-Fi、GPS)\
✅ **携帯型、バッテリー駆動**\
✅ **オープンソースでカスタマイズ可能**

### RayHunterとの組み合わせ

**RayHunter + DagShell** = **完全なモバイルセキュリティプラットフォーム**:
- **RayHunter**は高度なIMSIキャッチャー検出を提供
- **DagShell**は攻撃ツールとプライバシー機能を提供
- 同じ端末で両方を**同時に実行**
- **機能が補完し合い、重複しません**
- モバイルセキュリティのすべてを1つの**携帯型パッケージ**で実現

### 今すぐ始める

**オプション1: ファームウェア導入済み** (最も簡単)
- **STS Collective**: [RayHunterとDagShell搭載Orbic RCL400](https://stscollective.com/products/orbic-rcl400-rayhunter-dagshell-hotspot)
- **すぐ使える状態**で届きます
- 面倒なインストールは不要
- 専門家が設定済み

**オプション2: DIYインストール**
- このガイドの手順に従う
- Orbic RCL400を所有していれば**無料**
- インストール方法を学ぶ
- 用途に合わせてカスタマイズ

### 関連記事

- **[RayHunterデバイスのフラッシュ方法: 完全ガイド](/articles/how-to-flash-rayhunter-devices-complete-guide/)**：先にRayHunterをインストール
- **[RayHunterデバイス比較: 完全レビュー](/articles/rayhunter-device-comparison-2026-complete-review/)**：プラットフォームを選択
- **[Flock-You検出プロジェクト: 監視対抗ハードウェアガイド](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/)**：ほかの検出ツール

### 最後に

**セキュリティ研究者**、**ペネトレーションテスター**、**プライバシー擁護者**、**ネットワーク管理者**のいずれにも、DagShellはモバイルセキュリティ作業向けの**携帯性が高く、強力で手頃な**プラットフォームを提供します。

**免責事項**: 責任を持って使用してください。自分が所有するネットワークと端末、または評価する明確な書面許可を得たものだけをテストしてください。法律と倫理を守ってください。ハッキングを楽しんでください! 🚀

{{< figure src="dagshell-orbic-rcl400-mobile-security-lab-conclusion-overview.webp" alt="DagShellファームウェアを搭載したOrbic RCL400ホットスポット。モバイルセキュリティ調査用の完全な携帯型ラボ" >}}


______

## 参考資料

1. [DagShell GitHubリポジトリー](https://github.com/dagnazty/DagShell)
2. [DagShellドキュメント](https://dagnazty.github.io/DagShell/)
3. [STS Collective - ファームウェア導入済み端末](https://stscollective.com/products/orbic-rcl400-rayhunter-dagshell-hotspot)
4. [WiGLE - Wi-Fiマッピングプロジェクト](https://wigle.net/)
5. [Computer Fraud and Abuse Act (CFAA)](https://www.law.cornell.edu/uscode/text/18/1030)
6. [Raspberry Pi公式ドキュメント](https://www.raspberrypi.org/documentation/)
7. [U-Blox GPSモジュールのドキュメント](https://www.u-blox.com/)
8. [OUIデータベース - IEEE標準](https://standards.ieee.org/products-programs/regauth/)
9. [iptablesチュートリアル](https://www.netfilter.org/documentation/)
10. [OpenSSLドキュメント](https://www.openssl.org/docs/)
