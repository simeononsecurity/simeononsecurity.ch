---
title: "Pearl (PRL) 2026 minen: Einrichtung, Rentabilität und Nutzen der Blockchain"
date: 2026-09-22
lastmod: 2026-11-19
toc: true
draft: false
description: "Richte PRL-Mining mit SRBMiner ein, prüfe Proof of Useful Work, schätze Margen und bewerte den praktischen Nutzen der Blockchain."
genre: ["Kryptowährungen", "GPU-Kryptomining", "KI-Rechenleistung", "DePIN", "Blockchains", "Linux", "Heimlabor", "Geräte"]
tags: ["Pearl-Kryptomining", "PRL-Kryptomining", "Pearl PRL", "Nutzarbeitsnachweis", "PoUW", "NoisyGEMM", "SRBMiner Pearlhash", "Pearl-Miningpool", "LuckyPool Pearl", "GPU-Kryptomining 2026", "KI-Rechenleistung und Krypto", "Pearl Research Labs", "Nockchain-Zusatzverdienst", "Nock-Zusatzverdienst", "RTX-3070-Kryptomining", "SRBMiner einrichten", "Linux-Mining-Rechner", "systemd-Miner-Dienst", "Mining mit Matrixmultiplikation", "vLLM-Mining-Programm", "PRL-Geldbörse", "prl1-Adresse", "Mining-Rentabilität", "KI-Rechenleistung minen", "Krypto-Mining-Anleitung", "NVIDIA-Kryptomining", "Mining-Übertaktungseinstellungen"]
cover: "/img/cover/pearl-blockchain-gpu-mining-matrix-multiplication-2026.webp"
coverAlt: "Illustration eines modernen GPU-Mining-Rigs, das Matrixmultiplikationen für die Pearl-Blockchain berechnet, mit dynamischen Datenströmen und leuchtenden Farben vor dunklem Hintergrund."
coverCaption: ""
ref: ["/other/efficient-spacemesh-mining-multiple-gpus-guide", "/articles/local-ai-2026-build-your-rig-now"]
---

**Pearl ist die erste Proof-of-Useful-Work-Blockchain, die echte Produktionsgröße erreicht hat. Miner erhalten Belohnungen für Matrixmultiplikationen statt fürs Hashing.** Das Mainnet startete am **27. April 2026**. Innerhalb weniger Wochen löste die Behauptung, eine Blockchain zu sichern und gleichzeitig KI-Rechenleistung zu erzeugen, einen GPU-Mining-Boom aus.

*Die Behauptung ist technisch plausibel, wirtschaftlich aber unbewiesen. Der Abstand zwischen beidem ist die ganze Geschichte.*

Diese Anleitung erklärt, wie du PRL minest, was der Miner berechnet, warum die Margen nach dem Start schnell sanken und ob die Blockchain einen Mehrwert erzeugt.

**Dein Ergebnis:** eine Wallet, ein verifizierter Miner, eine gemessene Leistungsaufnahme und eine Rentabilitätsrechnung mit deinem Stromtarif. Behandle Poolschätzungen und Einnahmen aus der Startphase als Beobachtungen zu einem bestimmten Datum, nicht als Kaufgarantie.

## Die Kurzantwort

**Pearl ist eine echte technische Leistung, die mit dem wirtschaftlichen Problem konfrontiert ist, vor dem jede neue Kryptowährung steht.**

| Frage | Kurzantwort |
|---|---|
| **Was ist Pearl?** | Eine von Bitcoin abgeleitete L1, die mit Proof of Useful Work gesichert wird. Miner berechnen verrauschte Matrixmultiplikationen statt SHA-256 |
| **Wie minest du Pearl?** | Mit SRBMiner-MULTI und `--algorithm pearlhash` über einen Pool oder mit Pearls eigenem vLLM-Miner am eigenen Node |
| **Warum war es rentabel?** | Die Emissionen zum Start übertrafen die Schwierigkeit einige Wochen lang, bis die Schwierigkeit aufholte |
| **Ist es noch rentabel?** | Das hängt von der Hardware ab, und das Zeitfenster wird kleiner. Siehe den Abschnitt zu den Margen |
| **Ist die Blockchain nützlich?** | **Der Mechanismus schon, der Marktplatz noch nicht.** Einzelheiten im Fazit |

**Das Wichtigste vor dem Bau eines Mining-Rigs:** In den eigenen Versionshinweisen des Miner-Entwicklers zu Version 3.6.8 steht, dass ein kommendes Pearl-Upgrade Consumer-GPUs fürs Mining „praktisch unbrauchbar“ machen wird. Das sagt kein externer Kritiker. Es sagt der Entwickler des Miners selbst.

## Pearls Aufbau

Pearl ist eine von **Pearl Research Labs** entwickelte L1-Blockchain. Das eigene Repository beschreibt sie so:

> "Pearl ist eine L1-Blockchain auf Basis des Proof-of-Useful-Work-Protokolls, bei dem Mining als Nebenprodukt beliebiger Matrixmultiplikationen entsteht."

Das Repository enthält einen vollständigen Node, einen Wallet-Daemon, einen SPV-Light-Client, ein Zero-Knowledge-Beweissystem und einen GPU-Miner. Die Lizenz ist die **ISC License**, eine freizügige Lizenz. Die Blockchain-Infrastruktur stammt von bewährten Bitcoin-Projekten: **btcd** für den Node, **btcwallet** für die Wallet und **neutrino** für den Light-Client.

**Das Design orientiert sich bewusst an Bitcoin**, bis hin zu einem maximalen Angebot von **2,1 Milliarden PRL**, genau dem Hundertfachen von Bitcoins 21 Millionen, sinkenden Blockbelohnungen und etwa zweiminütigen Blöcken.

