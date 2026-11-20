---
title: "Minare Pearl (PRL) nel 2026: configurazione, redditività e utilità della blockchain"
date: 2026-09-22
lastmod: 2026-11-19
toc: true
draft: false
description: "Configura il mining di Pearl PRL con SRBMiner, esamina la prova di lavoro utile, stima i margini e valuta l’utilità pratica della blockchain."
genre: ["Criptovalute", "Mining GPU", "Calcolo IA", "DePIN", "Catene di blocchi", "Linux", "Laboratorio domestico", "Componenti"]
tags: ["mining di Pearl", "mining di PRL", "Pearl PRL", "prova di lavoro utile", "PoUW", "NoisyGEMM", "SRBMiner Pearlhash", "pool di mining Pearl", "LuckyPool Pearl", "mining GPU 2026", "crypto e calcolo IA", "Pearl Research Labs", "mining combinato Nockchain", "mining combinato Nock", "mining RTX 3070", "configurare SRBMiner", "rig di mining Linux", "servizio di mining systemd", "mining con moltiplicazione di matrici", "miner vLLM", "wallet Pearl", "indirizzo prl1", "redditività del mining", "mining di calcolo IA", "guida al mining crypto", "mining NVIDIA", "impostazioni di overclock per il mining"]
cover: "/img/cover/pearl-blockchain-gpu-mining-matrix-multiplication-2026.webp"
coverAlt: "Illustrazione di un moderno rig di mining GPU che esegue moltiplicazioni di matrici per la blockchain Pearl, con flussi di dati dinamici e colori vivaci su uno sfondo scuro."
coverCaption: ""
ref: ["/other/efficient-spacemesh-mining-multiple-gpus-guide", "/articles/local-ai-2026-build-your-rig-now"]
---

**Pearl è la prima blockchain con prova di lavoro utile ad aver raggiunto una vera scala produttiva e premia i miner per le moltiplicazioni di matrici invece che per l’hashing.** La mainnet è stata avviata il **27 aprile 2026** e in poche settimane la promessa di proteggere una blockchain producendo calcolo per l’IA nello stesso passaggio ha scatenato una corsa al mining GPU.

*L’affermazione è tecnicamente reale, ma la sua validità economica non è dimostrata. La distanza tra queste due cose è tutta la storia.*

Questa guida spiega come minare PRL, quali calcoli esegue il miner, perché i margini si sono ridotti così rapidamente dopo il lancio e se la blockchain produce valore.

**Al termine avrai:** un wallet, un miner verificato, un consumo energetico misurato e un calcolo della redditività basato sulla tua tariffa. Considera le stime dei pool e i ricavi iniziali come osservazioni riferite a una data, non come garanzia d’acquisto.

## La risposta breve

**Pearl è un autentico risultato tecnico, ma deve affrontare il problema economico del mining che riguarda ogni nuova moneta.**

| Domanda | Risposta breve |
|---|---|
| **Che cos’è?** | Una blockchain L1 derivata da Bitcoin e protetta dalla prova di lavoro utile. I miner eseguono moltiplicazioni di matrici rumorose invece di SHA-256 |
| **Come si mina?** | SRBMiner-MULTI con `--algorithm pearlhash` su un pool, oppure il miner vLLM di Pearl sul proprio nodo |
| **Perché era redditizia?** | Per alcune settimane le emissioni iniziali hanno superato la difficoltà, poi la difficoltà le ha raggiunte |
| **È ancora redditizia?** | Dipende dall’hardware e la finestra si restringe. Consulta la sezione sui margini |
| **La blockchain è utile?** | **Il meccanismo sì, il mercato non ancora.** Dettagli nel verdetto |

**La cosa più importante da sapere prima di costruire un rig:** le note di rilascio 3.6.8 dello stesso sviluppatore del miner dicono che un aggiornamento di Pearl renderà le GPU consumer «praticamente inutili» per il mining. Non è la critica di un osservatore esterno. Lo dice chi sviluppa il miner.

## Che cos’è Pearl

Pearl è una blockchain L1 sviluppata da **Pearl Research Labs**. Il suo repository la descrive così:

> "Pearl è una blockchain L1 basata sul protocollo Proof of Useful Work, in cui il mining è un sottoprodotto di moltiplicazioni arbitrarie di matrici."

Il repository include un nodo completo, un wallet daemon, un client leggero SPV, un sistema di prove a conoscenza zero e un miner GPU. Usa la **licenza ISC**, una licenza permissiva. L’infrastruttura deriva da progetti Bitcoin collaudati: **btcd** per il nodo, **btcwallet** per il wallet e **neutrino** per il client leggero.

**Il design riprende volutamente elementi di Bitcoin**, fino a un’offerta massima di **2,1 miliardi di PRL**, esattamente cento volte i 21 milioni di Bitcoin, con ricompense di blocco in calo e blocchi di circa due minuti.

*L’infrastruttura è volutamente conservativa. La novità riguarda interamente la funzione di lavoro.*

### Cos’è la prova di lavoro utile

La prova di lavoro utile è un’idea vecchia con una storia deludente. La proposta è sempre stata sostituire l’hashing deliberatamente dispendioso di Bitcoin con calcoli che producano anche qualcosa di valore. Quasi tutti i tentativi precedenti sono falliti per lo stesso motivo: il lavoro «utile» non era utile oppure non si poteva verificare a basso costo per proteggere una blockchain.

