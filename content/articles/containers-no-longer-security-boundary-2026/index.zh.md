---
title: "2026年，容器已不再是安全边界"
date: 2026-09-28
lastmod: 2026-11-27
toc: true
draft: false
description: "2026年的内核漏洞揭示了多租户容器隔离为何不足。了解 Copy Fail、Dirty Frag、Fragnesia 和 CVE-2026-80521，并比较加固容器与 microVM 边界。"
genre: ["容器安全", "Linux", "内核安全", "虚拟化", "云安全", "威胁研究", "蓝队", "DevSecOps"]
tags: ["容器逃逸", "容器安全边界", "Linux 内核 CVE", "本地权限提升", "LPE 2026", "Copy Fail", "CVE-2026-31431", "Dirty Frag", "CVE-2026-43284", "CVE-2026-43500", "Fragnesia", "CVE-2026-46300", "CVE-2026-80521", "kernelCTF", "kvmCTF", "microVM", "Firecracker", "Kata Containers", "页缓存损坏", "AF_ALG", "AF_UNIX", "XFRM ESP", "RxRPC", "命名空间隔离", "clone 系统调用", "AI 漏洞发现", "Docker 安全", "Kubernetes 安全", "多租户隔离", "沙箱逃逸", "nsjail", "Bubblewrap", "Firejail", "Dirty Pipe", "内核 CVE 趋势"]
cover: "/img/cover/container-security-vulnerabilities-kernel-escapes-2026.webp"
coverAlt: "多个发光容器连接到中央内核符号的数字插图。深色背景上的彩色元素表示从内核扩散出的漏洞。"
coverCaption: ""
ref: ["/articles/docker-vs-vms", "/articles/how-to-secure-your-docker-and-kubernetes-environment", "/cvss-calculator"]
---
**容器共享同一个内核。2026年，四个独立的漏洞系列证明，一个内核错误就足以让攻击者离开容器并进入主机。** Copy Fail、Dirty Frag、Fragnesia 和 CVE-2026-80521 都能让无特权的本地用户获得 root 权限。每个漏洞都越过了容器边界。

*令人担忧的不是漏洞本身，而是 AI 如今能以多低的成本找到它们，以及一个补丁如何又引入了另一个漏洞。*

本文说明容器如何隔离工作负载、这种隔离为何如今依赖越来越狭窄的基础、2026年的每个漏洞会造成什么影响，以及有哪些隔离技术值得信赖。

**你将了解：**按每个工作负载的代码来源进行梳理，确定它需要哪些内核功能，并在加固容器和 microVM 边界之间作出选择。将2026年的案例视为有时间限制的研究证据。修改生产内核前，请重新核实供应商当前的公告。

## 简要回答

| 问题 | 简要回答 |
|---|---|
| **容器能隔离吗？** | 能隔离进程和文件系统。所有容器共享一个内核，因此内核漏洞会造成共同风险 |
| **为什么是现在？** | AI 辅助漏洞搜索降低了发现内核缺陷的成本。截至2026年9月，已发布近 **6,000 个内核 CVE** |
| **什么会突破边界？** | 内核中的任何本地权限提升。逃逸不需要容器配置错误 |
| **打补丁够吗？** | 打补丁是必要的，但速度已跟不上漏洞发现。一项2026年的补丁**引入了新的可利用漏洞** |
| **什么更有效？** | Firecracker 或 Kata Containers 等 microVM，它们为每个工作负载提供独立内核 |
| **替代方案完美吗？** | 不完美。虚拟机监控程序也是代码，但其攻击面小了许多，这正是关键差异 |

## 容器如何隔离

要理解边界，先要了解容器不是什么。

**容器不是虚拟机。** 它没有第二个内核、模拟硬件，也没有虚拟机监控程序位于进程和硬件之间。运行容器镜像时，你是在现有内核上运行一个进程，只是它看到的系统视图经过了修改。

其机制是 **`clone` 系统调用**。`fork` 会复制进程的地址空间，`clone` 则创建子进程，并精细控制执行上下文中的哪些部分共享、哪些部分替换。Docker 向 `clone` 传入一组**命名空间**：

