---
title: "Microsoft Defender for Cloud でクラウド環境を保護する"
date: 2023-04-10
lastmod: 2026-11-14
toc: true
draft: false
description: "Microsoft Defender for Cloud を使って Azure ワークロードを保護する方法を説明します。Azure Security Center の旧称、推奨事項、ポリシー、対応手順も確認します。"
tags: ["Azure", "Security Center", "クラウドセキュリティ", "Azure Sentinel", "Azure Defender", "ネットワークセキュリティ", "ID管理", "データセキュリティ", "脅威検出", "脅威対応", "MFA", "RBAC", "NSGs", "Azure Firewall", "WAF", "Azure AD", "Azure Information Protection", "Azure Storage Service Encryption", "Azure Disk Encryption"]
cover: "/img/cover/A_shield_icon_surrounded_by_cloud_symbols.webp"
coverAlt: "クラウドの記号に囲まれた盾が、安全なクラウド環境を表しています。盾には Azure Security Center のロゴがあります。"
coverCaption: ""
---

**Azure Security Centerによるクラウド環境のセキュリティ確保方法**」。

クラウド環境のセキュリティ確保は、組織のデータ、アプリケーション、インフラを脅威から保護するために不可欠です。マイクロソフトの**Azure Security Center**は、セキュリティ態勢を強化し、Azure環境における潜在的なリスクを迅速に特定するのに役立つ強力なツールです。この記事では、Azure Security Centerを使用してクラウド環境を保護する方法について説明し、さまざまなセキュリティ機能を実装するための推奨される実践方法を取り上げます。さらに、この記事では、Azure Security Centerを使用してクラウド環境を保護する方法をよりよく理解するために、より技術的な詳細と例に飛び込んでいきます。

______

*この記事の初版以降、製品名が変更されました。Microsoft Azure Security Center は Microsoft Defender for Cloud に、Azure Active Directory は Microsoft Entra ID に、Azure Sentinel は Microsoft Sentinel に名称変更されました。Azure Defender は Defender for Cloud のプランとワークロード保護を指します。2023年当時の用語を説明する箇所では旧名称を残しています。*

現在の [Defender for Cloud の概要](https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-cloud-introduction)では、クラウドセキュリティ態勢管理、DevSecOps、クラウドワークロード保護を備えたクラウドネイティブ アプリケーション保護プラットフォームとして説明されています。機能とライセンスの提供状況は、クラウド、リソースの種類、サブスクリプション、プランによって異なります。

## Azure Security Centerを理解する

Azure Security Centerは、クラウド環境における潜在的な脆弱性の特定と対処を支援する**統合型インフラストラクチャ セキュリティ管理システム**です。脅威の検出、セキュリティ姿勢の管理、コンプライアンス管理など、いくつかの機能を提供し、Azure環境が常に安全であることを保証します。

**継続的なセキュリティ評価**と**高度な脅威保護**は、Azure Security Centerの2つの主要機能です。継続的なセキュリティアセスメントは、環境内の潜在的なセキュリティ問題の特定を支援し、高度な脅威保護は、潜在的な脅威の検出と対応を支援します。

______

## セキュリティポリシーとコンプライアンス標準の実装

