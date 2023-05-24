---
title: "Guia definitiva: actualitzacions fora de línia de Linux per a Ubuntu Debian i CentOS RHEL"
date: 2023-05-30
toc: true
draft: false
description: "Discover the best methods for handling offline Linux updates on Ubuntu/Debian and CentOS/RHEL systems, using local repositories or caches."
tags: ["Actualitzacions de Linux", "Ubuntu", "Debian", "CentOS", "RHEL", "actualitzacions fora de línia", "repositori local", "memòria cau", "configuració del servidor", "configuració del client", "mirall apte", "debmirror", "crearrepo", "apt-cacher-ng", "yum-cron", "Actualitzacions del sistema Linux", "actualitzacions de paquets fora de línia", "actualitzacions de programari fora de línia", "dipòsit local de paquets", "memòria cau de paquets locals", "actualitzacions fora de línia de Linux", "gestionar les actualitzacions fora de línia", "mètodes d'actualització fora de línia", "manteniment del sistema fora de línia", "Actualitzacions del servidor Linux", "Actualitzacions del client Linux", "gestió de programari fora de línia", "gestió de paquets fora de línia", "estratègies d'actualització", "Actualitzacions de seguretat de Linux"]
cover: "/img/cover/A_cartoon_illustration_depicting_a_server_and_multiple_clients.png"
coverAlt: "Una il·lustració de dibuixos animats que representa un servidor i diversos dispositius client intercanviant actualitzacions fora de línia."
coverCaption: ""
---

**Millors maneres de gestionar la instal·lació d'actualitzacions de Linux fora de línia per a Ubuntu/Debian i CentOS/RHEL**

Les actualitzacions de Linux són essencials per mantenir la seguretat i l'estabilitat del vostre sistema. Tanmateix, en alguns escenaris, és possible que hàgiu de fer front a entorns fora de línia on la connectivitat a Internet és limitada o inexistent. En aquests casos, és crucial tenir una estratègia adequada per instal·lar actualitzacions fora de línia. Aquest article us guiarà a través de les **millors maneres de gestionar la instal·lació d'actualitzacions de Linux per a Ubuntu/Debian i CentOS/RHEL** en entorns fora de línia, centrant-vos específicament en l'ús d'un dipòsit o memòria cau local.

## Configuració d'un dipòsit local

Una de les maneres més efectives de gestionar les actualitzacions fora de línia és configurar un dipòsit local. Un repositori local conté tots els paquets de programari i les actualitzacions necessàries, que us permeten actualitzar el vostre sistema sense connexió a Internet. A continuació s'explica com podeu configurar un dipòsit local tant per a distribucions basades en Debian com per a distribucions basades en Red Hat:

### Per a Debian/Ubuntu