| 命名空间 | 模拟内容 |
|---|---|
| **Mount** | 私有文件系统根目录，让容器看到自己的目录树，而不是你的目录树 |
| **PID** | 独立的进程编号，因此 `PID 1` 是容器的第一个进程，而不是 `systemd` |
| **User** | 身份映射，让容器内的“root”对应主机上的无特权用户 |
| **Network** | 私有接口、路由表和端口 |
| **IPC** | 隔离的共享内存和消息队列 |
| **UTS** | 独立的主机名和域名 |
| **Cgroup** | 私有的资源限制视图 |

在镜像上添加一个**联合文件系统**，结果*看起来*像一台独立计算机。在容器内运行 `id` 会显示 `uid=0(root)`。文件系统看起来像精简版 Ubuntu 安装。进程列表只显示容器自己的进程。

**在系统调用层面，这不是安全边界。** 容器内的进程打开文件、分配内存或访问网络套接字时，主机上的同一个内核会处理所有容器的请求。命名空间改变的是*进程能看到什么*，不是*内核会为进程做什么*。

*内核才是容器与主机之间真正的边界。其他一切都是呈现方式。*

{{< figure src="container-namespace-isolation-shared-kernel.webp" alt="图示展示三个容器共用同一内核。mount、PID、user 和 network 命名空间隔离各自的视图，但所有系统调用最终都由同一个共享内核处理" >}}

{{< youtube id="9-2CSJC114k" enable="true" title="the change is finally coming" nocookie="true" >}}

## 边界由代码实现，而代码会有漏洞

容器执行的每个操作都会经过**系统调用接口**。打开文件、读取内存、写入套接字、更改 UID：这些都由内核中介，因为内核不允许进程直接访问 CPU、文件系统或网络。

这种中介机制就是安全模型，而中介机制由代码实现。具体来说，它约有**三千万行**代码。

本地权限提升（LPE）是指进程利用中介代码中的缺陷，取得原本未获授予的权限。**LPE 并非新问题。** 自内核中介机制早期起就存在，几十年来业界一直面对持续出现的此类问题。

**2022年的 Dirty Pipe** 是大多数人熟悉的典型案例。它利用 pipe 缓冲区处理缺陷覆盖只读文件。之所以成为新闻，是因为此类严重漏洞**大约每一两年才会出现一次**。人们打上补丁后继续工作，并假设数百万人阅读的代码中没有大型缺陷长期未被发现。

*这个假设已经不成立。*

## 2026年发生了什么变化

变化不在于攻击者技能提升，而在于**寻找内核内存损坏漏洞从研究职业变成了工程任务**。

今年的三项数据具体说明了这种变化：

| 发现 | 发现者 | 方法 |
|---|---|---|
| **Copy Fail**（CVE-2026-31431） | Taeyang Lee，Theori | 借助 **Xint Code**，一款 AI 静态分析工具。扫描 Linux 加密子系统约用了**一小时** |
| **CVE-2026-80521** | Zhenpeng（Leo）Lin，DepthFirst | 使用针对漏洞检测训练的内部 AI 模型 **dfs-large1** 发现 |
| **CVE-2026-80521**，独立发现 | Kyle，**OpenAI** | 独立发现同一漏洞，并在同一天报告 |

再看第三行。两家组织使用不同的 AI 工具，发现了 **AF_UNIX 中同一个释放后使用漏洞（UAF）**，并在**同一天**报告给 `security@kernel.org`。这不是人才巧合，而是一个可重复的流程两次得出同样结果。

DepthFirst 直接说明了规模：**截至2026年9月，已发布近6,000个内核 CVE**。数量增长曲线跟随 AI 辅助能力的普及，而非内核开发者人数。

*当 AI 扫描一小时就能在加密子系统中发现一个十年前的漏洞，内核漏洞利用的成本结构就被颠覆了。*

## 一年四次逃逸

每个漏洞都能让无特权的本地账户获得 root。它们都不需要容器配置错误、特权标志或网络立足点。

| 漏洞 | CVE | 子系统 | 利用原语 | 发现者 |
|---|---|---|---|---|
| **Copy Fail** | CVE-2026-31431 | `algif_aead` / AF_ALG | 向任意可读文件的页缓存写入4字节 | Theori，AI 辅助 |
| **Dirty Frag** | CVE-2026-43284 + CVE-2026-43500 | XFRM ESP、RxRPC | 通过两个链式变体向页缓存写入4字节 | Hyunwoo Kim |
| **Fragnesia** | CVE-2026-46300 | XFRM ESP-in-TCP (在 TCP 中封装的 ESP) | 向页缓存写入单字节 | Hyunwoo Kim |
| **AF_UNIX UAF** | CVE-2026-80521 | AF_UNIX 套接字 | `unix_vertex` 垃圾回收中的释放后使用漏洞 | DepthFirst，AI 辅助 |

