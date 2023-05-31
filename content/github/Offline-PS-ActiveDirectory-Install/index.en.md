---
title: "Offline Installation of RSAT ActiveDirectory PowerShell Module for Windows 10"
date: 2020-12-16
draft: false
toc: true
description: "Learn how to install the RSAT ActiveDirectory PowerShell module offline on Windows 10 using a simple script."
tags: ["Remote Server Administration Toolkit", "PowerShell RSAT ActiveDirectory Module", "Windows 10", "Offline Installer", "PowerShell Script", "PowerShell Module", "ActiveDirectory", "Windows", "Offline", "Install", "Server", "Administration", "Toolkit", "Scripting", "Module", "Windows Server", "PowerShell Core", "Windows PowerShell", "Microsoft", "IT Administration", "Active Directory management", "Windows 10 administration", "PowerShell commands", "offline installation", "IT tools", "AD management", "scripting", "RSAT tools", "Windows system administration", "install active directory powershell module windows 10", "active directory module for windows powershell", "import module active directory windows 10", "powershell active directory module install"]
---

**Install Active Directory PowerShell Module on Windows 10**

Are you looking to manage Active Directory on your Windows 10 machine? The Active Directory PowerShell module provides powerful tools for managing Active Directory objects using PowerShell commands. In this article, we will guide you through the process of installing the Active Directory PowerShell module on Windows 10.

## Prerequisites

Before we begin, make sure you meet the following requirements:

- Windows 10 operating system
- Administrative privileges on your machine

## **Downloading the Module**

To install the Active Directory PowerShell module, you can use the **Remote Server Administration Toolkit (RSAT)**. Follow the steps below to download and install the module:

1. Visit the [Microsoft Download Center](https://www.microsoft.com/en-us/download/details.aspx?id=45520) and search for "Remote Server Administration Tools for Windows 10".
2. Select the version that matches your system architecture (32-bit or 64-bit) and click **Download**.
3. Once the download is complete, open the installation file and follow the on-screen instructions to install the RSAT tools.

## **Installing the Module Offline**

In some cases, you may need to install the Active Directory PowerShell module offline. Here's how you can do it:

1. [Download the Offline-PS-ActiveDirectory-Install script](https://github.com/simeononsecurity/Offine-PS-ActiveDirectory-Install/archive/master.zip).
2. Extract the downloaded zip file to a location on your machine.
3. Open a PowerShell terminal with administrative privileges.
4. Navigate to the extracted folder using the `cd` command.
5. Run the following command to execute the installation script:
```powershell
.\sos-offlinepsadinstall.ps1
```
The script will perform the following actions:

- Copy the necessary files and modules to the appropriate locations on your system.
- Unblock the new PowerShell modules and DLLs.
- Import the Active Directory module and DLLs using the `Import-Module` command.
- Once the script execution is complete, you will have the Active Directory PowerShell module installed on your Windows 10 machine.

**Verifying the Installation**

To verify that the Active Directory PowerShell module is installed correctly, follow these steps:

1. Open a PowerShell terminal.
2. Run the command `Import-Module ActiveDirectory`.
3. If no errors are displayed, the module is successfully installed.

**Conclusion**

By following the steps outlined in this article, you can easily install the Active Directory PowerShell module on your Windows 10 machine. This module enables you to manage Active Directory objects efficiently using PowerShell commands, providing a powerful tool for IT administration.

Make sure to explore the various capabilities offered by the Active Directory PowerShell module and leverage its features to streamline your Active Directory management tasks.

**References**

- [Microsoft Download Center](https://www.microsoft.com/en-us/download/details.aspx?id=45520)
- [Offline-PS-ActiveDirectory-Install Script](https://github.com/simeononsecurity/Offine-PS-ActiveDirectory-Install/archive/master.zip)
