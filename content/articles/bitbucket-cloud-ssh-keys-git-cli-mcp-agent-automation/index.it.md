---
title: "Chiavi SSH di Bitbucket Cloud: accesso Git in sola lettura per agenti AI"
date: 2026-10-11
lastmod: 2026-11-09
toc: true
draft: false
description: "Configura chiavi SSH di Bitbucket Cloud, accesso Git CLI, token REST API, 1Password e strumenti MCP per flussi di lavoro degli agenti AI in sola lettura."
genre: ["Sicurezza cloud", "Strumenti per sviluppatori", "Amministrazione di sistema"]
tags: ["Bitbucket Cloud", "chiavi SSH Bitbucket", "chiavi di accesso al repository", "chiavi di accesso al progetto", "chiavi di accesso all’area di lavoro", "Git CLI", "Bitbucket CLI", "1Password CLI", "1Password SSH Agent", "MCP", "Model Context Protocol", "REST API", "ambiti dei token API", "autorizzazioni degli agenti", "automazione in sola lettura", "chiavi host SSH"]
cover: "/img/cover/bitbucket-cloud-ssh-keys-git-cli-mcp-agent-automation.webp"
coverAlt: "Flusso di lavoro nel terminale che collega accesso Git a Bitbucket Cloud, chiavi SSH con ambito limitato, 1Password, letture REST API e strumenti MCP"
coverCaption: ""
---

**Un flusso di lavoro limitato per gli agenti separa le letture del repository, le letture API, la gestione dei segreti e le scritture remote.** Usa Git tramite Secure Shell (SSH) per accedere ai sorgenti, una chiave di accesso Bitbucket in sola lettura per il checkout automatizzato, l’API REST per i metadati e un server Model Context Protocol (MCP) per gli strumenti approvati. Conserva le chiavi private e i token API in 1Password. Mantieni le scritture dietro un passaggio di approvazione umana.

<!--more-->

## Punti chiave

- **Sola lettura come impostazione predefinita:** usa una chiave di accesso al repository o al progetto per il checkout dell’agente. Nessuna delle due consente il push.
- **Identità personale:** usa una chiave SSH personale per il lavoro interattivo legato a un account utente.
- **Custodia dei segreti:** usa 1Password SSH Agent affinché Git riceva un’operazione di firma senza leggere la chiave privata.
- **Significato di CLI:** considera `git`, `curl` e un piccolo wrapper API verificato come gli strumenti pratici da riga di comando per Bitbucket.
- **Confine MCP:** esponi strumenti di lettura circoscritti. Disabilita gli strumenti di scrittura o mettili dietro un processo di approvazione separato.
- **Gate di scrittura:** consenti all’agente di ispezionare, confrontare e preparare una modifica. Richiedi l’approvazione umana prima di un push, pull request, merge o aggiornamento delle impostazioni.

## Prima di iniziare

**Prerequisiti:** accesso a Bitbucket Cloud, Git, un client OpenSSH, 1Password 8, 1Password CLI, una CLI autenticata o un account di servizio approvato e un host MCP con controlli di approvazione dei server. Prevedi 45 minuti. Difficoltà: intermedia.

Per il primo test usa un repository di prova. Sostituisci tutti i segnaposto negli esempi. I comandi seguenti sono esempi non testati. Non si riferiscono a un account Bitbucket o a un repository attivo.

**Versioni:** questo articolo offre indicazioni di progettazione, non una procedura operativa vincolata a specifiche versioni. Prima di testare, verifica le versioni installate di Git, OpenSSH, 1Password CLI, Teamwork Graph CLI, host MCP e server MCP. Configura 1Password SSH Agent per il sistema operativo corrente prima di usare `ssh-add -l`.

**Tieni le credenziali fuori da shell, log, URL, remote Git e file sorgente.** Usa segnaposto come `<workspace>`, `<repository>`, `<api-token>` e `<socket-path>`. Non incollare una vera chiave privata in una trascrizione del terminale.

## Scegli il perimetro di accesso

