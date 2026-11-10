---
title: "Docker w LXC na Proxmox: niezawodność, dowody i migracja do VM"
date: 2026-09-16
lastmod: 2026-11-08
toc: true
draft: false
description: "Oceń Docker wewnątrz Proxmox LXC na podstawie udokumentowanego błędu AppArmor, uważnej analizy zgłoszenia o zawieszeniu hosta, poleceń diagnostycznych i planu migracji do VM."
genre: ["Wirtualizacja", "Administracja Linuksem", "Homelab"]
tags: ["Docker w LXC", "Docker na Proxmox", "LXC w Proxmox", "maszyna wirtualna Docker", "niezawodność homelabu", "zawieszanie hosta Proxmox", "Debianowa maszyna wirtualna Docker", "kontenery bez uprawnień", "zagnieżdżanie kontenerów", "izolacja jądra Linuksa", "AppArmor", "runc", "lxc-pve", "Docker Compose", "sterowniki pamięci masowej Docker", "magazyn obrazów containerd", "presja pamięci", "Linux PSI", "trwały dziennik", "kopie zapasowe Proxmox", "kopie zapasowe bind mountów", "migracja VM", "domeny awarii", "przekazywanie GPU", "rozwiązywanie problemów z serwerem domowym"]
cover: "/img/cover/docker-lxc-vm-homelab-isolation.webp"
coverAlt: "Izometryczna ilustracja domowego serwera przedstawiająca zagnieżdżone obciążenia i osobną maszynę wirtualną podłączoną do współdzielonego sprzętu"
coverCaption: "Ilustracja koncepcyjna współdzielonego sprzętu i różnych granic izolacji obciążeń"
---

**Docker wewnątrz Linux Containers (LXC)** zmniejsza narzut infrastruktury, ale zwiększa liczbę interakcji między środowiskiem uruchomieniowym aplikacji a hostem Proxmox. Dla usług Docker, od których zależy domowa sieć, praktycznym punktem wyjścia jest **maszyna wirtualna (VM) z Debianem**. Oddziela ona jądro gościa i upraszcza środowisko, które trzeba odtworzyć podczas diagnozowania problemów. Ten artykuł analizuje przekazany film, sprawdza powiązany raport o incydencie oraz dodaje udokumentowane awarie i plan migracji.

<!--more-->

## Najważniejsze wnioski

- **Rozróżniaj typy awarii:** Błąd uruchamiania Docker, zawieszona VM i niereagujący fizyczny host wymagają odrębnej diagnostyki.
- **Oceń dowody:** Stabilność po migracji uzasadnia decyzję o odzyskiwaniu działania, ale nie dowodzi pierwotnej przyczyny.
- **Sprawdź aktualną dokumentację:** Natywna obsługa obrazów OCI i Docker zagnieżdżony w LXC to różne ścieżki wdrożenia.
- **Chroń trwałe dane:** Kopie zapasowe Proxmox i pliki Compose nie obejmują automatycznie każdej lokalizacji danych aplikacji.
- **Przetestuj plan odzyskiwania:** Zmierz odtwarzanie, zachowanie po ponownym uruchomieniu i dostępność usług przed wycofaniem starego wdrożenia.

## Zanim zaczniesz

**Poziom trudności:** Średni. **Odbiorcy:** Administratorzy Proxmox wybierający między zagnieżdżonym Docker a Docker w VM. Przed użyciem przykładów diagnostycznych rozpoznawaj projekt Compose, montowanie kontenera i wiersz poleceń Linux.

**Szacowany czas:** Przeznacz 30–60 minut na inwentaryzację i zbieranie dowodów. Czas migracji zależy od rozmiaru bazy danych, przepustowości pamięci masowej, dostępu do sprzętu i wybranego okna przestoju. Poniższe przykłady to udokumentowane procedury i ilustracyjne rozumowanie, a nie wyniki testów laboratoryjnych na potrzeby tego artykułu.

| Wymaganie | Dlaczego ma znaczenie |
|---|---|
| **Dostęp do konsoli hosta** | Pozwala odróżnić awarię sieci od zawieszenia całego hosta |
| **Aktualne kopie zapasowe** | Zapewniają ścieżkę odzyskiwania przed zmianą wdrożenia |
| **Identyfikatory kontenerów i VM** | Kierują polecenia hosta do właściwego obciążenia |
| **Inwentaryzacja danych aplikacji** | Wskazuje wolumeny, bind mounty, bazy danych i zależności zewnętrzne |
| **Oddzielne środowisko testowe** | Umożliwia próbę migracji bez równoległych zapisów produkcyjnych |

