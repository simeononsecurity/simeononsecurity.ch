---
title: "ESP32 WiFi Canary: detectarea pasivă a amenințărilor la 2,4 GHz"
date: 2026-06-06
lastmod: 2026-11-22
toc: true
draft: false
description: "Analiză tehnică a ESP32 WiFi Canary, un senzor pasiv de 2,4 GHz care detectează evil twin, deautentificarea, retrogradarea securității și inundarea cu beaconuri."
genre: ["Securitatea rețelelor", "Securitate WiFi", "Securitate IoT", "Cercetare în securitate", "Sisteme încorporate", "Instrumente de confidențialitate", "Proiecte ESP32", "Securitatea hardware", "Securitate wireless", "Securitate open source"]
tags: ["ESP32", "WiFi Canary", "M5Stack Atom Lite", "Detectarea deautentificării", "Detectarea evil twin", "Securitate WiFi", "Monitorizare pasivă WiFi", "Cadre de management 802.11", "Securitatea rețelelor", "Securitate IoT", "NeoPixel", "SK6812", "PlatformIO", "C++", "Software cu sursă deschisă", "Senzor de securitate", "Detectarea amenințărilor wireless", "Monitorizare BSSID", "Monitorizare SSID", "Detectarea retrogradării securității", "Detectarea inundării cu beaconuri", "Monitorizare WiFi", "LED RGB", "Mod promiscuous", "Securitate încorporată", "Securitate în călătorii", "Securitate WiFi la hotel", "WiFi în cafenele", "Conștientizare de securitate", "simeononsecurity"]
canonical: "https://simeononsecurity.com/articles/esp32-wifi-canary-passive-wifi-threat-detection-2026/"
cover: "/img/cover/esp32-wifi-canary-passive-wifi-threat-detection-2026.webp"
coverAlt: "Ilustrație a unui dispozitiv mic, asemănător cu ESP32 WiFi Canary, conectat la un port USB. LED-ul RGB luminează în culori diferite pentru a simboliza detectarea amenințărilor."
coverCaption: ""
---

**Un senzor pasiv WiFi de mărimea unui deget mare, care nu transmite niciodată**

## Problema rețelelor WiFi publice

Când te conectezi la WiFi-ul unui hotel, la hotspotul unei cafenele sau la rețeaua unui aeroport, presupui că punctul de acces este autentic. Problema este că **cadrele de management 802.11**, care anunță rețele, gestionează conexiuni și coordonează clienți, sunt *complet neautentificate în majoritatea implementărilor*. Cu hardware simplu, oricine poate clona un SSID, trimite cadre de deautentificare sau crea o rețea deschisă-capcană lângă o rețea WPA2 legitimă.

