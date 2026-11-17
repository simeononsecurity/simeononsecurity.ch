---
title: "Test odtwarzania VM Proxmox: sprawdź, czy system gościa działa"
date: 2026-10-11
lastmod: 2026-11-15
toc: true
draft: false
description: "Przetestuj kopię zapasową VM Proxmox przez odtworzenie w izolowanym środowisku. Sprawdź zakres dysków, tryb kopii, dane gościa, stan usługi i czas odzyskiwania bez ingerencji w produkcję."
genre: ["Wirtualizacja", "Kopia zapasowa i odzyskiwanie", "Domowe laboratorium"]
tags: ["test odtwarzania Proxmox", "kopia zapasowa VM Proxmox", "ćwiczenie odtwarzania Proxmox", "qmrestore", "vzdump", "weryfikacja Proxmox Backup Server", "kopia migawkowa Proxmox", "test odzyskiwania VM", "RPO i RTO kopii zapasowej", "odtwarzanie VM w izolacji", "tryb kopii Proxmox", "kopia z agentem gościa"]
cover: "/img/cover/proxmox-vm-backup-restore-drill.webp"
coverAlt: "Kopia zapasowa przechodzi z pomarańczowej produkcyjnej VM przez magazyn do niebieskiej, odizolowanej testowej VM. Sprawdzane są dyski, usługi i czas."
coverCaption: "Zakończone zadanie kopii zapasowej to początek testu odzyskiwania."
---

Zielone zadanie kopii zapasowej oznacza, że Proxmox zapisał kopię. Nie pokazuje, czy gość się uruchomi, czy ma aktualne dane ani czy działa jego główna usługa. **Odtwórz kopię pod nowym identyfikatorem VM w odizolowanej sieci.** Wynik daje dowód odzyskiwania, zanim awaria zmusi Cię do przeprowadzenia testu.

<!--more-->

To ćwiczenie obejmuje jedną **maszynę wirtualną Proxmox VE**. Kontenery podlegają innym regułom kopii, zwłaszcza w przypadku montowań bind i urządzeń. [Test kopii zapasowej i odtwarzania w domowym laboratorium](/articles/homelab-backup-restore-drill/) opisuje szersze odzyskiwanie plików. Tutaj przetestujesz kopię VM Proxmox i jej obciążenie.

**Gość** to system operacyjny działający wewnątrz maszyny wirtualnej. **Montowania bind** i **montowania urządzeń** udostępniają gościowi zasoby hosta. Sprawdź te zasoby w ramach osobnego planu odzyskiwania.

## Najważniejsze wnioski

- **Najpierw określ sukces:** wybierz element danych, test usługi i akceptowalny czas odzyskiwania.
- **Sprawdź zakres kopii:** kopia VM pomija dyski oznaczone **No backup** i nie odtwarza usług zewnętrznych ani pominiętych danych.
- **Odtwarzaj osobno:** użyj nieużywanego identyfikatora VM i odizoluj przywróconą sieć od produkcji.
- **Zapisz dowody:** zmierz wiek kopii, czas odtwarzania, uruchomienie, obecność dysków i rzeczywisty test aplikacji.

## Zanim zaczniesz

Wybierz VM, której kopię można bezpiecznie przetestować. Potrzebujesz dostępu administratora do Proxmox, ukończonej kopii na magazynie plików lub Proxmox Backup Server (PBS), wystarczającej ilości miejsca na drugą VM oraz odizolowanego mostu sieciowego albo odłączonego urządzenia sieciowego. Odizolowany most to wirtualna sieć Proxmox bez trasy do produkcyjnej sieci LAN. Jeśli go nie masz, użyj odłączonego adaptera lub testowej sieci VLAN. Pozostaw produkcyjną VM uruchomioną. Zarezerwuj nowy identyfikator VM, na przykład **920**, po sprawdzeniu, czy inny gość go nie używa. Zaplanuj wystarczająco dużo czasu na pełne odtwarzanie i test obciążenia.

Zapisz kryteria zaliczenia przed odtworzeniem. Dla serwera plików wybierz niedawny plik i oczekiwaną sumę kontrolną lub treść. Dla bazy danych wybierz bezpieczne zapytanie tylko do odczytu i rekord zapisany przed kopią. Dla usługi internetowej wybierz lokalny test stanu i reprezentatywną stronę. Zapisz najnowszy akceptowalny czas danych, **cel punktu odzyskiwania (RPO)**, oraz czas do przywrócenia usługi, czyli **cel czasu odzyskiwania (RTO)**. Sam ekran rozruchowy nie spełnia tych kryteriów.

