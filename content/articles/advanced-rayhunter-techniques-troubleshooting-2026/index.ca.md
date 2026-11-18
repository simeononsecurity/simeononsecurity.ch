---
title: "RayHunter avançat 2026: tècniques i resolució de problemes"
draft: false
toc: true
date: 2026-03-10
lastmod: 2026-11-14
description: "Guia tècnica sobre tècniques avançades de RayHunter, resolució de problemes, configuracions personalitzades, integració d’API i fluxos de detecció d’IMSI catchers."
tags: ["Rayhunter", "tècniques avançades", "resolució de problemes", "configuració experta", "IMSI catcher", "detecció de vigilància", "optimització d’heurístiques", "integració d’API", "fluxos d’anàlisi", "modelatge d’amenaces", "seguretat cel·lular", "anàlisi forense sense fil", "optimització de detecció", "configuracions personalitzades", "desplegament avançat", "recerca de seguretat", "anàlisi de xarxa", "anàlisi RF", "contramesures de vigilància", "eines de privadesa"]
cover: "/img/cover/advanced-rayhunter-techniques-troubleshooting-2026.webp"
coverAlt: "Il·lustració digital de diversos dispositius, com ara ordinadors portàtils i telèfons intel·ligents, connectats per línies lluminoses. Al fons fosc hi ha torres cel·lulars abstractes i fluxos de dades."
coverCaption: "Tècniques avançades de RayHunter: guia experta de configuració i anàlisi 2026"
---

**Domina la configuració avançada, la resolució de problemes i l’optimització de RayHunter per detectar IMSI catchers a nivell expert**

## Resum

**El desplegament avançat de RayHunter requereix estratègies de configuració ben pensades, ajust d’heurístiques personalitzades i experiència completa en resolució de problemes**. Aquesta guia experta tracta l’optimització d’heurístiques per a entorns d’amenaça específics (reducció de falsos positius de fins al 80%), fluxos de treball d’anàlisi automatitzada amb API, detecció coordinada amb diversos dispositius, integració forense avançada i mètodes complexos de diagnòstic. Entre les capacitats avançades principals hi ha els canvis a **config.toml** per a entorns especialitzats, l’automatització de la **REST API** per a la integració empresarial, l’anàlisi avançada de **QMDL/PCAP**, el desplegament coordinat de diversos sensors i algorismes sofisticats de correlació d’amenaces. **Amb una configuració avançada adequada, els usuaris experts poden assolir una precisió de detecció superior al 99% i menys de l’1% de falsos positius**, i integrar RayHunter en centres d’operacions de seguretat complets i sistemes automatitzats de resposta a amenaces.

## Introducció a les operacions avançades de RayHunter

**El desplegament avançat de RayHunter** va molt més enllà de la instal·lació i la configuració bàsiques. L’ús expert requereix un coneixement profund dels **protocols cel·lulars**, les tècniques d’**anàlisi RF**, els principis de **modelatge d’amenaces** i les capacitats avançades d’integració de sistemes. Aquesta guia tracta les tècniques necessàries per a operacions de seguretat professionals, entorns de recerca i escenaris de detecció de vigilància d’alt risc.

El desplegament avançat de **RayHunter** inclou:
- **Desenvolupament d’heurístiques personalitzades** i optimització per a entorns d’amenaça específics
- **Automatització amb API** i integració amb centres d’operacions de seguretat
- **Coordinació de diversos dispositius** per cobrir una àrea sencera
- **Integració forense avançada** amb eines d’anàlisi de xarxes cel·lulars
- **Modelatge personalitzat d’amenaces** i configuracions adaptades a l’entorn
- **Resolució de problemes i manteniment a escala empresarial**

*Aquesta guia pressuposa que coneixes la instal·lació i la configuració bàsiques de **RayHunter**.* Les tècniques avançades requereixen coneixements dels protocols cel·lulars (2G/3G/4G/LTE), els principis d’anàlisi RF, la seguretat de xarxa i la integració amb un centre d’operacions de seguretat.

{{< stscollective-ad "rayhunter" >}}

## Estratègies avançades de configuració

### Optimització d’heurístiques personalitzades

L’eficàcia de detecció de **RayHunter** depèn molt de configurar les heurístiques adequadament per a cada entorn operatiu. **Els usuaris avançats poden millorar notablement la precisió de detecció i reduir els falsos positius** ajustant les heurístiques amb cura.

#### Perfils d’heurístiques per entorn

**Configuració per a zones urbanes d’alta densitat**:
```toml
[heuristics]
# Redueix la sensibilitat en zones urbanes concorregudes
connection_release_detection = { enabled = true, sensitivity = "low", timeout = 30 }
imsi_request_detection = { enabled = true, threshold = 3, window = 60 }
null_cipher_detection = { enabled = true, immediate_alert = false }
sib_downgrade_detection = { enabled = true, sensitivity = "medium" }
incomplete_sib_detection = { enabled = false }  # Taxa elevada de falsos positius en zones urbanes

[filtering]
# Filtratge avançat per a entorns urbans
tower_density_threshold = 20
legitimate_carrier_whitelist = ["Verizon", "AT&T", "T-Mobile"]
frequency_hopping_tolerance = 5
```

**Configuració per a zones rurals de baixa densitat**:
```toml
[heuristics]
# Augmenta la sensibilitat en entorns poc densos
connection_release_detection = { enabled = true, sensitivity = "high", timeout = 10 }
imsi_request_detection = { enabled = true, threshold = 1, window = 30 }
null_cipher_detection = { enabled = true, immediate_alert = true }
sib_downgrade_detection = { enabled = true, sensitivity = "high" }
incomplete_sib_detection = { enabled = true, threshold = 2 }

[filtering]
# Filtratge mínim per a entorns rurals
tower_density_threshold = 5
legitimate_carrier_whitelist = []
frequency_hopping_tolerance = 1
```

