---
title: "Minar Pearl (PRL) el 2026: configuració, rendibilitat i utilitat de la cadena"
date: 2026-09-22
lastmod: 2026-11-19
toc: true
draft: false
description: "Configura la mineria de PRL amb SRBMiner, revisa la prova de treball útil, estima els marges i avalua la utilitat pràctica de la cadena."
genre: ["Criptomonedes", "Mineria amb GPU", "Còmput d’IA", "DePIN", "Cadena de blocs", "Linux", "Laboratori domèstic", "Maquinari"]
tags: ["mineria de Pearl", "mineria de PRL", "Pearl PRL", "prova de treball útil", "PoUW", "NoisyGEMM", "SRBMiner Pearlhash", "pool de mineria de Pearl", "LuckyPool Pearl", "mineria amb GPU 2026", "cripto de còmput d’IA", "Pearl Research Labs", "mineria combinada amb Nockchain", "mineria combinada amb Nock", "mineria amb RTX 3070", "configuració de SRBMiner", "equip de mineria Linux", "servei de mineria systemd", "mineria amb multiplicació de matrius", "miner de vLLM", "moneder Pearl", "adreça prl1", "rendibilitat de la mineria", "mineria de còmput d’IA", "guia de mineria de criptomonedes", "mineria amb NVIDIA", "ajustos d’overclock de mineria"]
cover: "/img/cover/pearl-blockchain-gpu-mining-matrix-multiplication-2026.webp"
coverAlt: "Il·lustració d’un equip modern de mineria amb GPU que calcula multiplicacions de matrius per a la blockchain Pearl, amb fluxos de dades dinàmics i colors vius sobre un fons fosc."
coverCaption: ""
ref: ["/other/efficient-spacemesh-mining-multiple-gpus-guide", "/articles/local-ai-2026-build-your-rig-now"]
---

**Pearl és la primera cadena de prova de treball útil que arriba a una escala de producció real. Remunera els miners per multiplicar matrius en comptes de calcular hashes.** La xarxa principal es va llançar el **27 d’abril de 2026** i, en poques setmanes, va desencadenar una onada de mineria amb GPU basada en la promesa de protegir una blockchain i produir còmput d’IA alhora.

*La promesa és tècnicament real, però encara no s’ha demostrat econòmicament. La distància entre aquestes dues coses és tota la història.*

Aquesta guia explica com minar PRL, què calcula el miner, per què els marges es van reduir tan de pressa després del llançament i si la cadena produeix res de valor.

**Resultat per al lector:** acabar amb un moneder, un miner verificat, una mesura del consum elèctric i un càlcul de rendibilitat amb la teva tarifa. Tracta les estimacions dels pools i els ingressos de l’època del llançament com a observacions d’una data concreta, no com una garantia de compra.

## Resposta breu

**Pearl és un assoliment tècnic real envoltat d’un problema econòmic de mineria que afronta tota moneda nova.**

| Pregunta | Resposta breu |
|---|---|
| **Què és?** | Una L1 derivada de Bitcoin i protegida amb prova de treball útil, on els miners fan multiplicacions de matrius sorolloses en lloc de SHA-256 |
| **Com es mina?** | Amb SRBMiner-MULTI i `--algorithm pearlhash` contra un pool, o amb el miner vLLM de Pearl contra el teu propi node |
| **Per què era rendible?** | Les emissions del llançament van superar la dificultat durant unes setmanes, fins que la dificultat les va atrapar |
| **Encara és rendible?** | Depèn del maquinari i la finestra es tanca. Consulta l’apartat dels marges |
| **La cadena és útil?** | **El mecanisme sí, el mercat encara no.** Trobaràs els detalls a la valoració |

**El més important abans de muntar-hi un equip:** les notes de la versió 3.6.8 del mateix desenvolupador del miner diuen que una pròxima actualització de Pearl farà que les GPU de consum siguin «gairebé inútils» per minar. No ho diu un crític extern. Ho diu qui escriu el miner.

## Què és Pearl exactament

Pearl és una blockchain L1 creada per **Pearl Research Labs** i descrita així al seu repositori:

> "Pearl és una blockchain L1 basada en el protocol de prova de treball útil, en què la mineria és un subproducte de multiplicacions arbitràries de matrius."

El repositori inclou un node complet, un dimoni de moneder, un client lleuger SPV, un sistema de proves de coneixement zero i un miner amb GPU. Té la llicència **ISC License**, una llicència permissiva. La infraestructura deriva de projectes de Bitcoin ben provats: **btcd** per al node, **btcwallet** per al moneder i **neutrino** per al client lleuger.

**El disseny pren Bitcoin com a model deliberadament**, fins i tot amb un màxim de **2.100 milions de PRL**, exactament cent vegades els 21 milions de Bitcoin, una recompensa de bloc decreixent i blocs cada dos minuts aproximadament.

*La base és conservadora expressament. La novetat es troba tota en la funció de treball.*

