---
title: "Proxmox 上 LXC 中的 Docker：可靠性、证据与迁移到 VM"
date: 2026-09-16
lastmod: 2026-11-20
toc: true
draft: false
description: "通过一项有记录的 AppArmor 故障、对主机冻结报告的审慎解读、诊断命令和 VM 迁移计划，评估在 Proxmox LXC 中运行 Docker。"
genre: ["虚拟化", "Linux 管理", "家庭实验室"]
tags: ["LXC 中的 Docker", "Proxmox 上的 Docker", "Proxmox 上的 LXC 容器", "Docker 虚拟机", "家庭实验室可靠性", "Proxmox 主机冻结", "Debian Docker 虚拟机", "非特权容器", "容器嵌套", "Linux 内核隔离", "AppArmor", "runc", "lxc-pve", "Docker Compose", "Docker 存储驱动", "containerd 镜像存储", "内存压力", "Linux PSI", "持久化日志", "Proxmox 备份", "bind mount 备份", "虚拟机迁移", "故障域", "GPU 直通", "家庭服务器故障排查"]
cover: "/img/cover/docker-lxc-vm-homelab-isolation.webp"
coverAlt: "家用服务器等距插画，展示嵌套工作负载方框，以及连接到共享硬件的独立虚拟机隔间"
coverCaption: "共享硬件与不同工作负载隔离边界的概念图"
---
**在 Linux 容器（LXC）中运行 Docker** 能减少一些基础设施开销，但会增加应用运行时与 Proxmox 主机之间的交互。对于家庭依赖的 Docker 服务，Debian **虚拟机（VM）** 是一个实用的起点，因为它隔离了来宾内核，也简化了故障排查时需要复现的环境。本文会审视给定的视频、核对相关事件报告，并补充已记录的故障案例和迁移计划。

<!--more-->

## 要点

- **区分故障类型**：Docker 启动错误、VM 停滞和物理主机无响应，需要不同的调查方法。
- **评估证据**：迁移后的稳定性支持恢复决策，但无法证明最初的原因。
- **核对当前文档**：原生 OCI 镜像支持与在 LXC 中嵌套运行 Docker 是不同的部署路径。
- **保护持久数据**：Proxmox 备份和 Compose 文件不会自动涵盖所有应用数据位置。
- **测试恢复计划**：在退役旧部署之前，测量恢复、重启行为和服务可用性。

## 开始前

**难度**：中级。**读者**：正在选择嵌套 Docker 或 VM 中 Docker 的 Proxmox 管理员。阅读诊断示例前，你应能识别 Compose 项目、容器挂载和 Linux 命令行提示符。

**预计投入**：为清点资产和收集证据预留 30 到 60 分钟。迁移时间取决于数据库大小、存储吞吐量、硬件访问方式和你选择的停机窗口。下文示例属于有文档依据的流程和说明性推理，并非本文实验室测得的基准数据。

| 要求 | 原因 |
|---|---|
| **主机控制台访问** | 区分网络故障与整台主机停滞 |
| **当前备份** | 更改部署前提供恢复路径 |
| **容器和 VM ID** | 确保主机命令指向预期工作负载 |
| **应用数据清单** | 找出卷、绑定挂载、数据库和外部依赖 |
| **独立测试环境** | 支持迁移演练，避免生产环境出现重复写入 |

## 观看来源视频

{{< youtube id="XyPBHhZg0Ok" enable="true" title="Proxmox: The Hidden Danger of Running Docker Inside LXC" description="讲解在 Proxmox LXC 中嵌套运行 Docker、主机间歇性冻结以及迁移到 Debian 虚拟机" uploadDate="2026-09-15T17:00:09-07:00" >}}

