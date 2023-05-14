---
title: "BGW-320をバイパスする：Azores COTS ONTの使用 - ステップバイステップガイド"
draft: false
toc: true
date: 2023-04-30
description: "BGW-320をバイパスして、アゾレス社製のCOTS ONTを使ってISPのネットワークに接続する方法を、この簡単なガイドでご紹介します。"
tags: ["COTS ONT", "BGW-320", "アゾレス", "繊維", "ネットワーク", "XGS-PON（エックスジーエスポン", "イーサネット", "IPパススルー", "カスタム化", "ISP", "アイディー", "MACアドレス", "機器ID", "イメージバージョン", "ハードウェアバージョン", "テルネット", "CLIアプリケーション", "ウェブGUI", "ファクトリーコンフィグレーションモード", "相性問題"]
cover: "/img/cover/A_cartoon_technician_holding_a_COTS_ONT_with_a_fiber_cable.png"
coverAlt: "ファイバーケーブルを背景に、COTS ONTを手にする漫画の技術者。"
coverCaption: ""
---

## BGW-320をバイパスしてアゾレスWAG-D20を使用する方法

ファイバーを使っている人の多くは、ファイバーからONT、イーサネットからゲートウェイ、ファイバーから直接ゲートウェイという2通りの方法でインターネットに接続しています。今回は、BGW-320をバイパスして、Azores社製のCOTS ONTを使用する方法を中心に解説します。

### 技術的側面

その[Azores WAG-D20](https://cdn.shopifycdn.net/s/files/1/0280/5153/8029/files/Azores_Product_Specification_-_WAG-D20_v0.6.pdf?v=1604914153) is a XGS-PON ONU/ONT that comprises of a 10GE port along with a 2.5GE port even though it may be labeled on the device exterior as GE LAN. It may be acquired [here](https://www.balticnetworks.com/products/azores-1x-10gbe-1x-2-5gbe-intel-based-xgspon-ont)

{{< figure src="azores-wag-d20-xgs-pon-ont-front_225x225_crop_center.webp" alt="Azores WAG-D20" >}}

### デバイスアクセス

デバイスのデフォルトIPアドレスは192.168.1.1で、ゲートウェイアドレスはパブリックIPアドレスを使用した工場出荷時のタイプミス（192.168.1.1ではなく、192.162.1.1を示す）です。

起動したら、TTLシリアルインターフェース（115200 8N1）でログインプロンプトが表示されるので、Enterキーを押す必要があります。このデバイスは、A/Bイメージシステムと、カスタマイズしたファイルを格納するオーバーレイパーティションを持っています。
 
### 認証情報

-`admin``ADMIN123!@#`- Web GUI用管理者ログイン
-`Guest``welcome`- ゲストログイン
-`test``default`- 工場ログイン

### イーサネットインターフェース

クライアントを10Gイーサネットポートに接続し、192.168.1.x/24ネットワークのアドレス（192.168.1.2/255.255.0）で設定します。

1-65535のポートスキャンを実行すると、いくつかのポートが開いていることに気づきます：

- ポート`23`&`8009`- Telnet、要ログイン、CLIアプリケーションを実行します。
- ポート`10002`- 不明な点
- ポート`80`- WebUI、2つの機能のみ

### ONT のカスタマイズ

{{< figure src="customizingtheont.png" alt="A BGW-320" >}}

次に重要なのは、ISPのネットワークと互換性を持たせるために、デバイスの情報を変更することです。

まず、ISPのゲートウェイまたはONTから以下の情報を取得します：

1.**ONT ID**
2.**MACアドレス
3.**機器ID
4.**画像バージョン
5.**ハードウェアのバージョン

注：これらはOMCIの値であり、Web UIからの値ではありません。

パーソナルONTにTelnet（telnet 192.168.1.1）し、**としてログインします。`test`を使用している。`default`パスワードを入力し、「test」コマンドを実行すると、工場出荷時設定モードに移行します。

show'コマンドで現在設定されている値を表示する：

-`show gpon mac`
-`show sn`
-`show equipment id`

以下のコマンドで、xをお使いのデバイスの値に置き換えて、設定をカスタマイズしてください：

-`set gpon mac xx:xx:xx:xx:xx:xx`
-`set sn <insert ONT ID here>`

HUMAXの場合：

-`set equipment id “iONT320500G”`
-`config ONU-G_Version "BGW320-500_2.1”`

ノキアの場合：

-`set equipment id “iONT320505G”`
-`config ONU-G_Version "BGW320-505_2.2”`

注：最後の2つのコマンドは、**としてログインしているtelnetから適用する必要があります。`test`のユーザーです。

### 再起動して真のIPパススルーを楽しむ

カスタマイズ後、ONTを再起動し、真のIPパススルーをお楽しみください。

### トラブルシューティングと追加ステップ
このトピックの詳細については、以下のサイトを参照してください。[8311 discord](https://discord.gg/XbTWBbSG4p) or the notes provided on [google docs](https://docs.google.com/document/d/13gucfDOf8X9ptkj5BOg12V0xcqqDZDnvROJpW5CIpJ4/)

### 結論

以上の手順で、BGW-320 をバイパスして、Azores 社製の COTS ONT を使用して ISP のネットワークに接続することができます。ただし、コマンドの入力には注意が必要で、'x'をデバイスの値に正しく置き換えるようにしないと、互換性の問題に直面し、接続に失敗する可能性があることを確認してください。


