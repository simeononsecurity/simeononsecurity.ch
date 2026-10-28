---
title: "1Password SSH Agent and CLI: Accesso in sola lettura per agenti AI"
date: 2026-10-11
lastmod: 2026-10-28
toc: true
draft: false
description: "Progetta un flusso di lavoro SSH in sola lettura con 1Password CLI, SSH Agent e MCP. Utilizza comandi sintetici, permessi ristretti e approvazione umana prima dei test live."
genre: ["System Administration", "Cloud Security", "Automation"]
tags: ["1Password CLI", "SSH keys", "1Password SSH Agent", "MCP", "Model Context Protocol", "agent administration", "systems administration", "Bitbucket Cloud", "Git over SSH", "secret references", "service accounts", "least privilege", "public key authentication", "secret management", "command line security", "automation safety"]
cover: "/img/cover/1password-cli-ssh-keys-mcp-agent-administration.webp"
coverAlt: "Diagramma astratto di un agente che utilizza un riferimento segreto, un SSH agent e strumenti MCP senza mostrare le chiavi private."
coverCaption: ""
---

**Un agente da riga di comando necessita di un accesso utile, non di una copia di ogni credenziale.** Questa guida presenta un design delimitato per 1Password CLI, l'Agente SSH di 1Password, l'accesso Git a Bitbucket e il Model Context Protocol (MCP). Il primo flusso di lavoro utilizza nomi sintetici, azioni solo di lettura e l'approvazione umana al confine SSH.

<!--more-->

La distinzione chiave è semplice. **L'SSH interattivo utilizza il consenso tramite l'Agente SSH di 1Password. L'automazione non presidiata richiede un'identità separata, un accesso ristretto e un ciclo di vita delle chiavi diverso.** Non considerare una connessione MCP come autorizzazione per eseguire uno di questi due flussi di lavoro.

## Punti chiave

- **Protezione della chiave privata:** L'Agente SSH di 1Password esegue l'autenticazione SSH mantenendo le chiavi private all'interno dell'app 1Password.
- **Gestione della chiave pubblica:** Pubblicare solo una chiave pubblica su Bitbucket o su un account remoto. Conservare la metà privata in un elemento Chiave SSH.
- **Consenso interattivo:** Una persona approva un client o una sessione terminale prima che l'Agente SSH utilizzi una chiave.
- **Separazione non presidiata:** Un lavoro pianificato richiede un account di servizio dedicato e un ambito vault ristretto. Un'approvazione dell'Agente SSH interattivo non soddisfa questo requisito.
- **Confini MCP:** MCP collega un agente a strumenti e risorse. Il client, il server, il sistema operativo e la policy di 1Password controllano comunque l'accesso.

## Prima di iniziare

**Prerequisiti:** Installare 1Password 8 e 1Password CLI 2.20.0 o versioni successive. Accedere tramite un account 1Password supportato. Utilizzare un client OpenSSH. Creare un repository di test Bitbucket o un altro target non di produzione. Tenere disponibile un percorso amministrativo secondario per il rollback.

**Tempo:** Da 30 a 45 minuti per una revisione del design e una simulazione sintetica.

**Difficoltà:** Intermedia. Sono necessarie conoscenze base di Git, SSH, shell e controllo degli accessi.

Questa guida copre design e pianificazione. L'articolo collegato su Bitbucket copre i confini di accesso specifici di Bitbucket. Questa guida non testa un account live, non crea una chiave reale, non si connette a un host reale e non registra un server MCP reale. Ogni identificatore qui sotto è sintetico. **Sostituire i segnaposto solo all'interno del proprio ambiente controllato.**

