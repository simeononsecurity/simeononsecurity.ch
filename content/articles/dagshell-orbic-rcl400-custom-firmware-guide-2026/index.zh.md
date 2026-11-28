---
title: "Orbic RCL400 的 DagShell 定制固件：2026 指南"
date: 2026-05-28
lastmod: 2026-11-27
toc: true
draft: false
description: "Orbic RCL400 DagShell 固件技术指南，介绍安装、隐私工具、巡行扫描和研究限制。"
genre: ["定制固件", "移动安全", "隐私工具", "网络安全", "巡行扫描", "渗透测试", "IoT 安全", "安全研究", "硬件安全", "隐私技术"]
tags: ["DagShell", "Orbic RCL400", "定制固件", "热点安全", "隐私工具", "TTL 修正", "MAC 欺骗", "IMSI 捕获器检测", "巡行扫描", "GPS 跟踪", "Evil Twin 攻击", "强制门户", "DNS 嗅探器", "ARP 扫描器", "端口扫描器", "Raspberry Pi Companion", "WiFi 安全", "移动热点", "网络监控", "渗透测试", "安全研究", "Bluetooth 扫描", "取消认证攻击", "WiFi 扫描", "OUI 查询", "Wigle 上传", "蜂窝塔监控", "AT 命令", "防火墙管理器", "广告拦截", "TLS 加密", "RayHunter 集成", "STS Collective", "移动安全实验室", "网络分析", "隐私固件", "开源安全", "ARM 交叉编译", "嵌入式 Linux", "安全工具包", "黑客工具", "红队", "网络侦察"]
canonical: "https://simeononsecurity.com/articles/dagshell-orbic-rcl400-custom-firmware-guide-2026/"
cover: "/img/cover/dagshell-orbic-rcl400-custom-firmware-guide-2026.webp"
coverAlt: "深蓝色背景上，Orbic RCL400 移动热点显示绿色界面，周围有图表和地图等抽象安全工具图案。"
coverCaption: ""
---

**将 Orbic RCL400 变成移动安全研究实验室**

## 引言：黑客热点

**DagShell** 是适用于 **Orbic RCL400 移动热点**的开源定制固件，可将普通蜂窝设备变成**便携式安全研究与隐私工具包**。安全研究员“dag”开发了这款终端风格固件，提供**黑客工具、隐私功能和网络监控能力**，界面采用简洁的黑底绿字风格。

本指南介绍：
- **DagShell 的定义和完整功能**
- **使用网页刷写器或手动安装的步骤**
- **各项工具和能力**
- **Raspberry Pi Companion** 扩展设置
- **DagShell 与 RayHunter** 配合使用的原因
- **安全研究员和隐私倡导者的实际用例**
- **法律与伦理注意事项**

**概要**：Orbic RCL400 上的 DagShell 与 RayHunter 组合成**完整的移动安全实验室**，用于 IMSI 捕获器检测、巡行扫描、网络分析和隐私保护。

