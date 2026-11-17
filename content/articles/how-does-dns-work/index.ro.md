---
title: "Cum funcționează DNS: DNS root, importanță și depanare"
draft: false
toc: true
date: 2023-07-20
lastmod: 2026-11-13
description: "Află cum funcționează DNS și DNS root, ierarhia lor, procesul de rezolvare, memorarea în cache și depanarea."
genre: ["Noțiuni de bază DNS", "DNS root", "Sistemul de nume de domeniu", "Rezolvare DNS", "Ierarhia DNS", "Memorare DNS în cache", "Depanare DNS", "Înregistrări DNS", "Administrare DNS", "Comenzi DNS"]
tags: ["DNS", "DNS root", "Sistemul de nume de domeniu", "Rezolvare DNS", "Ierarhia DNS", "Memorare DNS în cache", "Înregistrări DNS", "Administrare DNS", "Depanare DNS", "rețelistică", "infrastructura Internetului", "adrese IP", "acces la site-uri", "interogare recursivă", "servere de nume autoritative", "TTL", "mecanisme de cache", "golirea cache-ului DNS", "servere DNS root", "rutare anycast", "ICANN", "cooperare DNS", "înregistrare A", "înregistrare AAAA", "înregistrare CNAME", "înregistrare MX", "înregistrare TXT", "înregistrare SRV", "înregistrare NS", "înregistrare PTR", "înregistrare SOA", "comenzi de depanare DNS", "Windows", "macOS", "Linux", "Linie de comandă", "terminal de sistem"]
cover: "/img/cover/An_image_depicting_interconnected_computer_ne.webp"
coverAlt: "Imagine cu rețele de calculatoare interconectate, nume de domenii și adrese IP, care ilustrează funcționarea DNS și DNS root."
coverCaption: "Înțelege DNS și stăpânește sistemul de nume de domeniu"
---

## Cum funcționează DNS și DNS root

### Introducere

Domain Name System (DNS) este o parte importantă a infrastructurii Internetului. Permite accesarea site-urilor cu nume de domenii în loc de adrese IP. DNS funcționează ca o agendă telefonică și transformă numele de domenii lizibile pentru oameni în adrese IP înțelese de calculatoare. DNS root este nucleul ierarhic și distribuit care participă la rezolvarea numelor. Acest articol explică DNS, DNS root și înregistrările asociate unui domeniu.

{{< youtube id="mpQZVYPuDGU" >}}

## Domain Name System (DNS)

**Domain Name System (DNS)** este un sistem descentralizat de denumire care asociază nume de domenii cu adrese IP. Poți accesa site-uri și alte resurse de pe Internet introducând un nume în browser. DNS te scutește de memorarea adreselor IP complexe.

### Ierarhia DNS

DNS funcționează într-o structură ierarhică formată din mai multe niveluri. În partea de sus se află zona rădăcină, urmată de domeniile de nivel superior (TLD), domeniile de nivelul al doilea și subdomenii. Fiecare nivel contribuie la numele complet. În `www.example.com`, „www” este subdomeniul, „example” este domeniul de nivelul al doilea, iar „com” este TLD-ul.

### Procesul de rezolvare DNS

Când introduci un nume de domeniu în browser, începe rezolvarea DNS. Browserul trimite o interogare către un rezolvitor DNS, furnizat de obicei de furnizorul de Internet (ISP). Rezolvitorul parcurge mai multe etape pentru a găsi adresa IP asociată numelui.

1. **Cache DNS local**: rezolvitorul caută mai întâi în cache-ul local numele și adresa IP solicitate. Dacă găsește datele, returnează rezultatul fără alte interogări.

2. **Interogare recursivă**: dacă datele lipsesc din cache, rezolvitorul pornește o interogare recursivă. Contactează mai întâi serverele DNS root, responsabile pentru zona „.” (punct). Acestea returnează adresele IP ale serverelor TLD pentru domeniul solicitat.

3. **Interogare TLD**: rezolvitorul contactează serverele TLD identificate anterior și cere adresele IP ale serverelor de nume autoritative pentru domeniu.

4. **Interogare către serverul de nume autoritativ**: rezolvitorul interoghează serverele autoritative furnizate de serverele TLD. Acestea păstrează înregistrările autoritative ale domeniului și returnează adresa IP asociată numelui.

5. **Răspuns către client**: rezolvitorul primește adresa IP de la serverele autoritative și o trimite browserului. Apoi browserul se poate conecta la serverul web folosind adresa primită.

### Memorarea DNS în cache

Rezolvoarele DNS folosesc cache-ul pentru a îmbunătăți performanța și a reduce încărcarea serverelor DNS. După primirea unui răspuns, rezolvitorul salvează local asocierea dintre numele domeniului și adresa IP. Interogările ulterioare pentru același nume pot primi răspuns din cache, fără parcurgerea ierarhiei DNS.

