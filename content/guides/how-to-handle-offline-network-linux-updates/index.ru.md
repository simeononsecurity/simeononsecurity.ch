---
title: "Полное руководство: автономные обновления Linux для Ubuntu Debian и CentOS RHEL"
date: 2023-05-30
toc: true
draft: false
description: "Discover the best methods for handling offline Linux updates on Ubuntu/Debian and CentOS/RHEL systems, using local repositories or caches."
tags: ["Обновления Linux", "Убунту", "Дебиан", "CentOS", "РЕЛ", "автономные обновления", "локальный репозиторий", "тайник", "настройка сервера", "настройка клиента", "подходящее зеркало", "debmirror", "создать репозиторий", "apt-cacher-нг", "ням-крон", "Обновления системы Linux", "автономные обновления пакетов", "автономные обновления программного обеспечения", "локальный репозиторий пакетов", "локальный кэш пакетов", "автономные обновления Linux", "обработка автономных обновлений", "автономные способы обновления", "автономное обслуживание системы", "Обновления сервера Linux", "Обновления клиента Linux", "автономное управление программным обеспечением", "автономное управление пакетами", "обновить стратегии", "Обновления безопасности Linux"]
cover: "/img/cover/A_cartoon_illustration_depicting_a_server_and_multiple_clients.png"
coverAlt: "Мультяшная иллюстрация, изображающая сервер и несколько клиентских устройств, обменивающихся обновлениями в автономном режиме."
coverCaption: ""
---

**Лучшие способы установки обновлений Linux в автономном режиме для Ubuntu/Debian и CentOS/RHEL**

Обновления Linux необходимы для поддержания безопасности и стабильности вашей системы. Однако в некоторых сценариях вам, возможно, придется иметь дело с автономными средами, где подключение к Интернету ограничено или отсутствует. В таких случаях крайне важно иметь правильную стратегию для установки обновлений в автономном режиме. Эта статья расскажет вам о **наилучших способах установки обновлений Linux для Ubuntu/Debian и CentOS/RHEL** в автономной среде, уделяя особое внимание использованию локального репозитория или кэша.

## Настройка локального репозитория

Одним из наиболее эффективных способов обработки автономных обновлений является создание локального репозитория. Локальный репозиторий содержит все необходимые программные пакеты и обновления, что позволяет обновлять вашу систему без подключения к Интернету. Вот как вы можете настроить локальный репозиторий как для дистрибутивов на основе Debian, так и для дистрибутивов на основе Red Hat:

### Для Debian/Ubuntu

