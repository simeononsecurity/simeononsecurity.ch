---
title: "Shodan Powershell Modules"
date: 2020-11-14T19:34:03-06:00
draft: false
tags: ['shodan', 'api', 'powershell', 'modules', 'automation', 'enumeration', 'Shodan API', 'Showdan PowerShell', 'PowerShell Modules']
toc: true
---

# Shodan_PS
A collection of PowerShell Modules for Interacting with the Shodan API

**Notes:**
- You'll need you Shodan API key, which can be found on your [Shodan Account](https://account.shodan.io/)
- Examples of the APIs used in the modules may be found on the [Shodan Developers Page](https://developer.shodan.io/api)


## Download and Install
- Download the modules from the [GitHub Repository](https://github.com/simeononsecurity/Shodan_PS)
- Install all the modules
```ps
Get-ChildItem -Recurse *.ps1 | Import-Module
```