| Zapis | Przykładowy dowód |
|---|---|
| **Punkt kopii** | Czas migawki i ostatni oczekiwany element danych |
| **Cel odzyskiwania** | Wolny identyfikator VM, magazyn docelowy, odizolowany most |
| **Test obciążenia** | Logowanie, zamontowanie woluminu i odczyt z aplikacji |
| **Limit czasu** | Czas rozpoczęcia i zakończenia odtwarzania oraz testu usługi |

Nie podłączaj odtworzonego gościa do sieci produkcyjnej przed sprawdzeniem jego nazwy, adresu IP, adresu MAC, zaplanowanych zadań i integracji zewnętrznych. Skopiowana tożsamość może powodować konflikt z działającą VM albo wysyłać podwójne zadania.

## Sprawdź zakres kopii zapasowej

**Zakres wersji:** tych przykładów nie uruchamiano podczas przygotowywania artykułu. Przed testem zapisz wynik `pveversion --verbose`. Korzystaj z dokumentacji odpowiadającej zainstalowanej wersji Proxmox VE. W raporcie ćwiczenia zapisz backend magazynu, typ gościa i wynik poleceń.

Na węźle Proxmox poniższe polecenie tylko do odczytu pokazuje konfigurację źródłowej VM. Zastąp **120** identyfikatorem źródłowej VM:

```bash
qm config 120
```

