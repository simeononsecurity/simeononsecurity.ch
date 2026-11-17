---
title: "Hermes 本地模型基准测试：我会选择的 GPU 与模型组合"
date: 2026-10-24
lastmod: 2026-11-15
toc: true
draft: false
description: "我对 Hermes 模型的建议来自在 RTX 5060 Ti、RTX 2000E Ada、RTX 3060 Ti 和 RTX 3070 系统上进行的长上下文、工具、流式输出和视觉测试。"
genre: ["人工智能", "本地 AI", "硬件"]
tags: ["Hermes Agent", "本地语言模型", "LLM 基准测试", "GPU 推理", "RTX 3060 Ti", "RTX 3070", "RTX 2000E Ada", "RTX 5060 Ti", "模型资格验证", "工具调用", "长上下文", "llama.cpp", "Ollama", "Qwen3.5", "Qwen3.6", "Qwen3.8"]
cover: "/img/cover/hermes-local-model-gpu-benchmarks.webp"
coverAlt: "深蓝色背景上的插图，包含双风扇和低矮型显卡，旁边是 Hermes Model Benchmarks 标题"
coverCaption: ""
---

对于 Hermes 的长上下文任务，我会先在两张 16GB RTX 5060 Ti 上运行 Qwen3.5 35B。测试路线通过 LiteLLM 保留了 239,153 个输入 token，并分别通过了工具、流式输出、视觉、排队请求和取消检查。单卡替代方案是 Qwen3.6。在 RTX 3060 Ti 和 RTX 3070 系统上，我会从 Qwen3.5 2B 或 4B 开始。

这些选择来自在代理实际使用的推理路径上运行模型。我测试了长输入保留、工具往返、流式响应、图像问答和模型释放。我也测试了这些路径依赖的模式与内存设置，因为模型成功加载并不能说明它在代理长请求中是否有用。

Hermes 在代理调用工具时至少需要 64,000 个上下文 token。我将 65,536 个实际输入 token 作为长上下文资格门槛。输入 token 数量比服务器宣称的上下文大小更重要。([Hermes Agent 提供商文档](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/integrations/providers.md))

## 各系统使用的 GPU

结果中的系统字母代表以下硬件组合。

| 系统 | 此基准测试使用的 GPU | 我的首选起始模型 |
|---|---|---|
| A | 2 × GeForce RTX 5060 Ti，每张 16GB | 两张卡运行 Qwen3.5 35B，或单卡运行 Qwen3.6 |
| B | 1 × RTX 2000E Ada，16GB | 如果任务适合花几分钟处理长输入，就用 Qwen3.5 9B |
| C | 1 × RTX 2000E Ada，16GB | 用 Gemma 3 4B 处理测试过的长输入路径，用关闭思考模式的 Qwen3.5 0.8B 做有限范围的回忆任务 |
| D | 1 × RTX 2000E Ada，16GB | 用 Qwen3.5 9B、Gemma 4 12B-IT 或 GPT-OSS 20B 处理测试过的大模型工作负载 |
| E | 9 × GeForce RTX 3060 Ti，每张 8GB | Qwen3.5 2B 或 4B |
| F | 8 × GeForce RTX 3060 Ti，每张 8GB | Qwen3.5 2B 或 4B |
| G | 3 × GeForce RTX 3070 | Qwen3.5 2B 或 4B |

安装的显卡数量不代表每个请求都使用了所有 GPU。系统 A 上的 Qwen3.5 35B 和 Flash Next 试验使用了两张卡。Qwen3.6 使用了一张卡。系统 E 上成功重测的 Qwen3.5 4B 视觉测试从八张卡中选了一张，另有一张卡仍被排除在 AI 工作之外。

请将下方耗时视为测试模型、运行时和系统的综合结果。这些运行比较的是可用配置，无法将 GPU 架构单独确定为速度差异的原因。

## 两张 RTX 5060 Ti 让 Qwen3.5 35B 成为我的长上下文首选

在这些测试中，Qwen3.5 35B 保留了最多输入。Ollama 直接渐进测试在 262,144 token 的运行时上下文中保留了 248,279 个输入 token。另一次通过网关的流式请求保留了 239,153 个输入 token，返回开头标记，并在 148.12 秒后自然结束，共输出 31 个 token。

网关结果对 Hermes 很重要，因为请求经过了代理和 LiteLLM。其他独立请求完成了工具往返、识别了红色图像，并在同时提交时返回了两个正确答案。代理将这两个请求排入队列。关闭一个流式请求后，代理被释放，模型在 60.31 秒内卸载。

| Qwen3.5 35B 请求 | 输入 token | 输出 token | 耗时 | 结果 |
|---|---:|---:|---:|---|
| 直接 Ollama，首个渐进阶段 | 69,429 | 31 | 38.783 s | 开头标记完全匹配 |
| 直接 Ollama，共享前缀继续请求 | 124,179 | 31 | 28.472 s | 开头标记完全匹配 |
| 直接 Ollama，共享前缀继续请求 | 182,579 | 31 | 38.974 s | 开头标记完全匹配 |
| 直接 Ollama，共享前缀继续请求 | 248,279 | 31 | 54.215 s | 开头标记完全匹配 |
| 代理流式请求 | 69,427 | 29 | 38.872 s | 开头标记完全匹配 |
| LiteLLM 流式请求 | 239,153 | 31 | 148.12 s | 开头标记完全匹配，正常卸载 |

渐进式直接请求重复使用了不断扩大的前缀。它们的耗时描述的是模型已预热后的续接行为。54.215 秒不是对全新 248K 提示进行独立冷启动处理的测量结果。

在最大的直接测试阶段，模型报告两张 GPU 上驻留了约 273 亿字节。每张卡的内存峰值分别达到 14,964 和 12,386 MiB。

最高温度达到 62 和 63 C，运行过程中没有记录 OOM 或 Xid 故障。输入在配置上下文中为后续处理留下了 13,865 个 token。简短的标记回答用了其中 31 个。

当保留大型工作集比缩短首次响应更重要时，我会使用这条路线。工具和视觉检查验证了有用的代理行为，而长输入测试验证了上下文保留能力。这些属于不同工作负载。

## Qwen3.6 是单卡方案

Qwen3.6-35B-A3B UD-Q4_K_XL 在一张 RTX 5060 Ti 上保留了 131,000 个输入 token。测试时另一张卡处于空闲状态。当不希望为一个模型占用两张卡时，这为系统提供了实用替代方案。

