---
title: "Jocuri în rețeaua Helium: exploatarea vulnerabilităților cu MiddleMan și Chirp Stack Packet Multiplexer"
date: 2023-02-18
toc: true
draft: false
description: "Aflați cum să jucați rețeaua Helium exploatând vulnerabilitățile cu MiddleMan și Chirp Stack Packet Multiplexer, precum și riscurile și consecințele acestui lucru."
tags: ["Rețeaua de heliu", "Dovada de acoperire", "Intermediar", "Multiplexor de pachete Chirp Stack", "jocuri de noroc", "exploatarea vulnerabilităților", "Rețeaua LoRaWAN", "criptomoneda", "blockchain", "rețea descentralizată", "hotspot-uri", "falsificarea", "înșelăciune", "activitate ilegală", "pedepsele", "integritatea rețelei", "recompense", "actori rău intenționați", "securitatea retelei", "gazde legitime"]
cover: "/img/cover/A_cartoonish_depiction_of_a_group_of_individuals_exploiting.png"
coverAlt: "O reprezentare în desene animate a unui grup de indivizi care exploatează un balon cu heliu cu o imagine a unui gateway LoRaWAN și MiddleMan sau Chirp Stack Packet Multiplexer în fundal."
coverCaption: ""
---

**Disclaimer**:
Este important de reținut că jocul în rețeaua Helium este o activitate ilegală și lipsită de etică, care este puternic dezaprobată de comunitatea Helium și de comunitatea mai largă de criptomonede și blockchain. Jocul în rețea subminează integritatea rețelei și dăunează gazdelor legitime care oferă o acoperire valoroasă rețelei.

În plus, în timp ce utilizarea MiddleMan și Chirp Stack Packet Multiplexer pentru a exploata vulnerabilitățile din rețeaua Helium poate fi un motiv de îngrijorare, este important de reținut că aceste probleme pot fi rezolvate doar de Helium prin introducerea de gateway-uri securizate. Acest lucru ar necesita înlocuirea tuturor hotspot-urilor din rețea, ceea ce este o activitate semnificativă și poate să nu fie fezabilă. Drept urmare, comunitatea Helium trebuie să rămână vigilentă și proactivă în abordarea provocărilor pe care le reprezintă jocurile în rețea.

De asemenea, merită remarcat faptul că echipa Helium a fost conștientă de problemă de ceva timp și a luat măsuri pentru a o rezolva, dar sunt necesare mai multe măsuri pentru a rezolva problema. Comunitatea solicită să se ia măsuri reale pentru a aborda aceste vulnerabilități și pentru a se asigura că rețeaua poate continua să se extindă și să se dezvolte într-o manieră sigură și de încredere.

Scriind acest articol, sperăm să creștem gradul de conștientizare cu privire la problema jocurilor în rețeaua Helium și a utilizării MiddleMan și Chirp Stack Packet Multiplexer pentru a exploata vulnerabilitățile din sistem. Credem că, aruncând lumină asupra acestei probleme și aducându-i mai multă publicitate, comunitatea Helium și comunitatea mai largă de blockchain și criptomonede se pot reuni pentru a aborda problema și a lucra pentru o rețea mai sigură și de încredere.

Mai mult, prin evidențierea acestei probleme, sperăm să încurajăm echipa Helium să ia măsuri mai hotărâte în abordarea vulnerabilităților din rețea și să implementeze măsuri de securitate mai robuste pentru a preveni jocurile în viitor. Credem că este important ca echipa Helium să fie transparentă cu privire la eforturile lor de a aborda această problemă și să comunice cu comunitatea despre progresul lor în remedierea acestor vulnerabilități.

În cele din urmă, aducând mai multă publicitate acestei probleme, sperăm să încurajăm o mai mare conștientizare și educație cu privire la riscurile și consecințele jocurilor de noroc în rețeaua Helium. Este important ca utilizatorii să înțeleagă importanța comportamentului etic în rețea și potențialul prejudiciu care poate fi cauzat de jocuri. Lucrând împreună pentru a aborda aceste probleme, putem contribui la asigurarea creșterii continue și a succesului rețelei Helium.

