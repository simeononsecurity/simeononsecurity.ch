---
title: "终极指南：Ubuntu Debian 和 CentOS RHEL 的离线 Linux 更新"
date: 2023-05-30
toc: true
draft: false
description: "Discover the best methods for handling offline Linux updates on Ubuntu/Debian and CentOS/RHEL systems, using local repositories or caches."
tags: ["Linux 更新", "Ubuntu", "德比安", "中央操作系统", "RHEL", "离线更新", "本地存储库", "缓存", "服务器设置", "客户端设置", "镜像", "debmirror", "创建仓库", "apt-缓存-ng", "yumcron", "Linux 系统更新", "离线包更新", "离线软件更新", "本地包存储库", "本地包缓存", "离线 Linux 更新", "处理离线更新", "离线更新方法", "离线系统维护", "Linux 服务器更新", "Linux 客户端更新", "离线软件管理", "离线包管理", "更新策略", "Linux 安全更新"]
cover: "/img/cover/A_cartoon_illustration_depicting_a_server_and_multiple_clients.png"
coverAlt: "描绘服务器和多个客户端设备离线交换更新的卡通插图。"
coverCaption: ""
---

**处理 Ubuntu/Debian 和 CentOS/RHEL 离线安装 Linux 更新的最佳方法**

Linux 更新对于维护系统的安全性和稳定性至关重要。但是，在某些情况下，您可能不得不处理 Internet 连接受限或不存在的离线环境。在这种情况下，制定适当的离线安装更新策略就变得至关重要。本文将指导您通过**在离线环境中为 Ubuntu/Debian 和 CentOS/RHEL** 安装 Linux 更新的最佳方法，特别侧重于使用本地存储库或缓存。

## 设置本地存储库

处理离线更新的最有效方法之一是设置本地存储库。本地存储库包含所有必要的软件包和更新，允许您在没有互联网连接的情况下更新系统。以下是为基于 Debian 和基于 Red Hat 的发行版设置本地存储库的方法：

### 对于 Debian/Ubuntu

