---
title: "Come funziona il DNS: DNS root, importanza e risoluzione dei problemi"
draft: false
toc: true
date: 2023-07-20
lastmod: 2026-11-13
description: "Scopri il funzionamento del DNS e del DNS root, la loro gerarchia, il processo di risoluzione, la cache e i suggerimenti per la diagnosi."
genre: ["Fondamenti DNS", "DNS root", "Sistema dei nomi di dominio", "Risoluzione DNS", "Gerarchia DNS", "Cache DNS", "Diagnosi DNS", "Record DNS", "Gestione DNS", "Comandi DNS"]
tags: ["DNS", "DNS root", "Sistema dei nomi di dominio", "Risoluzione DNS", "Gerarchia DNS", "Cache DNS", "Record DNS", "Gestione DNS", "Diagnosi DNS", "reti", "infrastruttura Internet", "indirizzi IP", "accesso ai siti web", "query ricorsiva", "server dei nomi autorevoli", "TTL", "meccanismi di cache", "svuotamento della cache DNS", "server DNS root", "instradamento anycast", "ICANN", "collaborazione DNS", "record A", "record AAAA", "record CNAME", "record MX", "record TXT", "record SRV", "record NS", "record PTR", "record SOA", "comandi di diagnosi DNS", "Windows", "macOS", "Linux", "Prompt dei comandi", "Terminale"]
cover: "/img/cover/An_image_depicting_interconnected_computer_ne.webp"
coverAlt: "Immagine di reti informatiche interconnesse con nomi di dominio e indirizzi IP, che rappresenta il funzionamento del DNS e del DNS root."
coverCaption: "Scopri il DNS e padroneggia il sistema dei nomi di dominio"
---

## Come funzionano il DNS e il DNS root

### Introduzione

Il Domain Name System (DNS) è una componente essenziale dell'infrastruttura Internet. Consente di raggiungere i siti web usando nomi di dominio invece di indirizzi IP. Funziona come una rubrica che converte nomi di dominio leggibili dalle persone in indirizzi IP comprensibili dai computer. Alla base del DNS si trova il DNS root, un sistema gerarchico e distribuito importante per la risoluzione dei nomi. In questo articolo vedremo come funzionano il DNS, il DNS root e i record associati ai domini.

{{< youtube id="mpQZVYPuDGU" >}}

## Domain Name System (DNS)

Il **Domain Name System (DNS)** è un sistema di denominazione decentralizzato che associa i nomi di dominio agli indirizzi IP. Consente di raggiungere siti web e altre risorse Internet digitando un nome di dominio nel browser. Il DNS evita di dover memorizzare indirizzi IP complessi.

### Gerarchia DNS

Il DNS usa una struttura gerarchica con più livelli. In cima si trova la zona root, seguita dai domini di primo livello (TLD), dai domini di secondo livello e dai sottodomini. Ogni livello contribuisce a formare il nome di dominio completo. In `www.example.com`, "www" è un sottodominio, "example" è il dominio di secondo livello e "com" è il TLD.

### Processo di risoluzione DNS

Quando inserisci un nome di dominio nel browser, inizia la risoluzione DNS. Il browser invia una query a un resolver DNS, di solito fornito dal provider Internet (ISP). Il resolver segue una serie di passaggi per risolvere il nome di dominio e trovare l'indirizzo IP corrispondente.

1. **Cache DNS locale**: il resolver controlla prima la cache locale per trovare il nome di dominio e l'indirizzo IP richiesti. Se trova i dati, restituisce subito il risultato.

2. **Query ricorsiva**: se i dati non sono nella cache, il resolver avvia una query ricorsiva. Contatta prima i server DNS root, responsabili della zona "." (punto). I server root restituiscono gli indirizzi IP dei server TLD per il dominio richiesto.

3. **Query TLD**: il resolver contatta i server TLD indicati nel passaggio precedente e chiede gli indirizzi IP dei server dei nomi autorevoli per il dominio.

4. **Query al server dei nomi autorevole**: il resolver invia una query ai server autorevoli ricevuti dai server TLD. Questi server contengono i record autorevoli del dominio e rispondono con l'indirizzo IP associato al nome.

5. **Risposta al client**: il resolver riceve l'indirizzo IP dai server autorevoli e lo restituisce al browser. Il browser può quindi connettersi al server web tramite quell'indirizzo.

### Cache DNS

