---
title: "Tailscale e Headscale a confronto"
date: 2026-05-24
lastmod: 2026-11-23
toc: true
draft: false
description: "Confronta Tailscale e Headscale per modello di hosting, gestione delle identità, funzionalità, costi, operatività e supporto, e scegli la VPN mesh basata su WireGuard più adatta alle tue esigenze."
genre: ["VPN", "Sicurezza di rete", "Hosting autonomo", "WireGuard", "Zero Trust", "Reti mesh", "Software libero", "Infrastruttura cloud", "Accesso remoto", "Gestione della rete"]
tags: ["tailscale a confronto con headscale", "headscale a confronto con tailscale", "vpn in hosting autonomo", "vpn wireguard", "vpn mesh", "reti zero trust", "alternativa a tailscale", "configurazione di headscale", "confronto tra vpn", "VPN a codice sorgente aperto", "prezzi di tailscale", "funzionalità di headscale", "rete mesh wireguard", "rete privata", "prestazioni delle vpn", "funzionalità di tailscale", "installazione di headscale", "reti mesh", "accesso remoto sicuro", "sicurezza delle vpn", "coordinamento di rete", "tailnet", "distribuzione di vpn", "vpn aziendale", "vpn per homelab", "reti in hosting autonomo", "costo di tailscale", "headscale con docker", "gestione delle vpn", "server di coordinamento wireguard"]
cover: "/img/cover/tailscale-vs-headscale-comparison-guide.webp"
coverAlt: "Illustrazione di una rete mesh con dispositivi interconnessi da linee luminose su uno sfondo scuro. I dispositivi sono rappresentati da icone stilizzate dai colori vivaci che simboleggiano connessioni sicure."
coverCaption: ""
---

## Introduzione

