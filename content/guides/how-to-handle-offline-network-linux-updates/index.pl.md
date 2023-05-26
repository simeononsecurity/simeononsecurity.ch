---
title: "Kompletny przewodnik: Aktualizacje offline dla Ubuntu, Debiana i CentOS RHEL"
date: 2023-05-30
toc: true
draft: false
description: "Discover the best methods for handling offline Linux updates on Ubuntu/Debian and CentOS/RHEL systems, using local repositories or caches."
tags: ["Aktualizacje systemu Linux", "Ubuntu", "Debian", "CentOS", "RHEL", "aktualizacje offline", "lokalne repozytorium", "cache", "konfiguracja serwera", "konfiguracja klienta", "apt-mirror", "debmirror", "createrepo", "apt-cacher-ng", "yum-cron", "Aktualizacje systemu Linux", "aktualizacje pakietów offline", "aktualizacje oprogramowania offline", "lokalne repozytorium pakietów", "lokalna pamięć podręczna pakietów", "Aktualizacje systemu Linux w trybie offline", "obsługa aktualizacji offline", "metody aktualizacji offline", "konserwacja systemu offline", "Aktualizacje serwerów Linux", "Aktualizacje klienta Linux", "Zarządzanie oprogramowaniem offline", "Zarządzanie pakietami offline", "strategie aktualizacji", "Aktualizacje zabezpieczeń systemu Linux"]
cover: "/img/cover/A_cartoon_illustration_depicting_a_server_and_multiple_clients.png"
coverAlt: "Rysunkowa ilustracja przedstawiająca serwer i wiele urządzeń klienckich wymieniających aktualizacje w trybie offline."
coverCaption: ""
---

**Najlepsze sposoby radzenia sobie z instalacją aktualizacji Linuksa offline dla Ubuntu/Debian i CentOS/RHEL**

Aktualizacje systemu Linux są niezbędne do utrzymania bezpieczeństwa i stabilności systemu. Jednak w niektórych scenariuszach możesz mieć do czynienia ze środowiskami offline, w których łączność z Internetem jest ograniczona lub nie istnieje. W takich przypadkach kluczowe staje się posiadanie odpowiedniej strategii instalowania aktualizacji w trybie offline. Ten artykuł poprowadzi Cię przez **najlepsze sposoby radzenia sobie z instalacją aktualizacji Linuksa dla Ubuntu/Debian i CentOS/RHEL** w środowiskach offline, koncentrując się w szczególności na korzystaniu z lokalnego repozytorium lub pamięci podręcznej.

## Konfiguracja lokalnego repozytorium

Jednym z najskuteczniejszych sposobów obsługi aktualizacji offline jest skonfigurowanie lokalnego repozytorium. Lokalne repozytorium zawiera wszystkie niezbędne pakiety oprogramowania i aktualizacje, umożliwiając aktualizację systemu bez połączenia z Internetem. Oto jak skonfigurować lokalne repozytorium dla dystrybucji opartych na Debianie i Red Hat:

### Dla Debiana/Ubuntu

