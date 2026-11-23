---
title: "ESP32 WiFi Canary : détection passive des menaces sur 2,4 GHz"
date: 2026-06-06
lastmod: 2026-11-23
toc: true
draft: false
description: "Présentation technique d'ESP32 WiFi Canary, un capteur passif 2,4 GHz qui détecte les evil twins, la désauthentification, les baisses de sécurité et les inondations de balises."
genre: ["Sécurité réseau", "Sécurité WiFi", "Sécurité IoT", "Recherche en sécurité", "Systèmes embarqués", "Outils de confidentialité", "Projets ESP32", "Sécurité matérielle", "Sécurité sans fil", "Sécurité open source"]
tags: ["ESP32", "WiFi Canary", "M5Stack Atom Lite", "Détection de désauthentification", "Détection d'evil twin", "Sécurité WiFi", "Surveillance passive du WiFi", "Trames de gestion 802.11", "Sécurité réseau", "Sécurité IoT", "NeoPixel", "SK6812", "PlatformIO", "C++", "Logiciel libre", "Capteur de sécurité", "Détection de menaces sans fil", "Surveillance BSSID", "Surveillance SSID", "Détection de baisse de sécurité", "Détection d'inondation de balises", "Surveillance WiFi", "LED RGB", "Mode promiscuous", "Sécurité embarquée", "Sécurité en voyage", "Sécurité WiFi à l'hôtel", "WiFi dans les cafés", "Sensibilisation à la sécurité", "simeononsecurity"]
canonical: "https://simeononsecurity.com/articles/esp32-wifi-canary-passive-wifi-threat-detection-2026/"
cover: "/img/cover/esp32-wifi-canary-passive-wifi-threat-detection-2026.webp"
coverAlt: "Illustration d'un petit appareil ressemblant à ESP32 WiFi Canary, branché sur un port USB. Sa LED RGB s'illumine de différentes couleurs pour représenter ses capacités de détection des menaces."
coverCaption: ""
---

**Un capteur passif de menaces WiFi, minuscule comme un pouce, qui ne répond jamais**

## Le problème du WiFi public

Chaque connexion au WiFi d'un hôtel, d'un café ou d'un aéroport suppose que le point d'accès est authentique. Pourtant, les **trames de gestion 802.11**, qui annoncent les réseaux, gèrent les connexions et coordonnent les clients, ne sont *pas authentifiées dans la plupart des déploiements*. Avec du matériel modeste, il est possible de cloner un SSID, d'envoyer des trames de désauthentification ou de créer un leurre ouvert à côté d'un réseau WPA2 légitime.

