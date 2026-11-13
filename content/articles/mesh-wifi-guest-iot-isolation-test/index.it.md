---
title: "Verifica l’isolamento di ospiti e dispositivi IoT su una rete Wi-Fi mesh"
date: 2026-10-11
lastmod: 2026-11-12
toc: true
draft: false
description: "Verifica se le reti ospiti e IoT del tuo Wi-Fi mesh bloccano l’accesso ai dispositivi domestici. Prova ogni rete con un servizio funzionante e registra i limiti."
genre: ["Reti domestiche", "Sicurezza Wi-Fi", "Casa intelligente"]
tags: ["rete Wi-Fi mesh per ospiti", "test isolamento rete ospiti", "isolamento rete IoT", "sicurezza Wi-Fi mesh", "isolamento client", "test Wi-Fi ospiti", "SSID IoT", "modalità access point", "modalità router", "accesso LAN", "test rete locale", "rete ospiti Deco", "rete ospiti Orbi", "rete ospiti ASUS", "Wi-Fi ospiti Google Nest", "Test-NetConnection", "test connettività TCP", "rete casa intelligente", "isolamento client wireless", "segmentazione rete domestica"]
cover: "/img/cover/mesh-wifi-guest-iot-isolation-test.webp"
coverAlt: "Una casa a due piani con due router mesh, telefoni ospiti, luci e telecamere IoT e uno scudo che blocca il percorso verso un laptop affidabile e un NAS."
coverCaption: "Prova separatamente i percorsi tra rete ospiti, IoT e rete principale."
---

Un nome Wi-Fi distinto non rivela quali dispositivi comunicano tra loro. Un sistema mesh potrebbe trattare la **rete ospiti**, la **rete IoT** e l’**isolamento dei client wireless** come controlli diversi. Questa guida ti aiuta a provare i percorsi sui tuoi dispositivi senza presumere che l’etichetta del produttore descriva la regola applicata.

<!--more-->

## Punti chiave

- **Verifica prima che la destinazione funzioni:** raggiungi un servizio noto dalla rete principale prima di provare un percorso bloccato.
- **Prova ogni confine:** l’accesso da ospiti alla rete principale, da IoT alla rete principale e tra ospiti risponde a domande diverse.
- **Registra la configurazione:** modello, firmware, modalità router o access point e nodo mesh connesso incidono sull’interpretazione.
- **Ripeti dopo ogni modifica:** un risultato valido riguarda solo i dispositivi, il servizio, la famiglia di indirizzi e la configurazione provati.

## Prima di iniziare

Dedica circa 20 minuti. Ti serve un laptop che possa collegarsi alle reti Wi-Fi principale, ospiti e IoT. Ti serve anche un dispositivo attendibile sulla rete principale con un **servizio TCP aperto noto**, ad esempio l’interfaccia web di un NAS. Un servizio TCP è un servizio di rete in ascolto su una porta numerata, per esempio la porta 443 di una pagina web NAS. Usa un servizio di tua proprietà o che amministri. Annota il suo indirizzo locale e la porta, senza pubblicarli. Mantieni il servizio attivo per tutta la prova.

Annota modello mesh, versione firmware, modalità operativa e impostazioni di accesso ospiti, accesso IoT, dispositivi condivisi e isolamento client. Controlla il nome Wi-Fi del laptop dopo ogni cambio di rete. Se le tue regole abituali lo consentono, disconnetti la VPN o il proxy per questa prova del percorso locale, poi ripristinali. Una VPN modifica il percorso in esame.

> **Avviso:** prova solo i tuoi dispositivi o quelli che hai il permesso di amministrare. La pagina di accesso del router non sostituisce un host sulla rete principale, perché l’accesso al gateway segue regole diverse.

Una **rete locale (LAN)** è la tua rete domestica privata. **IoT**, o Internet delle cose, comprende dispositivi come telecamere, altoparlanti e prese intelligenti. L’**isolamento client** blocca il traffico diretto tra dispositivi sulla stessa rete Wi-Fi.

## Definisci il confine

Scegli il risultato desiderato prima di cambiare un’impostazione. L’accesso a Internet e l’accesso locale sono risultati distinti.

