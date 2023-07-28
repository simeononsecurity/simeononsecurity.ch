---
title: "ChromiumADMX：适合 Chromium 浏览器的 ADMX 模板"
date: 2020-07-25
---


适合 Chromium 浏览器的 ADMX 模板

作为一家公司，Chromium 未能发布可与 Google Chrome 模板同时安装的 Chromium 浏览器 ADMX 模板。
有鉴于此，我们修改了 Google Chrome 浏览器的 ADMX 模板，以反映 Chromium 浏览器的注册表路径，并将其放置在 GPO 中 Google ADMX 文件夹的 tandum 中。

**这些策略定义处于预开发阶段。它们只能用于测试目的**

## 下载所需文件

**下载所需文件 [GitHub Repository](https://github.com/simeononsecurity/ChromiumADMX)

## Notes

根据 Google Chrome 浏览器政策定义进行了修改：
[Chromium Policy Templates](https://www.chromium.org/administrators/policy-templates)

**注：** 将 "HKEY_LOCAL_MACHINE/Software/Policies/Google/Chrome "替换为 "HKEY_LOCAL_MACHINE/Software/Policies/Chromium/"

**注意：** 不要同时安装 SOS'es Chromium 和 Brave Browser ADMX 模板。

## 如何安装

1.)将除 readme.md 以外的所有文件复制到 "C:\Windows\PolicyDefinitions "和/或"\\domain.tld\domain\Policies\PolicyDefinitions "中

2.)利润？




