---
title: "Privacy.com Carte Virtuali: Come Funziona la Privacy nei Pagamenti"
date: 2023-09-03
lastmod: 2026-10-08
toc: true
draft: false
description: Cosa viene memorizzato su una carta di pagamento, perché la banda magnetica è la parte più debole, cosa vede il commerciante quando paghi con un numero virtuale e come funzionano in pratica i tipi di carta e i limiti di Privacy.com.
genre:
- Sicurezza dei Pagamenti
- Privacy Digitale
- Carte Virtuali
- Privacy Finanziaria
- Prevenzione delle Frodi
- Sicurezza del Consumatore
tags:
- privacy.com
- carte virtuali
- carte di debito virtuali
- carte monouso
- carte bloccate per commerciante
- carte bloccate per categoria
- tokenizzazione
- token di rete
- pan
- cvv
- skimming della carta
- banda magnetica
- traccia 1
- traccia 2
- sicurezza delle carte di pagamento
- frode con carta di credito
- gestione abbonamenti
- limiti di spesa
- pci dss
- soc 2
- frode senza presenza della carta
- privacy finanziaria
- privacy nei pagamenti
- numero di carta virtuale
- carta mascherata
- controlli della carta
cover: /img/cover/privacy_virtual_cards.webp
coverAlt: Un'illustrazione digitale che mostra una carta virtuale schermata che protegge un simbolo di lucchetto, rappresentando la sicurezza e la privacy offerte dalle carte di debito virtuali.
coverCaption: Proteggi, Controlla e Metti in Sicurezza le Tue Transazioni Online.
ref:
- /magnetic-stripe-decoder
- /articles/personal-security-checklist-prioritized-2026
- /personal-security-course/personal-finance
---

**Una carta virtuale fa una cosa specifica: cambia ciò che il commerciante riceve, non ciò che la tua banca conosce.** Questo è tutto il meccanismo, e capirlo spiega sia la protezione che ottieni sia quella che non ottieni.

La maggior parte delle trattazioni considera le carte virtuali come uno strumento generale di privacy e salta i dettagli tecnici. Questo articolo spiega cosa è memorizzato su una carta, perché la banda magnetica è il punto debole e come si comportano in pratica i tipi di carta di Privacy.com.

*Il vantaggio pratico è ristretto e reale: un numero rubato diventa inutile per un ladro, perché funziona solo presso il commerciante per cui è stato emesso.*

## La Risposta Breve

| Domanda | Risposta Breve |
|---|---|
| **Cosa cambia una carta virtuale?** | Il numero che il commerciante memorizza. I tuoi dati reali della carta non li raggiungono mai |
| **La transazione è privata?** | No. La tua banca, la rete e l’emittente la vedono comunque |
| **Cosa impedisce che una violazione ti danneggi?** | Un numero bloccato per commerciante o monouso, che fallisce ovunque altrove |
| **Qual è la parte più debole di una carta fisica?** | La banda magnetica, che memorizza i dati completi della traccia in chiaro |
| **Costruisce credito?** | No. Non sono conti di credito e non avviene alcuna verifica del credito |
| **Chi può usare Privacy.com?** | Cittadini o residenti legali USA, 18+, con conto corrente bancario o creditizio USA |

## Cosa C’è su una Carta di Pagamento

**Tre elementi autorizzano una transazione senza presenza della carta: il numero di conto principale, la data di scadenza e il valore di verifica.**

| Elemento | Lunghezza | Origine |
|---|---|---|
| **Numero di Conto Principale (PAN)** | Fino a 19 cifre | L’emittente, con cifre iniziali che identificano lo schema e la banca |
| **Scadenza** | Quattro cifre come MM/AA | L’emittente |
| **CVV o CVC** | Tre o quattro cifre | Derivato da PAN, scadenza e una chiave che solo l’emittente possiede |
| **Nome del titolare** | Fino a 26 caratteri | Presente solo sulla Traccia 1 della banda magnetica |

