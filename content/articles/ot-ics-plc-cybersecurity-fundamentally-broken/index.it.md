---
title: "Perché la sicurezza informatica di OT, ICS e PLC continua a non funzionare"
draft: false
toc: true
date: 2026-06-26
lastmod: 2026-11-22
description: "Scopri perché i controlli di sicurezza OT restano indietro rispetto alla progettazione legacy, ai vincoli operativi e ai percorsi reali degli attacchi."
tags: ["sicurezza OT", "sicurezza ICS", "sicurezza PLC", "sicurezza IoT", "cybersecurity industriale", "sicurezza SCADA", "NIST 800-82", "IEC 62443", "NERC CIP", "tecnologia operativa", "infrastrutture critiche", "sensori analogici", "isolamento di rete", "sistemi legacy", "opinione sulla cybersecurity", "sistemi di controllo industriale", "SCADA", "Stuxnet", "sicurezza dei sistemi di controllo", "sicurezza ciberfisica", "sicurezza della catena di fornitura", "catena di fornitura OT"]
cover: "/img/cover/ot-ics-plc-cybersecurity-fundamentally-broken.webp"
coverAlt: "Illustrazione che confronta un vecchio PLC con funzioni analogiche e un moderno controllore capace di supportare la sicurezza informatica e interfacce digitali, su sfondo scuro."
coverCaption: ""
---

Ho trascorso abbastanza tempo in ambienti industriali per dirlo con chiarezza: **la maggior parte dei programmi di sicurezza informatica OT, ICS e PLC è teatro**. Produce documentazione di conformità. Non produce sicurezza. È nello spazio tra le due cose che viene colpita l'infrastruttura critica.

Questo non è un attacco a chi scrive gli standard. **NIST SP 800-82 Rev 3**, **IEC 62443** e **NERC CIP** sono documenti tecnicamente validi. Il problema non sono le indicazioni. *Il problema è a quali sistemi si applicano.*

## I sistemi sono stati progettati per funzionare, non per essere protetti

**PLC, sistemi SCADA, sistemi di controllo distribuito (DCS) e hardware industriale IoT legacy** sono stati progettati per un solo scopo: funzionare in modo affidabile a lungo. **La disponibilità era l'unico obiettivo di progettazione degno di discussione.** Riservatezza, integrità, autenticazione e registrazione degli eventi non erano requisiti. In molti casi non erano nemmeno concetti presi in considerazione quando questi sistemi furono progettati.

NIST SP 800-82 Rev 3 (2023) lo ammette chiaramente. Descrive gli ambienti OT come sistemi con *«requisiti particolari di prestazioni, affidabilità e sicurezza»*, nei quali *«la sicurezza non può interferire con il funzionamento del sistema»*. Rileggilo. **Il principale documento di orientamento sulla sicurezza della tecnologia operativa riconosce esplicitamente che la sicurezza passa in secondo piano.** Non è un difetto del documento. È una descrizione accurata dell'ambiente.

Non puoi applicare il controllo degli accessi basato sui ruoli a un PLC che non conosce i ruoli utente. Non puoi correggere il firmware su hardware il cui produttore non esiste più. **I protocolli seriali legacy, tra cui Modbus RTU e Profibus DP, non offrono autenticazione nativa.** Trasmettono comandi e dati a chiunque li richieda. Non verificano chi li richiede.

*Le indicazioni sono valide. Spesso i sistemi non sono in grado di seguirle.* Sono problemi diversi.

## Esistono due categorie di sistemi OT completamente diverse

**I PLC legacy dagli anni Ottanta ai primi anni Duemila** sono stati progettati per funzionare isolati e con accesso solo fisico. Eseguono sistemi operativi proprietari. Spesso sono gestiti da workstation di ingegneria che si collegano anche alle reti aziendali. Le configurazioni sono archiviate in formati privi di verifica dell'integrità. Questi sistemi costituiscono una parte significativa dell'infrastruttura in esercizio nel trattamento dell'acqua, nella generazione di energia, nella produzione e nei trasporti.