În rezumat, jocul în rețeaua Helium nu este tolerat de comunitate sau de noi și încurajăm utilizatorii să acționeze în mod etic și legal atunci când participă la rețea. Deși există vulnerabilități în rețea care pot fi exploatate, este important să rămâneți vigilenți și proactivi în abordarea acestor probleme și să lucrați pentru o rețea mai sigură și mai fiabilă pentru toți utilizatorii.

# Cum să joci rețeaua Helium cu MiddleMan și Chirp Stack Packet Multiplexer
Rețeaua Helium este o rețea LoRaWAN® descentralizată care îi compensează pe cei care găzduiesc hotspot-uri fizice, recompensându-i cu jetoane Helium sau $HNT. Acest sistem este cunoscut sub numele de Proof-of-Coverage (PoC). Pe măsură ce rețeaua a crescut și gradul de conștientizare a acestui proiect a crescut, a existat un număr din ce în ce mai mare de trișori care exploatează protocolul și mecanismele de recompensă. În acest articol, vom discuta despre cum să joci rețeaua Helium folosind MiddleMan și Chirp Stack Packet Multiplexer.

## Înțelegerea problemei jocurilor în rețea cu heliu
Rețeaua Helium se bazează pe Dovada Acoperirii pentru a se asigura că hotspot-urile oferă acoperire acolo unde este nevoie. Cu toate acestea, acest sistem este vulnerabil la jocuri, spoofing, hacking și alte tipuri de comportament rău care pot dăuna rețelei. Problema jocurilor din rețeaua Helium costă gazdele legitime mii de $ HNT pe lună. Helium, Inc, împreună cu DeWi, au luat măsuri agresive la începutul anului 2022 pentru a ajuta la eliminarea acestei probleme.

