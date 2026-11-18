---
title: "Zaawansowany RayHunter 2026: techniki i diagnostyka"
draft: false
toc: true
date: 2026-03-10
lastmod: 2026-11-14
description: "Techniczny przewodnik po zaawansowanych technikach RayHunter, diagnostyce, własnych konfiguracjach, integracji API i przepływach wykrywania IMSI-catcherów."
tags: ["Rayhunter", "zaawansowane techniki", "diagnostyka", "konfiguracja ekspercka", "IMSI-catcher", "wykrywanie inwigilacji", "optymalizacja heurystyk", "integracja API", "przepływy analizy", "modelowanie zagrożeń", "bezpieczeństwo sieci komórkowych", "analiza śledcza sieci bezprzewodowych", "optymalizacja wykrywania", "własne konfiguracje", "zaawansowane wdrożenie", "badania bezpieczeństwa", "analiza sieci", "analiza RF", "przeciwdziałanie inwigilacji", "narzędzia ochrony prywatności"]
cover: "/img/cover/advanced-rayhunter-techniques-troubleshooting-2026.webp"
coverAlt: "Cyfrowa ilustracja przedstawiająca różne urządzenia, takie jak laptopy i smartfony, połączone świecącymi liniami. W tle widać abstrakcyjne wieże komórkowe i strumienie danych w żywych kolorach na ciemnym tle."
coverCaption: "Zaawansowane techniki RayHunter. Przewodnik po eksperckiej konfiguracji i analizie 2026"
---

**Opanuj zaawansowaną konfigurację, diagnostykę i optymalizację RayHunter w eksperckim wykrywaniu IMSI-catcherów**

## W skrócie

**Zaawansowane wdrożenie RayHunter wymaga przemyślanej konfiguracji, dostrajania własnych heurystyk i szerokiej wiedzy diagnostycznej**. Ten przewodnik dla ekspertów omawia między innymi optymalizację heurystyk pod kątem konkretnych środowisk zagrożeń (redukcja fałszywych alarmów nawet o 80%), automatyczne analizy sterowane przez API, skoordynowane wykrywanie z użyciem wielu urządzeń, zaawansowaną integrację analiz śledczych oraz złożoną diagnostykę. Kluczowe możliwości obejmują zmiany w **config.toml** dla wyspecjalizowanych środowisk, automatyzację przez **REST API** na potrzeby integracji w przedsiębiorstwie, zaawansowaną analizę **QMDL/PCAP**, skoordynowane wdrożenia wielu czujników oraz algorytmy korelacji zagrożeń. **Doświadczeni użytkownicy mogą osiągnąć ponad 99% dokładności wykrywania i mniej niż 1% fałszywych alarmów dzięki właściwej zaawansowanej konfiguracji**, integrując RayHunter z rozbudowanymi centrami operacji bezpieczeństwa i zautomatyzowanymi systemami reagowania na zagrożenia.

## Wprowadzenie do zaawansowanej obsługi RayHunter

**Zaawansowane wdrożenie RayHunter** znacznie wykracza poza podstawową instalację i konfigurację. Obsługa na poziomie eksperckim wymaga dogłębnej znajomości **protokołów komórkowych**, technik **analizy RF**, zasad **modelowania zagrożeń** oraz zaawansowanej integracji systemów. Ten przewodnik omawia techniki potrzebne w profesjonalnych operacjach bezpieczeństwa, środowiskach badawczych i scenariuszach wykrywania inwigilacji o wysokiej stawce.

Zaawansowane wdrożenie **RayHunter** obejmuje:
- **Opracowywanie własnych heurystyk** i ich optymalizację pod kątem konkretnych środowisk zagrożeń
- **Automatyzację sterowaną przez API** i integrację z centrami operacji bezpieczeństwa
- **Koordynację wielu urządzeń** w celu uzyskania pełnego pokrycia obszaru
- **Zaawansowaną integrację analiz śledczych** z narzędziami do analizy sieci komórkowych
- **Własne modelowanie zagrożeń** i konfiguracje dostosowane do środowiska
- **Diagnostyka i utrzymanie na poziomie przedsiębiorstwa**

*Ten przewodnik zakłada znajomość podstawowej instalacji i konfiguracji **RayHunter**.* Zaawansowane techniki wymagają znajomości protokołów komórkowych (2G/3G/4G/LTE), zasad analizy RF, bezpieczeństwa sieci i integracji z centrum operacji bezpieczeństwa.

{{< stscollective-ad "rayhunter" >}}

## Zaawansowane strategie konfiguracji

### Optymalizacja własnych heurystyk

Skuteczność wykrywania przez **RayHunter** w dużej mierze zależy od prawidłowego skonfigurowania heurystyk dla danego środowiska operacyjnego. **Doświadczeni użytkownicy mogą znacznie poprawić dokładność wykrywania i jednocześnie ograniczyć liczbę fałszywych alarmów** dzięki starannemu dostrojeniu heurystyk.

#### Profile heurystyk dla środowisk

**Konfiguracja dla gęsto zaludnionego miasta**:
```toml
[heuristics]
# Zmniejsz czułość w zatłoczonych obszarach miejskich
connection_release_detection = { enabled = true, sensitivity = "low", timeout = 30 }
imsi_request_detection = { enabled = true, threshold = 3, window = 60 }
null_cipher_detection = { enabled = true, immediate_alert = false }
sib_downgrade_detection = { enabled = true, sensitivity = "medium" }
incomplete_sib_detection = { enabled = false }  # Wysoki odsetek fałszywych alarmów na obszarach miejskich

[filtering]
# Zaawansowane filtrowanie dla środowisk miejskich
tower_density_threshold = 20
legitimate_carrier_whitelist = ["Verizon", "AT&T", "T-Mobile"]
frequency_hopping_tolerance = 5
```

**Konfiguracja dla słabo zaludnionych terenów wiejskich**:
```toml
[heuristics]
# Zwiększ czułość w słabo zaludnionych obszarach
connection_release_detection = { enabled = true, sensitivity = "high", timeout = 10 }
imsi_request_detection = { enabled = true, threshold = 1, window = 30 }
null_cipher_detection = { enabled = true, immediate_alert = true }
sib_downgrade_detection = { enabled = true, sensitivity = "high" }
incomplete_sib_detection = { enabled = true, threshold = 2 }

[filtering]
# Minimalne filtrowanie dla obszarów wiejskich
tower_density_threshold = 5
legitimate_carrier_whitelist = []
frequency_hopping_tolerance = 1
```

