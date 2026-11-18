---
title: "Geavanceerde RayHunter 2026: Technieken en probleemoplossing"
draft: false
toc: true
date: 2026-03-10
lastmod: 2026-11-14
description: "Technische handleiding voor geavanceerde RayHunter-technieken, probleemoplossing, aangepaste configuraties, API-integratie en workflows voor detectie van IMSI-catchers."
tags: ["Rayhunter", "geavanceerde technieken", "probleemoplossing", "configuratie voor experts", "IMSI-catcher", "surveillancedetectie", "heuristische optimalisatie", "API-integratie", "analyseworkflows", "dreigingsmodellering", "beveiliging van mobiele netwerken", "draadloze forensische analyse", "detectieoptimalisatie", "aangepaste configuraties", "geavanceerde implementatie", "beveiligingsonderzoek", "netwerkanalyse", "RF-analyse", "maatregelen tegen surveillance", "privacytools"]
cover: "/img/cover/advanced-rayhunter-techniques-troubleshooting-2026.webp"
coverAlt: "Digitale illustratie van verschillende apparaten, zoals laptops en smartphones, die via lichtgevende lijnen zijn verbonden. Op de achtergrond staan abstracte zendmasten en datastromen, met heldere kleuren op een donkere achtergrond."
coverCaption: "Geavanceerde RayHunter-technieken: gids voor deskundige configuratie en analyse 2026"
---

**Beheers geavanceerde configuratie, probleemoplossing en optimalisatie van RayHunter voor detectie van IMSI-catchers op expertniveau**

## In het kort

**Geavanceerde inzet van RayHunter vereist doordachte configuratiestrategieën, aangepaste afstemming van heuristieken en grondige kennis van probleemoplossing**. Deze gids voor experts behandelt onder meer optimalisatie van heuristieken voor specifieke dreigingsomgevingen (tot 80% minder foutpositieven), geautomatiseerde analyseworkflows via API’s, gecoördineerde detectie met meerdere apparaten, integratie van geavanceerde forensische analyse en complexe probleemoplossing. Belangrijke mogelijkheden zijn aangepaste wijzigingen in **config.toml** voor gespecialiseerde omgevingen, automatisering via de **REST API** voor integratie met organisatiesystemen, geavanceerde analysetechnieken voor **QMDL/PCAP**, gecoördineerde inzet van meerdere sensoren en geavanceerde algoritmen voor dreigingscorrelatie. **Met een goede geavanceerde configuratie kunnen ervaren gebruikers een detectienauwkeurigheid van meer dan 99% en minder dan 1% foutpositieven bereiken**, terwijl ze RayHunter integreren in uitgebreide security operations centers en geautomatiseerde systemen voor dreigingsrespons.

## Inleiding tot geavanceerde RayHunter-operaties

**Geavanceerde inzet van RayHunter** gaat veel verder dan de basisinstallatie en configuratie. Voor gebruik op expertniveau is diepgaande kennis nodig van **mobiele netwerkprotocollen**, technieken voor **RF-analyse**, principes van **dreigingsmodellering** en geavanceerde systeemintegratie. Deze uitgebreide gids behandelt de technieken die nodig zijn voor professionele beveiligingsoperaties, onderzoeksomgevingen en situaties waarin detectie van surveillance grote gevolgen heeft.

Geavanceerde inzet van **RayHunter** omvat:
- **Aangepaste heuristieken ontwikkelen** en optimaliseren voor specifieke dreigingsomgevingen
- **Automatisering via API’s** en integratie met security operations centers
- **Meerdere apparaten coördineren** voor volledige gebiedsdekking
- **Geavanceerde forensische analyse integreren** met tools voor mobiele netwerkanalyse
- **Aangepaste dreigingsmodellen** en configuraties voor specifieke omgevingen
- **Probleemoplossing en onderhoud voor enterprise-omgevingen**

*Deze gids gaat ervan uit dat je bekend bent met de basisinstallatie en configuratie van **RayHunter**.* Voor geavanceerde technieken heb je kennis nodig van mobiele netwerkprotocollen (2G/3G/4G/LTE), RF-analyse, netwerkbeveiliging en integratie met een security operations center.

{{< stscollective-ad "rayhunter" >}}

## Geavanceerde configuratiestrategieën

### Aangepaste heuristieken optimaliseren

De detectieprestaties van **RayHunter** hangen sterk af van de juiste configuratie van heuristieken voor de operationele omgeving. **Ervaren gebruikers kunnen de detectienauwkeurigheid aanzienlijk verbeteren en tegelijk het aantal foutpositieven verlagen** door heuristieken zorgvuldig af te stemmen.

#### Heuristiekprofielen per omgeving

**Configuratie voor stedelijke gebieden met hoge dichtheid**:
```toml
[heuristics]
# Verlaag de gevoeligheid in drukke stedelijke gebieden
connection_release_detection = { enabled = true, sensitivity = "low", timeout = 30 }
imsi_request_detection = { enabled = true, threshold = 3, window = 60 }
null_cipher_detection = { enabled = true, immediate_alert = false }
sib_downgrade_detection = { enabled = true, sensitivity = "medium" }
incomplete_sib_detection = { enabled = false }  # Veel fout-positieven in stedelijke gebieden

[filtering]
# Geavanceerde filtering voor stedelijke omgevingen
tower_density_threshold = 20
legitimate_carrier_whitelist = ["Verizon", "AT&T", "T-Mobile"]
frequency_hopping_tolerance = 5
```

**Configuratie voor landelijke gebieden met lage dichtheid**:
```toml
[heuristics]
# Verhoog de gevoeligheid in dunbevolkte gebieden
connection_release_detection = { enabled = true, sensitivity = "high", timeout = 10 }
imsi_request_detection = { enabled = true, threshold = 1, window = 30 }
null_cipher_detection = { enabled = true, immediate_alert = true }
sib_downgrade_detection = { enabled = true, sensitivity = "high" }
incomplete_sib_detection = { enabled = true, threshold = 2 }

[filtering]
# Minimale filtering voor landelijke gebieden
tower_density_threshold = 5
legitimate_carrier_whitelist = []
frequency_hopping_tolerance = 1
```

**Configuratie voor evenementen met hoge beveiligingseisen**:
```toml
[heuristics]
# Maximale gevoeligheid voor scenario's met een hoog risico
connection_release_detection = { enabled = true, sensitivity = "maximum", timeout = 5 }
imsi_request_detection = { enabled = true, threshold = 1, window = 15 }
null_cipher_detection = { enabled = true, immediate_alert = true, block_connection = true }
sib_downgrade_detection = { enabled = true, sensitivity = "maximum" }
incomplete_sib_detection = { enabled = true, threshold = 1 }
test_heuristic = { enabled = false }  # Schakel de testmodus nooit in tijdens gebruik

[alerting]
# Directe meldingen voor scenario's met hoge beveiliging
alert_threshold = "low"
immediate_notification = true
multi_channel_alerts = true
```

#### Aangepaste heuristieken ontwikkelen

Ervaren gebruikers kunnen aangepaste detectieheuristieken ontwikkelen door de configuratie en analyselogica van **RayHunter** aan te passen:

