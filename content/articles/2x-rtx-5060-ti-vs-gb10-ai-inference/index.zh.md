---
title: "2x RTX 5060 Ti 对比 GB10：256K 上下文下五款模型的本地 AI 基准测试"
date: 2026-10-10
lastmod: 2026-11-08
toc: true
draft: false
description: "对比 RTX 5060 Ti 与 GB10 上的五款模型，并展示同一主机上 Qwen3.8 Flash-Next Strata 运行至 256K 上下文的基准测试。"
genre: ["人工智能", "本地 AI", "GPU 硬件", "基准测试", "计算机硬件"]
tags: ["RTX 5060 Ti", "GB10", "DGX Spark", "Qwen3.8", "Qwen3.8 Flash-Next", "GSQ-RCO", "Qwen4Exp", "Strata", "Qwen3.5", "Qwen3.6", "GPT-OSS", "Nemotron", "本地 LLM", "本地推理", "统一内存", "VRAM", "GPU 基准测试", "长上下文", "PCIe 开销", "AI 硬件", "NVIDIA Blackwell", "LLM 性能", "GPU 内存"]
cover: "/img/cover/nvidia-rtx-5060-ti-vs-gb10-memory-performance-comparison.webp"
coverAlt: "插图左侧是两张 NVIDIA RTX 5060 Ti 显卡，右侧是 NVIDIA GB10 系统，两者在深色背景上以鲜艳色彩突出显示。"
coverCaption: "本地模型的性能取决于内存架构、模型选择和上下文长度。"
---

**两张 16 GB RTX 5060 Ti 显卡合计提供 32 GB VRAM。** NVIDIA GB10 系统提供 128 GB 一致性统一内存。新的五模型基准测试比之前仅测试 Qwen 的结果更全面。

在 256K 设置下，双卡系统的四款模型生成速度更快。GB10 在 Qwen3.8 27B 上明显领先，并为模型、上下文和运行时分配保留更多内存。最佳选择取决于模型和工作负载。

另一项同主机测试比较了 Strata 上的 Qwen3.8-Flash-Next IQ2_XS 与 Ollama 上的 dense Qwen3.8 27B Q4_K_M。预热后，Flash-Next 的生成速度中位数为每秒 92.8 个 token，提示词含 260,446 个 token。Dense Qwen3.8 使用含 260,444 个 token 的提示词，速度为每秒 0.939 个 token。