Pearl la implementa con una routine chiamata **NoisyGEMM**. In pratica, un miner esegue moltiplicazioni di matrici rumorose su una GPU, crea un commitment tramite hash e racchiude il lavoro in una **prova a conoscenza zero**, così la blockchain può verificarlo a basso costo.

Il metodo si basa su un articolo di crittografia del 2025, **"Proofs of Useful Work from Arbitrary Matrix Multiplication"**, di Komargodski, Schen e Weinstein. L’articolo dichiara un sovraccarico di circa **1 + o(1) rispetto a una moltiplicazione matriciale ingenua**. È l’affermazione portante del progetto. Se proteggere la blockchain costa quasi nulla oltre al calcolo sottostante, produrre quel calcolo è quasi gratis.

**La promessa è doppia: un passaggio GPU, due risultati.**

È questa affermazione a distinguere Pearl da un decennio di concetti PoUW falliti. La maggior parte non aveva un limite del genere.

{{< figure src="pearl-noisygemm-proof-of-useful-work-flow.webp" alt="Diagramma che mostra come la prova di lavoro utile di Pearl trasforma una moltiplicazione di matrici su GPU in un commitment hash e una prova a conoscenza zero verificabili a basso costo dalla blockchain" >}}

### Quali calcoli esegue il programma

Esistono due metodi e non sono equivalenti.

**Il metodo ufficiale** si trova nel repository Pearl. Comprende due componenti: `pearl-gateway`, che collega al nodo, e `vllm-miner`, che esegue il calcolo GPU tramite vLLM. Il gateway comunica in JSON-RPC con un nodo `pearld` locale e offre un’interfaccia di mining su socket Unix o sulla porta TCP 8337.

**Il metodo con pool** è quello più usato. SRBMiner-MULTI implementa l’algoritmo Pearl `pearlhash` e lo configuri per collegarlo a un pool.

La differenza conta per valutare l’utilità. **Il miner ufficiale carica un vero modello linguistico.** L’esempio della documentazione Pearl esegue `pearl-ai/Llama-3.3-70B-Instruct-pearl` in Docker con accesso alla GPU. Il modello da 70 miliardi di parametri esegue inferenza mentre lo stesso passaggio protegge la blockchain.

*Produrre inferenza è una capacità reale. Produrre inferenza che nessuno compra è un centro di costo con una blockchain collegata. Tieni distinte queste due idee.*

## Perché era redditizia e perché è cambiato tutto

La redditività iniziale di Pearl non era un mistero e non dipendeva dall’IA. Era la normale curva di emissione di una nuova moneta.

| Quando | Che cosa è successo |
|---|---|
| **27 aprile 2026** | Avvio della mainnet |
| **Fine maggio 2026** | Inizia la corsa al mining GPU, cinque settimane dopo l’avvio della blockchain |
| **Giugno 2026** | I ricavi giornalieri stimati di una RTX 5090 **si dimezzano circa** con l’aumento della difficoltà |
| **Da metà a fine 2026** | L’efficienza del software miner migliora rapidamente e compensa in parte il calo |

Il meccanismo di compressione è semplice:

1. **All’inizio le emissioni sono alte e la difficoltà è bassa.** I primi miner ricevono ricompense sproporzionate per unità di hashrate.
2. **Le ricompense attirano hashrate.** Altre GPU si collegano alla blockchain.
3. **La difficoltà sale per adeguarsi.** La ricompensa per GPU diminuisce.

Pearl aggiunge un’altra pressione al ribasso perché la ricompensa di blocco cala per progetto. **I ricavi hanno due motivi per scendere e la difficoltà uno per salire.**

### La forza compensativa: l’efficienza dei programmi

I margini non sono crollati in modo uniforme, perché i miner sono diventati più veloci. Il registro delle modifiche pearlhash di SRBMiner mostra i progressi:

| Versione | Modifica a Pearlhash |
|---|---|
| **3.6.1** | Aggiunto il supporto B300. Per B300 SXM6 con `--gpu-cclock 1600` sono stati riportati circa **706 TH/s a 920 W** |
| **3.6.2** | Miglioramenti per H100, H200 e serie 4000 |
| **3.6.8** | Miglioramento dell’hashrate, soprattutto sulla serie 3000 |
| **3.6.9** | **Grandi miglioramenti di efficienza.** Hashrate uguale o superiore con molta meno potenza sulla maggior parte delle architetture |

**Per chi mina a casa, l’elettricità è il costo operativo dominante.** Un rilascio che mantiene l’hashrate riducendo i consumi migliora direttamente il margine, senza variazioni del prezzo del token o della difficoltà di rete. Per questo un rig marginale a giugno può sembrare ragionevole a settembre con lo stesso hardware.

*I guadagni di efficienza aiutano davvero, ma solo temporaneamente, perché anche tutti gli altri li sfruttano e aumentano la difficoltà.*

## Il soft fork con penalità per il rango

Nella notte del **6 agosto 2026**, su Pearl si è attivato un soft fork verso le **02:00 UTC, blocco 96251**. Molti miner lo hanno scoperto la mattina seguente, quando il loro hashrate è sceso.

