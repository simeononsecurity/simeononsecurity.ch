---
title: "Thunderbird 153.6: esposizione delle credenziali NTLM su Windows e come aggiornare (2026)"
date: 2026-10-28
lastmod: 2026-11-12
toc: true
draft: false
description: "Due gravi vulnerabilità di Thunderbird espongono dati di autenticazione NTLM su Windows quando viene visualizzata un’e-mail preparata ad arte. Scopri i due percorsi, verifica la versione e limita l’SMB in uscita durante l’aggiornamento."
genre: ["Sicurezza informatica", "Sicurezza della posta elettronica", "Sicurezza di Windows"]
tags: ["Thunderbird 153.6", "Thunderbird 153.6.0esr", "aggiornamento di sicurezza Thunderbird", "vulnerabilità Thunderbird su Windows", "fuga NTLM Thunderbird", "autenticazione SMB Thunderbird", "CVE-2026-118174", "CVE-2026-118176", "MFSA 2026-122", "allegato di chiave OpenPGP", "allegato esterno", "blocco dei contenuti remoti", "URL mailbox", "percorso UNC esteso", "nome account Windows", "dati di autenticazione NTLM", "esposizione di credenziali SMB", "SMB in uscita", "porta TCP 445", "sicurezza della posta elettronica", "client di posta Windows", "verifica versione Thunderbird", "aggiornamento Thunderbird", "relay NTLM", "cracking delle password offline"]
cover: ""
coverAlt: ""
coverCaption: ""
---

