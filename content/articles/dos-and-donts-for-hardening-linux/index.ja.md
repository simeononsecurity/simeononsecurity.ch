---
title: "Linuxシステムのハードニングに欠かせない「やるべきこと」と「やってはいけないこと」。"
date: 2023-02-28
toc: true
draft: false
description: "アップデート、ファイアウォールの使用、SELinuxやAppArmorの有効化、パスワードポリシーの設定、システムログの監視など、Linuxシステムの堅牢化に不可欠なDoとDonを学ぶことができます。"
tags: ["Linuxのセキュリティ", "システムハードニング", "ファイヤーウォール", "セリナックス", "AppArmor", "パスワードポリシー", "システムアップデート", "システムログ", "セキュリティモジュール", "アクセスコントロールポリシー", "サイバーセキュリティ", "システムセキュリティ", "ネットワークセキュリティ", "脆弱性管理", "セキュリティベストプラクティス", "ITセキュリティ", "情報セキュリティ", "ソフトウェアアップデート", "ルートアクセス", "パスワードマネージャ"]
cover: "/img/cover/A_cartoon_lock_holding_a_shield_with_the_word_Linux_on_it.png"
coverAlt: "Linuxと書かれた盾を持つ漫画のロックが、矢を盾に跳ね返される。"
coverCaption: ""
---


Linuxは、個人でも企業でもよく使われるオペレーティングシステムです。オープンソースであることから、他のオペレーティング・システムよりも安全だと思われがちですが、システムとデータの安全性を確保するためには、適切なハードニングが必要です。この記事では、Linuxシステムの安全性を維持するための一般的なハードニングの方法と注意点について説明します。

## Do's：

### システムを常にアップデートしておく

