---
title: "Guía definitiva: actualizaciones de Linux sin conexión para Ubuntu Debian y CentOS RHEL"
date: 2023-05-30
toc: true
draft: false
description: "Discover the best methods for handling offline Linux updates on Ubuntu/Debian and CentOS/RHEL systems, using local repositories or caches."
tags: ["actualizaciones de linux", "ubuntu", "Debian", "CentOS", "RHEL", "actualizaciones sin conexión", "repositorio local", "cache", "configuración del servidor", "configuración del cliente", "apt-espejo", "debmirror", "crearrepo", "apt-cacher-ng", "yum-cron", "Actualizaciones del sistema Linux", "actualizaciones de paquetes sin conexión", "actualizaciones de software sin conexión", "repositorio de paquetes locales", "caché de paquetes locales", "actualizaciones de Linux sin conexión", "manejo de actualizaciones fuera de línea", "métodos de actualización fuera de línea", "mantenimiento del sistema fuera de línea", "actualizaciones del servidor linux", "Actualizaciones de clientes de Linux", "gestión de software fuera de línea", "gestión de paquetes fuera de línea", "actualizar estrategias", "Actualizaciones de seguridad de Linux"]
cover: "/img/cover/A_cartoon_illustration_depicting_a_server_and_multiple_clients.png"
coverAlt: "Una ilustración de dibujos animados que muestra un servidor y varios dispositivos cliente que intercambian actualizaciones sin conexión."
coverCaption: ""
---

**Las mejores formas de manejar la instalación de actualizaciones de Linux sin conexión para Ubuntu/Debian y CentOS/RHEL**

Las actualizaciones de Linux son esenciales para mantener la seguridad y la estabilidad de su sistema. Sin embargo, en algunos escenarios, es posible que deba lidiar con entornos fuera de línea donde la conectividad a Internet es limitada o inexistente. En tales casos, se vuelve crucial contar con una estrategia adecuada para instalar actualizaciones sin conexión. Este artículo lo guiará a través de las **mejores formas de manejar la instalación de actualizaciones de Linux para Ubuntu/Debian y CentOS/RHEL** en entornos fuera de línea, centrándose específicamente en el uso de un repositorio o caché local.

## Configuración de un repositorio local

Una de las formas más efectivas de manejar las actualizaciones fuera de línea es configurar un repositorio local. Un repositorio local contiene todos los paquetes de software y actualizaciones necesarios, lo que le permite actualizar su sistema sin conexión a Internet. Así es como puede configurar un repositorio local para distribuciones basadas en Debian y Red Hat:

### Para Debian/Ubuntu

