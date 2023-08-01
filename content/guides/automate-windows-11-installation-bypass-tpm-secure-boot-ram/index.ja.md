---
title: "Windows 11のインストールを自動化：TPM、セキュアブート、RAMチェックを回避する"
date: 2023-09-08
toc: true
draft: false
description: "autounattend.xmlとvTPMを使用して、TPM、セキュアブート、RAMのチェックを回避することにより、仮想化環境におけるWindows 11のインストールを合理化します。"
genre: ["テクノロジー", "ウィンドウズ11", "インストール", "仮想化", "オートメーション", "レジストリ・キー", "TPMバイパス", "セキュアブート・バイパス", "RAMバイパス", "ブイティピーエム"]
tags: ["ウィンドウズ11", "インストール", "オートメーション", "仮想化", "ブイティピーエム", "レジストリ・キー", "TPMバイパス", "セキュアブート・バイパス", "RAMバイパス", "Autounattend.xml", "VMware vSphere", "Windowsセットアップ", "Windowsプリインストール環境", "仮想マシン", "Windowsインストールの回避策", "レジストリエディタ", "マイクロソフト・ウィンドウズのセットアップ", "システム要件", "Windowsセキュリティ", "ウィンドウズ・パフォーマンス", "政府規制", "NISTコンプライアンス", "マイクロソフト", "ウィンドウズOS", "チェックの回避", "ウィンドウズ展開", "セットアップ・オートメーション", "コマンドプロンプト", "技術ハウツー", "Windows 11の自動インストール", "VMware vSphereにおけるvTPMの構成", "Windows 11の要件を回避する"]
cover: "/img/cover/windows11-installation-cartoon.png"
coverAlt: "仮想化環境にWindows 11をインストールする仮想マシンと、そのプロセスを見守る笑顔のITプロフェッショナルを描いた漫画風の画像。"
coverCaption: "スマイルでセットアップを簡素化：Windows 11のインストールを自動化"
---

**仮想化環境におけるWindows 11の自動インストール

# **はじめに**

Windows 11 では、TPM (Trusted Platform Module)、セキュアブート、十分な RAM などの新しいシステム要件が導入されています。これらの要件はセキュリティとパフォーマンスを向上させますが、ネイティブの TPM サポートがない仮想化環境に Windows 11 をインストールする際に課題となる可能性があります。しかし、これらのチェックを回避し、Windows 11を正常にインストールするための回避策があります。

### Windows 11 の TPM、セキュアブート、および RAM のチェックを回避する**」。

VMware vSphere のような仮想化環境では、仮想 TPM (vTPM) を使用して TPM 2.0 デバイスをエミュレートし、Windows 11 インストールの TPM 要件を満たすことができます。ただし、vTPMが使用できないシナリオでは、以下の**レジストリキー**を使用して、インストールプロセス中のチェックをバイパスすることができます：

- BypassTPMCheck**：TPMチェックをスキップします。
- BypassTPMCheck**：TPMチェックをスキップします：セキュアブートチェックをスキップします。
- BypassRAMCheck**：RAMチェックをスキップします：RAMチェックをスキップします。

```reg
[HKEY_LOCAL_MACHINE\SYSTEM\Setup\LabConfig]
"BypassTPMCheck"=dword:00000001
"BypassSecureBootCheck"=dword:00000001
"BypassRAMCheck"=dword:00000001
```

手動インストール**中に手動でチェックをバイパスするには、以下の手順に従ってください：

1.このPCはWindows 11を実行できません」というメッセージが表示されたら、[Shift]+[F10]を押してコマンドプロンプトを開く。
2.regedit**コマンドを使用してレジストリエディタを開きます。
3.HKEY_LOCAL_MACHINESYSTEMSetupLabConfig**の下に、前述のレジストリ値を**dword:00000001**の値で手動で追加する。
```powershell
# Create the LabConfig key if it doesn't exist
New-Item -Path "HKLM:\SYSTEM\Setup" -Name "LabConfig" -Force

# Set the registry values under LabConfig
Set-ItemProperty -Path "HKLM:\SYSTEM\Setup\LabConfig" -Name "BypassTPMCheck" -Value 1 -Type DWord
Set-ItemProperty -Path "HKLM:\SYSTEM\Setup\LabConfig" -Name "BypassSecureBootCheck" -Value 1 -Type DWord
Set-ItemProperty -Path "HKLM:\SYSTEM\Setup\LabConfig" -Name "BypassRAMCheck" -Value 1 -Type DWord
```
4.コマンドプロンプトを終了し、残っているダイアログを閉じてセットアップを続行します。

