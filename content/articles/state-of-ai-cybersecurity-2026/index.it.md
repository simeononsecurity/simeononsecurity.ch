---
title: "Cybersecurity dell'IA nel 2026: implementare in fretta, proteggere dopo"
draft: false
toc: true
date: 2026-06-26
lastmod: 2026-11-23
description: "Una valutazione dell'adozione della cybersecurity dell'IA, delle lacune operative, delle linee guida attuali e dei controlli pratici per le organizzazioni nel 2026."
tags: ["sicurezza dell'IA", "cybersecurity dell'IA 2026", "prompt injection", "agenti IA", "sicurezza MCP", "catena di fornitura dell'IA", "shadow AI", "red teaming dell'IA", "sicurezza LLM", "osservabilità dell'IA", "IA agentica", "minacce dell'IA", "attacchi dell'IA", "sicurezza dei modelli", "governance dell'IA", "NIST AI 600-1", "OWASP LLM", "MITRE ATLAS", "risposta agli incidenti IA", "sicurezza dell'IA aziendale", "identità IA", "avvelenamento del contesto", "avvelenamento degli strumenti", "autorizzazione dell'IA"]
cover: "/img/cover/state-of-ai-cybersecurity-2026.webp"
coverAlt: "Illustrazione di sistemi di IA interconnessi rappresentati da nodi luminosi su uno sfondo scuro, con linee vivaci che mostrano i collegamenti e ombre che indicano vulnerabilità di sicurezza intorno ad alcuni nodi."
coverCaption: ""
---

Nel 2023, 2024 e 2025 le organizzazioni hanno implementato sistemi di IA a un ritmo che le linee guida difensive, gli strumenti di sicurezza e le pratiche operative non sono riusciti a seguire. **Nel 2026 il risultato è un'ampia superficie di attacco, poco monitorata e collegata a sistemi aziendali reali, mentre le difese sono ancora in fase di costruzione.**

Voglio essere preciso su ciò che mi preoccupa e sul perché. Non è un avvertimento generico sui rischi dell'IA. Descrive l'aspetto concreto della superficie di attacco, le lacune documentate e ciò che le organizzazioni devono affrontare.

## Perché esiste questa lacuna

La sicurezza del software tradizionale è maturata in circa tre decenni. Decenni di esperienza nella risposta agli incidenti, ricerca sulle vulnerabilità, sviluppo di strumenti e conoscenze operative acquisite con fatica hanno prodotto i framework, i prodotti e le pratiche su cui si basano i moderni programmi di sicurezza.

**L'IA generativa aziendale ha raggiunto milioni di implementazioni in produzione in circa due anni.**

Le discipline che rendono efficace la sicurezza del software, come la modellazione delle minacce per architetture specifiche, i modelli di distribuzione rafforzati, i playbook maturi di risposta agli incidenti e le pratiche consolidate di audit e osservabilità, non hanno avuto il tempo di svilupparsi prima che le organizzazioni distribuissero l'IA su larga scala. *Le linee guida sono arrivate dopo la distribuzione. Gli strumenti sono arrivati dopo le linee guida. Le competenze operative sono ancora in evoluzione.*

Non si tratta di attribuire colpe. È una spiegazione del perché le lacune siano strutturali e non accidentali.

## I quattro livelli della sicurezza dell'IA

Gran parte della confusione nelle discussioni sulla sicurezza dell'IA nasce dal trattare documenti di governance, tassonomie delle minacce, linee guida ingegneristiche e controlli operativi come se fossero la stessa cosa. Non lo sono.

**Il livello 1 è la governance.** NIST AI RMF, ISO/IEC 42001 ed EU AI Act operano sul piano organizzativo e dei processi. Descrivono come gestire i rischi dell'IA, strutturare la supervisione e documentare le responsabilità. Sono framework di governance, non controlli tecnici.

**Il livello 2 è la tassonomia delle minacce.** MITRE ATLAS documenta le tattiche avversarie contro i sistemi di IA. OWASP Top 10 for LLMs e OWASP Agentic AI Top 10 elencano classi di attacco specifiche. Questi documenti danno un nome agli attacchi. Non prescrivono difese.

