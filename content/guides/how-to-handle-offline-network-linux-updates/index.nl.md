---
title: "Ultieme gids: Offline Linux-updates voor Ubuntu Debian en CentOS RHEL"
date: 2023-05-30
toc: true
draft: false
description: "Discover the best methods for handling offline Linux updates on Ubuntu/Debian and CentOS/RHEL systems, using local repositories or caches."
tags: ["Linux-updates", "Ubuntu", "Debian", "CentOS", "RHEL", "offline updates", "lokale opslagplaats", "cache", "server instellen", "klantinstelling", "apt-mirror", "debmirror", "createrepo", "apt-cacher-ng", "yum-cron", "Linux systeem updates", "offline pakket updates", "offline software-updates", "lokale pakketopslagplaats", "lokale pakketcache", "offline Linux-updates", "afhandeling van offline updates", "offline update-methoden", "offline systeemonderhoud", "Linux server updates", "Linux-client updates", "offline softwarebeheer", "offline pakketbeheer", "updatestrategieën", "Linux beveiligingsupdates"]
cover: "/img/cover/A_cartoon_illustration_depicting_a_server_and_multiple_clients.png"
coverAlt: "Een cartoonillustratie van een server en meerdere client-apparaten die offline updates uitwisselen."
coverCaption: ""
---

**Beste manieren om Linux-updates offline te installeren voor Ubuntu/Debian en CentOS/RHEL**.

Linux-updates zijn essentieel voor het behoud van de veiligheid en stabiliteit van uw systeem. In sommige scenario's kunt u echter te maken krijgen met offline omgevingen waar de internetverbinding beperkt of onbestaande is. In dergelijke gevallen wordt het cruciaal om een goede strategie te hebben voor het offline installeren van updates. Dit artikel leidt je door de **beste manieren om Linux updates voor Ubuntu/Debian en CentOS/RHEL** te installeren in offline omgevingen, met speciale aandacht voor het gebruik van een lokale repository of cache.

## Een lokale opslagplaats opzetten

Een van de meest effectieve manieren om offline updates aan te pakken is het opzetten van een lokale repository. Een lokaal archief bevat alle benodigde softwarepakketten en updates, waardoor u uw systeem kunt bijwerken zonder internetverbinding. Hier leest u hoe u een lokaal archief kunt opzetten voor zowel Debian- als Red Hat-distributies:

### Voor Debian/Ubuntu

