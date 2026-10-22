---
title: "Linux+ XK0-006 Services and User Management Lab"
date: 2026-10-10
lastmod: 2026-10-21
toc: true
draft: false
description: "Practice Linux+ XK0-006 services and user management with accounts, processes, packages, systemd, logs, and containers in a disposable lab."
genre: ["CompTIA Linux+ Course", "Linux Certification", "System Administration"]
tags: ["CompTIA Linux+", "XK0-006", "user management", "systemd", "processes", "package management", "containers"]
cover: "/img/cover/comptia-linux-plus-xk0-005-study-guide-illustration.webp"
coverAlt: "Linux server and terminal illustration used for a services and user management lab."
coverCaption: "Practice Linux services and user management"
---

[Return to the Linux+ course](/linux-plus-start/)

**Services and User Management makes up 20% of Linux+ XK0-006.** You need to manage local accounts, processes, applications, systemd units, and containers. Follow this lesson on a disposable Debian or Ubuntu VM with a snapshot and a non-root account that has approved sudo access. The commands and expected observations are examples. Record your own output.

## Identify the System Before Changing It

Run these read-only checks and save the results in a private lab log:

```bash
cat /etc/os-release
id
getent passwd
systemctl --version
```

The release identifies the distribution. `id` shows your effective user and groups. `getent passwd` lists account records from configured identity sources, so it might include more than `/etc/passwd`. If `systemctl` reports that systemd is not PID 1, use a VM that runs systemd for the unit exercise.

## Manage One Disposable Account

Create a lab account named `labreader` only on the VM. Ask the VM owner before using a different host. The Debian `adduser` command prompts for a password and optional details:

```bash
sudo adduser labreader
id labreader
getent passwd labreader
sudo chage -l labreader
```

Check the UID, primary group, home directory, shell, and account aging. A user account, system account, and service account serve different purposes. Do not assign broad sudo rights to a service identity to make a test pass. To test access, create a harmless file in your home directory and compare its readability as your user and `labreader`. Record an allowed and a denied result. The [security lesson](/linux-plus/linux-security/) covers ownership, ACLs, and sudo policy in detail.

Locking a password is not the same as disabling every access route. SSH keys, sessions, and external identity systems need separate review. On this disposable account, compare `passwd -S labreader` before and after the following commands:

```bash
sudo passwd -l labreader
sudo passwd -u labreader
```

Only remove the account after you have saved evidence and confirmed that no lab task still needs it. `sudo deluser --remove-home labreader` deletes its home directory on Debian-based systems. Check the path before using that cleanup command.

## Inspect Processes and Jobs

Use `ps -eo pid,ppid,user,stat,comm` to see process IDs, parents, owners, states, and names. Compare one service process with its unit using `systemctl status`. A sleeping process is not necessarily stuck. A zombie has exited but awaits parent collection. A high CPU value needs a time window and baseline before you label it a fault.

Start a harmless shell job in your own session:

```bash
sleep 60 &
jobs -l
```

Record its PID. Send `TERM` with `kill <PID>`, then confirm the job has exited with `jobs -l` or `ps -p <PID>`. Replace `<PID>` with the PID you observed. Do not send signals to a guessed system process. `TERM` permits graceful handling, while `KILL` forces termination and gives a process no cleanup opportunity.

## Inspect Packages and a Service

Use the package manager for the distribution you recorded. On Debian or Ubuntu, run `apt-cache policy nginx` to inspect the candidate version without installing it. On an RPM-based system, use `dnf info nginx`. Confirm repository trust and planned changes before installing any package. A third-party repository adds its own update and signing risk.

Use an already installed service for a read-only systemd check. On many VMs, `systemd-journald.service` exists:

```bash
systemctl status systemd-journald.service --no-pager
journalctl -u systemd-journald.service -n 20 --no-pager
systemctl is-enabled systemd-journald.service
```

Expected evidence is a unit state, recent log entries, and an enablement result. `active` and `enabled` answer different questions. A service can run now without starting automatically at boot. If this unit is absent, choose another installed service and write down its exact unit name. Practice start, stop, reload, and override commands only on a disposable lab service, not on the host logger or remote access service.

Systemd also manages timers, mounts, and targets. Use `systemctl list-timers --all` to identify one timer and its next scheduled run. Use `timedatectl status` to inspect time synchronization. Explain which service or timer owns each observed action.

## Inspect a Container Safely

If Podman or Docker is installed and the VM owner approved a known image, run a small offline-capable or local image. Record its exact source and digest before use. Use `podman ps -a`, `podman inspect <container>`, and `podman logs <container>` to capture state, configuration, and output. Stop and remove only the container you created. A container shares the host kernel, so it is not a substitute for a disposable VM when testing untrusted code.

Without an approved runtime or image, mark this task Not run. Explain image layers, a `Dockerfile` with `FROM`, `USER`, `CMD`, and `ENTRYPOINT`, bridge versus host networking, and why a privileged container broadens host access. Compare those notes with the [official XK0-006 objective 2.5](https://lecbyo.files.cmp.optimizely.com/download/4ae79a48529711f08baa4a1390fb0d85).

## Trace Authentication, Authorization, and Accounting

Objective 2.6 covers the path from identity to permitted action and audit evidence. On the same disposable VM, use the account you created above. Run read-only checks:

```bash
id labreader
getent group sudo
sudo -l -U labreader
sudo journalctl _COMM=sudo -n 10 --no-pager
```

Record the groups for `labreader`, whether a sudo rule permits any command, and whether the journal contains an event from your own lab activity. `sudo -l -U` might return a nonzero status for a user without privileges. That denial is useful evidence. The journal might have no matching entries if logging is configured elsewhere. Redact account names and host details before sharing a report. Do not edit sudoers or a production PAM stack to create a passing result.

On Debian or Ubuntu, inspect `/etc/pam.d/sudo` with `cat` and identify which PAM entries delegate authentication or account checks. If `pkaction` is installed, run `pkaction --version` and explain that Polkit governs selected system actions through policy and an authentication agent. These checks show configuration and available tools, not proof that every login or authorization path has been tested. For centralized identity, draw a path from a client through SSSD or Winbind to a directory such as LDAP or an authentication system such as Kerberos. Explain where Samba fits when Windows file or domain integration is in scope. Mark live centralized-identity tests Not run unless the VM has an approved test directory. If `auditd` is installed, identify its running state and one relevant audit rule or event without changing system policy.

**Pass check:** a reviewer can separate identity lookup, authentication, authorization, and accounting in your observed local example. The reviewer can point to the actual command output supporting each observed claim and identify which centralized-identity or auditing paths remain untested. Use the [official XK0-006 objective 2.6](https://lecbyo.files.cmp.optimizely.com/download/4ae79a48529711f08baa4a1390fb0d85) as the topic boundary.

## Check Your Work

Give a reviewer your account record, allowed and denied file test, process PID and signal result, package candidate, unit state and log excerpt, timer result, authentication and authorization trace, and container evidence or Not run reason. Include the initial snapshot name, the commands you ran, and cleanup. A pass needs observed evidence from your VM and a correct explanation of why each result occurred. Revisit any numbered objective without evidence before claiming exam readiness.

Continue with [Linux Security](/linux-plus/linux-security/), then [Automation and Scripting](/linux-plus/scripting-containers-automation/).

## Next Steps

Continue with [Linux Security](/linux-plus/linux-security/) and return to the [Linux+ course](/linux-plus-start/).
