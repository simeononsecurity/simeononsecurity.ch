---
title: "CompTIA Linux+ (XK0-005): Linux Troubleshooting"
date: 2025-01-01
toc: true
draft: false
description: "Master Linux troubleshooting for the CompTIA Linux+ XK0-005 exam. Diagnose storage, network, DNS, CPU, memory, authentication, boot, service, and package problems with real commands."
genre: ["CompTIA Linux+ Course", "Linux Troubleshooting", "System Administration", "Performance Tuning", "Network Diagnostics", "Boot Recovery", "Linux Certification", "DevOps", "IT Support", "Diagnostics"]
tags: ["CompTIA Linux+", "XK0-005", "troubleshooting", "fsck", "journalctl", "systemctl", "tcpdump", "dig", "top", "htop", "boot failures", "GRUB", "DNS", "performance", "storage", "network connectivity"]
cover: "/img/cover/comptia-linux-troubleshooting-workflow-illustration.webp"
coverAlt: "An illustration showing a modern computer setup with terminal commands related to Linux troubleshooting, including network connectivity and performance graphs, against a dark background."
coverCaption: "Master Linux Troubleshooting for the XK0-005 Exam"
---

#### [Click Here to Return To the CompTIA Linux+ Course Page](/linux-plus-start/)

**Troubleshooting** is **28%** of the **CompTIA Linux+ (XK0-005)** exam, the second-heaviest domain. This module teaches you a structured method plus the exact commands you run to fix storage, network, performance, authentication, boot, and service problems. *Strong troubleshooting separates a junior admin from a senior one.*

## Troubleshooting Methodology

Work every problem the same way so you fix the cause, not the symptom:

1. **Identify the problem** and gather information
2. **Establish a theory** of probable cause
3. **Test the theory** to confirm or reject it
4. **Plan and implement** a fix
5. **Verify** full functionality
6. **Document** findings and lessons learned

Example: a website returns 502 errors. You theorize the backend is down, test with `systemctl status app`, see it failed, read `journalctl -u app`, find a config typo, fix it, restart, and confirm the site loads.

## Storage Troubleshooting

```bash
df -h                  # which filesystem is full
df -i                  # inode exhaustion (many tiny files)
du -sh /var/* | sort -h # find the largest directories
lsblk                  # confirm devices and mounts
sudo fsck /dev/sdb1    # check and repair ext filesystems (unmounted)
sudo xfs_repair /dev/sdb1   # repair XFS
```

A full **/boot** stops kernel updates, so clear old kernels. *A filesystem that remounts read-only usually points to disk errors, which you confirm in `dmesg` and the SMART data from `smartctl`.* Check LVM with **pvs**, **vgs**, and **lvs**.

## Network Connectivity

```bash
ping -c4 8.8.8.8          # is the network reachable
ip route                  # is there a default gateway
ip addr                   # does the interface have an address
traceroute example.com    # where does the path break
mtr example.com           # continuous path quality
ss -tulpn                 # what is listening locally
sudo tcpdump -i eth0 port 443   # capture traffic for analysis
```

Work up the stack: link, address, gateway, DNS, then application.

## DNS Resolution

```bash
dig example.com           # full query detail
dig +short example.com    # just the answer
nslookup example.com
host example.com
cat /etc/resolv.conf      # which resolvers are configured
cat /etc/nsswitch.conf    # hosts: files dns order
resolvectl status         # systemd-resolved view
```

*If `ping 8.8.8.8` works but `ping example.com` fails, the problem is DNS, not connectivity.*

## CPU and Memory Performance

```bash
uptime                # load average over 1, 5, 15 minutes
top                   # live CPU and memory by process
htop                  # interactive version
vmstat 1 5            # CPU, memory, IO, and swap activity
free -h               # memory and swap usage
sar -u 1 5            # historical CPU stats
```

**Load average** compares to your core count. A load of 4.0 on a 4-core box is full but healthy. When memory runs out, the **OOM killer** terminates a process and logs it to `journalctl -k`. Heavy **swap** use means you need more RAM.

Find and stop a runaway process:

```bash
ps aux --sort=-%cpu | head     # top CPU consumers
ps aux --sort=-%mem | head     # top memory consumers
kill -15 <pid>                 # ask it to stop
kill -9 <pid>                  # force it if needed
```

## Authentication and Access

```bash
passwd -S alice           # account status (locked, expired)
sudo faillock --user alice # failed-login lockouts
chage -l alice            # password aging
ls -ld ~/.ssh             # must be 700
ls -l ~/.ssh/authorized_keys   # must be 600
```

*SSH refuses keys when `~/.ssh` or `authorized_keys` permissions are too open, so fix them first.* PAM misconfigurations in **/etc/pam.d/** can lock everyone out, so test changes in a second session.

## Logs

```bash
ls /var/log/                       # syslog, secure, messages, journal
journalctl -u sshd                 # one service
journalctl -b                      # since last boot
journalctl -p err --since "1 hour ago"
journalctl -k                      # kernel messages
```

Make the journal persistent by creating `/var/log/journal` and running `systemctl restart systemd-journald`.

## Boot Failures

```bash
# At the GRUB menu, edit the kernel line and append:
systemd.unit=rescue.target     # minimal single-user shell
systemd.unit=emergency.target  # even more minimal

# Rebuild a missing initramfs:
sudo dracut --force                 # Red Hat family
sudo update-initramfs -u            # Debian/Ubuntu

# Repair GRUB:
sudo grub2-mkconfig -o /boot/grub2/grub.cfg
```

A failed mount in **/etc/fstab** drops you to emergency mode, so comment the bad line and reboot.

## Service and Package Failures

```bash
systemctl status app          # current state and recent logs
journalctl -u app -n 50       # last 50 log lines
systemctl cat app             # show the unit file
systemctl daemon-reload       # after editing a unit
```

Fix package problems:

```bash
sudo dnf clean all && sudo dnf makecache    # rebuild dnf cache
sudo apt clean && sudo apt update           # rebuild apt index
sudo dpkg --configure -a                    # finish interrupted installs
```

## Security Anomalies

Investigate signs of compromise:

```bash
find / -perm -4000 -type f 2>/dev/null   # unexpected SUID binaries
sudo crontab -l ; ls /etc/cron.*          # unauthorized cron jobs
ss -tunp                                  # suspicious connections
last ; lastb                              # login and failed-login history
```

*A new SUID root binary, an unknown cron job, or an outbound connection to an odd port all warrant a deeper investigation.*

## Next Steps

Troubleshooting ties the course together. Revisit [Linux System Management](/linux-plus/linux-system-management/) for the administration commands, [Linux Security](/linux-plus/linux-security/) for hardening, and [Scripting, Containers, and Automation](/linux-plus/scripting-containers-automation/) to automate fixes.

Return to the [CompTIA Linux+ Course](/linux-plus-start/) and confirm your readiness with the [CompTIA Linux+ Practice Test](/linux-plus-practice-test/).
