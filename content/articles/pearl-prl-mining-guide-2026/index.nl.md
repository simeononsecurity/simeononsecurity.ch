---
title: "Pearl (PRL) minen in 2026: installatie, winstgevendheid en nut van het netwerk"
date: 2026-09-22
lastmod: 2026-11-20
toc: true
draft: false
description: "Stel PRL-mining met SRBMiner in, bekijk bewijs van nuttig werk (PoUW), bereken marges en beoordeel het praktische nut van de blockchain."
genre: ["Cryptovaluta", "Mijnen met GPU’s", "AI-berekeningen", "DePIN", "Blockchaintechnologie", "Linux", "Thuislab", "Computeronderdelen"]
tags: ["pearl minen", "prl-minen", "pearl prl", "bewijs van nuttig werk", "pouw", "noisygemm", "srbminer pearlhash", "pearl-mijnpool", "luckypool pearl", "gpu-minen 2026", "cryptovaluta voor AI-compute", "pearl research labs", "nockchain gecombineerd minen", "nock gecombineerd minen", "rtx 3070-minen", "srbminer-installatie", "linux-miningrig", "systemd-minerservice", "matrixvermenigvuldiging minen", "vllm-miner", "pearl-portemonnee", "prl1-adres", "winstgevendheid van mining", "mining voor AI-compute", "crypto-mininggids", "nvidia-minen", "mining-overclockinstellingen"]
cover: "/img/cover/pearl-blockchain-gpu-mining-matrix-multiplication-2026.webp"
coverAlt: "Een illustratie van een moderne GPU-miningrig die matrixvermenigvuldiging uitvoert voor de Pearl-blockchain, met dynamische datastromen en heldere kleuren tegen een donkere achtergrond."
coverCaption: ""
ref: ["/other/efficient-spacemesh-mining-multiple-gpus-guide", "/articles/local-ai-2026-build-your-rig-now"]
---

**Pearl is de eerste blockchain met bewijs van nuttig werk (PoUW) die echte productieschaal heeft bereikt. Miners krijgen er beloningen voor matrixvermenigvuldiging in plaats van hashing.** Het mainnet ging op **27 april 2026** van start. Binnen enkele weken ontstond een hausse in GPU-mining, gebaseerd op de claim dat dezelfde berekening de blockchain beveiligt en rekenwerk voor AI oplevert.

*De claim klopt technisch, maar is economisch nog niet bewezen. Dat verschil vormt het hele verhaal.*

Deze gids legt uit hoe je PRL mint, welke berekening de miner uitvoert, waarom de marges na de lancering zo snel krompen en of de blockchain iets van waarde oplevert.

**Wat je na afloop kunt:** een portemonnee instellen, een miner verifiëren, het stroomverbruik meten en de winstgevendheid berekenen met je eigen stroomtarief. Zie ramingen van de miningpool en inkomsten rond de lancering als waarnemingen op een bepaalde datum, niet als aankoopgarantie.

## Het korte antwoord

**Pearl is een echte technische prestatie, gekoppeld aan het economische probleem waar elke nieuwe munt mee te maken krijgt.**

| Vraag | Kort antwoord |
|---|---|
| **Wat is het?** | Een van Bitcoin afgeleide L1 die met bewijs van nuttig werk (PoUW) wordt beveiligd. Miners voeren matrixvermenigvuldigingen met ruis uit in plaats van SHA-256-hashing |
| **Hoe mine je het?** | Met SRBMiner-MULTI en `--algorithm pearlhash` via een pool, of met Pearls eigen vLLM-miner op je eigen node |
| **Waarom was het winstgevend?** | De emissies rond de lancering waren enkele weken hoger dan de moeilijkheidsgraad. Daarna haalde de moeilijkheidsgraad de beloningen in |
| **Is het nog winstgevend?** | Dat hangt af van je apparatuur en de kans wordt kleiner. Bekijk de margesectie hieronder |
| **Is de blockchain nuttig?** | **Het mechanisme wel, de marktplaats nog niet.** Zie het oordeel verderop |

**Het belangrijkste om te weten voordat je hiervoor een rig bouwt:** in de eigen releasenotes van versie 3.6.8 schrijft de minerontwikkelaar dat een komende Pearl-upgrade GPU’s voor consumenten „vrijwel onbruikbaar” maakt om mee te minen. Dat zegt geen externe criticus, maar de maker van de miner zelf.

## Pearl: opbouw en doel

Pearl is een L1-blockchain gebouwd door **Pearl Research Labs**. In de eigen repository staat deze beschrijving:

> "Pearl is een L1-blockchain op basis van het protocol voor bewijs van nuttig werk (PoUW), waarbij minen als bijproduct van willekeurige matrixvermenigvuldiging plaatsvindt."

De repository bevat een volledige node, een portemonneedienst, een SPV-lightclient, een zero-knowledge-bewijssysteem en een GPU-miner. De software valt onder de **ISC License**, een permissieve auteursrechtlicentie. De blockchaininfrastructuur is afgeleid van grondig geteste Bitcoin-projecten: **btcd** voor de node, **btcwallet** voor de portemonnee en **neutrino** voor de lightclient.

**Het ontwerp leunt bewust op Bitcoin** en heeft een maximale voorraad van **2,1 miljard PRL**, precies honderd keer Bitcoins 21 miljoen. De blokbeloning neemt af en er verschijnen ongeveer elke twee minuten nieuwe blokken.

