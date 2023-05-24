---
title: "Guida definitiva: aggiornamenti Linux offline per Ubuntu Debian e CentOS RHEL"
date: 2023-05-30
toc: true
draft: false
description: "Discover the best methods for handling offline Linux updates on Ubuntu/Debian and CentOS/RHEL systems, using local repositories or caches."
tags: ["Aggiornamenti Linux", "Ubuntu", "Debian", "CentOS", "REL", "aggiornamenti offline", "deposito locale", "cache", "configurazione del server", "configurazione del cliente", "apt-specchio", "debmirror", "createrepo", "apt-cacher-ng", "yum-cron", "Aggiornamenti del sistema Linux", "aggiornamenti dei pacchetti offline", "aggiornamenti software offline", "repository di pacchetti locale", "cache dei pacchetti locale", "aggiornamenti Linux offline", "gestire gli aggiornamenti offline", "metodi di aggiornamento offline", "manutenzione del sistema offline", "Aggiornamenti del server Linux", "Aggiornamenti del client Linux", "gestione del software offline", "gestione dei pacchetti offline", "aggiornare le strategie", "Aggiornamenti di sicurezza Linux"]
cover: "/img/cover/A_cartoon_illustration_depicting_a_server_and_multiple_clients.png"
coverAlt: "Un fumetto raffigurante un server e più dispositivi client che scambiano aggiornamenti offline."
coverCaption: ""
---

**I modi migliori per gestire l'installazione offline degli aggiornamenti di Linux per Ubuntu/Debian e CentOS/RHEL**

Gli aggiornamenti di Linux sono essenziali per mantenere la sicurezza e la stabilità del tuo sistema. Tuttavia, in alcuni scenari, potresti dover gestire ambienti offline in cui la connettività Internet è limitata o inesistente. In tali casi, diventa fondamentale disporre di una strategia adeguata per l'installazione degli aggiornamenti offline. Questo articolo ti guiderà attraverso i **modi migliori per gestire l'installazione degli aggiornamenti Linux per Ubuntu/Debian e CentOS/RHEL** in ambienti offline, concentrandosi in particolare sull'utilizzo di un repository locale o di una cache.

## Impostazione di un repository locale

Uno dei modi più efficaci per gestire gli aggiornamenti offline consiste nell'impostare un repository locale. Un repository locale contiene tutti i pacchetti software e gli aggiornamenti necessari, consentendoti di aggiornare il tuo sistema senza una connessione Internet. Ecco come configurare un repository locale per distribuzioni basate su Debian e Red Hat:

### Per Debian/Ubuntu