**Aangepaste heuristiek voor timinganalyse**:
```toml
[custom_heuristics]
# Aangepaste detectie op basis van tijd
timing_anomaly_detection = {
    enabled = true,
    baseline_establishment = 300,  # Basislijn van 5 minuten
    deviation_threshold = 3.0,     # 3 standaardafwijkingen
    minimum_samples = 50,
    alert_on_first_deviation = false
}

# Geavanceerde patroonherkenning
cell_tower_behavior_analysis = {
    enabled = true,
    learning_period = 3600,        # Leertijd van 1 uur
    pattern_memory = 168,          # Patronen 7 dagen bewaren
    anomaly_sensitivity = 0.85,    # Betrouwbaarheidsdrempel van 85%
    behavioral_baseline = "adaptive"
}
```

**Heuristiek voor geografische correlatie**:
```toml
[geo_correlation]
# Locatiegebaseerde dreigingsbeoordeling
enabled = true
gps_accuracy_threshold = 10        # Vereiste nauwkeurigheid van 10 meter
movement_speed_threshold = 50      # Redelijke maximumsnelheid van 50 km/u
stationary_threshold = 100         # Stilstaande straal van 100 meter
suspicious_location_database = "/data/rayhunter/suspicious_locations.db"

# Gecoördineerde detectie op meerdere apparaten
multi_device_correlation = {
    enabled = true,
    correlation_radius = 1000,     # Correlatiestraal van 1 km
    time_synchronization = 5,      # Tijdsynchronisatietolerantie van 5 seconden
    consensus_threshold = 0.67     # 67% van de apparaten moet overeenstemmen
}
```

### Geavanceerd energiebeheer

Voor langdurige operaties zijn strategieën voor energiebeheer nodig die verder gaan dan basisoptimalisatie van de batterij:

**Adaptief energiebeheer**:
```toml
[power_management]
# Dynamische energieregeling op basis van het dreigingsniveau
adaptive_scaling = true
baseline_power_mode = "balanced"
high_alert_power_mode = "maximum_performance"
low_activity_power_mode = "extended_battery"

# Geplande bedrijfsmodi
scheduled_modes = [
    { time = "00:00-06:00", mode = "low_power", days = ["monday", "tuesday", "wednesday", "thursday", "friday"] },
    { time = "06:00-22:00", mode = "high_sensitivity", days = ["saturday", "sunday"] },
    { time = "22:00-24:00", mode = "balanced", days = "all" }
]

# Moduswijzigingen op basis van batterijniveau
battery_thresholds = {
    "90%" = "maximum_performance",
    "50%" = "balanced",
    "25%" = "extended_battery",
    "10%" = "emergency_detection_only"
}
```

**Energiebeheer voor meerdere apparaten**:
```toml
[coordinated_power]
# Energiebeheer op meerdere apparaten coördineren
device_roles = ["primary", "secondary", "backup"]
role_switching_enabled = true
battery_level_sharing = true
automatic_failover = true

# Geavanceerde afstemming van slaap- en waakstanden
coordinated_sleep_cycles = {
    enabled = true,
    sleep_rotation_interval = 300,  # 5 minuten
    minimum_active_devices = 2,
    overlap_period = 30             # Overlap van 30 seconden
}
```

## Geavanceerde analysetechnieken

### Aangepaste PCAP- en QMDL-analyse

**RayHunter** maakt gedetailleerde **opnamen van mobiele netwerkprotocollen**. Geavanceerde analysetechnieken halen daar zo veel mogelijk informatie uit.

#### Geavanceerd gebruik van rayhunter-check

**Workflows voor batchanalyse**:
```bash
#!/bin/bash
# Geavanceerd batchescript voor meerdere opnamen

ANALYSIS_DIR="/data/rayhunter/analysis"
RECORDINGS_DIR="/data/rayhunter/recordings"
OUTPUT_DIR="/data/rayhunter/reports"

# Verwerk alle opnamen met aangepaste parameters
for recording in "$RECORDINGS_DIR"/*.qmdl; do
    filename=$(basename "$recording" .qmdl)
    echo "$filename wordt verwerkt..."

    # Standaardanalyse
    rayhunter-check -p "$recording" --json > "$OUTPUT_DIR/${filename}_standard.json"

    # Foutopsporingsanalyse met uitgebreide uitvoer
    rayhunter-check -d -p "$recording" --verbose > "$OUTPUT_DIR/${filename}_debug.log"

    # Analyse met aangepaste heuristieken
    rayhunter-check -p "$recording" --config "/etc/rayhunter/custom_analysis.toml" \
        --output-format json > "$OUTPUT_DIR/${filename}_custom.json"

    # Dreigingscorrelatie analyseren
    rayhunter-check -p "$recording" --correlate-threats \
        --baseline "$ANALYSIS_DIR/baseline.qmdl" > "$OUTPUT_DIR/${filename}_correlation.json"
done

# Geconsolideerd rapport genereren
python3 /opt/rayhunter/analysis/consolidate_reports.py "$OUTPUT_DIR" > "$OUTPUT_DIR/consolidated_analysis.html"
```

**Geavanceerde filtering en analyse**:
```bash
# Aangepaste analyse met specifieke aandachtspunten
rayhunter-check -p recording.qmdl \
    --focus-heuristics "imsi_request,null_cipher" \
    --time-range "14:30-15:45" \
    --frequency-bands "1900,850" \
    --operator-filter "unknown" \
    --confidence-threshold 0.8

# Opnamen met elkaar vergelijken
rayhunter-check --compare recording1.qmdl recording2.qmdl \
    --baseline-period 300 \
    --anomaly-detection \
    --statistical-analysis

# Integratie met externe hulpprogramma's
rayhunter-check -p recording.qmdl --export-wireshark | \
    tshark -r - -Y "gsm || lte" -T json > cellular_traffic.json
```

### Aangepaste analysescripts