Azure Security Center では、クラウド環境全体でセキュリティポリシーを実装し管理することができます。Azure Policy** サービスを使用してカスタムセキュリティポリシーを作成したり、組み込みポリシーを使用して推奨される実践方法やコンプライアンス標準を適用したりできます。また、セキュリティ態勢を業界標準と照らし合わせて評価できます。該当する基準には、[NIST 800-53](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final)、[CIS](https://www.cisecurity.org/)、[ISO 27001](https://www.iso.org/isoiec-27001-information-security.html)があります。

Azure Security Centerは、コンプライアンス管理機能も備えており、組織がさまざまな規制の枠組みにどの程度準拠しているかを確認できます。代表的な枠組みには、[GDPR](https://gdpr.eu/)、[HIPAA](https://www.hhs.gov/hipaa/index.html)、[PCI DSS](https://www.pcisecuritystandards.org/)があります。

______

## Azureリソースの安全確保

**リソースセキュリティ衛生**は、クラウド環境を保護するための重要な側面です。Azure Security Centerは、お客様のセキュリティ態勢の測定である**Secure Score**を提供し、お客様のリソースの全体的なセキュリティを理解するのに役立ちます。Azure Security Centerが提供する推奨事項に対処することで、Secure Scoreを向上させることができます。

### ネットワークセキュリティ

ネットワークセキュリティグループ（NSG）**、**Azure Firewall**、*Web Application Firewall（WAF）**などの適切なネットワークセキュリティ対策を実施することは、潜在的な脅威からAzure環境を保護するために非常に重要です。これらのツールは、入出力のネットワークトラフィックを制御し、不正アクセスや潜在的な攻撃からリソースを保護するのに役立ちます。

#### ネットワークセキュリティグループ(NSG)

NSG は、Azure リソースの仮想ファイアウォールとして機能し、リソースへのネットワークトラフィッ クを許可または拒否するルールを定義することができます。たとえば、特定のトラフィックを許可または拒否するルールを持つ NSG を作成することができます：

```azurecli
# ネットワーク セキュリティ グループを作成する
az network nsg create --name MyNSG --resource-group MyResourceGroup

# トラフィックを許可または拒否するルールを追加する
az network nsg rule create --name MyNSGRule --nsg-name MyNSG --priority 100 --resource-group MyResourceGroup --access Allow --protocol Tcp --direction Inbound --source-address-prefixes '*' --source-port-ranges '*' --destination-address-prefixes '*' --destination-port-ranges '80'
```
について詳しくはこちら[Network Security Groups](https://docs.microsoft.com/en-us/azure/virtual-network/security-overview) 本番環境では全 IPv4 送信元を許可せず、既知の送信元範囲を指定してください。[NSG セキュリティの概要](https://learn.microsoft.com/en-us/azure/virtual-network/network-security-groups-overview)を確認してください。を公式ドキュメントに掲載しています。

#### Azure Firewall（アジュールファイアウォール
Azure Firewallは、Azureリソースを保護する、マネージド型のクラウドベースのネットワークセキュリティサービスです。脅威インテリジェンスベースのフィルタリング、ウェブカテゴリ、集中型ロギングと分析などの高度な機能を提供します。Azure Firewall をセットアップするには、以下の手順に従います。[quickstart instructions](https://learn.microsoft.com/en-us/azure/firewall-manager/quick-firewall-policy-bicep)

#### ウェブアプリケーションファイアウォール(WAF)
Web Application Firewall (WAF) は、**Azure Application Gateway** の機能で、SQL インジェクション、クロスサイトスクリプティングなどの一般的な Web 悪用やその他の脅威から Web アプリケーションを保護するものです。WAFは、既存のWebアプリケーションと簡単に統合でき、特定の攻撃パターンから保護するためのカスタムルールを設定することができます。

以下は、WAFを有効にしたアプリケーションゲートウェイを作成する方法の例です：
```azurecli
# WAF ポリシーを作成する
az network application-gateway waf-policy create --name MyWafPolicy --resource-group MyResourceGroup --location EastUS

# 仮想ネットワークとサブネットを作成する
az network vnet create --name MyVNet --resource-group MyResourceGroup --location EastUS --address-prefix 10.0.0.0/16
az network vnet subnet create --name MySubnet --resource-group MyResourceGroup --vnet-name MyVNet --address-prefix 10.0.0.0/24

# パブリック IP アドレスを作成する
az network public-ip create --name MyPublicIP --resource-group MyResourceGroup --location EastUS --sku Standard

# WAF を有効にした Application Gateway を作成する
az network application-gateway create --name MyAppGateway --resource-group MyResourceGroup --location EastUS --vnet-name MyVNet --subnet MySubnet --public-ip-address MyPublicIP --http-settings-cookie-based-affinity Enabled --sku WAF_v2 --waf-policy MyWafPolicy

```
について詳しくはこちら[Web Application Firewall](https://docs.microsoft.com/en-us/azure/web-application-firewall/ag/ag-overview)を公式ドキュメントに掲載しています。

### Identity and Access Management（アイデンティティとアクセス管理

**Azure Active Directory (Azure AD)**は、クラウド環境のセキュリティを確保するために不可欠なコンポーネントです。Azure Security Centerでは、**多要素認証（MFA）**の有効化、**役割ベースのアクセス制御（RBAC）**の実装、疑わしいアクティビティの監視など、IDおよびアクセス管理の改善に向けた推奨事項を提供しています。

#### 多要素認証(MFA)

MFA は、アクセスを許可する前にユーザーに 2 つ以上の検証形式を要求することで、Azure AD アカウントに追加のセキュリティ層を追加します。以下の手順に従って、組織の MFA を有効にすることができます。[step-by-step guide](https://docs.microsoft.com/en-us/azure/active-directory/authentication/tutorial-enable-azure-mfa)マイクロソフト社から提供されています。

例あるユーザーに対してMFAを有効にする

```powershell
# Azure AD に接続
Connect-AzureAD

# 特定のユーザーに MFA を有効化
$UserPrincipalName = "johndoe@example.com"
$StsUserObjectID = (Get-AzureADUser -Filter "UserPrincipalName eq '$UserPrincipalName'").ObjectId
$StrongAuthRequirements = @(@{"Location"=""; "SatisfactionFactor"="2"; "VerificationMethod"="1"};@{"Location"=""; "SatisfactionFactor"="2"; "VerificationMethod"="2"})
Set-AzureADUser -ObjectId $StsUserObjectID -StrongAuthenticationRequirements $StrongAuthRequirements
```
#### ロールベースアクセスコントロール(RBAC)
RBAC を使用すると、Azure リソースの詳細なアクセス許可を定義し、ユーザーが適切なレベルのアクセス権を持つことを保証できます。ユーザー、グループ、またはアプリケーションにロールを割り当てて、組織内のリソースへのアクセスを管理することができます。RBAC を実装するには、次の手順に従います。[official guide](https://docs.microsoft.com/en-us/azure/role-based-access-control/overview)をマイクロソフトから発売しました。

例ユーザーにロールを割り当てる
```azurecli
# ユーザーに Reader ロールを割り当てる
az role assignment create --assignee johndoe@example.com --role "Reader" --scope "/subscriptions/your_subscription_id/resourceGroups/your_resource_group"
```
#### 不審な活動の監視
Azure ADには、疑わしい活動を監視し対応するための**Identity Protection**や**Conditional Access**といった機能があります。Identity Protectionは、機械学習アルゴリズムを使用して異常や危険なサインインの試みを検出し、Conditional Accessは、デバイス、場所、リスクレベルなどの要素に基づいてアクセスを制御するポリシーを設定することができます。

Azure AD Identity Protectionをセットアップするには、次の手順に従います。[official guide](https://learn.microsoft.com/en-us/azure/active-directory/identity-protection/concept-identity-protection-b2b)をマイクロソフトから発売しました。

例条件付きアクセスポリシーの作成

```powershell
# Azure AD に接続
Connect-AzureAD

# 条件付きアクセス ポリシーを作成
$PolicyName = "BlockSignInFromUnknownLocations"
$PolicyDescription = "不明な場所からのユーザーのサインインをブロックします。"
$PolicyState = "Enabled"
$Conditions = @{
    "SignInRiskLevels" = @("medium","high");
    "Locations" = @{
        "Included" = @();
        "Excluded" = @("AllTrusted")
    }
}
$GrantControls = @{
    "Operator" = "OR";
    "BuiltInControls" = @("Block")
}
New-AzureADMSConditionalAccessPolicy -DisplayName $PolicyName -State $PolicyState -Conditions $Conditions -GrantControls $GrantControls -Description $PolicyDescription

```
詳細は公式ドキュメントの[Azure AD Identity Protection](https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/overview)と[Conditional Access](https://learn.microsoft.com/en-us/azure/active-directory/conditional-access/overview)をご覧ください。


### データセキュリティ

クラウド上のデータを保護することは非常に重要です。Azure Security Centerは、**Azure Information Protection**、**Azure Storage Service Encryption**、**Azure Disk Encryption**などの複数のデータセキュリティ機能を提供します。これらの機能は、データの暗号化とアクセス管理を支援し、機密情報の安全性を確保します。

#### Azure Information Protection

**Azure Information Protection (AIP) **は、機密文書や電子メールを分類、ラベル付け、保護するためのクラウドベースのソリューションです。AIPは、「Confidential」や「Personal」などの組み込みラベルのセットを提供し、組織のニーズに応じてカスタマイズすることができます。また、事前に定義されたルールに基づいて自動的にラベルを適用するようにAIPを設定することも可能です。AIPを使い始めるには、以下の手順に従ってください。[official guide](https://docs.microsoft.com/en-us/azure/information-protection/what-is-information-protection) Azure Information Protection は過去の製品名で、Sentinel の最新ドキュメントでは非推奨です。新規導入の前に Microsoft Purview Information Protection のドキュメントを確認してください。

例カスタムラベルを作成する

```powershell
# AIP サービスに接続
Connect-AipService

# 保護設定を含むカスタム ラベルを作成
$LabelName = "Sensitive - Internal Use Only"
$LabelDescription = "このラベルは、内部利用のみを対象とした暗号化とアクセス ポリシーを適用します。"
$LabelProtectionSettings = @{
    "ContentExpirationDate" = (Get-Date).AddMonths(6).ToUniversalTime();
    "OfflineAccessInterval" = "P7D";
    "UserRights" = @("domain\GroupA=View", "domain\GroupB=View,Edit,Print")
}
New-AipServiceLabel -Name $LabelName -Description $LabelDescription -ProtectionSettings $LabelProtectionSettings
```
#### Azure Storage Service Encryption
**Azure Storage Service Encryption (SSE**) は、Blob、File、Table、Queue ストレージを含む Azure Storage アカウントで、静止状態のデータを自動的に暗号化します。SSEは、Azureが管理する鍵または顧客が管理する鍵を使用して、ストレージアカウントレベルで暗号化を提供します。SSEを有効にするには、次の手順に従います。[step-by-step guide](https://docs.microsoft.com/en-us/azure/storage/common/storage-service-encryption)マイクロソフト社から提供されています。

例ストレージアカウントでSSEを有効化する

```azurecli
# Azure 管理キーを使用して SSE を有効にする
az storage account update --name mystorageaccount --resource-group myresourcegroup --encryption-services blob file
```
#### Azure Disk Encryption（アジュール ディスク エンクリプション
**Azure Disk Encryption** は、BitLocker (Windows) または dm-crypt (Linux) で仮想マシンディスクを暗号化することで、仮想マシンディスクを保護します。暗号化キーとシークレットは、Azure Key Vaultによって保護され、データが静止状態で保護されることを保証します。Azure Disk Encryptionを有効にするには、次の手順に従います。[official guide](https://learn.microsoft.com/en-us/azure/virtual-machines/disk-encryption-overview)をマイクロソフトから購入しました。

例仮想マシンのAzure Disk Encryptionの有効化
```azurecli
# Windows VM で Azure Disk Encryption を有効にする
az vm encryption enable --resource-group myResourceGroup --name myVM --disk-encryption-keyvault myKeyVault
```
公式ドキュメントで、[Azure Information Protection](https://docs.microsoft.com/en-us/azure/information-protection/what-is-information-protection)、[Azure Storage Service Encryption](https://docs.microsoft.com/en-us/azure/storage/common/storage-service-encryption)、[Azure Disk Encryption](https://learn.microsoft.com/en-us/azure/virtual-machines/disk-encryption-overview)の詳細を確認できます。
______

## 脅威の発見と対応

Azure Security Centerは、高度な脅威検知機能により、潜在的な脅威を特定し、警告を発します。Azure Sentinel**と統合することで、環境全体のセキュリティインシデントを監視、調査、対応することができます。

### 脅威の検出

Azure Security Centerは、高度な脅威検出機能のセットである**Azure Defender**を使用して、潜在的なセキュリティ脅威を特定します。Azure Defenderは、お客様のリソースを監視して侵害の指標を見つけ、潜在的な脅威に対応するためのアラートと推奨事項を提供します。Azure Defenderを有効にするには、次の手順に従います。[official guide](https://docs.microsoft.com/en-us/azure/security-center/defender-for-cloud-enable)

例サブスクリプションのAzure Defenderを有効化する

```azurecli
# サブスクリプションで Azure Defender を有効にする
az security auto-provisioning-setting update --name default --auto-provision on
```
### 脅威への対応
脅威が検出された場合、迅速かつ効果的に対応することが不可欠です。Azure Security Centerは、**Security Incident** 管理を提供し、セキュリティインシデントの調査や対応を支援します。また、**Azure Sentinel**と統合することで、自動化されたプレイブックを作成し、セキュリティインシデントへの対応をオーケストレーションすることができます。Azure Security CenterとAzure Sentinelの統合については、**公式ドキュメント**で詳しく説明しています。

例Azure Sentinel用のLogic Appプレイブックを作成する。
```azurecli
# リソース グループを作成する
az group create --name MyResourceGroup --location EastUS

# Logic App を作成する
az logic workflow create --resource-group MyResourceGroup --location EastUS --name MyPlaybook --definition @playbook-definition.json
```
のことです。`playbook-definition.json`ファイルには、Logic App のプレイブック定義が含まれている必要があります。Azure Sentinelのプレイブックの例は、以下のページで見ることができます。[Azure-Sentinel GitHub repository](https://github.com/Azure/Azure-Sentinel/tree/master/Playbooks)

Azure Security Centerの脅威検知機能を活用し、Azure Sentinelと統合することで、Azure環境における脅威を検知し対応するための強固なセキュリティ戦略を構築できます。詳細は公式ドキュメントの[Azure Defender](https://learn.microsoft.com/en-us/azure/defender-for-cloud/enable-enhanced-security)と[Azure Sentinel](https://docs.microsoft.com/en-us/azure/sentinel/overview)をご覧ください。
______

現在は[Defender for Cloud コネクタ](https://learn.microsoft.com/en-us/azure/sentinel/connect-defender-for-cloud)を使ってアラートを Microsoft Sentinel に送信します。自動化に依存する前に、コネクタ、データ収集ルール、分析ルール、インシデント対応手順を確認してください。

## モニタリングとレポーティング

モニタリングとレポーティングは、安全なクラウド環境を維持するために不可欠な要素です。Azure Security Centerは、**Security Dashboard**, **Security Alerts**, **Compliance Reports** など、監視と報告のためのいくつかのツールを提供します。

### セキュリティダッシュボード

Azure Security Center の Security Dashboard は、お客様のセキュリティ態勢を包括的に把握することができます。セキュアスコア、セキュリティ勧告、およびアクティブなセキュリティ警告が表示されます。また、ダッシュボードは、お客様のコンプライアンス状況についての洞察を提供し、時間の経過とともに進捗状況を追跡することができます。

### セキュリティアラート

Azure Security Centerは、潜在的な脅威が検出された場合にセキュリティアラートを生成します。これらのアラートでは、脅威に関する詳細な情報と、リスクを軽減するための推奨事項が提供されます。Azure Security Centerは、電子メール、SMS、または以下のようなサードパーティツールと統合して通知を送信するように構成することができます。[Slack](https://slack.com/) or [Microsoft Teams](https://www.microsoft.com/en-us/microsoft-teams/group-chat-software)

### コンプライアンス報告書

Azure Security Center では、GDPR、HIPAA、PCI DSS など、さまざまな規制の枠組みに対するコンプライアンスレポートを作成できます。これらのレポートは、組織のコンプライアンス状況を追跡し、改善が必要な領域を特定するのに役立ちます。

______

## Azure Security Centerの推奨される実践方法

Azure Security Centerを最大限に活用するために、以下の推奨される実践方法の実施をご検討ください：

1. **すべてのサブスクリプションで Azure Security Center を有効にする**：すべてのサブスクリプションでAzure Security Centerを有効にする**：すべてのAzureサブスクリプションがAzure Security Centerによって保護されていることを確認することは、安全なクラウド環境を維持するために重要です。
2.**Secure Scoreを定期的に確認する**：Secure Scoreをモニタリングすることで、全体的なセキュリティ状況を把握し、改善が必要な領域を特定することができます。
3.**セキュリティ勧告を実施する**：Azure Security Centerが提供するセキュリティ勧告に対処することで、セキュリティ態勢を改善し、潜在的なリスクを低減することができます。
4.**セキュリティ警告の監視**：潜在的な脅威を軽減し、安全な環境を維持するために、定期的にセキュリティアラートを確認し、対応する。
5.**コンプライアンス要件に対応する**：コンプライアンスポリシーを定期的に見直し、更新することで、組織が最新の規制枠組みに準拠していることを確認する。

______
## Defender for Cloud の現在のワークフロー

現在の環境を導入する際は、次の順序で進めます。以前のセクション名は過去の情報を検索する際に役立ちますが、ポータルとドキュメントでは Defender for Cloud の用語が使われています。

1. **サブスクリプションとコネクタを棚卸しする。** Azure サブスクリプション、AWS または GCP コネクタ、DevOps プロジェクト、重要なリソースを記録します。
2. **必要な Defender プランを有効にする。** ワークロードごとにプランを選び、本番サブスクリプションで有効にする前にライセンスを確認します。
3. **Cloud Secure Score と推奨事項を確認する。** インターネットへの公開、ID リスク、悪用可能な脆弱性、ログ不足を優先します。スコアは完全なコンプライアンスの証明ではありません。
4. **Microsoft Entra の制御を設定する。** 重要なアカウントにフィッシング耐性のある MFA を要求し、最小権限の RBAC を使い、特権アクセスを確認します。
5. **Microsoft Sentinel にアラートを送る。** アラートの取り込み、分析ルール、担当者、対応の自動化、保持期間を確認します。
6. **変更後に再確認する。** パッチ適用、アーキテクチャ変更、コネクタ追加、プラン変更後に推奨事項を確認します。

## 実務向けレビューのチェックリスト

- **ID:** 古いアカウントを削除し、常時の管理者アクセスを減らし、条件付きアクセスの除外を確認します。
- **ネットワーク:** 公開された管理ポートを削除し、NSG の送信元範囲を狭め、ファイアウォールと WAF のログが監視ワークスペースに届くことを確認します。
- **データ:** 機密データストアを分類し、暗号化とキーの所有者を確認して、バックアップからの復元をテストします。
- **検出:** アラートの重大度、通知経路、インシデント担当者、対応プレイブックを確認します。
- **ガバナンス:** 各ポリシー施策に担当者、例外の期限、必要なフレームワークの証跡を割り当てます。


## 参考文献
- [Azure Security Center Documentation](https://docs.microsoft.com/en-us/azure/security-center/)
- [Azure Policy Service](https://docs.microsoft.com/en-us/azure/governance/policy/)
- [NIST 800-53](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final)
- [CIS](https://www.cisecurity.org/)
- [ISO 27001](https://www.iso.org/isoiec-27001-information-security.html)
- [GDPR](https://gdpr.eu/)
- [HIPAA](https://www.hhs.gov/hipaa/index.html)
- [PCI DSS](https://www.pcisecuritystandards.org/)

