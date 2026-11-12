---
title: "Perché il filtro DNS viene aggirato: verifica il percorso del resolver"
date: 2026-10-11
lastmod: 2026-11-12
toc: true
draft: false
description: "Scopri perché un dispositivo o un browser ignora il filtro DNS. Confronta le query dirette e predefinite, controlla i log e verifica DNS crittografato, VPN, IPv6 e impostazioni del router."
genre: ["Reti domestiche", "DNS", "Privacy"]
tags: ["aggiramento filtro DNS", "aggiramento Pi-hole", "registro query DNS", "DNS sicuro browser", "DNS over HTTPS", "Android Private DNS", "iCloud Private Relay", "DNS VPN", "DNS IPv6", "DHCP DNS router", "Resolve-DnsName", "risoluzione problemi DNS", "test filtro DNS", "risoluzione problemi NextDNS", "risoluzione problemi AdGuard DNS"]
cover: "/img/cover/dns-filtering-bypass-troubleshooting.webp"
coverAlt: "Il percorso DNS blu di un portatile attraversa un filtro e si ferma a un simbolo di blocco, mentre il percorso arancione del browser raggiunge un altro resolver."
coverCaption: "Traccia il percorso della query prima di modificare la regola del filtro."
---

Hai configurato un resolver con filtro, ma un dispositivo continua a raggiungere un dominio bloccato dalle tue regole. La causa potrebbe essere la regola, l’assegnazione del Domain Name System (DNS) al dispositivo, un resolver crittografato del browser o una VPN. **Verifica il percorso prima di modificare le impostazioni.** Una query diretta al filtro risponde a una domanda diversa rispetto a una normale query del dispositivo.

<!--more-->

## Punti chiave

- **Controlla prima la regola:** Verifica che il filtro riceva e blocchi un dominio di test sicuro.
- **Traccia ogni livello:** Router, sistema operativo, browser, VPN e impostazioni mobili influiscono sull’instradamento DNS.
- **Usa query nuove:** Abbina un nuovo nome host e l’orario al registro delle query del filtro.
- **Dichiara il limite:** Una query osservata dimostra un solo percorso, non il comportamento di ogni app o dispositivo.

## Prima di iniziare

Prevedi circa 20 minuti. Ti servono l’accesso al registro delle query del resolver filtrante, un dispositivo con il problema e una copia delle impostazioni DNS del router. Gli esempi usano un portatile Windows e **Pi-hole**, ma lo stesso confronto funziona con qualsiasi resolver che registra le query per client. Individua prima l’indirizzo esatto del filtro. Non includere indirizzi privati dei client, registri delle query o regole in un rapporto pubblico.

Scegli un **dominio di test innocuo** già bloccato dalle tue regole. In alternativa, aggiungi temporaneamente una regola di rifiuto esatta per un dominio che controlli in un profilo di test. Annota la regola e rimuovila dopo il test. Non usare come sonda un dominio malware attivo. Una pagina bloccata è un sintomo utile, ma il registro del resolver fornisce prove più solide sul percorso.

| Livello | Domanda |
|---|---|
| **Filtro** | Una query diretta raggiunge il resolver previsto e corrisponde alla regola? |
| **Dispositivo** | Quali server DNS assegna la rete? |
| **Browser o app** | Questo client usa il resolver del dispositivo o un percorso separato? |
| **VPN o relay** | Un tunnel attivo cambia la destinazione delle query? |

## Verifica il filtro

Apri il registro delle query del resolver. Interroga direttamente il filtro sul dominio bloccato scelto. In Windows usa PowerShell e inserisci l’indirizzo del filtro e il dominio di test quando richiesto:

```powershell
$filterAddress = Read-Host "Filtering DNS server address"
$testDomain = Read-Host "Harmless domain blocked by your test rule"
Resolve-DnsName -Name $testDomain -Server $filterAddress -Type A -DnsOnly
```