Cache-ul funcționează la mai multe niveluri: rezolvitorul local, cel al ISP-ului și dispozitive precum routerele și sistemele de operare. Valoarea Time-to-Live (TTL) din răspunsul DNS stabilește cât timp rămâne o înregistrare în cache. Când expiră TTL-ul, rezolvitorul șterge înregistrarea și face o nouă interogare.

#### Golirea cache-ului DNS local

Golirea cache-ului DNS ajută la rezolvarea unor probleme și permite sistemului să obțină înregistrările actualizate. Iată pașii pentru diferite sisteme de operare:

##### Windows

Pentru a goli cache-ul DNS în Windows:

1. Apasă `Win + R`, scrie `cmd` și apasă Enter pentru a deschide Linia de comandă.

2. Introdu comanda următoare și apasă Enter:

```bash
ipconfig /flushdns
```

Comanda golește cache-ul rezolvitorului DNS din Windows.

##### macOS

Pentru a goli cache-ul DNS în macOS:

1. Deschide Terminal din Aplicații > Utilitare sau caută-l cu Spotlight.

2. Introdu comanda următoare în Terminal și apasă Enter:

```bash
sudo killall -HUP mDNSResponder
```

Comanda repornește procesul mDNSResponder, care se ocupă de rezolvarea DNS în macOS.

##### Linux

Metoda de golire a cache-ului DNS în Linux depinde de distribuție și de rezolvitorul folosit. Iată două metode comune:

1. **Sisteme bazate pe systemd (de exemplu, Ubuntu și Fedora)**:

Deschide Terminal și rulează comanda următoare cu drepturi de administrator:

```bash
sudo systemd-resolve --flush-caches

```

Comanda golește cache-ul DNS pe sistemele care folosesc systemd-resolved ca rezolvitor.

2. **Sisteme fără systemd**:

Deschide Terminal și rulează comanda următoare cu drepturi de administrator:

```bash
sudo /etc/init.d/nscd restart

```

Comanda repornește Name Service Cache Daemon (nscd), responsabil pentru cache-ul DNS în distribuțiile Linux fără systemd.

Aceștia sunt pași generali. Comenzile și metodele pot varia în funcție de versiunea sistemului de operare. Golirea cache-ului DNS poate rezolva unele probleme, dar nu toate problemele de conectivitate la rețea.

## Cum funcționează sistemul DNS root

Sistemul DNS root este o parte fundamentală a infrastructurii DNS. Iată cum funcționează:

### 1. Zona rădăcină și serverele root

Sistemul DNS root începe cu **zona rădăcină**, nivelul superior al ierarhiei DNS. Aceasta conține informații despre serverele de nume autoritative pentru toate domeniile de nivel superior (TLD), precum .com, .org, .net și domeniile naționale, precum .us și .uk.

Sistemul DNS root cuprinde 13 servere root, identificate cu literele de la A la M. Sunt distribuite geografic în lume pentru redundanță și fiabilitate.

### 2. Rutare anycast

Pentru a gestiona volumul mare de trafic DNS, serverele root folosesc **rutarea anycast**. Mai multe servere folosesc aceeași adresă IP, dar se află în locații diferite. Condițiile rețelei direcționează interogarea către serverul potrivit și distribuie încărcarea.

Când un utilizator pornește o interogare DNS, anycast o direcționează către cel mai apropiat server root disponibil. Infrastructura rețelei alege ruta cea mai scurtă în funcție de condiții. Anycast distribuie încărcarea și ajută la prevenirea blocajelor.

### 3. Rezolvoare DNS recursive

Când un rezolvitor DNS primește o interogare pentru un nume de domeniu, începe rezolvarea recursivă și contactează unul dintre serverele root.

Serverul root răspunde cu o trimitere către adresele IP ale serverelor de nume TLD responsabile pentru TLD-ul solicitat. Aceste servere conțin informații despre serverele autoritative pentru domeniile din TLD.

### 4. Trimiteri și servere de nume autoritative

După ce primește trimiterea serverului root, rezolvitorul contactează serverul de nume TLD potrivit.

Serverul TLD răspunde cu o altă trimitere, care conține adresele IP ale serverelor de nume autoritative pentru domeniul solicitat.

Apoi, rezolvitorul cere serverelor autoritative adresa IP asociată numelui de domeniu.

### 5. Cache și TTL

În timpul rezolvării DNS, cache-ul îmbunătățește performanța și reduce încărcarea serverelor. Rezolvoarele salvează asocierile dintre numele de domenii și adresele IP.

