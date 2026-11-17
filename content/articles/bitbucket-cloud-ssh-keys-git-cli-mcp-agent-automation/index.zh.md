---
title: "Bitbucket Cloud SSH 密钥：面向 AI 代理的只读 Git 访问"
date: 2026-10-11
lastmod: 2026-11-09
toc: true
draft: false
description: "为 AI 代理的只读工作流配置 Bitbucket Cloud SSH 密钥、Git CLI 访问、REST API 令牌、1Password 和 MCP 工具。"
genre: ["云安全", "开发工具", "系统管理"]
tags: ["Bitbucket Cloud", "Bitbucket SSH 密钥", "仓库访问密钥", "项目访问密钥", "工作区访问密钥", "Git CLI", "Bitbucket CLI", "1Password CLI", "1Password SSH Agent", "MCP", "Model Context Protocol", "REST API", "API 令牌范围", "代理权限", "只读自动化", "SSH 主机密钥"]
cover: "/img/cover/bitbucket-cloud-ssh-keys-git-cli-mcp-agent-automation.webp"
coverAlt: "终端工作流连接 Bitbucket Cloud Git 访问、限权 SSH 密钥、1Password、REST API 读取和 MCP 工具"
coverCaption: ""
---

**受限的代理工作流将仓库读取、API 读取、机密管理和远程写入分开。**通过 Secure Shell (SSH) 使用 Git 访问源代码，使用只读 Bitbucket 访问密钥执行自动检出，通过 REST API 读取元数据，并使用 Model Context Protocol (MCP) 服务器调用获准的工具。将私钥和 API 令牌保存在 1Password 中。写入操作须经过人工批准。

<!--more-->

## 要点

- **默认只读：**代理检出仓库时使用仓库或项目访问密钥。两者都不授予 push 权限。
- **个人身份：**与用户帐户关联的交互式工作使用个人 SSH 密钥。
- **机密保管：**使用 1Password SSH Agent，让 Git 发起获准的签名操作，而无需读取私钥。
- **CLI 的含义：**将 `git`、`curl` 和经过审计的小型 API 包装器视为实用的 Bitbucket 命令行工具。
- **MCP 边界：**只开放范围有限的读取工具。禁用写入工具，或将它们置于单独的审批流程之后。
- **写入审批：**允许代理检查、比较并准备更改。push、pull request、merge 或设置更新须经人工批准。

## 开始之前

**前提条件：**Bitbucket Cloud 访问权限、Git、OpenSSH 客户端、1Password 8、1Password CLI、已登录的 CLI 或获准的服务帐户，以及支持服务器审批控制的 MCP 主机。预留 45 分钟。难度为中级。

首次操作请使用测试仓库。替换示例中的所有占位符。下列命令未经测试，仅供示例参考，不代表真实的 Bitbucket 帐户或仓库。

**版本说明：**本文提供设计建议，不是针对特定版本编写的操作手册。测试前确认已安装的 Git、OpenSSH、1Password CLI、Teamwork Graph CLI、MCP 主机和 MCP 服务器版本。使用 `ssh-add -l` 前，先为当前操作系统配置 1Password SSH Agent。

**不要将凭据放入 shell、日志、URL、Git 远程地址或源文件。**使用 `<workspace>`、`<repository>`、`<api-token>` 和 `<socket-path>` 等占位符。不要在终端记录中粘贴真实私钥。

## 选择访问边界

