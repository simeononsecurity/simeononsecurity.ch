---
title: "Curs Network Plus: Înțelegerea modelului OSI, a topologiilor și a tipurilor de rețele"
date: 2023-07-01
toc: true
draft: false
description: "Explorați importanța elementelor fundamentale ale rețelelor, inclusiv modelul OSI, topologiile de rețea și diversele tipuri de rețele, pentru construirea unor infrastructuri eficiente și fiabile."
genre: ["Tehnologie", "Rețea", "Infrastructura IT", "Arhitectura de rețea", "Informatică", "Comunicarea datelor", "Tehnologia informației", "Securitatea rețelelor", "Managementul rețelei", "Internet"]
tags: ["fundamentele rețelelor", "Modelul OSI", "topologii de rețea", "tipuri de rețele", "încapsularea datelor", "straturi de rețea", "topologie de plasă", "topologie în stea", "topologie bus", "topologie în inel", "topologie hibridă", "rețea peer-to-peer", "rețea client-server", "LAN", "MAN", "WAN", "WLAN", "PAN", "CAN", "SAN", "SDWAN", "MPLS", "mGRE", "vSwitch", "vNIC", "NFV", "hipervizor", "legături prin satelit", "DSL", "internet prin cablu", "linie închiriată", "metro-optic"]
cover: "/img/cover/A_symbolic_illustration_of_interconnected_nodes.png"
coverAlt: "O ilustrare simbolică a nodurilor interconectate care formează o rețea."
coverCaption: "Dezlănțuirea puterii noțiunilor de bază ale rețelelor."
---

#### [Click Here to Return To the Network Plus Course Page](/network-plus-start)

Bazele rețelelor joacă un rol crucial în lumea interconectată de astăzi. Fie că este vorba de navigarea pe internet, de trimiterea de e-mailuri sau de streaming video, toate aceste activități se bazează pe o infrastructură de rețea robustă. În acest articol, vom oferi o prezentare generală a **fundamentelor de rețea**, începând cu conceptele **modeluluiOSI** și **capsulării**. De asemenea, vom explora diferite **topologii de rețea** și caracteristicile acestora.

## Prezentare generală a modelului OSI și a conceptelor de încapsulare

Modelul **OSI (Open Systems Interconnection)** este un cadru conceptual care definește funcțiile unei rețele în șapte straturi diferite. Fiecare strat are responsabilități specifice și interacționează cu straturile de deasupra și de sub el. Înțelegerea modelului OSI este esențială pentru a înțelege modul în care sunt transmise și procesate datele într-o rețea.

### Modelul OSI Straturi

{{< youtube id="G7aVKgGUe9c" >}}

1. **Nivelul 1 - fizic**: Nivelul fizic se ocupă de transmiterea și recepția efectivă a fluxurilor de biți brute pe suporturi fizice, cum ar fi firele de cupru, cablurile de fibră optică sau conexiunile fără fir.

2. **Livelul 2 - Legătura de date**: Stratul de legătură de date este responsabil de stabilirea și terminarea conexiunilor între dispozitivele de rețea. De asemenea, se ocupă de detectarea și corectarea erorilor pentru a asigura o transmisie fiabilă a datelor.

3. **Nivelul 3 - Rețea**: Stratul rețea facilitează rutarea pachetelor de date de la sursă la destinație prin mai multe noduri de rețea. Acesta abordează probleme legate de **congestia rețelei**, **rutarea pachetelor** și **adresarea IP**.

4. **Cercul 4 - Transport**: Stratul de transport asigură **livrarea datelor de la un capăt la altul** și stabilește o comunicare fiabilă între sursă și destinație. Acesta gestionează **segmentarea datelor**, **controlul fluxului** și **recuperarea erorilor**.

5. **Cercul 5 - Sesiune**: Stratul de sesiune stabilește, menține și termină sesiunile de comunicare între aplicații. Acesta gestionează **controlul dialogului** și **sincronizarea** între dispozitive.

6. **Cercul 6 - Prezentare**: Stratul de prezentare se concentrează pe **sintaxa** și **semantica** informațiilor schimbate între aplicații. Acesta se ocupă de **criptarea** datelor**, **comprimarea** și **formatul** pentru o interpretare corectă.

7. **Cercul 7 - Aplicație**: Stratul de aplicații reprezintă aplicațiile și serviciile de rețea reale utilizate de utilizatorii finali. Acesta furnizează servicii precum **curierul electronic**, **transferul de fișiere**, **navigarea pe internet** și **accesul la distanță**.