[**ESP32 WiFi Canary**](https://github.com/simeononsecurity/esp32-wifi-canary) est un capteur de veille passive qui rend ce risque visible dans un format minuscule. Il tient dans le M5Stack Atom Lite, grosso modo la taille d'un morceau de sucre. Branché sur un port USB, il apprend son environnement et allume une LED RGB lorsqu'il détecte des motifs associés à des menaces sans fil.

Il ne se connecte à rien, ne capture pas d'identifiants et ne transmet aucune trame. Il observe, attribue un score et indique la situation par une couleur.

Cet article constitue une référence technique complète du projet : détections, modèle de confiance, compilation et flashage, ainsi que limites en conditions réelles.

---

## Ce que fait et ne fait pas ESP32 WiFi Canary

### Toujours passif

WiFi Canary utilise deux modes radio, jamais simultanément :

1. **Mode promiscuous** : reçoit et inspecte les trames de gestion 802.11, notamment de désauthentification et de désassociation, sans s'associer à un réseau.
2. **Mode scan** : effectue des scans WiFi actifs pour répertorier les points d'accès proches et les comparer à une base de référence apprise.

L'appareil ne réalise aucune des actions suivantes :
- Il ne s'associe à aucun réseau et ne s'y connecte pas ;
- Il ne capture ni trame de données ni identifiant ;
- Il ne transmet aucune trame 802.11 ;
- Il n'écrit rien dans une mémoire flash persistante ;
- Il ne communique pas sur Internet.

**Tout ce qu'il apprend reste en RAM et disparaît au redémarrage.** C'est voulu : le canari est un **capteur**, pas un appareil de capture.

### La LED sert d'interface

Il n'y a ni écran, ni application, ni interface Web. La sortie de l'appareil se limite à un **NeoPixel RGB SK6812** sur GPIO 27 du M5Stack Atom Lite. La LED indique quatre états :

| État de la LED | Signification |
|---|---|
| 🔵 Bleu (impulsion lente) | Démarrage, création de la référence |
| 🟢 Vert (fixe) | Normal, aucun problème de confiance élevée |
| 🟡 Jaune (fixe) | Prudence, motif suspect détecté |
| 🔴 Rouge (impulsion rapide) | Alerte, menace de confiance supérieure détectée |

Le démarrage prend environ **24 secondes** (3 scans de 8 secondes). Lorsque la LED quitte le bleu, la référence est prête et la surveillance commence.

---

## Matériel

### Cible principale : M5Stack Atom Lite

Le projet est conçu pour le M5Stack Atom Lite, une plateforme de développement ESP32 complète dans un boîtier de 24 × 24 mm.

| Composant | Détail |
|---|---|
| MCU | ESP32-PICO-D4 |
| LED | Un NeoPixel RGB SK6812 (GPIO 27) |
| Bouton | GPIO 39, actif à l'état bas |
| USB | Pont UART CP2104 |
| Alimentation | USB-C, environ 80–120 mA pendant le scan |

**Aucune breadboard, aucun composant externe et aucune soudure.** Branchez-le à une alimentation USB pour le démarrer.

### ESP32 DevKit générique pour le développement et les tests

Le projet comprend un second environnement de compilation PlatformIO (`esp32dev`) destiné aux cartes ESP32 standard. Dans cette configuration :

- la LED intégrée au GPIO 2 remplace le NeoPixel ;
- toute la sortie de débogage série est activée ;
- la logique de détection fonctionne comme sur Atom Lite.

Le projet est ainsi accessible aux personnes disposant d'un ESP32 DevKit à 5 $ et permet de tester la détection sans le matériel cible.

---

## Apprentissage de la référence

### Pourquoi une référence est importante

Un canari qui se déclenche sur chaque réseau ouvert d'une ville serait inutile. ESP32 WiFi Canary apprend d'abord son environnement, puis évalue les menaces. La première phase construit une **table de référence** des points d'accès légitimes présents dans la zone.

### Trois scans en 24 secondes

Au démarrage, l'appareil effectue trois scans WiFi séquentiels séparés par une pause. Une fois terminés, les points d'accès appris - SSID, BSSID, type de chiffrement et puissance du signal - sont enregistrés comme référence.

La sortie série de cette phase ressemble à ceci :

```
==============================================
 Travel WiFi Canary v1.0
 Passive 2.4 GHz awareness sensor
==============================================
[canary] setup done - starting baseline learning
[canary] baseline scan start (aps=0 score=0)
[canary] scan found 18 APs
[canary] baseline scan 1/3
[canary] baseline scan start (aps=18 score=0)
[canary] scan found 18 APs
[canary] baseline scan 2/3
[canary] baseline scan start (aps=18 score=0)
[canary] scan found 19 APs
[canary] baseline complete: 19 APs learned
  [00] MyHomeWifi                    aa:bb:cc:dd:ee:ff ch06 WPA2     -52 dBm
  [01] XFINITY                       11:22:33:44:55:66 ch01 WPA2     -71 dBm
  ...
[canary] STARTUP → NORMAL  (score=0  "")
```

Lorsque la LED passe du bleu au vert, l'appareil fonctionne pleinement.

---

## Détections : catégories de menaces

WiFi Canary surveille six types de motifs. Chacun contribue à un **score de confiance** qui commande l'état de la LED. *Aucun indicateur isolé ne suffit à conclure* : le modèle accumule des éléments corroborants avant d'escalader.

### 1. Rafales de désauthentification et de désassociation

Les **sous-types 10 (désassociation) et 12 (désauthentification) des trames de gestion 802.11** sont couramment utilisés dans les attaques WiFi. Tout appareil peut envoyer ces trames, et les clients qui les reçoivent sont déconnectés de leur point d'accès.

En **mode promiscuous**, le canari compte ces trames par adresse MAC source dans une fenêtre glissante de **5 secondes**.

| Condition | Points ajoutés |
|---|---|
| ≥ 8 trames d'une source en 5 s | +2 |
| ≥ 20 trames d'une source en 5 s | +4 |
| ≥ 5 trames de désauthentification en broadcast | +1 |

**Les seuils comptent** : un client qui passe d'un point d'accès à un autre génère quelques trames légitimes. Les outils d'attaque en produisent des centaines par seconde contre une cible. La fenêtre de 5 secondes et le seuil de 8 trames écartent le bruit normal de l'itinérance tout en détectant les rafales prolongées d'outils comme `aireplay-ng`.

### 2. Clone ouvert d'un réseau chiffré connu (evil twin)

**C'est la détection la plus fiable.** Une attaque evil twin consiste souvent à :

1. Créer une copie ouverte, sans mot de passe, d'un SSID WPA2 connu.
2. Émettre plus fort que le vrai point d'accès pour que les clients s'y connectent automatiquement.

Après l'apprentissage de la référence, un nouveau scan détecte un SSID qui n'utilisait que WPA/WPA2/WPA3, mais apparaît maintenant comme **OPEN** :

| Condition | Points ajoutés |
|---|---|
| Même SSID, chiffré auparavant, désormais ouvert | +3 |
| BSSID absent de la référence | +1 |
| Signal du clone ≥ 10 dB plus fort que le point d'accès connu | +1 |

Un clone ouvert du WiFi de l'hôtel, 10 dB plus puissant que le point d'accès réel, est un cas d'école. *Cette combinaison atteint 5 points (Prudence) en un seul cycle de scan.*

**Exemple série** :

```
[canary] OPEN CLONE: SSID='MyHomeWifi' baseline=WPA2 clone=OPEN bssid=de:ad:be:ef:00:01 rssi=-48/-52
[canary] score +4 → 4  "open clone of encrypted SSID 'MyHomeWifi'"
[canary] NORMAL → CAUTION  (score=4  "open clone of encrypted SSID 'MyHomeWifi'")
```

### 3. Point d'accès chiffré d'origine absent et clone ouvert présent

Variante plus avancée : le clone plus puissant attire les clients tandis que le vrai point d'accès est simultanément expulsé des ondes par désauthentification.

| Condition | Points ajoutés |
|---|---|
| Point chiffré de référence disparu et réseau ouvert correspondant apparu | +3 |

Cela couvre le cas où le point d'accès réel émet toujours, mais perd la compétition de puissance du signal, ou subit une perturbation active.

### 4. Dégradation de sécurité

Le même SSID qu'une entrée de référence est observé, mais avec un chiffrement plus faible que celui enregistré.

| Condition | Points ajoutés |
|---|---|
| WPA3 → WPA2 | +1 |
| WPA2 → WPA | +1 |
| Baisse d'au moins 2 niveaux de chiffrement | +3 |

*Les dégradations vers un réseau ouvert relèvent de la détection evil twin, avec un score plus élevé.* Cette catégorie vise les baisses partielles qui échapperaient à une simple comparaison entre ouvert et chiffré.

### 5. SSID dupliqué d'un fournisseur inattendu

Même SSID et même type de sécurité qu'un point d'accès de référence, mais BSSID doté d'un **OUI de fournisseur différent** (les 3 premiers octets de l'adresse MAC).

