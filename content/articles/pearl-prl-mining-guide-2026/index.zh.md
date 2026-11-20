---
title: "2026 年 Pearl (PRL) 挖矿指南：配置、收益与链的实用性"
date: 2026-09-22
lastmod: 2026-11-20
toc: true
draft: false
description: "使用 SRBMiner 配置 Pearl PRL 挖矿，了解有用工作量证明，估算利润并评估区块链的实际用途。"
genre: ["加密货币", "GPU 挖矿", "AI 计算", "DePIN", "区块链", "Linux", "家庭实验室", "硬件"]
tags: ["Pearl 挖矿", "PRL 挖矿", "Pearl PRL", "有用工作量证明", "PoUW", "NoisyGEMM", "SRBMiner Pearlhash", "Pearl 挖矿池", "LuckyPool Pearl", "2026 GPU 挖矿", "AI 计算加密货币", "Pearl Research Labs", "Nockchain 合并挖矿", "Nock 合并挖矿", "RTX 3070 挖矿", "SRBMiner 配置", "Linux 挖矿设备", "systemd 矿工服务", "矩阵乘法挖矿", "vLLM 矿工", "Pearl 钱包", "prl1 地址", "挖矿收益", "AI 计算挖矿", "加密货币挖矿指南", "NVIDIA 挖矿", "挖矿超频设置"]
cover: "/img/cover/pearl-blockchain-gpu-mining-matrix-multiplication-2026.webp"
coverAlt: "一幅现代 GPU 挖矿设备为 Pearl 区块链执行矩阵乘法的插图。深色背景上有动态数据流和鲜艳色彩。"
coverCaption: ""
ref: ["/other/efficient-spacemesh-mining-multiple-gpus-guide", "/articles/local-ai-2026-build-your-rig-now"]
---

**Pearl 是首个达到实际生产规模的有用工作量证明区块链。它奖励矿工执行矩阵乘法，而不是哈希运算。** 主网于 **2026 年 4 月 27 日**上线，几周内便引发 GPU 挖矿热潮，背后的主张是同一次运算既能保护区块链，也能产生 AI 计算结果。

*这一主张在技术上成立，但经济价值尚未得到证明。两者之间的差距就是本文要讨论的核心。*

本指南介绍如何挖 PRL、矿工计算什么、为何启动后利润率迅速下降，以及这条链是否创造了任何价值。

**读完后你将拥有：**一个钱包、经过验证的矿工、实测功耗，以及按你自己的电价计算的收益。把矿池估算值和上线初期收入视为某个日期的观察结果，而非购买保证。

## 简短回答

**Pearl 是一项真正的技术成果，同时也面临每种新币都会遇到的挖矿经济问题。**

| 问题 | 简短回答 |
|---|---|
| **它是什么？** | 一个源自 Bitcoin、由有用工作量证明保护的 L1 区块链。矿工执行带噪声的矩阵乘法，而不是 SHA-256 |
| **如何挖矿？** | 使用带 `--algorithm pearlhash` 参数的 SRBMiner-MULTI 连接矿池，或让 Pearl 自带的 vLLM 矿工连接自己的节点 |
| **为何曾经有利可图？** | 上线初期的排放量在数周内高于网络难度，之后难度追了上来 |
| **现在还有利可图吗？** | 取决于硬件，机会窗口正在缩小。请看下文的利润率分析 |
| **这条链有用吗？** | **机制有用，市场尚未形成。**详情请看结论 |

**搭建矿机前最该了解的一点：**矿工开发者在 3.6.8 版发布说明中表示，Pearl 即将升级，届时消费级 GPU 将“几乎无法用于挖矿”。这不是外部批评者的意见，而是矿工作者自己的判断。

## Pearl 是什么

Pearl 是由 **Pearl Research Labs** 构建的 L1 区块链。其代码仓库这样介绍项目：

> “Pearl 是一个基于有用工作量证明协议的 L1 区块链，挖矿是任意矩阵乘法的副产品。”

仓库包含完整节点、钱包守护进程、SPV 轻客户端、零知识证明系统和 GPU 矿工。项目采用**ISC 许可证**，许可宽松且无 copyleft。链的基础设施分叉自经过充分验证的 Bitcoin 项目：节点使用 **btcd**，钱包使用 **btcwallet**，轻客户端使用 **neutrino**。

**该设计有意借鉴 Bitcoin**，包括 **21 亿 PRL 的最大供应量**，正好是 Bitcoin 2100 万枚的 100 倍；区块奖励递减，出块时间约为两分钟。

*底层基础设施刻意保持保守。创新完全体现在工作函数上。*

### 什么是有用工作量证明

