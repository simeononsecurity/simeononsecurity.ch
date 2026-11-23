---
title: "Proxmox VE 8 升级到 9 指南"
date: 2026-07-22
lastmod: 2026-11-23
toc: true
draft: false
description: "通过前置检查、手动步骤和自动化，将 Proxmox VE 8 升级到 9，并了解不兼容变更与恢复方法。"
genre: ["虚拟化", "Linux 管理", "Proxmox", "服务器管理", "开源软件", "家庭实验室"]
tags: ["Proxmox VE 9", "Proxmox 升级", "PVE 8 升级到 9", "Debian Trixie", "Debian 13", "apt dist-upgrade", "pve8to9", "Proxmox Ceph", "proxmox-boot-tool", "grub-efi", "LVM 升级", "ZFS 升级", "NVIDIA vGPU", "cgroupv2", "Proxmox 自动化", "Bash 升级脚本", "Proxmox 集群升级", "原地升级", "pve8to9-upgrade.sh", "Proxmox VE 9.0"]
cover: "/img/cover/proxmox-ve-8-to-9-upgrade-guide-automation.webp"
coverAlt: "现代服务器机房的屏幕显示代表虚拟机的发光图标。一位技术人员在深蓝色设备间使用笔记本电脑，周围点缀蓝色、绿色和紫色灯光。"
coverCaption: "Proxmox VE 8 升级到 9：使用自动化助手脚本进行原地升级的分步指南。"
canonical: "https://simeononsecurity.com/articles/proxmox-ve-8-to-9-upgrade-guide/"
---

**Proxmox VE 9.0 基于 Debian 13 Trixie 发布，采用内核 6.14、QEMU 10、LXC 6 和 ZFS 2.3。** 本指南介绍手动原地升级流程和自动化 Bash 脚本。脚本会检测配置并处理仓库变更、已知问题和升级前检查。

## Proxmox VE 9 有哪些新内容

Proxmox VE 9 于 2025 年 8 月发布，是一个主要版本升级。主要变化：

| 组件 | PVE 8 | PVE 9.0 |
|-----------|--------|--------|
| **Debian 基础版本** | Bookworm (12) | Trixie (13) |
| **默认内核** | 6.8 | 6.14 |
| **QEMU** | 9.x | 10.x |
| **LXC** | 5.x | 6.x |
| **ZFS** | 2.2 | 2.3 |
| **Ceph** | Quincy / Reef / Squid | Squid (19.2) |
| **cgroup** | cgroupv2（仍可使用 v1） | 仅 cgroupv2 |

