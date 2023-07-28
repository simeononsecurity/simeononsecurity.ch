---
title: "Windows Hardening CTF: Consolidarea securității dispozitivului Windows pentru evenimentele Capture the Flag"
date: 2020-10-19
toc: true
draft: false
description: "Descoperiți un script puternic care îmbunătățește securitatea Windows prin implementarea diverselor măsuri de întărire pentru a împiedica compromiterea."
tags: ["Întărirea ferestrelor", "Securitatea Windows", "script", "Dispozitiv Windows", "prompt de comandă", "LLMNR", "PowerShell", "SMB", "Timestamp-uri TCP", "AppLocker", "Înregistrare Windows", "DEP", "Configurații EMET", "Modul de limbaj restricționat PowerShell", "Criptare SMB", "Măsuri de atenuare Spectre și Meltdown", "Windows Defender", "Windows Firewall", "PSWindowsUpdate", "Actualizări Windows", "script de întărire", "Politici recomandate de ANS", "Controale de logare și securitate pentru Windows", "Controlul aplicațiilor Windows Defender", "Proceduri de reducere a suprafeței de atac a Windows Defender", "Protecții bazate pe cloud pentru Windows Defender", "Protecții împotriva exploatărilor din Windows Defender", "Instalarea PSWindowsUpdate", "Îmbunătățirea securității dispozitivelor Windows", "Măsuri de întărire a Windows", "consolidarea securității Windows"]
---

**Fereastră-Încălzire-CTF**
Un script de întărire a Windows care face dificilă și mai enervantă compromiterea unui dispozitiv Windows.

## Ce face acest script?
- Dezactive Command Prompt
- Dezactivează LLMNR
- Dezactivează PowerShell v2
- Dezactive compresia SMB
- Dezactivează SMB v1
- Dezactivează SMB v2
- Dezactivează Timestamps TCP
- Dezactivează WSMAN și PSRemoting
- Activează AppLocker cu politicile recomandate de NSA
- Activează cele mai bune practici de logare și control al securității Windows
- Activează DEP
- Activează configurațiile EMET (se aplică numai la sistemele cu EMET instalat)
- Enables PowerShell Constrined Language Mode (Activează modul de limbaj constrâns PowerShell)
- Enables PowerShell Logging (Activează jurnalizarea PowerShell)
- Enables SMB Encryption (Activează criptarea SMB)
- Enables Spectre and Meltdown Mitigations (Activează atenuările Spectre și Meltdown)
- Activează controlul aplicațiilor Windows Defender
- Activează Windows Defender Attack Surface Reduction Procections (Proceduri de reducere a suprafeței de atac)
- Activează Windows Defender Protecții bazate pe cloud
- Activează Windows Defender Exploit Protections
- Activează Windows Firewall și logare
- Instalează PSWindowsUpdate și instalează toate actualizările Windows disponibile

## Descărcați fișierele necesare:

Descărcați fișierele necesare de pe site-ul [GitHub Repository](https://github.com/simeononsecurity/Windows-Hardening-CTF)

## Cum se execută scriptul:

**Scriptul poate fi lansat din descărcarea extrasă de pe GitHub astfel:**
```
.\sos-windows-hardening-ctf.ps1
```
