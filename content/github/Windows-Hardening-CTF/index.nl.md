---
title: "Windows Hardening CTF: Versterk de beveiliging van uw Windows-apparaat voor Capture the Flag-evenementen"
date: 2020-10-19
toc: true
draft: false
description: "Ontdek een krachtig script dat de beveiliging van Windows verbetert door verschillende hardening-maatregelen toe te passen om compromissen te voorkomen."
tags: ["Ramen verharden", "Windows beveiliging", "script", "Windows-apparaat", "opdrachtprompt", "LLMNR", "PowerShell", "SMB", "TCP-tijdstempels", "AppLocker", "Windows logging", "DEP", "EMET-configuraties", "PowerShell beperkte taalmodus", "SMB encryptie", "Spectre en Meltdown mitigaties", "Windows Defender", "Windows Firewall", "PSWindowsUpdate", "Windows updates", "hardening script", "NSA aanbevolen beleid", "Windows Logging en beveiligingscontroles", "Windows Defender Toepassingscontrole", "Windows Defender Beperking van het aanvalsoppervlak", "Windows Defender Cloud-gebaseerde Bescherming", "Windows Defender Bescherming tegen Exploit", "PSWindowsUpdate installatie", "Verbetering van de beveiliging van Windows-apparaten", "Hardening van Windows", "de beveiliging van Windows versterken"]
---

**Windows-Hardening-CTF**
Een windows hardening script dat het moeilijk en vervelender maakt om een Windows apparaat te compromitteren.

## Wat doet dit script?
- Schakelt Command Prompt uit
- Schakelt LLMNR uit
- Schakelt PowerShell v2 uit
- Schakelt SMB Compressie uit
- Schakelt SMB v1 uit
- Schakelt SMB v2 uit
- Schakelt TCP Timestamps uit
- Schakelt WSMAN en PSRemoting uit.
- Schakelt AppLocker in met NSA aanbevolen beleid.
- Schakelt Best Practice Windows Logging and Security Controls in.
- Schakelt DEP in
- Schakelt EMET-configuraties in (geldt alleen voor systemen waarop EMET is geïnstalleerd).
- Maakt PowerShell Constrined Language Mode mogelijk
- Schakelt PowerShell Logging in
- SMB-codering inschakelen
- Spectre en Meltdown Mitigations inschakelen
- Maakt Windows Defender Application Control mogelijk
- Maakt Windows Defender Attack Surface Reduction Procections mogelijk.
- Maakt Windows Defender cloud-gebaseerde beveiliging mogelijk
- Maakt Windows Defender bescherming tegen exploits mogelijk
- Schakelt Windows Firewall en logboekregistratie in
- Installeert PSWindowsUpdate en installeert alle beschikbare Windows-updates.

## Download de vereiste bestanden:

Download de vereiste bestanden van de [GitHub Repository](https://github.com/simeononsecurity/Windows-Hardening-CTF)

## Hoe voer je het script uit:

**Het script kan worden gelanceerd vanaf de uitgepakte GitHub-download als volgt:**
```
.\sos-windows-hardening-ctf.ps1
```