**Il PAN non è una stringa casuale.** La prima cifra identifica lo schema, le successive identificano la banca emittente e il resto identifica il conto. La struttura permette di verificare la plausibilità del numero senza contattare nessuno, e spiega perché la cifra di controllo Luhn rileva una singola cifra trasposta.

**Il CVV dimostra che qualcuno ha fisicamente posseduto la carta** quando è stata emessa. Non è memorizzato sulla banda magnetica, ed è proprio per questo che uno skimmer che copia la banda non lo ottiene mai.

*Esamina tutto questo da solo con il **[Decodificatore e Codificatore di Bande Magnetiche](/magnetic-stripe-decoder/)**, che analizza la Traccia 1 e la Traccia 2, decodifica i codici di servizio e ricodifica il risultato. Funziona interamente nel tuo browser, il che è importante perché questo è il contenuto completo di una carta di pagamento.*

{{< figure src="payment-card-data-anatomy-pan-cvv-tracks.webp" alt="Diagramma che mostra gli elementi di una carta di pagamento inclusi il numero di conto principale, la data di scadenza, il CVV e le tre tracce della banda magnetica con cosa contiene ciascuna" >}}

## Perché la Banda Magnetica è il Punto Debole

**La banda memorizza i dati dell’account in chiaro, e qualsiasi lettore compatibile li legge.**

Una banda magnetica contiene fino a tre tracce. La Traccia 1 contiene il PAN, il nome del titolare, la scadenza e un codice di servizio a tre cifre, ed è l’unica traccia che contiene testo alfabetico. La Traccia 2 contiene PAN, scadenza e codice di servizio in una codifica numerica più densa, e **la Traccia 2 è quella che quasi tutti i terminali di punto vendita leggono.** La Traccia 3 è praticamente inutilizzata dalle principali reti e spesso non è presente sulla carta.

Il codice di servizio è importante da capire perché descrive l’uso consentito della carta. La prima cifra riguarda le regole di interscambio, la seconda la gestione dell’autorizzazione, e la terza la gamma di servizi. Una carta codificata `201` permette l’interscambio internazionale, non richiede un percorso di autorizzazione speciale e non ha restrizioni di servizio.

La storia spiega perché la banda è durata così a lungo. Nel 1969 un ingegnere IBM di nome Forrest Parry provò ad attaccare un nastro magnetico a una carta di plastica ma non riuscì a farlo aderire senza danneggiarlo. Sua moglie suggerì di usare un ferro da stiro, e il calore incollò il nastro alla carta. Questa improvvisazione divenne lo standard per oltre mezzo secolo.

Due sviluppi stanno ponendo fine a questa tecnologia:

| Traguardo | Stato |
|---|---|
| **Mastercard ha annunciato la rimozione della banda** | Entro il 2033, nessuna carta Mastercard di credito o debito la avrà più |
| **Europa** | Le bande hanno iniziato a sparire dalle carte Mastercard nel 2024 |
| **Stati Uniti** | Le banche smetteranno di emetterle a partire dal 2027 |

*La banda è stata sostituita da chip e pagamenti contactless perché copiarla non richiede abilità oltre al possesso di un lettore. Il nostro **[strumento per bande magnetiche](/magnetic-stripe-decoder/)** mostra quanto pochi dati servano per ricostruire una traccia funzionante.*

{{< figure src="magnetic-stripe-track-layout-track1-track2.webp" alt="Diagramma di una banda magnetica che mostra la posizione fisica delle tracce uno, due e tre, con la disposizione dei campi di ogni traccia inclusi sentinelle, PAN, nome, scadenza e codice di servizio" >}}

## Come Leggere i Dati della Traccia

**Una stringa di banda magnetica è una sequenza di campi, non un secondo numero di carta.** Il lettore trova il sentinella di inizio, separa i campi, legge la scadenza e il codice di servizio, poi verifica il sentinella di fine e il LRC.

