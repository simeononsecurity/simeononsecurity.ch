---
title: "SenseCAP M1 Raspberry Pi Shield: pinout și reutilizare LoRaWAN"
date: 2026-09-12
lastmod: 2026-11-07
toc: true
draft: false
description: "Înțelege shield-ul SenseCAP M1, compară hărțile GPIO contradictorii, inspectează ATECC608 și planifică un gateway LoRaWAN cu o versiune modernă de Raspberry Pi OS."
genre: ["Raspberry Pi", "IoT", "Securitatea hardware-ului"]
tags: ["SenseCAP M1", "Shield SenseCAP M1", "Pinout SenseCAP M1", "Shield Raspberry Pi", "Raspberry Pi HAT", "Gateway LoRaWAN", "WM1302", "WM1303", "SX1302", "SX1303", "Seeed Studio", "Reutilizarea hotspotului Helium", "Concentrator LoRa", "SPI GPIO", "GPIO17", "LED GPIO22", "libgpiod", "Raspberry Pi OS", "ATECC608", "CryptoAuthLib", "Diagnosticare I2C", "STTS751", "LoRa Basics Station", "ChirpStack", "The Things Stack", "Inginerie inversă hardware"]
cover: "/img/cover/sensecap-wm1302-shield-hardware.webp"
coverAlt: "Shield SenseCAP M1 cu modul Seeed WM1302, conector Raspberry Pi, cablu de antenă, mufă USB-C și conector de ventilator"
coverCaption: "Fotografia plăcii: Clockwork Bird, 2023. Sursa și atribuirea apar la finalul articolului."
coverCredit: "Clockwork Bird"
coverCreditURL: "https://clockworkbird9.wordpress.com/2023/05/03/sensecap-m1-raspberry-pi-shield/"
---

