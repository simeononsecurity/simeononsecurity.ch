---
title: "1Password SSH Agent 和 CLI：只读 AI 代理访问"
date: 2026-10-11
lastmod: 2026-10-28
toc: true
draft: false
description: "使用 1Password CLI、SSH Agent 和 MCP 设计只读 SSH 工作流。使用合成命令、窄权限，并在实时测试前进行人工审批。"
genre: ["系统管理", "云安全", "自动化"]
tags: ["1Password CLI", "SSH 密钥", "1Password SSH Agent", "MCP", "Model Context Protocol", "代理管理", "系统管理", "Bitbucket Cloud", "Git over SSH", "密钥引用", "服务账户", "最小权限", "公钥认证", "密钥管理", "命令行安全", "自动化安全"]
cover: "/img/cover/1password-cli-ssh-keys-mcp-agent-administration.webp"
coverAlt: "抽象示意图，展示代理使用密钥引用、SSH Agent 和 MCP 工具，而不显示私钥。"
coverCaption: ""
---

**命令行代理需要的是有用的访问权限，而非所有凭证的副本。** 本指南为 1Password CLI、1Password SSH 代理、Bitbucket Git 访问以及模型上下文协议（MCP）提供了一种有界的设计方案。第一个工作流使用合成名称、只读操作，并在 SSH 边界处进行人工审批。

<!--more-->

关键区别很简单。**交互式 SSH 通过 1Password SSH 代理实现基于同意的认证。无人值守自动化则需要独立的身份、狭窄的访问权限以及不同的密钥生命周期。** 不要将 MCP 连接视为运行上述任一工作流的权限。

## 关键要点

- **私钥保护：** 1Password SSH 代理执行 SSH 认证，同时保持私钥位于 1Password 应用内部。
- **公钥处理：** 仅将公钥发布到 Bitbucket 或远程账户。将私钥部分保留在 SSH 密钥条目中。
- **交互式同意：** 在 SSH 代理使用密钥之前，由人员批准客户端或终端会话。
- **无人值守隔离：** 计划任务需要专用的服务账户和狭窄的保险库范围。交互式 SSH 代理的批准无法满足此需求。
- **MCP 边界：** MCP 将代理连接到工具和资源。客户端、服务器、操作系统以及 1Password 策略仍然控制访问权限。

## 开始之前

**先决条件：** 安装 1Password 8 和 1Password CLI 2.20.0 或更高版本。通过受支持的 1Password 账户登录。使用 OpenSSH 客户端。创建一个测试用的 Bitbucket 仓库或其他非生产环境目标。保留一条第二管理路径以便回滚。

**时间：** 设计审查和合成演练需要 30 到 45 分钟。

**难度：** 中级。您需要具备基本的 Git、SSH、Shell 和访问控制知识。

本指南涵盖设计和规划。链接的 Bitbucket 文章涵盖 Bitbucket 特定的访问边界。本指南不测试实时账户、不创建真实密钥、不连接到真实主机，也不注册真实的 MCP 服务器。以下所有标识符均为合成数据。**仅在您自己受控的环境中替换占位符。**

