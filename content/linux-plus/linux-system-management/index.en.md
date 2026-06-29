---
title: "CompTIA Linux+ (XK0-005): Linux System Management"
date: 2025-01-01
toc: true
draft: false
description: "Master Linux system management for the CompTIA Linux+ XK0-005 exam. Learn file management, storage and LVM, networking, processes, systemd services, package management, users, cron, and boot loaders with real command examples."
genre: ["CompTIA Linux+ Course", "Linux System Administration", "System Management", "Storage Management", "Linux Networking", "Process Management", "systemd", "Package Management", "Linux Certification", "DevOps"]
tags: ["CompTIA Linux+", "XK0-005", "system management", "LVM", "systemd", "file management", "storage", "partitions", "networking", "processes", "cron", "package management", "dnf", "apt", "GRUB2", "kernel modules", "user management", "fstab"]
cover: "/img/cover/comptia-linux-system-management-illustration.webp"
coverAlt: "A laptop displaying a Linux terminal interface with various commands and colorful outputs. Surrounding elements include files, storage devices, and network representations, all on a dark background."
coverCaption: "Master Linux System Management for the XK0-005 Exam"
---

#### [Click Here to Return To the CompTIA Linux+ Course Page](/linux-plus-start/)

**System Management** is the largest domain on the **CompTIA Linux+ (XK0-005)** exam at **32%** of your score. This module teaches you how to manage files, storage, networking, processes, services, software, users, and the boot process on Linux. Every command here is something a working administrator runs weekly. *Master this domain first, because the security, scripting, and troubleshooting domains all build on it.*

## File and Directory Management

The shell is where you spend most of your time. Learn these commands until they are muscle memory.

**ls** lists directory contents. The flags matter on the exam:

```bash
ls -l       # long format: permissions, owner, size, date
ls -lh      # human-readable sizes (K, M, G)
ls -la      # include hidden dotfiles
ls -lt      # sort by modification time, newest first
ls -lR      # recurse into subdirectories
```

**cp**, **mv**, and **rm** copy, move, and remove. The `-r` flag works on directories, and `-i` prompts before overwriting:

```bash
cp -r /etc/skel /home/newuser    # copy a directory tree
mv report.txt /srv/reports/      # move (or rename)
rm -rf /tmp/build                # remove recursively, no prompt
```

*The command `rm -rf /` deletes everything, so check your path twice before you run a recursive delete as root.*

**find** searches the live filesystem by name, size, owner, type, or time. It is the most flexible search tool you have:

```bash
find /var/log -name "*.log" -mtime +7      # logs older than 7 days
find /home -user alice -type f             # files owned by alice
find / -size +100M 2>/dev/null             # files larger than 100 MB
find /etc -name "*.conf" -exec grep -l ssh {} \;   # run a command on each hit
```

**locate** searches a prebuilt index instead of walking the disk, so it returns results fast. The index is refreshed by **updatedb**:

```bash
sudo updatedb
locate sshd_config
```

*locate is fast but stale, since it only knows what the last updatedb run indexed.*

### Archiving with tar

**tar** bundles many files into one archive, often compressed:

```bash
tar -czf backup.tar.gz /etc            # create gzip archive
tar -xzf backup.tar.gz                 # extract
tar -tzf backup.tar.gz                 # list contents without extracting
tar -cJf backup.tar.xz /etc            # create xz archive (smaller)
```

Remember the letters: **c** create, **x** extract, **t** list, **z** gzip, **J** xz, **f** file.

### Links: hard vs symbolic

**ln** creates links. A **hard link** is a second name for the same inode and data. A **symbolic link** (symlink) is a small file that points to a path.

```bash
ln file.txt hardlink.txt        # hard link, same inode
ln -s /opt/app/bin app          # symbolic link to a path
ls -li                          # the -i flag shows inode numbers
```

| Property | Hard link | Symbolic link |
|----------|-----------|---------------|
| Points to | Inode | Path |
| Works across filesystems | No | Yes |
| Survives target rename | Yes | No (breaks) |
| Can link directories | No | Yes |

*A symlink breaks when its target path moves, while a hard link keeps working until every name for that inode is removed.*

### File globbing

The shell expands wildcards before the command runs:

- `*` matches any string, so `ls *.txt` lists every text file
- `?` matches one character, so `file?.log` matches `file1.log`
- `[a-c]` matches a range, so `report[1-3].csv` matches three files
- `{a,b}` brace expansion, so `cp file.{txt,bak}` copies to two names

## Storage, Partitions, and Filesystems

You prepare a new disk in three steps: partition it, put a filesystem on it, then mount it.

**Partition** the disk. Use **fdisk** for MBR and **gdisk** or **parted** for GPT:

```bash
sudo fdisk /dev/sdb     # interactive MBR partitioning
sudo gdisk /dev/sdb     # interactive GPT partitioning
sudo parted /dev/sdb print
```

