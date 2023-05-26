---
title: "Ansible入門：ITインフラ管理の自動化"
draft: false
toc: true
date: 2023-02-25
description: "宣言型言語によりITインフラ管理を簡素化するオープンソースの自動化ツール、Ansibleの基本を学ぶ。"
tags: ["Ansible入門", "ITインフラ管理の自動化", "Ansibleの基礎知識", "ITインフラの自動化", "コンフィギュレーション管理", "アプリケーションの展開", "プロビジョニング", "継続的デリバリー", "セキュリティコンプライアンス", "オーケストレーション", "ヤムル", "Ansibleモジュール", "役割分担", "ベストプラクティス", "バージョン管理", "テスト", "レッドハット", "システム管理者", "リナックス", "マックオス", "ウィンドウズ", "Ansibleのインストール", "Ansibleのインベントリ", "Ansible playbooks（アンシブル・プレイブック", "Ansibleモジュール", "Ansibleの役割", "Ansibleのベストプラクティス", "Ansibleのテスト", "ITインフラ自動化ツール", "Ansibleチュートリアル", "インフラ管理の自動化"]
cover: "/img/cover/A_cartoon_character_sitting_at_a_desk_surrounded_by_servers.png"
coverAlt: "サーバーやケーブルに囲まれたデスクに座り、パソコンの画面にはAnsibleのロゴが表示され、タスクが自動化されると微笑む漫画のキャラクターが登場します。"
coverCaption: ""
---

Ansibleは、システム管理者がITインフラ管理を自動化できるようにするオープンソースの自動化ツールです。インフラストラクチャの望ましい状態を記述するためのシンプルな言語を提供し、その状態を自動的に実行します。これにより、大規模で複雑なシステムを管理するために必要な時間と労力を削減することができます。

この記事では、Ansibleを初めて使う方のために、基本的なコンセプトや使い始め方など、ツールの紹介をします。

## Ansible入門

Ansibleは2012年にMichael DeHaanによって開発され、2015年にRed Hatによって買収されました。それ以来、業界で最も人気のある自動化ツールの 1 つとなっています。

Ansibleは、YAML（「YAML Ain't Markup Language」の略）と呼ばれるシンプルな宣言型言語を使用して、インフラストラクチャの望ましい状態を定義します。そのため、ノンプログラマーでも読みやすく、理解しやすい。

Ansibleは、以下のような幅広いタスクの自動化に利用することができます：

- コンフィギュレーション管理
- **アプリケーションのデプロイメント**。
- **継続的なデリバリー**。
- ** プロビジョニング**
- ** セキュリティコンプライアンス**
- **オーケストレーション

## Ansibleをはじめよう

Ansibleを使い始めるには、お使いのシステムにインストールする必要があります。Ansibleは、Linux、macOS、Windowsなど、さまざまなOSにインストールすることができます。