1. Начните с настройки **зеркала репозитория Debian** на сервере с доступом в Интернет. Вы можете использовать такие инструменты, как [`apt-mirror`](https://manpages.debian.org/jessie/apt-mirror/apt-mirror.1.en.html) or [`debmirror`](https://wiki.debian.org/debmirror) для создания локального зеркала официальных репозиториев Debian или Ubuntu.

#### Настройка зеркала репозитория Debian с помощью apt-mirror:

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

#### Настройка зеркала репозитория Debian с помощью debmirror:
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
#### Инструкции клиента Debian

2. Настройте локальный репозиторий, отредактировав **`/etc/apt/sources.list` файл в автономной системе. Замените URL-адреса репозитория по умолчанию на URL-адрес локального репозитория. Например, если ваш локальный репозиторий размещен по адресу `http://local-repo/ubuntu` обновить `sources.list` файл соответственно.

Пример `/etc/apt/sources.list` файл:
```
deb http://local-repo/ubuntu focal main restricted universe multiverse
```

3. После обновления конфигурации вы можете запустить **`apt update` в автономной системе для получения списков пакетов из локального репозитория.

```shell
sudo apt update
```

4. Наконец, вы можете использовать **`apt upgrade` Команда для установки доступных обновлений из локального репозитория.

```shell
sudo apt upgrade
```

### Для CentOS/RHEL

1. Чтобы настроить локальный репозиторий для CentOS/RHEL, вам нужно использовать [**`createrepo`**](https://linux.die.net/man/8/createrepo) инструмент. Этот инструмент создает необходимые метаданные для локального репозитория.

2. Создайте каталог для хранения файлов репозитория на сервере с доступом в Интернет. Например, вы можете создать каталог с именем **`local-repo`

3. Скопируйте все соответствующие файлы пакета RPM и обновления в **`local-repo` каталог.

#### Настройка локального репозитория с помощью createrepo:

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
4. После того, как метаданные репозитория сгенерированы, вы можете перенести все `local-repo` каталог в автономную систему с помощью USB-накопителя или любым другим способом.

5. В автономной системе создайте новый `.repo` файл в `/etc/yum.repos.d/` каталог. Укажите необходимые сведения о конфигурации, такие как `baseurl` указывая на локальный каталог репозитория.

Например, создайте файл с именем `local.repo` в `/etc/yum.repos.d/` каталог и добавьте следующее содержимое:
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
6. Сохраните файл и выйдите из редактора.

7. После настройки репозитория вы можете использовать команду yum update для установки обновлений из локального репозитория.

```shell
sudo yum update
```

Эта команда обновит пакеты в системе, используя пакеты из локального репозитория.

Не забудьте обновить локальный репозиторий, запустив `createrepo` Команда всякий раз, когда новые пакеты добавляются или удаляются из репозитория.

Обратите внимание, что вам нужно будет заменить `/path/to/local-repo` с фактическим путем к каталогу, в котором вы сохранили файлы репозитория.

## Настройка локального кэша

Другой способ обработки автономных обновлений — настройка локального кэша. В локальном кеше хранятся загруженные пакеты и обновления, что позволяет распространять их по нескольким системам без необходимости загрузки отдельных файлов. Вы должны установить этот кэш в онлайн-системе, а затем переместить каталог в автономную систему, чтобы другие системы могли получить доступ к пакетам. Вот как вы можете настроить локальный кеш как для дистрибутивов на основе Debian, так и для дистрибутивов на основе Red Hat:

### Для Debian/Ubuntu

1. Установите и настройте [**`apt-cacher-ng`**](https://www.unix-ag.uni-kl.de/~bloch/acng/) кеширующий прокси для пакетов Debian/Ubuntu. Вы можете установить его, выполнив команду **`sudo apt-get install apt-cacher-ng`

2. После установки отредактируйте **`/etc/apt-cacher-ng/acng.conf` файл для настройки поведения кэширования. Убедитесь, что **`PassThroughPattern` Параметр включает необходимые URL-адреса репозитория.

```shell
sudo nano /etc/apt-cacher-ng/acng.conf
```
Раскомментируйте или добавьте необходимые URL-адреса репозитория в параметр PassThroughPattern. Например, чтобы включить репозитории Ubuntu, добавьте или раскомментируйте следующую строку:
```yml
PassThroughPattern: (security|archive).ubuntu.com/ubuntu
```
Сохраните файл и выйдите из редактора.

3. Запустите [**`apt-cacher-ng`**](https://www.unix-ag.uni-kl.de/~bloch/acng/) обслуживание с помощью команды **`sudo systemctl start apt-cacher-ng`

```shell
sudo systemctl start apt-cacher-ng
```

4. В автономных системах настройте **`/etc/apt/apt.conf.d/02proxy` файл, указывающий на локальный кеш. Используйте следующую строку: **`Acquire::http::Proxy "http://<cache-server-ip>:3142";`

```shell
sudo nano /etc/apt/apt.conf.d/02proxy
```
Добавьте в файл следующую строку, заменив <cache-server-ip> IP-адресом сервера кэширования:
```text
Acquire::http::Proxy "http://<cache-server-ip>:3142";
```
Сохраните файл и выйдите из редактора

5. Теперь при запуске **`apt update` и **`apt upgrade` команды в автономных системах, они извлекут пакеты из локального кеша.

```shell
sudo apt update
sudo apt upgrade
```
Эти команды будут извлекать и устанавливать обновления из локального кеша, уменьшая потребность в доступе в Интернет в автономных системах.

Обратите внимание, что вам нужно будет заменить **`<cache-server-ip>` с фактическим IP-адресом машины, на которой установлено **apt-cacher-ng**.

### Для CentOS/RHEL

1. Для CentOS/RHEL вы можете использовать [**`yum-cron`**](https://linux.die.net/man/8/yum-cron) настроить локальный кеш. Установите его, выполнив команду **`sudo yum install yum-cron`

2. Отредактируйте **`/etc/yum/yum-cron.conf` файл и настроить **`download_only` параметр до **`yes` Это гарантирует, что пакеты только загружаются, а не устанавливаются автоматически.

```shell
sudo nano /etc/yum/yum-cron.conf
```

3. Запустите [**`yum-cron`**](https://linux.die.net/man/8/yum-cron) обслуживание с помощью команды **`sudo systemctl start yum-cron`

```shell
sudo systemctl start yum-cron
```

4. В автономных системах создайте локальный каталог для хранения загруженных пакетов, например, **`/var/cache/yum`

```shell
sudo mkdir /var/cache/yum
```

5. Скопируйте загруженные пакеты из онлайн-системы в каталог локального кеша.

```shell
sudo cp -R /var/cache/yum /path/to/local/cache
```

Заменять `/path/to/local/cache` с путем к каталогу локального кэша в автономной системе.

6. В офлайн-системах создайте новый **`.repo` файл в **`/etc/yum.repos.d/` каталог, указывающий на локальный каталог кэша.

```bash
sudo nano /etc/yum.repos.d/local.repo
```
Добавьте в файл следующее содержимое, заменив `<local-cache-path>` с путем к каталогу локального кеша:
```toml
[local]
name=Local Cache
baseurl=file:///path/to/local/cache
enabled=1
gpgcheck=0
```
Сохраните файл и выйдите из редактора.

7. Наконец, вы можете использовать **`yum update` в автономных системах для установки обновлений из локального кеша.

```shell
sudo yum update
```

Эта команда обновит пакеты в автономных системах, используя пакеты из локального кеша.

Обратите внимание, что вам нужно будет заменить **`<local-cache-path>` с фактическим путем к каталогу локального кэша в автономной системе.

______

## Заключение

Обработка обновлений Linux в автономной среде может быть сложной задачей, но при правильном подходе вы можете обеспечить актуальность и безопасность своих систем. В этой статье мы обсудили лучшие способы установки обновлений в автономном режиме для Ubuntu/Debian и CentOS/RHEL. Мы рассмотрели настройку локального репозитория и локального кэша, предоставив пошаговые инструкции как для дистрибутивов на основе Debian, так и для дистрибутивов на основе Red Hat.

Следуя этим методам, вы сможете поддерживать безопасность и стабильность своих систем Linux даже в автономной среде. Не забывайте периодически обновлять локальный репозиторий или кеш, чтобы включать последние обновления.

______

## Использованная литература

- [apt-mirror Documentation](https://manpages.debian.org/jessie/apt-mirror/apt-mirror.1.en.html)
- [debmirror Documentation](https://wiki.debian.org/debmirror)
- [createrepo Documentation](https://linux.die.net/man/8/createrepo)
- [apt-cacher-ng Documentation](https://www.unix-ag.uni-kl.de/~bloch/acng/)
- [yum-cron Documentation](https://linux.die.net/man/8/yum-cron)