*De basis is bewust behoudend. De vernieuwing zit volledig in de functie die het werk uitvoert.*

### Bewijs van nuttig werk uitgelegd

Bewijs van nuttig werk is een oud idee met een slechte staat van dienst. Het voorstel was steeds om Bitcoins opzettelijk verspilde hashing te vervangen door berekeningen die daarnaast iets waardevols opleveren. Bijna alle eerdere pogingen faalden om dezelfde reden: het „nuttige” werk bleek niet nuttig, of was niet goedkoop genoeg te verifiëren om een blockchain te beveiligen.

Pearl voert dit uit met een routine die **NoisyGEMM** heet. Een miner laat op een GPU matrixvermenigvuldigingen met ruis uitvoeren, hasht het resultaat tot een commitment en verpakt het werk in een **zero-knowledge-bewijs**, zodat de blockchain dit goedkoop kan verifiëren.

Het schema is gebaseerd op een cryptografiepaper uit 2025, **"Proofs of Useful Work from Arbitrary Matrix Multiplication"** van Komargodski, Schen en Weinstein. De paper claimt een overhead van ongeveer **1 + o(1) ten opzichte van een naïeve matrixvermenigvuldiging**. Dit is de dragende claim van het project. Als het beveiligen van de blockchain vrijwel niets kost boven op de berekening zelf, is die berekening bijna gratis te produceren.

**De belofte is twee voor de prijs van één. Eén GPU-bewerking, twee resultaten.**

Deze claim onderscheidt Pearl van tien jaar mislukte PoUW-concepten. De meeste daarvan hadden geen vergelijkbare bovengrens.

{{< figure src="pearl-noisygemm-proof-of-useful-work-flow.webp" alt="Diagram dat toont hoe Pearl met bewijs van nuttig werk een GPU-matrixvermenigvuldiging omzet in een hashcommitment en een zero-knowledge-bewijs dat de blockchain goedkoop verifieert" >}}

### Wat de miningsoftware werkelijk berekent

Er zijn twee routes, en die zijn niet gelijkwaardig.

**De officiële route** staat in Pearls eigen repository. Die bestaat uit twee onderdelen: `pearl-gateway`, dat de verbinding met je node verzorgt, en `vllm-miner`, dat via vLLM het GPU-werk uitvoert. De gateway communiceert via JSON-RPC met een lokale `pearld`-node en biedt een mininginterface via een Unix-socket of TCP-poort 8337.

**De miningpoolroute** is wat de meeste mensen gebruiken. SRBMiner-MULTI ondersteunt Pearl met het algoritme `pearlhash`; je richt de miner op een miningpool.

Dit verschil is belangrijk voor de claim over nut. **De officiële miner laadt een echt taalmodel.** Het documentatievoorbeeld van Pearl draait `pearl-ai/Llama-3.3-70B-Instruct-pearl` in Docker met GPU-doorgifte. Dit model met 70 miljard parameters voert inferentie uit terwijl dezelfde bewerking de blockchain beveiligt.

*Inferentie produceren is een echte mogelijkheid. Inferentie produceren waarvoor niemand betaalt, is een kostenpost met een blockchain eraan vast. Houd die twee ideeën uit elkaar.*

## Inkomsten uit Pearl minen en de omslag daarna

De aanvankelijke winstgevendheid van Pearl was geen raadsel en had niets met AI te maken. Het was de gebruikelijke emissiecurve van een nieuwe munt.

| Wanneer | Wat gebeurde er |
|---|---|
| **27 april 2026** | Lancering van het mainnet |
| **Eind mei 2026** | Vijf weken na de start van de blockchain begint een hausse in GPU-mining |
| **Juni 2026** | De geschatte dagelijkse inkomsten van een RTX 5090 **halveerden ongeveer** doordat de moeilijkheidsgraad steeg |
| **Midden tot eind 2026** | De minersoftware werd veel efficiënter en compenseerde een deel van de daling |

De inkrimping werkt mechanisch:

1. **Bij de lancering zijn de emissies groot en is de moeilijkheidsgraad laag.** Vroege miners ontvangen bovengemiddelde beloningen per eenheid hashrate.
2. **Die beloningen trekken hashrate aan.** Meer GPU’s gaan de blockchain minen.
3. **De moeilijkheidsgraad stijgt mee.** De beloning per GPU daalt.

Pearl voegt een tweede neerwaartse kracht toe, want de blokbeloning neemt volgens het ontwerp af. **De inkomsten kunnen dus om twee redenen dalen en de moeilijkheidsgraad heeft één reden om te stijgen.**

### Tegengestelde kracht: efficiëntie van miningprogramma’s

De marges stortten niet overal even hard in, omdat de miners sneller werden. De wijzigingslijst voor SRBMiner en pearlhash laat de verbetering zien:

| Versie | Wijziging voor Pearlhash |
|---|---|
| **3.6.1** | B300-ondersteuning toegevoegd. Voor een B300 SXM6 op `--gpu-cclock 1600` werd ongeveer **706 TH/s bij 920 W** gemeld |
| **3.6.2** | Verbeteringen voor H100, H200 en de 4000-serie |
| **3.6.8** | Hogere hashrate, vooral op de 3000-serie |
| **3.6.9** | **Grote efficiëntieverbeteringen.** Op de meeste architecturen dezelfde of hogere hashrate bij veel lager stroomverbruik |

