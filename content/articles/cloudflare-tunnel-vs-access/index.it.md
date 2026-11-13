---
title: "Cloudflare Tunnel e Access: servono entrambi?"
date: 2026-09-11
lastmod: 2026-11-12
toc: true
draft: false
description: "Scopri le differenze tra Cloudflare Tunnel e Access, scegli la protezione per una dashboard domestica ed evita di pubblicare un'app privata senza autenticazione."
genre: ["Sicurezza di rete", "Self-hosting", "Sicurezza cloud"]
tags: ["Cloudflare Tunnel", "Cloudflare Access", "Cloudflare Tunnel e Access", "Cloudflare Zero Trust", "cloudflared", "applicazioni self-hosted", "sicurezza homelab", "accesso remoto", "provider di identità", "policy di accesso", "autenticazione applicativa", "hostname pubblico", "protezione dell'origine", "tunnel in uscita", "service token", "Service Auth", "MFA", "dashboard privata", "reverse proxy", "CGNAT"]
cover: "/img/cover/cloudflare-tunnel-vs-access.webp"
coverAlt: "Un server domestico si collega attraverso un passaggio trasparente a un gateway cloud con un punto separato di verifica dell'identità."
coverCaption: ""
---

**Cloudflare Tunnel** collega la tua applicazione a Cloudflare. **Cloudflare Access** controlla chi può raggiungerla. Per una dashboard domestica privata esposta con un hostname pubblico, usa entrambi. Un tunnel funzionante da solo non aggiunge un controllo dell'identità. La [guida di Cloudflare alla pubblicazione delle applicazioni](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/) spiega la differenza.

## Punti chiave

- **Spiega il percorso:** distingui il connettore, l'origine e il controllo dell'identità.
- **Configura una policy:** consenti a persone specifiche di accedere a una dashboard privata.
- **Valuta la protezione:** prova percorsi di accesso consentiti, negati e alternativi.
- **Progetta l'accesso:** documenta requisiti separati per visitatori e automazioni.

## Prima di iniziare

**Destinatari:** proprietari di server domestici che vogliono proteggere una dashboard nel browser. L'esempio presuppone un dominio attivo su Cloudflare, un'applicazione web locale funzionante e l'autorizzazione ad amministrare entrambi. **Tempo stimato:** 20–30 minuti per l'esercizio sulle policy dopo la configurazione del connettore. **Difficoltà:** da principiante a intermedia.

**Percorso di lettura:** inizia dai ruoli dei prodotti, segui una richiesta, poi configura e verifica una policy semplice. Concludi scrivendo una specifica di accesso per il tuo servizio.

## Cosa fa ogni prodotto

L'**origine** è il server che esegue l'applicazione. Il connettore **`cloudflared`** avvia connessioni dalla tua infrastruttura verso Cloudflare, quindi l'origine non richiede un indirizzo IP pubblico raggiungibile. Le richieste e le risposte viaggiano poi sulla connessione stabilita. [Panoramica di Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/).

| Domanda | Tunnel | Access |
|---|---|---|
| **Come raggiunge Cloudflare il mio server?** | Stabilisce la connessione | Non sostituisce la connettività con l'origine |
| **Chi ottiene l'accesso?** | Da solo non fornisce un accesso utente | Valuta le policy di accesso configurate |
| **Cosa configuro?** | Connettore e percorso dell'applicazione | Applicazione, provider di identità e policy |
| **Cosa dimostra il successo?** | L'origine è raggiungibile attraverso il percorso | Una richiesta ha soddisfatto la policy configurata |

Un **provider di identità (IdP)** autentica il visitatore. Una **policy Access** definisce un'azione e criteri di corrispondenza. Allow consente l'accesso agli utenti corrispondenti. Bypass disabilita l'applicazione di Access per il traffico corrispondente. [Riferimento alle policy Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/).

## Segui una richiesta del browser

Per **`dashboard.example.com`**, il percorso logico della richiesta è:

```text
Navigatore -> Cloudflare Access -> connessione del tunnel -> cloudflared -> pannello di controllo
                      |
                      +-> provider di identità quando è necessaria l’autenticazione
```

Il **connettore avvia la connessione del tunnel verso l'esterno** dalla tua rete. Le richieste del browser raggiungono poi l'origine attraverso questa connessione già stabilita. Una connessione in uscita che trasporta richieste applicative in entrata è il motivo principale per cui Tunnel funziona senza un normale port forwarding verso l'origine. [Modello di connessione Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/).

