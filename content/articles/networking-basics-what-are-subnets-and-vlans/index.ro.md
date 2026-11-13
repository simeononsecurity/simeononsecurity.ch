---
title: "Noțiuni de bază despre rețele: subrețele, împărțire în subrețele și proiectarea VLAN"
draft: false
toc: true
date: 2023-07-23
lastmod: 2026-11-13
description: "Învață bazele subrețelelor, subnetării și VLAN-urilor pentru administrarea eficientă și securizarea rețelelor."
genre: ["Noțiuni de bază despre rețele", "Împărțire în subrețele", "VLAN-uri", "Administrarea rețelei", "Securitatea rețelei", "Adresare IP", "Segmentarea rețelei", "Utilizarea eficientă a resurselor", "Performanța rețelei", "IPv4"]
tags: ["noțiuni de bază despre rețele", "subrețele", "împărțire în subrețele", "VLAN-uri", "administrarea rețelei", "securitatea rețelei", "adresare IP", "segmentarea rețelei", "utilizarea eficientă a resurselor", "performanța rețelei", "IPv4", "configurarea subrețelei", "măști de subrețea", "alocarea adreselor IP", "comunicare între VLAN-uri", "porturi switch", "configurare VLAN", "interfețe VLAN", "conectivitate de rețea", "rețele subdivizate", "domenii de broadcast", "măsuri de securitate", "interval de adrese IP", "exemple de subrețele", "implementare VLAN", "administrarea rețelelor", "configurare switch", "configurare router", "scalabilitatea rețelei", "comunicare și transfer de date", "rețele eficiente"]
cover: "/img/cover/A_symbolic_illustration_of_interconnected_comp.webp"
coverAlt: "Ilustrație simbolică a rețelelor de calculatoare interconectate, cu subrețele și VLAN-uri"
coverCaption: "Rețele eficiente: subrețelele și VLAN-urile explicate simplu."
---

## Noțiuni de bază despre rețele: subrețele, împărțire în subrețele și proiectarea VLAN

### Introducere

În lumea conectată de astăzi, rețelele de calculatoare sunt esențiale pentru comunicare și transferul de date. Noțiunile de bază despre rețele sunt utile specialiștilor IT și utilizatorilor. Acest articol prezintă subrețelele, subnetarea și VLAN-urile, precum și scopul și funcționarea lor.

## Subrețele: explicație detaliată

### Ce este o subrețea?

{{< youtube id="nR5xCmXJE5E" >}}

O **subrețea** este o subdiviziune logică a unei rețele IP. Administratorul poate împărți o rețea mare în segmente mai mici, mai ușor de gestionat. Fiecare subrețea are propriul interval de adrese IP, ceea ce ajută la folosirea eficientă a adreselor disponibile.

### De ce să folosești subrețele?

Rețelele folosesc subrețele din mai multe motive:

1. **Segmentarea rețelei:** Subrețelele împart o rețea mare în rețele mai mici. Astfel cresc performanța și scade congestia.

2. **Securitate sporită:** Separarea dispozitivelor în subrețele diferite permite folosirea firewall-urilor și a listelor de control al accesului pentru gestionarea traficului.

3. **Folosirea eficientă a resurselor:** Subnetarea alocă mai bine adresele IP, o resursă limitată în IPv4.

### Cum se creează subrețele?

{{< youtube id="LdSAaSHfK3M" >}}

Subnetarea împarte o rețea în subrețele mai mici. Urmează acești pași:

1. **Stabilește cerințele rețelei:** Determină numărul de subrețele și de gazde necesare în fiecare.

2. **Alege schema de adresare IP:** Selectează o schemă potrivită pentru numărul de subrețele și gazde necesare.

3. **Calculează măștile de subrețea:** Determină măștile în funcție de numărul necesar de subrețele și gazde.

4. **Alocă adrese IP:** Alocă adrese fiecărei subrețele și verifică intervalul corespunzător.

5. **Testează și verifică:** Testează conectivitatea și verifică alocările adreselor IP.

### Exemple de împărțire în subrețele

Să analizăm un exemplu simplu de împărțire în subrețele:

Să presupunem că avem intervalul IP 192.168.0.0/24 și dorim să creăm patru subrețele cu același număr de gazde. Împărțim rețeaua astfel:

1. **Pasul 1: Stabilește cerințele rețelei:** Avem nevoie de patru subrețele cu același număr de gazde.

2. **Pasul 2: Alege schema de adresare IP:** Alegem o mască /26, care oferă 64 de adrese pentru fiecare subrețea.

3. **Pasul 3: Calculează măștile de subrețea:** Masca /26 este 255.255.255.192.

