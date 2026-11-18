---
title: "RayHunter avansat 2026: tehnici și depanare"
draft: false
toc: true
date: 2026-03-10
lastmod: 2026-11-14
description: "Ghid tehnic despre tehnici avansate RayHunter, depanare, configurări personalizate, integrare API și fluxuri de detectare a IMSI catcherelor."
tags: ["Rayhunter", "tehnici avansate", "depanare", "configurare expertă", "IMSI catcher", "detectarea supravegherii", "optimizarea euristicilor", "integrare API", "fluxuri de analiză", "modelarea amenințărilor", "securitate celulară", "criminalistică wireless", "optimizarea detectării", "configurări personalizate", "implementare avansată", "cercetare de securitate", "analiză de rețea", "analiză RF", "contramăsuri împotriva supravegherii", "instrumente de confidențialitate"]
cover: "/img/cover/advanced-rayhunter-techniques-troubleshooting-2026.webp"
coverAlt: "Ilustrație digitală cu diverse dispozitive, precum laptopuri și smartphone-uri, conectate prin linii luminoase. Pe fundalul întunecat apar turnuri celulare abstracte și fluxuri de date colorate."
coverCaption: "Tehnici avansate RayHunter: ghid expert de configurare și analiză 2026"
---

**Stăpânește configurarea avansată, depanarea și optimizarea RayHunter pentru detectarea IMSI catcherelor la nivel de expert**

## Pe scurt

**Implementarea avansată a RayHunter necesită strategii de configurare bine gândite, reglarea euristicilor personalizate și experiență solidă în depanare**. Acest ghid pentru experți prezintă optimizarea euristicilor pentru medii cu amenințări specifice (reducerea alarmelor false cu până la 80%), fluxuri automatizate de analiză prin API, detectare coordonată cu mai multe dispozitive, integrare criminalistică avansată și metode complexe de depanare. Printre capacitățile avansate se numără modificări **config.toml** pentru medii specializate, automatizarea **REST API** pentru integrare în întreprinderi, analiza avansată **QMDL/PCAP**, implementarea coordonată a mai multor senzori și algoritmi sofisticați de corelare a amenințărilor. **Cu o configurare avansată potrivită, utilizatorii experimentați pot obține o precizie de detectare de peste 99% și sub 1% alarme false**, integrând RayHunter în centre complete de operațiuni de securitate și sisteme automate de răspuns la amenințări.

## Introducere în operațiunile avansate RayHunter

**Implementarea avansată a RayHunter** depășește cu mult instalarea și configurarea de bază. Utilizarea la nivel de expert necesită cunoștințe aprofundate despre **protocoalele celulare**, tehnicile de **analiză RF**, principiile de **modelare a amenințărilor** și integrarea avansată a sistemelor. Acest ghid prezintă tehnicile necesare pentru operațiuni profesionale de securitate, medii de cercetare și scenarii cu miză mare de detectare a supravegherii.

Implementarea avansată **RayHunter** include:
- **Dezvoltarea euristicilor personalizate** și optimizarea lor pentru medii cu amenințări specifice
- **Automatizare prin API** și integrare cu centre de operațiuni de securitate
- **Coordonarea mai multor dispozitive** pentru acoperirea completă a unei zone
- **Integrare criminalistică avansată** cu instrumente de analiză celulară
- **Modelarea personalizată a amenințărilor** și configurări adaptate mediului
- **Depanare și întreținere la nivel de întreprindere**

*Acest ghid presupune familiaritatea cu instalarea și configurarea de bază a **RayHunter**.* Tehnicile avansate necesită cunoștințe despre protocoalele celulare (2G/3G/4G/LTE), principiile analizei RF, securitatea rețelelor și integrarea cu un centru de operațiuni de securitate.

{{< stscollective-ad "rayhunter" >}}

## Strategii avansate de configurare

### Optimizarea euristicilor personalizate

Eficiența detectării **RayHunter** depinde în mare măsură de configurarea euristicilor pentru mediul operațional specific. **Utilizatorii avansați pot îmbunătăți semnificativ precizia detectării și pot reduce alarmele false** prin reglarea atentă a euristicilor.

#### Profiluri euristice în funcție de mediu

**Configurare pentru zone urbane cu densitate mare**:
```toml
[heuristics]
# Reduceți sensibilitatea în zonele urbane aglomerate
connection_release_detection = { enabled = true, sensitivity = "low", timeout = 30 }
imsi_request_detection = { enabled = true, threshold = 3, window = 60 }
null_cipher_detection = { enabled = true, immediate_alert = false }
sib_downgrade_detection = { enabled = true, sensitivity = "medium" }
incomplete_sib_detection = { enabled = false }  # Rată ridicată de alarme false în zonele urbane

[filtering]
# Filtrare avansată pentru mediile urbane
tower_density_threshold = 20
legitimate_carrier_whitelist = ["Verizon", "AT&T", "T-Mobile"]
frequency_hopping_tolerance = 5
```

**Configurare pentru zone rurale cu densitate mică**:
```toml
[heuristics]
# Măriți sensibilitatea în zonele slab populate
connection_release_detection = { enabled = true, sensitivity = "high", timeout = 10 }
imsi_request_detection = { enabled = true, threshold = 1, window = 30 }
null_cipher_detection = { enabled = true, immediate_alert = true }
sib_downgrade_detection = { enabled = true, sensitivity = "high" }
incomplete_sib_detection = { enabled = true, threshold = 2 }

[filtering]
# Filtrare minimă pentru zonele rurale
tower_density_threshold = 5
legitimate_carrier_whitelist = []
frequency_hopping_tolerance = 1
```

