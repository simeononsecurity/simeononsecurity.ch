---
title: "I migliori harness per agenti AI nel 2026: scegli in base al workflow"
date: 2026-10-06
lastmod: 2026-10-10
toc: true
draft: false
description: "Confronta Deep Agents, Claude Agent SDK, OpenAI Agents SDK, Pydantic AI, Pi e LangGraph per esecuzione degli strumenti, memoria, recupero e impegno di integrazione."
genre: ["Intelligenza artificiale", "Sviluppo software", "Sicurezza AI"]
tags: ["harness per agenti AI", "migliori framework per agenti", "Deep Agents", "Claude Agent SDK", "OpenAI Agents SDK", "Pydantic AI", "agente di coding Pi", "LangGraph", "runtime per agenti", "chiamate agli strumenti", "memoria degli agenti", "gestione del contesto", "esecuzione duratura", "permessi degli agenti", "sicurezza degli agenti AI", "agenti AI locali", "valutazione degli agenti", "human in the loop", "confronto SDK per agenti", "agenti in produzione"]
cover: "/img/cover/ai-agent-execution-components.webp"
coverAlt: "Componenti metallici modulari collegati a un processore centrale luminoso da percorsi turchesi e arancioni su una superficie di lavoro scura"
coverCaption: "Illustrazione concettuale dei componenti che circondano un modello AI."
---

**Deep Agents è la mia prima scelta per un agente generale con modelli configurabili e gestione del contesto integrata.** Claude Agent SDK è adatto a incorporare il comportamento di esecuzione di Claude Code. OpenAI Agents SDK e Pydantic AI meritano una prova per agenti specifici di un'applicazione. Pi preferisce un core piccolo ed estensibile, mentre LangGraph privilegia il controllo esplicito del workflow.

**La scelta migliore dipende dal lavoro che vuoi accettare.** Un assistente di ricerca, un editor di repository e un servizio che gestisce richieste dei clienti richiedono strumenti e regole di recupero diverse. Queste raccomandazioni sono giudizi editoriali basati sulla documentazione ufficiale verificata il **10 ottobre 2026**, non risultati di un benchmark pratico delle prestazioni.

<!--more-->

## Punti chiave

- **Scegli prima l'astrazione:** agente assemblato, SDK applicativo o runtime del workflow.
- **Controlla i confini di esecuzione:** approvazione degli strumenti, isolamento del filesystem e policy di rete risolvono problemi diversi.
- **Prova il recupero:** la cronologia della conversazione da sola non impedisce azioni esterne duplicate.
- **Misura il lavoro accettato:** includi errori, tempo di revisione e infrastruttura nel confronto dei costi.
- **Mantieni esplicito il modello:** cambiare modello e software dell'agente verifica il sistema completo, non solo il software.

## Cosa offre un harness

Un **agent harness è il software attorno a una chiamata al modello.** Prepara il contesto, espone gli strumenti, esegue le azioni approvate, restituisce i risultati e decide quando continuare o fermarsi. In base all'implementazione gestisce anche memoria, delega, permessi e recupero.

Un **modello** propone la prossima azione. Uno **strumento** esegue un'operazione. Un **runtime** esegue e conserva il workflow. Nei prodotti assemblati queste responsabilità si sovrappongono, ma separarle aiuta a trovare le capacità mancanti.

| Componente | Domanda da porsi |
|---|---|
| **Gestione del contesto** | Quali requisiti sopravvivono a un'esecuzione lunga? |
| **Esecuzione degli strumenti** | Chi valida gli argomenti e limita l'autorità? |
| **Archiviazione dello stato** | Cosa sopravvive al riavvio del processo? |
| **Verifica** | Quale prova stabilisce il completamento? |

Considera un **agente di supporto illustrativo** incaricato di controllare un ordine e preparare una richiesta di sostituzione. La lettura dell'ordine, la proposta della sostituzione e l'invio devono avere autorizzazioni separate. Una spiegazione convincente non prova il permesso di inviare la richiesta. Una trascrizione salvata non prova che l'invio sia già avvenuto.