**Configuració per a esdeveniments d’alta seguretat**:
```toml
[heuristics]
# Sensibilitat màxima per a escenaris d’alt risc
connection_release_detection = { enabled = true, sensitivity = "maximum", timeout = 5 }
imsi_request_detection = { enabled = true, threshold = 1, window = 15 }
null_cipher_detection = { enabled = true, immediate_alert = true, block_connection = true }
sib_downgrade_detection = { enabled = true, sensitivity = "maximum" }
incomplete_sib_detection = { enabled = true, threshold = 1 }
test_heuristic = { enabled = false }  # No activis mai el mode de prova durant les operacions

[alerting]
# Alertes immediates per a escenaris d’alta seguretat
alert_threshold = "low"
immediate_notification = true
multi_channel_alerts = true
```

#### Desenvolupament d’heurístiques personalitzades

Els usuaris avançats poden desenvolupar heurístiques de detecció pròpies modificant la configuració i la lògica d’anàlisi de **RayHunter**:

**Heurística personalitzada d’anàlisi temporal**:
```toml
[custom_heuristics]
# Detecció personalitzada basada en el temps
timing_anomaly_detection = {
    enabled = true,
    baseline_establishment = 300,  # Línia de base de 5 minuts
    deviation_threshold = 3.0,     # 3 desviacions estàndard
    minimum_samples = 50,
    alert_on_first_deviation = false
}

# Reconeixement avançat de patrons
cell_tower_behavior_analysis = {
    enabled = true,
    learning_period = 3600,        # Aprenentatge durant 1 hora
    pattern_memory = 168,          # Retenció de patrons durant 7 dies
    anomaly_sensitivity = 0.85,    # Llindar de confiança del 85%
    behavioral_baseline = "adaptive"
}
```

**Heurística de correlació geogràfica**:
```toml
[geo_correlation]
# Avaluació d’amenaces basada en la ubicació
enabled = true
gps_accuracy_threshold = 10        # Cal una precisió de 10 metres
movement_speed_threshold = 50      # Velocitat màxima raonable: 50 km/h
stationary_threshold = 100         # Radi d’estacionarietat de 100 metres
suspicious_location_database = "/data/rayhunter/suspicious_locations.db"

# Detecció coordinada entre diversos dispositius
multi_device_correlation = {
    enabled = true,
    correlation_radius = 1000,     # Radi de correlació d’1 km
    time_synchronization = 5,      # Tolerància de sincronització horària de 5 segons
    consensus_threshold = 0.67     # Cal que hi estigui d’acord el 67% dels dispositius
}
```

### Gestió avançada de l’energia

Les operacions prolongades requereixen estratègies de gestió energètica que vagin més enllà de l’optimització bàsica de la bateria:

**Gestió adaptativa de l’energia**:
```toml
[power_management]
# Escalat dinàmic de potència segons el nivell d’amenaça
adaptive_scaling = true
baseline_power_mode = "balanced"
high_alert_power_mode = "maximum_performance"
low_activity_power_mode = "extended_battery"

# Modes d’operació programats
scheduled_modes = [
    { time = "00:00-06:00", mode = "low_power", days = ["monday", "tuesday", "wednesday", "thursday", "friday"] },
    { time = "06:00-22:00", mode = "high_sensitivity", days = ["saturday", "sunday"] },
    { time = "22:00-24:00", mode = "balanced", days = "all" }
]

# Canvis de mode activats pel nivell de bateria
battery_thresholds = {
    "90%" = "maximum_performance",
    "50%" = "balanced",
    "25%" = "extended_battery",
    "10%" = "emergency_detection_only"
}
```

**Coordinació energètica de diversos dispositius**:
```toml
[coordinated_power]
# Coordina la gestió de l’energia entre diversos dispositius
device_roles = ["primary", "secondary", "backup"]
role_switching_enabled = true
battery_level_sharing = true
automatic_failover = true

# Coordinació avançada de repòs i activació
coordinated_sleep_cycles = {
    enabled = true,
    sleep_rotation_interval = 300,  # 5 minuts
    minimum_active_devices = 2,
    overlap_period = 30             # Solapament de 30 segons
}
```

## Tècniques avançades d’anàlisi

### Anàlisi personalitzada de PCAP i QMDL

**RayHunter** genera **captures detallades de protocols cel·lulars**. Les tècniques avançades d’anàlisi permeten extreure’n el màxim valor informatiu.

#### Ús avançat de rayhunter-check

**Fluxos de treball d’anàlisi per lots**:
```bash
#!/bin/bash
# Script avançat d’anàlisi per lots de diverses gravacions

ANALYSIS_DIR="/data/rayhunter/analysis"
RECORDINGS_DIR="/data/rayhunter/recordings"
OUTPUT_DIR="/data/rayhunter/reports"

# Processa totes les gravacions amb paràmetres personalitzats
for recording in "$RECORDINGS_DIR"/*.qmdl; do
    filename=$(basename "$recording" .qmdl)
    echo "S'està processant $filename..."

    # Anàlisi estàndard
    rayhunter-check -p "$recording" --json > "$OUTPUT_DIR/${filename}_standard.json"

    # Anàlisi de depuració amb sortida ampliada
    rayhunter-check -d -p "$recording" --verbose > "$OUTPUT_DIR/${filename}_debug.log"

    # Anàlisi heurística personalitzada
    rayhunter-check -p "$recording" --config "/etc/rayhunter/custom_analysis.toml" \
        --output-format json > "$OUTPUT_DIR/${filename}_custom.json"

    # Anàlisi de correlació d’amenaces
    rayhunter-check -p "$recording" --correlate-threats \
        --baseline "$ANALYSIS_DIR/baseline.qmdl" > "$OUTPUT_DIR/${filename}_correlation.json"
done

# Genera un informe consolidat
python3 /opt/rayhunter/analysis/consolidate_reports.py "$OUTPUT_DIR" > "$OUTPUT_DIR/consolidated_analysis.html"
```