| Traccia | Inizio | Campi principali | Fine | Set di caratteri |
|---|---|---|---|---|
| **Traccia 1** | `%` | Codice formato, PAN, nome, scadenza, codice servizio, dati discrezionali | `?` più LRC | ALPHA a sei bit, quindi contiene lettere |
| **Traccia 2** | `;` | PAN, scadenza, codice servizio, dati discrezionali | `?` più LRC | BCD a quattro bit, quindi contiene cifre e un piccolo set di punteggiatura |

I sentinelle opzionali identificano i confini fisici del record. Un decodificatore spesso li omette quando visualizza i campi, ma un codificatore fisico necessita del formato completo del record previsto dal lettore.

### Esempio Traccia 1

Questo è un esempio sintetico. Usa il PAN di test standard dello strumento e nome, scadenza, codice servizio e dati discrezionali finti. Non è una carta Privacy.com e non sono dati di pagamento validi.

```text
%B4111111111111111^TEST/USER^2912501000000000?
```

Leggilo da sinistra a destra:

| Segmento | Valore | Significato |
|---|---|---|
| **Sentinella di inizio** | `%` | Inizio record Traccia 1 |
| **Codice formato** | `B` | Formato carta finanziaria B |
| **PAN** | `4111111111111111` | Numero di conto primario sintetico |
| **Separatore campo** | `^` | Fine PAN e inizio nome |
| **Nome** | `TEST/USER` | Cognome, separatore, nome |
| **Separatore campo** | `^` | Fine nome e inizio campi transazione |
| **Scadenza** | `2912` | Dicembre 2029 in formato AAmm |
| **Codice servizio** | `501` | Intercambio nazionale, elaborazione normale, nessuna restrizione |
| **Dati discrezionali** | `0000000` | Riempitivo definito dall’emittente in questo esempio |
| **Sentinella di fine** | `?` | Fine dati Traccia 1 prima del LRC |

Il record codificato reale porta anche un carattere LRC dopo la sentinella di fine quando il lettore lo richiede. La forma testuale visibile è utile per studiare la struttura. La rappresentazione a livello di bit include anche la parità dispari per ogni carattere.

### Esempio Traccia 2

La Traccia 2 elimina nome e codice formato. Gli stessi valori sintetici diventano:

```text
;4111111111111111=291250100000000?
```

| Segmento | Valore | Significato |
|---|---|---|
| **Sentinella di inizio** | `;` | Inizio record Traccia 2 |
| **PAN** | `4111111111111111` | Numero di conto primario sintetico |
| **Separatore** | `=` | Fine PAN e inizio campi transazione |
| **Scadenza** | `2912` | Dicembre 2029 in formato AAmm |
| **Codice servizio** | `501` | Stesso codice servizio sintetico della Traccia 1 |
| **Dati discrezionali** | `0000000` | Riempitivo definito dall’emittente in questo esempio |
| **Sentinella di fine** | `?` | Fine dati Traccia 2 prima del LRC |

**La Traccia 2 è più corta perché non contiene il nome del titolare.** Molti terminali leggono la Traccia 2 per transazioni con strisciata ordinaria, mentre la Traccia 1 fornisce il campo nome quando un lettore lo richiede.

### Cifre del Codice Servizio

**Le tre cifre del codice servizio descrivono il comportamento del terminale e dell’autorizzazione.** Non contengono il CVV e modificarle su una carta reale senza autorizzazione dell’emittente produce una credenziale di pagamento malformata o fuorviante.

| Cifra | Valori | Cosa descrive |
|---|---|---|
| **Prima** | `0`, `1`, `2`, `5`, `6`, `7`, `9` | Regole di intercambio e preferenza chip |
| **Seconda** | `0`, `1`, `2`, `4` | Percorso di autorizzazione |
| **Terza** | `0` fino a `7` | Restrizioni su PIN, contanti, beni e servizi |

**La prima cifra** copre intercambio e preferenza chip:

| Valore | Significato |
|---|---|
| `0` | Uso nazionale |
| `1` | Intercambio internazionale consentito |
| `2` | Intercambio internazionale, usa IC (chip) dove possibile |
| `5` | Solo intercambio nazionale salvo accordo bilaterale |
| `6` | Solo intercambio nazionale salvo accordo bilaterale, usa IC dove possibile |
| `7` | Nessun intercambio salvo accordo bilaterale (circuito chiuso) |
| `9` | Test |

