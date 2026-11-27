---
title: Home Assistant Core 2026.11 回退到 2026.10.4：修复 HTTP 存储版本 3
date: 2026-11-15
lastmod: 2026-11-27
toc: true
draft: false
description: Home Assistant Core 2026.11 在 Yellow 上回退到 2026.10.4 后，修复 HTTP 存储版本 3 错误。包含带保护措施的命令和经过验证的输出。
genre:
- 家庭自动化
- 故障排查
tags:
- Home Assistant Yellow
- Home Assistant OS
- Core 2026.11 回退
- Core 2026.10.4
- HTTP 存储版本 3
- CM4
cover: /img/cover/home-assistant-yellow-core-rollback-http-recovery.webp
coverAlt: 黄色计算机板、断开的配置链接和已恢复的网页仪表盘插图
coverCaption: ''
---

Home Assistant Core 2026.11 更新失败后，我的 Yellow CM4 回退到了 2026.10.4。Yellow 仍可通过网络访问，但不再提供仪表盘。回退后，HTTP 设置文件的存储版本为 3.1，而 Core 2026.10.4 支持版本 2.2。我保留了原文件，在严格检查下转换其副本，恢复 HTTP 访问，然后将 Core 更新到 2026.11.1。

<!--more-->

## 要点

- **确认版本不匹配。** 将 Core 日志错误与已安装的版本和 HTTP 存储版本对照。
- **保留文件。** 恢复前，保留未更改的副本和一份设备外备份。
- **验证结果。** 检查 Core 状态、已保存的监听端口、仪表盘和已安装版本。

