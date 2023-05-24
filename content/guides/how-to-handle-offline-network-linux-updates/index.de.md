---
title: "Ultimativer Leitfaden: Offline-Linux-Updates für Ubuntu Debian und CentOS RHEL"
date: 2023-05-30
toc: true
draft: false
description: "Discover the best methods for handling offline Linux updates on Ubuntu/Debian and CentOS/RHEL systems, using local repositories or caches."
tags: ["Linux-Updates", "Ubuntu", "Debian", "CentOS", "RHEL", "Offline-Updates", "lokales Repository", "Zwischenspeicher", "Server-Setup", "Client-Setup", "passender Spiegel", "debmirror", "createrepo", "apt-cacher-ng", "lecker-cron", "Linux-Systemaktualisierungen", "Offline-Paketaktualisierungen", "Offline-Software-Updates", "lokales Paket-Repository", "lokaler Paketcache", "Offline-Linux-Updates", "Umgang mit Offline-Updates", "Offline-Update-Methoden", "Offline-Systemwartung", "Linux-Server-Updates", "Linux-Client-Updates", "Offline-Softwareverwaltung", "Offline-Paketverwaltung", "Update-Strategien", "Linux-Sicherheitsupdates"]
cover: "/img/cover/A_cartoon_illustration_depicting_a_server_and_multiple_clients.png"
coverAlt: "Eine Cartoon-Illustration, die einen Server und mehrere Client-Geräte zeigt, die offline Updates austauschen."
coverCaption: ""
---

**Beste Methoden zur Offline-Installation von Linux-Updates für Ubuntu/Debian und CentOS/RHEL**

Linux-Updates sind für die Aufrechterhaltung der Sicherheit und Stabilität Ihres Systems unerlässlich. In einigen Szenarien müssen Sie sich jedoch möglicherweise mit Offline-Umgebungen auseinandersetzen, in denen die Internetverbindung eingeschränkt oder nicht vorhanden ist. In solchen Fällen ist es von entscheidender Bedeutung, über eine geeignete Strategie für die Offline-Installation von Updates zu verfügen. Dieser Artikel führt Sie durch die **besten Methoden zur Installation von Linux-Updates für Ubuntu/Debian und CentOS/RHEL** in Offline-Umgebungen, wobei der Schwerpunkt insbesondere auf der Verwendung eines lokalen Repositorys oder Caches liegt.

## Einrichten eines lokalen Repositorys

Eine der effektivsten Möglichkeiten, Offline-Updates durchzuführen, ist die Einrichtung eines lokalen Repositorys. Ein lokales Repository enthält alle notwendigen Softwarepakete und Updates, sodass Sie Ihr System ohne Internetverbindung aktualisieren können. So können Sie ein lokales Repository sowohl für Debian-basierte als auch für Red Hat-basierte Distributionen einrichten:

### Für Debian/Ubuntu