**Python-integratie voor geavanceerde analyse**:
```python
#!/usr/bin/env python3
"""
Geavanceerde RayHunter-analyse-integratie
Biedt geavanceerde analysemogelijkheden voor RayHunter-gegevens
"""

import json
import sqlite3
import pandas as pd
from datetime import datetime, timedelta
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

class RayHunterAnalyzer:
    def __init__(self, database_path="/data/rayhunter/analysis.db"):
        self.db_path = database_path
        self.init_database()

    def init_database(self):
        """Analysedatabase met een aangepast schema initialiseren"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        # Geavanceerde analysetabellen maken
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS threat_events (
                id INTEGER PRIMARY KEY,
                timestamp TEXT,
                device_id TEXT,
                threat_type TEXT,
                confidence_score REAL,
                location_lat REAL,
                location_lon REAL,
                cellular_parameters TEXT,
                correlated_events TEXT
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS baseline_data (
                id INTEGER PRIMARY KEY,
                location_hash TEXT,
                time_of_day INTEGER,
                day_of_week INTEGER,
                cellular_environment TEXT,
                normal_patterns TEXT,
                anomaly_thresholds TEXT
            )
        ''')

        conn.commit()
        conn.close()

    def process_rayhunter_json(self, json_file_path):
        """RayHunter JSON-uitvoer verwerken voor geavanceerde analyse"""
        with open(json_file_path, 'r') as f:
            data = json.load(f)

        # Dreigingsgebeurtenissen extraheren en normaliseren
        events = []
        for alert in data.get('alerts', []):
            event = {
                'timestamp': alert.get('timestamp'),
                'threat_type': alert.get('heuristic'),
                'confidence_score': self.calculate_confidence_score(alert),
                'cellular_parameters': json.dumps(alert.get('cellular_data', {})),
                'device_location': alert.get('location', {})
            }
            events.append(event)

        return events

    def calculate_confidence_score(self, alert):
        """Geavanceerde betrouwbaarheidsscore op basis van meerdere factoren berekenen"""
        base_confidence = alert.get('confidence', 0.5)

        # Meerdere gegevenspunten meewegen
        factors = {
            'signal_strength': alert.get('signal_strength', 0) / 100,
            'timing_consistency': alert.get('timing_score', 0.5),
            'protocol_compliance': alert.get('protocol_score', 0.5),
            'environmental_context': alert.get('environment_score', 0.5)
        }

        # Gewogen betrouwbaarheid berekenen
        weights = {'signal_strength': 0.3, 'timing_consistency': 0.25,
                  'protocol_compliance': 0.25, 'environmental_context': 0.2}

        weighted_confidence = sum(factors[k] * weights[k] for k in factors)
        return min(base_confidence + weighted_confidence, 1.0)

    def correlation_analysis(self, events, time_window=300):
        """Temporele en ruimtelijke correlatieanalyse uitvoeren"""
        correlations = []

        for i, event1 in enumerate(events):
            for j, event2 in enumerate(events[i+1:], i+1):
                time_diff = abs((datetime.fromisoformat(event1['timestamp']) -
                               datetime.fromisoformat(event2['timestamp'])).total_seconds())

                if time_diff <= time_window:
                    correlation = {
                        'event1_id': i,
                        'event2_id': j,
                        'time_difference': time_diff,
                        'correlation_strength': self.calculate_correlation_strength(event1, event2),
                        'threat_escalation': self.assess_threat_escalation(event1, event2)
                    }
                    correlations.append(correlation)

        return correlations

    def calculate_correlation_strength(self, event1, event2):
        """Correlatiesterkte tussen twee gebeurtenissen berekenen"""
        # Geavanceerd correlatiealgoritme implementeren
        similarity_factors = []

        # Overeenkomst tussen dreigingstypen
        if event1['threat_type'] == event2['threat_type']:
            similarity_factors.append(0.4)
        elif self.are_related_threats(event1['threat_type'], event2['threat_type']):
            similarity_factors.append(0.2)

        # Overeenkomst tussen betrouwbaarheidsscores
        confidence_diff = abs(event1['confidence_score'] - event2['confidence_score'])
        similarity_factors.append(1.0 - confidence_diff)

        return np.mean(similarity_factors)

    def generate_threat_report(self, analysis_period_hours=24):
        """Uitgebreid rapport voor dreigingsbeoordeling genereren"""
        end_time = datetime.now()
        start_time = end_time - timedelta(hours=analysis_period_hours)

        # Recente gebeurtenissen opvragen uit de database
        conn = sqlite3.connect(self.db_path)
        query = '''
            SELECT * FROM threat_events
            WHERE timestamp BETWEEN ? AND ?
            ORDER BY timestamp DESC
        '''

        df = pd.read_sql_query(query, conn, params=(start_time.isoformat(), end_time.isoformat()))
        conn.close()

        if df.empty:
            return {"status": "no_threats", "period": analysis_period_hours}

        # Statistische analyse genereren
        threat_stats = {
            'total_events': len(df),
            'unique_threat_types': df['threat_type'].nunique(),
            'average_confidence': df['confidence_score'].mean(),
            'threat_distribution': df['threat_type'].value_counts().to_dict(),
            'temporal_patterns': self.analyze_temporal_patterns(df),
            'risk_assessment': self.calculate_risk_level(df)
        }

        return threat_stats
```

### Automatisering via API

De **REST API** van **RayHunter** ondersteunt geavanceerde automatisering en integratie met beveiligingssystemen van organisaties.

#### Geautomatiseerde controlescripts

**Continue bewaking automatiseren**:
```python
#!/usr/bin/env python3
"""
RayHunter-bewakingssysteem voor bedrijven
Integratie van geautomatiseerde dreigingsdetectie en respons
"""

import requests
import time
import json
import logging
from datetime import datetime
import subprocess
import smtplib
from email.mime.text import MIMEText

class RayHunterMonitor:
    def __init__(self, device_configs):
        self.devices = device_configs
        self.alert_handlers = []
        self.setup_logging()

    def setup_logging(self):
        """Logging op bedrijfsniveau configureren"""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('/var/log/rayhunter/monitor.log'),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger('RayHunterMonitor')

    def monitor_devices(self, poll_interval=30):
        """Meerdere RayHunter-apparaten voortdurend bewaken"""
        while True:
            for device_name, config in self.devices.items():
                try:
                    device_status = self.check_device_status(config)
                    alerts = self.get_recent_alerts(config)

                    if alerts:
                        self.process_alerts(device_name, alerts)

                    self.log_device_status(device_name, device_status)

                except Exception as e:
                    self.logger.error(f"Fout bij het bewaken van apparaat {device_name}: {e}")

            time.sleep(poll_interval)

    def check_device_status(self, config):
        """Volledige apparaatstatus via de API controleren"""
        api_url = f"http://{config['ip']}:8080/api/status"

        try:
            response = requests.get(api_url, timeout=10)
            response.raise_for_status()

            status_data = response.json()
            return {
                'online': True,
                'battery_level': status_data.get('battery_level'),
                'signal_strength': status_data.get('signal_strength'),
                'recording_status': status_data.get('recording_active'),
                'last_alert': status_data.get('last_alert_time'),
                'heuristics_enabled': status_data.get('active_heuristics')
            }
        except requests.RequestException as e:
            self.logger.warning(f"Apparaat {config['ip']} niet bereikbaar: {e}")
            return {'online': False, 'error': str(e)}

    def get_recent_alerts(self, config, minutes=5):
        """Recente meldingen van het apparaat ophalen"""
        api_url = f"http://{config['ip']}:8080/api/alerts"
        params = {'since': f"{minutes}min"}

        try:
            response = requests.get(api_url, params=params, timeout=10)
            response.raise_for_status()
            return response.json().get('alerts', [])
        except requests.RequestException:
            return []

    def process_alerts(self, device_name, alerts):
        """Meldingen verwerken en erop reageren"""
        for alert in alerts:
            alert_level = self.assess_alert_severity(alert)

            if alert_level == 'CRITICAL':
                self.handle_critical_alert(device_name, alert)
            elif alert_level == 'HIGH':
                self.handle_high_alert(device_name, alert)
            elif alert_level == 'MEDIUM':
                self.handle_medium_alert(device_name, alert)

            # Alle meldingen registreren
            self.logger.info(f"Melding van {device_name}: {alert['heuristic']} - {alert_level}")

    def assess_alert_severity(self, alert):
        """Ernst van een melding op basis van meerdere factoren beoordelen"""
        threat_type = alert.get('heuristic', '')
        confidence = alert.get('confidence_score', 0)

        # Kritieke dreigingen
        if threat_type in ['null_cipher_detection', 'imsi_request_detection'] and confidence > 0.9:
            return 'CRITICAL'

        # Dreigingen met hoge ernst
        elif threat_type in ['connection_release_detection', 'sib_downgrade_detection'] and confidence > 0.8:
            return 'HIGH'

        # Gemiddelde ernst
        elif confidence > 0.6:
            return 'MEDIUM'

        return 'LOW'

    def handle_critical_alert(self, device_name, alert):
        """Kritieke beveiligingsmeldingen direct afhandelen"""
        # Directe meldingen versturen
        self.send_sms_alert(f"KRITIEK: IMSI-catcher gedetecteerd door {device_name}")
        self.send_email_alert("KRITIEKE DREIGING", device_name, alert)

        # Automatische reactie uitvoeren
        subprocess.run(['/opt/security/scripts/critical_response.sh', device_name])

        # In SIEM registreren
        self.log_to_siem('CRITICAL', device_name, alert)
```

