---
title: "I tipi di attacco informatico più comuni e come rilevarli"
date: 2026-09-11
lastmod: 2026-11-07
toc: true
draft: false
description: "Scopri i tipi di attacco informatico più comuni, individua le tracce lasciate nei log e nella telemetria e prova le tecniche di rilevamento in un laboratorio domestico di sicurezza."
genre: ["Cybersecurity", "Rilevamento delle minacce", "Blue Team", "Operazioni di sicurezza", "Sviluppo professionale"]
tags: ["tipi di attacco informatico", "malware", "ransomware", "phishing", "spear phishing", "ingegneria sociale", "spoofing", "attacchi basati sull'identità", "credential stuffing", "password spraying", "SQL injection", "cross-site scripting", "attacco alla catena di fornitura", "minaccia interna", "tunneling DNS", "attacchi IoT", "attacchi basati sull'IA", "negazione del servizio", "detection engineering", "analista SOC", "blue team", "laboratorio domestico", "analisi dei log", "risposta agli incidenti", "MITRE ATT&CK", "carriera nella cybersecurity", "threat hunting", "centro operativo di sicurezza", "telemetria", "triage degli avvisi"]
cover: "/img/cover/types-of-cyberattacks-icons-illustration.webp"
coverAlt: "Illustrazione digitale con icone astratte e colorate che rappresentano diversi tipi di attacco informatico, come ransomware, phishing e negazione del servizio, su uno sfondo scuro."
coverCaption: ""
---

Un **tipo di attacco** è una categoria di tecniche, non un singolo strumento. Ransomware, phishing e credential stuffing descrivono metodi che un avversario ripete contro molti obiettivi con variazioni minime. Conoscere queste categorie ti offre un indice mentale per gli avvisi che incontrerai in un team di sicurezza.

*Le singole famiglie di malware compaiono e scompaiono nel giro di pochi mesi. Le categorie di attacco qui sotto restano stabili da anni e ciascuna lascia tracce riconoscibili nella telemetria degli endpoint, delle identità, della rete o della posta elettronica.*

<!--more-->

## Punti chiave

- **Impara lo schema, non il payload.** Le categorie di attacco cambiano molto più lentamente dei singoli strumenti.
- **Ogni categoria lascia tracce.** Il rilevamento inizia sapendo quale telemetria registra l'attività.
- **Riproduci un attacco per capirlo.** Un laboratorio domestico trasforma una categoria astratta in un'osservazione registrata.
- **Documenta ciò che trovi.** Una breve nota d'indagine dimostra il lavoro e spiega quali prove hai raccolto.

## Tipi di attacco a colpo d'occhio

La tabella elenca le categorie che i team di sicurezza incontrano più spesso. Le sezioni successive descrivono ogni categoria, le varianti comuni e i dati che un difensore esamina per rilevarla.

| Tipo di attacco | Cosa fa |
|---|---|
| **Malware** | Esegue software dannoso come ransomware, spyware e trojan |
| **Negazione del servizio** | Inonda un servizio di traffico finché gli utenti legittimi perdono l'accesso |
| **Phishing** | Induce una persona a rivelare credenziali o ad avviare un file dannoso |
| **Spoofing** | Si spaccia per un sistema, mittente o indirizzo attendibile |
| **Attacchi basati sull'identità** | Abusano di credenziali rubate o falsificate per agire come un utente valido |
| **Iniezione di codice** | Inserisce codice dannoso in un'applicazione per modificarne il comportamento |
| **Attacchi alla catena di fornitura** | Compromettono un fornitore, una libreria o un canale di aggiornamento attendibile |
| **Ingegneria sociale** | Manipola una persona affinché compia un'azione non sicura |
| **Minacce interne** | Abusano degli accessi di un dipendente attuale o precedente |
| **Tunneling DNS** | Codifica dati nelle query DNS per superare i controlli |
| **Attacchi IoT** | Prendono di mira dispositivi connessi per spostarsi nella rete, spiare o entrare in una botnet |
| **Attacchi basati sull'IA** | Usano l'apprendimento automatico per generare contenuti, impersonare persone o eludere i filtri |

