---
title: "Pianificare e testare la segmentazione VLAN di un homelab"
date: 2026-10-10
lastmod: 2026-11-12
toc: true
draft: false
description: "Crea un piano VLAN per separare dispositivi fidati, server, IoT e ospiti nel tuo homelab. Definisci il traffico consentito, configura la rete per fasi e verifica l'isolamento."
genre: ["Homelab", "Sicurezza di rete", "Networking"]
tags: ["VLAN homelab", "segmentazione VLAN", "rete IoT", "rete ospiti", "firewall homelab", "routing tra VLAN", "802.1Q", "isolamento di rete", "test VLAN", "VLAN pfSense", "porta di accesso", "porta trunk", "regole firewall", "sicurezza homelab", "piano di rete", "subnet", "DHCP", "DNS", "switch gestito", "SSID wireless"]
cover: "/img/cover/homelab-vlan-segmentation-plan.webp"
coverAlt: "Un router e uno switch homelab separano laptop, server, dispositivi IoT e ospiti in zone di rete protette."
coverCaption: "Pianifica i confini VLAN, quindi verifica ogni percorso consentito e negato."
---

Un homelab spesso colloca laptop, server, telecamere e dispositivi degli ospiti sulla stessa rete. **La segmentazione VLAN** colloca questi gruppi su reti separate. Un router, firewall o switch di livello 3 instrada il traffico tra le reti. Le regole del firewall o le liste di controllo degli accessi dello switch governano i flussi instradati. Questa guida ti aiuta a scrivere il piano, applicare una modifica alla volta e verificare il risultato.

## Punti chiave

- **Raggruppa in base al livello di fiducia:** colloca dispositivi di gestione, server, IoT e ospiti su reti separate quando hanno esigenze di accesso diverse.
- **Documenta i percorsi consentiti:** registra origine, destinazione, servizio e motivo di ogni connessione tra reti.
- **Configura entrambi i livelli:** le impostazioni VLAN di switch e access point collocano i dispositivi. Le regole firewall o le liste di controllo accessi dello switch controllano il traffico instradato.
- **Verifica entrambi gli esiti:** controlla una connessione consentita e una negata da ogni rete pertinente.

## Prima di iniziare

Ti serve un router o firewall con interfacce VLAN, oppure uno switch di livello 3 che supporti il routing VLAN e le liste di controllo accessi. Uno switch gestito trasporta le VLAN cablate. Se separi i client wireless, ti serve anche un access point con reti wireless associate alle VLAN. Mantieni un dispositivo sulla rete di gestione attuale mentre modifichi la configurazione. Salva prima le impostazioni di router, switch e access point. I passaggi seguenti usano un **piano illustrativo**, quindi adatta indirizzi e porte alla tua apparecchiatura.

Un'**interfaccia VLAN** è la connessione del gateway a una VLAN. Il gateway può essere un router, un firewall o uno switch di livello 3. Un **ambito DHCP** è l'intervallo di indirizzi che un servizio DHCP offre ai dispositivi di quella rete. Un **relay DHCP** inoltra richieste di indirizzo da una VLAN a un server DHCP su un'altra rete. Usa un relay quando il gateway non assegna gli indirizzi per quella VLAN e il server DHCP si trova altrove. La [guida al relay DHCP di Juniper](https://www.juniper.net/documentation/us/en/software/junos/dhcp/topics/topic-map/dhcp-relay-agent-security-devices.html) descrive questo percorso. Un **SSID** wireless è il nome della rete a cui si collegano i client. Se la tua apparecchiatura non dispone di uno switch gestito o di un access point compatibile con VLAN, inizia dalla rete ospiti integrata e verifica l'isolamento prima di acquistare o cambiare hardware.

