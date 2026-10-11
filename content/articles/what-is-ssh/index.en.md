---
title: "SSH Guide: Secure Remote Access, Keys, and File Transfer"
date: 2023-06-14
lastmod: 2026-10-11
toc: true
draft: false
description: "Learn what SSH does, how to create keys, verify host keys, transfer files, and manage client and server settings."
tags: ["SSH", "Secure Shell", "remote access", "remote management", "encryption", "authentication", "data integrity", "portability", "file transfer", "SCP", "SFTP", "SSH keys", "Ed25519", "SSH configuration", "known hosts", "network protocol", "remote command execution", "OpenSSH", "two-factor authentication", "public key cryptography", "IP address", "domain name", "terminal", "command prompt", "security", "system administrators", "developers", "authentication methods", "tunneling"]
cover: "/img/cover/A_cartoon_illustration_of_a_person_securely_connecting.webp"
coverAlt: "A cartoon illustration of a person securely connecting to a server using SSH."
coverCaption: ""
---

**What is SSH and How to Use SSH?**

**SSH** (Secure Shell) is a network protocol for encrypted remote login, command execution, port forwarding, and file transfer. An SSH client connects to an SSH server over an untrusted network. The server proves its identity with a host key, then the user authenticates with a password, public key, or another configured method.

The [OpenBSD `ssh(1)` manual](https://man.openbsd.org/ssh) describes the client as a tool for secure encrypted communication between untrusted hosts. This guide focuses on **OpenSSH**, the implementation found on many Linux, macOS, BSD, and Windows systems.

{{< youtube id="Atbl7D_yPug" enable="true" >}}

**Difficulty:** Beginner. **Time:** 15 minutes.

## Key takeaways

- SSH checks the server host key before user authentication.
- A passphrase-protected Ed25519 key is the preferred starting point for new users.
- Use `ssh` for remote commands, `scp` for file copies, and `sftp` for interactive transfers.
- Test a new key in a separate session before disabling password authentication.

## Before you begin

- Install an OpenSSH client on your local computer.
- Get the remote hostname or IP address, account name, SSH port, and an approved way to authenticate.
- Obtain the server host-key fingerprint from a trusted console, administrator record, or other independent source.
- Keep an existing password login or local console session available when installing a public key or changing server settings.

The shell commands in this guide use POSIX syntax on Linux, macOS, BSD, or a compatible environment. Windows OpenSSH users should adapt file paths and permission commands for PowerShell or WSL. Run client commands on your local computer. Run server commands, including `sshd -t`, on the SSH server with access to its configuration and host keys.

## SSH at a glance

| Task | Tool | Result |
|------|------|--------|
| **Remote login** | `ssh` | Open a shell or run a command on a remote host |
| **Key creation** | `ssh-keygen` | Create a private key and a matching public key |
| **File copy** | `scp` | Copy files over an SSH connection |
| **Interactive transfer** | `sftp` | Browse and transfer files through SFTP |
| **Client settings** | `~/.ssh/config` | Store per-host connection options |
| **Server settings** | `/etc/ssh/sshd_config` | Configure the OpenSSH daemon |

*The encrypted channel protects transport. You still need to verify the destination, restrict keys, and review each remote command.*

## Benefits of SSH

SSH separates **host authentication** from **user authentication**. A client checks the server host key, a cryptographic identity for the server. The server then checks the user's password, public key, or another allowed method.

1. **Security**: SSH encrypts the session between the client and server. Encryption protects credentials, commands, and returned data while they cross an untrusted network.

2. **Authentication**: SSH supports passwords, public keys, keyboard-interactive methods, and other server-approved methods. Public-key authentication keeps the private key on the client and sends proof of key ownership during login.

3. **Data integrity**: The SSH transport protects messages from undetected modification. A valid encrypted session still depends on correct host-key verification.

4. **Portability**: OpenSSH clients and servers exist across Linux, macOS, BSD, and Windows. The same basic `ssh`, `scp`, and `sftp` workflow transfers across those platforms.

5. **Flexibility**: SSH supports remote commands, file transfer, port forwarding, and other connection features. Use each feature only for an approved purpose and destination.

| Authentication choice | Strength | Operational trade-off |
|-----------------------|----------|-----------------------|
| **Password** | Familiar and easy to deploy | Exposed to guessing and credential reuse |
| **Public key** | Private key stays on the client | Requires key lifecycle and recovery planning |
| **Public key with passphrase** | Adds protection if a private key file is copied | Requires passphrase entry or an SSH agent |
| **Keyboard-interactive or multi-factor authentication (MFA)** | Adds a server-controlled challenge | Needs server and client support |

***A passphrase-protected user key is the default choice for interactive administration.***

## How to Use SSH

### Generating SSH Keys

Before using public-key authentication, create an SSH key pair. The pair contains a **public key** for the remote account and a **private key** for the local client. Place the public key in the remote account's `~/.ssh/authorized_keys` file. Keep the private key on the client and protect the private key with a passphrase.

1. Install **OpenSSH** on your local machine if OpenSSH is absent. Refer to the official documentation for the operating system.

2. Open a terminal or command prompt and run the following command to generate the original RSA example:

```shell

ssh-keygen -t rsa -b 4096

```

For a new user key, use **Ed25519** on systems with current OpenSSH support:

```shell
ssh-keygen -t ed25519 -C "reader@example.com"
```

The current OpenBSD manual lists Ed25519 as the default key type when `ssh-keygen` receives no `-t` option. The original RSA command remains useful for older systems or compatibility requirements. The `-b` flag controls RSA key size. Ed25519 uses a fixed key size.

3. Enter a file name and a strong passphrase when prompted. Press Enter to accept the default file name only when the default key will serve the intended account. A blank passphrase leaves a copied private key without at-rest protection.

4. The key pair will be generated. The public key ends in `.pub`. The private key has no extension and must stay private.

Install the public key through an existing password login or a local console session. On a system with `ssh-copy-id`, run:

```shell
ssh-copy-id -i ~/.ssh/id_ed25519.pub username@remote_server_ip
```

Use `~/.ssh/id_ed25519.pub` with the Ed25519 command. The preserved RSA command creates `~/.ssh/id_rsa.pub`, so substitute the RSA path when installing an RSA key. If `ssh-copy-id` is unavailable, run this on the client through an existing password login:

```shell
cat ~/.ssh/id_ed25519.pub | ssh username@remote_server_ip 'umask 077 && mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys'
```

The command creates a private remote `.ssh` directory and appends one public-key line. Verify the remote `~/.ssh/authorized_keys` file contains the intended key. The `authorized_keys` file lists public keys permitted to log in. If a local console session is the only access path, append the same public-key line there, then set `~/.ssh` to mode `700` and `authorized_keys` to mode `600`.

If you selected the RSA example, replace every later `id_ed25519` path with `id_rsa`.

Open a new terminal and test the key before changing server authentication settings:

```shell
ssh -o PreferredAuthentications=publickey -o PasswordAuthentication=no -i ~/.ssh/id_ed25519 username@remote_server_ip
```

Confirm the new session opens with the intended account. Keep the existing session available for recovery if the test fails.

Check a public-key fingerprint before installing or auditing a key:

```shell
ssh-keygen -l -f ~/.ssh/id_ed25519.pub
```

*Do not paste a private key into a ticket, chat, shell history, or remote command. Replace a private key after suspected disclosure and remove its public key from every authorized account.*

### Connecting to a Remote Server

To connect to a remote server using SSH, follow these steps:

1. Obtain the **IP address** or domain name of the remote server you want to connect to.

2. Open a terminal or command prompt and use the following command to initiate an SSH connection:

```shell
ssh username@remote_server_ip
```

Replace `username` with your username on the remote server and `remote_server_ip` with the actual IP address or domain name of the server.

3. On a first connection, SSH presents a host-key warning. Compare the fingerprint with a trusted console, administrator record, or other independent source before accepting the key. The client stores accepted host keys in `~/.ssh/known_hosts`.

4. When prompted, enter your account password or the passphrase for the selected private key. Select a named key with the `-i` option:

```shell
ssh -i ~/.ssh/id_ed25519 username@remote_server_ip
```

5. If authentication succeeds, SSH opens the remote shell. A changed host key needs investigation before another login attempt. Do not bypass host-key checking to silence a warning.

To inspect fingerprints already stored for known hosts:

```shell
ssh-keygen -l -f ~/.ssh/known_hosts
```

### File Transfer with SSH

SSH also supports secure file transfer. **SCP** copies files over an SSH connection. **SFTP** provides an interactive file-transfer session.

1. Open a terminal or command prompt on your local machine.

2. Use the following command to copy a file from your local machine to the remote server:

```shell

scp /path/to/local/file username@remote_server_ip:/path/to/remote/location

```

Replace `/path/to/local/file` with the actual path and filename of the file on your local machine. Similarly, replace `username@remote_server_ip:/path/to/remote/location` with the appropriate username, server IP or remote file location.

Select a named private key with `-i` when the client configuration does not select the intended key:

```shell
scp -i ~/.ssh/id_ed25519 /path/to/local/file username@remote_server_ip:/path/to/remote/location
```

3. A first connection often presents a warning about the authenticity of the host. Verify the server's fingerprint before proceeding.

4. Enter your account password or the passphrase for the selected private key if prompted. The file will be copied through the SSH connection.

For an interactive SSH File Transfer Protocol (SFTP) session, use:

```shell
sftp username@remote_server_ip
```

Since OpenSSH 9.0, `scp` uses SFTP for transfers by default. The `-O` option selects the legacy SCP protocol for compatibility with a server or filename pattern requiring the legacy mode. Prefer the default mode unless a documented compatibility case requires `-O`.

### SSH Configuration

SSH configuration files customize client and server behavior. The main server file is usually `/etc/ssh/sshd_config`. The per-user client file is `~/.ssh/config`.

Create a client alias so repeated connections use the same reviewed settings:

```sshconfig
Host lab-server
    HostName remote_server_ip
    User username
    IdentityFile ~/.ssh/id_ed25519
    IdentitiesOnly yes
```

Connect with the alias:

```shell
ssh lab-server
```

`IdentityFile` selects the key. `IdentitiesOnly yes` limits authentication offers to configured identities. Protect the client configuration directory and file:

```shell
chmod 700 ~/.ssh
chmod 600 ~/.ssh/config
```

The OpenSSH daemon reads public keys from `~/.ssh/authorized_keys` by default. On the server, before applying a configuration change, test the daemon configuration syntax and host-key availability with:

```shell
sshd -t
```

Run this server-side check with the permissions required to read the server configuration and host keys. This check does not test a user's authorized key or prove public-key login works. Keep an existing session open while testing a new key. Set `PasswordAuthentication no` only after a separate public-key login succeeds and a recovery path exists.

| Configuration area | File or option | Review question |
|-------------------|----------------|-----------------|
| **Client alias** | `~/.ssh/config` | Does the alias point to the intended host and user? |
| **Client identity** | `IdentityFile` | Does the key belong to the intended account? |
| **Identity selection** | `IdentitiesOnly` | Will the client offer only the reviewed key? |
| **Server authorization** | `~/.ssh/authorized_keys` | Does each key have an owner and removal plan? |
| **Password fallback** | `PasswordAuthentication` | Is a tested recovery path available before a change? |

## Troubleshooting SSH

Start with the evaluated client configuration and verbose output. These checks expose wrong aliases, wrong users, unexpected keys, and host-key file paths without changing server settings:

```shell
ssh -G lab-server
ssh -vvv lab-server
```

If key authentication fails, check the following in order:

- **Host identity**: Compare the presented fingerprint with a trusted record.
- **Key pairing**: Compare the fingerprint of the local public key with the key installed for the remote account.
- **File permissions**: Keep `~/.ssh` private and keep `config`, private keys, and `authorized_keys` protected from other users.
- **Client selection**: Check `IdentityFile` and `IdentitiesOnly` in the evaluated configuration.
- **Server syntax**: Run `sshd -t` before reloading a changed server configuration.
- **Recovery path**: Keep a separate administrative session until a new login succeeds.

For a connection failure, separate the network check from the authentication check:

- **Name resolution**: Test the hostname with the operating system's DNS tools. Try the server IP only after confirming the address from a trusted source.
- **Port and firewall**: Use the server's configured SSH port. Confirm the server firewall permits the client network.
- **Connection refused**: Check whether the SSH daemon is running and listening on the expected address and port.
- **Connection timeout**: Check routing, security groups, host firewalls, and VPN access before changing keys.
- **Server logs**: Review the SSH daemon logs on the server for the rejected username, key, or policy.
- **Remote key permissions**: Confirm the account owns `~/.ssh`, `authorized_keys` has restrictive permissions, and the parent home directory permits SSH to read the path.

## Conclusion

SSH is a secure protocol for remote access and management of servers and computers. Its encryption, host-key checks, authentication methods, and file-transfer tools support administrators, developers, and other authorized users.

Start with a passphrase-protected key, verify the server fingerprint, use a per-host client alias, and keep a recovery session open during server changes. These steps give you a repeatable SSH workflow without treating encryption as a substitute for access control.

For the next step, read the [Linux hardening guide](/articles/dos-and-donts-for-hardening-linux/) for host-level controls. For repeatable administration, see [Ansible for beginners](/articles/ansible-for-beginners/) and its SSH-based connection workflow.

______

## Next steps

- Replace placeholder hostnames, usernames, and paths with values reviewed for your environment.
- Record host-key fingerprints and key ownership in your administration records.
- Test a second administrative login before changing password or firewall settings.
- Add SSH configuration review to your system hardening and automation process.

## References

- [SSH on Wikipedia](https://en.wikipedia.org/wiki/Secure_Shell)
- [SCP Documentation](https://man.openbsd.org/scp)
- [SSH Configuration File Documentation](https://man.openbsd.org/sshd_config)
- [OpenSSH `ssh-keygen(1)` manual](https://man.openbsd.org/ssh-keygen)
- [OpenSSH `ssh(1)` manual](https://man.openbsd.org/ssh)
- [OpenSSH `ssh_config(5)` manual](https://man.openbsd.org/ssh_config)
- [OpenSSH `sshd(8)` manual](https://man.openbsd.org/sshd)
- [OpenSSH release notes](https://www.openssh.org/releasenotes.html)