**Nota sull'ambito:** queste categorie si sovrappongono. Un messaggio di phishing spesso distribuisce malware e il furto di credenziali spesso precede un attacco basato sull'identità. Considera l'elenco come un insieme di prospettive, non come categorie rigide.

______

## Malware

**Malware** comprende qualsiasi programma creato per danneggiare, controllare o trarre profitto da un sistema. Il termine include ransomware, malware fileless, spyware, adware, trojan, worm, rootkit, keylogger e botnet.

| Sottotipo | Comportamento |
|---|---|
| **Ransomware** | Cifra i file e chiede un pagamento per la chiave di decrittazione |
| **Malware fileless** | Si serve degli strumenti di sistema integrati e scrive poco su disco |
| **Spyware** | Raccoglie dati sulle attività senza che l'utente lo sappia |
| **Trojan** | Si presenta come software legittimo per ottenere l'esecuzione |
| **Worm** | Si copia tra gli host senza intervento dell'utente |
| **Rootkit** | Si nasconde nel sistema operativo per mantenere il controllo persistente |

**Dove trovare le prove:** gli strumenti di endpoint detection and response, o **EDR**, registrano alberi dei processi, righe di comando, scritture di file e modifiche al registro. Anche un attacco fileless produce telemetria sui processi e sugli script, perché il sistema operativo avvia comunque gli strumenti sfruttati dall'attacco.

______

## Negazione del servizio

**Un attacco di negazione del servizio (DoS)** inonda un obiettivo di richieste finché gli utenti legittimi perdono l'accesso. **Un attacco distribuito di negazione del servizio (DDoS)** ripete la stessa tecnica da molti sistemi contemporaneamente, rendendo molto più difficile filtrare il traffico in base all'indirizzo di origine.

| Caratteristica | DoS | DDoS |
|---|---|---|
| **Origine** | Un sistema | Molti sistemi |
| **Difficoltà di blocco** | Moderata | Alta, perché le origini si trovano su molte reti |
| **Impatto tipico** | Perdita di disponibilità | Perdita di disponibilità su scala maggiore |

**Dove trovare le prove:** volume del traffico rispetto alla baseline, connessioni per origine, picchi nella frequenza delle richieste e variazioni del tasso di errori. Il monitoraggio della disponibilità spesso genera un avviso prima che l'evento raggiunga il team di sicurezza.

______

## Phishing

**Il phishing** usa email, messaggi di testo, telefonate o social media per spingere una persona a rivelare credenziali o ad aprire un allegato dannoso. La categoria si divide in base al bersaglio e al canale.

| Variante | Bersaglio e canale |
|---|---|
| **Spear phishing** | Una persona o un team specifico, di solito via email |
| **Whaling** | Dirigenti e personale senior, spesso per spostare denaro o dati |
| **Smishing** | Messaggi di testo fraudolenti |
| **Vishing** | Telefonate o messaggi vocali fraudolenti |

**Dove trovare le prove:** log del gateway email, risultati dell'analisi degli URL, analisi degli allegati e segnalazioni degli utenti. La segnalazione di un dipendente prudente è uno dei segnali di maggior valore in questo elenco.

______

## Spoofing

**Lo spoofing** nasconde un aggressore dietro un'identità attendibile, così il bersaglio accetta la connessione, il messaggio o l'indirizzo. Il travestimento guadagna tempo e aggira i controlli basati sulla fiducia.

| Tipo | Cosa viene falsificato |
|---|---|
| **Domain spoofing** | Un sito o dominio email simile che imita un marchio reale |
| **Email spoofing** | L'indirizzo del mittente di un messaggio |
| **ARP spoofing** | Un indirizzo di rete locale per intercettare il traffico tra due host |

**Dove trovare le prove:** risultati SPF, DKIM e DMARC nelle intestazioni email, data di registrazione del dominio, differenze nei certificati e avvisi di indirizzi duplicati sulla rete locale.

______

## Attacchi basati sull'identità

**Gli attacchi basati sull'identità** usano un account valido invece di una vulnerabilità software. L'aggressore possiede credenziali funzionanti, quindi l'attività somiglia a un uso normale e si confonde con il rumore di fondo. Questa categoria genera una quota significativa degli avvisi che un **centro operativo di sicurezza (SOC)** gestisce ogni giorno.