有用工作量证明是一个历史表现不佳的老想法。它的目标一直是用能顺带产出有价值结果的计算，取代 Bitcoin 刻意消耗资源的哈希运算。此前几乎所有尝试都因同一原因失败：“有用”工作并不真正有用，或者验证成本太高，无法低成本地保护区块链。

Pearl 通过名为 **NoisyGEMM** 的程序实现这一机制。矿工在 GPU 上执行带噪声的矩阵乘法，将结果哈希为承诺，再用**零知识证明**封装工作，让区块链能以较低成本验证。

该方案基于 Komargodski、Schen 和 Weinstein 于 2025 年发表的密码学论文 **《任意矩阵乘法的有用工作量证明》**。论文声称，相比朴素矩阵乘法，额外开销约为 **1 + o(1)**。这是整个项目的核心主张。如果保护区块链几乎不会增加基础计算的成本，那么这些计算几乎是免费产生的。

**这相当于一份投入、两份产出：一次 GPU 运算，两个结果。**

这项主张让 Pearl 区别于过去十年失败的 PoUW 概念。大多数方案都没有这样的开销界限。

{{< figure src="pearl-noisygemm-proof-of-useful-work-flow.webp" alt="示意图展示 Pearl 如何将 GPU 矩阵乘法转换为哈希承诺和零知识证明，并由区块链低成本验证" >}}

### 矿工实际计算什么

有两种挖矿方式，两者并不相同。

**官方方式**发布在 Pearl 自己的仓库中，包含两个组件：连接本地节点的 `pearl-gateway`，以及通过 vLLM 执行 GPU 计算的 `vllm-miner`。网关通过 JSON-RPC 与本地 `pearld` 节点通信，并通过 Unix 套接字或 TCP 端口 8337 提供挖矿接口。

**矿池方式**是大多数人的选择。SRBMiner-MULTI 通过 `pearlhash` 算法支持 Pearl，你只需将它指向矿池。

这一区别关系到“有用性”的论证。**官方矿工会加载真实的语言模型。**Pearl 文档示例在 Docker 中运行 `pearl-ai/Llama-3.3-70B-Instruct-pearl`，并直通 GPU。这是一个拥有 700 亿参数的模型，在保护区块链的同一次运算中提供推理服务。

*产生推理能力是真正的功能。没人购买的推理服务则是附带区块链的成本中心。请区分这两件事。*

## 为什么挖矿曾经有利可图，后来又变了

Pearl 初期的盈利并不神秘，也与 AI 无关。这是新币常见的发行曲线。

| 时间 | 发生的事情 |
|---|---|
| **2026 年 4 月 27 日** | 主网上线 |
| **2026 年 5 月下旬** | 网络启动五周后，GPU 挖矿热潮开始 |
| **2026 年 6 月** | 难度上升，RTX 5090 的估算日收入**大约减半** |
| **2026 年年中至年底** | 矿工软件效率大幅提高，部分抵消了收入下降 |

收入压缩的机制很直接：

1. **上线初期发行量大、难度低。**早期矿工每单位算力能获得更多奖励。
2. **奖励吸引算力。**更多 GPU 接入网络。
3. **难度随算力上升。**每块 GPU 的奖励下降。

Pearl 还有第二个下行因素：区块奖励按设计逐步减少。**收入有两个下跌原因，难度有一个上升原因。**

### 软件效率带来的反向作用

由于矿工不断提速，利润率并非一致下跌。SRBMiner 的 pearlhash 更新日志记录了效率提升：

| 版本 | Pearlhash 改动 |
|---|---|
| **3.6.1** | 新增 B300 支持。B300 SXM6 使用 `--gpu-cclock 1600` 时，报告约 **706 TH/s，功耗 920 W** |
| **3.6.2** | 改进 H100、H200 和 4000 系列 |
| **3.6.8** | 提高算力，主要针对 3000 系列 |
| **3.6.9** | **效率大幅提升。**多数架构以更低功耗获得相同或更高的算力 |

**对家庭矿工来说，电费是主要运营成本。**若新版本在保持算力的同时降低功耗，利润率就会直接改善，无需改变币价或网络难度。因此，6 月看起来勉强盈利的同一台矿机，到 9 月可能变得合理。

*效率提升确实有帮助，但这种优势不会持久，因为其他矿工也能获得同样的改进，并继续推高难度。*

## 等级惩罚软分叉

**2026 年 8 月 6 日**夜间，Pearl 激活了一次软分叉，时间约为 **UTC 02:00，区块 96251**。许多矿工直到第二天早上看到算力下降才知道发生了变化。