这四个漏洞有一个值得注意的共同设计模式：**它们攻击页缓存，而不是磁盘。**

### Copy Fail：无需竞态的逻辑缺陷

Copy Fail 是四者中最直接、也最令人担忧的漏洞。

几乎所有 Linux LPE 都需要一个时序窗口或特定于内核的内存偏移。**Copy Fail 两者都不需要。** 它是 `algif_aead` 中直接的逻辑缺陷。该模块通过 AF_ALG 向用户空间提供认证加密访问。

利用链使用 `splice()` 将页缓存页面放入操作，然后滥用原位 AEAD 路径向该页面写入**四个受控字节**。受损页面**从不标记为 dirty**，因此不会写回磁盘。磁盘上的文件保持完整，校验和与完整性检查都会通过，但内存中的副本已经被修改。

一个 **732 字节的 Python 脚本**能在2017年以来发布的所有 Linux 发行版上取得 root。漏洞由 `algif_aead` 中的**2017年优化**引入，2026年的补丁只是撤销该优化。主线提交 `a664bf3d603d`。

*该漏洞在所有主流发行版中潜伏近十年，AI 工具约一小时就发现了它。*

### Dirty Frag：两个互补的变体

Dirty Frag 的名称准确描述了它的脉络：**Dirty Pipe 覆盖 `struct pipe_buffer`。Dirty Frag 覆盖 `struct sk_buff` 的 `frag` 字段。**

它由**两个串联的漏洞**组成，串联方式正是巧妙之处：

- **CVE-2026-43284** 利用 `esp_input()` 跳过 copy-on-write 路径，再对 splice 插入的片段进行原位解密。它需要创建 **用户命名空间** 的权限，部分发行版会限制该权限。
- **CVE-2026-43500** 利用 `rxkad_verify_packet_1()` 对片段进行原位解密。它不需要命名空间权限，但大多数发行版没有 `rxrpc` 模块。Ubuntu 默认加载该模块。

**单独使用时，每个变体都有盲点。组合后，它们相互补足。** 允许用户命名空间时，ESP 路径先运行。若其受限但存在 `rxrpc`，则改走 RxRPC 路径。这样，一个漏洞利用二进制程序就能适配多个发行版。RxRPC 变体会清空 `/etc/passwd` 中一个字段，并利用 PAM 的 `nullok` 接受空密码，从而获得 root。

**对防御者最重要的发现是：** 无论 **`algif_aead` 是否可用**，Dirty Frag 都会触发。广泛传播的 Copy Fail 缓解措施通过屏蔽该模块，**完全无法防御 Dirty Frag**。

### Fragnesia：补丁引入的漏洞

Fragnesia 与 Dirty Frag 属于同一类，但针对 XFRM 的 **ESP-in-TCP** 路径。这是其中最具启发性的案例。

该漏洞利用 `skb` 合并过程中对共享页面片段处理不当。攻击者在套接字切换到 `espintcp` 上层协议模式前，将文件支持的页面 splice 到 TCP 接收队列中。ESP 处理启用后，内核会**原位解密**队列数据，AES-GCM 密钥流操纵会破坏底层页缓存。攻击者能对缓存文件页面反复执行**单字节写入**。

该漏洞利用通过用小型 ELF 载荷覆盖 `/usr/bin/su` 的开头字节来取得 root。**改动只存在于内存中，不会触及磁盘上的二进制文件。**

无特权的 **用户命名空间和网络命名空间** 在隔离的命名空间内提供 `CAP_NET_ADMIN`，随后 NETLINK_XFRM 安装精心构造的安全关联。

*请仔细读这句话：* Fragnesia 是**修复最初 Dirty Frag 漏洞的某个补丁带来的意外副作用**。修复 Dirty Frag 反而产生了一个可独立利用的新 root 漏洞。

### CVE-2026-80521：赢得 kernelCTF 的容器逃逸

AF_UNIX 竞态终结了“这只是理论风险”的说法。