**提供预刷写设备**：本文由 **STS Collective** 赞助。该商店提供已预装 **RayHunter 和 DagShell**、开箱即可使用的 Orbic RCL400 热点：[stscollective.com/products/orbic-rcl400-rayhunter-dagshell-hotspot](https://stscollective.com/products/orbic-rcl400-rayhunter-dagshell-hotspot)

> 💰 **读者专属折扣**：购买 STS Collective 产品（包括预刷写 Orbic RCL400）最高可省 20%。结账时使用代码 **SIMEONONSECURITY**，或[直接使用折扣购物](https://stscollective.com/discount/SIMEONONSECURITY)。

______

## DagShell 是什么？

### 概览

**DagShell** 是开源定制固件，用**全面的安全工具包**替换 Orbic RCL400 原厂网页界面，功能包括：

- **带 ASCII 艺术和黑客风格的终端界面**
- 使用自签名证书的 **TLS 1.2+ 加密**网页界面
- **隐私保护工具**，包括 TTL 屏蔽、MAC 欺骗和基于 DNS 的广告拦截
- **网络监控**，包括活动连接、路由表和 DNS 查询
- **IMSI 捕获器检测**、端口扫描和 ARP 发现等工具
- **Evil Twin AP**、强制门户钓鱼和取消认证攻击等能力
- **GPS 跟踪和巡行扫描**，并支持 Wigle 兼容 CSV 导出
- **用于 GPS**、Bluetooth 扫描和 WiFi 侦察的 Raspberry Pi Companion
- **通过浏览器文件管理器访问文件系统**
- **通过 AT 命令使用** SMS 功能
- **持久运行**，开机自动启动

### 技术规格

**平台**：Orbic RCL400 移动热点
**架构**：ARM Linux（内核 3.18）
**语言**：C/C++（静态 ARM 二进制文件）
**加密**：TLS 1.2+ 与自签名证书（双层 PKI）
**Web 服务器**：自定义嵌入式 HTTPS 服务器（端口 8443）
**界面**：基于浏览器的终端 UI
**许可**：MIT（开源）
**GitHub**: [github.com/dagnazty/DagShell](https://github.com/dagnazty/DagShell)

### 视觉设计

DagShell 采用**复古黑客风格**：
- **每个页面都有 ASCII 艺术徽标**
- **Matrix 风格的黑底绿字配色**
- **等宽字体**（Fira Code）
- **扫描线效果和发光文字**
- **终端风格布局**

{{< figure src="dagshell-orbic-rcl400-hacker-terminal-interface-feature-overview.webp" alt="Orbic RCL400 上运行的 DagShell 定制固件，显示黑底绿字终端界面、ASCII 图案和安全工具菜单" >}}

______

## 完整功能介绍

### 🏠 控制面板

**系统概览**：
- **运行时间**：显示设备已运行多久
- **AT 命令界面**：供高级用户直接控制调制解调器
- **快速状态**：显示 IP 地址和连接状态

**AT 命令**可进行底层调制解调器控制：
```
AT 命令示例：
AT+CSQ       - 信号质量
AT+COPS?     - 当前网络运营商
AT+CREG?     - 网络注册状态
AT+CIMI      - 获取 IMSI（用户身份标识）
AT+CGSN      - 获取 IMEI（设备标识符）
```

### 🌐 网络工具

**当前网络信息**：
- **IP 地址和接口详情**
- **子网掩码**、网关和广播地址
- **网络统计**（发送/接收的数据包）

**路由表查看器**：
- 查看所有网络路由
- 默认网关信息
- 接口映射

**活动连接监控器**：
- **实时列出所有 TCP**/UDP 连接
- 本地和远程 IP 地址
- 端口号和连接状态
- **便于监控设备正在与哪些主机通信**

### 🔒 隐私保护工具集

#### TTL 修正

**用途**：隐藏热点流量，避免运营商检测

**工作原理**：
- 将 IP 数据包的 **Time To Live (TTL)** 值改为 **65**
- 运营商可根据 TTL 递减识别网络共享（手机=64，共享设备=63）
- **TTL 设为 65** 后，所有流量看起来都来自本地

**用途**：绕过运营商对网络共享的限制或限速

**命令**：
```bash
# 启用 TTL 修复
iptables -t mangle -A POSTROUTING -j TTL --ttl-set 65

# 禁用 TTL 修复
iptables -t mangle -D POSTROUTING -j TTL --ttl-set 65
```

#### MAC 地址欺骗

**用途**：随机更改设备 MAC 地址以保护隐私

**工作原理**：
- **更改 wlan0**（WiFi 接口）的 MAC 地址
- **生成随机 MAC**，也允许自定义输入
- **降低设备在不同会话间被跟踪的可能**

**用途**：阻止你连接的网络通过 MAC 地址跟踪设备

**过程**：
1. 关闭接口
2. 应用新的 MAC 地址
3. 重新启用接口
4. 重新建立连接

#### 基于 DNS 的广告拦截

**用途**：在 DNS 层拦截广告和跟踪

**工作原理**：
- **将拦截列表写入** `/etc/hosts` 文件
- 列表中的域名解析到 **127.0.0.1**（本地主机）
- **为所有已连接设备拦截广告**

**用途**：无需逐台配置，即可在整个网络拦截广告

**拦截列表来源**：常见广告和跟踪域名，可自定义

### 📱 SMS 管理

**发送 SMS**：
- **使用 AT 命令让调制解调器发送短信**
- **适用于远程通知或测试**

**查看消息**：
- 链接到 Orbic 原生收件箱
- 阅读收到的短信

**使用的 AT 命令**：
```
AT+CMGS="PHONE_NUMBER"
此处填写短信内容^Z
```

### 🔧 安全测试工具

#### IMSI 捕获器检测器

**用途**：监控基站信息，发现可能表明存在 **IMSI catcher/Stingray** 设备的异常

**工作原理**：
- 从调制解调器查询**基站数据**：
  - **Cell ID**（基站标识）
  - **LAC**（位置区代码）
  - **MCC/MNC**（移动国家/网络代码）
  - **信号强度**（RSSI）
  - **网络代际**（2G/3G/4G）
- **记录变化**，以发现可疑的基站切换
- **建立基线**，记录所在区域的常见基站

**检测指标**：
- **静止时基站突然切换**
- **降级到 2G** *(IMSI 捕获器常强制使用 2G，以去除加密)*
- **出现未知 Cell ID**
- **假基站信号较弱**
- **频繁重新连接**

**与 RayHunter 配合**：****DagShell 提供基站监控****，RayHunter 通过更复杂的分析专门检测 IMSI 捕获器（见下文）。

#### 端口扫描器

**用途**：扫描目标 IP 地址上的开放端口

**工作原理**：
- **TCP SYN 扫描向目标端口发送** SYN 数据包
- **根据超时判断端口是开放**、关闭还是被过滤
- **可扫描单个端口或端口范围**

**用途**：
- **网络侦察**
- **发现 IoT 设备**
- **审计本地网络安全**
- **识别服务**

**命令**：
```bash
# 扫描目标的 1–1000 端口
nc -zv -w 2 TARGET_IP 1-1000 2>&1
```

#### 防火墙管理器

**用途**：使用 iptables 屏蔽或解除屏蔽 IP 地址

**工作原理**：
- **使用 iptables 规则丢弃来自指定** IP 或发往指定 IP 的数据包
- **保存后的规则在重启后仍然生效**
- **提供允许列表和阻止列表**

**用途**：
- **屏蔽恶意 IP**
- **阻止未授权访问**
- **整形或过滤流量**
- **家长控制**

**命令**：
```bash
# 屏蔽 IP
iptables -I INPUT -s IP_ADDRESS -j DROP
iptables -I OUTPUT -d IP_ADDRESS -j DROP

# 解除 IP 屏蔽
iptables -D INPUT -s IP_ADDRESS -j DROP
iptables -D OUTPUT -d IP_ADDRESS -j DROP
```

### ⚔️ 攻击工具

**重要法律免责声明**：****这些工具仅供******经授权的安全测试**使用。对不属于你或未经明确书面许可的网络使用，在多数司法管辖区都属**违法**。仅在自己的网络或受控实验室环境中使用。

#### DNS 嗅探器

**用途**：记录已连接客户端的 DNS 查询

**工作原理**：
- **在 53 端口**（DNS）使用 iptables 记录日志
- **无需混杂模式**
- 记录热点客户端的所有 DNS 请求
- **显示客户端访问的网站和服务**

**用途**（经授权）：
- **网络流量分析**
- **监护自己的家庭网络**
- **在自己的设备上进行安全研究**
- **分析恶意软件行为**

*此功能会记录已连接客户端访问的域名等元数据。仅在自己拥有或管理的网络上部署。*

#### ARP 扫描器

**用途**：发现本地网络中的设备

**工作原理**：
- **向子网中的所有 IP 发送** ARP 请求
- **设备以自己的 MAC 地址响应**
- **OUI 查询可识别制造商**，例如 Apple 或 Samsung
- **绘制活动设备的网络图**

**用途**：
- **建立网络资产清单**
- **检测未知设备**
- **分析 BYOD 网络**
- **发现 IoT 设备**

**输出示例**：
```
IP: 192.168.1.50
MAC: A4:83:E7:XX:XX:XX
Vendor: Apple, Inc.

IP: 192.168.1.75
MAC: 2C:54:91:XX:XX:XX
Vendor: Samsung Electronics
```

#### 路由跟踪

**用途**：显示到目标位置的网络路径

**工作原理**：
- **发送 TTL 逐渐增加的数据包**
- 每一跳都会递减 TTL，并返回 **ICMP Time Exceeded**
- **显示到目标的路由器和路径**
- **测量每一跳的往返时间**（RTT）

**用途**：
- **排查网络问题**
- **分析路由**
- **诊断延迟**
- **调查 ISP 对等互联**

#### Evil Twin AP

**用途**：创建仿冒现有 SSID 的虚假 WiFi 接入点

**工作原理**：
- **使用 wlan1**（如果 Pi Companion 提供第二个 WiFi 接口）
- **克隆目标网络的 SSID 和加密类型**
- **捕获尝试连接的客户端**
- **提供强制门户以收集凭据**

**攻击场景**（实验室环境）：
1. 扫描合法 WiFi 网络
2. **创建使用相同 SSID 的虚假** AP
3. **使用取消认证攻击**，将客户端踢下真实 AP
4. **客户端自动重新连接到虚假 AP**
5. 强制门户收集凭据

***检测方法**：如果两个 AP 同时可见，客户端会看到重复的 SSID。*

#### 强制门户

**用途**：提供收集凭据的钓鱼页面模板

**包含的模板**：
- **通用 ISP 或酒店风格的** WiFi 登录页
- **仿冒 Facebook**、Twitter、Instagram 的社交媒体登录页
- **企业登录门户**
- **机场和咖啡店 WiFi 门户**

**工作原理**：
1. **Evil Twin AP** 将所有流量重定向到门户
2. **客户端看到登录页**
3. 客户端输入凭据
4. **凭据记录到文件中**
5. 客户端随后获得互联网访问，或看到错误提示

**教育用途**：**展示社会工程风险**，并说明用户应核实 URL 的原因

### 📍 GPS 跟踪器与巡行扫描

#### GPS 功能

**GPS 来源**：**仅使用 Raspberry Pi** Companion
- *Orbic RCL400 **没有内置 GPS**，不使用 Pi Companion 就没有位置数据。*
- **Pi 连接 U**-Blox 7 芯片组的 USB GPS 接收器
- **Pi 通过共享数据文件将坐标发送到 Orbic**
- **自动执行 ECEF 到经纬度的转换**

**控制面板显示**：
- **十进制度数的纬度**/经度
- **海拔高度**
- **GPS 定位状态和精度**
- **每 5 秒自动刷新**
- **不使用浏览器 API**，因此不会弹出浏览器地理位置请求

**共享 GPS 状态**：
- **所有 DagShell 进程都能访问** GPS 数据
- 巡行扫描会自动使用 GPS
- 各功能之间不会冲突

#### 巡行扫描模式

**用途**：扫描 WiFi 网络并附加 GPS 坐标，以便绘图

**工作原理**：
1. **等待有效 GPS 定位**，避免记录 0,0 坐标
2. **持续循环**，每 5 秒扫描 WiFi 网络
3. 记录网络数据：
   - **SSID**（网络名称）
   - **BSSID**（MAC 地址）
   - **加密类型**（WPA2、WPA3、开放）
   - **信号强度**（dBm 的 RSSI）
   - **频道号**
   - **GPS 坐标**（经纬度）
   - **时间戳**
4. **导出为 Wigle 兼容的** CSV 格式

**Wigle 集成**：
- **WiGLE**（wigle.net）是全球 WiFi 地图项目
- **DagShell CSV 可直接上传到** WiGLE
- **从“文件”页通过浏览器上传**，无需外部工具
- **可为 WiFi 位置公共数据库做贡献**

**用途**：
- **绘制 WiFi 覆盖范围**
- **为 ISP 调查网络**
- **分析信号强度**
- **研究开放网络和弱加密等安全问题**
- **基于位置的数据分析**

**CSV 格式示例**：
```csv
MAC,SSID,AuthMode,FirstSeen,Channel,RSSI,Latitude,Longitude,AltitudeMeters
A1:B2:C3:D4:E5:F6,HomeNetwork,WPA2,2026-05-28 10:30:15,6,-45,40.7128,-74.0060,10
```

{{< figure src="dagshell-wardriving-gps-wifi-network-mapping-wigle-csv-export.webp" alt="DagShell 巡行扫描模式将 GPS 坐标以及扫描到的 WiFi 网络 SSID、BSSID、加密类型和信号强度记录到 Wigle 兼容 CSV 中" >}}

### 🥧 Raspberry Pi Companion

**Raspberry Pi Companion** 通过**外部硬件**扩展 DagShell 功能：

#### 硬件要求

**最低要求**：
- **Raspberry Pi 3B**+ 或更新型号 *(Pi Zero 无法为外围设备提供足够 USB 电力)*
- **USB GPS 接收器**（推荐 U-Blox 7 芯片组）
- **电源** *(Pi 需要单独供电，Orbic USB 端口供电不足)*

**可选设备**：
- **WiFi 适配器**，以便保持连接的同时使用另一个接口扫描
- **Bluetooth 接收器**（如果 Pi 内置蓝牙较弱）

#### GPS 模块（U-Blox 7）

**连接**：USB GPS 接收器连接到 Pi
**协议**：通过串行接口传输 NMEA 语句
**转换**：Pi 自动将 ECEF 转换为经纬度
**数据共享**：**将 GPS 坐标写入** Orbic 上的共享文件

**语句解析**：
```
$GPGGA,123519,4807.038,N,01131.000,E,1,08,0.9,545.4,M,46.9,M,,*47
       |       |          |           |  |  |   |
       时间  纬度  经度  定位状态  卫星数  海拔
```

#### Bluetooth 扫描（BLE）

**用途**：发现附近的 Bluetooth 设备

**工作原理**：
- **扫描 BLE 广播**
- **捕获 MAC 地址**
- **通过 OUI 查询识别制造商**
- **以 CSV 格式记录**

**远程控制**：
- **从 DagShell 网页** UI 启动或停止扫描
- 无需 SSH 登录 Pi
- 实时更新状态

**用途**：
- **跟踪和统计设备**
- **分析人流量**
- **发现 Bluetooth 设备**
- **IoT 安全研究**

**CSV 输出**：
```csv
Timestamp,MAC,RSSI,Name,Manufacturer
2026-05-28 10:30:15,AA:BB:CC:DD:EE:FF,-65,Fitbit Charge,Fitbit Inc.
```

#### WiFi 扫描

**用途**：Pi 扫描 WiFi 网络并将数据发送到 Orbic

**优势**：**使用专用接口扫描时**，Orbic 仍可维持热点连接

**工作原理**：
- **Pi 使用第二个 WiFi** 适配器，或在无需联网时使用内置 WiFi
- **扫描所有频道**（2.4GHz 的 1-14 频道，若支持则扫描 5GHz 的 36-165 频道）
- 通过共享存储将结果发送到 Orbic
- **DagShell 将结果记录到 wardriver** CSV

**协调方式**：
- **Pi 和 Orbic** 根据 GPS 时间戳同步
- 避免重复记录
- **将两个扫描来源合并到同一日志**

#### 取消认证攻击

**用途**：在实验室测试中断开 WiFi 客户端

**工作原理**：
- **发送 802**.11 去认证帧
- **伪造 AP 的** MAC 地址
- 客户端收到 AP 发来的“断开连接”消息
- **客户端断开连接并尝试重新连接**

**控制方式**：
- **单次取消认证**：发送一组帧
- **持续取消认证**：阻止重新连接（DoS）
- **远程控制**：从 DagShell 扫描页触发

**用途**（须经授权）：
- **从自己的网络中移除恶意设备**
- **获得许可后进行渗透测试**
- **在实验室进行 Evil Twin** 攻击，将客户端引导至虚假 AP

**⚠️ 法律警告**：对不属于自己的网络发起取消认证攻击属**违法行为**，可能违反 FCC 规定并面临 CFAA 指控。

#### 自动启动服务

**systemd 服务**：Pi Companion 在启动时自动运行

**服务文件**（`/etc/systemd/system/pi-companion.service`）：
```ini
[Unit]
Description=DagShell Pi Companion
After=network.target

[Service]
ExecStart=/usr/bin/python3 /opt/dagshell/pi_companion.py
Restart=always
User=root

[Install]
WantedBy=multi-user.target
```

**命令**：
```bash
# 启用自动启动
sudo systemctl enable pi-companion

# 启动服务
sudo systemctl start pi-companion

# 检查状态
sudo systemctl status pi-companion
```

#### OUI 数据库

**用途**：查询 MAC 地址对应的厂商/制造商

**数据库**：[OUI Master Database](https://standards.ieee.org/products-programs/regauth/) 前缀查询 API

**工作原理**：
- **提取 MAC 地址的前** 3 个字节（OUI 前缀）
- 查询 API：`api.example.com/oui/A4:83:E7`
- **返回制造商名称**

**示例**：
```
MAC: A4:83:E7:12:34:56
OUI: A4:83:E7
Vendor: Apple, Inc.
```

**集成**：ARP 扫描器、BLE 扫描器和 WiFi 巡行扫描都会使用它

### 📁 文件浏览器

**用途**：浏览和管理设备上的文件

**位置**：`/data/` 目录（可写分区）

**功能**：
- **浏览文件和子目录**
- **将文件下载到电脑**
- **确认后删除文件**
- **查看文件大小和时间戳**

**常见文件**：
- `wardrive_log.csv`：WiFi 扫描数据
- `bluetooth_scan.csv`：BLE 设备数据
- `gps_track.gpx`：GPS 轨迹
- `dns_queries.log`：捕获的 DNS 请求
- `arp_scan.txt`：网络设备列表

**上传到 Wigle**：
- **从“文件”页直接通过浏览器上传**
- 使用 WiGLE 账户进行身份验证
- 无需先下载即可上传 CSV

______

{{< stscollective-ad "rayhunter" >}}

## 安装指南

### 前置条件

**硬件**：
- **Orbic RCL400 移动热点**
- **Windows**、macOS 或 Linux 电脑
- **直接刷写固件时需要 USB 线缆**

**软件**：
- **安装了** `requests` 和 `cryptography` 模块的 Python 3
- **Chrome**、Firefox、Edge 或 Safari 浏览器

**可选**：
- **Raspberry Pi 3B**+ 或更新型号，用于 GPS 和扩展功能
- **U-Blox 7** 芯片组的 USB GPS 接收器

### 方法一：网页刷写器（推荐）

**最简单的方法**，无需命令行

**步骤 1**：打开 DagShell Webflasher
- 网址：[dagnazty.github.io/DagShell/orbic.html](https://dagnazty.github.io/DagShell/orbic.html)

**步骤 2**：生成 PKI 证书
- 点击 **"Generate Certificates"** 按钮
- **浏览器会生成双层 PKI**（根 CA 和服务器证书）
- **下载** `root.der` 和 `server.der` 文件

**步骤 3**：在 Orbic 上启用 Root Shell
- 连接到 Orbic WiFi 网络
- **在网页表单中输入管理员密码**
- 点击 **"Enable Shell"**
- **网页利用 Orbic API** 在 24 端口打开 root shell

**步骤 4**：部署固件
- 点击 **"Deploy DagShell"** 按钮
- 脚本会上传：
  - `orbic_app`（主固件二进制文件）
  - `root.der`（根证书）
  - `server.der`（TLS 服务器证书）
  - `dagshell_boot.sh`（持久化脚本）
- **安装需要 2-3** 分钟

**步骤 5**：重启 Orbic
- 关闭并重新启动设备
- DagShell 会在开机时自动启动

**步骤 6**：访问 DagShell
- 在浏览器中打开 `https://192.168.1.1:8443/`
- **接受安全警告**（自签名证书会触发此预期提示）
- 如果出现提示，请使用默认凭据登录

### 方法二：手动安装

适用于希望从源代码构建的**高级用户**。

#### 步骤 1：安装依赖

**Windows**:
```powershell
# 安装 Python 3
# 从 python.org 下载

# 安装所需模块
pip install requests cryptography

# ARM 交叉编译器位于 gcc_win 文件夹
```

**macOS**:
```bash
# 如果尚未安装，请安装 Homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# 安装 Python 3
brew install python3

# 安装所需模块
pip3 install requests cryptography

# ARM 工具链位于 gcc_mac 文件夹
```

**Linux**:
```bash
# 安装 Python 3 和 pip
sudo apt-get update
sudo apt-get install python3 python3-pip

# 安装所需模块
pip3 install requests cryptography

# 安装 ARM 交叉编译器
sudo apt-get install gcc-arm-linux-gnueabihf
```

#### 步骤 2：克隆仓库

```bash
git clone https://github.com/dagnazty/DagShell.git
cd DagShell
```

#### 步骤 3：构建固件

**Windows**:
```powershell
cd orbic_fw_c
python gen_pki.py          # 生成证书
.\build.ps1                # 编译固件
```

**macOS/Linux**:
```bash
cd orbic_fw_c
python3 gen_pki.py         # 生成证书
./build.sh                 # 编译固件时会自动构建 BearSSL
```

**输出**：`orbic_app`（静态 ARM 二进制文件）和 DER 证书文件

**⚠️ macOS 注意事项**：`gcc_mac/` 目录包含使用 **crosstool-ng** 构建的自定义 ARM 工具链，目标为 **Linux kernel 3.2** 标头，以兼容 Orbic 的 3.18 内核。*Homebrew 标准 ARM 编译器面向更新的内核，**无法使用**。*

#### 步骤 4：在 Orbic 上启用 Root Shell

```bash
# 连接到 Orbic WiFi
# 将 YOUR_ADMIN_PASSWORD 替换为实际密码

python enable_shell.py YOUR_ADMIN_PASSWORD
```

此步骤利用 Orbic Web API 在 **24 端口**打开 root shell。

#### 步骤 5：部署固件

```bash
python deploy_base64.py
```

此命令会上传并安装：
- 将 `orbic_app` 放入 `/data/orbic_app`
- 将证书放入 `/data/root.der` 和 `/data/server.der`
- 将启动脚本放入 `/etc/rc.d/dagshell_boot.sh`

**持久性**：固件通过 init 脚本在重启后自动启动

#### 步骤 6：重启并访问

```bash
# 重启 Orbic（断电重启或通过 SSH）
reboot

# 重启后访问 DagShell
# 浏览器：https://192.168.1.1:8443/
```

### 安全证书警告

访问 DagShell 时会看到 **"Not Secure" (不安全) 或 "Not Trusted" (不受信任)** 警告：

**桌面浏览器**：
- 点击 **"Advanced" (高级)**
- 点击 **"Proceed to 192.168.1.1 (unsafe)" (仍要访问 192.168.1.1（不安全）)**

**移动浏览器**：
- 点击 **"Show Details" (显示详情)**
- 点击 **"visit this website" (访问此网站)**

**原因**：
- **证书是自签名的**，并非由 Let's Encrypt 等可信 CA 签发
- 设备的信任存储中没有根证书
- ***这是定制固件的预期行为**，不代表设备已被入侵。*

**连接是否安全？**：
- **是**，连接使用 **TLS 1.2+** 加密
- 数据无法被截取
- *证书没有通过公共 CA 建立可信证书链，但加密确实有效。*

**可选**：将 `root.der` 安装到设备的信任存储中，以消除警告

______

## Raspberry Pi Companion 设置

如需完整功能，**建议使用此可选扩展**。

### 硬件设置

**步骤 1**：准备组件
- **Raspberry Pi 3B**+ 或更新型号（$35-55）
- **U-Blox 7** 芯片组 USB GPS 接收器（$15-30）
- **用于安装 Pi OS** 的 16GB 或更大 MicroSD 卡（$10）
- **Pi 电源**（$10）

**步骤 2**：安装 Raspberry Pi OS
```bash
# 下载 Raspberry Pi Imager
# https://www.raspberrypi.org/software/

# 将 Raspberry Pi OS Lite 刷写到 SD 卡
# 启动 Pi 并完成设置
```

**步骤 3**：连接 GPS 接收器
- 将 USB GPS 接收器插入 Pi
- 检查识别情况：`lsusb`（应显示 GPS 设备）
- 确认串行端口：`ls /dev/ttyUSB*` 或 `ls /dev/ttyACM*`

### 软件安装

**步骤 1**：在 Pi 上克隆 DagShell 仓库

```bash
git clone https://github.com/dagnazty/DagShell.git
cd DagShell/pi_companion
```

**步骤 2**：安装依赖

```bash
# 更新软件包列表
sudo apt-get update

# 安装所需软件包
sudo apt-get install python3-serial python3-requests gpsd gpsd-clients

# 安装 Python 模块
pip3 install pyserial gps3 bluetooth pybluez
```

**步骤 3**：配置 GPS 守护进程

```bash
# 编辑 gpsd 配置
sudo nano /etc/default/gpsd

# 将 DEVICES 行设为 GPS 串口
DEVICES="/dev/ttyUSB0"  # 按需调整

# 重启 gpsd
sudo systemctl restart gpsd

# 测试 GPS
cgps -s  # 约 30 秒后应显示卫星数据
```

**步骤 4**：配置 Pi Companion

```bash
# 编辑配置文件
nano pi_companion/config.py

# 设置 Orbic IP 地址
ORBIC_IP = "192.168.1.1"
ORBIC_PORT = "8443"

# 设置 GPS 串口
GPS_DEVICE = "/dev/ttyUSB0"

# 保存并退出
```

**步骤 5**：安装 systemd 服务

```bash
# 复制服务文件
sudo cp pi_companion.service /etc/systemd/system/

# 重新加载 systemd
sudo systemctl daemon-reload

# 启用自动启动
sudo systemctl enable pi-companion

# 启动服务
sudo systemctl start pi-companion

# 检查状态
sudo systemctl status pi-companion
```

**步骤 6**：验证通信

```bash
# 检查日志
journalctl -u pi-companion -f

# 应能看到 GPS 坐标发送到 Orbic
```

### 网络设置

**选项 A**：WiFi 连接

```bash
# Pi 连接到 Orbic 热点
# 编辑 wpa_supplicant 配置
sudo nano /etc/wpa_supplicant/wpa_supplicant.conf

# 添加网络
network={
    ssid="Orbic_SSID"
    psk="PASSWORD"
}

# 重启 WiFi
sudo systemctl restart networking
```

**选项 B**：USB 以太网（推荐）

- **使用 USB 线连接** Pi 和 Orbic 的 USB 端口
- **在 Pi 上启用** USB gadget mode
- **Pi 会作为 USB** 以太网设备运行
- *持续传输数据时比 WiFi 更可靠*
- Pi 通过 Orbic 访问互联网

**USB Gadget 配置**：
```bash
# 编辑 config.txt
sudo nano /boot/config.txt

# 在末尾添加
dtoverlay=dwc2

# 编辑 cmdline.txt
sudo nano /boot/cmdline.txt

# 在 rootwait 后添加
modules-load=dwc2,g_ether

# 重启
sudo reboot
```

______

## 为什么将 DagShell 与 RayHunter 配合使用？

{{< figure src="dagshell-rayhunter-complementary-capabilities.webp" alt="对照图展示同一台 Orbic RCL400 热点上的 DagShell WiFi 巡行扫描和网络攻击工具，以及 RayHunter 的蜂窝协议异常检测功能" >}}

### 互补能力

**DagShell** 与 **RayHunter** 是**高度互补**的安全工具，分别覆盖移动安全研究的不同方面：

| 功能 | DagShell | RayHunter |
|---------|----------|-----------|
| **IMSI 捕获器检测** | 基础基站监控 | 高级模式分析 |
| **GPS 跟踪** | 有（通过 Pi） | 有（通过调制解调器） |
| **WiFi 巡行扫描** | 有 | 无 |
| **Bluetooth 扫描** | 有（通过 Pi） | 无 |
| **网络工具** | 有（DNS 嗅探、ARP 扫描、端口扫描） | 无 |
| **攻击工具** | 有（Evil Twin、强制门户、取消认证） | 无 |
| **隐私工具** | 有（TTL 修正、MAC 欺骗、广告拦截） | 少量 |
| **基站数据库** | 基础 | 全面 |
| **AI/ML 分析** | 无 | 有（异常检测） |
| **运营商协议分析** | 有限 | 深入（SS7/Diameter） |

### 协同用例

#### 1. **全面防御 IMSI 捕获器**

**场景**：在高监控区域旅行

**DagShell 的作用**：
- **实时监控基站变化**
- **发生可疑切换时跟踪 GPS 位置**
- **记录所有基站数据供后续分析**

**RayHunter 的作用**：
- **对蜂窝协议执行基于 ML 的异常检测**
- **检查 SS7**/Diameter 数据包以发现复杂攻击
- **提供已知可信基站数据库以供比较**

**组合优势**：****DagShell 持续监控****，RayHunter 深入分析

#### 2. **安全巡行扫描**

**场景**：绘制城市区域的 WiFi 网络地图

**DagShell 的作用**：
- **扫描 WiFi 并附加** GPS 坐标
- **使用网络分析工具查看信号强度和加密**
- **导出 Wigle CSV** 用于绘图

**RayHunter 的作用**：
- **巡行扫描时跟踪基站**
- **扫描 WiFi 时检测** IMSI 捕获器
- **蜂窝安全受到威胁时发出警告**

**组合优势**：**在了解蜂窝安全状态的同时安全巡行扫描**

#### 3. **安全研究实验室**

**场景**：红队或渗透测试

**DagShell 的作用**：
- **使用 Evil Twin** AP 测试 WiFi
- **使用强制门户演示社会工程**
- **使用取消认证攻击测试韧性**
- **提供网络侦察工具**

**RayHunter 的作用**：
- **测试期间检测你是否遭到监控**
- **提供基站安全态势信息**
- **防止测试期间受到反监控**

**组合优势**：**在具备防御意识的同时使用进攻工具**

#### 4. **注重隐私的旅行**

**场景**：记者或活动人士处于敏感环境

**DagShell 的作用**：
- **使用 TTL 屏蔽隐藏网络共享**
- **使用 MAC 欺骗保持匿名**
- **使用广告拦截防止跟踪**
- **监控 IMSI 捕获器**

**RayHunter 的作用**：
- **高级 IMSI 捕获器检测**
- **协议层攻击检测**
- **蜂窝安全警报**

**组合优势**：**通过多层防护实现更强隐私保护**

### 同时安装

**预刷写方案**（最简单）：
- 从 **STS Collective** 购买：[预装 RayHunter 和 DagShell 的 Orbic RCL400](https://stscollective.com/products/orbic-rcl400-rayhunter-dagshell-hotspot)
- **开箱即可使用**
- **两种固件均已测试和验证**
- **无需自行安装**

**自行安装**：
1. **先刷写 RayHunter**（参见[RayHunter 设备刷写完整指南](/articles/how-to-flash-rayhunter-devices-complete-guide/)）
2. **再刷写 DagShell**，两者可共存
3. **RayHunter 使用默认端口**
4. **DagShell 使用 8443** 端口
5. 使用不同浏览器标签页访问两者

**不会冲突**：
- RayHunter 使用 **80/443** 端口
- DagShell 使用 **8443** 端口
- 两者互不干扰
- **可以同时运行**

不想自行安装？预刷写版 **[RayHunter 与 DagShell Orbic RCL400](https://stscollective.com/products/orbic-rcl400-rayhunter-dagshell-hotspot)** 开箱即可使用。在 STS Collective 购物时使用读者代码 **SIMEONONSECURITY**，最高可享 20% 折扣。

{{< centerbutton href="https://stscollective.com/discount/SIMEONONSECURITY" >}}
  购买预刷写 RCL400，立省 20%
{{< /centerbutton >}}

______

## 实际用例

### 用例 1：安全研究员

**背景**：执行 WiFi 安全评估的渗透测试人员

**使用的 DagShell 工具**：
- **使用 WiFi 巡行扫描绘制客户网络地图**
- **使用 ARP 扫描器发现设备**
- **使用端口扫描器识别服务**
- **使用 Evil Twin** 和强制门户测试对社会工程的抵御能力
- **使用文件浏览器导出结果**

**工作流程**：
1. 绕客户设施外围行驶
2. 巡行扫描并绘制 WiFi 覆盖地图
3. 获得许可后创建客户网络的 Evil Twin
4. 监控客户端的连接尝试
5. 根据收集的数据生成报告

**RayHunter 集成**：确保研究员在评估期间没有遭到监控

### 用例 2：隐私倡导者

**背景**：出国旅行的记者

**使用的 DagShell 工具**：
- **使用 TTL 修正绕过运营商限制**
- **使用 MAC 欺骗隐藏设备身份**
- **使用 IMSI 捕获器检测器了解监控风险**
- **使用 DNS 嗅探器检查设备是否泄漏数据**
- **使用广告拦截防止跟踪**

**工作流程**：
1. 使用设备前启用 TTL 修正
2. 随机化 MAC 地址
3. 持续监控 IMSI 捕获器检测器
4. 为所有连接设备启用广告拦截
5. 记录可疑蜂窝活动

**RayHunter 集成**：在基础监控之外提供高级 IMSI 捕获器检测

### 用例 3：网络管理员

**背景**：管理多个场所的 IT 管理员

**使用的 DagShell 工具**：
- **使用 WiFi 巡行扫描验证覆盖范围**
- **使用 ARP 扫描器盘点设备**
- **使用端口扫描器执行安全审计**
- **使用活动连接监控器查看未授权流量**
- **使用防火墙管理器屏蔽 IP**

**工作流程**：
1. 在场所内巡行扫描，验证 WiFi 覆盖范围
2. 执行 ARP 扫描以发现所有网络设备
3. 扫描服务器端口，查找暴露的服务
4. 通过防火墙屏蔽恶意 IP
5. 导出报告以供记录

**RayHunter 集成**：为使用移动设备的场所监控蜂窝安全

### 用例 4：IoT 安全研究员

**背景**：分析 IoT 设备安全性的研究员

**使用的 DagShell 工具**：
- **使用带 OUI 查询功能的** ARP 扫描器识别 IoT 设备
- **使用端口扫描器查找开放服务**
- **使用 DNS 嗅探器捕获** IoT 流量模式
- **使用 Bluetooth 扫描器**（Pi）查找 BLE IoT 设备
- **使用路由跟踪分析连接**

**工作流程**：
1. 在测试环境中部署 Orbic 和 Pi
2. 执行 ARP 扫描以发现 IoT 设备
3. 扫描端口，查找易受攻击的服务
4. 扫描 BLE，查找 Bluetooth IoT 设备
5. 嗅探 DNS，分析设备“回连”行为
6. 记录漏洞

**RayHunter 集成**：检测 IoT 设备是否具备蜂窝连接，并监控异常

{{< figure src="dagshell-rayhunter-combined-mobile-security-research-use-cases.webp" alt="展示 DagShell 与 RayHunter 四种联合应用的示意图：安全研究员、隐私倡导者、网络管理员和 IoT 研究员" >}}

______

## 法律与伦理注意事项

### 法律框架

**DagShell 等工具的法律边界并不总是明确**：

**合法用途**：
**✅ 测试自己的设备和网络**
**✅ 获得书面许可后执行渗透测试**
**✅ 在隔离实验室环境中学习**
**✅ 在自己的设备上使用 TTL** 修正和 MAC 欺骗保护隐私
**✅ 进行安全研究并负责任地披露漏洞**

**非法用途**：
**❌ 攻击不属于自己的网络**（违反 CFAA）
**❌ 对他人网络发动取消认证攻击**（违反 FCC 规定，可能构成重罪）
**❌ 对公众发动 Evil** Twin 攻击（电信欺诈、身份盗用）
**❌ 未经同意嗅探他人的 DNS**（窃听）
**❌ 绕过安全措施实施欺诈**

### 需要了解的法律

**美国**：
- **Computer Fraud and** Abuse Act (CFAA)：未经授权访问计算机或网络
- **Wiretap Act**：截取电子通信
- **FCC 规定**：无线电频率干扰，包括取消认证攻击

**英国**：
- **Computer Misuse Act** 1990：与 CFAA 类似
- **Regulation of Investigatory** Powers Act (RIPA)：通信截取限制

**欧盟**：
- **GDPR**：数据保护，包括扫描可识别的 BLE/WiFi 数据
- *各国的地方法规和执法力度差异很大。*

### 伦理准则

**应该做**：
- **✅ 仅在自己的设备和网络上使用**
- **✅ 测试他人系统前取得书面许可**
- **✅ 发现漏洞后负责任地披露**
- **✅ 在受控环境中用于教育**
- **✅ 保护自己的隐私**

**不应该做**：
- ❌ 攻击不属于自己的网络
- ❌ 收集陌生人的凭据
- ❌ 干扰关键基础设施
- ❌ 恶意使用工具
- ❌ 散布捕获的数据

### 负责任使用声明

DagShell 是一款**安全研究与隐私工具**。它的功能与 **Kali Linux**、**WiFi Pineapple** 或 **HackRF** 等专业渗透测试工具相似。

**意图很重要**：**恶意黑客**和**安全专业人员**会使用相同工具，区别在于：
- **是否获得测试授权**
- **是为了提升安全还是造成伤害**
- **是报告发现还是利用漏洞**

**请****负责任且合乎伦理地**使用 DagShell。*如果不确定某项操作是否合法，请先停止并咨询律师。*

{{< figure src="dagshell-legal-ethical-security-research-responsible-use.webp" alt="DagShell 安全研究的法律与伦理框架图，展示授权与未授权用例及相关法律" >}}


______

## 故障排除

### 安装问题

**问题**：`enable_shell.py` 无法连接

**解决方法**：
- **确认已连接到 Orbic WiFi**
- 检查 IP 地址是否为 **192.168.1.1**（默认值）
- 再次输入管理员密码，注意区分大小写
- 检查 80 端口是否可访问：`telnet 192.168.1.1 80`

**问题**：固件上传失败

**解决方法**：
- 先确认 root shell 已启用（`enable_shell.py` 已成功）
- 检查网络稳定性，尽可能使用有线连接
- 尝试使用 `deploy_net.py`，代替 `deploy_base64.py`
- 检查 `/data` 分区空间：`df -h /data`

**问题**：证书警告一直出现

**解决方法**：
- ***自签名证书出现此提示是正常的**，连接仍然经过加密。*
- 每次都点击“Advanced” (高级)->“Proceed anyway” (仍要继续)
- **可选**：将 `root.der` 安装到设备的信任存储中

### 运行问题

**问题**：DagShell 未在开机时启动

**解决方法**：
- 检查启动脚本：`ls -la /etc/rc.d/dagshell_boot.sh`
- 确认脚本可执行：`chmod +x /etc/rc.d/dagshell_boot.sh`
- 检查日志：`logread | grep dagshell`
- 手动启动：`/data/orbic_app &`

**问题**：GPS 不工作

**解决方法**：
- **确认 Pi Companion** 正在运行：`systemctl status pi-companion`
- 检查 GPS 是否已锁定卫星：`cgps -s`（在 Pi 上）
- 确认 GPS 接收器已连接：`lsusb`
- *冷启动定位需等待 5-10 分钟，首次在室外启动时 GPS 定位会更慢。*

**问题**：巡行扫描没有记录数据

**解决方法**：
- 开始前确认 GPS 已定位
- 检查 `/data` 是否可写
- 确认 CSV 文件是否生成：`ls -la /data/wardrive_log.csv`
- 检查 WiFi 接口是否已启用：`ifconfig wlan0`

**问题**：Pi Companion 无法与 Orbic 通信

**解决方法**：
- 检查网络连通性：`ping 192.168.1.1`
- 检查配置文件中的 IP 是否正确
- 确认 8443 端口已开放：`telnet 192.168.1.1 8443`
- 查看 Pi Companion 日志：`journalctl -u pi-companion`

### 性能问题

**问题**：网页界面缓慢或卡顿

**解决方法**：
- 清除浏览器缓存
- 禁用浏览器扩展，广告拦截器可能造成干扰
- **使用有线连接连接 Orbic**，代替 WiFi
- 重启 DagShell：`killall orbic_app && /data/orbic_app &`

**问题**：巡行扫描耗时过长

**解决方法**：
- 在设置中增加扫描间隔，以较低频率换取更好的性能
- 减少扫描的频道数量
- *GPS 定位信号弱会拖慢扫描，系统会等待有效坐标后再记录。*

{{< figure src="dagshell-troubleshooting-installation-gps-wardriving-common-issues.webp" alt="DagShell 故障排除流程图，展示安装、GPS 和巡行扫描常见问题及其分步解决方案" >}}


______

## 高级配置

### 自定义 DagShell

**修改源代码**：
- 编辑 `orbic_fw_c/` 目录中的文件
- 使用 `build.sh` 或 `build.ps1` 重新构建
- 重新部署固件

**添加自定义页面**：
- DagShell 在 C++ 代码中嵌入 HTML
- 编辑 `main.cpp` 添加新路由
- 重新编译并部署

**自定义证书**：
- 使用 `gen_pki.py` 生成自己的 PKI
- **或使用 OpenSSL 创建证书**
- 替换 `root.der` 和 `server.der`

### 与其他工具集成

**将数据导出到 Wireshark**：
```bash
# 抓取 pcap 文件
tcpdump -i wlan0 -w /data/capture.pcap

# 通过文件浏览器下载
# 在电脑上的 Wireshark 中打开
```

**将 GPS 轨迹导入 QGIS**：
```bash
# 导出为 GPX 格式
python gps_to_gpx.py /data/gps_coords.txt

# 导入到 QGIS 作为矢量图层
```

**与外部数据库同步**：
```python
# 将 wardrive 数据上传到 MySQL 的自定义脚本
import mysql.connector
import csv

conn = mysql.connector.connect(
    host="your_server",
    user="username",
    password="password",
    database="wardriving"
)

with open('/data/wardrive_log.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        cursor.execute("INSERT INTO networks (ssid, bssid, lat, lon) VALUES (%s, %s, %s, %s)",
                      (row['SSID'], row['MAC'], row['Latitude'], row['Longitude']))
conn.commit()
```

### 性能调优

**优化扫描速度**：
```bash
# 编辑 wardrive 扫描间隔
# 在 DagShell 网页界面将 5 秒改为 3 秒以加快扫描
# 代价是 CPU 使用率上升，且可能漏掉网络
```

**优化电池使用**（使用外接电池时）：
```bash
# 降低 Orbic 屏幕亮度
# 禁用未使用的功能（不需要时关闭 BT 和 GPS）
# 在 wardrive 会话之间使用睡眠模式
```

______

## 与其他方案比较

### DagShell 与 WiFi Pineapple

| 功能 | DagShell (Orbic RCL400) | WiFi Pineapple |
|---------|------------------------|----------------|
| **价格** | $60-80 + 设备 | $99-299 |
| **蜂窝网络** | ✅ 内置 4G LTE | ❌ 无（仅 WiFi） |
| **GPS** | ✅ 通过 Pi Companion | ⚠️ 通过 USB 接收器 |
| **Evil Twin** | ✅ 支持 | ✅ 支持 |
| **强制门户** | ✅ 支持 | ✅ 支持 |
| **取消认证** | ✅ 支持（通过 Pi） | ✅ 支持 |
| **巡行扫描** | ✅ 支持 | ✅ 支持 |
| **IMSI 检测** | ✅ 基础功能 | ❌ 不支持 |
| **便携性** | ✅ 高度便携 | ⚠️ 中等 |
| **电池** | ✅ 内置 | ⚠️ 需要外接 |
| **学习难度** | 中等 | 低（界面完善） |

**推荐选择**：****移动蜂窝安全研究选 DagShell****，使用简单界面进行 WiFi 专项测试选 Pineapple。

### DagShell 与 Pi 上的 Kali Linux

| 功能 | DagShell | Pi 上的 Kali |
|---------|----------|-----------|
| **设置时间** | 15 分钟 | 2-3 小时 |
| **蜂窝 LTE** | ✅ 内置 | ❌ 需要 USB 调制解调器 |
| **网页界面** | ✅ 有 | ⚠️ 有限（需要 VNC/SSH） |
| **工具数量** | 约 15 个 | 600+ 个 |
| **专长** | 移动安全 | 通用渗透测试 |
| **便携性** | ✅ 口袋大小 | ⚠️ 需要屏幕和电源 |
| **电池续航** | 8-10 小时 | 2-4 小时 |

**推荐选择**：****移动专项任务选 DagShell****，综合工具包选 Kali。

### DagShell 与 Orbic 原厂固件

| 功能 | DagShell | 原厂固件 |
|---------|----------|----------------|
| **安全工具** | ✅ 丰富 | ❌ 无 |
| **隐私功能** | ✅ 有 | ❌ 很少 |
| **自定义** | ✅ 完全可定制 | ❌ 锁定 |
| **巡行扫描** | ✅ 支持 | ❌ 不支持 |
| **GPS** | ✅ 支持（通过 Pi） | ❌ 不支持 |
| **开源** | ✅ 是 | ❌ 专有 |
| **支持** | ⚠️ 社区 | ✅ 官方 |
| **稳定性** | ⚠️ Beta | ✅ 生产级 |

**推荐选择**：****研究员选 DagShell****，普通用户选原厂固件。

______

## 结论：完整的移动实验室

**DagShell** 将普通的 **Orbic RCL400 热点**变成一套具备多种能力的**移动安全实验室**：

**✅ 隐私保护**：TTL 屏蔽、MAC 欺骗和广告拦截
**✅ 网络监控**：连接、DNS 和路由
**✅ 安全测试工具**：IMSI 检测、端口扫描和 ARP 发现
**✅ 攻击能力**：Evil Twin、强制门户和取消认证
**✅ 集成 Wigle** 的 GPS 巡行扫描
**✅ Raspberry Pi** 扩展：BLE、WiFi 和 GPS
**✅ 便携并由电池供电**
**✅ 开源且可自定义**

### 与 RayHunter 配合使用

**RayHunter + DagShell** = **完整的移动安全平台**：
- **RayHunter 提供高级 IMSI** 捕获器检测
- **DagShell 提供攻击与隐私工具**
- **两者可在同一设备上同时运行**
- **功能互补**，没有重复
- **一个便携套件满足移动安全需求**

### 立即开始

**方案一：预刷写设备**（最简单）
- **STS Collective**：[预装 RayHunter 和 DagShell 的 Orbic RCL400](https://stscollective.com/products/orbic-rcl400-rayhunter-dagshell-hotspot)
- **到货即可使用**
- 无需自行安装
- 由专业人员配置

**方案二：自行安装**
- 按照本指南操作
- **已有 Orbic RCL400** 则无需额外设备费用
- 学习安装过程
- 按需定制

### 延伸阅读

- **[RayHunter 设备刷写完整指南](/articles/how-to-flash-rayhunter-devices-complete-guide/)** - 先安装 RayHunter
- **[RayHunter 设备对比完整评测](/articles/rayhunter-device-comparison-2026-complete-review/)** - 选择合适平台
- **[Flock-You 检测项目：反监控硬件指南](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/)** - 了解更多检测工具

### 最后建议

无论你是**安全研究员**、**渗透测试人员**、**隐私倡导者**还是**网络管理员**，DagShell 都能为移动安全工作提供**便携、实用且价格适中的**平台。

**免责声明**：请负责任地使用。只测试自己拥有或已获得明确书面许可的网络和设备。遵守法律和伦理，祝安全测试顺利！🚀

{{< figure src="dagshell-orbic-rcl400-mobile-security-lab-conclusion-overview.webp" alt="安装 DagShell 固件的 Orbic RCL400 热点，组成完整的便携式移动安全研究实验室" >}}


______

## 参考资料

1. [DagShell GitHub 仓库](https://github.com/dagnazty/DagShell)
2. [DagShell 文档](https://dagnazty.github.io/DagShell/)
3. [STS Collective - 预刷写设备](https://stscollective.com/products/orbic-rcl400-rayhunter-dagshell-hotspot)
4. [WiGLE - WiFi 地图项目](https://wigle.net/)
5. [《计算机欺诈与滥用法案》（CFAA）](https://www.law.cornell.edu/uscode/text/18/1030)
6. [Raspberry Pi 官方文档](https://www.raspberrypi.org/documentation/)
7. [U-Blox GPS 模块文档](https://www.u-blox.com/)
8. [OUI 数据库 - IEEE 标准](https://standards.ieee.org/products-programs/regauth/)
9. [iptables 教程](https://www.netfilter.org/documentation/)
10. [OpenSSL 文档](https://www.openssl.org/docs/)
