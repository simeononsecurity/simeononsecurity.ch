---
title: "ChromiumADMX：适用于 Chromium 浏览器的 ADMX 模板"
date: 2020-07-25
---


适合 Chromium 浏览器的 ADMX 模板

Chromium 作为一家公司未能发布可能与 Google Chrome 模板同时安装的 Chromium 浏览器的 ADMX 模板。
考虑到这一点，我们修改了 Google Chrome ADMX 模板以反映 Chromium 浏览器的注册表路径，并将其放在 GPO 的 Google ADMX 文件夹中。

**这些策略定义处于 Pre-Alpha 状态。它们应该仅用于测试目的**

## 下载需要的文件

**从下载所需的文件[GitHub Repository](https://github.com/simeononsecurity/ChromiumADMX)

## 注释

根据以下内容修改了 Google Chrome 策略定义：
[Chromium Policy Templates](https://www.chromium.org/administrators/policy-templates)

**注意：** 将“HKEY_LOCAL_MACHINE\Software\Policies\Google\Chrome”替换为“HKEY_LOCAL_MACHINE\Software\Policies\Chromium\”

**注意：** 不要同时安装 SOS 的 Chromium 和 Brave Browser ADMX 模板。

＃＃ 如何安装

1.) 将除 readme.md 之外的所有文件复制到“C:\Windows\PolicyDefinitions”和/或“\\\domain.tld\domain\Policies\PolicyDefinitions”

2.) 利润？