**版本状态：** 对于此工作流，请使用 1Password 8 和 [1Password CLI 2.20.0 或更高版本](https://www.1password.dev/ssh/manage-keys)。[1Password CLI 1 已弃用](https://www.1password.dev/cli/upgrade/)。[1Password 7 将于 2027 年初停止服务](https://support.1password.com/add-account/)。SSH 密钥的生成、导入和共享需要 1Password 8。在测试前，请确认已安装的 Git、OpenSSH、MCP 主机和 MCP 服务器版本。以下示例未经过测试。

**保险库**是 1Password 中受保护的条目集合。**OpenSSH** 是许多操作系统使用的 SSH 客户端和服务器软件。**MCP**（即模型上下文协议）将智能体连接到经过批准的工具或资源。

## 为何保持私钥不可读

SSH 密钥对包含公钥和私钥。远程 Git 服务或服务器存储公钥。客户端在身份验证过程中证明拥有私钥。私钥无需传输到远程服务。

[1Password SSH Agent](https://www.1password.dev/ssh/agent) 扩展了这一模型。其文档指出，SSH 和 Git 客户端通过该代理进行身份验证，而私钥保留在 1Password 应用中。客户端接收的是签名结果，而非私钥文件。

这一边界减少了多种暴露路径：

- **源代码控制：** 私钥不会进入代码仓库或拉取请求。
- **Shell 历史记录：** 私钥值不会出现在命令参数中。
- **临时文件：** 脚本无需将私钥写入 `~/.ssh/`。
- **代理上下文：** 大型语言模型（LLM）无需私钥文本即可请求 SSH 操作。
- **意外重用：** 任务结束后，复制的密钥不会残留在旧的工作区中。

该边界并不能使 SSH 变得无害。拥有使用代理套接字权限的进程可能会以已批准密钥的身份执行操作。主机密钥验证、远程账户限制、仓库权限、命令策略和进程隔离仍然至关重要。

*私钥边界保护密钥材料。该边界并不批准远程命令，也不证明目标主机是可信的。*

## 交互式 SSH 同意

为代理密钥配置专用的保险库。使用 SSH Agent 配置文件选择最小的密钥集和特定主机的密钥。不要向自动化进程暴露来自每个内置保险库的所有合格密钥。

[1Password SSH Agent 安全模型](https://www.1password.dev/ssh/agent/security) 将批准与特定密钥及请求进程绑定。提示会识别该进程和密钥。随后，用户通过配置的身份验证方法批准该请求。

1Password 文档记录了多种批准范围。按密钥和按应用程序的批准是默认设置。终端会话范围将批准限定在特定的标签页或会话中。按请求的批准会对每个请求再次询问。存在一种所有进程批准选项，但该选项会授予当前操作系统用户下的所有进程在该会话中的访问权限。

**使用适合任务的最窄审批范围。** 系统管理代理应在专用终端或沙箱中运行。如果单个终端会话就足够了，就不要批准所有进程。

审批会话并非永久授权。1Password 会记录授权，直至配置的期限结束，或应用锁定或退出。当应用锁定时，代理不会保留私钥以供后续使用。当启用了受支持的设置时，即使 1Password 已关闭，SSH Agent 进程仍会在后台继续运行，但新的签名请求需要 1Password 处于解锁状态。

[1Password SSH 设置指南](https://www.1password.dev/ssh/get-started) 展示了通用流程：生成或导入密钥、发布公钥、启用 SSH Agent、配置 SSH 客户端、运行 SSH 或 Git 命令，并批准请求。确切的套接字路径因操作系统而异。请使用当前平台的说明，而不是从另一台机器复制路径。

在成功处理新的签名请求之前，必须解锁 1Password 应用。即使应用已关闭，代理进程也可能继续在后台运行。锁定的应用不会释放私钥材料用于签名。

## 公钥与 Bitbucket

[1Password 密钥管理指南](https://www.1password.dev/ssh/manage-keys) 记录了 SSH 密钥项、密钥生成、密钥导入、公钥、指纹和私钥。CLI 示例使用 `op item create --category ssh` 来创建 SSH 密钥项。在此示例中，1Password CLI 默认生成 Ed25519 密钥，并在其输出中隐藏私钥。

Bitbucket Cloud 使用标准的 Git 和 OpenSSH 命令行工作流。其[命令行指南](https://support.atlassian.com/bitbucket-cloud/docs/find-the-command-line/) 描述了从本地仓库执行的 Git 操作。其[SSH 配置指南](https://support.atlassian.com/bitbucket-cloud/docs/configure-ssh-and-two-step-verification) 列出了 SSH 远程形式和支持的公钥格式。

**将 Bitbucket 视为公钥消费者。** 通过已批准的 Bitbucket 账户或仓库设置注册公钥或指纹。将私钥保留在 1Password 中。Git 客户端请求 SSH Agent 进行签名。客户端不读取私钥文件。

有关 Bitbucket 访问密钥范围、注册路径和只读 Git 测试，请参阅 [Bitbucket Cloud SSH 密钥和 Git CLI：AI 代理的只读访问](/articles/bitbucket-cloud-ssh-keys-git-cli-mcp-agent-automation/)。

Bitbucket 文档将此称为 Git CLI 工作流。本文不假设存在单独的 Bitbucket MCP 服务器或名为 Bitbucket CLI 的产品。Bitbucket 特定的 CLI 需要其自身的最新文档及其自身的权限审查。

## 代理与 MCP 边界

在审查新服务器时，请使用当前的 [MCP 规范](https://modelcontextprotocol.io/specification/2026-07-28)。

以下背景段落中提到的 2025-06-18 规范 URL 是历史版本。对于新的审查，请使用 2026-07-28 规范。

[MCP](https://modelcontextprotocol.io/specification/2025-06-18) 标准化了 LLM 应用、客户端连接器与服务器之间的连接。服务器提供工具、资源或提示词。规范还规定，主机在暴露数据或调用工具之前必须获得用户同意。

**MCP 本身不授予权限。** MCP 工具仍在服务器进程、操作系统用户、网络路径、云账户以及已配置凭据的权限范围内运行。工具描述并非授权策略。

[1Password AI 安全文档](https://www.1password.dev/security-for-ai) 描述了 Environments MCP Server 和安全的 MCP 配置模式。同一页面还描述了从 1Password 运行时加载 MCP 配置值。这些页面并未定义通用的 1Password SSH 密钥 MCP 产品，也未定义适用于所有代理客户端的通用 SSH 工作流程。

将 MCP 用作狭窄的控制界面：

- **读取工具：** 检查服务状态、仓库元数据或已批准的日志。
- **计划工具：** 准备命令或变更记录，但不执行该命令。
- **审批工具：** 在远程写入之前请求人工决策。
- **写入工具：** 在目标、命令、范围和回滚计划明确之前，保持禁用状态。

代理应接收引用、元数据和操作结果。**代理不应接收私钥文本、整个保险库的项目转储或不受限制的 shell。**

## 安全的首个策略

在启用代理之前，先制定书面策略。将策略保存在靠近 MCP 配置的位置，但不要在该文件中存放凭据。

```yaml
agent_policy:
  purpose: "Read-only repository and system inspection"
  identities:
    interactive_ssh: "1Password SSH Agent with per-terminal consent"
    unattended_jobs: "Dedicated service account with one narrow vault"
  allowed:
    - "Read repository metadata through Git"
    - "Read approved service status and logs"
    - "Run one synthetic SSH connectivity check"
  approval_required:
    - "Any remote write"
    - "Any package, firewall, clock, or service change"
    - "Any new host-key acceptance"
    - "Any private-key export"
  denied:
    - "Read or print private-key fields"
    - "List every vault or every item"
    - "Write tokens or secrets to shell profiles"
    - "Run arbitrary commands from tool output"
  rollback:
    - "Revoke the service account"
    - "Remove the public key from the target"
    - "Disable the MCP server entry"
    - "Lock 1Password and end the agent session"
```

此策略仅为示例，并非 1Password 配置格式。请将实际策略存储在你的代理客户端所使用的控制平面中。在启用每个工具之前，根据策略审查每个工具。

## 服务账户与密钥引用

**服务账户**为自动化进程提供独立的身份。[1Password CLI 脚本指南](https://www.1password.dev/cli/secrets-scripts) 建议使用服务账户以实现对选定保险库的最小权限访问。这将无人值守的任务与个人的 SSO、MFA、保险库清单及日常账户分离开来。

**秘密引用**用于在不将值置于源代码中的情况下指定该值。[1Password CLI 参考](https://www.1password.dev/cli/reference)使用形式 `op://vault/item/field`。仅当周围进程仍具有狭窄访问权限时，存储引用才是安全的。引用不会绕过策略。

当一条命令需要一个值时，使用 `op read`。当子进程需要一组受控的运行时值时，使用 `op run`。当需要在已批准的保险库中存在一个新的 SSH Key 项目时，使用 `op item create`。

不要将运行时注入与私钥保护混淆。作为环境变量传递的 API 令牌对子进程仍然是可见的。通过环境变量传递私钥更糟糕，因为该值会将暴露范围扩展到进程检查、崩溃报告、调试输出、Shell 跟踪以及意外日志记录。

**优先在源代码中使用引用，并在尽可能小的进程中使用运行时值。** 保持进程短生命周期。禁用 Shell 跟踪。不要打印环境变量。在运行失败后删除临时文件。

## 安全初始工作流

以下序列将公钥注册、交互式 SSH、MCP 发现和无人值守设计分离开来。

### 1. 定义目标

写下目标类别、远程账户、预期的仓库或命令、主机密钥来源、审批负责人以及回滚操作。在首次练习中使用合成记录。

```text
target_class: test-repository
remote_account: git
operation: read-only connectivity check
host_key_source: approved administrator record
approval_owner: named operator
rollback: remove public key and revoke test identity
```

**预期结果，未测试：** 该记录标识一个目标和一个操作。该记录不包含主机名、IP 地址、令牌、私钥或个人数据。

### 2. 创建或选择 SSH Key 项目

官方 [1Password SSH 密钥指南](https://www.1password.dev/ssh/manage-keys)记录了 CLI 创建模式。下面的命令使用合成标题和命名的测试保险库。

```bash
op item create --category ssh --ssh-generate-key=ed25519 --vault "synthetic-test-vault" --title "synthetic-agent-admin-key"
```

**预期输出，未测试：** 1Password 在命名的测试保险库中创建一个 SSH Key 项目，并在终端输出中隐藏私钥。该命令会更改 1Password 状态。确切的人类可读输出取决于 CLI 版本和登录状态。

在测试记录中捕获返回的项目标识符，但不要复制私钥字段。仅在确认项目架构后，才使用标识符或确切的项标题进行后续特定字段的读取。

不要将此输出重定向到共享日志。当本地过程支持安全的结构化输出时，仅捕获项目标识符、公钥指纹和审批记录。

### 3. 处理公钥

在 1Password 中打开 SSH Key 条目，并使用其“复制公钥”操作。只有在确认您自己账户中的公钥字段标签后，才使用特定于字段的引用。不要转储完整的条目。

```bash
PUBLIC_KEY_REF="op://synthetic-test-vault/synthetic-agent-admin-key/synthetic-public-key-field"
op read "$PUBLIC_KEY_REF"
```

**预期输出，未经测试：** 一行合成的 OpenSSH 公钥，或来自已确认字段的公钥值。上述占位符字段名称并不保证与您条目的字段标签一致。

在批准的 Bitbucket 账户、Bitbucket 仓库或远程账户中注册公钥。切勿将匹配的私钥粘贴到 Bitbucket 中。[Bitbucket SSH 指南](https://support.atlassian.com/bitbucket-cloud/docs/configure-ssh-and-two-step-verification) 还建议在首次连接前记录 Bitbucket 主机密钥。

对于 Bitbucket，获取已发布的主机密钥记录，并在向 `~/.ssh/known_hosts` 添加一行之前，将该记录与独立的受信任副本进行比较。比较通过后，使用严格的主机检查。在代理运行期间，不要接受已更改的主机密钥。

### 4. 启用交互式 SSH

在桌面应用中开启 1Password SSH Agent。根据平台特定的 `IdentityAgent` 或 `SSH_AUTH_SOCK` 值配置 OpenSSH，这些值来自[官方设置指南](https://www.1password.dev/ssh/get-started)。将首次测试限制在一个仓库或一个非生产环境中。

在 macOS 或 Linux 上，从平台设置指南中设置套接字，并运行 `ssh-add -l`。在 Windows 上，使用受支持的命名管道配置，并通过 1Password SSH Agent 界面或文档化的 Windows SSH 测试来验证可用的密钥。不要将 `ssh-add -l` 作为跨平台验证命令呈现。

仅在 macOS 或 Linux 上：

```bash
ssh-add -l
git ls-remote "<repository-ssh-url>" HEAD
```

**预期输出，未经测试：** 在 macOS 或 Linux 上，`ssh-add -l` 列出活动代理的指纹。在 Windows 上，使用文档化的命名管道测试或 1Password SSH Agent 界面。成功的 Git 读取操作将返回提交引用。上述仓库占位符需要在受控测试中进行替换。

该命令使用仓库占位符。仅在受控测试中替换占位符。**不要批准您未预期的目标或进程的提示。**

### 5. 在 SSH 路径正常工作后添加 MCP

首先在没有 MCP 的情况下验证 SSH 客户端和目标。然后添加一个只读 MCP 服务器或本地连接器。为代理提供诸如 `read_status` 或 `prepare_command` 之类的工具。不要从通用 shell 工具开始。

MCP 配置应通过客户端支持的环境机制引用运行时值。[1Password AI 安全指南](https://www.1password.dev/security-for-ai)描述了将明文 MCP 配置令牌替换为从 1Password 加载的环境变量。**在配置中保留引用或变量名。将解析后的值排除在代理转录之外。**

本节描述的是一种设计，而非经过测试的 MCP 配置。此处未固定任何客户端、服务器、传输方式、版本或测试夹具。在将代理连接到生产系统之前，请在单独的测试配置文件中验证一个只读服务器。

### 6. 记录结果

记录目标类别、工具名称、审批决定、公钥指纹、命令结果以及清理结果。省略机密值。将每个输出标记为“已观察”或“预期”。

**预期结果，未测试：** 代理读取状态，提出一个有界命令，针对 SSH 请求获得明确批准，完成只读操作，并生成不包含私钥文本的记录。

## 合成命令序列

以下序列展示了顺序，但不使用真实基础设施。这些命令仅为示例。它们在文章准备期间未被执行。

```bash
op --version
op item create --category ssh --ssh-generate-key=ed25519 --vault "synthetic-test-vault" --title "synthetic-agent-admin-key"
op read "op://synthetic-test-vault/synthetic-agent-admin-key/synthetic-public-key-field"
# macOS or Linux only
ssh-add -l
git ls-remote "<repository-ssh-url>" HEAD
```

**预期输出，未测试：**

```text
2.x.y
SSH Key item created. Private key: redacted
ssh-ed25519 AAAA<synthetic-public-key> synthetic-key-label
256 SHA256:<synthetic-fingerprint> synthetic-agent-admin-key (ED25519)
<synthetic-commit-id>        HEAD
```

输出块仅为示意。该块不代表针对 1Password 账户、Bitbucket、Git 提供商或远程主机的运行。生产记录应仅存储已批准的元数据以及成功或失败状态。

## 交互式与无人值守访问

| 访问模式 | 身份 | 私钥路径 | 审批模型 |
|---|---|---|---|
| **交互式 SSH** | 通过 1Password SSH Agent 的人类账户 | 私钥保留在 1Password 应用中 | 人类批准进程、终端会话或请求 |
| **计划读取** | 专用服务账户 | `op run` 提供狭窄的运行时值 | 作业策略和服务账户范围 |
| **计划 SSH** | 专用自动化身份 | 密钥导出仍为最后手段的设计 | 作业隔离、短生命周期、主机限制和轮换 |
| **代理写入** | 人类或特定任务身份 | 取决于已批准的集成 | 在每个定义好的更改之前进行人类批准 |

*不要围绕交互式 SSH Agent 提示来安排工作流。请使用单独的自动化设计，或保持该步骤由人类操作。*

对于无人值守任务，请创建一个仅能访问单个保险库或一组少量条目的服务账户。为任务赋予单一用途。使用专用的仓库或服务器账户。添加主机密钥验证。设置执行超时。记录操作元数据，但不记录机密信息。测试完成后轮换或撤销该身份。

如果无人值守任务确实需要 SSH 私钥，请使用专用的自动化密钥，配合权限范围狭窄的远程账户，并记录明确的截止日期。使用 `op read` 获取私钥仍然会将密钥材料导出到进程边界之外。与 1Password SSH Agent 相比，这种设计具有更大的影响范围。当目标系统支持时，优先使用平台身份、部署服务或其他工作负载身份。

## 为什么明文环境变量会增加风险

环境变量可以将机密信息从源文件中移除，但并不能使机密信息不可见。子进程会读取其环境变量。进程检查、崩溃处理程序、调试输出、Shell 跟踪以及复制的命令记录都可能导致值泄露。

1Password 将 `op run` 记录为一种在运行时将引用加载到子进程中的方法。对于进程真正需要的值，请使用 `op run`。保持子进程生命周期短暂，并限制其命令。当 SSH Agent 可以消除导出需求时，不要通过 `SSH_PRIVATE_KEY`、`KEY` 或类似变量传递私钥。

更安全的顺序是：

1. **使用 SSH Agent** 进行交互式 SSH。
2. **使用公钥注册** 用于 Bitbucket 或远程账户。
3. **使用 `op run`** 用于权限范围狭窄的无人值守子进程。
4. **使用 `op read`** 用于单个值，当子进程不需要完整的环境变量时。
5. **导出私钥** 仅在具备书面例外批准、狭窄范围、清理计划和轮换计划之后进行。

## 决策表

| 需求 | 首选路径 | 停止或重新设计的原因 |
|---|---|---|
| 人类通过 SSH 运行 Git | 1Password SSH Agent | 如果提示中出现了意外的进程或密钥，则停止 |
| 注册仓库密钥 | 读取或自动填充公钥 | 切勿将私钥复制到仓库服务中 |
| Agent 读取服务状态 | 具有操作系统级作用域的只读 MCP 工具 | 如果该工具暴露了不受限制的 shell，则停止 |
| Agent 提议远程更改 | 先使用规划工具，然后由人类批准 | 如果目标、命令或回滚方案不明确，则停止 |
| 任务读取一个 API 令牌 | 服务账户加上 `op read` 或 `op run` | 如果令牌进入源代码、日志或全局配置文件，则停止 |
| 任务需要 SSH 访问 | 工作负载身份或专用自动化密钥 | 如果任务需要个人密钥或广泛账户权限，则停止 |
| MCP 配置需要令牌 | 由受支持的客户端加载的运行时引用 | 如果明文令牌被提交到配置中，则停止 |

## 故障处理

**意外的 SSH 同意提示：** 拒绝该提示。检查进程名称、终端会话、密钥指纹、仓库目标以及主机密钥。在重试之前，审查 SSH 客户端配置。

**没有 SSH Agent 套接字：** 确认 1Password 桌面应用已通过受支持的方法安装，SSH Agent 已启用，并且客户端使用了特定于平台的套接字。[官方 SSH Agent 页面](https://www.1password.dev/ssh/agent) 列出了操作系统要求和套接字设置链接。

**公钥身份验证失败：** 检查所选公钥、远程账户、仓库权限、主机密钥以及 SSH 配置。使用公钥指纹进行比较。不要通过导出无关的私钥来解决此错误。

**`op read` 拒绝访问：** 检查服务账户保险库作用域、项标识符、字段引用、登录状态以及项状态。将引用减少到一个已批准的项。不要将扩大保险库授权作为第一响应措施。

**`op run` 暴露了值：** 停止任务。仅保留最少的事件记录。根据您的保留程序删除复制的日志和临时文件。轮换受影响的密钥或秘密。审查 shell 跟踪、进程检查、崩溃报告以及 MCP 转录记录的保留情况。

**MCP 工具行为异常：** 将工具输出视为不可信数据。在执行输出中建议的命令之前停止操作。检查服务器源代码、配置、权限和传输层。MCP 主机必须获得用户同意。规范还为实施者提供了关于同意和访问控制的指导，但该协议不能替代您的审查。

## 回滚与移除

回滚始于访问权限的移除，而非文件删除。

1. **停止代理或计划任务。** 禁用 MCP 服务器条目或断开客户端连接。
2. **锁定 1Password。** 结束交互式 SSH 授权会话。
3. **移除公钥。** 从 Bitbucket、仓库或远程账户中删除测试密钥。
4. **撤销服务账户。** 移除其保险库访问权限并使令牌失效。
5. **删除测试 SSH Key 项目**，在确认没有已批准的工作流使用该条目后执行。
6. **移除临时配置。** 删除测试引用、本地套接字覆盖和生成的日志。
7. **审查证据。** 确认回滚记录中不包含私钥、令牌或环境转储。

*删除本地文件不会撤销公钥、服务账户、缓存令牌或远程授权。必须在源头移除每项授权。*

## 故障排除

### 代理在每个命令中都请求密钥

检查所选的授权范围。按请求审批更为严格。终端或应用程序会话可能已结束。1Password 在锁定或退出事件后也会再次请求。

### 代理在其转录中看到私钥

停止工作流并轮换密钥。检查 MCP 服务器响应、Shell 命令、调试日志和工具封装器。对于交互式任务，用 SSH Agent 的使用替代私钥读取。对于任务，用专用身份和记录的例外情况替代个人密钥。

### 密钥列表包含过多身份

1Password SSH Agent 会暴露其配置保险库中符合条件的密钥。使用范围限定的代理配置或特定主机的 SSH 配置。[代理文档](https://www.1password.dev/ssh/agent) 还提到了 OpenSSH 服务器的六密钥限制。

### 手动执行命令成功但在任务中失败

比较身份、保险库范围、环境、主机密钥数据、工作目录和审批假设。交互式 1Password 会话包含人工同意。计划任务则不包含。将任务设计为独立的访问模式。

### MCP 服务器已连接但任务失败

连接并不证明已获得授权。请分步骤检查工具发现、服务器凭据、客户端同意、操作系统权限、网络访问以及目标端权限。首次测试请保持只读。

## 后续步骤

对于新的审批，请使用当前 2026-07-28 版本的 MCP 规范。本文中任何 2025-06-18 版本的规范链接均为历史背景信息。

从一个合成仓库和一个只读 MCP 工具开始。在受控环境产生证据之前，将每个预期结果记录为“未测试”。然后，使用非生产目标、指定操作员、已验证的主机密钥以及书面回滚记录，重复该工作流程。

阅读 [1Password CLI 参考](https://www.1password.dev/cli/reference) 以获取当前命令标志。在创建服务账户自动化之前，阅读 [将密钥加载到脚本中](https://www.1password.dev/cli/secrets-scripts)。在批准来自新服务器的工具之前，阅读 [MCP 规范](https://modelcontextprotocol.io/specification/2026-07-28)。

**保持交互式 SSH 需经人工批准。将无人值守访问与交互式访问分开。只要目标支持基于代理的身份验证，就始终保持私钥不可读。**
