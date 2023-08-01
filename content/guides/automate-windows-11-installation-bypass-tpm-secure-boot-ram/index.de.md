---
title: "Automatisieren Sie die Installation von Windows 11: Umgehung von TPM, Secure Boot und RAM-Prüfungen"
date: 2023-09-08
toc: true
draft: false
description: "Optimieren Sie die Installation von Windows 11 in virtualisierten Umgebungen, indem Sie TPM-, Secure Boot- und RAM-Prüfungen mit autounattend.xml und vTPM umgehen."
genre: ["Technologie", "Fenster 11", "Einrichtung", "Virtualisierung", "Automatisierung", "Registry-Schlüssel", "TPM-Umgehung", "Secure Boot-Umgehung", "RAM-Umgehung", "vTPM"]
tags: ["Fenster 11", "Einrichtung", "Automatisierung", "Virtualisierung", "vTPM", "Registry-Schlüssel", "TPM-Umgehung", "Secure Boot-Umgehung", "RAM-Umgehung", "Autounattend.xml", "VMware vSphere", "Windows-Einrichtung", "Windows Vorinstallationsumgebung", "Virtuelle Maschine", "Umgehung der Windows-Installation", "Registrierungs-Editor", "Microsoft Windows-Einrichtung", "Systemanforderungen", "Windows-Sicherheit", "Windows-Leistung", "Staatliche Vorschriften", "NIST-Konformität", "Microsoft", "Windows-Betriebssystem", "Umgehung von Kontrollen", "Windows-Bereitstellung", "Automatisierung einrichten", "Eingabeaufforderung", "Technisches How-To", "Automatisierte Windows 11-Installation", "vTPM-Konfiguration in VMware vSphere", "Umgehung der Windows 11-Anforderungen"]
cover: "/img/cover/windows11-installation-cartoon.png"
coverAlt: " Ein Bild im Cartoon-Stil, das eine virtuelle Maschine zeigt, die Windows 11 in einer virtualisierten Umgebung installiert, während ein lächelnder IT-Experte den Vorgang überwacht."
coverCaption: "Vereinfachen Sie die Einrichtung mit Smiles: Automatisieren Sie die Installation von Windows 11"
---

**Automatisierte Windows 11-Installation in virtualisierten Umgebungen**

## **Einführung**

Windows 11 führt neue Systemanforderungen ein, darunter die Notwendigkeit eines TPM (Trusted Platform Module), Secure Boot und ausreichend RAM. Während diese Anforderungen die Sicherheit und Leistung verbessern, können sie bei der Installation von Windows 11 in virtualisierten Umgebungen ohne native TPM-Unterstützung zu Problemen führen. Es gibt jedoch Umgehungsmöglichkeiten, um diese Prüfungen zu umgehen und Windows 11 erfolgreich zu installieren.

**Umgehung der TPM-, Secure Boot- und RAM-Prüfungen in Windows 11**

Virtualisierte Umgebungen wie VMware vSphere können ein virtuelles TPM (vTPM) verwenden, um ein TPM 2.0-Gerät zu emulieren und so die TPM-Anforderungen für die Installation von Windows 11 zu erfüllen. Für Szenarien, in denen kein vTPM verfügbar ist, können jedoch die folgenden **Registrierungsschlüssel** verwendet werden, um die Prüfungen während des Installationsprozesses zu umgehen:

- **BypassTPMCheck**: TPM-Prüfung überspringen.
- **BypassSecureBootCheck**: Secure Boot-Prüfung überspringen.
- **BypassRAMCheck**: RAM-Prüfung überspringen.

```reg
[HKEY_LOCAL_MACHINE\SYSTEM\Setup\LabConfig]
"BypassTPMCheck"=dword:00000001
"BypassSecureBootCheck"=dword:00000001
"BypassRAMCheck"=dword:00000001
```

Um die Prüfungen während einer **manuellen Installation** manuell zu umgehen, gehen Sie wie folgt vor:

