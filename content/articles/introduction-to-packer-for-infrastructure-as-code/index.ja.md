---
title: "コードとしてのインフラ（IaC）にPackerを使う方法：ベストプラクティスと利点"
date: 2023-05-04
lastmod: 2026-11-16
toc: true
draft: false
description: "メンテナンスが容易で安全なマシンイメージを作成するためのPackerの使い方をご紹介します。"
tags: ["Packer", "コードとしてのインフラ", "開発と運用", "自動化", "セキュリティ", "再現性", "スケーラビリティ", "マルチプラットフォーム", "バージョン管理", "クラウドコンピューティング", "マシンイメージ", "仮想化", "構成管理", "継続的インテグレーション", "継続的デリバリー", "ソフトウェア開発", "ベストプラクティス", "テスト", "オープンソース", "マルチクラウド"]
cover: "/img/cover/A_cartoon-style_image_of_a_packer_creating_different_machines.webp"
coverAlt: "マルチプラットフォーム用に異なるマシンイメージを作成するパッカーが、ノートパソコンと雲を背景に漫画風に描かれたイメージ。"
coverCaption: ""
---

**コードとしてのインフラアプリケーションにおけるPacker入門**

**Packer**は、**マシンイメージ**や**仮想マシンテンプレート**を作成し、複数のプラットフォームに同一の環境を展開できる人気のツールです。**AWS、Google Cloud Platform、Azure、VMware**などのプラットフォーム向けにイメージを作成する工程を自動化します。Packerはオープンソースのツールで、Vagrant、Consul、Terraformなども開発したHashiCorpが作成しました。

この記事では、Packerを紹介し、さまざまなプラットフォーム用のマシンイメージを作成するためにPackerを使用する方法を紹介します。また、Packerを使用するメリットやベストプラクティスについても説明します。

## Packerとは？

Packerは、さまざまなプラットフォーム向けのマシンイメージを作成するプロセスを自動化するツールです。Vagrant、Consul、Terraformなどの有名なツールを開発したHashiCorpによって作られたオープンソースのツールです。

Packerを使用すると、開発者はAWS、Google Cloud Platform、Azure、VMwareなどの異なるプラットフォーム用のマシンイメージや仮想マシンテンプレートを作成できます。これらのマシンイメージは、複数のプラットフォームで同一の環境を展開するために使用することができます。

## Packerを使用するメリット

Packerを使用することで、以下のようなメリットがあります：

- **再現性**：Packerは毎回同じ方法でマシンイメージを作成し、環境間の一貫性を保ちます。
- **自動化**：マシンイメージの作成を自動化し、時間を節約して人的ミスを減らします。
- **マルチプラットフォーム対応**：異なる環境で使えるマシンイメージを作成しやすくします。
- **他のツールとの統合**：Ansible、Chef、Puppetと連携し、既存のツールでイメージを作成できます。
- **スケーラビリティ**：複数のイメージを並行して作成し、作成プロセスを拡張しやすくします。

## Packerをはじめよう

Packerを使い始めるには、Packerのダウンロードとインストールが必要です。Packerは、Windows、macOS、Linuxで利用可能です。