该漏洞是 `SCM_RIGHTS` 消息垃圾回收机制中的 **堆上释放后使用漏洞（UAF）**。进程通过 `SCM_RIGHTS` 相互传递文件描述符。在回收循环套接字引用时发生竞态，释放了 `struct unix_vertex`，但仍存活的套接字 SCC 环中还保留着它的指针。下一轮回收会遍历过期的环并解引用已释放的内存。

它的意义不止于 Linux，因为 **AF_UNIX 是本地 IPC 的基础**。本地数据库、`systemd`，甚至 Docker 本身都依赖它。DepthFirst 指出，这个漏洞影响大多数基于内核构建的操作系统级 sandbox，**包括 `nsjail`、`Firejail` 和 `Bubblewrap`**，以及现代容器运行时。

DepthFirst 于 **2026年7月24日**凭此漏洞赢得 **Google kernelCTF 名额**，于 **8月5日**在 `lts-6.12.95` 名额中获得确认，当天报告给 `security@kernel.org`，随后得知 **OpenAI 的 Kyle 也报告了同一个漏洞**。上游补丁于 **8月6日**合入。研究成果于 **9月22日**发布。

他们发布了针对 **Ubuntu 26.04** 的可用漏洞利用程序，以及另一个利用 CVE-2026-52910 逃逸 **Ubuntu 24.04** 的漏洞利用程序。

{{< figure src="kernel-page-cache-overwrite-container-escape.webp" alt="示意图展示容器内的无特权进程损坏页缓存页面，在内存中修改 setuid 二进制并提升为 root，随后越过容器边界进入主机内核" >}}

## 缓解建议为何不断失效

今年防御者经历了三轮变通方案，每一轮都存在部分问题。

| 缓解措施 | 能阻止什么 | 遗漏什么 |
|---|---|---|
| 将 **`algif_aead`** 加入黑名单 | Copy Fail | **Dirty Frag 的任何部分都不行**，它完全不依赖该模块 |
| 将 **`esp4`、`esp6`、`rxrpc`** 加入黑名单 | Dirty Frag、Fragnesia | 需要 IPsec 的团队。全新的子系统也会遗漏 |
| 限制**无特权用户命名空间** | ESP 变体 | RxRPC 变体不需要命名空间。AppArmor 策略也只是**部分**缓解 |
| **修补内核** | 已修复的漏洞 | 下一个漏洞，以及补丁引入的任何漏洞 |

有两个模式值得注意。

**第一，变通方案彼此冲突。** 禁用 `algif_aead` 可以缓解 Copy Fail。Dirty Frag **无论该模块是否存在都会触发**。Fragnesia 需要禁用 `esp4` 和 `esp6`，这会影响任何使用 IPsec 的人。没有一份模块黑名单能覆盖整个漏洞系列。

**第二，更糟的是，打补丁并非毫无代价的胜利。** Fragnesia 是由 **Dirty Frag 补丁引入的**。每个补丁都有引入新逻辑错误的风险，而在这个子系统中，逻辑错误会导致获取 root 权限的漏洞利用。

*令人不安的结论是：这些漏洞都在页缓存中，都能从无特权代码触达，而且都是由每季度都在改进的工具发现的。任何黑名单都无法一直保持完整。*

## 诚实回应反方观点

有一个合理的反对意见值得直接回答：**虚拟机监控程序也有漏洞。**

KVM 的攻击面确实存在。Google 专门运行 **kvmCTF** 来发现此类漏洞，并提供丰厚奖励：

| 等级 | 奖励 |
|---|---|
| **完整 VM 逃逸** | **$250,000** |
| 任意内存写入 | $100,000 |
| 任意内存读取 | $50,000 |
| 相对内存写入 | $50,000 |
| 拒绝服务 | $20,000 |
| 相对内存读取 | $10,000 |

奖励不累加。目标是运行 KVM 的 Linux LTS 内核，guest 为 Debian 12.5。目标是实现**从 guest 到 host 的攻击**。

**发现 Dirty Frag 的同一位研究人员 Hyunwoo Kim 也会获得 KVM 漏洞赏金**，并因 VM 逃逸赢得了完整的 $250,000。因此，诚实的总结是：两个层面都有缺陷，有时是同一个人发现了它们。

**但比较一下规模：**