Il protocollo Pearl ha un parametro **noise rank**. Un rango più alto rendeva più facile vincere un jackpot con la stessa quantità di lavoro. **Alcuni miner sceglievano intenzionalmente ranghi elevati e ottenevano hashrate effettivo e ricompense sproporzionati.** Il team ha esaminato quelle che definiva ottimizzazioni anomale e introdotto una penalità.

| Modifica della regola | Effetto |
|---|---|
| **Rango minimo consentito** | 128 |
| **Limite del jackpot** | Ora calcolato con la formula `128 / rank` |
| **Vantaggio dei ranghi elevati** | Eliminato del tutto |

**Impatto sui miner:**

- Minare sopra il rango 128 è costato agli operatori **dal 50% all’87,5% dell’hashrate effettivo**
- Minare al rango 128 o inferiore è costato quasi nulla

Chi inizia ora deve tenere presenti due lezioni.

**L’hashrate dipende dal software e dalle regole di rete, non solo dalla GPU.** Una configurazione che a luglio sembrava efficace non misurava ciò che l’operatore credeva.

**Aggiorna il miner quando cambia la rete.** Le versioni vecchie perdono molta efficienza o smettono di funzionare correttamente con le nuove regole. Prima del fork sono stati aggiornati i software dei pool, tra cui PearlFortune v2.1.0 e Krig (Kryptex) v1.1.0, insieme a miner come Tw-pearl-miner v3.3.0 e Wildrig 0.49.8.

*Un soft fork che taglia una ricompensa fino all’87,5% dimostra chiaramente perché devi seguire gli annunci del progetto, non soltanto una dashboard dei pagamenti.*

## Due modi per minare Pearl

| | Mining su pool | Miner ufficiale vLLM |
|---|---|---|
| **Software** | SRBMiner-MULTI | `pearl-gateway` e `vllm-miner` |
| **Algoritmo** | `pearlhash` | NoisyGEMM tramite vLLM |
| **Serve un nodo** | No | **Sì, un `pearld` sincronizzato** |
| **Pagamento** | Pool, PPLNS o solo | Direttamente al tuo indirizzo di mining |
| **Esegue un modello reale** | No | **Sì, ad esempio Llama-3.3-70B-Instruct** |
| **Impegno di configurazione** | Basso | Alto, servono CUDA Toolkit e Python 3.12 |
| **Ideale per** | Portare rapidamente hashrate sulla rete | Fornire direttamente potenza di calcolo alla rete |

**Inizia con il mining su pool.** Non servono nodo, sincronizzazione o download di modelli e ottieni hashrate e un indirizzo di pagamento in pochi minuti. Passa al miner ufficiale solo se vuoi fornire inferenza o gestire un nodo.

{{< figure src="pearl-mining-pool-vs-vllm-miner-comparison.webp" alt="Confronto tra mining Pearl su pool con SRBMiner e miner ufficiale vLLM, con i componenti di nodo, gateway e inferenza richiesti da ciascun metodo" >}}

## Schede video per l’uso domestico

Pearl è notevole per ciò che non richiede. Hashrate Index definisce l’hardware necessario **insolitamente leggero: poca RAM, poco spazio e poca CPU, senza la costosa rete multifibra richiesta da un vero cluster di addestramento.** Un analista l’ha descritta come «un ottimo modo per usare apparecchiature esistenti».

Questo è il suo richiamo concreto. **Le GPU che possiedi già, anche quelle vecchie, producono qualcosa.**

| Classe GPU | Osservazione |
|---|---|
| **RTX 5090 e 4090** | Ricavi più alti per scheda. È in queste fasce che è stato misurato il dimezzamento iniziale dei ricavi |
| **Serie RTX 3000** | Il miglioramento hashrate della versione 3.6.8 era rivolto soprattutto a questa serie. Resta valida, ma l’efficienza conta più della velocità grezza |
| **Acceleratori per data center** | H100, H200 e B300 sono stati aggiunti e migliorati nel 2026. La corsa all’hashrate si dirige qui |
| **Schede vecchie o con poca VRAM** | Marginali. Consulta un calcolatore di redditività aggiornato prima di costruire qualsiasi cosa |

**Ogni rilascio del 2026 segue lo stesso schema.** Prima sono stati aggiunti e migliorati gli acceleratori di punta, perché lì l’hashrate vale di più. Le schede consumer hanno ricevuto attenzione quando la serie 3000 aveva margine per recuperare.

*La messa a punto dell’efficienza produce più ricavi della corsa alle frequenze. È l’opposto di ciò che insegnano molte guide di mining.*

## Configurazione su Linux

Il metodo con pool richiede quattro cose: il binario SRBMiner, un indirizzo wallet Pearl, un endpoint del pool e un servizio che lo mantenga in esecuzione.

### Crea prima un indirizzo del portafoglio

Gli indirizzi di mining Pearl iniziano con **`prl1`**. Il wallet ufficiale è **Oyster**, il daemon HD nel repository Pearl, con interfacce JSON-RPC e gRPC. Genera da lì un indirizzo di mining **Taproot**.

Non saltare questo passaggio e non riutilizzare un indirizzo di un’altra blockchain. **Le ricompense inviate a un indirizzo che non controlli sono perse.**

### Pool, porte e mining combinato

Il pool Pearl più grande è LuckyPool, che offre porte suddivise in base all’hashrate previsto:

