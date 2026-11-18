---
title: "La corsa al rilevamento delle telecamere Flock: cosa è cambiato nel 2026"
date: 2026-09-10
lastmod: 2026-11-13
toc: true
draft: false
description: "Esamina i cambiamenti segnalati nel rilevamento Flock Safety, le risposte della comunità e i metodi a infrarossi per identificare i sistemi di telecamere."
genre: ["Tecnologie per la privacy", "Controsorveglianza", "Progetti open source", "Diritti digitali", "Sicurezza di rete", "Ricerca sulla sicurezza", "Modifica hardware", "Strumenti per la privacy"]
tags: ["Flock Safety", "ALPR", "Flock-You", "Rilevamento OUI", "Richiesta probe wildcard", "Modalità WiFi promiscua", "Monitoraggio 802.11", "DeFlockJoplin", "NitekryDPaul", "Rilevamento BLE", "WiFi a 5 GHz", "MAC amministrato localmente", "Corrispondenza pattern SSID", "Hardware di controsorveglianza", "STS Collective", "colonelpanichacks", "Elusione del rilevamento", "ESP32", "Rilevamento WiFi", "Consapevolezza della sorveglianza", "OUI-SPY", "M5 Atom Lite", "Flock Finder", "Tracciamento issue GitHub", "Aggiornamento firmware", "Protezione dal tracciamento tramite impronta digitale", "Randomizzazione MAC", "Fingerprinting degli Information Element", "Salto di canale", "Tutela della privacy", "Sicurezza open source", "Sorveglianza di massa", "Firmware di rilevamento", "Rilevamento WiFi in movimento", "Rimozione telecamere", "Hardware per la privacy", "Rilevamento a infrarossi", "Illuminatore IR", "ESP32-CAM", "Seeed Studio XIAO ESP32S3 Sense", "Quectel L76K", "Rilevamento ottico", "Valleytech Custom Solutions"]
cover: "/img/cover/flock-camera-detection-techniques-2026.webp"
coverAlt: "Scena urbana con una telecamera Flock su un lampione e un veicolo dotato di un dispositivo avanzato di rilevamento. Segnali luminosi mostrano la comunicazione dati wireless su uno sfondo scuro."
coverCaption: "Come l'hardware aggiornato di Flock Safety continua a interrompere gli strumenti open source e come la comunità recupera il terreno"
canonical: "https://simeononsecurity.com/articles/flock-camera-detection-arms-race-2026/"
---

**Se il tuo rilevatore Flock-You è diventato silenzioso su un percorso dove prima individuava sempre le telecamere, non te lo stai immaginando e probabilmente l'hardware non è guasto.** Nell'ultimo anno l'hardware e il firmware delle telecamere Flock Safety sono cambiati almeno due volte. I metodi di rilevamento della comunità si sono interrotti e i ricercatori open source hanno dovuto ricostruire ogni volta una nuova firma.

*La situazione cambia rapidamente. Il metodo di rilevamento e l'elenco OUI qui sotto riflettono il ramo `colonelpanichacks/flock-you` `main` a settembre 2026. Controlla il [repository GitHub](https://github.com/colonelpanichacks/flock-you) prima di considerare difettoso il tuo dispositivo.*

{{< youtube id="cVf-id71BuQ" >}}

*Il video sopra di Valleytech Custom Solutions documenta il sintomo descritto: un normale giro di wardriving che improvvisamente registra zero rilevamenti su più versioni firmware, lungo un percorso in cui prima le telecamere venivano rilevate in modo affidabile e in una contea dove alcune telecamere segnalate erano state rimosse fisicamente.*

______

## Un giro di wardriving che improvvisamente non rileva nulla

Le segnalazioni descrivono spesso lo stesso schema. Un conducente percorre un itinerario già fatto decine di volte. Il rilevatore usa il firmware attuale e in passato ha individuato le stesse telecamere. Durante un viaggio non rileva nulla: né un segnale acustico né una voce di log, su tutte le build personalizzate provate.

Il video di Valleytech racconta un caso simile: il tragitto quotidiano verso l'ufficio postale registrava sempre almeno una telecamera Flock, ma ora nessuna. Un secondo percorso vicino a Micro Center prima ne segnalava cinque; ora solo una risulta attiva e le altre quattro sono state sradicate dai pali.

**Sulla stessa linea temporale accadevano due cose, facili da confondere:**

- **Alcune telecamere vengono rimosse o spostate fisicamente**, quindi i dispositivi da rilevare diminuiscono davvero.
- **La firma wireless delle telecamere è cambiata**, quindi un dispositivo ancora sul palo potrebbe non attivare hardware con firmware obsoleto.

Due issue GitHub nel repository `colonelpanichacks/flock-you`, aperte a mesi di distanza, documentano il secondo problema. Letti in ordine mostrano come la comunità abbia già dovuto evolvere due volte il metodo di rilevamento.

______

## Issue #20: l'access point di gestione è scomparso

