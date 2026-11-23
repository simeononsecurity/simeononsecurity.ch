---
title: "Przewodnik aktualizacji Proxmox VE 8 do 9"
date: 2026-07-22
lastmod: 2026-11-23
toc: true
draft: false
description: "Aktualizacja Proxmox VE 8 do 9: kontrole wstępne, instrukcje ręczne, automatyzacja, istotne zmiany i odzyskiwanie systemu."
genre: ["Wirtualizacja", "Administracja Linuksem", "Proxmox", "Zarządzanie serwerami", "Oprogramowanie open source", "Domowe laboratorium"]
tags: ["Proxmox VE 9", "aktualizacja Proxmox", "PVE 8 do 9", "Debian Trixie", "Debian 13", "apt dist-upgrade", "pve8to9", "Proxmox Ceph", "proxmox-boot-tool", "grub-efi", "aktualizacja LVM", "aktualizacja ZFS", "NVIDIA vGPU", "cgroupv2", "automatyzacja Proxmox", "skrypt aktualizacyjny Bash", "aktualizacja klastra Proxmox", "aktualizacja na miejscu", "pve8to9-upgrade.sh", "Proxmox VE 9.0"]
cover: "/img/cover/proxmox-ve-8-to-9-upgrade-guide-automation.webp"
coverAlt: "Nowoczesna serwerownia z podświetlonymi ikonami maszyn wirtualnych na ekranach. Technik pracuje przy laptopie pośród ciemnogranatowych urządzeń z niebieskimi, zielonymi i fioletowymi akcentami."
coverCaption: "Aktualizacja Proxmox VE 8 do 9: instrukcja krok po kroku i automatyczny skrypt pomocniczy."
canonical: "https://simeononsecurity.com/articles/proxmox-ve-8-to-9-upgrade-guide/"
---

**Proxmox VE 9.0 wydano na Debianie 13 Trixie z jądrem 6.14, QEMU 10, LXC 6 i ZFS 2.3.** Ten przewodnik opisuje ręczną aktualizację na miejscu oraz skrypt Bash, który wykrywa konfigurację i obsługuje zmiany repozytoriów, znane problemy oraz kontrole przed aktualizacją.

## Co nowego w Proxmox VE 9

Proxmox VE 9 (wydany w sierpniu 2025 r.) to aktualizacja głównej wersji. Najważniejsze zmiany:

| Składnik | PVE 8 | PVE 9.0 |
|-----------|--------|--------|
| **Podstawa Debiana** | Bookworm (12) | Trixie (13) |
| **Domyślne jądro** | 6.8 | 6.14 |
| **QEMU** | 9.x | 10.x |
| **LXC** | 5.x | 6.x |
| **ZFS** | 2.2 | 2.3 |
| **Ceph** | Quincy / Reef / Squid | Squid (19.2) |
| **cgroup** | cgroupv2 (v1 nadal możliwe) | tylko cgroupv2 |

