---
title: "Automatyzacja instalacji Windows 11: Obejście TPM, bezpiecznego rozruchu i kontroli pamięci RAM"
date: 2023-09-08
toc: true
draft: false
description: "Usprawnij instalację Windows 11 w środowiskach zwirtualizowanych, omijając kontrole TPM, Secure Boot i pamięci RAM za pomocą autounattend.xml i vTPM."
genre: ["Technologia", "Windows 11", "Instalacja", "Wirtualizacja", "Automatyzacja", "Klucze rejestru", "Obejście TPM", "Bezpieczne obejście rozruchu", "Obejście pamięci RAM", "vTPM"]
tags: ["Windows 11", "Instalacja", "Automatyzacja", "Wirtualizacja", "vTPM", "Klucze rejestru", "Obejście TPM", "Bezpieczne obejście rozruchu", "Obejście pamięci RAM", "Autounattend.xml", "VMware vSphere", "Konfiguracja systemu Windows", "Środowisko preinstalacji systemu Windows", "Maszyna wirtualna", "Obejście instalacji w systemie Windows", "Edytor rejestru", "Konfiguracja systemu Microsoft Windows", "Wymagania systemowe", "Bezpieczeństwo systemu Windows", "Wydajność systemu Windows", "Przepisy rządowe", "Zgodność z NIST", "Microsoft", "System operacyjny Windows", "Omijanie kontroli", "Wdrożenie w systemie Windows", "Automatyzacja ustawień", "Wiersz polecenia", "Porady techniczne", "Zautomatyzowana instalacja systemu Windows 11", "Konfiguracja vTPM w VMware vSphere", "Obejście wymagań systemu Windows 11"]
cover: "/img/cover/windows11-installation-cartoon.png"
coverAlt: " Obraz w stylu kreskówki przedstawiający maszynę wirtualną instalującą system Windows 11 w zwirtualizowanym środowisku z uśmiechniętym specjalistą IT nadzorującym proces."
coverCaption: "Uprość instalację dzięki Smiles: Automatyzacja instalacji systemu Windows 11"
---

**Automatyczna instalacja Windows 11 w środowiskach zwirtualizowanych**

**Wprowadzenie**

Windows 11 wprowadza nowe wymagania systemowe, w tym potrzebę posiadania modułu TPM (Trusted Platform Module), bezpiecznego rozruchu i wystarczającej ilości pamięci RAM. Chociaż wymagania te zwiększają bezpieczeństwo i wydajność, mogą stanowić wyzwanie podczas instalowania systemu Windows 11 w środowiskach zwirtualizowanych bez natywnej obsługi TPM. Istnieją jednak obejścia, które pozwalają ominąć te kontrole i pomyślnie zainstalować system Windows 11.

**Ominięcie kontroli TPM, Secure Boot i pamięci RAM w systemie Windows 11**.

Środowiska zwirtualizowane, takie jak VMware vSphere, mogą wykorzystywać wirtualny moduł TPM (vTPM) do emulacji urządzenia TPM 2.0, spełniając wymóg modułu TPM dla instalacji systemu Windows 11. Jednak w scenariuszach, w których vTPM nie jest dostępny, można użyć następujących **kluczy rejestru**, aby ominąć kontrole podczas procesu instalacji:

- **BypassTPMCheck**: Pomiń sprawdzanie TPM.
- **BypassSecureBootCheck**: Pomiń sprawdzanie Secure Boot.
- **BypassRAMCheck**: Pomiń sprawdzanie pamięci RAM.

```reg
[HKEY_LOCAL_MACHINE\SYSTEM\Setup\LabConfig]
"BypassTPMCheck"=dword:00000001
"BypassSecureBootCheck"=dword:00000001
"BypassRAMCheck"=dword:00000001
```

Aby ręcznie ominąć kontrole podczas **ręcznej instalacji**, wykonaj następujące kroki:

1. Po napotkaniu komunikatu "Ten komputer nie może uruchomić systemu Windows 11", naciśnij [Shift]+[F10], aby otworzyć wiersz polecenia.
2. Użyj polecenia **regedit**, aby otworzyć Edytor rejestru.
3. Ręcznie dodaj wyżej wymienione wartości rejestru pod **HKEY_LOCAL_MACHINE\SYSTEM\Setup\LabConfig** z wartością **dword:00000001**.
```powershell
# Create the LabConfig key if it doesn't exist
New-Item -Path "HKLM:\SYSTEM\Setup" -Name "LabConfig" -Force

# Set the registry values under LabConfig
Set-ItemProperty -Path "HKLM:\SYSTEM\Setup\LabConfig" -Name "BypassTPMCheck" -Value 1 -Type DWord
Set-ItemProperty -Path "HKLM:\SYSTEM\Setup\LabConfig" -Name "BypassSecureBootCheck" -Value 1 -Type DWord
Set-ItemProperty -Path "HKLM:\SYSTEM\Setup\LabConfig" -Name "BypassRAMCheck" -Value 1 -Type DWord
```
4. Wyjdź z wiersza poleceń i zamknij wszystkie pozostałe okna dialogowe, aby kontynuować konfigurację.

**Automatyczna instalacja przy użyciu pliku Autounattend.xml**.

W przypadku automatycznych instalacji w środowiskach zwirtualizowanych, plik **autounattend.xml** może być użyty do określenia ustawień konfiguracyjnych. Aby uwzględnić **Bypass Registry Keys** w pliku autounattend.xml, należy użyć polecenia **RunSynchronous** w następujący sposób:

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

### **Używaj ostrożności i przestrzegaj przepisów**

**Ominięcie** tych kontroli powinno być wykonywane tylko w określonych scenariuszach, takich jak środowiska zwirtualizowane, które mają odpowiednie środki bezpieczeństwa. Istotne jest, aby **zrozumieć konsekwencje** ominięcia tych wymagań i ocenić potencjalne ryzyko.

Potrzeba TPM 2.0 i Secure Boot do instalacji Windows 11 opiera się na wymaganiach systemowych określonych przez Microsoft. W niektórych przypadkach, na przykład w środowiskach rządowych lub regulowanych, pominięcie tych kontroli może być niezgodne z określonymi przepisami lub standardami bezpieczeństwa. Organizacje powinny dokładnie rozważyć swoje wymagania i skonsultować się z obowiązującymi przepisami, takimi jak te z agencji rządowych, takich jak **National Institute of Standards and Technology (NIST)**, aby zapewnić zgodność.



## **Wniosek**

Postępując zgodnie z krokami opisanymi w tym artykule, można zautomatyzować instalację systemu Windows 11 w środowiskach zwirtualizowanych i ominąć kontrole TPM, Secure Boot i pamięci RAM przy użyciu narzędzia `autounattend.xml` plik. Należy jednak pamiętać, aby postępować ostrożnie i rozumieć potencjalne konsekwencje pominięcia tych podstawowych kontroli bezpieczeństwa i wydajności.

## **Referencje**

1. [VMware vSphere Documentation](https://docs.vmware.com/en/VMware-vSphere/index.html)
2. [Enable Virtual Trusted Platform Module for an Existing Virtual Machine](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.vm_admin.doc/GUID-4DBF65A4-4BA0-4667-9725-AE9F047DE00A.html)
3. [National Institute of Standards and Technology (NIST)](https://www.nist.gov/)
4. [Windows 11 – autounattend.xml – BypassTPMCheck – BypassSecureBootCheck](https://iamroot.it/2021/10/06/windows-11-autounattend-xml-bypasstpmcheck-bypasssecurebootcheck/)