| | Linux 内核 | KVM 虚拟机监控程序 |
|---|---|---|
| **2026年的 CVE** | 近 **6,000 个** | 少数，每位研究人员每年发现几个 |
| **可从何处触达** | 任何无特权进程都能通过 syscall 接口触达 | 只能由已经运行在 guest 内的代码触达 |
| **攻击面** | 所有部分：网络、文件系统、加密、IPC、驱动程序 | 虚拟设备和 hypercall 接口 |
| **漏洞类型** | 三千万行代码中的任何内存安全或逻辑缺陷 | 局限于虚拟化边界 |

*差距是多个数量级，而非两倍。这正是 microVM 改变风险计算的原因。*

## 什么能提供真正的边界

**microVM** 让每个工作负载拥有**独立的内核实例**，运行在硬件强制的虚拟化之上，而不是通过命名空间共享主机内核。

这套技术栈有三个值得说明的层次：

- **CPU** 提供硬件机制，把一个内存区域与另一个区域隔离。
- **KVM** 将这些机制提供给 Linux 内核，让内核充当虚拟机监控程序。
- **VMM（虚拟机监控程序）**，如 Firecracker 或 QEMU，通过 KVM 创建并运行 guest。

由于 guest 运行自己的内核，**guest 内部的**内核漏洞利用程序只会危及 guest。攻击者没有共享内核可攻击。接下来攻击者必须逃出虚拟机监控程序本身，而 KVM 漏洞所在的攻击面更小。

实际应用中有两种重要实现，DepthFirst 的建议也都提到了：

| 技术 | 方法 | 说明 |
|---|---|---|
| **Firecracker** | 专用 VMM，设备模型精简 | 由 AWS 构建，专为大规模多租户隔离而设计 |
| **Kata Containers** | 包装 microVM 的 OCI 兼容运行时 | 在 VM 边界之上运行标准容器镜像 |

对多数团队来说，迁移到 Kata 更简单，因为它接受现有容器镜像和工具。**Firecracker 的攻击面更小**，因为相比通用 VMM，它实现的设备模拟少得多。

{{< figure src="microvm-vs-container-isolation-boundary.webp" alt="图示比较通过共享内核命名空间实现的容器隔离与 microVM 隔离。后者让每个工作负载在 KVM 和虚拟机监控程序上运行自己的内核" >}}

## 现在该怎么做

并非每个容器都需要 microVM。决策关键在于**谁会在容器内运行代码**。

| 你的情况 | 风险 | 建议 |
|---|---|---|
| **运行自己的代码**，单租户 | 低 | 保留容器。及时打补丁、移除 capabilities，并将根文件系统设为只读 |
| **多租户主机**，用户可使用 shell | **高** | 将不可信工作负载迁移到 microVM。这是 DepthFirst 首先指出的情况 |
| **运行不可信拉取请求的 CI 运行器** | **高** | 拉取请求中的代码会在运行器上获得 root 权限。将每项任务隔离到自己的 VM 中 |
| **Notebook、agent sandbox、serverless** | **高** | 租户代码会成为主机 root。每个租户使用一个 microVM |
| **Kubernetes 集群** | **较高** | 页缓存由主机共享。使用合适原语的 pod 会危及节点并跨越租户边界 |

共同原则很简单。**容器是优秀的打包和进程隔离工具。** 它们从来不是为阻止恶意代码而设计的，只因方便又便宜，业界便悄悄把它们用于此目的。

### 在任何情况下都有用的加固措施

这些措施都不能替代 VM 边界，但可以消除容易利用的路径：

```bash
# 不需要时，禁用 page-cache 家族滥用的模块
printf 'install algif_aead /bin/false\ninstall esp4 /bin/false\ninstall esp6 /bin/false\ninstall rxrpc /bin/false\n' \
  > /etc/modprobe.d/harden-pagecache-family.conf
rmmod algif_aead esp4 esp6 rxrpc 2>/dev/null || true
```

```bash
# 限制非特权用户命名空间，从而阻止 ESP 变体
# Debian 和 Ubuntu：这只是部分缓解措施，并非完整方案
sysctl -w kernel.unprivileged_userns_clone=0

# 怀疑遭到利用时，清空页缓存以丢弃内存中已修改的二进制文件
echo 1 | tee /proc/sys/vm/drop_caches
```

