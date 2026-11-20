---
title: "Migracja maszyny wirtualnej Hyper-V do Proxmox VE: odwracalna lista kontrolna"
date: 2026-10-11
lastmod: 2026-11-19
toc: true
draft: false
description: "Przenieś maszynę wirtualną Hyper-V do Proxmox VE przez eksport wyłączonego źródła, dopasowanie firmware, import dysków, odizolowany test rozruchu i plan wycofania."
genre: ["Wirtualizacja", "Administracja systemami", "Domowe laboratorium"]
tags: ["Migracja z Hyper-V do Proxmox", "Migracja Hyper-V", "Migracja Proxmox VE", "Import VHDX", "qm disk import", "Przełączenie maszyny wirtualnej", "Eksport Hyper-V", "Windows VM w Proxmox", "VirtIO w Proxmox", "Wycofanie VM", "Migracja UEFI", "Punkty kontrolne Hyper-V", "Wirtualny TPM", "Odzyskiwanie BitLocker", "Migracja domowego laboratorium"]
cover: "/img/cover/hyper-v-to-proxmox-migration-checklist.webp"
coverAlt: "Dysk przejeżdża przez most z niebieskiej szafy serwerowej do pomarańczowej, obok widać osobną drogę powrotną i tarczę przy celu."
coverCaption: "Zachowaj dostęp do źródłowej maszyny wirtualnej, dopóki nowy gość nie przejdzie kontroli przełączenia."
---

**Eksport Hyper-V** zachowuje pliki maszyny wirtualnej, natomiast Proxmox VE wymaga nowej konfiguracji gościa i zaimportowanych plików dysków wirtualnych VHDX. Udana kopia nie dowodzi, że gość się uruchomi ani będzie obsługiwał użytkowników. Ta lista prowadzi przez eksport zatrzymanego źródła, kontrolowany test rozruchu i przełączenie z określoną drogą powrotu.

<!--more-->

## Najważniejsze informacje

- **Zapisz konfigurację źródła:** przed eksportem zanotuj generację firmware, ścieżki dysków, punkty kontrolne, sieć i szyfrowanie.
- **Zatrzymaj zapisy:** wyłącz VM Hyper-V przed końcowym eksportem i pozostaw ją wyłączoną podczas testu w Proxmox.
- **Dopasuj rozruch:** Hyper-V generacji 1 używa starszego BIOS-u. Generacja 2 używa UEFI.
- **Sprawdź usługę:** przed wycofaniem źródła sprawdź dane, dostęp sieciowy, kopie zapasowe i stan gościa.

## Przygotowanie

Zaplanuj okno serwisowe i najpierw przetestuj procedurę na jednorazowej VM. Potrzebujesz uprawnień administratora w Hyper-V i Proxmox VE, miejsca na eksport oraz zweryfikowanej kopii zapasowej niezależnej od kopii migracyjnej. Zaplanuj czas na przesłanie wszystkich dysków wirtualnych i przetestowanie aplikacji gościa. Przestój zależy od rozmiaru dysku i szybkości transferu.

Procedura dotyczy typowej VM z dyskami wirtualnymi. **Maszyny osłonięte, dyski przekazywane bezpośrednio, dyski współdzielone, obciążenia klastrowe i licencje powiązane ze sprzętem** wymagają osobnych planów. Zapisz, kto podejmuje decyzję o przełączeniu i do kiedy można wycofać zmianę. Nie uruchamiaj obu kopii w sieci produkcyjnej z tą samą tożsamością maszyny.

| Informacja o źródle | Zastosowanie |
|---|---|
| **Generacja i firmware VM** | Wybór SeaBIOS lub OVMF w Proxmox |
| **Stan i szablon Secure Boot** | Dopasowanie zasad rozruchu i rejestracja zgodnych kluczy |
| **Dyski rozruchowe i danych** | Import wszystkich wymaganych dysków VHDX we właściwej kolejności |
| **Punkty kontrolne i pliki AVHDX** | Unikanie traktowania dysku różnicowego jak niezależnego dysku bazowego |
| **IP, DNS, MAC i VLAN** | Przywrócenie łączności bez powielania tożsamości |
| **vTPM i BitLocker** | Przygotowanie odzyskiwania przed zmianą sprzętu wirtualnego |
| **Usługi i sprawdzenie danych** | Określenie dowodów sukcesu i wycofania |