システムを常に最新の状態に保つ [Linux](https://simeononsecurity.ch/articles/how-do-i-learn-linux/)システムのセキュリティを維持するためには、システムを最新にすることが重要です。定期的なアップデートは、セキュリティの脆弱性やバグを修正するのに役立ち、潜在的な攻撃に対してシステムの安全性を維持することを保証します。ここでは、**apt-get** または **yum** パッケージマネージャを使用して Linux システムを更新する方法の例をいくつか紹介します：

#### apt-get を使用した Ubuntu のアップデート

apt-get**を使用してUbuntuシステムを更新するには、ターミナルウィンドウを開き、次のように入力します：
```bash
sudo apt-get update
```

これにより、Ubuntuパッケージリポジトリから最新のパッケージリストがダウンロードされます。このコマンドが完了したら、次のコマンドを使用して、利用可能なアップデートをインストールすることができます：

```bash
sudo apt-get upgrade

```

これにより、お使いのシステムで利用可能なアップデートがダウンロードされ、インストールされます。

### yumを使ったCentOSのアップデート

yum**を使用してCentOSシステムをアップデートするには、ターミナルウィンドウを開き、次のように入力します：

```bash
sudo yum update
```

これにより、お使いのシステムで利用可能なすべてのアップデートがダウンロードされ、インストールされます。また、次のコマンドを使用して、古いパッケージや未使用のパッケージをクリーンアップすることもできます：

```bash
sudo yum autoremove
```

これにより、お使いのシステムで不要になったパッケージが削除されます。

Linuxシステムのセキュリティと安定性を確保するために、定期的にアップデートを確認し、インストールすることを忘れないでください。


### ファイアウォールを使用する

ファイアウォールは、不正アクセスやその他のサイバー脅威から保護するためのものであり、Linux システムにとって不可欠なセキュリティ対策です。ここでは、Linux システムで **ufw** ファイアウォールを使用する方法を説明します：

#### Ubuntu ベースのシステムにおける ufw のインストールと有効化

ufw**をインストールし、有効にするには、ターミナルウィンドウを開き、次のように入力します：

```bash
sudo apt install ufw -y
sudo ufw allow ssh
sudo ufw enable
```

HTTPトラフィックの受信を許可する（ポート80）：

```bash
sudo ufw allow http
```

特定のIPアドレスからの受信をブロックする場合：

```bash
sudo ufw deny from <ip_address>
```

ルールを削除するには、次のようにします：
```bash
sudo ufw delete <rule_number>
```

と入力することで、現在の**ufw**ルールを表示することができます：

```bash
sudo ufw status
```


これにより、現在のルールとそのステータスが表示されます。

潜在的な脅威からシステムを保護するために、**ufw**ルールを定期的に見直し、更新することを忘れないようにしてください。


#### CentOS ベースのシステムにおける firewalld のインストールと有効化

CentOSのデフォルトのファイアウォールである**firewalld**をインストールし、有効にするには、以下のコマンドを使用することができます：

```bash
sudo yum install firewalld
sudo systemctl enable firewalld
sudo systemctl start firewalld
```

これにより、**firewalld**がインストールされ、システム上で有効になります。

#### CentOSベースのシステムでfirewalldルールを設定する

firewalld**を有効にしたら、そのルールを設定して、受信および送信トラフィックを許可またはブロックすることができます。以下はその例です：

SSH トラフィック（ポート 22）の着信を許可する場合：

```bash
sudo firewall-cmd --permanent --add-service=ssh
sudo firewall-cmd --reload
```

HTTPトラフィックの受信を許可する（ポート80）：

```bash
sudo firewall-cmd --permanent --add-service=http
sudo firewall-cmd --reload
```

特定のIPアドレスからの受信をブロックする場合：

```bash
sudo firewall-cmd --permanent --add-rich-rule='rule family="ipv4" source address="<ip_address>" reject'
sudo firewall-cmd --reload
```

ルールを削除するには、次のようにします：

```bash
sudo firewall-cmd --permanent --remove-<type>=<rule>
sudo firewall-cmd --reload
```

と入力すると、現在の**firewalld**ルールを表示することができます：

```bash
sudo firewall-cmd --list-all
```

これにより、現在のルールとそのステータスが表示されます。

定期的に**firewalld**のルールを見直し、更新することを忘れずに、システム

### SELinux または AppArmor を有効にします。

SELinux (Security-Enhanced Linux) と AppArmor は、Linux システムで強制的なアクセス制御ポリシーを適用するために使用できる 2 つのセキュリティモジュールです。最新のLinuxディストリビューションには、デフォルトでSELinuxまたはAppArmorがインストールされており、これらを有効にしてシステムのセキュリティを強化することができます。

#### CentOS ベースのシステムで SELinux を有効にする

お使いのシステムで SELinux が有効になっているかどうかを確認するには、次のコマンドを実行します：

```bash
sestatus
```

SELinuxがインストールされていない場合は、以下のコマンドでインストールすることができます：

```bash
sudo yum install selinux-policy selinux-policy-targeted
```

SELinuxを有効にするには、**/etc/selinux/config**ファイルを編集して、**SELINUX**変数を**enforcing**に設定する必要があります：

```bash
sudo nano /etc/selinux/config
```
**SELINUX=enforcingに変更する**。
```
SELINUX=enforcing
```

CTRL+XとY、そしてEnterでファイルを保存して終了し、システムを再起動します。

#### UbuntuベースのシステムでAppArmorを有効にする

お使いのシステムでAppArmorが有効になっているかどうかを確認するには、次のコマンドを実行します：
```bash
sudo apparmor_status
```


AppArmorがインストールされていない場合は、以下のコマンドでインストールすることができます：
```bash
sudo apt-get install apparmor
```

AppArmorを有効にするには、**/etc/default/grub**ファイルを編集して、**GRUB_CMDLINE_LINUX**変数に**security=apparmor**パラメータを追加する必要があります：

```bash
sudo nano /etc/default/grub
```
**セキュリティ=apparmor**を追加する。
```bash
GRUB_CMDLINE_LINUX="... security=apparmor"
```

CTRL+XとYを使用してファイルを保存して終了してから、次のコマンドを実行してシステムのブートローダ設定を更新します：

```bash
sudo update-grub
```

最後に、システムを再起動します。

SELinuxまたはAppArmorを有効にすると、それらのポリシーを設定して、プロセスの特権を制限し、システムリソースへのアクセスを制限することができます。これにより、攻撃が成功した場合の潜在的な影響を最小限に抑え、システム全体のセキュリティを強化することができます。


### パスワードポリシーの設定

パスワードポリシーの構成は、Linux システムのセキュリティを強化するための重要なステップです。強力なパスワード要件を実施することで、ユーザーアカウントの安全性を確保し、潜在的な攻撃から保護することができます。ここでは、Linux システムでパスワードポリシーを構成する方法を説明します：

#### Ubuntu でのパスワードポリシーの設定

Ubuntu でパスワードポリシーを構成するには、**pam_pwquality** モジュールを使用できます。このモジュールは、パスワードポリシーの実施に使用できるパスワード強度チェックのセットを提供します。pam_pwquality**モジュールをインストールするには、ターミナルウィンドウを開き、次のように入力します：

```bash
sudo apt-get install libpam-pwquality
```

モジュールがインストールされると、**/etc/pam.d/common-password**ファイルを編集することで、その設定を行うことができます。例えば、パスワードの最小文字数を8文字とし、少なくとも1つの大文字、1つの小文字、1つの数字、1つの特殊文字を要求するためには、ファイルに次の行を追加します：

```bash
password requisite pam_pwquality.so minlen=8 ucredit=-1 lcredit=-1 dcredit=-1 ocredit=-1
```

また、ファイルに行を追加することで、パスワードの最大年齢など、その他の設定も可能です。

#### CentOSでのパスワードポリシーの設定

CentOS でパスワードポリシーを設定するには、**authconfig** ツールを使用します。このツールは、パスワードポリシーを構成するために使用できるオプションのセットを提供します。たとえば、パスワードの最小長を 8 文字とし、少なくとも 1 つの大文字、1 つの小文字、1 つの数字、および 1 つの特殊文字を要求するには、次のコマンドを使用します：

```bash
sudo authconfig --passalgo=sha512 --update --enablereqlower --enablerequpper --enablereqdigit --enablereqother --passminlen=8
```

これにより、システムの **/etc/pam.d/system-auth** および **/etc/pam.d/password-auth** ファイルが更新され、指定したパスワードポリシーが適用されます。

パスワードポリシーが潜在的な攻撃に対して有効であることを確認するために、定期的に見直し、更新することを忘れないでください。


### システムログの監視

システムログの監視は、Linux システムのセキュリティを維持する上で重要な要素です。システムログは、ログインの失敗、エラー、その他の重要なイベントなどのシステムの活動を記録し、潜在的なセキュリティ脅威や注意を必要とするその他の問題に対する貴重な洞察を提供することができます。ここでは、システムログを監視する方法について説明します：

#### Journalctl コマンドを使用する

ほとんどの最新の Linux ディストリビューションでは、システムログを表示するために **journalctl** コマンドを使用できます。このコマンドには、ログエントリーのフィルタリングや検索に使用できるさまざまなオプションが用意されています。

すべてのログエントリーを表示するには、次のコマンドを実行するだけです：

```bash
sudo journalctl
```

これにより、すべてのログエントリーが表示され、最新のエントリーが一番下に表示されます。

サービスやプロセスなどの特定のユニットでログエントリをフィルタリングするには、**-u**オプションの後にユニット名を付けます。たとえば、**sshd**サービスのログエントリを表示するには、次のコマンドを実行します：
```bash
sudo journalctl -u sshd
```


特定の時間範囲でログエントリーをフィルタリングするには、**--since**および**--until**オプションの後に、タイムスタンプまたは時間範囲を指定することができます。たとえば、過去1時間のログエントリーを表示するには、次のコマンドを実行します：

```bash
sudo journalctl --since "1 hour ago"
```

#### ログ管理ツールの使用

大規模または複雑なシステムの場合、ログ管理ツールを使用してシステムログを収集および分析することが有用な場合があります。ログ管理ツールは、リアルタイムのログ監視、ログ集計、ログ分析などの高度な機能を提供し、潜在的なセキュリティ脅威の特定と対応をより効率的に行うことができます。

Linux用のログ管理ツールの例としては、以下のものがあります：

- Logwatch**：システムログのサマリーを毎日電子メールで提供するシンプルなログ分析ツールです。
- Logrotate**：ログファイルを自動的に回転させ、圧縮してディスクスペースを節約するツール
- ELKスタック**：Elasticsearch、Logstash、Kibanaを組み合わせたオープンソースのログ管理ツールで、リアルタイムのログ監視と分析機能を提供する。

潜在的なセキュリティ脅威をタイムリーに検知し対応するために、システムログを定期的に確認・分析することを忘れないようにしましょう。

______

## Don'ts：

### 弱いパスワードの使用

脆弱なパスワードを使用することは、Linux システムを攻撃されやすい状態にする一般的な間違いです。攻撃者は、一般的な単語、名前、または日付に基づいたパスワードを推測するツールを使用することができます。簡単に推測できない、強力でユニークなパスワードを使用することが重要です。

大文字、小文字、数字、特殊文字を組み合わせて使用することで、強力なパスワードを作成することができます。を使用するのもよい習慣です。 [password manager](https://simeononsecurity.ch/articles/bitwarden-and-keepassxc-vs-the-rest/) to generate and store complex passwords securely. [Password managers](https://simeononsecurity.ch/articles/bitwarden-and-keepassxc-vs-the-rest/)は、パスワードを覚えて、複数のアカウントで同じパスワードを使用しないようにするのにも役立ちます。

### rootのSSHアクセスを許可する

root SSH アクセスを許可することは、攻撃者が Linux システムを完全に制御できるようにするセキュリティリスクです。代わりに、非 root ユーザーアカウントでシステムにログインし、**sudo** コマンドを使用して特権を昇格する必要があります。これは、ユーザーアカウントの特権を制限することによって、攻撃の潜在的な影響を制限するのに役立ちます。

### 不要なソフトウェアをインストールする

不要なソフトウェアをインストールすると、Linux システムの攻撃対象が増え、攻撃に対してより脆弱になる可能性があります。システムにとって必要なソフトウェアのみをインストールし、不要なソフトウェアは削除することが重要です。これにより、システム上の潜在的な脆弱性の数を減らし、攻撃が成功するリスクを最小化することができます。

### 時代遅れのソフトウェアを使う

古いソフトウェアを使用すると、既知の脆弱性を悪用した攻撃に対して、システムが脆弱な状態になる可能性があります。セキュリティを確保するためには、常に最新版のソフトウェアを使用し、定期的にアップデートすることが重要です。これにより、既知の脆弱性にパッチを適用し、潜在的な攻撃からシステムを保護することができます。

______

## 結論

結論として、Linux システムのセキュリティを確保し、保持しているデータを保護するために、ハードニングは非常に重要です。この記事で説明した「やること」と「やらないこと」に従うことで、システムを保護し、サイバー脅威のリスクを低減するための重要なステップを踏むことができます。システムを常に最新の状態に保つこと、ファイアウォールを使用すること、パスワードポリシーを設定すること、システムログを監視することを忘れないでください。弱いパスワードの使用、自動アップデートの無効化、SSHのルートアクセス許可、不要なソフトウェアのインストール、古いソフトウェアの使用は避けましょう。これらのベストプラクティスを念頭に置くことで、Linuxシステムの安全性と保護を確保することができます。

## 参考文献

- [The Center for Internet Security's Linux Hardening Guide](https://www.cisecurity.org/cis-hardened-images/)
- [Red Hat Enterprise Linux Security Guide](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/security_guide/index)
- [Ubuntu Security Documentation](https://ubuntu.com/security)
- [Linux Security Wiki](https://en.wikibooks.org/wiki/Linux_Security)