### Què és la prova de treball útil

La prova de treball útil és una idea antiga amb un historial pobre. La proposta sempre ha estat substituir els hashes deliberadament malbaratadors de Bitcoin per càlculs que també produeixin alguna cosa valuosa. Gairebé tots els intents anteriors van fracassar pel mateix motiu: el treball «útil» no ho era, o bé no es podia verificar prou barat per protegir una cadena.

Pearl ho implementa amb una rutina anomenada **NoisyGEMM**. El miner calcula multiplicacions sorolloses de matrius en una GPU, enllaça el resultat amb un hash i l’empaqueta en una **prova de coneixement zero** perquè la cadena el verifiqui a baix cost.

L’esquema parteix d’un article de criptografia del 2025, **"Proofs of Useful Work from Arbitrary Matrix Multiplication"**, de Komargodski, Schen i Weinstein. L’article reclama una sobrecàrrega d’aproximadament **1 + o(1) respecte d’una multiplicació de matrius ingènua**. És la premissa fonamental de tot el projecte. Si protegir la cadena gairebé no costa res a més del còmput subjacent, produir aquest còmput és gairebé gratuït.

**La proposta és dos per un. Una passada de GPU, dos resultats.**

Aquesta premissa diferencia Pearl d’una dècada de conceptes de PoUW fallits. La majoria no tenia aquest límit.

{{< figure src="pearl-noisygemm-proof-of-useful-work-flow.webp" alt="Diagrama de com la prova de treball útil de Pearl converteix una multiplicació de matrius amb GPU en un compromís hash i una prova de coneixement zero que la cadena verifica a baix cost" >}}

### Què calcula realment el programari de mineria

Hi ha dues opcions, i no són equivalents.

**L’opció oficial** es troba al repositori de Pearl. Té dos components: `pearl-gateway`, que connecta amb el node, i `vllm-miner`, que fa la feina amb la GPU mitjançant vLLM. La passarel·la parla amb un node `pearld` local per JSON-RPC i exposa una interfície de mineria en un sòcol Unix o al port TCP 8337.

**L’opció amb pool** és la que fa servir la majoria. SRBMiner-MULTI implementa Pearl amb l’algoritme `pearlhash` i es configura perquè apunti a un pool.

La diferència importa per valorar la utilitat. **El miner oficial carrega un model lingüístic real.** L’exemple de la documentació de Pearl executa `pearl-ai/Llama-3.3-70B-Instruct-pearl` dins de Docker amb pas de GPU. És un model de 70.000 milions de paràmetres que fa inferència mentre la mateixa passada protegeix la cadena.

*Produir inferència és una capacitat real. Produir-ne sense compradors és un centre de costos amb una blockchain al damunt. No confonguis aquestes dues idees.*

## Per què era rendible i què ha canviat

La rendibilitat inicial de Pearl no era cap misteri ni tenia a veure amb la IA. Era la corba d’emissions habitual d’una moneda nova.

| Quan | Què va passar |
|---|---|
| **27 d’abril de 2026** | Llançament de la xarxa principal |
| **Finals de maig de 2026** | Comença una onada de mineria amb GPU, cinc setmanes després de l’inici de la cadena |
| **Juny de 2026** | Els ingressos diaris estimats de l’RTX 5090 **es van reduir aproximadament a la meitat** quan va pujar la dificultat |
| **De mitjan a final del 2026** | L’eficiència del programari de mineria va millorar molt i va compensar part de la caiguda |

El mecanisme de compressió és directe:

1. **Al llançament, les emissions són altes i la dificultat és baixa.** Els primers miners reben recompenses desproporcionades per unitat de hash rate.
2. **Les recompenses atrauen hash rate.** Més GPU apunten a la cadena.
3. **La dificultat puja per igualar-lo.** Baixa la recompensa per GPU.

Pearl hi afegeix una segona força descendent perquè la recompensa de bloc disminueix expressament. **Els ingressos tenen dos motius per baixar i la dificultat en té un per pujar.**

### La força contrària: l’eficiència del programari

Els marges no es van enfonsar igual a tot arreu perquè els miners es van accelerar. El registre de canvis de pearlhash de SRBMiner mostra aquesta millora:

| Versió | Canvi de Pearlhash |
|---|---|
| **3.6.1** | S’hi afegeix suport per a B300. A B300 SXM6 amb `--gpu-cclock 1600` es van registrar aproximadament **706 TH/s a 920 W** |
| **3.6.2** | Millores per a H100, H200 i la sèrie 4000 |
| **3.6.8** | Millora del hash rate, sobretot a la sèrie 3000 |
| **3.6.9** | **Grans millores d’eficiència.** El mateix hash rate o superior amb molta menys potència en la majoria d’arquitectures |

**Per a qui mina a casa, l’electricitat és la principal despesa operativa.** Una versió que manté el hash rate i redueix el consum millora directament el marge sense canviar el preu del token ni la dificultat. Per això el mateix equip, marginal al juny, sembla raonable al setembre.

