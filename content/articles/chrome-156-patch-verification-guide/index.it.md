---
title: "Aggiornamento di sicurezza di Chrome 156: verifica la patch di ottobre"
date: 2026-10-28
lastmod: 2026-11-09
toc: true
draft: false
description: "Verifica il rilascio di sicurezza di Chrome 156 del 27 ottobre su Windows, macOS, Linux e Android. Confronta la build installata, completa un riavvio in sospeso e controlla separatamente i dispositivi gestiti."
genre: ["Browser", "Sicurezza", "Gestione delle patch"]
tags: ["Chrome 156", "aggiornamento di sicurezza di Chrome", "verifica delle patch di Chrome", "controllo della versione di Chrome", "Chrome 156 per Windows", "Chrome 156 per macOS", "Chrome 156 per Linux", "Chrome 156 per Android", "CVE-2026-118306", "CVE-2026-118331", "CVE-2026-118348", "CVE-2026-118344", "patch per browser", "Chrome Enterprise Core", "browser gestiti", "sicurezza di Chromium", "aggiornamenti del browser", "riavvio di Chrome", "chrome://version", "chrome://settings/help", "aggiornamento di Chrome per Android", "aggiornamenti di sicurezza di Brave", "aggiornamenti di sicurezza di Edge"]
cover: "/img/cover/cybersecurity-padlock-shield.webp"
coverAlt: "Illustrazione di un lucchetto e di uno scudo che rappresentano un aggiornamento di sicurezza, non una schermata della versione di Chrome"
coverCaption: ""
---