*Die Basis ist bewusst konservativ. Neu ist allein die Arbeitsfunktion.*

### Nutzarbeitsnachweis erklärt

Proof of Useful Work ist eine alte Idee mit wenig Erfolg. Der Vorschlag war stets, Bitcoins absichtlich verschwenderisches Hashing durch Berechnungen zu ersetzen, die nebenbei etwas Wertvolles erzeugen. Fast alle früheren Versuche scheiterten aus demselben Grund: Die „nützliche“ Arbeit war nicht nützlich oder nicht günstig genug zu verifizieren, um eine Blockchain zu sichern.

Pearl setzt die Idee mit einer Routine namens **NoisyGEMM** um. Ein Miner berechnet verrauschte Matrixmultiplikationen auf einer GPU, hasht das Ergebnis zu einem Commitment und verpackt die Arbeit in einen **Zero-Knowledge-Beweis**, damit die Blockchain sie günstig verifizieren kann.

Das Verfahren basiert auf der Kryptografiearbeit von 2025 **"Proofs of Useful Work from Arbitrary Matrix Multiplication"** von Komargodski, Schen und Weinstein. Die Arbeit behauptet einen Mehraufwand von ungefähr **1 + o(1) gegenüber einer naiven Matrixmultiplikation**. Das ist die tragende Annahme des Projekts. Wenn die Sicherung der Blockchain fast nichts zusätzlich zur eigentlichen Berechnung kostet, lässt sich diese Berechnung nahezu kostenlos erzeugen.

**Das Versprechen lautet zwei zum Preis von einem. Ein GPU-Durchlauf, zwei Ergebnisse.**

Diese Behauptung unterscheidet Pearl von einem Jahrzehnt gescheiterter PoUW-Konzepte. Den meisten fehlte eine solche Schranke.

{{< figure src="pearl-noisygemm-proof-of-useful-work-flow.webp" alt="Diagramm zeigt, wie Pearl Proof of Useful Work eine GPU-Matrixmultiplikation in ein Hash-Commitment und einen günstig verifizierbaren Zero-Knowledge-Beweis umwandelt" >}}

### Berechnung im Programm

Es gibt zwei Wege, die nicht gleichwertig sind.

**Der offizielle Weg** steckt in Pearls eigenem Repository. Er besteht aus `pearl-gateway`, das deinen Node anbindet, und `vllm-miner`, das über vLLM die GPU-Arbeit übernimmt. Das Gateway spricht per JSON-RPC mit einem lokalen `pearld`-Node und stellt eine Mining-Schnittstelle über einen Unix-Socket oder TCP-Port 8337 bereit.

**Der Pool-Weg** ist die übliche Variante. SRBMiner-MULTI unterstützt Pearl mit dem Algorithmus `pearlhash`; du richtest den Miner auf einen Pool.

Der Unterschied ist für die Nützlichkeitsbehauptung wichtig. **Der offizielle Miner lädt ein echtes Sprachmodell.** Das Dokumentationsbeispiel von Pearl startet `pearl-ai/Llama-3.3-70B-Instruct-pearl` in Docker mit GPU-Passthrough. Das Modell mit 70 Milliarden Parametern führt Inferenz aus, während derselbe Durchlauf die Blockchain sichert.

*Inferenz zu erzeugen ist eine echte Fähigkeit. Inferenz zu erzeugen, die niemand kauft, ist eine Kostenstelle mit angebundener Blockchain. Halte diese Gedanken auseinander.*

## Ursachen der frühen Rentabilität und ihres Rückgangs

Pearls anfängliche Rentabilität war kein Rätsel und hatte nichts mit KI zu tun. Es war die übliche Emissionskurve einer neuen Kryptowährung.

| Zeitpunkt | Ereignis |
|---|---|
| **27. April 2026** | Start des Mainnets |
| **Ende Mai 2026** | Fünf Wochen nach dem Start beginnt ein GPU-Mining-Boom |
| **Juni 2026** | Der geschätzte Tagesumsatz einer RTX 5090 **halbierte sich ungefähr**, als die Schwierigkeit stieg |
| **Mitte bis Ende 2026** | Die Miner-Software wurde deutlich effizienter und glich einen Teil des Rückgangs aus |

Der Rückgang läuft mechanisch ab:

1. **Zum Start sind die Emissionen hoch und die Schwierigkeit niedrig.** Frühe Miner erhalten überdurchschnittliche Belohnungen pro Hashrate.
2. **Diese Belohnungen ziehen Hashrate an.** Mehr GPUs minen die Blockchain.
3. **Die Schwierigkeit steigt entsprechend.** Die Belohnung pro GPU sinkt.

Pearl fügt eine zweite Abwärtskraft hinzu, weil die Blockbelohnung planmäßig sinkt. **Die Einnahmen haben zwei Gründe zu fallen, die Schwierigkeit einen Grund zu steigen.**

### Gegenkraft: effizientere Versionen

Die Margen brachen nicht überall gleich stark ein, weil die Miner schneller wurden. Das pearlhash-Änderungsprotokoll von SRBMiner zeigt den Fortschritt:

| Version | Pearlhash-Änderung |
|---|---|
| **3.6.1** | B300-Unterstützung ergänzt. B300 SXM6 meldete mit `--gpu-cclock 1600` rund **706 TH/s bei 920 W** |
| **3.6.2** | Verbesserungen für H100, H200 und die 4000er-Serie |
| **3.6.8** | Höhere Hashrate, vor allem bei der 3000er-Serie |
| **3.6.9** | **Deutliche Effizienzsteigerungen.** Bei den meisten Architekturen gleiche oder bessere Hashrate bei deutlich weniger Stromverbrauch |

