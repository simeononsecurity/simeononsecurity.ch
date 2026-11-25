---
title: "Linux 系统加固的应做与不应做事项"
date: 2023-02-28
lastmod: 2026-11-25
toc: true
draft: false
description: "Linux 加固指南，涵盖更新、防火墙、SELinux 或 AppArmor、密码策略和日志监控。"
tags: ["Linux 安全", "系统加固", "防火墙", "SELinux", "AppArmor", "密码策略", "系统更新", "系统日志", "安全模块", "访问控制策略", "网络安全", "系统安全", "网络安全防护", "漏洞管理", "安全最佳实践", "IT 安全", "信息安全", "软件更新", "root 访问", "密码管理器"]
cover: "/img/cover/A_cartoon_lock_holding_a_shield_with_the_word_Linux_on_it.webp"
coverAlt: "一个卡通锁拿着写有 Linux 的盾牌，一支箭从盾牌上弹开。"
coverCaption: ""
---


Linux 是个人和企业广泛使用的操作系统。由于采用开源模式，人们常认为它比其他操作系统更安全，但仍需妥善加固系统，保护系统和其中的数据。本文介绍一些通用的 Linux 加固建议，帮助你保护系统安全。

## 应做事项：

### 保持系统更新

及时更新 [Linux 系统](https://simeononsecurity.com/articles/how-do-i-learn-linux/) 对维护安全至关重要。定期更新有助于修复安全漏洞和错误，降低系统遭受攻击的风险。下面是使用 **apt-get** 或 **yum** 包管理器更新 Linux 系统的示例：

#### 使用 apt-get 更新 Ubuntu

使用 **apt-get** 更新 Ubuntu 时，打开终端并输入：
```bash
sudo apt-get update
```

此命令会从 Ubuntu 软件包仓库下载最新的软件包列表。命令完成后，可运行以下命令安装可用更新：

```bash
sudo apt-get upgrade

```

此命令会下载并安装系统的可用更新。

### 使用 yum 更新 CentOS

使用 **yum** 更新 CentOS 时，打开终端并输入：

```bash
sudo yum update
```

此命令会下载并安装系统的可用更新。你也可以使用以下命令清理过时或未使用的软件包：

```bash
sudo yum autoremove
```

此命令会删除系统不再需要的软件包。

请定期检查并安装 Linux 系统更新，以维护系统安全与稳定。


### 使用防火墙

防火墙是保护 Linux 系统的重要安全措施，有助于防止未经授权的访问和其他网络威胁。下面介绍如何使用 **ufw** 防火墙：

#### 在基于 Ubuntu 的系统上安装并启用 ufw

要安装并启用 **ufw**，请打开终端并输入：

```bash
sudo apt install ufw -y
sudo ufw allow ssh
sudo ufw enable
```

要允许传入的 HTTP 流量（端口 80）：

```bash
sudo ufw allow http
```

要阻止来自特定 IP 地址的传入流量：

```bash
sudo ufw deny from <ip_address>
```

要删除规则：
```bash
sudo ufw delete <rule_number>
```

输入以下命令可查看当前的 **ufw** 规则：

```bash
sudo ufw status
```


此命令会显示当前规则及其状态。

请定期检查并更新 **ufw** 规则，确保系统能够抵御潜在威胁。


#### 在基于 CentOS 的系统上安装并启用 firewalld

要安装并启用 CentOS 默认防火墙 **firewalld**，请运行以下命令：

```bash
sudo yum install firewalld
sudo systemctl enable firewalld
sudo systemctl start firewalld
```

这些命令会安装 **firewalld** 并在系统上启用它。

#### 在基于 CentOS 的系统上配置 firewalld 规则

启用 **firewalld** 后，可以配置规则来允许或阻止传入和传出的流量。以下是一些示例：

要允许传入的 SSH 流量（端口 22）：

```bash
sudo firewall-cmd --permanent --add-service=ssh
sudo firewall-cmd --reload
```

要允许传入的 HTTP 流量（端口 80）：

```bash
sudo firewall-cmd --permanent --add-service=http
sudo firewall-cmd --reload
```

要阻止来自特定 IP 地址的传入流量：

```bash
sudo firewall-cmd --permanent --add-rich-rule='rule family="ipv4" source address="<ip_address>" reject'
sudo firewall-cmd --reload
```

要删除规则：

```bash
sudo firewall-cmd --permanent --remove-<type>=<rule>
sudo firewall-cmd --reload
```

输入以下命令可查看当前的 **firewalld** 规则：

```bash
sudo firewall-cmd --list-all
```

此命令会显示当前规则及其状态。

请定期检查并更新 **firewalld** 规则，确保系统能够抵御潜在威胁。

### 启用 SELinux 或 AppArmor

SELinux（Security-Enhanced Linux）和 AppArmor 是可在 Linux 系统中实施强制访问控制策略的安全模块。大多数现代 Linux 发行版默认安装 SELinux 或 AppArmor。启用并配置它们有助于提高系统安全性。

#### 在基于 CentOS 的系统上启用 SELinux

运行以下命令，检查 SELinux 是否已启用：

```bash
sestatus
```

如果尚未安装 SELinux，可运行以下命令安装：

```bash
sudo yum install selinux-policy selinux-policy-targeted
```

要启用 SELinux，请编辑 **/etc/selinux/config** 文件，并将 **SELINUX** 变量设为 **enforcing**：

```bash
sudo nano /etc/selinux/config
```
**将 SELINUX 变量设为 enforcing**
```
SELINUX=enforcing
```

保存并退出文件，按 CTRL+X、Y 和 Enter，然后重启系统。

#### 在基于 Ubuntu 的系统上启用 AppArmor

运行以下命令，检查 AppArmor 是否已启用：
```bash
sudo apparmor_status
```


如果尚未安装 AppArmor，可运行以下命令安装：
```bash
sudo apt-get install apparmor
```

要启用 AppArmor，请编辑 **/etc/default/grub** 文件，并将 **security=apparmor** 参数添加到 **GRUB_CMDLINE_LINUX** 变量：

```bash
sudo nano /etc/default/grub
```
**添加 security=apparmor**
```bash
GRUB_CMDLINE_LINUX="... security=apparmor"
```

保存并退出文件，按 CTRL+X、Y 和 Enter，然后运行以下命令更新系统的引导加载程序配置：

```bash
sudo update-grub
```

最后，重启系统。

启用 SELinux 或 AppArmor 后，可以配置策略来限制进程的权限及其对系统资源的访问。这有助于减轻成功攻击造成的影响，并提高系统整体安全性。


### 配置密码策略

配置密码策略是加固 Linux 系统安全的重要步骤。强制执行严格的密码要求有助于保护用户账户，防止潜在攻击。以下介绍如何在 Linux 系统上配置密码策略：

#### 在 Ubuntu 上配置密码策略

在 Ubuntu 上，可以使用 **pam_pwquality** 模块配置密码策略。此模块提供一系列密码强度检查，可用于执行密码要求。要安装 **pam_pwquality** 模块，请打开终端并输入：

```bash
sudo apt-get install libpam-pwquality
```

安装模块后，编辑 **/etc/pam.d/common-password** 文件以配置其设置。例如，要要求密码至少包含 8 个字符，并至少有一个大写字母、一个小写字母、一个数字和一个特殊字符，可在文件中添加以下行：

```bash
password requisite pam_pwquality.so minlen=8 ucredit=-1 lcredit=-1 dcredit=-1 ocredit=-1
```

也可通过向文件添加配置项来设置其他要求，例如密码最长使用期限。

#### 在 CentOS 上配置密码策略

在 CentOS 上，可以使用 **authconfig** 工具配置密码策略。该工具提供了多种配置选项。例如，要要求密码至少包含 8 个字符，并至少有一个大写字母、一个小写字母、一个数字和一个特殊字符，可运行：

```bash
sudo authconfig --passalgo=sha512 --update --enablereqlower --enablerequpper --enablereqdigit --enablereqother --passminlen=8
```

此命令会更新系统的 **/etc/pam.d/system-auth** 和 **/etc/pam.d/password-auth** 文件，以执行指定的密码策略。

请定期检查并更新密码策略，确保其能够持续抵御潜在攻击。


### 监控系统日志

监控系统日志是维护 Linux 系统安全的重要环节。系统日志会记录系统活动，例如登录失败、错误和其他重要事件，可帮助你发现潜在的安全威胁或需要处理的问题。以下介绍如何监控系统日志：

#### 使用 journalctl 命令

大多数现代 Linux 发行版都可以使用 **journalctl** 命令查看系统日志。该命令提供多种选项，可用于筛选和搜索日志记录。

要查看所有日志记录，请运行：

```bash
sudo journalctl
```

此命令会显示所有日志记录，最新的记录位于底部。

要按特定单元（例如服务或进程）筛选日志记录，可使用 **-u** 选项，后接单元名称。例如，要查看 **sshd** 服务的日志记录，请运行：
```bash
sudo journalctl -u sshd
```


要按时间范围筛选日志记录，可使用 **--since** 和 **--until** 选项，后接时间戳或时间范围。例如，要查看过去一小时的日志记录，请运行：

```bash
sudo journalctl --since "1 hour ago"
```

#### 使用日志管理工具

对于较大或更复杂的系统，可以使用日志管理工具收集并分析系统日志。这类工具提供实时日志监控、日志聚合和日志分析等高级功能，帮助你更高效地发现并应对潜在安全威胁。

Linux 日志管理工具示例：

- **Logwatch**：简单的日志分析工具，每天通过电子邮件发送系统日志摘要
- **Logrotate**：自动轮换并压缩日志文件，以节省磁盘空间
- **ELK 技术栈**：常见的开源日志管理方案，由 Elasticsearch、Logstash 和 Kibana 组成，提供实时日志监控与分析能力

请定期检查和分析系统日志，及时发现并应对潜在安全威胁。

______

## 不应做的事项：

### 不要使用弱密码

使用弱密码是常见错误，可能使 Linux 系统容易遭受攻击。攻击者可以利用工具猜测基于常见词语、姓名或日期的密码。请使用难以猜测且彼此不同的强密码。

你可以组合大小写字母、数字和特殊字符来创建强密码。使用[密码管理器](https://simeononsecurity.com/articles/bitwarden-and-keepassxc-vs-the-rest/)生成并安全保存复杂密码也是良好做法。[密码管理器](https://simeononsecurity.com/articles/bitwarden-and-keepassxc-vs-the-rest/)还能帮你记住密码，并避免多个账户重复使用同一个密码。

### 不要允许 root 通过 SSH 登录

允许 root 通过 SSH 登录存在安全风险，攻击者可能借此完全控制 Linux 系统。请改用非 root 用户账户登录，再通过 **sudo** 命令提升所需权限。限制用户账户权限有助于减轻攻击造成的潜在影响。

### 不要安装不必要的软件

安装不必要的软件会扩大 Linux 系统的攻击面，使其更容易受到攻击。只安装系统所需的软件，并删除不需要的软件。这样有助于减少潜在漏洞数量，降低攻击成功的风险。

### 不要使用过时的软件

使用过时的软件会使系统容易受到利用已知漏洞的攻击。请使用软件的最新版本并定期更新，以修复已知漏洞并保护系统免受潜在攻击。

______

## 结论

加固 Linux 系统对于保护系统及其中的数据至关重要。按照本文的建议操作，有助于保护系统并降低网络威胁风险。请保持系统更新、使用防火墙、配置密码策略并监控系统日志。避免使用弱密码、关闭自动更新、允许 root 通过 SSH 登录、安装不必要的软件以及使用过时的软件。遵循这些最佳实践，有助于保持 Linux 系统的安全。

## 参考资料：

- [The Center for Internet Security's Linux Hardening Guide](https://www.cisecurity.org/cis-hardened-images/)
- [Red Hat Enterprise Linux Security Guide](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/security_guide/index)
- [Ubuntu Security Documentation](https://ubuntu.com/security)
- [Linux Security Wiki](https://en.wikibooks.org/wiki/Linux_Security)