**I controllori moderni con funzioni di sicurezza sono diversi.** Siemens, Schneider, Rockwell, Beckhoff e Phoenix Contact oggi distribuiscono piattaforme con avvio sicuro, firmware firmato, controllo degli accessi basato sui ruoli, identità supportata da TPM e comunicazioni cifrate. EtherNet/IP CIP Security, PROFINET Security Class e OPC UA con autenticazione sono disponibili sulle piattaforme hardware attuali.

Non sto sminuendo l'ingegneria moderna della sicurezza OT. I progressi sono reali. **Il problema è che la maggior parte dei sistemi installati non è moderna.** Quando si parla di «sicurezza informatica OT», di solito si descrive il tentativo di proteggere un controllore programmabile di vent'anni con un framework di sicurezza informatica scritto nel 2023. È questo il divario.

## Cosa funziona davvero

**La sicurezza fisica e l'isolamento della rete sono i controlli più affidabili per gli ambienti OT legacy.** Tutti i principali framework di sicurezza ICS affermano la stessa cosa. IEC 62443 organizza gli ambienti OT in zone di sicurezza con condotti definiti. L'obiettivo è costringere il movimento laterale a passare attraverso confini controllati, invece di attraversare una rete piatta.

L'isolamento della rete riduce notevolmente la superficie di attacco via rete. Non elimina ogni rischio. Supporti rimovibili, accesso interno, laptop di manutenzione, connessioni temporanee di ingegneria e compromissione della catena di fornitura sono percorsi documentati verso sistemi senza esposizione di rete. **Stuxnet**, arrivato agli impianti iraniani di centrifughe isolati dalla rete tramite unità USB infette, è l'esempio classico. *L'isolamento della rete è necessario. Non è sufficiente.*

**Il monitoraggio umano dei parametri del processo fisico** resta uno dei meccanismi di rilevamento più affidabili. Un operatore formato che osserva pressione, temperatura e portata in tempo reale rileva cose che nessun sistema di rilevamento delle intrusioni vedrà, perché l'IDS non può verificare se il valore digitale corrisponde alla realtà fisica.

Controlli che riducono il rischio nei contesti appropriati:

- **I diodi dati** consentono l'uscita della telemetria senza permettere connessioni in ingresso
- **Le liste di applicazioni consentite** sulle workstation HMI limitano ciò che viene eseguito sui sistemi con accesso ai sistemi di controllo
- **Le piattaforme passive di rilevamento delle anomalie** di Claroty, Dragos e Nozomi analizzano il traffico senza toccare le comunicazioni del piano di controllo
- **La segmentazione di rete** tra zone OT rallenta il movimento laterale senza richiedere un isolamento fisico completo
- **I principi zero trust**, citati in NIST SP 800-82 Rev 3, aggiungono requisiti di verifica per sessione ad alcune architetture OT moderne

*Nessuno di questi controlli risolve i vincoli di progettazione alla base del problema. Riducono il rischio ai margini di sistemi che non sono mai stati progettati per questo.*

## I segnali analogici non possono essere autenticati

**I loop di corrente da 4-20 mA, i segnali da 0-10 V, le uscite delle termocoppie e le letture RTD vengono trasmessi come segnali elettrici variabili.** Il segnale fisico non dispone di un meccanismo per verificarne l'autenticità. Chi applica il segnale giusto al cavo viene considerato attendibile.

Stuxnet lo ha dimostrato concretamente. L'attacco ha manipolato la logica PLC in esecuzione sui controllori Siemens S7 e, nello stesso tempo, ha riprodotto sulle interfacce operatore dati di processo normali registrati in precedenza. **Gli operatori guardavano schermate con valori normali mentre le centrifughe venivano spinte oltre i limiti operativi.** L'inganno è durato abbastanza da causare danni fisici che sembravano un guasto dell'apparecchiatura, non un attacco.