| Qwen3.6 网关请求 | 输入 token | 输出 token | 耗时 | 结果 |
|---|---:|---:|---:|---|
| 首个长请求 | 66,007 |  | 167.82 s | 保留开头标记 |
| 更长请求 | 90,000 | 11 | 159.92 s | 保留开头标记，缓存输入为零 |
| 更长请求 | 119,999 | 11 | 250.61 s | 保留开头标记，缓存输入为零 |
| 接近运行时上限 | 131,000 | 11 | 287.09 s | 保留开头标记，缓存输入为零 |

131,000 token 的请求接近 131,072 token 的运行时上限。对于代理，我会给回答和后续工具消息留出更多空间。接近上限的保留结果能说明输入处理能力，但不适合作为合理的默认输入预算。

关闭思考模式后，工具调用测试通过。默认思考模式在发出工具调用前耗尽了 512 token 的测试配额。成功的试运行也通过了快速、流式和视觉请求。其首次 65,845 token 上下文检查耗时 139.57 秒。

## Qwen3.8 27B 在相同 66K 响应对比中胜出

在系统 A 上处理相同的 66,007 token 标记任务时，Qwen3.8 27B 返回答案最快。对于接近测试输入规模的请求，我会保留这条路线，同时用 Qwen3.5 35B 处理更大的工作集。

| 系统 A 路线 | 输入 token | 耗时 | 结果 |
|---|---:|---:|---|
| Qwen3.8 27B | 66,007 | 54.64 s | 保留开头标记 |
| Qwen3.6-35B-A3B UD-Q4_K_XL | 66,007 | 167.82 s | 保留开头标记 |
| Qwen3.8-Flash-Next UD-IQ4_XS | 66,007 | 164.58 s | 保留开头标记 |
| Flash Next IQ4 兼容别名 | 66,007 | 213.25 s | 保留标记 |

Qwen3.8 27B 的耗时约为匹配的 Qwen3.6 和 Flash Next 请求的三分之一。这些是在测试运行时下完整请求的观察结果，不是单独比较硬件。

快速响应、流式输出和工具调用也通过了。关闭思考模式后完成了完整颜色序列和工具往返，而思考模式测试在 512 token 配额内只返回了部分颜色序列。

由于内存压力，Flash Next 在此系统上仍不适合作为首选默认项。它的 65,847 token 试运行在 98,304 运行时上下文下耗时 201.41 秒并通过。此前两个 131,072 上下文配置在就绪前触及内存限制。

后续路线触及了 54 GiB cgroup 上限。对于无人值守任务，我会选择内存余量更大的路线。

标记为 `flash-iq2` 的路线实际使用了 Flash Next IQ4 兼容后端。这个名称并不代表 IQ2 结果。

## RTX 2000E Ada 能处理长输入，但模型选择会改变等待时间

在系统 C 上，Gemma 3 4B 是我测试过的长输入首选路线。两条路径在约 88 秒内保留了超过 84K 个输入 token。较大模型路线也通过了有用的保留检查，但请求耗时数分钟。

| 系统 | 模型和路径 | 输入 token | 耗时 | 结果 |
|---|---|---:|---:|---|
| B | Qwen3.5 9B，网关 | 72,265 | 263 s | 保留两个哨兵，后续挖矿恢复检查通过 |
| C | Gemma 3 4B，网关 | 84,044 | 88.05 s | 保留开头标记 |
| C | Gemma 3 4B，Aperture | 84,045 | 87.68 s | 保留开头标记 |
| C | Gemma 4 12B-IT，网关 | 67,254 | 263.07 s | 保留开头标记 |
| C | Gemma 4 12B-IT，Aperture 非流式 | 67,255 | 274.24 s | 保留开头标记 |
| C | Gemma 4 12B-IT，Aperture 流式 | 67,255 | 282.16 s | 保留开头标记 |
| C | Qwen3.5 9B，网关 | 75,648 | 319.36 s | 保留开头标记，模型已卸载 |
| C | GPT-OSS 20B，网关 | 84,099 | 315.83 s | 保留开头标记，模型已卸载 |
| D | Qwen3.5 9B，Aperture | 81,051 | 324.07 s | 已安装的制品通过保留测试 |
| D | Gemma 4 12B-IT，Aperture | 72,057 | 300.67 s | 已安装的制品通过保留测试 |
| D | GPT-OSS 20B，Aperture | 72,104 | 245.94 s | 已安装的制品通过保留测试 |

流式输出并未缩短系统 C 上 Gemma 4 的长预填充等待。首个流式内容在 277.49 秒后到达，比 274.24 秒完成的非流式响应还晚。此前一次非流式尝试超时，之后重试成功。我会将此路线用于能够容忍数分钟初始处理的任务。

Gemma 3 4B 也说明为什么应针对每个测试系统分别验证。系统 D 在两次 65K 回忆测试中都漏掉了开头标记，其中包括一次温度为零、输入 67,252 个 token 的复测。确定性请求在 GPU 完全驻留的情况下于 62.07 秒自然结束。

快速完成和正常 API 响应并不意味着答案正确。我会使用系统 C 的成功路线，并将系统 D 的失败路线排除在 Hermes 选择之外。

## 思考模式决定 Qwen3.5 0.8B 是否实用

关闭思考模式后，Qwen3.5 0.8B 成为系统 C 上适合有限回忆任务的候选模型。小型 Q8_0 模型通过网关在 65.92 秒内保留了 75,649 个输入 token。此结果仅适用于测试过的 Q8_0 制品和无思考路线，不适用于表格其他位置的旧 16K 上下文配置。

| 系统 C 上的 Qwen3.5 0.8B 请求 | 输入 token | 输出 token | 耗时 | 结果 |
|---|---:|---:|---:|---|
| 默认思考，简短诊断 | 9,050 | 3,391 | 66.56 s | 开头标记完全匹配 |
| 关闭思考，匹配诊断 | 9,055 | 21 | 7.65 s | 开头标记完全匹配，无推理文本 |
| 默认思考，长请求 |  |  | 600 s 超时 | 未完成回答 |
| 关闭思考，原生 Ollama | 75,656 | 22 | 69.80 s | 开头标记完全匹配 |
| 无思考的 OpenAI 兼容端点 | 75,646 | 12 | 69.09 s | 开头标记完全匹配 |
| 强制无思考模式的代理 | 75,647 | 13 | 66.83 s | 开头标记完全匹配 |
| 从系统 A 到系统 C 的 LiteLLM | 75,649 | 15 | 65.92 s | 开头标记完全匹配 |

匹配诊断从 66.56 秒降至 7.65 秒，快约 8.7 倍，同时生成内容从 3,391 个 token 降至 21 个。因此，对于简单的提取和路由任务，我会明确设置推理模式。默认推理将大部分处理花在任务不需要的输出上。

