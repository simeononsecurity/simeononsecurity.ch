---
title: "Proxmox VE 9: ogranicz zużycie dysków wirtualnych i odzyskaj miejsce"
date: 2026-11-09
lastmod: 2026-11-20
toc: true
draft: false
description: "Ogranicz zużycie pamięci masowej przez VM i kontenery LXC w Proxmox VE 9. Porównaj formaty i backendy, włącz discard, uruchom trim i sprawdź migawki przed odzyskaniem miejsca."
genre: ["Wirtualizacja", "Administracja Linuksem", "platforma Proxmox VE", "Pamięć masowa", "Domowe laboratorium"]
tags: ["miejsce na dysku Proxmox VE 9", "cienkie przydzielanie miejsca Proxmox", "powiadomienia discard Proxmox", "polecenie TRIM Proxmox", "Windows ReTrim w Proxmox", "Linux fstrim w Proxmox", "użycie dysku LXC Proxmox", "cienkie przydzielanie LVM Proxmox", "rzadki zvol ZFS Proxmox", "urządzenia blokowe Ceph RBD Proxmox", "format qcow2 Proxmox", "dysk raw Proxmox", "migawki Proxmox", "odzyskiwanie miejsca na dysku wirtualnym", "typy pamięci Proxmox", "kontroler VirtIO SCSI", "wykrywanie zapisu zer Proxmox", "pamięć kopii zapasowych Proxmox"]
cover: "/img/cover/proxmox-ve-9-virtual-disk-space-reclamation.webp"
coverAlt: "Dwie siatki bloków połączone strzałką pokazują używane bloki dysku wirtualnego i wolną pojemność puli pamięci masowej."
coverCaption: "Usunięcie plików w gościu, wysłanie discard i odzyskanie miejsca to osobne kroki."
---

**Mniejszy system plików gościa nie zawsze oznacza mniejsze zużycie pamięci masowej Proxmox.** Zwolnienie miejsca na hoście wymaga dysku obsługującego thin provisioning, sprawnej ścieżki discard dla VM oraz backendu bez bloków zatrzymanych przez migawki. Ten poradnik opisuje ustawienia i kontrole dla VM oraz kontenerów LXC w Proxmox VE 9.

<!--more-->

## Najważniejsze informacje

- **Najpierw wybierz backend.** Deklarowany rozmiar dysku wirtualnego różni się od miejsca przydzielonego na hoście tylko wtedy, gdy format obrazu lub backend obsługuje thin provisioning.
- **Włącz discard dla VM, a potem uruchom trim w gościu.** Windows ReTrim i Linux `fstrim` przekazują żądania dotyczące nieużywanych bloków przez dysk wirtualny.
- **Osobno sprawdź migawki i kopie zapasowe.** Stare bloki pozostają przydzielone, dopóki odwołuje się do nich migawka. Pliki kopii i fragmenty PBS podlegają osobnym zasadom retencji.
- **Rozróżniaj typy montowań LXC.** Zarządzane woluminy rootfs i punkty montowania, bind mounty oraz montowania urządzeń różnią się właścicielem i sposobem tworzenia kopii.

## Zanim zaczniesz

Potrzebujesz **uprawnień administratora Proxmox VE 9**, sprawdzonej kopii zapasowej każdego gościa oraz odpowiedniej ilości wolnego miejsca w puli. Przed zmianą ustawień zanotuj identyfikator gościa, magistralę dysku, identyfikator woluminu i pamięci, migawki oraz bieżące przydzielenie miejsca. Użyj [testu odtwarzania VM](/articles/proxmox-vm-backup-restore-drill/), aby sprawdzić odzyskiwanie.

**Szacowany czas:** od 20 do 60 minut na gościa, plus dłuższe zadania trim lub czyszczenia. **Poziom trudności:** Średni. Zacznij od VM o niskim ryzyku i porównaj użycie pamięci przed zmianą i po niej.

