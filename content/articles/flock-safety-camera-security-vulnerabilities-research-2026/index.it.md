---
title: "Vulnerabilità delle telecamere Flock Safety: oltre 50 falle individuate"
date: 2026-05-24
lastmod: 2026-11-15
toc: true
draft: false
description: "La ricerca sulle vulnerabilità delle telecamere Flock Safety analizza credenziali esposte, protezioni deboli, accesso fisico e limiti nella divulgazione delle falle."
genre: ["Ricerca sulla sicurezza", "Analisi delle vulnerabilità", "Tecnologie di sorveglianza", "Sicurezza informatica", "Tutela della privacy", "Sicurezza IoT", "Sicurezza fisica", "Sicurezza di rete", "Infrastrutture critiche", "Tecnologie governative"]
tags: ["Vulnerabilità Flock Safety", "Sicurezza ALPR", "Hacking delle telecamere", "Falle di sicurezza IoT", "Password hardcoded", "Vulnerabilità Android Things", "Exploit con accesso fisico", "Sicurezza di rete", "Errori di crittografia", "Violazioni della privacy dei dati", "Divulgazioni CVE", "Ricerca sulla sicurezza", "Ricerca GainSec", "Indagine di Ben Jordan", "Sicurezza delle telecamere di sorveglianza", "Falle nelle tecnologie governative", "Vulnerabilità critiche", "Divulgazione responsabile", "Analisi della cybersecurity", "Tecnologie delle forze dell'ordine", "Sicurezza pubblica", "Access point wireless", "Bypass dell'autenticazione", "Credenziali in chiaro", "Perdita RF", "Attacco TEMPEST", "Divulgazione di informazioni", "Accesso alla shell root", "Esecuzione di codice remoto", "Audit di sicurezza", "Valutazione delle vulnerabilità", "Rischio per la sicurezza nazionale", "Indagine del Senato", "Programma di ricompensa per bug", "Vulnerabilità zero-day", "Sviluppo di exploit", "Penetration test", "White paper sulla sicurezza", "Copertura di 404 Media", "Ricerca indipendente", "Sicurezza hardware", "Analisi del firmware", "Sfruttamento del sistema"]
cover: "/img/cover/flock-safety-camera-security-vulnerabilities-research-2026.webp"
coverAlt: "Una telecamera di sorveglianza ad alta tecnologia con riflessi blu e verdi su uno sfondo scuro. Forme e linee astratte la circondano e rappresentano le vulnerabilità della sicurezza digitale."
coverCaption: "Gravi falle di sicurezza espongono oltre 80.000 telecamere di sorveglianza ad accessi non autorizzati"
canonical: "https://simeononsecurity.com/articles/flock-safety-camera-security-vulnerabilities-research-2026/"
---

**Oltre 50 vulnerabilità critiche espongono la più grande rete privata di sorveglianza del Paese**

## Introduzione: una crisi di sicurezza nazionale

Tra la fine del 2024 e tutto il 2025, ricercatori indipendenti hanno scoperto quella che potrebbe essere **la più grave falla di sicurezza nella tecnologia di sorveglianza delle forze dell'ordine nella storia degli Stati Uniti**. Nei sistemi di telecamere Flock Safety sono state individuate **oltre 50 vulnerabilità critiche**. Le stesse telecamere fotografano e tracciano ogni giorno più di **150 milioni di veicoli**, nell'ambito di oltre **80.000 installazioni** in tutto il Paese.

Questo articolo presenta un'analisi tecnica completa delle vulnerabilità sulla base di:
- **Il white paper formale di GainSec**, "Examining the Security Posture of an Anti-Crime Ecosystem" (51 rilievi, 22 CVE assegnati, 8 in attesa)
- **L'inchiesta giornalistica di Ben Jordan** e i suoi test pratici di sicurezza
- **Le notizie di 404 Media** sui flussi delle telecamere esposti al pubblico
- **Le risposte ufficiali** di Flock Safety e dei senatori statunitensi
- **Le divulgazioni pubblicate** nel National Vulnerability Database (NVD)
- **Il dump del filesystem del settembre 2026**, pubblicato da Distributed Denial of Secrets, con analisi tecnica riga per riga di Micah Lee e un'inchiesta congiunta di WIRED e 404 Media

Per approfondire **perché esistono queste telecamere** e le **implicazioni per la privacy**, leggi: **[Telecamere di sorveglianza Flock Safety: diffusione, problemi di privacy e strategie di protezione](/articles/flock-safety-camera-surveillance-prevalence-privacy-protection-2026/)**

Per sapere **come rilevare queste telecamere**, consulta: **[Progetto di rilevamento Flock-You: guida hardware alla contro-sorveglianza](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/)**

______

## La portata del problema

### Dimensioni dell'infrastruttura vulnerabile

A maggio 2026:
- **Oltre 80.000 telecamere Flock Safety** installate negli Stati Uniti
- **Oltre 5.000 città e centri abitati** usano i servizi Flock
- **Oltre 3.500 forze dell'ordine** hanno accesso al sistema
- **Oltre 22.000 utenti delle forze dell'ordine** consultano le banche dati
- **Miliardi di punti dati** sono conservati in database consultabili

### Cronologia delle vulnerabilità

- **Fine 2024**: il ricercatore Jon "GainSec" Gaines scopre le prime vulnerabilità
- **Febbraio 2025**: inizia la divulgazione responsabile a Flock Safety
- **Aprile 2025**: vengono pubblicate le prime assegnazioni CVE
- **Novembre 2025**: pubblicazione del white paper formale con 51 rilievi
- **Dicembre 2025**: Ben Jordan mostra le vulnerabilità in un video
- **Gennaio 2026**: 404 Media trova oltre 60 flussi di telecamere accessibili pubblicamente
- **Febbraio 2026**: senatori USA chiedono alla FTC di avviare un'indagine
- **Maggio 2026**: il processo di divulgazione è ancora in corso

### Categorie di vulnerabilità

Le oltre 50 vulnerabilità ricadono in diverse categorie:
1. **Autenticazione e autorizzazione** (password hardcoded, assenza di MFA)
2. **Crittografia** (dati non cifrati a riposo e in transito)
3. **Sicurezza di rete** (access point Wi-Fi esposti, credenziali in chiaro)
4. **Sicurezza fisica** (exploit tramite pulsante, porte USB esposte)
5. **Privacy dei dati** (raccolta non autorizzata, conservazione prolungata)
6. **Progettazione del sistema** (software obsoleto, controlli di accesso insufficienti)
7. **Divulgazione di informazioni** (chiavi API esposte, flussi pubblici delle telecamere)

______

## Il dump del filesystem del settembre 2026

**Nel settembre 2026, l'organizzazione non-profit Distributed Denial of Secrets, impegnata per la trasparenza, ha pubblicato immagini complete del filesystem estratte da una telecamera Flock in servizio.** Un collettivo che si fa chiamare **stegan0gram** ha svitato l'hardware dal palo, copiato la memoria interna e pubblicato le immagini. **404 Media** e **WIRED** hanno condotto un'inchiesta congiunta, mentre il ricercatore di sicurezza **Micah Lee** ha pubblicato un'analisi tecnica del contenuto.

Tutti i rilievi precedenti di questo articolo provenivano da dispositivi di laboratorio o acquistati dai ricercatori. Questo insieme di dati proviene da una telecamera in servizio presso un comune, e costituisce la prova più solida pubblicata finora.

*La telecamera non è stata violata tramite rete. È stata rimossa fisicamente.*

### Contenuto del dump

La pubblicazione include immagini di tre partizioni, ognuna con una parte diversa della storia.

| Partizione | Dimensione | Perché è importante |
|-----------|------------|---------------------|
| **system** | 1,5 GB | Immagine Android con **19 app sviluppate da Flock**, tra cui `flock-sambuca`, `flock-collins` e `flock-phone-home` |
| **persist** | 32 MB | Credenziali del dispositivo in `flock/auth0/auth0_cred`, su una **partizione non cifrata che sopravvive al ripristino delle impostazioni di fabbrica** |
| **media** | 18 GB | Log e immagini in un contenitore la cui **chiave di decifratura si trova sulla stessa partizione** |

### Il problema delle credenziali, confermato

Il dump chiarisce se le credenziali hardcoded fossero solo teoriche o fossero usate in produzione. Sono in uso.

**Una chiave API che consente l'accesso al backend Flock è hardcoded nei binari delle applicazioni.** Il valore si trova in una classe chiamata `CameraSettings` all'interno di `com.flocksafety.android.common.lib`. Flock include la libreria condivisa in tutte e 19 le app, quindi la chiave è presente in ognuna. L'app `flock-sambuca` la usa durante il provisioning.

**Il flusso di autenticazione funziona così:**

1. Ogni telecamera richiede credenziali a un server Flock e si identifica tramite l'indirizzo **MAC**
2. Il servizio di accesso **Okta Auth0** di Flock restituisce un token `FlockAuth0Token` a breve durata
3. La telecamera memorizza le credenziali restituite **in chiaro**

L'ID e il segreto client di Auth0 si trovano sulla partizione **`/persist` non cifrata**, in un file progettato per sopravvivere al ripristino delle impostazioni di fabbrica. L'attaccante recupera prima la partizione persist, perché non è protetta.

