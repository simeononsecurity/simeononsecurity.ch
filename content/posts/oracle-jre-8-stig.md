---
title: "Automating Oracle JRE 8 STIG"
date: 2020-08-05T21:54:53-05:00
draft: false
tags: ['JAVA', 'STIG', 'JAVA STIG', 'JRE', 'JRE8', 'JRE STIG', 'Compliance', 'Automation', 'Powershell', 'Script']
---

# Automate Oracle JRE 8 STIGS

The Oracle JRE STIGs aren’t so straight forward, requiring administrators to research JAVA documentation and generate java config files, when most administrators are used to solely STIG-ing using group policy.

## Download the required files

Download the required files from the [GitHub Repository](https://github.com/simeononsecurity/JAVA-STIG-Script)

## STIGS/SRGs Applied:
- [Oracle JRE 8 V1R5](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Oracle_JRE_8_Windows_V1R5_STIG.zip)

## Sources:
- [MyITGuy - deployment.properties](https://gist.github.com/MyITGuy/9628895)

- [cbu.edu - Java Technotes](http://stu.cbu.edu/java/docs/technotes/guides/deploy/properties.html)

## How to run the script

**The script may be lauched from the extracted GitHub download like this:**

```
.\sos-install-java-config.ps1
```
