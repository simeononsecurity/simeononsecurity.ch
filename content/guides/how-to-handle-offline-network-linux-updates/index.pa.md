---
title: "ਅੰਤਮ ਗਾਈਡ: ਉਬੰਟੂ ਡੇਬੀਅਨ ਅਤੇ CentOS RHEL ਲਈ ਔਫਲਾਈਨ ਲੀਨਕਸ ਅਪਡੇਟਸ"
date: 2023-05-30
toc: true
draft: false
description: "Discover the best methods for handling offline Linux updates on Ubuntu/Debian and CentOS/RHEL systems, using local repositories or caches."
tags: ["ਲੀਨਕਸ ਅੱਪਡੇਟ", "ਉਬੰਟੂ", "ਡੇਬੀਅਨ", "CentOS", "RHEL", "ਔਫਲਾਈਨ ਅੱਪਡੇਟ", "ਸਥਾਨਕ ਭੰਡਾਰ", "ਕੈਸ਼", "ਸਰਵਰ ਸੈੱਟਅੱਪ", "ਗਾਹਕ ਸੈੱਟਅੱਪ", "apt-ਸ਼ੀਸ਼ਾ", "debmirror", "createrepo", "apt-cacher-ng", "yum-cron", "ਲੀਨਕਸ ਸਿਸਟਮ ਅੱਪਡੇਟ", "ਔਫਲਾਈਨ ਪੈਕੇਜ ਅੱਪਡੇਟ", "ਔਫਲਾਈਨ ਸਾਫਟਵੇਅਰ ਅੱਪਡੇਟ", "ਸਥਾਨਕ ਪੈਕੇਜ ਰਿਪੋਜ਼ਟਰੀ", "ਸਥਾਨਕ ਪੈਕੇਜ ਕੈਸ਼", "ਔਫਲਾਈਨ ਲੀਨਕਸ ਅੱਪਡੇਟ", "ਔਫਲਾਈਨ ਅੱਪਡੇਟਾਂ ਨੂੰ ਸੰਭਾਲਣਾ", "ਔਫਲਾਈਨ ਅੱਪਡੇਟ ਢੰਗ", "ਔਫਲਾਈਨ ਸਿਸਟਮ ਰੱਖ-ਰਖਾਅ", "ਲੀਨਕਸ ਸਰਵਰ ਅੱਪਡੇਟ", "ਲੀਨਕਸ ਕਲਾਇੰਟ ਅੱਪਡੇਟ", "ਔਫਲਾਈਨ ਸਾਫਟਵੇਅਰ ਪ੍ਰਬੰਧਨ", "ਔਫਲਾਈਨ ਪੈਕੇਜ ਪ੍ਰਬੰਧਨ", "ਅੱਪਡੇਟ ਰਣਨੀਤੀ", "ਲੀਨਕਸ ਸੁਰੱਖਿਆ ਅੱਪਡੇਟ"]
cover: "/img/cover/A_cartoon_illustration_depicting_a_server_and_multiple_clients.png"
coverAlt: "ਇੱਕ ਸਰਵਰ ਅਤੇ ਇੱਕ ਤੋਂ ਵੱਧ ਕਲਾਇੰਟ ਡਿਵਾਈਸਾਂ ਨੂੰ ਔਫਲਾਈਨ ਅਪਡੇਟਾਂ ਦਾ ਆਦਾਨ-ਪ੍ਰਦਾਨ ਕਰਨ ਵਾਲਾ ਇੱਕ ਕਾਰਟੂਨ ਚਿੱਤਰ।"
coverCaption: ""
---

**ਉਬੰਟੂ/ਡੇਬੀਅਨ ਅਤੇ CentOS/RHEL ਲਈ ਔਫਲਾਈਨ ਲੀਨਕਸ ਅੱਪਡੇਟਾਂ ਨੂੰ ਸਥਾਪਿਤ ਕਰਨ ਦੇ ਵਧੀਆ ਤਰੀਕੇ**