1. Inizia impostando un **debian repository mirror** su un server con accesso a Internet. Puoi usare strumenti come [`apt-mirror`](https://manpages.debian.org/jessie/apt-mirror/apt-mirror.1.en.html) or [`debmirror`](https://wiki.debian.org/debmirror) per creare un mirror locale dei repository Debian o Ubuntu ufficiali.

#### Configurazione di un mirror del repository Debian con apt-mirror:

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

#### Configurazione di un mirror del repository Debian con debmirror:
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
#### Istruzioni per il client Debian

2. Configura il tuo repository locale modificando il **`/etc/apt/sources.list` file sul sistema offline. Sostituisci gli URL del repository predefinito con l'URL del repository locale. Ad esempio, se il tuo repository locale è ospitato su `http://local-repo/ubuntu` aggiornare il `sources.list` file di conseguenza.

Esempio `/etc/apt/sources.list` file:
```
deb http://local-repo/ubuntu focal main restricted universe multiverse
```

3. Una volta aggiornata la configurazione, è possibile eseguire **`apt update` comando sul sistema offline per recuperare gli elenchi dei pacchetti dal repository locale.

```shell
sudo apt update
```

4. Infine, puoi utilizzare **`apt upgrade` comando per installare gli aggiornamenti disponibili dal repository locale.

```shell
sudo apt upgrade
```

### Per CentOS/RHEL

1. Per configurare un repository locale per CentOS/RHEL, è necessario utilizzare il file [**`createrepo`**](https://linux.die.net/man/8/createrepo) attrezzo. Questo strumento crea i metadati necessari per un repository locale.

2. Creare una directory per archiviare i file del repository su un server con accesso a Internet. Ad esempio, puoi creare una directory chiamata **`local-repo`

3. Copiare tutti i file e gli aggiornamenti del pacchetto RPM rilevanti nel **`local-repo` directory.

#### Impostazione di un repository locale con createrepo:

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
4. Una volta generati i metadati del repository, è possibile trasferire l'intero file `local-repo` directory al sistema offline utilizzando un'unità USB o qualsiasi altro mezzo.

5. Sul sistema offline, creare un nuovo file `.repo` file nel `/etc/yum.repos.d/` directory. Fornire i dettagli di configurazione necessari, ad esempio il file `baseurl` che punta alla directory del repository locale.

Ad esempio, crea un file chiamato `local.repo` nel `/etc/yum.repos.d/` directory e aggiungere il seguente contenuto:
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
6. Salvare il file ed uscire dall'editor.

7. Dopo aver configurato il repository, è possibile utilizzare il comando yum update per installare gli aggiornamenti dal repository locale.

```shell
sudo yum update
```

Questo comando aggiornerà i pacchetti sul sistema utilizzando i pacchetti dal repository locale.

Ricordarsi di aggiornare il repository locale eseguendo il file `createrepo` comando ogni volta che vengono aggiunti o rimossi nuovi pacchetti dal repository.

Si prega di notare che sarà necessario sostituire `/path/to/local-repo` con il percorso effettivo della directory in cui sono stati archiviati i file del repository.

## Impostazione di una cache locale

Un altro approccio per gestire gli aggiornamenti offline consiste nell'impostare una cache locale. Una cache locale archivia i pacchetti e gli aggiornamenti scaricati, consentendoti di distribuirli su più sistemi senza la necessità di download individuali. Dovresti impostare questa cache su un sistema online, quindi spostare la directory su un sistema offline per consentire ad altri sistemi di accedere ai pacchetti. Ecco come configurare una cache locale per le distribuzioni basate su Debian e Red Hat:

### Per Debian/Ubuntu

1. Installa e configura [**`apt-cacher-ng`**](https://www.unix-ag.uni-kl.de/~bloch/acng/) un proxy di memorizzazione nella cache per i pacchetti Debian/Ubuntu. Puoi installarlo eseguendo il comando **`sudo apt-get install apt-cacher-ng`

2. Una volta installato, modifica **`/etc/apt-cacher-ng/acng.conf` file per configurare il comportamento della memorizzazione nella cache. Assicurati che **`PassThroughPattern` Il parametro include gli URL del repository necessari.

```shell
sudo nano /etc/apt-cacher-ng/acng.conf
```
Rimuovere il commento o aggiungere gli URL del repository necessari al parametro PassThroughPattern. Ad esempio, per includere i repository di Ubuntu, aggiungi o decommenta la riga seguente:
```yml
PassThroughPattern: (security|archive).ubuntu.com/ubuntu
```
Salva il file ed esci dall'editor.

3. Avviare il file [**`apt-cacher-ng`**](https://www.unix-ag.uni-kl.de/~bloch/acng/) servizio utilizzando il comando **`sudo systemctl start apt-cacher-ng`

```shell
sudo systemctl start apt-cacher-ng
```

4. Sui sistemi offline, configurare **`/etc/apt/apt.conf.d/02proxy` file in modo che punti alla cache locale. Usa la seguente riga: **`Acquire::http::Proxy "http://<cache-server-ip>:3142";`

```shell
sudo nano /etc/apt/apt.conf.d/02proxy
```
Aggiungi la seguente riga al file, sostituendo <cache-server-ip> con l'indirizzo IP del server cache:
```text
Acquire::http::Proxy "http://<cache-server-ip>:3142";
```
Salva il file ed esci dall'editor

5. Ora, quando esegui **`apt update` E **`apt upgrade` comandi sui sistemi offline, recupereranno i pacchetti dalla cache locale.

```shell
sudo apt update
sudo apt upgrade
```
Questi comandi recupereranno e installeranno gli aggiornamenti dalla cache locale, riducendo la necessità di accesso a Internet sui sistemi offline.

Si prega di notare che sarà necessario sostituire **`<cache-server-ip>` con l'effettivo indirizzo IP della macchina su cui è installato **apt-cacher-ng**.

### Per CentOS/RHEL

1. Per CentOS/RHEL, puoi usare [**`yum-cron`**](https://linux.die.net/man/8/yum-cron) per impostare una cache locale. Installalo eseguendo il comando **`sudo yum install yum-cron`

2. Modifica il **`/etc/yum/yum-cron.conf` archiviare e configurare il **`download_only` parametro a **`yes` Ciò garantisce che i pacchetti vengano solo scaricati e non installati automaticamente.

```shell
sudo nano /etc/yum/yum-cron.conf
```

3. Avviare il file [**`yum-cron`**](https://linux.die.net/man/8/yum-cron) servizio utilizzando il comando **`sudo systemctl start yum-cron`

```shell
sudo systemctl start yum-cron
```

4. Sui sistemi offline, creare una directory locale per archiviare i pacchetti scaricati, ad esempio **`/var/cache/yum`

```shell
sudo mkdir /var/cache/yum
```

5. Copiare i pacchetti scaricati dal sistema online nella directory della cache locale.

```shell
sudo cp -R /var/cache/yum /path/to/local/cache
```

Sostituire `/path/to/local/cache` con il percorso della directory della cache locale sul sistema offline.

6. Sui sistemi offline, crea un nuovo **`.repo` archiviare in **`/etc/yum.repos.d/` directory, puntando alla directory della cache locale.

```bash
sudo nano /etc/yum.repos.d/local.repo
```
Aggiungi il seguente contenuto al file, sostituendo `<local-cache-path>` con il percorso della directory della cache locale:
```toml
[local]
name=Local Cache
baseurl=file:///path/to/local/cache
enabled=1
gpgcheck=0
```
Salva il file ed esci dall'editor.

7. Infine, puoi utilizzare **`yum update` comando sui sistemi offline per installare gli aggiornamenti dalla cache locale.

```shell
sudo yum update
```

Questo comando aggiornerà i pacchetti sui sistemi offline utilizzando i pacchetti dalla cache locale.

Si prega di notare che sarà necessario sostituire **`<local-cache-path>` con il percorso effettivo della directory della cache locale sul sistema offline.

______

## Conclusione

La gestione degli aggiornamenti di Linux in ambienti offline può essere impegnativa, ma con l'approccio giusto puoi assicurarti che i tuoi sistemi rimangano aggiornati e sicuri. In questo articolo, abbiamo discusso i modi migliori per gestire l'installazione degli aggiornamenti offline per Ubuntu/Debian e CentOS/RHEL. Abbiamo esplorato l'impostazione di un repository locale e l'impostazione di una cache locale, fornendo istruzioni dettagliate per le distribuzioni basate su Debian e Red Hat.

Seguendo questi metodi, puoi mantenere la sicurezza e la stabilità dei tuoi sistemi Linux, anche in ambienti offline. Ricorda di aggiornare periodicamente il repository locale o la cache per includere gli ultimi aggiornamenti.

______

## Riferimenti

- [apt-mirror Documentation](https://manpages.debian.org/jessie/apt-mirror/apt-mirror.1.en.html)
- [debmirror Documentation](https://wiki.debian.org/debmirror)
- [createrepo Documentation](https://linux.die.net/man/8/createrepo)
- [apt-cacher-ng Documentation](https://www.unix-ag.uni-kl.de/~bloch/acng/)
- [yum-cron Documentation](https://linux.die.net/man/8/yum-cron)