I resolver DNS usano la cache per migliorare le prestazioni e ridurre il carico sui server DNS. Dopo una risposta, il resolver memorizza localmente l'associazione tra nome di dominio e indirizzo IP. Le query successive per lo stesso nome possono ottenere la risposta dalla cache senza consultare di nuovo la gerarchia DNS.

La cache è presente a più livelli, tra cui il resolver locale, quello dell'ISP e dispositivi come router e sistemi operativi. Il valore Time-to-Live (TTL) nella risposta DNS determina per quanto tempo un record resta in cache. Alla scadenza del TTL, il resolver elimina il record e invia una nuova query.

#### Svuotare la cache DNS locale

Svuotare la cache DNS aiuta a risolvere alcuni problemi DNS e fa recuperare al sistema i record più recenti. Ecco come farlo nei diversi sistemi operativi:

##### Windows

Per svuotare la cache DNS in Windows:

1. Premi `Win + R`, digita `cmd` e premi Invio per aprire il Prompt dei comandi.

2. Digita il comando seguente e premi Invio:

```bash
ipconfig /flushdns
```

Il comando svuota la cache del resolver DNS nel sistema Windows.

##### macOS

Per svuotare la cache DNS in macOS:

1. Apri Terminale dalla cartella Applicazioni > Utility oppure cercalo con Spotlight.

2. Digita il comando seguente in Terminale e premi Invio:

```bash
sudo killall -HUP mDNSResponder
```

Il comando riavvia mDNSResponder, il processo che gestisce la risoluzione DNS in macOS.

##### Linux

La procedura per svuotare la cache DNS in Linux varia in base alla distribuzione e al resolver. Ecco due metodi comuni:

1. **Sistemi basati su systemd (ad esempio Ubuntu e Fedora)**:

Apri Terminale ed esegui il comando seguente con privilegi amministrativi:

```bash
sudo systemd-resolve --flush-caches

```

Il comando svuota la cache DNS sui sistemi che usano systemd-resolved come resolver.

2. **Sistemi senza systemd**:

Apri Terminale ed esegui il comando seguente con privilegi amministrativi:

```bash
sudo /etc/init.d/nscd restart

```

Il comando riavvia Name Service Cache Daemon (nscd), responsabile della cache DNS nelle distribuzioni Linux senza systemd.

Questi passaggi sono indicazioni generali. I comandi e i metodi possono variare leggermente in base alla versione del sistema operativo. Svuotare la cache DNS può risolvere alcuni problemi, ma non tutti i problemi di connettività.

## Come funziona il sistema DNS root

Il sistema DNS root è una parte fondamentale dell'infrastruttura DNS. Ecco come funziona:

### 1. Zona root e server root

Il sistema DNS root parte dalla **zona root**, il livello più alto della gerarchia DNS. La zona root contiene informazioni sui server dei nomi autorevoli per tutti i domini di primo livello (TLD), come .com, .org, .net e i domini nazionali come .us e .uk.

Il sistema DNS root comprende 13 server root, identificati dalle lettere da A a M. Sono distribuiti geograficamente nel mondo per garantire ridondanza e affidabilità.

### 2. Instradamento anycast

Per gestire l'enorme traffico DNS, i server root usano l'**instradamento anycast**. Più server condividono lo stesso indirizzo IP pur trovandosi in posizioni diverse. In base alle condizioni di rete, la query viene indirizzata al server più adatto, distribuendo il carico in modo efficiente.

Quando un utente avvia una query DNS, anycast la indirizza al server root disponibile più vicino. L'infrastruttura di rete invia la query lungo il percorso più breve. Anycast distribuisce il carico e aiuta a evitare colli di bottiglia.

### 3. Resolver DNS ricorsivi

Quando un resolver DNS riceve una query per un nome di dominio, avvia una risoluzione ricorsiva e contatta uno dei server root.

Il server root risponde con un riferimento agli indirizzi IP dei server dei nomi TLD responsabili del TLD richiesto. Questi server contengono informazioni sui server autorevoli dei domini all'interno del TLD.

### 4. Riferimenti e server dei nomi autorevoli

Dopo aver ricevuto il riferimento dal server root, il resolver contatta il server dei nomi TLD appropriato.

Il server TLD risponde con un altro riferimento, contenente gli indirizzi IP dei server dei nomi autorevoli per il dominio richiesto.

Il resolver contatta quindi i server autorevoli e chiede l'indirizzo IP associato al nome di dominio.

### 5. Cache e TTL

Durante la risoluzione DNS, la cache migliora le prestazioni e riduce il carico sui server. I resolver memorizzano le associazioni tra nomi di dominio e indirizzi IP.

