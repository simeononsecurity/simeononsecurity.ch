---
title: "究極ガイド: Ubuntu Debian および CentOS RHEL のオフライン Linux アップデート"
date: 2023-05-30
toc: true
draft: false
description: "Discover the best methods for handling offline Linux updates on Ubuntu/Debian and CentOS/RHEL systems, using local repositories or caches."
tags: ["Linuxのアップデート", "Ubuntu", "デビアン", "CentOS", "RHEL", "オフラインアップデート", "ローカルリポジトリ", "キャッシュ", "サーバーのセットアップ", "クライアントのセットアップ", "適切なミラー", "デブミラー", "リポジトリの作成", "apt-cacher-ng", "ヤムクロン", "Linux システムのアップデート", "オフラインパッケージのアップデート", "オフラインソフトウェアアップデート", "ローカルパッケージリポジトリ", "ローカルパッケージキャッシュ", "オフライン Linux アップデート", "オフラインアップデートの処理", "オフラインアップデート方法", "オフラインでのシステムメンテナンス", "Linuxサーバーのアップデート", "Linuxクライアントのアップデート", "オフラインのソフトウェア管理", "オフラインパッケージ管理", "戦略を更新する", "Linuxのセキュリティアップデート"]
cover: "/img/cover/A_cartoon_illustration_depicting_a_server_and_multiple_clients.png"
coverAlt: "オフラインで更新を交換するサーバーと複数のクライアント デバイスを描いた漫画のイラスト。"
coverCaption: ""
---

**Ubuntu/Debian および CentOS/RHEL の Linux アップデートをオフラインでインストールする最良の方法**

Linux のアップデートは、システムのセキュリティと安定性を維持するために不可欠です。ただし、シナリオによっては、インターネット接続が制限されているか存在しないオフライン環境に対処する必要がある場合があります。このような場合、オフラインで更新プログラムをインストールするための適切な戦略を立てることが重要になります。この記事では、オフライン環境で Ubuntu/Debian および CentOS/RHEL の Linux アップデートをインストールするための最良の方法**を説明します。特に、ローカル リポジトリまたはキャッシュの使用に重点を置いています。

## ローカル リポジトリのセットアップ

オフライン更新を処理する最も効果的な方法の 1 つは、ローカル リポジトリをセットアップすることです。ローカル リポジトリには、必要なソフトウェア パッケージとアップデートがすべて含まれているため、インターネットに接続していなくてもシステムをアップデートできます。 Debian ベースと Red Hat ベースの両方のディストリビューションにローカル リポジトリを設定する方法は次のとおりです。

### Debian/Ubuntu の場合