4. **Pasul 4: Alocă adrese IP:** Alocăm subrețelelor următoarele adrese:

   - subrețea 1: 192.168.0.0/26
   - subrețea 2: 192.168.0.64/26
   - subrețea 3: 192.168.0.128/26
   - subrețea 4: 192.168.0.192/26

5. **Pasul 5: Testează și verifică:** Verificăm conectivitatea între dispozitivele din fiecare subrețea.

### Tabele utile de împărțire în subrețele

#### Tabel de referință pentru calcularea subrețelelor

| Mască de subrețea | Notație CIDR | Număr total de adrese IP | Adrese IP utilizabile |
|-------------|---------------|--------------------|---------------------|
| /30 | 255.255.255.252 | 4 | 2 |
| /29 | 255.255.255.248 | 8 | 6 |
| /28 | 255.255.255.240 | 16 | 14 |
| /27 | 255.255.255.224 | 32 | 30 |
| /26 | 255.255.255.192 | 64 | 62 |
| /25 | 255.255.255.128 | 128 | 126 |
| /24 | 255.255.255.0 | 256 | 254 |
| /23 | 255.255.254.0 | 512 | 510 |
| /22 | 255.255.252.0 | 1,024 | 1,022 |
| /21 | 255.255.248.0 | 2,048 | 2,046 |
| /20 | 255.255.240.0 | 4,096 | 4,094 |
| /19 | 255.255.224.0 | 8,192 | 8,190 |
| /18 | 255.255.192.0 | 16,384 | 16,382 |
| /17 | 255.255.128.0 | 32,768 | 32,766 |
| /16 | 255.255.0.0 | 65,536 | 65,534 |
| /15 | 255.254.0.0 | 131,072 | 131,070 |
| /14 | 255.252.0.0 | 262,144 | 262,142 |
| /13 | 255.248.0.0 | 524,288 | 524,286 |
| /12 | 255.240.0.0 | 1,048,576 | 1,048,574 |
| /11 | 255.224.0.0 | 2,097,152 | 2,097,150 |
| /10 | 255.192.0.0 | 4,194,304 | 4,194,302 |
| /9 | 255.128.0.0 | 8,388,608 | 8,388,606 |
| /8 | 255.0.0.0 | 16,777,216 | 16,777,214 |
| /7 | 254.0.0.0 | 33,554,432 | 33,554,430 |
| /6 | 252.0.0.0 | 67,108,864 | 67,108,862 |
| /5 | 248.0.0.0 | 134,217,728 | 134,217,726 |
| /4 | 240.0.0.0 | 268,435,456 | 268,435,454 |
| /3 | 224.0.0.0 | 536,870,912 | 536,870,910 |
| /2 | 192.0.0.0 | 1,073,741,824 | 1,073,741,822 |
| /1 | 128.0.0.0 | 2,147,483,648 | 2,147,483,646 |
| /0 | 0.0.0.0 | 4,294,967,296 | 4,294,967,294 |

#### Tabelul subrețelelor utilizabile

| Notație CIDR | Număr de subrețele utilizabile |
|---------------|-------------------------|
| /0 | 1 |
| /1 | 2 |
| /2 | 4 |
| /3 | 8 |
| /4 | 16 |
| /5 | 32 |
| /6 | 64 |
| /7 | 128 |
| /8 | 256 |
| /9 | 512 |
| /10 | 1024 |
| /11 | 2048 |
| /12 | 4096 |
| /13 | 8192 |
| /14 | 16384 |
| /15 | 32768 |
| /16 | 65536 |
| /17 | 131072 |
| /18 | 262144 |
| /19 | 524288 |
| /20 | 1048576 |
| /21 | 2097152 |
| /22 | 4194304 |
| /23 | 8388608 |
| /24 | 16777216 |
| /25 | 33554432 |
| /26 | 67108864 |
| /27 | 134217728 |
| /28 | 268435456 |
| /29 | 536870912 |
| /30 | 1073741824 |
| /31 | 2147483648 |
| /32 | 4294967296 |

#### Tabelul puterilor lui doi