Mozilla ha corretto due **gravi vulnerabilità che espongono credenziali Windows** in Thunderbird 153.6. Bastava visualizzare un’e-mail malevola per attivare una delle richieste di rete descritte in [MFSA 2026-122](https://www.mozilla.org/en-US/security/advisories/mfsa2026-122/). L’avviso descrive una possibile divulgazione di dati NTLM, non una compromissione confermata delle credenziali di ogni destinatario.

<!--more-->

## Punti chiave

- **CVE-2026-118174** riguardava un allegato di chiave OpenPGP ospitato esternamente. Visualizzare il messaggio avviava una richiesta senza intervento dell’utente, anche con i contenuti remoti bloccati.
- **CVE-2026-118176** riguardava un URL `mailbox:` appositamente creato con un percorso UNC esteso. Visualizzare il messaggio avviava una connessione SMB a un server scelto dal mittente.
- **Aggiorna Thunderbird su Windows** e verifica la versione installata. L’avviso indica Thunderbird 153.6 come versione corretta. Le note di rilascio di Thunderbird indicano la build corrispondente 153.6.0esr.

## Cosa attiva l’e-mail

**Le due vulnerabilità hanno punti di ingresso diversi.** Secondo le descrizioni di Mozilla, nessuna richiede che il destinatario faccia clic su un collegamento nell’e-mail. Il rischio per le credenziali Windows dipende dal fatto che la richiesta di rete raggiunga una condivisione controllata dall’aggressore e che avvenga lo scambio di autenticazione risultante. L’avviso di Mozilla non segnala uno sfruttamento attivo.

| Problema | Cosa si attiva quando si visualizza l’e-mail | Rischio per le credenziali Windows |
| --- | --- | --- |
| **CVE-2026-118174** | Thunderbird carica il contenuto di un allegato di chiave OpenPGP per offrire l’importazione della chiave. Il mittente lo contrassegna come allegato esterno con un URL scelto dall’aggressore. | Un URL a una condivisione di rete espone le credenziali NTLM dell’utente se la richiesta raggiunge la condivisione. |
| **CVE-2026-118176** | Un percorso UNC esteso aggira la restrizione di Thunderbird sulle condivisioni remote negli URL `mailbox:`. | Thunderbird si collega a un server SMB scelto dall’aggressore e divulga il nome dell’account Windows e dati di autenticazione NTLM. |

Per il percorso dell’**allegato OpenPGP**, Mozilla afferma esplicitamente che la richiesta aggirava il blocco dei contenuti remoti e non richiedeva alcun intervento dell’utente. Anche sui sistemi diversi da Windows, il problema consentiva una richiesta remota contraria all’impostazione dei contenuti remoti, ma Mozilla limita a Windows la fuga delle credenziali NTLM. Per il percorso dell’**URL `mailbox:`**, Mozilla afferma che gli altri sistemi operativi non sono interessati. Consulta le voci di [CVE-2026-118174](https://www.mozilla.org/en-US/security/advisories/mfsa2026-122/#CVE-2026-118174) e [CVE-2026-118176](https://www.mozilla.org/en-US/security/advisories/mfsa2026-122/#CVE-2026-118176).

**I dati di autenticazione NTLM non sono una password in testo in chiaro.** Mozilla afferma che i dati divulgati attraverso il percorso SMB comportano il rischio di cracking delle password offline o di attacchi relay. Ricevere un messaggio preparato non dimostra che un attacco sia riuscito. L’avviso elenca anche altre vulnerabilità di Thunderbird, compresi percorsi distinti per calendario e RSS. Questo articolo tratta i due percorsi attivati dalla visualizzazione dell’e-mail, senza assimilare tutti i problemi della versione.

## Verifica e aggiorna Thunderbird

Il flusso interessato è **la lettura della posta in Thunderbird su Windows** prima di installare la correzione pertinente. L’avviso di Mozilla indica **Thunderbird 153.6** come versione corretta, ma non specifica l’intero intervallo delle versioni precedenti interessate da questi due problemi. Le [note di rilascio 153.6.0esr](https://www.thunderbird.net/en-US/thunderbird/153.6.0esr/releasenotes/) indicano una build ESR pubblicata il 27 ottobre 2026. Non dedurre lo stato della patch di un altro canale, fork o pacchetto solo dall’etichetta della versione.

1. Su Windows, apri **Help > About Thunderbird**. Leggi la versione mostrata nella finestra About, che verifica anche la presenza di aggiornamenti. Le [istruzioni di aggiornamento di Mozilla](https://support.mozilla.org/en-US/kb/updating-thunderbird) descrivono questo percorso.
2. Se è disponibile un aggiornamento, lascia che Thunderbird lo scarichi, quindi seleziona **Restart Thunderbird to Update**. Riapri **Help > About Thunderbird** e conferma la versione installata dopo il riavvio.
3. Per la **linea 153 ESR**, confronta la versione ottenuta con **153.6.0esr** nelle note di Thunderbird. Se la tua organizzazione gestisce gli aggiornamenti, chiedi all’amministratore di verificare la correzione del fornitore invece di presumere che sia già installata.

> **Nota sulla versione:** le note di 153.6.0esr confermano che la release esiste, mentre MFSA 2026-122 collega le correzioni di sicurezza a Thunderbird 153.6. Le note non descrivono singolarmente queste due CVE. Consulta l’avviso per i dettagli delle vulnerabilità.

## Riduci l’esposizione durante l’aggiornamento

**Installa prima la correzione del fornitore.** Disattivare i contenuti remoti da solo non arresta CVE-2026-118174, perché la richiesta descritta aggirava l’impostazione. Il consiglio «non fare clic» non basta. Mozilla descrive richieste attivate dalla visualizzazione del messaggio.

Come **difesa in profondità**, limita l’SMB in uscita dai client Windows verso Internet, compresa la **porta TCP 445**, sul firewall aziendale o sui dispositivi gestiti. Le [indicazioni Microsoft sul traffico SMB](https://learn.microsoft.com/en-us/windows-server/storage/file-server/smb-secure-traffic) raccomandano di bloccare il TCP 445 in uscita verso Internet e limitare l’accesso ai file server necessari. Elenca le condivisioni necessarie prima di applicare una regola, soprattutto se l’ambiente usa un servizio file cloud o lavoratori remoti fuori dal perimetro. Questo controllo di rete limita il percorso SMB descritto, ma non ripara Thunderbird e non risolve tutti i problemi di richieste remote dell’avviso.

Se un computer Windows con una vecchia build di Thunderbird ha visualizzato un messaggio sospetto, **considera l’esposizione una questione da indagare, non una prova di compromissione**. Esamina con il team di sicurezza i registri disponibili delle connessioni SMB in uscita e dell’autenticazione. L’avviso del fornitore non fornisce un test di esposizione né un’istruzione generale di cambiare tutte le password.

## Fonti

- [Mozilla Foundation Security Advisory 2026-122: vulnerabilità corrette in Thunderbird 153.6](https://www.mozilla.org/en-US/security/advisories/mfsa2026-122/)
- [Note di rilascio Thunderbird Desktop: 153.6.0esr](https://www.thunderbird.net/en-US/thunderbird/153.6.0esr/releasenotes/)
- [Supporto Mozilla: aggiorna Thunderbird all’ultima versione](https://support.mozilla.org/en-US/kb/updating-thunderbird)
- [Microsoft Learn: proteggere il traffico SMB in Windows Server](https://learn.microsoft.com/en-us/windows-server/storage/file-server/smb-secure-traffic)