**针对本案例的修复步骤：**[保留 HTTP 文件](#preserve-recovery-options)，[创建并验证版本 2.2 候选文件](#apply-the-tested-fix-for-version-31)，[停止 Core 后安装该文件](#apply-the-tested-fix-for-version-31)，并[验证更新结果](#verify-the-update-outcome)。转换过程会检查原始字段，字段不一致时停止。不要将此方法用于未经检查的 HTTP 文件。

## 开始之前

你需要能接触 Yellow CM4、USB-C 数据线、可用的串行控制台，以及可用备份或保留的配置。手动步骤需要访问主机 shell，并仔细检查 JSON。请为诊断和修复留出至少 30 分钟。大型安装中的 Core 启动和备份恢复需要更长时间。

## 识别故障

Core 日志中出现了决定性错误：

```text
Storage file http has version 3 which is newer than the max supported version 2
```

较旧的 Core 版本无法加载 `http`。前端和其他依赖 HTTP 的组件也无法工作。路由器租约正常、Observer 页面可访问，都不能证明仪表盘可用。[Home Assistant Core 问题 #190583](https://github.com/home-assistant/core/issues/190583)记录了多个安装中出现的同类回退故障，包括 Yellow。[我在该问题下的评论](https://github.com/home-assistant/core/issues/190583#issuecomment-6908185955)记录了在这台 Yellow 上测试的恢复方法和 Core 最终状态。

**网页无法访问的原因：**Core 2026.11 将 `.storage/http` 写成 3.1 格式。回退恢复了 Core 2026.10.4，却没有恢复兼容的 HTTP 文件。Core 2026.10.4 会拒绝存储版本 3。这台 Yellow 保存的 `intermediate_v6` 配置也不符合旧版架构。首次更新为何失败并触发回退，原因未知。截至 2026-11-15，相关问题仍处于开放状态，讨论中没有维护者确认的修复方案。

更改文件之前，检查已安装的 Core 版本和 HTTP 存储：

```bash
ha core info --raw-json | jq -r '.data.version'

storage=/mnt/data/supervisor/homeassistant/.storage
jq '{version, minor_version, pending_present: (.data.pending != null), profile: .data.stable.ssl_profile}' "$storage/http"
ha core logs | grep -F 'Storage file http has version 3'
```

以下输出对应本案例，其中时间戳和私人信息已删除：

```text
2026.10.4
{
  "version": 3,
  "minor_version": 1,
  "pending_present": false,
  "profile": "intermediate_v6"
}
Storage file http has version 3 which is newer than the max supported version 2
```

以下恢复命令会比较 Supervisor 保存的监听端口与 HTTP 文件中的值，但不会显示任何一个值。如果二者不同，请先检查 Core 的实际监听端口，再更改文件。

| 信号 | 含义 |
| --- | --- |
| Core 支持存储版本 2，文件报告版本 3 | 旧版本无法加载已保存的 HTTP 设置 |
| HTTP 文件与 Supervisor 列表中的监听端口不同 | 判断原因前，先检查 Core 的实际监听端口 |
| 首页有响应，但 Core 状态仍为 STARTING | 前端有响应并不能证明启动已完成 |

## 保留恢复选项 {#preserve-recovery-options}

再次更新前，请在 Yellow 设备之外保留可用备份。[Home Assistant 备份指南](https://www.home-assistant.io/common-tasks/general/backups/)介绍了云端和设备外的存储位置。加密备份需要对应的恢复密钥。排查此存储版本不匹配问题时，不要擦除 NVMe 数据盘。

编辑 HTTP 文件之前，先复制它：

```bash
storage=/mnt/data/supervisor/homeassistant/.storage
test ! -e "$storage/http.before-recovery" &&
  cp -p "$storage/http" "$storage/http.before-recovery" &&
  cmp -s "$storage/http" "$storage/http.before-recovery"
```

如果命令失败，请停止。不要覆盖已有的同名恢复副本。选择新名称，并在继续前重新检查。

仪表盘不可用时，请使用 Yellow 的串行控制台。[Nabu Casa 的 Linux 和 macOS 指南](https://support.nabucasa.com/hc/en-us/articles/25454972435357-Using-the-serial-console-on-Home-Assistant-Yellow-for-debugging-Linux-macOS)介绍了 USB-C 连接方式和 JP1 UART 位置。请按照适用于你硬件的 CM4 说明操作。

## 应用针对版本 3.1 测试过的修复方法 {#apply-the-tested-fix-for-version-31}

首选方法是使用更新前的兼容 HTTP 文件。如果适合完整恢复，请按照 Home Assistant 文档中的流程恢复备份。如果只提取一个文件，请先确认其存储版本和保存的监听端口，再替换活动文件。没有可用的兼容 HTTP 文件时，我在这台 Yellow 上测试的直接修复方法就是下面的命令。

[该问题最初的临时解决方法](https://github.com/home-assistant/core/issues/190583)会移走 `.storage/http`，让旧版 Core 创建新文件。后续一篇[关于 Yellow 的报告](https://github.com/home-assistant/core/issues/190583#issuecomment-6749568119)显示，重新生成的文件使用了不同的监听端口。确认网页界面已修复之前，请检查新文件和 `ha core info` 的结果。

我的安装没有 `http:` YAML 块、待处理的 HTTP 配置，稳定设置中也没有 TLS 证书或密钥。保存的配置为 `intermediate_v6`。在这个有限条件下，我单独创建了版本 2.2 候选文件，并保留现有监听端口：

```bash
storage=/mnt/data/supervisor/homeassistant/.storage

expected=$(ha core info --raw-json | jq -r '.data.port') &&
stored=$(jq -r '.data.stable.server_port' "$storage/http") &&
test -n "$expected" &&
test "$expected" != null &&
test "$expected" = "$stored" &&
test ! -e "$storage/http.v2-candidate" &&
jq -e '
  if .version == 3 and .minor_version == 1 and
     .data.pending == null and
     .data.stable.ssl_profile == "intermediate_v6" and
     (.data.stable | has("ssl_certificate") | not) and
     (.data.stable | has("ssl_peer_certificate") | not) and
     (.data.stable | has("ssl_key") | not) and
     (.data.stable | has("trusted_proxies") | not) and
     (.data.stable | has("use_x_forwarded_for") | not)
  then .version = 2 | .minor_version = 2 | .data.stable.ssl_profile = "intermediate"
  else error("Unexpected HTTP config. Stop and inspect")
  end
' \
  "$storage/http" > "$storage/http.v2-candidate" &&

jq -e '.version == 2 and .minor_version == 2 and .data.pending == null and .data.stable.ssl_profile == "intermediate"' \
  "$storage/http.v2-candidate" >/dev/null &&

test "$(jq -r '.data.stable.server_port' "$storage/http")" = \
  "$(jq -r '.data.stable.server_port' "$storage/http.v2-candidate")"
```

替换活动文件前，上述每条命令都必须成功。如果 `jq` 失败，请先检查候选文件，再决定是否删除并重试。[Core 2026.10.4 的 HTTP 源码](https://github.com/home-assistant/core/blob/2026.10.4/homeassistant/components/http/config.py)定义了存储版本 2.2，并接受 `intermediate` 配置。[Core 2026.11.1 的源码](https://github.com/home-assistant/core/blob/2026.11.1/homeassistant/components/http/config.py)使用版本 3.1 和带版本号的配置名称。安装前，我还使用已安装旧版 Core 中的 `HTTP_STORAGE_SCHEMA` 验证了候选文件。

容器仍在运行时，使用已安装的旧版 Core 执行架构检查：

```bash
docker exec homeassistant python3 -c '
import json
from homeassistant.components.http.config import HTTP_STORAGE_SCHEMA
with open("/config/.storage/http.v2-candidate") as source:
    data = json.load(source)
stable = {
    key: value for key, value in data["data"]["stable"].items()
    if key not in ("created_at", "error", "error_message")
}
HTTP_STORAGE_SCHEMA(stable)
print("架构已通过验证")
'
```

如果架构检查拒绝候选文件，请停止。此步骤无法验证每个集成，也无法验证未经测试的 HTTP 存储形式。

该候选文件的架构检查结果为 `架构已通过验证`。出现其他结果时，请停止此恢复流程。

这项手动转换只针对所述字段进行了测试。包含 TLS 设置、可信代理或待处理配置的文件需要单独审查。只更改最高层版本号，会留下旧版 Core 不接受的配置。

在我的案例中，Supervisor 有一个活动的 Core 任务，因此拒绝了 `ha core stop`。我从主机控制台停止 Core 容器，安装经过验证的候选文件，然后启动容器：

```bash
storage=/mnt/data/supervisor/homeassistant/.storage
jq -e '.version == 2 and .minor_version == 2 and .data.pending == null and .data.stable.ssl_profile == "intermediate"' \
  "$storage/http.v2-candidate" >/dev/null &&
  docker stop homeassistant &&
  test "$(docker inspect -f '{{.State.Running}}' homeassistant)" = false &&
  cmp -s "$storage/http" "$storage/http.before-recovery" &&
  mv "$storage/http.v2-candidate" "$storage/http" &&
  docker start homeassistant
```

停止后，如果命令失败，请先检查活动的 HTTP 文件，再运行 `docker start homeassistant`。如果文件已更改，请根据最新内容重新创建候选文件。执行此步骤后，HTTP 页面恢复了。仅有 HTTP 响应并不能证明 Core 已完成启动，因此我先检查 Supervisor 状态，再判断系统是否恢复。

在这台 Yellow 上，随后运行 `docker inspect -f '{{.State.Status}}' homeassistant` 得到 `running`。请求下一次更新前，请检查 `ha core info` 和仪表盘。

## 验证更新结果 {#verify-the-update-outcome}

HTTP 访问恢复后，我将 Core 更新到了 2026.11.1。请求此版本的命令是：

```bash
ha core update --version 2026.11.1
```

长时间启动后，命令报告失败。随后，Supervisor 将 Core 记录为 RUNNING，并显示 `Successfully started Home Assistant 2026.11.1`。状态检查显示，已安装版本是最新版本，HTTP 文件已再次迁移到版本 3.1，而且观察期间容器没有重启。通过身份验证的仪表盘成功加载。**即使更新命令报告失败，也要检查最终状态。**

在你的系统中，长时间更新后请检查版本、Supervisor 健康状态和容器状态：

```bash
ha core info --raw-json | jq '{version: .data.version, update_available: .data.update_available}'
ha supervisor info --raw-json | jq '{healthy: .data.healthy, supported: .data.supported}'
docker inspect -f '{{.State.Status}} restarts={{.RestartCount}}' homeassistant
```

在本案例中，第一条和第三条命令产生了以下已清理的结果：

```text
{
  "version": "2026.11.1",
  "update_available": false
}
running restarts=0
```

然后通过常用的本地地址打开仪表盘，确认实时状态已加载。等下一次备份完成并确认系统正常运行后，再删除保存的 HTTP 文件。

这台 Yellow 上的证据无法确定首次更新失败的原因。后续任务的失败信息也没有说明原因。已安装版本和正常工作的仪表盘，比单独的 CLI 消息更能证明最终状态，但二者都无法解释 Supervisor 为何将任务标记为失败。

## 后续步骤

如果 HTTP 存储错误仍存在，请检查保留的文件并恢复兼容备份，或运行能够读取该存储版本的 Core。较旧 Core 加载保留的版本 3 文件会再次发生故障。如果 Core 已达到 RUNNING，但个别设备仍不可用，请分别调查相应集成。请保留恢复副本和云端备份，直到下一次备份完成且仪表盘持续正常响应。