I record DNS vengono memorizzati per la durata indicata dal valore Time-to-Live (TTL). Il TTL indica per quanto tempo il record resta valido. Alla scadenza, il resolver lo elimina e invia una nuova query per ottenere l'indirizzo IP aggiornato.

### 6. Collaborazione e gestione

Il sistema DNS root è gestito tramite la collaborazione tra Internet Corporation for Assigned Names and Numbers (ICANN) e operatori dei server root.

ICANN supervisiona la gestione e il coordinamento generale del DNS e collabora con gli operatori dei server root. Insieme mantengono il file della zona root, che contiene informazioni sui 13 server DNS root e sui relativi indirizzi IP.

operatori dei server root garantiscono il funzionamento e la disponibilità dei server root, contribuendo alla stabilità e alla resilienza dell'infrastruttura DNS.

Il sistema DNS root è il punto di partenza della risoluzione DNS. Consente di associare i nomi di dominio agli indirizzi IP e permette di raggiungere in modo efficiente siti e risorse Internet.

#### I 13 server DNS root

I 13 server DNS root sono identificati dalle lettere da A a M. Ogni server è ospitato in diverse sedi fisiche per garantire ridondanza e tolleranza ai guasti. Gestiscono le query per la zona root, che comprende TLD come .com, .org, .net e domini nazionali come .us e .uk.

#### ICANN e gestione del DNS root

Internet Corporation for Assigned Names and Numbers (**ICANN**) gestisce e coordina il DNS e l'assegnazione degli indirizzi IP. Collabora con operatori dei server root per garantire la stabilità e la sicurezza del DNS root. Insieme mantengono il file della zona root con le informazioni sui 13 server root e sui relativi indirizzi IP.

______

## Tipi di record DNS e loro scopi

{{< youtube id="HnUDtycXSNE" >}}

I record DNS sono componenti essenziali del Domain Name System (DNS) e forniscono diversi tipi di informazioni associate a un nome di dominio. Ecco alcuni tipi comuni e i relativi scopi:

| Tipo di record | Descrizione | Esempio |
|-------------|-----------------------------------------------------------------------------|-------------------------------------------|
| A | Associa un nome di dominio a un indirizzo IPv4. | `example.com     IN A 192.0.2.1` |
| AAAA | Associa un nome di dominio a un indirizzo IPv6. | `example.com     IN AAAA 2001:db8::1` |
| CNAME | Associa un alias (nome canonico) al nome di dominio effettivo. | `www.example.com IN CNAME example.com` |
| MX | Indica i server di posta che ricevono le e-mail per il dominio. | `example.com     IN MX 10 mail.example.com` |
| TXT | Memorizza testo arbitrario, spesso per SPF, DKIM o verifica del dominio. | `example.com     IN TXT "v=spf1 a mx -all"`|
| NS | Indica i server dei nomi autorevoli per il dominio. | `example.com     IN NS ns1.example.com` |
| SOA | Specifica proprietà globali della zona (record start of authority). | `example.com     IN SOA ns1.example.com` |
| SRV | Definisce la posizione di un servizio specifico offerto dal dominio. | `_service._proto.example.com IN SRV 10 20 5060 target.example.com` |
| PTR | Associa un indirizzo IP a un nome di dominio (ricerca DNS inversa). | `1.2.0.192.in-addr.arpa IN PTR example.com` |

### 1. Record A (Record dell’indirizzo)

Il **record A** associa un nome di dominio a un indirizzo IPv4. È il tipo di record DNS più semplice e diffuso. Quando inserisci un nome nel browser, il record A permette di trovare l'indirizzo IP del server web che ospita il sito.

### 2. Record AAAA (Record dell’indirizzo IPv6)

Il **record AAAA** ha lo stesso scopo del record A, ma associa il dominio a un indirizzo IPv6. Con la transizione a IPv6, i record AAAA sono sempre più importanti per la connettività sulle reti IPv6.

### 3. Record CNAME (Record del nome canonico)

Il **record CNAME** crea un alias o nome canonico per un dominio. Si usa quando vuoi indirizzare un dominio o sottodominio verso un altro dominio o sottodominio. Per esempio, puoi creare un CNAME che indirizza "www" a "mywebsite.com".

### 4. Record MX (Record dello scambio di posta)

Il **record MX** specifica il server di posta che riceve i messaggi per un dominio. Indica dove consegnare le e-mail. Puoi definire più record MX, ciascuno con una priorità che stabilisce l'ordine dei tentativi quando il server principale non è disponibile.