> **Ostrzeżenie:** Pełna pula thin powoduje błędy wejścia/wyjścia w gościach i grozi uszkodzeniem systemów plików. Nie przydzielaj więcej miejsca, niż jest dostępne, bez monitorowania wolnej przestrzeni na dane i metadane puli. [Dokumentacja pamięci masowej Proxmox](https://github.com/proxmox/pve-docs/blob/master/pvesm.adoc)

## Prześledź łańcuch przydzielania miejsca

**Usuwanie**, **discard** i **odzyskiwanie** zachodzą na różnych warstwach. Gość usuwa plik i oznacza jego bloki systemu plików jako wolne. System plików wysyła dla nich TRIM lub UNMAP. QEMU przekazuje żądanie, jeśli na dysku wirtualnym włączono discard. Backend zwalnia fizycznie przydzielone bloki, jeśli jego format i pula obsługują tę operację. [Dokumentacja dysków VM Proxmox](https://github.com/proxmox/pve-docs/blob/master/qm.adoc)

| Warstwa | Co sprawdzić | Przydatne dane |
|---|---|---|
| **Pliki gościa** | Wolne miejsce w systemie plików | Właściwości woluminu Windows lub Linux `df -h` |
| **Dysk wirtualny** | Magistrala, discard, emulacja SSD, format obrazu | Karta VM **Hardware** lub `qm config VMID` |
| **Wolumin PVE** | Właściciel i skonfigurowany rozmiar | Karta **Content** pamięci masowej lub `pvesm list STORAGE_ID` |
| **Pula pamięci** | Wolne dane i metadane, zachowane bloki | `pvesm status` i narzędzia backendu |

**Dysk wirtualny o pojemności 100 GiB wyznacza limit, ale nie gwarantuje przydzielenia 100 GiB.** Z kolei informacja gościa o użyciu 20 GiB nie dowodzi, że host wykorzystuje 20 GiB. Metadane, migawki, kopie zapasowe i wcześniej zapisane bloki zmieniają wynik. [Dokumentacja pamięci masowej Proxmox](https://github.com/proxmox/pve-docs/blob/master/pvesm.adoc)

## Porównaj formaty dysków

**Backend pamięci masowej decyduje o dostępnych formatach obrazów.** zvol ZFS i Ceph RBD używają wirtualnych dysków raw. LVM zwykle używa raw, z wyjątkiem łańcuchów woluminów w Proxmox VE 9 opisanym poniżej. Pamięci plikowe, takie jak directory i NFS, obsługują raw lub qcow2. Sam format raw nie zapewnia przydzielania thin ani migawek. Te funkcje musi zapewniać pamięć bazowa. Qcow2 obsługuje przydzielanie metodą copy-on-write i migawki na poziomie obrazu. [Dokumentacja dysków VM Proxmox](https://github.com/proxmox/pve-docs/blob/master/qm.adoc)

| Format | Mechanizm przydzielania | Koszt pamięci |
|---|---|---|
| **qcow2 na pamięci plikowej** | Qcow2 przydziela klastry podczas zapisu | Metadane obrazu i łańcuchy migawek zajmują miejsce |
| **Plik raw na pamięci plikowej** | Obsługa plików rzadkich przez system plików, jeśli dostępna | Sam raw nie zapewnia thin provisioning ani migawek |
| **Wolumin blokowy raw** | LVM thin, ZFS, Ceph RBD lub inna pamięć bazowa | Przydzielanie miejsca puli i migawki zależą od backendu |

**Proxmox VE 9 thick LVM ma specjalny tryb migawek.** `snapshot-as-volume-chain` używa relacji qcow2 backing między woluminami logicznymi thick LVM. Nie korzysta z wewnętrznych migawek qcow2. Opcja dotyczy tylko nowych dysków VM i według aktualnej dokumentacji Proxmox pozostaje wersją technologiczną do testów. PVE pokazuje każdą migawkę jako w pełni przydzieloną. Rzeczywiste przydzielenie miejsca w SAN jest mniejsze tylko wtedy, gdy pamięć bazowa obsługuje thin provisioning i discard. [Dokumentacja pamięci LVM Proxmox](https://github.com/proxmox/pve-docs/blob/master/pve-storage-lvm.adoc)

**Nie konwertuj dysku tylko dlatego, że ma rozszerzenie `.raw`.** Najpierw sprawdź wtyczkę pamięci i przydzielone bloki. Dysk raw na `local-lvm` jest przydzielany inaczej niż w pełni przydzielony plik raw na zwykłej pamięci directory.

## Porównaj typy pamięci masowej

Proxmox rozdziela **pamięć plikową** i **pamięć blokową**. Wtyczka steruje też migawkami, klonami, współdzieleniem i typami zawartości akceptowanymi przez pulę. Sprawdź wpis **Datacenter > Storage**, zanim zaczniesz polegać na formacie lub funkcji. [Tabela typów pamięci Proxmox](https://github.com/proxmox/pve-docs/blob/master/pvesm.adoc)

| Pamięć masowa | Zachowanie dysku VM | Kontrola odzyskiwania |
|---|---|---|
| **Directory, ext4, XFS** | Pliki raw lub qcow2 | Porównaj bajty przydzielone według `du` z pojemnością wirtualną obrazu. Sprawdź migawki, jeśli zapewnia je inna warstwa. |
| **NFS, CIFS** | Pliki raw lub qcow2 na współdzielonej pamięci | Sprawdź miejsce przydzielone na serwerze. Wynik trim gościa nie dowodzi, że serwer zwolnił miejsce. |
| **LVM z cienkim przydziałem (`local-lvm`)** | Lokalne woluminy logiczne raw thin | Monitoruj `lvs` i procent wykorzystania danych oraz metadanych puli thin. |
| **LVM thick** | LV raw lub łańcuchy woluminów qcow2 VE 9 | Usunięcie plików w gościu nie zmniejsza stałej rezerwacji LV. Osobno sprawdź alokację thin w SAN. |
| **Magazyn ZFS (`local-zfs`)** | zvol raw lub podwoluminy kontenerów | Sprawdź `sparse`, właściwości zbioru danych, użycie puli i migawki. |
| **Ceph RBD** | Obrazy RBD raw thin na współdzielonej pamięci | Sprawdź pojemność puli Ceph, użycie obrazu, migawki i discard. |
| **Btrfs** | Woluminy plikowe z podwoluminami Btrfs dla obrazów raw | Traktuj wtyczkę Btrfs PVE jako wersję technologiczną do testów i sprawdź migawki oraz użycie systemu plików. |

**Inne wtyczki pamięci masowej mają odmienne zastosowania.** CephFS zapewnia współdzieloną pamięć plikową. iSCSI i Fibre Channel udostępniają współdzielone urządzenia blokowe, często dzielone przez LVM na woluminy VM. ZFS over iSCSI wykorzystuje zdalną pamięć blokową opartą na ZFS. Proxmox Backup Server (PBS) przechowuje kopie zapasowe, a nie aktywne dyski VM. Sprawdź włączone typy **Content**, zanim umieścisz tam dane `images`, `rootdir`, `backup` lub `iso`. [Tabela typów pamięci Proxmox](https://github.com/proxmox/pve-docs/blob/master/pvesm.adoc)

**Flagi alokacji pamięci plikowej mają znaczenie podczas tworzenia dysku.** Ustawienie `format` wybiera `raw`, `qcow2` lub `vmdk`, jeśli są obsługiwane. `preallocation` dla plików raw i qcow2 przyjmuje `off`, `metadata`, `falloc` lub `full`. Domyślna wartość to `metadata`, traktowana jako `off` dla raw. `full` rezerwuje miejsce z góry i likwiduje typowy mały początkowy ślad pliku. Przed utworzeniem dużego dysku sprawdź konfigurację pamięci. Flaga `shared` tylko deklaruje istniejący dostęp współdzielony. Nie udostępnia lokalnej pamięci. [Wspólne właściwości pamięci Proxmox](https://github.com/proxmox/pve-docs/blob/master/pvesm.adoc)

**ZFS `sparse` to ustawienie tworzenia zvol thin.** Bez sparse zvol utworzenie rezerwuje miejsce zgodnie z konfiguracją woluminu. Przed zmianą istniejącego wdrożenia sprawdź ustawienia pamięci i puli. [Dokumentacja pamięci ZFS Proxmox](https://github.com/proxmox/pve-docs/blob/master/pve-storage-zfspool.adoc)

**Pamięć directory wymaga dodatkowej kontroli.** Logiczna długość pliku qcow2 nie jest pojemnością wirtualną widoczną dla gościa. `du -h` podaje bloki systemu plików przydzielone obrazowi. `ls -lh` pokazuje logiczną długość pliku. Dla zatrzymanej VM `qemu-img info` podaje pojemność wirtualną i rozmiar na hoście. W przypadku NFS przy podejmowaniu decyzji o pojemności korzystaj z pomiarów serwera. [Dokumentacja QEMU `qemu-img`](https://www.qemu.org/docs/master/tools/qemu-img.html)

**NFS ma kolejną granicę alokacji.** Ponowne użycie pustego klastra w pliku qcow2 nie oznacza, że serwer NFS zwalnia bloki tego pliku. Hole punching wymaga obsługi przez klienta, uzgodniony protokół, serwer i jego system plików. NFSv4.2 definiuje `DEALLOCATE`, ale sam numer wersji nie dowodzi, że serwer oddał miejsce. Sprawdź uzgodnione montowanie NFS i zmierz alokację na serwerze. [Specyfikacja NFSv4.2 `DEALLOCATE`](https://www.rfc-editor.org/rfc/rfc7862.html#section-6.2.2)

## Ustaw flagi dysku VM

W interfejsie Proxmox otwórz **VM > Hardware > Hard Disk > Edit**. Sprawdź magistralę dysku i opcje zaawansowane. Poniższe flagi wpływają na alokację lub określają, czy optymalizacja będzie przydatna. [Oficjalna dokumentacja opcji `qm`](https://github.com/proxmox/pve-docs/blob/master/generated/qm.conf.5-opts.adoc) podaje ich dostępność dla poszczególnych magistral.

| Magistrala | Ustawienie związane z miejscem |
|---|---|
| **IDE** | Zgodność ze starszymi systemami. Używaj tylko, jeśli gość nie ma nowszego sterownika. |
| **SATA** | Szeroko obsługiwana emulacja. Przed poleganiem na odzyskiwaniu sprawdź trim gościa i opcje dysku. |
| **SCSI z VirtIO SCSI** | Zalecana nowoczesna ścieżka discard i ustawień dysku. Windows wymaga sterownika VirtIO. |
| **VirtIO Block** | Dysk parawirtualizowany. Discard w Linuksie wymaga jądra 5.0 lub nowszego. Brak emulacji SSD. |

| Ustawienie | Efekt | Zalecenie |
|---|---|---|
| **Przekazuj discard (`on`)** | Przekazuje TRIM lub UNMAP gościa | Wymagane do odzyskiwania miejsca z gościa na zgodnym backendzie thin. Domyślne `ignore` blokuje przekazywanie. |
| **Emulacja SSD `ssd=1`** | Przedstawia dysk gościowi jako SSD | Niektóre systemy wymagają tego oznaczenia, by wysyłać trim. Flaga nie przyspiesza fizycznej pamięci. VirtIO Block jej nie ma. |
| **Detect zeroes `detect_zeroes=1`** | Wykrywa i próbuje optymalizować zapisy zer | Opcjonalna optymalizacja I/O. Nie zastępuje trim ani nie gwarantuje odzyskania miejsca. |
| **Magistrala: SCSI / VirtIO SCSI single** | Udostępnia dysk SCSI przez kontroler VirtIO | Praktyczny wybór dla nowoczesnych gości Windows i Linux. Zainstaluj sterowniki VirtIO dla Windows. |
| **Magistrala: VirtIO Block** | Używa urządzenia blokowego VirtIO | Discard w Linuksie wymaga jądra 5.0 lub nowszego. Brak emulacji SSD. |
| **Wątek I/O `iothread=1`** | Przydziela operacje dyskowe osobnemu wątkowi | Używaj z VirtIO Block lub SCSI na kontrolerze VirtIO SCSI single. To ustawienie wydajności, nie odzyskiwania miejsca. |
| **Cache i AIO** | Zmieniają buforowanie i asynchroniczne I/O | Dostosuj do obciążenia i backendu. Żadne z nich nie zmniejsza dysku. |
| **Backup `backup=0`** | Wyklucza dysk z kopii VM | Zmniejsza zakres kopii i usuwa dane dysku z odzyskiwania VM. Udokumentuj osobną kopię. |
| **Replikacja `replicate=0`** | Wyklucza dysk z replikacji pamięci | Zmniejsza ilość replikowanych danych i usuwa dysk z repliki. |

**Pozostałe opcje dysku opisują jego zachowanie, a nie odzyskiwanie miejsca.** `format` ma znaczenie przy przydzielaniu dysku na backendzie obsługującym kilka formatów. `size` to pojemność wirtualna, nie przydzielone bajty. `ro=1` ustawia tylko do odczytu. `snapshot=1` włącza tymczasowy tryb migawki QEMU, który odrzuca zmiany dysku po wyłączeniu VM. Nie jest to opcja do uwzględniania dysku w migawkach VM Proxmox. Unikaj jej dla trwałych danych. Przed użyciem `backup=0` lub `replicate=0` sprawdź zakres odzyskiwania. [Opcje dysków VM Proxmox](https://github.com/proxmox/pve-docs/blob/master/generated/qm.conf.5-opts.adoc)

**Nie wklejaj skróconego polecenia `qm set --scsi0` na istniejącym dysku.** Sprawdź **`qm config VMID`** i zachowaj pełny identyfikator woluminu oraz istniejące opcje. Skrócone przypisanie grozi usunięciem innych ustawień dysku. Po każdej zmianie sprawdź zapisane opcje w interfejsie.

```bash
qm config 100
pvesm status
```

`100` to przykładowy identyfikator VM. Poniższe polecenie pokazuje składnię przydzielania **nowego** dysku SCSI o rozmiarze 64 GiB do istniejącej VM z kontrolerem **VirtIO SCSI single** i wymaganym sterownikiem w gościu. Zastąp oba identyfikatory VM i pamięci własnymi wartościami.

```bash
qm set 100 --scsi0 local-lvm:64,discard=on,ssd=1,iothread=1
```

**Przed użyciem przykładu sprawdź, czy `scsi0` już istnieje.** Polecenie zmienia to gniazdo. Przy istniejącym dysku użyj interfejsu, jeśli łatwiej zachować w nim dokładny ciąg opcji. Zobacz [dokumentację polecenia Proxmox `qm`](https://github.com/proxmox/pve-docs/blob/master/generated/qm.1-synopsis.adoc).

## Oczyść pliki systemu gościa

**Najpierw zwolnij pliki w gościu.** Sprawdź ustawienia pamięci Windows, pliki tymczasowe, stare instalatory, pamięci podręczne aplikacji i kosz. Czyść bazy danych i środowiska kontenerów za pomocą ich własnych interfejsów. Usuwanie aktywnych danych aplikacji tylko po to, by zmniejszyć alokację, grozi utratą danych.

**Potwierdź, że wolumin używa dysku wirtualnego obsługującego discard**, a następnie otwórz podwyższoną sesję PowerShell w VM Windows:

```powershell
fsutil behavior query DisableDeleteNotify
Optimize-Volume -DriveLetter C -ReTrim -Verbose
```

`DisableDeleteNotify = 0` oznacza, że Windows włączył powiadomienia o usuwaniu dla zgłoszonego systemu plików. **ReTrim** ponownie wysyła żądania trim dla obecnie nieużywanych obszarów woluminu. Pomyślne zakończenie potwierdza wysłanie operacji przez gościa, ale nie określa liczby bajtów odzyskanych na hoście. Po zakończeniu zadania sprawdź host. [Dokumentacja Microsoft `Optimize-Volume`](https://learn.microsoft.com/en-us/powershell/module/storage/optimize-volume?view=windowsserver2025-ps) i [dokumentacja dysków VM Proxmox](https://github.com/proxmox/pve-docs/blob/master/qm.adoc)

**Nie myl QEMU guest agent z TRIM.** Agent obsługuje sterowanie gościem i zapewnia spójność kopii. Powiadomienia systemu plików o usuwaniu są przesyłane przez dysk wirtualny. Sama instalacja agenta nie odzyskuje bloków. [Dokumentacja Proxmox guest agent dla VM](https://github.com/proxmox/pve-docs/blob/master/qm.adoc)

## Odzyskaj miejsce w Linuksie

**Przed trim sprawdź ścieżkę blokową i system plików.** Nowoczesna dystrybucja często okresowo uruchamia `fstrim.timer`. Sprawdź jego stan, a po usunięciu zbędnych danych gościa wykonaj trim zamontowanych systemów plików.

```bash
lsblk -D
systemctl status fstrim.timer
sudo fstrim -av
```

**`lsblk -D`** podaje ziarnistość discard i limity widocznych urządzeń blokowych. **`fstrim -av`** wykonuje trim obsługiwanych zamontowanych systemów plików i pokazuje wysłane zakresy. Wysłane bajty nie są równe bajtom zwróconym do puli. Urządzenia szyfrowane, LVM, RAID i inne warstwy stosu wymagają discard na każdym poziomie. [Wskazówki Red Hat dotyczące nieużywanych bloków](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/8/html/managing_file_systems/discarding-unused-blocks_managing-file-systems)

Użyj zaplanowanego trim lub przemyślanej polityki discard online. **Nie włączaj ciągłego `discard` na każdym systemie plików zamiast sprawdzić ścieżkę pamięci.** Po trim w gościu sprawdź wolumin i pulę PVE. Jeśli usunięte rekordy nadal zajmują miejsce w plikach, sprawdź własną politykę kompaktowania bazy danych lub usługi.

## Osobno sprawdź pamięć kontenerów

**LXC nie ma emulowanej magistrali dysku VM dla głównego systemu plików.** Zacznij od `pct config CTID` i znajdź wpisy `rootfs` oraz `mpN`. Proxmox rozróżnia montowania oparte na pamięci, bind mounty i montowania urządzeń. Ścieżka widoczna w kontenerze nie wskazuje, który wolumin hosta jest właścicielem bloków. [Punkty montowania kontenerów Proxmox](https://github.com/proxmox/pve-docs/blob/master/pct.adoc)

```bash
pct config 101
pct exec 101 -- df -h
pvesm status
```

W przypadku **zarządzanego rootfs lub punktu montowania** usuń pliki z kontenera albo aplikacji, a potem sprawdź wolumin bazowy i migawki na hoście. **Nie wykonuj poleceń `qm` discard dla VM na CT.** Migawki podwoluminów ZFS zatrzymują usunięte bloki. Przy directory i LVM thin sprawdź rzeczywistą alokację backendu, a nie skonfigurowany rozmiar CT.

Po czyszczeniu CT uruchom **`pct fstrim` na hoście Proxmox**, jeśli pamięć bazowa obsługuje discard. Proxmox wykonuje trim na rootfs CT i kwalifikujących się zarządzanych punktach montowania. Pomija bind mounty i punkty tylko do odczytu. Użyj `--ignore-mountpoints`, aby trimować tylko rootfs. Porównaj użycie pamięci przed i po. [Dokumentacja Proxmox `pct fstrim`](https://github.com/proxmox/pve-docs/blob/master/generated/pct.1-synopsis.adoc)

```bash
pct fstrim 101
pct fstrim 101 --ignore-mountpoints 1
```

Polecenia pokazują **alternatywne zakresy** dla przykładowego ID CT `101`. Wybierz zakres odpowiedni dla układu pamięci. Udany trim nie gwarantuje odzyskania takiej samej liczby bajtów, jeśli migawki trzymają stare bloki.

**Proxmox nie zarządza bind mountami ani montowaniami urządzeń.** Dane źródłowe pozostają na hoście lub urządzeniu zewnętrznym. Kopie kontenera `vzdump` pomijają ich zawartość. Dodatkowe punkty montowania oparte na pamięci są też domyślnie wykluczone, chyba że obejmuje je opcja `backup`. Przed czyszczeniem sprawdź rzeczywistą politykę kopii. [Dokumentacja kopii zapasowych Proxmox](https://github.com/proxmox/pve-docs/blob/master/vzdump.adoc)

W przypadku zagnieżdżonego Dockera sprawdź warstwy obrazów, woluminy i logi w miejscu, które faktycznie przechowuje dane, zanim użyjesz poleceń czyszczenia Dockera. [Poradnik niezawodności Dockera w LXC](/articles/docker-in-lxc-proxmox-reliability/) opisuje granice montowań i kopii. Usunięcie obrazu kontenera domyślnie nie usuwa trwałego woluminu.

## Zmierz poprawnie serwer

**Zapisz te same pomiary przed czyszczeniem i po nim.** Wolne miejsce puli to ostateczny wskaźnik pojemności. Dane dla woluminów pomagają znaleźć gościa odpowiedzialnego za wzrost.

```bash
pvesm status
pvesm list local-lvm
qm config 100
pct config 101
```

**`pvesm list`** pokazuje zarządzane woluminy i skonfigurowane rozmiary. Nie mierzy przydzielonych bajtów w pamięci thin. Dla pamięci **directory** sprawdź dokładną ścieżkę montowania i znany plik obrazu. Zastąp ścieżki wartościami z **Datacenter > Storage** i konfiguracji VM.

```bash
df -hT /var/lib/vz
du -h /var/lib/vz/images/100/vm-100-disk-0.qcow2
ls -lh /var/lib/vz/images/100/vm-100-disk-0.qcow2
```

Dla **zatrzymanej VM** porównaj pojemność wirtualną i alokację na hoście bez modyfikowania pliku:

```bash
qemu-img info /var/lib/vz/images/100/vm-100-disk-0.qcow2
```

Dla **LVM thin** monitoruj dane i metadane puli:

```bash
lvs -a -o lv_name,vg_name,lv_size,data_percent,metadata_percent,segtype
```

Dla **ZFS** oddziel aktywne dane zbioru danych od bloków zatrzymanych przez migawki:

```bash
zpool list
zfs list -o name,used,available,referenced,usedbysnapshots -r POOL_OR_DATASET
zfs list -t snapshot -o name,used,referenced,written -r DATASET
```

**`usedbysnapshots`** podaje bloki zatrzymane przez wszystkie migawki zbioru danych. Wartości `used` migawek nie sumują się, ponieważ migawki współdzielą bloki. Usunięcie pliku może nie zmienić użycia puli, dopóki nie wygaśnie lub nie zostanie usunięta zgodnie z polityką retencji każda migawka odwołująca się do jego bloków. [Migawki i klony OpenZFS](https://openzfs.github.io/openzfs-docs/Basic%20Concepts/Datasets/Snapshots%20and%20Clones.html)

Dla **Ceph RBD** najpierw przyporządkuj ID woluminu Proxmox do obrazu. **`qm config VMID`** pokazuje `STORAGE_ID:IMAGE`. Otwórz wpis RBD w **Datacenter > Storage**, aby znaleźć **pulę** i opcjonalną **przestrzeń nazw**. ID pamięci nie musi być nazwą puli. Zbuduj `POOL/IMAGE` z wartości puli i obrazu. Uruchom polecenia na kliencie skonfigurowanym dla właściwego klastra Ceph i z prawidłowymi danymi logowania. [Dokumentacja pamięci RBD Proxmox](https://github.com/proxmox/pve-docs/blob/master/pve-storage-rbd.adoc)

```bash
ceph df
rbd du POOL/IMAGE
rbd snap ls POOL/IMAGE
```

**`rbd du`** podaje przydzielone i rzeczywiste użycie obrazu, łącznie z powiązanymi migawkami. Bez funkcji obrazu `fast-diff` odpytuje OSD o potencjalne obiekty, co wymaga więcej pracy. **`ceph df`** pokazuje pojemność puli i klastra. Replikacja, kodowanie erasure i migawki wpływają na surowe użycie klastra, dlatego bajty obrazu i puli są różne. [Dokumentacja polecenia Ceph RBD](https://docs.ceph.com/en/squid/man/8/rbd/) i [wskazówki Ceph dotyczące użycia puli](https://docs.ceph.com/en/squid/rados/operations/monitoring/)

Jeśli pamięć RBD używa przestrzeni nazw, dodaj **`--namespace NAMESPACE`** do każdego polecenia `rbd`. Użyj przestrzeni nazw skonfigurowanej we wpisie pamięci Proxmox, nie ID pamięci Proxmox.

## Uwzględnij migawki i kopie zapasowe

**Migawki zachowują starsze wersje bloków.** Jeśli użycie nie spada po trim, sprawdź kartę **Snapshots** VM lub CT oraz migawki backendu. Przed usunięciem sprawdź właściciela i zależności. Kopia zapasowa to oddzielna kopia z własną retencją, niezależną od bieżącego wyniku `df` w gościu.

**Deduplicacja PBS zmienia sposób liczenia.** Datastore przechowuje bloki współdzielone przez kopie. Pruning usuwa metadane migawek kopii. Później garbage collection usuwa niepowiązane bloki po okresie karencji. Przed deklaracją odzyskania miejsca na kopie sprawdź oba zadania. [Dokumentacja konserwacji PBS](https://pbs.proxmox.com/docs/maintenance.html)

> **Ostrzeżenie:** Nigdy nie usuwaj pliku woluminu zarządzanego przez Proxmox, zvol ani migawki tylko na podstawie nazwy. Najpierw określ gościa i politykę retencji. Czyszczenie musi zachować kopię i ścieżkę wycofania zmian.

## Odtwórz obraz dysku po wyłączeniu VM

**Konwersji offline używaj tylko wtedy, gdy zwykły trim gościa i ścieżka backendu nie rozwiązują problemu alokacji qcow2.** Wyłącz VM, sprawdź kopię zapasową, rozpoznaj wszystkie zależności migawek i łańcuchów backing oraz zapisz oddzielny obraz docelowy. QEMU ostrzega przed modyfikowaniem obrazu używanego przez inny proces. [Dokumentacja QEMU `qemu-img`](https://www.qemu.org/docs/master/tools/qemu-img.html)

**Wybierz przeniesienie zarządzane przez Proxmox albo przepływ kopii i odtwarzania**, jeśli dysk ma migawki lub leży na zarządzanej pamięci blokowej. Samodzielne `qemu-img convert` obrazu należącego do PVE nie aktualizuje konfiguracji VM, własności woluminu ani odwołań do migawek. Nie używaj `qemu-img resize --shrink` do odzyskania usuniętych plików. Zmniejszenie pojemności widocznej dla gościa grozi ucięciem danych, jeśli wcześniej nie zmniejszono partycji i systemów plików.

## Rozwiąż problem nieudanego odzyskiwania

| Objaw | Prawdopodobna kontrola | Następne działanie |
|---|---|---|
| **`df` gościa spada, host bez zmian** | Flaga discard VM, trim gościa, migawki | Sprawdź całą ścieżkę discard i zachowane migawki. |
| **`fstrim` zgłasza brak obsługi** | Magistrala dysku gościa, urządzenia warstwowe, backend | Sprawdź `lsblk -D`, jądro gościa i każdą warstwę pośrednią. |
| **Windows ReTrim kończy się, host bez zmian** | Alokacja backendu, migawki, pomiar serwera | Porównaj wolumin i pulę. Potwierdź, że dysk korzysta z thin storage. |
| **`ls -lh` i `du -h` się różnią** | Plik rzadki lub qcow2 | `du` pokazuje przydzielone bloki systemu plików. |
| **Pula LVM thin pozostaje mocno zajęta** | Dane, metadane, migawki | Przed usuwaniem sprawdź `lvs` i migawki PVE. |
| **Pula ZFS pozostaje mocno zajęta** | Bloki zatrzymane przez migawki i rezerwacje | Sprawdź `usedbysnapshots`, ustawienia zvol i pojemność puli. |
| **`df` CT nie zgadza się z pulą** | Bind mounty, punkty montowania, migawki | Przyporządkuj `rootfs` i każdy `mpN` do właściciela na hoście. |

**Sprawdź ponownie po zakończeniu zadań w tle.** Ewidencja pamięci może się opóźniać po trim, usunięciu migawki lub garbage collection backendu. Porównaj zmierzone wolne miejsce puli z wartością początkową. Nie uznawaj samego kodu zakończenia polecenia gościa za dowód sukcesu.

## Następne kroki

**Prowadź rejestr pamięci dla każdego gościa:** pojemność wirtualna, przydzielone bajty, backend, magistrala, flaga discard, liczba migawek, zakres kopii zapasowych i wolne miejsce puli. Wybierz jedną VM, włącz obsługiwaną ścieżkę discard, wykonaj trim w gościu i porównaj zapisane wartości. Powtórz dopiero, gdy wynik pierwszej VM odpowiada oczekiwanemu zachowaniu backendu.

Aby zaplanować pełniejsze odzyskiwanie, wykonaj [test kopii zapasowej i odtwarzania Proxmox](/articles/proxmox-vm-backup-restore-drill/) oraz skorzystaj z [poradnika aktualizacji Proxmox VE 8 do 9](/articles/proxmox-ve-8-to-9-upgrade-guide/).

## Źródła

- [Administracja pamięcią Proxmox VE](https://github.com/proxmox/pve-docs/blob/master/pvesm.adoc), typy pamięci, thin provisioning i ryzyko braku pojemności.
- [Pamięć LVM Proxmox VE](https://github.com/proxmox/pve-docs/blob/master/pve-storage-lvm.adoc), łańcuchy woluminów migawek VE 9 i alokacja.
- [Pamięć RBD Proxmox VE](https://github.com/proxmox/pve-docs/blob/master/pve-storage-rbd.adoc), konfiguracja puli i przestrzeni nazw.
- [Maszyny wirtualne Proxmox VE](https://github.com/proxmox/pve-docs/blob/master/qm.adoc), magistrale, formaty dysków, discard i guest agent.
- [Opcje dysków VM Proxmox VE](https://github.com/proxmox/pve-docs/blob/master/generated/qm.conf.5-opts.adoc), flagi zależne od magistrali.
- [Kontenery Proxmox VE](https://github.com/proxmox/pve-docs/blob/master/pct.adoc), główne systemy plików i własność punktów montowania.
- [Polecenia kontenerów Proxmox VE](https://github.com/proxmox/pve-docs/blob/master/generated/pct.1-synopsis.adoc), trim kontenera z hosta.
- [Kopie zapasowe i odtwarzanie Proxmox VE](https://github.com/proxmox/pve-docs/blob/master/vzdump.adoc), zakres kopii VM i CT.
- [dokumentacja Microsoft dla polecenia `Optimize-Volume`](https://learn.microsoft.com/en-us/powershell/module/storage/optimize-volume?view=windowsserver2025-ps), składnia Windows ReTrim.
- [Wskazówki Red Hat dotyczące nieużywanych bloków](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/8/html/managing_file_systems/discarding-unused-blocks_managing-file-systems), działanie Linux `fstrim`.
- [Migawki i klony OpenZFS](https://openzfs.github.io/openzfs-docs/Basic%20Concepts/Datasets/Snapshots%20and%20Clones.html), bloki zatrzymane przez migawki.
- [Dokumentacja polecenia Ceph RBD](https://docs.ceph.com/en/squid/man/8/rbd/), użycie obrazów i migawki.
- [Specyfikacja NFSv4.2](https://www.rfc-editor.org/rfc/rfc7862.html#section-6.2.2), zwalnianie miejsca po stronie serwera.
- [Dokumentacja konserwacji PBS](https://pbs.proxmox.com/docs/maintenance.html), pruning i garbage collection.
- [Narzędzie obrazów dysków QEMU](https://www.qemu.org/docs/master/tools/qemu-img.html), bezpieczeństwo konwersji offline.
