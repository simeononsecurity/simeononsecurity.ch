---
title: "ESP32 WiFi Canary: detecció passiva d'amenaces a 2,4 GHz"
date: 2026-06-06
lastmod: 2026-11-22
toc: true
draft: false
description: "Anàlisi tècnica d'ESP32 WiFi Canary, un sensor passiu de 2,4 GHz que detecta punts d'accés falsos, desautenticacions, degradacions de seguretat i inundacions de balises."
genre: ["Seguretat de xarxes", "Seguretat WiFi", "Seguretat IoT", "Recerca de seguretat", "Sistemes encastats", "Eines de privadesa", "Projectes ESP32", "Seguretat de maquinari", "Seguretat sense fil", "Seguretat de codi obert"]
tags: ["ESP32", "WiFi Canary", "M5Stack Atom Lite", "Detecció de desautenticació", "Detecció de punts d'accés falsos", "Seguretat WiFi", "Monitoratge passiu de WiFi", "Trames de gestió 802.11", "Seguretat de xarxes", "Seguretat IoT", "NeoPixel", "SK6812", "PlatformIO", "C++", "Codi obert", "Sensor de seguretat", "Detecció d'amenaces sense fil", "Monitoratge de BSSID", "Monitoratge de SSID", "Detecció de degradació de seguretat", "Detecció d'inundacions de balises", "Monitoratge WiFi", "LED RGB", "Mode promiscu", "Seguretat encastada", "Seguretat en viatges", "Seguretat WiFi d'hotels", "WiFi de cafeteries", "Conscienciació sobre seguretat", "simeononsecurity"]
canonical: "https://simeononsecurity.com/articles/esp32-wifi-canary-passive-wifi-threat-detection-2026/"
cover: "/img/cover/esp32-wifi-canary-passive-wifi-threat-detection-2026.webp"
coverAlt: "Il·lustració d'un dispositiu petit semblant a ESP32 WiFi Canary, connectat a un port USB, amb un LED RGB que brilla en diversos colors i representa les seves funcions de detecció d'amenaces."
coverCaption: ""
---

**Un sensor passiu d'amenaces WiFi, de la mida d'un polze, que no transmet mai**

## El problema de la WiFi pública

Quan et connectes a la WiFi d'un hotel, una cafeteria o un aeroport, confies que el punt d'accés sigui legítim. El problema és que les **trames de gestió 802.11**, que anuncien xarxes, gestionen connexions i coordinen clients, *no s'autentiquen en la majoria de desplegaments*. Amb maquinari senzill, qualsevol pot clonar un SSID, enviar trames de desautenticació als clients o crear un esquer obert al costat d'una xarxa WPA2 legítima.

