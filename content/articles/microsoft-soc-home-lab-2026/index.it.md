---
title: "Laboratorio SOC Microsoft domestico: acquisisci esperienza in cybersicurezza nel 2026"
date: 2026-09-11
lastmod: 2026-11-27
toc: true
draft: false
description: "Crea un laboratorio SOC Microsoft con Sentinel, Defender, Intune ed Entra. Analizza incidenti, verifica le policy delle passkey e documenta prove per il portfolio."
genre: ["Cybersicurezza", "Sicurezza cloud", "Sviluppo professionale"]
tags: ["laboratorio SOC domestico", "Microsoft Sentinel", "Microsoft Defender XDR", "Defender for Endpoint", "Defender for Cloud", "Defender for Servers", "Microsoft Intune", "Microsoft Entra ID", "laboratorio Azure domestico", "esperienza in cybersicurezza", "analista SOC", "centro operativo di sicurezza", "risposta agli incidenti", "KQL", "Log Analytics", "Conditional Access", "MFA resistente al phishing", "passkey", "sicurezza delle identità", "portfolio di cybersicurezza", "gestione dei costi cloud", "sicurezza degli endpoint"]
cover: "/img/cover/microsoft-soc-home-lab.webp"
coverAlt: "Un portatile mostra cronologie di incidenti di sicurezza su una scrivania domestica, sotto una nuvola con server ed endpoint."
coverCaption: ""
---

Un **laboratorio SOC domestico** offre uno spazio per analizzare gli avvisi, spiegare le prove e testare modifiche difensive. Crea un piccolo ambiente Microsoft, raccogli la telemetria e documenta ogni indagine. Il risultato utile è un’indagine ripetibile supportata da prove.

Questa guida sviluppa l’approccio al laboratorio descritto nel video di carriera nella cybersicurezza di Mad Hat e nel runbook Cyber Range fornito. Usa la documentazione Microsoft per i requisiti dei prodotti e separa configurazione, rilevamento e convalida in attività misurabili.

## Punti principali

- **Inizia in piccolo:** un client Windows gestito e un’identità di test bastano per i primi esercizi.
- **Verifica la telemetria:** vedere un dispositivo o un portale connesso non prova che i log stiano arrivando.
- **Completa l’indagine:** registra l’innesco, le prove, la risposta e il nuovo test.
- **Controlla le spese:** monitora separatamente licenze, conservazione dei dati, rete e calcolo.
- **Descrivi l’esperienza con precisione:** presenta l’ambiente come progetto di laboratorio nel curriculum.

## Prima di iniziare

**Prerequisiti:** nozioni di amministrazione Windows e reti, oltre a familiarità con le macchine virtuali. Usa un tenant Microsoft Entra dedicato e una sottoscrizione Azure riservata al laboratorio. Tieni fuori dall’esercizio identità di produzione, file personali e sistemi del datore di lavoro.

**Impegno stimato:** riserva un fine settimana per la configurazione iniziale, poi pianifica sessioni d’indagine mirate. È una stima di pianificazione. Approvazione della prova, quote e provisioning dei servizi influenzano il tempo effettivo. **Difficoltà:** intermedia.

Prepara un account amministrativo separato e un utente di test senza privilegi. Prima di testare le regole di accesso, crea e verifica l’accesso di emergenza. Assegna privilegi per ogni attività di configurazione, poi usa un account con privilegi inferiori per le indagini di routine.

| Componente | Scopo nel laboratorio |
|---|---|
| **Sentinel** | Gestione delle informazioni e degli eventi di sicurezza (SIEM) per le origini di log collegate |
| **Defender XDR** | Correlazione e indagine tra servizi di sicurezza Microsoft coperti da licenza |
| **Defender for Endpoint** (protezione degli endpoint) | Rilevamento e risposta endpoint sui dispositivi integrati |
| **Intune** | Registrazione dei dispositivi e gestione dei criteri di sicurezza endpoint |
| **Entra ID** | Identità, registri di accesso e valutazione dei criteri di accesso |
| **Defender for Servers** (protezione dei server) | Protezione dei server tramite Defender for Cloud |