Bitbucket Cloud supporta chiavi di accesso a livello di repository, progetto e area di lavoro. L’ambito determina l’impatto di una chiave copiata. Il [confronto ufficiale delle chiavi di accesso](https://support.atlassian.com/bitbucket-cloud/kb/difference-between-repository-project-and-workspace-access-keys/) descrive direttamente le differenze di autorizzazione.

| Percorso di accesso | Ambito | Possibilità di scrittura | Uso adatto |
|---|---|---:|---|
| **Chiave di accesso al repository** | Un repository | No | Checkout predefinito dell’agente |
| **Chiave di accesso al progetto** | Repository di un progetto | No | Attività di sola lettura per un piccolo gruppo di repository |
| **Chiave di accesso all’area di lavoro** | Repository di un’area di lavoro | Sì | Automazione controllata con un piano di scrittura separato |
| **Chiave SSH personale** | Repository consentiti per un utente | Segue l’account utente | Amministrazione interattiva |
| **Token API** | Ambiti API e portata dell’account basati sull’utente | Dipende dagli ambiti | Letture REST API o attività di scrittura temporanea |

**Inizia dal perimetro utile più ristretto.** Scegli una chiave di accesso al repository quando basta un repository. Scegli una chiave di progetto quando più repository condividono un progetto e basta l’accesso in sola lettura. Considera una chiave dell’area di lavoro un’identità di scrittura, non un’opzione predefinita comoda.

Crea e registra la chiave con l’ambito minimo tramite il percorso corrispondente nelle impostazioni di Bitbucket:

1. Apri Repository settings, Access keys e Add key per un repository. Incolla la chiave pubblica e mantieni l’accesso in sola lettura.
2. Apri Project settings, Access keys e Add key quando più repository necessitano di un’identità di lettura limitata al progetto.
3. Usa una chiave dell’area di lavoro solo in un’area condivisa con un progetto di scrittura approvato. Le aree di lavoro personali non offrono lo stesso percorso a livello di area.
4. Registra etichetta della chiave, ambito, impronta della chiave pubblica, proprietario e data di rotazione. Conserva la chiave privata in 1Password.

Dopo la registrazione esegui un test esatto di connessione in sola lettura:

```bash
git ls-remote git@bitbucket.org:<workspace>/<repository>.git HEAD
```

**Output previsto:** un riferimento al commit per `HEAD`. Esempio non testato. Un risultato positivo dimostra che un’identità SSH consentita ha raggiunto il repository indicato. Non dimostra che sia stata selezionata la chiave registrata né che esistano permessi di scrittura. Ripeti il test dopo la configurazione di una chiave per repository.

Per la custodia delle chiavi private e il consenso di 1Password SSH Agent, consulta [1Password CLI e SSH Agent: chiavi SSH sicure per agenti AI](/articles/1password-cli-ssh-keys-mcp-agent-administration/).

## Definire correttamente “Bitbucket CLI”

L’espressione **Bitbucket CLI** spesso confonde tre interfacce diverse. Tienile separate.

- **Git CLI:** `git clone` e `git fetch` trasferiscono dati del repository tramite SSH o HTTPS. `git diff` confronta file locali o revisioni.
- **Client REST:** `curl` o un wrapper verificato chiama l’API Bitbucket Cloud Representational State Transfer (REST). Un’API è un’interfaccia programmatica per richiedere dati o azioni. Il [riferimento REST API di Bitbucket Cloud](https://developer.atlassian.com/cloud/bitbucket/rest/) elenca risorse per repository, sorgenti, branch, pull request, pipeline e stato.
- **Atlassian CLI:** `acli` è l’interfaccia ufficiale a riga di comando di Atlassian. La [guida introduttiva](https://developer.atlassian.com/cloud/acli/guides/introduction/) descrive il prodotto, mentre il [riferimento dei comandi](https://developer.atlassian.com/cloud/acli/reference/commands/) elenca le superfici `admin`, `jira`, `feedback` e `rovodev`. Il riferimento non documenta comandi Bitbucket Cloud.

**Il riferimento ufficiale dei comandi `acli` di Atlassian non documenta comandi Bitbucket Cloud.** Non inventare un comando come `acli bitbucket clone`. Usa Git per le operazioni Git e REST API per i dati Bitbucket Cloud.

### Teamwork Graph CLI facoltativa

**Atlassian pubblica anche Teamwork Graph CLI, o `twg`.** La sua [panoramica](https://developer.atlassian.com/cloud/twg-cli/) e il [catalogo dei comandi](https://developer.atlassian.com/platform/teamwork-graph/twg-cli/commands/commands-catalog/) documentano famiglie di comandi Bitbucket. Il comando di configurazione è:

```bash
twg setup
```

Il comando di configurazione modifica lo stato di autenticazione locale. Segui le richieste della versione installata per la configurazione facoltativa dei token Bitbucket. Il percorso dei token Bitbucket CLI è separato da Atlassian OAuth. Mantieni la sintassi dei comandi legata alla versione installata e al catalogo corrente. Usa un profilo separato, un token con ambito ristretto, skill installate verificate e approvazione umana per i comandi che modificano dati.

**Risultato previsto, non testato:** il profilo isolato riceve le impostazioni di autenticazione Bitbucket. Registra lo stato precedente del profilo prima della configurazione. Per il rollback, rimuovi le credenziali salvate tramite la procedura documentata di logout o rimozione della configurazione della versione installata.

Se un progetto di terze parti si presenta come Bitbucket CLI, verifica sorgente, processo di rilascio, checksum, percorso di aggiornamento, flusso di autenticazione, ambiti richiesti, destinazioni di rete, gestione dei log e comandi di scrittura. Un nome binario familiare non dimostra supporto del fornitore né autorizzazioni sicure.

## Mantieni le chiavi SSH sotto il controllo di 1Password

[1Password SSH Agent](https://www.1password.dev/ssh/agent) fornisce a Git e ai client SSH le chiavi SSH archiviate in 1Password. Il client esegue una richiesta di firma autorizzata. La chiave privata resta nell’app 1Password, che richiede il consenso prima che un client approvato usi una chiave.

Il [riferimento 1Password CLI](https://www.1password.dev/cli/reference) ha un ruolo diverso. Usa `op` per accesso controllato a elementi, token API, account di servizio e configurazione dell’automazione. Usa SSH Agent per la firma SSH. Evita di esportare una chiave privata in un file temporaneo solo per semplificare un flusso dell’agente.

Controlla lo stato locale della CLI e dell’agente con comandi di sola lettura:

```bash
op --version
ssh-add -l
```

**Output previsto:** una versione di 1Password CLI e una o più impronte di chiavi pubbliche dall’agente attivo. Esempio non testato. Un risultato vuoto di `ssh-add -l` significa che la socket dell’agente selezionata non dispone di chiavi.

Per una nuova chiave, crea un elemento Ed25519 SSH Key in 1Password oppure importa una chiave generata con un processo locale fidato. Assegna un’etichetta basata su scopo, ambito e data di rotazione. Aggiungi solo la chiave pubblica a Bitbucket Cloud. La [guida Linux per le chiavi di accesso al repository](https://support.atlassian.com/bitbucket-cloud/docs/set-up-repository-access-keys-on-linux/) descrive il percorso delle impostazioni e il limite di sola lettura.

## Verifica prima la chiave host di Bitbucket

L’autenticazione dell’utente SSH non prova l’identità del server. Prima di inviare una richiesta di autenticazione, il client deve verificare la chiave host di Bitbucket Cloud. La [guida Atlassian su SSH e verifica in due passaggi](https://support.atlassian.com/bitbucket-cloud/docs/configure-ssh-and-two-step-verification/) elenca le chiavi host pubbliche e mostra l’endpoint ufficiale per recuperare voci known-hosts.

Recupera i dati pubblici della chiave host per il confronto:

```bash
curl --fail --silent --show-error https://bitbucket.org/site/ssh
```

**Output previsto:** righe OpenSSH `known_hosts` per `bitbucket.org`. Esempio non testato. Prima di inserire la riga in `~/.ssh/known_hosts`, confronta la chiave o l’impronta restituita con una copia indipendente e fidata.

Dopo aver aggiunto la voce approvata, usa il controllo rigoroso dell’host:

```sshconfig
Host bitbucket.org
    StrictHostKeyChecking yes
    UserKnownHostsFile ~/.ssh/known_hosts
```

**Non accettare una chiave host modificata durante un’esecuzione dell’agente.** Interrompi l’esecuzione, verifica il registro corrente delle chiavi host Bitbucket Cloud e controlla la voce locale in `known_hosts`. L’accettazione automatica elimina un confine di sicurezza della chiave.

## Seleziona una chiave per repository

Un dispositivo spesso contiene diverse chiavi Bitbucket. Un agente SSH con accesso ampio offre varie identità durante una connessione. Un server o una policy con un limite basso di tentativi di autenticazione potrebbe rifiutare la chiave corretta dopo i tentativi precedenti.

La [guida Atlassian per più chiavi di accesso ai repository](https://support.atlassian.com/bitbucket-cloud/docs/managing-multiple-repository-access-keys-on-one-device/) usa `core.sshCommand` in un file di configurazione Git del repository e `includeIf` nella configurazione Git globale. Segui lo stesso schema con una chiave per repository.

Esempio portabile basato su file:

```ini
# .gitconfig inside one local repository
[core]
    sshCommand = ssh -o IdentitiesOnly=yes -i ~/.ssh/<repository-automation-key>
```

```ini
# ~/.gitconfig
[includeIf "gitdir:~/src/<repository>/"]
    path = ~/src/<repository>/.gitconfig
```

Il blocco sopra è un’eccezione basata su file per una chiave privata destinata a un’identità di automazione dedicata. Non configura 1Password SSH Agent. Per 1Password SSH Agent, configura il valore specifico della piattaforma `IdentityAgent` o `SSH_AUTH_SOCK` indicato nella [guida di configurazione 1Password](https://www.1password.dev/ssh/get-started). Alcune configurazioni OpenSSH usano un file `.pub` come selettore di identità dell’agente. Verifica il supporto della piattaforma prima di usarlo. Una configurazione basata su file richiede il percorso corrispondente alla chiave privata. Non passare mai un file `.pub` a un comando che si aspetta materiale di chiave privata e non esportare una chiave privata personale.

Usa una configurazione esplicita del repository quando un clone locale necessita di una chiave. Usa `includeIf` quando una directory contiene diversi cloni che condividono lo stesso confine di accesso. La [guida per più chiavi](https://support.atlassian.com/bitbucket-cloud/docs/managing-multiple-repository-access-keys-on-one-device/) mostra entrambe le impostazioni nel flusso Bitbucket.

Clona tramite Git su SSH:

```bash
git clone git@bitbucket.org:<workspace>/<repository>.git <local-directory>
```

**Output previsto:** Git crea `<local-directory>` e recupera il repository tramite `bitbucket.org`. Esempio non testato. Una chiave di accesso al repository consente solo clone e pull.

## Usa token API per letture REST limitate

Usa SSH per il trasporto Git. Usa REST API per metadati o operazioni al di fuori del trasporto Git. La [guida alle autorizzazioni dei token API](https://support.atlassian.com/bitbucket-cloud/docs/api-token-permissions/) elenca ambiti del repository come Read, Write, Admin e Delete. Repository Read corrisponde a `read:repository:bitbucket` e non include l’accesso ai pull request.

Per l’automazione in lettura, preferisci un token di accesso Bitbucket per repository o progetto quando l’endpoint richiesto lo supporta. Un token API basato sull’utente conserva l’accesso più ampio dell’account. Usa un token dell’area di lavoro solo se l’attività specifica il confine più ampio. Consulta la [guida ai token di accesso Bitbucket](https://support.atlassian.com/bitbucket-cloud/docs/access-tokens/) prima di scegliere il tipo di token.

Per il percorso di lettura dell’agente, inizia con `read:repository:bitbucket`. Aggiungi `read:pullrequest:bitbucket` solo quando servono dati dei pull request. Aggiungi ambiti di area di lavoro o pipeline solo dopo che l’attività specifica endpoint e risultato. Gli ambiti di scrittura e amministrazione richiedono un processo di approvazione separato.

Crea ogni token API per uno scopo, imposta una data di scadenza, registrala nel registro di rotazione e sostituisci il token prima della scadenza. La [guida Atlassian alla creazione dei token API](https://support.atlassian.com/bitbucket-cloud/docs/create-an-api-token/) richiede nome, scadenza, selezione dell’app e ambiti. Il token viene mostrato una sola volta dopo la creazione.

Conserva il valore in 1Password o in un segreto gestito a runtime. Non inserirlo in un URL remoto. Passa un bearer token tramite variabile d’ambiente solo al processo che deve eseguire una lettura:

```bash
op run --env-file=/path/to/agent.env -- \
sh -c 'curl --fail --silent --show-error \
  --request GET \
  --url "https://api.bitbucket.org/2.0/repositories/<workspace>/<repository>" \
  --header "Authorization: Bearer ${BITBUCKET_API_TOKEN}" \
  --header "Accept: application/json"'
```

Tieni `/path/to/agent.env` fuori dal repository. Nel file conserva un riferimento come `BITBUCKET_API_TOKEN=op://synthetic-vault/synthetic-api-token/credential`. `op run` risolve il riferimento ed espone il valore al processo figlio di curl per la durata del sottoprocesso. Non impedisce al processo figlio di leggere o registrare il valore d’ambiente. Non sostituire il segnaposto con un token letterale.

**Output previsto:** metadati JSON del repository selezionato. Esempio non testato. Il segnaposto non deve mai diventare un token reale in un file sottoposto a commit o in un log.

Per automazioni più lunghe, lascia che 1Password inietti il segreto nell’ambiente del processo tramite la CLI supportata o il flusso dell’account di servizio. Mantieni la durata del token adeguata all’attività. Revoca il token se l’attività termina in anticipo o cambia il proprietario dell’host.

## Mantieni ridotta la superficie di lettura MCP

Per esaminare un nuovo server, usa la [specifica MCP corrente](https://modelcontextprotocol.io/specification/2026-07-28) e le sue [regole di autorizzazione](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization). I server HTTP devono controllare il destinatario del token e gestire chiaramente le risposte 401 e 403.

L’host MCP ottiene il consenso dell’utente. Il client mantiene una connessione con un server. Il server espone strumenti, risorse o prompt. Considera ogni server codice non attendibile finché non ne verifichi sorgente, trasporto, account e autorizzazioni.

L’URL della specifica 2025-06-18 nel paragrafo seguente è storico. Per le nuove revisioni usa la specifica corrente 2026-07-28.

La [specifica MCP](https://modelcontextprotocol.io/specification/2025-06-18) definisce la comunicazione tra host, client e server MCP. Un server espone strumenti, risorse o prompt tramite il protocollo. MCP standardizza il formato della connessione. Host, implementazione del server, account, ambito del token e policy di approvazione continuano a decidere dove arriva una chiamata.

Usa un server MCP come adattatore ristretto per Git e Bitbucket Cloud REST API.

Proteggi l’adattatore da inoltro dei token, server-side request forgery (SSRF) e comportamento confused-deputy. SSRF permette a un server di inviare richieste a destinazioni non previste. Il comportamento confused-deputy si verifica quando un server usa privilegi più ampi per conto di chi lo chiama. Proteggilo anche da server locali malevoli, reindirizzamenti OAuth non sicuri e risposte con dati sorgente eccessivi. Fissa le origini Bitbucket consentite e gli identificatori dei repository. Esegui i server locali in una sandbox con un utente del sistema operativo dedicato. Oscura i segreti nei risultati degli strumenti e nei log.

Questa sezione descrive un progetto, non una configurazione MCP testata. Non è fissato alcun client, server, trasporto, versione o fixture. Valida un server di sola lettura in un profilo di test separato prima di collegare un agente a un repository di produzione.

Esempi di strumenti di lettura:

| Strumento | Risultato limitato |
|---|---|
| **`get_repository_metadata`** | Restituisce i metadati di un repository |
| **`read_source_file`** | Legge un percorso a una revisione specifica |
| **`list_branches`** | Elenca i branch di un repository |
| **`get_pull_request`** | Restituisce un pull request dopo che il token dispone dell’ambito di lettura dei pull request |
| **`get_build_status`** | Restituisce i dati di stato di un commit |

Questi nomi descrivono un progetto. Non sono comandi Atlassian. Impedisci al server di accettare URL arbitrari, comandi shell arbitrari, token in chiaro, richieste di esportazione di chiavi private o identificatori di repository senza restrizioni.

Imposta le autorizzazioni su quattro livelli:

1. **Bitbucket Cloud:** chiave di lettura per repository o progetto per Git, più gli ambiti minimi dei token API per le letture REST.
2. **1Password:** un vault o account di servizio dedicato all’attività, senza percorso di esportazione delle chiavi private.
3. **Server MCP:** allowlist di strumenti di lettura, endpoint Bitbucket Cloud fissi, validazione degli input, limiti di timeout e log oscurati.
4. **Host MCP:** approvazione utente del server e di ogni azione che consente scritture, con strumenti di scrittura disabilitati nel profilo predefinito.

*Un elenco di strumenti MCP prova che gli strumenti sono stati individuati. Non prova autorizzazione, ambito corretto, gestione sicura dell’input o correttezza del risultato.*

## Organizza il flusso di lavoro dell’agente

Mantieni esplicito il flusso di lavoro. Ogni fase produce prove per la successiva.

| Fase | Azione dell’agente | Autorizzazione | Controllo umano |
|---|---|---|---|
| **Preparazione** | Legge configurazione, record della chiave host, etichetta della chiave, ambito e scadenza del token | Lettura locale | Approva il record di configurazione |
| **Ispezione** | Clona o recupera tramite Git su SSH e interroga i metadati REST | Lettura repository e API | Nessuno dopo la configurazione |
| **Analisi** | Legge file, branch, pull request e stato delle build tramite strumenti approvati | Strumenti MCP di sola lettura | Nessuno per letture limitate |
| **Preparazione della modifica** | Produce una patch, un piano di branch o una bozza di pull request in uno spazio di lavoro locale | Solo scrittura locale | Esamina diff e destinazione |
| **Approvazione della scrittura** | Presenta azione remota, ambito e rollback esatti | Nessuna scrittura remota | Approvazione umana |
| **Esecuzione della scrittura** | Esegue push di un branch, crea un pull request o chiama un endpoint di scrittura | Identità di scrittura a breve durata | Conferma ogni azione |
| **Verifica** | Legge commit, pull request o stato risultante | Di nuovo sola lettura | Conferma il risultato atteso |

Il profilo predefinito dell’agente dovrebbe fermarsi dopo **Analisi** o **Preparazione della modifica**. Un profilo di scrittura separato dovrebbe usare un token o una chiave diversi, una scadenza breve, una destinazione fissa e una richiesta di approvazione. Una chiave di accesso al repository non può eseguire il passaggio di scrittura, creando un utile confine tecnico.

## Rollback e rimozione

Inizia il rollback rimuovendo l’accesso, poi pulisci la configurazione locale:

1. Rimuovi la chiave di accesso a repository, progetto o area di lavoro nella pagina delle impostazioni Bitbucket corrispondente.
2. Revoca il token API per repository, progetto, area di lavoro o utente nella pagina di sicurezza Bitbucket corrispondente.
3. Rimuovi le credenziali salvate di Teamwork Graph tramite la [procedura di autenticazione documentata](https://developer.atlassian.com/platform/teamwork-graph/twg-cli/getting-started/how-authentication-works/) per la versione CLI installata. Conserva le credenziali precedenti solo nel gestore segreti approvato. Verifica che il profilo isolato non elenchi più le credenziali di test.
4. Al termine del test, rimuovi il file `.gitconfig` del repository e la relativa voce `includeIf`. Non modificare la configurazione Git non correlata.
5. Rimuovi solo la voce verificata della chiave host Bitbucket aggiunta per il test. Mantieni le altre chiavi host approvate.
6. Rimuovi il file esterno `agent.env` e l’output temporaneo. Rimuovi la voce del server MCP dalla configurazione dell’host, quindi riavvia l’host.

Registra ogni rimozione, l’operatore e l’ora. Ruota una chiave o un token se un valore finisce in un log, record di processo o trascrizione non previsti.

## Ciclo di lettura remota e aggiornamento dei riferimenti locali

Usa un ciclo breve per l’ispezione periodica dei repository:

```bash
LOCAL_REPO="<local-directory>"
git -C "$LOCAL_REPO" fetch --no-tags
git -C "$LOCAL_REPO" status --short --branch
git -C "$LOCAL_REPO" log -1 --format='%H %ad %s' --date=iso-strict
```

`HEAD` indica il riferimento attualmente estratto del repository. Un risultato positivo prova che un’identità SSH autorizzata ha raggiunto il repository indicato. Non prova quale chiave sia stata selezionata né se esista accesso push.

**Output previsto:** risultato del fetch, stato del branch e una riga di commit. Esempio non testato. `fetch` non esegue scritture remote, ma aggiorna riferimenti locali e `FETCH_HEAD`. Il ciclo non esegue push né cambia branch.

Il server MCP dovrebbe esporre lo stesso confine di lettura tramite operazioni nominate. Un wrapper shell locale o uno strumento MCP dovrebbe rifiutare un verbo di scrittura prima di inviare una richiesta. Registra nome dello strumento, segnaposto del repository, revisione, classe del risultato e durata. Oscura token, cookie, percorsi privati e contenuti dei file a meno che l’attività richieda esplicitamente un file.

## Risoluzione dei problemi

### `Permission denied (publickey)`

Controlla la socket attiva dell’agente, la chiave pubblica selezionata, la voce di accesso al repository e `IdentitiesOnly`. Una chiave di repository deve essere presente nel repository o progetto di destinazione. Una chiave personale richiede autorizzazioni dell’account. Una chiave dell’area di lavoro ha un diverso confine di scrittura.

### Viene offerta la chiave sbagliata per il repository

Usa una chiave per repository con `core.sshCommand`, oppure raggruppa i cloni in una directory gestita da `includeIf`. Elenca le chiavi dell’agente con `ssh-add -l`. Se sono disponibili molte chiavi 1Password, usa un selettore esplicito di identità o un segnalibro SSH di 1Password. La [guida 1Password Agent](https://www.1password.dev/ssh/agent) descrive gli aspetti legati al numero di chiavi e ai segnalibri.

### SSH segnala una chiave host modificata

Ferma l’agente. Non eliminare `known_hosts` come prima risposta. Confronta il registro corrente delle chiavi host Bitbucket Cloud con la voce locale usando un canale indipendente. Rimuovi o sostituisci una voce solo dopo che il confronto è riuscito.

### L’API restituisce `401` o `403`

Controlla scadenza e tipo del token, ambito dell’endpoint e confine dell’account o dell’area di lavoro. Un ambito di lettura del repository non include i pull request. Un endpoint di scrittura richiede un ambito di scrittura e un profilo approvato. Non ampliare gli ambiti finché non hai identificato l’endpoint non riuscito.

### L’API restituisce i dati del repository ma nessun pull request

Aggiungi l’ambito minimo di lettura dei pull request a un token nuovo o ruotato. Non riutilizzare un token utente ampio per un server MCP di sola lettura.

### Il server MCP elenca strumenti ma una chiamata non riesce

Separa registrazione del server, connessione, rilevamento degli strumenti, esecuzione e verifica del risultato. Esamina il log del server senza esporre il token. Verifica endpoint e formato dell’input. Riprova una volta dopo aver controllato la connettività. Contrassegna l’operazione come incompleta se fallisce anche il secondo tentativo.

### Un Bitbucket CLI di terze parti chiede accesso ampio

Interrompi l’installazione. Confronta l’accesso richiesto con la registrazione dell’attività. Esamina sorgente, firme o checksum delle release, destinazioni di rete, archiviazione dei segreti e comportamento di scrittura. Il riferimento ufficiale dei comandi Atlassian CLI non dimostra il supporto di un binario Bitbucket di terze parti.

## Passaggi successivi

Crea un breve record di accesso con ambito del repository o progetto, etichetta della chiave, data di verifica della chiave host, ambiti API, scadenza del token, responsabile 1Password, allowlist degli strumenti MCP, policy dei log e approvatore delle scritture.

Esegui un clone di sola lettura, una lettura dei metadati REST e una lettura tramite strumento MCP usando segnaposto nella trascrizione. Confronta i risultati. Mantieni il profilo dell’agente in sola lettura finché il record e i log non vengono approvati.

Quando arriva un’attività di scrittura, prepara prima un diff locale. Presenta branch di destinazione, percorsi modificati, metodo API richiesto, ambito del token e passo di rollback. Usa un’identità di scrittura separata e a breve durata solo dopo che una persona approva l’azione esatta.
