---
title: "Ubiquiti UniFi Express：コンパクトなゲートウェイとWiFi 6アクセスポイントのレビュー"
date: 2024-01-03
lastmod: 2026-11-08
toc: true
draft: false
description: "WiFi 6アクセスポイントを備えたコンパクトなゲートウェイ、UniFi Expressの機能と簡単な管理方法を紹介します。"
genre: ["技術レビュー", "ネットワークソリューション", "ホームネットワークの設定", "WiFi 6デバイス", "UniFi Expressの解説", "コンパクトなゲートウェイ", "無線アクセスポイント", "Ubiquiti製品", "ネットワークセキュリティ", "小規模事業者向けネットワーク"]
tags: ["UniFi Express", "WiFi 6", "ネットワークゲートウェイ", "Ubiquiti", "無線アクセスポイント", "技術レビュー", "ネットワークセキュリティ", "ホームネットワーク", "コンパクトなゲートウェイ", "小規模事業者", "オールインワンデバイス", "メッシュネットワーク", "デバイス設定", "インターネット接続", "Ubiquitiソリューション", "デュアルコアCPU", "WiFiのカバレッジ", "IDS/IPS", "VPNオプション", "アプリケーション認識型ファイアウォール", "UniFi OS", "ワイヤレスメッシュ", "ネットワーク拡張", "VLANサポート", "技術情報", "デバイスの制限", "Ubiquiti Networks", "ルーティング性能", "簡素化されたネットワーク管理"]
cover: "/img/cover/UniFi_Express_Connectivity.webp"
coverAlt: "コンパクトなデザインと滑らかな接続を表現したUniFi Expressのイラスト。効率性と革新性を強調しています"
coverCaption: "シンプルに。つなげる。革新する。UniFi Expressでネットワークを手軽に管理。"
ref: ["/articles/the-ideal-ubiquiti-unifi-networking-setup-both-simple-and-advanced", "/articles/ubiquiti-unifi-good-for-home-use", "/articles/ubiquiti-unifi-vs-tp-link-omada"]
---
**Ubiquiti UniFi Express：家庭や小規模事業者向けのコンパクトで高性能なゲートウェイ**

ネットワークソリューションが急速に進化する中、UbiquitiのUniFi Expressは、コンパクトながら高性能なゲートウェイとWiFi 6アクセスポイントを備えた製品です。このレビューでは、仕様や機能、他製品との比較を取り上げ、家庭や小規模事業者のネットワークに適しているかを説明します。

## UniFi Expressの概要

UniFi Expressは、次世代ファイアウォール、アプリケーション認識機能、内蔵WiFi 6アクセスポイントをスリムでコンパクトな筐体にまとめ、ネットワーク管理を簡素化します。このレビューでは、機能と制限を詳しく見て、他のUniFiゲートウェイと比較します。

{{< youtube id="VbIamWqXjAk" >}}

______

## 技術仕様：UniFi Expressのスペック

{{< figure src="sos-unifi-express.webp" alt="Ubiquiti UniFi Express" caption="Ubiquiti UniFi Express" link="https://amzn.to/418yMvj" >}}

UniFi Expressには、1 GHzで動作するデュアルコアARM Cortex-A53 CPUと1 GBのDDR3Lメモリが搭載されています。0.9インチのディスプレイにはリアルタイム情報が表示されます。最大スループットは1 Gbpsですが、Suspicious Activity機能がなく、UniFiデバイスのサポート数が5台に限られるなどの制約があります。

- **CPU：** 1 GHzデュアルコアARM Cortex-A53
- **メモリ：** 1 GB DDR3L
- **内蔵フラッシュストレージ：** 10 GB
- **ディスプレイ：** 0.9インチ
- **最大SQMスループット：** 1 Gbps
- **WANポート：** 1x Gigabit RJ45
- **LANポート：** 1x Gigabit RJ45
- **電源方式：** USB-C (5 V / 3 A)
- **最大消費電力：** 10 W
- **寸法：** 98 x 98 x 30 mm

これらの仕様を基に、さまざまなネットワーク環境でのUniFi Expressの性能を評価できます。