Bitbucket Cloud 支持仓库、项目和工作区级访问密钥。密钥被复制后的影响取决于其范围。[官方访问密钥对比](https://support.atlassian.com/bitbucket-cloud/kb/difference-between-repository-project-and-workspace-access-keys/)明确说明了权限差异。

| 访问方式 | 范围 | 写入能力 | 适用场景 |
|---|---|---:|---|
| **仓库访问密钥** | 一个仓库 | 否 | 代理的默认检出方式 |
| **项目访问密钥** | 一个项目中的仓库 | 否 | 对少量仓库执行只读任务 |
| **工作区访问密钥** | 一个工作区中的仓库 | 是 | 配有独立写入计划的受控服务自动化 |
| **个人 SSH 密钥** | 用户获准访问的仓库 | 随用户帐户权限变化 | 交互式管理 |
| **API 令牌** | 与用户关联的 API 范围和帐户访问权限 | 取决于令牌范围 | REST API 读取或临时写入任务 |

**从满足需求的最小边界开始。**一个仓库足够时，选择仓库密钥。多个仓库属于同一项目且只需读取时，选择项目密钥。将工作区密钥视为写入身份，而非方便的默认选项。

通过对应的 Bitbucket 设置路径创建并登记权限最小的密钥：

1. 对一个仓库，打开 Repository settings、Access keys 和 Add key。粘贴公钥，并将密钥设为只读。
2. 多个仓库需要项目范围的读取身份时，打开 Project settings、Access keys 和 Add key。
3. 只有在共享工作区中具有获准的写入设计时才使用工作区访问密钥。个人工作区不提供相同的工作区级路径。
4. 记录密钥标签、范围、公钥指纹、所有者和轮换日期。将私钥保存在 1Password 中。

登记后，执行一次精确的只读连接测试：

```bash
git ls-remote git@bitbucket.org:<workspace>/<repository>.git HEAD
```

**预期输出：**`HEAD` 的一个 commit 引用。未经测试的示例。成功结果仅证明某个获准的 SSH 身份到达了指定仓库，不能证明使用的是已登记密钥，也不能证明有写入权限。为每个仓库单独配置密钥后再次测试。

有关私钥保管和 1Password SSH Agent 授权，请参阅[1Password CLI 和 SSH Agent：为 AI 代理保护 SSH 密钥](/articles/1password-cli-ssh-keys-mcp-agent-administration/)。

## 正确定义“Bitbucket CLI”

**Bitbucket CLI** 这一说法常把三种不同接口混为一谈。请分别看待。

- **Git CLI：**`git clone` 和 `git fetch` 通过 SSH 或 HTTPS 传输仓库数据。`git diff` 比较本地文件或修订版本。
- **REST 客户端：**`curl` 或经过审查的包装器调用 Bitbucket Cloud Representational State Transfer (REST) API。API 是用于请求数据或操作的程序接口。[Bitbucket Cloud REST API 参考](https://developer.atlassian.com/cloud/bitbucket/rest/)列出仓库、源代码、分支、pull request、流水线和状态资源。
- **Atlassian CLI：**`acli` 是 Atlassian 官方命令行工具。[简介](https://developer.atlassian.com/cloud/acli/guides/introduction/)介绍该产品，[命令参考](https://developer.atlassian.com/cloud/acli/reference/commands/)列出 `admin`、`jira`、`feedback` 和 `rovodev` 等功能。参考文档没有记录 Bitbucket Cloud 命令。

**Atlassian 官方 `acli` 命令参考没有记录 Bitbucket Cloud 命令。**不要臆造 `acli bitbucket clone` 之类的命令。Git 操作使用 Git，Bitbucket Cloud 数据使用 REST API。

### 可选的 Teamwork Graph CLI

**Atlassian 还发布了 Teamwork Graph CLI，简称 `twg`。**其[概览](https://developer.atlassian.com/cloud/twg-cli/)和[命令目录](https://developer.atlassian.com/platform/teamwork-graph/twg-cli/commands/commands-catalog/)记录了 Bitbucket 命令系列。设置命令为：

```bash
twg setup
```

设置命令会更改本地身份验证状态。若要选择配置 Bitbucket 令牌，请按照已安装版本的提示操作。CLI 中的 Bitbucket 令牌路径与 Atlassian OAuth 分开。命令语法应以已安装版本和当前命令目录为准。对会修改数据的命令，使用独立配置文件、受限令牌、经过审查的已安装技能，并要求人工批准。

**预期结果，未经测试：**隔离配置文件会收到 Bitbucket 身份验证设置。设置前记录配置文件原有状态。回滚时，按照已安装版本文档中的注销或移除配置流程删除已保存凭据。

如果第三方项目自称 Bitbucket CLI，请审计其源代码、发布流程、校验和、更新路径、身份验证流程、请求的范围、网络目标、日志处理和写入命令。熟悉的二进制名称不能证明厂商支持或权限安全。

## 让 1Password 管理 SSH 密钥

[1Password SSH Agent](https://www.1password.dev/ssh/agent)向 Git 和 SSH 客户端提供存储在 1Password 中的 SSH 密钥。客户端发起获准的签名请求。私钥保留在 1Password 应用内，获准的客户端使用密钥前，1Password 会请求授权。

[1Password CLI 参考](https://www.1password.dev/cli/reference)承担不同职责。使用 `op` 受控访问条目、API 令牌、服务帐户和自动化设置。SSH 签名使用 SSH Agent。不要仅为方便代理工作流而将私钥导出到临时文件。

使用只读命令检查本地 CLI 和 Agent 状态：

```bash
op --version
ssh-add -l
```

**预期输出：**1Password CLI 版本，以及活动 Agent 的一个或多个公钥指纹。未经测试的示例。若 `ssh-add -l` 输出为空，表示所选 Agent 套接字没有可用密钥。

创建新密钥时，可在 1Password 中创建 Ed25519 SSH Key 条目，或导入通过可信本地流程生成的密钥。标签应注明用途、范围和轮换日期。只将公钥添加到 Bitbucket Cloud。[Linux 仓库访问密钥指南](https://support.atlassian.com/bitbucket-cloud/docs/set-up-repository-access-keys-on-linux/)说明了仓库设置路径和只读限制。

## 先验证 Bitbucket 主机密钥

SSH 用户身份验证不能证明服务器身份。客户端必须先验证 Bitbucket Cloud 的主机密钥，再发送身份验证请求。Atlassian 的[SSH 和两步验证指南](https://support.atlassian.com/bitbucket-cloud/docs/configure-ssh-and-two-step-verification/)列出公开主机密钥，并提供获取 known-host 条目的官方端点。

获取公开主机密钥数据以供比较：

```bash
curl --fail --silent --show-error https://bitbucket.org/site/ssh
```

**预期输出：**`bitbucket.org` 的 OpenSSH `known_hosts` 行。未经测试的示例。将该行写入 `~/.ssh/known_hosts` 前，先将返回的密钥或指纹与独立可信副本进行比较。

获准条目存在后，启用严格主机检查：

```sshconfig
Host bitbucket.org
    StrictHostKeyChecking yes
    UserKnownHostsFile ~/.ssh/known_hosts
```

**代理运行期间不要接受已更改的主机密钥。**停止运行，核对 Bitbucket Cloud 当前的主机密钥记录，并检查本地 `known_hosts` 条目。自动接受会移除密钥安全边界。

## 每个仓库使用一个密钥

一台设备通常保存多个 Bitbucket 密钥。范围较大的 SSH Agent 会在一次连接中提供多个身份。若服务器或策略限制身份验证尝试次数，先前密钥失败后，正确密钥也可能被拒绝。

Atlassian 的[单设备多仓库访问密钥指南](https://support.atlassian.com/bitbucket-cloud/docs/managing-multiple-repository-access-keys-on-one-device/)在仓库 Git 配置文件中使用 `core.sshCommand`，并在全局 Git 配置中使用 `includeIf`。每个仓库使用一个密钥时也采用此模式。

基于文件的可移植示例：

```ini
# .gitconfig inside one local repository
[core]
    sshCommand = ssh -o IdentitiesOnly=yes -i ~/.ssh/<repository-automation-key>
```

```ini
# ~/.gitconfig
[includeIf "gitdir:~/src/<repository>/"]
    path = ~/src/<repository>/.gitconfig
```

上面的配置块是专用自动化身份的文件型私钥例外，不会配置 1Password SSH Agent。若要使用 1Password SSH Agent，请从[1Password 设置指南](https://www.1password.dev/ssh/get-started)获取适用于平台的 `IdentityAgent` 或 `SSH_AUTH_SOCK` 值并进行配置。某些 OpenSSH 配置使用 `.pub` 文件作为 Agent 身份选择器，使用前请确认平台支持。文件型配置需要对应私钥路径。切勿将 `.pub` 文件传给需要私钥材料的命令，也不要导出个人私钥。

本地克隆需要指定密钥时，使用明确的仓库配置。同一目录中有多个克隆且共享访问边界时，使用 `includeIf`。[多密钥指南](https://support.atlassian.com/bitbucket-cloud/docs/managing-multiple-repository-access-keys-on-one-device/)展示了 Bitbucket 工作流中的这两种设置。

通过 SSH 使用 Git 克隆：

```bash
git clone git@bitbucket.org:<workspace>/<repository>.git <local-directory>
```

**预期输出：**Git 创建 `<local-directory>` 并通过 `bitbucket.org` 获取仓库。未经测试的示例。仓库访问密钥仅允许 clone 和 pull。

## 使用 API 令牌进行受限 REST 读取

Git 传输使用 SSH。Git 传输之外的元数据或操作使用 REST API。[API 令牌权限指南](https://support.atlassian.com/bitbucket-cloud/docs/api-token-permissions/)列出 Read、Write、Admin 和 Delete 等仓库范围。Repository Read 对应 `read:repository:bitbucket`，不包含 pull request 访问权限。

若目标端点支持所需操作，读取自动化优先使用 Bitbucket 仓库或项目访问令牌。基于用户的 API 令牌会保留用户帐户更广的访问权限。只有任务记录明确指定更广边界时，才使用工作区访问令牌。选择令牌类型前，请查看[Bitbucket 访问令牌指南](https://support.atlassian.com/bitbucket-cloud/docs/access-tokens/)。

代理读取从 `read:repository:bitbucket` 开始。只有代理需要 pull request 数据时才添加 `read:pullrequest:bitbucket`。只有任务记录列出端点和结果时，才添加工作区或流水线范围。Write 和 Admin 范围须走单独审批流程。

每个 API 令牌只用于一个目的，设置到期日期并记录在轮换记录中，到期前更换令牌。Atlassian 的[API 令牌创建指南](https://support.atlassian.com/bitbucket-cloud/docs/create-an-api-token/)要求提供名称、到期日期、应用选择和范围。创建后令牌只显示一次。

将令牌保存在 1Password 或受管理的运行时机密中。不要把值放进远程 URL。仅通过环境变量向需要执行一次读取的进程传递 bearer 令牌：

```bash
op run --env-file=/path/to/agent.env -- \
sh -c 'curl --fail --silent --show-error \
  --request GET \
  --url "https://api.bitbucket.org/2.0/repositories/<workspace>/<repository>" \
  --header "Authorization: Bearer ${BITBUCKET_API_TOKEN}" \
  --header "Accept: application/json"'
```

将 `/path/to/agent.env` 放在仓库之外。在文件中保存类似 `BITBUCKET_API_TOKEN=op://synthetic-vault/synthetic-api-token/credential` 的引用。`op run` 会解析引用，并在子进程存续期间将值提供给 curl 子进程。这不能阻止子进程读取环境变量的值或将其写入日志。不要将占位符替换成真实令牌。

**预期输出：**所选仓库的 JSON 元数据。未经测试的示例。占位符不得变成提交文件或日志中的真实令牌。

对于较长时间的自动化，使用受支持的 CLI 或服务帐户流程，将机密注入进程环境。令牌有效期应与任务匹配。若任务提前结束或主机所有权变更，请撤销令牌。

## 为 MCP 保留小型读取面

审查新服务器时，使用[当前 MCP 规范](https://modelcontextprotocol.io/specification/2026-07-28)及其[授权规则](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization)。HTTP 服务器需要检查令牌受众，并明确处理 401 和 403 响应。

MCP 主机获取用户同意。客户端与一个服务器保持连接。服务器公开工具、资源或提示。审查其来源、传输方式、帐户和权限前，将每台服务器视为不受信任的代码。

下一段中的 2025-06-18 规范 URL 是历史版本。新审查应使用当前的 2026-07-28 规范。

[MCP 规范](https://modelcontextprotocol.io/specification/2025-06-18)定义 MCP 主机、客户端和服务器之间的通信。服务器通过协议公开工具、资源或提示。MCP 标准化连接格式。调用实际能访问什么，仍由主机、服务器实现、帐户、令牌范围和审批策略决定。

将 MCP 服务器用作 Git 与 Bitbucket Cloud REST API 之上的受限适配器。

保护适配器，防止令牌透传、服务器端请求伪造（SSRF）和混淆代理行为。SSRF 会让服务器向非预期目标发送请求。混淆代理是指服务器代表调用者使用更广泛的权限。还要防范恶意本地服务器、不安全的 OAuth 重定向和过大的源数据响应。固定允许的 Bitbucket 来源和仓库标识符。使用专用操作系统用户，在沙箱中运行本地服务器。从工具结果和日志中移除机密。

本节描述的是设计，不是经过测试的 MCP 配置。此处未指定客户端、服务器、传输方式、版本或测试样例。将代理连接到生产仓库前，应在独立测试配置文件中验证只读服务器。

只读工具示例：

| 工具 | 受限结果 |
|---|---|
| **`get_repository_metadata`** | 返回一个仓库的元数据 |
| **`read_source_file`** | 读取指定修订版本中的一个路径 |
| **`list_branches`** | 列出一个仓库的分支 |
| **`get_pull_request`** | 令牌具有 pull request 读取范围时，返回一个 pull request |
| **`get_build_status`** | 返回一个 commit 的状态数据 |

这些名称描述的是设计，不是 Atlassian 命令。禁止服务器接受任意 URL、任意 shell 命令、原始令牌、私钥导出请求或不受限制的仓库标识符。

在四个层面设置权限：

1. **Bitbucket Cloud：**Git 使用仓库或项目读取密钥，REST 读取使用范围最小的 API 令牌。
2. **1Password：**为任务使用一个保管库或服务帐户，不提供私钥导出路径。
3. **MCP 服务器：**设置只读工具允许列表、固定的 Bitbucket Cloud 端点、输入验证、超时限制和去除机密的日志。
4. **MCP 主机：**服务器和每项可写操作都须获得用户批准；默认配置文件中禁用写入工具。

*MCP 工具列表只能证明工具已被发现，不能证明授权、范围正确、输入处理安全或结果正确。*

## 安排代理工作流

明确工作流。每个阶段都为下一阶段提供证据。

| 阶段 | 代理操作 | 权限 | 人工关口 |
|---|---|---|---|
| **准备** | 读取配置、主机密钥记录、密钥标签、令牌范围和到期时间 | 本地读取 | 批准设置记录 |
| **检查** | 通过 SSH 使用 Git clone 或 fetch，并查询 REST 元数据 | 仓库读取和 API 读取 | 设置后无需批准 |
| **分析** | 通过获准工具读取文件、分支、pull request 和构建状态 | 只读 MCP 工具 | 范围内读取无需批准 |
| **准备更改** | 在本地工作区生成补丁、分支计划或 pull request 草稿 | 仅本地写入 | 审查 diff 和目标 |
| **批准写入** | 展示确切的远程操作、范围和回滚方案 | 尚未远程写入 | 人工批准 |
| **执行写入** | 推送分支、创建 pull request 或调用写入端点 | 短期写入身份 | 确认每项操作 |
| **验证** | 读取生成的 commit、pull request 或状态 | 恢复只读 | 确认预期结果 |

默认代理配置文件应在**分析**或**准备更改**后停止。单独的写入配置文件应使用不同的令牌或密钥、较短的有效期、固定目标和审批提示。仓库访问密钥无法执行写入步骤，因此形成了有用的技术边界。

## 回滚和移除

先移除访问权限，再清理本地配置：

1. 从对应的 Bitbucket 设置页移除仓库、项目或工作区访问密钥。
2. 从对应的 Bitbucket 安全页面撤销仓库、项目、工作区或用户 API 令牌。
3. 根据已安装 CLI 版本的[文档认证流程](https://developer.atlassian.com/platform/teamwork-graph/twg-cli/getting-started/how-authentication-works/)移除已保存的 Teamwork Graph 凭据。此前的凭据只保留在获准的机密管理器中。确认隔离配置文件不再列出测试凭据。
4. 测试结束后，移除仓库的 `.gitconfig` 文件和 `includeIf` 条目。保留无关的 Git 配置。
5. 只移除测试时添加且已验证的 Bitbucket 主机密钥行。保留其他获准的主机密钥。
6. 删除外部 `agent.env` 文件和临时输出。从主机配置中移除 MCP 服务器条目，然后重启主机。

记录每次移除、操作人员和时间。如果某个值出现在意外的日志、进程记录或转录中，请轮换密钥或令牌。

## 远程读取并更新本地引用

定期检查仓库时，使用简短的循环：

```bash
LOCAL_REPO="<local-directory>"
git -C "$LOCAL_REPO" fetch --no-tags
git -C "$LOCAL_REPO" status --short --branch
git -C "$LOCAL_REPO" log -1 --format='%H %ad %s' --date=iso-strict
```

`HEAD` 表示仓库当前检出的引用。成功结果证明某个获准的 SSH 身份到达指定仓库，但不能证明使用了哪个密钥，也不能证明存在 push 权限。

**预期输出：**fetch 结果、分支状态和一行 commit 信息。未经测试的示例。`fetch` 不会写入远程，但会更新本地引用和 `FETCH_HEAD`。此循环不会 push 或切换分支。

MCP 服务器应通过命名操作提供相同的读取边界。本地 shell 包装器或 MCP 工具应在发送请求前拒绝写入动词。记录工具名称、仓库占位符、修订版本、结果类别和耗时。除非任务明确需要某个文件，否则从日志中移除令牌、Cookie、私有路径和文件内容。

## 故障排除

### `Permission denied (publickey)`

检查活动 Agent 套接字、所选公钥、仓库访问密钥条目和 `IdentitiesOnly`。目标仓库或项目中必须存在仓库密钥。个人密钥需要帐户权限。工作区访问密钥具有不同的写入边界。

### 提供了错误的仓库密钥

使用 `core.sshCommand` 为每个仓库指定一个密钥，或将克隆放在由 `includeIf` 控制的目录中。使用 `ssh-add -l` 列出 Agent 密钥。如果有多个 1Password 密钥，请使用明确的身份选择器或 1Password SSH 书签。[1Password Agent 指南](https://www.1password.dev/ssh/agent)说明了密钥数量和书签的注意事项。

### SSH 报告主机密钥已更改

停止代理。不要一开始就删除 `known_hosts`。通过独立渠道将 Bitbucket Cloud 当前主机密钥记录与本地条目进行比较。只有比较通过后才移除或替换条目。

### API 返回 `401` 或 `403`

检查令牌是否过期、令牌类型、端点范围以及帐户或工作区边界。仓库读取范围不包含 pull request。写入端点需要写入范围和获准的写入配置文件。确定失败端点前不要扩大范围。

### API 返回仓库数据，但没有 pull request

为新令牌或轮换后的令牌添加最小的 pull request 读取范围。只读 MCP 服务器不要复用范围很广的用户令牌。

### MCP 服务器列出了工具，但调用失败

分别检查服务器注册、连接、工具发现、执行和结果验证。检查服务器日志时不要暴露令牌。验证端点和输入格式。确认连接正常后只重试一次。第二次调用仍失败时，将操作标记为未完成。

### 第三方 Bitbucket CLI 请求广泛访问权限

停止安装。将请求的访问权限与任务记录进行比较。审查源代码、发布签名或校验和、网络目标、机密存储和写入行为。Atlassian CLI 官方命令参考不能证明其支持第三方 Bitbucket 二进制文件。

## 后续步骤

创建简短的访问记录，注明仓库或项目范围、密钥标签、主机密钥验证日期、API 范围、令牌到期时间、1Password 所有者、MCP 工具允许列表、日志策略和写入审批人。

在转录中使用占位符，执行一次只读克隆、一次 REST 元数据读取和一次 MCP 工具读取。比较结果。访问记录和日志通过审查前，将代理配置文件保持为只读。

收到写入任务时，先准备本地 diff。说明目标分支、修改路径、请求的 API 方法、令牌范围和回滚步骤。只有在人工批准确切操作后，才使用单独的短期写入身份。