一次简短的 OpenAI 兼容探测未能匹配标记，温度为零的重试才通过。成功的路线检查使用无思考模式，并在没有输出上限的情况下自然结束。另有三个网关在 4.22、4.37 和 3.85 秒内通过了简短标记请求。这些检查验证路由，而 75,649 token 请求验证通过网关保留长输入的能力。

我会为范围明确的回忆和提取任务试用这条路线。对于开放式代理推理，我会选择更大的模型。找回一个合成标记远比规划、编程或协调多个工具简单。

## RTX 3060 Ti 和 RTX 3070 系统更适合 Qwen3.5 2B 和 4B

对于 8GB 显卡，Qwen3.5 2B 和 4B 是实用的起步选择。系统 E、F 和 G 的文本上下文请求均以 65,579 个输入 token 通过，耗时从 30.343 到 93.753 秒。测试过的 4B 路线还通过了工具、流式输出和图像检查。

系统 E 的 4B 视觉上下文复测在 44.88 秒内以 65,637 个输入 token 保留了两个标记和图像颜色顺序。正序和反序颜色请求也通过了。另一张卡发生 Xid 79 链路故障并导致系统重启后，此次复测使用了一张健康的卡。

| 系统 | Qwen3.5 2B 文本上下文 | Qwen3.5 4B 文本上下文 | Qwen3.5 4B 视觉上下文 |
|---|---|---|---|
| E，RTX 3060 Ti 集群 | 65,579 token，30.343 s | 65,579 token，53.787 s | 65,637 token，44.88 s |
| F，RTX 3060 Ti 集群 | 65,579 token，61.282 s | 65,579 token，93.753 s | 65,635 token，84.749 s |
| G，RTX 3070 集群 | 65,579 token，76.731 s | 65,579 token，90.807 s | 65,635 token，87.496 s |

这些系统各自记录了 29 项通过的检查。两套 RTX 3060 Ti 系统之间的耗时差异也说明了为什么我会选择测试过的系统配置，而不是根据这些请求时长给显卡排名。

推理窗口结束后，七套系统都恢复了挖矿。系统 B 的单独停机后恢复检查通过，并获得了新的已接受份额。系统 E 中出故障的显卡在重启并加固 PCIe 链路后恢复挖矿，但仍被排除在 AI 集群之外。窗口结束时恢复挖矿，与每次推理请求后自动交还资源是不同的结果。

## 模型加载成功并不代表通过资格验证

我会将 DeepSeek Coder V2 16B 从测试过的 65K Hermes 选择中排除。它的 f16 缓存运行保留了 50,477 个输入 token，但 65K 目标运行触发了 VRAM 保护。Q4 和 Q8 缓存选项虽将权重加载到 GPU，却随后触及主机内存上限，或在长提示下吞吐量过低。

| DeepSeek Coder V2 缓存配置 | 运行时上下文 | 观察结果 | 我的评估 |
|---|---:|---|---|
| f16 | 81,920 | 50,477 token 回忆测试通过，过大的请求被拒绝 | 较短上下文下有用 |
| f16 | 73,728 | 65K 目标预填充在 GPU 使用量 15,802 MiB 时停止 | 不符合 65K 要求 |
| Q4_0 | 98,304 | 受控停止前，长预填充降至 96.72 token/s | 不适合此工作负载 |
| Q8_0 | 77,824 | 受控停止前，长预填充降至 120.12 token/s | 不适合此工作负载 |
| Q4_0 / Q8_0，较大配置 | 163,840 / 98,304 | 主机内存保护停止了测试 | 内存是否合适取决于整个系统 |

实际经验是测试你准备发送的请求。GPU 驻留、简短回答和较大的配置上下文，都不能证明模型能以实用延迟保留长输入。

系统 A 上针对路线的后续工作改善了 Granite 4.2 8B 和 GPT-OSS 20B。Granite 的 Q6_K 路线在没有缓存输入时，于 88.636 秒内保留了 66,082 个输入 token。修复代理后，GPT-OSS 完成了工具往返，调用耗时 9.854 秒，后续请求耗时 9.849 秒。我会将这些成功的路线检查与此前未完成的尝试区分开。

## 完整基准测试结果

表格包含 59 种模型和系统组合的 295 项检查。矩阵记录了 273 项通过、1 项回忆检查失败，以及 7 项未完成、不一致或不兼容的结果。14 项检查不属于 65K 资格范围。每行均保留了测量结果。

我的建议适用于通过的路线和工作负载。失败或未完成的行不能验证对应行为。

短上下文和嵌入测试的通过只适用于各自的工作负载。16K 或 32K 上下文通过，不能证明路线符合 Hermes 65,536 输入 token 工作负载的要求。此处的模型名称是路线标签。`flash-iq2` 标签实际使用 IQ4 兼容后端。

系统 A 的 Qwen3.5 35B 上下文行是上文渐进测试中最后一个共享前缀阶段。工具时长中的加号分别表示调用和后续请求。

并发测试行给出两个排队请求的耗时。取消测试行给出客户端关闭流后释放资源的时间。其他上下文渐进测试和 Qwen3.5 0.8B 路线比较见上方各自的表格。

### 系统 A