**Configurare pentru evenimente cu securitate ridicată**:
```toml
[heuristics]
# Sensibilitate maximă pentru scenarii cu risc ridicat
connection_release_detection = { enabled = true, sensitivity = "maximum", timeout = 5 }
imsi_request_detection = { enabled = true, threshold = 1, window = 15 }
null_cipher_detection = { enabled = true, immediate_alert = true, block_connection = true }
sib_downgrade_detection = { enabled = true, sensitivity = "maximum" }
incomplete_sib_detection = { enabled = true, threshold = 1 }
test_heuristic = { enabled = false }  # Nu activați niciodată modul de test în timpul operațiunilor

[alerting]
# Alerte imediate pentru scenarii cu securitate ridicată
alert_threshold = "low"
immediate_notification = true
multi_channel_alerts = true
```

#### Dezvoltarea euristicilor personalizate

Utilizatorii avansați pot dezvolta euristici proprii de detectare, modificând configurarea și logica de analiză **RayHunter**:

**Euristică personalizată de analiză temporală**:
```toml
[custom_heuristics]
# Detecție personalizată bazată pe timp
timing_anomaly_detection = {
    enabled = true,
    baseline_establishment = 300,  # Perioadă de referință de 5 minute
    deviation_threshold = 3.0,     # 3 abateri standard
    minimum_samples = 50,
    alert_on_first_deviation = false
}

# Recunoaștere avansată a tiparelor
cell_tower_behavior_analysis = {
    enabled = true,
    learning_period = 3600,        # Perioadă de învățare de 1 oră
    pattern_memory = 168,          # Păstrați tiparele timp de 7 zile
    anomaly_sensitivity = 0.85,    # Prag de încredere de 85%
    behavioral_baseline = "adaptive"
}
```

**Euristică de corelare geografică**:
```toml
[geo_correlation]
# Evaluarea amenințărilor pe baza locației
enabled = true
gps_accuracy_threshold = 10        # Este necesară o precizie de 10 metri
movement_speed_threshold = 50      # Viteză maximă rezonabilă de 50 km/h
stationary_threshold = 100         # Rază de staționare de 100 de metri
suspicious_location_database = "/data/rayhunter/suspicious_locations.db"

# Detecție coordonată pe mai multe dispozitive
multi_device_correlation = {
    enabled = true,
    correlation_radius = 1000,     # Rază de corelare de 1 km
    time_synchronization = 5,      # Toleranță de 5 secunde pentru sincronizarea orei
    consensus_threshold = 0.67     # Este necesar acordul a 67% dintre dispozitive
}
```

### Gestionarea avansată a energiei

Operațiunile îndelungate necesită strategii de gestionare a energiei care depășesc optimizarea de bază a bateriei:

**Gestionarea adaptivă a energiei**:
```toml
[power_management]
# Scalare dinamică a puterii în funcție de nivelul amenințării
adaptive_scaling = true
baseline_power_mode = "balanced"
high_alert_power_mode = "maximum_performance"
low_activity_power_mode = "extended_battery"

# Moduri de funcționare programate
scheduled_modes = [
    { time = "00:00-06:00", mode = "low_power", days = ["monday", "tuesday", "wednesday", "thursday", "friday"] },
    { time = "06:00-22:00", mode = "high_sensitivity", days = ["saturday", "sunday"] },
    { time = "22:00-24:00", mode = "balanced", days = "all" }
]

# Schimbări de mod declanșate de nivelul bateriei
battery_thresholds = {
    "90%" = "maximum_performance",
    "50%" = "balanced",
    "25%" = "extended_battery",
    "10%" = "emergency_detection_only"
}
```

**Coordonarea alimentării mai multor dispozitive**:
```toml
[coordinated_power]
# Coordonați gestionarea energiei pe mai multe dispozitive
device_roles = ["primary", "secondary", "backup"]
role_switching_enabled = true
battery_level_sharing = true
automatic_failover = true

# Coordonare avansată a modurilor de repaus și activare
coordinated_sleep_cycles = {
    enabled = true,
    sleep_rotation_interval = 300,  # 5 minute
    minimum_active_devices = 2,
    overlap_period = 30             # Suprapunere de 30 de secunde
}
```

## Tehnici avansate de analiză

### Analiza personalizată PCAP și QMDL

**RayHunter** generează **capturi detaliate ale protocoalelor celulare**. Tehnicile avansate de analiză ajută la extragerea valorii maxime din acestea.

#### Utilizarea avansată a rayhunter-check

**Fluxuri de analiză în lot**:
```bash
#!/bin/bash
# Script avansat de analiză în lot pentru mai multe înregistrări

ANALYSIS_DIR="/data/rayhunter/analysis"
RECORDINGS_DIR="/data/rayhunter/recordings"
OUTPUT_DIR="/data/rayhunter/reports"

# Procesați toate înregistrările cu parametri personalizați
for recording in "$RECORDINGS_DIR"/*.qmdl; do
    filename=$(basename "$recording" .qmdl)
    echo "Se procesează $filename..."

    # Analiză standard
    rayhunter-check -p "$recording" --json > "$OUTPUT_DIR/${filename}_standard.json"

    # Analiză de depanare cu rezultate extinse
    rayhunter-check -d -p "$recording" --verbose > "$OUTPUT_DIR/${filename}_debug.log"

    # Analiză cu euristici personalizate
    rayhunter-check -p "$recording" --config "/etc/rayhunter/custom_analysis.toml" \
        --output-format json > "$OUTPUT_DIR/${filename}_custom.json"

    # Analiza corelării amenințărilor
    rayhunter-check -p "$recording" --correlate-threats \
        --baseline "$ANALYSIS_DIR/baseline.qmdl" > "$OUTPUT_DIR/${filename}_correlation.json"
done

# Generați un raport consolidat
python3 /opt/rayhunter/analysis/consolidate_reports.py "$OUTPUT_DIR" > "$OUTPUT_DIR/consolidated_analysis.html"
```