[**ESP32 WiFi Canary**](https://github.com/simeononsecurity/esp32-wifi-canary) és un sensor passiu de conscienciació que aborda aquest risc amb una empremta mínima. Cap en un M5Stack Atom Lite, aproximadament de la mida d'un terròs de sucre; es connecta a qualsevol port USB, aprèn l'entorn i encén un LED RGB quan detecta patrons compatibles amb amenaces sense fil.

No es connecta a cap xarxa. No captura credencials. No transmet cap trama. Observa, calcula una puntuació i t'indica l'estat amb un color.

Aquest article és una referència tècnica completa del projecte: què detecta, com funciona el model de confiança, com compilar-lo i gravar-lo, i quines limitacions té en l'ús real.

---

## Què fa ESP32 WiFi Canary i què no fa

### Sempre és passiu

WiFi Canary funciona en dos modes de ràdio, mai alhora:

1. **Mode promiscu**: rep i inspecciona trames de gestió 802.11, com ara desautenticacions i desassociacions, sense associar-se a cap xarxa.
2. **Mode d'escaneig**: cerca punts d'accés WiFi propers i els compara amb una línia base apresa.

El dispositiu mai:
- s'associa ni es connecta a cap xarxa;
- captura trames de dades ni credencials;
- transmet trames 802.11;
- desa dades a la memòria flaix persistent;
- es comunica per Internet.

**Tot el que aprèn es manté a la RAM i s'esborra en reiniciar.** És intencionat: el canari és un **sensor**, no un dispositiu de captura.

### El LED és la interfície

No hi ha pantalla, aplicació ni interfície web. L'única sortida del dispositiu és un **NeoPixel RGB SK6812** al GPIO 27 del M5Stack Atom Lite. El LED comunica quatre estats:

| Estat del LED | Significat |
|---|---|
| 🔵 Blau (pols lent) | Inici, creació de la línia base |
| 🟢 Verd (fix) | Normal, sense incidències d'alta confiança |
| 🟡 Groc (fix) | Precaució, patró sospitós detectat |
| 🔴 Vermell (pols ràpid) | Alerta, amenaça de confiança més alta detectada |

L'inici dura aproximadament **24 segons** (3 escanejos de 8 segons). Quan el LED deixa el blau, ja hi ha una línia base funcional i comença el monitoratge actiu.

---

## Maquinari

### Objectiu principal: M5Stack Atom Lite

El projecte està dissenyat per a l'M5Stack Atom Lite, una plataforma ESP32 completa dins una carcassa de 24 × 24 mm.

| Element | Detall |
|---|---|
| MCU | ESP32-PICO-D4 |
| LED | Un NeoPixel RGB SK6812 (GPIO 27) |
| Botó | GPIO 39, actiu en nivell baix |
| USB | Pont UART CP2104 |
| Alimentació | USB-C, ~80–120 mA durant l'escaneig |

**No necessites protoboard, components externs ni soldar.** Connecta'l a l'alimentació USB i funcionarà.

### ESP32 DevKit genèric per al desenvolupament i les proves

El projecte inclou un segon entorn de compilació de PlatformIO (`esp32dev`) per a plaques ESP32 estàndard. En aquesta configuració:

- s'utilitza el LED integrat al GPIO 2 en lloc del NeoPixel;
- s'activa tota la sortida de depuració sèrie;
- tota la lògica de detecció funciona igual que a la compilació Atom Lite.

Això fa que el projecte sigui accessible a qualsevol persona amb un ESP32 DevKit de 5 $, i permet provar la lògica de detecció sense el maquinari objectiu.

---

## Procés d'aprenentatge de la línia base

### Per què importa una línia base

Un canari que s'activés amb cada xarxa oberta d'una ciutat seria inútil. ESP32 WiFi Canary aprèn l'entorn abans de puntuar amenaces. La primera fase crea una **taula de referència** dels punts d'accés que existeixen legítimament a la zona.

### Tres escanejos, 24 segons

En iniciar-se, el dispositiu fa tres escanejos WiFi consecutius, separats per una pausa. En acabar, desa com a línia base el conjunt de punts d'accés après: SSID, BSSID, tipus de xifratge i intensitat del senyal.

La sortida sèrie durant aquesta fase és semblant a:

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

Quan el LED passa del blau al verd, el dispositiu ja funciona plenament.

---

## Què detecta: categories d'amenaces

WiFi Canary supervisa sis patrons d'amenaça. Cadascun aporta punts a una **puntuació de confiança** que determina l'estat del LED. *Cap indicador per si sol es considera cert; el model acumula proves corroborants abans d'escalar l'alerta.*

### 1. Ràfegues de desautenticació o desassociació

Els **subtipus 10 (desassociació) i 12 (desautenticació) de les trames de gestió 802.11** són eines habituals dels atacs WiFi. Qualsevol dispositiu pot enviar aquestes trames, i els clients que les reben es desconnecten del seu punt d'accés.

El canari supervisa aquestes trames en **mode promiscu** i les compta per adreça MAC d'origen dins una **finestra mòbil de 5 segons**.

| Condició | Punts afegits |
|---|---|
| ≥ 8 trames d'una font en 5 s | +2 |
| ≥ 20 trames d'una font en 5 s | +4 |
| ≥ 5 trames de desautenticació de difusió | +1 |

**Per què importen els llindars**: un client que canvia de punt d'accés genera algunes trames legítimes de desautenticació o desassociació. *Les eines d'atac generen un patró diferent*: centenars de trames per segon mantingudes contra un objectiu. La finestra de 5 segons i el mínim de 8 trames filtren el soroll normal de roaming i detecten ràfegues sostingudes d'eines com `aireplay-ng`.

### 2. Còpia oberta d'una xarxa xifrada coneguda (evil twin)

**És la detecció de més confiança.** Un atac evil twin sovint funciona així:

1. Es crea una còpia oberta (sense contrasenya) d'un SSID WPA2 conegut.
2. Se li dona més potència que al punt d'accés real perquè els clients s'hi connectin automàticament.

Després d'aprendre la línia base, si un escaneig nou mostra com a **OPEN** un SSID que abans només utilitzava WPA, WPA2 o WPA3:

| Condició | Punts afegits |
|---|---|
| Mateix SSID, abans xifrat i ara obert | +3 |
| BSSID absent de la línia base | +1 |
| Senyal de la còpia ≥ 10 dB més fort que el punt d'accés conegut | +1 |

Una còpia oberta del SSID WiFi d'un hotel, amb un senyal 10 dB més fort que el punt d'accés real, és un cas de manual. *Aquesta combinació porta la puntuació a 5 (precaució) en un sol cicle d'escaneig.*

**Exemple sèrie**:

```
[canary] OPEN CLONE: SSID='MyHomeWifi' baseline=WPA2 clone=OPEN bssid=de:ad:be:ef:00:01 rssi=-48/-52
[canary] score +4 → 4  "open clone of encrypted SSID 'MyHomeWifi'"
[canary] NORMAL → CAUTION  (score=4  "open clone of encrypted SSID 'MyHomeWifi'")
```

### 3. Desapareix el punt d'accés xifrat original i apareix una còpia oberta

En una variant més avançada, la còpia més potent de l'atacant fa que els clients la prefereixin mentre el punt d'accés real queda fora de l'aire per desautenticació.

| Condició | Punts afegits |
|---|---|
| Ha desaparegut un punt d'accés xifrat de la línia base i ha aparegut una xarxa oberta coincident | +3 |

Això cobreix el cas en què el punt d'accés real encara emet, però perd la competició d'intensitat del senyal, o en què algú el desestabilitza deliberadament.

### 4. Degradació de seguretat

Es detecta el mateix SSID que a la línia base, però amb un xifratge més feble.

| Condició | Punts afegits |
|---|---|
| WPA3 → WPA2 | +1 |
| WPA2 → WPA | +1 |
| Descens de 2 o més nivells de xifratge | +3 |

*Les degradacions a una xarxa oberta s'identifiquen amb la detecció d'evil twin i reben més punts.* Aquesta categoria se centra en degradacions parcials que podrien passar desapercebudes en una comparació només entre obert i xifrat.

### 5. SSID duplicat d'un fabricant inesperat

És el mateix SSID i tipus de seguretat que un punt d'accés de la línia base, però amb una **OUI de fabricant diferent** al BSSID (els tres primers bytes de l'adreça MAC).