**Ambito:** questa guida confronta software integrabile e opzioni runtime. Per le interfacce quotidiane degli sviluppatori, usa il [confronto tra coding agent CLI](/articles/cli-coding-agents-comparison/) o il [confronto tra coding agent GUI](/articles/gui-coding-agents-comparison/). Un confronto tra SDK non deve diventare di nascosto una classifica tra strumenti terminali ed estensioni degli editor.

## La shortlist pratica

| Requisito iniziale | Prima opzione da valutare | Responsabilità principale che resta a te |
|---|---|---|
| **Agente generale** | Deep Agents | Configurare backend, permessi e modello |
| **Claude Code in un'app** | Claude Agent SDK | Gestire e isolare il processo di esecuzione |
| **Workflow di strumenti applicativi** | OpenAI Agents SDK | Definire strumenti, approvazioni e accettazione |
| **Applicazione Python tipizzata** | Pydantic AI e il suo pacchetto Harness | Scegliere capacità e workspace |
| **Core di coding integrabile e minimale** | Pi SDK | Assemblare estensioni e policy di esecuzione |
| **Workflow duraturo esplicito** | LangGraph | Progettare stato del grafo e recupero |

**Sono punti di partenza diversi.** Deep Agents usa già LangGraph, quindi la scelta non è per forza esclusiva. Pydantic AI separa anche il framework core per agenti dalle capacità assemblate dell'harness. Confronta la quantità di codice applicativo che devi gestire invece di considerare ogni riga una libreria intercambiabile.

**Inizia dal livello più piccolo che supera il test di accettazione.** Usa un framework applicativo tipizzato per chiamate agli strumenti delimitate, un agente assemblato per lavoro aperto su file o ricerca e un grafo esplicito quando recupero e transizioni richiedono stati nominati. Aggiungi memoria, accesso shell o subagenti solo dopo un test che dimostri il limite del livello più semplice.

## Deep Agents: capacità assemblate

