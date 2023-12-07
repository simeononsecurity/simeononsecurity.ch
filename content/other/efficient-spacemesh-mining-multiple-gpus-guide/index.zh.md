---
title: "使用多 GPU 高效进行 Spacemesh 挖矿--最大化您的回报"
date: 2023-08-18
toc: true
draft: false
description: "了解如何利用生态友好型 PoST 算法优化使用多个 GPU 的 Spacemesh 挖矿，并最大限度地提高您的回报。"
genre: ["加密货币", "区块链", "采矿", "技术", "分散式", "GPU 采矿", "时空证明", "环保", "加密货币小贴士", "数字资产"]
tags: ["太空网", "采矿", "图形处理器", "时空证明", "加密货币", "区块链", "环保", "分散式", "PoST 算法", "采矿指南", "加密货币小贴士", "奖励", "优化", "节能", "GPU 采矿", "数字资产", "技术", "非集中化", "空间证明", "时空挖掘", "采矿效率最大化", "生态友好型加密货币", "Spacemesh 网络", "GPU 挖矿设置", "使用多个 GPU 挖矿", "去中心化区块链采矿", "加密货币挖矿技巧", "高效 GPU 采矿", "时空算法证明", "加密货币奖励"]
cover: "/img/cover/spacemesh-mining-gpus.png"
coverAlt: "一幅卡通风格的插图，展示了多个 GPU 协同工作开采 Spacemesh 的情况。"
coverCaption: "矿山更智能，矿山更环保！"
---
导言

Spacemesh 是一个开创性的加密货币平台，它采用一种名为 "时空证明"（PoST）的高能效共识算法进行挖矿，是比特币等传统工作量证明（PoW）加密货币的生态友好型替代品。如果你有多个 GPU 并对 Spacemesh 挖矿感兴趣，本综合指南将指导你使用功能强大的 postcli 应用程序最大限度地挖掘挖矿潜力。

## 前提条件

在进入挖矿流程之前，请确保具备以下先决条件：

1.**多个 GPU：** 确保至少有两个 GPU 能够有效处理 Spacemesh 挖矿。

2.**postcli应用程序：** 从以下网址下载postcli应用程序 [here](https://github.com/spacemeshos/post/)并确保在系统环境路径中正确安装并可用。

## 使用多个 GPU 挖掘 Spacemesh

要开始使用多个 GPU 开采 Spacemesh，请按照以下简单步骤操作：

______

#### 第 1 步：配置变量

打开文本编辑器或 PowerShell 脚本编辑器，根据需要设置可配置变量。
所提供的脚本中已经包含了一些可以调整的变量，其他变量可以从在 spacemech GUI 应用程序上开始分析时获得的 json 文件中提取：

- `$numGpus`设置要用于挖矿的 GPU 数量。例如 `2`用于两个 GPU。

 `$commitmentAtxId`将其替换为您的承诺 ATX ID，这是您承诺参与 Spacemesh 网络的唯一标识符。

- `$nodeId`将其替换为您的节点 ID，这是您在 Spacemesh 网络上的节点的唯一标识符。

- `$LabelsPerUnit`设置每个存储单元的标签数。默认值为 4294967296。

- `$MaxFileSize`设置最大文件大小。默认值为 2147483648。

- `$numUnits`设置要挖掘的存储单元数。默认值为 16。

- `$datadir`设置存储采矿数据的数据目录路径。

#### 第 2 步：执行脚本

保存带有已定义变量的脚本，并在 PowerShell 中执行。脚本将自动在指定的 GPU 之间分配挖矿工作量，优化挖矿效率。

#### Windows

```powershell
## Configurable Variables
$numGpus = 2
$commitmentAtxId = ""
$nodeId = ""
$LabelsPerUnit = 4294967296
$MaxFileSize = 2147483648
$numUnits = 16
$datadir = "C:\root\post\data"

## Script
foreach ($gpuIndex in 0..($numGpus - 1)) {
    $fromFile = $gpuIndex * ($numUnits * 32 / $numGpus)
    $toFile = ($gpuIndex + 1) * ($numUnits * 32 / $numGpus) - 1
    
    Start-Process -NoNewWindow -FilePath "postcli" -ArgumentList "-provider $gpuIndex", "-commitmentAtxId", $commitmentAtxId, "-id", $nodeId, "-labelsPerUnit", $LabelsPerUnit, "-maxFileSize", $MaxFileSize , "-numUnits", $numUnits, "-datadir", $datadir, "-fromFile", $fromFile, "-toFile", $toFile
}
```

#### Linux
```bash
#!/bin/bash

# Configurable Variables
numGpus=2
commitmentAtxId=""
nodeId=""
LabelsPerUnit=4294967296
MaxFileSize=2147483648
numUnits=16
datadir="\root\post\data"

# Script
for ((gpuIndex=0; gpuIndex<numGpus; gpuIndex++)); do
    fromFile=$((gpuIndex * (numUnits * 32 / numGpus)))
    toFile=$(( (gpuIndex + 1) * (numUnits * 32 / numGpus) - 1 ))
    
    postcli -provider $gpuIndex -commitmentAtxId "$commitmentAtxId" -id "$nodeId" -labelsPerUnit $LabelsPerUnit -maxFileSize $MaxFileSize -numUnits $numUnits -datadir "$datadir" -fromFile $fromFile -toFile $toFile &
done
```
______

### 步骤 3：监测采矿进度

脚本运行后，就可以监控挖矿进度了。postcli 应用程序将开始使用指定的 GPU，利用 PoST 算法挖掘 Spacemesh。每个 GPU 将被分配到特定范围的存储单元，以确保公平分配工作。

______

## 结论

使用多个 GPU 开采 Spacemesh 是一种高效的方式，既能为网络做出贡献，又能最大限度地发挥硬件潜能。通过使用提供的 PowerShell 脚本和 postcli 应用程序，您可以使用 PoST 算法无缝挖掘 Spacemesh，而无需进行基于 PoW 的加密货币所需的高能耗计算。

请务必记住及时更新您的 postcli 应用程序，并随时了解 Spacemesh 网络的任何变化或更新。祝您挖矿愉快

## 参考资料

1. [Spacemesh Official Website](https://spacemesh.io/)
2. [Spacemesh GitHub Repository](https://github.com/spacemeshos/)
3. [Spacemesh POST CLI Application](https://github.com/spacemeshos/post)
