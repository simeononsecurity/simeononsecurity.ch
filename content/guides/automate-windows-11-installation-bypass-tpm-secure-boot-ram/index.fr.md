---
title: "Automatiser l'installation de Windows 11 : Contourner les contrôles TPM, Secure Boot et RAM"
date: 2023-09-08
toc: true
draft: false
description: "Rationaliser l'installation de Windows 11 dans les environnements virtualisés en contournant les contrôles TPM, Secure Boot et RAM à l'aide de autounattend.xml et vTPM."
genre: ["Technologie", "Windows 11", "Installation", "Virtualisation", "Automatisation", "Clés de registre", "Contournement du TPM", "Contournement du démarrage sécurisé", "Dérivation de la RAM", "vTPM"]
tags: ["Windows 11", "Installation", "Automatisation", "Virtualisation", "vTPM", "Clés de registre", "Contournement du TPM", "Contournement du démarrage sécurisé", "Dérivation de la RAM", "Autounattend.xml", "VMware vSphere", "Configuration de Windows", "Environnement de préinstallation de Windows", "Machine virtuelle", "Solution de contournement pour l'installation de Windows", "Éditeur de registre", "Installation de Microsoft Windows", "Configuration requise", "Sécurité Windows", "Performance de Windows", "Réglementation gouvernementale", "Conformité NIST", "Microsoft", "Système d'exploitation Windows", "Contournement des contrôles", "Déploiement de Windows", "Automatisation de la mise en place", "Invite de commande", "Mode d'emploi de la technologie", "Installation automatisée de Windows 11", "Configuration de la vTPM dans VMware vSphere", "Contourner les exigences de Windows 11"]
cover: "/img/cover/windows11-installation-cartoon.png"
coverAlt: " Image de style bande dessinée représentant une machine virtuelle installant Windows 11 dans un environnement virtualisé, sous le regard souriant d'un professionnel de l'informatique."
coverCaption: "Simplifiez l'installation avec Smiles : Automatiser l'installation de Windows 11"
---

**Installation automatisée de Windows 11 dans les environnements virtualisés**

## **Introduction**

Windows 11 introduit de nouvelles exigences en matière de système, notamment la nécessité d'un TPM (Trusted Platform Module), d'un démarrage sécurisé et d'une quantité suffisante de mémoire vive. Bien que ces exigences améliorent la sécurité et les performances, elles peuvent poser des problèmes lors de l'installation de Windows 11 dans des environnements virtualisés sans prise en charge native du TPM. Toutefois, il existe des solutions de contournement permettant d'éviter ces vérifications et d'installer Windows 11 avec succès.

### **Contourner les vérifications du TPM, du Secure Boot et de la RAM dans Windows 11**

Les environnements virtualisés tels que VMware vSphere peuvent utiliser un TPM virtuel (vTPM) pour émuler un périphérique TPM 2.0, satisfaisant ainsi à l'exigence de TPM pour l'installation de Windows 11. Cependant, pour les scénarios où un vTPM n'est pas disponible, les **clés de registre** suivantes peuvent être utilisées pour contourner les vérifications pendant le processus d'installation :

- **BypassTPMCheck** : Ignorer la vérification du TPM.
- **BypassSecureBootCheck** : Ignorer la vérification de l'amorçage sécurisé.
- **BypassRAMCheck** : Ignorer la vérification de la RAM.

```reg
[HKEY_LOCAL_MACHINE\SYSTEM\Setup\LabConfig]
"BypassTPMCheck"=dword:00000001
"BypassSecureBootCheck"=dword:00000001
"BypassRAMCheck"=dword:00000001
```

Pour contourner manuellement les contrôles lors d'une **installation manuelle**, procédez comme suit :

1. Lorsque le message "Ce PC ne peut pas exécuter Windows 11" apparaît, appuyez sur [Shift]+[F10] pour ouvrir une invite de commande.
2. Utilisez la commande **regedit** pour ouvrir l'éditeur du registre.
3. Ajoutez manuellement les valeurs de registre susmentionnées sous **HKEY_LOCAL_MACHINE\SYSTEM\Setup\LabConfig** avec une valeur de **dword:00000001**.
```powershell
# Create the LabConfig key if it doesn't exist
New-Item -Path "HKLM:\SYSTEM\Setup" -Name "LabConfig" -Force

# Set the registry values under LabConfig
Set-ItemProperty -Path "HKLM:\SYSTEM\Setup\LabConfig" -Name "BypassTPMCheck" -Value 1 -Type DWord
Set-ItemProperty -Path "HKLM:\SYSTEM\Setup\LabConfig" -Name "BypassSecureBootCheck" -Value 1 -Type DWord
Set-ItemProperty -Path "HKLM:\SYSTEM\Setup\LabConfig" -Name "BypassRAMCheck" -Value 1 -Type DWord
```
4. Quittez l'invite de commande et fermez toutes les boîtes de dialogue restantes pour procéder à l'installation.

### **Installation automatisée à l'aide de Autounattend.xml**

Pour les installations automatisées dans des environnements virtualisés, un fichier **autounattend.xml** peut être utilisé pour spécifier les paramètres de configuration. Pour inclure les **clés de registre de contournement** dans le fichier autounattend.xml, utilisez la commande **RunSynchronous** comme suit :

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

### **Utiliser la prudence et respecter les réglementations**

**Le contournement** de ces vérifications ne doit être effectué que dans des scénarios spécifiques, tels que les environnements virtualisés qui ont mis en place des mesures de sécurité appropriées. Il est essentiel de **comprendre les implications** du contournement de ces exigences et d'évaluer les risques potentiels.

La nécessité de disposer de TPM 2.0 et de Secure Boot pour l'installation de Windows 11 est basée sur les exigences système énoncées par Microsoft. Dans certains cas, comme dans les environnements gouvernementaux ou réglementés, le contournement de ces vérifications peut ne pas être conforme à des réglementations spécifiques ou à des normes de sécurité. Les organisations doivent examiner attentivement leurs besoins et consulter les réglementations applicables, telles que celles des agences gouvernementales comme le **National Institute of Standards and Technology (NIST)**, pour s'assurer de leur conformité.



## **Conclusion**

En suivant les étapes décrites dans cet article, vous pouvez automatiser l'installation de Windows 11 dans des environnements virtualisés et contourner les vérifications du TPM, du Secure Boot et de la RAM à l'aide d'un logiciel d'installation de Windows 11. `autounattend.xml` de l'ordinateur. Cependant, n'oubliez pas de procéder avec prudence et de comprendre les conséquences potentielles du contournement de ces contrôles essentiels de sécurité et de performance.

## **Références**

1. [VMware vSphere Documentation](https://docs.vmware.com/en/VMware-vSphere/index.html)
2. [Enable Virtual Trusted Platform Module for an Existing Virtual Machine](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.vm_admin.doc/GUID-4DBF65A4-4BA0-4667-9725-AE9F047DE00A.html)
3. [National Institute of Standards and Technology (NIST)](https://www.nist.gov/)
4. [Windows 11 – autounattend.xml – BypassTPMCheck – BypassSecureBootCheck](https://iamroot.it/2021/10/06/windows-11-autounattend-xml-bypasstpmcheck-bypasssecurebootcheck/)
