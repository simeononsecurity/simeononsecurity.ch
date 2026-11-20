---
title: "minare Pearl (PRL) în 2026: configurare, rentabilitate și utilitatea rețelei"
date: 2026-09-22
lastmod: 2026-11-20
toc: true
draft: false
description: "Configurează minarea Pearl PRL cu SRBMiner, înțelege dovada de lucru utilă, estimează marjele și evaluează utilitatea practică a rețelei."
genre: ["Criptomonede", "minare cu GPU", "Calcul AI", "DePIN", "Lanț de blocuri", "Linux", "Laborator acasă", "Echipamente"]
tags: ["minare Pearl", "minare PRL", "Pearl PRL", "dovadă de lucru utilă", "PoUW", "NoisyGEMM", "SRBMiner Pearlhash", "pool de minare Pearl", "LuckyPool Pearl", "minare cu GPU 2026", "cripto și calcul AI", "Pearl Research Labs", "minare combinată Nockchain", "minare combinată Nock", "minare RTX 3070", "configurare SRBMiner", "rig de minare Linux", "serviciu miner systemd", "minare prin înmulțirea matricilor", "miner vLLM", "portofel Pearl", "adresă prl1", "rentabilitatea minării", "minare pentru calcul AI", "ghid de minare cripto", "minare NVIDIA", "setări de overclock pentru minare"]
cover: "/img/cover/pearl-blockchain-gpu-mining-matrix-multiplication-2026.webp"
coverAlt: "Ilustrație cu un rig modern de minare cu GPU care execută înmulțiri de matrici pentru blockchainul Pearl, cu fluxuri de date dinamice și culori vii pe un fundal întunecat."
coverCaption: ""
ref: ["/other/efficient-spacemesh-minare-multiple-gpus-guide", "/articles/local-ai-2026-build-your-rig-now"]
---

**Pearl este primul blockchain bazat pe dovada de lucru utilă care a ajuns la o scară reală de producție. Minerii sunt recompensați pentru înmulțirea matricilor, nu pentru hashing.** Mainnetul a fost lansat pe **27 aprilie 2026**, iar în câteva săptămâni a declanșat o cursă de minare cu GPU bazată pe promisiunea de a securiza un blockchain și de a produce calcul AI în aceeași operație.

*Afirmația este reală din punct de vedere tehnic, dar nu este dovedită economic. Diferența dintre aceste două lucruri este esența poveștii.*

Acest ghid explică cum să minezi PRL, ce calculează minerul, de ce marjele s-au comprimat atât de repede după lansare și dacă rețeaua produce ceva valoros.

**La final:** vei avea un portofel, un miner verificat, consumul măsurat și un calcul de rentabilitate bazat pe tariful tău la electricitate. Tratează estimările poolurilor și veniturile din perioada lansării drept observații valabile la o anumită dată, nu drept garanții de cumpărare.

## Răspunsul pe scurt

**Pearl este o realizare tehnică autentică, confruntată cu problema economică a minării pe care o are fiecare monedă nouă.**

| Întrebare | Răspuns pe scurt |
|---|---|
| **Ce este?** | Un blockchain L1 derivat din Bitcoin, securizat prin dovada de lucru utilă. Minerii execută înmulțiri zgomotoase de matrici în loc de SHA-256 |
| **Cum îl minezi?** | SRBMiner-MULTI cu `--algorithm pearlhash` conectat la un pool sau minerul vLLM al Pearl conectat la propriul nod |
| **De ce a fost rentabil?** | Emisiile de la lansare au depășit dificultatea timp de câteva săptămâni, apoi dificultatea a recuperat diferența |
| **Mai este rentabil?** | Depinde de hardware, iar fereastra se îngustează. Vezi secțiunea despre marje |
| **Este util blockchainul?** | **Mecanismul este, piața încă nu.** Detalii în evaluarea finală |

**Cel mai important lucru de înțeles înainte să construiești un rig:** notele de lansare ale dezvoltatorului minerului pentru versiunea 3.6.8 spun că o actualizare Pearl va face GPU-urile de consum „practic inutile” pentru minare. Nu este critica unui observator extern. Este afirmația celui care scrie minerul.

## Ce este Pearl

Pearl este un blockchain L1 construit de **Pearl Research Labs** și descris astfel în propriul repository:

> „Pearl este un blockchain L1 bazat pe protocolul dovezii de lucru utilă, în care minarea se face ca produs secundar al înmulțirii arbitrare a matricilor.”

Repository-ul include un nod complet, un daemon de portofel, un client ușor SPV, un sistem de demonstrații zero-knowledge și un miner GPU. Licența este **ISC**, permisivă și fără copyleft, iar infrastructura rețelei derivă din proiecte Bitcoin testate: **btcd** pentru nod, **btcwallet** pentru portofel și **neutrino** pentru clientul ușor.

**Designul împrumută în mod intenționat de la Bitcoin**, inclusiv limita de **2,1 miliarde PRL**, exact de 100 de ori mai mare decât cele 21 de milioane ale Bitcoin, cu recompense descrescătoare pe bloc și blocuri la aproximativ două minute.

*Infrastructura este conservatoare intenționat. Noutatea este în întregime în funcția de lucru.*