1. Comience configurando un **espejo del repositorio de Debian** en un servidor que tenga acceso a Internet. Puedes usar herramientas como [`apt-mirror`](https://manpages.debian.org/jessie/apt-mirror/apt-mirror.1.en.html) or [`debmirror`](https://wiki.debian.org/debmirror) para crear un espejo local de los repositorios oficiales de Debian o Ubuntu.

#### Configuración de un repositorio de Debian Mirror con apt-mirror:

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

#### Configurar un Debian Repository Mirror con debmirror:
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
#### Instrucciones del cliente Debian

2. Configure su repositorio local editando **`/etc/apt/sources.list` archivo en el sistema fuera de línea. Reemplace las URL del repositorio predeterminado con la URL del repositorio local. Por ejemplo, si su repositorio local está alojado en `http://local-repo/ubuntu` actualizar el `sources.list` archivo en consecuencia.

Ejemplo `/etc/apt/sources.list` archivo:
```
deb http://local-repo/ubuntu focal main restricted universe multiverse
```

3. Una vez actualizada la configuración, puede ejecutar **`apt update` Comando en el sistema fuera de línea para obtener las listas de paquetes del repositorio local.

```shell
sudo apt update
```

4. Finalmente, puedes usar el **`apt upgrade` comando para instalar las actualizaciones disponibles desde el repositorio local.

```shell
sudo apt upgrade
```

### Para CentOS/RHEL

1. Para configurar un repositorio local para CentOS/RHEL, debe usar el [**`createrepo`**](https://linux.die.net/man/8/createrepo) herramienta. Esta herramienta crea los metadatos necesarios para un repositorio local.

2. Cree un directorio para almacenar los archivos del repositorio en un servidor con acceso a Internet. Por ejemplo, puede crear un directorio llamado **`local-repo`

3. Copie todos los archivos y actualizaciones relevantes del paquete RPM en **`local-repo` directorio.

#### Configuración de un repositorio local con createrepo:

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
4. Una vez que se generan los metadatos del repositorio, puede transferir la totalidad `local-repo` directorio al sistema fuera de línea utilizando una unidad USB o cualquier otro medio.

5. En el sistema fuera de línea, cree un nuevo `.repo` archivo en el `/etc/yum.repos.d/` directorio. Proporcione los detalles de configuración necesarios, como el `baseurl` apuntando al directorio del repositorio local.

Por ejemplo, cree un archivo llamado `local.repo` en el `/etc/yum.repos.d/` directorio y agregue el siguiente contenido:
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
6. Guarde el archivo y salga del editor.

7. Después de configurar el repositorio, puede usar el comando yum update para instalar actualizaciones desde el repositorio local.

```shell
sudo yum update
```

Este comando actualizará los paquetes en el sistema utilizando los paquetes del repositorio local.

Recuerde actualizar el repositorio local ejecutando el `createrepo` comando cada vez que se agregan o eliminan nuevos paquetes del repositorio.

Tenga en cuenta que tendrá que reemplazar `/path/to/local-repo` con la ruta real al directorio donde ha almacenado los archivos del repositorio.

## Configuración de un caché local

Otro enfoque para manejar las actualizaciones fuera de línea es configurar un caché local. Un caché local almacena los paquetes y actualizaciones descargados, lo que le permite distribuirlos en varios sistemas sin necesidad de descargas individuales. Configuraría este caché en un sistema en línea, luego movería el directorio a un sistema que está fuera de línea para permitir que otros sistemas accedan a los paquetes. Así es como puede configurar un caché local para distribuciones basadas en Debian y Red Hat:

### Para Debian/Ubuntu

1. Instalar y configurar [**`apt-cacher-ng`**](https://www.unix-ag.uni-kl.de/~bloch/acng/) un proxy de almacenamiento en caché para paquetes Debian/Ubuntu. Puede instalarlo ejecutando el comando **`sudo apt-get install apt-cacher-ng`

2. Una vez instalado, edite el **`/etc/apt-cacher-ng/acng.conf` archivo para configurar el comportamiento de almacenamiento en caché. Asegúrese de que **`PassThroughPattern` El parámetro incluye las URL de repositorio necesarias.

```shell
sudo nano /etc/apt-cacher-ng/acng.conf
```
Quite los comentarios o agregue las URL de repositorio necesarias al parámetro PassThroughPattern. Por ejemplo, para incluir los repositorios de Ubuntu, agregue o descomente la siguiente línea:
```yml
PassThroughPattern: (security|archive).ubuntu.com/ubuntu
```
Guarde el archivo y salga del editor.

3. Inicie el [**`apt-cacher-ng`**](https://www.unix-ag.uni-kl.de/~bloch/acng/) servicio usando el comando **`sudo systemctl start apt-cacher-ng`

```shell
sudo systemctl start apt-cacher-ng
```

4. En los sistemas fuera de línea, configure **`/etc/apt/apt.conf.d/02proxy` archivo para apuntar a la memoria caché local. Utilice la siguiente línea: **`Acquire::http::Proxy "http://<cache-server-ip>:3142";`

```shell
sudo nano /etc/apt/apt.conf.d/02proxy
```
Agregue la siguiente línea al archivo, reemplazando <cache-server-ip> con la dirección IP del servidor de caché:
```text
Acquire::http::Proxy "http://<cache-server-ip>:3142";
```
Guarde el archivo y salga del editor.

5. Ahora, cuando ejecutes **`apt update` y **`apt upgrade` comandos en los sistemas fuera de línea, recuperarán los paquetes del caché local.

```shell
sudo apt update
sudo apt upgrade
```
Estos comandos buscarán e instalarán las actualizaciones desde el caché local, lo que reducirá la necesidad de acceso a Internet en los sistemas fuera de línea.

Tenga en cuenta que deberá reemplazar **`<cache-server-ip>` con la dirección IP real de la máquina donde está instalado **apt-cacher-ng**.

### Para CentOS/RHEL

1. Para CentOS/RHEL, puede usar [**`yum-cron`**](https://linux.die.net/man/8/yum-cron) para configurar un caché local. Instálelo ejecutando el comando **`sudo yum install yum-cron`

2. Edite el **`/etc/yum/yum-cron.conf` archivo y configurar el **`download_only` parámetro a **`yes` Esto asegura que los paquetes solo se descarguen y no se instalen automáticamente.

```shell
sudo nano /etc/yum/yum-cron.conf
```

3. Inicie el [**`yum-cron`**](https://linux.die.net/man/8/yum-cron) servicio usando el comando **`sudo systemctl start yum-cron`

```shell
sudo systemctl start yum-cron
```

4. En los sistemas fuera de línea, cree un directorio local para almacenar los paquetes descargados, por ejemplo, **`/var/cache/yum`

```shell
sudo mkdir /var/cache/yum
```

5. Copie los paquetes descargados del sistema en línea al directorio de caché local.

```shell
sudo cp -R /var/cache/yum /path/to/local/cache
```

Reemplazar `/path/to/local/cache` con la ruta al directorio de caché local en el sistema fuera de línea.

6. En los sistemas fuera de línea, cree un nuevo **`.repo` archivo en el **`/etc/yum.repos.d/` directorio, apuntando al directorio de caché local.

```bash
sudo nano /etc/yum.repos.d/local.repo
```
Agregue el siguiente contenido al archivo, reemplazando `<local-cache-path>` con la ruta al directorio de caché local:
```toml
[local]
name=Local Cache
baseurl=file:///path/to/local/cache
enabled=1
gpgcheck=0
```
Guarde el archivo y salga del editor.

7. Finalmente, puedes usar el **`yum update` Comando en los sistemas fuera de línea para instalar actualizaciones desde el caché local.

```shell
sudo yum update
```

Este comando actualizará los paquetes en los sistemas fuera de línea usando los paquetes del caché local.

Tenga en cuenta que deberá reemplazar **`<local-cache-path>` con la ruta real al directorio de caché local en el sistema fuera de línea.

______

## Conclusión

Manejar las actualizaciones de Linux en entornos fuera de línea puede ser un desafío, pero con el enfoque correcto, puede asegurarse de que sus sistemas permanezcan actualizados y seguros. En este artículo, discutimos las mejores formas de manejar la instalación de actualizaciones sin conexión para Ubuntu/Debian y CentOS/RHEL. Exploramos la configuración de un repositorio local y la configuración de un caché local, brindando instrucciones paso a paso para las distribuciones basadas en Debian y Red Hat.

Siguiendo estos métodos, puede mantener la seguridad y la estabilidad de sus sistemas Linux, incluso en entornos fuera de línea. Recuerde actualizar periódicamente su repositorio o caché local para incluir las últimas actualizaciones.

______

## Referencias

- [apt-mirror Documentation](https://manpages.debian.org/jessie/apt-mirror/apt-mirror.1.en.html)
- [debmirror Documentation](https://wiki.debian.org/debmirror)
- [createrepo Documentation](https://linux.die.net/man/8/createrepo)
- [apt-cacher-ng Documentation](https://www.unix-ag.uni-kl.de/~bloch/acng/)
- [yum-cron Documentation](https://linux.die.net/man/8/yum-cron)