| Condition | Points ajoutés |
|---|---|
| OUI différent du point de référence partageant le même SSID | +1 |
| Clone également ≥ 10 dB plus puissant | +2 |

*Le score reste volontairement faible.* Les réseaux d'entreprise, systèmes mesh et points d'accès de fournisseurs d'accès ont souvent plusieurs BSSID légitimes pour un même SSID, chez différents fabricants. Ce signal doit s'ajouter à d'autres éléments plutôt que déclencher seul une alerte.

### 6. Inondation de balises ou de SSID

Compte les nouveaux SSID absents de la référence et apparus dans une **fenêtre glissante de 30 secondes**.

| Condition | Points ajoutés |
|---|---|
| ≥ 15 nouveaux SSID en 30 s | +2 |
| ≥ 30 nouveaux SSID en 30 s | +3 |

Les **attaques par inondation de balises** diffusent des milliers de faux SSID pour perturber les tables de scan ou empêcher les balises légitimes. Quinze SSID inconnus en 30 secondes constituent un événement inhabituel dans la plupart des environnements.

---

## Modèle de score de confiance

Toutes les détections alimentent un **score de menace** entier qui commande l'état de la LED :

| Plage de score | État de la LED |
|---|---|
| 0–2 | Normal (vert) |
| 3–5 | Prudence (jaune) |
| 6+ | Alerte (rouge, impulsion rapide) |

