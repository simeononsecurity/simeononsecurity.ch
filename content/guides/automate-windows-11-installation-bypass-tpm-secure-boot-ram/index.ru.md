---
title: "Автоматизация установки Windows 11: Обход проверок TPM, безопасной загрузки и оперативной памяти"
date: 2023-09-08
toc: true
draft: false
description: "Оптимизация установки Windows 11 в виртуальных средах за счет обхода проверок TPM, Secure Boot и оперативной памяти с помощью autounattend.xml и vTPM."
genre: ["Технология", "Windows 11", "Установка", "Виртуализация", "Автоматизация", "Ключи реестра", "Обходной путь TPM", "Обход безопасной загрузки", "Обход оперативной памяти", "vTPM"]
tags: ["Windows 11", "Установка", "Автоматизация", "Виртуализация", "vTPM", "Ключи реестра", "Обходной путь TPM", "Обход безопасной загрузки", "Обход оперативной памяти", "Autounattend.xml", "VMware vSphere", "Настройка Windows", "Среда предустановки Windows", "Виртуальная машина", "Обходной путь установки Windows", "Редактор реестра", "Настройка Microsoft Windows", "Системные требования", "Безопасность Windows", "Производительность Windows", "Государственное регулирование", "Соответствие требованиям NIST", "Microsoft", "ОС Windows", "Обход проверок", "Развертывание Windows", "Автоматизация настройки", "Командная строка", "Tech How-To", "Автоматизированная установка Windows 11", "Конфигурация vTPM в VMware vSphere", "Обход требований Windows 11"]
cover: "/img/cover/windows11-installation-cartoon.png"
coverAlt: " Изображение виртуальной машины, устанавливающей Windows 11 в виртуализированной среде, с улыбающимся ИТ-специалистом, наблюдающим за процессом."
coverCaption: "Упростите установку с помощью Smiles: Автоматизация установки Windows 11"
---

**Автоматизированная установка Windows 11 в виртуальных средах**.

## **Введение**

Windows 11 предъявляет новые системные требования, включая необходимость наличия TPM (Trusted Platform Module), Secure Boot и достаточного объема оперативной памяти. Хотя эти требования повышают безопасность и производительность, они могут создавать проблемы при установке Windows 11 в виртуальных средах без встроенной поддержки TPM. Однако существуют обходные пути, позволяющие обойти эти проверки и успешно установить Windows 11.

### **Обход проверок TPM, Secure Boot и оперативной памяти в Windows 11**.

В виртуальных средах, таких как VMware vSphere, можно использовать виртуальный TPM (vTPM) для эмуляции устройства TPM 2.0, что удовлетворяет требованию TPM для установки Windows 11. Однако в сценариях, где vTPM недоступен, для обхода проверок в процессе установки можно использовать следующие **ключи реестра**:

- **BypassTPMCheck**: Пропустить проверку TPM.
- **BypassSecureBootCheck**: Пропуск проверки Secure Boot.
- **BypassRAMCheck**: Пропустить проверку оперативной памяти.

```reg
[HKEY_LOCAL_MACHINE\SYSTEM\Setup\LabConfig]
"BypassTPMCheck"=dword:00000001
"BypassSecureBootCheck"=dword:00000001
"BypassRAMCheck"=dword:00000001
```

Чтобы вручную обойти проверки при **ручной установке**, выполните следующие действия:

1. При появлении сообщения "This PC can't run Windows 11" нажмите [Shift]+[F10], чтобы открыть командную строку.
2. С помощью команды **regedit** откройте редактор реестра.
3. Вручную добавьте вышеупомянутые значения реестра в раздел **HKEY_LOCAL_MACHINE\SYSTEM\Setup\LabConfig** со значением **dword:00000001**.
```powershell
# Create the LabConfig key if it doesn't exist
New-Item -Path "HKLM:\SYSTEM\Setup" -Name "LabConfig" -Force

# Set the registry values under LabConfig
Set-ItemProperty -Path "HKLM:\SYSTEM\Setup\LabConfig" -Name "BypassTPMCheck" -Value 1 -Type DWord
Set-ItemProperty -Path "HKLM:\SYSTEM\Setup\LabConfig" -Name "BypassSecureBootCheck" -Value 1 -Type DWord
Set-ItemProperty -Path "HKLM:\SYSTEM\Setup\LabConfig" -Name "BypassRAMCheck" -Value 1 -Type DWord
```
4. Выйдите из командной строки и закройте все оставшиеся диалоговые окна, чтобы продолжить настройку.

### **Автоматическая установка с использованием Autounattend.xml**

Для автоматической установки в виртуализированных средах можно использовать файл **autounattend.xml**, в котором задаются параметры конфигурации. Чтобы включить **Bypass Registry Keys** в файл autounattend.xml, используйте команду **RunSynchronous** следующим образом:

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

### **Пользуйтесь осторожностью и соблюдайте правила**.

**Обход** этих проверок должен осуществляться только в определенных сценариях, например, в виртуализированных средах, в которых приняты соответствующие меры безопасности. Необходимо **понимать последствия** обхода этих требований и оценивать потенциальные риски.

Необходимость использования TPM 2.0 и Secure Boot для установки Windows 11 основана на заявленных компанией Microsoft системных требованиях. В некоторых случаях, например, в государственных или регулируемых средах, обход этих проверок может не соответствовать определенным нормам или стандартам безопасности. Организациям следует тщательно изучить свои требования и обратиться к соответствующим нормативным документам, например, к документам правительственных агентств, таких как **Национальный институт стандартов и технологий (NIST)**, чтобы убедиться в их соответствии.



## **Вывод**

Выполнив описанные в этой статье действия, можно автоматизировать установку Windows 11 в виртуальных средах и обойти проверки TPM, Secure Boot и RAM с помощью программы `autounattend.xml` файл. Однако следует помнить об осторожности и понимать возможные последствия обхода этих важных проверок безопасности и производительности.

## **Ссылки**

1. [VMware vSphere Documentation](https://docs.vmware.com/en/VMware-vSphere/index.html)
2. [Enable Virtual Trusted Platform Module for an Existing Virtual Machine](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.vm_admin.doc/GUID-4DBF65A4-4BA0-4667-9725-AE9F047DE00A.html)
3. [National Institute of Standards and Technology (NIST)](https://www.nist.gov/)
4. [Windows 11 – autounattend.xml – BypassTPMCheck – BypassSecureBootCheck](https://iamroot.it/2021/10/06/windows-11-autounattend-xml-bypasstpmcheck-bypasssecurebootcheck/)