### **Autounattend.xml**を使用した自動インストール

仮想化環境での自動インストールでは、**autounattend.xml** ファイルを使用して構成設定を指定できます。autounattend.xml ファイルに **Bypass Registry Keys** を含めるには、次のように **RunSynchronous** コマンドを使用します：

```xml
<?xml version="1.0" encoding="utf-8"?>
<unattend xmlns="urn:schemas-microsoft-com:unattend">
    <settings pass="windowsPE">
        <!-- Other settings -->
        <component name="Microsoft-Windows-Setup" processorArchitecture="amd64" publicKeyToken="31bf3856ad364e35" language="neutral" versionScope="nonSxS" xmlns:wcm="http://schemas.microsoft.com/WMIConfig/2002/State" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">            
            <RunSynchronous>
                <RunSynchronousCommand wcm:action="add">
                    <Order>1</Order>
                    <Description>BypassTPMCheck</Description>
                    <Path>cmd /c reg add "HKLM\SYSTEM\Setup\LabConfig" /v "BypassTPMCheck" /t REG_DWORD /d 1</Path>
                </RunSynchronousCommand>
                <RunSynchronousCommand wcm:action="add">
                    <Order>2</Order>
                    <Description>BypassSecureBootCheck</Description>
                    <Path>cmd /c reg add "HKLM\SYSTEM\Setup\LabConfig" /v "BypassSecureBootCheck" /t REG_DWORD /d 1</Path>
                </RunSynchronousCommand>
                <RunSynchronousCommand wcm:action="add">
                    <Order>3</Order>
                    <Description>BypassRAMCheck</Description>
                    <Path>cmd /c reg add "HKLM\SYSTEM\Setup\LabConfig" /v "BypassRAMCheck" /t REG_DWORD /d 1</Path>
                </RunSynchronousCommand>
            </RunSynchronous>
            <!-- Other components and settings -->
        </component>
        <!-- Other settings -->
    </settings>
    <!-- Disk configurations and other sections -->
</unattend>
```

### 注意と規則を守ること。

**これらのチェックのバイパス**は、適切なセキュリティ対策が施されている仮想化環境など、特定のシナリオにおいてのみ実行されるべきである。これらの要件をバイパスすることの意味**を理解し、潜在的なリスクを評価することが不可欠です。

Windows 11のインストールにおけるTPM 2.0とセキュアブートの必要性は、マイクロソフトのシステム要件に基づいています。政府機関や規制された環境など、場合によっては、これらのチェックをバイパスすることが特定の規制やセキュリティ標準に準拠していない可能性があります。組織は、要件を慎重に検討し、**国立標準技術研究所（NIST）** などの政府機関による規制など、適用される規制を参照して、コンプライアンスを確保する必要があります。

______
{{< inarticle-dark >}}
______

## 結論**

この記事で説明した手順に従うことで、仮想化環境への Windows 11 のインストールを自動化し、TPM、セキュアブート、RAM のチェックを回避することができます。 `autounattend.xml`ファイルを使用する。しかし、これらの重要なセキュリティーとパフォーマンスのチェックを迂回した場合に起こりうる結果を理解し、慎重に進めることを忘れないでください。

## 参考文献**

1. [VMware vSphere Documentation](https://docs.vmware.com/en/VMware-vSphere/index.html)
2. [Enable Virtual Trusted Platform Module for an Existing Virtual Machine](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.vm_admin.doc/GUID-4DBF65A4-4BA0-4667-9725-AE9F047DE00A.html)
3. [National Institute of Standards and Technology (NIST)](https://www.nist.gov/)
4. [Windows 11 – autounattend.xml – BypassTPMCheck – BypassSecureBootCheck](https://iamroot.it/2021/10/06/windows-11-autounattend-xml-bypasstpmcheck-bypasssecurebootcheck/)