```text
# 初始检测信号
- 工作负载无正当理由地意外调用 unshare(CLONE_NEWUSER)
- IPsec 主机之外出现 NETLINK_XFRM 活动或 XFRM 安全关联
- 请求绑定 AF_ALG 套接字
- 未运行 IPsec 或 AFS 的主机加载 esp4、esp6 或 rxrpc
```

> **警告：`drop_caches` 会丢弃被修改的内存副本，从而清除损坏，但不能移除已经取得 root 的攻击者。应将其视为事件响应，而非修复措施。**

### 补丁节奏问题

即使尽了最大努力，内核打补丁也已变成一场竞赛：

- 今年发布近 **6,000 个 CVE**，仅数量就超过了大多数维护窗口的承受能力。
- **补丁会引入漏洞。** Fragnesia 已在这个子系统中证明了这一点。
- **缓解清单会过期。** 4月时 `algif_aead` 是答案。到了5月，它对 Dirty Frag 毫无帮助。

*快速打补丁既必要又不够。架构决定漏掉一个补丁后会导致可控事件还是主机失陷。*

## 更难的问题：对手是谁？

技术层面的答案很明确。战略层面的答案取决于多数团队忽略的一个问题。

**如果你的威胁模型是好奇的用户或粗心的开发者，容器仍然够用。** 容器逃逸需要本地代码执行和内核漏洞利用代码。两者都不轻松，把所有工作负载迁移到 microVM 的运维成本也是真实存在的。

**如果威胁模型包括能在你的基础设施上运行代码的对手，那么容器如今只是一个小障碍。** DepthFirst 的结论值得直接引用：

> “将这些漏洞武器化的门槛已大幅降低，因此我们必须假设攻击者已经能够随意逃逸标准容器。”

这是有产品要销售的安全供应商在为某种架构辩护，对其保持质疑是合理的。**不过，这一论点并不依赖供应商。** 6,000 个 CVE 的数字是公开的，漏洞利用代码已发布，而且内核在设计上就是共享的。

*坦率地说：对于已经进入系统的攻击者，容器作为边界的价值正在下降；对于其他威胁，其价值没有变化。*

## 结论

**容器仍然是打包、部署和进程分隔的合适工具，但它们已不再是抵御恶意代码的可靠安全边界。**

以下三项结论按可信度排序：

1. **技术前提已经明确。** 容器共享主机内核。本文中的四个漏洞都从无特权账户越过了边界，而且漏洞利用代码已公开。

2. **AI 改变了速度，而非原理。** 内核 LPE 一直存在。现在发现一个漏洞约需**一小时 AI 扫描**，而非数月专家工作；两家组织还在同一天独立发现了同一个零日漏洞。

3. **迁移有成本，不迁移也有成本。** Firecracker 和 Kata 会带来开销、运维复杂度和新技能要求。选择很直接：接受额外开销，或者接受内核漏洞会导致主机失陷。

**如果你运营多租户基础设施或执行不可信代码，现在就开始规划迁移到 microVM。** 不是因为灾难即将发生，而是趋势明确，而且迁移需要几个季度而非几个星期。

**如果你在单租户容器中运行自己的代码，就继续使用容器。** 比以往更快地为内核打补丁，禁用不需要的模块，并在引入不可信代码时重新评估方案。

*把内核视为无条件可信边界的时代正在结束。假定内核会被攻破并据此设计的基础设施，才能在入侵后存活。*

## 要点

- **容器共享主机内核。** 隔离来自 `clone` 系统调用的命名空间，而非硬件虚拟化，所以内核漏洞也会影响容器。
- **2026年的四个漏洞从无特权本地账户越过边界：** Copy Fail、Dirty Frag、Fragnesia 和 CVE-2026-80521。四者都攻击页缓存。
- **截至2026年9月，已发布近6,000个内核 CVE**，AI 工具加快了发现速度。**Copy Fail 只用了约一小时 AI 扫描就被发现。**
- **Dirty Frag 补丁引入了 Fragnesia。** 同一个子系统的补丁产生了一个新的 root 漏洞。
- **Copy Fail 的缓解措施挡不住 Dirty Frag。** 将 `algif_aead` 加入黑名单只能覆盖一个漏洞。
- **CVE-2026-80521 还影响了 `nsjail`、`Firejail` 和 `Bubblewrap`**，而不只是容器运行时。
- **microVM 改变了风险计算方式**，因为每个工作负载都有自己的内核。KVM 也有漏洞，但攻击面小得多。
- **根据谁运行代码来选择方案。** 单租户容器运行自有代码的风险较低；共享主机运行不可信代码则有主机失陷风险。