| Condició | Punts afegits |
|---|---|
| OUI diferent de la del punt d'accés de línia base amb el mateix SSID | +1 |
| La còpia també és ≥ 10 dB més potent | +2 |

*Aquesta senyal té una puntuació deliberadament baixa.* Xarxes empresarials, sistemes mesh i punts d'accés d'ISP poden tenir legítimament diversos BSSID del mateix SSID amb fabricants diferents. La senyal s'acumula amb altres proves, no ha d'activar l'alerta per si sola.

### 6. Inundació de balises o SSID

Compta els SSID nous, absents de la línia base, que apareixen en una **finestra mòbil de 30 segons**.

| Condició | Punts afegits |
|---|---|
| ≥ 15 SSID nous en 30 s | +2 |
| ≥ 30 SSID nous en 30 s | +3 |

Els atacs d'**inundació de balises** emeten milers de SSID falsos per confondre les taules d'escaneig dels clients o impedir les balises legítimes. En la majoria d'entorns, 15 SSID desconeguts en 30 segons és inusual.

---

## Model de puntuació de confiança

Tots els senyals detectats alimenten una única **puntuació d'amenaça** entera. La puntuació determina l'estat del LED:

| Interval de puntuació | Estat del LED |
|---|---|
| 0–2 | Normal (verd) |
| 3–5 | Precaució (groc) |
| 6 o més | Alerta (vermell, pols ràpid) |