**Il livello 3 è la guida ingegneristica.** Google SAIF, Microsoft AI SDL, OWASP AI Exchange e NIST AI 600-1 forniscono indicazioni per costruire e distribuire l'IA in sicurezza. NIST AI 600-1 è molto più specifico dell'AI RMF di base e tratta prompt injection, avvelenamento dei dati e rischi informativi nelle distribuzioni di IA generativa.

**Il livello 4 è l'operatività.** Monitoraggio, risposta agli incidenti, controlli in fase di esecuzione, logging, privilegi minimi, pipeline di valutazione e governance degli accessi sono pratiche operative. Richiedono processi organizzativi, non solo documentazione.

*La maggior parte delle organizzazioni ha una copertura incompleta dei livelli 3 e 4. È lì che si trova quasi tutto il rischio operativo.*

## Cosa è in produzione

L'IA aziendale nel 2026 non consiste solo in chatbot. I sistemi in produzione includono:

- **Sistemi RAG** che recuperano informazioni da repository interni di documenti, wiki, database e record dei clienti
- **Agenti di assistenza clienti** con accesso a informazioni sugli account e sistemi di gestione dei casi
- **Assistenti interni alla produttività** integrati con e-mail, calendari, file system e piattaforme di comunicazione
- **Strumenti di revisione e generazione del codice** con accesso ai repository sorgente
- **Agenti automatizzati** che eseguono flussi di lavoro pianificati con credenziali per API interne
- **Sistemi che elaborano documenti, contratti e dati finanziari**
- **Modelli di IA integrati nel rilevamento delle frodi, nelle assunzioni e nelle decisioni di controllo degli accessi**

Ogni sistema rappresenta una superficie di attacco diversa. Un sistema RAG collegato alla knowledge base interna è al tempo stesso un rischio di divulgazione delle informazioni e un bersaglio di prompt injection. **Un agente con accesso alla posta elettronica e una credenziale persistente è un processo autonomo con una reale capacità d'azione su sistemi reali.**

*Spesso i team di sicurezza non hanno partecipato alla decisione di distribuire questi sistemi. Molte volte scoprono implementazioni di IA esistenti tramite audit invece che durante la revisione del progetto.*

## L'IA è ora da entrambe le parti

**Le stesse capacità di IA disponibili per il team di sicurezza sono disponibili agli aggressori.**

**Lo sviluppo assistito dall'IA** riduce il tempo necessario per trasformare le divulgazioni pubbliche di vulnerabilità in proof-of-concept funzionanti e strumenti operativi. Per chiunque usi questi strumenti, inclusi gli aggressori, è più rapido passare dalla lettura di una CVE al codice funzionante.

**I contenuti di phishing generati dall'IA** producono e-mail con una grammatica migliore, un contesto più convincente e meno errori rilevabili rispetto a molti attacchi scritti da persone. I segnali di formattazione e gli schemi linguistici che gli utenti hanno imparato a riconoscere sono meno affidabili quando il contenuto è generato dall'IA.

**La clonazione vocale per campagne di vishing** imita dirigenti e colleghi durante chiamate in tempo reale. La soglia di ingresso per l'ingegneria sociale mirata è scesa con il miglioramento della sintesi vocale e la diminuzione dei costi di accesso.

**I video deepfake per la compromissione della posta aziendale** sono passati dalla teoria all'operatività. Dal 2024 sono state documentate in più settori frodi finanziarie che usano video di dirigenti generati dall'IA per autorizzare transazioni. *La formazione di sensibilizzazione era stata progettata per un altro modello di minaccia.*

## Prompt injection e avvelenamento del contesto

**Capire la prompt injection è il punto di partenza per comprendere la sicurezza dei sistemi di IA.**