### Dovada de lucru utilă, explicată

Dovada de lucru utilă este o idee veche, cu un istoric slab. Propunerea a fost mereu înlocuirea hashingului intenționat risipitor al Bitcoin cu un calcul care produce și ceva valoros. Aproape toate încercările anterioare au eșuat din același motiv: munca „utilă” nu era utilă sau nu putea fi verificată suficient de ieftin pentru a securiza o rețea.

Pearl implementează ideea printr-o rutină numită **NoisyGEMM**. În practică, minerul execută înmulțiri zgomotoase de matrici pe GPU, transformă rezultatul într-un angajament criptografic și învelește munca într-o **demonstrație zero-knowledge**, astfel încât rețeaua să o verifice ieftin.

Schema se bazează pe un articol de criptografie din 2025, **„Dovezi de lucru util prin înmulțirea arbitrară a matricilor”**, de Komargodski, Schen și Weinstein. Articolul afirmă că suprasarcina este aproximativ **1 + o(1) față de o înmulțire naivă de matrici**, afirmația esențială a întregului proiect. Dacă securizarea rețelei costă aproape nimic peste calculul de bază, atunci acel calcul este aproape gratuit de produs.

**Promisiunea oferă două rezultate la preț de unul. O operație GPU, două rezultate.**

Această afirmație diferențiază Pearl de un deceniu de concepte PoUW eșuate. Majoritatea nu aveau o limită similară.

{{< figure src="pearl-noisygemm-proof-of-useful-work-flow.webp" alt="Diagramă care arată cum dovada de lucru utilă a Pearl transformă o înmulțire de matrici pe GPU într-un angajament hash și o demonstrație zero-knowledge, verificate ieftin de rețea" >}}

### Ce calculează în realitate minerul

Există două căi, iar ele nu sunt echivalente.

**Calea oficială** este disponibilă în repository-ul Pearl. Are două componente: `pearl-gateway`, care face legătura cu nodul tău, și `vllm-miner`, care execută lucrul GPU prin vLLM. Gatewayul comunică prin JSON-RPC cu un nod `pearld` local și oferă o interfață de minare prin socket Unix sau portul TCP 8337.

**Calea prin pool** este folosită de majoritatea oamenilor. SRBMiner-MULTI implementează Pearl prin algoritmul `pearlhash`, iar tu îl conectezi la un pool.

Diferența contează pentru argumentul utilității. **Minerul oficial încarcă un model lingvistic real.** Exemplul din documentația Pearl rulează `pearl-ai/Llama-3.3-70B-Instruct-pearl` într-un container Docker cu acces la GPU. Este un model cu 70 de miliarde de parametri care execută inferență în timp ce aceeași operație securizează rețeaua.

*Inferența produsă este o capabilitate reală. Inferența pe care nu o cumpără nimeni este un centru de costuri atașat la un blockchain. Păstrează separate aceste două idei.*

## De ce a fost rentabil și de ce s-a schimbat situația

Rentabilitatea inițială a Pearl nu era un mister și nu avea legătură cu AI. Era curba obișnuită a emisiilor unei monede noi.

| Când | Ce s-a întâmplat |
|---|---|
| **27 aprilie 2026** | Lansarea mainnetului |
| **Sfârșitul lui mai 2026** | Începe goana după minare cu GPU, la cinci săptămâni de la lansarea rețelei |
| **Iunie 2026** | Venitul zilnic estimat al RTX 5090 s-a **înjumătățit aproximativ** pe măsură ce a crescut dificultatea |
| **Mijlocul și sfârșitul lui 2026** | Eficiența software-ului de minare se îmbunătățește puternic și compensează parțial scăderea |

Mecanismul comprimării este simplu:

1. **Emisiile de la lansare sunt mari, iar dificultatea este redusă.** Primii mineri primesc recompense disproporționate pentru fiecare unitate de hashrate.
2. **Recompensele atrag hashrate.** Mai multe GPU-uri se conectează la rețea.
3. **Dificultatea crește pentru a ține pasul.** Recompensa per GPU scade.

Pearl adaugă încă o presiune de scădere, deoarece recompensa pe bloc scade prin design. **Veniturile au două motive să scadă, iar dificultatea unul să crească.**

### Forța contrară: eficiența software-ului

Marjele nu s-au prăbușit uniform, pentru că minerii au devenit mai rapizi. Changelogul pearlhash din SRBMiner urmărește această evoluție:

| Versiune | Schimbare Pearlhash |
|---|---|
| **3.6.1** | A adăugat suportul B300. B300 SXM6 la `--gpu-cclock 1600` a raportat aproximativ **706 TH/s la 920 W** |
| **3.6.2** | Îmbunătățiri pentru H100, H200 și seria 4000 |
| **3.6.8** | Hashrate mai bun, mai ales pentru seria 3000 |
| **3.6.9** | **Îmbunătățiri mari de eficiență.** Același hashrate sau unul mai bun la putere mult mai mică pentru majoritatea arhitecturilor |

**Pentru minerii de acasă, electricitatea este principalul cost operațional.** O versiune care păstrează hashrate-ul și reduce consumul îmbunătățește direct marja, fără schimbări ale prețului tokenului sau dificultății rețelei. De aceea, același rig care părea marginal în iunie poate părea rezonabil în septembrie.