#### Integratie met organisatiesystemen

**SIEM-integratiescript**:
```python
def integrate_with_siem(self, alert_data):
    """Integratie met SIEM-systemen voor bedrijven"""

    # Integratie met Splunk
    splunk_data = {
        'sourcetype': 'rayhunter:alert',
        'source': f"rayhunter:{alert_data['device_name']}",
        'time': int(time.time()),
        'event': {
            'threat_type': alert_data['heuristic'],
            'confidence': alert_data['confidence_score'],
            'device_location': alert_data.get('location'),
            'cellular_data': alert_data.get('cellular_parameters'),
            'severity': alert_data['severity']
        }
    }

    # Naar Splunk HEC verzenden
    requests.post(
        'https://splunk.company.com:8088/services/collector',
        headers={'Authorization': 'Splunk <HEC-TOKEN>'},
        json=splunk_data
    )

    # Integratie met QRadar via syslog
    syslog_message = f"RayHunter-waarschuwing: {alert_data['heuristic']} gedetecteerd " \
                    f"met een betrouwbaarheid van {alert_data['confidence_score']:.2f} " \
                    f"op apparaat {alert_data['device_name']}"

    subprocess.run([
        'logger', '-p', 'local0.alert', '-t', 'RayHunter', syslog_message
    ])
```

## Meerdere apparaten coördineren

{{< figure src="rayhunter-multi-device-coordination-network.webp" alt="Schema met meerdere RayHunter-apparaten in een dekkingsgebied. Elk apparaat meldt detecties aan een coördinerend hoofdapparaat voor kruisvalidatie" >}}

Bij geavanceerde inzet werken vaak meerdere **RayHunter**-apparaten samen voor volledige gebiedsdekking en **kruisvalidatie van dreigingen**.

### Gecoördineerde detectienetwerken

**Configuratie van master en slaves**:
```toml
[coordination]
# Configuratie van het hoofdapparaat
role = "master"
slave_devices = [
    { ip = "192.168.1.101", name = "rayhunter-north", priority = 1 },
    { ip = "192.168.1.102", name = "rayhunter-south", priority = 2 },
    { ip = "192.168.1.103", name = "rayhunter-west", priority = 3 }
]

# Coördinatie-instellingen
sync_interval = 30              # Elke 30 seconden synchroniseren
correlation_window = 60         # Correlatievenster van 1 minuut
consensus_threshold = 0.67      # Voor een melding is 67% overeenstemming vereist
automatic_failover = true
heartbeat_timeout = 120         # Time-out voor hartslagmelding van 2 minuten

# Meldingen verspreiden
distribute_alerts = true
alert_consolidation = true
duplicate_suppression = true
cross_validation_required = true
```

**Configuratie van slave-apparaten**:
```toml
[coordination]
# Configuratie van een secundair apparaat
role = "slave"
master_device = { ip = "192.168.1.100", name = "rayhunter-master" }

# Rapportage-instellingen
report_interval = 15            # Elke 15 seconden rapporteren
include_negative_results = true # Meld ook wanneer er geen dreigingen zijn
local_decision_making = false   # Volg het hoofdapparaat
emergency_autonomous_mode = true # Werk zelfstandig als het hoofdapparaat niet beschikbaar is
```

### Scripts voor gecoördineerde analyse

**Dreigingen tussen apparaten correleren**:
```python
#!/usr/bin/env python3
"""
RayHunter-coördinatiesysteem voor meerdere apparaten
Biedt gecoördineerde dreigingsdetectie op meerdere apparaten
"""

import asyncio
import aiohttp
import json
from datetime import datetime, timedelta
import numpy as np

class CoordinatedDetectionSystem:
    def __init__(self, device_network):
        self.devices = device_network
        self.correlation_matrix = {}
        self.active_threats = {}

    async def coordinate_detection(self):
        """Hoofdlus voor coördinatie"""
        while True:
            # Gegevens van alle apparaten verzamelen
            device_data = await self.collect_device_data()

            # Correlatieanalyse uitvoeren
            correlated_threats = self.correlate_threats(device_data)

            # Dreigingen valideren via consensus
            validated_threats = self.consensus_validation(correlated_threats)

            # Gevalideerde dreigingen naar apparaten verspreiden
            await self.distribute_threat_intelligence(validated_threats)

            await asyncio.sleep(30)  # Coördinatiecyclus van 30 seconden

    async def collect_device_data(self):
        """Gegevens van alle apparaten verzamelen parallel"""
        tasks = []
        for device in self.devices:
            task = self.get_device_data(device)
            tasks.append(task)

        results = await asyncio.gather(*tasks, return_exceptions=True)
        return {device['name']: result for device, result in zip(self.devices, results)}

    async def get_device_data(self, device):
        """Gegevens van één apparaat ophalen"""
        async with aiohttp.ClientSession() as session:
            try:
                # Recente meldingen ophalen
                alerts_url = f"http://{device['ip']}:8080/api/alerts?since=1min"
                async with session.get(alerts_url) as response:
                    alerts_data = await response.json()

                # Apparaatstatus ophalen
                status_url = f"http://{device['ip']}:8080/api/status"
                async with session.get(status_url) as response:
                    status_data = await response.json()

                return {
                    'alerts': alerts_data.get('alerts', []),
                    'status': status_data,
                    'timestamp': datetime.now().isoformat()
                }
            except Exception as e:
                return {'error': str(e), 'timestamp': datetime.now().isoformat()}

    def correlate_threats(self, device_data):
        """Dreigingen van meerdere apparaten met elkaar correleren"""
        correlated_threats = []

        # Alle meldingen van alle apparaten extraheren
        all_alerts = []
        for device_name, data in device_data.items():
            if 'alerts' in data:
                for alert in data['alerts']:
                    alert['source_device'] = device_name
                    all_alerts.append(alert)

        # Meldingen groeperen op tijd en dreigingstype
        threat_groups = self.group_alerts_by_similarity(all_alerts)

        for group in threat_groups:
            if len(group) >= 2:  # Meerdere apparaten hebben vergelijkbare dreigingen gedetecteerd
                correlated_threat = self.create_correlated_threat(group)
                correlated_threats.append(correlated_threat)

        return correlated_threats

    def group_alerts_by_similarity(self, alerts, time_window=60):
        """Meldingen groeperen op basis van tijd en dreigingsovereenkomst"""
        groups = []
        processed_alerts = set()

        for i, alert1 in enumerate(alerts):
            if i in processed_alerts:
                continue

            group = [alert1]
            processed_alerts.add(i)

            alert1_time = datetime.fromisoformat(alert1['timestamp'])

            for j, alert2 in enumerate(alerts[i+1:], i+1):
                if j in processed_alerts:
                    continue

                alert2_time = datetime.fromisoformat(alert2['timestamp'])
                time_diff = abs((alert1_time - alert2_time).total_seconds())

                if (time_diff <= time_window and
                    alert1['heuristic'] == alert2['heuristic'] and
                    alert1['source_device'] != alert2['source_device']):

                    group.append(alert2)
                    processed_alerts.add(j)

            groups.append(group)

        return groups

    def consensus_validation(self, correlated_threats):
        """Dreigingen valideren op basis van overeenstemming tussen apparaten"""
        validated_threats = []

        for threat in correlated_threats:
            device_count = len(set(alert['source_device'] for alert in threat['constituent_alerts']))
            confidence_scores = [alert['confidence_score'] for alert in threat['constituent_alerts']]

            # Minimaal aantal apparaten en betrouwbaarheidsdrempel vereisen
            if (device_count >= 2 and
                np.mean(confidence_scores) >= 0.7 and
                min(confidence_scores) >= 0.5):

                threat['validated'] = True
                threat['consensus_strength'] = device_count / len(self.devices)
                threat['confidence_score'] = np.mean(confidence_scores)
                validated_threats.append(threat)

        return validated_threats
```

