---
title: "使用 BraveADMX 控制 Brave 浏览器策略 - 修改后的 ADMX 模板"
date: 2020-07-25
---


作为一家公司，Brave 未能发布用于 brave 浏览器站点的 ADMX 模板，将纯注册表作为唯一受支持的选项。
由于 Brave 浏览器是基于 Chromium 构建的，它应该支持来自 Chromium 和 Google Chrome ADMX 模板的大部分（如果不是全部）相同的策略。
考虑到这一点，我们修改了 Google Chrome ADMX 模板以反映 Brave 浏览器的注册表路径。经过一些初步的故障排除和测试后，模板似乎可以正常工作。

**这些策略定义处于 Pre-Alpha 状态。它们应该仅用于测试目的**

## 下载所需的文件。

**从下载所需的文件[GitHub Repository](https://github.com/simeononsecurity/BraveADMX)

## 注释

根据以下内容修改了 Google Chrome 策略定义：
[Brave Group Policy](https://support.brave.com/hc/en-us/articles/360039248271-Group-Policy)

**注意：** 将“HKEY_LOCAL_MACHINE\Software\Policies\Google\Chrome”替换为“HKEY_LOCAL_MACHINE\Software\Policies\BraveSoftware\Brave”

**注意：** 不要同时安装 SOS 的 Chromium 和 Brave Browser ADMX 模板。

＃＃ 如何安装

1.) 将除 readme.md 之外的所有文件复制到“C:\Windows\PolicyDefinitions”和/或“\\\domain.tld\domain\Policies\PolicyDefinitions”

2.) 利润？