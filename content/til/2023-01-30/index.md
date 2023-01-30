---

title: "Today I Learned how to Create Chocolatey Packages"
date: 2023-01-30
toc: true
draft: false
description: "Today I Learned about Custom Windows Image Creation, Sysprep, and Generalizing"
tags: ['Sysprep', 'NTLite', 'Generalization', 'Custom Images', 'Custom Windows Images', 'Windows 11', 'Debloat', 'Customization']
---
# Today I learned / Read About...
**What SimeonOnSecurity learned about and found interesting today**

Today, SimeonOnSecurity learned about the process of capturing and applying Windows 10 images using DISM, a command-line tool used to manage Windows images. To capture an image, one can use the Sysprep tool to generalize the installation, which removes hardware-specific information and prepares the image for deployment on multiple devices.

SimeonOnSecurity was introduced to various resources that provide information on capturing and applying Windows images, including Microsoft's Learn website and the WinCustom repository on GitHub. The Microsoft resources cover the basics of capturing and applying a Windows image using a single .WIM file, creating bootable Windows PE media, and generalizing a Windows installation with Sysprep.

Additionally, SimeonOnSecurity learned about NTLite, a software that allows for customization and optimization of Windows images. NTLite can be used to remove unnecessary components from a Windows image, saving disk space and improving performance.

Overall, SimeonOnSecurity's research today provided a comprehensive understanding of the process of capturing and applying Windows images.

## Repos Created/Updated:
- None / N/A

## Learning Resources:
- [Learn How to Sysprep Capture Windows 10 Image using DISM](https://www.anoopcnair.com/sysprep-capture-windows-10-image-using-dism/)
- [Microsoft - Capture and apply a Windows image using a single .WIM file](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/capture-and-apply-windows-using-a-single-wim?view=windows-11)
- [Microsoft - Create bootable Windows PE media](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/winpe-create-usb-bootable-drive?view=windows-11)
- [Microsoft - Sysprep (Generalize) a Windows installation](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/sysprep--generalize--a-windows-installation?view=windows-11)
- [WinTenDev/WinCustom](https://github.com/WinTenDev/WinCustom)

## Software Discussed and/or Utilized:
- [NTLite](https://www.ntlite.com/)