**Le autorizzazioni dell'applicazione** richiedono una decisione separata. L'accesso a una dashboard non stabilisce automaticamente chi può modificarne le impostazioni o cancellarne i dati. Se l'applicazione offre ruoli di sola visualizzazione e amministrazione, configurali e testali separatamente.

Per esempio, **un familiare con accesso in sola lettura** deve vedere lo stato dei backup, mentre tu devi poter cambiare le destinazioni. Scrivi questi requisiti prima di scegliere le identità. Due persone che superano lo stesso controllo Access non dovrebbero ottenere automaticamente gli stessi privilegi nell'applicazione.

## Quando servono entrambi

**La protezione dipende dal pubblico.** Confronta queste configurazioni prima di pubblicare un percorso:

| Pubblico previsto | Configurazione suggerita | Verifica prima dell'uso |
|---|---|---|
| **Chiunque legga un sito pubblico** | Tunnel, se serve la connettività con l'origine | L'esposizione pubblica è intenzionale |
| **Tu e alcuni familiari** | Tunnel più Access | Consenti solo le identità previste |
| **Un'origine pubblica esistente** | Access con protezione separata dell'origine | L'accesso diretto all'origine non deve aggirare il controllo |
| **Uno script pianificato** | Tunnel più una policy Service Auth | Il client supporta il metodo di autenticazione |

**Access senza Tunnel** è supportato per un'origine già raggiungibile. Proteggi anche i percorsi alternativi verso il server. Cloudflare consiglia di creare prima l'applicazione Access quando pubblichi una nuova route del tunnel. [Requisiti per le applicazioni self-hosted](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/).

*Per una dashboard domestica privata raggiunta tramite hostname pubblico, inizia con Tunnel e Access.*

## Configura una policy per la dashboard

Usa questa **configurazione guidata** per due visitatori previsti. Sostituisci entrambi gli indirizzi di esempio con identità che controlli. Crea l'applicazione Access prima di aggiungere il percorso pubblico del tunnel.

1. **Applicazione:** apri Zero Trust → Access controls → Applications e crea un'applicazione self-hosted con hostname pubblico.
2. **Hostname:** inserisci l'hostname dedicato alla dashboard. Per questo esempio che copre tutto l'hostname, lascia il percorso senza restrizioni.
3. **Policy:** crea una policy Allow chiamata `Dashboard viewers`.
4. **Selettore d'identità:** aggiungi una regola Include usando Emails e sostituisci `alice@example.com` e `bob@example.com` con i due indirizzi previsti.
5. **Accesso:** seleziona il provider d'identità usato dai visitatori e scegli consapevolmente la durata della sessione.
6. **Percorso:** salva l'applicazione, poi collega l'hostname alla dashboard tramite il tunnel.

Il [flusso ufficiale per le applicazioni](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/) documenta queste impostazioni. **Risultato atteso:** un nuovo visitatore deve autenticarsi prima di raggiungere l'applicazione. Prima di affidarti alla policy, esegui il test per un'identità non autorizzata descritto sotto.

## Interpreta la logica delle regole

**Include** combina alternative con OR. **Require** aggiunge condizioni obbligatorie con AND. **Exclude** rimuove gli utenti corrispondenti. Aggiungere un'altra condizione Include allarga il gruppo idoneo. [Semantica delle regole Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/).

| Frammento della policy | Effetto logico |
|---|---|
| **Include Alice or Bob** | È idonea una delle due identità nominate |
| **Include Alice, Include a country** | Sono idonee anche le persone che corrispondono al paese |
| **Include Alice, Require a country** | Alice deve anche corrispondere alla condizione del paese |

**Esercizio di revisione della policy:** il requisito nomina solo Alice e Bob, ma un collega aggiunge un paese come ulteriore condizione Include. Rifiuta la modifica perché ammette un altro gruppo di persone. La posizione geografica non dimostra che qualcuno appartenga alla tua famiglia.

## Autentica gli script pianificati

Un **service token** contiene un Client ID e un Client Secret per le richieste automatizzate. Configura la policy dell'applicazione affinché accetti il token tramite **Service Auth**. Creare un token senza la policy corrispondente non concede l'accesso all'applicazione. [Service token Cloudflare](https://developers.cloudflare.com/cloudflare-one/access-controls/service-credentials/service-tokens/).