Un modello linguistico segue le istruzioni incorporate nella sua finestra di contesto. Il contesto comprende il prompt di sistema, la cronologia della conversazione, i risultati degli strumenti e i documenti recuperati. **Il modello non distingue in modo affidabile le istruzioni dello sviluppatore dell'applicazione da quelle inserite da un aggressore nel contenuto che il modello sta elaborando.** Questo è il nucleo della prompt injection secondo la definizione OWASP.

La *prompt injection diretta* prende di mira direttamente l'input del modello. L'utente fornisce testo progettato per sovrascrivere le istruzioni di sistema.

La *prompt injection indiretta* è più grave nelle distribuzioni aziendali. L'agente RAG recupera un documento dalla knowledge base. Il documento contiene istruzioni che dicono all'agente di compiere un'altra azione. Lo strumento di riepilogo elabora una pagina web contenente direttive nascoste. Il bot di assistenza legge un allegato del cliente contenente istruzioni. L'agente elabora le istruzioni e agisce di conseguenza.

**L'avvelenamento del contesto** è una categoria più ampia. Per compromettere il sistema di IA, gli aggressori non devono compromettere il modello. Devono inserire contenuti malevoli nel contesto del modello. Ciò comprende documenti RAG avvelenati, voci di memoria avvelenate, e-mail create in modo malevolo che l'agente elabora, PDF avversari e pagine web controllate dagli aggressori che l'agente di navigazione visita. *Sono situazioni diverse dall'avvelenamento del modello. Il modello è integro. Il contesto no.*

La difesa in profondità riduce questo rischio. Filtri di input, convalida dell'output, ambiti limitati per gli strumenti, esecuzione in sandbox e approvazione umana per le azioni con conseguenze aiutano. **Nessuna di queste difese elimina la classe di attacco.** OWASP, NIST, Anthropic, OpenAI e Microsoft raccomandano approcci stratificati perché nessun singolo controllo è sufficiente.

*Progetta dando per scontato che la prompt injection avrà successo su una certa percentuale degli input. Limita di conseguenza le conseguenze.*

## Agenti IA, confini delle autorizzazioni e problema del raggio d'impatto

Gli agenti differiscono dai chatbot in un modo cruciale dal punto di vista operativo: **eseguono azioni.**

Un agente collegato a e-mail, GitHub, Jira, Slack, Salesforce, AWS e API interne è un processo autonomo con accesso agli stessi sistemi usati dai dipendenti più connessi. **Una prompt injection riuscita contro questo agente non produce una risposta testuale indesiderata. Produce un'azione indesiderata su un sistema reale.**

**Il raggio d'impatto di una compromissione dipende da ciò a cui l'agente può accedere.** La maggior parte delle implementazioni attuali concede agli agenti un accesso molto superiore a quello richiesto da ciascuna attività. Un agente che deve leggere un ticket Jira non dovrebbe avere anche accesso in scrittura al branch principale di GitHub. Un agente che elabora richieste di assistenza non dovrebbe conservare credenziali del sistema di fatturazione.

**L'autorizzazione dell'IA è un problema distinto dall'autorizzazione dell'utente.** Le applicazioni tradizionali chiedono se un utente è autorizzato a compiere un'azione. Le architetture con agenti devono chiedere se questo agente è autorizzato a compiere questa specifica azione per questo specifico utente in questo preciso momento e in base al contesto corrente. La maggior parte delle distribuzioni attuali di agenti non lo implementa.

**L'avvelenamento degli strumenti** è diverso dalla prompt injection. Uno strumento malevolo o compromesso collegato a un agente restituisce descrizioni o dati progettati per modificarne il comportamento. I ricercatori considerano sempre più l'avvelenamento degli strumenti una classe distinta dalla prompt injection, in particolare nelle integrazioni basate su MCP.

*I flussi di approvazione umana dovrebbero essere l'ultima barriera per le azioni degli agenti con conseguenze. Le organizzazioni stanno scoprendo che esiste anche la stanchezza da approvazione. Quando gli agenti chiedono regolarmente l'approvazione per azioni di routine, gli utenti iniziano ad approvare automaticamente senza esaminare la richiesta. La barriera diventa una formalità.*