1. Beginnen Sie mit der Einrichtung eines **Debian-Repository-Spiegels** auf einem Server mit Internetzugang. Sie können Tools wie verwenden [`apt-mirror`](https://manpages.debian.org/jessie/apt-mirror/apt-mirror.1.en.html) or [`debmirror`](https://wiki.debian.org/debmirror) um einen lokalen Spiegel der offiziellen Debian- oder Ubuntu-Repositorys zu erstellen.

#### Einrichten eines Debian-Repository-Spiegels mit apt-mirror:

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

#### Einrichten eines Debian-Repository-Spiegels mit Debmirror:
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
#### Debian-Client-Anweisungen

2. Konfigurieren Sie Ihr lokales Repository, indem Sie ** bearbeiten`/etc/apt/sources.list` Datei auf dem Offline-System. Ersetzen Sie die Standard-Repository-URLs durch die lokale Repository-URL. Wenn Ihr lokales Repository beispielsweise unter gehostet wird `http://local-repo/ubuntu` Aktualisieren Sie die `sources.list` entsprechend einreichen.

Beispiel `/etc/apt/sources.list` Datei:
```
deb http://local-repo/ubuntu focal main restricted universe multiverse
```

3. Sobald die Konfiguration aktualisiert ist, können Sie ** ausführen`apt update` Befehl auf dem Offline-System, um die Paketlisten aus dem lokalen Repository abzurufen.

```shell
sudo apt update
```

4. Schließlich können Sie das ** verwenden`apt upgrade` Befehl zum Installieren der verfügbaren Updates aus dem lokalen Repository.

```shell
sudo apt upgrade
```

### Für CentOS/RHEL

1. Um ein lokales Repository für CentOS/RHEL einzurichten, müssen Sie das verwenden [**`createrepo`**](https://linux.die.net/man/8/createrepo) Werkzeug. Dieses Tool erstellt die notwendigen Metadaten für ein lokales Repository.

2. Erstellen Sie ein Verzeichnis zum Speichern der Repository-Dateien auf einem Server mit Internetzugang. Sie können beispielsweise ein Verzeichnis mit dem Namen ** erstellen`local-repo`

3. Kopieren Sie alle relevanten RPM-Paketdateien und Updates in das **`local-repo` Verzeichnis.

#### Einrichten eines lokalen Repositorys mit createrepo:

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
4. Sobald die Repository-Metadaten generiert sind, können Sie sie vollständig übertragen `local-repo` Verzeichnis über ein USB-Laufwerk oder auf andere Weise auf das Offline-System übertragen.

5. Erstellen Sie auf dem Offline-System ein neues `.repo` Datei in der `/etc/yum.repos.d/` Verzeichnis. Geben Sie die erforderlichen Konfigurationsdetails an, z `baseurl` zeigt auf das lokale Repository-Verzeichnis.

Erstellen Sie beispielsweise eine Datei mit dem Namen `local.repo` im `/etc/yum.repos.d/` Verzeichnis und fügen Sie den folgenden Inhalt hinzu:
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
6. Speichern Sie die Datei und verlassen Sie den Editor.

7. Nachdem Sie das Repository konfiguriert haben, können Sie mit dem Befehl yum update Updates aus dem lokalen Repository installieren.

```shell
sudo yum update
```

Dieser Befehl aktualisiert die Pakete auf dem System mithilfe der Pakete aus dem lokalen Repository.

Denken Sie daran, das lokale Repository zu aktualisieren, indem Sie Folgendes ausführen `createrepo` Befehl immer dann, wenn neue Pakete zum Repository hinzugefügt oder daraus entfernt werden.

Bitte beachten Sie, dass ein Austausch erforderlich ist `/path/to/local-repo` mit dem tatsächlichen Pfad zu dem Verzeichnis, in dem Sie die Repository-Dateien gespeichert haben.

## Einrichten eines lokalen Caches

Ein weiterer Ansatz zur Handhabung von Offline-Updates ist die Einrichtung eines lokalen Caches. Ein lokaler Cache speichert die heruntergeladenen Pakete und Updates, sodass Sie sie auf mehrere Systeme verteilen können, ohne dass einzelne Downloads erforderlich sind. Sie würden diesen Cache auf einem Online-System einrichten und dann das Verzeichnis auf ein Offline-System verschieben, um anderen Systemen den Zugriff auf die Pakete zu ermöglichen. So können Sie einen lokalen Cache sowohl für Debian-basierte als auch für Red Hat-basierte Distributionen einrichten:

### Für Debian/Ubuntu

1. Installieren und konfigurieren [**`apt-cacher-ng`**](https://www.unix-ag.uni-kl.de/~bloch/acng/) ein Caching-Proxy für Debian/Ubuntu-Pakete. Sie können es installieren, indem Sie den Befehl ** ausführen`sudo apt-get install apt-cacher-ng`

2. Bearbeiten Sie nach der Installation das **`/etc/apt-cacher-ng/acng.conf` Datei zum Konfigurieren des Caching-Verhaltens. Stellen Sie sicher, dass **`PassThroughPattern` Der Parameter enthält die erforderlichen Repository-URLs.

```shell
sudo nano /etc/apt-cacher-ng/acng.conf
```
Entfernen Sie die Kommentarzeichen oder fügen Sie die erforderlichen Repository-URLs zum PassThroughPattern-Parameter hinzu. Um beispielsweise die Ubuntu-Repositorys einzuschließen, fügen Sie die folgende Zeile hinzu oder entfernen Sie ihre Auskommentierung:
```yml
PassThroughPattern: (security|archive).ubuntu.com/ubuntu
```
Speichern Sie die Datei und verlassen Sie den Editor.

3. Starten Sie die [**`apt-cacher-ng`**](https://www.unix-ag.uni-kl.de/~bloch/acng/) Dienst mit dem Befehl **`sudo systemctl start apt-cacher-ng`

```shell
sudo systemctl start apt-cacher-ng
```

4. Konfigurieren Sie auf den Offline-Systemen die **`/etc/apt/apt.conf.d/02proxy` Datei so, dass sie auf den lokalen Cache verweist. Verwenden Sie die folgende Zeile: **`Acquire::http::Proxy "http://<cache-server-ip>:3142";`

```shell
sudo nano /etc/apt/apt.conf.d/02proxy
```
Fügen Sie der Datei die folgende Zeile hinzu und ersetzen Sie <cache-server-ip> durch die IP-Adresse des Cache-Servers:
```text
Acquire::http::Proxy "http://<cache-server-ip>:3142";
```
Speichern Sie die Datei und verlassen Sie den Editor

5. Wenn Sie nun ** ausführen`apt update` Und **`apt upgrade` Befehle auf den Offline-Systemen ausführen, rufen sie die Pakete aus dem lokalen Cache ab.

```shell
sudo apt update
sudo apt upgrade
```
Diese Befehle rufen die Updates aus dem lokalen Cache ab und installieren sie, wodurch die Notwendigkeit eines Internetzugangs auf den Offline-Systemen verringert wird.

Bitte beachten Sie, dass Sie ** ersetzen müssen`<cache-server-ip>` mit der tatsächlichen IP-Adresse des Computers, auf dem **apt-cacher-ng** installiert ist.

### Für CentOS/RHEL

1. Für CentOS/RHEL können Sie verwenden [**`yum-cron`**](https://linux.die.net/man/8/yum-cron) um einen lokalen Cache einzurichten. Installieren Sie es, indem Sie den Befehl ** ausführen`sudo yum install yum-cron`

2. Bearbeiten Sie das **`/etc/yum/yum-cron.conf` Datei und konfigurieren Sie die **`download_only` Parameter zu **`yes` Dadurch wird sichergestellt, dass die Pakete nur heruntergeladen und nicht automatisch installiert werden.

```shell
sudo nano /etc/yum/yum-cron.conf
```

3. Starten Sie die [**`yum-cron`**](https://linux.die.net/man/8/yum-cron) Dienst mit dem Befehl **`sudo systemctl start yum-cron`

```shell
sudo systemctl start yum-cron
```

4. Erstellen Sie auf den Offline-Systemen ein lokales Verzeichnis zum Speichern der heruntergeladenen Pakete, zum Beispiel **`/var/cache/yum`

```shell
sudo mkdir /var/cache/yum
```

5. Kopieren Sie die heruntergeladenen Pakete vom Online-System in das lokale Cache-Verzeichnis.

```shell
sudo cp -R /var/cache/yum /path/to/local/cache
```

Ersetzen `/path/to/local/cache` mit dem Pfad zum lokalen Cache-Verzeichnis auf dem Offline-System.

6. Erstellen Sie auf den Offline-Systemen ein neues **`.repo` Datei im **`/etc/yum.repos.d/` Verzeichnis, das auf das lokale Cache-Verzeichnis verweist.

```bash
sudo nano /etc/yum.repos.d/local.repo
```
Fügen Sie der Datei den folgenden Inhalt hinzu und ersetzen Sie ihn `<local-cache-path>` mit dem Pfad zum lokalen Cache-Verzeichnis:
```toml
[local]
name=Local Cache
baseurl=file:///path/to/local/cache
enabled=1
gpgcheck=0
```
Speichern Sie die Datei und verlassen Sie den Editor.

7. Schließlich können Sie das ** verwenden`yum update` Befehl auf den Offline-Systemen, um Updates aus dem lokalen Cache zu installieren.

```shell
sudo yum update
```

Dieser Befehl aktualisiert die Pakete auf den Offline-Systemen mithilfe der Pakete aus dem lokalen Cache.

Bitte beachten Sie, dass Sie ** ersetzen müssen`<local-cache-path>` mit dem tatsächlichen Pfad zum lokalen Cache-Verzeichnis auf dem Offline-System.

______

## Abschluss

Die Handhabung von Linux-Updates in Offline-Umgebungen kann eine Herausforderung sein, aber mit dem richtigen Ansatz können Sie sicherstellen, dass Ihre Systeme auf dem neuesten Stand und sicher bleiben. In diesem Artikel haben wir die besten Möglichkeiten zur Offline-Installation von Updates für Ubuntu/Debian und CentOS/RHEL besprochen. Wir haben die Einrichtung eines lokalen Repositorys und eines lokalen Caches untersucht und Schritt-für-Schritt-Anleitungen sowohl für Debian-basierte als auch für Red Hat-basierte Distributionen bereitgestellt.

Wenn Sie diese Methoden befolgen, können Sie die Sicherheit und Stabilität Ihrer Linux-Systeme auch in Offline-Umgebungen aufrechterhalten. Denken Sie daran, Ihr lokales Repository oder Ihren Cache regelmäßig zu aktualisieren, um die neuesten Updates aufzunehmen.

______

## Verweise

- [apt-mirror Documentation](https://manpages.debian.org/jessie/apt-mirror/apt-mirror.1.en.html)
- [debmirror Documentation](https://wiki.debian.org/debmirror)
- [createrepo Documentation](https://linux.die.net/man/8/createrepo)
- [apt-cacher-ng Documentation](https://www.unix-ag.uni-kl.de/~bloch/acng/)
- [yum-cron Documentation](https://linux.die.net/man/8/yum-cron)
