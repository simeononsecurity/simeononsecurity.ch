---
title: "Windows GVLKs：释放许可密钥的威力，提升性能"
date: 2023-09-09
toc: true
draft: false
description: "了解 Windows GVLK 如何彻底改变性能！探索最佳许可密钥，毫不费力地提高系统生产力。"
genre: ["技术", "软件", "生产率", "操作系统", "微软", "视窗", "许可", "关键管理", "IT 解决方案", "增强"]
tags: ["视窗 GVLK", "许可密钥", "生产率", "系统性能", "关键管理", "操作系统", "Windows 服务器", "Windows 10", "IT 解决方案", "软件", "长期服务渠道", "LTSC", "长期服务处", "LTSB", "增强性能", "微软", "IT 管理", "激活密钥", "KMS 客户", "GVLK 名单", "Windows 版本", "许可证激活", "客户产品密钥", "服务器 2019", "服务器 2016", "Windows 11 Pro", "Windows 10 企业版", "Windows LTSB 2016", "信息技术管理员"]
cover: "/img/cover/windows_gvlks_unlocked.png"
coverAlt: "彩色卡通插图是一把钥匙打开了一扇门，代表了 GVLK 在释放 Windows 全部潜能方面的威力。"
coverCaption: "利用 GVLK 释放 Windows 的潜能！"
---

## 如何为 Windows 和 Windows Server 安装产品密钥 (GVLK)

如果要将计算机从 KMS 主机、MAK 或 Windows 零售版转换为 KMS 客户端，则需要安装适用的产品密钥，也称为 GVLK（通用批量许可证密钥）。GVLK 用于使用密钥管理服务 (KMS) 激活卷。以下是如何在 Windows 或 Windows Server 系统上安装 GVLK 的分步指南。

## 自动 GLVK 安装脚本