[Proxmox VE 9.2](https://forum.proxmox.com/threads/proxmox-virtual-environment-9-2-available.183742/) domyślnie korzysta z jądra 7.0, QEMU 11, LXC 7 i ZFS 2.4. Domyślnym Ceph w wersji 9.2 jest Tentacle, ale Squid nadal jest dostępny. Aktualizacja klastra Ceph w VE 8 do Squid przed aktualizacją VE stanowi osobny wymóg.

**Najważniejsze nowe funkcje w PVE 9.0+:**
- Migawki maszyn wirtualnych na grubym LVM przez łańcuchy woluminów (wersja testowa, pełna obsługa od 9.1)
- Reguły koligacji wysokiej dostępności zamiast grup HA
- SDN Fabrics dla sieci Ceph full mesh z OpenFabric i OSPF
- Nowy mobilny interfejs WWW (Rust/Yew)
- Rozszerzanie urządzeń ZFS RAIDZ bez przestoju
- Dynamiczne równoważenie obciążenia przez Cluster Resource Scheduler (PVE 9.2)
- WireGuard i BGP jako protokoły SDN Fabric (PVE 9.2)
- `/tmp` jest teraz montowane jako `tmpfs` (zmiana Debiana Trixie, pliki są okresowo usuwane)

{{< figure src="proxmox-ve-8-to-9-component-changes.webp" alt="Diagram porównujący Proxmox VE 8 i VE 9 oraz wersje jądra, QEMU, LXC, ZFS i Ceph" >}}

______

## Zanim zaczniesz: wymagania wstępne

**Spełnij wszystkie poniższe wymagania przed zmianą repozytoriów.** Pełną listę kontroli znajdziesz na [oficjalnej wiki aktualizacji — wymagania wstępne](https://pve.proxmox.com/wiki/Upgrade_from_8_to_9#Prerequisites).

### 1. Wymagany Proxmox VE 8.4

```bash
pveversion
```

Wynik musi wskazywać `pve-manager/8.4.x` lub nowszą wersję. Jeśli nie:

```bash
apt update && apt dist-upgrade
```

### 2. Ceph musi używać Squid (19.x), tylko w klastrach hiperkonwergentnych

```bash
ceph --version
```

Wynik musi wskazywać wersję 19.x (Squid). Jeśli używasz Reef (18.x) lub Quincy (17.x), najpierw zaktualizuj Ceph. Aktualizuj zawsze o jedną wersję naraz:

- Quincy (17) → Reef (18) → Squid (19)

*Nie rozpoczynaj aktualizacji PVE 9, dopóki wszystkie węzły Ceph nie będą używać Squid.*

### 3. Współinstalowany Proxmox Backup Server

Jeśli PBS 3.4 i PVE 8.4 działają na tym samym węźle, postępuj zgodnie z [instrukcją współinstalacji](https://pbs.proxmox.com/wiki/Upgrade_from_3_to_4#Installed_alongside_Proxmox_VE) i skoordynuj obie aktualizacje w ramach jednej operacji APT. Sprawdź, czy kopie zapasowe dają się odtworzyć, oraz uruchom `pve8to9 --full` i `pbs3to4 --full` przed zmianą repozytoriów. Przed kontynuowaniem rozwiąż zgłoszone problemy.

### 4. Wymagany dostęp

- **Zalecany**: dostęp do konsoli przez IPMI, iKVM lub fizyczną klawiaturę. Sesja SSH zostanie przerwana podczas ponownego uruchamiania usług.
- **SSH**: użyj `tmux` lub `screen`, aby aktualizacja trwała dalej po zerwaniu połączenia:
  ```bash
  tmux new -s upgrade
  ```

### 5. Miejsce na dysku

```bash
df -h /
```

Zostaw co najmniej **5 GB** wolnego miejsca, najlepiej 10 GB lub więcej.

### 6. Sprawdzone kopie zapasowe

Przed kontynuowaniem wykonaj kopie wszystkich maszyn wirtualnych i kontenerów na zewnętrznym nośniku. Przetestuj odtwarzanie. Sprawna kopia zapasowa jest niezbędna.

______

## Ważne zmiany, które musisz znać

Przeczytaj tę sekcję przed aktualizacją. Kilka zmian wymaga działania przed aktualizacją lub po niej.

### Usunięto cgroup V1

PVE 9 w ogóle nie obsługuje starszego środowiska cgroupv1. Jeśli wcześniej je włączono:

```bash
grep -E 'cgroup_no_v1|systemd.unified_cgroup_hierarchy=0' /proc/cmdline
```

Jeśli polecenie zwróci wynik, usuń parametr jądra z `/etc/default/grub` i przed aktualizacją uruchom `update-grub`.

**Wpływ na kontenery**: Kontenery z systemd 230 lub starszym (CentOS 7, Ubuntu 16.04) nie uruchomią się w PVE 9. Najpierw przenieś te obciążenia. Wsparcie producenta dla Proxmox VE 8.4 zakończyło się w sierpniu 2026 r.

### Wycofano grupy HA

Reguły HA zastępują grupy HA. Migracja następuje automatycznie, gdy wszystkie węzły klastra korzystają z PVE 9. Nie trzeba wykonywać ręcznych czynności, ale po aktualizacji ostatniego węzła sprawdź wynik migracji.

### Usunięto uprawnienie VM.Monitor

Niestandardowe role zawierające `VM.Monitor` wymagają aktualizacji. Zamiast tego użyj `Sys.Audit`, aby zapewnić podstawowy dostęp do monitora KVM. Skrypt `pve8to9` wykrywa role, których dotyczy problem.

### Nowe uprawnienie: VM.Replicate

Tworzenie i edycja zadań replikacji pamięci masowej wymaga teraz `VM.Replicate` dla `/vms/<vmid>`. W razie potrzeby dostosuj własne role.

### Kontenery LXC z uprawnieniami wymagają Sys.Modify

Tworzenie nowych kontenerów z uprawnieniami wymaga teraz `Sys.Modify`. Odtworzenie istniejącego kontenera z uprawnieniami w tym samym miejscu tego nie wymaga.

### systemd-sysctl nie czyta już /etc/sysctl.conf

Własne ustawienia w `/etc/sysctl.conf` będą po aktualizacji po cichu ignorowane. Przed ponownym uruchomieniem przenieś je do `/etc/sysctl.d/<NN-name.conf>`.

```bash
# Sprawdź zawartość sysctl.conf
grep -v '^\s*#\|^\s*$' /etc/sysctl.conf
```

### /tmp jest teraz tmpfs

Debian Trixie montuje `/tmp` jako tmpfs (do 50% pamięci RAM). Pliki są okresowo usuwane podczas pracy systemu. Jeśli przechowujesz duże pliki tymczasowe w `/tmp`, przenieś je do `/var/tmp` lub na osobny system plików.

### Zgodność kopii zapasowych i odtwarzania Veeam {#veeam-backup-broken-for-qemu-machine-version--100}

Przed aktualizacją sprawdź wersje [Veeam Backup & Replication i wtyczki Proxmox](https://helpcenter.veeam.com/docs/vbr/userguide/pve_system_requirements.html). Aktualne wymagania obejmują Proxmox VE od 8.2 do 9.2 na hostach x86-64 zainstalowanych z oficjalnego obrazu ISO Proxmox. Starsze wersje Veeam mają własne zakresy wsparcia.

Aktualne [ograniczenia Veeam](https://helpcenter.veeam.com/docs/vbr/userguide/pve_limitations.html) obsługują kopie maszyn wirtualnych z pamięci LVM po włączeniu Snapshots as Volume Chains (SAVC). Nie oznacza to, że SAVC jest obsługiwanym miejscem na pliki robocze Veeam ani celem Instant Recovery. Osobny [problem z odtwarzaniem opisany w KB4773](https://www.veeam.com/kb4773) dotyczy typów maszyn QEMU sprzed wersji 10 z dyskami QCOW2 odtwarzanymi do pamięci SAVC w PVE 9. Użyj celu bez SAVC albo odtwórz dysk jako RAW zgodnie z dokumentacją. To obejścia problemu odtwarzania, a nie powód, by przypinać typ maszyny w całym środowisku. Zanim oprzesz się na aktualizacji, przetestuj kopię i odtworzenie na docelowej pamięci.

### Nazwy interfejsów sieciowych mogą się zmienić

Jądro 6.14 rozpoznaje więcej funkcji kart sieciowych niż 6.8. Niektóre karty otrzymają dodatkowe sufiksy w nazwie. Narzędzie `pve-network-interface-pinning` pozwala przed aktualizacją przypisać wszystkim interfejsom stabilne nazwy `nicX`:

```bash
pve-network-interface-pinning --help
```

______

## Opcja A: ręczna aktualizacja na miejscu

Wykonaj oficjalne kroki z [pve.proxmox.com/wiki/Upgrade_from_8_to_9](https://pve.proxmox.com/wiki/Upgrade_from_8_to_9).

### Krok 1: uruchom kontrolę pve8to9

```bash
pve8to9 --full
```

Przed kontynuowaniem rozwiąż wszystkie problemy oznaczone jako `FAIL`. Po każdej poprawce uruchom kontrolę ponownie.

### Krok 2: przenieś uruchomione maszyny wirtualne (jeśli używasz klastra)

```bash
qm migrate <vmid> <target-node>
pct migrate <ctid> <target-node>
```

### Krok 3: w pełni zaktualizuj PVE 8

```bash
apt update && apt dist-upgrade
pveversion   # wynik powinien wskazywać 8.4.1 lub nowszą
```

### Krok 4: zaktualizuj podstawowe repozytoria Debiana

```bash
sed -i 's/bookworm/trixie/g' /etc/apt/sources.list
sed -i 's/bookworm/trixie/g' /etc/apt/sources.list.d/pve-enterprise.list
```

Zakomentuj lub usuń pozostałe wpisy repozytoriów Bookworm.

### Krok 5: dodaj repozytorium pakietów PVE 9

**Enterprise (wymagana subskrypcja):**

```bash
cat > /etc/apt/sources.list.d/pve-enterprise.sources << EOF
Types: deb
URIs: https://enterprise.proxmox.com/debian/pve
Suites: trixie
Components: pve-enterprise
Signed-By: /usr/share/keyrings/proxmox-archive-keyring.gpg
EOF
```

**Bez subskrypcji:**

```bash
cat > /etc/apt/sources.list.d/proxmox.sources << EOF
Types: deb
URIs: http://download.proxmox.com/debian/pve
Suites: trixie
Components: pve-no-subscription
Signed-By: /usr/share/keyrings/proxmox-archive-keyring.gpg
EOF
```

Sprawdź, czy nowe repozytorium pojawia się bez błędów za pomocą `apt update && apt policy`. Następnie usuń lub zakomentuj stary plik `.list`.

### Krok 6: zaktualizuj repozytorium Ceph (tylko w klastrach hiperkonwergentnych)

```bash
cat > /etc/apt/sources.list.d/ceph.sources << EOF
Types: deb
URIs: https://enterprise.proxmox.com/debian/ceph-squid
Suites: trixie
Components: enterprise
Signed-By: /usr/share/keyrings/proxmox-archive-keyring.gpg
EOF
```

W instalacji bez subskrypcji użyj `http://download.proxmox.com/debian/ceph-squid` z `pve-no-subscription`.

### Krok 7: odśwież indeks pakietów

```bash
apt update
```

Sprawdź, czy nie ma błędów.

### Krok 8: wykonaj dist-upgrade

```bash
apt dist-upgrade
```

Zależnie od szybkości pamięci operacja potrwa od 5 do ponad 60 minut. Podczas aktualizacji:

- **`/etc/issue`**: zachowaj bieżącą wersję (bezpiecznie)
- **`/etc/lvm/lvm.conf`**: zainstaluj wersję opiekuna pakietu (zalecane)
- **`/etc/ssh/sshd_config`**: zainstaluj wersję opiekuna pakietu, jeśli nie zmieniałeś pliku
- **`/etc/default/grub`**: zachowaj bieżącą wersję, jeśli plik był zmieniany
- **`/etc/chrony/chrony.conf`**: zainstaluj wersję opiekuna pakietu, jeśli plik nie był zmieniany

### Krok 9: uruchom ponownie system

```bash
reboot
```

Ponowne uruchomienie jest wymagane nawet wtedy, gdy jądro 6.14 było już opcjonalnie zainstalowane w PVE 8. Jądro zostanie ponownie zbudowane przy użyciu łańcuchów narzędzi PVE 9.

### Krok 10: czynności po aktualizacji

```bash
# Wyczyść pamięć podręczną przeglądarki: Ctrl+Shift+R (lub ⌘+Alt+R w macOS)
# Sprawdź wszystkie węzły klastra:
pvesh get /nodes

# W klastrach grupy HA są automatycznie migrowane do reguł HA po aktualizacji wszystkich węzłów do PVE 9
journalctl -eu pve-ha-crm  # sprawdź błędy
```

______

## Opcja B: skrypt automatyczny (pve8to9-upgrade.sh)

Ręczny proces obejmuje wiele kroków zależnych od konfiguracji. Skrypt `pve8to9-upgrade.sh` automatyzuje je wszystkie.

**Źródło skryptu:** [gist.github.com/simeononsecurity/ba3831f487c4e960f9e218c7da5c4b8d](https://gist.github.com/simeononsecurity/ba3831f487c4e960f9e218c7da5c4b8d)

### Co robi skrypt

Skrypt automatycznie przeprowadza całą aktualizację, w tym:

| Wykrywanie | Działanie |
|-----------|--------|
| Repozytoria Enterprise i bez subskrypcji | Używa **aktywnie włączonego** typu repozytorium; nie włącza Enterprise w węzłach bez subskrypcji |
| Wersja Ceph | Zatrzymuje działanie dla Quincy lub Reef i wyświetla szczegółową instrukcję aktualizacji Ceph |
| Typ repozytorium Ceph | Tworzy `ceph.sources` z istniejącym typem repozytorium |
| Sterownik NVIDIA vGPU | Zatrzymuje działanie przy wersji starszej niż 570.158.02 (minimum GRID 18.3) |
| NVIDIA GPU passthrough | Ostrzega i tworzy przypomnienie o teście po aktualizacji |
| Repozytoria CUDA | Zmienia `debian12` na `debian13` w ścieżkach URI |
| Metapakiet systemd-boot | Usuwa go, aby zapobiec błędowi Debiana #1110177 przerywającemu dist-upgrade |
| Własne ustawienia `sysctl.conf` | Przenosi je do `/etc/sysctl.d/99-pve8to9-migrated.conf` |
| Zakleszczenie FRR po uruchomieniu | Zmienia `/etc/network/interfaces` przed ponownym uruchomieniem |
| `systemd-journald-audit.socket` | Wyłącza gniazdo, aby uniknąć zalewania logów podczas aktualizacji |
| Problem GRUB w UEFI + LVM | Instaluje `grub-efi-amd64` i zapisuje ściągawkę w `/root/` |
| Repozytoria zewnętrzne `bookworm` | Zakomentowuje je i przypomina o aktualizacji |
| Konflikt z `linux-image-amd64` | Usuwa pakiet, jeśli jest zainstalowany |
| Automatyczna aktywacja LVM | Uruchamia skrypt migracji przed aktualizacją i po niej |
| Proxmox Backup Server (serwer kopii zapasowych Proxmox) | Uruchamia kontrolę `pbs3to4 --full` i aktualizuje repozytoria PBS dla Trixie |
| ZFS jako system plików głównych | Wykrywa konfigurację i potwierdza ją; dodatkowe działanie nie jest wymagane |

Wszystkie zmiany są zapisywane w `/var/log/pve8to9-upgrade-<timestamp>.log`. Kopie repozytoriów APT trafiają do `/root/pve8to9-apt-backups/`, nigdy jako pliki `.bak` w `/etc/apt/sources.list.d/`. Takie pliki powodowałyby błędy „invalid extension” w interfejsie WWW.

### Instalacja i użycie

```bash
# Pobierz skrypt
curl -fsSL https://gist.githubusercontent.com/simeononsecurity/ba3831f487c4e960f9e218c7da5c4b8d/raw/pve8to9-upgrade.sh \\
  -o pve8to9-upgrade.sh

# Nadaj uprawnienia do uruchamiania
chmod +x pve8to9-upgrade.sh

# Przeczytaj skrypt przed uruchomieniem (zawsze czytaj skrypty przed wykonaniem ich jako root)
less pve8to9-upgrade.sh
```

**Tryby uruchamiania:**

```bash
# Pełny tryb interaktywny (zalecany)
./pve8to9-upgrade.sh

# Automatycznie zatwierdź bezpieczne, niedestrukcyjne poprawki
./pve8to9-upgrade.sh --yes

# Przebieg próbny: pokaż każdą zmianę bez jej wprowadzania
./pve8to9-upgrade.sh --dry-run

# Pomiń wstępną pełną kontrolę pve8to9 (niezalecane)
./pve8to9-upgrade.sh --skip-preflight
```

*Jeśli łączysz się przez SSH, uruchom skrypt wewnątrz `tmux` lub `screen`.*

### Przykładowy wynik działania skryptu

Przed wyświetleniem prośby o kontynuację skrypt podsumowuje wykrytą konfigurację:

```
══════════════════════════════════════════
  SUMMARY of detected configuration
══════════════════════════════════════════

  PVE version      : pve-manager/8.4.3/...
  Debian           : bookworm
  Subscription     : true (status: Active)
  PVE repo type    : enterprise  (enterprise was active: true)
  Ceph             : YES (v19.2.3, enterprise repos)
  ZFS root         : false
  UEFI boot        : true
  LVM root         : true
  NVIDIA           : NO
  CUDA repos       : NO
  systemd-boot     : meta=true efi=true
  sysctl.conf      : custom=false (0 lines)
  cgroupv1         : false (must be false for PVE 9)
  FRR post-up      : false (broken pattern)
  LVM autoact.     : false
  PBS co-install   : NO
  3rd-party bookwm : none
```

### Blokujące kontrole bezpieczeństwa skryptu

Skrypt **odmówi kontynuowania**, jeśli zachodzi którykolwiek z tych warunków:

- cgroup V1 jest jawnie włączone w parametrach jądra
- Ceph nadal używa Quincy (17.x) lub Reef (18.x); skrypt wyświetli dokładne polecenia aktualizacji Ceph
- sterownik NVIDIA vGPU ma wersję starszą niż 570 (GRID 18.3)
- wersja PVE jest starsza niż 8.4

Dla każdego blokującego problemu skrypt wyświetla dokładne polecenia rozwiązania go przed ponownym uruchomieniem.

______

## Znane problemy z aktualizacją

### GRUB nie uruchamia systemu z LVM w trybie UEFI

**Dotyczy**: systemów z głównym systemem plików na LVM, uruchamianych w trybie UEFI i zaktualizowanych z PVE 7.x.

```bash
# Naprawa (uruchom w działającym systemie po aktualizacji):
[ -d /sys/firmware/efi ] && apt install grub-efi-amd64
```

Skrypt `pve8to9-upgrade.sh` wykrywa UEFI + LVM i automatycznie instaluje ten pakiet. Zapisuje też instrukcję odzyskiwania w `/root/GRUB-RECOVERY-CHEATSHEET.txt`.

**Jeśli węzeł utknął** przy `grub rescue>` lub komunikacie „disk 'lvmid/...' not found”:

1. Uruchom obraz ISO PVE → Advanced → **Rescue Boot**
2. Możesz też wykonać [kroki odzyskiwania GRUB dla LVM](https://pve.proxmox.com/wiki/Recover_From_Grub_Failure#Recovering_from_grub_.22disk_not_found.22_error_when_booting_from_LVM) z oficjalnej wiki

### Metapakiet systemd-boot przerywa dist-upgrade

Metapakiet `systemd-boot` instalował się automatycznie w systemach z obrazów ISO PVE 8.1–8.4. W Trixie zawiera haki uruchamiane podczas aktualizacji innych pakietów. Mogą one przerwać `dist-upgrade`, jeśli partycja ESP nie jest zamontowana (błąd Debiana #1110177).

```bash
# Usuń go przed dist-upgrade:
apt remove systemd-boot
# NIE usuwaj systemd-boot-efi ani systemd-boot-tools; pozostają w systemie
```

Skrypt `pve8to9-upgrade.sh` obsługuje to automatycznie i szczegółowo wyjaśnia przyczynę.

### Przekazywanie PCI czasem nie działa z jądrem 6.14

Niektórzy użytkownicy zgłaszają, że maszyny wirtualne z przekazywaniem PCI nie uruchamiają się z jądrem 6.14. Jeśli dotyczy cię ten problem:

```bash
# Tymczasowo przypnij starsze jądro:
proxmox-boot-tool kernel pin 6.8.12-4-pve
```

### Klastry Ceph full mesh blokują się przy ponownym uruchomieniu

Jeśli `/etc/network/interfaces` zawiera:

```
post-up /usr/bin/systemctl restart frr.service
```

Zmień wpis na:

```
post-up /usr/bin/systemctl is-active --quiet frr.service && /usr/bin/systemctl restart frr.service || true
```

Zrób to **przed ponownym uruchomieniem**. Skrypt automatycznie wykrywa i poprawia ten wzorzec.

### Wymagana naprawa puli LVM thin pool

W niektórych systemach po aktualizacji pojawia się komunikat:

```
Check of pool pve/data failed (status:64). Manual repair required!
```

Napraw pulę poleceniem:

```bash
lvconvert --repair pve/data
```

### Minimalna wersja sterownika NVIDIA vGPU

Przed aktualizacją wymagany jest co najmniej **sterownik 570.158.02** (GRID 18.3). Starsze sterowniki nie są zgodne z jądrem 6.x.

```bash
nvidia-smi --query-gpu=driver_version --format=csv,noheader
```

______

## Kolejność aktualizacji klastra

Aktualizuj węzły pojedynczo. Przed rozpoczęciem aktualizacji kolejnego sprawdź, czy poprzedni działa prawidłowo.

```bash
# Przed aktualizacją każdego węzła sprawdź stan klastra:
pvecm status
ceph -s   # jeśli wdrożono Ceph
```

**Zasady migracji podczas częściowej aktualizacji:**

- Maszyna VM/CT z PVE 8 → PVE 9: zawsze działa
- Maszyna VM/CT z PVE 9 → PVE 8: zasadniczo nie jest obsługiwana

Po aktualizacji wszystkich węzłów do PVE 9 grupy HA automatycznie migrują do reguł koligacji HA. Sprawdź błędy:

```bash
journalctl -eu pve-ha-crm
```

______

## Rozwiązywanie problemów

### Aktualizacja zatrzymuje się / pojawia się komunikat „proxmox-ve would be removed”

Jeśli zobaczysz:
```
W: (pve-apt-hook) You are attempting to remove the meta-package 'proxmox-ve'!
```

Niektórych pakietów nie da się zaktualizować, ponieważ nadal skonfigurowano repozytorium Bookworm. Znajdź pozostałe wpisy Bookworm:

```bash
grep -r 'bookworm' /etc/apt/sources.list /etc/apt/sources.list.d/
```

Zakomentuj te wpisy, a następnie uruchom:

```bash
apt update && apt dist-upgrade
```

Jeśli aktualizacja została częściowo ukończona:

```bash
apt -f install
```

### System nie uruchamia się po aktualizacji ZFS

Jeśli używasz ZFS jako głównego systemu plików i starszego rozruchu BIOS, przeczytaj [ZFS: przejście z Legacy Boot na Proxmox Boot Tool](https://pve.proxmox.com/wiki/ZFS:_Switch_Legacy-Boot_to_Proxmox_Boot_Tool). W systemach ZFS rozruchem musi zarządzać `proxmox-boot-tool`, a nie bezpośrednio GRUB. Dzięki temu system pozostanie uruchamialny po aktualizacji funkcji ZFS.

______

## Lista kontrolna po aktualizacji

Po ponownym uruchomieniu każdego węzła sprawdź:

- [ ] Wyczyść pamięć podręczną przeglądarki (`Ctrl+Shift+R` / `⌘+Alt+R`)
- [ ] `pveversion` pokazuje 9.x
- [ ] `uname -r` pokazuje 6.14.x lub nowszą wersję
- [ ] Wszystkie maszyny VM i kontenery CT uruchamiają się poprawnie
- [ ] Stan Ceph: `ceph -s` pokazuje HEALTH_OK
- [ ] Przy UEFI + LVM: sprawdź, czy `grubx64.efi` ma świeży czas modyfikacji
- [ ] Przy NVIDIA passthrough: przetestuj maszynę nieprodukcyjną
- [ ] Zaktualizuj repozytoria zewnętrzne zakomentowane podczas aktualizacji
- [ ] Przenieś własne ustawienia z `/etc/sysctl.conf` do `/etc/sysctl.d/`

______

## Weryfikacja po aktualizacji

Po aktualizacji sprawdź konfigurację repozytoriów, kworum klastra, stan pamięci masowej, uruchamianie gości, kopie zapasowe, reguły zapory i dostęp administracyjny. Przed uznaniem aktualizacji za zakończoną przejrzyj dzienniki systemu. Jeśli klaster na to pozwala, przetestuj odtwarzanie jednej maszyny gościa na osobnym hoście.

Korzystaj z aktualnej [instrukcji administracyjnej Proxmox VE](https://pve.proxmox.com/pve-docs/) i [informacji o wydaniach](https://pve.proxmox.com/wiki/Roadmap), aby dobrać polecenia do swojej wersji. Nie kopiuj polecenia ze starszego wydania bez sprawdzenia docelowej wersji i stanu kopii zapasowej.

## Źródła

1. [Oficjalna aktualizacja Proxmox VE z wersji 8 do 9](https://pve.proxmox.com/wiki/Upgrade_from_8_to_9)
2. [Oficjalne wymagania aktualizacji z wersji 8 do 9](https://pve.proxmox.com/wiki/Upgrade_from_8_to_9#Prerequisites)
3. [Skrypt automatyzujący pve8to9-upgrade.sh](https://gist.github.com/simeononsecurity/ba3831f487c4e960f9e218c7da5c4b8d)
4. [Znane problemy Proxmox VE 9.0 (Roadmap)](https://pve.proxmox.com/wiki/Roadmap#9.0-known-issues)
5. [Odzyskiwanie GRUB — błąd LVM „disk not found”](https://pve.proxmox.com/wiki/Recover_From_Grub_Failure#Recovering_from_grub_.22disk_not_found.22_error_when_booting_from_LVM)
6. [ZFS: przejście z Legacy Boot na Proxmox Boot Tool](https://pve.proxmox.com/wiki/ZFS:_Switch_Legacy-Boot_to_Proxmox_Boot_Tool)
7. [Instrukcja aktualizacji Ceph Reef do Squid](https://pve.proxmox.com/wiki/Ceph_Reef_to_Squid)
8. [Przypinanie interfejsów sieciowych w Proxmox](https://pve.proxmox.com/pve-docs/chapter-sysadmin.html)
9. [Informacje o wydaniu Debian 13 Trixie](https://www.debian.org/releases/trixie/releasenotes)
