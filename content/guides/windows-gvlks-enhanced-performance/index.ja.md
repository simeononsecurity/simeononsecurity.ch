---
title: "Windows GVLKs：パフォーマンス向上のためのライセンスキーのパワーを解き放つ"
date: 2023-09-09
toc: true
draft: false
description: "Windows GVLKがどのようにパフォーマンスに革命を起こすかをご覧ください！最高のライセンシングキーを探求し、あなたのシステムの生産性を楽に向上させましょう。"
genre: ["テクノロジー", "ソフトウェア", "生産性", "オペレーティング・システム", "マイクロソフト", "ウィンドウズ", "ライセンス", "キーマネージメント", "ITソリューション", "強化"]
tags: ["ウィンドウズGVLK", "ライセンスキー", "生産性", "システム・パフォーマンス", "キーマネージメント", "オペレーティング・システム", "Windowsサーバー", "ウィンドウズ10", "ITソリューション", "ソフトウェア", "長期サービシング・チャネル", "LTSC", "長期サービシング支店", "LTSB", "強化されたパフォーマンス", "マイクロソフト", "ITマネジメント", "アクティベーション・キー", "KMSのお客様", "GVLKリスト", "ウィンドウズ版", "ライセンス認証", "クライアント・プロダクト・キー", "2019年サーバー", "サーバー2016", "ウィンドウズ11プロ", "Windows 10 Enterprise", "Windows LTSB 2016", "IT管理者"]
cover: "/img/cover/windows_gvlks_unlocked.png"
coverAlt: "カラフルな漫画で描かれた鍵がドアを開ける様子は、Windowsの可能性を最大限に引き出すGVLKの力を表現しています。"
coverCaption: "GVLKでWindowsの可能性を引き出す！"
---

## WindowsおよびWindows Server用プロダクトキー(GVLK)のインストール方法

WindowsのKMSホスト、MAK、またはリテール版からKMSクライアントにコンピュータを変換する場合、GVLK（Generic Volume License Key）としても知られる該当するプロダクトキーをインストールする必要があります。GVLKは、KMS（Key Management Services）によるボリュームのアクティベーションに使用されます。ここでは、WindowsまたはWindows ServerシステムにGVLKをインストールする方法をステップ・バイ・ステップで説明します。

## 自動GLVKインストールスクリプト

