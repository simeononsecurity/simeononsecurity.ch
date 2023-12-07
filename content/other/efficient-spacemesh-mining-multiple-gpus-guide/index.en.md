---
title: "Efficient Spacemesh Mining with Multiple GPUs - Maximize Your Reward"
date: 2023-08-18
toc: true
draft: false
description: "Learn how to optimize your Spacemesh mining using multiple GPUs with the eco-friendly PoST algorithm and maximize your rewards."
genre: ["Cryptocurrency", "Blockchain", "Mining", "Technology", "Decentralized", "GPU Mining", "Proof of Space-Time", "Eco-friendly", "Crypto Tips", "Digital Assets"]
tags: ["Spacemesh", "Mining", "GPUs", "Proof of Space-Time", "Cryptocurrency", "Blockchain", "Eco-friendly", "Decentralized", "PoST Algorithm", "Mining Guide", "Crypto Tips", "Rewards", "Optimization", "Energy-efficient", "GPU Mining", "Digital Assets", "Technology", "Decentralization", "Proof of Space", "Space-Time Mining", "Maximizing Mining Efficiency", "Eco-friendly Cryptocurrency", "Spacemesh Network", "GPU Mining Setup", "Mining with Multiple GPUs", "Decentralized Blockchain Mining", "Crypto Mining Tips", "Efficient GPU Mining", "Proof of Space-Time Algorithm", "Cryptocurrency Rewards"]
cover: "/img/cover/spacemesh-mining-gpus.png"
coverAlt: "A cartoon-style illustration showing multiple GPUs working together to mine Spacemesh."
coverCaption: "Mine Smarter, Mine Greener!"
ref: ["/other/spacemesh-mining-eco-friendly-decentralized-rewards"]
---

## Introduction

Spacemesh is a groundbreaking cryptocurrency platform that employs an energy-efficient consensus algorithm known as "Proof of Space-Time" (PoST) for mining, presenting an eco-friendly alternative to traditional Proof of Work (PoW) cryptocurrencies like Bitcoin. If you have multiple GPUs and an interest in mining Spacemesh, this comprehensive guide will walk you through the process of maximizing your mining potential using the powerful postcli application.

{{< youtube id="_-OLJi3-038" >}}

## SpaceMesh Mining Phases & Their Requirements

### SpaceMesh's First Mining Phase: Plotting the Storage

*Initiating the Spacemesh mining journey begins with plotting the storage, a critical first step.*

- *Requirements:* A **high-performance GPU** is essential for optimal plotting, with the GTX 4090 being the fastest option. **Note** that it typically takes approximately **2 days to plot 1TB**. While multi-GPU plotting is not natively supported, innovative community scripts have enabled this capability.

### SpaceMesh's Second Mining Phase: Finding Proof within Existing Storage

*Every 14 days, smeshers have an opportunity to uncover proof within existing storage, a process requiring meticulous attention to specific hardware aspects.*

- *Process Overview:* The disk is read, and the CPU must locate proof within the storage to qualify for participation and subsequent rewards in the upcoming period. Critical factors include **CPU assignment** and **disk read speeds**.

- *Optimal Hardware:* Utilizing a recent **Ryzen core** allows for efficient handling of this process, achieving a minimum proof of **256GB** within one hour. The full window permits 12 x 256GB per CPU core. It's crucial to ensure that your system boasts adequate **write speeds**.

- *Performance Expectations:* In an 8-core Ryzen system, anticipate the ability to submit **12TB in 12 hours** for a streamlined mining experience.


## Prerequisites

Before diving into the mining process, ensure you have the following prerequisites in place:

1. **Multiple GPUs:** Make sure you have at least two GPUs capable of handling Spacemesh mining effectively. Ideally, all of the gpus you use will match. Using odd numbers of gpus is only supported when running the scripts below manually.

