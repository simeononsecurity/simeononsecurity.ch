---
title: "HSTS 预加载 如何增强网站安全性：分步指南"
date: 2023-08-20
toc: true
draft: false
description: "了解如何通过在 Chrome 浏览器和火狐浏览器上预载 HSTS 设置来提高网站安全性和用户信任度。请按照我们的分步指南进行无缝实施。"
cover: "/img/cover/enhanced-website-security.png"
coverAlt: "这是一幅卡通风格的插图，一个网站被一把锁遮挡住，代表着更高的安全性和对网络威胁的防护。"
coverCaption: "加强网站防御，采用 HSTS 预加载。"
---

## **使用 HSTS 预加载增强网站安全性：分步指南**

HTTP 严格传输安全（HSTS）是一种**重要的安全机制，可确保网站执行 HTTPS 连接，以**保护用户免受潜在的安全威胁**。通过在 Chrome 浏览器和火狐浏览器上预载 HSTS 设置，您可以**增强网站安全性**并建立**用户信任**。在本综合指南中，我们将向您介绍成功预载 HSTS 设置的**基本步骤，并提供**有用的建议**以优化安全性。

______

### **了解 HSTS 预加载**

**HSTS 预加载**是将您的网站域名**提交到主要浏览器预加载列表的过程。一旦添加，这些浏览器将**自动为您的域和所有子域执行 HTTPS 连接。这可确保用户始终安全地访问您的网站，降低**中间人攻击**和未经授权窃听的风险。有关 HSTS 预加载的更多详情，请参阅官方的 [documentation](https://hstspreload.org/)

______

{{< inarticle-dark >}}

______

### **提交要求**

在提交您的域名进行 HSTS 预加载之前，请确保您的网站满足以下**基本要求**：

1.**有效证书**：您的网站必须提供**有效的 SSL 或 TLS 证书**，以启用**安全的 HTTPS 连接**。

2.**HTTP 到 HTTPS 重定向**：确保您的网站在 80 端口监听时，所有 **HTTP 请求都会重定向**到其 **HTTPS 对应端口。

3.所有子域的**HTTPS**：网站的所有子域必须**支持 HTTPS 连接**，才有资格进行 HSTS 预加载。

4.基域上的 **HSTS 标头**：在基域上为 HTTPS 请求加入**HSTS 标头**，设置如下：
   - `max-age`必须**至少 31536000 秒**（1 年）。
   - 时间 `includeSubDomains`指令必须指定，以包括所有子域。
   - 该 `preload`指令，以要求将其纳入预加载列表。

下面是一个有效的 HSTS 标头示例：

```http
Strict-Transport-Security: max-age=63072000; includeSubDomains; preload
```

______

### **如何预载 HSTS 设置**

如果您的网站已**完全使用 HTTPS**并符合上述要求，请按照以下**关键步骤**成功预载 HSTS 设置：

1.**检查子域**：确保您网站的所有**子域**都能通过 HTTPS 正常工作，为用户提供无缝浏览体验。

2.**逐步升级**：为了测试和修复任何潜在问题，请在 HTTPS 响应中添加**HSTS 标头**，并使用**低***。 `max-age`值**（如 300 秒）。逐渐增加 `max-age`分阶段值：
   - 5 分钟： `max-age=300; includeSubDomains`
   - 1 周 `max-age=604800; includeSubDomains`
   - 1 个月 `max-age=2592000; includeSubDomains`

3.**监测指标**：在每个阶段，**密切监测网站的指标**，包括流量和收入，以发现并解决任何问题，然后再进入下一阶段。

4.**将最大使用期限延长至 2 年**：一旦您**确信不再有任何问题**，设置 `max-age`为**2 年（63072000 秒）**，并加上 `preload`指令到 HSTS 标头：
```http
Strict-Transport-Security: max-age=63072000; includeSubDomains; preload
```

5.**提交网站**：实施 2 年 `max-age`设置，使用以下网站上提供的表格将您的网站**提交到 HSTS 预加载列表中 [hstspreload.org](https://hstspreload.org/)请注意，列入预加载列表可能需要几个月的时间才能通过 Chrome 浏览器更新到达用户。
______

### **选择加入 HSTS 预加载：增强网站运营商的能力**

支持 HSTS 预加载是一项**优秀的安全实践**，可增强网站保护。不过，这应该是网站运营商的**选择决定。如果您提供了**HTTPS配置建议**或提供了启用HSTS的选项，请**避免包含以下内容 `preload`指令**。这种方法可防止意外包含在预加载列表中，从而导致难以访问某些子域。

为确保顺利体验，请**告知网站操作员**预加载的**长期后果，并强调在为其域启用 HSTS 之前**满足所有要求的重要性。

______

### **从预载列表中删除：慎重决定**

列入预加载列表是一项**永久性决定**，不能轻易撤销。但是，如果您遇到**强烈的技术或成本相关原因**，导致无法为某些子域提供 HTTPS 支持，您可以选择通过 [removal form](https://hstspreload.org/removal/)

在做出这一重大决定之前，请确保您已仔细评估了相关影响。
______

{{< inarticle-dark >}}

______

### **更安全的浏览从 HSTS 预加载开始**

总之，在 Chrome 浏览器和 Firefox 浏览器上预载 HSTS 设置是为用户提供更安全的网络浏览体验的**积极步骤。通过**加强 HTTPS 连接**，您可以**保护敏感数据**，并在访客中建立**信任。按照上述**指南**，即可**成功预加载 HSTS 设置**，并享受**增强的网站安全性**。

______

### 参考资料

1. [Chromium - HTTP Strict Transport Security (HSTS)](https://www.chromium.org/hsts/)
2. [HSTS Preload Submission](https://hstspreload.org/)
3. [Mozilla Web Security Guidelines](https://infosec.mozilla.org/guidelines/web_security)
4. [Google Web Fundamentals - Security](https://developers.google.com/web/fundamentals/security/)