## Obejrzyj film źródłowy

{{< youtube id="XyPBHhZg0Ok" enable="true" title="Proxmox: The Hidden Danger of Running Docker Inside LXC" description="Omówienie Dockera zagnieżdżonego w Proxmox LXC, sporadycznych zawieszeń hosta i migracji do maszyn wirtualnych z Debianem" uploadDate="2026-09-15T17:00:09-07:00" >}}

**Film źródłowy:** [Proxmox: The Hidden Danger of Running Docker Inside LXC](https://www.youtube.com/watch?v=XyPBHhZg0Ok), opublikowany 15 września 2026 r. przez *Proxmox x Kubernetes x Homelab x Backup*. Główne pytanie brzmi: ile niepewności operacyjnej wiąże się z architekturą oszczędzającą zasoby?

**Granice dowodów:** Film opisuje incydent i proponuje wnioski. Poniższe sekcje rozdzielają obserwacje właściciela, udokumentowane zachowanie oprogramowania i wynikające z nich zalecenia.

## Co wynika z incydentu

Pierwotne zgłoszenie opisuje **host z procesorem Intel Core i3-13100 i płytą BIOSTAR H610MHP**. Właściciel zgłaszał sporadyczne zawieszenia wpływające na dostęp do zarządzania i usług LXC. Podłączony ekran przestał reagować, choć w raporcie wyraźnie napisano, że syslog nadal zapisywał dane. To bardziej precyzyjny opis niż stwierdzenie, że nie było żadnych logów. [Pierwotne zgłoszenie na forum Proxmox](https://forum.proxmox.com/threads/pve-host-freezes-every-2-3-weeks.185009/)

Właściciel później zgłosił **poprawę po migracji**. W aktualizacji z 3 sierpnia opisał przeniesienie obciążeń Docker do maszyn wirtualnych z Debianem i zatrzymanie kontenerów LXC uruchamiających Docker. W chwili aktualizacji nie odnotowano kolejnych zawieszeń. Film podaje okres 16 dni stabilnej pracy. Żadna z tych informacji nie przedstawia kontrolowanego odtworzenia problemu ani nie wskazuje konkretnego wadliwego elementu. [Aktualizacja właściciela w tym samym wątku](https://forum.proxmox.com/threads/pve-host-freezes-every-2-3-weeks.185009/)

| Obserwacja | Co potwierdza | Czego nie dowodzi |
|---|---|---|
| **Długi początkowy czas pracy** | Poprzednia kombinacja obciążenia i oprogramowania działała poprawnie | Niezawodności po każdej późniejszej aktualizacji |
| **Zawiesza się host i usługi** | Awaria wykracza poza jedną aplikację | Dockera jako głównej przyczyny |
| **Migracja poprzedza poprawę** | Przydatne obejście operacyjne | Która zmiana usunęła czynnik wyzwalający |
| **Szesnaście stabilnych dni** | Ograniczony okres obserwacji | Usunięcia każdego wzorca awarii powtarzającego się co dwa lub trzy tygodnie |

**Okres obserwacji** wymaga uwagi. Szesnaście dni mieści się w przedziale nawrotu wynoszącym 14–21 dni. Dłuższa obserwacja obejmująca kilka poprzednich okresów awarii, porównywalne obciążenia i zwykłe prace serwisowe zwiększa pewność, ale nadal nie dowodzi związku przyczynowego w kontrolowanych warunkach.

**Sukces operacyjny i dowód przyczyny źródłowej** to odrębne wyniki. Przywrócenie zaufanych usług domowych jest dobrym powodem do migracji. Opisuj wynik jako poprawę zaobserwowanej niezawodności, dopóki silniejsze dowody nie wykażą mechanizmu.

## Określ granicę jądra

```text
Docker inside LXC:
Application -> Docker runtime -> LXC namespaces and policy
            -> Proxmox host kernel -> physical hardware

Docker inside a VM:
Application -> Docker runtime -> guest Linux kernel
            -> virtual hardware / KVM-QEMU
            -> Proxmox host kernel -> physical hardware
```

**LXC** korzysta z jądra hosta. Przestrzenie nazw, grupy kontrolne, uprawnienia, seccomp i profile bezpieczeństwa ograniczają procesy, ale nie dostarczają oddzielnego jądra. Dodanie Dockera wewnątrz LXC tworzy kolejną warstwę zarządzania kontenerami dla obciążeń korzystających z tego samego jądra hosta. [Architektura LXC i funkcje izolacji](https://linuxcontainers.org/lxc/introduction/)

**VM** wprowadza jądro gościa. Awaria jądra gościa zwykle wpływa na tę VM, a Proxmox nadal zarządza pozostałymi gośćmi. VM nadal zależy od fizycznego hosta, hypervisora, pamięci masowej i sieci. Awaria sprzętu lub wada jądra hosta pozostają wspólną zależnością.

| Granica | Docker w LXC | Docker w VM |
|---|---|---|
| **Jądro używane przez aplikacje** | Jądro hosta Proxmox | Jądro gościa |
| **Środowisko Docker runtime** | Ograniczone polityką zewnętrznego kontenera | Zainstalowane w typowym systemie operacyjnym gościa |
| **Aktualizacje jądra gościa** | Powiązane z jądrem hosta | Zarządzane wewnątrz gościa |
| **Awaria fizycznego hosta** | Zatrzymuje zależne obciążenia | Zatrzymuje zależne obciążenia |

VM ogranicza **część propagacji awarii**, ale nie całą. Awaria procesu aplikacji w LXC nie powoduje automatycznie awarii Proxmox. Umieszczenie wszystkich usług domowych w jednej VM z Docker nadal łączy je w ramach jednego systemu operacyjnego gościa i jednego harmonogramu prac serwisowych.

Więcej informacji o **szerszym porównaniu koncepcyjnym** zawiera artykuł [Kontenery Docker a maszyny wirtualne](/articles/docker-vs-vms/). Tutaj wybór dotyczy miejsca uruchomienia Dockera w Proxmox i wynikających z tego granic diagnostyki.

## Precyzyjnie określ wsparcie

Określenie **„nieobsługiwane”** wymaga wskazania komponentu i wersji. Rozróżnij wdrożenie zalecane przez dostawcę, udokumentowane funkcje, utrzymanie dystrybucji i uprawnienie do wsparcia wynikające z umowy. Działająca zagnieżdżona konfiguracja nie dowodzi, że wszystkie jej kombinacje są testowane tak samo. Zalecenie VM nie oznacza też, że opiekunowie odrzucają każdy błąd związany z nestingiem.

**Aktualna dokumentacja Proxmox** wprowadza ważne rozróżnienie. Kod źródłowy zestawu narzędzi kontenerowych opisuje obsługę obrazów aplikacji **Open Container Initiative (OCI)** jako podgląd technologii, w którym obrazy są konwertowane do frameworka LXC. Dla wymagań obejmujących izolację i migrację na żywo zaleca też kontenery wewnątrz VM QEMU. Import obrazu OCI do tego frameworka różni się od instalacji Docker Engine i uruchamiania Compose w gościu LXC. [Dokumentacja zestawu narzędzi kontenerowych Proxmox](https://github.com/proxmox/pve-docs/blob/master/pct.adoc)

| Wdrożenie | Pytanie do sprawdzenia |
|---|---|
| **Tradycyjny gość LXC** | Czy jego szablon systemu operacyjnego i aplikacja mieszczą się w udokumentowanych ograniczeniach kontenerów? |
| **Docker zagnieżdżony w LXC** | Które kombinacje jądra, runtime, polityki bezpieczeństwa i pamięci masowej zostały przetestowane? |
| **Natywny import obrazu OCI** | Czy zainstalowana wersja Proxmox udostępnia udokumentowaną funkcję i wymagane zachowanie? |
| **Docker w VM z Debianem** | Czy wydanie systemu gościa spełnia wymagania instalacyjne Docker? |

Docker publikuje **ścieżkę instalacji dla Debiana**. Użyj listy obsługiwanych wydań i instrukcji repozytorium dla systemu gościa. Zapisuj wdrażane wersje zamiast zakładać, że starszy poradnik jest nadal aktualny. To udokumentowana podstawa instalacji, a nie gwarancja dostępności ani automatyczna umowa płatnego wsparcia. [Docker Engine w Debianie](https://docs.docker.com/engine/install/debian/)

## Potwierdzona awaria zagnieżdżenia

**Niezgodność runc/AppArmor z 2025 r.** to weryfikowalny przykład. Opiekunowie runc opisali problem z ponownym otwieraniem deskryptora wewnątrz zewnętrznego kontenera z profilem AppArmor. AppArmor błędnie zinterpretował dostęp do **`/proc/sys`** jako dostęp do **`/sys`**, przez co polityka go zablokowała. [Issue runc 4968](https://github.com/opencontainers/runc/issues/4968)

**Dotknięta problemem próba uruchomienia** zgłaszała fragment błędu:

```text
open sysctl net.ipv4.ip_unprivileged_port_start file: reopen fd 8: permission denied
```

Odnotowana awaria uniemożliwiała **uruchomienie kontenera**. Nie wyjaśnia zawieszeń hosta opisanych na forum. Issue wskazuje **`lxc-pve 6.0.5-2`** jako poprawkę Proxmox dla tego konkretnego problemu. Odpowiednia zmiana upstream w LXC została scalona 20 listopada 2025 r. *To historyczne odniesienia do poprawek, a nie zalecenie przypięcia pakietu w obecnej instalacji.* [Podsumowanie poprawki przez opiekuna](https://github.com/opencontainers/runc/issues/4968), [scalona zmiana LXC](https://github.com/lxc/lxc/pull/4609)

Wniosek dotyczy **koordynacji zależności**. Zmiana zabezpieczeń runtime weszła w konflikt z polityką zewnętrznego kontenera, a poprawka wymagała pracy w innej warstwie. Zastosuj odpowiednią aktualizację utrzymywanego pakietu dla swojego wydania. Nie wyłączaj na stałe AppArmor ani nie zachowuj starego, podatnego runtime.

> **Najważniejszy wniosek:** Ten incydent pokazuje rzeczywisty problem zgodności zagnieżdżonych kontenerów i reakcję opiekunów. Nie dowodzi ogólnej niestabilności LXC ani nie wyjaśnia odrębnego zawieszenia hosta.

## Porównaj rzeczywiste koszty

Mierz wydajność na **własnym obciążeniu**. W porównywalnych warunkach zestaw presję pamięci na hoście, użycie CPU, opóźnienia pamięci masowej, czas odpowiedzi aplikacji i wysiłek związany z odzyskiwaniem działania. Przydzielona pamięć RAM VM, wolna pamięć gościa i pamięć rezydentna hosta to różne pomiary.

| Deklarowana oszczędność | Pomiar do zebrania | Dodatkowy koszt do zapisania |
|---|---|---|
| **Mniejszy narzut pamięci** | Użycie i presja pamięci hosta przy tym samym obciążeniu | Czas zarządzania zagnieżdżonymi limitami i diagnozowania konfliktów |
| **Szybsze wdrożenie** | Czas do uruchomienia usługi z odtworzonymi danymi | Czas odbudowy po nieudanej aktualizacji |
| **Prostsze współdzielenie sprzętu** | Wymagane urządzenia, uprawnienia i poprawne działanie aplikacji | Zależność od sterowników hosta i ograniczenia migracji |
| **Łatwiejsze kopie zapasowe** | Udane odtworzenie wszystkich wymaganych danych | Montowania zewnętrzne i spójność aplikacji |

Domyślnie Docker dopuszcza **nieograniczone użycie CPU i pamięci**, o ile nie ustawisz limitów. W LXC własne limity dodaje zewnętrzny kontener. W VM przydział zasobów gościowi tworzy kolejną granicę pojemności. Gość potrzebuje też zasobów dla systemu operacyjnego, Docker, pamięci podręcznych i szczytowego zapotrzebowania aplikacji. [Ograniczenia zasobów Docker](https://docs.docker.com/engine/containers/resource_constraints/)

**Dostęp do sprzętu** wynika z wymagań obciążenia. Współdzielenie hostowego układu graficznego z kontenerem i przypisanie urządzenia PCI do VM wymagają innych konfiguracji sterowników i izolacji. Przed wyborem określ urządzenie i wymagania aplikacji. Na przykład obciążenie multimedialne wymagające dekodowania sprzętowego wymaga po migracji udanego testu dekodowania oraz zwykłych kontroli HTTP.

Unikaj **uniwersalnych wartości narzutu**. Ten artykuł nie podaje stałego zapotrzebowania na RAM ani procentowego wyniku wydajności, ponieważ takie dane wymagają kontrolowanego obciążenia, konfiguracji i metody pomiaru. W poniższym protokole decyzji zapisz wynik własnego porównania.

## Zbieraj dowody według warstwy

**Zacznij od hosta Proxmox**, używając powłoki administratora. Zastąp **`101`** identyfikatorem badanej instancji LXC:

```bash
pveversion -v
uname -r
pct config 101
journalctl --list-boots
journalctl -k -b -1 --no-pager
```

**`pveversion -v`** zapisuje wersje zainstalowanych składników Proxmox. **`pct config`** zapisuje konfigurację zewnętrznego kontenera. W **`journalctl`** opcja **`-k`** wybiera komunikaty jądra, **`-b -1`** wybiera poprzednie uruchomienie, a **`--no-pager`** zwraca zwykły tekst w terminalu. Odczyt komunikatów z poprzedniego uruchomienia wymaga zachowanych danych dziennika. [Zestaw narzędzi Proxmox](https://github.com/proxmox/pve-docs/blob/master/pct.adoc), [dokumentacja journalctl systemd](https://github.com/systemd/systemd/blob/main/man/journalctl.xml)

**Następnie sprawdź hosta Docker** wewnątrz LXC lub VM, gdzie działa demon:

```bash
docker version
docker info
docker compose version
docker ps -a
docker stats --no-stream
```

Zapisz informacje o **obu środowiskach**. Sam tag obrazu kontenera nie podaje wersji Docker, containerd, runc, jądra hosta, polityki bezpieczeństwa ani backendu pamięci masowej. Zapisz czas incydentu, ostatnie aktualizacje i informację, czy lokalna konsola hosta reagowała. Przed publikacją materiału diagnostycznego usuń dane uwierzytelniające i prywatne szczegóły aplikacji.

**Sprawdź konkretne obciążenie**, zastępując **`app`** nazwą kontenera:

```bash
docker inspect --format '{{json .State}}' app
docker inspect --format '{{.RestartCount}}' app
docker inspect --format '{{json .Mounts}}' app
```

**`docker inspect`** pokazuje stan, liczbę restartów i informacje o montowaniach wskazanego kontenera. Traktuj liczbę restartów jako wskazówkę do porównania z logami, a nie dowód wady hosta. Odtworzony kontener zaczyna też nową historię. [Dokumentacja docker inspect](https://docs.docker.com/reference/cli/docker/inspect/)

## Odróżnij presję od zawieszenia

**Podczas narastania problemu zbieraj na hoście informacje o presji systemu Linux:**

```bash
cat /proc/pressure/cpu
cat /proc/pressure/memory
cat /proc/pressure/io
```

**Pressure Stall Information**, czyli PSI, raportuje czas utracony przez zadania oczekujące na zasoby. Pola **`some`** i **`full`** opisują różne warunki zastoju, a **`avg10`**, **`avg60`** i **`avg300`** podsumowują ostatnie okresy. Presja pamięci różni się od jej zajętości. Sama duża pamięć podręczna nie dowodzi niedoboru. [Dokumentacja PSI Linux](https://docs.kernel.org/accounting/psi.html)

| Dowód | Przydatna interpretacja | Następna kontrola |
|---|---|---|
| **Jeden kontener wielokrotnie się zatrzymuje** | Awaria aplikacji lub runtime kontenera | Stan zakończenia, logi usługi, zasady restartu |
| **SSH nie działa, konsola działa** | Awaria sieci lub ścieżki zarządzania | Stan łącza, sterownik NIC, bridge, zapora |
| **Memory PSI rośnie pod obciążeniem** | Zadania tracą czas z powodu konkurencji o pamięć | Limity, odzyskiwanie pamięci, wpisy OOM, wzrost obciążenia |
| **Żądania pamięci masowej się blokują** | Zależność I/O opóźnia pracę | Stan urządzenia, logi pamięci masowej, opóźnienia i kolejki |
| **Watchdog zgłasza lockup** | Detektor jądra wykrył określony zastój | Pełny ślad, wersja jądra, odtwarzalny czynnik wyzwalający |
| **Brak ostatniego wpisu logu** | Zbieranie dowodów zakończyło się przed uzyskaniem użytecznych danych | Trwały lub zewnętrzny zapis przed kolejnym wystąpieniem |

**Zgłoszenie lockupu Linux** ma konkretne znaczenie techniczne. Watchdogi jądra rozróżniają miękkie i twarde lockupy. Przekroczenie czasu odpowiedzi w przeglądarce nie dowodzi żadnego z nich. Brak zgłoszenia watchdog nie dowodzi też, że host działał poprawnie. [Dokumentacja wykrywania lockupów Linux](https://docs.kernel.org/admin-guide/lockup-watchdogs.html)

**Zmiany firmware i stanów zasilania** są eksperymentami. Zapisz poprzednie ustawienie, powód zmiany i okres obserwacji. Wyłączenie stanu bezczynności CPU wpływa na zużycie energii i temperaturę. Zgłoszenie dotyczące innej maszyny nie wystarcza, by zalecić powszechnie takie samo ustawienie.

## Zachowaj przydatne logi

**Trwałe przechowywanie dziennika** zwiększa szansę zachowania dowodów po restarcie. Plik konfiguracyjny journald używa tego ustawienia:

```ini
[Journal]
Storage=persistent
```

**`Storage=persistent`** żąda zapisu dziennika na dysku, jeśli jest dostępny. Ustaw limity retencji i sprawdź dostępną przestrzeń dyskową. Następnie potwierdź, że wcześniejsze uruchomienia są widoczne w **`journalctl --list-boots`**. Trwałe logowanie nadal zależy od zapisania danych przez host przed awarią. [Konfiguracja systemd journald](https://github.com/systemd/systemd/blob/main/man/journald.conf.xml)

**Zewnętrzna obserwacja** dostarcza dodatkowej perspektywy. Monitoruj usługę z innej maszyny i zapisuj znaczniki czasu. Monitor działający na zawieszającym się hoście Proxmox znika podczas tej samej awarii, więc trudniej mu odróżnić przestój od braku telemetrii.

**Przykładowy test:** Zaplanuj lekkie sprawdzenie HTTP z osobnego systemu, a następnie porównaj awarie z dostępnością hosta i zachowaniem lokalnej konsoli. Przekroczenie czasu odpowiedzi aplikacji przy działającym hoście wymaga innej diagnozy niż jednoczesna awaria aplikacji, zarządzania i konsoli. To projekt diagnostyczny, a nie wynik zaobserwowany podczas opisywanego incydentu.

## Zaplanuj kontrolowaną migrację

Zacznij od **jednego projektu Compose o niskim ryzyku**. Przygotuj VM z Debianem w wydaniu wymienionym w dokumentacji instalacji Docker, skonfiguruj kopie zapasowe i przydział zasobów. Zachowaj pierwotne wdrożenie jako opcję wycofania do czasu pomyślnego przejścia testów przez zamiennik. [Instrukcje instalacji Docker dla Debiana](https://docs.docker.com/engine/install/debian/)

**Zrób inwentaryzację projektu Compose** w jego katalogu roboczym:

```bash
docker compose config --quiet
docker compose config --images
docker compose config --volumes
```

**`--quiet`** sprawdza konfigurację bez wyświetlania jej. **`--images`** wyświetla używane obrazy, a **`--volumes`** nazwane wolumeny. Polecenia te nie eksportują danych aplikacji ani nie zapewniają kompletnej listy bind mountów. Sprawdź również plik Compose i montowania każdego kontenera. [Dokumentacja docker compose config](https://docs.docker.com/reference/cli/docker/compose/config/)

| Dane lub zależność | Działanie migracyjne |
|---|---|
| **Definicje Compose** | Przenieś pliki projektu i zachowaj przetestowaną konfigurację |
| **Sekrety i środowisko** | Odtwórz wymagane wartości zgodnie z wybranym procesem zarządzania sekretami |
| **Nazwane wolumeny** | Utwórz kopię i odtwórz zawartość zgodnie z procedurą spójną z aplikacją |
| **Ścieżki bind mountów** | Przenieś lub ponownie podłącz dane źródłowe i sprawdź właściciela |
| **Bazy danych** | Użyj obsługiwanej procedury kopii i odtworzenia lub kopiowania po zatrzymaniu zapisów |
| **Urządzenia i udziały** | Przywróć dostęp i przetestuj działanie aplikacji |
| **Porty i DNS** | Przygotuj nowy adres i zaplanuj przełączenie |

**Wolumeny** istnieją dłużej niż kontenery, ale nie migrują same. Plik Compose nazywa zasoby i definiuje usługi. Dokumentacja wolumenów Docker opisuje osobne operacje tworzenia kopii i przywracania trwałych danych. Ponowne utworzenie projektu nie odtwarza automatycznie danych. [Cykl życia i kopie zapasowe wolumenów Docker](https://docs.docker.com/engine/storage/volumes/)

Osobno sprawdź **zakres kopii zapasowych Proxmox**. Dokumentacja kopii wyklucza zawartość urządzeń i bind mountów z kopii kontenerów. Udana kopia systemu plików root LXC nie potwierdza więc ochrony wszystkich udostępnionych katalogów. [Dokumentacja kopii zapasowych Proxmox](https://github.com/proxmox/pve-docs/blob/master/vzdump.adoc)

### Sprawdź pamięć masową przed kopiowaniem

**Sprawdź rzeczywistą konfigurację pamięci masowej Docker** na każdym hoście Docker:

```bash
docker info
findmnt -T /var/lib/docker
```

**`findmnt`** wskazuje system plików zawierający podaną ścieżkę. Zastąp **`/var/lib/docker`**, jeśli daemon korzysta z innego katalogu danych, i w razie potrzeby sprawdź ścieżkę pamięci masowej containerd. Docker opisuje różnicę między magazynem obrazów containerd a klasycznymi sterownikami pamięci masowej oraz wymagania poszczególnych backendów. [Wybór backendu pamięci masowej Docker](https://docs.docker.com/engine/storage/drivers/select-storage-driver/)

**Odtwórz obrazy i dane aplikacji** zgodnie z dokumentacją wybranego backendu. Kopiowanie działającego katalogu danych Docker między różnymi konfiguracjami pamięci masowej zakłada dodatkowe kwestie metadanych, stanu montowań i spójności. To inna operacja niż kopia wolumenu danych zatrzymanej aplikacji.

### Przełącz usługę z planem wycofania

1. **Przećwicz odtwarzanie** w VM z osobnymi adresami i danymi testowymi, jeśli to właściwe.
2. **Zatrzymaj zapisy produkcyjne** w uzgodnionym oknie przestoju i wykonaj ostatnią spójną kopię zapasową.
3. **Odtwórz i zweryfikuj** dane aplikacji, uprawnienia, dane uwierzytelniające i wymagany dostęp do sprzętu.
4. **Przełącz routing usług** po przejściu przez zamiennik kontroli specyficznych dla aplikacji.
5. **Pozostaw oryginał zatrzymany**, zachowując jego konfigurację i dane odzyskiwania.
6. **Udokumentuj wycofanie** zmian dotyczących danych zapisanych po przełączeniu, zanim uruchomisz stary system.

Unikaj **dwóch aktywnych źródeł zapisu** do tej samej pamięci bazy danych. Wycofanie po nowych zapisach produkcyjnych wymaga planu zachowania tych danych lub świadomego ich odrzucenia. Samo ponowne uruchomienie starego kontenera nie scala dwóch rozbieżnych historii danych.

## Testuj więcej niż uptime

**Testy akceptacyjne** powinny odpowiadać przeznaczeniu usługi. Zielony status kontenera potwierdza działanie procesu. Użyteczna usługa wymaga też danych, dostępu do sieci, zależności i sprawnego odzyskiwania.

| Test | Zachowywany dowód |
|---|---|
| **Działanie aplikacji** | Udana rzeczywista transakcja, kwerenda lub operacja medialna |
| **Kompletność danych** | Oczekiwane rekordy, pliki, uprawnienia i ostatnie zmiany |
| **Ponowne uruchomienie gościa** | Usługi wracają bez ręcznej naprawy |
| **Odtworzenie kopii** | Odtworzona kopia przechodzi ten sam test funkcjonalny |
| **Reprezentatywne obciążenie** | Opóźnienia, CPU, presja pamięci i zachowanie pamięci masowej |
| **Próba konserwacji** | Przetestowana aktualizacja i użyteczna procedura odzyskiwania |
| **Dłuższa obserwacja** | Rejestry dostępności obejmujące kilka poprzednich okresów awarii |

**Przykładowa decyzja:** Usługa kamery i eksperymentalny program pobierający współdzielą jedną zagnieżdżoną konfigurację. Przeniesienie obu do jednej VM poprawia rozdzielenie jąder, ale zachowuje wspólną granicę konserwacji systemu gościa. Jeśli priorytetem jest dostępność kamery, rozważ oddzielne grupy konserwacyjne i limity zasobów, a następnie sprawdź ciągłość nagrań podczas aktualizacji programu pobierającego.

**Oczekiwane rozumowanie:** Wybierz miejsce wdrożenia zgodnie z zależnością usługi, którą chcesz odizolować. Dwie VM na jednym fizycznym serwerze nadal współdzielą zasilanie, pamięć masową i jądro hosta. Jeśli wymaganie obejmuje przetrwanie awarii serwera, potrzebny jest dodatkowy niezależny system lub akceptowalna procedura ręczna.

## Przygotuj protokół decyzji

**Korzystaj z pomiarów**, wybierz wdrożenie i określ, kiedy ponownie je ocenisz:

```text
Service and household impact:
Current host / kernel / LXC / Docker versions:
Required GPU, device, and network access:
Measured memory, CPU, storage, and latency:
Known failure signature and recurrence interval:
Backup coverage and successful restore evidence:
Chosen deployment and reason:
Permitted outage window and recovery target:
Cutover and post-cutover data rollback procedure:
Acceptance tests and observation period:
Condition requiring another architecture review:
```

**Wybierz świadomie zagnieżdżenie LXC**, gdy jego zalety uzasadniają nakład pracy integracyjnej, a ścieżka odzyskiwania została przetestowana. Wybierz VM, gdy typowe środowisko Docker i oddzielne jądro gościa upraszczają działanie usługi. Żadna z tych decyzji nie zastępuje kopii zapasowych, monitorowania ani konserwacji hosta.

## Zastosuj bramkę zmian przed migracją

Traktuj migrację jako **kontrolowaną zmianę**, a nie dowód przyczyny pierwotnego incydentu. Przed przełączeniem zapisz konfigurację kontenerów, skróty obrazów, ścieżki bind mountów, klucze środowiskowe, mapowania urządzeń i wynik ostatniego udanego odtworzenia. Po przełączeniu porównaj te same testy usług i odczyty zasobów. Pozostaw stare obciążenie zatrzymane do czasu przejścia przez nową kopię okresu akceptacji.

Jeśli po migracji incydent powróci, porównaj jądro hosta, pamięć masową, presję pamięci, dostęp do urządzeń i wersje Docker w obu wdrożeniach. Porównanie zawęzi diagnozę. Udana migracja nie staje się eksperymentem przyczynowym, chyba że odpowiednie zmienne pozostały pod kontrolą.

## Następne kroki

**Najpierw zinwentaryzuj jedną usługę.** Określ jej trwałe dane, zależności sprzętowe, objawy awarii i cel odzyskiwania. Przećwicz odtwarzanie przed podjęciem decyzji o migracji.

W ramach **powiązanych materiałów** skorzystaj z [przewodnika aktualizacji Proxmox VE](/articles/proxmox-ve-8-to-9-upgrade-guide/) do planowania aktualizacji i [przewodnika zabezpieczania Docker i Kubernetes](/articles/how-to-secure-your-docker-and-kubernetes-environment/) do wzmacniania ochrony obciążeń. Wybór architektury, wykonanie aktualizacji i diagnozę incydentu traktuj jako odrębne decyzje oparte na własnych dowodach.

## Źródła i dowody

**Stan badań:** 16 września 2026 r. Przekazany transkrypt wskazał temat. Metadane filmu, pierwotny raport o incydencie, issue upstream i oficjalną dokumentację sprawdzono oddzielnie. Ćwiczenia poglądowe i proponowane etapy walidacji oznaczono w tekście.

| Źródło | Rola |
|---|---|
| **[Film źródłowy](https://www.youtube.com/watch?v=XyPBHhZg0Ok)** | Pierwotne omówienie i zgłoszony okres stabilności |
| **[Wątek incydentu Proxmox](https://forum.proxmox.com/threads/pve-host-freezes-every-2-3-weeks.185009/)** | Obserwacje z pierwszej ręki i aktualizacja po migracji |
| **[Zestaw narzędzi kontenerowych Proxmox](https://github.com/proxmox/pve-docs/blob/master/pct.adoc)** | Architektura kontenerów i aktualne rozróżnienie OCI |
| **[Issue runc 4968](https://github.com/opencontainers/runc/issues/4968)** | Udokumentowana awaria uruchamiania i historyczna poprawka pakietu |
| **[Pull request LXC 4609](https://github.com/lxc/lxc/pull/4609)** | Scalona zmiana AppArmor upstream |
| **[Dokumentacja Docker](https://docs.docker.com/engine/install/debian/)** | Podstawa instalacji w gościu, ze szczegółowymi odnośnikami do runtime i pamięci masowej powyżej |
| **[Dokumentacja PSI Linux](https://docs.kernel.org/accounting/psi.html)** | Interpretacja presji zasobów |
| **[Dokumentacja watchdog Linux](https://docs.kernel.org/admin-guide/lockup-watchdogs.html)** | Zdefiniowane warunki lockup jądra |
| **[Dokumentacja kopii zapasowych Proxmox](https://github.com/proxmox/pve-docs/blob/master/vzdump.adoc)** | Wyłączenia montowań kontenerów i działanie kopii zapasowych |
