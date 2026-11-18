---
title: "我们标出了146,526台“Flock摄像头”，其中50,278台是ClickShare系统"
date: 2026-09-21
lastmod: 2026-11-14
toc: true
draft: false
description: "Flock Finder审计发现ClickShare等误报，说明证据依据，并记录由此实施的更改。"
genre: ["安全研究", "隐私技术", "开源项目", "数据新闻", "反监控"]
tags: ["Flock Finder", "Flock Safety", "ALPR", "OUI指纹识别", "WiGLE", "误报", "数据质量", "Barco ClickShare", "MAC地址", "IEEE OUI", "信息元素指纹识别", "ESP32", "Flock-You", "NitekryDPaul", "DeFlockJoplin", "开源问责", "监控地图", "WiFi", "探测请求", "MAC随机化"]
cover: "/img/cover/flock-finder-oui-false-positive-audit-2026.webp"
coverAlt: "深色城市地图布满红色标记，这些标记最终对应办公室WiFi设备，少数绿色标记仍代表更有力的检测结果"
coverCaption: "对146,526条Flock Finder记录的审计揭示了有用的现场观察如何演变成过度确定的地图结论。"
canonical: "https://simeononsecurity.com/articles/flock-finder-oui-false-positive-audit-2026/"
---

**我们在监控摄像头地图上放置了146,526个点。其中至少50,278个是Barco ClickShare演示系统。会议室设备占我们标题所称“已标注摄像头”的三分之一以上。**

这是我们的项目、数据管线，也是我们的错误。Flock Finder每天查询WiGLE，搜索在Flock Safety摄像头上观察到的MAC地址前缀，以完整坐标精度发布结果，并将它们绘制成相同的标记。记录元数据里有`suspected`一词，文档也提到了误报。地图和标题仍然传达了确定性。

**读者收获：**复现审计，区分观察与归因，并在地图标记和标题所在的位置展示置信度。前缀匹配只是调查线索，不是摄像头的证明。

我们终于对SSID列运行频率直方图时，几分钟内就从数据集中看出了问题。ClickShare只是最大的类别。另有6,099条记录名为`SMARTGATE_*`；3,801条以通用WiFi Direct前缀`DIRECT-`开头；314条名称正好为`AndroidAP`；138条为`Audi HUD`；133条为`MAX-PRINTER`；还有30条包含另一个检测器的判定字符串。总计，**60,793行，即41.5%，符合原始审计中已知的其他设备命名规则。**

Flock Finder现在按记录发布证据类别，默认从地图和标题中排除已知的其他硬件，公开筛选器，标记主要市场之外的记录，并区分高置信度前缀与合同制造商前缀。本文记录错误、证据和仍然存在的限制。

______

## 社区ALPR检测如何工作

社区开发的Flock检测器通常结合三类无线证据：

1. **WiFi MAC/OUI前缀。**全球管理MAC地址的开头字节可标识获得该地址块的组织。
2. **WiFi行为。**SSID、通配探测请求、接收方地址、信道模式或一组802.11信息元素可缩小设备类别范围。
3. **蓝牙证据。**制造商ID和服务UUID可识别特定产品或固件版本暴露的无线电设备。

