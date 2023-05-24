---
title: "コマンドラインSSH経由のUbiquiti Unifi UDM ProおよびUDM SEのオフラインファームウェアアップデート"
draft: false
toc: true
date: 2023-05-28
description: "最適なパフォーマンスとセキュリティを実現するために、コマンド ライン SSH を使用して Ubiquiti Unifi UDM Pro および UDM SE のファームウェアをオフラインで更新する方法を学びます。"
tags: ["ユビキティファームウェアアップデート", "UDM プロ", "UDM SE", "オフラインファームウェアアップデート", "コマンドラインSSH", "ネットワーク管理", "ネットワークセキュリティー", "ファームウェアのアップグレード", "SSH接続", "ファームウェアファイル", "UniFi ネットワーク コントローラー", "バグの修正", "パフォーマンスの向上", "セキュリティパッチ", "ネットワーキング", "ネットワークデバイス", "テクノロジー", "IT管理", "ファームウェアアップデートプロセス", "ネットワークの最適化", "ユビキティネットワークファームウェアアップデート", "UDM Pro ファームウェアのアップデート", "UDM SEファームウェアアップデート", "オフラインファームウェアアップデートプロセス", "SSHファームウェアアップデート", "ネットワークデバイス管理", "ネットワークセキュリティアップデート", "ファームウェアのアップデート戦略", "オフラインファームウェア管理", "ネットワークパフォーマンスの最適化", "セキュリティパッチ管理", "ネットワーキングテクノロジーのアップデート"]
cover: "/img/cover/A_colorful_illustration_depicting_a_computer_connecting.png"
coverAlt: "SSH を介してルーターに接続するコンピューターを描いたカラフルなイラストは、Ubiquiti Unifi UDM Pro および UDM SE デバイスのオフライン ファームウェア アップデート プロセスを象徴しています。"
coverCaption: ""
---

**Ubiquiti Unifi UDM Pro および UDM SE を SSH 経由でオフラインで更新します**

ネットワーキングの世界では、**ユビキティ ネットワーク** はその革新的なソリューションで知られています。 **Ubiquiti Unifi Dream Machine Pro (UDM Pro)** と **Unifi Dream Machine SE (UDM SE)** は、包括的なネットワーク管理機能を提供する 2 つの人気のある製品です。最適なパフォーマンスとセキュリティを確保するには、これらのデバイスのファームウェアを更新することが重要です。この記事では、コマンドライン SSH を使用して、**オフライン**で UDM Pro および UDM SE のファームウェアを更新する方法を説明します。

______

## ファームウェアを更新する理由

ファームウェアの更新にはバグ修正、パフォーマンスの向上、セキュリティ パッチが含まれることが多いため、あらゆるネットワーク デバイスにとって不可欠です。ネットワークの安全性を確保し、スムーズに動作させるには、UDM Pro および UDM SE のファームウェアを定期的に更新することが重要です。

______

## オフラインファームウェアアップデート

UDM Pro および UDM SE のファームウェアの更新は、**UniFi ダッシュボード** から実行できます。ただし、シナリオによっては、インターネット接続が利用できない、またはインターネット接続が望ましくない場合があります。このような場合、コマンドライン SSH を使用したオフライン更新が代替ソリューションとなります。

______

## オフライン更新の準備

オフライン更新を続行する前に、次の前提条件を満たしていることを確認してください。

1. SSH クライアントがインストールされているコンピューターまたはデバイス。
2. UDM Pro または UDM SE の最新のファームウェア ファイル。ファームウェア ファイルは次から入手できます。 [Ubiquiti Downloads](https://www.ui.com/download/unifi) for the [UDM Pro](https://www.ui.com/download/unifi/unifi-dream-machine-pro) page. For early access firmwares, you can see them on the [community releases page](https://community.ui.com/releases) once you've signed into your.[**ui.com**](https://account.ui.com/) アカウント

______

## SSH接続の確立

コマンドライン SSH 経由で UDM Pro または UDM SE を更新するには、次の手順に従います。

1. コンピュータまたはデバイスが UDM Pro または UDM SE と同じネットワークに接続されていることを確認します。
2. 優先 SSH クライアントを開き、**UDM Pro または UDM SE の IP アドレス**への SSH 接続を確立します。たとえば、Linux または macOS で **OpenSSH クライアント**を使用すると、次のコマンドを使用できます。

```bash
ssh root@<UDM_IP_ADDRESS>
```

交換 `<UDM_IP_ADDRESS>` UDM Pro または UDM SE の実際の IP アドレスに置き換えます。

3. プロンプトが表示されたら、**ユーザー名** と **パスワード** を入力します。 Ubiquiti デバイスのデフォルトの認証情報は通常、 `ubnt` ユーザー名とパスワードの両方について。

______

## ファームウェアの更新

SSH 接続を確立したら、ファームウェアのアップデートを続行できます。

1. **SCP (セキュア コピー)** を使用して、ファームウェア ファイルを UDM Pro または UDM SE にアップロードします。 SCP により、SSH 経由で安全なファイル転送が可能になります。ファームウェア ファイルがローカル マシン上にあると仮定すると、次のコマンドを使用できます。

```bash
scp <FIRMWARE_FILE_PATH> ubnt@<UDM_IP_ADDRESS>:/root/fwupdate.bin
```

交換 `<FIRMWARE_FILE_PATH>` ローカル マシン上のファームウェア ファイルへのパスを使用して、 `<UDM_IP_ADDRESS>` UDM Pro または UDM SE の IP アドレスに置き換えます。

2. ファームウェア ファイルがアップロードされたら、ファームウェアの更新プロセスを開始できます。次のコマンドを実行します。

```bash
ssh ubnt@<UDM_IP_ADDRESS> "ubnt-tools fwupdate /root/fwupdate.bin"
```

3. UDM Pro または UDM SE がファームウェアのアップデート プロセスを開始します。ちょっと時間かかります。 **更新が完了するまでプロセスを中断しないでください**。

4. アップデートが完了したら、UniFi ネットワーク コントローラーにログインするか、次のコマンドを実行して、ファームウェアのバージョンを確認できます。

```bash
ssh ubnt@<UDM_IP_ADDRESS> "show version"
```
上記のプロセスは、UDM Pro または UDM SE に必要なファームウェア ファイルがあることを前提としていることに注意してください。特定のデバイスのモデルとバージョンに対応した正しいファームウェア ファイルがあることを確認してください。

＃＃ 結論

Ubiquiti Unifi UDM Pro および UDM SE デバイスのファームウェアを更新することは、最適なパフォーマンスとセキュリティを確保するための重要な手順です。 UniFi ネットワーク コントローラーはファームウェアをアップデートする便利な方法を提供しますが、インターネット接続が利用できない場合、またはインターネット接続が望ましくない場合は、コマンド ライン SSH を介してオフライン アップデートを実行することが実行可能な解決策となります。

この記事で説明されている手順に従うと、コマンドライン SSH を使用して UDM Pro および UDM SE デバイスのファームウェアを正常に更新できます。バグ修正、パフォーマンス向上、セキュリティ パッチを活用するには、ユビキティ ネットワークスが提供する最新のファームウェア バージョンを常に使用してください。

## 参考文献

- [Ubiquiti Downloads](https://www.ui.com/download/unifi/) - ファームウェア ファイルの公式 Ubiquiti ダウンロード ページ。
- [Unifi Advanced Updating Techniques](https://help.ui.com/hc/en-us/articles/204910064-UniFi-Upgrade-the-Firmware-of-a-UniFi-Device)