Pearl 协议有一个**噪声等级（rank）**参数。等级越高，相同工作量赢得头奖 的机会越大。**一些矿工故意使用高等级，以此获得不成比例的有效算力和奖励。**团队调查了其所称的异常挖矿优化，并引入惩罚机制。

| 规则变更 | 影响 |
|---|---|
| **最低允许等级** | 128 |
| **头奖上限** | 改为按公式 `128 / rank` 缩放 |
| **高等级的优势** | 完全取消 |

**对矿工的影响：**

- 等级高于 128 时，运营者损失了 **50% 至 87.5% 的有效算力**
- 等级为 128 或更低时，损失几乎为零

现在开始挖矿的人应记住两点。

**算力取决于软件和网络规则，不只取决于 GPU。**7 月表现良好的配置，可能并没有测出运营者以为的东西。

**网络规则改变时更新矿工。**旧版本可能效率明显下降，或无法按新规则正常工作。软分叉前矿池软件已更新，包括 PearlFortune v2.1.0 和 Krig (Kryptex) v1.1.0，以及 Tw-pearl-miner v3.3.0、Wildrig 0.49.8 等矿工。

*一次能削减最多 87.5% 奖励的软分叉，清楚说明了为什么要关注项目公告，而不只是查看支付面板。*

## Pearl 的两种挖矿方式

| | 矿池挖矿 | 官方 vLLM 矿工 |
|---|---|---|
| **软件** | SRBMiner-MULTI | `pearl-gateway` 和 `vllm-miner` |
| **算法** | `pearlhash` | 通过 vLLM 执行 NoisyGEMM |
| **是否需要节点** | 否 | **需要，且 `pearld` 必须同步完成** |
| **支付方式** | 矿池、PPLNS 或单人挖矿 | 直接发到你的挖矿地址 |
| **是否运行真实模型** | 否 | **是，例如 Llama-3.3-70B-Instruct** |
| **配置工作量** | 低 | 高，需要 CUDA 工具包和 Python 3.12 |
| **适合用途** | 快速接入网络并获得算力 | 直接向网络贡献计算资源 |

**从矿池挖矿开始。**它不需要节点、同步或下载模型，几分钟内即可获得算力并设置收款地址。只有在你确实想提供推理服务或运行节点时，再考虑官方矿工。

{{< figure src="pearl-mining-pool-vs-vllm-miner-comparison.webp" alt="对比 SRBMiner 矿池挖矿和官方 vLLM 矿工的示意图，展示两种方式所需的节点、网关和推理组件" >}}

## 消费级 GPU 的硬件说明

Pearl 的特点之一是要求低。Hashrate Index 指出，其硬件需求**异常轻：内存、存储和 CPU 要求低，也不需要真实训练集群所需的昂贵多光纤网络。**一位分析师称它“很适合利用闲置设备”。

这才是它的实际吸引力。**现有 GPU，包括较旧型号，也能带来一些收入。**

| GPU 类别 | 观察 |
|---|---|
| **RTX 5090 和 4090** | 单卡收入最高，也是早期收入减半数据所涉及的类别 |
| **RTX 3000 系列** | 3.6.8 版本的算力提升主要针对该系列。仍有可行性，但效率比原始速度更重要 |
| **数据中心加速卡** | H100、H200 和 B300 在 2026 年加入并得到优化。算力竞争正朝这个方向发展 |
| **较旧或显存较小的卡** | 利润空间有限。投入设备前先查看实时收益计算器 |

**2026 年每次发布都呈现相同规律。**团队先加入并优化旗舰加速卡，因为它们的算力价值最高。消费级显卡得到关注，是在 3000 系列还有提升空间时。

*调整效率比追求频率更能增加收入。这与大多数挖矿指南的说法相反。*

## 在 Linux 上配置

矿池挖矿需要四样东西：SRBMiner 二进制文件、Pearl 钱包地址、矿池端点，以及一个保持其运行的服务。

### 先获取钱包地址

Pearl 挖矿地址以 **`prl1`** 开头。官方钱包是 **Oyster**，它是 Pearl 仓库中的 HD 钱包守护进程，提供 JSON-RPC 和 gRPC 接口。用它生成一个 **Taproot** 挖矿地址。

不要跳过这一步，也不要重复使用其他链的地址。**奖励发到你无法控制的地址后就无法找回。**

### 矿池、端口和合并挖矿

Pearl 最大的矿池是 LuckyPool，提供按预期算力分级的端口：

| 端口 | 起始难度 | 建议算力 |
|---|---|---|
| **3360** | 2M | 低于 500 TH/s |
| **3361** | 4M | 500 至 1000 TH/s |
| **3362** | 8M | 高于 1000 TH/s |

