---
title: "Flock 摄像头检测竞赛：2026 年发生了什么变化"
date: 2026-09-10
lastmod: 2026-11-14
toc: true
draft: false
description: "了解 Flock Safety 检测方式的变化、社区的应对，以及用于识别摄像头系统的红外方案。"
genre: ["隐私技术", "反监控", "开源项目", "数字权利", "网络安全", "安全研究", "硬件改造", "隐私工具"]
tags: ["Flock Safety", "ALPR", "Flock-You", "OUI 检测", "通配 Probe 请求", "WiFi 混杂模式", "802.11 监测", "DeFlockJoplin", "NitekryDPaul", "BLE 检测", "5GHz WiFi", "本地管理 MAC 地址", "SSID 模式匹配", "反监控硬件", "STS Collective", "colonelpanichacks", "规避检测", "ESP32", "WiFi 检测", "监控意识", "OUI-SPY", "M5 Atom Lite", "Flock Finder", "GitHub 问题跟踪", "固件更新", "设备数字指纹防护", "MAC 随机化", "信息元素指纹识别", "信道跳转", "隐私倡导", "开源安全", "大规模监控", "检测固件", "无线巡测", "拆除摄像头", "隐私硬件", "红外检测", "IR 照明器", "ESP32-CAM", "Seeed Studio XIAO ESP32S3 Sense", "Quectel L76K", "光学检测", "Valleytech Custom Solutions"]
cover: "/img/cover/flock-camera-detection-techniques-2026.webp"
coverAlt: "城市街景中，Flock 摄像头安装在路灯杆上，一辆车配有先进检测设备。发光信号在深色背景中表示无线数据通信。"
coverCaption: "Flock Safety 的硬件变化如何持续打断开源检测工具，以及社区如何跟上变化"
canonical: "https://simeononsecurity.com/articles/flock-camera-detection-arms-race-2026/"
---

**如果你的 Flock-You 检测器在一条过去总能发现摄像头的路线突然变得毫无反应，你没有看错，硬件也很可能没有损坏。**过去一年，Flock Safety 摄像头的硬件和固件至少变化了两次，导致社区的检测方式失效。开源研究人员每次都不得不对新的特征进行逆向分析。