**Scegli Deep Agents per primo per un agente che lavora tra file, strumenti e conversazioni lunghe.** La sua [panoramica ufficiale](https://docs.langchain.com/oss/python/deepagents/overview) documenta backend filesystem, trasferimento del contesto, riepiloghi, subagenti e approvazione umana. Si basa su LangChain e sul runtime LangGraph, con integrazioni per più provider di modelli.

**La configurazione determina ancora il comportamento.** La documentazione corrente indica che la pianificazione dei task è opt-in dalla versione 0.7. Non presumere che un tutorial vecchio descriva i default attuali. Registra versione del pacchetto e middleware attivo.

**Controlla con attenzione l'ambito dei permessi.** Le regole filesystem documentate coprono gli strumenti file integrati, non comandi shell arbitrari tramite backend sandbox. Negare uno strumento file non basta se un altro percorso raggiunge lo stesso file. Testa insieme backend e confine shell.

**La mia raccomandazione:** inseriscilo nella shortlist per un servizio di analisi documenti o repository quando vuoi capacità assemblate e scelta del provider. Preferisci un punto di partenza più piccolo per due chiamate API definite e una risposta validata. Ogni strumento aggiuntivo porta comportamento da valutare.

## Claude: esecuzione integrata

**Scegli Claude Agent SDK quando vuoi l'agente Claude Code nella tua applicazione.** Anthropic descrive una libreria Python e TypeScript con lo stesso ciclo di esecuzione, strumenti e gestione del contesto di Claude Code. L'SDK esegue il binario Claude Code in un processo gestito da te. È distinto dal client API base di Anthropic e dai Managed Agents ospitati. [Panoramica Agent SDK](https://code.claude.com/docs/en/agent-sdk/overview).

**Il vantaggio è riusare un sistema di esecuzione esistente.** Operazioni sui file, comandi, hook, permessi, sessioni e subagenti arrivano come capacità documentate. La tua integrazione fornisce il confine applicativo e i controlli di accettazione della task.

**L'hosting resta una decisione tecnica.** Le [indicazioni di deployment](https://code.claude.com/docs/en/agent-sdk/secure-deployment) di Anthropic trattano controlli filesystem, restrizioni di rete e isolamento. Configurali attorno al processo invece di considerare una richiesta di permesso un confine del sistema operativo.

**La mia raccomandazione:** valutalo per automazione di documenti o codice centrata su Claude con molto lavoro su file e comandi. Scegli un'alternativa flessibile sui provider se confrontare modelli locali e più provider ospitati è un requisito centrale.

| Opzione assemblata | Priorità di integrazione |
|---|---|
| **Deep Agents** | Selezione del modello, middleware e configurazione backend |
| **Claude Agent SDK** | Esecuzione di Claude Code dentro un processo applicativo |

## OpenAI: workflow di strumenti applicativi

**Scegli OpenAI Agents SDK per un'applicazione organizzata intorno a funzioni, task delegate e output espliciti.** La sua [panoramica](https://openai.github.io/openai-agents-python/) documenta loop dell'agente, handoff, guardrail, tracing e capacità sandbox-agent. È un'interfaccia per builder, distinta dall'applicazione sviluppatore Codex.

**L'approvazione è un comportamento configurabile.** La [guida human-in-the-loop](https://openai.github.io/openai-agents-python/human_in_the_loop/) descrive run interrotte e stato serializzato per riprendere dopo una decisione. Per strumenti shell e patch locali l'approvazione è opt-in. Un callback da solo non rende obbligatoria l'approvazione.

**Il supporto ai modelli va oltre OpenAI.** La [documentazione dei provider](https://openai.github.io/openai-agents-python/models/) descrive punti di integrazione e adapter esterni. Valida output strutturati, tool calling e trasporto con l'endpoint scelto invece di presumere la parità delle funzioni.

**La mia raccomandazione:** inseriscilo nella shortlist per un servizio le cui azioni utili sono già funzioni applicative ben definite. Recupera un ordine, calcola l'idoneità in codice ordinario e prepara una richiesta strutturata. Tieni autorizzazione e controlli nell'applicazione anche quando il modello sceglie lo strumento successivo.

## Pydantic AI: applicazioni tipizzate

**Scegli Pydantic AI quando tipi Python e output validati sono centrali.** La sua [documentazione core](https://pydantic.dev/docs/ai/overview/) tratta strumenti tipizzati, dependency injection, output strutturati e integrazioni per esecuzione duratura. La validazione stabilisce la struttura richiesta. Non stabilisce la verità di ogni campo.

**Il pacchetto Harness separato aggiunge capacità assemblate.** La sua [documentazione](https://pydantic.dev/docs/ai/harness/) include stack Coder e Researcher, accesso filesystem e shell, memoria e integrazioni workspace. Workspace locale e sandbox isolato sono scelte diverse. Le capacità harness richiedono un workspace invece di sceglierne uno in silenzio.

**La mia raccomandazione:** valuta il framework core per un servizio Python che restituisce record tipizzati. Aggiungi capacità harness quando servono esplorazione del workspace o ricerca aperta. Evita così di dare accesso shell a un servizio bounded senza una necessità concreta.

Per un **agente illustrativo di revisione fatture**, la validazione dello schema controlla che un totale sia numerico e che una valuta appartenga a un insieme consentito. La logica applicativa separata confronta il totale con le righe e verifica le prove della fonte. Entrambi i controlli appartengono alla prova.

| Aspetto applicativo | Test di accettazione |
|---|---|
| **Output strutturato** | Valida i campi e verifica separatamente il loro significato |
| **Pausa di approvazione** | Salva l'azione in attesa e la decisione esatte |
| **Cambio di provider** | Ripeti i test di compatibilità di tool call e output |

## Pi: core piccolo ed estensibile

**Scegli l'SDK di Pi per controllare direttamente un'implementazione compatta di coding agent.** La [documentazione del progetto](https://github.com/earendil-works/pi/tree/main/packages/coding-agent) descrive integrazione SDK e RPC insieme all'interfaccia interattiva. Gli strumenti predefiniti leggono, scrivono, modificano ed eseguono shell, con estensioni per altro comportamento.

**Il minimalismo sposta lavoro sull'integratore.** Pi omette deliberatamente popup di permesso integrati e orchestrazione dei subagenti. La documentazione indirizza a container o estensioni personalizzate per i flussi di conferma. Valuta l'SDK incorporato, non l'interfaccia terminale contro l'editor grafico di un altro vendor.

**La mia raccomandazione:** valuta Pi per un servizio di coding personalizzato se sei pronto a gestire restrizioni di esecuzione, revisione delle estensioni e policy di recupero. Il core piccolo facilita comprensione e modifica del comportamento. È meno adatto quando serve già un sistema di approvazione e orchestrazione assemblato.

## LangGraph: controllo esplicito del workflow

**Scegli LangGraph quando il workflow richiede stato e transizioni espliciti.** La [documentazione sulla persistenza](https://docs.langchain.com/oss/python/langgraph/persistence) distingue checkpoint legati al thread e store tra thread. Un checkpointer persistente supporta il recupero dopo il riavvio. Uno in memoria no.

**LangGraph è una base runtime.** Definisci il workflow e scegli dove collocare il comportamento guidato dal modello. Deep Agents usa già questa base. Scendere a LangGraph ha senso per un controllo più diretto dei percorsi di esecuzione.

**La mia raccomandazione:** inseriscilo nella shortlist per un processo con fasi nominate, pause di revisione e regole di recupero distinte. Un workflow di intake documenti potrebbe estrarre campi, validarli, chiedere revisione e pubblicare un record approvato. Transizioni fisse aiutano quando il modello sceglie il contenuto ma non deve inventare il processo aziendale.

| Fase del workflow | Prova di completamento |
|---|---|
| **Estrazione** | Record candidato collegato alla fonte |
| **Validazione** | Controlli deterministici ed eccezioni |
| **Revisione** | Decisione collegata al candidato specifico |
| **Pubblicazione** | Ricevuta esterna legata all'operazione |

**Gli effetti esterni richiedono un proprio design di recupero.** Salvare lo stato del grafo non rende atomica una transazione remota con il checkpoint. Usa un identificatore dell'operazione e riconcilia il risultato esterno prima di ritentare l'invio.

## Prova ciò che manca

**Una lista di feature è solo un punto di partenza.** Esegui ogni candidato attraverso errori simili al tuo workload. Usa un workspace usa e getta e servizi di test con record sintetici.

| Test | Prova da conservare |
|---|---|
| **Invio interrotto** | Un effetto esterno dopo il recupero |
| **Conversazione lunga** | I requisiti originali restano soddisfatti |
| **Azione rifiutata** | Nessun effetto tramite uno strumento alternativo |
| **Istruzione non attendibile nel documento** | Il testo non acquisisce autorità |
| **Argomenti dello strumento malformati** | Rifiuto prima della mutazione applicativa |
| **Esaurimento del budget** | Arresto delimitato con lavoro parziale ispezionabile |

**Definisci la ripetizione in modo esplicito.** Per un servizio di richieste di sostituzione, ferma il worker dopo l'accettazione della richiesta da parte del servizio di test ma prima del salvataggio locale. Al riavvio il workflow deve cercare l'identificatore dell'operazione, non inviare di nuovo alla cieca. È un test proposto, non un risultato osservato per i prodotti elencati.

**Controlla le prove dopo la compattazione.** Metti un requisito importante all'inizio del task e fornisci materiale realistico sufficiente ad attivare la strategia di contesto. Chiedi all'agente artefatto finale e riferimenti alle fonti. La nostra [analisi di CLM e memoria degli agenti](/articles/context-language-models-agent-memory-hallucinations/) spiega perché conservare note e conservare prove accurate sono questioni diverse.

**Controlla le destinazioni della telemetria.** Tracce degli strumenti e store della memoria spesso contengono dati della task. Registra quali sistemi li ricevono e per quanto tempo restano disponibili. L'inferenza locale non implica logging, retrieval o esecuzione solo locali.

## Confronta il costo per task accettato

**Usa due percorsi di valutazione.** Un confronto controllato mantiene costanti modello, strumenti, task set e budget quando possibile. Un confronto di deployment usa la configurazione prevista per ogni candidato. Il primo isola alcuni effetti software. Il secondo risponde a quale setup completo serve meglio il tuo lavoro.

**Non forzare configurazioni non supportate nel percorso controllato.** Se manca un modello o un'interfaccia comune, descrivi il confronto come valutazione del sistema. Registra anche effort di setup e guida umana.

```yaml
# Illustrative trial record, not a framework configuration file
candidate: "package and pinned version"
model: "provider and exact model identifier"
workspace: "isolated test environment"
task_set: "frozen fixtures and acceptance checks"
limits:
  elapsed_minutes: 15
  model_calls: 30
  tool_calls: 60
record:
  - accepted_result
  - unsupported_claims
  - duplicate_external_actions
  - inference_cost
  - infrastructure_cost
  - human_review_minutes
  - recovery_outcome
```

**Esegui più prove per task.** Mantieni i tentativi falliti al denominatore e riporta conteggi grezzi insieme alle percentuali. Una prova piccola mostra pattern di errore, non una classifica stabile del settore.

**Calcolo illustrativo dei costi:** setup A spende 12 $ su dieci tentativi e produce otto risultati accettati. Il costo di inferenza per task accettato è 1,50 $. Setup B spende 8 $ e produce quattro risultati accettati, quindi 2,00 $. Nessuna cifra include revisione umana o infrastruttura. Registra questi elementi in un totale separato.

**Definisci prima i fallimenti squalificanti.** Un invio non autorizzato o una fuga di dati tra utenti non deve sparire in un punteggio medio. Dopo aver applicato i requisiti, confronta correttezza, recupero, effort di revisione e costo.

## Fai una scelta delimitata

**Inizia con due candidati e un workflow reale.** Per un agente assemblato flessibile sui provider, confronta Deep Agents con un'alternativa più stretta adatta all'applicazione. Per il comportamento Claude Code in un servizio, prova Claude Agent SDK. Per app tipizzate confronta Pydantic AI e OpenAI Agents SDK. Scegli Pi quando il comportamento personalizzato giustifica il lavoro aggiuntivo. Scegli LangGraph quando il controllo esplicito del workflow è prioritario.

**Prerequisiti della prova:** accesso approvato al modello, fixture sintetiche, workspace isolato quando serve e criteri di accettazione scritti. Dedica un pomeriggio iniziale a setup e test degli errori, poi raccogli run ripetute prima della decisione di produzione. La difficoltà va da intermedia ad avanzata in base ad azioni esterne e recupero.

**Seleziona il sistema più piccolo che soddisfa i requisiti.** Conserva fixture, versioni dei pacchetti e record degli errori. Ripeti i test quando cambi modello, strategia del contesto, strumenti o backend di esecuzione. Questi cambiamenti modificano il sistema valutato.

## Riferimenti

- [LangChain: Deep Agents overview](https://docs.langchain.com/oss/python/deepagents/overview)
- [Anthropic: Claude Agent SDK overview](https://code.claude.com/docs/en/agent-sdk/overview)
- [Anthropic: Secure deployment](https://code.claude.com/docs/en/agent-sdk/secure-deployment)
- [OpenAI: Agents SDK](https://openai.github.io/openai-agents-python/)
- [OpenAI: Human-in-the-loop execution](https://openai.github.io/openai-agents-python/human_in_the_loop/)
- [OpenAI: Model and provider integration](https://openai.github.io/openai-agents-python/models/)
- [Pydantic: AI framework overview](https://pydantic.dev/docs/ai/overview/)
- [Pydantic: AI Harness](https://pydantic.dev/docs/ai/harness/)
- [Earendil: Pi coding-agent SDK and integration modes](https://github.com/earendil-works/pi/tree/main/packages/coding-agent)
- [LangChain: LangGraph persistence](https://docs.langchain.com/oss/python/langgraph/persistence)