| 模型路线标签 | 检查项 | 结果 | 输入 token | 请求耗时 |
|---|---|---|---:|---:|
| bonsai-2-27b | context | 通过 | 65,621 | 88.746 s |
| bonsai-2-27b | quick | 通过 | 57 | 6.429 s |
| bonsai-2-27b | stream | 通过 |  | 9.371 s |
| bonsai-2-27b | tools | 通过 |  | 10.478 s |
| deepseek-coder-v2:16b | context | 不兼容 | 50,477 |  |
| deepseek-coder-v2:16b | quick | 通过 | 77 | 43.239 s |
| flash-iq2 | context | 通过 | 66,007 | 213.25 s |
| flash-iq2 | quick | 通过 |  | 56.03 s |
| flash-iq2 | stream | 通过 |  | 1.35 s |
| flash-iq2 | tools | 通过 |  | 16.55 s |
| gemma-4-12b-it | context | 通过 | 65,590 | 51.225 s |
| gemma-4-12b-it | quick | 通过 | 21 | 5.166 s |
| gemma-4-12b-it | stream | 通过 |  | 4.653 s |
| gemma-4-12b-it | tools | 通过 |  | 18.72 s |
| gemma-4-12b-it | vision | 通过 | 115 | 7.222 s |
| gemma-4-12b-it | vision_context | 通过 | 65,685 | 56.06 s |
| gemma-4-12b-it | vision_reverse | 通过 | 115 | 7.467 s |
| gemma-4-e4b-it | context | 通过 | 65,590 | 21.889 s |
| gemma-4-e4b-it | quick | 通过 | 21 | 17.919 s |
| gemma-4-e4b-it | stream | 通过 |  | 4.25 s |
| gemma-4-e4b-it | tools | 通过 |  | 8.734 s |
| gpt-oss-20b | context | 通过 | 65,637 | 159.155 s |
| gpt-oss-20b | quick | 通过 | 73 | 10.548 s |
| gpt-oss-20b | stream | 通过 |  | 20.594 s |
| gpt-oss-20b | tools | 通过 |  | 9.854 + 9.849 s |
| granite-4.2-3b | context | 通过 | 65,589 | 70.968 s |
| granite-4.2-3b | quick | 通过 | 20 | 4.009 s |
| granite-4.2-3b | stream | 通过 |  | 5.365 s |
| granite-4.2-3b | tools | 通过 |  | 6.086 s |
| granite-4.2-8b | context | 通过 | 66,082 | 88.636 s |
| granite-4.2-8b | quick | 通过 | 20 | 5.857 s |
| granite-4.2-8b | stream | 通过 |  | 11.826 s |
| granite-4.2-8b | tools | 通过 |  | 11.852 s |
| qwen27b | context | 通过 | 66,007 | 54.64 s |
| qwen27b | quick | 通过 | 57 | 31.5 s |
| qwen27b | stream | 通过 |  | 0.92 s |
| qwen27b | tools | 通过 |  | 4.25 s |
| qwen3-embedding-0.6b | context | 通过 | 32,767 | 7.736 s |
| qwen3-embedding-0.6b | quick | 通过 | 14 | 2.125 s |
| qwen3.5-0.8b | context | 通过 | 16,429 | 10.5 s |
| qwen3.5-0.8b | quick | 通过 | 17 | 14.316 s |
| qwen3.5-0.8b | stream | 通过 |  | 2.125 s |
| qwen3.5-0.8b | tools | 通过 |  | 4.416 s |
| qwen3.5-2b | context | 通过 | 65,581 | 11.175 s |
| qwen3.5-2b | quick | 通过 | 17 | 4.519 s |
| qwen3.5-2b | stream | 通过 |  | 3.736 s |
| qwen3.5-2b | tools | 通过 |  | 5.046 s |
| qwen3.5-4b | context | 通过 | 65,579 | 36.451 s |
| qwen3.5-4b | quick | 通过 | 15 | 19.935 s |
| qwen3.5-4b | stream | 通过 |  | 17.496 s |
| qwen3.5-4b | tools | 通过 |  | 7.308 s |
| qwen3.5-4b | vision | 通过 | 70 | 7.848 s |
| qwen3.5-4b | vision_context | 通过 | 65,635 | 28.24 s |
| qwen3.5-4b | vision_reverse | 通过 | 70 | 4.386 s |
| qwen3.5-9b | context | 通过 | 65,581 | 34.139 s |
| qwen3.5-9b | quick | 通过 | 17 | 3.88 s |
| qwen3.5-9b | stream | 通过 |  | 3.378 s |
| qwen3.5-9b | tools | 通过 |  | 10.204 s |
| qwen3.5-9b | vision | 通过 | 72 | 4.441 s |
| qwen3.5-9b | vision_context | 通过 | 65,637 | 33.745 s |
| qwen3.5-9b | vision_reverse | 通过 | 72 | 3.97 s |
| qwen3.5:35b-a3b-q4_K_M | cancellation | 通过 |  | 60.31 s |
| qwen3.5:35b-a3b-q4_K_M | concurrency | 通过 |  | 26.23 / 25.33 s |
| qwen3.5:35b-a3b-q4_K_M | context | 通过 | 248,279 | 54.215 s |
| qwen3.5:35b-a3b-q4_K_M | gateway | 通过 | 239,153 | 148.12 s |
| qwen3.5:35b-a3b-q4_K_M | quick | 通过 | 79 | 10.08 s |
| qwen3.5:35b-a3b-q4_K_M | stream | 通过 | 69,429 | 38.783 s |
| qwen3.5:35b-a3b-q4_K_M | tools | 通过 |  | 15.22 + 14.83 s |
| qwen3.5:35b-a3b-q4_K_M | vision | 通过 |  | 18.39 s |
| Qwen3.6-35B-A3B UD-Q4_K_XL | context | 通过 | 65,845 | 139.57 s |
| Qwen3.6-35B-A3B UD-Q4_K_XL | quick | 通过 | 15 | 3.97 s |
| Qwen3.6-35B-A3B UD-Q4_K_XL | stream | 通过 |  | 0.45 s |
| Qwen3.6-35B-A3B UD-Q4_K_XL | tools | 通过 | 293 | 5.48 s |
| Qwen3.6-35B-A3B UD-Q4_K_XL | vision | 通过 | 38 | 0.59 s |
| Qwen3.8-Flash-Next UD-IQ4_XS | context | 通过 | 65,847 | 201.41 s |
| Qwen3.8-Flash-Next UD-IQ4_XS | quick | 通过 | 17 | 54.62 s |
| Qwen3.8-Flash-Next UD-IQ4_XS | stream | 通过 |  | 1.2 s |
| Qwen3.8-Flash-Next UD-IQ4_XS | tools | 通过 |  | 22.18 s |
| Qwen3.8-Flash-Next UD-IQ4_XS | vision | 通过 |  | 3.86 s |

### 系统 B

