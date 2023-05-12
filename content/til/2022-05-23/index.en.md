---

title: "Today I Learned how to Create Chocolatey Packages"
date: 2022-05-23
toc: true
draft: false
description: "Today I Learned more about Ansible conditionals and variable management"
tags: ['Automation', 'Powershell', 'Chocolatey Package Manager', 'Chocolatey', 'Choco', 'cinstall', 'Nupkg', 'Nethor', 'Windows Package Managers', 'IAC', 'Infrastructure As Code']
---

**What SimeonOnSecurity learned about and found interesting today**

Today, SimeonOnSecurity learned about the process of creating packages for the Chocolatey Package Manager. Chocolatey is a package manager for Windows that makes it easy to install, upgrade, and manage applications and tools. By creating packages, SimeonOnSecurity can automate the installation of software and share packages with others in the community.

SimeonOnSecurity created and updated two repositories on GitHub related to creating Chocolatey packages. The first repository, simeononsecurity/Chocolatey-Nethor, is a package for Nethor. The second repository, simeononsecurity/chocolateypackages, is a collection of packages created by SimeonOnSecurity for various applications and tools.

To create a package, SimeonOnSecurity used the Nuspec file format, which provides metadata about the package and its contents. The package creation process also involved using functions such as Install-ChocolateyInstallPackage and Install-ChocolateyPackage to specify the software to be installed and any necessary dependencies.

SimeonOnSecurity also reviewed several learning resources, including the official Chocolatey documentation and a tutorial by Top Bug Net, to gain a deeper understanding of the process of creating and publishing Chocolatey packages.

Overall, SimeonOnSecurity's learning experience today provided a comprehensive understanding of the process of creating packages for the Chocolatey Package Manager, making it easier to automate software installations and share packages with others in the community.

## Repos Created/Updated:
- [simeononsecurity/Chocolatey-Nethor](https://github.com/simeononsecurity/Chocolatey-Nethor)
- [simeononsecurity/chocolateypackages](https://github.com/simeononsecurity/chocolateypackages)

## Learning resources:
- [Chocolatey - Create Packages](https://docs.chocolatey.org/en-us/create/create-packages#nuspec)
- [Chocolatey - Install-ChocolateyInstallPackage](https://docs.chocolatey.org/en-us/create/functions/install-chocolateyinstallpackage)
- [Chocolatey - Install-ChocolateyPackage](https://docs.chocolatey.org/en-us/create/functions/install-chocolateypackage)
- [Top Bug Net - Create and Publish Chocolatey Packages](https://www.topbug.net/blog/2012/07/02/a-simple-tutorial-create-and-publish-chocolatey-packages/)