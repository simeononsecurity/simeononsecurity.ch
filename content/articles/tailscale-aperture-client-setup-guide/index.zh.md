---
title: "Tailscale Aperture：2026 年配置 AI 客户端的推理和 MCP"
date: 2026-11-09
lastmod: 2026-11-20
toc: true
draft: false
description: "通过 Tailscale Aperture 转发模型请求和 MCP 工具。为另一台设备或网关配置 Codex、Claude Code、Claude Desktop、OpenCode 和 Hermes。"
genre: ["人工智能", "开发工具", "网络"]
tags: ["Tailscale Aperture", "Aperture 配置", "AI 代理", "LLM 网关", "MCP 网关", "Codex Aperture", "Claude Code Aperture", "Claude Desktop Aperture", "OpenCode Aperture", "Hermes Agent Aperture", "Codex MCP", "Claude MCP", "OpenCode MCP", "Hermes MCP", "AI 推理代理", "Responses API", "Anthropic Messages API", "远程 MCP", "Streamable HTTP", "Tailscale", "自托管 AI", "编程代理", "AI 客户端配置"]
cover: "/img/cover/tailscale-aperture-agent-setup.webp"
coverAlt: "Aperture 通过独立的蓝色推理路由和绿色工具路由，将客户端面板连接到模型与 MCP 工具服务"
coverCaption: ""
---

## 简介

Tailscale Aperture 为 AI 客户端提供一个接入 tailnet 的网关，用于模型推理和 Model Context Protocol (MCP) 工具。每个客户端都必须使用与其 API 协议相匹配的路由。MCP 工具使用单独的端点，Aperture 授权决定每个 Tailscale 身份能够访问哪些模型和连接器。

本指南介绍如何在 macOS、Linux 和 Windows 上配置 Codex、Claude Code、Claude Desktop、OpenCode 和 Hermes。内容涵盖命令行与桌面设置、如何查询当前身份可用的模型 ID，以及一个可复用的匿名化提示词，用于配置另一台设备或 Aperture 实例。

**路由选择：** 端点路径取决于网关和各 API 协议。`/codex` 这样的 Responses 路由不处理 Anthropic Messages 或 MCP 流量。确认网关主机名和每个客户端的推理路由。修改客户端设置前，请通过自己的 Aperture 访问权限查询模型 ID。

## 要点

- **模型流量**需要与客户端协议相符的 API 路由。
- **MCP 流量**使用单独的 `/v1/mcp` 端点。
- **网关权限**必须允许你的 Tailscale 身份使用相应模型和连接器。
- **客户端配置**只能证明设置已保存。还要验证真实请求和一次 MCP 工具调用。

## 路由如何配合

| 用途 | 客户端请求 | Aperture 路由 | 路由提供的服务 |
|---|---|---|---|
| Codex 和兼容 Responses 的模型 | OpenAI Responses API | 通常为 `/v1`。`/codex` 等自定义路径取决于部署。 | 模型推理 |
| Claude 模型推理 | Anthropic Messages API | 网关基础 URL。Aperture 处理 `/v1/messages` | 兼容 Claude 的推理 |
| MCP 工具 | Streamable HTTP MCP | `/v1/mcp` | 已配置连接器中的工具和资源 |

{{< figure src="aperture-client-routes.webp" alt="Codex 和 Hermes 使用 Responses 路由，Claude 使用 Anthropic Messages，MCP 客户端通过独立的 /v1/mcp 路由访问 Aperture 连接器" caption="模型推理和 MCP 流量使用不同的 Aperture 端点" >}}