1. Comenceu configurant una **mirall del dipòsit de Debian** en un servidor que tingui accés a Internet. Podeu utilitzar eines com [`apt-mirror`](https://manpages.debian.org/jessie/apt-mirror/apt-mirror.1.en.html) or [`debmirror`](https://wiki.debian.org/debmirror) per crear un mirall local dels dipòsits oficials de Debian o Ubuntu.

#### Configuració d'un mirall del dipòsit de Debian amb apt-mirror:

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

#### Configuració d'un mirall del dipòsit de Debian amb debmirror:
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
#### Instruccions del client Debian

2. Configureu el vostre dipòsit local editant el **`/etc/apt/sources.list` fitxer al sistema fora de línia. Substituïu els URL del dipòsit predeterminat per l'URL del dipòsit local. Per exemple, si el vostre dipòsit local està allotjat a `http://local-repo/ubuntu` actualitzar el `sources.list` arxivar en conseqüència.

Exemple `/etc/apt/sources.list` dossier:
```
deb http://local-repo/ubuntu focal main restricted universe multiverse
```

3. Un cop actualitzada la configuració, podeu executar el **`apt update` comanda al sistema fora de línia per obtenir les llistes de paquets del dipòsit local.

```shell
sudo apt update
```

4. Finalment, podeu utilitzar el **`apt upgrade` comanda per instal·lar les actualitzacions disponibles des del dipòsit local.

```shell
sudo apt upgrade
```

### Per a CentOS/RHEL

1. Per configurar un dipòsit local per a CentOS/RHEL, heu d'utilitzar el [**`createrepo`**](https://linux.die.net/man/8/createrepo) eina. Aquesta eina crea les metadades necessàries per a un repositori local.

2. Creeu un directori per emmagatzemar els fitxers del repositori en un servidor amb accés a Internet. Per exemple, podeu crear un directori anomenat **`local-repo`

3. Copieu tots els fitxers i les actualitzacions del paquet RPM rellevants al **`local-repo` directori.

#### Configuració d'un dipòsit local amb createrepo:

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
4. Un cop generades les metadades del repositori, podeu transferir-les senceres `local-repo` directori al sistema fora de línia mitjançant una unitat USB o qualsevol altre mitjà.

5. Al sistema fora de línia, creeu-ne un `.repo` fitxer al `/etc/yum.repos.d/` directori. Proporcioneu els detalls de configuració necessaris, com ara `baseurl` apuntant al directori del dipòsit local.

Per exemple, creeu un fitxer anomenat `local.repo` en el `/etc/yum.repos.d/` directori i afegiu el contingut següent:
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
6. Deseu el fitxer i sortiu de l'editor.

7. Després de configurar el dipòsit, podeu utilitzar l'ordre yum update per instal·lar actualitzacions des del dipòsit local.

```shell
sudo yum update
```

Aquesta ordre actualitzarà els paquets del sistema utilitzant els paquets del repositori local.

Recordeu actualitzar el repositori local executant el fitxer `createrepo` comanda sempre que s'afegeixin o s'eliminin paquets nous del repositori.

Tingueu en compte que haureu de substituir `/path/to/local-repo` amb el camí real al directori on heu emmagatzemat els fitxers del dipòsit.

## Configuració d'una memòria cau local

Un altre enfocament per gestionar les actualitzacions fora de línia és configurar una memòria cau local. Una memòria cau local emmagatzema els paquets i les actualitzacions descarregats, cosa que us permet distribuir-los entre diversos sistemes sense necessitat de descàrregues individuals. Hauríeu de configurar aquesta memòria cau en un sistema en línia i, a continuació, moureu el directori a un sistema que estigui fora de línia per permetre que altres sistemes accedeixin als paquets. A continuació s'explica com podeu configurar una memòria cau local tant per a distribucions basades en Debian com per a Red Hat:

### Per a Debian/Ubuntu

1. Instal·leu i configureu [**`apt-cacher-ng`**](https://www.unix-ag.uni-kl.de/~bloch/acng/) un servidor intermediari de memòria cau per a paquets Debian/Ubuntu. Podeu instal·lar-lo executant l'ordre **`sudo apt-get install apt-cacher-ng`

2. Un cop instal·lat, editeu el **`/etc/apt-cacher-ng/acng.conf` fitxer per configurar el comportament de la memòria cau. Assegureu-vos que el **`PassThroughPattern` El paràmetre inclou els URL del repositori necessaris.

```shell
sudo nano /etc/apt-cacher-ng/acng.conf
```
Descomenteu o afegiu els URL del repositori necessaris al paràmetre PassThroughPattern. Per exemple, per incloure els repositoris d'Ubuntu, afegiu o descomenteu la línia següent:
```yml
PassThroughPattern: (security|archive).ubuntu.com/ubuntu
```
Deseu el fitxer i sortiu de l'editor.

3. Inicieu el [**`apt-cacher-ng`**](https://www.unix-ag.uni-kl.de/~bloch/acng/) servei mitjançant l'ordre **`sudo systemctl start apt-cacher-ng`

```shell
sudo systemctl start apt-cacher-ng
```

4. Als sistemes fora de línia, configureu el **`/etc/apt/apt.conf.d/02proxy` fitxer per apuntar a la memòria cau local. Utilitzeu la línia següent: **`Acquire::http::Proxy "http://<cache-server-ip>:3142";`

```shell
sudo nano /etc/apt/apt.conf.d/02proxy
```
Afegiu la línia següent al fitxer, substituint <cache-server-ip> per l'adreça IP del servidor de memòria cau:
```text
Acquire::http::Proxy "http://<cache-server-ip>:3142";
```
Deseu el fitxer i sortiu de l'editor

5. Ara, quan executeu el **`apt update` i **`apt upgrade` ordres als sistemes fora de línia, recuperaran els paquets de la memòria cau local.

```shell
sudo apt update
sudo apt upgrade
```
Aquestes ordres obtindran i instal·laran les actualitzacions de la memòria cau local, reduint la necessitat d'accés a Internet als sistemes fora de línia.

Tingueu en compte que haureu de substituir **`<cache-server-ip>` amb l'adreça IP real de la màquina on està instal·lat **apt-cacher-ng**.

### Per a CentOS/RHEL

1. Per a CentOS/RHEL, podeu utilitzar [**`yum-cron`**](https://linux.die.net/man/8/yum-cron) per configurar una memòria cau local. Instal·leu-lo executant l'ordre **`sudo yum install yum-cron`

2. Editeu el **`/etc/yum/yum-cron.conf` fitxer i configureu el **`download_only` paràmetre a **`yes` Això garanteix que els paquets només es baixin i no s'instal·lin automàticament.

```shell
sudo nano /etc/yum/yum-cron.conf
```

3. Inicieu el [**`yum-cron`**](https://linux.die.net/man/8/yum-cron) servei mitjançant l'ordre **`sudo systemctl start yum-cron`

```shell
sudo systemctl start yum-cron
```

4. Als sistemes fora de línia, creeu un directori local per emmagatzemar els paquets baixats, per exemple, **`/var/cache/yum`

```shell
sudo mkdir /var/cache/yum
```

5. Copieu els paquets descarregats del sistema en línia al directori de memòria cau local.

```shell
sudo cp -R /var/cache/yum /path/to/local/cache
```

Substitueix `/path/to/local/cache` amb el camí al directori de la memòria cau local al sistema fora de línia.

6. Als sistemes fora de línia, creeu un ** nou`.repo` fitxer al **`/etc/yum.repos.d/` directori, apuntant al directori de la memòria cau local.

```bash
sudo nano /etc/yum.repos.d/local.repo
```
Afegiu el contingut següent al fitxer, substituint `<local-cache-path>` amb el camí al directori de la memòria cau local:
```toml
[local]
name=Local Cache
baseurl=file:///path/to/local/cache
enabled=1
gpgcheck=0
```
Deseu el fitxer i sortiu de l'editor.

7. Finalment, podeu utilitzar el **`yum update` comanda als sistemes fora de línia per instal·lar actualitzacions des de la memòria cau local.

```shell
sudo yum update
```

Aquesta ordre actualitzarà els paquets als sistemes fora de línia utilitzant els paquets de la memòria cau local.

Tingueu en compte que haureu de substituir **`<local-cache-path>` amb el camí real al directori de memòria cau local al sistema fora de línia.

______

## Conclusió

Gestionar les actualitzacions de Linux en entorns fora de línia pot ser un repte, però amb l'enfocament adequat, podeu assegurar-vos que els vostres sistemes es mantinguin actualitzats i segurs. En aquest article, vam parlar de les millors maneres de gestionar la instal·lació d'actualitzacions fora de línia per a Ubuntu/Debian i CentOS/RHEL. Vam explorar la configuració d'un dipòsit local i la configuració d'una memòria cau local, proporcionant instruccions pas a pas per a distribucions basades en Debian i Red Hat.

Seguint aquests mètodes, podeu mantenir la seguretat i l'estabilitat dels vostres sistemes Linux, fins i tot en entorns fora de línia. Recordeu actualitzar periòdicament el vostre dipòsit o memòria cau local per incloure les últimes actualitzacions.

______

## Referències

- [apt-mirror Documentation](https://manpages.debian.org/jessie/apt-mirror/apt-mirror.1.en.html)
- [debmirror Documentation](https://wiki.debian.org/debmirror)
- [createrepo Documentation](https://linux.die.net/man/8/createrepo)
- [apt-cacher-ng Documentation](https://www.unix-ag.uni-kl.de/~bloch/acng/)
- [yum-cron Documentation](https://linux.die.net/man/8/yum-cron)