| 模型路线标签 | 检查项 | 结果 | 输入 token | 请求耗时 |
|---|---|---|---:|---:|
| gemma-4-12b-it | context | 通过 | 65,590 | 299.163 s |
| gemma-4-12b-it | quick | 通过 | 21 | 15.261 s |
| gemma-4-12b-it | stream | 通过 |  | 148.792 s |
| gemma-4-12b-it | tools | 通过 |  | 34.124 s |
| gemma-4-12b-it | vision | 通过 | 120 | 61.455 s |
| gemma-4-12b-it | vision_context | 通过 | 65,690 | 295.581 s |
| gemma-4-12b-it | vision_reverse | 通过 | 120 | 32.511 s |
| gemma3-4b | context | 通过 | 65,584 | 67.382 s |
| gemma3-4b | quick | 通过 | 15 | 6.329 s |
| gemma3-4b | stream | 通过 |  | 24.138 s |
| gemma3-4b | vision | 通过 | 306 | 7.018 s |
| gemma3-4b | vision_context | 通过 | 65,876 | 70.912 s |
| gemma3-4b | vision_reverse | 通过 | 306 | 5.762 s |
| gpt-oss-20b | context | 通过 | 65,637 | 206.767 s |
| gpt-oss-20b | quick | 通过 | 72 | 16.583 s |
| gpt-oss-20b | stream | 通过 |  | 32.075 s |
| gpt-oss-20b | tools | 通过 |  | 28.102 s |
| nomic-embed-text | context | 未完成 | 2,048 |  |
| nomic-embed-text | quick | 通过 |  | 7.117 s |
| qwen3-14b | context | 未完成 |  | 1800.09 s |
| qwen3-14b | quick | 通过 | 15 | 37.199 s |
| qwen3-14b | stream | 通过 |  | 35.471 s |
| qwen3-14b | tools | 通过 |  | 87.554 s |
| qwen3-8b | context | 低于 65K 范围外，排除 |  |  |
| qwen3-8b | quick | 低于 65K 范围外，通过 | 15 | 21.059 s |
| qwen3-8b | stream | 低于 65K 范围外，排除 |  |  |
| qwen3-8b | tools | 低于 65K 范围外，排除 |  |  |
| qwen3.5-9b | context | 通过 | 65,579 | 282.796 s |
| qwen3.5-9b | litellm_long_route | 通过 | 72,265 | 263 s |
| qwen3.5-9b | post_external_stop_mining | 通过 |  |  |
| qwen3.5-9b | quick | 通过 | 15 | 25.881 s |
| qwen3.5-9b | stream | 通过 |  | 143.44 s |
| qwen3.5-9b | tools | 通过 |  | 31.812 s |
| qwen3.5-9b | vision | 通过 | 75 | 32.015 s |
| qwen3.5-9b | vision_context | 通过 | 65,640 | 396.288 s |
| qwen3.5-9b | vision_reverse | 通过 | 75 | 28.626 s |

### 系统 C

| 模型路线标签 | 检查项 | 结果 | 输入 token | 请求耗时 |
|---|---|---|---:|---:|
| gemma-4-12b-it | aperture_context | 通过 | 67,255 | 274.24 s |
| gemma-4-12b-it | aperture_short | 通过 | 35 | 39.32 s |
| gemma-4-12b-it | aperture_stream_context | 通过 | 67,255 | 282.16 s |
| gemma-4-12b-it | context | 通过 | 65,670 | 313.661 s |
| gemma-4-12b-it | gateway_context | 通过 | 67,254 | 263.07 s |
| gemma-4-12b-it | gateway_short | 通过 | 27 | 20.98 s |
| gemma-4-12b-it | quick | 通过 | 21 | 16.447 s |
| gemma-4-12b-it | stream | 通过 |  | 15.175 s |
| gemma-4-12b-it | tools | 通过 |  | 37.821 s |
| gemma-4-12b-it | vision | 通过 | 120 | 58.52 s |
| gemma-4-12b-it | vision_context | 通过 | 65,690 | 308.759 s |
| gemma-4-12b-it | vision_reverse | 通过 | 120 | 31.25 s |
| gemma3-4b | aperture_context | 通过 | 84,045 | 87.68 s |
| gemma3-4b | aperture_after_system_d_route_change | 通过 | 24 | 5.42 s |
| gemma3-4b | aperture_short | 通过 | 22 | 5.45 s |
| gemma3-4b | aperture_stream | 通过 |  | 3.72 s |
| gemma3-4b | context | 通过 | 65,664 | 67.543 s |
| gemma3-4b | gateway_context | 通过 | 84,044 | 88.05 s |
| gemma3-4b | gateway_short_via_system_a | 通过 |  | 3.16 s |
| gemma3-4b | gateway_short_via_system_e | 通过 |  |  |
| gemma3-4b | gateway_short_via_system_f | 通过 |  | 4.15 s |
| gemma3-4b | gateway_short_via_system_g | 通过 |  | 6.06 s |
| gemma3-4b | quick | 通过 | 15 | 5.163 s |
| gemma3-4b | stream | 通过 |  | 24.691 s |
| gemma3-4b | vision | 通过 | 306 | 7.318 s |
| gemma3-4b | vision_context | 通过 | 65,876 | 72.476 s |
| gemma3-4b | vision_reverse | 通过 | 306 | 5.831 s |
| gpt-oss-20b | context | 通过 | 65,716 | 216.594 s |
| gpt-oss-20b | gateway_context | 通过 | 84,099 | 315.83 s |
| gpt-oss-20b | gateway_short | 不一致 |  |  |
| gpt-oss-20b | quick | 通过 | 72 | 21.603 s |
| gpt-oss-20b | stream | 通过 |  | 31.957 s |
| gpt-oss-20b | tools | 通过 |  | 26.096 s |
| nomic-embed-text | context | 低于 65K 范围外，未完成 | 2,048 |  |
| nomic-embed-text | quick | 低于 65K 范围外，通过 |  | 4.178 s |
| qwen3-14b | context | 低于 65K 范围外，未完成 |  | 1800.06 s |
| qwen3-14b | quick | 低于 65K 范围外，通过 | 15 | 35.809 s |
| qwen3-14b | stream | 低于 65K 范围外，通过 |  | 35.43 s |
| qwen3-14b | tools | 低于 65K 范围外，通过 |  | 87.723 s |
| qwen3-8b | context | 低于 65K 范围外，排除 |  |  |
| qwen3-8b | quick | 低于 65K 范围外，通过 | 15 | 21.293 s |
| qwen3-8b | stream | 低于 65K 范围外，未完成 |  | 900.01 s |
| qwen3-8b | tools | 低于 65K 范围外，排除 |  |  |
| qwen3.5-9b | context | 通过 | 65,662 | 287.984 s |
| qwen3.5-9b | gateway_context | 通过 | 75,648 | 319.36 s |
| qwen3.5-9b | gateway_short | 通过 | 21 | 72.14 s |
| qwen3.5-9b | quick | 通过 | 15 | 24.635 s |
| qwen3.5-9b | stream | 通过 |  | 143.157 s |
| qwen3.5-9b | tools | 通过 |  | 30.395 s |
| qwen3.5-9b | vision | 通过 | 75 | 27.756 s |
| qwen3.5-9b | vision_context | 通过 | 65,640 | 398.797 s |
| qwen3.5-9b | vision_reverse | 通过 | 75 | 28.645 s |

### 系统 D