*Câștigurile de eficiență sunt un avantaj real, dar temporar, deoarece aceleași îmbunătățiri sunt disponibile tuturor celorlalți care cresc dificultatea împreună cu tine.*

## Soft forkul cu penalizare de rang

În noaptea de **6 august 2026**, un soft fork s-a activat pe Pearl în jurul orei **02:00 UTC, blocul 96251**. Mulți mineri au aflat abia în dimineața următoare, când le-a scăzut hashrate-ul.

Protocolul Pearl are un parametru de **rank al zgomotului**. Un rank mai mare făcea mai ușor câștigul unui jackpot pentru aceeași cantitate de muncă. **Unii mineri foloseau intenționat ranguri mari și obțineau hashrate efectiv și recompense disproporționate.** Echipa a investigat ceea ce a numit optimizări anormale de minare și a răspuns cu un mecanism de penalizare.

| Modificarea regulii | Efect |
|---|---|
| **Rank minim permis** | 128 |
| **Limita jackpotului** | Acum se scalează după formula `128 / rank` |
| **Avantajul rangurilor mari** | Eliminat complet |

**Impact asupra minerilor:**

- Miningul peste rangul 128 le-a costat operatorilor **50% până la 87,5% din hashrate-ul efectiv**
- Miningul la rangul 128 sau mai jos a costat aproape nimic

Două lecții se aplică oricui începe acum.

**Hashrate-ul depinde de software și regulile rețelei, nu doar de GPU.** O configurație care a avut rezultate bune în iulie poate să nu fi măsurat ceea ce presupunea operatorul.

**Actualizează minerul când se schimbă rețeaua.** Versiunile vechi pierd eficiență sau nu mai funcționează corect cu noile reguli. Software-ul poolurilor a fost actualizat înainte de fork, inclusiv PearlFortune v2.1.0 și Krig (Kryptex) v1.1.0, alături de mineri precum Tw-pearl-miner v3.3.0 și Wildrig 0.49.8.

*Un soft fork care taie recompensa cu până la 87,5% este argumentul cel mai clar pentru a urmări anunțurile proiectului, nu doar tabloul de plăți.*

## Două moduri de a mina Pearl

| | minare prin pool | Minerul oficial vLLM |
|---|---|---|
| **Software** | SRBMiner-MULTI | `pearl-gateway` și `vllm-miner` |
| **Algoritm** | `pearlhash` | NoisyGEMM prin vLLM |
| **Necesită nod** | Nu | **Da, un `pearld` sincronizat** |
| **Plată** | Pool, PPLNS sau solo | Direct la adresa ta de minare |
| **Rulează un model real** | Nu | **Da, de exemplu Llama-3.3-70B-Instruct** |
| **Efort de configurare** | Redus | Ridicat, necesită toolkitul CUDA și Python 3.12 |
| **Potrivit pentru** | Hashrate rapid în rețea | Contribuție directă cu putere de calcul |

**Începe cu minarea prin pool.** Nu necesită nod, sincronizare sau descărcarea unui model și îți oferă hashrate și o adresă de plată în câteva minute. Treci la minerul oficial doar dacă vrei în mod special să servești inferență sau să rulezi un nod.

{{< figure src="pearl-mining-pool-vs-vllm-miner-comparison.webp" alt="Diagramă care compară minarea Pearl prin pool cu SRBMiner și minerul oficial vLLM, prezentând nodul, gatewayul și componentele de inferență necesare fiecărei metode" >}}

## Echipamente pentru GPU-uri de consum

Pearl se remarcă prin cerințele reduse. Hashrate Index a observat că profilul hardware este **neobișnuit de ușor: puțină memorie RAM, stocare redusă, CPU modest și fără rețeaua costisitoare cu mai multe fibre de care are nevoie un cluster real de antrenare.** Un analist a numit-o „o metodă excelentă de a folosi echipamentele”.

Acesta este avantajul sincer. **GPU-urile existente, inclusiv modelele mai vechi, câștigă ceva.**

| Clasa GPU | Observație |
|---|---|
| **RTX 5090 și 4090** | Cele mai mari venituri pe placă și segmentele în care s-a măsurat înjumătățirea timpurie a veniturilor |
| **Seria RTX 3000** | A fost vizată în mod special de îmbunătățirea hashrate-ului din versiunea 3.6.8. Rămâne viabilă, dar eficiența contează mai mult decât viteza brută |
| **Acceleratoare pentru centre de date** | H100, H200 și B300 au fost adăugate și îmbunătățite în 2026. Aici se îndreaptă cursa hashrate-ului |
| **Plăci vechi sau cu VRAM redus** | Rentabilitate marginală. Verifică un calculator actual de rentabilitate înainte să construiești ceva |

**Tiparul este același în toate versiunile din 2026.** Acceleratoarele de top au fost adăugate și îmbunătățite primele, deoarece acolo hashrate-ul are cea mai mare valoare. Plăcile de consum au primit atenție când seria 3000 mai avea loc de recuperare.

