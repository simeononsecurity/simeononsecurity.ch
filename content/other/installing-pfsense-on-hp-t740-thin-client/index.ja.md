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
---
 HP t740 Thin Client 上の pfSense、OPNsense、または HardenedBSD**

pfSense、OPNsense、または HardenedBSD を実行するための強力なデバイスをお探しの場合は、HP t740 Thin Client が適切な選択肢となる可能性があります。

## より強力でコンパクトなホーム サーバー

HP t740 Thin Client は、強力な pfSense ボックスまたはコンパクトなホーム サーバーとして使用できるコンパクトなデバイスです。 t730 または t620 Plus よりも多くの電力を提供するため、特にファイバー インターネットを使用している場合、PPPoE を実行するのに適した選択肢になります。 10 ギガビット ネットワーキングへのアップグレード パスも提供できます。

## PS/2 フリーズ

ただし、FreeBSD や pfSense、OPNsense、HardenedBSD などの派生製品を (ESXi や Proxmox 内ではなく) ベアメタル上で実行する予定の場合、起動時にシステムが「atkbd0: [」というメッセージでフリーズする問題が発生する可能性があります。巨大ロック]`。幸いなことに、この問題はブート プロンプトで次のコマンドを入力することで解決できます。

```bash
unset hint.uart.0.at
unset hint.uart.1.at
```

*Note that you need to unset both, otherwise, it will still lock up at boot.*

After you install the OS, open a post-installation shell and run the following command:

```bash
vi /boot/loader.conf.local
```
Then, add these two lines:
```bash
hint.uart.0.disabled="1"
hint.uart.1.disabled="1"
```

### Persist Changes using VI
For those not familiar with vi, you can add the line by doing the following :

Adding the lines `hint.uart.0.disabled="1"` and `hint.uart.1.disabled="1"` to the `/boot/loader.conf.local` file using the vi editor can be done with the following steps:

1. Open the terminal on your FreeBSD system.

2. Type `vi /boot/loader.conf.local` and press Enter to open the file in the vi editor.

3. Press the `i` key to enter insert mode.

4. Move the cursor to the bottom of the file using the arrow keys.

5. Type `hint.uart.0.disabled="1"` without the quotes.

6. Press Enter to start a new line.

7. Type `hint.uart.1.disabled="1"` without the quotes.

8. Press the `Esc` key to exit insert mode.

9. Type `:wq` and press Enter to save and exit the file.

This will add the two lines to the `/boot/loader.conf.local` file, which will disable the UARTs and fix the freezing issue during boot on certain HP t740 "Thin Client" devices when running FreeBSD or its derivatives like pfSense, OPNsense, or HardenedBSD.

This will fix the issue across reboots and firmware upgrades on pfSense/OPNsense. 

## SSD

If you're using the HP M.2 eMMC, it will not be detected on an out-of-the-box FreeBSD installation. In that case, you will need a third-party M.2 SSD. Any M.2 SSD can work, SATA or NVMe. 

If you are looking for a third-party M.2 SSD for your HP t740 thin client, we recommend considering the [Western Digital 500GB WD Blue SN570 NVMe](https://amzn.to/44bFCBk) or the [Western Digital 500GB WD Blue SA510 SATA](https://amzn.to/3AEbd0V). Both of these options are reliable and should work well with your device. If you want to take advantage of both slots, you'll need both. You'll sacrifice the speeds of the NVME, but you'll gain some redundancy that's oh so important.

Note that the author of this article has successfully run pfSense CE 2.5.2 and OPNsense 22.1 on their t740 without any issues after following the above steps. 

## Troubleshooting and Post Install

After installation, if you encounter any issues with editing files, you can install the nano editor using `pkg update` and `pkg install nano`. This will help you edit text files with ease.

To ensure that the changes made to the `/boot/loader.conf.local` file persist across pfSense version upgrades, you need to add the following lines to `/boot/loader.conf` and `/etc/rc.conf.local`: 
```bash
hint.uart.0.disabled="1"
hint.uart.1.disabled="1"
```

However, sometimes the editing of `/boot/loader.conf.local` file before rebooting doesn't fix the issue. In such cases, it may be necessary to add the following lines at the beginning of the first boot:

```bash
unset hint.uart.0.at
unset hint.uart.1.at
```

これらの手順により、インストール プロセス中およびインストール プロセス後に発生する可能性のあるほとんどの問題が解決されます。

### 参考文献:
-[HP t740 "Thin Client"](https://www8.hp.com/us/en/thin-clients/t740.html)
-[pfSense](https://www.pfsense.org/)
-[OPNsense](https://opnsense.org/)
-[HardenedBSD](https://hardenedbsd.org/)
-[ServeTheHome](https://www.servethehome.com/hp-t740-thin-client-review/)
-[FreeBSD (or pfSense/OPNsense) on the HP t740 Thin Client](https://www.neelc.org/posts/hp-t740-freebsd/)