ਤੁਹਾਡੇ ਸਿਸਟਮ ਦੀ ਸੁਰੱਖਿਆ ਅਤੇ ਸਥਿਰਤਾ ਨੂੰ ਬਣਾਈ ਰੱਖਣ ਲਈ ਲੀਨਕਸ ਅੱਪਡੇਟ ਜ਼ਰੂਰੀ ਹਨ। ਹਾਲਾਂਕਿ, ਕੁਝ ਸਥਿਤੀਆਂ ਵਿੱਚ, ਤੁਹਾਨੂੰ ਔਫਲਾਈਨ ਵਾਤਾਵਰਨ ਨਾਲ ਨਜਿੱਠਣਾ ਪੈ ਸਕਦਾ ਹੈ ਜਿੱਥੇ ਇੰਟਰਨੈਟ ਕਨੈਕਟੀਵਿਟੀ ਸੀਮਤ ਜਾਂ ਗੈਰ-ਮੌਜੂਦ ਹੈ। ਅਜਿਹੇ ਮਾਮਲਿਆਂ ਵਿੱਚ, ਅੱਪਡੇਟ ਔਫਲਾਈਨ ਸਥਾਪਤ ਕਰਨ ਲਈ ਇੱਕ ਸਹੀ ਰਣਨੀਤੀ ਬਣਾਉਣਾ ਮਹੱਤਵਪੂਰਨ ਹੋ ਜਾਂਦਾ ਹੈ। ਇਹ ਲੇਖ ਤੁਹਾਨੂੰ ਔਫਲਾਈਨ ਵਾਤਾਵਰਨ ਵਿੱਚ **ਉਬੰਟੂ/ਡੇਬੀਅਨ ਅਤੇ CentOS/RHEL** ਲਈ ਲੀਨਕਸ ਅੱਪਡੇਟ ਸਥਾਪਤ ਕਰਨ ਦੇ ਸਭ ਤੋਂ ਵਧੀਆ ਤਰੀਕਿਆਂ ਬਾਰੇ ਮਾਰਗਦਰਸ਼ਨ ਕਰੇਗਾ, ਖਾਸ ਤੌਰ 'ਤੇ ਸਥਾਨਕ ਰਿਪੋਜ਼ਟਰੀ ਜਾਂ ਕੈਸ਼ ਦੀ ਵਰਤੋਂ ਕਰਨ 'ਤੇ ਧਿਆਨ ਕੇਂਦਰਤ ਕਰਦਾ ਹੈ।

## ਇੱਕ ਸਥਾਨਕ ਰਿਪੋਜ਼ਟਰੀ ਸੈੱਟਅੱਪ ਕਰਨਾ

ਔਫਲਾਈਨ ਅੱਪਡੇਟਾਂ ਨੂੰ ਸੰਭਾਲਣ ਦੇ ਸਭ ਤੋਂ ਪ੍ਰਭਾਵਸ਼ਾਲੀ ਤਰੀਕਿਆਂ ਵਿੱਚੋਂ ਇੱਕ ਸਥਾਨਕ ਰਿਪੋਜ਼ਟਰੀ ਸਥਾਪਤ ਕਰਨਾ ਹੈ। ਇੱਕ ਸਥਾਨਕ ਰਿਪੋਜ਼ਟਰੀ ਵਿੱਚ ਸਾਰੇ ਲੋੜੀਂਦੇ ਸਾਫਟਵੇਅਰ ਪੈਕੇਜ ਅਤੇ ਅੱਪਡੇਟ ਹੁੰਦੇ ਹਨ, ਜਿਸ ਨਾਲ ਤੁਸੀਂ ਬਿਨਾਂ ਇੰਟਰਨੈਟ ਕਨੈਕਸ਼ਨ ਦੇ ਆਪਣੇ ਸਿਸਟਮ ਨੂੰ ਅੱਪਡੇਟ ਕਰ ਸਕਦੇ ਹੋ। ਇੱਥੇ ਇਹ ਹੈ ਕਿ ਤੁਸੀਂ ਡੇਬੀਅਨ-ਅਧਾਰਿਤ ਅਤੇ Red Hat-ਅਧਾਰਿਤ ਡਿਸਟਰੀਬਿਊਸ਼ਨਾਂ ਲਈ ਇੱਕ ਸਥਾਨਕ ਰਿਪੋਜ਼ਟਰੀ ਕਿਵੇਂ ਸੈਟ ਕਰ ਸਕਦੇ ਹੋ:

### ਡੇਬੀਅਨ/ਉਬੰਟੂ ਲਈ

1. ਇੰਟਰਨੈੱਟ ਪਹੁੰਚ ਵਾਲੇ ਸਰਵਰ 'ਤੇ **ਡੇਬੀਅਨ ਰਿਪੋਜ਼ਟਰੀ ਮਿਰਰ** ਸਥਾਪਤ ਕਰਕੇ ਸ਼ੁਰੂਆਤ ਕਰੋ। ਵਰਗੇ ਸਾਧਨਾਂ ਦੀ ਵਰਤੋਂ ਕਰ ਸਕਦੇ ਹੋ [`apt-mirror`](https://manpages.debian.org/jessie/apt-mirror/apt-mirror.1.en.html) or [`debmirror`](https://wiki.debian.org/debmirror) ਅਧਿਕਾਰਤ ਡੇਬੀਅਨ ਜਾਂ ਉਬੰਟੂ ਰਿਪੋਜ਼ਟਰੀਆਂ ਦਾ ਇੱਕ ਸਥਾਨਕ ਸ਼ੀਸ਼ਾ ਬਣਾਉਣ ਲਈ।

