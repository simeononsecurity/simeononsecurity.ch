---
title: "Infrastructure as CodeのためのTerraformをはじめよう。"
date: 2023-05-04
toc: true
draft: false
description: "Infrastructure as Codeの代表的なツールであるTerraformの基本を学び、インフラを効率的に管理するための使い方を紹介します。"
tags: ["テラフォーム", "コードとしてのインフラ", "アイエーシー", "クラウドコンピューティング", "デブオプス", "オートメーション", "エーダブリュエス", "アズール", "グーグルクラウド", "クラウドプロバイダー", "コンフィギュレーションマネジメント", "デプロイメント", "プロビジョニング", "リソースマネジメント", "スケーラビリティ", "レジリエンス", "セキュリティ", "コンプライアンス", "ベストプラクティス"]
cover: "/img/cover/A_cartoon_computer_monitor_with_multiple_network-connected.png"
coverAlt: "Terraformでインフラを管理することを意味し、ネットワークに接続された複数の機器が積み木のように見える漫画のようなコンピューターモニター。"
coverCaption: ""
---

**Infrastructure as CodeアプリケーションのためのTeraForm入門**。

より多くの組織がインフラをクラウドに移行するにつれ、それを効果的に管理する必要性が最も高くなります。そこで登場するのがInfrastructure as Code (IaC)です。IaCとは、手作業ではなく、コードによってインフラを管理し、プロビジョニングするプロセスのことです。これにより、インフラストラクチャの管理における一貫性、スピード、信頼性を向上させることができます。IaCのための最も人気のあるツールの1つがTeraformです。

## Teraformとは？

**Teraform**はオープンソースのInfrastructure as Codeソフトウェアツールで、ユーザーがInfrastructure as Codeを記述、計画、作成することを可能にします。HashiCorpによって開発されたTeraformは、AWS、Azure、Google Cloud Platformを含む様々なクラウドプロバイダーでインフラを管理することができます。Teraformでは、ユーザーはインフラをコードとして設定ファイルに定義し、コードを適用してインフラを作成または更新し、不要になったらインフラを破棄することができます。

## Teraformを利用するメリット

Infrastructure as Codeの用途にTeraformを使用することで、以下のような利点があります：

- 効率とスピード:** Teraformは、手作業によるプロセスを排除することで、より速く、より効率的なインフラ管理を可能にします。

- インフラストラクチャの定義にコードを使用することで、Teraformは環境間の一貫性を確保します。

- スケーラビリティ:** Teraformは、増大する需要に対応するため、インフラストラクチャを容易に拡張することが可能です。

- コラボレーション： ** Teraformの設定ファイルはバージョン管理され、チームメンバー間で共有することができるため、コラボレーションを容易にすることができます。

- **Cost Savings:** Teraformはリソースのプロビジョニングとデプロビジョニングを簡単に行うことができるため、コスト削減が可能です。

## Teraformを使いこなすために

Teraformを使い始めるには、以下のものが必要です：