### Decaïment de la puntuació

La puntuació **baixa un punt cada 60 segons** si no hi ha cap nou esdeveniment que l'augmenti. És una de les decisions de disseny més pràctiques del projecte:

- Una sola ràfega de desautenticació porta l'estat a precaució, però torna a normal en uns minuts si l'atac s'atura.
- Un atac sostingut que continua generant esdeveniments manté l'estat d'alerta.
- El dispositiu es recupera sense intervenció ni reinici.

Això vol dir que:
- **Les anomalies breus**, com els canvis d'AP o les xarxes veïnes transitòries, desapareixen soles.
- **Els atacs sostinguts** continuen assenyalats.
- **No hi ha fatiga d'alertes** per esdeveniments únics que no es repeteixen.

### Reinici amb el botó

Prémer el botó GPIO 39 de l'Atom Lite fa dues coses:

1. Aboca la taula completa d'AP actual a la sortida sèrie, útil per auditar exactament què detecta el dispositiu.
2. Reinicia la puntuació d'amenaça a 0. El LED torna immediatament al verd perquè puguis observar el següent escaneig des de zero.

---

## Compilar i gravar

### Requisits

- **PlatformIO** (CLI o extensió per a VS Code)
- **M5Stack Atom Lite** (o ESP32 DevKit per provar)
- Cable USB-C

### Gravar a l'M5Stack Atom Lite

```bash
git clone https://github.com/simeononsecurity/esp32-wifi-canary.git
cd esp32-wifi-canary

# Compila i grava
pio run -e atom-lite --target upload

# Obre el monitor sèrie a 115200 bauds
pio device monitor -b 115200
```

### Gravar a un ESP32 DevKit genèric

```bash
pio run -e esp32dev --target upload
```

La compilació DevKit utilitza el GPIO 2 (LED integrat) i mostra el registre sèrie complet. No controla cap NeoPixel. La lògica de detecció és idèntica a la de l'Atom Lite.

### Estructura del projecte

```
esp32-wifi-canary/
├── main.cpp              # Tota la lògica del microprogramari
├── platformio.ini        # Entorns de compilació (atom-lite, esp32dev)
├── partitions_4mb.csv    # Taula de particions de flaix de 4 MB
└── README.md
```

Tot el microprogramari és un **únic fitxer de codi font C++**. La lògica de detecció no depèn de biblioteques externes; només utilitza el framework ESP32 Arduino per escanejar WiFi, fer servir crides de retorn en mode promiscu i controlar el NeoPixel.

### Entorns de platformio.ini

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

L'entorn `atom-lite` utilitza la definició de placa `m5stick-c` (el mateix xip ESP32-PICO-D4 i una assignació de pins compatible amb el NeoPixel del GPIO 27).

---

## Referència de la sortida sèrie

El dispositiu registra informació detallada a **115200 bauds**. Totes les línies comencen amb `[canary]` per facilitar-ne el filtratge.

### Seqüència d'inici

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

### Esdeveniments de detecció

```
[canary] normal scan start (aps=19 score=0)
[canary] scan found 21 APs
[canary] OPEN CLONE: SSID='HotelWiFi' baseline=WPA2 clone=OPEN bssid=de:ad:be:ef:00:01 rssi=-48/-52
[canary] score +4 → 4  "open clone of encrypted SSID 'HotelWiFi'"
[canary] NORMAL → CAUTION  (score=4  "open clone of encrypted SSID 'HotelWiFi'")
```

### Canvis de puntuació