{{< inarticle-dark >}}

### Încapsularea și decapsularea datelor în cadrul contextului modelului OSI

{{< youtube id="_fPzeQ9PHhA" >}}

Încapsularea datelor este procesul de adăugare a antetelor și a remorcilor specifice protocolului la încărcătura utilă la fiecare nivel al modelului OSI. Această încapsulare permite datelor să traverseze rețeaua și să ajungă la destinația dorită. În schimb, decapsularea presupune eliminarea antetelor și a remorcilor adăugate în fiecare strat al modelului OSI pentru a extrage încărcătura utilă originală.

În contextul modelului OSI, următoarele elemente contribuie la încapsularea și decapsularea datelor:

- **Eheader Ethernet**: Antetul Ethernet conține informații precum adresele MAC ale dispozitivelor sursă și destinație, tipul de protocol Ethernet și mecanismele de verificare a erorilor.

- **În antetul protocolului Internet (IP)**: Antetul IP include adresele IP sursă și destinație, identificarea pachetului, time-to-live și alți parametri esențiali pentru comunicarea bazată pe IP.

- **Capitoletul Protocolului de control al transmisiunii (TCP)/Protocolul de control al datelor de utilizator (UDP)**: Capetele TCP și UDP conțin numere de port, numere de secvență, sume de control și alte informații relevante necesare pentru comunicarea la nivelul de transport.

- **TCP Flags**: Stegulețele TCP indică funcții de control și opțiuni specifice în timpul unei sesiuni TCP. Acestea includ indicatori pentru stabilirea conexiunilor, confirmarea datelor, terminarea conexiunilor și altele.

- **Payload**: Încărcătura utilă este reprezentată de datele efective care sunt transmise, cum ar fi o pagină web, un mesaj de e-mail sau un fișier media.

- **Unitatea maximă de transmisie (MTU)**: MTU reprezintă dimensiunea maximă a unui pachet de date care poate fi transmis printr-o rețea fără fragmentare.

{{< inarticle-dark >}}

## Explorarea topologiilor de rețea și a caracteristicilor acestora

{{< youtube id="zbqrNg4C98U" >}}

Topologiile de rețea definesc dispunerea fizică sau logică a dispozitivelor de rețea și interconexiunile dintre acestea. Fiecare topologie are propriile puncte forte și puncte slabe, iar alegerea topologiei potrivite depinde de diverși factori, cum ar fi scalabilitatea, toleranța la erori și costul.

### Topologie de tip plasă

Într-o **topologie de tip plasă**, fiecare dispozitiv este conectat la fiecare alt dispozitiv, formând o rețea complet interconectată. Această redundanță asigură o toleranță ridicată la erori, dar poate fi costisitoare și complexă de implementat. Topologiile de tip plasă sunt utilizate în mod obișnuit în infrastructurile critice și în mediile de calcul de înaltă performanță.

### Topologia stea/module și rază

Într-o **topologie în stea**, toate dispozitivele sunt conectate la un hub sau la un comutator central. Hub-ul acționează ca un punct central de conectare, facilitând comunicarea între dispozitive. Această topologie este ușor de gestionat și oferă un control centralizat, dar poate crea un singur punct de eșec în cazul în care hub-ul cedează.

### Topologia Bus

Într-o **topologie de bus**, toate dispozitivele sunt conectate la o singură linie de comunicare, numită bus. Datele sunt transmise secvențial de-a lungul autobuzului, iar dispozitivele primesc datele care le sunt destinate. Topologiile de tip bus sunt simple și rentabile, dar pot suferi congestii de rețea și au o scalabilitate limitată.

### Topologie în inel

Într-o **topologie în inel**, dispozitivele sunt conectate într-un lanț circular, fiecare dispozitiv fiind conectat la următorul, iar ultimul dispozitiv se conectează înapoi la primul. Datele circulă într-o singură direcție în jurul inelului. Topologiile în inele oferă un acces echitabil și pot gestiona sarcini mari de trafic, dar pot suferi de întreruperi ale rețelei în cazul în care un dispozitiv cedează.

### Topologie hibridă

O **topologie hibridă** combină mai multe topologii pentru a forma o rețea mai flexibilă și mai scalabilă. De exemplu, o combinație de topologii în stea și în inel poate oferi redundanță și toleranță la erori, menținând în același timp scalabilitatea.

