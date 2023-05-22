---
title: "Ultimate Guide: Offline Linux Updates for Ubuntu Debian and CentOS RHEL"
date: 2023-05-30
toc: true
draft: false
description: "Discover the best methods for handling offline Linux updates on Ubuntu/Debian and CentOS/RHEL systems, using local repositories or caches."
tags: ["Linux updates", "Ubuntu", "Debian", "CentOS", "RHEL", "offline updates", "local repository", "cache", "server setup", "client setup", "apt-mirror", "debmirror", "createrepo", "apt-cacher-ng", "yum-cron", "Linux system updates", "offline package updates", "offline software updates", "local package repository", "local package cache", "offline Linux updates", "handling offline updates", "offline update methods", "offline system maintenance", "Linux server updates", "Linux client updates", "offline software management", "offline package management", "update strategies", "Linux security updates"]
cover: "/img/cover/A_cartoon_illustration_depicting_a_server_and_multiple_clients.png"
coverAlt: "A cartoon illustration depicting a server and multiple client devices exchanging updates offline."
coverCaption: ""
---

**Best Ways to Handle Installing Linux Updates Offline for Ubuntu/Debian and CentOS/RHEL**

Linux updates are essential for maintaining the security and stability of your system. However, in some scenarios, you may have to deal with offline environments where internet connectivity is limited or non-existent. In such cases, it becomes crucial to have a proper strategy in place for installing updates offline. This article will guide you through the **best ways to handle installing Linux updates for Ubuntu/Debian and CentOS/RHEL** in offline environments, specifically focusing on using a local repository or cache.

## Setting Up a Local Repository

One of the most effective ways to handle offline updates is by setting up a local repository. A local repository contains all the necessary software packages and updates, allowing you to update your system without an internet connection. Here's how you can set up a local repository for both Debian-based and Red Hat-based distributions:

### For Debian/Ubuntu