## Verifica prima le licenze

**Microsoft 365 E5** è un modo per ottenere un laboratorio esteso, ma l’accesso dipende dai piani di servizio e dalle licenze assegnati agli utenti coinvolti. Office 365 E5 e Microsoft 365 E5 sono pacchetti diversi. La licenza di un amministratore non copre automaticamente ogni utente di test o carico di lavoro. Consulta i [prerequisiti di Defender XDR](https://learn.microsoft.com/en-us/defender-xdr/prerequisites) prima di scegliere una sottoscrizione.

**Sentinel nel portale Defender** funziona senza E5 o Defender XDR. L’aggiunta di XDR comporta requisiti di licenza e configurazione separati. Una vista degli incidenti vuota non dimostra che manchi una licenza E5. La [documentazione di onboarding di Sentinel](https://learn.microsoft.com/en-us/unified-secops/microsoft-sentinel-onboard) descrive entrambe le configurazioni.

**La protezione dei server** segue un percorso di licenza distinto. Defender for Servers si integra con Defender for Endpoint per i carichi server supportati. I sistemi operativi client Windows richiedono una copertura client adeguata. Non dare per scontato che ogni VM Azure abbia automaticamente una licenza server. Consulta la documentazione Microsoft sull’[integrazione di Defender for Endpoint](https://learn.microsoft.com/en-us/azure/defender-for-cloud/integration-defender-for-endpoint).

**Pianifica la prova:** verifica nel tuo account l’idoneità, la scadenza, il rinnovo e i servizi inclusi. Non basare il budget sulla durata promessa di una prova o su un importo mensile fisso citato in un video.

## Pianifica le spese

**I budget Azure** inviano notifiche. Non interrompono i consumi quando raggiungi una soglia. Anche la reportistica dei costi è in ritardo. Crea gli avvisi presto e controlla le spese dopo ogni sessione seguendo la [guida Microsoft per i budget](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/tutorial-acm-create-budgets).

| Categoria di costo | Domanda di pianificazione |
|---|---|
| **Licenze utente** | Quali utenti richiedono quali piani di servizio e quando scadono le prove? |
| **Calcolo** | Quante ore VM richiede ogni esercizio? |
| **Archiviazione** | Quali dischi e snapshot restano dopo l’arresto? |
| **Raccolta log** | Quali tabelle richiedono l’ingestione e per quanto tempo conservare i dati? |
| **Rete** | Il progetto include Bastion a pagamento, IP pubblici o servizi in uscita? |
| **Protezione server** | Quali carichi hanno abilitato un piano Defender a pagamento? |

**Scelta di progetto:** inizia con un client. Aggiungi un server quando un esercizio richiede la telemetria del server. Quattro client e vari server aumentano amministrazione e costi prima di offrire pratica d’indagine utile.

## Crea la rete

**Schema suggerito:** inserisci le risorse Azure in un gruppo con un nome chiaro, ad esempio **`rg-soc-lab`**. Usa sottoreti separate per client e server, regole esplicite per i gruppi di sicurezza di rete e accesso amministrativo privato. La sola separazione delle sottoreti non blocca il traffico tra i carichi.

Per un’istanza dedicata di **Azure Bastion**, rispetta i requisiti SKU, incluso il nome riservato **`AzureBastionSubnet`** e una sottorete **`/26`** o più grande nelle distribuzioni correnti. Developer SKU usa un modello diverso. Consulta le [impostazioni di configurazione Bastion](https://learn.microsoft.com/en-us/azure/bastion/configuration-settings) prima di scegliere.

Mantieni RDP e SSH chiusi a Internet pubblico. Limita il traffico amministrativo al percorso scelto. Consenti la connettività in uscita necessaria per registrazione e telemetria di sicurezza.

**Convalida:** stabilisci l’accesso amministrativo privato e verifica le regole di rete effettive prima di installare i carichi. Se in seguito aggiungi un’applicazione intenzionalmente vulnerabile, lasciala nella rete di esercizio e limita l’accesso ai computer di test.

## Collega Sentinel e i log

**Configurazione del portale:** crea un’area di lavoro Log Analytics e abilita Sentinel. Se non compare nel portale Defender, apri **System > Settings > Microsoft Sentinel > Connect a workspace** (Sistema > Impostazioni > Microsoft Sentinel > Connetti un’area di lavoro). Verifica il tenant e i ruoli Azure ed Entra richiesti nei [prerequisiti di onboarding](https://learn.microsoft.com/en-us/unified-secops/microsoft-sentinel-onboard).

**La raccolta dei log è un passaggio separato.** In Entra, configura le impostazioni diagnostiche per inviare le categorie di attività richieste alla stessa area di lavoro. Inizia con gli accessi interattivi e gli eventi di controllo. La [guida di integrazione dei log Entra](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/howto-integrate-activity-logs-with-azure-monitor-logs) descrive permessi e destinazione.

Il flusso Sentinel attuale supporta anche la connessione tramite il portale Microsoft Defender. Prima di cercare la causa di una tabella vuota, conferma che l’area di lavoro primaria sia quella prevista, che il tenant corrisponda alle identità di test e che l’account abbia i ruoli richiesti. La visibilità nel portale non dimostra l’ingestione. [Onboarding Sentinel nel portale Defender](https://learn.microsoft.com/en-us/azure/sentinel/microsoft-sentinel-onboard)

```kusto
SigninLogs
| where TimeGenerated > ago(24h)
| where UserPrincipalName =~ "soc-test@YOUR-TENANT.onmicrosoft.com"
| project TimeGenerated, UserPrincipalName, AppDisplayName,
          IPAddress, ResultType, ConditionalAccessStatus, CorrelationId
| order by TimeGenerated desc
```

Esegui questo esempio di **Kusto Query Language (KQL)** nella vista Logs dell’area di lavoro dopo aver generato un nuovo accesso di test. Sostituisci l’UPN di esempio con l’utente del laboratorio. Le colonne seguono lo [schema della tabella SigninLogs](https://learn.microsoft.com/en-us/azure/azure-monitor/reference/tables/signinlogs).

**Risultato atteso:** una riga corrispondente all’account e all’ora dell’accesso di test. Se non trovi righe, controlla intervallo temporale, identità, impostazioni di raccolta, destinazione e ritardo d’ingestione. Una tabella assente indica prima un problema di raccolta o dell’area di lavoro, poi un problema di rilevamento.

## Integra il primo endpoint

**L’iscrizione a Intune e l’onboarding EDR** sono verifiche separate. Collega Intune e Defender for Endpoint, iscrivi un client Windows supportato e assegna una policy di onboarding EDR al suo gruppo di laboratorio. La registrazione Entra da sola non conferma nessuna delle due.

In Intune controlla **Endpoint security > Defender for Endpoint** (Sicurezza degli endpoint > Defender for Endpoint (protezione degli endpoint)). Se la connessione non è disponibile, abilita il collegamento Intune nelle funzionalità avanzate per endpoint di Defender. Segui i passaggi specifici della piattaforma nella [guida d’integrazione Intune e Defender](https://learn.microsoft.com/en-us/intune/device-security/microsoft-defender/configure-integration).

| Verifica | Prova da raccogliere |
|---|---|
| **Iscrizione** | Il client compare in Intune con una sincronizzazione recente |
| **Assegnazione della policy** | La policy di onboarding si applica al gruppo di dispositivi previsto |
| **Segnalazione del sensore** | Defender mostra onboarding completato e telemetria recente |
| **Test di rilevamento** | Un test documentato produce il segnale di sicurezza previsto |

**Per i server**, abilita il piano Defender for Servers scelto e la sua integrazione endpoint, poi verifica distribuzione e segnalazione del sensore. Defender for Cloud rileva le macchine anche prima del completamento dell’onboarding. La presenza nell’inventario non basta, come spiega la guida Microsoft al [rilevamento e onboarding delle risorse](https://learn.microsoft.com/en-us/azure/defender-for-cloud/integration-defender-for-endpoint).

## Analizza un avviso di test

**Inizia dal test di rilevamento EDR documentato da Microsoft** sull’endpoint di laboratorio. Segui le [istruzioni di test aggiornate](https://learn.microsoft.com/en-us/defender-endpoint/edr-detection), inclusi prerequisiti della piattaforma e risoluzione dei problemi. Registra l’ora di esecuzione prima di aprire la coda degli avvisi.

Tratta l’avviso generato come un esercizio d’indagine. Il titolo assegnato dal prodotto è solo un punto di partenza. Devi stabilire cosa è successo e sostenere la decisione con prove.

1. **Triage:** identifica origine dell’avviso, dispositivo, account e ora dell’evento.
2. **Ispezione:** esamina albero dei processi, riga di comando, dettagli del file e attività di rete disponibili.
3. **Perimetro:** cerca attività correlate sull’identità di test e sugli altri dispositivi del laboratorio.
4. **Valutazione:** spiega se le prove corrispondono all’esercizio previsto o a un evento estraneo.
5. **Risposta:** documenta la risposta scelta, l’impatto e i passaggi di ripristino. Esegui il contenimento supportato solo quando l’esercizio lo richiede.
6. **Nuovo test:** dopo aver modificato un controllo, ripeti il test pertinente e confronta le prove.

**Non inventare risultati mancanti.** Se l’avviso non arriva, conserva il registro dell’esecuzione e risolvi il problema di raccolta. Se un controllo blocca il test prima dell’evento atteso, documenta il risultato di prevenzione.

## Testa i controlli di identità

**Il phishing adversary-in-the-middle (AiTM)** inserisce un intermediario controllato dall’attaccante nel flusso di accesso. Il runbook fornito usa questo scenario per motivare un’autenticazione più forte. Per il primo esercizio d’identità, prova direttamente il comportamento della policy con il tuo account senza privilegi.

Inizia registrando un accesso legittimo e i relativi dettagli di autenticazione. Consulta il [riferimento Microsoft al rilevamento dei rischi Entra](https://learn.microsoft.com/en-us/entra/id-protection/concept-identity-protection-risks) prima di interpretare i segnali di rischio. Prerequisiti e trattamento differiscono in base al segnale. Un nuovo indirizzo IP o un accesso fallito non garantiscono un avviso AiTM.

**Le passkey (FIDO2)** usano credenziali legate al servizio legittimo invece di codici riutilizzabili inseriti in una pagina di accesso inoltrata. Abilita un profilo passkey adatto al gruppo pilota e registra il metodo prima di applicare una policy. Consulta la [guida Microsoft alla configurazione delle passkey](https://learn.microsoft.com/en-us/entra/identity/authentication/how-to-authentication-passkeys-fido2) per autenticatore supportati e limitazioni.

**Esercizio Conditional Access (accesso condizionale):** crea una policy rivolta soltanto al gruppo pilota del laboratorio, escludi gli account di accesso di emergenza e seleziona **Require authentication strength > Phishing-resistant MFA strength** (livello di autenticazione e MFA resistente al phishing). Inizia in modalità **Report-only (solo report)**, esamina l’impatto e poi abilita la policy. Adatta l’[esempio Microsoft di policy amministratore](https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-admin-phish-resistant-mfa) a un piccolo gruppo di test.

| Verifica | Prova da raccogliere |
|---|---|
| **Policy Report-only (solo report)** | Record di accesso che mostra la valutazione della policy proposta |
| **Policy applicata, metodo più debole** | Una nuova autenticazione richiede un metodo più forte prima di concedere l’accesso |
| **Policy applicata, passkey registrata** | Accesso riuscito che soddisfa la robustezza richiesta |

Usa una nuova autenticazione per ogni confronto e controlla i dettagli della policy. Le sessioni esistenti complicano il confronto. **Ambito della prova:** l’esercizio convalida il requisito di autenticazione. Non dimostra una protezione universale dalla compromissione dell’endpoint o dal furto di una sessione esistente.

## Scrivi prove per il portfolio

**Una voce utile nel portfolio** spiega una decisione affinché un altro analista possa valutarla. Includi una breve descrizione dell’architettura, i prerequisiti di raccolta, la cronologia dell’evento e il ragionamento alla base della risposta.

```text
Esercizio:
Data e intervallo orario UTC:
Ambito del laboratorio e prerequisiti:
Evento scatenante e segnale atteso:
Avviso osservato o prevenzione:
Prove e query:
Identità e dispositivi interessati:
Valutazione e motivazione:
Risposta e ripristino:
Modifica del controllo e nuovo test:
Limiti e attività successive:
```

Sostituisci ogni campo con le tue osservazioni. **Ripulisci le esportazioni:** prima di pubblicare screenshot o risultati delle query, rimuovi credenziali, dati di sessione, informazioni personali e identificatori non necessari.

**Esempio per il curriculum:** «Ho creato un laboratorio di sicurezza Microsoft, collegato i log d’identità a Sentinel, analizzato avvisi di test endpoint e documentato la convalida di Conditional Access». Usa questa descrizione solo dopo aver completato tali attività. Inseriscila in progetti o formazione pratica con date e ambito reali.

Un laboratorio dimostra pratica individuale. **Il lavoro in un SOC di produzione** comprende anche impatto aziendale, escalation, impegni di servizio e coordinamento con altri team. Spiega quali parti hai praticato e quali non fanno ancora parte della tua esperienza.

## Risoluzione dei problemi

| Sintomo | Primo controllo |
|---|---|
| **Area di lavoro assente in Defender** | Stesso tenant, Sentinel abilitato e ruoli d’onboarding richiesti |
| **SigninLogs assente o vuoto** | Categorie diagnostiche, destinazione, nuovi eventi e intervallo temporale |
| **Client assente da Intune** | Prerequisiti e stato d’iscrizione |
| **Dispositivo visibile senza telemetria** | Stato reale di onboarding, integrità del sensore e connettività in uscita |
| **Policy di onboarding non applicata** | Ambito di assegnazione, piattaforma e sincronizzazione recente |
| **Nessun avviso di rischio d’identità** | Prerequisiti del segnale e attività registrata, senza presumere un rilevamento deterministico |
| **Accesso concesso in modo inatteso** | Stato Report-only (solo report), esclusioni, ambito risorse e sessione esistente |
| **Addebiti dopo l’arresto** | Stato di allocazione e risorse fatturate a prescindere dal calcolo |

**Ordine di risoluzione:** dimostra prima che l’evento è avvenuto, poi che la raccolta ha funzionato e infine esamina la logica di rilevamento. Registra ogni guasto e correzione nelle note del progetto.

## Sospendi o rimuovi il laboratorio

**La deallocazione** libera l’allocazione di calcolo della VM. Arrestare solo il sistema operativo guest non garantisce la deallocazione. Controlla lo stato di alimentazione mostrato in Azure e consulta la documentazione Microsoft sugli [stati e la fatturazione delle VM](https://learn.microsoft.com/en-us/azure/virtual-machines/states-billing).

**Le risorse conservate** richiedono comunque una revisione. Dischi, snapshot, servizi di rete, conservazione dei log e sottoscrizioni utente hanno cicli di vita separati. Imposta un promemoria prima della scadenza di ogni prova e controlla il rapporto d’uso successivo alla pulizia.

Prima di eliminare il gruppo di risorse del laboratorio, esporta le prove da conservare e controllane il contenuto. **L’eliminazione del gruppo è distruttiva** per le risorse contenute. Utenti del tenant, policy Intune, policy Conditional Access, sottoscrizioni e impostazioni di sicurezza a livello di sottoscrizione potrebbero richiedere una pulizia separata.

## Passaggi successivi

**Completa un’indagine documentata** prima di aggiungere un altro carico. Poi aggiungi un server, un esercizio d’identità o una regola di rilevamento con una condizione di test chiara. Registra cosa insegna il nuovo componente e quanto costa.

Usa la [guida al laboratorio IT](/it-career-playbook/getting-started-in-it/building-an-it-home-lab/) per esercitarti con l’infrastruttura e la [guida al curriculum IT](/it-career-playbook/getting-a-job-in-it/it-resume-writing-tips/) per presentare il lavoro. Mantieni il progetto successivo abbastanza piccolo da poter spiegare configurazione, prove e pulizia.
