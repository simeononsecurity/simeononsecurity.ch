---
title: 「BGW-320 のバイパス: Azores COTS ONT の使用 - ステップバイステップ ガイド」
draft: false
toc: true
date: 2023-04-30
description: 「このわかりやすいガイドで、BGW-320 をバイパスし、Azores 製の COTS ONT を使用して ISP のネットワークに接続する方法を学びましょう。」
tags: [「コッツオント」、「BGW-320」、「アゾレス諸島」、"ファイバ"、"通信網"、「XGS-PON」、"イーサネット"、"IP パススルー"、「カスタマイズ」、「ISP」、"オント ID"、"Macアドレス"、"機器ID",「イメージバージョン」、「ハードウェアバージョン」、「テルネット」、"CLI アプリケーション"、「ウェブGUI」、"工場出荷時設定モード",「互換性の問題」]
cover: "/img/cover/A_cartoon_technician_holding_a_COTS_ONT_with_a_fiber_cable.png"
coverAlt: 「背景にファイバーケーブルを備えた COTS ONT を保持している漫画の技術者。」
coverCaption: 「」
---

## BGW-320 をバイパスし、Azores WAG-D20 を使用する方法

光ファイバーを使用しているほとんどの人は、インターネットに接続する方法が 2 つあります。光ファイバーから ONT、イーサネットからゲートウェイ、または光ファイバーからゲートウェイに直接接続します。この記事では、BGW-320 をバイパスして Azores 製の COTS ONT を使用する方法に焦点を当てます。

### 技術的側面

の[Azores WAG-D20](https://cdn.shopifycdn.net/s/files/1/0280/5153/8029/files/Azores_Product_Specification_-_WAG-D20_v0.6.pdf?v=1604914153) is a XGS-PON ONU/ONT that comprises of a 10GE port along with a 2.5GE port even though it may be labeled on the device exterior as GE LAN. It may be acquired [here](https://www.balticnetworks.com/products/azores-1x-10gbe-1x-2-5gbe-intel-based-xgspon-ont)

{{< figure src="azores-wag-d20-xgs-pon-ont-front_225x225_crop_center.webp" alt="Azores WAG-D20" >}}

### デバイスアクセス

デバイスのデフォルトの IP アドレスは 192.168.1.1 で、そのゲートウェイ アドレスにはパブリック IP アドレスを使用した工場出荷時の入力ミスがあります。つまり、192.168.1.1 ではなく 192.162.1.1 と表示されます。

起動したら、Enter キーを押して、TTL シリアル インターフェイス (115200 8N1) でログイン プロンプトを表示する必要があります。このデバイスには、カスタマイズしたファイルを保持するオーバーレイ パーティションを備えた A/B イメージ システムが搭載されています。
 
＃＃＃ 資格

- `admin`/`ADMIN123!@#` - Web GUIの管理者ログイン
- `ゲスト`/`ようこそ` - ゲストログイン
- `test`/`default` - 工場出荷時のログイン

### イーサネットインターフェイス

クライアントを 10G イーサネット ポートに接続し、192.168.1.x/24 ネットワーク内のアドレス (192.168.1.2/255.255.255.0 など) を使用して構成します。

1 ～ 65535 のポート スキャンを実行すると、いくつかのポートが開いていることがわかります。

- ポート `23` および `8009` - Telnet、ログインが必要、CLI アプリケーションを実行します。
- ポート「10002」 - 不明
- ポート `80` - WebUI、機能は 2 つだけ

### ONT のカスタマイズ

{{< figure src="customizingtheont.png" alt="A BGW-320" >}}

ここで重要な部分が始まります。つまり、デバイス情報を変更して、ISP のネットワークと互換性を持たせる必要があります。

まず、ISP ゲートウェイまたは ONT から次の情報を取得します。

1. **ONT ID**
2. **MAC アドレス**
3. **機器ID**
4. **イメージバージョン**
5. **ハードウェアバージョン**

注: これらは OMCI 値であり、Web UI からの値ではありません。

個人用 ONT (telnet 192.168.1.1) に Telnet し、**`default`** パスワードを使用して **`test`** としてログインし、コマンド 'test' を実行して工場出荷時設定モードに切り替えます。

「show」コマンドを使用して、現在設定されている値を表示します。

- `gpon macを表示`
- `snを表示`
- `機器IDを表示`

完了したら、x をデバイスの値に置き換えて次のコマンドを使用して設定をカスタマイズします。

- `set gpon mac xx:xx:xx:xx:xx:xx`
- `set sn <ここにONT IDを挿入>`

ヒューマックスの場合:

- `機器ID「iONT320500G」を設定`
- `config ONU-G_Version "BGW320-500_2.1"`

ノキアの場合:

- `機器ID「iONT320505G」を設定`
- `config ONU-G_Version "BGW320-505_2.2"`

注: 最後の 2 つのコマンドは、**`test`** ユーザーとしてログインした Telnet から適用する必要があります。

### 再起動して True IP パススルーをお楽しみください

カスタマイズ後、ONT を再起動して、真の IP パススルーをお楽しみください。

### トラブルシューティングと追加の手順
このトピックの詳細については、以下を参照してください。[8311 discord](https://discord.gg/XbTWBbSG4p) or the notes provided on [google docs](https://docs.google.com/document/d/13gucfDOf8X9ptkj5BOg12V0xcqqDZDnvROJpW5CIpJ4/)

＃＃＃ 結論

これらの手順に従うことで、BGW-320 をバイパスし、Azores 製の COTS ONT を使用して ISP のネットワークに接続できます。ただし、コマンドを入力するときは注意し、「x」をデバイスの値に正しく置き換えてください。そうしないと、互換性の問題が発生し、接続エラーが発生する可能性があります。


