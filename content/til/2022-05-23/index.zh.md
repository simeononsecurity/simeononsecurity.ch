---
title: "今天我学会了如何制作巧克力包装"
date: 2022-05-23
toc: true
draft: false
description: "今天，我学到了更多有关 Ansible 条件和变量管理的知识"
genre: ["自动化", "Windows 软件包管理", "软件包创建", "软件包管理", "基础设施即代码（IaC）", "Windows 软件部署", "软件包装", "视窗自动化", "软件包存储库", "视窗工具"]
tags: ["自动化", "Powershell", "巧克力包装管理器", "巧克力", "巧克力", "软件包创建", "包装自动化", "Nuspec", "内索", "Windows 软件包管理器", "IAC", "基础设施即代码", "视窗软件部署", "软件包装", "存储库管理", "套餐共享", "巧克力文件", "教程", "包装出版"]
---

**SimeonOnSecurity 今天了解到的有趣内容**

今天，SimeonOnSecurity 学习了为 Chocolatey 软件包管理器创建软件包的过程。Chocolatey 是 Windows 的软件包管理器，可以轻松安装、升级和管理应用程序和工具。通过创建软件包，SimeonOnSecurity 可以自动安装软件，并与社区中的其他人共享软件包。

SimeonOnSecurity 在 GitHub 上创建并更新了两个与创建 Chocolatey 软件包相关的软件仓库。第一个软件源 simeononsecurity/Chocolatey-Nethor 是 Nethor 的软件包。第二个软件源 simeononsecurity/chocolateypackages 是 SimeonOnSecurity 为各种应用程序和工具创建的软件包集合。

SimeonOnSecurity 使用 Nuspec 文件格式创建软件包，该格式提供了软件包及其内容的元数据。软件包创建过程还包括使用 Install-ChocolateyInstallPackage 和 Install-ChocolateyPackage 等函数来指定要安装的软件和任何必要的依赖关系。

SimeonOnSecurity 还查阅了一些学习资源，包括 Chocolatey 官方文档和 Top Bug Net 的教程，以便更深入地了解创建和发布 Chocolatey 软件包的过程。

总之，SimeonOnSecurity 通过今天的学习，全面了解了为 Chocolatey 软件包管理器创建软件包的过程，从而可以更轻松地自动安装软件并与社区中的其他人共享软件包。

## Repos Created/Updated：
- [simeononsecurity/Chocolatey-Nethor](https://github.com/simeononsecurity/Chocolatey-Nethor)
- [simeononsecurity/chocolateypackages](https://github.com/simeononsecurity/chocolateypackages)

## 学习资源：
- [Chocolatey - Create Packages](https://docs.chocolatey.org/en-us/create/create-packages#nuspec)
- [Chocolatey - Install-ChocolateyInstallPackage](https://docs.chocolatey.org/en-us/create/functions/install-chocolateyinstallpackage)
- [Chocolatey - Install-ChocolateyPackage](https://docs.chocolatey.org/en-us/create/functions/install-chocolateypackage)
- [Top Bug Net - Create and Publish Chocolatey Packages](https://www.topbug.net/blog/2012/07/02/a-simple-tutorial-create-and-publish-chocolatey-packages/)