## Tipuri și caracteristici ale rețelelor

{{< youtube id="6a-roIeJ_a4" >}}

Rețelele cuprind diferite tipuri de rețele, fiecare dintre ele răspunzând unor nevoi și cazuri de utilizare specifice. Iată câteva tipuri comune de rețele:

### Rețeaua peer-to-Peer (P2P)

Într-o **rețea peer-to-peer (P2P)**, dispozitivele se conectează direct între ele fără a se baza pe un server centralizat. Rețelele P2P sunt adesea utilizate pentru partajarea fișierelor, aplicații colaborative și sisteme descentralizate.

### Rețea client-server

O **rețea client-server** implică clienți, care solicită servicii sau resurse, și servere, care furnizează aceste servicii sau resurse. Rețelele client-server sunt utilizate pe scară largă în mediile de întreprindere, unde controlul centralizat și gestionarea resurselor sunt esențiale.

### Rețea locală (LAN)

O **rețea locală (LAN)** se întinde pe o zonă geografică mică, cum ar fi o clădire de birouri sau o casă. Ea permite dispozitivelor din cadrul rețelei să comunice și să partajeze resurse. LAN-urile sunt utilizate în mod obișnuit pentru comunicarea internă, partajarea fișierelor și a imprimantelor.

### Metropolitan Area Network (MAN)

O **rețea de zonă metropolitană (MAN)** acoperă o zonă geografică mai mare decât o rețea LAN, dar mai mică decât o rețea WAN. Aceasta conectează mai multe LAN-uri în cadrul unui oraș sau al unei regiuni metropolitane. MAN-urile sunt adesea utilizate de organizațiile care au nevoie de conectivitate de mare viteză între sucursalele sau campusurile lor.

### Wide Area Network (WAN)

O **rețea WAN (Wide Area Network) ** se întinde pe o zonă geografică mare, conectând mai multe LAN sau MAN din orașe, țări sau continente diferite. WAN-urile se bazează pe diverse tehnologii de comunicare, cum ar fi liniile închiriate, sateliții și rețelele optice, pentru a transmite date pe distanțe mari.

### Rețea locală fără fir (WLAN)

O **rețea locală fără fir (WLAN)** oferă conectivitate fără fir într-o zonă limitată, folosind de obicei tehnologia Wi-Fi. WLAN-urile se găsesc în mod obișnuit în case, birouri, cafenele și spații publice, permițând utilizatorilor să își conecteze dispozitivele fără cabluri fizice.

### Personal Area Network (PAN)

O **rețea de zonă personală (PAN)** acoperă o zonă restrânsă, de obicei în spațiul de lucru al unei persoane sau în împrejurimile imediate. Aceasta permite comunicarea între dispozitivele personale, cum ar fi smartphone-urile, tabletele și dispozitivele purtabile.

### Campus Area Network (CAN)

O **rețea de zonă de campus (CAN)** este o rețea care se întinde pe teritoriul unui campus universitar sau al unei mari corporații. Aceasta oferă conectivitate la diverse clădiri și facilități din zona campusului, facilitând comunicarea și partajarea resurselor.

### Storage Area Network (SAN)

O **rețea de stocare (SAN)** este o rețea specializată concepută în scopuri de stocare. Aceasta permite mai multor servere să acceseze resurse de stocare partajate, cum ar fi matricele de discuri sau bibliotecile de benzi, printr-o conexiune de mare viteză.

### Software-Defined Wide Area Network (SDWAN)

**Software-Defined Wide Area Network (SDWAN)** este o tehnologie care simplifică gestionarea și configurarea rețelelor WAN prin separarea planului de control al rețelei de hardware-ul de bază. Aceasta oferă un control centralizat și permite organizațiilor să își gestioneze în mod dinamic infrastructura WAN.

### Multiprotocol Label Switching (MPLS)

**Multiprotocol Label Switching (MPLS)** este o tehnică de rutare care utilizează etichete pentru a redirecționa eficient pachetele de date într-o rețea. Oferă comunicații de înaltă performanță, fiabile și sigure, ceea ce o face potrivită pentru furnizorii de servicii și întreprinderi.

### Multipoint Generic Routing Encapsulation (mGRE)

