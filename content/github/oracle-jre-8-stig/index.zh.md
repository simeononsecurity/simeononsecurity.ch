---
title: "使用 Powershell 脚本自动实现 Oracle JRE 8 STIG 合规性"
date: 2020-08-05
---


Oracle JRE STIG 就没那么简单了，它需要管理员研究 JAVA 文档并生成 java 配置文件，而大多数管理员习惯于只使用组策略进行 STIG。

## 下载所需文件

从 [GitHub Repository](https://github.com/simeononsecurity/JAVA-STIG-Script)

## STIGS/SRGs 已应用：
- [Oracle JRE 8 V1R5](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Oracle_JRE_8_Windows_V1R5_STIG.zip)

## 来源：
- [MyITGuy - deployment.properties](https://gist.github.com/MyITGuy/9628895)

- [cbu.edu - Java Technotes](http://stu.cbu.edu/java/docs/technotes/guides/deploy/properties.html)

## 如何运行脚本

**脚本可以从 GitHub 下载中提取，如下所示：**

```
.\sos-install-java-config.ps1
```
