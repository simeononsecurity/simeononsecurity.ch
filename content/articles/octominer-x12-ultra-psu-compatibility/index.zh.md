---
title: "Octominer X12 Ultra 电源兼容性：Chicony 与 LiteOn 实测"
date: 2026-11-12
lastmod: 2026-11-12
toc: true
draft: false
description: "在五风扇、三电源的 Octominer X12 Ultra 上进行测试后发现，一台 Chicony 电源能启动设备，而测试过的 LiteOn 电源亮琥珀色灯且无法启动。"
genre: ["挖矿硬件", "计算机硬件"]
tags: ["Octominer X12 Ultra", "服务器电源", "电源兼容性", "Chicony R12-1K6P2A", "LiteOn PS-2142-2L"]
cover: "/img/cover/octominer-x12-ultra-psu-compatibility.webp"
coverAlt: "机箱内三台服务器电源的抽象插画，状态灯呈绿色、琥珀色和灰色"
coverCaption: ""
---

**Chicony R12-1K6P2A 启动了我的五风扇、三电源 Octominer X12 Ultra。** 我测试的 LiteOn PS-2142-2L 电源先亮绿灯，再变为琥珀色，设备未能启动。此结果仅适用于配有 **OCTOMINER (12PIN) 3x DPS1200 rev. 20** 电源背板的这台设备。额定功率相同，或某份独立 X12 转接板清单列出该型号，都不能证明它兼容 Octominer 背板。