Generacja 1 używa starszego BIOS-u. Generacja 2 używa Ujednoliconego Rozszerzalnego Interfejsu Firmware (UEFI). **Plik AVHDX** to dysk różnicowy Hyper-V połączony z bazowym VHDX. **vTPM** to wirtualny Trusted Platform Module używany przez BitLocker i inne funkcje. **VLAN** to oddzielna sieć logiczna przesyłana przez współdzielony sprzęt sieciowy.

**SeaBIOS** zapewnia firmware starszego BIOS-u. **OVMF** zapewnia firmware UEFI. **VirtIO** to szybki interfejs urządzenia wirtualnego wymagający sterowników gościa. **initramfs** to wczesny system plików Linuksa, który ładuje sterowniki przed uruchomieniem głównego systemu.

## Zbierz dane maszyny wirtualnej w Hyper-V

Uruchom te polecenia tylko do odczytu w podwyższonej sesji PowerShell na hoście Hyper-V. To nieprzetestowane przykłady. Przed użyciem sprawdź każde polecenie względem zainstalowanego modułu Hyper-V i procedury zmian. Wpisz nazwę VM po wyświetleniu monitu:

```powershell
$vmName = Read-Host "Nazwa maszyny wirtualnej Hyper-V"
Get-VM -Name $vmName | Select-Object Name, State, Generation, ProcessorCount, MemoryAssigned
Get-VMHardDiskDrive -VMName $vmName | Select-Object ControllerType, ControllerNumber, ControllerLocation, Path
Get-VMSnapshot -VMName $vmName | Select-Object Name, CreationTime
Get-VMNetworkAdapter -VMName $vmName | Select-Object Name, SwitchName, MacAddress
```