## L'identità dell'IA è un problema di sicurezza aziendale

**Gli agenti possiedono credenziali.** Token OAuth, chiavi API, credenziali degli account di servizio e ruoli cloud IAM compaiono tutti nelle distribuzioni di agenti IA. Sono identità non umane con accesso reale.

Lacune specifiche nelle distribuzioni attuali:

- **Le credenziali degli agenti spesso hanno una lunga durata** e non vengono ruotate con una cadenza paragonabile a quella degli account di servizio
- **Gli ambiti dei token degli agenti sono spesso più ampi** di quanto richiedano le attività che svolgono
- La registrazione degli audit delle azioni svolte con identità di agente varia notevolmente
- **La fuga di credenziali tramite prompt** è un rischio documentato. Un agente che include le proprie chiavi API nel contesto o negli output le espone a chiunque legga l'output o recuperi la conversazione.
- Gli agenti che ottengono altre credenziali tramite chiamate agli strumenti creano **catene di identità difficili da sottoporre ad audit**

*Gestisci le identità degli agenti come gli account di servizio privilegiati. Oggi ciò richiede un impegno deliberato perché la maggior parte degli strumenti di governance delle identità non supporta in modo nativo i modelli di identità degli agenti IA.*

## La memoria persistente degli agenti crea una superficie di attacco a lungo termine

**Gli agenti con memoria persistente presentano una superficie di attacco assente nei sistemi senza stato.**

Un aggressore che riesce a inserire contenuti nella memoria di un agente costruisce una posizione che persiste tra le sessioni. *L'attacco non deve riuscire in una singola interazione. L'influenza accumulata nella memoria per giorni o settimane condiziona il comportamento futuro dell'agente.* A volte questo è chiamato **attacco a lungo termine o attacco con contesto dormiente**.

Per questo rischio specifico esistono pochissime indicazioni operative. Le organizzazioni che distribuiscono agenti con archiviazione della memoria persistente devono:

- Trattare gli **archivi di memoria come dati di alto valore** che richiedono controlli di accesso
- **Convalidare i contenuti della memoria** prima che gli agenti agiscano su di essi
- Integrare nell'architettura la possibilità di **eseguire audit e ripristinare lo stato della memoria**

## La catena di fornitura dei modelli non è trattata come quella del software

**Le organizzazioni che scaricano modelli preaddestrati da repository pubblici accettano artefatti IA eseguibili provenienti da fonti esterne. I controlli applicati a questi download di solito non sono paragonabili a quelli che le stesse organizzazioni applicano ai pacchetti npm, PyPI o Maven.**

Rischi specifici nei repository di modelli:

- **I file di modelli in formato pickle PyTorch** eseguono codice Python arbitrario durante il caricamento. Ciò è stato sfruttato in attacchi documentati alla catena di fornitura. **SafeTensors** è il formato progettato appositamente per affrontare questo problema. Preferiscilo quando disponibile.
- Loader malevoli che installano dipendenze o eseguono codice di configurazione insieme al modello
- Modelli addestrati su **dataset avvelenati** che producono risultati sottilmente errati in specifici contesti
- Modelli con **backdoor incorporate** che si attivano in determinate condizioni
- **Squatting sui nomi dei repository** per distribuire modelli malevoli con nomi familiari

*Poche organizzazioni mantengono una distinta base del software che copra i loro sistemi di IA.* La maggior parte non sa indicare da quale modello base è partito un sistema di produzione, quale versione dei dati di addestramento è stata usata per il fine-tuning o se i pesi in distribuzione corrispondono a quelli valutati per ultimi. Questo livello di tracciabilità è un prerequisito per una sicurezza significativa della catena di fornitura. Oggi non è diffuso.

## Lo shadow AI crea flussi di dati incontrollati

**Gli account personali dei servizi di IA per consumatori sono il luogo in cui i dati si spostano senza controlli.**