| Percorso | Domanda | Esempio di risultato previsto |
|---|---|---|
| **Ospiti verso LAN principale** | È possibile raggiungere un computer o un NAS? | Bloccato, salvo eccezioni scelte |
| **IoT verso LAN principale** | È possibile raggiungere dispositivi privati? | Dipende dal prodotto e dalla tua regola |
| **Ospite verso ospite** | Due ospiti riescono a comunicare? | Dipende dalle impostazioni di isolamento client |
| **Ospiti verso dispositivo condiviso** | È possibile usare una stampante o uno schermo condiviso? | Consentito solo se previsto |
| **Ospiti verso Internet** | È accessibile un normale sito pubblico? | Consentito se la regola ospiti include Internet |

Queste righe rappresentano prove separate. La [guida TP-Link all’isolamento dei dispositivi Deco](https://www.tp-link.com/us/support/faq/3968/) spiega che i dispositivi isolati conservano l’accesso a Internet e la comunicazione con altri dispositivi isolati, mentre l’accesso ai dispositivi della rete principale è bloccato. La [guida ASUS all’isolamento AP](https://www.asus.com/us/support/faq/1044821/) descrive un controllo tra peer wireless e specifica che un percorso attraverso un router cablato a monte non rientra nel controllo. **Un singolo percorso bloccato non dimostra che tutti gli altri confini siano rispettati.**

## Controlla le impostazioni mesh

Individua la funzione che controlla il confine da provare. I nomi dei menu e la loro disponibilità variano in base a modello e firmware.

| Impostazione mesh | Che cosa verificare |
|---|---|
| **Rete ospiti TP-Link Deco** | La [modalità router isola gli ospiti dalla rete principale](https://www.tp-link.com/us/support/faq/1460/). In modalità access point, controlla **Allow Local Access**. |
| **Profilo ospiti ASUS** | [Access Intranet](https://www.asus.com/uk/support/faq/1009857/) controlla l’accesso alla rete principale nei profili supportati. |
| **Wi-Fi ospiti Google Nest** | Controlla l’elenco dei [dispositivi condivisi](https://support.google.com/googlehome/answer/6327302?hl=en) prima di aspettarti che una stampante o uno schermo siano nascosti. |
| **Rete IoT o isolamento dispositivi** | Verifica se il prodotto offre un controllo di isolamento separato. Un nome Wi-Fi IoT da solo non definisce la regola di accesso. |

Su Deco, l’[isolamento dei dispositivi](https://www.tp-link.com/us/support/faq/3968/) richiede il supporto dell’unità principale e dei satelliti. Annota quale nodo serve il laptop di prova. Se una funzione non è presente, consulta la documentazione del modello e del firmware esatti invece di presumere che l’app di un altro proprietario mostri la stessa configurazione.

## Stabilisci un controllo positivo

Collega il laptop Windows di prova al **Wi-Fi principale**. Verifica che il servizio scelto funzioni da quel laptop. Se usi PowerShell, inserisci l’indirizzo dell’host della rete principale e la sua porta aperta nota quando richiesto:

```powershell
$targetAddress = Read-Host "Main-network test host address"
$targetPort = [int](Read-Host "Known open TCP port")
Test-NetConnection -ComputerName $targetAddress -Port $targetPort
```

La [documentazione Microsoft di Test-NetConnection](https://learn.microsoft.com/powershell/module/nettcpip/test-netconnection) definisce `-ComputerName` e `-Port` come un test per uno specifico host e servizio TCP. Registra `TcpTestSucceeded`. Ottieni prima `True`, poi interpreta un eventuale `False`. Se il test sulla rete principale fallisce, il problema riguarda il servizio, l’indirizzo, il firewall dell’host o la configurazione del laptop. Risolvi prima il test sulla rete principale.

Se usi un telefono o un altro sistema operativo, apri lo stesso servizio noto nel browser o nell’app. Mantieni esattamente lo stesso servizio e l’indirizzo di destinazione quando cambi rete Wi-Fi. Un elenco di rilevamento dei dispositivi fornisce prove meno solide, perché il traffico di rilevamento e l’accesso TCP diretto seguono percorsi diversi.

## Prova l’accesso ospiti e IoT

Collega lo stesso laptop al **Wi-Fi ospiti**. Verifica il nome della rete. Apri un sito pubblico se la tua regola ospiti include l’accesso a Internet. Esegui di nuovo lo stesso comando `Test-NetConnection` senza cambiare `$targetAddress` né `$targetPort`. Registra il risultato.

Torna alla rete principale e verifica che il servizio restituisca ancora `True`. Se il test principale ora fallisce, il risultato ospiti non è conclusivo. Poi collega lo stesso laptop al **Wi-Fi IoT**, se il sistema consente il collegamento di un laptop, e ripeti il test. Non presumere che l’esito IoT corrisponda a quello ospiti. Un esito positivo da IoT alla rete principale significa che, in questa configurazione, il servizio TCP locale scelto era raggiungibile dalla rete IoT.

Se vuoi isolare gli ospiti tra loro, usa due dispositivi che controlli sulla rete ospiti. Da uno, prova un servizio noto sull’altro. Registra questo risultato separatamente dall’accesso ospiti verso la rete principale. Se vuoi che una stampante o uno schermo condiviso funzioni, prova anche l’eccezione prevista. Il controllo cloud di un dispositivo smart non dimostra l’esistenza di un percorso locale diretto.

Ripeti la prova ospiti-verso-principale vicino a ogni nodo mesh. Se l’app segnala il nodo collegato, controllalo. **IPv6** è la famiglia di indirizzi del Protocollo Internet più recente e usa indirizzi a 128 bit. Se l’host principale supporta IPv6 e il controllo positivo sulla rete principale riesce via IPv6, ripeti lo stesso test di famiglia di indirizzi dalle reti Wi-Fi ospiti e IoT. Un test solo IPv4 non copre un percorso IPv6.

## Interpreta una differenza

| Osservazione | Controllo successivo |
|---|---|
| **Falliscono sia la rete principale sia quella ospiti** | Controlla il servizio di destinazione, l’indirizzo, la porta e il firewall dell’host. L’isolamento non è dimostrato. |
| **Riescono sia la rete principale sia quella ospiti** | Controlla l’accesso locale ospiti, le eccezioni dei dispositivi condivisi e la modalità router rispetto alla modalità access point. |
| **Rete principale riuscita, ospiti fallita** | Registra le prove per questa destinazione e questo percorso TCP. Prova gli altri percorsi richiesti dalla tua regola. |
| **Ospiti bloccata, IoT riuscita** | Verifica se il nome IoT identifica una rete di compatibilità senza una regola di isolamento corrispondente. |
| **Ospiti verso rete principale bloccato, ospiti tra loro riuscito** | Controlla separatamente l’isolamento dei client wireless. |

Un **ping** fallito non risponde alla domanda TCP. Il firewall di un host potrebbe bloccare il ping e accettare il servizio scelto. Anche un test TCP fallito ha una portata limitata: non dice nulla su altre porte, dispositivi, IPv6 o eccezioni per i dispositivi condivisi. Considera una differenza come un motivo per controllare la regola configurata e ripetere un test controllato.

## Correggi e registra il risultato

Modifica un solo controllo alla volta. Su Deco in modalità access point, controlla **Allow Local Access**. Su un profilo ospiti ASUS, controlla **Access Intranet**. Su Google Nest Wifi, rimuovi un elemento non previsto da **Shared devices**. Se ti serve il controllo locale della casa intelligente, decidi quale dispositivo deve raggiungere quale servizio prima di aggiungere un’eccezione. Una **VLAN** è una rete logica trasportata su hardware condiviso. Il [piano di segmentazione VLAN](/articles/homelab-vlan-segmentation-plan/) del sito descrive una rete gestita quando un mesh consumer non offre la regola di accesso necessaria.

Registra modello mesh, firmware, modalità operativa, nodo, nome Wi-Fi, dispositivo di origine, servizio di destinazione, famiglia di indirizzi, risultato previsto, risultato effettivo e singola modifica effettuata. Non pubblicare indirizzi privati o password di rete. Ripeti le stesse prove dopo aggiornamenti firmware, cambi di nodo o passaggi tra modalità router e access point.

Se stai ancora scegliendo l’attrezzatura, confronta le funzioni nella [guida all’acquisto di Wi-Fi mesh](/articles/best-wifi-mesh-system-for-consumers/). Poi usa questa procedura per verificare la rete installata. **Un’etichetta o un interruttore nell’app è un’affermazione. Un controllo positivo e una nuova prova a condizioni uguali forniscono prove per il percorso specifico che ti interessa.**

## Passi successivi

Ripeti i test di isolamento dopo modifiche a firmware, nodi o modalità operative. Usa il [piano di segmentazione VLAN](/articles/homelab-vlan-segmentation-plan/) quando i controlli mesh non rispettano il confine richiesto.