[Moduł PowerShell Hyper-V](https://learn.microsoft.com/en-us/powershell/module/hyper-v/) opisuje te polecenia inwentaryzacyjne. Porównaj ścieżki dysków z ustawieniami VM i zanotuj podłączone obrazy ISO, dyski danych, przełączniki wirtualne, adresy statyczne oraz rezerwacje DHCP. Zapisz system operacyjny i wersje aplikacji gościa. Zweryfikuj kopię zapasową, odtwarzając kopię testową albo sprawdzając niedawny, udokumentowany wynik odtwarzania. Sama kopia plików bez testu odzyskiwania daje słabszy dowód.

W przypadku VM **generacji 2** zapisz też firmware i ustawienia zabezpieczeń:

```powershell
Get-VMFirmware -VMName $vmName | Format-List *
Get-VMSecurity -VMName $vmName | Format-List *
```

Zapisz stan **Secure Boot**, szablon i ustawienie vTPM. Dokumentacja Microsoft dotycząca [**`Get-VMFirmware`**](https://learn.microsoft.com/en-us/powershell/module/hyper-v/get-vmfirmware) ogranicza polecenie do generacji 2. [**`Get-VMSecurity`**](https://learn.microsoft.com/en-us/powershell/module/hyper-v/get-vmsecurity) wyświetla konfigurację zabezpieczeń VM. Nie uruchamiaj **`Get-VMFirmware`** dla gościa generacji 1. **Adres MAC** identyfikuje interfejs sieciowy. **DNS** mapuje nazwy na adresy. **DHCP** przydziela ustawienia sieci. **Dysk EFI** przechowuje ustawienia UEFI.

**Rozwiąż punkty kontrolne przed końcowym eksportem.** Microsoft informuje, że eksport Hyper-V zbiera pliki punktów kontrolnych oraz dyski VHDX. Usunięcie punktu kontrolnego w Hyper-V scala jego dysk różnicowy. Nigdy nie usuwaj pliku **`.avhdx`** z systemu plików, aby skasować punkt kontrolny. Jeśli scalanie się nie powiedzie albo łańcuch dysków będzie niekompletny, przerwij i zastosuj [wskazówki Microsoft dotyczące odzyskiwania punktów kontrolnych](https://learn.microsoft.com/en-us/troubleshoot/windows-server/virtualization/hyper-v-snapshots-checkpoints-differencing-disks). [Przewodnik Microsoft po punktach kontrolnych](https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/checkpoints) opisuje zwykłe usuwanie i scalanie.

W przypadku gościa Windows z **BitLockerem** lub **wirtualnym TPM** uzyskaj i sprawdź klucz odzyskiwania przed zmianą sprzętu wirtualnego. [Dokumentacja zabezpieczeń Hyper-V generacji 2](https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/generation-2-virtual-machine-security-features) opisuje szyfrowanie oparte na vTPM. [Często zadawane pytania Microsoft dotyczące BitLockera](https://learn.microsoft.com/en-us/windows/security/information-protection/bitlocker/bitlocker-key-management-faq) wyjaśniają, dlaczego zmiana rozruchu wywołuje odzyskiwanie. Nowe urządzenie TPM w Proxmox nie odtwarza starego stanu TPM. Przechowuj klucz poza wyeksportowaną VM.

## Eksportuj zatrzymaną VM

Prawidłowo zamknij gościa. Potwierdź, że Hyper-V pokazuje **Off** (wyłączona), a nie Saved (zapisana). Poczekaj na zakończenie scalania punktów kontrolnych, a następnie wyeksportuj VM do lokalizacji z odpowiednią ilością wolnego miejsca. W Hyper-V Manager kliknij VM prawym przyciskiem, wybierz **Export** (eksportuj) i wskaż miejsce docelowe. Odpowiednik PowerShell:

```powershell
$vmName = Read-Host "Nazwa zatrzymanej maszyny Hyper-V"
$exportPath = Read-Host "Katalog docelowy eksportu"
$vm = Get-VM -Name $vmName -ErrorAction Stop
if ($vm.State -ne 'Off') { throw "Zatrzymaj VM i poczekaj, aż Hyper-V pokaże Off (wyłączona) przed eksportem." }
Export-VM -Name $vmName -Path $exportPath
```

[Przewodnik eksportu Microsoft](https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/deploy/export-and-import-virtual-machines) informuje, że eksport obejmuje dyski wirtualne, konfigurację i pliki punktów kontrolnych. Dokumentacja [**`Export-VM`**](https://learn.microsoft.com/en-us/powershell/module/hyper-v/export-vm) opisuje polecenie. Potwierdź obecność oczekiwanych plików dysków i ich rozmiary. Zachowaj wyłączoną źródłową VM i niezależną kopię zapasową. **Nie modyfikuj wyeksportowanych plików podczas importu.**

Przenieś pliki VHDX do lokalizacji dostępnej z hosta Proxmox. Traktuj eksport jako poufne dane gościa. Użyj szyfrowanego transferu, ogranicz dostęp do lokalizacji transferu i magazynu docelowego, a po walidacji usuń kopie tymczasowe. Sprawdź wolne miejsce w obu lokalizacjach. Zachowaj niezmieniony eksport na potrzeby wycofania. Jeśli eksport zawiera pliki **`.avhdx`**, nie wybieraj bazowego **`.vhdx`** tylko na podstawie nazwy i nie zakładaj, że zawiera najnowsze zapisy. Przed kontynuacją rozwiąż łańcuch dysków w Hyper-V.

## Utwórz docelową maszynę wirtualną w Proxmox

W interfejsie WWW Proxmox utwórz nową VM z zapisanym typem systemu gościa, procesorem i pamięcią. Wybierz nowy, nieużywany identyfikator VM. Nie instaluj nowego systemu operacyjnego. Przed importem dysku źródłowego usuń pusty dysk utworzony przez kreator. Przy pierwszym uruchomieniu odłącz kartę sieciową od mostu produkcyjnego lub podłącz ją do odizolowanej sieci testowej.

| Źródło Hyper-V | Cel Proxmox |
|---|---|
| **Generacja 1, starszy BIOS** | SeaBIOS |
| **Generacja 2, UEFI** | OVMF z dyskiem EFI i dopasowaną polityką Secure Boot |
| **Dysk rozruchowy Windows bez sterownika magazynu VirtIO** | Początkowo podłącz jako SATA |
| **Windows z vTPM lub BitLockerem** | W razie potrzeby nowe urządzenie stanu TPM, klucz odzyskiwania gotowy przed pierwszym uruchomieniem |

[Przewodnik Microsoft po generacjach VM](https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/plan/Should-I-create-a-generation-1-or-2-virtual-machine-in-Hyper-V) mapuje generację 1 na starszy BIOS, a generację 2 na UEFI. [Dokumentacja VM Proxmox](https://github.com/proxmox/pve-docs/blob/master/qm.adoc) opisuje SeaBIOS, OVMF i dysk EFI przechowujący ustawienia UEFI. **Dopasuj tryb rozruchu źródła.** Zmiana podczas migracji tworzy kolejny problem do zdiagnozowania.

Dla źródła generacji 2 zachowaj informację, czy **Secure Boot** był włączony. Sprawdź szablon źródła i wybierz zgodne, zarejestrowane klucze dla gościa. Nazwy szablonów Hyper-V nie przenoszą się do Proxmox. Dysk EFI Proxmox 4 MB i opcja **Pre-Enroll keys** (wstępna rejestracja kluczy) zapewniają klucze Secure Boot i domyślnie włączają tę funkcję. Przed przełączeniem sprawdź rozruch celu. [Dokumentacja firmware Microsoft](https://learn.microsoft.com/en-us/powershell/module/hyper-v/set-vmfirmware) opisuje wymagania szablonu źródła. [Dokumentacja dysku EFI Proxmox](https://github.com/proxmox/pve-docs/blob/master/qm.adoc) opisuje klucze celu.

Przed zmianą kluczy EFI potwierdź, że klucz odzyskiwania jest przechowany i zapisz obecne identyfikatory protectorów. Zgodnie z dokumentacją zainstalowanego Proxmox VE i OVMF zarejestruj klucze EFI. Ponownie sprawdź klucz odzyskiwania i uruchom `manage-bde -status` przed pierwszym startem. Nie zawieszaj, nie wyłączaj ani nie usuwaj protectorów jako ogólnego kroku migracji. Zapisz wersję pakietu firmware, stan Secure Boot i wersję firmware oraz stan BitLockera.

Jeśli źródło używa **vTPM**, przed pierwszym uruchomieniem dodaj **TPM State** (stan TPM) w panelu Hardware (sprzęt) Proxmox. Wybierz **wersję 2.0**, chyba że istnieje udokumentowane wymaganie wersji 1.2. Tworzy to nowy stan TPM, a nie kopię vTPM Hyper-V. Gość z BitLockerem potrzebuje sprawdzonego klucza odzyskiwania przy pierwszym starcie. [Dokumentacja TPM Proxmox](https://github.com/proxmox/pve-docs/blob/master/qm.adoc) opisuje operację Hardware (sprzęt) i dostępne wersje.

W Windows zacznij od dysku rozruchowego SATA, chyba że gość ma już wymagany sterownik magazynu VirtIO. Po udanym uruchomieniu zainstaluj obsługiwane sterowniki VirtIO i zmieniaj po jednym urządzeniu wirtualnym. Proxmox zaleca VirtIO SCSI ze względu na wydajność, ale bez sterownika rozruchowego Windows nie uzyska dostępu do dysku systemowego. W Linuksie sprawdź, czy initramfs zawiera docelowy sterownik magazynu, zanim zmienisz magistralę. [Dokumentacja VM Proxmox](https://github.com/proxmox/pve-docs/blob/master/qm.adoc) opisuje kontrolery dysków.

## Importuj i podłącz dyski

Na hoście Proxmox sprawdź skopiowaną ścieżkę VHDX. Poniższy przykład importuje dysk dla identyfikatora VM **230** do magazynu o identyfikatorze **`local-lvm`**. Zastąp wszystkie trzy wartości:

```bash
qm disk import 230 /path/to/exported/boot.vhdx local-lvm
```

Dokumentacja Proxmox dla [**`qm disk import`**](https://github.com/proxmox/pve-docs/blob/master/generated/qm.1-synopsis.adoc) mówi, że obraz źródłowy jest importowany jako **nieużywany dysk**. [Dokumentacja obrazów QEMU](https://www.qemu.org/docs/master/system/images) wymienia VHDX jako obsługiwany format konwersji. Importuj oddzielnie każdy dysk danych. Poczekaj na zakończenie każdego zadania i porównaj rozmiary z inwentaryzacją źródła.

W panelu **Hardware** (sprzęt) VM podłącz nieużywany dysk rozruchowy jako **SATA** na potrzeby pierwszego rozruchu Windows. Podłącz dyski danych w zapisanej kolejności. W **Options > Boot Order** (Opcje > kolejność rozruchu) wybierz dysk rozruchowy. W przypadku gościa generacji 2 sprawdź **OVMF** i dysk EFI. Zachowaj pliki importu i źródłową VM do czasu zakończenia walidacji.

## Przetestuj przed przełączeniem

Uruchom gościa Proxmox w odizolowanej sieci. W konsoli sprawdź ekran rozruchu, logowanie do systemu, woluminy, dane aplikacji i dzienniki usługi. Sam ekran logowania nie dowodzi sukcesu migracji. Wykonaj kontrole zapisane przed eksportem, w tym reprezentacyjną transakcję lub odczyt aktualnych danych.

Jeśli gość używa BitLockera i pojawi się monit, odblokuj go kluczem odzyskiwania. Po uruchomieniu Windows sprawdź stan ochrony woluminu systemowego oraz protectory w podwyższonym wierszu polecenia:

```powershell
manage-bde -status C:
manage-bde -protectors -get C:
```

[Przewodnik operacyjny BitLocker Microsoft](https://learn.microsoft.com/en-us/windows/security/operating-system-security/data-protection/bitlocker/operations-guide) opisuje sprawdzanie protectorów i tworzenie kopii kluczy. Wynik zawiera poufne dane odzyskiwania. Nie wklejaj go do zgłoszenia ani publicznego dziennika. Sprawdź wymagany protector i zgodnie z polityką zachowaj aktualną metodę odzyskiwania. Uruchom ponownie gościa i przed przełączeniem potwierdź, że nie pojawia się kolejny monit odzyskiwania. Powtarzające się monity oznaczają niezaliczony test migracji, a nie powód do odrzucenia oryginalnego klucza.

| Sprawdzenie | Warunek zaliczenia |
|---|---|
| **Rozruch i dyski** | Gość uruchamia się i montuje wszystkie oczekiwane woluminy |
| **Secure Boot i BitLocker** | Obowiązuje właściwa polityka rozruchu, a szyfrowany gość uruchamia się ponownie bez kolejnych żądań odzyskiwania |
| **Aplikacja** | Reprezentacyjny odczyt lub transakcja kończy się powodzeniem |
| **Sieć** | Wymagane urządzenia docierają do testowego gościa na określonych portach |
| **Odzyskiwanie** | Kopia Proxmox i odizolowany test odtworzenia działają przed wycofaniem źródła |
| **Operacje** | Monitorowanie, synchronizacja czasu, zamykanie i agent gościa działają zgodnie z założeniami |

Po pomyślnych testach aplikacji zmień trasę lub adres sieci produkcyjnej w oknie serwisowym. Pozostaw Hyper-V wyłączony. Nowa wirtualna karta sieciowa może wymagać nowej rezerwacji DHCP albo poprawienia statycznego adresu w gościu. Z osobnego klienta sprawdź DNS, reguły zapory i zależne usługi. [Dokumentacja VM Proxmox](https://github.com/proxmox/pve-docs/blob/master/qm.adoc) opisuje urządzenia sieciowe i opcje agenta gościa.

## Rozwiązywanie problemów i wycofanie

| Objaw | Pierwsza kontrola |
|---|---|
| **Brak urządzenia rozruchowego** | Kolejność rozruchu, zaimportowany dysk, tryb BIOS/UEFI i klucze Secure Boot |
| **Błąd magazynu Windows** | Podłączenie SATA i brakujący sterownik magazynu VirtIO |
| **Powtarzający się monit BitLocker** | Nowy stan TPM, polityka Secure Boot, pomiary rozruchu i protectory |
| **Gość uruchamia się bez sieci** | Nowa karta wirtualna, bridge, VLAN, rezerwacja DHCP i adres statyczny |
| **Stare lub brakujące dane** | Zły VHDX, niepełny eksport, łańcuch punktów kontrolnych lub brakujący dysk danych |

Jeśli wymagany test nie powiedzie się przed terminem wycofania, zatrzymaj VM Proxmox i odłącz jej sieć produkcyjną. Przywróć trasę sieciową źródła i uruchom oryginalną VM Hyper-V. **Nigdy nie uruchamiaj obu kopii z tą samą tożsamością produkcyjną.** Zapisz operacje zapisu przyjęte przez kopię Proxmox przed powrotem do Hyper-V. Wymagają one osobnego odzyskania lub uzgodnienia, bo dysk źródłowy ich nie otrzymał.

Zachowaj źródłową VM i eksport do czasu, aż gość Proxmox przejdzie test usług, otrzyma nową kopię zapasową i przejdzie odizolowany test odtworzenia oraz ustalony okres obserwacji. [Porównanie platform wirtualizacji w witrynie](/articles/vmware-esxi-citrix-xenserver-hyper-v-comparison/) pomaga wybrać platformę. [Przewodnik aktualizacji Proxmox VE 8 do 9](/articles/proxmox-ve-8-to-9-upgrade-guide/) opisuje późniejsze zadanie serwisowe. **Migracja kończy się, gdy obciążenie i ścieżka odzyskiwania działają na nowym hoście, a nie po samym imporcie dysku.**

## Kolejne kroki

Zachowaj źródłową VM i eksport, dopóki kontrole obciążenia, kopii zapasowej i wycofania nie przejdą w uzgodnionym okresie obserwacji. Przed wycofaniem źródła zapoznaj się z [testem odtwarzania kopii VM Proxmox](/articles/proxmox-vm-backup-restore-drill/).