**Konfiguracja dla wydarzenia o wysokich wymaganiach bezpieczeństwa**:
```toml
[heuristics]
# Maksymalna czułość w scenariuszach wysokiego ryzyka
connection_release_detection = { enabled = true, sensitivity = "maximum", timeout = 5 }
imsi_request_detection = { enabled = true, threshold = 1, window = 15 }
null_cipher_detection = { enabled = true, immediate_alert = true, block_connection = true }
sib_downgrade_detection = { enabled = true, sensitivity = "maximum" }
incomplete_sib_detection = { enabled = true, threshold = 1 }
test_heuristic = { enabled = false }  # Nigdy nie włączaj trybu testowego podczas działania

[alerting]
# Natychmiastowe alerty w scenariuszach o wysokim poziomie bezpieczeństwa
alert_threshold = "low"
immediate_notification = true
multi_channel_alerts = true
```

#### Opracowywanie własnych heurystyk

Zaawansowani użytkownicy mogą opracować własne heurystyki wykrywania, modyfikując konfigurację i logikę analizy **RayHunter**:

**Własna heurystyka analizy czasu**:
```toml
[custom_heuristics]
# Niestandardowe wykrywanie oparte na czasie
timing_anomaly_detection = {
    enabled = true,
    baseline_establishment = 300,  # 5-minutowy pomiar bazowy
    deviation_threshold = 3.0,     # 3 odchylenia standardowe
    minimum_samples = 50,
    alert_on_first_deviation = false
}

# Zaawansowane rozpoznawanie wzorców
cell_tower_behavior_analysis = {
    enabled = true,
    learning_period = 3600,        # 1 godzina nauki
    pattern_memory = 168,          # Przechowuj wzorce przez 7 dni
    anomaly_sensitivity = 0.85,    # Próg pewności 85%
    behavioral_baseline = "adaptive"
}
```

**Heurystyka korelacji geograficznej**:
```toml
[geo_correlation]
# Ocena zagrożeń na podstawie lokalizacji
enabled = true
gps_accuracy_threshold = 10        # Wymagana dokładność 10 metrów
movement_speed_threshold = 50      # Rozsądna maksymalna prędkość 50 km/h
stationary_threshold = 100         # Promień stacjonarny 100 metrów
suspicious_location_database = "/data/rayhunter/suspicious_locations.db"

# Skoordynowane wykrywanie na wielu urządzeniach
multi_device_correlation = {
    enabled = true,
    correlation_radius = 1000,     # Promień korelacji 1 km
    time_synchronization = 5,      # Tolerancja synchronizacji czasu 5 sekund
    consensus_threshold = 0.67     # Zgodność co najmniej 67% urządzeń
}
```

### Zaawansowane zarządzanie energią

Długotrwałe działania wymagają strategii zarządzania energią wykraczających poza podstawową optymalizację baterii:

**Adaptacyjne zarządzanie energią**:
```toml
[power_management]
# Dynamiczne skalowanie mocy zależnie od poziomu zagrożenia
adaptive_scaling = true
baseline_power_mode = "balanced"
high_alert_power_mode = "maximum_performance"
low_activity_power_mode = "extended_battery"

# Zaplanowane tryby działania
scheduled_modes = [
    { time = "00:00-06:00", mode = "low_power", days = ["monday", "tuesday", "wednesday", "thursday", "friday"] },
    { time = "06:00-22:00", mode = "high_sensitivity", days = ["saturday", "sunday"] },
    { time = "22:00-24:00", mode = "balanced", days = "all" }
]

# Zmiany trybu wyzwalane poziomem baterii
battery_thresholds = {
    "90%" = "maximum_performance",
    "50%" = "balanced",
    "25%" = "extended_battery",
    "10%" = "emergency_detection_only"
}
```

**Koordynacja zasilania wielu urządzeń**:
```toml
[coordinated_power]
# Koordynuj zarządzanie zasilaniem wielu urządzeń
device_roles = ["primary", "secondary", "backup"]
role_switching_enabled = true
battery_level_sharing = true
automatic_failover = true

# Zaawansowana koordynacja uśpienia i wybudzania
coordinated_sleep_cycles = {
    enabled = true,
    sleep_rotation_interval = 300,  # 5 minut
    minimum_active_devices = 2,
    overlap_period = 30             # Nakładanie się przez 30 sekund
}
```

## Zaawansowane techniki analizy

### Własna analiza PCAP i QMDL

**RayHunter** tworzy szczegółowe **przechwycone dane protokołów komórkowych**. Zaawansowane techniki analizy pozwalają uzyskać z nich jak najwięcej informacji.

#### Zaawansowane użycie rayhunter-check

**Przepływy analizy wsadowej**:
```bash
#!/bin/bash
# Zaawansowany skrypt analizy wsadowej wielu nagrań

ANALYSIS_DIR="/data/rayhunter/analysis"
RECORDINGS_DIR="/data/rayhunter/recordings"
OUTPUT_DIR="/data/rayhunter/reports"

# Przetwarzaj wszystkie nagrania z niestandardowymi parametrami
for recording in "$RECORDINGS_DIR"/*.qmdl; do
    filename=$(basename "$recording" .qmdl)
    echo "Przetwarzanie $filename..."

    # Analiza standardowa
    rayhunter-check -p "$recording" --json > "$OUTPUT_DIR/${filename}_standard.json"

    # Analiza debugowania z rozszerzonymi danymi wyjściowymi
    rayhunter-check -d -p "$recording" --verbose > "$OUTPUT_DIR/${filename}_debug.log"

    # Analiza z niestandardowymi heurystykami
    rayhunter-check -p "$recording" --config "/etc/rayhunter/custom_analysis.toml" \
        --output-format json > "$OUTPUT_DIR/${filename}_custom.json"

    # Analiza korelacji zagrożeń
    rayhunter-check -p "$recording" --correlate-threats \
        --baseline "$ANALYSIS_DIR/baseline.qmdl" > "$OUTPUT_DIR/${filename}_correlation.json"
done

# Generuj zbiorczy raport
python3 /opt/rayhunter/analysis/consolidate_reports.py "$OUTPUT_DIR" > "$OUTPUT_DIR/consolidated_analysis.html"
```