| Porta | Difficoltà iniziale | Hashrate consigliato |
|---|---|---|
| **3360** | 2M | Meno di 500 TH/s |
| **3361** | 4M | Da 500 a 1000 TH/s |
| **3362** | 8M | Oltre 1000 TH/s |

Scegli la porta adatta all’hashrate effettivo del tuo rig. **Una sola GPU consumer deve usare la 3360.** Un rig piccolo su una porta ad alta difficoltà aspetta a lungo tra una share e l’altra e aumenta la varianza senza alcun vantaggio.

Due funzioni dei pool meritano attenzione:

- **Il mining solo** funziona su qualsiasi porta se anteponi `solo:` all’indirizzo del wallet. Se trovi un blocco, tieni l’intera ricompensa; altrimenti non ricevi nulla. Con l’hashrate di una GPU consumer, l’attesa è lunga.
- **Il mining combinato con Nockchain** genera NOCK oltre a PRL con lo stesso hashrate. Aggiungi `+NOCK_ADDRESS` al wallet Pearl. Il pool paga NOCK direttamente su Nockchain, quindi non può riceverlo un indirizzo di token wrapped che inizia con `0x`. **Il tuo miner deve supportare il mining combinato. Senza questa funzione continuerà a minare Pearl normalmente.**

Il pool pubblica host `luckypool.io` e host di instradamento `lproute.com`. Se la rete blocca il traffico di mining diretto, mantieni la porta e cambia dominio.

## Una procedura di installazione funzionante

Lo script seguente configura SRBMiner come servizio systemd su Debian o Ubuntu. Rileva ogni GPU, applica le opzioni di overclock per scheda, verifica il download con l’MD5 pubblicato, crea l’unità e una regola logrotate, quindi riavvia il servizio.

```bash
#!/usr/bin/env bash
# install-pearl-miner.sh -- configura SRBMiner (Pearl / PRL) come servizio systemd.
# Esegui: sudo bash install-pearl-miner.sh
set -euo pipefail

ALGO="pearlhash"
POOL="${POOL:-pearl-us-east.luckypool.io:3360}"
WALLET="${WALLET:-<YOUR_PR1_ADDRESS>}"   # prl1... aggiungi +NOCK_ADDRESS per il mining combinato
WORKER="${WORKER:-rig-1}"
SRB_VERSION="${SRB_VERSION:-3.6.9}"
MINER_DIR="/opt/srbminer"
UNIT="/etc/systemd/system/pearl-miner.service"
SVC="pearl-miner.service"
LOG="/var/log/pearl-miner.log"

# Regolazione per RTX 3070. MCORE blocca il clock della memoria a un valore assoluto, molto inferiore al
# valore originale della scheda di 7001 MHz. È un underclock volontario per migliorare l’efficienza, non
# un overclock delle prestazioni. Imposta il valore su "" per disattivare l’opzione.
CCLOCK="${CCLOCK:-1560}"
MCLOCK="${MCLOCK:-5001}"
COFFSET="${COFFSET:-150}"
PLIMIT="${PLIMIT:-180}"
FAN="${FAN:-}"
THERMAL="${THERMAL:-88}"
```

Il blocco di regolazione merita una spiegazione, perché a prima vista sembra errato. **`MCORE=5001` è inferiore al clock di memoria originale di una 3070.** È intenzionale. Pearl premia l’efficienza della memoria e ridurne il clock abbassa i consumi più dell’hashrate. **Non copiare i valori di overclock da una riga di un database hashrate senza controllare quale GPU è stata usata nel test.** Spesso il benchmark riguarda una scheda diversa dalla tua.

```bash
[ "$(id -u)" -eq 0 ] || { echo "esegui come root (sudo)"; exit 1; }
command -v nvidia-smi >/dev/null || { echo "nvidia-smi non trovato: installa prima il driver"; exit 1; }

GPU_N=$(nvidia-smi --query-gpu=index --format=csv,noheader | wc -l)
echo "== GPU NVIDIA rilevate: $GPU_N =="
nvidia-smi --query-gpu=index,name,memory.total,power.limit --format=csv,noheader

# Crea un insieme di opzioni di overclock per ogni GPU rilevata
OC=""
for i in $(seq 0 $((GPU_N - 1))); do
    [ -n "$COFFSET" ] && OC="$OC --gpu-coffset$i $COFFSET"
    [ -n "$CCLOCK" ]  && OC="$OC --gpu-cclock$i $CCLOCK"
    [ -n "$MCLOCK" ]  && OC="$OC --gpu-mclock$i $MCLOCK"
    [ -n "$PLIMIT" ]  && OC="$OC --gpu-plimit$i $PLIMIT"
    [ -n "$FAN" ]     && OC="$OC --gpu-fan$i $FAN"
done
THERMAL_ARG=""
[ -n "$THERMAL" ] && THERMAL_ARG=" --shutdown-temperature $THERMAL"

# Scarica e verifica il rilascio
STEM="SRBMiner-Multi-$(echo "$SRB_VERSION" | tr . -)-Linux"
BASE="https://github.com/doktor83/SRBMiner-Multi/releases/download/$SRB_VERSION"
TMP=$(mktemp -d); trap 'rm -rf "$TMP"' EXIT
curl -fsSL -o "$TMP/$STEM.tar.gz"  "$BASE/$STEM.tar.gz"
curl -fsSL -o "$TMP/$STEM.tar.md5" "$BASE/$STEM.tar.md5"
(cd "$TMP" && md5sum -c <(tr -d '\r' < "$STEM.tar.md5"))

# Ferma il servizio prima di sostituire il binario: il processo tiene aperto il file
systemctl stop "$SVC" 2>/dev/null || true
tar -xzf "$TMP/$STEM.tar.gz" -C "$TMP"
SRC=$(find "$TMP" -maxdepth 1 -type d -name 'SRBMiner-Multi-*' | head -1)
mkdir -p "$MINER_DIR"
[ -f "$MINER_DIR/SRBMiner-MULTI" ] && \
    cp -a "$MINER_DIR/SRBMiner-MULTI" "$MINER_DIR/SRBMiner-MULTI.bak-$(date +%F-%H%M%S)"
cp -a "$SRC"/. "$MINER_DIR"/
chown -R root:root "$MINER_DIR"
chmod 755 "$MINER_DIR/SRBMiner-MULTI"
```