## 后续步骤

1. **阅读问题分析和已发布的漏洞利用程序：** **[容器不再是安全边界 - DepthFirst](https://depthfirst.com/research/containers-are-no-longer-safe)**
2. **查看 Copy Fail 系列的权威公告和缓解指导：** **[CERT/CC VU#260001](https://www.kb.cert.org/vuls/id/260001/)**
3. **阅读 Dirty Frag 技术分析**，了解漏洞链及 `algif_aead` 缓解为何失效：**[Dirty Frag 技术分析](https://github.com/V4bel/dirtyfrag)**
4. **查看 kvmCTF 规则和奖励等级**，了解虚拟机监控程序的攻击面：**[kvmCTF 概览](https://google.github.io/security-research/kvmctf/rules.html)**
5. **使用我们的浏览器端工具评估这些 CVE：** **[CVSS v3.1 计算器](/cvss-calculator/)**
6. **加固当前运行环境：** **[如何保护 Docker 和 Kubernetes 环境](/articles/how-to-secure-your-docker-and-kubernetes-environment/)**
7. **深入了解隔离取舍：** **[Docker 与虚拟机 2026](/articles/docker-vs-vms/)**
8. **无法添加边界时，降低权限：** **[Linux 最小权限访问控制](/articles/mastering-least-privilege-access-control-linux/)**

## 相关文章

| 文章 | 内容 |
|---|---|
| **[Docker 与虚拟机 2026](/articles/docker-vs-vms/)** | 本文所依据的架构比较，包括性能和安全取舍 |
| **[如何保护 Docker 和 Kubernetes 环境](/articles/how-to-secure-your-docker-and-kubernetes-environment/)** | 加固容器层的实用方法，在 microVM 内也值得采用 |
| **[Proxmox LXC 中的 Docker：可靠性、证据和迁移到 VM](/articles/docker-in-lxc-proxmox-reliability/)** | 容器嵌套、证据，以及何时将工作负载迁移到完整 VM |
| **[理解虚拟化：概念和应用](/articles/understanding-virtualization_-concepts-and-applications/)** | 虚拟机监控程序基础，包括 microVM 所依赖的 CPU 功能 |
| **[Linux 最小权限访问控制](/articles/mastering-least-privilege-access-control-linux/)** | 降低逃逸后获得的权限，从而限制影响范围 |

## 参考资料

1. [容器不再是安全边界 - DepthFirst（Zhenpeng Lin，2026年9月22日）](https://depthfirst.com/research/containers-are-no-longer-safe)
2. [CERT/CC Vulnerability Note VU#260001 - Copy Fail（CVE-2026-31431）](https://www.kb.cert.org/vuls/id/260001/)
3. [Copy Fail 官方披露网站和漏洞利用分析](https://copy.fail/)
4. [Dirty Frag 技术分析 - Hyunwoo Kim（CVE-2026-43284、CVE-2026-43500）](https://github.com/V4bel/dirtyfrag)
5. [Fragnesia：通过 ESP-in-TCP 在 Linux 内核中本地提升权限 - Wiz（CVE-2026-46300）](https://www.wiz.io/blog/fragnesia-linux-kernel-local-privilege-escalation-via-esp-in-tcp)
6. [kvmCTF 概览及奖励等级 - Google](https://google.github.io/security-research/kvmctf/rules.html)
7. [CVE-2026-31431 的 NVD 条目](https://nvd.nist.gov/vuln/detail/CVE-2026-31431)
8. [Copy Fail 的上游 mainline 修复提交](https://github.com/torvalds/linux/commit/a664bf3d603dc3bdcf9ae47cc21e0daec706d7a5)
9. [Ubuntu 关于 Copy Fail 修复的安全公告](https://ubuntu.com/blog/copy-fail-vulnerability-fixes-available)
10. [KernelCTF 漏洞利用代码与提交记录 - Google Security Research](https://github.com/google/security-research/tree/master/pocs/linux/kernelctf)