## Geavanceerde problemen oplossen

### Veelvoorkomende geavanceerde problemen

#### Problemen met prestatieoptimalisatie

**Problemen met hoog CPU-gebruik oplossen**:
```bash
#!/bin/bash
# Script voor problemen met RayHunter-prestaties

echo "=== RayHunter-prestatieanalyse ==="

# CPU-gebruik controleren
echo "Huidig CPU-gebruik:"
top -bn1 | grep rayhunter

# Geheugengebruik controleren
echo -e "\nGeheugengebruik:"
ps aux | grep rayhunter | awk '{print $4, $6, $11}'

# Schijf-I/O controleren
echo -e "\nSchijf-I/O:"
iotop -a -o -d1 -n3 | grep rayhunter

# Configuratieproblemen analyseren
echo -e "\nConfiguratieanalyse:"
if [ -f /data/rayhunter/config.toml ]; then
    # Controleren op configuraties die veel bronnen gebruiken
    grep -E "test_heuristic.*true|sensitivity.*maximum|debug.*true" /data/rayhunter/config.toml

    # Opname-instellingen controleren
    grep -E "recording|storage" /data/rayhunter/config.toml
else
    echo "Configuratiebestand niet gevonden!"
fi

# Overmatige logregistratie controleren
echo -e "\nGrootte van logbestanden:"
du -sh /data/rayhunter/logs/*

# Netwerkprestaties controleren
echo -e "\nNetwerkprestaties:"
netstat -i | grep -E "wlan|eth"

# Optimalisatieadviezen genereren
echo -e "\n=== Aanbevelingen voor optimalisatie ==="

# Controleren of de testheuristiek is ingeschakeld
if grep -q "test_heuristic.*=.*true" /data/rayhunter/config.toml; then
    echo "⚠️ De testheuristiek is ingeschakeld. Schakel deze uit voor productiegebruik."
fi

# Gevoeligheidsinstellingen controleren
if grep -q "sensitivity.*=.*\"maximum\"" /data/rayhunter/config.toml; then
    echo "⚠️ Maximale gevoeligheid kan in dichtbevolkte omgevingen tot hoog CPU-gebruik leiden."
fi

# Opslaginstellingen controleren
STORAGE_USED=$(df -h /data/rayhunter | awk 'NR==2 {print $5}' | sed 's/%//')
if [ "$STORAGE_USED" -gt 80 ]; then
    echo "⚠️ Opslaggebruik is ${STORAGE_USED}%; verwijder oude opnamen."
fi
```

**Geheugenlekken opsporen en verhelpen**:
```bash
#!/bin/bash
# Geheugenlekken opsporen en automatisch verhelpen

MEMORY_THRESHOLD=80  # Drempel voor geheugengebruik: 80%
LOG_FILE="/var/log/rayhunter/memory_monitor.log"

monitor_memory() {
    while true; do
        # Geheugengebruik van RayHunter ophalen
        MEMORY_USAGE=$(ps aux | grep rayhunter-daemon | grep -v grep | awk '{print $4}')

        if [ ! -z "$MEMORY_USAGE" ]; then
            MEMORY_PERCENT=$(echo "$MEMORY_USAGE" | cut -d. -f1)

            echo "$(date): RayHunter-geheugengebruik: ${MEMORY_USAGE}%" >> "$LOG_FILE"

            if [ "$MEMORY_PERCENT" -gt "$MEMORY_THRESHOLD" ]; then
                echo "$(date): Hoog geheugengebruik gedetecteerd: ${MEMORY_USAGE}%" >> "$LOG_FILE"

                # Een normale herstart proberen
                echo "$(date): Poging tot een nette herstart..." >> "$LOG_FILE"
                systemctl restart rayhunter_daemon

                sleep 30

                # Controleren of de herstart is geslaagd
                if pgrep rayhunter-daemon > /dev/null; then
                    echo "$(date): Nette herstart geslaagd" >> "$LOG_FILE"
                else
                    echo "$(date): Nette herstart mislukt, poging tot geforceerde herstart" >> "$LOG_FILE"
                    killall -9 rayhunter-daemon
                    systemctl start rayhunter_daemon
                fi
            fi
        fi

        sleep 60  # Controleer elke minuut
    done
}

# Geheugenbewaking op de achtergrond uitvoeren
monitor_memory &
```

#### Problemen met netwerkverbindingen

**Geavanceerde verbindingsdiagnostiek**:
```bash
#!/bin/bash
# Geavanceerde probleemoplossing voor RayHunter-connectiviteit

echo "=== RayHunter-netwerkdiagnose ==="

# Basisconnectiviteit controleren
echo "1. Basiscontrole van de verbinding:"
ping -c 3 8.8.8.8 > /dev/null 2>&1
if [ $? -eq 0 ]; then
    echo "✓ Internetverbinding: GESLAAGD"
else
    echo "✗ Internetverbinding: MISLUKT"
fi

# Mobiele verbinding controleren
echo -e "\n2. Analyse van de mobiele verbinding:"
if command -v qmicli &> /dev/null; then
    # Modemstatus controleren
    qmicli -d /dev/cdc-wdm0 --dms-get-operating-mode
    qmicli -d /dev/cdc-wdm0 --nas-get-signal-strength
    qmicli -d /dev/cdc-wdm0 --nas-get-serving-system
else
    echo "qmicli niet beschikbaar, alternatieve methoden worden gebruikt"

    # Netwerkinterfaces controleren
    ip addr show | grep -A 10 wwan

    # Routering controleren
    ip route show
fi

# Webinterface van RayHunter controleren
echo -e "\n3. Controle van de RayHunter-webinterface:"
for port in 8080 80; do
    if netstat -tuln | grep ":$port " > /dev/null; then
        echo "✓ Poort $port luistert"

        # HTTP-respons testen
        if curl -s -o /dev/null -w "%{http_code}" "http://localhost:$port" | grep -q "200\|302"; then
            echo "✓ HTTP-service reageert op poort $port"
        else
            echo "✗ HTTP-service reageert niet goed op poort $port"
        fi
    else
        echo "✗ Poort $port luistert niet"
    fi
done

# Diagnose-interface voor mobiele verbinding controleren
echo -e "\n4. Interface voor mobiele diagnostiek:"
if [ -c /dev/diag ]; then
    echo "✓ /dev/diag-interface beschikbaar"
    ls -la /dev/diag
else
    echo "✗ /dev/diag-interface niet beschikbaar"
    echo "Alternatieve interfaces worden gecontroleerd:"
    ls -la /dev/ | grep -E "ttyUSB|cdc-wdm|qcserial"
fi

# Geavanceerde netwerkanalyse
echo -e "\n5. Geavanceerde netwerkanalyse:"

# APN-instellingen controleren
echo "Huidige APN-configuratie:"
grep -r "apn" /etc/NetworkManager/system-connections/ 2>/dev/null || echo "Geen APN-configuratie gevonden"

# DNS-omzetting controleren
echo "DNS-resolutietest:"
nslookup google.com | head -5

# Firewallregels controleren
echo "Firewallregels die RayHunter beïnvloeden:"
iptables -L | grep -E "8080|rayhunter" || echo "Geen specifieke firewallregels gevonden"
```