*Se provi una sola categoria in un laboratorio domestico, scegli questa. I segnali sono ricchi, gli esercizi sono ripetibili e la configurazione resta contenuta.*

| Tecnica | Cosa succede |
|---|---|
| **Kerberoasting** | Richiede un ticket di servizio e poi ne decifra offline la password cifrata |
| **Man-in-the-middle (MITM)** | Si inserisce tra due parti per leggere o modificare una sessione |
| **Pass-the-hash** | Riutilizza un hash di password rubato per aprire una nuova sessione |
| **Golden ticket** | Falsifica un ticket-granting ticket Kerberos per ottenere ampio accesso al dominio |
| **Silver ticket** | Falsifica un ticket di servizio per un singolo servizio |
| **Raccolta di credenziali** | Raccoglie in massa nomi utente e password |
| **Credential stuffing** | Riprova le stesse credenziali su molti siti non correlati |
| **Password spraying** | Prova una password comune su molti account |
| **Brute force** | Prova molte password contro un account |
| **Downgrade** | Forza una connessione a usare una versione del protocollo più debole |

**Dove trovare le prove:** record di accesso, conteggi di autenticazioni non riuscite, anomalie nei token, segnalazioni di spostamenti impossibili e rilevamenti dei rischi d'identità. Anche il **phishing adversary-in-the-middle (AiTM)** appartiene a questa categoria, perché l'aggressore ruba un token di sessione attivo anziché una password e il successivo riutilizzo da infrastrutture sconosciute attiva il motore di rilevamento dei rischi d'identità.

______

## Iniezione di codice

**L'iniezione di codice** inserisce codice controllato dall'aggressore in un'applicazione vulnerabile, così l'applicazione lo esegue durante il normale funzionamento. È l'applicazione, non l'aggressore, a compiere l'azione dannosa.

| Tipo | Obiettivo |
|---|---|
| **SQL injection** | Una query al database costruita con input non convalidati |
| **Cross-site scripting (XSS)** | Una pagina web che esegue lo script dell'aggressore nel browser di un visitatore |
| **Malvertising** | Uno spazio pubblicitario legittimo riempito con codice dannoso |
| **Avvelenamento dei dati** | Un insieme di addestramento per un modello di IA o di apprendimento automatico |

**Dove trovare le prove:** log dell'applicazione web, record delle query al database, report della Content Security Policy e pattern di richieste diversi dal normale uso dell'applicazione.

______

## Attacchi alla catena di fornitura

**Un attacco alla catena di fornitura** prende di mira una terza parte attendibile, il cui prodotto o servizio raggiunge molti clienti. **Un attacco alla catena di fornitura software** inserisce codice dannoso in un'applicazione, una libreria o un aggiornamento, così lo ricevono tutti gli utenti del prodotto. **Un attacco alla catena di fornitura hardware** compromette un componente fisico prima della spedizione.

*Il software moderno dipende da librerie di terze parti, quindi una sola dipendenza compromessa raggiunge molti più utenti del fornitore originario.*

**Dove trovare le prove:** analisi della composizione software, record della pipeline di compilazione, connessioni in uscita inattese da un aggiornamento attendibile e controlli d'integrità sugli artefatti distribuiti.

______

## Ingegneria sociale

**L'ingegneria sociale** usa la pressione psicologica per spingere una persona a compiere un'azione non sicura. L'aggressore fa leva su autorità, urgenza, paura, denaro o fiducia.

| Tecnica | Approccio |
|---|---|
| **Pretexting** | Inventa uno scenario credibile per ottenere fiducia |
| **Business email compromise (BEC)** | Impersona un collega fidato per deviare un pagamento o condividere dati |
| **Disinformazione** | Diffonde narrazioni false attraverso social media e bot |
| **Quid pro quo** | Offre una ricompensa in cambio di informazioni o accesso |
| **Honeytrap** | Costruisce una relazione falsa per ottenere denaro, dati o accesso |
| **Tailgating** | Segue un dipendente attraverso una porta protetta |

**Dove trovare le prove:** risultati dell'autenticazione email, richieste insolite di modifica dei pagamenti, record dell'helpdesk e log degli accessi fisici.

______

## Minacce interne