**La seconda cifra** copre la gestione dell’autorizzazione:

| Valore | Significato |
|---|---|
| `0` | Autorizzazione normale |
| `1` | Autorizzazione normale |
| `2` | Contatta l’emittente via canali online |
| `4` | Contatta l’emittente via canali online salvo accordo bilaterale |

**La terza cifra** copre le restrizioni di servizio:

| Valore | Significato |
|---|---|
| `0` | Nessuna restrizione, PIN richiesto |
| `1` | Nessuna restrizione |
| `2` | Solo beni e servizi (no contanti) |
| `3` | Solo ATM, PIN richiesto |
| `4` | Solo contanti |
| `5` | Solo beni e servizi (no contanti), PIN richiesto |
| `6` | Nessuna restrizione, usa PIN dove possibile |
| `7` | Solo beni e servizi (no contanti), usa PIN dove possibile |

Per esempio, `201` significa intercambio internazionale con uso chip dove possibile, elaborazione autorizzazione normale e nessuna restrizione di servizio. Il decodificatore espone ogni cifra separatamente così non devi memorizzare la tabella.

### LRC e Parità

**L’LRC è un carattere di controllo, non un altro campo da inventare.** Il codificatore fa l’XOR del valore dati di ogni carattere dal sentinella di inizio fino al sentinella di fine. Converte il risultato nel range di caratteri stampabili della traccia e riporta separatamente i bit di parità dispari codificati.

La Traccia 1 usa un set di caratteri ALPHA a sei bit. Il suo valore dati è il codice ASCII meno `0x20`. La Traccia 2 usa un set di caratteri BCD a quattro bit. Il suo valore dati è il nibble basso del codice ASCII. Applicare la mappatura della Traccia 1 alla Traccia 2 produce un LRC errato.

L’opzione **Includi LRC calcolato** del decodificatore aggiunge il carattere LRC stampabile all’output. La sua scomposizione mostra anche il pattern di bit LRC con parità dispari. Usalo per imparare come un lettore verifica il record, non per bypassare i controlli dell’emittente.

## Scrivere Carte Sintetiche per Test

**Usa il decodificatore per scrivere stringhe di test, non carte di pagamento reali.** Lo strumento accetta i campi, ricostruisce Traccia 1 e Traccia 2, aggiunge sentinelle opzionali e calcola l’LRC. Funziona localmente nel browser.

1. Apri il **[Decodificatore e Codificatore di Strisce Magnetiche](/magnetic-stripe-decoder/)**.
2. Seleziona **Carica Carta di Test**. Questo riempie lo strumento con il PAN sintetico `4111111111111111`, il nome `TEST/USER`, la scadenza `2912`, il codice di servizio `201` e i dati discrezionali di test.
3. Abilita **Includi sentinelle di inizio e fine** per mostrare i confini fisici del record.
4. Abilita **Includi LRC calcolato** per aggiungere il carattere di controllo calcolato.
5. Abilita **Dividi i dati discrezionali in PVKI, PVV e CVV** solo per vedere come viene visualizzato un campo sintetico di nove cifre. Queste etichette sono convenzioni dell'emittente, non un layout universale della Traccia 1 o Traccia 2.
6. Modifica il nome, la scadenza, il codice di servizio o i dati discrezionali sintetici. L'output si aggiorna mentre digiti.
7. Confronta i campi decodificati con le stringhe generate. Pulisci i campi al termine.

Per un esercizio sulla Traccia 1 sintetica, usa:

```text
PAN: 4111111111111111
Surname: TEST
First name: USER
Expiry: 12/29
Service code: 201
Discretionary data: 000000000
```

Per un esercizio sulla Traccia 2 sintetica, usa lo stesso PAN, scadenza, codice di servizio e un campo discrezionale numerico. La stringa generata per la Traccia 2 omette il nome perché la Traccia 2 non ha un campo nome.

