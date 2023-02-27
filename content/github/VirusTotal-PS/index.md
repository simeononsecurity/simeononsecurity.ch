---
title: ""Efficient Virus Scans with VirusTotal PowerShell Modules""
date: 2020-11-24
toc: true
draft: false
description: "Perform efficient virus scans with the VirusTotal PowerShell Modules by automating the interaction with VirusTotal API and streamlining your security workflow."
tags: ["PowerShell Modules", "PowerShell", "Automation", "VirusTotal", "Virus Scans", "Domain Scans", "API Key", "VirusTotal API", "VirusTotal Developers Page", "System Administration", "Security Workflow", "Efficient Virus Scans", "Download and Install", "GitHub Repository", "API Usage Examples"]

---
A collection of PowerShell Modules for Interacting with the VirusTotal API

**Notes:**
- You'll need your VirusTotal API key, which can be found on your [Shodan Account](https://www.virustotal.com/gui/)
- Examples of the APIs used in the modules may be found on the [VirusTotal Developers Page](https://developers.virustotal.com/reference#getting-started)

## Download and Install
- Download the modules from the [GitHub Repository](https://github.com/simeononsecurity/VirusTotal-PS)
- Install all the modules
```ps
Get-ChildItem -Recurse *.ps1 | Import-Module
```