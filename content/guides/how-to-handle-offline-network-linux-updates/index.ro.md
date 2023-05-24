---
title: "Ghid final: Actualizări offline Linux pentru Ubuntu Debian și CentOS RHEL"
date: 2023-05-30
toc: true
draft: false
description: "Discover the best methods for handling offline Linux updates on Ubuntu/Debian and CentOS/RHEL systems, using local repositories or caches."
tags: ["Actualizări Linux", "Ubuntu", "Debian", "CentOS", "RHEL", "actualizări offline", "depozit local", "cache", "configurarea serverului", "configurarea clientului", "apt-oglindă", "debmirror", "createrepo", "apt-cacher-ng", "yum-cron", "Actualizări de sistem Linux", "actualizări de pachete offline", "actualizări de software offline", "depozitul local de pachete", "memoria cache locală a pachetelor", "actualizări offline Linux", "gestionarea actualizărilor offline", "metode de actualizare offline", "întreținere offline a sistemului", "Actualizări de server Linux", "Actualizări ale clientului Linux", "management software offline", "gestionarea pachetelor offline", "strategii de actualizare", "Actualizări de securitate Linux"]
cover: "/img/cover/A_cartoon_illustration_depicting_a_server_and_multiple_clients.png"
coverAlt: "O ilustrație de desene animate ilustrând un server și mai multe dispozitive client care fac schimb de actualizări offline."
coverCaption: ""
---

**Cele mai bune modalități de a gestiona instalarea actualizărilor Linux offline pentru Ubuntu/Debian și CentOS/RHEL**

Actualizările Linux sunt esențiale pentru menținerea securității și stabilității sistemului dumneavoastră. Cu toate acestea, în unele scenarii, este posibil să aveți de a face cu medii offline în care conectivitatea la internet este limitată sau inexistentă. În astfel de cazuri, devine crucial să existe o strategie adecvată pentru instalarea actualizărilor offline. Acest articol vă va ghida prin **cele mai bune modalități de a gestiona instalarea actualizărilor Linux pentru Ubuntu/Debian și CentOS/RHEL** în medii offline, concentrându-se în special pe utilizarea unui depozit local sau a unui cache.

## Configurarea unui depozit local

Una dintre cele mai eficiente moduri de a gestiona actualizările offline este configurarea unui depozit local. Un depozit local conține toate pachetele software și actualizările necesare, permițându-vă să vă actualizați sistemul fără o conexiune la internet. Iată cum puteți configura un depozit local atât pentru distribuțiile bazate pe Debian, cât și pe cele bazate pe Red Hat:

### Pentru Debian/Ubuntu

