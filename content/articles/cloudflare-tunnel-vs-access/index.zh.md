---
title: "Cloudflare Tunnel 与 Access：两者都需要吗？"
date: 2026-09-11
lastmod: 2026-11-09
toc: true
draft: false
description: "了解 Cloudflare Tunnel 与 Access 的区别，为家庭仪表板选择保护方式，并避免在没有身份验证时公开私有应用。"
genre: ["网络安全", "自托管", "云安全"]
tags: ["Cloudflare Tunnel", "Cloudflare Access", "Cloudflare Tunnel 与 Access", "Cloudflare Zero Trust", "cloudflared", "自托管应用", "家庭实验室安全", "远程访问", "身份提供商", "访问策略", "应用身份验证", "公共主机名", "源站保护", "出站隧道", "服务令牌", "Service Auth", "MFA", "私有仪表板", "反向代理", "CGNAT"]
cover: "/img/cover/cloudflare-tunnel-vs-access.webp"
coverAlt: "家庭服务器通过透明通道连接到云网关，网关设有独立的身份检查点。"
coverCaption: ""
---

**Cloudflare Tunnel** 将应用连接到 Cloudflare。**Cloudflare Access** 控制谁能访问应用。通过公共主机名公开私有家庭仪表板时，两者都要使用。隧道正常运行本身不会增加身份检查。[Cloudflare 的应用发布指南](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/)解释了两者的区别。

## 要点

- **说明访问路径：** 区分连接器、源站和身份检查。
- **配置策略：** 只允许指定人员访问一个私有仪表板。
- **评估保护效果：** 测试允许、拒绝和替代访问路径。
- **设计访问方式：** 分别记录访客和自动化需求。

## 开始之前

**适用读者：** 希望保护浏览器仪表板的家庭服务器所有者。示例假设你在 Cloudflare 上有一个有效域名、本地 Web 应用正常运行，并且获准管理两者。**预计投入：** 配置好连接器后，策略练习需要 20 到 30 分钟。**难度：** 初级到中级。

**阅读顺序：** 先了解两种产品的作用，再跟踪一个请求，随后配置并检查一条简单策略。最后为自己的服务编写访问规范。

## 两种产品的作用

**源站**是运行应用的服务器。**`cloudflared`** 连接器从你的基础设施向 Cloudflare 发起连接，因此源站无需拥有可从公网路由的 IP 地址。之后，请求和响应都通过已建立的连接传输。[Cloudflare Tunnel 概览](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/)。

| 问题 | Tunnel | Access |
|---|---|---|
| **Cloudflare 如何连接到我的服务器？** | 建立连接 | 不替代源站连接 |
| **谁能访问？** | 本身不提供用户登录 | 按已配置的访问策略进行判断 |
| **需要配置什么？** | 连接器和应用路由 | 应用、身份提供商和策略 |
| **成功证明什么？** | 能通过该路由访问源站 | 请求符合已配置的策略 |

**身份提供商（IdP）**负责验证访客身份。**Access 策略**定义采取的操作和匹配条件。Allow 允许符合条件的用户访问。Bypass 会对符合条件的流量停用 Access 强制执行。[Access 策略参考](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)。

## 跟踪一次浏览器请求

对于 **`dashboard.example.com`**，请求的逻辑路径如下：

```text
Browser -> Cloudflare Access -> tunnel connection -> cloudflared -> dashboard
               |
               +-> identity provider when authentication is needed
```

**连接器从你的网络向外发起隧道连接。** 浏览器请求随后通过这条已建立的连接到达源站。出站连接承载入站应用请求，这正是 Tunnel 无需传统源站端口转发即可工作的主要原因。[Tunnel 连接模型](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/)。

**应用内部权限**需要另外决定。能够访问仪表板，并不会自动决定谁能修改设置或删除数据。如果应用设有查看者和管理员角色，应分别配置并测试。

例如，**家庭成员中的只读用户**需要查看备份状态，而你需要更改备份目标。选择身份前先写明这些要求。两人通过同一项 Access 检查，并不表示他们应自动获得相同的应用权限。

## 何时需要两者

**访问者决定保护方式。** 发布路由前，比较以下设置：

| 目标访问者 | 建议设置 | 使用前检查 |
|---|---|---|
| **任何公共网站读者** | 若需连接源站，则使用 Tunnel | 公开访问是有意安排的 |
| **你和少数家庭成员** | Tunnel 加 Access | 只允许指定身份 |
| **已有公共源站** | Access 并单独保护源站 | 直接访问源站不能绕过检查 |
| **定时脚本** | Tunnel 加 Service Auth 策略 | 客户端支持该身份验证方式 |

**没有 Tunnel 也能使用 Access**，前提是源站本来就可访问。也要保护通往服务器的其他路径。Cloudflare 建议在发布新的隧道路由时先创建 Access 应用。[自托管应用要求](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/)。

*对于通过公共主机名访问的私有家庭仪表板，建议从 Tunnel 加 Access 开始。*

## 配置仪表板策略

下面的**配置示例**适用于两名指定访客。请将示例地址替换为你控制的身份。添加公共隧道路由之前，先创建 Access 应用。