**Voor iemand die thuis mint, is elektriciteit de grootste bedrijfskostenpost.** Een nieuwe versie die de hashrate behoudt en het verbruik verlaagt, verbetert de marge direct, zonder wijziging van de tokenprijs of netwerkmoeilijkheid. Daarom lijkt dezelfde rig die in juni marginaal was, in september redelijk met identieke apparatuur.

*Efficiëntiewinst helpt echt, maar tijdelijk. Dezelfde verbeteringen zijn beschikbaar voor iedereen die tegelijk met jou de moeilijkheidsgraad omhoog drijft.*

## De strafsoftfork voor hoge ranks

In de nacht van **6 augustus 2026** werd rond **02:00 UTC, blok 96251** een softfork op Pearl geactiveerd. Veel miners merkten dit pas de volgende ochtend, toen hun hashrate was gedaald.

Het Pearl-protocol heeft een parameter voor de **noise-rang**. Een hogere rang maakte het makkelijker om met dezelfde hoeveelheid werk een jackpot te winnen. **Sommige miners kozen bewust hoge rangen en kregen zo onevenredig veel effectieve hashrate en beloningen.** Het team onderzocht wat het abnormale miningoptimalisaties noemde en reageerde met een strafmechanisme.

| Regelwijziging | Effect |
|---|---|
| **Laagst toegestane rang** | 128 |
| **Jackpotgrens** | Wordt nu geschaald met de formule `128 / rank` |
| **Voordeel van hoge rangen** | Volledig verwijderd |

**Gevolgen voor miners:**

- Mining boven rang 128 kostte operators **50% tot 87,5% van hun effectieve hashrate**
- Mining op of onder rang 128 kostte vrijwel niets

Voor iedereen die nu begint, gelden twee lessen.

**Je hashrate hangt af van programma’s en netwerkregels, niet alleen van je GPU.** Een configuratie die in juli goed benchmarkte, mat niet wat de operator dacht dat die mat.

**Werk de miner bij wanneer het netwerk verandert.** Oudere versies verliezen veel efficiëntie of werken niet goed onder de nieuwe regels. De software van miningpools werd vóór de fork bijgewerkt, waaronder PearlFortune v2.1.0 en Krig (Kryptex) v1.1.0, samen met miners zoals Tw-pearl-miner v3.3.0 en Wildrig 0.49.8.

*Een softfork die de beloning met maximaal 87,5% verlaagt, maakt duidelijk waarom je projectaankondigingen moet volgen en niet alleen een uitbetalingsdashboard moet bekijken.*

## De twee manieren om Pearl te minen

| | Minen via een pool | Officiële vLLM-miner |
|---|---|---|
| **Programma** | SRBMiner-MULTI | `pearl-gateway` plus `vllm-miner` |
| **Algoritme** | `pearlhash` | NoisyGEMM via vLLM |
| **Node nodig** | Nee | **Ja, een gesynchroniseerde `pearld`** |
| **Uitbetaling** | Miningpool, PPLNS of solo | Rechtstreeks naar je miningadres |
| **Draait een echt model** | Nee | **Ja, bijvoorbeeld Llama-3.3-70B-Instruct** |
| **Installatie-inspanning** | Laag | Hoog, vereist de CUDA-toolkit en Python 3.12 |
| **Geschikt voor** | Snel hashrate aan het netwerk leveren | Rechtstreeks rekenwerk aan het netwerk bijdragen |

**Begin met poolmining.** Je hebt geen node, synchronisatie of modeldownload nodig. Binnen enkele minuten heb je hashrate en een uitbetalingsadres. Gebruik de officiële miner alleen als je specifiek inferentie wilt aanbieden of een node wilt draaien.

{{< figure src="pearl-mining-pool-vs-vllm-miner-comparison.webp" alt="Diagram dat minen via een pool met SRBMiner vergelijkt met de officiële vLLM-miner en per route de vereiste node-, gateway- en inferentieonderdelen toont" >}}

## Apparatuur voor GPU’s voor consumenten

Pearl valt op door wat het niet vereist. Hashrate Index merkte op dat de apparatuurvereisten **ongewoon laag zijn: weinig RAM, weinig opslag, een lichte CPU en geen duur glasvezelnetwerk zoals een echt trainingscluster nodig heeft.** Een analist noemde het „een goede manier om bestaande apparatuur te benutten”.

Dat is het eerlijke voordeel. **Ook bestaande, oudere GPU’s leveren iets op.**

| GPU-klasse | Waarneming |
|---|---|
| **RTX 5090 en 4090** | Hoogste inkomsten per kaart. Hier werd ook de vroege halvering van de inkomsten gemeten |
| **RTX 3000-serie** | Specifiek gericht op de hashrateverbetering in 3.6.8. Nog bruikbaar, waarbij efficiëntie belangrijker is dan ruwe snelheid |
| **Datacenteraccelerators** | H100, H200 en B300 zijn in 2026 toegevoegd en verbeterd. De hashraterace beweegt deze kant op |
| **Oudere kaarten of kaarten met weinig VRAM** | Marginaal. Controleer een actuele winstcalculator voordat je iets bouwt |

**Het patroon van elke release in 2026 is hetzelfde.** Eerst werden vlaggenschipaccelerators toegevoegd en het sterkst verbeterd, omdat daar de hashrate het meeste waard is. Consumentenkaarten kregen aandacht toen de 3000-serie nog ruimte had om te verbeteren.