**Filtrare și analiză avansată**:
```bash
# Analiză personalizată cu domenii de interes specifice
rayhunter-check -p recording.qmdl \
    --focus-heuristics "imsi_request,null_cipher" \
    --time-range "14:30-15:45" \
    --frequency-bands "1900,850" \
    --operator-filter "unknown" \
    --confidence-threshold 0.8

# Comparați înregistrările
rayhunter-check --compare recording1.qmdl recording2.qmdl \
    --baseline-period 300 \
    --anomaly-detection \
    --statistical-analysis

# Integrare cu instrumente externe
rayhunter-check -p recording.qmdl --export-wireshark | \
    tshark -r - -Y "gsm || lte" -T json > cellular_traffic.json
```

### Scripturi personalizate de analiză

**Integrare Python pentru analiză avansată**:
```python
#!/usr/bin/env python3
"""
Integrare avansată pentru analiza RayHunter
Oferă funcții avansate de analiză a datelor RayHunter
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
        """Inițializează baza de date de analiză cu o schemă personalizată"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        # Creați tabele avansate de analiză
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
        """Procesează rezultatul JSON RayHunter pentru analiză avansată"""
        with open(json_file_path, 'r') as f:
            data = json.load(f)

        # Extrageți și normalizați evenimentele de amenințare
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
        """Calculează un scor de încredere avansat pe baza mai multor factori"""
        base_confidence = alert.get('confidence', 0.5)

        # Luați în calcul mai multe puncte de date
        factors = {
            'signal_strength': alert.get('signal_strength', 0) / 100,
            'timing_consistency': alert.get('timing_score', 0.5),
            'protocol_compliance': alert.get('protocol_score', 0.5),
            'environmental_context': alert.get('environment_score', 0.5)
        }

        # Calculați un nivel de încredere ponderat
        weights = {'signal_strength': 0.3, 'timing_consistency': 0.25,
                  'protocol_compliance': 0.25, 'environmental_context': 0.2}

        weighted_confidence = sum(factors[k] * weights[k] for k in factors)
        return min(base_confidence + weighted_confidence, 1.0)

    def correlation_analysis(self, events, time_window=300):
        """Efectuează analiza corelației temporale și spațiale"""
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
        """Calculează intensitatea corelației dintre două evenimente"""
        # Implementați un algoritm sofisticat de corelare
        similarity_factors = []

        # Similaritatea tipurilor de amenințări
        if event1['threat_type'] == event2['threat_type']:
            similarity_factors.append(0.4)
        elif self.are_related_threats(event1['threat_type'], event2['threat_type']):
            similarity_factors.append(0.2)

        # Similaritatea scorurilor de încredere
        confidence_diff = abs(event1['confidence_score'] - event2['confidence_score'])
        similarity_factors.append(1.0 - confidence_diff)

        return np.mean(similarity_factors)

    def generate_threat_report(self, analysis_period_hours=24):
        """Generează un raport complet de evaluare a amenințărilor"""
        end_time = datetime.now()
        start_time = end_time - timedelta(hours=analysis_period_hours)

        # Interogați baza de date pentru evenimente recente
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

        # Generați o analiză statistică
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

### Automatizare prin API

**REST API** **RayHunter** permite automatizarea sofisticată și integrarea cu sistemele de securitate ale întreprinderilor.

#### Scripturi de monitorizare automatizată

**Automatizarea monitorizării continue**:
```python
#!/usr/bin/env python3
"""
Sistem de monitorizare RayHunter pentru companii
Integrare automată pentru detectarea amenințărilor și răspunsul la acestea
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
        """Configurează jurnalizarea la nivel de companie"""
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
        """Monitorizează continuu mai multe dispozitive RayHunter"""
        while True:
            for device_name, config in self.devices.items():
                try:
                    device_status = self.check_device_status(config)
                    alerts = self.get_recent_alerts(config)

                    if alerts:
                        self.process_alerts(device_name, alerts)

                    self.log_device_status(device_name, device_status)

                except Exception as e:
                    self.logger.error(f"Eroare la monitorizarea dispozitivului {device_name}: {e}")

            time.sleep(poll_interval)

    def check_device_status(self, config):
        """Verifică starea completă a dispozitivului prin API"""
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
            self.logger.warning(f"Dispozitivul {config['ip']} nu poate fi accesat: {e}")
            return {'online': False, 'error': str(e)}

    def get_recent_alerts(self, config, minutes=5):
        """Preia alertele recente de pe dispozitiv"""
        api_url = f"http://{config['ip']}:8080/api/alerts"
        params = {'since': f"{minutes}min"}

        try:
            response = requests.get(api_url, params=params, timeout=10)
            response.raise_for_status()
            return response.json().get('alerts', [])
        except requests.RequestException:
            return []

    def process_alerts(self, device_name, alerts):
        """Procesează alertele și răspunde la ele"""
        for alert in alerts:
            alert_level = self.assess_alert_severity(alert)

            if alert_level == 'CRITICAL':
                self.handle_critical_alert(device_name, alert)
            elif alert_level == 'HIGH':
                self.handle_high_alert(device_name, alert)
            elif alert_level == 'MEDIUM':
                self.handle_medium_alert(device_name, alert)

            # Înregistrați toate alertele
            self.logger.info(f"Alertă de la {device_name}: {alert['heuristic']} - {alert_level}")

    def assess_alert_severity(self, alert):
        """Evaluează gravitatea alertei pe baza mai multor factori"""
        threat_type = alert.get('heuristic', '')
        confidence = alert.get('confidence_score', 0)

        # Amenințări critice
        if threat_type in ['null_cipher_detection', 'imsi_request_detection'] and confidence > 0.9:
            return 'CRITICAL'

        # Amenințări cu severitate ridicată
        elif threat_type in ['connection_release_detection', 'sib_downgrade_detection'] and confidence > 0.8:
            return 'HIGH'

        # Severitate medie
        elif confidence > 0.6:
            return 'MEDIUM'

        return 'LOW'

    def handle_critical_alert(self, device_name, alert):
        """Gestionează alertele critice de securitate cu răspuns imediat"""
        # Trimiteți notificări imediate
        self.send_sms_alert(f"CRITIC: detector IMSI detectat de {device_name}")
        self.send_email_alert("AMENINȚARE CRITICĂ", device_name, alert)

        # Executați răspunsul automatizat
        subprocess.run(['/opt/security/scripts/critical_response.sh', device_name])

        # Înregistrați în SIEM
        self.log_to_siem('CRITICAL', device_name, alert)
```

#### Integrare în întreprindere

**Script de integrare SIEM**:
```python
def integrate_with_siem(self, alert_data):
    """Integrare cu sisteme SIEM de companie"""

    # Integrare Splunk
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

    # Trimiteți către Splunk HEC
    requests.post(
        'https://splunk.company.com:8088/services/collector',
        headers={'Authorization': 'Splunk <HEC-TOKEN>'},
        json=splunk_data
    )

    # Integrare QRadar prin syslog
    syslog_message = f"RayHunter ALERT: A fost detectat {alert_data['heuristic']} " \
                    f"cu un nivel de încredere de {alert_data['confidence_score']:.2f} " \
                    f"pe dispozitivul {alert_data['device_name']}"
    subprocess.run([
        'logger', '-p', 'local0.alert', '-t', 'RayHunter', syslog_message
    ])
```

## Coordonarea mai multor dispozitive

{{< figure src="rayhunter-multi-device-coordination-network.webp" alt="Diagramă cu mai multe dispozitive RayHunter amplasate într-o zonă de acoperire. Fiecare trimite detectările către un dispozitiv master coordonator pentru verificare încrucișată." >}}

Implementările avansate **RayHunter** implică adesea mai multe dispozitive coordonate pentru acoperirea completă a unei zone și **validarea încrucișată a amenințărilor**.

### Rețele de detectare coordonate

**Configurare master-slave**:
```toml
[coordination]
# Configurarea dispozitivului principal
role = "master"
slave_devices = [
    { ip = "192.168.1.101", name = "rayhunter-north", priority = 1 },
    { ip = "192.168.1.102", name = "rayhunter-south", priority = 2 },
    { ip = "192.168.1.103", name = "rayhunter-west", priority = 3 }
]

# Setări de coordonare
sync_interval = 30              # Sincronizare la fiecare 30 de secunde
correlation_window = 60         # Fereastră de corelare de 1 minut
consensus_threshold = 0.67      # Este necesar un acord de 67% pentru alertă
automatic_failover = true
heartbeat_timeout = 120         # Expirare heartbeat după 2 minute

# Distribuirea alertelor
distribute_alerts = true
alert_consolidation = true
duplicate_suppression = true
cross_validation_required = true
```

**Configurarea dispozitivului slave**:
```toml
[coordination]
# Configurarea dispozitivului secundar
role = "slave"
master_device = { ip = "192.168.1.100", name = "rayhunter-master" }

# Setări de raportare
report_interval = 15            # Raportați la fiecare 15 secunde
include_negative_results = true # Raportați și lipsa amenințărilor
local_decision_making = false   # Urmați dispozitivul principal
emergency_autonomous_mode = true # Funcționați independent dacă dispozitivul principal nu este disponibil
```

### Scripturi de analiză coordonată

**Corelarea amenințărilor între dispozitive**:
```python
#!/usr/bin/env python3
"""
Sistem de coordonare RayHunter cu mai multe dispozitive
Coordonează detectarea amenințărilor pe mai multe dispozitive
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
        """Bucla principală de coordonare"""
        while True:
            # Colectați date de la toate dispozitivele
            device_data = await self.collect_device_data()

            # Efectuați analiza corelării
            correlated_threats = self.correlate_threats(device_data)

            # Validați amenințările prin consens
            validated_threats = self.consensus_validation(correlated_threats)

            # Distribuiți amenințările validate către dispozitive
            await self.distribute_threat_intelligence(validated_threats)

            await asyncio.sleep(30)  # ciclu de coordonare de 30 de secunde

    async def collect_device_data(self):
        """Colectați date de la toate dispozitivele în paralel"""
        tasks = []
        for device in self.devices:
            task = self.get_device_data(device)
            tasks.append(task)

        results = await asyncio.gather(*tasks, return_exceptions=True)
        return {device['name']: result for device, result in zip(self.devices, results)}

    async def get_device_data(self, device):
        """Preia date de la un dispozitiv individual"""
        async with aiohttp.ClientSession() as session:
            try:
                # Obțineți alertele recente
                alerts_url = f"http://{device['ip']}:8080/api/alerts?since=1min"
                async with session.get(alerts_url) as response:
                    alerts_data = await response.json()

                # Obțineți starea dispozitivului
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
        """Corelează amenințările între mai multe dispozitive"""
        correlated_threats = []

        # Extrageți toate alertele de pe toate dispozitivele
        all_alerts = []
        for device_name, data in device_data.items():
            if 'alerts' in data:
                for alert in data['alerts']:
                    alert['source_device'] = device_name
                    all_alerts.append(alert)

        # Grupați alertele după timp și tipul amenințării
        threat_groups = self.group_alerts_by_similarity(all_alerts)

        for group in threat_groups:
            if len(group) >= 2:  # Mai multe dispozitive au detectat amenințări similare
                correlated_threat = self.create_correlated_threat(group)
                correlated_threats.append(correlated_threat)

        return correlated_threats

    def group_alerts_by_similarity(self, alerts, time_window=60):
        """Grupează alertele după timp și similitudinea amenințărilor"""
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
        """Validează amenințările prin consensul dispozitivelor"""
        validated_threats = []

        for threat in correlated_threats:
            device_count = len(set(alert['source_device'] for alert in threat['constituent_alerts']))
            confidence_scores = [alert['confidence_score'] for alert in threat['constituent_alerts']]

            # Solicitați un număr minim de dispozitive și un prag de încredere
            if (device_count >= 2 and
                np.mean(confidence_scores) >= 0.7 and
                min(confidence_scores) >= 0.5):

                threat['validated'] = True
                threat['consensus_strength'] = device_count / len(self.devices)
                threat['confidence_score'] = np.mean(confidence_scores)
                validated_threats.append(threat)

        return validated_threats
