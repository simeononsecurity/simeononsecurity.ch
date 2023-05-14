---
title: "Protegiu Windows dels atacs de canal lateral d'execució especulativa"
date: 2020-06-18
toc: true
draft: false
description: "Apreneu a protegir el vostre sistema Windows contra atacs de canal lateral d'execució especulativa amb l'script de mitigació i les actualitzacions de microprogramari de Microsoft"
tags: ["Script de mitigació de Windows Spectre Meltdown", "Execució especulativa Atacs de canal lateral", "Microsoft", "Intel", "AMD", "VIA", "ARM", "Android", "Chrome", "iOS", "macOS", "Injecció Branch Target", "Comprovació de límits Bypass", "Càrrega de la memòria cau de dades fraudulentes", "Bypass especulatiu de la botiga", "Mostra de dades de microarquitectura", "CVE", "Actualitzacions de firmware", "Repositori GitHub", "PowerShell"]
---
 https://support.microsoft.com/en-us/help/4073119/protect-against-speculative-execution-side-channel-vulnerabilities-in
** Script senzill per implementar proteccions contra les vulnerabilitats del canal lateral d'execució especulativa als sistemes Windows.**

Microsoft és conscient d'una nova classe de vulnerabilitats divulgada públicament que s'anomenen "atacs de canal lateral d'execució especulativa" i que afecten molts processadors moderns, inclosos Intel, AMD, VIA i ARM.

**Nota:** aquest problema també afecta altres sistemes operatius, com ara Android, Chrome, iOS i macOS. Per tant, aconsellem als clients que busquin orientació d'aquests venedors.

Hem publicat diverses actualitzacions per ajudar a mitigar aquestes vulnerabilitats. També hem pres mesures per protegir els nostres serveis al núvol. Consulteu les seccions següents per obtenir més detalls.

Encara no hem rebut cap informació que indiqui que aquestes vulnerabilitats es van utilitzar per atacar clients. Estem treballant estretament amb socis del sector, com ara fabricants de xips, fabricants de maquinari i proveïdors d'aplicacions per protegir els clients. Per obtenir totes les proteccions disponibles, cal actualitzar el firmware (microcodi) i el programari. Això inclou microcodi dels OEM de dispositius i, en alguns casos, actualitzacions del programari antivirus.

**Aquest article aborda les vulnerabilitats següents:**
- CVE-2017-5715 - "Injecció diana de sucursal"
- CVE-2017-5753: "Bounds Check Bypass"
- CVE-2017-5754: "Càrrega de la memòria cau de dades fraudulentes"
- CVE-2018-3639: "Bloc de la botiga especulativa"
- CVE-2018-11091: "Memòria no cacheable de mostreig de dades de microarquitectura (MDSUM)"
- CVE-2018-12126: "Mostreig de dades de memòria intermèdia de botiga microarquitectura (MSBDS)"
- CVE-2018-12127: "Mostreig de dades de buffer d'ompliment microarquitectònic (MFBDS)"
- CVE-2018-12130: "Mostreig de dades de port de càrrega microarquitectònic (MLPDS)"

**ACTUALITZAT EL 6 D'AGOST DE 2019** El 6 d'agost de 2019 Intel va publicar detalls sobre una vulnerabilitat de divulgació d'informació del nucli de Windows. Aquesta vulnerabilitat és una variant de la vulnerabilitat del canal lateral d'execució especulativa Spectre Variant 1 i se li ha assignat CVE-2019-1125.

**ACTUALITZAT EL 12 DE NOVEMBRE DE 2019** El 12 de novembre de 2019, Intel va publicar un assessorament tècnic sobre la vulnerabilitat d'Avortament asíncron de transaccions d'Intel® Transactional Synchronization Extensions (Intel® TSX) a la qual se li assigna CVE-2019-11135. Microsoft ha publicat actualitzacions per ajudar a mitigar aquesta vulnerabilitat i les proteccions del sistema operatiu estan habilitades de manera predeterminada per a les edicions del sistema operatiu client de Windows.

## Accions recomanades
Els clients han de prendre les accions següents per ajudar a protegir-se de les vulnerabilitats:

- Apliqueu totes les actualitzacions disponibles del sistema operatiu Windows, incloses les actualitzacions mensuals de seguretat de Windows.
- Apliqueu l'actualització de firmware (microcodi) aplicable que proporciona el fabricant del dispositiu.
- Avalueu el risc per al vostre entorn basant-vos en la informació que es proporciona als avisos de seguretat de Microsoft: ADV180002, ADV180012, ADV190013 i la informació proporcionada en aquest article de la base de coneixement.
- Preneu les mesures necessàries utilitzant els avisos i la informació de clau de registre que es proporcionen en aquest article de la Base de coneixement.

## Baixeu els fitxers necessaris:

Baixeu els fitxers necessaris des del[GitHub Repository](https://github.com/simeononsecurity/Windows-Spectre-Meltdown-Mitigation-Script)

## Com executar l'script:

**L'script es pot llançar des de la descàrrega de GitHub extreta així:**
```
.\sos-spectre-meltdown-mitigations.ps1
```
