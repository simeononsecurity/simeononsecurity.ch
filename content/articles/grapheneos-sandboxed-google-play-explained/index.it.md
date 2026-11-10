---
title: "Google Play con sandbox su GrapheneOS: spiegazione"
date: 2026-09-11
lastmod: 2026-11-07
toc: true
draft: false
description: "Scopri cosa cambia con Sandboxed Google Play su GrapheneOS, quando è utile un profilo separato e come si collegano account, notifiche e compatibilità delle app."
genre: ["Privacy", "Sicurezza mobile", "Open source"]
tags: ["GrapheneOS", "sandboxed Google Play", "Google Play services", "Google Play Store", "privacy Android", "sicurezza Android", "sandbox delle app", "account Google", "profili GrapheneOS", "profilo proprietario", "profili utente", "profilo di lavoro", "compatibilità app", "notifiche push", "Firebase Cloud Messaging", "autorizzazioni app", "privacy Pixel", "installazione Google Play", "privacy mobile", "GrapheneOS App Store"]
cover: "/img/cover/grapheneos-sandboxed-google-play-explained.webp"
coverAlt: "Lo schermo di uno smartphone mostra app in scomparti trasparenti separati, tra cui un simbolo colorato di un app store."
coverCaption: ""
---

**Sandboxed Google Play** permette di installare i componenti ufficiali di Google Play su GrapheneOS come normali app. Funzionano senza i privilegi di sistema che Google Play riceve normalmente sul sistema operativo standard. L'installazione è facoltativa. [Panoramica delle funzioni di GrapheneOS](https://grapheneos.org/features#sandboxed-google-play).

## Punti chiave

- **Capisci l'isolamento:** distingui le autorizzazioni delle app dall'attività degli account online.
- **Raggruppa le dipendenze:** mantieni nello stesso profilo l'app dipendente e Play.
- **Verifica il comportamento:** controlla le notifiche in background e le funzioni essenziali.
- **Prepara un piano:** annota profili, account e requisiti delle app che hai scelto.

## Prima di iniziare

**Destinatari:** utenti GrapheneOS che decidono se installare Google Play e dove collocarlo. **Requisiti:** un dispositivo supportato con GrapheneOS aggiornato e accesso agli account essenziali. L'installazione del sistema operativo è descritta nella [guida all'installazione di GrapheneOS](/guides/how-to-install-graphine-os/).

**Tempo stimato:** 20–30 minuti per l'inventario iniziale delle app e le verifiche, oltre al normale uso quotidiano per valutare l'affidabilità delle notifiche. **Difficoltà:** principiante. Prova prima un'app rappresentativa e poi riorganizza il telefono.

## Cosa cambia con la sandbox

La **sandbox delle applicazioni** di Android separa le risorse delle app tramite le protezioni del sistema operativo. Un'app non ottiene accesso illimitato ai file privati di un'altra app. La protezione si applica sia al codice nativo sia a quello eseguito nell'ambiente gestito di Android. [Documentazione sulla sandbox delle applicazioni Android](https://source.android.com/docs/security/app-sandbox).