**提供商根 URL：** Aperture 会把客户端请求路径追加到提供商基础 URL。将提供商的 `baseurl` 设置为其 API 根 URL。如果传入路径已包含 `/v1`，不要在上游基础 URL 中再添加 `/v1`。URL 构造、模型注册和授权方式见 [Aperture 配置参考](https://tailscale.com/docs/aperture/configuration)。

## 准备网关

**编辑前，**向 Aperture 管理员索取以下信息：

- **网关主机名：** 对于大多数已连接 tailnet 的客户端，使用 `http://`。Claude Desktop 推理要求使用 `https://` 和受信任的证书。
- **推理路由：** OpenAI Responses 和 Anthropic Messages 使用不同的请求格式。
- **模型 ID：** 使用下方端点查询当前 Tailscale 身份可用的模型。使用为该身份返回的准确 ID。
- **身份验证：** 确认客户端发送的是占位 API 密钥还是用户凭据。
- **MCP 端点：** tailnet 客户端通常使用 `http://<APERTURE_HOST>/v1/mcp`。Claude Desktop 推理要求 HTTPS 和受信任的证书。
- **访问授权：** 检查当前 Tailscale 身份对应的模型和连接器权限。

**网络访问：** 客户端设备必须通过 tailnet 访问网关。只有主机名并不代表有模型或工具权限。没有匹配的授权允许模型或连接器时，Aperture 会拒绝访问。

### 查询你的用户可用模型

**在已连接到同一 tailnet 的设备上查询模型列表。** Aperture 使用该设备的 Tailscale 身份，并返回授权给该用户的模型。详见[模型授权指南](https://tailscale.com/docs/aperture/how-to/grant-model-access)：

```sh
# macOS 或 Linux
curl -fsS http://<APERTURE_HOST>/v1/models
```

```powershell
# Windows PowerShell，使用 curl.exe 以绕过旧版 curl 别名
curl.exe -fsS http://<APERTURE_HOST>/v1/models
```

**读取结果：** 将返回的每个 `id` 用作模型 ID。检查 `metadata.provider.id` 以识别 Aperture 提供商。选择支持客户端 API 格式的模型。例如，Claude Desktop 需要 Anthropic Messages 模型。Aperture 的[模型目录](https://tailscale.com/docs/aperture/reference/chat)也列出了当前登录用户可用的模型标识符。

**缺少模型：** 如果预期模型未显示，请让 Aperture 管理员检查提供商配置和模型授权。用户不能通过该端点自行授权。

**URL 协议：** Tailscale 建议同一 tailnet 上的大多数客户端使用 `http://`。WireGuard 会加密此流量。Claude Desktop 要求使用 `https://` 和操作系统信任的证书。各客户端请使用下文指定的协议。

### 添加推理提供商

**OpenAI Responses：** 将上游提供商添加到 Aperture，并启用客户端使用的 API 格式。OpenAI 提供商可以添加如下配置片段：

```json
{
  "providers": {
    "openai": {
      "baseurl": "https://api.openai.com",
      "apikey": "<UPSTREAM_PROVIDER_KEY>",
      "models": ["<MODEL_ID>"],
      "compatibility": {
        "openai_chat": true,
        "openai_responses": true
      }
    }
  }
}
```

**Anthropic Messages：** 使用 Anthropic API 根 URL、`x-api-key` 授权格式和 `anthropic_messages` 兼容性。模型 ID 也必须列在提供商的 `models` 中。添加如下配置片段：

```json
{
  "providers": {
    "anthropic": {
      "baseurl": "https://api.anthropic.com",
      "apikey": "<UPSTREAM_PROVIDER_KEY>",
      "authorization": "x-api-key",
      "models": ["<CLAUDE_MODEL_ID>"],
      "compatibility": {
        "anthropic_messages": true
      }
    }
  }
}
```

**修改配置：** 将占位符替换为上游提供商的值，把配置片段添加到现有 Aperture 配置中。保留文件其余内容。为提供商支持的 API 启用相应兼容标记。

**访问授权：** Aperture 控制每个用户对模型和连接器的访问。只为每个目标 Tailscale 用户授予所需权限。以下示例为一名用户授权一个提供商模型和一个连接器：

```json
{
  "grants": [
    {
      "src": ["<TAILSCALE_USER>"],
      "app": {
        "tailscale.com/cap/aperture": [
          {"role": "user", "models": "openai/<MODEL_ID>"},
          {"connectors": ["teamtools/**"]}
        ]
      }
    }
  ]
}
```

**模型授权：** 在授权模式中使用提供商 ID 和模型 ID。[连接器设置指南](https://tailscale.com/docs/aperture/connectors/get-started)介绍当前的 `connectors.servers` 配置。旧版顶层 `mcp.servers` 配置已弃用。

### 添加 MCP 连接器

**MCP 连接器：** Aperture 连接上游 MCP 服务器，并通过 `/v1/mcp` 提供工具：

```json
{
  "connectors": {
    "servers": {
      "teamtools": {
        "protocol": "mcp",
        "url": "<UPSTREAM_MCP_ENDPOINT>"
      }
    }
  }
}
```

**连接器 URL：** 使用上游服务器的完整 MCP 端点。然后为你的 Tailscale 用户授权 `teamtools/**` 或范围更窄的工具模式。[MCP 代理参考](https://tailscale.com/docs/aperture/mcp-server)说明了单一客户端端点和连接器行为。

## Codex CLI 和桌面版

**共享设置：** Codex CLI 和桌面应用使用同一配置。在 macOS 和 Linux 上编辑 `~/.codex/config.toml`。在 Windows 上编辑 `%USERPROFILE%\.codex\config.toml`（会展开主目录的 shell 也支持 `~/.codex/config.toml`）。[Codex 应用介绍](https://openai.com/index/introducing-the-codex-app/)说明桌面应用会读取 Codex CLI 配置。Codex 用户设置位于 `~/.codex/config.toml`。[配置基础文档](https://learn.chatgpt.com/docs/config-file/config-basic)介绍了用户级提供商和 MCP 字段。将提供商添加到该文件，重启应用，然后确认界面中显示了提供商和模型。

```toml
model = "<MODEL_ID>"
model_provider = "aperture"

[model_providers.aperture]
name = "Aperture Proxy"
base_url = "http://<APERTURE_HOST>/v1"
wire_api = "responses"
requires_openai_auth = true
supports_websockets = false
```

**可选字段：** 这两个值对应一种 Codex 提供商配置。仅当网关和 Codex 配置需要时才保留。Tailscale 当前的 [Codex Aperture 指南](https://tailscale.com/docs/aperture/how-to/use-codex)省略了它们，使用 `wire_api = "responses"`，并说明 Aperture 会注入上游凭据。使用网关管理员提供的准确 Responses URL。`/codex` 是部署专用路由。Tailscale 文档中的默认路由是 `/v1`。

**MCP 配置：** 将服务器添加到同一用户配置：

```toml
[mcp_servers.aperture]
url = "http://<APERTURE_HOST>/v1/mcp"
enabled = true
```

**验证 Codex：** 运行 `codex mcp list`，启动新会话并检查 `/mcp`。服务器列表证明服务器已注册。工具出现在列表中且一次调用成功，才证明工具已发现并能执行。[Codex 配置参考](https://learn.chatgpt.com/docs/config-file/config-reference)介绍了用户级提供商和 MCP 设置。

## Claude Code CLI

**协议：** Claude Code 使用 Anthropic Messages。将 Claude Code 的全局设置文件指向兼容 Anthropic 的 Aperture 网关。在 macOS 和 Linux 上使用 `~/.claude/settings.json`，在 Windows 上使用 `%USERPROFILE%\.claude\settings.json`。PowerShell 中可使用 `$HOME\.claude\settings.json`。该路由必须处理 `/v1/messages`。Codex Responses 使用不同协议和路由。Tailscale 建议 Claude Code 在 tailnet 上使用 HTTP，因为 WireGuard 会加密连接。

```json
{
  "apiKeyHelper": "echo '-'",
  "env": {
    "ANTHROPIC_BASE_URL": "http://<APERTURE_HOST>"
  }
}
```

**客户端身份验证：** Aperture 客户端指南在 `apiKeyHelper` 中使用占位符，因为 Aperture 会注入上游凭据。如果要透传 Claude 订阅，Aperture 的 Anthropic 提供商必须转发用户的 Claude 凭据。此时不要设置 `ANTHROPIC_API_KEY` 和 `ANTHROPIC_AUTH_TOKEN`，因为这些变量会替代订阅凭据。请按 Claude Code 版本查看当前的 [Claude Code Aperture 说明](https://tailscale.com/docs/aperture/how-to/use-claude-code)，并参阅 [Anthropic 网关指南](https://code.claude.com/docs/en/llm-gateway-connect)了解身份验证方式。

**通过 HTTP 使用 MCP：** 运行以下命令添加端点：

```sh
claude mcp add --transport http --scope user aperture http://<APERTURE_HOST>/v1/mcp
claude mcp list
```

**验证 Claude Code：** 启动会话并运行 `/mcp`，确认连接成功。Anthropic 在其 [MCP 文档](https://code.claude.com/docs/en/mcp)中建议远程 MCP 服务器使用 HTTP。

## Claude Desktop 图形界面

**独立设置：** Claude Desktop 有一个第三方推理设置页面。此设置会将 Claude Desktop 的模型请求转发到 Aperture。MCP 配置需要另行完成。

1. 在 macOS 或 Windows 版 Claude Desktop 中选择**帮助 > 故障排除 > 启用开发者模式**。Linux 测试版如有此菜单，也执行相同操作。按提示重启应用。如果菜单不存在，请更新 Claude Desktop 并查看平台对应的发行说明。
2. 选择**开发者 > 配置第三方推理**。
3. 将**连接类型**设为**网关**，将**凭据类型**设为**静态 API 密钥**。
4. 在**网关基础 URL**中输入 `https://<APERTURE_HOST>`。使用受信任 TLS 证书覆盖的完整主机名。
5. 输入非空占位值，例如 `aperture`，作为网关密钥。Aperture 会忽略此占位值，并通过 tailnet 进行身份验证。
6. 自定义推理标头留空。
7. 添加已启用模型，并使用 `GET /v1/models` 为当前 Tailscale 身份返回的准确 ID。选择 Anthropic Messages 模型，手动填写模型 ID、显示名称和可选级别别名。Claude Desktop 不会在此页面自动发现模型。
8. 选择**保存更改**，再选择**应用更改**。退出并重新打开 Claude Desktop。

**协议检查：** [Aperture 的 Claude Desktop 指南](https://tailscale.com/docs/aperture/how-to/use-claude-desktop)说明 Claude Desktop 在 `/v1/messages` 上使用 Anthropic Messages。不要填写 Codex 路由 `/codex`，也不要选择 OpenAI 兼容连接类型。

### 将 Claude Desktop 连接到 MCP

**私有 MCP 访问：** 在 Claude Desktop 所在的同一台电脑上运行本地 stdio 桥接程序。将以下内容添加到 Claude Desktop 本地 MCP 配置：

```json
{
  "mcpServers": {
    "aperture": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "http://<APERTURE_HOST>/v1/mcp"]
    }
  }
}
```

**桥接方式：** 本地进程通过电脑的 Tailscale 连接访问 Aperture。按操作系统选择配置路径：macOS 为 `~/Library/Application Support/Claude/claude_desktop_config.json`；Windows 为 `%APPDATA%\Claude\claude_desktop_config.json`；Linux 测试版打开**设置 > 开发者 > 编辑配置**，使用 Claude Desktop 打开的路径。Linux 路径因软件包而异。重启 Claude Desktop，检查连接器列表，并执行一次无害的工具调用。[`mcp-remote` 项目](https://github.com/punkpeye/mcp-remote)介绍了这种本地到远程桥接方式。

**远程连接器：** Anthropic 的“设置 > 连接器”流程需要 Anthropic 服务能够访问的远程服务器。只对 tailnet 开放的主机名仅供你的设备使用，因此私有端点应采用本地桥接。如果公开 MCP 服务，请先配置身份验证和权限，再将其添加为云端连接器。参见 Anthropic 的[远程 MCP 连接器指南](https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp)。

## OpenCode CLI 和桌面版

**共享设置：** OpenCode CLI 和桌面应用读取同一份 OpenCode 配置。当前 OpenCode V2 文档使用 `providers` 映射配置自定义提供商，并将 MCP 服务器放在 `mcp.servers` 下。本示例使用 `/v1` 上兼容 OpenAI 的聊天端点。使用此模型路由前，确认 Aperture 提供商支持 OpenAI Chat Completions。

**全局配置：** 在 macOS 和 Linux 上编辑 `~/.config/opencode/opencode.json`。在 Windows 上使用 `%USERPROFILE%\.config\opencode\opencode.json`。添加兼容 OpenAI 的提供商，并将 `<MODEL_ID>` 替换为准确的 Aperture 模型 ID。OpenCode 也支持在同一目录使用 `opencode.jsonc` 添加注释。[配置参考](https://opencode.ai/docs/config/)说明全局设置和项目设置的优先级。

```jsonc
{
  "$schema": "https://opencode.ai/config.json",
  "model": "aperture/<MODEL_ID>",
  "providers": {
    "aperture": {
      "env": ["APERTURE_API_KEY"],
      "package": "@opencode/ai/providers/openai-compatible",
      "settings": {
        "baseURL": "http://<APERTURE_HOST>/v1"
      },
      "models": {
        "<MODEL_ID>": { "modelID": "<MODEL_ID>" }
      }
    }
  },
  "mcp": {
    "servers": {
      "aperture": {
        "type": "remote",
        "url": "http://<APERTURE_HOST>/v1/mcp",
        "oauth": false
      }
    }
  }
}
```

**客户端身份验证：** `oauth: false`会跳过 OpenCode 默认的 OAuth 流程。Aperture 通过 Tailscale 识别调用者。OpenCode 还需要提供商身份验证条目，因此在本地环境中设置 `APERTURE_API_KEY=-`。桌面应用也必须收到此变量。如果它没有继承 shell 环境，请在应用中运行 `/connect`，并为 Aperture 输入 `-`。不要将上游提供商密钥写入此文件。OpenCode 的[提供商指南](https://opencode.ai/docs/providers/)和[MCP 指南](https://opencode.ai/docs/mcp-servers/)说明当前格式。运行 `opencode mcp list` 检查服务器，再在应用中运行 `/mcps` 查看状态。

## Hermes CLI 和桌面版

**共享设置：** Hermes Agent 在 macOS 和 Linux 上将命名提供商和 MCP 服务器保存在 `~/.hermes/config.yaml`。Windows 原生安装使用 `%LOCALAPPDATA%\hermes\config.yaml`。运行 `hermes config path` 查看当前生效的文件。`HERMES_HOME` 可覆盖默认位置。本地 Hermes Desktop 使用与 CLI 相同的 Hermes 主目录和配置档案。如果 Desktop 连接远程 Hermes 网关，请在运行 Hermes 的机器上配置 Aperture，并确认服务器能访问 tailnet。参阅 [Hermes Desktop 指南](https://hermes-agent.nousresearch.com/docs/user-guide/desktop)了解本地和远程设置。

**Responses 提供商：** 添加一个命名提供商。`api` 必须与 Aperture 实例的 Responses 端点相符：

```yaml
providers:
  aperture:
    api: "http://<APERTURE_HOST>/v1"
    transport: codex_responses
    default_model: "<MODEL_ID>"
    # 仅当 Aperture 需要客户端密钥时添加 key_env。
    # key_env: APERTURE_API_KEY

model:
  provider: "custom:aperture"
  default: "<MODEL_ID>"
```

**选择协议：** 对于 OpenAI Chat Completions，设置 `transport: chat_completions`。对于 Anthropic Messages，设置 `transport: anthropic_messages`，并使用 Anthropic Messages 网关 URL。当前[提供商指南](https://hermes-agent.nousresearch.com/docs/integrations/providers)介绍 Hermes 命名提供商中的 `api`、`transport` 和 `default_model` 字段。

**MCP 配置：** 在同一 YAML 文件中添加 Aperture MCP：

```yaml
mcp_servers:
  aperture:
    url: "http://<APERTURE_HOST>/v1/mcp"
    enabled: true
```

**验证 Hermes：** 运行 `hermes mcp`，并在交互式服务器选择器中检查每个连接。本地 Desktop 使用相同的配置档案。Hermes 文档介绍了[远程 HTTP MCP 服务器](https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp)和完整的[MCP 配置参考](https://hermes-agent.nousresearch.com/docs/reference/mcp-config-reference)。

## 验证两条路径

**分别检查**模型推理和 MCP：

1. 确认设备已连接 Tailscale 且能访问网关。对于 Claude Desktop，还要确认网关提供受信任的 TLS 证书。
2. 通过每个已配置客户端发送简短提示。确认 Aperture 会话列表中出现对应请求。
3. 确认所选模型 ID 对应授权给当前 Tailscale 身份的模型。
4. 打开每个客户端的 MCP 状态页面或运行列表命令。确认 Aperture 服务器已连接并提供预期工具。
5. 调用一个只读工具。将返回内容与上游来源核对。
6. 如果模型或工具调用失败，请检查 Aperture 日志。配置已保存并不能证明请求成功。

| 现象 | 检查项 |
|---|---|
| 模型请求返回 404 或 405 | 确认客户端端点使用正确的路由和协议。不要将 `/codex` 用于 Anthropic Messages 或 MCP。 |
| 模型不可用 | 以目标 Tailscale 用户身份查询 `/v1/models`。检查准确 ID 是否存在，以及 API 格式是否适合客户端。请管理员检查缺少的提供商条目或授权。 |
| 请求未获授权 | 确认客户端需要占位符、Bearer 令牌还是订阅透传。不要把上游提供商密钥复制到公开项目文件。 |
| MCP 服务器已列出但没有工具 | 检查 `/v1/mcp`、连接器健康状态、连接器授权，以及客户端到 Aperture 的网络路径。 |
| Claude Desktop 无法连接私有 MCP URL | 运行 `mcp-remote` 等本地桥接程序，或使用已批准且配置了适当身份验证的公共连接器。 |

## 在另一台设备上重建配置

**新设备：** 安装同一个客户端，并先将设备连接到 tailnet。从新设备查询 `/v1/models`，查看授权给该 Tailscale 身份的模型。复用配置结构，凭据保存在本地。将 `<APERTURE_HOST>`、`<MODEL_ID>` 和 `<UPSTREAM_MCP_ENDPOINT>` 替换为目标 Aperture 实例的值。每种 API 协议使用独立端点，并为工具流量配置 `/v1/mcp`。最后验证一次模型请求和一次 MCP 工具调用。

**多个网关：** 每个 Aperture 实例使用单独配置。设备需要为 Codex 和 Hermes 配置 Responses 端点，为 Claude 配置 Anthropic Messages 端点，并为工具配置 MCP 聚合端点。将 API 凭据保存在各客户端的本地密钥存储或环境变量中。不要把 API 密钥复制到共享的 `config.toml`、`opencode.json`、`config.yaml` 或公共仓库。

## 可复用的 Aperture 配置提示词

**将这段匿名化提示词复制到编程助手中。** 替换为你的网关信息。助手必须先以你的 Tailscale 身份查询 Aperture，再选择模型 ID。

```text
配置我现有的 Tailscale Aperture 网关和此设备上已安装的 AI 客户端。

范围内的客户端：Codex CLI 和桌面版、Claude Code、Claude Desktop、OpenCode CLI 和桌面版、Hermes CLI 和桌面版。

先检测此设备运行 macOS、Linux 还是 Windows，识别当前 shell（例如 zsh、bash 或 PowerShell），并始终使用该平台的路径和命令语法。先检查当前网关、Tailscale 连接、客户端版本和现有客户端设置。阅读最新官方文档。保留无关配置，并在编辑每个文件前备份。不要猜测主机名、模型 ID、API 路由或凭据。上游提供商密钥应保存在 Aperture，不要放入客户端文件或本仓库。

从此 Tailscale 设备查询可用模型：
1. 使用客户端所用的 Tailscale 身份查询 `http://<APERTURE_HOST>/v1/models`。若网关文档指定了不同的模型列表 URL，则使用该 URL。
2. 读取每个模型的 `id` 和 `metadata.provider.id`。列表反映授权给我当前身份的模型。不要用管理员的列表替代，也不要编造 ID。
3. 根据客户端匹配模型的 API 兼容性。Codex 使用 OpenAI Responses，Claude 客户端使用 Anthropic Messages。OpenCode 和 Hermes 需要配置兼容的提供商和传输方式。
4. 尽可能保留客户端已有的默认模型。如果客户端必须设置默认模型而我没有偏好，请列出兼容模型并让我选择。Claude Desktop 要求手动输入准确模型 ID。
5. 如果端点没有返回适用模型，仅当我有管理员权限时才检查提供商和授权设置。否则，报告需要管理员授予的模型访问权限。不要给自己授权。

找到 Aperture 的部署和配置来源。不要假设文件路径，也不要替换整份配置。OpenAI Responses 要求 `openai_responses`；Anthropic 客户端要求 `anthropic_messages`。MCP 连接器使用当前的 `connectors.servers` 配置，客户端通过 `/v1/mcp` 连接。

更改共享网关前，先准备最小化的提供商、连接器和授权差异。仅当我有管理员权限且本请求授权更改网关时才应用。如果我没有权限，向实例所有者报告精确的建议变更。没有所有者明确授权时，不要创建或扩大授权。保留网关的所有现有设置。

按照最新官方格式和操作系统路径配置已安装的客户端：
- Codex CLI 和桌面版在 macOS/Linux 共用 `~/.codex/config.toml`，Windows 使用 `%USERPROFILE%\.codex\config.toml`。配置 Aperture 提供商、兼容模型、`wire_api = "responses"`，并在 `mcp_servers` 中配置 MCP。
- Claude Code 使用 `ANTHROPIC_BASE_URL` 和 HTTP 远程 MCP。macOS/Linux 使用 `~/.claude/settings.json`，Windows 使用 `%USERPROFILE%\.claude\settings.json`。
- Claude Desktop 使用开发者模式、“配置第三方推理”、Gateway、静态 API 密钥、带受信任证书的 HTTPS 网关 URL，以及为我当前用户查询到的模型 ID。私有 tailnet 上的 MCP 使用本地 `mcp-remote` 桥接。若可用，从“设置 > 开发者 > 编辑配置”查找 MCP 配置，否则使用检测到的系统所对应的文档路径。
- OpenCode 使用当前 V2 `providers` 模式和 `mcp.servers`。macOS/Linux 全局配置位于 `~/.config/opencode/opencode.json`，Windows 位于 `%USERPROFILE%\.config\opencode\opencode.json`。Aperture MCP 设置 `oauth: false`。必要时使用本地占位 API 密钥。
- Hermes 使用命名提供商、与模型 API 匹配的传输方式和 `mcp_servers`。macOS/Linux 使用 `~/.hermes/config.yaml`。Windows 运行 `hermes config path` 查看路径，通常为 `%LOCALAPPDATA%\hermes\config.yaml`。检查 Hermes Desktop 是否共享本地 Hermes 配置档案。

客户端支持时，tailnet 流量使用 HTTP。Claude Desktop 推理必须使用带受信任证书的 HTTPS。除非该网关文档指定其他路由，否则使用 `/v1`。

重启已配置的客户端。在 Aperture 中为每个客户端验证一次模型请求，并调用一次无害的只读 MCP 工具。报告当前身份发现的模型、修改的客户端和文件、验证结果及剩余管理员操作。不要安装软件、公开网关、提交更改或发布内容。
```

## 总结

Aperture 正常工作需要三个条件：网关可访问、模型路由与客户端协议匹配，以及对所需模型和 MCP 连接器的授权。相同的配置模式适用于 macOS、Linux 和 Windows，但每个客户端会将设置保存在不同的系统路径。

使用将要访问模型的 Tailscale 身份查询模型 ID。分别配置模型推理和 `/v1/mcp`，然后验证真实请求和只读工具调用。迁移到另一台设备或 Aperture 实例时，沿用本指南的配置结构，核对目标实例的路由和授权，并将凭据保存在本地密钥存储中。

## 后续步骤

**MCP 练习：** 要了解已保存服务器与已验证工具调用的区别，请阅读[MCP 服务器配置：权限、工具测试和安全移除](/articles/effective-ai-mcp-server-setup/)。了解更广泛的自托管架构，请参阅[混合 AI 代理集群：Tailscale、LiteLLM 和 Hermes](/articles/hybrid-agentic-ai-fleet-tailscale-litellm-hermes/)。
