---
title: "ESP32 WiFi Canary : Détection passive des menaces 2,4 GHz avec alertes LED RGB"
date: 2026-06-06
toc: true
draft: false
description: "Une analyse détaillée du projet ESP32 WiFi Canary - un capteur de surveillance compact et passif 2,4 GHz pour le M5Stack Atom Lite qui surveille silencieusement les AP Evil Twin, les attaques de désauthentification, les rétrogradations de sécurité et les floods de balises avec un modèle de menace à score de confiance et une seule LED RGB."
genre: ["Sécurité réseau", "Sécurité WiFi", "Sécurité IoT", "Recherche en sécurité", "Systèmes embarqués", "Outils de confidentialité", "Projets ESP32", "Sécurité matérielle", "Sécurité sans fil", "Sécurité open source"]
tags: ["ESP32", "WiFi Canary", "M5Stack Atom Lite", "Détection Deauth", "Détection Evil Twin", "Sécurité WiFi", "Surveillance WiFi passive", "Trames de gestion 802.11", "Sécurité réseau", "Sécurité IoT", "NeoPixel", "SK6812", "PlatformIO", "C++", "Open Source", "Capteur de sécurité", "Détection de menaces sans fil", "Surveillance BSSID", "Surveillance SSID", "Détection rétrogradation sécurité", "Détection flood de balises", "Surveillance WiFi", "LED RGB", "Mode promiscuité", "Sécurité embarquée", "Sécurité en voyage", "Sécurité WiFi hôtel", "WiFi café", "Sensibilisation à la sécurité", "simeononsecurity"]
canonical: "https://simeononsecurity.com/articles/esp32-wifi-canary-passive-wifi-threat-detection-2026/"
cover: "/img/cover/esp32-wifi-canary-passive-wifi-threat-detection-2026.webp"
coverAlt: "Une illustration d'un petit appareil ressemblant à l'ESP32 WiFi Canary, branché dans un port USB, avec une LED RGB qui brille en différentes couleurs sur fond sombre, symbolisant ses capacités de détection de menaces."
coverCaption: ""
---

**Un capteur WiFi passif de la taille d'un pouce qui ne répond jamais**

## Introduction : Le problème avec le WiFi public

Chaque fois que vous vous connectez au WiFi d'un hôtel, d'un café ou d'un aéroport, vous faites confiance au fait que le point d'accès devant vous est le vrai. Le problème est que les **trames de gestion 802.11** - les trames qui annoncent les réseaux, gèrent les connexions et coordonnent les clients - sont *complètement non authentifiées dans la plupart des déploiements*. N'importe qui avec du matériel modeste peut cloner un SSID, envoyer des trames de désauthentification aux clients, ou placer un leurre ouvert à côté d'un réseau WPA2 légitime.

L'[**ESP32 WiFi Canary**](https://github.com/simeononsecurity/esp32-wifi-canary) est un capteur de surveillance passif qui répond à cette réalité avec la plus petite empreinte possible. Il tient sur le M5Stack Atom Lite, un appareil à peu près de la taille d'un morceau de sucre, se branche dans n'importe quel port USB, apprend l'environnement environnant et allume une LED RGB quand il détecte des schémas cohérents avec des menaces sans fil.

Il ne se connecte à rien. Il ne capture pas d'identifiants. Il ne transmet pas une seule trame. Il observe, évalue et vous dit de quelle couleur est la situation.

Cet article est une référence technique complète pour le projet : ce qu'il détecte, comment fonctionne le modèle de confiance, comment le construire et le flasher, et quelles sont ses limites dans le monde réel.

---

## Ce que fait l'ESP32 WiFi Canary (et ne fait pas)

### Passif uniquement, toujours

Le WiFi Canary fonctionne en deux modes radio, jamais simultanément :

1. **Mode promiscuité** - reçoit et inspecte les trames de gestion 802.11 (désauthentification, désassociation) sans s'associer à aucun réseau
2. **Mode scan** - effectue des scans WiFi actifs pour inventorier les points d'accès à proximité et les comparer à une baseline apprise

L'appareil ne fait jamais :
- S'associer ou se connecter à un réseau
- Capturer des trames de données ou des identifiants
- Transmettre des trames 802.11 de quelque type que ce soit
- Stocker quoi que ce soit dans la flash persistante
- Communiquer sur internet

**Tout ce qu'il apprend est conservé en RAM et réinitialisé au redémarrage.** Cette conception est intentionnelle : le canary est un **capteur**, pas un appareil de capture.

### La LED est l'interface

Il n'y a pas d'écran, pas d'application, pas d'interface web. La seule sortie de l'appareil est un unique **SK6812 RGB NeoPixel** sur GPIO 27 du M5Stack Atom Lite. La LED parle un langage à quatre états :

| État de la LED | Signification |
|---------------|--------------|
| 🔵 Bleu (pulsation lente) | Démarrage - construction de la référence de base |
| 🟢 Vert (fixe) | Normal - aucun problème à haute confiance |
| 🟡 Jaune (fixe) | Attention - schéma suspect détecté |
| 🔴 Rouge (pulsation rapide) | Alerte - menace à plus haute confiance détectée |