1. 首先在可以访问互联网的服务器上设置 **Debian 存储库镜像**。你可以使用像这样的工具 [`apt-mirror`](https://manpages.debian.org/jessie/apt-mirror/apt-mirror.1.en.html) or [`debmirror`](https://wiki.debian.org/debmirror) 创建官方 Debian 或 Ubuntu 存储库的本地镜像。

#### 使用 apt-mirror 设置 Debian 存储库镜像：

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

#### 使用 debmirror 设置 Debian 存储库镜像：
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
#### Debian 客户端说明

2. 通过编辑 ** 配置您的本地存储库`/etc/apt/sources.list` 离线系统上的文件。将默认存储库 URL 替换为本地存储库 URL。例如，如果您的本地存储库托管在 `http://local-repo/ubuntu` 更新 `sources.list` 相应地归档。

例子 `/etc/apt/sources.list` 文件：
```
deb http://local-repo/ubuntu focal main restricted universe multiverse
```

3.配置更新后，您可以运行**`apt update` 命令在离线系统上从本地存储库中获取包列表。

```shell
sudo apt update
```

4.最后，你可以使用**`apt upgrade` 命令从本地存储库安装可用更新。

```shell
sudo apt upgrade
```

### 对于 CentOS/RHEL

1. 要为 CentOS/RHEL 设置本地存储库，您需要使用 [**`createrepo`**](https://linux.die.net/man/8/createrepo) 工具。此工具为本地存储库创建必要的元数据。

2. 在可以访问互联网的服务器上创建一个目录来存储存储库文件。例如，您可以创建一个名为 ** 的目录`local-repo`

3.复制所有相关的RPM包文件和更新到**`local-repo` 目录。

#### 使用 createrepo 设置本地存储库：

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
4. 生成存储库元数据后，您可以传输整个 `local-repo` 使用 USB 驱动器或任何其他方式将目录复制到离线系统。

5.在离线系统上，新建一个 `.repo` 文件在 `/etc/yum.repos.d/` 目录。提供必要的配置详细信息，例如 `baseurl` 指向本地存储库目录。

例如，创建一个名为 `local.repo` 在里面 `/etc/yum.repos.d/` 目录并添加以下内容：
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
6. 保存文件并退出编辑器。

7. 配置存储库后，您可以使用 yum update 命令从本地存储库安装更新。

```shell
sudo yum update
```

此命令将使用本地存储库中的包更新系统上的包。

请记住通过运行更新本地存储库 `createrepo` 每当从存储库中添加或删除新包时，都会执行命令。

请注意，您需要更换 `/path/to/local-repo` 使用存储存储库文件的目录的实际路径。

## 设置本地缓存

处理离线更新的另一种方法是设置本地缓存。本地缓存存储下载的包和更新，使您可以跨多个系统分发它们，而无需单独下载。您可以在在线系统上设置此缓存，然后将目录移动到离线系统以允许其他系统访问这些包。以下是为基于 Debian 和基于 Red Hat 的发行版设置本地缓存的方法：

### 对于 Debian/Ubuntu

1.安装配置 [**`apt-cacher-ng`**](https://www.unix-ag.uni-kl.de/~bloch/acng/) Debian/Ubuntu 软件包的缓存代理。您可以通过运行命令来安装它**`sudo apt-get install apt-cacher-ng`

2.安装后，编辑**`/etc/apt-cacher-ng/acng.conf` 文件来配置缓存行为。确保**`PassThroughPattern` 参数包括必要的存储库 URL。

```shell
sudo nano /etc/apt-cacher-ng/acng.conf
```
取消注释或将必要的存储库 URL 添加到 PassThroughPattern 参数。例如，要包含 Ubuntu 存储库，请添加或取消注释以下行：
```yml
PassThroughPattern: (security|archive).ubuntu.com/ubuntu
```
保存文件并退出编辑器。

3.开始 [**`apt-cacher-ng`**](https://www.unix-ag.uni-kl.de/~bloch/acng/) 使用命令服务**`sudo systemctl start apt-cacher-ng`

```shell
sudo systemctl start apt-cacher-ng
```

4.在离线系统上，配置**`/etc/apt/apt.conf.d/02proxy` 文件指向本地缓存。使用以下行：**`Acquire::http::Proxy "http://<cache-server-ip>:3142";`

```shell
sudo nano /etc/apt/apt.conf.d/02proxy
```
将以下行添加到文件中，将 <cache-server-ip> 替换为缓存服务器的 IP 地址：
```text
Acquire::http::Proxy "http://<cache-server-ip>:3142";
```
保存文件并退出编辑器

5. 现在，当你运行 **`apt update` 和 **`apt upgrade` 在离线系统上执行命令，它们将从本地缓存中检索包。

```shell
sudo apt update
sudo apt upgrade
```
这些命令将从本地缓存中获取并安装更新，从而减少离线系统对 Internet 访问的需求。

请注意，您需要更换 **`<cache-server-ip>` 使用安装了 **apt-cacher-ng** 的机器的实际 IP 地址。

### 对于 CentOS/RHEL

1.对于CentOS/RHEL，你可以使用 [**`yum-cron`**](https://linux.die.net/man/8/yum-cron) 设置本地缓存。通过运行命令安装它**`sudo yum install yum-cron`

2.编辑**`/etc/yum/yum-cron.conf` 文件并配置**`download_only` 参数为**`yes` 这可确保仅下载包，而不会自动安装包。

```shell
sudo nano /etc/yum/yum-cron.conf
```

3.开始 [**`yum-cron`**](https://linux.die.net/man/8/yum-cron) 使用命令服务**`sudo systemctl start yum-cron`

```shell
sudo systemctl start yum-cron
```

4. 在离线系统上，创建一个本地目录来存放下载的包，例如**`/var/cache/yum`

```shell
sudo mkdir /var/cache/yum
```

5.将在线系统下载的包复制到本地缓存目录。

```shell
sudo cp -R /var/cache/yum /path/to/local/cache
```

代替 `/path/to/local/cache` 使用离线系统上本地缓存目录的路径。

6.在离线系统上，新建一个**`.repo` 文件在**`/etc/yum.repos.d/` directory，指向本地缓存目录。

```bash
sudo nano /etc/yum.repos.d/local.repo
```
将以下内容添加到文件中，替换 `<local-cache-path>` 使用本地缓存目录的路径：
```toml
[local]
name=Local Cache
baseurl=file:///path/to/local/cache
enabled=1
gpgcheck=0
```
保存文件并退出编辑器。

7.最后，你可以使用**`yum update` 命令在脱机系统上从本地缓存安装更新。

```shell
sudo yum update
```

此命令将使用本地缓存中的包更新离线系统上的包。

请注意，您需要更换 **`<local-cache-path>` 使用离线系统上本地缓存目录的实际路径。

______

＃＃ 结论

在离线环境中处理 Linux 更新可能具有挑战性，但通过正确的方法，您可以确保您的系统保持最新和安全。在本文中，我们讨论了处理 Ubuntu/Debian 和 CentOS/RHEL 离线安装更新的最佳方法。我们探索了设置本地存储库和设置本地缓存，为基于 Debian 和基于 Red Hat 的发行版提供了分步说明。

通过遵循这些方法，即使在离线环境中，您也可以保持 Linux 系统的安全性和稳定性。请记住定期更新本地存储库或缓存以包含最新更新。

______

＃＃ 参考

- [apt-mirror Documentation](https://manpages.debian.org/jessie/apt-mirror/apt-mirror.1.en.html)
- [debmirror Documentation](https://wiki.debian.org/debmirror)
- [createrepo Documentation](https://linux.die.net/man/8/createrepo)
- [apt-cacher-ng Documentation](https://www.unix-ag.uni-kl.de/~bloch/acng/)
- [yum-cron Documentation](https://linux.die.net/man/8/yum-cron)
