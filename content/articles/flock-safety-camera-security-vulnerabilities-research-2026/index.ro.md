---
title: "Vulnerabilitățile camerelor Flock Safety: peste 50 de deficiențe descoperite"
date: 2026-05-24
lastmod: 2026-11-15
toc: true
draft: false
description: "Cercetarea vulnerabilităților camerelor Flock Safety analizează credențiale expuse, protecții slabe, riscuri legate de accesul fizic și limitele divulgării."
genre: ["Cercetare de securitate", "Analiza vulnerabilităților", "Tehnologie de supraveghere", "Securitate cibernetică", "Protecția vieții private", "Securitatea IoT", "Securitate fizică", "Securitatea rețelelor", "Infrastructură critică", "Tehnologie guvernamentală"]
tags: ["Vulnerabilități Flock Safety", "Securitate ALPR", "Compromiterea camerelor", "Deficiențe de securitate IoT", "Parole codificate direct în cod", "Vulnerabilități Android Things", "Exploatare prin acces fizic", "Securitatea rețelelor", "Deficiențe de criptare", "Încălcări ale confidențialității datelor", "Divulgări CVE", "Cercetare de securitate", "Cercetare GainSec", "Investigația lui Ben Jordan", "Securitatea camerelor de supraveghere", "Deficiențe ale tehnologiei guvernamentale", "Vulnerabilități critice", "Divulgare responsabilă", "Analiză de securitate cibernetică", "Tehnologie pentru poliție", "Siguranță publică", "Punct de acces wireless", "Ocolirea autentificării", "Credențiale în text simplu", "Scurgere RF", "Atac Tempest", "Divulgare de informații", "Acces la shell root", "Execuție de cod la distanță", "Audit de securitate", "Evaluarea vulnerabilităților", "Risc pentru securitatea națională", "Investigație a Senatului", "Program de recompense pentru erori", "Vulnerabilitate zero-day", "Dezvoltarea exploatărilor", "Testare de penetrare", "Raport tehnic de securitate", "Relatarea 404 Media", "Cercetare independentă", "Securitate hardware", "Analiza firmware-ului", "Exploatarea sistemelor"]
cover: "/img/cover/flock-safety-camera-security-vulnerabilities-research-2026.webp"
coverAlt: "O cameră de supraveghere avansată apare pe un fundal întunecat, cu accente albastre și verzi. Formele și liniile abstracte din jur reprezintă vulnerabilități de securitate digitală."
coverCaption: "Deficiențe critice expun peste 80.000 de camere de supraveghere la acces neautorizat"
canonical: "https://simeononsecurity.com/articles/flock-safety-camera-security-vulnerabilities-research-2026/"
---

**Peste 50 de vulnerabilități critice expun cea mai mare rețea privată de supraveghere din țară**

## Introducere: o criză de securitate națională

La sfârșitul lui 2024 și pe parcursul lui 2025, cercetători independenți de securitate au descoperit ceea ce ar putea fi **cel mai grav eșec de securitate din istoria tehnologiei de supraveghere a forțelor de ordine din Statele Unite**. În sistemele de camere Flock Safety au fost găsite peste **50 de vulnerabilități critice**. Aceleași camere fotografiază și urmăresc peste **150 de milioane de vehicule pe zi**, în mai mult de **80.000 de puncte de instalare** din țară.

Acest articol prezintă o analiză tehnică amplă a vulnerabilităților, bazată pe:

- **Raportul tehnic oficial GainSec**, „Examining the Security Posture of an Anti-Crime Ecosystem” (51 de constatări, 22 de CVE-uri atribuite și 8 în așteptare)
- **Investigațiile jurnalistice ale lui Ben Jordan** și testele sale practice de securitate
- **Relatările 404 Media** despre fluxuri video expuse public
- **Răspunsurile oficiale** ale Flock Safety și ale senatorilor americani
- **Divulgările publicate în National Vulnerability Database (NVD)**
- **Imaginea sistemului de fișiere publicată în septembrie 2026** de organizația Distributed Denial of Secrets, cu analiza tehnică detaliată a lui Micah Lee și o investigație comună WIRED și 404 Media

Pentru a înțelege **de ce există aceste camere** și **implicațiile pentru viața privată**, consultă articolul nostru: **[Supravegherea cu camere Flock Safety: prevalență, preocupări privind confidențialitatea și strategii de protecție](/articles/flock-safety-camera-surveillance-prevalence-privacy-protection-2026/)**

Pentru a afla **cum să detectezi aceste camere**, consultă: **[Proiectul de detectare Flock-You: ghid de hardware contra supravegherii](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/)**

______

## Amploarea problemei

### Dimensiunea infrastructurii vulnerabile

În mai 2026:

- **Peste 80.000 de camere Flock Safety** instalate în Statele Unite
- **Peste 5.000 de orașe și localități** folosesc serviciile Flock
- **Peste 3.500 de agenții de aplicare a legii** au acces la sistem
- **Peste 22.000 de utilizatori din forțele de ordine** accesează bazele de date
- **Miliarde de puncte de date** stocate în baze de date cu funcție de căutare

### Cronologia vulnerabilităților

- **Sfârșitul lui 2024**: cercetătorul de securitate Jon „GainSec” Gaines descoperă vulnerabilitățile inițiale
- **Februarie 2025**: începe divulgarea responsabilă către Flock Safety
- **Aprilie 2025**: sunt publicate primele atribuiri CVE
- **Noiembrie 2025**: este publicat raportul tehnic oficial cu 51 de constatări
- **Decembrie 2025**: Ben Jordan demonstrează vulnerabilitățile într-un videoclip
- **Ianuarie 2026**: 404 Media descoperă peste 60 de fluxuri video accesibile public
- **Februarie 2026**: senatorii americani cer o investigație FTC
- **Mai 2026**: procesul de divulgare continuă

### Categorii de vulnerabilități

Cele peste 50 de vulnerabilități se încadrează în mai multe categorii:

1. **Autentificare și autorizare** (parole codificate direct, lipsa MFA)
2. **Criptografie și criptare** (date necriptate în repaus și în tranzit)
3. **Securitatea rețelelor** (puncte de acces Wi-Fi expuse, credențiale în text simplu)
4. **Securitate fizică** (exploatări prin apăsarea butoanelor, porturi USB expuse)
5. **Confidențialitatea datelor** (colectare neautorizată, retenție extinsă)
6. **Proiectarea sistemului** (software învechit, controale de acces insuficiente)
7. **Divulgarea informațiilor** (chei API expuse, fluxuri publice ale camerelor)

______

## Imaginea sistemului de fișiere din septembrie 2026

**În septembrie 2026, organizația non-profit pentru transparență Distributed Denial of Secrets a publicat imagini complete ale sistemului de fișiere preluate de la o cameră Flock aflată în serviciu.** Un colectiv care se numește **stegan0gram** a desfăcut camera de pe stâlp, a copiat stocarea internă și a publicat imaginile. **404 Media** și **WIRED** au realizat o investigație comună, iar cercetătorul de securitate **Micah Lee** a publicat o analiză tehnică a conținutului.

Toate constatările anterioare din acest articol provin de la un dispozitiv de laborator al unui cercetător sau de la o unitate cumpărată. Acest set de date provine de la o cameră folosită activ de o municipalitate, ceea ce îl face cea mai solidă dovadă publicată până acum.

*Camera nu a fost compromisă prin rețea. A fost demontată fizic.*

### Ce conține imaginea

Publicarea include imagini ale trei partiții, fiecare cu o parte diferită din poveste.

| Partiție | Dimensiune | Relevanță |
|-----------|------|----------------|
| **system** | 1,5 GB | Imagine de sistem Android cu **19 aplicații create de Flock**, inclusiv `flock-sambuca`, `flock-collins` și `flock-phone-home` |
| **persist** | 32 MB | Credențiale ale dispozitivului în `flock/auth0/auth0_cred`, într-o **partiție necriptată, concepută să supraviețuiască unei resetări din fabrică** |
| **media** | 18 GB | Jurnale și imagini într-un container a cărui **cheie de decriptare este stocată pe aceeași partiție** |

### Problema credențialelor, confirmată

Imaginea clarifică dacă credențialele codificate direct sunt teoretice sau sunt folosite în dispozitivele instalate. Sunt folosite.

**O cheie API care acordă acces la backend-ul Flock este codificat directa în fișierele binare ale aplicațiilor.** Valoarea se află într-o clasă numită `CameraSettings`, în `com.flocksafety.android.common.lib`. Flock include biblioteca partajată în toate cele 19 aplicații, deci cheia este livrată în fiecare dintre ele. Aplicația `flock-sambuca` o folosește în timpul configurării.

**Fluxul de autentificare funcționează astfel:**

1. Fiecare cameră solicită credențiale de la un server Flock și se identifică prin **adresa MAC**
2. Serviciul de autentificare **Okta Auth0** al Flock returnează un `FlockAuth0Token` cu durată scurtă
3. Camera stochează credențialele primite **în text simplu**

ID-ul și secretul client Auth0 se află pe **partiția `/persist` necriptată**, într-un fișier conceput să supraviețuiască unei resetări din fabrică. Un atacator recuperează mai întâi partiția persist, deoarece nu este protejată.