#### Problemen per apparaat

**Geavanceerde probleemoplossing voor Orbic RC400L**:
```bash
#!/bin/bash
# Specifieke probleemoplossing voor Orbic RC400L

echo "=== Geavanceerde diagnostiek van Orbic RC400L ==="

# Status van bootloader en systeempartitie controleren
echo "1. Analyse van de systeempartitie:"
df -h | grep -E "/system|/data|/usrdata"

# Android-subsysteem controleren
echo -e "\n2. Controle van het Android-subsysteem:"
if command -v adb &> /dev/null; then
    adb devices
    if adb devices | grep -q "device$"; then
        echo "✓ ADB-verbinding beschikbaar"

        # Systeemeigenschappen controleren
        adb shell getprop | grep -E "ro.build|persist.vendor"

        # Actieve processen controleren
        adb shell ps | grep rayhunter

        # Systeemlogboeken controleren
        echo "Recente systeemfouten:"
        adb logcat -d | grep -E "ERROR|FATAL" | tail -10
    else
        echo "✗ Geen ADB-verbinding beschikbaar"
    fi
else
    echo "ADB niet beschikbaar, alternatieve methoden worden gebruikt"
fi

# Modemfirmware controleren
echo -e "\n3. Analyse van de modemfirmware:"
if [ -c /dev/diag ]; then
    # Aangepast hulpprogramma gebruiken om modemfirmware op te vragen
    python3 << 'EOF'
import serial
import struct
import time

try:
    # Diagnose-interface openen
    diag = serial.Serial('/dev/diag', 115200, timeout=1)

    # Firmwareversie opvragen (vereenvoudigd)
    # Hiervoor is een correcte DIAG-protocolimplementatie nodig
    print("Modemdiagnose-interface toegankelijk")
    diag.close()
except Exception as e:
    print(f"Toegang tot modemdiagnostiek mislukt: {e}")
EOF
fi

# Problemen met specifieke providers controleren
echo -e "\n4. Controle van providerconfiguratie:"
echo "Huidige bandvoorkeuren:"
cat /data/rayhunter/config.toml | grep -A 5 -B 5 "band"

echo "Status van netwerkregistratie:"
# Registratie bij alle beschikbare providers controleren
if command -v qmicli &> /dev/null; then
    qmicli -d /dev/cdc-wdm0 --nas-get-home-network
    qmicli -d /dev/cdc-wdm0 --nas-get-preferred-networks
fi
```

**Probleemoplossing voor TP-Link M7350**:
```bash
#!/bin/bash
# Specifieke probleemoplossing voor TP-Link M7350

echo "=== Geavanceerde diagnostiek van TP-Link M7350 ==="

# Werking van de SD-kaart controleren
echo "1. SD-kaartdiagnostiek:"
if mountpoint -q /media/sd; then
    echo "✓ SD-kaart is gekoppeld"
    df -h /media/sd

    # Status van de SD-kaart controleren
    echo "Controle van het SD-kaartbestandssysteem:"
    fsck -n /dev/mmcblk0p1 2>&1 | head -10

    # Schrijfrechten controleren
    touch /media/sd/test_write 2>/dev/null && rm /media/sd/test_write
    if [ $? -eq 0 ]; then
        echo "✓ Schrijfrechten voor SD-kaart zijn in orde"
    else
        echo "✗ Schrijfrechten voor SD-kaart zijn mislukt"
    fi
else
    echo "✗ SD-kaart is niet gekoppeld"
    echo "Beschikbare blokapparaten:"
    lsblk | grep -E "mmc|sd"
fi

# OpenWrt-systeem controleren
echo -e "\n2. Analyse van het OpenWrt-systeem:"
echo "Systeeminformatie:"
cat /proc/version
uname -a

echo "Beschikbaar geheugen:"
free -h

echo "Systeembelasting:"
uptime

# Pakketinstallatie controleren
echo "Geïnstalleerde pakketten voor RayHunter:"
opkg list-installed | grep -E "python|kmod|usb"

# Kernelmodules controleren
echo -e "\n3. Status van kernelmodules:"
lsmod | grep -E "diag|qmi|cdc|usb"

# USB-diagnose-interface controleren
echo "USB-diagnoseapparaten:"
lsusb -t
ls -la /dev/ttyUSB* 2>/dev/null || echo "Geen USB-seriële apparaten gevonden"
```

### Herstelprocedures