*Reglarea eficienței aduce venituri mai mari decât urmărirea frecvenței de clock. Este opusul a ceea ce predau majoritatea ghidurilor de minare.*

## Configurare pe Linux

Varianta prin pool are nevoie de patru lucruri: binarul SRBMiner, o adresă de portofel Pearl, un endpoint de pool și un serviciu care să-l mențină în funcțiune.

### Obține mai întâi o adresă de portofel

Adresele de minare Pearl încep cu **`prl1`**. Portofelul oficial este **Oyster**, daemonul HD din repository-ul Pearl, care expune interfețe JSON-RPC și gRPC. Generează cu el o adresă de minare **Taproot**.

Nu sări peste acest pas și nu reutiliza o adresă de pe alt blockchain. **Recompensele trimise la o adresă pe care nu o controlezi sunt pierdute.**

### Pooluri, porturi și minare combinată

Cel mai mare pool Pearl este LuckyPool, care oferă porturi în funcție de hashrate-ul estimat:

| Port | Dificultatea inițială | Hashrate recomandat |
|---|---|---|
| **3360** | 2M | Sub 500 TH/s |
| **3361** | 4M | 500–1000 TH/s |
| **3362** | 8M | Peste 1000 TH/s |

Alege portul potrivit pentru hashrate-ul real al rigului. **O singură placă GPU de consum ar trebui conectată la 3360.** Un rig mic conectat la un port cu dificultate mare are intervale lungi fără shares și variație mai mare, fără niciun avantaj.

Două funcții ale poolului merită cunoscute:

- **Miningul solo** funcționează pe orice port dacă pui `solo:` înaintea portofelului. Păstrezi întreaga recompensă a blocului dacă găsești unul și nu câștigi nimic dacă nu găsești. Cu hashrate de consum, așteaptă-te la multă așteptare.
- **Miningul combinat cu Nockchain** generează NOCK alături de PRL pentru același hashrate, dacă adaugi `+NOCK_ADDRESS` la portofelul Pearl. Poolul plătește NOCK pe Nockchain, deci o adresă de token wrapped care începe cu `0x` nu îl poate primi. **Minerul trebuie să accepte minare combinată; fără acest suport, continuă să mineze Pearl în mod normal.**

Poolul publică atât gazde `luckypool.io`, cât și gazde de rutare `lproute.com`. Dacă rețeaua ta blochează traficul direct de minare, păstrează portul și schimbă domeniul.

## Un script funcțional de instalare

Scriptul de mai jos configurează SRBMiner ca serviciu systemd pe Debian sau Ubuntu. Detectează fiecare GPU, aplică opțiuni de overclock pentru fiecare placă, verifică descărcarea folosind MD5-ul publicat, scrie unitatea și politica logrotate și repornește serviciul.

```bash
#!/usr/bin/env bash
# install-pearl-miner.sh -- configurează SRBMiner (Pearl / PRL) ca serviciu systemd.
# Rulează: sudo bash install-pearl-miner.sh
set -euo pipefail

ALGO="pearlhash"
POOL="${POOL:-pearl-us-east.luckypool.io:3360}"
WALLET="${WALLET:-<YOUR_PR1_ADDRESS>}"   # prl1... adaugă +NOCK_ADDRESS pentru minare combinată
WORKER="${WORKER:-rig-1}"
SRB_VERSION="${SRB_VERSION:-3.6.9}"
MINER_DIR="/opt/srbminer"
UNIT="/etc/systemd/system/pearl-miner.service"
SVC="pearl-miner.service"
LOG="/var/log/pearl-miner.log"

# Reglaj pentru RTX 3070. MCORE fixează absolut clockul memoriei mult sub valoarea
# standard a plăcii de 7001 MHz. Este un underclock intenționat pentru eficiență, nu un overclock de performanță.
# Setează orice valoare la "" pentru a dezactiva opțiunea.
CCLOCK="${CCLOCK:-1560}"
MCLOCK="${MCLOCK:-5001}"
COFFSET="${COFFSET:-150}"
PLIMIT="${PLIMIT:-180}"
FAN="${FAN:-}"
THERMAL="${THERMAL:-88}"
```

Blocul de reglare merită explicat, fiindcă pare greșit la prima vedere. **`MCORE=5001` este sub clockul standard al memoriei unei plăci 3070.** Este intenționat. Pearl recompensează eficiența memoriei, iar blocarea memoriei la o frecvență mai mică reduce consumul mai mult decât reduce hashrate-ul. **Nu copia valorile de overclock dintr-un rând al unei baze de hashrate fără să verifici modelul GPU folosit la test.** Rezultatele sunt adesea obținute cu altă placă decât cea din calculatorul tău.