**Filtratge i anàlisi avançats**:
```bash
# Anàlisi personalitzada amb àrees d’interès específiques
rayhunter-check -p recording.qmdl \
    --focus-heuristics "imsi_request,null_cipher" \
    --time-range "14:30-15:45" \
    --frequency-bands "1900,850" \
    --operator-filter "unknown" \
    --confidence-threshold 0.8

# Anàlisi comparativa entre gravacions
rayhunter-check --compare recording1.qmdl recording2.qmdl \
    --baseline-period 300 \
    --anomaly-detection \
    --statistical-analysis

# Integració amb eines externes
rayhunter-check -p recording.qmdl --export-wireshark | \
    tshark -r - -Y "gsm || lte" -T json > cellular_traffic.json
```

### Scripts d’anàlisi personalitzats

**Integració amb Python per a l’anàlisi avançada**:
```python
#!/usr/bin/env python3
"""
Integració avançada de l’anàlisi de RayHunter
Ofereix capacitats d’anàlisi avançades per a les dades de RayHunter
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
        """Inicialitza la base de dades d’anàlisi amb un esquema personalitzat"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        # Crea taules d’anàlisi avançada
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
        """Processa la sortida JSON de RayHunter per fer una anàlisi avançada"""
        with open(json_file_path, 'r') as f:
            data = json.load(f)

        # Extreu i normalitza els esdeveniments d’amenaça
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
        """Calcula una puntuació de confiança avançada a partir de diversos factors"""
        base_confidence = alert.get('confidence', 0.5)

        # Tingues en compte diversos punts de dades
        factors = {
            'signal_strength': alert.get('signal_strength', 0) / 100,
            'timing_consistency': alert.get('timing_score', 0.5),
            'protocol_compliance': alert.get('protocol_score', 0.5),
            'environmental_context': alert.get('environment_score', 0.5)
        }

        # Càlcul ponderat de la confiança
        weights = {'signal_strength': 0.3, 'timing_consistency': 0.25,
                  'protocol_compliance': 0.25, 'environmental_context': 0.2}

        weighted_confidence = sum(factors[k] * weights[k] for k in factors)
        return min(base_confidence + weighted_confidence, 1.0)

    def correlation_analysis(self, events, time_window=300):
        """Fes una anàlisi de correlació temporal i espacial"""
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
        """Calcula la intensitat de correlació entre dos esdeveniments"""
        # Implementa un algorisme de correlació sofisticat
        similarity_factors = []

        # Similitud dels tipus d’amenaça
        if event1['threat_type'] == event2['threat_type']:
            similarity_factors.append(0.4)
        elif self.are_related_threats(event1['threat_type'], event2['threat_type']):
            similarity_factors.append(0.2)

        # Similitud de les puntuacions de confiança
        confidence_diff = abs(event1['confidence_score'] - event2['confidence_score'])
        similarity_factors.append(1.0 - confidence_diff)

        return np.mean(similarity_factors)

    def generate_threat_report(self, analysis_period_hours=24):
        """Genera un informe complet d’avaluació d’amenaces"""
        end_time = datetime.now()
        start_time = end_time - timedelta(hours=analysis_period_hours)

        # Consulta els esdeveniments recents a la base de dades
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

        # Genera una anàlisi estadística
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

### Automatització amb API

La **REST API** de **RayHunter** permet automatitzar processos sofisticats i integrar-los amb els sistemes de seguretat empresarials.

#### Scripts de supervisió automatitzada

**Automatització de la supervisió contínua**:
```python
#!/usr/bin/env python3
"""
Sistema empresarial de monitoratge de RayHunter
Integració de detecció i resposta automatitzades a les amenaces
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
        """Configura el registre de nivell empresarial"""
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
        """Monitoratge continu de diversos dispositius RayHunter"""
        while True:
            for device_name, config in self.devices.items():
                try:
                    device_status = self.check_device_status(config)
                    alerts = self.get_recent_alerts(config)

                    if alerts:
                        self.process_alerts(device_name, alerts)

                    self.log_device_status(device_name, device_status)

                except Exception as e:
                    self.logger.error(f"Error en supervisar el dispositiu {device_name}: {e}")

            time.sleep(poll_interval)

    def check_device_status(self, config):
        """Comprova l’estat complet del dispositiu mitjançant l’API"""
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
            self.logger.warning(f"No es pot accedir al dispositiu {config['ip']}: {e}")
            return {'online': False, 'error': str(e)}

    def get_recent_alerts(self, config, minutes=5):
        """Recupera les alertes recents del dispositiu"""
        api_url = f"http://{config['ip']}:8080/api/alerts"
        params = {'since': f"{minutes}min"}

        try:
            response = requests.get(api_url, params=params, timeout=10)
            response.raise_for_status()
            return response.json().get('alerts', [])
        except requests.RequestException:
            return []

    def process_alerts(self, device_name, alerts):
        """Processa les alertes i respon-hi"""
        for alert in alerts:
            alert_level = self.assess_alert_severity(alert)

            if alert_level == 'CRITICAL':
                self.handle_critical_alert(device_name, alert)
            elif alert_level == 'HIGH':
                self.handle_high_alert(device_name, alert)
            elif alert_level == 'MEDIUM':
                self.handle_medium_alert(device_name, alert)

            # Registra totes les alertes
            self.logger.info(f"Alerta de {device_name}: {alert['heuristic']} - {alert_level}")

    def assess_alert_severity(self, alert):
        """Avalua la gravetat de l’alerta a partir de diversos factors"""
        threat_type = alert.get('heuristic', '')
        confidence = alert.get('confidence_score', 0)

        # Amenaces crítiques
        if threat_type in ['null_cipher_detection', 'imsi_request_detection'] and confidence > 0.9:
            return 'CRITICAL'

        # Amenaces d’alta gravetat
        elif threat_type in ['connection_release_detection', 'sib_downgrade_detection'] and confidence > 0.8:
            return 'HIGH'

        # Gravetat mitjana
        elif confidence > 0.6:
            return 'MEDIUM'

        return 'LOW'

    def handle_critical_alert(self, device_name, alert):
        """Gestiona les alertes de seguretat crítiques amb una resposta immediata"""
        # Envia notificacions immediates
        self.send_sms_alert(f"CRÍTIC: {device_name} ha detectat un IMSI catcher")
        self.send_email_alert("AMENAÇA CRÍTICA", device_name, alert)

        # Executa una resposta automatitzada
        subprocess.run(['/opt/security/scripts/critical_response.sh', device_name])

        # Registra-ho a SIEM
        self.log_to_siem('CRITICAL', device_name, alert)
```

#### Integració empresarial

**Script d’integració amb SIEM**:
```python
def integrate_with_siem(self, alert_data):
    """Integració amb sistemes SIEM empresarials"""

    # Integració amb Splunk
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

    # Envia-ho a Splunk HEC
    requests.post(
        'https://splunk.company.com:8088/services/collector',
        headers={'Authorization': 'Splunk <HEC-TOKEN>'},
        json=splunk_data
    )

    # Integració de QRadar mitjançant syslog
    syslog_message = f"Alerta de RayHunter: {alert_data['heuristic']} detectat " \
                    f"amb una confiança de {alert_data['confidence_score']:.2f} " \
                    f"al dispositiu {alert_data['device_name']}"

    subprocess.run([
        'logger', '-p', 'local0.alert', '-t', 'RayHunter', syslog_message
    ])
```

## Coordinació de diversos dispositius

{{< figure src="rayhunter-multi-device-coordination-network.webp" alt="Diagrama amb diversos dispositius RayHunter desplegats en una zona de cobertura. Cada dispositiu envia les deteccions a un dispositiu mestre coordinador per validar-les de manera creuada." >}}

Els desplegaments avançats de **RayHunter** sovint coordinen diversos dispositius per cobrir una àrea sencera i **validar les amenaces de manera creuada**.

### Xarxes de detecció coordinades

**Configuració mestre-esclau**:
```toml
[coordination]
# Configuració del dispositiu mestre
role = "master"
slave_devices = [
    { ip = "192.168.1.101", name = "rayhunter-north", priority = 1 },
    { ip = "192.168.1.102", name = "rayhunter-south", priority = 2 },
    { ip = "192.168.1.103", name = "rayhunter-west", priority = 3 }
]

# Configuració de coordinació
sync_interval = 30              # Sincronitza cada 30 segons
correlation_window = 60         # Finestra de correlació d’1 minut
consensus_threshold = 0.67      # Cal un acord del 67% per generar l’alerta
automatic_failover = true
heartbeat_timeout = 120         # Temps d’espera del batec: 2 minuts

# Distribució d’alertes
distribute_alerts = true
alert_consolidation = true
duplicate_suppression = true
cross_validation_required = true
```

**Configuració del dispositiu esclau**:
```toml
[coordination]
# Configuració del dispositiu secundari
role = "slave"
master_device = { ip = "192.168.1.100", name = "rayhunter-master" }

# Configuració d’informes
report_interval = 15            # Informa cada 15 segons
include_negative_results = true # Informa també quan no hi hagi amenaces
local_decision_making = false   # Delega en el dispositiu mestre
emergency_autonomous_mode = true # Actua de manera independent si el dispositiu mestre no està disponible
```

### Scripts d’anàlisi coordinada

**Correlació d’amenaces entre dispositius**:
```python
#!/usr/bin/env python3
"""
Sistema de coordinació de RayHunter amb diversos dispositius
Ofereix una detecció coordinada d’amenaces en diversos dispositius
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
        """Bucle principal de coordinació"""
        while True:
            # Recull dades de tots els dispositius
            device_data = await self.collect_device_data()

            # Fes l’anàlisi de correlació
            correlated_threats = self.correlate_threats(device_data)

            # Valida les amenaces per consens
            validated_threats = self.consensus_validation(correlated_threats)

            # Distribueix les amenaces validades als dispositius
            await self.distribute_threat_intelligence(validated_threats)

            await asyncio.sleep(30)  # Cicle de coordinació de 30 segons

    async def collect_device_data(self):
        """Recull dades de tots els dispositius en paral·lel"""
        tasks = []
        for device in self.devices:
            task = self.get_device_data(device)
            tasks.append(task)

        results = await asyncio.gather(*tasks, return_exceptions=True)
        return {device['name']: result for device, result in zip(self.devices, results)}

    async def get_device_data(self, device):
        """Obtén dades d’un dispositiu individual"""
        async with aiohttp.ClientSession() as session:
            try:
                # Consulta les alertes recents
                alerts_url = f"http://{device['ip']}:8080/api/alerts?since=1min"
                async with session.get(alerts_url) as response:
                    alerts_data = await response.json()

                # Consulta l’estat del dispositiu
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
        """Correlaciona les amenaces entre diversos dispositius"""
        correlated_threats = []

        # Extreu totes les alertes de tots els dispositius
        all_alerts = []
        for device_name, data in device_data.items():
            if 'alerts' in data:
                for alert in data['alerts']:
                    alert['source_device'] = device_name
                    all_alerts.append(alert)

        # Agrupa les alertes per hora i tipus d’amenaça
        threat_groups = self.group_alerts_by_similarity(all_alerts)

        for group in threat_groups:
            if len(group) >= 2:  # S’han detectat amenaces semblants en diversos dispositius
                correlated_threat = self.create_correlated_threat(group)
                correlated_threats.append(correlated_threat)

        return correlated_threats

    def group_alerts_by_similarity(self, alerts, time_window=60):
        """Agrupa les alertes per similitud temporal i de les amenaces"""
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
        """Valida les amenaces mitjançant el consens dels dispositius"""
        validated_threats = []

        for threat in correlated_threats:
            device_count = len(set(alert['source_device'] for alert in threat['constituent_alerts']))
            confidence_scores = [alert['confidence_score'] for alert in threat['constituent_alerts']]

            # Exigeix un nombre mínim de dispositius i un llindar de confiança
            if (device_count >= 2 and
                np.mean(confidence_scores) >= 0.7 and
                min(confidence_scores) >= 0.5):

                threat['validated'] = True
                threat['consensus_strength'] = device_count / len(self.devices)
                threat['confidence_score'] = np.mean(confidence_scores)
                validated_threats.append(threat)

        return validated_threats
