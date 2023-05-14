---
title: "Azureセキュリティセンター：クラウド環境の安全性を確保する"
date: 2023-04-10
toc: true
draft: false
description: "Azure Security Centerを使用してクラウド環境を保護する方法を、ベストプラクティスと実例を交えてご紹介します。"
tags: ["アズール", "セキュリティセンター", "クラウドセキュリティ", "アズールセンチネル", "アズールディフェンダー", "ネットワークセキュリティ", "アイデンティティ管理", "データ機密保護", "脅威検出", "脅威応答", "エムエフエー", "アールビーエーシー", "ニューサウスウェールズ", "アジュールファイアウォール", "ウォーファーフ", "Azure AD", "Azure情報保護", "Azure Storage Serviceの暗号化", "Azure Disk Encryption（アジュール ディスク エンクリプション"]
cover: "/img/cover/A_shield_icon_surrounded_by_cloud_symbols.png"
coverAlt: "安全なクラウド環境を表す、雲のシンボルに囲まれた盾のアイコンに、Azure Security Centerのロゴが描かれています。"
coverCaption: ""
---

**Azure Security Centerによるクラウド環境のセキュリティ確保方法**」。

クラウド環境のセキュリティ確保は、組織のデータ、アプリケーション、インフラを脅威から保護するために不可欠です。マイクロソフトの**Azure Security Center**は、セキュリティ態勢を強化し、Azure環境における潜在的なリスクを迅速に特定するのに役立つ強力なツールです。この記事では、Azure Security Centerを使用してクラウド環境を保護する方法について説明し、さまざまなセキュリティ機能を実装するためのベストプラクティスを取り上げます。さらに、この記事では、Azure Security Centerを使用してクラウド環境を保護する方法をよりよく理解するために、より技術的な詳細と例に飛び込んでいきます。

______

## Azure Security Centerを理解する

Azure Security Centerは、クラウド環境における潜在的な脆弱性の特定と対処を支援する**統合型インフラストラクチャ セキュリティ管理システム**です。脅威の検出、セキュリティ姿勢の管理、コンプライアンス管理など、いくつかの機能を提供し、Azure環境が常に安全であることを保証します。

**継続的なセキュリティ評価**と**高度な脅威保護**は、Azure Security Centerの2つの主要機能です。継続的なセキュリティアセスメントは、環境内の潜在的なセキュリティ問題の特定を支援し、高度な脅威保護は、潜在的な脅威の検出と対応を支援します。

______

## セキュリティポリシーとコンプライアンス標準の実装