**Non copiare un PAN, scadenza, CVV o valore discrezionale reale di Privacy.com in una carta scrivibile.** Privacy.com descrive il suo prodotto come numeri di carta virtuali creati tramite il suo sito web o app. La sua pagina ufficiale non presenta il servizio come un sistema di scrittura su striscia magnetica, mentre un numero di carta virtuale non è prova di un record fisico autorizzato dall'emittente. Una carta di test scrivibile contenente una credenziale reale crea uno strumento di pagamento duplicato e viola i termini dell'emittente o le regole di pagamento.

Il confine sicuro è semplice: usa il campione sintetico integrato nello strumento, usa una carta da laboratorio con valori fittizi e usa una carta fisica approvata dall'emittente quando devi pagare di persona. Non tentare di trasformare una carta virtuale Privacy.com in una carta fisica da striscia magnetica.

## Cosa Cambia una Carta Virtuale

**Una carta virtuale è un secondo numero che sta davanti al primo.**

Quando paghi con una carta virtuale, il commerciante riceve un numero, una scadenza e un CVV appartenenti alla carta virtuale. Il tuo vero PAN non arriva mai a loro. Praticamente, il cambiamento si nota dopo una violazione:

| Scenario | Con la tua carta reale | Con una carta virtuale bloccata al commerciante |
|---|---|---|
| **Database del commerciante compromesso** | Il numero è valido ovunque venga accettato | Il numero fallisce in ogni altro commerciante |
| **Abbonamento che hai cancellato** | Le addebiti continuano fino a quando non le contestate | Chiudi la carta e l'addebito fallisce |
| **Prova che si converte silenziosamente** | Addebito indesiderato sul tuo estratto conto | Il limite o la chiusura lo fermano |
| **Dettagli della carta venduti su un forum** | Usabile per frodi senza presenza fisica | Usabile solo presso un commerciante, se proprio |

**Ciò che non cambia** è altrettanto importante. La tua banca vede ancora la transazione. La rete di pagamento la elabora ancora. L'emittente detiene ancora la tua identità, perché le regole antiriciclaggio richiedono la verifica. **Una carta virtuale riduce l'esposizione lato commerciante. Non è un modo per spendere anonimamente.**

*La distinzione confonde costantemente le persone. Se il tuo modello di minaccia include l'emittente o la rete, una carta virtuale non cambia nulla.*

{{< figure src="virtual-card-merchant-shielding-flow.webp" alt="Diagramma che mostra un numero di carta virtuale che va al commerciante mentre il numero reale della carta rimane tra il titolare e la banca emittente" >}}

## I Tre Tipi di Oggetto a Forma di Carta

La terminologia è usata in modo incoerente e la differenza conta quando scegli cosa consegnare a un commerciante.

| Tipo | Numero della Carta | Versione Fisica | Uso Tipico |
|---|---|---|---|
| **Carta digitale** | Uguale alla tua carta fisica | Sì | Aggiungere la tua carta esistente a un portafoglio mobile |
| **Carta virtuale** | Diversa da qualsiasi carta fisica | No | Acquisti online, abbonamenti, commercianti occasionali |
| **Carta digital-first** | Diversa, con una carta fisica collegata opzionale | Opzionale | Conti fintech dove la carta fisica non riporta dettagli stampati |

**Un portafoglio mobile usa un meccanismo completamente diverso.** Quando aggiungi una carta a un portafoglio, il portafoglio memorizza un token specifico del dispositivo invece del tuo PAN, e il commerciante riceve il token. Questo si chiama tokenizzazione ed è il motivo per cui pagare con il telefono è più sicuro che consegnare la plastica anche senza una carta virtuale.

*La tokenizzazione di rete e le carte virtuali risolvono parti sovrapposte dello stesso problema. La tokenizzazione protegge il numero in transito e a riposo. Una carta virtuale ti protegge da ciò che il commerciante conserva dopo.*

## Tipi di Carta Privacy.com

**Privacy.com offre quattro comportamenti di carta, e non sono intercambiabili.**

