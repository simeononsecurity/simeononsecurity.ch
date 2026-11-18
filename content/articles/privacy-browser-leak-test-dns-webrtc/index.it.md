---
title: "Verifica le perdite DNS e WebRTC del browser con una VPN"
date: 2026-10-11
lastmod: 2026-11-12
toc: true
draft: false
description: "Controlla l'IP pubblico, il resolver DNS e gli indirizzi WebRTC del browser prima e dopo aver collegato una VPN. Interpreta i risultati e individua i problemi di instradamento."
genre: ["Privacy", "Browser", "Reti"]
tags: ["test perdita DNS", "test perdita WebRTC", "test perdita VPN", "test privacy browser", "perdita indirizzo IP", "DNS su HTTPS", "DNS sicuro", "DNS Firefox", "DNS sicuro Chrome", "candidati WebRTC", "split tunneling VPN", "perdita IPv6", "test resolver", "privacy browser", "privacy di rete", "risoluzione problemi VPN", "resolver DNS", "candidati ICE", "indirizzo IP privato", "mDNS"]
cover: "/img/cover/privacy-browser-leak-test-dns-webrtc.webp"
coverAlt: "Finestra del browser con tre pannelli per IP pubblico, DNS e connessioni peer, più un tunnel continuo e un percorso alternativo tratteggiato verso server remoti."
coverCaption: "Confronta ogni percorso di rete prima e dopo aver collegato la VPN."
---

L'icona di connessione di una rete privata virtuale (VPN) non dimostra che ogni richiesta del browser segua lo stesso percorso. Verifica separatamente il tuo **IP pubblico**, il **resolver del Domain Name System (DNS)** e gli **indirizzi WebRTC**. Ogni risultato risponde a una domanda diversa. Questa guida propone una verifica ripetibile e un metodo per indagare un risultato inatteso.

<!--more-->

## Punti chiave

- **Confronta due condizioni:** Registra gli stessi test prima e dopo aver collegato la VPN.
- **Leggi ogni risultato a sé:** Un IP pubblico diverso non indica dove siano finite le richieste DNS.
- **Controlla i candidati WebRTC:** Cerca un indirizzo pubblico fuori dal percorso previsto. Un indirizzo privato ha un significato diverso.
- **Modifica un'impostazione per volta:** Ripeti il test dopo ogni modifica a VPN, browser o DNS.

## Prima di iniziare

Usa il browser e la connessione di rete che vuoi proteggere. Stabilisci se la VPN deve coprire l'intero dispositivo o solo alcune app. Se la VPN usa lo split tunneling, annota se il browser di test passa dal tunnel. Tieni a disposizione la policy DNS del client VPN per il confronto.

Lo **split tunneling** invia alcune app tramite la VPN e lascia che altre usino la rete normale.