**Una minaccia interna** consiste nell'abuso degli accessi da parte di un dipendente attuale o precedente, un collaboratore o un partner. Alcuni agiscono intenzionalmente, spinti dal denaro o dal risentimento. Altri agiscono per negligenza, ad esempio lasciando credenziali in un documento condiviso.

*Nei rapporti sugli incidenti compaiono più spesso insider negligenti che insider malevoli. Entrambi richiedono lo stesso controllo investigativo: confrontare gli accessi con una baseline relativa al ruolo.*

**Dove trovare le prove:** volume dei trasferimenti di dati, attività fuori dall'orario abituale, modifiche ai privilegi e download in massa da repository sensibili.

______

## Tunneling DNS

**Il tunneling DNS** codifica dati nelle query e nelle risposte DNS. Quasi tutte le reti consentono il DNS, quindi questa tecnica fa passare dati oltre i controlli pensati per ispezionare il traffico web.

*Il rilevamento si basa su volume e forma. Un singolo host che invia migliaia di query a un dominio si distingue dalla baseline normale, mentre sottodomini insolitamente lunghi suggeriscono un payload codificato.*

**Dove trovare le prove:** record delle query DNS, lunghezza e volume delle query per host, tipi di record poco comuni come TXT e richieste a domini registrati pochi giorni prima.

______

## Attacchi ai dispositivi IoT

**Un attacco basato sull'IoT** prende di mira un dispositivo connesso, come una telecamera, una stampante, un termostato o un sensore. Le credenziali predefinite deboli e gli aggiornamenti firmware rari rendono questi dispositivi un punto d'ingresso comune. Una volta compromesso, un dispositivo entra in una botnet, divulga dati o diventa una via d'accesso alla rete più ampia.

*L'espansione del 5G aggiunge dispositivi connessi su larga scala. Ogni nuovo dispositivo diventa un altro obiettivo con un ciclo di aggiornamento lungo.*

**Dove trovare le prove:** inventario dei dispositivi, pattern delle connessioni in uscita, trasferimenti anomali da un dispositivo con ruolo fisso e differenze tra le versioni firmware dei dispositivi della flotta.

______

## Attacchi basati sull'IA

**Gli attacchi basati sull'IA** applicano l'apprendimento automatico alle attività dell'aggressore.

| Tecnica | Uso |
|---|---|
| **IA/ML avversaria** | Manipola dati o input di addestramento per trarre in inganno un modello |
| **Dark AI** | Applica IA e apprendimento automatico specificamente per sfruttare vulnerabilità |
| **Deepfake** | Genera audio, video o immagini falsi ma realistici |
| **Ingegneria sociale generata dall'IA** | Gestisce conversazioni convincenti via chat o voce su larga scala |

*Una telefonata con voce deepfake o una chat di phishing scorrevole aumenta la credibilità di un vecchio trucco. La tecnica di fondo resta familiare, perciò le competenze di rilevamento basate sul comportamento durano più di quelle legate a un singolo strumento.*

**Dove trovare le prove:** segnali di provenienza dei contenuti, verifica tramite un canale separato per richieste di denaro o accesso e anomalie comportamentali nelle modifiche a identità e pagamenti.

______

## Associare gli attacchi alla telemetria

Ogni categoria alimenta una fonte di dati diversa. La tabella le abbina e offre un punto di partenza per il lavoro di rilevamento.

| Tipo di attacco | Telemetria principale |
|---|---|
| **Malware** | Record EDR di processi, file e registro |
| **Negazione del servizio** | Flussi di rete e monitor di disponibilità |
| **Phishing** | Record del gateway email e dell'analisi degli URL |
| **Spoofing** | Record di autenticazione email e indirizzi di rete |
| **Basato sull'identità** | Record di accesso e protezione delle identità |
| **Iniezione di codice** | Log delle applicazioni web e delle query al database |
| **Catena di fornitura** | Pipeline di compilazione e inventario delle dipendenze |
| **Ingegneria sociale** | Record email, helpdesk e accessi fisici |
| **Minaccia interna** | Record di accesso e trasferimento dei dati |
| **Tunneling DNS** | Record delle query DNS |
| **IoT** | Inventario dei dispositivi e record dei flussi in uscita |
| **Basato sull'IA** | Record di identità, pagamenti e provenienza dei contenuti |

