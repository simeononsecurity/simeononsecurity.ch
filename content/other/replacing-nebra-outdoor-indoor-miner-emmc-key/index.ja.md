---
title: "Nebra Helium Miner SDカードの交換：ステップバイステップガイド"
draft: false
toc: true
date: 2022-02-13
description: "このガイドで、Nebra IndoorおよびOutdoor、第1世代および第2世代、EMMC Key SDカードの交換または再フラッシュの方法と、Helium Minerの同期に関する問題の解決方法をご覧ください。"
genre: ["テクノロジー", "暗号通貨", "ハードウェア", "ヘリウム採掘", "トラブルシューティング", "SDカードの交換", "同期の問題", "ラズベリーパイ", "バレナ・エッチャー", "ネブラ・ヘリウム採掘機"]
tags: ["ネブラ・ヘリウム採掘機", "SDカードの交換", "同期の問題", "ヘリウム採掘", "トラブルシューティング", "ラズベリーパイ", "バレナ・エッチャー", "ハードウェアガイド", "SDカードのアップグレード", "同期の問題を解決する", "ステップ・バイ・ステップ・ガイド", "ヘリウム・マイナーの同期修正", "ネブラ インドアマイナー", "ネブラ・アウトドア・マイナー", "Raspberry Piコンピュート・モジュール3", "Balena Raspberry Pi CM3 イメージ", "ヘリウム鉱山のトラブルシューティング", "ネブラ鉱山機械", "バレナ・エッチャー・ソフトウェア", "Nebra MinerのEMMCキーの交換", "ヘリウム・マイナーのSDカード修理", "ヘリウムマイナーの同期に関する問題の修正", "Nebra Miner SDカードの交換", "Nebraヘリウム鉱山のトラブルシューティングの手引き", "ヘリウム採掘のヒント", "Nebra Helium Miner SDカードのアップグレード", "Nebra Miner SDカードを再イメージする方法", "Nebra Helium Minerの同期に関する問題のトラブルシューティング"]
cover: "/img/cover/A_cartoon_illustration_of_a_person_holding_a_Nebra_Helium_M.png"
coverAlt: "Nebra Helium Minerを持つ人の漫画イラスト。パネルが開いてSDカードスロットが見え、ガイドのステップがガイドブックとしてデバイスの上に浮かび上がっている。"
coverCaption: "同期の問題を解決し、Helium Minerを簡単にアップグレードできます。"
---

**Nebra屋内・屋外EMMCキー/SDカード**の交換と再イメージング

この包括的なガイドでは、NebraインドアおよびアウトドアEMMCキー/SDカードの交換または再フラッシュの手順を説明します。これらの手順に従うことで、Helium Minerとの同期の問題を解決し、スムーズな操作を保証することができます。このガイドでは、config.jsonファイルを取得し、Balena Raspberry Pi CM3イメージを使って新しいSDカードをフラッシュし、元のconfigファイルを新しいSDカードに転送するために必要な手順だけでなく、必要なツールやソフトウェアについても詳しく説明します。

## はじめに

Nebra Helium Minersは、屋内モデルと屋外モデルの両方で、その機能をEMMCキー/SDカードに依存しています。時間の経過とともに、同期の問題に対処し、最適なパフォーマンスを維持するために、このカードを交換または再フラッシュする必要が生じることがあります。このガイドでは、この作業を効果的に行うために必要な知識と手順を説明します。

