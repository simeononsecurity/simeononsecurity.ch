---
title: "Flock Finder: Flock Safety ALPR ਕੈਮਰਿਆਂ ਦਾ ਨਕਸ਼ਾ"
date: 2026-07-22
toc: true
draft: false
description: "Flock Finder ਇੱਕ ਓਪਨ-ਸੋਰਸ ਟੂਲ ਹੈ ਜੋ WiGLE WiFi ਡੇਟਾ ਅਤੇ OUI ਫਿੰਗਰਪ੍ਰਿੰਟਿੰਗ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਦੁਨੀਆ ਭਰ ਵਿੱਚ 40,000+ Flock Safety ALPR ਕੈਮਰਿਆਂ ਦਾ ਨਕਸ਼ਾ ਬਣਾਉਂਦਾ ਹੈ। ਜਾਣੋ ਇਹ ਕਿਵੇਂ ਕੰਮ ਕਰਦਾ ਹੈ, ਇਸ ਦੀਆਂ ਸੀਮਾਵਾਂ ਅਤੇ ਰੀਅਲ-ਟਾਈਮ ਖੋਜ ਲਈ ਹਾਰਡਵੇਅਰ ਟੂਲ।"
genre: ["ਗੋਪਨੀਯਤਾ ਤਕਨੀਕ", "ਜਵਾਬੀ ਨਿਗਰਾਨੀ", "ਓਪਨ ਸੋਰਸ ਪ੍ਰੋਜੈਕਟ", "ਡਿਜੀਟਲ ਅਧਿਕਾਰ", "ਨੈੱਟਵਰਕ ਸੁਰੱਖਿਆ", "ਗੋਪਨੀਯਤਾ ਸਾਧਨ", "ਹਾਰਡਵੇਅਰ ਹੈਕਿੰਗ", "ਸੁਰੱਖਿਆ ਖੋਜ"]
tags: ["Flock Finder", "Flock Safety", "ALPR", "ਲਾਇਸੈਂਸ ਪਲੇਟ ਰੀਡਰ", "OUI ਫਿੰਗਰਪ੍ਰਿੰਟਿੰਗ", "WiGLE", "WiFi ਨਿਗਰਾਨੀ", "ਜਵਾਬੀ ਨਿਗਰਾਨੀ", "STS Collective", "FlockYou", "ESP32", "ਗੋਪਨੀਯਤਾ ਸਾਧਨ", "NitekryDPaul", "DeFlockJoplin", "ALPR ਖੋਜ", "ਓਪਨ ਸੋਰਸ ਸੁਰੱਖਿਆ", "ਨਿਗਰਾਨੀ ਮੈਪਿੰਗ", "ਸਮੂਹਿਕ ਨਿਗਰਾਨੀ", "WiFi OUI", "ਗੋਪਨੀਯਤਾ ਸੁਰੱਖਿਆ", "MAC ਪਤਾ", "ਪ੍ਰੋਮਿਸਕਿਊਸ ਮੋਡ", "802.11", "ਰੀਅਲ-ਟਾਈਮ ਖੋਜ", "Wardriving", "ਡਿਜੀਟਲ ਅਧਿਕਾਰ", "ਨਾਗਰਿਕ ਸੁਤੰਤਰਤਾਵਾਂ", "ਨਿਗਰਾਨੀ ਜਾਗਰੂਕਤਾ", "GitHub", "Python"]
cover: "/img/cover/flock-finder-open-source-alpr-camera-map.webp"
coverAlt: "ਇੱਕ ਇੰਟਰੈਕਟਿਵ ਨਕਸ਼ਾ ਜਿਸ ਵਿੱਚ Flock Safety ALPR ਕੈਮਰਿਆਂ ਦੀਆਂ ਸਥਿਤੀਆਂ ਦਰਸਾਉਣ ਵਾਲੇ ਰੰਗਦਾਰ ਮਾਰਕਰ ਦਿਖਾਏ ਗਏ ਹਨ, ਹਨੇਰੇ ਪਿਛੋਕੜ 'ਤੇ ਮਾਰਕਰਾਂ ਤੋਂ ਅਮੂਰਤ WiFi ਸੰਕੇਤ ਨਿਕਲ ਰਹੇ ਹਨ।"
coverCaption: "Flock Finder WiGLE WiFi ਡੇਟਾ ਅਤੇ OUI ਫਿੰਗਰਪ੍ਰਿੰਟਿੰਗ ਦੀ ਵਰਤੋਂ ਕਰਕੇ 40,000+ ਸ਼ੱਕੀ Flock Safety ALPR ਕੈਮਰਿਆਂ ਦਾ ਨਕਸ਼ਾ ਬਣਾਉਂਦਾ ਹੈ।"
canonical: "https://simeononsecurity.com/articles/flock-finder-alpr-surveillance-mapping-tool/"
---

**ਇੱਕ ਓਪਨ-ਸੋਰਸ ਨਿਗਰਾਨੀ ਜਾਗਰੂਕਤਾ ਟੂਲ ਜੋ ਕ੍ਰਾਊਡਸੋਰਸਡ WiFi ਡੇਟਾ ਦੀ ਵਰਤੋਂ ਕਰਕੇ Flock Safety ALPR ਕੈਮਰਿਆਂ ਦਾ ਨਕਸ਼ਾ ਬਣਾਉਂਦਾ ਹੈ।**

## Flock Finder ਕੀ ਹੈ?