### Décroissance du score

Le score **baisse d'un point toutes les 60 secondes** en l'absence de nouveaux événements. C'est un choix de conception important :

- Une rafale de désauthentification fait passer le score à Prudence, puis il revient automatiquement à Normal en quelques minutes si l'attaque cesse.
- Une attaque soutenue qui produit des événements maintient l'état Alerte.
- L'appareil se réinitialise sans intervention ni redémarrage.

Cela signifie que :
- **Les anomalies brèves** (itinérance ou transitoires de réseaux voisins) se résolvent seules.
- **Les attaques soutenues** restent signalées.
- **Pas de fatigue liée aux alertes** pour un événement isolé qui ne se répète pas.

### Réinitialisation par bouton

Le bouton GPIO 39 de l'Atom Lite permet deux actions :

1. Envoyer la table complète des points d'accès sur la sortie série, pour auditer ce que voit l'appareil.
2. Ramener le score de menace à 0 et repasser immédiatement au vert afin d'observer le prochain scan sans historique.

---

## Compilation et flashage

### Prérequis

- **PlatformIO** (CLI ou extension VS Code)
- **M5Stack Atom Lite** (ou ESP32 DevKit pour les tests)
- Câble USB-C

### Flasher le M5Stack Atom Lite

```bash
git clone https://github.com/simeononsecurity/esp32-wifi-canary.git
cd esp32-wifi-canary

# Compilation et flashage
pio run -e atom-lite --target upload

# Ouvrir le moniteur série à 115200 bauds
pio device monitor -b 115200
```

### Flasher un ESP32 DevKit générique

```bash
pio run -e esp32dev --target upload
```

La compilation DevKit utilise GPIO 2 (LED intégrée) et affiche tout le journal série. Aucun NeoPixel n'est piloté. La logique de détection est identique à celle d'Atom Lite.

### Structure du projet

```
esp32-wifi-canary/
├── main.cpp              # Toute la logique du firmware
├── platformio.ini        # Environnements de compilation (atom-lite, esp32dev)
├── partitions_4mb.csv    # Table de partition flash de 4 Mo
└── README.md
```

Le firmware complet tient dans **un seul fichier source C++**. La détection n'utilise aucune bibliothèque externe, seulement le framework ESP32 Arduino pour les scans WiFi, les callbacks en mode promiscuous et le contrôle NeoPixel.

### Environnements platformio.ini

```ini
[env:atom-lite]
platform = espressif32
board = m5stick-c
framework = arduino

[env:esp32dev]
platform = espressif32
board = esp32dev
framework = arduino
```

L'environnement `atom-lite` utilise la définition de carte `m5stick-c` (même puce ESP32-PICO-D4 et brochage compatible avec le NeoPixel sur GPIO 27).

---

## Référence de la sortie série

L'appareil produit des journaux détaillés à **115200 bauds**. Toutes les lignes commencent par `[canary]`, ce qui facilite leur filtrage.

### Séquence de démarrage

```
==============================================
 Travel WiFi Canary v1.0
 Passive 2.4 GHz awareness sensor
==============================================
[canary] setup done - starting baseline learning
[canary] baseline scan start (aps=0 score=0)
[canary] scan found 18 APs
[canary] baseline scan 1/3
...
[canary] baseline complete: 19 APs learned
  [00] MyHomeWifi                    aa:bb:cc:dd:ee:ff ch06 WPA2     -52 dBm
  [01] XFINITY                       11:22:33:44:55:66 ch01 WPA2     -71 dBm
[canary] STARTUP → NORMAL  (score=0  "")
```