**Für Heim-Miner sind Stromkosten der größte laufende Aufwand.** Eine Version, die die Hashrate hält und den Stromverbrauch senkt, verbessert die Marge direkt, ohne Tokenpreis oder Netzwerkschwierigkeit zu ändern. Darum wirkt dasselbe Rig, das im Juni grenzwertig war, im September auf identischer Hardware sinnvoll.

*Effizienzgewinne helfen tatsächlich, aber nur vorübergehend, denn alle anderen, die mit dir die Schwierigkeit erhöhen, erhalten dieselben Verbesserungen.*

## Die Änderung zur Bestrafung hoher Ränge

In der Nacht des **6. August 2026** wurde gegen **02:00 UTC, Block 96251** eine Softfork bei Pearl aktiviert. Viele Miner bemerkten sie erst am nächsten Morgen, als ihre Hashrate sank.

Das Pearl-Protokoll hat einen Parameter namens **Noise-Rank**. Ein höherer Rang erleichterte es, mit derselben Arbeitsmenge einen Jackpot zu gewinnen. **Einige Miner wählten absichtlich hohe Ränge und erhielten unverhältnismäßig viel effektive Hashrate und Belohnungen.** Das Team untersuchte die von ihm als ungewöhnlich beschriebenen Mining-Optimierungen und reagierte mit einem Strafmechanismus.

| Regeländerung | Auswirkung |
|---|---|
| **Niedrigster erlaubter Rang** | 128 |
| **Jackpot-Grenze** | Wird jetzt mit der Formel `128 / rank` skaliert |
| **Vorteil hoher Ränge** | Vollständig entfernt |

**Auswirkungen auf Miner:**

- Mining über Rang 128 kostete Betreiber **50 bis 87,5 % der effektiven Hashrate**
- Mining bei Rang 128 oder darunter kostete fast nichts

Für alle, die jetzt anfangen, gelten zwei Lehren.

**Deine Hashrate hängt von Software und Netzwerkregeln ab, nicht nur von der GPU.** Eine im Juli gut benchmarkte Konfiguration maß nicht das, was der Betreiber annahm.

**Aktualisiere den Miner bei Änderungen am Netzwerk.** Ältere Versionen verlieren viel Effizienz oder funktionieren mit den neuen Regeln nicht korrekt. Pool-Software wurde vor der Fork aktualisiert, darunter PearlFortune v2.1.0 und Krig (Kryptex) v1.1.0 sowie Miner wie Tw-pearl-miner v3.3.0 und Wildrig 0.49.8.

*Eine Softfork, die Belohnungen um bis zu 87,5 % kürzt, ist das deutlichste Argument dafür, Projektankündigungen zu verfolgen statt nur ein Auszahlungs-Dashboard zu lesen.*

## Zwei Verfahren für Pearl

| | Pool-Mining | Offizieller vLLM-Miner |
|---|---|---|
| **Software** | SRBMiner-MULTI | `pearl-gateway` plus `vllm-miner` |
| **Algorithmus** | `pearlhash` | NoisyGEMM über vLLM |
| **Node erforderlich** | Nein | **Ja, ein synchronisierter `pearld`** |
| **Auszahlung** | Pool, PPLNS oder solo | Direkt an deine Mining-Adresse |
| **Führt ein echtes Modell aus** | Nein | **Ja, zum Beispiel Llama-3.3-70B-Instruct** |
| **Einrichtungsaufwand** | Niedrig | Hoch, CUDA-Toolkit und Python 3.12 nötig |
| **Am besten für** | Schnell Hashrate ins Netzwerk bringen | Direkt Rechenleistung beitragen |

**Beginne mit Pool-Mining.** Dafür brauchst du weder Node noch Synchronisierung oder Modelldownload und erhältst in wenigen Minuten Hashrate und Auszahlungsadresse. Nutze den offiziellen Miner nur, wenn du ausdrücklich Inferenz anbieten oder einen Node betreiben möchtest.

{{< figure src="pearl-mining-pool-vs-vllm-miner-comparison.webp" alt="Diagramm vergleicht Pearl-Pool-Mining mit SRBMiner und den offiziellen vLLM-Miner und zeigt die erforderlichen Node-, Gateway- und Inferenzkomponenten" >}}

## Hinweise zu Grafikkarten für Privatnutzer

Pearl fällt durch die geringen Anforderungen auf. Hashrate Index merkte an, das Hardwareprofil sei **ungewöhnlich leicht: wenig RAM, wenig Speicherplatz, eine schwache CPU und keine teure Mehrfaser-Netzwerkanbindung wie bei einem echten Trainingscluster.** Ein Analyst nannte es „eine gute Möglichkeit, Geräte weiterzuverwenden“.

Das ist der ehrliche Reiz. **Vorhandene GPUs, auch ältere, bringen etwas ein.**

| GPU-Klasse | Beobachtung |
|---|---|
| **RTX 5090 und 4090** | Höchster Umsatz pro Karte; hier wurde die frühe Halbierung der Einnahmen gemessen |
| **RTX-3000-Serie** | Das Hashrate-Upgrade 3.6.8 zielte besonders auf sie. Sie bleibt brauchbar, Effizienz zählt mehr als rohe Geschwindigkeit |
| **Rechenzentrumsbeschleuniger** | H100, H200 und B300 wurden 2026 ergänzt und verbessert. In diese Richtung entwickelt sich der Hashrate-Wettlauf |
| **Ältere Karten oder wenig VRAM** | Grenzwertig. Prüfe vor dem Bau einen aktuellen Rentabilitätsrechner |

**Das Muster aller Versionen von 2026 ist gleich.** Zuerst kamen Flaggschiff-Beschleuniger hinzu und erhielten die größten Verbesserungen, weil dort die Hashrate am wertvollsten ist. Consumer-Karten rückten in den Fokus, als die 3000er-Serie noch Reserven hatte.