La procedura usa le pagine [IP di BrowserLeaks](https://browserleaks.com/ip), [DNS](https://browserleaks.com/dns) e [WebRTC](https://browserleaks.com/webrtc). Il servizio vede l'indirizzo di connessione quando lo visiti. Secondo la descrizione del test, la prova DNS chiede al browser di risolvere 50 nomi casuali. Non eseguire test esterni su una rete gestita o soggetta a restrizioni senza autorizzazione. Non inserire credenziali, nomi host interni o registri privati di navigazione in un sito di test.

> **Avviso:** Non pubblicare gli IP esatti in screenshot pubblici o post di assistenza. Registra se gli indirizzi corrispondono al percorso previsto del provider Internet o della VPN. Condividi i valori effettivi solo tramite un canale di assistenza approvato.

## Cosa mostra ogni test

| Controllo | Cosa confrontare | Cosa non dimostra il risultato |
|---|---|---|
| **IP pubblico** | Indirizzo visto da un normale sito web | Quale resolver ha gestito il DNS |
| **Resolver DNS** | Server osservati durante nuove ricerche di nomi | Dove ogni app invia il DNS |
| **WebRTC** | Candidati di connessione locali e pubblici | Quale candidato userà una chiamata successiva |

La pagina IP pubblico riporta l'indirizzo usato per la richiesta web. La pagina DNS avvia nuove ricerche e indica i resolver che le gestiscono. WebRTC, abbreviazione di Web Real-Time Communication, permette alle app del browser di stabilire connessioni peer. La pagina WebRTC controlla gli indirizzi esposti durante queste connessioni. Un **candidato ICE** è un possibile indirizzo di rete per una connessione peer. Un **exit VPN** è l'indirizzo pubblico usato dal traffico quando esce dalla VPN. [RFC 8828](https://datatracker.ietf.org/doc/html/rfc8828) spiega perché i candidati di connessione WebRTC a volte includono indirizzi diversi da quello visto da una normale richiesta web, soprattutto con split tunnel o proxy.

Un server DNS del provider VPN, un resolver distinto selezionato nella VPN oppure un resolver cifrato scelto dal browser producono nomi diversi nel test. Il solo nome del resolver non prova una perdita. Confrontalo con la policy prevista.

## Registra una condizione iniziale

Disconnetti la VPN solo se la tua situazione permette una verifica senza tunnel. Apri le tre pagine di test in un normale profilo del browser. Esegui il test DNS e attendi il risultato. Registra questi dati senza pubblicare gli indirizzi esatti:

| Campo | Nota iniziale |
|---|---|
| **Browser e versione** | Nome, versione ed estensioni privacy pertinenti |
| **Rete** | Wi-Fi domestico, hotspot mobile o un'altra rete approvata |
| **IPv4 e IPv6 pubblici** | Se ciascun indirizzo appartiene alla connessione normale |
| **Risultato DNS** | Nomi o operatori dei resolver mostrati |
| **Risultato WebRTC** | Candidati pubblici, privati o `.local` mostrati |

Se non puoi disconnettere la VPN, parti dal percorso VPN previsto e indica la condizione senza tunnel come non disponibile. Non dedurre l'IP normale del provider da un'etichetta geografica o da una mappa. I database di localizzazione a volte non corrispondono all'effettivo operatore di rete.

## Ripeti il test con la VPN collegata

Collega la VPN e conferma che il client segnali un tunnel attivo. Ricarica ogni pagina di test nello **stesso profilo del browser**. Esegui di nuovo il test DNS per creare nuove richieste. Registra anche IPv4 e IPv6 quando il servizio li mostra.

Confronta i risultati in questo ordine:

1. **IP pubblico:** La richiesta web dovrebbe mostrare un indirizzo coerente con l'exit VPN o con il percorso configurato intenzionalmente. Se il browser dovrebbe essere nel tunnel ma compare l'IP normale del provider, c'è un problema di instradamento.
2. **DNS:** Confronta ogni resolver con le impostazioni DNS della VPN e del browser. Verifica un resolver del provider Internet fuori dal tunnel previsto. Un resolver di terze parti è atteso se lo hai selezionato nel browser.
3. **WebRTC:** Confronta il candidato WebRTC pubblico con l'exit VPN e con l'IP pubblico iniziale. Se tutto il traffico del browser dovrebbe passare dalla VPN, la comparsa dell'IP normale del provider solo in WebRTC è un motivo di verifica.
4. **Indirizzi privati:** Un indirizzo negli [intervalli privati RFC 1918](https://www.rfc-editor.org/rfc/rfc1918) o un candidato `.local` è diverso da un IP pubblico del provider. Registra la voce locale e valuta se il sito deve conoscerla.

Lo [standard WebRTC per la gestione degli IP](https://datatracker.ietf.org/doc/html/rfc8828) descrive come un'app rileva altri indirizzi pubblici o privati tramite la scoperta dei candidati ICE. Il progetto dei [candidati host mDNS di Chromium](https://groups.google.com/a/chromium.org/g/blink-dev/c/z5hSy6Rf_aE/m/aGND030cAgAJ) sostituisce alcuni indirizzi privati con nomi `.local`. Un risultato WebRTC vuoto è **inconcludente** se JavaScript, l'API o il server di test non hanno funzionato. Un risultato vuoto non dimostra una protezione completa.

> **Risultato atteso:** La normale richiesta web del browser e i candidati WebRTC pubblici seguono il percorso scelto. I risultati DNS corrispondono alla policy del resolver VPN o del browser che hai registrato.

## Indaga una differenza DNS

Per prima cosa, controlla se il browser sceglie un resolver proprio. Le impostazioni [DNS over HTTPS di Firefox](https://support.mozilla.org/en-US/kb/dns-over-https) mostrano lo stato attivo e il livello di protezione. La protezione predefinita in alcune condizioni torna al resolver di sistema e rispetta i segnali della rete. I livelli Aumentata e Personalizzata usano un provider scelto con comportamento di fallback. Il livello Massima avvisa se la risoluzione sicura fallisce. Controlla lo stato e l'elenco delle eccezioni, non solo l'interruttore.

La [guida DNS sicuro di Chrome](https://support.google.com/chrome/answer/10468685?co=GENIE.Platform%3DDesktop&hl=en) descrive la modalità automatica e un provider personalizzato. La modalità automatica ripiega su una richiesta non cifrata se la risoluzione sicura non riesce. Un provider personalizzato non passa per impostazione predefinita alla modalità non cifrata. I dispositivi gestiti e i controlli parentali limitano questa impostazione. Controlla l'interfaccia attuale del browser prima di modificare una policy gestita.

Se la causa non è il resolver del browser, confronta l'impostazione DNS del client VPN, l'elenco delle app incluse nello split tunnel, il resolver del sistema operativo e il percorso IPv6. Modifica una voce e ripeti il test DNS. Il test DNS del browser misura il percorso di ricerca di quel browser. Non dice come risolvono i nomi le altre app. Se la rete usa il [filtraggio DNS](/articles/nextdns-vs-adguard-ad-blocker-comparison/), prova un dominio che blocchi intenzionalmente e uno che consenti. L'assenza di un annuncio non prova l'instradamento del resolver.

## Indaga una differenza WebRTC

Controlla se il browser è escluso dal tunnel VPN o usa un proxy fuori dal percorso previsto. Correggi il percorso e ripeti il test. Non disattivare IPv6 o WebRTC come prima risposta a un solo risultato ambiguo. Lo [standard WebRTC](https://datatracker.ietf.org/doc/html/rfc8828) descrive il compromesso tra esposizione dell'indirizzo e prestazioni delle chiamate dirette. Limitare i candidati o imporre un proxy influisce sulle videochiamate e sulle altre connessioni peer.

Se il browser o la VPN offrono un controllo documentato per la gestione degli IP WebRTC, leggi la descrizione attuale e scegli una policy coerente con il tuo uso delle chiamate. Ripeti il test del candidato pubblico. Un solo indirizzo locale non dimostra che l'IP pubblico del provider sia uscito dalla VPN. Un IP pubblico del provider esposto, insieme a un IP HTTP VPN diverso, è un segnale più forte.

## Conserva un registro dei test

| Campo | Risultato da inserire |
|---|---|
| **Data e browser** | Versione, profilo, estensioni e rete |
| **Percorso previsto** | VPN per tutto il dispositivo, split tunnel o proxy del browser |
| **Prima e dopo** | Operatore IP pubblico, operatore DNS, candidato WebRTC pubblico |
| **Differenza** | Quale risultato non corrispondeva alla policy prevista |
| **Singola modifica** | Impostazione modificata e motivo |
| **Nuovo test** | Nuovo risultato e incertezze rimaste |

Ripeti la verifica dopo le modifiche alla configurazione del browser, della VPN o della rete. Un risultato pulito vale per il browser, il profilo, la rete e il momento testati. Non dimostra anonimato e non copre ogni app. Se devi ancora scegliere un browser, consulta il [confronto dei browser per la privacy](/articles/best-privacy-browsers-librewolf-brave-firefox-tor/) per le funzionalità, poi esegui questo test sulla tua configurazione.

## Passi successivi

Ripeti il test dopo modifiche al browser, alla VPN o alla rete. Consulta il [confronto dei browser per la privacy](/articles/best-privacy-browsers-librewolf-brave-firefox-tor/) per scegliere un browser.