*L’eficiència és un avantatge real però temporal, perquè les mateixes millores també les té tothom que augmenta la dificultat.*

## La soft fork amb penalització de rang

La nit del **6 d’agost de 2026** es va activar una soft fork a Pearl cap a les **02:00 UTC, al bloc 96251**. Molts miners se’n van assabentar l’endemà al matí quan va baixar el seu hash rate.

El protocol Pearl té un paràmetre de **rang de soroll**. Un rang superior facilitava guanyar el premi gros amb la mateixa quantitat de feina. **Alguns miners van triar rangs alts expressament i van obtenir hash rate efectiu i recompenses desproporcionats.** L’equip va investigar el que va anomenar optimitzacions de mineria anòmales i va respondre amb un mecanisme de penalització.

| Canvi de regla | Efecte |
|---|---|
| **Rang mínim permès** | 128 |
| **Límit del premi gros** | Ara s’escala amb la fórmula `128 / rank` |
| **Avantatge dels rangs alts** | Eliminat del tot |

**Impacte en els miners:**

- Minar per sobre del rang 128 va costar als operadors **del 50% al 87,5% del hash rate efectiu**
- Minar al rang 128 o per sota gairebé no va tenir cost

Hi ha dues lliçons per a qui comenci ara.

**El teu hash rate depèn del programari i de les regles de la xarxa, no només de la GPU.** Una configuració amb bons resultats al juliol no mesurava el que l’operador es pensava.

**Actualitza el miner quan canviï la xarxa.** Les versions antigues perden molta eficiència o deixen de funcionar bé amb les regles noves. El programari dels pools es va actualitzar abans de la bifurcació, inclosos PearlFortune v2.1.0 i Krig (Kryptex) v1.1.0, juntament amb miners com Tw-pearl-miner v3.3.0 i Wildrig 0.49.8.

*Una soft fork que redueix una recompensa fins a un 87,5% és el motiu més clar per seguir els avisos del projecte i no només un tauler de pagaments.*

## Les dues maneres de minar Pearl

| | Mineria amb pool | Miner vLLM oficial |
|---|---|---|
| **Programari** | SRBMiner-MULTI | `pearl-gateway` més `vllm-miner` |
| **Algoritme** | `pearlhash` | NoisyGEMM amb vLLM |
| **Cal un node?** | No | **Sí, un `pearld` sincronitzat** |
| **Pagament** | Pool, PPLNS o en solitari | Directe a la teva adreça de mineria |
| **Executa un model real?** | No | **Sí, per exemple Llama-3.3-70B-Instruct** |
| **Feina de configuració** | Baixa | Alta; calen el conjunt d’eines CUDA i Python 3.12 |
| **Ideal per a** | Afegir hash rate a la xarxa de seguida | Aportar còmput directament a la xarxa |

**Comença amb la mineria amb pool.** No cal cap node, sincronització ni descàrrega de models, i tindràs hash rate i adreça de pagament en pocs minuts. Passa al miner oficial només si vols oferir inferència o executar un node.

{{< figure src="pearl-mining-pool-vs-vllm-miner-comparison.webp" alt="Diagrama que compara la mineria Pearl amb SRBMiner a través d’un pool i el miner vLLM oficial, i mostra els components de node, passarel·la i inferència de cada opció" >}}

## Maquinari per a GPU de consum

Pearl destaca per allò que no exigeix. Hashrate Index va assenyalar que el perfil de maquinari és **inusualment lleuger: poca RAM, poc emmagatzematge, una CPU modesta i cap xarxa de fibra múltiple cara com la d’un clúster real d’entrenament.** Un analista ho va descriure com «una bona manera d’aprofitar equips».

Aquest és l’atractiu honest. **Les GPU que ja tens, també les antigues, generen alguna cosa.**

| Classe de GPU | Observació |
|---|---|
| **RTX 5090 i 4090** | Més ingressos per targeta. Aquí es va mesurar la reducció inicial dels ingressos a la meitat |
| **Sèrie RTX 3000** | La millora de hash rate de la 3.6.8 s’hi va adreçar expressament. Encara és viable, i l’eficiència importa més que la velocitat bruta |
| **Acceleradors de centre de dades** | H100, H200 i B300 es van afegir i millorar durant el 2026. La cursa de hash rate es dirigeix aquí |
| **Targetes antigues o amb poca VRAM** | Marginals. Consulta una calculadora de rendibilitat actual abans de construir res |

**El patró de tots els llançaments del 2026 és el mateix.** Primer s’hi van afegir i optimitzar més els acceleradors de gamma alta perquè el hash rate val més. Les targetes de consum van rebre atenció quan la sèrie 3000 encara tenia marge de millora.

*Ajustar l’eficiència genera més ingressos que perseguir la velocitat de rellotge. És el contrari del que ensenyen la majoria de guies de mineria.*

## Configuració a Linux