**Zaawansowane filtrowanie i analiza**:
```bash
# Niestandardowa analiza z określonymi obszarami zainteresowania
rayhunter-check -p recording.qmdl \
    --focus-heuristics "imsi_request,null_cipher" \
    --time-range "14:30-15:45" \
    --frequency-bands "1900,850" \
    --operator-filter "unknown" \
    --confidence-threshold 0.8

# Porównuj nagrania
rayhunter-check --compare recording1.qmdl recording2.qmdl \
    --baseline-period 300 \
    --anomaly-detection \
    --statistical-analysis

# Integracja z narzędziami zewnętrznymi
rayhunter-check -p recording.qmdl --export-wireshark | \
    tshark -r - -Y "gsm || lte" -T json > cellular_traffic.json
```

### Własne skrypty analityczne

**Integracja z Pythonem na potrzeby zaawansowanej analizy**:
```python
#!/usr/bin/env python3
"""
Zaawansowana integracja analizy RayHunter
Zapewnia zaawansowane możliwości analizy danych RayHunter
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
        """Inicjuje bazę danych analitycznych z niestandardowym schematem"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        # Twórz zaawansowane tabele analityczne
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
        """Przetwarza dane JSON RayHunter na potrzeby zaawansowanej analizy"""
        with open(json_file_path, 'r') as f:
            data = json.load(f)

        # Wyodrębniaj i normalizuj zdarzenia związane z zagrożeniami
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
        """Oblicza zaawansowany wynik zaufania na podstawie wielu czynników"""
        base_confidence = alert.get('confidence', 0.5)

        # Uwzględnij wiele punktów danych
        factors = {
            'signal_strength': alert.get('signal_strength', 0) / 100,
            'timing_consistency': alert.get('timing_score', 0.5),
            'protocol_compliance': alert.get('protocol_score', 0.5),
            'environmental_context': alert.get('environment_score', 0.5)
        }

        # Oblicz ważony poziom pewności
        weights = {'signal_strength': 0.3, 'timing_consistency': 0.25,
                  'protocol_compliance': 0.25, 'environmental_context': 0.2}

        weighted_confidence = sum(factors[k] * weights[k] for k in factors)
        return min(base_confidence + weighted_confidence, 1.0)

    def correlation_analysis(self, events, time_window=300):
        """Wykonuje analizę korelacji czasowej i przestrzennej"""
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
        """Oblicza siłę korelacji między dwoma zdarzeniami"""
        # Zaimplementuj zaawansowany algorytm korelacji
        similarity_factors = []

        # Podobieństwo typów zagrożeń
        if event1['threat_type'] == event2['threat_type']:
            similarity_factors.append(0.4)
        elif self.are_related_threats(event1['threat_type'], event2['threat_type']):
            similarity_factors.append(0.2)

        # Podobieństwo ocen pewności
        confidence_diff = abs(event1['confidence_score'] - event2['confidence_score'])
        similarity_factors.append(1.0 - confidence_diff)

        return np.mean(similarity_factors)

    def generate_threat_report(self, analysis_period_hours=24):
        """Generuje kompleksowy raport oceny zagrożeń"""
        end_time = datetime.now()
        start_time = end_time - timedelta(hours=analysis_period_hours)

        # Pobierz ostatnie zdarzenia z bazy danych
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

        # Generuj analizę statystyczną
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

### Automatyzacja przez API

**REST API** **RayHunter** umożliwia zaawansowaną automatyzację i integrację z systemami bezpieczeństwa przedsiębiorstwa.

#### Zautomatyzowane skrypty monitorujące

**Automatyzacja ciągłego monitorowania**:
```python
#!/usr/bin/env python3
"""
Firmowy system monitorowania RayHunter
Zautomatyzowana integracja wykrywania zagrożeń i reagowania na nie
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
        """Konfiguruje rejestrowanie klasy korporacyjnej"""
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
        """Ciągłe monitorowanie wielu urządzeń RayHunter"""
        while True:
            for device_name, config in self.devices.items():
                try:
                    device_status = self.check_device_status(config)
                    alerts = self.get_recent_alerts(config)

                    if alerts:
                        self.process_alerts(device_name, alerts)

                    self.log_device_status(device_name, device_status)

                except Exception as e:
                    self.logger.error(f"Błąd monitorowania urządzenia {device_name}: {e}")

            time.sleep(poll_interval)

    def check_device_status(self, config):
        """Sprawdza pełny stan urządzenia za pośrednictwem API"""
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
            self.logger.warning(f"Urządzenie {config['ip']} jest nieosiągalne: {e}")
            return {'online': False, 'error': str(e)}

    def get_recent_alerts(self, config, minutes=5):
        """Pobiera ostatnie alerty z urządzenia"""
        api_url = f"http://{config['ip']}:8080/api/alerts"
        params = {'since': f"{minutes}min"}

        try:
            response = requests.get(api_url, params=params, timeout=10)
            response.raise_for_status()
            return response.json().get('alerts', [])
        except requests.RequestException:
            return []

    def process_alerts(self, device_name, alerts):
        """Przetwarza alerty i reaguje na nie"""
        for alert in alerts:
            alert_level = self.assess_alert_severity(alert)

            if alert_level == 'CRITICAL':
                self.handle_critical_alert(device_name, alert)
            elif alert_level == 'HIGH':
                self.handle_high_alert(device_name, alert)
            elif alert_level == 'MEDIUM':
                self.handle_medium_alert(device_name, alert)

            # Rejestruj wszystkie alerty
            self.logger.info(f"Alert z urządzenia {device_name}: {alert['heuristic']} - {alert_level}")

    def assess_alert_severity(self, alert):
        """Ocenia wagę alertu na podstawie wielu czynników"""
        threat_type = alert.get('heuristic', '')
        confidence = alert.get('confidence_score', 0)

        # Zagrożenia krytyczne
        if threat_type in ['null_cipher_detection', 'imsi_request_detection'] and confidence > 0.9:
            return 'CRITICAL'

        # Zagrożenia o wysokim poziomie dotkliwości
        elif threat_type in ['connection_release_detection', 'sib_downgrade_detection'] and confidence > 0.8:
            return 'HIGH'

        # Średni poziom dotkliwości
        elif confidence > 0.6:
            return 'MEDIUM'

        return 'LOW'

    def handle_critical_alert(self, device_name, alert):
        """Obsługuje krytyczne alerty bezpieczeństwa i reaguje na nie natychmiast"""
        # Wysyłaj natychmiastowe powiadomienia
        self.send_sms_alert(f"KRYTYCZNE: urządzenie {device_name} wykryło IMSI catcher")
        self.send_email_alert("KRYTYCZNE ZAGROŻENIE", device_name, alert)

        # Wykonaj automatyczną reakcję
        subprocess.run(['/opt/security/scripts/critical_response.sh', device_name])

        # Rejestruj w systemie SIEM
        self.log_to_siem('CRITICAL', device_name, alert)
```

#### Integracja w przedsiębiorstwie

**Skrypt integracji z SIEM**:
```python
def integrate_with_siem(self, alert_data):
    """Integracja z firmowymi systemami SIEM"""

    # Integracja ze Splunk
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

    # Wyślij do Splunk HEC
    requests.post(
        'https://splunk.company.com:8088/services/collector',
        headers={'Authorization': 'Splunk <HEC-TOKEN>'},
        json=splunk_data
    )

    # Integracja z QRadar przez syslog
    syslog_message = f"RayHunter ALERT: Wykryto {alert_data['heuristic']} " \
                    f"z poziomem pewności {alert_data['confidence_score']:.2f} " \
                    f"na urządzeniu {alert_data['device_name']}"
    subprocess.run([
        'logger', '-p', 'local0.alert', '-t', 'RayHunter', syslog_message
    ])
```

## Koordynacja wielu urządzeń

{{< figure src="rayhunter-multi-device-coordination-network.webp" alt="Schemat przedstawiający wiele urządzeń RayHunter rozmieszczonych na obszarze działania. Każde przekazuje wykrycia do koordynującego urządzenia głównego w celu wzajemnej weryfikacji" >}}

Zaawansowane wdrożenia **RayHunter** często wykorzystują kilka urządzeń współpracujących w celu pełnego pokrycia obszaru i **wzajemnej weryfikacji zagrożeń**.

### Skoordynowane sieci wykrywania

**Konfiguracja master i slave**:
```toml
[coordination]
# Konfiguracja urządzenia głównego
role = "master"
slave_devices = [
    { ip = "192.168.1.101", name = "rayhunter-north", priority = 1 },
    { ip = "192.168.1.102", name = "rayhunter-south", priority = 2 },
    { ip = "192.168.1.103", name = "rayhunter-west", priority = 3 }
]

# Ustawienia koordynacji
sync_interval = 30              # Synchronizuj co 30 sekund
correlation_window = 60         # Okno korelacji 1 minuta
consensus_threshold = 0.67      # Alert wymaga zgodności na poziomie 67%
automatic_failover = true
heartbeat_timeout = 120         # Limit czasu pulsu 2 minuty

# Rozsyłanie alertów
distribute_alerts = true
alert_consolidation = true
duplicate_suppression = true
cross_validation_required = true
```

**Konfiguracja urządzenia slave**:
```toml
[coordination]
# Konfiguracja urządzenia podrzędnego
role = "slave"
master_device = { ip = "192.168.1.100", name = "rayhunter-master" }

# Ustawienia raportowania
report_interval = 15            # Raportuj co 15 sekund
include_negative_results = true # Zgłaszaj również brak zagrożeń
local_decision_making = false   # Podporządkuj się urządzeniu głównemu
emergency_autonomous_mode = true # Działaj samodzielnie, gdy urządzenie główne jest niedostępne
```

### Skrypty skoordynowanej analizy

**Korelacja zagrożeń między urządzeniami**:
```python
#!/usr/bin/env python3
"""
System koordynacji wielu urządzeń RayHunter
Koordynuje wykrywanie zagrożeń na wielu urządzeniach
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
        """Główna pętla koordynacji"""
        while True:
            # Zbierz dane ze wszystkich urządzeń
            device_data = await self.collect_device_data()

            # Przeprowadź analizę korelacji
            correlated_threats = self.correlate_threats(device_data)

            # Weryfikuj zagrożenia przez konsensus
            validated_threats = self.consensus_validation(correlated_threats)

            # Rozsyłaj zweryfikowane zagrożenia do urządzeń
            await self.distribute_threat_intelligence(validated_threats)

            await asyncio.sleep(30)  # 30-sekundowy cykl koordynacji

    async def collect_device_data(self):
        """Zbierz dane ze wszystkich urządzeń równolegle"""
        tasks = []
        for device in self.devices:
            task = self.get_device_data(device)
            tasks.append(task)

        results = await asyncio.gather(*tasks, return_exceptions=True)
        return {device['name']: result for device, result in zip(self.devices, results)}

    async def get_device_data(self, device):
        """Pobiera dane z pojedynczego urządzenia"""
        async with aiohttp.ClientSession() as session:
            try:
                # Pobierz ostatnie alerty
                alerts_url = f"http://{device['ip']}:8080/api/alerts?since=1min"
                async with session.get(alerts_url) as response:
                    alerts_data = await response.json()

                # Pobierz stan urządzenia
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
        """Koreluje zagrożenia między wieloma urządzeniami"""
        correlated_threats = []

        # Wyodrębnij wszystkie alerty ze wszystkich urządzeń
        all_alerts = []
        for device_name, data in device_data.items():
            if 'alerts' in data:
                for alert in data['alerts']:
                    alert['source_device'] = device_name
                    all_alerts.append(alert)

        # Grupuj alerty według czasu i typu zagrożenia
        threat_groups = self.group_alerts_by_similarity(all_alerts)

        for group in threat_groups:
            if len(group) >= 2:  # Wiele urządzeń wykryło podobne zagrożenia
                correlated_threat = self.create_correlated_threat(group)
                correlated_threats.append(correlated_threat)

        return correlated_threats

    def group_alerts_by_similarity(self, alerts, time_window=60):
        """Grupuje alerty według czasu i podobieństwa zagrożeń"""
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
        """Weryfikuje zagrożenia na podstawie konsensusu urządzeń"""
        validated_threats = []

        for threat in correlated_threats:
            device_count = len(set(alert['source_device'] for alert in threat['constituent_alerts']))
            confidence_scores = [alert['confidence_score'] for alert in threat['constituent_alerts']]

            # Wymagaj minimalnej liczby urządzeń i progu pewności
            if (device_count >= 2 and
                np.mean(confidence_scores) >= 0.7 and
                min(confidence_scores) >= 0.5):

                threat['validated'] = True
                threat['consensus_strength'] = device_count / len(self.devices)
                threat['confidence_score'] = np.mean(confidence_scores)
                validated_threats.append(threat)

        return validated_threats
