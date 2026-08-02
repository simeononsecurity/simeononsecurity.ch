---
title: "Flock Finder: Flock Safety ALPRカメラのマッピングツール"
date: 2026-07-22
toc: true
draft: false
description: "Flock FinderはWiGLE WiFiデータとOUIフィンガープリンティングを使用して、世界中の40,000以上のFlock Safety ALPRカメラをマッピングするオープンソースツールです。仕組み、制限事項、およびリアルタイム検出のハードウェアツールについて学びましょう。"
genre: ["プライバシー技術", "対監視", "オープンソースプロジェクト", "デジタル権利", "ネットワークセキュリティ", "プライバシーツール", "ハードウェアハッキング", "セキュリティ研究"]
tags: ["Flock Finder", "Flock Safety", "ALPR", "ナンバープレートリーダー", "OUIフィンガープリンティング", "WiGLE", "WiFi監視", "対監視", "STS Collective", "FlockYou", "ESP32", "プライバシーツール", "NitekryDPaul", "DeFlockJoplin", "ALPR検出", "オープンソースセキュリティ", "監視マッピング", "大規模監視", "WiFi OUI", "プライバシー保護", "MACアドレス", "プロミスキャスモード", "802.11", "リアルタイム検出", "Wardriving", "デジタル権利", "市民的自由", "監視への意識", "GitHub", "Python"]
cover: "/img/cover/flock-finder-open-source-alpr-camera-map.webp"
coverAlt: "Flock Safety ALPRカメラの位置を示すカラフルなマーカーを表示するインタラクティブマップ。暗い背景にマーカーから抽象的なWiFi信号が放射されている。"
coverCaption: "Flock FinderはWiGLE WiFiデータとOUIフィンガープリンティングを使用して40,000以上の疑わしいFlock Safety ALPRカメラをマッピングします。"
canonical: "https://simeononsecurity.com/articles/flock-finder-alpr-surveillance-mapping-tool/"
---

**クラウドソーシングされたWiFiデータを使用してFlock Safety ALPRカメラをマッピングする、オープンソースの監視意識向上ツール。**

## Flock Finderとは？