Azure Security Center では、クラウド環境全体でセキュリティポリシーを実装し管理することができます。Azure Policy** サービスを使用してカスタムセキュリティポリシーを作成したり、組み込みポリシーを使用してベストプラクティスやコンプライアンス標準を適用したりできます。また、以下のような業界標準に照らして、セキュリティ姿勢を評価することができます。[NIST 800-53](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final), [CIS](https://www.cisecurity.org/), and [ISO 27001](https://www.iso.org/isoiec-27001-information-security.html)

Azure Security Centerは、コンプライアンス管理機能も備えており、以下のようなさまざまな規制の枠組みに対する組織のコンプライアンス状況を把握することができます。[GDPR](https://gdpr.eu/), [HIPAA](https://www.hhs.gov/hipaa/index.html), and [PCI DSS](https://www.pcisecuritystandards.org/)

______

## Azureリソースの安全確保

**リソースセキュリティ衛生**は、クラウド環境を保護するための重要な側面です。Azure Security Centerは、お客様のセキュリティ態勢の測定である**Secure Score**を提供し、お客様のリソースの全体的なセキュリティを理解するのに役立ちます。Azure Security Centerが提供する推奨事項に対処することで、Secure Scoreを向上させることができます。

### ネットワークセキュリティ

ネットワークセキュリティグループ（NSG）**、**Azure Firewall**、*Web Application Firewall（WAF）**などの適切なネットワークセキュリティ対策を実施することは、潜在的な脅威からAzure環境を保護するために非常に重要です。これらのツールは、入出力のネットワークトラフィックを制御し、不正アクセスや潜在的な攻撃からリソースを保護するのに役立ちます。

#### ネットワークセキュリティグループ(NSG)

NSG は、Azure リソースの仮想ファイアウォールとして機能し、リソースへのネットワークトラフィッ クを許可または拒否するルールを定義することができます。たとえば、特定のトラフィックを許可または拒否するルールを持つ NSG を作成することができます：

```azurecli
# Create a Network Security Group
az network nsg create --name MyNSG --resource-group MyResourceGroup

# Add rules to allow or deny traffic
az network nsg rule create --name MyNSGRule --nsg-name MyNSG --priority 100 --resource-group MyResourceGroup --access Allow --protocol Tcp --direction Inbound --source-address-prefixes '*' --source-port-ranges '*' --destination-address-prefixes '*' --destination-port-ranges '80'
```
について詳しくはこちら[Network Security Groups](https://docs.microsoft.com/en-us/azure/virtual-network/security-overview)を公式ドキュメントに掲載しています。

#### Azure Firewall（アジュールファイアウォール
Azure Firewallは、Azureリソースを保護する、マネージド型のクラウドベースのネットワークセキュリティサービスです。脅威インテリジェンスベースのフィルタリング、ウェブカテゴリ、集中型ロギングと分析などの高度な機能を提供します。Azure Firewall をセットアップするには、以下の手順に従います。[quickstart instructions](https://learn.microsoft.com/en-us/azure/firewall-manager/quick-firewall-policy-bicep)

#### ウェブアプリケーションファイアウォール(WAF)
Web Application Firewall (WAF) は、**Azure Application Gateway** の機能で、SQL インジェクション、クロスサイトスクリプティングなどの一般的な Web 悪用やその他の脅威から Web アプリケーションを保護するものです。WAFは、既存のWebアプリケーションと簡単に統合でき、特定の攻撃パターンから保護するためのカスタムルールを設定することができます。

以下は、WAFを有効にしたアプリケーションゲートウェイを作成する方法の例です：
```azurecli
# Create a WAF policy
az network application-gateway waf-policy create --name MyWafPolicy --resource-group MyResourceGroup --location EastUS

# Create a virtual network and subnet
az network vnet create --name MyVNet --resource-group MyResourceGroup --location EastUS --address-prefix 10.0.0.0/16
az network vnet subnet create --name MySubnet --resource-group MyResourceGroup --vnet-name MyVNet --address-prefix 10.0.0.0/24

# Create a public IP address
az network public-ip create --name MyPublicIP --resource-group MyResourceGroup --location EastUS --sku Standard

# Create an Application Gateway with WAF enabled
az network application-gateway create --name MyAppGateway --resource-group MyResourceGroup --location EastUS --vnet-name MyVNet --subnet MySubnet --public-ip-address MyPublicIP --http-settings-cookie-based-affinity Enabled --sku WAF_v2 --waf-policy MyWafPolicy

```
について詳しくはこちら[Web Application Firewall](https://docs.microsoft.com/en-us/azure/web-application-firewall/ag/ag-overview)を公式ドキュメントに掲載しています。

### Identity and Access Management（アイデンティティとアクセス管理

**Azure Active Directory (Azure AD)**は、クラウド環境のセキュリティを確保するために不可欠なコンポーネントです。Azure Security Centerでは、**多要素認証（MFA）**の有効化、**役割ベースのアクセス制御（RBAC）**の実装、疑わしいアクティビティの監視など、IDおよびアクセス管理の改善に向けた推奨事項を提供しています。

#### 多要素認証(MFA)

MFA は、アクセスを許可する前にユーザーに 2 つ以上の検証形式を要求することで、Azure AD アカウントに追加のセキュリティ層を追加します。以下の手順に従って、組織の MFA を有効にすることができます。[step-by-step guide](https://docs.microsoft.com/en-us/azure/active-directory/authentication/tutorial-enable-azure-mfa)マイクロソフト社から提供されています。

例あるユーザーに対してMFAを有効にする

```powershell
# Connect to Azure AD
Connect-AzureAD

# Enable MFA for a specific user
$UserPrincipalName = "johndoe@example.com"
$StsUserObjectID = (Get-AzureADUser -Filter "UserPrincipalName eq '$UserPrincipalName'").ObjectId
$StrongAuthRequirements = @(@{"Location"=""; "SatisfactionFactor"="2"; "VerificationMethod"="1"};@{"Location"=""; "SatisfactionFactor"="2"; "VerificationMethod"="2"})
Set-AzureADUser -ObjectId $StsUserObjectID -StrongAuthenticationRequirements $StrongAuthRequirements
```
#### ロールベースアクセスコントロール(RBAC)
RBAC を使用すると、Azure リソースの詳細なアクセス許可を定義し、ユーザーが適切なレベルのアクセス権を持つことを保証できます。ユーザー、グループ、またはアプリケーションにロールを割り当てて、組織内のリソースへのアクセスを管理することができます。RBAC を実装するには、次の手順に従います。[official guide](https://docs.microsoft.com/en-us/azure/role-based-access-control/overview)をマイクロソフトから発売しました。

例ユーザーにロールを割り当てる
```azurecli
# Assign a Reader role to a user
az role assignment create --assignee johndoe@example.com --role "Reader" --scope "/subscriptions/your_subscription_id/resourceGroups/your_resource_group"
```
#### 不審な活動の監視
Azure ADには、疑わしい活動を監視し対応するための**Identity Protection**や**Conditional Access**といった機能があります。Identity Protectionは、機械学習アルゴリズムを使用して異常や危険なサインインの試みを検出し、Conditional Accessは、デバイス、場所、リスクレベルなどの要素に基づいてアクセスを制御するポリシーを設定することができます。

Azure AD Identity Protectionをセットアップするには、次の手順に従います。[official guide](https://learn.microsoft.com/en-us/azure/active-directory/identity-protection/concept-identity-protection-b2b)をマイクロソフトから発売しました。

例条件付きアクセスポリシーの作成

```powershell
# Connect to Azure AD
Connect-AzureAD

# Create a Conditional Access policy
$PolicyName = "BlockSignInFromUnknownLocations"
$PolicyDescription = "Block sign-ins for users from unknown locations."
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
について詳しくはこちら[Azure AD Identity Protection](https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/overview) and [Conditional Access](https://learn.microsoft.com/en-us/azure/active-directory/conditional-access/overview)を公式ドキュメントに掲載しています。


### データセキュリティ

クラウド上のデータを保護することは非常に重要です。Azure Security Centerは、**Azure Information Protection**、**Azure Storage Service Encryption**、**Azure Disk Encryption**などの複数のデータセキュリティ機能を提供します。これらの機能は、データの暗号化とアクセス管理を支援し、機密情報の安全性を確保します。

#### Azure Information Protection

**Azure Information Protection (AIP) **は、機密文書や電子メールを分類、ラベル付け、保護するためのクラウドベースのソリューションです。AIPは、「Confidential」や「Personal」などの組み込みラベルのセットを提供し、組織のニーズに応じてカスタマイズすることができます。また、事前に定義されたルールに基づいて自動的にラベルを適用するようにAIPを設定することも可能です。AIPを使い始めるには、以下の手順に従ってください。[official guide](https://docs.microsoft.com/en-us/azure/information-protection/what-is-information-protection)

例カスタムラベルを作成する

```powershell
# Connect to the AIP service
Connect-AipService

# Create a custom label with protection settings
$LabelName = "Sensitive - Internal Use Only"
$LabelDescription = "This label applies encryption and an access policy for internal use only."
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
# Enable SSE using Azure-managed keys
az storage account update --name mystorageaccount --resource-group myresourcegroup --encryption-services blob file
```
#### Azure Disk Encryption（アジュール ディスク エンクリプション
**Azure Disk Encryption** は、BitLocker (Windows) または dm-crypt (Linux) で仮想マシンディスクを暗号化することで、仮想マシンディスクを保護します。暗号化キーとシークレットは、Azure Key Vaultによって保護され、データが静止状態で保護されることを保証します。Azure Disk Encryptionを有効にするには、次の手順に従います。[official guide](https://learn.microsoft.com/en-us/azure/virtual-machines/disk-encryption-overview)をマイクロソフトから購入しました。

例仮想マシンのAzure Disk Encryptionの有効化
```azurecli
# Enable Azure Disk Encryption for a Windows VM
az vm encryption enable --resource-group myResourceGroup --name myVM --disk-encryption-keyvault myKeyVault
```
について詳しくはこちら[Azure Information Protection](https://docs.microsoft.com/en-us/azure/information-protection/what-is-information-protection), [Azure Storage Service Encryption](https://docs.microsoft.com/en-us/azure/storage/common/storage-service-encryption), and [Azure Disk Encryption](https://learn.microsoft.com/en-us/azure/virtual-machines/disk-encryption-overview)を公式文書に記載します。
______

## 脅威の発見と対応

Azure Security Centerは、高度な脅威検知機能により、潜在的な脅威を特定し、警告を発します。Azure Sentinel**と統合することで、環境全体のセキュリティインシデントを監視、調査、対応することができます。

### 脅威の検出

Azure Security Centerは、高度な脅威検出機能のセットである**Azure Defender**を使用して、潜在的なセキュリティ脅威を特定します。Azure Defenderは、お客様のリソースを監視して侵害の指標を見つけ、潜在的な脅威に対応するためのアラートと推奨事項を提供します。Azure Defenderを有効にするには、次の手順に従います。[official guide](https://docs.microsoft.com/en-us/azure/security-center/defender-for-cloud-enable)

例サブスクリプションのAzure Defenderを有効化する

```azurecli
# Enable Azure Defender for a subscription
az security auto-provisioning-setting update --name default --auto-provision on
```
### 脅威への対応
脅威が検出された場合、迅速かつ効果的に対応することが不可欠です。Azure Security Centerは、**Security Incident** 管理を提供し、セキュリティインシデントの調査や対応を支援します。また、**Azure Sentinel**と統合することで、自動化されたプレイブックを作成し、セキュリティインシデントへの対応をオーケストレーションすることができます。Azure Security CenterとAzure Sentinelの統合については、**公式ドキュメント**で詳しく説明しています。

例Azure Sentinel用のLogic Appプレイブックを作成する。
```azurecli
# Create a resource group
az group create --name MyResourceGroup --location EastUS

# Create a Logic App
az logic workflow create --resource-group MyResourceGroup --location EastUS --name MyPlaybook --definition @playbook-definition.json
```
のことです。`playbook-definition.json`ファイルには、Logic App のプレイブック定義が含まれている必要があります。Azure Sentinelのプレイブックの例は、以下のページで見ることができます。[Azure-Sentinel GitHub repository](https://github.com/Azure/Azure-Sentinel/tree/master/Playbooks)

Azure Security Centerの脅威検知機能を活用し、Azure Sentinelと統合することで、Azure環境における脅威を検知し対応するための強固なセキュリティ戦略を構築することができます。の詳細については、こちらをご覧ください。[Azure Defender](https://learn.microsoft.com/en-us/azure/defender-for-cloud/enable-enhanced-security) and [Azure Sentinel](https://docs.microsoft.com/en-us/azure/sentinel/overview)を公式文書に記載します。
______

## モニタリングとレポーティング

モニタリングとレポーティングは、安全なクラウド環境を維持するために不可欠な要素です。Azure Security Centerは、**Security Dashboard**, **Security Alerts**, **Compliance Reports** など、監視と報告のためのいくつかのツールを提供します。

### セキュリティダッシュボード

Azure Security Center の Security Dashboard は、お客様のセキュリティ態勢を包括的に把握することができます。セキュアスコア、セキュリティ勧告、およびアクティブなセキュリティ警告が表示されます。また、ダッシュボードは、お客様のコンプライアンス状況についての洞察を提供し、時間の経過とともに進捗状況を追跡することができます。

### セキュリティアラート

Azure Security Centerは、潜在的な脅威が検出された場合にセキュリティアラートを生成します。これらのアラートでは、脅威に関する詳細な情報と、リスクを軽減するための推奨事項が提供されます。Azure Security Centerは、電子メール、SMS、または以下のようなサードパーティツールと統合して通知を送信するように構成することができます。[Slack](https://slack.com/) or [Microsoft Teams](https://www.microsoft.com/en-us/microsoft-teams/group-chat-software)

### コンプライアンス報告書

Azure Security Center では、GDPR、HIPAA、PCI DSS など、さまざまな規制の枠組みに対するコンプライアンスレポートを作成できます。これらのレポートは、組織のコンプライアンス状況を追跡し、改善が必要な領域を特定するのに役立ちます。

______

## Azure Security Centerのベストプラクティス

Azure Security Centerを最大限に活用するために、以下のベストプラクティスの実施をご検討ください：

1.1. **すべてのサブスクリプションで Azure Security Center を有効にする**：すべてのサブスクリプションでAzure Security Centerを有効にする**：すべてのAzureサブスクリプションがAzure Security Centerによって保護されていることを確認することは、安全なクラウド環境を維持するために重要です。
2.**Secure Scoreを定期的に確認する**：Secure Scoreをモニタリングすることで、全体的なセキュリティ状況を把握し、改善が必要な領域を特定することができます。
3.**セキュリティ勧告を実施する**：Azure Security Centerが提供するセキュリティ勧告に対処することで、セキュリティ態勢を改善し、潜在的なリスクを低減することができます。
4.**セキュリティ警告の監視**：潜在的な脅威を軽減し、安全な環境を維持するために、定期的にセキュリティアラートを確認し、対応する。
5.**コンプライアンス要件に対応する**：コンプライアンスポリシーを定期的に見直し、更新することで、組織が最新の規制枠組みに準拠していることを確認する。

______

## 参考文献

-[Azure Security Center Documentation](https://docs.microsoft.com/en-us/azure/security-center/)
-[Azure Policy Service](https://docs.microsoft.com/en-us/azure/governance/policy/)
-[NIST 800-53](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final)
-[CIS](https://www.cisecurity.org/)
-[ISO 27001](https://www.iso.org/isoiec-27001-information-security.html)
-[GDPR](https://gdpr.eu/)
-[HIPAA](https://www.hhs.gov/hipaa/index.html)
-[PCI DSS](https://www.pcisecuritystandards.org/)

