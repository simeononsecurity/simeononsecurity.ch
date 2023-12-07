---
title: "マルチGPUによる効率的なSpacemeshマイニング - 報酬を最大化する"
date: 2023-08-18
toc: true
draft: false
description: "環境に優しいPoSTアルゴリズムで複数のGPUを使用してSpacemeshマイニングを最適化し、報酬を最大化する方法を学びましょう。"
genre: ["暗号通貨", "ブロックチェーン", "鉱業", "テクノロジー", "分散型", "GPUマイニング", "時空の証明", "環境に優しい", "暗号のヒント", "デジタル資産"]
tags: ["スペースメッシュ", "鉱業", "GPU", "時空の証明", "暗号通貨", "ブロックチェーン", "環境に優しい", "分散型", "PoSTアルゴリズム", "マイニングガイド", "暗号のヒント", "報酬", "最適化", "エネルギー効率", "GPUマイニング", "デジタル資産", "テクノロジー", "地方分権", "宇宙の証明", "時空間マイニング", "採掘効率の最大化", "環境に優しい暗号通貨", "スペースメッシュ・ネットワーク", "GPUマイニングのセットアップ", "複数のGPUによるマイニング", "分散型ブロックチェーン・マイニング", "暗号マイニングのヒント", "効率的なGPUマイニング", "時空間アルゴリズムの証明", "暗号通貨の報酬"]
cover: "/img/cover/spacemesh-mining-gpus.png"
coverAlt: "複数のGPUが協力してSpacemeshを採掘する様子を描いた漫画風のイラスト。"
coverCaption: "よりスマートに、よりグリーンに！"
---
はじめに

Spacemeshは、Bitcoinのような従来のプルーフ・オブ・ワーク（PoW）暗号通貨に代わる環境に優しい、「時空間証明（PoST）」と呼ばれるエネルギー効率の高いコンセンサスアルゴリズムをマイニングに採用した画期的な暗号通貨プラットフォームです。複数のGPUを持ち、Spacemeshのマイニングに興味がある場合、この包括的なガイドでは、強力なpostcliアプリケーションを使用してマイニングの可能性を最大化するプロセスを説明します。

## 前提条件

マイニングプロセスに入る前に、以下の前提条件が整っていることを確認してください：

1.**複数のGPU:** Spacemeshマイニングを効率的に処理できるGPUが少なくとも2つあることを確認してください。

2.**postcliアプリケーション:** Postcliアプリケーションを以下からダウンロードしてください。 [here](https://github.com/spacemeshos/post/)を正しくインストールし、システムの環境パスで利用可能であることを確認してください。

## 複数のGPUでSpacemeshをマイニングする

複数のGPUを使ってSpacemeshのマイニングを始めるには、以下の簡単な手順に従います：

______

### ステップ1：変数の設定

テキストエディタまたはPowerShellスクリプトエディタを開き、要件に応じて設定可能な変数を設定します。
提供されているスクリプトにはすでに調整可能な変数がいくつか含まれていますが、残りはspacemech GUIアプリケーションでスメッシングを開始したときに得られるjsonファイルから引き出すことができます：

- `$numGpus`マイニングに利用したいGPUの数を設定する。例えば `2`GPU2台分。

- `$commitmentAtxId`これをあなたのコミットメントATX IDに置き換えてください。これは、Spacemeshネットワークに参加することを約束するための一意の識別子です。

- `$nodeId`これをあなたのノードID（Spacemeshネットワーク上のあなたのノードの一意な識別子）に置き換えてください。

- `$LabelsPerUnit`ストレージユニットあたりのラベル数を設定します。デフォルト値は4294967296です。

- `$MaxFileSize`最大ファイルサイズを設定します。デフォルト値は2147483648です。

- `$numUnits`採掘するストレージの数を設定する。デフォルト値は16。

- `$datadir`マイニングデータを保存するデータディレクトリへのパスを設定します。

### ステップ2：スクリプトの実行

定義した変数とともにスクリプトを保存し、PowerShellで実行します。このスクリプトは、マイニングのワークロードを指定したGPUに自動的に分割し、マイニング効率を最適化します。

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

#### リナックス
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

### ステップ3：採掘の進捗状況の監視

スクリプトが実行されると、マイニングの進捗状況を監視できます。postcliアプリケーションは、PoSTアルゴリズムを使ってSpacemeshを採掘するために指定されたGPUの利用を開始します。各GPUには、作業の公平な分配を確実にするために、特定の範囲のストレージユニットが割り当てられます。

______

## 結論

複数のGPUを使ってSpacemeshをマイニングすることは、ハードウェアの可能性を最大限に引き出しながらネットワークに貢献する効率的な方法です。提供されているPowerShellスクリプトをpostcliアプリケーションと一緒に使用することで、PoWベースの暗号通貨で必要とされるエネルギー集約的な計算をすることなく、PoSTアルゴリズムを使ってシームレスにSpacemeshをマイニングすることができます。

postcliアプリケーションを常に最新の状態に保ち、Spacemeshネットワークの変更や更新について常に情報を得ることを忘れないでください。マイニングをお楽しみください！

## 参考文献

1. [Spacemesh Official Website](https://spacemesh.io/)
2. [Spacemesh GitHub Repository](https://github.com/spacemeshos/)
3. [Spacemesh POST CLI Application](https://github.com/spacemeshos/post)