该脚本必须从管理 Powershell 启动，目录中包含来自 [GitHub Repository](https://github.com/simeononsecurity/KMS-Auto-PS/archive/main.zip)
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
Get-ChildItem -Recurse *.ps1 | Unblock-File
.\sos-kmsglvkactivationauto.ps1
```

## 手动安装激活步骤

### 先决条件

在继续之前，请确保您的 Windows 版本和版本拥有合法有效的产品密钥。使用未经授权或盗版的产品密钥违反微软的服务条款，并可能导致法律后果。

### 安装步骤

1.**打开管理命令提示符：** 右键单击 "开始 "按钮，选择 "Windows 终端（管理）"或 "命令提示符（管理）"。如果使用的是 Windows 11 或 Windows 10，可以搜索 "命令提示符"，右键单击该命令提示符，然后选择 "以管理员身份运行"。

2.**找到合适的产品密钥 (GVLK)：** 从以下列表中查找适用于您的 Windows 或 Windows Server 版本和版本的 GVLK：

   - Windows Server 2022:*
     - Windows Server 2022 Datacenter：WX4NM-KYWYW-QJJR4-XV3QB-6VM33
     - Windows Server 2022 Datacenter Azure Edition：NTBV8-9K7Q8-V27C6-M2BTV-KHMXV
     - Windows Server 2022 标准版VDYBN-27WPP-V4HQT-9VMD4-VMK7H

   - Windows Server 2019:*
     - Windows Server 2019 Datacenter：WMDGN-G9PQG-XVVXX-R3X43-63DFG
     - Windows Server 2019 标准版：N69G4-B89J2-4G8F4-WWYCC-J464C
     - Windows Server 2019 Essentials：WVDHN-86M7X-466P6-VHXV7-YY726

   - Windows Server 2016：*
     - Windows Server 2016 Datacenter：CB7KF-BWN84-R7R2Y-793K2-8XDDG
     - Windows Server 2016 标准版WC2BQ-8NRM3-FDDYY-2BFGV-KHKQY
     - Windows Server 2016 Essentials：JCKRF-N37P4-C2D82-9YXRT-4M63B

   [Click Here to See the Others](#complete-list-of-generic-volume-license-keys-gvlk)

3.**安装产品密钥 (GVLK)：** 在管理命令提示符中，键入以下命令，替换为 `<product key>`使用适当的 GVLK：
```sh
slmgr /ipk <product key>
```

例如，要为 Windows Server 2022 Datacenter 版安装 GVLK，命令如下：

```sh
slmgr /ipk WX4NM-KYWYW-QJJR4-XV3QB-6VM33
```

4.**按 Enter：** 输入命令后，按 Enter。系统将尝试安装指定的产品密钥。

5.**确认信息：** 如果安装成功，你会看到一条产品密钥已安装的确认信息。

如果没有看到确认信息，或想强制 Windows 尝试使用密钥激活，请尝试执行以下命令：

```sh
slmgr /ato
slmgr /dlv
```

## 重要说明

- 请务必确保您使用的 Windows 版本和版本的产品密钥合法有效。
- slmgr "命令涉及许可和激活，请谨慎使用。
- 对于 Windows 11 和 Windows 10，不同版本的 GVLK 完整列表请参阅原始表格。

切记遵守微软的许可指南和服务条款，以保持合规合法。

*免责声明：本文仅供参考。产品密钥的使用应遵守微软的许可条款，任何滥用行为均由用户负责。


## 通用批量许可密钥 (GVLK) 完整列表

在下面的表格中，您可以找到 Windows 各版本的通用批量许可密钥 (GVLK)。*LTSC* 代表长期服务通道，*LTSB* 代表长期服务分支。有关 GVLK，请参阅下表：

### Windows 服务器（LTSC 版本）

#### Windows Server 2022

| KMS 客户端产品密钥
|--------------------------------|-------------------------------|
|WX4NM-KYWYW-QJJR4-XV3QB-6VM33 | Windows Server 2022 Datacenter
| Windows Server 2022 Datacenter<br/>Azure Edition | NTBV8-9K7Q8-V27C6-M2BTV-KHMXV | Windows Server 2022 Standard<br/>Azure Edition | NTBV8-9K7Q8-V27C6-M2BTV-KHMXV
| Windows Server 2022 标准版<br/> VDYBN-27WPP-V4HQT-9VMD4-VMK7H | Windows Server 2022 数据中心版<br/>Azure 版

#### Windows Server 2019

| 操作系统版本 | KMS 客户端产品密钥 | KMS 客户端产品密钥
|--------------------------------|-------------------------------|
| Windows Server 2019 Datacenter | WMDGN-G9PQG-XVVXX-R3X43-63DFG | Windows Server 2019 标准版
| Windows Server 2019 标准版 | N69G4-B89J2-4G8F4-WWYCC-J464C | Windows Server 2019 基本版
| Windows Server 2019 Essentials | WVDHN-86M7X-466P6-VHXV7-YY726 | Windows Server 2019 Standard | N69G4-B89J2-4G8F4-WWYCC-J464C

#### Windows Server 2016

| 操作系统版本 | KMS 客户端产品密钥 | KMS 客户端产品密钥
|--------------------------------|-------------------------------|
| Windows Server 2016 Datacenter | CB7KF-BWN84-R7R2Y-793K2-8XDDG | | Windows Server 2016 标准版
| Windows Server 2016 Standard | WC2BQ-8NRM3-FDDYY-2BFGV-KHKQY | Windows Server 2016 Essentials | Essentials | Essentials | Essentials | Essentials
| Windows Server 2016 Essentials | JCKRF-N37P4-C2D82-9YXRT-4M63B | Windows Server 2016 Standard | WC2BQ-8NRM3-FDDYY-2BFGV-KHKQY

#### Windows Server（半年度渠道版本）

#### Windows Server，版本 20H2、2004、1909、1903 和 1809

| KMS 客户端产品密钥
|---------------------------|-------------------------------|
| Windows Server Datacenter | 6NMRW-2C8FM-D24W7-TQWMY-CWH2D | Windows Server Standard | NNMRW-2C8FM-D24W7-TQWMY-CWH2D
| Windows Server Standard | N2KJX-J94YW-TQVFB-DG9YT-724CC | | N2KJX-J94YW-TQVFB-DG9YT-724CC

#### Windows 11 和 Windows 10（半年渠道版本）

| 操作系统版本 | KMS 客户端产品密钥 | KMS 客户端产品密钥
|-----------------------------------|-------------------------------|
|Windows 11 Pro<br/>Windows 10 Pro |W269N-WFGWX-YVC9B-4J6C9-T83GX |W269N-WFGWXYVC9B-4J6C9-T83GX
|Windows 11 Pro N<br/>Windows 10 Pro N | MH37W-N47XK-V7XM9-C7227-GCQG9 ||Windows 11 Pro for Workstat
| Windows 11 Pro for Workstations<br/>Windows 10 Pro for Workstations | NRG8B-VKK3Q-CXVCJ-9G2XF-6Q84J | Windows 11 Pro for Workstations<br/>Windows 10 Pro N
| Windows 11 Pro 工作站 N<br/>Windows 10 Pro 工作站 N | 9FNHH-K3HBT-3W4TD-6383H-6XYWF | | Windows 11 Pro 教育版<br/>Windows 10 Pro 教育版
|Windows 11 Pro 教育版<br/>Windows 10 Pro 教育版 |6TP4R-GNPTD-KYYHQ-7B7DP-J447Y |Windows 11 Pro 教育版N<br/>Windows 10 Pro for Workstation N
| Windows 11 Pro Education N<br/>Windows 10 Pro Education N | YVWGF-BXNMC-HTQYQ-CPQ99-66QFC | | Windows 11 Education<br/>Windows 10 Pro Education N
| Windows 11 教育版<br/>Windows 10 教育版 | NW6C2-QMPVW-D7KK-3GKT6-VCFB2 | Windows 11 教育N版<br/>Windows 10 教育N版
| Windows 11 Education N<br/>Windows 10 Education N | 2WH4N-8QGBV-H22JP-CT43Q-MDWWJ | | Windows 11 Enterprise<br/>Windows 10 企业版
| Windows 11 企业版<br/>Windows 10 企业版 | NPPR9-FWDCX-D2C8J-H872K-2YT43 | Windows 11 教育版
| Windows 11 Enterprise N<br/>Windows 10 Enterprise N | DPH2V-TTNVB-4X9Q3-TJR4H-KHJW4 | Windows 11 Enterprise G<br/>Windows 10 Enterprise G<br/>Windows 10 Enterprise G<br/>Windows 11 Enterprise G
|Windows 11 Enterprise G<br/>Windows 10 Enterprise G |YYVX9-NTFWV-6MDM3-9PT4T-4M68B |Windows 11 Enterprise N<br/>Windows 10 Enterprise N
|Windows 11 Enterprise G N<br/>Windows 10 Enterprise G N | 44RPN-FTY23-9VTTB-MP9BX-T84FV ||Windows 11 Enterprise G N<br/>Windows 10 Enterprise G N

### Windows 10（LTSC/LTSB 版本）

#### Windows 10 LTSC 2021 和 2019

| 操作系统版本 | KMS 客户端产品密钥 | KMS 客户端产品密钥
|-----------------------------------|-------------------------------|
|Windows 10 Enterprise LTSC 2021<br/>Windows 10 Enterprise LTSC 2019 |M7XTQ-FN8P6-TTKYV-9D4CC-J462D |
|Windows 10 Enterprise N LTSC 2021<br/>Windows 10 Enterprise N LTSC 2019 |92NFX-8DJQP-P6BBQ-THF9C-7CG2H ||Windows 10 Enterprise N LTSC 2021<br/>Windows 10 Enterprise N LTSC 2019

#### Windows 10 LTSB 2016

| 操作系统版本 | KMS 客户端产品密钥 | KMS 客户端产品密钥
|-----------------------------------|-------------------------------|
| Windows 10 Enterprise LTSB 2016 | DCPHK-NFMTC-H88MJ-PFHPY-QJ4BJ | | DCPHK-NFMTC-H88MJ-PFHPY-QJ4BJ | | Windows 10 Enterprise N LTSB 2016
|Windows 10 Enterprise N LTSB 2016 | QFFDN-GRT3P-VKWWX-X7T3R-8B639 |

#### Windows 10 LTSB 2015

| 操作系统版本 | KMS 客户端产品密钥 | KMS 客户端产品密钥
|-----------------------------------|-------------------------------|
| Windows 10 Enterprise 2015 LTSB | WNMTR-4C88C-JK8YV-HQ7T2-76DF9 | | Windows 10 Enterprise 2015 LTSB N
| Windows 10 Enterprise 2015 LTSB N | 2F77B-TNFGY-69QQF-B8YKP-D69TJ | | Windows 10 Enterprise 2015 LTSB N

### 早期版本的 Windows Server

#### Windows Server，1803 版

| KMS 客户端产品密钥
|---------------------------|-------------------------------|
| Windows Server Datacenter | 2HXDN-KRXHB-GPYC7-YCKFJ-7FVDG | | Windows Server Standard | PTXN8-JFHJM-4WC78-MCKFJ-7FVDG | | KMS Client Product Key
| Windows Server Standard | PTXN8-JFHJM-4WC78-MPCBR-9W4KR | KMS Client 产品密钥

#### Windows Server，版本 1709

| 操作系统版本 | KMS 客户端产品密钥 | KMS 客户端产品密钥
|---------------------------|-------------------------------|
| Windows Server Datacenter | 6Y6KB-N82V8-D8CQV-23MJW-BWTG6 | Windows Server Standard | DPCNP-XQFKJ-BJFF-BWTG6 | KMS Client Product Key
| Windows Server Standard | DPCNP-XQFKJ-BJF7R-FRC8D-GF6G4 | KMS Client 产品密钥

#### Windows Server 2012 R2

| 操作系统版本 | KMS 客户端产品密钥 | | KMS 客户端产品密钥
|----------------------------------------|-------------------------------|
| Windows Server 2012 R2 标准版 | D2N9P-3P6X9-2R39C-7RTCD-MDVJX | | Windows Server 2012 R2 数据中心版
| Windows Server 2012 R2 Datacenter | W3GGN-FT8W3-Y4M27-J84CP-Q3VJ9 |W3GGN-FT8W3-Y4M27-J84CP-Q3VJ9
| Windows Server 2012 R2 Essentials | KNC87-3J2TX-XB4WP-VCPJV-M4FWM | | Windows Server 2012 R2 Datacenter

#### Windows Server 2012

| 操作系统版本 | KMS 客户端产品密钥 | KNC87-3J2TX-XB4WP-VCPJV-M4FWM
|-----------------------------------------|-------------------------------|
| Windows Server 2012 | BN3D2-R7TKB-3YPBD-8DRP2-27GG4 | KMS客户端产品密钥
| Windows Server 2012 N | 8N2M2-HWPGY-7PGT9-HGDD8-GVGGY | | 8N2M2-HWPGY-7PGT9-HGDD8-GVGGY | | Windows Server 2012 单语言
| Windows Server 2012 单语言版本 | 2WN2H-YGCQR-KFX6K-CD6TF-84YXQ | Windows Server 2012 国家特定版本
| Windows Server 2012 国家/地区专用语言 | 4K36P-JN4VD-GDC6V-KDT89-DYFKP | | Windows Server 2012 标准版
| Windows Server 2012 标准版 | XC9B7-NBPP2-83J2H-RHMBY-92BT4 | Windows Server 2012 多点版
| Windows Server 2012 MultiPoint Standard | HM7DN-YVMH3-46JC3-XYTG7-CYQJJ | Windows Server 2012 MultiPoint Standard | HM7DN-YVMH3-46JC3-XYTG7-CYQJJ
Windows Server 2012 MultiPoint Premium | XNH6W-2V9GX-RGJ4K-Y8X6F-QGJ2G | Windows Server 2012 Datacenter | XNH6W-2V9GX-RGJ4K-Y8X6F-QGJ2G
| Windows Server 2012 Datacenter | 48HP8-DN98B-MYWDG-T2DCC-8W83P | Windows Server 2012 多点高级版

#### Windows Server 2008 R2

| 操作系统版本 | KMS 客户端产品密钥 | KMS 客户端产品密钥
|--------------------------------------------------|-------------------------------|
| Windows Server 2008 R2 Web | 6TPJF-RBVHG-WBW2R-86QPH-6RTM4 | | Windows Server 2008 R2 HPC版
| Windows Server 2008 R2 HPC 版本 | TT8MH-CG224-D3D7Q-498W2-9QCTX | | Windows Server 2008 R2 标准版
| Windows Server 2008 R2 Standard | YC6KT-GKW9T-YTKYR-T4X34-R7VHC | Windows Server 2008 R2 Enterprise | TT8MH-CG224-D3D7Q-498W2-9QCTX | Windows Server 2008 R2 HPC 版
| Windows Server 2008 R2 企业版 | 489J6-VHDMP-X63PK-3K798-CPX3Y | Windows Server 2008 R2 数据版
| Windows Server 2008 R2 Datacenter | 74YFP-3QFB3-KQT8W-PMXWJ-7M648 | Windows Server 2008 R2 for iphone | 74YFP-3QFB3-KQT8W-PMXWJ-7M648
| Windows Server 2008 R2 for Itanium-based Systems | GT63C-RJFQ3-4GMB6-BRFB9-CB83V | Windows Server 2008 R2 数据中心

#### Windows Server 2008

| 操作系统版本 | KMS 客户端产品密钥 | KMS 客户端产品密钥
|------------------------------------------------|-------------------------------|
| Windows Web Server 2008 | WYR28-R7TFJ-3X2YQ-YCY4H-M249D | Windows Server 2008 标准版
| Windows Server 2008 Standard | TM24T-X9RMF-VWXK6-X8JC9-BFGM2 | Windows Server 2008 Standard（不含 Hyper ®）。
| 不带 Hyper-V 的 Windows Server 2008 标准版 | W7VD6-7JFBR-RX26B-YKQ3Y-6FFFJ | Windows Server 2008 企业版
| Windows Server 2008 Enterprise | YQGMW-MPWTJ-34KDK-48M3W-X4Q6V | Windows Server 2008 Enterprise（不含 Hyper-V
| Windows Server 2008 Enterprise（不含 Hyper-V ） | 39BXF-X8Q23-P2WWT-38T2F-G3FPG | | Windows Server 2008 HPC（不含 Hyper-V
| Windows Server 2008 HPC | RCTX3-KWVHP-BR6TB-RB6DM-6X7HP | Windows Server 2008 数据中心
| Windows Server 2008 Datacenter | 7M67G-PC374-GR742-YH8V4-TCBY3 | | Windows Server 2008 HPC
| 不带 Hyper-V 的 Windows Server 2008 Datacenter | 22XQ2-VRXRG-P8D42-K34TD-G3QQC | | Windows Server 2008 for Itanium
| Windows Server 2008 for Itanium-Based Systems | 4DWFP-JF3DJ-B7DTH-78FJB-PDRHK | Windows Server 2008 Datacenter（不含 Hyper-V

### 早期版本的 Windows

#### Windows 8.1

| 操作系统版本 | KMS 客户端产品密钥 | KMS 客户端产品密钥
|--------------------------|-------------------------------|
| Windows 8.1 Pro | GCRJD-8NW9H-F2CDX-CCM8D-9D6T9 | Windows 8.1 Pro N | HMCNV-VVBFX-7HMBH | KMS Client Product Key
| Windows 8.1 Pro N | HMCNV-VVBFX-7HMBH-CTY9B-B4FXY | | Windows 8.1 企业版
| Windows 8.1 Enterprise | MHF9N-XY6XB-WVXMC-BTDCT-MKKG7 | | Windows 8.1 Enterprise N
| Windows 8.1 Enterprise N | TT4HM-HN7YT-62K67-RGRQJ-JFFXW | Windows 8.1 企业版

#### Windows 8

| 操作系统版本 | KMS 客户端产品密钥 | KMS 客户端产品密钥
|--------------------------|-------------------------------|
| Windows 8 Pro | NG4HW-VH26C-733KW-K6F98-J8CK4 | | Windows 8 Pro N
| Windows 8 Pro N | XCVCF-2NXM9-723PB-MHCB7-2RYQQ | | Windows 8 企业版
| Windows 8 Enterprise | 32JNW-9KQ84-P47T8-D8GGY-CWCK7 | | Windows 8 N
| Windows 8 Enterprise N | JMNMF-RHW7P-DMY6X-RF3DR-X2BQT | Windows 8 Enterprise N | JMNMF-RHW7P-DMY6X-RF3DR-X2BQT | Windows 8 Enterprise N

#### Windows 7

| 操作系统版本 | KMS 客户端产品密钥 | KMS 客户端产品密钥
|--------------------------|-------------------------------|
| Windows 7 专业版 | FJ82H-XT6CR-J8D7P-XQJJ2-GPDD4 | | Windows 7 专业版 N
|Windows 7 Professional N | MRPKT-YTG23-K7D7T-X2JMM-QY7MG |
| Windows 7 专业版 E | W82YF-2Q76Y-63HXB-FGJG9-GF7QX | Windows 7 企业版
| Windows 7 Enterprise | 33PXH-7Y6KF-2VJC9-XBBR8-HVTHH | | Windows 7 Enterprise N
| Windows 7 Enterprise N | YDRBP-3D83W-TY26F-D46B2-XCKRJ | Windows 7 Enterprise E | YDRBP-3D83W-TY26F-D46B2-XCKRJ | Windows 7 Enterprise E
| C29WB-22CC8-VJ326-GHFJW-H9DH4 | Windows 7 Enterprise E

#### Windows Vista

| 操作系统版本 | KMS 客户端产品密钥
|--------------------------|-------------------------------|
|Windows Vista Business | YFKBB-PQJJV-G996G-VWGXY-2V3X8 ||Windows Vista Business N
|Windows Vista Business N | HMBQG-8H2RH-C77VX-27R82-VMQBT ||Windows Vista Enterprise | |Windows Vista N
|Windows Vista Enterprise | VKK3X-68KWM-X2YGT-QR4M6-4BWMV ||Windows Vista Enterprise N
|Windows Vista Enterprise N |VTC42-BM838-43QHV-84HX6-XJXKV |Windows Vista Enterprise N |VTC42-BM838-43QHV-84HX6-XJXKV

## 参考文献
- [Key Management Services (KMS) client activation and product keys](https://learn.microsoft.com/en-us/windows-server/get-started/kms-client-activation-keys)