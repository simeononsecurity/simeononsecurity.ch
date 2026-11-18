---
title: "ਉੱਨਤ RayHunter 2026: ਤਕਨੀਕਾਂ ਅਤੇ ਸਮੱਸਿਆ ਨਿਵਾਰਨ"
draft: false
toc: true
date: 2026-03-10
lastmod: 2026-11-14
description: "RayHunter ਦੀਆਂ ਉੱਨਤ ਤਕਨੀਕਾਂ, ਸਮੱਸਿਆ ਨਿਵਾਰਨ, ਕਸਟਮ ਕਨਫਿਗਰੇਸ਼ਨ, API ਏਕੀਕਰਨ ਅਤੇ IMSI catcher ਪਛਾਣ ਵਰਕਫਲੋ ਲਈ ਤਕਨੀਕੀ ਗਾਈਡ।"
tags: ["Rayhunter", "ਉੱਨਤ ਤਕਨੀਕਾਂ", "ਸਮੱਸਿਆ ਨਿਵਾਰਨ", "ਮਾਹਰ ਕਨਫਿਗਰੇਸ਼ਨ", "IMSI catcher", "ਨਿਗਰਾਨੀ ਪਛਾਣ", "ਹਿਊਰਿਸਟਿਕ ਅਨੁਕੂਲਨ", "API ਏਕੀਕਰਨ", "ਵਿਸ਼ਲੇਸ਼ਣ ਵਰਕਫਲੋ", "ਖ਼ਤਰਾ ਮਾਡਲਿੰਗ", "ਸੈਲੂਲਰ ਸੁਰੱਖਿਆ", "ਵਾਇਰਲੈੱਸ ਫੋਰੈਂਸਿਕਸ", "ਪਛਾਣ ਅਨੁਕੂਲਨ", "ਕਸਟਮ ਕਨਫਿਗਰੇਸ਼ਨ", "ਉੱਨਤ ਤੈਨਾਤੀ", "ਸੁਰੱਖਿਆ ਖੋਜ", "ਨੈੱਟਵਰਕ ਵਿਸ਼ਲੇਸ਼ਣ", "RF ਵਿਸ਼ਲੇਸ਼ਣ", "ਨਿਗਰਾਨੀ ਵਿਰੋਧੀ ਉਪਾਅ", "ਪਰਦੇਦਾਰੀ ਸੰਦ"]
cover: "/img/cover/advanced-rayhunter-techniques-troubleshooting-2026.webp"
coverAlt: "ਲੈਪਟਾਪ ਅਤੇ ਸਮਾਰਟਫੋਨ ਵਰਗੇ ਕਈ ਡਿਵਾਈਸਾਂ ਨੂੰ ਚਮਕਦੀਆਂ ਲਾਈਨਾਂ ਨਾਲ ਜੁੜਿਆ ਦਿਖਾਉਂਦਾ ਡਿਜ਼ਿਟਲ ਚਿੱਤਰ। ਗੂੜ੍ਹੇ ਪਿਛੋਕੜ ਵਿੱਚ ਅਮੂਰਤ ਸੈਲੂਲਰ ਟਾਵਰ ਅਤੇ ਡਾਟਾ ਧਾਰਾਵਾਂ ਹਨ।"
coverCaption: "ਉੱਨਤ RayHunter ਤਕਨੀਕਾਂ: ਮਾਹਰ ਕਨਫਿਗਰੇਸ਼ਨ ਅਤੇ ਵਿਸ਼ਲੇਸ਼ਣ ਗਾਈਡ 2026"
---

**ਮਾਹਰ ਪੱਧਰ ’ਤੇ IMSI catcher ਦੀ ਪਛਾਣ ਲਈ RayHunter ਦੀ ਉੱਨਤ ਕਨਫਿਗਰੇਸ਼ਨ, ਸਮੱਸਿਆ ਨਿਵਾਰਨ ਅਤੇ ਅਨੁਕੂਲਨ ਵਿੱਚ ਮਾਹਰ ਬਣੋ**

## ਸੰਖੇਪ ਵਿੱਚ

**RayHunter ਦੀ ਉੱਨਤ ਤੈਨਾਤੀ ਲਈ ਸੋਚੀ-ਸਮਝੀ ਕਨਫਿਗਰੇਸ਼ਨ ਰਣਨੀਤੀ, ਕਸਟਮ ਹਿਊਰਿਸਟਿਕਾਂ ਦੀ ਸੈਟਿੰਗ ਅਤੇ ਸਮੱਸਿਆ ਨਿਵਾਰਨ ਦਾ ਵਿਆਪਕ ਤਜਰਬਾ ਚਾਹੀਦਾ ਹੈ**। ਇਹ ਮਾਹਰ ਗਾਈਡ ਖਾਸ ਖ਼ਤਰੇ ਵਾਲੇ ਮਾਹੌਲ ਲਈ ਹਿਊਰਿਸਟਿਕ ਅਨੁਕੂਲਨ (ਗਲਤ ਸਕਾਰਾਤਮਕ ਨਤੀਜੇ 80% ਤੱਕ ਘਟਾਉਣਾ), API-ਅਧਾਰਿਤ ਆਟੋਮੈਟਿਕ ਵਿਸ਼ਲੇਸ਼ਣ ਵਰਕਫਲੋ, ਕਈ ਡਿਵਾਈਸਾਂ ਰਾਹੀਂ ਤਾਲਮੇਲ ਵਾਲੀ ਪਛਾਣ, ਉੱਨਤ ਫੋਰੈਂਸਿਕ ਏਕੀਕਰਨ ਅਤੇ ਜਟਿਲ ਸਮੱਸਿਆ ਨਿਵਾਰਨ ਤਰੀਕਿਆਂ ਬਾਰੇ ਦੱਸਦੀ ਹੈ। ਮੁੱਖ ਉੱਨਤ ਸਮਰੱਥਾਵਾਂ ਵਿੱਚ ਖਾਸ ਮਾਹੌਲ ਲਈ **config.toml** ਵਿੱਚ ਤਬਦੀਲੀਆਂ, ਐਂਟਰਪ੍ਰਾਈਜ਼ ਏਕੀਕਰਨ ਲਈ **REST API** ਆਟੋਮੇਸ਼ਨ, ਉੱਨਤ **QMDL/PCAP** ਵਿਸ਼ਲੇਸ਼ਣ, ਕਈ ਸੈਂਸਰਾਂ ਦੀ ਤਾਲਮੇਲ ਵਾਲੀ ਤੈਨਾਤੀ ਅਤੇ ਖ਼ਤਰਿਆਂ ਨੂੰ ਜੋੜਨ ਵਾਲੇ ਉੱਨਤ ਐਲਗੋਰਿਦਮ ਸ਼ਾਮਲ ਹਨ। **ਸਹੀ ਉੱਨਤ ਕਨਫਿਗਰੇਸ਼ਨ ਨਾਲ ਤਜਰਬੇਕਾਰ ਵਰਤੋਂਕਾਰ 99% ਤੋਂ ਵੱਧ ਪਛਾਣ ਸਹੀਤਾ ਅਤੇ 1% ਤੋਂ ਘੱਟ ਗਲਤ ਸਕਾਰਾਤਮਕ ਦਰ ਹਾਸਲ ਕਰ ਸਕਦੇ ਹਨ**, ਅਤੇ RayHunter ਨੂੰ ਪੂਰੇ ਸੁਰੱਖਿਆ ਕਾਰਜ ਕੇਂਦਰਾਂ ਤੇ ਆਟੋਮੈਟਿਕ ਖ਼ਤਰਾ ਜਵਾਬ ਪ੍ਰਣਾਲੀਆਂ ਨਾਲ ਜੋੜ ਸਕਦੇ ਹਨ।

## ਉੱਨਤ RayHunter ਕਾਰਜਾਂ ਦੀ ਜਾਣ-ਪਛਾਣ

**RayHunter ਦੀ ਉੱਨਤ ਤੈਨਾਤੀ** ਬੁਨਿਆਦੀ ਇੰਸਟਾਲੇਸ਼ਨ ਅਤੇ ਕਨਫਿਗਰੇਸ਼ਨ ਤੋਂ ਕਿਤੇ ਅੱਗੇ ਜਾਂਦੀ ਹੈ। ਮਾਹਰ ਪੱਧਰ ਦੀ ਵਰਤੋਂ ਲਈ **ਸੈਲੂਲਰ ਪ੍ਰੋਟੋਕੋਲਾਂ**, **RF ਵਿਸ਼ਲੇਸ਼ਣ**, **ਖ਼ਤਰਾ ਮਾਡਲਿੰਗ** ਅਤੇ ਉੱਨਤ ਸਿਸਟਮ ਏਕੀਕਰਨ ਦੀ ਡੂੰਘੀ ਸਮਝ ਚਾਹੀਦੀ ਹੈ। ਇਹ ਗਾਈਡ ਪੇਸ਼ੇਵਰ ਸੁਰੱਖਿਆ ਕਾਰਜਾਂ, ਖੋਜ ਮਾਹੌਲ ਅਤੇ ਉੱਚ ਜੋਖਮ ਵਾਲੀ ਨਿਗਰਾਨੀ ਪਛਾਣ ਲਈ ਲੋੜੀਂਦੀਆਂ ਉੱਨਤ ਤਕਨੀਕਾਂ ਬਾਰੇ ਦੱਸਦੀ ਹੈ।

ਉੱਨਤ **RayHunter** ਤੈਨਾਤੀ ਵਿੱਚ ਇਹ ਸ਼ਾਮਲ ਹਨ:
- ਖਾਸ ਖ਼ਤਰਾ ਮਾਹੌਲ ਲਈ **ਕਸਟਮ ਹਿਊਰਿਸਟਿਕਾਂ ਦਾ ਵਿਕਾਸ ਅਤੇ ਅਨੁਕੂਲਨ**
- **API-ਅਧਾਰਿਤ ਆਟੋਮੇਸ਼ਨ** ਅਤੇ ਸੁਰੱਖਿਆ ਕਾਰਜ ਕੇਂਦਰਾਂ ਨਾਲ ਏਕੀਕਰਨ
- ਵੱਡੇ ਖੇਤਰ ਨੂੰ ਕਵਰ ਕਰਨ ਲਈ **ਕਈ ਡਿਵਾਈਸਾਂ ਦਾ ਤਾਲਮੇਲ**
- ਸੈਲੂਲਰ ਵਿਸ਼ਲੇਸ਼ਣ ਸੰਦਾਂ ਨਾਲ **ਉੱਨਤ ਫੋਰੈਂਸਿਕ ਏਕੀਕਰਨ**
- **ਕਸਟਮ ਖ਼ਤਰਾ ਮਾਡਲਿੰਗ** ਅਤੇ ਮਾਹੌਲ ਅਨੁਸਾਰ ਕਨਫਿਗਰੇਸ਼ਨ
- **ਐਂਟਰਪ੍ਰਾਈਜ਼ ਪੱਧਰ ਦਾ ਸਮੱਸਿਆ ਨਿਵਾਰਨ ਅਤੇ ਰੱਖ-ਰਖਾਅ**

*ਇਹ ਗਾਈਡ ਮੰਨਦੀ ਹੈ ਕਿ ਤੁਹਾਨੂੰ **RayHunter** ਦੀ ਬੁਨਿਆਦੀ ਇੰਸਟਾਲੇਸ਼ਨ ਅਤੇ ਕਨਫਿਗਰੇਸ਼ਨ ਦੀ ਜਾਣਕਾਰੀ ਹੈ।* ਉੱਨਤ ਤਕਨੀਕਾਂ ਲਈ ਸੈਲੂਲਰ ਪ੍ਰੋਟੋਕੋਲ (2G/3G/4G/LTE), RF ਵਿਸ਼ਲੇਸ਼ਣ ਦੇ ਸਿਧਾਂਤ, ਨੈੱਟਵਰਕ ਸੁਰੱਖਿਆ ਅਤੇ ਸੁਰੱਖਿਆ ਕਾਰਜ ਕੇਂਦਰ ਨਾਲ ਏਕੀਕਰਨ ਦੀ ਜਾਣਕਾਰੀ ਚਾਹੀਦੀ ਹੈ।

{{< stscollective-ad "rayhunter" >}}

## ਉੱਨਤ ਕਨਫਿਗਰੇਸ਼ਨ ਰਣਨੀਤੀਆਂ

