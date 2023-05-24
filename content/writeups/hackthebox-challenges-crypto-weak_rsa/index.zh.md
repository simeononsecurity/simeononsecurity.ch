---
title: "HackTheBox - 挑战 - 加密 - 弱 RSA"
draft: false
description: "了解如何使用自动化 RSA 攻击工具 RsaCtfTool 轻松解决 HackTheBox 弱 RSA 加密挑战。"
tags: ["破解盒子", "挑战", "加密货币", "弱RSA", "RsaCtf工具", "HTB 弱RSA密码", "轻松挑战", "RSA密码", "flag.enc", "key.pub", "OpenSSL 包", "自动 RSA 攻击工具", "蟒蛇脚本", "RsaCtf工具", "蟒蛇3", "公钥", "解密文件", "标志示例"]
toc: true
cover: "/img/cover/A_cartoon_hacker_wearing_a_cape_and_a_mask_standing.png"
coverAlt: "一位戴着斗篷和面具的卡通黑客，站在带有 HTB 标志的金库门前，手持工具（如扳手或螺丝刀），背景为绿色，象征成功，上方对话泡泡中有旗帜他们的头。"
coverCaption: ""
---
 轻松应对 HTB 弱 RSA 密码挑战。基于 RSA 密码，这个简单的挑战需要使用自动 RSA 攻击工具，如 RsaCtfTool。通过一个简单的命令获取旗帜，并通过 HackTheBox 挑战扩展您的加密技能。

______

## 提供的文件：

**您将获得以下文件：**
- flag.enc
- key.pub

## 演练：

乍一看，您会认为可以使用公钥解密标志。
为此，我们可能会使用 OpenSSL 包来解密标志。
这次有点不同，您会发现 OpenSSL 包无法应对这一挑战。

我们将使用自动 RSA 攻击工具。一个常见的 python 脚本是 [RsaCtfTool](https://github.com/Ganapati/RsaCtfTool)

```bash
python3 RsaCtfTool.py --publickey ./key.pub --uncipherfile ./flag.enc 
```
  
简而言之，此工具可以自动为您轻松找到标志。

______

### 标志示例：
```
HTB{XXXXXX_XXXXXXX_XXXXXX}
```