Le démarrage prend environ **24 secondes** (3 scans × 8 secondes chacun).

---

## Le processus d'apprentissage de la baseline

### Pourquoi une baseline est importante

Un canary qui se déclenche sur chaque réseau ouvert dans une ville serait inutile. L'ESP32 WiFi Canary résout ce problème en apprenant son environnement avant de commencer à évaluer les menaces.

### Trois scans, 24 secondes

Au démarrage, l'appareil effectue trois scans WiFi séquentiels. Après leur achèvement, l'ensemble appris d'APs, SSID, BSSID, type de chiffrement, intensité du signal, est stocké comme baseline.

---

## Ce qu'il détecte : Catégories de menaces

Le WiFi Canary surveille cinq schémas de menaces distincts.

### 1. Bursts de désauthentification / désassociation

| Condition | Points ajoutés |
|-----------|---------------|
| ≥ 8 trames d'une source en 5 s | +2 |
| ≥ 20 trames d'une source en 5 s | +4 |
| ≥ 5 trames de désauthentification en diffusion | +1 |

### 2. Clone ouvert d'un réseau chiffré connu (Evil Twin)

| Condition | Points ajoutés |
|-----------|---------------|
| Même SSID, était chiffré, maintenant ouvert | +3 |
| BSSID non vu dans la baseline | +1 |
| Signal du clone ≥ 10 dB plus fort que l'AP connu | +1 |

### 3. AP chiffré original manquant + Clone ouvert présent

| Condition | Points ajoutés |
|-----------|---------------|
| AP chiffré de la baseline disparu + réseau ouvert correspondant apparu | +3 |

### 4. Rétrogradation de sécurité

| Condition | Points ajoutés |
|-----------|---------------|
| WPA3 → WPA2 | +1 |
| WPA2 → WPA | +1 |
| Chute de 2+ rangs de chiffrement | +3 |

### 5. SSID dupliqué d'un fournisseur inattendu

| Condition | Points ajoutés |
|-----------|---------------|
| OUI différent de l'AP de la baseline avec le même SSID | +1 |
| Le clone est aussi ≥ 10 dB plus fort | +2 |

### 6. Flood de balises / SSID

| Condition | Points ajoutés |
|-----------|---------------|
| ≥ 15 nouveaux SSID en 30 s | +2 |
| ≥ 30 nouveaux SSID en 30 s | +3 |

---

## Le modèle de score de confiance

Tous les signaux détectés alimentent un unique **score de menace** entier.

| Plage de score | État de la LED |
|----------------|----------------|
| 0–2 | Normal (vert) |
| 3–5 | Attention (jaune) |
| 6+ | Alerte (rouge, pulsation rapide) |

### Décroissance du score

Le score **diminue de 1 point toutes les 60 secondes** sans nouveaux événements déclencheurs.

---

## Construction et flashage

### Prérequis

- **PlatformIO** (CLI ou extension VS Code)
- **M5Stack Atom Lite** (ou tout ESP32 DevKit pour les tests)
- Câble USB-C

### Flasher sur M5Stack Atom Lite

```bash
git clone https://github.com/simeononsecurity/esp32-wifi-canary.git
cd esp32-wifi-canary

# Construire et flasher
pio run -e atom-lite --target upload

# Ouvrir le moniteur série à 115200 bauds
pio device monitor -b 115200
```

### Flasher sur ESP32 DevKit générique

```bash
pio run -e esp32dev --target upload
```

---

## Notes de détection et limites pratiques

### Ce qui peut causer des faux positifs

**Les réseaux d'entreprise et mesh** sont la plus grande source de faux positifs. Un grand déploiement d'entreprise, un hôtel avec de nombreux APs, ou un système mesh peut légitimement montrer plusieurs BSSID pour le même SSID avec différents OUI de fournisseurs.

### Ce qui peut causer des faux négatifs

**Une attaque Evil Twin bien conçue** qui usurpe le BSSID exact de l'AP légitime *peut ne pas accumuler suffisamment de score pour franchir le seuil d'Attention*.

---

## Cas d'utilisation

### Voyager avec des données professionnelles sensibles

Le canary est conçu principalement pour les voyages. Branchez-le dans un port USB d'un ordinateur portable, une prise USB d'un hôtel, ou une batterie portable, et laissez-le apprendre l'environnement.

### Cafés et WiFi public

Les environnements WiFi ouverts sont la surface d'attaque la plus commune pour les configurations Evil Twin.

### Sensibilisation à la sécurité et formation

La sortie série de l'appareil fournit un journal détaillé et lisible par les humains.

---

## Conclusion

L'ESP32 WiFi Canary est un outil ciblé qui fait une chose : surveiller l'environnement 2,4 GHz autour de vous et changer de couleur quand quelque chose semble anormal. Il ne cherche pas à être un système complet de détection d'intrusion sans fil. C'est un canary, un capteur passif dont le travail est de remarquer quand la mine devient dangereuse.

**GitHub** : [github.com/simeononsecurity/esp32-wifi-canary](https://github.com/simeononsecurity/esp32-wifi-canary)