#### apt-mirrਰ ਨਾਲ ਡੇਬੀਅਨ ਰਿਪੋਜ਼ਟਰੀ ਮਿਰਰ ਸੈਟ ਅਪ ਕਰਨਾ:

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

#### ਡੇਬਮਿਰਰ ਨਾਲ ਡੇਬੀਅਨ ਰਿਪੋਜ਼ਟਰੀ ਮਿਰਰ ਸੈਟ ਅਪ ਕਰਨਾ:
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
#### ਡੇਬੀਅਨ ਕਲਾਇੰਟ ਹਦਾਇਤਾਂ

2. ** ਨੂੰ ਸੰਪਾਦਿਤ ਕਰਕੇ ਆਪਣੀ ਸਥਾਨਕ ਰਿਪੋਜ਼ਟਰੀ ਨੂੰ ਕੌਂਫਿਗਰ ਕਰੋ`/etc/apt/sources.list` ਔਫਲਾਈਨ ਸਿਸਟਮ ਤੇ ਫਾਈਲ. ਮੂਲ ਰਿਪੋਜ਼ਟਰੀ URL ਨੂੰ ਸਥਾਨਕ ਰਿਪੋਜ਼ਟਰੀ URL ਨਾਲ ਬਦਲੋ। ਉਦਾਹਰਨ ਲਈ, ਜੇਕਰ ਤੁਹਾਡੀ ਸਥਾਨਕ ਰਿਪੋਜ਼ਟਰੀ 'ਤੇ ਹੋਸਟ ਕੀਤੀ ਗਈ ਹੈ `http://local-repo/ubuntu` ਨੂੰ ਅਪਡੇਟ ਕਰੋ `sources.list` ਅਨੁਸਾਰ ਫਾਈਲ.

ਉਦਾਹਰਨ `/etc/apt/sources.list` ਫਾਈਲ:
```
deb http://local-repo/ubuntu focal main restricted universe multiverse
```

3. ਇੱਕ ਵਾਰ ਸੰਰਚਨਾ ਅੱਪਡੇਟ ਹੋਣ ਤੋਂ ਬਾਅਦ, ਤੁਸੀਂ ** ਚਲਾ ਸਕਦੇ ਹੋ`apt update` ਸਥਾਨਕ ਰਿਪੋਜ਼ਟਰੀ ਤੋਂ ਪੈਕੇਜ ਸੂਚੀਆਂ ਪ੍ਰਾਪਤ ਕਰਨ ਲਈ ਔਫਲਾਈਨ ਸਿਸਟਮ ਉੱਤੇ ਕਮਾਂਡ ਦਿਓ।

```shell
sudo apt update
```

4. ਅੰਤ ਵਿੱਚ, ਤੁਸੀਂ ** ਦੀ ਵਰਤੋਂ ਕਰ ਸਕਦੇ ਹੋ`apt upgrade` ਸਥਾਨਕ ਰਿਪੋਜ਼ਟਰੀ ਤੋਂ ਉਪਲੱਬਧ ਅੱਪਡੇਟਾਂ ਨੂੰ ਇੰਸਟਾਲ ਕਰਨ ਲਈ ਕਮਾਂਡ।

```shell
sudo apt upgrade
```

### CentOS/RHEL ਲਈ

