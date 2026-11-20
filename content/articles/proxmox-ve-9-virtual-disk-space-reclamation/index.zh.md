---
title: "Proxmox VE 9：减少虚拟磁盘占用并回收空间"
date: 2026-11-09
lastmod: 2026-11-20
toc: true
draft: false
description: "减少 Proxmox VE 9 VM 和 LXC 的存储占用。比较磁盘格式与存储后端，启用 discard，在 Windows 和 Linux 客户机中执行 trim，并在回收空间前检查快照。"
genre: ["虚拟化", "Linux 管理", "Proxmox VE 平台", "存储", "家庭实验室"]
tags: ["Proxmox VE 9 磁盘空间", "Proxmox 精简配置", "Proxmox discard 通知", "Proxmox TRIM 命令", "Proxmox Windows 客户机的 ReTrim", "Proxmox Linux 客户机的 fstrim", "Proxmox LXC 磁盘占用", "Proxmox LVM 精简配置", "Proxmox ZFS 稀疏 zvol", "Proxmox Ceph RBD 块设备", "Proxmox qcow2 格式", "Proxmox raw 磁盘", "Proxmox 快照", "虚拟磁盘空间回收", "Proxmox 存储类型", "VirtIO SCSI 控制器", "Proxmox 零写入检测", "Proxmox 备份存储"]
cover: "/img/cover/proxmox-ve-9-virtual-disk-space-reclamation.webp"
coverAlt: "两个方块网格由箭头连接，分别表示已使用的虚拟磁盘块和存储池中的可用容量。"
coverCaption: "在客户机中删除文件、发送 discard 和回收存储空间是不同的步骤。"
---

**客户机文件系统变小，并不代表 Proxmox 存储占用或费用一定下降。** 要释放主机空间，磁盘必须支持精简配置，VM 必须有可用的 discard 路径，后端存储也不能有快照保留的块。本指南介绍 Proxmox VE 9 VM 和 LXC 容器的设置与检查方法。

<!--more-->

## 要点

- **先选择后端存储。** 只有磁盘映像格式或存储后端支持精简配置时，虚拟磁盘的标称大小才会不同于主机实际分配的空间。
- **启用 VM discard，然后在客户机中执行 trim。** Windows ReTrim 和 Linux `fstrim` 会通过虚拟磁盘发送未使用块请求。
- **分别检查快照和备份。** 只要快照仍引用旧块，这些块就会继续占用空间。备份文件和 PBS 数据块有各自的保留规则。
- **按类型处理 LXC 挂载。** 受 Proxmox 管理的 rootfs 和挂载点卷、bind 挂载及设备挂载在归属和备份行为上各不相同。

## 开始之前

你需要 **Proxmox VE 9 管理员访问权限**、每个受影响客户机的已验证备份，以及足够的操作可用池空间。更改设置前，记录每个客户机的 ID、磁盘总线、卷 ID、存储 ID、快照和当前分配量。使用 [VM 还原演练](/articles/proxmox-vm-backup-restore-drill/)测试恢复流程。

**预计时间：** 每台客户机 20 至 60 分钟，大型 trim 或清理任务还需额外时间。**难度：** 中级。先从一台低风险 VM 开始，比较操作前后的存储用量。