| 模型路线标签 | 检查项 | 结果 | 输入 token | 请求耗时 |
|---|---|---|---:|---:|
| gemma-4-12b-it | context | 通过 | 65,590 | 275.395 s |
| gemma-4-12b-it | exact_digest_aperture_65k | 通过 | 72,057 | 300.67 s |
| gemma-4-12b-it | exact_digest_broker_short | 通过 | 34 | 30.74 s |
| gemma-4-12b-it | quick | 通过 | 21 | 15.05 s |
| gemma-4-12b-it | stream | 通过 |  | 14.722 s |
| gemma-4-12b-it | tools | 通过 |  | 33.869 s |
| gemma-4-12b-it | vision | 通过 | 120 | 56.315 s |
| gemma-4-12b-it | vision_context | 通过 | 65,690 | 282.174 s |
| gemma-4-12b-it | vision_reverse | 通过 | 120 | 29.978 s |
| gemma3-4b | context | 通过 | 65,584 | 63.564 s |
| gemma3-4b | exact_digest_65k_recall | 失败 | 67,252 | 62.07 s |
| gemma3-4b | quick | 通过 | 15 | 5.151 s |
| gemma3-4b | stream | 通过 |  | 22.552 s |
| gemma3-4b | vision | 通过 | 306 | 8.276 s |
| gemma3-4b | vision_context | 通过 | 65,876 | 67.575 s |
| gemma3-4b | vision_reverse | 通过 | 306 | 5.651 s |
| gpt-oss-20b | context | 通过 | 65,637 | 189.07 s |
| gpt-oss-20b | exact_digest_aperture_65k | 通过 | 72,104 | 245.94 s |
| gpt-oss-20b | exact_digest_broker_short | 通过 | 84 | 15.96 s |
| gpt-oss-20b | quick | 通过 | 72 | 15.431 s |
| gpt-oss-20b | stream | 通过 |  | 31.052 s |
| gpt-oss-20b | tools | 通过 |  | 23.65 s |
| nomic-embed-text | context | 未完成 | 2,048 |  |
| nomic-embed-text | quick | 通过 |  | 2.798 s |
| qwen3-14b | context | 未完成 | 40,939 | 872.209 s |
| qwen3-14b | quick | 通过 | 15 | 36.021 s |
| qwen3-14b | stream | 通过 |  | 33.491 s |
| qwen3-14b | tools | 通过 |  | 82.471 s |
| qwen3-8b | context | 未完成 |  | 1800.07 s |
| qwen3-8b | quick | 通过 | 15 | 19.283 s |
| qwen3-8b | stream | 通过 |  | 19.401 s |
| qwen3-8b | tools | 通过 |  | 65.054 s |
| qwen3.5-9b | context | 通过 | 65,579 | 258.048 s |
| qwen3.5-9b | exact_digest_aperture_65k | 通过 | 81,051 | 324.07 s |
| qwen3.5-9b | exact_digest_broker_short | 通过 | 29 | 94.48 s |
| qwen3.5-9b | quick | 通过 | 15 | 27.16 s |
| qwen3.5-9b | stream | 通过 |  | 28.62 s |
| qwen3.5-9b | tools | 通过 |  | 28.129 s |
| qwen3.5-9b | vision | 通过 | 75 | 25.047 s |
| qwen3.5-9b | vision_context | 通过 | 65,640 | 369.477 s |
| qwen3.5-9b | vision_reverse | 通过 | 75 | 27.602 s |

### 系统 E

| 模型路线标签 | 检查项 | 结果 | 输入 token | 请求耗时 |
|---|---|---|---:|---:|
| gemma-4-e4b-it | context | 通过 | 65,590 | 49.086 s |
| gemma-4-e4b-it | quick | 通过 | 21 | 23.911 s |
| gemma-4-e4b-it | stream | 通过 |  | 28.136 s |
| gemma-4-e4b-it | tools | 通过 |  | 56.756 s |
| granite-4.0-h-tiny | context | 通过 | 65,566 |  |
| granite-4.0-h-tiny | quick | 通过 | 35 | 10.408 s |
| granite-4.0-h-tiny | stream | 通过 |  | 27.798 s |
| granite-4.0-h-tiny | tools | 通过 |  | 43.304 s |
| granite-4.2-3b | context | 通过 | 65,589 | 1014.03 s |
| granite-4.2-3b | quick | 通过 | 20 | 14.569 s |
| granite-4.2-3b | stream | 通过 |  | 6.948 s |
| granite-4.2-3b | tools | 通过 |  | 56.376 s |
| qwen3-embedding-0.6b | context | 通过 | 32,767 | 20.387 s |
| qwen3-embedding-0.6b | quick | 通过 | 14 | 9.592 s |
| qwen3.5-0.8b | context | 通过 | 16,429 | 9.128 s |
| qwen3.5-0.8b | quick | 通过 | 17 | 452.417 s |
| qwen3.5-0.8b | stream | 通过 |  | 11.163 s |
| qwen3.5-0.8b | tools | 通过 |  | 39.214 s |
| qwen3.5-2b | context | 通过 | 65,579 | 30.343 s |
| qwen3.5-2b | quick | 通过 | 15 | 12.509 s |
| qwen3.5-2b | stream | 通过 |  | 26.165 s |
| qwen3.5-2b | tools | 通过 |  | 42.056 s |
| qwen3.5-4b | context | 通过 | 65,579 | 53.787 s |
| qwen3.5-4b | quick | 通过 | 15 | 26.736 s |
| qwen3.5-4b | stream | 通过 |  | 26.02 s |
| qwen3.5-4b | tools | 通过 |  | 57.293 s |
| qwen3.5-4b | vision | 通过 | 72 | 10.09 s |
| qwen3.5-4b | vision_context | 通过 | 65,637 | 44.88 s |
| qwen3.5-4b | vision_reverse | 通过 | 72 | 9.96 s |

### 系统 F

| 模型路线标签 | 检查项 | 结果 | 输入 token | 请求耗时 |
|---|---|---|---:|---:|
| gemma-4-e4b-it | context | 通过 | 65,590 | 98.443 s |
| gemma-4-e4b-it | quick | 通过 | 21 | 27.51 s |
| gemma-4-e4b-it | stream | 通过 |  | 28.042 s |
| gemma-4-e4b-it | tools | 通过 |  | 73.891 s |
| granite-4.0-h-tiny | context | 通过 | 65,599 | 19.692 s |
| granite-4.0-h-tiny | quick | 通过 | 35 | 43.818 s |
| granite-4.0-h-tiny | stream | 通过 |  | 27.296 s |
| granite-4.0-h-tiny | tools | 通过 |  | 75.377 s |
| granite-4.2-3b | context | 通过 | 65,589 | 145.179 s |
| granite-4.2-3b | quick | 通过 | 20 | 15.703 s |
| granite-4.2-3b | stream | 通过 |  | 35.482 s |
| granite-4.2-3b | tools | 通过 |  | 52.539 s |
| qwen3-embedding-0.6b | context | 通过 | 32,767 | 20.656 s |
| qwen3-embedding-0.6b | quick | 通过 | 14 | 8.122 s |
| qwen3.5-0.8b | context | 通过 | 16,429 | 13.326 s |
| qwen3.5-0.8b | quick | 通过 | 17 | 445.22 s |
| qwen3.5-0.8b | stream | 通过 |  | 13.266 s |
| qwen3.5-0.8b | tools | 通过 |  | 40.825 s |
| qwen3.5-2b | context | 通过 | 65,579 | 61.282 s |
| qwen3.5-2b | quick | 通过 | 15 | 16.738 s |
| qwen3.5-2b | stream | 通过 |  | 25.29 s |
| qwen3.5-2b | tools | 通过 |  | 47.444 s |
| qwen3.5-4b | context | 通过 | 65,579 | 93.753 s |
| qwen3.5-4b | quick | 通过 | 15 | 33.039 s |
| qwen3.5-4b | stream | 通过 |  | 25.658 s |
| qwen3.5-4b | tools | 通过 |  | 71.731 s |
| qwen3.5-4b | vision | 通过 | 70 | 43.053 s |
| qwen3.5-4b | vision_context | 通过 | 65,635 | 84.749 s |
| qwen3.5-4b | vision_reverse | 通过 | 70 | 27.518 s |