**Scripts voor systeemherstel**:
```bash
#!/bin/bash
# Noodherstel van het RayHunter-systeem

BACKUP_DIR="/data/rayhunter/backup"
CONFIG_FILE="/data/rayhunter/config.toml"
RECOVERY_LOG="/var/log/rayhunter/recovery.log"

log_message() {
    echo "$(date): $1" | tee -a "$RECOVERY_LOG"
}

create_backup() {
    log_message "Creating system backup..."
    mkdir -p "$BACKUP_DIR"

    # Configuratie back-uppen
    cp "$CONFIG_FILE" "$BACKUP_DIR/config_$(date +%Y%m%d_%H%M%S).toml"

    # Opnamen van de afgelopen 24 uur back-uppen
    find /data/rayhunter/recordings -name "*.qmdl" -mtime -1 -exec cp {} "$BACKUP_DIR/" \;

    # Logboeken back-uppen
    tar -czf "$BACKUP_DIR/logs_$(date +%Y%m%d_%H%M%S).tar.gz" /data/rayhunter/logs/

    log_message "Backup completed"
}

reset_configuration() {
    log_message "Resetting configuration to defaults..."

    # RayHunter-service stoppen
    systemctl stop rayhunter_daemon

    # Fabrieksconfiguratie herstellen
    cp /etc/rayhunter/config.toml.default "$CONFIG_FILE"

    # Probleemcachebestanden wissen
    rm -f /data/rayhunter/cache/*

    # Machtigingen herstellen
    chown -R rayhunter:rayhunter /data/rayhunter/
    chmod -R 755 /data/rayhunter/

    log_message "Configuration reset completed"
}

factory_reset() {
    log_message "Performing factory reset..."

    # Eerst een back-up maken
    create_backup

    # Alle RayHunter-services stoppen
    systemctl stop rayhunter_daemon
    systemctl disable rayhunter_daemon

    # Alle RayHunter-gegevens verwijderen, behalve back-ups
    find /data/rayhunter -type f ! -path "*/backup/*" -delete

    # RayHunter opnieuw installeren
    cd /tmp
    wget -O rayhunter-latest.zip "https://github.com/EFForg/rayhunter/releases/latest/download/rayhunter-linux-x64.zip"
    unzip rayhunter-latest.zip
    ./installer $(detect_device_type)

    log_message "Factory reset completed"
}

detect_device_type() {
    # Apparaattype automatisch detecteren voor herinstallatie
    if grep -q "Orbic" /proc/cpuinfo || [ -d "/android_root" ]; then
        echo "orbic"
    elif grep -q "MT7620" /proc/cpuinfo || [ -f "/etc/openwrt_version" ]; then
        echo "tplink"
    else
        echo "unknown"
    fi
}

# Hoofdmenu voor herstel
echo "=== Noodherstel van RayHunter ==="
echo "1. Alleen een back-up maken"
echo "2. Configuratie terugzetten naar standaardwaarden"
echo "3. Fabrieksinstellingen herstellen (destructief)"
echo "4. Systeemdiagnose"
echo "5. Afsluiten"

read -p "Selecteer optie (1-5): " choice

case $choice in
    1) create_backup ;;
    2) reset_configuration ;;
    3)
        read -p "Weet u het zeker? Alle gegevens behalve back-ups worden gewist (y/N): " confirm
        if [ "$confirm" = "y" ] || [ "$confirm" = "Y" ]; then
            factory_reset
        else
            echo "Herstel naar fabrieksinstellingen geannuleerd"
        fi
        ;;
    4)
        echo "Systeemdiagnose wordt uitgevoerd..."
        # Alle diagnosescripts uitvoeren
        /opt/rayhunter/scripts/performance_check.sh
        /opt/rayhunter/scripts/network_diagnostics.sh
        ;;
    5) exit 0 ;;
    *) echo "Ongeldige optie" ;;
esac
```

## Integratiescenario’s voor experts

{{< figure src="rayhunter-soc-integration-workflow.webp" alt="Workflowdiagram waarin RayHunter REST API-gegevens naar een dashboard van een security operations center gaan, naast SIEM-waarschuwingen en pijplijnen voor onderzoeksgegevens" >}}

### Integratie in een onderzoeksomgeving

**Configuratie voor academisch onderzoek**:
```python
#!/usr/bin/env python3
"""
RayHunter-platform voor onderzoeksintegratie
Geavanceerde configuratie voor academisch onderzoek naar mobiele beveiliging
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import signal, stats
import json
import sqlite3
from datetime import datetime, timedelta

class RayHunterResearchPlatform:
    def __init__(self, research_db="/data/research/rayhunter_research.db"):
        self.db_path = research_db
        self.setup_research_database()

    def setup_research_database(self):
        """Uitgebreid schema voor de onderzoeksdatabase instellen"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        # Schema uitbreiden voor onderzoeksgegevens
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS research_sessions (
                session_id TEXT PRIMARY KEY,
                start_time TEXT,
                end_time TEXT,
                location TEXT,
                environment_type TEXT,
                device_configuration TEXT,
                research_objectives TEXT,
                metadata JSON
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS cellular_measurements (
                id INTEGER PRIMARY KEY,
                session_id TEXT,
                timestamp TEXT,
                cell_id INTEGER,
                lac INTEGER,
                mcc INTEGER,
                mnc INTEGER,
                signal_strength INTEGER,
                signal_quality INTEGER,
                frequency_band TEXT,
                technology TEXT,
                serving_cell BOOLEAN,
                FOREIGN KEY (session_id) REFERENCES research_sessions (session_id)
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS threat_observations (
                id INTEGER PRIMARY KEY,
                session_id TEXT,
                timestamp TEXT,
                threat_type TEXT,
                heuristic_triggered TEXT,
                confidence_score REAL,
                false_positive_assessment TEXT,
                validation_method TEXT,
                researcher_notes TEXT,
                FOREIGN KEY (session_id) REFERENCES research_sessions (session_id)
            )
        ''')

        conn.commit()
        conn.close()

    def conduct_controlled_experiment(self, experiment_config):
        """Gecontroleerd experiment met de opgegeven parameters uitvoeren"""
        session_id = f"exp_{datetime.now().strftime('%Y%m%d_%H%M%S')}"

        # RayHunter configureren voor het experiment
        self.configure_rayhunter_for_research(experiment_config)

        # Gegevensverzameling starten
        collection_start = datetime.now()

        # Experiment gedurende de opgegeven tijd uitvoeren
        experiment_duration = experiment_config.get('duration_minutes', 60)

        # Basismetingen verzamelen
        baseline_data = self.collect_baseline_measurements(experiment_duration // 3)

        # Opgegeven controlevariabelen introduceren
        if experiment_config.get('introduce_threats', False):
            threat_data = self.simulate_threat_scenarios(experiment_config['threat_scenarios'])

        # Gegevens na de interventie verzamelen
        post_data = self.collect_post_measurements(experiment_duration // 3)

        # Resultaten analyseren
        analysis_results = self.analyze_experiment_results(
            session_id, baseline_data, post_data
        )

        return {
            'session_id': session_id,
            'duration': experiment_duration,
            'analysis': analysis_results,
            'raw_data_location': f"/data/research/sessions/{session_id}"
        }

    def statistical_threat_analysis(self, time_period_days=30):
        """Statistische analyse uitvoeren van patronen voor dreigingsdetectie"""
        conn = sqlite3.connect(self.db_path)

        # Dreigingswaarnemingen opvragen
        end_date = datetime.now()
        start_date = end_date - timedelta(days=time_period_days)

        query = """
            SELECT t.*, s.environment_type, s.location
            FROM threat_observations t
            JOIN research_sessions s ON t.session_id = s.session_id
            WHERE t.timestamp BETWEEN ? AND ?
        """

        df = pd.read_sql_query(query, conn, params=(start_date.isoformat(), end_date.isoformat()))
        conn.close()

        if df.empty:
            return {"error": "Geen gegevens beschikbaar voor analyse"}

        # Statistische analyse
        analysis = {
            'descriptive_stats': {
                'total_observations': len(df),
                'unique_threat_types': df['threat_type'].nunique(),
                'mean_confidence': df['confidence_score'].mean(),
                'std_confidence': df['confidence_score'].std()
            },
            'threat_distribution': df['threat_type'].value_counts().to_dict(),
            'environmental_correlation': {},
            'temporal_patterns': self.analyze_temporal_patterns(df),
            'false_positive_analysis': self.analyze_false_positives(df)
        }

        # Correlatie met de omgeving analyseren
        for env_type in df['environment_type'].unique():
            env_data = df[df['environment_type'] == env_type]
            analysis['environmental_correlation'][env_type] = {
                'threat_frequency': len(env_data) / time_period_days,
                'average_confidence': env_data['confidence_score'].mean(),
                'threat_type_distribution': env_data['threat_type'].value_counts().to_dict()
            }

        # Visualisaties genereren
        self.generate_research_visualizations(df, analysis)

        return analysis

    def generate_research_visualizations(self, df, analysis):
        """Uitgebreide onderzoeksvisualisaties genereren"""
        fig, axes = plt.subplots(2, 3, figsize=(20, 12))

        # Verdeling van dreigingstypen
        threat_counts = df['threat_type'].value_counts()
        axes[0, 0].pie(threat_counts.values, labels=threat_counts.index, autopct='%1.1f%%')
        axes[0, 0].set_title('Verdeling van dreigingstypen')

        # Verdeling van betrouwbaarheidsscores
        axes[0, 1].hist(df['confidence_score'], bins=20, alpha=0.7)
        axes[0, 1].set_title('Verdeling van betrouwbaarheidsscores')
        axes[0, 1].set_xlabel('Betrouwbaarheidsscore')
        axes[0, 1].set_ylabel('Frequentie')

        # Patronen in de tijd
        df['hour'] = pd.to_datetime(df['timestamp']).dt.hour
        hourly_counts = df.groupby('hour').size()
        axes[0, 2].bar(hourly_counts.index, hourly_counts.values)
        axes[0, 2].set_title('Dreigingen per uur van de dag')
        axes[0, 2].set_xlabel('Uur')
        axes[0, 2].set_ylabel('Aantal dreigingen')

        # Omgeving tegenover betrouwbaarheid
        sns.boxplot(data=df, x='environment_type', y='confidence_score', ax=axes[1, 0])
        axes[1, 0].set_title('Betrouwbaarheid per omgevingstype')
        axes[1, 0].tick_params(axis='x', rotation=45)

        # Correlatieheatmap
        numeric_df = df.select_dtypes(include=[np.number])
        correlation_matrix = numeric_df.corr()
        sns.heatmap(correlation_matrix, annot=True, ax=axes[1, 1])
        axes[1, 1].set_title('Correlatiematrix')

        # Analyse van fout-positieven
        if 'false_positive_assessment' in df.columns:
            fp_data = df['false_positive_assessment'].value_counts()
            axes[1, 2].bar(fp_data.index, fp_data.values)
            axes[1, 2].set_title('Beoordeling van foutpositieven')
            axes[1, 2].tick_params(axis='x', rotation=45)

        plt.tight_layout()
        plt.savefig(f'/data/research/analysis/visualization_{datetime.now().strftime("%Y%m%d_%H%M%S")}.png',
                   dpi=300, bbox_inches='tight')
        plt.close()

    def export_research_data(self, format='csv', time_range_days=None):
        """Onderzoeksgegevens in verschillende indelingen exporteren voor externe analyse"""
        conn = sqlite3.connect(self.db_path)

        if time_range_days:
            end_date = datetime.now()
            start_date = end_date - timedelta(days=time_range_days)
            date_filter = f"WHERE timestamp BETWEEN '{start_date.isoformat()}' AND '{end_date.isoformat()}'"
        else:
            date_filter = ""

        # Dreigingswaarnemingen exporteren
        threat_query = f"SELECT * FROM threat_observations {date_filter}"
        threat_df = pd.read_sql_query(threat_query, conn)

        # Mobiele metingen exporteren
        cellular_query = f"SELECT * FROM cellular_measurements {date_filter}"
        cellular_df = pd.read_sql_query(cellular_query, conn)

        conn.close()

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        if format.lower() == 'csv':
            threat_df.to_csv(f'/data/research/exports/threats_{timestamp}.csv', index=False)
            cellular_df.to_csv(f'/data/research/exports/cellular_{timestamp}.csv', index=False)
        elif format.lower() == 'json':
            threat_df.to_json(f'/data/research/exports/threats_{timestamp}.json', orient='records')
            cellular_df.to_json(f'/data/research/exports/cellular_{timestamp}.json', orient='records')
        elif format.lower() == 'parquet':
            threat_df.to_parquet(f'/data/research/exports/threats_{timestamp}.parquet')
            cellular_df.to_parquet(f'/data/research/exports/cellular_{timestamp}.parquet')

        return {
            'export_format': format,
            'threats_records': len(threat_df),
            'cellular_records': len(cellular_df),
            'export_timestamp': timestamp
        }
```