**[Issue #20](https://github.com/colonelpanichacks/flock-you/issues/20)** fu aperta a gennaio 2026. Un utente provò il dispositivo accanto a una telecamera Flock nota e registrata su DeFlock, ma non rilevò nulla. Nelle settimane seguenti arrivarono segnalazioni simili da Florida, Indiana, Atlanta e Midwest, con hardware e antenne diverse.

Un commentatore pose la domanda decisiva: **Flock aveva cambiato qualcosa dal proprio lato, interrompendo il rilevamento per tutti più o meno nello stesso momento?**

Il manutentore colonelpanichacks confermò. **Intorno a dicembre 2025 Flock disattivò l'access point di gestione che le telecamere trasmettevano.** Era la base iniziale del rilevamento wireless. Quando scomparve, la comunità passò ai segnali Bluetooth Low Energy (BLE), che entro la primavera 2026 divennero anch'essi inaffidabili.

| Superficie di rilevamento | Stato |
|---|---|
| **AP WiFi di gestione** | Disattivato da Flock, circa dicembre 2025 |
| **Beacon BLE** | Inaffidabili dalla primavera 2026 |
| **Uplink cellulare LTE** | Ancora usato per gli upload cloud, ma non rilevabile passivamente |
| **Richieste probe wildcard 802.11** | Base attuale del rilevamento, vedi sotto |

*I firmware personalizzati basati sui vecchi segnali AP o BLE ora cercano segnali che le telecamere non trasmettono più. Per questo un dispositivo funzionante può diventare completamente silenzioso senza avere un guasto hardware.*

______

## Il metodo sostitutivo: wildcard probe e fingerprinting dei frame

Il firmware attuale di `flock-you` usa una modalità promiscua 802.11 dedicata. La radio non trasmette e non si unisce alle reti: ascolta soltanto, passando sui canali WiFi 11, 6 e 1 con una permanenza di 250 millisecondi per seguire i cambi di canale delle telecamere.

**Il firmware segnala una rilevazione solo quando coincidono tutte queste condizioni:**

1. Il frame è una **Management Probe Request** 802.11 (tipo 0, sottotipo 4).
2. L'**SSID Information Element è presente con lunghezza 0**, quindi è una probe wildcard e non cerca una rete specifica.
3. L'indirizzo del trasmettitore (**addr2**) corrisponde a un prefisso OUI Flock noto.
4. Gli altri Information Element corrispondono al fingerprint documentato dalla comunità DeFlockJoplin, sulla base delle ricerche di Pintor e Atzori del 2022 sul **[fingerprinting degli IE nelle richieste probe WiFi](https://ieeexplore.ieee.org/document/10001618)**.

Il firmware chiama il metodo `wifi_wildcard_probe_ie_sig`. Nei test sul campo la comunità DeFlockJoplin ha individuato **11 telecamere note su 12 con solo 2 falsi positivi**, la stessa baseline verificata sul campo citata nella **[guida hardware](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/)**. Il dodicesimo OUI è stato aggiunto successivamente alla lista.

{{< figure src="flock-detection-arms-race-timeline-2026.webp" alt="Cronologia dei metodi per rilevare le telecamere Flock: access point WiFi di gestione, beacon Bluetooth Low Energy, wildcard probe e fingerprint degli Information Element, con nuove tecniche SSID, 5GHz e MAC" >}}

______

## L'elenco OUI attuale

Il fingerprint wildcard probe si attiva solo quando il MAC del trasmettitore corrisponde a un prefisso OUI verificato dalla comunità su hardware Flock reale. La lista è mantenuta soprattutto dal ricercatore **@NitekryDPaul**. La comunità **DeFlockJoplin** ha aggiunto il 31º elemento dopo aver rilevato una telecamera non inclusa nella lista originaria di 30.

```text
70:c9:4e  3c:91:80  d8:f3:bc  80:30:49  b8:35:32
14:5a:fc  74:4c:a1  08:3a:88  9c:2f:9d  c0:35:32
94:08:53  e4:aa:ea  f4:6a:dd  f8:a2:d6  24:b2:b9
00:f4:8d  d0:39:57  e8:d0:fc  e0:4f:43  b8:1e:a4
70:08:94  58:8e:81  ec:1b:bd  3c:71:bf  58:00:e3
90:35:ea  5c:93:a2  64:6e:69  48:27:ea  a4:cf:12
82:6b:f2
```

**L'elenco non è statico.** Le note di ricerca descrivono prefissi declassati dopo i test: uno apparteneva a un lettore multimediale Sony, un altro era un segnaposto iniziale mai corrispondente. Due voci hanno bassa affidabilità. Il prefisso `82:6b:f2` resta anche se è amministrato localmente, perché rimuoverlo avrebbe perso una rilevazione reale confermata da DeFlockJoplin.

**Un prefisso ha ora una conferma hardware indipendente.** Le immagini del file system di un'unità Flock pubblicate a settembre 2026 contenevano il MAC **`f4:6a:dd:57:46:fb`**; il prefisso `f4:6a:dd` occupa la posizione 13. Non proviene da un laboratorio o da un campione acquistato: apparteneva a una telecamera su un palo a Wauwatosa, Wisconsin, che fotografava il traffico. È la conferma più solida finora per un prefisso.

*Se mantieni un fork del firmware, recupera l'elenco OUI dalla cartella upstream `datasets/` invece di codificarne una copia. La ricerca aggiorna la lista e una copia obsoleta può far perdere telecamere senza segnalarlo.*

______

## Classifica dei segnali di rilevamento

La corrispondenza OUI è il metodo usato dal firmware attuale, ma è il più debole dei cinque segnali disponibili. La comunità di **[WiFi Mothership](https://wifimothership.com/flock)** li ordina per affidabilità usando le ricerche firmware di GainSec.

| Affidabilità | Segnale | Note |
|---|---|---|
| **ALTA** | **ID produttore BLE `0x09C8`** (XUNTONG) | Fingerprint digitale più forte. Presente sui Raven e sui Falcon o Sparrow con modulo batteria |
| **ALTA** | **UUID servizi BLE Raven da `0x3100` a `0x3500`** | Servizi GATT Raven per GPS, alimentazione, rete, upload ed errori. Solo hardware Raven |
| **MEDIA** | **Pattern SSID WiFi `^Flock-[A-Z0-9]+$`** | Nome hotspot predefinito per la configurazione. Altri SSID nel firmware: `FS Ext Battery`, `Penguin`, `Pigvision` |
| **MEDIA** | **Sottostringa del nome BLE** | Nomi come `FS Ext Battery` appaiono nei pacchetti pubblicitari senza parsing dei dati produttore |
| **BASSA** | **MAC e prefisso OUI** | **Metodo più rumoroso.** I prefissi dei fornitori di componenti compaiono in migliaia di prodotti estranei |

*La riga in fondo è quella da cui dipende di più il firmware attuale, ed è il problema centrale del rilevamento basato prima sull'OUI.*

### Perché la lista OUI è rumorosa

I 31 prefissi elencati non sono 31 identificatori Flock. WiFi Mothership **ne segue 26 in parallelo e ne classifica ogni proprietario effettivo**.

| Categoria | Numero | Proprietario |
|---|---:|---|
| **Flock Safety** | **1** | `B4:1E:52`, assegnazione IEEE all'azienda stessa |
| **Moduli batteria** | 10 | Componenti Silicon Labs nei pacchi batteria estesi |
| **Moduli camera** | 11 | Moduli WiFi per videocamere Liteon Technology |
| **Infrastruttura di calcolo** | 4 | Raspberry Pi Foundation e Raspberry Pi Trading |

**Venticinque di quei 26 prefissi appartengono a fornitori di componenti**, usati in enormi quantità di hardware non correlato. Un prefisso Silicon Labs o Liteon compare in prodotti senza rapporto con Flock Safety, e le schede Raspberry Pi sono diffuse.

**Una corrispondenza è un indizio, non un'identificazione.** Per questo il fingerprint wildcard probe è importante: combinato con un OUI, una richiesta probe con SSID vuoto porta la fiducia da ipotesi a 62 sulla scala del progetto.

*Solo `B4:1E:52` risponde da solo alla domanda «è un dispositivo Flock?». Gli altri 30 prefissi sono prove di supporto.*

### Quante telecamere espongono un hotspot

I dati wardriving forniscono un limite minimo. WiFi Mothership ha contato **almeno 900 access point Flock su WiGLE nel 2025**. Un AP Flock indica un dispositivo che trasmette l'hotspot SSID predefinito `Flock-XXXX`.

Il numero descrive i dispositivi con hotspot di configurazione, non tutte le installazioni. Flock dichiara decine di migliaia di telecamere e la maggior parte non trasmette nulla che un wardriver in transito registri. **La mappa è un campione, ed è piccolo.**

______



## Issue #43: nuovo schema SSID, 5GHz e anti-fingerprinting MAC

Tre mesi dopo la chiusura dell'Issue #20 è arrivata una seconda segnalazione, che descrive una possibile contromisura deliberata al rilevamento, non una modifica firmware casuale. **[Issue #43](https://github.com/colonelpanichacks/flock-you/issues/43)**, aperto a maggio 2026, usa dati di wardriving di WiGLE raccolti vicino a una telecamera già confermata su DeFlock. Documenta tre aspetti che gli strumenti esistenti non consideravano.

### Risultato 1: un formato SSID diverso

L'hotspot Flock documentato seguiva sempre il modello `Flock-XXXXXX`. La telecamera della segnalazione trasmetteva invece **`Flock Camera net.`**, una convenzione di denominazione del tutto diversa. Chi cercava su WiGLE il carattere jolly `Flock-*`, come facevano diversi ricercatori, non avrebbe ottenuto alcun risultato per questa telecamera, benché stesse trasmettendo.

### Risultato 2: hotspot 5GHz confermato

La stessa telecamera trasmetteva simultaneamente sul **canale 1 a 2,4GHz** e sul **canale 157 a 5GHz**, usando indirizzi MAC sequenziali su ciascuna banda (`...9f:a2:de` e `...9f:a2:df`). Questo suggerisce un singolo modulo WiFi dual-band che assegna indirizzi adiacenti alle due radio, non due dispositivi distinti. Una segnalazione indipendente del ricercatore nsm_barii aveva già registrato una richiesta probe Flock sul canale 149 a 5GHz. Ora ci sono due osservazioni che confermano che il 5GHz è effettivamente usato.

**Tutti i metodi di rilevamento descritti sopra, compreso il firmware attuale basato su wildcard probe, ascoltano solo a 2,4GHz.** Una telecamera che trasmette soltanto o soprattutto a 5GHz resta invisibile a quell'hardware, indipendentemente dall'accuratezza dell'elenco OUI.

### Risultato 3: indirizzi MAC amministrati localmente sull'hotspot

Entrambi gli indirizzi MAC acquisiti hanno il **bit di amministrazione locale impostato**, quindi non provengono dal blocco OUI registrato da Flock presso IEEE. La logica standard di rilevamento di `flock-you` ignora intenzionalmente gli indirizzi amministrati localmente, perché è il metodo abituale per filtrare telefoni e laptop che randomizzano il MAC.

**Questo filtro, pensato per ridurre i falsi positivi, esclude anche una telecamera Flock che usi un MAC amministrato localmente sull'interfaccia hotspot.** Gli ultimi byte sequenziali dei due indirizzi escludono una generazione casuale e fanno pensare a un'assegnazione strutturata e intenzionale.

| Risultato | Cosa continua a funzionare |
|---|---|
| **Nuovo formato SSID** (`Flock Camera net.`) | Il riconoscimento del modello SSID funziona se si amplia il modello di corrispondenza |
| **Uso del 5GHz** | Nulla nel firmware WiFi attuale, che esegue scansioni solo a 2,4GHz |
| **MAC amministrato localmente** | Il riconoscimento del modello SSID, perché non dipende dall'indirizzo MAC |

*Il riconoscimento dell'SSID è l'unico metodo in questa tabella che continua a funzionare indipendentemente dalla banda o dall'assegnazione dell'indirizzo MAC. È un motivo pratico per supportare modelli SSID più ampi invece di affidarsi solo alle corrispondenze OUI.*

______

## Flock sta eludendo intenzionalmente il rilevamento?

Nessuna delle due segnalazioni GitHub dimostra un intento. L'autore dell'Issue #43 l'ha posta come domanda aperta: il comportamento è comune alle installazioni Flock o riguarda una sola versione firmware su una singola telecamera?

Considerando insieme entrambe le segnalazioni emerge uno schema. Una superficie di rilevamento scompare; la comunità trova un'alternativa; i punti ciechi di quest'ultima (scansione solo a 2,4GHz, corrispondenze OUI e filtro degli indirizzi MAC amministrati localmente) coincidono con le caratteristiche che un nuovo SSID, una radio a 5GHz e un MAC amministrato localmente potrebbero sfruttare. **Potrebbe essere una coincidenza dovuta a un ciclo di aggiornamento firmware non correlato. Potrebbe anche trattarsi di un fornitore che riduce la propria presenza wireless, rendendo più difficile il rilevamento da parte di terzi come effetto collaterale, intenzionale o meno.**

*La posizione più utile non è scegliere una spiegazione. È costruire sistemi di rilevamento che non dipendano da una singola ipotesi, perché la storia biennale di questo progetto mostra che nessuna è rimasta valida per sempre.*

### Conferma visiva: accesa, ma senza trasmissioni

**[Un terzo breve video di Valleytech Custom Solutions](https://www.youtube.com/shorts/sjI8FB0cLk0) verifica l'ipotesi che la telecamera fosse stata rimossa.**

{{< youtube id="sjI8FB0cLk0" >}}

Di notte, l'autore è tornato alla telecamera del primo video e ha verificato visivamente che i **LED IR erano ancora attivi**: l'unità era accesa e illuminava la scena per le riprese notturne. Allo stesso tempo, **ogni firmware personalizzato testato ha registrato zero rilevamenti validi**. È scattato un avviso, ma era un falso positivo confermato. La telecamera non trasmetteva nulla sul lato wireless.

**Questo distingue chiaramente le due spiegazioni possibili.** Una telecamera sradicata o spostata non spiega un'unità visibilmente accesa e attiva di notte. Una telecamera funzionante e illuminata, ma silenziosa per tutti i metodi WiFi, indica che è scomparsa la firma wireless, non l'hardware.

Dopo aver parlato con altri sviluppatori al lavoro sullo stesso problema, l'autore ha riferito che non si trattava di un caso isolato. **Più persone hanno osservato lo stesso schema all'incirca nello stesso periodo**, il che suggerisce un cambiamento coordinato su scala nazionale da parte di Flock, non un'anomalia locale. *È un'affermazione aneddotica, basata su conversazioni informali e non su un dataset pubblicato. È coerente con le finestre di dicembre 2025 e primavera 2026 descritte nell'Issue #20. Una nuova segnalazione GitHub sarebbe il posto adatto per documentarla.*

______

## Cosa significa per il tuo hardware di rilevamento

Se il dispositivo ha smesso di rilevare, verifica questi punti prima di concludere che sia guasto:

1. **Aggiorna prima il firmware.** Se usi una versione precedente all'attuale ramo `main`, potresti ancora cercare l'AP di gestione disattivato o i beacon BLE inattendibili. Scarica il firmware più recente e reinstallalo.
2. **Verifica che la telecamera sia ancora presente.** Alcune segnalazioni di zero rilevamenti riguardavano hardware davvero rimosso o spostato, non un guasto del rilevamento. Confronta con **[Flock Finder](/articles/flock-finder-alpr-surveillance-mapping-tool/)** o **[DeFlock](https://deflock.org/)** prima di diagnosticare il dispositivo.
3. **Rallenta agli incroci.** Una permanenza di 250 ms per canale può farti superare la finestra di rilevamento prima che la radio raggiunga il canale giusto. Fermarti per 30-60 secondi rileva più telecamere di un passaggio rapido con un'antenna più grande.
4. **Segnala ciò che osservi.** Zero rilevamenti accanto a una telecamera verificata visivamente è proprio il tipo di dato che ha portato agli Issue #20 e #43. Apri una nuova segnalazione invece di presumere che qualcun altro l'abbia già fatta.
5. **Considera i limiti attuali.** Un firmware solo WiFi e 2,4GHz non rileva una telecamera passata al 5GHz o silenziosa sulle bande scansionate. È una lacuna reale, non un errore della tua build.

**Questo non rende inutile l'hardware.** L'elenco OUI e l'impronta wildcard probe rilevano ancora la maggior parte delle telecamere installate. Considera ogni rilevatore, autocostruito o acquistato, come una fotografia della gara tecnologica in corso, non come una soluzione permanente.

{{< stscollective-ad "flockyou" >}}

______

## Un approccio parallelo: rilevare il lampo infrarosso invece del segnale WiFi

Il rilevamento wireless non è l'unico fronte di questa gara. **[Un video di approfondimento](https://www.youtube.com/shorts/mzpr6bslsYA) dello stesso autore, Valleytech Custom Solutions, descrive un approccio completamente diverso**: osservare l'illuminatore a infrarossi della telecamera invece di ascoltare una firma radio.

{{< youtube id="mzpr6bslsYA" >}}

La maggior parte delle telecamere ALPR, comprese quelle Flock, usa **illuminazione a infrarossi per acquisire targhe leggibili di notte**. La luce IR è invisibile all'occhio umano, ma è visibile a un sensore d'immagine privo del filtro IR-cut. *È proprio l'assenza di questo filtro a trasformare un normale modulo fotocamera in un rilevatore Flock.*

### Aspetto del prototipo

L'approccio mostrato nel video ha attraversato varie iterazioni prima di arrivare a una combinazione utilizzabile:

- **Primo tentativo**: ricevitori con fotodiodi IR dedicati. Funzionavano, ma i componenti costavano troppo per un progetto fai-da-te pratico.
- **Secondo tentativo**: **Jetson Nano con un modulo fotocamera Raspberry Pi**. Ha dimostrato che il concetto funzionava, ma costo e consumo energetico lo rendevano inadatto a una configurazione portatile o da veicolo.
- **Configurazione attuale**: **modulo fotocamera ESP32 senza lente IR-cut**. L'autore ha provato una **ESP32-CAM** e una **M5Stack S3 Cam**, poi ha scelto la **Seeed Studio XIAO ESP32S3 Sense**, abbinata a un **modulo GNSS Seeed XIAO basato sul chip Quectel L76K** per associare coordinate GPS ai rilevamenti, seguendo lo stesso metodo di wardriving GPS usato dalla dashboard WiFi di `flock-you`.

| Requisito | Perché conta |
|---|---|
| **Modulo fotocamera senza filtro IR-cut** | Il filtro che rende i colori delle foto normali impedisce di vedere la luce necessaria a questo metodo |
| **Fotocamera invece di un fotodiodo** | I ricevitori a fotodiodo in grado di isolare il segnale costavano troppo per una soluzione fai-da-te pratica |
| **Registrazione GPS** | Collega i rilevamenti a una posizione, come la dashboard Flask del firmware WiFi |

### Schema di lampeggio della telecamera

Il metodo presuppone che l'illuminatore lampeggi con uno schema ripetuto e rilevabile, anziché restare acceso. L'autore ha riferito una **misurazione personale di circa 20 millisecondi acceso e 80 spento, per un periodo di 100 millisecondi: ciclo di lavoro del 20% a 10Hz**. Ha chiarito che la misura non è verificata e potrebbe essere errata. *Usa questo valore come punto di partenza per le tue misurazioni, non come specifica confermata: Flock non l'ha pubblicata e l'autore non ha dichiarato certezza.*

### Stato del progetto

**È un prototipo iniziale per uso fai-da-te, non un prodotto finito.** L'autore ha descritto il software come «vibe coded» e ancora in sviluppo. Un cicalino per gli avvisi sonori è previsto, ma non è stato ancora aggiunto; non esiste una scheda pronta all'uso equivalente all'OUI-SPY. La versione attuale richiede che **una persona confermi visivamente** che un rilevamento segnalato sia una telecamera e non un'altra sorgente IR. È quindi uno strumento di screening, non un sistema completamente automatico.

*È una superficie di rilevamento diversa da tutte le altre descritte nell'articolo. Non dipende da WiFi, 2,4 o 5GHz, corrispondenze OUI o comportamento degli indirizzi MAC, quindi le tecniche di elusione dell'Issue #43 non la influenzano. Ha però i suoi limiti: linea di vista, interferenze della luce diurna e un ciclo di lavoro non confermato in modo indipendente.*

______

## Cosa sta facendo la comunità

La risposta a entrambe le segnalazioni ha seguito lo schema che da due anni mantiene utile questo progetto: qualcuno segnala una lacuna, qualcun altro contribuisce a una correzione e l'aggiornamento viene distribuito invece di restare in arretrato.

- **L'Issue #20** si è concluso con una causa confermata e una riscrittura del firmware basata sulla firma wildcard probe, grazie alla ricerca sul campo della comunità DeFlockJoplin.
- **L'Issue #43** è ancora aperto al momento della stesura; il suggerimento di riconoscere il modello SSID non è stato ancora implementato. *Aggiungere `Flock Camera` come modello aggiuntivo è un contributo circoscritto per chi conosce la logica di corrispondenza del firmware.*
- Il dataset OUI è versionato e datato. Le voci declassate e quelle a bassa affidabilità sono documentate, non rimosse senza spiegazioni, così chi crea un fork vede cosa è cambiato e perché.

*Questo è il vantaggio pratico degli strumenti di rilevamento open source rispetto a un'alternativa chiusa. Chi scopre una lacuna non può correggere un rilevatore proprietario. Questo progetto è già stato aggiornato due volte.*

______

## L'altra risposta: rimuovere l'hardware

Il rilevamento wireless è una risposta a queste telecamere. Un'iniziativa parallela ha preso di mira l'hardware stesso e, a settembre 2026, ha prodotto le prove pubbliche più dettagliate sul funzionamento interno di una telecamera Flock.

**Il collettivo stegan0gram ha rimosso una telecamera dal palo, copiato la memoria interna e pubblicato le immagini del filesystem tramite Distributed Denial of Secrets.** Ha descritto il lavoro così:

> "Perché distruggerle e basta, quando possiamo fare reverse engineering e trovare i segreti di chi ci spia? Abbiamo liberato sul campo l'hardware, lo abbiamo disarmato e poi abbiamo analizzato le telecamere e le apparecchiature solari associate."

*La distinzione conta. Distruggere una telecamera rimuove un'unità. Il reverse engineering fornisce prove sull'intera flotta.*

### Cosa ha rivelato la rimozione

Il dataset include una **partizione multimediale da 18 GB**, un'**immagine di sistema Android da 1,5 GB** e una **partizione delle credenziali da 32 MB**, oltre alla chiave recuperata per il contenitore multimediale cifrato. I ricercatori hanno identificato le versioni del sistema operativo e del kernel, credenziali backend codificate nel firmware e token di autenticazione in chiaro memorizzati dalla telecamera.

Queste prove sostengono la ricerca sulla sicurezza in **[Vulnerabilità delle telecamere Flock Safety: oltre 50 difetti individuati](/articles/flock-safety-camera-security-vulnerabilities-research-2026/)**, che in precedenza si basava su dispositivi di laboratorio e unità acquistate.

### La risposta alla rimozione

Gli interventi fisici hanno conseguenze e il quadro è contrastante:

- **Più persone sono state arrestate in tutto il paese** per presunti atti di vandalismo contro telecamere Flock.
- **Alcuni comuni hanno annunciato che smetteranno di usare le telecamere.** Questo è il risultato auspicato dagli oppositori.
- **Un dipartimento di polizia ha costruito un falso alloggiamento Flock stampato in 3D** per attirare e arrestare potenziali vandali.

Noel Pichardo, ex agente di polizia a Pawtucket, Rhode Island, è diventato critico di Flock dopo aver contestato l'uso delle telecamere da parte del suo dipartimento. A WIRED ha detto di capire la frustrazione, ma di temere che il sabotaggio convinca polizia e governo che questa tecnologia sia necessaria. «Più a lungo il governo ignora le lamentele dei residenti contrari a questo tipo di sorveglianza, più spesso succederà», ha affermato.

### Il ruolo del rilevamento

La rimozione non cambia il problema del rilevamento. La telecamera continua a trasmettere; il firmware ha ancora bisogno dell'elenco OUI e della firma probe; i due casi documentati di perdita del segnale restano rilevanti.

Il dump conferma **l'identità dell'hardware**, inclusa una voce OUI verificata su un dispositivo reale. **Le telecamere scompaiono da un percorso perché un consiglio comunale chiude un contratto, non perché un rilevatore smette di funzionare.** Gli strumenti wireless rispondono a una domanda personale sull'ambiente circostante. Il dibattito politico risponde alla questione più ampia, e il dump ha fornito a quel dibattito le prove più solide finora disponibili.

______

## Conclusione: il rilevamento è un bersaglio mobile

Un rilevatore silenzioso su un percorso dove prima individuava telecamere non dimostra che l'hardware sia guasto. Indica che la firma wireless su cui fa affidamento è cambiata di nuovo, già due volte in un anno. **L'AP di gestione, i beacon BLE e forse ora le ipotesi di soli 2,4GHz e soli OUI nel firmware** si sono rivelati tutti temporanei.

**La soluzione non è mai stata rinunciare al rilevamento wireless.** Mantieni visibili e documentate le ipotesi, così da poterle aggiornare quando arriva una segnalazione come l'Issue #20 o #43. Questo è il vantaggio del firmware open source rispetto a un'alternativa chiusa: la comunità può colmare la lacuna quando la individua, senza aspettare il fornitore.

### Punti principali

- **Due segnali di rilevamento sono già scomparsi**: l'AP WiFi di gestione, disattivato intorno a dicembre 2025, e i beacon BLE, inaffidabili dalla primavera 2026.
- **Il metodo attuale, wildcard probe con fingerprinting OUI e IE, ha rilevato 11 telecamere su 12 nei test sul campo**, ma funziona solo tramite WiFi a 2,4GHz.
- **Una segnalazione aperta descrive un nuovo formato SSID, un hotspot 5GHz confermato e MAC amministrati localmente**, che il metodo OUI attuale limitato a 2,4GHz non rileva.
- **Sta emergendo un metodo alternativo senza WiFi**: una fotocamera ESP32 priva di filtro IR-cut rileva l'illuminazione infrarossa e non risente delle tecniche di elusione wireless descritte.
- **La verifica visiva conferma il silenzio wireless**: una telecamera era accesa e illuminava la scena di notte, ma ha prodotto zero rilevamenti WiFi validi. In quel caso la rimozione non spiega il silenzio.
- **Zero rilevamenti vicino a una telecamera nota non significa subito che l'hardware sia guasto.** Aggiorna prima il firmware, poi verifica che la telecamera sia ancora presente.
- **Il progetto open source pubblica correzioni quando la comunità trova lacune.** Leggi le issue GitHub insieme al README per conoscere lo stato attuale.

### Prossimi passi

1. **Aggiorna il firmware** all'attuale ramo `main` prima di fare altre verifiche: **[github.com/colonelpanichacks/flock-you](https://github.com/colonelpanichacks/flock-you)**
2. **Leggi la guida hardware completa** se non l'hai già fatto: **[Progetto di rilevamento Flock-You: guida all'hardware di contro-sorveglianza](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/)**
3. **Confronta le possibili zone cieche** con **[Flock Finder](/articles/flock-finder-alpr-surveillance-mapping-tool/)** prima di concludere che il dispositivo non abbia rilevato qualcosa.
4. **Scopri cosa stai affrontando**: **[Sorveglianza con telecamere Flock Safety: diffusione, problemi di privacy e strategie di protezione](/articles/flock-safety-camera-surveillance-prevalence-privacy-protection-2026/)**
5. **Combina il rilevamento WiFi con quello cellulare** tramite **[Rayhunter](/articles/how-to-flash-rayhunter-devices-complete-guide/)** per un quadro più ampio. Nessuno dei metodi di questo articolo rileva gli IMSI catcher.

{{< centerbutton href="https://stscollective.com/discount/SIMEONONSECURITY" >}}
  Acquista dispositivi FlockYou pronti all'uso e risparmia il 20%
{{< /centerbutton >}}

______

## Articoli correlati

| Articolo | Contenuto |
|---------|---------------|
| **[Progetto di rilevamento Flock-You: guida all'hardware di contro-sorveglianza](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/)** | Guida tecnica alle tre piattaforme hardware, alla configurazione firmware e al metodo di rilevamento descritto in questo articolo |
| **[Flock Finder: mappa ogni presunta telecamera Flock vicino a te](/articles/flock-finder-alpr-surveillance-mapping-tool/)** | Confronta una possibile zona cieca con oltre 40.000 posizioni di telecamere mappate prima di diagnosticare il dispositivo |
| **[Telecamere Flock: strumento di sicurezza pubblica o macchina di sorveglianza senza mandato?](/articles/flock-cameras-public-safety-or-surveillance-2026/)** | Analisi di ciò che consente il database Flock e del motivo per cui la questione dei mandati conta più del rilevamento |
| **[Sorveglianza con telecamere Flock Safety: diffusione, problemi di privacy e strategie di protezione](/articles/flock-safety-camera-surveillance-prevalence-privacy-protection-2026/)** | Diffusione, casi documentati di abuso e risorse per l'organizzazione comunitaria |
| **[Vulnerabilità delle telecamere Flock Safety: oltre 50 difetti individuati](/articles/flock-safety-camera-security-vulnerabilities-research-2026/)** | Ricerca sulla sicurezza hardware e software, distinta dal tema del rilevamento wireless |
| **[Come aggiornare i dispositivi Rayhunter: guida completa](/articles/how-to-flash-rayhunter-devices-complete-guide/)** | Rileva IMSI catcher e stingray, l'equivalente cellulare della lacuna WiFi descritta qui |

______

## Riferimenti

1. [Repository GitHub di Flock-You - colonelpanichacks](https://github.com/colonelpanichacks/flock-you)
2. [GitHub Issue #20 - Telecamere Flock non rilevate, mentre altri dispositivi sì](https://github.com/colonelpanichacks/flock-you/issues/20)
3. [GitHub Issue #43 - Segnale 5GHz? Nuovo OUI / filtro degli indirizzi MAC](https://github.com/colonelpanichacks/flock-you/issues/43)
4. [Dataset di ricerca OUI NitekryDPaul](https://github.com/colonelpanichacks/flock-you/blob/main/datasets/NitekryDPaul_wifi_ouis.md)
5. [nitekry/nite-oui-collection](https://github.com/nitekry/nite-oui-collection)
6. [DeFlock Joplin - Ricerca ALPR della comunità](https://deflockjoplin.today)
7. [Pintor, L. & Atzori, L. (2022) - Analisi delle richieste Wi-Fi probe per il fingerprinting degli Information Element, IEEE GLOBECOM](https://ieeexplore.ieee.org/document/10001618)
8. [WIRED e 404 Media - Hacker sono entrati in una telecamera Flock](https://www.wired.com/story/hackers-flock-camera-data-shows-how-system-works/)
9. [Micah Lee - Le telecamere Flock sono piene di vulnerabilità e credenziali codificate nel firmware](https://micahflee.com/flock-cameras-are-riddled-with-security-vulnerabilities-and-hard-coded-credentials/)
10. [Distributed Denial of Secrets - Immagini del filesystem di una telecamera ALPR Flock](https://ddosecrets.org/article/flock-alpr-camera)
11. [Hackaday - Questa settimana nella sicurezza: le telecamere Flock sono vecchie, patch Microsoft e ricercatori attaccano SSH](https://hackaday.com/2026/09/18/this-week-in-security-flock-cameras-are-old-microsoft-patches-patches-and-researchers-attack-ssh/)
12. [WiFi Mothership - Rilevamento ALPR Flock Safety e riferimento dei dispositivi](https://wifimothership.com/flock)
13. [GainSec - Ricerca firmware e avvisi di sicurezza](https://gainsec.com/)
14. [The Hunt for the Hidden Probe - Comportamento dei wildcard probe con SSID nascosto](https://goodwi.fi/posts/2023/12/hunt-for-hidden-probe/)
15. [DeFlock - Mappa collaborativa delle telecamere ALPR](https://deflock.org/)
16. [Colonel Panic Tech - OUI-SPY e hardware di rilevamento](https://colonelpanic.tech)
17. [STS Collective - Dispositivi FlockYou](https://stscollective.com/discount/SIMEONONSECURITY)
18. [Sta succedendo qualcosa di strano con le telecamere Flock - Valleytech Custom Solutions](https://www.youtube.com/shorts/cVf-id71BuQ)
19. [Wardriving a infrarossi per telecamere Flock - Valleytech Custom Solutions](https://www.youtube.com/shorts/mzpr6bslsYA)
20. [Telecamere Flock accese ma senza trasmissioni - Valleytech Custom Solutions](https://www.youtube.com/shorts/sjI8FB0cLk0)
21. [Riconoscimento automatico delle targhe - Wikipedia (illuminazione a infrarossi nei sistemi ANPR/ALPR)](https://en.wikipedia.org/wiki/Automatic_number-plate_recognition)
22. [Seeed Studio XIAO ESP32S3 Sense](https://www.seeedstudio.com/XIAO-ESP32S3-Sense-p-5639.html)
23. [Modulo GNSS L76K per Seeed Studio XIAO](https://www.seeedstudio.com/L76K-GNSS-Module-for-Seeed-Studio-XIAO-p-5864.html)