选择与你矿机实际算力相匹配的端口。**单张消费级 GPU 应使用 3360。**小型矿机接入高难度端口会导致很久才提交一次 share，增加收益波动，却没有任何好处。

矿池有两个值得了解的功能：

- **单人挖矿**可以在任意端口使用，只需在钱包地址前加 `solo:`。找到区块时获得全部奖励，找不到就没有收入。消费级算力可能要等待很久。
- **Nockchain 合并挖矿**可以在相同算力下同时获得 NOCK 和 PRL，方法是在 Pearl 钱包后添加 `+NOCK_ADDRESS`。矿池在 Nockchain 本身支付 NOCK，因此以 `0x` 开头的封装代币地址无法收款。**你的矿工必须支持合并挖矿；不支持时仍可照常挖 Pearl。**

矿池提供 `luckypool.io` 主机和 `lproute.com` 路由主机。如果网络阻止直接的挖矿流量，保留端口并更换域名。

## 可用的安装脚本

下面的脚本会在 Debian 或 Ubuntu 主机上将 SRBMiner 配置为 systemd 服务。它会检测所有 GPU、为每张卡应用超频参数、使用公开的 MD5 校验下载、写入 unit 文件和 logrotate 策略，然后重启服务。

```bash
#!/usr/bin/env bash
# install-pearl-miner.sh -- 将 SRBMiner (Pearl / PRL) 配置为 systemd 服务。
# 运行：sudo bash install-pearl-miner.sh
set -euo pipefail

ALGO="pearlhash"
POOL="${POOL:-pearl-us-east.luckypool.io:3360}"
WALLET="${WALLET:-<YOUR_PR1_ADDRESS>}"   # prl1... 添加 +NOCK_ADDRESS 以进行合并挖矿
WORKER="${WORKER:-rig-1}"
SRB_VERSION="${SRB_VERSION:-3.6.9}"
MINER_DIR="/opt/srbminer"
UNIT="/etc/systemd/system/pearl-miner.service"
SVC="pearl-miner.service"
LOG="/var/log/pearl-miner.log"

# RTX 3070 类显卡的设置。MCORE 将内存频率固定在远低于默认值的位置，
# 默认值为 7001 MHz。这是为了提高能效而降频，并非为了提升性能而超频。
# 将任意参数设为 "" 可关闭此选项。
CCLOCK="${CCLOCK:-1560}"
MCLOCK="${MCLOCK:-5001}"
COFFSET="${COFFSET:-150}"
PLIMIT="${PLIMIT:-180}"
FAN="${FAN:-}"
THERMAL="${THERMAL:-88}"
```

这个调节区块值得说明，因为乍看之下似乎不合理。**`MCORE=5001` 低于 3070 的默认内存频率。**这是有意为之。Pearl 奖励内存效率，降低内存频率节省的功耗大于它损失的算力。**不要照搬算力数据库中的超频数据，先确认测试使用的 GPU 型号。**测试数据经常来自与你机器不同的显卡。

```bash
[ "$(id -u)" -eq 0 ] || { echo "请以 root 身份运行 (sudo)"; exit 1; }
command -v nvidia-smi >/dev/null || { echo "缺少 nvidia-smi，请先安装驱动"; exit 1; }

GPU_N=$(nvidia-smi --query-gpu=index --format=csv,noheader | wc -l)
echo "== 已检测到 $GPU_N 个 NVIDIA GPU =="
nvidia-smi --query-gpu=index,name,memory.total,power.limit --format=csv,noheader

# 为检测到的每张 GPU 创建一组超频参数
OC=""
for i in $(seq 0 $((GPU_N - 1))); do
    [ -n "$COFFSET" ] && OC="$OC --gpu-coffset$i $COFFSET"
    [ -n "$CCLOCK" ]  && OC="$OC --gpu-cclock$i $CCLOCK"
    [ -n "$MCLOCK" ]  && OC="$OC --gpu-mclock$i $MCLOCK"
    [ -n "$PLIMIT" ]  && OC="$OC --gpu-plimit$i $PLIMIT"
    [ -n "$FAN" ]     && OC="$OC --gpu-fan$i $FAN"
done
THERMAL_ARG=""
[ -n "$THERMAL" ] && THERMAL_ARG=" --shutdown-temperature $THERMAL"

# 下载并验证发布包
STEM="SRBMiner-Multi-$(echo "$SRB_VERSION" | tr . -)-Linux"
BASE="https://github.com/doktor83/SRBMiner-Multi/releases/download/$SRB_VERSION"
TMP=$(mktemp -d); trap 'rm -rf "$TMP"' EXIT
curl -fsSL -o "$TMP/$STEM.tar.gz"  "$BASE/$STEM.tar.gz"
curl -fsSL -o "$TMP/$STEM.tar.md5" "$BASE/$STEM.tar.md5"
(cd "$TMP" && md5sum -c <(tr -d '\r' < "$STEM.tar.md5"))

# 替换进程正打开的二进制文件前先停止服务
systemctl stop "$SVC" 2>/dev/null || true
tar -xzf "$TMP/$STEM.tar.gz" -C "$TMP"
SRC=$(find "$TMP" -maxdepth 1 -type d -name 'SRBMiner-Multi-*' | head -1)
mkdir -p "$MINER_DIR"
[ -f "$MINER_DIR/SRBMiner-MULTI" ] && \
    cp -a "$MINER_DIR/SRBMiner-MULTI" "$MINER_DIR/SRBMiner-MULTI.bak-$(date +%F-%H%M%S)"
cp -a "$SRC"/. "$MINER_DIR"/
chown -R root:root "$MINER_DIR"
chmod 755 "$MINER_DIR/SRBMiner-MULTI"
```