L’opció amb pool necessita quatre coses: el binari de SRBMiner, una adreça de moneder Pearl, un punt de connexió al pool i un servei que el mantingui en marxa.

### Primer, crea una adreça de moneder

Les adreces de mineria Pearl comencen amb **`prl1`**. El moneder oficial és **Oyster**, el dimoni HD del repositori de Pearl, que exposa interfícies JSON-RPC i gRPC. Genera-hi una adreça de mineria **Taproot**.

No et saltis aquest pas ni reutilitzis una adreça d’una altra cadena. **Les recompenses enviades a una adreça que no controles es perden.**

### Grups de mineria, ports i mineria combinada

El pool Pearl més gran és LuckyPool, que ofereix ports amb diferents nivells segons el hash rate previst:

| Port | Dificultat inicial | Hash rate recomanat |
|---|---|---|
| **3360** | 2M | Menys de 500 TH/s |
| **3361** | 4M | De 500 a 1000 TH/s |
| **3362** | 8M | Més de 1000 TH/s |

Tria el port segons el hash rate real del teu equip. **Una sola GPU de consum ha d’anar al 3360.** Enviar un equip petit a un port de dificultat alta comporta llargs períodes sense participacions i més variància, sense cap benefici.

Cal conèixer dues funcions del pool:

- **La mineria en solitari** funciona a qualsevol port si poses `solo:` abans de l’adreça del moneder. Si trobes un bloc, et quedes tota la recompensa; si no, no guanyes res. Amb hash rate de consum, prepara’t per esperar molt.
- **La mineria combinada amb Nockchain** dona NOCK a més de PRL amb el mateix hash rate. Afegeix `+NOCK_ADDRESS` a l’adreça Pearl. El pool paga NOCK a la mateixa Nockchain, així que no es pot rebre en una adreça de token embolicat que comenci per `0x`. **El miner ha de ser compatible amb la mineria combinada. Si no ho és, encara podràs minar Pearl normalment.**

El pool publica servidors `luckypool.io` i servidors de ruta `lproute.com`. Si la xarxa bloqueja el trànsit directe de mineria, conserva el port i canvia el domini.

## Un guió d’instal·lació funcional

L’script següent configura SRBMiner com a servei systemd en un equip Debian o Ubuntu. Detecta totes les GPU, aplica opcions d’overclock per targeta, verifica la descàrrega amb l’MD5 publicat, escriu la unitat i una política de rotació de registres i reinicia el servei.

```bash
#!/usr/bin/env bash
# install-pearl-miner.sh -- instal·la SRBMiner (Pearl / PRL) com a servei systemd.
# Executa: sudo bash install-pearl-miner.sh
set -euo pipefail

ALGO="pearlhash"
POOL="${POOL:-pearl-us-east.luckypool.io:3360}"
WALLET="${WALLET:-<YOUR_PR1_ADDRESS>}"   # prl1... afegeix +NOCK_ADDRESS per fer mineria combinada
WORKER="${WORKER:-rig-1}"
SRB_VERSION="${SRB_VERSION:-3.6.9}"
MINER_DIR="/opt/srbminer"
UNIT="/etc/systemd/system/pearl-miner.service"
SVC="pearl-miner.service"
LOG="/var/log/pearl-miner.log"

# Ajust per a la classe RTX 3070. MCORE fixa el rellotge de memòria molt per sota del
# valor d’origen de 7001 MHz. És una reducció deliberada per eficiència, no un
# overclock de rendiment. Posa qualsevol valor a "" per desactivar-ne el paràmetre.
CCLOCK="${CCLOCK:-1560}"
MCLOCK="${MCLOCK:-5001}"
COFFSET="${COFFSET:-150}"
PLIMIT="${PLIMIT:-180}"
FAN="${FAN:-}"
THERMAL="${THERMAL:-88}"
```

Cal comentar el bloc d’ajustos perquè a primera vista sembla erroni. **`MCORE=5001` és inferior al rellotge de memòria d’origen d’una 3070.** És intencionat. Pearl recompensa l’eficiència de la memòria i reduir-ne el rellotge abaixa el consum més que el hash rate. **No copiïs xifres d’overclock d’una base de dades sense comprovar quina GPU es va provar.** Sovint els registres provenen d’una targeta diferent de la del teu equip.