### ਕਸਟਮ ਹਿਊਰਿਸਟਿਕਾਂ ਦਾ ਅਨੁਕੂਲਨ

**RayHunter** ਦੀ ਪਛਾਣ ਕਾਰਗੁਜ਼ਾਰੀ ਖਾਸ ਕਾਰਜ ਮਾਹੌਲ ਲਈ ਹਿਊਰਿਸਟਿਕਾਂ ਦੀ ਸਹੀ ਕਨਫਿਗਰੇਸ਼ਨ ’ਤੇ ਬਹੁਤ ਨਿਰਭਰ ਕਰਦੀ ਹੈ। **ਤਜਰਬੇਕਾਰ ਵਰਤੋਂਕਾਰ ਹਿਊਰਿਸਟਿਕਾਂ ਨੂੰ ਧਿਆਨ ਨਾਲ ਸੈੱਟ ਕਰਕੇ ਪਛਾਣ ਸਹੀਤਾ ਵਧਾ ਸਕਦੇ ਹਨ ਅਤੇ ਗਲਤ ਸਕਾਰਾਤਮਕ ਨਤੀਜੇ ਘਟਾ ਸਕਦੇ ਹਨ**।

#### ਮਾਹੌਲ ਅਨੁਸਾਰ ਹਿਊਰਿਸਟਿਕ ਪ੍ਰੋਫਾਈਲ

**ਘਣੀ ਆਬਾਦੀ ਵਾਲੇ ਸ਼ਹਿਰੀ ਮਾਹੌਲ ਦੀ ਕਨਫਿਗਰੇਸ਼ਨ**:
```toml
[heuristics]
# ਵੱਧ ਰੁਝੇਵੇਂ ਵਾਲੇ ਸ਼ਹਿਰੀ ਇਲਾਕਿਆਂ ਵਿੱਚ ਸੰਵੇਦਨਸ਼ੀਲਤਾ ਘਟਾਓ
connection_release_detection = { enabled = true, sensitivity = "low", timeout = 30 }
imsi_request_detection = { enabled = true, threshold = 3, window = 60 }
null_cipher_detection = { enabled = true, immediate_alert = false }
sib_downgrade_detection = { enabled = true, sensitivity = "medium" }
incomplete_sib_detection = { enabled = false }  # ਸ਼ਹਿਰੀ ਇਲਾਕਿਆਂ ਵਿੱਚ ਗਲਤ ਚੇਤਾਵਨੀਆਂ ਦੀ ਦਰ ਉੱਚੀ ਹੈ

[filtering]
# ਸ਼ਹਿਰੀ ਮਾਹੌਲ ਲਈ ਉੱਨਤ ਫਿਲਟਰਿੰਗ
tower_density_threshold = 20
legitimate_carrier_whitelist = ["Verizon", "AT&T", "T-Mobile"]
frequency_hopping_tolerance = 5
```

**ਘੱਟ ਆਬਾਦੀ ਵਾਲੇ ਪੇਂਡੂ ਮਾਹੌਲ ਦੀ ਕਨਫਿਗਰੇਸ਼ਨ**:
```toml
[heuristics]
# ਘੱਟ ਆਬਾਦੀ ਵਾਲੇ ਇਲਾਕਿਆਂ ਵਿੱਚ ਸੰਵੇਦਨਸ਼ੀਲਤਾ ਵਧਾਓ
connection_release_detection = { enabled = true, sensitivity = "high", timeout = 10 }
imsi_request_detection = { enabled = true, threshold = 1, window = 30 }
null_cipher_detection = { enabled = true, immediate_alert = true }
sib_downgrade_detection = { enabled = true, sensitivity = "high" }
incomplete_sib_detection = { enabled = true, threshold = 2 }

[filtering]
# ਪੇਂਡੂ ਇਲਾਕਿਆਂ ਲਈ ਘੱਟੋ-ਘੱਟ ਫਿਲਟਰਿੰਗ
tower_density_threshold = 5
legitimate_carrier_whitelist = []
frequency_hopping_tolerance = 1
```

**ਉੱਚ ਸੁਰੱਖਿਆ ਵਾਲੇ ਸਮਾਗਮ ਦੀ ਕਨਫਿਗਰੇਸ਼ਨ**:
```toml
[heuristics]
# ਉੱਚ-ਖ਼ਤਰੇ ਵਾਲੀਆਂ ਸਥਿਤੀਆਂ ਲਈ ਵੱਧ ਤੋਂ ਵੱਧ ਸੰਵੇਦਨਸ਼ੀਲਤਾ
connection_release_detection = { enabled = true, sensitivity = "maximum", timeout = 5 }
imsi_request_detection = { enabled = true, threshold = 1, window = 15 }
null_cipher_detection = { enabled = true, immediate_alert = true, block_connection = true }
sib_downgrade_detection = { enabled = true, sensitivity = "maximum" }
incomplete_sib_detection = { enabled = true, threshold = 1 }
test_heuristic = { enabled = false }  # ਕਾਰਵਾਈ ਦੌਰਾਨ ਟੈਸਟ ਮੋਡ ਕਦੇ ਵੀ ਚਾਲੂ ਨਾ ਕਰੋ

[alerting]
# ਉੱਚ-ਸੁਰੱਖਿਆ ਵਾਲੀਆਂ ਸਥਿਤੀਆਂ ਲਈ ਤੁਰੰਤ ਚੇਤਾਵਨੀਆਂ
alert_threshold = "low"
immediate_notification = true
multi_channel_alerts = true
```

#### ਕਸਟਮ ਹਿਊਰਿਸਟਿਕਾਂ ਦਾ ਵਿਕਾਸ

ਤਜਰਬੇਕਾਰ ਵਰਤੋਂਕਾਰ **RayHunter** ਦੀ ਕਨਫਿਗਰੇਸ਼ਨ ਅਤੇ ਵਿਸ਼ਲੇਸ਼ਣ ਤਰਕ ਬਦਲ ਕੇ ਆਪਣੀਆਂ ਪਛਾਣ ਹਿਊਰਿਸਟਿਕਾਂ ਬਣਾ ਸਕਦੇ ਹਨ:

**ਸਮੇਂ ਦੇ ਵਿਸ਼ਲੇਸ਼ਣ ਲਈ ਕਸਟਮ ਹਿਊਰਿਸਟਿਕ**:
```toml
[custom_heuristics]
# ਸਮੇਂ-ਅਧਾਰਿਤ ਕਸਟਮ ਪਛਾਣ
timing_anomaly_detection = {
    enabled = true,
    baseline_establishment = 300,  # 5 ਮਿੰਟ ਦੀ ਬੇਸਲਾਈਨ
    deviation_threshold = 3.0,     # 3 ਮਿਆਰੀ ਵਿਸਥਾਪਨ
    minimum_samples = 50,
    alert_on_first_deviation = false
}

# ਉੱਨਤ ਪੈਟਰਨ ਪਛਾਣ
cell_tower_behavior_analysis = {
    enabled = true,
    learning_period = 3600,        # 1 ਘੰਟੇ ਦੀ ਸਿੱਖਣ ਮਿਆਦ
    pattern_memory = 168,          # ਪੈਟਰਨ 7 ਦਿਨਾਂ ਲਈ ਸੰਭਾਲੋ
    anomaly_sensitivity = 0.85,    # 85% ਭਰੋਸੇ ਦੀ ਹੱਦ
    behavioral_baseline = "adaptive"
}
```

**ਭੂਗੋਲਿਕ ਸਬੰਧ ਹਿਊਰਿਸਟਿਕ**:
```toml
[geo_correlation]
# ਟਿਕਾਣੇ-ਅਧਾਰਿਤ ਖ਼ਤਰੇ ਦਾ ਮੁਲਾਂਕਣ
enabled = true
gps_accuracy_threshold = 10        # 10 ਮੀਟਰ ਦੀ ਸ਼ੁੱਧਤਾ ਲਾਜ਼ਮੀ
movement_speed_threshold = 50      # ਵਾਜਬ ਵੱਧ ਤੋਂ ਵੱਧ ਗਤੀ 50 km/h
stationary_threshold = 100         # 100 ਮੀਟਰ ਦਾ ਸਥਿਰ ਘੇਰਾ
suspicious_location_database = "/data/rayhunter/suspicious_locations.db"

# ਕਈ ਡਿਵਾਈਸਾਂ ਵਿਚਕਾਰ ਤਾਲਮੇਲ ਵਾਲੀ ਪਛਾਣ
multi_device_correlation = {
    enabled = true,
    correlation_radius = 1000,     # 1 km ਦਾ ਸਬੰਧ ਘੇਰਾ
    time_synchronization = 5,      # ਸਮਾਂ-ਸਮਕਾਲੀਕਰਨ ਦੀ 5 ਸਕਿੰਟ ਸਹਿਣਸ਼ੀਲਤਾ
    consensus_threshold = 0.67     # 67% ਡਿਵਾਈਸਾਂ ਦੀ ਸਹਿਮਤੀ ਲਾਜ਼ਮੀ
}
```

### ਉੱਨਤ ਪਾਵਰ ਪ੍ਰਬੰਧਨ

ਲੰਮੇ ਸਮੇਂ ਦੇ ਕਾਰਜਾਂ ਲਈ ਬੈਟਰੀ ਦੇ ਬੁਨਿਆਦੀ ਅਨੁਕੂਲਨ ਤੋਂ ਅੱਗੇ ਦੀਆਂ ਪਾਵਰ ਪ੍ਰਬੰਧਨ ਰਣਨੀਤੀਆਂ ਚਾਹੀਦੀਆਂ ਹਨ:

**ਅਨੁਕੂਲ ਪਾਵਰ ਪ੍ਰਬੰਧਨ**:
```toml
[power_management]
# ਖ਼ਤਰੇ ਦੇ ਪੱਧਰ ਅਨੁਸਾਰ ਗਤੀਸ਼ੀਲ ਪਾਵਰ ਸਕੇਲਿੰਗ
adaptive_scaling = true
baseline_power_mode = "balanced"
high_alert_power_mode = "maximum_performance"
low_activity_power_mode = "extended_battery"

# ਤੈਅ ਕੀਤੇ ਕਾਰਜ ਮੋਡ
scheduled_modes = [
    { time = "00:00-06:00", mode = "low_power", days = ["monday", "tuesday", "wednesday", "thursday", "friday"] },
    { time = "06:00-22:00", mode = "high_sensitivity", days = ["saturday", "sunday"] },
    { time = "22:00-24:00", mode = "balanced", days = "all" }
]

# ਬੈਟਰੀ ਪੱਧਰ ਅਨੁਸਾਰ ਮੋਡ ਬਦਲਾਅ
battery_thresholds = {
    "90%" = "maximum_performance",
    "50%" = "balanced",
    "25%" = "extended_battery",
    "10%" = "emergency_detection_only"
}
```

**ਕਈ ਡਿਵਾਈਸਾਂ ਲਈ ਪਾਵਰ ਤਾਲਮੇਲ**:
```toml
[coordinated_power]
# ਕਈ ਡਿਵਾਈਸਾਂ ਵਿੱਚ ਪਾਵਰ ਪ੍ਰਬੰਧਨ ਦਾ ਤਾਲਮੇਲ ਕਰੋ
device_roles = ["primary", "secondary", "backup"]
role_switching_enabled = true
battery_level_sharing = true
automatic_failover = true

# ਉੱਨਤ ਸਲੀਪ/ਵੇਕ ਤਾਲਮੇਲ
coordinated_sleep_cycles = {
    enabled = true,
    sleep_rotation_interval = 300,  # 5 ਮਿੰਟ
    minimum_active_devices = 2,
    overlap_period = 30             # 30 ਸਕਿੰਟ ਦਾ ਓਵਰਲੈਪ
}
```

## ਉੱਨਤ ਵਿਸ਼ਲੇਸ਼ਣ ਤਕਨੀਕਾਂ

### ਕਸਟਮ PCAP ਅਤੇ QMDL ਵਿਸ਼ਲੇਸ਼ਣ