[Vulnerabilitatea critică nr. 4](#critical-vulnerability-4-hardcoded-credentials-throughout-system) tratează modelul mai larg al secretelor codificate direct în platformă.

### Cheia de criptare livrată împreună cu lacătul

Flock descrie camerele ca fiind protejate prin **criptare la nivelul dispozitivului**. Imaginea arată cum funcționează implementarea în practică.

Partiția media de 18 GB se află într-un container criptat. Cheia de decriptare se află pe aceeași partiție, într-un fișier al cărui nume se termină în `.key`. Colectivul stegan0gram a recuperat cheia, a deblocat containerul și i-a citit conținutul. **Imaginile sunt criptate în același sens în care o cutie este încuiată când cheia este lipită cu bandă de capac.**

Jurnalele recuperate au dezvăluit și poziția camerei. Coordonatele GPS apar **de 155 de ori** în jurnale, grupate pe o rază de aproximativ 100 de metri, o variație normală pentru un receptor fixat pe un stâlp. Coordonatele indică **Wauwatosa, Wisconsin**, o suburbie a orașului Milwaukee, unde camera era instalată pe N Mayfair Road. Micah Lee a comparat jurnalele cu Google Street View și a identificat unitatea exactă după numărul de serie și adresa MAC.

*Criptarea datelor în repaus nu ajută dacă cheia este stocată lângă textul cifrat.*

### Ce a spus Flock

Răspunsul Flock a repetat poziția companiei față de constatările anterioare ale GainSec. Un purtător de cuvânt a declarat:

> „Flock tratează securitatea cu seriozitate și menține o Politică publică de divulgare a vulnerabilităților, prin care cercetătorii de securitate ne pot raporta direct potențiale vulnerabilități. Nu am primit niciun raport prin acel proces și, pe baza informațiilor limitate furnizate, nu avem detalii suficiente pentru a evalua afirmațiile făcute.”

Este dificil să împaci acest răspuns cu cronologia. Vulnerabilitățile sistemului de operare al camerei au fost remediate public în **2018 și 2021**, iar standardele pentru stocarea credențialelor și gestionarea cheilor existau cu mult înainte ca această cameră să fie livrată. **Verificarea unui deceniu de istoric public al vulnerabilităților nu necesită un raport extern.**

Flock a caracterizat și demontarea și analiza camerei drept ilegale, ceea ce este adevărat conform legislației actuale. Totuși, constatările de securitate se susțin independent de modul în care a fost obținut hardware-ul.

### De ce contează mai mult decât cercetarea anterioară

Raportul GainSec a documentat 51 de constatări privind dispozitive obținute legal. Flock a contestat gravitatea și a susținut că accesul necesita apropiere fizică.

Această imagine elimină acele rezerve. Starea implicită a unei camere de producție, fără modificări făcute de operatori, conține credențiale de infrastructură în text simplu, chei stocate lângă datele pe care ar trebui să le protejeze și un sistem de operare fără opt ani de actualizări de securitate. **Nimic din toate acestea nu a necesitat o exploatare. A fost nevoie de o cheie franceză.**

______


## Flota de dispozitive

Flock vinde o gamă de produse, nu o singură cameră, iar caracteristicile de securitate diferă între dispozitive. Specificațiile de mai jos provin din demontările GainSec și din analiza firmware-ului compilată de comunitatea de detecție **[WiFi Mothership](https://wifimothership.com/flock)**.

| Dispozitiv | Rol | Platformă | Sistem de operare |
|--------|------|----------|-----|
| **Falcon** | Cameră ALPR alimentată solar | Qualcomm MSM8953 (Snapdragon 625) / OpenQ 624A SoM | Android 8.1 |
| **Sparrow** | Cameră ALPR alimentată prin cablu | La fel ca Falcon | Android 8.1 |
| **Raven** | Detecție audio a focurilor de armă și a apelurilor de ajutor | ESP32-WROOM-32D cu DSP Syntiant NDP120-B0 | FreeRTOS / ESP-IDF |
| **Bravo** | Unitate de calcul AI la marginea rețelei | Qualcomm QCS6490 / TurboX QCS6490-U8B | **Android 13, kernel 5.4.180** |
| **Picard** | Unitate de calcul veche | Înlocuită treptat de Bravo | |
| **Condor** | Cameră PTZ | Documentată incomplet | |
| **Alpha** | Dronă autonomă | Proiectată de Flock, conformă cu NDAA | Pilot automat proprietar |
| **Aerodome M350** | Dronă veche | DJI Matrice M350 / M300 RTK | Firmware DJI |
| **Remorca LPR (ATS-5)** | Platformă ALPR mobilă | Șasiu All Traffic Solutions cu o cameră Flock | La fel ca Falcon |
| **Wing** | Punte software pentru camere terțe | Niciuna, învelește camere IP existente | |

*Diferența dintre generații sare prima în ochi. Unitatea de calcul rulează Android 13, în timp ce camerele pe care le deservește folosesc Android 8.1, un sistem de operare lansat în 2017.*

**Falcon merită urmărită.** Gestionează sarcina ALPR, încă rulează Android 8.1 și stochează date pe **eMMC necriptat de 32 GB**. Același eMMC conținea imaginile și jurnalele recuperate de colectivul stegan0gram. Sparrow folosește aceeași platformă, dar este alimentată prin cablu.

**Bravo este cazul opus.** O unitate de calcul modernă, care rulează Android 13 și execută inferență AI pentru fluxurile camerelor, arată că firma alege să livreze software actualizat atunci când dorește.

## Identificatori CVE verificați

Au fost atribuite cincisprezece CVE-uri familiilor Falcon, Sparrow, Raven și Bravo. Am verificat fiecare identificator de mai jos în **înregistrarea CVE.org** în septembrie 2026, nu l-am preluat dintr-o sursă secundară.

### Dispozitive de detecție a focurilor de armă și audio

| CVE | Constatare | CVSS |
|-----|---------|------|
| **CVE-2025-47818** | Parolă codificată direct pentru o conexiune | 2.2 |
| **CVE-2025-47819** | Interfață de depanare pe cip cu control de acces necorespunzător | 6.4 |
| **CVE-2025-47820** | Stocare necriptată a codului | 2.0 |
| **CVE-2025-47821** | Parolă de sistem codificată direct | 2.2 |

Toate patru afectează dispozitivele de detecție a focurilor de armă **anterioare versiunii 1.3**.

### Camere de recunoaștere a numerelor de înmatriculare

| CVE | Constatare | CVSS |
|-----|---------|------|
| **CVE-2025-47822** | Interfață de depanare pe cip cu control de acces necorespunzător | 6.4 |
| **CVE-2025-47823** | Parolă de sistem codificată direct | 2.2 |
| **CVE-2025-47824** | Stocare necriptată a codului | 2.0 |

Aceste trei vulnerabilități afectează firmware-ul camerelor de recunoaștere a numerelor de înmatriculare **până la versiunea 2.2 inclusiv**.

### Defecte ale aplicațiilor din întreaga flotă

| CVE | Constatare | CVSS |
|-----|---------|------|
| **CVE-2025-59403** | Aplicația Collins expune puncte finale administrative pe **portul 8080 fără autentificare**: `/reboot`, `/logs`, `/crashpack` și `/adb/enable`. Ultimul pornește ADB prin TCP fără confirmare de depanare, oferind atacatorului din aceeași rețea acces la un shell | **9.8 CRITIC** |
| **CVE-2025-59407** | Aplicația DetectionProcessing include un keystore Java și **parola inclusă direct în cod**. Keystore-ul conține o cheie privată | **9.8 CRITIC** |
| **CVE-2025-59405** | Aplicația Peripheral conține o cheie API DataDog în text simplu | 7.5 |
| **CVE-2025-59409** | Firmware-ul de producție Falcon și Sparrow livrează **date de autentificare Wi-Fi de dezvoltare în text simplu** | 7.5 |
| **CVE-2025-59406** | Aplicația Pisco include un **secret de client Auth0** în text simplu | 6.2 |

### Unitatea de calcul Bravo

| CVE | Constatare | CVSS |
|-----|---------|------|
| **CVE-2025-59402** | Acceptă încărcătorul Firehose implicit Thundercomm TurboX 6490, ceea ce permite scrierea firmware-ului și extragerea partițiilor | 5.4 |
| **CVE-2025-59404** | Este livrată cu bootloader-ul deblocat, ocolind Android Verified Boot | 7.5 |
| **CVE-2025-59408** | Este livrată cu Secure Boot dezactivat | 7.3 |

**Patru dintre aceste CVE-uri au vector de atac prin rețea și scor de cel puțin 7.5. Niciuna nu necesită acces fizic.** CVE-2025-59403 este identificatorul atribuit căii API fără autentificare și include apelul `/adb/enable`, de care depinde [Vulnerabilitatea critică nr. 1](#critical-vulnerability-1-button-press-wireless-access-point) pentru a obține un shell root.

*Înregistrările CVE contează și dintr-un al doilea motiv. Registre independente confirmă problema secretelor în text simplu, nu doar articolele cercetătorilor, iar pagina de alertă de securitate a Flock este citată în înregistrările pentru Raven și LPR.*

______

## Vulnerabilitatea critică nr. 1: punct de acces wireless activat prin apăsarea unui buton {#critical-vulnerability-1-button-press-wireless-access-point}

### CVE-2025-59403

**Gravitate**: CRITICĂ (CVSS 9.8)

### Exploatarea

Cea mai alarmantă vulnerabilitate descoperită permite **oricui are acces fizic** la o cameră Flock Safety să obțină control complet în mai puțin de 60 de secunde:

**Pasul 1**: Apasă de **trei ori** butonul de pe spatele camerei Falcon/Sparrow
**Pasul 2**: Dispozitivul creează un punct de acces Wi-Fi deschis
**Pasul 3**: Conectează-te la rețeaua Wi-Fi (parola codificată direct este documentată în raportul GainSec)
**Pasul 4**: Trimite comanda de activare ADB (Android Debug Bridge)
**Pasul 5**: Conectează-te prin ADB și obține acces la un shell root

### Detalii tehnice

```
Dispozitiv: cameră ALPR Flock Safety Falcon/Sparrow
Hardware: Android Things 8.0/8.1 (suport încheiat în 2021)
Vector de atac: secvență de apăsări fizice ale butonului
Autentificare: parolă WiFi codificată în firmware (identică pe toate dispozitivele)
Impact: compromiterea completă a dispozitivului, exfiltrarea datelor și instalarea de programe malware
```

### Ce permite

După obținerea accesului la shell, atacatorul poate:
- **Extrage toate imaginile stocate**, inclusiv imagini cu oameni, nu doar vehicule
- **Modifica sau șterge probele** stocate pe dispozitiv
- **Instala malware persistent**, care supraviețuiește repornirilor
- **Clona identitatea dispozitivului** pentru falsificare
- **Intercepta și modifica** fluxurile video
- **Folosi dispozitivul ca client într-o botnet** pentru atacuri DDoS
- **Captura datele de autentificare Wi-Fi** ale dispozitivelor din apropiere prin atacuri de tip honeypot
- **Dezactiva camera** sau provoca refuzul serviciului

### Demonstrație

Cercetătorul în securitate Ben Jordan a demonstrat exploatarea pe YouTube și a arătat:
- Conectarea la punctul de acces Wi-Fi în **mai puțin de 30 de secunde**
- Obținerea accesului la shell root în **mai puțin de 60 de secunde în total**
- Acces complet la sistemul de fișiere, imaginile stocate și memoria sistemului
- Posibilitatea de a instala aplicații Android arbitrare

**Citat din demonstrație**:
> „Parola pentru acel punct de acces este [REDACTED], scrisă cu litere mici. Toate camerele pe care le-am încercat aveau aceeași parolă codificată direct. Apoi îi trimiți o comandă pentru a activa ADB... în mai puțin de 30 de secunde poți obține un shell pe dispozitiv și acces complet la el.”

### Răspunsul furnizorului

Inițial, Flock Safety a susținut că vulnerabilitatea afecta doar **dispozitivele neconectate la cloud**, comparându-le cu **„un iPhone furat din camion înainte să fie conectat”**.

*Cercetătorii au infirmat afirmația.* Au reprodus vulnerabilitatea **pe dispozitive conectate la cloud**, pe mai multe modele de camere cu **aceeași vulnerabilitate** și pe dispozitive obținute din **surse diferite**. Toate prezentau defectul.

______

## Vulnerabilitatea critică nr. 2: sistem de operare Android învechit

### CVE-2025-47822 până la CVE-2025-47824

**Gravitate**: MEDIE până la SCĂZUTĂ (CVSS 6.4, 2.2 și 2.0)

### Problema

Camerele Flock Safety rulează **Android Things 8.0 sau 8.1**, care:
- A fost **întrerupt de Google în 2021**
- Nu a mai primit **actualizări de securitate din 2021**
- Are **peste 900 de vulnerabilități publicate** până în 2026
- Este **ieșit din suport de peste cinci ani**

### Analiză tehnică

**Sistem de operare**: Android Things 8.0/8.1
**Sfârșitul suportului**: ianuarie 2021
**Vulnerabilități cunoscute**: peste 900
**Actualizări de securitate**: niciuna de la sfârșitul suportului
**Dispozitive afectate**: camerele Falcon, Sparrow, Condor și unitățile de calcul Bravo

### Ce arată imaginea din septembrie 2026

Imaginile sistemului de fișiere publicate în septembrie 2026 dezvăluie versiunile exacte ale unei camere aflate în serviciu, nu ale unei unități de laborator.

| Componentă | Versiunea de pe cameră | Stare |
|-----------|----------------------|--------|
| **Android** | 8.1, versiune construită la 5 iunie 2025 | Nivelul actualizării de securitate **2018-06-05** |
| **Kernel Linux** | 3.18.71 | Lansat în 2017. Seria 3.18 s-a încheiat la versiunea 3.18.140 în mai 2019 |
| **Versiunea Android actuală** | Android 17, iunie 2026 | Cu nouă versiuni majore mai nouă |

Versiunea camerei în sine este recentă. **Sistemul de operare de dedesubt nu este**, iar nivelul de actualizare arată că dispozitivul nu a primit actualizări de securitate Android de **opt ani**. Kernelul este cu **69 de revizii de corecții în urma** ultimei versiuni a propriei ramuri de mentenanță, ceea ce înseamnă peste nouă ani fără remedieri.

### Două vulnerabilități prezente în această versiune

Micah Lee a identificat două defecte cunoscute public, care afectează componentele incluse în cameră. Datele corecțiilor demonstrează că firmware-ul camerei le precedă.

| CVE | Componentă | Efect | Corectată |
|-----|-----------|--------|---------|
| **CVE-2021-1905** | Driverul GPU Qualcomm Adreno | O utilizare după eliberare permite **oricărui cod de pe dispozitiv, inclusiv aplicațiilor fără privilegii, să corupă memoria kernelului și să preia controlul complet** | Mai 2021 |
| **CVE-2018-9568**, „WrongZone” | Gestionarea socketurilor în kernelul Linux | O confuzie de tip prin IPv6 permite unui program să **obțină privilegii root**. Cod de exploatare public este disponibil | Decembrie 2018 |

Ambele au fost corectate cu ani înainte de construirea firmware-ului acestei camere. **Niciuna nu depinde de acces fizic, deoarece ambele sunt accesibile prin software care rulează deja pe dispozitiv.** Condiția de proximitate invocată de Flock pentru a minimaliza constatările GainSec nu se aplică aici.

### Comparație cu dispozitivele de consum

Pentru perspectivă:
- **Telefonul tău** nu mai primește actualizări după aproximativ cinci ani, iar producătorii **încetează să-l mai vândă**
- O **cameră de securitate pentru locuință** cu software vechi de cinci ani ar fi considerată **critic vulnerabilă**
- Agențiile guvernamentale cer **software actualizat și acceptat** pentru sistemele sensibile

*Totuși, Flock Safety continuă să instaleze și să vândă camere cu software fără suport de la furnizor, fără actualizări de securitate, cu sute de exploituri cunoscute și care procesează date sensibile ale organelor de aplicare a legii.*

### De ce contează

Folosirea unui **software ieșit din suport** pe dispozitive de supraveghere înseamnă:
- **Orice vulnerabilitate publicată pentru Android 8.x** funcționează pe aceste camere
- **Codul de exploatare este disponibil public** pentru multe vulnerabilități
- **Nicio actualizare nu va remedia** problemele descoperite în viitor
- **Conformitatea cu reglementările** (FISMA, NIST, CMMC) devine imposibilă

______

## Vulnerabilitatea critică nr. 3: lipsa criptării în timpul funcționării

### CVE-2025-47824 și CVE-2025-59407

**Gravitate**: RIDICATĂ până la CRITICĂ (CVSS 2.0 până la 9.8)

### Afirmațiile Flock Safety și realitatea

**Site-ul Flock Safety afirmă**:
> „Datele și imaginile sunt criptate pe întregul ciclu de viață.”

**Constatările cercetătorilor independenți** (GainSec și Ben Jordan):
> „În toată cercetarea noastră, nu am decriptat și nu am spart nimic. Totul era necriptat în timpul funcționării.”

*Diferența dintre afirmația de marketing și realitatea tehnică este totală.*

### Ce nu este criptat

Când au examinat dispozitivele, cercetătorii au găsit următoarele **necriptate**:
1. **Înregistrări video și imagini stocate**
2. **Date și metadate despre numerele de înmatriculare**
3. **Date de autentificare Wi-Fi și chei API**
4. **Fișiere de baze de date cu înregistrări de detecție**
5. **Trafic de rețea** (vezi Vulnerabilitatea nr. 6)
6. **Jurnale de sistem cu informații sensibile**

### Contradicția privind păstrarea datelor

**Afirmația Flock Safety**: datele sunt eliminate automat după șapte zile.
**Constatările cercetării**: au fost găsite imagini datând **din momentul fabricării dispozitivului**, cu luni sau ani în urmă.

Fragment din raportul GainSec:
> „Am găsit imagini mai vechi de șapte zile. De fapt, imaginile stocate fuseseră capturate când camera s-a activat în fabrica unde a fost produsă.”

*Asta înseamnă că dispozitivele nu aplică politicile de confidențialitate declarate.*

### Implicații asupra confidențialității

Această deficiență a criptării înseamnă:
- **Furtul fizic al dispozitivului** provoacă o breșă imediată de date
- **Interceptarea rețelei** expune date în text simplu
- **Persoanele din interior cu intenții rele** pot exfiltra ușor date
- **Protecțiile asociate mandatelor** s-ar putea să nu se aplice datelor necriptate
- **Încălcarea cerințelor de conformitate** pentru numeroase reglementări (HIPAA, CCPA etc.)

______

## Vulnerabilitatea critică nr. 4: credențiale codificate direct în întregul sistem {#critical-vulnerability-4-hardcoded-credentials-throughout-system}

### CVE-2025-47818, CVE-2025-47821, CVE-2025-47823, CVE-2025-59407 și CVE-2025-59409

**Gravitate**: CRITICĂ (CVSS 9.8, limita superioară a intervalului)

### Categorii de secrete codificate direct

Cercetătorii de securitate au descoperit **numeroase credențiale codificate direct**:

#### 1. Parole pentru punctele de acces Wi-Fi

- **Parolă universală** pentru toate camerele Falcon/Sparrow
- **Utilizatorii și administratorii nu o pot schimba**
- **Cunoscută de cercetători** și publicată în raport tehnic (cu secțiuni redactate)
- **Confirmat de CVE-2025-59409**: firmware-ul de producție Falcon și Sparrow (build `OPM1.171019.026`) este livrat cu **credențiale Wi-Fi de dezvoltare în text simplu**

#### 2. Chei API și tokenuri

- **Codificate direct în firmware** și în codul aplicațiilor
- **Acordă acces la backend-uri** pentru diverse servicii
- **Găsite prin inginerie inversă** a APK-urilor Android
- **Confirmate de imaginea din septembrie 2026**: o cheie API pentru backend este codificată direct în `CameraSettings`, în `com.flocksafety.android.common.lib`, o bibliotecă partajată inclusă în **toate cele 19 aplicații Flock** de pe dispozitiv
- **ID-ul și secretul clientului Auth0 sunt stocate pe partiția `/persist` necriptată**, la `flock/auth0/auth0_cred`, într-o locație concepută să supraviețuiască resetării din fabrică
- **Credențialele returnate sunt stocate în text simplu** după ce camera se autentifică la serviciul Okta Auth0 al Flock folosind propria adresă MAC

#### 3. Credențiale pentru baze de date

- **Baze de date SQLite** fără protecție prin parolă
- Credențiale **MySQL/PostgreSQL** în fișiere de configurare
- **Acces direct la baza de date** dintr-un shell local

#### 4. Keystore-uri criptografice

- **Confirmate de CVE-2025-59407**: aplicația DetectionProcessing include un keystore Java împreună cu parola sa codificată direct, iar keystore-ul conține o **cheie privată**
- **Gravitate**: CRITICĂ (CVSS 9.8), deoarece materialul cheii este livrat împreună cu binarul care ar trebui să-l protejeze

#### 5. Nume de rețele Wi-Fi

- În firmware este codificată direct o **listă de rețele preferate**
- Permite atacuri cu **puncte de acces false** (vezi vulnerabilitatea nr. 6)

#### 6. Credențiale pentru servicii cloud

- **Tokenuri AWS/Azure** încorporate în cod
- **Chei API terțe** (ArcGIS, servicii de cartografiere)
- **Tokenuri OAuth** care nu sunt reînnoite niciodată

### Scenariu de atac: rețea falsă

Folosind numele de rețea Wi-Fi codificate direct, cercetătorii au demonstrat:

1. Atacatorul configurează o **rețea Wi-Fi falsă** cu SSID-ul codificat direct
2. Camera **se conectează automat** (prioritizează rețelele codificate direct)
3. Atacatorul capturează **tot traficul de rețea** printr-un atac de tip man-in-the-middle
4. Din trafic sunt extrase credențiale în text simplu
5. Atacatorul obține **acces la sistemul backend**

**Nu este necesar accesul fizic la cameră.** Este suficient să se afle în raza Wi-Fi.

______

{{< figure src="flock-safety-hardcoded-credentials-attack-vectors-diagram.webp" alt="Diagramă cu cinci vectori de atac prin credențiale codificate direct în camere Flock Safety, inclusiv parole Wi-Fi, chei API, credențiale pentru baze de date și tokenuri pentru servicii cloud" >}}

______

## Vulnerabilitatea critică nr. 5: lipsa autentificării multifactor

### Eșecul politicii organizaționale

**Gravitate**: RIDICATĂ (organizațională)

### Dezvăluirea

**Flock Safety nu impune 2FA/MFA** unor agenții de aplicare a legii, *aceleași agenții care accesează zilnic date de urmărire pentru 150 de milioane de vehicule.*

Declarația unui cercetător de securitate:

> „Când am aflat prima dată acest lucru, pur și simplu nu mi-a venit să cred. Procesul de securitate necesar pentru conectarea la Disney Plus li se pare prea complicat unor departamente de poliție atunci când accesează informații confidențiale și locația, în unele cazuri, a aproape tuturor.”

### De ce contează

Fără MFA/2FA:

- **O singură parolă compromisă** oferă acces complet la sistem
- **Atacurile de phishing** sunt foarte eficiente
- **Atacurile de tip credential stuffing** reutilizează parole din alte breșe
- **Amenințările din interior** sunt mai ușor de pus în practică
- **Dispozitivele furate** oferă acces imediat

### Comparație

Cerințe de securitate pentru sisteme **mai puțin sensibile**:

- **Disney+**: 2FA disponibilă
- **Gmail**: 2FA activată implicit pentru conturile noi
- **Servicii bancare**: 2FA impusă prin lege
- **Rețele sociale**: 2FA standard

Cerințe de securitate pentru urmărirea **a peste 150 de milioane de vehicule pe zi**:

- **Flock Safety**: 2FA opțională (unele agenții nu o folosesc)

### Răspunsul unui senator american

Această constatare a fost evidențiată în mod special în **scrisoarea senatorului Wyden** prin care se solicită o investigație FTC. Scrisoarea o citează ca dovadă că Flock Safety:

> „a expus inutil date personale sensibile ale americanilor riscului de furt din partea hackerilor și a spionilor străini”

### Soluție simplă

**Cheile de securitate USB/NFC** costă **10–25 USD** și oferă:

- Autentificare **rezistentă la phishing**
- **Nu sunt necesare aplicații sau coduri suplimentare**
- Conformitate cu standardele **FIDO2/WebAuthn**
- **Experiență simplă pentru utilizator** (conectează sau apropie dispozitivul)

*Dacă acest lucru este „prea complicat” pentru personalul din forțele de ordine, acesta **nu ar trebui să aibă acces** la sisteme naționale de supraveghere.*

______

## Vulnerabilitatea critică nr. 6: trafic de rețea în text simplu

### În așteptarea atribuirii unui identificator

**Gravitate**: RIDICATĂ (CVSS 7.8 estimat de cercetători)

**Această categorie nu a primit un identificator CVE.** Cea mai apropiată înregistrare atribuită, CVE-2025-59406, are clasificarea CWE-319 pentru transmisie în text simplu, dar se referă la un secret Auth0 încorporat, nu la interceptarea datelor în tranzit. Constatările din această secțiune se bazează în continuare pe rapoartele cercetătorilor citate mai sus.

### Vulnerabilitatea

Când camerele se conectează la rețele (LTE sau Wi-Fi), transmit date **fără criptare adecvată**:

**Trafic afectat**:

- Imagini și text cu numere de înmatriculare
- Metadate de detecție
- Jurnale de sistem
- Date de configurare
- Credențiale (în unele cazuri)

### Vector de atac nr. 1: rețea Wi-Fi falsă

Cercetătorii au demonstrat următorii pași:

1. Scoateți cartela SIM din cameră **sau** configurați o rețea falsă cu SSID-ul codificat direct
2. Camera se conectează la rețeaua Wi-Fi falsă
3. Capturați traficul cu **Wireshark** sau un analizor de pachete similar
4. Analizați-l cu instrumente precum **NetworkMiner** sau **Unblo**
5. Extrageți **credențiale în text simplu** și date sensibile

Fragment din cercetarea GainSec:

> „Am capturat pentru puțin timp datele pcap transmise de una dintre aceste camere și le-am analizat cu Wireshark și Unblo... și, într-adevăr, datele conțineau credențiale în text simplu.”

### Vector de atac nr. 2: captator IMSI / Stingray

Un atac mai sofisticat nu necesită apropiere fizică:

1. Folosiți un **captator IMSI** (dispozitiv Stingray improvizat) sau un SDR profesional
2. **Deturnați conexiunea LTE** imitând un turn de telefonie mobilă
3. Camera se conectează la o **stație de bază falsă**
4. Interceptați tot traficul printr-un atac **man-in-the-middle**
5. Extrageți credențiale, imagini și metadate

**Nu este necesar accesul fizic.** Atacul funcționează de la **sute de picioare distanță**.

### Potențialul atacurilor Tempest moderne

Transmiterea în text simplu permite și **atacuri de tip Tempest**, în care:

- Pot fi captate emisiile RF ale camerei
- Fluxul video poate fi **reconstituit de la distanță**
- Tehnica este similară celor folosite de **CIA în timpul Războiului Rece**
- Echipamentele SDR moderne fac metoda **accesibilă pasionaților**

______


## Vulnerabilitatea critică nr. 7: fluxuri video ale camerelor expuse public

### Descoperirea din ianuarie 2026

**Gravitate**: CRITICĂ (CVSS 10.0, expunerea completă a sistemului)

### Descoperirea

În ianuarie 2026, Ben Jordan și **404 Media** au descoperit că, folosind **căutări simple pe Google**, puteau găsi:

- Peste **60 de interfețe administrative Flock Safety complet expuse**
- Nu era necesar **niciun nume de utilizator sau parolă**
- **Fluxuri video live** și 30 de zile de înregistrări arhivate
- Acces complet la panoul de **control al camerelor**

### Ce era accesibil

Oricine putea folosi aceste interfețe expuse pentru a:

- **Urmări fluxuri video live** în timp real
- **Consulta 30 de zile** de înregistrări arhivate
- **Descărca direct fișiere video**
- **Controla camerele PTZ** (rotire, înclinare, zoom) ale unităților Condor
- **Vedea căile și hash-urile fișierelor** de probă
- **Șterge probe** printr-un singur clic
- **Modifica setările camerelor**
- **Vedea numerele de serie și locațiile dispozitivelor**

### Încălcări ale confidențialității observate

Ben Jordan a documentat scenele pe care le-a văzut:

- **O familie care punea un bebeluș în mașină** în parcarea Lowe’s
- **Un bărbat care pleca dimineața de acasă** în New York
- **O femeie care alerga singură** pe o potecă din pădurea Georgiei
- **Un cuplu care se certa** la o piață stradală din Atlanta (zoom-ul automat cu IA le-a urmărit fețele)
- **Un polițist și o ambulanță** care asistau o persoană în criză de sănătate mintală în Iowa
- **Copii care se jucau** într-un loc de joacă din zona golfului Californiei
- **Un bărbat pe un leagăn** într-un parc gol, într-un moment privat

Fragment din declarația lui Ben Jordan:

> „Numai să spun aceste lucruri cu voce tare mă îngrețoșează. Dar încerc să vă arăt doar o fracțiune din informațiile pe care oricine din lume, cu acces la un motor de căutare comercial, le-a putut vedea despre oricine a mers la această piață sau pe această potecă în ultimele 31 de zile.”

### Capacități de urmărire

Camerele Condor PTZ expuse au **urmărire bazată pe IA**:

- **Măresc automat** imaginea persoanelor
- **Urmăresc indivizii** în timp ce se deplasează
- **Detectează și focalizează** smartphone-uri (pentru a citi ecranele)
- **Urmăresc simultan mai multe ținte**
- **Înregistrează continuu** fără supraveghere

### Potențial de doxing

Ben Jordan a demonstrat cât de ușor pot imaginile expuse să dezvăluie identități:

> „În două minute de OSINT, folosind un motor comercial de recunoaștere facială, am aflat că una dintre persoane tocmai terminase facultatea de medicină, iar cealaltă se confruntă cu sindromul de colon iritabil cronic. Cuplul a avut și un copil anul trecut... Știu și că au condus peste 45 de minute de la adresa lor din suburbii.”

Corelând imaginile cu:

- Servicii de **recunoaștere facială**
- Profiluri de **rețele sociale**
- Baze de date cu **registre publice**
- Informații din **breșe de date** (Park Mobile etc.)
- **Jurnale ale apelurilor de urgență** (publicate de multe orașe)

Rezultat: **de-anonimizare completă în câteva minute**

{{< figure src="flock-exposed-camera-feed-ptz-ai-tracking-privacy-violation-overview.webp" alt="Diagramă de ansamblu care arată cum camerele Flock Safety PTZ expuse, cu urmărire automată prin IA, permiteau accesul public la fluxuri video live cu persoane din parcuri, de pe poteci și din parcări" >}}

______


## Vulnerabilitatea critică nr. 8: colectarea neautorizată a datelor

### Contradicție cu declarațiile publice

**Gravitate**: RIDICATĂ (implicații privind confidențialitatea și aspectele juridice)

### Afirmațiile Flock Safety

**Declarație pe site-ul oficial**:

> „Flock Safety nu capturează și nu înregistrează date despre persoane, ci doar despre vehicule.”

### Constatările cercetării independente

**Ce fac de fapt camerele**:

1. **Detectarea mișcării** declanșează camera **pentru orice**, nu doar pentru vehicule
2. **IA caută plăcuța de înmatriculare** în imagine
3. **Dacă nu găsește o plăcuță**, imaginea este **totuși stocată** (nu este ștearsă)
4. Un **dosar separat** stochează imaginile fără plăcuțe
5. **Persoanele, pietonii și bicicliștii** sunt capturați și păstrați

*Afirmația „doar vehicule” este falsă. Camera stochează imagini cu oricine trece prin fața ei.*

### Observații verificate

Cercetătorii au documentat camere care au capturat:

- **O persoană care mergea** prin fața camerei (imagine stocată)
- **O mână care făcea cu mâna** spre obiectiv (imagine stocată)
- **O masă sau un obiect** mutat lângă cameră (imagine stocată)
- **Angajați ai fabricii** în unitatea de producție (stocați luni întregi)

Fragment din declarația GainSec:

> „Când am trecut prin fața camerei, modulul radar a declanșat modulul camerei să-mi facă o fotografie. Apoi, IA de pe dispozitiv a căutat o plăcuță de înmatriculare, nu a găsit una, dar tot a salvat imaginea într-un dosar separat.”

### Implicații juridice

Această colectare neautorizată de date ar putea:

- **Încălca politicile de confidențialitate declarate** (practici înșelătoare)
- **Încălca contractele de achiziție** (dacă orașele au specificat „doar vehicule”)
- **Declanșa încălcări GDPR/CCPA** (cetățeni UE, rezidenți ai Californiei)
- **Invalida acordurile de consimțământ**
- **Expune compania la litigii** pentru publicitate falsă

### Extinderea domeniului supravegherii

Camerele **Condor PTZ** (instalate în 2025–2026) sunt **proiectate explicit** pentru a urmări persoane:

- **Detectarea persoanelor cu IA**
- **Zoom automat** pe fețe
- **Urmărirea deplasării** persoanelor
- **Fără mecanism de renunțare**
- **Instalate frecvent** în parcuri, pe poteci și în stații de transport

*Acest lucru extinde masiv utilizarea de la „cititoare de plăcuțe de înmatriculare” la supravegherea populației, fără schimbări de politică, contracte noi sau notificare publică.*

______

## Vulnerabilitatea critică nr. 9: porturi USB expuse atacurilor Rubber Ducky

### Exploatare prin acces fizic

**Gravitate**: RIDICATĂ (cu acces fizic)

### Vulnerabilitatea

**Cutii de calcul Bravo** și unele modele de camere au:

- **Porturi USB-C expuse** la exterior
- **Nicio protecție fizică** (sigilii ale carcasei)
- **Executare automată** a dispozitivelor USB
- **Nu este necesară autentificarea**

### Atac Rubber Ducky / BadUSB

Un **dispozitiv BadUSB** (costă 5–15 USD):

- Este detectat de sistem ca **tastatură USB**
- **Execută scripturi preprogramate** (payload-uri)
- **Rulează automat** când este conectat
- **Nu necesită interacțiunea utilizatorului**

### Scenariu de atac

GainSec a demonstrat acești pași:

1. Apropie-te de un dispozitiv Flock instalat
2. Conectează **dispozitivul BadUSB** la portul expus
3. Dispozitivul execută payload-ul (scriptul)
4. Payload-ul instalează **malware persistent**
5. Atacatorul **pleacă**
6. Malware-ul **comunică cu serverul de comandă și control** prin LTE/Wi-Fi

**Timp total**: sub 30 de secunde

### Ce pot face payload-urile

Scripturile automatizate pot:

- **Activa un punct de acces wireless** (ocolind apăsarea butonului)
- **Instala un backdoor** pentru acces la distanță
- **Exfiltra date** către un server la distanță
- **Modifica înregistrări** sau probe
- **Dezactiva camera** sau provoca refuzul serviciului
- **Adăuga dispozitivul la o botnet** pentru atacuri DDoS
- **Captura credențiale** din alte sisteme

### De ce contează

Dintre cele **peste 80.000 de camere**, multe se află în **zone semirurale** cu **vizibilitate redusă**:

- **Accesul fizic** este relativ ușor
- **Nu există paznici** sau monitorizare constantă
- Sunt fixate cu **coliere simple de furtun**
- Sunt adesea montate la **2,1 metri de sol** (pot fi atinse cu un scăunel)

Fragment din declarația lui Ben Jordan:

> „Aceste camere nu sunt niște mici fortărețe impenetrabile. Sunt camere Android din plastic și cutii de calcul montate la 2,1 metri de sol cu coliere de furtun.”

______

{{< figure src="badusb-rubber-ducky-flock-camera-usb-exploit-attack-chain.webp" alt="Diagramă a lanțului de atac care arată cum un dispozitiv BadUSB conectat la portul USB expus al unei camere Flock Safety poate instala malware persistent în mai puțin de 30 de secunde" >}}

______

## Vulnerabilitatea critică nr. 10: chei API expuse public

### Descoperirea unui cercetător OSINT

**Gravitate**: CRITICĂ (CVSS 9.5)

### Descoperirea

În 2025, cercetătorul **OSINT Joshua Michael** a descoperit:

- Un **site demonstrativ Flock Safety expus**, găsit prin Google dorking
- **5.000 de linii de cod sursă** vizibile
- O **cheie API activă** încorporată în cod
- Acces la peste **50 de straturi private** de date geospațiale

### Ce acces oferea cheia API

Cheia **ArcGIS API** expusă permitea accesul la:

**1. Date de înregistrare**

- Numele clienților
- Adrese de e-mail
- Numărul de camere pentru fiecare locație
- Posibilitatea de atașare a fișierelor

**2. Locațiile mașinilor de patrulare live** (mai multe departamente)

- Urmărire GPS în timp real a vehiculelor de poliție
- Implementarea din Aurora, Colorado
- Departamentul de Poliție Carrollton
- **Risc pentru securitatea națională**

**3. Informații personale despre polițiști**

- Nume și numere de telefon
- Adrese de e-mail
- Zone de patrulare preconizate
- Jurisdicții de origine

**4. Baza de date cu alerte pentru lista de vehicule urmărite** (Dallas, Texas)

- **6.000 de înregistrări** ale vehiculelor semnalate
- Numere de înmatriculare și motivele semnalării
- Locații și marcaje temporale ale detecțiilor
- ID-urile camerelor care au surprins vehiculele
- **Cinci luni de urmărire a deplasărilor**

Fragment din declarația lui Joshua Michael:

> „Oricine putea căuta pe Google, găsi această hartă și urmări tiparele de deplasare ale acestor persoane timp de cinci luni. Mai menționez că motivul unei înregistrări este doar «suspect», iar multe altele nu au niciun motiv sau câmpul este gol.”

### Suprafața de atac

Cheile API expuse permit:

- **Urmărirea unor vehicule specifice**
- **Compromiterea siguranței polițiștilor** (adrese de domiciliu, tipare de patrulare)
- **Încălcarea securității operaționale** (unde se află sau nu se află poliția)
- **Intimidarea martorilor** (urmărirea celor care au raportat infracțiuni)
- **Colectarea de informații criminale** de către grupări organizate

### Contextul breșei: Flax Typhoon

Cu doar câteva săptămâni înainte de această descoperire, grupul de hackeri **Flax Typhoon**, **susținut de statul chinez**, a compromis ArcGIS, potrivit cercetătorilor de securitate Alexa Feminina și James Zhang.

Fragment din InfoSecurity Magazine:

> „Se presupune că hackerii au vizat o aplicație ArcGIS legitimă, accesibilă publicului... folosită pentru recuperarea după dezastre, gestionarea situațiilor de urgență și alte funcții critice.”

**Acest lucru înseamnă că state ostile ar fi putut avea acces** la locațiile vehiculelor de poliție, identitățile polițiștilor, pozițiile camerelor de supraveghere și tiparele de răspuns la urgențe.

______

## Vulnerabilități suplimentare (rezumatul a peste 50)

### Vulnerabilitățile 11–51

Raportul GainSec documentează **41 de constatări suplimentare**, inclusiv:

**Defecte de proiectare a sistemului**:
- Modul de depanare activat în firmware-ul de producție
- Procesul nesigur de pornire permite compromiterea bootloader-ului
- Niciun element securizat sau TPM pentru stocarea cheilor
- Mecanism previzibil de actualizare a firmware-ului

**Probleme de autentificare**:
- Tokenurile de sesiune nu expiră niciodată
- Nicio restricție de acces bazată pe adresa IP
- Date de autentificare partajate între flotele de dispozitive
- Niciun certificate pinning

**Securitatea rețelei**:
- Porturi deschise cu servicii de depanare
- Telnet activat pe unele unități
- Servere FTP cu date de autentificare slabe
- Vulnerabilități de tip DNS rebinding

**Confidențialitate și păstrarea datelor**:
- Imagini păstrate peste perioada declarată
- Metadate care nu sunt șterse niciodată
- Date de recunoaștere facială colectate
- Urmărirea locației și în afara vehiculelor

**Securitate fizică**:
- Carcase ușor de demontat
- Interfețe seriale expuse
- Porturi de depanare JTAG accesibile
- Lipsa sigiliilor care indică intervenția

**Deficiențe criptografice**:
- Generare slabă a numerelor aleatorii
- Chei de criptare codificate direct
- MD5 încă folosit în lanțul de hash-uri
- Validarea certificatelor dezactivată

**Divulgarea informațiilor**:
- Mesaje de eroare detaliate care dezvăluie elemente interne
- Listarea directoarelor activată pe serverele web
- Comentarii în codul sursă care conțin date de autentificare
- Copii de rezervă ale configurației lizibile de oricine

### Situația CVE-urilor

În mai 2026:
- **22 de CVE-uri atribuite** și publicate
- **8 CVE-uri în așteptarea** atribuirii de către MITRE
- **21 de constatări** neînaintate pentru atribuire CVE, la discreția cercetătorilor
- **Toate constatările** documentate în raportul GainSec

Detalii tehnice complete: [github.com/GainSec/anti-crime-ecosystem-research](https://github.com/GainSec/anti-crime-ecosystem-research)

______

## Răspunsul Flock Safety

### Declarații oficiale

**Postare pe blog din noiembrie 2025**:
> „Flock se angajează să îmbunătățească securitatea în mod continuu... Niciuna dintre vulnerabilitățile detaliate în raport nu afectează capacitatea clienților noștri de a-și îndeplini obiectivele de siguranță publică.”

**Afirmație**: vulnerabilitățile necesită acces fizic și „cunoștințe aprofundate”.

**Dovezi contrare**:
- Pentru a găsi fluxurile camerelor expuse era suficientă **o căutare pe Google**
- Exploatările wireless necesită doar **proximitate**
- Expunerea cheii API putea fi exploatată **complet de la distanță**
- După divulgare, parolele codificate direct erau **cunoscute de toată lumea**

### Descalificarea dispozitivelor de cercetare

Inițial, Flock a susținut că dispozitivele de cercetare:
> „Nu erau conectate la cloud... ca un iPhone furat din camion înainte să fie conectat.”

*Afirmația s-a dovedit falsă.* Cercetătorii au testat **dispozitive conectate la cloud** și au obținut rezultate identice. Camerele accesibile publicului aveau **aceleași vulnerabilități**, iar 404 Media a găsit **peste 60 de camere de producție expuse**.

### Răspunsul față de cercetători

Potrivit GainSec, încercările de divulgare responsabilă au primit aceste răspunsuri:
- **Program de recompense pentru erori cu NDA**, care reducea divulgarea la tăcere
- **Nicio confirmare** a remedierilor
- **Comunicat de presă** publicat înainte de termenul de 90 de zile
- **Nicio recunoaștere** a cercetătorului în comunicat
- **Pierderea locului de muncă** de către cercetător în 48 de ore de la publicarea videoclipului

Ben Jordan a relatat:
- **Vizite ale poliției** la proprietatea sa
- Persoane bănuite a fi **detectivi particulari** care îi fotografiau locuința
- **Hărțuire din partea vecinilor**
- Amenințări cu o **notificare de încetare a activității** din partea Flock Safety

Fragment din declarația lui Ben:
> „Nu văd aceste lucruri ca pe consecințe sau pedepse pentru cercetarea vulnerabilităților de securitate. Le văd ca pe consecințe și pedepse pentru faptul că am făcut-o etic și transparent.”

### Instalările continuă

*În ciuda tuturor acestor lucruri*, Flock Safety:
- **Continuă să vândă** dispozitive vulnerabile
- Nu a lansat **actualizări de firmware** care să remedieze cauzele principale
- Continuă să folosească **Android Things 8.x**, ieșit din suport în 2021
- Nu impune **MFA obligatoriu** organelor de aplicare a legii

______

______


## Răspuns legislativ și de politici publice

### Cererea Senatului SUA pentru o investigație

**Februarie 2026**: senatorii **Ron Wyden** (Oregon) și **Raja Krishnamoorthi** (Illinois) au trimis FTC o scrisoare oficială prin care au cerut o investigație.

**Fragment din scrisoare**:
> „Flock a expus inutil datele personale sensibile ale americanilor riscului de furt din partea hackerilor și a spionilor străini.”

**Motivele invocate**:
- Riscuri pentru securitatea națională
- Afirmații înșelătoare despre confidențialitate
- Practici de securitate necorespunzătoare
- Lipsa cerințelor MFA

### Acțiuni ale consiliilor municipale

**Denver, Colorado**:
- În decembrie 2025, consiliul municipal **a votat împotriva** reînnoirii contractului cu Flock
- A invocat **„lipsa de onestitate și responsabilitate”** a companiei
- În ianuarie 2026, primarul **a anulat decizia** printr-un „acord pe ascuns”
- Reacția publică continuă

**Evanston, Illinois**:
- A descoperit că **ICE folosea camerele** fără consimțământ
- A votat pentru **scoaterea camerelor**
- *Flock a reinstalat camerele fără autorizație*
- Orașul folosește banii contribuabililor pentru a **acoperi camerele** cu prelate și pentru a lua măsuri juridice

**Oakland, California**:
- A amânat votul pentru o **extindere de 2,25 milioane de dolari**
- A comandat un audit de securitate independent
- A considerat **înșelătoare** afirmațiile Flock despre eficacitate

### Cereri privind registrele publice

Mai multe orașe desfășoară investigații pe baza:
- Cercetărilor de securitate disponibile public
- Cererilor FOIA pentru contractele Flock
- Cerințelor de audit independent
- Presiunii exercitate de activiștii comunitari

______

## Analiză tehnică: scenarii reale de atac

### Scenariul 1: supraveghere de către un stat-națiune

**Actorul amenințării**: serviciu de informații străin

**Obiectiv**: urmărirea oficialilor guvernamentali

**Metodă**:
1. Folosește un captator IMSI pentru a intercepta traficul LTE al camerelor
2. Extrage datele de autentificare în text simplu din flux
3. Accesează backend-ul cu chei API compromise sau cu un strat ArcGIS expus anterior
4. Interoghează baza de date pentru vehicule înregistrate la clădiri guvernamentale
5. Urmărește deplasările oficialilor și personalului militar

**Timp de execuție**: zile, după instalarea infrastructurii
**Probabilitate de detectare**: scăzută, deoarece traficul C2 criptat imită traficul legitim

### Scenariul 2: contrasupraveghere din partea crimei organizate

**Actorul amenințării**: organizație de trafic de droguri

**Obiectiv**: identificarea tiparelor de patrulare ale poliției

**Metodă**:
1. Cumpără un dispozitiv BadUSB (15 USD)
2. Se deplasează la camerele din zona sa de activitate
3. Conectează BadUSB la un port USB expus (30 de secunde)
4. Payload-ul dezactivează camera sau modifică înregistrările
5. Alternativ, payload-ul exfiltrează urmărirea vehiculelor de poliție către un server la distanță

**Timp de execuție**: 30 de secunde pentru fiecare cameră
**Probabilitate de detectare**: scăzută, pare activitate legitimă a dispozitivului

### Scenariul 3: hărțuire și violență domestică

**Actorul amenințării**: fost partener abuziv

**Obiectiv**: urmărirea deplasărilor victimei

**Metodă**:
1. Obține numărul de înmatriculare al victimei, o informație publică
2. Caută pe Google o interfață Flock expusă, prin vulnerabilitatea din ianuarie 2026
3. Caută aparițiile vehiculului în 30 de zile de înregistrări
4. Compară rezultatele cu baze de date publice despre locul de muncă, domiciliu etc.
5. Stabilește rutina și programul victimei

**Timp de execuție**: minute până la ore
**Probabilitate de detectare**: zero, nu există jurnale de autentificare

### Scenariul 4: falsificarea probelor

**Actorul amenințării**: inculpat într-un proces penal

**Obiectiv**: distrugerea probelor înaintea procesului

**Metodă**:
1. Află locația camerei din documentele obținute prin mandat
2. Obține acces fizic la cameră, folosind secvența de apăsări pe buton
3. Obține un shell root
4. Navighează la dosarul cu probe
5. Șterge anumite imagini sau videoclipuri ori modifică marcajele temporale

**Timp de execuție**: sub cinci minute
**Probabilitate de detectare**: scăzută, dacă apărarea nu examinează criminalistic camera înainte de acces

### Scenariul 5: activist pentru confidențialitate sau jurnalist

**Actorul amenințării**: susținător al transparenței

**Obiectiv**: documentarea supravegherii excesive

**Metodă**:
1. Folosește dispozitive de detecție (vezi [Ghidul nostru pentru hardware Flock-You](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/))
2. Cartografiază locațiile camerelor din comunitate
3. Depune cereri FOIA privind politicile de înregistrare
4. Demonstrează vulnerabilitățile în fața consiliului municipal
5. Cere eliminarea camerelor sau supraveghere asupra utilizării lor

**Timp de execuție**: continuu
**Probabilitate de detectare**: ridicată, activitatea este publică

______

{{< figure src="flock-camera-attack-scenario-threat-actor-matrix-nation-state-crime.webp" alt="Matrice care compară cinci scenarii reale de atac asupra camerelor Flock Safety: supravegherea de către un stat-națiune, contrasupravegherea crimei organizate, hărțuirea, falsificarea probelor și activismul pentru confidențialitate" >}}

______

## Apărarea împotriva acestor vulnerabilități

### Pentru organele de aplicare a legii

**Acțiuni imediate**:
1. **Impune MFA/2FA** pentru toți utilizatorii, cu chei de securitate USB
2. **Auditează jurnalele de acces** lunar pentru interogări neautorizate
3. **Limitează partajarea** la jurisdicțiile strict necesare
4. **Izolează rețeaua** și plasează camerele în VLAN-uri dedicate
5. **Asigură protecția fizică**, cu sigilii anti-intervenție și supravegherea camerelor
6. **Pregătește un plan de răspuns la incidente** pentru compromiteri

**Cerințe contractuale**:
1. **Audituri regulate de securitate** realizate de firme independente
2. **Actualizări obligatorii de firmware** în cel mult 30 de zile de la publicarea remedierii
3. **Notificarea CVE-urilor** în cel mult 24 de ore
4. **Stocarea criptată a probelor** cu chei gestionate de client
5. **Penalități SLA** pentru breșe de securitate
6. **Dreptul de a audita** sediile și codul furnizorului

**Strategie pe termen lung**:
1. **Plan de tranziție** de la sistemele de operare ieșite din suport
2. **Infrastructură găzduită intern** pentru a reduce dependența de cloud
3. **Evaluarea alternativelor open-source**
4. **Transparență față de comunitate** privind locațiile și politicile camerelor

### Pentru Flock Safety (recomandări)

**Prioritate critică** (imediat):
1. **Dezactivează crearea punctului de acces wireless** prin apăsarea butonului
2. **Impune MFA** pentru toate conturile, fără excepții
3. **Schimbă toate credențialele codificate direct** în întregul sistem
4. **Aplică o remediere de urgență** interfețelor publice expuse
5. **Criptează datele în repaus** și gestionează corect cheile

**Prioritate ridicată** (30 de zile):
1. **Migrează la un sistem de operare acceptat**, Android 12+ sau Linux
2. Creează un **program de recompense pentru erori fără NDA-uri**
3. Realizează un **audit de securitate de către o terță parte** și publică rezultatele
4. **Criptează traficul de rețea de la un capăt la altul**
5. **Îmbunătățește securitatea fizică**, elimină porturile USB expuse și consolidează carcasele

**Prioritate medie** (90 de zile):
1. **Reproiectează complet** sistemul de autentificare
2. Implementează **pornire securizată** cu firmware verificat
3. Integrează un **modul de securitate hardware**
4. Obține **certificări de conformitate** (FedRAMP, SOC 2, ISO 27001)
5. Creează un **panou de securitate pentru clienți** cu notificări despre breșe

**Termen lung** (un an):
1. **Deschide componentele de securitate** pentru a construi încredere
2. Creează un program de **testare adversarială** (echipă roșie)
3. Stabilește cerințe pentru rolurile de **inginerie de securitate**
4. Integrează securitatea în **ciclul de dezvoltare software** (DevSecOps)
5. Participă la definirea **standardelor din industrie** (OWASP, CIS)

### Pentru persoane fizice

**Strategii de protecție**:
1. **Folosește dispozitive de detecție** (vezi [Ghidul nostru hardware](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/))
2. **Cartografiază camerele** din zona ta
3. **Variează traseele și orele** pentru a reduce analiza tiparelor
4. **Cere supraveghere și transparență** în consiliul municipal
5. Depune **cereri FOIA** pentru datele tale, acolo unde legea permite
6. **Susține legislația privind confidențialitatea** la nivel statal și federal

**Măsuri de securitate operațională (OpSec)**:
1. **Evită vehiculele unice**, alege o marcă, un model și o culoare comune
2. Folosește **vehicule diferite** pentru activități sensibile, acolo unde legea permite
3. Alege **transport alternativ**, bicicleta, transportul public sau mersul pe jos
4. Folosește **huse de număr care protejează confidențialitatea**, numai dacă sunt legale în jurisdicția ta
5. Folosește **huse Faraday** pentru telefoane când există riscul corelării

{{< stscollective-ad "flockyou" >}}

______

{{< figure src="flock-safety-security-remediation-priority-roadmap.webp" alt="Plan prioritizat de remediere cu măsuri imediate, în 30 de zile, în 90 de zile și pe termen lung pe care Flock Safety ar trebui să le implementeze pentru vulnerabilitățile critice" >}}

______
## Echipa de cercetare

### GainSec (Jon „GainSec” Gaines)

**Experiență**: profesionist în securitate ofensivă, cu peste zece ani de experiență

**Contribuții**:
- A descoperit **47 dintre cele 51** de vulnerabilități
- A publicat un **raport tehnic oficial** cu detalii
- A coordonat **divulgarea responsabilă** către Flock Safety
- A înregistrat **30 de CVE-uri** (22 publicate, 8 în așteptare)
- A creat o **listă de verificare pentru apărători** din domeniul securității

**Contact**: whitepaper@gainsecmail.com
**Cercetare**: [github.com/GainSec/anti-crime-ecosystem-research](https://github.com/GainSec/anti-crime-ecosystem-research)
**Blog**: [gainsec.com](https://gainsec.com)

### Ben Jordan (Benn Jordan)

**Experiență**: jurnalist, muzician și investigator în domeniul tehnologiei

**Contribuții**:
- **Documentarea video** a vulnerabilităților
- **Demonstrații publice** pentru jurnaliști (The Guardian, 404 Media)
- A descoperit prin Google **peste 60 de fluxuri video ale camerelor expuse**
- **Susținere și educare a publicului**
- **Coordonare legislativă** cu birourile senatorilor

**Contact**: prin canalul YouTube
**Lucrări**: YouTube - Benn Jordan

### Joshua Michael (Next AI)

**Experiență**: specialist OSINT și cercetător în domeniul confidențialității

**Contribuții**:
- A descoperit prin Google dorking **chei API expuse**
- A documentat **expunerea straturilor ArcGIS**
- A aplicat o **metodologie OSINT** pentru urmărirea cercetării
- A realizat **corelarea datelor** cu breșe publice

**Organizație**: Next AI, firmă de informații din surse multiple

### Contribuitori

- **404 Media**: jurnalism de investigație și divulgare publică
- **The Guardian**: acoperire internațională
- **Lucy Parsons Labs**: ani de susținere și cercetare privind ALPR
- **Sassy South**: organizare comunitară și transparență
- **DeFlock / Will Freeman**: proiect de cartografiere a camerelor
- **Ed Vogel**: analiză juridică și de politici publice

______

## Considerații etice

### Calendarul divulgării responsabile

Comunitatea de securitate a urmat bunele practici de **divulgare responsabilă**:

**Protocol standard**:
1. Descoperirea vulnerabilității
2. **Notificarea privată a furnizorului în 90 de zile**
3. Furnizorul dezvoltă și implementează o remediere
4. **Divulgarea publică** după remediere sau după 90 de zile, oricare survine prima
5. Publicarea unei analize detaliate pentru învățare defensivă

**Ce s-a întâmplat de fapt**:
1. GainSec a descoperit vulnerabilitățile (sfârșitul lui 2024)
2. A încercat **repetat să contacteze** Flock Safety (din februarie 2025)
3. Flock a oferit un **program de recompense cu NDA**, care reducea divulgarea la tăcere
4. Flock a publicat **un comunicat de presă înainte de termen**, fără a recunoaște cercetătorul
5. **Nu a confirmat** implementarea remedierilor
6. GainSec a făcut **divulgarea publică** după perioadele de 90 de zile
7. Ben Jordan și 404 Media au **verificat independent** problemele pe sisteme de producție

### Represalii împotriva cercetătorilor

Atât GainSec, cât și Ben Jordan au relatat:
- **Pierderea locului de muncă** sau dificultăți profesionale
- **Vizite ale poliției** la locuințele personale
- **Supravegherea suspectată** a locuințelor și proprietăților
- **Hărțuire din partea vecinilor**
- **Amenințări de încetare a activității**
- **Atacuri pe rețelele sociale**, inclusiv etichetarea drept „teroriști” de către directorul general al Flock

Acest **efect de intimidare** asupra cercetării în securitate:
- Descurajează divulgarea vulnerabilităților
- Întârzie remedierile critice de securitate
- Afectează siguranța publică
- Încalcă normele etice ale comunității de securitate

*Răspunsul Flock Safety față de cercetătorii care au urmat protocoalele de divulgare creează un precedent periculos pentru întreaga comunitate de cercetare în securitate.*

Fragment din declarația lui Ben Jordan:
> „Nu îmi permit să dedic încă și mai multe luni unei alte vulnerabilități Flock Safety, dar, după cum vedeți, aceasta este urgentă și, sincer, mă tem că este deja exploatată.”

### Interesul public

Acești cercetători au acționat **în interes public** prin:
- **Respectarea** protocoalelor de divulgare responsabilă
- **Notificarea prealabilă a furnizorului** înaintea divulgării publice
- **Redactarea detaliilor sensibile** care ar facilita exploatarea
- **Oferirea de îndrumări defensive** practicienilor
- **Susținerea schimbărilor de politici** prin canalele adecvate
- **Asumarea riscurilor personale** pentru a informa publicul

Fără munca lor:
- **Peste 80.000 de camere vulnerabile** ar fi continuat să funcționeze fără remediere
- **Peste 150 de milioane de scanări zilnice de vehicule** ar fi rămas neprotejate
- **Milioane de americani** ar fi fost expuși fără să știe
- **Securitatea națională** ar fi fost compromisă
- **Nu ar fi fost în curs nicio acțiune legislativă**

______

## Concluzie: calea de urmat

{{< figure src="flock-safety-vulnerability-disclosure-timeline-2026.webp" alt="Diagramă cronologică ce rezumă procesul de divulgare a vulnerabilităților Flock Safety din 2024 până în 2026, de la descoperirea inițială și divulgarea responsabilă până la expunerea continuă fără remedieri" >}}

### Situația actuală (mai 2026)

- **Peste 50 de vulnerabilități critice** documentate și divulgate parțial
- **Peste 80.000 de camere** rămân instalate cu defecte neremediate
- Furnizorul nu a aplicat **nicio remediere cuprinzătoare**
- **Acțiuni de reglementare limitate** (s-a cerut o investigație FTC, dar aceasta nu a început)
- **Risc continuu de exploatare** pentru securitatea națională și confidențialitatea individuală

### Ce trebuie să se întâmple

**La nivelul întregii industrii**:
1. **Audituri de securitate obligatorii** înainte de implementarea în instituții guvernamentale
2. **Testare independentă** de către terți calificați
3. **Publicarea rezultatelor auditurilor**
4. **Răspunderea furnizorilor** pentru deficiențele de securitate
5. **Respectarea standardelor** (NIST, ISO etc.)

**Pentru Flock Safety**:
1. **Remedieri de urgență imediate** pentru vulnerabilitățile critice
2. **Migrarea sistemului de operare** la o platformă acceptată
3. **Recunoașterea publică** a amplorii problemelor
4. **Compensarea cercetătorilor afectați**
5. **Rapoarte transparente** privind postura de securitate

**Pentru organele de aplicare a legii**:
1. **Cerințe de securitate** în contractele de achiziție
2. **Audituri regulate** ale sistemelor instalate
3. **MFA obligatoriu** pentru toți utilizatorii
4. **Planuri de răspuns la incidente**
5. **Transparență față de comunitate** cu privire la programele de supraveghere

**Pentru legislatori**:
1. **Standarde federale** pentru tehnologia de supraveghere
2. **Divulgarea obligatorie** a vulnerabilităților către părțile afectate
3. **Protecție pentru avertizorii de integritate** și cercetătorii în securitate
4. **Mijloace civile de reparare** pentru încălcări ale confidențialității
5. **Mecanisme de supraveghere** a sistemelor de supraveghere

### Imaginea de ansamblu

Acest studiu de caz reprezintă **mai mult decât Flock Safety**. El ilustrează:
- O **industrie a supravegherii** care prioritizează creșterea în detrimentul securității
- **Achiziții guvernamentale** fără expertiză tehnică suficientă
- **Afirmații ale furnizorilor** lăsate neverificate și necontestate
- **Stimulente financiare** nealiniate cu siguranța publică
- **Lacune de reglementare** în supravegherea tehnologiilor emergente

*Fiecare oraș care semnează un contract cu Flock fără verificare independentă de securitate acceptă aceste riscuri în numele locuitorilor săi.*

### Apel la acțiune

**Pentru profesioniștii în securitate**:
- **Susține divulgarea responsabilă**
- **Contribuie la instrumentele de securitate open-source**
- **Cere protecție pentru cercetători**

**Pentru organele de aplicare a legii**:
- **Cere responsabilitate** furnizorilor
- **Solicită audituri de securitate** înainte de instalare
- **Implementează imediat MFA**
- **Consultă comunitatea de securitate**

**Pentru factorii de decizie**:
- **Adoptă legi** care impun standarde de securitate
- **Finanțează audituri independente** ale tehnologiei de supraveghere
- **Protejează avertizorii de integritate** și cercetătorii
- **Înființează organisme de supraveghere** cu expertiză tehnică

**Pentru public**:
- **Informează-te** despre supravegherea din comunitatea ta
- **Participă la ședințele consiliului municipal** când se discută contracte
- **Susține organizațiile** care cer transparență
- **Contactează reprezentanții aleși** pentru a-ți exprima preocupările
- **Folosește instrumente de detecție** pentru a cartografia supravegherea (vezi [Ghidul nostru hardware](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/))

### Lecturi conexe

- **[Supravegherea cu camere Flock Safety: răspândire, preocupări privind confidențialitatea și strategii de protecție](/articles/flock-safety-camera-surveillance-prevalence-privacy-protection-2026/)**: înțelege contextul supravegherii
- **[Proiectul de detecție Flock-You: ghid hardware pentru contrasupraveghere](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/)**: construiește propriul dispozitiv de detecție

Așteptarea ca industria să remedieze aceste defecte nu este o strategie de protecție. **[Dispozitivele de detecție FlockYou](https://stscollective.com/collections/flockyou-alpr-flock-safety-awareness-devices)** de la STS Collective sunt disponibile acum, iar codul promoțional **SIMEONONSECURITY** oferă până la 20% reducere.

{{< centerbutton href="https://stscollective.com/discount/SIMEONONSECURITY" >}}
  Cumpără detectoare FlockYou și economisește 20%
{{< /centerbutton >}}

______

## Referințe

1. [Cercetarea GainSec asupra ecosistemului anti-crimă - GitHub](https://github.com/GainSec/anti-crime-ecosystem-research)
2. [Raportul GainSec - DOI Zenodo: 10.5281/zenodo.17529423](https://zenodo.org/records/17584876)
3. [Blogul GainSec - analize tehnice neoficiale](https://gainsec.com/)
4. [Răspunsul oficial Flock Safety - noiembrie 2025](https://www.flocksafety.com/blog/response-to-compiled-security-research-on-flock-safety-devices)
5. [404 Media - fluxuri video Flock expuse](https://www.404media.co/)
6. [YouTube Ben Jordan - demonstrații ale vulnerabilităților](https://www.youtube.com/@BennJordan)
7. [Baza de date națională a vulnerabilităților](https://nvd.nist.gov/)
8. [Baza de date MITRE CVE](https://cve.mitre.org/)
9. [Electronic Frontier Foundation - supravegherea ALPR](https://www.eff.org/issues/automated-license-plate-readers)
10. [Scrisoarea senatorului Wyden către FTC](https://www.wyden.senate.gov/)
11. [Lucy Parsons Labs - cercetare ALPR](https://lucyparsonslabs.com/)
12. [Proiectul DeFlock - cartografierea camerelor](https://deflockproject.org/)
13. [Distributed Denial of Secrets - imagini ale sistemului de fișiere al camerelor Flock ALPR](https://ddosecrets.org/article/flock-alpr-camera)
14. [Micah Lee - camerele Flock sunt pline de vulnerabilități și credențiale codificate direct](https://micahflee.com/flock-cameras-are-riddled-with-security-vulnerabilities-and-hard-coded-credentials/)
15. [WIRED și 404 Media - hackerii au pătruns într-o cameră Flock](https://www.wired.com/story/hackers-flock-camera-data-shows-how-system-works/)
16. [Hackaday - Săptămâna aceasta în securitate: camerele Flock sunt vechi](https://hackaday.com/2026/09/18/this-week-in-security-flock-cameras-are-old-microsoft-patches-patches-and-researchers-attack-ssh/)
17. [NVD - CVE-2021-1905, utilizare după eliberare în GPU-ul Qualcomm Adreno](https://nvd.nist.gov/vuln/detail/CVE-2021-1905)
18. [NVD - CVE-2018-9568, confuzie de tip în socketurile kernelului Linux](https://nvd.nist.gov/vuln/detail/CVE-2018-9568)
19. [WiFi Mothership - detecția și referința dispozitivelor ALPR Flock Safety](https://wifimothership.com/flock)
20. [CVE.org - căutare în înregistrările programului CVE](https://www.cve.org/)
21. [Alertă de securitate Flock Safety - detecția focurilor de armă și cititoare de numere](https://www.flocksafety.com/articles/gunshot-detection-and-license-plate-reader-security-alert)
22. [GainSec - Fly By Device 2: execuție la distanță wireless Falcon și Sparrow](https://gainsec.com/2025/09/27/fly-by-device-2-the-falcon-sparrow-gated-wireless-rce-camera-feed-dos-information-disclosure-and-more/)
23. [GainSec - Root from the Coop Device 3: shell root pe unitatea de calcul Bravo Flock Safety](https://gainsec.com/2025/09/19/root-from-the-coop-device-3-root-shell-on-flock-safetys-bravo-compute-box/)
