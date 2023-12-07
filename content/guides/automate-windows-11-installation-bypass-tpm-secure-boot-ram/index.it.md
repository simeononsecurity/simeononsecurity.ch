---
title: "Automatizzare l'installazione di Windows 11: Bypassare i controlli TPM, Secure Boot e RAM"
date: 2023-09-08
toc: true
draft: false
description: "Semplificate l'installazione di Windows 11 negli ambienti virtualizzati aggirando i controlli TPM, Secure Boot e RAM utilizzando autounattend.xml e vTPM."
genre: ["Tecnologia", "Windows 11", "Installazione", "Virtualizzazione", "Automazione", "Chiavi di registro", "Bypass del TPM", "Bypass dell'avvio sicuro", "Bypass della RAM", "vTPM"]
tags: ["Windows 11", "Installazione", "Automazione", "Virtualizzazione", "vTPM", "Chiavi di registro", "Bypass del TPM", "Bypass dell'avvio sicuro", "Bypass della RAM", "Autounattend.xml", "VMware vSphere", "Impostazione di Windows", "Ambiente di preinstallazione di Windows", "Macchina virtuale", "Soluzione per l'installazione di Windows", "Editor del Registro di sistema", "Installazione di Microsoft Windows", "Requisiti di sistema", "Sicurezza di Windows", "Prestazioni di Windows", "Regolamenti governativi", "Conformità NIST", "Microsoft", "Sistema operativo Windows", "Bypassare i controlli", "Distribuzione di Windows", "Impostazione dell'automazione", "Prompt dei comandi", "Come fare per la tecnologia", "Installazione automatica di Windows 11", "Configurazione di vTPM in VMware vSphere", "Bypassare i requisiti di Windows 11"]
cover: "/img/cover/windows11-installation-cartoon.png"
coverAlt: " Un'immagine in stile cartone animato che raffigura una macchina virtuale che installa Windows 11 in un ambiente virtualizzato con un professionista IT sorridente che supervisiona il processo."
coverCaption: "Semplificare l'installazione con i sorrisi: Automatizzare l'installazione di Windows 11"
---

**Installazione automatizzata di Windows 11 in ambienti virtualizzati**

## **Introduzione**

Windows 11 introduce nuovi requisiti di sistema, tra cui la necessità di un modulo TPM (Trusted Platform Module), Secure Boot e una quantità sufficiente di RAM. Se da un lato questi requisiti migliorano la sicurezza e le prestazioni, dall'altro possono rappresentare una sfida per l'installazione di Windows 11 in ambienti virtualizzati privi di supporto TPM nativo. Tuttavia, esistono soluzioni per aggirare questi controlli e installare Windows 11 con successo.

### **Esclusione dei controlli TPM, Secure Boot e RAM in Windows 11**

Gli ambienti virtualizzati come VMware vSphere possono utilizzare un TPM virtuale (vTPM) per emulare un dispositivo TPM 2.0, soddisfacendo il requisito TPM per l'installazione di Windows 11. Tuttavia, per gli scenari in cui un vPM viene utilizzato per emulare un dispositivo TPM 2.0, è possibile aggirare questi controlli. Tuttavia, per gli scenari in cui non è disponibile un vTPM, è possibile utilizzare le seguenti **chiavi di registro** per aggirare i controlli durante il processo di installazione:

- **BypassTPMCheck**: Salta il controllo TPM.
- **BypassSecureBootCheck**: Salta il controllo Secure Boot.
- **BypassRAMCheck**: Salta il controllo della RAM.

```reg
[HKEY_LOCAL_MACHINE\SYSTEM\Setup\LabConfig]
"BypassTPMCheck"=dword:00000001
"BypassSecureBootCheck"=dword:00000001
"BypassRAMCheck"=dword:00000001
```

Per bypassare manualmente i controlli durante un'installazione **manuale**, procedere come segue:

1. Quando viene visualizzato il messaggio "Questo PC non può eseguire Windows 11", premere [Maiusc]+[F10] per aprire un prompt dei comandi.
2. Utilizzare il comando **regedit** per aprire l'Editor del Registro di sistema.
3. Aggiungete manualmente i valori del registro di cui sopra in **HKEY_LOCAL_MACHINE\SYSTEM\Setup\LabConfig** con un valore di **dword:00000001**.
```powershell
# Create the LabConfig key if it doesn't exist
New-Item -Path "HKLM:\SYSTEM\Setup" -Name "LabConfig" -Force

# Set the registry values under LabConfig
Set-ItemProperty -Path "HKLM:\SYSTEM\Setup\LabConfig" -Name "BypassTPMCheck" -Value 1 -Type DWord
Set-ItemProperty -Path "HKLM:\SYSTEM\Setup\LabConfig" -Name "BypassSecureBootCheck" -Value 1 -Type DWord
Set-ItemProperty -Path "HKLM:\SYSTEM\Setup\LabConfig" -Name "BypassRAMCheck" -Value 1 -Type DWord
```
4. Uscire dal prompt dei comandi e chiudere le finestre di dialogo rimanenti per procedere con la configurazione.

### **Installazione automatica con Autounattend.xml**

Per le installazioni automatiche in ambienti virtualizzati, è possibile utilizzare un file **autounattend.xml** per specificare le impostazioni di configurazione. Per includere le **chiavi di registro di bypass** nel file autounattend.xml, usare il comando **RunSynchronous** come segue:

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

### **Utilizzare con cautela e rispettare i regolamenti**

**L'elusione di questi controlli deve essere effettuata solo in scenari specifici, come gli ambienti virtualizzati che dispongono di misure di sicurezza adeguate. È essenziale **comprendere le implicazioni** dell'aggiramento di questi requisiti e valutare i rischi potenziali.

La necessità di TPM 2.0 e Secure Boot per l'installazione di Windows 11 si basa sui requisiti di sistema dichiarati da Microsoft. In alcuni casi, ad esempio in ambienti governativi o regolamentati, l'esclusione di questi controlli potrebbe non essere conforme a normative o standard di sicurezza specifici. Le organizzazioni devono considerare attentamente i propri requisiti e consultare le normative applicabili, come quelle di agenzie governative come il **National Institute of Standards and Technology (NIST)**, per garantire la conformità.



## **Conclusione**

Seguendo i passaggi illustrati in questo articolo, è possibile automatizzare l'installazione di Windows 11 in ambienti virtualizzati e bypassare i controlli di TPM, Secure Boot e RAM utilizzando un programma di installazione di Windows. `autounattend.xml` file. Tuttavia, ricordate di procedere con cautela e di comprendere le potenziali conseguenze dell'elusione di questi controlli essenziali di sicurezza e prestazioni.

## **Riferimenti**

1. [VMware vSphere Documentation](https://docs.vmware.com/en/VMware-vSphere/index.html)
2. [Enable Virtual Trusted Platform Module for an Existing Virtual Machine](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.vm_admin.doc/GUID-4DBF65A4-4BA0-4667-9725-AE9F047DE00A.html)
3. [National Institute of Standards and Technology (NIST)](https://www.nist.gov/)
4. [Windows 11 – autounattend.xml – BypassTPMCheck – BypassSecureBootCheck](https://iamroot.it/2021/10/06/windows-11-autounattend-xml-bypasstpmcheck-bypasssecurebootcheck/)