Wyświetl każdy dysk wirtualny i jego ustawienie kopii. [Dokumentacja dysków VM Proxmox](https://github.com/proxmox/pve-docs/blob/master/qm.adoc) wyjaśnia, że opcja **No backup** wyklucza dysk z kopii VM. Sprawdź, czy dane aplikacji znajdują się na wykluczonym dysku, montowaniu hosta, sprzęcie przekazanym bezpośrednio albo usłudze zdalnej. Zapisz osobną procedurę odzyskiwania dla tych zasobów. Test rozruchu VM nie potwierdza ochrony wykluczonych danych.

Sprawdź znacznik czasu, rozmiar, dziennik zadania i lokalizację magazynu najnowszej kopii. W interfejsie Proxmox otwórz widok **Backups** magazynu kopii lub kartę **Backup** VM. Potwierdź, że zadanie zakończyło się bez błędów. [Dokumentacja kopii Proxmox](https://github.com/proxmox/pve-docs/blob/master/vzdump.adoc) rozróżnia zwykłe pliki kopii od magazynu PBS, który przechowuje zdeduplikowane bloki i metadane.

| Tryb kopii | Zachowanie VM | Decyzja na potrzeby ćwiczenia |
|---|---|---|
| **Snapshot** | Tworzy kopię działającej VM przy krótkiej przerwie. Zapisy gościa niosą niewielkie ryzyko niespójności. | Odpowiedni do rutynowych testów, jeśli obciążenie toleruje taki punkt odzyskiwania. |
| **Stop** | Wyłącza gościa na początku kopii i zapewnia najwyższą spójność. | Użyj, gdy obciążenie wymaga czystego zamknięcia, a przestój jest akceptowalny. |
| **Suspend** | Wstrzymuje gościa przed trybem snapshot i wydłuża przestój bez ogólnej poprawy spójności. | Nie wybieraj suspend jako domyślnego ulepszenia względem snapshot. |

Te różnice opisuje [dokumentacja trybów kopii Proxmox](https://github.com/proxmox/pve-docs/blob/master/vzdump.adoc). **QEMU Guest Agent** to usługa wewnątrz gościa, która pozwala Proxmox żądać takich działań jak zamrożenie i odmrożenie systemu plików. Działający gość z włączonym i sprawnym agentem obsługuje te działania podczas kopii snapshot. Zamrożenie systemu plików poprawia spójność, ale nie zastępuje testu odzyskiwania specyficznego dla bazy danych. Zapisz rzeczywisty tryb i stan agenta zamiast zakładać, że zaplanowane zadanie używa preferowanych ustawień.

## Utwórz lub wybierz punkt odzyskiwania

Jeśli ćwiczenie sprawdza rutynowe odzyskiwanie, użyj niedawnej, udanej kopii zaplanowanej. Jeśli potrzebujesz nowej, jednorazowej kopii, otwórz kartę **Backup** VM, wybierz **Backup now**, ustaw magazyn docelowy i tryb, a następnie poczekaj na komunikat o powodzeniu w dzienniku zadania. W powłoce Proxmox poniższy przykład tworzy kopię VM **120** w trybie snapshot na magazynie o identyfikatorze **backup-nfs**:

```bash
vzdump 120 --storage backup-nfs --mode snapshot
```

Zastąp oba identyfikatory własnymi wartościami. Uruchom polecenie dopiero po potwierdzeniu, że magazyn przyjmuje kopie i ma wystarczająco dużo miejsca. [Dokumentacja `vzdump` Proxmox](https://github.com/proxmox/pve-docs/blob/master/vzdump.adoc) opisuje opcje trybu i magazynu. Po zakończeniu polecenia sprawdź dziennik zadania. Nie traktuj starej kopii jako aktualnego punktu odzyskiwania tylko dlatego, że nazwa pliku wygląda na nową.

Jeśli celem jest **PBS**, uruchom lub sprawdź zadanie weryfikacji wybranego magazynu danych. [Dokumentacja weryfikacji PBS](https://pbs.proxmox.com/docs/maintenance.html) wyjaśnia, jak sprawdzić integralność danych i zaplanować kolejne kontrole. Weryfikacja wykrywa uszkodzone bloki kopii. **Udana weryfikacja nie dowodzi, że odtworzony system operacyjny, aplikacja lub zewnętrzna zależność działają.** Kontynuuj ćwiczenie odtwarzania nawet po pomyślnej weryfikacji.

## Odtwórz na odizolowanej VM

W interfejsie Proxmox wybierz kopię w widoku **Backups** magazynu i wybierz **Restore**. Podaj nieużywany identyfikator VM oraz docelowy magazyn. Pozostaw **Start after restore** wyłączone. Sprawdź opcję wygenerowania nowego adresu MAC. Oficjalna [składnia `qmrestore`](https://github.com/proxmox/pve-docs/blob/master/generated/qmrestore.1-synopsis.adoc) opisuje unikalny identyfikator VM, wybór magazynu, `--unique` dla losowego adresu Ethernet i domyślne nieuruchamianie odtworzonej VM.

Dla archiwum `vzdump` opartego na pliku poniższe polecenie powłoki pokazuje równoważny wzorzec. Zastąp ścieżkę archiwum, nowy identyfikator VM i identyfikator magazynu wartościami ze swojego środowiska:

```bash
qmrestore /path/to/vzdump-qemu-120-2026_10_11-02_00_00.vma.zst 920 --storage local-lvm --unique 1
```

[Opis odtwarzania Proxmox](https://github.com/proxmox/pve-docs/blob/master/qmrestore.adoc) wskazuje, że bez magazynu docelowego odtwarzanie próbuje użyć magazynu źródłowego. Ustaw **`--storage`**, jeśli starego magazynu nie ma na węźle testowym. Nie używaj **`--force`** podczas ćwiczenia. Ta opcja pozwala nadpisać istniejącą VM, a ta procedura wymaga wolnego identyfikatora. Kopie PBS również odtwarza się z interfejsu Proxmox. Wybierz wpis magazynu dla migawki PBS, zamiast traktować migawkę jak lokalny plik `.vma.zst`.

Przed pierwszym uruchomieniem sprawdź wszystkie odtworzone interfejsy sieciowe, także dodatkowe i przekazane bezpośrednio. **Adres MAC** identyfikuje interfejs sieciowy. **DNS** przypisuje nazwy do adresów. **DHCP** przydziela ustawienia sieci. **VLAN** to logiczna sieć przenoszona przez współdzielony sprzęt. **Wirtualny TPM** przechowuje stan bezpieczeństwa gościa. Odłącz każdy interfejs albo podłącz go wyłącznie do odizolowanego segmentu testowego. Upewnij się, że trasy produkcyjne, ścieżki DNS, usługi DHCP, sieć zarządzająca i integracje zewnętrzne są niedostępne. Jeśli obciążenie wymaga innej usługi testowej, zapewnij jej kopię w odizolowanej sieci. Porównaj mapowanie dysków, firmware, wymagania wirtualnego TPM i urządzenia specjalne ze źródłem. Zewnętrzne dyski, urządzenia przekazane bezpośrednio i sekrety przechowywane poza VM wymagają osobnych planów.

## Przetestuj gościa i obciążenie

Uruchom odtworzoną VM i najpierw użyj jej konsoli. Sprawdź, czy system operacyjny się uruchamia, oczekiwane woluminy są zamontowane, zegar pokazuje właściwy czas, a aplikacja startuje. Następnie wykonaj wcześniej zapisane kryterium zaliczenia. Porównaj znany element danych z jego wartością i znacznikiem czasu sprzed kopii. Ekran logowania ani działający proces sam w sobie nie dowodzi, że usługa zawiera właściwe dane.

| Test | Warunek zaliczenia |
|---|---|
| **Rozruch** | Gość osiąga normalne logowanie bez trybu naprawy i powtarzających się monitów odzyskiwania. |
| **Dyski** | Każdy dysk objęty kopią jest widoczny, zamontowany i zawiera oczekiwane dane. |
| **Usługa** | Reprezentatywne lokalne żądanie lub odczyt kończy się powodzeniem. |
| **Punkt odzyskiwania** | Odtworzone dane spełniają zapisane RPO. |
| **Czas odzyskiwania** | Odtwarzanie, rozruch i sprawdzenie usługi mieszczą się w zapisanym RTO. |
| **Izolacja** | Produkcyjny adres, zadanie ani integracja nie otrzymują podwójnego ruchu. |

Izoluj odtworzonego gościa podczas sprawdzania zaplanowanych zadań, hooków powiadomień, agentów kopii i danych logowania aplikacji. Nie uruchamiaj testu, który wysyła prawdziwe wiadomości do klientów lub zapisuje dane w usługach produkcyjnych. Jeśli test się nie powiedzie, zapisz dokładny etap. Rozróżnij **błąd integralności kopii**, **błąd rozruchu VM**, **brak danych** i **błąd aplikacji**. Każdy wymaga innej poprawki.

| Kategoria błędu | Dowód potwierdzający | Pierwsza poprawka | Ponowny test |
|---|---|---|---|
| **Integralność kopii** | Zadanie weryfikacji lub odtwarzania zgłasza uszkodzone dane | Wybierz inny zweryfikowany punkt odzyskiwania i sprawdź stan magazynu | Powtórz weryfikację i odtwarzanie |
| **Rozruch VM** | Konsola pokazuje błędy firmware, dysku lub odzyskiwania | Porównaj firmware, mapowanie dysków i kolejność rozruchu ze źródłem | Uruchom izolowaną kopię i zapisz wynik z konsoli |
| **Brak danych** | Brakuje oczekiwanego pliku, woluminu lub rekordu bazy | Sprawdź wykluczone dyski, montowania, migawki i zależności zewnętrzne | Ponów wskazany test pliku lub danych |
| **Aplikacja** | Gość startuje, ale test usługi się nie udaje | Sprawdź dzienniki, dane logowania, zależności i kroki odzyskiwania usługi | Uruchom ten sam lokalny test stanu i test obciążenia |

Proxmox oferuje [odtwarzanie pojedynczych plików z kopii PBS](https://github.com/proxmox/pve-docs/blob/master/vzdump.adoc). Użyj go, aby przetestować ścieżkę odzyskiwania pliku, jeśli wymaga tego obciążenie. Odzyskany plik nie zastępuje pełnego rozruchu VM i testu usługi. Proxmox umożliwia też odtwarzanie na żywo z PBS. Dokumentacja wskazuje, że po nieudanym odtwarzaniu na żywo VM pozostaje w nieokreślonym stanie. W tym zaplanowanym ćwiczeniu użyj normalnego, zakończonego odtwarzania.

## Zapisz wynik i zakończ ćwiczenie

Zapisz źródłowy identyfikator VM, magazyn kopii, czas wykonania kopii, tryb, nowy identyfikator VM, magazyn docelowy, izolację sieci, czasy rozpoczęcia i zakończenia odtwarzania, test aplikacji, czas danych i nieudane kontrole. Porównaj zmierzony punkt oraz czas odzyskiwania z celami. Błąd jest użytecznym dowodem tylko wtedy, gdy zmienisz plan kopii i powtórzysz ćwiczenie.

Po zakończeniu testu wyłącz odtworzoną VM. Usuń jej kopię testową dopiero po zapisaniu wyniku i potwierdzeniu, że produkcyjna VM nadal działa zgodnie z oczekiwaniami. Zachowaj kopię zgodnie ze zwykłą polityką retencji. Nie zmieniaj retencji, aby zaliczyć jedno ćwiczenie.

Powtórz test po istotnych zmianach magazynu, gościa lub konfiguracji kopii. Testuj na zmianę ważne VM, w tym gości z wykluczonymi dyskami lub zależnościami zewnętrznymi. [Przewodnik migracji z Hyper-V do Proxmox](/articles/hyper-v-to-proxmox-migration-checklist/) wykorzystuje taki dowód odzyskiwania przed wycofaniem źródłowej VM. **Użyteczna kopia ma znaną ścieżkę odtwarzania, przetestowane obciążenie i zmierzony punkt odzyskiwania.**

## Następne kroki

Powtórz ćwiczenie po zmianach magazynu, gościa lub kopii. Informacje o odzyskiwaniu plików znajdziesz w [teście kopii zapasowej i odtwarzania w domowym laboratorium](/articles/homelab-backup-restore-drill/).
