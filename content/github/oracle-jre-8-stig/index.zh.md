---
title: "使用 Powershell 脚本自动化 Oracle JRE 8 STIG 合规性"
date: 2020-08-05
---


Oracle JRE STIG 不是那么简单，需要管理员研究 JAVA 文档并生成 java 配置文件，而大多数管理员习惯于使用组策略单独进行 STIG。

## 下载需要的文件

从中下载所需的文件[GitHub Repository](https://github.com/simeononsecurity/JAVA-STIG-Script)

## STIGS/SRGs 应用：
-[Oracle JRE 8 V1R5](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Oracle_JRE_8_Windows_V1R5_STIG.zip)

## 来源：
-[MyITGuy - deployment.properties](https://gist.github.com/MyITGuy/9628895)

-[cbu.edu - Java Technotes](http://stu.cbu.edu/java/docs/technotes/guides/deploy/properties.html)

## 如何运行脚本

**脚本可以从提取的 GitHub 下载中启动，如下所示：**

```
.\sos-install-java-config.ps1
```