Nebra Helium MinerのSDカードをうまく交換するには、特定のツールとソフトウェアが必要です。工具には、プラスドライバーまたは [Allen Key Set](https://amzn.to/34SlnOS) (depending on the model), a [Micro SD Card Reader](https://amzn.to/3Jl3U0w), a [64GB A2 micro SD card](https://amzn.to/3oJtTqs) (or larger), and a [Micro USB 2.0 Cable](https://amzn.to/3LxXYmA). The essential software needed for this process includes [Balena Etcher](https://www.balena.io/etcher/), Balena Raspberry Pi Image, and [Raspberry Pi USB Boot](https://github.com/raspberrypi/usbboot/raw/master/win32/rpiboot_setup.exe)これらのリソースが手元にあれば、SDカードの交換や再フラッシュを行う準備が整います。

## 必要な工具
- プラスドライバーまたは [plastic pry bar](https://amzn.to/3rLXVfc) for the Nebra Indoor Miner or [allen key set](https://amzn.to/34SlnOS)Nebra Outdoor Miner用
- 古いSDカードを取り外すための強力な爪、ピンセット、またはプライヤー。
- [A Micro SD Card Reader](https://amzn.to/3Jl3U0w)
- [A 64gb (or larger) A2 micro sd card](https://amzn.to/3oJtTqs)
- [A Micro USB 2.0 Cable](https://amzn.to/3LxXYmA)
## 必要なソフトウェア
- [Balena Etcher](https://www.balena.io/etcher/)
- [Raspberry Pi USB Boot](https://github.com/raspberrypi/usbboot/raw/master/win32/rpiboot_setup.exe)
- あなたの特定のデバイスのための最新のNebraイメージ：
*お持ちのデバイスが不明な場合は、下記をご参照ください。 [nebra documentatio](https://support.nebra.com/support/home)それよりも古い場合は、第一世代のデバイスを使用していると考えて間違いないだろう。
  - [Nebra Outdoor 2](https://github.com/NebraLtd/helium-nebra-outdoor2/releases/)
  - [Nebra Indoor 2](https://github.com/NebraLtd/helium-nebra-indoor2/releases/)
  - [Nebra Outdoor 1](https://github.com/NebraLtd/helium-nebra-outdoor1/releases)
  - [Nebra Indoor 1](https://github.com/NebraLtd/helium-nebra-indoor1/releases)

## ネブラのヘリウム採掘機の内部
### ネブラ屋内鉱夫の中身：
{{< figure src="Indoor-internal-lights.png" alt="Nebra Indoor Miner" >}}
### ネブラ・アウトドア・マイナーの内容：
{{< figure src="Inside-Interfaces.jpg" alt="Nebra Outdoor Miner" >}}
 - 1.) 9-16V @ 15W DC 6.5MMx2.0MM バレル・ジャック
 - 2.)イーサネット・コネクター
 - 3.)LEDインジケーター
 - 4.)インターフェイスボタン
 - 5.)4G / LTEモジュールコネクター
 - 6.)Simカードスロット

## SD カードの交換方法
### ステップ1: EMMC Keyからconfig.jsonファイルを取得します：
- ダウンロードしてインストールする [Raspberry Pi USB Boot](https://github.com/raspberrypi/usbboot/raw/master/win32/rpiboot_setup.exe)これは、コンピュートモジュールをUSBファイルシステムとしてブートするために必要です。
- CM3ドーターボードのジャンパーピンを特定し、プログラミングモードに合わせます。
 - {{< figure src="daughterboardBreakdown.png" alt="Nebra Daughterboard Overview" >}}
   - 5.)マイクロUSBポート
   - 7.)JP4 USBジャンパー-通常動作とフラッシュ・モードの切り替えに使用され、通常動作の場合は1-2 の位置に、プログラミングの場合は2-3 の位置にあることを確認する。
   - 8.)JP3 電源ジャンパー - Micro USB コネクターからモジュールに電源を供給します。PCからプログラミングするときのみ接続し、メインボードが接続されていないことを確認してください。
 - JP4 ジャンパーを 2+3 の位置に動かします。
 - USBケーブルを接続し [Raspberry Pi USB Boot](https://github.com/raspberrypi/usbboot/raw/master/win32/rpiboot_setup.exe)ユーティリティ
 - ファイルエクスプローラを開くと、"resin-boot" というドライブが表示されます。このディレクトリから "config.json "ファイルを取り出します。
 - USBケーブルを抜き、JP4ジャンパを1+2の位置にリセットします。
### ステップ2: 新しいSDカードにBalena Raspberry Pi CM3イメージをフラッシュします：
- 適切なイメージをダウンロードして展開します。
  - [Nebra Outdoor 2](https://github.com/NebraLtd/helium-nebra-outdoor2/releases/)
  - [Nebra Indoor 2](https://github.com/NebraLtd/helium-nebra-indoor2/releases/)
  - [Nebra Outdoor 1](https://github.com/NebraLtd/helium-nebra-outdoor1/releases)
  - [Nebra Indoor 1](https://github.com/NebraLtd/helium-nebra-indoor1/releases)
- 使用 [Balena Etcher](https://www.balena.io/etcher/)最近解凍した.imgファイルと新しいmicrosdカードをターゲットデバイスとして選択します。
- フラッシュを選択します。
### ステップ3：新しいSDカードを取り付け、Nebra Minerを再度組み立てます：
 - 以前EMMCキーがあったスロットにSDカードを取り付けます。
 - マイナーを再組み立てする
 - 新しくフラッシュしたNebra Minerに最初に電源を入れるときは、Wifi接続を再び設定する前に、イーサネットで20～30分間接続してください。
### ステップ4：利益？