1. **应用：** 打开 Zero Trust → Access controls → Applications，创建一个使用公共主机名的自托管应用。
2. **主机名：** 输入专用的仪表板主机名。本例覆盖整个主机名，因此不限制路径。
3. **策略：** 创建一条名为 `Dashboard viewers` 的 Allow 策略。
4. **身份选择器：** 使用 Emails 添加 Include 规则，并将 `alice@example.com` 和 `bob@example.com` 替换成两名目标用户的地址。
5. **登录：** 选择访客使用的身份提供商，并谨慎设置会话时长。
6. **路由：** 保存应用，然后通过隧道将主机名连接到仪表板。

[官方应用配置流程](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/)介绍了这些设置。**预期结果：** 新访客必须先完成身份验证才能访问应用。依赖策略之前，请先完成下方的拒绝身份测试。

## 理解规则逻辑

**Include** 使用 OR 组合备选条件。**Require** 使用 AND 添加必需条件。**Exclude** 会排除匹配用户。增加另一项 Include 条件会扩大符合条件的群体。[Access 规则语义](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)。

| 策略片段 | 逻辑效果 |
|---|---|
| **Include Alice or Bob** | 两个指定身份中任意一个符合条件 |
| **Include Alice, Include a country** | 符合国家条件的人也会获准访问 |
| **Include Alice, Require a country** | Alice 还必须符合国家条件 |

**策略审查练习：** 你的要求只包含 Alice 和 Bob，但同事又添加一个国家作为 Include 条件。应拒绝这项更改，因为它会额外允许一类人访问。地理位置无法证明某人属于你的家庭。

## 验证定时脚本

**服务令牌**包含用于自动请求的 Client ID 和 Client Secret。配置应用策略，通过 **Service Auth** 接受该令牌。只创建令牌但没有对应策略，并不会授予应用访问权限。[Cloudflare 服务令牌](https://developers.cloudflare.com/cloudflare-one/access-controls/service-credentials/service-tokens/)。

对于备份脚本或监控检查，将**密钥**存放在工具的受保护凭据库中。为每个集成指定单独的令牌名称和合理的到期日。停用集成时轮换或撤销令牌。服务令牌文档介绍了这些生命周期操作。

**明确检查客户端兼容性。** 需要 API 响应的工具未必能处理交互式浏览器登录。选择策略前，确认工具支持请求标头或其他受支持的身份验证方式。

## 测试访问决策

将以下内容作为部署的**验收检查**：

| 检查 | 记录的证据 |
|---|---|
| **未登录访客** | Access 拦截来自全新浏览器会话的请求 |
| **允许的身份** | 登录后能够加载目标应用 |
| **拒绝的身份** | 未列出的账户无法访问应用 |
| **替代路径** | 旧 DNS 名称和源站端口不会造成意外访问 |
| **自动化** | 获批的客户端成功执行，不带凭据的请求失败 |

**出现登录页面**只能证明一条路径遇到了身份验证。还要测试拒绝场景和替代路径。这些是建议进行的检查，不是已部署示例的测试结果。

## 检查源站边界

**信任 Access 身份的源站**应验证已签名的应用令牌。Cloudflare 会在 **`Cf-Access-Jwt-Assertion`** 标头中转发令牌。标头存在本身不能证明令牌真实。[Cloudflare JWT 验证](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/validating-json/)。

**JSON Web Token（JWT）**包含已签名的声明。将 Access 身份集成到源站时，应使用文档指定的验证方法，包括预期的签发者和应用受众。解码令牌并读取其中的邮箱字段不足以完成验证。

**Issuer** 标明令牌的签发机构。**Audience** 标明令牌对应的应用。使用受支持的验证库检查令牌是否有效以及是否过期，避免自行实现签名检查。

**明确边界：** 确认验证发生的位置，以及哪些路由能够到达应用。即使主机名通过全部浏览器测试，旧端口转发或其他主机名也值得单独审查。

## 排查策略不匹配

| 现象 | 下一项检查 |
|---|---|
| **意外访客成功进入** | 检查 Include 条件、Bypass 策略和主机名覆盖范围 |
| **目标访客遭到拒绝** | 将登录身份与选择器中的准确值进行比较 |
| **脚本收到登录页面** | 检查其凭据和 Service Auth 策略 |
| **获准的查看者能修改设置** | 检查应用自身的角色分配 |

**会话行为**也会影响重测。Access 有多种会话时长，包括应用会话和全局会话。记录当前设置，并在测试新身份时使用新会话。[Access 会话管理](https://developers.cloudflare.com/cloudflare-one/access-controls/access-settings/session-management/)。

## 编写访问规范

添加另一项服务之前，先写一份**简短规范**：

```text
服务和主机名：
获准的人员身份：
所需应用角色：
自动化凭据及到期时间：
通往源站的其他路径：
Access 令牌的验证位置：
允许身份测试结果：
拒绝身份测试结果：
```

**完成标准：** 另一名管理员应能看懂谁能访问、每个客户端如何验证身份，以及哪些证据能证明拒绝有效。以后若添加监控集成，请更新凭据记录，并重新测试未经身份验证的请求。

## 下一步

按照站点的 [Cloudflare Tunnel 设置指南](/guides/how-to-setup-and-use-cloudflare-tunnels/)配置连接器，然后执行[官方 Access 应用配置流程](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/)。如果使用蜂窝网络，在选择远程访问路径前，阅读 [T-Mobile Home Internet 端口转发限制](/articles/t-mobile-home-internet-port-forwarding/)。