## Hardware necesar
-[Dragino LPS8](https://www.ebay.com/sch/i.html?_nkw=dragino+lps8)
-[Other Lorawan Gateways that Use the Semtech Forwarder](https://amzn.to/41bcskb)
-[Raspberry Pi](https://amzn.to/3KjFCYp)
-[Other PC that can run docker images or linux software](https://amzn.to/3YkFhcj)

## Utilizarea MiddleMan pentru a juca rețeaua Helium
O modalitate de a juca rețeaua Helium este utilizarea MiddleMan. MiddleMan este un instrument software care poate fi folosit pentru a crea un hotspot fals care pare să ofere acoperire într-o anumită locație. Folosind MiddleMan, un utilizator poate crea un hotspot fals care va primi recompense pentru furnizarea de acoperire într-o anumită zonă, chiar dacă hotspot-ul nu este situat fizic în acea zonă.

Pentru a utiliza MiddleMan, un utilizator trebuie să instaleze software-ul și să creeze un hotspot fals. Utilizatorul poate configura apoi hotspot-ul pentru a raporta locația acestuia rețelei Helium folosind un instrument de falsificare GPS. Rețeaua Helium va crede că hotspot-ul fals oferă acoperire în locația specificată și va recompensa utilizatorul cu $HNT.

V-ați configura gateway-ul lorawan pentru a indica acest software și acesta manipulează valorile astfel încât toate PoC-urile primite să fie considerate valide. Utilizarea expeditorului semtech este unul dintre diferitele standarde din comunitatea LoraWAN. Remedierea problemei de manipulare ar necesita reinventarea roții și implementarea propriului protocol de la zero. Lucruri precum sumele de control și criptarea ar împiedica acest lucru să se întâmple. Dar ar îngreuna, de asemenea, furnizorilor cu hardware diferit să realizeze hotspot-uri. Ca să nu mai vorbim că este un caz de utilizare acceptat pentru a avea un miner de heliu și mai multe porți lora pentru o acoperire îmbunătățită. Deși aceasta este mai mult o problemă la nivel de întreprindere.

 -[helium-DIY-middleman](https://github.com/curiousfokker/helium-DIY-middleman)

## Folosind Chirp Stack Packet Multiplexer pentru a juca rețeaua Helium
O altă modalitate de a juca rețeaua Helium este utilizarea Chirp Stack Packet Multiplexer. Chirp Stack Packet Multiplexer este un instrument care poate fi folosit pentru a crea un hotspot virtual care poate primi pachete de la mai multe hotspot-uri fizice. Folosind Chirp Stack Packet Multiplexer, un utilizator poate crea un hotspot virtual care primește pachete de la hotspot-uri fizice în mai multe locații, ceea ce va crește recompensele câștigate.

Pentru a utiliza Chirp Stack Packet Multiplexer, un utilizator trebuie să instaleze software-ul și să îl configureze pentru a primi pachete de la hotspot-uri fizice sau gateway-uri lorawan în mai multe locații. Hotspot-ul va primi pachetele și va raporta locația acestuia rețelei Helium, care va recompensa utilizatorul cu $HNT.

Acest lucru permite accesul mai multor redirecționari și mai multe gateway-uri. Există cazuri de utilizare legitime pentru acest software în comunitatea LoraWAN, dar utilizarea lui în heliu este o zonă gri în cel mai bun caz. Depinde de cum îl folosești și de intenția ta.

Configurarea acestuia necesită câteva fișiere de configurare. Dar se poate face în 5 minute sau mai puțin.
-[chirpstack-packet-multiplexer](https://github.com/brocaar/chirpstack-packet-multiplexer)


## Riscuri și consecințe ale jocurilor în rețeaua Helium
Jocul în rețeaua Helium este o activitate riscantă și ilegală care poate avea consecințe grave. Helium, Inc, împreună cu DeWi, lucrează în mod activ pentru a detecta și a preveni jocurile în rețea, iar utilizatorii care sunt prinși jucând în rețea vor fi penalizați.

Sancțiunile pentru jocurile în rețeaua Helium pot include pierderea accesului la rețea, interzicerea permanentă a hotspot-urilor și pierderea oricărui $ HNT câștigat prin jocuri. În plus, jocul în rețeaua Helium subminează integritatea rețelei și dăunează gazdelor legitime care oferă o acoperire valoroasă rețelei.

## Concluzie
În timp ce rețeaua Helium oferă gazdelor hotspot legitime oportunități de a câștiga recompense prin Proof-of-Coverage, ea prezintă, de asemenea, o țintă atractivă pentru actorii rău intenționați care doresc să joace sistemul. Utilizarea MiddleMan și Chirp Stack Packet Multiplexer, deși nu este acceptată de Helium Inc. sau de comunitatea mai largă, este un exemplu al modului în care unii actori răi exploatează vulnerabilitățile din rețea pentru a obține recompense în detrimentul altora.

Este important ca comunitatea Helium să continue să lucreze împreună pentru a identifica și aborda jocurile în rețea, deoarece acestea amenință integritatea sistemului și subminează eforturile gazdelor legitime. Aceasta poate include eforturi pentru a dezvolta și implementa măsuri de detectare și prevenire mai sofisticate, precum și creșterea gradului de conștientizare și educare cu privire la riscurile și consecințele jocurilor de noroc în rețea.

În cele din urmă, succesul rețelei Helium depinde de dorința părților interesate de a lucra împreună pentru a construi un sistem sigur, fiabil și de încredere, care oferă valoare reală utilizatorilor săi. Rămânând vigilenți și proactivi în abordarea provocărilor reprezentate de jocurile de noroc, comunitatea poate contribui la asigurarea faptului că rețeaua Helium continuă să crească și să evolueze într-o direcție pozitivă.