---
title: "Proteggere Windows dagli attacchi al canale laterale dell'esecuzione speculativa"
date: 2020-06-18
toc: true
draft: false
description: "Scoprite come proteggere il vostro sistema Windows dagli attacchi side-channel di esecuzione speculativa con lo script di mitigazione e gli aggiornamenti del firmware di Microsoft."
tags: ["Script per la mitigazione di Spectre e Meltdown in Windows", "Attacchi side channel all'esecuzione speculativa", "Microsoft", "Intel", "AMD", "VIA", "BRACCIO", "Android", "Cromo", "iOS", "macOS", "Iniezione dell'obiettivo del ramo", "Bypass del controllo dei limiti", "Carico della cache dei dati anomali", "Bypass del negozio speculativo", "Campionamento dei dati microarchitettonici", "CVE", "Aggiornamenti del firmware", "GitHub Repository", "PowerShell"]
---
 https://support.microsoft.com/en-us/help/4073119/protect-against-speculative-execution-side-channel-vulnerabilities-in
**Semplice script per implementare protezioni contro le vulnerabilità dei canali laterali di esecuzione speculativa nei sistemi Windows.**

Microsoft è a conoscenza di una nuova classe di vulnerabilità divulgata pubblicamente, denominata "attacchi side-channel di esecuzione speculativa", che colpisce molti processori moderni, tra cui Intel, AMD, VIA e ARM.

**Nota:** Questo problema riguarda anche altri sistemi operativi, come Android, Chrome, iOS e macOS. Pertanto, consigliamo ai clienti di rivolgersi a tali fornitori.

Abbiamo rilasciato diversi aggiornamenti per contribuire a mitigare queste vulnerabilità. Abbiamo anche intrapreso azioni per proteggere i nostri servizi cloud. Per maggiori dettagli, consultare le sezioni seguenti.

Non abbiamo ancora ricevuto alcuna informazione che indichi che queste vulnerabilità siano state utilizzate per attaccare i clienti. Stiamo lavorando a stretto contatto con i partner del settore, tra cui produttori di chip, OEM di hardware e fornitori di applicazioni, per proteggere i clienti. Per ottenere tutte le protezioni disponibili, è necessario aggiornare il firmware (microcodice) e il software. Ciò include il microcodice degli OEM dei dispositivi e, in alcuni casi, gli aggiornamenti del software antivirus.

**Questo articolo tratta le seguenti vulnerabilità:**
- CVE-2017-5715 - "Branch Target Injection".
- CVE-2017-5753 - "Bypass del controllo dei limiti".
- CVE-2017-5754 - "Caricamento anomalo della cache dei dati".
- CVE-2018-3639 - "Bypass del negozio speculativo".
- CVE-2018-11091 - "Memoria non memorizzabile con campionamento dati microarchitetturale (MDSUM)"
- CVE-2018-12126 - "Microarchitectural Store Buffer Data Sampling (MSBDS)"
- CVE-2018-12127 - "Microarchitectural Fill Buffer Data Sampling (MFBDS)"
- CVE-2018-12130 - "Microarchitectural Load Port Data Sampling (MLPDS)"

**AGGIORNAMENTO DEL 6 AGOSTO 2019** Il 6 agosto 2019 Intel ha rilasciato dettagli su una vulnerabilità di divulgazione delle informazioni del kernel di Windows. Questa vulnerabilità è una variante della vulnerabilità del canale laterale di esecuzione speculativa Spectre Variant 1 ed è stata assegnata a CVE-2019-1125.

**Il 12 novembre 2019 Intel ha pubblicato un avviso tecnico sulla vulnerabilità Intel® Transactional Synchronization Extensions (Intel® TSX) Transaction Asynchronous Abort, assegnata a CVE-2019-11135. Microsoft ha rilasciato aggiornamenti per mitigare questa vulnerabilità e le protezioni del sistema operativo sono abilitate per impostazione predefinita per le edizioni del sistema operativo Windows Client.

## Azioni consigliate
I clienti devono intraprendere le seguenti azioni per proteggersi dalle vulnerabilità:

- Applicare tutti gli aggiornamenti del sistema operativo Windows disponibili, compresi gli aggiornamenti di sicurezza mensili di Windows.
- Applicare l'aggiornamento del firmware (microcodice) fornito dal produttore del dispositivo.
- Valutare il rischio per il proprio ambiente in base alle informazioni fornite negli avvisi di sicurezza Microsoft: ADV180002, ADV180012, ADV190013 e le informazioni fornite in questo articolo della Knowledge Base.
- Adottare le misure necessarie utilizzando gli avvisi e le informazioni sulle chiavi di registro fornite in questo articolo della Knowledge Base.

## Scaricare i file necessari:

Scaricare i file necessari dal sito[GitHub Repository](https://github.com/simeononsecurity/Windows-Spectre-Meltdown-Mitigation-Script)

## Come eseguire lo script:

**Lo script può essere prelevato dal download estratto da GitHub in questo modo:**
```
.\sos-spectre-meltdown-mitigations.ps1
```
