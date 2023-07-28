---
title: "PowerShellスクリプトでAdobe Reader Pro DCのSTIGを自動化する"
date: 2020-08-27
---

企業環境において、セキュリティ・テクニカル・インプリメンテーション・ガイド（STIGs）に100％準拠することは、環境のセキュリティを向上させるために極めて重要である。しかし、Adobe Reader Pro DCのSTIGsを手動で適用するプロセスは、時間がかかり、エラーが発生しやすい場合があります。幸いなことに、このプロセスを自動化するPowerShellスクリプトが用意されており、コンプライアンスプロセスを簡素化し、指定されたSTIGとSRGへの完全なコンプライアンスを確保するのに役立ちます。

## Adobe Reader Pro DC STIG自動化スクリプトとは？

Adobe Reader Pro DC STIG自動化スクリプトは、Adobe Reader Pro DC ContinousおよびClassicバージョンのSTIGおよびSRGを適用するPowerShellスクリプトであり、環境のセキュリティ体制を改善します。

## 適用されるSTIG/SRG

このスクリプトでは、以下の STIG/SRG が適用されます：

- [Adobe Reader Pro DC Continous V1R2](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Adobe_Acrobat_Pro_DC_Classic_V1R3_STIG.zip)

- [Adobe Reader Pro DC Classic V1R3](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Adobe_Acrobat_Pro_DC_Continuous_V1R2_STIG.zip)

## Adobe Reader Pro DC STIG自動化スクリプトのメリット

このスクリプトには、以下のような利点があります：

- コンプライアンスプロセスの簡素化**：このスクリプトは、Adobe Reader Pro DCのSTIGおよびSRGの適用プロセスを自動化し、コンプライアンス達成に必要な時間と労力を削減します。

- 完全なコンプライアンスの確保**：このスクリプトは、指定されたすべての STIG および SRG を適用し、環境が適用される規制に完全に準拠していることを保証します。

- セキュリティ態勢の改善**：STIG と SRG を適用することで、スクリプトは環境のセキュリティを向上させ、セキュリティ インシデントのリスクを低減します。

## Adobe Reader Pro DC STIG自動化スクリプトのダウンロードと実行

Adobe Reader Pro DC STIG自動化スクリプトは、次のサイトからダウンロードできます。 [GitHub repository](https://github.com/simeononsecurity/Adobe-Reader-DC-STIG-Script)ダウンロードしたスクリプトは、PowerShellのコマンド1つで実行できる：

```powershell
.\sos-adobe-stig.ps1
```

## 結論

結論として、Adobe Reader Pro DC STIG 自動化スクリプトを使用して Adobe Reader Pro DC STIG を適用するプロセスを自動化することで、コンプライアンスプロセスを簡素化し、完全なコンプライアンスを確保し、環境のセキュリティ態勢を改善することができます。上記で説明した手順に従うことで、企業組織はスクリプトの利点を活用し、指定されたSTIGおよびSRGに対する100%のコンプライアンスを達成することができます。

___________