1. Începeți prin a configura o **oglindă a depozitului Debian** pe un server care are acces la internet. Puteți folosi instrumente precum [`apt-mirror`](https://manpages.debian.org/jessie/apt-mirror/apt-mirror.1.en.html) or [`debmirror`](https://wiki.debian.org/debmirror) pentru a crea o oglindă locală a depozitelor oficiale Debian sau Ubuntu.

#### Configurarea unei oglinzi a depozitului Debian cu apt-mirror:

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

#### Configurarea unei oglinzi a depozitului Debian cu debmirror:
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
#### Instrucțiuni pentru clientul Debian

2. Configurați depozitul local prin editarea **`/etc/apt/sources.list` fișier pe sistemul offline. Înlocuiți adresele URL implicite ale depozitului cu adresa URL a depozitului local. De exemplu, dacă depozitul dvs. local este găzduit la `http://local-repo/ubuntu` actualizați `sources.list` dosar în consecință.

Exemplu `/etc/apt/sources.list` fişier:
```
deb http://local-repo/ubuntu focal main restricted universe multiverse
```

3. Odată ce configurația este actualizată, puteți rula **`apt update` comanda pe sistemul offline pentru a prelua listele de pachete din depozitul local.

```shell
sudo apt update
```

4. În cele din urmă, puteți utiliza **`apt upgrade` comandă pentru a instala actualizările disponibile din depozitul local.

```shell
sudo apt upgrade
```

### Pentru CentOS/RHEL

1. Pentru a configura un depozit local pentru CentOS/RHEL, trebuie să utilizați [**`createrepo`**](https://linux.die.net/man/8/createrepo) instrument. Acest instrument creează metadatele necesare pentru un depozit local.

2. Creați un director pentru a stoca fișierele de depozit pe un server cu acces la internet. De exemplu, puteți crea un director numit **`local-repo`

3. Copiați toate fișierele relevante ale pachetului RPM și actualizările în **`local-repo` director.

#### Configurarea unui depozit local cu createrepo:

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
4. Odată ce metadatele din depozit sunt generate, puteți transfera întregul `local-repo` directorul către sistemul offline folosind o unitate USB sau orice alt mijloc.

5. În sistemul offline, creați un nou `.repo` dosar în `/etc/yum.repos.d/` director. Furnizați detaliile de configurare necesare, cum ar fi `baseurl` indicând directorul de depozit local.

De exemplu, creați un fișier numit `local.repo` în `/etc/yum.repos.d/` director și adăugați următorul conținut:
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
6. Salvați fișierul și părăsiți editorul.

7. După configurarea depozitului, puteți utiliza comanda yum update pentru a instala actualizări din depozitul local.

```shell
sudo yum update
```

Această comandă va actualiza pachetele din sistem folosind pachetele din depozitul local.

Nu uitați să actualizați magazia locală rulând fișierul `createrepo` comanda ori de câte ori sunt adăugate sau eliminate pachete noi din depozit.

Vă rugăm să rețineți că va trebui să înlocuiți `/path/to/local-repo` cu calea reală către directorul în care ați stocat fișierele de depozit.

## Configurarea unui cache local

O altă abordare pentru a gestiona actualizările offline este configurarea unui cache local. Un cache local stochează pachetele și actualizările descărcate, permițându-vă să le distribuiți pe mai multe sisteme fără a fi nevoie de descărcări individuale. Veți configura acest cache pe un sistem online, apoi mutați directorul într-un sistem care este offline pentru a permite altor sisteme să acceseze pachetele. Iată cum puteți configura un cache local atât pentru distribuțiile bazate pe Debian, cât și pe cele bazate pe Red Hat:

### Pentru Debian/Ubuntu

1. Instalați și configurați [**`apt-cacher-ng`**](https://www.unix-ag.uni-kl.de/~bloch/acng/) un proxy de stocare în cache pentru pachetele Debian/Ubuntu. Îl puteți instala rulând comanda **`sudo apt-get install apt-cacher-ng`

2. Odată instalat, editați **`/etc/apt-cacher-ng/acng.conf` fișier pentru a configura comportamentul de cache. Asigurați-vă că **`PassThroughPattern` parametrul include URL-urile de depozit necesare.

```shell
sudo nano /etc/apt-cacher-ng/acng.conf
```
Anulați comentariile sau adăugați adresele URL de depozit necesare la parametrul PassThroughPattern. De exemplu, pentru a include depozitele Ubuntu, adăugați sau decomentați următoarea linie:
```yml
PassThroughPattern: (security|archive).ubuntu.com/ubuntu
```
Salvați fișierul și ieșiți din editor.

3. Porniți [**`apt-cacher-ng`**](https://www.unix-ag.uni-kl.de/~bloch/acng/) serviciu folosind comanda **`sudo systemctl start apt-cacher-ng`

```shell
sudo systemctl start apt-cacher-ng
```

4. Pe sistemele offline, configurați **`/etc/apt/apt.conf.d/02proxy` fișier pentru a indica memoria cache locală. Utilizați următoarea linie: **`Acquire::http::Proxy "http://<cache-server-ip>:3142";`

```shell
sudo nano /etc/apt/apt.conf.d/02proxy
```
Adăugați următoarea linie la fișier, înlocuind <cache-server-ip> cu adresa IP a serverului cache:
```text
Acquire::http::Proxy "http://<cache-server-ip>:3142";
```
Salvați fișierul și ieșiți din editor

5. Acum, când rulați **`apt update` și **`apt upgrade` comenzile de pe sistemele offline, acestea vor prelua pachetele din memoria cache locală.

```shell
sudo apt update
sudo apt upgrade
```
Aceste comenzi vor prelua și instala actualizările din memoria cache locală, reducând nevoia de acces la internet pe sistemele offline.

Vă rugăm să rețineți că va trebui să înlocuiți **`<cache-server-ip>` cu adresa IP reală a mașinii în care este instalat **apt-cacher-ng**.

### Pentru CentOS/RHEL

1. Pentru CentOS/RHEL, puteți utiliza [**`yum-cron`**](https://linux.die.net/man/8/yum-cron) pentru a configura un cache local. Instalați-l rulând comanda **`sudo yum install yum-cron`

2. Editați **`/etc/yum/yum-cron.conf` fișier și configurați **`download_only` parametru la **`yes` Acest lucru asigură că pachetele sunt descărcate doar și nu instalate automat.

```shell
sudo nano /etc/yum/yum-cron.conf
```

3. Porniți [**`yum-cron`**](https://linux.die.net/man/8/yum-cron) serviciu folosind comanda **`sudo systemctl start yum-cron`

```shell
sudo systemctl start yum-cron
```

4. Pe sistemele offline, creați un director local pentru a stoca pachetele descărcate, de exemplu, **`/var/cache/yum`

```shell
sudo mkdir /var/cache/yum
```

5. Copiați pachetele descărcate din sistemul online în directorul cache local.

```shell
sudo cp -R /var/cache/yum /path/to/local/cache
```

A inlocui `/path/to/local/cache` cu calea către directorul cache local pe sistemul offline.

6. Pe sistemele offline, creați un nou **`.repo` fișier în **`/etc/yum.repos.d/` director, indicând directorul cache local.

```bash
sudo nano /etc/yum.repos.d/local.repo
```
Adăugați următorul conținut la fișier, înlocuind `<local-cache-path>` cu calea către directorul cache local:
```toml
[local]
name=Local Cache
baseurl=file:///path/to/local/cache
enabled=1
gpgcheck=0
```
Salvați fișierul și ieșiți din editor.

7. În cele din urmă, puteți utiliza **`yum update` comanda pe sistemele offline pentru a instala actualizări din memoria cache locală.

```shell
sudo yum update
```

Această comandă va actualiza pachetele de pe sistemele offline folosind pachetele din memoria cache locală.

Vă rugăm să rețineți că va trebui să înlocuiți **`<local-cache-path>` cu calea reală către directorul cache local pe sistemul offline.

______

## Concluzie

Gestionarea actualizărilor Linux în medii offline poate fi o provocare, dar cu abordarea corectă, vă puteți asigura că sistemele dumneavoastră rămân actualizate și securizate. În acest articol, am discutat cele mai bune modalități de a gestiona instalarea actualizărilor offline pentru Ubuntu/Debian și CentOS/RHEL. Am explorat configurarea unui depozit local și configurarea unui cache local, oferind instrucțiuni pas cu pas atât pentru distribuțiile bazate pe Debian, cât și pentru cele bazate pe Red Hat.

Urmând aceste metode, puteți menține securitatea și stabilitatea sistemelor dvs. Linux, chiar și în medii offline. Nu uitați să actualizați periodic depozitul local sau memoria cache pentru a include cele mai recente actualizări.

______

## Referințe

- [apt-mirror Documentation](https://manpages.debian.org/jessie/apt-mirror/apt-mirror.1.en.html)
- [debmirror Documentation](https://wiki.debian.org/debmirror)
- [createrepo Documentation](https://linux.die.net/man/8/createrepo)
- [apt-cacher-ng Documentation](https://www.unix-ag.uni-kl.de/~bloch/acng/)
- [yum-cron Documentation](https://linux.die.net/man/8/yum-cron)