```
[canary] CAUTION → NORMAL  (score=2  "score decay")
[canary] NORMAL → ALERT    (score=6  "sustained deauth burst + open clone")
```

El registre sèrie permet entendre què ha vist el dispositiu, quan ho ha vist i per què ha canviat la puntuació. Això el converteix en un **registre d'auditoria passiu**, fins i tot si no mires el LED.

---

## Notes de detecció i limitacions pràctiques

El README és inusualment honest sobre allò que el dispositiu no pot fer, i val la pena repetir-ho amb detall.

### Causes possibles de falsos positius

Les **xarxes empresarials i mesh** són la font principal de falsos positius. Una empresa gran, un hotel amb molts AP o un sistema mesh com Eero o Google WiFi pot mostrar legítimament:
- diversos BSSID per al mateix SSID amb OUI de fabricants diferents (detecció de fabricant);
- configuracions de seguretat diferents entre bandes (detecció de degradació);
- punts d'accés que apareixen i desapareixen mentre s'ajusta la xarxa mesh.

Els **encaminadors d'Airbnb i SOHO** amb diversos SSID per a bandes diferents també poden activar discrepàncies d'OUI si les ràdios de 2,4 i 5 GHz utilitzen MAC consecutives de blocs diferents.

*Canvis transitoris a xarxes veïnes*: una xarxa xifrada que desapareix temporalment de l'escaneig i reapareix amb paràmetres diferents (actualització de microprogramari, reinici o reconfiguració) pot activar una detecció momentània.

La puntuació de confiança i el decaïment volen *reduir, però no eliminar*, aquests falsos positius.

### Causes possibles de falsos negatius

Un **atac evil twin ben preparat** que:
- falsifica exactament el BSSID del punt d'accés legítim perquè coincideixi l'OUI;
- utilitza exactament el mateix tipus de seguretat (WPA2 amb una configuració IE correcta);
- manté la intensitat del senyal a menys de 10 dB de la del punt d'accés real,

*potser no acumula prou puntuació per arribar al llindar de precaució.* La part de desautenticació de l'atac, necessària per apartar clients del punt d'accés real, sumaria punts. Però un atacant sofisticat que minimitzi aquestes trames podria quedar per sota del llindar.

### Interrupció durant el canvi de ràdio

**La ràdio WiFi de l'ESP32 no pot estar en mode promiscu i escanejar AP activament alhora.** El microprogramari alterna aquests modes, de manera que **les trames de desautenticació que arribin durant els ~3 segons d'escaneig no es capturen**. *Un atacant que sincronitzés les ràfegues amb les finestres d'escaneig podria esquivar la detecció*, tot i que necessitaria conèixer l'horari d'escaneig del dispositiu.

### Només 2,4 GHz

La ràdio ESP32 funciona a 2,4 GHz. **No escaneja ni supervisa xarxes de 5 o 6 GHz.** *En entorns on l'atac utilitza evil twins de 5 GHz, el dispositiu no els detectarà.*

### Abast passiu

La detecció de desautenticació exigeix que el dispositiu sigui dins l'abast de recepció de les trames. *Un atacant llunyà o amb antena molt direccional, o que ataqui un client situat lluny del canari, pot no generar senyals prou forts per activar els comptadors.*

---

## Casos d'ús

### Viatges amb feina sensible

El canari està pensat sobretot per viatjar. Connecta'l a l'USB d'un portàtil, a una presa USB d'una habitació d'hotel o a una bateria portàtil, i deixa que aprengui l'entorn de l'hotel o del centre de conferències. Si després apareix una còpia oberta del SSID de l'hotel, el cas d'atac més habitual, com a mínim indicarà precaució.

### Cafeteries i WiFi pública

Els entorns WiFi oberts són la superfície d'atac més habitual per als evil twins. La línia base permet aprendre quin és l'AP legítim de la cafeteria en arribar i vigilar l'aparició de SSID competidors.

### Conscienciació i formació en seguretat

La sortida sèrie ofereix un registre detallat i llegible del que detecta. En una formació, veure en temps real l'aspecte d'una ràfega de desautenticació i el canvi de color del LED és més efectiu que una presentació.