GrapheneOS aggiunge un **livello di compatibilità** che consente ai componenti ufficiali di Play di funzionare con queste restrizioni ordinarie. Le app nello stesso profilo hanno ancora modalità supportate per comunicare con il consenso reciproco. La sandbox limita i privilegi, ma non impedisce ogni scambio intenzionale tra app. [Progetto di Sandboxed Google Play](https://grapheneos.org/features#sandboxed-google-play).

| Aspetto | Significato pratico |
|---|---|
| **File privati delle app** | Installare Play non concede accesso illimitato ai dati delle altre app |
| **Autorizzazioni** | Esamina l'accesso richiesto come faresti con un'altra app |
| **Funzioni basate su Google** | Se un'app usa un servizio Google, continua a comunicare con quel servizio |
| **Attività dell'account** | Accedere a un servizio resta una decisione distinta sulla privacy |

**Sandbox e privacy dell'account** rispondono a domande diverse. Una sandbox limita l'accesso locale. Non cancella le informazioni che invii consapevolmente a un servizio online. Per esempio, accedere a un'app di acquisti continua a identificare il tuo account presso il gestore del servizio.

## Separa tre decisioni sulla privacy

**Accesso locale, uso dei servizi e identità** sono questioni distinte. Se un'app richiede accesso ai contatti e l'accesso a un account, valuta ogni richiesta separatamente:

| Decisione | Domanda |
|---|---|
| **Autorizzazione locale** | Questa funzione ha bisogno dei miei contatti, del microfono o della posizione? |
| **Dipendenza da un servizio** | Quale funzione dipende da Play services? |
| **Identità online** | A quale account collego questa attività? |

**Esempio pratico:** un account di acquisti contiene già il tuo indirizzo di consegna. Spostare l'app in un altro profilo non cambia l'indirizzo conservato dal venditore. Negare l'accesso ai contatti riguarda invece i dati disponibili sul telefono.

**Obiettivo di privacy:** annota l'esposizione specifica che vuoi ridurre. “Impedire a questa app di accedere ai miei contatti personali” è verificabile. “Rendere anonimo questo account” richiede decisioni ulteriori rispetto alla scelta del profilo.

## Profilo Proprietario o profilo separato?

**Installare nel profilo Proprietario** è una scelta supportata e semplice. Google Play resta nella sandbox. Un profilo utente o di lavoro separato ti permette di scegliere a quale gruppo di app rendere disponibile Play. [Indicazioni di installazione di GrapheneOS](https://grapheneos.org/usage#sandboxed-google-play-installation).

| Priorità | Configurazione iniziale | Compromesso |
|---|---|---|
| **Semplice uso quotidiano** | Mantieni le app necessarie e Play in Proprietario | Play è disponibile alle app che collaborano in questo profilo |
| **Separare le app dipendenti da Google** | Installale insieme in un altro profilo | Più gestione dei profili |
| **Evitare i servizi Google** | Inizia senza Play | Verifica le dipendenze di ciascuna app |

**La scelta del profilo** conta più che installare gli stessi componenti ovunque. Le FAQ di GrapheneOS spiegano che la disponibilità di Play è limitata ai profili selezionati. Molte app funzionano senza oppure lo richiedono solo per alcune funzioni. [FAQ sui servizi Google](https://grapheneos.org/faq#google-services).

*Usa un profilo separato quando la disponibilità selettiva di Play risolve un'esigenza concreta che hai individuato.*

## Capisci l'attività dei profili

**Un profilo utente secondario** ha le proprie istanze delle app e i propri dati. Passare a un altro utente e terminare la sessione dell'utente precedente sono azioni diverse. **Termina sessione** arresta le app nel profilo secondario e ripristina lo stato di inattività della memoria cifrata. [FAQ di GrapheneOS su cifratura e profili](https://grapheneos.org/faq#encryption).

**L'inoltro delle notifiche** può mostrare all'utente attivo le notifiche di un utente in esecuzione in background. Non mantiene attiva una sessione terminata. [Funzioni dei profili utente di GrapheneOS](https://grapheneos.org/features).

| Stato del profilo | Condizione di consegna |
|---|---|
| **Attivo** | Verifica la consegna in questo profilo |
| **In esecuzione in background** | Controlla l'inoltro all'utente attivo |
| **Sessione terminata** | Le app in questo profilo sono arrestate |

Per **un'app di messaggistica quotidiana**, decidi se è essenziale ricevere messaggi mentre usi Proprietario. Una configurazione che richiede frequenti arresti delle sessioni è incompatibile con la consegna continua in background. Valuta questo compromesso prima di spostare la cronologia delle conversazioni principali.

## Installazione e account

Apri il **GrapheneOS App Store** integrato, seleziona **Google Play services** e installalo. Verrà installato anche il Play Store, che ne dipende. Lascia che sia l'App Store a gestire questi componenti. Escludi Play services dall'ottimizzazione della batteria per rendere affidabili le funzioni in background, come le notifiche push. [Istruzioni ufficiali di installazione](https://grapheneos.org/usage#sandboxed-google-play-installation).

**Accedere con un account Google** è facoltativo per le funzioni che non dipendono da un account. Per installare app tramite il Play Store devi accedere. Le installazioni meno recenti includono anche Google Services Framework, che il progetto consiglia di mantenere. Segui le istruzioni di installazione aggiornate invece di una vecchia lista di tre pacchetti.

## Prova prima un'app

Usa un'**app rappresentativa a basso rischio** per verificare la configurazione dei profili che hai scelto. Durante la prova, mantieni disponibili i metodi di recupero degli account esistenti.

1. **Scegli un profilo:** decidi dove collocare l'app prima di installare le sue dipendenze.
2. **Installa Play:** segui in questo profilo i passaggi ufficiali indicati sopra.
3. **Installa l'app:** usa una fonte di distribuzione affidabile e completa la configurazione iniziale.
4. **Esamina le richieste:** approva le autorizzazioni adatte alla funzione che stai verificando.
5. **Prova una funzione:** invia un messaggio, apri una mappa o esegui un'altra azione reversibile.
6. **Registra il risultato:** annota la versione dell'app e del sistema operativo, il profilo e l'operazione esatta.

**Prova attesa:** una descrizione ripetibile come “un messaggio di prova è arrivato con lo schermo bloccato e il profilo attivo”. Evita di annotare solo “funziona”, perché non specifica la funzione e le condizioni verificate.

## Diagnostica delle notifiche mancanti

Le **notifiche push** dipendono dall'implementazione dell'app. Alcune app mantengono una propria connessione in background. Altre si affidano a Firebase Cloud Messaging di Google. Il fatto che un'app si apra non dimostra che le notifiche funzionino dopo aver bloccato il telefono. [FAQ di GrapheneOS sulle notifiche](https://grapheneos.org/faq#notifications).

**Controlla le condizioni di consegna** prima di modificare le autorizzazioni di più app:

| Sintomo | Restringi l'indagine |
|---|---|
| **I messaggi compaiono solo dopo l'apertura** | Controlla il metodo di consegna in background dell'app e le impostazioni della batteria |
| **La consegna funziona solo nel suo profilo** | Controlla l'attività del profilo e l'inoltro delle notifiche |
| **Nessuna consegna dopo Termina sessione** | Avvia il profilo secondario prima di riprovare |
| **La notifica arriva senza suono** | Controlla il canale di notifica e le impostazioni audio dell'app |

I **canali di notifica** raggruppano il comportamento delle notifiche di un'app, inclusi importanza e suono. Android offre controlli dei canali all'utente. [Documentazione sui canali di notifica Android](https://developer.android.com/develop/ui/compose/notifications/channels).

**Ripeti il test cambiando una condizione alla volta:** mantieni fissi il dispositivo mittente e il tipo di messaggio mentre cambi lo stato del profilo ricevente. Registra “attivo”, “in esecuzione in background” o “sessione terminata” per ogni risultato. Così distingui un problema del ciclo di vita del profilo da un problema di configurazione delle notifiche.

## Valuta le funzioni essenziali

Prima di affidarti a una nuova configurazione, esegui un breve **test personale di accettazione**:

| Flusso di lavoro | Verifica sul dispositivo |
|---|---|
| **Messaggistica** | Ricevi un messaggio con lo schermo bloccato |
| **Accesso all'account** | Accedi e completa il secondo fattore richiesto |
| **Servizi bancari o pagamenti** | Prova la funzione esatta che ti serve, inclusi eventuali controlli del dispositivo |
| **Navigazione** | Ottieni la posizione con le autorizzazioni scelte |

**L'avvio di un'app** è solo il primo controllo. Quando risolvi un problema, registra la versione dell'app e di GrapheneOS e l'operazione non riuscita. Questo articolo offre un quadro decisionale, non un elenco di compatibilità testate.

**Decisione di migrazione:** mantieni il metodo di accesso precedente finché ogni operazione essenziale non ha superato la prova. Un'app di messaggistica e una bancaria richiedono criteri di accettazione diversi. La consegna di un messaggio non dice nulla sui controlli dell'account o del dispositivo di un'altra app.

**Ripeti i controlli dopo gli aggiornamenti di GrapheneOS o delle app.** La posizione del profilo, le autorizzazioni, i canali di notifica e lo stato della sessione definiscono ancora il test. Registra la versione con ogni risultato per evitare conclusioni sulla privacy non supportate da cambiamenti nelle notifiche o nell'accesso.

Per **un accesso di lavoro**, prova l'intera sequenza di login e il secondo fattore richiesto. Per un'app di viaggio, prova la funzione che prevedi di usare fuori casa. Scegli azioni rappresentative senza effettuare acquisti superflui né modificare la sicurezza dell'account.

## Prepara il piano delle app

Completa questo **inventario** per le tue cinque app più importanti. Le righe sono suggerimenti, non affermazioni di compatibilità su prodotti specifici:

| Categoria dell'app | Requisito da registrare | Prova da raccogliere |
|---|---|---|
| **Messaggistica** | Consegna in background e scelta del profilo | Prova con schermo bloccato e profilo in background |
| **Accesso al lavoro** | Login richiesto e secondo fattore | Accesso completato |
| **Navigazione** | Autorizzazione alla posizione e necessità offline | Un percorso nelle condizioni previste |
| **Servizi bancari** | Operazioni essenziali supportate | Risultati per ogni funzione richiesta |
| **Acquisti** | Accesso all'account e ai dati locali | Esame delle autorizzazioni e normale uso dell'account |

**Prendi una decisione** per ogni riga: profilo scelto, dipendenza da Play, requisito dell'account, autorizzazioni approvate e alternativa. Segna come sconosciute le dipendenze non verificate. Così eviti di installare componenti aggiuntivi solo perché servivano a un'altra app.

**Esercizio di verifica:** un'app funziona mentre il profilo secondario è attivo, poi smette di ricevere messaggi dopo Termina sessione. Per prima cosa riavvia il profilo e riprova. Concedere l'accesso ai contatti non risolverebbe una sessione arrestata.

**Criterio di completamento:** il piano spiega perché ogni app si trova nel profilo scelto e quale prova giustifica il fatto di farvi affidamento. Rivedi la voce pertinente dopo un aggiornamento che modifica il comportamento.

## Prossimi passi

Se non hai installato il sistema operativo, usa la [guida all'installazione di GrapheneOS](/guides/how-to-install-graphine-os/). Poi scegli una configurazione dei profili e prova le app essenziali prima di aggiungere altri profili o modificare impostazioni generali delle autorizzazioni.