1. Wenn die Meldung "Auf diesem PC kann Windows 11 nicht ausgeführt werden" angezeigt wird, drücken Sie [Umschalt]+[F10], um eine Eingabeaufforderung zu öffnen.
2. Verwenden Sie den Befehl **regedit**, um den Registrierungseditor zu öffnen.
3. Fügen Sie die oben genannten Registrierungswerte manuell unter **HKEY_LOCAL_MACHINE\SYSTEM\Setup\LabConfig** mit einem Wert von **dword:00000001** hinzu.
```powershell
# Create the LabConfig key if it doesn't exist
New-Item -Path "HKLM:\SYSTEM\Setup" -Name "LabConfig" -Force

# Set the registry values under LabConfig
Set-ItemProperty -Path "HKLM:\SYSTEM\Setup\LabConfig" -Name "BypassTPMCheck" -Value 1 -Type DWord
Set-ItemProperty -Path "HKLM:\SYSTEM\Setup\LabConfig" -Name "BypassSecureBootCheck" -Value 1 -Type DWord
Set-ItemProperty -Path "HKLM:\SYSTEM\Setup\LabConfig" -Name "BypassRAMCheck" -Value 1 -Type DWord
```
4. Beenden Sie die Eingabeaufforderung und schließen Sie alle verbleibenden Dialogfelder, um mit der Einrichtung fortzufahren.

### **Automatische Installation mit Autounattend.xml**

Für automatisierte Installationen in virtualisierten Umgebungen kann eine **autounattend.xml**-Datei verwendet werden, um Konfigurationseinstellungen festzulegen. Um die **Bypass Registry Keys** in die Datei autounattend.xml aufzunehmen, verwenden Sie den Befehl **RunSynchronous** wie folgt:

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

### **Vorsicht und Einhaltung der Vorschriften**

**Die Umgehung** dieser Prüfungen sollte nur in bestimmten Szenarien erfolgen, z. B. in virtualisierten Umgebungen, die über angemessene Sicherheitsmaßnahmen verfügen. Es ist wichtig, **die Auswirkungen** der Umgehung dieser Anforderungen zu verstehen und die potenziellen Risiken zu bewerten.

Die Notwendigkeit von TPM 2.0 und Secure Boot für die Installation von Windows 11 basiert auf den von Microsoft angegebenen Systemanforderungen. In einigen Fällen, z. B. in Behörden oder regulierten Umgebungen, ist die Umgehung dieser Prüfungen möglicherweise nicht mit bestimmten Vorschriften oder Sicherheitsstandards konform. Organisationen sollten ihre Anforderungen sorgfältig abwägen und die geltenden Vorschriften, z. B. die von Regierungsbehörden wie dem **National Institute of Standards and Technology (NIST)**, konsultieren, um die Einhaltung der Vorschriften sicherzustellen.

______
{{< inarticle-dark >}}
______

## **Schlussfolgerung**

Wenn Sie die in diesem Artikel beschriebenen Schritte befolgen, können Sie die Installation von Windows 11 in virtualisierten Umgebungen automatisieren und die TPM-, Secure Boot- und RAM-Prüfungen mithilfe eines `autounattend.xml` Datei. Seien Sie jedoch vorsichtig und machen Sie sich die möglichen Folgen einer Umgehung dieser wichtigen Sicherheits- und Leistungsprüfungen bewusst.

## **Referenzen**

1. [VMware vSphere Documentation](https://docs.vmware.com/en/VMware-vSphere/index.html)
2. [Enable Virtual Trusted Platform Module for an Existing Virtual Machine](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.vm_admin.doc/GUID-4DBF65A4-4BA0-4667-9725-AE9F047DE00A.html)
3. [National Institute of Standards and Technology (NIST)](https://www.nist.gov/)
4. [Windows 11 – autounattend.xml – BypassTPMCheck – BypassSecureBootCheck](https://iamroot.it/2021/10/06/windows-11-autounattend-xml-bypasstpmcheck-bypasssecurebootcheck/)