*Effizienzoptimierung bringt mehr Einnahmen als die Jagd nach Taktfrequenz. Das ist das Gegenteil der meisten Mining-Anleitungen.*

## Einrichtung unter Linux

Für den Pool-Weg brauchst du vier Dinge: die SRBMiner-Binärdatei, eine Pearl-Wallet-Adresse, einen Pool-Endpunkt und einen Dienst, der den Miner laufen lässt.

### Zuerst eine PRL-Adresse erstellen

Pearl-Mining-Adressen beginnen mit **`prl1`**. Die offizielle Wallet heißt **Oyster**, der HD-Wallet-Daemon im Pearl-Repository mit JSON-RPC- und gRPC-Schnittstellen. Erstelle damit eine **Taproot**-Mining-Adresse.

Überspringe diesen Schritt nicht und verwende keine Adresse einer anderen Blockchain. **Belohnungen an eine Adresse, die du nicht kontrollierst, sind verloren.**

### Adressen der Anbieter und gemeinsame Blocksuche

LuckyPool ist der größte Pearl-Pool und bietet Ports mit Schwierigkeitsstufen passend zur erwarteten Hashrate:

| Port | Startschwierigkeit | Empfohlene Hashrate |
|---|---|---|
| **3360** | 2M | Unter 500 TH/s |
| **3361** | 4M | 500 bis 1000 TH/s |
| **3362** | 8M | Über 1000 TH/s |

Wähle den Port passend zur tatsächlichen Hashrate deines Rigs. **Eine einzelne Consumer-GPU gehört an Port 3360.** Ein kleines Rig an einen Port mit hoher Schwierigkeit zu schicken, führt ohne Vorteil zu langen Abständen zwischen Shares und höherer Varianz.

Zwei Pool-Funktionen solltest du kennen:

- **Solo-Mining** funktioniert an jedem Port, wenn du `solo:` vor die Wallet-Adresse setzt. Findest du einen Block, erhältst du die ganze Blockbelohnung; sonst nichts. Bei Consumer-Hashrate musst du lange warten.
- **Nockchain-Merge-Mining** bringt NOCK zusätzlich zu PRL bei derselben Hashrate ein. Hänge `+NOCK_ADDRESS` an deine Pearl-Wallet-Adresse an. Der Pool zahlt NOCK auf Nockchain selbst aus, daher kann eine Adresse für einen Wrapped Token, die mit `0x` beginnt, ihn nicht empfangen. **Dein Miner muss Merge-Mining unterstützen. Ohne diese Funktion minest du Pearl weiterhin normal.**

Der Pool veröffentlicht `luckypool.io`-Hosts und `lproute.com`-Routen-Hosts. Wenn dein Netzwerk direkten Mining-Verkehr blockiert, behalte den Port und tausche die Domain aus.

## Ein funktionierendes Installationsskript

Das folgende Skript richtet SRBMiner auf einem Debian- oder Ubuntu-Rechner als systemd-Dienst ein. Es erkennt alle GPUs, setzt Übertaktungsoptionen je Karte, prüft den Download anhand der veröffentlichten MD5-Prüfsumme, schreibt die Unit und eine logrotate-Richtlinie und startet den Dienst neu.

```bash
#!/usr/bin/env bash
# install-pearl-miner.sh -- SRBMiner (Pearl / PRL) als systemd-Dienst einrichten.
# Ausführen: sudo bash install-pearl-miner.sh
set -euo pipefail

ALGO="pearlhash"
POOL="${POOL:-pearl-us-east.luckypool.io:3360}"
WALLET="${WALLET:-<YOUR_PR1_ADDRESS>}"   # prl1... für Merge-Mining +NOCK_ADDRESS ergänzen
WORKER="${WORKER:-rig-1}"
SRB_VERSION="${SRB_VERSION:-3.6.9}"
MINER_DIR="/opt/srbminer"
UNIT="/etc/systemd/system/pearl-miner.service"
SVC="pearl-miner.service"
LOG="/var/log/pearl-miner.log"

# Tuning für RTX-3070-Klasse. MCORE sperrt den Speichertakt deutlich unter dem
# Standardwert der Karte von 7001 MHz. Das ist bewusst ein Effizienz-Undertakt, kein
# Leistungs-Overclock. Setze einen Wert auf "", um die Option abzuschalten.
CCLOCK="${CCLOCK:-1560}"
MCLOCK="${MCLOCK:-5001}"
COFFSET="${COFFSET:-150}"
PLIMIT="${PLIMIT:-180}"
FAN="${FAN:-}"
THERMAL="${THERMAL:-88}"
```

Der Tuning-Block braucht eine Erklärung, weil er auf den ersten Blick falsch wirkt. **`MCORE=5001` liegt unter dem Standard-Speichertakt einer 3070.** Das ist beabsichtigt. Pearl belohnt Speichereffizienz, und ein niedrigerer Speichertakt senkt den Stromverbrauch stärker als die Hashrate. **Übernimm keine Übertaktungswerte aus einer Hashrate-Datenbank, ohne zu prüfen, mit welcher GPU der Eintrag gemessen wurde.** Oft stammt der Benchmark von einer anderen Karte.