### 系统 G

| 模型路线标签 | 检查项 | 结果 | 输入 token | 请求耗时 |
|---|---|---|---:|---:|
| gemma-4-e4b-it | context | 通过 | 65,590 | 92.696 s |
| gemma-4-e4b-it | quick | 通过 | 21 | 38.329 s |
| gemma-4-e4b-it | stream | 通过 |  | 43.549 s |
| gemma-4-e4b-it | tools | 通过 |  | 66.616 s |
| granite-4.0-h-tiny | context | 通过 | 65,599 | 69.777 s |
| granite-4.0-h-tiny | quick | 通过 | 35 | 33.17 s |
| granite-4.0-h-tiny | stream | 通过 |  | 31.751 s |
| granite-4.0-h-tiny | tools | 通过 |  | 63.338 s |
| granite-4.2-3b | context | 通过 | 65,589 | 100.849 s |
| granite-4.2-3b | quick | 通过 | 20 | 23.355 s |
| granite-4.2-3b | stream | 通过 |  | 28.75 s |
| granite-4.2-3b | tools | 通过 |  | 44.226 s |
| qwen3-embedding-0.6b | context | 通过 | 32,767 | 23.055 s |
| qwen3-embedding-0.6b | quick | 通过 | 14 | 8.924 s |
| qwen3.5-0.8b | context | 通过 | 16,429 | 16.74 s |
| qwen3.5-0.8b | quick | 通过 | 17 | 504.813 s |
| qwen3.5-0.8b | stream | 通过 |  | 15.095 s |
| qwen3.5-0.8b | tools | 通过 |  | 36.672 s |
| qwen3.5-2b | context | 通过 | 65,579 | 76.731 s |
| qwen3.5-2b | quick | 通过 | 15 | 20.949 s |
| qwen3.5-2b | stream | 通过 |  | 25.194 s |
| qwen3.5-2b | tools | 通过 |  | 37.552 s |
| qwen3.5-4b | context | 通过 | 65,579 | 90.807 s |
| qwen3.5-4b | quick | 通过 | 15 | 41.84 s |
| qwen3.5-4b | stream | 通过 |  | 40.812 s |
| qwen3.5-4b | tools | 通过 |  | 54.999 s |
| qwen3.5-4b | vision | 通过 | 70 | 29.619 s |
| qwen3.5-4b | vision_context | 通过 | 65,635 | 87.496 s |
| qwen3.5-4b | vision_reverse | 通过 | 70 | 26.283 s |

## 我如何测试 Hermes 的可用性

我在长提示开头附近放置一个合成标记，并要求模型在填充文本后返回该标记。响应必须给出预期值。请求大小由服务器报告的输入 token 数确定。即使模型在大提示后能正常回答，只要开头标记错误，测试仍然失败。

Qwen3.5 35B 渐进测试使用编号填充记录、温度 0，以及逐步增加到 3,800、6,800、10,000 和 13,600 条记录的输入。这些阶段分别返回 69,429、124,179、182,579 和 248,279 个提示 token。模型在各阶段之间保持加载，因此可以复用前缀。单独进行的 Qwen3.6 接近上限检查报告缓存 token 为零。

0.8B 长提示在开头答案键与最后的回忆问题之间，将 `river stone lantern orchard circuit velvet compass marble` 重复了 8,400 次。原生运行发送了 `think:false`、`num_ctx:131072`、`stream:false` 和 `keep_alive:0`。OpenAI 兼容路径使用 `reasoning_effort:"none"`。代理对其路线强制使用无思考模式，因此网关调用方不需要在客户端覆盖设置。

### 工具、视觉和释放检查

工具测试检查了请求，以及工具结果返回后的回答。一个简单测试调用 `add_numbers(7, 11)` 并期待 18。Qwen3.5 35B 测试调用 `lookup_square` 并期待 49。GPT-OSS 执行库存查询，并需要在回答中使用返回的库存结果。

视觉检查使用红色和蓝色图像问答、反转图像顺序，以及包含图像颜色和首尾标记的长提示。Qwen3.5 35B 测试使用一张 256 × 256 的红色 PNG。代理需要修复图像内容转换后，该请求才通过。系统 E 的 4B 长视觉测试要求两个标记和颜色顺序都能在输入中保留下来。

我在长时间运行期间及前后检查了 GPU 内存、模型驻留、温度、主机内存压力、OOM 事件和 GPU 故障。Qwen3.5 35B 保护机制还检查了受控中断后的资源释放。后续的客户端取消和排队请求测试覆盖了代理路径。两个排队请求证明系统能在测试负载下处理请求，不代表有两个独立 GPU 后端同时运行。

### 如何解读性能结果

请求耗时包括长输入预填充和返回的回答，不等同于每秒生成 token 数。流式输出需要关注首个内容到达时间，缓存前缀的渐进结果也需要单独解读。

系统 A 和 C 上较大模型的成功后续测试使用了挖矿暂停时的专用推理窗口。请求结束后，模型被卸载。测试窗口结束时，七套系统都恢复了挖矿。这些结果描述的是推理窗口中的模型服务，并非同时挖矿和推理。

## 测试使用的后端配置

选择与你要复现的工作负载对应的配置。量化、运行时上下文、缓存类型、推理模式和 GPU 分配都会影响结果。