1. まず、インターネットにアクセスできるサーバー上に **Debian リポジトリ ミラー**をセットアップします。次のようなツールを使用できます [`apt-mirror`](https://manpages.debian.org/jessie/apt-mirror/apt-mirror.1.en.html) or [`debmirror`](https://wiki.debian.org/debmirror) 公式 Debian または Ubuntu リポジトリのローカル ミラーを作成します。

#### apt-mirror を使用した Debian リポジトリ ミラーのセットアップ:

```shell
# Install apt-mirror
sudo apt-get install apt-mirror

# Edit the apt-mirror configuration file
sudo nano /etc/apt/mirror.list

# Uncomment the deb line for the desired repository
# For example, uncomment the line for Ubuntu 20.04:
# deb http://archive.ubuntu.com/ubuntu focal main restricted universe multiverse

# Specify the mirror location
# Modify the base_path to your desired location
set base_path /path/to/mirror

# Save and close the file

# Run apt-mirror to start the mirroring process
sudo apt-mirror

# Wait for the mirroring process to complete
```

#### debmirror を使用した Debian リポジトリ ミラーのセットアップ:
```shell
# Install debmirror
sudo apt-get install debmirror

# Create a directory to store the mirror
sudo mkdir /path/to/mirror

# Run debmirror to start the mirroring process
# Replace <RELEASE> with the Debian or Ubuntu release and <MIRROR_URL> with the official repository URL
# For example, to mirror Ubuntu 20.04:
sudo debmirror --arch=amd64 --verbose --method=http --dist=<RELEASE> --root=<MIRROR_URL> /path/to/mirror

# Wait for the mirroring process to complete
```
#### Debian クライアントの手順

2. ** を編集してローカル リポジトリを構成します。`/etc/apt/sources.list` オフライン システム上のファイル。デフォルトのリポジトリ URL をローカル リポジトリ URL に置き換えます。たとえば、ローカル リポジトリが次の場所でホストされている場合、 `http://local-repo/ubuntu` を更新する `sources.list` それに応じてファイルを作成します。

例 `/etc/apt/sources.list` ファイル：
```
deb http://local-repo/ubuntu focal main restricted universe multiverse
```

3. 構成が更新されたら、** を実行できます。`apt update` オフライン システム上でコマンドを使用して、ローカル リポジトリからパッケージ リストを取得します。

```shell
sudo apt update
```

4. 最後に、** を使用できます。`apt upgrade` コマンドを使用して、ローカル リポジトリから利用可能なアップデートをインストールします。

```shell
sudo apt upgrade
```

### CentOS/RHEL の場合

1. CentOS/RHEL のローカル リポジトリを設定するには、 [**`createrepo`**](https://linux.die.net/man/8/createrepo) 道具。このツールは、ローカル リポジトリに必要なメタデータを作成します。

2. インターネットにアクセスできるサーバー上にリポジトリ ファイルを保存するディレクトリを作成します。たとえば、** というディレクトリを作成できます。`local-repo`

3. 関連するすべての RPM パッケージ ファイルと更新を **`local-repo` ディレクトリ。

#### createrepo を使用したローカル リポジトリのセットアップ:

```shell
# Install the createrepo tool
sudo yum install createrepo

# Create a directory to store the repository files
sudo mkdir /path/to/local-repo

# Move or copy the RPM package files and updates to the local-repo directory

# Run the createrepo command to generate the necessary repository metadata
sudo createrepo /path/to/local-repo

# Update the repository metadata whenever new packages are added or removed
sudo createrepo --update /path/to/local-repo
```
4. リポジトリのメタデータが生成されたら、全体を転送できます。 `local-repo` USB ドライブまたはその他の手段を使用して、ディレクトリをオフライン システムにコピーします。

5. オフライン システムで、新しいファイルを作成します。 `.repo` 内のファイル `/etc/yum.repos.d/` ディレクトリ。必要な構成の詳細を入力します。 `baseurl` ローカル リポジトリ ディレクトリを指します。

たとえば、という名前のファイルを作成します。 `local.repo` の中に `/etc/yum.repos.d/` ディレクトリに移動し、次のコンテンツを追加します。
```shell
sudo nano /etc/yum.repos.d/local.repo
```
```toml
[local]
name=Local Repository
baseurl=file:///path/to/local-repo
enabled=1
gpgcheck=0
```
6. ファイルを保存し、エディタを終了します。

7. リポジトリを構成した後、yum update コマンドを使用してローカル リポジトリから更新をインストールできます。

```shell
sudo yum update
```

このコマンドは、ローカル リポジトリのパッケージを使用してシステム上のパッケージを更新します。

を実行して、ローカル リポジトリを忘れずに更新してください。 `createrepo` 新しいパッケージがリポジトリに追加またはリポジトリから削除されるたびに、このコマンドを実行します。

交換が必要となりますのでご注意ください `/path/to/local-repo` リポジトリ ファイルを保存したディレクトリへの実際のパスを置き換えます。

## ローカル キャッシュのセットアップ

オフライン更新を処理するもう 1 つの方法は、ローカル キャッシュを設定することです。ローカル キャッシュには、ダウンロードしたパッケージとアップデートが保存されるため、個別にダウンロードすることなく、それらを複数のシステムに配布できます。このキャッシュをオンライン システムに設定してから、ディレクトリをオフラインのシステムに移動して、他のシステムがパッケージにアクセスできるようにします。 Debian ベースと Red Hat ベースの両方のディストリビューションにローカル キャッシュを設定する方法は次のとおりです。

### Debian/Ubuntu の場合

1. インストールと設定 [**`apt-cacher-ng`**](https://www.unix-ag.uni-kl.de/~bloch/acng/) Debian/Ubuntu パッケージのキャッシュ プロキシ。 ** コマンドを実行してインストールできます。`sudo apt-get install apt-cacher-ng`

2. インストールしたら、** を編集します。`/etc/apt-cacher-ng/acng.conf` ファイルを使用してキャッシュ動作を構成します。 ** を確認してください。`PassThroughPattern` パラメータには必要なリポジトリ URL が含まれます。

```shell
sudo nano /etc/apt-cacher-ng/acng.conf
```
コメントを解除するか、必要なリポジトリ URL を PassThroughPattern パラメータに追加します。たとえば、Ubuntu リポジトリを含めるには、次の行を追加するかコメントを解除します。
```yml
PassThroughPattern: (security|archive).ubuntu.com/ubuntu
```
ファイルを保存してエディタを終了します。

3. を開始します。 [**`apt-cacher-ng`**](https://www.unix-ag.uni-kl.de/~bloch/acng/) コマンド ** を使用したサービス`sudo systemctl start apt-cacher-ng`

```shell
sudo systemctl start apt-cacher-ng
```

4. オフライン システムで、** を設定します。`/etc/apt/apt.conf.d/02proxy` ファイルをローカル キャッシュを指すように指定します。次の行を使用します: **`Acquire::http::Proxy "http://<cache-server-ip>:3142";`

```shell
sudo nano /etc/apt/apt.conf.d/02proxy
```
次の行をファイルに追加し、 <cache-server-ip> をキャッシュ サーバーの IP アドレスに置き換えます。
```text
Acquire::http::Proxy "http://<cache-server-ip>:3142";
```
ファイルを保存してエディタを終了します

5. ここで、** を実行すると、`apt update` と **`apt upgrade` オフライン システム上でコマンドを実行すると、ローカル キャッシュからパッケージが取得されます。

```shell
sudo apt update
sudo apt upgrade
```
これらのコマンドはローカル キャッシュからアップデートを取得してインストールするため、オフライン システムでのインターネット アクセスの必要性が軽減されます。

** を交換する必要があることに注意してください。`<cache-server-ip>` **apt-cacher-ng** がインストールされているマシンの実際の IP アドレスに置き換えます。

### CentOS/RHEL の場合

1. CentOS/RHEL の場合、次を使用できます。 [**`yum-cron`**](https://linux.die.net/man/8/yum-cron) ローカル キャッシュをセットアップします。コマンド ** を実行してインストールします。`sudo yum install yum-cron`

2. **を編集します`/etc/yum/yum-cron.conf` ファイルを作成して ** を設定します`download_only` パラメータを ** に設定`yes` これにより、パッケージはダウンロードのみが行われ、自動的にはインストールされなくなります。

```shell
sudo nano /etc/yum/yum-cron.conf
```

3. を開始します。 [**`yum-cron`**](https://linux.die.net/man/8/yum-cron) コマンド ** を使用したサービス`sudo systemctl start yum-cron`

```shell
sudo systemctl start yum-cron
```

4. オフライン システムで、ダウンロードしたパッケージを保存するローカル ディレクトリを作成します (例: **)。`/var/cache/yum`

```shell
sudo mkdir /var/cache/yum
```

5. ダウンロードしたパッケージをオンライン システムからローカル キャッシュ ディレクトリにコピーします。

```shell
sudo cp -R /var/cache/yum /path/to/local/cache
```

交換 `/path/to/local/cache` オフライン システム上のローカル キャッシュ ディレクトリへのパスを使用します。

6. オフライン システムで、新しい ** を作成します。`.repo` **内のファイル`/etc/yum.repos.d/` ディレクトリ。ローカル キャッシュ ディレクトリを指します。

```bash
sudo nano /etc/yum.repos.d/local.repo
```
次の内容をファイルに追加し、置き換えます `<local-cache-path>` ローカル キャッシュ ディレクトリへのパスを指定します。
```toml
[local]
name=Local Cache
baseurl=file:///path/to/local/cache
enabled=1
gpgcheck=0
```
ファイルを保存してエディタを終了します。

7. 最後に、** を使用できます。`yum update` オフライン システムでコマンドを使用して、ローカル キャッシュから更新をインストールします。

```shell
sudo yum update
```

このコマンドは、ローカル キャッシュのパッケージを使用して、オフライン システム上のパッケージを更新します。

** を交換する必要があることに注意してください。`<local-cache-path>` オフライン システム上のローカル キャッシュ ディレクトリへの実際のパスを使用します。

______

＃＃ 結論

オフライン環境で Linux アップデートを処理するのは難しい場合がありますが、適切なアプローチを使用すれば、システムを最新かつ安全に保つことができます。この記事では、Ubuntu/Debian および CentOS/RHEL の更新プログラムをオフラインでインストールする最適な方法について説明しました。ローカル リポジトリのセットアップとローカル キャッシュのセットアップを検討し、Debian ベースと Red Hat ベースの両方のディストリビューションについて段階的な手順を説明しました。

これらの方法に従うことで、オフライン環境でも Linux システムのセキュリティと安定性を維持できます。ローカル リポジトリまたはキャッシュを定期的に更新して、最新の更新を含めるようにしてください。

______

## 参考文献

- [apt-mirror Documentation](https://manpages.debian.org/jessie/apt-mirror/apt-mirror.1.en.html)
- [debmirror Documentation](https://wiki.debian.org/debmirror)
- [createrepo Documentation](https://linux.die.net/man/8/createrepo)
- [apt-cacher-ng Documentation](https://www.unix-ag.uni-kl.de/~bloch/acng/)
- [yum-cron Documentation](https://linux.die.net/man/8/yum-cron)