1. CentOS/RHEL ਲਈ ਇੱਕ ਸਥਾਨਕ ਰਿਪੋਜ਼ਟਰੀ ਸਥਾਪਤ ਕਰਨ ਲਈ, ਤੁਹਾਨੂੰ ਵਰਤਣ ਦੀ ਲੋੜ ਹੈ [**`createrepo`**](https://linux.die.net/man/8/createrepo) ਸੰਦ. ਇਹ ਟੂਲ ਇੱਕ ਸਥਾਨਕ ਰਿਪੋਜ਼ਟਰੀ ਲਈ ਲੋੜੀਂਦਾ ਮੈਟਾਡੇਟਾ ਬਣਾਉਂਦਾ ਹੈ।

2. ਇੰਟਰਨੈੱਟ ਪਹੁੰਚ ਵਾਲੇ ਸਰਵਰ 'ਤੇ ਰਿਪੋਜ਼ਟਰੀ ਫਾਈਲਾਂ ਨੂੰ ਸਟੋਰ ਕਰਨ ਲਈ ਇੱਕ ਡਾਇਰੈਕਟਰੀ ਬਣਾਓ। ਉਦਾਹਰਨ ਲਈ, ਤੁਸੀਂ ** ਨਾਮ ਦੀ ਇੱਕ ਡਾਇਰੈਕਟਰੀ ਬਣਾ ਸਕਦੇ ਹੋ`local-repo`

3. ਸਾਰੀਆਂ ਸੰਬੰਧਿਤ RPM ਪੈਕੇਜ ਫਾਈਲਾਂ ਅਤੇ ਅੱਪਡੇਟ ਨੂੰ ** ਵਿੱਚ ਕਾਪੀ ਕਰੋ`local-repo` ਡਾਇਰੈਕਟਰੀ.

#### createrepo ਨਾਲ ਇੱਕ ਸਥਾਨਕ ਰਿਪੋਜ਼ਟਰੀ ਸੈਟ ਅਪ ਕਰਨਾ:

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
4. ਇੱਕ ਵਾਰ ਰਿਪੋਜ਼ਟਰੀ ਮੈਟਾਡੇਟਾ ਤਿਆਰ ਹੋਣ ਤੋਂ ਬਾਅਦ, ਤੁਸੀਂ ਪੂਰਾ ਟ੍ਰਾਂਸਫਰ ਕਰ ਸਕਦੇ ਹੋ `local-repo` ਇੱਕ USB ਡਰਾਈਵ ਜਾਂ ਕਿਸੇ ਹੋਰ ਸਾਧਨ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਔਫਲਾਈਨ ਸਿਸਟਮ ਲਈ ਡਾਇਰੈਕਟਰੀ।

5. ਔਫਲਾਈਨ ਸਿਸਟਮ 'ਤੇ, ਇੱਕ ਨਵਾਂ ਬਣਾਓ `.repo` ਵਿੱਚ ਫਾਈਲ `/etc/yum.repos.d/` ਡਾਇਰੈਕਟਰੀ. ਲੋੜੀਂਦੇ ਸੰਰਚਨਾ ਵੇਰਵੇ ਪ੍ਰਦਾਨ ਕਰੋ, ਜਿਵੇਂ ਕਿ `baseurl` ਸਥਾਨਕ ਰਿਪੋਜ਼ਟਰੀ ਡਾਇਰੈਕਟਰੀ ਵੱਲ ਇਸ਼ਾਰਾ ਕਰ ਰਿਹਾ ਹੈ।

ਉਦਾਹਰਨ ਲਈ, ਨਾਮ ਦੀ ਇੱਕ ਫਾਇਲ ਬਣਾਓ `local.repo` ਵਿੱਚ `/etc/yum.repos.d/` ਡਾਇਰੈਕਟਰੀ ਅਤੇ ਹੇਠ ਦਿੱਤੀ ਸਮੱਗਰੀ ਸ਼ਾਮਲ ਕਰੋ:
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
6. ਫਾਈਲ ਸੇਵ ਕਰੋ ਅਤੇ ਐਡੀਟਰ ਤੋਂ ਬਾਹਰ ਜਾਓ।

7. ਰਿਪੋਜ਼ਟਰੀ ਦੀ ਸੰਰਚਨਾ ਕਰਨ ਤੋਂ ਬਾਅਦ, ਤੁਸੀਂ ਸਥਾਨਕ ਰਿਪੋਜ਼ਟਰੀ ਤੋਂ ਅੱਪਡੇਟ ਇੰਸਟਾਲ ਕਰਨ ਲਈ yum ਅੱਪਡੇਟ ਕਮਾਂਡ ਦੀ ਵਰਤੋਂ ਕਰ ਸਕਦੇ ਹੋ।

```shell
sudo yum update
```

ਇਹ ਕਮਾਂਡ ਸਥਾਨਕ ਰਿਪੋਜ਼ਟਰੀ ਤੋਂ ਪੈਕੇਜਾਂ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਸਿਸਟਮ ਉੱਤੇ ਪੈਕੇਜਾਂ ਨੂੰ ਅੱਪਡੇਟ ਕਰੇਗੀ।

ਨੂੰ ਚਲਾ ਕੇ ਸਥਾਨਕ ਰਿਪੋਜ਼ਟਰੀ ਨੂੰ ਅੱਪਡੇਟ ਕਰਨਾ ਯਾਦ ਰੱਖੋ `createrepo` ਕਮਾਂਡ ਜਦੋਂ ਵੀ ਰਿਪੋਜ਼ਟਰੀ ਵਿੱਚੋਂ ਨਵੇਂ ਪੈਕੇਜ ਸ਼ਾਮਲ ਜਾਂ ਹਟਾਏ ਜਾਂਦੇ ਹਨ।

ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਦਿਓ ਕਿ ਤੁਹਾਨੂੰ ਬਦਲਣ ਦੀ ਲੋੜ ਪਵੇਗੀ `/path/to/local-repo` ਡਾਇਰੈਕਟਰੀ ਦੇ ਅਸਲ ਮਾਰਗ ਨਾਲ ਜਿੱਥੇ ਤੁਸੀਂ ਰਿਪੋਜ਼ਟਰੀ ਫਾਈਲਾਂ ਨੂੰ ਸਟੋਰ ਕੀਤਾ ਹੈ।

## ਇੱਕ ਸਥਾਨਕ ਕੈਸ਼ ਸੈੱਟਅੱਪ ਕਰਨਾ

ਔਫਲਾਈਨ ਅੱਪਡੇਟਾਂ ਨੂੰ ਸੰਭਾਲਣ ਲਈ ਇੱਕ ਹੋਰ ਪਹੁੰਚ ਇੱਕ ਸਥਾਨਕ ਕੈਸ਼ ਸਥਾਪਤ ਕਰਨਾ ਹੈ। ਇੱਕ ਸਥਾਨਕ ਕੈਸ਼ ਡਾਉਨਲੋਡ ਕੀਤੇ ਪੈਕੇਜਾਂ ਅਤੇ ਅੱਪਡੇਟਾਂ ਨੂੰ ਸਟੋਰ ਕਰਦਾ ਹੈ, ਜਿਸ ਨਾਲ ਤੁਸੀਂ ਉਹਨਾਂ ਨੂੰ ਵਿਅਕਤੀਗਤ ਡਾਊਨਲੋਡਾਂ ਦੀ ਲੋੜ ਤੋਂ ਬਿਨਾਂ ਕਈ ਸਿਸਟਮਾਂ ਵਿੱਚ ਵੰਡ ਸਕਦੇ ਹੋ। ਤੁਸੀਂ ਇਸ ਕੈਸ਼ ਨੂੰ ਇੱਕ ਔਨਲਾਈਨ ਸਿਸਟਮ ਤੇ ਸੈੱਟ ਕਰੋਗੇ, ਫਿਰ ਡਾਇਰੈਕਟਰੀ ਨੂੰ ਇੱਕ ਸਿਸਟਮ ਵਿੱਚ ਭੇਜੋ ਜੋ ਕਿ ਔਫਲਾਈਨ ਹੈ ਤਾਂ ਜੋ ਹੋਰ ਸਿਸਟਮਾਂ ਨੂੰ ਪੈਕੇਜਾਂ ਤੱਕ ਪਹੁੰਚ ਕਰਨ ਦੀ ਇਜਾਜ਼ਤ ਦਿੱਤੀ ਜਾ ਸਕੇ। ਇੱਥੇ ਇਹ ਹੈ ਕਿ ਤੁਸੀਂ ਡੇਬੀਅਨ-ਅਧਾਰਿਤ ਅਤੇ Red Hat-ਅਧਾਰਿਤ ਡਿਸਟਰੀਬਿਊਸ਼ਨਾਂ ਲਈ ਇੱਕ ਸਥਾਨਕ ਕੈਸ਼ ਕਿਵੇਂ ਸੈਟ ਕਰ ਸਕਦੇ ਹੋ:

### ਡੇਬੀਅਨ/ਉਬੰਟੂ ਲਈ

1. ਸਥਾਪਿਤ ਕਰੋ ਅਤੇ ਕੌਂਫਿਗਰ ਕਰੋ [**`apt-cacher-ng`**](https://www.unix-ag.uni-kl.de/~bloch/acng/) ਡੇਬੀਅਨ/ਉਬੰਟੂ ਪੈਕੇਜਾਂ ਲਈ ਇੱਕ ਕੈਚਿੰਗ ਪ੍ਰੌਕਸੀ। ਤੁਸੀਂ ਇਸਨੂੰ ਕਮਾਂਡ ਚਲਾ ਕੇ ਸਥਾਪਿਤ ਕਰ ਸਕਦੇ ਹੋ **`sudo apt-get install apt-cacher-ng`

2. ਇੱਕ ਵਾਰ ਸਥਾਪਿਤ ਹੋਣ ਤੋਂ ਬਾਅਦ, ** ਨੂੰ ਸੰਪਾਦਿਤ ਕਰੋ`/etc/apt-cacher-ng/acng.conf` ਕੈਸ਼ਿੰਗ ਵਿਵਹਾਰ ਨੂੰ ਸੰਰਚਿਤ ਕਰਨ ਲਈ ਫਾਈਲ. ਯਕੀਨੀ ਬਣਾਓ ਕਿ **`PassThroughPattern` ਪੈਰਾਮੀਟਰ ਵਿੱਚ ਲੋੜੀਂਦੇ ਰਿਪੋਜ਼ਟਰੀ URL ਸ਼ਾਮਲ ਹੁੰਦੇ ਹਨ।

```shell
sudo nano /etc/apt-cacher-ng/acng.conf
```
PassThroughPattern ਪੈਰਾਮੀਟਰ ਵਿੱਚ ਲੋੜੀਂਦੇ ਰਿਪੋਜ਼ਟਰੀ URLs ਨੂੰ ਅਣਕਮੇਂਟ ਕਰੋ ਜਾਂ ਜੋੜੋ। ਉਦਾਹਰਨ ਲਈ, ਉਬੰਟੂ ਰਿਪੋਜ਼ਟਰੀਆਂ ਨੂੰ ਸ਼ਾਮਲ ਕਰਨ ਲਈ, ਹੇਠਾਂ ਦਿੱਤੀ ਲਾਈਨ ਨੂੰ ਜੋੜੋ ਜਾਂ ਅਨਕਮੈਂਟ ਕਰੋ:
```yml
PassThroughPattern: (security|archive).ubuntu.com/ubuntu
```
ਫਾਈਲ ਸੇਵ ਕਰੋ ਅਤੇ ਐਡੀਟਰ ਤੋਂ ਬਾਹਰ ਜਾਓ।

3. ਸ਼ੁਰੂ ਕਰੋ [**`apt-cacher-ng`**](https://www.unix-ag.uni-kl.de/~bloch/acng/) ਕਮਾਂਡ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਸੇਵਾ **`sudo systemctl start apt-cacher-ng`

```shell
sudo systemctl start apt-cacher-ng
```

4. ਔਫਲਾਈਨ ਸਿਸਟਮਾਂ 'ਤੇ, ** ਨੂੰ ਕੌਂਫਿਗਰ ਕਰੋ`/etc/apt/apt.conf.d/02proxy` ਸਥਾਨਕ ਕੈਸ਼ ਵੱਲ ਇਸ਼ਾਰਾ ਕਰਨ ਲਈ ਫਾਈਲ. ਹੇਠ ਦਿੱਤੀ ਲਾਈਨ ਦੀ ਵਰਤੋਂ ਕਰੋ: **`Acquire::http::Proxy "http://<cache-server-ip>:3142";`

```shell
sudo nano /etc/apt/apt.conf.d/02proxy
```
<cache-server-ip> ਨੂੰ ਕੈਸ਼ ਸਰਵਰ ਦੇ IP ਐਡਰੈੱਸ ਨਾਲ ਬਦਲ ਕੇ, ਫਾਈਲ ਵਿੱਚ ਹੇਠਲੀ ਲਾਈਨ ਜੋੜੋ:
```text
Acquire::http::Proxy "http://<cache-server-ip>:3142";
```
ਫਾਈਲ ਸੇਵ ਕਰੋ ਅਤੇ ਐਡੀਟਰ ਤੋਂ ਬਾਹਰ ਜਾਓ

5. ਹੁਣ, ਜਦੋਂ ਤੁਸੀਂ ** ਨੂੰ ਚਲਾਉਂਦੇ ਹੋ`apt update` ਅਤੇ **`apt upgrade` ਔਫਲਾਈਨ ਸਿਸਟਮਾਂ 'ਤੇ ਕਮਾਂਡਾਂ, ਉਹ ਸਥਾਨਕ ਕੈਸ਼ ਤੋਂ ਪੈਕੇਜਾਂ ਨੂੰ ਮੁੜ ਪ੍ਰਾਪਤ ਕਰਨਗੇ।

```shell
sudo apt update
sudo apt upgrade
```
ਇਹ ਕਮਾਂਡਾਂ ਸਥਾਨਕ ਕੈਸ਼ ਤੋਂ ਅੱਪਡੇਟ ਪ੍ਰਾਪਤ ਕਰਨ ਅਤੇ ਸਥਾਪਤ ਕਰਨਗੀਆਂ, ਔਫਲਾਈਨ ਸਿਸਟਮਾਂ 'ਤੇ ਇੰਟਰਨੈੱਟ ਪਹੁੰਚ ਦੀ ਲੋੜ ਨੂੰ ਘਟਾਉਂਦੀਆਂ ਹਨ।

ਕਿਰਪਾ ਕਰਕੇ ਨੋਟ ਕਰੋ ਕਿ ਤੁਹਾਨੂੰ ** ਨੂੰ ਬਦਲਣ ਦੀ ਲੋੜ ਪਵੇਗੀ`<cache-server-ip>` ਮਸ਼ੀਨ ਦੇ ਅਸਲ IP ਪਤੇ ਦੇ ਨਾਲ ਜਿੱਥੇ **apt-cacher-ng** ਇੰਸਟਾਲ ਹੈ।

### CentOS/RHEL ਲਈ

1. CentOS/RHEL ਲਈ, ਤੁਸੀਂ ਵਰਤ ਸਕਦੇ ਹੋ [**`yum-cron`**](https://linux.die.net/man/8/yum-cron) ਇੱਕ ਸਥਾਨਕ ਕੈਸ਼ ਸਥਾਪਤ ਕਰਨ ਲਈ. ਕਮਾਂਡ ਚਲਾ ਕੇ ਇਸਨੂੰ ਸਥਾਪਿਤ ਕਰੋ **`sudo yum install yum-cron`

2. ** ਨੂੰ ਸੰਪਾਦਿਤ ਕਰੋ`/etc/yum/yum-cron.conf` ਫਾਈਲ ਕਰੋ ਅਤੇ ** ਨੂੰ ਕੌਂਫਿਗਰ ਕਰੋ`download_only` ਪੈਰਾਮੀਟਰ ਨੂੰ **`yes` ਇਹ ਯਕੀਨੀ ਬਣਾਉਂਦਾ ਹੈ ਕਿ ਪੈਕੇਜ ਸਿਰਫ਼ ਡਾਊਨਲੋਡ ਕੀਤੇ ਗਏ ਹਨ ਅਤੇ ਸਵੈਚਲਿਤ ਤੌਰ 'ਤੇ ਸਥਾਪਤ ਨਹੀਂ ਕੀਤੇ ਗਏ ਹਨ।

```shell
sudo nano /etc/yum/yum-cron.conf
```

3. ਸ਼ੁਰੂ ਕਰੋ [**`yum-cron`**](https://linux.die.net/man/8/yum-cron) ਕਮਾਂਡ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਸੇਵਾ **`sudo systemctl start yum-cron`

```shell
sudo systemctl start yum-cron
```

4. ਔਫਲਾਈਨ ਸਿਸਟਮਾਂ 'ਤੇ, ਡਾਊਨਲੋਡ ਕੀਤੇ ਪੈਕੇਜਾਂ ਨੂੰ ਸਟੋਰ ਕਰਨ ਲਈ ਇੱਕ ਸਥਾਨਕ ਡਾਇਰੈਕਟਰੀ ਬਣਾਓ, ਉਦਾਹਰਨ ਲਈ, **`/var/cache/yum`

```shell
sudo mkdir /var/cache/yum
```

5. ਔਨਲਾਈਨ ਸਿਸਟਮ ਤੋਂ ਡਾਊਨਲੋਡ ਕੀਤੇ ਪੈਕੇਜਾਂ ਨੂੰ ਸਥਾਨਕ ਕੈਸ਼ ਡਾਇਰੈਕਟਰੀ ਵਿੱਚ ਕਾਪੀ ਕਰੋ।

```shell
sudo cp -R /var/cache/yum /path/to/local/cache
```

ਬਦਲੋ `/path/to/local/cache` ਔਫਲਾਈਨ ਸਿਸਟਮ ਤੇ ਸਥਾਨਕ ਕੈਸ਼ ਡਾਇਰੈਕਟਰੀ ਦੇ ਮਾਰਗ ਦੇ ਨਾਲ।

6. ਔਫਲਾਈਨ ਸਿਸਟਮਾਂ 'ਤੇ, ਇੱਕ ਨਵਾਂ ** ਬਣਾਓ`.repo` ** ਵਿੱਚ ਫਾਈਲ`/etc/yum.repos.d/` ਡਾਇਰੈਕਟਰੀ, ਸਥਾਨਕ ਕੈਸ਼ ਡਾਇਰੈਕਟਰੀ ਵੱਲ ਇਸ਼ਾਰਾ ਕਰਦੀ ਹੈ।

```bash
sudo nano /etc/yum.repos.d/local.repo
```
ਹੇਠਾਂ ਦਿੱਤੀ ਸਮੱਗਰੀ ਨੂੰ ਫਾਈਲ ਵਿੱਚ ਸ਼ਾਮਲ ਕਰੋ, ਬਦਲੋ `<local-cache-path>` ਸਥਾਨਕ ਕੈਸ਼ ਡਾਇਰੈਕਟਰੀ ਦੇ ਮਾਰਗ ਦੇ ਨਾਲ:
```toml
[local]
name=Local Cache
baseurl=file:///path/to/local/cache
enabled=1
gpgcheck=0
```
ਫਾਈਲ ਸੇਵ ਕਰੋ ਅਤੇ ਐਡੀਟਰ ਤੋਂ ਬਾਹਰ ਜਾਓ।

7. ਅੰਤ ਵਿੱਚ, ਤੁਸੀਂ ** ਦੀ ਵਰਤੋਂ ਕਰ ਸਕਦੇ ਹੋ`yum update` ਸਥਾਨਕ ਕੈਸ਼ ਤੋਂ ਅੱਪਡੇਟ ਸਥਾਪਤ ਕਰਨ ਲਈ ਔਫਲਾਈਨ ਸਿਸਟਮਾਂ 'ਤੇ ਕਮਾਂਡ.

```shell
sudo yum update
```

ਇਹ ਕਮਾਂਡ ਸਥਾਨਕ ਕੈਸ਼ ਤੋਂ ਪੈਕੇਜਾਂ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਔਫਲਾਈਨ ਸਿਸਟਮਾਂ ਉੱਤੇ ਪੈਕੇਜਾਂ ਨੂੰ ਅੱਪਡੇਟ ਕਰੇਗੀ।

ਕਿਰਪਾ ਕਰਕੇ ਨੋਟ ਕਰੋ ਕਿ ਤੁਹਾਨੂੰ ** ਨੂੰ ਬਦਲਣ ਦੀ ਲੋੜ ਪਵੇਗੀ`<local-cache-path>` ਔਫਲਾਈਨ ਸਿਸਟਮ ਤੇ ਸਥਾਨਕ ਕੈਸ਼ ਡਾਇਰੈਕਟਰੀ ਦੇ ਅਸਲ ਮਾਰਗ ਦੇ ਨਾਲ।

______

## ਸਿੱਟਾ

ਔਫਲਾਈਨ ਵਾਤਾਵਰਨ ਵਿੱਚ ਲੀਨਕਸ ਅੱਪਡੇਟ ਨੂੰ ਸੰਭਾਲਣਾ ਚੁਣੌਤੀਪੂਰਨ ਹੋ ਸਕਦਾ ਹੈ, ਪਰ ਸਹੀ ਪਹੁੰਚ ਨਾਲ, ਤੁਸੀਂ ਯਕੀਨੀ ਬਣਾ ਸਕਦੇ ਹੋ ਕਿ ਤੁਹਾਡੇ ਸਿਸਟਮ ਅੱਪ ਟੂ ਡੇਟ ਅਤੇ ਸੁਰੱਖਿਅਤ ਹਨ। ਇਸ ਲੇਖ ਵਿੱਚ, ਅਸੀਂ ਉਬੰਟੂ/ਡੇਬੀਅਨ ਅਤੇ CentOS/RHEL ਲਈ ਔਫਲਾਈਨ ਅੱਪਡੇਟ ਸਥਾਪਤ ਕਰਨ ਦੇ ਸਭ ਤੋਂ ਵਧੀਆ ਤਰੀਕਿਆਂ ਬਾਰੇ ਚਰਚਾ ਕੀਤੀ ਹੈ। ਅਸੀਂ ਡੇਬੀਅਨ-ਅਧਾਰਿਤ ਅਤੇ Red Hat-ਅਧਾਰਿਤ ਡਿਸਟਰੀਬਿਊਸ਼ਨ ਦੋਵਾਂ ਲਈ ਕਦਮ-ਦਰ-ਕਦਮ ਨਿਰਦੇਸ਼ ਪ੍ਰਦਾਨ ਕਰਦੇ ਹੋਏ, ਇੱਕ ਸਥਾਨਕ ਰਿਪੋਜ਼ਟਰੀ ਸਥਾਪਤ ਕਰਨ ਅਤੇ ਇੱਕ ਸਥਾਨਕ ਕੈਸ਼ ਸਥਾਪਤ ਕਰਨ ਦੀ ਖੋਜ ਕੀਤੀ।

ਇਹਨਾਂ ਤਰੀਕਿਆਂ ਦੀ ਪਾਲਣਾ ਕਰਕੇ, ਤੁਸੀਂ ਆਪਣੇ ਲੀਨਕਸ ਸਿਸਟਮਾਂ ਦੀ ਸੁਰੱਖਿਆ ਅਤੇ ਸਥਿਰਤਾ ਨੂੰ ਬਰਕਰਾਰ ਰੱਖ ਸਕਦੇ ਹੋ, ਇੱਥੋਂ ਤੱਕ ਕਿ ਔਫਲਾਈਨ ਵਾਤਾਵਰਨ ਵਿੱਚ ਵੀ। ਨਵੀਨਤਮ ਅੱਪਡੇਟ ਸ਼ਾਮਲ ਕਰਨ ਲਈ ਸਮੇਂ-ਸਮੇਂ 'ਤੇ ਆਪਣੀ ਸਥਾਨਕ ਰਿਪੋਜ਼ਟਰੀ ਜਾਂ ਕੈਸ਼ ਨੂੰ ਅੱਪਡੇਟ ਕਰਨਾ ਯਾਦ ਰੱਖੋ।

______

## ਹਵਾਲੇ

- [apt-mirror Documentation](https://manpages.debian.org/jessie/apt-mirror/apt-mirror.1.en.html)
- [debmirror Documentation](https://wiki.debian.org/debmirror)
- [createrepo Documentation](https://linux.die.net/man/8/createrepo)
- [apt-cacher-ng Documentation](https://www.unix-ag.uni-kl.de/~bloch/acng/)
- [yum-cron Documentation](https://linux.die.net/man/8/yum-cron)