```bash
[ "$(id -u)" -eq 0 ] || { echo "als root ausführen (sudo)"; exit 1; }
command -v nvidia-smi >/dev/null || { echo "nvidia-smi fehlt - installiere zuerst den Treiber"; exit 1; }

GPU_N=$(nvidia-smi --query-gpu=index --format=csv,noheader | wc -l)
echo "== $GPU_N NVIDIA-GPU(s) erkannt =="
nvidia-smi --query-gpu=index,name,memory.total,power.limit --format=csv,noheader

# Übertaktungsoptionen für jede erkannte GPU erstellen
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

# Version herunterladen und prüfen
STEM="SRBMiner-Multi-$(echo "$SRB_VERSION" | tr . -)-Linux"
BASE="https://github.com/doktor83/SRBMiner-Multi/releases/download/$SRB_VERSION"
TMP=$(mktemp -d); trap 'rm -rf "$TMP"' EXIT
curl -fsSL -o "$TMP/$STEM.tar.gz"  "$BASE/$STEM.tar.gz"
curl -fsSL -o "$TMP/$STEM.tar.md5" "$BASE/$STEM.tar.md5"
(cd "$TMP" && md5sum -c <(tr -d '\r' < "$STEM.tar.md5"))

# Dienst vor dem Austausch der Binärdatei stoppen: Er hält die Datei geöffnet
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

**Prüfe die MD5-Prüfsumme, bevor du eine Mining-Binärdatei startest.** Releases veröffentlichen Hashes je Datei, und ein Miner läuft mit Root-Rechten und liest die GPU aus. Ohne Prüfung vertraust du einem Download, den du nicht kontrolliert hast.

Zwei betriebliche Details in der Service-Unit:

```bash
cat >"$UNIT" <<EOF
[Unit]
Description=Pearl (PRL) SRBMiner-Version $SRB_VERSION - Worker $WORKER
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

- **`--disable-cpu`** hält den Miner von der CPU fern, was wichtig ist, wenn der Rechner noch andere Aufgaben erledigt.
- **`--shutdown-temperature 88`** stoppt den Miner bei einem Lüfterausfall, statt die Karte zu überhitzen.
- **`--gpu-reset-oc`** löscht frühere Takteinstellungen, bevor es deine setzt. So bleiben keine alten Werte aktiv.
- **`Restart=always` mit `RestartSec=10`** übersteht Treiberprobleme, die bei Rigs mit mehreren GPUs häufig auftreten.
- **`--api-enable` öffnet einen Überwachungsport.** Prüfe, an welche Schnittstelle Port 21550 gebunden ist, und stelle ihn nicht in ein nicht vertrauenswürdiges Netzwerk. Ein Rig-Monitor muss nicht von außerhalb erreichbar sein.

Richte zuletzt die Log-Rotation ein, denn Mining-Protokolle wachsen unbegrenzt:

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

*`copytruncate` ist hier wichtig. SRBMiner hält die Logdatei geöffnet. Benennt die Rotation die Datei um, schreibt der Miner in einen gelöschten Inode und die Festplatte füllt sich trotzdem.*

Verfolge den Fortschritt mit einem gefilterten Log-Auszug statt mit dem Rohprotokoll:

```bash
grep -aE 'Hashrate|accepted|Pool:' /var/log/pearl-miner.log | tail -20
```

## Probleme zwischen Juli und September 2026

**Eine Pearl-Mining-Anleitung muss mit den Problemen beginnen, denn sie wirken sich alle auf deine Auszahlung aus.** Zwischen Juli und September 2026 gingen vier Dinge schief.

### Der Markt hängt an einer Börse

Am **23. Juli 2026** erreichte PRL mit **0,1399 $** ein Allzeittief, nach etwa **87 Cent** im Juni. Der Kurs fiel an einem Tag um **24,2 %** und in einer Woche um **26,7 %**, während der übrige Kryptomarkt im selben Zeitraum rund 2 % gewann.

Der Grund waren keine Nachrichten. Es war die Markttiefe.

- **95,17 % des gemeldeten Handelsvolumens** entfielen auf **eine Börse namens SafeTrade**, die keinen CoinGecko-Vertrauenswert hat. Ein einzelnes PRL/USDT-Paar machte **738.399 von rund 775.000 $** Handelsvolumen in 24 Stunden aus.
- Beide SafeTrade-Paare meldeten eine **Orderbuchtiefe von 0,00 $**.

*Eine gewöhnliche Verkaufsorder bewegt einen solchen Markt um zweistellige Prozentsätze. Das ist eine strukturelle Eigenschaft des Tokens, kein vorübergehender Zustand.*

Die Angebotslage verstärkt das:

| Kennzahl | Wert |
|---|---|
| **Marktkapitalisierung** | 55,7 Millionen $ |
| **Vollständig verwässerte Bewertung** | 458,6 Millionen $ |
| **Verhältnis** | Mehr als 8× |
| **Umlaufmenge** | 255 Millionen von 2,1 Milliarden, unter **13 %** |

**Ein Token mit Preisbildung auf einem dünnen Orderbuch und 87 % gesperrtem oder noch nicht ausgegebenem Angebot hat eine große Spanne plausibler Preise.** Plane, was du mit Auszahlungen machst, und behandle den Spotpreis nicht als verlässliche Umsatzschätzung.

### Ein Auszahlungsdienst wurde kompromittiert

Ein am **18. September 2026** eröffneter Issue berichtet, dass Pearl Wallet 2.0.5 „nach dem Pool-Hack vor einem Monat weiterhin Senden und Empfangen ausgesetzt“ habe.

**Lies das zweimal, denn es enthält zwei Fakten.** Ein Pearl-Pool wurde etwa **im August 2026** kompromittiert, worauf die offizielle Wallet Überweisungen aussetzte. Einen Monat später galt die Sperre noch immer.

Der Pool, den du auswählst, verwahrt deine Auszahlung. Prüfe seine Vorfallshistorie, bevor du ein Rig darauf richtest.

### Die Projektwebsite ist nicht erreichbar

Zum Zeitpunkt der Erstellung **erreicht pearlresearch.ai keinen Server.** Alle öffentlichen Resolver liefern für die Apex-Domain und Subdomains wie `compute` und `explorer` eine Nullroute `0.0.0.0`. Die Domainregistrierung ist `ACTIVE`, also ist dies ein bewusster DNS-Zustand und kein Ablauf.