Se ti servono prima i termini di base, leggi [subnet e VLAN](/articles/networking-basics-what-are-subnets-and-vlans/). La [guida alla segmentazione di rete](/articles/how-to-perform-network-segmentation-for-improved-security/) del sito spiega il concetto di sicurezza più ampio. CISA descrive reti domestiche separate per ospiti e dispositivi Internet of Things nella propria [guida alla sicurezza per il lavoro mobile federale](https://www.cisa.gov/sites/default/files/2024-08/Federal-Mobile-Workplace-Security_508_2024-08-14.pdf).

> **Avviso:** una modifica VLAN sulla porta che trasporta la tua connessione di gestione potrebbe bloccarti l'accesso. Mantieni l'accesso fisico e una procedura di ripristino nota finché tutte le reti non superano i test.

Prima di spostare un cavo, esporta la configurazione di ogni dispositivo e annota l'IP di gestione attuale, la porta dello switch, l'impostazione VLAN e l'accesso amministrativo. Lascia una porta di gestione funzionante e un laptop sulla rete originale. Se una modifica interrompe l'accesso, ricollega il laptop a quella porta, ripristina l'impostazione o configurazione salvata e verifica che il vecchio gateway risponda prima di riprovare. Se non puoi raggiungere il percorso di gestione dello switch, usa la procedura documentata per la console o il ripristino locale. Non ripristinare il dispositivo finché non sai cosa cancella il ripristino.

## Inventaria dispositivi e flussi

Elenca ogni dispositivo, il suo indirizzo attuale, il proprietario e i servizi necessari. Associa a ogni dispositivo un motivo per accedere a un'altra rete. Per esempio, un laptop potrebbe amministrare un server, mentre una telecamera potrebbe raggiungere solo un registratore e un server DNS. Il telefono di un ospite ha bisogno di Internet, ma non dell'accesso ai server.

| Gruppo di dispositivi | Dispositivi di esempio | Accesso richiesto |
|---|---|---|
| **Gestione** | Laptop amministratore, gestione di switch e access point | Router, switch, access point, amministrazione server |
| **Server** | Hypervisor, NAS, destinazione dei backup | Aggiornamenti, DNS, traffico applicativo approvato |
| **IoT** | Telecamere, prese intelligenti, dispositivi multimediali | DNS, servizio orario, controller o registratore specifico |
| **Ospiti** | Telefoni e laptop dei visitatori | Internet, DNS, nessun accesso alle subnet private |

Annota le eccezioni prima di aggiungere regole. Le funzioni di rilevamento locale, come la trasmissione a uno schermo, spesso dipendono da traffico multicast che per impostazione predefinita non attraversa un confine instradato. Non consentire tutto il traffico tra VLAN per risolvere un problema di rilevamento. Identifica il protocollo e aggiungi l'eccezione più limitata supportata.

## Assegna VLAN e indirizzi

Assegna a ogni gruppo un ID VLAN e una subnet IP separata. Questo **piano illustrativo** usa indirizzi riservati alla documentazione e presuppone che il router fornisca DHCP e DNS. Non copiare la tabella in una rete attiva senza verificare eventuali conflitti di indirizzo.

| Rete | ID VLAN | Subnet | Gateway di esempio |
|---|---:|---|---|
| **Gestione** | 10 | `192.0.2.0/27` | `192.0.2.1` |
| **Server** | 20 | `198.51.100.0/27` | `198.51.100.1` |
| **IoT** | 30 | `203.0.113.0/27` | `203.0.113.1` |
| **Ospiti** | 40 | `192.0.2.32/27` | `192.0.2.33` |

Questi intervalli riservati alla documentazione illustrano solo la disposizione, come definito dalla [RFC 5737](https://www.rfc-editor.org/info/rfc5737). Usa indirizzi privati della [RFC 1918](https://www.rfc-editor.org/info/rfc1918) per il tuo laboratorio, con una subnet non sovrapposta per ogni VLAN. Registra nel piano ciascun gateway reale, pool DHCP, indirizzo DNS e prenotazione dispositivo.

Le **porte di accesso** trasportano la rete di un singolo dispositivo senza tag VLAN. Le **porte trunk** trasportano VLAN selezionate con tag tra router, switch e access point. Imposta lo stesso ID VLAN e la stessa configurazione nativa o senza tag a entrambe le estremità. La [guida VLAN per switch di Netgate](https://docs.netgate.com/pfsense/en/latest/recipes/switch-vlan-configuration.html) spiega porte trunk con tag, porte di accesso senza tag e ID VLAN delle porte. Evita di usare la VLAN 1 predefinita per la gestione quando l'hardware consente una VLAN separata, come descritto nella [guida alla sicurezza VLAN di Netgate](https://docs.netgate.com/pfsense/en/latest/vlan/security.html).

Il traffico **nativo** o **senza tag** su un trunk non ha un tag VLAN. Le due estremità devono assegnarlo alla stessa VLAN, altrimenti un dispositivo potrebbe finire sulla rete sbagliata. Consenti solo le VLAN necessarie al collegamento. Disabilita le porte dello switch inutilizzate oppure assegnale a una rete limitata. Netgate sconsiglia inoltre di considerare una VLAN un confine di sicurezza completo quando un attaccante controlla una porta dello switch. Proteggi le porte fisiche e le credenziali dei dispositivi oltre al traffico instradato.

## Crea una matrice del traffico

Una VLAN da sola separa i domini di broadcast. Il **routing tra VLAN** sul router o sullo switch di livello 3 richiede comunque regole di accesso. Decidi quale dispositivo instrada il traffico tra VLAN. Se uno switch di livello 3 instrada localmente, il traffico tra le sue VLAN potrebbe non raggiungere mai il firewall del router. Applica ACL equivalenti sullo switch oppure instrada attraverso il firewall, poi verifica nel punto in cui avviene l'applicazione delle regole. Controlla la direzione dell'ACL dello switch e se mantiene lo stato delle connessioni. Molte ACL degli switch valutano i pacchetti separatamente in ciascuna direzione, quindi una connessione consentita potrebbe aver bisogno di una regola limitata per il traffico di risposta. La [guida ACL di Cisco](https://www.cisco.com/c/en/us/td/docs/switches/lan/c9000/security/acls/acls-configuration-guide/access-control-lists.html) descrive la direzione dell'interfaccia e l'ordine delle corrispondenze dei pacchetti. Usa l'inventario dispositivi per registrare le connessioni che vuoi consentire. Le righe seguenti sono esempi, non un insieme universale di regole.

| Origine | Destinazione | Servizio | Decisione |
|---|---|---|---|
| **Gestione** | Interfaccia di amministrazione del server | TCP 443 | Consenti ai dispositivi di amministrazione approvati |
| **Gestione** | Interfacce di amministrazione di router, switch e access point | Le relative porte di gestione documentate | Consenti ai dispositivi di amministrazione approvati |
| **IoT** | Registratore telecamere | Porta documentata del registratore | Consenti solo se necessario |
| **IoT** | DNS e servizio orario approvati | DNS e NTP | Consenti solo verso i servizi scelti |
| **IoT** | Subnet di gestione | Qualsiasi | Nega |
| **Ospiti** | Subnet private | Qualsiasi | Nega |
| **Ospiti** | DNS e Internet | DNS, traffico web | Consenti tramite resolver e gateway approvati |

Includi nel piano anche i servizi del router. Una regola che blocca l'accesso IoT alle altre VLAN potrebbe lasciare raggiungibile l'interfaccia amministrativa del router. Limita i servizi di gestione alla rete di gestione. Inizia solo con le regole di autorizzazione necessarie e una negazione predefinita per il resto del traffico instradato. Controlla le regole di autorizzazione ampie esistenti prima di presumere che il comportamento predefinito neghi qualcosa. Le [best practice firewall di Netgate](https://docs.netgate.com/pfsense/en/latest/firewall/best-practices.html) osservano che una LAN pfSense predefinita contiene una regola di autorizzazione. Se usi pfSense, la [metodologia delle regole](https://docs.netgate.com/pfsense/en/latest/firewall/rule-methodology.html) spiega che le regole di interfaccia filtrano il traffico in ingresso da quell'interfaccia e che le connessioni autorizzate creano uno stato per il traffico di risposta.

La tabella di esempio riguarda IPv4. Se la rete usa IPv6, assegna un prefisso e una policy IPv6 a ogni VLAN, controlla gli annunci del router e testa anche i percorsi IPv6 consentiti e negati. Un blocco IPv4 non dimostra l'isolamento IPv6. Se non intendi instradare IPv6, controlla le impostazioni IPv6 del router e gli indirizzi client invece di presumere che IPv6 sia assente. Netgate documenta il [comportamento firewall IPv6](https://docs.netgate.com/pfsense/en/latest/config/advanced-networking.html) e gli [annunci del router](https://docs.netgate.com/pfsense/en/latest/services/dhcp/ipv6-ra.html).

## Configura una rete alla volta

1. Scegli il gateway della VLAN. Se la instrada il router o firewall, crea lì un'interfaccia VLAN e assegnale l'indirizzo gateway. Se la instrada uno switch di livello 3, crea l'interfaccia VLAN sullo switch. Configura un ambito DHCP sul gateway oppure un relay DHCP verso il server DHCP esistente. Verifica che un resolver DNS approvato sia raggiungibile. La [guida alla configurazione VLAN di Netgate](https://docs.netgate.com/pfsense/en/latest/vlan/configuration.html) elenca i passaggi di interfaccia e servizio per un gateway pfSense.
2. Se il router è il gateway VLAN, aggiungi quella VLAN al trunk tra router e switch. Se il gateway è lo switch di livello 3, assegna allo switch l'indirizzo gateway della VLAN e instrada verso router o firewall tramite una rete di transito separata o un uplink instradato. Imposta sullo switch una route predefinita verso il router upstream. Aggiungi sul router, tramite lo switch, una route di ritorno per ogni VLAN con gateway sullo switch. Controlla la policy firewall del router e il NAT in uscita per quelle subnet sorgente se devono raggiungere Internet. Non configurare lo stesso indirizzo gateway o ambito DHCP su entrambi i dispositivi. La [guida al routing tra VLAN di Cisco](https://www.cisco.com/c/en/us/support/docs/lan-switching/inter-vlan-routing/41260-189.html) mostra gateway VLAN posseduti dallo switch. Netgate documenta le [route di ritorno](https://docs.netgate.com/pfsense/en/latest/routing/static.html) e il [NAT in uscita](https://docs.netgate.com/pfsense/en/latest/nat/outbound.html) per reti dietro un router interno. Aggiungi la VLAN al trunk pertinente tra switch e access point se i client wireless ne hanno bisogno.
3. Assegna alla VLAN una porta di accesso di test o un SSID wireless. Collega a quella porta o SSID un dispositivo di test non critico.
4. Aggiungi le regole firewall o ACL dello switch previste sul dispositivo che instrada la VLAN. Verifica che il resto del traffico instradato sia negato. Controlla direzione ACL e traffico di risposta se lo switch non mantiene lo stato. Testa l'accesso a ogni gateway e interfaccia di gestione, a ogni subnet locale e a IPv6 se presente. Consenti solo i percorsi della matrice. Limita l'accesso di gestione alla rete di gestione. Controlla l'ordine delle regole e rimuovi o restringi le regole di autorizzazione ampie esistenti solo dopo aver verificato che il percorso di gestione di prova funziona.
5. Verifica che il dispositivo di test riceva un indirizzo, un gateway e un server DNS dalla subnet prevista. Quindi esegui i controlli di connessione qui sotto prima di spostare altri dispositivi.

Non spostare l'ultimo dispositivo di gestione finché il percorso sostitutivo non funziona. Salva la configurazione funzionante dopo che ogni rete supera i test. Se DHCP, DNS o l'accesso di gestione non funziona, ricollega il dispositivo di test alla porta o SSID originale, ripristina l'ultima modifica di switch o router dalla configurazione salvata e verifica di nuovo la rete originale prima di procedere.

## Verifica isolamento e accesso

Usa un servizio che controlli e sai essere in ascolto sulla destinazione. Da un dispositivo Windows di test, sostituisci l'indirizzo e la porta di esempio con un server reale ed esegui:

```powershell
Test-NetConnection -ComputerName 198.51.100.10 -Port 443
```

Il campo **`TcpTestSucceeded`** indica se una connessione TCP è stata completata. La [documentazione Microsoft di Test-NetConnection](https://learn.microsoft.com/powershell/module/nettcpip/test-netconnection) descrive i parametri `-ComputerName` e `-Port`. Una connessione non riuscita da sola non dimostra che la regola firewall abbia funzionato. Il servizio potrebbe essere arrestato oppure il firewall dell'host potrebbe rifiutare il traffico. Controlla il servizio di destinazione e il log del firewall di rete prima di concludere.

Esegui il test da un dispositivo realmente connesso a ciascuna VLAN di origine. Prima di ogni prova, annota indirizzo sorgente, gateway e server DNS. Verifica una connessione consentita al servizio previsto, una connessione negata a un servizio interno fuori dalla matrice, una ricerca DNS tramite il resolver previsto e l'accesso Internet dove pianificato. Per una VLAN il cui gateway si trova sullo switch, controlla la route predefinita dello switch, la route di ritorno del router e il percorso di ritorno dalla destinazione se una connessione consentita non riesce. Ripeti i test consentiti e negati usando indirizzi IPv6 se IPv6 è attivo. In pfSense, **Stato > Registri di sistema > Firewall** mostra le azioni consentite o bloccate registrate. La [guida ai log firewall di Netgate](https://docs.netgate.com/pfsense/en/latest/monitoring/logs/firewall.html) descrive questa schermata. Confronta origine, destinazione, porta e regola del log con il test. Se il test riesce inaspettatamente, controlla le regole di autorizzazione ampie e le voci di stato esistenti. Avvia una nuova connessione dopo aver modificato le regole, poiché una connessione già stabilita potrebbe continuare a funzionare tramite il suo stato esistente.

Per una verifica DNS su Windows, esegui `nslookup example.com` e confronta il server mostrato con il resolver previsto. Poi prova una ricerca da un client ospite o IoT in cui il DNS è limitato. Una ricerca riuscita da sola non dimostra che il client abbia usato il resolver scelto, quindi controlla il server indicato e un log del firewall o del resolver. Verifica separatamente, come caso da negare, l'accesso diretto all'indirizzo di gestione del router da un dispositivo IoT o ospite.

I dispositivi sulla **stessa VLAN** potrebbero scambiare traffico senza attraversare il firewall del router. Verifica separatamente l'isolamento client locale se l'access point lo offre e usa firewall host sui server. I test firewall tra VLAN non dimostrano l'isolamento all'interno della stessa VLAN.

> **Risultato previsto:** ogni dispositivo riceve un indirizzo dalla subnet pianificata. I servizi consentiti funzionano. I tentativi negati corrispondono a un blocco firewall o a un controllo equivalente documentato.

## Risoluzione dei problemi

- **Nessun indirizzo:** controlla la VLAN della porta di accesso o dell'SSID, i tag trunk, l'ambito DHCP e l'interfaccia gateway.
- **L'indirizzo funziona, DNS no:** controlla l'indirizzo del resolver, il binding del servizio del router e la regola firewall per il traffico DNS.
- **Un dispositivo raggiunge inaspettatamente un'altra VLAN:** controlla le regole del router, le regole di autorizzazione ampie e se i dispositivi condividono ancora una rete senza tag.
- **Nessun log firewall per traffico instradato:** verifica se uno switch di livello 3 o un gateway alternativo ha instradato la connessione prima che raggiungesse il firewall.
- **Una VLAN con gateway sullo switch raggiunge le reti locali ma non Internet:** controlla la route predefinita dello switch, le route di ritorno del router, la policy firewall e il NAT in uscita per la subnet VLAN.
- **IPv4 è bloccato ma la connessione funziona:** controlla indirizzi IPv6, annunci del router, regole IPv6 e voci di stato esistenti.
- **Un test negato va in timeout senza un log firewall:** conferma che il servizio di destinazione sia in ascolto. Poi controlla routing e impostazioni di logging. La [guida alla risoluzione dei problemi firewall di Netgate](https://docs.netgate.com/pfsense/en/latest/troubleshooting/firewall.html) descrive i controlli di log e stato.
- **Trasmissione o rilevamento smette di funzionare:** identifica il protocollo di rilevamento e il percorso verso il controller prima di aggiungere un'eccezione limitata.

## Passaggi successivi

Conserva l'inventario dei dispositivi e la matrice del traffico insieme al diagramma di rete. Rivedi le regole quando aggiungi un server o un dispositivo IoT. Ripeti un test consentito e uno negato dopo ogni modifica di rete pertinente. Per i principi di progettazione più ampi, torna alla [segmentazione di rete](/articles/how-to-perform-network-segmentation-for-improved-security/).