**RayHunter** ਵਿਸਤ੍ਰਿਤ **ਸੈਲੂਲਰ ਪ੍ਰੋਟੋਕੋਲ ਕੈਪਚਰ** ਬਣਾਉਂਦਾ ਹੈ। ਇਨ੍ਹਾਂ ਤੋਂ ਵੱਧ ਤੋਂ ਵੱਧ ਜਾਣਕਾਰੀ ਲੈਣ ਲਈ ਉੱਨਤ ਵਿਸ਼ਲੇਸ਼ਣ ਤਕਨੀਕਾਂ ਚਾਹੀਦੀਆਂ ਹਨ।

#### rayhunter-check ਦੀ ਉੱਨਤ ਵਰਤੋਂ

**ਬੈਚ ਵਿਸ਼ਲੇਸ਼ਣ ਵਰਕਫਲੋ**:
```bash
#!/bin/bash
# ਕਈ ਰਿਕਾਰਡਿੰਗਾਂ ਲਈ ਉੱਨਤ ਬੈਚ ਵਿਸ਼ਲੇਸ਼ਣ ਸਕ੍ਰਿਪਟ

ANALYSIS_DIR="/data/rayhunter/analysis"
RECORDINGS_DIR="/data/rayhunter/recordings"
OUTPUT_DIR="/data/rayhunter/reports"

# ਕਸਟਮ ਪੈਰਾਮੀਟਰਾਂ ਨਾਲ ਸਾਰੀਆਂ ਰਿਕਾਰਡਿੰਗਾਂ ਦੀ ਪ੍ਰਕਿਰਿਆ ਕਰੋ
for recording in "$RECORDINGS_DIR"/*.qmdl; do
    filename=$(basename "$recording" .qmdl)
    echo "$filename ਦੀ ਪ੍ਰਕਿਰਿਆ ਜਾਰੀ ਹੈ..."

    # ਮਿਆਰੀ ਵਿਸ਼ਲੇਸ਼ਣ
    rayhunter-check -p "$recording" --json > "$OUTPUT_DIR/${filename}_standard.json"

    # ਵਾਧੂ ਆਉਟਪੁੱਟ ਨਾਲ ਡੀਬੱਗ ਵਿਸ਼ਲੇਸ਼ਣ
    rayhunter-check -d -p "$recording" --verbose > "$OUTPUT_DIR/${filename}_debug.log"

    # ਕਸਟਮ ਹੀਉਰਿਸਟਿਕ ਵਿਸ਼ਲੇਸ਼ਣ
    rayhunter-check -p "$recording" --config "/etc/rayhunter/custom_analysis.toml" \
        --output-format json > "$OUTPUT_DIR/${filename}_custom.json"

    # ਖ਼ਤਰਾ-ਸਬੰਧ ਵਿਸ਼ਲੇਸ਼ਣ
    rayhunter-check -p "$recording" --correlate-threats \
        --baseline "$ANALYSIS_DIR/baseline.qmdl" > "$OUTPUT_DIR/${filename}_correlation.json"
done

# ਇਕੱਠੀ ਰਿਪੋਰਟ ਤਿਆਰ ਕਰੋ
python3 /opt/rayhunter/analysis/consolidate_reports.py "$OUTPUT_DIR" > "$OUTPUT_DIR/consolidated_analysis.html"
```

**ਉੱਨਤ ਫਿਲਟਰਿੰਗ ਅਤੇ ਵਿਸ਼ਲੇਸ਼ਣ**:
```bash
# ਖ਼ਾਸ ਧਿਆਨ ਵਾਲੇ ਖੇਤਰਾਂ ਸਮੇਤ ਕਸਟਮ ਵਿਸ਼ਲੇਸ਼ਣ
rayhunter-check -p recording.qmdl \
    --focus-heuristics "imsi_request,null_cipher" \
    --time-range "14:30-15:45" \
    --frequency-bands "1900,850" \
    --operator-filter "unknown" \
    --confidence-threshold 0.8

# ਰਿਕਾਰਡਿੰਗਾਂ ਦੀ ਆਪਸੀ ਤੁਲਨਾ ਕਰੋ
rayhunter-check --compare recording1.qmdl recording2.qmdl \
    --baseline-period 300 \
    --anomaly-detection \
    --statistical-analysis

# ਬਾਹਰੀ ਟੂਲਾਂ ਨਾਲ ਏਕੀਕਰਨ
rayhunter-check -p recording.qmdl --export-wireshark | \
    tshark -r - -Y "gsm || lte" -T json > cellular_traffic.json
```

### ਕਸਟਮ ਵਿਸ਼ਲੇਸ਼ਣ ਸਕ੍ਰਿਪਟਾਂ