**Postura di versione:** Utilizzare 1Password 8 e [1Password CLI 2.20.0 o versioni successive](https://www.1password.dev/ssh/manage-keys) per questo flusso di lavoro. [1Password CLI 1 è deprecato](https://www.1password.dev/cli/upgrade/). [1Password 7 verrà ritirato all'inizio del 2027](https://support.1password.com/add-account/). La generazione, l'importazione e la condivisione delle chiavi SSH richiedono 1Password 8. Confermare le versioni di Git, OpenSSH, host MCP e server MCP installati prima dei test. Gli esempi qui sotto rimangono non testati.

Una **vault** è una raccolta protetta di elementi 1Password. **OpenSSH** è il software client e server SSH utilizzato da molti sistemi operativi. **MCP**, o Model Context Protocol, collega un agente a strumenti o risorse approvati.

## Perché mantenere le chiavi private non leggibili

Una coppia di chiavi SSH comprende una chiave pubblica e una chiave privata. Un servizio Git remoto o un server memorizza la chiave pubblica. Il client dimostra il possesso della chiave privata durante l'autenticazione. La chiave privata non ha bisogno di essere inviata al servizio remoto.

L'[1Password SSH Agent](https://www.1password.dev/ssh/agent) estende questo modello. La sua documentazione afferma che i client SSH e Git si autenticano tramite l'agente, mentre la chiave privata rimane nell'app 1Password. Il client riceve un risultato di firma, non un file della chiave privata.

Questo confine riduce diversi percorsi di esposizione:

- **Controllo delle versioni:** Una chiave privata non entra in un repository o in una pull request.
- **Cronologia del shell:** Il valore di una chiave privata non appare in un argomento di comando.
- **File temporanei:** Uno script non ha bisogno di scrivere una chiave privata in `~/.ssh/`.
- **Contesto dell'agente:** Un modello linguistico di grandi dimensioni (LLM) non ha bisogno del testo della chiave privata per richiedere un'operazione SSH.
- **Riutilizzo accidentale:** Una chiave copiata non rimane in un vecchio workspace dopo la fine di un compito.

Il confine non rende SSH innocuo. Un processo con il permesso di utilizzare il socket dell'agente potrebbe eseguire azioni come la chiave approvata. La verifica della chiave host, i limiti dell'account remoto, i permessi del repository, la politica dei comandi e l'isolamento dei processi sono ancora importanti.

*Il confine della chiave privata protegge il materiale della chiave. Il confine non approva un comando remoto né dimostra che l'host di destinazione è fidato.*

## Consenso SSH interattivo

Configura una vault dedicata per le chiavi dell'agente. Utilizza il file di configurazione SSH Agent per selezionare il set di chiavi più piccolo e una chiave specifica per host. Non esporre ogni chiave idonea da ogni vault integrata a un processo di automazione.

Il [modello di sicurezza 1Password SSH Agent](https://www.1password.dev/ssh/agent/security) lega l'approvazione a una chiave e a un processo richiedente. Il prompt identifica il processo e la chiave. La persona approva quindi la richiesta tramite il metodo di autenticazione configurato.

1Password documenta diversi ambiti di approvazione. L'approvazione per chiave e per applicazione è il valore predefinito. Un ambito di sessione terminale restringe l'approvazione a una scheda o a una sessione. L'approvazione per richiesta chiede di nuovo per ogni richiesta. Esiste un'opzione di approvazione per tutti i processi, ma questa opzione concede a tutti i processi sotto l'utente del sistema operativo corrente l'accesso per la sessione.

**Utilizza l'ambito di approvazione più ristretto adatto al compito.** Un agente di amministrazione di sistema dovrebbe essere eseguito in un terminale dedicato o in un ambiente sandbox. Non approvare ogni processo quando una singola sessione di terminale è sufficiente.

La sessione di approvazione non è una concessione permanente. 1Password registra l'autorizzazione per il periodo configurato o fino a quando l'app non viene bloccata o chiusa. Quando l'app è bloccata, l'agente non conserva le chiavi private per un uso successivo. Il processo SSH Agent continua in background quando l'impostazione supportata è abilitata mentre 1Password è chiuso, ma una nuova richiesta di firma richiede che 1Password sia sbloccato.

La [guida alla configurazione SSH di 1Password](https://www.1password.dev/ssh/get-started) mostra il flusso generale: generare o importare una chiave, pubblicare la chiave pubblica, abilitare l'agente SSH, configurare il client SSH, eseguire un comando SSH o Git e approvare la richiesta. Il percorso esatto del socket varia in base al sistema operativo. Utilizza le istruzioni della piattaforma corrente invece di copiare un percorso da un'altra macchina.

L'app 1Password deve essere sbloccata prima che una nuova richiesta di firma abbia esito positivo. Il processo dell'agente potrebbe continuare in background mentre l'app è chiusa. Un'app bloccata non rilascia il materiale della chiave privata per la firma.

## Chiavi pubbliche e Bitbucket

La [guida alla gestione delle chiavi di 1Password](https://www.1password.dev/ssh/manage-keys) documenta gli elementi SSH Key, la generazione delle chiavi, l'importazione delle chiavi, le chiavi pubbliche, le impronte digitali e le chiavi private. L'esempio CLI utilizza `op item create --category ssh` per creare un elemento SSH Key. 1Password CLI genera una chiave Ed25519 per impostazione predefinita per questo esempio e oscura la chiave privata nel suo output.

Bitbucket Cloud utilizza il normale flusso di lavoro da riga di comando Git e OpenSSH. La sua [guida alla riga di comando](https://support.atlassian.com/bitbucket-cloud/docs/find-the-command-line/) descrive le operazioni Git da un repository locale. La sua [guida alla configurazione SSH](https://support.atlassian.com/bitbucket-cloud/docs/configure-ssh-and-two-step-verification) elenca le forme remote SSH e i formati di chiave pubblica supportati.

**Tratta Bitbucket come consumatore della chiave pubblica.** Registra la chiave pubblica o l'impronta digitale tramite l'account Bitbucket approvato o l'impostazione del repository. Mantieni la chiave privata in 1Password. Il client Git chiede all'agente SSH di firmare. Il client non legge un file di chiave privata.

Per l'ambito della chiave di accesso Bitbucket, il percorso di registrazione e il test Git in sola lettura, consulta [Bitbucket Cloud SSH Keys and Git CLI: Read-Only Access for AI Agents](/articles/bitbucket-cloud-ssh-keys-git-cli-mcp-agent-automation/).

La documentazione di Bitbucket definisce questo un flusso di lavoro Git CLI. Questo articolo non presuppone un server MCP Bitbucket separato o un prodotto denominato Bitbucket CLI. Un CLI specifico per Bitbucket richiede la propria documentazione aggiornata e la propria revisione dei permessi.

## Il confine tra Agente e MCP

Utilizzare la specifica MCP attuale](https://modelcontextprotocol.io/specification/2026-07-28) quando si esamina un nuovo server.

L'URL della specifica 2025-06-18 nel seguente paragrafo di contesto è una versione storica. Utilizzare la specifica 2026-07-28 per le nuove revisioni.

[MCP](https://modelcontextprotocol.io/specification/2025-06-18) standardizza le connessioni tra un'applicazione LLM, un client connector e un server. Un server offre strumenti, risorse o prompt. La specifica stabilisce inoltre che gli host devono ottenere il consenso dell'utente prima di esporre dati o invocare strumenti.

**MCP stesso non concede autorizzazioni.** Uno strumento MCP viene comunque eseguito all'interno delle autorizzazioni del processo del server, dell'utente del sistema operativo, del percorso di rete, dell'account cloud e delle credenziali configurate. Una descrizione dello strumento non è una politica di autorizzazione.

La [documentazione 1Password Security for AI](https://www.1password.dev/security-for-ai) descrive un Environments MCP Server e modelli di configurazione MCP sicuri. La stessa pagina descrive il caricamento runtime dei valori di configurazione MCP da 1Password. Queste pagine non definiscono un prodotto MCP generico per chiavi SSH di 1Password né un flusso di lavoro SSH universale per ogni client agent.

Utilizzare MCP come superficie di controllo ristretta:

- **Strumenti di lettura:** Ispezionare lo stato del servizio, i metadati del repository o i log approvati.
- **Strumenti di pianificazione:** Preparare un comando o un record di modifica senza eseguire il comando.
- **Strumenti di approvazione:** Richiedere una decisione umana prima di una scrittura remota.
- **Strumenti di scrittura:** Mantenere disabilitati finché destinazione, comando, ambito e piano di rollback non sono espliciti.

L'agente dovrebbe ricevere riferimenti, metadati e risultati delle operazioni. **L'agente non dovrebbe ricevere il testo della chiave privata, un dump completo della vault o un shell illimitato.**

## Una prima politica sicura

Iniziare con una politica scritta prima di abilitare un agente. Mantenere la politica vicino alla configurazione MCP, ma non inserire credenziali nel file.

```yaml
agent_policy:
  purpose: "Read-only repository and system inspection"
  identities:
    interactive_ssh: "1Password SSH Agent with per-terminal consent"
    unattended_jobs: "Dedicated service account with one narrow vault"
  allowed:
    - "Read repository metadata through Git"
    - "Read approved service status and logs"
    - "Run one synthetic SSH connectivity check"
  approval_required:
    - "Any remote write"
    - "Any package, firewall, clock, or service change"
    - "Any new host-key acceptance"
    - "Any private-key export"
  denied:
    - "Read or print private-key fields"
    - "List every vault or every item"
    - "Write tokens or secrets to shell profiles"
    - "Run arbitrary commands from tool output"
  rollback:
    - "Revoke the service account"
    - "Remove the public key from the target"
    - "Disable the MCP server entry"
    - "Lock 1Password and end the agent session"
```

Questa politica è un esempio, non un formato di configurazione 1Password. Conservare la politica reale nel control plane utilizzato dal client agent. Rivedere ogni strumento rispetto alla politica prima di abilitare ciascuno strumento.

## Account di servizio e riferimenti ai segreti

Un **account di servizio** conferisce a un processo automatizzato la propria identità. La [guida agli script 1Password CLI](https://www.1password.dev/cli/secrets-scripts) raccomanda gli account di servizio per l'accesso con privilegi minimi a vault selezionati. Questo separa un lavoro non presidiato dall'SSO, MFA, inventario della vault e account giornaliero di una persona.

Un **riferimento segreto** indica un valore senza inserirlo nel codice sorgente. Il [riferimento CLI di 1Password](https://www.1password.dev/cli/reference) utilizza la forma `op://vault/item/field`. Il riferimento è sicuro da archiviare solo se il processo circostante mantiene un accesso ristretto. Un riferimento non aggira la policy.

Utilizza `op read` quando un comando richiede un singolo valore. Utilizza `op run` quando un processo figlio richiede un insieme controllato di valori di runtime. Utilizza `op item create` quando è necessario che un nuovo elemento SSH Key esista nella vault approvata.

Non confondere l'iniezione di runtime con la protezione della chiave privata. Un token API passato come variabile d'ambiente è comunque visibile al processo figlio. Una chiave privata passata tramite variabile d'ambiente è ancora peggiore, poiché il valore espande l'esposizione all'ispezione dei processi, ai report di crash, all'output di debug, al tracciamento del shell e alla registrazione accidentale.

**Preferisci un riferimento nel sorgente e un valore di runtime nel processo più piccolo possibile.** Mantieni il processo a vita breve. Disabilita il tracciamento del shell. Non stampare l'ambiente. Rimuovi i file temporanei dopo un'esecuzione non riuscita.

## Flusso di lavoro sicuro iniziale

La sequenza seguente separa la registrazione della chiave pubblica, SSH interattivo, scoperta MCP e progettazione non presidiata.

### 1. Definire il target

Annota la classe del target, l'account remoto, il repository o il comando previsto, la fonte della chiave host, il responsabile dell'approvazione e l'azione di rollback. Utilizza un record sintetico durante il primo esercizio.

```text
target_class: test-repository
remote_account: git
operation: read-only connectivity check
host_key_source: approved administrator record
approval_owner: named operator
rollback: remove public key and revoke test identity
```

**Risultato atteso, non testato:** Il record identifica un singolo target e una singola operazione. Il record non contiene hostname, indirizzo IP, token, chiave privata o dati personali.

### 2. Creare o selezionare l'elemento SSH Key

La [guida ufficiale alle chiavi SSH di 1Password](https://www.1password.dev/ssh/manage-keys) documenta il modello di creazione tramite CLI. Il comando seguente utilizza un titolo sintetico e una vault di test nominata.

```bash
op item create --category ssh --ssh-generate-key=ed25519 --vault "synthetic-test-vault" --title "synthetic-agent-admin-key"
```

**Output atteso, non testato:** 1Password crea un elemento SSH Key nella vault di test nominata e oscura la chiave privata nell'output del terminale. Il comando modifica lo stato di 1Password. L'output leggibile dall'utente esatto dipende dalla versione della CLI e dallo stato di accesso.

Cattura l'identificatore dell'elemento restituito nel record di test senza copiare il campo della chiave privata. Utilizza l'identificatore o il titolo esatto dell'elemento per letture specifiche di campo solo dopo che lo schema dell'elemento è stato confermato.

Non reindirizzare questo output a un log condiviso. Cattura solo l'identificatore dell'elemento, l'impronta digitale della chiave pubblica e il record di approvazione quando la procedura locale supporta un output strutturato sicuro.

### 3. Gestire la chiave pubblica

Apri l'elemento Chiave SSH in 1Password e usa l'azione Copia chiave pubblica. Usa un riferimento specifico al campo solo dopo aver confermato l'etichetta del campo della chiave pubblica nel tuo account. Non scaricare l'intero elemento.

```bash
PUBLIC_KEY_REF="op://synthetic-test-vault/synthetic-agent-admin-key/synthetic-public-key-field"
op read "$PUBLIC_KEY_REF"
```

**Output atteso, non testato:** Una riga sintetica di chiave pubblica OpenSSH o un valore di chiave pubblica dal campo confermato. Il nome del campo segnaposto sopra non è una garanzia sull'etichetta del campo del tuo elemento.

Registra la chiave pubblica nell'account Bitbucket approvato, nel repository Bitbucket o nell'account remoto. Non incollare mai la chiave privata corrispondente in Bitbucket. La [guida SSH di Bitbucket](https://support.atlassian.com/bitbucket-cloud/docs/configure-ssh-and-two-step-verification) raccomanda anche di registrare la chiave host di Bitbucket prima della prima connessione.

Per Bitbucket, recupera il record della chiave host pubblicata e confronta il record con una copia fidata indipendente prima di aggiungere una riga a `~/.ssh/known_hosts`. Usa il controllo rigoroso dell'host dopo che il confronto è superato. Non accettare una chiave host modificata durante l'esecuzione di un agente.

### 4. Abilita SSH interattivo

Attiva l'Agente SSH di 1Password nell'app desktop. Configura OpenSSH con il valore specifico della piattaforma `IdentityAgent` o `SSH_AUTH_SOCK` dalla [guida di configurazione ufficiale](https://www.1password.dev/ssh/get-started). Limita il primo test a un repository o a un account non di produzione.

Su macOS o Linux, imposta il socket dalla guida di configurazione della piattaforma ed esegui `ssh-add -l`. Su Windows, usa la configurazione del pipe nominato supportato e verifica le chiavi disponibili tramite l'interfaccia dell'Agente SSH di 1Password o un test SSH di Windows documentato. Non presentare `ssh-add -l` come comando di verifica multipiattaforma.

Solo su macOS o Linux:

```bash
ssh-add -l
git ls-remote "<repository-ssh-url>" HEAD
```

**Output atteso, non testato:** Su macOS o Linux, `ssh-add -l` elenca le impronte digitali dall'agente attivo. Su Windows, usa il test del pipe nominato documentato o l'interfaccia dell'Agente SSH di 1Password. Una lettura Git riuscita restituisce un riferimento al commit. Il segnaposto del repository sopra richiede la sostituzione in un test controllato.

Il comando usa un segnaposto per il repository. Sostituisci il segnaposto solo in un test controllato. **Non approvare una richiesta per un target o un processo che non ti aspetti.**

### 5. Aggiungi MCP dopo che il percorso SSH funziona

Prima verifica il client SSH e il target senza MCP. Poi aggiungi un server MCP o un connettore locale in sola lettura. Fornisci all'agente uno strumento come `read_status` o `prepare_command`. Non iniziare con uno strumento shell generico.

La configurazione MCP deve fare riferimento ai valori di runtime tramite il meccanismo di ambiente supportato dal client. La [guida alla sicurezza AI di 1Password](https://www.1password.dev/security-for-ai) descrive la sostituzione dei token di configurazione MCP in testo normale con variabili di ambiente caricate da 1Password. **Mantenere il riferimento o il nome della variabile nella configurazione. Escludere il valore risolto dalla trascrizione dell'agente.**

Questa sezione descrive una progettazione, non una configurazione MCP testata. Nessun client, server, trasporto, versione o fixture è fissato qui. Validare un server in sola lettura in un profilo di test separato prima di collegare un agente a un sistema di produzione.

### 6. Registrare il risultato

Registrare la classe di destinazione, il nome dello strumento, la decisione di approvazione, l'impronta digitale della chiave pubblica, l'esito del comando e il risultato della pulizia. Omettere i valori segretati. Contrassegnare ogni output come osservato o atteso.

**Risultato atteso, non testato:** L'agente legge lo stato, propone un comando limitato, riceve l'approvazione esplicita per la richiesta SSH, completa l'operazione in sola lettura e produce un record senza testo della chiave privata.

## Sequenza di comandi sintetica

La seguente sequenza mostra l'ordine senza utilizzare infrastruttura reale. Questi comandi sono solo esempi. Non sono stati eseguiti durante la preparazione dell'articolo.

```bash
op --version
op item create --category ssh --ssh-generate-key=ed25519 --vault "synthetic-test-vault" --title "synthetic-agent-admin-key"
op read "op://synthetic-test-vault/synthetic-agent-admin-key/synthetic-public-key-field"
# macOS or Linux only
ssh-add -l
git ls-remote "<repository-ssh-url>" HEAD
```

**Output atteso, non testato:**

```text
2.x.y
SSH Key item created. Private key: redacted
ssh-ed25519 AAAA<synthetic-public-key> synthetic-key-label
256 SHA256:<synthetic-fingerprint> synthetic-agent-admin-key (ED25519)
<synthetic-commit-id>        HEAD
```

Il blocco di output è illustrativo. Il blocco non rappresenta un'esecuzione contro un account 1Password, Bitbucket, un provider Git o un host remoto. Un record di produzione dovrebbe archiviare solo metadati approvati e uno stato di successo o fallimento.

## Accesso interattivo rispetto a non presidiato

| Modalità di accesso | Identità | Percorso chiave privata | Modello di approvazione |
|---|---|---|---|
| **SSH interattivo** | Account umano tramite 1Password SSH Agent | La chiave privata rimane nell'app 1Password | L'umano approva un processo, una sessione terminale o una richiesta |
| **Lettura programmata** | Account di servizio dedicato | `op run` fornisce valori di runtime ristretti | Politica del lavoro e ambito dell'account di servizio |
| **SSH programmato** | Identità di automazione dedicata | L'esportazione della chiave rimane una progettazione di ultima istanza | Isolamento del lavoro, breve durata, restrizione dell'host e rotazione |
| **Scrittura agente** | Identità umana o specifica per il compito | Dipende dall'integrazione approvata | Approvazione umana prima di ogni modifica definita |

*Non programmare un flusso di lavoro attorno a un prompt dell'agente SSH interattivo. Utilizzare una progettazione di automazione separata o mantenere il passo operato da un umano.*

Per i lavori non presidiati, crea un account di servizio con accesso a un singolo vault o a un piccolo insieme di elementi. Assegna al lavoro un unico scopo. Utilizza un repository o un account di server dedicato. Aggiungi la verifica delle chiavi host. Imposta un timeout di esecuzione. Registra i metadati delle azioni senza includere segreti. Ruota o revoca l'identità dopo il test.

Se un lavoro non presidiato ha realmente bisogno di una chiave privata SSH, utilizza una chiave di automazione dedicata con un account remoto ristretto e una data di fine documentata. Il recupero della chiave privata tramite `op read` comporta comunque l'esportazione del materiale della chiave attraverso un confine di processo. Questa progettazione ha un raggio d'impatto maggiore rispetto a 1Password SSH Agent. Quando il sistema di destinazione lo supporta, preferisci un'identità di piattaforma, un servizio di deployment o un'altra identità di workload.

## Perché le variabili d'ambiente in testo semplice aumentano il rischio

Le variabili d'ambiente mantengono i segreti fuori dai file sorgente, ma non li rendono invisibili. Un processo figlio legge il proprio ambiente. L'ispezione dei processi, i gestori di arresti anomali, l'output di debug, il tracciamento del shell e i record copiati dei comandi potrebbero esporre i valori.

1Password documenta `op run` come metodo di runtime per caricare riferimenti in un processo figlio. Utilizza `op run` per i valori di cui un processo ha realmente bisogno. Mantieni il processo figlio a vita breve e limita il suo comando. Non passare una chiave privata tramite `SSH_PRIVATE_KEY`, `KEY` o una variabile simile quando l'SSH Agent elimina la necessità di esportazione.

L'ordine più sicuro è:

1. **Utilizza l'SSH Agent** per SSH interattivo.
2. **Utilizza la registrazione della chiave pubblica** per Bitbucket o l'account remoto.
3. **Utilizza `op run`** per un processo figlio non presidiato ristretto.
4. **Utilizza `op read`** per un singolo valore quando un processo figlio non ha bisogno di un ambiente completo.
5. **Esporta una chiave privata** solo dopo un'eccezione scritta, un ambito ristretto, un piano di pulizia e un piano di rotazione.

## Tabella delle decisioni

| Esigenza | Percorso preferito | Motivo per interrompere o riprogettare |
|---|---|---|
| L'utente esegue Git tramite SSH | 1Password SSH Agent | Interrompere se la richiesta indica un processo o una chiave inattesi |
| Registrazione di una chiave del repository | Lettura o compilazione automatica della chiave pubblica | Non copiare mai la chiave privata nel servizio del repository |
| L'agente legge lo stato del servizio | Strumento MCP in sola lettura con ambito a livello di sistema operativo | Interrompere se lo strumento espone un shell illimitato |
| L'agente propone una modifica remota | Strumento di pianificazione seguito dall'approvazione umana | Interrompere se l'obiettivo, il comando o il rollback non sono chiari |
| Il lavoro legge un token API | Account di servizio più `op read` o `op run` | Interrompere se il token entra nel codice sorgente, nei log o in un profilo globale |
| Il lavoro necessita di accesso SSH | Identità del workload o chiave di automazione dedicata | Interrompere se il lavoro richiede una chiave personale o un account ampio |
| La configurazione MCP necessita di un token | Riferimento runtime caricato dal client supportato | Interrompere se un token in testo normale viene commitato nella configurazione |

## Gestione dei guasti

**Richiesta di consenso SSH inattesa:** Negare la richiesta. Verificare il nome del processo, la sessione del terminale, l'impronta digitale della chiave, l'obiettivo del repository e la chiave host. Rivedere la configurazione del client SSH prima di riprovare.

**Socket SSH Agent non disponibile:** Confermare che l'app desktop di 1Password sia installata tramite un metodo supportato, che l'SSH Agent sia abilitato e che il client utilizzi il socket specifico della piattaforma. La [pagina ufficiale SSH Agent](https://www.1password.dev/ssh/agent) elenca i requisiti del sistema operativo e i link per la configurazione del socket.

**Autenticazione a chiave pubblica non riuscita:** Verificare la chiave pubblica selezionata, l'account remoto, i permessi del repository, la chiave host e la configurazione SSH. Utilizzare un confronto dell'impronta digitale pubblica. Non risolvere l'errore esportando una chiave privata non correlata.

**`op read` nega l'accesso:** Verificare l'ambito della vault dell'account di servizio, l'identificatore dell'elemento, il riferimento al campo, lo stato di accesso e lo stato dell'elemento. Ridurre il riferimento a un singolo elemento approvato. Non ampliare l'autorizzazione della vault come prima risposta.

**`op run` espone un valore:** Interrompere il lavoro. Conservare solo il minimo record dell'incidente. Rimuovere i log copiati e i file temporanei secondo la propria procedura di conservazione. Ruotare il segreto o la chiave interessati. Rivedere il tracciamento dello shell, l'ispezione dei processi, i report di crash e la conservazione dei transcript MCP.

**Comportamento imprevisto dello strumento MCP:** Tratta l'output dello strumento come dati non affidabili. Interrompi l'operazione prima di eseguire i comandi suggeriti dall'output. Ispeziona il codice sorgente del server, la configurazione, i permessi e il trasporto. L'host MCP deve ottenere il consenso dell'utente. La specifica fornisce anche indicazioni per gli implementatori riguardo al consenso e ai controlli di accesso, ma il protocollo non sostituisce la tua revisione.

## Rollback e rimozione

Il rollback inizia con la rimozione degli accessi, non con l'eliminazione dei file.

1. **Ferma l'agente o il lavoro pianificato.** Disabilita la voce del server MCP o scollega il client.
2. **Blocca 1Password.** Termina la sessione di autorizzazione SSH interattiva.
3. **Rimuovi la chiave pubblica.** Elimina la chiave di test da Bitbucket, dal repository o dall'account remoto.
4. **Revoca l'account di servizio.** Rimuovi il suo accesso alla vault e invalida il suo token.
5. **Elimina l'elemento Chiave SSH di test** dopo aver confermato che nessun flusso di lavoro approvato utilizza tale elemento.
6. **Rimuovi la configurazione temporanea.** Elimina i riferimenti di test, le sovrascritture dei socket locali e i log generati.
7. **Rivedi le prove.** Conferma che il record di rollback non contenga chiavi private, token o dump dell'ambiente.

*L'eliminazione di un file locale non revoca una chiave pubblica, un account di servizio, un token in cache o un'autorizzazione remota. Rimuovi ogni concessione alla sua fonte.*

## Risoluzione dei problemi

### L'agente richiede una chiave per ogni comando

Verifica l'ambito di autorizzazione selezionato. L'approvazione per singola richiesta è più restrittiva. Una sessione di terminale o applicazione potrebbe essere terminata. 1Password richiede nuovamente l'autorizzazione dopo un evento di blocco o uscita.

### L'agente vede una chiave privata nel suo transcript

Interrompi il flusso di lavoro e ruota la chiave. Ispeziona la risposta del server MCP, il comando shell, il log di debug e il wrapper dello strumento. Sostituisci la lettura delle chiavi private con l'uso di SSH Agent per i task interattivi. Per i job, sostituisci una chiave personale con un'identità dedicata e un'eccezione documentata.

### L'elenco delle chiavi contiene troppe identità

L'agente SSH di 1Password espone le chiavi idonee dalle vault configurate. Utilizza una configurazione dell'agente con ambito specifico o una configurazione SSH specifica per host. La [documentazione dell'agente](https://www.1password.dev/ssh/agent)] nota anche il limite di sei chiavi del server OpenSSH.

### Un comando funziona manualmente ma fallisce in un job

Confronta identità, ambito della vault, ambiente, dati della chiave host, directory di lavoro e presupposti di approvazione. Una sessione interattiva di 1Password include il consenso umano. Un job pianificato non lo include. Progetta il job come una modalità di accesso separata.

### Il server MCP è connesso ma il task fallisce

La connessione non dimostra l'autorizzazione. Verificare la scoperta degli strumenti, le credenziali del server, il consenso del client, i permessi del sistema operativo, l'accesso di rete e i permessi lato target in fasi separate. Mantenere il primo test in sola lettura.

## Prossimi Passi

Utilizzare la specifica MCP corrente del 2026-07-28 per le nuove approvazioni. Qualsiasi link alla specifica del 2025-06-18 presente in questo articolo è contesto storico.

Iniziare con un singolo repository sintetico e uno strumento MCP in sola lettura. Registrare ogni risultato previsto come non testato finché un ambiente controllato non produce evidenze. Successivamente, ripetere il flusso di lavoro con un target non di produzione, un operatore nominato, una chiave host verificata e un registro scritto del rollback.

Leggere il [riferimento CLI di 1Password](https://www.1password.dev/cli/reference) per le opzioni di comando attuali. Leggere [Caricare i segreti negli script](https://www.1password.dev/cli/secrets-scripts) prima di creare l'automazione con account di servizio. Leggere la [specifica MCP](https://modelcontextprotocol.io/specification/2026-07-28) prima di approvare gli strumenti da un nuovo server.

**Mantenere l'SSH interattivo approvato da un operatore umano. Mantenere l'accesso non presidiato separato. Mantenere le chiavi private non leggibili sempre che il target supporti l'autenticazione basata su agente.**