```bash
[ "$(id -u)" -eq 0 ] || { echo "executa’m com a root (sudo)"; exit 1; }
command -v nvidia-smi >/dev/null || { echo "falta nvidia-smi - instal·la primer el controlador"; exit 1; }

GPU_N=$(nvidia-smi --query-gpu=index --format=csv,noheader | wc -l)
echo "== s’han detectat $GPU_N GPU de NVIDIA =="
nvidia-smi --query-gpu=index,name,memory.total,power.limit --format=csv,noheader

# Crea un conjunt d’opcions d’overclock per cada GPU detectada
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

# Baixa i verifica la versió
STEM="SRBMiner-Multi-$(echo "$SRB_VERSION" | tr . -)-Linux"
BASE="https://github.com/doktor83/SRBMiner-Multi/releases/download/$SRB_VERSION"
TMP=$(mktemp -d); trap 'rm -rf "$TMP"' EXIT
curl -fsSL -o "$TMP/$STEM.tar.gz"  "$BASE/$STEM.tar.gz"
curl -fsSL -o "$TMP/$STEM.tar.md5" "$BASE/$STEM.tar.md5"
(cd "$TMP" && md5sum -c <(tr -d '\r' < "$STEM.tar.md5"))

# Atura el servei abans de substituir el binari: manté el fitxer obert
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

**Verifica l’MD5 abans d’executar qualsevol binari de mineria.** Les versions publiquen hashes per fitxer, i el miner funciona amb permisos root i llegeix la GPU. Si omets la verificació, confies en una descàrrega que no has inspeccionat.

Dos detalls operatius de la unitat de servei:

```bash
cat >"$UNIT" <<EOF
[Unit]
Description=Pearl (PRL) SRBMiner versió $SRB_VERSION - worker $WORKER
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

- **`--disable-cpu`** evita que el miner usi la CPU, cosa important si l’equip també fa altres tasques.
- **`--shutdown-temperature 88`** atura el miner en comptes de fer malbé la targeta si falla un ventilador.
- **`--gpu-reset-oc`** elimina els rellotges anteriors abans d’aplicar els teus i evita que s’arrosseguin valors d’una execució prèvia.
- **`Restart=always` amb `RestartSec=10`** supera problemes puntuals dels controladors, habituals en equips amb diverses GPU.
- **`--api-enable` obre un port de monitoratge.** Confirma a quina interfície s’associa el port 21550 i no l’exposis a una xarxa no fiable. El monitoratge de l’equip no ha de ser accessible des de fora.

Finalment, configura la rotació de registres perquè els registres de mineria creixen sense límit:

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

*Aquí `copytruncate` és important. SRBMiner manté el registre obert. Si la rotació canvia el nom del fitxer, el miner continua escrivint en un inode esborrat i el disc s’acaba omplint igualment.*

Segueix el progrés amb una cua filtrada en comptes del registre en brut:

```bash
grep -aE 'Hashrate|accepted|Pool:' /var/log/pearl-miner.log | tail -20
```

## Què ha anat malament

**Una guia de mineria Pearl ha de començar pels problemes perquè tots afecten el pagament.** Entre juliol i setembre de 2026 van passar quatre coses.

### El mercat depèn d’una sola plataforma d’intercanvi

El **23 de juliol de 2026**, PRL va marcar un mínim històric de **$0,1399**, després d’haver cotitzat a uns **87 cèntims** al juny. Va caure **un 24,2% en un dia** i **un 26,7% en una setmana**, mentre el mercat cripto general pujava un 2% en el mateix període.

La causa no va ser cap notícia. Va ser la profunditat.

- **El 95,17% de tot el volum comunicat** es concentrava en **un únic exchange, SafeTrade**, sense puntuació de confiança de CoinGecko. Un sol parell PRL/USDT representava **738.399 dels aproximadament 775.000 dòlars** negociats en 24 hores.
- Els dos parells de SafeTrade indicaven una **profunditat del llibre d’ordres de 0,00 $**.

*Una ordre de venda normal mou un mercat així en dos dígits percentuals. És una característica estructural del token, no una situació temporal.*

La distribució de l’oferta ho agreuja:

| Mètrica | Valor |
|---|---|
| **Capitalització de mercat** | 55,7 milions de dòlars |
| **Valoració totalment diluïda** | 458,6 milions de dòlars |
| **Relació** | Més de 8× |
| **Oferta circulant** | 255 milions de 2.100 milions, menys del **13%** |

**Un token cotitzat en un únic llibre poc profund, amb el 87% de l’oferta bloquejada o encara no emesa, té un rang ampli de preus possibles.** Planifica què faràs amb els pagaments i no tractis el preu al comptat com una estimació fiable d’ingressos.

### Un grup de mineria va patir un atac

Una incidència oberta el **18 de setembre de 2026** diu que el moneder Pearl 2.0.5 «encara mantenia suspesos els enviaments i les recepcions després de l’atac al pool del mes anterior».

**Llegeix-ho dues vegades, perquè conté dos fets.** Un pool Pearl va patir una intrusió cap a **l’agost del 2026** i el moneder oficial va suspendre les transferències. La suspensió encara durava un mes després.

El pool que triïs guarda el teu pagament. Revisa’n l’historial d’incidents abans d’hi connectar un equip.

### El lloc web del projecte no és accessible

En el moment d’escriure, **pearlresearch.ai no arriba a cap servidor.** Tots els resolvers públics retornen una ruta nul·la, `0.0.0.0`, per al domini arrel i subdominis com `compute` i `explorer`. El registre del domini és `ACTIVE`, així que és un estat DNS deliberat i no un venciment.