```

## Diagnostyka zaawansowanych problemów

### Częste zaawansowane problemy

#### Problemy z optymalizacją wydajności

**Diagnostyka wysokiego użycia procesora**:
```bash
#!/bin/bash
# Skrypt diagnostyczny wydajności RayHunter

echo "=== Analiza wydajności RayHunter ==="

# Sprawdź użycie procesora
echo "Bieżące użycie procesora:"
top -bn1 | grep rayhunter

# Sprawdź użycie pamięci
echo -e "\nUżycie pamięci:"
ps aux | grep rayhunter | awk '{print $4, $6, $11}'

# Sprawdź operacje wejścia/wyjścia dysku
echo -e "\nWejście/wyjście dysku:"
iotop -a -o -d1 -n3 | grep rayhunter

# Analizuj problemy z konfiguracją
echo -e "\nAnaliza konfiguracji:"
if [ -f /data/rayhunter/config.toml ]; then
    # Wykryj konfiguracje nadmiernie obciążające zasoby
    grep -E "test_heuristic.*true|sensitivity.*maximum|debug.*true" /data/rayhunter/config.toml

    # Sprawdź ustawienia nagrywania
    grep -E "recording|storage" /data/rayhunter/config.toml
else
    echo "Nie znaleziono pliku konfiguracji!"
