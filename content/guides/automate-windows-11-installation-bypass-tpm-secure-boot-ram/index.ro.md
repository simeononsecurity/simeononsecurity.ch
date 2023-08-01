---
title: "Automatizarea instalării Windows 11: Ocoliți verificările TPM, Secure Boot și RAM"
date: 2023-09-08
toc: true
draft: false
description: "Simplificați instalarea Windows 11 în mediile virtualizate prin ocolirea verificărilor TPM, Secure Boot și RAM folosind autounattend.xml și vTPM."
genre: ["Tehnologie", "Windows 11", "Instalare", "Virtualizare", "Automatizare", "Chei de registru", "Bypass TPM", "Bypassarea Secure Boot", "Bypass RAM", "vTPM"]
tags: ["Windows 11", "Instalare", "Automatizare", "Virtualizare", "vTPM", "Chei de registru", "Bypass TPM", "Bypassarea Secure Boot", "Bypass RAM", "Autounattend.xml", "VMware vSphere", "Configurarea Windows", "Mediul de preinstalare Windows", "Mașină virtuală", "Soluție de lucru pentru instalarea Windows", "Editor de registru", "Configurarea Microsoft Windows", "Cerințe de sistem", "Securitatea Windows", "Performanța Windows", "Reglementări guvernamentale", "Conformitate NIST", "Microsoft", "Sistemul de operare Windows", "Ocolirea controalelor", "Implementarea Windows", "Automatizare de configurare", "Prompt de comandă", "Tehnică Cum se face", "Instalarea automată a Windows 11", "Configurarea vTPM în VMware vSphere", "Ocoliți cerințele Windows 11"]
cover: "/img/cover/windows11-installation-cartoon.png"
coverAlt: " O imagine în stil de desen animat care prezintă o mașină virtuală care instalează Windows 11 într-un mediu virtualizat, cu un profesionist IT zâmbitor care supraveghează procesul."
coverCaption: "Simplificați instalarea cu zâmbete: Automatizați instalarea Windows 11"
---

**Instalarea automată a Windows 11 în mediile virtualizate**

## **Introducere**

Windows 11 introduce noi cerințe de sistem, inclusiv necesitatea unui TPM (Trusted Platform Module), Secure Boot și suficientă memorie RAM. În timp ce aceste cerințe sporesc securitatea și performanța, ele pot reprezenta provocări la instalarea Windows 11 în medii virtualizate fără suport nativ pentru TPM. Cu toate acestea, există soluții de rezolvare pentru a ocoli aceste verificări și a instala Windows 11 cu succes.

### **Bypassing TPM, Secure Boot și verificările RAM în Windows 11**

Mediile virtualizate, cum ar fi VMware vSphere, pot utiliza un TPM virtual (vTPM) pentru a emula un dispozitiv TPM 2.0, satisfăcând cerința TPM pentru instalarea Windows 11. Cu toate acestea, pentru scenariile în care nu este disponibil un vTPM, următoarele **chei de registru** pot fi utilizate pentru a ocoli verificările în timpul procesului de instalare:

- **BypassTPMCheck**: Omite verificarea TPM.
- **BypassSecureBootCheck**: Omite verificarea Secure Boot.
- **BypassRAMCheck**: Ignoră verificarea RAM.

```reg
[HKEY_LOCAL_MACHINE\SYSTEM\Setup\LabConfig]
"BypassTPMCheck"=dword:00000001
"BypassSecureBootCheck"=dword:00000001
"BypassRAMCheck"=dword:00000001
```

Pentru a ocoli manual verificările în timpul unei instalări **manuale**, urmați acești pași:

1. La întâlnirea mesajului "Acest PC nu poate rula Windows 11", apăsați [Shift]+[F10] pentru a deschide un prompt de comandă.
2. Utilizați comanda **regedit** pentru a deschide Editorul de registru.
3. 3. Adăugați manual valorile de registru menționate mai sus în **HKEY_LOCAL_MACHINE\SYSTEM\Setup\LabConfig** cu o valoare de **dword:00000001**.
```powershell
# Create the LabConfig key if it doesn't exist
New-Item -Path "HKLM:\SYSTEM\Setup" -Name "LabConfig" -Force

# Set the registry values under LabConfig
Set-ItemProperty -Path "HKLM:\SYSTEM\Setup\LabConfig" -Name "BypassTPMCheck" -Value 1 -Type DWord
Set-ItemProperty -Path "HKLM:\SYSTEM\Setup\LabConfig" -Name "BypassSecureBootCheck" -Value 1 -Type DWord
Set-ItemProperty -Path "HKLM:\SYSTEM\Setup\LabConfig" -Name "BypassRAMCheck" -Value 1 -Type DWord
```
4. Ieșiți din promptul de comandă și închideți toate ferestrele de dialog rămase pentru a continua cu configurarea.

### **Instalare automatizată utilizând Autounattend.xml**

Pentru instalări automate în medii virtualizate, se poate utiliza un fișier **autounattend.xml** pentru a specifica setările de configurare. Pentru a include **Bypass Registry Keys** în fișierul autounattend.xml, utilizați comanda **RunSynchronous** după cum urmează:

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

### **Utilizați cu prudență și respectați reglementările**

**Pasarea** acestor verificări ar trebui să se facă numai în scenarii specifice, cum ar fi mediile virtualizate care dispun de măsuri de securitate adecvate. Este esențial să **înțelegeți implicațiile** ocolirii acestor cerințe și să evaluați riscurile potențiale.

Nevoia de TPM 2.0 și Secure Boot pentru instalarea Windows 11 se bazează pe cerințele de sistem declarate de Microsoft. În unele cazuri, cum ar fi în mediile guvernamentale sau reglementate, este posibil ca ocolirea acestor verificări să nu fie conformă cu reglementările sau standardele de securitate specifice. Organizațiile ar trebui să analizeze cu atenție cerințele lor și să consulte reglementările aplicabile, cum ar fi cele ale agențiilor guvernamentale precum **National Institute of Standards and Technology (NIST)**, pentru a asigura conformitatea.

______
{{< inarticle-dark >}}
______

## **Concluzie**

Urmând pașii descriși în acest articol, puteți automatiza instalarea Windows 11 în mediile virtualizate și puteți ocoli verificările TPM, Secure Boot și RAM folosind un `autounattend.xml` dosar. Cu toate acestea, nu uitați să procedați cu prudență și să înțelegeți consecințele potențiale ale ocolirii acestor verificări esențiale de securitate și performanță.

## **Referințe**

1. [VMware vSphere Documentation](https://docs.vmware.com/en/VMware-vSphere/index.html)
2. [Enable Virtual Trusted Platform Module for an Existing Virtual Machine](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.vm_admin.doc/GUID-4DBF65A4-4BA0-4667-9725-AE9F047DE00A.html)
3. [National Institute of Standards and Technology (NIST)](https://www.nist.gov/)
4. [Windows 11 – autounattend.xml – BypassTPMCheck – BypassSecureBootCheck](https://iamroot.it/2021/10/06/windows-11-autounattend-xml-bypasstpmcheck-bypasssecurebootcheck/)