```

## Resolució de problemes avançats

### Problemes avançats habituals

#### Problemes d’optimització del rendiment

**Diagnòstic d’un ús elevat de la CPU**:
```bash
#!/bin/bash
# Script de resolució de problemes de rendiment de RayHunter

echo "=== Anàlisi del rendiment de RayHunter ==="

# Comprova l’ús de CPU
echo "Ús actual de la CPU:"
top -bn1 | grep rayhunter

# Comprova l’ús de memòria
echo -e "\nÚs de memòria:"
ps aux | grep rayhunter | awk '{print $4, $6, $11}'

# Comprova l’E/S del disc
echo -e "\nE/S del disc:"
iotop -a -o -d1 -n3 | grep rayhunter

# Analitza els problemes de configuració
echo -e "\nAnàlisi de la configuració:"
if [ -f /data/rayhunter/config.toml ]; then
    # Comprova les configuracions que consumeixen molts recursos
    grep -E "test_heuristic.*true|sensitivity.*maximum|debug.*true" /data/rayhunter/config.toml

    # Comprova la configuració de gravació
    grep -E "recording|storage" /data/rayhunter/config.toml
else
    echo "No s’ha trobat el fitxer de configuració!"
fi

# Comprova si es generen massa registres
echo -e "\nMides dels fitxers de registre:"
du -sh /data/rayhunter/logs/*

# Comprovació del rendiment de xarxa
echo -e "\nRendiment de la xarxa:"
netstat -i | grep -E "wlan|eth"

# Genera recomanacions d’optimització
echo -e "\n=== Recomanacions d’optimització ==="

# Comprova si la heurística de prova està activada
if grep -q "test_heuristic.*=.*true" /data/rayhunter/config.toml; then
    echo "⚠️ La heurística de prova està activada; desactiva-la en producció"
fi

# Comprova la configuració de sensibilitat
if grep -q "sensitivity.*=.*\"maximum\"" /data/rayhunter/config.toml; then
    echo "⚠️ La sensibilitat màxima pot augmentar l'ús de la CPU en entorns densos"
fi

# Comprova la configuració d’emmagatzematge
STORAGE_USED=$(df -h /data/rayhunter | awk 'NR==2 {print $5}' | sed 's/%//')
if [ "$STORAGE_USED" -gt 80 ]; then
    echo "⚠️ L'emmagatzematge ocupa ${STORAGE_USED}%; elimina enregistraments antics"
fi
```

**Detecció i resolució de fuites de memòria**:
```bash
#!/bin/bash
# Detecta filtracions de memòria i corregeix-les automàticament

MEMORY_THRESHOLD=80  # Llindar d’ús de memòria del 80%
LOG_FILE="/var/log/rayhunter/memory_monitor.log"

monitor_memory() {
    while true; do
        # Consulta l’ús de memòria de RayHunter
        MEMORY_USAGE=$(ps aux | grep rayhunter-daemon | grep -v grep | awk '{print $4}')

        if [ ! -z "$MEMORY_USAGE" ]; then
            MEMORY_PERCENT=$(echo "$MEMORY_USAGE" | cut -d. -f1)

            echo "$(date): Ús de memòria de RayHunter: ${MEMORY_USAGE}%" >> "$LOG_FILE"

            if [ "$MEMORY_PERCENT" -gt "$MEMORY_THRESHOLD" ]; then
                echo "$(date): S’ha detectat un ús elevat de memòria: ${MEMORY_USAGE}%" >> "$LOG_FILE"

                # Prova de reinici controlat
                echo "$(date): S’intenta un reinici ordenat..." >> "$LOG_FILE"
                systemctl restart rayhunter_daemon

                sleep 30

                # Verifica que el reinici s’hagi completat correctament
                if pgrep rayhunter-daemon > /dev/null; then
                    echo "$(date): El reinici ordenat s’ha completat correctament" >> "$LOG_FILE"
                else
                    echo "$(date): Ha fallat el reinici ordenat; s’intenta un reinici forçat" >> "$LOG_FILE"
                    killall -9 rayhunter-daemon
                    systemctl start rayhunter_daemon
                fi
            fi
        fi

        sleep 60  # Comprova cada minut
    done
}

# Executa la supervisió de memòria en segon pla
monitor_memory &
```

#### Problemes de connectivitat de xarxa

**Diagnòstic avançat de connectivitat**:
```bash
#!/bin/bash
# Resolució avançada de problemes de connectivitat de RayHunter

echo "=== Diagnòstic de xarxa de RayHunter ==="

# Comprova la connectivitat bàsica
echo "1. Comprovació bàsica de connectivitat:"
ping -c 3 8.8.8.8 > /dev/null 2>&1
if [ $? -eq 0 ]; then
    echo "✓ Connexió a Internet: CORRECTA"
else
    echo "✗ Connexió a Internet: FALLIDA"
fi

# Comprova la connexió mòbil
echo -e "\n2. Anàlisi de la connexió mòbil:"
if command -v qmicli &> /dev/null; then
    # Comprova l’estat del mòdem
    qmicli -d /dev/cdc-wdm0 --dms-get-operating-mode
    qmicli -d /dev/cdc-wdm0 --nas-get-signal-strength
    qmicli -d /dev/cdc-wdm0 --nas-get-serving-system
else
    echo "qmicli no està disponible; s’utilitzen mètodes alternatius"

    # Comprova les interfícies de xarxa
    ip addr show | grep -A 10 wwan

    # Comprova l’encaminament
    ip route show
fi

# Comprova la interfície web de RayHunter
echo -e "\n3. Comprovació de la interfície web de RayHunter:"
for port in 8080 80; do
    if netstat -tuln | grep ":$port " > /dev/null; then
        echo "✓ El port $port està escoltant"

        # Prova la resposta HTTP
        if curl -s -o /dev/null -w "%{http_code}" "http://localhost:$port" | grep -q "200\|302"; then
            echo "✓ El servei HTTP respon al port $port"
        else
            echo "✗ El servei HTTP no respon correctament al port $port"
        fi
    else
        echo "✗ El port $port no està escoltant"
    fi
done

# Comprova la interfície de diagnòstic mòbil
echo -e "\n4. Interfície de diagnòstic mòbil:"
if [ -c /dev/diag ]; then
    echo "✓ La interfície /dev/diag està disponible"
    ls -la /dev/diag
else
    echo "✗ La interfície /dev/diag no està disponible"
    echo "Comprovació de les interfícies alternatives:"
    ls -la /dev/ | grep -E "ttyUSB|cdc-wdm|qcserial"
fi

# Anàlisi avançada de xarxa
echo -e "\n5. Anàlisi avançada de xarxa:"

# Comprova la configuració de l’APN
echo "Configuració actual de l’APN:"
grep -r "apn" /etc/NetworkManager/system-connections/ 2>/dev/null || echo "No s’ha trobat cap configuració d’APN"

# Comprova la resolució DNS
echo "Prova de resolució DNS:"
nslookup google.com | head -5

# Comprova les regles del tallafoc
echo "Regles del tallafoc que afecten RayHunter:"
iptables -L | grep -E "8080|rayhunter" || echo "No s’han trobat regles específiques del tallafoc"
```

#### Resolució de problemes específica del dispositiu

**Resolució avançada de problemes de l’Orbic RC400L**:
```bash
#!/bin/bash
# Procediments de resolució de problemes específics de l’Orbic RC400L

echo "=== Diagnòstic avançat de l’Orbic RC400L ==="

# Comprova l’estat del carregador d’arrencada i de la partició del sistema
echo "1. Anàlisi de la partició del sistema:"
df -h | grep -E "/system|/data|/usrdata"

# Comprova el subsistema Android
echo -e "\n2. Comprovació del subsistema Android:"
if command -v adb &> /dev/null; then
    adb devices
    if adb devices | grep -q "device$"; then
        echo "✓ Connexió ADB disponible"

        # Comprova les propietats del sistema
        adb shell getprop | grep -E "ro.build|persist.vendor"

        # Comprova els processos en execució
        adb shell ps | grep rayhunter

        # Comprova els registres del sistema
        echo "Errors recents del sistema:"
        adb logcat -d | grep -E "ERROR|FATAL" | tail -10
    else
        echo "✗ No hi ha cap connexió ADB disponible"
    fi
else
    echo "ADB no està disponible; s’utilitzen mètodes alternatius"
fi

# Comprova el microprogramari del mòdem
echo -e "\n3. Anàlisi del microprogramari del mòdem:"
if [ -c /dev/diag ]; then
    # Utilitza una eina personalitzada per consultar el microprogramari del mòdem
    python3 << 'EOF'
import serial
import struct
import time

try:
    # Obre la interfície de diagnòstic
    diag = serial.Serial('/dev/diag', 115200, timeout=1)

    # Consulta simplificada de la versió del microprogramari
    # Això requereix una implementació correcta del protocol DIAG
    print("Es pot accedir a la interfície de diagnòstic del mòdem")
    diag.close()
except Exception as e:
    print(f"Ha fallat l’accés al diagnòstic del mòdem: {e}")
EOF
fi

# Comprova els problemes específics de l’operador
echo -e "\n4. Comprovació de la configuració de l’operador:"
echo "Preferències de banda actuals:"
cat /data/rayhunter/config.toml | grep -A 5 -B 5 "band"

echo "Estat del registre a la xarxa:"
# Comprova el registre amb tots els operadors disponibles
if command -v qmicli &> /dev/null; then
    qmicli -d /dev/cdc-wdm0 --nas-get-home-network
    qmicli -d /dev/cdc-wdm0 --nas-get-preferred-networks
fi
```

**Resolució de problemes del TP-Link M7350**:
```bash
#!/bin/bash
# Resolució de problemes específica del TP-Link M7350

echo "=== Diagnòstic avançat del TP-Link M7350 ==="

# Comprova el funcionament de la targeta SD
echo "1. Diagnòstic de la targeta SD:"
if mountpoint -q /media/sd; then
    echo "✓ La targeta SD està muntada"
    df -h /media/sd

    # Comprova l’estat de la targeta SD
    echo "Comprovació del sistema de fitxers de la targeta SD:"
    fsck -n /dev/mmcblk0p1 2>&1 | head -10

    # Comprova els permisos d’escriptura
    touch /media/sd/test_write 2>/dev/null && rm /media/sd/test_write
    if [ $? -eq 0 ]; then
        echo "✓ Permisos d’escriptura de la targeta SD correctes"
    else
        echo "✗ Han fallat els permisos d’escriptura de la targeta SD"
    fi
else
    echo "✗ La targeta SD no està muntada"
    echo "Dispositius de blocs disponibles:"
    lsblk | grep -E "mmc|sd"
fi

# Comprova el sistema OpenWrt
echo -e "\n2. Anàlisi del sistema OpenWrt:"
echo "Informació del sistema:"
cat /proc/version
uname -a

echo "Memòria disponible:"
free -h

echo "Càrrega del sistema:"
uptime

# Comprova la instal·lació dels paquets
echo "Paquets instal·lats relacionats amb RayHunter:"
opkg list-installed | grep -E "python|kmod|usb"

# Comprova els mòduls del nucli
echo -e "\n3. Estat dels mòduls del nucli:"
lsmod | grep -E "diag|qmi|cdc|usb"

# Comprova la interfície de diagnòstic USB
echo "Dispositius de diagnòstic USB:"
lsusb -t
ls -la /dev/ttyUSB* 2>/dev/null || echo "No s’han trobat dispositius sèrie USB"
```

### Procediments de recuperació

**Scripts de recuperació del sistema**:
```bash
#!/bin/bash
# Recuperació d’emergència del sistema RayHunter

BACKUP_DIR="/data/rayhunter/backup"
CONFIG_FILE="/data/rayhunter/config.toml"
RECOVERY_LOG="/var/log/rayhunter/recovery.log"

log_message() {
    echo "$(date): $1" | tee -a "$RECOVERY_LOG"
}

create_backup() {
    log_message "Creating system backup..."
    mkdir -p "$BACKUP_DIR"

    # Fes una còpia de seguretat de la configuració
    cp "$CONFIG_FILE" "$BACKUP_DIR/config_$(date +%Y%m%d_%H%M%S).toml"

    # Fes una còpia de seguretat de les gravacions (últimes 24 hores)
    find /data/rayhunter/recordings -name "*.qmdl" -mtime -1 -exec cp {} "$BACKUP_DIR/" \;

    # Fes una còpia de seguretat dels registres
    tar -czf "$BACKUP_DIR/logs_$(date +%Y%m%d_%H%M%S).tar.gz" /data/rayhunter/logs/

    log_message "Backup completed"
}

reset_configuration() {
    log_message "Resetting configuration to defaults..."

    # Atura el servei RayHunter
    systemctl stop rayhunter_daemon

    # Restableix la configuració de fàbrica
    cp /etc/rayhunter/config.toml.default "$CONFIG_FILE"

    # Esborra els fitxers de memòria cau que causen problemes
    rm -f /data/rayhunter/cache/*

    # Restableix els permisos
    chown -R rayhunter:rayhunter /data/rayhunter/
    chmod -R 755 /data/rayhunter/

    log_message "Configuration reset completed"
}

factory_reset() {
    log_message "Performing factory reset..."

    # Fes primer una còpia de seguretat
    create_backup

    # Atura tots els serveis de RayHunter
    systemctl stop rayhunter_daemon
    systemctl disable rayhunter_daemon

    # Elimina totes les dades de RayHunter (excepte les còpies de seguretat)
    find /data/rayhunter -type f ! -path "*/backup/*" -delete

    # Torna a instal·lar RayHunter
    cd /tmp
    wget -O rayhunter-latest.zip "https://github.com/EFForg/rayhunter/releases/latest/download/rayhunter-linux-x64.zip"
    unzip rayhunter-latest.zip
    ./installer $(detect_device_type)

    log_message "Factory reset completed"
}

detect_device_type() {
    # Detecta automàticament el tipus de dispositiu per reinstal·lar-lo
    if grep -q "Orbic" /proc/cpuinfo || [ -d "/android_root" ]; then
        echo "orbic"
    elif grep -q "MT7620" /proc/cpuinfo || [ -f "/etc/openwrt_version" ]; then
        echo "tplink"
    else
        echo "unknown"
    fi
}

# Menú principal de recuperació
echo "=== Recuperació d'emergència del sistema RayHunter ==="
echo "1. Crea només una còpia de seguretat"
echo "2. Restableix la configuració als valors predeterminats"
echo "3. Restabliment de fàbrica (destructiu)"
echo "4. Diagnòstic del sistema"
echo "5. Surt"

read -p "Selecciona una opció (1-5): " choice

case $choice in
    1) create_backup ;;
    2) reset_configuration ;;
    3)
        read -p "Segur que vols continuar? Això esborrarà totes les dades excepte les còpies de seguretat (y/N): " confirm
        if [ "$confirm" = "y" ] || [ "$confirm" = "Y" ]; then
            factory_reset
        else
            echo "S'ha cancel·lat el restabliment de fàbrica"
        fi
        ;;
    4)
        echo "S'estan executant els diagnòstics del sistema..."
        # Executa tots els scripts de diagnòstic
        /opt/rayhunter/scripts/performance_check.sh
        /opt/rayhunter/scripts/network_diagnostics.sh
        ;;
    5) exit 0 ;;
    *) echo "Opció no vàlida" ;;
esac
```

## Escenaris d’integració per a experts

{{< figure src="rayhunter-soc-integration-workflow.webp" alt="Diagrama de flux que mostra les dades de la RayHunter REST API en un tauler d’un centre d’operacions de seguretat, juntament amb alertes SIEM i fluxos d’exportació de recerca." >}}

### Integració en entorns de recerca

**Configuració per a recerca acadèmica**:
```python
#!/usr/bin/env python3
"""
Plataforma d’integració de recerca de RayHunter
Configuració avançada per a la recerca acadèmica en seguretat mòbil
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
        """Configura un esquema complet per a la base de dades de recerca"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        # Esquema ampliat per a dades de recerca
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
        """Fes un experiment controlat amb els paràmetres especificats"""
        session_id = f"exp_{datetime.now().strftime('%Y%m%d_%H%M%S')}"

        # Configura RayHunter per a l’experiment
        self.configure_rayhunter_for_research(experiment_config)

        # Inicia la recollida de dades
        collection_start = datetime.now()

        # Executa l’experiment durant el temps especificat
        experiment_duration = experiment_config.get('duration_minutes', 60)

        # Recull les mesures de referència
        baseline_data = self.collect_baseline_measurements(experiment_duration // 3)

        # Introdueix variables controlades si s’especifiquen
        if experiment_config.get('introduce_threats', False):
            threat_data = self.simulate_threat_scenarios(experiment_config['threat_scenarios'])

        # Recull dades posteriors a la intervenció
        post_data = self.collect_post_measurements(experiment_duration // 3)

        # Analitza els resultats
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
        """Fes una anàlisi estadística dels patrons de detecció d’amenaces"""
        conn = sqlite3.connect(self.db_path)

        # Consulta les observacions d’amenaces
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
            return {"error": "No hi ha dades disponibles per a l’anàlisi"}

        # Anàlisi estadística
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

        # Anàlisi de correlació ambiental
        for env_type in df['environment_type'].unique():
            env_data = df[df['environment_type'] == env_type]
            analysis['environmental_correlation'][env_type] = {
                'threat_frequency': len(env_data) / time_period_days,
                'average_confidence': env_data['confidence_score'].mean(),
                'threat_type_distribution': env_data['threat_type'].value_counts().to_dict()
            }

        # Genera visualitzacions
        self.generate_research_visualizations(df, analysis)

        return analysis

    def generate_research_visualizations(self, df, analysis):
        """Genera visualitzacions de recerca completes"""
        fig, axes = plt.subplots(2, 3, figsize=(20, 12))

        # Distribució dels tipus d’amenaça
        threat_counts = df['threat_type'].value_counts()
        axes[0, 0].pie(threat_counts.values, labels=threat_counts.index, autopct='%1.1f%%')
        axes[0, 0].set_title('Distribució del tipus d’amenaça')

        # Distribució de les puntuacions de confiança
        axes[0, 1].hist(df['confidence_score'], bins=20, alpha=0.7)
        axes[0, 1].set_title('Distribució de la puntuació de confiança')
        axes[0, 1].set_xlabel('Puntuació de confiança')
        axes[0, 1].set_ylabel('Freqüència')

        # Patrons temporals
        df['hour'] = pd.to_datetime(df['timestamp']).dt.hour
        hourly_counts = df.groupby('hour').size()
        axes[0, 2].bar(hourly_counts.index, hourly_counts.values)
        axes[0, 2].set_title('Amenaces per hora del dia')
        axes[0, 2].set_xlabel('Hora')
        axes[0, 2].set_ylabel('Nombre d’amenaces')

        # Entorn en relació amb la confiança
        sns.boxplot(data=df, x='environment_type', y='confidence_score', ax=axes[1, 0])
        axes[1, 0].set_title('Confiança segons el tipus d’entorn')
        axes[1, 0].tick_params(axis='x', rotation=45)

        # Mapa de calor de correlació
        numeric_df = df.select_dtypes(include=[np.number])
        correlation_matrix = numeric_df.corr()
        sns.heatmap(correlation_matrix, annot=True, ax=axes[1, 1])
        axes[1, 1].set_title('Matriu de correlació')

        # Anàlisi de falsos positius
        if 'false_positive_assessment' in df.columns:
            fp_data = df['false_positive_assessment'].value_counts()
            axes[1, 2].bar(fp_data.index, fp_data.values)
            axes[1, 2].set_title('Avaluació dels falsos positius')
            axes[1, 2].tick_params(axis='x', rotation=45)

        plt.tight_layout()
        plt.savefig(f'/data/research/analysis/visualization_{datetime.now().strftime("%Y%m%d_%H%M%S")}.png',
                   dpi=300, bbox_inches='tight')
        plt.close()

    def export_research_data(self, format='csv', time_range_days=None):
        """Exporta dades de recerca en diversos formats per a l’anàlisi externa"""
        conn = sqlite3.connect(self.db_path)

        if time_range_days:
            end_date = datetime.now()
            start_date = end_date - timedelta(days=time_range_days)
            date_filter = f"WHERE timestamp BETWEEN '{start_date.isoformat()}' AND '{end_date.isoformat()}'"
        else:
            date_filter = ""

        # Exporta les observacions d’amenaces
        threat_query = f"SELECT * FROM threat_observations {date_filter}"
        threat_df = pd.read_sql_query(threat_query, conn)

        # Exporta les mesures mòbils
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

## Conclusió

El desplegament avançat de **RayHunter** requereix experiència tècnica en diversos àmbits, com ara els **protocols cel·lulars**, l’**anàlisi RF**, la integració de sistemes i el modelatge d’amenaces. Les tècniques d’aquesta guia ajuden els experts a aprofitar al màxim les capacitats de detecció de **RayHunter** i, alhora, a reduir els falsos positius i la càrrega operativa.

*Aquests són els punts clau de les operacions avançades de **RayHunter**:*

1. **L’optimització d’heurístiques personalitzades** pot reduir els falsos positius un 80% i mantenir una sensibilitat de detecció alta amb una configuració adaptada a l’entorn
2. **L’automatització amb API** permet desplegar a escala empresarial i integrar-se amb els centres d’operacions de seguretat existents
3. **La coordinació de diversos dispositius** ofereix cobertura completa i validació creuada per augmentar la confiança en la detecció d’amenaces
4. **Les metodologies avançades de diagnòstic** afavoreixen un funcionament fiable en entorns diversos i exigents
5. **La integració de recerca** dona suport a la recerca acadèmica i comercial sobre amenaces cel·lulars

Els usuaris experts de **RayHunter** haurien de seguir els avenços en **seguretat cel·lular**, **tecnologia de vigilància** i capacitats de detecció de codi obert. *Les amenaces canvien i exigeixen millorar contínuament les tècniques de detecció i els procediments operatius.*

Les organitzacions que utilitzen **RayHunter** en operacions de seguretat professionals haurien de considerar una integració amb un **centre d’operacions de seguretat** dedicat, formació periòdica del personal i col·laboració amb la comunitat **RayHunter** per compartir informació sobre amenaces i millores de detecció.

Encara no tens el maquinari per a aquestes configuracions avançades? **[Dispositius verificats compatibles amb RayHunter](https://stscollective.com/collections/rayhunter)** es poden trobar a STS Collective. El codi per a lectors **SIMEONONSECURITY** ofereix fins a un 20% de descompte.

{{< centerbutton href="https://stscollective.com/discount/SIMEONONSECURITY" >}}
  Compra dispositius RayHunter i estalvia un 20%
{{< /centerbutton >}}

## Referències

- [Documentació oficial de RayHunter](https://efforg.github.io/rayhunter/introduction.html)
- [Referència de la REST API de RayHunter](https://efforg.github.io/rayhunter/api-docs/)
- [Electronic Frontier Foundation](https://www.eff.org/)
- [Repositori de RayHunter a GitHub](https://github.com/EFForg/rayhunter)
- [Recursos d’anàlisi de protocols cel·lulars](https://www.sharetechnote.com/)
- [Recursos d’anàlisi RF i SDR](https://greatscottgadgets.com/sdr/)
- [Bones pràctiques d’integració de seguretat empresarial](https://www.sans.org/white-papers/)