このスクリプトは、GLVKのインストールに必要なすべてのファイルを含むディレクトリで、管理者用のパワーシェルから起動する必要があります。 [GitHub Repository](https://github.com/simeononsecurity/KMS-Auto-PS/archive/main.zip)
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
Get-ChildItem -Recurse *.ps1 | Unblock-File
.\sos-kmsglvkactivationauto.ps1
```

## 手動インストールのアクティベーション手順

### 前提条件

先に進む前に、ご使用のWindowsのバージョンとエディションの有効で合法なプロダクトキーがあることを確認してください。未承認のプロダクトキーや海賊版のプロダクトキーを使用することは、Microsoftの利用規約に反しており、法的な結果につながる可能性があります。

### インストール手順

1.**スタート」ボタンを右クリックし、"Windows Terminal (Admin)" または "Command Prompt (Admin)" を選択します。Windows 11またはWindows 10を使用している場合は、"コマンドプロンプト "を検索して右クリックし、"管理者として実行 "を選択することができます。

2.**適切なプロダクトキー(GVLK)を見つける:** 以下のリストから、お使いのWindowsまたはWindows Serverのバージョンとエディションに対応するGVLKを見つけます：

   - Windows Server 2022：* Windows Server 2022 Datacenter：*
     - Windows Server 2022 Datacenter：WX4NM-KYWYW-QJJR4-XV3QB-6VM33
     - Windows Server 2022 Datacenter Azure Edition：NTBV8-9K7Q8-V27C6-M2BTV-KHMXV
     - Windows Server 2022 Standard：VDYBN-27WPP-V4HQT-9VMD4-VMK7H

   - Windows Server 2019:*
     - Windows Server 2019 Datacenter：WMDGN-G9PQG-XVVXX-R3X43-63DFG
     - Windows Server 2019 Standardです：N69G4-B89J2-4G8F4-WWYCC-J464C
     - Windows Server 2019 Essentials：WVDHN-86M7X-466P6-VHXV7-YY726

   - *Windows Server 2016:*
     - Windows Server 2016 Datacenter：CB7KF-BWN84-R7R2Y-793K2-8XDDG
     - Windows Server 2016 Standard：WC2BQ-8NRM3-FDDYY-2BFGV-KHKQY
     - Windows Server 2016 Essentials：JCKRF-N37P4-C2D82-9YXRT-4M63B

   - [Click Here to See the Others](#complete-list-of-generic-volume-license-keys-gvlk)

3.**プロダクトキー(GVLK)のインストール: **管理コマンドプロンプトで、以下のコマンドを入力します。 `<product key>`適切なGVLKで：
```sh
slmgr /ipk <product key>
```

例えば、Windows Server 2022 Datacenter版のGVLKをインストールする場合、コマンドは次のようになる：

```sh
slmgr /ipk WX4NM-KYWYW-QJJR4-XV3QB-6VM33
```

4.**コマンドを入力したら、Enterを押します。システムは指定されたプロダクトキーのインストールを試みます。

5.**インストールが成功すると、プロダクト・キーがインストールされたことを示す確認メッセージが表示されます。

確認メッセージが表示されない場合、またはキーを使用して強制的にウィンドウズのアクティベーションを試行したい場合は、以下のコマンドをお試しください：

```sh
slmgr /ato
slmgr /dlv
```

## 重要なお知らせ

- Windowsのバージョンとエディションに対して有効で合法なプロダクトキーを使用していることを常に確認してください。
- slmgr "コマンドはライセンスとアクティベーションを扱うので、注意して使用してください。
- Windows 11とWindows 10については、各エディションのGVLKの完全なリストについては、オリジナルの表を参照してください。

コンプライアンスと合法性を保つために、Microsoftのライセンス・ガイドラインと利用規約に従うことを忘れないでください。

*免責事項：この記事は情報提供のみを目的としています。プロダクトキーの使用はMicrosoftのライセンス条項に従うべきであり、誤用はユーザーの責任となります。


## ジェネリックボリュームライセンスキー(GVLK)の完全なリスト

以下の表では、Windowsの各バージョンおよびエディションのGeneric Volume License Keys (GVLK)を示しています。LTSC*はLong-Term Servicing Channel、*LTSB*はLong-Term Servicing Branchを表しています。GVLKについては、以下の表を参照してください：

### Windows Server（LTSCバージョン）

#### Windows Server 2022

| オペレーティングシステムエディション｜KMSクライアントプロダクトキー
|--------------------------------|-------------------------------|
| Windows Server 2022 Datacenter Edition｜WX4NM-KYWYW-QJR4-XV3QB-6VM33
| Windows Server 2022 Datacenter<br/>Azure Edition｜NTBV8-9K7Q8-V27C6-M2BTV-KHMXV
| Windows Server 2022 Standard<br/> VDYBN-27WPP-V4HQT-9VMD4-VMK7H

#### Windows Server 2019

| オペレーティングシステムエディション｜KMSクライアントプロダクトキー
|--------------------------------|-------------------------------|
|Windows Server 2019 Datacenter | WMDGN-G9PQG-XVXX-R3X43-63DFG
| Windows Server 2019 Standard | N69G4-B89J2-4G8F4-WWYCC-J464C
| Windows Server 2019 Essentials｜WVDHN-86M7X-466P6-VHXV7-YY726｜Windows Server 2019 Essentials｜WVDHN-86M7X-466P6-VHXV7-YY726

#### Windows Server 2016

| オペレーティングシステムエディション｜KMS クライアントプロダクトキー
|--------------------------------|-------------------------------|
| Windows Server 2016 Datacenter | CB7KF-BWN84-R7R2Y-793K2-8XDDG
| Windows Server 2016 Standard | WC2BQ-8NRM3-FDDYYY-2BFGV-KHKQY
| Windows Server 2016 Essentials | JCKRF-N37P4-C2D82-9YXRT-4M63B

### Windows Server (半期チャネル版)

#### Windows Server、バージョン 20H2、2004、1909、1903、および 1809

| オペレーティングシステムエディション｜KMSクライアントプロダクトキー
|---------------------------|-------------------------------|
| Windows Server Datacenter｜6NMRW-2C8FM-D24W7-TQWMY-CWH2D｜。
| Windows Server Standard｜N2KJX-J94YW-TQVFB-DG9YT-724CC

### Windows 11 および Windows 10 (Semi-Annual Channel バージョン)

| オペレーティングシステムエディション｜KMSクライアントプロダクトキー｜N2KX-J94W-TQVB-DG9YT-724CC
|-----------------------------------|-------------------------------|
| Windows 11 Pro<br/>Windows 10 Pro<br/>W269N-WFGWX-YVC9B-4J6C9-T83GX
| Windows 11 Pro N<br/>Windows 10 Pro N | MH37W-N47XK-V7XM9-C7227-GCQG9
| |Windows 11 Pro for Workstations<br/>Windows 10 Pro for Workstations｜NRG8B-VKK3Q-CXVCJ-9G2XF-6Q84J

| Windows 11 Pro Education<br/>Windows 10 Pro Education | 6TP4R-GNPTD-KYYHQ-7B7DP-J447Y
| Windows 11 Education<br/>Windows 10 Pro Education N｜YVWGF-BXNMC-HTQYQ-CPQ99-66QFC
| Windows 11 Education<br/>Windows 10 Education | NW6C2-QMPVW-D7KK-3GKT6-VCFB2
| Windows 11 Education N<br/>Windows 10 Education N｜2WH4N-8QGBV-H22JP-CT43Q-MDWWJ
| Windows 11 Enterprise<br/>Windows 10 Enterprise<br/>NPPR9-FWDCX-D2C8J-H872K-2YT43
| Windows 11 Enterprise N<br/>Windows 10 Enterprise N｜DPH2V-TTNVB-4X9Q3-TJR4H-KHJW4
| Windows 11 Enterprise G<br/>Windows 10 Enterprise G | YYVX9-NTFWV-6MDM3-9PT4T-4M68B
| Windows 11 Enterprise G N<br/>Windows 10 Enterprise G N｜44RPN-FTY23-9VTTB-MP9BX-T84FV

### Windows 10 (LTSC/LTSBバージョン)

#### Windows 10 LTSC 2021および2019

| オペレーティングシステムエディション｜KMSクライアントプロダクトキー｜KMSクライアントプロダクトキー
|-----------------------------------|-------------------------------|
|Windows 10 Enterprise LTSC 2021<br/>Windows 10 Enterprise LTSC 2019 | M7XTQ-FN8P6-TTKYV-9D4CC-J462D
| Windows 10 Enterprise N LTSC 2021<br/>Windows 10 Enterprise N LTSC 2019｜92NFX-8DJQP-P6BBQ-THF9C-7CG2H

#### Windows 10 LTSB 2016

| オペレーティングシステムエディション｜KMSクライアントプロダクトキー
|-----------------------------------|-------------------------------|
| Windows 10 Enterprise LTSB 2016｜DCPHK-NFMTC-H88MJ-PFHPY-QJ4BJ
| Windows 10 Enterprise N LTSB 2016 | QFFDN-GRT3P-VKWWX-X7T3R-8B639

#### Windows 10 LTSB 2015

| KMSクライアントプロダクトキー
|-----------------------------------|-------------------------------|
Windows 10 Enterprise 2015 LTSB | WNMTR-4C88C-JK8YV-HQ7T2-76DF9 | | Windows 10 Enterprise 2015 LTSB N | 2F77B-TNFGY-69
| Windows 10 Enterprise 2015 LTSB N | 2F77B-TNFGY-69QF-B8YKP-D69TJ

### 以前のバージョンの Windows Server

#### Windows Server バージョン 1803

| オペレーティングシステムのエディション｜KMSクライアントのプロダクトキー
|---------------------------|-------------------------------|
| Windows Server Datacenter｜2HXDN-KRXHB-GPYC7-YCKFJ-7FVDG
| Windows Server Standard｜PTXN8-JFHJM-4WC78-MPCBR-9W4KR

#### Windows Server バージョン 1709

| KMSクライアントのプロダクトキー
|---------------------------|-------------------------------|
| Windows Server Datacenter｜6Y6KB-N82V8-D8CQV-23MJW-BWTG6
| Windows Server Standard｜DPCNP-XQFKJ-BJF7R-FRC8D-GF6G4｜｜です。

#### Windows Server 2012 R2

| オペレーティングシステムエディション｜KMS クライアントプロダクトキー｜DPCNP-XQKJ-BJ7R-FRCD-GF6G4
|----------------------------------------|-------------------------------|
| Windows Server 2012 R2 Standard｜D2N9P-3P6X9-2R39C-7RTCD-MDVJX
| Windows Server 2012 R2 Datacenter｜W3GGN-FT8W3-Y4M27-J84CP-Q3VJ9
| Windows Server 2012 R2 Essentials | KNC87-3J2TX-XB4WP-VCPJV-M4FWM

#### Windows Server 2012

| オペレーティングシステムエディション｜KMS クライアントプロダクトキー
|-----------------------------------------|-------------------------------|

| Windows Server 2012 N｜8N2M2-HWPGY-7PGT9-HGDD8-GVGGY
| Windows Server 2012 単一言語版｜2WN2H-YGCQR-KFX6K-CD6TF-84YXQ
| Windows Server 2012 各国語版 | 4K36P-JN4VD-GDC6V-KDT89-DYFKP
| Windows Server 2012 Standard｜XC9B7-NBPP2-83J2H-RHMBY-92BT4
| Windows Server 2012 MultiPoint Standard｜HM7DN-YVMH3-46JC3-XYTG7-CYQJJ
| Windows Server 2012 MultiPoint Premium｜XNH6W-2V9GX-RGJ4K-Y8X6F-QGJ2G
| Windows Server 2012 Datacenter | 48HP8-DN98B-MYWDG-T2DCC-8W83P

#### Windows Server 2008 R2

| オペレーティングシステムエディション｜KMSクライアントプロダクトキー｜### Windows Server 2008 R2
|--------------------------------------------------|-------------------------------|
| Windows Server 2008 R2 Web エディション｜6TPJF-RBVHG-WBW2R-86QPH-6RTM4
| Windows Server 2008 R2 HPC エディション | TT8MH-CG224-D3D7Q-498W2-9QCTX
| Windows Server 2008 R2 Standard エディション｜YC6KT-GKW9T-YTKYR-T4X34-R7VHC
| Windows Server 2008 R2 Enterprise | 489J6-VHDMP-X63PK-3K798-CPX3Y
| Windows Server 2008 R2 Datacenter｜74YFP-3QFB3-KQT8W-PMXWJ-7M648
| Windows Server 2008 R2 for Itanium-based Systems | GT63C-RJFQ3-4GMB6-BRFB9-CB83V

#### Windows Server 2008

| オペレーティングシステムエディション｜KMSクライアントプロダクトキー
|------------------------------------------------|-------------------------------|
| Windows Web Server 2008｜WYR28-R7TFJ-3X2YQ-YCY4H-M249D
| Windows Server 2008 Standard｜TM24T-X9RMF-VWXK6-X8JC9-BFGM2
| Windows Server 2008 Standard Hyper-V非対応モデル｜W7VD6-7JFBR-RX26B-YKQ3Y-6FFFJ
| Windows Server 2008 Enterprise｜YQGMW-MPWTJ-34KDK-48M3W-X4Q6V｜Hyper-V非搭載のWindows Server 2008 Enterprise。
| Windows Server 2008 Enterprise Hyper-V非対応モデル｜39BXF-X8Q23-P2WWT-38T2F-G3FPG
| Windows Server 2008 HPC RCTX3-KWVHP-BR6TB-RB6DM-6X7HP
| Windows Server 2008 Datacenter｜7M67G-PC374-GR742-YH8V4-TCBY3
| Windows Server 2008 Datacenter Hyper-V非対応｜22XQ2-VRXRG-P8D42-K34TD-G3QQC｜Windows Server 2008 for Itanium-Based｜7M67GPC374-GR742-YH8V4-TCBY3
| Windows Server 2008 for Itanium-Based Systems｜4DWFP-JF3DJ-B7DTH-78FJB-PDRHK

### 以前のバージョンのWindows

#### Windows 8.1

| オペレーティングシステムエディション｜KMSクライアントプロダクトキー
|--------------------------|-------------------------------|
| Windows 8.1 Pro｜GCRJD-8NW9H-F2CDX-CCM8D-9D6T9
| Windows 8.1 Pro N｜HMCNV-VVBFX-7HMBH-CTY9B-B4FXY
| Windows 8.1 Enterprise N｜MHF9N-XY6XB-WVXMC-BTDCT-MKKG7
Windows 8.1 Enterprise N | TT4HM-HN7YT-62K67-RGRQJ-JFFXW | Windows 8.1 Enterprise N | TT4HM-HN7YT-62K67-RGRQJ-JFFXW

#### Windows 8

| KMSクライアントプロダクトキー
|--------------------------|-------------------------------|
| Windows 8 Pro｜NG4HW-VH26C-733KW-K6F98-J8CK4
| Windows 8 Pro N | XCVCF-2NXM9-723PB-MHCB7-2RYQQ
| Windows 8 Enterprise N｜JMNW-9KQ84-P47T8-D8GGY-CWCK7
| Windows 8 Enterprise N｜JMNMF-RHW7P-DMY6X-RF3DR-X2BQT

#### Windows 7

| オペレーティングシステムエディション｜KMSクライアントプロダクトキー
|--------------------------|-------------------------------|
| Windows 7 プロフェッショナル版｜FJ82H-XT6CR-J8D7P-XQJJ2-GPDD4
| Windows 7 プロフェッショナル N｜MRPKT-YTG23-K7D7T-X2JMM-QY7MG
| Windows 7 プロフェッショナル E｜W82YF-2Q76Y-63HXB-FGJG9-GF7QX
| Windows 7 Enterprise｜33PXH-7Y6KF-2VJC9-XBBR8-HVTHH
| Windows 7 Enterprise N｜YDRBP-3D83W-TY26F-D46B2-XCKRJ
| Windows 7 Enterprise E｜C29WB-22CC8-VJ326-GHFJW-H9DH4

#### Windows Vista

| オペレーティングシステムエディション｜KMSクライアントプロダクトキー
|--------------------------|-------------------------------|
|Windows Vista ビジネス｜YFKBB-PQJJV-G996G-VWGXY-2V3X8
|Windows Vista Business N｜HMBQG-8H2RH-C77VX-27R82-VMQBT
|Windows Vista Enterprise｜VKK3X-68KWM-X2YGT-QR4M6-4BWMV
|Windows Vista Enterprise N VTC42-BM838-43QHV-84HX6-XJXKV

## 参考文献
- [Key Management Services (KMS) client activation and product keys](https://learn.microsoft.com/en-us/windows-server/get-started/kms-client-activation-keys)