[Proxmox VE 9.2](https://forum.proxmox.com/threads/proxmox-virtual-environment-9-2-available.183742/) 默认提供内核 7.0、QEMU 11、LXC 7 和 ZFS 2.4。Ceph Tentacle 是 9.2 默认版本，Squid 仍可用。在升级 VE 8 Ceph 集群前迁移到 Squid 是单独的前置要求。

**PVE 9.0 及更高版本的主要新功能：**
- 通过卷链在厚置备 LVM 上创建 VM 快照（技术预览，9.1 起可用于生产环境）
- 使用高可用性亲和性规则取代 HA 组
- 使用 OpenFabric 和 OSPF 全网格 Ceph 网络的 SDN Fabrics
- 全新的移动端 Web 界面（Rust/Yew）
- 无需停机即可扩展 ZFS RAIDZ 设备
- 使用集群资源调度器动态平衡负载（PVE 9.2）
- 将 WireGuard 和 BGP 用作 SDN 网络协议（PVE 9.2）
- `/tmp` 现在是 `tmpfs`（Debian Trixie 变更，系统定期清理文件）

{{< figure src="proxmox-ve-8-to-9-component-changes.webp" alt="Proxmox VE 8 与 VE 9 的并排对比图，显示内核、QEMU、LXC、ZFS 和 Ceph 的组件版本变化" >}}

______

## 开始之前：前置要求

**修改软件仓库前，必须满足以下所有要求。** 请查看[官方升级 Wiki 的前置要求清单](https://pve.proxmox.com/wiki/Upgrade_from_8_to_9#Prerequisites)。

### 1. 至少使用 Proxmox VE 8.4

```bash
pveversion
```

输出必须包含 `pve-manager/8.4.x` 或更高版本。否则运行：

```bash
apt update && apt dist-upgrade
```

### 2. Ceph 必须为 Squid (19.x)，仅适用于超融合环境

```bash
ceph --version
```

输出必须显示 19.x (Squid)。如果使用 Reef (18.x) 或 Quincy (17.x)，先升级 Ceph。升级路径必须逐个主版本前进：

- Quincy (17) → Reef (18) → Squid (19)

*所有 Ceph 节点都运行 Squid 后，才能开始升级 PVE 9。*

### 3. 同一节点安装了 Proxmox Backup Server

如果 PBS 3.4 与 PVE 8.4 共用一个节点，请遵循[共存安装说明](https://pbs.proxmox.com/wiki/Upgrade_from_3_to_4#Installed_alongside_Proxmox_VE)，并在一次 APT 操作中协调两项升级。确认备份可恢复，并在更改仓库前运行 `pve8to9 --full` 和 `pbs3to4 --full`。先解决报告的问题。

### 4. 访问要求

- **优先选择**：通过 IPMI、iKVM 或实体键盘访问控制台。服务重启时 SSH 会断开。
- **SSH**：使用 `tmux` 或 `screen`，这样即使连接中断，升级仍会继续：
  ```bash
  tmux new -s upgrade
  ```

### 5. 磁盘空间

```bash
df -h /
```

至少预留 **5 GB**，最好有 10 GB 以上。

### 6. 有效备份

升级前将所有 VM 和容器备份到外部存储并测试恢复。有效备份是必需条件。

______

## 必须了解的不兼容变更

升级前阅读以下内容，其中一些要求在升级前或之后采取行动。

### cgroup V1 已移除

PVE 9 完全不支持旧版 cgroupv1。如果你以前启用过：

```bash
grep -E 'cgroup_no_v1|systemd.unified_cgroup_hierarchy=0' /proc/cmdline
```

如果命令返回任何内容，请在升级前从 `/etc/default/grub` 移除内核参数并运行 `update-grub`。

**对容器的影响**：运行 systemd 230 或更早版本的容器（CentOS 7、Ubuntu 16.04）无法在 PVE 9 启动。升级前迁移这些工作负载。Proxmox VE 8.4 的供应商支持已于 2026 年 8 月结束。

### HA 组已弃用

HA 规则取代 HA 组。所有集群节点升级到 PVE 9 后会自动迁移。无需手动操作，但最后一个节点升级后要检查结果。

### VM.Monitor 权限已移除

引用 `VM.Monitor` 的自定义角色需要更新。基本 KVM 监视器访问权限改用 `Sys.Audit`。`pve8to9` 会检测受影响的角色。

### 新权限：VM.Replicate

创建或编辑存储复制任务现在需要在 `/vms/<vmid>` 上拥有 `VM.Replicate`。按需调整自定义角色。

### 特权 LXC 容器需要 Sys.Modify

创建新的特权容器现在需要 `Sys.Modify`。原地恢复现有特权容器不需要此权限。

### systemd-sysctl 不再读取 /etc/sysctl.conf

升级后，`/etc/sysctl.conf` 中的自定义设置会被静默忽略。重启前将其迁移到 `/etc/sysctl.d/<NN>-name.conf`。

```bash
# 检查 sysctl.conf 中的内容
grep -v '^\s*#\|\s*$' /etc/sysctl.conf
```

### /tmp 现在是 tmpfs

Debian Trixie 将 `/tmp` 挂载为 tmpfs（最多使用 50% 的 RAM）。系统运行期间会定期清理文件。大型临时文件应移到 `/var/tmp` 或专用挂载点。

### Veeam 备份与恢复兼容性 {#veeam-backup-broken-for-qemu-machine-version--100}

升级前请检查 [Veeam Backup & Replication 和 Proxmox 插件版本](https://helpcenter.veeam.com/docs/vbr/userguide/pve_system_requirements.html)。当前要求列出在官方 Proxmox ISO 安装的 x86-64 主机上支持 Proxmox VE 8.2 至 9.2。旧版 Veeam 有自己的支持范围。

当前 [Veeam 限制](https://helpcenter.veeam.com/docs/vbr/userguide/pve_limitations.html)允许在启用 Snapshots as Volume Chains (SAVC) 的 LVM 存储上备份 VM。这并不意味着 SAVC 可用作 Veeam 辅助进程文件位置或 Instant Recovery 目标。单独的[恢复问题 KB4773](https://www.veeam.com/kb4773)影响 PVE 9 上恢复到 SAVC 存储的、使用旧于 QEMU 10 机器类型且带 QCOW2 磁盘的 VM。使用不带 SAVC 的目标，或按文档将磁盘恢复为 RAW。这是恢复解决方案，不是让整个机群固定机器类型的理由。升级前在目标存储测试备份和恢复。

### 网络接口名称可能变化

内核 6.14 识别的 NIC 功能多于 6.8，某些 NIC 会有额外名称后缀。升级前可用 `pve-network-interface-pinning` 将所有接口固定为稳定的 `nicX` 名称：

```bash
pve-network-interface-pinning --help
```

______

## 选项 A：手动原地升级

遵循 [pve.proxmox.com/wiki/Upgrade_from_8_to_9](https://pve.proxmox.com/wiki/Upgrade_from_8_to_9) 上的官方步骤。

### 步骤 1：运行 pve8to9 检查清单

```bash
pve8to9 --full
```

继续前解决所有 `FAIL` 项。每次修复后重新运行。

### 步骤 2：迁移正在运行的 VM（如果在集群中）

```bash
qm migrate <vmid> <target-node>
pct migrate <ctid> <target-node>
```

### 步骤 3：完整更新 PVE 8

```bash
apt update && apt dist-upgrade
pveversion   # 必须显示 8.4.1 或更高版本
```

### 步骤 4：更新 Debian 基础仓库

```bash
sed -i 's/bookworm/trixie/g' /etc/apt/sources.list
sed -i 's/bookworm/trixie/g' /etc/apt/sources.list.d/pve-enterprise.list
```

注释或删除所有剩余的 Bookworm 专用仓库行。

### 步骤 5：添加 PVE 9 软件包仓库

**Enterprise（需要订阅）：**

```bash
cat > /etc/apt/sources.list.d/pve-enterprise.sources << EOF
Types: deb
URIs: https://enterprise.proxmox.com/debian/pve
Suites: trixie
Components: pve-enterprise
Signed-By: /usr/share/keyrings/proxmox-archive-keyring.gpg
EOF
```

**无需订阅：**

```bash
cat > /etc/apt/sources.list.d/proxmox.sources << EOF
Types: deb
URIs: http://download.proxmox.com/debian/pve
Suites: trixie
Components: pve-no-subscription
Signed-By: /usr/share/keyrings/proxmox-archive-keyring.gpg
EOF
```

运行 `apt update && apt policy`，确认新仓库正常显示且没有错误。然后删除或注释旧的 `.list` 文件。

### 步骤 6：更新 Ceph 仓库（仅适用于超融合环境）

```bash
cat > /etc/apt/sources.list.d/ceph.sources << EOF
Types: deb
URIs: https://enterprise.proxmox.com/debian/ceph-squid
Suites: trixie
Components: enterprise
Signed-By: /usr/share/keyrings/proxmox-archive-keyring.gpg
EOF
```

无订阅环境使用 `http://download.proxmox.com/debian/ceph-squid` 和 `pve-no-subscription`。

### 步骤 7：刷新软件包索引

```bash
apt update
```

确认没有错误。

### 步骤 8：运行 dist-upgrade

```bash
apt dist-upgrade
```

根据存储速度，过程需要 5 到 60 分钟以上。升级时：

- **`/etc/issue`**：保留当前版本（安全）
- **`/etc/lvm/lvm.conf`**：安装维护者版本（推荐）
- **`/etc/ssh/sshd_config`**：如果未自定义，则安装维护者版本
- **`/etc/default/grub`**：如果已自定义，则保留当前版本
- **`/etc/chrony/chrony.conf`**：如果未自定义，则安装维护者版本

### 步骤 9：重启

```bash
reboot
```

即使内核 6.14 已作为 PVE 8 的可选版本安装，也必须重启，因为内核会使用 PVE 9 工具链重新构建。

### 步骤 10：升级后操作

```bash
# 清除浏览器缓存：Ctrl+Shift+R（macOS 上为 ⌘+Alt+R）
# 检查集群中的所有节点：
pvesh get /nodes

# 所有节点升级到 PVE 9 后，HA 组会自动迁移为 HA 规则
journalctl -eu pve-ha-crm  # 检查错误
```

______

## 选项 B：自动化脚本 (pve8to9-upgrade.sh)

手动流程包含许多因配置而异的条件步骤。`pve8to9-upgrade.sh` 会自动处理这些步骤。

**脚本来源：** [gist.github.com/simeononsecurity/ba3831f487c4e960f9e218c7da5c4b8d](https://gist.github.com/simeononsecurity/ba3831f487c4e960f9e218c7da5c4b8d)

### 脚本会做什么

脚本会自动处理完整升级，包括：

| 检测项 | 操作 |
|-----------|--------|
| Enterprise 或无订阅仓库 | 使用**当前已启用**的仓库类型，不会在无订阅节点启用 Enterprise |
| Ceph 版本 | 如果是 Quincy 或 Reef 则阻止升级，并显示 Ceph 分步升级指南 |
| Ceph 仓库类型 | 写入与现有仓库类型匹配的新 `ceph.sources` |
| NVIDIA vGPU 驱动 | 如果驱动低于 570.158.02（GRID 18.3 最低版本）则阻止 |
| NVIDIA GPU 直通 | 发出警告并生成升级后的测试提醒 |
| CUDA 仓库 | 将 URI 路径中的 `debian12` 更新为 `debian13` |
| systemd-boot 元软件包 | 移除该包（修复会中止 dist-upgrade 的 Debian 错误 #1110177） |
| `sysctl.conf` 自定义设置 | 迁移到 `/etc/sysctl.d/99-pve8to9-migrated.conf` |
| FRR post-up 死锁 | 重启前修复 `/etc/network/interfaces` |
| `systemd-journald-audit.socket` | 禁用以防升级期间日志泛滥 |
| UEFI + LVM 的 GRUB 问题 | 安装 `grub-efi-amd64` 并在 `/root/` 写入速查表 |
| 第三方 `bookworm` 仓库 | 注释仓库并提醒你更新 |
| `linux-image-amd64` 冲突 | 如果存在则移除 |
| LVM 自动激活 | 升级前后均运行迁移脚本 |
| Proxmox 备份服务器 | 运行 `pbs3to4 --full` 检查并更新 PBS 的 Trixie 仓库 |
| ZFS 根文件系统 | 检测并确认（无需特殊操作） |

所有变更都会记录到 `/var/log/pve8to9-upgrade-<timestamp>.log`。APT 仓库备份保存在 `/root/pve8to9-apt-backups/`，绝不会作为 `.bak` 文件放在 `/etc/apt/sources.list.d/` 中，否则 Web 界面会报“invalid extension”（扩展名无效）错误。

### 安装和使用

```bash
# 下载脚本
curl -fsSL https://gist.githubusercontent.com/simeononsecurity/ba3831f487c4e960f9e218c7da5c4b8d/raw/pve8to9-upgrade.sh \
  -o pve8to9-upgrade.sh

# 添加执行权限
chmod +x pve8to9-upgrade.sh

# 运行前先审查脚本（以 root 身份执行前务必阅读脚本）
less pve8to9-upgrade.sh
```

**运行模式：**

```bash
# 完整交互模式（推荐）
./pve8to9-upgrade.sh

# 自动批准所有安全且非破坏性的修复
./pve8to9-upgrade.sh --yes

# 试运行：显示所有变更但不应用
./pve8to9-upgrade.sh --dry-run

# 跳过 pve8to9 --full 前置检查（不推荐）
./pve8to9-upgrade.sh --skip-preflight
```

*通过 SSH 连接时，请在 `tmux` 或 `screen` 中运行。*

### 脚本输出示例

脚本会先显示配置摘要，再询问你是否继续：

```
══════════════════════════════════════════
  检测到的配置摘要
══════════════════════════════════════════

  PVE version      : pve-manager/8.4.3/...
  Debian           : bookworm
  Subscription     : true (status: Active)
  PVE repo type    : enterprise  (enterprise was active: true)
  Ceph             : YES (v19.2.3, enterprise repos)
  ZFS root         : false
  UEFI boot        : true
  LVM root         : true
  NVIDIA           : NO
  CUDA repos       : NO
  systemd-boot     : meta=true efi=true
  sysctl.conf      : custom=false (0 lines)
  cgroupv1         : false (must be false for PVE 9)
  FRR post-up      : false (broken pattern)
  LVM autoact.     : false
  PBS co-install   : NO
  3rd-party bookwm : none
```

### 脚本的阻断性安全检查

出现以下任一情况时，脚本会**拒绝继续**：

- 内核命令行中显式启用了 cgroup V1
- Ceph 仍是 Quincy (17.x) 或 Reef (18.x)，脚本会显示准确的 Ceph 升级命令
- NVIDIA vGPU 驱动低于 570 (GRID 18.3)
- PVE 版本低于 8.4

对于每个阻断问题，脚本都会列出解决后重新运行所需的准确命令。

______

## 已知升级问题

### GRUB 无法从 UEFI 模式的 LVM 启动

**受影响对象**：从 PVE 7.x 升级、以 LVM 为根并使用 UEFI 启动的系统

```bash
# 修复方法（升级后在运行中的系统上执行）：
[ -d /sys/firmware/efi ] && apt install grub-efi-amd64
```

`pve8to9-upgrade.sh` 会检测 UEFI+LVM 并自动安装该包，也会在 `/root/` 写入恢复速查表 `/root/GRUB-RECOVERY-CHEATSHEET.txt`。

**如果节点已停在** `grub rescue>` 或显示“disk 'lvmid/...' not found”（找不到磁盘）：

1. 从 PVE ISO 启动 → Advanced → **Rescue Boot**
2. 或按官方 Wiki 的 [LVM 恢复 Grub 故障章节](https://pve.proxmox.com/wiki/Recover_From_Grub_Failure#Recovering_from_grub_.22disk_not_found.22_error_when_booting_from_LVM)操作

### systemd-boot 元软件包中止 dist-upgrade

所有 PVE 8.1–8.4 ISO 系统都会自动安装 `systemd-boot` 元软件包。在 Trixie 中，它含有其他软件包升级时运行的钩子；如果 ESP 未挂载，可能会中途停止 `dist-upgrade`（Debian 错误 #1110177）。

```bash
# 在 dist-upgrade 前移除该包：
apt remove systemd-boot
# 不要移除 systemd-boot-efi 或 systemd-boot-tools，它们需要保留
```

`pve8to9-upgrade.sh` 会自动处理此问题并说明原因。

### 内核 6.14 有时会导致 PCI 直通故障

一些用户报告带 PCI 直通的 VM 在内核 6.14 下无法启动。如果受影响：

```bash
# 暂时固定旧内核：
proxmox-boot-tool kernel pin 6.8.12-4-pve
```

### Ceph 全网格配置在重启时死锁

如果 `/etc/network/interfaces` 包含：

```
post-up /usr/bin/systemctl restart frr.service
```

请将其改为：

```
post-up /usr/bin/systemctl is-active --quiet frr.service && /usr/bin/systemctl restart frr.service || true
```

在**重启前**完成。脚本会自动检测并修复此模式。

### LVM thin pool 需要修复

升级后，部分系统可能显示：

```
Check of pool pve/data failed (status:64). Manual repair required!
```

修复：

```bash
lvconvert --repair pve/data
```

### NVIDIA vGPU 驱动最低版本

升级前驱动必须至少为 **570.158.02**（GRID 18.3）。旧版驱动与内核 6.x 不兼容。

```bash
nvidia-smi --query-gpu=driver_version --format=csv,noheader
```

______

## 集群升级顺序

每次升级一个节点。开始下一个节点前，确认当前节点运行正常。

```bash
# 每次升级节点前检查集群健康状况：
pvecm status
ceph -s   # 如果部署了 Ceph
```

**部分节点升级期间的迁移规则：**

- VM/CT 从 PVE 8 迁移到 PVE 9：始终可用
- VM/CT 从 PVE 9 迁移到 PVE 8：通常不受支持

所有节点升级到 PVE 9 后，HA 组会自动迁移为 HA 亲和性规则。检查错误：

```bash
journalctl -eu pve-ha-crm
```

______

## 故障排除

### 升级停止：系统提示将移除 `proxmox-ve`

如果看到：
```
W: (pve-apt-hook) You are attempting to remove the meta-package 'proxmox-ve'!
```

一个或多个软件包无法升级，通常是因为仍配置了 Bookworm 仓库。查找残留条目：

```bash
grep -r 'bookworm' /etc/apt/sources.list /etc/apt/sources.list.d/
```

注释这些条目，然后运行：

```bash
apt update && apt dist-upgrade
```

如果升级只完成了一部分：

```bash
apt -f install
```

### ZFS 升级后无法启动

如果使用 ZFS 根文件系统和旧式 BIOS 启动，请参阅[将旧式启动切换到 Proxmox Boot Tool 的 ZFS 指南](https://pve.proxmox.com/wiki/ZFS:_Switch_Legacy-Boot_to_Proxmox_Boot_Tool)。ZFS 系统必须由 `proxmox-boot-tool` 管理启动，而不能直接由 GRUB 管理，才能支持 ZFS 功能升级。

______

## 升级后检查清单

每个节点重启后：

- [ ] 清除浏览器缓存（`Ctrl+Shift+R` / `⌘+Alt+R`）
- [ ] `pveversion` 显示 9.x
- [ ] `uname -r` 显示 6.14.x 或更高版本
- [ ] 所有 VM 和 CT 均可正常启动
- [ ] Ceph 健康状态：`ceph -s` 显示 HEALTH_OK
- [ ] 如果使用 UEFI+LVM：确认 `grubx64.efi` 的修改时间较新
- [ ] 如果使用 NVIDIA 直通：测试一个非生产 VM
- [ ] 更新升级期间被注释掉的第三方仓库
- [ ] 将 `/etc/sysctl.conf` 的自定义设置迁移到 `/etc/sysctl.d/`

______

## 升级后验证

升级后检查软件仓库配置、集群仲裁、存储状态、客户机启动、备份、防火墙规则和管理访问。确认升级完成前检查系统日志。如果集群支持，请在另一台主机上测试客户机恢复。

针对特定版本命令，请参阅当前的 [Proxmox VE 管理指南](https://pve.proxmox.com/pve-docs/)和[发行说明](https://pve.proxmox.com/wiki/Roadmap)。不要复制旧版本命令而不检查目标版本和备份状态。

## 参考资料

1. [官方：Proxmox VE 8 升级到 9](https://pve.proxmox.com/wiki/Upgrade_from_8_to_9)
2. [官方：从 8 升级到 9 的前置要求](https://pve.proxmox.com/wiki/Upgrade_from_8_to_9#Prerequisites)
3. [pve8to9-upgrade.sh 自动化脚本](https://gist.github.com/simeononsecurity/ba3831f487c4e960f9e218c7da5c4b8d)
4. [Proxmox VE 9.0 已知问题 (Roadmap)](https://pve.proxmox.com/wiki/Roadmap#9.0-known-issues)
5. [从 GRUB 启动故障恢复，LVM 报错 “disk not found”（找不到磁盘）](https://pve.proxmox.com/wiki/Recover_From_Grub_Failure#Recovering_from_grub_.22disk_not_found.22_error_when_booting_from_LVM)
6. [ZFS：将旧式启动切换到 Proxmox Boot Tool](https://pve.proxmox.com/wiki/ZFS:_Switch_Legacy-Boot_to_Proxmox_Boot_Tool)
7. [Ceph Reef 升级到 Squid 指南](https://pve.proxmox.com/wiki/Ceph_Reef_to_Squid)
8. [Proxmox 网络接口固定工具](https://pve.proxmox.com/pve-docs/chapter-sysadmin.html)
9. [Debian 13 Trixie 发行说明](https://www.debian.org/releases/trixie/releasenotes)
