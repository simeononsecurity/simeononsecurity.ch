---
title: "Abbiamo mappato 146.526 «telecamere Flock». 50.278 erano sistemi ClickShare"
date: 2026-09-21
lastmod: 2026-11-14
toc: true
draft: false
description: "Un audit di Flock Finder individua ClickShare e altri falsi positivi, spiega le prove e documenta le modifiche apportate."
genre: ["Ricerca sulla sicurezza", "Tecnologia della privacy", "Progetti open source", "Giornalismo dei dati", "Controsorveglianza"]
tags: ["Flock Finder", "Flock Safety", "ALPR", "Fingerprinting OUI", "WiGLE", "Falsi positivi", "Qualità dei dati", "Barco ClickShare", "Indirizzo MAC", "IEEE OUI", "Fingerprinting degli elementi informativi", "ESP32", "Flock-You", "NitekryDPaul", "DeFlockJoplin", "Responsabilità open source", "Mappatura della sorveglianza", "WiFi", "Probe request", "Randomizzazione MAC"]
cover: "/img/cover/flock-finder-oui-false-positive-audit-2026.webp"
coverAlt: "Una mappa urbana scura piena di segnaposto rossi che indicano dispositivi WiFi da ufficio, mentre pochi segnaposto verdi rappresentano rilevamenti più solidi"
coverCaption: "L’audit di 146.526 record di Flock Finder ha mostrato come un’utile osservazione sul campo sia diventata un’affermazione cartografica eccessivamente sicura."
canonical: "https://simeononsecurity.com/articles/flock-finder-oui-false-positive-audit-2026/"
---

**Abbiamo inserito 146.526 punti su una mappa delle telecamere di sorveglianza. Almeno 50.278 erano sistemi di presentazione Barco ClickShare. L’hardware delle sale conferenze rappresentava più di un terzo di ciò che il nostro titolo chiamava «telecamere mappate».**

Questo era il nostro progetto, la nostra pipeline di dati e il nostro errore. Flock Finder interrogava ogni giorno WiGLE per cercare prefissi MAC osservati sulle telecamere Flock Safety, pubblicava i risultati con coordinate di precisione completa e rappresentava tutti i dati con lo stesso segnaposto. I metadati contenevano la parola `suspected` e la documentazione menzionava i falsi positivi. La mappa e il titolo comunicavano comunque certezza.

**Risultato per il lettore:** riproduci l’audit, separa osservazione e attribuzione e mostra il livello di confidenza accanto al segnaposto e al titolo. Una corrispondenza di prefisso è un indizio da investigare, non la prova di una telecamera.

Quando abbiamo calcolato un istogramma di frequenza della colonna SSID, il dataset ha rivelato il problema in pochi minuti. ClickShare era soltanto la categoria più grande. Altri 6.099 record si chiamavano `SMARTGATE_*`, 3.801 iniziavano con il prefisso generico WiFi Direct `DIRECT-`, 314 avevano esattamente il nome `AndroidAP`, 138 indicavano `Audi HUD`, 133 `MAX-PRINTER`, e 30 contenevano la stringa di verdetto di un altro rilevatore. In totale, **60.793 righe, pari al 41,5%, corrispondevano alle regole note nell’audit originale per i nomi di altri dispositivi.**

Ora Flock Finder pubblica una classe di evidenza per ogni record, esclude per impostazione predefinita dalla mappa e dal titolo l’hardware noto come altro, espone filtri, segnala i record fuori dal mercato principale e distingue i prefissi ad alta confidenza da quelli dei produttori su contratto. Questo articolo documenta l’errore, le prove e i limiti ancora presenti.

______

## Come funziona il rilevamento ALPR della comunità

I rilevatori Flock sviluppati dalla comunità combinano in genere tre tipi di prove wireless:

1. **Prefissi WiFi MAC/OUI.** I primi byte di un indirizzo MAC amministrato globalmente possono identificare l’organizzazione che ha ricevuto il blocco di indirizzi.
2. **Comportamento WiFi.** Un SSID, una probe request wildcard, l’indirizzo del destinatario, il pattern dei canali o una sequenza di elementi informativi 802.11 possono restringere la classe del dispositivo.
3. **Prove Bluetooth.** Gli ID del produttore e gli UUID dei servizi possono identificare le radio esposte da un prodotto o da una generazione di firmware.

