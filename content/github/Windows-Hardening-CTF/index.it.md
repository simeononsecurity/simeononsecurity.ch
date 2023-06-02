---
title: "Windows Hardening CTF: rafforzare la sicurezza del dispositivo Windows per gli eventi Capture the Flag"
date: 2020-10-19
toc: true
draft: false
description: "Scoprite un potente script che migliora la sicurezza di Windows implementando varie misure di hardening per impedire la compromissione."
tags: ["Indurimento delle finestre", "Sicurezza di Windows", "sceneggiatura", "Dispositivo Windows", "prompt dei comandi", "LLMNR", "PowerShell", "SMB", "Timestamp TCP", "AppLocker", "Registrazione di Windows", "DEP", "Configurazioni EMET", "Modalità linguistica vincolata di PowerShell", "Crittografia SMB", "Attenuazioni di Spectre e Meltdown", "Windows Defender", "Firewall di Windows", "PSWindowsUpdate", "Aggiornamenti di Windows", "script di indurimento", "Politiche raccomandate dall'ANS", "Controlli di sicurezza e registrazione di Windows", "Controllo applicazioni di Windows Defender", "Procedimenti di riduzione della superficie di attacco di Windows Defender", "Protezioni basate sul cloud di Windows Defender", "Protezioni Exploit di Windows Defender", "Installazione di PSWindowsUpdate", "Miglioramento della sicurezza dei dispositivi Windows", "Misure di hardening di Windows", "rafforzare la sicurezza di Windows"]
---

**Indurimento di Windows-CTF**
Uno script per l'indurimento di Windows che rende più difficile e fastidiosa la compromissione di un dispositivo Windows.

## Cosa fa questo script?
- Disabilita il prompt dei comandi
- Disabilita LLMNR
- Disabilita PowerShell v2
- Disabilita la compressione SMB
- Disabilita SMB v1
- Disabilita SMB v2
- Disabilita i timestamp TCP
- Disabilita WSMAN e PSRemoting
- Abilita AppLocker con i criteri consigliati dall'NSA
- Abilita le migliori pratiche di registrazione e controlli di sicurezza di Windows
- Abilita DEP
- Abilita le configurazioni EMET (si applica solo ai sistemi con EMET installato)
- Abilita la modalità PowerShell Constrined Language
- Abilita la registrazione di PowerShell
- Abilita la crittografia SMB
- Abilita le mitigazioni di Spectre e Meltdown
- Abilita il controllo delle applicazioni di Windows Defender
- Abilita le procedure di riduzione della superficie di attacco di Windows Defender
- Abilita le protezioni basate sul cloud di Windows Defender
- Attiva le protezioni Exploit di Windows Defender
- Attiva il firewall e la registrazione di Windows
- Installa PSWindowsUpdate e installa tutti gli aggiornamenti disponibili di Windows

## Scaricare i file necessari:

Scaricare i file necessari dal sito [GitHub Repository](https://github.com/simeononsecurity/Windows-Hardening-CTF)

## Come eseguire lo script:

**Lo script può essere prelevato dal download estratto da GitHub in questo modo:**
```
.\sos-windows-hardening-ctf.ps1
```
