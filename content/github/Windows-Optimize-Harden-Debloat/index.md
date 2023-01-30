---
title: "Optimize and Debloat Windows 10 Deployments"
date: 2020-12-29
toc: true
draft: false
description: "For those who seek to minimize their Windows 10 installs."
tags: ['Automation', 'Windows Updates', 'Windows 10 Optimizations', 'Windows 10 Debloat', 'Windows 10', 'Powershell', 'Script']
---
# Optimize, Harden, and Debloat Windows 10 and Windows 11 Deployments




## Introduction:



Windows 10 and Windows 11 are invasive and insecure operating system out of the box.

Organizations like [PrivacyTools.io](https://PrivacyTools.io), [Microsoft](https://microsoft.com), [Cyber.mil](https://public.cyber.mil), the [Department of Defense](https://dod.gov), and the [National Security Agency](https://www.nsa.gov/) have recommended configuration changes to lockdown, harden, and secure the operating system. These changes cover a wide range of mitigations including blocking telemetry, macros, removing bloatware, and preventing many digital and physical attacks on a system. This script aims to automate the configurations recommended by those organizations.



## Notes, Warnings, and Considerations:



**WARNING:**



This script should work for most, if not all, systems without issue. While [@SimeonOnSecurity](https://github.com/simeononsecurity) creates, reviews, and tests each repo intensively, we can not test every possible configuration nor does [@SimeonOnSecurity](https://github.com/simeononsecurity) take any responsibility for breaking your system. If something goes wrong, be prepared to submit an [issue](../../issues).



- This script is designed for operation in primarily **Personal Use** environments. With that in mind, certain enterprise configuration settings are not implemented. This script is not designed to bring a system to 100% compliance. Rather it should be used as a stepping stone to complete most, if not all, the configuration changes that can be scripted while skipping past issues like branding and banners where those should not be implemented even in a hardened personal use environment.

- This script is designed in such a way that the optimizations, unlike some other scripts, will not break core windows functionality.

- Features like Windows Update, Windows Defender, the Windows Store, and Cortona have been restricted, but are not in a dysfunctional state like most other Windows 10 Privacy scripts.

- If you seek a minimized script targeted only to commercial environments, please see this [GitHub Repository](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)





**Do not run this script if you don't understand what it does. It is your responsibility to review and test the script before running it.**



**FOR EXAMPLE, THE FOLLOWING WILL BREAK IF YOU RUN THIS WITHOUT TAKING PREVENTATIVE STEPS:**



- Using the default administrator account named "Administrator" is disabled and renamed per DoD STIG



  - Does not apply to the default account created but does apply to using the Default Administrator account often found on Enterprise, IOT, and Windows Server Versions



  - Create a new account under Computer Management and set it as an administrator if you wish. Then copy the contents of the previous users folder into the new one after signing into the new user for the first time to work around this prior to running the script.



- Signing in using a microsoft account is disabled per DoD STIG. 



  - When trying to be secure and private, signing into your local account via a Microsoft Account is not advised. This is enforced by this repo.



  - Create a new account under Computer Management and set it as an administrator if you wish. Then copy the contents of the previous users folder into the new one after signing into the new user for the first time to work around this prior to running the script.