OUI匹配之所以普及，是因为成本低且为被动方式。廉价ESP32无需连接网络，就能检查附近的802.11帧。像[WiGLE](https://wigle.net/)这样的历史数据库也让项目无需部署自己的扫描器就能搜索旧观察数据。

这种方法沿着社区脉络发展： [DeFlock](https://deflock.org/)的地图和本地组织工作；[colonelpanichacks/flock-you](https://github.com/colonelpanichacks/flock-you)；分支及配套项目，例如我们自己的[flock-you-esp32](https://github.com/simeononsecurity/flock-you-esp32)；最后是[Flock Finder](https://github.com/simeononsecurity/flock-finder)，它将前缀列表应用于全球范围的WiGLE数据。

最初的现场工作应得到明确致谢。[@NitekryDPaul](https://github.com/NitekryDPaul)通过混杂模式研究，在真实Flock设备上观察到30个前缀。[DeFlockJoplin](https://github.com/DeflockJoplin/flock-you)在现场测试中补充了另一个。这些观察是有效的。我们的下游错误，是把**“在Flock摄像头上观察到”当成“Flock摄像头独有”。**

______

## 结构性缺陷：OUI说明的是供应链事实

IEEE将OUI描述为分配给供应商、制造商或其他组织的24位标识符。它与受让方自行选择的另外24位组合成MAC地址。[IEEE Registration Authority](https://standards.ieee.org/products-programs/regauth/)发布该注册表。

它告诉我们谁获得了地址块，但不一定说明成品上印的品牌。合同制造商会为许多客户生产无线电模块，因此同一家芯片供应商可能出现在摄像头、投影仪、打印机、车辆和爱好者开发板中。

我们列表背后的注册分配已经显示出风险：

| 注册方 | 审计列表中的前缀 |
|---|---|
| Liteon Technology | `74:4C:A1`、`F4:6A:DD`、`9C:2F:9D`、`C0:35:32`、`E4:AA:EA`、`14:5A:FC`等 |
| Universal Global Scientific Industrial (USI) | `E0:4F:43`、`08:3A:88` |
| Espressif | `A4:CF:12`、`3C:71:BF` |
| Silicon Laboratories | `58:8E:81`、`90:35:EA`、`EC:1B:BD` |
| Flock Safety | `B4:1E:52` |

Espressif条目本应让我们警觉。所谓摄像头列表里的两个前缀属于全球最常见的嵌入式WiFi平台之一的制造商，其中也包括许多社区检测器使用的芯片。

`B4:1E:52`有所不同，因为它直接注册给Flock Safety。它在审计提交版本中已加入38前缀列表，**但尚未查询**：`scan_stats.json`显示只查询了31个前缀。六个新加入的电池组前缀也是如此。因此，这个快照没有证据说明Flock自有前缀常见还是罕见，我们不会把“未查询”写成“零结果”。

当前仓库在加入`E0:0A:F6`以匹配检测器固件后，共有39个前缀。保留的扫描摘要仍只报告31个前缀的数据。因此，新条目仍需等待完整重新计算，不能视为已证明零结果。

______

## 数据集自己揭示了问题

下列每个历史审计数字，都是用Python标准库的`csv`和`collections.Counter`，从Flock Finder提交[`5551829`](https://github.com/simeononsecurity/flock-finder/tree/5551829)中的`data/flock_cameras.csv`重新生成。无需再次开车测试。名称、地理位置和前缀组成已经与标题相矛盾。关于修正后实现的数据取自当前仓库保留的`scan_stats.json`摘要。

### 地理分布是早期警报

146,526行中，75,818行位于美国，70,674行位于美国以外，34行没有国家值。德国有13,491条记录，其后是加拿大6,251条、法国5,839条、英国4,836条、荷兰4,636条和瑞士4,515条。

{{< figure src="flock-finder-us-non-us-split.webp" alt="堆叠条形图显示美国记录75,818条、美国以外记录70,674条、无国家值记录34条" caption="国家直方图合计146,492，因为34行的国家字段为空。" >}}

地理位置是筛查信号，不是证明。Flock称其网络覆盖“全国”，并表示其连接美国[49个州](https://www.flocksafety.com/flock-ecosystem)的客户。国际扩张也可能改变市场边界。因此我们标记市场之外的记录供复核，而不是删除它们或宣布所有非美国记录为误报。

保守结论已足够：近一半记录位于项目的主要美国市场之外。因此，没有其他信号时，不能认为全球OUI命中同样可信。

### 超过60,000台设备报出了自己的名称

| 原始审计中的SSID族 | 记录数 | 占比 | 名称表示的内容 |
|---|---:|---:|---|
| 包含`ClickShare` | 50,278 | 34.3% | Barco无线演示设备 |
| `SMARTGATE_*` | 6,099 | 4.2% | 网关或OBD类设备系列 |
| `DIRECT-*` | 3,801 | 2.6% | WiFi Direct设备，例如打印机、电视和适配器 |
| 名称正好为`AndroidAP` | 314 | 0.2% | Android热点 |
| 名称正好为`Audi HUD` | 138 | 0.1% | Audi信息娱乐或抬头显示WiFi |
| 名称正好为`MAX-PRINTER` | 133 | 0.1% | 办公打印机 |
| `Flock ALPR [...]` | 30 | <0.1% | 作为SSID保存的另一个检测器判定 |
| **原始审计合计** | **60,793** | **41.5%** | 可识别为其他硬件或检测器输出 |

Barco支持文档称，ClickShare基站的默认网络名称为[`ClickShare-<serial base number>`](https://www.barco.com/en/support/knowledge-base/2675-how-to-connect-to-your-clickshare-base-unit-wifi)。这提供了产品系列的一手确认，无需根据地理位置或供应商注册信息猜测。

生产分类器此后用不区分大小写的正则表达式替代了精确名称检查，覆盖ClickShare、SmartGate、WiFi Direct、AndroidAP、Audi HUD、MAX-PRINTER和检测器输出标签。在相同的146,526行中，它匹配629个AndroidAP变体、139个Audi HUD变体和134个MAX-PRINTER变体。因此，当前仓库报告**61,110条`identified_other`记录**，略多于原始审计发现的60,793条。

### 确认信号只有2.4%

只有**3,502行**带有真正符合Flock模式的SSID。另有24,964行没有SSID。其余记录要么表明是其他硬件，要么只有一个OUI和未分类名称。

这3,502条已确认记录包含161种真实SSID变体：3,342条使用简单名称`Flock`，157条是一次性的`Flock-XXXXXX`或`FLOCK-XXXXXX`配置名称，另有三种名称包含`flock`。README曾报告166种变体，其中包括五种不同的`Flock ALPR [...]`检测器注释字符串。这五种是检测器的证据，不是摄像头的证据。

{{< figure src="flock-finder-evidence-class-breakdown.webp" alt="100%堆叠条形图将146,526条记录划分为SSID确认3,502条、具名未分类57,267条、隐藏SSID且仅有OUI 24,964条、识别为其他60,763条、检测器反馈30条" caption="旧标题将五种实质不同的证据类别压成一个数字。" >}}

### 前缀质量差异很大

误报率并不一致。有些前缀保留了有用的Flock信号；另一些则主要由具名办公或消费设备组成。

{{< figure src="flock-finder-per-oui-composition.webp" alt="31个OUI前缀的水平堆叠条形图：绿色为Flock SSID，红色为已知其他设备的SSID，浅灰色为隐藏SSID，深灰色为未分类记录" caption="最大的前缀往往包含最多已知其他设备。计数取自146,526行审计快照。" >}}

看两个被旧地图标记相同的前缀：

- `70:C9:4E`有495行：133个Flock模式名称，29个已知其他设备名称。
- `74:4C:A1`有11,872行：211个Flock模式名称，8,385个已知其他设备名称。

{{< figure src="flock-finder-prefix-signal-contrast.webp" alt="对比前缀70 C9 4E的Flock SSID占26.9%、已知其他设备占5.9%，与前缀74 4C A1的Flock SSID占1.8%、已知其他设备占70.6%" caption="单一标签掩盖了相反的信噪比。" >}}

最大记录中也有相同模式：`F4:6A:DD`有8,422个已知其他设备名称，对应327个Flock名称；`D0:39:57`为8,270对473；`E0:4F:43`则有6,238个已知其他设备名称，对应66个Flock名称。前缀的数量不等于证据质量。

______

## 隐藏在30行中的反馈循环

德克萨斯州有30条记录，其SSID显然是另一个检测器的输出：

| 作为SSID存储的检测器标签 | 工具给出的置信度 | 记录数 |
|---|---:|---:|
| `Flock ALPR [wifi_receiver_oui;low]` | 低 | 20 |
| `Flock ALPR [wifi_oui_wildcard_probe;medium]` | 中 | 4 |
| `Flock ALPR [wifi_bssid_oui;low]` | 低 | 3 |
| `Flock ALPR [flock_receiver_oui;low]` | 低 | 2 |
| `Flock ALPR [wifi_hidden_ssid_oui;low]` | 低 | 1 |

创建这些数据的工具将30条中的26条标为低置信度。随后，WiGLE上传把该工具的判定保存到SSID字段。我们的管线看到`Flock`一词，可能会把该标签当成独立确认。

从统计角度看，30行很少。但其机制影响重大：共享众包数据库的工具可能摄取彼此的输出，把低置信度猜测洗成表面上的佐证。修正方法会在查找确认子串`flock`之前，屏蔽整个`Flock ALPR [`模式。

______

## 我们错在哪里

README标题写着**“已标注摄像头 | 146,526”**。地图发布完整精度坐标，并将每条结果绘制成相同标记。它按GitHub Actions计划更新，让弱启发式看起来像持续维护的清单。

我们确实添加了限定说明。每个要素都带有`match_confidence: "suspected"`。README讨论过ClickShare可能同时存在，项目也为SSID发现保留了单独的候选项通道。但这些说明没有影响读者实际看到的数字、标记或默认视图。

文字里我们使用了保留措辞，标题却给出了确定数字。地图作出了断言。

最容易避免的问题是，我们的[flock-you-esp32](https://github.com/simeononsecurity/flock-you-esp32)固件早已将高置信度标识符与合同制造商标识符分开，并把弱证据评分降至警报阈值以下。这个概念在同一组织里已经存在，地图管线却没有继承它。

我们通过对自己的SSID列运行直方图发现了错误规模。只花了几分钟。我们每天都在提交146,526行与自身展示方式相矛盾的证据。

______

## 我们做了哪些更改

修正已落实到Flock Finder的数据模型和界面中：

- **每条记录的证据类别：**`ssid_confirmed`、`oui_high`、`oui_mfr`或`identified_other`。
- **OUI等级：**将前缀分为现场观察的高置信度和共享合同制造商等级。
- **排除已知其他设备：**默认从地图和标题中排除ClickShare、SmartGate、WiFi Direct、Android热点、Audi HUD、MAX-PRINTER和检测器输出SSID。
- **显示不确定性：**标记颜色、弹窗、计数和筛选器展示证据类别。
- **市场标记：**主要美国市场之外的记录带有`out_of_market: true`，仍可供复核。
- **拆分后的标题数字：**SSID确认3,502条、高等级OUI疑似73,691条、合同制造商OUI疑似8,223条、识别为其他61,110条。

修正后可供行动的数字为**85,416**，其中仍包含81,914条未经确认的OUI匹配。这是对符合当前规则项目的合理统计，不是经过验证的摄像头清单。

`identified_other`同样是操作性分类器，不是全知判断。ClickShare默认SSID有可靠的一手文档支持；而`DIRECT-`这类宽泛模式描述的是许多产品类别使用的WiFi Direct命名规则。公开匹配规则和`blocked_reason`字段后，研究者可以审计这些排除项，并在证据增强时修订。

### 长期方案是固件指纹识别

OUI分级能限制损害，但无法让共享制造商前缀变成产品专属标识。更可靠的方向是分析802.11探测请求中信息元素的顺序结构。上游工作记录了这种TLV签名：

```text
2,12,127,221:506f9a16030103,45,191,221:0050f208000000
```

这一序列描述的是特定固件栈的行为，而不是MAC地址块的所有者。探测请求指纹识别是成熟的设备识别技术。[关于802.11 MAC层指纹识别的已发表研究](https://doi.org/10.1155/2017/6235484)显示，即使MAC地址轮换，探测请求信息元素仍可能具有识别性。它也针对[flock-you issue #43](https://github.com/colonelpanichacks/flock-you/issues/43)报告的具体故障：`Flock Camera net.`出现在2.4和5 GHz频段连续的本地管理MAC地址上。

该签名仍需在不同硬件和固件版本上独立进行现场验证，畸形捕获数据也需采用防御性解析。不过方向正确。MAC随机化让仅靠OUI匹配走向注定失败的终点。

______

## 为什么这不只是一个仓库的问题

人们会用监控地图决定驾车路线、停车地点、举报内容、研究方向和组织行动。一个错误标记会分散注意力。数万个错误标记会让旁边准确的观察也失去公信力。

公信力还存在不对称。供应商或批评者只需找到一个可证明错误的ClickShare标记，就能质疑整个数据集。我们提供了50,278个。记者和倡议组织传播一个简洁标题的速度，可能快于后续更正追上的速度。

开源透明工作通过可检查的方法和清晰的不确定性赢得信任。公开原始数据帮助我们发现错误，但原始数据可访问并不能为夸大结论的界面开脱。读者在哪里遇到这个主张，修正就应出现在哪里：字段、筛选器、标记、图例和标题。

### 致所有Flock与ALPR地图项目

其他Flock和ALPR地图项目也应审计自己的数据集。这是比较方法的邀请，不是指称每张地图都继承了我们的错误。

[WiGLE](https://www.wigle.net/stats/)是我们所知覆盖最广、可公开访问且支持全球搜索的WiFi观察数据集。正是这种覆盖面让Flock Finder具有吸引力：一个API就能把经现场研究的签名列表转为全球地图。它也让错误大到足以测量。全球数据库会返回所有与无线电供应商地址空间重叠的无关产品，而不只是促使查询的那类产品。

其他地图使用不同证据。有些依靠照片和志愿者现场观察；另一些导入OpenStreetMap监控标签、公开记录、供应商披露或其他社区项目的数据。它们的总量不能直接与我们的WiGLE结果比较，2.4%的SSID确认比例也不能套用到现场核验数据集上。共同风险在于，一个项目的分类流入另一个项目的源数据，然后看起来像独立佐证。

每张公开地图都应能回答以下审计问题：

1. **一个标记代表什么？**拍到的设备、政府记录、OUI匹配、用户报告，还是从另一张地图导入的项目？
2. **有多少记录有直接产品证据？**按证据类别发布计数，而不是给出一个汇总摄像头总数。
3. **哪些来源彼此独立？**跟踪导入数据的来源，避免把同一观察算成多次确认。
4. **哪些因素与分类相矛盾？**对SSID、供应商、国家、贡献者标签及其他分类字段运行频率表。
5. **如何呈现不确定性和争议？**在标记、筛选器、导出内容和标题中显示置信度与更正状态。
6. **其他研究者能否复现计数？**发布查询、源快照、分类规则和日期。

这项审计没有减轻Flock问题。ALPR摄像头网络仍可能记录出行，在不同司法辖区间支持搜索，并影响从未同意收集数据的人。准确计数会让相关批评更难被驳回。如果我们要质疑监控系统，地图就必须区分观察到的、推断出的和确认的内容。

我们犯了一个基于充分信息仍然发生的错误。前缀来自正当的现场研究，管线可以复现，限定说明也确实存在。但推断仍超出了证据。良好意图和良好输入，并不能免除我们在规模化运行时检验系统输出的责任。

______

## 复现审计

检出提交`5551829`，然后在仓库根目录运行以下命令。代码只使用Python标准库，并打印总数、地理分布、常见SSID和选定的具名设备系列。

```bash
git clone https://github.com/simeononsecurity/flock-finder.git
cd flock-finder
git checkout 5551829

python3 - <<'PY'
import csv
from collections import Counter

with open("data/flock_cameras.csv", newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

ssids = Counter((row["ssid"] or "").strip() for row in rows)
countries = Counter((row["country"] or "").strip() for row in rows)

families = {
    "clickshare": lambda s: "clickshare" in s.lower(),
    "smartgate": lambda s: s.lower().startswith("smartgate_"),
    "direct": lambda s: s.lower().startswith("direct-"),
    "androidap": lambda s: s.lower().startswith("androidap"),
    "detector_output": lambda s: s.lower().startswith("flock alpr ["),
}

print("行", len(rows))
print("美国", countries["US"])
print("美国以外", sum(countries.values()) - countries["US"] - countries[""])
print("缺少国家信息", countries[""])
print("热门 SSID", ssids.most_common(20))
for name, matches in families.items():
    print(name, sum(matches(ssid) for ssid in ssids.elements()))
PY
```

要使用准确的历史输入，请使用该提交中的CSV，而不是当前生成的数据集。审计之后，项目停止提交大型CSV、GeoJSON和按OUI拆分的文件，因为每次扫描都会重写数百兆字节，并让仓库大幅膨胀。当前生成的数据从滚动的[`data-latest`版本](https://github.com/simeononsecurity/flock-finder/releases/tag/data-latest)恢复并发布；较小的`scan_stats.json`摘要仍保存在Git中。因此，当前分支缺少生成文件，并不意味着历史证据已删除，也不意味着计数变成零。

______

## 教训

**元数据将启发式标记为“疑似”，地图却把它画成确定的标记，这仍然是一项主张。**标签必须存在于数据模型和可视化中，不能只写在文档里。