NVIDIA GB10 使用 128 GB 一致性统一内存。NVIDIA 列出的 GB10 平台规格包括 128 GB LPDDR5x 统一内存和 140 W 芯片 TDP。RTX 5060 Ti 每张卡使用 16 GB GDDR7、128 位内存接口，总图形功率为 180 W。[NVIDIA RTX 5060 Ti 规格](https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5060-family/)和 [NVIDIA GB10 规格](https://www.nvidia.com/en-us/products/workstations/dgx-spark/)说明了硬件差异。

**两种系统以不同方式提供内存。** 两张卡形成两个独立的 16 GB 内存池。GB10 将模型、上下文数据、运行时缓冲区和操作系统分配放在同一个共享地址空间中。

## 内存对比

| 系统 | 内存 | 内存模型 | 报告的功耗数据 |
|---|---:|---|---:|
| **2x RTX 5060 Ti 16 GB** | 合计 32 GB | 两个独立 GPU 内存池 | GPU 总计 360 W |
| **GB10 系统** | 128 GB | 一致性统一系统内存 | GB10 TDP 140 W |

GB10 并非因为 LPDDR5x 内存带宽匹配独立显卡，就能赢得每项吞吐测试。它的优势来自容量和内存放置方式。CPU 与 GPU 共享同一个地址空间，因此工作集无需塞进两个互相隔离的 16 GB 设备。

双卡系统面临内存放置问题。模型必须分到两张卡上。运行时必须在两张卡之间传输数据。PCIe 流量会增加延迟并占用带宽。根据 NVIDIA 规格，RTX 5060 Ti 也不支持 NVLink。

## 五模型基准测试

更新后的测试在两种系统上使用相同的请求矩阵，涵盖五款 Ollama 模型以及 4K、16K、32K、64K、128K 和 256K 上下文设置。每个请求以温度 0 生成 128 个 token。

测试使用以下模型标签：

- **Qwen3.8 27B：** `qwen3.8:27b`
- **GPT-OSS 20B：** `gpt-oss:20b`
- **Qwen3.6 35B-A3B：** `qwen3.6:35b`
- **Qwen3.5 35B-A3B：** `qwen3.5:35b-a3b-q4_K_M`
- **Nemotron 3.5 Lightning 30B-A3B：** `nemotron-3.5-lightning:30b-a3b-q4_K_M`

双卡系统使用两张 16 GB RTX 5060 Ti。GB10 系统使用 128 GB 统一内存。测试使用 Ollama，双卡系统版本为 0.34.2，GB10 版本为 0.40.2。

### 生成速度

生成速度衡量模型在提示词处理完后生成 token 的速度。交互式对话最看重这项指标。

双 RTX 5060 Ti 系统：

| 上下文 | GPT-OSS 20B | Nemotron 3.5 | Qwen3.5 35B | Qwen3.6 35B | Qwen3.8 27B |
|---:|---:|---:|---:|---:|---:|
| 4K | 91.518 | 162.027 | 117.547 | 156.104 | 55.654 |
| 16K | 87.176 | 161.377 | 112.903 | 140.596 | 51.656 |
| 32K | 82.372 | 157.055 | 106.455 | 144.833 | 47.369 |
| 64K | 74.661 | 135.106 | 95.979 | 125.008 | 38.863 |
| 128K | 62.767 | 130.924 | 79.572 | 115.352 | 26.399 |
| 256K | 67.853 | 106.221 | 58.947 | 67.159 | 1.079 |

GB10：

| 上下文 | GPT-OSS 20B | Nemotron 3.5 | Qwen3.5 35B | Qwen3.6 35B | Qwen3.8 27B |
|---:|---:|---:|---:|---:|---:|
| 4K | 62.199 | 98.648 | 72.405 | 100.906 | 32.985 |
| 16K | 56.764 | 94.366 | 69.782 | 95.448 | 32.939 |
| 32K | 53.257 | 98.175 | 64.055 | 95.025 | 29.772 |
| 64K | 49.201 | 96.132 | 58.428 | 84.528 | 25.625 |
| 128K | 40.637 | 80.238 | 48.108 | 74.579 | 22.294 |
| 256K | 43.688 | 68.043 | 36.649 | 62.115 | 22.371 |

在 256K 下，双卡系统在 GPT-OSS、Nemotron、Qwen3.5 和 Qwen3.6 上生成更快。GB10 在 Qwen3.8 上更快。双卡系统的 Qwen3.8 速度降到每秒 1.079 个 token，而 GB10 达到每秒 22.371 个 token。

Qwen3.6 的结果接近。双卡系统达到每秒 67.159 个 token，GB10 达到每秒 62.115 个 token。结果不支持“统一内存总是更快”或“两张独立 GPU 总是更快”这类普遍结论。

### 提示词处理速度

提示词处理速度衡量运行时在生成前读取输入上下文的速度。长文档和重复加载上下文时，这项指标很重要。

双 RTX 5060 Ti 系统：

| 上下文 | GPT-OSS 20B | Nemotron 3.5 | Qwen3.5 35B | Qwen3.6 35B | Qwen3.8 27B |
|---:|---:|---:|---:|---:|---:|
| 4K | 4745.9 | 2409.0 | 2701.7 | 464.3 | 783.9 |
| 16K | 7617.0 | 3031.8 | 4175.3 | 2654.0 | 840.1 |
| 32K | 8099.5 | 3074.2 | 4335.8 | 2623.2 | 811.2 |
| 64K | 6809.5 | 2893.0 | 4129.9 | 2400.4 | 727.8 |
| 128K | 5089.9 | 2362.7 | 3084.0 | 1723.6 | 546.1 |
| 256K | 5838.3 | 1813.2 | 2229.1 | 1011.0 | 251.3 |

GB10：

| 上下文 | GPT-OSS 20B | Nemotron 3.5 | Qwen3.5 35B | Qwen3.6 35B | Qwen3.8 27B |
|---:|---:|---:|---:|---:|---:|
| 4K | 3295.5 | 576.0 | 2067.9 | 628.8 | 756.9 |
| 16K | 4675.5 | 3006.7 | 2691.2 | 2556.3 | 812.6 |
| 32K | 4571.4 | 3077.9 | 2691.7 | 2563.9 | 794.1 |
| 64K | 3704.7 | 3066.9 | 2585.3 | 2444.9 | 714.0 |
| 128K | 2857.0 | 2802.9 | 2360.4 | 2229.9 | 655.5 |
| 256K | 3243.4 | 2325.4 | 1938.5 | 1817.6 | 535.1 |

在 256K 下，双卡系统在 GPT-OSS 和 Qwen3.5 的提示词处理上领先。GB10 在 Nemotron、Qwen3.6 和 Qwen3.8 上领先。模型架构和运行时行为与内存接口同样重要。

## 补充 Qwen3.8 Flash-Next 基准测试

三次额外测试在双 RTX 5060 Ti 系统上测量了 Qwen3.8 Flash-Next GGUF 包，使用 4K 和 16K 上下文设置。每一行都列出 Hugging Face 模型的精确引用和量化格式。

| 精确模型 | 量化格式 | 4K 生成速度 | 16K 生成速度 |
|---|---:|---:|---:|
| [`hf.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF:IQ2_XS`](https://huggingface.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF/tree/main/IQ2_XS) | IQ2_XS | 31.77 tok/s | 28.20 tok/s |
| [`hf.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF:IQ3_S`](https://huggingface.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF/tree/main/IQ3_S) | IQ3_S | 24.54 tok/s | 22.60 tok/s |
| [`hf.co/orcarouter/Qwen3.8-Flash-Next-Uncensored-GGUF:Q4_K_M`](https://huggingface.co/orcarouter/Qwen3.8-Flash-Next-Uncensored-GGUF/tree/main) | Q4_K_M | 17.91 tok/s | 17.02 tok/s |

IQ2_XS 包在这一组中的吞吐最高。它在 4K 下达到每秒 31.77 个 token，高于 IQ3_S 的 24.54 和 Q4_K_M 的 17.91。在 16K 下，顺序相同，分别为 28.20、22.60 和 17.02 个 token 每秒。

使用 Ollama 运行相同的模型引用：

```bash
ollama run hf.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF:IQ2_XS
ollama run hf.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF:IQ3_S
ollama run hf.co/orcarouter/Qwen3.8-Flash-Next-Uncensored-GGUF:Q4_K_M
```

这些早期补充结果来自双 GPU 系统，与上文 RTX 5060 Ti 和 GB10 的匹配请求矩阵分开。记录包含精确模型引用、量化格式、请求的上下文设置和生成速度，但没有已解析的 manifest digest、已处理提示词 token 数、输出长度、预热状态、设备分配、CPU、系统 RAM、散热配置或测量日期。

## 256K 下 Strata 对比 dense Ollama

**2026 年 10 月 14 日的第二项基准测试，在同一台双 RTX 5060 Ti 主机上比较了两种模型与运行时组合。** Dense 基线使用 Ollama 上的 [`qwen3.8:27b`](https://ollama.com/library/qwen3.8:27b)，这是采用 Q4_K_M 的 273 亿参数 Qwen35 模型。Flash 组合使用 [Qwen3.8-Flash-Next IQ2_XS](https://huggingface.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF/tree/main/IQ2_XS)，这是 Strata 统一原生包中的 Qwen4Exp 混合专家模型。

这是整个技术栈的比较。模型架构、量化、打包方式、专家路由和推理引擎都同时改变。本轮不包括 IQ3_S 和 Q4_K_M Flash 变体。

### 测试系统和方法

| 组件 | 记录的配置 |
|---|---|
| **GPU** | 2x NVIDIA GeForce RTX 5060 Ti，每张 16 GiB，compute capability 12.0 |
| **GPU 链路** | 每张卡 PCIe 4.0 x4，PHB 拓扑，无 NVLink |
| **CPU** | AMD Ryzen 9 5900XT，32 线程 |
| **主机内存** | 62 GiB RAM 和 15 GiB swap |
| **NVIDIA 驱动** | 595.99.02 |

测试程序生成了编号的合成记录。每行采用 `Record 00001: alpha beta gamma delta epsilon zeta eta theta iota kappa.` 格式。指令要求先输出 `BENCHMARK_OK`，再生成简洁的技术总结，直到输出上限。六个提示词包含 180、720、1,500、3,100、6,200 和 12,400 条记录。

每次运行使用温度 0、seed 42，最多输出 128 个 token。每种上下文先预热一次，再测量五个请求。Ollama 测试使用 `/api/generate`，Strata 测试使用 `/v1/chat/completions`。所有测量请求均完成，未出现 API 错误。

解码控制并不一致。Strata 明确将 `reasoning_effort` 设为 `none`，并通过 chat template 禁用 thinking。Dense Ollama 请求未发送 `think: false`，后续探测在 thinking 和 response 字段中发现了输出。因此，生成结果只适用于记录的解码模式。

| 上下文设置 | Dense 提示词 token 数 | Flash 提示词 token 数 |
|---:|---:|---:|
| **4K** | 3,824 | 3,826 |
| **16K** | 15,164 | 15,166 |
| **32K** | 31,544 | 31,546 |
| **64K** | 65,144 | 65,146 |
| **128K** | 130,244 | 130,246 |
| **256K** | 260,444 | 260,446 |

两个模型的 header 都声明最大上下文为 262,144 个 token。每个检查点上的配对提示词只相差两个 token。

### 预热后生成速度中位数

每个中位数包含一次预热后的五个测量请求。每个 Dense 测量请求重复使用前一个提示词的所有内容，只改动四个 token。每个 Flash 请求只改动七个 token。该表测量的是带预热前缀缓存的解码吞吐，不是冷启动到完整响应的延迟。

| 上下文 | Strata 上的 Flash IQ2_XS | Ollama 上的 Dense Q4_K_M | Flash 领先幅度 |
|---:|---:|---:|---:|
| **4K** | 98.4 tok/s | 65.0 tok/s | 1.51x |
| **16K** | 96.8 tok/s | 60.6 tok/s | 1.60x |
| **32K** | 95.3 tok/s | 64.4 tok/s | 1.48x |
| **64K** | 89.6 tok/s | 51.2 tok/s | 1.75x |
| **128K** | 92.9 tok/s | 31.5 tok/s | 2.95x |
| **256K** | 92.8 tok/s | 0.939 tok/s | 98.9x |

从 64K 到 256K，Flash 组合保持在每秒约 90 个 token。Dense Qwen3.8 在 64K 后明显变慢，在 256K 时降至每秒 0.939 个 token。256K Flash 响应在 67 个 token 后正常结束。Dense 运行达到 128-token 输出上限。

### 第一次请求的提示词处理

| 上下文 | Flash 第一次请求 | Dense 第一次请求 |
|---:|---:|---:|
| **4K** | 1,134 tok/s | 832 tok/s |
| **16K** | 2,013 tok/s | 856 tok/s |
| **32K** | 2,386 tok/s | 799 tok/s |
| **64K** | 2,509 tok/s | 690 tok/s |
| **128K** | 2,538 tok/s | 489 tok/s |
| **256K** | 2,399 tok/s | 214 tok/s |

Dense 的第一次请求在每个检查点都处理了完整提示词。Strata 在 64K、128K 和 256K 分别复用了 16,384、49,152 和 114,688 个前缀 token。因此，64K 至 256K 的 Flash 速度属于首次请求的续传吞吐，不是完全没有缓存的 prefill。

在 256K 下，Strata 用 60.8 秒处理了第一次请求。Ollama 用时约 1,215.4 秒。前缀复用意味着此检查点无法直接比较冷启动 prefill。

### 运行时放置方式解释了长上下文差异

Ollama 0.34.2 使用 llama-server 0.4.1-dev，启用 CUDA 层卸载、ChatML template 和最大 draft 宽度为四的 MTP speculative decoding。32K 时 batch 和 microbatch 均为 1,024；64K 至 256K 时均为 512。32K 和 64K 时，全部 66 层 dense layer 都留在 GPU 上。128K 时，66 层中有 63 层留在 GPU 上，另有 1,404 MiB 转入 CPU 映射内存。256K 时，66 层中有 42 层留在 GPU 上，另有 6,002 MiB 转入 CPU 映射内存。256K 的 MTP 接受率约为 69.4%。

Strata 0.1.44.1 配合 CUDA 13.0.3，将 48 层分布在两张 GPU 上。4K 和 16K 配置将第 0 至 23 层放在第一张 GPU，第 24 至 47 层放在第二张 GPU。本轮使用自动 700 MiB VRAM 预留和 16,047 个常驻 expert slot。

32K 至 256K 配置将第 0 至 24 层放在第一张 GPU，第 25 至 47 层放在第二张 GPU。本轮使用自动 prefill、0.5 speculative minimum probability、INT8 KV 存储、每个 QSA layer 32,768 个常驻 KV cell、832 MiB VRAM 预留、包含 15,318 个 slot 和 21,024 MiB 的 expert cache，以及最大 draft 宽度为四的 MTP speculative decoding。

Strata native 和 PLE blob 的 digest 为 `sha256:1473e0664c2017095f9164b6d617d7a71893452c1180c83002c4f28fc8c2b0da`。运行还依赖 expert profile 和 MTP draft pack，但它们没有公开不可变 digest。

Strata 运行使用默认的 route-tail skip 模式。此设置会轻微改变模型输出，因此结果仅适用于记录的运行时配置。Flash 响应带有 `BENCHMARK_OK` 标记。Dense 请求没有 API 错误，但主测试程序未捕获标记。原始行记录的 response character 数为零。后续探测在 response 和 thinking 字段中找到了输出，并确认 response 中有 `BENCHMARK_OK`。

4K 和 16K 配置的一项请求记录到 409 MiB 可用显存，并建议预留 832 MiB。长上下文配置的一项请求记录到 481 MiB 可用显存，并建议预留 896 MiB。两个值都低于引擎 512 MiB 的 driver-paging 阈值。没有请求失败，但低内存状态会影响复现稳定性。

**应将 98.9x 视为长上下文完整技术栈的结果，而非证明引擎本身快 98.9 倍。** 测试固定了主机，没有单独隔离模型、量化或运行时的影响。

## 实际提示词长度很重要

请求的上下文长度不等于实际处理的提示词 token 数。在 256K 设置下，Qwen3.5、Qwen3.6、Nemotron 和 Qwen3.8 在两种系统上都处理了约 171,359 至 171,365 个实际提示词 token。

GPT-OSS 在两种系统的 256K 设置下都处理了 65,538 个实际提示词 token。因此，它的 256K 数据行与其他模型的输入长度并不相同。

256K Qwen3.8 结果最能体现差异。双卡系统以每秒 251.3 个 token 处理了 171,359 个提示词 token，生成速度为每秒 1.079 个 token。GB10 处理了相同数量的提示词 token，速度为每秒 535.1 个 token，生成速度为每秒 22.371 个 token。

**上下文设置表示请求的上限。** 实际提示词 token 数表示运行时完成了多少工作。

## 合计 VRAM 仍然重要

### 1. 模型看不到一张 32 GB 显卡

两张 GPU 不会将显存合并为一个本地地址空间。Model-parallel 运行时会将层或张量分配到不同设备。每个设备都需要空间存放分配给它的权重、临时缓冲区和部分上下文状态。

可用容量低于简单相加的结果。具体开销取决于模型格式、量化、推理后端、张量拆分和上下文长度。

### 2. 生成期间上下文内存会增长

模型权重只占内存预算的一部分。键值缓存（KV cache）会保存先前 token 的 attention 数据。上下文越长，所需缓存内存越多。4K 测试不能预测 128K 或 256K 部署的表现。

新结果显示，不同模型有不同的性能瓶颈。256K 下，双卡系统的 Qwen3.8 生成速度严重下降。其他四款模型在两种系统上都保持了可用的生成速度。内存容量仍然重要，因为它决定模型和上下文组合能否在留出运行时分配空间后装入系统。

### 3. PCIe 传输会增加成本

运行时在 GPU 之间移动 activation 或张量时，数据会经过主机互连。每个步骤都会增加同步点和延迟。惩罚程度取决于张量放置、模型架构、量化和上下文长度。

这并不意味着双 GPU 系统毫无用处。运行时配置和模型共同决定结果。只报告 4K 提示词处理速度的基准测试不会显示这项成本。

### 4. 能效是系统级优势

GB10 在提供更多内存容量的同时，报告的芯片或 GPU 功耗更低。两张 RTX 5060 Ti 的 GPU 总功耗为 360 W，还未计入系统其他部分。NVIDIA 列出的 GB10 TDP 为 140 W。

**GB10 以多个模型上的峰值吞吐为代价，换来更大容量、共享工作集和更低的报告 GPU 功耗。** 在本测试中，双卡系统在多个较新的 MoE 模型上测得更高吞吐。

## 5060ti-x2 系统便宜得多

2026 年 10 月 10 日，一台配备两张 16 GB RTX 5060 Ti 的完整工作站标价 **$3,479**。配置包括 Intel Ultra 7 265K、Z890 主板、32 GB DDR5、1 TB 存储、1,000 W 电源和两张 GPU。[查看双 GPU 完整工作站列表](https://greenbeastgaming.com/products/dual-gpu-rtx-5060-ti-16gb-intel-focus-g-white)。

NVIDIA 美国 marketplace 将 128 GB DGX Spark 标价 **$6,950**。商品包括 128 GB 一致性统一内存和 4 TB NVMe 存储，但显示缺货。[查看 NVIDIA 当前 DGX Spark 商品](https://marketplace.nvidia.com/en-us/enterprise/personal-ai-supercomputers/dgx-spark/)。

AMD Ryzen AI Halo Developer Platform 提供另一项对比。Micro Center 上的 Strix Halo 系统售价 **$3,999.99**，配备 128 GB LPDDR5x 统一内存和 2 TB 存储。Strix Halo 通常属于与 GB10 系统相近的实用本地 AI 级别，但独立测试经常显示 GB10 的吞吐和软件成熟度更高。[查看 Micro Center 当前 Linux 商品](https://www.microcenter.com/product/711961/amd-ryzen-ai-halo-developer-platform?osfs=false)，并[阅读 Strix Halo 对比 GB10 的评测](https://www.tomshardware.com/pc-components/gpus/embargo-mon-july-6-8am-pt-1100-edt-amd-ryzen-ai-halo-review/4)。

| 完整系统 | 2026 年 10 月 10 日标价 | 价格差额 |
|---|---:|---:|
| **5060ti-x2 工作站** | $3,479 | 基准价 |
| **AMD Ryzen AI Halo，Strix Halo** | $3,999.99 | 高 $520.99 |
| **128 GB GB10 DGX Spark** | $6,950 | 高 $3,471 |

GB10 提供更大的统一内存池和更低的报告 GPU 功耗。AMD 系统以约 $4,000 提供同级别的 128 GB 内存。税费和运费前，5060ti-x2 工作站的价格约为 GB10 标价的 **50%**。

这些是不同供应商的标价，并非受控的零售购物清单。5060ti-x2 系统的系统内存和存储也较少。目前 16 GB RTX 5060 Ti 显卡单张售价约 **$789 至 $830**，远高于 $429 的首发建议零售价。即使 GPU 价格目前上涨，双卡系统仍有价格优势。[查看 RTX 5060 Ti 当前价格](https://www.pcgamer.com/hardware/graphics-cards/graphics-card-price-watch-deals/)。

## 对本地 AI 工作负载的意义

双 16 GB 显卡配置可在长上下文设置下运行多款量化后的 27B 至 35B 模型。基准测试没有给所有模型都选出同一个赢家。

如果你看重以下方面，请选择双卡系统：

- **本测试中 GPT-OSS、Nemotron、Qwen3.5 和 Qwen3.6 的更高生成速度。**
- **五款模型在短上下文下的更高吞吐。**
- **低于标价 GB10 系统的采购成本。**
- **NVIDIA 独立 GPU 软件兼容性**以及测试新模型的空间。

如果你看重以下方面，请选择 GB10：

- **256K 下运行 Qwen3.8 27B**，GB10 的生成速度超过 20 倍。
- **单一 128 GB 内存池**，为模型权重、KV cache 和运行时缓冲区留出更多空间。
- **低于两张独立显卡的报告 GPU 或芯片功耗。**
- **减少多设备内存放置限制**，适用于令双卡配置承压的模型。

这与[16GB VRAM 是否足以认真运行本地 LLM？](/articles/is-16gb-vram-enough-local-llm/)中的容量规划建议一致，该指南将权重、上下文和运行时分配视为同一预算。[Qwen 27B 的 32GB VRAM 指南](/articles/32gb-vram-qwen-27b-hardware-guide/)对双卡配置也得出相同结论。合计容量不等于可用余量。

为长上下文部署购买硬件前，先问四个问题：

- **所选量化格式能否与运行时缓冲区一起装入内存？** 仅看模型权重无法确定内存需求。
- **上下文能否装入，同时避免 KV cache 严重受限？** 长提示词会改变结果。
- **运行时能否高效拆分设备工作？** PCIe 传输和张量放置会影响每个生成的 token。
- **系统能否完成目标上下文？** 4K 下的快速结果无法弥补 256K 工作负载失败。

**新的基准测试按模型回答了这些问题。** 256K 下，Qwen3.8 明显更适合 GB10。在此特定配置中，其他四款模型的生成速度更适合双卡系统。更大的统一内存池仍提供更多容量余量，即使它没有带来最高的实测吞吐。

同一双 GPU 硬件还在 Strata 上以 Flash-Next IQ2_XS 运行 256K，记录到预热后每秒 92.8 个 token 的中位数。这项独立结果不会推翻 dense Qwen3.8 在 GB10 上的表现。Flash-Next 使用不同的混合专家架构、量化、软件包、运行时和解码模式。本数据集中没有 GB10 上的匹配 Flash-Next 结果。

## 结论

**在 256K 下测试的五款模型中，双 RTX 5060 Ti 系统有四款生成速度更快。** 它的标价也约为 GB10 系统的一半。对于 256K 下的 Qwen3.8 27B、容量余量以及适合共享内存池的工作负载，GB10 仍是更好的选择。

之前仅测试 Qwen 的结果暗示 GB10 会轻松获胜。更新后的五模型测试说明这个结论过于宽泛。模型架构、运行时版本、张量放置和上下文行为都会影响结果。

如果你运行 GPT-OSS、Nemotron 3.5 Lightning、Qwen3.5 或 Qwen3.6，这次基准测试中双卡系统的生成速度更高。如果你在 256K 下运行 Qwen3.8 27B，GB10 仍保持可用生成速度，而双卡系统几乎停滞。

**内存容量和吞吐是不同的购买标准。** GB10 提供四倍合计内存和更简单的共享工作集。双卡系统在大多数测试模型上提供更高的实测吞吐，系统标价则低得多。

Strata 结果还带来另一点启示。在同一台双 GPU 主机上，运行时放置、模型架构和解码模式改变了 256K 结果。Flash-Next IQ2_XS 的预热后中位数接近每秒 93 个 token，而 dense Qwen3.8 将 24 层卸载到 GPU 之外，速度降到每秒一个 token 以下。

## 基准测试限制

基准测试记录了模型标签、请求的上下文、实际提示词 token 数、提示词处理速度、生成速度、Ollama 版本和 128-token 生成目标。它没有记录已解析的 manifest digest、CPU 功耗、墙上插座功耗、风扇速度或散热配置。

两个系统的 GPT-OSS 256K 数据行都处理了 65,538 个实际提示词 token。其他 256K 数据行处理了约 171K 个实际提示词 token。应将这些数字视为观测到的系统对比，而非所有 RTX 5060 Ti 双卡组合和所有 GB10 实现的通用排名。

Strata 对比 dense 的测试记录了精确提示词数量、每种上下文的五个测量请求、运行时版本、设备放置、缓存设置和请求状态。模型架构、量化、打包方式、运行时和解码模式同时改变。32K 以上时 Strata 还复用了提示词前缀。两个技术栈的测量生成请求都复用了几乎整个提示词。

无法仅凭本文精确复现测试。基准测试 harness、Strata 包布局、expert profile 和 MTP draft pack 没有公开不可变 digest。低 VRAM 警告也会增加不同运行之间的变化风险。测试固定了主机，而非推理引擎。

上述硬件规格来自 NVIDIA。性能数据来自本文的受控基准测试。

## 参考资料

- [Ollama Qwen3.8 模型库](https://ollama.com/library/qwen3.8)
- [ISTA-DASLab Qwen3.8 Flash-Next GSQ-RCO GGUF 模型](https://huggingface.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF)
- [orcarouter Qwen3.8 Flash-Next Uncensored GGUF 模型](https://huggingface.co/orcarouter/Qwen3.8-Flash-Next-Uncensored-GGUF)
- [Ollama Qwen3.5 模型库](https://ollama.com/library/qwen3.5)
- [Ollama Qwen3.6 模型库](https://ollama.com/library/qwen3.6)
- [Ollama Nemotron 3.5 Lightning 模型库](https://ollama.com/library/nemotron-3.5-lightning)
- [Ollama GPT-OSS 模型标签](https://ollama.com/library/gpt-oss/tags)
- [16GB VRAM 是否足以认真运行本地 LLM？](/articles/is-16gb-vram-enough-local-llm/)
- [Qwen 27B 的 32GB VRAM 指南](/articles/32gb-vram-qwen-27b-hardware-guide/)
- [本地 AI GPU 上下文指南](/articles/local-ai-model-gpu-context-guide/)
- [Vast.ai 上的 Qwen3.8 27B GPU 基准测试](/articles/qwen38-27b-vast-ai-gpu-benchmark/)
- [双 RTX 5060 Ti 16 GB 完整工作站列表](https://greenbeastgaming.com/products/dual-gpu-rtx-5060-ti-16gb-intel-focus-g-white)
- [NVIDIA DGX Spark 美国 marketplace 商品](https://marketplace.nvidia.com/en-us/enterprise/personal-ai-supercomputers/dgx-spark/)
- [AMD Ryzen AI Halo 128 GB Linux 商品](https://www.microcenter.com/product/711961/amd-ryzen-ai-halo-developer-platform?osfs=false)
- [Tom's Hardware Strix Halo 对比 GB10 评测](https://www.tomshardware.com/pc-components/gpus/embargo-mon-july-6-8am-pt-1100-edt-amd-ryzen-ai-halo-review/4)
- [RTX 5060 Ti 当前价格](https://www.pcgamer.com/hardware/graphics-cards/graphics-card-price-watch-deals/)
