---
title: "HackTheBox - Invite Challenge (Windows/Linux)"
draft: false
toc: true
description: "了解如何生成邀请码并加入 HackTheBox 在线平台，以测试和提高您在 Windows 和 Linux 上的渗透测试和网络安全方面的技能。"
tags: ["破解盒子", "邀请挑战", "渗透测试", "网络安全", "视窗", "Linux", "在线平台", "HTTP POST", "邀请代码", "Base64编码", "电源外壳", "Linux 狂欢", "Base64解码", "邀请码生成", "编程", "Web开发", "技术", "信息安全", "资讯科技培训"]
cover: "/img/cover/A_cartoon_computer_screen_showing_the_HackTheBox_website.png"
coverAlt: "卡通电脑屏幕显示 HackTheBox 网站，金库门用钥匙打开，露出奖杯或奖章，城市景观背景采用 HackTheBox 徽标（蓝色和白色）的配色方案。"
coverCaption: ""
---
 在 Windows 或 Linux 上完成 HackTheBox 邀请挑战的分步说明。了解如何生成邀请码并加入在线平台以测试和提高您在渗透测试和网络安全方面的技能。文章提供了简单和高级的解决方案，使各个级别的用户都可以轻松完成挑战并获得平台访问权限。

______

## 什么是破解盒子？

HackTheBox 是一个在线平台，用于测试和提高您在渗透测试和网络安全方面的技能。

## 你如何加入 Hack the box？

要在 HackTheBox (HTB) 上创建帐户，您必须完成邀请挑战，或者自己闯关。别担心，尽管这并不难，本文将帮助您完成挑战。

首先，前往[HackTheBox Website](https://hackthebox.eu) 然后点击加入按钮。

您将看到一个明确要求输入邀请码的框。

您可以清楚地看到一个文本框，要求我们提供邀请码。

按键盘上的 ***“F12”*** 或 ***“Ctrl + Shift + I”*** 打开浏览器开发者工具。

在“元素”选项卡上，您会找到一个脚本 **[inviteapi.min.js](https://www.hackthebox.eu/js/inviteapi.min.js)

查看 javascript 和 makeInviteCode 函数，您会发现您需要发送 **HTTP POST** 到 **/api/invite/generate** 以获得邀请码。

您可以通过以下方式获取 Base64 编码的邀请码：

＃＃＃ 解决方案：

＃＃＃＃ 简单的：
- **Windows**：```powershell (Invoke-WebRequest -Method POST "https://www.hackthebox.eu//api/invite/generate" | ConvertFrom-JSON) ```
- **Linux**: ```bash curl -X POST "https://www.hackthebox.eu/api/invite/generate" ```

Which will generate the following content: ```json {"success":1,"data":{"code":"Tk9ULVRIRS1GTEFHLVlPVSdSRS1MT09LSU5HLUZPUg==","format":"encoded"},"0":200} ```

If you take the encoded invite code to [base64decode.org](https://www.base64decode.org/), you'll get your invite code!

#### Advanced (Instantly print out invite code):
 - **Windows**: ```powershell $base64api=((Invoke-WebRequest -Method POST "https://www.hackthebox.eu//api/invite/generate" | ConvertFrom-JSON).Data).Code ; [System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String($base64api)) ```
- **Linux**: ```bash curl -X POST "https://www.hackthebox.eu/api/invite/generate" | jq -r '.data.code' | base64 -d ```
 - **Note**: You'll need to install the [jq](https://stedolan.github.io/jq/download/) package.

______

### Invite Code Ex:
```XXXXX-XXXXX-XXXXX-XXXXX-XXXXX```