*这件事仍在快速发展。以下检测方法和 OUI 列表反映的是 `colonelpanichacks/flock-you` 仓库截至 2026 年 9 月的 `main` 分支。假设设备损坏前，请先查看 [GitHub 仓库](https://github.com/colonelpanichacks/flock-you)。*

{{< youtube id="cVf-id71BuQ" >}}

*上面这段 Valleytech Custom Solutions 视频记录了本文讨论的症状：一次常规无线巡测突然在多个固件版本上都没有任何检测结果。此前这条路线一直能可靠发现摄像头，而同一县内几台先前标记的摄像头已从杆上被实际拆除。*

______

## 一次巡测突然什么也没发现

几乎所有报告都描述了同一种情况。驾驶者走一条已经走过几十次的路线。检测器运行最新固件，过去曾发现同一批摄像头。但有一天，它什么也没检测到。尝试过的所有自定义固件版本都没有提示音，也没有日志记录。

上面 Valleytech 的视频正是这种情况：一条日常邮局路线过去总能记录至少一台 Flock 摄像头，现在一台也没有。另一条经过 Micro Center 的路线过去会标记五台摄像头，现在只显示一台仍在工作，另外四台已从杆上被实际拔除。

**同一时期发生了两件事，很容易混为一谈：**

- **有些地区的摄像头被实际拆除或迁移，**这确实减少了可检测设备的数量。
- **摄像头广播的无线特征发生了变化，**因此即便摄像头仍在杆上，运行旧固件的检测硬件也不会触发。

`colonelpanichacks/flock-you` 仓库中两个相隔数月提交的 GitHub 问题详细记录了第二种情况。按顺序阅读，就能了解社区为何已经两次改进检测方法。

______

## Issue #20：管理接入点消失

**[Issue #20](https://github.com/colonelpanichacks/flock-you/issues/20)** 于 2026 年 1 月开启，起因是一个熟悉的问题：用户把设备放在 DeFlock 上登记的一台已知 Flock 摄像头旁测试，却什么也没发现。之后数周，佛罗里达、印第安纳、亚特兰大和中西部的更多用户，用不同硬件和天线报告了相同结果。

有位评论者提出了后来最关键的问题：**Flock 是否在自家系统上做了某种改动，导致所有人的检测方法大致同时失效？**

项目维护者 colonelpanichacks 最终确认确实如此。**大约在 2025 年 12 月，Flock 停用了摄像头曾广播的管理接入点。**该 AP 原本是无线检测的基础。它消失后，社区改用低功耗蓝牙（BLE）信号作为替代方案。但到 2026 年春季，这种替代方式也不再可靠。

| 检测面 | 状态 |
|---|---|
| **管理 WiFi AP** | Flock 大约在 2025 年 12 月停用 |
| **BLE 广播** | 2026 年春季起不再可靠 |
| **蜂窝 LTE 上行链路** | 仍用于向云端上传，但无法被被动检测 |
| **通配 802.11 Probe 请求** | 当前检测基础（见下文） |

*所有基于旧 AP 或 BLE 检测路径的自定义固件现在都在寻找摄像头已停止发送的信号。这就是原本能用的设备突然完全沉默，而硬件本身并未损坏的原因。*

______


## 替代方法：通配 Probe 与帧指纹识别

当前 `flock-you` 固件在专用 802.11 混杂模式下运行。无线电从不发射，也不会加入任何网络。它只监听 WiFi 11、6 和 1 信道，并在每个信道停留 250 毫秒，以跟上摄像头自身的信道切换速度。

**现在，固件只有在以下条件全部满足时才会发出检测提示：**

1. 帧是 802.11 **管理 Probe 请求**（类型 0，子类型 4）。
2. **SSID 信息元素存在且长度为 0**，即它是通配 Probe，而非请求特定网络。
3. 发送方地址（**addr2**）匹配一个已知 Flock OUI 前缀。
4. 帧中其余信息元素匹配 DeFlockJoplin 社区记录的指纹模式，该模式基于 Pintor 和 Atzori 于 2022 年发表的 **[WiFi Probe 请求 IE 指纹识别研究](https://ieeexplore.ieee.org/document/10001618)**。

固件将此方法命名为 `wifi_wildcard_probe_ie_sig`。DeFlockJoplin 社区的实地测试沿测试路线发现了 **12 台已知摄像头中的 11 台，只有 2 次误报**。这与项目自身 **[硬件指南](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/)**引用的实地验证基准一致。第 12 台摄像头使用的 OUI 后来已加入下方列表。

{{< figure src="flock-detection-arms-race-timeline-2026.webp" alt="时间线图展示 Flock 摄像头检测从管理 WiFi 接入点、Bluetooth Low Energy 广播，发展到当前的通配 Probe 请求与信息元素指纹识别，并显示第四阶段的新 SSID、5GHz 和 MAC 地址规避方式" >}}

______

## 当前 OUI 列表

只有当发送方 MAC 地址匹配社区在真实 Flock 硬件上确认过的 OUI 前缀时，上述通配 Probe 指纹才会触发。研究人员 **@NitekryDPaul** 主要维护该列表。**DeFlockJoplin** 社区发现一台原先 30 项列表中没有的摄像头，因此贡献了第 31 项。

```text
70:c9:4e  3c:91:80  d8:f3:bc  80:30:49  b8:35:32
14:5a:fc  74:4c:a1  08:3a:88  9c:2f:9d  c0:35:32
94:08:53  e4:aa:ea  f4:6a:dd  f8:a2:d6  24:b2:b9
00:f4:8d  d0:39:57  e8:d0:fc  e0:4f:43  b8:1e:a4
70:08:94  58:8e:81  ec:1b:bd  3c:71:bf  58:00:e3
90:35:ea  5c:93:a2  64:6e:69  48:27:ea  a4:cf:12
82:6b:f2
```

**此列表并非固定不变。**上游研究记录了若干经过测试后被降级的前缀。一个后来被确认属于 Sony 媒体播放器，另一个是早期占位符，从未匹配到任何设备。两项标记为低可信度。`82:6b:f2` 虽是本地管理地址，仍被特意保留，因为将它过滤掉会悄悄丢弃 DeFlockJoplin 确认过的真实检测结果。

**其中一项现已得到市政在用摄像头的独立硬件确认。**2026 年 9 月公开其文件系统映像的 Flock 设备使用 MAC 地址 **`f4:6a:dd:57:46:fb`**，`f4:6a:dd` 在该列表中排第 13 位。这不是实验室设备，也不是购买的样品。它安装在 Wisconsin 州 Wauwatosa 的杆上并拍摄交通，因此这是列表中某个前缀收到的最有力单项确认。

*如果你维护自己的固件分支，请从上游 `datasets/` 目录拉取 OUI 列表，而不要硬编码一份副本。列表会随研究更新，旧副本会让你逐渐、悄无声息地漏掉摄像头。*

______

## 检测信号排序

当前固件最依赖 OUI 匹配，但它也是五种可用信号中最弱的一种。检测社区 **[WiFi Mothership](https://wifimothership.com/flock)**根据可信度对信号排序，参考了 GainSec 的固件研究。

| 可信度 | 信号 | 说明 |
|---|---|---|
| **高** | **BLE 制造商 ID `0x09C8`**（XUNTONG） | 最强的数字指纹。出现在 Raven 设备，以及连接电池模块的 Falcon 或 Sparrow 设备上 |
| **高** | **Raven BLE 服务 UUID `0x3100` 至 `0x3500`** | Raven 专属 GATT 服务，涉及 GPS、电源、网络、上传和错误。仅在 Raven 硬件上触发 |
| **中** | **WiFi SSID 模式 `^Flock-[A-Z0-9]+$`** | 默认配置热点名称。固件中还发现了 `FS Ext Battery`、`Penguin` 和 `Pigvision` 等其他 SSID |
| **中** | **BLE 设备名称片段** | `FS Ext Battery` 等名称出现在广播负载中，无需解析制造商数据 |
| **低** | **MAC 和 OUI 前缀匹配** | **噪声最多的方法。**组件供应商前缀也用于数千种无关产品 |

*当前固件最依赖的正是最后一行，这也是优先使用 OUI 检测的核心问题。*

### 为什么 OUI 列表噪声这么多

上述 31 个前缀并非 31 个 Flock 标识。WiFi Mothership 同时跟踪其中 **26 个前缀，并按实际所有者逐一分类**，从而显示出列表的组成。

| 类别 | 数量 | 所有者 |
|---|---:|---|
| **Flock Safety** | **1** | `B4:1E:52`，IEEE 分配给公司本身的前缀 |
| **电池模块** | 10 | 扩展电池包中的 Silicon Labs 部件 |
| **摄像头模块** | 11 | Liteon Technology WiFi 摄像头模块 |
| **计算基础设施** | 4 | Raspberry Pi Foundation 和 Raspberry Pi Trading |

**这 26 个前缀中有 25 个属于组件供应商，**这些部件大量用于与 Flock Safety 无关的硬件。Silicon Labs 电池包或 Liteon 摄像头模块的前缀也会出现在无关产品中，Raspberry Pi 板更是随处可见。

**匹配到其中任何一项都只是线索，不是身份确认。**这就是通配 Probe 特征在当前固件中如此重要的原因。将 OUI 匹配与空 SSID Probe 请求结合，会把可信度从猜测提升到项目自有量表中的 62。

*只有 `B4:1E:52` 能单独回答「这是 Flock 设备吗？」其他 30 个前缀都应视为辅助证据。*

### 有多少摄像头会暴露热点？

无线巡测数据给出了部署规模的下限。WiFi Mothership 统计，**2025 年 WiGLE 上至少有 900 个 Flock 接入点**。这里的 Flock AP 指广播默认 `Flock-XXXX` 热点 SSID 的设备。

这个数字描述的是会暴露配置热点的设备，而非已安装总数。Flock 声称部署了数万台摄像头，而其中大多数不会广播经过路人记录的信号。**地图只是样本，而且样本很小。**

______

## Issue #43：新 SSID 模式、5GHz 与 MAC 反指纹

Issue #20 关闭三个月后，又出现了第二份报告。它描述的似乎是有意的反检测措施，而非偶然的固件变化。**[Issue #43](https://github.com/colonelpanichacks/flock-you/issues/43)** 于 2026 年 5 月提交，依据的是在 DeFlock 已确认摄像头附近采集的 WiGLE 无线巡测数据，记录了现有工具都未考虑的三项发现。

### 发现 1：不同的 SSID 格式

有记录的 Flock 热点 SSID 一直遵循 `Flock-XXXXXX` 模式。但报告中的摄像头广播的是 **`Flock Camera net.`**，采用完全不同的命名方式。研究人员之前一直在 WiGLE 中搜索 `Flock-*` 通配模式，因此即使该摄像头正在广播，他们也会得到零结果。

### 发现 2：已确认的 5GHz 热点

同一摄像头同时在 **2.4GHz 信道 1** 和 **5GHz 信道 157** 上广播，两条频段使用连续的 MAC 地址（`...9f:a2:de` 和 `...9f:a2:df`）。这更像是一个双频 WiFi 模块为两个无线电分配相邻地址，而不是两个无关设备。研究人员 nsm_barii 先前的一份独立报告已记录到 Flock 在 5GHz 信道 149 上发送 Probe 请求。现在有两项数据确认 5GHz 运行确实存在，并非一次性配置错误。

**本文前面介绍的所有检测方法，包括当前通配 Probe 固件，都只监听 2.4GHz。**无论 OUI 列表多准确，只要摄像头专门或主要在 5GHz 广播，这些硬件就看不到它。

### 发现 3：热点使用本地管理 MAC 地址

捕获到的两个 MAC 地址都设置了**本地管理位**，这表示它们并非来自 Flock 在 IEEE 注册的真实 OUI 块。标准 `flock-you` 检测逻辑会有意跳过本地管理地址，因为这是过滤随机化 MAC 地址手机和笔记本电脑的常见方法。

**这个为减少误报而设置的过滤器，也会用同一逻辑过滤掉在热点接口上使用本地管理 MAC 的 Flock 摄像头。**捕获的两个地址末尾字节连续，这排除了随机生成，更像是有意且结构化的地址分配，而非巧合。

| 发现 | 仍然有效的方法 |
|---|---|
| **新 SSID 格式**（`Flock Camera net.`） | 扩展匹配模式后，SSID 模式匹配仍有效 |
| **5GHz 运行** | 当前 WiFi 固件没有办法，因为它只扫描 2.4GHz |
| **本地管理 MAC** | SSID 模式匹配，因为它完全不依赖 MAC 地址 |

*此表中只有 SSID 匹配不受摄像头使用频段或 MAC 地址分配方式影响。这也是扩展 SSID 模式支持、而不是单独依赖 OUI 匹配的实际理由。*

______

## Flock 是否在有意规避检测？

这两个 GitHub 问题都无法证明存在主观意图，准确表述这一点很重要。Issue #43 作者自己把它作为一个开放问题，而非结论：这种情况在 Flock 的部署中是否普遍存在，还是仅限于某台摄像头上的某个固件版本？

但把两个问题放在一起看。某种检测面消失了。社区找到了替代方案。替代方案的盲点，包括只扫描 2.4GHz、依靠 OUI 匹配、过滤本地管理 MAC，恰好对应新 SSID 格式、5GHz 无线电和本地管理 MAC 会利用的特性。**这可能是无关固件升级周期造成的巧合，也可能是供应商缩减无线信号、连带破坏第三方检测的结果，无论是否有意。**

*最有用的做法不是争论哪种解释正确，而是构建不依赖单一假设永久成立的检测方式。该项目过去两年的经历表明，这些假设都可能变化。*

### 视觉确认：设备开启但不广播

**[Valleytech Custom Solutions 发布的第三段短视频](https://www.youtube.com/shorts/sjI8FB0cLk0)**排除了「也许摄像头已被拆除」的解释。

{{< youtube id="sjI8FB0cLk0" >}}

创作者夜间回到第一段视频中的同一台摄像头，目视确认其 **IR LED 仍在闪烁**，说明设备已开机并正在为夜间拍摄照明。与此同时，**所有测试过的自定义固件都没有记录到该摄像头的有效命中**。有一次触发了提示，但确认是误报，并非真实检测。摄像头的无线侧没有任何信号到达检测器。

**这清楚地区分了两种相互竞争的解释。**摄像头已被拔除或迁移，无法解释一台明显开机且夜间照明的设备。摄像头在线、照明，却对所有 WiFi 检测方法保持沉默，说明无线特征消失了，而不是硬件不见了。

创作者还表示，他与研究同一问题的其他开发者交流后发现这并非个例。**多人在大致相同的时间观察到相同模式，**这更像是 Flock 方面的全国性协调变化，而非单台摄像头的局部异常。*这一说法属于轶事，来自非正式交谈，而非公开数据集。但它与 Issue #20 提到的 2025 年 12 月和 2026 年春季时间点一致。这类报告应提交为新的 GitHub issue，而不是留在评论串里。*

______

## 这对你的检测硬件意味着什么

如果设备已经无反应，请先按以下清单检查，再判断它是否损坏：

1. **先更新固件。**如果运行的版本早于当前 `main` 分支，你可能仍在搜索已停用的管理 AP 或失效的 BLE 信标。拉取最新固件并重新刷写。
2. **确认摄像头仍在现场。**一些「零检测」报告后来发现是硬件确实被拆除或迁移，并非检测失败。排查设备前，先与 **[Flock Finder](/articles/flock-finder-alpr-surveillance-mapping-tool/)** 或 **[DeFlock](https://deflock.org/)** 比较。
3. **经过路口时减速。**每个信道停留 250 毫秒，快速驶过会让车辆在无线电切换到正确频道前就错过检测窗口。停留 30 到 60 秒比开车快速经过并换用更大天线能发现更多摄像头。
4. **报告你的观察。**在目视确认的摄像头旁得到零检测结果，正是促成 Issue #20 和 #43 的那类数据。请新建 issue，不要假设别人已经报告。
5. **了解当前限制。**只支持 WiFi 和 2.4GHz 的固件无法发现迁移到 5GHz 或在扫描频段静默的摄像头。这是目前确实存在的缺口，并非你的特定构建有 bug。

**这并不意味着硬件毫无用处。**目前 OUI 列表和通配 Probe 指纹仍能发现绝大多数已部署的摄像头。关键是将任何检测器，无论 DIY 还是购买的产品，都视为当前竞赛状态的快照，而非永久解决方案。

{{< stscollective-ad "flockyou" >}}

______

## 另一种方案：检测红外闪光，而非 WiFi 信号

无线检测并非这场竞赛的唯一战线。**同一创作者 Valleytech Custom Solutions 发布的[另一个后续视频](https://www.youtube.com/shorts/mzpr6bslsYA)介绍了一种完全不同的方法**：不监听无线特征，而是观察摄像头的红外照明器。

{{< youtube id="mzpr6bslsYA" >}}

大多数 ALPR 摄像头，包括 Flock 的设备，都会使用**红外照明在夜间拍摄可读车牌**，普通安全摄像头也正是因此能在黑暗中工作。红外线对人眼不可见，但未安装红外截止滤镜的图像传感器可以看到。*缺少红外截止滤镜这一硬件细节，就能把普通摄像头模块变成 Flock 检测器。*

### 原型是什么样

视频中的方案经过多次迭代，才找到可行组合：

- **第一次尝试**：专用 IR 光电二极管接收器。技术上可行，但部件过于昂贵，不适合作为实用 DIY 方案。
- **第二次尝试**：**Jetson Nano 配合 Raspberry Pi 摄像头模块。**这证明概念可行，但硬件成本和功耗使其不适合手持或车载构建。
- **当前构建**：**不带红外截止镜头的 ESP32 摄像头模块。**创作者测试了 **ESP32-CAM** 和 **M5Stack S3 Cam**，最终选用 **Seeed Studio XIAO ESP32S3 Sense**，并搭配**基于 Quectel L76K 芯片的 Seeed XIAO GNSS 模块**为检测结果添加 GPS 标签。这与 WiFi 版 `flock-you` 仪表板使用的 GPS 无线巡测方式相同。

| 要求 | 原因 |
|---|---|
| **摄像头模块不带红外截止滤镜** | 让普通照片颜色正确的滤镜也会挡住此方法需要观察的光线 |
| **用摄像头而非光电二极管** | 能隔离信号的光电二极管接收器价格太高，不适合实用 DIY 构建 |
| **GPS 记录** | 像 WiFi 固件的 Flask 仪表板一样，将检测结果关联到位置 |

### 摄像头的闪烁模式

这个构想依赖照明器以可检测的重复模式闪烁，而不是持续点亮。创作者报告了**自己测得的时间约为亮 20 毫秒、灭 80 毫秒，周期 100 毫秒，在 10Hz 下占空比为 20%**，并明确表示该数据未经验证且可能有误。*请把这个具体数值当作自行测量的起点，而非已确认规格。Flock 从未公布该数值，创作者也没有声称确定。*

### 项目现状

**这是早期、仅供 DIY 使用的原型，不是成品。**创作者称软件是「vibe coded」，仍在开发中。计划加入可听提示的蜂鸣器，但尚未完成，也没有与 OUI-SPY 相当的成品板卡。目前仍需**人工目视确认**触发的检测究竟是真摄像头还是其他红外光源，因此它是筛查工具，不是全自动方案。

*这确实是与本文其他方法不同的检测面。它完全不依赖 WiFi、2.4GHz 或 5GHz、OUI 匹配或 MAC 地址行为，因此 Issue #43 中的规避手段不适用于它。它也有自身限制：需要视线无遮挡，会受日光干扰，并依赖尚未经过独立确认的占空比假设。*

______

## 社区正在做什么

对两个 issue 的回应遵循了这个项目两年来一直有用的模式：有人报告缺口，其他人贡献修复，然后修复作为更新发布，而不是一直留在待办事项中。

- **Issue #20** 找到了已确认的根本原因，并围绕通配 Probe 特征重写固件。这项成果归功于 DeFlockJoplin 社区的实地研究。
- **截至本文撰写时，Issue #43 仍未关闭，**SSID 模式匹配建议尚待实现。*如果你想帮助填补缺口，可以把 `Flock Camera` 加为额外匹配模式。这是一项范围明确、适合熟悉固件匹配逻辑者的小型贡献。*
- 底层 OUI 数据集在仓库中有版本号和日期。降级及低可信度条目也会记录，而非悄悄删除，让任何分叉项目的人都能了解改动内容和原因。

*这就是开源检测工具优于闭源替代品的实际理由。发现缺口的人无法修补专有检测器。这个项目已经两次及时发布修复。*

______

## 另一种应对：拆走硬件

无线检测是应对这些摄像头的一种方式。另一个行动直接针对硬件，并在 2026 年 9 月产生了当时最详细的公开证据，揭示 Flock 摄像头内部的工作方式。

**stegan0gram 集体从杆上拆下一台摄像头，复制了内部存储，并通过 Distributed Denial of Secrets 发布文件系统映像。**他们这样描述这项工作：

> 「为什么只摧毁它们？我们可以做逆向工程，揭开监视我们的人的秘密。我们在现场拆解了硬件，将其解除武装，并对摄像头和相关太阳能设备进行了逆向工程。」

*这个区别很重要。摧毁摄像头只移除一台，逆向工程则能产生有关所有摄像头的证据。*

### 拆除带来了什么

发布的数据集包含 **18 GB 媒体分区**、**1.5 GB Android 系统映像**和 **32 MB 凭据分区**，还包括恢复出的加密媒体容器密钥。研究人员据此确定了操作系统版本、内核版本、硬编码的后端凭据，以及摄像头存储的明文身份验证令牌。

这些证据现已支持 **[Flock Safety 摄像头漏洞：发现 50 多个缺陷](/articles/flock-safety-camera-security-vulnerabilities-research-2026/)**中的安全研究。此前该研究基于实验室设备和购买的样品。

### 对拆除行为的回应

物理干预会带来后果，情况并不单一。

- **全国各地有多人因涉嫌篡改或破坏 Flock 摄像头而被捕。**
- **有些城镇宣布将停止使用 Flock 摄像头，**这正是反对者希望看到的结果。
- **有一支警察部门制作了 3D 打印的假 Flock 摄像头外壳，**用来诱捕潜在破坏者，目的是促成逮捕。

Noel Pichardo 曾是 Rhode Island 州 Pawtucket 的警察，因质疑所在部门使用摄像头而成为 Flock 批评者。他直接提出了反对破坏行为的理由。他告诉 WIRED，自己理解人们的挫折感，但担心这种做法适得其反。「我认为这种私刑行为只会让警方和整个州政府更加相信这类工具是必要的，」他说。「州政府越是无视反对这种监控的选民的抱怨，这类事情就越会发生。」

### 检测在其中的作用

拆解摄像头并不会改变本文讨论的检测问题。摄像头仍按原方式广播，固件仍需要 OUI 列表和 Probe 特征，已记录的两次中断也依然存在。

数据转储增加了**硬件身份的确认，**包括一个现已在真实设备上核实的 OUI 条目，也提醒我们什么样的压力会改变部署情况。**摄像头离开某条路线，是因为委员会投票终止合同，而不是检测器停止响应。**无线工具回答的是你周围环境这个个人问题。政策争论回答的是更广泛的问题，而这些数据为政策争论提供了迄今最有力的证据。

______

## 结论：检测目标会变化，并没有固定答案

在曾发现摄像头的路线中，检测器保持沉默并不能证明硬件故障。这说明它识别的无线特征再次发生变化，而这一模式在一年内已经重复两次。**管理 AP、BLE 广播，以及当前固件可能固化的「仅 2.4GHz」和「仅 OUI」假设，**都只在有限时期内有效。

**解决办法从来不是放弃无线检测。**而是让检测方法的假设清晰、留有记录，并在 Issue #20 或 #43 这样的报告出现时允许修正。这就是使用开源固件而非闭源替代品的理由：社区发现缺口后就能发布修复，而不用等待供应商安排。

### 要点

- **两个有记录的检测面已经失效：**管理 WiFi AP（约于 2025 年 12 月停用）和 BLE 广播（到 2026 年春季已不可靠）。
- **当前方法将通配 Probe 请求与 OUI 和 IE 指纹匹配结合，实地验证的检测率为 12 台中 11 台，**但仅支持 WiFi 和 2.4GHz。
- **一份待处理报告描述了新的 SSID 格式、已确认的 5GHz 热点和本地管理 MAC 地址，**而当前基于 OUI、仅支持 2.4GHz 的方法看不到这些信号。
- **另一种不依赖无线电的方法正在出现：**移除了红外截止滤镜的 ESP32 摄像头模块能发现 Flock 摄像头的红外照明器。它完全不使用 WiFi，也不受上述规避方式影响。
- **视觉确认支持无线静默的判断：**一台摄像头明显开机并在夜间照明，但 WiFi 检测仍没有记录到有效命中，因此可以排除该设备被拆除的解释。
- **已知摄像头没有被检测到，并不自动意味着硬件坏了。**先更新固件，再确认摄像头是否仍在现场。
- **这个开源项目会在社区发现缺口后持续发布修复。**要了解当前检测状态，请阅读 GitHub issues，而不只是 README。

### 后续步骤

1. **先将固件更新到当前 `main` 分支，**再排查其他问题：**[github.com/colonelpanichacks/flock-you](https://github.com/colonelpanichacks/flock-you)**
2. **如果还没看过，请阅读完整硬件指南**：**[Flock-You 检测项目：反监控硬件指南](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/)**
3. **排查疑似盲区**，并与 **[Flock Finder](/articles/flock-finder-alpr-surveillance-mapping-tool/)** 对照
4. **了解你面对的情况**：**[Flock Safety 摄像头监控：普及程度、隐私顾虑和防护策略](/articles/flock-safety-camera-surveillance-prevalence-privacy-protection-2026/)**
5. **将 WiFi 检测与蜂窝检测结合起来**，使用 **[Rayhunter](/articles/how-to-flash-rayhunter-devices-complete-guide/)**，获得更完整的反监控视角，因为本文方法都无法检测手机基站模拟器

{{< centerbutton href="https://stscollective.com/discount/SIMEONONSECURITY" >}}
  购买即用型 FlockYou 设备，节省 20%
{{< /centerbutton >}}

______

## 相关文章

| 文章 | 内容 |
|---|---|
| **[Flock-You 检测项目：反监控硬件指南](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/)** | 三种硬件平台、固件设置及本文所依据的检测方法的完整技术指南 |
| **[Flock Finder：查看附近所有疑似 Flock 摄像头](/articles/flock-finder-alpr-surveillance-mapping-tool/)** | 在排查设备前，将疑似盲区与超过 40,000 个已映射摄像头位置对照 |
| **[Flock 摄像头：公共安全工具还是无需搜查令的监控机器？](/articles/flock-cameras-public-safety-or-surveillance-2026/)** | 独立分析 Flock 数据库实际支持的能力，以及为什么搜查令问题比检测问题更重要 |
| **[Flock Safety 摄像头监控：普及程度、隐私顾虑和防护策略](/articles/flock-safety-camera-surveillance-prevalence-privacy-protection-2026/)** | 部署规模、已记录的滥用案例及社区组织资源的完整介绍 |
| **[Flock Safety 摄像头漏洞：发现 50 多个缺陷](/articles/flock-safety-camera-security-vulnerabilities-research-2026/)** | Flock 摄像头硬件与软件的安全研究，与本文无线检测问题不同 |
| **[Rayhunter 设备刷写完整指南](/articles/how-to-flash-rayhunter-devices-complete-guide/)** | 检测 IMSI 捕获器和 Stingray，即本文所述 WiFi 检测缺口的蜂窝网络对应问题 |

______

## 参考资料

1. [Flock-You GitHub 仓库 - colonelpanichacks](https://github.com/colonelpanichacks/flock-you)
2. [GitHub Issue #20 - 未检测到 Flock 摄像头，但检测到了其他设备](https://github.com/colonelpanichacks/flock-you/issues/20)
3. [GitHub Issue #43 - 5GHz 信号？新 OUI 或 MAC 地址过滤](https://github.com/colonelpanichacks/flock-you/issues/43)
4. [NitekryDPaul OUI 研究数据集](https://github.com/colonelpanichacks/flock-you/blob/main/datasets/NitekryDPaul_wifi_ouis.md)
5. [nitekry/nite-oui-collection](https://github.com/nitekry/nite-oui-collection)
6. [DeFlock Joplin - 社区 ALPR 研究](https://deflockjoplin.today)
7. [Pintor 与 Atzori（2022）- WiFi Probe 请求的信息元素指纹分析，IEEE GLOBECOM](https://ieeexplore.ieee.org/document/10001618)
8. [WIRED 和 404 Media - 黑客进入 Flock 摄像头](https://www.wired.com/story/hackers-flock-camera-data-shows-how-system-works/)
9. [Micah Lee - Flock 摄像头存在大量安全漏洞和硬编码凭据](https://micahflee.com/flock-cameras-are-riddled-with-security-vulnerabilities-and-hard-coded-credentials/)
10. [Distributed Denial of Secrets - Flock ALPR 摄像头文件系统映像](https://ddosecrets.org/article/flock-alpr-camera)
11. [Hackaday - 本周安全动态：Flock 摄像头已过时](https://hackaday.com/2026/09/18/this-week-in-security-flock-cameras-are-old-microsoft-patches-patches-and-researchers-attack-ssh/)
12. [WiFi Mothership - Flock Safety ALPR 检测与设备参考](https://wifimothership.com/flock)
13. [GainSec - 固件研究与安全公告](https://gainsec.com/)
8. [寻找隐藏的 Probe - 隐藏 SSID 通配 Probe 行为](https://goodwi.fi/posts/2023/12/hunt-for-hidden-probe/)
9. [DeFlock - 众包 ALPR 摄像头地图](https://deflock.org/)
10. [Colonel Panic Tech - OUI-SPY 与检测硬件](https://colonelpanic.tech)
11. [STS Collective - FlockYou 设备](https://stscollective.com/discount/SIMEONONSECURITY)
12. [Flock 摄像头出现异常 - Valleytech Custom Solutions](https://www.youtube.com/shorts/cVf-id71BuQ)
13. [红外无线巡测 Flock 摄像头 - Valleytech Custom Solutions](https://www.youtube.com/shorts/mzpr6bslsYA)
14. [Flock 摄像头仍在运行但没有广播 - Valleytech Custom Solutions](https://www.youtube.com/shorts/sjI8FB0cLk0)
15. [自动车牌识别 - Wikipedia（ANPR/ALPR 系统中的红外照明）](https://en.wikipedia.org/wiki/Automatic_number-plate_recognition)
16. [Seeed Studio XIAO ESP32S3 Sense](https://www.seeedstudio.com/XIAO-ESP32S3-Sense-p-5639.html)
17. [Seeed Studio XIAO 的 L76K GNSS 模块](https://www.seeedstudio.com/L76K-GNSS-Module-for-Seeed-Studio-XIAO-p-5864.html)