### Événements détectés

```
[canary] normal scan start (aps=19 score=0)
[canary] scan found 21 APs
[canary] OPEN CLONE: SSID='HotelWiFi' baseline=WPA2 clone=OPEN bssid=de:ad:be:ef:00:01 rssi=-48/-52
[canary] score +4 → 4  "open clone of encrypted SSID 'HotelWiFi'"
[canary] NORMAL → CAUTION  (score=4  "open clone of encrypted SSID 'HotelWiFi'")
```

### Transitions du score

```
[canary] CAUTION → NORMAL  (score=2  "score decay")
[canary] NORMAL → ALERT    (score=6  "sustained deauth burst + open clone")
```

Le journal série indique ce que l'appareil a vu, à quel moment et pourquoi le score a évolué. Il sert aussi de **journal d'audit passif**, même sans regarder la LED.

---

## Notes de détection et limites pratiques

Le README explique franchement les limites de l'appareil. Elles méritent d'être détaillées.

### Causes possibles de faux positifs

**Les réseaux d'entreprise et mesh** sont la principale source de faux positifs. Un grand déploiement d'entreprise, un hôtel ou un système mesh comme Eero ou Google WiFi peut légitimement présenter :

- Plusieurs BSSID pour le même SSID avec différents OUI de fournisseur.
- Des configurations de sécurité différentes selon les bandes.
- Des points d'accès qui apparaissent et disparaissent à mesure que le mesh s'adapte.

**Les routeurs Airbnb et SOHO** avec plusieurs SSID pour les bandes peuvent également présenter des OUI différents si les radios 2,4 et 5 GHz utilisent des blocs MAC consécutifs provenant de blocs différents.

*Transitoires des réseaux voisins* : un réseau chiffré qui disparaît brièvement du scan et revient avec d'autres paramètres (mise à jour du firmware, redémarrage ou reconfiguration) peut déclencher une détection passagère.

Le score et sa décroissance visent à *réduire, sans éliminer*, ces faux positifs.

### Causes possibles de faux négatifs

Une **attaque evil twin bien conçue** qui :

- Usurpe le BSSID exact du point d'accès légitime pour faire correspondre l'OUI.
- Reprend exactement le type de sécurité avec une configuration IE WPA2 correcte.
- Émet à une puissance située à moins de 10 dB du point d'accès réel.

*Peut ne pas accumuler assez de points pour atteindre Prudence.* La désauthentification nécessaire pour éjecter les clients du point réel ajouterait des points, mais un attaquant sophistiqué qui réduit le nombre de trames pourrait rester sous le seuil.

### Lacune pendant le changement de radio

**La radio ESP32 ne peut pas être en mode promiscuous et scanner activement les points d'accès simultanément.** Le firmware alterne entre ces modes. Ainsi, **les trames de désauthentification arrivant pendant la fenêtre de scan d'environ 3 secondes ne sont pas capturées**. Un attaquant pourrait synchroniser ses rafales avec cette fenêtre, mais devrait connaître le calendrier de scan.

### 2,4 GHz uniquement

La radio ESP32 fonctionne en 2,4 GHz. **Les réseaux 5 et 6 GHz ne sont ni scannés ni surveillés.** L'appareil ne détectera pas les evil twins opérant uniquement en 5 GHz.

### Portée passive

La détection de désauthentification exige que l'appareil reçoive les trames. Un attaquant éloigné, utilisant une antenne très directive, ou ciblant un client loin du canari, peut émettre des trames trop faibles pour activer les compteurs.

---

## Cas d'utilisation

### Voyager avec des données sensibles

Le canari est d'abord conçu pour les déplacements. Branchez-le à un port USB d'ordinateur portable, d'hôtel ou de batterie externe et laissez-le apprendre l'environnement de l'hôtel ou du centre de conférence. Toute apparition ultérieure d'un clone ouvert du SSID de l'hôtel, scénario d'attaque le plus courant, déclenche au minimum Prudence.

### Cafés et WiFi public