Le interferenze elettromagnetiche di cavi di alimentazione, azionamenti a frequenza variabile, fulmini e messa a terra scorretta alterano le misurazioni analogiche durante il normale funzionamento. IEC 61000 esiste per questo motivo. Gli impianti industriali usano cavi schermati, messa a terra adeguata, filtri e separazione fisica per gestire il problema.

I dispositivi di campo intelligenti moderni convertono internamente le misurazioni analogiche in formato digitale prima di trasmetterle tramite HART-IP, WirelessHART, EtherNet/IP CIP Security o OPC UA. L'hardware moderno supporta comunicazioni digitali autenticate a livello di dispositivo. **Il cavo analogico da 4-20 mA che collega un trasmettitore legacy a un ingresso PLC legacy non offre autenticazione e non potrà mai offrirla.** Una parte significativa della strumentazione installata usa ancora questo cavo.

## La validazione dei sensori è un controllo di sicurezza funzionale, non di sicurezza informatica

I sistemi di sicurezza di processo eseguono **votazioni ridondanti dei sensori**. Una configurazione 2 su 3, con due sensori che indicano 230 PSI e uno che indica 14 PSI, segnala il valore anomalo. Offre una resilienza limitata contro la manipolazione di un singolo sensore. *È un controllo di ingegneria della sicurezza funzionale, non un controllo di sicurezza informatica.*

I PLC standard non hanno una validazione crittografica dei loro ingressi analogici. Un generatore di segnale collegato al loop non si distingue da un trasmettitore legittimo. Il PLC legge la corrente e agisce di conseguenza.

**I sistemi strumentati di sicurezza dovevano essere l'ultima linea di difesa indipendente.** Nel 2017 **TRITON** (noto anche come **TRISIS**) ha preso di mira unità SIS Triconex di Schneider Electric con l'obiettivo specifico di disattivare quel livello. Gli aggressori hanno raggiunto il sistema di sicurezza tramite la rete delle workstation di ingegneria. *L'indipendenza del livello dipendeva da una separazione di rete che non era stata mantenuta.*

IEC 62443-3-3, IEC 62443-4-2 e il coordinamento con la sicurezza funzionale secondo IEC 61511 riflettono oggi questa lezione. Per anni gruppi diversi hanno trattato la sicurezza di processo e la sicurezza informatica come discipline separate. **TRITON ha dimostrato nella pratica ciò che analisi indipendenti sostenevano in teoria:** un aggressore che neutralizza il sistema di sicurezza prima di innescare la condizione pericolosa rimuove l'ultimo controllo che impedisce conseguenze fisiche.

## La catena di fornitura è un vettore che probabilmente stai ignorando

**La maggior parte dei programmi di sicurezza OT si concentra sull'architettura di rete. Molte compromissioni OT recenti hanno sfruttato punti d'ingresso che l'architettura di rete non blocca.**

I rischi della catena di fornitura OT includono:

- **L'integrità del firmware prima dell'installazione**, in particolare se l'hardware arriva dalla fabbrica o dal distributore con firmware non verificato
- **Le sessioni di accesso remoto dei fornitori**, che restano esposizioni persistenti nei siti che dipendono dal supporto del produttore
- **Le workstation di ingegneria** collegate sia alla rete aziendale sia alla rete OT, spesso per comodità operativa
- L'assenza di **elenchi dei materiali software (SBOM)** nella maggior parte delle implementazioni OT legacy, che rende quasi impossibile tracciare i componenti software
- **I tecnici di manutenzione** che portano laptop e unità USB in ambienti operativi isolati
- **Il supporto per gli aggiornamenti firmware firmati**, che manca sulla maggior parte delle piattaforme più vecchie

NIST SP 800-82 Rev 3 dedica sezioni specifiche alle dipendenze dai fornitori e all'accesso di terze parti. *Se l'isolamento della rete è intatto all'interno, ma il fornitore delle apparecchiature mantiene un portale di accesso remoto persistente alla rete di ingegneria, non hai una rete isolata. Hai una breccia con una porta controllata da qualcun altro.*