1. Begin met het opzetten van een **Debian repository mirror** op een server met internettoegang. U kunt tools gebruiken zoals [`apt-mirror`](https://manpages.debian.org/jessie/apt-mirror/apt-mirror.1.en.html) or [`debmirror`](https://wiki.debian.org/debmirror) om een lokale mirror te maken van de officiële Debian of Ubuntu repositories.

#### Het opzetten van een Debian Repository Spiegel met apt-mirror:

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

#### Het opzetten van een Debian Repository Mirror met debmirror:
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
#### Debian-client instructies

2. Configureer uw lokale archief door de ** te bewerken`/etc/apt/sources.list` bestand op het offline systeem. Vervang de standaard archief URL's door de lokale archief URL. Bijvoorbeeld, als je lokale archief gehost wordt op `http://local-repo/ubuntu` de `sources.list` bestand dienovereenkomstig.

Voorbeeld `/etc/apt/sources.list` bestanden:
```
deb http://local-repo/ubuntu focal main restricted universe multiverse
```

3. Zodra de configuratie is bijgewerkt, kunt u de **`apt update` commando op het offline systeem om de pakketlijsten uit het lokale archief op te halen.

```shell
sudo apt update
```

4. Tot slot kunt u de **`apt upgrade` commando om de beschikbare updates uit de lokale repository te installeren.

```shell
sudo apt upgrade
```

### Voor CentOS/RHEL

1. Om een lokale repository voor CentOS/RHEL in te stellen, moet je de [**`createrepo`**](https://linux.die.net/man/8/createrepo) gereedschap. Dit hulpmiddel creëert de nodige metadata voor een lokaal archief.

2. Maak een map om de bestanden van het archief op te slaan op een server met internettoegang. Je kunt bijvoorbeeld een map aanmaken met de naam **`local-repo`

3. Kopieer alle relevante RPM-pakketbestanden en updates naar de **`local-repo` map.

#### Een lokaal archief opzetten met createrepo:

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
4. Zodra de metadata van het archief zijn gegenereerd, kunt u de volledige `local-repo` map naar het offline systeem met behulp van een USB-stick of een ander middel.

5. Maak op het offline systeem een nieuwe `.repo` bestand in de `/etc/yum.repos.d/` directory. Geef de nodige configuratiegegevens, zoals de `baseurl` die naar de lokale archiefmap wijst.

Maak bijvoorbeeld een bestand aan met de naam `local.repo` in de `/etc/yum.repos.d/` directory en voeg de volgende inhoud toe:
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
6. Sla het bestand op en sluit de editor af.

7. Na het configureren van de repository, kun je het yum update commando gebruiken om updates uit de lokale repository te installeren.

```shell
sudo yum update
```

Dit commando zal de pakketten op het systeem bijwerken met de pakketten uit het lokale archief.

Vergeet niet het lokale archief bij te werken door het commando `createrepo` commando wanneer nieuwe pakketten worden toegevoegd of verwijderd uit het archief.

Merk op dat je het volgende moet vervangen `/path/to/local-repo` met het eigenlijke pad naar de map waar u de bestanden van het archief hebt opgeslagen.

## Een lokale cache instellen

Een andere benadering om offline updates af te handelen is het opzetten van een lokale cache. Een lokale cache slaat de gedownloade pakketten en updates op, waardoor je ze over meerdere systemen kunt verspreiden zonder dat je ze afzonderlijk hoeft te downloaden. Je zou deze cache instellen op een online systeem en dan de directory verplaatsen naar een systeem dat offline is om andere systemen toegang te geven tot de pakketten. Hier ziet u hoe u een lokale cache kunt opzetten voor zowel Debian- als Red Hat-gebaseerde distributies:

### Voor Debian/Ubuntu

1. Installeer en configureer [**`apt-cacher-ng`**](https://www.unix-ag.uni-kl.de/~bloch/acng/) een caching proxy voor Debian/Ubuntu-pakketten. U kunt het installeren door het commando ** uit te voeren`sudo apt-get install apt-cacher-ng`

2. Eenmaal geïnstalleerd, bewerkt u de **`/etc/apt-cacher-ng/acng.conf` bestand om het cachinggedrag te configureren. Zorg ervoor dat de **`PassThroughPattern` parameter bevat de noodzakelijke URL's van de opslagplaatsen.

```shell
sudo nano /etc/apt-cacher-ng/acng.conf
```
Haal het commentaar weg of voeg de nodige URL's van de repositories toe aan de PassThroughPattern parameter. Bijvoorbeeld, om de Ubuntu-repositories op te nemen, voeg je de volgende regel toe of maak je het commentaar ongedaan:
```yml
PassThroughPattern: (security|archive).ubuntu.com/ubuntu
```
Sla het bestand op en sluit de editor af.

3. Start de [**`apt-cacher-ng`**](https://www.unix-ag.uni-kl.de/~bloch/acng/) dienst met het commando **`sudo systemctl start apt-cacher-ng`

```shell
sudo systemctl start apt-cacher-ng
```

4. Configureer op de offline systemen de **`/etc/apt/apt.conf.d/02proxy` bestand te verwijzen naar de lokale cache. Gebruik de volgende regel: **`Acquire::http::Proxy "http://<cache-server-ip>:3142";`

```shell
sudo nano /etc/apt/apt.conf.d/02proxy
```
Voeg de volgende regel toe aan het bestand en vervang <cache-server-ip> door het IP-adres van de cachingserver:
```text
Acquire::http::Proxy "http://<cache-server-ip>:3142";
```
Sla het bestand op en sluit de editor af

5. Wanneer u nu de **`apt update` en **`apt upgrade` commando's op de offline systemen, zullen ze de pakketten ophalen uit de lokale cache.

```shell
sudo apt update
sudo apt upgrade
```
Deze commando's zullen de updates ophalen en installeren vanuit de lokale cache, waardoor er minder behoefte is aan internettoegang op de offline systemen.

Merk op dat u **`<cache-server-ip>` met het werkelijke IP-adres van de machine waarop **apt-cacher-ng** is geïnstalleerd.

### Voor CentOS/RHEL

1. Voor CentOS/RHEL kunt u het volgende gebruiken [**`yum-cron`**](https://linux.die.net/man/8/yum-cron) om een lokale cache in te stellen. Installeer het door het commando ** uit te voeren`sudo yum install yum-cron`

2. Bewerk de **`/etc/yum/yum-cron.conf` bestand en configureer de **`download_only` parameter naar **`yes` Dit zorgt ervoor dat de pakketten alleen worden gedownload en niet automatisch worden geïnstalleerd.

```shell
sudo nano /etc/yum/yum-cron.conf
```

3. Start de [**`yum-cron`**](https://linux.die.net/man/8/yum-cron) dienst met het commando **`sudo systemctl start yum-cron`

```shell
sudo systemctl start yum-cron
```

4. Maak op de offline systemen een lokale map aan om de gedownloade pakketten in op te slaan, bijvoorbeeld **`/var/cache/yum`

```shell
sudo mkdir /var/cache/yum
```

5. Kopieer de gedownloade pakketten van het online systeem naar de lokale cache-directory.

```shell
sudo cp -R /var/cache/yum /path/to/local/cache
```

Vervang `/path/to/local/cache` met het pad naar de lokale cachemap op het offline systeem.

6. Maak op de offline systemen een nieuwe **`.repo` bestand in de **`/etc/yum.repos.d/` directory, die verwijst naar de lokale cache directory.

```bash
sudo nano /etc/yum.repos.d/local.repo
```
Voeg de volgende inhoud toe aan het bestand, ter vervanging van `<local-cache-path>` met het pad naar de lokale cache-map:
```toml
[local]
name=Local Cache
baseurl=file:///path/to/local/cache
enabled=1
gpgcheck=0
```
Sla het bestand op en sluit de editor af.

7. Tot slot kunt u de **`yum update` commando op de offline systemen om updates uit de lokale cache te installeren.

```shell
sudo yum update
```

Dit commando zal de pakketten op de offline systemen bijwerken met behulp van de pakketten uit de lokale cache.

Merk op dat u **`<local-cache-path>` met het werkelijke pad naar de lokale cache-map op het offline systeem.

______

## Conclusie

Omgaan met Linux-updates in offline omgevingen kan een uitdaging zijn, maar met de juiste aanpak kunt u ervoor zorgen dat uw systemen up-to-date en veilig blijven. In dit artikel hebben we de beste manieren besproken om updates offline te installeren voor Ubuntu/Debian en CentOS/RHEL. We onderzochten het opzetten van een lokale repository en het opzetten van een lokale cache, met stapsgewijze instructies voor zowel op Debian als Red Hat gebaseerde distributies.

Door deze methoden te volgen, kunt u de veiligheid en stabiliteit van uw Linux-systemen handhaven, zelfs in offline-omgevingen. Vergeet niet om je lokale repository of cache regelmatig bij te werken met de laatste updates.

______

## Referenties

- [apt-mirror Documentation](https://manpages.debian.org/jessie/apt-mirror/apt-mirror.1.en.html)
- [debmirror Documentation](https://wiki.debian.org/debmirror)
- [createrepo Documentation](https://linux.die.net/man/8/createrepo)
- [apt-cacher-ng Documentation](https://www.unix-ag.uni-kl.de/~bloch/acng/)
- [yum-cron Documentation](https://linux.die.net/man/8/yum-cron)
