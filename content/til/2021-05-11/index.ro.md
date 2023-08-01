---
title: "Astăzi am învățat despre Auditpol, Sysmon, și configurații Sysmon"
date: 2021-05-11
toc: true
draft: false
description: ""
genre: ["PowerShell", "Automatizare", "Sysmon", "Configurații", "Securitatea Windows", "Monitorizarea evenimentelor", "Administrare Windows", "Auditul de securitate", "Vânătoarea de amenințări", "Analiza malware-ului"]
tags: ["PowerShell", "Automatizare", "Sysmon", "Configurații", "SwiftOnSecurity", "Securitatea Windows", "Monitorizarea evenimentelor", "Polul de audit", "Politica de audit Windows", "Automate-Sysmon", "Windows-Audit-Policy", "Noțiuni de bază pentru a începe cu Sysmon", "Arheologie Malware Cheat Sheets", "Microsoft Sysinternals", "Configurații Sysmon", "Comenzi Auditpol", "Auditpol backup", "Auditpol Clear", "Lista polilor de audit", "Auditpol Restore", "Sysmon-Modular", "Instrumente de administrare Windows", "Înregistrare de securitate", "Detectarea amenințărilor", "Înregistrarea evenimentelor", "Monitorizarea securității", "Cele mai bune practici de securitate Windows", "Soluții de automatizare", "Tehnici de auditare a securității"]
---

**Ce a aflat SimeonOnSecurity despre și a găsit interesant astăzi**

SimeonOnSecurity a învățat și a descoperit astăzi mai multe lucruri interesante legate de securitatea Windows și monitorizarea evenimentelor.

În primul rând, au fost identificate două depozite noi și actualizate. Depozitul Automate-Sysmon oferă o soluție pentru automatizarea instalării, configurării și gestionării Sysmon, un instrument popular pentru monitorizarea și înregistrarea activității sistemului pe sistemele Windows. Depozitul Windows-Audit-Policy oferă o soluție pentru automatizarea configurării politicilor de audit Windows, care controlează auditarea diferitelor evenimente legate de securitate pe sistemele Windows.

SimeonOnSecurity a găsit, de asemenea, mai multe resurse de învățare legate de securitatea Windows și monitorizarea evenimentelor. Articolul Getting Started With Sysmon oferă o introducere cuprinzătoare în Sysmon, inclusiv caracteristicile, beneficiile și modul de utilizare eficientă a acestuia. Fișele de ieftinire Malware Archaeology Cheat Sheets oferă informații concise și ușor de aplicat pe diverse subiecte legate de analiza malware și de vânătoarea de amenințări. Documentația Microsoft Sysinternals - Sysmon oferă informații despre caracteristicile și utilizarea lui Sysmon. Depozitul sysmon-config oferă un set de reguli Sysmon preconfigurate care pot fi utilizate ca punct de plecare pentru personalizarea configurației Sysmon.

În cele din urmă, SimeonOnSecurity a găsit mai multe resurse legate de instrumentul de linie de comandă pentru politica de audit Windows (auditpol). Documentele auditpol backup, auditpol clear, auditpol list și auditpol restore oferă informații despre modul de utilizare a acestor comenzi pentru a gestiona politica de audit Windows. Documentul auditpol oferă o prezentare cuprinzătoare a instrumentului auditpol și a capacităților sale. În cele din urmă, depozitul sysmon-modular oferă o abordare modulară a configurării Sysmon, care poate fi utilă pentru organizațiile mari cu cerințe de securitate complexe.

## Depozite noi/actualizate:

- [simeononsecurity/Automate-Sysmon](https://github.com/simeononsecurity/Automate-Sysmon)
- [simeononsecurity/Windows-Audit-Policy](https://github.com/simeononsecurity/Windows-Audit-Policy)

## Resurse de învățare:

- [BHIS - Getting Started With Sysmon](https://www.blackhillsinfosec.com/getting-started-with-sysmon/)
- [Malware Archaeology Cheat Sheets](https://www.malwarearchaeology.com/cheat-sheets)
- [Microsoft Sysinternals - Sysmon](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon)
- [SwiftOnSecurity/sysmon-config](https://github.com/SwiftOnSecurity/sysmon-config)
- [auditpol backup](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/auditpol-backup)
- [auditpol clear](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/auditpol-clear)
- [auditpol list](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/auditpol-list)
- [auditpol restore](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/auditpol-restore)
- [auditpol](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/auditpol)
- [olafhartong/sysmon-modular](https://github.com/olafhartong/sysmon-modular)
