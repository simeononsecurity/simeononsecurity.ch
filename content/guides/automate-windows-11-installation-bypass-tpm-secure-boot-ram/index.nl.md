---
title: "Windows 11-installatie automatiseren: TPM, Secure Boot en RAM-controles omzeilen"
date: 2023-09-08
toc: true
draft: false
description: "Stroomlijn de installatie van Windows 11 in gevirtualiseerde omgevingen door TPM, Secure Boot en RAM-controles te omzeilen met autounattend.xml en vTPM."
genre: ["Technologie", "Windows 11", "Installatie", "Virtualisatie", "Automatisering", "Registersleutels", "TPM omleiding", "Beveiligd opstarten omzeilen", "RAM omleiding", "vTPM"]
tags: ["Windows 11", "Installatie", "Automatisering", "Virtualisatie", "vTPM", "Registersleutels", "TPM omleiding", "Beveiligd opstarten omzeilen", "RAM omleiding", "Autounattend.xml", "VMware vSphere", "Windows instellen", "Windows-omgeving voor installatie", "Virtuele machine", "Windows installatie-omleiding", "Register-editor", "Microsoft Windows instellen", "Systeemvereisten", "Windows Beveiliging", "Windows prestaties", "Overheidsvoorschriften", "NIST-naleving", "Microsoft", "Windows OS", "Controles omzeilen", "Windows installatie", "Automatisering instellen", "Opdrachtprompt", "Technische handleiding", "Geautomatiseerde installatie van Windows 11", "vTPM-configuratie in VMware vSphere", "Windows 11-vereisten omzeilen"]
cover: "/img/cover/windows11-installation-cartoon.png"
coverAlt: " Een cartoonachtige afbeelding van een virtuele machine die Windows 11 installeert in een gevirtualiseerde omgeving met een lachende IT-professional die toezicht houdt op het proces."
coverCaption: "Vereenvoudig installatie met Smiles: Installatie van Windows 11 automatiseren"
---

**Geautomatiseerde installatie van Windows 11 in gevirtualiseerde omgevingen**

## **Inleiding**

Windows 11 introduceert nieuwe systeemvereisten, waaronder de behoefte aan een TPM (Trusted Platform Module), Secure Boot en voldoende RAM. Hoewel deze vereisten de beveiliging en prestaties verbeteren, kunnen ze uitdagingen vormen bij het installeren van Windows 11 in gevirtualiseerde omgevingen zonder native TPM-ondersteuning. Er zijn echter workarounds om deze controles te omzeilen en Windows 11 met succes te installeren.

### TPM-, Secure Boot- en RAM-controles omzeilen in Windows 11**

Gevirtualiseerde omgevingen zoals VMware vSphere kunnen een virtuele TPM (vTPM) gebruiken om een TPM 2.0-apparaat te emuleren, waardoor wordt voldaan aan de TPM-vereiste voor Windows 11-installatie. Voor scenario's waar geen vTPM beschikbaar is, kunnen de volgende **registersleutels** worden gebruikt om de controles tijdens het installatieproces te omzeilen:

- **BypassTPMCheck**: Sla de TPM-controle over.
- **BypassSecureBootCheck**: Secure Boot-controle overslaan.
- SlaRAMCheck** over: Sla RAM-controle over.

```reg
[HKEY_LOCAL_MACHINE\SYSTEM\Setup\LabConfig]
"BypassTPMCheck"=dword:00000001
"BypassSecureBootCheck"=dword:00000001
"BypassRAMCheck"=dword:00000001
```

Volg deze stappen om de controles handmatig te omzeilen tijdens een **handmatige installatie**:

1. Wanneer u het bericht "Deze pc kan Windows 11 niet uitvoeren" tegenkomt, drukt u op [Shift]+[F10] om een opdrachtprompt te openen.
2. Gebruik de opdracht **regedit** om de Register-editor te openen.
3. Voeg handmatig de bovengenoemde registerwaarden toe onder **HKEY_LOCAL_MACHINE\SYSTEM\SetupLabConfig** met als waarde **dword:00000001**.
```powershell
# Create the LabConfig key if it doesn't exist
New-Item -Path "HKLM:\SYSTEM\Setup" -Name "LabConfig" -Force

# Set the registry values under LabConfig
Set-ItemProperty -Path "HKLM:\SYSTEM\Setup\LabConfig" -Name "BypassTPMCheck" -Value 1 -Type DWord
Set-ItemProperty -Path "HKLM:\SYSTEM\Setup\LabConfig" -Name "BypassSecureBootCheck" -Value 1 -Type DWord
Set-ItemProperty -Path "HKLM:\SYSTEM\Setup\LabConfig" -Name "BypassRAMCheck" -Value 1 -Type DWord
```
4. Sluit de opdrachtprompt af en sluit alle resterende dialoogvensters om verder te gaan met de installatie.

**Geautomatiseerde installatie met Autounattend.xml**

Voor geautomatiseerde installaties in gevirtualiseerde omgevingen kan een **autounattend.xml** bestand gebruikt worden om configuratie-instellingen op te geven. Gebruik de opdracht **RunSynchronous** om de **Bypass Registry Keys** in het autounattend.xml-bestand op te nemen:

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

**Gebruik voorzichtigheid en houd u aan de voorschriften**

**Het omzeilen** van deze controles mag alleen gedaan worden in specifieke scenario's, zoals gevirtualiseerde omgevingen met de juiste beveiligingsmaatregelen. Het is essentieel om de implicaties** van het omzeilen van deze vereisten te begrijpen en de potentiële risico's in te schatten.

De noodzaak van TPM 2.0 en Secure Boot voor de installatie van Windows 11 is gebaseerd op de door Microsoft opgegeven systeemvereisten. In sommige gevallen, zoals in overheids- of gereguleerde omgevingen, is het omzeilen van deze controles mogelijk niet in overeenstemming met specifieke voorschriften of beveiligingsstandaarden. Organisaties moeten zorgvuldig hun vereisten overwegen en toepasselijke voorschriften raadplegen, zoals die van overheidsinstellingen zoals het **National Institute of Standards and Technology (NIST)**, om naleving te garanderen.

______
{{< inarticle-dark >}}
______

**Conclusie**

Door de in dit artikel beschreven stappen te volgen, kunt u de installatie van Windows 11 in gevirtualiseerde omgevingen automatiseren en de TPM-, Secure Boot- en RAM-controles omzeilen met een `autounattend.xml` bestand. Wees echter voorzichtig en begrijp de mogelijke gevolgen van het omzeilen van deze essentiële beveiligings- en prestatiecontroles.

## Verwijzingen**

1. [VMware vSphere Documentation](https://docs.vmware.com/en/VMware-vSphere/index.html)
2. [Enable Virtual Trusted Platform Module for an Existing Virtual Machine](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.vm_admin.doc/GUID-4DBF65A4-4BA0-4667-9725-AE9F047DE00A.html)
3. [National Institute of Standards and Technology (NIST)](https://www.nist.gov/)
4. [Windows 11 – autounattend.xml – BypassTPMCheck – BypassSecureBootCheck](https://iamroot.it/2021/10/06/windows-11-autounattend-xml-bypasstpmcheck-bypasssecurebootcheck/)