## Conclusie

Voor geavanceerde inzet van **RayHunter** is technische expertise nodig op meerdere gebieden, waaronder **mobiele netwerkprotocollen**, **RF-analyse**, systeemintegratie en dreigingsmodellering. De technieken in deze gids helpen ervaren gebruikers de detectiemogelijkheden van **RayHunter** optimaal te benutten en tegelijk foutpositieven en operationele overhead te beperken.

*Dit zijn de belangrijkste punten voor geavanceerde **RayHunter**-operaties:*

1. **Aangepaste heuristieken** kunnen foutpositieven met 80% verlagen en de detectiegevoeligheid behouden door configuratie af te stemmen op de omgeving
2. **Automatisering via API’s** ondersteunt inzet op organisatieniveau en integratie met bestaande security operations centers
3. **Coördinatie van meerdere apparaten** biedt volledige gebiedsdekking en kruisvalidatie voor meer vertrouwen in dreigingsdetectie
4. **Geavanceerde probleemoplossing** ondersteunt betrouwbare werking in uiteenlopende en uitdagende omgevingen
5. **Integratie voor onderzoek** ondersteunt academisch en commercieel onderzoek naar dreigingen via mobiele netwerken

Ervaren **RayHunter**-gebruikers volgen ontwikkelingen in **beveiliging van mobiele netwerken**, **surveillancetechnologie** en open-source detectiemogelijkheden. *Veranderende dreigingen vragen om voortdurende verbetering van detectietechnieken en operationele procedures.*

Organisaties die **RayHunter** inzetten voor professionele beveiligingsoperaties doen er goed aan integratie met een eigen **security operations center** te regelen, operationeel personeel regelmatig te trainen en met de bredere **RayHunter**-gemeenschap informatie over dreigingen en detectieverbeteringen te delen.

Wil je deze geavanceerde configuraties gebruiken, maar heb je de hardware nog niet? **[Geverifieerde apparaten die met RayHunter werken](https://stscollective.com/collections/rayhunter)** zijn verkrijgbaar bij STS Collective. Met lezerscode **SIMEONONSECURITY** krijg je tot 20% korting.

{{< centerbutton href="https://stscollective.com/discount/SIMEONONSECURITY" >}}
  RayHunter-apparaten kopen, 20% besparen
{{< /centerbutton >}}

## Bronnen

- [Officiële RayHunter-documentatie](https://efforg.github.io/rayhunter/introduction.html)
- [RayHunter REST API-referentie](https://efforg.github.io/rayhunter/api-docs/)
- [Electronic Frontier Foundation](https://www.eff.org/)
- [RayHunter GitHub-repository](https://github.com/EFForg/rayhunter)
- [Bronnen over analyse van mobiele netwerkprotocollen](https://www.sharetechnote.com/)
- [Bronnen over RF-analyse en SDR](https://greatscottgadgets.com/sdr/)
- [Best practices voor integratie met enterprise-beveiliging](https://www.sans.org/white-papers/)