**Shield-ul SenseCAP M1 este util ca hardware pentru un gateway LoRaWAN, dar cablajul lui cere mai multă atenție decât un tutorial generic pentru Raspberry Pi HAT.** Acest ghid extinde [investigația din 2023 a lui Clockwork Bird](https://clockworkbird9.wordpress.com/2023/05/03/sensecap-m1-raspberry-pi-shield/) cu documentația producătorului, examinarea unui driver upstream și recomandări GPIO actuale. Vei identifica hardware-ul, vei separa faptele confirmate de informațiile incomplete despre pinout și vei crea o fișă repetabilă de punere în funcțiune.

> **Domeniu:** Acesta este un ghid hardware bazat pe documentație. Comenzile și mapările plăcii nu au fost testate pe un M1 fizic pentru acest articol.

## Idei principale

- **Identifică ambele plăci:** suportul M1 și concentratorul detașabil au modele și revizii distincte.
- **Verifică scripturile de resetare:** valorile CoreCell implicite intră în conflict cu semnalele din pinout-ul M1 publicat.
- **Verifică interfețele sistemului:** fișierele dispozitiv SPI, numerotarea GPIO și versiunile uneltelor GPIO răspund la întrebări diferite.
- **Păstrează provisionarea elementului securizat:** citirea informațiilor dispozitivului diferă de configurarea lui sau generarea de chei.
- **Demonstrează întregul traseu:** detectarea unui concentrator nu dovedește livrarea datelor senzorului.

## Înainte să începi

**Dificultate: intermediară.** Rezervă aproximativ una sau două ore pentru inventariere, pregătirea sistemului și verificări documentare. Verificarea electrică, adaptarea driverului și implementarea serverului de rețea cer muncă suplimentară, mai ales dacă revizia plăcii nu este cunoscută.

| Element | Scop |
|---|---|
| **Shield M1 și concentrator** | Citește revizia suportului și eticheta completă a modulului |
| **Raspberry Pi 4** | Începe cu gazda folosită în proiectul M1 original |
| **Card microSD de rezervă** | Pregătește un alt sistem fără să pierzi instalarea originală |
| **Sursă și antenă potrivite** | Potrivește ansamblul și banda RF a modulului |
| **SSH sau consolă locală** | Înregistrează diagnosticarea și editează configurația |
| **Senzor și server LoRaWAN** | Verifică livrarea reală către aplicație după pornirea hardware-ului |
| **Multimetru și experiență hardware** | Rezolvă conexiunile nedocumentate înainte să le comanzi |

Fotografiază ambele fețe ale ansamblului nealimentat înainte să demontezi ceva. Notează orientarea conectorilor, șuruburile, distanțierele și traseul antenei. Păstrează cardul și configurația originală până când noua instalare trece verificările de acceptare.

## Identifică cele trei straturi

**M1 complet, suportul shield și concentratorul sunt componente diferite.** Seeed descrie hotspotul asamblat ca un Raspberry Pi 4 cu un concentrator WM1302/SX1302 sau WM1303/SX1303. O listare intitulată „SenseCAP M1 shield” nu stabilește care dintre aceste piese însoțește suportul. [Prezentarea generală M1 de la Seeed Studio](https://www.sensecapmx.com/docs/sensecap-m1/overview/)

**Suportul** conectează alimentarea și semnalele periferice între Pi și modul. **Concentratorul** gestionează recepția și transmisia radio. Un **forwarder de pachete** rulează pe gazdă și schimbă cu un server pachetele radio recepționate și downlink-urile programate. [Prezentarea generală SX1302 HAL de la Semtech](https://github.com/Lora-net/sx1302_hal)

De exemplu, un senzor de temperatură de pe raft trimite un uplink radio. Concentratorul îl recepționează, gazda îl redirecționează, iar serviciile de rețea și aplicație îl procesează. Pornirea Linux demonstrează numai partea gazdei din acest lanț.

Fotografia lui Clockwork Bird arată un suport M1 v1.1 cu un modul etichetat explicit `WM1302-SPI-EU868`. Folosește imaginea pentru a găsi etichetele de pe hardware-ul tău. Numerele de serie identifică echipamentul fotografiat, nu configurația altui gateway.

{{< figure src="m1-carrier-wm1302-board.webp" alt="Suport M1 verde cu modul WM1302 SPI EU868 etichetat, lângă USB-C, buton, mufă de ventilator și cablu de antenă" caption="Hardware M1 v1.1 fotografiat de Clockwork Bird, folosit și pentru coperta articolului" credit="Clockwork Bird" attr="Clockwork Bird, 2023-05-03" attrlink="https://clockworkbird9.wordpress.com/2023/05/03/sensecap-m1-raspberry-pi-shield/" >}}

## Conexiuni de alimentare și radio

**Tratează conectorul USB-C al M1 ca intrare de alimentare.** Producătorul specifică 5 V CC, 3 A pentru gateway-ul complet și identifică USB-C ca interfață a sursei. Denumirea de port de încărcare sugerează o baterie care nu apare în specificații. [Specificațiile SenseCAP M1](https://www.sensecapmx.com/docs/sensecap-m1/overview/)

Diagrama de bloc a producătorului separă sursa de 5 V de linia reglată de 3,3 V a modulului. Diferența contează la depanare: Pi-ul poate funcționa în timp ce concentratorul nu este alimentat. Nu injecta 5 V într-un pin de semnal și nu presupune că cele două intrări de alimentare sunt izolate una de alta.

**Variantele de modul SPI și USB cer conexiuni diferite la gazdă.** Documentația WM1302 de la Seeed descrie acces SPI direct pentru modelul SPI și o punte USB STM32L4 pentru modelul USB. Forma mini-PCIe descrie formatul modulului, în timp ce interfețele electrice documentate sunt SPI sau USB. O mufă de laptop cu aceeași formă nu dovedește compatibilitatea. [Documentația WM1302 de la Seeed](https://github.com/seeed-lora/WM1302-doc)

Înainte de alimentarea ansamblului, montează modulul cu sursa deconectată și conectează o antenă potrivită. Potrivește hardware-ul RF, antena și planul regional propus. Schimbarea numelui unui fișier de configurare nu modifică componentele RF, iar mufa de alimentare M1 nu dovedește compatibilitatea cu o variantă USB de concentrator.

{{< figure src="m1-power-spi-system-diagram.webp" alt="Diagramă de bloc ce conectează Raspberry Pi 4 la shield-ul M1 prin alimentare, SPI, GPIO și I2C" caption="Diagramă a producătorului SenseCAP reprodusă în articolul original al lui Clockwork Bird, care arată proiectarea WM1302" credit="Seeed Studio / SenseCAP, via Clockwork Bird" attr="Seeed Studio / SenseCAP, via Clockwork Bird" attrlink="https://www.sensecapmx.com/docs/sensecap-m1/overview/" >}}

## Citește cu atenție pinout-ul

**Înregistrează separat numerele GPIO BCM și pinii fizici ai conectorului.** De exemplu, BCM GPIO17 este pinul fizic 11 al conectorului Pi. Conectorul de margine al modulului adaugă un al treilea sistem de numerotare, deci numărul pinului de resetare nu este un număr GPIO Raspberry Pi.

Tabelul de mai jos transcrie conexiunile din imaginea adnotată a conectorului de la Clockwork Bird. Este o **referință comunitară**, nu o schemă completă emisă de producător și nici o măsurătoare a fiecărei revizii M1. Desenul folosește etichete `SX1262`, în timp ce scriptul generic de resetare Semtech folosește nume `SX1261`.

| Semnal în desen | BCM / pin fizic | Interpretare |
|---|---|---|
| **I2C SDA / SCL** | GPIO2 / 3, GPIO3 / 5 | Magistrală de administrare partajată |
| **Resetare SX1302** | GPIO17 / 11 | Candidat pentru resetarea concentratorului |
| **LED utilizator** | GPIO22 / 15 | Adnotare M1 |
| **SPI MOSI / MISO** | GPIO10 / 19, GPIO9 / 21 | Semnale de date SPI |
| **Ceas SPI** | GPIO11 / 23 | Semnal de ceas SPI |
| **Selectare SX1302** | GPIO8 / 24 | SPI0 CE0 |
| **Resetare SX1262** | GPIO5 / 29 | Candidat pentru resetarea radioului auxiliar |
| **Selectare SX1262** | GPIO6 / 31 | GPIO6, diferit de SPI0 CE1 |
| **SX1262 BUSY** | GPIO18 / 12 | Ieșire de stare a radioului auxiliar |
| **SX1262 IO1 / IO2** | GPIO23 / 16, GPIO24 / 18 | Semnale auxiliare de verificat înainte de utilizare |

Adnotările GPS/UART tăiate nu demonstrează că M1 are GPS. Nu include configurarea GPS dacă hardware-ul tău nu îl are. Diagrama publicată nu clarifică nici butonul utilizatorului, nici comanda ventilatorului. [Investigația pinout-ului de către Clockwork Bird](https://clockworkbird9.wordpress.com/2023/05/03/sensecap-m1-raspberry-pi-shield/)

{{< figure src="m1-community-header-pinout.webp" alt="Desen adnotat al conectorului Raspberry Pi cu LED M1, resetarea concentratorului, semnale SPI și conexiuni GPS tăiate" caption="Referință adnotată de comunitate, cu acoperire incompletă a reviziilor, nu o schemă completă M1" credit="Clockwork Bird" attr="Clockwork Bird, 2023-05-03" attrlink="https://clockworkbird9.wordpress.com/2023/05/03/sensecap-m1-raspberry-pi-shield/" >}}

## Rezolvă conflictele scripturilor de resetare

**Un script de resetare selectează ieșiri electrice, nu simple preferințe software.** `reset_lgw.sh` upstream de la Semtech vizează proiectul de referință CoreCell. Valorile implicite includ GPIO23 pentru resetarea concentratorului, GPIO18 pentru activarea alimentării, GPIO22 pentru resetare auxiliară și GPIO13 pentru resetarea AD5338R. [Sursa scriptului de resetare Semtech](https://github.com/Lora-net/sx1302_hal/blob/master/tools/reset_lgw.sh)

Instrucțiunile vechi de configurare Seeed schimbă cele două atribuiri de resetare la GPIO17 și GPIO5, dar păstrează celelalte intrări ale proiectului de referință. Compară valorile cu imaginea M1 adnotată înainte să urmezi exemplul. [Instrucțiuni de configurare WM1302 de la Seeed](https://github.com/seeed-lora/WM1302-doc)

| Atribuire | Dovezi contradictorii | Decizie necesară |
|---|---|---|
| **GPIO22 ca resetare auxiliară** | Imaginea M1 îl etichetează drept LED utilizator | Elimină presupunerea înainte să activezi LED-ul |
| **GPIO18 ca activare a alimentării** | Imaginea M1 îl etichetează drept BUSY auxiliar | Verifică rețeaua și direcția înainte să îl comanzi |
| **GPIO13 ca resetare DAC** | Scriptul generic numește alt proiect de referință | Stabilește dacă circuitul există |
| **Dispozitiv SPI auxiliar** | Imaginea M1 selectează GPIO6, nu CE1 | Confirmă rutarea selecției și compatibilitatea driverului |

**Inferență:** dacă GPIO18 se conectează la o ieșire radio auxiliară așa cum este desenat, configurarea părții Pi ca ieșire creează risc de conflict electric. Divergența impune verificare; nu dovedește daune sau un cablaj universal pentru toate M1.

Deconectează toate sursele de alimentare și urmărește conexiunile accesibile dintre conector și modul. Notează revizia plăcii și ambele capete. Continuitatea dovedește conectivitatea, iar documentația componentei stabilește direcția semnalului și limitele electrice.

Folosește diagrama modulului de mai jos pentru a nu confunda pinii conectorului de margine cu pinii Pi. Etichetele pentru radio auxiliar descriu referința publicată a modulului, nu același siliciu sau aceleași funcții pentru fiecare revizie. [Pinout-ul modulului WM1302 de la Seeed](https://github.com/seeed-lora/WM1302-doc/blob/master/pinout.jpg)

{{< figure src="wm1302-module-edge-connector.webp" alt="Diagramă Seeed cu ambele laturi ale conectorului de margine WM1302, alimentare, SPI, I2C și semnale radio auxiliare" caption="Numerotarea conectorului de margine al modulului diferă de numerotarea conectorului Raspberry Pi" credit="Seeed Studio" attr="Seeed Studio, WM1302-doc" attrlink="https://github.com/seeed-lora/WM1302-doc" >}}

## Pregătește Raspberry Pi OS

Înregistrează mediul gazdei pe instalarea de rezervă:

```bash
cat /etc/os-release
uname -r
tr -d '\0' < /proc/device-tree/model
```

Versiunea sistemului, kernelul și modelul Pi constituie punctul de pornire reproductibil. Notează-le înainte să compari rezultatele cu un tutorial vechi.

Instalează instrumentele de inspecție și compilare:

```bash
sudo apt update
sudo apt install git build-essential i2c-tools gpiod
sudo raspi-config
```

În **Interface Options**, activează SPI și I2C, apoi repornește. SPI deservește traseul concentratorului, iar I2C dispozitivele de administrare descrise mai jos. Nu prelua modificări GPS seriale fără legătură dintr-un tutorial pentru alt HAT.

Inspectează interfețele expuse:

```bash
ls -l /dev/spidev* /dev/i2c-*
i2cdetect -l
gpiodetect
gpioinfo
gpioset --version
```

Aceste comenzi listează nodurile de dispozitiv, adaptoarele, controlerele GPIO, liniile și versiunea instrumentului GPIO instalat. **`i2cdetect -l` listează adaptoarele fără să scaneze adrese.** Fișierul `/dev/spidev0.0` demonstrează că este expusă o interfață SPI, nu comunicarea cu un concentrator funcțional. [Manual i2c-tools](https://kernel.googlesource.com/pub/scm/utils/i2c-tools/i2c-tools/+/refs/tags/v4.3/tools/i2cdetect.8), [Recomandări GPIO Raspberry Pi](https://pip-assets.raspberrypi.com/categories/685-app-notes-guides-whitepapers/documents/RP-006553-WP/A-history-of-GPIO-usage-on-Raspberry-Pi-devices-and-current-best-practices)

### Ține cont de versiunile GPIO

**Nu copia numere GPIO globale de pe altă mașină.** Scripturile vechi scriu prin `/sys/class/gpio`, o interfață declarată învechită de documentația kernelului. Integrările noi din spațiul utilizatorului trebuie să folosească interfața GPIO character device cu controlerul și offset-ul liniei corecte. [Documentația Linux GPIO](https://www.kernel.org/doc/html/next/admin-guide/gpio/sysfs.html)

Verifică și `gpioset --help` înainte să adaptezi un script. Sintaxa și comportamentul proceselor diferă între versiunile 1 și 2. Instrumentul actual păstrează implicit liniile solicitate, dar contractul portabil nu garantează starea lor după ieșirea procesului. [Documentația gpioset libgpiod](https://libgpiod.readthedocs.io/en/master/gpioset.html)

Raspberry Pi documentează persistența ieșirilor în kernel și oferă opțiuni de modificare. Înregistrează configurația reală a kernelului în loc să presupui că fiecare Linux se comportă la fel. O numerotare nouă sau un instrument GPIO mai recent nu repară o mapare electrică greșită. [Ghid Raspberry Pi pentru GPIO](https://pip-assets.raspberrypi.com/categories/685-app-notes-guides-whitepapers/documents/RP-006553-WP/A-history-of-GPIO-usage-on-Raspberry-Pi-devices-and-current-best-practices)

## Testează LED-ul utilizatorului

După ce verifici că GPIO22 aparține LED-ului și elimini utilizările GPIO conflictuale, editează configurația de pornire:

```bash
sudoedit /boot/firmware/config.txt
```

Versiunile moderne Raspberry Pi OS montează configurația de pornire în **`/boot/firmware/config.txt`**. Imaginile vechi folosesc `/boot/config.txt`, calea din articolul din 2023. Fă o copie de siguranță a fișierului activ înainte să îl editezi. [Documentație Raspberry Pi config.txt](https://www.raspberrypi.com/documentation/computers/config_txt.html)

Adaugă overlay-ul LED într-o secțiune aplicabilă Pi-ului, precum `[all]`:

```ini
dtoverlay=gpio-led,gpio=22,label=lorawan,trigger=heartbeat
```

Parametrul **`gpio`** folosește numerotarea BCM. **`label`** denumește dispozitivul LED Linux, iar **`trigger=heartbeat`** selectează declanșatorul heartbeat al kernelului. Clockwork Bird raportează această atribuire pentru M1, iar referința overlay Raspberry Pi documentează parametrii. [Observația originală a LED-ului](https://clockworkbird9.wordpress.com/2023/05/03/sensecap-m1-raspberry-pi-shield/), [Referință overlay gpio-led](https://github.com/raspberrypi/linux/blob/rpi-6.12.y/arch/arm/boot/dts/overlays/README)

După repornire, inspectează LED-ul înregistrat:

```bash
ls -l /sys/class/leds/
cat /sys/class/leds/lorawan/trigger
```

Rezultatul așteptat este intrarea LED `lorawan` cu `heartbeat` selectat între paranteze drepte. LED-ul care clipește demonstrează traseul GPIO/driver. Nu confirmă înregistrarea LoRaWAN, recepția radio sau starea Helium.

## Examinează dispozitivele I2C

**O adresă I2C este un indiciu, nu identitatea dispozitivului.** Clockwork Bird a observat răspunsuri la `0x60` și `0x39`, apoi a citit informațiile ATECC608 prin biblioteca criptografică. Identificarea senzorului de temperatură rămânea provizorie în articolul original.

Începe cu lista adaptoarelor din secțiunea anterioară. Scanările largi `i2cdetect` trimit tranzacții de sondare, nu observă pasiv traficul, iar manualul upstream avertizează asupra posibilelor perturbări. Evită scanările de rutină ale unui gateway în funcțiune sau ale unor dispozitive conectate necunoscute. [Comportamentul de sondare i2c-tools](https://kernel.googlesource.com/pub/scm/utils/i2c-tools/i2c-tools/+/refs/tags/v4.3/tools/i2cdetect.8)

| Observație | Concluzie susținută | Întrebare nerezolvată |
|---|---|---|
| **Răspuns la `0x60`** | Un dispozitiv a recunoscut sondarea | Este elementul securizat așteptat? |
| **Răspuns la `0x39`** | Un dispozitiv a recunoscut sondarea | Ce componentă și revizie au răspuns? |
| **`UU` într-o scanare** | Un driver deține adresa, iar sondarea a fost omisă | Ce driver o deține? |
| **Fără răspuns** | Sondarea nu a primit confirmare | Alimentare, magistrală, proprietar sau protocol? |

### Clarifică pista senzorului de temperatură

**STTS751 este un candidat pentru `0x39` susținut de surse.** Antetul driverului de temperatură Semtech asociază explicit `0x39` cu `STTS751-0DP3F`. Aceasta întărește ipoteza originală fără să identifice toate plăcile populate la această adresă. [Antetul driverului Semtech STTS751](https://github.com/Lora-net/sx1302_hal/blob/master/libloragw/inc/loragw_stts751.h)

După identificarea unei componente compatibile și verificarea faptului că niciun alt proces nu o folosește, citește registrele de identificare:

```bash
sudo i2cget 1 0x39 0xfd b
sudo i2cget 1 0x39 0xfe b
```

Aici **`1`** selectează magistrala verificată, **`0x39`** dispozitivul și **`b`** cere o citire SMBus byte-data. Pentru STTS751-0, ID-ul de produs documentat la `0xFD` este `0x00`, iar ID-ul producătorului la `0xFE` este `0x53`. Tranzacțiile selectează adrese de registru, dar nu scriu valori de configurare. [Fișa tehnică STTS751, harta registrelor și registre de identificare](https://www.st.com/resource/en/datasheet/stts751.pdf)

Compară citirile cu marcajul cipului și documentația. O pereche potrivită adaugă dovezi pentru identificare; o eroare cere verificarea magistralei și a proprietarului înainte de schimbarea configurației hardware. Senzorul măsoară temperatura locală, diferită de temperatura procesorului Pi.

## Inspectează elementul securizat

**ATECC608 este o componentă de autentificare separată.** Tratează configurația, numărul de serie, cheia publică și materialul de cheie protejat ca noțiuni distincte. Citirea cheii publice nu dezvăluie cheia privată corespondentă.

**CryptoAuthLib** de la Microchip oferă interfața dispozitivului. Depozitul **cryptoauthtools** conține exemple bazate pe bibliotecă. Pregătește biblioteca nativă și binding-urile Python pentru sistemul țintă urmând instrucțiunile proiectelor înainte să rulezi un exemplu. Instalarea unui pachet Python fără legătură sau copierea unui singur script nu demonstrează că backend-ul I2C funcționează. [CryptoAuthLib Microchip](https://github.com/MicrochipTech/cryptoauthlib), [cryptoauthtools Microchip](https://github.com/MicrochipTech/cryptoauthtools)

Dintr-un director `cryptoauthtools/python/examples` pregătit, rulează comanda de inspecție din articolul original:

```bash
sudo python3 info.py -i i2c
```

Argumentul **`-i i2c`** selectează interfața. Într-un mediu virtual, folosește explicit interpretul Python al acestuia și asigură-te că găsește biblioteca nativă corespunzătoare. În multe instalări, `sudo python3` alege interpretul sistemului, ceea ce explică unele erori de import.

`info.py` analizat citește informații de revizie, numărul de serie, configurația și starea blocării. Dacă zona de date este blocată, încearcă să citească cheia publică din slotul 0. Nu rulează secvența de provisionare din exemplu. Eșecul izolat al citirii cheii publice din slotul 0 nu dovedește că dispozitivul este defect. [Sursa Microchip info.py](https://github.com/MicrochipTech/cryptoauthtools/blob/master/python/examples/info.py)

| Rezultat sau operație | Semnificație |
|---|---|
| **Configurație blocată** | Restricțiile de configurare sunt active |
| **Zona de date blocată** | Interpretează accesul conform politicilor sloturilor configurate |
| **Cheie publică afișată** | Au fost recuperate informații publice, nu exportată o cheie privată |
| **Rularea `config.py`** | Exemplu de provisionare cu configurare, blocare și generare de chei |

**Nu rula `config.py` ca să repari o eroare de inspecție.** Codul include scrieri de configurare, apeluri de blocare a zonelor și generare de chei. Calea implicită de generare contează și pe un dispozitiv deja configurat. [Sursa Microchip config.py](https://github.com/MicrochipTech/cryptoauthtools/blob/master/python/examples/config.py)

Profilurile de provisionare documentate de Microchip arată de ce o zonă de date blocată nu înseamnă că toate sloturile au permisiuni identice. Aceste profiluri nu stabilesc configurația exactă a M1. Păstrează configurația existentă și consultă documentația piesei potrivite înainte de o reutilizare ce implică chei. [Politicile Microchip pentru memorie și accesul la sloturi](https://onlinedocs.microchip.com/oxy/GUID-8F01540E-14A9-479E-9D27-FFFB14DE474E-en-US-2/GUID-92031846-201F-42DA-831D-FA3B6CF79B9B.html)

## Cercetează necunoscutele ventilatorului și butonului

**O mufă de ventilator cu trei pini nu stabilește tensiunea, polaritatea sau metoda de control.** Fotografiază numerotarea pinilor și citește eticheta ventilatorului. Confirmă conexiunile de alimentare și control înainte să conectezi un înlocuitor sau să alegi un overlay GPIO.

Investigația originală nu identifică nici GPIO-ul butonului. Caută un driver sau o configurație pentru revizia plăcii tale, apoi verifică legăturile cu alimentarea deconectată. Nu configura toate GPIO-urile aparent nefolosite ca ieșiri ca să găsești butonul.

| Periferic | Dovezi de adunat | Condiție de acceptare |
|---|---|---|
| **Alimentarea ventilatorului** | Ratingul ventilatorului, masa și alimentarea conectorului | Sursa măsurată respectă specificația ventilatorului |
| **Controlul ventilatorului** | Driver/configurație sau circuit de control urmărit | Comportament definit la pornire și la temperatură ridicată |
| **Buton utilizator** | Cablajul contactelor, maparea GPIO, polaritatea intrării | O apăsare intenționată produce evenimentul așteptat |

O instalare nouă a sistemului nu reproduce automat politica de răcire a aparatului original. La primul test prelungit, observă simultan ventilatorul și temperaturile. Păstrează fluxul de aer al carcasei și oprește testul dacă ansamblul pierde răcirea necesară.

## Alege stiva gateway-ului

**Separă suportul plăcii de protocolul serverului.** Un server LoRaWAN compatibil nu repară o rutină de resetare greșită sau o calibrare RF incorectă. Alege mai întâi software compatibil cu concentratorul, cablajul suportului, sistemul de operare și configurația regională.

| Opțiune software | Rol util | Verifică înainte de implementare |
|---|---|---|
| **Semtech SX1302 HAL** | Pornire la nivel de sursă și instrumente de diagnosticare | Rutină de resetare a plăcii și configurația modulului |
| **LoRa Basics Station** | Conexiune autentificată a gateway-ului la server | Integrare funcțională a plăcii și credențialele serverului |
| **ChirpStack Concentratord** | Serviciu dedicat concentratorului | Model compatibil, calibrare și mapare GPIO |

ChirpStack listează modelul SPI **`seeed_wm1302`**. Aceasta dovedește suportul modulului, nu o imagine M1 completă sau suport pentru fiecare revizie M1. Nu trata instrucțiunile separate de instalare SenseCAP M2 ca instrucțiuni de firmware M1. [Suport hardware ChirpStack](https://www.chirpstack.io/docs/chirpstack-concentratord/hardware-support.html), [Ținta de instalare Seeed ChirpStack](https://www.chirpstack.io/docs/chirpstack-gateway-os/install/seeed.html)

Pentru The Things Stack, documentația recomandă **LoRa Basics Station** în locul forwarder-ului UDP Semtech vechi. Station oferă TLS și autentificare cu token, plus funcții de configurare centralizată. Exemplele UDP ajută la înțelegerea transferului de pachete, dar setările adresei serverului nu oferă aceste protecții. [Recomandări UDP The Things Stack](https://www.thethingsindustries.com/docs/hardware/gateways/concepts/udp/), [Documentația LoRa Basics Station](https://www.thethingsindustries.com/docs/hardware/gateways/concepts/lora-basics-station/)

### Pregătește uneltele upstream

Compilează pe Pi-ul țintă într-un director nou de lucru:

```bash
git clone https://github.com/Lora-net/sx1302_hal.git
cd sx1302_hal
git rev-parse HEAD
make
```

Salvează identificatorul commit-ului împreună cu rezultatul compilării. O compilare reușită demonstrează compatibilitatea compilatorului, dar radioul are nevoie și de implementarea verificată a resetării și de configurația corectă. Documentația Semtech explică rolul HAL și al programelor auxiliare. [Documentația de compilare și unelte SX1302 HAL](https://github.com/Lora-net/sx1302_hal)

Examinează fișierul de resetare înainte să rulezi unelte care accesează hardware-ul:

```bash
sed -n '1,180p' tools/reset_lgw.sh
```

Nu copia fișierul nemodificat în directorul de execuție. Semtech documentează folosirea automată a scriptului de resetare de către programele sale de acces hardware, inclusiv uneltele de identificare. Verificarea ta trebuie să acopere fiecare pin alocat, direcția semnalului, API-ul GPIO și starea la pornire și oprire.

După verificarea plăcii, urmează instrucțiunile stivei alese pentru a citi EUI-ul concentratorului și a înregistra gateway-ul. Păstrează calibrarea modulului și setările RF când adaugi configurația serverului. În configurația UDP Semtech, `gateway_ID` reprezintă EUI-ul; Gateway ID din consola The Things Stack este identificatorul de înregistrare lizibil de oameni. [Configurația gateway-ului The Things Stack](https://www.thethingsindustries.com/docs/hardware/gateways/concepts/udp/)

## Demonstrează livrarea senzorului

**Folosește dovezi etapizate ca să găsești primul nivel care eșuează.** Marcarea gateway-ului ca online demonstrează o conexiune la server. Testul de acceptare are nevoie și de un senzor cunoscut, un plan de frecvență potrivit și un payload de aplicație decodat.

Secvența de mai jos este un plan de test propus, nu un rezultat măsurat pe M1:

| Punct de verificare | Dovezi de salvat | Semnificație |
|---|---|---|
| **Gazdă pregătită** | Sistem, kernel, alimentare și inventarul interfețelor | Pregătirea Linux s-a încheiat |
| **Concentratorul răspunde** | EUI și jurnal de inițializare reușită | Comunicarea gazdă-concentrator funcționează |
| **Recepție radio** | Pachetul așteptat de la senzor și metadate de recepție | Traseul de recepție configurat funcționează |
| **Serverul acceptă** | Eveniment gateway asociat senzorului | Forwarding-ul și rutarea serverului funcționează |
| **Decodare aplicație** | Măsurătoarea și marcajul temporal așteptate | Traseul aplicației funcționează |
| **Recuperare după restart** | Aceleași verificări după repornire | Configurația de pornire este reproductibilă |

Pentru un senzor **OTAA**, confirmă și schimbul de activare și uplink-ul ulterior. OTAA înseamnă activare over-the-air, procedura de asociere care stabilește o sesiune. Primirea unei cereri de asociere nu demonstrează că asocierea sau downlink-ul au reușit. [Documentația activării The Things Stack](https://www.thethingsindustries.com/docs/hardware/devices/concepts/abp-vs-otaa/)

**Diagnostic practic:** gateway-ul se conectează la server și raportează EUI-ul, dar senzorul nu apare. Prioritizează configurația de transmisie a senzorului, canalele de recepție alese, traseul antenei și jurnalele radio. Reprogramarea ATECC608 nu ar rezolva lipsa dovezilor din acest scenariu.

**Al doilea diagnostic:** un pachet al senzorului apare local, dar nu ajunge la aplicație. Corelează ora pachetului cu evenimentele gateway-ului și serverului, apoi verifică rutarea, înregistrarea dispozitivului și decodarea. Un pachet RF într-un jurnal nu este suficient ca să acuzi decodorul payload-ului înainte ca serverul să accepte evenimentul.

## Depanează după simptom

| Simptom | Verifică mai întâi | Următoarea acțiune |
|---|---|---|
| **Lipsește fișierul dispozitivului SPI** | Configurația activă de boot și setările interfeței | Activează interfața dorită și repornește |
| **SPI există, radioul eșuează** | Alimentarea, montarea, secvența de reset și selecția cipului | Verifică traseul electric înainte de schimbările serverului |
| **Eroare GPIO export** | Presupuneri sysfs vechi și kernel instalat | Folosește o implementare verificată pentru API-ul GPIO |
| **GPIO deja folosit** | Consumatorul afișat de `gpioinfo` | Rezolvă proprietatea înainte de o nouă încercare |
| **LED-ul nu merge după configurare** | Aplicarea overlay-ului și conflicte GPIO22 | Inspectează dispozitivele LED înregistrate și scriptul de reset |
| **Dispozitiv I2C absent** | Numărul magistralei, alimentarea și proprietarul actual | Investighează fără scanări largi repetate |
| **Importul bibliotecii crypto eșuează** | Interpretul, binding-urile și calea bibliotecii native | Repară mediul software |
| **Citirea cheii publice eșuează** | Politica slotului și citirile anterioare reușite | Verifică setările fără provisionare |
| **Ventilatorul nu pornește** | Alimentarea verificată și implementarea răcirii | Restabilește răcirea înaintea testelor prelungite |
| **Uplink-urile ajung, asocierea eșuează** | Traseul downlink și setările regionale/de dispozitiv | Urmărește răspunsul de asociere și ferestrele de recepție |

Tratează fiecare remediere ca un singur experiment. Salvează configurația anterioară, schimbă o variabilă, repetă aceeași verificare și notează dacă a apărut dovada așteptată.

## Creează fișa hardware

Folosește șablonul pentru un transfer de informații repetabil:

```text
Revizia suportului și fotografii:
Modelul concentratorului, interfața și banda RF:
Model gazdă / sistem / kernel / versiunea uneltei GPIO:
Sursă / antenă / configurație de răcire:
Maparea pinilor verificată și dovezi:
Rețele nerezolvate și funcții excluse:
Depozit software și commit:
Implementarea resetării și proprietarul GPIO:
EUI gateway / server / plan de frecvențe:
Activarea senzorului și dovezi pentru uplink-ul decodat:
Rezultatul recuperării după restart:
Locul cardului original și procedura de rollback:
```

**Exercițiu de decizie:** ai un suport simplu ieftin fără etichetă pentru modul și un ansamblu mai scump cu etichete lizibile și funcționare documentată. Alege ce se potrivește proiectului după ce incluzi în comparație Pi-ul, concentratorul, antena, sursa și timpul de verificare necesar. Alegerea potrivită depinde de costul total și dovezile cerute de serviciul vizat, nu doar de prețul suportului.

**Raționament așteptat:** un proiect de învățare tolerează cablaje nerezolvate dacă ai instrumente și timp. Un gateway pentru senzori operaționali cere pornire repetabilă, răcire, suport software și livrare demonstrată. Notează ce problemă nerezolvată ar opri implementarea.

## Pașii următori

Începe prin completarea fișei hardware și rezolvarea neconcordanțelor scriptului de resetare. Apoi pornește un senzor cunoscut și salvează dovezi până la decodarea aplicației înainte să adaugi alte dispozitive.

**Fișă de acceptare:** salvează revizia plăcii, eticheta modulului, banda radio, măsurarea sursei, dispozitivul SPI activ, numele liniilor GPIO, secvența de resetare, jurnalul concentratorului, conexiunea serverului și un uplink decodat. Marchează fiecare valoare ca observată, documentată sau încă presupusă. Nu considera pornirea unui proces dovadă a performanței RF sau a livrării către aplicație.

Dacă obiectivul tău este mesageria mesh, compară mai întâi rolurile protocoalelor în [ghidul nostru Meshtastic, MeshCore și Reticulum](/articles/meshtastic-vs-meshcore-vs-reticulum-comparison-guide/). Folosirea aceleiași tehnologii radio LoRa nu demonstrează compatibilitatea firmware-ului. Pentru mesagerie, consultă [documentația hardware-ului suportat de MeshtasticD](https://meshtastic.org/docs/meshtasticd/) în loc să tratezi această procedură LoRaWAN ca o conversie Meshtastic.

## Surse și credite pentru imagini

Cercetare verificată la 12 septembrie 2026. Linkurile nedatate la documente și depozite indică versiunile examinate pentru acest articol. Figurile locale își păstrează etichetele și atribuirea originale.

| Editor | Sursă și dată |
|---|---|
| **Clockwork Bird** | [SenseCAP M1 Raspberry Pi Shield](https://clockworkbird9.wordpress.com/2023/05/03/sensecap-m1-raspberry-pi-shield/), 2023-05-03. Fotografia plăcii, conector adnotat și diagramă de bloc a producătorului reprodusă |
| **Seeed Studio / SenseCAP** | [Prezentare și specificații M1](https://www.sensecapmx.com/docs/sensecap-m1/overview/), fără dată. Atribuirea diagramei originale |
| **Seeed Studio** | [Documentație WM1302 și pinout-ul modulului](https://github.com/seeed-lora/WM1302-doc), depozit |
| **Semtech** | [SX1302/SX1303 HAL](https://github.com/Lora-net/sx1302_hal), inclusiv sursele legate ale scriptului de resetare și driverului de temperatură |
| **Raspberry Pi** | [Configurație boot](https://www.raspberrypi.com/documentation/computers/config_txt.html), [ghid GPIO](https://pip-assets.raspberrypi.com/categories/685-app-notes-guides-whitepapers/documents/RP-006553-WP/A-history-of-GPIO-usage-on-Raspberry-Pi-devices-and-current-best-practices) și [referință overlay](https://github.com/raspberrypi/linux/blob/rpi-6.12.y/arch/arm/boot/dts/overlays/README) |
| **Linux / libgpiod** | [Interfața GPIO sysfs învechită](https://www.kernel.org/doc/html/next/admin-guide/gpio/sysfs.html) și [manualul gpioset](https://libgpiod.readthedocs.io/en/master/gpioset.html), acesta din urmă din august 2026 |
| **i2c-tools** | [Manual i2cdetect](https://kernel.googlesource.com/pub/scm/utils/i2c-tools/i2c-tools/+/refs/tags/v4.3/tools/i2cdetect.8), sursa v4.3 |
| **STMicroelectronics** | [Fișa tehnică STTS751](https://www.st.com/resource/en/datasheet/stts751.pdf), revizia 7 |
| **Microchip** | [CryptoAuthLib](https://github.com/MicrochipTech/cryptoauthlib), [cryptoauthtools](https://github.com/MicrochipTech/cryptoauthtools) și [documentația politicilor de acces la sloturi](https://onlinedocs.microchip.com/oxy/GUID-8F01540E-14A9-479E-9D27-FFFB14DE474E-en-US-2/GUID-92031846-201F-42DA-831D-FA3B6CF79B9B.html) |
| **ChirpStack** | [Suport hardware Concentratord](https://www.chirpstack.io/docs/chirpstack-concentratord/hardware-support.html) și [ținta de instalare Seeed](https://www.chirpstack.io/docs/chirpstack-gateway-os/install/seeed.html) |
| **The Things Industries** | [Forwarder UDP](https://www.thethingsindustries.com/docs/hardware/gateways/concepts/udp/), [LoRa Basics Station](https://www.thethingsindustries.com/docs/hardware/gateways/concepts/lora-basics-station/) și [activarea dispozitivului](https://www.thethingsindustries.com/docs/hardware/devices/concepts/abp-vs-otaa/) |
| **Meshtastic** | [Documentația MeshtasticD](https://meshtastic.org/docs/meshtasticd/), fără dată |