**[Flock Finder](https://simeononsecurity.github.io/flock-finder/)** は、米国および108の他の国々で**Flock Safety ALPR（自動ナンバープレート読み取り）カメラ**をマッピングするオープンソースプロジェクトです。**31の既知のFlock Safety WiFi OUI（組織固有識別子）プレフィックス**と**WiGLEクラウドソーシングWiFiデータベース**を組み合わせて、疑わしいカメラの位置を特定し、インタラクティブマップにプロットします。

このプロジェクトは**[github.com/simeononsecurity/flock-finder](https://github.com/simeononsecurity/flock-finder)**にあり、GitHub Actionsを通じて毎日自動更新され、2026年7月時点で世界964地域にわたる**40,000以上の疑わしいカメラ**をマッピングしています。

| 指標 | 値 |
|--------|-------|
| **マッピングされたカメラ** | 40,026以上 |
| **既知のOUIプレフィックス** | 31 |
| **対象国** | 109 |
| **対象地域** | 964 |
| **データ保持期間** | 730日（2年） |
| **自動更新頻度** | 毎日 |

*これは一般的な意識向上ツールであり、確定的な目録ではありません。データから結論を導く前に制限事項のセクションをお読みください。*

Flock Safety ALPRの監視がプライバシーにとって重要な理由については、**[Flock Safety カメラ監視：普及状況、プライバシーの懸念、保護戦略](/articles/flock-safety-camera-surveillance-prevalence-privacy-protection-2026/)**をお読みください。

______

## 仕組み：WiGLEを通じたOUIフィンガープリンティング

### 核心的な洞察

Flock Safetyカメラには**WiFiトランシーバー**が搭載されており、キャプチャしたナンバープレートデータをクラウドにアップロードするために定期的にスリープから覚醒します。これらの短いアクティブウィンドウの間、カメラはその**MACアドレス**を含むWiFiフレームをブロードキャストします。MACアドレスの最初の3バイトはメーカーを識別します。これが**OUI（組織固有識別子）**です。

セキュリティ研究者**@NitekryDPaul**は、**プロミスキャスモード2.4GHz分析**を通じて、Flock Safetyカメラハードウェアに一貫して関連する**30のOUIプレフィックス**を発見しました。31番目のプレフィックス（`82:6B:F2`）は、Joplin, MOでのフィールドテスト中に**Michael / DeFlockJoplin**によって提供されました。

Flock Finderはこれら31のOUIを取得し、WiGLEにこれらのプレフィックスに一致する記録済みWiFiネットワークを照会し、結果をマップにプロットします。

### Flock Safetyの31の既知OUIプレフィックス

| # | OUIプレフィックス | ソース | # | OUIプレフィックス | ソース |
|---|-----------|--------|---|-----------|--------|
| 1 | **70:C9:4E** | @NitekryDPaul | 17 | **D0:39:57** | @NitekryDPaul |
| 2 | **3C:91:80** | @NitekryDPaul | 18 | **E8:D0:FC** | @NitekryDPaul |
| 3 | **D8:F3:BC** | @NitekryDPaul | 19 | **E0:4F:43** | @NitekryDPaul |
| 4 | **80:30:49** | @NitekryDPaul | 20 | **B8:1E:A4** | @NitekryDPaul |
| 5 | **B8:35:32** | @NitekryDPaul | 21 | **70:08:94** | @NitekryDPaul |
| 6 | **14:5A:FC** | @NitekryDPaul | 22 | **58:8E:81** | @NitekryDPaul |
| 7 | **74:4C:A1** | @NitekryDPaul | 23 | **EC:1B:BD** | @NitekryDPaul |
| 8 | **08:3A:88** | @NitekryDPaul | 24 | **3C:71:BF** | @NitekryDPaul |
| 9 | **9C:2F:9D** | @NitekryDPaul | 25 | **58:00:E3** | @NitekryDPaul |
| 10 | **C0:35:32** | @NitekryDPaul | 26 | **90:35:EA** | @NitekryDPaul |
| 11 | **94:08:53** | @NitekryDPaul | 27 | **5C:93:A2** | @NitekryDPaul |
| 12 | **E4:AA:EA** | @NitekryDPaul | 28 | **64:6E:69** | @NitekryDPaul |
| 13 | **F4:6A:DD** | @NitekryDPaul | 29 | **48:27:EA** | @NitekryDPaul |
| 14 | **F8:A2:D6** | @NitekryDPaul | 30 | **A4:CF:12** | @NitekryDPaul |
| 15 | **24:B2:B9** | @NitekryDPaul | 31 | **82:6B:F2** | DeFlockJoplin |
| 16 | **00:F4:8D** | @NitekryDPaul | | | |

### addr1検出技術

@NitekryDPaulの重要な発見は、送信機MACアドレスの単純なマッチングを超えています。Flockカメラはそのデューティサイクルの大部分を**スリープ**状態で過ごします。近くのアクセスポイントがカメラ*宛て*にフレームを送信すると、カメラのMACは802.11フレームの**addr1（受信者アドレス）**として表示されます — カメラ自体が積極的に送信していない場合でも。

**ワイルドカードプローブリクエスト検出**（802.11管理フレーム タイプ=0、サブタイプ=4、空のSSID）と組み合わせることで、非常に精密な検出シグネチャが得られます。Joplin, MOでのフィールドテストでは、**2つの誤検知のみで12台中11台のカメラを検出**することができました。

> ⚠️ **重要**: WiGLEベースのFlock Finderマップはaddr1技術を**実装していません**。WiGLEは歴史的で、受動的に収集されたデータセットです。送信機のみを記録し、受信機は記録しません。@NitekryDPaulの方法を実際に使用するリアルタイム検出には、フィールドで稼働する専用ハードウェアが必要です。

______

## ライブマップの使用

インタラクティブマップは**[simeononsecurity.github.io/flock-finder/](https://simeononsecurity.github.io/flock-finder/)**でライブ公開されています。表示内容：

- **クラスター化されたカメラマーカー** OUIプレフィックスでカラーコード化
- **検索** 都市、州、またはBSSIDによる
- **OUIデータテーブル** プレフィックスごとのカメラ数
- **統計パネル** 総カメラ数、地域、最終更新タイムスタンプを表示
- **ALPRについてのページ** 記録されたプライバシー被害、法的コンテキスト、コミュニティリソース

マップデータのエクスポートも直接利用可能：

- `data/flock_cameras.geojson` — QGIS、Leaflet、または他のツールで使用するためのGeoJSON
- `data/flock_cameras.csv` — スプレッドシート対応フォーマット
- `data/scan_stats.json` — スキャン統計と数

### 主な制限事項

**マップは慎重に利用してください。** WiGLEはクラウドソーシングされた、散発的に更新されるデータセットであり、ライブフィードではありません。

- **Flockカメラは継続的にブロードキャストしません。** データをアップロードするために短時間覚醒するため、WiGLEの記録はちょうど適切なタイミングにワードライバーが近くにいることに完全に依存します。
- **データは数ヶ月または数年前のものかもしれません。** 移動または削除されたカメラがまだ表示される場合があります。
- **OUIマッチングはヒューリスティックです。** OUIは共有、再割り当て、またはスプーフィングされる可能性があります。すべての結果は*疑わしい* Flockデバイスであり、確認済みではありません。
- **カバレッジは均一ではありません。** 密集した都市部ではWiGLEデータが多く、農村部では非常に少ないです。

*マップを使用して、お住まいの地域の監視密度についての一般的な意識を高めてください。実際のリアルタイム検出については、以下のハードウェアオプションをご覧ください。*

______

## Flock Finderを自分で実行する

### 前提条件

- Python 3.8以上
- API認証情報付きの無料[WiGLE](https://wigle.net/account)アカウント

### セットアップ

```bash
# Clone the repository
git clone https://github.com/simeononsecurity/flock-finder.git
cd flock-finder

# Install dependencies
pip install -r requirements.txt

# Set up your WiGLE API credentials
cp .env.example .env
# Edit .env with your WiGLE API Name and Token
```

### スキャナーの実行

```bash
# Full scan — all 31 OUI prefixes, worldwide
python3 scripts/wigle_query.py

# Single OUI test
python3 scripts/wigle_query.py --oui 70:C9:4E

# US only
python3 scripts/wigle_query.py --country US

# Specific bounding box (lat1,lon1,lat2,lon2)
python3 scripts/wigle_query.py --bbox 37,-97,39,-94

# Dry run — verify auth, no API queries
python3 scripts/wigle_query.py --dry-run
```

### ローカルでマップを表示する

```bash
python3 -m http.server 8080 --directory docs/
# Open http://localhost:8080 in your browser
```

### GitHub Actionsによる自動日次更新

リポジトリをフォークし、WiGLE認証情報を**リポジトリシークレット**（`WIGLE_API_NAME`と`WIGLE_API_TOKEN`）として追加します。含まれているワークフローは毎日UTC午前6時に実行され、新しいカメラが見つかるたびに更新されたデータファイルを自動コミットします。

______

## リアルタイム検出：STS Collective FlockYouハードウェア

WiGLEマップはカメラが*観察された場所*を教えてくれます。走行中のリアルタイム検出 — ライブWiFiトラフィックで@NitekryDPaulの実際のOUIマッチング方法を使用する — には専用ハードウェアが必要です。

**[STS Collective](https://stscollective.com/discount/SIMEONONSECURITY)**は、Flock OUIシグネチャをスキャンし、一致するシグネチャが検出された瞬間に警告を発する、ポータブルなESP32ベースの検出器を製造しています。

### FlockYouデバイスラインナップ

| デバイス | 説明 |
|--------|-------------|
| **[FlockYou — M5 Atom Lite](https://stscollective.com/products/flockyou-m5-atom-lite-flock-camera-detector)** | コンパクトなポケットサイズのFlock検出器。事前フラッシュ済み、プラグアンドプレイ。検出時にLEDアラート。 |
| **FlockYou Pro — LED + Audio** | LEDインジケーターに加えて音声アラートを追加。走行中にカメラを見逃しません。 |
| **FlockYou Atom VoiceS3R** | ハンズフリーで道路に目を向けたまま操作できる音声アラート付きボイス対応検出器。 |

全デバイス共通：
- **事前フラッシュ済み**、箱から出してすぐに使用可能
- 既知の31のFlock OUI全てについてライブWiFiトラフィックをスキャン
- コンパクトでポータブル — カップホルダーやポケットに収まる
- USB-Cで電源供給（カーアダプター、モバイルバッテリー、またはノートPC）

> 💰 **限定割引**：コード **FLOCKFINDER** を使用すると、すべてのSTS Collective FlockYouデバイスで**20%オフ** — またはコード **SIMEONONSECURITY** を使用すると注文全体で最大20%オフ。[stscollective.com/discount/SIMEONONSECURITYで購入](https://stscollective.com/discount/SIMEONONSECURITY)。

これらのデバイスとDIY代替品の完全な技術的分析については、**[Flock-You検出プロジェクト：完全な対監視ハードウェアおよびセットアップガイド](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/)**をお読みください。

______

## プロジェクト構造

```
flock-finder/
├── scripts/
│   └── wigle_query.py        # WiGLE API query and data pipeline
├── data/
│   ├── flock_ouis.csv         # 31 known Flock Safety OUI prefixes
│   ├── flock_cameras.geojson  # Camera locations (GeoJSON)
│   ├── flock_cameras.csv      # Camera locations (CSV)
│   └── scan_stats.json        # Scan statistics
├── docs/
│   └── index.html             # Interactive Leaflet map
└── .github/workflows/
    └── update-data.yml        # Daily auto-update workflow
```

______

## よくある質問

### これは合法ですか？

はい。**Flock Finderは、自発的に提供されたWiFi調査データを集約するWiGLEデータベースから、公開されているデータのみを使用しています。**ハッキング、不正アクセス、独自システムは一切関与していません。OUIシグネチャのための受動的WiFi監視は米国では合法です。

### マッピングされた全てのカメラは確実にFlockカメラですか？

いいえ。OUIマッチングは**ヒューリスティック**です。OUIプレフィックスはメーカー間で共有、再割り当て、またはスプーフィングされる可能性があります。データベースの各レコードは*疑わしい* Flockデバイスであり、確認済みではありません。修正リクエストの詳細については[データポリシー](https://github.com/simeononsecurity/flock-finder/blob/main/docs/data-policy.md)をお読みください。

### なぜ一部のOUIプレフィックスがカメラを表示しないのですか？

WiGLEのカバレッジは均一ではありません。その特定のOUIがアクティブな状態で特定の地域をスキャンしたワードライバーがいない場合、レコードは存在しません。*データの不在はカメラの不在を意味しません。*

### データはどの程度最新ですか？

GitHub Actionsワークフローは毎日実行され、最新のWiGLE結果を取得します。ただし、WiGLE自体は特定の場所について数日から数年前のレコードを持っている場合があります。最近のスキャンのタイムスタンプについては`scan_stats.json`ファイルを確認してください。

### 自分のwardriveデータを提供できますか？

はい。wardriveデータを[WiGLE](https://wigle.net)にアップロードしてください — Flock Finderの次の日次スキャンに自動的に反映されます。[貢献ガイド](https://github.com/simeononsecurity/flock-finder/blob/main/CONTRIBUTING.md)を通じてOUIプレフィックスやコードの改善も貢献できます。

______

## コミュニティと関連プロジェクト

Flock Finderは単独では機能しません。ALPR監視を記録し、対抗するために取り組むツールと組織の成長するエコシステムがあります：

- **[DeFlock.org](https://deflockjoplin.org/)** — コミュニティ主導のALPR追跡、文書化、および支持活動
- **[Have I Been Flocked?](https://haveibeenflocked.com/)** — あなたのナンバープレートがFlockのシステムで検索されたか確認
- **[FlockHopper](https://flockhopper.com/)** — 既知のALPRカメラを避けたルート計画
- **[Atlas of Surveillance (EFF)](https://atlasofsurveillance.org/)** — 法執行機関が使用する監視技術のEFFデータベース
- **[NoALPRs.com](https://noalprs.com/)** — ALPRの導入と戦うコミュニティのためのリソース
- **[DeFlockJoplin](https://deflockjoplin.org/)** — オープンソースファームウェアとフィールド研究；31番目のOUIプレフィックスを提供

______

## クレジット

- **OUI研究**：@NitekryDPaul — 30の元のOUIプレフィックス全てとaddr1/プロミスキャスモード検出戦略
- **フィールドテスト**：Michael / DeFlockJoplin — 31番目のOUIプレフィックス（`82:6B:F2`）とワイルドカードプローブの強化
- **データソース**：[WiGLE](https://wigle.net) — クラウドソーシングされたWiFi/携帯電話ネットワークデータベース
- **インスピレーション元**：[DeFlock](https://deflockjoplin.org/)およびtrack-openroaming-passpoint
- **ハードウェアパートナー**：[STS Collective](https://stscollective.com/discount/SIMEONONSECURITY) — FlockYou ESP32検出器

______

## 結論

**Flock Finder**は誰でもFlock Safety ALPRカメラがどれほど広く展開されているかを素早く視覚的に把握できます — クラウドソーシングされたWiFiデータから毎日自動更新される109カ国40,000以上の推定位置。

これは**透明性ツール**であり、ライブトラッカーではありません。そのデータは歴史的、不完全、確率的です。しかし、要約やレポートでは表現できない方法でALPR監視の規模を可視化します。

監視された地域を移動する際の真のリアルタイム保護には、マップと専用ハードウェアを組み合わせてください。**[STS CollectiveのFlockYouデバイス](https://stscollective.com/discount/SIMEONONSECURITY)**は@NitekryDPaulの検出方法をESP32に直接実装し、ライブカメラシグネチャが検出された瞬間に警告を発します — **[stscollective.com](https://stscollective.com/discount/SIMEONONSECURITY)**でコード**FLOCKFINDER**または**SIMEONONSECURITY**を使用して最大20%オフで入手可能。

### 関連記事

| 記事 | 内容 |
|---------|---------------|
| **[Flock Safety カメラ監視：プライバシーと保護](/articles/flock-safety-camera-surveillance-prevalence-privacy-protection-2026/)** | 全体像：普及統計、市民の自由の問題、ACLUツールキット、DeFlock統計、FOIAガイド、保護戦略 |
| **[Flock-You検出プロジェクト：対監視ハードウェアガイド](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/)** | ESP32ベースのFlock検出器の完全技術ガイド — OUI-SPY、M5 Atom Lite、DIYビルド、ステップバイステップのファームウェアセットアップ |
| **[Rayhunterデバイスのフラッシュ方法：完全ガイド](/articles/how-to-flash-rayhunter-devices-complete-guide/)** | 完全な対監視意識のためにALPRカメラと並行してIMSIキャッチャー（セルサイトシミュレーター）を検出 |
| **[Orbic RCL400用DagShellカスタムファームウェア](/articles/dagshell-orbic-rcl400-custom-firmware-guide-2026/)** | モバイルホットスポットをセキュリティ研究プラットフォームに変換 — Flock検出ハードウェアとの相性が良い |
| **[Rayhunterデバイス比較2026](/articles/rayhunter-device-comparison-2026-complete-review/)** | ALPRおよびセルラー監視の脅威カテゴリーにわたる検出ハードウェアオプションを比較 |

______

## 参考文献

1. [Flock Finder GitHubリポジトリ](https://github.com/simeononsecurity/flock-finder)
2. [Flock Finderインタラクティブマップ](https://simeononsecurity.github.io/flock-finder/)
3. [STS Collective — FlockYouデバイス](https://stscollective.com/discount/SIMEONONSECURITY)
4. [WiGLE — ワイヤレスネットワークマッピング](https://wigle.net)
5. [DeFlock — コミュニティALPR意識](https://deflockjoplin.org/)
6. [DeFlockJoplin — オープンソース検出ファームウェア](https://deflockjoplin.org/)
7. [Electronic Frontier Foundation — ALPR](https://www.eff.org/issues/automated-license-plate-readers)
8. [ACLU — あなたは追跡されています](https://www.aclu.org/issues/privacy-technology/location-tracking/you-are-being-tracked)
