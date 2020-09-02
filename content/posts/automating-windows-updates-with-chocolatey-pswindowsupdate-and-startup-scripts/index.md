---
title: "Automating Windows Updates with Chocolatey, PSWindowsUpdate, and Startup Scripts"
date: 2020-07-22T17:46:00-05:00
draft: false
tags: ['Automation', 'How To Automate Windows Updates', 'Windows Updates', 'Windows 10', 'Powershell', 'Script']
---

# Automating Windows Updates with Chocolatey, PSWindowsUpdate, and Startup Scripts

Download all supporting files from the [GitHub Repository](https://github.com/simeononsecurity/ChocoAutomateWindowsUpdates)

     In today's modern workplace environment, system administrators constantly are battling for time. Rolling out the latest Windows updates can be extremely time consuming taking up to a week given enough systems.
Along with some assistance from Chocolatey, PSWindowsUpdates, and Startup Scripts, Systems Administrators can roll out update with as little as a single reboot of each machine.

## How to set up the shutdown script
We have chosen to set it up as a shutdown script to avoid having to reboot twice.
We will be following the tutorial from [Microsoft](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/dn789190(v=ws.11)) to do this.

In the windows gui perform the following steps:

1.) Open the Local Group Policy Editor by hitting **"Win + R"** and typing **"gpedit.msc"** followed by **"Ctrl + Shift + Enter"**

2.) Navigate to Computer **Configuration\Windows Settings\Scripts (Startup/Shutdown).**

3.) In the results pane, double-click Shutdown.

4.) Select the powershell tab

5.) In the Shutdown Properties dialog box, click Add.

6.) In the Script Name box, type the path to the script, or click Browse to search "*chocoautomatewindowsupdates.ps1*" in the Netlogon shared folder on the domain controller.

7.) Reboot

8.) Profit?

Now in the future, all an administrator has to do is reboot the computer to perform windows updates. 

The same steps can be performed in GPO to acomplish the same thing on multiple Windows machines at the same time.


## How the script works
**The script we will be working with today titled "*chocoautomatewindowsupdates.ps1*":**

```
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
choco feature enable -n=allowGlobalConfirmation
choco feature enable -n useFipsCompliantChecksums
choco upgrade all
choco install pswindowsupdate
Add-WUServiceManager -ServiceID 7971f918-a847-4430-9279-4a52d1efe18d -Confirm:$false
Install-WindowsUpdate -MicrosoftUpdate -AcceptAll 
Get-WuInstall -AcceptAll -IgnoreReboot
```

**From [Chocolatey](https://chocolatey.org/install), the script below installs the Chocolatey package manager:**
```
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
```

**Folowed by a couple prefered Chocolatey configuration changes;**
``` 
choco feature enable -n=allowGlobalConfirmation
choco feature enable -n useFipsCompliantChecksums
choco upgrade all
```

**Lastly we will install and run [PSWindowsUpdates](https://www.powershellgallery.com/packages/PSWindowsUpdate/2.0.0.4) to install all of the available windows updates.**
```
choco install pswindowsupdate
Add-WUServiceManager -ServiceID 7971f918-a847-4430-9279-4a52d1efe18d -Confirm:$false
Install-WindowsUpdate -MicrosoftUpdate -AcceptAll 
Get-WuInstall -AcceptAll -IgnoreReboot
```