**Il rilascio di sicurezza di Chrome del 27 ottobre 2026** include 52 correzioni. Per verificare la tua installazione, confronta la versione completa con quella pubblicata per il tuo sistema operativo, poi riavvia Chrome per completare gli aggiornamenti in sospeso. L'annuncio di una versione non dimostra che il dispositivo abbia ricevuto l'aggiornamento. ([Rilascio di Chrome per desktop](https://chromereleases.googleblog.com/2026/10/stable-channel-update-for-desktop_0562499947.html))

<!--more-->

## Quale versione dovresti vedere?

Google ha pubblicato queste versioni del canale Stable il 27 ottobre 2026. L'annuncio per desktop elenca build separate per Windows e macOS e per Linux. Il [rilascio per Android](https://chromereleases.googleblog.com/2026/10/chrome-for-android-update_0160078013.html) indica la propria build e specifica che le versioni Android contengono le stesse correzioni di sicurezza delle versioni desktop corrispondenti, «salvo diversa indicazione».

| Piattaforma | Build nell'annuncio Google del 27 ottobre |
|---|---|
| **Windows** | 156.0.8078.73 o 156.0.8078.74 |
| **macOS** | 156.0.8078.73 o 156.0.8078.74 |
| **Linux** | 156.0.8078.73 |
| **Android** | 156.0.8078.73 |

*Usa questa tabella per il rilascio del 27 ottobre, non come obiettivo permanente. Per i successivi aggiornamenti di sicurezza consulta il [feed aggiornato dei rilasci di Chrome](https://chromereleases.googleblog.com/).* Google ha dichiarato che la distribuzione per desktop avrebbe richiesto «i prossimi giorni o settimane» e che la build Android sarebbe arrivata su Google Play nei giorni successivi. Un dispositivo con una versione inferiore a quella indicata deve comunque essere controllato, anche durante una distribuzione graduale. ([Avviso desktop](https://chromereleases.googleblog.com/2026/10/stable-channel-update-for-desktop_0562499947.html), [avviso Android](https://chromereleases.googleblog.com/2026/10/chrome-for-android-update_0160078013.html))

L'[elenco delle correzioni di sicurezza per desktop](https://chromereleases.googleblog.com/2026/10/stable-channel-update-for-desktop_0562499947.html) classifica quattro difetti segnalati come **Critical**: corruzione della memoria in FileSystem [CVE-2026-118306](https://nvd.nist.gov/vuln/detail/CVE-2026-118306), convalida errata dell'input in FileAPI CVE-2026-118331, convalida errata dell'input in Skia CVE-2026-118348 e use-after-free in Layout CVE-2026-118344. Lo stesso avviso elenca altri CVE classificati **High** e **Medium**. Il numero 52 indica le correzioni di sicurezza incluse nel rilascio, non 52 segnalazioni di sfruttamento verificate in modo indipendente. ([Record NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-118306))

**L'avviso del rilascio non afferma che le vulnerabilità elencate siano sfruttate attivamente.** L'avvertenza riguarda i tempi di divulgazione: «L'accesso ai dettagli dei bug e ai collegamenti potrebbe rimanere limitato finché la maggior parte degli utenti non avrà ricevuto una correzione». Non considerare l'accesso limitato ai dettagli come prova di sfruttamento. ([Avviso desktop](https://chromereleases.googleblog.com/2026/10/stable-channel-update-for-desktop_0562499947.html))

## Verifica e completa l'aggiornamento desktop

1. Apri **`chrome://version`** nell'installazione di Chrome che usi. Annota la versione completa e il sistema operativo, non solo il numero principale 156. Verifica separatamente le finestre di Chrome appartenenti a un altro canale o a un'altra installazione.
2. Apri **`chrome://settings/help`** oppure seleziona **Altro > Guida > Informazioni su Google Chrome**. Google specifica che Chrome cerca gli aggiornamenti in questa pagina. Attendi il completamento del controllo. ([Istruzioni Google per l'aggiornamento desktop](https://support.google.com/chrome/answer/95414?co=GENIE.Platform%3DDesktop&hl=en))
3. Se la pagina offre l'opzione, seleziona **Riavvia**. Prima salva il lavoro in corso. Chiudi le altre finestre di Chrome, riapri il browser e controlla di nuovo **`chrome://version`**. Confronta con la tabella la versione visualizzata dopo il riavvio.
4. Se la versione è ancora inferiore alla build annunciata, cerca di nuovo gli aggiornamenti disponibili. Se un'organizzazione gestisce il browser o il programma di aggiornamento segnala un errore, contatta l'amministratore. Un download riuscito non dimostra che la versione del browser in esecuzione sia cambiata.

> **Risultato previsto:** Dopo il riavvio, la build Stable di Chrome in esecuzione corrisponde alla versione indicata per la piattaforma nell'annuncio del 27 ottobre o a una versione successiva annunciata dal fornitore. Un pulsante Riavvia ancora visibile non prova che l'aggiornamento sia completato.

Su **Android**, apri Play Store > icona del profilo > Gestisci app e dispositivo, quindi aggiorna Chrome nella sezione Aggiornamenti disponibili, se l'opzione è presente. In Chrome, apri Altro > Impostazioni > Informazioni su Chrome per leggere la versione installata. Dopo il completamento dell'aggiornamento dell'app, confrontala con la riga Android. Questi percorsi dei menu seguono le [istruzioni Google per Android](https://support.google.com/chrome/answer/95414?co=GENIE.Platform%3DAndroid&hl=en).

## Verifica i parchi di browser gestiti

Per i browser registrati, usa il **rapporto sulle versioni di Chrome** nella Console di amministrazione Google per individuare le build meno recenti in base al sistema operativo. Apri la vista Browser Versions, seleziona l'unità organizzativa pertinente, controlla la versione secondaria completa ed esporta il CSV se ti serve un elenco operativo dei dispositivi. Google afferma che il rapporto include i browser che hanno inviato dati negli ultimi 28 giorni. Segnala possibili ritardi, soprattutto nei parchi di grandi dimensioni. ([Visualizza i dettagli delle versioni di Chrome](https://support.google.com/chrome/a/answer/10025748?hl=en))

**Separa l'inventario segnalato dalla verifica in tempo reale.** Controlla l'ora dell'ultimo rapporto e il canale di ogni dispositivo, poi conferma le eccezioni direttamente nel browser o tramite l'inventario degli endpoint gestiti. Google conta separatamente le installazioni distinte di Chrome, come Stable e Beta. I rapporti sui browser richiedono la registrazione e la [reportistica dei browser gestiti](https://support.google.com/chrome/a/answer/9301421?hl=en). L'assenza di un computer dal rapporto non dimostra che sia aggiornato.

## Verifica separatamente i browser derivati da Chromium

**La tabella delle versioni di Chrome si applica a Google Chrome.** Microsoft Edge, Brave e gli altri browser basati su Chromium hanno pacchetti, numeri di rilascio e calendari di aggiornamento propri. L'annuncio di Chrome non conferma il loro stato delle patch. Controlla la versione installata di ciascun browser e il relativo avviso di sicurezza o le note di rilascio per le correzioni Chromium pertinenti. Non confrontare direttamente una versione di Edge o Brave con il numero 156.0.8078.73 di Chrome e dichiararla aggiornata.

Per ogni derivato, annota il nome del prodotto, il canale, la build installata, l'URL dell'avviso del fornitore e la build che il fornitore indica come corretta. Se il fornitore non ha confermato una correzione, contrassegna lo stato come **non verificato** e segui le istruzioni di aggiornamento indicate. Registra Chrome e i browser derivati in righe separate dell'inventario.

## Fonti e riferimenti

- [Chrome Releases: aggiornamento Stable Channel per desktop, 27 ottobre 2026](https://chromereleases.googleblog.com/2026/10/stable-channel-update-for-desktop_0562499947.html). Build desktop, 52 correzioni, CVE e testo del fornitore sulla divulgazione.
- [Chrome Releases: aggiornamento di Chrome per Android, 27 ottobre 2026](https://chromereleases.googleblog.com/2026/10/chrome-for-android-update_0160078013.html). Build Android e nota sulle correzioni desktop corrispondenti.
- [Issue tracker Chromium: ricerca delle correzioni di sicurezza M156](https://issues.chromium.org/issues?q=customfield1223088:1-M156). Collegamento incluso nell'annuncio desktop. L'accesso ai dettagli dei singoli problemi dipende dalle restrizioni di divulgazione.
- [NVD: CVE-2026-118306](https://nvd.nist.gov/vuln/detail/CVE-2026-118306) e [CVE-2026-118331](https://nvd.nist.gov/vuln/detail/CVE-2026-118331). Descrizioni delle vulnerabilità e versioni di Chrome interessate. I livelli di gravità sopra riportati seguono l'avviso di Google, non una valutazione CVSS di NVD.
- [Guida di Google Chrome: aggiornare Chrome sui computer](https://support.google.com/chrome/answer/95414?co=GENIE.Platform%3DDesktop&hl=en) e [su Android](https://support.google.com/chrome/answer/95414?co=GENIE.Platform%3DAndroid&hl=en). Controllo degli aggiornamenti e percorsi dei menu della versione.
- [Guida di Chrome Enterprise: visualizzare i dettagli della versione di Chrome](https://support.google.com/chrome/a/answer/10025748?hl=en) e [attivare la reportistica dei browser gestiti](https://support.google.com/chrome/a/answer/9301421?hl=en). Prerequisiti e limiti dei rapporti sui parchi.