**[Flock Finder](https://simeononsecurity.github.io/flock-finder/)** ਇੱਕ ਓਪਨ-ਸੋਰਸ ਪ੍ਰੋਜੈਕਟ ਹੈ ਜੋ ਸੰਯੁਕਤ ਰਾਜ ਅਮਰੀਕਾ ਅਤੇ 108 ਹੋਰ ਦੇਸ਼ਾਂ ਵਿੱਚ **Flock Safety ALPR (ਆਟੋਮੈਟਿਕ ਲਾਇਸੈਂਸ ਪਲੇਟ ਰੀਡਰ) ਕੈਮਰਿਆਂ** ਦਾ ਨਕਸ਼ਾ ਬਣਾਉਂਦਾ ਹੈ। ਇਹ **31 ਜਾਣੇ-ਪਛਾਣੇ Flock Safety WiFi OUI (ਸੰਗਠਨਾਤਮਕ ਤੌਰ 'ਤੇ ਵਿਲੱਖਣ ਪਛਾਣਕਰਤਾ) ਪ੍ਰੀਫਿਕਸਾਂ** ਨੂੰ **WiGLE ਕ੍ਰਾਊਡਸੋਰਸਡ WiFi ਡੇਟਾਬੇਸ** ਨਾਲ ਮਿਲਾਉਂਦਾ ਹੈ ਤਾਂ ਜੋ ਸ਼ੱਕੀ ਕੈਮਰਾ ਸਥਿਤੀਆਂ ਨੂੰ ਇੱਕ ਇੰਟਰੈਕਟਿਵ ਨਕਸ਼ੇ 'ਤੇ ਪਛਾਣਿਆ ਅਤੇ ਪਲਾਟ ਕੀਤਾ ਜਾ ਸਕੇ।

ਇਹ ਪ੍ਰੋਜੈਕਟ **[github.com/simeononsecurity/flock-finder](https://github.com/simeononsecurity/flock-finder)** 'ਤੇ ਮੌਜੂਦ ਹੈ, GitHub Actions ਰਾਹੀਂ ਰੋਜ਼ਾਨਾ ਆਟੋਮੈਟਿਕ ਅੱਪਡੇਟ ਹੁੰਦਾ ਹੈ, ਅਤੇ ਜੁਲਾਈ 2026 ਤੱਕ ਦੁਨੀਆ ਭਰ ਦੇ 964 ਖੇਤਰਾਂ ਵਿੱਚ **40,000 ਤੋਂ ਵੱਧ ਸ਼ੱਕੀ ਕੈਮਰਿਆਂ** ਦਾ ਨਕਸ਼ਾ ਬਣਾ ਚੁੱਕਾ ਹੈ।

| ਮੈਟ੍ਰਿਕ | ਮੁੱਲ |
|--------|-------|
| **ਨਕਸ਼ੇ 'ਤੇ ਕੈਮਰੇ** | 40,026+ |
| **ਜਾਣੇ-ਪਛਾਣੇ OUI ਪ੍ਰੀਫਿਕਸ** | 31 |
| **ਕਵਰ ਕੀਤੇ ਦੇਸ਼** | 109 |
| **ਕਵਰ ਕੀਤੇ ਖੇਤਰ** | 964 |
| **ਡੇਟਾ ਸੰਭਾਲ** | 730 ਦਿਨ (2 ਸਾਲ) |
| **ਆਟੋਮੈਟਿਕ ਅੱਪਡੇਟ ਦੀ ਬਾਰੰਬਾਰਤਾ** | ਰੋਜ਼ਾਨਾ |

*ਇਹ ਇੱਕ ਸਧਾਰਨ ਜਾਗਰੂਕਤਾ ਟੂਲ ਹੈ, ਨਿਸ਼ਚਿਤ ਸੂਚੀ ਨਹੀਂ। ਡੇਟਾ ਤੋਂ ਸਿੱਟੇ ਕੱਢਣ ਤੋਂ ਪਹਿਲਾਂ ਸੀਮਾਵਾਂ ਵਾਲਾ ਭਾਗ ਪੜ੍ਹੋ।*

Flock Safety ALPR ਨਿਗਰਾਨੀ ਗੋਪਨੀਯਤਾ ਲਈ ਕਿਉਂ ਮਹੱਤਵਪੂਰਨ ਹੈ, ਇਸ ਬਾਰੇ ਪਿਛੋਕੜ ਲਈ ਪੜ੍ਹੋ **[Flock Safety ਕੈਮਰਾ ਨਿਗਰਾਨੀ: ਪ੍ਰਸਾਰ, ਗੋਪਨੀਯਤਾ ਚਿੰਤਾਵਾਂ ਅਤੇ ਸੁਰੱਖਿਆ ਰਣਨੀਤੀਆਂ](/articles/flock-safety-camera-surveillance-prevalence-privacy-protection-2026/)**।

______

## ਇਹ ਕਿਵੇਂ ਕੰਮ ਕਰਦਾ ਹੈ: WiGLE ਰਾਹੀਂ OUI ਫਿੰਗਰਪ੍ਰਿੰਟਿੰਗ

### ਮੁੱਖ ਸਮਝ

Flock Safety ਕੈਮਰਿਆਂ ਵਿੱਚ **WiFi ਟ੍ਰਾਂਸਸੀਵਰ** ਹੁੰਦੇ ਹਨ ਜੋ ਕੈਪਚਰ ਕੀਤੇ ਲਾਇਸੈਂਸ ਪਲੇਟ ਡੇਟਾ ਨੂੰ ਕਲਾਊਡ 'ਤੇ ਅੱਪਲੋਡ ਕਰਨ ਲਈ ਸਮੇਂ-ਸਮੇਂ 'ਤੇ ਨੀਂਦ ਤੋਂ ਜਾਗਦੇ ਹਨ। ਇਹਨਾਂ ਸੰਖੇਪ ਸਰਗਰਮ ਵਿੰਡੋਜ਼ ਦੌਰਾਨ, ਕੈਮਰਾ WiFi ਫ੍ਰੇਮ ਪ੍ਰਸਾਰਿਤ ਕਰਦਾ ਹੈ ਜਿਨ੍ਹਾਂ ਵਿੱਚ ਇਸਦਾ **MAC ਪਤਾ** ਹੁੰਦਾ ਹੈ — ਅਤੇ ਹਰੇਕ MAC ਪਤੇ ਦੇ ਪਹਿਲੇ ਤਿੰਨ ਬਾਈਟ ਨਿਰਮਾਤਾ ਦੀ ਪਛਾਣ ਕਰਦੇ ਹਨ। ਇਹ **OUI (ਸੰਗਠਨਾਤਮਕ ਤੌਰ 'ਤੇ ਵਿਲੱਖਣ ਪਛਾਣਕਰਤਾ)** ਹੈ।

ਸੁਰੱਖਿਆ ਖੋਜਕਰਤਾ **@NitekryDPaul** ਨੇ **promiscuous-mode 2.4 GHz ਵਿਸ਼ਲੇਸ਼ਣ** ਰਾਹੀਂ Flock Safety ਕੈਮਰਾ ਹਾਰਡਵੇਅਰ ਨਾਲ ਲਗਾਤਾਰ ਜੁੜੇ **30 OUI ਪ੍ਰੀਫਿਕਸ** ਲੱਭੇ। Joplin, MO ਵਿੱਚ ਫੀਲਡ ਟੈਸਟਿੰਗ ਦੌਰਾਨ **Michael / DeFlockJoplin** ਨੇ 31ਵਾਂ ਪ੍ਰੀਫਿਕਸ (`82:6B:F2`) ਯੋਗਦਾਨ ਦਿੱਤਾ।

Flock Finder ਉਹ 31 OUI ਲੈਂਦਾ ਹੈ, WiGLE ਨੂੰ ਉਹਨਾਂ ਪ੍ਰੀਫਿਕਸਾਂ ਨਾਲ ਮੇਲ ਖਾਂਦੇ ਕਿਸੇ ਵੀ ਰਿਕਾਰਡ ਕੀਤੇ WiFi ਨੈੱਟਵਰਕ ਲਈ ਪੁੱਛਦਾ ਹੈ, ਅਤੇ ਨਤੀਜਿਆਂ ਨੂੰ ਇੱਕ ਨਕਸ਼ੇ 'ਤੇ ਪਲਾਟ ਕਰਦਾ ਹੈ।

### Flock Safety ਦੇ 31 ਜਾਣੇ-ਪਛਾਣੇ OUI ਪ੍ਰੀਫਿਕਸ

| # | OUI ਪ੍ਰੀਫਿਕਸ | ਸਰੋਤ | # | OUI ਪ੍ਰੀਫਿਕਸ | ਸਰੋਤ |
|---|-----------|--------|---|-----------|--------|
| 1 | **70:C9:4E** | @NitekryDPaul | 17 | **D0:39:57** | @NitekryDPaul |
| 2 | **3C:91:80** | @NitekryDPaul | 18 | **E8:D0:FC** | @NitekryDPaul |
| 3 | **D8:F3:BC** | @NitekryDPaul | 19 | **E0:4F:43** | @NitekryDPaul |
| 4 | **80:30:49** | @NitekryDPaul | 20 | **B8:1E:A4** | @NitekryDPaul |
| 5 | **B8:35:32** | @NitekryDPaul | 21 | **70:08:94** | @NitekryDPaul |
| 6 | **14:5A:FC** | @NitekryDPaul | 22 | **58:8E:81** | @NitekryDPaul |
| 7 | **74:4C:A1** | @NitekryDPaul | 23 | **EC:1B:BD** | @NitekryDPaul |
| 8 | **08:3A:88** | @NitekryDPaul | 24 | **3C:71:BF** | @NitekryDPaul |
| 9 | **9C:2F:9D** | @NitekryDPaul | 25 | **58:00:E3** | @NitekryDPaul |
| 10 | **C0:35:32** | @NitekryDPaul | 26 | **90:35:EA** | @NitekryDPaul |
| 11 | **94:08:53** | @NitekryDPaul | 27 | **5C:93:A2** | @NitekryDPaul |
| 12 | **E4:AA:EA** | @NitekryDPaul | 28 | **64:6E:69** | @NitekryDPaul |
| 13 | **F4:6A:DD** | @NitekryDPaul | 29 | **48:27:EA** | @NitekryDPaul |
| 14 | **F8:A2:D6** | @NitekryDPaul | 30 | **A4:CF:12** | @NitekryDPaul |
| 15 | **24:B2:B9** | @NitekryDPaul | 31 | **82:6B:F2** | DeFlockJoplin |
| 16 | **00:F4:8D** | @NitekryDPaul | | | |

### addr1 ਖੋਜ ਤਕਨੀਕ

@NitekryDPaul ਦੀ ਮੁੱਖ ਖੋਜ ਟ੍ਰਾਂਸਮੀਟਰ MAC ਪਤੇ 'ਤੇ ਸਧਾਰਨ ਮੇਲ ਤੋਂ ਪਰੇ ਜਾਂਦੀ ਹੈ। Flock ਕੈਮਰੇ ਆਪਣੇ ਡਿਊਟੀ ਸਾਈਕਲ ਦਾ ਜ਼ਿਆਦਾਤਰ ਸਮਾਂ **ਸੁੱਤੇ** ਬਿਤਾਉਂਦੇ ਹਨ। ਜਦੋਂ ਇੱਕ ਨੇੜਲਾ ਐਕਸੈਸ ਪੁਆਇੰਟ ਕੈਮਰੇ ਨੂੰ *ਸੰਬੋਧਿਤ* ਫ੍ਰੇਮ ਭੇਜਦਾ ਹੈ, ਤਾਂ ਕੈਮਰੇ ਦਾ MAC 802.11 ਫ੍ਰੇਮਾਂ ਵਿੱਚ **addr1 (ਪ੍ਰਾਪਤਕਰਤਾ ਪਤੇ)** ਵਜੋਂ ਦਿਖਾਈ ਦਿੰਦਾ ਹੈ — ਭਾਵੇਂ ਕੈਮਰਾ ਆਪ ਸਰਗਰਮੀ ਨਾਲ ਪ੍ਰਸਾਰਿਤ ਨਹੀਂ ਕਰ ਰਿਹਾ।

**wildcard probe ਬੇਨਤੀ ਖੋਜ** (802.11 ਪ੍ਰਬੰਧਨ ਫ੍ਰੇਮ type=0, subtype=4, ਖਾਲੀ SSID) ਦੇ ਨਾਲ ਮਿਲ ਕੇ, ਇਹ ਇੱਕ ਬਹੁਤ ਸਟੀਕ ਖੋਜ ਦਸਤਖਤ ਦਿੰਦਾ ਹੈ। Joplin, MO ਵਿੱਚ ਫੀਲਡ ਟੈਸਟਿੰਗ ਨੇ **ਸਿਰਫ 2 ਝੂਠੇ ਸਕਾਰਾਤਮਕ ਨਾਲ 12 ਵਿੱਚੋਂ 11 ਕੈਮਰੇ ਖੋਜੇ**।

> ⚠️ **ਮਹੱਤਵਪੂਰਨ**: WiGLE-ਆਧਾਰਿਤ Flock Finder ਨਕਸ਼ਾ addr1 ਤਕਨੀਕ ਨੂੰ **ਲਾਗੂ ਨਹੀਂ ਕਰਦਾ**। WiGLE ਇੱਕ ਇਤਿਹਾਸਕ, ਪੈਸਿਵ ਤੌਰ 'ਤੇ ਇਕੱਠਾ ਕੀਤਾ ਡੇਟਾਸੈੱਟ ਹੈ — ਇਹ ਸਿਰਫ ਟ੍ਰਾਂਸਮੀਟਰ ਰਿਕਾਰਡ ਕਰਦਾ ਹੈ, ਪ੍ਰਾਪਤਕਰਤਾ ਨਹੀਂ। @NitekryDPaul ਦੀ ਅਸਲ ਵਿਧੀ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਰੀਅਲ-ਟਾਈਮ ਖੋਜ ਲਈ, ਤੁਹਾਨੂੰ ਫੀਲਡ ਵਿੱਚ ਚੱਲ ਰਹੇ ਸਮਰਪਿਤ ਹਾਰਡਵੇਅਰ ਦੀ ਲੋੜ ਹੈ।

______

## ਲਾਈਵ ਨਕਸ਼ੇ ਦੀ ਵਰਤੋਂ ਕਰਨਾ

ਇੰਟਰੈਕਟਿਵ ਨਕਸ਼ਾ **[simeononsecurity.github.io/flock-finder/](https://simeononsecurity.github.io/flock-finder/)** 'ਤੇ ਲਾਈਵ ਹੈ। ਇਹ ਦਿਖਾਉਂਦਾ ਹੈ:

- **ਕਲੱਸਟਰਡ ਕੈਮਰਾ ਮਾਰਕਰ** OUI ਪ੍ਰੀਫਿਕਸ ਦੁਆਰਾ ਰੰਗ-ਕੋਡਡ
- **ਖੋਜ** ਸ਼ਹਿਰ, ਰਾਜ, ਜਾਂ BSSID ਦੁਆਰਾ
- **OUI ਡੇਟਾ ਸਾਰਣੀ** ਪ੍ਰਤੀ-ਪ੍ਰੀਫਿਕਸ ਕੈਮਰਾ ਗਿਣਤੀ ਦੇ ਨਾਲ
- **ਅੰਕੜਾ ਪੈਨਲ** ਕੁੱਲ ਕੈਮਰੇ, ਖੇਤਰ ਅਤੇ ਆਖਰੀ ਅੱਪਡੇਟ ਟਾਈਮਸਟੈਂਪ ਦਿਖਾਉਂਦਾ ਹੈ
- **ALPR ਬਾਰੇ ਪੇਜ** ਦਸਤਾਵੇਜ਼ੀ ਗੋਪਨੀਯਤਾ ਨੁਕਸਾਨ, ਕਾਨੂੰਨੀ ਸੰਦਰਭ ਅਤੇ ਕਮਿਊਨਿਟੀ ਸਰੋਤਾਂ ਦੇ ਨਾਲ

ਨਕਸ਼ਾ ਡੇਟਾ ਐਕਸਪੋਰਟ ਵੀ ਸਿੱਧੇ ਉਪਲਬਧ ਹਨ:

- `data/flock_cameras.geojson` — QGIS, Leaflet, ਜਾਂ ਹੋਰ ਟੂਲਾਂ ਵਿੱਚ ਵਰਤੋਂ ਲਈ GeoJSON
- `data/flock_cameras.csv` — ਸਪ੍ਰੈਡਸ਼ੀਟ-ਅਨੁਕੂਲ ਫਾਰਮੈਟ
- `data/scan_stats.json` — ਸਕੈਨ ਅੰਕੜੇ ਅਤੇ ਗਿਣਤੀ

### ਮੁੱਖ ਸੀਮਾਵਾਂ

**ਨਕਸ਼ੇ ਨੂੰ ਸਾਵਧਾਨੀ ਨਾਲ ਲਓ।** WiGLE ਇੱਕ ਕ੍ਰਾਊਡਸੋਰਸਡ, ਅਨਿਯਮਿਤ ਰੂਪ ਨਾਲ ਅੱਪਡੇਟ ਕੀਤਾ ਡੇਟਾਸੈੱਟ ਹੈ, ਲਾਈਵ ਫੀਡ ਨਹੀਂ।

- **Flock ਕੈਮਰੇ ਲਗਾਤਾਰ ਪ੍ਰਸਾਰਿਤ ਨਹੀਂ ਕਰਦੇ।** ਡੇਟਾ ਅੱਪਲੋਡ ਕਰਨ ਲਈ ਸੰਖੇਪ ਵਿੱਚ ਜਾਗਦੇ ਹਨ, ਇਸ ਲਈ WiGLE ਰਿਕਾਰਡ ਪੂਰੀ ਤਰ੍ਹਾਂ ਸਹੀ ਸਮੇਂ 'ਤੇ ਨੇੜੇ ਇੱਕ wardriver ਹੋਣ 'ਤੇ ਨਿਰਭਰ ਕਰਦੇ ਹਨ।
- **ਡੇਟਾ ਮਹੀਨਿਆਂ ਜਾਂ ਸਾਲਾਂ ਪੁਰਾਣਾ ਹੋ ਸਕਦਾ ਹੈ।** ਤਬਦੀਲ ਜਾਂ ਹਟਾਏ ਗਏ ਕੈਮਰੇ ਅਜੇ ਵੀ ਦਿਖਾਈ ਦੇ ਸਕਦੇ ਹਨ।
- **OUI ਮਿਲਾਨ ਇੱਕ ਅਨੁਮਾਨੀ ਹੈ।** OUI ਸਾਂਝੇ ਕੀਤੇ ਜਾ ਸਕਦੇ ਹਨ, ਮੁੜ ਨਿਰਧਾਰਿਤ ਕੀਤੇ ਜਾ ਸਕਦੇ ਹਨ, ਜਾਂ ਸਪੂਫ ਕੀਤੇ ਜਾ ਸਕਦੇ ਹਨ। ਹਰ ਨਤੀਜਾ ਇੱਕ *ਸ਼ੱਕੀ* Flock ਡਿਵਾਈਸ ਹੈ, ਪੁਸ਼ਟੀ ਨਹੀਂ।
- **ਕਵਰੇਜ ਅਸਮਾਨ ਹੈ।** ਸੰਘਣੇ ਮਹਾਨਗਰੀ ਖੇਤਰਾਂ ਵਿੱਚ ਵਧੇਰੇ WiGLE ਡੇਟਾ ਹੈ; ਪੇਂਡੂ ਖੇਤਰਾਂ ਵਿੱਚ ਬਹੁਤ ਘੱਟ ਹੈ।

*ਆਪਣੇ ਖੇਤਰ ਵਿੱਚ ਨਿਗਰਾਨੀ ਘਣਤਾ ਬਾਰੇ ਆਮ ਜਾਗਰੂਕਤਾ ਵਿਕਸਿਤ ਕਰਨ ਲਈ ਨਕਸ਼ੇ ਦੀ ਵਰਤੋਂ ਕਰੋ। ਜ਼ਮੀਨੀ-ਸੱਚ, ਰੀਅਲ-ਟਾਈਮ ਖੋਜ ਲਈ, ਹੇਠਾਂ ਹਾਰਡਵੇਅਰ ਵਿਕਲਪ ਦੇਖੋ।*

______

## Flock Finder ਆਪ ਚਲਾਉਣਾ

### ਲੋੜਾਂ

- Python 3.8+
- API ਕ੍ਰੈਡੇਨਸ਼ੀਅਲਾਂ ਨਾਲ ਮੁਫ਼ਤ [WiGLE](https://wigle.net/account) ਖਾਤਾ

### ਸੈੱਟਅੱਪ

```bash
# Clone the repository
git clone https://github.com/simeononsecurity/flock-finder.git
cd flock-finder

# Install dependencies
pip install -r requirements.txt

# Set up your WiGLE API credentials
cp .env.example .env
# Edit .env with your WiGLE API Name and Token
```

### ਸਕੈਨਰ ਚਲਾਉਣਾ

```bash
# Full scan — all 31 OUI prefixes, worldwide
python3 scripts/wigle_query.py

# Single OUI test
python3 scripts/wigle_query.py --oui 70:C9:4E

# US only
python3 scripts/wigle_query.py --country US

# Specific bounding box (lat1,lon1,lat2,lon2)
python3 scripts/wigle_query.py --bbox 37,-97,39,-94

# Dry run — verify auth, no API queries
python3 scripts/wigle_query.py --dry-run
```

### ਨਕਸ਼ੇ ਨੂੰ ਸਥਾਨਕ ਤੌਰ 'ਤੇ ਦੇਖਣਾ

```bash
python3 -m http.server 8080 --directory docs/
# Open http://localhost:8080 in your browser
```

### GitHub Actions ਰਾਹੀਂ ਆਟੋਮੇਟਡ ਰੋਜ਼ਾਨਾ ਅੱਪਡੇਟ

ਰਿਪੋ ਫੋਰਕ ਕਰੋ ਅਤੇ ਆਪਣੇ WiGLE ਕ੍ਰੈਡੇਨਸ਼ੀਅਲਾਂ ਨੂੰ **ਰਿਪੋਜ਼ਿਟਰੀ ਸੀਕ੍ਰੇਟਸ** (`WIGLE_API_NAME` ਅਤੇ `WIGLE_API_TOKEN`) ਵਜੋਂ ਜੋੜੋ। ਸ਼ਾਮਲ ਕੀਤਾ ਵਰਕਫਲੋ ਰੋਜ਼ਾਨਾ UTC ਸਵੇਰੇ 6 ਵਜੇ ਚੱਲਦਾ ਹੈ ਅਤੇ ਨਵੇਂ ਕੈਮਰੇ ਮਿਲਣ 'ਤੇ ਆਟੋਮੈਟਿਕ ਅੱਪਡੇਟ ਕੀਤੀਆਂ ਡੇਟਾ ਫਾਈਲਾਂ ਕਮਿੱਟ ਕਰਦਾ ਹੈ।

______

## ਰੀਅਲ-ਟਾਈਮ ਖੋਜ: STS Collective FlockYou ਹਾਰਡਵੇਅਰ

WiGLE ਨਕਸ਼ਾ ਤੁਹਾਨੂੰ ਦੱਸਦਾ ਹੈ ਕਿ ਕੈਮਰੇ *ਕਿੱਥੇ ਦੇਖੇ ਗਏ ਹਨ*। ਗੱਡੀ ਚਲਾਉਂਦੇ ਸਮੇਂ ਰੀਅਲ-ਟਾਈਮ ਖੋਜ ਲਈ — ਲਾਈਵ WiFi ਟ੍ਰੈਫਿਕ 'ਤੇ @NitekryDPaul ਦੀ ਅਸਲ OUI ਮਿਲਾਨ ਵਿਧੀ ਦੀ ਵਰਤੋਂ ਕਰਕੇ — ਤੁਹਾਨੂੰ ਸਮਰਪਿਤ ਹਾਰਡਵੇਅਰ ਦੀ ਲੋੜ ਹੈ।

**[STS Collective](https://stscollective.com/discount/SIMEONONSECURITY)** ਪੋਰਟੇਬਲ ESP32-ਆਧਾਰਿਤ ਡਿਟੈਕਟਰ ਬਣਾਉਂਦਾ ਹੈ ਜੋ Flock OUI ਦਸਤਖਤਾਂ ਲਈ ਸਕੈਨ ਕਰਦੇ ਹਨ ਅਤੇ ਮੇਲ ਖਾਂਦੇ ਦਸਤਖਤ ਦਾ ਪਤਾ ਲੱਗਣ ਦੇ ਪਲ ਤੁਹਾਨੂੰ ਸੁਚੇਤ ਕਰਦੇ ਹਨ।

### FlockYou ਡਿਵਾਈਸ ਲਾਈਨਅੱਪ

| ਡਿਵਾਈਸ | ਵੇਰਵਾ |
|--------|-------------|
| **[FlockYou — M5 Atom Lite](https://stscollective.com/products/flockyou-m5-atom-lite-flock-camera-detector)** | ਕੰਪੈਕਟ, ਜੇਬ ਆਕਾਰ ਦਾ Flock ਡਿਟੈਕਟਰ। ਪ੍ਰੀ-ਫਲੈਸ਼ਡ, ਪਲੱਗ-ਐਂਡ-ਪਲੇ। ਖੋਜ 'ਤੇ LED ਚੇਤਾਵਨੀਆਂ। |
| **FlockYou Pro — LED + Audio** | LED ਸੂਚਕਾਂ ਦੇ ਨਾਲ ਆਡੀਓ ਚੇਤਾਵਨੀਆਂ ਜੋੜਦਾ ਹੈ। ਗੱਡੀ ਚਲਾਉਂਦੇ ਸਮੇਂ ਕੋਈ ਕੈਮਰਾ ਨਾ ਖੁੰਝਾਓ। |
| **FlockYou Atom VoiceS3R** | ਹੈਂਡਸ-ਫ੍ਰੀ, ਸੜਕ 'ਤੇ ਨਜ਼ਰ ਰੱਖਣ ਵਾਲੀ ਆਪਰੇਸ਼ਨ ਲਈ ਬੋਲੇ ਗਏ ਆਡੀਓ ਚੇਤਾਵਨੀਆਂ ਵਾਲਾ ਵੌਇਸ-ਸਮਰਥਿਤ ਡਿਟੈਕਟਰ। |

ਸਾਰੀਆਂ ਡਿਵਾਈਸਾਂ:
- **ਪ੍ਰੀ-ਫਲੈਸ਼ਡ**, ਬਕਸੇ ਤੋਂ ਬਾਹਰ ਵਰਤੋਂ ਲਈ ਤਿਆਰ
- ਸਾਰੇ 31 ਜਾਣੇ-ਪਛਾਣੇ Flock OUI ਲਈ ਲਾਈਵ WiFi ਟ੍ਰੈਫਿਕ ਸਕੈਨ ਕਰਦੀਆਂ ਹਨ
- ਕੰਪੈਕਟ ਅਤੇ ਪੋਰਟੇਬਲ — ਕੱਪ ਹੋਲਡਰ ਜਾਂ ਜੇਬ ਵਿੱਚ ਫਿੱਟ
- USB-C ਰਾਹੀਂ ਚਲਾਈਆਂ ਜਾਂਦੀਆਂ ਹਨ (ਕਾਰ ਅਡੈਪਟਰ, ਪਾਵਰ ਬੈਂਕ, ਜਾਂ ਲੈਪਟਾਪ)

> 💰 **ਵਿਸ਼ੇਸ਼ ਛੋਟਾਂ**: ਸਾਰੀਆਂ STS Collective FlockYou ਡਿਵਾਈਸਾਂ 'ਤੇ **20% ਛੋਟ** ਲਈ ਕੋਡ **FLOCKFINDER** ਵਰਤੋ — ਜਾਂ ਆਪਣੇ ਪੂਰੇ ਆਰਡਰ 'ਤੇ 20% ਤੱਕ ਛੋਟ ਲਈ ਕੋਡ **SIMEONONSECURITY** ਵਰਤੋ। [stscollective.com/discount/SIMEONONSECURITY 'ਤੇ ਖਰੀਦਾਰੀ ਕਰੋ](https://stscollective.com/discount/SIMEONONSECURITY)।

ਇਹਨਾਂ ਡਿਵਾਈਸਾਂ ਅਤੇ DIY ਵਿਕਲਪਾਂ ਦੇ ਪੂਰੇ ਤਕਨੀਕੀ ਵਿਸ਼ਲੇਸ਼ਣ ਲਈ ਪੜ੍ਹੋ **[Flock-You ਖੋਜ ਪ੍ਰੋਜੈਕਟ: ਪੂਰਾ ਜਵਾਬੀ ਨਿਗਰਾਨੀ ਹਾਰਡਵੇਅਰ ਅਤੇ ਸੈੱਟਅੱਪ ਗਾਈਡ](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/)**।

______

## ਪ੍ਰੋਜੈਕਟ ਢਾਂਚਾ

```
flock-finder/
├── scripts/
│   └── wigle_query.py        # WiGLE API query and data pipeline
├── data/
│   ├── flock_ouis.csv         # 31 known Flock Safety OUI prefixes
│   ├── flock_cameras.geojson  # Camera locations (GeoJSON)
│   ├── flock_cameras.csv      # Camera locations (CSV)
│   └── scan_stats.json        # Scan statistics
├── docs/
│   └── index.html             # Interactive Leaflet map
└── .github/workflows/
    └── update-data.yml        # Daily auto-update workflow
```

______

## ਅਕਸਰ ਪੁੱਛੇ ਜਾਂਦੇ ਸਵਾਲ

### ਕੀ ਇਹ ਕਾਨੂੰਨੀ ਹੈ?

ਹਾਂ। **Flock Finder ਸਿਰਫ WiGLE ਡੇਟਾਬੇਸ ਤੋਂ ਜਨਤਕ ਤੌਰ 'ਤੇ ਉਪਲਬਧ ਡੇਟਾ ਦੀ ਵਰਤੋਂ ਕਰਦਾ ਹੈ**, ਜੋ ਸਵੈਇੱਛਕ ਰੂਪ ਨਾਲ ਯੋਗਦਾਨ ਕੀਤੇ WiFi ਸਰਵੇਖਣ ਡੇਟਾ ਨੂੰ ਇਕੱਠਾ ਕਰਦਾ ਹੈ। ਕੋਈ ਹੈਕਿੰਗ, ਅਣਅਧਿਕਾਰਤ ਪਹੁੰਚ, ਜਾਂ ਮਲਕੀਅਤ ਪ੍ਰਣਾਲੀਆਂ ਸ਼ਾਮਲ ਨਹੀਂ ਹਨ। OUI ਦਸਤਖਤਾਂ ਲਈ ਪੈਸਿਵ WiFi ਨਿਗਰਾਨੀ ਸੰਯੁਕਤ ਰਾਜ ਅਮਰੀਕਾ ਵਿੱਚ ਕਾਨੂੰਨੀ ਹੈ।

### ਕੀ ਹਰ ਨਕਸ਼ੇ 'ਤੇ ਦਿੱਤਾ ਕੈਮਰਾ ਯਕੀਨੀ ਤੌਰ 'ਤੇ Flock ਕੈਮਰਾ ਹੈ?

ਨਹੀਂ। OUI ਮਿਲਾਨ ਇੱਕ **ਅਨੁਮਾਨੀ** ਹੈ। OUI ਪ੍ਰੀਫਿਕਸ ਨਿਰਮਾਤਾਵਾਂ ਵਿੱਚ ਸਾਂਝੇ, ਮੁੜ ਨਿਰਧਾਰਿਤ, ਜਾਂ ਸਪੂਫ ਕੀਤੇ ਜਾ ਸਕਦੇ ਹਨ। ਡੇਟਾਬੇਸ ਵਿੱਚ ਹਰ ਰਿਕਾਰਡ ਇੱਕ *ਸ਼ੱਕੀ* Flock ਡਿਵਾਈਸ ਹੈ — ਪੁਸ਼ਟੀ ਨਹੀਂ। ਸੁਧਾਰ ਬੇਨਤੀ ਕਿਵੇਂ ਕਰਨੀ ਹੈ ਬਾਰੇ ਜਾਣਕਾਰੀ ਲਈ [ਡੇਟਾ ਨੀਤੀ](https://github.com/simeononsecurity/flock-finder/blob/main/docs/data-policy.md) ਪੜ੍ਹੋ।

### ਕੁਝ OUI ਪ੍ਰੀਫਿਕਸ ਕੋਈ ਕੈਮਰੇ ਕਿਉਂ ਨਹੀਂ ਦਿਖਾਉਂਦੇ?

WiGLE ਕਵਰੇਜ ਅਸਮਾਨ ਹੈ। ਜੇ ਕਿਸੇ wardriver ਨੇ ਉਸ ਖਾਸ OUI ਦੇ ਸਰਗਰਮ ਹੋਣ ਨਾਲ ਕਿਸੇ ਖੇਤਰ ਨੂੰ ਸਕੈਨ ਨਹੀਂ ਕੀਤਾ, ਤਾਂ ਕੋਈ ਰਿਕਾਰਡ ਨਹੀਂ ਹੋਣਗੇ। *ਡੇਟਾ ਦੀ ਅਣਹੋਂਦ ਦਾ ਮਤਲਬ ਕੈਮਰਿਆਂ ਦੀ ਅਣਹੋਂਦ ਨਹੀਂ ਹੈ।*

### ਡੇਟਾ ਕਿੰਨਾ ਮੌਜੂਦਾ ਹੈ?

GitHub Actions ਵਰਕਫਲੋ ਰੋਜ਼ਾਨਾ ਚੱਲਦਾ ਹੈ ਅਤੇ ਨਵੀਨਤਮ WiGLE ਨਤੀਜੇ ਖਿੱਚਦਾ ਹੈ। ਹਾਲਾਂਕਿ, WiGLE ਆਪ ਕਿਸੇ ਖਾਸ ਸਥਾਨ ਲਈ ਦਿਨਾਂ ਤੋਂ ਲੈ ਕੇ ਸਾਲਾਂ ਪੁਰਾਣੇ ਰਿਕਾਰਡ ਰੱਖ ਸਕਦਾ ਹੈ। ਸਭ ਤੋਂ ਹਾਲੀਆ ਸਕੈਨ ਦੇ ਟਾਈਮਸਟੈਂਪ ਲਈ `scan_stats.json` ਫਾਈਲ ਜਾਂਚੋ।

### ਕੀ ਮੈਂ ਆਪਣਾ wardrive ਡੇਟਾ ਯੋਗਦਾਨ ਕਰ ਸਕਦਾ ਹਾਂ?

ਹਾਂ। ਆਪਣਾ wardrive ਡੇਟਾ [WiGLE](https://wigle.net) 'ਤੇ ਅੱਪਲੋਡ ਕਰੋ — ਇਹ ਆਟੋਮੈਟਿਕ Flock Finder ਦੇ ਅਗਲੇ ਰੋਜ਼ਾਨਾ ਸਕੈਨ ਵਿੱਚ ਸ਼ਾਮਲ ਹੋ ਜਾਂਦਾ ਹੈ। ਤੁਸੀਂ [ਯੋਗਦਾਨ ਗਾਈਡ](https://github.com/simeononsecurity/flock-finder/blob/main/CONTRIBUTING.md) ਰਾਹੀਂ OUI ਪ੍ਰੀਫਿਕਸ ਜਾਂ ਕੋਡ ਸੁਧਾਰ ਵੀ ਯੋਗਦਾਨ ਕਰ ਸਕਦੇ ਹੋ।

______

## ਕਮਿਊਨਿਟੀ ਅਤੇ ਸੰਬੰਧਿਤ ਪ੍ਰੋਜੈਕਟ

Flock Finder ਇਕੱਲਾ ਨਹੀਂ ਖੜ੍ਹਾ। ALPR ਨਿਗਰਾਨੀ ਨੂੰ ਦਸਤਾਵੇਜ਼ ਅਤੇ ਇਸਦਾ ਮੁਕਾਬਲਾ ਕਰਨ ਲਈ ਟੂਲਾਂ ਅਤੇ ਸੰਗਠਨਾਂ ਦਾ ਇੱਕ ਵਧ ਰਿਹਾ ਈਕੋਸਿਸਟਮ ਕੰਮ ਕਰ ਰਿਹਾ ਹੈ:

- **[DeFlock.org](https://deflockjoplin.org/)** — ਕਮਿਊਨਿਟੀ-ਚਾਲਿਤ ALPR ਟ੍ਰੈਕਿੰਗ, ਦਸਤਾਵੇਜ਼ੀਕਰਨ ਅਤੇ ਵਕਾਲਤ
- **[Have I Been Flocked?](https://haveibeenflocked.com/)** — ਜਾਂਚੋ ਕਿ ਕੀ ਤੁਹਾਡੀ ਪਲੇਟ Flock ਦੇ ਸਿਸਟਮ ਵਿੱਚ ਖੋਜੀ ਗਈ ਹੈ
- **[FlockHopper](https://flockhopper.com/)** — ਜਾਣੇ-ਪਛਾਣੇ ALPR ਕੈਮਰਿਆਂ ਤੋਂ ਬਚਦੇ ਹੋਏ ਰੂਟ ਯੋਜਨਾਬੰਦੀ
- **[Atlas of Surveillance (EFF)](https://atlasofsurveillance.org/)** — ਕਾਨੂੰਨ ਲਾਗੂਕਰਨ ਦੁਆਰਾ ਵਰਤੀ ਜਾਂਦੀ ਨਿਗਰਾਨੀ ਤਕਨੀਕ ਦਾ EFF ਦਾ ਡੇਟਾਬੇਸ
- **[NoALPRs.com](https://noalprs.com/)** — ALPR ਤਾਇਨਾਤੀਆਂ ਦੇ ਵਿਰੁੱਧ ਲੜਨ ਵਾਲੀਆਂ ਕਮਿਊਨਿਟੀਆਂ ਲਈ ਸਰੋਤ
- **[DeFlockJoplin](https://deflockjoplin.org/)** — ਓਪਨ-ਸੋਰਸ ਫਰਮਵੇਅਰ ਅਤੇ ਫੀਲਡ ਖੋਜ; 31ਵਾਂ OUI ਪ੍ਰੀਫਿਕਸ ਯੋਗਦਾਨ ਦਿੱਤਾ

______

## ਕ੍ਰੈਡਿਟ

- **OUI ਖੋਜ**: @NitekryDPaul — ਸਾਰੇ 30 ਅਸਲ OUI ਪ੍ਰੀਫਿਕਸ ਅਤੇ addr1/promiscuous-mode ਖੋਜ ਰਣਨੀਤੀ
- **ਫੀਲਡ ਟੈਸਟਿੰਗ**: Michael / DeFlockJoplin — 31ਵਾਂ OUI ਪ੍ਰੀਫਿਕਸ (`82:6B:F2`) ਅਤੇ wildcard probe ਤੰਗ ਕਰਨਾ
- **ਡੇਟਾ ਸਰੋਤ**: [WiGLE](https://wigle.net) — ਕ੍ਰਾਊਡਸੋਰਸਡ WiFi/ਸੈੱਲ ਨੈੱਟਵਰਕ ਡੇਟਾਬੇਸ
- **ਪ੍ਰੇਰਿਤ**: [DeFlock](https://deflockjoplin.org/) ਅਤੇ track-openroaming-passpoint ਤੋਂ
- **ਹਾਰਡਵੇਅਰ ਭਾਈਵਾਲ**: [STS Collective](https://stscollective.com/discount/SIMEONONSECURITY) — FlockYou ESP32 ਡਿਟੈਕਟਰ

______

## ਸਿੱਟਾ

**Flock Finder** ਕਿਸੇ ਨੂੰ ਵੀ Flock Safety ALPR ਕੈਮਰਿਆਂ ਦੀ ਤਾਇਨਾਤੀ ਦੇ ਪੈਮਾਨੇ ਦੀ ਇੱਕ ਤੇਜ਼, ਦ੍ਰਿਸ਼ਟੀਗਤ ਸਮਝ ਦਿੰਦਾ ਹੈ — 109 ਦੇਸ਼ਾਂ ਵਿੱਚ 40,000+ ਅਨੁਮਾਨਿਤ ਸਥਾਨ, ਕ੍ਰਾਊਡਸੋਰਸਡ WiFi ਡੇਟਾ ਤੋਂ ਹਰ ਦਿਨ ਆਟੋਮੈਟਿਕ ਅੱਪਡੇਟ ਹੁੰਦੇ ਹਨ।

ਇਹ ਇੱਕ **ਪਾਰਦਰਸ਼ਿਤਾ ਟੂਲ** ਹੈ, ਲਾਈਵ ਟ੍ਰੈਕਰ ਨਹੀਂ। ਇਸਦਾ ਡੇਟਾ ਇਤਿਹਾਸਕ, ਅਧੂਰਾ ਅਤੇ ਸੰਭਾਵਿਕ ਹੈ। ਪਰ ਇਹ ALPR ਨਿਗਰਾਨੀ ਦੇ ਪੈਮਾਨੇ ਨੂੰ ਉਸ ਤਰੀਕੇ ਨਾਲ ਦ੍ਰਿਸ਼ਟੀਮਾਨ ਬਣਾਉਂਦਾ ਹੈ ਜੋ ਸੰਖੇਪ ਅਤੇ ਰਿਪੋਰਟਾਂ ਨਹੀਂ ਕਰ ਸਕਦੀਆਂ।

ਨਿਗਰਾਨੀ ਵਾਲੇ ਖੇਤਰਾਂ ਵਿੱਚੋਂ ਲੰਘਦੇ ਸਮੇਂ ਅਸਲ ਰੀਅਲ-ਟਾਈਮ ਸੁਰੱਖਿਆ ਲਈ, ਨਕਸ਼ੇ ਨੂੰ ਸਮਰਪਿਤ ਹਾਰਡਵੇਅਰ ਨਾਲ ਜੋੜੋ। **[STS Collective ਦੀਆਂ FlockYou ਡਿਵਾਈਸਾਂ](https://stscollective.com/discount/SIMEONONSECURITY)** @NitekryDPaul ਦੀ ਖੋਜ ਵਿਧੀ ਨੂੰ ਸਿੱਧੇ ESP32 'ਤੇ ਲਾਗੂ ਕਰਦੀਆਂ ਹਨ ਅਤੇ ਲਾਈਵ ਕੈਮਰਾ ਦਸਤਖਤ ਦਾ ਪਤਾ ਲੱਗਣ ਦੇ ਪਲ ਤੁਹਾਨੂੰ ਸੁਚੇਤ ਕਰਦੀਆਂ ਹਨ — **[stscollective.com](https://stscollective.com/discount/SIMEONONSECURITY)** 'ਤੇ ਕੋਡ **FLOCKFINDER** ਜਾਂ **SIMEONONSECURITY** ਨਾਲ 20% ਤੱਕ ਛੋਟ 'ਤੇ ਉਪਲਬਧ।

### ਸੰਬੰਧਿਤ ਲੇਖ

| ਲੇਖ | ਕੀ ਕਵਰ ਕਰਦਾ ਹੈ |
|---------|---------------|
| **[Flock Safety ਕੈਮਰਾ ਨਿਗਰਾਨੀ: ਗੋਪਨੀਯਤਾ ਅਤੇ ਸੁਰੱਖਿਆ](/articles/flock-safety-camera-surveillance-prevalence-privacy-protection-2026/)** | ਪੂਰੀ ਤਸਵੀਰ: ਪ੍ਰਸਾਰ ਅੰਕੜੇ, ਨਾਗਰਿਕ ਸੁਤੰਤਰਤਾ ਮੁੱਦੇ, ACLU ਟੂਲਕਿੱਟ, DeFlock ਅੰਕੜੇ, FOIA ਗਾਈਡ ਅਤੇ ਸੁਰੱਖਿਆ ਰਣਨੀਤੀਆਂ |
| **[Flock-You ਖੋਜ ਪ੍ਰੋਜੈਕਟ: ਜਵਾਬੀ ਨਿਗਰਾਨੀ ਹਾਰਡਵੇਅਰ ਗਾਈਡ](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/)** | ESP32-ਆਧਾਰਿਤ Flock ਡਿਟੈਕਟਰਾਂ ਲਈ ਪੂਰਾ ਤਕਨੀਕੀ ਗਾਈਡ — OUI-SPY, M5 Atom Lite, DIY ਬਿਲਡ, ਕਦਮ-ਦਰ-ਕਦਮ ਫਰਮਵੇਅਰ ਸੈੱਟਅੱਪ |
| **[Rayhunter ਡਿਵਾਈਸਾਂ ਕਿਵੇਂ ਫਲੈਸ਼ ਕਰੀਏ: ਪੂਰੀ ਗਾਈਡ](/articles/how-to-flash-rayhunter-devices-complete-guide/)** | ਪੂਰੀ ਜਵਾਬੀ ਨਿਗਰਾਨੀ ਜਾਗਰੂਕਤਾ ਲਈ ALPR ਕੈਮਰਿਆਂ ਦੇ ਨਾਲ IMSI ਕੈਚਰ (ਸੈੱਲ-ਸਾਈਟ ਸਿਮੂਲੇਟਰ) ਦਾ ਪਤਾ ਲਗਾਓ |
| **[Orbic RCL400 ਲਈ DagShell ਕਸਟਮ ਫਰਮਵੇਅਰ](/articles/dagshell-orbic-rcl400-custom-firmware-guide-2026/)** | ਮੋਬਾਈਲ ਹੌਟਸਪੌਟ ਨੂੰ ਸੁਰੱਖਿਆ ਖੋਜ ਪਲੇਟਫਾਰਮ ਵਿੱਚ ਬਦਲੋ — Flock ਖੋਜ ਹਾਰਡਵੇਅਰ ਨਾਲ ਵਧੀਆ ਜੁੜਦਾ ਹੈ |
| **[Rayhunter ਡਿਵਾਈਸ ਤੁਲਨਾ 2026](/articles/rayhunter-device-comparison-2026-complete-review/)** | ALPR ਅਤੇ ਸੈਲੂਲਰ ਨਿਗਰਾਨੀ ਖਤਰੇ ਸ਼੍ਰੇਣੀਆਂ ਵਿੱਚ ਖੋਜ ਹਾਰਡਵੇਅਰ ਵਿਕਲਪਾਂ ਦੀ ਤੁਲਨਾ ਕਰੋ |

______

## ਹਵਾਲੇ

1. [Flock Finder GitHub ਰਿਪੋਜ਼ਿਟਰੀ](https://github.com/simeononsecurity/flock-finder)
2. [Flock Finder ਇੰਟਰੈਕਟਿਵ ਨਕਸ਼ਾ](https://simeononsecurity.github.io/flock-finder/)
3. [STS Collective — FlockYou ਡਿਵਾਈਸਾਂ](https://stscollective.com/discount/SIMEONONSECURITY)
4. [WiGLE — ਵਾਇਰਲੈੱਸ ਨੈੱਟਵਰਕ ਮੈਪਿੰਗ](https://wigle.net)
5. [DeFlock — ਕਮਿਊਨਿਟੀ ALPR ਜਾਗਰੂਕਤਾ](https://deflockjoplin.org/)
6. [DeFlockJoplin — ਓਪਨ-ਸੋਰਸ ਖੋਜ ਫਰਮਵੇਅਰ](https://deflockjoplin.org/)
7. [Electronic Frontier Foundation — ALPR](https://www.eff.org/issues/automated-license-plate-readers)
8. [ACLU — ਤੁਹਾਨੂੰ ਟ੍ਰੈਕ ਕੀਤਾ ਜਾ ਰਿਹਾ ਹੈ](https://www.aclu.org/issues/privacy-technology/location-tracking/you-are-being-tracked)