*Tuning voor efficiëntie levert meer op dan jagen op kloksnelheid. Dat is het tegenovergestelde van wat de meeste mininggidsen leren.*

## Installatie op Linux

De miningpoolroute vereist vier dingen: het SRBMiner-programma, een Pearl-portemonneeadres, een endpoint van een miningpool en een service die de miner actief houdt.

### Maak eerst een portemonneeadres aan

Pearl-miningadressen beginnen met **`prl1`**. De officiële portemonnee heet **Oyster**. Dit is de HD-portemonneedienst in de Pearl-repository, met JSON-RPC- en gRPC-interfaces. Genereer daarmee een **Taproot**-miningadres.

Sla deze stap niet over en hergebruik geen adres van een andere blockchain. **Beloningen die naar een adres gaan waarover je geen controle hebt, zijn verloren.**

### Poorten van de miningpool en gecombineerd minen

LuckyPool is de grootste miningpool voor Pearl en biedt poorten met een moeilijkheidsgraad die is afgestemd op de verwachte hashrate:

| Poort | Startmoeilijkheid | Aanbevolen hashrate |
|---|---|---|
| **3360** | 2M | Minder dan 500 TH/s |
| **3361** | 4M | 500 tot 1000 TH/s |
| **3362** | 8M | Meer dan 1000 TH/s |

Kies de poort die past bij de werkelijke hashrate van je rig. **Eén consumentengpu hoort op poort 3360.** Een kleine rig op een poort met hoge moeilijkheid zetten, zorgt voor lange onderbrekingen tussen shares en meer variantie, zonder voordeel.

Houd rekening met twee poolfuncties:

- **Solo-mining** werkt op elke poort als je `solo:` voor je portemonneeadres zet. Vind je een blok, dan krijg je de volledige blokbeloning. Zo niet, dan verdien je niets. Met een hashrate van een consumentengpu kan het lang duren.
- **Nockchain-merge-mining** levert NOCK naast PRL op dezelfde hashrate op. Voeg daarvoor `+NOCK_ADDRESS` toe aan je Pearl-portemonneeadres. De miningpool betaalt NOCK uit op Nockchain zelf, dus een adres voor een wrapped token dat met `0x` begint kan die betaling niet ontvangen. **Je miner moet merge-mining ondersteunen. Zonder die functie mine je nog steeds gewoon Pearl.**

De miningpool publiceert hosts op zowel `luckypool.io` als `lproute.com`. Als je netwerk rechtstreeks miningverkeer blokkeert, behoud dan de poort en vervang het domein.

## Een werkend installatiescript

Het volgende script installeert SRBMiner als een systemd-service op een Debian- of Ubuntu-computer. Het detecteert alle GPU’s, past per kaart overclockvlaggen toe, controleert de download met de gepubliceerde MD5-hash, schrijft de unit en een logrotatebeleid en start de service opnieuw.

```bash
#!/usr/bin/env bash
# install-pearl-miner.sh -- installeer SRBMiner (Pearl / PRL) als systemd-service.
# Uitvoeren: sudo bash install-pearl-miner.sh
set -euo pipefail

ALGO="pearlhash"
POOL="${POOL:-pearl-us-east.luckypool.io:3360}"
WALLET="${WALLET:-<YOUR_PR1_ADDRESS>}"   # prl1... voeg +NOCK_ADDRESS toe voor merge-mining
WORKER="${WORKER:-rig-1}"
SRB_VERSION="${SRB_VERSION:-3.6.9}"
MINER_DIR="/opt/srbminer"
UNIT="/etc/systemd/system/pearl-miner.service"
SVC="pearl-miner.service"
LOG="/var/log/pearl-miner.log"

# Tuning voor RTX 3070-klasse. MCORE vergrendelt de geheugenklok ruim onder de
# standaardwaarde van 7001 MHz van de kaart. Dit is dus bewust een efficiënte underclock, geen
# prestatiegerichte overclock. Zet een waarde op "" om die vlag uit te schakelen.
CCLOCK="${CCLOCK:-1560}"
MCLOCK="${MCLOCK:-5001}"
COFFSET="${COFFSET:-150}"
PLIMIT="${PLIMIT:-180}"
FAN="${FAN:-}"
THERMAL="${THERMAL:-88}"
```

De tuninginstellingen verdienen uitleg, want ze lijken op het eerste gezicht verkeerd. **`MCORE=5001` ligt onder de standaardgeheugenkloksnelheid van een 3070.** Dat is opzettelijk. Pearl beloont geheugenefficiëntie en een lagere geheugenklok verlaagt het stroomverbruik meer dan de hashrate. **Neem overclockwaarden uit een hashratedatabase niet over zonder te controleren op welke GPU de meting is uitgevoerd.** Vaak is een benchmark opgenomen op een andere kaart dan die in jouw machine.