La [documentazione Microsoft di **`Resolve-DnsName`**](https://learn.microsoft.com/en-us/powershell/module/dnsclient/resolve-dnsname) definisce **`-Server`** come una query inviata al resolver specificato. Cerca la query nel registro del filtro e verifica la risposta e la regola applicata. La [documentazione di Pi-hole su query e registri](https://docs.pi-hole.net/main/pihole-command/) descrive gli strumenti locali per le query. Se la query diretta viene consentita, correggi la regola o l’assegnazione del gruppo client prima di indagare su un bypass. Se non raggiunge il filtro, controlla l’indirizzo, il servizio e il percorso di rete.

**Questo test diretto non dimostra che il portatile usi normalmente il filtro.** L’opzione **`-Server`** sostituisce il resolver predefinito per questa query. Questa distinzione evita un falso esito positivo comune.

## Traccia il percorso del dispositivo

Usa un nuovo nome host per evitare una precedente voce nella cache DNS. L’esempio seguente invia una query direttamente al filtro e un’altra tramite la normale selezione del resolver del portatile. I nomi sono diversi, così puoi identificare quale voce del registro appartiene a ciascun percorso. Una risposta **NXDOMAIN** significa che il server DNS indica che il nome host non esiste. È normale se il nome casuale non è in uso. Qui conta la presenza della query nel registro del filtro.

```powershell
$stamp = [guid]::NewGuid().ToString("N")
Resolve-DnsName -Name "direct-${stamp}.example.com" -Server $filterAddress -Type A -DnsOnly
Resolve-DnsName -Name "default-${stamp}.example.com" -Type A -DnsOnly
```

Cerca nel registro del filtro entrambi i nomi esatti e annota l’orario e il client indicato. Se compare **`direct-`** ma non **`default-`**, controlla i server DNS assegnati al portatile. In Windows, **`Get-DnsClientServerAddress`** mostra gli indirizzi DNS per interfaccia. Controlla l’adattatore Wi-Fi o Ethernet attivo, non uno scollegato. La [documentazione Microsoft del client DNS](https://learn.microsoft.com/en-us/powershell/module/dnsclient/get-dnsclientserveraddress) descrive questo comando di sola lettura.

Lascia visibili gli errori durante il primo test. Un errore o un timeout richiede una diagnosi separata e non equivale a una query assente dal registro.

```powershell
Get-DnsClientServerAddress | Select-Object InterfaceAlias, AddressFamily, ServerAddresses
```

Confronta le righe IPv4 e IPv6. **DHCP** assegna impostazioni di rete come i server DNS. **IPv6** è la famiglia più recente di indirizzi Internet Protocol e usa indirizzi a 128 bit. Un lease IPv4 potrebbe indicare il filtro mentre gli annunci IPv6 del router forniscono un altro server DNS. Controlla gli annunci **DHCP** e **DNS IPv6** del router, quindi rinnova il lease di rete del dispositivo dopo una correzione. La [guida post-installazione di Pi-hole](https://docs.pi-hole.net/main/post-install/) spiega come DHCP indirizza i client a Pi-hole. L’[esempio per router](https://docs.pi-hole.net/routers/fritzbox/) tratta gli annunci DNS IPv6.

Se il registro mostra il **router** come client, il router potrebbe inoltrare le query per conto dei dispositivi. In tal caso, il registro prova che il router ha raggiunto il filtro, non quale dispositivo ha originato la query. Verifica l’inoltro del router prima di considerare l’identità del client come un dato mancante.

## Controlla il DNS del browser

Una query da riga di comando verifica il percorso del resolver del dispositivo. Un browser potrebbe usare invece **DNS over HTTPS (DoH)**. Apri lo stesso dominio di test bloccato nel browser e cerca nel registro del filtro la query corrispondente. Svuota la cache DNS del browser oppure usa un nuovo nome host coperto da una regola di test se i risultati memorizzati rendono difficile il confronto.

In **Chrome su un computer**, apri **Impostazioni > Privacy e sicurezza > Sicurezza > Usa DNS sicuro**. La [guida di Google Chrome](https://support.google.com/chrome/answer/10468685?co=GENIE.Platform%3DDesktop&hl=en) spiega che la modalità automatica usa il provider corrente e, in caso di errore, ripiega su una ricerca non crittografata. Un provider personalizzato selezionato non effettua lo stesso fallback. Annota la modalità e il provider selezionati prima di cambiare impostazioni.

In **Firefox**, apri **Impostazioni > Privacy e sicurezza > DNS su HTTPS**. La [guida Mozilla sui livelli di protezione](https://support.mozilla.org/en-US/kb/dns-over-https) distingue le modalità Predefinita, Aumentata, Massima, Personalizzata e Disattivata. La [panoramica DoH](https://support.mozilla.org/en-US/kb/firefox-dns-over-https) spiega quando un resolver del browser aggira un filtro DNS locale. Ripeti il test dopo una sola modifica controllata, quindi ripristina l’impostazione di privacy desiderata.

**Non definire automaticamente un bypass ogni query mancante del browser.** Il browser potrebbe riutilizzare dati in cache, raggiungere un indirizzo già noto o usare un proxy. Confronta un nome nuovo, una finestra temporale corrispondente e l’impostazione del resolver del browser prima di concludere dove è andata la query.

## Controlla percorsi mobili e VPN

Su **Android**, controlla **Impostazioni > Rete e Internet > DNS privato**. Un nome host del provider seleziona un servizio DNS privato distinto dal DNS annunciato dal router. Le [impostazioni di rete Android di Google](https://support.google.com/android/answer/9654714?hl=en) descrivono le opzioni Disattivato, Automatico e Nome host del provider. Per un risultato locale controllato, esegui il test in Wi-Fi con i dati cellulari disattivati, quindi ripristina l’impostazione normale.

Sui **dispositivi Apple**, verifica se **iCloud Private Relay** è attivo per la rete e se Safari segue il percorso previsto. Apple afferma che [Private Relay protegge la navigazione Safari e le informazioni DNS](https://support.apple.com/en-gb/102602). I [controlli di rete](https://support.apple.com/en-ie/102022) descrivono la gestione per rete quando il filtro entra in conflitto con Private Relay. Non estendere un risultato di Safari a tutte le app del dispositivo.

Una **VPN** potrebbe fornire un resolver DNS proprio o inviare le query attraverso il tunnel. Annota se la VPN è connessa, le sue impostazioni DNS e la policy di split tunneling. Confronta lo stesso test con la VPN attiva e disattiva solo se le tue regole di sicurezza lo consentono. Un risultato diverso identifica una differenza di percorso. Da solo non prova una fuga di dati né un difetto del filtro.

## Interpreta i risultati

| Evidenza | Controllo successivo probabile |
|---|---|
| **Query diretta assente dal registro del filtro** | Indirizzo del filtro, servizio DNS, registrazione o raggiungibilità di rete |
| **Query diretta consentita** | Regola di rifiuto esatta, policy del gruppo o priorità delle regole |
| **Query diretta registrata, predefinita assente** | DHCP, DNS statico del dispositivo, DNS IPv6 o resolver VPN |
| **Query predefinita registrata, browser assente** | DoH del browser, cache, proxy o relay |
| **Entrambe registrate e bloccate, ma il sito si apre** | Altro nome host, contenuto in cache, indirizzo diretto o percorso dell’app |

**I log mancanti sono ambigui** se la registrazione è disattivata, il router inoltra per il client o il test riutilizza dati memorizzati. Ripeti con un nuovo nome host e controlla l’orario della query prima di modificare le regole firewall. Bloccare il DNS in chiaro verso resolver esterni non obbliga un browser crittografato o una VPN a usare il filtro. La [guida OPNsense di Pi-hole](https://docs.pi-hole.net/routers/opnsense/) presenta il blocco del DNS esterno come controllo di rete opzionale. Le policy del dispositivo e la configurazione del browser restano controlli separati.

## Correggi e ripeti il test

Modifica un livello alla volta. Correggi gli annunci DHCP o DNS IPv6, rimuovi un resolver statico non previsto, seleziona il provider DNS desiderato nel browser oppure adegua la policy DNS della VPN. Non indebolire senza avviso DNS crittografato o protezioni relay su tutti i dispositivi per risolvere un singolo test fallito. Registra dispositivo di origine, interfaccia, indirizzo del filtro, nome richiesto, orario, risposta, client nel registro, modalità del browser, stato VPN e modifica effettuata.

Dopo ogni modifica ripeti i test **diretto**, **predefinito** e **del browser**. Usa un nuovo nome host per ogni esecuzione. Se un dispositivo ha più profili di rete, verifica ciascuno separatamente. Il [confronto tra resolver DNS](/articles/dns-comparison-adguard-quad9-cloudflare-pi-hole/) aiuta a scegliere un servizio. Il [test delle perdite del browser](/articles/privacy-browser-leak-test-dns-webrtc/) risponde a una domanda diversa: quali informazioni di rete escono dalla configurazione del browser e della VPN. **Un risultato affidabile del filtro richiede una regola verificata e un percorso client verificato.**

## Prossimi passi

Ripeti i test diretto, predefinito e del browser dopo ogni modifica controllata. Consulta il [confronto tra resolver DNS](/articles/dns-comparison-adguard-quad9-cloudflare-pi-hole/) quando scegli un servizio di filtraggio.