**Create a filesystem** with the right **mkfs** variant:

```bash
sudo mkfs.ext4 /dev/sdb1
sudo mkfs.xfs  /dev/sdb1
```

Inspect block devices and usage:

```bash
lsblk                  # tree of disks, partitions, and mount points
blkid                  # show UUIDs and filesystem types
df -h                  # mounted filesystem usage, human readable
df -i                  # inode usage (a disk full of tiny files)
du -sh /var/log        # total size of a directory
```

*A disk that reports full while `df -h` shows free space often has run out of inodes, which `df -i` reveals.*

## Logical Volume Manager (LVM)

**LVM** adds a flexible layer between physical disks and filesystems, so you grow storage without downtime. The stack is **physical volume (PV) → volume group (VG) → logical volume (LV)**.

A complete worked example that builds a volume and then grows it:

```bash
# 1. Mark two disks as physical volumes
sudo pvcreate /dev/sdb /dev/sdc

# 2. Pool them into a volume group named "data"
sudo vgcreate data /dev/sdb /dev/sdc

# 3. Carve a 50 GB logical volume named "web"
sudo lvcreate -L 50G -n web data

# 4. Put a filesystem on it and mount it
sudo mkfs.xfs /dev/data/web
sudo mkdir /srv/web
sudo mount /dev/data/web /srv/web

# 5. Later, grow the volume and the filesystem online
sudo lvextend -L +20G /dev/data/web
sudo xfs_growfs /srv/web          # XFS grows in place
# For ext4 you would run: sudo resize2fs /dev/data/web
```

Check LVM status with **pvs**, **vgs**, and **lvs**. *XFS only grows, never shrinks, so plan sizes before you commit.*

## Mounting and /etc/fstab

**mount** attaches a filesystem to a directory, and **umount** detaches it:

```bash
sudo mount /dev/sdb1 /mnt
sudo umount /mnt
```

Manual mounts vanish on reboot. For persistent mounts, add a line to **/etc/fstab**. Each line has six fields:

```
UUID=1234-5678   /srv/web   xfs   defaults   0   2
```

| Field | Meaning |
|-------|---------|
| 1 | Device (UUID is safest, since device names change) |
| 2 | Mount point |
| 3 | Filesystem type |
| 4 | Options (defaults, noatime, ro) |
| 5 | dump (almost always 0) |
| 6 | fsck order (0 skip, 1 root, 2 others) |

Get the UUID from **blkid**, then test before rebooting:

```bash
sudo mount -a    # mount everything in fstab; errors show now, not at boot
```

*A bad fstab entry stops the system at boot, so always run `mount -a` to test before you reboot.*

**autofs** mounts filesystems on demand and unmounts them after idle time, which suits network shares.

## Disk Quotas

Quotas limit how much storage a user or group consumes. Enable the `usrquota` or `grpquota` mount option, then:

```bash
sudo quotacheck -cug /home     # build quota database files
sudo edquota -u alice          # edit soft and hard limits for a user
sudo quota -u alice            # report a user's usage
```

A **soft limit** warns and starts a grace period, while a **hard limit** blocks writes immediately.

## Network Configuration

Modern distributions manage networking with **NetworkManager** and **systemd**. Learn the **ip** suite plus **nmcli**.

```bash
ip addr                # show interfaces and IP addresses
ip route               # show the routing table
ip link set eth0 up    # bring an interface up
nmcli device status    # NetworkManager view of devices
nmcli connection show  # saved connection profiles
nmtui                  # text menu for connections
hostnamectl set-hostname web01
```

DNS resolvers live in **/etc/resolv.conf**, static name mappings in **/etc/hosts**, and you inspect open sockets with **ss**:

```bash
ss -tulpn        # TCP/UDP listening ports with process names
```

*Edit connections through nmcli or nmtui, since NetworkManager overwrites hand-edited interface files on many distributions.*

## Process and Service Management

Every running program is a **process** with a PID. You list, prioritize, and signal them.

```bash
ps aux              # every process with CPU and memory use
ps -ef              # full-format listing with parent PIDs
top                 # live, sortable process view
htop                # friendlier interactive version
```

Send signals with **kill**, **killall**, or **pkill**:

```bash
kill 1432           # send SIGTERM (15), a polite stop
kill -9 1432        # send SIGKILL (9), a forced stop
killall nginx       # signal by name
pkill -u alice      # signal all of a user's processes
```

*Reach for SIGTERM first so the process cleans up, and use SIGKILL only when it refuses to exit.*

Adjust scheduling priority with **nice** (start) and **renice** (running). Lower numbers get more CPU:

```bash
nice -n 10 ./batch.sh     # start with lower priority
renice -n -5 -p 1432      # raise priority of a running PID (root only)
```

Manage background jobs in your shell with **jobs**, **bg**, and **fg**, and suspend with Ctrl+Z.

### systemd and systemctl