### 5. Record TXT (Record di testo)

Il **record TXT** memorizza informazioni testuali associate a un dominio. È usato spesso per verificare il dominio, pubblicare record SPF (Sender Policy Framework) per l'autenticazione delle e-mail e conservare note o informazioni generali.

### 6. Record SRV (Record del servizio)

Il **record SRV** definisce la posizione di un servizio o una risorsa specifica nel dominio. È usato per servizi VoIP, messaggistica istantanea e altre applicazioni che devono individuare server o servizi specifici.

### 7. Record NS (Record del server dei nomi)

Il **record NS** specifica i server dei nomi autorevoli per un dominio. Questi server contengono i record DNS del dominio. Il resolver consulta gli NS per trovare i server autorevoli necessari.

### 8. Record PTR (Record puntatore)

Il **record PTR** associa un indirizzo IP a un nome di dominio nelle ricerche DNS inverse. È spesso usato per verificare l'identità di un server di posta e contribuire a prevenire lo spam. Le ricerche inverse aiutano a convalidare l'autenticità di un server e-mail.

### 9. Record SOA (Record di inizio autorità)

Il **record SOA** contiene informazioni amministrative sul dominio. Include dettagli come il server dei nomi autorevole principale, l'indirizzo e-mail del responsabile e i parametri temporali dei record DNS.

Questi sono solo alcuni dei tipi di record DNS disponibili. Ognuno ha una funzione specifica e contribuisce alla risoluzione efficiente e accurata dei nomi di dominio.

______

## Comandi di diagnosi DNS per diversi sistemi operativi

Quando si verificano problemi DNS, i comandi diagnostici aiutano a individuarne la causa. Ecco alcuni comandi comuni per i diversi sistemi operativi:

### Windows

#### 1. `ipconfig /flushdns`

Questo comando svuota la cache DNS in Windows e può risolvere problemi causati da record obsoleti o errati. Apri il Prompt dei comandi e avvia il comando.

#### 2. `ipconfig /all`

Il comando `ipconfig /all` mostra informazioni dettagliate sulle interfacce di rete Windows, compresi i server DNS configurati. Puoi verificare che siano in uso i server corretti.

### macOS

#### 1. `sudo killall -HUP mDNSResponder`

Questo comando riavvia mDNSResponder in macOS, il processo che gestisce la risoluzione DNS. Può aggiornare le impostazioni DNS e aiutare a risolvere i problemi. Apri Terminale ed esegui il comando con privilegi amministrativi.

#### 2. `nslookup`

Il comando `nslookup` consente di interrogare i record DNS, testare la risoluzione e verificare la connettività ai server DNS. Apri Terminale ed esegui `nslookup` seguito dal nome di dominio o dall'indirizzo IP da esaminare.

### Linux

#### 1. `systemd-resolve --flush-caches`

Nei sistemi Linux che usano systemd come resolver DNS, `systemd-resolve --flush-caches` svuota la cache DNS. Può risolvere problemi causati da voci obsolete. Apri Terminale ed esegui il comando con privilegi amministrativi.

#### 2. `dig`

Il comando `dig` è uno strumento versatile di diagnosi DNS disponibile in Linux. Fornisce informazioni dettagliate su query, risposte e configurazione dei server. Usa `dig` per interrogare record specifici, testare la risoluzione e analizzare i problemi DNS. Apri Terminale ed esegui `dig` seguito dal dominio o dall'indirizzo IP da esaminare.

Questi comandi sono utili per diagnosticare e risolvere problemi DNS. Permettono di controllare configurazioni DNS, impostazioni dei server e problemi di connettività.

I comandi e le opzioni disponibili possono variare in base alla versione del sistema operativo e alla distribuzione. Consulta la documentazione della tua versione per informazioni dettagliate sull'uso.
______


## Conclusione

Il Domain Name System (DNS) e il DNS root svolgono un ruolo centrale nel funzionamento di Internet. Il DNS consente di raggiungere siti web tramite nomi di dominio intuitivi, mentre il DNS root costituisce la base dell'intera gerarchia DNS. Capire come funzionano aiuta a usare il web e a comprendere l'infrastruttura che sostiene i servizi online.

______

## Riferimenti

- [DNS su Wikipedia](https://en.wikipedia.org/wiki/Domain_Name_System)
- [Come funziona il DNS secondo Cloudflare](https://www.cloudflare.com/learning/dns/what-is-dns/)
- [Sito ufficiale ICANN](https://www.icann.org/)
- [operatori dei server root](https://www.root-servers.org/)