**Verifica l’MD5 prima di eseguire qualsiasi binario di mining.** Le versioni pubblicano gli hash per ogni file e il miner gira con privilegi root accedendo alla GPU. Saltare il controllo significa fidarsi di un download che non hai verificato.

Due dettagli operativi nell’unità di servizio:

```bash
cat >"$UNIT" <<EOF
[Unit]
Description=Miner Pearl (PRL) SRBMiner v$SRB_VERSION - $WORKER
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=$MINER_DIR
ExecStart=$MINER_DIR/SRBMiner-MULTI --algorithm $ALGO --pool $POOL --wallet $WALLET --worker $WORKER --disable-cpu --gpu-reset-oc$OC$THERMAL_ARG --api-enable --api-port 21550 --api-rig-name $WORKER
Restart=always
RestartSec=10
StandardOutput=append:$LOG
StandardError=append:$LOG
LimitNOFILE=65536

[Install]
WantedBy=multi-user.target
EOF
```

- **`--disable-cpu`** impedisce al miner di usare la CPU, utile se la macchina svolge anche altre attività.
- **`--shutdown-temperature 88`** ferma il miner se una ventola si guasta, invece di surriscaldare la scheda.
- **`--gpu-reset-oc`** cancella le precedenti impostazioni di clock prima di applicare le tue, evitando che restino attivi valori obsoleti.
- **`Restart=always` con `RestartSec=10`** supera i problemi del driver, comuni nei rig con più GPU.
- **`--api-enable` apre una porta di monitoraggio.** Verifica su quale interfaccia è in ascolto la porta 21550 e non esporla a una rete non affidabile. L’endpoint di monitoraggio del rig non deve essere raggiungibile dall’esterno della macchina.

Infine, configura la rotazione dei log, perché i registri del miner crescono senza limiti:

```bash
cat >/etc/logrotate.d/pearl-miner <<EOF
$LOG {
    weekly
    rotate 4
    compress
    delaycompress
    missingok
    notifempty
    copytruncate
}
EOF

systemctl daemon-reload
systemctl enable "$SVC" >/dev/null 2>&1 || true
systemctl restart "$SVC"
```

*Qui `copytruncate` è importante. SRBMiner tiene aperto il file di log. Se la rotazione lo rinomina, il miner continua a scrivere in un inode eliminato e il disco si riempie comunque.*

Controlla i progressi con un estratto filtrato invece del log grezzo:

```bash
grep -aE 'Hashrate|accepted|Pool:' /var/log/pearl-miner.log | tail -20
```

## Che cosa è andato storto

**Una guida al mining di Pearl deve iniziare dai problemi, perché incidono tutti sui pagamenti.** Tra luglio e settembre 2026 sono successe quattro cose.

### Il mercato dipende da una sola piattaforma

Il **23 luglio 2026**, PRL ha segnato un minimo storico di **0,1399 $**, rispetto a circa **87 centesimi** di giugno. È sceso del **24,2% in un giorno** e del **26,7% in una settimana**, mentre il mercato crypto più ampio è salito di circa il 2% nello stesso periodo.

La causa non è stata una notizia. È stata la scarsa profondità del mercato.

- **Il 95,17% di tutto il volume dichiarato** era concentrato su **un solo exchange, SafeTrade**, senza punteggio di fiducia CoinGecko. Una coppia PRL/USDT rappresentava **738.399 $ su circa 775.000 $** scambiati in 24 ore.
- Entrambe le coppie SafeTrade riportavano una **profondità del book di 0,00 $**.

*Un normale ordine di vendita muove un mercato simile di decine di punti percentuali. È una caratteristica strutturale del token, non una condizione temporanea.*

La distribuzione dell’offerta amplifica il problema:

| Metrica | Valore |
|---|---|
| **Capitalizzazione di mercato** | 55,7 milioni di dollari |
| **Valutazione completamente diluita** | 458,6 milioni di dollari |
| **Rapporto** | Oltre 8 volte |
| **Offerta circolante** | 255 milioni su 2,1 miliardi, meno del **13%** |

**Un token valutato su un book poco profondo, con l’87% dell’offerta ancora bloccato o non emesso, ammette un’ampia gamma di prezzi plausibili.** Pianifica l’uso dei pagamenti e non trattare il prezzo spot come stima affidabile dei ricavi.