```bash
[ "$(id -u)" -eq 0 ] || { echo "voer dit uit als root (sudo)"; exit 1; }
command -v nvidia-smi >/dev/null || { echo "nvidia-smi ontbreekt - installeer eerst het stuurprogramma"; exit 1; }

GPU_N=$(nvidia-smi --query-gpu=index --format=csv,noheader | wc -l)
echo "== $GPU_N NVIDIA-GPU(s) gevonden =="
nvidia-smi --query-gpu=index,name,memory.total,power.limit --format=csv,noheader

# Maak voor elke gevonden GPU een set overclockvlaggen
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

# Download en verifieer de release
STEM="SRBMiner-Multi-$(echo "$SRB_VERSION" | tr . -)-Linux"
BASE="https://github.com/doktor83/SRBMiner-Multi/releases/download/$SRB_VERSION"
TMP=$(mktemp -d); trap 'rm -rf "$TMP"' EXIT
curl -fsSL -o "$TMP/$STEM.tar.gz"  "$BASE/$STEM.tar.gz"
curl -fsSL -o "$TMP/$STEM.tar.md5" "$BASE/$STEM.tar.md5"
(cd "$TMP" && md5sum -c <(tr -d '\r' < "$STEM.tar.md5"))

# Stop de service voordat je het programma vervangt: de service houdt het bestand open
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

**Controleer de MD5-hash voordat je een miningprogramma uitvoert.** Bij elke uitgave staan hashes per bestand. Een miner draait met rootrechten en leest je GPU uit. Als je de controle overslaat, vertrouw je een download die je niet hebt gecontroleerd.

Twee operationele details in de service-unit:

```bash
cat >"$UNIT" <<EOF
[Unit]
Description=Pearl (PRL) SRBMiner versie $SRB_VERSION - werker $WORKER
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

- **`--disable-cpu`** voorkomt dat de miner de CPU gebruikt. Dat is van belang als de machine ook iets anders doet.
- **`--shutdown-temperature 88`** stopt de miner als een ventilator uitvalt, zodat de kaart niet oververhit raakt.
- **`--gpu-reset-oc`** wist eerdere klokinstellingen voordat jouw instellingen worden toegepast. Zo blijven oude waarden van een eerdere sessie niet actief.
- **`Restart=always` met `RestartSec=10`** herstelt de service na driverproblemen, die vaak voorkomen bij rigs met meerdere GPU’s.
- **`--api-enable` opent een monitoringpoort.** Controleer op welke interface poort 21550 luistert en stel die niet bloot aan een onbetrouwbaar netwerk. Een monitorendpoint voor een rig hoeft niet buiten de machine bereikbaar te zijn.

Configureer tot slot logrotatie, want mininglogs blijven anders onbeperkt groeien:

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

*`copytruncate` is hier belangrijk. SRBMiner houdt het logbestand open. Als logrotatie het bestand hernoemt, schrijft de miner naar een verwijderde inode en loopt de schijf alsnog vol.*

Volg de voortgang met een gefilterde logweergave in plaats van het volledige log:

```bash
grep -aE 'Hashrate|accepted|Pool:' /var/log/pearl-miner.log | tail -20
```

## Wat er misging

**Een Pearl-mininggids moet beginnen met de problemen, want die beïnvloeden allemaal je uitbetaling.** Tussen juli en september 2026 gingen vier dingen mis.

### De markt hangt van één handelsplatform af

Op **23 juli 2026** bereikte PRL een nieuw dieptepunt van **$0,1399**, tegenover ongeveer **87 cent** in juni. De munt daalde **24,2% op één dag** en **26,7% in een week**, terwijl de bredere cryptomarkt in dezelfde periode ongeveer 2% steeg.

De oorzaak was geen nieuwsbericht, maar de marktdiepte.

- **95,17% van al het gerapporteerde handelsvolume** zat op **één handelsplatform, SafeTrade**, zonder vertrouwensscore van CoinGecko. Eén PRL/USDT-paar was goed voor **$738.399 van ongeveer $775.000** aan handel in 24 uur.
- Voor beide SafeTrade-paren werd **$0,00 orderboekdiepte** gemeld.

*Een gewone verkooporder beweegt zo’n markt met dubbele cijfers. Dat is een structurele eigenschap van de token, geen tijdelijke situatie.*

De voorraad maakt dit effect sterker:

| Maatstaf | Waarde |
|---|---|
| **Marktkapitalisatie** | $55,7 miljoen |
| **Volledig verwaterde waardering** | $458,6 miljoen |
| **Verhouding** | Meer dan 8× |
| **Circulerende voorraad** | 255 miljoen van 2,1 miljard, minder dan **13%** |

**Een token met een prijs op basis van één dun orderboek en 87% van de voorraad die nog vastzit of niet is uitgegeven, kent een brede bandbreedte aan mogelijke prijzen.** Bepaal wat je met uitbetalingen doet en beschouw de spotprijs niet als betrouwbare inkomstenraming.

### Een miningpool werd gehackt

In een melding van **18 september 2026** staat dat Pearl-portemonnee 2.0.5 „nog steeds geen verzendingen en ontvangsten toestond na de hack van een miningpool een maand eerder”.

**Lees dat nog eens, want er staan twee feiten in.** Rond **augustus 2026** werd een miningpool voor Pearl gecompromitteerd. De officiële portemonnee schortte daarop transacties op. Een maand later gold die opschorting nog steeds.

De miningpool die je kiest beheert je uitbetaling. Controleer de incidentgeschiedenis voordat je er een rig op aansluit.

### De projectwebsite is onbereikbaar

Op het moment van schrijven **verbindt pearlresearch.ai niet met een server.** Iedere openbare resolver retourneert voor het hoofddomein en subdomeinen als `compute` en `explorer` een null-route, `0.0.0.0`. De domeinregistratie staat op `ACTIVE`, dus de DNS-status is bewust ingesteld en niet het gevolg van een verlopen registratie.