Il confronto OUI si è diffuso perché costa poco ed è passivo. Un ESP32 economico può esaminare i frame 802.11 vicini senza collegarsi a una rete. Un database storico come [WiGLE](https://wigle.net/) permette anche di cercare osservazioni precedenti senza installare scanner propri.

Il metodo segue una genealogia comunitaria: la mappatura e l’organizzazione locale di [DeFlock](https://deflock.org/), [colonelpanichacks/flock-you](https://github.com/colonelpanichacks/flock-you), fork e progetti complementari come il nostro [flock-you-esp32](https://github.com/simeononsecurity/flock-you-esp32), infine [Flock Finder](https://github.com/simeononsecurity/flock-finder), che ha applicato la lista dei prefissi ai dati WiGLE su scala globale.

Il lavoro sul campo originale merita un riconoscimento chiaro. [@NitekryDPaul](https://github.com/NitekryDPaul) ha osservato 30 prefissi su apparecchiature Flock reali tramite ricerca in modalità promiscua. [DeFlockJoplin](https://github.com/DeflockJoplin/flock-you) ne ha aggiunto un altro durante i test sul campo. Quelle osservazioni erano legittime. Il nostro errore a valle è stato trattare **«osservato su una telecamera Flock» come se significasse «esclusivo delle telecamere Flock».**

______

## Il difetto strutturale: un OUI descrive la catena di fornitura

IEEE definisce un OUI come un identificatore a 24 bit assegnato a un fornitore, produttore o altra organizzazione. Insieme ad altri 24 bit scelti dal destinatario, forma un indirizzo MAC. La [IEEE Registration Authority](https://standards.ieee.org/products-programs/regauth/) pubblica il registro.

Questo dice chi ha ricevuto un blocco di indirizzi. Non rivela necessariamente il marchio sul prodotto finito. I produttori su contratto costruiscono moduli radio per molti clienti. Lo stesso fornitore di chip può quindi comparire in telecamere, proiettori, stampanti, veicoli e schede per hobbisti.

Le assegnazioni nel registro dietro alla nostra lista rendevano evidente il rischio:

| Registrante | Prefissi nella lista sottoposta ad audit |
|---|---|
| Liteon Technology | `74:4C:A1`, `F4:6A:DD`, `9C:2F:9D`, `C0:35:32`, `E4:AA:EA`, `14:5A:FC` e altri |
| Universal Global Scientific Industrial (USI) | `E0:4F:43`, `08:3A:88` |
| Espressif | `A4:CF:12`, `3C:71:BF` |
| Silicon Laboratories | `58:8E:81`, `90:35:EA`, `EC:1B:BD` |
| Flock Safety | `B4:1E:52` |

Le voci Espressif avrebbero dovuto metterci in guardia. Due prefissi di una presunta lista di telecamere appartenevano al produttore di una delle piattaforme WiFi embedded più comuni al mondo, compresi i chip usati da molti rilevatori comunitari.

`B4:1E:52` è diverso perché è registrato direttamente a Flock Safety. Era stato aggiunto alla lista di 38 prefissi nel commit sottoposto ad audit, **ma non era ancora stato interrogato**: `scan_stats.json` indicava 31 prefissi interrogati. Lo stesso valeva per sei nuovi prefissi di batterie. Lo snapshot non prova quanto sia comune o raro il prefisso proprio di Flock. Non trasformeremo «non interrogato» in «zero risultati».

Il repository attuale contiene 39 prefissi dopo l’aggiunta di `E0:0A:F6` per allinearsi al firmware del rilevatore. Il riepilogo di scansione conservato riporta ancora dati per 31 prefissi. Le nuove voci attendono quindi un ricalcolo completo e non sono prefissi con zero risultati dimostrati.

______

## Il dataset ha verificato se stesso

Ogni cifra storica dell’audit riportata qui sotto è stata rigenerata da `data/flock_cameras.csv` nel commit Flock Finder [`5551829`](https://github.com/simeononsecurity/flock-finder/tree/5551829), usando `csv` e `collections.Counter` della libreria standard Python. Non serviva un nuovo test su strada. Nomi, geografia e composizione dei prefissi contraddicevano già il titolo. I dati sull’implementazione corretta provengono dal riepilogo `scan_stats.json` mantenuto nel repository attuale.

### La geografia era un segnale iniziale

Su 146.526 righe, 75.818 erano negli Stati Uniti, 70.674 fuori dagli Stati Uniti e 34 senza un valore di paese. La Germania aveva 13.491 record, seguita dal Canada con 6.251, dalla Francia con 5.839, dalla Gran Bretagna con 4.836, dai Paesi Bassi con 4.636 e dalla Svizzera con 4.515.

{{< figure src="flock-finder-us-non-us-split.webp" alt="Barra impilata con 75.818 record negli Stati Uniti, 70.674 fuori dagli Stati Uniti e 34 senza valore di paese" caption="L’istogramma dei paesi totalizza 146.492 perché 34 righe hanno un paese nullo." >}}

La geografia è un segnale di screening, non una prova. Flock descrive la propria rete come attiva «nationwide» e afferma di collegare clienti in [49 stati degli Stati Uniti](https://www.flocksafety.com/flock-ecosystem). L’espansione internazionale può modificare il confine del mercato. Segnaliamo quindi i record fuori mercato per la revisione, invece di eliminarli o dichiarare falsi tutti i record non statunitensi.

La conclusione prudente basta: quasi metà dei record si trovava fuori dal mercato statunitense principale del progetto. Senza un altro segnale, una corrispondenza OUI mondiale non poteva essere considerata altrettanto plausibile.

### Oltre 60.000 dispositivi si identificavano con il proprio nome

| Famiglia SSID nell’audit originale | Record | Quota | Indicazione del nome |
|---|---:|---:|---|
| Contiene `ClickShare` | 50.278 | 34,3% | Hardware di presentazione wireless Barco |
| `SMARTGATE_*` | 6.099 | 4,2% | Famiglia di gateway o dispositivi tipo OBD |
| `DIRECT-*` | 3.801 | 2,6% | Dispositivi WiFi Direct, come stampanti, TV e adattatori |
| Nome esatto `AndroidAP` | 314 | 0,2% | Hotspot Android |
| Nome esatto `Audi HUD` | 138 | 0,1% | WiFi per infotainment o head-up display Audi |
| Nome esatto `MAX-PRINTER` | 133 | 0,1% | Stampanti da ufficio |
| `Flock ALPR [...]` | 30 | <0,1% | Verdetto di un altro rilevatore salvato come SSID |
| **Totale dell’audit originale** | **60.793** | **41,5%** | Identificabili come altro hardware o output del rilevatore |

La documentazione di supporto Barco dice che il nome di rete predefinito di una base ClickShare è [`ClickShare-<serial base number>`](https://www.barco.com/en/support/knowledge-base/2675-how-to-connect-to-your-clickshare-base-unit-wifi). È una conferma diretta della famiglia di prodotti, senza supposizioni basate sulla geografia o sul registro dei fornitori.

Il classificatore di produzione ha poi sostituito i controlli sui nomi esatti con espressioni regolari senza distinzione tra maiuscole e minuscole. Comprende ClickShare, SmartGate, WiFi Direct, AndroidAP, Audi HUD, MAX-PRINTER ed etichette di output dei rilevatori. Sulle stesse 146.526 righe trova 629 varianti AndroidAP, 139 Audi HUD e 134 MAX-PRINTER. Il repository attuale riporta quindi **61.110 record `identified_other`**, leggermente più dei 60.793 dell’audit originale.

### Il segnale di conferma era solo il 2,4%

Solo **3.502 righe** avevano un SSID autentico con pattern Flock. Altre 24.964 non avevano un SSID. I restanti record indicavano altro hardware oppure un OUI abbinato a un nome non classificato.

Le 3.502 righe confermate contenevano 161 varianti SSID autentiche: 3.342 occorrenze del semplice nome `Flock`, 157 nomi di provisioning univoci `Flock-XXXXXX` o `FLOCK-XXXXXX` e altri tre nomi contenenti `flock`. Un precedente conteggio README di 166 varianti includeva cinque stringhe distinte di annotazione del rilevatore `Flock ALPR [...]`. Quelle cinque sono prove del rilevatore, non della telecamera.

{{< figure src="flock-finder-evidence-class-breakdown.webp" alt="Barra impilata al 100% che divide 146.526 record in 3.502 confermati da SSID, 57.267 con nome non classificato, 24.964 solo OUI nascosto, 60.763 identificati come altri e 30 record di feedback del rilevatore" caption="Il vecchio titolo riduceva cinque classi di evidenza sostanzialmente diverse a un solo conteggio." >}}

### La qualità dei prefissi variava molto

Il tasso di falsi positivi non era uniforme. Alcuni prefissi mantenevano un segnale Flock utile. Altri erano dominati da dispositivi da ufficio o di consumo con nome.

{{< figure src="flock-finder-per-oui-composition.webp" alt="Barre orizzontali impilate per 31 prefissi OUI: SSID Flock verdi, SSID noti di altri dispositivi rossi, SSID nascosti grigio chiaro e record non classificati grigio scuro" caption="I prefissi più grandi spesso contenevano più dispositivi noti come altri. Conteggi dallo snapshot di audit di 146.526 righe." >}}

Considera due prefissi che la vecchia mappa etichettava allo stesso modo:

- `70:C9:4E` aveva 495 righe: 133 nomi con pattern Flock e 29 nomi noti di altri dispositivi.
- `74:4C:A1` aveva 11.872 righe: 211 nomi con pattern Flock e 8.385 nomi noti di altri dispositivi.

{{< figure src="flock-finder-prefix-signal-contrast.webp" alt="Confronto del prefisso 70 C9 4E con il 26,9% di SSID Flock e il 5,9% di noti altri, rispetto a 74 4C A1 con l’1,8% di SSID Flock e il 70,6% di noti altri" caption="Un’unica etichetta nascondeva rapporti segnale-rumore opposti." >}}

Lo stesso schema emerge nei gruppi maggiori: `F4:6A:DD` aveva 8.422 nomi noti di altri dispositivi contro 327 nomi Flock, `D0:39:57` ne aveva 8.270 contro 473, `E0:4F:43` comprendeva 6.238 nomi noti di altri contro 66 nomi Flock. Il volume del prefisso non provava la qualità delle evidenze.

______

## Il ciclo di feedback nascosto in 30 righe

Trenta record in Texas avevano SSID che erano chiaramente l’output di un altro rilevatore:

| Etichetta del rilevatore salvata come SSID | Confidenza indicata dallo strumento | Record |
|---|---:|---:|
| `Flock ALPR [wifi_receiver_oui;low]` | bassa | 20 |
| `Flock ALPR [wifi_oui_wildcard_probe;medium]` | media | 4 |
| `Flock ALPR [wifi_bssid_oui;low]` | bassa | 3 |
| `Flock ALPR [flock_receiver_oui;low]` | bassa | 2 |
| `Flock ALPR [wifi_hidden_ssid_oui;low]` | bassa | 1 |

Lo strumento che li ha creati indicava bassa confidenza per 26 record su 30. Un caricamento su WiGLE ha poi salvato il verdetto dello strumento nel campo SSID. La nostra pipeline ha trovato la parola `Flock` e avrebbe potuto considerare l’etichetta una conferma indipendente.

Trenta righe sono poche dal punto di vista statistico. Il meccanismo è importante: gli strumenti che condividono un database collaborativo possono acquisire l’output degli altri e trasformare una supposizione poco affidabile in una corroborazione apparente. La correzione esclude l’intero pattern `Flock ALPR [` prima di cercare la sottostringa di conferma `flock`.

______

## Dove abbiamo sbagliato

Il titolo README diceva **«Telecamere mappate | 146.526»**. La mappa pubblicava coordinate a precisione completa e mostrava ogni risultato con lo stesso segnaposto. Si aggiornava secondo una pianificazione GitHub Actions, facendo apparire un’euristica debole come un inventario mantenuto.

Avevamo incluso delle riserve. Ogni elemento riportava `match_confidence: "suspected"`. Il README citava ClickShare come possibile dispositivo presente insieme alla telecamera e il progetto teneva una traccia separata dei candidati trovati tramite SSID. Queste riserve non governavano il conteggio, il segnaposto o la vista predefinita vista dai lettori.

Nel testo eravamo cauti, nel titolo quantificavamo. La mappa faceva l’affermazione.

La parte più evitabile è che il firmware di [flock-you-esp32](https://github.com/simeononsecurity/flock-you-esp32) separava già gli identificatori ad alta confidenza da quelli dei produttori su contratto e valutava le prove deboli sotto la soglia di allarme. Il concetto esisteva nella stessa organizzazione, ma la pipeline di mappatura non lo aveva ereditato.

Abbiamo individuato la portata dell’errore creando un istogramma della nostra colonna SSID. Ci sono voluti pochi minuti. Ogni giorno pubblicavamo 146.526 righe di prove contro la nostra presentazione.

______

## Cosa abbiamo cambiato

La correzione è implementata nel modello dati e nell’interfaccia di Flock Finder:

- **Evidenza per record:** `ssid_confirmed`, `oui_high`, `oui_mfr` o `identified_other`.
- **Livelli OUI:** i prefissi sono distinti in alta confidenza osservata sul campo e livelli condivisi dei produttori su contratto.
- **Esclusione dell’hardware noto come altro:** ClickShare, SmartGate, WiFi Direct, hotspot Android, Audi HUD, MAX-PRINTER e SSID prodotti da rilevatori sono esclusi per impostazione predefinita da mappa e titolo.
- **Incertezza visibile:** colori dei segnaposto, popup, conteggi e filtri mostrano la classe di evidenza.
- **Segnalazione del mercato:** i record fuori dal mercato statunitense principale hanno `out_of_market: true` e restano disponibili per la revisione.
- **Titolo suddiviso:** 3.502 confermati da SSID, 73.691 sospetti da OUI di fascia alta, 8.223 sospetti da OUI di produttori su contratto e 61.110 identificati come altri.

Il conteggio corretto utile all’azione è **85.416**, e include ancora 81.914 corrispondenze OUI non confermate. È una contabilità difendibile dei record che superano le regole attuali, non un inventario verificato di telecamere.

Anche `identified_other` è un classificatore operativo, non un oracolo. ClickShare dispone di solide prove documentali dirette sul suo SSID predefinito, mentre un pattern ampio come `DIRECT-` descrive una convenzione di denominazione WiFi Direct usata da molte categorie di prodotti. Pubblicare la regola di corrispondenza e il campo `blocked_reason` permette ai ricercatori di controllare le esclusioni e aggiornarle quando migliorano le prove.

### La risposta a lungo termine è il fingerprinting del firmware

La classificazione OUI limita i danni, ma non rende specifico per un prodotto un prefisso di produttore condiviso. La strada più solida è la struttura ordinata degli elementi informativi delle probe request 802.11. Il lavoro a monte documenta questa firma TLV:

```text
2,12,127,221:506f9a16030103,45,191,221:0050f208000000
```

La sequenza descrive il comportamento di uno stack firmware specifico, non il proprietario di un blocco MAC. Il fingerprinting delle probe request è una tecnica consolidata di identificazione dei dispositivi. [La ricerca pubblicata sul fingerprinting MAC 802.11](https://doi.org/10.1155/2017/6235484) mostra che gli elementi informativi delle probe request possono restare identificativi anche quando gli indirizzi MAC ruotano. Affronta inoltre il problema specifico segnalato in [flock-you issue #43](https://github.com/colonelpanichacks/flock-you/issues/43): `Flock Camera net.` compare su indirizzi MAC a gestione locale sequenziali nelle bande 2,4 e 5 GHz.

La firma richiede ancora una validazione indipendente sul campo con hardware e versioni firmware diverse, e i frame malformati richiedono parsing difensivo. Resta comunque la direzione giusta. La randomizzazione MAC rende il solo confronto OUI una strada destinata a fallire.

______

## Perché conta oltre un singolo repository

Le persone usano mappe di sorveglianza per decidere dove guidare, parcheggiare, segnalare, fare ricerca e organizzarsi. Un segnaposto falso sposta l’attenzione. Decine di migliaia possono screditare le osservazioni accurate vicine.

Esiste anche un’asimmetria di credibilità. A un fornitore o a un critico basta un segnaposto ClickShare dimostrabilmente falso per mettere in dubbio l’intero dataset. Noi ne abbiamo forniti 50.278. Giornalisti e gruppi di advocacy possono ripetere un titolo netto più velocemente di quanto arrivi una correzione successiva.

Il lavoro di trasparenza open source si guadagna fiducia con metodi ispezionabili e incertezza visibile. Pubblicare i dati grezzi ha aiutato a scoprire l’errore, ma l’accesso ai dati non giustifica un’interfaccia che esagera le conclusioni. La correzione deve comparire ovunque il lettore incontra l’affermazione: campo, filtro, segnaposto, legenda e titolo.

### Un invito a tutte le mappe Flock e ALPR

Anche gli altri progetti di mappatura Flock e ALPR dovrebbero controllare i propri dataset. È un invito a confrontare i metodi, non un’accusa che ogni mappa abbia ereditato il nostro errore.

[WiGLE](https://www.wigle.net/stats/) è il più ampio dataset pubblico di osservazioni WiFi con ricerca globale che conosciamo. Questa portata rendeva Flock Finder interessante: una API poteva trasformare una lista di firme ricercate sul campo in una mappa mondiale. Ha anche reso l’errore abbastanza grande da misurare. Un database globale restituisce tutti i prodotti estranei che condividono lo spazio di indirizzi di un fornitore radio, non solo il prodotto che ha motivato la ricerca.

Altre mappe usano prove diverse. Alcune si basano su foto e osservazioni volontarie sul campo. Altre importano tag di sorveglianza OpenStreetMap, registri pubblici, dichiarazioni dei fornitori o dati di un altro progetto comunitario. I loro totali non sono direttamente confrontabili con i nostri risultati WiGLE e il nostro 2,4% di conferme SSID non va applicato a dataset verificati sul campo. Il rischio comune è che la classificazione di un progetto entri nei dati sorgente di un altro e sembri una conferma indipendente.

Ogni mappa pubblica dovrebbe saper rispondere a un breve audit:

1. **Che cosa significa un segnaposto?** Un dispositivo fotografato, un documento pubblico, una corrispondenza OUI, una segnalazione utente o un’importazione da un’altra mappa?
2. **Quanti record hanno prove dirette sul prodotto?** Pubblica i conteggi per classe di evidenza invece di un solo totale di telecamere.
3. **Quali fonti sono indipendenti?** Traccia la provenienza delle importazioni per non contare la stessa osservazione come più conferme.
4. **Che cosa contraddice la classificazione?** Calcola le frequenze di SSID, fornitori, paesi, etichette dei collaboratori e altri campi categorici.
5. **Come vengono mostrate incertezza e contestazioni?** Mostra confidenza e stato delle correzioni in segnaposti, filtri, esportazioni e titoli.
6. **Un altro ricercatore può riprodurre il conteggio?** Pubblica query, snapshot della fonte, regole di classificazione e data.

Questo audit non ridimensiona il problema Flock. Una rete di telecamere ALPR può ancora registrare gli spostamenti, consentire ricerche tra giurisdizioni e colpire persone che non hanno mai acconsentito alla raccolta. Conteggi accurati rendono più difficile respingere la critica. Se contestiamo i sistemi di sorveglianza, le nostre mappe devono distinguere ciò che abbiamo osservato, dedotto e confermato.

Abbiamo commesso un errore ben informato. I prefissi provenivano da ricerche sul campo legittime, la pipeline era riproducibile e le riserve erano reali. L’inferenza superava comunque le prove. Buone intenzioni e buoni dati in ingresso non eliminano l’obbligo di verificare i risultati di un sistema su larga scala.

______

## Riprodurre l’audit

Recupera il commit `5551829`, poi esegui quanto segue dalla radice del repository. Usa solo la libreria standard Python e stampa totale, geografia, SSID comuni e alcune famiglie di dispositivi denominate.

```bash
git clone https://github.com/simeononsecurity/flock-finder.git
cd flock-finder
git checkout 5551829

python3 - <<'PY'
import csv
from collections import Counter

with open("data/flock_cameras.csv", newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

ssids = Counter((row["ssid"] or "").strip() for row in rows)
countries = Counter((row["country"] or "").strip() for row in rows)

families = {
    "clickshare": lambda s: "clickshare" in s.lower(),
    "smartgate": lambda s: s.lower().startswith("smartgate_"),
    "direct": lambda s: s.lower().startswith("direct-"),
    "androidap": lambda s: s.lower().startswith("androidap"),
    "detector_output": lambda s: s.lower().startswith("flock alpr ["),
}

print("righe", len(rows))
print("USA", countries["US"])
print("fuori dagli Stati Uniti", sum(countries.values()) - countries["US"] - countries[""])
print("paese mancante", countries[""])
print("SSID più frequenti", ssids.most_common(20))
for name, matches in families.items():
    print(name, sum(matches(ssid) for ssid in ssids.elements()))
PY
```

Per l’input storico esatto, usa il CSV di quel commit e non un dataset generato attuale. Dopo l’audit il progetto ha smesso di includere in Git il CSV grande, il GeoJSON e i file per OUI, perché ogni scansione riscriveva centinaia di megabyte e aveva fatto crescere molto il repository. I dati generati attuali sono ripristinati e pubblicati nella release continua [`data-latest`](https://github.com/simeononsecurity/flock-finder/releases/tag/data-latest). Il piccolo riepilogo `scan_stats.json` resta in Git. L’assenza di un file generato nel branch attuale quindi non significa che le prove storiche siano state eliminate o che il loro conteggio sia zero.

______

## La lezione

**Un’euristica indicata come «sospetta» nei metadati ma resa come segnaposto certo sulla mappa è un’affermazione.** L’etichetta deve stare nel modello dati e nella visualizzazione, non solo nella documentazione.

