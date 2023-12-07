---
title: "vTPMで仮想マシンのセキュリティを強化：ステップバイステップガイド"
date: 2023-09-02
toc: true
draft: false
description: "包括的なステップバイステップのガイドでvTPMを使用して仮想マシンのセキュリティを強化し、プラットフォームの認証とBitLocker暗号化のサポートを提供します。"
genre: ["サイバーセキュリティ", "仮想化", "VMware", "ブイ・スフィア", "セキュリティ", "トラステッド・プラットフォーム・モジュール", "ブイティピーエム", "ゲストOS", "暗号化", "プラットフォーム認証"]
tags: ["仮想信頼プラットフォーム・モジュール", "vTPMガイド", "VMセキュリティの強化", "プラットフォーム認証", "ビットロッカー暗号化", "VMware vSphere", "仮想化セキュリティ", "サイバーセキュリティ", "ゲストOSの保護", "VMハードウェア", "TPM 2.0", "セキュアブート", "暗号操作", "VMセキュリティのベストプラクティス", "vCenterサーバー", "ESXiホスト", "EFIファームウェア", "キー・プロバイダー", "VMwareドキュメント", "Windowsサーバー", "ウィンドウズ7", "リナックスOS", "セキュアなVM構成", "セキュリティ機能", "vSphereクライアント", "バーチャルチップ", "データ保護", "タンパー検出", "VMの完全性の検証", "VMwareのセキュリティ"]
cover: "/img/cover/enhanced-vm-security.png"
coverAlt: "vTPMによって強化されたセキュリティを表す、輝くロックを持つ仮想マシンを象徴的に示す図。"
coverCaption: "前例のないVMセキュリティのロックを解除！"
---

## 既存の仮想マシンで仮想Trusted Platform Moduleを有効にする

仮想トラステッドプラットフォームモジュール（vTPM）は、仮想マシン上で実行されるゲストオペレーティングシステムのセキュリティを強化する重要なセキュリティ機能です。この記事では、VMware vSphere 環境の既存の仮想マシンに vTPM を追加する手順と、シームレスな実装を実現するための重要な考慮事項について説明します。

______

## 前提条件

仮想マシンにvTPMを追加する前に、以下の前提条件を満たしていることを確認してください：

1.**vSphere 環境にキープロバイダーが設定されていること。この手順は、暗号化処理を安全に管理するために非常に重要です。このステップは、暗号化操作を安全に管理するために非常に重要です。 [vSphere Security documentation](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.security.doc/GUID-52188148-C579-4F6A-8335-CFBCE0DD2167.html)を参照されたい。

2.**サポートされるゲストOS:** ゲストOSがvTPMと互換性があることを確認してください。VMware vTPMはTPM 2.0と互換性があり、Windows Server 2008以降、Windows 7以降、およびさまざまなLinuxディストリビューションをサポートしています。

3.**仮想マシンのステータス:** vTPMの追加を行う前に、変更する仮想マシンがオフになっていることを確認します。

4.**ESXiホストのバージョン:** 環境のESXiホストは、WindowsゲストOSのESXi 6.7以降、またはLinuxゲストOSのESXi 7.0 Update 2のいずれかを実行している必要があります。

5.**EFIファームウェア:** 仮想マシンは、vTPMをサポートするためにEFIファームウェアを使用する必要があります。

6.**必要な権限:** vTPM を追加および管理するための暗号操作に必要な権限があることを確認します。必要な権限は以下のとおりです：
   - 暗号化操作.クローン
   - 暗号化操作.暗号化
   - 暗号化操作.Encrypt new
   - 暗号化操作.Migrate
   - 暗号化操作：VMの登録



## 仮想トラステッドプラットフォームモジュール(vTPM)の追加

以下の手順に従って、既存の仮想マシンにvTPMを追加します：

1.**vSphere Clientを起動し、vCenter Serverにログインします。

2.**vSphere Clientの左側にあるインベントリで、変更する仮想マシンを探します。仮想マシン名を右クリックし、"Edit Settings "を選択します。

3.**Edit Settings "ダイアログボックスで、"Add New Device "ボタンをクリックします。デバイスタイプのリストから、「Trusted Platform Module」（vTPM）を選択します。

4.4. **Confirm Selection:**「OK」ボタンをクリックして、vTPMデバイスを仮想マシンに追加します。

5.5. **Verify Addition:** vTPMの追加に成功すると、仮想マシンのSummaryタブに "Virtual Trusted Platform Module "がVM Hardwareペインに表示されます。

______

## 仮想トラステッドプラットフォームモジュール（vTPM）の利点

仮想マシンでvTPMを有効にすると、いくつかの大きなメリットがあります：

1.**セキュリティの強化：*** vTPMは仮想マシン用に仮想化されたTPM 2.0チップを作成し、セキュアブートや暗号化操作などのハードウェアベースのセキュリティ機能を提供します。これにより、ゲストオペレーティングシステムのセキュリティ態勢が強化されます。

2.**プラットフォーム認証：** vTPM は、仮想マシンが自身の状態の暗号化測定を生成し、プラットフォーム認証を可能にします。この機能により、仮想マシンの完全性が検証され、改ざんされていないことが保証されます。

3.**BitLocker暗号化のサポート：** WindowsゲストOSを実行している場合、vTPMを有効にすることは、仮想マシンのディスクでBitLocker暗号化を使用するための前提条件です。これにより、データ保護のレイヤーが追加されます。



## 結論

既存の仮想マシンに仮想トラステッドプラットフォームモジュール（vTPM）を実装することは、仮想化インフラス トラクチャのセキュリティを強化するための重要なステップです。説明した手順に従い、すべての前提条件を満たすようにすることで、ゲストオペレーティングシステムの強化されたセキュリティ機能、プラットフォーム認証、およびBitLocker暗号化サポートを有効にすることができます。

vSphere のバージョンと構成に関する詳細については、VMware の公式ドキュメントを参照してください。

______

## 参考文献

- [VMware vSphere Security Documentation](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.security.doc/GUID-52188148-C579-4F6A-8335-CFBCE0DD2167.html)
- [VMware vSphere Documentation](https://docs.vmware.com/en/VMware-vSphere/index.html)
- [Trusted Platform Module (TPM) Overview](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.vm_admin.doc/GUID-A43B6914-E5F9-4CB1-9277-448AC9C467FB.html)
- [BitLocker Encryption Overview](https://docs.microsoft.com/en-us/windows/security/information-protection/bitlocker/bitlocker-overview)