1.**Teraform のダウンロード： ** Teraform は、以下のサイトからダウンロードすることができます。[official website](https://www.terraform.io/downloads.html)

2.**Create a Configuration File:** Teraformは、HashiCorp Configuration Language（HCL）またはJSONで書かれた設定ファイルを使用します。設定ファイルには、作成・更新・削除したいインフラが定義されています。

Terraformを使用するには、目的のインフラストラクチャを定義するための設定ファイルを作成する必要があります。設定ファイルには、作成するリソース、そのプロパティ、依存関係が指定されています。

設定ファイルは、人間が読むことができ、習得しやすいように設計された言語であるHashiCorp Configuration Language（HCL）、またはJSONフォーマットで記述することができます。HCLの構文は他のプログラミング言語と同様で、ブロック、属性、値を使用します。

以下は、AWS EC2インスタンスを作成するHCL形式の基本的なTerraform設定ファイルの例です：

```HCL
provider "aws" {
  region = "us-west-2"
}

resource "aws_instance" "example" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
}
```
この例では、設定ファイルでawsプロバイダを指定し、Amazon Machine Image（AMI）とインスタンスタイプを持つaws_instanceリソースを作成しています。

また、より高度な例として、Terraformを使用してVMWareを使用したシステムを構成する次の例を参照してください：
```HCL
provider "vsphere" {
  user           = "user@domain.com"
  password       = "password"
  vsphere_server = "vcenter.example.com"
}

data "vsphere_datacenter" "dc" {
  name = "Datacenter"
}

data "vsphere_datastore" "ds" {
  name          = "Datastore"
  datacenter_id = data.vsphere_datacenter.dc.id
}

data "vsphere_network_interface" "nic" {
  label          = "Network adapter 1"
  datacenter_id  = data.vsphere_datacenter.dc.id
  network_id     = "VM Network"
}

resource "vsphere_virtual_machine" "vm" {
  name             = "terraform-vm"
  folder           = "/terraform"
  num_cpus         = 2
  memory           = 2048
  guest_id         = "otherLinux64Guest"
  scsi_type        = "pvscsi"
  datastore_id     = data.vsphere_datastore.ds.id

  network_interface {
    network_id = data.vsphere_network_interface.nic.network_id
  }

  disk {
    label            = "disk0"
    size             = 20
    eagerly_scrub    = true
    thin_provisioned = true
  }

  clone {
    template_uuid = "template-uuid"
  }
}

```

この例では、設定ファイルでvsphereプロバイダーを指定し、名前、フォルダ、CPU数、メモリ量、ゲストOS、SCSIタイプ、およびディスク設定を指定したvsphere_virtual_machineリソースを作成します。また、指定されたテンプレートから仮想マシンをクローン化します。

また、設定ファイルはデータブロックを使用して、仮想マシンリソースが使用するデータセンター、データストア、およびネットワークインターフェイスに関する情報をvSphereインフラストラクチャに問い合わせます。

構成ファイルを作成すると、それを使用してインフラストラクチャ・リソースを作成、更新、または削除することができます。

3.**Teraformの初期化:**設定ファイルを作成したら、Teraformを初期化するために`terraform init`コマンドを実行します。これにより、必要なプラグインやモジュールがダウンロードされます。

例えば、設定ファイルの名前が`main.tf`という名前のディレクトリに`terraform-example`で以下のコマンドを実行することで、Terraformを初期化することができます。`terraform-example`ディレクトリを作成します：```terraform init```

設定ファイルに指定された必要なプラグインやモジュールをダウンロードします。

1.**Plan and Apply Infrastructure:** 初期化した後、次のように実行します。`terraform plan`コマンドを使用して、インフラストラクチャにどのような変更が行われるかを確認し、変更を適用します。`terraform apply`コマンドを使用します。

初期化後、インフラストラクチャにどのような変更を加えるかを計画するために`terraform plan`コマンドを使用します。これにより、どのようなリソースが作成、更新、または削除されるかがわかります。たとえば、次のような名前の設定ファイルがあるとします。`main.tf`という名前のディレクトリに`terraform-example`は、以下のコマンドを実行することで、インフラの変更を計画することができます：

```terraform plan```

これにより、インフラに加えられる変更のプレビューが表示されます。

変更内容に満足したら、その変更を適用するために`terraform apply`コマンドを使用します。たとえば、次のような名前の設定ファイルがある場合、そのファイルは`main.tf`という名前のディレクトリに`terraform-example`は、以下のコマンドを実行することで、インフラストラクチャの変更を適用することができます：

```terraform apply```

これにより、お客様のインフラストラクチャに変更が適用されます。変更の適用には、インフラの規模や複雑さによって時間がかかる場合がありますので、ご注意ください。

## Teraformを使うためのベストプラクティス

Teraformを効果的に使用するために、以下のベストプラクティスに従うことを検討してください：

- バージョンコントロールの使用:** Teraformの設定ファイルをバージョンコントロールに保存し、コラボレーションを可能にし、変更点を確実に追跡します。

- モジュールを使用する:** Teraformのモジュールを使用して、コードを整理し再利用します。

- **Separate Configurations:** 環境ごとに設定を分ける (例: dev, staging, prod) ことで、一貫性を確保し、設定のドリフトを回避します。

- 変更を検証する:**インフラストラクチャに変更を適用する前に、(1) (2) (3) (4) (5) (6) (7)を使用して、変更を検証してください。`terraform plan`コマンドを使用します。

## 結論

Teraformは、より速く、より効率的で、一貫性のあるインフラストラクチャ管理を可能にする、強力なInfrastructure as Codeツールです。Teraformを利用することで、組織は時間とコストを削減し、さらにコラボレーションとスケーラビリティを改善することができます。ベストプラクティスに従ってTeraformを使い始めることで、これらの利点を活用し、より効果的にインフラを管理することができます。

---

**参考文献：**1

-[Teraform Official Website](https://www.terraform.io/)
-[Teraform Documentation](https://www.terraform.io/docs/index.html)
-[AWS Best Practices for Security, Identity, & Compliance](https://aws.amazon.com/architecture/security-identity-compliance/)