| Tipo di Carta | Comportamento | Ideale Per |
|---|---|---|
| **Uso Singolo** | Si chiude automaticamente dopo una transazione | Acquisti occasionali e commercianti sconosciuti |
| **Bloccata al Commerciante** | Si blocca al primo commerciante che la usa e fallisce altrove | Shopping online quotidiano |
| **Bloccata per Categoria** | Limitata a una categoria di spesa | Contenere una classe intera di spese |
| **Ovunque** | Una carta fisica con lo stesso modello di protezione | Acquisti di persona |

**Il blocco al commerciante è il meccanismo che porta la maggior parte del valore.** Una carta bloccata fallisce in qualsiasi commerciante diverso da quello con cui è stata usata per la prima volta, il che significa che una violazione presso quel commerciante rende il numero inutile altrove.

**L'uso singolo è l'opzione più forte dove applicabile.** Una carta che si chiude dopo un addebito non può essere riutilizzata e rimuove la necessità di ricordarsi di chiuderla in seguito.

Due dettagli operativi da conoscere:

- **Le carte condivise si bloccano al primo commerciante con cui vengono usate**, quindi condividerla con un familiare o un dipendente mantiene comunque la restrizione al commerciante.
- **Una carta viene messa in pausa anziché chiusa.** La pausa è reversibile, utile quando vuoi fermare temporaneamente un abbonamento senza perdere i dettagli della carta.

## Limiti di Spesa e Controlli

**Ogni carta ha un limite di spesa, che è un controllo separato dal blocco al commerciante.**

| Controllo | Cosa Previene |
|---|---|
| **Limite per transazione** | Un singolo addebito superiore a quello autorizzato |
| **Limite mensile** | Addebiti accumulati in un periodo di fatturazione |
| **Pausa** | Qualsiasi addebito, in modo reversibile |
| **Chiusura** | Qualsiasi addebito futuro, in modo permanente |

**Imposta sia un limite per transazione sia un limite mensile su qualsiasi carta legata a un abbonamento.** Un commerciante che aumenta silenziosamente il prezzo colpisce il limite anziché il tuo saldo, e te ne accorgi da un addebito fallito invece che da una riga mancante nell'estratto conto.

*Il nostro modulo **[Sicurezza Finanziaria Personale](/personal-security-course/personal-finance/)** colloca questo insieme a blocchi di credito e tokenizzazione della carta come i tre controlli che limitano ciò a cui un singolo commerciante compromesso può accedere.*

## Piani e Cosa Sblocca Ognuno

Privacy.com offre un piano gratuito insieme a tre piani a pagamento. Prezzi e limiti delle funzionalità possono variare, quindi verifica i termini attuali prima di sottoscrivere.

| Piano | Prezzo | Aggiunte Notevoli |
|---|---|---|
| **Personale (gratuito)** | $0 | Carte virtuali, blocco per commerciante, limiti di spesa, nessuna commissione sulle transazioni nazionali |
| **Plus** | $5/mese | Carte per categoria, note sulle carte per organizzare le spese |
| **Pro** | $10/mese | Cashback sugli acquisti qualificati, carte fisiche Everywhere |
| **Premium** | $25/mese | Tutto in Pro, con limite mensile di creazione carte aumentato a 60 |

**Il piano gratuito copre il beneficio principale di sicurezza.** Il blocco per commerciante, le carte monouso e i limiti di spesa sono i meccanismi che riducono l’esposizione, e sono disponibili senza costi. I piani a pagamento aggiungono organizzazione e comodità, non protezione aggiuntiva.

**Le commissioni sulle transazioni estere variano per piano.** Il piano gratuito applica il 3% sulle transazioni estere con un minimo di $0,50, mentre i piani a pagamento non le applicano.

## Cosa Privacy.com Non Fa

**Essere chiari sui limiti è più utile di una lista di funzionalità.**