**ਉੱਨਤ ਵਿਸ਼ਲੇਸ਼ਣ ਲਈ Python ਏਕੀਕਰਨ**:
```python
#!/usr/bin/env python3
"""
RayHunter ਲਈ ਉੱਨਤ ਵਿਸ਼ਲੇਸ਼ਣ ਏਕੀਕਰਨ
RayHunter ਡਾਟਾ ਲਈ ਉੱਨਤ ਵਿਸ਼ਲੇਸ਼ਣ ਸਮਰੱਥਾਵਾਂ ਦਿੰਦਾ ਹੈ
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
        """ਕਸਟਮ ਸਕੀਮਾ ਨਾਲ ਵਿਸ਼ਲੇਸ਼ਣ ਡਾਟਾਬੇਸ ਸ਼ੁਰੂ ਕਰੋ"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        # ਉੱਨਤ ਵਿਸ਼ਲੇਸ਼ਣ ਟੇਬਲ ਬਣਾਓ
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
        """ਉੱਨਤ ਵਿਸ਼ਲੇਸ਼ਣ ਲਈ RayHunter JSON ਆਉਟਪੁੱਟ ਦੀ ਪ੍ਰਕਿਰਿਆ ਕਰੋ"""
        with open(json_file_path, 'r') as f:
            data = json.load(f)

        # ਖ਼ਤਰੇ ਵਾਲੀਆਂ ਘਟਨਾਵਾਂ ਕੱਢੋ ਅਤੇ ਸਧਾਰਣ ਰੂਪ ਦਿਓ
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
        """ਕਈ ਕਾਰਕਾਂ ਦੇ ਆਧਾਰ ’ਤੇ ਉੱਨਤ ਭਰੋਸਾ ਸਕੋਰ ਕੱਢੋ"""
        base_confidence = alert.get('confidence', 0.5)

        # ਕਈ ਡਾਟਾ ਬਿੰਦੂਆਂ ਨੂੰ ਧਿਆਨ ਵਿੱਚ ਰੱਖੋ
        factors = {
            'signal_strength': alert.get('signal_strength', 0) / 100,
            'timing_consistency': alert.get('timing_score', 0.5),
            'protocol_compliance': alert.get('protocol_score', 0.5),
            'environmental_context': alert.get('environment_score', 0.5)
        }

        # ਭਾਰਿਤ ਭਰੋਸਾ ਗਣਨਾ
        weights = {'signal_strength': 0.3, 'timing_consistency': 0.25,
                  'protocol_compliance': 0.25, 'environmental_context': 0.2}

        weighted_confidence = sum(factors[k] * weights[k] for k in factors)
        return min(base_confidence + weighted_confidence, 1.0)

    def correlation_analysis(self, events, time_window=300):
        """ਸਮੇਂ ਅਤੇ ਸਥਾਨ ਅਨੁਸਾਰ ਸਬੰਧ ਵਿਸ਼ਲੇਸ਼ਣ ਕਰੋ"""
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
        """ਦੋ ਘਟਨਾਵਾਂ ਵਿਚਕਾਰ ਸਬੰਧ ਦੀ ਤਾਕਤ ਕੱਢੋ"""
        # ਉੱਨਤ ਸਬੰਧ ਐਲਗੋਰਿਦਮ ਲਾਗੂ ਕਰੋ
        similarity_factors = []

        # ਖ਼ਤਰੇ ਦੀ ਕਿਸਮ ਦੀ ਸਮਾਨਤਾ
        if event1['threat_type'] == event2['threat_type']:
            similarity_factors.append(0.4)
        elif self.are_related_threats(event1['threat_type'], event2['threat_type']):
            similarity_factors.append(0.2)

        # ਭਰੋਸਾ ਸਕੋਰ ਦੀ ਸਮਾਨਤਾ
        confidence_diff = abs(event1['confidence_score'] - event2['confidence_score'])
        similarity_factors.append(1.0 - confidence_diff)

        return np.mean(similarity_factors)

    def generate_threat_report(self, analysis_period_hours=24):
        """ਖ਼ਤਰੇ ਦੇ ਮੁਲਾਂਕਣ ਦੀ ਵਿਸਤ੍ਰਿਤ ਰਿਪੋਰਟ ਬਣਾਓ"""
        end_time = datetime.now()
        start_time = end_time - timedelta(hours=analysis_period_hours)

        # ਹਾਲੀਆ ਘਟਨਾਵਾਂ ਲਈ ਡਾਟਾਬੇਸ ਪੁੱਛੋ
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

        # ਅੰਕੜਾ ਵਿਸ਼ਲੇਸ਼ਣ ਤਿਆਰ ਕਰੋ
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

### API-ਅਧਾਰਿਤ ਆਟੋਮੇਸ਼ਨ

**RayHunter** ਦਾ **REST API** ਉੱਨਤ ਆਟੋਮੇਸ਼ਨ ਅਤੇ ਐਂਟਰਪ੍ਰਾਈਜ਼ ਸੁਰੱਖਿਆ ਪ੍ਰਣਾਲੀਆਂ ਨਾਲ ਏਕੀਕਰਨ ਸੰਭਵ ਕਰਦਾ ਹੈ।

#### ਆਟੋਮੈਟਿਕ ਨਿਗਰਾਨੀ ਸਕ੍ਰਿਪਟਾਂ

**ਲਗਾਤਾਰ ਨਿਗਰਾਨੀ ਦਾ ਆਟੋਮੇਸ਼ਨ**:
```python
#!/usr/bin/env python3
"""
RayHunter ਐਂਟਰਪ੍ਰਾਈਜ਼ ਨਿਗਰਾਨੀ ਸਿਸਟਮ
ਧਮਕੀ ਪਛਾਣ ਅਤੇ ਜਵਾਬ ਲਈ ਸਵੈਚਾਲਿਤ ਏਕੀਕਰਨ
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
        """ਐਂਟਰਪ੍ਰਾਈਜ਼-ਪੱਧਰ ਲਾਗਿੰਗ ਸੰਰਚਿਤ ਕਰੋ"""
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
        """ਕਈ RayHunter ਡਿਵਾਈਸਾਂ ਦੀ ਲਗਾਤਾਰ ਨਿਗਰਾਨੀ"""
        while True:
            for device_name, config in self.devices.items():
                try:
                    device_status = self.check_device_status(config)
                    alerts = self.get_recent_alerts(config)

                    if alerts:
                        self.process_alerts(device_name, alerts)

                    self.log_device_status(device_name, device_status)

                except Exception as e:
                    self.logger.error(f"{device_name} ਡਿਵਾਈਸ ਦੀ ਨਿਗਰਾਨੀ ਕਰਦੇ ਸਮੇਂ ਗਲਤੀ: {e}")

            time.sleep(poll_interval)

    def check_device_status(self, config):
        """API ਰਾਹੀਂ ਡਿਵਾਈਸ ਦੀ ਪੂਰੀ ਸਥਿਤੀ ਜਾਂਚੋ"""
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
            self.logger.warning(f"ਡਿਵਾਈਸ {config['ip']} ਪਹੁੰਚਯੋਗ ਨਹੀਂ: {e}")
            return {'online': False, 'error': str(e)}

    def get_recent_alerts(self, config, minutes=5):
        """ਡਿਵਾਈਸ ਤੋਂ ਹਾਲੀਆ ਚੇਤਾਵਨੀਆਂ ਪ੍ਰਾਪਤ ਕਰੋ"""
        api_url = f"http://{config['ip']}:8080/api/alerts"
        params = {'since': f"{minutes}min"}

        try:
            response = requests.get(api_url, params=params, timeout=10)
            response.raise_for_status()
            return response.json().get('alerts', [])
        except requests.RequestException:
            return []

    def process_alerts(self, device_name, alerts):
        """ਚੇਤਾਵਨੀਆਂ ਦੀ ਪ੍ਰਕਿਰਿਆ ਕਰੋ ਅਤੇ ਜਵਾਬ ਦਿਓ"""
        for alert in alerts:
            alert_level = self.assess_alert_severity(alert)

            if alert_level == 'CRITICAL':
                self.handle_critical_alert(device_name, alert)
            elif alert_level == 'HIGH':
                self.handle_high_alert(device_name, alert)
            elif alert_level == 'MEDIUM':
                self.handle_medium_alert(device_name, alert)

            # ਸਾਰੀਆਂ ਚੇਤਾਵਨੀਆਂ ਲੌਗ ਕਰੋ
            self.logger.info(f"{device_name} ਵੱਲੋਂ ਚੇਤਾਵਨੀ: {alert['heuristic']} - {alert_level}")

    def assess_alert_severity(self, alert):
        """ਕਈ ਕਾਰਕਾਂ ਦੇ ਆਧਾਰ ’ਤੇ ਚੇਤਾਵਨੀ ਦੀ ਗੰਭੀਰਤਾ ਅੰਕੋ"""
        threat_type = alert.get('heuristic', '')
        confidence = alert.get('confidence_score', 0)

        # ਗੰਭੀਰ ਖ਼ਤਰੇ
        if threat_type in ['null_cipher_detection', 'imsi_request_detection'] and confidence > 0.9:
            return 'CRITICAL'

        # ਉੱਚ ਗੰਭੀਰਤਾ ਵਾਲੇ ਖ਼ਤਰੇ
        elif threat_type in ['connection_release_detection', 'sib_downgrade_detection'] and confidence > 0.8:
            return 'HIGH'

        # ਦਰਮਿਆਨੀ ਗੰਭੀਰਤਾ
        elif confidence > 0.6:
            return 'MEDIUM'

        return 'LOW'

    def handle_critical_alert(self, device_name, alert):
        """ਗੰਭੀਰ ਸੁਰੱਖਿਆ ਚੇਤਾਵਨੀਆਂ ਦਾ ਤੁਰੰਤ ਜਵਾਬ ਦਿਓ"""
        # ਤੁਰੰਤ ਸੂਚਨਾਵਾਂ ਭੇਜੋ
        self.send_sms_alert(f"ਗੰਭੀਰ: {device_name} ਵੱਲੋਂ IMSI ਕੈਚਰ ਦਾ ਪਤਾ ਲੱਗਿਆ")
        self.send_email_alert("ਗੰਭੀਰ ਖ਼ਤਰਾ", device_name, alert)

        # ਸਵੈਚਾਲਿਤ ਜਵਾਬ ਚਲਾਓ
        subprocess.run(['/opt/security/scripts/critical_response.sh', device_name])

        # SIEM ਵਿੱਚ ਲੌਗ ਕਰੋ
        self.log_to_siem('CRITICAL', device_name, alert)
```

#### ਐਂਟਰਪ੍ਰਾਈਜ਼ ਏਕੀਕਰਨ

**SIEM ਏਕੀਕਰਨ ਸਕ੍ਰਿਪਟ**:
```python
def integrate_with_siem(self, alert_data):
    """ਐਂਟਰਪ੍ਰਾਈਜ਼ SIEM ਸਿਸਟਮਾਂ ਨਾਲ ਏਕੀਕਰਨ"""

    # Splunk ਏਕੀਕਰਨ
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

    # Splunk HEC ਨੂੰ ਭੇਜੋ
    requests.post(
        'https://splunk.company.com:8088/services/collector',
        headers={'Authorization': 'Splunk <HEC-TOKEN>'},
        json=splunk_data
    )

    # syslog ਰਾਹੀਂ QRadar ਏਕੀਕਰਨ
    syslog_message = f"RayHunter ALERT: {alert_data['heuristic']} ਦੀ ਪਛਾਣ ਹੋਈ " \
                    f"ਭਰੋਸੇ ਦੇ ਪੱਧਰ {alert_data['confidence_score']:.2f} ਨਾਲ " \
                    f"ਡਿਵਾਈਸ {alert_data['device_name']} ਉੱਤੇ"
    subprocess.run([
        'logger', '-p', 'local0.alert', '-t', 'RayHunter', syslog_message
    ])
```

## ਕਈ ਡਿਵਾਈਸਾਂ ਦਾ ਤਾਲਮੇਲ

{{< figure src="rayhunter-multi-device-coordination-network.webp" alt="ਕਵਰੇਜ ਖੇਤਰ ਵਿੱਚ ਤੈਨਾਤ ਕਈ RayHunter ਡਿਵਾਈਸਾਂ ਦਾ ਚਿੱਤਰ। ਹਰ ਡਿਵਾਈਸ ਪਛਾਣ ਦੇ ਨਤੀਜੇ ਆਪਸੀ ਜਾਂਚ ਲਈ ਤਾਲਮੇਲ ਕਰਨ ਵਾਲੇ ਮਾਸਟਰ ਡਿਵਾਈਸ ਨੂੰ ਭੇਜਦੀ ਹੈ।" >}}

ਉੱਨਤ **RayHunter** ਤੈਨਾਤੀਆਂ ਵਿੱਚ ਅਕਸਰ ਕਈ ਡਿਵਾਈਸ ਇਕੱਠੇ ਕੰਮ ਕਰਦੇ ਹਨ, ਤਾਂ ਜੋ ਵੱਡਾ ਖੇਤਰ ਕਵਰ ਹੋਵੇ ਅਤੇ **ਖ਼ਤਰਿਆਂ ਦੀ ਆਪਸੀ ਪੁਸ਼ਟੀ** ਹੋ ਸਕੇ।

### ਤਾਲਮੇਲ ਵਾਲੇ ਪਛਾਣ ਨੈੱਟਵਰਕ

**ਮਾਸਟਰ-ਸਲੇਵ ਕਨਫਿਗਰੇਸ਼ਨ**:
```toml
[coordination]
# ਮਾਸਟਰ ਡਿਵਾਈਸ ਦੀ ਸੰਰਚਨਾ
role = "master"
slave_devices = [
    { ip = "192.168.1.101", name = "rayhunter-north", priority = 1 },
    { ip = "192.168.1.102", name = "rayhunter-south", priority = 2 },
    { ip = "192.168.1.103", name = "rayhunter-west", priority = 3 }
]

# ਤਾਲਮੇਲ ਸੈਟਿੰਗਾਂ
sync_interval = 30              # ਹਰ 30 ਸਕਿੰਟ ਬਾਅਦ ਸਿੰਕ ਕਰੋ
correlation_window = 60         # 1 ਮਿੰਟ ਦੀ ਸਬੰਧ ਵਿੰਡੋ
consensus_threshold = 0.67      # ਚੇਤਾਵਨੀ ਲਈ 67% ਸਹਿਮਤੀ ਲਾਜ਼ਮੀ
automatic_failover = true
heartbeat_timeout = 120         # 2 ਮਿੰਟ ਦਾ ਹਾਰਟਬੀਟ ਟਾਈਮਆਉਟ

# ਚੇਤਾਵਨੀਆਂ ਵੰਡੋ
distribute_alerts = true
alert_consolidation = true
duplicate_suppression = true
cross_validation_required = true
```

**ਸਲੇਵ ਡਿਵਾਈਸ ਦੀ ਕਨਫਿਗਰੇਸ਼ਨ**:
```toml
[coordination]
# ਸਲੇਵ ਡਿਵਾਈਸ ਦੀ ਸੰਰਚਨਾ
role = "slave"
master_device = { ip = "192.168.1.100", name = "rayhunter-master" }

# ਰਿਪੋਰਟਿੰਗ ਸੈਟਿੰਗਾਂ
report_interval = 15            # ਹਰ 15 ਸਕਿੰਟ ਬਾਅਦ ਰਿਪੋਰਟ ਕਰੋ
include_negative_results = true # ਖ਼ਤਰੇ ਨਾ ਮਿਲਣ ਦੀ ਜਾਣਕਾਰੀ ਵੀ ਦਿਓ
local_decision_making = false   # ਮਾਸਟਰ ਦੇ ਨਿਰਦੇਸ਼ ਮੰਨੋ
emergency_autonomous_mode = true # ਮਾਸਟਰ ਉਪਲਬਧ ਨਾ ਹੋਵੇ ਤਾਂ ਸੁਤੰਤਰ ਤੌਰ 'ਤੇ ਕੰਮ ਕਰੋ
```

### ਤਾਲਮੇਲ ਵਾਲੀਆਂ ਵਿਸ਼ਲੇਸ਼ਣ ਸਕ੍ਰਿਪਟਾਂ

**ਡਿਵਾਈਸਾਂ ਵਿਚਕਾਰ ਖ਼ਤਰਾ ਸਬੰਧ**:
```python
#!/usr/bin/env python3
"""
ਬਹੁ-ਡਿਵਾਈਸ RayHunter ਤਾਲਮੇਲ ਸਿਸਟਮ
ਕਈ ਡਿਵਾਈਸਾਂ ਵਿੱਚ ਤਾਲਮੇਲ ਨਾਲ ਧਮਕੀਆਂ ਦੀ ਪਛਾਣ ਕਰਦਾ ਹੈ
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
        """ਮੁੱਖ ਤਾਲਮੇਲ ਚੱਕਰ"""
        while True:
            # ਸਾਰੇ ਡਿਵਾਈਸਾਂ ਤੋਂ ਡਾਟਾ ਇਕੱਠਾ ਕਰੋ
            device_data = await self.collect_device_data()

            # ਸਬੰਧ ਵਿਸ਼ਲੇਸ਼ਣ ਕਰੋ
            correlated_threats = self.correlate_threats(device_data)

            # ਸਹਿਮਤੀ ਰਾਹੀਂ ਖ਼ਤਰਿਆਂ ਦੀ ਪੁਸ਼ਟੀ ਕਰੋ
            validated_threats = self.consensus_validation(correlated_threats)

            # ਪੁਸ਼ਟੀ ਕੀਤੇ ਖ਼ਤਰੇ ਡਿਵਾਈਸਾਂ ਨੂੰ ਵਾਪਸ ਭੇਜੋ
            await self.distribute_threat_intelligence(validated_threats)

            await asyncio.sleep(30)  # 30 ਸਕਿੰਟਾਂ ਦਾ ਤਾਲਮੇਲ ਚੱਕਰ

    async def collect_device_data(self):
        """ਸਾਰੇ ਡਿਵਾਈਸਾਂ ਤੋਂ ਡਾਟਾ ਇਕੱਠਾ ਕਰੋ ਸਮਾਂਤਰ ਢੰਗ ਨਾਲ"""
        tasks = []
        for device in self.devices:
            task = self.get_device_data(device)
            tasks.append(task)

        results = await asyncio.gather(*tasks, return_exceptions=True)
        return {device['name']: result for device, result in zip(self.devices, results)}

    async def get_device_data(self, device):
        """ਇੱਕ ਡਿਵਾਈਸ ਤੋਂ ਡਾਟਾ ਪ੍ਰਾਪਤ ਕਰੋ"""
        async with aiohttp.ClientSession() as session:
            try:
                # ਹਾਲੀਆ ਚੇਤਾਵਨੀਆਂ ਪ੍ਰਾਪਤ ਕਰੋ
                alerts_url = f"http://{device['ip']}:8080/api/alerts?since=1min"
                async with session.get(alerts_url) as response:
                    alerts_data = await response.json()

                # ਡਿਵਾਈਸ ਦੀ ਸਥਿਤੀ ਪ੍ਰਾਪਤ ਕਰੋ
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
        """ਕਈ ਡਿਵਾਈਸਾਂ ਵਿਚਕਾਰ ਧਮਕੀਆਂ ਦਾ ਸਬੰਧ ਜੋੜੋ"""
        correlated_threats = []

        # ਸਾਰੇ ਡਿਵਾਈਸਾਂ ਤੋਂ ਸਾਰੀਆਂ ਚੇਤਾਵਨੀਆਂ ਕੱਢੋ
        all_alerts = []
        for device_name, data in device_data.items():
            if 'alerts' in data:
                for alert in data['alerts']:
                    alert['source_device'] = device_name
                    all_alerts.append(alert)

        # ਚੇਤਾਵਨੀਆਂ ਨੂੰ ਸਮੇਂ ਅਤੇ ਖ਼ਤਰੇ ਦੀ ਕਿਸਮ ਅਨੁਸਾਰ ਸਮੂਹਬੱਧ ਕਰੋ
        threat_groups = self.group_alerts_by_similarity(all_alerts)

        for group in threat_groups:
            if len(group) >= 2:  # ਕਈ ਡਿਵਾਈਸਾਂ ਵਿੱਚ ਮਿਲਦੀਆਂ-ਜੁਲਦੀਆਂ ਧਮਕੀਆਂ ਮਿਲੀਆਂ
                correlated_threat = self.create_correlated_threat(group)
                correlated_threats.append(correlated_threat)

        return correlated_threats

    def group_alerts_by_similarity(self, alerts, time_window=60):
        """ਸਮੇਂ ਅਤੇ ਧਮਕੀ ਸਮਾਨਤਾ ਅਨੁਸਾਰ ਚੇਤਾਵਨੀਆਂ ਦੇ ਸਮੂਹ ਬਣਾਓ"""
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
        """ਡਿਵਾਈਸਾਂ ਦੀ ਸਹਿਮਤੀ ਨਾਲ ਧਮਕੀਆਂ ਦੀ ਪੁਸ਼ਟੀ ਕਰੋ"""
        validated_threats = []

        for threat in correlated_threats:
            device_count = len(set(alert['source_device'] for alert in threat['constituent_alerts']))
            confidence_scores = [alert['confidence_score'] for alert in threat['constituent_alerts']]

            # ਡਿਵਾਈਸਾਂ ਦੀ ਘੱਟੋ-ਘੱਟ ਗਿਣਤੀ ਅਤੇ ਭਰੋਸੇ ਦੀ ਹੱਦ ਲਾਜ਼ਮੀ ਕਰੋ
            if (device_count >= 2 and
                np.mean(confidence_scores) >= 0.7 and
                min(confidence_scores) >= 0.5):

                threat['validated'] = True
                threat['consensus_strength'] = device_count / len(self.devices)
                threat['confidence_score'] = np.mean(confidence_scores)
                validated_threats.append(threat)

        return validated_threats