## Proteggere i sistemi legacy costa più del dovuto

Ogni programma PLC è scritto su misura per un processo specifico. La logica che gestisce il controllo delle sovratensioni di una raffineria è del tutto diversa da quella che gestisce una sequenza di clorazione per il trattamento dell'acqua o un regolatore di turbina. Non è una scelta. I processi fisici sono diversi.

**Proteggere i sistemi OT legacy costa spesso più del previsto** a causa dei requisiti di convalida ingegneristica, dei tempi di inattività necessari, dei vincoli di supporto dei fornitori, delle lacune nella documentazione e dei cicli di test che superano le stime iniziali. In alcuni casi con hardware senza supporto del fornitore, i costi di protezione si avvicinano o superano quelli di sostituzione del sistema.

**La conformità NERC CIP per gli asset informatici del sistema elettrico su vasta scala costa alle singole utility milioni di dollari ogni anno.** Un'indagine del 2019 dell'American Public Power Association ha documentato costi di conformità molto variabili, con oneri sproporzionati per le utility più piccole. Molti sistemi idrici e utility minori non rientrano nei requisiti NERC CIP e non affrontano obblighi di conformità comparabili.

## I sistemi dovrebbero essere sostituiti

**Sostituire i sistemi OT legacy è la risposta corretta.** Nei grandi impianti significa decine di milioni di dollari, lunghi periodi di transizione e il rischio di codificare in modo errato conoscenze operative complesse durante la migrazione. Sono costi e rischi reali.

Le indicazioni industriali di CISA e ICS-CERT raccomandano di applicare controlli compensativi mentre avanza la pianificazione della sostituzione. È una risposta razionale ai vincoli. *In parole semplici, riconosce che non è possibile ottenere una sicurezza completa sulle apparecchiature legacy. Applica i controlli adatti e pianifica la sostituzione futura.*

**La realtà è che molti di questi sistemi resteranno in servizio per decenni.** È un problema di finanziamenti e politiche. La comunità tecnica ha chiarito cosa serve. I budget operativi e i programmi di sostituzione non sono stati all'altezza.

## Aggiungere connettività di rete ai sistemi OT spesso peggiora la situazione

Molte organizzazioni hanno aggiunto funzioni di accesso remoto e monitoraggio ad ambienti OT originariamente isolati. L'argomento operativo è semplice: la visibilità remota riduce i tempi di risposta e il supporto dei fornitori è più rapido con una connessione remota. **La conseguenza per la sicurezza è che sistemi isolati senza una superficie di attacco remota ora ne hanno una.**

L'**incidente del 2021 nell'impianto idrico di Oldsmar** è avvenuto tramite una connessione di accesso remoto TeamViewer. L'aggressore ha modificato le impostazioni di dosaggio dell'idrossido di sodio usando uno strumento legittimo di accesso remoto aggiunto per comodità. L'**incidente Colonial Pipeline del 2021** è iniziato con la compromissione di una rete IT. L'operatore ha fermato preventivamente le operazioni della pipeline OT perché non poteva confermare che la rete OT fosse rimasta intatta. *L'attacco non ha violato direttamente la rete OT. L'incertezza su una possibile violazione ha causato l'interruzione.*

Aggiungere connettività di rete ai sistemi OT legacy per vantaggi operativi, senza progettarla secondo standard adeguati, **in molti casi genera più rischio di quanto giustifichi il vantaggio**. Il Modello Purdue resta un'utile architettura di riferimento, ma NIST non lo considera più sufficiente da solo. IIoT moderno, connettività cloud, operazioni remote e architetture ibride richiedono una progettazione più attenta della sola segmentazione in zone.

## La conformità agli standard scritti non è sicurezza