**来源视频：**[Proxmox: The Hidden Danger of Running Docker Inside LXC](https://www.youtube.com/watch?v=XyPBHhZg0Ok)，由 *Proxmox x Kubernetes x Homelab x Backup* 于 2026 年 9 月 15 日发布。核心问题很实用：节省资源的架构会带来多少运维不确定性？

**证据边界**：视频讲述了一起事件并提出经验。下文将所有者的观察、已有文档记录的软件行为以及由此得出的建议分别说明。

## 该事件能证明什么

原始报告描述了一台配备 **Intel Core i3-13100 和 BIOSTAR H610MHP** 的主机。所有者报告称，间歇性冻结影响了管理访问和 LXC 服务。连接的显示器停止响应，但报告明确说明 syslog 仍持续输出。相比将事件描述为完全没有日志，这一细节更准确。[Proxmox 论坛原始报告](https://forum.proxmox.com/threads/pve-host-freezes-every-2-3-weeks.185009/)

所有者后来报告称，**迁移后情况有所改善**。在 8 月 3 日的跟进中，他们称已将 Docker 工作负载迁至 Debian 虚拟机，并停止承载 Docker 的 LXC。当时他们未报告再次冻结，视频则引用了连续稳定 16 天的记录。两种说法都没有提供受控复现，也没有指出具体哪个组件存在缺陷。[同一讨论串中的所有者跟进](https://forum.proxmox.com/threads/pve-host-freezes-every-2-3-weeks.185009/)

| 观察 | 能支持什么 | 不能证明什么 |
|---|---|---|
| **最初长时间运行正常** | 先前的工作负载和软件组合曾成功运行 | 每次后续更新后的可靠性 |
| **主机和服务停滞** | 故障影响范围超出单个应用 | Docker 是根本原因 |
| **迁移后情况改善** | 一种有用的运维变通方案 | 哪项变化消除了触发条件 |
| **稳定运行十六天** | 一个有界的观察期 | 所有两到三周一次的故障模式都已解决 |

**观察期**需要仔细审视。十六天落在 14 至 21 天的复发窗口内。延长观察期，覆盖此前多个故障间隔、相近的工作负载和常规维护，可以增加信心，但仍不足以构成受控的因果证明。

**运维成功与根因证明**是两个不同结果。恢复家庭依赖的服务，是迁移的合理理由。在更有力的证据证实机制之前，应将结果描述为观察到的可靠性有所改善。

## 找出内核边界

```text
LXC中的Docker：
应用程序 -> Docker运行时 -> LXC命名空间和策略
                 -> Proxmox宿主机内核 -> 物理硬件

虚拟机中的Docker：
应用程序 -> Docker运行时 -> 来宾Linux内核
                 -> 虚拟硬件 / KVM-QEMU
                 -> Proxmox宿主机内核 -> 物理硬件
```

**LXC**使用主机内核。命名空间、控制组、能力、seccomp 和安全配置文件会限制进程，但不会提供独立内核。在 LXC 中再运行 Docker，会为使用同一主机底层内核的工作负载增加另一层容器管理。 [LXC 架构与隔离功能](https://linuxcontainers.org/lxc/introduction/)

**VM**会引入来宾内核。来宾内核故障通常只影响对应 VM，Proxmox 仍可管理其他来宾。VM 仍依赖物理主机、虚拟机监控程序、存储和网络。硬件故障或主机内核缺陷依然是共享依赖项。

| 边界 | LXC 中的 Docker | VM 中的 Docker |
|---|---|---|
| **应用使用的内核** | Proxmox 主机内核 | 来宾内核 |
| **Docker 运行环境** | 受外层容器策略限制 | 安装在常规来宾操作系统中 |
| **来宾内核更新** | 与主机内核绑定 | 在来宾内部管理 |
| **物理主机故障** | 停止依赖它的工作负载 | 停止依赖它的工作负载 |

VM 能限制**部分故障传播**，但无法阻止所有故障。LXC 中的应用进程崩溃不会自动导致 Proxmox 崩溃。同样，把所有家庭服务都放进一个 Docker VM，仍会让这些服务共用一个来宾操作系统和维护计划。

如需了解**更广泛的概念比较**，请参阅 [Docker 容器与虚拟机](/articles/docker-vs-vms/)。本文讨论的是 Docker 在 Proxmox 中的部署位置以及由此形成的故障排查边界。

## 准确定义支持范围

**“不受支持”** 必须指出具体组件和版本。请区分供应商推荐的部署方式、已记录的功能、发行版维护以及合同中的支持权益。嵌套架构能够运行，并不能证明每种组合都经过同等测试；推荐使用 VM，也不意味着维护者会拒绝所有与嵌套有关的问题报告。

**当前 Proxmox 文档** 还指出了一个重要区别。其容器工具包源码将 **开放容器倡议（OCI）** 应用镜像支持描述为技术预览，并会将镜像转换为 LXC 框架。对于强调隔离和在线迁移的需求，文档也建议在 QEMU VM 中运行容器。将 OCI 镜像导入该框架，与在 LXC 来宾中安装 Docker Engine 并运行 Compose，并不是同一做法。[Proxmox 容器工具包文档](https://github.com/proxmox/pve-docs/blob/master/pct.adoc)

| 部署方式 | 需要核对的问题 |
|---|---|
| **传统 LXC 来宾** | 其操作系统模板和应用是否符合已记录的容器限制？ |
| **在 LXC 中嵌套 Docker** | 哪些内核、运行时、安全策略和存储组合经过测试？ |
| **原生 OCI 镜像导入** | 已安装的 Proxmox 版本是否提供文档所述功能和所需行为？ |
| **在 Debian VM 中运行 Docker** | 来宾发行版是否满足 Docker 安装要求？ |

Docker 发布了 **Debian 安装路径**。请使用来宾对应的受支持版本列表和软件源说明。记录实际部署的版本，不要假定旧教程仍然准确。这提供了有文档依据的安装基线，但不保证正常运行时间，也不会自动产生付费支持合同。[Debian 上的 Docker Engine](https://docs.docker.com/engine/install/debian/)

## 已确认的嵌套故障

**2025 年 runc 与 AppArmor 的不兼容问题**是一个可核实案例。runc 维护者记录了一起故障：在启用了 AppArmor 配置文件的外层容器中重新打开文件描述符时发生错误。AppArmor 将对 **`/proc/sys`** 的访问误判为对 **`/sys`** 的访问，从而拒绝了策略请求。[runc 问题 4968](https://github.com/opencontainers/runc/issues/4968)

**受影响的启动过程**报告了以下错误片段：

```text
open sysctl net.ipv4.ip_unprivileged_port_start file: reopen fd 8: permission denied
```

已记录的故障阻止了**容器启动**，但无法解释论坛所有者报告的主机冻结。该问题记录显示，**`lxc-pve 6.0.5-2`** 是 Proxmox 针对此特定问题提供的修复版本，对应的上游 LXC 更改于 2025 年 11 月 20 日合并。*这些是历史修复记录，并非建议当前安装固定使用该软件包版本。* [维护者的修复摘要](https://github.com/opencontainers/runc/issues/4968)，[已合并的 LXC 更改](https://github.com/lxc/lxc/pull/4609)

这里的经验是**协调依赖项**。运行时安全更改与外层容器策略发生了交互，修复则需要修改另一层。应安装适用于当前发行版的维护版软件包更新，不要永久关闭 AppArmor，也不要保留存在已知漏洞的旧运行时。

> **要点**：该事件说明嵌套容器确实存在兼容性问题，维护者也确实作出了响应。它既不能证明 LXC 普遍不稳定，也不能说明另一起主机锁死事件的原因。

## 比较实际成本

使用你的**实际工作负载**测量效率。在相同条件下比较主机内存压力、CPU 需求、存储延迟、应用响应时间和恢复工作量。VM 分配的内存、来宾可用内存和主机常驻内存代表不同测量值。

| 声称的节省 | 要收集的测量值 | 要记录的额外成本 |
|---|---|---|
| **降低内存开销** | 相同工作负载下的主机内存用量和压力 | 管理嵌套限制并诊断资源争用所花的时间 |
| **部署更快** | 恢复数据并让服务正常运行所需的时间 | 更新失败后重建所需的时间 |
| **更简单地共享硬件** | 所需设备、权限和应用成功使用情况 | 对主机驱动程序的依赖及迁移限制 |
| **备份更容易** | 全部所需数据成功恢复的情况 | 外部挂载和应用一致性 |

Docker 文档说明，默认情况下 **CPU 和内存不受限制**，除非设置了限制。在 LXC 部署中，外层容器会增加自身限制。在 VM 中，来宾资源分配也会形成容量边界。来宾仍需要为操作系统、Docker、缓存和应用峰值需求预留容量。[Docker 资源限制](https://docs.docker.com/engine/containers/resource_constraints/)

**硬件访问**是工作负载要求的一部分。将主机图形设备共享给容器，与把 PCI 设备分配给 VM，涉及不同的驱动程序和隔离方式。选择前应列明具体设备和应用需求。例如，需要硬件解码的媒体工作负载，迁移后应进行实际解码测试，不能只做普通 HTTP 健康检查。

避免使用**普遍适用的开销数字**。本文没有给出固定的 RAM 成本或性能百分比，因为这些数字需要受控的工作负载、配置和测量方法。请在下方决策记录中填写你自己比较得出的观察结果。

## 按层收集证据

**先从 Proxmox 主机开始**，使用管理员 shell。将 **`101`** 替换为正在调查的 LXC ID：

```bash
pveversion -v
uname -r
pct config 101
journalctl --list-boots
journalctl -k -b -1 --no-pager
```

**`pveversion -v`** 会记录已安装的 Proxmox 组件版本。**`pct config`** 会记录外层容器配置。在 **`journalctl`** 中，**`-k`** 选择内核消息，**`-b -1`** 选择上一次启动，**`--no-pager`** 则输出纯文本。要查看之前启动的消息，必须保留对应的 journal 数据。[Proxmox 工具包](https://github.com/proxmox/pve-docs/blob/master/pct.adoc)，[systemd journalctl 参考](https://github.com/systemd/systemd/blob/main/man/journalctl.xml)

**然后检查 Docker 主机**，也就是运行其守护进程的 LXC 或 VM 内部：

```bash
docker version
docker info
docker compose version
docker ps -a
docker stats --no-stream
```

记录**两个环境**的信息。只记录容器镜像标签，会漏掉 Docker、containerd、runc、主机内核、安全策略和存储后端。保存事件时间、近期更新以及本地主机控制台是否有响应。发布诊断材料前，请删除凭据和应用私密信息。

**检查某个工作负载**，将 **`app`** 替换为容器名称：

```bash
docker inspect --format '{{json .State}}' app
docker inspect --format '{{.RestartCount}}' app
docker inspect --format '{{json .Mounts}}' app
```

**`docker inspect`** 会显示指定容器的状态、重启次数和挂载信息。将重启次数视为需要与日志关联的线索，而不是主机级故障的证据。重新创建的容器也会开始一段新的记录。[docker inspect 参考](https://docs.docker.com/reference/cli/docker/inspect/)

## 区分资源压力与锁死

问题发生时，**在主机上收集 Linux 资源压力信息**：

```bash
cat /proc/pressure/cpu
cat /proc/pressure/memory
cat /proc/pressure/io
```

**Pressure Stall Information（PSI，压力停滞信息）** 会报告任务等待资源时损失的时间。**`some`** 和 **`full`** 字段描述不同的停滞状况，**`avg10`**、**`avg60`** 和 **`avg300`** 则汇总近期区间。内存压力不同于内存占用量。仅有大量缓存，不能证明内存不足。[Linux PSI 文档](https://docs.kernel.org/accounting/psi.html)

| 证据 | 有用的解释 | 下一步检查 |
|---|---|---|
| **某个容器反复退出** | 应用或容器运行时故障 | 退出状态、服务日志、重启策略 |
| **SSH 失败，但控制台正常** | 网络或管理路径故障 | 链路状态、网卡驱动、网桥、防火墙 |
| **负载下内存 PSI 上升** | 任务因内存争用而损失时间 | 限制、回收活动、OOM 记录、工作负载增长 |
| **存储请求停滞** | I/O 依赖项延迟了处理 | 设备健康状态、存储日志、延迟和队列 |
| **看门狗报告锁死** | 内核检测器观察到了定义明确的停滞状况 | 完整跟踪、内核版本、可复现的触发条件 |
| **没有最后一条日志** | 证据收集在有用输出到达前结束 | 在再次发生前启用持久或外部采集 |

**Linux 锁死报告**具有特定技术含义。内核看门狗会区分软锁死和硬锁死。浏览器请求超时不能证明发生了其中任一种情况；没有看门狗报告，也不能证明主机一直正常。[Linux 锁死检测器文档](https://docs.kernel.org/admin-guide/lockup-watchdogs.html)

**固件和电源状态更改**属于实验。记录旧设置、更改理由和观察期。禁用 CPU 空闲状态会改变功耗和温度行为，因此另一台设备的报告不足以支持将相同设置普遍作为建议。

## 保留有用日志

启用**持久日志记录**有助于在重启后保留证据。journald 的配置片段使用以下设置：

```ini
[Journal]
Storage=persistent
```

**`Storage=persistent`** 会在条件允许时请求将 journal 写入磁盘。更改时应同时配置保留限制和可用磁盘容量，然后确认 **`journalctl --list-boots`** 中出现了之前的启动记录。持久日志仍依赖主机在故障前完成写入。[systemd journald 配置](https://github.com/systemd/systemd/blob/main/man/journald.conf.xml)

**外部监测**会提供另一个视角。从其他机器监测服务并记录时间戳。如果监测程序运行在发生故障的 Proxmox 主机上，它会随着同一次故障消失，因而难以区分服务停机和遥测缺失。

**说明性测试**：从另一台系统安排一次轻量 HTTP 检查，再将检查失败与主机可达性及本地控制台状态进行比较。应用超时但主机仍有响应，与应用、管理连接和控制台同时失效，代表不同的调查方向。这是一种诊断设计，并非来源事件中实际观察到的结果。

## 规划受控迁移

从**一个低风险 Compose 项目**开始。使用 Docker 安装文档中列出的 Debian 版本准备 VM、建立备份并配置资源分配。替代部署通过测试前，保留原部署以便回滚。[Docker 在 Debian 上的安装说明](https://docs.docker.com/engine/install/debian/)

在工作目录中**清点 Compose 项目**：

```bash
docker compose config --quiet
docker compose config --images
docker compose config --volumes
```

**`--quiet`** 会验证配置但不输出内容。**`--images`** 会列出引用的镜像，**`--volumes`** 会列出命名卷。这些命令不会导出应用数据，也无法完整列出绑定挂载。还应检查 Compose 文件和每个容器的挂载配置。[Docker Compose 配置 参考](https://docs.docker.com/reference/cli/docker/compose/config/)

| 数据或依赖项 | 迁移操作 |
|---|---|
| **Compose 定义** | 传输项目文件并保留经过测试的配置 |
| **密钥和环境变量** | 通过选定的密钥管理流程重新设置所需值 |
| **命名卷** | 使用符合应用一致性要求的流程备份和恢复卷内容 |
| **绑定挂载路径** | 传输或重新连接实际源数据，并验证所有权 |
| **数据库** | 使用数据库支持的备份/恢复流程，或在静默写入后复制 |
| **设备和共享目录** | 重新建立访问并测试应用行为 |
| **端口和 DNS** | 准备替代地址并规划切换 |

**卷**会在容器删除后保留，但不会自动迁移。Compose 文件用于命名资源和定义服务。Docker 卷文档说明，持久内容需要单独执行备份和恢复操作。不要假定重新创建项目就能恢复数据。[Docker 卷生命周期与备份](https://docs.docker.com/engine/storage/volumes/)

还要单独核对 **Proxmox 备份覆盖范围**。其备份文档说明，容器备份不包含设备和绑定挂载中的内容。因此，成功备份 LXC 根文件系统，并不能证明已保护其中暴露的所有目录。[Proxmox 备份文档](https://github.com/proxmox/pve-docs/blob/master/vzdump.adoc)

### 复制前检查存储

**在每个 Docker 主机上检查实际存储配置**：

```bash
docker info
findmnt -T /var/lib/docker
```

**`findmnt`** 会识别指定路径所在的文件系统。如果守护进程使用了其他数据根目录，请替换 **`/var/lib/docker`**；适用时还要检查 containerd 的存储路径。Docker 文档区分了 containerd 镜像存储与经典存储驱动，它们各自有后端特定要求。[Docker 存储后端选择](https://docs.docker.com/engine/storage/drivers/select-storage-driver/)

按照所选后端的文档流程**重新创建镜像并恢复应用数据**。在不同存储架构之间复制正在使用的 Docker 数据目录，会引入关于元数据、挂载状态和一致性的额外假设。这不同于备份已停止应用的数据卷。

### 切换并保留回滚路径

1. **在 VM 中演练恢复**，适当时使用独立地址和测试数据。
2. **在约定的停机窗口内停止生产写入**，并执行最后一次一致性备份。
3. **恢复并验证**应用数据、权限、凭据和必要的硬件访问。
4. **在替代部署通过应用专属检查后**切换服务路由。
5. **保持原部署停止运行**，同时保留其配置和恢复数据。
6. **记录回滚处理办法**，说明切换后写入的数据应如何处理，然后再启动旧系统。

避免让**两个活动写入者**同时操作同一数据库存储。若回滚时已有新的生产数据，就需要计划如何保留或有意丢弃这些写入。仅仅重启旧容器，无法合并两份已经分叉的数据历史。

## 不要只测试运行时间

**验收测试**应符合服务用途。容器状态为绿色只说明进程正在运行。可用服务还需要数据、网络访问、依赖项和有效的恢复行为。

| 测试 | 要保留的证据 |
|---|---|
| **应用功能** | 一次成功的真实事务、查询或媒体操作 |
| **数据完整性** | 预期记录、文件、权限和近期更改 |
| **来宾重启** | 无需手动修复即可恢复服务 |
| **备份恢复** | 恢复副本通过相同的功能检查 |
| **代表性负载** | 延迟、CPU、内存压力和存储行为 |
| **维护演练** | 经过测试的更新和可用的恢复流程 |
| **延长观察期** | 覆盖此前多个故障间隔的可用性记录 |

**示例决策**：摄像头服务和实验性下载器目前共用一个嵌套环境。把二者迁移到同一 VM 能改善内核隔离，但仍共用一个来宾维护边界。如果摄像头可用性优先，应评估独立维护组和资源限制，再测试下载器更新期间录像是否连续。

**预期推理**：应根据你要隔离的服务依赖来选择部署位置。同一物理服务器上的两台 VM 仍共用电源、存储和主机内核。如果需求包括承受服务器停机，设计还需要另一套独立系统或可接受的人工备用方案。

## 创建决策记录

**使用实测证据**选择部署方式，并确定何时重新评估：

```text
服务和家庭影响：
当前宿主机 / 内核 / LXC / Docker版本：
所需的GPU、设备和网络访问：
测得的内存、CPU、存储和延迟：
已知故障特征及复现间隔：
备份覆盖范围及成功恢复的证据：
所选架构及原因：
允许的中断窗口和恢复目标：
切换及切换后的数据回滚流程：
验收测试和观察期：
需要重新评估架构的条件：
```

当 LXC 嵌套的收益足以抵偿集成工作，而且你已经测试恢复路径时，才**有意识地选择 LXC 嵌套**。如果常规 Docker 来宾环境和独立来宾内核能简化服务运维，就选择 VM。无论哪种选择，都不能取代备份、监控和主机维护。

## 迁移前设置变更门槛

将迁移视为一项**受控变更**，而非原始事件原因的证明。切换前，记录当前容器配置、镜像摘要、绑定挂载路径、环境变量键、设备映射以及最近一次成功恢复的证据。切换后，对比相同的服务检查和资源读数。新副本通过验收期之前，保持旧工作负载停止。

如果迁移后事件再次发生，应比较两种部署中的主机内核、存储、内存压力、设备访问和 Docker 版本。这样的比较能缩小调查范围。只有相关变量保持受控，迁移成功才可能成为因果实验。

## 后续步骤

先**清点一项服务**。找出它的持久数据、物理依赖、故障症状和恢复目标。决定是否需要迁移之前，先演练恢复。

对于**相关工作**，可使用 [Proxmox VE 升级指南](/articles/proxmox-ve-8-to-9-upgrade-guide/)规划升级，并使用 [Docker 与 Kubernetes 安全指南](/articles/how-to-secure-your-docker-and-kubernetes-environment/)加固工作负载。架构选择、升级执行和事件诊断应作为不同决策处理，并分别保留证据。

## 来源与证据

**核查日期**：2026 年 9 月 16 日。本文主题参考了给定的文字记录。视频元数据、原始事件报告、上游问题和官方文档分别核对。说明性练习和建议的验证步骤均已在正文中标明。

| 来源 | 用途 |
|---|---|
| **[来源视频](https://www.youtube.com/watch?v=XyPBHhZg0Ok)** | 原始讲解和其中报告的稳定时长 |
| **[Proxmox 事件讨论串](https://forum.proxmox.com/threads/pve-host-freezes-every-2-3-weeks.185009/)** | 当事人的观察和迁移后的跟进 |
| **[Proxmox 容器工具包](https://github.com/proxmox/pve-docs/blob/master/pct.adoc)** | 容器架构和当前 OCI 区别 |
| **[runc 问题 4968](https://github.com/opencontainers/runc/issues/4968)** | 已记录的启动故障和历史软件包修复 |
| **[LXC 拉取请求 4609](https://github.com/lxc/lxc/pull/4609)** | 已合并的上游 AppArmor 更改 |
| **[Docker 文档](https://docs.docker.com/engine/install/debian/)** | 来宾安装基线，正文上方附有具体运行时和存储参考 |
| **[Linux PSI 文档](https://docs.kernel.org/accounting/psi.html)** | 资源压力解读 |
| **[Linux 看门狗文档](https://docs.kernel.org/admin-guide/lockup-watchdogs.html)** | 已定义的内核锁死条件 |
| **[Proxmox 备份文档](https://github.com/proxmox/pve-docs/blob/master/vzdump.adoc)** | 容器挂载排除项和备份行为 |