Linux、この場合はUbuntuにAnsibleをインストールするには、以下のコマンドを使用します：
```bash
sudo apt-get update
sudo apt-get install ansible -y
```
それ以外の場合は、以下のガイドを参考にして、ansibleをインストールしてください：
- [Installing Ansible](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html)
- [Installation Guide](https://docs.ansible.com/ansible/latest/installation_guide/index.html)

Ansibleのインストールが完了したら、以下のコマンドを実行することで動作確認ができます：
```bash
ansible --version
```

これにより、インストールされているAnsibleのバージョンが表示されるはずです。

## Ansibleインベントリ

Ansibleを使用するための最初のステップは、インベントリを定義することです。インベントリとは、Ansibleが管理するサーバーのリストです。インベントリは、INI、YAML、JSONなど様々なフォーマットで定義することができます。

以下は、INI形式のインベントリファイルの例です：

```ini
[webservers]
webserver1.example.com
webserver2.example.com

[databases]
dbserver1.example.com
dbserver2.example.com
```

このインベントリファイルは、「ウェブサーバー」と「データベース」という2つのサーバーグループを定義し、各グループに属するサーバーのホスト名をリストアップしています。

## Ansible Playbooks

インベントリを定義したら、次のステップはプレイブックを定義することです。Playbookとは、インベントリ内のサーバーに対してAnsibleが実行すべき一連のタスクを記述したYAMLファイルです。

以下は、シンプルなplaybookの例です：
```yml
name: Install Nginx
hosts: webservers
become: yes

tasks:
    - name: Install Nginx package
        apt:
        name: nginx
        state: present
```

このプレイブックは、「webservers」グループに属するすべてのサーバーにNginx Webサーバーをインストールします。

このプレイブックでは `hosts`パラメータは、playbookを実行するサーバーのグループを指定します。を指定します。 `become`パラメータは、タスクが昇格した権限で実行されることを指定します（「昇格した権限で実行する」を使用）。 `sudo`または `su`

のことです。 `tasks`セクションには、playbookが実行すべき個々のタスクがリストアップされています。この場合、タスクは1つだけで、Nginxパッケージを `apt`モジュールになります。

## Ansibleモジュール

Ansibleモジュールは、特定のタスクを実行するために使用できる、再利用可能なコードのユニットです。Ansibleには幅広いビルトインモジュールが付属しており、また多くのサードパーティーモジュールも用意されています。

ここでは、ビルトインモジュールの例をいくつか紹介します：

- `apt`- Debianベースのシステムでパッケージを管理する
- `yum`- Red Hatベースのシステムでパッケージを管理する
- `file`- ファイル管理
- `service`- システムサービスを管理する
- `user`- ユーザーとグループの管理
- `copy`- コントロールマシンから管理対象サーバーへのファイルコピー

ビルトインモジュールの完全な一覧は [Ansible documentation](https://docs.ansible.com/ansible/latest/modules/modules_by_category.html)

## Ansibleの役割とフォルダー構造

Ansibleのロールは、共通のタスクや設定を整理して再利用するための方法です。タスク、ハンドラ、テンプレート、ファイル、およびその他のリソースを含むディレクトリ構造です。

ここでは、Nginxをインストールし設定するためのシンプルなAnsibleロールの例を示します：
```
roles/
└── nginx/
    ├── tasks/
    │   ├── main.yml
    ├── handlers/
    │   ├── main.yml
    ├── templates/
    │   ├── nginx.conf.j2
    ├── files/
    ├── vars/
    ├── defaults/
    ├── meta/
```
この例では、nginxの役割は、いくつかのサブディレクトリを含むディレクトリであり、各サブディレクトリは特定の目的を果たす：

- タスク**：ロールによって実行されるタスクが含まれています。
- タスク**：役割によって実行されるタスクが含まれます。
- **templates**: Nginxの設定ファイルを生成するために使用されるJinja2テンプレートが含まれています。
- **files**: ロールによって必要とされる静的ファイルが含まれます。
- **vars**: ロールに固有の変数が含まれます。
- defaults**：役割のデフォルト変数が含まれています。
- meta**：依存関係などの役割に関するメタデータが含まれます。

ロールは、複数のプレイブックやプロジェクトで簡単に共有・再利用することができます。

以下は、tasksディレクトリにあるmain.ymlファイルの例です：
```yaml
---
- name: Install Nginx
  apt:
    name: nginx
    state: present
  notify: restart nginx

- name: Enable Nginx
  systemd:
    name: nginx
    enabled: yes
    state: started
```

このタスクは、aptモジュールを使ってNginxをインストールし、systemdモジュールを使ってNginxサービスを有効化して起動します。また、restart nginx handlerに通知し、設定に変更があった場合はNginxを再起動します。

このようなAnsibleロールを使用することで、複数のサーバーや環境にまたがるソフトウェアの管理・設定プロセスを簡略化することができます。タスク、ハンドラ、テンプレート、その他のリソースを1つのディレクトリ構造に分離することで、異なるプレイブックやプロジェクト間でこれらのコンポーネントをより簡単に管理、再利用することができます。

## Ansibleのベストプラクティス

Ansibleを使用する際に従うべきベストプラクティスをいくつか紹介します：

### 1.バージョン管理の使用

Ansible の playbook とロールを Git のようなバージョン管理システムに保存することは、変更を追跡して他の人とコラボレーションするのに役立つベストプラクティスと言えます。バージョン管理は、コードベースに加えられた変更の履歴を提供し、必要に応じて以前のバージョンにロールバックすることを可能にします。また、コードの共有やコンフリクトの管理など、他者とのコラボレーションも容易になります。

### 2.ロールを使ってプレイブックを整理する

ロールは、Ansible の playbook とタスクを整理するための強力な方法です。関連するタスクをロールにまとめることで、Playbookをよりモジュール化し、再利用可能にすることができます。また、ロールによって、異なるプロジェクト間でコードを簡単に共有することができます。

ここでは、ロールを使用してNginxをインストールおよび構成するプレイブックの例を示します：

```yml
name: Install and configure Nginx
hosts: webservers
become: yes
roles:
  - nginx
```

このプレイブックでは、「nginx」というロールを使用して、ホストの「webservers」グループにNginxをインストールし、設定します。

### 3.タグを使用してタスクをグループ化する

Ansible playbook では、タグを使用して関連するタスクをグループ化することができます。これにより、特に大規模で複雑なプレイブックを扱う場合に、プレイブックの特定の部分を実行することが容易になります。

以下は、Ansibleのプレイブックでタグを使用する方法の一例です：
```yml
name: Install and configure Nginx
hosts: webservers
become: yes
tasks:
  - name: Install Nginx
    apt:
    name: nginx
    state: present
    tags: nginx_install

  - name: Configure Nginx
    template:
    src: nginx.conf.j2
    dest: /etc/nginx/nginx.conf
    tags: nginx_config
```

このPlaybookには、NginxをインストールするタスクとNginxを設定するタスクの2つがあります。各タスクにはタグが関連付けられており、必要なタスクだけを簡単に実行することができます。

### 4.プレイブックをより柔軟にするために変数を使用する

変数を使用することで、Ansible のプレイブックをより柔軟で再利用しやすいものにすることができます。変数を使用することで、プレイブックをより汎用的にし、異なる環境に適応させることができます。

ここでは、Ansibleのプレイブックで変数を使用する方法を例として説明します：
```yml
name: Install and configure Nginx
hosts: webservers
become: yes

vars:
nginx_port: 80
nginx_user: www-data

tasks:
  - name: Install Nginx
    apt:
    name: nginx
    state: present
  - name: Configure Nginx
    template:
    src: nginx.conf.j2
    dest: /etc/nginx/nginx.conf
    notify: restart nginx

handlers:
  - name: restart nginx
    service:
    name: nginx
    state: restarted
```

このPlaybookでは、NginxがリッスンするポートやNginxを実行するユーザーを変数で指定します。これにより、このプレイブックはより柔軟で、さまざまな環境に適応できるようになっています。

### 5.プレイブックをテストする

Ansible のプレイブックをテストすることは、エラーを発見し、プレイブックが期待通りに動作していることを確認するのに役立つベストプラクティスと言えます。Ansible playbook をテストするための人気のあるツールの 1 つが Molecule です。

Moleculeは、一貫した自動化された方法でプレイブックをテストすることができるテストフレームワークです。Moleculeは、仮想マシンを作成し、プレイブックを適用し、すべてが期待通りに動作していることを確認することができます。これにより、本番環境にデプロイする前に、エラーを発見し、プレイブックが正しく動作していることを確認することができます。

以下は、Moleculeを使用してAnsibleロールをテストする方法の例です：

```bash
molecule init role myrole
cd myrole
molecule test
```

## 結論

今回は、複雑なITインフラの管理に役立つ強力な自動化ツールであるAnsibleを紹介しました。インベントリ、プレイブック、モジュール、ロールなど、Ansibleの基本的な概念について説明しました。

また、バージョン管理の使用、ロールによるプレイブックの整理、タグと変数の使用、プレイブックのテストなど、Ansibleを使用するためのベストプラクティスも説明しました。

Ansibleを初めて使う方は、まずは簡単なPlaybookを試してみて、時間をかけて徐々にスキルと知識を高めていくことをお勧めします。練習を重ねれば、最も複雑なインフラストラクチャのタスクも簡単に自動化できるようになるはずです！