| Limitazione | Dettaglio |
|---|---|
| **Non ti rende anonimo** | La tua identità è verificata all’iscrizione e l’emittente la detiene |
| **Non nasconde la transazione alla tua banca** | La tua banca vede il trasferimento di fondi e la rete vede la transazione |
| **Non costruisce credito** | Non sono conti di credito e non avviene alcuna verifica creditizia |
| **È solo per gli USA** | Richiede cittadinanza o residenza legale negli USA e un conto bancario o creditizio USA |
| **Richiede verifica dell’identità** | I controlli Know Your Customer sono obbligatori per le norme antiriciclaggio |
| **Non copre tutti i commercianti** | Alcuni commercianti bloccano le carte prepagate e virtuali |

**Il punto sul blocco dei commercianti è importante nella pratica.** Alcuni servizi in abbonamento e compagnie aeree rifiutano le carte associate a carte virtuali o prepagate, e nessuna configurazione risolve il problema. Tieni una carta reale come riserva per questi casi.

*Il riassunto onesto: una carta virtuale è un controllo di contenimento per l’esposizione lato commerciante, non uno strumento di anonimato. Se ti serve anonimato, è un problema diverso con strumenti diversi.*

## Chi Emmette la Carta e Perché Conta

**Una carta virtuale è comunque una carta reale, emessa da una banca reale, sotto una licenza di circuito reale.**

| Dettaglio | Valore |
|---|---|
| **Banca emittente** | Patriot Bank, N.A., Membro FDIC |
| **Licenze circuito** | Mastercard e Visa |
| **Dove è accettata** | Ovunque siano accettate Mastercard e Visa |
| **Finanziamento** | Trasferito dal tuo conto corrente USA collegato |

**Ecco perché la protezione è autentica.** La carta gode delle stesse protezioni di circuito di qualsiasi altro prodotto Mastercard o Visa, il che significa che si applicano normalmente i diritti di chargeback e i processi di contestazione frodi. Non è una carta regalo o un credito a circuito chiuso.

Due certificazioni meritano di essere citate perché sono verificabili indipendentemente e non solo affermazioni di marketing:

- **Conformità PCI-DSS**, lo standard dell’industria delle carte di pagamento per la gestione dei dati del titolare della carta
- **SOC 2 Tipo II**, un rapporto auditato che copre i controlli di sicurezza su un periodo di tempo e non una semplice dichiarazione istantanea

**Sul modello di business:** l’azienda dichiara di guadagnare l’interchange dai commercianti e di non vendere dati dei clienti ad inserzionisti o terze parti. È lo stesso modello di ricavo di ogni altro emittente di carte, ed è importante capirlo senza considerarlo insolito.

*La ragione pratica per verificare la banca emittente è la conferma. Chiunque può dichiarare di gestire un programma carte, e il nome dell’emittente sulla carta è ciò che confermi rispetto alla banca indicata nei documenti.*

Controlla il circuito e la banca dal prefisso PAN usando il **[Magnetic Stripe Decoder](/magnetic-stripe-decoder/)**, che riporta l’intervallo del circuito principale e valida la cifra di controllo Luhn.

## Usare Bene le Carte Virtuali

**I controlli aiutano solo se li configuri.** Sei abitudini portano la maggior parte del beneficio.

1. **Blocca ogni carta a un commerciante** a meno che non ci sia un motivo per non farlo. Il blocco rende inutile un numero trapelato.
2. **Usa carte monouso per tutto ciò che è sconosciuto**, inclusi i periodi di prova e acquisti una tantum da siti minori.
3. **Imposta entrambi i limiti di spesa** sulle carte per abbonamenti, così un aumento di prezzo fallisce invece di addebitare.
4. **Nomina ogni carta con il nome del commerciante**, così la lista delle transazioni è leggibile e un addebito inatteso risalta.
5. **Metti in pausa invece di chiudere** quando prevedi di riprendere un servizio, e chiudi quando non lo farai.
6. **Tieni una carta reale per i commercianti che rifiutano le carte virtuali**, così un blocco al checkout non diventa un’emergenza.

> **Errore comune: considerare una carta virtuale un sostituto per controllare gli estratti conto.** Il blocco per commerciante previene una categoria di danni. Non rileva un conto compromesso in banca, un trasferimento non autorizzato o un addebito fraudolento sulla carta reale sottostante.

