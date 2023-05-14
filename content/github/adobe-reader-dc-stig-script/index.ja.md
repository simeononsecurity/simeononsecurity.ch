---
title: "PowerShell スクリプトを使用して Adobe Reader Pro DC STIG を自動化する"
date: 2020-08-27
---

エンタープライズ環境では、環境のセキュリティを向上させるために、セキュリティ技術導入ガイド (STIG) への 100% の準拠を達成することが重要です。ただし、Adobe Reader Pro DC STIG を手動で適用するプロセスは時間がかかり、エラーが発生しやすくなります。幸いなことに、このプロセスを自動化する PowerShell スクリプトが利用可能であり、コンプライアンス プロセスを簡素化し、指定された STIG および SRG への完全なコンプライアンスを確保するのに役立ちます。

## Adobe Reader Pro DC STIG オートメーション スクリプトとは何ですか?

Adobe Reader Pro DC STIG オートメーション スクリプトは、Adobe Reader Pro DC Continous および Classic バージョンの STIG と SRG を適用し、環境のセキュリティ体制を向上させる PowerShell スクリプトです。

## STIG/SRG が適用されました

次の STIG/SRG がスクリプトによって適用されます。

-[Adobe Reader Pro DC Continous V1R2](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Adobe_Acrobat_Pro_DC_Classic_V1R3_STIG.zip)

-[Adobe Reader Pro DC Classic V1R3](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Adobe_Acrobat_Pro_DC_Continuous_V1R2_STIG.zip)

## Adobe Reader Pro DC STIG 自動化スクリプトを使用する利点

このスクリプトには、次のようないくつかの利点があります。

- **コンプライアンス プロセスの簡素化**: このスクリプトは、Adobe Reader Pro DC の STIG および SRG を適用するプロセスを自動化し、コンプライアンスを達成するために必要な時間と労力を削減します。

- **完全なコンプライアンスの確保**: スクリプトは、指定されたすべての STIG および SRG を適用し、環境が該当する規制に完全に準拠していることを確認します。

- **セキュリティ体制の改善**: STIG と SRG を適用することで、スクリプトは環境のセキュリティを向上させ、セキュリティ インシデントのリスクを軽減します。

## Adobe Reader Pro DC STIG 自動化スクリプトをダウンロードして実行する

Adobe Reader Pro DC STIG オートメーション スクリプトは、次の場所からダウンロードできます。[GitHub repository](https://github.com/simeononsecurity/Adobe-Reader-DC-STIG-Script) ダウンロードしたら、PowerShell で 1 つのコマンドを実行してスクリプトを実行できます。

```powershell
.\sos-adobe-stig.ps1
```

＃＃ 結論

結論として、Adobe Reader Pro DC STIG 自動化スクリプトを使用して Adobe Reader Pro DC STIG を適用するプロセスを自動化すると、コンプライアンス プロセスを簡素化し、完全なコンプライアンスを確保し、環境のセキュリティ体制を向上させることができます。上記の手順に従うことで、企業組織はスクリプトの利点を活用し、指定された STIG および SRG への 100% の準拠を達成できます。

____________