### Un pool è stato violato

Un problema aperto il **18 settembre 2026** segnala che il wallet Pearl 2.0.5 «sospende ancora invio e ricezione dopo l’hack del suo pool avvenuto un mese fa».

**Rileggi la frase: contiene due fatti.** Un pool Pearl è stato compromesso verso **agosto 2026** e il wallet ufficiale ha sospeso i trasferimenti. La sospensione era ancora attiva un mese dopo.

Il pool scelto trattiene i tuoi pagamenti. Controlla lo storico degli incidenti prima di collegarvi un rig.

### Il sito del progetto non è raggiungibile

Al momento della stesura, **pearlresearch.ai non raggiunge alcun server.** Tutti i resolver pubblici restituiscono una route nulla, `0.0.0.0`, per il dominio principale e per sottodomini come `compute` ed `explorer`. La registrazione del dominio risulta `ACTIVE`, quindi è una configurazione DNS intenzionale, non una scadenza.

**Tre link che una guida al mining normalmente consiglierebbe non funzionano**, incluso l’esploratore di blocchi. Mining Pool Stats li elenca ancora, così i lettori provano a raggiungere indirizzi che non caricano mai.

Per esplorare i blocchi, usa **[l’esploratore di blocchi PRL](https://prlscan.com)**. Ho verificato che la pagina funziona.

### Il programma presenta ancora bug aperti

A fine settembre 2026 il tracker pubblico mostrava problemi irrisolti. La creazione di nuove segnalazioni è limitata, quindi questa panoramica è parziale.

| Problema | Data | Effetto |
|---|---|---|
| **Codice RPC del wallet desktop inattivo** | 22 set. | Il wallet non raggiunge un nodo |
| **La testnet non riesce a sincronizzarsi da zero**, i nodi si bloccano all’altezza 36760 | 22 set. | Difetto che blocca la sincronizzazione |
| **Invio e ricezione del wallet ancora sospesi** dopo l’hack del pool | 18 set. | I trasferimenti sono interessati |
| **La release macOS ARM64 ha una firma del codice non valida** | 17 set. | Non funziona senza aggirare Gatekeeper |
| **La modalità prune elimina certificati necessari per verificare gli header** | 30 ago. | Difetto di validazione |
| **Il nodo si blocca senza limite se nessun peer connesso è candidato alla sincronizzazione** | 30 ago. | Sincronizzazione fragile |
| **pearl-gemm non funziona su RTX 5070**: i kernel hash funzionano, quelli GEMM no | 31 ago. | Le schede consumer più recenti non sono supportate |

*Il caso RTX 5070 è da notare se pensavi di comprare una scheda attuale. L’architettura consumer più recente non funzionava con il percorso GEMM ufficiale.*

**In sintesi:** il software di mining è mantenuto attivamente, mentre l’esperienza utente e il mercato sono i punti deboli. SRBMiner ha pubblicato la versione 3.6.9 con importanti guadagni di efficienza il giorno prima dei reclami sul wallet.

## La blockchain è utile?

Questa domanda merita una risposta attenta, perché in molti articoli «lavoro utile» indica due cose. **Descrive un meccanismo di consenso e una tesi economica, che hanno risposte molto diverse.**

### Utilità funzionale: parziale

**La blockchain funziona. Il prodotto che la circonda non è del tutto operativo.**

Che cosa funziona:

- **La mainnet è stata avviata il 27 aprile 2026** e da allora produce blocchi.
- **L’intero stack esiste davvero**: un nodo, un wallet daemon, un client leggero SPV, un sistema di prove a conoscenza zero e un miner GPU nello stesso repository.
- **L’infrastruttura è collaudata a livello di codice.** Nodo, wallet e client leggero derivano da **btcd**, **btcwallet** e **neutrino**, progetti Bitcoin sottoposti per anni a test avversariali.
- **Il codice riflette un impegno serio.** Conta 315 stelle, 76 fork, oltre 6.800 commit e un tracker pubblico con segnalazioni di bug precise.
- **Il mining funziona.** SRBMiner ha pubblicato 247 release e ottimizzato più volte `pearlhash`. Ci sono vari pool attivi. Il mining combinato Nockchain funziona.

Che cosa non funziona:

- **I trasferimenti nel wallet ufficiale sono sospesi** dopo l’hack del pool.
- **Il wallet desktop non riesce a raggiungere un nodo** a fine settembre, secondo il suo tracker.
- **La sincronizzazione ha difetti bloccanti** sia su testnet sia su mainnet.
- **Il sito del progetto non è raggiungibile.**
- **Le GPU consumer più recenti non funzionano con il percorso GEMM.**

**La conclusione onesta è che Pearl funziona a livello di protocollo ma è inaffidabile come prodotto.** Per chi studia la prova di lavoro utile è un aspetto interessante. Per chi si aspetta di minare e ricevere pagamenti regolari è un avvertimento.

### Utilità tecnica: il meccanismo sì, il mercato no

La risposta onesta si divide in due. Confondere i due aspetti è l’errore che fanno molti articoli.

**Il meccanismo è davvero innovativo.** NoisyGEMM esegue moltiplicazioni di matrici rumorose su GPU, crea un commitment tramite hash e racchiude il lavoro in una prova a conoscenza zero per mantenere basso il costo della verifica. La costruzione si basa sull’articolo "Proofs of Useful Work from Arbitrary Matrix Multiplication" di Komargodski, Schen e Weinstein, che dichiara un sovraccarico di circa **1 + o(1)** rispetto a una moltiplicazione matriciale ingenua.

**Se il limite regge, la blockchain si protegge a un costo quasi nullo oltre al calcolo sottostante.** Questo è ciò che i precedenti tentativi PoUW non sono riusciti a ottenere. La matematica non è decorativa.

**Il mercato non è affermato.** Hashrate Index lo riassume così: «oggi la maggior parte del lavoro utile è inferenza che nessuno ha comprato, quindi gran parte del mining attuale è proof-of-work con forma di IA». È un riassunto corretto. Il calcolo ha la forma giusta, ma quasi nessuno lo paga.

L’eccezione è reale e importante. Pearl ha siglato una partnership esclusiva con **Together AI**, che ha portato in produzione un endpoint di inferenza basato su Pearl a prezzo scontato. È il primo cliente e il motivo per cui il progetto merita più credito della tipica moneta con marchio IA.

**Un cliente dimostra il concetto, non l’esistenza di un mercato.**

### Utilità pratica: per ora, ma la finestra si chiude

Per un miner la situazione pratica è mista e limitata nel tempo.

**A favore di Pearl:**

- Le GPU già disponibili generano qualcosa, anche quelle vecchie, perché i requisiti hardware sono contenuti
- I continui miglioramenti del miner aumentano direttamente il margine sull’hardware che possiedi già
- Il mining combinato con Nockchain aggiunge una seconda fonte di ricavi allo stesso hashrate
- Un sovraccarico quasi nullo evita che la blockchain consumi elettricità per hashing inutile

**A sfavore:**

- **La ricompensa di blocco diminuisce per progetto.** È il modello di Bitcoin e le emissioni calano anche se il prezzo sale.
- **La difficoltà continua a salire.** I ricavi per GPU hanno una sola direzione possibile.
- **La liquidità è scarsa.** Hashrate Index indica che è utile monitorare la liquidità PRL oltre gli exchange minori. Poca liquidità significa spread più ampi e prezzi realizzati peggiori.
- **L’aggiornamento del protocollo.** Le note SRBMiner 3.6.8 dicono che il prossimo aggiornamento Pearl renderà le GPU consumer «praticamente inutili». Prendilo sul serio: lo dice lo sviluppatore, che trae vantaggio dal fatto che la gente continui a minare.

## Il verdetto

**Pearl è l’implementazione della prova di lavoro utile più credibile mai realizzata, ma non ha dimostrato che il suo lavoro sia utile dal punto di vista economico.**

Quattro affermazioni, in ordine di certezza:

1. **Il meccanismo di consenso funziona e l’affermazione crittografica è reale.** Pearl ha risolto il problema tecnico difficile: rendere PoUW economico da verificare. È un contributo autentico, a prescindere dal futuro del token.

2. **Il calcolo è una promessa, non un prodotto.** Produrre inferenza non equivale a venderla. Oggi c’è una partnership pagante contro una rete piena di hashrate speculativo. Il ciclo è progettato, ma non gira.

3. **La finestra per il mining con GPU consumer si restringe e il protocollo la chiuderà.** Ricompense in calo, difficoltà in salita, un aggiornamento annunciato che elimina la sostenibilità delle GPU consumer e un soft fork che ha già ridotto fino all’87,5% alcuni miner descrivono un’opportunità temporanea, non una fonte di reddito.

4. **I veri rischi sono operativi e di mercato, non crittografici.** Un pool violato, i trasferimenti wallet sospesi, un sito irraggiungibile, problemi di sincronizzazione irrisolti e il 95% del volume su un exchange senza profondità del book determinano se il mining paga. Il protocollo è la parte che funziona.

*Per dirla in modo diretto: Pearl ha risolto il problema difficile, non quello che sembra facile. Dimostrare che una moltiplicazione matriciale è utile è crittografia. Trovare chi compra il risultato è vendita.*

**Se vuoi minare, consideralo un uso a breve termine dell’hardware che possiedi già.** Non comprare GPU per Pearl. Non costruire un rig pensando che i numeri attuali resteranno stabili: il calendario delle emissioni e le note dello sviluppatore del miner dicono il contrario.

**Se vuoi capire la prova di lavoro utile, Pearl è l’implementazione più importante da studiare oggi.** È la prima ad aver raggiunto una scala reale. Le prove dei prossimi due anni mostreranno se il «lavoro utile» è una vera primitiva o un fallimento ricorrente con crittografia migliore.

{{< figure src="pearl-prl-usefulness-assessment.webp" alt="Valutazione della prova di lavoro utile Pearl su tre assi: maturità funzionale elevata, meccanismo tecnico solido ma mercato pagante non dimostrato e validità pratica del mining limitata nel tempo" >}}

## Punti chiave

- **Pearl è una blockchain L1 derivata da Bitcoin e protetta dalla prova di lavoro utile.** I miner eseguono moltiplicazioni matriciali rumorose invece di hashing. La mainnet è stata avviata il **27 aprile 2026**.
- **Puoi minare in due modi:** SRBMiner con `--algorithm pearlhash` su un pool oppure il `vllm-miner` di Pearl su un nodo sincronizzato.
- **La redditività iniziale veniva dalla curva di emissione del lancio**, non dalla domanda di IA. I ricavi giornalieri stimati di una RTX 5090 si sono dimezzati poche settimane dopo la corsa.
- **I miglioramenti di efficienza del miner hanno compensato parte del calo.** La versione 3.6.9 offriva lo stesso hashrate o uno superiore con molta meno potenza.
- **Il soft fork con penalità per rango del 6 agosto 2026 ha ridotto del 50%-87,5% l’hashrate effettivo** dei miner sopra il rango 128. Aggiorna il miner quando cambiano le regole di rete.
- **Il token dipende da un solo exchange.** SafeTrade aveva il 95,17% del volume e nessuna profondità del book. Meno del 13% dell’offerta è in circolazione.
- **Un pool è stato violato verso agosto 2026**, e i trasferimenti del wallet ufficiale erano ancora sospesi un mese dopo.
- **Il sito del progetto non risolve il dominio.** Usa `prlscan.com` per esplorare i blocchi.
- **Ottimizza l’efficienza, non la frequenza.** Pearl premia l’efficienza della memoria e ridurne il clock taglia i consumi più dell’hashrate.
- **Usa la porta 3360 con una sola GPU consumer** e aggiungi `+NOCK_ADDRESS` per il mining combinato Nockchain.
- **Verifica l’MD5** di ogni download del miner prima di eseguirlo come root.
- **Mina con hardware che possiedi già.** La blockchain funziona a livello di protocollo, è inaffidabile come prodotto e il mercato del calcolo a pagamento si basa su una sola partnership.

## Prossimi passi

1. **Leggi il repository sorgente** del nodo, del wallet e del miner vLLM ufficiale: **[Repository Pearl Research Labs](https://github.com/pearl-research-labs/pearl)**
2. **Controlla il changelog prima di regolare il miner**, perché l’efficienza cambia tra versioni: **[Release SRBMiner-MULTI](https://github.com/doktor83/SRBMiner-Multi/releases)**
3. **Scegli una porta del pool** adatta al tuo hashrate misurato: **[LuckyPool per Pearl](https://pearl.luckypool.io)**
4. **Confronta la distribuzione dell’hashrate dei pool** prima di decidere: **[Statistiche dei pool di mining Pearl](https://miningpoolstats.stream/pearl)**
5. **Calcola prima il costo elettrico**, perché determina la redditività: **[Costruire un box redditizio per entrate passive](/other/creating-profitable-low-powered-crypto-miners/)**
6. **Applica le regole di tuning multi-GPU** dalla nostra altra guida al mining con lavoro utile: **[Minare Spacemesh in modo efficiente con più GPU](/other/efficient-spacemesh-mining-multiple-gpus-guide/)**

## Articoli correlati

| Articolo | Contenuto |
|---|---|
| **[Minare Spacemesh in modo efficiente con più GPU](/other/efficient-spacemesh-mining-multiple-gpus-guide/)** | Tuning multi-GPU e gestione dell’energia su un’altra blockchain a lavoro utile |
| **[Costruire un box redditizio per entrate passive](/other/creating-profitable-low-powered-crypto-miners/)** | Dimensionare l’hardware di mining in base al costo elettrico prima dell’acquisto |
| **[IA locale nel 2026: un modello 27B batte Sonnet 4.6](/articles/local-ai-2026-build-your-rig-now/)** | Cosa fanno le stesse GPU con inferenza locale anziché mining |
| **[Minare Verus su Android: guida semplice al mining da smartphone](/other/mine-verus-on-android-guide/)** | Mining CPU con hardware che possiedi già |

## Riferimenti

1. [Pearl Research Labs - monorepo della rete](https://github.com/pearl-research-labs/pearl)
2. [Problemi aperti nel repository Pearl](https://github.com/pearl-research-labs/pearl/issues)
3. [Pearl (PRL): come la matematica matriciale diventa calcolo IA e mining - Hashrate Index](https://hashrateindex.com/blog/pearl-prl-ai-compute-cryptocurrency/)
4. [Attivato il soft fork con penalità per rango sulla rete Pearl (PRL) - Cryptoage](https://cryptoage.com/en/5400-rank-penalty-softfork-activated-on-the-pearl-prl-network.html)
5. [Pearl tocca un nuovo minimo storico: il 95% del volume è su un exchange senza profondità del book - CryptoNewsLive](https://www.cryptonewslive.org/article/pearl-hit-a-fresh-all-time-low-today-95-of-its-volume-sits-on-one-exchange-with-zero-order-book-depth)
6. [Release SRBMiner-MULTI - doktor83](https://github.com/doktor83/SRBMiner-Multi/releases)
7. [LuckyPool - pool di mining combinato Pearl e Nock](https://pearl.luckypool.io)
8. [Statistiche dei pool di mining - Pearl (PRL) PearlHash](https://miningpoolstats.stream/pearl)
9. [Esploratore di blocchi PRL - prlscan.com](https://prlscan.com)

**Nota sul dominio ufficiale:** al momento della stesura, `pearlresearch.ai` e i sottodomini `compute` ed `explorer` restituiscono una route nulla. L’articolo li omette deliberatamente anziché pubblicare link non funzionanti e indirizza all’esplorazione dei blocchi su `prlscan.com`.
