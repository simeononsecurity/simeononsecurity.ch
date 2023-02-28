---
title: "Essential Do's and Don'ts for Hardening Your Linux System"
date: 2023-02-28
toc: true
draft: false
description: "Learn the essential do's and don'ts for hardening your Linux system, including updating, using firewalls, enabling SELinux or AppArmor, configuring password policies, and monitoring system logs."
tags: ["Linux security", "system hardening", "firewall", "SELinux", "AppArmor", "password policy", "system updates", "system logs", "security modules", "access control policies", "cybersecurity", "system security", "network security", "vulnerability management", "security best practices", "IT security", "information security", "software updates", "root access", "password manager"]
cover: "/img/cover/A_cartoon_lock_holding_a_shield_with_the_word_Linux_on_it.png"
coverAlt: "A cartoon lock holding a shield with the word "Linux" on it, while an arrow bounces off the shield."
coverCaption: ""
---


Linux is a popular operating system used by individuals and businesses alike. While it is often considered more secure than other operating systems due to its open-source nature, it still requires proper hardening to ensure the safety of the system and the data it holds. In this article, we will go over some general hardening do's and don'ts that can help keep your Linux system secure.

## Do's:

### Keep your system updated

Keeping your [Linux](https://simeononsecurity.ch/articles/how-do-i-learn-linux/) system up-to-date is crucial for maintaining its security. Regular updates help fix security vulnerabilities and bugs, ensuring that your system remains secure against potential attacks. Here are some examples of how to update your Linux system using the **apt-get** or **yum** package manager:

#### Updating Ubuntu using apt-get

To update your Ubuntu system using **apt-get**, open a terminal window and type:
```bash
sudo apt-get update
```

This will download the latest package lists from the Ubuntu package repositories. Once this command completes, you can install any available updates using the following command:

```bash
sudo apt-get upgrade

```

This will download and install any available updates for your system.

### Updating CentOS using yum

To update your CentOS system using **yum**, open a terminal window and type:

```bash
sudo yum update
```

This will download and install any available updates for your system. You may also want to use the following command to clean up any old or unused packages:

```bash
sudo yum autoremove
```

This will remove any packages that are no longer needed on your system.

Remember to regularly check for and install updates on your Linux system to ensure its security and stability.


### Use a firewall

A firewall is an essential security measure for any Linux system, as it helps protect against unauthorized access and other cyber threats. Here's how to use the **ufw** firewall on your Linux system:

#### Installing and enabling ufw for Ubuntu Based Systems

To install and enable **ufw**, open a terminal window and type:

```bash
sudo apt install ufw -y
sudo ufw allow ssh
sudo ufw enable
```

To allow incoming HTTP traffic (port 80):

```bash
sudo ufw allow http
```

To block incoming traffic from a specific IP address:

```bash
sudo ufw deny from <ip_address>
```

To delete a rule:
```bash
sudo ufw delete <rule_number>
```

You can view the current **ufw** rules by typing:

```bash
sudo ufw status
```


This will display the current rules and their status.

Remember to regularly review and update your **ufw** rules to ensure that your system is protected against potential threats.


#### Installing and enabling firewalld for CentOS Based Systems

To install and enable the default firewall on CentOS, which is **firewalld**, you can use the following commands:

```bash
sudo yum install firewalld
sudo systemctl enable firewalld
sudo systemctl start firewalld
```

This will install **firewalld** and enable it on your system.

#### Configuring firewalld rules for CentOS Based Systems

Once **firewalld** is enabled, you can configure its rules to allow or block incoming and outgoing traffic. Here are some examples:

To allow incoming SSH traffic (port 22):

```bash
sudo firewall-cmd --permanent --add-service=ssh
sudo firewall-cmd --reload
```

To allow incoming HTTP traffic (port 80):

```bash
sudo firewall-cmd --permanent --add-service=http
sudo firewall-cmd --reload
```

To block incoming traffic from a specific IP address:

```bash
sudo firewall-cmd --permanent --add-rich-rule='rule family="ipv4" source address="<ip_address>" reject'
sudo firewall-cmd --reload
```

To delete a rule:

```bash
sudo firewall-cmd --permanent --remove-<type>=<rule>
sudo firewall-cmd --reload
```

You can view the current **firewalld** rules by typing:

```bash
sudo firewall-cmd --list-all
```

This will display the current rules and their status.

Remember to regularly review and update your **firewalld** rules to ensure that your system

### Enable SELinux or AppArmor

SELinux (Security-Enhanced Linux) and AppArmor are two security modules that can be used to enforce mandatory access control policies in Linux systems. By default, most modern Linux distributions come with SELinux or AppArmor installed, and they can be enabled and configured to enhance the security of your system.

#### Enabling SELinux for CentOS Based Systems

To check if SELinux is enabled on your system, run the following command:

```bash
sestatus
```

If SELinux is not installed, you can install it using the following command:

```bash
sudo yum install selinux-policy selinux-policy-targeted
```

To enable SELinux, you need to edit the **/etc/selinux/config** file and set the **SELINUX** variable to **enforcing**:

```bash
sudo nano /etc/selinux/config
```
**Change SELINUX=enforcing**
```
SELINUX=enforcing
```

Save and exit the file, using CTRL+X and Y then enter, then reboot your system.

#### Enabling AppArmor for Ubuntu Based Systems

To check if AppArmor is enabled on your system, run the following command:
```bash
sudo apparmor_status
```


If AppArmor is not installed, you can install it using the following command:
```bash
sudo apt-get install apparmor
```

To enable AppArmor, you need to edit the **/etc/default/grub** file and add the **security=apparmor** parameter to the **GRUB_CMDLINE_LINUX** variable:

```bash
sudo nano /etc/default/grub
```
**Add security=apparmor**
```bash
GRUB_CMDLINE_LINUX="... security=apparmor"
```

Save and exit the file, using CTRL+X and Y then enter, then run the following command to update your system's bootloader configuration:

```bash
sudo update-grub
```

Finally, reboot your system.

Once SELinux or AppArmor is enabled, you can configure their policies to restrict the privileges of processes and limit their access to system resources. This can help minimize the potential impact of a successful attack and enhance the overall security of your system.


### Configure password policies

Configuring password policies is an important step in hardening your Linux system's security. By enforcing strong password requirements, you can ensure that user accounts are secure and protected against potential attacks. Here's how to configure password policies on your Linux system:

#### Configuring password policies on Ubuntu

To configure password policies on Ubuntu, you can use the **pam_pwquality** module. This module provides a set of password strength checks that can be used to enforce password policies. To install the **pam_pwquality** module, open a terminal window and type:

```bash
sudo apt-get install libpam-pwquality
```

Once the module is installed, you can configure its settings by editing the **/etc/pam.d/common-password** file. For example, to enforce a minimum password length of 8 characters and require at least one uppercase letter, one lowercase letter, one digit, and one special character, you can add the following line to the file:

```bash
password requisite pam_pwquality.so minlen=8 ucredit=-1 lcredit=-1 dcredit=-1 ocredit=-1
```

You can also configure other settings, such as the maximum password age, by adding lines to the file.

#### Configuring password policies on CentOS

To configure password policies on CentOS, you can use the **authconfig** tool. This tool provides a set of options that can be used to configure password policies. For example, to enforce a minimum password length of 8 characters and require at least one uppercase letter, one lowercase letter, one digit, and one special character, you can use the following command:

```bash
sudo authconfig --passalgo=sha512 --update --enablereqlower --enablerequpper --enablereqdigit --enablereqother --passminlen=8
```

This will update the system's **/etc/pam.d/system-auth** and **/etc/pam.d/password-auth** files to enforce the specified password policies.

Remember to regularly review and update your password policies to ensure that they remain effective against potential attacks.


### Monitor your system logs

Monitoring your system logs is an important aspect of maintaining the security of your Linux system. System logs record system activity, such as failed login attempts, errors, and other important events, and can provide valuable insights into potential security threats or other issues that require attention. Here's how to monitor your system logs:

#### Using the journalctl command

On most modern Linux distributions, you can use the **journalctl** command to view system logs. This command provides a variety of options that can be used to filter and search log entries.

To view all log entries, simply run the following command:

```bash
sudo journalctl
```

This will display all log entries, with the most recent entries at the bottom.

To filter log entries by a specific unit, such as a service or a process, you can use the **-u** option followed by the unit name. For example, to view log entries for the **sshd** service, you can run the following command:
```bash
sudo journalctl -u sshd
```


To filter log entries by a specific time range, you can use the **--since** and **--until** options followed by a timestamp or time range. For example, to view log entries from the last hour, you can run the following command:

```bash
sudo journalctl --since "1 hour ago"
```

#### Using a log management tool

For larger or more complex systems, it may be useful to use a log management tool to collect and analyze system logs. Log management tools can provide advanced features, such as real-time log monitoring, log aggregation, and log analysis, and can help you identify and respond to potential security threats more efficiently.

Examples of log management tools for Linux include:

- **Logwatch**: a simple log analysis tool that provides daily email summaries of system logs
- **Logrotate**: a tool that automatically rotates and compresses log files to conserve disk space
- **ELK stack**: a popular open-source log management tool that combines Elasticsearch, Logstash, and Kibana to provide real-time log monitoring and analysis capabilities

Remember to regularly review and analyze your system logs to detect and respond to potential security threats in a timely manner.

______

## Don'ts:

### Use weak passwords

Using weak passwords is a common mistake that can leave your Linux system vulnerable to attacks. Attackers can use tools to guess passwords that are based on common words, names, or dates. It is important to use strong and unique passwords that are not easily guessable. 

You can create strong passwords by using a combination of uppercase and lowercase letters, numbers, and special characters. It is also a good practice to use a [password manager](https://simeononsecurity.ch/articles/bitwarden-and-keepassxc-vs-the-rest/) to generate and store complex passwords securely. [Password managers](https://simeononsecurity.ch/articles/bitwarden-and-keepassxc-vs-the-rest/) can also help you to remember your passwords and avoid using the same password for multiple accounts.

### Allow root SSH access

Allowing root SSH access is a security risk that can give attackers complete control over your Linux system. Instead, you should use a non-root user account to log in to your system and then elevate privileges using the **sudo** command. This helps to limit the potential impact of an attack by restricting the privileges of user accounts.

### Install unnecessary software

Installing unnecessary software can increase the attack surface of your Linux system, making it more vulnerable to attacks. It is important to only install software that is necessary for your system and remove any unnecessary software. This helps to reduce the number of potential vulnerabilities on your system and minimize the risk of a successful attack.

### Use outdated software

Using outdated software can leave your system vulnerable to attacks that exploit known vulnerabilities. It is important to always use the latest version of software and regularly update it to ensure security. This helps to patch known vulnerabilities and protect your system against potential attacks.

______

## Conclusion

In conclusion, hardening your Linux system is critical to ensure its security and protect the data it holds. By following the do's and don'ts outlined in this article, you can take important steps to secure your system and reduce the risk of cyber threats. Remember to always keep your system up-to-date, use a firewall, configure password policies, and monitor system logs. Avoid using weak passwords, disabling automatic updates, allowing root SSH access, installing unnecessary software, and using outdated software. With these best practices in mind, you can ensure that your Linux system remains secure and protected.

## References:

- [The Center for Internet Security's Linux Hardening Guide](https://www.cisecurity.org/cis-hardened-images/)
- [Red Hat Enterprise Linux Security Guide](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/security_guide/index)
- [Ubuntu Security Documentation](https://ubuntu.com/security)
- [Linux Security Wiki](https://en.wikibooks.org/wiki/Linux_Security)
