---
title: "Enhancing Oracle JRE 8 Security: Best Practices, STIGs, and Configuration Examples"
date: 2023-10-29
toc: true
draft: false
description: "Discover key practices for securing Oracle JRE 8 with code examples and best practices. Strengthen your system's defense against vulnerabilities."
genre: ["Technology", "Cybersecurity", "Software Development", "Computer Science", "Programming", "Security", "Java Programming", "Software Security", "IT Management", "System Administration"]
tags: ["Oracle JRE 8", "Java Security", "Code Examples", "Software Security", "STIG", "System Hardening", "Secure Configuration", "Cybersecurity", "Vulnerability Management", "System Updates", "Deployment Configuration", "Java Web Start", "Online Certificate Validation", "System-wide Configuration", "Secure Execution Control", "Security Best Practices", "System Security Measures", "Security Guidelines", "IT Security", "Linux Security", "Windows Security", "Security Automation", "IT Compliance", "Security Implementation", "IT Best Practices", "IT Governance", "Security Solutions", "Software Updates", "Java Deployment", "Security Strategies"]
cover: "/img/cover/enhanced-jre-security.png"
coverAlt: "An illustration depicting a locked JRE symbolizing enhanced security."
coverCaption: "Strengthen Your JRE Security"
---

**Secure Configuration Guide for Oracle JRE 8: Best Practices and Code Examples**

In today's interconnected world, **securing software components** like the **Oracle Java Runtime Environment (JRE)** is **paramount**. The Oracle JRE is integral for **running Java applications**, yet **default configurations** can expose systems to vulnerabilities. This guide presents **actionable steps** to **secure Oracle JRE 8**, offering **code examples** and insights for each **finding** identified in the **Security Technical Implementation Guide (STIG)**. Whether on **Windows or Linux**, by following these guidelines, you'll **bolster the security** of your system and applications.

## Introduction

The **Oracle JRE**, an **indispensable tool for executing Java applications and applets**, comes with **default settings** that may compromise system security. The **Security Technical Implementation Guide (STIG)** identifies **key vulnerabilities** and provides **solutions** for **Oracle JRE 8 users**. To **enhance your understanding** and implementation of these solutions, let's delve into **each finding**, their importance, and **practical code examples**.
______

