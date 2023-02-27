---
title: "Streamline Windows Updates with Automation using Chocolatey, PSWindowsUpdate, and Startup Scripts"
date: 2020-07-22T17:46:00-05:00
toc: true
draft: false
description: "Learn how to automate Windows updates with a single reboot and save valuable time for system administrators using Chocolatey, PSWindowsUpdate, and Startup Scripts."
tags: ["Automation", "Windows Updates", "Windows 10", "Powershell", "Script", "Chocolatey", "PSWindowsUpdate", "Startup Scripts", "System Administrators", "Windows Update Processes", "Local Group Policy Editor", "GP", "GPO", "Group Policy Objects", "Package Manager", "Consistency", "Centralized Management", "Security", "Software Management", "Microsoft Updates"]
---
# Automating Windows Updates with Chocolatey, PSWindowsUpdate, and Startup Scripts

In today's fast-paced business environment, time is of the essence for system administrators. Updating Windows machines, a critical aspect of systems administration, can be an extremely time-consuming task that can take up to a week, given enough systems. However, with some assistance from Chocolatey, PSWindowsUpdates, and Startup Scripts, it is now possible to roll out updates with as little as a single reboot of each machine, significantly reducing the amount of time required to perform updates.

## Streamlining Windows Updates with Automation

Windows updates are critical in maintaining the stability and security of Windows machines. Performing updates on a large number of machines can be a time-consuming task, especially for system administrators with limited resources. However, with the use of automation tools such as Chocolatey, PSWindowsUpdate, and Startup Scripts, this process can be streamlined to allow administrators to perform updates with minimal effort.

### Chocolatey

[Chocolatey](https://chocolatey.org/) is a package manager for Windows that can be used to automate the installation of software on Windows machines. It is similar to apt-get on Ubuntu or homebrew on macOS, and it can be used to install and manage a wide range of software packages. Chocolatey can be used to install packages silently, meaning that they can be installed without user intervention.

### PSWindowsUpdate

[PSWindowsUpdate](https://www.powershellgallery.com/packages/PSWindowsUpdate/2.0.0.4) is a PowerShell module that can be used to automate the installation of Windows updates. It provides cmdlets that can be used to install, uninstall, and list Windows updates. PSWindowsUpdate is a powerful tool that can be used to manage Windows updates on multiple machines, making it ideal for system administrators who need to manage large numbers of machines.

### Startup Scripts

[Startup Scripts](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/dn789190(v=ws.11)) are scripts that can be used to automate tasks that need to be performed when a machine starts up or shuts down. These scripts can be used to perform tasks such as installing software, configuring settings, and managing Windows updates.

## Automating Windows Updates with a Single Reboot

To automate Windows updates using Chocolatey, PSWindowsUpdate, and Startup Scripts, administrators can follow the step-by-step guide below.

### Setting Up the Shutdown Script
Download all supporting files from the [GitHub Repository](https://github.com/simeononsecurity/ChocoAutomateWindowsUpdates)

1. Open the Local Group Policy Editor by hitting **"Win + R"** and typing **"gpedit.msc"** followed by **"Ctrl + Shift + Enter"**.
2. Navigate to Computer **Configuration\Windows Settings\Scripts (Startup/Shutdown)**.
3. In the results pane, double-click Shutdown.
4. Select the PowerShell tab.
5. In the Shutdown Properties dialog box, click Add.
6. In the Script Name box, type the path to the script, or click Browse to search "*chocoautomatewindowsupdates.ps1*" in the Netlogon shared folder on the domain controller.
7. Reboot.

Now, all an administrator has to do is reboot the computer to perform Windows updates.

### Understanding the Script

The script used to automate Windows updates is titled "*chocoautomatewindowsupdates.ps1*". It performs the following tasks:

1. Installs Chocolatey package manager.
2. Enables a couple of preferred Chocolatey configuration changes.
3. Upgrades all installed Chocolatey packages.
4. Installs PSWindowsUpdate PowerShell module.
5. Adds Windows Update service manager.
6. Installs all available Windows updates.
7. Installs any missing drivers or updates required by previously installed updates.

### Benefits of Automating Windows Updates

Automating Windows updates using Chocolatey, PSWindowsUpdate, and Startup Scripts has several benefits for system administrators. These benefits include:

- **Time-saving**: Automating Windows updates significantly reduces the amount of time required to perform updates. Administrators no longer have to manually install updates on each machine.
- **Consistency**: Automating Windows updates ensures that updates are installed consistently across all machines. This reduces the likelihood of errors and security vulnerabilities.
- **Centralized management**: Automating Windows updates allows administrators to manage updates from a central location, making it easier to keep track of which updates have been installed and which machines need updates.
- **Increased security**: Automating Windows updates ensures that machines are kept up to date with the latest security patches, reducing the risk of security breaches.

### Conclusion

Automating Windows updates using Chocolatey, PSWindowsUpdate, and Startup Scripts is a powerful tool that can save system administrators a lot of time and effort. It allows updates to be installed consistently and efficiently, ensuring that machines are up to date with the latest security patches. By following the steps outlined in this tutorial, administrators can automate Windows updates with just a single reboot, making the process of updating Windows machines much faster and easier.