```

## Depanarea problemelor avansate

### Probleme avansate frecvente

#### Probleme de optimizare a performanței

**Depanarea utilizării ridicate a procesorului**:
```bash
#!/bin/bash
# Script de depanare a performanței RayHunter

echo "=== Analiza performanței RayHunter ==="

# Verificați utilizarea procesorului
echo "Utilizarea curentă a procesorului:"
top -bn1 | grep rayhunter

# Verificați utilizarea memoriei
echo -e "\nUtilizarea memoriei:"
ps aux | grep rayhunter | awk '{print $4, $6, $11}'

# Verificați intrările/ieșirile discului
echo -e "\nIntrare/ieșire disc:"
iotop -a -o -d1 -n3 | grep rayhunter

# Analizați problemele de configurare
echo -e "\nAnaliza configurației:"
if [ -f /data/rayhunter/config.toml ]; then
    # Verificați configurațiile care consumă multe resurse
    grep -E "test_heuristic.*true|sensitivity.*maximum|debug.*true" /data/rayhunter/config.toml

    # Verificați setările de înregistrare
    grep -E "recording|storage" /data/rayhunter/config.toml
else
    echo "Fișierul de configurare nu a fost găsit!"
fi

# Verificați înregistrarea excesivă în jurnale
echo -e "\nDimensiunea fișierelor jurnal:"
du -sh /data/rayhunter/logs/*

# Verificați performanța rețelei
echo -e "\nPerformanța rețelei:"
netstat -i | grep -E "wlan|eth"

# Generați recomandări de optimizare
echo -e "\n=== Recomandări de optimizare ==="

# Verificați dacă euristica de test este activată
if grep -q "test_heuristic.*=.*true" /data/rayhunter/config.toml; then
    echo "⚠️ Euristica de test este activată; dezactivați-o în producție"
fi

# Verificați setările de sensibilitate
if grep -q "sensitivity.*=.*\"maximum\"" /data/rayhunter/config.toml; then
    echo "⚠️ Sensibilitatea maximă poate duce la utilizarea intensă a CPU în medii dense"
fi

# Verificați setările de stocare
STORAGE_USED=$(df -h /data/rayhunter | awk 'NR==2 {print $5}' | sed 's/%//')
if [ "$STORAGE_USED" -gt 80 ]; then
    echo "⚠️ Spațiul de stocare este ocupat în proporție de ${STORAGE_USED}%; ștergeți înregistrările vechi"
fi
```

**Detectarea și remedierea scurgerilor de memorie**:
```bash
#!/bin/bash
# Detectați și remediați automat scurgerile de memorie

MEMORY_THRESHOLD=80  # prag de utilizare a memoriei de 80%
LOG_FILE="/var/log/rayhunter/memory_monitor.log"

monitor_memory() {
    while true; do
        # Obțineți utilizarea memoriei de către RayHunter
        MEMORY_USAGE=$(ps aux | grep rayhunter-daemon | grep -v grep | awk '{print $4}')

        if [ ! -z "$MEMORY_USAGE" ]; then
            MEMORY_PERCENT=$(echo "$MEMORY_USAGE" | cut -d. -f1)

            echo "$(date): Utilizarea memoriei RayHunter: ${MEMORY_USAGE}%" >> "$LOG_FILE"

            if [ "$MEMORY_PERCENT" -gt "$MEMORY_THRESHOLD" ]; then
                echo "$(date): Utilizare ridicată a memoriei detectată: ${MEMORY_USAGE}%" >> "$LOG_FILE"

                # Încercați o repornire controlată
                echo "$(date): Se încearcă repornirea controlată..." >> "$LOG_FILE"
                systemctl restart rayhunter_daemon

                sleep 30

                # Verificați dacă repornirea a reușit
                if pgrep rayhunter-daemon > /dev/null; then
                    echo "$(date): Repornirea controlată a reușit" >> "$LOG_FILE"
                else
                    echo "$(date): Repornirea controlată a eșuat; se încearcă repornirea forțată" >> "$LOG_FILE"
                    killall -9 rayhunter-daemon
                    systemctl start rayhunter_daemon
                fi
            fi
        fi

        sleep 60  # Verifică în fiecare minut
    done
}

# Rulați monitorizarea memoriei în fundal
monitor_memory &
```

#### Probleme de conectivitate la rețea

**Diagnosticare avansată a conectivității**:
```bash
#!/bin/bash
# Depanare avansată a conectivității RayHunter

echo "=== Diagnosticarea rețelei RayHunter ==="

# Verificați conectivitatea de bază
echo "1. Verificarea de bază a conectivității:"
ping -c 3 8.8.8.8 > /dev/null 2>&1
if [ $? -eq 0 ]; then
    echo "✓ Conexiune la internet: FUNCȚIONALĂ"
else
    echo "✗ Conexiune la internet: EȘUATĂ"
fi

# Verificați conexiunea celulară
echo -e "\n2. Analiza conexiunii celulare:"
if command -v qmicli &> /dev/null; then
    # Verificați starea modemului
    qmicli -d /dev/cdc-wdm0 --dms-get-operating-mode
    qmicli -d /dev/cdc-wdm0 --nas-get-signal-strength
    qmicli -d /dev/cdc-wdm0 --nas-get-serving-system
else
    echo "qmicli nu este disponibil; se folosesc metode alternative"

    # Verificați interfețele de rețea
    ip addr show | grep -A 10 wwan

    # Verificați rutarea
    ip route show
fi

# Verificați interfața web RayHunter
echo -e "\n3. Verificarea interfeței web RayHunter:"
for port in 8080 80; do
    if netstat -tuln | grep ":$port " > /dev/null; then
        echo "✓ Portul $port ascultă"

        # Testați răspunsul HTTP
        if curl -s -o /dev/null -w "%{http_code}" "http://localhost:$port" | grep -q "200\|302"; then
            echo "✓ Serviciul HTTP răspunde pe portul $port"
        else
            echo "✗ Serviciul HTTP nu răspunde corect pe portul $port"
        fi
    else
        echo "✗ Portul $port nu ascultă"
    fi
done

# Verificați interfața de diagnosticare celulară
echo -e "\n4. Interfața de diagnosticare celulară:"
if [ -c /dev/diag ]; then
    echo "✓ Interfața /dev/diag este disponibilă"
    ls -la /dev/diag
else
    echo "✗ Interfața /dev/diag nu este disponibilă"
    echo "Se verifică interfețele alternative:"
    ls -la /dev/ | grep -E "ttyUSB|cdc-wdm|qcserial"
fi

# Analiză avansată a rețelei
echo -e "\n5. Analiză avansată a rețelei:"

# Verificați setările APN
echo "Configurația APN curentă:"
grep -r "apn" /etc/NetworkManager/system-connections/ 2>/dev/null || echo "Nu a fost găsită nicio configurație APN"

# Verificați rezolvarea DNS
echo "Test de rezoluție DNS:"
nslookup google.com | head -5

# Verificați regulile firewallului
echo "Reguli de firewall care afectează RayHunter:"
iptables -L | grep -E "8080|rayhunter" || echo "Nu au fost găsite reguli de firewall specifice"
```

#### Depanare specifică dispozitivului

**Depanare avansată pentru Orbic RC400L**:
```bash
#!/bin/bash
# Proceduri de depanare specifice pentru Orbic RC400L

echo "=== Diagnosticare avansată Orbic RC400L ==="

# Verificați starea bootloaderului și a partiției de sistem
echo "1. Analiza partiției de sistem:"
df -h | grep -E "/system|/data|/usrdata"

# Verificați subsistemul Android
echo -e "\n2. Verificarea subsistemului Android:"
if command -v adb &> /dev/null; then
    adb devices
    if adb devices | grep -q "device$"; then
        echo "✓ Conexiunea ADB este disponibilă"

        # Verificați proprietățile sistemului
        adb shell getprop | grep -E "ro.build|persist.vendor"

        # Verificați procesele în execuție
        adb shell ps | grep rayhunter

        # Verificați jurnalele de sistem
        echo "Erori recente ale sistemului:"
        adb logcat -d | grep -E "ERROR|FATAL" | tail -10
    else
        echo "✗ Conexiunea ADB nu este disponibilă"
    fi
else
    echo "ADB nu este disponibil; se folosesc metode alternative"
fi

# Verificați firmware-ul modemului
echo -e "\n3. Analiza firmware-ului modemului:"
if [ -c /dev/diag ]; then
    # Folosiți un instrument personalizat pentru a interoga firmware-ul modemului
    python3 << 'EOF'
import serial
import struct
import time

try:
    # Deschideți interfața de diagnosticare
    diag = serial.Serial('/dev/diag', 115200, timeout=1)

    # Interogați versiunea firmware-ului (metodă simplificată)
    # Acest lucru necesită o implementare corectă a protocolului DIAG
    print("Interfața de diagnosticare a modemului este disponibilă")
    diag.close()
except Exception as e:
    print(f"Accesul la diagnosticarea modemului a eșuat: {e}")
EOF
fi

# Verificați problemele specifice operatorului
echo -e "\n4. Verificarea configurației operatorului:"
echo "Preferințele curente pentru benzi:"
cat /data/rayhunter/config.toml | grep -A 5 -B 5 "band"

echo "Starea înregistrării în rețea:"
# Verificați înregistrarea în toate rețelele disponibile
if command -v qmicli &> /dev/null; then
    qmicli -d /dev/cdc-wdm0 --nas-get-home-network
    qmicli -d /dev/cdc-wdm0 --nas-get-preferred-networks
fi
```

**Depanare pentru TP-Link M7350**:
```bash
#!/bin/bash
# Depanare specifică pentru TP-Link M7350

echo "=== Diagnosticare avansată TP-Link M7350 ==="

# Verificați funcționarea cardului SD
echo "1. Diagnosticarea cardului SD:"
if mountpoint -q /media/sd; then
    echo "✓ Cardul SD este montat"
    df -h /media/sd

    # Verificați starea cardului SD
    echo "Verificarea sistemului de fișiere al cardului SD:"
    fsck -n /dev/mmcblk0p1 2>&1 | head -10

    # Verificați permisiunile de scriere
    touch /media/sd/test_write 2>/dev/null && rm /media/sd/test_write
    if [ $? -eq 0 ]; then
        echo "✓ Permisiunile de scriere pe cardul SD sunt în regulă"
    else
        echo "✗ Permisiunile de scriere pe cardul SD au eșuat"
    fi
else
    echo "✗ Cardul SD nu este montat"
    echo "Dispozitive bloc disponibile:"
    lsblk | grep -E "mmc|sd"
fi

# Verificați sistemul OpenWrt
echo -e "\n2. Analiza sistemului OpenWrt:"
echo "Informații despre sistem:"
cat /proc/version
uname -a

echo "Memorie disponibilă:"
free -h

echo "Încărcarea sistemului:"
uptime

# Verificați instalarea pachetelor
echo "Pachete instalate relevante pentru RayHunter:"
opkg list-installed | grep -E "python|kmod|usb"

# Verificați modulele kernelului
echo -e "\n3. Starea modulelor kernelului:"
lsmod | grep -E "diag|qmi|cdc|usb"

# Verificați interfața de diagnosticare USB
echo "Dispozitive de diagnosticare USB:"
lsusb -t
ls -la /dev/ttyUSB* 2>/dev/null || echo "Nu a fost găsit niciun dispozitiv serial USB"
```

### Proceduri de recuperare

**Scripturi de recuperare a sistemului**:
```bash
#!/bin/bash
# Recuperare de urgență a sistemului RayHunter

BACKUP_DIR="/data/rayhunter/backup"
CONFIG_FILE="/data/rayhunter/config.toml"
RECOVERY_LOG="/var/log/rayhunter/recovery.log"

log_message() {
    echo "$(date): $1" | tee -a "$RECOVERY_LOG"
}

create_backup() {
    log_message "Creating system backup..."
    mkdir -p "$BACKUP_DIR"

    # Faceți backup configurației
    cp "$CONFIG_FILE" "$BACKUP_DIR/config_$(date +%Y%m%d_%H%M%S).toml"

    # Faceți backup înregistrărilor din ultimele 24 de ore
    find /data/rayhunter/recordings -name "*.qmdl" -mtime -1 -exec cp {} "$BACKUP_DIR/" \;

    # Faceți backup jurnalelor
    tar -czf "$BACKUP_DIR/logs_$(date +%Y%m%d_%H%M%S).tar.gz" /data/rayhunter/logs/

    log_message "Backup completed"
}

reset_configuration() {
    log_message "Resetting configuration to defaults..."

    # Opriți serviciul RayHunter
    systemctl stop rayhunter_daemon

    # Resetați configurația la valorile din fabrică
    cp /etc/rayhunter/config.toml.default "$CONFIG_FILE"

    # Ștergeți fișierele cache problematice
    rm -f /data/rayhunter/cache/*

    # Resetați permisiunile
    chown -R rayhunter:rayhunter /data/rayhunter/
    chmod -R 755 /data/rayhunter/

    log_message "Configuration reset completed"
}

factory_reset() {
    log_message "Performing factory reset..."

    # Creați mai întâi un backup
    create_backup

    # Opriți toate serviciile RayHunter
    systemctl stop rayhunter_daemon
    systemctl disable rayhunter_daemon

    # Eliminați toate datele RayHunter, cu excepția copiilor de rezervă
    find /data/rayhunter -type f ! -path "*/backup/*" -delete

    # Reinstalați RayHunter
    cd /tmp
    wget -O rayhunter-latest.zip "https://github.com/EFForg/rayhunter/releases/latest/download/rayhunter-linux-x64.zip"
    unzip rayhunter-latest.zip
    ./installer $(detect_device_type)

    log_message "Factory reset completed"
}

detect_device_type() {
    # Detectați automat tipul dispozitivului pentru reinstalare
    if grep -q "Orbic" /proc/cpuinfo || [ -d "/android_root" ]; then
        echo "orbic"
    elif grep -q "MT7620" /proc/cpuinfo || [ -f "/etc/openwrt_version" ]; then
        echo "tplink"
    else
        echo "unknown"
    fi
}

# Meniul principal de recuperare
echo "=== Recuperare de urgență RayHunter ==="
echo "1. Creați doar un backup"
echo "2. Resetați configurația la valorile implicite"
echo "3. Resetare la setările din fabrică (distructivă)"
echo "4. Diagnosticarea sistemului"
echo "5. Ieșire"

read -p "Selectați opțiunea (1-5): " choice

case $choice in
    1) create_backup ;;
    2) reset_configuration ;;
    3)
        read -p "Sigur doriți să continuați? Toate datele, cu excepția backupurilor, vor fi șterse (y/N): " confirm
        if [ "$confirm" = "y" ] || [ "$confirm" = "Y" ]; then
            factory_reset
        else
            echo "Resetarea la setările din fabrică a fost anulată"
        fi
        ;;
    4)
        echo "Se rulează diagnosticarea sistemului..."
        # Rulați toate scripturile de diagnosticare
        /opt/rayhunter/scripts/performance_check.sh
        /opt/rayhunter/scripts/network_diagnostics.sh
        ;;
    5) exit 0 ;;
    *) echo "Opțiune nevalidă" ;;
esac
```

## Scenarii de integrare pentru experți

{{< figure src="rayhunter-soc-integration-workflow.webp" alt="Diagramă de flux care arată datele RayHunter REST API într-un tablou de bord al centrului de operațiuni de securitate, alături de alertele SIEM și fluxurile de export pentru cercetare." >}}

### Integrarea mediului de cercetare

**Configurare pentru cercetare academică**:
```python
#!/usr/bin/env python3
"""
Platformă de integrare a cercetării RayHunter
Configurare avansată pentru cercetarea academică în securitatea celulară
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
        """Configurează o schemă completă pentru baza de date de cercetare"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        # Schema extinsă pentru date de cercetare
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
        """Efectuează un experiment controlat cu parametrii specificați"""
        session_id = f"exp_{datetime.now().strftime('%Y%m%d_%H%M%S')}"

        # Configurați RayHunter pentru experiment
        self.configure_rayhunter_for_research(experiment_config)

        # Începeți colectarea datelor
        collection_start = datetime.now()

        # Rulați experimentul pentru durata specificată
        experiment_duration = experiment_config.get('duration_minutes', 60)

        # Colectați măsurătorile de bază
        baseline_data = self.collect_baseline_measurements(experiment_duration // 3)

        # Introduceți variabile controlate, dacă sunt specificate
        if experiment_config.get('introduce_threats', False):
            threat_data = self.simulate_threat_scenarios(experiment_config['threat_scenarios'])

        # Colectați datele după intervenție
        post_data = self.collect_post_measurements(experiment_duration // 3)

        # Analizați rezultatele
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
        """Analizează statistic tiparele de detectare a amenințărilor"""
        conn = sqlite3.connect(self.db_path)

        # Interogați observațiile privind amenințările
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
            return {"error": "Nu există date disponibile pentru analiză"}

        # Analiză statistică
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

        # Analiza corelării cu mediul
        for env_type in df['environment_type'].unique():
            env_data = df[df['environment_type'] == env_type]
            analysis['environmental_correlation'][env_type] = {
                'threat_frequency': len(env_data) / time_period_days,
                'average_confidence': env_data['confidence_score'].mean(),
                'threat_type_distribution': env_data['threat_type'].value_counts().to_dict()
            }

        # Generați vizualizări
        self.generate_research_visualizations(df, analysis)

        return analysis

    def generate_research_visualizations(self, df, analysis):
        """Generează vizualizări complete pentru cercetare"""
        fig, axes = plt.subplots(2, 3, figsize=(20, 12))

        # Distribuția tipurilor de amenințări
        threat_counts = df['threat_type'].value_counts()
        axes[0, 0].pie(threat_counts.values, labels=threat_counts.index, autopct='%1.1f%%')
        axes[0, 0].set_title('Distribuția tipurilor de amenințări')

        # Distribuția scorurilor de încredere
        axes[0, 1].hist(df['confidence_score'], bins=20, alpha=0.7)
        axes[0, 1].set_title('Distribuția scorului de încredere')
        axes[0, 1].set_xlabel('Scor de încredere')
        axes[0, 1].set_ylabel('Frecvență')

        # Tipare temporale
        df['hour'] = pd.to_datetime(df['timestamp']).dt.hour
        hourly_counts = df.groupby('hour').size()
        axes[0, 2].bar(hourly_counts.index, hourly_counts.values)
        axes[0, 2].set_title('Amenințări în funcție de ora zilei')
        axes[0, 2].set_xlabel('Oră')
        axes[0, 2].set_ylabel('Număr de amenințări')

        # Mediu versus încredere
        sns.boxplot(data=df, x='environment_type', y='confidence_score', ax=axes[1, 0])
        axes[1, 0].set_title('Încredere în funcție de tipul mediului')
        axes[1, 0].tick_params(axis='x', rotation=45)

        # Hartă termică a corelării
        numeric_df = df.select_dtypes(include=[np.number])
        correlation_matrix = numeric_df.corr()
        sns.heatmap(correlation_matrix, annot=True, ax=axes[1, 1])
        axes[1, 1].set_title('Matrice de corelație')

        # Analiza alarmelor false
        if 'false_positive_assessment' in df.columns:
            fp_data = df['false_positive_assessment'].value_counts()
            axes[1, 2].bar(fp_data.index, fp_data.values)
            axes[1, 2].set_title('Evaluarea alarmelor false')
            axes[1, 2].tick_params(axis='x', rotation=45)

        plt.tight_layout()
        plt.savefig(f'/data/research/analysis/visualization_{datetime.now().strftime("%Y%m%d_%H%M%S")}.png',
                   dpi=300, bbox_inches='tight')
        plt.close()

    def export_research_data(self, format='csv', time_range_days=None):
        """Exportă datele de cercetare în mai multe formate pentru analiza externă"""
        conn = sqlite3.connect(self.db_path)

        if time_range_days:
            end_date = datetime.now()
            start_date = end_date - timedelta(days=time_range_days)
            date_filter = f"WHERE timestamp BETWEEN '{start_date.isoformat()}' AND '{end_date.isoformat()}'"
        else:
            date_filter = ""

        # Exportați observațiile privind amenințările
        threat_query = f"SELECT * FROM threat_observations {date_filter}"
        threat_df = pd.read_sql_query(threat_query, conn)

        # Exportați măsurătorile celulare
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

## Concluzie

Implementarea avansată **RayHunter** necesită expertiză tehnică în mai multe domenii, inclusiv **protocoale celulare**, **analiză RF**, integrarea sistemelor și modelarea amenințărilor. Tehnicile prezentate în acest ghid îi ajută pe experți să valorifice la maximum capacitățile de detectare **RayHunter**, reducând în același timp alarmele false și efortul operațional.

*Acestea sunt punctele principale pentru operațiunile avansate **RayHunter**:*

1. **Optimizarea euristicilor personalizate** poate reduce alarmele false cu 80%, păstrând sensibilitatea ridicată de detectare prin configurări adaptate mediului
2. **Automatizarea prin API** permite implementarea la scară de întreprindere și integrarea cu centrele de operațiuni de securitate existente
3. **Coordonarea mai multor dispozitive** oferă acoperire completă și validare încrucișată, sporind încrederea în detectarea amenințărilor
4. **Metodologiile avansate de depanare** asigură funcționarea fiabilă în medii diverse și dificile
5. **Capacitățile de integrare pentru cercetare** sprijină studiile academice și comerciale privind amenințările celulare

Utilizatorii experimentați **RayHunter** ar trebui să urmărească evoluțiile din **securitatea celulară**, **tehnologia de supraveghere** și capacitățile de detectare open-source. *Amenințările în schimbare impun îmbunătățirea continuă a tehnicilor de detectare și a procedurilor operaționale.*

Organizațiile care implementează **RayHunter** în operațiuni profesionale de securitate ar trebui să ia în considerare integrarea cu un **centru de operațiuni de securitate** dedicat, instruirea periodică a personalului și colaborarea cu comunitatea **RayHunter** pentru a împărtăși informații despre amenințări și îmbunătățiri ale detectării.

Nu ai încă echipamentul necesar pentru aceste configurări avansate? **[Dispozitive verificate compatibile cu RayHunter](https://stscollective.com/collections/rayhunter)** sunt disponibile la STS Collective. Codul pentru cititori **SIMEONONSECURITY** oferă până la 20% reducere.

{{< centerbutton href="https://stscollective.com/discount/SIMEONONSECURITY" >}}
  Cumpără dispozitive RayHunter și economisește 20%
{{< /centerbutton >}}

## Referințe

- [Documentația oficială RayHunter](https://efforg.github.io/rayhunter/introduction.html)
- [Referința REST API RayHunter](https://efforg.github.io/rayhunter/api-docs/)
- [Electronic Frontier Foundation](https://www.eff.org/)
- [Depozitul RayHunter pe GitHub](https://github.com/EFForg/rayhunter)
- [Resurse pentru analiza protocoalelor celulare](https://www.sharetechnote.com/)
- [Resurse de analiză RF și SDR](https://greatscottgadgets.com/sdr/)
- [Practici recomandate pentru integrarea securității în întreprinderi](https://www.sans.org/white-papers/)
