---
title: "PowerShell DSC：スタートガイド"
date: 2023-04-02
toc: true
draft: false
description: "PowerShell Desired State Configuration (DSC)を使用して、安全でコンプライアンスに準拠した環境のためのシステム構成を自動化および管理する方法を説明します。"
tags: ["パワーシェル", "ディスクロージャー", "コンフィギュレーションマネジメント", "オートメーション", "ウィンドウズ", "システム管理", "ベストプラクティス", "コンプライアンス", "セキュリティ", "インフラストラクチャー", "デブオプス", "サーバー構成", "テスト", "ギット", "ソースコントロール", "政府規制", "エヌアイエスティー", "CIS", "コンフィギュレーションドリフト", "カスタムリソース"]
cover: "/img/cover/A_cartoon_image_of_a_confident_system_administrator.png"
coverAlt: "スーパーヒーローのマントを羽織った自信に満ちたシステム管理者が、整然としたサーバーラックの横に立ち、片手にPowerShell DSCスクリプト、もう片手にWindowsロゴの入った盾を持ち、設定ドリフトやセキュリティ脅威からサーバーを守っている漫画のような画像です。"
coverCaption: ""
---

**PowerShell Desired State Configuration (DSC)を使った構成管理ガイド**」を掲載しました。

______

## 序章

PowerShell Desired State Configuration (**DSC**) は、IT 管理者や DevOps 担当者にとって強力かつ **不可欠なツール** であり、Windows および Linux システムの展開と構成を自動化することが可能です。この記事では、構成管理のためにPowerShell DSCを使用するための包括的なガイドを提供し、ベストプラクティス、政府規制、および有用なリファレンスを含みます。

______

## PowerShell Desired State Configuration を使い始めよう

### PowerShell Desired State Configurationとは？

PowerShell Desired State Configuration (**DSC**) は、PowerShell に組み込まれた **宣言言語** で、管理者がシステム、アプリケーション、およびサービスの構成を自動化することを可能にします。DSCは、システム、アプリケーション、およびサービスの構成を自動化するための、**標準化された一貫性のある**方法を提供し、システムを望ましい状態に保つことを保証します。

### PowerShell DSCのインストール

PowerShell DSCを使い始めるには、**Windows Management Framework (WMF)**をインストールする必要があります。WMFは、PowerShell、DSC、その他の必須管理ツールを含むパッケージです。WMFの最新版は、以下のサイトからダウンロードできます。 [Microsoft Download Center](https://www.microsoft.com/en-us/download/details.aspx?id=54616)

______

## DSCコンフィギュレーションの作成と適用

### DSCコンフィギュレーションの作成

DSC 構成は、システムの望ましい状態を記述する **PowerShell スクリプト** です。システムのコンポーネントに必要な設定やプロパティを定義する1つまたは複数の**DSCリソース**で構成されます。ここでは、WindowsサーバーにWebサーバー（IIS）ロールをインストールする簡単なDSC構成の例を示します：

```powershell
Configuration InstallIIS {
    Import-DscResource -ModuleName PSDesiredStateConfiguration

    Node 'localhost' {
        WindowsFeature IIS {
            Ensure = 'Present'
            Name   = 'Web-Server'
        }
    }
}
```
### DSC 設定の適用
DSC 構成を記述したら、**Start-DscConfiguration** コマンドレットを使用してターゲットシステムに適用することができます。まず、PowerShellでコンフィギュレーションスクリプトを実行してコンパイルします：

```powershell
InstallIIS
```

これにより、コンパイルされた構成を含む**MOF**ファイル(Managed Object Format)が生成されます。次に、以下のコマンドを使用して、ターゲット・システムにコンフィグレーションを適用します：

```powershell
Start-DscConfiguration -Path .\InstallIIS -Wait -Verbose
```

## PowerShell DSCの使用に関するベストプラクティス

### 構成をモジュール化する

インフラストラクチャのさまざまなコンポーネントを **個々の DSC リソース** に分離することで、**モジュール化された再利用可能な**コンフィギュレーションを作成します。このアプローチにより、環境の成長に合わせて構成を簡単に **維持および拡張** することができます。

### ソース管理の使用

DSCの設定とカスタムリソースは、常にGitのような**ソース管理システム**に保存してください。この方法によって、変更点の追跡、チームとのコラボレーション、必要なときに以前のバージョンの構成に戻すことが容易になります。

### 設定をテストする

**テストは、構成管理の重要な側面です。DSC 構成を展開する前に、**非本番環境**でテストし、期待通りに動作し、意図しない結果をもたらさないことを確認します。また、以下のようなツールを使用することができます。 [Pester](https://github.com/pester/Pester)DSCのコンフィギュレーションを自動テストするためのものです。

______

## 政府規制とガイドライン

### NIST ガイドライン

米国国立標準技術研究所（NIST）は、システム構成管理に関するガイドラインを提供しています。特に、その [NIST SP 800-53](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r5.pdf) publication contains a section (CM-2)DSC の使用に関連する「ベースラインコンフィギュレーション」に関するガイドラインです。このガイドラインでは、システム構成の変更を維持、監視、制御することの重要性が強調されています。PowerShell DSCは、システム構成を管理するための一貫した自動化された方法を提供することで、組織がこれらのガイドラインに準拠するのを助けることができます。

### 連邦情報セキュリティ管理法(FISMA)

連邦情報セキュリティ管理法 [FISMA](https://www.dhs.gov/cisa/federal-information-security-modernization-act)は、連邦政府機関に対して、情報セキュリティ管理の有効性を確保するための包括的な枠組みを導入することを求めています。構成管理は FISMA コンプライアンスの重要な要素であり、PowerShell DSC は、組織がこれらの要件を満たすために不可欠な役割を果たすことができる。
______

## 結論

PowerShell Desired State Configuration (DSC) は、システム構成の展開と管理を自動化するための強力かつ柔軟なツールです。ベストプラクティスに従い、政府の規制を遵守することで、コンプライアンスを維持しながら、組織のシステムを望ましい状態に保つことができます。PowerShell DSCの理解を深め、構成管理プロセスを改善するために、この記事で提供されたリソースを活用することを忘れないでください。
______

## 参考文献

- [PowerShell Desired State Configuration (DSC) official documentation](https://learn.microsoft.com/en-us/powershell/dsc/getting-started/wingettingstarted?view=dsc-1.1)
- [NIST SP 800-53 - Security and Privacy Controls for Federal Information Systems and Organizations](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r5.pdf)
- [Federal Information Security Management Act (FISMA)](https://www.dhs.gov/cisa/federal-information-security-modernization-act)
- [Pester - PowerShell Testing Framework](https://github.com/pester/Pester)
- [A Beginner's Guide to Using Encryption for Data Protection](https://simeononsecurity.com/articles/a-beginners-guide-to-using-encryption-for-data-protection/)
- [Best Practices for Installing Security Patches on Windows](https://simeononsecurity.com/articles/best-practices-for-installing-security-patches-on-windows/)