ChatGPT Enterprise, Claude Enterprise e Microsoft Copilot per M365 includono protezioni contrattuali per i dati dei clienti. **Gli account personali di ChatGPT, Claude, Gemini e servizi consumer simili non forniscono queste garanzie per impostazione predefinita.**

I dipendenti che usano account personali per elaborare documenti di lavoro trasferiscono strategie legali, record dei clienti, codice sorgente, proiezioni finanziarie, decisioni sul personale e comunicazioni interne tramite pipeline che l'organizzazione non controlla. *I team di sicurezza spesso non hanno informazioni accurate sul volume di questa attività né sulle categorie di dati coinvolte.*

I controlli DLP non rilevano i dati che passano tramite browser verso un servizio di IA consumer. Le politiche di conservazione dei dati non si applicano alla cronologia delle conversazioni su una piattaforma di terze parti. **Gli obblighi normativi previsti da GDPR, HIPAA, SOX e dalle regole settoriali non cambiano in base al fatto che i dati siano usciti accidentalmente o tramite una scheda del browser.**

*Scoprire la portata reale prima di costruire i controlli è il primo passo necessario. Quasi certamente la tua stima di questo problema è inferiore alla realtà.*

## I sistemi di IA divulgano dati in modi diversi dalle applicazioni tradizionali

**Il recupero eccessivo RAG** restituisce documenti a utenti che non dovrebbero accedervi. Un dipendente pone una domanda. Il componente di recupero restituisce un documento da una sezione riservata della knowledge base. La risposta include informazioni di quel documento. *La violazione del controllo degli accessi si è verificata nel livello di recupero, non in quello applicativo.* Molte implementazioni RAG sono state create senza imporre autorizzazioni a livello di documento corrispondenti a quelle del sistema sorgente.

**La divulgazione del prompt di sistema** rivela le istruzioni operative incorporate nel prodotto di IA. I prompt di sistema devono essere trattati come riservati. La fuga di credenziali tramite prompt, quando le credenziali dell'agente compaiono nel contesto o negli output del modello, è di solito un'esposizione più grave del solo contenuto del prompt di sistema.

**Gli errori di isolamento dell'IA multi-tenant** si verificano quando modelli ottimizzati su dati di più clienti mostrano le informazioni di un cliente nel contesto di un altro. È una categoria di rischio documentata per i prodotti IA SaaS multi-tenant.

**La memorizzazione del modello** porta i modelli a riprodurre alla lettera contenuti dei dati di addestramento. Il rischio non è eliminato, in particolare nei modelli ottimizzati su dataset privati piccoli o non sufficientemente deduplicati. Le organizzazioni che eseguono fine-tuning su dati interni sensibili devono valutare il rischio di memorizzazione per l'approccio e i dati specifici che utilizzano.

## Le organizzazioni non hanno visibilità al momento dell'inferenza

I programmi di sicurezza tradizionali dispongono di un'ampia copertura dei log dell'infrastruttura. **La maggior parte delle distribuzioni di IA non ha una copertura equivalente dei componenti IA.**

Monitorare un modello linguistico o un agente in produzione richiede una telemetria diversa da quella usata per un server applicativo. Le organizzazioni devono raccogliere:

- **Contenuto di prompt e output** in un formato adatto alla revisione delle policy e al rilevamento delle anomalie
- **Log delle invocazioni degli strumenti** da parte degli agenti, con nomi degli strumenti, argomenti e risposte
- **Log di recupero** per sistemi RAG, con query, documenti restituiti e decisioni di controllo degli accessi
- **Segnali di classificazione** dei tentativi di jailbreak e iniezione
- **Monitoraggio della coerenza degli output** per rilevare derive comportamentali tra versioni del modello
- **Schemi di latenza** che potrebbero indicare tentativi di riempimento del contesto

*Molte organizzazioni che hanno distribuito l'IA nel 2023 e 2024 dispongono di codici di stato HTTP e metriche di latenza. In questi ambienti spesso manca la telemetria necessaria per rilevare o indagare un incidente di sicurezza dell'IA. Scoprirlo dopo un incidente è troppo tardi.*