______

## WiFi 6の機能：内蔵アクセスポイント

UniFi Expressの主な機能の一つは、WiFi 6アクセスポイントを内蔵していることです。6 GHz帯（WiFi 6E）には対応しませんが、2.4 GHz帯と5 GHz帯の両方で高いスループットを提供します。約140 m²（1,500 ft²）の範囲をカバーし、そのエリア内で安定した接続を実現します。

- **2.4 GHz送信出力：** 22 dBm
- **5 GHz送信出力：** 25 dBm
- **MIMO：** 2 x 2 (DL/UL MU-MIMO)
- **2.4 GHzスループット：** 573.5 Mbps
- **5 GHzスループット：** 2.4 Gbps
- **同時接続クライアント数：** 60台以上

UniFi Expressはメッシュアクセスポイントとしても使用でき、ネットワークを簡単に拡張できます。

______

## UniFi Expressと他のゲートウェイの比較

{{< figure src="sos-unifi-express-vs-unifi-gateway-lite.webp" alt="Ubiquiti UniFi ExpressとUbiquiti UniFi Gateway Liteの比較" caption="Ubiquiti UniFi ExpressとUbiquiti UniFi Gateway Liteの比較" link="https://amzn.to/3uPFKta" >}}

UbiquitiのUniFi Express、UniFi Gateway Lite、UniFi Dream Router (UDR)、UniFi Dream Machine Pro (UDM Pro/SE)を比較すると、ネットワークの要件に合うゲートウェイを選びやすくなります。

### UniFi Express