Les réseaux WiFi ouverts sont une cible fréquente des evil twins. Grâce à sa référence, le canari apprend le point d'accès légitime à l'arrivée, puis surveille l'apparition de SSID concurrents.

### Sensibilisation et formation à la sécurité

La sortie série fournit un journal détaillé et lisible de ce qu'il observe. En formation, montrer une rafale de désauthentification en temps réel et voir la LED changer de couleur est bien plus efficace qu'un diaporama.

### Surveillance passive de laboratoire

Dans un laboratoire domestique ou un petit bureau, le canari sert de moniteur ambiant permanent. La LED fournit un état immédiat et le bouton permet d'afficher la table actuelle des réseaux à la demande.

---

## Notes d'architecture

### Pourquoi un score unique plutôt que des alertes séparées

Le modèle agrège différents signaux en un seul nombre au lieu de présenter plusieurs catégories. C'est un choix d'interface délibéré : la sortie est une LED avec trois états. Des alertes distinctes nécessiteraient un écran ou une application. *Le score traduit des signaux bruités et partiellement corrélés en un indicateur exploitable.*

### Pourquoi le score décroît

Sans décroissance, un faux positif isolé nécessiterait une intervention manuelle par bouton. Avec une baisse toutes les 60 secondes, les anomalies brèves disparaissent en quelques minutes. **Le canari fonctionne ainsi sans surveillance**, dans un sac, une chambre d'hôtel ou une voiture, puis revient à son état de référence après un événement transitoire.

### Pourquoi trois scans de référence

Un scan unique peut manquer un point d'accès qui ne diffusait pas pendant cette période, par exemple à cause d'une pause ou d'une coupure temporaire. *Trois scans sur environ 24 secondes donnent une image plus complète de l'environnement stable avant le début de la surveillance.*

---

## Contributions et état du projet

Le projet est disponible sur [github.com/simeononsecurity/esp32-wifi-canary](https://github.com/simeononsecurity/esp32-wifi-canary) sous une licence d'utilisation passive. Le code tient dans un seul `main.cpp`, facile à lire, auditer et étendre.

Avec PlatformIO et ESP32, le projet se compile sans modification pour Atom Lite et pour un DevKit standard.

---

## Comparaison avec d'autres méthodes de surveillance WiFi

| Approche | Passive ? | Sans identifiants | Sortie par LED unique | Format voyage |
|---|---|---|---|---|
| ESP32 WiFi Canary | ✅ | ✅ | ✅ | ✅ |
| Kismet (ordinateur portable) | ✅ | ✅ | ❌ (écran requis) | ❌ (encombrant) |
| WiFi Pineapple | ❌ (actif) | ❌ | ❌ | Partiel |
| IDS sans fil (entreprise) | ✅ | ✅ | ❌ (infrastructure requise) | ❌ |
| Scan manuel (application mobile) | Partiel | ✅ | ❌ | ✅ |

Le canari occupe un créneau précis : **surveillance ambiante permanente, sans interaction ni connexion réseau**, dans un format qui tient à un porte-clés ou dans un sac d'ordinateur.

---

## Conclusion

ESP32 WiFi Canary fait une seule chose : surveiller l'environnement 2,4 GHz et changer de couleur quand quelque chose paraît anormal. Ce n'est ni un système complet de détection d'intrusion sans fil, ni un outil de capture de paquets, ni un analyseur forensique. C'est un canari, un capteur passif qui remarque quand l'environnement devient dangereux.

Le **modèle de score de confiance**, la **décroissance du score** et la **référence en trois phases** répondent au problème des faux positifs des capteurs de sécurité ambiants. L'appareil peut fonctionner sans surveillance dans un hôtel ou un centre de conférence et signaler les anomalies importantes sans réagir au bruit normal du réseau.

Pour quiconque prépare une trousse de sécurité portable, travaille avec une infrastructure WiFi non fiable ou cherche un projet ESP32 utile, WiFi Canary vaut une après-midi et un M5Stack Atom Lite à 15 $.

**GitHub** : [github.com/simeononsecurity/esp32-wifi-canary](https://github.com/simeononsecurity/esp32-wifi-canary)