**Tres enllaços que una guia de mineria normalment recomanaria són morts**, inclòs l’explorador de blocs. Mining Pool Stats encara els mostra i els lectors acaben provant una adreça que no es carrega mai.

Fes servir **[prlscan.com](https://prlscan.com)** per consultar blocs. He confirmat que la pàgina funciona.

### El programari encara té errors oberts

El rastrejador públic d’incidències mostra problemes no resolts a finals de setembre de 2026. La creació d’incidències està restringida, així que és una visió parcial.

| Incidència | Data | Què implica |
|---|---|---|
| **Codi RPC del moneder d’escriptori inactiu** | 22 set. | El moneder no pot arribar a un node |
| **La xarxa de proves no pot sincronitzar des de zero**, els nodes queden bloquejats a l’alçada 36760 | 22 set. | La lògica de sincronització té un defecte bloquejant |
| **Enviaments i recepcions del moneder encara suspesos** després de l’atac al pool | 18 set. | Les transferències estan afectades |
| **La versió macOS ARM64 té una signatura de codi no vàlida** | 17 set. | No funcionarà sense saltar-se Gatekeeper |
| **El mode de poda elimina certificats necessaris per verificar capçaleres** | 30 ag. | Un defecte de validació |
| **El node queda bloquejat indefinidament si cap peer connectat pot sincronitzar** | 30 ag. | Fragilitat de sincronització |
| **pearl-gemm falla a l’RTX 5070**; els nuclis hash funcionen però els nuclis GEMM fallen | 31 ag. | Les GPU de consum més noves no són compatibles |

*Fixa’t en l’entrada de l’RTX 5070 si pensaves comprar una targeta actual per a això. L’arquitectura de consum més nova no funcionava amb la via GEMM oficial.*

**En resum:** el programari de mineria es manté activament, però les capes d’usuari i de mercat són febles. SRBMiner va publicar la 3.6.9 amb grans guanys d’eficiència el dia abans que apareguessin les queixes del moneder.

## La cadena és útil?

La pregunta mereix una resposta acurada perquè «treball útil» té dues funcions en la majoria de cobertures. **Descriu un mecanisme de consens i una afirmació econòmica, i les respostes són ben diferents.**

### Utilitat funcional: parcial

**La cadena funciona. El producte que l’envolta no funciona del tot.**

Què funciona:

- **La xarxa principal es va llançar el 27 d’abril de 2026** i des d’aleshores ha produït blocs.
- **El conjunt complet existeix:** un node, un dimoni de moneder, un client lleuger SPV, un sistema de proves de coneixement zero i un miner amb GPU, tot en un repositori.
- **La base està provada a escala de codi.** El node, el moneder i el client lleuger deriven de **btcd**, **btcwallet** i **neutrino**, projectes de Bitcoin amb anys de proves adversàries.
- **La base de codi és un esforç seriós.** Té 315 estrelles, 76 forks, més de 6.800 commits i un rastrejador públic amb informes d’errors precisos.
- **La mineria funciona.** SRBMiner ha publicat 247 versions i ha optimitzat `pearlhash` repetidament. Funcionen diversos pools i també la mineria combinada amb Nockchain.

Què no funciona:

- **Les transferències del moneder oficial estan suspeses** després de l’atac al pool.
- **El moneder d’escriptori no pot arribar a un node** a finals de setembre, segons el seu rastrejador.
- **La sincronització té defectes bloquejants** tant a la xarxa de proves com a la principal.
- **El lloc web del projecte no és accessible.**
- **Les GPU de consum més noves fallen a la via GEMM.**

**La síntesi honesta és que Pearl funciona a nivell de protocol i és poc fiable com a producte.** Per estudiar la prova de treball útil, val la pena seguir-la. Si esperes minar i cobrar de manera fiable, és un avís.

### Utilitat tècnica: sí al mecanisme, no al mercat

La resposta honesta es divideix en dues. Confondre-les és l’error de la majoria de cobertures.

**El mecanisme és realment nou.** NoisyGEMM executa multiplicacions sorolloses de matrius en una GPU, enllaça el resultat amb un hash i empaqueta el treball en una prova de coneixement zero perquè la verificació sigui barata. La construcció parteix de l’article real "Proofs of Useful Work from Arbitrary Matrix Multiplication", de Komargodski, Schen i Weinstein, que reclama una sobrecàrrega d’aproximadament **1 + o(1)** respecte d’una multiplicació ingènua de matrius.

**Si el límit es compleix, la cadena es protegeix amb un cost addicional gairebé nul sobre el còmput subjacent.** És el que els intents anteriors de PoUW no van aconseguir. Les matemàtiques no són decoratives.

**El mercat encara no està establert.** Hashrate Index ho va descriure així: «avui la majoria de treball útil és inferència que ningú no ha comprat; per això bona part de la mineria actual és una prova de treball amb forma d’IA». És un resum just. El còmput té la forma adequada, però ningú paga per la major part.

L’excepció és real i important. Pearl va aconseguir una col·laboració exclusiva amb **Together AI**, que va posar en producció un punt final d’inferència amb Pearl a preu reduït. És el primer client i el motiu pel qual el projecte mereix més crèdit que la moneda mitjana amb marca d’IA.

**Un client és una prova de concepte, no un mercat.**

### Utilitat pràctica: de moment, amb una finestra que es tanca

Per a qui mina, la situació pràctica és mixta i temporal.

**A favor de Pearl:**

- Les GPU existents, incloses les antigues, generen alguna cosa perquè les necessitats de maquinari són baixes
- Les millores contínues d’eficiència del miner augmenten directament el marge amb el maquinari que ja tens
- La mineria combinada amb Nockchain afegeix una segona font d’ingressos amb el mateix hash rate
- Una sobrecàrrega gairebé nul·la evita gastar electricitat en hashes inútils

**En contra:**

- **La recompensa de bloc disminueix expressament.** És el model de Bitcoin i les emissions baixen encara que no pugi el preu.
- **La dificultat només puja.** Els ingressos per GPU només poden anar en una direcció.
- **La liquiditat és baixa.** Hashrate Index assenyala que cal vigilar si PRL aconsegueix liquiditat fora d’exchanges menors. Poca liquiditat vol dir diferències més grans i pitjors preus realitzats.
- **L’actualització del protocol.** Les notes de SRBMiner 3.6.8 diuen que una pròxima actualització de Pearl farà les GPU de consum «gairebé inútils». Pren-t’ho seriosament: ho diu el desenvolupador, que es beneficia si la gent continua minant.

## Valoració

**Pearl és la implementació de prova de treball útil més creïble fins ara, però encara no ha demostrat que la feina sigui útil econòmicament.**

Quatre afirmacions, ordenades per confiança:

1. **El mecanisme de consens funciona i l’afirmació criptogràfica és real.** Pearl va resoldre el problema tècnic difícil: fer que PoUW es pugui verificar a baix cost. És una contribució real, passi el que passi amb el token.

2. **El còmput és una promesa, no un producte.** Produir inferència no és el mateix que vendre-la. Avui hi ha una col·laboració que paga davant d’una xarxa plena de hash rate especulatiu. El volant està dissenyat, però no gira.

3. **La finestra per minar amb GPU de consum s’estreny i el protocol la tancarà.** Una recompensa decreixent, dificultat creixent, una actualització anunciada que elimina la viabilitat del consumidor i una soft fork que ja va reduir alguns miners fins a un 87,5% formen una oportunitat temporal, no una font d’ingressos.

4. **Els riscos reals són les capes operatives i de mercat, no la criptografia.** Un pool atacat, transferències del moneder suspeses, un lloc web inaccessible, defectes de sincronització pendents i el 95% del volum en un exchange sense profunditat d’ordres determinen si la mineria paga. El protocol és la part que funciona.

*La manera més clara de dir-ho: Pearl ha resolt el problema difícil, però encara no el que sembla fàcil. Fer que la multiplicació de matrius sigui demostrablement útil és criptografia. Trobar un comprador per al resultat és vendre.*

**Si vens a minar, tracta-ho com un ús a curt termini del maquinari que ja tens.** No compris GPU per a Pearl. No muntis un equip assumint que les xifres actuals duraran: tant el calendari d’emissions com les notes del desenvolupador diuen que no.

**Si vols entendre la prova de treball útil, Pearl és ara mateix la implementació més important per estudiar.** És la primera que arriba a una escala real. Els dos anys vinents de proves mostraran si el «treball útil» és un primitiu autèntic o un fracàs recurrent amb millor criptografia.

{{< figure src="pearl-prl-usefulness-assessment.webp" alt="Diagrama que avalua la prova de treball útil de Pearl en tres eixos: maduresa funcional alta, mecanisme tècnic sòlid però mercat de pagament no provat i viabilitat pràctica de mineria limitada en el temps" >}}

## Idees clau

- **Pearl és una L1 derivada de Bitcoin i protegida amb prova de treball útil.** Els miners fan multiplicacions sorolloses de matrius en lloc de calcular hashes. La xarxa principal es va llançar el **27 d’abril de 2026**.
- **La pots minar de dues maneres:** SRBMiner amb `--algorithm pearlhash` a través d’un pool, o `vllm-miner` de Pearl contra un node sincronitzat.
- **La rendibilitat inicial venia de la corba d’emissions del llançament**, no de la demanda d’IA. Els ingressos diaris estimats de l’RTX 5090 es van reduir gairebé a la meitat poques setmanes després de l’onada.
- **Les versions més eficients van compensar part de la caiguda.** La 3.6.9 va donar el mateix hash rate o més amb molta menys potència.
- **La soft fork de penalització de rang del 6 d’agost de 2026 va reduir del 50% al 87,5% el hash rate efectiu** dels miners per sobre del rang 128. Actualitza el miner quan canviïn les regles.
- **El token depèn d’un sol exchange.** SafeTrade concentrava el 95,17% del volum sense profunditat al llibre d’ordres i circula menys del 13% de l’oferta.
- **Un pool va patir un atac cap a l’agost del 2026** i les transferències del moneder oficial continuaven suspeses un mes després.
- **El lloc web del projecte no resol el domini.** Fes servir `prlscan.com` per consultar blocs.
- **Ajusta l’eficiència, no la velocitat de rellotge.** Pearl recompensa l’eficiència de la memòria i reduir-ne el rellotge estalvia més potència que hash rate.
- **Fes servir el port 3360 amb una sola GPU de consum** i afegeix `+NOCK_ADDRESS` per minar també Nockchain.
- **Verifica l’MD5** de qualsevol descàrrega de miner abans d’executar-la com a root.
- **Mina amb el maquinari que ja tens.** La cadena funciona a nivell de protocol, és poc fiable com a producte i el mercat de còmput de pagament només té un soci.

## Passos següents

1. **Llegeix el repositori font** del node, el moneder i el miner vLLM oficial: **[pearl-research-labs/pearl](https://github.com/pearl-research-labs/pearl)**
2. **Consulta el registre de canvis del miner abans d’ajustar res**, perquè l’eficiència varia entre versions: **[Versions de SRBMiner-Multi](https://github.com/doktor83/SRBMiner-Multi/releases)**
3. **Tria un port de pool** segons el teu hash rate real: **[Pool Pearl de LuckyPool](https://pearl.luckypool.io)**
4. **Compara la distribució del hash rate dels pools** abans de comprometre’t: **[Estadístiques de pools de mineria - Pearl](https://miningpoolstats.stream/pearl)**
5. **Calcula primer el cost elèctric**, perquè l’electricitat determina la rendibilitat: **[Construeix una caixa rendible d’ingressos passius](/other/creating-profitable-low-powered-crypto-miners/)**
6. **Aplica les pautes d’ajust de diverses GPU** de la nostra altra guia de mineria útil: **[Minar Spacemesh eficientment amb diverses GPU](/other/efficient-spacemesh-mining-multiple-gpus-guide/)**

## Articles relacionats

| Article | Què explica |
|---|---|
| **[Minar Spacemesh eficientment amb diverses GPU](/other/efficient-spacemesh-mining-multiple-gpus-guide/)** | Ajust de diverses GPU i gestió de potència en una altra cadena de treball útil |
| **[Construeix una caixa rendible d’ingressos passius](/other/creating-profitable-low-powered-crypto-miners/)** | Dimensionar maquinari de mineria segons el cost elèctric abans de comprar |
| **[IA local el 2026: un model 27B supera Sonnet 4.6](/articles/local-ai-2026-build-your-rig-now/)** | Què fan les mateixes GPU quan les dediques a inferència local en lloc de mineria |
| **[Minar Verus a Android: guia fàcil per minar amb un telèfon intel·ligent](/other/mine-verus-on-android-guide/)** | Mineria amb CPU en maquinari que ja tens |

## Referències

1. [pearl-research-labs/pearl - monorepositori de la xarxa](https://github.com/pearl-research-labs/pearl)
2. [pearl-research-labs/pearl - incidències obertes](https://github.com/pearl-research-labs/pearl/issues)
3. [Pearl (PRL): de les matemàtiques matricials a la mineria de criptomonedes amb còmput d’IA - Hashrate Index](https://hashrateindex.com/blog/pearl-prl-ai-compute-cryptocurrency/)
4. [Activació de la soft fork amb penalització de rang a la xarxa Pearl (PRL) - Cryptoage](https://cryptoage.com/en/5400-rank-penalty-softfork-activated-on-the-pearl-prl-network.html)
5. [Pearl marca avui un nou mínim històric: el 95% del volum és en un exchange sense profunditat d’ordres - CryptoNewsLive](https://www.cryptonewslive.org/article/pearl-hit-a-fresh-all-time-low-today-95-of-its-volume-sits-on-one-exchange-with-zero-order-book-depth)
6. [Versions de SRBMiner-Multi - doktor83](https://github.com/doktor83/SRBMiner-Multi/releases)
7. [LuckyPool - pool de mineria combinada de Pearl i Nock](https://pearl.luckypool.io)
8. [Estadístiques de pools de mineria - Pearl (PRL) PearlHash](https://miningpoolstats.stream/pearl)
9. [prlscan.com - explorador de blocs PRL](https://prlscan.com)

**Nota sobre el domini oficial:** en el moment d’escriure, `pearlresearch.ai` i els subdominis `compute` i `explorer` retornen una ruta nul·la. Aquest article els omet expressament en lloc de publicar enllaços morts i dirigeix la consulta de blocs a `prlscan.com`.