## La risposta agli incidenti IA richiede playbook propri

**I playbook di risposta agli incidenti esistenti coprono endpoint, reti, applicazioni e identità. Non coprono scenari specifici dell'IA.**

Domande che il team IR dovrà affrontare e a cui i playbook attuali non rispondono:

- Come stabilire se un modello è stato avvelenato durante un ciclo di fine-tuning
- Come determinare il raggio d'impatto di una prompt injection indiretta riuscita contro un agente con accesso in scrittura a più sistemi
- Come valutare se i dati di addestramento o di fine-tuning sono stati esfiltrati durante una compromissione della catena di fornitura
- Come stabilire una **baseline comportamentale** del modello da confrontare con il comportamento successivo all'incidente
- Come rispondere quando un aggiornamento del modello di un fornitore terzo introduce un comportamento che sembra intenzionale anziché accidentale
- Come determinare se **la memoria di un agente è stata manipolata nel tempo**

*Questi scenari richiedono preparazione prima che si verifichino. La telemetria deve essere disponibile prima dell'incidente. Le baseline del comportamento del modello devono essere documentate prima che serva confrontarle.*

## Le pipeline di valutazione diventano una pratica ingegneristica standard

La sicurezza dell'IA si affida sempre più a **valutazioni strutturate prima della distribuzione**, invece che solo al monitoraggio successivo.

La valutazione della sicurezza prima della distribuzione include:

- **Test di prompt injection** con dataset consolidati e il caso d'uso specifico
- **Benchmark dei jailbreak** con suite pubblicate di prompt avversari
- **Valutazione della robustezza avversaria** per modelli che prendono decisioni con conseguenze
- **Test di regressione** tra versioni del modello per identificare cambiamenti nel comportamento
- **Valutazione delle policy** rispetto ai requisiti documentati di uso accettabile
- **Esercitazioni di red teaming** condotte da persone che cercano di superare difese specifiche

NIST, CISA, Anthropic, OpenAI, Microsoft e Google si aspettano sempre più spesso queste valutazioni per le distribuzioni ad alto rischio. *Creare pipeline minime di valutazione prima di distribuzioni con conseguenze rilevanti è più fattibile di quanto molte organizzazioni pensino.* OWASP AI Exchange e i framework di valutazione pubblicati dai principali fornitori di IA sono punti di partenza ragionevoli.

## L'inventario degli asset IA è probabilmente incompleto

La gestione tradizionale degli asset copre server, endpoint, applicazioni e dispositivi di rete. **I sistemi di IA introducono categorie di asset che la maggior parte degli inventari non registra ancora.**

Un inventario dei sistemi di IA deve includere:

- Ogni **modello in produzione**, inclusi modelli base, varianti ottimizzate e modelli di embedding
- Tutti i **prompt e le istruzioni di sistema** attivi in produzione
- Ogni **agente** in esecuzione nell'ambiente e gli strumenti a cui può accedere
- Tutti gli **indici RAG**, con le fonti dei dati e i controlli di accesso applicati durante il recupero
- Tutti i **database vettoriali** e i relativi contenuti
- Ogni **server MCP o framework di integrazione equivalente** collegato a qualsiasi agente
- I **servizi IA esterni** chiamati dalle applicazioni, inclusi i dati inviati a ciascuno

*Non puoi governare ciò che non hai inventariato. Nel 2026 la maggior parte delle organizzazioni impegnate nella sicurezza dell'IA scopre asset di cui ignorava l'esistenza.*

## Qual è lo stato reale delle difese

Gli strumenti, i framework e le pratiche di difesa per la sicurezza dell'IA sono in sviluppo attivo e significativo. Lo stato attuale è iniziale, ma in miglioramento.

**NIST AI 600-1** estende l'AI RMF di base per l'IA generativa con indicazioni operative molto più specifiche. Le organizzazioni che mantengono programmi di conformità sull'IA dovrebbero leggere AI 600-1, non solo il framework di base.