**运行任何挖矿二进制文件前都要验证 MD5。**发布包会提供每个文件的哈希值，而矿工会以 root 权限访问你的 GPU。跳过校验，就等于信任一个你从未检查过的下载文件。

服务 unit 文件中有两个运行细节：

```bash
cat >"$UNIT" <<EOF
[Unit]
Description=Pearl (PRL) SRBMiner 矿工 v$SRB_VERSION - $WORKER
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=$MINER_DIR
ExecStart=$MINER_DIR/SRBMiner-MULTI --algorithm $ALGO --pool $POOL --wallet $WALLET --worker $WORKER --disable-cpu --gpu-reset-oc$OC$THERMAL_ARG --api-enable --api-port 21550 --api-rig-name $WORKER
Restart=always
RestartSec=10
StandardOutput=append:$LOG
StandardError=append:$LOG
LimitNOFILE=65536

[Install]
WantedBy=multi-user.target
EOF
```

- **`--disable-cpu`** 禁止矿工使用 CPU，这对还要执行其他任务的机器很重要。
- **`--shutdown-temperature 88`** 会在风扇故障时停止矿工，避免显卡过热。
- **`--gpu-reset-oc`** 会先清除之前的频率设置再应用新设置，避免沿用旧配置。
- **`Restart=always` 配合 `RestartSec=10`** 可以应对驱动短暂故障，这种情况在多 GPU 矿机上很常见。
- **`--api-enable` 会开放监控端口。**确认 21550 端口绑定到哪个网络接口，并避免暴露给不可信网络。矿机监控端点无需从设备外部访问。

最后配置日志轮转，因为挖矿日志会不断增长：

```bash
cat >/etc/logrotate.d/pearl-miner <<EOF
$LOG {
    weekly
    rotate 4
    compress
    delaycompress
    missingok
    notifempty
    copytruncate
}
EOF

systemctl daemon-reload
systemctl enable "$SVC" >/dev/null 2>&1 || true
systemctl restart "$SVC"
```

*这里的 `copytruncate` 很重要。SRBMiner 会一直打开日志文件。如果轮转时重命名文件，矿工仍会写入已删除的 inode，磁盘最终还是会被占满。*

使用筛选后的日志尾部查看进度，不要直接输出原始日志：

```bash
grep -aE 'Hashrate|accepted|Pool:' /var/log/pearl-miner.log | tail -20
```

## 出现过的问题

**Pearl 挖矿指南必须先谈问题，因为每个问题都会影响你的收益。**2026 年 7 月到 9 月间发生了四件事。

### 市场几乎只依赖一家交易所

**2026 年 7 月 23 日**，PRL 跌至历史低点 **0.1399 美元**，6 月时价格约为 **0.87 美元**。一天跌了 **24.2%**，一周跌了 **26.7%**，同期更广泛的加密市场约上涨 2%。

原因不是新闻，而是市场深度。

- **全部报告交易量的 95.17%** 集中在 **一家名为 SafeTrade 的交易所**，CoinGecko 没有为其评定信任分数。一个 PRL/USDT 交易对占了 24 小时约 **775,000 美元成交额中的 738,399 美元**。
- SafeTrade 的两个交易对都显示**订单簿深度为 0.00 美元**。

*在这种市场里，一张普通卖单就能让价格变动两位数。这是代币的结构性问题，不是暂时现象。*

供应分布让问题更严重：

| 指标 | 数值 |
|---|---|
| **市值** | 5,570 万美元 |
| **完全稀释估值** | 4.586 亿美元 |
| **比例** | 超过 8 倍 |
| **流通供应量** | 21 亿枚中的 2.55 亿枚，不到 **13%** |