NIST SP 800-82 Rev 3, IEC 62443 e NERC CIP descrivono i controlli adatti a questi sistemi. Non li sto respingendo. Indico ciò che affermano esplicitamente: **non tutti i sistemi OT possono implementare ogni controllo.** I framework usano livelli di sicurezza graduati e disposizioni per controlli compensativi proprio perché i sistemi a cui si applicano spesso non riescono a soddisfare tutti i requisiti.

Il divario tra ciò che descrivono gli standard e ciò che può raggiungere una determinata installazione legacy non è un errore di documentazione. I sistemi non supportano quei controlli. Le indicazioni lo riconoscono. **Superare un audit di conformità su OT legacy non significa che l'ambiente sia sicuro.** Significa aver documentato i controlli compensativi presenti e averli fatti accettare da un auditor.

Il framework di gestione dei rischi NIST dichiara chiaramente che dopo l'applicazione dei controlli resta un rischio residuo. L'accettazione del rischio è uno dei quattro esiti del framework, insieme al trasferimento, alla riduzione e all'eliminazione del rischio. *Il riconoscimento del rischio residuo è parte integrante delle indicazioni ufficiali.* **Quando qualcuno sostiene che rispettare i requisiti di conformità rende sicuro il tuo ambiente OT, afferma qualcosa che i framework citati non supportano.**

## Cosa fare con OT legacy

Se gestisci ambienti OT legacy:

- **Tratta l'isolamento della rete come controllo principale** e verifica tutto ciò che attraversa il confine OT
- **Definisci un piano di protezione specifico per le workstation di ingegneria.** Collegano entrambi gli ambienti e sono spesso il punto d'ingresso
- **Controlla e registra tutti i supporti rimovibili** nelle aree OT
- **Verifica gli accessi remoti dei fornitori** e chiudi ogni sessione non in uso
- Implementa il monitoraggio ridondante dei sensori quando la progettazione del processo lo consente
- **Definisci un piano di sostituzione con stime di costo reali**, anche se la sostituzione è lontana anni
- **Smetti di considerare il completamento degli audit di conformità come un traguardo di sicurezza**

Se acquisti nuovi sistemi OT:

- **Inserisci i requisiti di sicurezza nelle specifiche di acquisto** prima che i fornitori rispondano
- Scegli piattaforme con supporto documentato per comunicazioni autenticate, aggiornamenti firmware firmati e controllo degli accessi basato sui ruoli
- **Progetta i confini IT/OT come condotti espliciti secondo IEC 62443**, non come una vaga regola del tipo "teneteli separati"
- **Richiedi SBOM per i componenti software OT** come requisito contrattuale

Il settore ha documentato bene il problema. Gli standard sono tecnicamente accurati. *I sistemi in uso spesso non possono ricevere ciò che gli standard prescrivono.* Riconoscerlo apertamente è il punto di partenza per decidere come gestire il rischio residuo.

## Riferimenti

- NIST SP 800-82 Rev 3: guida alla sicurezza della tecnologia operativa (OT) (2023)
- IEC 62443: serie sulla sicurezza dei sistemi di automazione e controllo industriale
- IEC 62443-3-3: requisiti di sicurezza dei sistemi e livelli di sicurezza
- IEC 62443-4-2: requisiti tecnici di sicurezza per componenti IACS
- IEC 61511: sicurezza funzionale per sistemi strumentati di sicurezza
- NERC CIP: standard di protezione delle infrastrutture critiche per il sistema elettrico su vasta scala
- IEC 61000: standard di compatibilità elettromagnetica
- Avvisi e buone pratiche CISA ICS-CERT
- Framework MITRE ATT&CK per ICS
- Analisi tecnica di Stuxnet, Langner Communications, 2011
- Analisi tecnica di TRITON/TRISIS, Dragos, 2017
- Revisione dell'incidente dell'impianto idrico di Oldsmar, CISA, 2021
- Indagine sui costi di conformità NERC CIP dell'American Public Power Association, 2019
