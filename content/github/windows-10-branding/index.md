---
title: "Automated Branding for Windows Systems - Easily Control Desktop, Lock Screen, and More"
date: 2020-08-14T14:37:16-05:00
toc: true
draft: false
description: "Control desktop wallpaper, users avatar, lock screen, and OEM logo with ease on Windows 10 and Server systems using a partially automated script."
tags: ["Automation", "Branding", "Windows Branding", "Customization", "Windows Customization", "Windows 10", "Windows Server 2016", "Windows Server 2019", "Powershell", "Script", "Windows System Branding", "Desktop Wallpaper", "Users Avatar", "Windows Lock Screen", "OEM Logo", "Microsoft Security Compliance Toolkit 1.0", "Organization Branding", "System Customization", "IT Automation", "Security Compliance"]
---

# Setup branding on Windows 10 and Server 2016/2019 Systems

Many organizations have a need or want to control the branding of a Windows system. 
This includes the desktop wallpaper, the users avatar, the Windows lock screen, and sometimes the OEM Logo. 
In Windows 10, Windows Server 2016, and Windows Server 2019 this is not particularly easy. 
But, with the aide of the linked script, we can partially automate it and make the process much easier.

## Download the required files

**Download the required files from the [GitHub Repository](https://github.com/simeononsecurity/Windows-Branding-Script)**

## How to set up the branding files

- [X] Replace all images with your branding images
  - [X] OEM logo must be either 95x95 or 120x20 and in ".bmp" format
  - [X] Generate the User Image along with 32x32, 40x40, 48x48, 192x192 variants.
  - [X] Generate or copy user image for guest image.

## How to run the script
```
.\sos-copybranding.ps1
```

## This script utilizes the following tool:

- [Microsoft Security Compliance Toolkit 1.0 - LGPO](https://www.microsoft.com/en-us/download/details.aspx?id=55319)