Packerは公式サイトからダウンロードすることができます：[https://www.packer.io/downloads](https://www.packer.io/downloads)

Packerをインストールしたら、さまざまなプラットフォーム用のマシンイメージの作成に取り掛かることができます。

## Packerでマシンイメージを作成する

Packerでマシンイメージを作成するには、イメージの構成を記述した**テンプレート**を定義します。テンプレートはJSON形式で記述され、マシンイメージの作成に必要な手順が指定されています。

以下は、AWSのマシンイメージを作成するためのPackerテンプレートの例です：

```json
{
"builders": [{
"type": "amazon-ebs",
"access_key": "ACCESS_KEY",
"secret_key": "SECRET_KEY",
"region": "us-west-2",
"source_ami": "ami-0c55b159cbfafe1f0",
"instance_type": "t2.micro",
"ssh_username": "ubuntu",
"ami_name": "my-image-{{timestamp}}"
}]
}
```

この例では、PackerがUbuntu AMIを使用してAmazon EBSにバックアップされたマシンイメージを作成するようテンプレートに指定します。作成されたマシンイメージは、末尾にタイムスタンプが付加された「my-image」という名前で提供されます。

Packerテンプレートを定義したら、`packer build`コマンドを使用してマシンイメージを作成することができます：

```bash
$ packer build template.json
```

### AnsibleプロビジョナーでAWS AMIを作る
AnsibleのプロビジョナーをPackerと一緒に使うことで、AWSのマシンイメージを作成することができます。以下はPackerテンプレートの例です：

```json
{
  "builders": [{
    "type": "amazon-ebs",
    "access_key": "ACCESS_KEY",
    "secret_key": "SECRET_KEY",
    "region": "us-west-2",
    "source_ami": "ami-0c55b159cbfafe1f0",
    "instance_type": "t2.micro",
    "ssh_username": "ubuntu",
    "ami_name": "my-image-{{timestamp}}"
  }],
  "provisioners": [{
    "type": "ansible",
    "playbook_file": "playbook.yml"
  }]
}
```
この例では、PackerテンプレートがAWSマシンイメージを作成し、Ansibleを使用してプロビジョニングします。テンプレートの`provisioners`セクションは、使用するAnsible playbookを指定します。

### Google Cloud Platformイメージ
Packerを使用して、Google Cloud Platform上のマシンイメージを作成することもできます。以下は、Packerテンプレートの例です：
```json
{
  "builders": [{
    "type": "googlecompute",
    "project_id": "PROJECT_ID",
    "source_image_family": "ubuntu-1604-lts",
    "zone": "us-central1-f",
    "image_name": "my-image",
    "image_description": "カスタムイメージ"
  }],
  "provisioners": [{
    "type": "shell",
    "inline": [
      "echo 'Hello, World!' > /tmp/hello.txt"
    ]
  }]
}
```

このPackerテンプレートは、Google Cloud Platformイメージを作成し、シェルプロビジョナーを使ってイメージにファイルを追加します。出来上がったマシンイメージは「my-image」という名前になり、「カスタムイメージ」という説明文が付きます。

### VMWare

```json
{
  "builders": [
    {
      "type": "vmware-iso",
      "iso_url": "https://releases.ubuntu.com/20.04.2/ubuntu-20.04.2-live-server-amd64.iso",
      "iso_checksum_type": "sha256",
      "iso_checksum": "a244fe4adcc2ad92d15c12e47ca4ea97fb5b5d67b1ba50880c9e420ae3f3c083",
      "guest_os_type": "ubuntu-64",
      "disk_size": 40960,
      "vm_name": "ubuntu-20.04.2-server-amd64",
      "ssh_username": "ubuntu",
      "ssh_password": "ubuntu",
      "ssh_port": 22,
      "ssh_wait_timeout": "60m",
      "shutdown_command": "sudo shutdown -P now",
      "vmx_data": {
        "memsize": "4096",
        "numvcpus": "2"
      }
    }
  ],
  "provisioners": [
    {
      "type": "shell",
      "inline": [
        "sudo apt-get update",
        "sudo apt-get install -y nginx"
      ]
    }
  ]
}
```

この例では、UbuntuサーバのISOを使用してVMwareマシンイメージを作成するように指定されています。作成されるマシンイメージは、4GBのRAM、2つのCPU、および40GBのディスクスペースを備えています。また、プロビジョニング中にnginxウェブサーバーがインストールされます。

これらは、Packerでできることのほんの一例に過ぎません。Packerを使えば、さまざまなプラットフォーム用のマシンイメージを作成し、さまざまなプロビジョナを使用してそれらを構成することができます。

## Packerを使用するためのベストプラクティス

Packerを使用するためのベストプラクティスをいくつか紹介します：

- **バージョン管理を使う**：変更を追跡して共同作業できるよう、Packerのテンプレートをバージョン管理に保存します。
- **テンプレートをパラメーター化する**：変数を使い、テンプレートの再利用と保守を容易にします。
- **テンプレートをテストする**：期待したマシンイメージが作成されることを確認します。
- **セキュリティのベストプラクティスに従う**：マシンイメージを作成するときは、生成される環境を保護します。
- **テンプレートをシンプルに保つ**：保守やデバッグが難しい複雑なテンプレートを避けます。
- **`packer init`コマンドを使う**：必要な構成で新しいテンプレートを初期化します。

## まとめ

Packerは、さまざまなプラットフォーム用のマシンイメージを作成するための強力なツールです。Packerは、再現性、自動化、マルチプラットフォームのサポート、およびスケーラビリティを提供します。ベストプラクティスに従うことで、Packerを使用して、保守が容易で安全なマシンイメージを作成することができます。

この記事では、Packerを紹介し、さまざまなプラットフォーム用のマシンイメージを作成するためのPackerの使用方法を紹介しました。また、Packerを使用するメリットと、Packerを使用するためのベストプラクティスについても説明しました。

Packerについてもっと知りたいという方は、以下の公式ドキュメントをご覧ください。[https://www.packer.io/docs](https://www.packer.io/docs)

