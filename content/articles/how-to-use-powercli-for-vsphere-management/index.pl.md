---
title: "PowerCLI w zarządzaniu vSphere"
date: 2023-08-02
lastmod: 2026-11-12
toc: true
draft: false
description: "Poznaj PowerCLI do zarządzania VMware vSphere, automatyzacji zadań i zwiększania produktywności."
genre: ["Technologia", "Wirtualizacja", "VMware", "Zarządzanie IT", "Automatyzacja", "Interfejs wiersza poleceń", "Skrypty", "Administracja systemami", "Chmura obliczeniowa", "Zarządzanie centrum danych"]
tags: ["PowerCLI", "VMware PowerCLI", "Instalacja PowerCLI", "Zainstaluj PowerCLI", "Pobierz PowerCLI", "Pobieranie PowerCLI", "Połączenie PowerCLI z vCenter", "Zarządzanie vSphere", "Zarządzanie maszynami wirtualnymi", "Zarządzanie hostami", "Automatyzacja", "Skrypty", "Wirtualizacja", "Serwer vCenter", "Hosty ESXi", "Zarządzanie magazynami danych", "Zarządzanie kartami sieciowymi", "Tworzenie maszyn wirtualnych", "Usuwanie maszyn wirtualnych", "Ustawienia maszyn wirtualnych", "Zasoby hosta", "Przydział procesora", "Przydział pamięci", "Ustawienia pamięci masowej", "Przykłady PowerCLI", "Dokumentacja PowerCLI", "Zarządzanie IT", "Administracja systemami", "Chmura obliczeniowa"]
cover: "/img/cover/An_illustrated_cartoon_image_showcasing_a_pers.webp"
coverAlt: "Ilustracja przedstawia osobę używającą poleceń PowerCLI do zarządzania maszynami wirtualnymi i hostami w środowisku vSphere."
coverCaption: "Usprawnij zarządzanie vSphere dzięki PowerCLI"
---

## Wprowadzenie

**PowerCLI** to narzędzie **wiersza poleceń (CLI)** firmy **VMware**, które pozwala administratorom **zarządzać środowiskami VMware vSphere i automatyzować ich obsługę**. Liczne **cmdlety** upraszczają zadania administracyjne i poprawiają produktywność zarówno początkujących, jak i doświadczonych użytkowników. Artykuł omawia instalację, połączenie z vCenter i praktyczne użycie PowerCLI.

______

## Instalacja PowerCLI

Zainstaluj PowerCLI na komputerze:

1. **Pobierz** instalator z oficjalnej witryny VMware. Link znajduje się w [dokumentacji PowerCLI](https://code.vmware.com/web/dp/tool/vmware-powercli). Wybierz wersję odpowiednią dla systemu operacyjnego.
2. **Uruchom** instalator i postępuj zgodnie z instrukcjami. Wybierz lokalizację oraz opcje.
3. Kliknij „Finish”, aby zakończyć instalację. PowerCLI jest gotowe do użycia.

______

## Łączenie z vCenter przez PowerCLI

Po instalacji połącz się z serwerem vCenter, aby zarządzać infrastrukturą wirtualną za pomocą cmdletów PowerCLI.

1. Uruchom PowerCLI z menu Start lub skrótu na pulpicie.
2. Połącz się z vCenter tym poleceniem:

```powershell
Connect-VIServer -Server <vCenter IP or hostname>
```

Zastąp `<vCenter IP or hostname>` rzeczywistym adresem IP lub nazwą hosta serwera vCenter.

3. Podaj dane logowania konta z uprawnieniami wystarczającymi do administrowania vCenter.
4. Sprawdź połączenie prostym poleceniem, na przykład **Get-VMHost**. Lista hostów ESXi potwierdza połączenie.

______

## Zarządzanie vSphere za pomocą PowerCLI

Po połączeniu z vCenter możesz wykonywać typowe zadania.

### Pobieranie informacji

PowerCLI udostępnia cmdlety do pobierania informacji o środowisku vSphere:

- **Get-VM**: pobiera informacje o maszynach wirtualnych.
- **Get-VMHost**: pobiera informacje o hostach ESXi.
- **Get-Datastore**: pobiera informacje o magazynach danych.
- **Get-NetworkAdapter**: pobiera informacje o kartach sieciowych.

Używaj parametrów, aby filtrować i formatować wyniki.

### Automatyzacja zadań

PowerCLI automatyzuje powtarzalne zadania. Kilka wierszy kodu pozwala wykonywać złożone operacje na wielu obiektach.

#### Tworzenie migawek wszystkich maszyn w folderze

```PowerShell
## Power off all virtual machines on a specific host
Get-VMHost -Name "MyHost" | Get-VM | Stop-VM

## Take a snapshot of all virtual machines in a specific folder
Get-Folder -Name "MyFolder" | Get-VM | New-Snapshot -Name "DailySnapshot" -Description "Daily Backup"
```

Skrypt pokazuje, jak wyłączyć maszyny wirtualne na wskazanym hoście i utworzyć migawki maszyn z folderu.

#### Bezpieczne zamykanie wszystkich maszyn w folderze

```PowerShell
## Retrieve the folder containing the virtual machines to be shutdown
$folder = Get-Folder -Name "MyFolder"

## Retrieve all virtual machines within the specified folder
$vms = Get-VM -Location $folder

## Shutdown all virtual machines gracefully
foreach ($vm in $vms) {
    if ($vm.PowerState -eq "PoweredOn") {
        $vm | Shutdown-VMGuest -Confirm:$false
    }
}
```

Skrypt pobiera folder przez `Get-Folder`, a następnie maszyny z folderu przez `Get-VM`. Pętla `foreach` sprawdza każdą maszynę. Dla stanu „PoweredOn” polecenie `Shutdown-VMGuest` rozpoczyna prawidłowe zamykanie. `-Confirm:$false` pomija monit o potwierdzenie. W ten sposób maszyny zostają bezpiecznie wyłączone w uporządkowany sposób. Skrypty PowerCLI pozwalają dopasować automatyzację do własnych potrzeb.

### Zarządzanie maszynami wirtualnymi i hostami

PowerCLI obsługuje różne zadania administracyjne:

- **Tworzenie i usuwanie maszyn wirtualnych**: użyj **`New-VM`** i **`Remove-VM`**. **[cmdlet New-VM](https://developer.vmware.com/docs/powercli/latest/vmware.vimautomation.core/commands/new-vm/#DefaultParameterSet)** przy tworzeniu przyjmuje ustawienia procesora, pamięci, dysku i sieci.
- **Zmiana ustawień maszyn**: modyfikuj procesor, pamięć, dysk i sieć. **[cmdlet Set-VM](https://developer.vmware.com/docs/powercli/latest/vmware.vimautomation.core/commands/set-vm/#DefaultSet)** zmienia przydział procesora i pamięci.
- **Zarządzanie zasobami hosta**: administruj procesorem, pamięcią, siecią i pamięcią masową. **[cmdlet Set-VMHost](https://vdc-repo.vmware.com/vmwb-repository/dcr-public/e7c1a32c-a3c6-4d7c-91bb-18a86a38daf7/12353298-ce6e-4d3f-bd8d-ab9f5ab044cc/doc/Set-VMHost.html)** modyfikuje konfigurację sieci i pamięci hosta.

To tylko kilka przykładów. Rozbudowany zestaw cmdletów PowerCLI upraszcza i automatyzuje zadania administracyjne vSphere.

## Podsumowanie

**PowerCLI** to przydatne narzędzie do zarządzania środowiskami VMware vSphere i ich automatyzacji. Cmdlety upraszczają administrację i poprawiają produktywność. Po instalacji i połączeniu z vCenter możesz pobierać informacje, automatyzować zadania oraz efektywnie zarządzać maszynami wirtualnymi i hostami.

Poznaj PowerCLI, aby uprościć zarządzanie vSphere.


## Źródła
- [Dokumentacja PowerCLI](https://code.vmware.com/web/dp/tool/vmware-powercli)
- [Connect-VIServer: dokumentacja cmdletu VMware PowerCLI](https://docs.vmware.com/en/VMware-PowerCLI/latest/VMware.VimAutomation.Core/Connect-VIServer.html)
- [Get-VM: dokumentacja cmdletu VMware PowerCLI](https://developer.vmware.com/docs/powercli/latest/vmware.vimautomation.core/commands/get-vm/#Default)