[**UniFi Express**](https://amzn.to/418yMvj)は、WiFi 6アクセスポイントを内蔵したコンパクトなオールインワンゲートウェイです。UniFi Networkアプリが動作し、ルーティング性能は1 Gbpsです。価格は149ドルです。IDSおよびIPSによる脅威検出機能はありません。

### UniFi Gateway Lite

[**UniFi Gateway Lite**](https://amzn.to/3uPFKta)はUniFi Security Gatewayの後継製品で、管理には別のコンソールが必要です。価格は129ドルで、UniFi Expressと同じ1 Gbpsのルーティング性能を備えますが、アクセスポイントは内蔵していません。一方、IDSおよびIPSによる脅威検出機能を備え、高度な保護を提供します。

### UniFi Dream Router (UDR)

[**UniFi Dream Router (UDR)**](https://amzn.to/41rpBq9)は家庭向けで、複数の機能を一台にまとめています。1 GHzのデュアルコアARM Cortex-A53プロセッサ、2 GBのメモリ、1 Gbpsのルーティング性能を備えます。UniFi NetworkとUniFi Protectが動作し、IDS/IPS脅威検出にも対応します。価格は199ドルで、アクセスポイントも内蔵しているため、充実したホームネットワークに適しています。

### UniFi Dream Machine Pro (UDM Pro/SE)

[**UniFi Dream Machine Pro (UDM Pro/SE)**](https://amzn.to/3uP1tS1)は企業向けの製品です。1.7 GHzのデュアルコアArm Cortex-A57、4 GBのRAM、10 Gbpsのルーティング性能を備えます。UniFi NetworkとUniFi Protect、IDS/IPS脅威検出、複数のPoEポートに対応し、大規模ネットワークに適しています。価格は379～499ドルです。複雑な環境向けの幅広い機能を提供します。

### 適切なゲートウェイを選ぶ

ゲートウェイを選ぶ際は、ネットワークの具体的な要件を考慮してください。シンプルな操作、コンパクトな設計、基本的な脅威対策で十分ならUniFi Expressが適しています。高度な脅威検出を優先する場合はUniFi Gateway Liteが候補になります。UniFi Dream Routerは家庭向け、UniFi Dream Machine Pro/SEは企業向けで、より広範なネットワーク機能を備えています。

______

## UniFi Expressのセットアップ：簡単な開始手順

UniFi Expressはセットアップでもプラグアンドプレイの使いやすさを発揮します。WANポートからインターネットに接続し、スマートフォンでUniFi Networkアプリを起動して簡単な初期設定を行います。使いやすいソフトウェア環境と連携するため、Ubiquitiアカウントが必要です。

### 初期設定

1. UniFi Expressをインターネットに接続します。
2. スマートフォンでUniFi Networkアプリを開きます。
3. 画面の指示に従い、UniFi Expressの名前とワイヤレスネットワークを設定します。
4. 案内が表示されたら、新しいワイヤレスネットワークに接続します。

簡単に設定できるUniFi Expressは、機能を損なわずに手軽さを求めるユーザーに適しています。

#### UniFi Networkの設定

ネットワーク設定は、ブラウザー版のUniFi Networkアプリで調整するのがおすすめです。ゲートウェイのIPアドレス、または[https://unifi.ui.com](https://unifi.ui.com)からサインインして設定を開きます。Ubiquiti UniFiデバイスのセットアップ全体は、以下の動画で確認できます。

{{< youtube id="bWJNZvXXgf8" >}}

______

## メッシュアクセスポイントとして使うUniFi Express：広がる用途

UniFi Expressは単独のゲートウェイとしてだけでなく、既存ネットワークのメッシュアクセスポイントとしても機能します。有線または無線のアップリンクを利用でき、ネットワークに簡単に統合できます。柔軟な構成が可能です。

- **サポート対象デバイス数：** UniFi Networkデバイスをあと4台
- **メッシュ時に両ポートをLANとして使用：** はい
- **メッシュ互換性：** 第2世代以降のすべてのUniFiアクセスポイント
- **VLANサポート：** LAN/WANポートでは利用不可
- **CloudKey用ゲートウェイ：** いいえ。UniFi Gateway Liteが必要

この柔軟性により、UniFi Expressをアクセスポイントとして使い、要件の変化に応じてネットワークを拡張できます。

______

## よくある質問

{{< youtube id="0A7a9_6ZgCU" >}}

1. **UniFi Express (UX)は何台のデバイスをサポートしますか？**
   - UniFi Expressは、ほかに4台のUniFi Networkデバイスを管理できます。

2. **メッシュ接続時に両方のポートをLANポートとして使えますか？**
   - はい。UniFi Expressをメッシュネットワークに接続すると、両方のポートをLANとして使用できます。

3. **UXは一般的なUniFiアクセスポイントとメッシュ接続できますか？**
   - はい。第2世代以降のすべてのUniFiアクセスポイントとメッシュ接続できます。

4. **LAN/WANポートでVLANをサポートしていますか？**
   - LANポートまたはWANポートにVLANを割り当てることはできません。

5. **UniFi ExpressをCloudKeyのゲートウェイとして使えますか？**
   - いいえ。CloudKeyがある場合、UXはアクセスポイントとしてのみ使用できます。その場合はUniFi Gateway Liteが必要です。

______

## まとめ

UniFi Expressは、シンプルなホームネットワークや小規模オフィスに適した魅力的なエントリーレベルのCloud Gatewayです。サポートするデバイス数に制限があり、IDS/IPSもありませんが、コンパクトな設計と内蔵アクセスポイントにより、多くのユーザーにとって便利なオールインワン製品です。ネットワークの要件が変わっても、アクセスポイントとして使い続けられます。

______

## 参考資料

1. [Ubiquiti UniFi Express製品ページ](https://store.ui.com/us/en/pro/category/all-unifi-cloud-gateways/products/ux)
2. [Ubiquiti UniFi Gateway Lite製品ページ](https://store.ui.com/us/en/products/uxg-lite)
3. [Ubiquitiドキュメント](https://help.ui.com/hc/en-us)
4. [UniFi Networkアプリ](https://apps.apple.com/us/app/unifi/id1057750338) (iOS)
5. [UniFi Networkアプリ](https://play.google.com/store/apps/details?id=com.ubnt.easyunifi&hl=en_US&gl=US) (Android)
6. [UniFi OSの更新情報](https://community.ui.com/releases)
7. [LazyAdminによるUniFi Expressレビュー](https://lazyadmin.nl/home-network/unifi-express-review/#:~:text=The%20UniFi%20Express%20is%20really,takes%20a%20couple%20of%20minutes.)