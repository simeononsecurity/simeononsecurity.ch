---
title: "PowershellスクリプトによるOracle JRE 8 STIG準拠の自動化"
date: 2020-08-05
---


オラクルJREのSTIGはそれほど単純ではなく、多くの管理者はグループ・ポリシーを使ったSTIGだけに慣れているのに、管理者はJAVAのドキュメントを調べ、Javaの設定ファイルを生成する必要がある。

## 必要なファイルのダウンロード

必要なファイルを [GitHub Repository](https://github.com/simeononsecurity/JAVA-STIG-Script)

## STIGS/SRGを適用：
- [Oracle JRE 8 V1R5](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Oracle_JRE_8_Windows_V1R5_STIG.zip)

## ソースは？
- [MyITGuy - deployment.properties](https://gist.github.com/MyITGuy/9628895)

- [cbu.edu - Java Technotes](http://stu.cbu.edu/java/docs/technotes/guides/deploy/properties.html)

## スクリプトの実行方法

**スクリプトは、GitHubからダウンロードしたスクリプトを次のように実行します。

```
.\sos-install-java-config.ps1
```