Înregistrările DNS sunt păstrate în cache pe durata stabilită de Time-to-Live (TTL). TTL-ul arată cât timp rămâne valabilă o înregistrare. Când expiră, rezolvitorul o șterge și face o nouă interogare pentru adresa IP actualizată.

### 6. Colaborare și gestionare

Sistemul DNS root este gestionat prin colaborarea dintre Internet Corporation for Assigned Names and Numbers (ICANN) și operatorii serverelor root.

ICANN supraveghează gestionarea și coordonarea generală a DNS și colaborează cu operatorii serverelor root. Împreună mențin fișierul zonei rădăcină, care conține informații despre cele 13 servere DNS root și adresele lor IP.

operatorii serverelor root asigură funcționarea și disponibilitatea serverelor root. Astfel, contribuie la stabilitatea și reziliența întregii infrastructuri DNS.

Sistemul DNS root este punctul de pornire al rezolvării DNS. Acesta asociază nume de domenii cu adrese IP și permite accesul eficient la site-uri și alte resurse de pe Internet.

#### Cele 13 servere DNS root

Cele 13 servere DNS root sunt identificate cu literele de la A la M. Fiecare server este găzduit în mai multe locații fizice pentru redundanță și toleranță la defecțiuni. Ele gestionează interogările pentru zona rădăcină, inclusiv TLD-uri precum .com, .org, .net și domenii naționale precum .us și .uk.

#### ICANN și gestionarea DNS root

Internet Corporation for Assigned Names and Numbers (**ICANN**) gestionează și coordonează DNS și alocarea adreselor IP. Colaborează cu operatorii serverelor root pentru a menține stabilitatea și securitatea DNS root. Împreună mențin fișierul zonei rădăcină, cu informații despre cele 13 servere root și adresele IP aferente.

______

## Tipuri de înregistrări DNS și scopul lor

{{< youtube id="HnUDtycXSNE" >}}

Înregistrările DNS sunt componente esențiale ale Domain Name System (DNS). Ele oferă diferite tipuri de informații asociate unui nume de domeniu. Iată câteva tipuri comune și scopurile lor:

| Tipul înregistrării | Descriere | Exemplu |
|-------------|-----------------------------------------------------------------------------|-------------------------------------------|
| A | Asociază un nume de domeniu cu o adresă IPv4. | `example.com     IN A 192.0.2.1` |
| AAAA | Asociază un nume de domeniu cu o adresă IPv6. | `example.com     IN AAAA 2001:db8::1` |
| CNAME | Asociază un alias (nume canonic) cu numele real al domeniului. | `www.example.com IN CNAME example.com` |
| MX | Indică serverele de e-mail care primesc mesaje pentru domeniu. | `example.com     IN MX 10 mail.example.com` |
| TXT | Stochează text arbitrar, adesea pentru SPF, DKIM sau verificarea domeniului. | `example.com     IN TXT "v=spf1 a mx -all"`|
| NS | Indică serverele de nume autoritative ale domeniului. | `example.com     IN NS ns1.example.com` |
| SOA | Specifică proprietățile generale ale zonei (înregistrare start of authority). | `example.com     IN SOA ns1.example.com` |
| SRV | Definește locația unui serviciu specific oferit de domeniu. | `_service._proto.example.com IN SRV 10 20 5060 target.example.com` |
| PTR | Asociază o adresă IP cu un nume de domeniu (căutare DNS inversă). | `1.2.0.192.in-addr.arpa IN PTR example.com` |

### 1. Înregistrarea A (înregistrare de adresă)

**Înregistrarea A** asociază un nume de domeniu cu o adresă IPv4. Este cel mai simplu și mai comun tip de înregistrare DNS. Când introduci un domeniu în browser, înregistrarea ajută la găsirea adresei IP a serverului web care găzduiește site-ul.

### 2. Înregistrarea AAAA (înregistrare de adresă IPv6)

**Înregistrarea AAAA** are același scop ca înregistrarea A, dar asociază domeniul cu o adresă IPv6. Odată cu tranziția la IPv6, acest tip devine tot mai important pentru conectivitatea prin rețele IPv6.

### 3. Înregistrarea CNAME (înregistrare de nume canonic)

**Înregistrarea CNAME** creează un alias sau un nume canonic pentru domeniu. Se folosește când un domeniu sau subdomeniu trebuie să indice către alt domeniu sau subdomeniu. De exemplu, poți crea un CNAME care direcționează "www" către "mywebsite.com".

### 4. Înregistrarea MX (înregistrare pentru schimbul de e-mail)

**Înregistrarea MX** specifică serverul de e-mail care primește mesajele pentru domeniu. Poți defini mai multe înregistrări MX cu priorități care stabilesc ordinea încercărilor când serverul principal nu este disponibil.