> **警告：** 精简池写满会导致客户机 I/O 错误，并可能损坏文件系统。没有监控池中的可用数据和元数据空间时，不要超额分配容量。[Proxmox 存储文档](https://github.com/proxmox/pve-docs/blob/master/pvesm.adoc)

## 沿分配链路逐层检查

**删除文件**、**discard** 和**回收空间**发生在不同层。客户机删除文件后，文件系统会将相应块标记为空闲。文件系统会对这些块发送 TRIM 或 UNMAP。只有在虚拟磁盘启用了 discard 时，QEMU 才会转发请求。如果映像格式和存储池支持，后端存储才会释放物理分配。[Proxmox VM 磁盘文档](https://github.com/proxmox/pve-docs/blob/master/qm.adoc)

| 层 | 检查内容 | 可用信息 |
|---|---|---|
| **客户机文件** | 文件系统可用空间 | Windows 卷属性或 Linux `df -h` |
| **虚拟磁盘** | 总线、discard、SSD 仿真、映像格式 | VM 的 **硬件** 标签页或 `qm config VMID` |
| **PVE 卷** | 所有者和配置大小 | 存储的 **内容** 标签页或 `pvesm list STORAGE_ID` |
| **存储池** | 可用数据空间、元数据和保留块 | `pvesm status` 及后端专用工具 |

**100 GiB 虚拟磁盘表示容量上限，并不保证已分配 100 GiB。** 反过来，客户机报告使用 20 GiB 也不能证明主机只使用了 20 GiB。元数据、快照、备份副本和以前写入的块都会改变数值。[Proxmox 存储文档](https://github.com/proxmox/pve-docs/blob/master/pvesm.adoc)

## 比较磁盘格式

**Proxmox 提供哪些映像格式取决于存储后端。** ZFS zvol 和 Ceph RBD 使用 raw 虚拟磁盘。LVM 通常使用 raw，以下介绍的 Proxmox VE 9 卷链例外除外。Directory 和 NFS 等文件后端支持 raw 或 qcow2。raw 本身不提供精简分配或快照，这些功能必须由底层存储提供。qcow2 在映像层提供写时复制分配和快照。[Proxmox VM 磁盘文档](https://github.com/proxmox/pve-docs/blob/master/qm.adoc)

| 格式 | 分配机制 | 空间权衡 |
|---|---|---|
| **文件存储上的 qcow2** | qcow2 随写入分配数据簇 | 映像元数据和快照链会占用空间 |
| **文件存储上的 raw 文件** | 在支持时使用文件系统稀疏文件行为 | raw 本身不提供精简配置或快照 |
| **raw 块卷** | LVM 精简配置、ZFS、Ceph RBD 或其他后端存储 | 池的分配和快照取决于后端 |

**Proxmox VE 9 的厚置备 LVM 提供了一种特殊快照模式。** `snapshot-as-volume-chain` 会在厚置备 LVM 逻辑卷之间使用 qcow2 后备关系，不使用 qcow2 内部快照。该选项只影响新建 VM 磁盘，当前 Proxmox 文档将其列为技术预览。PVE 会将每个快照显示为已分配完整容量。只有底层存储支持精简配置和 discard 时，SAN 的实际分配量才会更小。[Proxmox LVM 存储文档](https://github.com/proxmox/pve-docs/blob/master/pve-storage-lvm.adoc)

**不要仅因为扩展名是 `.raw` 就转换磁盘。** 先检查存储插件和已分配块。`local-lvm` 上的 raw 磁盘与普通 Directory 存储上完全分配的 raw 文件有不同的分配行为。

## 比较存储类型

Proxmox 将**文件存储**与**块存储**分开处理。存储插件还控制快照、克隆、共享，以及池接受哪些内容类型。依赖某种格式或功能前，先检查 **Datacenter > Storage** 中的存储条目。[Proxmox 存储类型表](https://github.com/proxmox/pve-docs/blob/master/pvesm.adoc)

| 存储 | VM 磁盘行为 | 空间回收检查 |
|---|---|---|
| **Directory、ext4、XFS** | raw 或 qcow2 文件 | 比较 `du` 显示的已分配字节与映像虚拟大小。若其他存储层提供快照，也要检查快照。 |
| **NFS、CIFS** | 共享存储上的 raw 或 qcow2 文件 | 检查服务器端的已分配空间。客户机 trim 的结果本身不能证明服务器空间减少。 |
| **LVM 精简配置 (`local-lvm`)** | 仅限本地的精简 raw 逻辑卷 | 使用 `lvs` 监控精简池的数据和元数据使用百分比。 |
| **厚置备 LVM** | raw LV 或 VE 9 qcow2 卷链 | 在客户机中删除文件不会减少固定 LV 预留。单独检查 SAN 的精简分配。 |
| **ZFS 存储 (`local-zfs`)** | raw zvol 或容器子卷 | 检查 `sparse`、数据集属性、池用量和快照。 |
| **Ceph RBD** | 共享存储上的精简 `raw RBD` 映像 | 检查 Ceph 池容量、映像用量、快照和 discard 行为。 |
| **Btrfs** | 使用 Btrfs 子卷存放 raw 映像的文件卷 | 将 PVE Btrfs 插件视为技术预览，并检查快照和文件系统用量。 |

**其他存储插件承担不同用途。** CephFS 提供共享文件存储。iSCSI 和 Fibre Channel 提供共享块设备，通常使用 LVM 将其分成 VM 卷。`ZFS over iSCSI` 使用远程 ZFS 块存储。Proxmox Backup Server (PBS) 存储的是备份，而不是活动 VM 磁盘。放置 `images`、`rootdir`、`backup` 或 `iso` 数据之前，检查每个存储启用的 **Content** 类型。[Proxmox 存储类型表](https://github.com/proxmox/pve-docs/blob/master/pvesm.adoc)

**文件存储分配标志在创建时很重要。** 存储级别的 `format` 默认值会在支持时选择 `raw`、`qcow2` 或 `vmdk`。raw 和 qcow2 文件的 `preallocation` 设置接受 `off`、`metadata`、`falloc` 或 `full`。默认值是 `metadata`，对 raw 会按 `off` 处理。`full` 会预先保留文件空间，从而失去初始占用小的优势。创建大磁盘前检查存储配置。存储级别的 `shared` 标志仅声明已经存在的共享访问，不会将本地存储变成共享存储。[Proxmox 通用存储属性](https://github.com/proxmox/pve-docs/blob/master/pvesm.adoc)

**ZFS 使用 `sparse` 设置创建精简 zvol。** 未启用 sparse zvol 时，创建卷会根据已配置的卷行为预留容量。更改现有环境前，先检查实际存储配置和池。[Proxmox ZFS 存储文档](https://github.com/proxmox/pve-docs/blob/master/pve-storage-zfspool.adoc)

**Directory 存储还需要额外检查。** qcow2 文件的逻辑长度不等于客户机可见的虚拟容量。`du -h` 报告映像文件已分配的文件系统块。`ls -lh` 显示映像文件的逻辑长度。对于已停止的 VM，`qemu-img info` 会报告虚拟容量和主机磁盘大小。在 NFS 上，最终容量判断应以服务器账目为准。[QEMU `qemu-img` 参考](https://www.qemu.org/docs/master/tools/qemu-img.html)

**NFS 还有另一个分配边界。** qcow2 文件内部重用空数据簇，与 NFS 服务器释放文件块是两回事。打孔需要客户端、协商的协议、服务器和服务器文件系统都提供支持。NFSv4.2 定义了 `DEALLOCATE`，但仅凭版本号无法证明服务器已归还空间。检查已协商的 NFS 挂载，并在服务器上测量分配量。[NFSv4.2 `DEALLOCATE` 规范](https://www.rfc-editor.org/rfc/rfc7862.html#section-6.2.2)

## 设置 VM 磁盘标志

在 Proxmox 界面中打开 **VM > Hardware > Hard Disk > Edit**。检查磁盘总线和高级选项。以下标志会影响分配，或决定某项优化是否有用。有关各总线的支持情况，请参阅[官方 `qm` 选项参考](https://github.com/proxmox/pve-docs/blob/master/generated/qm.conf.5-opts.adoc)。

| 总线 | 与空间有关的选择 |
|---|---|
| **IDE** | 用于旧版兼容。仅在客户机缺少较新驱动时使用。 |
| **SATA** | 支持广泛的模拟设备。依赖空间回收前，检查客户机 trim 和磁盘选项。 |
| **带 VirtIO SCSI 的 SCSI** | discard 和单盘设置的首选现代路径。Windows 需要 VirtIO 驱动。 |
| **VirtIO Block** | 半虚拟化磁盘。Linux 的 discard 通知 需要内核 5.0 或更高版本。不提供 SSD 仿真。 |

| 设置 | 作用 | 建议 |
|---|---|---|
| **启用 discard (`on`)** | 转发客户机 TRIM 或 UNMAP | 在支持的精简后端上进行客户机驱动的空间回收时必需。默认值 `ignore` 会阻止转发。 |
| **SSD 仿真 `ssd=1`** | 向客户机呈现 SSD 磁盘 | 某些客户机需要此标识才会发送 trim。此标志不会提高物理存储速度。VirtIO Block 不支持此标志。 |
| **零写入检测 `detect_zeroes=1`** | 检测并尝试优化零写入 | 可选的 I/O 优化。不能替代客户机 trim，也不保证回收空间。 |
| **总线：SCSI / VirtIO `SCSI single`** | 通过 VirtIO 控制器呈现 SCSI 磁盘 | 适用于现代 Windows 和 Linux 客户机。安装 Windows VirtIO 驱动。 |
| **总线：VirtIO Block** | 使用 VirtIO 块设备 | Linux 的 discard 通知 需要内核 5.0 或更高版本。不提供 SSD 仿真。 |
| **I/O 线程 `iothread=1`** | 将驱动器 I/O 分配给单独线程 | 与 VirtIO Block 或 VirtIO `SCSI single` 控制器上的 SCSI 配合使用。这是性能设置，不是空间回收开关。 |
| **缓存和 AIO** | 更改 I/O 缓冲和异步 I/O | 根据工作负载和后端行为调整。两项设置都不会缩小磁盘。 |
| **Backup `backup=0`** | 将磁盘排除在 VM 备份之外 | 缩小备份范围，并让该磁盘无法从 VM 备份中恢复。请记录单独的备份方式。 |
| **Replicate `replicate=0`** | 将磁盘排除在存储复制之外 | 减少复制数据，并从副本中排除该磁盘。 |

**其他驱动器选项用于描述行为，而非回收空间。** `format` 适用于在支持多种映像格式的后端上分配磁盘。`size` 是虚拟容量，不是已分配字节数。`ro=1` 会将磁盘设为只读。`snapshot=1` 会启用 QEMU 临时快照模式，VM 关闭时丢弃磁盘更改。它不是将磁盘纳入 Proxmox VM 快照的开关。不要将其用于持久数据。使用 `backup=0` 或 `replicate=0` 前，先检查恢复覆盖范围。[Proxmox VM 磁盘选项](https://github.com/proxmox/pve-docs/blob/master/generated/qm.conf.5-opts.adoc)

**不要将缩短的 `qm set --scsi0` 字符串粘贴到现有驱动器上。** 检查 **`qm config VMID`**，编辑时保留完整卷 ID 和已有选项。简写驱动器分配可能会丢掉其他单盘设置。每次更改后都在界面中确认保存的磁盘选项。

```bash
qm config 100
pvesm status
```

`100` 是 VM ID 示例。若要在控制器为 **VirtIO `SCSI single`** 且客户机已安装所需驱动的现有 VM 上添加**新建的**64 GiB SCSI 磁盘，下面的命令展示分配语法。请替换为自己的 VM ID 和存储 ID。

```bash
qm set 100 --scsi0 local-lvm:64,discard=on,ssd=1,iothread=1
```

**使用示例前，先检查 `scsi0` 是否已存在。** 此命令会更改该槽位。对于现有磁盘，如果通过图形界面更容易保留完整选项字符串，就使用图形界面。参阅 [Proxmox `qm` 命令参考](https://github.com/proxmox/pve-docs/blob/master/generated/qm.1-synopsis.adoc)。

## 清理客户机系统中的文件

**先清理客户机文件。** 检查 Windows 存储设置、临时文件、旧安装程序、应用缓存和回收站。使用数据库和容器运行时自己的界面进行清理。为了减少分配量而删除活动应用数据可能造成数据丢失。

**确认卷使用支持 discard 的虚拟磁盘后**，在 Windows VM 中打开管理员 PowerShell：

```powershell
fsutil behavior query DisableDeleteNotify
Optimize-Volume -DriveLetter C -ReTrim -Verbose
```

`DisableDeleteNotify = 0` 表示 Windows 已为报告的文件系统启用删除通知。**ReTrim** 会重新发送当前卷未使用区域的 trim 请求。命令成功只能确认客户机已发起操作，不能说明主机回收了多少字节。任务结束后检查主机。[Microsoft `Optimize-Volume` 参考](https://learn.microsoft.com/en-us/powershell/module/storage/optimize-volume?view=windowsserver2025-ps)和[Proxmox VM 磁盘文档](https://github.com/proxmox/pve-docs/blob/master/qm.adoc)

**不要把 QEMU 客户机代理与 TRIM 混为一谈。** 代理支持客户机控制和备份一致性功能。文件系统删除通知通过虚拟磁盘路径传递。仅安装代理并不会回收块。[Proxmox VM 客户机代理文档](https://github.com/proxmox/pve-docs/blob/master/qm.adoc)

## 标记文件系统的未用块

**执行 trim 前，检查块设备路径和文件系统。** 现代发行版通常会通过 `fstrim.timer` 定期执行 trim。先检查定时器状态，再删除客户机不需要的数据，然后 trim 已挂载的文件系统。

```bash
lsblk -D
systemctl status fstrim.timer
sudo fstrim -av
```

**`lsblk -D`** 会报告可见块设备的 discard 粒度和限制。**`fstrim -av`** 会 trim 支持此操作的已挂载文件系统，并报告已提交的范围。提交的字节数不等于返回到存储池的字节数。加密、LVM、RAID 和其他堆叠设备的每一层都需要支持 discard。[Red Hat 未使用块指南](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/8/html/managing_file_systems/discarding-unused-blocks_managing-file-systems)

使用定期 trim，或经过评估的在线 discard 策略。**不要在尚未检查存储路径时，把所有文件系统的连续 `discard` 当作替代方案。** 客户机 trim 完成后检查 PVE 卷和池。如果删除的数据库记录仍占用文件空间，也要检查数据库或服务自己的压缩策略。

## 单独检查容器存储

**LXC rootfs 没有模拟的 VM 磁盘总线。** 先运行 `pct config CTID` 并识别每个 `rootfs` 和 `mpN` 条目。Proxmox 区分存储管理的挂载、bind 挂载和设备挂载。仅凭容器内可见的路径，无法判断主机上哪个卷拥有这些块。[Proxmox 容器挂载点](https://github.com/proxmox/pve-docs/blob/master/pct.adoc)

```bash
pct config 101
pct exec 101 -- df -h
pvesm status
```

对于**受管理的 rootfs 或挂载点**，从容器或其应用中删除文件，然后在主机上检查后端卷和快照。**不要对 CT 运行 VM 的 `qm` discard 命令。** ZFS 子卷上的快照会保留已删除块。对于 Directory 和 thin-LVM 存储，要检查实际后端分配量，而不是 CT 配置大小。

清理后，如果后端存储支持 discard，**在 Proxmox 主机上运行 `pct fstrim`**。Proxmox 会 trim CT rootfs 和符合条件的受管理挂载点，但会跳过 bind 挂载和只读挂载点。使用 `--ignore-mountpoints` 只 trim rootfs。比较操作前后的后端存储用量。[Proxmox `pct fstrim` 参考](https://github.com/proxmox/pve-docs/blob/master/generated/pct.1-synopsis.adoc)

```bash
pct fstrim 101
pct fstrim 101 --ignore-mountpoints 1
```

这些命令以 CT ID `101` 展示了**不同的目标范围**。根据存储布局选择一种。即使 trim 成功，只要快照还保留旧块，释放的字节数也可能不相等。

**bind 挂载和设备挂载由 Proxmox 之外的机制管理。** 源数据仍位于主机或外部设备上。容器 `vzdump` 备份不包含这些内容。受存储管理的附加挂载点默认也会从备份中排除，除非其 `backup` 选项将其纳入。清理前检查该挂载点实际采用的备份策略。[Proxmox 备份文档](https://github.com/proxmox/pve-docs/blob/master/vzdump.adoc)

若在 LXC 中运行 Docker，执行 Docker 清理命令前，应在实际存储所有者处检查映像层、卷和日志。[LXC 中 Docker 可靠性指南](/articles/docker-in-lxc-proxmox-reliability/)介绍了挂载和备份边界。默认情况下，删除容器映像不会删除持久卷。

## 正确测量服务器用量

**清理前后记录相同的测量值。** 存储池可用空间是最终容量指标。卷级数据用于找到导致用量增长的客户机。

```bash
pvesm status
pvesm list local-lvm
qm config 100
pct config 101
```

**`pvesm list` 会列出受管理卷及其配置大小。** 它不会测量精简存储上已分配的字节数。对于 **Directory 存储**，检查确切挂载路径和一个已知映像文件。路径应根据 **Datacenter > Storage** 和 VM 配置替换。

```bash
df -hT /var/lib/vz
du -h /var/lib/vz/images/100/vm-100-disk-0.qcow2
ls -lh /var/lib/vz/images/100/vm-100-disk-0.qcow2
```

对于**已停止的 VM**，可在不修改文件的情况下比较映像虚拟容量和主机分配：

```bash
qemu-img info /var/lib/vz/images/100/vm-100-disk-0.qcow2
```

对于 **LVM 精简配置**，同时监控池数据和元数据：

```bash
lvs -a -o lv_name,vg_name,lv_size,data_percent,metadata_percent,segtype
```

对于 **ZFS**，区分数据集当前数据与快照保留的数据：

```bash
zpool list
zfs list -o name,used,available,referenced,usedbysnapshots -r POOL_OR_DATASET
zfs list -t snapshot -o name,used,referenced,written -r DATASET
```

**`usedbysnapshots`** 报告数据集中所有快照保留的块。由于快照共享块，不能将每个快照的 `used` 数值相加。只要仍有快照引用已删除文件的块，池用量就可能保持不变，直到这些快照按保留策略过期或被删除。[OpenZFS 快照与克隆](https://openzfs.github.io/openzfs-docs/Basic%20Concepts/Datasets/Snapshots%20and%20Clones.html)

对于 **Ceph RBD**，运行 Ceph 命令前先映射 Proxmox 卷 ID。**`qm config VMID`** 会显示 `STORAGE_ID:IMAGE`。在 **Datacenter > Storage** 的 RBD 条目中查找**池**和可选的**命名空间**。存储 ID 不一定与池名称相同。根据池和映像值构建 `POOL/IMAGE`。在已配置为连接目标 Ceph 集群且凭据有效的客户端上运行这些命令。[Proxmox RBD 存储文档](https://github.com/proxmox/pve-docs/blob/master/pve-storage-rbd.adoc)

```bash
ceph df
rbd du POOL/IMAGE
rbd snap ls POOL/IMAGE
```

**`rbd du`** 报告已预配和实际映像用量，包括相关快照。如果映像没有启用 `fast-diff` 功能，命令会向 OSD 查询可能存在的对象，需要更多工作。**`ceph df`** 显示池和集群容量。复制、纠删码和快照会影响集群原始用量，因此映像字节数与池字节数不同。[Ceph RBD 命令参考](https://docs.ceph.com/en/squid/man/8/rbd/)和[Ceph 池用量指南](https://docs.ceph.com/en/squid/rados/operations/monitoring/)

若 RBD 存储使用命名空间，每个 `rbd` 命令都要添加 **`--namespace NAMESPACE`**。使用 Proxmox 存储条目中配置的命名空间，而不是 Proxmox 存储 ID。

## 计算快照和备份占用

**快照会保留旧版本的块。** 如果 trim 后用量没有下降，请查看 VM 或 CT 的 **Snapshots** 标签页，并检查后端快照清单。删除快照前先确认所有权和依赖关系。备份是另一份副本，遵循备份存储的保留规则，与客户机当前的 `df` 结果无关。

**PBS 去重会改变空间统计方式。** 它的数据存储会保留多个备份共享的数据块。prune 会删除备份快照元数据。之后的垃圾回收会在宽限期等规则下删除不再引用的数据块。声称备份容量已回收前，应检查这两项任务。[PBS 维护文档](https://pbs.proxmox.com/docs/maintenance.html)

> **警告：** 不要根据名称猜测并删除 Proxmox 管理的卷文件、zvol 或快照。先确认客户机和保留策略。清理存储时，必须保留备份和回滚路径。

## 关闭 VM 后重建磁盘映像

**只有在常规客户机 trim 和后端路径无法解决 qcow2 分配问题时，才使用离线转换。** 关闭 VM，验证备份，识别所有快照与后备链关系，然后写入单独的目标映像。QEMU 警告不要修改正被其他进程使用的映像。[QEMU `qemu-img` 文档](https://www.qemu.org/docs/master/tools/qemu-img.html)

**对于有快照的磁盘或位于受管理块存储上的磁盘，优先使用 Proxmox 管理的迁移或备份与还原流程。** 对 PVE 管理的映像单独运行 `qemu-img convert` 不会自行更新 VM 配置、卷所有权或快照引用。不要通过 `qemu-img resize --shrink` 回收已删除文件的空间。如果尚未先缩小分区和文件系统，缩小容量会减少客户机可见空间并可能截断数据。

## 排查空间回收失败

| 现象 | 可能的检查项 | 下一步 |
|---|---|---|
| **客户机 `df` 用量下降，主机不变** | VM discard 标志、客户机 trim、快照 | 验证完整 discard 路径和保留的快照。 |
| **`fstrim` 报告不支持** | 客户机磁盘总线、堆叠块设备、后端 | 检查 `lsblk -D`、客户机内核及每个中间层。 |
| **Windows ReTrim 已完成，主机用量不变** | 后端分配、快照、服务器统计 | 比较卷和池的用量。确认磁盘使用精简存储。 |
| **`ls -lh` 与 `du -h` 数值不同** | 稀疏文件或 qcow2 文件 | 使用 `du` 查看已分配的文件系统块。 |
| **LVM 精简配置 池仍然占用率很高** | 数据、元数据、快照 | 删除内容前检查 `lvs` 和 PVE 快照。 |
| **ZFS 池仍然占用率很高** | 快照保留块和预留量 | 检查 `usedbysnapshots`、zvol 设置和池容量。 |
| **CT 的 `df` 与池用量不一致** | bind 挂载、挂载点、快照 | 将 `rootfs` 和各个 `mpN` 映射到主机上的所有者。 |

**后台任务结束后再次检查。** trim、删除快照或后端垃圾回收后，存储统计可能延迟更新。将测得的池可用空间与初始值比较。不要仅根据客户机命令的退出代码判断操作成功。

## 后续步骤

**为每个客户机建立存储记录：** 虚拟大小、已分配字节、后端、总线、discard 标志、快照数量、备份覆盖范围和池可用空间。选择一台 VM，启用受支持的 discard 路径，在客户机内执行 trim，并比较记录值。只有第一台 VM 的结果符合后端预期行为后，再处理其他客户机。

如需制定更全面的恢复计划，请完成 [Proxmox 备份与还原演练](/articles/proxmox-vm-backup-restore-drill/)，并阅读 [Proxmox VE 8 升级到 9 指南](/articles/proxmox-ve-8-to-9-upgrade-guide/)。

## 来源

- [Proxmox VE 存储管理](https://github.com/proxmox/pve-docs/blob/master/pvesm.adoc)，存储类型、精简配置和容量风险。
- [Proxmox VE LVM 存储](https://github.com/proxmox/pve-docs/blob/master/pve-storage-lvm.adoc)，VE 9 快照卷链和分配。
- [Proxmox VE RBD 存储](https://github.com/proxmox/pve-docs/blob/master/pve-storage-rbd.adoc)，池与命名空间配置。
- [Proxmox VE 虚拟机](https://github.com/proxmox/pve-docs/blob/master/qm.adoc)，磁盘总线、格式、discard 和客户机代理。
- [Proxmox VE VM 磁盘选项](https://github.com/proxmox/pve-docs/blob/master/generated/qm.conf.5-opts.adoc)，总线专用标志。
- [Proxmox VE 容器](https://github.com/proxmox/pve-docs/blob/master/pct.adoc)，root 文件系统和挂载点归属。
- [Proxmox VE 容器命令](https://github.com/proxmox/pve-docs/blob/master/generated/pct.1-synopsis.adoc)，由主机执行的容器 trim。
- [Proxmox VE 备份与还原](https://github.com/proxmox/pve-docs/blob/master/vzdump.adoc)，VM 和 CT 备份覆盖范围。
- [Microsoft `Optimize-Volume` 文档](https://learn.microsoft.com/en-us/powershell/module/storage/optimize-volume?view=windowsserver2025-ps)，Windows ReTrim 语法。
- [Red Hat 未使用块指南](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/8/html/managing_file_systems/discarding-unused-blocks_managing-file-systems)，Linux `fstrim` 行为。
- [OpenZFS 快照与克隆](https://openzfs.github.io/openzfs-docs/Basic%20Concepts/Datasets/Snapshots%20and%20Clones.html)，快照保留的块。
- [Ceph RBD 命令参考](https://docs.ceph.com/en/squid/man/8/rbd/)，映像用量和快照。
- [NFSv4.2 规范](https://www.rfc-editor.org/rfc/rfc7862.html#section-6.2.2)，服务器端空间释放。
- [PBS 维护文档](https://pbs.proxmox.com/docs/maintenance.html)，prune 和垃圾回收。
- [QEMU 磁盘映像工具](https://www.qemu.org/docs/master/tools/qemu-img.html)，离线映像转换安全性。