**MITRE ATLAS** fornisce documentazione delle TTP avversarie per i sistemi IA in formato ATT&CK. Modellare le minacce prima della distribuzione usando ATLAS produce requisiti di sicurezza più precisi rispetto al solo uso di framework di governance.

**OWASP LLM Top 10** e **OWASP Agentic AI Top 10** offrono oggi le indicazioni pubbliche più specifiche sul piano operativo. Per chi lavora sul campo sono entrambi più utili della maggior parte dei programmi formativi formali.

Il **red teaming dell'IA** prima della distribuzione è sempre più richiesto per i casi ad alto rischio da NIST, CISA e dai principali fornitori di IA. Il mercato esterno dei servizi di red teaming dell'IA esiste già ed è in crescita per le organizzazioni prive di capacità interne.

I prodotti di sicurezza specifici per l'IA che coprono monitoraggio, guardrail, autorizzazione e applicazione delle policy in fase di esecuzione sono nelle prime fasi commerciali. *La categoria esiste e merita una valutazione. Poiché il mercato è giovane, le affermazioni di marketing spesso superano le capacità dimostrate. Valuta i prodotti rispetto alla tua architettura specifica, non rispetto agli scenari descritti dai fornitori.*

## Cosa fare

**Fai l'inventario di ciò che è distribuito.** Scopri cosa è in esecuzione, quali dati può consultare, quali credenziali possiede, quali strumenti chiama e quali azioni esegue. È il prerequisito per tutto il resto.

**Tratta gli agenti IA come account privilegiati.** Applica il principio del privilegio minimo. Limita le credenziali all'accesso minimo necessario per ogni attività. Controlla a cosa può accedere ciascun agente e rimuovi ciò che non serve.

**Implementa l'osservabilità specifica per l'IA prima della distribuzione**, non dopo un incidente. Il logging di prompt e output, delle invocazioni degli strumenti e del recupero è la telemetria minima per l'analisi della sicurezza.

**Valuta l'esposizione allo shadow AI.** Scopri quali servizi di IA usano i dipendenti per il lavoro. Determina quali categorie di dati transitano negli account personali. Definisci policy e controlli sulla base dei risultati reali.

**Applica controlli di accesso a livello di documento nei sistemi RAG.** Se il livello di recupero non applica le regole di accesso dei sistemi sorgente, correggilo prima che mostri un documento riservato a un utente non autorizzato.

**Verifica la catena di fornitura dei modelli.** Documenta ogni modello base in uso. Preferisci SafeTensors ai formati pickle. Applica agli artefatti dei modelli controlli della catena di fornitura paragonabili a quelli delle dipendenze software.

**Governa le identità degli agenti.** Gestisci token OAuth e chiavi API degli agenti con le stesse pratiche di ciclo di vita, revisione degli ambiti e rotazione applicate agli account di servizio privilegiati.

**Crea subito playbook IR specifici per l'IA.** Definisci prima di un incidente come indagare gli scenari specifici dell'IA, quali prove servono e quali opzioni di risposta sono disponibili.

**Esegui valutazioni prima di distribuire l'IA in contesti ad alto impatto.** Se non disponi di strumenti interni, inizia dai framework pubblici disponibili.

*Non considerare la conformità alla governance come una postura di sicurezza. I framework di governance descrivono i processi e la gestione del rischio. Non descrivono sistemi tecnicamente difensivi. Servono entrambi.*

## Riferimenti

- NIST AI Risk Management Framework (AI RMF 1.0), 2023
- NIST AI 600-1: Generative AI Profile, 2024
- OWASP Top 10 for Large Language Model Applications, 2025
- OWASP Agentic AI Top 10
- OWASP AI Exchange
- MITRE ATLAS: Adversarial Threat Landscape for AI Systems
- Google Secure AI Framework (SAIF)
- Microsoft AI Security SDL
- CISA Guidance on AI Cybersecurity, 2024
- ISO/IEC 42001:2023 Artificial Intelligence Management Systems
- EU AI Act, Regulation (EU) 2024/1689
- SafeTensors format documentation, Hugging Face