### 5. Înregistrarea TXT (înregistrare text)

**Înregistrarea TXT** stochează informații text asociate unui domeniu. Este folosită pentru verificarea domeniului, înregistrări SPF (Sender Policy Framework) pentru autentificarea e-mailurilor și informații sau note generale.

### 6. Înregistrarea SRV (înregistrare de serviciu)

**Înregistrarea SRV** definește locația unui serviciu sau a unei resurse specifice din domeniu. Este folosită pentru VoIP, mesagerie instant și aplicații care trebuie să găsească anumite servere ori servicii.

### 7. Înregistrarea NS (înregistrare de server de nume)

**Înregistrarea NS** specifică serverele de nume autoritative ale domeniului. Acestea păstrează înregistrările DNS ale domeniului. Rezolvitorul consultă înregistrările NS pentru a găsi serverele autoritative.

### 8. Înregistrarea PTR (înregistrare pointer)

**Înregistrarea PTR** asociază o adresă IP cu un nume de domeniu într-o căutare DNS inversă. Este folosită pentru verificarea identității serverelor de e-mail și pentru a ajuta la prevenirea spamului. Căutările inverse ajută la validarea autenticității serverului.

### 9. Înregistrarea SOA (înregistrare de început al autorității)

**Înregistrarea SOA** conține informații administrative despre domeniu, precum serverul de nume autoritativ principal, adresa de e-mail a administratorului și diverși parametri temporali pentru înregistrările DNS.

Acestea sunt doar câteva dintre numeroasele tipuri de înregistrări DNS. Fiecare are un scop specific și ajută la rezolvarea eficientă și precisă a numelor de domenii către resursele asociate.

______

## Comenzi de depanare DNS pentru diferite sisteme de operare

La probleme DNS, comenzile de diagnostic ajută la identificarea cauzei. Iată câteva comenzi utilizate frecvent pentru diferite sisteme de operare:

### Windows

#### 1. `ipconfig /flushdns`

Această comandă golește cache-ul DNS în Windows și poate rezolva probleme cauzate de înregistrări învechite sau incorecte. Deschide Linia de comandă și rulează comanda.

#### 2. `ipconfig /all`

`ipconfig /all` afișează informații detaliate despre interfețele de rețea Windows, inclusiv serverele DNS configurate. Comanda ajută la verificarea serverelor folosite.

### macOS

#### 1. `sudo killall -HUP mDNSResponder`

Această comandă repornește mDNSResponder în macOS, procesul responsabil pentru rezolvarea DNS. Poate actualiza setările și rezolva unele probleme. Deschide Terminal și rulează comanda cu drepturi de administrator.

#### 2. `nslookup`

`nslookup` permite interogarea înregistrărilor DNS, testarea rezolvării și verificarea conectivității la serverele DNS. În Terminal, rulează `nslookup` urmat de numele domeniului sau adresa IP pe care vrei să o verifici.

### Linux

#### 1. `systemd-resolve --flush-caches`

Pe sistemele Linux care folosesc systemd ca rezolvitor DNS, `systemd-resolve --flush-caches` golește cache-ul DNS. Poate rezolva probleme cauzate de intrări învechite. Deschide Terminal și rulează comanda cu drepturi de administrator.

#### 2. `dig`

`dig` este un instrument versatil de diagnostic DNS disponibil în Linux. Oferă informații detaliate despre interogări, răspunsuri și configurația serverelor DNS. Folosește `dig` pentru a interoga înregistrări, a testa rezolvarea și a diagnostica probleme. În Terminal, rulează `dig` urmat de domeniul sau adresa IP pe care vrei să o verifici.

Aceste comenzi ajută la diagnosticarea și rezolvarea problemelor DNS pe diferite sisteme de operare. Permit verificarea configurației DNS, a serverelor și a problemelor de conectivitate.

Comenzile și opțiunile pot varia în funcție de versiunea sistemului de operare și distribuție. Consultă documentația versiunii tale pentru detalii despre utilizare.
______


## Concluzie

Domain Name System (DNS) și DNS root au roluri esențiale în funcționarea Internetului. DNS permite accesarea site-urilor folosind nume de domenii ușor de citit, iar DNS root stă la baza întregii ierarhii DNS. Înțelegerea funcționării lor ajută la navigarea pe web și la înțelegerea infrastructurii serviciilor online.

______

## Referințe

- [DNS pe Wikipedia](https://en.wikipedia.org/wiki/Domain_Name_System)
- [Cum funcționează DNS, de la Cloudflare](https://www.cloudflare.com/learning/dns/what-is-dns/)
- [Site-ul oficial ICANN](https://www.icann.org/)
- [operatorii serverelor root](https://www.root-servers.org/)
