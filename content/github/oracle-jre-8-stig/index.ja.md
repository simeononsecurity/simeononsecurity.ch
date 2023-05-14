---
title: "Powershell スクリプトを使用して Oracle JRE 8 STIG への準拠を自動化する"
date: 2020-08-05
---


Oracle JRE STIG はそれほど単純ではなく、ほとんどの管理者がグループ ポリシーのみを使用して STIG を実行することに慣れている場合、管理者は JAVA ドキュメントを調べて Java 構成ファイルを生成する必要があります。

## 必要なファイルをダウンロードします

から必要なファイルをダウンロードします。[GitHub Repository](https://github.com/simeononsecurity/JAVA-STIG-Script)

## STIGS/SRG が適用されました:
-[Oracle JRE 8 V1R5](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Oracle_JRE_8_Windows_V1R5_STIG.zip)

## 出典:
-[MyITGuy - deployment.properties](https://gist.github.com/MyITGuy/9628895)

-[cbu.edu - Java Technotes](http://stu.cbu.edu/java/docs/technotes/guides/deploy/properties.html)

## スクリプトの実行方法

**スクリプトは、次のように抽出された GitHub ダウンロードから起動できます:**

```
.\sos-install-java-config.ps1
```