| 系统和模型 | 测试过的后端配置 |
|---|---|
| A，Qwen3.5 35B-A3B Q4_K_M | Ollama 0.34.2、f16 KV 缓存、两张 16GB RTX 5060 Ti、64 GiB 主机 RAM；大型渐进测试使用 262,144 运行时上下文。原生请求使用 `think:false`、温度 0、流式输出，并在阶段间保持活动五分钟。网关请求经过代理和 LiteLLM。请求没有输出上限。 |
| A，Qwen3.8 27B | 通过代理和 LiteLLM 按需运行 llama.cpp，262,144 运行时上下文、一个推理槽、Q4 K/V 缓存、两张 RTX 5060 Ti。66,007 token 请求没有输出上限。 |
| A，Qwen3.6-35B-A3B UD-Q4_K_XL | Strata 0.1.48、131,072 上下文、INT8 KV 缓存、一张指定 GPU、55 GiB 进程组内存限制、30 分钟运行时限制、延迟加载、空闲 60 秒后卸载。试运行长回答：217 个输出 token。接近上限的网关回答：11 个输出 token，且请求没有输出上限。 |
| A，Qwen3.8-Flash-Next UD-IQ4_XS | Strata 0.1.48、98,304 上下文、Q4 KV 缓存、8 GiB 常驻专家缓存、两张 RTX 5060 Ti。试运行内存限制 52 GiB，后续路线 54 GiB。试运行长回答：10 个输出 token。此前更大的上下文/缓存组合在内存限制处停止。 |
| A，Granite 4.2 8B | Q6_K GGUF 权重、llama.cpp 共享工作进程、131,072 上下文、Q4_0 K/V 缓存、`--n-predict -1`。长请求使用温度 0、流式使用量统计，且没有输出上限。 |
| A，DeepSeek Coder V2 16B | Q4_0 GGUF 权重、Ollama 0.34.2、两张 RTX 5060 Ti、64 GiB 主机 RAM。单独的 f16、Q4_0 和 Q8_0 缓存测试使用了比较表中的运行时上下文。请求没有输出上限。 |
| B、C、D，经过审计的 Ollama 服务 | Ollama 0.34.2、131,072 上下文、并行度 1、加载一个模型、队列大小 128、keep-alive 0、Flash Attention、Q4_0 KV 缓存。 |
| B，Qwen3.5 9B 网关试运行 | LiteLLM 路线超时 1,800 秒、零次重试、不限制上下文或输出 token。输入 72,265 个 token 时保留了两个哨兵。单独的挖矿恢复检查通过。 |
| C，Qwen3.5 0.8B | Q8_0 权重运行在一张 RTX 2000E Ada 上，功率配置为 30 W。运行时上下文 131,072。原生 `think:false`、OpenAI 兼容 `reasoning_effort:"none"`，无输出上限。代理别名固定运行时上下文并强制使用无思考模式。 |
| C，Gemma 4 12B-IT | 单 GPU Ollama 配置、131,072 运行时上下文，Aperture 流式和非流式请求均无输出上限。Aperture 直接运行在设为 30 W 的配置下达到 75 C 和 30.64 W 峰值，随后卸载模型。 |
| D，Qwen3.5 9B、Gemma 4 12B-IT、GPT-OSS 20B | 通过 Aperture 测试确切的已安装制品，131,072 运行时上下文，单 GPU 完全驻留，自然完成且请求无输出上限。 |
| E、F、G，llama.cpp 聊天处理进程 | Build 11669、99 个 GPU 层、并行度 1、Flash Attention、Q4_0 K/V 缓存、`--n-predict -1`。运行时上下文因模型系列而异。 |

记录的服务配置描述的是各自的运行配置。系统 A 上单独测试的 f16 缓存 Qwen3.5 35B 配置，不继承较小 Ollama 系统的 Q4_0 缓存设置。

### 新增输入保留测试的模型指纹

这些模型标识符可将测试制品与名称相似的其他下载或别名区分开。

| 制品 | 量化 | 记录的摘要或文件 SHA-256 |
|---|---|---|
| Qwen3.5 35B-A3B Ollama 标签 | Q4_K_M | `72aac7c28be8ff9b81c2a270eb489c88e6d822a76ec0cb7bf34d965768848567` |
| Qwen3.5 0.8B 基础 Ollama 标签 | Q8_0 | `de63045f29755d4721c09d54c9b45c2dadb644f4fd7d604d4cac90d96049971c` |
| Granite 4.2 8B GGUF 文件 | Q6_K | `5ad3d67f6fe09a448031029bead7f6a088697ca2787c0c5640bf964c59df1a21` |

Ollama 清单摘要和权重文件 SHA-256 标识的是不同对象。请根据表中的制品类型匹配标识符。

## 我会在 Hermes 中运行什么

我会将 Qwen3.5 35B 作为双 RTX 5060 Ti 系统上的主要长上下文路线。通过网关保留 239,153 个 token、工具和视觉分别通过，以及请求资源释放经过验证，这些依据比模型宣称拥有大型上下文窗口更可靠。我会保留 Qwen3.8 27B，用于相同 66K 对比中更快的响应；当单卡运行更重要时，则使用 Qwen3.6。

在 RTX 2000E Ada 系统上，对于测试过的长输入响应工作负载，我会选用系统 C 上验证过的 Gemma 3 4B 路线。我会试用无思考模式的 Qwen3.5 0.8B 来做范围明确的回忆和提取。较大的 Gemma、Qwen 和 GPT-OSS 路线适合能够接受经测试的四到五分钟初始响应的任务。我会排除系统 D 上失败的 Gemma 3 路线。

对于 8GB RTX 3060 Ti 和 RTX 3070 显卡，我会从 Qwen3.5 2B 或 4B 开始。它们的 65K 文本结果和 4B 图像检查支持一种实用的起始配置，无需为每个请求都占用两张 16GB 显卡。测试配置中的 Flash Next 内存压力和 DeepSeek Coder V2 未完成的 65K 行为，使它们成为较弱的默认选择。

这些测试支持针对特定工作流的模型和系统选择。输入保留、正确的工具往返、图像识别和干净释放分别回答 Hermes 可用性的不同方面。可靠配置需要覆盖代理实际使用的行为，并为回答和工具流量留下足够上下文。

## 来源和相关阅读

- [Hermes Agent 提供商设置和上下文要求](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/integrations/providers.md)
- [NVIDIA GeForce RTX 3060 Ti 规格](https://www.nvidia.com/en-us/geforce/graphics-cards/30-series/rtx-3060-3060ti/)
- [NVIDIA GeForce RTX 5060 Ti 规格](https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5060-family/)
- [Hermes Agent 概览](/hermes-local-ai-broker-course/01-hermes-agent-overview/)
- [选择本地模型后端](/hermes-local-ai-broker-course/02-choose-a-backend/)