```bash
[ "$(id -u)" -eq 0 ] || { echo "rulează ca root (sudo)"; exit 1; }
command -v nvidia-smi >/dev/null || { echo "lipsește nvidia-smi, instalează mai întâi driverul"; exit 1; }

GPU_N=$(nvidia-smi --query-gpu=index --format=csv,noheader | wc -l)
echo "== GPU-uri NVIDIA detectate: $GPU_N =="
nvidia-smi --query-gpu=index,name,memory.total,power.limit --format=csv,noheader

# Construiește un set de opțiuni de overclock pentru fiecare GPU detectat
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

# Descarcă și verifică versiunea
STEM="SRBMiner-Multi-$(echo "$SRB_VERSION" | tr . -)-Linux"
BASE="https://github.com/doktor83/SRBMiner-Multi/releases/download/$SRB_VERSION"
TMP=$(mktemp -d); trap 'rm -rf "$TMP"' EXIT
curl -fsSL -o "$TMP/$STEM.tar.gz"  "$BASE/$STEM.tar.gz"
curl -fsSL -o "$TMP/$STEM.tar.md5" "$BASE/$STEM.tar.md5"
(cd "$TMP" && md5sum -c <(tr -d '\r' < "$STEM.tar.md5"))

# Oprește serviciul înainte să înlocuiești binarul ținut deschis de proces
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

**Verifică MD5-ul înainte să rulezi orice binar de minare.** Versiunile publică hashuri pentru fiecare fișier, iar minerul rulează cu privilegii root și accesează GPU-ul. Dacă sari peste verificare, ai încredere într-o descărcare pe care nu ai inspectat-o.

Două detalii operaționale ale unității de serviciu:

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

- **`--disable-cpu`** împiedică minerul să folosească procesorul, ceea ce contează pe o mașină care execută și alte activități.
- **`--shutdown-temperature 88`** oprește minerul în loc să supraîncălzească placa atunci când se defectează un ventilator.
- **`--gpu-reset-oc`** șterge setările de clock anterioare înainte să le aplice pe ale tale și previne păstrarea unor valori vechi.
- **`Restart=always` cu `RestartSec=10`** trece peste problemele temporare ale driverului, frecvente pe rigurile cu mai multe GPU-uri.
- **`--api-enable` deschide un port de monitorizare.** Verifică pe ce interfață ascultă portul 21550 și nu-l expune unei rețele nesigure. Endpointul de monitorizare nu trebuie să fie accesibil din afara mașinii.

În final, rotește logurile, deoarece fișierele de minare cresc fără limită:

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

*`copytruncate` contează aici. SRBMiner ține logul deschis, iar dacă rotația redenumește fișierul, minerul continuă să scrie într-un inode șters, iar discul se umple oricum.*

Urmărește progresul cu o căutare filtrată în loc să afișezi logul brut:

```bash
grep -aE 'Hashrate|accepted|Pool:' /var/log/pearl-miner.log | tail -20
```

## Ce nu a mers

**Un ghid de minare Pearl trebuie să înceapă cu problemele, fiindcă toate îți afectează plata.** Patru lucruri au mers prost între iulie și septembrie 2026.

### Piața depinde de o singură bursă

Pe **23 iulie 2026**, PRL a atins minimul istoric de **0,1399 USD**, în scădere de la aproximativ **0,87 USD** în iunie. A scăzut **24,2% într-o singură zi** și **26,7% în acea săptămână**, în timp ce piața cripto mai largă a crescut cu aproximativ 2% în aceeași perioadă.

Cauza nu a fost o știre. A fost lichiditatea.

- **95,17% din volumul raportat** era pe **o singură bursă numită SafeTrade**, fără scor de încredere CoinGecko. O singură pereche PRL/USDT a reprezentat **738.399 USD din aproximativ 775.000 USD** tranzacționați în 24 de ore.
- Ambele perechi SafeTrade raportau **0,00 USD adâncime în carnetul de ordine**.

*Un ordin obișnuit de vânzare mișcă o piață ca aceasta cu zeci de procente. Este o caracteristică structurală a tokenului, nu o condiție temporară.*

Distribuția ofertei amplifică problema:

| Indicator | Valoare |
|---|---|
| **Capitalizare de piață** | 55,7 milioane USD |
| **Evaluare complet diluată** | 458,6 milioane USD |
| **Raport** | Peste 8x |
| **Ofertă în circulație** | 255 de milioane din 2,1 miliarde, sub **13%** |

**Un token cotat într-un singur carnet subțire, cu 87% din ofertă încă blocată sau neemisă, poate avea o gamă largă de prețuri plauzibile.** Planifică ce faci cu plățile și nu trata prețul spot drept o estimare sigură a veniturilor.

### Un pool a fost compromis

Un issue deschis pe **18 septembrie 2026** relatează că portofelul Pearl 2.0.5 „încă suspenda trimiterea și primirea după atacul asupra poolului de acum o lună”.

**Citește din nou, fiindcă sunt două fapte aici.** Un pool Pearl a fost compromis în jurul lui **august 2026**, iar portofelul oficial a răspuns suspendând transferurile. Suspendarea era încă activă o lună mai târziu.

Poolul ales îți păstrează plata. Verifică istoricul incidentelor înainte să conectezi rigul la el.

### Site-ul proiectului nu este accesibil

La data redactării, **pearlresearch.ai nu ajunge la niciun server.** Toate serverele DNS publice returnează o rută nulă, `0.0.0.0`, pentru domeniul principal și subdomenii precum `compute` și `explorer`. Înregistrarea domeniului arată `ACTIVE`, deci starea DNS este deliberată, nu cauzată de expirare.

**Trei linkuri pe care un ghid de minare le-ar recomanda în mod normal sunt moarte**, inclusiv exploratorul de blocuri. Mining Pool Stats încă le listează, motiv pentru care cititorii caută o adresă care nu se încarcă niciodată.

Folosește **[prlscan.com](https://prlscan.com)** pentru explorarea blocurilor. Am confirmat că pagina funcționează.

### Software-ul are încă buguri deschise

Trackerul public de issues arată probleme nerezolvate la sfârșitul lui septembrie 2026. Crearea de issues este restricționată, deci aceasta este o imagine parțială.

| Problemă | Dată | Consecință |
|---|---|---|
| **Codul RPC al portofelului desktop este inactiv** | 22 sept. | Portofelul nu poate ajunge la un nod |
| **Testnetul nu se poate sincroniza de la zero**, nodurile se blochează la înălțimea 36760 | 22 sept. | Defect blocant în logica de sincronizare |
| **Trimiterea și primirea din portofel sunt încă suspendate** după atacul asupra poolului | 18 sept. | Transferurile sunt afectate |
| **Versiunea macOS ARM64 are o semnătură de cod invalidă** | 17 sept. | Nu rulează fără ocolirea Gatekeeper |
| **Modul prune elimină certificate necesare verificării antetelor** | 30 aug. | Defect de validare |
| **Nodul se blochează la nesfârșit dacă niciun peer conectat nu poate sincroniza** | 30 aug. | Sincronizare fragilă |
| **`pearl-gemm` nu funcționează pe RTX 5070**: kernelurile hash merg, dar cele GEMM nu | 31 aug. | Cele mai noi GPU-uri de consum nu sunt acceptate |

*Intrarea despre RTX 5070 merită atenție dacă plănuiai să cumperi o placă actuală. Cea mai nouă arhitectură de consum nu funcționa pe traseul GEMM oficial.*

**Concluzia:** software-ul de minare este întreținut activ, în timp ce partea destinată utilizatorilor și piața sunt punctele slabe. SRBMiner a lansat versiunea 3.6.9 cu câștiguri mari de eficiență cu o zi înainte să apară reclamațiile despre portofel.

## Este util blockchainul?

Întrebarea merită un răspuns atent, fiindcă în multe relatări „muncă utilă” are două sensuri. **Descrie un mecanism de consens și o afirmație economică, iar răspunsurile diferă mult.**

### Utilitate funcțională: parțială

**Rețeaua funcționează. Produsul din jur nu funcționează complet.**

Ce funcționează:

- **Mainnetul a fost lansat pe 27 aprilie 2026** și produce blocuri de atunci.
- **Întreaga suită există și este disponibilă**: un nod, un daemon de portofel, un client ușor SPV, un sistem de demonstrații zero-knowledge și un miner GPU, toate într-un singur repository.
- **Infrastructura este dovedită la nivel de cod.** Nodul, portofelul și clientul ușor derivă din **btcd**, **btcwallet** și **neutrino**, proiecte Bitcoin testate adversarial de ani de zile.
- **Baza de cod este un efort serios.** Are 315 stele, 76 forkuri, peste 6.800 de commituri și un tracker public unde contributorii raportează probleme precise.
- **Partea de minare funcționează.** SRBMiner a lansat 247 de versiuni și a optimizat repetat `pearlhash`. Mai multe pooluri funcționează. Miningul combinat cu Nockchain este operațional.

Ce nu funcționează:

- **Transferurile sunt suspendate în portofelul oficial** după compromiterea poolului.
- **Portofelul desktop nu poate ajunge la un nod**, conform trackerului propriu, la sfârșitul lui septembrie.
- **Logica de sincronizare are defecte blocante** atât pentru testnet, cât și pentru mainnet.
- **Site-ul proiectului nu este accesibil.**
- **Cele mai noi GPU-uri de consum eșuează pe ruta GEMM.**

**Rezumatul sincer este că Pearl funcționează la nivel de protocol, dar nu este de încredere la nivel de produs.** Pentru cine studiază dovada de lucru utilă, merită urmărită. Pentru cine se așteaptă să mineze și să primească regulat, este un avertisment.

### Utilitate tehnică: mecanismul da, piața nu

Răspunsul sincer are două părți. Confundarea lor este greșeala multor articole.

**Mecanismul este cu adevărat nou.** Rutina NoisyGEMM a Pearl execută înmulțiri zgomotoase de matrici pe GPU, transformă rezultatul într-un angajament și include o demonstrație zero-knowledge pentru a păstra verificarea ieftină. Construcția se bazează pe articolul real „Dovezi de lucru util prin înmulțire arbitrară de matrici”, de Komargodski, Schen și Weinstein, care afirmă o suprasarcină de aproximativ **1 + o(1)** față de înmulțirea naivă a matricilor.

**Dacă limita se confirmă, rețeaua se securizează cu un cost aproape nul peste calculul de bază.** Asta nu au reușit încercările PoUW anterioare. Matematica nu este decorativă.

**Piața nu este stabilită.** Hashrate Index a descris direct situația: „astăzi, cea mai mare parte a lucrului util este inferență pe care nimeni nu a cumpărat-o, astfel încât cea mai mare parte a minării actual este proof-of-work cu formă de AI”. Este un rezumat corect. Calculul are forma potrivită, dar aproape nimeni nu plătește pentru el.

Excepția contează și este reală. Pearl a încheiat un parteneriat exclusiv cu **Together AI**, care a pus în producție un endpoint de inferență Pearl cu reducere. Este primul client și motivul pentru care proiectul merită mai mult credit decât moneda medie cu branding AI.

**Un client este o dovadă de concept. Nu este o piață.**

### Utilitate practică: deocamdată, cu o fereastră care se închide

Pentru un miner, imaginea practică este mixtă și limitată în timp.

**Avantaje pentru Pearl:**

- GPU-urile existente generează ceva, inclusiv plăcile vechi, fiindcă profilul hardware este redus
- Îmbunătățirile continue ale eficienței minerului cresc direct marja hardware-ului pe care îl deții deja
- Miningul combinat cu Nockchain adaugă un al doilea flux de venit pe același hashrate
- Suprasarcina aproape nulă înseamnă că rețeaua nu consumă electricitatea pentru hashing fără rost

**Dezavantaje:**

- **Recompensa pe bloc scade prin design.** Acesta este modelul Bitcoin, iar emisiile se reduc indiferent de creșterea prețului.
- **Dificultatea doar crește.** Venitul per GPU are o singură direcție.
- **Lichiditatea este redusă.** Hashrate Index menționează ca subiect de urmărit dacă PRL obține lichiditate în afara burselor mici. Lichiditatea redusă înseamnă spreaduri mai mari și prețuri efective mai slabe.
- **Actualizarea protocolului.** Notele SRBMiner 3.6.8 spun că o viitoare actualizare Pearl va face GPU-urile de consum „practic inutile”. Ia avertismentul în serios. Vine de la dezvoltatorul care beneficiază dacă oamenii continuă să mineze.

## Concluzie

**Pearl este cea mai credibilă implementare de dovadă de lucru utilă construită până acum, dar nu a demonstrat că munca este utilă economic.**

Patru afirmații, în ordinea încrederii:

1. **Mecanismul de consens funcționează, iar afirmația criptografică este reală.** Pearl a rezolvat problema tehnică dificilă: verificarea ieftină a PoUW. Este o contribuție reală, indiferent de viitorul tokenului.

2. **Calculul este o promisiune, nu un produs.** Producerea inferenței nu înseamnă vânzarea ei, iar astăzi partea plătită este un singur parteneriat într-o rețea plină de hashrate speculativ. Mecanismul de creștere este proiectat. Nu se învârte încă.

3. **Fereastra pentru minare cu GPU-uri de consum se îngustează, iar protocolul o va închide.** Recompensa în scădere, dificultatea în creștere, o actualizare anunțată care elimină viabilitatea pentru consumatori și un soft fork care a redus deja hashrate-ul unor mineri cu până la 87,5% formează o oportunitate limitată în timp, nu o sursă de venit.

4. **Riscurile reale sunt operaționale și de piață, nu criptografice.** Un pool compromis, transferuri suspendate în portofel, un site inaccesibil, defecte de sincronizare nerezolvate și 95% din volum pe o singură bursă fără adâncime în carnetul de ordine decid dacă minarea plătește. Protocolul este partea care funcționează.

*Pe scurt: Pearl a rezolvat problema dificilă, dar nu a rezolvat-o încă pe cea care părea ușoară. Să demonstrezi că înmulțirea matricilor este utilă ține de criptografie. Să găsești cumpărători pentru rezultat ține de vânzări.*

**Dacă vrei să minezi, tratează asta ca utilizare pe termen scurt a hardware-ului pe care îl ai deja.** Nu cumpăra GPU-uri pentru Pearl. Nu construi un rig presupunând că cifrele actuale vor persista, fiindcă programul emisiilor și notele dezvoltatorului minerului spun că nu vor persista.

**Dacă vrei să înțelegi dovada de lucru utilă, Pearl este cea mai importantă implementare de studiat acum.** Este prima care a ajuns la scară reală, iar dovezile din următorii doi ani vor arăta dacă „munca utilă” este un primitiv autentic sau un eșec recurent cu o criptografie mai bună.

{{< figure src="pearl-prl-usefulness-assessment.webp" alt="Diagramă care evaluează dovada de lucru utilă Pearl pe trei axe: maturitate funcțională ridicată, mecanism tehnic puternic dar piață plătită nedovedită și viabilitate practică de minare limitată în timp" >}}

## Idei principale

- **Pearl este un blockchain L1 derivat din Bitcoin și securizat prin dovadă de lucru utilă**, în care minerii execută înmulțiri zgomotoase de matrici în loc de hashing. Mainnetul a fost lansat pe **27 aprilie 2026**.
- **Îl poți mina în două moduri:** SRBMiner cu `--algorithm pearlhash` conectat la un pool sau `vllm-miner` al Pearl conectat la un nod sincronizat.
- **Rentabilitatea timpurie a venit din curba emisiilor de la lansare**, nu din cererea de AI. Venitul zilnic estimat al RTX 5090 s-a înjumătățit aproximativ în câteva săptămâni de la cursa de minare.
- **Versiunile mai eficiente ale minerului au compensat parțial scăderea.** Versiunea 3.6.9 a oferit același hashrate sau unul mai bun la consum mult mai mic.
- **Soft forkul cu penalizare de rank din 6 august 2026 a redus hashrate-ul efectiv cu 50% până la 87,5%** pentru minerii peste rangul 128. Actualizează minerul când se schimbă regulile rețelei.
- **Tokenul depinde de o singură bursă pentru tranzacționare.** 95,17% din volum era pe SafeTrade, fără adâncime în carnetul de ordine, iar sub 13% din ofertă circulă.
- **Un pool a fost compromis în jurul lui august 2026**, iar transferurile portofelului oficial erau încă suspendate o lună mai târziu.
- **Site-ul proiectului nu se rezolvă.** Folosește `prlscan.com` pentru explorarea blocurilor.
- **Optimizează eficiența, nu frecvența clockului.** Pearl recompensează eficiența memoriei, iar reducerea clockului memoriei taie consumul mai mult decât hashrate-ul.
- **Folosește portul 3360 pentru o singură placă GPU de consum** și adaugă `+NOCK_ADDRESS` pentru minare combinată Nockchain.
- **Verifică MD5-ul** oricărei descărcări de miner înainte să o rulezi ca root.
- **Minează cu hardware-ul pe care îl deții deja.** Rețeaua funcționează la nivel de protocol, nu este fiabilă ca produs, iar piața de calcul plătit are un singur parteneriat.

## Pașii următori

1. **Citește repository-ul sursă** pentru nod, portofel și minerul oficial vLLM: **[pearl-research-labs/pearl](https://github.com/pearl-research-labs/pearl)**
2. **Verifică changelogul minerului înainte de orice ajustare**, deoarece eficiența se schimbă între versiuni: **[versiunile SRBMiner-Multi](https://github.com/doktor83/SRBMiner-Multi/releases)**
3. **Alege un port de pool** potrivit hashrate-ului real: **[LuckyPool Pearl](https://pearl.luckypool.io)**
4. **Compară distribuția hashrate-ului între pooluri** înainte să alegi: **[Statistici despre poolurile de minare Pearl](https://miningpoolstats.stream/pearl)**
5. **Calculează mai întâi costul energiei**, fiindcă electricitatea decide dacă minarea este rentabil: **[Construiește un sistem profitabil de venit pasiv](/other/creating-profitable-low-powered-crypto-miners/)**
6. **Aplică regulile de tuning multi-GPU** din celălalt ghid despre minare prin lucru util: **[minare Spacemesh eficient cu mai multe GPU-uri](/other/efficient-spacemesh-mining-multiple-gpus-guide/)**

## Articole conexe

| Articol | Ce prezintă |
|---|---|
| **[minare Spacemesh eficient cu mai multe GPU-uri](/other/efficient-spacemesh-mining-multiple-gpus-guide/)** | Tuning pentru mai multe GPU-uri și gestionarea energiei pe alt blockchain de lucru util |
| **[Construiește un sistem profitabil de venit pasiv](/other/creating-profitable-low-powered-crypto-miners/)** | Dimensionarea hardware-ului de minare în funcție de costul electricității, înainte de achiziție |
| **[AI local în 2026: un model 27B îl depășește pe Sonnet 4.6](/articles/local-ai-2026-build-your-rig-now/)** | Ce fac aceleași GPU-uri când rulează inferență locală în loc de minare |
| **[Minează Verus pe Android: ghid simplu pentru minare pe telefon](/other/mine-verus-on-android-guide/)** | minare CPU cu hardware-ul pe care îl deții deja |

## Referințe

1. [pearl-research-labs/pearl - monorepo-ul rețelei](https://github.com/pearl-research-labs/pearl)
2. [pearl-research-labs/pearl - probleme deschise](https://github.com/pearl-research-labs/pearl/issues)
3. [Pearl (PRL): cum matematica matricilor transformă calculul AI în minare - Hashrate Index](https://hashrateindex.com/blog/pearl-prl-ai-compute-cryptocurrency/)
4. [Soft forkul cu penalizare de rank activat în rețeaua Pearl (PRL) - Cryptoage](https://cryptoage.com/en/5400-rank-penalty-softfork-activated-on-the-pearl-prl-network.html)
5. [Pearl atinge un nou minim istoric - CryptoNewsLive](https://www.cryptonewslive.org/article/pearl-hit-a-fresh-all-time-low-today-95-of-its-volume-sits-on-one-exchange-with-zero-order-book-depth)
6. [Lansări SRBMiner-Multi - doktor83](https://github.com/doktor83/SRBMiner-Multi/releases)
7. [LuckyPool - pool de minare combinată Pearl și Nock](https://pearl.luckypool.io)
8. [Statistici pooluri de minare - Pearl (PRL) PearlHash](https://miningpoolstats.stream/pearl)
9. [prlscan.com - explorator de blocuri PRL](https://prlscan.com)

**Notă despre domeniul oficial:** la momentul redactării, `pearlresearch.ai` și subdomeniile `compute` și `explorer` returnau o rută nulă. Articolul le omite intenționat în loc să publice linkuri nefuncționale și indică `prlscan.com` pentru explorarea blocurilor.