```

## ਉੱਨਤ ਸਮੱਸਿਆ ਨਿਵਾਰਨ

### ਆਮ ਉੱਨਤ ਸਮੱਸਿਆਵਾਂ

#### ਕਾਰਗੁਜ਼ਾਰੀ ਅਨੁਕੂਲਨ ਦੀਆਂ ਸਮੱਸਿਆਵਾਂ

**CPU ਦੀ ਵੱਧ ਵਰਤੋਂ ਦਾ ਨਿਪਟਾਰਾ**:
```bash
#!/bin/bash
# RayHunter ਦੀ ਕਾਰਗੁਜ਼ਾਰੀ ਸਮੱਸਿਆਵਾਂ ਲਈ ਜਾਂਚ ਸਕ੍ਰਿਪਟ

echo "=== RayHunter ਕਾਰਗੁਜ਼ਾਰੀ ਵਿਸ਼ਲੇਸ਼ਣ ==="

# CPU ਦੀ ਵਰਤੋਂ ਜਾਂਚੋ
echo "ਮੌਜੂਦਾ CPU ਵਰਤੋਂ:"
top -bn1 | grep rayhunter

# ਮੈਮੋਰੀ ਦੀ ਵਰਤੋਂ ਜਾਂਚੋ
echo -e "\nਮੈਮੋਰੀ ਵਰਤੋਂ:"
ps aux | grep rayhunter | awk '{print $4, $6, $11}'

# ਡਿਸਕ I/O ਜਾਂਚੋ
echo -e "\nਡਿਸਕ I/O:"
iotop -a -o -d1 -n3 | grep rayhunter

# ਸੰਰਚਨਾ ਦੀਆਂ ਸਮੱਸਿਆਵਾਂ ਦਾ ਵਿਸ਼ਲੇਸ਼ਣ ਕਰੋ
echo -e "\nਸੰਰਚਨਾ ਵਿਸ਼ਲੇਸ਼ਣ:"
if [ -f /data/rayhunter/config.toml ]; then
    # ਵੱਧ ਸਰੋਤ ਵਰਤਣ ਵਾਲੀਆਂ ਸੰਰਚਨਾਵਾਂ ਦੀ ਜਾਂਚ ਕਰੋ
    grep -E "test_heuristic.*true|sensitivity.*maximum|debug.*true" /data/rayhunter/config.toml

    # ਰਿਕਾਰਡਿੰਗ ਸੈਟਿੰਗਾਂ ਜਾਂਚੋ
    grep -E "recording|storage" /data/rayhunter/config.toml
else
    echo "ਸੰਰਚਨਾ ਫ਼ਾਈਲ ਨਹੀਂ ਮਿਲੀ!"
fi