Per uno script di backup o un controllo di monitoraggio, conserva il **segreto** nell'archivio protetto delle credenziali dello strumento. Assegna a ogni integrazione un nome di token distinto e una data di scadenza intenzionale. Ruota o revoca il token quando ritiri l'integrazione. La documentazione dei service token descrive queste operazioni del ciclo di vita.

**Verifica esplicitamente la compatibilità del client.** Uno strumento che si aspetta una risposta API non è necessariamente in grado di gestire l'accesso interattivo dal browser. Prima di scegliere la policy, verifica che supporti gli header delle richieste o un altro metodo di autenticazione previsto.

## Verifica le decisioni di accesso

Considera questi **controlli di accettazione** per la tua implementazione:

| Controllo | Evidenza da registrare |
|---|---|
| **Visitatore disconnesso** | Access intercetta una richiesta da una nuova sessione del browser |
| **Identità consentita** | L'applicazione prevista si carica dopo l'accesso |
| **Identità non consentita** | Un account non elencato non accede all'applicazione |
| **Percorso alternativo** | Vecchi nomi DNS e porte dell'origine non offrono accesso involontario |
| **Automazione** | Il client approvato funziona e una richiesta senza credenziale fallisce |

**Una schermata di accesso visibile** dimostra solo che un percorso ha incontrato l'autenticazione. Verifica anche il caso negato e i percorsi alternativi. Sono controlli suggeriti, non risultati di un esempio distribuito.

## Verifica il confine dell'origine

Un'**origine che si fida dell'identità Access** dovrebbe convalidare il token applicativo firmato. Cloudflare lo inoltra nell'header **`Cf-Access-Jwt-Assertion`**. La sola presenza di un header non ne dimostra l'autenticità. [Convalida JWT di Cloudflare](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/validating-json/).

Un **JSON Web Token (JWT)** contiene claim firmati. Quando integri l'identità Access nell'origine, usa il metodo di convalida documentato, incluso l'issuer e l'audience previsti per l'applicazione. Decodificare un token e leggere il campo email non è una convalida sufficiente.

**Issuer** identifica l'autorità che emette il token. **Audience** identifica l'applicazione a cui è destinato. Verifica la validità e la scadenza del token con una libreria di convalida supportata, invece di implementare i controlli della firma da zero.

**Definisci chiaramente il confine:** identifica dove avviene la convalida e quali percorsi raggiungono l'applicazione. Un vecchio port forwarding o un hostname alternativo richiedono una revisione separata anche se l'hostname principale supera tutti i test del browser.

## Risolvi le discrepanze delle policy

| Osservazione | Prossimo controllo |
|---|---|
| **Un visitatore inaspettato riesce ad accedere** | Verifica le condizioni Include, le policy Bypass e la copertura dell'hostname |
| **Un visitatore previsto viene respinto** | Confronta l'identità autenticata con i valori esatti del selettore |
| **Uno script riceve una pagina di accesso** | Controlla la credenziale e la policy Service Auth |
| **Un utente ammesso modifica le impostazioni** | Verifica i ruoli assegnati dall'applicazione stessa |

**Il comportamento delle sessioni** influisce anche sui nuovi test. Access prevede diverse durate, incluse quelle per applicazione e globali. Registra l'impostazione e usa una sessione nuova quando verifichi una nuova identità. [Gestione delle sessioni Access](https://developers.cloudflare.com/cloudflare-one/access-controls/access-settings/session-management/).

## Scrivi la specifica di accesso

Prepara una **breve specifica** prima di aggiungere un altro servizio:

```text
Servizio e hostname:
Identità umane autorizzate:
Ruoli richiesti nell'applicazione:
Credenziale di automazione e scadenza:
Altri percorsi verso l'origine:
Posizione di convalida dei token Access:
Esito del test con identità consentita:
Esito del test con identità negata:
```

**Criterio di completamento:** un altro amministratore deve capire chi ottiene accesso, come si autentica ogni client e quale evidenza dimostra il rifiuto. Se aggiungi un'integrazione di monitoraggio, aggiorna la voce della credenziale e ripeti il controllo con una richiesta non autenticata.

## Prossimi passi

Segui la [guida di configurazione di Cloudflare Tunnel](/guides/how-to-setup-and-use-cloudflare-tunnels/) per impostare il connettore, poi applica il [flusso ufficiale dell'applicazione Access](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/). Per una connessione cellulare, leggi i [limiti del port forwarding di T-Mobile Home Internet](/articles/t-mobile-home-internet-port-forwarding/) prima di scegliere l'accesso remoto.