**Multipoint Generic Routing Encapsulation (mGRE)** este o tehnică utilizată pentru a crea rețele private virtuale (VPN) prin încapsularea pachetelor de date și trimiterea lor printr-o rețea multipunct. Aceasta permite o comunicare eficientă între mai multe site-uri sau puncte finale.

{{< inarticle-dark >}}

## Concepte de rețea virtuală

{{< youtube id="A29g5-Os-u8" >}}

Tehnologiile de virtualizare au revoluționat modul în care sunt proiectate și gestionate rețelele. Iată câteva concepte de rețea virtuală:

### vSwitch

Un **vSwitch**, sau comutator virtual, este un comutator de rețea bazat pe software care funcționează într-un mediu virtualizat, cum ar fi un hipervizor. Acesta permite comunicarea între mașinile virtuale (VM) și le conectează la rețeaua fizică.

### Carte de interfață de rețea virtuală (vNIC)

O **carte de interfață de rețea virtuală (vNIC)** este o placă de interfață de rețea virtualizată care emulează un adaptor de rețea fizic în cadrul unei mașini virtuale. Aceasta permite mașinilor virtuale să comunice cu comutatorul virtual și cu rețeaua fizică.

### Virtualizarea funcțiilor de rețea (NFV)

**Network Function Virtualization (NFV)** este o abordare care virtualizează funcțiile de rețea, cum ar fi firewall-urile, routerele și balanserii de sarcină, prin rularea acestora pe servere standard în locul dispozitivelor hardware dedicate. Aceasta oferă flexibilitate, scalabilitate și economii de costuri în infrastructura de rețea.

### Hypervisor

Un **hipervizor** este un strat software care permite crearea și gestionarea mașinilor virtuale. Acesta asigură abstractizarea hardware, permițând rularea mai multor mașini virtuale pe un singur server fizic.

## Legături cu furnizorii

{{< youtube id="M2cJtZXJrpE" >}}

Legăturile furnizorilor se referă la diferitele tipuri de opțiuni de conectivitate oferite de furnizorii de servicii. Iată câteva linkuri de furnizor comune:

### Satelit

**Legăturile prin satelit** utilizează sateliți de comunicații pentru a transmite date pe distanțe mari. Acestea sunt adesea utilizate în zone îndepărtate, unde alte opțiuni de conectivitate sunt limitate.

### Digital Subscriber Line (DSL)

**Digital Subscriber Line (DSL)** este o tehnologie care oferă acces la internet de mare viteză prin intermediul liniilor telefonice existente. Oferă viteze mai mari decât conexiunile dial-up tradiționale și este disponibilă pe scară largă în mediile rezidențiale și de afaceri.

### Cablu

**Internetul prin cablu** utilizează aceleași cabluri coaxiale folosite pentru televiziunea prin cablu pentru a oferi acces la internet de mare viteză. Este popular în zonele rezidențiale și oferă viteze mai rapide în comparație cu DSL.

### Leased Line

O **linie închiriată** este o conexiune dedicată, punct-la-punct, între două locații. Oferă o conectivitate fiabilă și sigură, ceea ce o face potrivită pentru întreprinderile cu cerințe mari de lățime de bandă.

### Metro-Optical

Rețelele **Metro-optice** utilizează tehnologia fibrei optice pentru a oferi conectivitate de mare viteză în cadrul unei zone metropolitane. Acestea oferă o lățime de bandă mare și o latență redusă, fiind ideale pentru aplicațiile cu utilizare intensivă a datelor.

______

În concluzie, înțelegerea fundamentelor rețelelor este crucială pentru construirea și menținerea unor infrastructuri de rețea fiabile și eficiente. Modelul **OSI** oferă un cadru pentru înțelegerea modului în care datele sunt transmise și procesate pe diferite straturi de rețea. În plus, cunoașterea **topologiilor de rețea** ajută la proiectarea rețelelor care îndeplinesc cerințe specifice de scalabilitate, toleranță la erori și eficiență a costurilor. Prin familiarizarea cu diferite **tipuri de rețele**, **concepte de rețea virtuală** și **legături de furnizor**, putem lua decizii în cunoștință de cauză atunci când configurăm și gestionăm rețele.

Referințe:
- [OSI Model - Cisco](https://learningnetwork.cisco.com/s/article/osi-model-reference-chart)
- [How Does the Internet Work? - Stanford University](https://web.stanford.edu/class/msande91si/www-spr04/readings/week1/InternetWhitepaper.htm)