**systemd** is the init system and service manager on most modern distributions. You control units with **systemctl**:

```bash
systemctl start nginx        # start now
systemctl stop nginx         # stop now
systemctl restart nginx      # stop then start
systemctl reload nginx       # reload config without dropping connections
systemctl enable nginx       # start at boot
systemctl disable nginx      # do not start at boot
systemctl status nginx       # state plus recent log lines
systemctl list-units --type=service
```

Unit files live in **/etc/systemd/system/** (admin) and **/usr/lib/systemd/system/** (packages). After editing one, run `systemctl daemon-reload`.

**Boot targets** replace old runlevels:

```bash
systemctl get-default
systemctl set-default multi-user.target    # text login, no GUI
systemctl isolate graphical.target         # switch now
```

Read logs with **journalctl**:

```bash
journalctl -u nginx          # logs for one unit
journalctl -b                # logs since last boot
journalctl -p err --since "1 hour ago"
```

**systemd timers** are a modern replacement for cron, pairing a `.timer` unit with a `.service` unit.

## Package Management

You install, update, and remove software with your distribution's package manager.

On Red Hat, Fedora, and Rocky Linux you use **dnf** (with **rpm** for single files):

```bash
sudo dnf install httpd
sudo dnf update
sudo dnf remove httpd
dnf search nginx
rpm -qa | grep httpd        # query installed packages
rpm -ivh package.rpm        # install a local rpm
```

On Debian and Ubuntu you use **apt** (with **dpkg** for single files):

```bash
sudo apt update             # refresh package index
sudo apt install nginx
sudo apt upgrade
sudo apt remove nginx
dpkg -l | grep nginx        # query installed packages
sudo dpkg -i package.deb    # install a local deb
```

When no package exists, you **compile from source**:

```bash
./configure        # check dependencies and set options
make               # build
sudo make install  # install
```

## Users, Groups, and Localization

Accounts live in **/etc/passwd** (account data), **/etc/shadow** (hashed passwords), and **/etc/group** (groups). Manage them with:

```bash
sudo useradd -m -s /bin/bash alice    # create with home dir and shell
sudo passwd alice                     # set a password
sudo usermod -aG wheel alice          # add to a supplementary group
sudo userdel -r alice                 # delete and remove home dir
sudo groupadd developers
```

The **/etc/skel** directory holds files copied into every new home directory, so put default dotfiles there.

Set localization with:

```bash
timedatectl set-timezone America/Chicago
timedatectl set-ntp true
localectl set-locale LANG=en_US.UTF-8
```

## Scheduling Tasks

**cron** runs recurring jobs. Edit your crontab with `crontab -e`. Each line has five time fields plus a command:

```
* * * * * command
| | | | |
| | | | +-- day of week (0-7, 0 and 7 are Sunday)
| | | +---- month (1-12)
| | +------ day of month (1-31)
| +-------- hour (0-23)
+---------- minute (0-59)
```

Examples:

```bash
0 2 * * *      /usr/local/bin/backup.sh    # every day at 02:00
*/15 * * * *   /usr/local/bin/check.sh      # every 15 minutes
0 0 1 * *      /usr/local/bin/report.sh      # midnight on the 1st
```

Run a one-time job later with **at**:

```bash
echo "/usr/local/bin/patch.sh" | at 22:00
```

**systemd timers** do the same work with logging and dependency control, using a `.timer` and `.service` pair.

## Kernel Modules

The kernel loads drivers as **modules**. Manage them with:

```bash
lsmod                       # list loaded modules
sudo modprobe e1000e        # load a module and its dependencies
sudo modprobe -r e1000e     # unload a module
modinfo e1000e              # show module details
```

To load a module at every boot, add its name to a file under **/etc/modules-load.d/**.

## Boot Loaders and GRUB2

**GRUB2** is the boot loader on most systems. You configure defaults in **/etc/default/grub**, then regenerate the real config:

```bash
sudo vi /etc/default/grub                 # edit timeout, kernel options
sudo grub2-mkconfig -o /boot/grub2/grub.cfg   # Red Hat family
sudo update-grub                          # Debian/Ubuntu wrapper
```

*Never hand-edit the generated grub.cfg, since the next regeneration overwrites it. Change /etc/default/grub instead.*

For recovery, you append `systemd.unit=rescue.target` or `single` to the kernel line in the GRUB menu to reach a minimal shell.

## Next Steps

System management gives you the foundation for the rest of the course. Continue with [Linux Security](/linux-plus/linux-security/) to harden these systems, then move to [Scripting, Containers, and Automation](/linux-plus/scripting-containers-automation/) to automate them. When something breaks, [Linux Troubleshooting](/linux-plus/linux-troubleshooting/) shows you how to diagnose it.

Return to the [CompTIA Linux+ Course](/linux-plus-start/) to track your progress, and measure your readiness with the [CompTIA Linux+ Practice Test](/linux-plus-practice-test/).
