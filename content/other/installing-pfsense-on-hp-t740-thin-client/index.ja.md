---
title: "HP t740 Thin Client での pfSense の実行: ヒントとトラブルシューティング ガイド"
draft: false
toc: true
date: 2023-04-29
description: "HP t740 Thin Client で pfSense をセットアップする方法、およびフリーズや SSD 検出の問題などの潜在的な問題のトラブルシューティング方法を学びます。"
tags: ["pfSense", "OPNセンス", "強化されたBSD", "HP t740", "シン・クライアント", "ホームサーバー", "PPPoE", "FreeBSD", "ブートプロンプト", "loader.conf.local", "ナノエディター", "SSDの検出", "M.2 SSD", "ウエスタンデジタル", "トラブルシューティング", "インストール後", "UART", "ESXi", "プロクスモックス"]
cover: "/img/cover/A_cartoon_of_a_wizard_casting_a_spell_to_fix_a_frozen_computer.png"
coverAlt: "フリーズしたコンピューターを修復するための呪文を唱えるウィザードの漫画。「問題が解決しました」という吹き出しが表示されます。"
coverCaption: ""
canonical: "https://simeononsecurity.ch/guides/installing-pfsense-on-hp-t740-thin-client/"
---
 HP t740 Thin Client 上の pfSense、OPNsense、または HardenedBSD**

pfSense、OPNsense、または HardenedBSD を実行する強力なデバイスをお探しの場合は、HP t740 Thin Client が適切な選択肢となる可能性があります。

## より強力でコンパクトなホーム サーバー

HP t740 Thin Client は、強力な pfSense ボックスまたはコンパクトなホーム サーバーとして使用できるコンパクトなデバイスです。 t730 または t620 Plus よりも多くの電力を提供するため、特にファイバー インターネットを使用している場合、PPPoE の実行に適しています。 10 ギガビット ネットワーキングへのアップグレード パスも提供できます。

## PS/2 フリーズ

ただし、FreeBSD またはその派生製品 (pfSense、OPNsense、HardenedBSD など) を (ESXi や Proxmox 内ではなく) ベアメタル上で実行する予定がある場合、起動時にシステムがフリーズし、次のメッセージが表示される問題が発生する可能性があります。 `atkbd0: [GIANT-LOCKED]` 幸いなことに、この問題はブート プロンプトで次のコマンドを入力することで解決できます。

```bash
unset hint.uart.0.at
unset hint.uart.1.at
```

*両方の設定を解除する必要があることに注意してください。そうしないと、起動時にロックアップしたままになります。*

OS をインストールした後、インストール後のシェルを開き、次のコマンドを実行します。

```bash
vi /boot/loader.conf.local
```
次に、次の 2 行を追加します。
```bash
hint.uart.0.disabled="1"
hint.uart.1.disabled="1"
```

### VI を使用して変更を保持する
vi に慣れていない人のために、次の手順を実行して行を追加できます。

行を追加する `hint.uart.0.disabled="1"` と `hint.uart.1.disabled="1"` に `/boot/loader.conf.local` vi エディターを使用してファイルを編集するには、次の手順を実行します。

1. FreeBSD システムでターミナルを開きます。

2. タイプ `vi /boot/loader.conf.local` Enter キーを押して、vi エディターでファイルを開きます。

3. を押します。 `i` キーを押して挿入モードに入ります。

4. 矢印キーを使用してカーソルをファイルの最後に移動します。

5. タイプ `hint.uart.0.disabled="1"` 引用符なしで。

6. Enter キーを押して新しい行を開始します。

7. タイプ `hint.uart.1.disabled="1"` 引用符なしで。

8. を押します。 `Esc` キーを押して挿入モードを終了します。

9. タイプ `:wq` Enter キーを押してファイルを保存して終了します。

これにより、次の 2 行が追加されます。 `/boot/loader.conf.local` これにより、UART が無効になり、FreeBSD またはその派生製品 (pfSense、OPNsense、HardenedBSD など) を実行しているときに、特定の HP t740 "Thin Client" デバイスでの起動中のフリーズ問題が修正されます。

これにより、pfSense/OPNsense の再起動とファームウェアのアップグレード後の問題が解決されます。

## SSD

HP M.2 eMMC を使用している場合、すぐに使える FreeBSD インストールでは検出されません。その場合、サードパーティ製の M.2 SSD が必要になります。 SATA または NVMe のすべての M.2 SSD が動作します。

HP t740 シン クライアント用のサードパーティ M.2 SSD をお探しの場合は、以下を検討することをお勧めします。 [Western Digital 500GB WD Blue SN570 NVMe](https://amzn.to/44bFCBk) or the [Western Digital 500GB WD Blue SA510 SATA](https://amzn.to/3AEbd0V) これらのオプションはどちらも信頼性が高く、デバイスで適切に動作するはずです。両方のスロットを利用したい場合は、両方が必要になります。 NVME の速度は犠牲になりますが、非常に重要な冗長性が得られます。

この記事の著者は、上記の手順を実行した後、t740 で pfSense CE 2.5.2 および OPNsense 22.1 を問題なく実行できたことに注意してください。

## トラブルシューティングとインストール後のトラブルシューティング

インストール後、ファイルの編集で問題が発生した場合は、次のコマンドを使用して nano エディターをインストールできます。 `pkg update` と `pkg install nano` これにより、テキスト ファイルを簡単に編集できます。

に加えられた変更を確実に行うには、 `/boot/loader.conf.local` ファイルが pfSense バージョンのアップグレード後も保持されるようにするには、次の行を追加する必要があります。 `/boot/loader.conf` と `/etc/rc.conf.local` 
```bash
hint.uart.0.disabled="1"
hint.uart.1.disabled="1"
```

ただし、場合によっては編集 `/boot/loader.conf.local` 再起動する前にファイルを編集しても問題は解決しません。このような場合、最初の起動の先頭に次の行を追加する必要がある場合があります。

```bash
unset hint.uart.0.at
unset hint.uart.1.at
```

これらの手順により、インストール プロセス中およびインストール プロセス後に発生する可能性のあるほとんどの問題が解決されます。

### 参考文献:
- [HP t740 "Thin Client"](https://www8.hp.com/us/en/thin-clients/t740.html)
- [pfSense](https://www.pfsense.org/)
- [OPNsense](https://opnsense.org/)
- [HardenedBSD](https://hardenedbsd.org/)
- [ServeTheHome](https://www.servethehome.com/hp-t740-thin-client-review/)
- [FreeBSD (or pfSense/OPNsense) on the HP t740 Thin Client](https://www.neelc.org/posts/hp-t740-freebsd/)