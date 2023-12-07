---
title: "Automatice la instalación de Windows 11: Eludir TPM, Secure Boot y comprobaciones de RAM"
date: 2023-09-08
toc: true
draft: false
description: "Agilice la instalación de Windows 11 en entornos virtualizados evitando las comprobaciones de TPM, Secure Boot y RAM mediante autounattend.xml y vTPM."
genre: ["Tecnología", "Windows 11", "Instalación", "Virtualización", "Automatización", "Claves de registro", "Bypass TPM", "Anulación del arranque seguro", "Bypass de RAM", "vTPM"]
tags: ["Windows 11", "Instalación", "Automatización", "Virtualización", "vTPM", "Claves de registro", "Bypass TPM", "Anulación del arranque seguro", "Bypass de RAM", "Autounattend.xml", "VMware vSphere", "Configuración de Windows", "Entorno de preinstalación de Windows", "Máquina virtual", "Solución para la instalación en Windows", "Editor del Registro", "Configuración de Microsoft Windows", "Requisitos del sistema", "Seguridad de Windows", "Rendimiento de Windows", "Normativa gubernamental", "Cumplimiento del NIST", "Microsoft", "Sistema operativo Windows", "Eludir los controles", "Implantación de Windows", "Automatización de la configuración", "Símbolo del sistema", "Tecnología", "Instalación automatizada de Windows 11", "Configuración de vTPM en VMware vSphere", "Eludir los requisitos de Windows 11"]
cover: "/img/cover/windows11-installation-cartoon.png"
coverAlt: " Una imagen de dibujos animados que muestra una máquina virtual instalando Windows 11 en un entorno virtualizado con un sonriente profesional de TI supervisando el proceso."
coverCaption: "Simplifique la instalación con Smiles: Automatice la instalación de Windows 11"
---

**Instalación automatizada de Windows 11 en entornos virtualizados**

## **Introducción**

Windows 11 introduce nuevos requisitos del sistema, incluida la necesidad de un TPM (Trusted Platform Module), Secure Boot y suficiente RAM. Aunque estos requisitos mejoran la seguridad y el rendimiento, pueden plantear problemas al instalar Windows 11 en entornos virtualizados sin compatibilidad nativa con TPM. Sin embargo, existen soluciones para evitar estas comprobaciones e instalar Windows 11 correctamente.

### Eludir las comprobaciones de TPM, arranque seguro y RAM en Windows 11

Los entornos virtualizados como VMware vSphere pueden utilizar un TPM virtual (vTPM) para emular un dispositivo TPM 2.0, satisfaciendo así el requisito de TPM para la instalación de Windows 11. Sin embargo, para situaciones en las que no se dispone de un vTPM, se pueden utilizar las siguientes **claves de registro** para omitir las comprobaciones durante el proceso de instalación:

- BypassTPMCheck**: Omitir comprobación de TPM.
- OmitirSecureBootCheck**: Omite la comprobación de Secure Boot.
- OmitirRAMCheck**: Omitir comprobación de RAM.

```reg
[HKEY_LOCAL_MACHINE\SYSTEM\Setup\LabConfig]
"BypassTPMCheck"=dword:00000001
"BypassSecureBootCheck"=dword:00000001
"BypassRAMCheck"=dword:00000001
```

Para evitar manualmente las comprobaciones durante una **instalación manual**, siga estos pasos:

1. Cuando aparezca el mensaje "Este PC no puede ejecutar Windows 11", pulse [Mayús]+[F10] para abrir un símbolo del sistema.
2. Utilice el comando **regedit** para abrir el Editor del Registro.
3. 3. Añada manualmente los valores de registro antes mencionados en **HKEY_LOCAL_MACHINE\SYSTEM\Setup\LabConfig** con un valor de **dword:00000001**.
```powershell
# Create the LabConfig key if it doesn't exist
New-Item -Path "HKLM:\SYSTEM\Setup" -Name "LabConfig" -Force

# Set the registry values under LabConfig
Set-ItemProperty -Path "HKLM:\SYSTEM\Setup\LabConfig" -Name "BypassTPMCheck" -Value 1 -Type DWord
Set-ItemProperty -Path "HKLM:\SYSTEM\Setup\LabConfig" -Name "BypassSecureBootCheck" -Value 1 -Type DWord
Set-ItemProperty -Path "HKLM:\SYSTEM\Setup\LabConfig" -Name "BypassRAMCheck" -Value 1 -Type DWord
```
4. Salga del símbolo del sistema y cierre los cuadros de diálogo restantes para continuar con la configuración.

### **Instalación automatizada mediante Autounattend.xml**

Para instalaciones automatizadas en entornos virtualizados, se puede utilizar un archivo **autounattend.xml** para especificar los parámetros de configuración. Para incluir el **Bypass Registry Keys** en el archivo autounattend.xml, utilice el comando **RunSynchronous** de la siguiente manera:

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

### **Tenga cuidado y respete las normas##

**Saltar** estas comprobaciones sólo debe hacerse en escenarios específicos, como entornos virtualizados que cuenten con las medidas de seguridad adecuadas. Es esencial **comprender las implicaciones** de saltarse estos requisitos y evaluar los riesgos potenciales.

La necesidad de TPM 2.0 y Secure Boot para la instalación de Windows 11 se basa en los requisitos del sistema establecidos por Microsoft. En algunos casos, como en entornos gubernamentales o regulados, saltarse estas comprobaciones puede no cumplir con normativas o estándares de seguridad específicos. Las organizaciones deben considerar detenidamente sus requisitos y consultar las normativas aplicables, como las de organismos gubernamentales como el **National Institute of Standards and Technology (NIST)**, para garantizar su cumplimiento.



## **Conclusión**

Siguiendo los pasos descritos en este artículo, puede automatizar la instalación de Windows 11 en entornos virtualizados y evitar las comprobaciones de TPM, Secure Boot y RAM utilizando un `autounattend.xml` archivo. Sin embargo, recuerde proceder con cautela y comprender las posibles consecuencias de saltarse estas comprobaciones esenciales de seguridad y rendimiento.

## **Referencias**

1. [VMware vSphere Documentation](https://docs.vmware.com/en/VMware-vSphere/index.html)
2. [Enable Virtual Trusted Platform Module for an Existing Virtual Machine](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.vm_admin.doc/GUID-4DBF65A4-4BA0-4667-9725-AE9F047DE00A.html)
3. [National Institute of Standards and Technology (NIST)](https://www.nist.gov/)
4. [Windows 11 – autounattend.xml – BypassTPMCheck – BypassSecureBootCheck](https://iamroot.it/2021/10/06/windows-11-autounattend-xml-bypasstpmcheck-bypasssecurebootcheck/)