## Punti Chiave

- **Una carta virtuale cambia il numero che il commerciante memorizza.** Il tuo PAN reale non arriva mai a loro, che è il meccanismo principale.
- **Non rende la transazione privata.** La tua banca, la rete e l’emittente la vedono ancora, e la verifica dell’identità è obbligatoria.
- **Il blocco per commerciante è la funzionalità di maggior valore**, perché un numero trapelato fallisce ovunque altrove.
- **Il piano gratuito include i controlli di sicurezza.** I piani a pagamento aggiungono organizzazione e comodità, non protezione.
- **La banda magnetica memorizza i dati della carta in chiaro** ed è in fase di rimozione entro il 2033, con le banche USA che smetteranno di emettere nel 2027.
- **Il CVV non è sulla banda**, perciò uno skimmer che copia le tracce non ha ciò che molti commercianti online richiedono.
- **Alcuni commercianti rifiutano le carte virtuali.** Tieni una carta reale come riserva.
- **Verifica la banca emittente** invece di fidarti di una dichiarazione del programma carte, e controlla tu stesso il prefisso PAN.

## Passi Successivi

1. **Ispeziona i dati della traccia della tua carta** e verifica esattamente cosa contiene la banda magnetica: **[Decodificatore e Codificatore di Bande Magnetiche](/magnetic-stripe-decoder/)**
2. **Blocca il tuo credito** se non l'hai già fatto, è il controllo più efficace contro le frodi da nuovi account: **[Sicurezza Finanziaria Personale](/personal-security-course/personal-finance/)**
3. **Applica la disciplina di classificazione** per decidere quanto impegno dedicare a questa situazione: **[Lista di Controllo Prioritaria per la Sicurezza Personale](/articles/personal-security-checklist-prioritized-2026/)**
4. **Esamina i piani e i termini attuali di Privacy.com** prima di sottoscrivere: **[Privacy.com](https://www.privacy.com/virtual-card)**
5. **Verifica se i tuoi dati sono già comparsi in una violazione** prima di presumere di non essere stato coinvolto: **[Have I Been Pwned](https://haveibeenpwned.com)**
6. **Leggi la lista di controllo per la sicurezza dei pagamenti** per la controparte organizzativa: **[Lista di Controllo per la Risposta agli Incidenti](/checklists/incident-response-checklist/)**

## Riferimenti

1. [Privacy.com - cosa sono le carte virtuali, blocco per commerciante e limiti di spesa](https://www.privacy.com/virtual-card)
2. [Carta digitale - Wikipedia, copre carte digitali vs virtuali, tracce a banda magnetica, codici di servizio, parità e LRC](https://en.wikipedia.org/wiki/Digital_card)
3. [ISO/IEC 7813:2006 - carte di identificazione, carte per transazioni finanziarie, struttura dati delle tracce 1 e 2](https://webstore.iec.ch/en/publication/11605)
4. [ISO/IEC 7813 - layout dettagliato dei campi delle tracce, inclusi sentinelle e codici di servizio](https://en.wikipedia.org/wiki/ISO/IEC_7813)
5. [PCI Security Standards Council - requisiti per l'ambiente dati del titolare della carta](https://www.pcisecuritystandards.org/)
6. [Consumer Financial Protection Bureau - rapporti e punteggi di credito](https://www.consumerfinance.gov/consumer-tools/credit-reports-and-scores/)
7. [Codifica dati ANSI/ISO ALPHA, set di caratteri e tabella di parità della Traccia 1](http://www.hhhh.org/~joeboy/resources/magcards/trackdata_ANSI-ISO_ALPHA.html)
8. [Caratteri ISO per carte magnetiche, set della Traccia 1 e Traccia 2 a confronto](https://www.pos.swiftpos.com.au/Help-SP/MagneticCardSwipeISOCharacters.html)
9. [Lettura dei dati di carte magnetiche, guida pratica con scansione dal vivo di una carta](https://blog.j2i.net/2024/06/18/reading-magnetic-card-data/)