**Tailscale** e **Headscale** sono entrambi server di coordinamento per creare VPN mesh sicure basate su [WireGuard](https://www.wireguard.com/). Tailscale è un servizio commerciale ospitato nel cloud con un piano gratuito generoso, mentre Headscale è un'alternativa open source in hosting autonomo che implementa il protocollo di controllo di Tailscale. Capire le differenze tra queste soluzioni è essenziale per scegliere l'approccio più adatto alle esigenze di rete della tua organizzazione.

La scelta principale riguarda **chi controlla il piano di controllo**. Scegli Tailscale se la priorità è avere servizi gestiti per identità, amministrazione e supporto. Valuta Headscale se l'hosting autonomo e il controllo sui dati di coordinamento giustificano il lavoro operativo aggiuntivo. Le sezioni seguenti confrontano funzionalità, prestazioni, costi, sicurezza e manutenzione.

______

## Come funzionano le VPN mesh e WireGuard

Per capire il confronto, conviene partire dalla tecnologia alla base delle due soluzioni:

### Che cos'è WireGuard?

**WireGuard** è un protocollo VPN moderno ad alte prestazioni che offre:
- **Prestazioni elevate:** Fino a 10 volte più veloce di OpenVPN
- **Superficie di attacco minima:** Circa 4.000 righe di codice, contro le oltre 100.000 di OpenVPN
- **Crittografia moderna:** Curve25519, ChaCha20, Poly1305
- **Integrazione nel kernel Linux:** A partire da Linux 5.6 (2020)

### Che cos'è una VPN mesh?

Una **VPN mesh** crea connessioni peer-to-peer tra i dispositivi, evitando di instradare tutto il traffico attraverso un server centrale:
- **Connessioni dirette:** I dispositivi si collegano direttamente tra loro quando possibile
- **Attraversamento del NAT:** Supera automaticamente firewall e NAT
- **Latenza ridotta:** Evita passaggi superflui attraverso server centrali
- **Prestazioni migliori:** Sfrutta tutta la larghezza di banda disponibile tra i peer

### Il ruolo dei server di coordinamento

WireGuard è un protocollo. Per creare una VPN mesh serve un **server di coordinamento** (o piano di controllo) che:
- Gestisca l'autenticazione e l'autorizzazione dei dispositivi
- Distribuisca le chiavi di cifratura
- Faciliti l'attraversamento del NAT e l'individuazione dei peer
- Gestisca le regole di controllo degli accessi
- Fornisca la risoluzione DNS all'interno della rete

**Tailscale** e **Headscale** sono entrambi server di coordinamento che svolgono queste funzioni.

______

## Panoramica di Tailscale e Headscale

| Aspetto | Tailscale | Headscale |
|--------|-----------|-----------|
| **Tipo** | SaaS commerciale | Open source, in hosting autonomo |
| **Licenza** | Proprietaria (piano gratuito disponibile) | Licenza BSD a 3 clausole |
| **Hosting** | Nel cloud (gestito da Tailscale) | Autonomo (lo gestisci tu) |
| **Prima release** | 2019 | 2020 |
| **Responsabile principale del progetto** | Tailscale Inc. | Juan Font e la comunità |
| **Stelle su GitHub** | Non applicabile (codice chiuso) | Oltre 38.900 (dato del 2026) |
| **Complessità della configurazione** | Molto bassa (5 minuti) | Moderata (30-60 minuti) |
| **Costo mensile (100 utenti)** | Da $0 (gratuito) a $18 per utente (Enterprise) | Solo costi di hosting del server ($5-50 al mese) |
| **Compatibilità del protocollo** | Protocollo Tailscale | Protocollo Tailscale (compatibile) |

______

## Confronto dettagliato delle funzionalità

### Funzionalità di rete di base

| Funzionalità | Tailscale | Headscale | Note |
|---------|-----------|-----------|-------|
| **Rete mesh basata su WireGuard** | ✅ Sì | ✅ Sì | Entrambi usano WireGuard per tutte le connessioni tra peer |
| **Attraversamento automatico del NAT** | ✅ Sì | ✅ Sì | STUN/DERP per una connettività affidabile |
| **Instradamento delle sottoreti** | ✅ Sì | ✅ Sì | Accesso alle reti dietro un gateway |
| **Nodi di uscita** | ✅ Sì | ✅ Sì | Instradamento di tutto il traffico Internet attraverso un nodo |
| **MagicDNS** | ✅ Sì | ✅ Sì | Risoluzione dei nomi all'interno della rete mesh |
| **DNS separato** | ✅ Sì | ✅ Sì | Impostazioni DNS specifiche per determinati domini |
| **Instradamento ad alta disponibilità** | ✅ Sì | ✅ Sì | Passaggio automatico a una rotta alternativa in caso di guasto |
| **Supporto IPv6** | ✅ Completo | ✅ Completo | Indirizzamento IPv6 completo nella rete mesh |
| **Supporto multicast** | ❌ No | ❌ No | Al momento nessuno dei due supporta il multicast |

### Controllo degli accessi e sicurezza

| Funzionalità | Tailscale | Headscale | Note |
|---------|-----------|-----------|-------|
| **Motore ACL** | ✅ Avanzato | ✅ Compatibile | Headscale implementa la sintassi ACL di Tailscale |
| **Controllo degli accessi basato su tag** | ✅ Sì | ✅ Sì | Raggruppamento dei dispositivi tramite tag |
| **Gestione di utenti e gruppi** | ✅ Sì | ✅ Sì | Headscale usa il concetto di «utenti» |
| **OpenID Connect (OIDC)** | ✅ Sì | ✅ Sì | Autenticazione con Google, Okta, Keycloak e altri |
| **Autenticazione SAML** | ✅ Sì (Enterprise) | ❌ No | Solo Tailscale |
| **Tailnet Lock** | ✅ Sì | ❌ No | Impedisce l'uso di server di coordinamento non autorizzati |
| **Verifiche dello stato di sicurezza** | ✅ Sì (beta) | ❌ No | Verifica la conformità dei dispositivi prima di consentire l'accesso |
| **Accesso just-in-time** | ✅ Sì | ❌ No | Privilegi elevati temporanei |
| **Registrazione degli eventi di audit** | ✅ Dettagliata | ⚠️ Di base | Tailscale fornisce log dettagliati |

### Gestione e amministrazione

| Funzionalità | Tailscale | Headscale | Limitazioni |
|---------|-----------|-----------|-------------|
| **Interfaccia web** | ✅ Ufficiale | ⚠️ Della comunità | Per Headscale esistono diverse interfacce sviluppate dalla comunità |
| **Gestione da riga di comando** | ✅ Sì | ✅ Sì | Entrambi offrono strumenti da riga di comando completi |
| **API REST** | ✅ Sì | ✅ Sì | Automazione delle attività di gestione |
| **API gRPC** | ❌ No | ✅ Sì | Headscale offre gRPC per il controllo remoto |
| **Provider Terraform** | ✅ Ufficiale | ❌ No | Integrazione con l'infrastruttura come codice |
| **Operatore Kubernetes** | ✅ Ufficiale | ⚠️ Della comunità | Operatore per Headscale sviluppato dalla comunità |
| **App per dispositivi mobili** | ✅ iOS, Android | ✅ Compatibili | Le app Tailscale funzionano con un server Headscale |
| **Console di amministrazione** | ✅ Completa | ❌ No | Headscale si affida a CLI e API |
| **Accesso per più amministratori** | ✅ Sì | ⚠️ Manuale | Headscale richiede un'implementazione personalizzata |

### Funzionalità avanzate

| Funzionalità | Tailscale | Headscale | Note |
|---------|-----------|-----------|-------|
| **Tailscale SSH** | ✅ Sì | ⚠️ Solo server | I nodi Headscale possono fungere da server SSH, ma non da client |
| **Taildrop (condivisione di file)** | ✅ Sì | ⚠️ Incompleto | Supporto limitato per Taildrop in Headscale |
| **Funnel (accesso pubblico in ingresso)** | ✅ Sì | ❌ No | Espone i servizi su Internet |
| **Serve (condivisione privata)** | ✅ Sì | ❌ No | Condivide i servizi all'interno della tailnet |
| **Inventario dei servizi** | ✅ Sì | ❌ Limitato | Individua i servizi sulla rete |
| **Tailscale DERP** | ✅ Rete globale | ⚠️ Integrato | Headscale integra un relay DERP e consente di usarne uno personalizzato |
| **Server DERP personalizzati** | ✅ Sì | ✅ Sì | Entrambi supportano server di relay personalizzati |
| **Estensione Docker** | ✅ Sì | ❌ No | Estensione Docker di Tailscale per la rete dei container |

______

## Confronto dei costi (2026)

### Prezzi di Tailscale

| Piano | Costo mensile | Costo annuale | Dispositivi | Funzionalità |
|------|-------------|-------------|---------|----------|
| **Personal** | $0 | $0 | Fino a 100 | 1 utente, funzionalità di base, supporto della comunità |
| **Personal Pro** | $6 per utente al mese | $48 per utente all'anno | Illimitati | Più utenti, instradamento delle sottoreti, ACL |
| **Team** | $10 per utente al mese | $100 per utente all'anno | Illimitati | Console di amministrazione, log di audit, SSO |
| **Business** | $15 per utente al mese | $150 per utente all'anno | Illimitati | ACL avanzate, gruppi di utenti, supporto prioritario |
| **Enterprise** | Da $18 per utente al mese | Su preventivo | Illimitati | Tailnet Lock, SAML, supporto dedicato, SLA |

**Nota:** Il piano gratuito Personal di Tailscale supporta fino a 100 dispositivi per uso personale, un limite particolarmente generoso per homelab e installazioni di piccole dimensioni.

### Costi di Headscale

Headscale è **gratuito e open source**, ma l'infrastruttura ha un costo:

| Risorsa | Fascia di costo mensile | Note |
|----------|-------------------|-------|
| **VPS piccolo** (1 CPU, 1 GB di RAM) | $5-10 | Adatto a <50 dispositivi |
| **VPS medio** (2 CPU, 4 GB di RAM) | $15-25 | Adatto a 50-200 dispositivi |
| **VPS grande** (4 CPU, 8 GB di RAM) | $40-80 | Adatto da 200 a oltre 1.000 dispositivi |
| **Nome di dominio** | $10-15 all'anno | Per i certificati TLS |
| **Larghezza di banda** | Di solito inclusa | Verifica i limiti del fornitore del VPS |
| **Tempo da dedicare** | Variabile | Configurazione, manutenzione, aggiornamenti |

**Costo totale di proprietà (100 utenti):**
- **Tailscale:** $0 (piano gratuito) o $1.000-1.800 al mese (piani a pagamento)
- **Headscale:** $15-30 al mese + 5-10 ore di configurazione + 2-5 ore di manutenzione al mese

**Punto di pareggio:** Per le organizzazioni con più di 3-5 utenti a pagamento, Headscale diventa conveniente se il costo del tempo di lavoro è inferiore a $50 all'ora.

______

## Confronto delle prestazioni

### Latenza e velocità di trasferimento

Sia Tailscale sia Headscale usano WireGuard per il piano dati, quindi **le prestazioni peer-to-peer sono identiche**:

| Metrica | Tailscale | Headscale |
|--------|-----------|-----------|
| **Latenza aggiuntiva P2P** | <1 ms | <1 ms |
| **Velocità di trasferimento P2P** | Quasi pari a quella senza VPN (~900 Mbps su 1 Gbps) | Quasi pari a quella senza VPN |
| **Velocità di trasferimento del traffico via relay (DERP)** | 50-300 Mbps | 10-200 Mbps (dipende dal tuo server) |
| **Latenza del traffico via relay** | +10-50 ms | +5-100 ms (dipende dalla posizione) |
| **Tempo per stabilire la connessione** | 100-500 ms | 200-800 ms |
| **Propagazione degli aggiornamenti alle regole ACL** | <5 secondi | <30 secondi |

**Differenza principale:** Tailscale gestisce una rete globale di relay DERP con server in tutto il mondo, offrendo prestazioni migliori quando la connessione diretta non riesce. Il relay DERP integrato in Headscale gira sul tuo server. Senza relay distribuiti geograficamente, la latenza potrebbe essere più alta.

### Scalabilità

| Aspetto | Tailscale | Headscale |
|--------|-----------|-----------|
| **Numero massimo di nodi** | Oltre 100.000 (testati) | Circa 5.000 (secondo la comunità) |
| **Numero consigliato di nodi** | Illimitato | <1.000 per un singolo server |
| **Richieste al minuto del piano di controllo** | Altamente ottimizzato | Dipende dalle specifiche del server |
| **Memoria per nodo** | Non applicabile (servizio gestito) | Circa 1-5 MB (lato server) |
| **Database** | PostgreSQL (gestito) | SQLite o PostgreSQL |

______

## Confronto della sicurezza

### Sicurezza dell'infrastruttura

| Aspetto | Tailscale | Headscale | Valutazione |
|--------|-----------|-----------|------------|
| **Fiducia nel server di coordinamento** | Devi fidarti di Tailscale Inc. | Controlli tu il server | Headscale offre più riservatezza |
| **Chiavi di cifratura** | I dispositivi le generano e non le inviano mai a Tailscale | I dispositivi le generano e non le inviano mai al server | ✅ Entrambi eccellenti |
| **Sicurezza del piano dati** | WireGuard (eccellente) | WireGuard (eccellente) | ✅ Entrambi eccellenti |
| **Sicurezza del piano di controllo** | HTTPS + attestazione | HTTPS + equivalente opzionale di Tailnet Lock | ⚠️ Tailscale leggermente più sicuro |
| **Tracciabilità per gli audit** | Registrazione completa degli eventi | Registrazione di base degli eventi | ⚠️ Tailscale superiore |
| **Programma di ricompense per le vulnerabilità** | ✅ Sì | ❌ No | Tailscale ha ricompensato ricercatori di sicurezza |
| **Certificazioni di sicurezza** | SOC 2 Type II | Non applicabile | Tailscale è adatto all'uso aziendale |

### Aspetti relativi alla privacy

| Aspetto della privacy | Tailscale | Headscale |
|----------------|-----------|-----------|
| **Visibilità dei metadati** | Tailscale vede nomi dei dispositivi, indirizzi IP e metadati delle connessioni | Controlli tutti i metadati |
| **Visibilità del traffico** | ❌ Il traffico è cifrato e non visibile | ❌ Il traffico è cifrato e non visibile |
| **Requisiti di conformità** | Si applica la giurisdizione statunitense | Si applica la giurisdizione del tuo server |
| **Residenza dei dati** | Infrastruttura cloud di Tailscale | Il data center che scegli |

**Verdetto:** Entrambe le soluzioni offrono **una cifratura eccellente e un'architettura a conoscenza zero** per il traffico effettivo. Headscale offre una maggiore **tutela della privacy** perché controlli tutti i metadati. Tailscale offre **maggiori garanzie di sicurezza** grazie a certificazioni, audit e programmi di ricompensa per le vulnerabilità.

______

## Confronto della configurazione e della distribuzione

### Configurare Tailscale

**Tempo necessario:** 5-10 minuti

1. **Crea un account** su [tailscale.com](https://tailscale.com/)
2. **Installa il client** su ogni dispositivo (con un comando o scaricando l'app)
3. **Autenticati** tramite OAuth (Google, Microsoft, GitHub, ecc.)
4. **Configura le ACL** (facoltativo, anche in un secondo momento)
5. **Fatto!** La rete è subito operativa

**Esempio di installazione (Linux):**

> **Controlla lo script di installazione prima di eseguirlo.** Scaricalo in un file temporaneo, esaminalo e verifica la distribuzione dell'host e la provenienza del pacchetto. Dopo l'installazione, esegui `tailscale version` e `tailscale status` per verificare il risultato. Se l'installazione non riesce, rimuovi il pacchetto con il gestore di pacchetti della tua distribuzione e ripristina lo stato precedente dei pacchetti dal backup di sistema.

```bash
curl -fsSL https://tailscale.com/install.sh -o /tmp/tailscale-install.sh
less /tmp/tailscale-install.sh
sh /tmp/tailscale-install.sh
sudo tailscale up
```

### Configurare Headscale

**Tempo necessario:** 30-90 minuti (prima configurazione)

1. **Predisponi un server** (VPS con IP pubblico, consigliato almeno 1 GB di RAM)
2. **Configura il DNS** (record A che punta al server)
3. **Installa Headscale** (tramite il gestore di pacchetti o Docker)
4. **Configura Headscale** (config.yaml con URL del server, database, ecc.)
5. **Configura i certificati TLS** (consigliato Let's Encrypt)
6. **Avvia il servizio Headscale**
7. **Crea gli utenti** da riga di comando con `headscale users create alice`
8. **Installa il client Tailscale** su ogni dispositivo
9. **Configura i client** affinché usino il server di coordinamento personalizzato
10. **Registra i nodi** tramite autenticazione web o chiavi di preautenticazione
11. **Configura le ACL** (file policy.json)

**Esempio di installazione di Headscale (Ubuntu):**
```bash
# Installa Headscale
curl -fsSL https://pkgs.headscale.net/headscale_<VERSION>_linux_amd64.deb -o headscale.deb
sudo apt install ./headscale.deb

# Configura Headscale
sudo nano /etc/headscale/config.yaml
# Imposta server_url su https://headscale.example.com

# Avvia il servizio
sudo systemctl enable --now headscale

# Crea un utente
headscale users create myuser

# Sul computer client
sudo tailscale up --login-server=https://headscale.example.com
```

**Configurazione più semplice:** **Tailscale** è decisamente più semplice da configurare la prima volta.

______

## Complessità operativa

### Gestione quotidiana

| Attività | Tailscale | Headscale | Soluzione più semplice |
|------|-----------|-----------|--------|
| **Aggiungere un dispositivo** | Apri il link e autenticati | Genera una chiave di autenticazione o autenticati via web | Tailscale (più semplice) |
| **Aggiornare le ACL** | Modifica dall'interfaccia web, effetto immediato | Modifica il file e ricarica la configurazione | Tailscale (più semplice) |
| **Controllare lo stato della connettività** | Dashboard web | CLI o interfaccia della comunità | Tailscale (più semplice) |
| **Risolvere i problemi** | Log dettagliati nella dashboard | Log del server e del client | Tailscale (più semplice) |
| **Aggiornare il software** | Aggiornamenti automatici | Aggiornamenti manuali del server | Tailscale (più semplice) |
| **Eseguire il backup della configurazione** | Automatico | Manuale (database e configurazione) | Tailscale (più semplice) |
| **Ripristinare il servizio dopo un guasto grave** | Ripristino automatico | Ripristino manuale da backup | Tailscale (più semplice) |

### Carico di manutenzione

**Tailscale (servizio gestito):**
- ✅ Nessuna manutenzione del server
- ✅ Aggiornamenti e patch di sicurezza automatici
- ✅ Ridondanza e failover integrati
- ✅ Supporto professionale disponibile
- ❌ Dipendenza dalla disponibilità del servizio Tailscale

**Headscale (hosting autonomo):**
- ⚠️ Aggiornamenti e patch di sicurezza del sistema operativo del server (mensili)
- ⚠️ Aggiornamenti di Headscale (ogni 1-3 mesi)
- ⚠️ Backup del database (consigliati ogni giorno)
- ⚠️ Rinnovo dei certificati TLS (automatizzato con Let's Encrypt)
- ⚠️ Configurazione del monitoraggio e degli avvisi
- ⚠️ Diagnosi e risoluzione dei problemi quando si presentano
- ✅ Controllo completo dell'infrastruttura
- ✅ Nessuna dipendenza da servizi di terze parti

**Tempo stimato al mese:**
- **Tailscale:** 30 minuti (revisione delle regole, aggiunta di utenti)
- **Headscale:** 2-5 ore (aggiornamenti, monitoraggio, risoluzione dei problemi)

______

## Suggerimenti per caso d'uso

### Quando scegliere Tailscale

✅ **Vuoi configurare la rete il più rapidamente possibile** - 5 minuti dalla creazione dell'account alla rete operativa\
✅ **Hai <100 dispositivi** - Il piano gratuito copre l'uso personale e quello delle piccole imprese\
✅ **Dai priorità alla semplicità d'uso** - Interfaccia web ed esperienza utente tra le migliori della categoria\
✅ **Ti servono funzionalità aziendali** - SSO, log di audit, Tailnet Lock, verifiche dello stato di sicurezza\
✅ **Vuoi risparmiare tempo** - Nessuna manutenzione a tuo carico, aggiornamenti automatici\
✅ **Ti serve una disponibilità garantita** - Tailscale offre uno SLA di disponibilità del 99,99% (Enterprise)\
✅ **Vuoi app ufficiali per dispositivi mobili** - App native per iOS e Android con tutte le funzionalità\
✅ **Ti serve supporto professionale** - I piani a pagamento includono il supporto prioritario\
✅ **La conformità è importante** - Certificazione SOC 2 Type II\
✅ **Operi come impresa commerciale** - Prezzi semplici per utente, senza costi nascosti\

### Quando scegliere Headscale

✅ **Ti serve piena sovranità sui dati** - Tutti i metadati restano sulla tua infrastruttura\
✅ **Hai vincoli di privacy o conformità** - I dati devono rimanere in giurisdizioni specifiche\
✅ **Hai competenze tecniche** - Sai amministrare Linux, usare Docker e risolvere problemi\
✅ **Hai >10 utenti a pagamento** - Il risparmio diventa significativo all'aumentare degli utenti\
✅ **Vuoi imparare** - È un ottimo progetto per capire come funzionano le VPN mesh\
✅ **Preferisci l'open source** - Puoi esaminare il codice, contribuire con correzioni e personalizzarlo\
✅ **Vuoi contenere le spese** - Costi ricorrenti minimi ($5-30 al mese per il server)\
✅ **Hai già un'infrastruttura** - Puoi installarlo su un'infrastruttura Kubernetes o su macchine virtuali esistenti\
✅ **Ti serve un'API gRPC** - Headscale offre gRPC per l'automazione avanzata\
✅ **Gestisci già servizi in autonomia** - Si integra con gli altri servizi che ospiti\

### Approccio ibrido con entrambe le soluzioni

Alcune organizzazioni usano **entrambe le soluzioni**:

1. **Tailscale per la produzione** - Infrastruttura critica con SLA e supporto
2. **Headscale per sviluppo e test** - Ambienti di sviluppo a costi contenuti
3. **Tailscale per gli utenti non tecnici** - Attivazione semplice per il personale
4. **Headscale per i team tecnici** - Tecnici abituati all'hosting autonomo

______

## Scenari di migrazione

### Migrare da Tailscale a Headscale

**Motivazione:** Riduzione dei costi, sovranità sui dati, maggiore controllo

**Procedura:**
1. Installa il server Headscale e verificane il funzionamento
2. Prova Headscale con un gruppo di dispositivi non critici
3. Esporta le ACL da Tailscale e adattale a Headscale
4. Migra gradualmente i dispositivi al server di coordinamento Headscale
5. Aggiorna le configurazioni DNS e le rotte delle sottoreti
6. Disattiva l'abbonamento a Tailscale

**Difficoltà:**
- Non esiste uno strumento di migrazione automatica
- Tutti i dispositivi devono autenticarsi di nuovo
- Alcune funzionalità (Funnel, Serve, Taildrop) non funzioneranno allo stesso modo
- La sintassi delle ACL è compatibile, ma serve verificarne il funzionamento

**Tempo necessario:** 5-20 ore a seconda della complessità

### Migrare da Headscale a Tailscale

**Motivazione:** Minore carico operativo, funzionalità aziendali, supporto migliore

**Procedura:**
1. Crea un account Tailscale e configura le ACL
2. Installa i client Tailscale (sullo stesso dispositivo puoi sostituire il client esistente)
3. Migra i dispositivi eseguendo `tailscale up` senza indicare un server personalizzato
4. Verifica la connettività e i controlli degli accessi
5. Dismetti il server Headscale

**Difficoltà:**
- Tutti i dispositivi devono autenticarsi di nuovo
- Alcuni utenti potrebbero aver bisogno di un account Tailscale (email o SSO)
- Occorre gestire il cambiamento e informare gli utenti

**Tempo necessario:** 2-8 ore a seconda delle dimensioni della rete

______

## Comunità ed ecosistema

### Ecosistema di Tailscale

| Risorsa | Disponibilità |
|----------|--------------|
| **Documentazione ufficiale** | ✅ Completa e ben aggiornata |
| **Forum della comunità** | ✅ Forum attivo con la partecipazione del personale di Tailscale |
| **Server Discord** | ✅ Molto attivo, con personale che risponde prontamente |
| **Segnalazioni su GitHub** | ❌ Codice chiuso (feedback tramite il forum) |
| **Stack Overflow** | ✅ Tag attivo con oltre 2.000 domande |
| **Tutorial su YouTube** | ✅ Contenuti ufficiali e della comunità |
| **Integrazioni** | ✅ Docker, Kubernetes, Terraform, Synology, QNAP, ecc. |

### Ecosistema di Headscale

| Risorsa | Disponibilità |
|----------|--------------|
| **Documentazione ufficiale** | ✅ Buona, curata dalla comunità |
| **Forum della comunità** | ⚠️ La comunità usa GitHub Discussions come forum |
| **Server Discord** | ✅ Server della comunità attivo |
| **Segnalazioni su GitHub** | ✅ Open source, sezione delle segnalazioni attiva (oltre 38.900 stelle) |
| **Stack Overflow** | ⚠️ Comunità più piccola (circa 100 domande) |
| **Tutorial su YouTube** | ⚠️ Contenuti creati dalla comunità |
| **Interfacce web** | ⚠️ Diverse opzioni della comunità (Headscale-UI, Headplane, ouroboros) |
| **Operatore Kubernetes** | ⚠️ Operatore mantenuto dalla comunità |

**Dimensioni delle comunità (2026):**
- **Tailscale:** Oltre 100.000 membri attivi nella comunità, con il sostegno di un'azienda ben finanziata
- **Headscale:** Oltre 10.000 membri attivi nella comunità, progetto open source

______

## Benchmark delle prestazioni in condizioni reali (2026)

Dati ricavati da test della comunità e benchmark pubblicati:

### Test della velocità di trasferimento (peer-to-peer)

| Scenario | Tailscale | Headscale | Riferimento (senza VPN) |
|----------|-----------|-----------|-------------------|
| **LAN gigabit** | 940 Mbps | 940 Mbps | 945 Mbps |
| **WAN (100 Mbps)** | 98 Mbps | 98 Mbps | 100 Mbps |
| **WAN (fibra da 1 Gbps)** | 920 Mbps | 920 Mbps | 950 Mbps |
| **Tra continenti (DERP)** | 180 Mbps | 95 Mbps | Non applicabile |

**Analisi:** Le connessioni peer-to-peer dirette offrono prestazioni identiche. Con le connessioni via relay, Tailscale ottiene risultati migliori grazie alla sua rete DERP globale.

### Test di latenza

| Scenario | Tailscale | Headscale | Riferimento |
|----------|-----------|-----------|----------|
| **Ping su LAN** | 1,2 ms | 1,2 ms | 0,8 ms |
| **WAN regionale (100 miglia)** | 15 ms | 15 ms | 12 ms |
| **Tra punti distanti nello stesso paese** | 48 ms | 48 ms | 45 ms |
| **Tra continenti (connessione diretta)** | 155 ms | 155 ms | 152 ms |
| **Tra continenti (DERP)** | 185 ms | 220 ms | Non applicabile |

**Analisi:** Entrambi aggiungono una latenza minima (circa 1-2 ms) alle connessioni dirette. La latenza del relay DERP di Headscale varia in base alla posizione del server.

### Utilizzo delle risorse

| Metrica | Client Tailscale | Client Headscale | Server Headscale |
|--------|------------------|------------------|------------------|
| **Utilizzo della RAM (a riposo)** | 80-120 MB | 80-120 MB | 50-200 MB (varia con il numero di nodi) |
| **Utilizzo della RAM (in attività)** | 120-200 MB | 120-200 MB | 100-500 MB |
| **Utilizzo della CPU (a riposo)** | <1% | <1% | <1% |
| **Utilizzo della CPU (in attività)** | 5-15% | 5-15% | 3-20% (dipende dal numero di nodi) |
| **Spazio su disco** | 100-500 MB | 100-500 MB | Da 100 MB a 2 GB (database) |

______

## Esempi di configurazione avanzata

### Headscale con Docker Compose

```yaml
version: '3'
services:
  headscale:
    image: headscale/headscale:0.28.0
    container_name: headscale
    restart: unless-stopped
    ports:
      - "127.0.0.1:8080:8080"  # API/web
      - "443:443"              # HTTPS
      - "3478:3478/udp"        # STUN
    volumes:
      - ./config:/etc/headscale
      - ./data:/var/lib/headscale
    command: serve
    environment:
      - TZ=UTC
```

### Esempio di ACL per Headscale

```json
{
  "groups": {
    "group:admin": ["alice@", "bob@"],
    "group:developers": ["charlie@", "diana@"]
  },
  "hosts": {
    "production-db": "100.64.0.10/32",
    "staging-db": "100.64.0.20/32"
  },
  "acls": [
    {
      "action": "accept",
      "src": ["group:admin"],
      "dst": ["*:*"]
    },
    {
      "action": "accept",
      "src": ["group:developers"],
      "dst": ["staging-db:5432", "autogroup:self:*"]
    }
  ]
}
```

### Configurazione del client Tailscale con Headscale

```bash
# Linux
sudo tailscale up \
  --login-server=https://headscale.example.com \
  --accept-routes \
  --advertise-tags=tag:server

# Con una chiave di preautenticazione
headscale preauthkeys create --user engineering --expiration 1h

sudo tailscale up \
  --login-server=https://headscale.example.com \
  --authkey=<YOUR_AUTH_KEY>
```

______

## Risoluzione dei problemi comuni

### Problemi con Tailscale

| Problema | Soluzione |
|---------|----------|
| **Impossibile connettersi al server di coordinamento** | Controlla il firewall e verifica la connettività Internet |
| **La connessione diretta non riesce** | Di solito Tailscale passa automaticamente a DERP. Controlla le impostazioni NAT |
| **Latenza elevata** | Verifica che la connessione sia diretta, senza relay |
| **Chiave scaduta** | Autenticati di nuovo o disattiva la scadenza delle chiavi nella console di amministrazione |
| **Le ACL bloccano il traffico** | Esamina le regole ACL e verifica il funzionamento della configurazione |

### Problemi con Headscale

| Problema | Soluzione |
|---------|----------|
| **I nodi non si registrano** | Verifica che l'URL di Headscale sia raggiungibile e controlla il certificato TLS |
| **La risoluzione DNS non funziona** | Verifica che MagicDNS sia configurato correttamente in config.yaml |
| **Il relay DERP non funziona** | Controlla che la porta STUN (3478/udp) sia aperta e verifica la configurazione di DERP |
| **Nodi offline dopo il riavvio** | Verifica che i client siano configurati per avviarsi all'accensione |
| **Le modifiche alle ACL non hanno effetto** | Ricarica Headscale con `systemctl reload headscale` |
| **Database danneggiato** | Ripristina il database da un backup e valuta PostgreSQL per la produzione |

### Comandi di diagnostica

```bash
# Diagnostica di Tailscale
tailscale status
tailscale netcheck
tailscale ping <hostname>
tailscale debug derp

# Diagnostica di Headscale
headscale nodes list
headscale nodes list-routes
headscale debug routes
journalctl -u headscale -f  # Visualizza i log
```

______

## Buone pratiche di sicurezza

### Per entrambe le soluzioni

1. **Attiva la scadenza delle chiavi** - Richiedi una nuova autenticazione a intervalli regolari
2. **Applica il principio del privilegio minimo** - Concedi tramite le ACL solo gli accessi necessari
3. **Assegna tag ai nodi dell'infrastruttura** - Separa i dispositivi degli utenti dai server
4. **Attiva la MFA** - Richiedi l'autenticazione a più fattori per l'accesso degli utenti
5. **Monitora i log degli accessi** - Esamina regolarmente le modalità di connessione
6. **Mantieni aggiornati i client** - Applica tempestivamente le patch di sicurezza

### Sicurezza specifica per Headscale

1. **Rafforza la sicurezza del sistema operativo del server** - Segui i benchmark CIS e disattiva i servizi superflui
2. **Usa Let's Encrypt** - Automatizza la gestione dei certificati TLS
3. **Configura fail2ban** - Previeni i tentativi di accesso a forza bruta
4. **Esegui backup regolari** - Automatizza i backup del database in una posizione separata
5. **Aggiorna tempestivamente** - Controlla le nuove release di Headscale per le patch di sicurezza
6. **Segmenta la rete** - Isola il server Headscale su una VLAN di gestione
7. **Attiva il firewall** - Esponi solo le porte necessarie (443, 3478/udp)

______

## Sviluppi futuri e piano di lavoro

### Piano di sviluppo di Tailscale (2026)

Secondo le dichiarazioni pubbliche di Tailscale:
- ✅ **Disponibili:** Aperture (gateway per la governance dell'IA), verifiche dello stato di sicurezza migliorate
- 🚧 **In sviluppo:** Rilevamento avanzato delle minacce, supporto per più piattaforme
- 📋 **In programma:** Modalità solo IPv6, osservabilità migliorata, altre integrazioni

### Stato di Headscale (2026)

Secondo le milestone su GitHub e le discussioni della comunità:
- ✅ **Aggiunte recenti:** Autenticazione OIDC, DERP migliorato, supporto ACL più completo
- 🚧 **In sviluppo:** Miglioramenti a Taildrop, migliore integrazione con le interfacce web
- 📋 **Richieste della comunità:** Funzionalità equivalenti a Funnel e Serve, logging avanzato, modalità ad alta disponibilità

**Valutazione della maturità:**
- **Tailscale:** Adatto alla produzione e all'uso aziendale, con almeno 5 anni di sviluppo
- **Headscale:** Pronto per la produzione nei casi d'uso di base, in sviluppo attivo e guidato dalla comunità

______

## Conclusioni

**Tailscale** e **Headscale** offrono entrambi ottime funzionalità per le VPN mesh basate su WireGuard, ma si rivolgono a utenti e casi d'uso diversi.

**Quando scegliere Tailscale:**
- Dai valore alla semplicità e vuoi iniziare a lavorare in pochi minuti
- Fai parte di un piccolo team (<100 dispositivi) che trae vantaggio dal generoso piano gratuito
- Ti servono funzionalità aziendali come SSO, log di audit e supporto professionale
- Preferisci i servizi gestiti all'hosting autonomo
- Le certificazioni di conformità (SOC 2) sono importanti per te

**Quando scegliere Headscale:**
- Ti serve il controllo completo dell'infrastruttura e dei metadati
- Hai competenze tecniche e ti piace gestire i servizi in autonomia
- Ridurre i costi è essenziale (>10 utenti a pagamento = risparmio significativo)
- La sovranità sui dati e la privacy sono prioritarie
- Preferisci soluzioni open source che puoi esaminare e personalizzare

**Raccomandazioni principali per il 2026:**

1. **Startup e PMI:** Inizia con il **piano gratuito di Tailscale**. È la scelta migliore per 0-100 dispositivi.
2. **IT aziendale:** **Tailscale Enterprise**, con SSO e supporto, offre il miglior costo totale di proprietà tenendo conto del tempo del personale.
3. **Utenti attenti alla privacy:** **Headscale** offre il massimo controllo e la massima riservatezza.
4. **Appassionati di homelab con competenze tecniche:** **Headscale** offre un'ottima occasione per imparare.
5. **Organizzazioni che adottano un approccio ibrido:** Usa **Tailscale per la produzione** e **Headscale per sviluppo e test**.

Qualunque sia la tua scelta, usi WireGuard, una tecnologia di riferimento per reti moderne e sicure. La decisione dipende dalle tue priorità tra **comodità e controllo**, **servizio gestito e hosting autonomo**, **costi e funzionalità**.

Per la maggior parte delle organizzazioni nel 2026, **il servizio gestito di Tailscale** offre il miglior equilibrio tra funzionalità, facilità d'uso e costo. Per le organizzazioni con esigenze specifiche di sovranità sui dati, privacy o contenimento dei costi, **Headscale offre una valida alternativa in hosting autonomo**.

______

## Riferimenti e risorse

1. [Sito ufficiale di Tailscale](https://tailscale.com/)
2. [Documentazione di Tailscale](https://tailscale.com/kb/)
3. [Documentazione ufficiale di Headscale](https://headscale.net/)
4. [Repository GitHub di Headscale](https://github.com/juanfont/headscale)
5. [Sito ufficiale di WireGuard](https://www.wireguard.com/)
6. [Blog di Tailscale - Come funziona Tailscale](https://tailscale.com/blog/how-tailscale-works/)
7. [Architettura Zero Trust del NIST](https://csrc.nist.gov/publications/detail/sp/800-207/final)
8. [Documento tecnico di WireGuard](https://www.wireguard.com/papers/wireguard.pdf)
