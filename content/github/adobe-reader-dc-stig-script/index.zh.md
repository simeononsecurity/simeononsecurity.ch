---
title: "使用 PowerShell 脚本自动化 Adobe Reader Pro DC STIGs"
date: 2020-08-27
---

在企业环境中，100% 遵守《安全技术实施指南》（STIG）对于提高环境的安全性至关重要。然而，手动应用 Adobe Reader Pro DC STIG 的过程既耗时又容易出错。幸运的是，有一个 PowerShell 脚本可以自动完成这一过程，简化了合规过程，并有助于确保完全符合指定的 STIG 和 SRG。

## 什么是 Adobe Reader Pro DC STIG 自动化脚本？

Adobe Reader Pro DC STIG Automation Script 是一个 PowerShell 脚本，用于为 Adobe Reader Pro DC Continous 和 Classic 版本应用 STIG 和 SRG，从而改善环境的安全态势。

## 应用的 STIGs/SRGs

脚本应用了以下 STIG/SRG：

- [Adobe Reader Pro DC Continous V1R2](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Adobe_Acrobat_Pro_DC_Classic_V1R3_STIG.zip)

- [Adobe Reader Pro DC Classic V1R3](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Adobe_Acrobat_Pro_DC_Continuous_V1R2_STIG.zip)

## 使用 Adobe Reader Pro DC STIG 自动化脚本的好处

该脚本具有多种优势，包括

- 简化合规流程**：该脚本可自动完成为 Adobe Reader Pro DC 应用 STIG 和 SRG 的过程，从而减少实现合规所需的时间和精力。

- 确保完全合规**：该脚本应用所有指定的 STIG 和 SRG，有助于确保环境完全符合适用法规。

- 改善安全态势**：通过应用 STIG 和 SRG，脚本有助于提高环境的安全性，降低安全事故的风险。

## 下载并运行 Adobe Reader Pro DC STIG 自动化脚本

Adobe Reader Pro DC STIG 自动化脚本可从以下网站下载 [GitHub repository](https://github.com/simeononsecurity/Adobe-Reader-DC-STIG-Script)下载后，只需在 PowerShell 中输入一条命令即可运行脚本：

```powershell
.\sos-adobe-stig.ps1
```

## 结论

总之，使用 Adobe Reader Pro DC STIG 自动化脚本将应用 Adobe Reader Pro DC STIG 的流程自动化，有助于简化合规流程，确保完全合规，并改善环境的安全态势。通过遵循上述步骤，企业组织可以充分利用脚本的优势，100% 符合指定的 STIG 和 SRG。

___________