| Puterea lui doi | Valoare |
|--------------|-------|
| 2^32 | 4294967296 |
| 2^31 | 2147483648 |
| 2^30 | 1073741824 |
| 2^29 | 536870912 |
| 2^28 | 268435456 |
| 2^27 | 134217728 |
| 2^26 | 67108864 |
| 2^25 | 33554432 |
| 2^24 | 16777216 |
| 2^23 | 8388608 |
| 2^22 | 4194304 |
| 2^21 | 2097152 |
| 2^20 | 1048576 |
| 2^19 | 524288 |
| 2^18 | 262144 |
| 2^17 | 131072 |
| 2^16 | 65536 |
| 2^15 | 32768 |
| 2^14 | 16384 |
| 2^13 | 8192 |
| 2^12 | 4096 |
| 2^11 | 2048 |
| 2^10 | 1024 |
| 2^9 | 512 |
| 2^8 | 256 |
| 2^7 | 128 |
| 2^6 | 64 |
| 2^5 | 32 |
| 2^4 | 16 |
| 2^3 | 8 |
| 2^2 | 4 |
| 2^1 | 2 |
| 2^0 | 1 |

## VLAN-uri: rețele locale virtuale

### Ce este un VLAN?

{{< youtube id="jC6MJTh9fRE" >}}

Un **VLAN (Virtual Local Area Network)** este un grup logic de dispozitive dintr-o rețea, indiferent de poziția fizică. VLAN-urile creează domenii de broadcast separate și sporesc flexibilitatea, securitatea și scalabilitatea rețelei.

### De ce să folosești VLAN-uri?

VLAN-urile oferă mai multe beneficii pentru administrarea rețelei:

1. **Securitate sporită:** VLAN-urile izolează datele sensibile și limitează accesul neautorizat. Traficul rămâne în segmente specifice, protejând resursele importante.

2. **Performanță mai bună:** VLAN-urile separă logic traficul, reduc congestia și îmbunătățesc performanța. Traficul broadcast rămâne în VLAN.

3. **Administrare simplificată:** VLAN-urile grupează dispozitivele după funcție, departament sau alt criteriu logic, simplificând administrarea și configurarea.

### Configurarea VLAN-urilor

Configurarea unui VLAN urmează, de obicei, acești pași:

1. **Identifică cerințele VLAN:** Stabilește scopul și domeniul implementării. Identifică dispozitivele și apartenența lor la VLAN-uri.

2. **Alocă ID-uri VLAN:** Atribuie fiecărui VLAN un ID unic. ID-urile sunt de obicei între 1 și 4094, iar unele sunt rezervate.

3. **Configurează porturile switch-ului:** Atribuie porturile VLAN-urilor potrivite ca porturi access sau trunk.

4. **Configurează interfețele VLAN:** Dacă este necesară comunicarea între VLAN-uri, [configurează interfețele VLAN](https://simeononsecurity.com/network-plus/ethernet-switching-vlans-port-configurations-security/) pe un switch de nivel 3 sau router.

5. **Testează și verifică:** Testează conectivitatea dintre dispozitivele din fiecare VLAN.

### Tabelul VLAN-urilor rezervate

| Etichete VLAN | Descriere |
|-------------------|----------------------------------------------------|
| VLAN 0 | ID VLAN rezervat, nu trebuie folosit |
| VLAN 1 | VLAN implicit pentru multe dispozitive de rețea |
| VLAN 2 | VLAN implicit pentru traficul de administrare |
| VLAN 3-4 | ID-uri VLAN rezervate |
| VLAN 5 | Rezervat pentru ID-ul VLAN Token Ring |
| VLAN 6-1001 | ID-uri VLAN rezervate |
| VLAN 1002-1005 | VLAN-uri implicite Cisco pentru scopuri specifice |
| VLAN 1006-1024 | ID-uri VLAN rezervate |
| VLAN 1025-4094 | Rezervat pentru intervalul VLAN extins |
| VLAN 4095 | ID VLAN rezervat, nu trebuie folosit |

## Concluzie

[Înțelegerea subrețelelor](https://simeononsecurity.com/articles/networking-basics-what-is-a-switch-router-gateway-subnet-firewall-and-dmz/) și a VLAN-urilor este esențială pentru proiectarea și administrarea rețelelor eficiente. Subrețelele segmentează rețeaua și îmbunătățesc performanța și securitatea. VLAN-urile grupează logic dispozitivele și simplifică gestionarea. Urmând acești pași, administratorii pot împărți rețelele și configura VLAN-uri conform cerințelor.

Noțiunile de bază despre rețele formează fundația unor rețele robuste și scalabile, potrivite comunicării și transferului modern de date.

## Referințe

- [Noțiuni de bază despre subnetting](https://www.cisco.com/c/en/us/support/docs/ip/routing-information-protocol-rip/13788-3.html)
- [Înțelegerea și configurarea VLAN-urilor](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst4500/12-2/25ew/configuration/guide/conf/vlans.pdf)
- [Standardul IEEE 802.1Q](https://standards.ieee.org/standard/802_1Q-2018.html)