*Inizia il rilevamento dalla colonna della telemetria. Una regola utile nasce da una fonte di dati nota e da un comportamento noto, non dal nome di uno strumento.*

**Le categorie si sovrappongono durante un incidente.** Un messaggio di phishing può causare furto di credenziali, esecuzione di malware e un'intrusione basata sull'identità. Etichetta la tecnica di accesso iniziale, poi registra separatamente i comportamenti successivi. Così un singolo evento non diventa quattro avvisi scollegati e l'indagine ottiene una cronologia più chiara.

______

## Esercitati a rilevarli in un laboratorio

Una categoria resta astratta finché non la osservi in azione. Un laboratorio domestico ti consente di generare l'attività, acquisire la telemetria e confrontare l'avviso con il record grezzo. Il [video sulla carriera che mostra la creazione di un centro operativo di sicurezza](https://www.youtube.com/watch?v=s3g8o7Np1_g) illustra l'intera configurazione per acquisire esperienza professionale prima di essere assunto.

{{< youtube id="s3g8o7Np1_g" >}}

Inizia dalla categoria dell'identità. Crea un utente di prova, abilita la registrazione degli accessi ed esegui una sequenza di accessi non riusciti e riusciti. Poi leggi il record di accesso e annota i campi che distinguono l'uso normale dall'esercizio.

**Un esercizio ripetibile:**

1. **Scegli una categoria** dalla tabella della telemetria qui sopra.
2. **Riproduci una versione innocua** dell'attività sul tuo sistema o account di prova.
3. **Raccogli la telemetria** prodotta dalla categoria.
4. **Scrivi l'idea di rilevamento** come regola, ricerca salvata o query.
5. **Prova la regola** con l'esercizio e verifica che si attivi sul comportamento previsto.
6. **Registra i limiti** della regola, incluse le attività che non rileva.

La guida [Microsoft SOC Home Lab](/articles/microsoft-soc-home-lab-2026/) descrive nel dettaglio la creazione dell'ambiente: licenze, segmentazione della rete, raccolta dei log e test dei controlli d'identità. La guida [Mad Hat Cyber Range](https://madhat.io/pages/cyber-range-guide) amplia la stessa idea con una configurazione da workshop che include un esercizio di attacco, rilevamento e difesa.

Per usare un vocabolario coerente, associa il comportamento osservato alla tecnica pertinente di [MITRE ATT&CK](https://attack.mitre.org/). Considera l'associazione un aiuto per l'analista, non una prova di attribuzione. Conserva con il record dell'esercizio l'evento grezzo, la query, la versione della regola e i punti ciechi noti.

{{< centerbutton href="/articles/microsoft-soc-home-lab-2026/" >}}
  Leggi la guida Microsoft SOC Home Lab
{{< /centerbutton >}}

______

## Prossimi passi

Inizia con una categoria e un esercizio. Aggiungi una seconda categoria dopo aver completato e documentato la prima. L'obiettivo è approfondire una singola indagine, non compilare una lista di strumenti.

- **[Guida Microsoft SOC Home Lab](/articles/microsoft-soc-home-lab-2026/)** crea l'ambiente per questi esercizi.
- **[Creare un laboratorio informatico domestico](/it-career-playbook/getting-started-in-it/building-an-it-home-lab/)** descrive l'infrastruttura alla base di un laboratorio di sicurezza.
- **[Consigli per scrivere un curriculum IT](/it-career-playbook/getting-a-job-in-it/it-resume-writing-tips/)** mostra come presentare un laboratorio documentato come esperienza pratica.
- **[I cinque principali vettori di attacco informatico e le relative mitigazioni](/articles/the-top-five-cyber-attack-vectors-and-mitigations/)** restringe l'elenco ai vettori più frequenti.

**Materiale di riferimento:** le categorie di attacco e i relativi sottotipi seguono la [panoramica di CrowdStrike sugli attacchi informatici comuni](https://www.crowdstrike.com/en-us/cybersecurity-101/cyberattacks/common-cyberattacks/) di Kurt Baker. I collegamenti a prodotti e riferimenti puntano alla documentazione Microsoft.