1. Zacznij od skonfigurowania kopii lustrzanej **repozytorium Debiana** na serwerze z dostępem do Internetu. Możesz użyć narzędzi takich jak [`apt-mirror`](https://manpages.debian.org/jessie/apt-mirror/apt-mirror.1.en.html) or [`debmirror`](https://wiki.debian.org/debmirror) aby utworzyć lokalną kopię lustrzaną oficjalnych repozytoriów Debiana lub Ubuntu.

#### Tworzenie kopii lustrzanej repozytorium Debiana za pomocą apt-mirror:

```shell
# Install apt-mirror
sudo apt-get install apt-mirror

# Edit the apt-mirror configuration file
sudo nano /etc/apt/mirror.list

# Uncomment the deb line for the desired repository
# For example, uncomment the line for Ubuntu 20.04:
# deb http://archive.ubuntu.com/ubuntu focal main restricted universe multiverse

# Specify the mirror location
# Modify the base_path to your desired location
set base_path /path/to/mirror

# Save and close the file

# Run apt-mirror to start the mirroring process
sudo apt-mirror

# Wait for the mirroring process to complete
```

#### Konfigurowanie kopii lustrzanej repozytorium Debiana za pomocą debmirror:
```shell
# Install debmirror
sudo apt-get install debmirror

# Create a directory to store the mirror
sudo mkdir /path/to/mirror

# Run debmirror to start the mirroring process
# Replace <RELEASE> with the Debian or Ubuntu release and <MIRROR_URL> with the official repository URL
# For example, to mirror Ubuntu 20.04:
sudo debmirror --arch=amd64 --verbose --method=http --dist=<RELEASE> --root=<MIRROR_URL> /path/to/mirror

# Wait for the mirroring process to complete
```
#### Instrukcje klienta Debiana

2. Skonfiguruj lokalne repozytorium, edytując **`/etc/apt/sources.list` w systemie offline. Zastąp domyślne adresy URL repozytoriów lokalnymi adresami URL repozytoriów. Na przykład, jeśli lokalne repozytorium jest hostowane pod adresem `http://local-repo/ubuntu` aktualizacja `sources.list` plik odpowiednio.

Przykład `/etc/apt/sources.list` pliki:
```
deb http://local-repo/ubuntu focal main restricted universe multiverse
```

3. Po zaktualizowaniu konfiguracji można uruchomić **`apt update` w systemie offline, aby pobrać listy pakietów z lokalnego repozytorium.

```shell
sudo apt update
```

4. Na koniec można użyć **`apt upgrade` aby zainstalować dostępne aktualizacje z lokalnego repozytorium.

```shell
sudo apt upgrade
```

### Dla CentOS/RHEL

1. Aby skonfigurować lokalne repozytorium dla CentOS/RHEL, należy użyć opcji [**`createrepo`**](https://linux.die.net/man/8/createrepo) tool. Narzędzie to tworzy niezbędne metadane dla lokalnego repozytorium.

2. Utwórz katalog do przechowywania plików repozytorium na serwerze z dostępem do Internetu. Na przykład, można utworzyć katalog o nazwie **`local-repo`

3. Skopiuj wszystkie odpowiednie pliki pakietów RPM i aktualizacje do **`local-repo` katalog.

#### Konfigurowanie lokalnego repozytorium za pomocą createrepo:

```shell
# Install the createrepo tool
sudo yum install createrepo

# Create a directory to store the repository files
sudo mkdir /path/to/local-repo

# Move or copy the RPM package files and updates to the local-repo directory

# Run the createrepo command to generate the necessary repository metadata
sudo createrepo /path/to/local-repo

# Update the repository metadata whenever new packages are added or removed
sudo createrepo --update /path/to/local-repo
```
4. Po wygenerowaniu metadanych repozytorium można przenieść całe repozytorium. `local-repo` do systemu offline za pomocą napędu USB lub w inny sposób.

5. W systemie offline utwórz nowy katalog `.repo` w pliku `/etc/yum.repos.d/` directory. Podaj niezbędne szczegóły konfiguracji, takie jak `baseurl` wskazując na lokalny katalog repozytorium.

Na przykład, utwórz plik o nazwie `local.repo` w `/etc/yum.repos.d/` i dodać następującą zawartość:
```shell
sudo nano /etc/yum.repos.d/local.repo
```
```toml
[local]
name=Local Repository
baseurl=file:///path/to/local-repo
enabled=1
gpgcheck=0
```
6. Zapisz plik i zamknij edytor.

7. Po skonfigurowaniu repozytorium można użyć polecenia yum update, aby zainstalować aktualizacje z lokalnego repozytorium.

```shell
sudo yum update
```

To polecenie zaktualizuje pakiety w systemie przy użyciu pakietów z lokalnego repozytorium.

Pamiętaj, aby zaktualizować lokalne repozytorium, uruchamiając polecenie `createrepo` za każdym razem, gdy nowe pakiety są dodawane lub usuwane z repozytorium.

Należy pamiętać, że trzeba będzie zastąpić `/path/to/local-repo` z rzeczywistą ścieżką do katalogu, w którym przechowywane są pliki repozytorium.

## Konfigurowanie lokalnej pamięci podręcznej

Innym podejściem do obsługi aktualizacji offline jest skonfigurowanie lokalnej pamięci podręcznej. Lokalna pamięć podręczna przechowuje pobrane pakiety i aktualizacje, umożliwiając ich dystrybucję w wielu systemach bez konieczności indywidualnego pobierania. Taką pamięć podręczną należy skonfigurować w systemie online, a następnie przenieść katalog do systemu, który jest offline, aby umożliwić innym systemom dostęp do pakietów. Oto jak skonfigurować lokalną pamięć podręczną dla dystrybucji opartych na Debianie i Red Hat:

### Dla Debiana/Ubuntu

1. Zainstaluj i skonfiguruj [**`apt-cacher-ng`**](https://www.unix-ag.uni-kl.de/~bloch/acng/) buforujący serwer proxy dla pakietów Debiana/Ubuntu. Można go zainstalować, uruchamiając polecenie **`sudo apt-get install apt-cacher-ng`

2. Po zainstalowaniu edytuj **`/etc/apt-cacher-ng/acng.conf` aby skonfigurować zachowanie buforowania. Upewnij się, że **`PassThroughPattern` zawiera niezbędne adresy URL repozytoriów.

```shell
sudo nano /etc/apt-cacher-ng/acng.conf
```
Usuń komentarz lub dodaj niezbędne adresy URL repozytoriów do parametru PassThroughPattern. Na przykład, aby uwzględnić repozytoria Ubuntu, należy dodać lub odkomentować następujący wiersz:
```yml
PassThroughPattern: (security|archive).ubuntu.com/ubuntu
```
Zapisz plik i zamknij edytor.

3. Uruchom aplikację [**`apt-cacher-ng`**](https://www.unix-ag.uni-kl.de/~bloch/acng/) przy użyciu polecenia **`sudo systemctl start apt-cacher-ng`

```shell
sudo systemctl start apt-cacher-ng
```

4. W systemach offline skonfiguruj **`/etc/apt/apt.conf.d/02proxy` aby wskazać lokalną pamięć podręczną. Użyj następującej linii: **`Acquire::http::Proxy "http://<cache-server-ip>:3142";`

```shell
sudo nano /etc/apt/apt.conf.d/02proxy
```
Dodaj następujący wiersz do pliku, zastępując <cache-server-ip> adresem IP serwera pamięci podręcznej:
```text
Acquire::http::Proxy "http://<cache-server-ip>:3142";
```
Zapisz plik i zamknij edytor

5. Teraz, po uruchomieniu **`apt update` i **`apt upgrade` na systemach offline, będą one pobierać pakiety z lokalnej pamięci podręcznej.

```shell
sudo apt update
sudo apt upgrade
```
Polecenia te będą pobierać i instalować aktualizacje z lokalnej pamięci podręcznej, zmniejszając potrzebę dostępu do Internetu w systemach offline.

Należy pamiętać, że konieczne będzie zastąpienie **`<cache-server-ip>` z rzeczywistym adresem IP komputera, na którym zainstalowany jest **apt-cacher-ng**.

### Dla CentOS/RHEL

1. Dla CentOS/RHEL, można użyć [**`yum-cron`**](https://linux.die.net/man/8/yum-cron) aby skonfigurować lokalną pamięć podręczną. Zainstaluj go, uruchamiając polecenie **`sudo yum install yum-cron`

2. Edytuj **`/etc/yum/yum-cron.conf` i skonfigurować **`download_only` parametr do **`yes` Zapewnia to, że pakiety są tylko pobierane, a nie instalowane automatycznie.

```shell
sudo nano /etc/yum/yum-cron.conf
```

3. Uruchomić [**`yum-cron`**](https://linux.die.net/man/8/yum-cron) przy użyciu polecenia **`sudo systemctl start yum-cron`

```shell
sudo systemctl start yum-cron
```

4. W systemach offline utwórz lokalny katalog do przechowywania pobranych pakietów, na przykład **`/var/cache/yum`

```shell
sudo mkdir /var/cache/yum
```

5. Skopiuj pobrane pakiety z systemu online do lokalnego katalogu pamięci podręcznej.

```shell
sudo cp -R /var/cache/yum /path/to/local/cache
```

Wymiana `/path/to/local/cache` ze ścieżką do lokalnego katalogu pamięci podręcznej w systemie offline.

6. W systemach offline utwórz nowy **`.repo` w pliku **`/etc/yum.repos.d/` wskazując na lokalny katalog pamięci podręcznej.

```bash
sudo nano /etc/yum.repos.d/local.repo
```
Dodaj następującą zawartość do pliku, zastępując `<local-cache-path>` ze ścieżką do lokalnego katalogu pamięci podręcznej:
```toml
[local]
name=Local Cache
baseurl=file:///path/to/local/cache
enabled=1
gpgcheck=0
```
Zapisz plik i zamknij edytor.

7. Na koniec możesz użyć **`yum update` w systemach offline, aby zainstalować aktualizacje z lokalnej pamięci podręcznej.

```shell
sudo yum update
```

To polecenie zaktualizuje pakiety w systemach offline przy użyciu pakietów z lokalnej pamięci podręcznej.

Należy pamiętać, że trzeba będzie zastąpić **`<local-cache-path>` z rzeczywistą ścieżką do lokalnego katalogu pamięci podręcznej w systemie offline.

______

## Wnioski

Obsługa aktualizacji systemu Linux w środowiskach offline może stanowić wyzwanie, ale przy odpowiednim podejściu można zapewnić, że systemy pozostaną aktualne i bezpieczne. W tym artykule omówiliśmy najlepsze sposoby radzenia sobie z instalowaniem aktualizacji offline dla Ubuntu/Debian i CentOS/RHEL. Przeanalizowaliśmy konfigurację lokalnego repozytorium i lokalnej pamięci podręcznej, dostarczając instrukcje krok po kroku zarówno dla dystrybucji opartych na Debianie, jak i Red Hat.

Postępując zgodnie z tymi metodami, można zachować bezpieczeństwo i stabilność systemów Linux, nawet w środowiskach offline. Pamiętaj, aby okresowo aktualizować lokalne repozytorium lub pamięć podręczną, aby zawierały najnowsze aktualizacje.

______

## Referencje

- [apt-mirror Documentation](https://manpages.debian.org/jessie/apt-mirror/apt-mirror.1.en.html)
- [debmirror Documentation](https://wiki.debian.org/debmirror)
- [createrepo Documentation](https://linux.die.net/man/8/createrepo)
- [apt-cacher-ng Documentation](https://www.unix-ag.uni-kl.de/~bloch/acng/)
- [yum-cron Documentation](https://linux.die.net/man/8/yum-cron)