[**ESP32 WiFi Canary**](https://github.com/simeononsecurity/esp32-wifi-canary) este un senzor pasiv care face riscul vizibil într-un format foarte mic. Se montează pe M5Stack Atom Lite, aproximativ cât un cub de zahăr. Se conectează la USB, învață mediul și aprinde un LED RGB când detectează tipare asociate cu amenințări wireless.

Nu se conectează la nimic, nu colectează acreditări și nu transmite cadre. Observă, calculează un scor și comunică situația prin culoare.

Acest articol este o referință tehnică completă pentru proiect: ce detectează, cum funcționează modelul de încredere, cum se construiește și se programează, precum și limitele sale practice.

---

## Ce face și ce nu face ESP32 WiFi Canary

### Întotdeauna doar pasiv

WiFi Canary folosește două moduri radio, niciodată simultan:

1. **Mod promiscuous**: primește și inspectează cadre de management 802.11, precum deautentificarea și dezasocierea, fără să se asocieze la o rețea.
2. **Mod de scanare**: efectuează scanări WiFi active pentru a enumera punctele de acces din apropiere și a le compara cu o bază învățată.

Dispozitivul nu:
- se asociază sau conectează la o rețea;
- capturează cadre de date sau acreditări;
- transmite cadre 802.11;
- salvează date în memoria flash persistentă;
- comunică prin Internet.

**Tot ce învață rămâne în RAM și se șterge la repornire.** Este o alegere intenționată: canary-ul este un **senzor**, nu un dispozitiv de captură.

### LED-ul este interfața

Nu există ecran, aplicație sau interfață web. Întreaga ieșire este un singur **NeoPixel RGB SK6812** pe GPIO 27 al M5Stack Atom Lite. LED-ul indică patru stări:

| Starea LED-ului | Semnificație |
|---|---|
| 🔵 Albastru (puls lent) | Pornire, creare bază de referință |
| 🟢 Verde (constant) | Normal, fără probleme cu încredere ridicată |
| 🟡 Galben (constant) | Atenție, tipar suspect detectat |
| 🔴 Roșu (puls rapid) | Alertă, amenințare cu încredere mai ridicată detectată |

Pornirea durează aproximativ **24 de secunde** (3 scanări de câte 8 secunde). Când LED-ul nu mai este albastru, baza este gata și monitorizarea începe.

---

## Hardware

### Ținta principală: M5Stack Atom Lite

Proiectul este conceput pentru M5Stack Atom Lite, o platformă completă de dezvoltare ESP32 într-o carcasă de 24 × 24 mm.

| Componentă | Detaliu |
|---|---|
| MCU | ESP32-PICO-D4 |
| LED | Un NeoPixel RGB SK6812 (GPIO 27) |
| Buton | GPIO 39, activ pe nivel scăzut |
| USB | Punte UART CP2104 |
| Alimentare | USB-C, aproximativ 80–120 mA în timpul scanării |

**Nu este nevoie de breadboard, componente externe sau lipire.** Conectează-l la alimentarea USB și pornește.

### ESP32 DevKit generic pentru dezvoltare și testare

Proiectul include un al doilea mediu PlatformIO (`esp32dev`) pentru plăci ESP32 standard. În această configurație:

- LED-ul integrat pe GPIO 2 înlocuiește NeoPixel-ul;
- este activată ieșirea completă de depanare serială;
- logica de detectare funcționează identic cu versiunea Atom Lite.

Proiectul este astfel accesibil oricui are un ESP32 DevKit de 5 USD și permite testarea logicii fără hardware-ul țintă.

---

## Procesul de învățare a bazei

### De ce contează o bază

Un canary care alertează la fiecare rețea deschisă dintr-un oraș ar fi inutil. ESP32 WiFi Canary învață mai întâi mediul și abia apoi evaluează amenințările. Prima etapă construiește un **tabel de referință** cu punctele de acces legitime din zonă.

### Trei scanări, 24 de secunde

La pornire, dispozitivul efectuează trei scanări WiFi succesive, cu pauze între ele. După finalizare, salvează ca bază punctele de acces învățate: SSID, BSSID, tipul de criptare și puterea semnalului.

Ieșirea serială din această etapă arată astfel:

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

Când LED-ul trece de la albastru la verde, dispozitivul funcționează complet.

---

## Ce detectează: categorii de amenințări

WiFi Canary monitorizează șase tipare de amenințare. Fiecare adaugă puncte la un **scor de încredere** care controlează LED-ul. *Niciun indicator individual nu este considerat cert*: modelul adună dovezi care se confirmă reciproc înainte de escaladare.

### 1. Rafale de deautentificare și dezasociere

**Subtipurile 10 (dezasociere) și 12 (deautentificare) ale cadrelor de management 802.11** sunt instrumente uzuale în atacurile WiFi. Orice dispozitiv le poate trimite, iar clienții care le primesc sunt deconectați de la punctul de acces.

În **mod promiscuous**, canary-ul numără aceste cadre per adresă MAC sursă, într-o fereastră mobilă de **5 secunde**.

| Condiție | Puncte adăugate |
|---|---|
| ≥ 8 cadre de la o sursă în 5 s | +2 |
| ≥ 20 cadre de la o sursă în 5 s | +4 |
| ≥ 5 cadre de deautentificare broadcast | +1 |

**Pragurile contează**: un client care trece între puncte de acces generează câteva cadre legitime. Instrumentele de atac pot trimite sute de cadre pe secundă către o țintă. Fereastra de 5 secunde și pragul de 8 cadre filtrează zgomotul normal de roaming și detectează rafale susținute, precum cele produse de `aireplay-ng`.

### 2. Clonă deschisă a unei rețele criptate cunoscute (evil twin)

**Aceasta este detectarea cu cea mai mare încredere.** Un atac evil twin implică adesea:

1. Crearea unei copii deschise, fără parolă, a unui SSID WPA2 cunoscut.
2. Transmiterea unui semnal mai puternic decât punctul real, astfel încât clienții să se conecteze automat.

După învățarea bazei, o scanare nouă detectează un SSID care folosea doar WPA/WPA2/WPA3, dar apare acum ca **OPEN**:

| Condiție | Puncte adăugate |
|---|---|
| Același SSID, criptat înainte și deschis acum | +3 |
| BSSID absent din baza de referință | +1 |
| Semnalul clonei ≥ 10 dB mai puternic decât punctul cunoscut | +1 |

O clonă deschisă a WiFi-ului hotelului, cu semnal cu 10 dB mai puternic decât punctul real, este un exemplu clasic. *Această combinație ajunge la 5 puncte (Atenție) într-un singur ciclu de scanare.*

**Exemplu serial**:

```
[canary] OPEN CLONE: SSID='MyHomeWifi' baseline=WPA2 clone=OPEN bssid=de:ad:be:ef:00:01 rssi=-48/-52
[canary] score +4 → 4  "open clone of encrypted SSID 'MyHomeWifi'"
[canary] NORMAL → CAUTION  (score=4  "open clone of encrypted SSID 'MyHomeWifi'")
```

### 3. Punctul de acces criptat original lipsește, clona deschisă este prezentă

O variantă avansată: clona mai puternică atrage clienții, iar punctul real este în același timp eliminat prin deautentificare.

| Condiție | Puncte adăugate |
|---|---|
| Punctul criptat din bază a dispărut și a apărut o rețea deschisă corespunzătoare | +3 |

Acoperă situația în care punctul real încă transmite, dar pierde competiția puterii semnalului sau este perturbat activ.

### 4. Retrogradarea securității

Același SSID ca într-o intrare din bază este observat cu criptare mai slabă decât cea înregistrată.

| Condiție | Puncte adăugate |
|---|---|
| WPA3 → WPA2 | +1 |
| WPA2 → WPA | +1 |
| Scădere de cel puțin 2 niveluri de criptare | +3 |

*Retrogradările la o rețea deschisă sunt gestionate de detectarea evil twin și primesc scoruri mai mari.* Categoria acoperă retrogradări parțiale care pot scăpa unei comparații simple între deschis și criptat.

### 5. SSID duplicat de la un furnizor neașteptat

Același SSID și același tip de securitate ca un punct din bază, dar BSSID-ul are un **OUI de furnizor diferit** (primii 3 octeți ai adresei MAC).

| Condiție | Puncte adăugate |
|---|---|
| OUI diferit față de punctul din bază cu același SSID | +1 |
| Clona este și cu ≥ 10 dB mai puternică | +2 |

*Scorul este intenționat mic.* Rețelele de companie, sistemele mesh și punctele ISP pot avea legitim mai multe BSSID-uri pentru același SSID, de la furnizori diferiți. Semnalul trebuie adunat cu alte dovezi, nu trebuie să declanșeze singur alerta.

### 6. Inundare cu beaconuri sau SSID-uri

Numără SSID-uri noi, absente din bază, care apar într-o **fereastră mobilă de 30 de secunde**.

| Condiție | Puncte adăugate |
|---|---|
| ≥ 15 SSID-uri noi în 30 s | +2 |
| ≥ 30 SSID-uri noi în 30 s | +3 |

Atacurile de **inundare cu beaconuri** transmit mii de SSID-uri false pentru a deruta tabelele de scanare sau a perturba beaconurile legitime. Cincisprezece SSID-uri necunoscute în 30 de secunde sunt neobișnuite în majoritatea mediilor.

---

## Modelul scorului de încredere

Toate semnalele detectate contribuie la un **scor de amenințare** întreg, care controlează LED-ul:

| Interval scor | Stare LED |
|---|---|
| 0–2 | Normal (verde) |
| 3–5 | Atenție (galben) |
| 6+ | Alertă (roșu, puls rapid) |

### Scăderea scorului

Fără evenimente noi, scorul **scade cu 1 punct la fiecare 60 de secunde**. Este una dintre cele mai importante decizii practice de proiectare:

- O rafală de deautentificare ridică scorul la Atenție, apoi revine automat la Normal în câteva minute dacă atacul se oprește.
- Un atac susținut menține starea Alertă.
- Dispozitivul se resetează singur, fără intervenție sau repornire.

Asta înseamnă că:
- **Anomaliile scurte** (roaming sau variații temporare ale rețelelor vecine) se rezolvă singure.
- **Atacurile susținute** rămân semnalate.
- **Nu apare oboseala alertelor** pentru evenimente unice care nu se repetă.

### Resetare cu butonul

Butonul GPIO 39 de pe Atom Lite face două lucruri:

1. Trimite tabelul complet actual al punctelor de acces către ieșirea serială, pentru a audita ce vede dispozitivul.
2. Resetează scorul de amenințare la 0 și revine imediat la verde, pentru a observa următorul ciclu de scanare de la zero.

---

## Construire și flashare

### Cerințe

- **PlatformIO** (CLI sau extensia VS Code)
- **M5Stack Atom Lite** (sau ESP32 DevKit pentru testare)
- Cablu USB-C

### Flashare pe M5Stack Atom Lite

```bash
git clone https://github.com/simeononsecurity/esp32-wifi-canary.git
cd esp32-wifi-canary

# Construire et flasher
pio run -e atom-lite --target upload

# Deschide monitorul serial la 115200 baud
pio device monitor -b 115200
```

### Flashare pe ESP32 DevKit generic

```bash
pio run -e esp32dev --target upload
```

Buildul DevKit folosește GPIO 2 (LED-ul integrat) și afișează jurnalul serial complet. Nu controlează NeoPixel-ul. Logica de detectare este identică celei pentru Atom Lite.

### Structura proiectului

```
esp32-wifi-canary/
├── main.cpp              # Toată logica firmware
├── platformio.ini        # Medii de compilare (atom-lite, esp32dev)
├── partitions_4mb.csv    # Tabel de partiții flash de 4 MB
└── README.md
```

Firmware-ul complet se află într-un **singur fișier sursă C++**. Logica de detectare nu are biblioteci externe, ci doar frameworkul ESP32 Arduino pentru scanarea WiFi, callbackurile promiscuous și controlul NeoPixel.

### Mediile platformio.ini

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

Mediul `atom-lite` folosește definiția de placă `m5stick-c` (același cip ESP32-PICO-D4, cu pini compatibili pentru NeoPixel pe GPIO 27).

---

## Referința ieșirii seriale

Dispozitivul produce loguri detaliate la **115200 baud**. Toate liniile încep cu `[canary]`, pentru a fi filtrate ușor.

### Secvența de pornire

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

### Evenimente de detectare

```
[canary] normal scan start (aps=19 score=0)
[canary] scan found 21 APs
[canary] OPEN CLONE: SSID='HotelWiFi' baseline=WPA2 clone=OPEN bssid=de:ad:be:ef:00:01 rssi=-48/-52
[canary] score +4 → 4  "open clone of encrypted SSID 'HotelWiFi'"
[canary] NORMAL → CAUTION  (score=4  "open clone of encrypted SSID 'HotelWiFi'")
```

### Tranziții ale scorului

```
[canary] CAUTION → NORMAL  (score=2  "score decay")
[canary] NORMAL → ALERT    (score=6  "sustained deauth burst + open clone")
```

Jurnalul serial arată ce a observat dispozitivul, când și de ce s-a schimbat scorul. Este și un **jurnal de audit pasiv**, chiar dacă nu privești LED-ul.

---

## Note de detectare și limite practice

README-ul explică deschis ce nu poate face dispozitivul. Iată limitele în detaliu.

### Cauze posibile de alarme false

**Rețelele de companie și mesh** sunt cea mai mare sursă de alarme false. O rețea mare, un hotel sau un sistem mesh ca Eero ori Google WiFi poate prezenta în mod legitim:

- Mai multe BSSID-uri pentru același SSID, cu OUI-uri diferite.
- Configurații de securitate diferite între benzi.
- Puncte de acces care apar și dispar când rețeaua mesh se adaptează.

**Routerele Airbnb și SOHO** cu mai multe SSID-uri pentru benzi pot produce diferențe OUI dacă radiourile de 2,4 și 5 GHz folosesc blocuri MAC consecutive de la furnizori diferiți.

*Variații temporare ale rețelelor vecine*: o rețea criptată care dispare temporar din scanare și revine cu parametri diferiți (actualizare firmware, repornire sau reconfigurare) poate declanșa o detectare scurtă.

Scorul și scăderea lui sunt concepute să *reducă, nu să elimine*, alarmele false.

### Cauze posibile de rezultate fals negative

Un **atac evil twin bine realizat** care:

- Falsifică BSSID-ul exact al punctului legitim, astfel încât OUI-ul se potrivește.
- Folosește același tip de securitate și configurarea IE WPA2 corectă.
- Are semnalul la mai puțin de 10 dB față de punctul real.

*Poate să nu acumuleze suficiente puncte pentru pragul Atenție.* Deautentificarea necesară pentru a îndepărta clienții de la punctul real ar adăuga puncte, dar un atacator sofisticat care reduce numărul cadrelor poate rămâne sub prag.

### Pauza la schimbarea radioului

**Radioul ESP32 nu poate fi simultan în mod promiscuous și să scaneze activ punctele de acces.** Firmware-ul alternează între moduri. Prin urmare, **cadrele de deautentificare sosite în fereastra de scanare de circa 3 secunde nu sunt capturate**. Un atacator ar putea sincroniza rafalele cu aceste ferestre, dar ar trebui să cunoască programul de scanare.

### Doar 2,4 GHz

Radioul ESP32 funcționează la 2,4 GHz. **Rețelele de 5 și 6 GHz nu sunt scanate sau monitorizate.** Dispozitivul nu detectează evil twin care operează doar la 5 GHz.

### Raza pasivă

Detectarea deautentificării cere ca dispozitivul să recepționeze cadrele. Un atacator îndepărtat, cu antenă foarte direcțională sau care vizează un client departe de canary, poate transmite prea slab pentru a activa contoarele.

---

## Cazuri de utilizare

### Călătorii cu muncă sensibilă

Canary-ul este conceput mai ales pentru călătorii. Conectează-l la laptop, la un port USB de hotel sau la o baterie externă și lasă-l să învețe mediul hotelului sau al centrului de conferințe. Apariția ulterioară a unei clone deschise a SSID-ului hotelului, cel mai comun scenariu de atac, declanșează cel puțin Atenție.

### Cafenele și WiFi public

Mediile WiFi deschise sunt ținte frecvente pentru evil twin. Baza învață punctul legitim al cafenelei la sosire, apoi urmărește SSID-uri concurente.

### Conștientizare și instruire în securitate

Ieșirea serială oferă un jurnal detaliat și lizibil cu ceea ce observă. În instruire, demonstrarea unei rafale de deautentificare în timp real și urmărirea schimbării culorii LED-ului sunt mai eficiente decât o prezentare.

### Monitorizare pasivă de laborator

Într-un laborator de acasă sau birou mic, canary-ul poate funcționa ca monitor ambiental permanent. LED-ul oferă starea dintr-o privire, iar butonul afișează la cerere tabelul actual al rețelelor.

---

## Note despre arhitectură

### De ce un singur scor, nu alerte separate

Modelul însumează semnale diferite într-un singur număr, în loc să prezinte categorii separate de alerte. Este o alegere intenționată de interfață: dispozitivul are un LED cu trei stări. Alertele separate ar cere ecran sau aplicație. *Scorul transformă semnale zgomotoase și parțial corelate într-un indicator practic.*

### De ce scade scorul

Fără scădere, un singur fals pozitiv ar cere resetare manuală. Cu scădere la fiecare 60 de secunde, anomaliile scurte dispar în câteva minute. **Astfel, canary-ul funcționează nesupravegheat** într-o geantă, cameră de hotel sau mașină și revine la normal după evenimente temporare.

### De ce trei scanări pentru bază

O singură scanare poate rata un punct care nu transmitea în acel moment, de exemplu din cauza unei pauze sau a unei întreruperi de curent. *Trei scanări în aproximativ 24 de secunde oferă o imagine mai completă a mediului stabil înainte de începerea monitorizării.*

---

## Contribuții și starea proiectului

Proiectul este disponibil pe [github.com/simeononsecurity/esp32-wifi-canary](https://github.com/simeononsecurity/esp32-wifi-canary), sub o licență pentru utilizare pasivă. Codul este într-un singur `main.cpp`, ușor de citit, auditat și extins.

Cei care folosesc PlatformIO și ESP32 pot compila proiectul fără modificări pentru Atom Lite și DevKit standard.

---

## Comparație cu alte metode de monitorizare WiFi

| Metodă | Pasivă? | Fără acreditări | Ieșire cu un singur LED | Format de călătorie |
|---|---|---|---|---|
| ESP32 WiFi Canary | ✅ | ✅ | ✅ | ✅ |
| Kismet (laptop) | ✅ | ✅ | ❌ (necesită ecran) | ❌ (greu) |
| WiFi Pineapple | ❌ (activă) | ❌ | ❌ | Parțial |
| IDS wireless (companie) | ✅ | ✅ | ❌ (necesită infrastructură) | ❌ |
| Scanare manuală (aplicație pe telefon) | Parțial | ✅ | ❌ | ✅ |

Canary-ul ocupă o nișă precisă: **conștientizare ambientală permanentă, fără interacțiune sau rețea**, într-un format ce încape la chei sau în geanta laptopului.

---

## Concluzie

ESP32 WiFi Canary face un singur lucru: observă mediul de 2,4 GHz și își schimbă culoarea când ceva pare suspect. Nu este un sistem complet de detectare a intruziunilor wireless, un instrument de captură de pachete sau un analizor criminalistic. Este un canary, un senzor pasiv care observă când mediul devine periculos.

**Modelul scorului de încredere**, **scăderea scorului** și **baza în trei faze** abordează problema alarmelor false a senzorilor ambientali. Dispozitivul poate funcționa nesupravegheat într-o cameră de hotel sau centru de conferințe și semnala anomalii importante fără a reacționa la schimbările normale ale rețelei.

Pentru cei care pregătesc un kit de securitate portabil, lucrează cu infrastructură WiFi nesigură sau caută un proiect ESP32 util, WiFi Canary merită o după-amiază și un M5Stack Atom Lite de 15 USD.

**GitHub**: [github.com/simeononsecurity/esp32-wifi-canary](https://github.com/simeononsecurity/esp32-wifi-canary)