### Monitoratge passiu de laboratori

En un laboratori domèstic o una oficina petita, el canari pot funcionar com a monitor ambiental permanent. El LED mostra l'estat d'un cop d'ull sense exigir vigilància activa. El bolcat d'AP amb el botó permet veure sota demanda quines xarxes detecta el dispositiu.

---

## Notes d'arquitectura

### Per què una puntuació única en lloc d'alertes separades

El model de confiança agrupa senyals diferents en una sola xifra en lloc de mostrar categories d'alerta separades. És una decisió d'experiència d'usuari: la interfície és un LED amb tres estats. Una alerta independent per categoria exigiria una pantalla o una aplicació. *El model converteix senyals sorollosos i parcialment correlacionats en un únic indicador accionable.*

### Per què decau la puntuació

Sense decaïment, un fals positiu únic exigiria una intervenció manual, com prémer el botó. Amb un decaïment de 60 segons, les anomalies breus desapareixen soles en pocs minuts. **Això permet deixar el canari sense vigilància** en una bossa, una habitació d'hotel o un cotxe, i recuperar la línia base després d'esdeveniments transitoris.

### Per què tres escanejos de línia base

Un únic escaneig podria no detectar un AP que no emetia en aquell moment, per exemple durant una pausa d'escaneig o perquè estava apagat temporalment. *Tres escanejos durant uns 24 segons ofereixen una imatge més completa de l'entorn estable abans de començar el monitoratge.*

---

## Contribucions i estat del projecte

El projecte és a [github.com/simeononsecurity/esp32-wifi-canary](https://github.com/simeononsecurity/esp32-wifi-canary) sota una llicència d'ús passiu. El codi consta d'un únic fitxer `main.cpp`, de manera que és fàcil de llegir, auditar i ampliar.

Si treballes amb PlatformIO i ESP32, el projecte està preparat per compilar-se sense modificacions tant per a l'Atom Lite com per a entorns DevKit estàndard.

---

## Comparació amb altres mètodes de monitoratge WiFi

| Mètode | Passiu? | Sense credencials | Sortida amb un LED | Format de viatge |
|---|---|---|---|---|
| ESP32 WiFi Canary | ✅ | ✅ | ✅ | ✅ |
| Kismet (portàtil) | ✅ | ✅ | ❌ (necessita pantalla) | ❌ (pesat) |
| WiFi Pineapple | ❌ (actiu) | ❌ | ❌ | Parcial |
| IDS sense fil (empresa) | ✅ | ✅ | ❌ (necessita infraestructura) | ❌ |
| Escaneig manual (aplicació de telèfon) | Parcial | ✅ | ❌ | ✅ |

El canari ocupa un nínxol específic: **conscienciació ambiental permanent, sense interacció ni xarxa**, en un format que pot viure sempre en un clauer o una bossa d'ordinador.

---

## Conclusió

ESP32 WiFi Canary és una eina d'abast limitat que fa una sola cosa: observa l'entorn de 2,4 GHz i canvia de color quan alguna cosa sembla incorrecta. No vol ser un sistema complet de detecció d'intrusions sense fil, una eina de captura de paquets ni un analitzador forense. És un canari: un sensor passiu que avisa quan l'entorn es torna perillós.

El **model de puntuació de confiança**, el **decaïment de puntuació** i l'**enfocament de tres fases per a la línia base** demostren un disseny atent al problema dels falsos positius que afecta els sensors ambientals de seguretat. El resultat és un dispositiu que pot funcionar sense vigilància en un hotel o centre de conferències i avisar de situacions realment inusuals, sense reaccionar al moviment normal de les xarxes.

Si estàs preparant un equip de seguretat portàtil, treballes en entorns amb WiFi no fiable o busques un projecte ESP32 útil, WiFi Canary mereix una tarda i un M5Stack Atom Lite de 15 $.

**GitHub**: [github.com/simeononsecurity/esp32-wifi-canary](https://github.com/simeononsecurity/esp32-wifi-canary)

---
