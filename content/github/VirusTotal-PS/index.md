---
title: "Efficient Virus Scans with VirusTotal PowerShell Modules: Get Your API Key and Start Automating Today"
date: 2020-11-24
toc: true
draft: false
description: "The VirusTotal PowerShell Modules are a collection of tools that allow you to interact with the VirusTotal API using the powerful automation capabilities of PowerShell. These modules allow you to quickly and easily perform virus scans, domain scans, and other security checks. To use the modules, you'll need your VirusTotal API key, which can be obtained from your VirusTotal account. The modules can be downloaded from the GitHub Repository, and installation is straightforward with a single command. The VirusTotal Developers Page provides examples of the APIs used in the modules, making it easy to get started. Whether you're an experienced system administrator or just starting out, these modules are a must-have for anyone looking to streamline their security workflow with VirusTotal."
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