| Name                                                    | Description                                                             |
|---------------------------------------------------------|-------------------------------------------------------------------------|
| {{< centerbutton href="https://amzn.to/3NgmefN" >}}NVIDIA GeForce RTX 3060 Ti{{< /centerbutton >}} | Powerful mid-range GPU with excellent performance for its price.  6 days per TB     |
| {{< centerbutton href="https://amzn.to/3R6FM7k" >}}NVIDIA GeForce RTX 3080 Ti{{< /centerbutton >}} | High-end GPU with top-tier performance, ideal for gaming enthusiasts. 3,5 days per TB |
| {{< centerbutton href="https://amzn.to/3GvHYR1" >}}NVIDIA GeForce RTX 3090{{< /centerbutton >}}    | Flagship GPU offering unparalleled performance for gaming and tasks.   3 days TB |
| {{< centerbutton href="https://amzn.to/3ReYzxe" >}}NVIDIA GeForce RTX 4060 Ti{{< /centerbutton >}} | Latest GPU providing approximately 20% better performance than RTX 3060 Ti, offering great value. 5 days per TB |

2. **Storage:** 

- [USB 3.0 SATA Drives](https://amzn.to/41aZlzY) (100Mb/Sec)
- [SATA Drives Internal](https://amzn.to/3uNSAbj) (200Mb/Sec)
- [SSD Drives](https://amzn.to/47NSVcu) (500Mb/Sec)
- [NVME SSD Drives](https://amzn.to/3Nh5WTY) (3000-7000Mb/sec)

4. **postcli Application:** Download the postcli application from [here](https://github.com/spacemeshos/post/) and ensure it is correctly installed and available in your system's environment path.

## Mining Spacemesh with Multiple GPUs

To begin mining Spacemesh with multiple GPUs, follow these simple steps:

______

### Step 1: Configure Variables

{{< youtube id="dHFNG7SyuqM" >}}

Open a text editor or PowerShell script editor and set the configurable variables according to your requirements. 

The provided script already includes some variables you can adjust, but the rest can be pulled from the json or key.bin file that you get when you start smeshing on the spacemech GUI application:

- **Special Values**:
  These values can be pulled from the `postdata_metadata.json` file in the folder when you used go-spacemesh or the gui application.

  These values can be pulled from the metadata.json file in the folder when you used go-spacemesh or the gui application. However we need to change their encoding. 
  1. Pull the base64 encoded values from the json file and go to this [base64 decoder](https://cryptii.com/pipes/text-to-base64).
  2. In the encoder, one at a time you'll convert the node and commitment ids from the metadata.json using text > base64 decode > bytes, hexadecimal, none. The output of this conversion is the value you need.

  > **Note**: *We now convert them for you in the windows version of the script. If you have the old version, the linux version, or would like to learn more, please see the video above.*

  - `$commitmentAtxId`: Replace this with your commitment ATX ID, a unique identifier for your commitment to participate in the Spacemesh network. 
  *Must be converted from your `postdata_metadata.json` file with the instruction above if using linux, otherwise please copy directly from the json file.*

  - `$nodeId`: Replace this with your Node ID.
  *Must be converted from your `postdata_metadata.json` file with the instruction above if using linux or using the last 64 characters in your `key.bin` file, otherwise please copy directly from the json file.*

- **Standard Values**
  These values can be changed manually to whatever you want. Use common sense. Select the number of gpus and copy and paste the values if they are different from the `postdata_metadata.json` file.

  - `$numGpus`: Set the number of GPUs you want to utilize for mining. For instance, `2` for two GPUs.

  - `$LabelsPerUnit`: Set the number of labels per storage unit. The default value is `4294967296`.

  - `$MaxFileSize`: Set the maximum file size. The default value is `2147483648`.

  - `$numUnits`: Set the number of storage units to mine. The default value is `16`. Each `num` is equivalent to **64 GigaBytes** in plot space.

  - `$datadir`: Set the path to the data directory where your mining data will be stored.

  - `$postcliPath`: Set the exact path to your `postcli.exe` executable.

______

### Step 2: Execute the Script

Save the script with the defined variables and execute it in PowerShell. The script will automatically divide the mining workload among the specified GPUs, optimizing mining efficiency.

#### Windows

{{< youtube id="OdqIK7N0loE" >}}

```powershell
## Configurable Variables
$numGpus = 2
$commitmentAtxId = ""
$nodeId = ""
$LabelsPerUnit = 4294967296
$MaxFileSize = 2147483648
$numUnits = 16
$datadir = "C:\root\post\data"
$postcliPath = "S:\postcli.exe" #This should be the full path to the postcli.exe executable.

####################################
# Convert data coppied from postdata_metadata.json. DO NOT MODIFY
try{
    # Decode Base64 to Bytes
    $commitmentAtxIdBytes = [System.Convert]::FromBase64String($commitmentAtxId)
    # Convert Bytes to Hex
    $commitmentAtxIdHex = -join ($commitmentAtxIdBytes | ForEach-Object { $_.ToString("X2") })
    # Take the first 64 characters (32 bytes)
    $commitmentAtxId = $commitmentAtxIdHex.Substring(0, 64)
    # Display the conversion results
    Write-Output "CommitmentAtxId after conversion: $commitmentAtxId"
}
Catch{
    Write-Output "Unable to convert CommitmentAtxId, trying to pass in as is..."
    $commitmentAtxId = $commitmentAtxId
}

try{
    # Convert NodeId from hexadecimal to bytes
    $nodeIdBytes = [System.Convert]::FromBase64String($nodeId)
    # Convert Bytes to Hex
    $nodeIdHex = -join ($nodeIdBytes | ForEach-Object { $_.ToString("X2") })
    # Take the first 64 characters (32 bytes)
    $nodeId = $nodeIdHex.Substring(0, 64)
    # Display the conversion results
    Write-Output "NodeId after conversion: $nodeId"
    ####################################
}
Catch{
    Write-Output "Unable to convert nodeId, trying to pass in as is..."
    $nodeId = $nodeId
}

$countBy = ($numUnits * 32) / $numGpus
$rangeCount = $numGpus
Write-Output "If done manually, you can do the following ranges"

for ($i = 1; $i -le $rangeCount; $i++) `
{
    $rangeStart = ($i - 1) * $countBy
    $rangeEnd = $rangeStart + $countBy - 1

    Write-Output "Range $i fromFile = $rangeStart, toFile = $rangeEnd"
}

foreach ($gpuIndex in 0..($numGpus - 1)) {
    # Calculate the range of files for each GPU with the completed offset
    $fromFile = [int][math]::floor(($gpuIndex * ($numUnits * 32 / $numGpus)) + $completedOffset)
    $toFile = [int][math]::floor((($gpuIndex + 1) * ($numUnits * 32 / $numGpus)) - 1 + $completedOffset)

    Start-Process -FilePath "$postcliPath" -ArgumentList "-provider $gpuIndex", "-commitmentAtxId", $commitmentAtxId, "-id", $nodeId, "-labelsPerUnit", $LabelsPerUnit, "-maxFileSize", $MaxFileSize , "-numUnits", $numUnits, "-datadir", $datadir, "-fromFile", $fromFile, "-toFile", $toFile
}
```

##### Manual Windows Spacemesh Script Modification

If you all want to calculate the ranges manually to troubleshoot and get more visibility you can comment out or remove the foreach loop in the script above and it'll just print the ranges for you to run the above script manually.

Which should get you something like:

```txt
If done manually, you can do the following ranges                                                         
Range 1 fromFile = 0, toFile = 511                                                                        
Range 2 fromFile = 512, toFile = 1023                                                                     
```   

Then you can take the start-process command in foreach loop and cut it out of the for each block, 
manually set the `provider` number and `fromFile` and `toFile` values needed and paste them manually into different terminals.
This also lets you plot one plot on multiple systems if you take advantage of network storage.

```bash
Start-Process -FilePath "$postcliPath" -ArgumentList "-provider 0", "-commitmentAtxId", $commitmentAtxId, "-id", $nodeId, "-labelsPerUnit", $LabelsPerUnit, "-maxFileSize", $MaxFileSize , "-numUnits", $numUnits, "-datadir", $datadir, "-fromFile", 0, "-toFile", 511
Start-Process -FilePath "$postcliPath" -ArgumentList "-provider 1", "-commitmentAtxId", $commitmentAtxId, "-id", $nodeId, "-labelsPerUnit", $LabelsPerUnit, "-maxFileSize", $MaxFileSize , "-numUnits", $numUnits, "-datadir", $datadir, "-fromFile", 512, "-toFile", 1023
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

### Step 2.5: Optional Advanced - Execute the Script

#### Advanced Linux

##### Advanced Linux Script

```bash
#!/bin/bash

# Configurable variables
desiredSizeGiB=1024 # 1TIB
datadir="/root/post/data"
commitmentAtxId=""
nodeId=""

## Automatic Values
desiredSizeBytes=$(($desiredSizeGiB * 1024 * 1024 * 1024))
numGpus=$(nvidia-smi --query-gpu=name --format=csv,noheader | wc -l)
numGpus=$(($numGpus + 0)) # convert to int
LabelsPerUnit=4294967296
MaxFileSize=2147483648
numUnits=$(($desiredSizeGiB / 64))           # 64 GiB per unit
numUnits=$(($numUnits + 0))                  # convert to int

# Script to run postcli for each GPU
for ((gpuIndex=0; gpuIndex<numGpus; gpuIndex++)); do
    fromFile=$((gpuIndex * (numUnits * 32 / numGpus)))
    toFile=$(( (gpuIndex + 1) * (numUnits * 32 / numGpus) - 1 ))
    
    postcli -provider $gpuIndex -commitmentAtxId "$commitmentAtxId" -id "$nodeId" -labelsPerUnit $LabelsPerUnit -maxFileSize $MaxFileSize -numUnits $numUnits -datadir "$datadir" -fromFile $fromFile -toFile $toFile &
done
```
______

### Step 3: Monitor Mining Progress

Once the script is running, you can monitor the mining progress. The postcli application will start utilizing the specified GPUs to mine Spacemesh using the PoST algorithm. Each GPU will be assigned a specific range of storage units to ensure fair distribution of work.

______

## Spacemesh Calculator: Optimizing Your Mining Potential

{{< figure src="sos-spacemesh-calculator.webp" alt="A image of the website spacemeshcalculator.com" link="https://www.spacemeshcalculator.com/" >}}


The [**Spacemesh Calculator**](https://www.spacemeshcalculator.com/) serves as an indispensable tool for individuals venturing into Spacemesh (SMH) mining. Designed to streamline the mining experience, this calculator enables users to input their chosen disk space and receive detailed estimates of potential monthly and daily earnings in SMH. By factoring in crucial data such as current Netspace, Smesher ranking, and Coinbases, the calculator provides insights into the competitive landscape of Spacemesh mining. Notably, it considers hardware specifications, offering recommendations on GPU choices and plotting times. This dynamic tool plays a pivotal role in preparing prospective miners for the evolving landscape of decentralized cryptocurrencies, providing valuable insights into potential earnings within the Spacemesh network.

______

## Conclusion

Mining Spacemesh with multiple GPUs is an efficient way to contribute to the network while maximizing your hardware potential. By employing the provided PowerShell script alongside the postcli application, you can seamlessly mine Spacemesh using the PoST algorithm without the energy-intensive computations required by PoW-based cryptocurrencies.

Always remember to keep your postcli application up to date and stay informed about any changes or updates to the Spacemesh network. Happy mining!

## References

1. [Spacemesh Official Website](https://spacemesh.io/)
2. [Spacemesh GitHub Repository](https://github.com/spacemeshos/)
3. [Spacemesh POST CLI Application](https://github.com/spacemeshos/post)
4. [Spacemesh Start](https://spacemesh.io/start/)
5. [Spacemesh FAQ](https://spacemesh.io/faq/)
6. [SpaceMeshOS GPU Post](https://github.com/spacemeshos/gpu-post)