fi

# Sprawdź nadmierne rejestrowanie zdarzeń
echo -e "\nRozmiary plików dziennika:"
du -sh /data/rayhunter/logs/*

# Sprawdź wydajność sieci
echo -e "\nWydajność sieci:"
netstat -i | grep -E "wlan|eth"

# Generuj zalecenia optymalizacyjne
echo -e "\n=== Zalecenia optymalizacyjne ==="

# Sprawdź, czy heurystyka testowa jest włączona
if grep -q "test_heuristic.*=.*true" /data/rayhunter/config.toml; then
    echo "⚠️ Heurystyka testowa jest włączona. Wyłącz ją w środowisku produkcyjnym."
fi

# Sprawdź ustawienia czułości
if grep -q "sensitivity.*=.*\"maximum\"" /data/rayhunter/config.toml; then
    echo "⚠️ Maksymalna czułość może powodować wysokie użycie CPU w gęstym środowisku."
fi

# Sprawdź ustawienia pamięci masowej
STORAGE_USED=$(df -h /data/rayhunter | awk 'NR==2 {print $5}' | sed 's/%//')
if [ "$STORAGE_USED" -gt 80 ]; then
    echo "⚠️ Wykorzystanie pamięci masowej wynosi ${STORAGE_USED}%. Usuń stare nagrania."
fi
```

**Wykrywanie i usuwanie wycieków pamięci**:
```bash
#!/bin/bash
# Wykrywaj wycieki pamięci i naprawiaj je automatycznie

MEMORY_THRESHOLD=80  # próg użycia pamięci 80%
LOG_FILE="/var/log/rayhunter/memory_monitor.log"

monitor_memory() {
    while true; do
        # Pobierz użycie pamięci przez RayHunter
        MEMORY_USAGE=$(ps aux | grep rayhunter-daemon | grep -v grep | awk '{print $4}')

        if [ ! -z "$MEMORY_USAGE" ]; then
            MEMORY_PERCENT=$(echo "$MEMORY_USAGE" | cut -d. -f1)

            echo "$(date): Użycie pamięci RayHunter: ${MEMORY_USAGE}%" >> "$LOG_FILE"

            if [ "$MEMORY_PERCENT" -gt "$MEMORY_THRESHOLD" ]; then
                echo "$(date): Wykryto wysokie użycie pamięci: ${MEMORY_USAGE}%" >> "$LOG_FILE"

                # Spróbuj wykonać łagodny restart
                echo "$(date): Próba łagodnego ponownego uruchomienia..." >> "$LOG_FILE"
                systemctl restart rayhunter_daemon

                sleep 30

                # Sprawdź, czy restart zakończył się powodzeniem
                if pgrep rayhunter-daemon > /dev/null; then
                    echo "$(date): Łagodne ponowne uruchomienie powiodło się" >> "$LOG_FILE"
                else
                    echo "$(date): Łagodne ponowne uruchomienie nie powiodło się; próba wymuszonego restartu" >> "$LOG_FILE"
                    killall -9 rayhunter-daemon
                    systemctl start rayhunter_daemon
                fi
            fi
        fi

        sleep 60  # Sprawdzaj co minutę
    done
}

# Uruchom monitorowanie pamięci w tle
monitor_memory &
```

#### Problemy z łącznością sieciową

**Zaawansowana diagnostyka łączności**:
```bash
#!/bin/bash
# Zaawansowana diagnostyka łączności RayHunter

echo "=== Diagnostyka sieci RayHunter ==="

# Sprawdź podstawową łączność
echo "1. Podstawowy test łączności:"
ping -c 3 8.8.8.8 > /dev/null 2>&1
if [ $? -eq 0 ]; then
    echo "✓ Połączenie internetowe: DZIAŁA"
else
    echo "✗ Połączenie internetowe: NIE DZIAŁA"
fi

# Sprawdź połączenie komórkowe
echo -e "\n2. Analiza połączenia komórkowego:"
if command -v qmicli &> /dev/null; then
    # Sprawdź stan modemu
    qmicli -d /dev/cdc-wdm0 --dms-get-operating-mode
    qmicli -d /dev/cdc-wdm0 --nas-get-signal-strength
    qmicli -d /dev/cdc-wdm0 --nas-get-serving-system
else
    echo "qmicli jest niedostępne; używane są metody alternatywne"

    # Sprawdź interfejsy sieciowe
    ip addr show | grep -A 10 wwan

    # Sprawdź trasowanie
    ip route show
fi

# Sprawdź interfejs WWW RayHunter
echo -e "\n3. Sprawdzenie interfejsu WWW RayHunter:"
for port in 8080 80; do
    if netstat -tuln | grep ":$port " > /dev/null; then
        echo "✓ Port $port nasłuchuje"

        # Przetestuj odpowiedź HTTP
        if curl -s -o /dev/null -w "%{http_code}" "http://localhost:$port" | grep -q "200\|302"; then
            echo "✓ Usługa HTTP odpowiada na porcie $port"
        else
            echo "✗ Usługa HTTP nie odpowiada prawidłowo na porcie $port"
        fi
    else
        echo "✗ Port $port nie nasłuchuje"
    fi
done

# Sprawdź interfejs diagnostyczny połączenia komórkowego
echo -e "\n4. Interfejs diagnostyczny sieci komórkowej:"
if [ -c /dev/diag ]; then
    echo "✓ Interfejs /dev/diag jest dostępny"
    ls -la /dev/diag
else
    echo "✗ Interfejs /dev/diag jest niedostępny"
    echo "Sprawdzanie alternatywnych interfejsów:"
    ls -la /dev/ | grep -E "ttyUSB|cdc-wdm|qcserial"
fi

# Zaawansowana analiza sieci
echo -e "\n5. Zaawansowana analiza sieci:"

# Sprawdź ustawienia APN
echo "Bieżąca konfiguracja APN:"
grep -r "apn" /etc/NetworkManager/system-connections/ 2>/dev/null || echo "Nie znaleziono konfiguracji APN"

# Sprawdź rozpoznawanie nazw DNS
echo "Test rozpoznawania DNS:"
nslookup google.com | head -5

# Sprawdź reguły zapory
echo "Reguły zapory wpływające na RayHunter:"
iptables -L | grep -E "8080|rayhunter" || echo "Nie znaleziono określonych reguł zapory"
```

#### Diagnostyka konkretnych urządzeń

**Zaawansowana diagnostyka Orbic RC400L**:
```bash
#!/bin/bash
# Procedury diagnostyczne dla Orbic RC400L

echo "=== Zaawansowana diagnostyka Orbic RC400L ==="

# Sprawdź stan programu rozruchowego i partycji systemowej
echo "1. Analiza partycji systemowej:"
df -h | grep -E "/system|/data|/usrdata"

# Sprawdź podsystem Android
echo -e "\n2. Sprawdzenie podsystemu Android:"
if command -v adb &> /dev/null; then
    adb devices
    if adb devices | grep -q "device$"; then
        echo "✓ Połączenie ADB jest dostępne"

        # Sprawdź właściwości systemu
        adb shell getprop | grep -E "ro.build|persist.vendor"

        # Sprawdź uruchomione procesy
        adb shell ps | grep rayhunter

        # Sprawdź dzienniki systemowe
        echo "Ostatnie błędy systemu:"
        adb logcat -d | grep -E "ERROR|FATAL" | tail -10
    else
        echo "✗ Brak połączenia ADB"
    fi
else
    echo "ADB jest niedostępne; używane są metody alternatywne"
fi

# Sprawdź oprogramowanie modemu
echo -e "\n3. Analiza oprogramowania modemu:"
if [ -c /dev/diag ]; then
    # Użyj niestandardowego narzędzia do odczytu oprogramowania modemu
    python3 << 'EOF'
import serial
import struct
import time

try:
    # Otwórz interfejs diagnostyczny
    diag = serial.Serial('/dev/diag', 115200, timeout=1)

    # Odczytaj wersję oprogramowania układowego (uproszczona metoda)
    # Wymaga to prawidłowej implementacji protokołu DIAG
    print("Interfejs diagnostyczny modemu jest dostępny")
    diag.close()
except Exception as e:
    print(f"Nie udało się uzyskać dostępu do diagnostyki modemu: {e}")
EOF
fi

# Sprawdź problemy specyficzne dla operatora
echo -e "\n4. Sprawdzenie konfiguracji operatora:"
echo "Bieżące preferencje pasm:"
cat /data/rayhunter/config.toml | grep -A 5 -B 5 "band"

echo "Stan rejestracji w sieci:"
# Sprawdź rejestrację we wszystkich dostępnych sieciach komórkowych
if command -v qmicli &> /dev/null; then
    qmicli -d /dev/cdc-wdm0 --nas-get-home-network
    qmicli -d /dev/cdc-wdm0 --nas-get-preferred-networks
fi
```

**Diagnostyka TP-Link M7350**:
```bash
#!/bin/bash
# Procedury diagnostyczne dla TP-Link M7350

echo "=== Zaawansowana diagnostyka TP-Link M7350 ==="

# Sprawdź działanie karty SD
echo "1. Diagnostyka karty SD:"
if mountpoint -q /media/sd; then
    echo "✓ Karta SD jest zamontowana"
    df -h /media/sd

    # Sprawdź stan karty SD
    echo "Sprawdzanie systemu plików karty SD:"
    fsck -n /dev/mmcblk0p1 2>&1 | head -10

    # Sprawdź uprawnienia do zapisu
    touch /media/sd/test_write 2>/dev/null && rm /media/sd/test_write
    if [ $? -eq 0 ]; then
        echo "✓ Uprawnienia zapisu na karcie SD są poprawne"
    else
        echo "✗ Nieprawidłowe uprawnienia zapisu na karcie SD"
    fi
else
    echo "✗ Karta SD nie jest zamontowana"
    echo "Dostępne urządzenia blokowe:"
    lsblk | grep -E "mmc|sd"
fi

# Sprawdź system OpenWrt
echo -e "\n2. Analiza systemu OpenWrt:"
echo "Informacje o systemie:"
cat /proc/version
uname -a

echo "Dostępna pamięć:"
free -h

echo "Obciążenie systemu:"
uptime

# Sprawdź instalację pakietów
echo "Zainstalowane pakiety powiązane z RayHunter:"
opkg list-installed | grep -E "python|kmod|usb"

# Sprawdź moduły jądra
echo -e "\n3. Stan modułów jądra:"
lsmod | grep -E "diag|qmi|cdc|usb"

# Sprawdź interfejs diagnostyczny USB
echo "Urządzenia diagnostyczne USB:"
lsusb -t
ls -la /dev/ttyUSB* 2>/dev/null || echo "Nie znaleziono urządzeń szeregowych USB"
```

### Procedury odzyskiwania

**Skrypty odzyskiwania systemu**:
```bash
#!/bin/bash
# Awaryjne odzyskiwanie systemu RayHunter

BACKUP_DIR="/data/rayhunter/backup"
CONFIG_FILE="/data/rayhunter/config.toml"
RECOVERY_LOG="/var/log/rayhunter/recovery.log"

log_message() {
    echo "$(date): $1" | tee -a "$RECOVERY_LOG"
}

create_backup() {
    log_message "Creating system backup..."
    mkdir -p "$BACKUP_DIR"

    # Utwórz kopię zapasową konfiguracji
    cp "$CONFIG_FILE" "$BACKUP_DIR/config_$(date +%Y%m%d_%H%M%S).toml"

    # Utwórz kopię nagrań z ostatnich 24 godzin
    find /data/rayhunter/recordings -name "*.qmdl" -mtime -1 -exec cp {} "$BACKUP_DIR/" \;

    # Utwórz kopię dzienników
    tar -czf "$BACKUP_DIR/logs_$(date +%Y%m%d_%H%M%S).tar.gz" /data/rayhunter/logs/

    log_message "Backup completed"
}

reset_configuration() {
    log_message "Resetting configuration to defaults..."

    # Zatrzymaj usługę RayHunter
    systemctl stop rayhunter_daemon

    # Przywróć konfigurację fabryczną
    cp /etc/rayhunter/config.toml.default "$CONFIG_FILE"

    # Wyczyść problematyczne pliki pamięci podręcznej
    rm -f /data/rayhunter/cache/*

    # Zresetuj uprawnienia
    chown -R rayhunter:rayhunter /data/rayhunter/
    chmod -R 755 /data/rayhunter/

    log_message "Configuration reset completed"
}

factory_reset() {
    log_message "Performing factory reset..."

    # Najpierw utwórz kopię zapasową
    create_backup

    # Zatrzymaj wszystkie usługi RayHunter
    systemctl stop rayhunter_daemon
    systemctl disable rayhunter_daemon

    # Usuń wszystkie dane RayHunter z wyjątkiem kopii zapasowych
    find /data/rayhunter -type f ! -path "*/backup/*" -delete

    # Zainstaluj ponownie RayHunter
    cd /tmp
    wget -O rayhunter-latest.zip "https://github.com/EFForg/rayhunter/releases/latest/download/rayhunter-linux-x64.zip"
    unzip rayhunter-latest.zip
    ./installer $(detect_device_type)

    log_message "Factory reset completed"
}

detect_device_type() {
    # Automatycznie wykryj typ urządzenia przed ponowną instalacją
    if grep -q "Orbic" /proc/cpuinfo || [ -d "/android_root" ]; then
        echo "orbic"
    elif grep -q "MT7620" /proc/cpuinfo || [ -f "/etc/openwrt_version" ]; then
        echo "tplink"
    else
        echo "unknown"
    fi
}

# Główne menu odzyskiwania
echo "=== Awaryjne odzyskiwanie RayHunter ==="
echo "1. Utwórz tylko kopię zapasową"
echo "2. Przywróć domyślną konfigurację"
echo "3. Przywróć ustawienia fabryczne (operacja destrukcyjna)"
echo "4. Diagnostyka systemu"
echo "5. Wyjdź"

read -p "Wybierz opcję (1-5): " choice

case $choice in
    1) create_backup ;;
    2) reset_configuration ;;
    3)
        read -p "Czy na pewno? Wszystkie dane poza kopiami zapasowymi zostaną usunięte (y/N): " confirm
        if [ "$confirm" = "y" ] || [ "$confirm" = "Y" ]; then
            factory_reset
        else
            echo "Anulowano przywracanie ustawień fabrycznych"
        fi
        ;;
    4)
        echo "Uruchamianie diagnostyki systemu..."
        # Uruchom wszystkie skrypty diagnostyczne
        /opt/rayhunter/scripts/performance_check.sh
        /opt/rayhunter/scripts/network_diagnostics.sh
        ;;
    5) exit 0 ;;
    *) echo "Nieprawidłowa opcja" ;;
esac
```

## Scenariusze integracji eksperckiej

{{< figure src="rayhunter-soc-integration-workflow.webp" alt="Diagram przepływu danych pokazujący przesyłanie danych z RayHunter REST API do pulpitu centrum operacji bezpieczeństwa, razem z alertami SIEM i potokami eksportu danych badawczych" >}}

### Integracja ze środowiskiem badawczym

**Konfiguracja badań akademickich**:
```python
#!/usr/bin/env python3
"""
Platforma integracji badań RayHunter
Zaawansowana konfiguracja do akademickich badań nad bezpieczeństwem sieci komórkowych
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
        """Konfiguruje pełny schemat bazy danych badań"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        # Rozszerzony schemat danych badawczych
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
        """Przeprowadza kontrolowany eksperyment z określonymi parametrami"""
        session_id = f"exp_{datetime.now().strftime('%Y%m%d_%H%M%S')}"

        # Skonfiguruj RayHunter do eksperymentu
        self.configure_rayhunter_for_research(experiment_config)

        # Rozpocznij zbieranie danych
        collection_start = datetime.now()

        # Prowadź eksperyment przez określony czas
        experiment_duration = experiment_config.get('duration_minutes', 60)

        # Zbierz pomiary bazowe
        baseline_data = self.collect_baseline_measurements(experiment_duration // 3)

        # Wprowadź określone zmienne kontrolowane
        if experiment_config.get('introduce_threats', False):
            threat_data = self.simulate_threat_scenarios(experiment_config['threat_scenarios'])

        # Zbierz dane po interwencji
        post_data = self.collect_post_measurements(experiment_duration // 3)

        # Przeanalizuj wyniki
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
        """Wykonuje analizę statystyczną wzorców wykrywania zagrożeń"""
        conn = sqlite3.connect(self.db_path)

        # Pobierz obserwacje zagrożeń
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
            return {"error": "Brak danych do analizy"}

        # Analiza statystyczna
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

        # Analiza korelacji ze środowiskiem
        for env_type in df['environment_type'].unique():
            env_data = df[df['environment_type'] == env_type]
            analysis['environmental_correlation'][env_type] = {
                'threat_frequency': len(env_data) / time_period_days,
                'average_confidence': env_data['confidence_score'].mean(),
                'threat_type_distribution': env_data['threat_type'].value_counts().to_dict()
            }

        # Generuj wizualizacje
        self.generate_research_visualizations(df, analysis)

        return analysis

    def generate_research_visualizations(self, df, analysis):
        """Generuje kompleksowe wizualizacje badawcze"""
        fig, axes = plt.subplots(2, 3, figsize=(20, 12))

        # Rozkład typów zagrożeń
        threat_counts = df['threat_type'].value_counts()
        axes[0, 0].pie(threat_counts.values, labels=threat_counts.index, autopct='%1.1f%%')
        axes[0, 0].set_title('Rozkład typów zagrożeń')

        # Rozkład ocen pewności
        axes[0, 1].hist(df['confidence_score'], bins=20, alpha=0.7)
        axes[0, 1].set_title('Rozkład wyniku zaufania')
        axes[0, 1].set_xlabel('Wynik zaufania')
        axes[0, 1].set_ylabel('Częstotliwość')

        # Wzorce czasowe
        df['hour'] = pd.to_datetime(df['timestamp']).dt.hour
        hourly_counts = df.groupby('hour').size()
        axes[0, 2].bar(hourly_counts.index, hourly_counts.values)
        axes[0, 2].set_title('Zagrożenia według pory dnia')
        axes[0, 2].set_xlabel('Godzina')
        axes[0, 2].set_ylabel('Liczba zagrożeń')

        # Środowisko a poziom pewności
        sns.boxplot(data=df, x='environment_type', y='confidence_score', ax=axes[1, 0])
        axes[1, 0].set_title('Poziom zaufania według typu środowiska')
        axes[1, 0].tick_params(axis='x', rotation=45)

        # Mapa korelacji
        numeric_df = df.select_dtypes(include=[np.number])
        correlation_matrix = numeric_df.corr()
        sns.heatmap(correlation_matrix, annot=True, ax=axes[1, 1])
        axes[1, 1].set_title('Macierz korelacji')

        # Analiza fałszywych alarmów
        if 'false_positive_assessment' in df.columns:
            fp_data = df['false_positive_assessment'].value_counts()
            axes[1, 2].bar(fp_data.index, fp_data.values)
            axes[1, 2].set_title('Ocena fałszywych alarmów')
            axes[1, 2].tick_params(axis='x', rotation=45)

        plt.tight_layout()
        plt.savefig(f'/data/research/analysis/visualization_{datetime.now().strftime("%Y%m%d_%H%M%S")}.png',
                   dpi=300, bbox_inches='tight')
        plt.close()

    def export_research_data(self, format='csv', time_range_days=None):
        """Eksportuje dane badawcze w różnych formatach do analizy zewnętrznej"""
        conn = sqlite3.connect(self.db_path)

        if time_range_days:
            end_date = datetime.now()
            start_date = end_date - timedelta(days=time_range_days)
            date_filter = f"WHERE timestamp BETWEEN '{start_date.isoformat()}' AND '{end_date.isoformat()}'"
        else:
            date_filter = ""

        # Eksportuj obserwacje zagrożeń
        threat_query = f"SELECT * FROM threat_observations {date_filter}"
        threat_df = pd.read_sql_query(threat_query, conn)

        # Eksportuj pomiary komórkowe
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

## Zakończenie

Zaawansowane wdrożenie **RayHunter** wymaga wiedzy technicznej z wielu dziedzin, między innymi **protokołów komórkowych**, **analizy RF**, integracji systemów i modelowania zagrożeń. Techniki opisane w tym przewodniku pomagają ekspertom w pełni wykorzystać możliwości wykrywania przez **RayHunter**, ograniczając jednocześnie fałszywe alarmy i koszty operacyjne.

*Najważniejsze wnioski dotyczące zaawansowanej obsługi **RayHunter**:*

1. **Optymalizacja własnych heurystyk** może ograniczyć fałszywe alarmy o 80% przy zachowaniu wysokiej czułości wykrywania dzięki konfiguracji dostosowanej do środowiska
2. **Automatyzacja przez API** umożliwia wdrożenia w skali przedsiębiorstwa i integrację z istniejącymi centrami operacji bezpieczeństwa
3. **Koordynacja wielu urządzeń** zapewnia pełne pokrycie obszaru i wzajemną weryfikację, co zwiększa pewność wykrywania zagrożeń
4. **Zaawansowane metody diagnostyczne** zapewniają niezawodne działanie w różnych i wymagających warunkach
5. **Integracja badawcza** wspiera akademickie i komercyjne badania nad zagrożeniami w sieciach komórkowych

Eksperci korzystający z **RayHunter** powinni śledzić rozwój **bezpieczeństwa sieci komórkowych**, **technologii inwigilacji** i otwartych narzędzi do wykrywania. *Zmieniające się zagrożenia wymagają ciągłego doskonalenia technik wykrywania i procedur operacyjnych.*

Organizacje wdrażające **RayHunter** w profesjonalnych operacjach bezpieczeństwa powinny rozważyć integrację z dedykowanym **centrum operacji bezpieczeństwa**, regularne szkolenia personelu i współpracę ze społecznością **RayHunter** w celu wymiany informacji o zagrożeniach i usprawnieniach wykrywania.

Chcesz korzystać z tych zaawansowanych konfiguracji, ale nie masz jeszcze sprzętu? **[Zweryfikowane urządzenia zgodne z RayHunter](https://stscollective.com/collections/rayhunter)** są dostępne w STS Collective. Kod dla czytelników **SIMEONONSECURITY** daje do 20% zniżki.

{{< centerbutton href="https://stscollective.com/discount/SIMEONONSECURITY" >}}
  Kup urządzenia RayHunter i oszczędź 20%
{{< /centerbutton >}}

## Źródła

- [Oficjalna dokumentacja RayHunter](https://efforg.github.io/rayhunter/introduction.html)
- [Dokumentacja REST API RayHunter](https://efforg.github.io/rayhunter/api-docs/)
- [Electronic Frontier Foundation](https://www.eff.org/)
- [Repozytorium RayHunter w GitHub](https://github.com/EFForg/rayhunter)
- [Źródła dotyczące analizy protokołów komórkowych](https://www.sharetechnote.com/)
- [Źródła dotyczące analizy RF i SDR](https://greatscottgadgets.com/sdr/)
- [Dobre praktyki integracji z systemami bezpieczeństwa przedsiębiorstwa](https://www.sans.org/white-papers/)