1. Start by setting up a **Debian repository mirror** on a server that has internet access. You can use tools like [`apt-mirror`](https://manpages.debian.org/jessie/apt-mirror/apt-mirror.1.en.html) or [`debmirror`](https://wiki.debian.org/debmirror) to create a local mirror of the official Debian or Ubuntu repositories.

#### Setting up a Debian Repository Mirror with apt-mirror:

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

#### Setting up a Debian Repository Mirror with debmirror:
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
#### Debian Client Instructions

2. Configure your local repository by editing the **`/etc/apt/sources.list`** file on the offline system. Replace the default repository URLs with the local repository URL. For example, if your local repository is hosted at `http://local-repo/ubuntu`, update the `sources.list` file accordingly.

Example `/etc/apt/sources.list` file:
```
deb http://local-repo/ubuntu focal main restricted universe multiverse
```

3. Once the configuration is updated, you can run the **`apt update`** command on the offline system to fetch the package lists from the local repository.

```shell
sudo apt update
```

4. Finally, you can use the **`apt upgrade`** command to install the available updates from the local repository.

```shell
sudo apt upgrade
```

### For CentOS/RHEL

1. To set up a local repository for CentOS/RHEL, you need to use the [**`createrepo`**](https://linux.die.net/man/8/createrepo) tool. This tool creates the necessary metadata for a local repository.

2. Create a directory to store the repository files on a server with internet access. For example, you can create a directory called **`local-repo`**.

3. Copy all the relevant RPM package files and updates to the **`local-repo`** directory.

#### Setting up a Local Repository with createrepo:

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
4. Once the repository metadata is generated, you can transfer the entire `local-repo` directory to the offline system using a USB drive or any other means.

5. On the offline system, create a new `.repo` file in the `/etc/yum.repos.d/` directory. Provide the necessary configuration details, such as the `baseurl` pointing to the local repository directory.

For example, create a file called `local.repo` in the `/etc/yum.repos.d/` directory and add the following content:
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
6. Save the file and exit the editor.

7. After configuring the repository, you can use the yum update command to install updates from the local repository.

```shell
sudo yum update
```

This command will update the packages on the system using the packages from the local repository.

Remember to update the local repository by running the `createrepo` command whenever new packages are added or removed from the repository.

Please note that you will need to replace `/path/to/local-repo` with the actual path to the directory where you have stored the repository files.

## Setting Up a Local Cache

Another approach to handle offline updates is by setting up a local cache. A local cache stores the downloaded packages and updates, allowing you to distribute them across multiple systems without the need for individual downloads. You would set this cache up on an online system, then move the directory to a system that is offline to allow other systems to access the packages. Here's how you can set up a local cache for both Debian-based and Red Hat-based distributions:

### For Debian/Ubuntu

1. Install and configure [**`apt-cacher-ng`**](https://www.unix-ag.uni-kl.de/~bloch/acng/), a caching proxy for Debian/Ubuntu packages. You can install it by running the command **`sudo apt-get install apt-cacher-ng`**.

2. Once installed, edit the **`/etc/apt-cacher-ng/acng.conf`** file to configure the caching behavior. Ensure that the **`PassThroughPattern`** parameter includes the necessary repository URLs.

```shell
sudo nano /etc/apt-cacher-ng/acng.conf
```
Uncomment or add the necessary repository URLs to the PassThroughPattern parameter. For example, to include the Ubuntu repositories, add or uncomment the following line:
```yml
PassThroughPattern: (security|archive).ubuntu.com/ubuntu
```
Save the file and exit the editor.

3. Start the [**`apt-cacher-ng`**](https://www.unix-ag.uni-kl.de/~bloch/acng/) service using the command **`sudo systemctl start apt-cacher-ng`**.

```shell
sudo systemctl start apt-cacher-ng
```

4. On the offline systems, configure the **`/etc/apt/apt.conf.d/02proxy`** file to point to the local cache. Use the following line: **`Acquire::http::Proxy "http://<cache-server-ip>:3142";`**.

```shell
sudo nano /etc/apt/apt.conf.d/02proxy
```
Add the following line to the file, replacing <cache-server-ip> with the IP address of the cache server:
```text
Acquire::http::Proxy "http://<cache-server-ip>:3142";
```
Save the file and exit the editor

5. Now, when you run the **`apt update`** and **`apt upgrade`** commands on the offline systems, they will retrieve the packages from the local cache.

```shell
sudo apt update
sudo apt upgrade
```
These commands will fetch and install the updates from the local cache, reducing the need for internet access on the offline systems.

Please note that you will need to replace **`<cache-server-ip>`** with the actual IP address of the machine where **apt-cacher-ng** is installed.

### For CentOS/RHEL

1. For CentOS/RHEL, you can use [**`yum-cron`**](https://linux.die.net/man/8/yum-cron) to set up a local cache. Install it by running the command **`sudo yum install yum-cron`**.

2. Edit the **`/etc/yum/yum-cron.conf`** file and configure the **`download_only`** parameter to **`yes`**. This ensures that the packages are only downloaded and not installed automatically.

```shell
sudo nano /etc/yum/yum-cron.conf
```

3. Start the [**`yum-cron`**](https://linux.die.net/man/8/yum-cron) service using the command **`sudo systemctl start yum-cron`**.

```shell
sudo systemctl start yum-cron
```

4. On the offline systems, create a local directory to store the downloaded packages, for example, **`/var/cache/yum`**.

```shell
sudo mkdir /var/cache/yum
```

5. Copy the downloaded packages from the online system to the local cache directory.

```shell
sudo cp -R /var/cache/yum /path/to/local/cache
```

Replace `/path/to/local/cache` with the path to the local cache directory on the offline system.

6. On the offline systems, create a new **`.repo`** file in the **`/etc/yum.repos.d/`** directory, pointing to the local cache directory.

```bash
sudo nano /etc/yum.repos.d/local.repo
```
Add the following content to the file, replacing `<local-cache-path>` with the path to the local cache directory:
```toml
[local]
name=Local Cache
baseurl=file:///path/to/local/cache
enabled=1
gpgcheck=0
```
Save the file and exit the editor.

7. Finally, you can use the **`yum update`** command on the offline systems to install updates from the local cache.

```shell
sudo yum update
```

This command will update the packages on the offline systems using the packages from the local cache.

Please note that you will need to replace **`<local-cache-path>`** with the actual path to the local cache directory on the offline system.

______

## Conclusion

Handling Linux updates in offline environments can be challenging, but with the right approach, you can ensure your systems remain up to date and secure. In this article, we discussed the best ways to handle installing updates offline for Ubuntu/Debian and CentOS/RHEL. We explored setting up a local repository and setting up a local cache, providing step-by-step instructions for both Debian-based and Red Hat-based distributions.

By following these methods, you can maintain the security and stability of your Linux systems, even in offline environments. Remember to periodically update your local repository or cache to include the latest updates.

______

## References

- [apt-mirror Documentation](https://manpages.debian.org/jessie/apt-mirror/apt-mirror.1.en.html)
- [debmirror Documentation](https://wiki.debian.org/debmirror)
- [createrepo Documentation](https://linux.die.net/man/8/createrepo)
- [apt-cacher-ng Documentation](https://www.unix-ag.uni-kl.de/~bloch/acng/)
- [yum-cron Documentation](https://linux.die.net/man/8/yum-cron)