La [vulnerabilità critica n. 4](#critical-vulnerability-4-hardcoded-credentials-throughout-system) descrive il problema più ampio dei segreti hardcoded nella piattaforma.

### La chiave di cifratura accanto alla serratura

Flock afferma che le telecamere sono protette dalla **cifratura sul dispositivo**. Il dump mostra come funziona in pratica.

La partizione media da 18 GB è contenuta in un archivio cifrato. La chiave di decifratura si trova sulla stessa partizione, in un file con estensione `.key`. Il collettivo stegan0gram ha recuperato la chiave, sbloccato il contenitore e letto il contenuto. **Le immagini sono cifrate come lo è una scatola chiusa quando la chiave è fissata al coperchio.**

I log recuperati hanno rivelato anche la posizione della telecamera. Le coordinate GPS compaiono **155 volte** nei log, concentrate in un raggio di circa 100 metri, una normale deriva per un ricevitore fissato a un palo. Le coordinate indicano **Wauwatosa, Wisconsin**, un sobborgo di Milwaukee, dove la telecamera era installata su N Mayfair Road. Micah Lee ha confrontato i log con Google Street View e identificato l'unità specifica tramite numero seriale e indirizzo MAC.

*La cifratura a riposo non serve a nulla se la chiave è conservata accanto al testo cifrato.*

### La risposta di Flock

La risposta di Flock ha ripetuto la posizione assunta in seguito ai precedenti rilievi GainSec. Un portavoce ha dichiarato:

> "Flock prende sul serio la sicurezza e mantiene una policy pubblica di divulgazione delle vulnerabilità, affinché i ricercatori possano segnalarci direttamente eventuali problemi. Non abbiamo ricevuto segnalazioni tramite questa procedura e, sulla base delle informazioni limitate fornite, non abbiamo dettagli sufficienti per valutare le affermazioni." 

È difficile conciliare questa risposta con la cronologia. Le vulnerabilità nel sistema operativo della telecamera erano state corrette pubblicamente nel **2018 e nel 2021**, e gli standard per la conservazione delle credenziali e la gestione delle chiavi non sono cambiati da molto prima della distribuzione del dispositivo. **Esaminare dieci anni di vulnerabilità pubbliche non richiede una segnalazione esterna.**

Flock ha inoltre definito illegale la rimozione e l'analisi della telecamera, come previsto dalla legge attuale, ma i risultati di sicurezza restano validi a prescindere da come è stato ottenuto l'hardware.

### Perché è più importante delle ricerche precedenti

Il white paper GainSec ha documentato 51 rilievi su dispositivi ottenuti legalmente. Flock ha contestato la gravità e sostenuto che servisse la vicinanza fisica.

Questo dump elimina tali riserve. Lo stato predefinito di una telecamera di produzione, senza modifiche degli operatori, include credenziali dell'infrastruttura in chiaro, chiavi conservate accanto ai dati che dovrebbero proteggere e un sistema operativo privo di patch di sicurezza da otto anni. **Non serviva alcun exploit. Bastava una chiave inglese.**

______

## La flotta dei dispositivi

Flock vende una linea di prodotti, non un solo modello, e le proprietà di sicurezza cambiano da un dispositivo all'altro. Le specifiche seguenti provengono dalle analisi GainSec e dall'analisi del firmware compilata dalla comunità che studia i dispositivi di rilevamento presso **[WiFi Mothership](https://wifimothership.com/flock)**.

| Dispositivo | Funzione | Piattaforma | Sistema operativo |
|---|---|---|---|
| **Falcon** | Telecamera ALPR a energia solare | Qualcomm MSM8953 (Snapdragon 625) / OpenQ 624A SoM | Android 8.1 |
| **Sparrow** | Telecamera ALPR cablata | Come Falcon | Android 8.1 |
| **Raven** | Rilevamento audio di spari e richieste di soccorso | ESP32-WROOM-32D con DSP Syntiant NDP120-B0 | FreeRTOS / ESP-IDF |
| **Bravo** | Unità di calcolo Edge AI | Qualcomm QCS6490 / TurboX QCS6490-U8B | **Android 13, kernel 5.4.180** |
| **Picard** | Unità di calcolo precedente | Dismessa a favore di Bravo | |
| **Condor** | Telecamera PTZ | Non documentata completamente | |
| **Alpha** | Drone autonomo | Progettato da Flock, conforme a NDAA | Autopilota proprietario |
| **Aerodome M350** | Drone precedente | DJI Matrice M350 / M300 RTK | Firmware DJI |
| **Rimorchio LPR (ATS-5)** | Piattaforma ALPR mobile | Telaio All Traffic Solutions con telecamera Flock | Come Falcon |
| **Wing** | Ponte software per telecamere di terze parti | Nessuna, integra telecamere IP esistenti | |

*Il divario generazionale salta subito all'occhio. L'unità di calcolo usa Android 13, mentre le telecamere a cui presta servizio usano Android 8.1, un sistema operativo uscito nel 2017.*

**Falcon è il dispositivo da tenere d'occhio.** Gestisce il lavoro ALPR, non è passato da Android 8.1 e salva i dati su una **memoria eMMC da 32 GB non cifrata**. La stessa memoria conteneva i file multimediali e i log recuperati dal collettivo stegan0gram. Sparrow usa la stessa piattaforma, ma è alimentata via cavo.

**Bravo è il caso opposto.** Un'unità di calcolo moderna con Android 13 e inferenza AI per i flussi delle telecamere dimostra che l'azienda è disposta a distribuire software aggiornato quando lo decide.

## Identificatori CVE verificati

Quindici CVE sono stati assegnati alle famiglie Falcon, Sparrow, Raven e Bravo. Ogni identificatore qui sotto è stato verificato nel **registro CVE.org** nel settembre 2026, invece di essere ripreso da una fonte secondaria.

### Rilevamento degli spari e dispositivi audio

| CVE | Rilievo | CVSS |
|-----|---------|------|
| **CVE-2025-47818** | Password hardcoded per una connessione | 2.2 |
| **CVE-2025-47819** | Interfaccia di debug sul chip senza controlli di accesso adeguati | 6.4 |
| **CVE-2025-47820** | Codice archiviato in chiaro | 2.0 |
| **CVE-2025-47821** | Password hardcoded per un sistema | 2.2 |

Tutte e quattro riguardano i dispositivi di rilevamento degli spari **precedenti alla versione 1.3**.

### Lettori di targhe

| CVE | Rilievo | CVSS |
|-----|---------|------|
| **CVE-2025-47822** | Interfaccia di debug sul chip senza controlli di accesso adeguati | 6.4 |
| **CVE-2025-47823** | Password hardcoded per un sistema | 2.2 |
| **CVE-2025-47824** | Codice archiviato in chiaro | 2.0 |

Queste tre vulnerabilità riguardano il firmware dei lettori di targhe **fino alla versione 2.2 compresa**.

### Difetti delle applicazioni presenti nell'intera flotta

| CVE | Rilievo | CVSS |
|-----|---------|------|
| **CVE-2025-59403** | L'app Collins espone endpoint amministrativi sulla **porta 8080 senza autenticazione**: `/reboot`, `/logs`, `/crashpack` e `/adb/enable`. L'ultimo avvia ADB via TCP senza conferma di debug e fornisce una shell a un attaccante sulla stessa rete | **9.8 CRITICO** |
| **CVE-2025-59407** | L'app DetectionProcessing include un keystore Java insieme alla sua **password hardcoded**; il keystore contiene una chiave privata | **9.8 CRITICO** |
| **CVE-2025-59405** | L'app Peripheral contiene una chiave API DataDog in chiaro | 7.5 |
| **CVE-2025-59409** | Il firmware di produzione Falcon e Sparrow include **credenziali Wi-Fi di sviluppo in chiaro** | 7.5 |
| **CVE-2025-59406** | L'app Pisco incorpora un **segreto client Auth0 in chiaro** | 6.2 |

### Unità di calcolo Bravo

| CVE | Rilievo | CVSS |
|-----|---------|------|
| **CVE-2025-59402** | Accetta il loader predefinito Thundercomm TurboX 6490 Firehose, consentendo il flashing del firmware e il dump delle partizioni | 5.4 |
| **CVE-2025-59404** | Viene distribuito con il bootloader sbloccato, aggirando Android Verified Boot | 7.5 |
| **CVE-2025-59408** | Viene distribuito con Secure Boot disabilitato | 7.3 |

**Quattro di queste vulnerabilità hanno un vettore di attacco di rete con un punteggio pari o superiore a 7,5, quindi non richiedono accesso fisico.** CVE-2025-59403 è l'identificatore assegnato al percorso API senza autenticazione e include la chiamata `/adb/enable`, che [la vulnerabilità critica n. 1](#critical-vulnerability-1-button-press-wireless-access-point) sfrutta per ottenere una shell root.

*I record CVE sono importanti anche per un altro motivo. Confermano il problema dei segreti in chiaro tramite registri indipendenti, e la pagina degli avvisi di sicurezza di Flock è citata come riferimento nei record Raven e LPR.*

______

## Vulnerabilità critica n. 1: access point wireless attivato da un pulsante {#critical-vulnerability-1-button-press-wireless-access-point}

### CVE-2025-59403

**Gravità**: CRITICA (CVSS 9.8)

### L'exploit

La vulnerabilità più allarmante consente a **chiunque abbia accesso fisico** a una telecamera Flock Safety di assumerne il controllo completo in meno di 60 secondi:

**Passaggio 1**: premi **tre volte** il pulsante sul retro della telecamera Falcon/Sparrow
**Passaggio 2**: il dispositivo crea un access point Wi-Fi aperto
**Passaggio 3**: connettiti alla rete Wi-Fi (la password hardcoded è documentata nel white paper GainSec)
**Passaggio 4**: invia il comando per abilitare ADB (Android Debug Bridge)
**Passaggio 5**: connettiti tramite ADB e ottieni una shell root

### Dettagli tecnici

```
Dispositivo: telecamera ALPR Flock Safety Falcon/Sparrow
Hardware: Android Things 8.0/8.1 (supporto terminato nel 2021)
Vettore di attacco: sequenza di pressioni fisiche del pulsante
Autenticazione: password WiFi codificata (uguale su tutti i dispositivi)
Impatto: compromissione completa del dispositivo, esfiltrazione dei dati e installazione di malware
```

### Cosa consente

Una volta ottenuto l'accesso alla shell, un attaccante può:
- **Estrarre tutte le immagini archiviate** (incluse quelle delle persone, non solo dei veicoli)
- **Modificare o eliminare le prove** presenti sul dispositivo
- **Installare malware persistente** (sopravvive al riavvio)
- **Clonare l'identità del dispositivo** per falsificarla
- **Intercettare e alterare** i flussi video
- **Usare il dispositivo come client botnet** per attacchi DDoS
- **Catturare le credenziali Wi-Fi** dei dispositivi vicini (attacchi honeypot)
- **Disattivare la telecamera** o provocare un denial of service

### Dimostrazione

Il ricercatore Ben Jordan ha mostrato l'exploit su YouTube, dimostrando:
- Connessione all'access point Wi-Fi in **meno di 30 secondi**
- Accesso alla shell root in **meno di 60 secondi complessivi**
- Accesso completo al filesystem, alle immagini archiviate e alla memoria di sistema
- Possibilità di installare applicazioni Android arbitrarie

**Citazione dalla dimostrazione**:
> "La password di quell'access point è [REDACTED], tutta in minuscolo. Ogni telecamera che abbiamo provato usa la stessa password hardcoded. Poi basta inviare un comando per abilitare ADB... ci vogliono probabilmente meno di 30 secondi per ottenere una shell completa e accesso totale al dispositivo."

### Risposta del fornitore

Inizialmente Flock Safety ha sostenuto che la vulnerabilità riguardasse solo **dispositivi non connessi al cloud**, paragonandoli a **"un iPhone rubato da un camion prima di essere connesso"**.

*Questa affermazione è stata smentita.* I ricercatori hanno riprodotto la vulnerabilità **su dispositivi connessi al cloud**, su diversi modelli di telecamera con la **stessa vulnerabilità** e su dispositivi provenienti da **fonti differenti**. Tutti presentavano il difetto.

______

## Vulnerabilità critica n. 2: sistema operativo Android obsoleto

### Da CVE-2025-47822 a CVE-2025-47824

**Gravità**: da MEDIA a BASSA (CVSS 6.4, 2.2 e 2.0)

### Il problema

Le telecamere Flock Safety usano **Android Things 8.0 o 8.1**, che:
- È stato **dismesso da Google nel 2021**
- **Non riceve aggiornamenti di sicurezza dal 2021**
- Conta **oltre 900 vulnerabilità pubblicate** nel 2026
- È **fuori supporto da oltre cinque anni**

### Analisi tecnica

**Sistema operativo**: Android Things 8.0/8.1
**Fine del supporto**: gennaio 2021
**Vulnerabilità note**: oltre 900
**Patch di sicurezza**: nessuna dopo la fine del supporto
**Dispositivi interessati**: Falcon, Sparrow, Condor e unità di calcolo Bravo

### Cosa mostra il dump del settembre 2026

Le immagini del filesystem pubblicate nel settembre 2026 indicano le versioni esatte di una telecamera in servizio, anziché di un dispositivo di laboratorio.

| Componente | Versione sulla telecamera | Stato |
|-----------|---------------------------|-------|
| **Android** | 8.1, build del 5 giugno 2025 | Livello patch di sicurezza **2018-06-05** |
| **Kernel Linux** | 3.18.71 | Rilasciato nel 2017; la serie 3.18 è terminata alla versione 3.18.140 nel maggio 2019 |
| **Versione Android attuale** | Android 17, giugno 2026 | Nove versioni principali più recente |

La build della telecamera è recente. **Il sistema operativo sottostante non lo è**, e il livello delle patch mostra che il dispositivo non riceve aggiornamenti di sicurezza Android da **otto anni**. Il kernel è indietro di **69 rilasci di patch** rispetto alla fine del proprio ramo di manutenzione, per oltre nove anni di correzioni mancanti.

### Due vulnerabilità presenti in questa build

Micah Lee ha individuato due falle note pubblicamente che interessano componenti presenti nella telecamera. Le date delle patch dimostrano che il firmware è antecedente a ogni correzione.

| CVE | Componente | Effetto | Patch |
|-----|------------|---------|-------|
| **CVE-2021-1905** | Driver GPU Qualcomm Adreno | Un use-after-free permette a **qualsiasi codice sul dispositivo, incluse app senza privilegi, di corrompere la memoria del kernel e assumerne il controllo completo** | Maggio 2021 |
| **CVE-2018-9568** "WrongZone" | Gestione dei socket nel kernel Linux | Un type confusion tramite IPv6 consente a un programma di **escalare i privilegi a root**. Esiste codice di exploit pubblico | Dicembre 2018 |

Entrambe le vulnerabilità erano state corrette anni prima della build del firmware della telecamera. **Nessuna richiede accesso fisico, perché il software già in esecuzione sul dispositivo può raggiungerle.** L'argomento della vicinanza usato da Flock per minimizzare i rilievi GainSec non si applica a nessuna delle due.

### Confronto con i dispositivi consumer

Per avere un termine di paragone:
- Il produttore di uno **smartphone** interrompe gli aggiornamenti dopo circa cinque anni e **smette di venderlo**
- Una **telecamera domestica** con software vecchio di cinque anni sarebbe considerata **criticamente insicura**
- Le agenzie governative richiedono software **aggiornato e supportato** per i sistemi sensibili

*Eppure Flock Safety continua a distribuire e vendere telecamere con software senza supporto del fornitore, privo di patch di sicurezza, contenente centinaia di exploit noti e destinato a elaborare dati sensibili delle forze dell'ordine.*

### Perché è importante

L'uso di **software fuori supporto** nei dispositivi di sorveglianza significa che:
- **Ogni vulnerabilità pubblicata di Android 8.x** funziona su queste telecamere
- Per molte vulnerabilità il **codice di exploit è disponibile al pubblico**
- Nessuna patch potrà mai correggere i **nuovi problemi scoperti**
- È impossibile rispettare normative come **FISMA, NIST e CMMC**

______

## Vulnerabilità critica n. 3: assenza di cifratura durante l'esecuzione

### CVE-2025-47824 e CVE-2025-59407

**Gravità**: da ALTA a CRITICA (CVSS da 2.0 a 9.8)

### Le dichiarazioni di Flock Safety e la realtà

**Il sito di Flock Safety dichiara**:
> "Dati e filmati sono cifrati per l'intero ciclo di vita"

**I risultati della ricerca indipendente** (GainSec e Ben Jordan):
> "Nella nostra ricerca non abbiamo decifrato né violato nulla. Tutto era in chiaro durante l'esecuzione."

*La distanza tra la dichiarazione promozionale e la realtà tecnica è totale.*

### Dati non cifrati

Esaminando i dispositivi, i ricercatori hanno trovato **non cifrati**:
1. **Filmati video e immagini archiviati**
2. **Dati delle targhe e metadati**
3. **Credenziali Wi-Fi e chiavi API**
4. **File di database con registri dei rilevamenti**
5. **Traffico di rete** (vedi vulnerabilità n. 6)
6. **Log di sistema con informazioni sensibili**

### Contraddizione sul periodo di conservazione dei dati

**Dichiarazione Flock Safety**: i dati vengono rimossi automaticamente dopo sette giorni
**Risultati dei ricercatori**: sono state trovate immagini risalenti alla **fabbricazione del dispositivo** (mesi o anni prima)

Estratto del white paper GainSec:
> "Abbiamo trovato immagini più vecchie di sette giorni. Alcune immagini archiviate erano state acquisite quando la telecamera era stata attivata all'interno della fabbrica in cui è stata costruita."

*Le policy sulla privacy dichiarate non vengono applicate sul dispositivo.*

### Implicazioni per la privacy

Questa assenza di cifratura comporta:
- **Il furto fisico del dispositivo** equivale a una violazione immediata dei dati
- **L'intercettazione della rete** espone dati in chiaro
- **Le minacce interne** possono esfiltrare facilmente i dati
- Le tutele dei **mandati** potrebbero non applicarsi a dati non cifrati
- **Violazioni di conformità** a numerose normative (HIPAA, CCPA ecc.)

______

## Vulnerabilità critica n. 4: credenziali hardcoded in tutto il sistema {#critical-vulnerability-4-hardcoded-credentials-throughout-system}

### CVE-2025-47818, CVE-2025-47821, CVE-2025-47823, CVE-2025-59407 e CVE-2025-59409

**Gravità**: CRITICA (CVSS fino a 9.8)

### Categorie di segreti hardcoded

I ricercatori di sicurezza hanno scoperto **numerose credenziali hardcoded**:

#### 1. Password degli access point Wi-Fi
- **Password universale** per tutte le telecamere Falcon/Sparrow
- Gli utenti e gli amministratori **non possono modificarla**
- **Nota ai ricercatori** e pubblicata nel white paper (con parti oscurate)
- **Confermata da CVE-2025-59409**: il firmware di produzione Falcon e Sparrow (build `OPM1.171019.026`) contiene **credenziali Wi-Fi di sviluppo in chiaro**

#### 2. Chiavi e token API
- **Hardcoded nel firmware** e nel codice delle app
- **Consentono l'accesso al backend** di vari servizi
- **Trovati tramite reverse engineering** degli APK Android
- **Confermati dal dump del settembre 2026**: una chiave API del backend è hardcoded in `CameraSettings` dentro `com.flocksafety.android.common.lib`, una libreria condivisa inclusa in **tutte le 19 app Flock** presenti sul dispositivo
- **L'ID e il segreto client Auth0 sono conservati nella partizione `/persist` non cifrata**, in `flock/auth0/auth0_cred`, un percorso progettato per sopravvivere al ripristino di fabbrica
- **Le credenziali restituite vengono salvate in chiaro** dopo che la telecamera si autentica al servizio Okta Auth0 di Flock usando il proprio indirizzo MAC

#### 3. Credenziali dei database
- **Database SQLite** senza protezione con password
- Credenziali **MySQL/PostgreSQL** nei file di configurazione
- **Accesso diretto al database** dalla shell locale

#### 4. Keystore crittografici
- **Confermato da CVE-2025-59407**: l'app DetectionProcessing include un keystore Java e la relativa password hardcoded; il keystore contiene una **chiave privata**
- **Gravità**: CRITICA (CVSS 9.8), perché il materiale della chiave viaggia insieme al binario che dovrebbe proteggerlo

#### 5. Nomi delle reti Wi-Fi
- Elenco delle reti preferite **hardcoded nel firmware**
- Consente attacchi tramite **access point fraudolenti** (vedi vulnerabilità n. 6)

#### 6. Credenziali dei servizi cloud
- **Token AWS/Azure** incorporati nel codice
- **Chiavi API di terze parti** (ArcGIS, servizi cartografici)
- **Token OAuth** mai ruotati

### Scenario di attacco: rete fraudolenta

Usando nomi di reti Wi-Fi hardcoded, i ricercatori hanno dimostrato questo attacco:

1. L'attaccante crea una **rete Wi-Fi falsa** con lo stesso SSID hardcoded
2. La telecamera **si collega automaticamente** (dà priorità alle reti hardcoded)
3. L'attaccante intercetta **tutto il traffico di rete** con un attacco man-in-the-middle
4. Estrae dal traffico le credenziali in chiaro
5. Ottiene **accesso ai sistemi backend**

**Non serve accesso fisico alla telecamera.** Basta trovarsi nel raggio del Wi-Fi.

______

{{< figure src="flock-safety-hardcoded-credentials-attack-vectors-diagram.webp" alt="Diagramma dei cinque vettori di attacco con credenziali hardcoded nelle telecamere Flock Safety: password Wi-Fi, chiavi API, credenziali di database e token dei servizi cloud" >}}

______

## Vulnerabilità critica n. 5: mancanza di autenticazione a più fattori

### Fallimento delle policy organizzative

**Gravità**: ALTA (organizzativa)

### La rivelazione

**Flock Safety non richiede 2FA/MFA** ad alcune forze dell'ordine, *le stesse che ogni giorno accedono ai dati di tracciamento di 150 milioni di veicoli.*

Citazione di un ricercatore di sicurezza:
> "Quando l'ho scoperto, non riuscivo a crederci. Il processo di sicurezza richiesto per accedere a Disney Plus è già troppo da chiedere ad alcuni dipartimenti di polizia che consultano informazioni riservate e la posizione di praticamente chiunque."

### Perché è importante

Senza MFA/2FA:
- **Una sola password compromessa** dà accesso completo al sistema
- Gli attacchi di **phishing** sono molto efficaci
- Funziona il **credential stuffing** basato su altre violazioni
- Le **minacce interne** sono più facili da realizzare
- I **dispositivi rubati** danno accesso immediato

### Confronto

Requisiti di sicurezza per sistemi **meno sensibili**:
- **Disney+**: 2FA disponibile
- **Gmail**: 2FA predefinita per i nuovi account
- **Servizi bancari**: 2FA obbligatoria per legge
- **Social media**: 2FA standard

Requisiti di sicurezza per il **tracciamento quotidiano di oltre 150 milioni di veicoli**:
- **Flock Safety**: 2FA facoltativa (alcune agenzie non la usano)

### La risposta di un senatore statunitense

Il rilievo è stato evidenziato in particolare nella **lettera del senatore Wyden** che chiedeva un'indagine FTC, citando come prova che Flock Safety aveva:
> "esposto inutilmente i dati personali sensibili degli americani al furto da parte di hacker e spie straniere"

### Una soluzione semplice

Le **chiavi di sicurezza USB/NFC** costano **10-25 dollari** e offrono:
- Autenticazione **resistente al phishing**
- **Nessuna app o codice aggiuntivo** necessario
- Conformità agli standard **FIDO2/WebAuthn**
- **Semplicità d'uso** (inserisci la chiave o avvicina il dispositivo)

*Se è "troppa fatica" per il personale delle forze dell'ordine, **non dovrebbe avere accesso** ai sistemi di sorveglianza nazionale.*

______

## Vulnerabilità critica n. 6: traffico di rete in chiaro

### Identificatore in attesa di assegnazione

**Gravità**: ALTA (CVSS 7.8 stimato dai ricercatori)

**A questa categoria non è stato assegnato un identificatore CVE.** Il record assegnato più vicino, CVE-2025-59406, include la classificazione CWE-319 relativa alla trasmissione in chiaro, ma riguarda un segreto Auth0 incorporato, non l'intercettazione del traffico in transito. I risultati presentati in questa sezione si basano ancora sulle pubblicazioni dei ricercatori citate sopra.

### La vulnerabilità

Quando si collegano alle reti (LTE o Wi-Fi), le telecamere trasmettono dati **senza una cifratura adeguata**:

**Traffico interessato**:
- Immagini e testo delle targhe
- Metadati dei rilevamenti
- Log di sistema
- Dati di configurazione
- Credenziali (in alcuni casi)

### Vettore di attacco n. 1: rete Wi-Fi fraudolenta

I ricercatori hanno dimostrato che è possibile:
1. Rimuovere la SIM della telecamera **oppure** configurare una rete falsa con l'SSID hardcoded
2. Attendere che la telecamera si colleghi al Wi-Fi fraudolento
3. Catturare il traffico con **Wireshark** o un analizzatore di pacchetti simile
4. Analizzarlo con strumenti come **NetworkMiner** o **Unblo**
5. Estrarre **credenziali in chiaro** e dati sensibili

Citazione della ricerca GainSec:
> "Ho catturato per un po' i dati pcap trasmessi da una di queste telecamere e li ho analizzati con Wireshark e Unblo... e ho trovato proprio credenziali in chiaro nei dati."

### Vettore di attacco n. 2: IMSI catcher / Stingray

Un attacco più sofisticato non richiede vicinanza fisica:
1. Usa un **IMSI catcher** (un dispositivo Stingray fai-da-te) o un SDR professionale
2. **Dirottare la connessione LTE** fingendoti una torre cellulare
3. La telecamera si collega alla **stazione radio base fraudolenta**
4. Intercetta **tutto il traffico** con un attacco man-in-the-middle
5. Estrai credenziali, immagini e metadati

**Non serve accesso fisico.** L'attacco funziona da **centinaia di piedi** di distanza.

### Potenziale degli attacchi Tempest moderni

La trasmissione in chiaro consente anche **attacchi in stile Tempest**, in cui:
- Si possono intercettare le emissioni RF della telecamera
- Il flusso video può essere **ricostruito da remoto**
- La tecnica ricorda i metodi della CIA **durante la Guerra fredda**
- Le moderne apparecchiature SDR la rendono **accessibile agli appassionati**

______

## Vulnerabilità critica n. 7: flussi pubblici delle telecamere esposti

### Scoperta del gennaio 2026

**Gravità**: CRITICA (CVSS 10.0 - esposizione completa del sistema)

### La scoperta

Nel gennaio 2026, Ben Jordan e **404 Media** hanno scoperto che con **semplici ricerche Google** era possibile trovare:
- **Oltre 60 interfacce amministrative Flock Safety completamente esposte**
- **Nessuna richiesta di nome utente o password**
- **Flussi video in diretta** e 30 giorni di filmati archiviati
- Accesso al pannello di **controllo completo delle telecamere**

### Cosa era accessibile

Da queste interfacce esposte chiunque poteva:
- **Guardare i flussi video in diretta**
- **Rivedere 30 giorni** di filmati archiviati
- **Scaricare video** direttamente
- **Controllare le telecamere PTZ** (panoramica/inclinazione/zoom) sulle unità Condor
- **Vedere percorsi e hash dei file** delle prove
- **Eliminare prove** con un solo clic
- **Modificare le impostazioni della telecamera**
- **Visualizzare numeri seriali e posizioni dei dispositivi**

### Violazioni della privacy osservate

Ben Jordan ha documentato immagini di:
- **Una famiglia che caricava un neonato in auto** nel parcheggio di Lowe's
- **Un uomo che usciva di casa** la mattina a New York
- **Una donna che correva da sola** su un sentiero boschivo in Georgia
- **Una coppia che litigava** a un mercato all'aperto di Atlanta (l'AI ha ingrandito i volti automaticamente)
- **Un agente e un'ambulanza** che prestavano assistenza durante una crisi di salute mentale in Iowa
- **Bambini che giocavano** in un parco giochi della Bay Area californiana
- **Un uomo su un'altalena** in un parco vuoto, in un momento privato

Citazione di Ben Jordan:
> "Mi viene la nausea anche solo a dirlo. Ma sto cercando di mostrarvi solo una frazione delle informazioni che chiunque nel mondo con accesso a un motore di ricerca commerciale ha potuto ottenere su chiunque sia stato a questo mercato o abbia camminato su questo sentiero negli ultimi 31 giorni."

### Capacità di individuazione e tracciamento

Le telecamere Condor PTZ esposte includono funzionalità di tracciamento basate su **AI**:
- **Ingrandiscono automaticamente** le persone
- **Seguono gli individui** mentre si muovono
- **Rilevano e mettono a fuoco gli smartphone** (per leggere gli schermi)
- **Tracciano più obiettivi** contemporaneamente
- **Registrano continuamente** senza supervisione

### Potenziale di doxxing

Ben Jordan ha mostrato quanto sia facile risalire all'identità da filmati esposti:
> "In due minuti di intelligence open source usando un servizio commerciale di riconoscimento facciale, ho scoperto che una delle persone aveva appena finito la facoltà di medicina e che l'altra soffriva di sindrome dell'intestino irritabile cronica. La coppia ha anche avuto un bambino l'anno scorso... so inoltre che ha guidato per oltre 45 minuti dal suo indirizzo in periferia."

Incrociando i dati con:
- Servizi di **riconoscimento facciale**
- Profili dei **social media**
- Database di **registri pubblici**
- Informazioni da **violazioni di dati** (Park Mobile ecc.)
- **Registri delle chiamate di emergenza** (molte città li pubblicano)

Risultato: **deanonimizzazione completa in pochi minuti**

______

{{< figure src="flock-exposed-camera-feed-ptz-ai-tracking-privacy-violation-overview.webp" alt="Schema che mostra come le telecamere PTZ Flock Safety esposte con tracciamento automatico AI consentivano l'accesso pubblico ai video in diretta di persone in parchi, sentieri e parcheggi" >}}

______

## Vulnerabilità critica n. 8: raccolta non autorizzata dei dati

### Contraddizione con le dichiarazioni pubbliche

**Gravità**: ALTA (implicazioni di privacy e legali)

### Le dichiarazioni di Flock Safety

**Dichiarazione sul sito ufficiale**:
> "Flock Safety non acquisisce né registra dati sulle persone, solo sui veicoli"

### I risultati della ricerca indipendente

**Cosa fanno realmente le telecamere**:
1. Il **rilevamento del movimento** attiva la telecamera **per qualsiasi movimento**, non solo dei veicoli
2. L'**AI cerca una targa** nell'immagine
3. **Se non trova targhe**, l'immagine **viene comunque archiviata** (non eliminata)
4. Una cartella separata conserva le immagini senza targa
5. **Le immagini vengono acquisite e conservate** di **persone, pedoni e ciclisti**

*L'affermazione "solo veicoli" è falsa. La telecamera salva le immagini di chiunque le passi davanti.*

### Osservazioni verificate

I ricercatori hanno documentato telecamere che acquisivano:
- **Una persona che passava** davanti alla telecamera (immagine archiviata)
- **Una mano che salutava** l'obiettivo (immagine archiviata)
- **Una scrivania o un oggetto spostato** vicino alla telecamera (immagine archiviata)
- **Operai della fabbrica** durante la produzione (conservati per mesi)

Citazione di GainSec:
> "Quando mi sono messo davanti alla telecamera, il modulo radar ha attivato quello della telecamera per scattarmi una foto. Poi l'AI integrata ha cercato una targa e non l'ha trovata, ma ha comunque salvato l'immagine in una cartella separata."

### Implicazioni legali

Questa raccolta non autorizzata dei dati potrebbe:
- **Violare le policy sulla privacy dichiarate** (pratiche ingannevoli)
- **Violazione dei contratti di appalto** (se le città hanno specificato "solo veicoli")
- **Comportare violazioni GDPR/CCPA** (cittadini UE, residenti in California)
- **Invalidare gli accordi di consenso**
- **Esporre l'azienda a cause legali** per pubblicità ingannevole

### Espansione della sorveglianza

Le telecamere **Condor PTZ** (installate nel 2025-2026) sono **progettate esplicitamente** per tracciare le persone:
- **Rilevamento delle persone basato sull'AI**
- **Zoom automatico** sui volti
- **Tracciamento** mentre le persone si muovono
- **Nessuna opzione di esclusione**
- Spesso installate in **parchi, sentieri e stazioni di trasporto**

*È una enorme estensione, dai "lettori di targhe" alla sorveglianza della popolazione generale, senza modifiche alle policy, nuovi contratti né avvisi pubblici.*

______

## Vulnerabilità critica n. 9: porte USB esposte agli attacchi Rubber Ducky

### Sfruttamento dell'accesso fisico

**Gravità**: ALTA (con accesso fisico)

### La vulnerabilità

Le **unità di calcolo Bravo** e alcuni modelli di telecamera hanno:
- **Porte USB-C esposte** all'esterno
- **Nessuna protezione fisica** (guarnizioni del case)
- **Esecuzione automatica** dei dispositivi USB
- **Nessuna autenticazione** richiesta

### Attacco Rubber Ducky / BadUSB

Un **dispositivo BadUSB** (costo: 5-15 dollari):
- Si presenta al sistema come **tastiera USB**
- **Esegue script preprogrammati** (payload)
- Si avvia **automaticamente** quando viene collegato
- **Non richiede interazione dell'utente**

### Scenario di attacco

GainSec ha mostrato che è possibile:
1. Avvicinarsi a un dispositivo Flock installato
2. Collegare il **dispositivo BadUSB** alla porta esposta
3. Il dispositivo esegue il payload (script)
4. Il payload installa **malware persistente**
5. L'attaccante **si allontana**
6. Il malware **contatta il server di comando** tramite LTE/Wi-Fi

**Tempo complessivo**: meno di 30 secondi

### Cosa possono fare i payload

Gli script automatizzati possono:
- **Abilitare l'access point wireless** (senza premere i pulsanti)
- **Installare una backdoor** per l'accesso remoto
- **Esfiltrare dati** a un server remoto
- **Modificare filmati** o prove
- **Disattivare la telecamera** o causare un DoS
- **Aggiungere il dispositivo a una botnet** per attacchi DDoS
- **Catturare credenziali** da altri sistemi

### Perché è importante

Con **oltre 80.000 telecamere**, spesso installate in **zone semirurali** con **visibilità limitata**:
- L'**accesso fisico** è relativamente semplice
- **Non ci sono guardie** né monitoraggio costante
- Sono fissate con **semplici fascette stringitubo**
- Spesso sono montate a **circa 2,1 metri da terra** (raggiungibili con uno sgabello)

Citazione di Ben Jordan:
> "Queste telecamere non sono fortezze impenetrabili. Sono telecamere Android di plastica e unità di calcolo montate a circa 2,1 metri da terra con fascette stringitubo."

______

{{< figure src="badusb-rubber-ducky-flock-camera-usb-exploit-attack-chain.webp" alt="Schema di un attacco che mostra come un dispositivo BadUSB collegato alla porta USB esposta di una telecamera Flock Safety può installare malware persistente in meno di 30 secondi" >}}

______

## Vulnerabilità critica n. 10: chiavi API esposte pubblicamente

### Scoperta di un ricercatore OSINT

**Gravità**: CRITICA (CVSS 9.5)

### La scoperta

Nel 2025, il **ricercatore OSINT Joshua Michael** ha individuato:
- **Un sito demo Flock Safety esposto**, trovato tramite Google dorking
- **5.000 righe di codice sorgente** visibili
- **Una chiave API attiva** incorporata nel codice
- **Accesso a oltre 50 layer geospaziali** privati

### Accesso fornito dalla chiave API

La chiave **ArcGIS** esposta consentiva l'accesso a:

**1. Dati di registrazione**
- Nomi dei clienti
- Indirizzi e-mail
- Numero di telecamere per sede
- Funzioni di allegato file

**2. Posizioni delle auto di pattuglia in tempo reale** (diversi dipartimenti)
- Tracciamento GPS in tempo reale dei veicoli di polizia
- Installazione di Aurora, Colorado
- Dipartimento di polizia di Carrollton
- **Rischio per la sicurezza nazionale**

**3. Informazioni personali degli agenti**
- Nomi e numeri di telefono
- Indirizzi e-mail
- Aree di pattuglia previste
- Giurisdizioni di appartenenza

**4. Database degli avvisi delle liste di veicoli ricercati** (Dallas, Texas)
- **6.000 record** di veicoli segnalati
- Targhe e motivi della segnalazione
- Luoghi e orari dei rilevamenti
- ID delle telecamere che hanno acquisito i veicoli
- **Cinque mesi di tracciamento degli spostamenti**

Citazione di Joshua Michael:
> "Chiunque avrebbe potuto cercare su Google e trovare questa mappa, poi tracciare per cinque mesi gli spostamenti di queste persone. Aggiungo che nella categoria del motivo c'è qualcuno indicato semplicemente come 'sospetto', e molti altri non hanno alcuna ragione o hanno il campo vuoto."

### Superficie di attacco

Le chiavi API esposte consentono:
- **Perseguitare veicoli specifici**
- **Compromettere la sicurezza degli agenti** (indirizzi di casa e schemi di pattugliamento)
- **Violazioni della sicurezza operativa** (dove si trova o non si trova la polizia)
- **Intimidire i testimoni** (tracciando chi ha segnalato crimini)
- Raccogliere **informazioni criminali per la criminalità organizzata**

### Contesto della violazione: Flax Typhoon

Poche settimane prima di questa scoperta, il gruppo di hacker **Flax Typhoon**, **sponsorizzato dallo Stato cinese**, aveva compromesso ArcGIS, secondo i ricercatori di sicurezza Alexa Feminina e James Zhang.

Citazione di InfoSecurity Magazine:
> "Gli hacker avrebbero preso di mira un'applicazione ArcGIS legittima e accessibile al pubblico... usata per il ripristino dopo disastri, la gestione delle emergenze e altre funzioni critiche."

**Questo significa che stati ostili avrebbero potuto accedere a** posizioni dei veicoli di polizia, identità degli agenti, collocazione delle telecamere di sorveglianza e schemi di risposta alle emergenze.

______

## Altre vulnerabilità (riepilogo di oltre 50 falle)

### Vulnerabilità 11-51

Il white paper GainSec documenta **41 ulteriori rilievi**, tra cui:

**Difetti di progettazione del sistema**:
- Modalità debug abilitata nel firmware di produzione
- Avvio non sicuro che consente la compromissione del bootloader
- Assenza di elemento sicuro o TPM per le chiavi
- Meccanismo di aggiornamento firmware prevedibile

**Problemi di autenticazione**:
- I token di sessione non scadono mai
- Nessuna restrizione di accesso basata su IP
- Credenziali condivise tra i dispositivi
- Nessun certificate pinning

**Sicurezza di rete**:
- Porte aperte con servizi di debug
- Telnet abilitato su alcune unità
- Server FTP con credenziali deboli
- Vulnerabilità DNS rebinding

**Privacy e conservazione dei dati**:
- Immagini conservate oltre il periodo dichiarato
- Metadati mai eliminati
- Raccolta di dati per il riconoscimento facciale
- Tracciamento della posizione anche oltre i veicoli

**Sicurezza fisica**:
- Involucri facili da smontare
- Interfacce seriali esposte
- Porte di debug JTAG accessibili
- Nessun sigillo antimanomissione

**Errori crittografici**:
- Generazione di numeri casuali debole
- Chiavi di cifratura hardcoded
- MD5 ancora usato nella catena hash
- Validazione dei certificati disabilitata

**Divulgazione di informazioni**:
- Messaggi di errore dettagliati rivelano informazioni interne
- Elenco delle directory abilitato sui server web
- Commenti nel codice sorgente con credenziali
- Backup di configurazione leggibili da tutti

### Stato dei CVE

A maggio 2026:
- **22 CVE assegnati** e pubblicati
- **8 CVE in attesa** di assegnazione MITRE
- **21 rilievi** non inviati per un CVE (a discrezione del ricercatore)
- **Tutti i rilievi** documentati nel white paper GainSec

Dettagli tecnici completi: [github.com/GainSec/anti-crime-ecosystem-research](https://github.com/GainSec/anti-crime-ecosystem-research)

______

## La risposta di Flock Safety

### Dichiarazioni ufficiali

**Post sul blog di novembre 2025**:
> "Flock si impegna a migliorare continuamente la sicurezza... Nessuna delle vulnerabilità descritte nel rapporto influisce sulla capacità dei clienti di raggiungere i propri obiettivi di sicurezza pubblica."

**Affermazione**: le vulnerabilità richiedono accesso fisico e "conoscenze approfondite"

**Controprove**:
- Per trovare i flussi esposti bastava una **ricerca Google**
- Gli exploit wireless richiedevano solo la **vicinanza**
- L'esposizione della chiave API era **interamente remota**
- Dopo la divulgazione, le password hardcoded erano **note a tutti**

### Contestazione dei dispositivi di ricerca

Inizialmente Flock ha affermato che i dispositivi usati per la ricerca:
> "Non erano connessi al cloud... come un iPhone rubato da un camion prima di essere connesso"

*È stato dimostrato che era falso.* I ricercatori hanno testato **dispositivi connessi al cloud** e ottenuto risultati identici. Le telecamere accessibili al pubblico mostravano le **stesse vulnerabilità**, e 404 Media ha trovato **oltre 60 telecamere di produzione esposte**.

### Risposta ai ricercatori

GainSec ha riferito che i tentativi di divulgazione responsabile hanno incontrato:
- **Bug bounty con NDA** (per impedire la divulgazione)
- **Nessuna conferma** delle correzioni
- **Dichiarazione PR** rilasciata prima della finestra di 90 giorni
- **Nessun riconoscimento** del ricercatore nel comunicato
- **Perdita del lavoro** per il ricercatore entro 48 ore dalla pubblicazione del video

Ben Jordan ha riferito:
- **Visite della polizia** alla sua proprietà
- **Investigatori privati sospetti** che fotografavano casa sua
- **Molestie da parte dei vicini**
- Minacce di **diffida e cessazione** da parte di Flock Safety

Citazione di Ben:
> "Non considero queste cose conseguenze o punizioni per aver studiato le vulnerabilità di sicurezza. Le considero conseguenze e punizioni per averlo fatto in modo etico e trasparente."

### Distribuzione continua

*Nonostante tutto questo*, Flock Safety:
- **Continua a vendere** dispositivi vulnerabili
- **Non rilascia aggiornamenti firmware** che risolvano le cause profonde
- **Continua a usare** Android Things 8.x (fuori supporto dal 2021)
- **Non impone MFA** alle forze dell'ordine

______

## Risposte legislative e politiche

### Richiesta d'indagine del Senato USA

**Febbraio 2026**: i senatori **Ron Wyden** (Oregon) e **Raja Krishnamoorthi** (Illinois) hanno inviato una lettera formale alla FTC chiedendo un'indagine.

**Estratto della lettera**:
> "Flock ha esposto inutilmente i dati personali sensibili degli americani al furto da parte di hacker e spie straniere."

**Motivazioni citate**:
- Rischi per la sicurezza nazionale
- Dichiarazioni ingannevoli sulla privacy
- Pratiche di sicurezza inadeguate
- Mancanza di requisiti MFA

### Iniziative dei consigli comunali

**Denver, Colorado**:
- Il consiglio comunale ha **votato contro** il rinnovo del contratto Flock (dicembre 2025)
- Ha citato il **"disprezzo per onestà e responsabilità"** di Flock
- Il sindaco ha **annullato la decisione** tramite un "accordo dietro le quinte" (gennaio 2026)
- Le proteste pubbliche continuano

**Evanston, Illinois**:
- Ha scoperto che **l'ICE usava le telecamere** senza consenso
- Ha votato per **rimuoverle**
- *Flock le ha reinstallate senza autorizzazione*
- La città usa fondi pubblici per **coprirle con teli** e avviare azioni legali

**Oakland, California**:
- Ha rinviato il voto sull'**espansione da 2,25 milioni di dollari**
- Ha commissionato un audit di sicurezza indipendente
- Ha giudicato **ingannevoli** le affermazioni di Flock sull'efficacia

### Richieste di accesso ai documenti pubblici

Diverse città stanno conducendo indagini basate su:
- Ricerca di sicurezza pubblicamente disponibile
- Richieste FOIA per i contratti Flock
- Requisiti di audit indipendenti
- Pressione delle organizzazioni locali

______

## Analisi tecnica: scenari reali di attacco

### Scenario 1: sorveglianza da parte di uno Stato

**Attore della minaccia**: servizio d'intelligence straniero

**Obiettivo**: tracciare funzionari governativi

**Metodo**:
1. Usare un IMSI catcher per intercettare il traffico LTE della telecamera
2. Estrarre dal flusso credenziali in chiaro
3. Accedere al backend con chiavi API compromesse (o tramite il layer ArcGIS esposto in precedenza)
4. Cercare nel database veicoli registrati presso strutture governative
5. Tracciare gli spostamenti di funzionari e militari

**Tempo necessario**: giorni (una volta predisposta l'infrastruttura)
**Probabilità di rilevamento**: bassa (il C2 cifrato imita traffico legittimo)

### Scenario 2: contro-sorveglianza della criminalità organizzata

**Attore della minaccia**: organizzazione dedita al traffico di droga

**Obiettivo**: individuare i percorsi di pattugliamento della polizia

**Metodo**:
1. Acquistare un dispositivo BadUSB (15 dollari)
2. Raggiungere le telecamere nella zona operativa
3. Collegare il BadUSB alla porta USB esposta (30 secondi)
4. Il payload disattiva la telecamera o modifica i filmati
5. In alternativa, il payload esfiltra le posizioni dei veicoli della polizia su un server remoto

**Tempo necessario**: 30 secondi per telecamera
**Probabilità di rilevamento**: bassa (sembra attività legittima del dispositivo)

### Scenario 3: stalker o autore di violenza domestica

**Attore della minaccia**: ex partner abusante

**Obiettivo**: seguire gli spostamenti della vittima

**Metodo**:
1. Ottenere la targa della vittima (informazione pubblica)
2. Cercare su Google un'interfaccia Flock esposta (vulnerabilità del gennaio 2026)
3. Consultare 30 giorni di filmati e cercare il veicolo
4. Incrociare i dati con database pubblici (indirizzo di lavoro, casa ecc.)
5. Ricostruire abitudini e orari

**Tempo necessario**: da minuti a ore
**Probabilità di rilevamento**: zero (non esistono log di autenticazione)

### Scenario 4: manomissione delle prove

**Attore della minaccia**: imputato in un processo penale

**Obiettivo**: distruggere le prove prima del processo

**Metodo**:
1. Scoprire la posizione della telecamera tramite le prove del mandato
2. Raggiungere fisicamente la telecamera (sequenza di pressione del pulsante)
3. Ottenere una shell root
4. Aprire la cartella delle prove
5. Eliminare immagini/video specifici o modificare i timestamp

**Tempo necessario**: meno di cinque minuti
**Probabilità di rilevamento**: bassa (a meno che la telecamera non venga sottoposta ad analisi forense prima dell'accesso della difesa)

### Scenario 5: attivista per la privacy o giornalista

**Attore della minaccia**: attivista per la trasparenza

**Obiettivo**: documentare gli eccessi della sorveglianza

**Metodo**:
1. Usare dispositivi di rilevamento (vedi la nostra [guida hardware Flock-You](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/))
2. Mappare le telecamere della comunità
3. Presentare richieste FOIA sulle policy dei filmati
4. Dimostrare le vulnerabilità al consiglio comunale
5. Promuovere la rimozione o la supervisione

**Tempo necessario**: continuo
**Probabilità di rilevamento**: alta (attività pubblica)

______

{{< figure src="flock-camera-attack-scenario-threat-actor-matrix-nation-state-crime.webp" alt="Matrice che confronta cinque scenari reali di attacco alle telecamere Flock Safety: sorveglianza statale, contro-sorveglianza criminale, stalking, manomissione delle prove e attivismo per la privacy" >}}

______

## Come difendersi da queste vulnerabilità

### Per le forze dell'ordine

**Azioni immediate**:
1. **Richiedere MFA/2FA** per tutti gli utenti (chiavi di sicurezza USB)
2. **Verificare ogni mese i log di accesso** per individuare query non autorizzate
3. **Limitare la condivisione** alle sole giurisdizioni necessarie
4. **Isolare la rete**: telecamere su VLAN dedicate
5. **Proteggere fisicamente i dispositivi**: sigilli antimanomissione e sorveglianza
6. **Preparare un piano di risposta agli incidenti** di compromissione

**Requisiti contrattuali**:
1. **Audit di sicurezza regolari** condotti da aziende indipendenti
2. **Aggiornamenti firmware obbligatori** entro 30 giorni dal rilascio delle patch
3. **Notifica CVE** entro 24 ore
4. **Archiviazione cifrata delle prove** con chiavi gestite dal cliente
5. **Penali SLA** in caso di violazione della sicurezza
6. **Diritto di audit** delle strutture e del codice del fornitore

**Strategia a lungo termine**:
1. **Piano di transizione** dai sistemi operativi fuori supporto
2. **Infrastruttura self-hosted** (minore dipendenza dal cloud)
3. **Valutazione delle alternative open source**
4. **Trasparenza verso la comunità** su posizioni e policy delle telecamere

### Per Flock Safety (raccomandazioni)

**Priorità critica** (immediata):
1. **Disabilitare la creazione dell'access point wireless** tramite pressione del pulsante
2. **Imporre MFA** a tutti gli account, senza eccezioni
3. **Ruotare tutte le credenziali hardcoded** nell'intero sistema
4. **Applicare una patch d'emergenza** alle interfacce pubbliche esposte
5. **Cifrare i dati a riposo** con gestione corretta delle chiavi

**Priorità alta** (30 giorni):
1. **Migrare a un sistema operativo supportato** (Android 12+ o Linux)
2. **Programma bug bounty** senza NDA
3. **Audit di sicurezza indipendente** e pubblicazione dei risultati
4. **Cifrare il traffico di rete end-to-end**
5. **Migliorare la sicurezza fisica** (rimuovere le USB esposte, rinforzare gli involucri)

**Priorità media** (90 giorni):
1. **Ripensare interamente il sistema di autenticazione**
2. **Secure boot** con firmware verificato
3. **Integrare un modulo di sicurezza hardware**
4. **Certificazioni di conformità** (FedRAMP, SOC 2, ISO 27001)
5. **Dashboard di sicurezza per i clienti** con avvisi di violazione

**A lungo termine** (1 anno):
1. **Aprire il codice dei componenti di sicurezza** per creare fiducia
2. **Programma di test avversariali** (red team)
3. **Requisiti per i ruoli di ingegneria della sicurezza**
4. **Integrare la sicurezza nell'SDLC** (DevSecOps)
5. **Partecipare agli standard di settore** (OWASP, CIS)

### Per le persone

**Strategie di protezione**:
1. **Usare dispositivi di rilevamento** (vedi la nostra [guida hardware](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/))
2. **Mappare le telecamere** della propria zona
3. **Variare percorsi e orari** per ridurre l'analisi degli schemi
4. **Chiedere supervisione e trasparenza** al consiglio comunale
5. **Presentare richieste FOIA** sui propri dati (dove consentito dalla legge)
6. **Sostenere leggi sulla privacy** statali e federali

**Misure OpSec**:
1. **Evitare veicoli unici** (marca, modello e colore comuni)
2. Usare **veicoli differenti** per attività sensibili (dove legale)
3. Scegliere **trasporti alternativi** (bici, trasporto pubblico, camminare)
4. Usare **copritarga per la privacy** (solo se legali nella giurisdizione)
5. Usare **borse Faraday** per i telefoni quando la correlazione è un rischio

{{< stscollective-ad "flockyou" >}}

______

{{< figure src="flock-safety-security-remediation-priority-roadmap.webp" alt="Roadmap di priorità delle correzioni immediate, a 30 e 90 giorni e a lungo termine che Flock Safety dovrebbe introdurre per risolvere le vulnerabilità critiche" >}}

______

## Il gruppo di ricerca

### GainSec (Jon "GainSec" Gaines)

**Esperienza**: professionista di sicurezza offensiva, oltre 10 anni di esperienza

**Contributo**:
- Ha scoperto **47 vulnerabilità su 51**
- Ha pubblicato un **white paper formale** con dettagli tecnici
- Ha coordinato la **divulgazione responsabile** con Flock Safety
- Ha registrato **30 CVE** (22 pubblicati, 8 in attesa)
- Ha creato la **checklist Defender** per i professionisti della sicurezza

**Contatto**: whitepaper@gainsecmail.com
**Ricerca**: [github.com/GainSec/anti-crime-ecosystem-research](https://github.com/GainSec/anti-crime-ecosystem-research)
**Blog**: [gainsec.com](https://gainsec.com)

### Ben Jordan (Benn Jordan)

**Esperienza**: giornalista, musicista, investigatore tecnologico

**Contributo**:
- **Documentazione video** delle vulnerabilità
- **Dimostrazioni pubbliche** per i giornalisti (The Guardian, 404 Media)
- Scoperta di **oltre 60 flussi di telecamere esposti** tramite Google
- **Attività di sensibilizzazione ed educazione pubblica**
- **Coordinamento legislativo** con gli uffici dei senatori

**Contatto**: tramite il canale YouTube
**Lavoro**: YouTube - Benn Jordan

### Joshua Michael (Next AI)

**Esperienza**: specialista OSINT, ricercatore di privacy

**Contributo**:
- Scoperta di **chiavi API esposte** tramite Google dorking
- Documentazione dell'**esposizione dei layer ArcGIS**
- **Metodologia OSINT** per seguire la ricerca
- **Correlazione di dati** con violazioni pubbliche

**Organizzazione**: Next AI - società d'intelligence all-source

### Collaboratori

- **404 Media** - giornalismo investigativo e divulgazione pubblica
- **The Guardian** - copertura internazionale
- **Lucy Parsons Labs** - anni di advocacy e ricerca sull'ALPR
- **Sassy South** - organizzazione della comunità
- **DeFlock / Will Freeman** - progetto di mappatura delle telecamere
- **Ed Vogel** - analisi legale e politica

______

## Considerazioni etiche

### Cronologia della divulgazione responsabile

La comunità di sicurezza ha seguito le migliori pratiche di **divulgazione responsabile**:

**Protocollo standard**:
1. Scoprire la vulnerabilità
2. **Notificare privatamente il fornitore con 90 giorni di anticipo**
3. Il fornitore sviluppa e distribuisce una patch
4. **Divulgazione pubblica** dopo la patch o dopo 90 giorni (a seconda di quale evento avvenga prima)
5. Analisi dettagliata per aiutare la difesa

**Cosa è successo realmente**:
1. GainSec ha scoperto le vulnerabilità (fine 2024)
2. **Ha contattato ripetutamente** Flock Safety (da febbraio 2025)
3. Flock ha offerto un **bug bounty con NDA** (per zittire la divulgazione)
4. Flock ha rilasciato **in anticipo una dichiarazione PR** senza riconoscere il ricercatore
5. **Nessuna conferma** dell'applicazione delle patch
6. GainSec ha proceduto alla **divulgazione pubblica** dopo le finestre di 90 giorni
7. Ben Jordan e 404 Media hanno **verificato indipendentemente** i sistemi di produzione

### Ritorsioni contro i ricercatori

GainSec e Ben Jordan hanno riferito:
- **Perdita del lavoro** o difficoltà professionali
- **Visite della polizia** alle abitazioni private
- **Sospetta sorveglianza** delle case e delle proprietà
- **Molestie da parte dei vicini**
- Minacce di **diffida e cessazione**
- **Attacchi sui social media** (il CEO di Flock li ha definiti "terroristi")

Questo **effetto dissuasivo** sulla ricerca di sicurezza:
- Scoraggia la divulgazione delle vulnerabilità
- Ritarda le correzioni critiche
- Danneggia la sicurezza pubblica
- Viola le norme etiche della comunità di sicurezza

*La risposta di Flock Safety ai ricercatori che hanno seguito i protocolli di divulgazione crea un precedente pericoloso per l'intera comunità di ricerca sulla sicurezza.*

Citazione di Ben Jordan:
> "Non ho il tempo di dedicare altri mesi a un'altra vulnerabilità Flock Safety, ma come vedete questa è urgente e, francamente, temo che sia già sfruttata."

### Interesse pubblico

Questi ricercatori hanno agito **nell'interesse pubblico**:
- **Hanno seguito** i protocolli di divulgazione responsabile
- **Hanno avvisato prima il fornitore** della divulgazione pubblica
- **Hanno oscurato i dettagli sensibili** che avrebbero facilitato l'exploit
- **Hanno fornito indicazioni difensive** ai professionisti
- **Hanno promosso cambiamenti politici** tramite i canali appropriati
- **Hanno accettato rischi personali** per informare il pubblico

Senza il loro lavoro:
- **Oltre 80.000 telecamere vulnerabili** sarebbero rimaste senza interventi
- **Oltre 150 milioni di scansioni giornaliere dei veicoli** sarebbero rimaste senza protezione
- **Milioni di americani** sarebbero stati esposti senza saperlo
- La **sicurezza nazionale** sarebbe stata compromessa
- **Non sarebbe in corso alcuna azione legislativa**

______

## Conclusione: la strada da seguire

{{< figure src="flock-safety-vulnerability-disclosure-timeline-2026.webp" alt="Cronologia del processo di divulgazione delle vulnerabilità Flock Safety dal 2024 al 2026, dalla scoperta iniziale alla divulgazione responsabile e all'esposizione ancora non corretta" >}}

### Situazione attuale (maggio 2026)

- **Oltre 50 vulnerabilità critiche** documentate e divulgate in parte
- **Oltre 80.000 telecamere** ancora in servizio con falle non corrette
- Il fornitore non ha attuato una **correzione completa**
- **Azione normativa limitata** (richiesta un'indagine FTC, ma non è stata avviata)
- **Rischio continuo di sfruttamento** per la sicurezza nazionale e la privacy individuale

### Cosa deve accadere

**A livello di settore**:
1. **Audit di sicurezza obbligatori** prima delle installazioni governative
2. **Test indipendenti** da parte di terzi qualificati
3. **Pubblicazione dei risultati degli audit**
4. **Responsabilità dei fornitori** per le falle di sicurezza
5. **Conformità agli standard** (NIST, ISO ecc.)

**Per Flock Safety**:
1. **Patch d'emergenza immediate** per le vulnerabilità critiche
2. **Migrazione del sistema operativo** a una piattaforma supportata
3. **Riconoscimento pubblico** della portata del problema
4. **Risarcimento** per i ricercatori coinvolti
5. **Rapporti di trasparenza** sullo stato della sicurezza

**Per le forze dell'ordine**:
1. **Requisiti di sicurezza** nei contratti d'acquisto
2. **Audit regolari** dei sistemi installati
3. **MFA obbligatoria** per tutti gli utenti
4. **Piani di risposta agli incidenti**
5. **Trasparenza pubblica** sui programmi di sorveglianza

**A livello legislativo**:
1. **Standard federali** per le tecnologie di sorveglianza
2. **Divulgazione obbligatoria delle vulnerabilità** alle parti interessate
3. **Tutele per i whistleblower** e i ricercatori di sicurezza
4. **Rimedi civili** per le violazioni della privacy
5. **Meccanismi di supervisione** dei sistemi di sorveglianza

### Il quadro generale

Questo caso rappresenta **più di un problema di Flock Safety**. È emblematico di:
- Un'**industria della sorveglianza** che antepone la crescita alla sicurezza
- **Acquisti governativi** senza competenze tecniche adeguate
- **Affermazioni dei fornitori** non verificate né contestate
- **Incentivi finanziari** non allineati alla sicurezza pubblica
- **Lacune normative** nella supervisione delle tecnologie emergenti

*Ogni città che firma un contratto Flock senza una verifica di sicurezza indipendente accetta questi rischi per conto dei residenti.*

### Invito all'azione

**Per i professionisti della sicurezza**:
- **Sostenere la divulgazione responsabile**
- **Contribuire agli strumenti di sicurezza open source**
- **Promuovere la protezione dei ricercatori**

**Per le forze dell'ordine**:
- **Chiedere responsabilità ai fornitori**
- **Richiedere audit di sicurezza** prima dell'installazione
- **Implementare subito MFA**
- **Consultare la comunità di sicurezza**

**Per i responsabili politici**:
- **Approvare leggi** che impongano standard di sicurezza
- **Finanziare audit indipendenti** delle tecnologie di sorveglianza
- **Proteggere whistleblower** e ricercatori
- **Creare organismi di supervisione** con competenze tecniche

**Per il pubblico**:
- **Informarsi sulla sorveglianza** nella propria comunità
- **Partecipare alle riunioni comunali** in cui si discutono i contratti
- **Sostenere le organizzazioni** che promuovono la trasparenza
- **Contattare i rappresentanti** per esprimere le proprie preoccupazioni
- **Usare strumenti di rilevamento** per mappare la sorveglianza (vedi la nostra [guida hardware](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/))

### Letture correlate

- **[Telecamere di sorveglianza Flock Safety: diffusione, problemi di privacy e strategie di protezione](/articles/flock-safety-camera-surveillance-prevalence-privacy-protection-2026/)** - approfondisci il contesto della sorveglianza
- **[Progetto di rilevamento Flock-You: guida hardware alla contro-sorveglianza](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/)** - costruisci il tuo dispositivo di rilevamento

Aspettare che il settore corregga queste falle non è una strategia di protezione. **I [dispositivi di rilevamento FlockYou](https://stscollective.com/collections/flockyou-alpr-flock-safety-awareness-devices)** di STS Collective funzionano già oggi; il codice **SIMEONONSECURITY** offre fino al 20% di sconto.

{{< centerbutton href="https://stscollective.com/discount/SIMEONONSECURITY" >}}
  Acquista i rilevatori FlockYou e risparmia il 20%
{{< /centerbutton >}}

______

## Riferimenti

1. [Ricerca GainSec sull'ecosistema anticrimine - GitHub](https://github.com/GainSec/anti-crime-ecosystem-research)
2. [White paper GainSec - Zenodo DOI: 10.5281/zenodo.17529423](https://zenodo.org/records/17584876)
3. [Blog GainSec - analisi tecniche informali](https://gainsec.com/)
4. [Risposta ufficiale di Flock Safety - novembre 2025](https://www.flocksafety.com/blog/response-to-compiled-security-research-on-flock-safety-devices)
5. [404 Media - flussi di telecamere Flock esposti](https://www.404media.co/)
6. [YouTube di Ben Jordan - dimostrazioni delle vulnerabilità](https://www.youtube.com/@BennJordan)
7. [National Vulnerability Database](https://nvd.nist.gov/)
8. [Database CVE MITRE](https://cve.mitre.org/)
9. [Electronic Frontier Foundation - sorveglianza ALPR](https://www.eff.org/issues/automated-license-plate-readers)
10. [Lettera del senatore Wyden alla FTC](https://www.wyden.senate.gov/)
11. [Lucy Parsons Labs - ricerca ALPR](https://lucyparsonslabs.com/)
12. [Progetto DeFlock - mappatura delle telecamere](https://deflockproject.org/)
13. [Distributed Denial of Secrets - immagini del filesystem della telecamera ALPR Flock](https://ddosecrets.org/article/flock-alpr-camera)
14. [Micah Lee - le telecamere Flock sono piene di vulnerabilità e credenziali hardcoded](https://micahflee.com/flock-cameras-are-riddled-with-security-vulnerabilities-and-hard-coded-credentials/)
15. [WIRED e 404 Media - gli hacker sono entrati in una telecamera Flock](https://www.wired.com/story/hackers-flock-camera-data-shows-how-system-works/)
16. [Hackaday - questa settimana in sicurezza: le telecamere Flock sono vecchie](https://hackaday.com/2026/09/18/this-week-in-security-flock-cameras-are-old-microsoft-patches-patches-and-researchers-attack-ssh/)
17. [NVD - CVE-2021-1905, use-after-free nella GPU Qualcomm Adreno](https://nvd.nist.gov/vuln/detail/CVE-2021-1905)
18. [NVD - CVE-2018-9568, type confusion dei socket nel kernel Linux](https://nvd.nist.gov/vuln/detail/CVE-2018-9568)
19. [WiFi Mothership - rilevamento ALPR Flock Safety e riferimenti sui dispositivi](https://wifimothership.com/flock)
20. [CVE.org - ricerca dei record del programma CVE](https://www.cve.org/)
21. [Avviso di sicurezza Flock Safety - rilevamento degli spari e lettori di targhe](https://www.flocksafety.com/articles/gunshot-detection-and-license-plate-reader-security-alert)
22. [GainSec - Fly By Device 2: RCE wireless Falcon e Sparrow](https://gainsec.com/2025/09/27/fly-by-device-2-the-falcon-sparrow-gated-wireless-rce-camera-feed-dos-information-disclosure-and-more/)
23. [GainSec - Root from the Coop Device 3: shell root nell'unità di calcolo Bravo Flock Safety](https://gainsec.com/2025/09/19/root-from-the-coop-device-3-root-shell-on-flock-safetys-bravo-compute-box/)