**Drie links waar een mininggids je normaal naartoe zou sturen, zijn dood**, waaronder die naar de blokverkenner. Mining Pool Stats vermeldt ze nog steeds, waardoor lezers een adres proberen dat nooit laadt.

Gebruik in plaats daarvan **[prlscan.com](https://prlscan.com)** om blokken te bekijken. Ik heb bevestigd dat de pagina werkt.

### De programma’s hebben nog openstaande fouten

De openbare lijst met meldingen vermeldt eind september 2026 nog onopgeloste problemen. Nieuwe meldingen aanmaken is beperkt, dus dit overzicht is onvolledig.

| Issue | Datum | Betekenis |
|---|---|---|
| **RPC-code van desktopportemonnee inactief** | 22 sep | De portemonnee kan geen node bereiken |
| **Testnet kan niet vanaf nul synchroniseren**, nodes lopen vast op hoogte 36760 | 22 sep | De synchronisatielogica heeft een blokkerend defect |
| **Verzenden en ontvangen via portemonnee nog opgeschort** na poolhack | 18 sep | Transacties zijn getroffen |
| **macOS ARM64-release heeft ongeldige codesignatuur** | 17 sep | Start niet zonder Gatekeeper te omzeilen |
| **Prunemodus verwijdert certificaten die nodig zijn om headers te verifiëren** | 30 aug | Een validatiefout |
| **Node loopt oneindig vast als geen verbonden peer een synchronisatiekandidaat is** | 30 aug | Kwetsbare synchronisatie |
| **pearl-gemm werkt niet op RTX 5070**. Hashkernels werken, maar GEMM-kernels falen | 31 aug | De nieuwste consumentenkaarten worden niet ondersteund |

*De melding over de RTX 5070 is relevant als je hiervoor een actuele kaart wilde kopen. De nieuwste consumentenarchitectuur werkte niet met het officiële GEMM-traject.*

**Dit is de kern:** de miningprogramma’s worden actief onderhouden, maar de gebruikersgerichte en marktgerichte onderdelen zijn zwak. SRBMiner bracht versie 3.6.9 met grote efficiëntiewinst uit op de dag voordat de klachten over de portemonnee verschenen.

## Is de blockchain nuttig?

Deze vraag verdient een zorgvuldig antwoord, want „nuttig werk” heeft in veel artikelen twee betekenissen. **Het beschrijft zowel een consensusmechanisme als een economische claim, en daarop zijn de antwoorden heel verschillend.**

### Functioneel nuttig: deels

**De blockchain draait. Het product eromheen werkt niet volledig.**

Wat wel standhoudt:

- **Het mainnet ging op 27 april 2026 van start** en produceert sindsdien blokken.
- **De volledige softwarestack bestaat echt:** één repository bevat een node, portemonneedienst, SPV-lightclient, zero-knowledge-bewijssysteem en GPU-miner.
- **De basis is op codeniveau beproefd.** De node, portemonnee en lightclient zijn afgeleid van **btcd**, **btcwallet** en **neutrino**, Bitcoin-projecten die jarenlang tegen aanvallen zijn getest.
- **De codebase is serieus werk.** De repository heeft 315 sterren, 76 forks, meer dan 6.800 commits en een openbare tracker met nauwkeurige bugmeldingen van bijdragers.
- **De miningkant werkt.** SRBMiner bracht 247 versies uit en optimaliseerde `pearlhash` herhaaldelijk. Er draaien meerdere miningpools en Nockchain-merge-mining werkt.

Wat niet werkt:

- **Transacties in de officiële portemonnee zijn opgeschort** na de hack van de miningpool.
- **De desktopportemonnee kan geen node bereiken**, volgens de eigen lijst met meldingen eind september.
- **De synchronisatie bevat blokkerende defecten** op zowel testnet- als mainnettrajecten.
- **De projectwebsite is onbereikbaar.**
- **De nieuwste consumentengpu’s werken niet met het GEMM-traject.**

**De eerlijke samenvatting is dat Pearl op protocolniveau functioneel is, maar op productniveau onbetrouwbaar.** Wie bewijs van nuttig werk bestudeert, heeft reden om op te letten. Wie verwacht betrouwbaar te kunnen minen en betaald te krijgen, moet dit als waarschuwing zien.

### Technisch nuttig: het mechanisme wel, de marktplaats niet

Het eerlijke antwoord bestaat uit twee delen. Door die door elkaar te halen, missen veel artikelen de kern.

**Het mechanisme is echt vernieuwend.** Pearls NoisyGEMM-routine voert matrixvermenigvuldigingen met ruis uit op een GPU, hasht het resultaat tot een commitment en verpakt het werk in een zero-knowledge-bewijs zodat verificatie goedkoop blijft. De constructie steunt op de echte paper "Proofs of Useful Work from Arbitrary Matrix Multiplication" van Komargodski, Schen en Weinstein. Daarin wordt ongeveer **1 + o(1)** overhead ten opzichte van een naïeve matrixvermenigvuldiging geclaimd.

**Als die grens klopt, beveiligt de blockchain zichzelf tegen vrijwel geen extra kosten boven op de berekening.** Dat is wat eerdere pogingen met bewijs van nuttig werk niet voor elkaar kregen. De wiskunde is geen versiering.

**De marktplaats is nog niet gevestigd.** Hashrate Index omschreef het zo: "vandaag bestaat het meeste nuttige werk uit inferentie waar niemand voor heeft betaald. Daardoor is het grootste deel van de huidige mining bewijs van werk in een AI-vorm." Dat is een redelijke samenvatting. De berekening heeft de juiste vorm, maar voor het grootste deel betaalt niemand.

Er is een echte uitzondering. Pearl sloot een exclusieve samenwerking met **Together AI**, dat een afgeprijsd Pearl-inferentie-endpoint in productie nam. Dit is de eerste klant en de reden waarom het project meer erkenning verdient dan de gemiddelde cryptomunt met een AI-label.

**Eén klant is een proof of concept, geen markt.**

### Praktisch nuttig: voorlopig, met een kleiner wordend tijdvenster

Voor mensen die minen is het praktische beeld gemengd en tijdelijk.

**Wat in Pearls voordeel werkt:**

- Bestaande GPU’s leveren iets op, ook oudere kaarten, doordat de apparatuurvereisten laag zijn
- Voortdurende efficiëntieverbeteringen in miners verhogen de marge op apparatuur die je al bezit
- Merge-mining met Nockchain voegt een tweede inkomstenstroom toe op dezelfde hashrate
- Bijna geen overhead betekent dat de blockchain geen stroom verspilt aan nutteloze hashing

**Wat ertegen werkt:**

- **De blokbeloning daalt volgens het ontwerp.** Dit is het model van Bitcoin en de emissies nemen af, ongeacht een eventuele prijsstijging.
- **De moeilijkheidsgraad stijgt alleen maar.** De inkomsten per GPU kunnen maar één kant op.
- **De liquiditeit is laag.** Hashrate Index noemt het iets om te volgen of PRL ook buiten kleine handelsplatforms liquiditeit krijgt. Lage liquiditeit betekent grotere spreads en slechtere gerealiseerde prijzen.
- **De protocolupgrade.** In de releasenotes van SRBMiner 3.6.8 staat dat een komende Pearl-upgrade GPU’s voor consumenten „vrijwel onbruikbaar” maakt. Neem dit serieus. De uitspraak komt van de ontwikkelaar, die er belang bij heeft dat mensen blijven minen.

## Het oordeel

**Pearl is de geloofwaardigste implementatie van bewijs van nuttig werk tot nu toe, maar heeft niet bewezen dat het werk economisch nuttig is.**

Vier claims, gerangschikt op zekerheid:

1. **Het consensusmechanisme werkt en de cryptografische claim is echt.** Pearl loste het moeilijke technische probleem op: bewijs van nuttig werk goedkoop verifieerbaar maken. Dat is een echte bijdrage, ongeacht wat er met de token gebeurt.

2. **De rekenkracht is een belofte, geen product.** Inferentie produceren is niet hetzelfde als die verkopen. Momenteel is er één betalende partner tegenover een netwerk vol speculatieve hashrate. Het vliegwiel is ontworpen, maar draait nog niet.

3. **Het venster voor minen met consumentengpu’s wordt kleiner en het protocol sluit het uiteindelijk.** Een dalende beloning, stijgende moeilijkheidsgraad, een aangekondigde upgrade die minen met consumentenkaarten onmogelijk maakt en een softfork die sommige miners al tot 87,5% kostte, wijzen op een tijdelijke kans en geen inkomstenstroom.

4. **De operationele en marktgerichte onderdelen vormen het echte risico, niet de cryptografie.** Een gehackte miningpool, opgeschorte transacties vanuit de portemonnee, een onbereikbare website, onopgeloste synchronisatiedefecten en 95% van het volume op één handelsplatform zonder orderboekdiepte bepalen of mining iets oplevert. Het protocol is juist het deel dat werkt.

*Kort gezegd: Pearl loste het moeilijke probleem op, maar nog niet het probleem dat eenvoudig klinkt. Bewijzen dat matrixvermenigvuldiging nuttig is, is cryptografie. Een koper voor de uitvoer vinden, is verkoop.*

**Wil je minen, zie het dan als een kortdurende benutting van apparatuur die je al bezit.** Koop geen GPU’s voor Pearl. Bouw geen rig op basis van de aanname dat de huidige cijfers blijven gelden. Zowel het emissieschema als de releasenotes van de minerontwikkelaar zeggen het tegendeel.

**Wil je bewijs van nuttig werk begrijpen, bestudeer Pearl dan als de belangrijkste implementatie van dit moment.** Het is de eerste die echte schaal bereikte. De komende twee jaar aan bewijs laten zien of „nuttig werk” een echt basismechanisme is of een terugkerende mislukking met betere cryptografie.

{{< figure src="pearl-prl-usefulness-assessment.webp" alt="Diagram dat Pearl en bewijs van nuttig werk op drie punten beoordeelt: hoge functionele volwassenheid, een sterk technisch mechanisme maar een onbewezen betaalde marktplaats, en mining waarvan de praktische haalbaarheid tijdelijk is" >}}

## Belangrijkste punten

- **Pearl is een van Bitcoin afgeleide L1 die met bewijs van nuttig werk wordt beveiligd.** Miners voeren matrixvermenigvuldigingen met ruis uit in plaats van hashing. Het mainnet ging op **27 april 2026** van start.
- **Je kunt op twee manieren minen:** SRBMiner met `--algorithm pearlhash` via een miningpool, of Pearls eigen `vllm-miner` op een gesynchroniseerde node.
- **De vroege winst kwam door de emissiecurve rond de lancering**, niet door AI-vraag. De geschatte dagelijkse inkomsten van een RTX 5090 halveerden binnen enkele weken na de hausse.
- **Efficiëntere miners compenseerden een deel van de daling.** Versie 3.6.9 leverde dezelfde of hogere hashrate bij veel lager stroomverbruik.
- **Een softfork met een straf voor hoge rangen verlaagde op 6 augustus 2026 de effectieve hashrate met 50% tot 87,5%** voor miners boven rang 128. Werk je miner bij als de netwerkregels veranderen.
- **De tokenmarkt hangt van één handelsplatform af.** SafeTrade had 95,17% van het volume en geen orderboekdiepte. Minder dan 13% van de voorraad circuleert.
- **Rond augustus 2026 werd een miningpool gehackt** en de officiële portemonnee hield transacties een maand later nog steeds tegen.
- **De projectwebsite verwijst niet naar een werkende server.** Gebruik `prlscan.com` om blokken te bekijken.
- **Stem af op efficiëntie, niet op kloksnelheid.** Pearl beloont geheugenefficiëntie. Een lagere geheugenklok bespaart meer stroom dan hij aan hashrate kost.
- **Gebruik poort 3360 met één consumentengpu** en voeg `+NOCK_ADDRESS` toe om Nockchain mee te minen.
- **Controleer de MD5-hash** van een minerdownload voordat je het programma als root uitvoert.
- **Mine met apparatuur die je al bezit.** De blockchain werkt op protocolniveau, is onbetrouwbaar als product en heeft slechts één samenwerkingspartner die voor rekenkracht betaalt.

## Volgende stappen

1. **Lees de bronrepository** voor de node, portemonnee en officiële vLLM-miner: **[pearl-research-labs/pearl](https://github.com/pearl-research-labs/pearl)**
2. **Controleer de changelog van de miner voordat je iets afstelt**, want de efficiëntie verschilt per versie: **[SRBMiner-Multi-versies](https://github.com/doktor83/SRBMiner-Multi/releases)**
3. **Kies een poort voor de miningpool** die past bij je werkelijke hashrate: **[LuckyPool-miningpool voor Pearl](https://pearl.luckypool.io)**
4. **Vergelijk de verdeling van hashrate over miningpools** voordat je begint: **[Statistieken van miningpools - Pearl](https://miningpoolstats.stream/pearl)**
5. **Bereken eerst je stroomkosten**, want elektriciteit bepaalt of mining winstgevend is: **[Een winstgevende box voor passief inkomen bouwen](/other/creating-profitable-low-powered-crypto-miners/)**
6. **Pas de tuning voor meerdere GPU’s toe** uit onze andere gids over mining met nuttig werk: **[Efficiënt Spacemesh minen met meerdere GPU’s](/other/efficient-spacemesh-mining-multiple-gpus-guide/)**

## Gerelateerde artikelen

| Artikel | Onderwerp |
|---|---|
| **[Efficiënt Spacemesh minen met meerdere GPU’s](/other/efficient-spacemesh-mining-multiple-gpus-guide/)** | Tuning van meerdere GPU’s en stroombeheer op een andere blockchain met nuttig werk |
| **[Een winstgevende box voor passief inkomen bouwen](/other/creating-profitable-low-powered-crypto-miners/)** | Miningapparatuur afstemmen op de stroomkosten voordat je iets koopt |
| **[Lokale AI in 2026: een 27B-model verslaat Sonnet 4.6](/articles/local-ai-2026-build-your-rig-now/)** | Wat dezelfde GPU’s doen als je ze voor lokale inferentie inzet in plaats van mining |
| **[Verus minen op Android: een eenvoudige gids voor smartphonemining](/other/mine-verus-on-android-guide/)** | CPU-mining op apparatuur die je al bezit |

## Bronnen

1. [pearl-research-labs/pearl - netwerkmonorepo](https://github.com/pearl-research-labs/pearl)
2. [pearl-research-labs/pearl - openstaande problemen](https://github.com/pearl-research-labs/pearl/issues)
3. [Pearl (PRL): cryptomunten minen met AI-rekenkracht - Hashrate Index](https://hashrateindex.com/blog/pearl-prl-ai-compute-cryptocurrency/)
4. [Rank-penalty softfork activated on the Pearl (PRL) network - Cryptoage](https://cryptoage.com/en/5400-rank-penalty-softfork-activated-on-the-pearl-prl-network.html)
5. [Pearl bereikt vandaag een nieuw dieptepunt: 95% van het handelsvolume staat op één beurs zonder diepte in het orderboek - CryptoNewsLive](https://www.cryptonewslive.org/article/pearl-hit-a-fresh-all-time-low-today-95-of-its-volume-sits-on-one-exchange-with-zero-order-book-depth)
6. [SRBMiner-Multi-versies - doktor83](https://github.com/doktor83/SRBMiner-Multi/releases)
7. [LuckyPool - Pearl- en Nock-combinatieminingpool](https://pearl.luckypool.io)
8. [Miningpoolstatistieken - Pearl (PRL) PearlHash](https://miningpoolstats.stream/pearl)
9. [prlscan.com - PRL-blockverkenner](https://prlscan.com)

**Opmerking over het officiële domein:** `pearlresearch.ai` en de subdomeinen `compute` en `explorer` verwijzen op het moment van schrijven naar een null-route. Dit artikel laat ze bewust weg in plaats van dode links te publiceren en verwijst voor blokverkenning naar `prlscan.com`.