**Drei Links, auf die eine Mining-Anleitung normalerweise verweist, sind tot**, darunter der Block-Explorer. Mining Pool Stats führt sie weiterhin auf, sodass Leser einer Adresse nachgehen, die nie lädt.

Nutze stattdessen **[PRL-Block-Explorer](https://prlscan.com)** zur Blocksuche. Ich habe bestätigt, dass die Seite funktioniert.

### Das Programm weist weiterhin offene Fehler auf

Der öffentliche Issue-Tracker zeigt Ende September 2026 ungelöste Probleme. Das Erstellen von Issues ist eingeschränkt, daher ist dies nur ein Teilausschnitt.

| Issue | Datum | Bedeutung |
|---|---|---|
| **RPC-Code der Desktop-Wallet inaktiv** | 22. Sep. | Die Wallet erreicht keinen Node |
| **Testnet kann nicht von Grund auf synchronisieren**, Nodes bleiben auf Höhe 36760 hängen | 22. Sep. | Ein blockierender Fehler in der Synchronisierung |
| **Senden und Empfangen der Wallet nach Pool-Hack weiterhin ausgesetzt** | 18. Sep. | Überweisungen betroffen |
| **macOS-ARM64-Version hat ungültige Codesignatur** | 17. Sep. | Läuft nur mit Umgehung von Gatekeeper |
| **Prune-Modus verwirft Zertifikate zur Header-Prüfung** | 30. Aug. | Ein Validierungsfehler |
| **Node hängt endlos, wenn kein verbundener Peer als Synchronisierungskandidat infrage kommt** | 30. Aug. | Anfällige Synchronisierung |
| **pearl-gemm scheitert auf RTX 5070**; Hash-Kernel laufen, GEMM-Kernel nicht | 31. Aug. | Neueste Consumer-Karten werden nicht unterstützt |

*Der RTX-5070-Eintrag ist wichtig, wenn du dafür eine aktuelle Karte kaufen wolltest. Die neueste Consumer-Architektur funktionierte nicht mit dem offiziellen GEMM-Pfad.*

**Das bedeutet:** Die Mining-Software wird aktiv gepflegt, während die nutzerseitigen und marktbezogenen Ebenen schwach sind. SRBMiner veröffentlichte Version 3.6.9 mit großen Effizienzgewinnen am Tag, bevor die Wallet-Beschwerden auftauchten.

## Ist die Blockchain nützlich?

Diese Frage verdient eine sorgfältige Antwort, denn „nützliche Arbeit“ meint in den meisten Berichten zwei Dinge. **Sie beschreibt sowohl einen Konsensmechanismus als auch eine wirtschaftliche Behauptung, und die Antworten darauf unterscheiden sich deutlich.**

### Funktional nützlich: teilweise

**Die Blockchain läuft. Das Produkt darum herum funktioniert nicht vollständig.**

Was trägt:

- **Das Mainnet startete am 27. April 2026** und produziert seitdem Blöcke.
- **Der ganze Stack ist real:** ein Node, Wallet-Daemon, SPV-Light-Client, Zero-Knowledge-Beweissystem und GPU-Miner in einem Repository.
- **Die Basis ist auf Codeebene erprobt.** Node, Wallet und Light-Client stammen von **btcd**, **btcwallet** und **neutrino** ab, Bitcoin-Projekten mit jahrelangen Angriffstests.
- **Die Codebasis ist ein ernsthaftes Projekt.** 315 Sterne, 76 Forks, über 6.800 Commits und ein öffentlicher Tracker mit präzisen Fehlerberichten.
- **Das Mining funktioniert.** SRBMiner veröffentlichte 247 Versionen und optimierte `pearlhash` wiederholt. Mehrere Pools laufen. Merge-Mining mit Nockchain funktioniert.

Was nicht funktioniert:

- **Überweisungen in der offiziellen Wallet sind nach dem Pool-Hack ausgesetzt.**
- **Die Desktop-Wallet erreicht laut eigenem Tracker Ende September keinen Node.**
- **Die Synchronisierung hat blockierende Fehler** im Testnet- und Mainnet-Pfad.
- **Die Projektwebsite ist nicht erreichbar.**
- **Neueste Consumer-GPUs scheitern am GEMM-Pfad.**

**Die ehrliche Zusammenfassung: Pearl funktioniert auf Protokollebene und ist auf Produktebene unzuverlässig.** Wer Proof of Useful Work untersucht, sollte hinschauen. Wer zuverlässig minen und bezahlt werden will, sollte dies als Warnung verstehen.

### Technisch nützlich: Mechanismus ja, Marktplatz nein

Die ehrliche Antwort teilt sich in zwei Hälften. Viele Berichte liegen falsch, weil sie diese vermischen.

**Der Mechanismus ist tatsächlich neuartig.** Pearls NoisyGEMM-Routine berechnet verrauschte Matrixmultiplikationen auf einer GPU, hasht das Ergebnis zu einem Commitment und verpackt die Arbeit in einen Zero-Knowledge-Beweis, damit die Verifizierung günstig bleibt. Die Konstruktion beruht auf der echten Arbeit "Proofs of Useful Work from Arbitrary Matrix Multiplication" von Komargodski, Schen und Weinstein. Sie behauptet einen Mehraufwand von ungefähr **1 + o(1)** gegenüber naiver Matrixmultiplikation.

**Wenn die Schranke hält, sichert sich die Blockchain mit fast keinen Zusatzkosten über der eigentlichen Berechnung.** Das schafften frühere PoUW-Versuche nicht. Die Mathematik ist kein Schmuck.

**Der Marktplatz ist nicht etabliert.** Hashrate Index sagte dazu: „Heute ist der Großteil der nützlichen Arbeit Inferenz, die niemand gekauft hat. Damit besteht ein Großteil des Minings aus KI-artigem Proof of Work.“ Das ist eine faire Zusammenfassung. Die Berechnung passt, doch für den größten Teil zahlt niemand.

Die Ausnahme ist wichtig und real. Pearl schloss eine exklusive Partnerschaft mit **Together AI**, die einen vergünstigten Pearl-Inferenz-Endpunkt produktiv einsetzte. Das ist der erste Kunde und der Grund, warum das Projekt mehr Anerkennung verdient als die durchschnittliche KI-Kryptowährung.

**Ein Kunde ist ein Konzeptnachweis, kein Markt.**

### Praktisch nützlich: vorerst, bei kleiner werdendem Zeitfenster

Für Miner ist die praktische Lage gemischt und zeitlich begrenzt.

**Was für Pearl spricht:**

- Vorhandene GPUs bringen etwas ein, auch ältere, denn die Hardware-Anforderungen sind niedrig
- Laufende Effizienzverbesserungen erhöhen die Marge direkt auf bereits vorhandener Hardware
- Merge-Mining mit Nockchain ergänzt eine zweite Einnahmequelle bei gleicher Hashrate
- Nahezu kein Mehraufwand bedeutet, dass die Blockchain keinen Strom mit nutzlosem Hashing verbraucht

**Was dagegen spricht:**

- **Die Blockbelohnung sinkt planmäßig.** Das ist Bitcoins Modell, und die Emissionen gehen unabhängig vom Preis zurück.
- **Die Schwierigkeit steigt nur.** Die Einnahmen pro GPU kennen nur eine Richtung.
- **Die Liquidität ist gering.** Hashrate Index nennt es als Beobachtungspunkt, ob PRL auch außerhalb kleiner Börsen Liquidität gewinnt. Geringe Liquidität bedeutet größere Spreads und schlechtere Verkaufspreise.
- **Das Protokoll-Upgrade.** SRBMiners Versionshinweise zu 3.6.8 sagen, ein kommendes Pearl-Upgrade werde Consumer-GPUs „praktisch nutzlos“ machen. Nimm das ernst. Es stammt vom Entwickler, der davon profitiert, wenn weiter gemint wird.

## Das Fazit

**Pearl ist die bisher glaubwürdigste Implementierung von Proof of Useful Work, hat aber nicht bewiesen, dass die Arbeit wirtschaftlich nützlich ist.**

Vier Aussagen, nach Sicherheit geordnet:

1. **Der Konsensmechanismus funktioniert, und die kryptografische Behauptung ist echt.** Pearl löste das schwierige technische Problem, PoUW günstig verifizierbar zu machen. Das ist ein echter Beitrag, unabhängig vom Token.

2. **Die Rechenleistung ist ein Versprechen, kein Produkt.** Inferenz zu erzeugen ist nicht dasselbe wie sie zu verkaufen. Heute gibt es einen zahlenden Partner und ein Netzwerk voller spekulativer Hashrate. Der Kreislauf ist entworfen, aber er dreht sich nicht.

3. **Das Zeitfenster für Consumer-GPU-Mining wird enger, und das Protokoll wird es schließen.** Sinkende Belohnung, steigende Schwierigkeit, ein angekündigtes Upgrade gegen Consumer-Karten und eine Softfork, die manche Miner bereits bis zu 87,5 % kostete, ergeben eine befristete Chance statt einer Einnahmequelle.

4. **Das echte Risiko liegt im Betrieb und Markt, nicht in der Kryptografie.** Ein gehackter Pool, ausgesetzte Wallet-Überweisungen, eine unerreichbare Website, ungelöste Synchronisierungsfehler und 95 % des Volumens auf einer Börse ohne Orderbuchtiefe entscheiden über die Auszahlung. Das Protokoll ist der funktionierende Teil.

*Am treffendsten: Pearl hat das schwierige Problem gelöst, nicht aber das einfach klingende. Matrixmultiplikationen nachweislich nützlich zu machen, ist Kryptografie. Einen Käufer für das Ergebnis zu finden, ist Vertrieb.*

**Wenn du minen willst, betrachte es als kurzfristige Nutzung bereits vorhandener Hardware.** Kaufe keine GPUs für Pearl. Baue kein Rig in der Annahme, die aktuellen Zahlen hielten an. Emissionsplan und Versionshinweise des Miner-Entwicklers sagen das Gegenteil.

**Wenn du Proof of Useful Work verstehen willst, ist Pearl derzeit die wichtigste Implementierung zum Untersuchen.** Sie erreichte als erste echte Größenordnung. Die nächsten zwei Jahre werden zeigen, ob „nützliche Arbeit“ ein echtes Grundelement oder ein wiederkehrendes Scheitern mit besserer Kryptografie ist.

{{< figure src="pearl-prl-usefulness-assessment.webp" alt="Diagramm bewertet Pearls Proof of Useful Work in drei Bereichen: hoher funktionaler Reifegrad, starker technischer Mechanismus bei unbewiesenem zahlendem Markt und zeitlich begrenzte praktische Mining-Tauglichkeit" >}}

## Wichtigste Punkte

- **Pearl ist eine von Bitcoin abgeleitete L1 mit Proof of Useful Work.** Miner berechnen verrauschte Matrixmultiplikationen statt Hashes. Das Mainnet startete am **27. April 2026**.
- **Du kannst auf zwei Wegen minen:** SRBMiner mit `--algorithm pearlhash` über einen Pool oder Pearls `vllm-miner` an einem synchronisierten Node.
- **Die frühe Rentabilität kam aus der Emissionskurve zum Start**, nicht aus KI-Nachfrage. Der geschätzte Tagesumsatz einer RTX 5090 halbierte sich wenige Wochen nach dem Boom.
- **Effizientere Miner-Versionen glichen einen Teil des Rückgangs aus.** Version 3.6.9 lieferte dieselbe oder höhere Hashrate bei deutlich weniger Leistung.
- **Die Rank-Penalty-Softfork vom 6. August 2026 senkte die effektive Hashrate über Rang 128 um 50 bis 87,5 %.** Aktualisiere den Miner bei Regeländerungen.
- **Der Token wird im Wesentlichen auf einer Börse gehandelt.** SafeTrade hatte 95,17 % des Volumens und keine Orderbuchtiefe; weniger als 13 % des Angebots sind im Umlauf.
- **Ein Pool wurde etwa im August 2026 gehackt**, und die offizielle Wallet hielt Überweisungen noch einen Monat später zurück.
- **Die Projektwebsite löst nicht auf.** Nutze `prlscan.com` zur Blocksuche.
- **Optimiere Effizienz statt Taktfrequenz.** Pearl belohnt Speichereffizienz, und ein niedrigerer Speichertakt senkt den Stromverbrauch stärker als die Hashrate.
- **Nutze Port 3360 für eine einzelne Consumer-GPU** und hänge `+NOCK_ADDRESS` für Merge-Mining von Nockchain an.
- **Prüfe die MD5-Prüfsumme** jedes Miner-Downloads, bevor du ihn als root startest.
- **Mine mit bereits vorhandener Hardware.** Die Blockchain funktioniert auf Protokollebene, ist als Produkt unzuverlässig und hat nur einen Partner für bezahlte Rechenleistung.

## Nächste Schritte

1. **Lies das Quell-Repository** für Node, Wallet und offiziellen vLLM-Miner: **[Pearl-Repository von Pearl Research Labs](https://github.com/pearl-research-labs/pearl)**
2. **Prüfe das Änderungsprotokoll des Miners vor dem Tuning**, da sich Effizienz je Version ändert: **[SRBMiner-Multi-Versionen](https://github.com/doktor83/SRBMiner-Multi/releases)**
3. **Wähle einen Pool-Port** passend zur gemessenen Hashrate: **[LuckyPool für Pearl](https://pearl.luckypool.io)**
4. **Vergleiche die Hashrate-Verteilung der Pools** vor deiner Entscheidung: **[Mining-Pool-Statistiken - Pearl](https://miningpoolstats.stream/pearl)**
5. **Berechne zuerst deine Stromkosten**, denn sie entscheiden über die Rentabilität: **[Eine rentable Box für passives Einkommen bauen](/other/creating-profitable-low-powered-crypto-miners/)**
6. **Wende die Multi-GPU-Tuning-Regeln an** aus unserer anderen Anleitung zum Mining mit nützlicher Arbeit: **[Spacemesh effizient mit mehreren GPUs minen](/other/efficient-spacemesh-mining-multiple-gpus-guide/)**

## Verwandte Artikel

| Artikel | Inhalt |
|---|---|
| **[Spacemesh effizient mit mehreren GPUs minen](/other/efficient-spacemesh-mining-multiple-gpus-guide/)** | Multi-GPU-Tuning und Strommanagement bei einer anderen Blockchain mit nützlicher Arbeit |
| **[Eine rentable Box für passives Einkommen bauen](/other/creating-profitable-low-powered-crypto-miners/)** | Mining-Hardware vor dem Kauf am Strompreis ausrichten |
| **[Lokale KI 2026: Ein 27B-Modell schlägt Sonnet 4.6](/articles/local-ai-2026-build-your-rig-now/)** | Was dieselben GPUs bei lokaler Inferenz statt beim Mining leisten |
| **[Verus auf Android minen: Einfache Anleitung für Smartphone-Mining](/other/mine-verus-on-android-guide/)** | CPU-Mining auf vorhandener Hardware |

## Quellen

1. [Netzwerk-Monorepository von Pearl Research Labs](https://github.com/pearl-research-labs/pearl)
2. [Offene Issues im Pearl-Repository](https://github.com/pearl-research-labs/pearl/issues)
3. [Pearl (PRL): Wie Matrixmathematik zu KI-Rechenleistung und Mining wird - Hashrate Index](https://hashrateindex.com/blog/pearl-prl-ai-compute-cryptocurrency/)
4. [Rank-Penalty-Softfork im Pearl-(PRL)-Netzwerk aktiviert - Cryptoage](https://cryptoage.com/en/5400-rank-penalty-softfork-activated-on-the-pearl-prl-network.html)
5. [Pearl erreicht neues Allzeittief: 95 % des Volumens auf einer Börse ohne Orderbuchtiefe - CryptoNewsLive](https://www.cryptonewslive.org/article/pearl-hit-a-fresh-all-time-low-today-95-of-its-volume-sits-on-one-exchange-with-zero-order-book-depth)
6. [SRBMiner-Multi-Versionen - doktor83](https://github.com/doktor83/SRBMiner-Multi/releases)
7. [LuckyPool - Pearl- und Nock-Merge-Mining-Pool](https://pearl.luckypool.io)
8. [Mining-Pool-Statistiken - Pearl (PRL) PearlHash](https://miningpoolstats.stream/pearl)
9. [PRL-Block-Explorer prlscan.com](https://prlscan.com)

**Hinweis zur offiziellen Domain:** `pearlresearch.ai` sowie die Subdomains `compute` und `explorer` liefern zum Zeitpunkt der Erstellung eine Nullroute. Der Artikel lässt sie bewusst weg, statt tote Links zu veröffentlichen, und verweist zur Blocksuche auf `prlscan.com`.