该机箱以 **3,600 W 配置**出售，配有三个电源槽位。[Octominer 为 X12 Ultra 列出三台 1,200 W 电源的选项](https://octominer.eu/product/octominer-x12-ultra-used/)，也提供其他配置。请先检查自己设备的标签和电源板，再参考这些结果。

## 测试结果

| 电源 | 在这台设备上的结果 |
|---|---|
| **Chicony R12-1K6P2A，1,600 W** | 在我的测试中启动了设备。本文未测持续负载，也未测试所有槽位。 |
| **LiteOn PS-2142-2L，1,400 W** | 测试设备先亮绿灯，后亮琥珀色灯，设备未启动。 |
| **Dell/Delta D1200E-S0，Dell 0F37X3** | 不常见的交流电入口导致电源线难以寻找。本次测试没有记录此电源的启动或负载结果。 |
| **HP HSTNS-PD30，1,200 W** | 在同一台设备上测试，系统未启动。 |
| **其他 HP Common Slot 型号** | 我测试的 1,200 W Platinum Plus 套件和 750 W HSTNS-PD22B、HSTNS-PL22B、HSTNS-PD18 均未启动设备。套件内电源的具体型号没有记录。 |

**不要把 LiteOn 的测试结果当作所有 PS-2142-2L 的故障诊断。** 观察到的现象只说明该机箱启动失败。测试没有单独检查使能信号、遥测通信、背板针脚定义，也没有确认某台电源是否损坏。同样，Chicony 的结果只证明设备成功启动，不代表机箱通过了 4,800 W 认证或具备长期可靠性记录。

## 哪款 Chicony 启动了设备？

成功启动的型号是 **Chicony R12-1K6P2A**，也在 [Parallel Miner 兼容性表](https://parallelminer.com/uncategorized/breakout-board-compatibility-list/)中列为部件 **R1K6A002L**。其 [80 PLUS 测试报告](https://www.clearesult.com/80plus/sites/80plus/files/manufacturer-certificate/chicony-power-r121k6p2a-5866.pdf)标明这是一台 1,600 W 电源，额定输入为 **200 至 240 V AC**、10 A、50 至 60 Hz。报告在 230 V 测试条件下测得半载效率为 94.19%。这些数据描述的是受测电源，不是整套挖矿设备。

**200 至 240 V 额定范围很重要。** 不要假定它能从 120 V 插座输出额定功率。根据一份[准确型号的服务器配件商品页](https://www.itcreations.com/product/142080)，受测电源配有标准 C14 输入接口。请使用额定电压和电流合适的电源线及配电设备。

我的测试确认 Chicony 在这块特定背板上成功启动。结果不代表适用于所有 X12 Ultra 修订版。购买更多电源前，请核对完整型号和电源标签。

## 为什么 LiteOn 清单会误导我

**LiteOn PS-2142-2L** 出现在 [Parallel Miner 的 X12 转接板兼容性表](https://parallelminer.com/uncategorized/breakout-board-compatibility-list/)中。其 [80 PLUS 报告](https://www.clearesult.com/80plus/sites/80plus/files/manufacturer-certificate/liteon-technology-corporation-ps21422l-6889.pdf)标明这是 1,400 W 型号。这些来源能确认型号及其与 **Parallel Miner X12 适配器**搭配使用的记录，但没有任何来源测试 Octominer 原厂电源板。

插入后，我的 PS-2142-2L 从**绿色变为琥珀色**，设备没有启动。输出端刀片形状相似，不代表启动、状态或通信行为相同。仅凭 LED 变化无法确定哪个差异导致启动失败。

同一份 [Parallel Miner 表格](https://parallelminer.com/uncategorized/breakout-board-compatibility-list/)把 **Dell/Delta D1200E-S0**、**LiteOn PS-2142-2L** 和 **Chicony R12-1K6P2A** 列在八针适配器系列下。它把 **HP HSTNS-PD30** 和几款 750 W HP Common Slot 电源列在另一组六针适配器下。我测试过的 HP 电源都未能启动设备。该表描述的是 Parallel Miner 的板卡，不是 **OCTOMINER (12PIN)** 背板的替换电源清单。

## 检查供电和线缆

[Octominer X12 Ultra 故障排除指南](https://octominer.com/wp-content/uploads/2021/12/X12ULTRA-TROUBLESHOOTING-GUIDE-V3.pdf?v=7516fd43adaa)称，风扇全速时机箱本身最高耗电 **200 W**。指南建议至少预留 **10% 电力余量**，并警告不要超过已安装电源额定输出的 **90%**。计算时要包括 GPU 功耗、机箱耗电，以及电源在实际交流电压下的输出能力。

**每台 Chicony 电源的 1,600 W 标签不会把机箱公布的 3,600 W 配置提升到 4,800 W。** 电源背板、内部线缆、连接器、交流配电和散热也会限制系统。我没有测量这台设备的限制。Octominer 确认准确背板修订版支持更高额定值前，请遵守已公布配置。

Dell/Delta **D1200E-S0 / 0F37X3** 遇到的是另一种问题：电源侧交流输入接口需要较少见的配套线缆。根据实物和线缆商品信息，我此前将输入端识别为 **LS-25**，线缆端连接器识别为 **LS-26**。购买线缆前请核对接口形状和电气标记。外形熟悉的 C13 插头不能替代正确的配套连接器。

## 检查自己的 X12

1. **记录准确的硬件信息。** 拍摄机箱标签、电源标签、交流输入口、输出刀片和电源板修订版。清点风扇和电源槽位。
2. **检查交流供电。** 将电源输入额定值与插座、电源线和 PDU 的额定值进行比较。Chicony R12-1K6P2A 报告标明输入为 200 至 240 V AC。
3. **测试最小配置。** 更换电源、GPU 或 PSON 连接前，先关机并断开所有交流电源。[Octominer 指南](https://octominer.com/wp-content/uploads/2021/12/X12ULTRA-TROUBLESHOOTING-GUIDE-V3.pdf?v=7516fd43adaa)建议检查电源是否插牢及其 LED、主板与电源板之间的六针 PSON 线，并用一台电源搭配一块 GPU 逐步排查启动问题。
4. **记录测试现象。** 记录电源型号、槽位、LED 变化、板卡和风扇是否启动，以及设备是否完成启动。只有安全关机后，才在其他槽位重复测试。
5. **增加负载前先测量。** 在预期 GPU 负载下检查电源遥测和墙上功耗。本文的启动结果不能替代负载测试。

## 结论

**在这次比较中，Chicony R12-1K6P2A 是唯一有记录显示能在我的三槽位 X12 Ultra 上成功启动的替换电源。** 测试过的 LiteOn PS-2142-2L 从绿灯变为琥珀色，未能启动。我测试过的 HP Common Slot 电源也未启动设备。在准确型号和 Octominer 背板通过受控启动及负载测试前，请把其他电源清单视为调查线索。先核对型号标签和背板修订版，再按 Octominer 的供电指导操作，然后提高 GPU 负载。