**一种代币若只在一本浅薄的订单簿上定价，且 87% 的供应仍被锁定或尚未发行，可能的价格范围就很大。**提前考虑如何处理矿池付款，不要把现货价格当作可靠的收入估值。

### 一个矿池遭到入侵

**2026 年 9 月 18 日**创建的 issue 称，Pearl 钱包 2.0.5“在一个月前矿池遭到攻击后，仍暂停发送和接收”。

**这句话里有两个事实。**Pearl 矿池在 **2026 年 8 月前后**遭到入侵，官方钱包随后暂停了转账。一个月后，转账仍未恢复。

你选择的矿池会保管你的付款。连接矿机前先查看它的安全事件记录。

### 项目网站无法访问

撰写本文时，**pearlresearch.ai 无法连接到任何服务器。**所有公共 DNS 解析器对根域名和 `compute`、`explorer` 等子域名都返回空路由 `0.0.0.0`。域名注册状态显示为 `ACTIVE`，所以这是有意设置的 DNS 状态，而非域名过期。

**挖矿指南通常会提供的三个链接都已失效**，其中包括区块浏览器。Mining Pool Stats 仍列出这些链接，因此读者会不断尝试打开一个永远无法加载的地址。

区块查询请使用 **[prlscan.com](https://prlscan.com)**。我确认该页面可以正常访问。

### 软件仍有未解决的错误

截至 2026 年 9 月下旬，公开 issue 跟踪器仍列有未解决的问题。创建 issue 受到限制，因此以下信息并不完整。

| 问题 | 日期 | 影响 |
|---|---|---|
| **桌面钱包的 RPC 代码未启用** | 9 月 22 日 | 钱包无法连接节点 |
| **测试网无法从头同步**，节点卡在高度 36760 | 9 月 22 日 | 同步逻辑有阻断性缺陷 |
| 矿池遭攻击后，**钱包发送和接收仍暂停** | 9 月 18 日 | 转账受影响 |
| **macOS ARM64 版本的代码签名无效** | 9 月 17 日 | 不绕过 Gatekeeper 就无法运行 |
| **Prune 模式会丢弃验证区块头所需的证书** | 8 月 30 日 | 验证缺陷 |
| **当连接的 peer 都无法用于同步时，节点会无限期卡住** | 8 月 30 日 | 同步可靠性差 |
| **`pearl-gemm` 无法在 RTX 5070 上运行**：哈希内核正常，但 GEMM 内核失败 | 8 月 31 日 | 最新消费级显卡不受支持 |

*如果你打算为此购买新显卡，应特别留意 RTX 5070 这一项。最新消费级架构无法运行官方 GEMM 路径。*

**总的来说：**挖矿软件仍在积极维护，但用户体验和市场层面较弱。SRBMiner 在有关钱包的投诉出现前一天，刚发布具有重大效率改进的 3.6.9 版。

## 这条链有用吗？

这个问题需要谨慎回答，因为很多报道中的“有用工作”同时指两件事。**它既描述共识机制，也表达经济主张，而这两件事的答案截然不同。**

### 功能层面：部分有用

**网络在运行。围绕它的产品尚未完全可用。**

运行正常的部分：

- **主网于 2026 年 4 月 27 日上线**，此后一直在产出区块。
- **完整软件栈确实存在**：一个节点、一个钱包守护进程、一个 SPV 轻客户端、一个零知识证明系统和一个 GPU 矿工都在同一仓库中。
- **基础设施在代码层面经过验证。**节点、钱包和轻客户端分叉自 **btcd**、**btcwallet** 和 **neutrino**，这些 Bitcoin 项目经历了多年对抗性测试。
- **代码库投入了大量工作。**它有 315 个星标、76 个 fork、超过 6,800 次提交，并设有公开跟踪器，贡献者会提交具体的缺陷报告。
- **挖矿部分正常。**SRBMiner 发布过 247 个版本，多次优化 `pearlhash`。多个矿池在运营，Nockchain 合并挖矿也可用。

存在问题的部分：

- 矿池遭攻击后，**官方钱包暂停了转账**。
- 截至 9 月下旬，**桌面钱包无法连接节点**，这是项目自己的跟踪器所显示的情况。
- **测试网和主网的同步逻辑都有阻断性缺陷**。
- **项目网站无法访问**。
- **最新消费级 GPU 无法运行 GEMM 路径**。

**坦率地说，Pearl 在协议层面可用，在产品层面却不可靠。**研究有用工作量证明的人值得关注它。期待稳定挖矿并按时收款的人应把这些问题视为警告。

### 技术上有用吗：机制有用，市场没有

诚实的答案分为两部分。很多报道的问题就在于把两部分混为一谈。

**这一机制确实新颖。**Pearl 的 NoisyGEMM 在 GPU 上执行带噪声的矩阵乘法，将结果哈希为承诺，再加入零知识证明以保持低验证成本。它基于一篇真实论文《任意矩阵乘法的有用工作量证明》，作者为 Komargodski、Schen 和 Weinstein。论文声称，相比朴素矩阵乘法，额外开销约为 **1 + o(1)**。

**如果这一界限成立，保护区块链所需的额外计算成本几乎为零。**此前的 PoUW 尝试都没有做到这一点。这套数学不是装饰。

**市场尚未建立。**Hashrate Index 直接指出：“如今大多数有用工作是无人购买的推理服务，因此当前大部分挖矿都只是带有 AI 外形的工作量证明。”这是公允的总结。计算形式是对的，但大多数计算都无人付费。

有一个真实且重要的例外。Pearl 与 **Together AI** 达成独家合作，将折扣版 Pearl 推理端点投入生产。这是第一个客户，也让该项目比普通的 AI 概念币更值得关注。

**一个客户能验证概念，但形不成市场。**

### 实际上有用吗：暂时有用，但窗口正在关闭

对矿工来说，实际情况喜忧参半，而且机会有时限。

**有利于 Pearl 的因素：**

- 由于硬件要求低，现有 GPU，包括旧卡，也能产生一些收入
- 矿工效率持续提升，可直接改善你已有硬件的利润率
- Nockchain 合并挖矿能用相同算力增加第二种收入
- 额外开销接近于零，链不会把电力浪费在无意义的哈希上

**不利因素：**

- **区块奖励按设计递减。**这是 Bitcoin 的模式，无论币价是否上涨，排放都会减少。
- **难度只会上升。**每块 GPU 的收入只能朝一个方向变化。
- **流动性较差。**Hashrate Index 将 PRL 是否能在小型交易所以外获得流动性列为观察事项。流动性不足会带来更大的价差和更差的实际成交价。
- **协议升级。**SRBMiner 3.6.8 的发布说明称，Pearl 的一次后续升级将令消费级 GPU“几乎无法用于挖矿”。请认真对待这个说法，它来自一位希望人们继续挖矿的开发者。

## 结论

**Pearl 是迄今最可信的有用工作量证明实现，但它尚未证明其工作在经济意义上有用。**

以下四点按可信度排序：

1. **共识机制有效，密码学主张也是真实的。**Pearl 解决了让 PoUW 低成本验证这一技术难题。无论代币将来如何，这都是实质贡献。

2. **计算能力目前只是承诺，并非成熟产品。**提供推理服务不等于卖出推理服务。如今付费份额只有一个合作方，网络中却充满投机算力。增长飞轮已经设计好，但还没有转起来。

3. **消费级 GPU 挖矿的窗口正在缩小，协议升级会彻底关闭它。**奖励下降、难度上升、计划中的升级将消除消费级 GPU 的可行性，以及一次已令部分矿工有效算力下降最多 87.5% 的软分叉，共同构成了限时机会，而非稳定收入来源。

4. **真正风险在运营和市场层面，不在密码学。**矿池遭攻击、钱包转账暂停、网站无法访问、同步缺陷未解决，以及 95% 的交易量集中在一家没有订单簿深度的交易所，这些因素决定挖矿能否兑现收入。协议反而是可靠的部分。

*最直接地说：Pearl 解决了难题，却还没解决看似简单的问题。用密码学证明矩阵乘法有用是一回事，为计算结果找到买家则是销售问题。*

**如果你来挖矿，就把它当作短期利用现有硬件的方式。**不要为了 Pearl 买 GPU，也不要认为当前数据会持续，因为排放计划和矿工开发者的发布说明都表明情况不会如此。

**如果你想研究有用工作量证明，Pearl 是目前最值得研究的实现。**它是首个达到实际规模的项目，未来两年的证据将显示“有用工作”究竟是一种真正的基础机制，还是一种采用了更好密码学的反复失败方案。

{{< figure src="pearl-prl-usefulness-assessment.webp" alt="图示从三个维度评估 Pearl 有用工作量证明：功能成熟度较高，技术机制强但付费市场尚未证明，实际挖矿可行性受时间限制" >}}

## 重点总结

- **Pearl 是源自 Bitcoin、由有用工作量证明保护的 L1 区块链**，矿工执行带噪声的矩阵乘法而不是哈希运算。主网于 **2026 年 4 月 27 日**上线。
- **有两种挖矿方式：**使用带 `--algorithm pearlhash` 参数的 SRBMiner 连接矿池，或让 Pearl 的 `vllm-miner` 连接已同步的节点。
- **早期收益来自上线发行曲线**，并非 AI 需求。挖矿热潮开始后几周内，RTX 5090 的估算日收入约减半。
- **矿工效率更新部分抵消了收入下降。**3.6.9 版以明显更低的功耗实现相同或更高算力。
- **2026 年 8 月 6 日的 等级惩罚软分叉令 等级高于 128 的矿工有效算力下降 50% 至 87.5%。**网络规则变更时更新矿工。
- **代币流动性几乎只来自一家交易所。**SafeTrade 占 95.17% 的交易量，订单簿深度为零，流通供应不足 13%。
- **2026 年 8 月前后有矿池遭到攻击**，官方钱包的转账一个月后仍处于暂停状态。
- **项目网站无法解析。**区块查询请改用 `prlscan.com`。
- **优先调整效率，而不是频率。**Pearl 奖励内存效率，降低内存频率节省的功耗大于它损失的算力。
- **单张消费级 GPU 使用 3360 端口**，并添加 `+NOCK_ADDRESS` 以合并挖 Nockchain。
- **运行矿工前验证 MD5**，尤其是在以 root 权限启动之前。
- **使用已有硬件挖矿。**该链在协议层面能运行，在产品层面不可靠，付费计算市场也仅有一个合作方。

## 后续步骤

1. **查看节点、钱包和官方 vLLM 矿工的源码仓库：** **[pearl-research-labs/pearl](https://github.com/pearl-research-labs/pearl)**
2. **调整参数前先查矿工更新日志**，不同版本的效率会变化：**[SRBMiner-Multi 发布版本](https://github.com/doktor83/SRBMiner-Multi/releases)**
3. **选择与实际算力匹配的矿池端口：** **[LuckyPool Pearl](https://pearl.luckypool.io)**
4. **决定前比较各矿池算力分布：** **[Pearl 矿池统计](https://miningpoolstats.stream/pearl)**
5. **先估算电费**，因为它决定挖矿能否盈利：**[搭建有利可图的低功耗被动收入设备](/other/creating-profitable-low-powered-crypto-miners/)**
6. **参考另一篇有用工作量挖矿指南，调整多 GPU 设备：** **[高效使用多 GPU 挖 Spacemesh](/other/efficient-spacemesh-mining-multiple-gpus-guide/)**

## 相关文章

| 文章 | 内容 |
|---|---|
| **[高效使用多 GPU 挖 Spacemesh](/other/efficient-spacemesh-mining-multiple-gpus-guide/)** | 另一种有用工作量区块链的多 GPU 调优和功耗管理 |
| **[搭建有利可图的低功耗被动收入设备](/other/creating-profitable-low-powered-crypto-miners/)** | 购买前根据电费确定挖矿设备规格 |
| **[2026 年本地 AI：27B 模型击败 Sonnet 4.6](/articles/local-ai-2026-build-your-rig-now/)** | 同一批 GPU 用于本地推理而非挖矿时能做什么 |
| **[在 Android 上挖 Verus：手机挖矿入门指南](/other/mine-verus-on-android-guide/)** | 使用已有设备进行 CPU 挖矿 |

## 参考资料

1. [pearl-research-labs/pearl - 网络单体仓库](https://github.com/pearl-research-labs/pearl)
2. [pearl-research-labs/pearl - 未解决的问题](https://github.com/pearl-research-labs/pearl/issues)
3. [Pearl (PRL)：矩阵数学如何将 AI 计算转为挖矿 - Hashrate Index](https://hashrateindex.com/blog/pearl-prl-ai-compute-cryptocurrency/)
4. [Pearl (PRL) 网络激活 等级惩罚软分叉 - Cryptoage](https://cryptoage.com/en/5400-rank-penalty-softfork-activated-on-the-pearl-prl-network.html)
5. [Pearl 创下历史新低 - CryptoNewsLive](https://www.cryptonewslive.org/article/pearl-hit-a-fresh-all-time-low-today-95-of-its-volume-sits-on-one-exchange-with-zero-order-book-depth)
6. [SRBMiner-Multi 发布版本 - doktor83](https://github.com/doktor83/SRBMiner-Multi/releases)
7. [LuckyPool - Pearl 与 Nock 合并挖矿池](https://pearl.luckypool.io)
8. [挖矿池统计 - Pearl (PRL) PearlHash](https://miningpoolstats.stream/pearl)
9. [prlscan.com - PRL 区块浏览器](https://prlscan.com)

**关于官方域名的说明：**撰写本文时，`pearlresearch.ai` 及其 `compute`、`explorer` 子域名都返回空路由。本文有意省略这些地址，避免提供失效链接，并改用 `prlscan.com` 查询区块。