# ਬਹੁਤ ਜ਼ਿਆਦਾ ਲੌਗਿੰਗ ਦੀ ਜਾਂਚ ਕਰੋ
echo -e "\nਲਾਗ ਫ਼ਾਈਲਾਂ ਦੇ ਆਕਾਰ:"
du -sh /data/rayhunter/logs/*

# ਨੈੱਟਵਰਕ ਦੀ ਕਾਰਗੁਜ਼ਾਰੀ ਜਾਂਚੋ
echo -e "\nਨੈੱਟਵਰਕ ਕਾਰਗੁਜ਼ਾਰੀ:"
netstat -i | grep -E "wlan|eth"

# ਅਨੁਕੂਲਤਾ ਲਈ ਸੁਝਾਅ ਤਿਆਰ ਕਰੋ
echo -e "\n=== ਅਨੁਕੂਲਤਾ ਲਈ ਸਿਫ਼ਾਰਸ਼ਾਂ ==="

# ਟੈਸਟ ਹੀਉਰਿਸਟਿਕ ਚਾਲੂ ਹੈ ਜਾਂ ਨਹੀਂ ਜਾਂਚੋ
if grep -q "test_heuristic.*=.*true" /data/rayhunter/config.toml; then
    echo "⚠️ ਟੈਸਟ ਹੀਉਰਿਸਟਿਕ ਚਾਲੂ ਹੈ; ਉਤਪਾਦਨ ਵਿੱਚ ਇਸਨੂੰ ਬੰਦ ਕਰੋ"
fi

# ਸੰਵੇਦਨਸ਼ੀਲਤਾ ਸੈਟਿੰਗਾਂ ਜਾਂਚੋ
if grep -q "sensitivity.*=.*\"maximum\"" /data/rayhunter/config.toml; then
    echo "⚠️ ਸੰਘਣੇ ਮਾਹੌਲ ਵਿੱਚ ਵੱਧ ਤੋਂ ਵੱਧ ਸੰਵੇਦਨਸ਼ੀਲਤਾ ਨਾਲ CPU ਦੀ ਵਰਤੋਂ ਵਧ ਸਕਦੀ ਹੈ"
fi

# ਸਟੋਰੇਜ ਸੈਟਿੰਗਾਂ ਜਾਂਚੋ
STORAGE_USED=$(df -h /data/rayhunter | awk 'NR==2 {print $5}' | sed 's/%//')
if [ "$STORAGE_USED" -gt 80 ]; then
    echo "⚠️ ਸਟੋਰੇਜ ਦੀ ਵਰਤੋਂ ${STORAGE_USED}%; ਪੁਰਾਣੀਆਂ ਰਿਕਾਰਡਿੰਗਾਂ ਮਿਟਾਓ"
fi
```

**ਮੈਮਰੀ ਲੀਕ ਦੀ ਪਛਾਣ ਅਤੇ ਹੱਲ**:
```bash
#!/bin/bash
# ਮੈਮੋਰੀ ਲੀਕ ਪਛਾਣੋ ਅਤੇ ਆਪਣੇ ਆਪ ਠੀਕ ਕਰੋ

MEMORY_THRESHOLD=80  # 80% ਮੈਮੋਰੀ ਵਰਤੋਂ ਦੀ ਹੱਦ
LOG_FILE="/var/log/rayhunter/memory_monitor.log"

monitor_memory() {
    while true; do
        # RayHunter ਦੀ ਮੈਮੋਰੀ ਵਰਤੋਂ ਪ੍ਰਾਪਤ ਕਰੋ
        MEMORY_USAGE=$(ps aux | grep rayhunter-daemon | grep -v grep | awk '{print $4}')

        if [ ! -z "$MEMORY_USAGE" ]; then
            MEMORY_PERCENT=$(echo "$MEMORY_USAGE" | cut -d. -f1)

            echo "$(date): RayHunter ਮੈਮੋਰੀ ਵਰਤੋਂ: ${MEMORY_USAGE}%" >> "$LOG_FILE"

            if [ "$MEMORY_PERCENT" -gt "$MEMORY_THRESHOLD" ]; then
                echo "$(date): ਵੱਧ ਮੈਮੋਰੀ ਵਰਤੋਂ ਮਿਲੀ: ${MEMORY_USAGE}%" >> "$LOG_FILE"

                # ਸਧਾਰਣ ਰੀਸਟਾਰਟ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰੋ
                echo "$(date): ਸੁਚੱਜੇ ਰੀਸਟਾਰਟ ਦੀ ਕੋਸ਼ਿਸ਼..." >> "$LOG_FILE"
                systemctl restart rayhunter_daemon

                sleep 30

                # ਰੀਸਟਾਰਟ ਸਫਲ ਹੋਇਆ ਜਾਂਚੋ
                if pgrep rayhunter-daemon > /dev/null; then
                    echo "$(date): ਸੁਚੱਜਾ ਰੀਸਟਾਰਟ ਸਫਲ ਰਿਹਾ" >> "$LOG_FILE"
                else
                    echo "$(date): ਸੁਚੱਜਾ ਰੀਸਟਾਰਟ ਅਸਫਲ; ਜ਼ਬਰਦਸਤੀ ਰੀਸਟਾਰਟ ਦੀ ਕੋਸ਼ਿਸ਼" >> "$LOG_FILE"
                    killall -9 rayhunter-daemon
                    systemctl start rayhunter_daemon
                fi
            fi
        fi

        sleep 60  # ਹਰ ਮਿੰਟ ਜਾਂਚੋ
    done
}

# ਬੈਕਗ੍ਰਾਊਂਡ ਵਿੱਚ ਮੈਮੋਰੀ ਦੀ ਨਿਗਰਾਨੀ ਕਰੋ
monitor_memory &
```

#### ਨੈੱਟਵਰਕ ਕਨੈਕਟਿਵਿਟੀ ਦੀਆਂ ਸਮੱਸਿਆਵਾਂ

**ਉੱਨਤ ਕਨੈਕਟਿਵਿਟੀ ਜਾਂਚ**:
```bash
#!/bin/bash
# RayHunter ਕਨੈਕਟੀਵਿਟੀ ਦੀ ਉੱਨਤ ਸਮੱਸਿਆ-ਜਾਂਚ

echo "=== RayHunter ਨੈੱਟਵਰਕ ਜਾਂਚ ==="

# ਮੁੱਢਲੀ ਕਨੈਕਟੀਵਿਟੀ ਜਾਂਚੋ
echo "1. ਬੁਨਿਆਦੀ ਕਨੈਕਟੀਵਿਟੀ ਜਾਂਚ:"
ping -c 3 8.8.8.8 > /dev/null 2>&1
if [ $? -eq 0 ]; then
    echo "✓ ਇੰਟਰਨੈੱਟ ਕਨੈਕਟੀਵਿਟੀ: ਠੀਕ ਹੈ"
else
    echo "✗ ਇੰਟਰਨੈੱਟ ਕਨੈਕਟੀਵਿਟੀ: ਅਸਫਲ"
fi

# ਸੈੱਲੂਲਰ ਕਨੈਕਸ਼ਨ ਜਾਂਚੋ
echo -e "\n2. ਸੈਲੂਲਰ ਕਨੈਕਸ਼ਨ ਵਿਸ਼ਲੇਸ਼ਣ:"
if command -v qmicli &> /dev/null; then
    # ਮੋਡਮ ਦੀ ਸਥਿਤੀ ਜਾਂਚੋ
    qmicli -d /dev/cdc-wdm0 --dms-get-operating-mode
    qmicli -d /dev/cdc-wdm0 --nas-get-signal-strength
    qmicli -d /dev/cdc-wdm0 --nas-get-serving-system
else
    echo "qmicli ਉਪਲਬਧ ਨਹੀਂ; ਵਿਕਲਪੀ ਤਰੀਕੇ ਵਰਤੇ ਜਾ ਰਹੇ ਹਨ"

    # ਨੈੱਟਵਰਕ ਇੰਟਰਫੇਸ ਜਾਂਚੋ
    ip addr show | grep -A 10 wwan

    # ਰਾਊਟਿੰਗ ਜਾਂਚੋ
    ip route show
fi

# RayHunter ਵੈੱਬ ਇੰਟਰਫੇਸ ਜਾਂਚੋ
echo -e "\n3. RayHunter ਵੈੱਬ ਇੰਟਰਫੇਸ ਜਾਂਚ:"
for port in 8080 80; do
    if netstat -tuln | grep ":$port " > /dev/null; then
        echo "✓ ਪੋਰਟ $port ਸੁਣ ਰਹੀ ਹੈ"

        # HTTP ਜਵਾਬ ਦੀ ਜਾਂਚ ਕਰੋ
        if curl -s -o /dev/null -w "%{http_code}" "http://localhost:$port" | grep -q "200\|302"; then
            echo "✓ HTTP ਸੇਵਾ ਪੋਰਟ $port ਉੱਤੇ ਜਵਾਬ ਦੇ ਰਹੀ ਹੈ"
        else
            echo "✗ HTTP ਸੇਵਾ ਪੋਰਟ $port ਉੱਤੇ ਠੀਕ ਤਰ੍ਹਾਂ ਜਵਾਬ ਨਹੀਂ ਦੇ ਰਹੀ"
        fi
    else
        echo "✗ ਪੋਰਟ $port ਸੁਣ ਨਹੀਂ ਰਹੀ"
    fi
done

# ਸੈੱਲੂਲਰ ਡਾਇਗਨੌਸਟਿਕ ਇੰਟਰਫੇਸ ਜਾਂਚੋ
echo -e "\n4. ਸੈਲੂਲਰ ਡਾਇਗਨੌਸਟਿਕ ਇੰਟਰਫੇਸ:"
if [ -c /dev/diag ]; then
    echo "✓ /dev/diag ਇੰਟਰਫੇਸ ਉਪਲਬਧ ਹੈ"
    ls -la /dev/diag
else
    echo "✗ /dev/diag ਇੰਟਰਫੇਸ ਉਪਲਬਧ ਨਹੀਂ ਹੈ"
    echo "ਵਿਕਲਪੀ ਇੰਟਰਫੇਸਾਂ ਦੀ ਜਾਂਚ ਜਾਰੀ ਹੈ:"
    ls -la /dev/ | grep -E "ttyUSB|cdc-wdm|qcserial"
fi

# ਉੱਨਤ ਨੈੱਟਵਰਕ ਵਿਸ਼ਲੇਸ਼ਣ
echo -e "\n5. ਉੱਨਤ ਨੈੱਟਵਰਕ ਵਿਸ਼ਲੇਸ਼ਣ:"

# APN ਸੈਟਿੰਗਾਂ ਜਾਂਚੋ
echo "ਮੌਜੂਦਾ APN ਸੰਰਚਨਾ:"
grep -r "apn" /etc/NetworkManager/system-connections/ 2>/dev/null || echo "APN ਸੰਰਚਨਾ ਨਹੀਂ ਮਿਲੀ"

# DNS ਰੈਜ਼ੋਲਿਊਸ਼ਨ ਜਾਂਚੋ
echo "DNS ਰੈਜ਼ੋਲੂਸ਼ਨ ਜਾਂਚ:"
nslookup google.com | head -5

# ਫਾਇਰਵਾਲ ਨਿਯਮ ਜਾਂਚੋ
echo "RayHunter ਨੂੰ ਪ੍ਰਭਾਵਿਤ ਕਰਨ ਵਾਲੇ ਫਾਇਰਵਾਲ ਨਿਯਮ:"
iptables -L | grep -E "8080|rayhunter" || echo "ਕੋਈ ਖਾਸ ਫਾਇਰਵਾਲ ਨਿਯਮ ਨਹੀਂ ਮਿਲੇ"
```

#### ਡਿਵਾਈਸ-ਵਿਸ਼ੇਸ਼ ਸਮੱਸਿਆ ਨਿਵਾਰਨ

**Orbic RC400L ਲਈ ਉੱਨਤ ਸਮੱਸਿਆ ਨਿਵਾਰਨ**:
```bash
#!/bin/bash
# Orbic RC400L ਲਈ ਖ਼ਾਸ ਸਮੱਸਿਆ-ਜਾਂਚ ਪ੍ਰਕਿਰਿਆਵਾਂ

echo "=== Orbic RC400L ਉੱਨਤ ਜਾਂਚ ==="

# ਬੂਟਲੋਡਰ ਅਤੇ ਸਿਸਟਮ ਪਾਰਟੀਸ਼ਨ ਦੀ ਸਥਿਤੀ ਜਾਂਚੋ
echo "1. ਸਿਸਟਮ ਪਾਰਟੀਸ਼ਨ ਵਿਸ਼ਲੇਸ਼ਣ:"
df -h | grep -E "/system|/data|/usrdata"

# Android ਸਬਸਿਸਟਮ ਜਾਂਚੋ
echo -e "\n2. Android ਸਬਸਿਸਟਮ ਜਾਂਚ:"
if command -v adb &> /dev/null; then
    adb devices
    if adb devices | grep -q "device$"; then
        echo "✓ ADB ਕਨੈਕਸ਼ਨ ਉਪਲਬਧ ਹੈ"

        # ਸਿਸਟਮ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਜਾਂਚੋ
        adb shell getprop | grep -E "ro.build|persist.vendor"

        # ਚੱਲ ਰਹੀਆਂ ਪ੍ਰਕਿਰਿਆਵਾਂ ਜਾਂਚੋ
        adb shell ps | grep rayhunter

        # ਸਿਸਟਮ ਲੌਗ ਜਾਂਚੋ
        echo "ਹਾਲੀਆ ਸਿਸਟਮ ਗਲਤੀਆਂ:"
        adb logcat -d | grep -E "ERROR|FATAL" | tail -10
    else
        echo "✗ ADB ਕਨੈਕਸ਼ਨ ਉਪਲਬਧ ਨਹੀਂ ਹੈ"
    fi
else
    echo "ADB ਉਪਲਬਧ ਨਹੀਂ; ਵਿਕਲਪੀ ਤਰੀਕੇ ਵਰਤੇ ਜਾ ਰਹੇ ਹਨ"
fi

# ਮੋਡਮ ਫਰਮਵੇਅਰ ਜਾਂਚੋ
echo -e "\n3. ਮੋਡਮ ਫਰਮਵੇਅਰ ਵਿਸ਼ਲੇਸ਼ਣ:"
if [ -c /dev/diag ]; then
    # ਮੋਡਮ ਫਰਮਵੇਅਰ ਪੁੱਛਣ ਲਈ ਕਸਟਮ ਟੂਲ ਵਰਤੋ
    python3 << 'EOF'
import serial
import struct
import time

try:
    # ਡਾਇਗਨੌਸਟਿਕ ਇੰਟਰਫੇਸ ਖੋਲ੍ਹੋ
    diag = serial.Serial('/dev/diag', 115200, timeout=1)

    # ਫਰਮਵੇਅਰ ਵਰਜਨ ਪੁੱਛੋ (ਸਰਲ ਰੂਪ)
    # ਇਸ ਲਈ DIAG ਪ੍ਰੋਟੋਕੋਲ ਦੀ ਢੁੱਕਵੀਂ ਲਾਗੂਕਰਨ ਲੋੜੀਂਦੀ ਹੈ
    print("ਮੋਡਮ ਡਾਇਗਨੌਸਟਿਕ ਇੰਟਰਫੇਸ ਉਪਲਬਧ ਹੈ")
    diag.close()
except Exception as e:
    print(f"ਮੋਡਮ ਡਾਇਗਨੌਸਟਿਕ ਪਹੁੰਚ ਅਸਫਲ: {e}")
EOF
fi

# ਕੈਰੀਅਰ-ਖ਼ਾਸ ਸਮੱਸਿਆਵਾਂ ਜਾਂਚੋ
echo -e "\n4. ਕੈਰੀਅਰ ਸੰਰਚਨਾ ਜਾਂਚ:"
echo "ਮੌਜੂਦਾ ਬੈਂਡ ਪਸੰਦਾਂ:"
cat /data/rayhunter/config.toml | grep -A 5 -B 5 "band"

echo "ਨੈੱਟਵਰਕ ਰਜਿਸਟ੍ਰੇਸ਼ਨ ਸਥਿਤੀ:"
# ਸਾਰੇ ਉਪਲਬਧ ਕੈਰੀਅਰਾਂ ਨਾਲ ਰਜਿਸਟ੍ਰੇਸ਼ਨ ਜਾਂਚੋ
if command -v qmicli &> /dev/null; then
    qmicli -d /dev/cdc-wdm0 --nas-get-home-network
    qmicli -d /dev/cdc-wdm0 --nas-get-preferred-networks
fi
```

**TP-Link M7350 ਲਈ ਸਮੱਸਿਆ ਨਿਵਾਰਨ**:
```bash
#!/bin/bash
# TP-Link M7350 ਲਈ ਖ਼ਾਸ ਸਮੱਸਿਆ-ਜਾਂਚ

echo "=== TP-Link M7350 ਉੱਨਤ ਜਾਂਚ ==="

# SD ਕਾਰਡ ਦੀ ਕਾਰਗੁਜ਼ਾਰੀ ਜਾਂਚੋ
echo "1. SD ਕਾਰਡ ਡਾਇਗਨੌਸਟਿਕਸ:"
if mountpoint -q /media/sd; then
    echo "✓ SD ਕਾਰਡ ਮਾਊਂਟ ਹੈ"
    df -h /media/sd

    # SD ਕਾਰਡ ਦੀ ਸਿਹਤ ਜਾਂਚੋ
    echo "SD ਕਾਰਡ ਫ਼ਾਈਲ-ਸਿਸਟਮ ਜਾਂਚ:"
    fsck -n /dev/mmcblk0p1 2>&1 | head -10

    # ਲਿਖਣ ਦੀਆਂ ਇਜਾਜ਼ਤਾਂ ਜਾਂਚੋ
    touch /media/sd/test_write 2>/dev/null && rm /media/sd/test_write
    if [ $? -eq 0 ]; then
        echo "✓ SD ਕਾਰਡ ਲਿਖਣ ਦੀਆਂ ਇਜਾਜ਼ਤਾਂ ਠੀਕ ਹਨ"
    else
        echo "✗ SD ਕਾਰਡ ਲਿਖਣ ਦੀਆਂ ਇਜਾਜ਼ਤਾਂ ਅਸਫਲ ਰਹੀਆਂ"
    fi
else
    echo "✗ SD ਕਾਰਡ ਮਾਊਂਟ ਨਹੀਂ ਹੈ"
    echo "ਉਪਲਬਧ ਬਲਾਕ ਡਿਵਾਈਸਾਂ:"
    lsblk | grep -E "mmc|sd"
fi

# OpenWrt ਸਿਸਟਮ ਜਾਂਚੋ
echo -e "\n2. OpenWrt ਸਿਸਟਮ ਵਿਸ਼ਲੇਸ਼ਣ:"
echo "ਸਿਸਟਮ ਜਾਣਕਾਰੀ:"
cat /proc/version
uname -a

echo "ਉਪਲਬਧ ਮੈਮੋਰੀ:"
free -h

echo "ਸਿਸਟਮ ਲੋਡ:"
uptime

# ਪੈਕੇਜ ਇੰਸਟਾਲੇਸ਼ਨ ਜਾਂਚੋ
echo "RayHunter ਲਈ ਸੰਬੰਧਿਤ ਇੰਸਟਾਲ ਕੀਤੇ ਪੈਕੇਜ:"
opkg list-installed | grep -E "python|kmod|usb"

# ਕਰਨਲ ਮੋਡੀਊਲ ਜਾਂਚੋ
echo -e "\n3. ਕਰਨਲ ਮੋਡੀਊਲ ਸਥਿਤੀ:"
lsmod | grep -E "diag|qmi|cdc|usb"

# USB ਡਾਇਗਨੌਸਟਿਕ ਇੰਟਰਫੇਸ ਜਾਂਚੋ
echo "USB ਡਾਇਗਨੌਸਟਿਕ ਡਿਵਾਈਸਾਂ:"
lsusb -t
ls -la /dev/ttyUSB* 2>/dev/null || echo "ਕੋਈ USB ਸੀਰੀਅਲ ਡਿਵਾਈਸ ਨਹੀਂ ਮਿਲੀ"
```

### ਰਿਕਵਰੀ ਪ੍ਰਕਿਰਿਆਵਾਂ

**ਸਿਸਟਮ ਰਿਕਵਰੀ ਸਕ੍ਰਿਪਟਾਂ**:
```bash
#!/bin/bash
# RayHunter ਸਿਸਟਮ ਦੀ ਐਮਰਜੈਂਸੀ ਰਿਕਵਰੀ

BACKUP_DIR="/data/rayhunter/backup"
CONFIG_FILE="/data/rayhunter/config.toml"
RECOVERY_LOG="/var/log/rayhunter/recovery.log"

log_message() {
    echo "$(date): $1" | tee -a "$RECOVERY_LOG"
}

create_backup() {
    log_message "Creating system backup..."
    mkdir -p "$BACKUP_DIR"

    # ਸੰਰਚਨਾ ਦਾ ਬੈਕਅੱਪ ਲਓ
    cp "$CONFIG_FILE" "$BACKUP_DIR/config_$(date +%Y%m%d_%H%M%S).toml"

    # ਪਿਛਲੇ 24 ਘੰਟਿਆਂ ਦੀਆਂ ਰਿਕਾਰਡਿੰਗਾਂ ਦਾ ਬੈਕਅੱਪ ਲਓ
    find /data/rayhunter/recordings -name "*.qmdl" -mtime -1 -exec cp {} "$BACKUP_DIR/" \;

    # ਲੌਗਾਂ ਦਾ ਬੈਕਅੱਪ ਲਓ
    tar -czf "$BACKUP_DIR/logs_$(date +%Y%m%d_%H%M%S).tar.gz" /data/rayhunter/logs/

    log_message "Backup completed"
}

reset_configuration() {
    log_message "Resetting configuration to defaults..."

    # RayHunter ਸੇਵਾ ਰੋਕੋ
    systemctl stop rayhunter_daemon

    # ਫੈਕਟਰੀ ਸੰਰਚਨਾ ਮੁੜ ਸੈੱਟ ਕਰੋ
    cp /etc/rayhunter/config.toml.default "$CONFIG_FILE"

    # ਸਮੱਸਿਆ ਵਾਲੀਆਂ ਕੈਸ਼ ਫਾਈਲਾਂ ਸਾਫ਼ ਕਰੋ
    rm -f /data/rayhunter/cache/*

    # ਇਜਾਜ਼ਤਾਂ ਮੁੜ ਸੈੱਟ ਕਰੋ
    chown -R rayhunter:rayhunter /data/rayhunter/
    chmod -R 755 /data/rayhunter/

    log_message "Configuration reset completed"
}

factory_reset() {
    log_message "Performing factory reset..."

    # ਪਹਿਲਾਂ ਬੈਕਅੱਪ ਬਣਾਓ
    create_backup

    # RayHunter ਦੀਆਂ ਸਾਰੀਆਂ ਸੇਵਾਵਾਂ ਰੋਕੋ
    systemctl stop rayhunter_daemon
    systemctl disable rayhunter_daemon

    # ਬੈਕਅੱਪਾਂ ਤੋਂ ਇਲਾਵਾ RayHunter ਦਾ ਸਾਰਾ ਡਾਟਾ ਹਟਾਓ
    find /data/rayhunter -type f ! -path "*/backup/*" -delete

    # RayHunter ਮੁੜ ਇੰਸਟਾਲ ਕਰੋ
    cd /tmp
    wget -O rayhunter-latest.zip "https://github.com/EFForg/rayhunter/releases/latest/download/rayhunter-linux-x64.zip"
    unzip rayhunter-latest.zip
    ./installer $(detect_device_type)

    log_message "Factory reset completed"
}

detect_device_type() {
    # ਮੁੜ ਇੰਸਟਾਲ ਕਰਨ ਲਈ ਡਿਵਾਈਸ ਦੀ ਕਿਸਮ ਆਪਣੇ ਆਪ ਪਛਾਣੋ
    if grep -q "Orbic" /proc/cpuinfo || [ -d "/android_root" ]; then
        echo "orbic"
    elif grep -q "MT7620" /proc/cpuinfo || [ -f "/etc/openwrt_version" ]; then
        echo "tplink"
    else
        echo "unknown"
    fi
}

# ਮੁੱਖ ਰਿਕਵਰੀ ਮੀਨੂ
echo "=== RayHunter ਦੀ ਐਮਰਜੈਂਸੀ ਰਿਕਵਰੀ ==="
echo "1. ਸਿਰਫ਼ ਬੈਕਅੱਪ ਬਣਾਓ"
echo "2. ਸੰਰਚਨਾ ਨੂੰ ਡਿਫਾਲਟ ਮੁੱਲਾਂ 'ਤੇ ਮੁੜ ਸੈੱਟ ਕਰੋ"
echo "3. ਫੈਕਟਰੀ ਰੀਸੈੱਟ (ਵਿਨਾਸ਼ਕਾਰੀ)"
echo "4. ਸਿਸਟਮ ਡਾਇਗਨੌਸਟਿਕ"
echo "5. ਬਾਹਰ ਨਿਕਲੋ"

read -p "ਵਿਕਲਪ ਚੁਣੋ (1-5): " choice

case $choice in
    1) create_backup ;;
    2) reset_configuration ;;
    3)
        read -p "ਕੀ ਤੁਸੀਂ ਯਕੀਨੀ ਹੋ? ਬੈਕਅੱਪ ਤੋਂ ਇਲਾਵਾ ਸਾਰਾ ਡਾਟਾ ਮਿਟ ਜਾਵੇਗਾ (y/N): " confirm
        if [ "$confirm" = "y" ] || [ "$confirm" = "Y" ]; then
            factory_reset
        else
            echo "ਫੈਕਟਰੀ ਰੀਸੈੱਟ ਰੱਦ ਕੀਤਾ ਗਿਆ"
        fi
        ;;
    4)
        echo "ਸਿਸਟਮ ਡਾਇਗਨੌਸਟਿਕ ਚੱਲ ਰਿਹਾ ਹੈ..."
        # ਸਾਰੇ ਡਾਇਗਨੌਸਟਿਕ ਸਕ੍ਰਿਪਟ ਚਲਾਓ
        /opt/rayhunter/scripts/performance_check.sh
        /opt/rayhunter/scripts/network_diagnostics.sh
        ;;
    5) exit 0 ;;
    *) echo "ਅਵੈਧ ਵਿਕਲਪ" ;;
esac
```

## ਮਾਹਰ ਏਕੀਕਰਨ ਦੇ ਦ੍ਰਿਸ਼

{{< figure src="rayhunter-soc-integration-workflow.webp" alt="RayHunter REST API ਡਾਟੇ ਨੂੰ ਸੁਰੱਖਿਆ ਕਾਰਜ ਕੇਂਦਰ ਡੈਸ਼ਬੋਰਡ ਤੱਕ ਭੇਜਣ ਦਾ ਵਰਕਫਲੋ ਚਿੱਤਰ, ਨਾਲ SIEM ਚੇਤਾਵਨੀਆਂ ਅਤੇ ਖੋਜ ਨਿਰਯਾਤ ਧਾਰਾਵਾਂ।" >}}

### ਖੋਜ ਮਾਹੌਲ ਨਾਲ ਏਕੀਕਰਨ

**ਅਕਾਦਮਿਕ ਖੋਜ ਕਨਫਿਗਰੇਸ਼ਨ**:
```python
#!/usr/bin/env python3
"""
RayHunter ਖੋਜ ਏਕੀਕਰਨ ਪਲੇਟਫਾਰਮ
ਅਕਾਦਮਿਕ ਸੈਲੂਲਰ ਸੁਰੱਖਿਆ ਖੋਜ ਲਈ ਉੱਨਤ ਸੰਰਚਨਾ
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
        """ਖੋਜ ਡਾਟਾਬੇਸ ਲਈ ਪੂਰਾ ਸਕੀਮਾ ਤਿਆਰ ਕਰੋ"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        # ਖੋਜ ਡਾਟਾ ਲਈ ਸਕੀਮਾ ਵਧਾਓ
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
        """ਦਿੱਤੇ ਪੈਰਾਮੀਟਰਾਂ ਨਾਲ ਨਿਯੰਤਰਿਤ ਪ੍ਰਯੋਗ ਕਰੋ"""
        session_id = f"exp_{datetime.now().strftime('%Y%m%d_%H%M%S')}"

        # ਪ੍ਰਯੋਗ ਲਈ RayHunter ਸੰਰਚਿਤ ਕਰੋ
        self.configure_rayhunter_for_research(experiment_config)

        # ਡਾਟਾ ਇਕੱਠਾ ਕਰਨਾ ਸ਼ੁਰੂ ਕਰੋ
        collection_start = datetime.now()

        # ਨਿਰਧਾਰਤ ਮਿਆਦ ਲਈ ਪ੍ਰਯੋਗ ਚਲਾਓ
        experiment_duration = experiment_config.get('duration_minutes', 60)

        # ਮੁੱਢਲੇ ਮਾਪ ਇਕੱਠੇ ਕਰੋ
        baseline_data = self.collect_baseline_measurements(experiment_duration // 3)

        # ਜੇ ਦਿੱਤੇ ਹੋਣ ਤਾਂ ਨਿਯੰਤਰਿਤ ਬਦਲ ਸ਼ਾਮਲ ਕਰੋ
        if experiment_config.get('introduce_threats', False):
            threat_data = self.simulate_threat_scenarios(experiment_config['threat_scenarios'])

        # ਦਖ਼ਲਅੰਦਾਜ਼ੀ ਤੋਂ ਬਾਅਦ ਦਾ ਡਾਟਾ ਇਕੱਠਾ ਕਰੋ
        post_data = self.collect_post_measurements(experiment_duration // 3)

        # ਨਤੀਜਿਆਂ ਦਾ ਵਿਸ਼ਲੇਸ਼ਣ ਕਰੋ
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
        """ਧਮਕੀ ਪਛਾਣ ਦੇ ਰੁਝਾਨਾਂ ਦਾ ਅੰਕੜਾਤਮਕ ਵਿਸ਼ਲੇਸ਼ਣ ਕਰੋ"""
        conn = sqlite3.connect(self.db_path)

        # ਖ਼ਤਰੇ ਦੇ ਅਵਲੋਕਨਾਂ ਲਈ ਪੁੱਛੋ
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
            return {"error": "ਵਿਸ਼ਲੇਸ਼ਣ ਲਈ ਕੋਈ ਡਾਟਾ ਉਪਲਬਧ ਨਹੀਂ"}

        # ਅੰਕੜਾ ਵਿਸ਼ਲੇਸ਼ਣ
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

        # ਵਾਤਾਵਰਣ ਨਾਲ ਸਬੰਧ ਦਾ ਵਿਸ਼ਲੇਸ਼ਣ
        for env_type in df['environment_type'].unique():
            env_data = df[df['environment_type'] == env_type]
            analysis['environmental_correlation'][env_type] = {
                'threat_frequency': len(env_data) / time_period_days,
                'average_confidence': env_data['confidence_score'].mean(),
                'threat_type_distribution': env_data['threat_type'].value_counts().to_dict()
            }

        # ਦ੍ਰਿਸ਼-ਰੂਪ ਤਿਆਰ ਕਰੋ
        self.generate_research_visualizations(df, analysis)

        return analysis

    def generate_research_visualizations(self, df, analysis):
        """ਖੋਜ ਲਈ ਵਿਸਤ੍ਰਿਤ ਦ੍ਰਿਸ਼ ਬਣਾਓ"""
        fig, axes = plt.subplots(2, 3, figsize=(20, 12))

        # ਖ਼ਤਰੇ ਦੀਆਂ ਕਿਸਮਾਂ ਦੀ ਵੰਡ
        threat_counts = df['threat_type'].value_counts()
        axes[0, 0].pie(threat_counts.values, labels=threat_counts.index, autopct='%1.1f%%')
        axes[0, 0].set_title('ਖ਼ਤਰੇ ਦੀ ਕਿਸਮ ਅਨੁਸਾਰ ਵੰਡ')

        # ਭਰੋਸਾ ਸਕੋਰਾਂ ਦੀ ਵੰਡ
        axes[0, 1].hist(df['confidence_score'], bins=20, alpha=0.7)
        axes[0, 1].set_title('ਭਰੋਸਾ ਸਕੋਰ ਦੀ ਵੰਡ')
        axes[0, 1].set_xlabel('ਭਰੋਸਾ ਸਕੋਰ')
        axes[0, 1].set_ylabel('ਆਵ੍ਰਿਤੀ')

        # ਸਮੇਂ ਅਨੁਸਾਰ ਰੁਝਾਨ
        df['hour'] = pd.to_datetime(df['timestamp']).dt.hour
        hourly_counts = df.groupby('hour').size()
        axes[0, 2].bar(hourly_counts.index, hourly_counts.values)
        axes[0, 2].set_title('ਦਿਨ ਦੇ ਘੰਟੇ ਅਨੁਸਾਰ ਖ਼ਤਰੇ')
        axes[0, 2].set_xlabel('ਘੰਟਾ')
        axes[0, 2].set_ylabel('ਖ਼ਤਰਿਆਂ ਦੀ ਗਿਣਤੀ')

        # ਵਾਤਾਵਰਣ ਅਤੇ ਭਰੋਸੇ ਦਾ ਸਬੰਧ
        sns.boxplot(data=df, x='environment_type', y='confidence_score', ax=axes[1, 0])
        axes[1, 0].set_title('ਵਾਤਾਵਰਣ ਦੀ ਕਿਸਮ ਅਨੁਸਾਰ ਭਰੋਸਾ')
        axes[1, 0].tick_params(axis='x', rotation=45)

        # ਸਬੰਧ ਹੀਟਮੈਪ
        numeric_df = df.select_dtypes(include=[np.number])
        correlation_matrix = numeric_df.corr()
        sns.heatmap(correlation_matrix, annot=True, ax=axes[1, 1])
        axes[1, 1].set_title('ਸਬੰਧ ਮੈਟ੍ਰਿਕਸ')

        # ਗਲਤ ਚੇਤਾਵਨੀਆਂ ਦਾ ਵਿਸ਼ਲੇਸ਼ਣ
        if 'false_positive_assessment' in df.columns:
            fp_data = df['false_positive_assessment'].value_counts()
            axes[1, 2].bar(fp_data.index, fp_data.values)
            axes[1, 2].set_title('ਗਲਤ ਸਕਾਰਾਤਮਕ ਦਾ ਮੁਲਾਂਕਣ')
            axes[1, 2].tick_params(axis='x', rotation=45)

        plt.tight_layout()
        plt.savefig(f'/data/research/analysis/visualization_{datetime.now().strftime("%Y%m%d_%H%M%S")}.png',
                   dpi=300, bbox_inches='tight')
        plt.close()

    def export_research_data(self, format='csv', time_range_days=None):
        """ਬਾਹਰੀ ਵਿਸ਼ਲੇਸ਼ਣ ਲਈ ਖੋਜ ਡਾਟਾ ਵੱਖ-ਵੱਖ ਫਾਰਮੈਟਾਂ ਵਿੱਚ ਨਿਰਯਾਤ ਕਰੋ"""
        conn = sqlite3.connect(self.db_path)

        if time_range_days:
            end_date = datetime.now()
            start_date = end_date - timedelta(days=time_range_days)
            date_filter = f"WHERE timestamp BETWEEN '{start_date.isoformat()}' AND '{end_date.isoformat()}'"
        else:
            date_filter = ""

        # ਖ਼ਤਰੇ ਦੇ ਅਵਲੋਕਨ ਐਕਸਪੋਰਟ ਕਰੋ
        threat_query = f"SELECT * FROM threat_observations {date_filter}"
        threat_df = pd.read_sql_query(threat_query, conn)

        # ਸੈੱਲੂਲਰ ਮਾਪ ਐਕਸਪੋਰਟ ਕਰੋ
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

## ਨਤੀਜਾ

**RayHunter** ਦੀ ਉੱਨਤ ਤੈਨਾਤੀ ਲਈ **ਸੈਲੂਲਰ ਪ੍ਰੋਟੋਕੋਲ**, **RF ਵਿਸ਼ਲੇਸ਼ਣ**, ਸਿਸਟਮ ਏਕੀਕਰਨ ਅਤੇ ਖ਼ਤਰਾ ਮਾਡਲਿੰਗ ਵਰਗੇ ਕਈ ਖੇਤਰਾਂ ਵਿੱਚ ਤਕਨੀਕੀ ਮਾਹਰਤਾ ਚਾਹੀਦੀ ਹੈ। ਇਸ ਗਾਈਡ ਦੀਆਂ ਤਕਨੀਕਾਂ ਮਾਹਰਾਂ ਨੂੰ ਗਲਤ ਸਕਾਰਾਤਮਕ ਨਤੀਜੇ ਅਤੇ ਕਾਰਜ ਭਾਰ ਘਟਾਉਂਦੇ ਹੋਏ **RayHunter** ਦੀ ਪਛਾਣ ਸਮਰੱਥਾ ਦਾ ਵੱਧ ਤੋਂ ਵੱਧ ਲਾਭ ਲੈਣ ਵਿੱਚ ਮਦਦ ਕਰਦੀਆਂ ਹਨ।

*ਉੱਨਤ **RayHunter** ਕਾਰਜਾਂ ਦੇ ਮੁੱਖ ਨੁਕਤੇ ਇਹ ਹਨ:*

1. **ਕਸਟਮ ਹਿਊਰਿਸਟਿਕ ਅਨੁਕੂਲਨ** ਮਾਹੌਲ ਅਨੁਸਾਰ ਕਨਫਿਗਰੇਸ਼ਨ ਰਾਹੀਂ ਪਛਾਣ ਸੰਵੇਦਨਸ਼ੀਲਤਾ ਕਾਇਮ ਰੱਖਦੇ ਹੋਏ ਗਲਤ ਸਕਾਰਾਤਮਕ ਨਤੀਜੇ 80% ਘਟਾ ਸਕਦਾ ਹੈ
2. **API-ਅਧਾਰਿਤ ਆਟੋਮੇਸ਼ਨ** ਐਂਟਰਪ੍ਰਾਈਜ਼ ਪੱਧਰ ਦੀ ਤੈਨਾਤੀ ਅਤੇ ਮੌਜੂਦਾ ਸੁਰੱਖਿਆ ਕਾਰਜ ਕੇਂਦਰਾਂ ਨਾਲ ਏਕੀਕਰਨ ਸੰਭਵ ਕਰਦੀ ਹੈ
3. **ਕਈ ਡਿਵਾਈਸਾਂ ਦਾ ਤਾਲਮੇਲ** ਵੱਡੇ ਖੇਤਰ ਦੀ ਕਵਰੇਜ ਅਤੇ ਆਪਸੀ ਪੁਸ਼ਟੀ ਦਿੰਦਾ ਹੈ, ਜਿਸ ਨਾਲ ਖ਼ਤਰਾ ਪਛਾਣ ’ਤੇ ਭਰੋਸਾ ਵਧਦਾ ਹੈ
4. **ਉੱਨਤ ਸਮੱਸਿਆ ਨਿਵਾਰਨ ਵਿਧੀਆਂ** ਵੱਖ-ਵੱਖ ਅਤੇ ਚੁਣੌਤੀਪੂਰਨ ਮਾਹੌਲਾਂ ਵਿੱਚ ਭਰੋਸੇਯੋਗ ਕਾਰਜ ਨੂੰ ਯਕੀਨੀ ਬਣਾਉਂਦੀਆਂ ਹਨ
5. **ਖੋਜ ਏਕੀਕਰਨ ਸਮਰੱਥਾਵਾਂ** ਸੈਲੂਲਰ ਸੁਰੱਖਿਆ ਖ਼ਤਰਿਆਂ ਬਾਰੇ ਅਕਾਦਮਿਕ ਅਤੇ ਵਪਾਰਕ ਖੋਜ ਦਾ ਸਮਰਥਨ ਕਰਦੀਆਂ ਹਨ

**RayHunter** ਦੇ ਮਾਹਰ ਵਰਤੋਂਕਾਰਾਂ ਨੂੰ **ਸੈਲੂਲਰ ਸੁਰੱਖਿਆ**, **ਨਿਗਰਾਨੀ ਤਕਨਾਲੋਜੀ** ਅਤੇ ਓਪਨ-ਸੋਰਸ ਪਛਾਣ ਸਮਰੱਥਾਵਾਂ ਵਿੱਚ ਤਰੱਕੀ ’ਤੇ ਨਜ਼ਰ ਰੱਖਣੀ ਚਾਹੀਦੀ ਹੈ। *ਬਦਲਦੇ ਖ਼ਤਰਿਆਂ ਲਈ ਪਛਾਣ ਤਕਨੀਕਾਂ ਅਤੇ ਕਾਰਜ ਪ੍ਰਕਿਰਿਆਵਾਂ ਨੂੰ ਲਗਾਤਾਰ ਸੁਧਾਰਨਾ ਲੋੜੀਂਦਾ ਹੈ।*

ਪੇਸ਼ੇਵਰ ਸੁਰੱਖਿਆ ਕਾਰਜਾਂ ਵਿੱਚ **RayHunter** ਵਰਤਣ ਵਾਲੀਆਂ ਸੰਸਥਾਵਾਂ ਨੂੰ ਸਮਰਪਿਤ **ਸੁਰੱਖਿਆ ਕਾਰਜ ਕੇਂਦਰ** ਨਾਲ ਏਕੀਕਰਨ, ਕਰਮਚਾਰੀਆਂ ਦੀ ਨਿਯਮਿਤ ਸਿਖਲਾਈ ਅਤੇ ਖ਼ਤਰੇ ਦੀ ਜਾਣਕਾਰੀ ਤੇ ਪਛਾਣ ਸੁਧਾਰ ਸਾਂਝੇ ਕਰਨ ਲਈ ਵੱਡੇ **RayHunter** ਭਾਈਚਾਰੇ ਨਾਲ ਸਹਿਯੋਗ ਬਾਰੇ ਸੋਚਣਾ ਚਾਹੀਦਾ ਹੈ।

ਇਨ੍ਹਾਂ ਉੱਨਤ ਕਨਫਿਗਰੇਸ਼ਨਾਂ ਲਈ ਹਾਰਡਵੇਅਰ ਨਹੀਂ ਹੈ? **[RayHunter ਨਾਲ ਅਨੁਕੂਲਤਾ ਦੀ ਪੁਸ਼ਟੀ ਕੀਤੇ ਡਿਵਾਈਸ](https://stscollective.com/collections/rayhunter)** STS Collective ’ਤੇ ਉਪਲਬਧ ਹਨ। ਪਾਠਕ ਕੋਡ **SIMEONONSECURITY** ਨਾਲ 20% ਤੱਕ ਛੂਟ ਮਿਲਦੀ ਹੈ।

{{< centerbutton href="https://stscollective.com/discount/SIMEONONSECURITY" >}}
  RayHunter ਡਿਵਾਈਸ ਖਰੀਦੋ, 20% ਬਚਾਓ
{{< /centerbutton >}}

## ਹਵਾਲੇ

- [RayHunter ਦਾ ਅਧਿਕਾਰਤ ਦਸਤਾਵੇਜ਼](https://efforg.github.io/rayhunter/introduction.html)
- [RayHunter REST API ਹਵਾਲਾ](https://efforg.github.io/rayhunter/api-docs/)
- [Electronic Frontier Foundation](https://www.eff.org/)
- [GitHub ’ਤੇ RayHunter ਰਿਪੋਜ਼ਟਰੀ](https://github.com/EFForg/rayhunter)
- [ਸੈਲੂਲਰ ਪ੍ਰੋਟੋਕੋਲ ਵਿਸ਼ਲੇਸ਼ਣ ਸਰੋਤ](https://www.sharetechnote.com/)
- [RF ਵਿਸ਼ਲੇਸ਼ਣ ਅਤੇ SDR ਸਰੋਤ](https://greatscottgadgets.com/sdr/)
- [ਐਂਟਰਪ੍ਰਾਈਜ਼ ਸੁਰੱਖਿਆ ਏਕੀਕਰਨ ਲਈ ਸਰਬੋਤਮ ਅਭਿਆਸ](https://www.sans.org/white-papers/)