## Automated JRE STIG Script
**SimeonOnSecurity** has developed an [JRE STIG Script](https://github.com/simeononsecurity/Oracle-JRE-8-STIG-Script/tree/master) you can use. **Check it out with the link above**.

______
## Oracle JAVA JRE8 STIG

### Keeping Oracle JRE Up to Date (V-66967)

**Ensuring the latest version of Oracle JRE is in use** is a cornerstone of system security. Regular updates address vulnerabilities and enhance protection. An automated update script can streamline this process, ensuring a consistent and secure environment.

#### Linux

```bash
#!/bin/bash

if [[ $(java -version 2>&1 | grep "1.8") ]]; then
    echo "Java version is Oracle JRE 8"
    latest_version=$(curl -s https://www.oracle.com/java/technologies/javase8-downloads.html | grep -oP 'JRE-8u\d+' | sort -u | tail -n 1)
    current_version=$(java -version 2>&1 | awk -F '"' '/version/ {print $2}')
    
    if [[ "$latest_version" != "$current_version" ]]; then
        echo "Updating Java..."
        # Download and install the latest version
        # Add your installation commands here
    else
        echo "Java is up to date."
    fi
else
    echo "Java version is not Oracle JRE 8."
fi
```

#### Linux using Ansible
```yml
---
- name: Install Linux Oracle JRE8 if available
  block:
    - name: Add PPA repository
      ansible.builtin.apt_repository:
        repo: "ppa:webupd8team/java"
        state: present
      when: package_facts.ansible_facts.package_mgr == "apt"
    - name: Install Oracle JRE8 using package manager (apt)
      ansible.builtin.package:
        name: 
            - "oracle-java8-installer"
            - "default-jre"
            - "default-jdk"
        state: latest
        update_cache: yes
      when: package_facts.ansible_facts.package_mgr == "apt"
```

#### Windows with Chocolatey
```powershell
### install chocolatey
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

### Install and Update Java
choco install -y jre8
choco update -y jre8
```

#### Windows using Ansible

```yml
---
- name: Update Oracle JRE on Windows using Chocolatey
  hosts: windows_hosts
  tasks:
    - name: Install Oracle JRE using Chocolatey
      chocolatey.chocolatey.win_chocolatey:
        name: jre8
        state: latest
```
______

### Creating deployment.properties (V-66943)
For **customized Java Runtime Environment configuration**, it's essential to have a `deployment.properties` file. If it doesn't exist, create one in a system-wide path for both Windows and Linux:

- **Windows**: `C:\Windows\Sun\Java\Deployment\` or `C:\Program Files\Java\jre1.8.x_x\lib`
- **Linux**: `/usr/lib/jvm/jre-1.8.x_x/lib`

See an [example of a `deployment.properties`](https://github.com/simeononsecurity/Oracle-JRE-8-STIG-Script/blob/master/Files/deployment.properties) file.

### Configuring deployment.config (V-66941)
For effective **management of Java deployment properties**, configure the `deployment.config` file. Set the path to the deployment.properties file in a system-wide location:
```java
deployment.system.config=file:///path/to/deployment.properties
deployment.system.config.mandatory=true
```

See an [example of a `deployment.config`](https://github.com/simeononsecurity/Oracle-JRE-8-STIG-Script/blob/master/Files/deployment.config) file.

### Using an Accepted Sites List (V-66957)
An **accepted sites list** limits software execution to authorized sources, minimizing potential risks. Implement this by creating an `exception.sites` file and listing approved sites:

1. Create a new file named exception.sites in the `C:\Windows\Sun\Java\Deployment\` directory on Windows or `/usr/lib/jvm/jre-1.8.x_x/lib/security` on Linux.
2. Add each authorized site on a new line.
    ```ini
    https://example.com
    https://simeononsecurity.com
    ```

See an example of a known [working configuration for `exception.sites`](https://github.com/simeononsecurity/Oracle-JRE-8-STIG-Script/blob/master/Files/exception.sites).

______

### Implementing Authorized Sites Management (V-66959)

Implementing an authorized sites list through the use of an `exception.sites` file is crucial. This **whitelist-based approach allows only authorized software to execute**, effectively limiting the number of applications that can run, thereby reducing risk.

```java
deployment.user.security.exception.sites=C:/Windows/Java/Deployment/exception.sites
```
______

### Allowing Java Web Start Applications (V-66947)
**Java Web Start (JWS) applications** play a pivotal role in the modern computing landscape. To grant permission for these applications, create a `deployment.properties` file and insert the following:
```java
deployment.webjava.enabled=true
```
______

### Preventing Download of Prohibited Mobile Code (V-66955)
Guarding against **malicious mobile code download**s is crucial. Configure your `deployment.properties` file to implement this security measure:
```java
deployment.security.askgrantdialog.notinca=true
```
______

### Restricting Execution of Untrusted Signed Content (V-66951)
Enforcing **strict execution control for signed content** prevents potential security breaches. Use this property in your `deployment.properties` file:

```java
deployment.security.sandbox.awtwarningwindow=true
```
______

### Enabling Online Certificate Validation (V-66953)
Enhance **certificate validation security** by enabling online certificate validation. Modify your `deployment.properties` file with:

```java
deployment.security.validation.ocsp=true
```
______

### Enforcing Publisher Certificate Revocation Checks (V-66723)

To bolster the security of your Oracle JRE 8 environment, **lock the option to enable users to check publisher certificates for revocation**. Revoked certificates can arise due to improper issuance, certificate compromise, or policy violations. By preventing the use of compromised certificates, you enhance the integrity of your system.

In your `deployment.properties` file, add the following line:
```java
deployment.security.revocation.check=ocsp,crl
```
______

### Implementing Authorized Sites Management (V-66959)

Implementing an authorized sites list through the use of an `exception.sites` file is crucial. This **whitelist-based approach allows only authorized software to execute**, effectively limiting the number of applications that can run, thereby reducing risk.

In your `deployment.properties` file, add the following line:
```java
deployment.user.security.exception.sites=C:/Windows/Java/Deployment/exception.sites
```

______

### Disabling Execution from Untrusted Authorities (V-66949)

Enhance your security posture by **disabling the dialog that grants permissions to execute signed content from untrusted authorities**. This step prevents even signed applets from potentially malicious sources from executing.

In your `deployment.properties` file, add the following line:
```java
deployment.security.sandbox.jnlp.enhanced=true
deployment.security.sandbox.jnlp.enhanced.locked
```

______

### Controlled Execution of Mobile Code (V-66963)

**Prompting users for action prior to executing mobile code** is essential for preventing unintended execution of potentially harmful code. This added layer of protection ensures that users are aware of and can control the execution process.

```java
deployment.security.askprompt=false
```

______

### Enabling Publisher Certificate Revocation Checks (V-66961)

Enable users to check the revocation status of publisher certificates to prevent the use of compromised certificates. A **valid certificate revocation list (CRL) helps maintain the integrity of your Java environment**.

```java
deployment.security.validation.ocsp=true
deployment.security.validation.ocsp.locked
deployment.security.validation.crl=true
deployment.security.validation.crl.locked
```

______

### Removing Previous Versions (V-66965)

**Enhance system security by removing previous versions** of Oracle JRE 8 when installing the latest version. By keeping only the latest version, you prevent potential exploitation of known vulnerabilities.

```
# Manual removal of previous versions required
```

______

### Configuring deployment.config (V-66939)

**Proper configuration of the `deployment.config` file is vital** for effective management of Java deployment properties. This file specifies the location and attributes of the `deployment.properties` file, ensuring accurate configuration.

______

### Defaulting to Secure Settings (V-66945)

Enhance your system's security posture by **configuring Oracle JRE 8 to default to the most secure built-in settings**. By requiring applications to be signed with valid certificates and include specific permissions, you reduce the likelihood of security breaches.

```
# Configuration through Java Control Panel settings
```
______

## Conclusion
Protecting your systems against vulnerabilities is an ongoing endeavor. By following these actionable guidelines and implementing code examples for securing Oracle JRE 8, you'll significantly reduce the risk of potential breaches. Keep in mind that regular updates, controlled execution, and authorized sites are key components of a robust security strategy.

______

## References

- [Oracle Java SE Downloads](https://www.oracle.com/java/technologies/javase-downloads.html)
- [Oracle JRE Documentation](https://docs.oracle.com/en/java/javase/index.html)
- [Oracle JRE8 Deploy Properties](https://docs.oracle.com/javase/8/docs/technotes/guides/deploy/properties.html)
- [STIG Overview](https://public.cyber.mil/stigs/downloads/)
- [Stigviewer.com JRE8 STIG Overview](https://www.stigviewer.com/stig/java_runtime_environment_jre_version_8_windows/)
- [SimeonOnSecurity - JRE8 STIG Script](https://github.com/simeononsecurity/Oracle-JRE-8-STIG-Script/tree/master)
